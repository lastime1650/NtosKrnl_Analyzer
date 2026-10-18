# MiWsleFree

- RVA: `0x00284600`–`0x00285415` (길이 `3,605` bytes)
- VA: `0x0000000140284600`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00066944`
- 디코드: `805`개 명령, `3,605/3,605` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x002846F2` → [MiGetPagePrivilege](MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)
- `0x00284876` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x002849F9` → [MiInsertPageInFreeOrZeroedList](../33/MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)
- `0x00284AE4` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x00284C63` → [MiInsertPageInFreeOrZeroedList](../33/MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)
- `0x00284C8A` → [MiReleasePageFileInfo](MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x00284D56` → [MiConfirmPageIsZero](../33/MiConfirmPageIsZero_function_00334380.md) (function, `0x00334380`)
- `0x00284D69` → [MiRewriteTrimPteAsDemandZero](../38/MiRewriteTrimPteAsDemandZero_function_003823F4.md) (function, `0x003823F4`)
- `0x00284D76` → [MiGetContainingPageTable](../34/MiGetContainingPageTable_function_003467F0.md) (function, `0x003467F0`)
- `0x00284E72` → [MiInsertPageInFreeOrZeroedList](../33/MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)
- `0x00284EE8` → [MiPfnShareCountIsZero](../33/MiPfnShareCountIsZero_function_00330930.md) (function, `0x00330930`)
- `0x00284F6E` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x00284FA6` → [MI_READ_PTE_LOCK_FREE](MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00284FE8` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x00285000` → [MI_READ_PTE_LOCK_FREE](MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0028503F` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x0028504C` → [MiGetContainingPageTable](../34/MiGetContainingPageTable_function_003467F0.md) (function, `0x003467F0`)
- `0x0028509C` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x002850CB` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x00285116` → [MiGetPagingFileOffset](../36/MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x00285192` → [MiGetPagingFileOffset](../36/MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x002851F0` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x00285253` → [MiReleasePageFileInfo](MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x00285263` → [MiReleasePageFileInfo](MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x002852A7` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002852B6` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002852C5` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x002852E2` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002852F1` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0028531A` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0028532A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00285388` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002853B6` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002853BF` → [MiBadShareCount](../37/MiBadShareCount_function_00370EF8.md) (function, `0x00370EF8`)
- `0x002853D6` → [MiBadShareCount](../37/MiBadShareCount_function_00370EF8.md) (function, `0x00370EF8`)
- `0x0028540F` → [MiBadShareCount](../37/MiBadShareCount_function_00370EF8.md) (function, `0x00370EF8`)

### Direct callers
- [MiFreeWsleList](../24/MiFreeWsleList_function_00241168.md) at `0x002412E3`

### Static image references
- `0x002848C4` → RVA `0x00E2DC80` (`.data`; read)
- `0x00284949` → RVA `0x00010880` (`.rdata`; read)
- `0x00284997` → RVA `0x00E30088` (`.data`; read)
- `0x00284D13` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00285299` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00284600  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00284605  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0028460A  55                              push rbp
0028460B  56                              push rsi
0028460C  57                              push rdi
0028460D  41 54                           push r12
0028460F  41 55                           push r13
00284611  41 56                           push r14
00284613  41 57                           push r15
00284615  48 81 EC 90 00 00 00            sub rsp, 0x90
0028461C  4C 8B E2                        mov r12, rdx
0028461F  48 BD 00 00 00 00 80 F6 FF FF   movabs rbp, 0xfffff68000000000
00284629  49 C1 EC 09                     shr r12, 9
0028462D  45 33 ED                        xor r13d, r13d
00284630  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0028463A  44 89 AC 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r13d
00284642  4C 23 E0                        and r12, rax
00284645  49 8B D9                        mov rbx, r9
00284648  4C 8B F9                        mov r15, rcx
0028464B  48 8B C5                        mov rax, rbp
0028464E  4C 03 E0                        add r12, rax
00284651  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
0028465B  49 8B C1                        mov rax, r9
0028465E  48 C1 E8 0C                     shr rax, 0xc
00284662  48 23 C1                        and rax, rcx
00284665  4C 8D 34 40                     lea r14, [rax + rax*2]
00284669  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00284673  49 C1 E6 04                     shl r14, 4
00284677  48 8B C0                        mov rax, rax
0028467A  4C 03 F0                        add r14, rax
0028467D  48 8B C5                        mov rax, rbp
00284680  48 BF FF FF FF FF FF F6 FF FF   movabs rdi, 0xfffff6ffffffffff
0028468A  48 3B D0                        cmp rdx, rax
0028468D  0F 83 9E 0B 00 00               jae 0x140285231
00284693  48 8B F3                        mov rsi, rbx
00284696  48 8B C3                        mov rax, rbx
00284699  48 C1 EE 3C                     shr rsi, 0x3c
0028469D  40 80 E6 07                     and sil, 7
002846A1  48 C1 E8 38                     shr rax, 0x38
002846A5  40 C0 E6 04                     shl sil, 4
002846A9  24 0F                           and al, 0xf
002846AB  40 0A F0                        or sil, al
002846AE  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002846B2  41 8B CD                        mov ecx, r13d
002846B5  48 85 C0                        test rax, rax
002846B8  0F 99 C1                        setns cl
002846BB  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
002846C2  41 F6 C0 04                     test r8b, 4
002846C6  0F 85 3D 06 00 00               jne 0x140284d09
002846CC  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002846D0  48 85 C0                        test rax, rax
002846D3  0F 88 09 06 00 00               js 0x140284ce2
002846D9  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
002846E0  24 0F                           and al, 0xf
002846E2  3C 01                           cmp al, 1
002846E4  0F 83 1F 06 00 00               jae 0x140284d09
002846EA  45 33 C0                        xor r8d, r8d
002846ED  33 D2                           xor edx, edx
002846EF  49 8B CE                        mov rcx, r14
002846F2  E8 29 0D 00 00                  call 0x140285420
002846F7  A9 FD FF FF FF                  test eax, 0xfffffffd
002846FC  0F 85 07 06 00 00               jne 0x140284d09
00284702  49 8B CC                        mov rcx, r12
00284705  48 C1 E1 19                     shl rcx, 0x19
00284709  48 8B C5                        mov rax, rbp
0028470C  48 C1 E0 19                     shl rax, 0x19
00284710  48 2B C8                        sub rcx, rax
00284713  48 C1 F9 10                     sar rcx, 0x10
00284717  48 8B C5                        mov rax, rbp
0028471A  48 3B C8                        cmp rcx, rax
0028471D  0F 83 D8 0B 00 00               jae 0x1402852fb
00284723  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00284727  66 83 F8 01                     cmp ax, 1
0028472B  0F 85 D8 05 00 00               jne 0x140284d09
00284731  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00284735  C1 E8 10                        shr eax, 0x10
00284738  24 C0                           and al, 0xc0
0028473A  3C 40                           cmp al, 0x40
0028473C  0F 85 C7 05 00 00               jne 0x140284d09
00284742  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00284746  C1 E8 18                        shr eax, 0x18
00284749  A8 40                           test al, 0x40
0028474B  0F 85 B8 05 00 00               jne 0x140284d09
00284751  BD 01 00 00 00                  mov ebp, 1
00284756  41 8B FD                        mov edi, r13d
00284759  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00284760  0F 82 AB 05 00 00               jb 0x140284d11
00284766  85 ED                           test ebp, ebp
00284768  0F 85 E5 05 00 00               jne 0x140284d53
0028476E  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
00284773  49 8B FD                        mov rdi, r13
00284776  F6 C3 04                        test bl, 4
00284779  0F 85 F4 05 00 00               jne 0x140284d73
0028477F  F6 C3 42                        test bl, 0x42
00284782  0F 85 E3 07 00 00               jne 0x140284f6b
00284788  44 39 AC 24 E8 00 00 00         cmp dword ptr [rsp + 0xe8], r13d
00284790  0F 84 B3 08 00 00               je 0x140285049
00284796  48 C7 44 24 40 FF FF FF FF      mov qword ptr [rsp + 0x40], 0xffffffffffffffff
0028479F  F6 84 24 E0 00 00 00 01         test byte ptr [rsp + 0xe0], 1
002847A7  48 BA FF FF FF FF FF FF FF 3F   movabs rdx, 0x3fffffffffffffff
002847B1  0F 85 0C 0A 00 00               jne 0x1402851c3
002847B7  41 0F B6 46 22                  movzx eax, byte ptr [r14 + 0x22]
002847BC  24 07                           and al, 7
002847BE  3C 06                           cmp al, 6
002847C0  0F 85 F6 0B 00 00               jne 0x1402853bc
002847C6  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002847CA  48 BD AB AA AA AA AA AA AA AA   movabs rbp, 0xaaaaaaaaaaaaaaab
002847D4  48 8B C8                        mov rcx, rax
002847D7  48 C7 C3 F7 FF FF FF            mov rbx, 0xfffffffffffffff7
002847DE  48 23 CA                        and rcx, rdx
002847E1  41 B9 FF FF 00 00               mov r9d, 0xffff
002847E7  48 FF C9                        dec rcx
002847EA  48 BA 00 00 00 00 00 00 00 C0   movabs rdx, 0xc000000000000000
002847F4  48 33 C1                        xor rax, rcx
002847F7  48 23 C2                        and rax, rdx
002847FA  48 33 C1                        xor rax, rcx
002847FD  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
00284801  48 85 C9                        test rcx, rcx
00284804  0F 85 45 07 00 00               jne 0x140284f4f
0028480A  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
0028480E  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
00284815  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00284819  48 85 C0                        test rax, rax
0028481C  0F 89 34 01 00 00               jns 0x140284956
00284822  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00284826  4D 8B FE                        mov r15, r14
00284829  48 C1 E8 05                     shr rax, 5
0028482D  4D 8B C5                        mov r8, r13
00284830  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00284835  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
0028483F  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00284843  4D 8B D5                        mov r10, r13
00284846  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
0028484B  49 83 FA 01                     cmp r10, 1
0028484F  0F 83 B3 00 00 00               jae 0x140284908
00284855  49 8B 6F 08                     mov rbp, qword ptr [r15 + 8]
00284859  C1 ED 03                        shr ebp, 3
0028485C  81 E5 FF 01 00 00               and ebp, 0x1ff
00284862  4D 85 C0                        test r8, r8
00284865  75 26                           jne 0x14028488d
00284867  49 8B 4F 28                     mov rcx, qword ptr [r15 + 0x28]
0028486B  41 B8 00 00 00 80               mov r8d, 0x80000000
00284871  48 23 CA                        and rcx, rdx
00284874  33 D2                           xor edx, edx
00284876  E8 95 E2 0A 00                  call 0x140332b10
0028487B  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
00284880  4C 8B C0                        mov r8, rax
00284883  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
0028488D  49 8B 0C E8                     mov rcx, qword ptr [r8 + rbp*8]
00284891  4D 8D 1C E8                     lea r11, [r8 + rbp*8]
00284895  4C 8B C9                        mov r9, rcx
00284898  48 BD 00 00 00 00 00 DE FF FF   movabs rbp, 0xffffde0000000000
002848A2  49 C1 E9 0C                     shr r9, 0xc
002848A6  4C 23 CA                        and r9, rdx
002848A9  4B 8D 14 49                     lea rdx, [r9 + r9*2]
002848AD  48 C1 E2 04                     shl rdx, 4
002848B1  48 8B C5                        mov rax, rbp
002848B4  48 03 D0                        add rdx, rax
002848B7  49 3B D7                        cmp rdx, r15
002848BA  0F 85 A0 0A 00 00               jne 0x140285360
002848C0  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
002848C4  48 8B 15 B5 93 BA 00            mov rdx, qword ptr [rip + 0xba93b5]
002848CB  83 E0 1F                        and eax, 0x1f
002848CE  49 C1 E1 07                     shl r9, 7
002848D2  49 0B C1                        or rax, r9
002848D5  48 83 C8 40                     or rax, 0x40
002848D9  48 C1 E0 05                     shl rax, 5
002848DD  48 85 D2                        test rdx, rdx
002848E0  74 0D                           je 0x1402848ef
002848E2  48 85 D0                        test rax, rdx
002848E5  0F 84 54 06 00 00               je 0x140284f3f
002848EB  48 83 C8 10                     or rax, 0x10
002848EF  49 89 03                        mov qword ptr [r11], rax
002848F2  49 8D 42 01                     lea rax, [r10 + 1]
002848F6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002848FB  4C 8B D0                        mov r10, rax
002848FE  48 83 F8 01                     cmp rax, 1
00284902  0F 85 28 04 00 00               jne 0x140284d30
00284908  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00284912  49 C1 E8 09                     shr r8, 9
00284916  4C 23 C0                        and r8, rax
00284919  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00284923  48 8B C0                        mov rax, rax
00284926  4C 03 C0                        add r8, rax
00284929  48 BD AB AA AA AA AA AA AA AA   movabs rbp, 0xaaaaaaaaaaaaaaab
00284933  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0028493C  41 B9 FF FF 00 00               mov r9d, 0xffff
00284942  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
00284949  48 8B 05 30 BF D8 FF            mov rax, qword ptr [rip - 0x2740d0]
00284950  4C 89 29                        mov qword ptr [rcx], r13
00284953  49 89 00                        mov qword ptr [r8], rax
00284956  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0028495A  48 C1 E8 3E                     shr rax, 0x3e
0028495E  83 E0 01                        and eax, 1
00284961  66 44 01 8C 24 E0 00 00 00      add word ptr [rsp + 0xe0], r9w
0028496A  0F 85 65 07 00 00               jne 0x1402850d5
00284970  85 C0                           test eax, eax
00284972  0F 84 2A 06 00 00               je 0x140284fa2
00284978  0F B6 84 24 E3 00 00 00         movzx eax, byte ptr [rsp + 0xe3]
00284980  A8 10                           test al, 0x10
00284982  0F 85 3D 0A 00 00               jne 0x1402853c5
00284988  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
0028498F  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00284993  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00284997  48 8B 0D EA B6 BA 00            mov rcx, qword ptr [rip + 0xbab6ea]
0028499E  48 C1 E8 2B                     shr rax, 0x2b
002849A2  25 FF 03 00 00                  and eax, 0x3ff
002849A7  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
002849AB  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
002849AF  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002849B4  48 0F BA E0 0A                  bt rax, 0xa
002849B9  72 1E                           jb 0x1402849d9
002849BB  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
002849C0  C0 E8 02                        shr al, 2
002849C3  A8 01                           test al, 1
002849C5  75 09                           jne 0x1402849d0
002849C7  0F B6 C2                        movzx eax, dl
002849CA  D0 E8                           shr al, 1
002849CC  A8 01                           test al, 1
002849CE  74 09                           je 0x1402849d9
002849D0  48 85 D2                        test rdx, rdx
002849D3  0F 85 74 08 00 00               jne 0x14028524d
002849D9  49 BF 00 00 00 00 00 DE FF FF   movabs r15, 0xffffde0000000000
002849E3  49 8B C7                        mov rax, r15
002849E6  49 8B CE                        mov rcx, r14
002849E9  BA 02 00 00 00                  mov edx, 2
002849EE  48 2B C8                        sub rcx, rax
002849F1  48 C1 F9 04                     sar rcx, 4
002849F5  48 0F AF CD                     imul rcx, rbp
002849F9  E8 22 03 0B 00                  call 0x140334d20
002849FE  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00284A03  48 83 F8 FF                     cmp rax, -1
00284A07  0F 84 5B 02 00 00               je 0x140284c68
00284A0D  49 B8 FF FF FF FF FF FF FF 7F   movabs r8, 0x7fffffffffffffff
00284A17  F0 4D 21 46 18                  lock and qword ptr [r14 + 0x18], r8
00284A1C  4C 8D 34 40                     lea r14, [rax + rax*2]
00284A20  49 C1 E6 04                     shl r14, 4
00284A24  49 8B C7                        mov rax, r15
00284A27  4C 03 F0                        add r14, rax
00284A2A  41 8B ED                        mov ebp, r13d
00284A2D  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00284A34  0F 82 E6 04 00 00               jb 0x140284f20
00284A3A  41 0F B6 46 22                  movzx eax, byte ptr [r14 + 0x22]
00284A3F  24 07                           and al, 7
00284A41  3C 06                           cmp al, 6
00284A43  0F 85 8A 09 00 00               jne 0x1402853d3
00284A49  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00284A4D  48 BA FF FF FF FF FF FF FF 3F   movabs rdx, 0x3fffffffffffffff
00284A57  48 8B C8                        mov rcx, rax
00284A5A  48 BD 00 00 00 00 00 00 00 C0   movabs rbp, 0xc000000000000000
00284A64  48 23 CA                        and rcx, rdx
00284A67  48 FF C9                        dec rcx
00284A6A  48 33 C1                        xor rax, rcx
00284A6D  48 23 C5                        and rax, rbp
00284A70  48 33 C1                        xor rax, rcx
00284A73  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
00284A77  48 85 C9                        test rcx, rcx
00284A7A  0F 85 E2 04 00 00               jne 0x140284f62
00284A80  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00284A84  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
00284A8B  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00284A8F  48 85 C0                        test rax, rax
00284A92  0F 89 24 01 00 00               jns 0x140284bbc
00284A98  4D 8B 56 10                     mov r10, qword ptr [r14 + 0x10]
00284A9C  4D 8B FE                        mov r15, r14
00284A9F  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00284AA3  4D 8B C5                        mov r8, r13
00284AA6  49 C1 EA 05                     shr r10, 5
00284AAA  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
00284AB4  4C 89 54 24 50                  mov qword ptr [rsp + 0x50], r10
00284AB9  49 83 FD 01                     cmp r13, 1
00284ABD  0F 83 AD 00 00 00               jae 0x140284b70
00284AC3  49 8B 6F 08                     mov rbp, qword ptr [r15 + 8]
00284AC7  C1 ED 03                        shr ebp, 3
00284ACA  81 E5 FF 01 00 00               and ebp, 0x1ff
00284AD0  4D 85 C0                        test r8, r8
00284AD3  75 26                           jne 0x140284afb
00284AD5  49 8B 4F 28                     mov rcx, qword ptr [r15 + 0x28]
00284AD9  41 B8 00 00 00 80               mov r8d, 0x80000000
00284ADF  48 23 CA                        and rcx, rdx
00284AE2  33 D2                           xor edx, edx
00284AE4  E8 27 E0 0A 00                  call 0x140332b10
00284AE9  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
00284AEE  4C 8B C0                        mov r8, rax
00284AF1  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
00284AFB  49 8B 0C E8                     mov rcx, qword ptr [r8 + rbp*8]
00284AFF  4D 8D 1C E8                     lea r11, [r8 + rbp*8]
00284B03  4C 8B C9                        mov r9, rcx
00284B06  48 BD 00 00 00 00 00 DE FF FF   movabs rbp, 0xffffde0000000000
00284B10  49 C1 E9 0C                     shr r9, 0xc
00284B14  4C 23 CA                        and r9, rdx
00284B17  4B 8D 14 49                     lea rdx, [r9 + r9*2]
00284B1B  48 C1 E2 04                     shl rdx, 4
00284B1F  48 8B C5                        mov rax, rbp
00284B22  48 03 D0                        add rdx, rax
00284B25  49 3B D7                        cmp rdx, r15
00284B28  0F 85 60 08 00 00               jne 0x14028538e
00284B2E  48 8B 15 4B 91 BA 00            mov rdx, qword ptr [rip + 0xba914b]
00284B35  41 8B C2                        mov eax, r10d
00284B38  83 E0 1F                        and eax, 0x1f
00284B3B  49 C1 E1 07                     shl r9, 7
00284B3F  49 0B C1                        or rax, r9
00284B42  48 83 C8 40                     or rax, 0x40
00284B46  48 C1 E0 05                     shl rax, 5
00284B4A  48 85 D2                        test rdx, rdx
00284B4D  74 0D                           je 0x140284b5c
00284B4F  48 85 C2                        test rdx, rax
00284B52  0F 84 EF 03 00 00               je 0x140284f47
00284B58  48 83 C8 10                     or rax, 0x10
00284B5C  49 89 03                        mov qword ptr [r11], rax
00284B5F  49 8D 45 01                     lea rax, [r13 + 1]
00284B63  4C 8B E8                        mov r13, rax
00284B66  48 83 F8 01                     cmp rax, 1
00284B6A  0F 85 82 03 00 00               jne 0x140284ef2
00284B70  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00284B7A  49 C1 E8 09                     shr r8, 9
00284B7E  4C 23 C0                        and r8, rax
00284B81  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00284B8B  48 8B C0                        mov rax, rax
00284B8E  4C 03 C0                        add r8, rax
00284B91  49 BF 00 00 00 00 00 DE FF FF   movabs r15, 0xffffde0000000000
00284B9B  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00284BA4  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
00284BAB  48 8B 05 CE BC D8 FF            mov rax, qword ptr [rip - 0x274332]
00284BB2  48 C7 01 00 00 00 00            mov qword ptr [rcx], 0
00284BB9  49 89 00                        mov qword ptr [r8], rax
00284BBC  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00284BC0  B9 FF FF 00 00                  mov ecx, 0xffff
00284BC5  48 C1 E8 3E                     shr rax, 0x3e
00284BC9  83 E0 01                        and eax, 1
00284BCC  66 01 8C 24 E0 00 00 00         add word ptr [rsp + 0xe0], cx
00284BD4  0F 85 77 05 00 00               jne 0x140285151
00284BDA  85 C0                           test eax, eax
00284BDC  0F 84 1A 04 00 00               je 0x140284ffc
00284BE2  0F B6 84 24 E3 00 00 00         movzx eax, byte ptr [rsp + 0xe3]
00284BEA  A8 10                           test al, 0x10
00284BEC  0F 85 EA 07 00 00               jne 0x1402853dc
00284BF2  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00284BF9  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00284BFD  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00284C01  48 8B 0D 80 B4 BA 00            mov rcx, qword ptr [rip + 0xbab480]
00284C08  48 C1 E8 2B                     shr rax, 0x2b
00284C0C  25 FF 03 00 00                  and eax, 0x3ff
00284C11  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00284C15  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00284C19  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00284C1E  48 0F BA E0 0A                  bt rax, 0xa
00284C23  72 1E                           jb 0x140284c43
00284C25  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00284C2A  C0 E8 02                        shr al, 2
00284C2D  A8 01                           test al, 1
00284C2F  75 09                           jne 0x140284c3a
00284C31  0F B6 C2                        movzx eax, dl
00284C34  D0 E8                           shr al, 1
00284C36  A8 01                           test al, 1
00284C38  74 09                           je 0x140284c43
00284C3A  48 85 D2                        test rdx, rdx
00284C3D  0F 85 1A 06 00 00               jne 0x14028525d
00284C43  49 8B C7                        mov rax, r15
00284C46  49 8B CE                        mov rcx, r14
00284C49  BA 02 00 00 00                  mov edx, 2
00284C4E  48 2B C8                        sub rcx, rax
00284C51  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00284C5B  48 C1 F9 04                     sar rcx, 4
00284C5F  48 0F AF C8                     imul rcx, rax
00284C63  E8 B8 00 0B 00                  call 0x140334d20
00284C68  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00284C72  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
00284C77  48 85 FF                        test rdi, rdi
00284C7A  74 13                           je 0x140284c8f
00284C7C  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00284C81  41 B8 01 00 00 00               mov r8d, 1
00284C87  48 8B D7                        mov rdx, rdi
00284C8A  E8 41 F3 FF FF                  call 0x140283fd0
00284C8F  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
00284C96  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00284C9E  02 C0                           add al, al
00284CA0  0C 01                           or al, 1
00284CA2  41 C1 EC 03                     shr r12d, 3
00284CA6  88 84 24 D9 00 00 00            mov byte ptr [rsp + 0xd9], al
00284CAD  B8 FF 01 00 00                  mov eax, 0x1ff
00284CB2  66 44 23 E0                     and r12w, ax
00284CB6  40 88 B4 24 D8 00 00 00         mov byte ptr [rsp + 0xd8], sil
00284CBE  66 44 89 A4 24 DA 00 00 00      mov word ptr [rsp + 0xda], r12w
00284CC7  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
00284CCE  48 81 C4 90 00 00 00            add rsp, 0x90
00284CD5  41 5F                           pop r15
00284CD7  41 5E                           pop r14
00284CD9  41 5D                           pop r13
00284CDB  41 5C                           pop r12
00284CDD  5F                              pop rdi
00284CDE  5E                              pop rsi
00284CDF  5D                              pop rbp
00284CE0  C3                              ret
00284CE1  CC                              int3
00284CE2  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00284CE6  48 0F BA E0 28                  bt rax, 0x28
00284CEB  72 0D                           jb 0x140284cfa
00284CED  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00284CF1  48 85 C0                        test rax, rax
00284CF4  0F 89 8D 05 00 00               jns 0x140285287
00284CFA  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00284CFE  48 0F BA E0 0A                  bt rax, 0xa
00284D03  0F 83 1A FA FF FF               jae 0x140284723
00284D09  41 8B ED                        mov ebp, r13d
00284D0C  E9 45 FA FF FF                  jmp 0x140284756
00284D11  FF C7                           inc edi
00284D13  85 3D 93 05 D4 00               test dword ptr [rip + 0xd40593], edi
00284D19  0F 84 7A 05 00 00               je 0x140285299
00284D1F  F3 90                           pause
00284D21  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00284D25  48 85 C0                        test rax, rax
00284D28  0F 89 2B FA FF FF               jns 0x140284759
00284D2E  EB E1                           jmp 0x140284d11
00284D30  49 8B 07                        mov rax, qword ptr [r15]
00284D33  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
00284D3D  48 23 C2                        and rax, rdx
00284D40  4C 8D 3C 40                     lea r15, [rax + rax*2]
00284D44  49 C1 E7 04                     shl r15, 4
00284D48  48 8B C5                        mov rax, rbp
00284D4B  4C 03 F8                        add r15, rax
00284D4E  E9 F8 FA FF FF                  jmp 0x14028484b
00284D53  49 8B CE                        mov rcx, r14
00284D56  E8 25 F6 0A 00                  call 0x140334380
00284D5B  85 C0                           test eax, eax
00284D5D  0F 84 0B FA FF FF               je 0x14028476e
00284D63  49 8B D6                        mov rdx, r14
00284D66  49 8B CF                        mov rcx, r15
00284D69  E8 86 D6 0F 00                  call 0x1403823f4
00284D6E  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
00284D73  49 8B CC                        mov rcx, r12
00284D76  E8 75 1A 0C 00                  call 0x1403467f0
00284D7B  41 8B 56 20                     mov edx, dword ptr [r14 + 0x20]
00284D7F  4C 8B F8                        mov r15, rax
00284D82  49 8B 4E 28                     mov rcx, qword ptr [r14 + 0x28]
00284D86  49 B8 FF FF FF FF FF FF FF 7F   movabs r8, 0x7fffffffffffffff
00284D90  89 94 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], edx
00284D97  49 23 C8                        and rcx, r8
00284D9A  80 A4 24 E3 00 00 00 D7         and byte ptr [rsp + 0xe3], 0xd7
00284DA2  49 89 4E 28                     mov qword ptr [r14 + 0x28], rcx
00284DA6  41 8B CD                        mov ecx, r13d
00284DA9  C1 EA 10                        shr edx, 0x10
00284DAC  80 E2 C7                        and dl, 0xc7
00284DAF  88 94 24 E2 00 00 00            mov byte ptr [rsp + 0xe2], dl
00284DB6  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00284DBD  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00284DC1  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00284DC5  48 0F BA E0 28                  bt rax, 0x28
00284DCA  73 0A                           jae 0x140284dd6
00284DCC  41 8B 4E 24                     mov ecx, dword ptr [r14 + 0x24]
00284DD0  81 E1 00 00 00 18               and ecx, 0x18000000
00284DD6  41 89 4E 24                     mov dword ptr [r14 + 0x24], ecx
00284DDA  48 BD 00 00 00 00 00 00 00 C0   movabs rbp, 0xc000000000000000
00284DE4  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00284DE8  48 23 C5                        and rax, rbp
00284DEB  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
00284DEF  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
00284DF3  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
00284DFA  66 44 89 AC 24 E0 00 00 00      mov word ptr [rsp + 0xe0], r13w
00284E03  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00284E0A  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00284E0E  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00284E12  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00284E17  C0 E8 02                        shr al, 2
00284E1A  A8 01                           test al, 1
00284E1C  0F 85 9E 04 00 00               jne 0x1402852c0
00284E22  49 8B FD                        mov rdi, r13
00284E25  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
00284E2A  48 85 FF                        test rdi, rdi
00284E2D  0F 85 B7 05 00 00               jne 0x1402853ea
00284E33  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00284E3D  48 8B C0                        mov rax, rax
00284E40  49 8B CE                        mov rcx, r14
00284E43  48 2B C8                        sub rcx, rax
00284E46  48 B8 AB AA AA AA AA AA AA 2A   movabs rax, 0x2aaaaaaaaaaaaaab
00284E50  48 F7 E9                        imul rcx
00284E53  48 8B CA                        mov rcx, rdx
00284E56  41 8B D5                        mov edx, r13d
00284E59  48 C1 F9 03                     sar rcx, 3
00284E5D  48 8B C1                        mov rax, rcx
00284E60  48 C1 E8 3F                     shr rax, 0x3f
00284E64  48 03 C8                        add rcx, rax
00284E67  83 E3 04                        and ebx, 4
00284E6A  48 85 DB                        test rbx, rbx
00284E6D  0F 95 C2                        setne dl
00284E70  FF C2                           inc edx
00284E72  E8 A9 FE 0A 00                  call 0x140334d20
00284E77  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00284E81  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
00284E86  4F 8D 34 7F                     lea r14, [r15 + r15*2]
00284E8A  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00284E94  49 C1 E6 04                     shl r14, 4
00284E98  48 8B C0                        mov rax, rax
00284E9B  4C 03 F0                        add r14, rax
00284E9E  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00284EA5  0F 82 B5 01 00 00               jb 0x140285060
00284EAB  41 0F B6 46 22                  movzx eax, byte ptr [r14 + 0x22]
00284EB0  24 07                           and al, 7
00284EB2  3C 06                           cmp al, 6
00284EB4  0F 85 52 05 00 00               jne 0x14028540c
00284EBA  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00284EBE  48 BA FF FF FF FF FF FF FF 3F   movabs rdx, 0x3fffffffffffffff
00284EC8  48 8B C8                        mov rcx, rax
00284ECB  48 23 CA                        and rcx, rdx
00284ECE  48 FF C9                        dec rcx
00284ED1  48 33 C1                        xor rax, rcx
00284ED4  48 23 C5                        and rax, rbp
00284ED7  48 33 C1                        xor rax, rcx
00284EDA  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
00284EDE  48 85 C9                        test rcx, rcx
00284EE1  75 7F                           jne 0x140284f62
00284EE3  33 D2                           xor edx, edx
00284EE5  49 8B CE                        mov rcx, r14
00284EE8  E8 43 BA 0A 00                  call 0x140330930
00284EED  E9 76 FD FF FF                  jmp 0x140284c68
00284EF2  49 8B 07                        mov rax, qword ptr [r15]
00284EF5  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
00284EFF  48 23 C2                        and rax, rdx
00284F02  4C 8D 3C 40                     lea r15, [rax + rax*2]
00284F06  49 C1 E7 04                     shl r15, 4
00284F0A  48 8B C5                        mov rax, rbp
00284F0D  4C 03 F8                        add r15, rax
00284F10  E9 A4 FB FF FF                  jmp 0x140284ab9
00284F15  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
00284F20  FF C5                           inc ebp
00284F22  85 2D 84 03 D4 00               test dword ptr [rip + 0xd40384], ebp
00284F28  0F 84 A6 03 00 00               je 0x1402852d4
00284F2E  F3 90                           pause
00284F30  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00284F34  48 85 C0                        test rax, rax
00284F37  0F 89 F0 FA FF FF               jns 0x140284a2d
00284F3D  EB E1                           jmp 0x140284f20
00284F3F  48 0B C2                        or rax, rdx
00284F42  E9 A8 F9 FF FF                  jmp 0x1402848ef
00284F47  48 0B C2                        or rax, rdx
00284F4A  E9 0D FC FF FF                  jmp 0x140284b5c
00284F4F  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00284F53  49 BF 00 00 00 00 00 DE FF FF   movabs r15, 0xffffde0000000000
00284F5D  E9 9C FA FF FF                  jmp 0x1402849fe
00284F62  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00284F66  E9 FD FC FF FF                  jmp 0x140284c68
00284F6B  49 8B CE                        mov rcx, r14
00284F6E  E8 5D BE 0E 00                  call 0x140370dd0
00284F73  48 8B F8                        mov rdi, rax
00284F76  48 85 C0                        test rax, rax
00284F79  0F 84 09 F8 FF FF               je 0x140284788
00284F7F  49 8B 4E 28                     mov rcx, qword ptr [r14 + 0x28]
00284F83  48 8B 05 FE B0 BA 00            mov rax, qword ptr [rip + 0xbab0fe]
00284F8A  48 C1 E9 2B                     shr rcx, 0x2b
00284F8E  81 E1 FF 03 00 00               and ecx, 0x3ff
00284F94  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00284F98  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00284F9D  E9 E6 F7 FF FF                  jmp 0x140284788
00284FA2  49 8D 4E 10                     lea rcx, [r14 + 0x10]
00284FA6  E8 F5 D8 FF FF                  call 0x1402828a0
00284FAB  48 0F BA E0 0A                  bt rax, 0xa
00284FB0  48 8B CB                        mov rcx, rbx
00284FB3  48 C7 C2 FF F7 FF FF            mov rdx, 0xfffffffffffff7ff
00284FBA  48 0F 42 CA                     cmovb rcx, rdx
00284FBE  48 23 C8                        and rcx, rax
00284FC1  0F B6 84 24 E2 00 00 00         movzx eax, byte ptr [rsp + 0xe2]
00284FC9  49 89 4E 10                     mov qword ptr [r14 + 0x10], rcx
00284FCD  49 8B CE                        mov rcx, r14
00284FD0  A8 10                           test al, 0x10
00284FD2  0F 84 A9 00 00 00               je 0x140285081
00284FD8  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00284FDF  BA 08 00 00 00                  mov edx, 8
00284FE4  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00284FE8  E8 13 50 03 00                  call 0x1402ba000
00284FED  49 BF 00 00 00 00 00 DE FF FF   movabs r15, 0xffffde0000000000
00284FF7  E9 02 FA FF FF                  jmp 0x1402849fe
00284FFC  49 8D 4E 10                     lea rcx, [r14 + 0x10]
00285000  E8 9B D8 FF FF                  call 0x1402828a0
00285005  48 0F BA E0 0A                  bt rax, 0xa
0028500A  48 C7 C1 FF F7 FF FF            mov rcx, 0xfffffffffffff7ff
00285011  48 0F 42 D9                     cmovb rbx, rcx
00285015  49 8B CE                        mov rcx, r14
00285018  48 23 D8                        and rbx, rax
0028501B  0F B6 84 24 E2 00 00 00         movzx eax, byte ptr [rsp + 0xe2]
00285023  49 89 5E 10                     mov qword ptr [r14 + 0x10], rbx
00285027  A8 10                           test al, 0x10
00285029  0F 84 81 00 00 00               je 0x1402850b0
0028502F  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00285036  BA 08 00 00 00                  mov edx, 8
0028503B  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
0028503F  E8 BC 4F 03 00                  call 0x1402ba000
00285044  E9 1F FC FF FF                  jmp 0x140284c68
00285049  49 8B CC                        mov rcx, r12
0028504C  E8 9F 17 0C 00                  call 0x1403467f0
00285051  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00285056  E9 44 F7 FF FF                  jmp 0x14028479f
0028505B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00285060  41 FF C5                        inc r13d
00285063  44 85 2D 42 02 D4 00            test dword ptr [rip + 0xd40242], r13d
0028506A  0F 84 9C 02 00 00               je 0x14028530c
00285070  F3 90                           pause
00285072  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00285076  48 85 C0                        test rax, rax
00285079  0F 89 1F FE FF FF               jns 0x140284e9e
0028507F  EB DF                           jmp 0x140285060
00285081  24 FA                           and al, 0xfa
00285083  BA 04 00 00 00                  mov edx, 4
00285088  0C 02                           or al, 2
0028508A  88 84 24 E2 00 00 00            mov byte ptr [rsp + 0xe2], al
00285091  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00285098  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
0028509C  E8 5F 4F 03 00                  call 0x1402ba000
002850A1  49 BF 00 00 00 00 00 DE FF FF   movabs r15, 0xffffde0000000000
002850AB  E9 4E F9 FF FF                  jmp 0x1402849fe
002850B0  24 FA                           and al, 0xfa
002850B2  BA 04 00 00 00                  mov edx, 4
002850B7  0C 02                           or al, 2
002850B9  88 84 24 E2 00 00 00            mov byte ptr [rsp + 0xe2], al
002850C0  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
002850C7  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002850CB  E8 30 4F 03 00                  call 0x1402ba000
002850D0  E9 93 FB FF FF                  jmp 0x140284c68
002850D5  85 C0                           test eax, eax
002850D7  0F 85 90 01 00 00               jne 0x14028526d
002850DD  0F B6 84 24 E2 00 00 00         movzx eax, byte ptr [rsp + 0xe2]
002850E5  A8 10                           test al, 0x10
002850E7  0F 84 47 02 00 00               je 0x140285334
002850ED  24 FB                           and al, 0xfb
002850EF  0C 03                           or al, 3
002850F1  88 84 24 E2 00 00 00            mov byte ptr [rsp + 0xe2], al
002850F8  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
002850FF  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
00285103  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00285107  48 0F BA E0 0A                  bt rax, 0xa
0028510C  0F 82 41 FE FF FF               jb 0x140284f53
00285112  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00285116  E8 15 A4 0E 00                  call 0x14036f530
0028511B  49 BF 00 00 00 00 00 DE FF FF   movabs r15, 0xffffde0000000000
00285125  85 C0                           test eax, eax
00285127  0F 84 D1 F8 FF FF               je 0x1402849fe
0028512D  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00285131  48 8B 0D 50 AF BA 00            mov rcx, qword ptr [rip + 0xbaaf50]
00285138  48 C1 E8 2B                     shr rax, 0x2b
0028513C  25 FF 03 00 00                  and eax, 0x3ff
00285141  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
00285145  C6 82 D3 02 00 00 01            mov byte ptr [rdx + 0x2d3], 1
0028514C  E9 AD F8 FF FF                  jmp 0x1402849fe
00285151  85 C0                           test eax, eax
00285153  0F 85 21 01 00 00               jne 0x14028527a
00285159  0F B6 84 24 E2 00 00 00         movzx eax, byte ptr [rsp + 0xe2]
00285161  A8 10                           test al, 0x10
00285163  0F 84 D8 01 00 00               je 0x140285341
00285169  24 FB                           and al, 0xfb
0028516B  0C 03                           or al, 3
0028516D  88 84 24 E2 00 00 00            mov byte ptr [rsp + 0xe2], al
00285174  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
0028517B  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
0028517F  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00285183  48 0F BA E0 0A                  bt rax, 0xa
00285188  0F 82 DA FA FF FF               jb 0x140284c68
0028518E  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00285192  E8 99 A3 0E 00                  call 0x14036f530
00285197  85 C0                           test eax, eax
00285199  0F 84 C9 FA FF FF               je 0x140284c68
0028519F  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002851A3  48 8B 0D DE AE BA 00            mov rcx, qword ptr [rip + 0xbaaede]
002851AA  48 C1 E8 2B                     shr rax, 0x2b
002851AE  25 FF 03 00 00                  and eax, 0x3ff
002851B3  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
002851B7  C6 82 D3 02 00 00 01            mov byte ptr [rdx + 0x2d3], 1
002851BE  E9 A5 FA FF FF                  jmp 0x140284c68
002851C3  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002851C7  48 23 C2                        and rax, rdx
002851CA  48 83 F8 01                     cmp rax, 1
002851CE  0F 85 E3 F5 FF FF               jne 0x1402847b7
002851D4  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002851D8  66 83 F8 01                     cmp ax, 1
002851DC  0F 85 D5 F5 FF FF               jne 0x1402847b7
002851E2  41 F6 46 22 10                  test byte ptr [r14 + 0x22], 0x10
002851E7  0F 85 CA F5 FF FF               jne 0x1402847b7
002851ED  49 8B CE                        mov rcx, r14
002851F0  E8 FB D4 09 00                  call 0x1403226f0
002851F5  48 BA FF FF FF FF FF FF FF 3F   movabs rdx, 0x3fffffffffffffff
002851FF  83 F8 05                        cmp eax, 5
00285202  0F 85 AF F5 FF FF               jne 0x1402847b7
00285208  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
0028520C  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
00285213  C1 E8 18                        shr eax, 0x18
00285216  24 FC                           and al, 0xfc
00285218  0C 04                           or al, 4
0028521A  88 84 24 E3 00 00 00            mov byte ptr [rsp + 0xe3], al
00285221  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00285228  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
0028522C  E9 86 F5 FF FF                  jmp 0x1402847b7
00285231  48 8B C7                        mov rax, rdi
00285234  48 3B D0                        cmp rdx, rax
00285237  0F 87 56 F4 FF FF               ja 0x140284693
0028523D  49 8B 36                        mov rsi, qword ptr [r14]
00285240  48 C1 EE 2A                     shr rsi, 0x2a
00285244  40 80 E6 07                     and sil, 7
00285248  E9 61 F4 FF FF                  jmp 0x1402846ae
0028524D  41 B8 01 00 00 00               mov r8d, 1
00285253  E8 78 ED FF FF                  call 0x140283fd0
00285258  E9 7C F7 FF FF                  jmp 0x1402849d9
0028525D  41 B8 01 00 00 00               mov r8d, 1
00285263  E8 68 ED FF FF                  call 0x140283fd0
00285268  E9 D6 F9 FF FF                  jmp 0x140284c43
0028526D  80 8C 24 E2 00 00 00 07         or byte ptr [rsp + 0xe2], 7
00285275  E9 7E FE FF FF                  jmp 0x1402850f8
0028527A  80 8C 24 E2 00 00 00 07         or byte ptr [rsp + 0xe2], 7
00285282  E9 ED FE FF FF                  jmp 0x140285174
00285287  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0028528B  48 85 C0                        test rax, rax
0028528E  0F 85 75 FA FF FF               jne 0x140284d09
00285294  E9 61 FA FF FF                  jmp 0x140284cfa
00285299  8B 05 19 18 D4 00               mov eax, dword ptr [rip + 0xd41819]
0028529F  A8 40                           test al, 0x40
002852A1  0F 84 78 FA FF FF               je 0x140284d1f
002852A7  E8 E4 A1 08 00                  call 0x14030f490
002852AC  84 C0                           test al, al
002852AE  0F 84 6B FA FF FF               je 0x140284d1f
002852B4  8B CF                           mov ecx, edi
002852B6  E8 A5 A1 08 00                  call 0x14030f460
002852BB  E9 61 FA FF FF                  jmp 0x140284d21
002852C0  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
002852C5  E8 C2 63 0A 00                  call 0x14032b68c
002852CA  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
002852CF  E9 56 FB FF FF                  jmp 0x140284e2a
002852D4  8B 05 DE 17 D4 00               mov eax, dword ptr [rip + 0xd417de]
002852DA  A8 40                           test al, 0x40
002852DC  0F 84 4C FC FF FF               je 0x140284f2e
002852E2  E8 A9 A1 08 00                  call 0x14030f490
002852E7  84 C0                           test al, al
002852E9  0F 84 3F FC FF FF               je 0x140284f2e
002852EF  8B CD                           mov ecx, ebp
002852F1  E8 6A A1 08 00                  call 0x14030f460
002852F6  E9 35 FC FF FF                  jmp 0x140284f30
002852FB  48 8B C7                        mov rax, rdi
002852FE  48 3B C8                        cmp rcx, rax
00285301  0F 87 1C F4 FF FF               ja 0x140284723
00285307  E9 FD F9 FF FF                  jmp 0x140284d09
0028530C  8B 05 A6 17 D4 00               mov eax, dword ptr [rip + 0xd417a6]
00285312  A8 40                           test al, 0x40
00285314  0F 84 56 FD FF FF               je 0x140285070
0028531A  E8 71 A1 08 00                  call 0x14030f490
0028531F  84 C0                           test al, al
00285321  0F 84 49 FD FF FF               je 0x140285070
00285327  41 8B CD                        mov ecx, r13d
0028532A  E8 31 A1 08 00                  call 0x14030f460
0028532F  E9 3E FD FF FF                  jmp 0x140285072
00285334  A8 08                           test al, 8
00285336  75 16                           jne 0x14028534e
00285338  24 FA                           and al, 0xfa
0028533A  0C 02                           or al, 2
0028533C  E9 B0 FD FF FF                  jmp 0x1402850f1
00285341  A8 08                           test al, 8
00285343  75 12                           jne 0x140285357
00285345  24 FA                           and al, 0xfa
00285347  0C 02                           or al, 2
00285349  E9 1F FE FF FF                  jmp 0x14028516d
0028534E  24 FB                           and al, 0xfb
00285350  0C 03                           or al, 3
00285352  E9 9A FD FF FF                  jmp 0x1402850f1
00285357  24 FB                           and al, 0xfb
00285359  0C 03                           or al, 3
0028535B  E9 0D FE FF FF                  jmp 0x14028516d
00285360  48 8B C5                        mov rax, rbp
00285363  4C 2B F8                        sub r15, rax
00285366  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0028536B  49 C1 FF 04                     sar r15, 4
0028536F  BA 06 00 00 00                  mov edx, 6
00285374  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
0028537E  4D 8B CB                        mov r9, r11
00285381  4D 0F AF C7                     imul r8, r15
00285385  8D 4A 48                        lea ecx, [rdx + 0x48]
00285388  E8 D3 82 27 00                  call 0x1404fd660
0028538D  CC                              int3
0028538E  48 8B C5                        mov rax, rbp
00285391  4C 2B F8                        sub r15, rax
00285394  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00285399  49 C1 FF 04                     sar r15, 4
0028539D  BA 06 00 00 00                  mov edx, 6
002853A2  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
002853AC  4D 8B CB                        mov r9, r11
002853AF  4D 0F AF C7                     imul r8, r15
002853B3  8D 4A 48                        lea ecx, [rdx + 0x48]
002853B6  E8 A5 82 27 00                  call 0x1404fd660
002853BB  CC                              int3
002853BC  49 8B CE                        mov rcx, r14
002853BF  E8 34 BB 0E 00                  call 0x140370ef8
002853C4  CC                              int3
002853C5  24 EF                           and al, 0xef
002853C7  88 84 24 E3 00 00 00            mov byte ptr [rsp + 0xe3], al
002853CE  E9 B5 F5 FF FF                  jmp 0x140284988
002853D3  49 8B CE                        mov rcx, r14
002853D6  E8 1D BB 0E 00                  call 0x140370ef8
002853DB  CC                              int3
002853DC  24 EF                           and al, 0xef
002853DE  88 84 24 E3 00 00 00            mov byte ptr [rsp + 0xe3], al
002853E5  E9 08 F8 FF FF                  jmp 0x140284bf2
002853EA  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002853EE  48 8B 0D 93 AC BA 00            mov rcx, qword ptr [rip + 0xbaac93]
002853F5  48 C1 E8 2B                     shr rax, 0x2b
002853F9  25 FF 03 00 00                  and eax, 0x3ff
002853FE  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00285402  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00285407  E9 27 FA FF FF                  jmp 0x140284e33
0028540C  49 8B CE                        mov rcx, r14
0028540F  E8 E4 BA 0E 00                  call 0x140370ef8
00285414  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWsleFree(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p11;
    unsigned __int16 v_stack_p12;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p1B;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_pE0;
    unsigned __int8 v_stack_pE2;
    unsigned __int8 v_stack_pE3;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (144);
    v_r12 = (a2) >> (9);
    v_r13 = 0;
    v_stack_p10 = 0;
    v_r12 = (v_r12) & (result);
    v_r12 = (v_r12) + (v_rbp);
    result = (a4) >> (12);
    result = (result) & (a1);
    v_r14 = (result + result * 2) << (4);
    v_r14 = (v_r14) + (result);
    if (a2 >= v_rbp) goto loc_00285231;
loc_00284693:
    v_rsi = (a4) >> (60);
    v_rsi = (unsigned __int8)((v_rsi) & (7));
    result = (a4) >> (56);
    v_rsi = (unsigned __int8)((v_rsi) << (4));
    result = (unsigned __int8)((result) & (15));
    v_rsi = (unsigned __int8)((v_rsi) | ((unsigned __int8)(result)));
loc_002846AE:
    a1 = (!sign_flag) ? 1 : 0;
    v_stack_p20 = (unsigned int)(a1);
    if ((((unsigned __int8)(a3)) & (4)) != 0) goto loc_00284D09;
    if (sign_flag) goto loc_00284CE2;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (((unsigned __int8)(result)) >= 1) goto loc_00284D09;
    a3 = 0;
    a2 = 0;
    result = MiGetPagePrivilege(v_r14, a2, a3, a4);
    if ((((unsigned int)(result)) & (0xFFFFFFFDULL)) != 0) goto loc_00284D09;
    a1 = (v_r12) << (25);
    result = (v_rbp) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    if (a1 >= v_rbp) goto loc_002852FB;
loc_00284723:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r14 + 32)))) != 1) goto loc_00284D09;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 32))) >> (16));
    result = (unsigned __int8)((result) & (192));
    if (((unsigned __int8)(result)) != 64) goto loc_00284D09;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_00284D09;
loc_00284756:
loc_00284759:
    if (condition_is_below) goto loc_00284D11;
    if (1 != 0) goto loc_00284D53;
loc_0028476E:
    v_stack_m98 = 0;
    if ((((unsigned __int8)(a4)) & (4)) != 0) goto loc_00284D73;
    if ((((unsigned __int8)(a4)) & (66)) != 0) goto loc_00284F6B;
loc_00284788:
    if (v_stack_p20 == 0) goto loc_00285049;
    v_stack_m88 = -1;
loc_0028479F:
    if (((v_stack_p18) & (1)) != 0) goto loc_002851C3;
loc_002847B7:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r14 + 34)) & (7));
    if (((unsigned __int8)(result)) != 6) goto loc_002853BC;
    a1 = (*(unsigned __int64 *)(v_r14 + 24)) & (0);
    a1 = (a1) - 1;
    result = (*(unsigned __int64 *)(v_r14 + 24)) ^ (a1);
    result = (result) & (0);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_r14 + 24) = result;
    if (a1 != 0) goto loc_00284F4F;
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    if (!sign_flag) goto loc_00284956;
    result = (*(unsigned __int64 *)(v_r14 + 16)) >> (5);
    v_stack_m78 = result;
    v_stack_m90 = 0;
loc_0028484B:
    if (0 >= 1) goto loc_00284908;
    v_rbp = (unsigned int)((*(unsigned __int64 *)(v_r14 + 8)) >> (3));
    v_rbp = (unsigned int)((v_rbp) & (511));
    result = *(unsigned __int64 *)(v_r14 + 40);
    v_r10 = 0;
    if (0 == 0) {
        a1 = *(unsigned __int64 *)(v_r14 + 40);
        a3 = 0x80000000ULL;
        a1 = (a1) & (0);
        a2 = 0;
        result = MiMapPageInHyperSpaceWorker(a1, a2, a3, (unsigned int)(0xFFFFULL));
        v_r10 = v_stack_m90;
        a3 = result;
    }
    a4 = (*(unsigned __int64 *)(a3 + v_rbp * 8)) >> (12);
    a4 = (a4) & (0);
    a2 = (a4 + a4 * 2) << (4);
    a2 = (a2) + (v_rbp);
    if (a2 != v_r14) goto loc_00285360;
    result = (unsigned int)(((unsigned int)(v_stack_m78)) & (31));
    a4 = (a4) << (7);
    result = (result) | (a4);
    result = (result) | (64);
    result = (result) << (5);
    if (*(unsigned __int64 *)(v_rip + 12227509) == 0) goto loc_002848EF;
    if (((result) & (*(unsigned __int64 *)(v_rip + 12227509))) == 0) goto loc_00284F3F;
    result = (result) | (16);
loc_002848EF:
    *(unsigned __int64 *)(a3 + v_rbp * 8) = result;
    v_stack_m90 = v_r10 + 1;
    if ((v_r10 + 1) != 1) goto loc_00284D30;
loc_00284908:
    a3 = (a3) >> (9);
    a3 = (a3) & (v_r10 + 1);
    a3 = (a3) + (v_r10 + 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872)) = 0;
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(v_rip - 2572496);
loc_00284956:
    result = (*(unsigned __int64 *)(v_r14 + 24)) >> (62);
    result = (unsigned int)((result) & (1));
    if (condition_is_not_equal) goto loc_002850D5;
    if ((unsigned int)(result) == 0) goto loc_00284FA2;
    if ((((unsigned __int8)(v_stack_p1B)) & (16)) != 0) goto loc_002853C5;
loc_00284988:
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_p18));
    result = (*(unsigned __int64 *)(v_r14 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m70 = *(unsigned __int64 *)(v_r14 + 16);
    if (condition_is_below) goto loc_002849D9;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_r14 + 16)) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_002849D0;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_m70)) >> (1));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_002849D9;
loc_002849D0:
    if (v_stack_m70 != 0) goto loc_0028524D;
loc_002849D9:
    a1 = (v_r14) - (v_r14);
    a1 = (a1) >> (4);
    a1 = (a1) * (v_rbp);
    result = MiInsertPageInFreeOrZeroedList(a1, 2, a3, (unsigned int)(0xFFFFULL));
loc_002849FE:
    if (v_stack_m88 == -1) goto loc_00284C68;
    v_r14 = (v_stack_m88 + v_stack_m88 * 2) << (4);
    v_r14 = (v_r14) + (v_r14);
loc_00284A2D:
    if (condition_is_below) goto loc_00284F20;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r14 + 34)) & (7));
    if (((unsigned __int8)(result)) != 6) goto loc_002853D3;
    a1 = (*(unsigned __int64 *)(v_r14 + 24)) & (2);
    a1 = (a1) - 1;
    result = (*(unsigned __int64 *)(v_r14 + 24)) ^ (a1);
    result = (result) & (0);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_r14 + 24) = result;
    if (a1 != 0) goto loc_00284F62;
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    if (!sign_flag) goto loc_00284BBC;
    v_r10 = (*(unsigned __int64 *)(v_r14 + 16)) >> (5);
    v_stack_m78 = v_r10;
loc_00284AB9:
    if (0 >= 1) goto loc_00284B70;
    v_rbp = (unsigned int)((*(unsigned __int64 *)(v_r14 + 8)) >> (3));
    v_rbp = (unsigned int)((v_rbp) & (511));
    result = *(unsigned __int64 *)(v_r14 + 40);
    if (0 == 0) {
        a1 = *(unsigned __int64 *)(v_r14 + 40);
        a3 = 0x80000000ULL;
        a1 = (a1) & (2);
        a2 = 0;
        result = MiMapPageInHyperSpaceWorker(a1, a2, a3, (unsigned int)(0xFFFFULL));
        v_r10 = v_stack_m78;
        a3 = result;
    }
    a4 = (*(unsigned __int64 *)(a3 + v_rbp * 8)) >> (12);
    a4 = (a4) & (0);
    a2 = (a4 + a4 * 2) << (4);
    a2 = (a2) + (v_rbp);
    if (a2 != v_r14) goto loc_0028538E;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) & (31));
    a4 = (a4) << (7);
    result = (result) | (a4);
    result = (result) | (64);
    result = (result) << (5);
    if (*(unsigned __int64 *)(v_rip + 12226891) == 0) goto loc_00284B5C;
    if (((*(unsigned __int64 *)(v_rip + 12226891)) & (result)) == 0) goto loc_00284F47;
    result = (result) | (16);
loc_00284B5C:
    *(unsigned __int64 *)(a3 + v_rbp * 8) = result;
    if ((v_r13 + 1) != 1) goto loc_00284EF2;
loc_00284B70:
    a3 = (a3) >> (9);
    a3 = (a3) & (v_r13 + 1);
    a3 = (a3) + (v_r13 + 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872)) = 0;
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(v_rip - 2573106);
loc_00284BBC:
    result = (*(unsigned __int64 *)(v_r14 + 24)) >> (62);
    result = (unsigned int)((result) & (1));
    if (condition_is_not_equal) goto loc_00285151;
    if ((unsigned int)(result) == 0) goto loc_00284FFC;
    if ((((unsigned __int8)(v_stack_p1B)) & (16)) != 0) goto loc_002853DC;
loc_00284BF2:
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_p18));
    result = (*(unsigned __int64 *)(v_r14 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m68 = *(unsigned __int64 *)(v_r14 + 16);
    if (condition_is_below) goto loc_00284C43;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_r14 + 16)) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00284C3A;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_m68)) >> (1));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00284C43;
loc_00284C3A:
    if (v_stack_m68 != 0) goto loc_0028525D;
loc_00284C43:
    a1 = (v_r14) - (v_r14);
    a1 = (a1) >> (4);
    a1 = (a1) * (v_r14);
    result = MiInsertPageInFreeOrZeroedList(a1, 2, a3, a4);
loc_00284C68:
    if (0 != 0) {
        a1 = v_stack_m98;
        a3 = 1;
        a2 = 0;
        result = MiReleasePageFileInfo(a1, a2, a3, a4);
    }
    result = (unsigned __int8)(((unsigned int)(v_stack_p20)) + ((unsigned __int8)((unsigned int)(v_stack_p20))));
    result = (unsigned __int8)((result) | (1));
    v_r12 = (unsigned int)((v_r12) >> (3));
    v_stack_p11 = (unsigned __int8)(result);
    v_r12 = (unsigned __int16)((v_r12) & (511));
    v_stack_p10 = (unsigned __int8)(v_rsi);
    v_stack_p12 = (unsigned __int16)(v_r12);
    v_rsp = (v_rsp) + (144);
    return (unsigned int)(v_stack_p10);
loc_00284CE2:
    if (condition_is_below) goto loc_00284CFA;
    if (!sign_flag) goto loc_00285287;
loc_00284CFA:
    if (condition_is_above_or_equal) goto loc_00284723;
loc_00284D09:
    goto loc_00284756;
loc_00284D11:
    v_rdi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 13895059)) & ((unsigned int)(v_rdi))) == 0) goto loc_00285299;
loc_00284D1F:
loc_00284D21:
    if (!sign_flag) goto loc_00284759;
    goto loc_00284D11;
loc_00284D30:
    result = (*(unsigned __int64 *)(v_r14)) & (a2);
    v_r15 = (result + result * 2) << (4);
    v_r15 = (v_r15) + ((unsigned int)((unsigned int)(v_r13 + 1)));
    goto loc_0028484B;
loc_00284D53:
    result = MiConfirmPageIsZero(v_r14, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0028476E;
    result = MiRewriteTrimPteAsDemandZero(v_r15, v_r14, a3, a4);
    v_stack_p30 = v_r13 + 1;
loc_00284D73:
    result = MiGetContainingPageTable(v_r12, v_r14, a3, a4);
    v_stack_pE0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    a1 = (*(unsigned __int64 *)(v_r14 + 40)) & (a3);
    *(unsigned __int64 *)(v_r14 + 40) = a1;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 32))) >> (16));
    a2 = (unsigned __int8)((a2) & (199));
    v_stack_pE2 = (unsigned __int8)(a2);
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_pE0));
    if (!(condition_is_above_or_equal)) {
        a1 = *(unsigned int *)(v_r14 + 36);
        a1 = (unsigned int)((a1) & (0x18000000ULL));
    }
    *(unsigned int *)(v_r14 + 36) = (unsigned int)(a1);
    result = (*(unsigned __int64 *)(v_r14 + 24)) & ((unsigned int)((unsigned int)(v_r13 + 1)));
    *(unsigned __int64 *)(v_r14 + 24) = result;
    v_stack_pE0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    v_stack_pE0 = (unsigned __int16)(v_r13 + 1);
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_pE0));
    v_stack_p48 = *(unsigned __int64 *)(v_r14 + 16);
    result = (unsigned __int8)((*(unsigned __int64 *)(v_r14 + 16)) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_002852C0;
    v_stack_p48 = v_r13 + 1;
loc_00284E2A:
    if (v_r13 + 1 != 0) goto loc_002853EA;
loc_00284E33:
    a1 = (v_r14) - (result);
    a1 = (a2) >> (3);
    result = (a1) >> (63);
    a1 = (a1) + (result);
    v_rbx = (unsigned int)((v_stack_p8) & (4));
    a2 = (v_rbx != 0) ? 1 : 0;
    a2 = (unsigned int)((a2) + 1);
    result = MiInsertPageInFreeOrZeroedList(a1, a2, a3, a4);
    v_r14 = (result + result * 2) << (4);
    v_r14 = (v_r14) + (result);
loc_00284E9E:
    if (condition_is_below) goto loc_00285060;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r14 + 34)) & (7));
    if (((unsigned __int8)(result)) != 6) goto loc_0028540C;
    a1 = (*(unsigned __int64 *)(v_r14 + 24)) & (a2);
    a1 = (a1) - 1;
    result = (*(unsigned __int64 *)(v_r14 + 24)) ^ (a1);
    result = (result) & ((unsigned int)((unsigned int)(v_r13 + 1)));
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_r14 + 24) = result;
    if (a1 != 0) goto loc_00284F62;
    a2 = 0;
    result = MiPfnShareCountIsZero(v_r14, a2, a3, a4);
    goto loc_00284C68;
loc_00284EF2:
    result = (*(unsigned __int64 *)(result)) & (0);
    v_r15 = (result + result * 2) << (4);
    v_r15 = (v_r15) + ((unsigned int)((unsigned int)(v_r13 + 1)));
    goto loc_00284AB9;
loc_00284F20:
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(v_r13 + 1))) + 1);
    if (((*(unsigned int *)(v_rip + 13894532)) & ((unsigned int)(v_rbp))) == 0) goto loc_002852D4;
loc_00284F2E:
loc_00284F30:
    if (!sign_flag) goto loc_00284A2D;
    goto loc_00284F20;
loc_00284F3F:
    result = (*(unsigned __int64 *)(v_r14 + 24)) | (0);
    goto loc_002848EF;
loc_00284F47:
    result = (result) | (0);
    goto loc_00284B5C;
loc_00284F4F:
loc_00284F53:
    goto loc_002849FE;
loc_00284F62:
    goto loc_00284C68;
loc_00284F6B:
    result = MiCaptureDirtyBitToPfn(v_r14, a2, a3, a4);
    if (result == 0) goto loc_00284788;
    a1 = (*(unsigned __int64 *)(v_r14 + 40)) >> (43);
    a1 = (unsigned int)((a1) & (0x3FFULL));
    v_stack_p30 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12235006) + a1 * 8);
    goto loc_00284788;
loc_00284FA2:
    result = MI_READ_PTE_LOCK_FREE(v_r14 + 16, a2, a3, a4);
    a1 = v_rbx;
    if (condition_is_below) { a1 = 0xFFFFFFFFFFFFF7FFULL; }
    a1 = (a1) & (result);
    *(unsigned __int64 *)(v_r14 + 16) = a1;
    if ((((unsigned __int8)(v_stack_pE2)) & (16)) == 0) goto loc_00285081;
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_pE0));
    result = MiInsertPageInList(v_r14, 8, a3, a4);
    goto loc_002849FE;
loc_00284FFC:
    result = MI_READ_PTE_LOCK_FREE(v_r14 + 16, 8, a3, a4);
    if (condition_is_below) { v_rbx = 0xFFFFFFFFFFFFF7FFULL; }
    v_rbx = (v_rbx) & (result);
    *(unsigned __int64 *)(v_r14 + 16) = v_rbx;
    if ((((unsigned __int8)(v_stack_pE2)) & (16)) == 0) goto loc_002850B0;
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_pE0));
    result = MiInsertPageInList(v_r14, 8, a3, a4);
    goto loc_00284C68;
loc_00285049:
    result = MiGetContainingPageTable(v_r12, 8, a3, a4);
    v_stack_p40 = result;
    goto loc_0028479F;
loc_00285060:
    v_r13 = (unsigned int)((v_r13 + 1) + 1);
    if (((*(unsigned int *)(v_rip + 13894210)) & ((unsigned int)(v_r13))) == 0) goto loc_0028530C;
loc_00285070:
loc_00285072:
    if (!sign_flag) goto loc_00284E9E;
    goto loc_00285060;
loc_00285081:
    result = (unsigned __int8)((*(unsigned __int64 *)(v_r14 + 24)) & (250));
    result = (unsigned __int8)((result) | (2));
    v_stack_pE2 = (unsigned __int8)(result);
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_pE0));
    result = MiInsertPageInList(v_r12, 4, a3, a4);
    goto loc_002849FE;
loc_002850B0:
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (2));
    v_stack_pE2 = (unsigned __int8)(result);
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_pE0));
    result = MiInsertPageInList(v_r12, 4, a3, a4);
    goto loc_00284C68;
loc_002850D5:
    if ((unsigned int)(result) != 0) goto loc_0028526D;
    if ((((unsigned __int8)(v_stack_pE2)) & (16)) == 0) goto loc_00285334;
    result = (unsigned __int8)((v_stack_pE2) & (251));
    result = (unsigned __int8)((result) | (3));
loc_002850F1:
    v_stack_pE2 = (unsigned __int8)(result);
loc_002850F8:
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_pE0));
    if (condition_is_below) goto loc_00284F53;
    result = MiGetPagingFileOffset(*(unsigned __int64 *)(v_r14 + 16), 4, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_002849FE;
    result = (*(unsigned __int64 *)(v_r14 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234576) + result * 8) + 723) = 1;
    goto loc_002849FE;
loc_00285151:
    if ((unsigned int)(result) != 0) goto loc_0028527A;
    if ((((unsigned __int8)(v_stack_pE2)) & (16)) == 0) goto loc_00285341;
    result = (unsigned __int8)((v_stack_pE2) & (251));
    result = (unsigned __int8)((result) | (3));
loc_0028516D:
    v_stack_pE2 = (unsigned __int8)(result);
loc_00285174:
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_pE0));
    if (condition_is_below) goto loc_00284C68;
    result = MiGetPagingFileOffset(*(unsigned __int64 *)(v_r14 + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234576) + result * 8), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00284C68;
    result = (*(unsigned __int64 *)(v_r14 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8) + 723) = 1;
    goto loc_00284C68;
loc_002851C3:
    result = (*(unsigned __int64 *)(v_r14 + 24)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8));
    if (result != 1) goto loc_002847B7;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r14 + 32)))) != 1) goto loc_002847B7;
    if (((*(unsigned __int8 *)(v_r14 + 34)) & (16)) != 0) goto loc_002847B7;
    result = MiGetPfnPriority(v_r14, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8), a3, a4);
    if (((unsigned int)(result)) != 5) goto loc_002847B7;
    v_stack_pE0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 32))) >> (24));
    result = (unsigned __int8)((result) & (252));
    result = (unsigned __int8)((result) | (4));
    v_stack_pE3 = (unsigned __int8)(result);
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_pE0));
    goto loc_002847B7;
loc_00285231:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8)) > result) goto loc_00284693;
    v_rsi = (*(unsigned __int64 *)(v_r14)) >> (42);
    v_rsi = (unsigned __int8)((v_rsi) & (7));
    goto loc_002846AE;
loc_0028524D:
    result = MiReleasePageFileInfo(v_r14, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8), 1, a4);
    goto loc_002849D9;
loc_0028525D:
    result = MiReleasePageFileInfo(v_r14, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8), 1, a4);
    goto loc_00284C43;
loc_0028526D:
    goto loc_002850F8;
loc_0028527A:
    goto loc_00285174;
loc_00285287:
    if (*(unsigned __int64 *)(v_r14 + 8) != 0) goto loc_00284D09;
    goto loc_00284CFA;
loc_00285299:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13899801)))) & (64)) == 0) goto loc_00284D1F;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_r14, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8), 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00284D1F;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8), 1, a4);
    goto loc_00284D21;
loc_002852C0:
    result = MiClearPageFileReservation(v_stack_p48, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8), 1, a4);
    goto loc_00284E2A;
loc_002852D4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13899742)))) & (64)) == 0) goto loc_00284F2E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p48, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8), 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00284F2E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8), 1, a4);
    goto loc_00284F30;
loc_002852FB:
    if (((unsigned int)((unsigned int)(v_rbp))) > v_stack_p48) goto loc_00284723;
    goto loc_00284D09;
loc_0028530C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13899686)))) & (64)) == 0) goto loc_00285070;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbp)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8), 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00285070;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r13)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12234462) + result * 8), 1, a4);
    goto loc_00285072;
loc_00285334:
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_0028534E;
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (2));
    goto loc_002850F1;
loc_00285341:
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_00285357;
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (2));
    goto loc_0028516D;
loc_0028534E:
    result = (unsigned __int8)((result) & (251));
    result = (unsigned __int8)((result) | (3));
    goto loc_002850F1;
loc_00285357:
    result = (unsigned __int8)((result) & (251));
    result = (unsigned __int8)((result) | (3));
    goto loc_0028516D;
loc_00285360:
    v_r15 = (v_r15) - (v_rbp);
    v_stack_p20 = (unsigned int)((unsigned int)(v_r13));
    v_r15 = (v_r15) >> (4);
    a3 = (1) * (v_r15);
    result = KeBugCheckEx(6 + 72, 6, a3, a3 + v_rbp * 8);
loc_0028538E:
    v_r15 = (v_r15) - (v_rbp);
    v_stack_p20 = 6 + 72;
    v_r15 = (v_r15) >> (4);
    a3 = (a3) * (v_r15);
    result = KeBugCheckEx(6 + 72, 6, a3, a3 + v_rbp * 8);
loc_002853BC:
    result = MiBadShareCount(v_r14, 6, a3, a3 + v_rbp * 8);
loc_002853C5:
    result = (unsigned __int8)((result) & (239));
    v_stack_pE3 = (unsigned __int8)(result);
    goto loc_00284988;
loc_002853D3:
    result = MiBadShareCount(v_r14, 6, a3, a3 + v_rbp * 8);
loc_002853DC:
    result = (unsigned __int8)((result) & (239));
    v_stack_pE3 = (unsigned __int8)(result);
    goto loc_00284BF2;
loc_002853EA:
    result = (*(unsigned __int64 *)(v_r14 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_p30 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12233875) + result * 8);
    goto loc_00284E33;
loc_0028540C:
    result = MiBadShareCount(v_r14, 6, a3, a3 + v_rbp * 8);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiWsleFree(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_p10;
    uint8_t v_stack_p11;
    uint16_t v_stack_p12;
    uint32_t v_stack_p18;
    uint8_t v_stack_p1B;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;
    uint32_t v_stack_pE0;
    uint8_t v_stack_pE2;
    uint8_t v_stack_pE3;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (144);
    local_r12 = (Arg2) >> (9);
    local_r13 = 0;
    v_stack_p10 = 0;
    local_r12 = (local_r12) & (result);
    local_r12 = (local_r12) + (local_rbp);
    result = (Arg4) >> (12);
    result = (result) & (Arg1);
    local_r14 = (result + result * 2) << (4);
    local_r14 = (local_r14) + (result);
    if (Arg2 >= local_rbp) goto loc_00285231;
loc_00284693:
    local_rsi = (Arg4) >> (60);
    local_rsi = (uint8_t)((local_rsi) & (7));
    result = (Arg4) >> (56);
    local_rsi = (uint8_t)((local_rsi) << (4));
    result = (uint8_t)((result) & (15));
    local_rsi = (uint8_t)((local_rsi) | ((uint8_t)(result)));
loc_002846AE:
    Arg1 = (!sign_flag) ? 1 : 0;
    v_stack_p20 = (uint32_t)(Arg1);
    if ((((uint8_t)(Arg3)) & (4)) != 0) goto loc_00284D09;
    if (sign_flag) goto loc_00284CE2;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (((uint8_t)(result)) >= 1) goto loc_00284D09;
    Arg3 = 0;
    Arg2 = 0;
    result = MiGetPagePrivilege(local_r14, Arg2, Arg3, Arg4);
    if ((((uint32_t)(result)) & (0xFFFFFFFDULL)) != 0) goto loc_00284D09;
    Arg1 = (local_r12) << (25);
    result = (local_rbp) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    if (Arg1 >= local_rbp) goto loc_002852FB;
loc_00284723:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)))) != 1) goto loc_00284D09;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) >> (16));
    result = (uint8_t)((result) & (192));
    if (((uint8_t)(result)) != 64) goto loc_00284D09;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_00284D09;
loc_00284756:
loc_00284759:
    if (condition_is_below) goto loc_00284D11;
    if (1 != 0) goto loc_00284D53;
loc_0028476E:
    v_stack_m98 = 0;
    if ((((uint8_t)(Arg4)) & (4)) != 0) goto loc_00284D73;
    if ((((uint8_t)(Arg4)) & (66)) != 0) goto loc_00284F6B;
loc_00284788:
    if (v_stack_p20 == 0) goto loc_00285049;
    v_stack_m88 = -1;
loc_0028479F:
    if (((v_stack_p18) & (1)) != 0) goto loc_002851C3;
loc_002847B7:
    result = (uint8_t)((*(uint8_t *)(local_r14 + 0x22)) & (7));
    if (((uint8_t)(result)) != 6) goto loc_002853BC;
    Arg1 = (*(uint64_t *)(local_r14 + 0x18)) & (0);
    Arg1 = (Arg1) - 1;
    result = (*(uint64_t *)(local_r14 + 0x18)) ^ (Arg1);
    result = (result) & (0);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_r14 + 0x18) = result;
    if (Arg1 != NULL) goto loc_00284F4F;
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    if (!sign_flag) goto loc_00284956;
    result = (*(uint64_t *)(local_r14 + 0x10)) >> (5);
    v_stack_m78 = result;
    v_stack_m90 = 0;
loc_0028484B:
    if (0 >= 1) goto loc_00284908;
    local_rbp = (uint32_t)((*(uint64_t *)(local_r14 + 0x8)) >> (3));
    local_rbp = (uint32_t)((local_rbp) & (511));
    result = *(uint64_t *)(local_r14 + 0x28);
    local_r10 = 0;
    if (0 == 0) {
        Arg1 = *(uint64_t *)(local_r14 + 0x28);
        Arg3 = 0x80000000ULL;
        Arg1 = (Arg1) & (0);
        Arg2 = 0;
        result = MiMapPageInHyperSpaceWorker(Arg1, Arg2, Arg3, (uint32_t)(0xFFFFULL));
        local_r10 = v_stack_m90;
        Arg3 = result;
    }
    Arg4 = (*(uint64_t *)(Arg3 + local_rbp * 8)) >> (12);
    Arg4 = (Arg4) & (0);
    Arg2 = (Arg4 + Arg4 * 2) << (4);
    Arg2 = (Arg2) + (local_rbp);
    if (Arg2 != local_r14) goto loc_00285360;
    result = (uint32_t)(((uint32_t)(v_stack_m78)) & (31));
    Arg4 = (Arg4) << (7);
    result = (result) | (Arg4);
    result = (result) | (64);
    result = (result) << (5);
    if (*(uint64_t *)(v_rip + 0xBA93B5) == 0) goto loc_002848EF;
    if (((result) & (*(uint64_t *)(v_rip + 0xBA93B5))) == 0) goto loc_00284F3F;
    result = (result) | (16);
loc_002848EF:
    *(uint64_t *)(Arg3 + local_rbp * 8) = result;
    v_stack_m90 = local_r10 + 1;
    if ((local_r10 + 1) != 1) goto loc_00284D30;
loc_00284908:
    Arg3 = (Arg3) >> (9);
    Arg3 = (Arg3) & (local_r10 + 1);
    Arg3 = (Arg3) + (local_r10 + 1);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838)) = 0;
    *(uint64_t *)(Arg3) = *(uint64_t *)(v_rip - 0x2740D0);
loc_00284956:
    result = (*(uint64_t *)(local_r14 + 0x18)) >> (62);
    result = (uint32_t)((result) & (1));
    if (condition_is_not_equal) goto loc_002850D5;
    if ((uint32_t)(result) == 0) goto loc_00284FA2;
    if ((((uint8_t)(v_stack_p1B)) & (16)) != 0) goto loc_002853C5;
loc_00284988:
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_p18));
    result = (*(uint64_t *)(local_r14 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m70 = *(uint64_t *)(local_r14 + 0x10);
    if (condition_is_below) goto loc_002849D9;
    result = (uint8_t)((*(uint64_t *)(local_r14 + 0x10)) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_002849D0;
    result = (uint8_t)(((uint8_t)(v_stack_m70)) >> (1));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_002849D9;
loc_002849D0:
    if (v_stack_m70 != 0) goto loc_0028524D;
loc_002849D9:
    Arg1 = (local_r14) - (local_r14);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (local_rbp);
    result = MiInsertPageInFreeOrZeroedList(Arg1, 2, Arg3, (uint32_t)(0xFFFFULL));
loc_002849FE:
    if (v_stack_m88 == -1) goto loc_00284C68;
    local_r14 = (v_stack_m88 + v_stack_m88 * 2) << (4);
    local_r14 = (local_r14) + (local_r14);
loc_00284A2D:
    if (condition_is_below) goto loc_00284F20;
    result = (uint8_t)((*(uint8_t *)(local_r14 + 0x22)) & (7));
    if (((uint8_t)(result)) != 6) goto loc_002853D3;
    Arg1 = (*(uint64_t *)(local_r14 + 0x18)) & (2);
    Arg1 = (Arg1) - 1;
    result = (*(uint64_t *)(local_r14 + 0x18)) ^ (Arg1);
    result = (result) & (0);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_r14 + 0x18) = result;
    if (Arg1 != NULL) goto loc_00284F62;
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    if (!sign_flag) goto loc_00284BBC;
    local_r10 = (*(uint64_t *)(local_r14 + 0x10)) >> (5);
    v_stack_m78 = local_r10;
loc_00284AB9:
    if (0 >= 1) goto loc_00284B70;
    local_rbp = (uint32_t)((*(uint64_t *)(local_r14 + 0x8)) >> (3));
    local_rbp = (uint32_t)((local_rbp) & (511));
    result = *(uint64_t *)(local_r14 + 0x28);
    if (0 == 0) {
        Arg1 = *(uint64_t *)(local_r14 + 0x28);
        Arg3 = 0x80000000ULL;
        Arg1 = (Arg1) & (2);
        Arg2 = 0;
        result = MiMapPageInHyperSpaceWorker(Arg1, Arg2, Arg3, (uint32_t)(0xFFFFULL));
        local_r10 = v_stack_m78;
        Arg3 = result;
    }
    Arg4 = (*(uint64_t *)(Arg3 + local_rbp * 8)) >> (12);
    Arg4 = (Arg4) & (0);
    Arg2 = (Arg4 + Arg4 * 2) << (4);
    Arg2 = (Arg2) + (local_rbp);
    if (Arg2 != local_r14) goto loc_0028538E;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) & (31));
    Arg4 = (Arg4) << (7);
    result = (result) | (Arg4);
    result = (result) | (64);
    result = (result) << (5);
    if (*(uint64_t *)(v_rip + 0xBA914B) == 0) goto loc_00284B5C;
    if (((*(uint64_t *)(v_rip + 0xBA914B)) & (result)) == 0) goto loc_00284F47;
    result = (result) | (16);
loc_00284B5C:
    *(uint64_t *)(Arg3 + local_rbp * 8) = result;
    if ((local_r13 + 1) != 1) goto loc_00284EF2;
loc_00284B70:
    Arg3 = (Arg3) >> (9);
    Arg3 = (Arg3) & (local_r13 + 1);
    Arg3 = (Arg3) + (local_r13 + 1);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838)) = 0;
    *(uint64_t *)(Arg3) = *(uint64_t *)(v_rip - 0x274332);
loc_00284BBC:
    result = (*(uint64_t *)(local_r14 + 0x18)) >> (62);
    result = (uint32_t)((result) & (1));
    if (condition_is_not_equal) goto loc_00285151;
    if ((uint32_t)(result) == 0) goto loc_00284FFC;
    if ((((uint8_t)(v_stack_p1B)) & (16)) != 0) goto loc_002853DC;
loc_00284BF2:
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_p18));
    result = (*(uint64_t *)(local_r14 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m68 = *(uint64_t *)(local_r14 + 0x10);
    if (condition_is_below) goto loc_00284C43;
    result = (uint8_t)((*(uint64_t *)(local_r14 + 0x10)) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00284C3A;
    result = (uint8_t)(((uint8_t)(v_stack_m68)) >> (1));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00284C43;
loc_00284C3A:
    if (v_stack_m68 != 0) goto loc_0028525D;
loc_00284C43:
    Arg1 = (local_r14) - (local_r14);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (local_r14);
    result = MiInsertPageInFreeOrZeroedList(Arg1, 2, Arg3, Arg4);
loc_00284C68:
    if (0 != 0) {
        Arg1 = v_stack_m98;
        Arg3 = 1;
        Arg2 = 0;
        result = MiReleasePageFileInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint8_t)(((uint32_t)(v_stack_p20)) + ((uint8_t)((uint32_t)(v_stack_p20))));
    result = (uint8_t)((result) | (1));
    local_r12 = (uint32_t)((local_r12) >> (3));
    v_stack_p11 = (uint8_t)(result);
    local_r12 = (uint16_t)((local_r12) & (511));
    v_stack_p10 = (uint8_t)(local_rsi);
    v_stack_p12 = (uint16_t)(local_r12);
    local_rsp = (local_rsp) + (144);
    return (uint32_t)(v_stack_p10);
loc_00284CE2:
    if (condition_is_below) goto loc_00284CFA;
    if (!sign_flag) goto loc_00285287;
loc_00284CFA:
    if (condition_is_above_or_equal) goto loc_00284723;
loc_00284D09:
    goto loc_00284756;
loc_00284D11:
    local_rdi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD40593)) & ((uint32_t)(local_rdi))) == 0) goto loc_00285299;
loc_00284D1F:
loc_00284D21:
    if (!sign_flag) goto loc_00284759;
    goto loc_00284D11;
loc_00284D30:
    result = (*(uint64_t *)(local_r14)) & (Arg2);
    local_r15 = (result + result * 2) << (4);
    local_r15 = (local_r15) + ((uint32_t)((uint32_t)(local_r13 + 1)));
    goto loc_0028484B;
loc_00284D53:
    result = MiConfirmPageIsZero(local_r14, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0028476E;
    result = MiRewriteTrimPteAsDemandZero(local_r15, local_r14, Arg3, Arg4);
    v_stack_p30 = local_r13 + 1;
loc_00284D73:
    result = MiGetContainingPageTable(local_r12, local_r14, Arg3, Arg4);
    v_stack_pE0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    Arg1 = (*(uint64_t *)(local_r14 + 0x28)) & (Arg3);
    *(void **)(local_r14 + 0x28) = Arg1;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) >> (16));
    Arg2 = (uint8_t)((Arg2) & (199));
    v_stack_pE2 = (uint8_t)(Arg2);
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_pE0));
    if (!(condition_is_above_or_equal)) {
        Arg1 = *(uint32_t *)(local_r14 + 0x24);
        Arg1 = (uint32_t)((Arg1) & (0x18000000ULL));
    }
    *(uint32_t *)(local_r14 + 0x24) = (uint32_t)(Arg1);
    result = (*(uint64_t *)(local_r14 + 0x18)) & ((uint32_t)((uint32_t)(local_r13 + 1)));
    *(uint64_t *)(local_r14 + 0x18) = result;
    v_stack_pE0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    v_stack_pE0 = (uint16_t)(local_r13 + 1);
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_pE0));
    v_stack_p48 = *(uint64_t *)(local_r14 + 0x10);
    result = (uint8_t)((*(uint64_t *)(local_r14 + 0x10)) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_002852C0;
    v_stack_p48 = local_r13 + 1;
loc_00284E2A:
    if (local_r13 + 1 != 0) goto loc_002853EA;
loc_00284E33:
    Arg1 = (local_r14) - (result);
    Arg1 = (Arg2) >> (3);
    result = (Arg1) >> (63);
    Arg1 = (Arg1) + (result);
    local_rbx = (uint32_t)((v_stack_p8) & (4));
    Arg2 = (local_rbx != 0) ? 1 : 0;
    Arg2 = (uint32_t)((Arg2) + 1);
    result = MiInsertPageInFreeOrZeroedList(Arg1, Arg2, Arg3, Arg4);
    local_r14 = (result + result * 2) << (4);
    local_r14 = (local_r14) + (result);
loc_00284E9E:
    if (condition_is_below) goto loc_00285060;
    result = (uint8_t)((*(uint8_t *)(local_r14 + 0x22)) & (7));
    if (((uint8_t)(result)) != 6) goto loc_0028540C;
    Arg1 = (*(uint64_t *)(local_r14 + 0x18)) & (Arg2);
    Arg1 = (Arg1) - 1;
    result = (*(uint64_t *)(local_r14 + 0x18)) ^ (Arg1);
    result = (result) & ((uint32_t)((uint32_t)(local_r13 + 1)));
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_r14 + 0x18) = result;
    if (Arg1 != NULL) goto loc_00284F62;
    Arg2 = 0;
    result = MiPfnShareCountIsZero(local_r14, Arg2, Arg3, Arg4);
    goto loc_00284C68;
loc_00284EF2:
    result = (*(uint64_t *)(result)) & (0);
    local_r15 = (result + result * 2) << (4);
    local_r15 = (local_r15) + ((uint32_t)((uint32_t)(local_r13 + 1)));
    goto loc_00284AB9;
loc_00284F20:
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(local_r13 + 1))) + 1);
    if (((*(uint32_t *)(v_rip + 0xD40384)) & ((uint32_t)(local_rbp))) == 0) goto loc_002852D4;
loc_00284F2E:
loc_00284F30:
    if (!sign_flag) goto loc_00284A2D;
    goto loc_00284F20;
loc_00284F3F:
    result = (*(uint64_t *)(local_r14 + 0x18)) | (0);
    goto loc_002848EF;
loc_00284F47:
    result = (result) | (0);
    goto loc_00284B5C;
loc_00284F4F:
loc_00284F53:
    goto loc_002849FE;
loc_00284F62:
    goto loc_00284C68;
loc_00284F6B:
    result = MiCaptureDirtyBitToPfn(local_r14, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00284788;
    Arg1 = (*(uint64_t *)(local_r14 + 0x28)) >> (43);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    v_stack_p30 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAB0FE) + arg1 * 8);
    goto loc_00284788;
loc_00284FA2:
    result = MI_READ_PTE_LOCK_FREE(local_r14 + 16, Arg2, Arg3, Arg4);
    Arg1 = local_rbx;
    if (condition_is_below) { Arg1 = 0xFFFFFFFFFFFFF7FFULL; }
    Arg1 = (Arg1) & (result);
    *(void **)(local_r14 + 0x10) = Arg1;
    if ((((uint8_t)(v_stack_pE2)) & (16)) == 0) goto loc_00285081;
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_pE0));
    result = MiInsertPageInList(local_r14, 8, Arg3, Arg4);
    goto loc_002849FE;
loc_00284FFC:
    result = MI_READ_PTE_LOCK_FREE(local_r14 + 16, 8, Arg3, Arg4);
    if (condition_is_below) { local_rbx = 0xFFFFFFFFFFFFF7FFULL; }
    local_rbx = (local_rbx) & (result);
    *(uint64_t *)(local_r14 + 0x10) = local_rbx;
    if ((((uint8_t)(v_stack_pE2)) & (16)) == 0) goto loc_002850B0;
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_pE0));
    result = MiInsertPageInList(local_r14, 8, Arg3, Arg4);
    goto loc_00284C68;
loc_00285049:
    result = MiGetContainingPageTable(local_r12, 8, Arg3, Arg4);
    v_stack_p40 = result;
    goto loc_0028479F;
loc_00285060:
    local_r13 = (uint32_t)((local_r13 + 1) + 1);
    if (((*(uint32_t *)(v_rip + 0xD40242)) & ((uint32_t)(local_r13))) == 0) goto loc_0028530C;
loc_00285070:
loc_00285072:
    if (!sign_flag) goto loc_00284E9E;
    goto loc_00285060;
loc_00285081:
    result = (uint8_t)((*(uint64_t *)(local_r14 + 0x18)) & (250));
    result = (uint8_t)((result) | (2));
    v_stack_pE2 = (uint8_t)(result);
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_pE0));
    result = MiInsertPageInList(local_r12, 4, Arg3, Arg4);
    goto loc_002849FE;
loc_002850B0:
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (2));
    v_stack_pE2 = (uint8_t)(result);
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_pE0));
    result = MiInsertPageInList(local_r12, 4, Arg3, Arg4);
    goto loc_00284C68;
loc_002850D5:
    if ((uint32_t)(result) != 0) goto loc_0028526D;
    if ((((uint8_t)(v_stack_pE2)) & (16)) == 0) goto loc_00285334;
    result = (uint8_t)((v_stack_pE2) & (251));
    result = (uint8_t)((result) | (3));
loc_002850F1:
    v_stack_pE2 = (uint8_t)(result);
loc_002850F8:
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_pE0));
    if (condition_is_below) goto loc_00284F53;
    result = MiGetPagingFileOffset(*(uint64_t *)(local_r14 + 0x10), 4, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002849FE;
    result = (*(uint64_t *)(local_r14 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAF50) + result * 8) + 0x2D3) = 1;
    goto loc_002849FE;
loc_00285151:
    if ((uint32_t)(result) != 0) goto loc_0028527A;
    if ((((uint8_t)(v_stack_pE2)) & (16)) == 0) goto loc_00285341;
    result = (uint8_t)((v_stack_pE2) & (251));
    result = (uint8_t)((result) | (3));
loc_0028516D:
    v_stack_pE2 = (uint8_t)(result);
loc_00285174:
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_pE0));
    if (condition_is_below) goto loc_00284C68;
    result = MiGetPagingFileOffset(*(uint64_t *)(local_r14 + 0x10), *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAF50) + result * 8), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00284C68;
    result = (*(uint64_t *)(local_r14 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8) + 0x2D3) = 1;
    goto loc_00284C68;
loc_002851C3:
    result = (*(uint64_t *)(local_r14 + 0x18)) & (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8));
    if (result != 1) goto loc_002847B7;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)))) != 1) goto loc_002847B7;
    if (((*(uint8_t *)(local_r14 + 0x22)) & (16)) != 0) goto loc_002847B7;
    result = MiGetPfnPriority(local_r14, *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8), Arg3, Arg4);
    if (((uint32_t)(result)) != 5) goto loc_002847B7;
    v_stack_pE0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) >> (24));
    result = (uint8_t)((result) & (252));
    result = (uint8_t)((result) | (4));
    v_stack_pE3 = (uint8_t)(result);
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_pE0));
    goto loc_002847B7;
loc_00285231:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8)) > result) goto loc_00284693;
    local_rsi = (*(uint64_t *)(local_r14)) >> (42);
    local_rsi = (uint8_t)((local_rsi) & (7));
    goto loc_002846AE;
loc_0028524D:
    result = MiReleasePageFileInfo(local_r14, *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8), 1, Arg4);
    goto loc_002849D9;
loc_0028525D:
    result = MiReleasePageFileInfo(local_r14, *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8), 1, Arg4);
    goto loc_00284C43;
loc_0028526D:
    goto loc_002850F8;
loc_0028527A:
    goto loc_00285174;
loc_00285287:
    if (*(uint64_t *)(local_r14 + 0x8) != 0) goto loc_00284D09;
    goto loc_00284CFA;
loc_00285299:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD41819)))) & (64)) == 0) goto loc_00284D1F;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_r14, *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8), 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00284D1F;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(result)), *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8), 1, Arg4);
    goto loc_00284D21;
loc_002852C0:
    result = MiClearPageFileReservation(v_stack_p48, *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8), 1, Arg4);
    goto loc_00284E2A;
loc_002852D4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD417DE)))) & (64)) == 0) goto loc_00284F2E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p48, *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8), 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00284F2E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8), 1, Arg4);
    goto loc_00284F30;
loc_002852FB:
    if (((uint32_t)((uint32_t)(local_rbp))) > v_stack_p48) goto loc_00284723;
    goto loc_00284D09;
loc_0028530C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD417A6)))) & (64)) == 0) goto loc_00285070;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbp)), *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8), 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00285070;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r13)), *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAEDE) + result * 8), 1, Arg4);
    goto loc_00285072;
loc_00285334:
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_0028534E;
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (2));
    goto loc_002850F1;
loc_00285341:
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_00285357;
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (2));
    goto loc_0028516D;
loc_0028534E:
    result = (uint8_t)((result) & (251));
    result = (uint8_t)((result) | (3));
    goto loc_002850F1;
loc_00285357:
    result = (uint8_t)((result) & (251));
    result = (uint8_t)((result) | (3));
    goto loc_0028516D;
loc_00285360:
    local_r15 = (local_r15) - (local_rbp);
    v_stack_p20 = (uint32_t)((uint32_t)(local_r13));
    local_r15 = (local_r15) >> (4);
    Arg3 = (1) * (local_r15);
    result = KeBugCheckEx(6 + 72, 6, Arg3, Arg3 + local_rbp * 8);
loc_0028538E:
    local_r15 = (local_r15) - (local_rbp);
    v_stack_p20 = 6 + 72;
    local_r15 = (local_r15) >> (4);
    Arg3 = (Arg3) * (local_r15);
    result = KeBugCheckEx(6 + 72, 6, Arg3, Arg3 + local_rbp * 8);
loc_002853BC:
    result = MiBadShareCount(local_r14, 6, Arg3, Arg3 + local_rbp * 8);
loc_002853C5:
    result = (uint8_t)((result) & (239));
    v_stack_pE3 = (uint8_t)(result);
    goto loc_00284988;
loc_002853D3:
    result = MiBadShareCount(local_r14, 6, Arg3, Arg3 + local_rbp * 8);
loc_002853DC:
    result = (uint8_t)((result) & (239));
    v_stack_pE3 = (uint8_t)(result);
    goto loc_00284BF2;
loc_002853EA:
    result = (*(uint64_t *)(local_r14 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_p30 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xBAAC93) + result * 8);
    goto loc_00284E33;
loc_0028540C:
    result = MiBadShareCount(local_r14, 6, Arg3, Arg3 + local_rbp * 8);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00284600&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
