# MiCommitExistingVad

- RVA: `0x0032A860`–`0x0032B685` (길이 `3,621` bytes)
- VA: `0x000000014032A860`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000760A8`
- 디코드: `835`개 명령, `3,621/3,621` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **56**; 고유 호출 대상: **36**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0032A8EF` → [MiMakeProtectionMask](MiMakeProtectionMask_function_00329480.md) (function, `0x00329480`)
- `0x0032AADB` → [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) (function, `0x00887630`)
- `0x0032AB15` → [MiVadPureReserve](../2C/MiVadPureReserve_function_002C34C0.md) (function, `0x002C34C0`)
- `0x0032AB40` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0032AB59` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0032AB72` → [MiCommitPageTablesForVad](../../page/88/MiCommitPageTablesForVad_function_00886D50.md) (function, `0x00886D50`)
- `0x0032ABC0` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0032ACA8` → [MiPteHasShadow](MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x0032AD56` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x0032ADD0` → [MiIncreaseUsedPtes](../24/MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x0032AE02` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0032AE13` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x0032AE25` → [UNLOCK_PAGE_TABLE_COMMITMENT](../2E/UNLOCK_PAGE_TABLE_COMMITMENT_function_002E27D0.md) (function, `0x002E27D0`)
- `0x0032AE71` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0032AEA0` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (function, `0x009E5D58`)
- `0x0032AEC5` → [MiIsPteDecommittedPage](../2C/MiIsPteDecommittedPage_function_002C5F90.md) (function, `0x002C5F90`)
- `0x0032AF06` → [MiGetPageProtection](MiGetPageProtection_function_0032BA10.md) (function, `0x0032BA10`)
- `0x0032AF2E` → [MiIncreaseUsedPtes](../24/MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x0032AF60` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x0032AFAB` → [MiIncreaseUsedPtes](../24/MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x0032AFC6` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x0032AFDC` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0032B02B` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0032B03D` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x0032B053` → [UNLOCK_PAGE_TABLE_COMMITMENT](../2E/UNLOCK_PAGE_TABLE_COMMITMENT_function_002E27D0.md) (function, `0x002E27D0`)
- `0x0032B083` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x0032B0BF` → [MiComputePageCommitment](../2C/MiComputePageCommitment_function_002C5C34.md) (function, `0x002C5C34`)
- `0x0032B0D7` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x0032B1B2` → [MiComputePreferredNode](../3D/MiComputePreferredNode_function_003D3438.md) (function, `0x003D3438`)
- `0x0032B1C9` → [MiLockWorkingSetForLargeMapping](../4E/MiLockWorkingSetForLargeMapping_function_004E3110.md) (function, `0x004E3110`)
- `0x0032B1E6` → [MiPopLargePfnList](../49/MiPopLargePfnList_function_0049C460.md) (function, `0x0049C460`)
- `0x0032B233` → [MiInsertLargeUserMapping](../3D/MiInsertLargeUserMapping_function_003D3154.md) (function, `0x003D3154`)
- `0x0032B24B` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0032B31C` → [MiChargeProcessPhysicalPages](../../page/A9/MiChargeProcessPhysicalPages_function_00A99CDC.md) (function, `0x00A99CDC`)
- `0x0032B347` → [PsReferencePartitionSafe](../3B/PsReferencePartitionSafe_function_003BA6C0.md) (function, `0x003BA6C0`)
- `0x0032B35C` → [MiReturnProcessPhysicalPages](../../page/AB/MiReturnProcessPhysicalPages_function_00AB91B8.md) (function, `0x00AB91B8`)
- `0x0032B384` → [MiFreeLargeZeroPages](../3B/MiFreeLargeZeroPages_function_003B5F0C.md) (function, `0x003B5F0C`)
- `0x0032B38F` → [MiReturnResident](../28/MiReturnResident_function_00286890.md) (function, `0x00286890`)
- `0x0032B3A6` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (function, `0x009E5D58`)
- `0x0032B3B4` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0032B440` → [MiLocateLockedVadEvent](../2A/MiLocateLockedVadEvent_function_002A7A0C.md) (function, `0x002A7A0C`)
- `0x0032B4B4` → [MiGetVadLargePageMinimumIndex](../4F/MiGetVadLargePageMinimumIndex_function_004F8038.md) (function, `0x004F8038`)
- `0x0032B4FE` → [MiCreateLargePfnList](../3D/MiCreateLargePfnList_function_003D2DA8.md) (function, `0x003D2DA8`)
- `0x0032B51E` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x0032B538` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (function, `0x009E5D58`)
- `0x0032B545` → [MiReturnProcessPhysicalPages](../../page/AB/MiReturnProcessPhysicalPages_function_00AB91B8.md) (function, `0x00AB91B8`)
- `0x0032B557` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x0032B56B` → [MiReturnCrossPartitionCharges](../28/MiReturnCrossPartitionCharges_function_002867D0.md) (function, `0x002867D0`)
- `0x0032B576` → [MiReturnProcessPhysicalPages](../../page/AB/MiReturnProcessPhysicalPages_function_00AB91B8.md) (function, `0x00AB91B8`)
- `0x0032B58D` → [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) (function, `0x00887630`)
- `0x0032B5A8` → [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) (function, `0x00887630`)
- `0x0032B5E3` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (function, `0x009E5D58`)
- `0x0032B5FE` → [MiFlushGraphicsPtes](../4E/MiFlushGraphicsPtes_function_004E1374.md) (function, `0x004E1374`)
- `0x0032B620` → [MiFlushGraphicsPtes](../4E/MiFlushGraphicsPtes_function_004E1374.md) (function, `0x004E1374`)
- `0x0032B63B` → [MiFlushGraphicsPtes](../4E/MiFlushGraphicsPtes_function_004E1374.md) (function, `0x004E1374`)
- `0x0032B664` → [MiReturnProcessPhysicalPages](../../page/AB/MiReturnProcessPhysicalPages_function_00AB91B8.md) (function, `0x00AB91B8`)

### Direct callers
- [MiAllocateVirtualMemory](../../page/88/MiAllocateVirtualMemory_function_00883B40.md) at `0x00883DE1`
- [MiAllocateFromSubAllocatedRegion](../../page/98/MiAllocateFromSubAllocatedRegion_function_00981C24.md) at `0x00981DC9`
- [MiLoadSectionIntoVsmEnclave](../../page/AB/MiLoadSectionIntoVsmEnclave_function_00AB1D4C.md) at `0x00AB1F16`
- [MiLoadDataIntoVsmEnclave](../../page/AC/MiLoadDataIntoVsmEnclave_function_00ACD114.md) at `0x00ACD306`

### Static image references
- `0x0032A87C` → RVA `0x00E0A740` (`.data`; read)
- `0x0032A95E` → RVA `0x00E30088` (`.data`; read)
- `0x0032A992` → RVA `0x00E2DC80` (`.data`; read)
- `0x0032B070` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x0032AADB` → [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) (`.text` → `PAGE`)
  - `0x0032AB72` → [MiCommitPageTablesForVad](../../page/88/MiCommitPageTablesForVad_function_00886D50.md) (`.text` → `PAGE`)
  - `0x0032AEA0` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (`.text` → `PAGE`)
  - `0x0032B31C` → [MiChargeProcessPhysicalPages](../../page/A9/MiChargeProcessPhysicalPages_function_00A99CDC.md) (`.text` → `PAGE`)
  - `0x0032B35C` → [MiReturnProcessPhysicalPages](../../page/AB/MiReturnProcessPhysicalPages_function_00AB91B8.md) (`.text` → `PAGE`)
  - `0x0032B3A6` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (`.text` → `PAGE`)
  - `0x0032B538` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (`.text` → `PAGE`)
  - `0x0032B545` → [MiReturnProcessPhysicalPages](../../page/AB/MiReturnProcessPhysicalPages_function_00AB91B8.md) (`.text` → `PAGE`)
  - `0x0032B576` → [MiReturnProcessPhysicalPages](../../page/AB/MiReturnProcessPhysicalPages_function_00AB91B8.md) (`.text` → `PAGE`)
  - `0x0032B58D` → [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) (`.text` → `PAGE`)
  - `0x0032B5A8` → [MiChargeFullProcessCommitment](../../page/88/MiChargeFullProcessCommitment_function_00887630.md) (`.text` → `PAGE`)
  - `0x0032B5E3` → [MiReturnFullProcessCommitment](../../page/9E/MiReturnFullProcessCommitment_function_009E5D58.md) (`.text` → `PAGE`)
  - `0x0032B664` → [MiReturnProcessPhysicalPages](../../page/AB/MiReturnProcessPhysicalPages_function_00AB91B8.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0032A860  40 55                           push rbp
0032A862  53                              push rbx
0032A863  56                              push rsi
0032A864  57                              push rdi
0032A865  41 54                           push r12
0032A867  41 55                           push r13
0032A869  41 56                           push r14
0032A86B  41 57                           push r15
0032A86D  48 8D AC 24 38 FF FF FF         lea rbp, [rsp - 0xc8]
0032A875  48 81 EC C8 01 00 00            sub rsp, 0x1c8
0032A87C  48 8B 05 BD FE AD 00            mov rax, qword ptr [rip + 0xadfebd]
0032A883  48 33 C4                        xor rax, rsp
0032A886  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
0032A88D  48 8B 85 58 01 00 00            mov rax, qword ptr [rbp + 0x158]
0032A894  33 F6                           xor esi, esi
0032A896  4C 8B 95 50 01 00 00            mov r10, qword ptr [rbp + 0x150]
0032A89D  48 8B D9                        mov rbx, rcx
0032A8A0  4C 8B B5 60 01 00 00            mov r14, qword ptr [rbp + 0x160]
0032A8A7  4C 8B E2                        mov r12, rdx
0032A8AA  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0032A8AE  BA 01 00 00 00                  mov edx, 1
0032A8B3  33 C0                           xor eax, eax
0032A8B5  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
0032A8BA  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0032A8BE  49 8B F8                        mov rdi, r8
0032A8C1  44 8B 41 30                     mov r8d, dword ptr [rcx + 0x30]
0032A8C5  0F 57 C0                        xorps xmm0, xmm0
0032A8C8  41 8B C0                        mov eax, r8d
0032A8CB  4C 89 55 88                     mov qword ptr [rbp - 0x78], r10
0032A8CF  25 00 00 20 04                  and eax, 0x4200000
0032A8D4  48 89 75 E0                     mov qword ptr [rbp - 0x20], rsi
0032A8D8  3D 00 00 20 04                  cmp eax, 0x4200000
0032A8DD  89 75 9C                        mov dword ptr [rbp - 0x64], esi
0032A8E0  8B CE                           mov ecx, esi
0032A8E2  0F 44 CA                        cmove ecx, edx
0032A8E5  89 4D 98                        mov dword ptr [rbp - 0x68], ecx
0032A8E8  41 8B C9                        mov ecx, r9d
0032A8EB  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
0032A8EF  E8 8C EB FF FF                  call 0x140329480
0032A8F4  41 8B C8                        mov ecx, r8d
0032A8F7  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
0032A8FB  C1 E9 07                        shr ecx, 7
0032A8FE  8B D0                           mov edx, eax
0032A900  83 E1 1F                        and ecx, 0x1f
0032A903  83 F8 18                        cmp eax, 0x18
0032A906  0F 84 04 07 00 00               je 0x14032b010
0032A90C  83 F9 18                        cmp ecx, 0x18
0032A90F  0F 84 63 06 00 00               je 0x14032af78
0032A915  83 E1 18                        and ecx, 0x18
0032A918  0F 85 66 08 00 00               jne 0x14032b184
0032A91E  8B C2                           mov eax, edx
0032A920  83 E0 18                        and eax, 0x18
0032A923  83 F8 18                        cmp eax, 0x18
0032A926  0F 84 29 0D 00 00               je 0x14032b655
0032A92C  83 F8 08                        cmp eax, 8
0032A92F  75 07                           jne 0x14032a938
0032A931  83 E2 F7                        and edx, 0xfffffff7
0032A934  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
0032A938  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0032A941  4C 8B EE                        mov r13, rsi
0032A944  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0032A948  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
0032A94D  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
0032A957  4C 8B 88 B8 00 00 00            mov r9, qword ptr [rax + 0xb8]
0032A95E  48 8B 05 23 57 B0 00            mov rax, qword ptr [rip + 0xb05723]
0032A965  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
0032A96A  41 0F B7 89 AE 04 00 00         movzx ecx, word ptr [r9 + 0x4ae]
0032A972  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0032A976  0F B7 01                        movzx eax, word ptr [rcx]
0032A979  66 41 89 06                     mov word ptr [r14], ax
0032A97D  44 8B 43 30                     mov r8d, dword ptr [rbx + 0x30]
0032A981  41 0F BA E0 19                  bt r8d, 0x19
0032A986  0F 82 CD 07 00 00               jb 0x14032b159
0032A98C  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
0032A990  8B C2                           mov eax, edx
0032A992  48 8B 15 E7 32 B0 00            mov rdx, qword ptr [rip + 0xb032e7]
0032A999  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0032A99D  83 E0 1F                        and eax, 0x1f
0032A9A0  48 C1 E0 05                     shl rax, 5
0032A9A4  48 85 D2                        test rdx, rdx
0032A9A7  74 0D                           je 0x14032a9b6
0032A9A9  48 85 D0                        test rax, rdx
0032A9AC  0F 84 E0 04 00 00               je 0x14032ae92
0032A9B2  48 83 C8 10                     or rax, 0x10
0032A9B6  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0032A9BA  41 8B C0                        mov eax, r8d
0032A9BD  25 00 00 20 14                  and eax, 0x14200000
0032A9C2  3D 00 00 20 10                  cmp eax, 0x10200000
0032A9C7  0F 84 7A 08 00 00               je 0x14032b247
0032A9CD  49 8B CC                        mov rcx, r12
0032A9D0  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0032A9DA  48 C1 E9 09                     shr rcx, 9
0032A9DE  48 23 C8                        and rcx, rax
0032A9E1  49 8B C3                        mov rax, r11
0032A9E4  48 03 C8                        add rcx, rax
0032A9E7  4D 8D 7C 24 FF                  lea r15, [r12 - 1]
0032A9EC  4C 03 FF                        add r15, rdi
0032A9EF  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
0032A9F3  49 81 CF FF 0F 00 00            or r15, 0xfff
0032A9FA  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0032AA04  49 8B D7                        mov rdx, r15
0032AA07  48 8B D9                        mov rbx, rcx
0032AA0A  48 C1 EA 09                     shr rdx, 9
0032AA0E  48 23 D0                        and rdx, rax
0032AA11  49 8B C3                        mov rax, r11
0032AA14  48 03 D0                        add rdx, rax
0032AA17  48 89 75 60                     mov qword ptr [rbp + 0x60], rsi
0032AA1B  48 8D 45 50                     lea rax, [rbp + 0x50]
0032AA1F  48 89 55 F8                     mov qword ptr [rbp - 8], rdx
0032AA23  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
0032AA27  33 FF                           xor edi, edi
0032AA29  48 8D 45 50                     lea rax, [rbp + 0x50]
0032AA2D  48 89 75 78                     mov qword ptr [rbp + 0x78], rsi
0032AA31  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
0032AA35  4C 8B DA                        mov r11, rdx
0032AA38  4C 2B D9                        sub r11, rcx
0032AA3B  48 89 B5 90 00 00 00            mov qword ptr [rbp + 0x90], rsi
0032AA42  48 8D 45 68                     lea rax, [rbp + 0x68]
0032AA46  49 C1 FB 03                     sar r11, 3
0032AA4A  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
0032AA4E  49 FF C3                        inc r11
0032AA51  48 8D 45 68                     lea rax, [rbp + 0x68]
0032AA55  4C 89 5D F0                     mov qword ptr [rbp - 0x10], r11
0032AA59  48 89 45 68                     mov qword ptr [rbp + 0x68], rax
0032AA5D  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
0032AA64  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
0032AA6B  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
0032AA72  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
0032AA79  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
0032AA80  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
0032AA87  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
0032AA8E  48 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], rax
0032AA95  41 8B C0                        mov eax, r8d
0032AA98  25 00 00 A0 00                  and eax, 0xa00000
0032AA9D  48 89 B5 A8 00 00 00            mov qword ptr [rbp + 0xa8], rsi
0032AAA4  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
0032AAA9  48 89 7D C0                     mov qword ptr [rbp - 0x40], rdi
0032AAAD  3D 00 00 A0 00                  cmp eax, 0xa00000
0032AAB2  0F 84 C8 07 00 00               je 0x14032b280
0032AAB8  F6 85 38 01 00 00 1A            test byte ptr [rbp + 0x138], 0x1a
0032AABF  0F 85 C6 03 00 00               jne 0x14032ae8b
0032AAC5  B8 01 00 00 00                  mov eax, 1
0032AACA  C7 45 94 03 00 00 00            mov dword ptr [rbp - 0x6c], 3
0032AAD1  49 8B D3                        mov rdx, r11
0032AAD4  48 89 45 00                     mov qword ptr [rbp], rax
0032AAD8  49 8B C9                        mov rcx, r9
0032AADB  E8 50 CB 55 00                  call 0x140887630
0032AAE0  48 C7 44 24 78 01 00 00 00      mov qword ptr [rsp + 0x78], 1
0032AAE9  85 C0                           test eax, eax
0032AAEB  0F 88 7A 05 00 00               js 0x14032b06b
0032AAF1  4C 8B 4D F0                     mov r9, qword ptr [rbp - 0x10]
0032AAF5  4C 89 4D 80                     mov qword ptr [rbp - 0x80], r9
0032AAF9  4D 8B F1                        mov r14, r9
0032AAFC  C7 45 A4 01 00 00 00            mov dword ptr [rbp - 0x5c], 1
0032AB03  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0032AB08  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0032AB0D  33 C0                           xor eax, eax
0032AB0F  48 8B CA                        mov rcx, rdx
0032AB12  89 45 A0                        mov dword ptr [rbp - 0x60], eax
0032AB15  E8 A6 89 F9 FF                  call 0x1402c34c0
0032AB1A  85 C0                           test eax, eax
0032AB1C  74 66                           je 0x14032ab84
0032AB1E  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0032AB22  48 8D BE 60 02 00 00            lea rdi, [rsi + 0x260]
0032AB29  45 33 C0                        xor r8d, r8d
0032AB2C  C7 45 A0 01 00 00 00            mov dword ptr [rbp - 0x60], 1
0032AB33  33 D2                           xor edx, edx
0032AB35  48 8B CF                        mov rcx, rdi
0032AB38  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
0032AB3F  90                              nop
0032AB40  E8 EB 56 EE FF                  call 0x140210230
0032AB45  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0032AB4B  48 8B F0                        mov rsi, rax
0032AB4E  73 0E                           jae 0x14032ab5e
0032AB50  4C 8B C7                        mov r8, rdi
0032AB53  48 8B D0                        mov rdx, rax
0032AB56  48 8B CF                        mov rcx, rdi
0032AB59  E8 32 51 EE FF                  call 0x14020fc90
0032AB5E  48 85 F6                        test rsi, rsi
0032AB61  74 04                           je 0x14032ab67
0032AB63  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0032AB67  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0032AB6C  4D 8B C7                        mov r8, r15
0032AB6F  49 8B D4                        mov rdx, r12
0032AB72  E8 D9 C1 55 00                  call 0x140886d50
0032AB77  85 C0                           test eax, eax
0032AB79  0F 88 C8 04 00 00               js 0x14032b047
0032AB7F  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0032AB84  48 8B 7D 00                     mov rdi, qword ptr [rbp]
0032AB88  33 C9                           xor ecx, ecx
0032AB8A  44 0F B7 F1                     movzx r14d, cx
0032AB8E  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
0032AB92  8B F1                           mov esi, ecx
0032AB94  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0032AB99  44 8B E9                        mov r13d, ecx
0032AB9C  44 8B F9                        mov r15d, ecx
0032AB9F  83 7D 94 00                     cmp dword ptr [rbp - 0x6c], 0
0032ABA3  44 8B E1                        mov r12d, ecx
0032ABA6  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
0032ABAA  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
0032ABAE  0F 84 F2 05 00 00               je 0x14032b1a6
0032ABB4  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032ABB9  48 81 C1 00 04 00 00            add rcx, 0x400
0032ABC0  E8 2B 20 F5 FF                  call 0x14027cbf0
0032ABC5  88 44 24 50                     mov byte ptr [rsp + 0x50], al
0032ABC9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0032ABD0  48 3B 5D F8                     cmp rbx, qword ptr [rbp - 8]
0032ABD4  0F 87 E2 01 00 00               ja 0x14032adbc
0032ABDA  45 85 E4                        test r12d, r12d
0032ABDD  0F 84 05 01 00 00               je 0x14032ace8
0032ABE3  48 F7 C3 FF 0F 00 00            test rbx, 0xfff
0032ABEA  0F 84 F8 00 00 00               je 0x14032ace8
0032ABF0  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
0032ABFA  48 83 7C 24 68 00               cmp qword ptr [rsp + 0x68], 0
0032AC00  0F 84 A9 01 00 00               je 0x14032adaf
0032AC06  4C 03 FF                        add r15, rdi
0032AC09  48 8B 13                        mov rdx, qword ptr [rbx]
0032AC0C  49 8B C0                        mov rax, r8
0032AC0F  48 3B D8                        cmp rbx, rax
0032AC12  72 34                           jb 0x14032ac48
0032AC14  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
0032AC1E  48 8B C0                        mov rax, rax
0032AC21  48 3B D8                        cmp rbx, rax
0032AC24  77 22                           ja 0x14032ac48
0032AC26  4C 8B C2                        mov r8, rdx
0032AC29  F6 C2 01                        test dl, 1
0032AC2C  74 10                           je 0x14032ac3e
0032AC2E  F6 C2 42                        test dl, 0x42
0032AC31  0F 95 C1                        setne cl
0032AC34  F6 C2 20                        test dl, 0x20
0032AC37  0F 95 C0                        setne al
0032AC3A  84 C8                           test al, cl
0032AC3C  74 6A                           je 0x14032aca8
0032AC3E  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
0032AC48  48 89 55 A8                     mov qword ptr [rbp - 0x58], rdx
0032AC4C  48 85 D2                        test rdx, rdx
0032AC4F  0F 85 6D 02 00 00               jne 0x14032aec2
0032AC55  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0032AC5A  48 3B 5D B8                     cmp rbx, qword ptr [rbp - 0x48]
0032AC5E  48 8D 04 31                     lea rax, [rcx + rsi]
0032AC62  48 0F 47 C6                     cmova rax, rsi
0032AC66  48 8B F0                        mov rsi, rax
0032AC69  48 83 F9 01                     cmp rcx, 1
0032AC6D  0F 85 31 01 00 00               jne 0x14032ada4
0032AC73  49 8B C0                        mov rax, r8
0032AC76  48 3B D8                        cmp rbx, rax
0032AC79  0F 83 03 08 00 00               jae 0x14032b482
0032AC7F  66 44 03 F7                     add r14w, di
0032AC83  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
0032AC87  48 89 03                        mov qword ptr [rbx], rax
0032AC8A  45 85 ED                        test r13d, r13d
0032AC8D  0F 85 4C 05 00 00               jne 0x14032b1df
0032AC93  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
0032AC97  48 8D 1C FB                     lea rbx, [rbx + rdi*8]
0032AC9B  48 8D 04 C8                     lea rax, [rax + rcx*8]
0032AC9F  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0032ACA3  E9 28 FF FF FF                  jmp 0x14032abd0
0032ACA8  E8 EB 0C 00 00                  call 0x14032b998
0032ACAD  48 85 C0                        test rax, rax
0032ACB0  74 8C                           je 0x14032ac3e
0032ACB2  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
0032ACB9  48 85 C9                        test rcx, rcx
0032ACBC  74 80                           je 0x14032ac3e
0032ACBE  48 8B C3                        mov rax, rbx
0032ACC1  48 C1 E8 03                     shr rax, 3
0032ACC5  25 FF 01 00 00                  and eax, 0x1ff
0032ACCA  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0032ACCE  A8 20                           test al, 0x20
0032ACD0  74 04                           je 0x14032acd6
0032ACD2  49 83 C8 20                     or r8, 0x20
0032ACD6  49 8B D0                        mov rdx, r8
0032ACD9  48 83 CA 42                     or rdx, 0x42
0032ACDD  A8 42                           test al, 0x42
0032ACDF  49 0F 44 D0                     cmove rdx, r8
0032ACE3  E9 56 FF FF FF                  jmp 0x14032ac3e
0032ACE8  66 45 85 F6                     test r14w, r14w
0032ACEC  0F 85 AB 02 00 00               jne 0x14032af9d
0032ACF2  83 7D 98 00                     cmp dword ptr [rbp - 0x68], 0
0032ACF6  0F 85 F1 08 00 00               jne 0x14032b5ed
0032ACFC  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
0032AD01  41 83 F8 01                     cmp r8d, 1
0032AD05  74 35                           je 0x14032ad3c
0032AD07  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
0032AD0B  48 85 D2                        test rdx, rdx
0032AD0E  0F 85 BC 02 00 00               jne 0x14032afd0
0032AD14  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0032AD1E  48 8B CB                        mov rcx, rbx
0032AD21  48 C1 E9 09                     shr rcx, 9
0032AD25  48 23 C8                        and rcx, rax
0032AD28  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0032AD32  48 8B C0                        mov rax, rax
0032AD35  48 03 C8                        add rcx, rax
0032AD38  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
0032AD3C  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0032AD41  45 8B C8                        mov r9d, r8d
0032AD44  44 0F B6 44 24 50               movzx r8d, byte ptr [rsp + 0x50]
0032AD4A  48 8B CB                        mov rcx, rbx
0032AD4D  8B 50 30                        mov edx, dword ptr [rax + 0x30]
0032AD50  C1 EA 0C                        shr edx, 0xc
0032AD53  83 E2 7F                        and edx, 0x7f
0032AD56  E8 15 52 F5 FF                  call 0x14027ff70
0032AD5B  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
0032AD65  49 8B C0                        mov rax, r8
0032AD68  48 3B D8                        cmp rbx, rax
0032AD6B  0F 83 36 01 00 00               jae 0x14032aea7
0032AD71  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0032AD7B  48 8B CB                        mov rcx, rbx
0032AD7E  48 C1 E9 09                     shr rcx, 9
0032AD82  48 23 C8                        and rcx, rax
0032AD85  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0032AD8F  48 8B C0                        mov rax, rax
0032AD92  48 03 C8                        add rcx, rax
0032AD95  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
0032AD99  41 BC 01 00 00 00               mov r12d, 1
0032AD9F  E9 56 FE FF FF                  jmp 0x14032abfa
0032ADA4  41 BD 01 00 00 00               mov r13d, 1
0032ADAA  E9 DB FE FF FF                  jmp 0x14032ac8a
0032ADAF  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
0032ADB4  4C 8B FF                        mov r15, rdi
0032ADB7  E9 4D FE FF FF                  jmp 0x14032ac09
0032ADBC  66 45 85 F6                     test r14w, r14w
0032ADC0  74 13                           je 0x14032add5
0032ADC2  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
0032ADC6  41 B9 02 00 00 00               mov r9d, 2
0032ADCC  45 0F B7 C6                     movzx r8d, r14w
0032ADD0  E8 5B 88 F1 FF                  call 0x140243630
0032ADD5  83 7D 98 00                     cmp dword ptr [rbp - 0x68], 0
0032ADD9  0F 85 30 08 00 00               jne 0x14032b60f
0032ADDF  83 7C 24 60 01                  cmp dword ptr [rsp + 0x60], 1
0032ADE4  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0032ADE9  0F 84 CB 01 00 00               je 0x14032afba
0032ADEF  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0032ADF3  48 85 C0                        test rax, rax
0032ADF6  74 0F                           je 0x14032ae07
0032ADF8  48 8B D0                        mov rdx, rax
0032ADFB  48 8D 8B 00 04 00 00            lea rcx, [rbx + 0x400]
0032AE02  E8 B9 C0 EE FF                  call 0x140216ec0
0032AE07  0F B6 54 24 50                  movzx edx, byte ptr [rsp + 0x50]
0032AE0C  48 8D 8B 00 04 00 00            lea rcx, [rbx + 0x400]
0032AE13  E8 78 28 F5 FF                  call 0x14027d690
0032AE18  83 7D A0 00                     cmp dword ptr [rbp - 0x60], 0
0032AE1C  74 0C                           je 0x14032ae2a
0032AE1E  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
0032AE22  48 8B D3                        mov rdx, rbx
0032AE25  E8 A6 79 FB FF                  call 0x1402e27d0
0032AE2A  83 7D A4 00                     cmp dword ptr [rbp - 0x5c], 0
0032AE2E  74 10                           je 0x14032ae40
0032AE30  48 85 F6                        test rsi, rsi
0032AE33  75 65                           jne 0x14032ae9a
0032AE35  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0032AE39  48 2B C6                        sub rax, rsi
0032AE3C  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0032AE40  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
0032AE45  41 8B 48 34                     mov ecx, dword ptr [r8 + 0x34]
0032AE49  41 0F B6 50 22                  movzx edx, byte ptr [r8 + 0x22]
0032AE4E  48 C1 E2 20                     shl rdx, 0x20
0032AE52  48 0B D1                        or rdx, rcx
0032AE55  48 03 55 80                     add rdx, qword ptr [rbp - 0x80]
0032AE59  41 89 50 34                     mov dword ptr [r8 + 0x34], edx
0032AE5D  48 C1 EA 20                     shr rdx, 0x20
0032AE61  41 88 50 22                     mov byte ptr [r8 + 0x22], dl
0032AE65  33 C0                           xor eax, eax
0032AE67  48 8B 8D B0 00 00 00            mov rcx, qword ptr [rbp + 0xb0]
0032AE6E  48 33 CC                        xor rcx, rsp
0032AE71  E8 CA 17 38 00                  call 0x1406ac640
0032AE76  48 81 C4 C8 01 00 00            add rsp, 0x1c8
0032AE7D  41 5F                           pop r15
0032AE7F  41 5E                           pop r14
0032AE81  41 5D                           pop r13
0032AE83  41 5C                           pop r12
0032AE85  5F                              pop rdi
0032AE86  5E                              pop rsi
0032AE87  5B                              pop rbx
0032AE88  5D                              pop rbp
0032AE89  C3                              ret
0032AE8A  CC                              int3
0032AE8B  B8 0D 00 00 C0                  mov eax, 0xc000000d
0032AE90  EB D5                           jmp 0x14032ae67
0032AE92  48 0B C2                        or rax, rdx
0032AE95  E9 1C FB FF FF                  jmp 0x14032a9b6
0032AE9A  48 8B D6                        mov rdx, rsi
0032AE9D  48 8B CB                        mov rcx, rbx
0032AEA0  E8 B3 AE 6B 00                  call 0x1409e5d58
0032AEA5  EB 8E                           jmp 0x14032ae35
0032AEA7  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0032AEB1  48 8B C0                        mov rax, rax
0032AEB4  48 3B D8                        cmp rbx, rax
0032AEB7  0F 86 DC FE FF FF               jbe 0x14032ad99
0032AEBD  E9 AF FE FF FF                  jmp 0x14032ad71
0032AEC2  48 8B CA                        mov rcx, rdx
0032AEC5  E8 C6 B0 F9 FF                  call 0x1402c5f90
0032AECA  85 C0                           test eax, eax
0032AECC  0F 85 39 02 00 00               jne 0x14032b10b
0032AED2  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
0032AED6  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0032AEDB  48 03 F1                        add rsi, rcx
0032AEDE  83 38 00                        cmp dword ptr [rax], 0
0032AEE1  0F 85 A3 FD FF FF               jne 0x14032ac8a
0032AEE7  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0032AEEC  4C 8D 4D 9C                     lea r9, [rbp - 0x64]
0032AEF0  33 C0                           xor eax, eax
0032AEF2  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0032AEF6  66 89 45 90                     mov word ptr [rbp - 0x70], ax
0032AEFA  48 8B D3                        mov rdx, rbx
0032AEFD  48 8D 45 90                     lea rax, [rbp - 0x70]
0032AF01  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0032AF06  E8 05 0B 00 00                  call 0x14032ba10
0032AF0B  48 83 7D E0 00                  cmp qword ptr [rbp - 0x20], 0
0032AF10  0F 84 D5 00 00 00               je 0x14032afeb
0032AF16  66 45 85 F6                     test r14w, r14w
0032AF1A  0F 84 58 03 00 00               je 0x14032b278
0032AF20  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
0032AF24  41 B9 02 00 00 00               mov r9d, 2
0032AF2A  45 0F B7 C6                     movzx r8d, r14w
0032AF2E  E8 FD 86 F1 FF                  call 0x140243630
0032AF33  45 33 E4                        xor r12d, r12d
0032AF36  45 0F B7 F4                     movzx r14d, r12w
0032AF3A  83 7D 98 00                     cmp dword ptr [rbp - 0x68], 0
0032AF3E  0F 85 E6 06 00 00               jne 0x14032b62a
0032AF44  83 7C 24 60 01                  cmp dword ptr [rsp + 0x60], 1
0032AF49  0F 85 CB 00 00 00               jne 0x14032b01a
0032AF4F  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032AF54  0F B6 54 24 50                  movzx edx, byte ptr [rsp + 0x50]
0032AF59  48 81 C1 00 04 00 00            add rcx, 0x400
0032AF60  E8 0B 3D F5 FF                  call 0x14027ec70
0032AF65  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
0032AF69  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0032AF6E  48 8B 08                        mov rcx, qword ptr [rax]
0032AF71  33 C9                           xor ecx, ecx
0032AF73  E9 27 FC FF FF                  jmp 0x14032ab9f
0032AF78  41 0F BA E0 15                  bt r8d, 0x15
0032AF7D  0F 82 9B F9 FF FF               jb 0x14032a91e
0032AF83  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
0032AF87  8B 48 20                        mov ecx, dword ptr [rax + 0x20]
0032AF8A  D1 E9                           shr ecx, 1
0032AF8C  83 E1 1F                        and ecx, 0x1f
0032AF8F  83 F9 18                        cmp ecx, 0x18
0032AF92  0F 84 86 F9 FF FF               je 0x14032a91e
0032AF98  E9 78 F9 FF FF                  jmp 0x14032a915
0032AF9D  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
0032AFA1  41 B9 02 00 00 00               mov r9d, 2
0032AFA7  45 0F B7 C6                     movzx r8d, r14w
0032AFAB  E8 80 86 F1 FF                  call 0x140243630
0032AFB0  33 C0                           xor eax, eax
0032AFB2  44 8B F0                        mov r14d, eax
0032AFB5  E9 38 FD FF FF                  jmp 0x14032acf2
0032AFBA  0F B6 54 24 50                  movzx edx, byte ptr [rsp + 0x50]
0032AFBF  48 8D 8B 00 04 00 00            lea rcx, [rbx + 0x400]
0032AFC6  E8 A5 3C F5 FF                  call 0x14027ec70
0032AFCB  E9 48 FE FF FF                  jmp 0x14032ae18
0032AFD0  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032AFD5  48 81 C1 00 04 00 00            add rcx, 0x400
0032AFDC  E8 DF BE EE FF                  call 0x140216ec0
0032AFE1  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
0032AFE6  E9 29 FD FF FF                  jmp 0x14032ad14
0032AFEB  39 44 24 54                     cmp dword ptr [rsp + 0x54], eax
0032AFEF  75 0B                           jne 0x14032affc
0032AFF1  8B 85 30 01 00 00               mov eax, dword ptr [rbp + 0x130]
0032AFF7  39 45 9C                        cmp dword ptr [rbp - 0x64], eax
0032AFFA  74 0A                           je 0x14032b006
0032AFFC  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
0032B000  C7 00 01 00 00 00               mov dword ptr [rax], 1
0032B006  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0032B00B  E9 7A FC FF FF                  jmp 0x14032ac8a
0032B010  BA 18 00 00 00                  mov edx, 0x18
0032B015  E9 1A F9 FF FF                  jmp 0x14032a934
0032B01A  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
0032B01F  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
0032B023  49 8D 8C 24 00 04 00 00         lea rcx, [r12 + 0x400]
0032B02B  E8 90 BE EE FF                  call 0x140216ec0
0032B030  0F B6 54 24 50                  movzx edx, byte ptr [rsp + 0x50]
0032B035  49 8D 8C 24 00 04 00 00         lea rcx, [r12 + 0x400]
0032B03D  E8 4E 26 F5 FF                  call 0x14027d690
0032B042  E9 1E FF FF FF                  jmp 0x14032af65
0032B047  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0032B04C  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
0032B050  48 8B D3                        mov rdx, rbx
0032B053  E8 78 77 FB FF                  call 0x1402e27d0
0032B058  4D 85 F6                        test r14, r14
0032B05B  0F 85 0A 03 00 00               jne 0x14032b36b
0032B061  B8 2D 01 00 C0                  mov eax, 0xc000012d
0032B066  E9 FC FD FF FF                  jmp 0x14032ae67
0032B06B  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
0032B070  4C 8D 2D 89 4F CD FF            lea r13, [rip - 0x32b077]
0032B077  33 C0                           xor eax, eax
0032B079  49 8D 89 00 04 00 00            lea rcx, [r9 + 0x400]
0032B080  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
0032B083  E8 68 1B F5 FF                  call 0x14027cbf0
0032B088  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
0032B08D  48 8D 55 C0                     lea rdx, [rbp - 0x40]
0032B091  0F B6 F0                        movzx esi, al
0032B094  48 85 FF                        test rdi, rdi
0032B097  B8 00 00 00 00                  mov eax, 0
0032B09C  49 8B CC                        mov rcx, r12
0032B09F  48 0F 44 D0                     cmove rdx, rax
0032B0A3  44 0F B6 CE                     movzx r9d, sil
0032B0A7  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
0032B0AC  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
0032B0B3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0032B0B8  49 8B D7                        mov rdx, r15
0032B0BB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0032B0BF  E8 70 AB F9 FF                  call 0x1402c5c34
0032B0C4  40 0F B6 D6                     movzx edx, sil
0032B0C8  48 8B F8                        mov rdi, rax
0032B0CB  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0032B0D0  48 8D 8E 00 04 00 00            lea rcx, [rsi + 0x400]
0032B0D7  E8 B4 25 F5 FF                  call 0x14027d690
0032B0DC  4C 8B 4D F0                     mov r9, qword ptr [rbp - 0x10]
0032B0E0  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0032B0E5  4C 2B CF                        sub r9, rdi
0032B0E8  4C 89 4D 80                     mov qword ptr [rbp - 0x80], r9
0032B0EC  48 83 FA 01                     cmp rdx, 1
0032B0F0  0F 84 0D 02 00 00               je 0x14032b303
0032B0F6  48 83 7D C0 00                  cmp qword ptr [rbp - 0x40], 0
0032B0FB  0F 85 02 02 00 00               jne 0x14032b303
0032B101  B8 18 00 00 C0                  mov eax, 0xc0000018
0032B106  E9 5C FD FF FF                  jmp 0x14032ae67
0032B10B  48 83 7C 24 78 01               cmp qword ptr [rsp + 0x78], 1
0032B111  0F 85 C8 00 00 00               jne 0x14032b1df
0032B117  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
0032B11B  48 C1 E1 05                     shl rcx, 5
0032B11F  48 8B C1                        mov rax, rcx
0032B122  48 33 C2                        xor rax, rdx
0032B125  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
0032B12B  48 33 C1                        xor rax, rcx
0032B12E  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0032B133  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0032B137  8B 49 30                        mov ecx, dword ptr [rcx + 0x30]
0032B13A  81 E1 00 00 20 14               and ecx, 0x14200000
0032B140  81 F9 00 00 20 10               cmp ecx, 0x10200000
0032B146  0F 84 64 02 00 00               je 0x14032b3b0
0032B14C  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0032B151  48 89 03                        mov qword ptr [rbx], rax
0032B154  E9 31 FB FF FF                  jmp 0x14032ac8a
0032B159  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
0032B15C  0F B6 4B 21                     movzx ecx, byte ptr [rbx + 0x21]
0032B160  48 C1 E1 20                     shl rcx, 0x20
0032B164  48 0B C8                        or rcx, rax
0032B167  48 B8 FF FF FF FF 0F 00 00 00   movabs rax, 0xfffffffff
0032B171  48 23 C8                        and rcx, rax
0032B174  49 8B C3                        mov rax, r11
0032B177  48 8D 04 C8                     lea rax, [rax + rcx*8]
0032B17B  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0032B17F  E9 0C F8 FF FF                  jmp 0x14032a990
0032B184  83 F9 10                        cmp ecx, 0x10
0032B187  0F 84 A4 F7 FF FF               je 0x14032a931
0032B18D  83 F9 08                        cmp ecx, 8
0032B190  0F 84 B4 04 00 00               je 0x14032b64a
0032B196  83 F9 18                        cmp ecx, 0x18
0032B199  0F 85 99 F7 FF FF               jne 0x14032a938
0032B19F  0B D1                           or edx, ecx
0032B1A1  E9 8E F7 FF FF                  jmp 0x14032a934
0032B1A6  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
0032B1AB  49 8D 89 00 04 00 00            lea rcx, [r9 + 0x400]
0032B1B2  E8 81 82 0A 00                  call 0x1403d3438
0032B1B7  44 8B C0                        mov r8d, eax
0032B1BA  C7 44 24 60 01 00 00 00         mov dword ptr [rsp + 0x60], 1
0032B1C2  49 8D 89 00 04 00 00            lea rcx, [r9 + 0x400]
0032B1C9  E8 42 7F 1B 00                  call 0x1404e3110
0032B1CE  88 44 24 50                     mov byte ptr [rsp + 0x50], al
0032B1D2  3C 11                           cmp al, 0x11
0032B1D4  0F 84 DA F9 FF FF               je 0x14032abb4
0032B1DA  E9 F1 F9 FF FF                  jmp 0x14032abd0
0032B1DF  8B 55 94                        mov edx, dword ptr [rbp - 0x6c]
0032B1E2  48 8D 4D 50                     lea rcx, [rbp + 0x50]
0032B1E6  E8 75 12 17 00                  call 0x14049c460
0032B1EB  48 8D 0C 40                     lea rcx, [rax + rax*2]
0032B1EF  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0032B1F9  48 C1 E1 04                     shl rcx, 4
0032B1FD  48 8B C0                        mov rax, rax
0032B200  44 8B 4D 94                     mov r9d, dword ptr [rbp - 0x6c]
0032B204  4C 8D 45 08                     lea r8, [rbp + 8]
0032B208  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
0032B20C  48 03 C8                        add rcx, rax
0032B20F  48 8D 45 08                     lea rax, [rbp + 8]
0032B213  48 89 4D 08                     mov qword ptr [rbp + 8], rcx
0032B217  48 89 4D 10                     mov qword ptr [rbp + 0x10], rcx
0032B21B  48 89 01                        mov qword ptr [rcx], rax
0032B21E  48 8D 45 08                     lea rax, [rbp + 8]
0032B222  48 89 41 08                     mov qword ptr [rcx + 8], rax
0032B226  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
0032B22A  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0032B22F  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0032B233  E8 1C 7F 0A 00                  call 0x1403d3154
0032B238  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0032B23D  33 C0                           xor eax, eax
0032B23F  44 8B E8                        mov r13d, eax
0032B242  E9 4C FA FF FF                  jmp 0x14032ac93
0032B247  48 8D 4D C8                     lea rcx, [rbp - 0x38]
0032B24B  E8 50 76 F5 FF                  call 0x1402828a0
0032B250  44 8B 43 30                     mov r8d, dword ptr [rbx + 0x30]
0032B254  48 8D 4D C8                     lea rcx, [rbp - 0x38]
0032B258  4C 8B 55 88                     mov r10, qword ptr [rbp - 0x78]
0032B25C  48 0F BA E8 1A                  bts rax, 0x1a
0032B261  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
0032B266  48 89 01                        mov qword ptr [rcx], rax
0032B269  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
0032B273  E9 55 F7 FF FF                  jmp 0x14032a9cd
0032B278  45 33 E4                        xor r12d, r12d
0032B27B  E9 BA FC FF FF                  jmp 0x14032af3a
0032B280  49 C1 E8 13                     shr r8, 0x13
0032B284  4C 8D 2D 75 4D CD FF            lea r13, [rip - 0x32b28b]
0032B28B  41 83 E0 03                     and r8d, 3
0032B28F  41 BB 10 00 00 00               mov r11d, 0x10
0032B295  B8 01 00 00 00                  mov eax, 1
0032B29A  4B 8B 8C C5 78 45 01 00         mov rcx, qword ptr [r13 + r8*8 + 0x14578]
0032B2A2  47 8B 84 85 10 3F 01 00         mov r8d, dword ptr [r13 + r8*4 + 0x13f10]
0032B2AA  49 3B CB                        cmp rcx, r11
0032B2AD  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0032B2B2  41 0F 44 C3                     cmove eax, r11d
0032B2B6  44 89 45 94                     mov dword ptr [rbp - 0x6c], r8d
0032B2BA  48 89 45 00                     mov qword ptr [rbp], rax
0032B2BE  48 8B 85 38 01 00 00            mov rax, qword ptr [rbp + 0x138]
0032B2C5  83 E0 1A                        and eax, 0x1a
0032B2C8  41 83 F8 01                     cmp r8d, 1
0032B2CC  0F 86 FA 00 00 00               jbe 0x14032b3cc
0032B2D2  48 83 F8 02                     cmp rax, 2
0032B2D6  0F 85 AF FB FF FF               jne 0x14032ae8b
0032B2DC  49 83 FA 01                     cmp r10, 1
0032B2E0  0F 84 52 01 00 00               je 0x14032b438
0032B2E6  4D 85 D2                        test r10, r10
0032B2E9  0F 84 74 01 00 00               je 0x14032b463
0032B2EF  49 8B F2                        mov rsi, r10
0032B2F2  4C 89 54 24 60                  mov qword ptr [rsp + 0x60], r10
0032B2F7  48 8B FE                        mov rdi, rsi
0032B2FA  48 89 7D C0                     mov qword ptr [rbp - 0x40], rdi
0032B2FE  E9 74 FD FF FF                  jmp 0x14032b077
0032B303  4D 85 C9                        test r9, r9
0032B306  0F 84 62 03 00 00               je 0x14032b66e
0032B30C  48 83 FA 01                     cmp rdx, 1
0032B310  48 8B CE                        mov rcx, rsi
0032B313  49 8B D1                        mov rdx, r9
0032B316  0F 84 71 02 00 00               je 0x14032b58d
0032B31C  E8 BB E9 76 00                  call 0x140a99cdc
0032B321  85 C0                           test eax, eax
0032B323  0F 84 38 FD FF FF               je 0x14032b061
0032B329  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
0032B32E  48 85 FF                        test rdi, rdi
0032B331  0F 84 71 02 00 00               je 0x14032b5a8
0032B337  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0032B33B  48 3B FE                        cmp rdi, rsi
0032B33E  0F 84 59 01 00 00               je 0x14032b49d
0032B344  48 8B CF                        mov rcx, rdi
0032B347  E8 74 F3 08 00                  call 0x1403ba6c0
0032B34C  84 C0                           test al, al
0032B34E  0F 85 49 01 00 00               jne 0x14032b49d
0032B354  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032B359  49 8B D1                        mov rdx, r9
0032B35C  E8 57 DE 78 00                  call 0x140ab91b8
0032B361  B8 A0 04 00 C0                  mov eax, 0xc00004a0
0032B366  E9 FC FA FF FF                  jmp 0x14032ae67
0032B36B  48 83 7C 24 78 01               cmp qword ptr [rsp + 0x78], 1
0032B371  0F 84 66 02 00 00               je 0x14032b5dd
0032B377  41 B8 01 00 00 00               mov r8d, 1
0032B37D  48 8D 55 50                     lea rdx, [rbp + 0x50]
0032B381  49 8B CD                        mov rcx, r13
0032B384  E8 83 AB 08 00                  call 0x1403b5f0c
0032B389  49 8B D6                        mov rdx, r14
0032B38C  49 8B CD                        mov rcx, r13
0032B38F  E8 FC B4 F5 FF                  call 0x140286890
0032B394  48 83 7C 24 60 00               cmp qword ptr [rsp + 0x60], 0
0032B39A  49 8B D6                        mov rdx, r14
0032B39D  0F 85 AE 01 00 00               jne 0x14032b551
0032B3A3  48 8B CB                        mov rcx, rbx
0032B3A6  E8 AD A9 6B 00                  call 0x1409e5d58
0032B3AB  E9 C0 01 00 00                  jmp 0x14032b570
0032B3B0  48 8D 4D A8                     lea rcx, [rbp - 0x58]
0032B3B4  E8 E7 74 F5 FF                  call 0x1402828a0
0032B3B9  48 0D 00 00 00 04               or rax, 0x4000000
0032B3BF  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0032B3C3  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
0032B3C7  E9 80 FD FF FF                  jmp 0x14032b14c
0032B3CC  0F 85 B3 01 00 00               jne 0x14032b585
0032B3D2  48 83 F8 08                     cmp rax, 8
0032B3D6  0F 85 AF FA FF FF               jne 0x14032ae8b
0032B3DC  B9 02 00 00 00                  mov ecx, 2
0032B3E1  48 BE 00 00 00 00 80 F6 FF FF   movabs rsi, 0xfffff68000000000
0032B3EB  41 2B C8                        sub ecx, r8d
0032B3EE  48 BF F8 FF FF FF 7F 00 00 00   movabs rdi, 0x7ffffffff8
0032B3F8  4C 8B 45 B8                     mov r8, qword ptr [rbp - 0x48]
0032B3FC  48 C1 EB 09                     shr rbx, 9
0032B400  48 23 DF                        and rbx, rdi
0032B403  48 8B C6                        mov rax, rsi
0032B406  48 C1 EA 09                     shr rdx, 9
0032B40A  48 03 D8                        add rbx, rax
0032B40D  48 23 D7                        and rdx, rdi
0032B410  48 8B C6                        mov rax, rsi
0032B413  49 C1 E8 09                     shr r8, 9
0032B417  48 03 D0                        add rdx, rax
0032B41A  4C 23 C7                        and r8, rdi
0032B41D  48 8B C6                        mov rax, rsi
0032B420  4C 03 C0                        add r8, rax
0032B423  48 83 E9 01                     sub rcx, 1
0032B427  75 D3                           jne 0x14032b3fc
0032B429  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
0032B42D  33 FF                           xor edi, edi
0032B42F  48 89 55 F8                     mov qword ptr [rbp - 8], rdx
0032B433  E9 A4 FE FF FF                  jmp 0x14032b2dc
0032B438  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0032B43D  41 8B D3                        mov edx, r11d
0032B440  E8 C7 C5 F7 FF                  call 0x1402a7a0c
0032B445  48 85 C0                        test rax, rax
0032B448  74 14                           je 0x14032b45e
0032B44A  48 8B 70 18                     mov rsi, qword ptr [rax + 0x18]
0032B44E  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
0032B453  48 85 F6                        test rsi, rsi
0032B456  0F 85 9B FE FF FF               jne 0x14032b2f7
0032B45C  EB 05                           jmp 0x14032b463
0032B45E  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
0032B463  41 0F B7 89 AE 04 00 00         movzx ecx, word ptr [r9 + 0x4ae]
0032B46B  48 8B 05 16 4C B0 00            mov rax, qword ptr [rip + 0xb04c16]
0032B472  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0032B476  48 8B B9 B8 00 00 00            mov rdi, qword ptr [rcx + 0xb8]
0032B47D  E9 78 FE FF FF                  jmp 0x14032b2fa
0032B482  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0032B48C  48 8B C0                        mov rax, rax
0032B48F  48 3B D8                        cmp rbx, rax
0032B492  0F 87 E7 F7 FF FF               ja 0x14032ac7f
0032B498  E9 E6 F7 FF FF                  jmp 0x14032ac83
0032B49D  48 8B 07                        mov rax, qword ptr [rdi]
0032B4A0  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0032B4A5  0F B7 00                        movzx eax, word ptr [rax]
0032B4A8  66 41 89 06                     mov word ptr [r14], ax
0032B4AC  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
0032B4B1  49 8B CA                        mov rcx, r10
0032B4B4  E8 7F CB 1C 00                  call 0x1404f8038
0032B4B9  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
0032B4BD  49 8B D4                        mov rdx, r12
0032B4C0  8B C8                           mov ecx, eax
0032B4C2  4D 8B C6                        mov r8, r14
0032B4C5  48 8D 45 50                     lea rax, [rbp + 0x50]
0032B4C9  4C 89 55 20                     mov qword ptr [rbp + 0x20], r10
0032B4CD  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0032B4D2  33 C0                           xor eax, eax
0032B4D4  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0032B4D8  0F B6 85 48 01 00 00            movzx eax, byte ptr [rbp + 0x148]
0032B4DF  4D 8B 8C CD 60 1C 01 00         mov r9, qword ptr [r13 + rcx*8 + 0x11c60]
0032B4E7  48 8D 4D 20                     lea rcx, [rbp + 0x20]
0032B4EB  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0032B4F0  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0032B4F4  8B 85 40 01 00 00               mov eax, dword ptr [rbp + 0x140]
0032B4FA  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0032B4FE  E8 A5 78 0A 00                  call 0x1403d2da8
0032B503  8B F8                           mov edi, eax
0032B505  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0032B50A  48 85 C0                        test rax, rax
0032B50D  0F 84 C2 00 00 00               je 0x14032b5d5
0032B513  48 3B C6                        cmp rax, rsi
0032B516  48 8B F0                        mov rsi, rax
0032B519  74 08                           je 0x14032b523
0032B51B  48 8B C8                        mov rcx, rax
0032B51E  E8 4D 79 01 00                  call 0x140342e70
0032B523  85 FF                           test edi, edi
0032B525  0F 89 50 01 00 00               jns 0x14032b67b
0032B52B  48 85 F6                        test rsi, rsi
0032B52E  75 0D                           jne 0x14032b53d
0032B530  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032B535  49 8B D6                        mov rdx, r14
0032B538  E8 1B A8 6B 00                  call 0x1409e5d58
0032B53D  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0032B542  49 8B D6                        mov rdx, r14
0032B545  E8 6E DC 78 00                  call 0x140ab91b8
0032B54A  8B C7                           mov eax, edi
0032B54C  E9 16 F9 FF FF                  jmp 0x14032ae67
0032B551  45 33 C0                        xor r8d, r8d
0032B554  49 8B CD                        mov rcx, r13
0032B557  E8 B4 CE F1 FF                  call 0x140248410
0032B55C  BA 02 00 00 00                  mov edx, 2
0032B561  4D 8B CE                        mov r9, r14
0032B564  49 8B CD                        mov rcx, r13
0032B567  44 8D 42 FF                     lea r8d, [rdx - 1]
0032B56B  E8 60 B2 F5 FF                  call 0x1402867d0
0032B570  49 8B D6                        mov rdx, r14
0032B573  48 8B CB                        mov rcx, rbx
0032B576  E8 3D DC 78 00                  call 0x140ab91b8
0032B57B  B8 2D 01 00 C0                  mov eax, 0xc000012d
0032B580  E9 E2 F8 FF FF                  jmp 0x14032ae67
0032B585  49 3B C3                        cmp rax, r11
0032B588  E9 49 FE FF FF                  jmp 0x14032b3d6
0032B58D  E8 9E C0 55 00                  call 0x140887630
0032B592  85 C0                           test eax, eax
0032B594  0F 88 CD F8 FF FF               js 0x14032ae67
0032B59A  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0032B59F  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
0032B5A3  E9 60 F5 FF FF                  jmp 0x14032ab08
0032B5A8  E8 83 C0 55 00                  call 0x140887630
0032B5AD  85 C0                           test eax, eax
0032B5AF  0F 88 A8 00 00 00               js 0x14032b65d
0032B5B5  0F B7 8E AE 04 00 00            movzx ecx, word ptr [rsi + 0x4ae]
0032B5BC  48 8B 05 C5 4A B0 00            mov rax, qword ptr [rip + 0xb04ac5]
0032B5C3  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0032B5C7  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
0032B5CB  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0032B5D0  E9 D7 FE FF FF                  jmp 0x14032b4ac
0032B5D5  48 8B F0                        mov rsi, rax
0032B5D8  E9 46 FF FF FF                  jmp 0x14032b523
0032B5DD  49 8B D6                        mov rdx, r14
0032B5E0  48 8B CB                        mov rcx, rbx
0032B5E3  E8 70 A7 6B 00                  call 0x1409e5d58
0032B5E8  E9 74 FA FF FF                  jmp 0x14032b061
0032B5ED  4D 85 FF                        test r15, r15
0032B5F0  0F 84 06 F7 FF FF               je 0x14032acfc
0032B5F6  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0032B5FB  49 8B D7                        mov rdx, r15
0032B5FE  E8 71 5D 1B 00                  call 0x1404e1374
0032B603  33 C0                           xor eax, eax
0032B605  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0032B60A  E9 ED F6 FF FF                  jmp 0x14032acfc
0032B60F  4D 85 FF                        test r15, r15
0032B612  0F 84 C7 F7 FF FF               je 0x14032addf
0032B618  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0032B61D  49 8B D7                        mov rdx, r15
0032B620  E8 4F 5D 1B 00                  call 0x1404e1374
0032B625  E9 B5 F7 FF FF                  jmp 0x14032addf
0032B62A  4D 85 FF                        test r15, r15
0032B62D  0F 84 11 F9 FF FF               je 0x14032af44
0032B633  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0032B638  49 8B D7                        mov rdx, r15
0032B63B  E8 34 5D 1B 00                  call 0x1404e1374
0032B640  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
0032B645  E9 FA F8 FF FF                  jmp 0x14032af44
0032B64A  83 E2 EF                        and edx, 0xffffffef
0032B64D  83 CA 08                        or edx, 8
0032B650  E9 DF F2 FF FF                  jmp 0x14032a934
0032B655  83 E2 E7                        and edx, 0xffffffe7
0032B658  E9 D7 F2 FF FF                  jmp 0x14032a934
0032B65D  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
0032B661  48 8B CE                        mov rcx, rsi
0032B664  E8 4F DB 78 00                  call 0x140ab91b8
0032B669  E9 F9 F7 FF FF                  jmp 0x14032ae67
0032B66E  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0032B673  4D 8B F1                        mov r14, r9
0032B676  E9 8D F4 FF FF                  jmp 0x14032ab08
0032B67B  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
0032B680  E9 7E F4 FF FF                  jmp 0x14032ab03
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCommitExistingVad(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, unsigned __int8 a6, unsigned int a7, unsigned __int8 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m164;
    unsigned int v_stack_m168;
    unsigned int v_stack_m16C;
    unsigned int v_stack_m170;
    unsigned int v_stack_m174;
    unsigned __int16 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B4;
    unsigned __int8 v_stack_m1B8;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p50;
    unsigned int v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (456);
    result = (*(unsigned __int64 *)(v_rip + 11402941)) ^ (v_rsp);
    v_stack_m58 = result;
    v_rsi = 0;
    v_stack_m138 = a10;
    result = 0;
    v_stack_m198 = a1;
    v_stack_mD8 = 0;
    v_stack_m180 = a9;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) & (0x4200000ULL));
    v_stack_m128 = 0;
    v_stack_m16C = 0;
    a1 = 0;
    if (((unsigned int)(result)) == 0x4200000ULL) { a1 = 1; }
    v_stack_m170 = (unsigned int)(a1);
    v_stack_mE8 = v_xmm0;
    result = MiMakeProtectionMask((unsigned int)(a4), 1, (unsigned int)(*(unsigned int *)(a1 + 48)), a4);
    v_stack_m1B4 = (unsigned int)(result);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) >> (7));
    a1 = (unsigned int)((a1) & (31));
    if (((unsigned int)(result)) == 24) goto loc_0032B010;
    if (((unsigned int)(a1)) == 24) goto loc_0032AF78;
loc_0032A915:
    a1 = (unsigned int)((a1) & (24));
    if (condition_is_not_equal) goto loc_0032B184;
loc_0032A91E:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) & (24));
    if (((unsigned int)(result)) == 24) goto loc_0032B655;
    if (((unsigned int)(result)) != 8) goto loc_0032A938;
loc_0032A931:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0xFFFFFFF7ULL));
loc_0032A934:
    v_stack_m1B4 = (unsigned int)(a2);
loc_0032A938:
    v_stack_m120 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m1A0 = 0;
    v_stack_m1B0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    *(unsigned __int16 *)(a11) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11556643) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8)));
    if (condition_is_below) goto loc_0032B159;
    v_stack_m150 = 0;
loc_0032A990:
    v_stack_mF0 = (unsigned int)((unsigned int)(a2));
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) & (31));
    result = (result) << (5);
    if (*(unsigned __int64 *)(v_rip + 11547367) == 0) goto loc_0032A9B6;
    if (((result) & (*(unsigned __int64 *)(v_rip + 11547367))) == 0) goto loc_0032AE92;
    result = (result) | (16);
loc_0032A9B6:
    v_stack_m140 = result;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) & (0x14200000ULL));
    if (((unsigned int)(result)) == 0x10200000ULL) goto loc_0032B247;
loc_0032A9CD:
    a1 = (a2) >> (9);
    a1 = (a1) & (result);
    a1 = (a1) + (v_r11);
    v_r15 = (a2 - 1) + (a3);
    v_stack_m130 = a1;
    v_r15 = (v_r15) | (0xFFFULL);
    a2 = (v_r15) >> (9);
    a2 = (a2) & (v_r11);
    a2 = (a2) + (v_r11);
    v_stack_mA8 = 0;
    v_stack_m110 = a2;
    v_stack_mB0 = v_stack_mB8;
    v_rdi = 0;
    v_stack_m90 = 0;
    v_stack_mB8 = v_stack_mB8;
    v_r11 = (a2) - (a1);
    v_stack_m78 = 0;
    v_r11 = (v_r11) >> (3);
    v_stack_m98 = v_stack_mA0;
    v_r11 = (v_r11) + 1;
    v_stack_m118 = v_r11;
    v_stack_mA0 = v_stack_mA0;
    v_stack_m80 = v_stack_m88;
    v_stack_m88 = v_stack_m88;
    v_stack_m68 = v_stack_m70;
    v_stack_m70 = v_stack_m70;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) & (0xA00000ULL));
    v_stack_m60 = 0;
    v_stack_m1A8 = 0;
    v_stack_m148 = 0;
    if (((unsigned int)(result)) == 0xA00000ULL) goto loc_0032B280;
    if (((a6) & (26)) != 0) goto loc_0032AE8B;
    v_stack_m174 = 3;
    v_stack_m108 = 1;
    result = MiChargeFullProcessCommitment(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_r11, (unsigned int)(*(unsigned int *)(a1 + 48)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184));
    v_stack_m190 = 1;
    if (sign_flag) goto loc_0032B06B;
    v_stack_m188 = v_stack_m118;
    v_stack_m164 = 1;
loc_0032AB03:
loc_0032AB08:
    result = 0;
    v_stack_m168 = 0;
    result = MiVadPureReserve(v_stack_m198, v_stack_m198, (unsigned int)(*(unsigned int *)(a1 + 48)), v_stack_m118);
    if ((unsigned int)(result) == 0) goto loc_0032AB84;
    a3 = 0;
    v_stack_m168 = 1;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m1B0 + 608, a2, a3, v_stack_m118);
    if (!(condition_is_above_or_equal)) {
        a3 = v_stack_m1B0 + 608;
        a2 = result;
        a1 = v_stack_m1B0 + 608;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_m118);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = MiCommitPageTablesForVad(v_stack_m198, a2, v_r15, v_stack_m118);
    if (sign_flag) goto loc_0032B047;
loc_0032AB84:
    a1 = 0;
    v_stack_m158 = 0;
    v_stack_m1A0 = 0;
loc_0032AB9F:
    v_stack_m180 = 0;
    v_stack_m1A8 = 0;
    if (v_stack_m174 == 0) goto loc_0032B1A6;
loc_0032ABB4:
    a1 = (v_stack_m1B0) + (0x400ULL);
    result = MiLockWorkingSetShared(a1, v_stack_m198, v_r15, v_stack_m118);
    v_stack_m1B8 = (unsigned __int8)(result);
loc_0032ABD0:
    if (a1 > v_stack_m110) goto loc_0032ADBC;
    if (0 == 0) goto loc_0032ACE8;
    if (((a1) & (0xFFFULL)) == 0) goto loc_0032ACE8;
loc_0032ABFA:
    if (v_stack_m1A0 == 0) goto loc_0032ADAF;
    v_r15 = (0) + (v_stack_m108);
loc_0032AC09:
    if (a1 < v_r15) goto loc_0032AC48;
    if (a1 > v_r15) goto loc_0032AC48;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (1)) == 0) goto loc_0032AC3E;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0032ACA8;
loc_0032AC3E:
loc_0032AC48:
    v_stack_m160 = *(unsigned __int64 *)(a1);
    if (*(unsigned __int64 *)(a1) != 0) goto loc_0032AEC2;
    result = v_stack_m190 + 0 * 1;
    if (a1 > v_stack_m150) { result = 0; }
    if (v_stack_m190 != 1) goto loc_0032ADA4;
    if (a1 >= (*(unsigned __int64 *)(a1))) goto loc_0032B482;
loc_0032AC7F:
    v_r14 = (unsigned __int16)((0) + ((unsigned __int16)(v_stack_m108)));
loc_0032AC83:
    *(unsigned __int64 *)(a1) = v_stack_m140;
loc_0032AC8A:
    if (0 != 0) goto loc_0032B1DF;
loc_0032AC93:
    v_stack_m130 = v_stack_m130 + v_stack_m190 * 8;
    goto loc_0032ABD0;
loc_0032ACA8:
    result = MiPteHasShadow(v_stack_m190, *(unsigned __int64 *)(a1), *(unsigned __int64 *)(a1), v_stack_m118);
    if (result == 0) goto loc_0032AC3E;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_0032AC3E;
    result = (a1 + v_stack_m108 * 8) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (32)) != 0) {
        a3 = (*(unsigned __int64 *)(a1)) | (32);
    }
    a2 = (a3) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (66)) == 0) { a2 = a3; }
    goto loc_0032AC3E;
loc_0032ACE8:
    if ((unsigned __int16)(v_r14) != 0) goto loc_0032AF9D;
loc_0032ACF2:
    if (v_stack_m170 != 0) goto loc_0032B5ED;
loc_0032ACFC:
    if (((unsigned int)((unsigned int)(v_stack_m1A8))) == 1) goto loc_0032AD3C;
    if (v_stack_m180 != 0) goto loc_0032AFD0;
loc_0032AD14:
    a1 = (a1 + v_stack_m108 * 8) >> (9);
    a1 = (a1) & (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8));
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8));
    v_stack_m180 = a1;
loc_0032AD3C:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m198 + 48))) >> (12));
    a2 = (unsigned int)((a2) & (127));
    result = MiMakeSystemAddressValid(a1 + v_stack_m108 * 8, a2, v_stack_m1B8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1A8))));
    if ((a1 + v_stack_m108 * 8) >= v_stack_m1B8) goto loc_0032AEA7;
loc_0032AD71:
    a1 = (a1 + v_stack_m108 * 8) >> (9);
    a1 = (a1) & (v_stack_m1B8);
    a1 = (a1) + (v_stack_m1B8);
    v_stack_m158 = a1;
loc_0032AD99:
    goto loc_0032ABFA;
loc_0032ADA4:
    goto loc_0032AC8A;
loc_0032ADAF:
    v_stack_m1A0 = a1 + v_stack_m108 * 8;
    goto loc_0032AC09;
loc_0032ADBC:
    result = v_stack_m1B8;
    if ((unsigned __int16)(v_r14) != 0) {
        a2 = v_stack_m158;
        a4 = 2;
        a3 = (unsigned __int16)(v_r14);
        result = MiIncreaseUsedPtes(a1, a2, a3, a4);
    }
    if (v_stack_m170 != 0) goto loc_0032B60F;
loc_0032ADDF:
    if (v_stack_m1A8 == 1) goto loc_0032AFBA;
    result = v_stack_m180;
    if (v_stack_m180 != 0) {
        a2 = v_stack_m180;
        a1 = v_stack_m1B0 + 1024;
        result = MiUnlockPageTable(a1, a2, a3, a4);
    }
    result = MiUnlockWorkingSetShared(v_stack_m1B0 + 1024, v_stack_m1B8, a3, a4);
loc_0032AE18:
    if (v_stack_m168 != 0) {
        a1 = v_stack_m120;
        a2 = v_stack_m1B0;
        result = UNLOCK_PAGE_TABLE_COMMITMENT(a1, a2, a3, a4);
    }
    if (v_stack_m164 == 0) goto loc_0032AE40;
    if (result != 0) goto loc_0032AE9A;
loc_0032AE35:
    result = (v_stack_m118) - (result);
    v_stack_m188 = result;
loc_0032AE40:
    a2 = (*(unsigned __int8 *)(v_stack_m198 + 34)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(v_stack_m198 + 52)));
    a2 = (a2) + (v_stack_m188);
    *(unsigned int *)(v_stack_m198 + 52) = (unsigned int)(a2);
    a2 = (a2) >> (32);
    *(unsigned __int8 *)(v_stack_m198 + 34) = (unsigned __int8)(a2);
    result = 0;
loc_0032AE67:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m198, a4);
    v_rsp = (v_rsp) + (456);
    return result;
loc_0032AE8B:
    goto loc_0032AE67;
loc_0032AE92:
    result = ((unsigned int)(0xC000000DULL)) | (a2);
    goto loc_0032A9B6;
loc_0032AE9A:
    result = MiReturnFullProcessCommitment(v_stack_m1B0, result, v_stack_m198, a4);
    goto loc_0032AE35;
loc_0032AEA7:
    if (v_stack_m1B0 <= result) goto loc_0032AD99;
    goto loc_0032AD71;
loc_0032AEC2:
    result = MiIsPteDecommittedPage(result, result, v_stack_m198, a4);
    if ((unsigned int)(result) != 0) goto loc_0032B10B;
    v_rsi = (result) + (v_stack_p78);
    if ((*(unsigned int *)(v_stack_m138)) != 0) goto loc_0032AC8A;
    result = 0;
    v_stack_m178 = 0;
    v_stack_p20 = v_stack_m178;
    result = MiGetPageProtection(v_stack_p70, v_stack_m1B0, v_stack_m128, v_stack_m16C);
    if (v_stack_m128 == 0) goto loc_0032AFEB;
    if ((unsigned __int16)(v_r14) == 0) goto loc_0032B278;
    result = MiIncreaseUsedPtes(v_stack_p70, v_stack_m158, (unsigned __int16)(v_r14), 2);
    v_r12 = 0;
loc_0032AF3A:
    if (v_stack_m170 != 0) goto loc_0032B62A;
loc_0032AF44:
    if (v_stack_p60 != 1) goto loc_0032B01A;
    a1 = (v_stack_p58) + (0x400ULL);
    result = MiUnlockWorkingSetExclusive(a1, v_stack_p50, (unsigned __int16)(v_r14), 2);
loc_0032AF65:
    a1 = 0;
    goto loc_0032AB9F;
loc_0032AF78:
    if (condition_is_below) goto loc_0032A91E;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1B0 + 72) + 32))) >> (1));
    a1 = (unsigned int)((a1) & (31));
    if (((unsigned int)(a1)) == 24) goto loc_0032A91E;
    goto loc_0032A915;
loc_0032AF9D:
    result = MiIncreaseUsedPtes(a1, v_stack_m158, 0, 2);
    result = 0;
    goto loc_0032ACF2;
loc_0032AFBA:
    result = MiUnlockWorkingSetExclusive(v_stack_m1B0 + 1024, v_stack_p50, 0, 2);
    goto loc_0032AE18;
loc_0032AFD0:
    a1 = (v_stack_p58) + (0x400ULL);
    result = MiUnlockPageTable(a1, v_stack_p50, 0, 2);
    goto loc_0032AD14;
loc_0032AFEB:
    if (v_stack_p54 != ((unsigned int)(result))) goto loc_0032AFFC;
    result = (unsigned int)(a5);
    if (v_stack_m16C != ((unsigned int)((unsigned int)(a5)))) {
        result = v_stack_m138;
        *(unsigned int *)(result) = 1;
    }
    goto loc_0032AC8A;
loc_0032B010:
    goto loc_0032A934;
loc_0032B01A:
    result = MiUnlockPageTable(v_stack_p58 + 1024, v_stack_m180, (unsigned int)(v_stack_p60), 2);
    result = MiUnlockWorkingSetShared(v_stack_p58 + 1024, v_stack_p50, (unsigned int)(v_stack_p60), 2);
    goto loc_0032AF65;
loc_0032B047:
    result = UNLOCK_PAGE_TABLE_COMMITMENT(v_stack_m120, v_stack_p58, (unsigned int)(v_stack_p60), 2);
    if (0 != 0) goto loc_0032B36B;
loc_0032B061:
    goto loc_0032AE67;
loc_0032B06B:
loc_0032B077:
    result = 0;
    v_stack_m164 = 0;
    result = MiLockWorkingSetShared(v_stack_p58 + 1024, v_stack_p58, (unsigned int)(v_stack_p60), v_stack_p58);
    a2 = v_stack_m148;
    if (v_stack_m108 == 0) { a2 = 0; }
    v_stack_p30 = a2;
    a1 = (v_stack_p58) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = MiComputePageCommitment(a1, v_stack_m108, v_stack_p70, (unsigned __int8)((unsigned __int8)(result)));
    result = MiUnlockWorkingSetShared(v_stack_p58 + 1024, (unsigned __int8)((unsigned __int8)(result)), v_stack_p70, (unsigned __int8)((unsigned __int8)(result)));
    a4 = (v_stack_m118) - (result);
    v_stack_m188 = a4;
    if (v_stack_p78 == 1) goto loc_0032B303;
    if (v_stack_m148 != 0) goto loc_0032B303;
    goto loc_0032AE67;
loc_0032B10B:
    if (v_stack_p78 != 1) goto loc_0032B1DF;
    a1 = (v_stack_mF0) << (5);
    result = (a1) ^ (v_stack_p78);
    result = (result) & (-993);
    result = (result) ^ (a1);
    v_stack_m160 = result;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p70 + 48))) & (0x14200000ULL));
    if (((unsigned int)(a1)) == 0x10200000ULL) goto loc_0032B3B0;
loc_0032B14C:
    *(unsigned __int64 *)(v_stack_p58) = result;
    goto loc_0032AC8A;
loc_0032B159:
    a1 = (*(unsigned __int8 *)(v_stack_p58 + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(v_stack_p58 + 28)));
    a1 = (a1) & ((unsigned int)(*(unsigned int *)(v_stack_p58 + 28)));
    v_stack_m150 = v_r11 + a1 * 8;
    goto loc_0032A990;
loc_0032B184:
    if (((unsigned int)(a1)) == 16) goto loc_0032A931;
    if (((unsigned int)(a1)) == 8) goto loc_0032B64A;
    if (((unsigned int)(a1)) != 24) goto loc_0032A938;
    a2 = (unsigned int)((v_stack_p78) | ((unsigned int)(a1)));
    goto loc_0032A934;
loc_0032B1A6:
    result = MiComputePreferredNode(v_stack_p58 + 1024, a2, v_stack_p70, v_stack_p58);
    v_stack_p60 = 1;
    result = MiLockWorkingSetForLargeMapping(v_stack_p58 + 1024, a2, (unsigned int)((unsigned int)(result)), v_stack_p58);
    v_stack_p50 = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) == 17) goto loc_0032ABB4;
    goto loc_0032ABD0;
loc_0032B1DF:
    result = MiPopLargePfnList(v_stack_mB8, (unsigned int)(v_stack_m174), (unsigned int)((unsigned int)(result)), v_stack_p58);
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    v_stack_m100 = a1;
    v_stack_mF8 = a1;
    *(unsigned __int64 *)(a1) = v_stack_m100;
    *(unsigned __int64 *)(a1 + 8) = v_stack_m100;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p54));
    result = MiInsertLargeUserMapping(v_stack_p70, v_stack_m130, v_stack_m100, (unsigned int)(v_stack_m174));
    result = 0;
    goto loc_0032AC93;
loc_0032B247:
    result = MI_READ_PTE_LOCK_FREE(v_stack_m140, v_stack_m130, v_stack_m100, (unsigned int)(v_stack_m174));
    *(unsigned __int64 *)(v_stack_m140) = result;
    goto loc_0032A9CD;
loc_0032B278:
    v_r12 = 0;
    goto loc_0032AF3A;
loc_0032B280:
    a3 = ((unsigned int)(*(unsigned int *)(v_stack_p58 + 48))) >> (19);
    a3 = (unsigned int)((a3) & (3));
    v_stack_p78 = *(unsigned __int64 *)(v_rip - 3322507 + a3 * 8 + 83320);
    result = 1;
    if ((*(unsigned __int64 *)(v_rip - 3322507 + a3 * 8 + 83320)) == 16) { result = 16; }
    v_stack_m174 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 3322507 + a3 * 4 + 81680)));
    v_stack_m108 = result;
    result = (unsigned int)((a6) & (26));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 3322507 + a3 * 4 + 81680)))) <= 1) goto loc_0032B3CC;
    if (result != 2) goto loc_0032AE8B;
loc_0032B2DC:
    if (v_stack_m180 == 1) goto loc_0032B438;
    if (v_stack_m180 == 0) goto loc_0032B463;
    v_stack_p60 = v_stack_m180;
loc_0032B2F7:
loc_0032B2FA:
    v_stack_m148 = v_stack_m180;
    goto loc_0032B077;
loc_0032B303:
    if (v_stack_p58 == 0) goto loc_0032B66E;
    if (v_stack_m130 == 1) goto loc_0032B58D;
    result = MiChargeProcessPhysicalPages(v_stack_m180, v_stack_p58, (unsigned int)(*(unsigned int *)(v_rip - 3322507 + a3 * 4 + 81680)), v_stack_p58);
    if ((unsigned int)(result) == 0) goto loc_0032B061;
    if (v_stack_p60 == 0) goto loc_0032B5A8;
    if (v_stack_p60 == v_stack_m180) goto loc_0032B49D;
    result = PsReferencePartitionSafe(v_stack_p60, v_stack_p58, (unsigned int)(*(unsigned int *)(v_rip - 3322507 + a3 * 4 + 81680)), v_stack_p58);
    if ((unsigned __int8)(result) != 0) goto loc_0032B49D;
    result = MiReturnProcessPhysicalPages(v_stack_p58, v_stack_p58, (unsigned int)(*(unsigned int *)(v_rip - 3322507 + a3 * 4 + 81680)), v_stack_p58);
    goto loc_0032AE67;
loc_0032B36B:
    if (v_stack_p78 == 1) goto loc_0032B5DD;
    result = MiFreeLargeZeroPages(v_rip - 3322507, v_stack_mB8, 1, v_stack_p58);
    result = MiReturnResident(v_rip - 3322507, 0, 1, v_stack_p58);
    if (v_stack_p60 != 0) goto loc_0032B551;
    result = MiReturnFullProcessCommitment(v_stack_p58, 0, 1, v_stack_p58);
    goto loc_0032B570;
loc_0032B3B0:
    result = MI_READ_PTE_LOCK_FREE(v_stack_m160, 0, 1, v_stack_p58);
    result = (result) | (0x4000000ULL);
    v_stack_m160 = result;
    goto loc_0032B14C;
loc_0032B3CC:
    if (condition_is_not_equal) goto loc_0032B585;
loc_0032B3D6:
    if (v_stack_m160 != 8) goto loc_0032AE8B;
    a1 = (unsigned int)((2) - (1));
loc_0032B3FC:
    v_rbx = (v_stack_p58) >> (9);
    v_rbx = (v_rbx) & (v_stack_p60);
    a2 = (0) >> (9);
    v_rbx = (v_rbx) + (v_stack_m180);
    a2 = (a2) & (v_stack_p60);
    a3 = (v_stack_m150) >> (9);
    a2 = (a2) + (v_stack_m180);
    a3 = (a3) & (v_stack_p60);
    a3 = (a3) + (v_stack_m180);
    a1 = (a1) - (1);
    if (condition_is_not_equal) goto loc_0032B3FC;
    v_stack_m150 = a3;
    v_rdi = 0;
    v_stack_m110 = a2;
    goto loc_0032B2DC;
loc_0032B438:
    result = MiLocateLockedVadEvent(v_stack_p70, 16, a3, v_stack_p58);
    if (result == 0) goto loc_0032B45E;
    v_stack_p60 = *(unsigned __int64 *)(result + 24);
    if (*(unsigned __int64 *)(result + 24) != 0) goto loc_0032B2F7;
    goto loc_0032B463;
loc_0032B45E:
    v_stack_p60 = 0;
loc_0032B463:
    goto loc_0032B2FA;
loc_0032B482:
    if (v_rbx > (*(unsigned __int64 *)(v_rip + 11553814))) goto loc_0032AC7F;
    goto loc_0032AC83;
loc_0032B49D:
    v_stack_p68 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11553814) + *(unsigned __int16 *)(v_stack_p58 + 1198) * 8) + 184));
    *(unsigned __int16 *)(0) = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11553814) + *(unsigned __int16 *)(v_stack_p58 + 1198) * 8) + 184))));
loc_0032B4AC:
    result = MiGetVadLargePageMinimumIndex(v_stack_p70, 16, a3, v_stack_p58);
    v_stack_mE8 = v_stack_p70;
    v_stack_p40 = v_stack_mB8;
    result = 0;
    v_stack_p38 = 0;
    v_stack_p30 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11553814) + *(unsigned __int16 *)(v_stack_p58 + 1198) * 8) + 184);
    v_stack_p28 = a8;
    v_stack_p20 = (unsigned int)((unsigned int)(a7));
    result = MiCreateLargePfnList(v_stack_mE8, 0, v_stack_m188, *(unsigned __int64 *)(v_rip - 3322507 + (unsigned int)((unsigned int)(result)) * 8 + 72800));
    if (v_stack_p60 == 0) goto loc_0032B5D5;
    result = v_stack_p60;
    if (v_stack_p60 != (*(unsigned __int64 *)(result + 24))) {
        a1 = v_stack_p60;
        result = PsDereferencePartition(a1, 0, v_stack_m188, *(unsigned __int64 *)(v_rip - 3322507 + (unsigned int)((unsigned int)(result)) * 8 + 72800));
    }
    if (!sign_flag) goto loc_0032B67B;
    if (v_stack_p60 == 0) {
        a1 = v_stack_p58;
        a2 = v_stack_m188;
        result = MiReturnFullProcessCommitment(a1, a2, v_stack_m188, *(unsigned __int64 *)(v_rip - 3322507 + (unsigned int)((unsigned int)(result)) * 8 + 72800));
    }
    result = MiReturnProcessPhysicalPages(v_stack_p58, v_stack_m188, v_stack_m188, *(unsigned __int64 *)(v_rip - 3322507 + (unsigned int)((unsigned int)(result)) * 8 + 72800));
    goto loc_0032AE67;
loc_0032B551:
    a3 = 0;
    result = MiReturnCommit(v_rip - 3322507, v_stack_m188, a3, *(unsigned __int64 *)(v_rip - 3322507 + (unsigned int)((unsigned int)(result)) * 8 + 72800));
    result = MiReturnCrossPartitionCharges(v_rip - 3322507, 2, 2 - 1, v_stack_m188);
loc_0032B570:
    result = MiReturnProcessPhysicalPages(v_rbx, v_stack_m188, 2 - 1, v_stack_m188);
    goto loc_0032AE67;
loc_0032B585:
    goto loc_0032B3D6;
loc_0032B58D:
    result = MiChargeFullProcessCommitment(v_rbx, v_stack_m188, 2 - 1, v_stack_m188);
    if (sign_flag) goto loc_0032AE67;
    goto loc_0032AB08;
loc_0032B5A8:
    result = MiChargeFullProcessCommitment(v_rbx, v_stack_m188, 2 - 1, v_stack_m188);
    if (sign_flag) goto loc_0032B65D;
    v_stack_p68 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11553477) + *(unsigned __int16 *)(v_stack_p60 + 1198) * 8);
    goto loc_0032B4AC;
loc_0032B5D5:
    goto loc_0032B523;
loc_0032B5DD:
    result = MiReturnFullProcessCommitment(v_rbx, v_stack_m188, 2 - 1, v_stack_m188);
    goto loc_0032B061;
loc_0032B5ED:
    if (v_stack_m108 == 0) goto loc_0032ACFC;
    result = MiFlushGraphicsPtes(v_stack_p68, v_stack_m108, 2 - 1, v_stack_m188);
    result = 0;
    v_stack_p68 = 0;
    goto loc_0032ACFC;
loc_0032B60F:
    if (v_stack_m108 == 0) goto loc_0032ADDF;
    result = MiFlushGraphicsPtes(v_stack_p68, v_stack_m108, 2 - 1, v_stack_m188);
    goto loc_0032ADDF;
loc_0032B62A:
    if (v_stack_m108 == 0) goto loc_0032AF44;
    result = MiFlushGraphicsPtes(v_stack_p68, v_stack_m108, 2 - 1, v_stack_m188);
    v_stack_p68 = 0;
    goto loc_0032AF44;
loc_0032B64A:
    a2 = (unsigned int)((v_stack_m108) & (0xFFFFFFEFULL));
    a2 = (unsigned int)((a2) | (8));
    goto loc_0032A934;
loc_0032B655:
    a2 = (unsigned int)((a2) & (0xFFFFFFE7ULL));
    goto loc_0032A934;
loc_0032B65D:
    result = MiReturnProcessPhysicalPages(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11553477) + *(unsigned __int16 *)(v_stack_p60 + 1198) * 8), v_stack_m188, 2 - 1, v_stack_m188);
    goto loc_0032AE67;
loc_0032B66E:
    goto loc_0032AB08;
loc_0032B67B:
    goto loc_0032AB03;
}
```

## 5. (Beta) C Style

```c
int64_t MiCommitExistingVad(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, uint8_t Arg6, uint32_t Arg7, uint8_t Arg8, int64_t Arg9, int64_t Arg10, void *Arg11)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg11 = (uint8_t *)Arg11;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m164;
    uint32_t v_stack_m168;
    uint32_t v_stack_m16C;
    uint32_t v_stack_m170;
    uint32_t v_stack_m174;
    uint16_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B4;
    uint8_t v_stack_m1B8;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p50;
    uint32_t v_stack_p54;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (456);
    result = (*(uint64_t *)(v_rip + 0xADFEBD)) ^ (local_rsp);
    v_stack_m58 = result;
    local_rsi = 0;
    v_stack_m138 = Arg10;
    result = 0;
    v_stack_m198 = Arg1;
    v_stack_mD8 = 0;
    v_stack_m180 = Arg9;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) & (0x4200000ULL));
    v_stack_m128 = 0;
    v_stack_m16C = 0;
    Arg1 = 0;
    if (((uint32_t)(result)) == 0x4200000ULL) { Arg1 = 1; }
    v_stack_m170 = (uint32_t)(Arg1);
    v_stack_mE8 = v_xmm0;
    result = MiMakeProtectionMask((uint32_t)(Arg4), 1, (uint32_t)(*(uint32_t *)(arg1 + 0x30)), Arg4);
    v_stack_m1B4 = (uint32_t)(result);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) >> (7));
    Arg1 = (uint32_t)((Arg1) & (31));
    if (((uint32_t)(result)) == 24) goto loc_0032B010;
    if (((uint32_t)(Arg1)) == 24) goto loc_0032AF78;
loc_0032A915:
    Arg1 = (uint32_t)((Arg1) & (24));
    if (condition_is_not_equal) goto loc_0032B184;
loc_0032A91E:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) & (24));
    if (((uint32_t)(result)) == 24) goto loc_0032B655;
    if (((uint32_t)(result)) != 8) goto loc_0032A938;
loc_0032A931:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0xFFFFFFF7ULL));
loc_0032A934:
    v_stack_m1B4 = (uint32_t)(Arg2);
loc_0032A938:
    v_stack_m120 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m1A0 = 0;
    v_stack_m1B0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    *(uint16_t *)(arg11) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB05723) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8)));
    if (condition_is_below) goto loc_0032B159;
    v_stack_m150 = 0;
loc_0032A990:
    v_stack_mF0 = (uint32_t)((uint32_t)(Arg2));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) & (31));
    result = (result) << (5);
    if (*(uint64_t *)(v_rip + 0xB032E7) == 0) goto loc_0032A9B6;
    if (((result) & (*(uint64_t *)(v_rip + 0xB032E7))) == 0) goto loc_0032AE92;
    result = (result) | (16);
loc_0032A9B6:
    v_stack_m140 = result;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) & (0x14200000ULL));
    if (((uint32_t)(result)) == 0x10200000ULL) goto loc_0032B247;
loc_0032A9CD:
    Arg1 = (Arg2) >> (9);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) + (local_r11);
    local_r15 = (Arg2 - 1) + (Arg3);
    v_stack_m130 = Arg1;
    local_r15 = (local_r15) | (0xFFFULL);
    Arg2 = (local_r15) >> (9);
    Arg2 = (Arg2) & (local_r11);
    Arg2 = (Arg2) + (local_r11);
    v_stack_mA8 = 0;
    v_stack_m110 = Arg2;
    v_stack_mB0 = v_stack_mB8;
    local_rdi = 0;
    v_stack_m90 = 0;
    v_stack_mB8 = v_stack_mB8;
    local_r11 = (Arg2) - (Arg1);
    v_stack_m78 = 0;
    local_r11 = (local_r11) >> (3);
    v_stack_m98 = v_stack_mA0;
    local_r11 = (local_r11) + 1;
    v_stack_m118 = local_r11;
    v_stack_mA0 = v_stack_mA0;
    v_stack_m80 = v_stack_m88;
    v_stack_m88 = v_stack_m88;
    v_stack_m68 = v_stack_m70;
    v_stack_m70 = v_stack_m70;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) & (0xA00000ULL));
    v_stack_m60 = 0;
    v_stack_m1A8 = 0;
    v_stack_m148 = 0;
    if (((uint32_t)(result)) == 0xA00000ULL) goto loc_0032B280;
    if (((Arg6) & (26)) != 0) goto loc_0032AE8B;
    v_stack_m174 = 3;
    v_stack_m108 = 1;
    result = MiChargeFullProcessCommitment(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), local_r11, (uint32_t)(*(uint32_t *)(arg1 + 0x30)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8));
    v_stack_m190 = 1;
    if (sign_flag) goto loc_0032B06B;
    v_stack_m188 = v_stack_m118;
    v_stack_m164 = 1;
loc_0032AB03:
loc_0032AB08:
    result = 0;
    v_stack_m168 = 0;
    result = MiVadPureReserve(v_stack_m198, v_stack_m198, (uint32_t)(*(uint32_t *)(arg1 + 0x30)), v_stack_m118);
    if ((uint32_t)(result) == 0) goto loc_0032AB84;
    Arg3 = 0;
    v_stack_m168 = 1;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m1B0 + 608, Arg2, Arg3, v_stack_m118);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_stack_m1B0 + 608;
        Arg2 = result;
        Arg1 = v_stack_m1B0 + 608;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_m118);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = MiCommitPageTablesForVad(v_stack_m198, Arg2, local_r15, v_stack_m118);
    if (sign_flag) goto loc_0032B047;
loc_0032AB84:
    Arg1 = 0;
    v_stack_m158 = 0;
    v_stack_m1A0 = 0;
loc_0032AB9F:
    v_stack_m180 = 0;
    v_stack_m1A8 = 0;
    if (v_stack_m174 == 0) goto loc_0032B1A6;
loc_0032ABB4:
    Arg1 = (v_stack_m1B0) + (0x400ULL);
    result = MiLockWorkingSetShared(Arg1, v_stack_m198, local_r15, v_stack_m118);
    v_stack_m1B8 = (uint8_t)(result);
loc_0032ABD0:
    if (Arg1 > v_stack_m110) goto loc_0032ADBC;
    if (0 == 0) goto loc_0032ACE8;
    if (((Arg1) & (0xFFFULL)) == 0) goto loc_0032ACE8;
loc_0032ABFA:
    if (v_stack_m1A0 == 0) goto loc_0032ADAF;
    local_r15 = (0) + (v_stack_m108);
loc_0032AC09:
    if (Arg1 < local_r15) goto loc_0032AC48;
    if (Arg1 > local_r15) goto loc_0032AC48;
    if ((((uint8_t)(*(uint64_t *)(arg1))) & (1)) == 0) goto loc_0032AC3E;
    Arg1 = ((((uint8_t)(*(uint64_t *)(arg1))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(arg1))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0032ACA8;
loc_0032AC3E:
loc_0032AC48:
    v_stack_m160 = *(uint64_t *)(arg1);
    if (*(uint64_t *)(arg1) != 0) goto loc_0032AEC2;
    result = v_stack_m190 + 0 * 1;
    if (Arg1 > v_stack_m150) { result = 0; }
    if (v_stack_m190 != 1) goto loc_0032ADA4;
    if (Arg1 >= (*(uint64_t *)(arg1))) goto loc_0032B482;
loc_0032AC7F:
    local_r14 = (uint16_t)((0) + ((uint16_t)(v_stack_m108)));
loc_0032AC83:
    *(uint64_t *)(arg1) = v_stack_m140;
loc_0032AC8A:
    if (0 != 0) goto loc_0032B1DF;
loc_0032AC93:
    v_stack_m130 = v_stack_m130 + v_stack_m190 * 8;
    goto loc_0032ABD0;
loc_0032ACA8:
    result = MiPteHasShadow(v_stack_m190, *(uint64_t *)(arg1), *(uint64_t *)(arg1), v_stack_m118);
    if (result == 0) goto loc_0032AC3E;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_0032AC3E;
    result = (Arg1 + v_stack_m108 * 8) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (32)) != 0) {
        Arg3 = (*(uint64_t *)(arg1)) | (32);
    }
    Arg2 = (Arg3) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (66)) == 0) { Arg2 = Arg3; }
    goto loc_0032AC3E;
loc_0032ACE8:
    if ((uint16_t)(local_r14) != 0) goto loc_0032AF9D;
loc_0032ACF2:
    if (v_stack_m170 != 0) goto loc_0032B5ED;
loc_0032ACFC:
    if (((uint32_t)((uint32_t)(v_stack_m1A8))) == 1) goto loc_0032AD3C;
    if (v_stack_m180 != 0) goto loc_0032AFD0;
loc_0032AD14:
    Arg1 = (Arg1 + v_stack_m108 * 8) >> (9);
    Arg1 = (Arg1) & (*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8));
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8));
    v_stack_m180 = Arg1;
loc_0032AD3C:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m198 + 0x30))) >> (12));
    Arg2 = (uint32_t)((Arg2) & (127));
    result = MiMakeSystemAddressValid(Arg1 + v_stack_m108 * 8, Arg2, v_stack_m1B8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1A8))));
    if ((Arg1 + v_stack_m108 * 8) >= v_stack_m1B8) goto loc_0032AEA7;
loc_0032AD71:
    Arg1 = (Arg1 + v_stack_m108 * 8) >> (9);
    Arg1 = (Arg1) & (v_stack_m1B8);
    Arg1 = (Arg1) + (v_stack_m1B8);
    v_stack_m158 = Arg1;
loc_0032AD99:
    goto loc_0032ABFA;
loc_0032ADA4:
    goto loc_0032AC8A;
loc_0032ADAF:
    v_stack_m1A0 = Arg1 + v_stack_m108 * 8;
    goto loc_0032AC09;
loc_0032ADBC:
    result = v_stack_m1B8;
    if ((uint16_t)(local_r14) != 0) {
        Arg2 = v_stack_m158;
        Arg4 = 2;
        Arg3 = (uint16_t)(local_r14);
        result = MiIncreaseUsedPtes(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m170 != 0) goto loc_0032B60F;
loc_0032ADDF:
    if (v_stack_m1A8 == 1) goto loc_0032AFBA;
    result = v_stack_m180;
    if (v_stack_m180 != 0) {
        Arg2 = v_stack_m180;
        Arg1 = v_stack_m1B0 + 1024;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiUnlockWorkingSetShared(v_stack_m1B0 + 1024, v_stack_m1B8, Arg3, Arg4);
loc_0032AE18:
    if (v_stack_m168 != 0) {
        Arg1 = v_stack_m120;
        Arg2 = v_stack_m1B0;
        result = UNLOCK_PAGE_TABLE_COMMITMENT(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m164 == 0) goto loc_0032AE40;
    if (result != 0) goto loc_0032AE9A;
loc_0032AE35:
    result = (v_stack_m118) - (result);
    v_stack_m188 = result;
loc_0032AE40:
    Arg2 = (*(uint8_t *)(v_stack_m198 + 0x22)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(v_stack_m198 + 0x34)));
    Arg2 = (Arg2) + (v_stack_m188);
    *(uint32_t *)(v_stack_m198 + 0x34) = (uint32_t)(Arg2);
    Arg2 = (Arg2) >> (32);
    *(uint8_t *)(v_stack_m198 + 0x22) = (uint8_t)(Arg2);
    result = 0;
loc_0032AE67:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m198, Arg4);
    local_rsp = (local_rsp) + (456);
    return result;
loc_0032AE8B:
    goto loc_0032AE67;
loc_0032AE92:
    result = ((uint32_t)(0xC000000DULL)) | (Arg2);
    goto loc_0032A9B6;
loc_0032AE9A:
    result = MiReturnFullProcessCommitment(v_stack_m1B0, result, v_stack_m198, Arg4);
    goto loc_0032AE35;
loc_0032AEA7:
    if (v_stack_m1B0 <= result) goto loc_0032AD99;
    goto loc_0032AD71;
loc_0032AEC2:
    result = MiIsPteDecommittedPage(result, result, v_stack_m198, Arg4);
    if ((uint32_t)(result) != 0) goto loc_0032B10B;
    local_rsi = (result) + (v_stack_p78);
    if ((*(uint32_t *)(v_stack_m138)) != 0) goto loc_0032AC8A;
    result = 0;
    v_stack_m178 = 0;
    v_stack_p20 = v_stack_m178;
    result = MiGetPageProtection(v_stack_p70, v_stack_m1B0, v_stack_m128, v_stack_m16C);
    if (v_stack_m128 == 0) goto loc_0032AFEB;
    if ((uint16_t)(local_r14) == 0) goto loc_0032B278;
    result = MiIncreaseUsedPtes(v_stack_p70, v_stack_m158, (uint16_t)(local_r14), 2);
    local_r12 = 0;
loc_0032AF3A:
    if (v_stack_m170 != 0) goto loc_0032B62A;
loc_0032AF44:
    if (v_stack_p60 != 1) goto loc_0032B01A;
    Arg1 = (v_stack_p58) + (0x400ULL);
    result = MiUnlockWorkingSetExclusive(Arg1, v_stack_p50, (uint16_t)(local_r14), 2);
loc_0032AF65:
    Arg1 = 0;
    goto loc_0032AB9F;
loc_0032AF78:
    if (condition_is_below) goto loc_0032A91E;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1B0 + 0x48) + 0x20))) >> (1));
    Arg1 = (uint32_t)((Arg1) & (31));
    if (((uint32_t)(Arg1)) == 24) goto loc_0032A91E;
    goto loc_0032A915;
loc_0032AF9D:
    result = MiIncreaseUsedPtes(Arg1, v_stack_m158, 0, 2);
    result = 0;
    goto loc_0032ACF2;
loc_0032AFBA:
    result = MiUnlockWorkingSetExclusive(v_stack_m1B0 + 1024, v_stack_p50, 0, 2);
    goto loc_0032AE18;
loc_0032AFD0:
    Arg1 = (v_stack_p58) + (0x400ULL);
    result = MiUnlockPageTable(Arg1, v_stack_p50, 0, 2);
    goto loc_0032AD14;
loc_0032AFEB:
    if (v_stack_p54 != ((uint32_t)(result))) goto loc_0032AFFC;
    result = (uint32_t)(Arg5);
    if (v_stack_m16C != ((uint32_t)((uint32_t)(Arg5)))) {
        result = v_stack_m138;
        *(uint32_t *)(result) = 1;
    }
    goto loc_0032AC8A;
loc_0032B010:
    goto loc_0032A934;
loc_0032B01A:
    result = MiUnlockPageTable(v_stack_p58 + 1024, v_stack_m180, (uint32_t)(v_stack_p60), 2);
    result = MiUnlockWorkingSetShared(v_stack_p58 + 1024, v_stack_p50, (uint32_t)(v_stack_p60), 2);
    goto loc_0032AF65;
loc_0032B047:
    result = UNLOCK_PAGE_TABLE_COMMITMENT(v_stack_m120, v_stack_p58, (uint32_t)(v_stack_p60), 2);
    if (0 != 0) goto loc_0032B36B;
loc_0032B061:
    goto loc_0032AE67;
loc_0032B06B:
loc_0032B077:
    result = 0;
    v_stack_m164 = 0;
    result = MiLockWorkingSetShared(v_stack_p58 + 1024, v_stack_p58, (uint32_t)(v_stack_p60), v_stack_p58);
    Arg2 = v_stack_m148;
    if (v_stack_m108 == 0) { Arg2 = 0; }
    v_stack_p30 = Arg2;
    Arg1 = (v_stack_p58) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = MiComputePageCommitment(Arg1, v_stack_m108, v_stack_p70, (uint8_t)((uint8_t)(result)));
    result = MiUnlockWorkingSetShared(v_stack_p58 + 1024, (uint8_t)((uint8_t)(result)), v_stack_p70, (uint8_t)((uint8_t)(result)));
    Arg4 = (v_stack_m118) - (result);
    v_stack_m188 = Arg4;
    if (v_stack_p78 == 1) goto loc_0032B303;
    if (v_stack_m148 != 0) goto loc_0032B303;
    goto loc_0032AE67;
loc_0032B10B:
    if (v_stack_p78 != 1) goto loc_0032B1DF;
    Arg1 = (v_stack_mF0) << (5);
    result = (Arg1) ^ (v_stack_p78);
    result = (result) & (-993);
    result = (result) ^ (Arg1);
    v_stack_m160 = result;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p70 + 0x30))) & (0x14200000ULL));
    if (((uint32_t)(Arg1)) == 0x10200000ULL) goto loc_0032B3B0;
loc_0032B14C:
    *(uint64_t *)(v_stack_p58) = result;
    goto loc_0032AC8A;
loc_0032B159:
    Arg1 = (*(uint8_t *)(v_stack_p58 + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x1C)));
    Arg1 = (Arg1) & ((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x1C)));
    v_stack_m150 = local_r11 + Arg1 * 8;
    goto loc_0032A990;
loc_0032B184:
    if (((uint32_t)(Arg1)) == 16) goto loc_0032A931;
    if (((uint32_t)(Arg1)) == 8) goto loc_0032B64A;
    if (((uint32_t)(Arg1)) != 24) goto loc_0032A938;
    Arg2 = (uint32_t)((v_stack_p78) | ((uint32_t)(Arg1)));
    goto loc_0032A934;
loc_0032B1A6:
    result = MiComputePreferredNode(v_stack_p58 + 1024, Arg2, v_stack_p70, v_stack_p58);
    v_stack_p60 = 1;
    result = MiLockWorkingSetForLargeMapping(v_stack_p58 + 1024, Arg2, (uint32_t)((uint32_t)(result)), v_stack_p58);
    v_stack_p50 = (uint8_t)(result);
    if (((uint8_t)(result)) == 17) goto loc_0032ABB4;
    goto loc_0032ABD0;
loc_0032B1DF:
    result = MiPopLargePfnList(v_stack_mB8, (uint32_t)(v_stack_m174), (uint32_t)((uint32_t)(result)), v_stack_p58);
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    v_stack_m100 = Arg1;
    v_stack_mF8 = Arg1;
    *(uint64_t *)(arg1) = v_stack_m100;
    *(uint64_t *)(arg1 + 0x8) = v_stack_m100;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p54));
    result = MiInsertLargeUserMapping(v_stack_p70, v_stack_m130, v_stack_m100, (uint32_t)(v_stack_m174));
    result = 0;
    goto loc_0032AC93;
loc_0032B247:
    result = MI_READ_PTE_LOCK_FREE(v_stack_m140, v_stack_m130, v_stack_m100, (uint32_t)(v_stack_m174));
    *(uint64_t *)(v_stack_m140) = result;
    goto loc_0032A9CD;
loc_0032B278:
    local_r12 = 0;
    goto loc_0032AF3A;
loc_0032B280:
    Arg3 = ((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x30))) >> (19);
    Arg3 = (uint32_t)((Arg3) & (3));
    v_stack_p78 = *(uint64_t *)(v_rip - 0x32B28B + Arg3 * 8 + 0x14578);
    result = 1;
    if ((*(uint64_t *)(v_rip - 0x32B28B + Arg3 * 8 + 0x14578)) == 16) { result = 16; }
    v_stack_m174 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x32B28B + Arg3 * 4 + 0x13F10)));
    v_stack_m108 = result;
    result = (uint32_t)((Arg6) & (26));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x32B28B + Arg3 * 4 + 0x13F10)))) <= 1) goto loc_0032B3CC;
    if (result != 2) goto loc_0032AE8B;
loc_0032B2DC:
    if (v_stack_m180 == 1) goto loc_0032B438;
    if (v_stack_m180 == 0) goto loc_0032B463;
    v_stack_p60 = v_stack_m180;
loc_0032B2F7:
loc_0032B2FA:
    v_stack_m148 = v_stack_m180;
    goto loc_0032B077;
loc_0032B303:
    if (v_stack_p58 == 0) goto loc_0032B66E;
    if (v_stack_m130 == 1) goto loc_0032B58D;
    result = MiChargeProcessPhysicalPages(v_stack_m180, v_stack_p58, (uint32_t)(*(uint32_t *)(v_rip - 0x32B28B + Arg3 * 4 + 0x13F10)), v_stack_p58);
    if ((uint32_t)(result) == 0) goto loc_0032B061;
    if (v_stack_p60 == 0) goto loc_0032B5A8;
    if (v_stack_p60 == v_stack_m180) goto loc_0032B49D;
    result = PsReferencePartitionSafe(v_stack_p60, v_stack_p58, (uint32_t)(*(uint32_t *)(v_rip - 0x32B28B + Arg3 * 4 + 0x13F10)), v_stack_p58);
    if ((uint8_t)(result) != 0) goto loc_0032B49D;
    result = MiReturnProcessPhysicalPages(v_stack_p58, v_stack_p58, (uint32_t)(*(uint32_t *)(v_rip - 0x32B28B + Arg3 * 4 + 0x13F10)), v_stack_p58);
    goto loc_0032AE67;
loc_0032B36B:
    if (v_stack_p78 == 1) goto loc_0032B5DD;
    result = MiFreeLargeZeroPages(v_rip - 3322507, v_stack_mB8, 1, v_stack_p58);
    result = MiReturnResident(v_rip - 3322507, 0, 1, v_stack_p58);
    if (v_stack_p60 != 0) goto loc_0032B551;
    result = MiReturnFullProcessCommitment(v_stack_p58, 0, 1, v_stack_p58);
    goto loc_0032B570;
loc_0032B3B0:
    result = MI_READ_PTE_LOCK_FREE(v_stack_m160, 0, 1, v_stack_p58);
    result = (result) | (0x4000000ULL);
    v_stack_m160 = result;
    goto loc_0032B14C;
loc_0032B3CC:
    if (condition_is_not_equal) goto loc_0032B585;
loc_0032B3D6:
    if (v_stack_m160 != 8) goto loc_0032AE8B;
    Arg1 = (uint32_t)((2) - (1));
loc_0032B3FC:
    local_rbx = (v_stack_p58) >> (9);
    local_rbx = (local_rbx) & (v_stack_p60);
    Arg2 = (0) >> (9);
    local_rbx = (local_rbx) + (v_stack_m180);
    Arg2 = (Arg2) & (v_stack_p60);
    Arg3 = (v_stack_m150) >> (9);
    Arg2 = (Arg2) + (v_stack_m180);
    Arg3 = (Arg3) & (v_stack_p60);
    Arg3 = (Arg3) + (v_stack_m180);
    Arg1 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_0032B3FC;
    v_stack_m150 = Arg3;
    local_rdi = 0;
    v_stack_m110 = Arg2;
    goto loc_0032B2DC;
loc_0032B438:
    result = MiLocateLockedVadEvent(v_stack_p70, 16, Arg3, v_stack_p58);
    if (result == 0) goto loc_0032B45E;
    v_stack_p60 = *(uint64_t *)(result + 0x18);
    if (*(uint64_t *)(result + 0x18) != 0) goto loc_0032B2F7;
    goto loc_0032B463;
loc_0032B45E:
    v_stack_p60 = 0;
loc_0032B463:
    goto loc_0032B2FA;
loc_0032B482:
    if (local_rbx > (*(uint64_t *)(v_rip + 0xB04C16))) goto loc_0032AC7F;
    goto loc_0032AC83;
loc_0032B49D:
    v_stack_p68 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB04C16) + *(uint16_t *)(v_stack_p58 + 0x4AE) * 8) + 0xB8));
    *(uint16_t *)(0) = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB04C16) + *(uint16_t *)(v_stack_p58 + 0x4AE) * 8) + 0xB8))));
loc_0032B4AC:
    result = MiGetVadLargePageMinimumIndex(v_stack_p70, 16, Arg3, v_stack_p58);
    v_stack_mE8 = v_stack_p70;
    v_stack_p40 = v_stack_mB8;
    result = 0;
    v_stack_p38 = 0;
    v_stack_p30 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB04C16) + *(uint16_t *)(v_stack_p58 + 0x4AE) * 8) + 0xB8);
    v_stack_p28 = Arg8;
    v_stack_p20 = (uint32_t)((uint32_t)(Arg7));
    result = MiCreateLargePfnList(v_stack_mE8, 0, v_stack_m188, *(uint64_t *)(v_rip - 0x32B28B + (uint32_t)((uint32_t)(result)) * 8 + 0x11C60));
    if (v_stack_p60 == 0) goto loc_0032B5D5;
    result = v_stack_p60;
    if (v_stack_p60 != (*(uint64_t *)(result + 0x18))) {
        Arg1 = v_stack_p60;
        result = PsDereferencePartition(Arg1, 0, v_stack_m188, *(uint64_t *)(v_rip - 0x32B28B + (uint32_t)((uint32_t)(result)) * 8 + 0x11C60));
    }
    if (!sign_flag) goto loc_0032B67B;
    if (v_stack_p60 == 0) {
        Arg1 = v_stack_p58;
        Arg2 = v_stack_m188;
        result = MiReturnFullProcessCommitment(Arg1, Arg2, v_stack_m188, *(uint64_t *)(v_rip - 0x32B28B + (uint32_t)((uint32_t)(result)) * 8 + 0x11C60));
    }
    result = MiReturnProcessPhysicalPages(v_stack_p58, v_stack_m188, v_stack_m188, *(uint64_t *)(v_rip - 0x32B28B + (uint32_t)((uint32_t)(result)) * 8 + 0x11C60));
    goto loc_0032AE67;
loc_0032B551:
    Arg3 = 0;
    result = MiReturnCommit(v_rip - 3322507, v_stack_m188, Arg3, *(uint64_t *)(v_rip - 0x32B28B + (uint32_t)((uint32_t)(result)) * 8 + 0x11C60));
    result = MiReturnCrossPartitionCharges(v_rip - 3322507, 2, 2 - 1, v_stack_m188);
loc_0032B570:
    result = MiReturnProcessPhysicalPages(local_rbx, v_stack_m188, 2 - 1, v_stack_m188);
    goto loc_0032AE67;
loc_0032B585:
    goto loc_0032B3D6;
loc_0032B58D:
    result = MiChargeFullProcessCommitment(local_rbx, v_stack_m188, 2 - 1, v_stack_m188);
    if (sign_flag) goto loc_0032AE67;
    goto loc_0032AB08;
loc_0032B5A8:
    result = MiChargeFullProcessCommitment(local_rbx, v_stack_m188, 2 - 1, v_stack_m188);
    if (sign_flag) goto loc_0032B65D;
    v_stack_p68 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB04AC5) + *(uint16_t *)(v_stack_p60 + 0x4AE) * 8);
    goto loc_0032B4AC;
loc_0032B5D5:
    goto loc_0032B523;
loc_0032B5DD:
    result = MiReturnFullProcessCommitment(local_rbx, v_stack_m188, 2 - 1, v_stack_m188);
    goto loc_0032B061;
loc_0032B5ED:
    if (v_stack_m108 == 0) goto loc_0032ACFC;
    result = MiFlushGraphicsPtes(v_stack_p68, v_stack_m108, 2 - 1, v_stack_m188);
    result = 0;
    v_stack_p68 = 0;
    goto loc_0032ACFC;
loc_0032B60F:
    if (v_stack_m108 == 0) goto loc_0032ADDF;
    result = MiFlushGraphicsPtes(v_stack_p68, v_stack_m108, 2 - 1, v_stack_m188);
    goto loc_0032ADDF;
loc_0032B62A:
    if (v_stack_m108 == 0) goto loc_0032AF44;
    result = MiFlushGraphicsPtes(v_stack_p68, v_stack_m108, 2 - 1, v_stack_m188);
    v_stack_p68 = 0;
    goto loc_0032AF44;
loc_0032B64A:
    Arg2 = (uint32_t)((v_stack_m108) & (0xFFFFFFEFULL));
    Arg2 = (uint32_t)((Arg2) | (8));
    goto loc_0032A934;
loc_0032B655:
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFE7ULL));
    goto loc_0032A934;
loc_0032B65D:
    result = MiReturnProcessPhysicalPages(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB04AC5) + *(uint16_t *)(v_stack_p60 + 0x4AE) * 8), v_stack_m188, 2 - 1, v_stack_m188);
    goto loc_0032AE67;
loc_0032B66E:
    goto loc_0032AB08;
loc_0032B67B:
    goto loc_0032AB03;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x21` | `8` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg2` | `- 0x1` | `64` | `R` |
| `Arg11` | `+ 0x0` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0032A860&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
