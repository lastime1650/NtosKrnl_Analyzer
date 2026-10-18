# MiIssueHardFault

- RVA: `0x00380074`–`0x0038086F` (길이 `2,043` bytes)
- VA: `0x0000000140380074`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007B838`
- 디코드: `477`개 명령, `2,043/2,043` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x003800D4` → [MiGetSessionIdForVa](../34/MiGetSessionIdForVa_function_00346C60.md) (function, `0x00346C60`)
- `0x003800F6` → [MiReferenceInPageFile](MiReferenceInPageFile_function_00380880.md) (function, `0x00380880`)
- `0x0038010C` → [MiReleaseFaultState](../27/MiReleaseFaultState_function_0027D290.md) (function, `0x0027D290`)
- `0x00380187` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00380278` → [EtwGetKernelTraceTimestampSilo](../37/EtwGetKernelTraceTimestampSilo_function_0037FBD0.md) (function, `0x0037FBD0`)
- `0x003802C0` → [MiIssueHardFaultIo](MiIssueHardFaultIo_function_003812EC.md) (function, `0x003812EC`)
- `0x00380327` → [MiWaitForInPageComplete](MiWaitForInPageComplete_function_00380AB8.md) (function, `0x00380AB8`)
- `0x0038033A` → [MiFinishHardFault](../2B/MiFinishHardFault_function_002B6F10.md) (function, `0x002B6F10`)
- `0x0038035E` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003803CF` → [MiMakeTransitionPteValid](../28/MiMakeTransitionPteValid_function_00283D60.md) (function, `0x00283D60`)
- `0x003803DF` → [MI_IS_SOFTWARE_PTE_SHADOW_STACK](MI_IS_SOFTWARE_PTE_SHADOW_STACK_function_003815D0.md) (function, `0x003815D0`)
- `0x0038044A` → [MiAllocateWsle](../33/MiAllocateWsle_function_003332C0.md) (function, `0x003332C0`)
- `0x0038045F` → [MiGetVmAccessLoggingPartition](MiGetVmAccessLoggingPartition_function_003815A0.md) (function, `0x003815A0`)
- `0x003804EF` → [MiZeroPhysicalPage](../33/MiZeroPhysicalPage_function_00332590.md) (function, `0x00332590`)
- `0x00380543` → [MiCompleteProtoPteFault](../34/MiCompleteProtoPteFault_function_00345710.md) (function, `0x00345710`)
- `0x00380590` → [MiOkToSetPteDirtyForNotValidFault](../43/MiOkToSetPteDirtyForNotValidFault_function_00437820.md) (function, `0x00437820`)
- `0x003805C5` → [MiGetPagingFileOffset](../36/MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x003805D9` → [MiLockPageAndSetDirty](../28/MiLockPageAndSetDirty_function_002857A0.md) (function, `0x002857A0`)
- `0x003805F4` → [MiGetEffectivePagePriorityThread](../36/MiGetEffectivePagePriorityThread_function_003626E0.md) (function, `0x003626E0`)
- `0x00380613` → [MiLogPageAccess](../24/MiLogPageAccess_function_00240870.md) (function, `0x00240870`)
- `0x00380684` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00380745` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00380751` → [MiRelockFaultState](../36/MiRelockFaultState_function_0036A230.md) (function, `0x0036A230`)
- `0x00380760` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00380785` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x003807A8` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x003807B8` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x0038081B` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x0038085F` → [MiLockAndDecrementShareCount](../2A/MiLockAndDecrementShareCount_function_002A2854.md) (function, `0x002A2854`)

### Direct callers
- [sub_0027F2B0](../27/Unknown_function_0027F2B0.md) at `0x0027F2EF`
- [MiInPagePageTable](../3E/MiInPagePageTable_function_003EF8DC.md) at `0x003EFE14`

### Static image references
- `0x00380099` → RVA `0x00E0A740` (`.data`; read)
- `0x00380177` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003801EB` → RVA `0x00FC6B00` (`ALMOSTRO`; reference)
- `0x00380280` → RVA `0x00F0F22C` (`.data`; read)
- `0x0038078C` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0038083E` → RVA `0x00E38860` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00380845` → [sub_006E4560](../6E/Unknown_function_006E4560.md) (`tail-transfer`)
  - `0x00380852` → [sub_006E4560](../6E/Unknown_function_006E4560.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00380074  40 55                           push rbp
00380076  41 54                           push r12
00380078  41 55                           push r13
0038007A  41 56                           push r14
0038007C  41 57                           push r15
0038007E  48 81 EC 80 00 00 00            sub rsp, 0x80
00380085  48 8D 6C 24 40                  lea rbp, [rsp + 0x40]
0038008A  48 89 5D 70                     mov qword ptr [rbp + 0x70], rbx
0038008E  48 89 75 78                     mov qword ptr [rbp + 0x78], rsi
00380092  48 89 BD 80 00 00 00            mov qword ptr [rbp + 0x80], rdi
00380099  48 8B 05 A0 A6 A8 00            mov rax, qword ptr [rip + 0xa8a6a0]
003800A0  48 33 C5                        xor rax, rbp
003800A3  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
003800A7  4C 8B F2                        mov r14, rdx
003800AA  4C 8B E1                        mov r12, rcx
003800AD  33 D2                           xor edx, edx
003800AF  88 55 00                        mov byte ptr [rbp], dl
003800B2  8B DA                           mov ebx, edx
003800B4  48 89 55 08                     mov qword ptr [rbp + 8], rdx
003800B8  41 8B B6 C0 00 00 00            mov esi, dword ptr [r14 + 0xc0]
003800BF  48 8B 09                        mov rcx, qword ptr [rcx]
003800C2  4D 8B BE 98 00 00 00            mov r15, qword ptr [r14 + 0x98]
003800C9  49 89 8E E0 00 00 00            mov qword ptr [r14 + 0xe0], rcx
003800D0  48 89 55 28                     mov qword ptr [rbp + 0x28], rdx
003800D4  E8 87 6B FC FF                  call 0x140346c60
003800D9  49 8B BE D0 00 00 00            mov rdi, qword ptr [r14 + 0xd0]
003800E0  48 85 FF                        test rdi, rdi
003800E3  0F 85 10 04 00 00               jne 0x1403804f9
003800E9  8B FA                           mov edi, edx
003800EB  41 B8 01 00 00 00               mov r8d, 1
003800F1  8B D0                           mov edx, eax
003800F3  49 8B CE                        mov rcx, r14
003800F6  E8 85 07 00 00                  call 0x140380880
003800FB  49 8D 4C 24 38                  lea rcx, [r12 + 0x38]
00380100  BA 01 00 00 00                  mov edx, 1
00380105  4C 8D 45 00                     lea r8, [rbp]
00380109  4C 8B E8                        mov r13, rax
0038010C  E8 7F D1 EF FF                  call 0x14027d290
00380111  45 33 C0                        xor r8d, r8d
00380114  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
00380118  49 8B 44 24 10                  mov rax, qword ptr [r12 + 0x10]
0038011D  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00380121  45 8D 50 01                     lea r10d, [r8 + 1]
00380125  4D 85 ED                        test r13, r13
00380128  0F 85 73 03 00 00               jne 0x1403804a1
0038012E  49 8B 86 C8 00 00 00            mov rax, qword ptr [r14 + 0xc8]
00380135  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00380139  49 89 8E C8 00 00 00            mov qword ptr [r14 + 0xc8], rcx
00380140  49 8B 44 24 10                  mov rax, qword ptr [r12 + 0x10]
00380145  41 84 C2                        test r10b, al
00380148  0F 85 CF 04 00 00               jne 0x14038061d
0038014E  45 00 97 AE 05 00 00            add byte ptr [r15 + 0x5ae], r10b
00380155  4D 8D 6C 24 38                  lea r13, [r12 + 0x38]
0038015A  49 8B 7D 00                     mov rdi, qword ptr [r13]
0038015E  8B BF B8 00 00 00               mov edi, dword ptr [rdi + 0xb8]
00380164  40 F6 C7 0F                     test dil, 0xf
00380168  0F 85 13 02 00 00               jne 0x140380381
0038016E  66 41 FF 8F E4 01 00 00         dec word ptr [r15 + 0x1e4]
00380176  90                              nop
00380177  44 39 05 A2 6B C4 00            cmp dword ptr [rip + 0xc46ba2], r8d
0038017E  74 13                           je 0x140380193
00380180  44 0F 20 C1                     mov rcx, cr8
00380184  8A 55 00                        mov dl, byte ptr [rbp]
00380187  E8 0C 55 17 00                  call 0x1404f5698
0038018C  45 33 C0                        xor r8d, r8d
0038018F  45 8D 50 01                     lea r10d, [r8 + 1]
00380193  0F B6 45 00                     movzx eax, byte ptr [rbp]
00380197  44 0F 22 C0                     mov cr8, rax
0038019B  41 8B 96 38 01 00 00            mov edx, dword ptr [r14 + 0x138]
003801A2  8B CA                           mov ecx, edx
003801A4  81 E1 FF 0F 00 00               and ecx, 0xfff
003801AA  0F BA E6 12                     bt esi, 0x12
003801AE  0F 82 02 03 00 00               jb 0x1403804b6
003801B4  45 8B 86 38 01 00 00            mov r8d, dword ptr [r14 + 0x138]
003801BB  45 33 C9                        xor r9d, r9d
003801BE  45 89 86 B8 00 00 00            mov dword ptr [r14 + 0xb8], r8d
003801C5  4C 89 4D 20                     mov qword ptr [rbp + 0x20], r9
003801C9  45 39 4E 24                     cmp dword ptr [r14 + 0x24], r9d
003801CD  0F 85 F7 00 00 00               jne 0x1403802ca
003801D3  8B C6                           mov eax, esi
003801D5  25 20 04 40 00                  and eax, 0x400420
003801DA  3D 20 00 40 00                  cmp eax, 0x400020
003801DF  0F 84 EA 00 00 00               je 0x1403802cf
003801E5  41 BA 00 20 00 00               mov r10d, 0x2000
003801EB  44 85 15 0E 69 C4 00            test dword ptr [rip + 0xc4690e], r10d
003801F2  0F 84 5F 04 00 00               je 0x140380657
003801F8  40 F6 C6 20                     test sil, 0x20
003801FC  0F 85 23 06 00 00               jne 0x140380825
00380202  8B 04 24                        mov eax, dword ptr [rsp]
00380205  48 83 EC 50                     sub rsp, 0x50
00380209  48 8D 7C 24 40                  lea rdi, [rsp + 0x40]
0038020E  8B 07                           mov eax, dword ptr [rdi]
00380210  48 89 7D 20                     mov qword ptr [rbp + 0x20], rdi
00380214  0F BA E6 0A                     bt esi, 0xa
00380218  0F 82 19 04 00 00               jb 0x140380637
0038021E  49 8B 46 60                     mov rax, qword ptr [r14 + 0x60]
00380222  49 8B 96 C8 00 00 00            mov rdx, qword ptr [r14 + 0xc8]
00380229  49 8B 8E E0 00 00 00            mov rcx, qword ptr [r14 + 0xe0]
00380230  48 89 4F 28                     mov qword ptr [rdi + 0x28], rcx
00380234  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
00380238  41 8B 87 10 05 00 00            mov eax, dword ptr [r15 + 0x510]
0038023F  89 47 38                        mov dword ptr [rdi + 0x38], eax
00380242  44 89 47 3C                     mov dword ptr [rdi + 0x3c], r8d
00380246  48 85 D2                        test rdx, rdx
00380249  0F 84 E0 03 00 00               je 0x14038062f
0038024F  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
00380253  48 89 47 30                     mov qword ptr [rdi + 0x30], rax
00380257  44 85 15 A2 68 C4 00            test dword ptr [rip + 0xc468a2], r10d
0038025E  0F 84 A5 04 00 00               je 0x140380709
00380264  4D 8B 87 20 02 00 00            mov r8, qword ptr [r15 + 0x220]
0038026B  41 8B D2                        mov edx, r10d
0038026E  48 8B CF                        mov rcx, rdi
00380271  4D 8B 80 F0 05 00 00            mov r8, qword ptr [r8 + 0x5f0]
00380278  E8 53 F9 FF FF                  call 0x14037fbd0
0038027D  45 33 C9                        xor r9d, r9d
00380280  8B 05 A6 EF B8 00               mov eax, dword ptr [rip + 0xb8efa6]
00380286  BE 01 00 00 00                  mov esi, 1
0038028B  40 84 C6                        test sil, al
0038028E  0F 85 B0 03 00 00               jne 0x140380644
00380294  4C 89 4F 40                     mov qword ptr [rdi + 0x40], r9
00380298  49 8B 7D 00                     mov rdi, qword ptr [r13]
0038029C  8B BF B8 00 00 00               mov edi, dword ptr [rdi + 0xb8]
003802A2  8B C7                           mov eax, edi
003802A4  C1 E8 18                        shr eax, 0x18
003802A7  24 30                           and al, 0x30
003802A9  3C 30                           cmp al, 0x30
003802AB  0F 84 7E 05 00 00               je 0x14038082f
003802B1  4D 8B 44 24 10                  mov r8, qword ptr [r12 + 0x10]
003802B6  83 CB 02                        or ebx, 2
003802B9  8B D3                           mov edx, ebx
003802BB  49 8B CE                        mov rcx, r14
003802BE  23 D6                           and edx, esi
003802C0  E8 27 10 00 00                  call 0x1403812ec
003802C5  45 33 C9                        xor r9d, r9d
003802C8  EB 05                           jmp 0x1403802cf
003802CA  BB 02 00 00 00                  mov ebx, 2
003802CF  41 8B 86 C0 00 00 00            mov eax, dword ptr [r14 + 0xc0]
003802D6  41 B8 01 00 00 00               mov r8d, 1
003802DC  40 0F B6 CF                     movzx ecx, dil
003802E0  03 C9                           add ecx, ecx
003802E2  8B D1                           mov edx, ecx
003802E4  33 D0                           xor edx, eax
003802E6  83 E2 E1                        and edx, 0xffffffe1
003802E9  33 D1                           xor edx, ecx
003802EB  41 89 96 C0 00 00 00            mov dword ptr [r14 + 0xc0], edx
003802F2  49 8B 4C 24 10                  mov rcx, qword ptr [r12 + 0x10]
003802F7  41 84 C8                        test r8b, cl
003802FA  0F 85 5B 02 00 00               jne 0x14038055b
00380300  49 8B BE F8 00 00 00            mov rdi, qword ptr [r14 + 0xf8]
00380307  49 8B B6 E8 00 00 00            mov rsi, qword ptr [r14 + 0xe8]
0038030E  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00380312  48 0F BA E0 28                  bt rax, 0x28
00380317  0F 83 67 01 00 00               jae 0x140380484
0038031D  4C 8D 45 20                     lea r8, [rbp + 0x20]
00380321  49 8B D6                        mov rdx, r14
00380324  49 8B CC                        mov rcx, r12
00380327  E8 8C 07 00 00                  call 0x140380ab8
0038032C  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
00380330  4C 8D 4D 28                     lea r9, [rbp + 0x28]
00380334  4D 8B C6                        mov r8, r14
00380337  49 8B CC                        mov rcx, r12
0038033A  E8 D1 6B F3 FF                  call 0x1402b6f10
0038033F  44 8B F0                        mov r14d, eax
00380342  8B 45 20                        mov eax, dword ptr [rbp + 0x20]
00380345  41 FE 8F AE 05 00 00            dec byte ptr [r15 + 0x5ae]
0038034C  89 45 18                        mov dword ptr [rbp + 0x18], eax
0038034F  45 85 F6                        test r14d, r14d
00380352  74 3A                           je 0x14038038e
00380354  41 8B C6                        mov eax, r14d
00380357  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
0038035B  48 33 CD                        xor rcx, rbp
0038035E  E8 DD C2 32 00                  call 0x1406ac640
00380363  48 8B 5D 70                     mov rbx, qword ptr [rbp + 0x70]
00380367  48 8B 75 78                     mov rsi, qword ptr [rbp + 0x78]
0038036B  48 8B BD 80 00 00 00            mov rdi, qword ptr [rbp + 0x80]
00380372  48 8D 65 40                     lea rsp, [rbp + 0x40]
00380376  41 5F                           pop r15
00380378  41 5E                           pop r14
0038037A  41 5D                           pop r13
0038037C  41 5C                           pop r12
0038037E  5D                              pop rbp
0038037F  C3                              ret
00380380  CC                              int3
00380381  66 41 FF 8F E6 01 00 00         dec word ptr [r15 + 0x1e6]
00380389  E9 E8 FD FF FF                  jmp 0x140380176
0038038E  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00380398  48 85 FF                        test rdi, rdi
0038039B  0F 84 25 04 00 00               je 0x1403807c6
003803A1  45 8B 6C 24 08                  mov r13d, dword ptr [r12 + 8]
003803A6  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
003803AA  41 83 E5 02                     and r13d, 2
003803AE  48 85 C0                        test rax, rax
003803B1  0F 88 4A 01 00 00               js 0x140380501
003803B7  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
003803BB  48 8B C1                        mov rax, rcx
003803BE  48 83 E0 01                     and rax, 1
003803C2  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
003803C6  0F 85 A5 02 00 00               jne 0x140380671
003803CC  48 8B CE                        mov rcx, rsi
003803CF  E8 8C 39 F0 FF                  call 0x140283d60
003803D4  48 89 45 08                     mov qword ptr [rbp + 8], rax
003803D8  48 8B D8                        mov rbx, rax
003803DB  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
003803DF  E8 EC 11 00 00                  call 0x1403815d0
003803E4  85 C0                           test eax, eax
003803E6  0F 85 B8 03 00 00               jne 0x1403807a4
003803EC  4D 85 ED                        test r13, r13
003803EF  0F 85 94 01 00 00               jne 0x140380589
003803F5  4C 39 6D 30                     cmp qword ptr [rbp + 0x30], r13
003803F9  0F 85 A1 02 00 00               jne 0x1403806a0
003803FF  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
00380403  41 B8 01 00 00 00               mov r8d, 1
00380409  41 8B D5                        mov edx, r13d
0038040C  49 8B CD                        mov rcx, r13
0038040F  41 84 C0                        test r8b, al
00380412  0F 85 B0 02 00 00               jne 0x1403806c8
00380418  41 8A 44 24 45                  mov al, byte ptr [r12 + 0x45]
0038041D  41 22 C0                        and al, r8b
00380420  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00380425  49 8B 4C 24 38                  mov rcx, qword ptr [r12 + 0x38]
0038042A  44 8B C2                        mov r8d, edx
0038042D  41 83 C8 10                     or r8d, 0x10
00380431  84 C0                           test al, al
00380433  44 0F 44 C2                     cmove r8d, edx
00380437  45 33 C9                        xor r9d, r9d
0038043A  44 89 44 24 28                  mov dword ptr [rsp + 0x28], r8d
0038043F  48 8B D6                        mov rdx, rsi
00380442  4C 8B C7                        mov r8, rdi
00380445  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0038044A  E8 71 2E FB FF                  call 0x1403332c0
0038044F  85 C0                           test eax, eax
00380451  0F 84 00 04 00 00               je 0x140380857
00380457  49 8B 4C 24 38                  mov rcx, qword ptr [r12 + 0x38]
0038045C  41 8B DE                        mov ebx, r14d
0038045F  E8 3C 11 00 00                  call 0x1403815a0
00380464  4C 8B C0                        mov r8, rax
00380467  44 39 A8 2C 44 00 00            cmp dword ptr [rax + 0x442c], r13d
0038046E  0F 85 73 01 00 00               jne 0x1403805e7
00380474  85 DB                           test ebx, ebx
00380476  B8 14 01 00 00                  mov eax, 0x114
0038047B  44 0F 44 F0                     cmove r14d, eax
0038047F  E9 D0 FE FF FF                  jmp 0x140380354
00380484  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00380488  48 85 C0                        test rax, rax
0038048B  0F 88 8C FE FF FF               js 0x14038031d
00380491  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00380495  48 85 C0                        test rax, rax
00380498  49 0F 45 F9                     cmovne rdi, r9
0038049C  E9 7C FE FF FF                  jmp 0x14038031d
003804A1  4D 89 AE C8 00 00 00            mov qword ptr [r14 + 0xc8], r13
003804A8  8B 5F 38                        mov ebx, dword ptr [rdi + 0x38]
003804AB  C1 EB 05                        shr ebx, 5
003804AE  41 23 DA                        and ebx, r10d
003804B1  E9 8A FC FF FF                  jmp 0x140380140
003804B6  41 8B C0                        mov eax, r8d
003804B9  85 C9                           test ecx, ecx
003804BB  0F 95 C0                        setne al
003804BE  C1 EA 0C                        shr edx, 0xc
003804C1  03 C2                           add eax, edx
003804C3  49 8B 94 C6 38 01 00 00         mov rdx, qword ptr [r14 + rax*8 + 0x138]
003804CB  48 8D 04 52                     lea rax, [rdx + rdx*2]
003804CF  48 03 C0                        add rax, rax
003804D2  48 B9 20 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000020
003804DC  8B 04 C1                        mov eax, dword ptr [rcx + rax*8]
003804DF  45 8B C2                        mov r8d, r10d
003804E2  C1 E8 10                        shr eax, 0x10
003804E5  33 C9                           xor ecx, ecx
003804E7  44 0F B6 C8                     movzx r9d, al
003804EB  41 C1 E9 06                     shr r9d, 6
003804EF  E8 9C 20 FB FF                  call 0x140332590
003804F4  E9 BB FC FF FF                  jmp 0x1403801b4
003804F9  48 8B 3F                        mov rdi, qword ptr [rdi]
003804FC  E9 EA FB FF FF                  jmp 0x1403800eb
00380501  49 8B 34 24                     mov rsi, qword ptr [r12]
00380505  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0038050F  48 C1 EE 09                     shr rsi, 9
00380513  48 23 F0                        and rsi, rax
00380516  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00380520  48 8B C0                        mov rax, rax
00380523  48 8B 55 28                     mov rdx, qword ptr [rbp + 0x28]
00380527  45 33 C9                        xor r9d, r9d
0038052A  48 C1 EA 0C                     shr rdx, 0xc
0038052E  4D 8B C5                        mov r8, r13
00380531  48 23 D1                        and rdx, rcx
00380534  48 03 F0                        add rsi, rax
00380537  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
0038053B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00380540  49 8B CC                        mov rcx, r12
00380543  E8 C8 51 FC FF                  call 0x140345710
00380548  45 33 ED                        xor r13d, r13d
0038054B  44 8B F0                        mov r14d, eax
0038054E  85 C0                           test eax, eax
00380550  0F 89 01 FF FF FF               jns 0x140380457
00380556  E9 F9 FD FF FF                  jmp 0x140380354
0038055B  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0038055F  44 38 01                        cmp byte ptr [rcx], r8b
00380562  0F 85 98 FD FF FF               jne 0x140380300
00380568  83 FB 02                        cmp ebx, 2
0038056B  0F 82 6C 01 00 00               jb 0x1403806dd
00380571  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
00380575  48 83 C1 28                     add rcx, 0x28
00380579  48 39 08                        cmp qword ptr [rax], rcx
0038057C  0F 84 92 01 00 00               je 0x140380714
00380582  B9 03 00 00 00                  mov ecx, 3
00380587  CD 29                           int 0x29
00380589  49 8B 14 24                     mov rdx, qword ptr [r12]
0038058D  48 8B CB                        mov rcx, rbx
00380590  E8 8B 72 0B 00                  call 0x140437820
00380595  48 8B 5D 08                     mov rbx, qword ptr [rbp + 8]
00380599  45 33 ED                        xor r13d, r13d
0038059C  85 C0                           test eax, eax
0038059E  0F 84 51 FE FF FF               je 0x1403803f5
003805A4  48 0F BA E3 0B                  bt rbx, 0xb
003805A9  0F 83 46 FE FF FF               jae 0x1403803f5
003805AF  48 83 CB 42                     or rbx, 0x42
003805B3  48 89 5D 08                     mov qword ptr [rbp + 8], rbx
003805B7  F6 47 22 10                     test byte ptr [rdi + 0x22], 0x10
003805BB  0F 85 34 FE FF FF               jne 0x1403803f5
003805C1  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
003805C5  E8 66 EF FE FF                  call 0x14036f530
003805CA  85 C0                           test eax, eax
003805CC  0F 84 23 FE FF FF               je 0x1403803f5
003805D2  41 8D 55 01                     lea edx, [r13 + 1]
003805D6  48 8B CF                        mov rcx, rdi
003805D9  E8 C2 51 F0 FF                  call 0x1402857a0
003805DE  48 8B 5D 08                     mov rbx, qword ptr [rbp + 8]
003805E2  E9 0E FE FF FF                  jmp 0x1403803f5
003805E7  83 7D 18 02                     cmp dword ptr [rbp + 0x18], 2
003805EB  0F 84 83 FE FF FF               je 0x140380474
003805F1  49 8B CF                        mov rcx, r15
003805F4  E8 E7 20 FE FF                  call 0x1403626e0
003805F9  41 3B 80 30 44 00 00            cmp eax, dword ptr [r8 + 0x4430]
00380600  0F 82 6E FE FF FF               jb 0x140380474
00380606  49 8B 4C 24 38                  mov rcx, qword ptr [r12 + 0x38]
0038060B  BA 01 00 00 00                  mov edx, 1
00380610  48 0B D6                        or rdx, rsi
00380613  E8 58 02 EC FF                  call 0x140240870
00380618  E9 57 FE FF FF                  jmp 0x140380474
0038061D  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00380621  44 38 10                        cmp byte ptr [rax], r10b
00380624  0F 84 2B FB FF FF               je 0x140380155
0038062A  E9 1F FB FF FF                  jmp 0x14038014e
0038062F  49 8B C1                        mov rax, r9
00380632  E9 1C FC FF FF                  jmp 0x140380253
00380637  41 8B 46 60                     mov eax, dword ptr [r14 + 0x60]
0038063B  48 C1 E0 0C                     shl rax, 0xc
0038063F  E9 DE FB FF FF                  jmp 0x140380222
00380644  48 A1 20 03 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000320]
0038064E  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
00380652  E9 41 FC FF FF                  jmp 0x140380298
00380657  8B 05 CF EB B8 00               mov eax, dword ptr [rip + 0xb8ebcf]
0038065D  BA 01 00 00 00                  mov edx, 1
00380662  84 C2                           test dl, al
00380664  0F 85 8E FB FF FF               jne 0x1403801f8
0038066A  8B F2                           mov esi, edx
0038066C  E9 27 FC FF FF                  jmp 0x140380298
00380671  48 8B C1                        mov rax, rcx
00380674  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00380678  80 38 04                        cmp byte ptr [rax], 4
0038067B  0F 85 4B FD FF FF               jne 0x1403803cc
00380681  48 8B CE                        mov rcx, rsi
00380684  E8 17 22 F0 FF                  call 0x1402828a0
00380689  48 25 9F FC FF FF               and rax, 0xfffffffffffffc9f
0038068F  48 0F BA E8 07                  bts rax, 7
00380694  48 89 45 08                     mov qword ptr [rbp + 8], rax
00380698  48 89 06                        mov qword ptr [rsi], rax
0038069B  E9 2C FD FF FF                  jmp 0x1403803cc
003806A0  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
003806A4  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
003806A8  8A 01                           mov al, byte ptr [rcx]
003806AA  3C 04                           cmp al, 4
003806AC  0F 84 DA 00 00 00               je 0x14038078c
003806B2  3C 05                           cmp al, 5
003806B4  0F 85 45 FD FF FF               jne 0x1403803ff
003806BA  41 8B D5                        mov edx, r13d
003806BD  41 B8 01 00 00 00               mov r8d, 1
003806C3  E9 50 FD FF FF                  jmp 0x140380418
003806C8  48 83 E0 FE                     and rax, 0xfffffffffffffffe
003806CC  80 38 03                        cmp byte ptr [rax], 3
003806CF  0F 85 43 FD FF FF               jne 0x140380418
003806D5  41 8B D0                        mov edx, r8d
003806D8  E9 3B FD FF FF                  jmp 0x140380418
003806DD  48 8D 41 38                     lea rax, [rcx + 0x38]
003806E1  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
003806E5  48 39 02                        cmp qword ptr [rdx], rax
003806E8  0F 85 94 FE FF FF               jne 0x140380582
003806EE  49 89 06                        mov qword ptr [r14], rax
003806F1  49 89 56 08                     mov qword ptr [r14 + 8], rdx
003806F5  4C 89 32                        mov qword ptr [rdx], r14
003806F8  4C 89 70 08                     mov qword ptr [rax + 8], r14
003806FC  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
00380703  48 01 41 48                     add qword ptr [rcx + 0x48], rax
00380707  EB 19                           jmp 0x140380722
00380709  0F 57 C0                        xorps xmm0, xmm0
0038070C  0F 11 07                        movups xmmword ptr [rdi], xmm0
0038070F  E9 6C FB FF FF                  jmp 0x140380280
00380714  49 89 0E                        mov qword ptr [r14], rcx
00380717  49 89 46 08                     mov qword ptr [r14 + 8], rax
0038071B  4C 89 30                        mov qword ptr [rax], r14
0038071E  4C 89 71 08                     mov qword ptr [rcx + 8], r14
00380722  44 0F 20 C1                     mov rcx, cr8
00380726  45 0F 22 C0                     mov cr8, r8
0038072A  44 39 0D EF 65 C4 00            cmp dword ptr [rip + 0xc465ef], r9d
00380731  75 2A                           jne 0x14038075d
00380733  49 8B 44 24 38                  mov rax, qword ptr [r12 + 0x38]
00380738  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
0038073E  A8 0F                           test al, 0xf
00380740  75 2B                           jne 0x14038076d
00380742  49 8B CF                        mov rcx, r15
00380745  E8 A6 E8 ED FF                  call 0x14025eff0
0038074A  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
0038074E  49 8B CD                        mov rcx, r13
00380751  E8 DA 9A FE FF                  call 0x14036a230
00380756  33 C0                           xor eax, eax
00380758  E9 FA FB FF FF                  jmp 0x140380357
0038075D  41 8A D0                        mov dl, r8b
00380760  E8 97 4F 17 00                  call 0x1404f56fc
00380765  41 B8 01 00 00 00               mov r8d, 1
0038076B  EB C6                           jmp 0x140380733
0038076D  90                              nop
0038076E  66 45 01 87 E6 01 00 00         add word ptr [r15 + 0x1e6], r8w
00380776  75 D2                           jne 0x14038074a
00380778  49 8D 87 98 00 00 00            lea rax, [r15 + 0x98]
0038077F  90                              nop
00380780  48 39 00                        cmp qword ptr [rax], rax
00380783  74 C5                           je 0x14038074a
00380785  E8 F6 24 F6 FF                  call 0x1402e2c80
0038078A  EB BE                           jmp 0x14038074a
0038078C  48 0F BA 25 F3 62 C4 00 24      bt qword ptr [rip + 0xc462f3], 0x24
00380795  72 54                           jb 0x1403807eb
00380797  48 89 1E                        mov qword ptr [rsi], rbx
0038079A  B8 14 01 00 00                  mov eax, 0x114
0038079F  E9 B3 FB FF FF                  jmp 0x140380357
003807A4  48 8D 4D 08                     lea rcx, [rbp + 8]
003807A8  E8 F3 20 F0 FF                  call 0x1402828a0
003807AD  48 83 C8 40                     or rax, 0x40
003807B1  48 8D 4D 08                     lea rcx, [rbp + 8]
003807B5  48 8B D0                        mov rdx, rax
003807B8  E8 53 10 F0 FF                  call 0x140281810
003807BD  48 8B 5D 08                     mov rbx, qword ptr [rbp + 8]
003807C1  E9 26 FC FF FF                  jmp 0x1403803ec
003807C6  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
003807CA  48 C1 E8 0C                     shr rax, 0xc
003807CE  48 23 C1                        and rax, rcx
003807D1  48 8D 3C 40                     lea rdi, [rax + rax*2]
003807D5  48 C1 E7 04                     shl rdi, 4
003807D9  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003807E3  48 03 F8                        add rdi, rax
003807E6  E9 B6 FB FF FF                  jmp 0x1403803a1
003807EB  F6 C3 20                        test bl, 0x20
003807EE  75 A7                           jne 0x140380797
003807F0  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003807FA  48 8B C0                        mov rax, rax
003807FD  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00380807  48 03 C1                        add rax, rcx
0038080A  48 3B F0                        cmp rsi, rax
0038080D  72 88                           jb 0x140380797
0038080F  41 B8 80 00 00 00               mov r8d, 0x80
00380815  48 8B D3                        mov rdx, rbx
00380818  48 8B CE                        mov rcx, rsi
0038081B  E8 60 25 F1 FF                  call 0x140292d80
00380820  E9 72 FF FF FF                  jmp 0x140380797
00380825  BE 01 00 00 00                  mov esi, 1
0038082A  E9 69 FA FF FF                  jmp 0x140380298
0038082F  49 8B 4D 00                     mov rcx, qword ptr [r13]
00380833  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
00380839  24 0F                           and al, 0xf
0038083B  40 3A C6                        cmp al, sil
0038083E  48 8D 05 1B 80 AB 00            lea rax, [rip + 0xab801b]
00380845  0F 84 15 3D 36 00               je 0x1406e4560
0038084B  48 8D 81 E0 00 00 00            lea rax, [rcx + 0xe0]
00380852  E9 09 3D 36 00                  jmp 0x1406e4560
00380857  BA 02 00 00 00                  mov edx, 2
0038085C  48 8B CF                        mov rcx, rdi
0038085F  E8 F0 1F F2 FF                  call 0x1402a2854
00380864  41 BE 17 00 00 C0               mov r14d, 0xc0000017
0038086A  E9 E5 FA FF FF                  jmp 0x140380354
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiIssueHardFault(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (128);
    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    result = (*(unsigned __int64 *)(v_rip + 11052704)) ^ (v_stack_m68);
    v_stack_m30 = result;
    a2 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    *(unsigned __int64 *)(a2 + 224) = *(unsigned __int64 *)(a1);
    v_stack_m40 = 0;
    result = MiGetSessionIdForVa(*(unsigned __int64 *)(a1), a2, a3, a4);
    if (*(unsigned __int64 *)(a2 + 208) != 0) goto loc_003804F9;
loc_003800EB:
    result = MiReferenceInPageFile(0, (unsigned int)((unsigned int)(result)), 1, a4);
    result = MiReleaseFaultState(a1 + 56, 1, v_stack_m68, a4);
    a3 = 0;
    v_stack_m50 = result;
    v_stack_m58 = *(unsigned __int64 *)(a1 + 16);
    if (result != 0) goto loc_003804A1;
    *(unsigned __int64 *)(a2 + 200) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 200) + 24);
loc_00380140:
    if ((((unsigned __int8)(a3 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(a1 + 16)))) != 0) goto loc_0038061D;
loc_0038014E:
loc_00380155:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 184)))) & (15)) != 0) goto loc_00380381;
loc_00380176:
    result = *(unsigned __int64 *)(a1 + 16);
    v_r10 = a3 + 1;
    if ((*(unsigned int *)(v_rip + 12872610)) != 0) {
        a1 = v_cr8;
        a2 = v_stack_m68;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
        a3 = 0;
        v_r10 = a3 + 1;
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 312))))) & (0xFFFULL));
    if (condition_is_below) goto loc_003804B6;
loc_003801B4:
    a4 = 0;
    *(unsigned int *)(a2 + 184) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 312)));
    v_stack_m48 = 0;
    if ((*(unsigned int *)(a2 + 36)) != 0) goto loc_003802CA;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 192))))) & (0x400420ULL));
    if (((unsigned int)(result)) == 0x400020ULL) goto loc_003802CF;
    if (((*(unsigned int *)(v_rip + 12871950)) & ((unsigned int)((unsigned int)(0x2000ULL)))) == 0) goto loc_00380657;
loc_003801F8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 192)))) & (32)) != 0) goto loc_00380825;
    v_rsp = (v_rsp) - (80);
    v_stack_m48 = v_stack_mB8;
    if (condition_is_below) goto loc_00380637;
loc_00380222:
    *(unsigned __int64 *)(v_stack_mB8 + 40) = *(unsigned __int64 *)(a2 + 224);
    *(unsigned __int64 *)(v_stack_mB8 + 32) = *(unsigned __int64 *)(a2 + 96);
    *(unsigned int *)(v_stack_mB8 + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 152) + 1296)));
    *(unsigned int *)(v_stack_mB8 + 60) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 312)));
    if (*(unsigned __int64 *)(a2 + 200) == 0) goto loc_0038062F;
loc_00380253:
    *(unsigned __int64 *)(v_stack_mB8 + 48) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 200) + 24);
    if (((*(unsigned int *)(v_rip + 12871842)) & ((unsigned int)((unsigned int)(0x2000ULL)))) == 0) goto loc_00380709;
    result = EtwGetKernelTraceTimestampSilo(v_stack_mB8, (unsigned int)((unsigned int)((unsigned int)(0x2000ULL))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 152) + 544) + 1520), a4);
    a4 = 0;
loc_00380280:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12119974))))) != 0) goto loc_00380644;
    *(unsigned __int64 *)(v_stack_mB8 + 64) = 0;
loc_00380298:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 184))))) >> (24));
    result = (unsigned __int8)((result) & (48));
    if (((unsigned __int8)(result)) == 48) goto loc_0038082F;
    v_rbx = (unsigned int)((0) | (2));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (1));
    result = MiIssueHardFaultIo(a2, a2, *(unsigned __int64 *)(a1 + 16), a4);
    a4 = 0;
    goto loc_003802CF;
loc_003802CA:
loc_003802CF:
    a1 = (unsigned int)(((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 184)))) + ((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 184))))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 192)))));
    a2 = (unsigned int)((a2) & (0xFFFFFFE1ULL));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a1)));
    *(unsigned int *)(a2 + 192) = (unsigned int)(a2);
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(a1 + 16)))) != 0) goto loc_0038055B;
loc_00380300:
    if (condition_is_above_or_equal) goto loc_00380484;
loc_0038031D:
    result = MiWaitForInPageComplete(a1, a2, v_stack_m48, a4);
    result = MiFinishHardFault(a1, v_stack_m50, a2, v_stack_m40);
    v_stack_m50 = (unsigned int)((unsigned int)(v_stack_m48));
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_0038038E;
loc_00380354:
loc_00380357:
    a1 = (v_stack_m30) ^ (v_stack_m68);
    result = _security_check_cookie(a1, v_stack_m50, a2, v_stack_m40);
    return result;
loc_00380381:
    goto loc_00380176;
loc_0038038E:
    if (v_stack_p18 == 0) goto loc_003807C6;
loc_003803A1:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) & (2));
    if (sign_flag) goto loc_00380501;
    result = (v_stack_m58) & (1);
    v_stack_m38 = result;
    if (condition_is_not_equal) goto loc_00380671;
loc_003803CC:
    result = MiMakeTransitionPteValid(v_stack_p10, v_stack_m50, a2, v_stack_m40);
    v_stack_m60 = result;
    result = MI_IS_SOFTWARE_PTE_SHADOW_STACK(*(unsigned __int64 *)(v_stack_p18 + 16), v_stack_m50, a2, v_stack_m40);
    if ((unsigned int)(result) != 0) goto loc_003807A4;
loc_003803EC:
    if (v_r13 != 0) goto loc_00380589;
loc_003803F5:
    if (v_stack_m38 != v_r13) goto loc_003806A0;
loc_003803FF:
    if (((1) & ((unsigned __int8)(v_stack_m58))) != 0) goto loc_003806C8;
loc_00380418:
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 69)) & (1));
    v_stack_p30 = v_r13;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13))))) | (16));
    if ((unsigned __int8)(result) == 0) { a3 = (unsigned int)((unsigned int)((unsigned int)(v_r13))); }
    a4 = 0;
    v_stack_p28 = (unsigned int)(a3);
    v_stack_p20 = result;
    result = MiAllocateWsle(*(unsigned __int64 *)(a1 + 56), v_stack_p10, v_stack_p18, a4);
    if ((unsigned int)(result) == 0) goto loc_00380857;
loc_00380457:
    result = MiGetVmAccessLoggingPartition(*(unsigned __int64 *)(a1 + 56), v_stack_p10, v_stack_p18, a4);
    if ((*(unsigned int *)(result + 17452)) != ((unsigned int)(v_r13))) goto loc_003805E7;
loc_00380474:
    v_r14 = (unsigned int)((unsigned int)(result));
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) == 0) { v_r14 = 276; }
    goto loc_00380354;
loc_00380484:
    if (sign_flag) goto loc_0038031D;
    v_rdi = v_stack_p18;
    if (*(unsigned __int64 *)(v_stack_p18 + 8) != 0) { v_rdi = 0; }
    goto loc_0038031D;
loc_003804A1:
    *(unsigned __int64 *)(v_r14 + 200) = v_r13;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 56))) >> (5));
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)((unsigned int)(0x2000ULL))));
    goto loc_00380140;
loc_003804B6:
    result = ((unsigned int)(*(unsigned __int64 *)(a1 + 56)) != 0) ? 1 : 0;
    a2 = (unsigned int)((v_stack_p10) >> (12));
    result = (unsigned int)((result) + ((unsigned int)(a2)));
    result = (*(unsigned __int64 *)(v_r14 + result * 8 + 312) + *(unsigned __int64 *)(v_r14 + result * 8 + 312) * 2) + (*(unsigned __int64 *)(v_r14 + result * 8 + 312) + *(unsigned __int64 *)(v_r14 + result * 8 + 312) * 2);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + result * 8))) >> (16));
    a1 = 0;
    a4 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    result = MiZeroPhysicalPage(a1, *(unsigned __int64 *)(v_r14 + result * 8 + 312), (unsigned int)((unsigned int)((unsigned int)(0x2000ULL))), a4);
    goto loc_003801B4;
loc_003804F9:
    goto loc_003800EB;
loc_00380501:
    v_rsi = (*(unsigned __int64 *)(a1)) >> (9);
    v_rsi = (v_rsi) & (result);
    a4 = 0;
    a2 = (v_stack_m40) >> (12);
    a2 = (a2) & (0);
    v_rsi = (v_rsi) + (result);
    v_stack_p20 = v_stack_m58;
    result = MiCompleteProtoPteFault(0, a2, v_r13, a4);
    v_r13 = 0;
    if (!sign_flag) goto loc_00380457;
    goto loc_00380354;
loc_0038055B:
    a1 = (0) & (-2);
    if ((*(unsigned __int8 *)(a1)) != 0) goto loc_00380300;
    if (((unsigned int)(v_rbx)) < 2) goto loc_003806DD;
    a1 = (a1) + (40);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48))) == a1) goto loc_00380714;
loc_00380582:
loc_00380589:
    result = MiOkToSetPteDirtyForNotValidFault(v_rbx, *(unsigned __int64 *)(a1), v_r13, a4);
    v_r13 = 0;
    if ((unsigned int)(result) == 0) goto loc_003803F5;
    if (condition_is_above_or_equal) goto loc_003803F5;
    v_rbx = (v_stack_m60) | (66);
    v_stack_m60 = v_rbx;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi) + 34)) & (16)) != 0) goto loc_003803F5;
    result = MiGetPagingFileOffset(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 16), *(unsigned __int64 *)(a1), v_r13, a4);
    if ((unsigned int)(result) == 0) goto loc_003803F5;
    result = MiLockPageAndSetDirty(*(unsigned __int64 *)(v_rdi), v_r13 + 1, v_r13, a4);
    goto loc_003803F5;
loc_003805E7:
    if (v_stack_m50 == 2) goto loc_00380474;
    result = MiGetEffectivePagePriorityThread(*(unsigned __int64 *)(a2 + 152), v_r13 + 1, v_r13, a4);
    if (((unsigned int)(result)) < (*(unsigned int *)(v_r13 + 17456))) goto loc_00380474;
    a2 = (1) | (v_rsi);
    result = MiLogPageAccess(*(unsigned __int64 *)(a1 + 56), a2, v_r13, a4);
    goto loc_00380474;
loc_0038061D:
    result = (result) & (-2);
    if ((*(unsigned __int8 *)(result)) == ((unsigned __int8)((unsigned int)(0x2000ULL)))) goto loc_00380155;
    goto loc_0038014E;
loc_0038062F:
    goto loc_00380253;
loc_00380637:
    result = ((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 96))) << (12);
    goto loc_00380222;
loc_00380644:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 64) = result;
    goto loc_00380298;
loc_00380657:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12118991))))) != 0) goto loc_003801F8;
    goto loc_00380298;
loc_00380671:
    result = (*(unsigned __int64 *)(a1 + 56)) & (-2);
    if ((*(unsigned __int8 *)(result)) != 4) goto loc_003803CC;
    result = MI_READ_PTE_LOCK_FREE(1, 1, v_r13, a4);
    result = (result) & (-865);
    v_stack_m60 = result;
    *(unsigned __int64 *)(1) = result;
    goto loc_003803CC;
loc_003806A0:
    a1 = (v_stack_m58) & (-2);
    if (((unsigned __int8)(*(unsigned __int8 *)(a1))) == 4) goto loc_0038078C;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1))) != 5) goto loc_003803FF;
    goto loc_00380418;
loc_003806C8:
    result = (*(unsigned __int8 *)(a1)) & (-2);
    if ((*(unsigned __int8 *)(result)) != 3) goto loc_00380418;
    goto loc_00380418;
loc_003806DD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56 + 8))) != (a1 + 56)) goto loc_00380582;
    *(unsigned __int64 *)((unsigned int)((unsigned int)(result))) = a1 + 56;
    *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8) = *(unsigned __int64 *)(a1 + 56 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56 + 8)) = (unsigned int)((unsigned int)(result));
    *(unsigned __int64 *)(a1 + 56 + 8) = (unsigned int)((unsigned int)(result));
    goto loc_00380722;
loc_00380709:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi)) = v_xmm0;
    goto loc_00380280;
loc_00380714:
    *(unsigned __int64 *)((unsigned int)((unsigned int)(result))) = a1;
    *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8) = (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 184));
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 184))) = (unsigned int)((unsigned int)(result));
    *(unsigned __int64 *)(a1 + 8) = (unsigned int)((unsigned int)(result));
loc_00380722:
    if ((*(unsigned int *)(v_rip + 12871151)) != 0) goto loc_0038075D;
loc_00380733:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 184)))) & (15)) != 0) goto loc_0038076D;
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(a2 + 152), *(unsigned __int64 *)(a1 + 56 + 8), 1, a4);
loc_0038074A:
    result = MiRelockFaultState(0, v_stack_m50, 1, a4);
    result = 0;
    goto loc_00380357;
loc_0038075D:
    result = KiRaiseIrqlProcessIrqlFlags(0, 1, 1, a4);
    goto loc_00380733;
loc_0038076D:
    if (condition_is_not_equal) goto loc_0038074A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 152) + 152)) == (*(unsigned __int64 *)(a2 + 152) + 152)) goto loc_0038074A;
    result = KiCheckForKernelApcDelivery(0, 1, 1, a4);
    goto loc_0038074A;
loc_0038078C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 152) + 152)) < (*(unsigned __int64 *)(a2 + 152) + 152)) goto loc_003807EB;
loc_00380797:
    *(unsigned __int64 *)(1) = v_stack_m60;
    goto loc_00380357;
loc_003807A4:
    result = MI_READ_PTE_LOCK_FREE(v_stack_m60, 1, 1, a4);
    result = (result) | (64);
    result = MiWriteValidPteNewProtection(v_stack_m60, result, 1, a4);
    goto loc_003803EC;
loc_003807C6:
    result = (v_stack_m40) >> (12);
    result = (result) & (v_stack_m60);
    v_rdi = (result + result * 2) << (4);
    v_rdi = (v_rdi) + (result);
    goto loc_003803A1;
loc_003807EB:
    if ((((unsigned __int8)(v_stack_m60)) & (32)) != 0) goto loc_00380797;
    result = (result) + (v_stack_m60);
    if (1 < result) goto loc_00380797;
    result = MiCheckLinearProtectedPteAccessedBit(1, v_stack_m60, 128, a4);
    goto loc_00380797;
loc_00380825:
    goto loc_00380298;
loc_0038082F:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r13) + 184))) & (15));
loc_00380857:
    result = MiLockAndDecrementShareCount(v_rdi, 2, 128, a4);
    goto loc_00380354;
}
```

## 5. (Beta) C Style

```c
int64_t MiIssueHardFault(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (128);
    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    result = (*(uint64_t *)(v_rip + 0xA8A6A0)) ^ (v_stack_m68);
    v_stack_m30 = result;
    Arg2 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    *(uint64_t *)(arg2 + 0xE0) = *(uint64_t *)(arg1);
    v_stack_m40 = 0;
    result = MiGetSessionIdForVa(*(uint64_t *)(arg1), Arg2, Arg3, Arg4);
    if (*(uint64_t *)(arg2 + 0xD0) != 0) goto loc_003804F9;
loc_003800EB:
    result = MiReferenceInPageFile(0, (uint32_t)((uint32_t)(result)), 1, Arg4);
    result = MiReleaseFaultState(Arg1 + 56, 1, v_stack_m68, Arg4);
    Arg3 = 0;
    v_stack_m50 = result;
    v_stack_m58 = *(uint64_t *)(arg1 + 0x10);
    if (result != 0) goto loc_003804A1;
    *(uint64_t *)(arg2 + 0xC8) = *(uint64_t *)(*(uint64_t *)(arg2 + 0xC8) + 0x18);
loc_00380140:
    if ((((uint8_t)(Arg3 + 1)) & ((uint8_t)(*(uint64_t *)(arg1 + 0x10)))) != 0) goto loc_0038061D;
loc_0038014E:
loc_00380155:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8)))) & (15)) != 0) goto loc_00380381;
loc_00380176:
    result = *(uint64_t *)(arg1 + 0x10);
    local_r10 = Arg3 + 1;
    if ((*(uint32_t *)(v_rip + 0xC46BA2)) != 0) {
        Arg1 = v_cr8;
        Arg2 = v_stack_m68;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
        Arg3 = 0;
        local_r10 = Arg3 + 1;
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x138))))) & (0xFFFULL));
    if (condition_is_below) goto loc_003804B6;
loc_003801B4:
    Arg4 = 0;
    *(uint32_t *)(arg2 + 0xB8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x138)));
    v_stack_m48 = 0;
    if ((*(uint32_t *)(arg2 + 0x24)) != 0) goto loc_003802CA;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC0))))) & (0x400420ULL));
    if (((uint32_t)(result)) == 0x400020ULL) goto loc_003802CF;
    if (((*(uint32_t *)(v_rip + 0xC4690E)) & ((uint32_t)((uint32_t)(0x2000ULL)))) == 0) goto loc_00380657;
loc_003801F8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC0)))) & (32)) != 0) goto loc_00380825;
    local_rsp = (local_rsp) - (80);
    v_stack_m48 = v_stack_mB8;
    if (condition_is_below) goto loc_00380637;
loc_00380222:
    *(uint64_t *)(v_stack_mB8 + 0x28) = *(uint64_t *)(arg2 + 0xE0);
    *(uint64_t *)(v_stack_mB8 + 0x20) = *(uint64_t *)(arg2 + 0x60);
    *(uint32_t *)(v_stack_mB8 + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x98) + 0x510)));
    *(uint32_t *)(v_stack_mB8 + 0x3C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x138)));
    if (*(uint64_t *)(arg2 + 0xC8) == 0) goto loc_0038062F;
loc_00380253:
    *(uint64_t *)(v_stack_mB8 + 0x30) = *(uint64_t *)(*(uint64_t *)(arg2 + 0xC8) + 0x18);
    if (((*(uint32_t *)(v_rip + 0xC468A2)) & ((uint32_t)((uint32_t)(0x2000ULL)))) == 0) goto loc_00380709;
    result = EtwGetKernelTraceTimestampSilo(v_stack_mB8, (uint32_t)((uint32_t)((uint32_t)(0x2000ULL))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x98) + 0x220) + 0x5F0), Arg4);
    Arg4 = 0;
loc_00380280:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB8EFA6))))) != 0) goto loc_00380644;
    *(uint64_t *)(v_stack_mB8 + 0x40) = 0;
loc_00380298:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8))))) >> (24));
    result = (uint8_t)((result) & (48));
    if (((uint8_t)(result)) == 48) goto loc_0038082F;
    local_rbx = (uint32_t)((0) | (2));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (1));
    result = MiIssueHardFaultIo(Arg2, Arg2, *(uint64_t *)(arg1 + 0x10), Arg4);
    Arg4 = 0;
    goto loc_003802CF;
loc_003802CA:
loc_003802CF:
    Arg1 = (uint32_t)(((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8)))) + ((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8))))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC0)))));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFE1ULL));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(Arg1)));
    *(uint32_t *)(arg2 + 0xC0) = (uint32_t)(Arg2);
    if (((1) & ((uint8_t)(*(uint64_t *)(arg1 + 0x10)))) != 0) goto loc_0038055B;
loc_00380300:
    if (condition_is_above_or_equal) goto loc_00380484;
loc_0038031D:
    result = MiWaitForInPageComplete(Arg1, Arg2, v_stack_m48, Arg4);
    result = MiFinishHardFault(Arg1, v_stack_m50, Arg2, v_stack_m40);
    v_stack_m50 = (uint32_t)((uint32_t)(v_stack_m48));
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_0038038E;
loc_00380354:
loc_00380357:
    Arg1 = (v_stack_m30) ^ (v_stack_m68);
    result = _security_check_cookie(Arg1, v_stack_m50, Arg2, v_stack_m40);
    return result;
loc_00380381:
    goto loc_00380176;
loc_0038038E:
    if (v_stack_p18 == 0) goto loc_003807C6;
loc_003803A1:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) & (2));
    if (sign_flag) goto loc_00380501;
    result = (v_stack_m58) & (1);
    v_stack_m38 = result;
    if (condition_is_not_equal) goto loc_00380671;
loc_003803CC:
    result = MiMakeTransitionPteValid(v_stack_p10, v_stack_m50, Arg2, v_stack_m40);
    v_stack_m60 = result;
    result = MI_IS_SOFTWARE_PTE_SHADOW_STACK(*(uint64_t *)(v_stack_p18 + 0x10), v_stack_m50, Arg2, v_stack_m40);
    if ((uint32_t)(result) != 0) goto loc_003807A4;
loc_003803EC:
    if (local_r13 != 0) goto loc_00380589;
loc_003803F5:
    if (v_stack_m38 != local_r13) goto loc_003806A0;
loc_003803FF:
    if (((1) & ((uint8_t)(v_stack_m58))) != 0) goto loc_003806C8;
loc_00380418:
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x45)) & (1));
    v_stack_p30 = local_r13;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13))))) | (16));
    if ((uint8_t)(result) == 0) { Arg3 = (uint32_t)((uint32_t)((uint32_t)(local_r13))); }
    Arg4 = 0;
    v_stack_p28 = (uint32_t)(Arg3);
    v_stack_p20 = result;
    result = MiAllocateWsle(*(uint64_t *)(arg1 + 0x38), v_stack_p10, v_stack_p18, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00380857;
loc_00380457:
    result = MiGetVmAccessLoggingPartition(*(uint64_t *)(arg1 + 0x38), v_stack_p10, v_stack_p18, Arg4);
    if ((*(uint32_t *)(result + 0x442C)) != ((uint32_t)(local_r13))) goto loc_003805E7;
loc_00380474:
    local_r14 = (uint32_t)((uint32_t)(result));
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) == 0) { local_r14 = 276; }
    goto loc_00380354;
loc_00380484:
    if (sign_flag) goto loc_0038031D;
    local_rdi = v_stack_p18;
    if (*(uint64_t *)(v_stack_p18 + 0x8) != 0) { local_rdi = 0; }
    goto loc_0038031D;
loc_003804A1:
    *(uint64_t *)(local_r14 + 0xC8) = local_r13;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x38))) >> (5));
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)((uint32_t)(0x2000ULL))));
    goto loc_00380140;
loc_003804B6:
    result = ((uint32_t)(*(uint64_t *)(arg1 + 0x38)) != 0) ? 1 : 0;
    Arg2 = (uint32_t)((v_stack_p10) >> (12));
    result = (uint32_t)((result) + ((uint32_t)(Arg2)));
    result = (*(uint64_t *)(local_r14 + result * 8 + 0x138) + *(uint64_t *)(local_r14 + result * 8 + 0x138) * 2) + (*(uint64_t *)(local_r14 + result * 8 + 0x138) + *(uint64_t *)(local_r14 + result * 8 + 0x138) * 2);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + result * 8))) >> (16));
    Arg1 = 0;
    Arg4 = (uint32_t)(((uint8_t)(result)) >> (6));
    result = MiZeroPhysicalPage(Arg1, *(uint64_t *)(local_r14 + result * 8 + 0x138), (uint32_t)((uint32_t)((uint32_t)(0x2000ULL))), Arg4);
    goto loc_003801B4;
loc_003804F9:
    goto loc_003800EB;
loc_00380501:
    local_rsi = (*(uint64_t *)(arg1)) >> (9);
    local_rsi = (local_rsi) & (result);
    Arg4 = 0;
    Arg2 = (v_stack_m40) >> (12);
    Arg2 = (Arg2) & (0);
    local_rsi = (local_rsi) + (result);
    v_stack_p20 = v_stack_m58;
    result = MiCompleteProtoPteFault(0, Arg2, local_r13, Arg4);
    local_r13 = 0;
    if (!sign_flag) goto loc_00380457;
    goto loc_00380354;
loc_0038055B:
    Arg1 = (0) & (-2);
    if ((*(uint8_t *)(arg1)) != 0) goto loc_00380300;
    if (((uint32_t)(local_rbx)) < 2) goto loc_003806DD;
    Arg1 = (Arg1) + (40);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x30))) == Arg1) goto loc_00380714;
loc_00380582:
loc_00380589:
    result = MiOkToSetPteDirtyForNotValidFault(local_rbx, *(uint64_t *)(arg1), local_r13, Arg4);
    local_r13 = 0;
    if ((uint32_t)(result) == 0) goto loc_003803F5;
    if (condition_is_above_or_equal) goto loc_003803F5;
    local_rbx = (v_stack_m60) | (66);
    v_stack_m60 = local_rbx;
    if (((*(uint8_t *)(*(uint64_t *)(local_rdi) + 0x22)) & (16)) != 0) goto loc_003803F5;
    result = MiGetPagingFileOffset(*(uint64_t *)(*(uint64_t *)(local_rdi) + 0x10), *(uint64_t *)(arg1), local_r13, Arg4);
    if ((uint32_t)(result) == 0) goto loc_003803F5;
    result = MiLockPageAndSetDirty(*(uint64_t *)(local_rdi), local_r13 + 1, local_r13, Arg4);
    goto loc_003803F5;
loc_003805E7:
    if (v_stack_m50 == 2) goto loc_00380474;
    result = MiGetEffectivePagePriorityThread(*(uint64_t *)(arg2 + 0x98), local_r13 + 1, local_r13, Arg4);
    if (((uint32_t)(result)) < (*(uint32_t *)(local_r13 + 0x4430))) goto loc_00380474;
    Arg2 = (1) | (local_rsi);
    result = MiLogPageAccess(*(uint64_t *)(arg1 + 0x38), Arg2, local_r13, Arg4);
    goto loc_00380474;
loc_0038061D:
    result = (result) & (-2);
    if ((*(uint8_t *)(result)) == ((uint8_t)((uint32_t)(0x2000ULL)))) goto loc_00380155;
    goto loc_0038014E;
loc_0038062F:
    goto loc_00380253;
loc_00380637:
    result = ((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x60))) << (12);
    goto loc_00380222;
loc_00380644:
    *(uint64_t *)(*(uint64_t *)(local_rdi) + 0x40) = result;
    goto loc_00380298;
loc_00380657:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB8EBCF))))) != 0) goto loc_003801F8;
    goto loc_00380298;
loc_00380671:
    result = (*(uint64_t *)(arg1 + 0x38)) & (-2);
    if ((*(uint8_t *)(result)) != 4) goto loc_003803CC;
    result = MI_READ_PTE_LOCK_FREE(1, 1, local_r13, Arg4);
    result = (result) & (-865);
    v_stack_m60 = result;
    *(uint64_t *)(1) = result;
    goto loc_003803CC;
loc_003806A0:
    Arg1 = (v_stack_m58) & (-2);
    if (((uint8_t)(*(uint8_t *)(arg1))) == 4) goto loc_0038078C;
    if (((uint8_t)(*(uint8_t *)(arg1))) != 5) goto loc_003803FF;
    goto loc_00380418;
loc_003806C8:
    result = (*(uint8_t *)(arg1)) & (-2);
    if ((*(uint8_t *)(result)) != 3) goto loc_00380418;
    goto loc_00380418;
loc_003806DD:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x38 + 0x8))) != (Arg1 + 56)) goto loc_00380582;
    *(void **)((uint32_t)((uint32_t)(result))) = Arg1 + 56;
    *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8) = *(uint64_t *)(arg1 + 0x38 + 0x8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x38 + 0x8)) = (uint32_t)((uint32_t)(result));
    *(uint64_t *)(arg1 + 0x38 + 0x8) = (uint32_t)((uint32_t)(result));
    goto loc_00380722;
loc_00380709:
    *(uint64_t *)(*(uint64_t *)(local_rdi)) = v_xmm0;
    goto loc_00380280;
loc_00380714:
    *(void **)((uint32_t)((uint32_t)(result))) = Arg1;
    *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8) = (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0xB8));
    *(uint64_t *)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0xB8))) = (uint32_t)((uint32_t)(result));
    *(uint64_t *)(arg1 + 0x8) = (uint32_t)((uint32_t)(result));
loc_00380722:
    if ((*(uint32_t *)(v_rip + 0xC465EF)) != 0) goto loc_0038075D;
loc_00380733:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0xB8)))) & (15)) != 0) goto loc_0038076D;
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(arg2 + 0x98), *(uint64_t *)(arg1 + 0x38 + 0x8), 1, Arg4);
loc_0038074A:
    result = MiRelockFaultState(0, v_stack_m50, 1, Arg4);
    result = 0;
    goto loc_00380357;
loc_0038075D:
    result = KiRaiseIrqlProcessIrqlFlags(0, 1, 1, Arg4);
    goto loc_00380733;
loc_0038076D:
    if (condition_is_not_equal) goto loc_0038074A;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x98) + 0x98)) == (*(uint64_t *)(arg2 + 0x98) + 152)) goto loc_0038074A;
    result = KiCheckForKernelApcDelivery(0, 1, 1, Arg4);
    goto loc_0038074A;
loc_0038078C:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x98) + 0x98)) < (*(uint64_t *)(arg2 + 0x98) + 152)) goto loc_003807EB;
loc_00380797:
    *(uint64_t *)(1) = v_stack_m60;
    goto loc_00380357;
loc_003807A4:
    result = MI_READ_PTE_LOCK_FREE(v_stack_m60, 1, 1, Arg4);
    result = (result) | (64);
    result = MiWriteValidPteNewProtection(v_stack_m60, result, 1, Arg4);
    goto loc_003803EC;
loc_003807C6:
    result = (v_stack_m40) >> (12);
    result = (result) & (v_stack_m60);
    local_rdi = (result + result * 2) << (4);
    local_rdi = (local_rdi) + (result);
    goto loc_003803A1;
loc_003807EB:
    if ((((uint8_t)(v_stack_m60)) & (32)) != 0) goto loc_00380797;
    result = (result) + (v_stack_m60);
    if (1 < result) goto loc_00380797;
    result = MiCheckLinearProtectedPteAccessedBit(1, v_stack_m60, 128, Arg4);
    goto loc_00380797;
loc_00380825:
    goto loc_00380298;
loc_0038082F:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r13) + 0xB8))) & (15));
loc_00380857:
    result = MiLockAndDecrementShareCount(local_rdi, 2, 128, Arg4);
    goto loc_00380354;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x45` | `8` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x24` | `32` | `R` |
| `Arg2` | `+ 0x60` | `32` | `R` |
| `Arg2` | `+ 0x60` | `64` | `R` |
| `Arg2` | `+ 0x98` | `64` | `R` |
| `Arg2` | `+ 0xB8` | `32` | `R` |
| `Arg2` | `+ 0xB8` | `32` | `W` |
| `Arg2` | `+ 0xC0` | `32` | `R` |
| `Arg2` | `+ 0xC0` | `32` | `W` |
| `Arg2` | `+ 0xC8` | `64` | `R` |
| `Arg2` | `+ 0xC8` | `64` | `W` |
| `Arg2` | `+ 0xD0` | `64` | `R` |
| `Arg2` | `+ 0xE0` | `64` | `R` |
| `Arg2` | `+ 0xE0` | `64` | `W` |
| `Arg2` | `+ 0xE8` | `64` | `R` |
| `Arg2` | `+ 0xF8` | `64` | `R` |
| `Arg2` | `+ 0x138` | `32` | `R` |
| `Arg2` | `+ 0x138 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00380074&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
