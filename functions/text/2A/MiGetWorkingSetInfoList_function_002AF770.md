# MiGetWorkingSetInfoList

- RVA: `0x002AF770`–`0x002B0D7C` (길이 `5,644` bytes)
- VA: `0x00000001402AF770`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006D520`
- 디코드: `1,239`개 명령, `5,644/5,644` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **74**; 고유 호출 대상: **45**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x002AF849` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002AF929` → [MiObtainReferencedVadEx](../31/MiObtainReferencedVadEx_function_00316690.md) (function, `0x00316690`)
- `0x002AFA06` → [MiPureAweVad](../32/MiPureAweVad_function_0032B9D0.md) (function, `0x0032B9D0`)
- `0x002AFA85` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002AFAB7` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002AFB2C` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002AFB5F` → [MiGetPagingFileOffset](../36/MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x002AFC0B` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002AFC2C` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002AFC44` → [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) (function, `0x00280D10`)
- `0x002AFC67` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x002AFCD1` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x002AFCDC` → [MI_NODE_FROM_PFN](../2B/MI_NODE_FROM_PFN_function_002B0F30.md) (function, `0x002B0F30`)
- `0x002AFD25` → [MiIsPageOnBadList](../2B/MiIsPageOnBadList_function_002B1018.md) (function, `0x002B1018`)
- `0x002AFD80` → [MiGetWsleContents](../31/MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x002AFE33` → [MiWorkingSetInfoCheckPageTable](MiWorkingSetInfoCheckPageTable_function_002AEFCC.md) (function, `0x002AEFCC`)
- `0x002AFEC0` → [MiGetProtectionFromPte](MiGetProtectionFromPte_function_002AEE78.md) (function, `0x002AEE78`)
- `0x002AFF26` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002AFF48` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002AFF56` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002AFF63` → [MiUnlockAndDereferenceVadShared](MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)
- `0x002AFFA5` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x002AFFBB` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002AFFE4` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002AFFFA` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x002B0080` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002B00E1` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002B0106` → [MiQueryPfn](../44/MiQueryPfn_function_0044EEC8.md) (function, `0x0044EEC8`)
- `0x002B01BE` → [MiGetPfnProtection](../32/MiGetPfnProtection_function_0032A650.md) (function, `0x0032A650`)
- `0x002B0231` → [MiGetProtoPteAddress](../32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x002B026C` → [KiStackAttachProcess](../21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x002B02BB` → [KiUnstackDetachProcess](../21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x002B02CF` → [MiWorkingSetIsContended](MiWorkingSetIsContended_function_002AE520.md) (function, `0x002AE520`)
- `0x002B02EB` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002B0315` → [MiUnlockAndDereferenceVadShared](MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)
- `0x002B0370` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x002B042E` → [MiRotatedToFrameBuffer](../2C/MiRotatedToFrameBuffer_function_002C5FE4.md) (function, `0x002C5FE4`)
- `0x002B0496` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002B04B5` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002B04D2` → [MiIsPageOnBadList](../2B/MiIsPageOnBadList_function_002B1018.md) (function, `0x002B1018`)
- `0x002B0530` → [MiGetProtoPteAddress](../32/MiGetProtoPteAddress_function_0032E970.md) (function, `0x0032E970`)
- `0x002B0588` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002B059A` → [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) (function, `0x002B8B80`)
- `0x002B05B6` → [MiLockLeafPage](../36/MiLockLeafPage_function_003658C0.md) (function, `0x003658C0`)
- `0x002B05D6` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x002B05E3` → [MiGetPagingFileOffset](../36/MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x002B061E` → [MmAccessFault](../27/MmAccessFault_function_0027EE80.md) (function, `0x0027EE80`)
- `0x002B0660` → [MiQueryPfn](../44/MiQueryPfn_function_0044EEC8.md) (function, `0x0044EEC8`)
- `0x002B06B5` → [MiIsPrototypePteVadLookup](../32/MiIsPrototypePteVadLookup_function_00328B70.md) (function, `0x00328B70`)
- `0x002B06E9` → [MmUnlockPages](../29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x002B06F3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002B0700` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x002B07AC` → [MiIsPfnEnclave](../37/MiIsPfnEnclave_function_00375FF0.md) (function, `0x00375FF0`)
- `0x002B0826` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002B083C` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002B0858` → [MiIsLazyStampedPte](../22/MiIsLazyStampedPte_function_00227B10.md) (function, `0x00227B10`)
- `0x002B089F` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x002B0910` → [MmProbeAndLockPages](../23/MmProbeAndLockPages_function_0023B990.md) (function, `0x0023B990`)
- `0x002B0923` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002B0957` → [MmUnlockPages](../29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x002B0961` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002B09BE` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002B09DB` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002B09F0` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002B0A63` → [MiGetValidAweProtection](../4D/MiGetValidAweProtection_function_004DD89C.md) (function, `0x004DD89C`)
- `0x002B0A98` → [MmMapLockedPagesSpecifyCache](../31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x002B0AD6` → [MiGetAweVadPageSize](../../page/AD/MiGetAweVadPageSize_function_00AD58F8.md) (function, `0x00AD58F8`)
- `0x002B0AFA` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002B0B2B` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x002B0B45` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x002B0C99` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x002B0CE4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002B0CF8` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B0D08` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- [MmQueryVirtualMemory](../../page/9D/MmQueryVirtualMemory_function_009D9280.md) at `0x009D96D7`

### Static image references
- `0x002AF786` → RVA `0x00E0A740` (`.data`; read)
- `0x002AF9A2` → RVA `0x00E2DB78` (`.data`; read)
- `0x002AFDA6` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x002B0003` → RVA `0x00E2DC80` (`.data`; read)
- `0x002B0040` → RVA `0x00E2DCE0` (`.data`; read)
- `0x002B009B` → RVA `0x00E30088` (`.data`; read)
- `0x002B0293` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002B067E` → RVA `0x00E2DB70` (`.data`; read)
- `0x002B0691` → RVA `0x00E2DB68` (`.data`; read)
- `0x002B0CEA` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x002B06F3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002B0923` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002B0961` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002B0AD6` → [MiGetAweVadPageSize](../../page/AD/MiGetAweVadPageSize_function_00AD58F8.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002AF770  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
002AF774  53                              push rbx
002AF775  56                              push rsi
002AF776  57                              push rdi
002AF777  41 54                           push r12
002AF779  41 55                           push r13
002AF77B  41 56                           push r14
002AF77D  41 57                           push r15
002AF77F  48 81 EC C0 01 00 00            sub rsp, 0x1c0
002AF786  48 8B 05 B3 AF B5 00            mov rax, qword ptr [rip + 0xb5afb3]
002AF78D  48 33 C4                        xor rax, rsp
002AF790  48 89 84 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rax
002AF798  49 8B D9                        mov rbx, r9
002AF79B  4D 8B F0                        mov r14, r8
002AF79E  4C 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r8
002AF7A6  8B C2                           mov eax, edx
002AF7A8  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
002AF7B0  48 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rcx
002AF7B8  4C 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r8
002AF7C0  45 33 E4                        xor r12d, r12d
002AF7C3  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
002AF7C8  4C 89 A4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r12
002AF7D0  0F 57 C0                        xorps xmm0, xmm0
002AF7D3  0F 11 84 24 F8 00 00 00         movups xmmword ptr [rsp + 0xf8], xmm0
002AF7DB  0F 11 84 24 08 01 00 00         movups xmmword ptr [rsp + 0x108], xmm0
002AF7E3  0F 11 84 24 18 01 00 00         movups xmmword ptr [rsp + 0x118], xmm0
002AF7EB  41 8B FC                        mov edi, r12d
002AF7EE  B9 FF FF FF FF                  mov ecx, 0xffffffff
002AF7F3  4C 3B C9                        cmp r9, rcx
002AF7F6  0F 87 1F 15 00 00               ja 0x1402b0d1b
002AF7FC  4C 8B C3                        mov r8, rbx
002AF7FF  49 C1 E8 04                     shr r8, 4
002AF803  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
002AF808  4D 85 C0                        test r8, r8
002AF80B  0F 84 14 15 00 00               je 0x1402b0d25
002AF811  A9 FC FF FF 3F                  test eax, 0x3ffffffc
002AF816  0F 85 0D 09 00 00               jne 0x1402b0129
002AF81C  83 E0 03                        and eax, 3
002AF81F  3C 03                           cmp al, 3
002AF821  0F 84 02 09 00 00               je 0x1402b0129
002AF827  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
002AF830  49 83 F8 08                     cmp r8, 8
002AF834  0F 87 3B 10 00 00               ja 0x1402b0875
002AF83A  49 C1 E0 04                     shl r8, 4
002AF83E  49 8B D6                        mov rdx, r14
002AF841  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
002AF849  E8 F2 6F 41 00                  call 0x1406c6840
002AF84E  EB 05                           jmp 0x1402af855
002AF850  E9 5B 07 00 00                  jmp 0x1402affb0
002AF855  4C 89 A4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r12
002AF85D  4C 8D AC 24 30 01 00 00         lea r13, [rsp + 0x130]
002AF865  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
002AF86A  4C 89 AC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r13
002AF872  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
002AF87A  48 39 9E B8 00 00 00            cmp qword ptr [rsi + 0xb8], rbx
002AF881  0F 85 D8 09 00 00               jne 0x1402b025f
002AF887  4D 8B FC                        mov r15, r12
002AF88A  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
002AF88F  4C 8D 83 00 04 00 00            lea r8, [rbx + 0x400]
002AF896  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
002AF89B  41 B2 11                        mov r10b, 0x11
002AF89E  44 88 54 24 30                  mov byte ptr [rsp + 0x30], r10b
002AF8A3  49 8B F4                        mov rsi, r12
002AF8A6  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
002AF8AB  4C 89 A4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r12
002AF8B3  44 89 A4 24 80 00 00 00         mov dword ptr [rsp + 0x80], r12d
002AF8BB  4D 8B DC                        mov r11, r12
002AF8BE  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
002AF8C3  48 BA FF FF FE FF FF 7F 00 00   movabs rdx, 0x7ffffffeffff
002AF8CD  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002AF8D2  8B 8C 24 08 02 00 00            mov ecx, dword ptr [rsp + 0x208]
002AF8D9  EB 0A                           jmp 0x1402af8e5
002AF8DB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
002AF8E0  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
002AF8E5  4D 8B F4                        mov r14, r12
002AF8E8  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
002AF8ED  83 E7 F7                        and edi, 0xfffffff7
002AF8F0  49 8B 5D 00                     mov rbx, qword ptr [r13]
002AF8F4  48 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rbx
002AF8FC  48 3B DA                        cmp rbx, rdx
002AF8FF  0F 87 A4 02 00 00               ja 0x1402afba9
002AF905  4C 8B CB                        mov r9, rbx
002AF908  49 C1 E9 0C                     shr r9, 0xc
002AF90C  4C 89 8C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r9
002AF914  4D 85 FF                        test r15, r15
002AF917  75 33                           jne 0x1402af94c
002AF919  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
002AF921  BA 02 00 00 00                  mov edx, 2
002AF926  48 8B CB                        mov rcx, rbx
002AF929  E8 62 6D 06 00                  call 0x140316690
002AF92E  4C 8B F8                        mov r15, rax
002AF931  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
002AF936  4C 8B 5C 24 40                  mov r11, qword ptr [rsp + 0x40]
002AF93B  48 85 C0                        test rax, rax
002AF93E  0F 84 E5 09 00 00               je 0x1402b0329
002AF944  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002AF94A  EB 37                           jmp 0x1402af983
002AF94C  41 0F B6 4F 20                  movzx ecx, byte ptr [r15 + 0x20]
002AF951  48 C1 E1 20                     shl rcx, 0x20
002AF955  41 8B 47 18                     mov eax, dword ptr [r15 + 0x18]
002AF959  48 0B C8                        or rcx, rax
002AF95C  4C 3B C9                        cmp r9, rcx
002AF95F  0F 82 7C 09 00 00               jb 0x1402b02e1
002AF965  41 0F B6 57 21                  movzx edx, byte ptr [r15 + 0x21]
002AF96A  48 C1 E2 20                     shl rdx, 0x20
002AF96E  41 8B 47 1C                     mov eax, dword ptr [r15 + 0x1c]
002AF972  48 0B D0                        or rdx, rax
002AF975  4C 3B CA                        cmp r9, rdx
002AF978  0F 87 63 09 00 00               ja 0x1402b02e1
002AF97E  4D 85 FF                        test r15, r15
002AF981  74 96                           je 0x1402af919
002AF983  48 8B CB                        mov rcx, rbx
002AF986  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
002AF98D  48 89 8C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rcx
002AF995  48 81 F9 00 00 FE 7F            cmp rcx, 0x7ffe0000
002AF99C  0F 84 0C 11 00 00               je 0x1402b0aae
002AF9A2  48 8B 05 CF E1 B7 00            mov rax, qword ptr [rip + 0xb7e1cf]
002AF9A9  48 3B C8                        cmp rcx, rax
002AF9AC  0F 84 F3 10 00 00               je 0x1402b0aa5
002AF9B2  83 E7 DF                        and edi, 0xffffffdf
002AF9B5  8B CF                           mov ecx, edi
002AF9B7  41 8B 47 30                     mov eax, dword ptr [r15 + 0x30]
002AF9BB  24 70                           and al, 0x70
002AF9BD  83 CF 20                        or edi, 0x20
002AF9C0  3C 10                           cmp al, 0x10
002AF9C2  0F 45 F9                        cmovne edi, ecx
002AF9C5  83 E7 F9                        and edi, 0xfffffff9
002AF9C8  89 7C 24 70                     mov dword ptr [rsp + 0x70], edi
002AF9CC  40 F6 C7 20                     test dil, 0x20
002AF9D0  75 41                           jne 0x1402afa13
002AF9D2  41 8B 4F 30                     mov ecx, dword ptr [r15 + 0x30]
002AF9D6  8B D1                           mov edx, ecx
002AF9D8  81 E2 00 00 20 00               and edx, 0x200000
002AF9DE  74 1B                           je 0x1402af9fb
002AF9E0  8B C1                           mov eax, ecx
002AF9E2  C1 E8 13                        shr eax, 0x13
002AF9E5  83 E0 03                        and eax, 3
002AF9E8  0F BA E1 17                     bt ecx, 0x17
002AF9EC  0F 82 8B 0A 00 00               jb 0x1402b047d
002AF9F2  83 F8 02                        cmp eax, 2
002AF9F5  0F 83 82 0A 00 00               jae 0x1402b047d
002AF9FB  85 D2                           test edx, edx
002AF9FD  0F 84 57 04 00 00               je 0x1402afe5a
002AFA03  49 8B CF                        mov rcx, r15
002AFA06  E8 C5 BF 07 00                  call 0x14032b9d0
002AFA0B  85 C0                           test eax, eax
002AFA0D  0F 85 B9 10 00 00               jne 0x1402b0acc
002AFA13  8B C7                           mov eax, edi
002AFA15  83 E0 02                        and eax, 2
002AFA18  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
002AFA1F  0F 85 C7 10 00 00               jne 0x1402b0aec
002AFA25  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
002AFA2A  4C 8B EB                        mov r13, rbx
002AFA2D  49 C1 ED 09                     shr r13, 9
002AFA31  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002AFA3B  4C 23 E8                        and r13, rax
002AFA3E  49 BE 00 00 00 00 80 F6 FF FF   movabs r14, 0xfffff68000000000
002AFA48  49 8B C6                        mov rax, r14
002AFA4B  4C 03 E8                        add r13, rax
002AFA4E  41 80 FA 11                     cmp r10b, 0x11
002AFA52  0F 85 03 02 00 00               jne 0x1402afc5b
002AFA58  49 8B DD                        mov rbx, r13
002AFA5B  48 C1 EB 09                     shr rbx, 9
002AFA5F  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002AFA69  48 23 D8                        and rbx, rax
002AFA6C  49 8B C6                        mov rax, r14
002AFA6F  48 03 D8                        add rbx, rax
002AFA72  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
002AFA7A  41 80 FA 11                     cmp r10b, 0x11
002AFA7E  75 0E                           jne 0x1402afa8e
002AFA80  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002AFA85  E8 66 D1 FC FF                  call 0x14027cbf0
002AFA8A  88 44 24 30                     mov byte ptr [rsp + 0x30], al
002AFA8E  49 C7 C4 FF FF FF FF            mov r12, 0xffffffffffffffff
002AFA95  4D 8B FC                        mov r15, r12
002AFA98  45 33 F6                        xor r14d, r14d
002AFA9B  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
002AFAA0  48 3B F3                        cmp rsi, rbx
002AFAA3  0F 85 53 01 00 00               jne 0x1402afbfc
002AFAA9  49 8B F5                        mov rsi, r13
002AFAAC  4C 89 AC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r13
002AFAB4  48 8B CE                        mov rcx, rsi
002AFAB7  E8 E4 2D FD FF                  call 0x1402828a0
002AFABC  48 8B D8                        mov rbx, rax
002AFABF  48 85 C0                        test rax, rax
002AFAC2  0F 84 AF 06 00 00               je 0x1402b0177
002AFAC8  24 81                           and al, 0x81
002AFACA  3C 81                           cmp al, 0x81
002AFACC  0F 84 F3 10 00 00               je 0x1402b0bc5
002AFAD2  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
002AFAD7  48 3B 84 24 98 00 00 00         cmp rax, qword ptr [rsp + 0x98]
002AFADF  0F 85 30 03 00 00               jne 0x1402afe15
002AFAE5  49 83 FF FF                     cmp r15, -1
002AFAE9  0F 85 B1 01 00 00               jne 0x1402afca0
002AFAEF  83 BC 24 84 00 00 00 00         cmp dword ptr [rsp + 0x84], 0
002AFAF7  0F 85 5A 12 00 00               jne 0x1402b0d57
002AFAFD  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
002AFB05  48 C1 E9 12                     shr rcx, 0x12
002AFB09  81 E1 F8 FF FF 3F               and ecx, 0x3ffffff8
002AFB0F  49 B9 00 00 00 40 FB F6 FF FF   movabs r9, 0xfffff6fb40000000
002AFB19  49 8B C1                        mov rax, r9
002AFB1C  48 03 C8                        add rcx, rax
002AFB1F  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
002AFB24  48 3B F1                        cmp rsi, rcx
002AFB27  75 4D                           jne 0x1402afb76
002AFB29  49 8B CD                        mov rcx, r13
002AFB2C  E8 6F 2D FD FF                  call 0x1402828a0
002AFB31  48 8B D8                        mov rbx, rax
002AFB34  A8 01                           test al, 1
002AFB36  0F 85 36 03 00 00               jne 0x1402afe72
002AFB3C  48 0F BA E0 0A                  bt rax, 0xa
002AFB41  0F 82 AA 09 00 00               jb 0x1402b04f1
002AFB47  48 0F BA E0 0B                  bt rax, 0xb
002AFB4C  0F 82 82 04 00 00               jb 0x1402affd4
002AFB52  40 F6 C7 04                     test dil, 4
002AFB56  0F 85 F9 0C 00 00               jne 0x1402b0855
002AFB5C  48 8B CB                        mov rcx, rbx
002AFB5F  E8 CC F9 0B 00                  call 0x14036f530
002AFB64  85 C0                           test eax, eax
002AFB66  0F 84 DE 05 00 00               je 0x1402b014a
002AFB6C  49 0F BA F6 16                  btr r14, 0x16
002AFB71  49 0F BA EE 17                  bts r14, 0x17
002AFB76  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002AFB7B  45 33 E4                        xor r12d, r12d
002AFB7E  4C 8B 5C 24 40                  mov r11, qword ptr [rsp + 0x40]
002AFB83  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
002AFB88  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002AFB8E  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
002AFB93  8B 8C 24 08 02 00 00            mov ecx, dword ptr [rsp + 0x208]
002AFB9A  48 BA FF FF FE FF FF 7F 00 00   movabs rdx, 0x7ffffffeffff
002AFBA4  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002AFBA9  0F BA E1 1E                     bt ecx, 0x1e
002AFBAD  73 18                           jae 0x1402afbc7
002AFBAF  41 F6 C6 01                     test r14b, 1
002AFBB3  0F 85 DC 02 00 00               jne 0x1402afe95
002AFBB9  49 0F BA E6 1E                  bt r14, 0x1e
002AFBBE  73 07                           jae 0x1402afbc7
002AFBC0  49 81 E6 FF FF 3F F0            and r14, 0xfffffffff03fffff
002AFBC7  4D 89 75 08                     mov qword ptr [r13 + 8], r14
002AFBCB  49 83 C5 10                     add r13, 0x10
002AFBCF  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
002AFBD4  4C 89 AC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r13
002AFBDC  48 83 E8 01                     sub rax, 1
002AFBE0  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002AFBE5  0F 85 F5 FC FF FF               jne 0x1402af8e0
002AFBEB  41 8B DC                        mov ebx, r12d
002AFBEE  4D 85 DB                        test r11, r11
002AFBF1  0F 84 34 03 00 00               je 0x1402aff2b
002AFBF7  E9 25 03 00 00                  jmp 0x1402aff21
002AFBFC  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
002AFC01  48 85 C0                        test rax, rax
002AFC04  74 19                           je 0x1402afc1f
002AFC06  B2 11                           mov dl, 0x11
002AFC08  48 8B C8                        mov rcx, rax
002AFC0B  E8 80 64 F9 FF                  call 0x140246090
002AFC10  33 C0                           xor eax, eax
002AFC12  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002AFC17  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
002AFC1F  48 85 F6                        test rsi, rsi
002AFC22  74 0D                           je 0x1402afc31
002AFC24  48 8B D6                        mov rdx, rsi
002AFC27  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002AFC2C  E8 8F 72 F6 FF                  call 0x140216ec0
002AFC31  45 33 C9                        xor r9d, r9d
002AFC34  4C 8D 84 24 B8 00 00 00         lea r8, [rsp + 0xb8]
002AFC3C  49 8B D5                        mov rdx, r13
002AFC3F  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002AFC44  E8 C7 10 FD FF                  call 0x140280d10
002AFC49  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
002AFC4E  48 8B B4 24 B8 00 00 00         mov rsi, qword ptr [rsp + 0xb8]
002AFC56  E9 59 FE FF FF                  jmp 0x1402afab4
002AFC5B  41 8D 45 08                     lea eax, [r13 + 8]
002AFC5F  A8 78                           test al, 0x78
002AFC61  0F 84 5E 06 00 00               je 0x1402b02c5
002AFC67  E8 74 77 FC FF                  call 0x1402773e0
002AFC6C  85 C0                           test eax, eax
002AFC6E  0F 85 3B 0D 00 00               jne 0x1402b09af
002AFC74  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002AFC7A  E9 D9 FD FF FF                  jmp 0x1402afa58
002AFC7F  83 E7 EF                        and edi, 0xffffffef
002AFC82  4C 8B E3                        mov r12, rbx
002AFC85  49 C1 EC 0C                     shr r12, 0xc
002AFC89  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
002AFC93  4C 23 E0                        and r12, rax
002AFC96  40 F6 C7 30                     test dil, 0x30
002AFC9A  0F 85 CD 06 00 00               jne 0x1402b036d
002AFCA0  4B 8D 34 64                     lea rsi, [r12 + r12*2]
002AFCA4  48 C1 E6 04                     shl rsi, 4
002AFCA8  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
002AFCB2  49 8B C0                        mov rax, r8
002AFCB5  48 03 F0                        add rsi, rax
002AFCB8  4C 8B EE                        mov r13, rsi
002AFCBB  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002AFCBF  48 0F BA E0 28                  bt rax, 0x28
002AFCC4  0F 82 5C 0D 00 00               jb 0x1402b0a26
002AFCCA  4D 8B 75 28                     mov r14, qword ptr [r13 + 0x28]
002AFCCE  49 8B CD                        mov rcx, r13
002AFCD1  E8 1A 2A 07 00                  call 0x1403226f0
002AFCD6  44 8B F8                        mov r15d, eax
002AFCD9  49 8B CD                        mov rcx, r13
002AFCDC  E8 4F 12 00 00                  call 0x1402b0f30
002AFCE1  41 83 E7 07                     and r15d, 7
002AFCE5  49 C1 E7 08                     shl r15, 8
002AFCE9  83 E0 3F                        and eax, 0x3f
002AFCEC  4C 0B F8                        or r15, rax
002AFCEF  49 C1 E7 10                     shl r15, 0x10
002AFCF3  49 C1 EE 30                     shr r14, 0x30
002AFCF7  41 81 E6 00 80 00 00            and r14d, 0x8000
002AFCFE  4D 0B FE                        or r15, r14
002AFD01  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
002AFD06  48 25 FF 7F C0 F8               and rax, 0xfffffffff8c07fff
002AFD0C  4C 0B F8                        or r15, rax
002AFD0F  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
002AFD14  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
002AFD17  C1 E8 18                        shr eax, 0x18
002AFD1A  A8 40                           test al, 0x40
002AFD1C  0F 85 24 0D 00 00               jne 0x1402b0a46
002AFD22  48 8B CE                        mov rcx, rsi
002AFD25  E8 EE 12 00 00                  call 0x1402b1018
002AFD2A  85 C0                           test eax, eax
002AFD2C  0F 85 14 0D 00 00               jne 0x1402b0a46
002AFD32  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002AFD37  49 0F BA E6 17                  bt r14, 0x17
002AFD3C  0F 82 73 01 00 00               jb 0x1402afeb5
002AFD42  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002AFD46  48 0F BA E0 28                  bt rax, 0x28
002AFD4B  0F 82 5F 01 00 00               jb 0x1402afeb0
002AFD51  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002AFD55  48 C1 E8 3C                     shr rax, 0x3c
002AFD59  24 07                           and al, 7
002AFD5B  3C 01                           cmp al, 1
002AFD5D  0F 84 9F 0C 00 00               je 0x1402b0a02
002AFD63  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002AFD67  48 C1 E8 3C                     shr rax, 0x3c
002AFD6B  24 07                           and al, 7
002AFD6D  3C 01                           cmp al, 1
002AFD6F  0F 84 34 0A 00 00               je 0x1402b07a9
002AFD75  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
002AFD7D  49 8B D2                        mov rdx, r10
002AFD80  E8 BB 67 06 00                  call 0x140316540
002AFD85  24 0F                           and al, 0xf
002AFD87  3C 08                           cmp al, 8
002AFD89  0F 84 A4 03 00 00               je 0x1402b0133
002AFD8F  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002AFD93  48 85 C0                        test rax, rax
002AFD96  0F 88 FA 03 00 00               js 0x1402b0196
002AFD9C  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
002AFD9F  48 C1 E8 05                     shr rax, 5
002AFDA3  83 E0 1F                        and eax, 0x1f
002AFDA6  48 8D 0D 53 02 D5 FF            lea rcx, [rip - 0x2afdad]
002AFDAD  44 8B B4 81 30 46 01 00         mov r14d, dword ptr [rcx + rax*4 + 0x14630]
002AFDB5  41 81 E6 FF 07 00 00            and r14d, 0x7ff
002AFDBC  49 C1 E6 04                     shl r14, 4
002AFDC0  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
002AFDC5  48 25 01 80 FF FF               and rax, 0xffffffffffff8001
002AFDCB  4C 0B F0                        or r14, rax
002AFDCE  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002AFDD3  41 8B 47 30                     mov eax, dword ptr [r15 + 0x30]
002AFDD7  25 00 00 20 04                  and eax, 0x4200000
002AFDDC  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002AFDE2  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
002AFDE7  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
002AFDEC  4C 8B 5C 24 40                  mov r11, qword ptr [rsp + 0x40]
002AFDF1  8B 8C 24 08 02 00 00            mov ecx, dword ptr [rsp + 0x208]
002AFDF8  48 BA FF FF FE FF FF 7F 00 00   movabs rdx, 0x7ffffffeffff
002AFE02  3D 00 00 20 04                  cmp eax, 0x4200000
002AFE07  0F 84 60 0C 00 00               je 0x1402b0a6d
002AFE0D  45 33 E4                        xor r12d, r12d
002AFE10  E9 8F FD FF FF                  jmp 0x1402afba4
002AFE15  0F B6 44 24 30                  movzx eax, byte ptr [rsp + 0x30]
002AFE1A  88 44 24 20                     mov byte ptr [rsp + 0x20], al
002AFE1E  44 8B 8C 24 08 02 00 00         mov r9d, dword ptr [rsp + 0x208]
002AFE26  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
002AFE2B  48 8B D6                        mov rdx, rsi
002AFE2E  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002AFE33  E8 94 F1 FF FF                  call 0x1402aefcc
002AFE38  85 C0                           test eax, eax
002AFE3A  0F 84 F9 0E 00 00               je 0x1402b0d39
002AFE40  33 F6                           xor esi, esi
002AFE42  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
002AFE47  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
002AFE4F  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002AFE55  E9 20 FC FF FF                  jmp 0x1402afa7a
002AFE5A  41 8B 47 40                     mov eax, dword ptr [r15 + 0x40]
002AFE5E  A8 01                           test al, 1
002AFE60  0F 84 9D FB FF FF               je 0x1402afa03
002AFE66  83 CF 02                        or edi, 2
002AFE69  89 7C 24 70                     mov dword ptr [rsp + 0x70], edi
002AFE6D  E9 A1 FB FF FF                  jmp 0x1402afa13
002AFE72  49 83 CE 01                     or r14, 1
002AFE76  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
002AFE7B  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
002AFE80  8B 40 30                        mov eax, dword ptr [rax + 0x30]
002AFE83  24 70                           and al, 0x70
002AFE85  3C 40                           cmp al, 0x40
002AFE87  0F 85 F2 FD FF FF               jne 0x1402afc7f
002AFE8D  83 CF 10                        or edi, 0x10
002AFE90  E9 ED FD FF FF                  jmp 0x1402afc82
002AFE95  49 0F BA E6 1E                  bt r14, 0x1e
002AFE9A  0F 83 27 FD FF FF               jae 0x1402afbc7
002AFEA0  49 81 E6 FF FF C0 F8            and r14, 0xfffffffff8c0ffff
002AFEA7  49 83 CE 0E                     or r14, 0xe
002AFEAB  E9 17 FD FF FF                  jmp 0x1402afbc7
002AFEB0  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002AFEB5  48 8B D3                        mov rdx, rbx
002AFEB8  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002AFEBD  49 8B CF                        mov rcx, r15
002AFEC0  E8 B3 EF FF FF                  call 0x1402aee78
002AFEC5  8B C8                           mov ecx, eax
002AFEC7  48 8D 05 32 01 D5 FF            lea rax, [rip - 0x2afece]
002AFECE  8B 94 88 30 46 01 00            mov edx, dword ptr [rax + rcx*4 + 0x14630]
002AFED5  81 E2 FF 07 00 00               and edx, 0x7ff
002AFEDB  48 C1 E2 04                     shl rdx, 4
002AFEDF  49 81 E6 0F 80 FF FF            and r14, 0xffffffffffff800f
002AFEE6  49 0B D6                        or rdx, r14
002AFEE9  41 8B 47 30                     mov eax, dword ptr [r15 + 0x30]
002AFEED  25 00 00 20 04                  and eax, 0x4200000
002AFEF2  3D 00 00 20 04                  cmp eax, 0x4200000
002AFEF7  0F 84 65 0D 00 00               je 0x1402b0c62
002AFEFD  48 0F BA EA 16                  bts rdx, 0x16
002AFF02  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
002AFF07  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
002AFF0B  48 85 C0                        test rax, rax
002AFF0E  0F 88 5C 0A 00 00               js 0x1402b0970
002AFF14  45 33 E4                        xor r12d, r12d
002AFF17  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002AFF1C  E9 5D FC FF FF                  jmp 0x1402afb7e
002AFF21  B2 11                           mov dl, 0x11
002AFF23  49 8B CB                        mov rcx, r11
002AFF26  E8 65 61 F9 FF                  call 0x140246090
002AFF2B  0F B6 74 24 30                  movzx esi, byte ptr [rsp + 0x30]
002AFF30  40 80 FE 11                     cmp sil, 0x11
002AFF34  74 25                           je 0x1402aff5b
002AFF36  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
002AFF3B  48 85 C0                        test rax, rax
002AFF3E  74 0D                           je 0x1402aff4d
002AFF40  48 8B D0                        mov rdx, rax
002AFF43  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002AFF48  E8 73 6F F6 FF                  call 0x140216ec0
002AFF4D  40 0F B6 D6                     movzx edx, sil
002AFF51  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002AFF56  E8 35 D7 FC FF                  call 0x14027d690
002AFF5B  4D 85 FF                        test r15, r15
002AFF5E  74 08                           je 0x1402aff68
002AFF60  49 8B CF                        mov rcx, r15
002AFF63  E8 A8 EF FF FF                  call 0x1402aef10
002AFF68  40 F6 C7 01                     test dil, 1
002AFF6C  0F 85 3F 03 00 00               jne 0x1402b02b1
002AFF72  48 8B BC 24 C0 00 00 00         mov rdi, qword ptr [rsp + 0xc0]
002AFF7A  48 85 FF                        test rdi, rdi
002AFF7D  0F 85 63 07 00 00               jne 0x1402b06e6
002AFF83  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
002AFF8B  4C 2B E8                        sub r13, rax
002AFF8E  49 83 E5 F0                     and r13, 0xfffffffffffffff0
002AFF92  4D 8B C5                        mov r8, r13
002AFF95  48 8D 94 24 30 01 00 00         lea rdx, [rsp + 0x130]
002AFF9D  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
002AFFA5  E8 96 68 41 00                  call 0x1406c6840
002AFFAA  EB 02                           jmp 0x1402affae
002AFFAC  EB 02                           jmp 0x1402affb0
002AFFAE  8B C3                           mov eax, ebx
002AFFB0  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
002AFFB8  48 33 CC                        xor rcx, rsp
002AFFBB  E8 80 C6 3F 00                  call 0x1406ac640
002AFFC0  48 81 C4 C0 01 00 00            add rsp, 0x1c0
002AFFC7  41 5F                           pop r15
002AFFC9  41 5E                           pop r14
002AFFCB  41 5D                           pop r13
002AFFCD  41 5C                           pop r12
002AFFCF  5F                              pop rdi
002AFFD0  5E                              pop rsi
002AFFD1  5B                              pop rbx
002AFFD2  C3                              ret
002AFFD3  CC                              int3
002AFFD4  45 33 E4                        xor r12d, r12d
002AFFD7  49 BE 00 00 00 00 00 DE FF FF   movabs r14, 0xffffde0000000000
002AFFE1  49 8B CD                        mov rcx, r13
002AFFE4  E8 B7 28 FD FF                  call 0x1402828a0
002AFFE9  48 8B D8                        mov rbx, rax
002AFFEC  48 0F BA E0 0B                  bt rax, 0xb
002AFFF1  0F 83 BD 0C 00 00               jae 0x1402b0cb4
002AFFF7  48 8B C8                        mov rcx, rax
002AFFFA  E8 11 2A 0C 00                  call 0x140372a10
002AFFFF  85 C0                           test eax, eax
002B0001  74 DE                           je 0x1402affe1
002B0003  48 8B 05 76 DC B7 00            mov rax, qword ptr [rip + 0xb7dc76]
002B000A  48 85 C0                        test rax, rax
002B000D  74 12                           je 0x1402b0021
002B000F  F6 C3 10                        test bl, 0x10
002B0012  0F 85 29 01 00 00               jne 0x1402b0141
002B0018  48 8B C8                        mov rcx, rax
002B001B  48 F7 D1                        not rcx
002B001E  48 23 CB                        and rcx, rbx
002B0021  48 C1 E9 0C                     shr rcx, 0xc
002B0025  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
002B002F  48 23 C8                        and rcx, rax
002B0032  48 8D 14 49                     lea rdx, [rcx + rcx*2]
002B0036  48 03 D2                        add rdx, rdx
002B0039  49 8B C6                        mov rax, r14
002B003C  48 8D 34 D0                     lea rsi, [rax + rdx*8]
002B0040  48 3B 0D 99 DC B7 00            cmp rcx, qword ptr [rip + 0xb7dc99]
002B0047  77 98                           ja 0x1402affe1
002B0049  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
002B0053  48 8B C0                        mov rax, rax
002B0056  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
002B005A  48 C1 E8 36                     shr rax, 0x36
002B005E  0F BA E0 00                     bt eax, 0
002B0062  0F 83 79 FF FF FF               jae 0x1402affe1
002B0068  44 89 A4 24 90 00 00 00         mov dword ptr [rsp + 0x90], r12d
002B0070  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
002B0077  0F 82 03 02 00 00               jb 0x1402b0280
002B007D  49 8B CD                        mov rcx, r13
002B0080  E8 1B 28 FD FF                  call 0x1402828a0
002B0085  48 3B C3                        cmp rax, rbx
002B0088  0F 85 CB 02 00 00               jne 0x1402b0359
002B008E  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002B0092  48 C1 E8 2B                     shr rax, 0x2b
002B0096  25 FF 03 00 00                  and eax, 0x3ff
002B009B  48 8B 15 E6 FF B7 00            mov rdx, qword ptr [rip + 0xb7ffe6]
002B00A2  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
002B00A6  8B 40 04                        mov eax, dword ptr [rax + 4]
002B00A9  84 C0                           test al, al
002B00AB  0F 88 E3 0B 00 00               js 0x1402b0c94
002B00B1  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
002B00B5  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
002B00BF  48 0B C1                        or rax, rcx
002B00C2  49 3B C5                        cmp rax, r13
002B00C5  0F 85 F1 0B 00 00               jne 0x1402b0cbc
002B00CB  49 BE 00 00 00 00 00 DE FF FF   movabs r14, 0xffffde0000000000
002B00D5  48 85 F6                        test rsi, rsi
002B00D8  0F 84 63 02 00 00               je 0x1402b0341
002B00DE  49 8B CD                        mov rcx, r13
002B00E1  E8 BA 27 FD FF                  call 0x1402828a0
002B00E6  49 8B C6                        mov rax, r14
002B00E9  48 8B CE                        mov rcx, rsi
002B00EC  48 2B C8                        sub rcx, rax
002B00EF  48 C1 F9 04                     sar rcx, 4
002B00F3  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002B00FD  48 0F AF C8                     imul rcx, rax
002B0101  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
002B0106  E8 BD ED 19 00                  call 0x14044eec8
002B010B  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002B0115  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
002B011A  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002B011F  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002B0124  E9 55 FA FF FF                  jmp 0x1402afb7e
002B0129  B8 0D 00 00 C0                  mov eax, 0xc000000d
002B012E  E9 7D FE FF FF                  jmp 0x1402affb0
002B0133  48 81 4C 24 68 00 00 40 00      or qword ptr [rsp + 0x68], 0x400000
002B013C  E9 4E FC FF FF                  jmp 0x1402afd8f
002B0141  48 83 E1 EF                     and rcx, 0xffffffffffffffef
002B0145  E9 D7 FE FF FF                  jmp 0x1402b0021
002B014A  48 85 DB                        test rbx, rbx
002B014D  0F 85 23 FA FF FF               jne 0x1402afb76
002B0153  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002B0158  41 F7 47 30 00 00 20 00         test dword ptr [r15 + 0x30], 0x200000
002B0160  0F 95 C1                        setne cl
002B0163  40 F6 C7 08                     test dil, 8
002B0167  0F 94 C0                        sete al
002B016A  84 C8                           test al, cl
002B016C  0F 85 09 FA FF FF               jne 0x1402afb7b
002B0172  E9 7F 03 00 00                  jmp 0x1402b04f6
002B0177  40 F6 C7 20                     test dil, 0x20
002B017B  0F 85 F5 F9 FF FF               jne 0x1402afb76
002B0181  44 39 B4 24 84 00 00 00         cmp dword ptr [rsp + 0x84], r14d
002B0189  0F 85 56 F9 FF FF               jne 0x1402afae5
002B018F  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
002B0194  EB BD                           jmp 0x1402b0153
002B0196  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002B019A  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
002B01A4  48 23 C1                        and rax, rcx
002B01A7  48 83 F8 07                     cmp rax, 7
002B01AB  0F 83 6E 01 00 00               jae 0x1402b031f
002B01B1  48 8B 5E 18                     mov rbx, qword ptr [rsi + 0x18]
002B01B5  48 23 D9                        and rbx, rcx
002B01B8  4C 8B C6                        mov r8, rsi
002B01BB  49 8B D2                        mov rdx, r10
002B01BE  E8 8D A4 07 00                  call 0x14032a650
002B01C3  8B C8                           mov ecx, eax
002B01C5  48 8D 05 34 FE D4 FF            lea rax, [rip - 0x2b01cc]
002B01CC  44 8B B4 88 30 46 01 00         mov r14d, dword ptr [rax + rcx*4 + 0x14630]
002B01D4  41 81 E6 FF 07 00 00            and r14d, 0x7ff
002B01DB  49 C1 E6 03                     shl r14, 3
002B01DF  83 E3 07                        and ebx, 7
002B01E2  4C 0B F3                        or r14, rbx
002B01E5  4D 03 F6                        add r14, r14
002B01E8  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
002B01ED  48 25 01 80 FF FF               and rax, 0xffffffffffff8001
002B01F3  4C 0B F0                        or r14, rax
002B01F6  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
002B01FB  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002B0200  40 F6 C7 08                     test dil, 8
002B0204  0F 85 41 06 00 00               jne 0x1402b084b
002B020A  41 F7 47 30 00 00 20 00         test dword ptr [r15 + 0x30], 0x200000
002B0212  0F 85 63 F9 FF FF               jne 0x1402afb7b
002B0218  4C 8D 8C 24 F0 00 00 00         lea r9, [rsp + 0xf0]
002B0220  41 B8 08 00 00 00               mov r8d, 8
002B0226  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
002B022E  49 8B CF                        mov rcx, r15
002B0231  E8 3A E7 07 00                  call 0x14032e970
002B0236  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
002B023A  48 BA 00 00 00 00 00 00 00 80   movabs rdx, 0x8000000000000000
002B0244  48 0B CA                        or rcx, rdx
002B0247  48 3B C1                        cmp rax, rcx
002B024A  0F 85 C4 FC FF FF               jne 0x1402aff14
002B0250  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002B0255  49 0F BA EE 1E                  bts r14, 0x1e
002B025A  E9 1C F9 FF FF                  jmp 0x1402afb7b
002B025F  4C 8D 84 24 F8 00 00 00         lea r8, [rsp + 0xf8]
002B0267  33 D2                           xor edx, edx
002B0269  48 8B CB                        mov rcx, rbx
002B026C  E8 AF 65 F6 FF                  call 0x140216820
002B0271  BF 01 00 00 00                  mov edi, 1
002B0276  E9 0C F6 FF FF                  jmp 0x1402af887
002B027B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
002B0280  44 8B B4 24 90 00 00 00         mov r14d, dword ptr [rsp + 0x90]
002B0288  41 FF C6                        inc r14d
002B028B  44 89 B4 24 90 00 00 00         mov dword ptr [rsp + 0x90], r14d
002B0293  44 85 35 12 50 D1 00            test dword ptr [rip + 0xd15012], r14d
002B029A  0F 84 4A 0A 00 00               je 0x1402b0cea
002B02A0  F3 90                           pause
002B02A2  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002B02A6  48 85 C0                        test rax, rax
002B02A9  0F 89 C1 FD FF FF               jns 0x1402b0070
002B02AF  EB CF                           jmp 0x1402b0280
002B02B1  33 D2                           xor edx, edx
002B02B3  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
002B02BB  E8 70 7A F6 FF                  call 0x140217d30
002B02C0  E9 AD FC FF FF                  jmp 0x1402aff72
002B02C5  33 D2                           xor edx, edx
002B02C7  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
002B02CC  48 8B CB                        mov rcx, rbx
002B02CF  E8 4C E2 FF FF                  call 0x1402ae520
002B02D4  85 C0                           test eax, eax
002B02D6  0F 84 8B F9 FF FF               je 0x1402afc67
002B02DC  E9 D3 06 00 00                  jmp 0x1402b09b4
002B02E1  4D 85 DB                        test r11, r11
002B02E4  74 22                           je 0x1402b0308
002B02E6  B2 11                           mov dl, 0x11
002B02E8  49 8B CB                        mov rcx, r11
002B02EB  E8 A0 5D F9 FF                  call 0x140246090
002B02F0  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
002B02F5  4C 89 A4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r12
002B02FD  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002B0303  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
002B0308  41 80 FA 11                     cmp r10b, 0x11
002B030C  0F 85 79 01 00 00               jne 0x1402b048b
002B0312  49 8B CF                        mov rcx, r15
002B0315  E8 F6 EB FF FF                  call 0x1402aef10
002B031A  E9 FA F5 FF FF                  jmp 0x1402af919
002B031F  BB 07 00 00 00                  mov ebx, 7
002B0324  E9 8F FE FF FF                  jmp 0x1402b01b8
002B0329  8B 9C 24 80 00 00 00            mov ebx, dword ptr [rsp + 0x80]
002B0330  81 FB 0A 01 00 C0               cmp ebx, 0xc000010a
002B0336  0F 85 4C F8 FF FF               jne 0x1402afb88
002B033C  E9 AD F8 FF FF                  jmp 0x1402afbee
002B0341  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
002B0349  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
002B034E  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002B0354  E9 21 F7 FF FF                  jmp 0x1402afa7a
002B0359  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002B0363  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
002B0368  E9 6A FC FF FF                  jmp 0x1402affd7
002B036D  49 8B CC                        mov rcx, r12
002B0370  E8 5B 89 08 00                  call 0x140338cd0
002B0375  8B D0                           mov edx, eax
002B0377  4B 8D 0C 64                     lea rcx, [r12 + r12*2]
002B037B  48 03 C9                        add rcx, rcx
002B037E  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
002B0388  49 8B C0                        mov rax, r8
002B038B  4C 8D 3C C8                     lea r15, [rax + rcx*8]
002B038F  4C 3B 25 4A D9 B7 00            cmp r12, qword ptr [rip + 0xb7d94a]
002B0396  77 24                           ja 0x1402b03bc
002B0398  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
002B03A2  48 8B C0                        mov rax, rax
002B03A5  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
002B03A9  48 C1 E9 36                     shr rcx, 0x36
002B03AD  0F BA E1 00                     bt ecx, 0
002B03B1  0F 82 0D 01 00 00               jb 0x1402b04c4
002B03B7  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002B03BC  8B F2                           mov esi, edx
002B03BE  83 E6 3F                        and esi, 0x3f
002B03C1  48 C1 E6 10                     shl rsi, 0x10
002B03C5  49 81 E6 FF FF C0 FF            and r14, 0xffffffffffc0ffff
002B03CC  49 0B F6                        or rsi, r14
002B03CF  40 F6 C7 20                     test dil, 0x20
002B03D3  74 56                           je 0x1402b042b
002B03D5  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002B03DA  41 8B 57 30                     mov edx, dword ptr [r15 + 0x30]
002B03DE  C1 EA 07                        shr edx, 7
002B03E1  83 E2 1F                        and edx, 0x1f
002B03E4  0F B6 C3                        movzx eax, bl
002B03E7  24 18                           and al, 0x18
002B03E9  3C 08                           cmp al, 8
002B03EB  0F 84 23 06 00 00               je 0x1402b0a14
002B03F1  F6 C3 10                        test bl, 0x10
002B03F4  74 03                           je 0x1402b03f9
002B03F6  83 CA 08                        or edx, 8
002B03F9  48 81 CE 01 00 40 00            or rsi, 0x400001
002B0400  8B C2                           mov eax, edx
002B0402  48 8D 15 F7 FB D4 FF            lea rdx, [rip - 0x2b0409]
002B0409  44 8B B4 82 30 46 01 00         mov r14d, dword ptr [rdx + rax*4 + 0x14630]
002B0411  41 81 E6 FF 07 00 00            and r14d, 0x7ff
002B0418  49 C1 E6 04                     shl r14, 4
002B041C  48 81 E6 0F 80 FF FF            and rsi, 0xffffffffffff800f
002B0423  4C 0B F6                        or r14, rsi
002B0426  E9 50 F7 FF FF                  jmp 0x1402afb7b
002B042B  49 8B CD                        mov rcx, r13
002B042E  E8 B1 5B 01 00                  call 0x1402c5fe4
002B0433  85 C0                           test eax, eax
002B0435  0F 84 C2 02 00 00               je 0x1402b06fd
002B043B  48 0F BA E3 0B                  bt rbx, 0xb
002B0440  0F 83 FD 08 00 00               jae 0x1402b0d43
002B0446  BA 04 00 00 00                  mov edx, 4
002B044B  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002B0450  41 8B 47 30                     mov eax, dword ptr [r15 + 0x30]
002B0454  44 8B C0                        mov r8d, eax
002B0457  41 81 E0 00 0C 00 00            and r8d, 0xc00
002B045E  A9 80 03 00 00                  test eax, 0x380
002B0463  0F 95 C1                        setne cl
002B0466  41 81 F8 00 0C 00 00            cmp r8d, 0xc00
002B046D  0F 94 C0                        sete al
002B0470  84 C8                           test al, cl
002B0472  0F 84 07 08 00 00               je 0x1402b0c7f
002B0478  83 CA 18                        or edx, 0x18
002B047B  EB 83                           jmp 0x1402b0400
002B047D  83 F8 02                        cmp eax, 2
002B0480  0F 83 E0 F9 FF FF               jae 0x1402afe66
002B0486  E9 70 F5 FF FF                  jmp 0x1402af9fb
002B048B  48 85 F6                        test rsi, rsi
002B048E  74 1E                           je 0x1402b04ae
002B0490  48 8B D6                        mov rdx, rsi
002B0493  49 8B C8                        mov rcx, r8
002B0496  E8 25 6A F6 FF                  call 0x140216ec0
002B049B  49 8B F4                        mov rsi, r12
002B049E  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
002B04A3  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002B04A9  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
002B04AE  41 0F B6 D2                     movzx edx, r10b
002B04B2  49 8B C8                        mov rcx, r8
002B04B5  E8 D6 D1 FC FF                  call 0x14027d690
002B04BA  C6 44 24 30 11                  mov byte ptr [rsp + 0x30], 0x11
002B04BF  E9 4E FE FF FF                  jmp 0x1402b0312
002B04C4  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
002B04C8  C1 E8 18                        shr eax, 0x18
002B04CB  A8 40                           test al, 0x40
002B04CD  75 10                           jne 0x1402b04df
002B04CF  49 8B CF                        mov rcx, r15
002B04D2  E8 41 0B 00 00                  call 0x1402b1018
002B04D7  85 C0                           test eax, eax
002B04D9  0F 84 D8 FE FF FF               je 0x1402b03b7
002B04DF  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002B04E4  B8 00 00 00 80                  mov eax, 0x80000000
002B04E9  4C 0B F0                        or r14, rax
002B04EC  E9 CB FE FF FF                  jmp 0x1402b03bc
002B04F1  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002B04F6  45 33 E4                        xor r12d, r12d
002B04F9  45 8B C4                        mov r8d, r12d
002B04FC  40 F6 C7 08                     test dil, 8
002B0500  0F 85 78 01 00 00               jne 0x1402b067e
002B0506  41 F7 47 30 00 00 20 00         test dword ptr [r15 + 0x30], 0x200000
002B050E  0F 85 AE 01 00 00               jne 0x1402b06c2
002B0514  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
002B051C  48 C1 EA 0C                     shr rdx, 0xc
002B0520  4C 8D 8C 24 F0 00 00 00         lea r9, [rsp + 0xf0]
002B0528  45 8D 44 24 08                  lea r8d, [r12 + 8]
002B052D  49 8B CF                        mov rcx, r15
002B0530  E8 3B E4 07 00                  call 0x14032e970
002B0535  4C 8B C0                        mov r8, rax
002B0538  48 85 DB                        test rbx, rbx
002B053B  0F 85 71 01 00 00               jne 0x1402b06b2
002B0541  49 8B D8                        mov rbx, r8
002B0544  48 85 DB                        test rbx, rbx
002B0547  0F 84 31 F6 FF FF               je 0x1402afb7e
002B054D  49 0F BA EE 0F                  bts r14, 0xf
002B0552  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
002B0557  49 3B D8                        cmp rbx, r8
002B055A  75 0A                           jne 0x1402b0566
002B055C  49 0F BA EE 1E                  bts r14, 0x1e
002B0561  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
002B0566  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
002B056E  48 33 C3                        xor rax, rbx
002B0571  48 A9 00 F0 FF FF               test rax, -0x1000
002B0577  74 38                           je 0x1402b05b1
002B0579  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
002B057E  48 85 C0                        test rax, rax
002B0581  74 12                           je 0x1402b0595
002B0583  B2 11                           mov dl, 0x11
002B0585  48 8B C8                        mov rcx, rax
002B0588  E8 03 5B F9 FF                  call 0x140246090
002B058D  4C 89 A4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r12
002B0595  33 D2                           xor edx, edx
002B0597  48 8B CB                        mov rcx, rbx
002B059A  E8 E1 85 00 00                  call 0x1402b8b80
002B059F  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002B05A4  48 85 C0                        test rax, rax
002B05A7  74 58                           je 0x1402b0601
002B05A9  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
002B05B1  33 D2                           xor edx, edx
002B05B3  48 8B CB                        mov rcx, rbx
002B05B6  E8 05 53 0B 00                  call 0x1403658c0
002B05BB  48 8B F0                        mov rsi, rax
002B05BE  48 8B 13                        mov rdx, qword ptr [rbx]
002B05C1  48 85 C0                        test rax, rax
002B05C4  75 70                           jne 0x1402b0636
002B05C6  48 F7 C2 00 0C 00 00            test rdx, 0xc00
002B05CD  0F 85 44 F9 FF FF               jne 0x1402aff17
002B05D3  48 8B CA                        mov rcx, rdx
002B05D6  E8 35 24 0C 00                  call 0x140372a10
002B05DB  85 C0                           test eax, eax
002B05DD  0F 84 34 F9 FF FF               je 0x1402aff17
002B05E3  E8 48 EF 0B 00                  call 0x14036f530
002B05E8  85 C0                           test eax, eax
002B05EA  0F 85 AE 00 00 00               jne 0x1402b069e
002B05F0  48 85 D2                        test rdx, rdx
002B05F3  0F 85 1E F9 FF FF               jne 0x1402aff17
002B05F9  4D 8B F4                        mov r14, r12
002B05FC  E9 7D F5 FF FF                  jmp 0x1402afb7e
002B0601  44 0F B6 74 24 30               movzx r14d, byte ptr [rsp + 0x30]
002B0607  41 80 FE 11                     cmp r14b, 0x11
002B060B  0F 85 08 02 00 00               jne 0x1402b0819
002B0611  45 33 C9                        xor r9d, r9d
002B0614  45 33 C0                        xor r8d, r8d
002B0617  48 8B D3                        mov rdx, rbx
002B061A  41 8D 49 02                     lea ecx, [r9 + 2]
002B061E  E8 5D E8 FC FF                  call 0x14027ee80
002B0623  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
002B062B  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002B0631  E9 44 F4 FF FF                  jmp 0x1402afa7a
002B0636  49 B8 00 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000000
002B0640  49 8B D0                        mov rdx, r8
002B0643  48 8B CE                        mov rcx, rsi
002B0646  48 2B CA                        sub rcx, rdx
002B0649  48 C1 F9 04                     sar rcx, 4
002B064D  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002B0657  48 0F AF C8                     imul rcx, rax
002B065B  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
002B0660  E8 63 E8 19 00                  call 0x14044eec8
002B0665  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002B066F  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
002B0674  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002B0679  E9 00 F5 FF FF                  jmp 0x1402afb7e
002B067E  4C 8B 05 EB D4 B7 00            mov r8, qword ptr [rip + 0xb7d4eb]
002B0685  48 81 BC 24 E8 00 00 00 00 00 FE 7F  cmp qword ptr [rsp + 0xe8], 0x7ffe0000
002B0691  4C 0F 44 05 CF D4 B7 00         cmove r8, qword ptr [rip + 0xb7d4cf]
002B0699  E9 A3 FE FF FF                  jmp 0x1402b0541
002B069E  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002B06A3  49 0F BA F6 16                  btr r14, 0x16
002B06A8  49 0F BA EE 17                  bts r14, 0x17
002B06AD  E9 CC F4 FF FF                  jmp 0x1402afb7e
002B06B2  48 8B CB                        mov rcx, rbx
002B06B5  E8 B6 84 07 00                  call 0x140328b70
002B06BA  85 C0                           test eax, eax
002B06BC  0F 85 7F FE FF FF               jne 0x1402b0541
002B06C2  48 8B 05 B7 D5 B7 00            mov rax, qword ptr [rip + 0xb7d5b7]
002B06C9  48 85 C0                        test rax, rax
002B06CC  74 0F                           je 0x1402b06dd
002B06CE  F6 C3 10                        test bl, 0x10
002B06D1  0F 85 3B 06 00 00               jne 0x1402b0d12
002B06D7  48 F7 D0                        not rax
002B06DA  48 23 D8                        and rbx, rax
002B06DD  48 C1 FB 10                     sar rbx, 0x10
002B06E1  E9 5E FE FF FF                  jmp 0x1402b0544
002B06E6  48 8B CF                        mov rcx, rdi
002B06E9  E8 F2 E7 FE FF                  call 0x14029eee0
002B06EE  33 D2                           xor edx, edx
002B06F0  48 8B CF                        mov rcx, rdi
002B06F3  E8 78 21 8D 00                  call 0x140b82870
002B06F8  E9 B1 F8 FF FF                  jmp 0x1402affae
002B06FD  49 8B CF                        mov rcx, r15
002B0700  E8 EB 1F 07 00                  call 0x1403226f0
002B0705  44 8B D0                        mov r10d, eax
002B0708  49 C1 E2 18                     shl r10, 0x18
002B070C  49 33 F2                        xor rsi, r10
002B070F  48 81 E6 FF FF FF F8            and rsi, 0xfffffffff8ffffff
002B0716  49 33 F2                        xor rsi, r10
002B0719  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
002B071E  41 8B 57 10                     mov edx, dword ptr [r15 + 0x10]
002B0722  48 C1 EA 05                     shr rdx, 5
002B0726  83 E2 1F                        and edx, 0x1f
002B0729  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
002B072D  48 0F BA E0 28                  bt rax, 0x28
002B0732  0F 82 15 06 00 00               jb 0x1402b0d4d
002B0738  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
002B073C  48 85 C0                        test rax, rax
002B073F  0F 88 08 06 00 00               js 0x1402b0d4d
002B0745  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
002B0749  48 85 C0                        test rax, rax
002B074C  0F 84 FB 05 00 00               je 0x1402b0d4d
002B0752  48 81 4C 24 68 00 80 00 00      or qword ptr [rsp + 0x68], 0x8000
002B075B  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B075F  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
002B0769  48 23 C1                        and rax, rcx
002B076C  48 83 F8 07                     cmp rax, 7
002B0770  0F 83 A6 02 00 00               jae 0x1402b0a1c
002B0776  49 8B 77 18                     mov rsi, qword ptr [r15 + 0x18]
002B077A  48 23 F1                        and rsi, rcx
002B077D  83 E6 07                        and esi, 7
002B0780  48 03 F6                        add rsi, rsi
002B0783  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
002B0788  48 83 E0 F1                     and rax, 0xfffffffffffffff1
002B078C  48 0B F0                        or rsi, rax
002B078F  8B C2                           mov eax, edx
002B0791  48 8D 15 68 F8 D4 FF            lea rdx, [rip - 0x2b0798]
002B0798  8B 94 82 70 10 01 00            mov edx, dword ptr [rdx + rax*4 + 0x11070]
002B079F  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002B07A4  E9 57 FC FF FF                  jmp 0x1402b0400
002B07A9  48 8B CE                        mov rcx, rsi
002B07AC  E8 3F 58 0C 00                  call 0x140375ff0
002B07B1  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002B07B6  85 C0                           test eax, eax
002B07B8  0F 84 9F 02 00 00               je 0x1402b0a5d
002B07BE  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
002B07C1  48 C1 E8 05                     shr rax, 5
002B07C5  83 E0 1F                        and eax, 0x1f
002B07C8  8B C0                           mov eax, eax
002B07CA  48 8D 0D 2F F8 D4 FF            lea rcx, [rip - 0x2b07d1]
002B07D1  44 8B B4 81 30 46 01 00         mov r14d, dword ptr [rcx + rax*4 + 0x14630]
002B07D9  41 81 E6 FF 07 00 00            and r14d, 0x7ff
002B07E0  49 C1 E6 04                     shl r14, 4
002B07E4  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
002B07E9  48 25 0F 80 FF FF               and rax, 0xffffffffffff800f
002B07EF  4C 0B F0                        or r14, rax
002B07F2  41 8B 47 30                     mov eax, dword ptr [r15 + 0x30]
002B07F6  25 00 00 20 04                  and eax, 0x4200000
002B07FB  3D 00 00 20 04                  cmp eax, 0x4200000
002B0800  75 0D                           jne 0x1402b080f
002B0802  48 B8 FF FF FF FF F0 FF FF FF   movabs rax, 0xfffffff0ffffffff
002B080C  4C 23 F0                        and r14, rax
002B080F  49 0F BA EE 16                  bts r14, 0x16
002B0814  E9 62 F3 FF FF                  jmp 0x1402afb7b
002B0819  48 85 F6                        test rsi, rsi
002B081C  74 15                           je 0x1402b0833
002B081E  48 8B D6                        mov rdx, rsi
002B0821  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002B0826  E8 95 66 F6 FF                  call 0x140216ec0
002B082B  49 8B F4                        mov rsi, r12
002B082E  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
002B0833  41 0F B6 D6                     movzx edx, r14b
002B0837  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002B083C  E8 4F CE FC FF                  call 0x14027d690
002B0841  C6 44 24 30 11                  mov byte ptr [rsp + 0x30], 0x11
002B0846  E9 C6 FD FF FF                  jmp 0x1402b0611
002B084B  49 0F BA EE 1E                  bts r14, 0x1e
002B0850  E9 26 F3 FF FF                  jmp 0x1402afb7b
002B0855  48 8B CB                        mov rcx, rbx
002B0858  E8 B3 72 F7 FF                  call 0x140227b10
002B085D  85 C0                           test eax, eax
002B085F  0F 84 F7 F2 FF FF               je 0x1402afb5c
002B0865  45 33 E4                        xor r12d, r12d
002B0868  45 8B F4                        mov r14d, r12d
002B086B  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002B0870  E9 09 F3 FF FF                  jmp 0x1402afb7e
002B0875  48 F7 C3 FF 0F 00 00            test rbx, 0xfff
002B087C  49 8B D4                        mov rdx, r12
002B087F  0F 95 C2                        setne dl
002B0882  48 83 C2 07                     add rdx, 7
002B0886  48 8B C3                        mov rax, rbx
002B0889  48 C1 E8 0C                     shr rax, 0xc
002B088D  48 03 D0                        add rdx, rax
002B0890  48 C1 E2 03                     shl rdx, 3
002B0894  B9 40 00 00 00                  mov ecx, 0x40
002B0899  41 B8 4D 6D 20 20               mov r8d, 0x20206d4d
002B089F  E8 9C AC 0A 00                  call 0x14035b540
002B08A4  4C 8B F8                        mov r15, rax
002B08A7  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
002B08AF  48 85 C0                        test rax, rax
002B08B2  0F 84 AE 00 00 00               je 0x1402b0966
002B08B8  4C 89 20                        mov qword ptr [rax], r12
002B08BB  41 8B D6                        mov edx, r14d
002B08BE  8B CA                           mov ecx, edx
002B08C0  81 E1 FF 0F 00 00               and ecx, 0xfff
002B08C6  48 81 C1 FF 0F 00 00            add rcx, 0xfff
002B08CD  48 03 CB                        add rcx, rbx
002B08D0  48 C1 E9 0C                     shr rcx, 0xc
002B08D4  66 83 C1 06                     add cx, 6
002B08D8  66 C1 E1 03                     shl cx, 3
002B08DC  66 89 48 08                     mov word ptr [rax + 8], cx
002B08E0  66 44 89 60 0A                  mov word ptr [rax + 0xa], r12w
002B08E5  49 8B C6                        mov rax, r14
002B08E8  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
002B08EE  49 89 47 20                     mov qword ptr [r15 + 0x20], rax
002B08F2  81 E2 FF 0F 00 00               and edx, 0xfff
002B08F8  41 89 57 2C                     mov dword ptr [r15 + 0x2c], edx
002B08FC  41 89 5F 28                     mov dword ptr [r15 + 0x28], ebx
002B0900  41 B8 01 00 00 00               mov r8d, 1
002B0906  0F B6 96 32 02 00 00            movzx edx, byte ptr [rsi + 0x232]
002B090D  49 8B CF                        mov rcx, r15
002B0910  E8 7B B0 F8 FF                  call 0x14023b990
002B0915  EB 18                           jmp 0x1402b092f
002B0917  8B D8                           mov ebx, eax
002B0919  33 D2                           xor edx, edx
002B091B  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
002B0923  E8 48 1F 8D 00                  call 0x140b82870
002B0928  8B C3                           mov eax, ebx
002B092A  E9 81 F6 FF FF                  jmp 0x1402affb0
002B092F  41 F6 47 0A 05                  test byte ptr [r15 + 0xa], 5
002B0934  0F 84 45 01 00 00               je 0x1402b0a7f
002B093A  4D 8B 6F 18                     mov r13, qword ptr [r15 + 0x18]
002B093E  4C 89 AC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r13
002B0946  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
002B094B  4D 85 ED                        test r13, r13
002B094E  0F 85 1E EF FF FF               jne 0x1402af872
002B0954  49 8B CF                        mov rcx, r15
002B0957  E8 84 E5 FE FF                  call 0x14029eee0
002B095C  33 D2                           xor edx, edx
002B095E  49 8B CF                        mov rcx, r15
002B0961  E8 0A 1F 8D 00                  call 0x140b82870
002B0966  B8 9A 00 00 C0                  mov eax, 0xc000009a
002B096B  E9 40 F6 FF FF                  jmp 0x1402affb0
002B0970  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
002B0974  49 B9 FF FF FF FF FF FF FF 3F   movabs r9, 0x3fffffffffffffff
002B097E  49 23 C1                        and rax, r9
002B0981  48 83 F8 07                     cmp rax, 7
002B0985  0F 83 E9 02 00 00               jae 0x1402b0c74
002B098B  4D 8B 75 18                     mov r14, qword ptr [r13 + 0x18]
002B098F  4D 23 F1                        and r14, r9
002B0992  41 83 E6 07                     and r14d, 7
002B0996  49 0F BA EE 1D                  bts r14, 0x1d
002B099B  4D 03 F6                        add r14, r14
002B099E  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
002B09A3  48 83 E0 F1                     and rax, 0xfffffffffffffff1
002B09A7  4C 0B F0                        or r14, rax
002B09AA  E9 CC F1 FF FF                  jmp 0x1402afb7b
002B09AF  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
002B09B4  4D 85 FF                        test r15, r15
002B09B7  74 17                           je 0x1402b09d0
002B09B9  B2 11                           mov dl, 0x11
002B09BB  49 8B CF                        mov rcx, r15
002B09BE  E8 CD 56 F9 FF                  call 0x140246090
002B09C3  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
002B09C8  4C 89 A4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r12
002B09D0  48 85 F6                        test rsi, rsi
002B09D3  74 13                           je 0x1402b09e8
002B09D5  48 8B D6                        mov rdx, rsi
002B09D8  48 8B CB                        mov rcx, rbx
002B09DB  E8 E0 64 F6 FF                  call 0x140216ec0
002B09E0  49 8B F4                        mov rsi, r12
002B09E3  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
002B09E8  0F B6 54 24 30                  movzx edx, byte ptr [rsp + 0x30]
002B09ED  48 8B CB                        mov rcx, rbx
002B09F0  E8 9B CC FC FF                  call 0x14027d690
002B09F5  41 B2 11                        mov r10b, 0x11
002B09F8  44 88 54 24 30                  mov byte ptr [rsp + 0x30], r10b
002B09FD  E9 56 F0 FF FF                  jmp 0x1402afa58
002B0A02  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002B0A06  48 85 C0                        test rax, rax
002B0A09  0F 89 54 F3 FF FF               jns 0x1402afd63
002B0A0F  E9 9C F4 FF FF                  jmp 0x1402afeb0
002B0A14  83 CA 18                        or edx, 0x18
002B0A17  E9 DD F9 FF FF                  jmp 0x1402b03f9
002B0A1C  BE 07 00 00 00                  mov esi, 7
002B0A21  E9 57 FD FF FF                  jmp 0x1402b077d
002B0A26  49 83 FF FF                     cmp r15, -1
002B0A2A  75 07                           jne 0x1402b0a33
002B0A2C  4D 8B FC                        mov r15, r12
002B0A2F  49 83 E7 F0                     and r15, 0xfffffffffffffff0
002B0A33  4F 8D 2C 7F                     lea r13, [r15 + r15*2]
002B0A37  49 C1 E5 04                     shl r13, 4
002B0A3B  49 8B C0                        mov rax, r8
002B0A3E  4C 03 E8                        add r13, rax
002B0A41  E9 84 F2 FF FF                  jmp 0x1402afcca
002B0A46  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002B0A4B  B8 00 00 00 80                  mov eax, 0x80000000
002B0A50  4C 0B F0                        or r14, rax
002B0A53  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
002B0A58  E9 DA F2 FF FF                  jmp 0x1402afd37
002B0A5D  48 8B D3                        mov rdx, rbx
002B0A60  49 8B CF                        mov rcx, r15
002B0A63  E8 34 CE 22 00                  call 0x1404dd89c
002B0A68  E9 5B FD FF FF                  jmp 0x1402b07c8
002B0A6D  48 B8 FF FF FF FF F0 FF FF FF   movabs rax, 0xfffffff0ffffffff
002B0A77  4C 23 F0                        and r14, rax
002B0A7A  E9 8E F3 FF FF                  jmp 0x1402afe0d
002B0A7F  C7 44 24 28 10 00 00 40         mov dword ptr [rsp + 0x28], 0x40000010
002B0A87  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
002B0A8C  45 33 C9                        xor r9d, r9d
002B0A8F  33 D2                           xor edx, edx
002B0A91  45 8D 41 01                     lea r8d, [r9 + 1]
002B0A95  49 8B CF                        mov rcx, r15
002B0A98  E8 63 7D 06 00                  call 0x140318800
002B0A9D  4C 8B E8                        mov r13, rax
002B0AA0  E9 99 FE FF FF                  jmp 0x1402b093e
002B0AA5  48 85 C0                        test rax, rax
002B0AA8  0F 84 04 EF FF FF               je 0x1402af9b2
002B0AAE  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
002B0AB6  8B 80 FC 05 00 00               mov eax, dword ptr [rax + 0x5fc]
002B0ABC  A8 01                           test al, 1
002B0ABE  0F 85 EE EE FF FF               jne 0x1402af9b2
002B0AC4  83 CF 08                        or edi, 8
002B0AC7  E9 E6 EE FF FF                  jmp 0x1402af9b2
002B0ACC  83 CF 04                        or edi, 4
002B0ACF  89 7C 24 70                     mov dword ptr [rsp + 0x70], edi
002B0AD3  49 8B CF                        mov rcx, r15
002B0AD6  E8 1D 4E 82 00                  call 0x140ad58f8
002B0ADB  48 3D 00 02 00 00               cmp rax, 0x200
002B0AE1  0F 83 7F F3 FF FF               jae 0x1402afe66
002B0AE7  E9 27 EF FF FF                  jmp 0x1402afa13
002B0AEC  4D 85 DB                        test r11, r11
002B0AEF  0F 84 3A 02 00 00               je 0x1402b0d2f
002B0AF5  B2 11                           mov dl, 0x11
002B0AF7  49 8B CB                        mov rcx, r11
002B0AFA  E8 91 55 F9 FF                  call 0x140246090
002B0AFF  4D 8B FC                        mov r15, r12
002B0B02  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
002B0B07  4C 89 A4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r12
002B0B0F  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002B0B15  41 80 FA 11                     cmp r10b, 0x11
002B0B19  74 37                           je 0x1402b0b52
002B0B1B  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
002B0B20  48 85 F6                        test rsi, rsi
002B0B23  74 19                           je 0x1402b0b3e
002B0B25  48 8B D6                        mov rdx, rsi
002B0B28  49 8B CE                        mov rcx, r14
002B0B2B  E8 90 63 F6 FF                  call 0x140216ec0
002B0B30  49 8B F4                        mov rsi, r12
002B0B33  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
002B0B38  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002B0B3E  41 0F B6 D2                     movzx edx, r10b
002B0B42  49 8B CE                        mov rcx, r14
002B0B45  E8 46 CB FC FF                  call 0x14027d690
002B0B4A  41 B2 11                        mov r10b, 0x11
002B0B4D  44 88 54 24 30                  mov byte ptr [rsp + 0x30], r10b
002B0B52  0F B6 03                        movzx eax, byte ptr [rbx]
002B0B55  E9 D0 EE FF FF                  jmp 0x1402afa2a
002B0B5A  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
002B0B61  45 33 E4                        xor r12d, r12d
002B0B64  48 BA FF FF FE FF FF 7F 00 00   movabs rdx, 0x7ffffffeffff
002B0B6E  4C 8B AC 24 A8 00 00 00         mov r13, qword ptr [rsp + 0xa8]
002B0B76  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002B0B7B  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002B0B80  8B 7C 24 70                     mov edi, dword ptr [rsp + 0x70]
002B0B84  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
002B0B8C  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
002B0B94  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
002B0B9C  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
002B0BA4  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002B0BAA  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002B0BAF  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
002B0BB4  4C 8B 5C 24 40                  mov r11, qword ptr [rsp + 0x40]
002B0BB9  8B 8C 24 08 02 00 00            mov ecx, dword ptr [rsp + 0x208]
002B0BC0  E9 E4 EF FF FF                  jmp 0x1402afba9
002B0BC5  4C 8B E3                        mov r12, rbx
002B0BC8  49 C1 EC 0C                     shr r12, 0xc
002B0BCC  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
002B0BD6  4C 23 E0                        and r12, rax
002B0BD9  4D 8B FC                        mov r15, r12
002B0BDC  41 B8 FF FF FF FF               mov r8d, 0xffffffff
002B0BE2  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
002B0BEC  48 8B C1                        mov rax, rcx
002B0BEF  48 3B F0                        cmp rsi, rax
002B0BF2  72 2F                           jb 0x1402b0c23
002B0BF4  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
002B0BFE  48 8B C0                        mov rax, rax
002B0C01  48 3B F0                        cmp rsi, rax
002B0C04  77 1D                           ja 0x1402b0c23
002B0C06  48 C1 E6 19                     shl rsi, 0x19
002B0C0A  48 8B C1                        mov rax, rcx
002B0C0D  48 C1 E0 19                     shl rax, 0x19
002B0C11  48 2B F0                        sub rsi, rax
002B0C14  48 C1 FE 10                     sar rsi, 0x10
002B0C18  41 FF C0                        inc r8d
002B0C1B  48 8B C1                        mov rax, rcx
002B0C1E  48 3B F0                        cmp rsi, rax
002B0C21  73 D1                           jae 0x1402b0bf4
002B0C23  B9 01 00 00 00                  mov ecx, 1
002B0C28  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
002B0C30  45 85 C0                        test r8d, r8d
002B0C33  74 1D                           je 0x1402b0c52
002B0C35  48 8B C2                        mov rax, rdx
002B0C38  25 FF 01 00 00                  and eax, 0x1ff
002B0C3D  48 0F AF C1                     imul rax, rcx
002B0C41  4C 03 E0                        add r12, rax
002B0C44  48 C1 EA 09                     shr rdx, 9
002B0C48  48 C1 E1 09                     shl rcx, 9
002B0C4C  41 83 E8 01                     sub r8d, 1
002B0C50  75 E3                           jne 0x1402b0c35
002B0C52  41 BE 01 00 80 00               mov r14d, 0x800001
002B0C58  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
002B0C5D  E9 83 EE FF FF                  jmp 0x1402afae5
002B0C62  48 B8 FF FF FF FF F0 FF FF FF   movabs rax, 0xfffffff0ffffffff
002B0C6C  48 23 D0                        and rdx, rax
002B0C6F  E9 89 F2 FF FF                  jmp 0x1402afefd
002B0C74  41 BE 07 00 00 00               mov r14d, 7
002B0C7A  E9 13 FD FF FF                  jmp 0x1402b0992
002B0C7F  41 81 F8 00 04 00 00            cmp r8d, 0x400
002B0C86  0F 85 74 F7 FF FF               jne 0x1402b0400
002B0C8C  83 CA 08                        or edx, 8
002B0C8F  E9 6C F7 FF FF                  jmp 0x1402b0400
002B0C94  33 D2                           xor edx, edx
002B0C96  48 8B CE                        mov rcx, rsi
002B0C99  E8 52 3D 15 00                  call 0x1404049f0
002B0C9E  48 8B F0                        mov rsi, rax
002B0CA1  48 85 C0                        test rax, rax
002B0CA4  0F 85 07 F4 FF FF               jne 0x1402b00b1
002B0CAA  49 BE 00 00 00 00 00 DE FF FF   movabs r14, 0xffffde0000000000
002B0CB4  49 8B F4                        mov rsi, r12
002B0CB7  E9 19 F4 FF FF                  jmp 0x1402b00d5
002B0CBC  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002B0CC0  48 0F BA E0 28                  bt rax, 0x28
002B0CC5  0F 82 00 F4 FF FF               jb 0x1402b00cb
002B0CCB  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
002B0CCF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002B0CD4  4C 8B CB                        mov r9, rbx
002B0CD7  4D 8B C5                        mov r8, r13
002B0CDA  BA 11 04 00 00                  mov edx, 0x411
002B0CDF  B9 1A 00 00 00                  mov ecx, 0x1a
002B0CE4  E8 77 C9 24 00                  call 0x1404fd660
002B0CE9  CC                              int3
002B0CEA  8B 05 C8 5D D1 00               mov eax, dword ptr [rip + 0xd15dc8]
002B0CF0  A8 40                           test al, 0x40
002B0CF2  0F 84 A8 F5 FF FF               je 0x1402b02a0
002B0CF8  E8 93 E7 05 00                  call 0x14030f490
002B0CFD  84 C0                           test al, al
002B0CFF  0F 84 9B F5 FF FF               je 0x1402b02a0
002B0D05  41 8B CE                        mov ecx, r14d
002B0D08  E8 53 E7 05 00                  call 0x14030f460
002B0D0D  E9 90 F5 FF FF                  jmp 0x1402b02a2
002B0D12  48 83 E3 EF                     and rbx, 0xffffffffffffffef
002B0D16  E9 C2 F9 FF FF                  jmp 0x1402b06dd
002B0D1B  B8 06 02 00 C0                  mov eax, 0xc0000206
002B0D20  E9 8B F2 FF FF                  jmp 0x1402affb0
002B0D25  B8 04 00 00 C0                  mov eax, 0xc0000004
002B0D2A  E9 81 F2 FF FF                  jmp 0x1402affb0
002B0D2F  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
002B0D34  E9 DC FD FF FF                  jmp 0x1402b0b15
002B0D39  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
002B0D3E  E9 A2 ED FF FF                  jmp 0x1402afae5
002B0D43  BA 01 00 00 00                  mov edx, 1
002B0D48  E9 FE F6 FF FF                  jmp 0x1402b044b
002B0D4D  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
002B0D52  E9 48 FA FF FF                  jmp 0x1402b079f
002B0D57  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
002B0D5C  44 0F B6 54 24 30               movzx r10d, byte ptr [rsp + 0x30]
002B0D62  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
002B0D67  45 33 E4                        xor r12d, r12d
002B0D6A  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
002B0D72  4C 8B 5C 24 40                  mov r11, qword ptr [rsp + 0x40]
002B0D77  E9 49 EC FF FF                  jmp 0x1402af9c5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetWorkingSetInfoList(__int64 a1, int a2, __int64 a3, __int64 a4)
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
    unsigned __int64 v_stack_m100;
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
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m174;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int8 v_stack_m1C8;
    unsigned __int8 v_stack_m1D8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_p10;
    unsigned int v_stack_p20;
    unsigned int v_stack_p208;
    unsigned int v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned int v_stack_p80;
    unsigned int v_stack_p84;
    unsigned __int64 v_stack_p88;
    unsigned int v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;
    unsigned __int64 v_stack_pF0;
    unsigned __int64 v_stack_pF8;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (448);
    result = (*(unsigned __int64 *)(v_rip + 11906995)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m128 = a3;
    v_stack_m148 = a1;
    v_stack_m120 = a1;
    v_stack_m118 = a3;
    v_r12 = 0;
    v_stack_m198 = 0;
    v_stack_m140 = 0;
    v_stack_m100 = v_xmm0;
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    if (a4 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_002B0D1B;
    a3 = (a4) >> (4);
    v_stack_m1B0 = a3;
    if (a3 == 0) goto loc_002B0D25;
    if ((((unsigned int)((unsigned int)(a2))) & (0x3FFFFFFCULL)) != 0) goto loc_002B0129;
    result = (unsigned int)(((unsigned int)(a2)) & (3));
    if (((unsigned __int8)(result)) == 3) goto loc_002B0129;
    if (a3 > 8) goto loc_002B0875;
    a3 = (a3) << (4);
    result = memcpy(v_stack_mC8, a3, a3, a4);
    goto loc_002AF855;
loc_002AF855:
    v_stack_m138 = 0;
    v_stack_m1A8 = v_stack_mC8;
    v_stack_m150 = v_stack_mC8;
loc_002AF872:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != v_stack_m148) goto loc_002B025F;
loc_002AF887:
    v_stack_m1A0 = 0;
    v_stack_m1C0 = v_stack_m148 + 1024;
    v_stack_m1C8 = 17;
    v_stack_m180 = 0;
    v_stack_m170 = 0;
    v_stack_m178 = 0;
    v_stack_m1B8 = 0;
    goto loc_002AF8E5;
loc_002AF8E0:
loc_002AF8E5:
    v_stack_m190 = 0;
    v_rdi = (unsigned int)((0) & (0xFFFFFFF7ULL));
    v_stack_m158 = *(unsigned __int64 *)(v_stack_mC8);
    if ((*(unsigned __int64 *)(v_stack_mC8)) > a3) goto loc_002AFBA9;
    a4 = (*(unsigned __int64 *)(v_stack_mC8)) >> (12);
    v_stack_m130 = a4;
    if (0 != 0) goto loc_002AF94C;
loc_002AF919:
    result = MiObtainReferencedVadEx(*(unsigned __int64 *)(v_stack_mC8), 2, v_stack_m178, a4);
    v_stack_m1A0 = result;
    if (result == 0) goto loc_002B0329;
    goto loc_002AF983;
loc_002AF94C:
    a1 = (*(unsigned __int8 *)(result + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(result + 24)));
    if (a4 < a1) goto loc_002B02E1;
    a2 = (*(unsigned __int8 *)(result + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(result + 28)));
    if (a4 > a2) goto loc_002B02E1;
    if (result == 0) goto loc_002AF919;
loc_002AF983:
    a1 = (*(unsigned __int64 *)(v_stack_mC8)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m110 = a1;
    if (a1 == 0x7FFE0000ULL) goto loc_002B0AAE;
    if (a1 == (*(unsigned __int64 *)(v_rip + 12050895))) goto loc_002B0AA5;
loc_002AF9B2:
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFDFULL));
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(result + 48))) & (112));
    v_rdi = (unsigned int)((v_rdi) | (32));
    if (((unsigned __int8)(result)) != 16) { v_rdi = (unsigned int)((unsigned int)((unsigned int)(v_rdi))); }
loc_002AF9C5:
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFF9ULL));
    v_stack_m188 = (unsigned int)(v_rdi);
    if ((((unsigned __int8)(v_rdi)) & (32)) != 0) goto loc_002AFA13;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) & (0x200000ULL));
    if (condition_is_equal) goto loc_002AF9FB;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) >> (19));
    result = (unsigned int)((result) & (3));
    if (condition_is_below) goto loc_002B047D;
    if (((unsigned int)(result)) >= 2) goto loc_002B047D;
loc_002AF9FB:
    if (a2 == 0) goto loc_002AFE5A;
loc_002AFA03:
    result = MiPureAweVad(result, a2, v_stack_m178, a4);
    if ((unsigned int)(result) != 0) goto loc_002B0ACC;
loc_002AFA13:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (2));
    v_stack_m174 = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_002B0AEC;
loc_002AFA2A:
    v_r13 = (*(unsigned __int64 *)(v_stack_mC8)) >> (9);
    v_r13 = (v_r13) & (result);
    v_r13 = (v_r13) + (0);
    if (((unsigned __int8)(v_stack_m1C8)) != 17) goto loc_002AFC5B;
loc_002AFA58:
    v_rbx = (v_r13) >> (9);
    v_rbx = (v_rbx) & (0);
    v_rbx = (v_rbx) + (0);
    v_stack_m160 = v_rbx;
loc_002AFA7A:
    result = 0;
    if (((unsigned __int8)(v_stack_m1C8)) == 17) {
        a1 = v_stack_m1C0;
        result = MiLockWorkingSetShared(a1, a2, v_stack_m178, a4);
        v_stack_m1C8 = (unsigned __int8)(result);
    }
    v_r14 = 0;
    v_stack_m190 = 0;
    if (v_stack_m180 != v_rbx) goto loc_002AFBFC;
    v_stack_m140 = v_r13;
loc_002AFAB4:
    result = MI_READ_PTE_LOCK_FREE(v_r13, a2, v_stack_m178, a4);
    if (result == 0) goto loc_002B0177;
    result = (unsigned __int8)((result) & (129));
    if (((unsigned __int8)(result)) == 129) goto loc_002B0BC5;
    if (v_stack_m180 != v_stack_m160) goto loc_002AFE15;
loc_002AFAE5:
    if (-1 != -1) goto loc_002AFCA0;
    if (v_stack_m174 != 0) goto loc_002B0D57;
    a1 = (v_stack_m158) >> (18);
    a1 = (unsigned int)((a1) & (0x3FFFFFF8ULL));
    a1 = (a1) + (a4);
    if (v_stack_m180 != a1) goto loc_002AFB76;
    result = MI_READ_PTE_LOCK_FREE(v_r13, a2, v_stack_m178, a4);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_002AFE72;
    if (condition_is_below) goto loc_002B04F1;
    if (condition_is_below) goto loc_002AFFD4;
    if ((((unsigned __int8)(v_rdi)) & (4)) != 0) goto loc_002B0855;
loc_002AFB5C:
    result = MiGetPagingFileOffset(result, a2, v_stack_m178, a4);
    if ((unsigned int)(result) == 0) goto loc_002B014A;
loc_002AFB76:
loc_002AFB7B:
    v_r12 = 0;
loc_002AFB7E:
loc_002AFB88:
loc_002AFBA4:
loc_002AFBA9:
    if (condition_is_above_or_equal) goto loc_002AFBC7;
    if (((0) & (1)) != 0) goto loc_002AFE95;
    if (!(condition_is_above_or_equal)) {
        v_r14 = (v_r14) & (0xFFFFFFFFF03FFFFFULL);
    }
    *(unsigned __int64 *)(v_stack_m1A8 + 8) = v_r14;
    v_r13 = (v_stack_m1A8) + (16);
    v_stack_m1A8 = v_r13;
    v_stack_m150 = v_r13;
    result = (v_stack_m1B0) - (1);
    v_stack_m1B0 = result;
    if (condition_is_not_equal) goto loc_002AF8E0;
loc_002AFBEE:
    if (v_stack_m1B8 == 0) goto loc_002AFF2B;
    goto loc_002AFF21;
loc_002AFBFC:
    result = v_stack_m1B8;
    if (v_stack_m1B8 != 0) {
        a2 = 17;
        a1 = v_stack_m1B8;
        result = MiUnlockProtoPoolPage(a1, a2, v_stack_m1C0, a4);
        result = 0;
        v_stack_m1B8 = 0;
        v_stack_m170 = 0;
    }
    if (v_stack_m180 != 0) {
        a2 = v_stack_m180;
        a1 = v_stack_m1C0;
        result = MiUnlockPageTable(a1, a2, v_stack_m1C0, a4);
    }
    a4 = 0;
    result = MiLockLowestValidPageTableEx(v_stack_m1C0, v_r13, v_stack_m140, a4);
    v_stack_m180 = result;
    goto loc_002AFAB4;
loc_002AFC5B:
    if ((((unsigned __int8)(v_r13 + 8)) & (120)) == 0) goto loc_002B02C5;
loc_002AFC67:
    result = KeShouldYieldProcessor(v_stack_m1C0, v_r13, v_stack_m140, a4);
    if ((unsigned int)(result) != 0) goto loc_002B09AF;
    goto loc_002AFA58;
loc_002AFC7F:
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFEFULL));
loc_002AFC82:
    v_r12 = (0) >> (12);
    v_r12 = (v_r12) & (result);
    if ((((unsigned __int8)(v_rdi)) & (48)) != 0) goto loc_002B036D;
loc_002AFCA0:
    v_rsi = (v_r12 + v_r12 * 2) << (4);
    v_rsi = (v_rsi) + (v_stack_m140);
    if (condition_is_below) goto loc_002B0A26;
loc_002AFCCA:
    result = MiGetPfnPriority(v_rsi, v_r13, v_stack_m140, a4);
    result = MI_NODE_FROM_PFN(v_rsi, v_r13, v_stack_m140, a4);
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (7));
    v_r15 = (v_r15) << (8);
    result = (unsigned int)((result) & (63));
    v_r15 = (v_r15) | (result);
    v_r15 = (v_r15) << (16);
    v_r14 = (*(unsigned __int64 *)(v_rsi + 40)) >> (48);
    v_r14 = (unsigned int)((v_r14) & (0x8000ULL));
    v_r15 = (v_r15) | (v_r14);
    result = (v_stack_m190) & (0xFFFFFFFFF8C07FFFULL);
    v_r15 = (v_r15) | (result);
    v_stack_m190 = v_r15;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_002B0A46;
    result = MiIsPageOnBadList(v_rsi, v_r13, v_stack_m140, a4);
    if ((unsigned int)(result) != 0) goto loc_002B0A46;
loc_002AFD37:
    if (condition_is_below) goto loc_002AFEB5;
    if (condition_is_below) goto loc_002AFEB0;
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 1) goto loc_002B0A02;
loc_002AFD63:
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 1) goto loc_002B07A9;
    result = MiGetWsleContents(v_rsi, v_stack_m158, v_stack_m140, a4);
    result = (unsigned __int8)((result) & (15));
    if (((unsigned __int8)(result)) == 8) goto loc_002B0133;
loc_002AFD8F:
    if (sign_flag) goto loc_002B0196;
    result = ((unsigned int)(*(unsigned int *)(v_rsi + 16))) >> (5);
    result = (unsigned int)((result) & (31));
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 2817453 + result * 4 + 83504))) & (0x7FFULL));
    v_r14 = (v_r14) << (4);
    result = (v_stack_m190) & (0xFFFFFFFFFFFF8001ULL);
    v_r14 = (v_r14) | (result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1A0 + 48))) & (0x4200000ULL));
    if (((unsigned int)(result)) == 0x4200000ULL) goto loc_002B0A6D;
loc_002AFE0D:
    v_r12 = 0;
    goto loc_002AFBA4;
loc_002AFE15:
    v_stack_m1D8 = (unsigned __int8)(v_stack_m1C8);
    result = MiWorkingSetInfoCheckPageTable(v_stack_m1C0, v_rsi, v_stack_m198, (unsigned int)(v_stack_p10));
    if ((unsigned int)(result) == 0) goto loc_002B0D39;
    v_rsi = 0;
    v_stack_m180 = 0;
    goto loc_002AFA7A;
loc_002AFE5A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1A0 + 64)))) & (1)) == 0) goto loc_002AFA03;
loc_002AFE66:
    v_rdi = (unsigned int)((v_rdi) | (2));
    v_stack_m188 = (unsigned int)(v_rdi);
    goto loc_002AFA13;
loc_002AFE72:
    v_r14 = (v_r14) | (1);
    v_stack_m190 = v_r14;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_m1A0 + 48))) & (112));
    if (((unsigned __int8)(result)) != 64) goto loc_002AFC7F;
    v_rdi = (unsigned int)((v_rdi) | (16));
    goto loc_002AFC82;
loc_002AFE95:
    if (condition_is_above_or_equal) goto loc_002AFBC7;
    v_r14 = (v_r14) & (0xFFFFFFFFF8C0FFFFULL);
    v_r14 = (v_r14) | (14);
    goto loc_002AFBC7;
loc_002AFEB0:
loc_002AFEB5:
    result = MiGetProtectionFromPte(v_stack_m1A0, v_stack_m160, v_stack_m198, (unsigned int)(v_stack_p10));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 2817742 + (unsigned int)((unsigned int)(result)) * 4 + 83504))) & (0x7FFULL));
    a2 = (a2) << (4);
    v_r14 = (v_stack_m190) & (0xFFFFFFFFFFFF800FULL);
    a2 = (a2) | (v_r14);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1A0 + 48))) & (0x4200000ULL));
    if (((unsigned int)(result)) == 0x4200000ULL) goto loc_002B0C62;
loc_002AFEFD:
    v_stack_m190 = a2;
    if (sign_flag) goto loc_002B0970;
loc_002AFF14:
    v_r12 = 0;
loc_002AFF17:
    goto loc_002AFB7E;
loc_002AFF21:
    result = MiUnlockProtoPoolPage(v_stack_m1B8, 17, v_stack_m198, (unsigned int)(v_stack_p10));
loc_002AFF2B:
    if (((unsigned __int8)(v_stack_m1C8)) == 17) goto loc_002AFF5B;
    result = v_stack_m180;
    if (v_stack_m180 != 0) {
        a2 = v_stack_m180;
        a1 = v_stack_m1C0;
        result = MiUnlockPageTable(a1, a2, v_stack_m198, (unsigned int)(v_stack_p10));
    }
    result = MiUnlockWorkingSetShared(v_stack_m1C0, (unsigned __int8)(v_stack_m1C8), v_stack_m198, (unsigned int)(v_stack_p10));
loc_002AFF5B:
    if (v_stack_m1A0 != 0) {
        a1 = v_stack_m1A0;
        result = MiUnlockAndDereferenceVadShared(a1, (unsigned __int8)(v_stack_m1C8), v_stack_m198, (unsigned int)(v_stack_p10));
    }
    if ((((unsigned __int8)(v_rdi)) & (1)) != 0) goto loc_002B02B1;
loc_002AFF72:
    if (v_stack_m138 != 0) goto loc_002B06E6;
    v_r13 = (v_stack_m1A8) - (v_stack_mC8);
    v_r13 = (v_r13) & (-16);
    result = memcpy(v_stack_m128, v_stack_mC8, v_r13, (unsigned int)(v_stack_p10));
    goto loc_002AFFAE;
loc_002AFFAE:
loc_002AFFB0:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_mC8, v_r13, (unsigned int)(v_stack_p10));
    v_rsp = (v_rsp) + (448);
    return result;
loc_002AFFD4:
    v_r12 = 0;
loc_002AFFD7:
loc_002AFFE1:
    result = MI_READ_PTE_LOCK_FREE(v_r13, v_stack_mC8, v_r13, (unsigned int)(v_stack_p10));
    if (condition_is_above_or_equal) goto loc_002B0CB4;
    result = MiInvalidPteConforms(result, v_stack_mC8, v_r13, (unsigned int)(v_stack_p10));
    if ((unsigned int)(result) == 0) goto loc_002AFFE1;
    if (*(unsigned __int64 *)(v_rip + 12049526) == 0) goto loc_002B0021;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_002B0141;
    a1 = ~(*(unsigned __int64 *)(v_rip + 12049526));
    a1 = (a1) & (result);
loc_002B0021:
    a1 = (a1) >> (12);
    a1 = (a1) & (*(unsigned __int64 *)(v_rip + 12049526));
    a2 = (a1 + a1 * 2) + (a1 + a1 * 2);
    if (a1 > (*(unsigned __int64 *)(v_rip + 12049561))) goto loc_002AFFE1;
    result = (*(unsigned __int64 *)(v_stack_m190 + a2 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_002AFFE1;
    v_stack_p90 = 0;
loc_002B0070:
    if (condition_is_below) goto loc_002B0280;
    result = MI_READ_PTE_LOCK_FREE(v_r13, a2, v_r13, (unsigned int)(v_stack_p10));
    if (result != result) goto loc_002B0359;
    result = (*(unsigned __int64 *)(v_stack_m190 + a2 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_002B0C94;
loc_002B00B1:
    result = (*(unsigned __int64 *)(v_stack_m190 + a2 * 8 + 8)) | (v_r13);
    if (result != v_r13) goto loc_002B0CBC;
loc_002B00CB:
loc_002B00D5:
    if (v_stack_m190 + a2 * 8 == 0) goto loc_002B0341;
    result = MI_READ_PTE_LOCK_FREE(v_r13, *(unsigned __int64 *)(v_rip + 12058598), v_r13, (unsigned int)(v_stack_p10));
    a1 = (v_stack_m190 + a2 * 8) - (v_stack_m190);
    a1 = (a1) >> (4);
    a1 = (a1) * (v_stack_m190);
    result = MiQueryPfn(a1, v_stack_p60, v_r13, (unsigned int)(v_stack_p10));
    goto loc_002AFB7E;
loc_002B0129:
    goto loc_002AFFB0;
loc_002B0133:
    goto loc_002AFD8F;
loc_002B0141:
    a1 = (a1) & (-17);
    goto loc_002B0021;
loc_002B014A:
    if (result != 0) goto loc_002AFB76;
loc_002B0153:
    a1 = (((*(unsigned int *)(v_stack_p58 + 48)) & (0x200000ULL)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(v_stack_m138)) & (8)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_002AFB7B;
    goto loc_002B04F6;
loc_002B0177:
    if ((((unsigned __int8)(v_stack_m138)) & (32)) != 0) goto loc_002AFB76;
    if (v_stack_p84 != ((unsigned int)(v_stack_p68))) goto loc_002AFAE5;
    goto loc_002B0153;
loc_002B0196:
    result = (*(unsigned __int64 *)(v_stack_p78 + 24)) & (a1);
    if (result >= 7) goto loc_002B031F;
    v_rbx = (*(unsigned __int64 *)(v_stack_p78 + 24)) & (a1);
loc_002B01B8:
    result = MiGetPfnProtection(a1, v_stack_m1C8, v_stack_p78, (unsigned int)(v_stack_p10));
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 2818508 + (unsigned int)((unsigned int)(result)) * 4 + 83504))) & (0x7FFULL));
    v_r14 = (v_r14) << (3);
    v_rbx = (unsigned int)((v_rbx) & (7));
    v_r14 = (v_r14) | (v_rbx);
    v_r14 = (v_r14) + (v_r14);
    result = (v_stack_p68) & (0xFFFFFFFFFFFF8001ULL);
    v_r14 = (v_r14) | (result);
    v_stack_p68 = v_r14;
    if ((((unsigned __int8)(v_stack_m138)) & (8)) != 0) goto loc_002B084B;
    if (((*(unsigned int *)(v_stack_p58 + 48)) & (0x200000ULL)) != 0) goto loc_002AFB7B;
    result = MiGetProtoPteAddress(v_stack_p58, v_stack_pC8, 8, v_stack_pF0);
    a1 = (*(unsigned __int64 *)(v_stack_p78 + 8)) | (v_stack_pC8);
    if (result != a1) goto loc_002AFF14;
    goto loc_002AFB7B;
loc_002B025F:
    a2 = 0;
    result = KiStackAttachProcess(v_rbx, a2, v_stack_pF8, v_stack_pF0);
    goto loc_002AF887;
loc_002B0280:
    v_r14 = (unsigned int)(((unsigned int)(v_stack_p90)) + 1);
    v_stack_p90 = (unsigned int)(v_r14);
    if (((*(unsigned int *)(v_rip + 13717522)) & ((unsigned int)(v_r14))) == 0) goto loc_002B0CEA;
loc_002B02A0:
loc_002B02A2:
    if (!sign_flag) goto loc_002B0070;
    goto loc_002B0280;
loc_002B02B1:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF8, a2, v_stack_pF8, v_stack_pF0);
    goto loc_002AFF72;
loc_002B02C5:
    a2 = 0;
    result = MiWorkingSetIsContended(v_stack_p38, a2, v_stack_pF8, v_stack_pF0);
    if ((unsigned int)(result) == 0) goto loc_002AFC67;
    goto loc_002B09B4;
loc_002B02E1:
    v_r10 = v_stack_m1C8;
    if (v_stack_m1B8 != 0) {
        a2 = 17;
        a1 = v_stack_m1B8;
        result = MiUnlockProtoPoolPage(a1, a2, v_stack_pF8, v_stack_pF0);
        v_stack_p40 = 0;
        v_stack_p88 = 0;
        v_r10 = v_stack_p30;
        a3 = v_stack_p38;
    }
    if (((unsigned __int8)(v_r10)) != 17) goto loc_002B048B;
loc_002B0312:
    result = MiUnlockAndDereferenceVadShared(v_stack_p58, a2, a3, v_stack_pF0);
    goto loc_002AF919;
loc_002B031F:
    goto loc_002B01B8;
loc_002B0329:
    if (((unsigned int)((unsigned int)(v_stack_p80))) != 0xC000010AULL) goto loc_002AFB88;
    goto loc_002AFBEE;
loc_002B0341:
    goto loc_002AFA7A;
loc_002B0359:
    goto loc_002AFFD7;
loc_002B036D:
    result = MiPageToNode(0, a2, a3, v_stack_pF0);
    a1 = (v_r12 + v_r12 * 2) + (v_r12 + v_r12 * 2);
    if (0 > (*(unsigned __int64 *)(v_rip + 12048714))) goto loc_002B03BC;
    a1 = (*(unsigned __int64 *)(a3 + a1 * 8)) >> (54);
    if (condition_is_below) goto loc_002B04C4;
loc_002B03B7:
loc_002B03BC:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) & (63));
    v_rsi = (v_rsi) << (16);
    v_r14 = (v_stack_p68) & (0xFFFFFFFFFFC0FFFFULL);
    v_rsi = (v_rsi) | (v_r14);
    if (((1) & (32)) == 0) goto loc_002B042B;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p58 + 48))) >> (7));
    a2 = (unsigned int)((a2) & (31));
    result = (unsigned __int8)(((unsigned __int8)(v_stack_p98)) & (24));
    if (((unsigned __int8)(result)) == 8) goto loc_002B0A14;
    if ((((unsigned __int8)(v_stack_p98)) & (16)) != 0) {
        a2 = (unsigned int)((a2) | (8));
    }
    v_rsi = (v_rsi) | (0x400001ULL);
loc_002B0400:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 2819081 + (unsigned int)(a2) * 4 + 83504))) & (0x7FFULL));
    v_r14 = (v_r14) << (4);
    v_rsi = (v_rsi) & (0xFFFFFFFFFFFF800FULL);
    v_r14 = (v_r14) | (v_rsi);
    goto loc_002AFB7B;
loc_002B042B:
    result = MiRotatedToFrameBuffer(v_r13, v_rip - 2819081, a3, v_stack_pF0);
    if ((unsigned int)(result) == 0) goto loc_002B06FD;
    if (condition_is_above_or_equal) goto loc_002B0D43;
loc_002B044B:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 48))))) & (0xC00ULL));
    a1 = ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p58 + 48)))) & (896)) != 0) ? 1 : 0;
    result = (((unsigned int)(a3)) == 0xC00ULL) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_002B0C7F;
    a2 = (unsigned int)((4) | (24));
    goto loc_002B0400;
loc_002B047D:
    if (((unsigned int)(result)) >= 2) goto loc_002AFE66;
    goto loc_002AF9FB;
loc_002B048B:
    v_r10 = v_stack_p30;
    if (v_rsi != 0) {
        a2 = v_rsi;
        a1 = a3;
        result = MiUnlockPageTable(a1, a2, a3, v_stack_pF0);
        v_rsi = 0;
        v_stack_p78 = 0;
        v_r10 = v_stack_p30;
        a3 = v_stack_p38;
    }
    result = MiUnlockWorkingSetShared(a3, (unsigned __int8)(v_r10), a3, v_stack_pF0);
    v_stack_p30 = 17;
    goto loc_002B0312;
loc_002B04C4:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p58 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_002B04DF;
    result = MiIsPageOnBadList(v_stack_p58, (unsigned __int8)(v_r10), a3, v_stack_pF0);
    if ((unsigned int)(result) == 0) goto loc_002B03B7;
loc_002B04DF:
    v_r14 = (v_stack_p68) | ((unsigned int)(0x80000000ULL));
    goto loc_002B03BC;
loc_002B04F1:
loc_002B04F6:
    v_r12 = 0;
    if (((1) & (8)) != 0) goto loc_002B067E;
    if (((*(unsigned int *)(v_stack_p58 + 48)) & (0x200000ULL)) != 0) goto loc_002B06C2;
    a2 = (v_stack_pA0) >> (12);
    result = MiGetProtoPteAddress(v_stack_p58, a2, v_r12 + 8, v_stack_pF0);
    if (v_stack_p98 != 0) goto loc_002B06B2;
loc_002B0541:
loc_002B0544:
    if (result == 0) goto loc_002AFB7E;
    v_stack_p68 = v_r14;
    if (result == result) {
        v_stack_p68 = v_r14;
    }
    result = (v_stack_p88) ^ (result);
    if (((result) & (0xFFFFFFFFFFFFF000ULL)) == 0) goto loc_002B05B1;
    result = v_stack_p40;
    if (v_stack_p40 != 0) {
        a2 = 17;
        a1 = v_stack_p40;
        result = MiUnlockProtoPoolPage(a1, a2, result, v_stack_pF0);
        v_stack_p88 = 0;
    }
    a2 = 0;
    result = MiLockProtoPoolPage(result, a2, result, v_stack_pF0);
    v_stack_p40 = result;
    if (result == 0) goto loc_002B0601;
    v_stack_p88 = result;
loc_002B05B1:
    a2 = 0;
    result = MiLockLeafPage(result, a2, result, v_stack_pF0);
    if (result != 0) goto loc_002B0636;
    if (((*(unsigned __int64 *)(result)) & (0xC00ULL)) != 0) goto loc_002AFF17;
    result = MiInvalidPteConforms(*(unsigned __int64 *)(result), *(unsigned __int64 *)(result), result, v_stack_pF0);
    if ((unsigned int)(result) == 0) goto loc_002AFF17;
    result = MiGetPagingFileOffset(*(unsigned __int64 *)(result), *(unsigned __int64 *)(result), result, v_stack_pF0);
    if ((unsigned int)(result) != 0) goto loc_002B069E;
    if (*(unsigned __int64 *)(result) != 0) goto loc_002AFF17;
    goto loc_002AFB7E;
loc_002B0601:
    if (((unsigned __int8)(v_stack_p30)) != 17) goto loc_002B0819;
loc_002B0611:
    a4 = 0;
    a3 = 0;
    result = MmAccessFault(a4 + 2, result, a3, a4);
    goto loc_002AFA7A;
loc_002B0636:
    a1 = (result) - (0);
    a1 = (a1) >> (4);
    a1 = (a1) * (result);
    result = MiQueryPfn(a1, v_stack_p60, a3, a4);
    goto loc_002AFB7E;
loc_002B067E:
    a3 = *(unsigned __int64 *)(v_rip + 12047595);
    if (v_stack_pE8 == 0x7FFE0000ULL) { a3 = *(unsigned __int64 *)(v_rip + 12047567); }
    goto loc_002B0541;
loc_002B069E:
    goto loc_002AFB7E;
loc_002B06B2:
    result = MiIsPrototypePteVadLookup(v_stack_p98, v_stack_p60, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_002B0541;
loc_002B06C2:
    if (*(unsigned __int64 *)(v_rip + 12047799) == 0) goto loc_002B06DD;
    if ((((unsigned __int8)(v_stack_p98)) & (16)) != 0) goto loc_002B0D12;
    result = ~(*(unsigned __int64 *)(v_rip + 12047799));
    v_rbx = (v_stack_p98) & (result);
loc_002B06DD:
    v_rbx = (v_rbx) >> (16);
    goto loc_002B0544;
loc_002B06E6:
    result = MmUnlockPages(1, v_stack_p60, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(1, a2, a3, a4);
    goto loc_002AFFAE;
loc_002B06FD:
    result = MiGetPfnPriority(v_stack_p58, a2, a3, a4);
    v_r10 = ((unsigned int)((unsigned int)(result))) << (24);
    v_rsi = (result) ^ (v_r10);
    v_rsi = (v_rsi) & (0xFFFFFFFFF8FFFFFFULL);
    v_rsi = (v_rsi) ^ (v_r10);
    v_stack_p68 = v_rsi;
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_p58 + 16))) >> (5);
    a2 = (unsigned int)((a2) & (31));
    if (condition_is_below) goto loc_002B0D4D;
    if (sign_flag) goto loc_002B0D4D;
    if (*(unsigned __int64 *)(v_stack_p58 + 8) == 0) goto loc_002B0D4D;
    result = (*(unsigned __int64 *)(v_stack_p58 + 24)) & (v_stack_p58);
    if (result >= 7) goto loc_002B0A1C;
    v_rsi = (*(unsigned __int64 *)(v_stack_p58 + 24)) & (v_stack_p58);
loc_002B077D:
    v_rsi = (unsigned int)((v_rsi) & (7));
    v_rsi = (v_rsi) + (v_rsi);
    result = (v_stack_p68) & (-15);
    v_rsi = (v_rsi) | (result);
loc_002B079F:
    goto loc_002B0400;
loc_002B07A9:
    result = MiIsPfnEnclave(v_rsi, (unsigned int)(*(unsigned int *)(v_rip - 2819992 + (unsigned int)(a2) * 4 + 69744)), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_002B0A5D;
    result = ((unsigned int)(*(unsigned int *)(v_rsi + 16))) >> (5);
    result = (unsigned int)((result) & (31));
loc_002B07C8:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip - 2820049 + (unsigned int)((unsigned int)(result)) * 4 + 83504))) & (0x7FFULL));
    v_r14 = (v_r14) << (4);
    result = (v_stack_p68) & (0xFFFFFFFFFFFF800FULL);
    v_r14 = (v_r14) | (result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p58 + 48))) & (0x4200000ULL));
    if (((unsigned int)(result)) == 0x4200000ULL) {
        v_r14 = (v_r14) & (result);
    }
    goto loc_002AFB7B;
loc_002B0819:
    if (v_rsi != 0) {
        a2 = v_rsi;
        a1 = v_stack_p38;
        result = MiUnlockPageTable(a1, a2, a3, a4);
        v_rsi = 0;
        v_stack_p78 = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_p38, (unsigned __int8)(v_r14), a3, a4);
    v_stack_p30 = 17;
    goto loc_002B0611;
loc_002B084B:
    goto loc_002AFB7B;
loc_002B0855:
    result = MiIsLazyStampedPte(v_rbx, (unsigned __int8)(v_r14), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_002AFB5C;
    v_r12 = 0;
    goto loc_002AFB7E;
loc_002B0875:
    a2 = (((v_rbx) & (0xFFFULL)) != 0) ? 1 : 0;
    a2 = (a2) + (7);
    result = (v_rbx) >> (12);
    a2 = (a2) + (result);
    a2 = (a2) << (3);
    result = MiAllocatePool(64, a2, (unsigned int)(0x20206D4DULL), a4);
    v_stack_pC0 = result;
    if (result == 0) goto loc_002B0966;
    *(unsigned __int64 *)(result) = 0;
    a1 = (unsigned int)((0) & (0xFFFULL));
    a1 = (a1) + (0xFFFULL);
    a1 = (a1) + (v_rbx);
    a1 = (a1) >> (12);
    a1 = (unsigned __int16)((a1) + (6));
    a1 = (unsigned __int16)((a1) << (3));
    *(unsigned __int16 *)(result + 8) = (unsigned __int16)(a1);
    *(unsigned __int16 *)(result + 10) = 0;
    result = (0) & (0xFFFFFFFFFFFFF000ULL);
    *(unsigned __int64 *)(result + 32) = result;
    a2 = (unsigned int)((0) & (0xFFFULL));
    *(unsigned int *)(result + 44) = a2;
    *(unsigned int *)(result + 40) = (unsigned int)(v_rbx);
    result = MmProbeAndLockPages(result, *(unsigned __int8 *)(v_rsi + 562), 1, a4);
    goto loc_002B092F;
loc_002B092F:
    if (((*(unsigned __int8 *)(result + 10)) & (5)) == 0) goto loc_002B0A7F;
loc_002B093E:
    v_stack_pA8 = *(unsigned __int64 *)(result + 24);
    v_stack_p50 = *(unsigned __int64 *)(result + 24);
    if (*(unsigned __int64 *)(result + 24) != 0) goto loc_002AF872;
    result = MmUnlockPages(result, *(unsigned __int8 *)(v_rsi + 562), 1, a4);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 1, a4);
loc_002B0966:
    goto loc_002AFFB0;
loc_002B0970:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 24)) & (0);
    if (result >= 7) goto loc_002B0C74;
    v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 24)) & (0);
loc_002B0992:
    v_r14 = (unsigned int)((v_r14) & (7));
    v_r14 = (v_r14) + (v_r14);
    result = (v_stack_p68) & (-15);
    v_r14 = (v_r14) | (result);
    goto loc_002AFB7B;
loc_002B09AF:
loc_002B09B4:
    if (result != 0) {
        a2 = 17;
        a1 = result;
        result = MiUnlockProtoPoolPage(a1, a2, 1, a4);
        v_stack_p40 = 0;
        v_stack_p88 = 0;
    }
    if (v_rsi != 0) {
        a2 = v_rsi;
        a1 = v_stack_p38;
        result = MiUnlockPageTable(a1, a2, 1, a4);
        v_rsi = 0;
        v_stack_p78 = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_p38, v_stack_p30, 1, a4);
    v_stack_p30 = 17;
    goto loc_002AFA58;
loc_002B0A02:
    if (!sign_flag) goto loc_002AFD63;
    goto loc_002AFEB0;
loc_002B0A14:
    a2 = (unsigned int)((v_stack_p30) | (24));
    goto loc_002B03F9;
loc_002B0A1C:
    goto loc_002B077D;
loc_002B0A26:
    v_r15 = result;
    if (result == -1) {
        v_r15 = 0;
        v_r15 = (v_r15) & (-16);
    }
    v_r13 = (v_r15 + v_r15 * 2) << (4);
    v_r13 = (v_r13) + (1);
    goto loc_002AFCCA;
loc_002B0A46:
    v_r14 = (v_stack_p68) | ((unsigned int)(0x80000000ULL));
    v_stack_p68 = v_r14;
    goto loc_002AFD37;
loc_002B0A5D:
    result = MiGetValidAweProtection(v_r15, v_stack_p38, 1, a4);
    goto loc_002B07C8;
loc_002B0A6D:
    v_r14 = (v_r14) & (result);
    goto loc_002AFE0D;
loc_002B0A7F:
    v_stack_p28 = 0x40000010ULL;
    v_stack_p20 = 0;
    a4 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(v_r15, a2, a4 + 1, a4);
    goto loc_002B093E;
loc_002B0AA5:
    if (result == 0) goto loc_002AF9B2;
loc_002B0AAE:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_pB0 + 1532)))) & (1)) != 0) goto loc_002AF9B2;
    v_rdi = (unsigned int)((1) | (8));
    goto loc_002AF9B2;
loc_002B0ACC:
    v_rdi = (unsigned int)((v_rdi) | (4));
    v_stack_p70 = (unsigned int)(v_rdi);
    result = MiGetAweVadPageSize(v_r15, a2, a4 + 1, a4);
    if (result >= 512) goto loc_002AFE66;
    goto loc_002AFA13;
loc_002B0AEC:
    if (v_stack_m1B8 == 0) goto loc_002B0D2F;
    result = MiUnlockProtoPoolPage(v_stack_m1B8, 17, a4 + 1, a4);
    v_stack_p40 = 0;
    v_stack_p88 = 0;
loc_002B0B15:
    if (((unsigned __int8)(v_stack_p30)) == 17) goto loc_002B0B52;
    v_rsi = 7;
    v_r10 = v_stack_p30;
    if (7 != 0) {
        a2 = 7;
        a1 = v_stack_p38;
        result = MiUnlockPageTable(a1, a2, a4 + 1, a4);
        v_rsi = 0;
        v_stack_p78 = 0;
        v_r10 = v_stack_p30;
    }
    result = MiUnlockWorkingSetShared(v_stack_p38, (unsigned __int8)(v_r10), a4 + 1, a4);
    v_stack_p30 = 17;
loc_002B0B52:
    goto loc_002AFA2A;
loc_002B0BC5:
    v_r12 = (v_stack_p38) >> (12);
    v_r12 = (v_r12) & (*(unsigned __int8 *)(v_stack_p38));
    if (v_rsi < v_stack_p38) goto loc_002B0C23;
loc_002B0BF4:
    if (v_rsi > v_stack_p38) goto loc_002B0C23;
    v_rsi = (v_rsi) << (25);
    result = (v_stack_p38) << (25);
    v_rsi = (v_rsi) - (result);
    v_rsi = (v_rsi) >> (16);
    a3 = (unsigned int)(((unsigned int)(0xFFFFFFFFULL)) + 1);
    if (v_rsi >= v_stack_p38) goto loc_002B0BF4;
loc_002B0C23:
    if ((unsigned int)(a3) == 0) goto loc_002B0C52;
loc_002B0C35:
    result = (unsigned int)((v_stack_pC8) & (511));
    result = (result) * (1);
    v_r12 = (v_r12) + (result);
    a2 = (v_stack_pC8) >> (9);
    a1 = (1) << (9);
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_not_equal) goto loc_002B0C35;
loc_002B0C52:
    v_stack_p68 = (unsigned int)(0x800001ULL);
    goto loc_002AFAE5;
loc_002B0C62:
    a2 = (a2) & (result);
    goto loc_002AFEFD;
loc_002B0C74:
    goto loc_002B0992;
loc_002B0C7F:
    if (((unsigned int)(a3)) != 0x400ULL) goto loc_002B0400;
    a2 = (unsigned int)((a2) | (8));
    goto loc_002B0400;
loc_002B0C94:
    a2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(v_rsi, a2, a3, a4);
    if (result != 0) goto loc_002B00B1;
loc_002B0CB4:
    goto loc_002B00D5;
loc_002B0CBC:
    if (condition_is_below) goto loc_002B00CB;
    v_stack_p20 = *(unsigned __int64 *)(v_r12 + 8);
    result = KeBugCheckEx(26, (unsigned int)(0x411ULL), result, v_stack_p38);
loc_002B0CEA:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13721032)))) & (64)) == 0) goto loc_002B02A0;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (unsigned int)(0x411ULL), result, v_stack_p38);
    if ((unsigned __int8)(result) == 0) goto loc_002B02A0;
    result = HvlNotifyLongSpinWait(7, (unsigned int)(0x411ULL), result, v_stack_p38);
    goto loc_002B02A2;
loc_002B0D12:
    v_rbx = (v_stack_p38) & (-17);
    goto loc_002B06DD;
loc_002B0D1B:
    goto loc_002AFFB0;
loc_002B0D25:
    goto loc_002AFFB0;
loc_002B0D2F:
    goto loc_002B0B15;
loc_002B0D39:
    goto loc_002AFAE5;
loc_002B0D43:
    goto loc_002B044B;
loc_002B0D4D:
    goto loc_002B079F;
loc_002B0D57:
    v_r12 = 0;
    goto loc_002AF9C5;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetWorkingSetInfoList(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
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
    uint64_t v_stack_m100;
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
    uint64_t v_stack_m170;
    uint32_t v_stack_m174;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint8_t v_stack_m1C8;
    uint8_t v_stack_m1D8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;
    uint32_t v_stack_p10;
    uint32_t v_stack_p20;
    uint32_t v_stack_p208;
    uint32_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;
    uint32_t v_stack_p80;
    uint32_t v_stack_p84;
    uint64_t v_stack_p88;
    uint32_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;
    uint64_t v_stack_pF0;
    uint64_t v_stack_pF8;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (448);
    result = (*(uint64_t *)(v_rip + 0xB5AFB3)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m128 = Arg3;
    v_stack_m148 = Arg1;
    v_stack_m120 = Arg1;
    v_stack_m118 = Arg3;
    local_r12 = 0;
    v_stack_m198 = 0;
    v_stack_m140 = 0;
    v_stack_m100 = v_xmm0;
    v_stack_mF0 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    if (Arg4 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_002B0D1B;
    Arg3 = (Arg4) >> (4);
    v_stack_m1B0 = Arg3;
    if (Arg3 == 0) goto loc_002B0D25;
    if ((((uint32_t)((uint32_t)(Arg2))) & (0x3FFFFFFCULL)) != 0) goto loc_002B0129;
    result = (uint32_t)(((uint32_t)(Arg2)) & (3));
    if (((uint8_t)(result)) == 3) goto loc_002B0129;
    if (Arg3 > 8) goto loc_002B0875;
    Arg3 = (Arg3) << (4);
    result = memcpy(v_stack_mC8, Arg3, Arg3, Arg4);
    goto loc_002AF855;
loc_002AF855:
    v_stack_m138 = 0;
    v_stack_m1A8 = v_stack_mC8;
    v_stack_m150 = v_stack_mC8;
loc_002AF872:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != v_stack_m148) goto loc_002B025F;
loc_002AF887:
    v_stack_m1A0 = 0;
    v_stack_m1C0 = v_stack_m148 + 1024;
    v_stack_m1C8 = 17;
    v_stack_m180 = 0;
    v_stack_m170 = 0;
    v_stack_m178 = 0;
    v_stack_m1B8 = 0;
    goto loc_002AF8E5;
loc_002AF8E0:
loc_002AF8E5:
    v_stack_m190 = 0;
    local_rdi = (uint32_t)((0) & (0xFFFFFFF7ULL));
    v_stack_m158 = *(uint64_t *)(v_stack_mC8);
    if ((*(uint64_t *)(v_stack_mC8)) > Arg3) goto loc_002AFBA9;
    Arg4 = (*(uint64_t *)(v_stack_mC8)) >> (12);
    v_stack_m130 = Arg4;
    if (0 != 0) goto loc_002AF94C;
loc_002AF919:
    result = MiObtainReferencedVadEx(*(uint64_t *)(v_stack_mC8), 2, v_stack_m178, Arg4);
    v_stack_m1A0 = result;
    if (result == 0) goto loc_002B0329;
    goto loc_002AF983;
loc_002AF94C:
    Arg1 = (*(uint8_t *)(result + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(result + 0x18)));
    if (Arg4 < Arg1) goto loc_002B02E1;
    Arg2 = (*(uint8_t *)(result + 0x21)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    if (Arg4 > Arg2) goto loc_002B02E1;
    if (result == 0) goto loc_002AF919;
loc_002AF983:
    Arg1 = (*(uint64_t *)(v_stack_mC8)) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m110 = Arg1;
    if (Arg1 == 0x7FFE0000ULL) goto loc_002B0AAE;
    if (Arg1 == (*(uint64_t *)(v_rip + 0xB7E1CF))) goto loc_002B0AA5;
loc_002AF9B2:
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFDFULL));
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (112));
    local_rdi = (uint32_t)((local_rdi) | (32));
    if (((uint8_t)(result)) != 16) { local_rdi = (uint32_t)((uint32_t)((uint32_t)(local_rdi))); }
loc_002AF9C5:
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFF9ULL));
    v_stack_m188 = (uint32_t)(local_rdi);
    if ((((uint8_t)(local_rdi)) & (32)) != 0) goto loc_002AFA13;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) & (0x200000ULL));
    if (condition_is_equal) goto loc_002AF9FB;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) >> (19));
    result = (uint32_t)((result) & (3));
    if (condition_is_below) goto loc_002B047D;
    if (((uint32_t)(result)) >= 2) goto loc_002B047D;
loc_002AF9FB:
    if (Arg2 == 0) goto loc_002AFE5A;
loc_002AFA03:
    result = MiPureAweVad(result, Arg2, v_stack_m178, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002B0ACC;
loc_002AFA13:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (2));
    v_stack_m174 = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_002B0AEC;
loc_002AFA2A:
    local_r13 = (*(uint64_t *)(v_stack_mC8)) >> (9);
    local_r13 = (local_r13) & (result);
    local_r13 = (local_r13) + (0);
    if (((uint8_t)(v_stack_m1C8)) != 17) goto loc_002AFC5B;
loc_002AFA58:
    local_rbx = (local_r13) >> (9);
    local_rbx = (local_rbx) & (0);
    local_rbx = (local_rbx) + (0);
    v_stack_m160 = local_rbx;
loc_002AFA7A:
    result = 0;
    if (((uint8_t)(v_stack_m1C8)) == 17) {
        Arg1 = v_stack_m1C0;
        result = MiLockWorkingSetShared(Arg1, Arg2, v_stack_m178, Arg4);
        v_stack_m1C8 = (uint8_t)(result);
    }
    local_r14 = 0;
    v_stack_m190 = 0;
    if (v_stack_m180 != local_rbx) goto loc_002AFBFC;
    v_stack_m140 = local_r13;
loc_002AFAB4:
    result = MI_READ_PTE_LOCK_FREE(local_r13, Arg2, v_stack_m178, Arg4);
    if (result == 0) goto loc_002B0177;
    result = (uint8_t)((result) & (129));
    if (((uint8_t)(result)) == 129) goto loc_002B0BC5;
    if (v_stack_m180 != v_stack_m160) goto loc_002AFE15;
loc_002AFAE5:
    if (-1 != -1) goto loc_002AFCA0;
    if (v_stack_m174 != 0) goto loc_002B0D57;
    Arg1 = (v_stack_m158) >> (18);
    Arg1 = (uint32_t)((Arg1) & (0x3FFFFFF8ULL));
    Arg1 = (Arg1) + (Arg4);
    if (v_stack_m180 != Arg1) goto loc_002AFB76;
    result = MI_READ_PTE_LOCK_FREE(local_r13, Arg2, v_stack_m178, Arg4);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_002AFE72;
    if (condition_is_below) goto loc_002B04F1;
    if (condition_is_below) goto loc_002AFFD4;
    if ((((uint8_t)(local_rdi)) & (4)) != 0) goto loc_002B0855;
loc_002AFB5C:
    result = MiGetPagingFileOffset(result, Arg2, v_stack_m178, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002B014A;
loc_002AFB76:
loc_002AFB7B:
    local_r12 = 0;
loc_002AFB7E:
loc_002AFB88:
loc_002AFBA4:
loc_002AFBA9:
    if (condition_is_above_or_equal) goto loc_002AFBC7;
    if (((0) & (1)) != 0) goto loc_002AFE95;
    if (!(condition_is_above_or_equal)) {
        local_r14 = (local_r14) & (0xFFFFFFFFF03FFFFFULL);
    }
    *(uint64_t *)(v_stack_m1A8 + 0x8) = local_r14;
    local_r13 = (v_stack_m1A8) + (16);
    v_stack_m1A8 = local_r13;
    v_stack_m150 = local_r13;
    result = (v_stack_m1B0) - (1);
    v_stack_m1B0 = result;
    if (condition_is_not_equal) goto loc_002AF8E0;
loc_002AFBEE:
    if (v_stack_m1B8 == 0) goto loc_002AFF2B;
    goto loc_002AFF21;
loc_002AFBFC:
    result = v_stack_m1B8;
    if (v_stack_m1B8 != 0) {
        Arg2 = 17;
        Arg1 = v_stack_m1B8;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, v_stack_m1C0, Arg4);
        result = 0;
        v_stack_m1B8 = 0;
        v_stack_m170 = 0;
    }
    if (v_stack_m180 != 0) {
        Arg2 = v_stack_m180;
        Arg1 = v_stack_m1C0;
        result = MiUnlockPageTable(Arg1, Arg2, v_stack_m1C0, Arg4);
    }
    Arg4 = 0;
    result = MiLockLowestValidPageTableEx(v_stack_m1C0, local_r13, v_stack_m140, Arg4);
    v_stack_m180 = result;
    goto loc_002AFAB4;
loc_002AFC5B:
    if ((((uint8_t)(local_r13 + 8)) & (120)) == 0) goto loc_002B02C5;
loc_002AFC67:
    result = KeShouldYieldProcessor(v_stack_m1C0, local_r13, v_stack_m140, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002B09AF;
    goto loc_002AFA58;
loc_002AFC7F:
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFEFULL));
loc_002AFC82:
    local_r12 = (0) >> (12);
    local_r12 = (local_r12) & (result);
    if ((((uint8_t)(local_rdi)) & (48)) != 0) goto loc_002B036D;
loc_002AFCA0:
    local_rsi = (local_r12 + local_r12 * 2) << (4);
    local_rsi = (local_rsi) + (v_stack_m140);
    if (condition_is_below) goto loc_002B0A26;
loc_002AFCCA:
    result = MiGetPfnPriority(local_rsi, local_r13, v_stack_m140, Arg4);
    result = MI_NODE_FROM_PFN(local_rsi, local_r13, v_stack_m140, Arg4);
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (7));
    local_r15 = (local_r15) << (8);
    result = (uint32_t)((result) & (63));
    local_r15 = (local_r15) | (result);
    local_r15 = (local_r15) << (16);
    local_r14 = (*(uint64_t *)(local_rsi + 0x28)) >> (48);
    local_r14 = (uint32_t)((local_r14) & (0x8000ULL));
    local_r15 = (local_r15) | (local_r14);
    result = (v_stack_m190) & (0xFFFFFFFFF8C07FFFULL);
    local_r15 = (local_r15) | (result);
    v_stack_m190 = local_r15;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_002B0A46;
    result = MiIsPageOnBadList(local_rsi, local_r13, v_stack_m140, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002B0A46;
loc_002AFD37:
    if (condition_is_below) goto loc_002AFEB5;
    if (condition_is_below) goto loc_002AFEB0;
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 1) goto loc_002B0A02;
loc_002AFD63:
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 1) goto loc_002B07A9;
    result = MiGetWsleContents(local_rsi, v_stack_m158, v_stack_m140, Arg4);
    result = (uint8_t)((result) & (15));
    if (((uint8_t)(result)) == 8) goto loc_002B0133;
loc_002AFD8F:
    if (sign_flag) goto loc_002B0196;
    result = ((uint32_t)(*(uint32_t *)(local_rsi + 0x10))) >> (5);
    result = (uint32_t)((result) & (31));
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x2AFDAD + result * 4 + 0x14630))) & (0x7FFULL));
    local_r14 = (local_r14) << (4);
    result = (v_stack_m190) & (0xFFFFFFFFFFFF8001ULL);
    local_r14 = (local_r14) | (result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x30))) & (0x4200000ULL));
    if (((uint32_t)(result)) == 0x4200000ULL) goto loc_002B0A6D;
loc_002AFE0D:
    local_r12 = 0;
    goto loc_002AFBA4;
loc_002AFE15:
    v_stack_m1D8 = (uint8_t)(v_stack_m1C8);
    result = MiWorkingSetInfoCheckPageTable(v_stack_m1C0, local_rsi, v_stack_m198, (uint32_t)(v_stack_p10));
    if ((uint32_t)(result) == 0) goto loc_002B0D39;
    local_rsi = 0;
    v_stack_m180 = 0;
    goto loc_002AFA7A;
loc_002AFE5A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x40)))) & (1)) == 0) goto loc_002AFA03;
loc_002AFE66:
    local_rdi = (uint32_t)((local_rdi) | (2));
    v_stack_m188 = (uint32_t)(local_rdi);
    goto loc_002AFA13;
loc_002AFE72:
    local_r14 = (local_r14) | (1);
    v_stack_m190 = local_r14;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x30))) & (112));
    if (((uint8_t)(result)) != 64) goto loc_002AFC7F;
    local_rdi = (uint32_t)((local_rdi) | (16));
    goto loc_002AFC82;
loc_002AFE95:
    if (condition_is_above_or_equal) goto loc_002AFBC7;
    local_r14 = (local_r14) & (0xFFFFFFFFF8C0FFFFULL);
    local_r14 = (local_r14) | (14);
    goto loc_002AFBC7;
loc_002AFEB0:
loc_002AFEB5:
    result = MiGetProtectionFromPte(v_stack_m1A0, v_stack_m160, v_stack_m198, (uint32_t)(v_stack_p10));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x2AFECE + (uint32_t)((uint32_t)(result)) * 4 + 0x14630))) & (0x7FFULL));
    Arg2 = (Arg2) << (4);
    local_r14 = (v_stack_m190) & (0xFFFFFFFFFFFF800FULL);
    Arg2 = (Arg2) | (local_r14);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x30))) & (0x4200000ULL));
    if (((uint32_t)(result)) == 0x4200000ULL) goto loc_002B0C62;
loc_002AFEFD:
    v_stack_m190 = Arg2;
    if (sign_flag) goto loc_002B0970;
loc_002AFF14:
    local_r12 = 0;
loc_002AFF17:
    goto loc_002AFB7E;
loc_002AFF21:
    result = MiUnlockProtoPoolPage(v_stack_m1B8, 17, v_stack_m198, (uint32_t)(v_stack_p10));
loc_002AFF2B:
    if (((uint8_t)(v_stack_m1C8)) == 17) goto loc_002AFF5B;
    result = v_stack_m180;
    if (v_stack_m180 != 0) {
        Arg2 = v_stack_m180;
        Arg1 = v_stack_m1C0;
        result = MiUnlockPageTable(Arg1, Arg2, v_stack_m198, (uint32_t)(v_stack_p10));
    }
    result = MiUnlockWorkingSetShared(v_stack_m1C0, (uint8_t)(v_stack_m1C8), v_stack_m198, (uint32_t)(v_stack_p10));
loc_002AFF5B:
    if (v_stack_m1A0 != 0) {
        Arg1 = v_stack_m1A0;
        result = MiUnlockAndDereferenceVadShared(Arg1, (uint8_t)(v_stack_m1C8), v_stack_m198, (uint32_t)(v_stack_p10));
    }
    if ((((uint8_t)(local_rdi)) & (1)) != 0) goto loc_002B02B1;
loc_002AFF72:
    if (v_stack_m138 != 0) goto loc_002B06E6;
    local_r13 = (v_stack_m1A8) - (v_stack_mC8);
    local_r13 = (local_r13) & (-16);
    result = memcpy(v_stack_m128, v_stack_mC8, local_r13, (uint32_t)(v_stack_p10));
    goto loc_002AFFAE;
loc_002AFFAE:
loc_002AFFB0:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_mC8, local_r13, (uint32_t)(v_stack_p10));
    local_rsp = (local_rsp) + (448);
    return result;
loc_002AFFD4:
    local_r12 = 0;
loc_002AFFD7:
loc_002AFFE1:
    result = MI_READ_PTE_LOCK_FREE(local_r13, v_stack_mC8, local_r13, (uint32_t)(v_stack_p10));
    if (condition_is_above_or_equal) goto loc_002B0CB4;
    result = MiInvalidPteConforms(result, v_stack_mC8, local_r13, (uint32_t)(v_stack_p10));
    if ((uint32_t)(result) == 0) goto loc_002AFFE1;
    if (*(uint64_t *)(v_rip + 0xB7DC76) == 0) goto loc_002B0021;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_002B0141;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xB7DC76));
    Arg1 = (Arg1) & (result);
loc_002B0021:
    Arg1 = (Arg1) >> (12);
    Arg1 = (Arg1) & (*(uint64_t *)(v_rip + 0xB7DC76));
    Arg2 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xB7DC99))) goto loc_002AFFE1;
    result = (*(uint64_t *)(v_stack_m190 + Arg2 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_002AFFE1;
    v_stack_p90 = 0;
loc_002B0070:
    if (condition_is_below) goto loc_002B0280;
    result = MI_READ_PTE_LOCK_FREE(local_r13, Arg2, local_r13, (uint32_t)(v_stack_p10));
    if (result != result) goto loc_002B0359;
    result = (*(uint64_t *)(v_stack_m190 + Arg2 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_002B0C94;
loc_002B00B1:
    result = (*(uint64_t *)(v_stack_m190 + Arg2 * 8 + 0x8)) | (local_r13);
    if (result != local_r13) goto loc_002B0CBC;
loc_002B00CB:
loc_002B00D5:
    if (v_stack_m190 + Arg2 * 8 == 0) goto loc_002B0341;
    result = MI_READ_PTE_LOCK_FREE(local_r13, *(uint64_t *)(v_rip + 0xB7FFE6), local_r13, (uint32_t)(v_stack_p10));
    Arg1 = (v_stack_m190 + Arg2 * 8) - (v_stack_m190);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (v_stack_m190);
    result = MiQueryPfn(Arg1, v_stack_p60, local_r13, (uint32_t)(v_stack_p10));
    goto loc_002AFB7E;
loc_002B0129:
    goto loc_002AFFB0;
loc_002B0133:
    goto loc_002AFD8F;
loc_002B0141:
    Arg1 = (Arg1) & (-17);
    goto loc_002B0021;
loc_002B014A:
    if (result != 0) goto loc_002AFB76;
loc_002B0153:
    Arg1 = (((*(uint32_t *)(v_stack_p58 + 0x30)) & (0x200000ULL)) != 0) ? 1 : 0;
    result = ((((uint8_t)(v_stack_m138)) & (8)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_002AFB7B;
    goto loc_002B04F6;
loc_002B0177:
    if ((((uint8_t)(v_stack_m138)) & (32)) != 0) goto loc_002AFB76;
    if (v_stack_p84 != ((uint32_t)(v_stack_p68))) goto loc_002AFAE5;
    goto loc_002B0153;
loc_002B0196:
    result = (*(uint64_t *)(v_stack_p78 + 0x18)) & (Arg1);
    if (result >= 7) goto loc_002B031F;
    local_rbx = (*(uint64_t *)(v_stack_p78 + 0x18)) & (Arg1);
loc_002B01B8:
    result = MiGetPfnProtection(Arg1, v_stack_m1C8, v_stack_p78, (uint32_t)(v_stack_p10));
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x2B01CC + (uint32_t)((uint32_t)(result)) * 4 + 0x14630))) & (0x7FFULL));
    local_r14 = (local_r14) << (3);
    local_rbx = (uint32_t)((local_rbx) & (7));
    local_r14 = (local_r14) | (local_rbx);
    local_r14 = (local_r14) + (local_r14);
    result = (v_stack_p68) & (0xFFFFFFFFFFFF8001ULL);
    local_r14 = (local_r14) | (result);
    v_stack_p68 = local_r14;
    if ((((uint8_t)(v_stack_m138)) & (8)) != 0) goto loc_002B084B;
    if (((*(uint32_t *)(v_stack_p58 + 0x30)) & (0x200000ULL)) != 0) goto loc_002AFB7B;
    result = MiGetProtoPteAddress(v_stack_p58, v_stack_pC8, 8, v_stack_pF0);
    Arg1 = (*(uint64_t *)(v_stack_p78 + 0x8)) | (v_stack_pC8);
    if (result != Arg1) goto loc_002AFF14;
    goto loc_002AFB7B;
loc_002B025F:
    Arg2 = 0;
    result = KiStackAttachProcess(local_rbx, Arg2, v_stack_pF8, v_stack_pF0);
    goto loc_002AF887;
loc_002B0280:
    local_r14 = (uint32_t)(((uint32_t)(v_stack_p90)) + 1);
    v_stack_p90 = (uint32_t)(local_r14);
    if (((*(uint32_t *)(v_rip + 0xD15012)) & ((uint32_t)(local_r14))) == 0) goto loc_002B0CEA;
loc_002B02A0:
loc_002B02A2:
    if (!sign_flag) goto loc_002B0070;
    goto loc_002B0280;
loc_002B02B1:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF8, Arg2, v_stack_pF8, v_stack_pF0);
    goto loc_002AFF72;
loc_002B02C5:
    Arg2 = 0;
    result = MiWorkingSetIsContended(v_stack_p38, Arg2, v_stack_pF8, v_stack_pF0);
    if ((uint32_t)(result) == 0) goto loc_002AFC67;
    goto loc_002B09B4;
loc_002B02E1:
    local_r10 = v_stack_m1C8;
    if (v_stack_m1B8 != 0) {
        Arg2 = 17;
        Arg1 = v_stack_m1B8;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, v_stack_pF8, v_stack_pF0);
        v_stack_p40 = 0;
        v_stack_p88 = 0;
        local_r10 = v_stack_p30;
        Arg3 = v_stack_p38;
    }
    if (((uint8_t)(local_r10)) != 17) goto loc_002B048B;
loc_002B0312:
    result = MiUnlockAndDereferenceVadShared(v_stack_p58, Arg2, Arg3, v_stack_pF0);
    goto loc_002AF919;
loc_002B031F:
    goto loc_002B01B8;
loc_002B0329:
    if (((uint32_t)((uint32_t)(v_stack_p80))) != 0xC000010AULL) goto loc_002AFB88;
    goto loc_002AFBEE;
loc_002B0341:
    goto loc_002AFA7A;
loc_002B0359:
    goto loc_002AFFD7;
loc_002B036D:
    result = MiPageToNode(0, Arg2, Arg3, v_stack_pF0);
    Arg1 = (local_r12 + local_r12 * 2) + (local_r12 + local_r12 * 2);
    if (0 > (*(uint64_t *)(v_rip + 0xB7D94A))) goto loc_002B03BC;
    Arg1 = (*(uint64_t *)(Arg3 + Arg1 * 8)) >> (54);
    if (condition_is_below) goto loc_002B04C4;
loc_002B03B7:
loc_002B03BC:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) & (63));
    local_rsi = (local_rsi) << (16);
    local_r14 = (v_stack_p68) & (0xFFFFFFFFFFC0FFFFULL);
    local_rsi = (local_rsi) | (local_r14);
    if (((1) & (32)) == 0) goto loc_002B042B;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x30))) >> (7));
    Arg2 = (uint32_t)((Arg2) & (31));
    result = (uint8_t)(((uint8_t)(v_stack_p98)) & (24));
    if (((uint8_t)(result)) == 8) goto loc_002B0A14;
    if ((((uint8_t)(v_stack_p98)) & (16)) != 0) {
        Arg2 = (uint32_t)((Arg2) | (8));
    }
    local_rsi = (local_rsi) | (0x400001ULL);
loc_002B0400:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x2B0409 + (uint32_t)(Arg2) * 4 + 0x14630))) & (0x7FFULL));
    local_r14 = (local_r14) << (4);
    local_rsi = (local_rsi) & (0xFFFFFFFFFFFF800FULL);
    local_r14 = (local_r14) | (local_rsi);
    goto loc_002AFB7B;
loc_002B042B:
    result = MiRotatedToFrameBuffer(local_r13, v_rip - 2819081, Arg3, v_stack_pF0);
    if ((uint32_t)(result) == 0) goto loc_002B06FD;
    if (condition_is_above_or_equal) goto loc_002B0D43;
loc_002B044B:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x30))))) & (0xC00ULL));
    Arg1 = ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x30)))) & (896)) != 0) ? 1 : 0;
    result = (((uint32_t)(Arg3)) == 0xC00ULL) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_002B0C7F;
    Arg2 = (uint32_t)((4) | (24));
    goto loc_002B0400;
loc_002B047D:
    if (((uint32_t)(result)) >= 2) goto loc_002AFE66;
    goto loc_002AF9FB;
loc_002B048B:
    local_r10 = v_stack_p30;
    if (local_rsi != 0) {
        Arg2 = local_rsi;
        Arg1 = Arg3;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, v_stack_pF0);
        local_rsi = 0;
        v_stack_p78 = 0;
        local_r10 = v_stack_p30;
        Arg3 = v_stack_p38;
    }
    result = MiUnlockWorkingSetShared(Arg3, (uint8_t)(local_r10), Arg3, v_stack_pF0);
    v_stack_p30 = 17;
    goto loc_002B0312;
loc_002B04C4:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_002B04DF;
    result = MiIsPageOnBadList(v_stack_p58, (uint8_t)(local_r10), Arg3, v_stack_pF0);
    if ((uint32_t)(result) == 0) goto loc_002B03B7;
loc_002B04DF:
    local_r14 = (v_stack_p68) | ((uint32_t)(0x80000000ULL));
    goto loc_002B03BC;
loc_002B04F1:
loc_002B04F6:
    local_r12 = 0;
    if (((1) & (8)) != 0) goto loc_002B067E;
    if (((*(uint32_t *)(v_stack_p58 + 0x30)) & (0x200000ULL)) != 0) goto loc_002B06C2;
    Arg2 = (v_stack_pA0) >> (12);
    result = MiGetProtoPteAddress(v_stack_p58, Arg2, local_r12 + 8, v_stack_pF0);
    if (v_stack_p98 != 0) goto loc_002B06B2;
loc_002B0541:
loc_002B0544:
    if (result == 0) goto loc_002AFB7E;
    v_stack_p68 = local_r14;
    if (result == result) {
        v_stack_p68 = local_r14;
    }
    result = (v_stack_p88) ^ (result);
    if (((result) & (0xFFFFFFFFFFFFF000ULL)) == 0) goto loc_002B05B1;
    result = v_stack_p40;
    if (v_stack_p40 != 0) {
        Arg2 = 17;
        Arg1 = v_stack_p40;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, result, v_stack_pF0);
        v_stack_p88 = 0;
    }
    Arg2 = 0;
    result = MiLockProtoPoolPage(result, Arg2, result, v_stack_pF0);
    v_stack_p40 = result;
    if (result == 0) goto loc_002B0601;
    v_stack_p88 = result;
loc_002B05B1:
    Arg2 = 0;
    result = MiLockLeafPage(result, Arg2, result, v_stack_pF0);
    if (result != 0) goto loc_002B0636;
    if (((*(uint64_t *)(result)) & (0xC00ULL)) != 0) goto loc_002AFF17;
    result = MiInvalidPteConforms(*(uint64_t *)(result), *(uint64_t *)(result), result, v_stack_pF0);
    if ((uint32_t)(result) == 0) goto loc_002AFF17;
    result = MiGetPagingFileOffset(*(uint64_t *)(result), *(uint64_t *)(result), result, v_stack_pF0);
    if ((uint32_t)(result) != 0) goto loc_002B069E;
    if (*(uint64_t *)(result) != 0) goto loc_002AFF17;
    goto loc_002AFB7E;
loc_002B0601:
    if (((uint8_t)(v_stack_p30)) != 17) goto loc_002B0819;
loc_002B0611:
    Arg4 = 0;
    Arg3 = 0;
    result = MmAccessFault(Arg4 + 2, result, Arg3, Arg4);
    goto loc_002AFA7A;
loc_002B0636:
    Arg1 = (result) - (0);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (result);
    result = MiQueryPfn(Arg1, v_stack_p60, Arg3, Arg4);
    goto loc_002AFB7E;
loc_002B067E:
    Arg3 = *(uint64_t *)(v_rip + 0xB7D4EB);
    if (v_stack_pE8 == 0x7FFE0000ULL) { Arg3 = *(uint64_t *)(v_rip + 0xB7D4CF); }
    goto loc_002B0541;
loc_002B069E:
    goto loc_002AFB7E;
loc_002B06B2:
    result = MiIsPrototypePteVadLookup(v_stack_p98, v_stack_p60, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002B0541;
loc_002B06C2:
    if (*(uint64_t *)(v_rip + 0xB7D5B7) == 0) goto loc_002B06DD;
    if ((((uint8_t)(v_stack_p98)) & (16)) != 0) goto loc_002B0D12;
    result = ~(*(uint64_t *)(v_rip + 0xB7D5B7));
    local_rbx = (v_stack_p98) & (result);
loc_002B06DD:
    local_rbx = (local_rbx) >> (16);
    goto loc_002B0544;
loc_002B06E6:
    result = MmUnlockPages(1, v_stack_p60, Arg3, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(1, Arg2, Arg3, Arg4);
    goto loc_002AFFAE;
loc_002B06FD:
    result = MiGetPfnPriority(v_stack_p58, Arg2, Arg3, Arg4);
    local_r10 = ((uint32_t)((uint32_t)(result))) << (24);
    local_rsi = (result) ^ (local_r10);
    local_rsi = (local_rsi) & (0xFFFFFFFFF8FFFFFFULL);
    local_rsi = (local_rsi) ^ (local_r10);
    v_stack_p68 = local_rsi;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x10))) >> (5);
    Arg2 = (uint32_t)((Arg2) & (31));
    if (condition_is_below) goto loc_002B0D4D;
    if (sign_flag) goto loc_002B0D4D;
    if (*(uint64_t *)(v_stack_p58 + 0x8) == 0) goto loc_002B0D4D;
    result = (*(uint64_t *)(v_stack_p58 + 0x18)) & (v_stack_p58);
    if (result >= 7) goto loc_002B0A1C;
    local_rsi = (*(uint64_t *)(v_stack_p58 + 0x18)) & (v_stack_p58);
loc_002B077D:
    local_rsi = (uint32_t)((local_rsi) & (7));
    local_rsi = (local_rsi) + (local_rsi);
    result = (v_stack_p68) & (-15);
    local_rsi = (local_rsi) | (result);
loc_002B079F:
    goto loc_002B0400;
loc_002B07A9:
    result = MiIsPfnEnclave(local_rsi, (uint32_t)(*(uint32_t *)(v_rip - 0x2B0798 + (uint32_t)(Arg2) * 4 + 0x11070)), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002B0A5D;
    result = ((uint32_t)(*(uint32_t *)(local_rsi + 0x10))) >> (5);
    result = (uint32_t)((result) & (31));
loc_002B07C8:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip - 0x2B07D1 + (uint32_t)((uint32_t)(result)) * 4 + 0x14630))) & (0x7FFULL));
    local_r14 = (local_r14) << (4);
    result = (v_stack_p68) & (0xFFFFFFFFFFFF800FULL);
    local_r14 = (local_r14) | (result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x30))) & (0x4200000ULL));
    if (((uint32_t)(result)) == 0x4200000ULL) {
        local_r14 = (local_r14) & (result);
    }
    goto loc_002AFB7B;
loc_002B0819:
    if (local_rsi != 0) {
        Arg2 = local_rsi;
        Arg1 = v_stack_p38;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, Arg4);
        local_rsi = 0;
        v_stack_p78 = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_p38, (uint8_t)(local_r14), Arg3, Arg4);
    v_stack_p30 = 17;
    goto loc_002B0611;
loc_002B084B:
    goto loc_002AFB7B;
loc_002B0855:
    result = MiIsLazyStampedPte(local_rbx, (uint8_t)(local_r14), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002AFB5C;
    local_r12 = 0;
    goto loc_002AFB7E;
loc_002B0875:
    Arg2 = (((local_rbx) & (0xFFFULL)) != 0) ? 1 : 0;
    Arg2 = (Arg2) + (7);
    result = (local_rbx) >> (12);
    Arg2 = (Arg2) + (result);
    Arg2 = (Arg2) << (3);
    result = MiAllocatePool(64, Arg2, (uint32_t)(0x20206D4DULL), Arg4);
    v_stack_pC0 = result;
    if (result == 0) goto loc_002B0966;
    *(uint64_t *)(result) = 0;
    Arg1 = (uint32_t)((0) & (0xFFFULL));
    Arg1 = (Arg1) + (0xFFFULL);
    Arg1 = (Arg1) + (local_rbx);
    Arg1 = (Arg1) >> (12);
    Arg1 = (uint16_t)((Arg1) + (6));
    Arg1 = (uint16_t)((Arg1) << (3));
    *(uint16_t *)(result + 0x8) = (uint16_t)(Arg1);
    *(uint16_t *)(result + 0xA) = 0;
    result = (0) & (0xFFFFFFFFFFFFF000ULL);
    *(uint64_t *)(result + 0x20) = result;
    Arg2 = (uint32_t)((0) & (0xFFFULL));
    *(uint32_t *)(result + 0x2C) = Arg2;
    *(uint32_t *)(result + 0x28) = (uint32_t)(local_rbx);
    result = MmProbeAndLockPages(result, *(uint8_t *)(local_rsi + 0x232), 1, Arg4);
    goto loc_002B092F;
loc_002B092F:
    if (((*(uint8_t *)(result + 0xA)) & (5)) == 0) goto loc_002B0A7F;
loc_002B093E:
    v_stack_pA8 = *(uint64_t *)(result + 0x18);
    v_stack_p50 = *(uint64_t *)(result + 0x18);
    if (*(uint64_t *)(result + 0x18) != 0) goto loc_002AF872;
    result = MmUnlockPages(result, *(uint8_t *)(local_rsi + 0x232), 1, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 1, Arg4);
loc_002B0966:
    goto loc_002AFFB0;
loc_002B0970:
    result = (*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x18)) & (0);
    if (result >= 7) goto loc_002B0C74;
    local_r14 = (*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x18)) & (0);
loc_002B0992:
    local_r14 = (uint32_t)((local_r14) & (7));
    local_r14 = (local_r14) + (local_r14);
    result = (v_stack_p68) & (-15);
    local_r14 = (local_r14) | (result);
    goto loc_002AFB7B;
loc_002B09AF:
loc_002B09B4:
    if (result != 0) {
        Arg2 = 17;
        Arg1 = result;
        result = MiUnlockProtoPoolPage(Arg1, Arg2, 1, Arg4);
        v_stack_p40 = 0;
        v_stack_p88 = 0;
    }
    if (local_rsi != 0) {
        Arg2 = local_rsi;
        Arg1 = v_stack_p38;
        result = MiUnlockPageTable(Arg1, Arg2, 1, Arg4);
        local_rsi = 0;
        v_stack_p78 = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_p38, v_stack_p30, 1, Arg4);
    v_stack_p30 = 17;
    goto loc_002AFA58;
loc_002B0A02:
    if (!sign_flag) goto loc_002AFD63;
    goto loc_002AFEB0;
loc_002B0A14:
    Arg2 = (uint32_t)((v_stack_p30) | (24));
    goto loc_002B03F9;
loc_002B0A1C:
    goto loc_002B077D;
loc_002B0A26:
    local_r15 = result;
    if (result == -1) {
        local_r15 = 0;
        local_r15 = (local_r15) & (-16);
    }
    local_r13 = (local_r15 + local_r15 * 2) << (4);
    local_r13 = (local_r13) + (1);
    goto loc_002AFCCA;
loc_002B0A46:
    local_r14 = (v_stack_p68) | ((uint32_t)(0x80000000ULL));
    v_stack_p68 = local_r14;
    goto loc_002AFD37;
loc_002B0A5D:
    result = MiGetValidAweProtection(local_r15, v_stack_p38, 1, Arg4);
    goto loc_002B07C8;
loc_002B0A6D:
    local_r14 = (local_r14) & (result);
    goto loc_002AFE0D;
loc_002B0A7F:
    v_stack_p28 = 0x40000010ULL;
    v_stack_p20 = 0;
    Arg4 = 0;
    Arg2 = 0;
    result = MmMapLockedPagesSpecifyCache(local_r15, Arg2, Arg4 + 1, Arg4);
    goto loc_002B093E;
loc_002B0AA5:
    if (result == 0) goto loc_002AF9B2;
loc_002B0AAE:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_pB0 + 0x5FC)))) & (1)) != 0) goto loc_002AF9B2;
    local_rdi = (uint32_t)((1) | (8));
    goto loc_002AF9B2;
loc_002B0ACC:
    local_rdi = (uint32_t)((local_rdi) | (4));
    v_stack_p70 = (uint32_t)(local_rdi);
    result = MiGetAweVadPageSize(local_r15, Arg2, Arg4 + 1, Arg4);
    if (result >= 512) goto loc_002AFE66;
    goto loc_002AFA13;
loc_002B0AEC:
    if (v_stack_m1B8 == 0) goto loc_002B0D2F;
    result = MiUnlockProtoPoolPage(v_stack_m1B8, 17, Arg4 + 1, Arg4);
    v_stack_p40 = 0;
    v_stack_p88 = 0;
loc_002B0B15:
    if (((uint8_t)(v_stack_p30)) == 17) goto loc_002B0B52;
    local_rsi = 7;
    local_r10 = v_stack_p30;
    if (7 != 0) {
        Arg2 = 7;
        Arg1 = v_stack_p38;
        result = MiUnlockPageTable(Arg1, Arg2, Arg4 + 1, Arg4);
        local_rsi = 0;
        v_stack_p78 = 0;
        local_r10 = v_stack_p30;
    }
    result = MiUnlockWorkingSetShared(v_stack_p38, (uint8_t)(local_r10), Arg4 + 1, Arg4);
    v_stack_p30 = 17;
loc_002B0B52:
    goto loc_002AFA2A;
loc_002B0BC5:
    local_r12 = (v_stack_p38) >> (12);
    local_r12 = (local_r12) & (*(uint8_t *)(v_stack_p38));
    if (local_rsi < v_stack_p38) goto loc_002B0C23;
loc_002B0BF4:
    if (local_rsi > v_stack_p38) goto loc_002B0C23;
    local_rsi = (local_rsi) << (25);
    result = (v_stack_p38) << (25);
    local_rsi = (local_rsi) - (result);
    local_rsi = (local_rsi) >> (16);
    Arg3 = (uint32_t)(((uint32_t)(0xFFFFFFFFULL)) + 1);
    if (local_rsi >= v_stack_p38) goto loc_002B0BF4;
loc_002B0C23:
    if ((uint32_t)(Arg3) == 0) goto loc_002B0C52;
loc_002B0C35:
    result = (uint32_t)((v_stack_pC8) & (511));
    result = (result) * (1);
    local_r12 = (local_r12) + (result);
    Arg2 = (v_stack_pC8) >> (9);
    Arg1 = (1) << (9);
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_not_equal) goto loc_002B0C35;
loc_002B0C52:
    v_stack_p68 = (uint32_t)(0x800001ULL);
    goto loc_002AFAE5;
loc_002B0C62:
    Arg2 = (Arg2) & (result);
    goto loc_002AFEFD;
loc_002B0C74:
    goto loc_002B0992;
loc_002B0C7F:
    if (((uint32_t)(Arg3)) != 0x400ULL) goto loc_002B0400;
    Arg2 = (uint32_t)((Arg2) | (8));
    goto loc_002B0400;
loc_002B0C94:
    Arg2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(local_rsi, Arg2, Arg3, Arg4);
    if (result != 0) goto loc_002B00B1;
loc_002B0CB4:
    goto loc_002B00D5;
loc_002B0CBC:
    if (condition_is_below) goto loc_002B00CB;
    v_stack_p20 = *(uint64_t *)(local_r12 + 0x8);
    result = KeBugCheckEx(26, (uint32_t)(0x411ULL), result, v_stack_p38);
loc_002B0CEA:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD15DC8)))) & (64)) == 0) goto loc_002B02A0;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (uint32_t)(0x411ULL), result, v_stack_p38);
    if ((uint8_t)(result) == 0) goto loc_002B02A0;
    result = HvlNotifyLongSpinWait(7, (uint32_t)(0x411ULL), result, v_stack_p38);
    goto loc_002B02A2;
loc_002B0D12:
    local_rbx = (v_stack_p38) & (-17);
    goto loc_002B06DD;
loc_002B0D1B:
    goto loc_002AFFB0;
loc_002B0D25:
    goto loc_002AFFB0;
loc_002B0D2F:
    goto loc_002B0B15;
loc_002B0D39:
    goto loc_002AFAE5;
loc_002B0D43:
    goto loc_002B044B;
loc_002B0D4D:
    goto loc_002B079F;
loc_002B0D57:
    local_r12 = 0;
    goto loc_002AF9C5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002AF770&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
