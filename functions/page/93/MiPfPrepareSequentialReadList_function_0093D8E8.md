# MiPfPrepareSequentialReadList

- RVA: `0x0093D8E8`–`0x0093E1A6` (길이 `2,238` bytes)
- VA: `0x000000014093D8E8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008FFA4`
- 디코드: `535`개 명령, `2,238/2,238` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **31**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0093D9EB` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0093DA0A` → [MiInitializeDemandCoalesceContext](../../text/3D/MiInitializeDemandCoalesceContext_function_003D3350.md) (function, `0x003D3350`)
- `0x0093DA12` → [MiProtectionToCacheAttribute](../../text/2B/MiProtectionToCacheAttribute_function_002B8530.md) (function, `0x002B8530`)
- `0x0093DA64` → [MiInitializePageChainPacket](../../text/43/MiInitializePageChainPacket_function_004367C0.md) (function, `0x004367C0`)
- `0x0093DA6D` → [MiGetPageChain](../../text/33/MiGetPageChain_function_00330130.md) (function, `0x00330130`)
- `0x0093DA89` → [MiAppendPageChain](../../text/45/MiAppendPageChain_function_004570F4.md) (function, `0x004570F4`)
- `0x0093DAC5` → [MiPfAllocateMdls](MiPfAllocateMdls_function_0093E45C.md) (function, `0x0093E45C`)
- `0x0093DAFB` → [MiReleaseReadListResources](MiReleaseReadListResources_function_0093D570.md) (function, `0x0093D570`)
- `0x0093DB05` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0093DB17` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0093DB3B` → [MiGetControlAreaPtes](../../text/24/MiGetControlAreaPtes_function_0024DB10.md) (function, `0x0024DB10`)
- `0x0093DB97` → [MiAllocateReadList](MiAllocateReadList_function_0093D4F0.md) (function, `0x0093D4F0`)
- `0x0093DBFA` → [MiOffsetToProtos](../../text/24/MiOffsetToProtos_function_0024D880.md) (function, `0x0024D880`)
- `0x0093DC05` → [MiGetControlAreaPartition](../../text/43/MiGetControlAreaPartition_function_0043E560.md) (function, `0x0043E560`)
- `0x0093DC11` → [MiGetAvailablePagesExcludeSlists](../../text/48/MiGetAvailablePagesExcludeSlists_function_00483924.md) (function, `0x00483924`)
- `0x0093DCA0` → [MiInitializePageColorBase](../../text/32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x0093DCA9` → [MiColorBaseToNode](../../text/46/MiColorBaseToNode_function_004660B4.md) (function, `0x004660B4`)
- `0x0093DD61` → [MiObtainFaultCharges](../../text/28/MiObtainFaultCharges_function_0028AEB0.md) (function, `0x0028AEB0`)
- `0x0093DD85` → [MiUseSlabAllocator](../../text/36/MiUseSlabAllocator_function_00365C68.md) (function, `0x00365C68`)
- `0x0093DDCE` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (function, `0x0043E130`)
- `0x0093DDD9` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (function, `0x0043E130`)
- `0x0093DDF6` → [IS_PTE_NOT_DEMAND_ZERO](../../text/22/IS_PTE_NOT_DEMAND_ZERO_function_0022F4D0.md) (function, `0x0022F4D0`)
- `0x0093DE37` → [MiUpdatePfnForPrefetchByPte](../../text/32/MiUpdatePfnForPrefetchByPte_function_00321210.md) (function, `0x00321210`)
- `0x0093DE62` → [MiAddViewsForSection](../../text/32/MiAddViewsForSection_function_00324990.md) (function, `0x00324990`)
- `0x0093DEA2` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0093DF4D` → [MiRefillPurgedExtents](../../text/47/MiRefillPurgedExtents_function_00479988.md) (function, `0x00479988`)
- `0x0093DF91` → [MiRemoveViewsFromSectionWithPfn](../../text/29/MiRemoveViewsFromSectionWithPfn_function_002986D4.md) (function, `0x002986D4`)
- `0x0093DFD2` → [MiGetSharedProtos](../../text/34/MiGetSharedProtos_function_00348D58.md) (function, `0x00348D58`)
- `0x0093E032` → [MiStartingOffset](../../text/34/MiStartingOffset_function_003482E0.md) (function, `0x003482E0`)
- `0x0093E03D` → [MiEndingOffsetWithLock](../../text/40/MiEndingOffsetWithLock_function_00404718.md) (function, `0x00404718`)
- `0x0093E0D1` → [MiReturnFaultCharges](../../text/36/MiReturnFaultCharges_function_0036D928.md) (function, `0x0036D928`)
- `0x0093E126` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0093E15C` → [MiReturnFaultCharges](../../text/36/MiReturnFaultCharges_function_0036D928.md) (function, `0x0036D928`)
- `0x0093E172` → [MiReturnFaultCharges](../../text/36/MiReturnFaultCharges_function_0036D928.md) (function, `0x0036D928`)
- `0x0093E19B` → [MiIssuePageHeatList](../../text/44/MiIssuePageHeatList_function_0044615C.md) (function, `0x0044615C`)

### Direct callers
- [MmPrefetchForCacheManager](MmPrefetchForCacheManager_function_0093D714.md) at `0x0093D78B`
- [MiPrefetchControlArea](MiPrefetchControlArea_function_0093E830.md) at `0x0093E8C9`

### Static image references
- `0x0093D907` → RVA `0x00E0A740` (`.data`; read)
- `0x0093DBB1` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **32**
  - `0x0093D9EB` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0093DA0A` → [MiInitializeDemandCoalesceContext](../../text/3D/MiInitializeDemandCoalesceContext_function_003D3350.md) (`PAGE` → `.text`)
  - `0x0093DA12` → [MiProtectionToCacheAttribute](../../text/2B/MiProtectionToCacheAttribute_function_002B8530.md) (`PAGE` → `.text`)
  - `0x0093DA64` → [MiInitializePageChainPacket](../../text/43/MiInitializePageChainPacket_function_004367C0.md) (`PAGE` → `.text`)
  - `0x0093DA6D` → [MiGetPageChain](../../text/33/MiGetPageChain_function_00330130.md) (`PAGE` → `.text`)
  - `0x0093DA89` → [MiAppendPageChain](../../text/45/MiAppendPageChain_function_004570F4.md) (`PAGE` → `.text`)
  - `0x0093DB05` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0093DB17` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0093DB3B` → [MiGetControlAreaPtes](../../text/24/MiGetControlAreaPtes_function_0024DB10.md) (`PAGE` → `.text`)
  - `0x0093DBFA` → [MiOffsetToProtos](../../text/24/MiOffsetToProtos_function_0024D880.md) (`PAGE` → `.text`)
  - `0x0093DC05` → [MiGetControlAreaPartition](../../text/43/MiGetControlAreaPartition_function_0043E560.md) (`PAGE` → `.text`)
  - `0x0093DC11` → [MiGetAvailablePagesExcludeSlists](../../text/48/MiGetAvailablePagesExcludeSlists_function_00483924.md) (`PAGE` → `.text`)
  - `0x0093DCA0` → [MiInitializePageColorBase](../../text/32/MiInitializePageColorBase_function_00320410.md) (`PAGE` → `.text`)
  - `0x0093DCA9` → [MiColorBaseToNode](../../text/46/MiColorBaseToNode_function_004660B4.md) (`PAGE` → `.text`)
  - `0x0093DD61` → [MiObtainFaultCharges](../../text/28/MiObtainFaultCharges_function_0028AEB0.md) (`PAGE` → `.text`)
  - `0x0093DD85` → [MiUseSlabAllocator](../../text/36/MiUseSlabAllocator_function_00365C68.md) (`PAGE` → `.text`)
  - `0x0093DDCE` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (`PAGE` → `.text`)
  - `0x0093DDD9` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (`PAGE` → `.text`)
  - `0x0093DDF6` → [IS_PTE_NOT_DEMAND_ZERO](../../text/22/IS_PTE_NOT_DEMAND_ZERO_function_0022F4D0.md) (`PAGE` → `.text`)
  - `0x0093DE37` → [MiUpdatePfnForPrefetchByPte](../../text/32/MiUpdatePfnForPrefetchByPte_function_00321210.md) (`PAGE` → `.text`)
  - `0x0093DE62` → [MiAddViewsForSection](../../text/32/MiAddViewsForSection_function_00324990.md) (`PAGE` → `.text`)
  - `0x0093DEA2` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x0093DF4D` → [MiRefillPurgedExtents](../../text/47/MiRefillPurgedExtents_function_00479988.md) (`PAGE` → `.text`)
  - `0x0093DF91` → [MiRemoveViewsFromSectionWithPfn](../../text/29/MiRemoveViewsFromSectionWithPfn_function_002986D4.md) (`PAGE` → `.text`)
  - `0x0093DFD2` → [MiGetSharedProtos](../../text/34/MiGetSharedProtos_function_00348D58.md) (`PAGE` → `.text`)
  - `0x0093E032` → [MiStartingOffset](../../text/34/MiStartingOffset_function_003482E0.md) (`PAGE` → `.text`)
  - `0x0093E03D` → [MiEndingOffsetWithLock](../../text/40/MiEndingOffsetWithLock_function_00404718.md) (`PAGE` → `.text`)
  - `0x0093E0D1` → [MiReturnFaultCharges](../../text/36/MiReturnFaultCharges_function_0036D928.md) (`PAGE` → `.text`)
  - `0x0093E126` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x0093E15C` → [MiReturnFaultCharges](../../text/36/MiReturnFaultCharges_function_0036D928.md) (`PAGE` → `.text`)
  - `0x0093E172` → [MiReturnFaultCharges](../../text/36/MiReturnFaultCharges_function_0036D928.md) (`PAGE` → `.text`)
  - `0x0093E19B` → [MiIssuePageHeatList](../../text/44/MiIssuePageHeatList_function_0044615C.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x0093DF3D` → [sub_00B25214 + 0x2A](../B2/Unknown_function_00B25214.md) (`tail-transfer`)
  - `0x0093DFDA` → [sub_00B25214 + 0x1C](../B2/Unknown_function_00B25214.md) (`tail-transfer`)
  - `0x0093E134` → [sub_00B25214](../B2/Unknown_function_00B25214.md) (`tail-transfer`)
  - `0x0093E192` → [sub_00B25214 + 0x8B](../B2/Unknown_function_00B25214.md) (`tail-transfer`)
  - `0x0093E1A1` → [sub_00B25214 + 0x8B](../B2/Unknown_function_00B25214.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0093D8E8  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0093D8ED  55                              push rbp
0093D8EE  56                              push rsi
0093D8EF  57                              push rdi
0093D8F0  41 54                           push r12
0093D8F2  41 55                           push r13
0093D8F4  41 56                           push r14
0093D8F6  41 57                           push r15
0093D8F8  48 8D AC 24 F0 FE FF FF         lea rbp, [rsp - 0x110]
0093D900  48 81 EC 10 02 00 00            sub rsp, 0x210
0093D907  48 8B 05 32 CE 4C 00            mov rax, qword ptr [rip + 0x4cce32]
0093D90E  48 33 C4                        xor rax, rsp
0093D911  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
0093D918  8B 85 80 01 00 00               mov eax, dword ptr [rbp + 0x180]
0093D91E  0F 57 C0                        xorps xmm0, xmm0
0093D921  45 33 ED                        xor r13d, r13d
0093D924  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
0093D928  48 8B 85 88 01 00 00            mov rax, qword ptr [rbp + 0x188]
0093D92F  48 8B F9                        mov rdi, rcx
0093D932  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
0093D936  4D 8B F9                        mov r15, r9
0093D939  48 8B 85 90 01 00 00            mov rax, qword ptr [rbp + 0x190]
0093D940  49 8B D8                        mov rbx, r8
0093D943  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
0093D947  4C 8B E2                        mov r12, rdx
0093D94A  33 C9                           xor ecx, ecx
0093D94C  4C 89 4D 28                     mov qword ptr [rbp + 0x28], r9
0093D950  48 89 55 88                     mov qword ptr [rbp - 0x78], rdx
0093D954  4C 89 28                        mov qword ptr [rax], r13
0093D957  F7 42 38 00 04 00 00            test dword ptr [rdx + 0x38], 0x400
0093D95E  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0093D962  0F 11 45 38                     movups xmmword ptr [rbp + 0x38], xmm0
0093D966  48 89 8D F0 00 00 00            mov qword ptr [rbp + 0xf0], rcx
0093D96D  0F 11 85 C0 00 00 00            movups xmmword ptr [rbp + 0xc0], xmm0
0093D974  89 8D F8 00 00 00               mov dword ptr [rbp + 0xf8], ecx
0093D97A  0F 11 85 D0 00 00 00            movups xmmword ptr [rbp + 0xd0], xmm0
0093D981  4C 89 6D C8                     mov qword ptr [rbp - 0x38], r13
0093D985  0F 11 85 E0 00 00 00            movups xmmword ptr [rbp + 0xe0], xmm0
0093D98C  75 0A                           jne 0x14093d998
0093D98E  4C 39 6A 40                     cmp qword ptr [rdx + 0x40], r13
0093D992  0F 85 A0 01 00 00               jne 0x14093db38
0093D998  41 BE EF 00 00 C0               mov r14d, 0xc00000ef
0093D99E  E9 67 01 00 00                  jmp 0x14093db0a
0093D9A3  4C 8B 65 90                     mov r12, qword ptr [rbp - 0x70]
0093D9A7  41 8B C6                        mov eax, r14d
0093D9AA  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
0093D9B0  4D 85 E4                        test r12, r12
0093D9B3  41 0F 44 C6                     cmove eax, r14d
0093D9B7  44 8B F0                        mov r14d, eax
0093D9BA  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
0093D9BE  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0093D9C2  48 85 C0                        test rax, rax
0093D9C5  0F 85 1A 05 00 00               jne 0x14093dee5
0093D9CB  4D 85 E4                        test r12, r12
0093D9CE  0F 84 12 01 00 00               je 0x14093dae6
0093D9D4  48 8B 7D C0                     mov rdi, qword ptr [rbp - 0x40]
0093D9D8  48 85 FF                        test rdi, rdi
0093D9DB  0F 84 B6 00 00 00               je 0x14093da97
0093D9E1  33 D2                           xor edx, edx
0093D9E3  48 8D 4D 50                     lea rcx, [rbp + 0x50]
0093D9E7  44 8D 42 70                     lea r8d, [rdx + 0x70]
0093D9EB  E8 50 92 D8 FF                  call 0x1406c6c40
0093D9F0  41 BE 01 00 00 00               mov r14d, 1
0093D9F6  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
0093D9FD  45 8B CE                        mov r9d, r14d
0093DA00  8D 5E 01                        lea ebx, [rsi + 1]
0093DA03  45 8B C6                        mov r8d, r14d
0093DA06  41 8D 56 0F                     lea edx, [r14 + 0xf]
0093DA0A  E8 41 59 A9 FF                  call 0x1403d3350
0093DA0F  8B 4D D0                        mov ecx, dword ptr [rbp - 0x30]
0093DA12  E8 19 AB 97 FF                  call 0x1402b8530
0093DA17  48 8B 75 98                     mov rsi, qword ptr [rbp - 0x68]
0093DA1B  48 8D 4D 50                     lea rcx, [rbp + 0x50]
0093DA1F  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
0093DA23  45 8D 46 01                     lea r8d, [r14 + 1]
0093DA27  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0093DA2C  45 33 C9                        xor r9d, r9d
0093DA2F  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0093DA34  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
0093DA3B  48 83 64 24 50 00               and qword ptr [rsp + 0x50], 0
0093DA41  C7 44 24 48 09 00 00 00         mov dword ptr [rsp + 0x48], 9
0093DA49  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0093DA4E  48 8B CE                        mov rcx, rsi
0093DA51  48 83 4C 24 38 FF               or qword ptr [rsp + 0x38], 0xffffffffffffffff
0093DA57  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
0093DA5C  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0093DA60  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0093DA64  E8 57 8D AF FF                  call 0x1404367c0
0093DA69  48 8D 4D 50                     lea rcx, [rbp + 0x50]
0093DA6D  E8 BE 26 9F FF                  call 0x140330130
0093DA72  48 8B 9D B8 00 00 00            mov rbx, qword ptr [rbp + 0xb8]
0093DA79  48 85 DB                        test rbx, rbx
0093DA7C  74 10                           je 0x14093da8e
0093DA7E  49 8D 4F 28                     lea rcx, [r15 + 0x28]
0093DA82  48 8D 95 A8 00 00 00            lea rdx, [rbp + 0xa8]
0093DA89  E8 66 96 B1 FF                  call 0x1404570f4
0093DA8E  48 3B DF                        cmp rbx, rdi
0093DA91  0F 85 CF 06 00 00               jne 0x14093e166
0093DA97  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
0093DA9B  49 8B CF                        mov rcx, r15
0093DA9E  4C 8B 4D 20                     mov r9, qword ptr [rbp + 0x20]
0093DAA2  49 2B C7                        sub rax, r15
0093DAA5  4C 8B 45 28                     mov r8, qword ptr [rbp + 0x28]
0093DAA9  48 2D F0 00 00 00               sub rax, 0xf0
0093DAAF  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
0093DAB3  48 C1 F8 03                     sar rax, 3
0093DAB7  41 89 87 C4 00 00 00            mov dword ptr [r15 + 0xc4], eax
0093DABE  4D 89 AF C8 00 00 00            mov qword ptr [r15 + 0xc8], r13
0093DAC5  E8 92 09 00 00                  call 0x14093e45c
0093DACA  44 8B F0                        mov r14d, eax
0093DACD  49 8D 87 E0 00 00 00            lea rax, [r15 + 0xe0]
0093DAD4  48 39 00                        cmp qword ptr [rax], rax
0093DAD7  74 0D                           je 0x14093dae6
0093DAD9  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0093DADD  4C 89 38                        mov qword ptr [rax], r15
0093DAE0  45 33 FF                        xor r15d, r15d
0093DAE3  45 33 F6                        xor r14d, r14d
0093DAE6  48 8B 5D C8                     mov rbx, qword ptr [rbp - 0x38]
0093DAEA  48 85 DB                        test rbx, rbx
0093DAED  0F 85 9B 06 00 00               jne 0x14093e18e
0093DAF3  4D 85 FF                        test r15, r15
0093DAF6  74 12                           je 0x14093db0a
0093DAF8  49 8B CF                        mov rcx, r15
0093DAFB  E8 70 FA FF FF                  call 0x14093d570
0093DB00  33 D2                           xor edx, edx
0093DB02  49 8B CF                        mov rcx, r15
0093DB05  E8 66 4D 24 00                  call 0x140b82870
0093DB0A  41 8B C6                        mov eax, r14d
0093DB0D  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
0093DB14  48 33 CC                        xor rcx, rsp
0093DB17  E8 24 EB D6 FF                  call 0x1406ac640
0093DB1C  48 8B 9C 24 68 02 00 00         mov rbx, qword ptr [rsp + 0x268]
0093DB24  48 81 C4 10 02 00 00            add rsp, 0x210
0093DB2B  41 5F                           pop r15
0093DB2D  41 5E                           pop r14
0093DB2F  41 5D                           pop r13
0093DB31  41 5C                           pop r12
0093DB33  5F                              pop rdi
0093DB34  5E                              pop rsi
0093DB35  5D                              pop rbp
0093DB36  C3                              ret
0093DB37  CC                              int3
0093DB38  49 8B CC                        mov rcx, r12
0093DB3B  E8 D0 FF 90 FF                  call 0x14024db10
0093DB40  4C 8B B5 70 01 00 00            mov r14, qword ptr [rbp + 0x170]
0093DB47  48 8B C8                        mov rcx, rax
0093DB4A  4D 85 F6                        test r14, r14
0093DB4D  0F 84 74 03 00 00               je 0x14093dec7
0093DB53  49 8B D6                        mov rdx, r14
0093DB56  B8 FF FF FF FF                  mov eax, 0xffffffff
0093DB5B  48 C1 EA 0C                     shr rdx, 0xc
0093DB5F  48 89 55 00                     mov qword ptr [rbp], rdx
0093DB63  48 3B D0                        cmp rdx, rax
0093DB66  0F 87 0D 04 00 00               ja 0x14093df79
0093DB6C  8B C2                           mov eax, edx
0093DB6E  48 3B C1                        cmp rax, rcx
0093DB71  0F 87 02 04 00 00               ja 0x14093df79
0093DB77  8B F2                           mov esi, edx
0093DB79  4D 85 FF                        test r15, r15
0093DB7C  74 17                           je 0x14093db95
0093DB7E  48 8B C3                        mov rax, rbx
0093DB81  48 C1 F8 0C                     sar rax, 0xc
0093DB85  83 E0 3F                        and eax, 0x3f
0093DB88  48 03 C6                        add rax, rsi
0093DB8B  48 83 F8 40                     cmp rax, 0x40
0093DB8F  0F 87 E4 03 00 00               ja 0x14093df79
0093DB95  8B CA                           mov ecx, edx
0093DB97  E8 54 F9 FF FF                  call 0x14093d4f0
0093DB9C  4C 8B F8                        mov r15, rax
0093DB9F  48 85 C0                        test rax, rax
0093DBA2  0F 84 4A 05 00 00               je 0x14093e0f2
0093DBA8  4C 89 60 08                     mov qword ptr [rax + 8], r12
0093DBAC  B9 FF 01 00 00                  mov ecx, 0x1ff
0093DBB1  F7 05 FD 8E 68 00 00 00 20 00   test dword ptr [rip + 0x688efd], 0x200000
0093DBBB  0F 85 48 05 00 00               jne 0x14093e109
0093DBC1  33 F6                           xor esi, esi
0093DBC3  4D 8D AC 24 80 00 00 00         lea r13, [r12 + 0x80]
0093DBCB  48 89 75 D8                     mov qword ptr [rbp - 0x28], rsi
0093DBCF  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0093DBD3  D1 E8                           shr eax, 1
0093DBD5  83 E0 1F                        and eax, 0x1f
0093DBD8  48 89 75 90                     mov qword ptr [rbp - 0x70], rsi
0093DBDC  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
0093DBE0  48 89 75 80                     mov qword ptr [rbp - 0x80], rsi
0093DBE4  48 89 75 08                     mov qword ptr [rbp + 8], rsi
0093DBE8  89 45 D0                        mov dword ptr [rbp - 0x30], eax
0093DBEB  4D 85 F6                        test r14, r14
0093DBEE  74 12                           je 0x14093dc02
0093DBF0  4C 8D 45 D8                     lea r8, [rbp - 0x28]
0093DBF4  48 8B D3                        mov rdx, rbx
0093DBF7  49 8B CC                        mov rcx, r12
0093DBFA  E8 81 FC 90 FF                  call 0x14024d880
0093DBFF  4C 8B E8                        mov r13, rax
0093DC02  49 8B CC                        mov rcx, r12
0093DC05  E8 56 09 B0 FF                  call 0x14043e560
0093DC0A  48 8B C8                        mov rcx, rax
0093DC0D  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0093DC11  E8 0E 5D B4 FF                  call 0x140483924
0093DC16  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0093DC1A  4C 8B E6                        mov r12, rsi
0093DC1D  48 89 75 E0                     mov qword ptr [rbp - 0x20], rsi
0093DC21  48 89 75 E8                     mov qword ptr [rbp - 0x18], rsi
0093DC25  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
0093DC29  48 85 FF                        test rdi, rdi
0093DC2C  0F 85 D7 02 00 00               jne 0x14093df09
0093DC32  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
0093DC36  48 8B FE                        mov rdi, rsi
0093DC39  48 8B 5D 88                     mov rbx, qword ptr [rbp - 0x78]
0093DC3D  49 8D 87 F0 00 00 00            lea rax, [r15 + 0xf0]
0093DC44  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0093DC48  4C 8D 4D 38                     lea r9, [rbp + 0x38]
0093DC4C  8B 85 78 01 00 00               mov eax, dword ptr [rbp + 0x178]
0093DC52  BA 03 00 00 00                  mov edx, 3
0093DC57  41 89 87 B8 00 00 00            mov dword ptr [r15 + 0xb8], eax
0093DC5E  41 C7 87 BC 00 00 00 05 00 00 00  mov dword ptr [r15 + 0xbc], 5
0093DC69  41 C7 87 C0 00 00 00 07 00 00 00  mov dword ptr [r15 + 0xc0], 7
0093DC74  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0093DC7D  44 8B 43 38                     mov r8d, dword ptr [rbx + 0x38]
0093DC81  41 C1 E8 14                     shr r8d, 0x14
0093DC85  41 83 E0 7F                     and r8d, 0x7f
0093DC89  89 75 A0                        mov dword ptr [rbp - 0x60], esi
0093DC8C  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
0093DC93  48 05 00 04 00 00               add rax, 0x400
0093DC99  48 8B C8                        mov rcx, rax
0093DC9C  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0093DCA0  E8 6B 27 9E FF                  call 0x140320410
0093DCA5  48 8D 4D 38                     lea rcx, [rbp + 0x38]
0093DCA9  E8 06 84 B2 FF                  call 0x1404660b4
0093DCAE  45 33 D2                        xor r10d, r10d
0093DCB1  45 33 F6                        xor r14d, r14d
0093DCB4  8B F0                           mov esi, eax
0093DCB6  4C 89 55 A8                     mov qword ptr [rbp - 0x58], r10
0093DCBA  33 C0                           xor eax, eax
0093DCBC  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
0093DCBF  3B 45 00                        cmp eax, dword ptr [rbp]
0093DCC2  0F 83 CF 03 00 00               jae 0x14093e097
0093DCC8  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
0093DCCC  4C 3B E1                        cmp r12, rcx
0093DCCF  0F 83 6C 01 00 00               jae 0x14093de41
0093DCD5  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
0093DCD9  4C 8B 45 B8                     mov r8, qword ptr [rbp - 0x48]
0093DCDD  49 8B 1C 24                     mov rbx, qword ptr [r12]
0093DCE1  F6 C3 01                        test bl, 1
0093DCE4  0F 85 40 01 00 00               jne 0x14093de2a
0093DCEA  48 0F BA E3 0A                  bt rbx, 0xa
0093DCEF  0F 83 F7 00 00 00               jae 0x14093ddec
0093DCF5  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0093DCF9  8A 40 3E                        mov al, byte ptr [rax + 0x3e]
0093DCFC  24 0C                           and al, 0xc
0093DCFE  3C 04                           cmp al, 4
0093DD00  0F 84 3C 02 00 00               je 0x14093df42
0093DD06  48 85 D2                        test rdx, rdx
0093DD09  0F 85 F6 00 00 00               jne 0x14093de05
0093DD0F  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0093DD13  4D 8B C4                        mov r8, r12
0093DD16  4C 8B 4D F8                     mov r9, qword ptr [rbp - 8]
0093DD1A  48 85 C9                        test rcx, rcx
0093DD1D  49 8B C1                        mov rax, r9
0093DD20  48 0F 45 C1                     cmovne rax, rcx
0093DD24  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0093DD28  4D 89 21                        mov qword ptr [r9], r12
0093DD2B  4D 3B D5                        cmp r10, r13
0093DD2E  0F 84 96 00 00 00               je 0x14093ddca
0093DD34  49 83 C8 02                     or r8, 2
0093DD38  4C 89 6D A8                     mov qword ptr [rbp - 0x58], r13
0093DD3C  4D 89 01                        mov qword ptr [r9], r8
0093DD3F  4C 89 65 08                     mov qword ptr [rbp + 8], r12
0093DD43  4C 3B 65 E8                     cmp r12, qword ptr [rbp - 0x18]
0093DD47  0F 84 B0 03 00 00               je 0x14093e0fd
0093DD4D  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0093DD51  BA 01 00 00 00                  mov edx, 1
0093DD56  49 83 C1 08                     add r9, 8
0093DD5A  44 8B C2                        mov r8d, edx
0093DD5D  4C 89 4D F8                     mov qword ptr [rbp - 8], r9
0093DD61  E8 4A D1 94 FF                  call 0x14028aeb0
0093DD66  48 85 C0                        test rax, rax
0093DD69  0F 84 34 FC FF FF               je 0x14093d9a3
0093DD6F  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0093DD73  48 8D 45 A0                     lea rax, [rbp - 0x60]
0093DD77  44 8B CE                        mov r9d, esi
0093DD7A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0093DD7F  4C 8B C3                        mov r8, rbx
0093DD82  49 8B D5                        mov rdx, r13
0093DD85  E8 DE 7E A2 FF                  call 0x140365c68
0093DD8A  85 C0                           test eax, eax
0093DD8C  0F 85 9F 01 00 00               jne 0x14093df31
0093DD92  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
0093DD96  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
0093DD9A  48 05 A0 00 00 00               add rax, 0xa0
0093DDA0  48 3B C8                        cmp rcx, rax
0093DDA3  0F 87 1A 03 00 00               ja 0x14093e0c3
0093DDA9  48 FF C1                        inc rcx
0093DDAC  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
0093DDB0  48 FF 45 90                     inc qword ptr [rbp - 0x70]
0093DDB4  48 8B 5D 88                     mov rbx, qword ptr [rbp - 0x78]
0093DDB8  8B 45 A4                        mov eax, dword ptr [rbp - 0x5c]
0093DDBB  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0093DDBF  FF C0                           inc eax
0093DDC1  49 83 C4 08                     add r12, 8
0093DDC5  E9 F2 FE FF FF                  jmp 0x14093dcbc
0093DDCA  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
0093DDCE  E8 5D 03 B0 FF                  call 0x14043e130
0093DDD3  49 8B CC                        mov rcx, r12
0093DDD6  48 8B D0                        mov rdx, rax
0093DDD9  E8 52 03 B0 FF                  call 0x14043e130
0093DDDE  48 3B D0                        cmp rdx, rax
0093DDE1  0F 85 4D FF FF FF               jne 0x14093dd34
0093DDE7  E9 53 FF FF FF                  jmp 0x14093dd3f
0093DDEC  48 0F BA E3 0B                  bt rbx, 0xb
0093DDF1  72 37                           jb 0x14093de2a
0093DDF3  48 8B CB                        mov rcx, rbx
0093DDF6  E8 D5 16 8F FF                  call 0x14022f4d0
0093DDFB  85 C0                           test eax, eax
0093DDFD  0F 85 0C FF FF FF               jne 0x14093dd0f
0093DE03  EB AF                           jmp 0x14093ddb4
0093DE05  49 8B C4                        mov rax, r12
0093DE08  4C 89 65 B8                     mov qword ptr [rbp - 0x48], r12
0093DE0C  49 2B C0                        sub rax, r8
0093DE0F  48 C1 F8 03                     sar rax, 3
0093DE13  48 C1 E0 0C                     shl rax, 0xc
0093DE17  48 03 F8                        add rdi, rax
0093DE1A  48 89 3A                        mov qword ptr [rdx], rdi
0093DE1D  48 83 C2 08                     add rdx, 8
0093DE21  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
0093DE25  E9 E5 FE FF FF                  jmp 0x14093dd0f
0093DE2A  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
0093DE2E  49 8B CC                        mov rcx, r12
0093DE31  8B 95 78 01 00 00               mov edx, dword ptr [rbp + 0x178]
0093DE37  E8 D4 33 9E FF                  call 0x140321210
0093DE3C  E9 73 FF FF FF                  jmp 0x14093ddb4
0093DE41  4D 85 E4                        test r12, r12
0093DE44  0F 85 A8 00 00 00               jne 0x14093def2
0093DE4A  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0093DE4D  A8 20                           test al, 0x20
0093DE4F  0F 85 4C 01 00 00               jne 0x14093dfa1
0093DE55  41 8B 55 2C                     mov edx, dword ptr [r13 + 0x2c]
0093DE59  41 B8 04 00 00 00               mov r8d, 4
0093DE5F  49 8B CD                        mov rcx, r13
0093DE62  E8 29 6B 9E FF                  call 0x140324990
0093DE67  44 8B F0                        mov r14d, eax
0093DE6A  85 C0                           test eax, eax
0093DE6C  0F 88 D3 02 00 00               js 0x14093e145
0093DE72  4D 8B 65 08                     mov r12, qword ptr [r13 + 8]
0093DE76  49 8D 5F 18                     lea rbx, [r15 + 0x18]
0093DE7A  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
0093DE7E  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
0093DE83  48 39 1B                        cmp qword ptr [rbx], rbx
0093DE86  74 0A                           je 0x14093de92
0093DE88  83 79 10 05                     cmp dword ptr [rcx + 0x10], 5
0093DE8C  0F 85 69 01 00 00               jne 0x14093dffb
0093DE92  BA 40 00 00 00                  mov edx, 0x40
0093DE97  B9 00 01 00 00                  mov ecx, 0x100
0093DE9C  41 B8 4D 6D 53 6C               mov r8d, 0x6c536d4d
0093DEA2  E8 99 D6 A1 FF                  call 0x14035b540
0093DEA7  48 8B C8                        mov rcx, rax
0093DEAA  48 85 C0                        test rax, rax
0093DEAD  0F 84 D1 00 00 00               je 0x14093df84
0093DEB3  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0093DEB7  48 39 18                        cmp qword ptr [rax], rbx
0093DEBA  0F 84 2D 01 00 00               je 0x14093dfed
0093DEC0  B9 03 00 00 00                  mov ecx, 3
0093DEC5  CD 29                           int 0x29
0093DEC7  48 B8 00 00 00 00 01 00 00 00   movabs rax, 0x100000000
0093DED1  48 3B C8                        cmp rcx, rax
0093DED4  0F 83 9F 00 00 00               jae 0x14093df79
0093DEDA  8B D1                           mov edx, ecx
0093DEDC  48 89 55 00                     mov qword ptr [rbp], rdx
0093DEE0  E9 92 FC FF FF                  jmp 0x14093db77
0093DEE5  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0093DEE9  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0093DEED  E9 D9 FA FF FF                  jmp 0x14093d9cb
0093DEF2  4D 8B 6D 10                     mov r13, qword ptr [r13 + 0x10]
0093DEF6  4D 85 ED                        test r13, r13
0093DEF9  0F 84 98 01 00 00               je 0x14093e097
0093DEFF  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
0093DF04  E9 41 FF FF FF                  jmp 0x14093de4a
0093DF09  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0093DF0D  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
0093DF11  8B 4F 0C                        mov ecx, dword ptr [rdi + 0xc]
0093DF14  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
0093DF19  81 E1 FF 01 00 00               and ecx, 0x1ff
0093DF1F  0F BA E9 09                     bts ecx, 9
0093DF23  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
0093DF27  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
0093DF2C  E9 08 FD FF FF                  jmp 0x14093dc39
0093DF31  8B 5D A0                        mov ebx, dword ptr [rbp - 0x60]
0093DF34  83 FB 04                        cmp ebx, 4
0093DF37  0F 87 55 FE FF FF               ja 0x14093dd92
0093DF3D  E9 FC 72 1E 00                  jmp 0x140b2523e
0093DF42  44 8B 44 24 78                  mov r8d, dword ptr [rsp + 0x78]
0093DF47  49 8B D4                        mov rdx, r12
0093DF4A  49 8B CD                        mov rcx, r13
0093DF4D  E8 36 BA B3 FF                  call 0x140479988
0093DF52  44 8B F0                        mov r14d, eax
0093DF55  85 C0                           test eax, eax
0093DF57  0F 89 57 FE FF FF               jns 0x14093ddb4
0093DF5D  4C 8B 65 90                     mov r12, qword ptr [rbp - 0x70]
0093DF61  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
0093DF65  4D 85 E4                        test r12, r12
0093DF68  0F 85 50 FA FF FF               jne 0x14093d9be
0093DF6E  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
0093DF74  E9 45 FA FF FF                  jmp 0x14093d9be
0093DF79  41 BE F1 00 00 C0               mov r14d, 0xc00000f1
0093DF7F  E9 86 FB FF FF                  jmp 0x14093db0a
0093DF84  41 8B 55 2C                     mov edx, dword ptr [r13 + 0x2c]
0093DF88  41 B8 04 00 00 00               mov r8d, 4
0093DF8E  49 8B CD                        mov rcx, r13
0093DF91  E8 3E A7 95 FF                  call 0x1402986d4
0093DF96  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
0093DF9C  E9 45 FB FF FF                  jmp 0x14093dae6
0093DFA1  4D 8B 65 08                     mov r12, qword ptr [r13 + 8]
0093DFA5  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0093DFA9  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
0093DFAE  0F BA E0 11                     bt eax, 0x11
0093DFB2  73 5D                           jae 0x14093e011
0093DFB4  F7 43 38 00 00 00 08            test dword ptr [rbx + 0x38], 0x8000000
0093DFBB  74 54                           je 0x14093e011
0093DFBD  49 83 7D 18 00                  cmp qword ptr [r13 + 0x18], 0
0093DFC2  0F 84 F2 00 00 00               je 0x14093e0ba
0093DFC8  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
0093DFCC  4D 8B C5                        mov r8, r13
0093DFCF  48 8B CB                        mov rcx, rbx
0093DFD2  E8 81 AD A0 FF                  call 0x140348d58
0093DFD7  48 85 C0                        test rax, rax
0093DFDA  0F 85 50 72 1E 00               jne 0x140b25230
0093DFE0  4C 8B 65 E0                     mov r12, qword ptr [rbp - 0x20]
0093DFE4  49 83 C4 F8                     add r12, -8
0093DFE8  E9 CB FD FF FF                  jmp 0x14093ddb8
0093DFED  48 89 19                        mov qword ptr [rcx], rbx
0093DFF0  48 89 41 08                     mov qword ptr [rcx + 8], rax
0093DFF4  48 89 08                        mov qword ptr [rax], rcx
0093DFF7  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
0093DFFB  49 83 7F 10 00                  cmp qword ptr [r15 + 0x10], 0
0093E000  75 04                           jne 0x14093e006
0093E002  4D 89 6F 10                     mov qword ptr [r15 + 0x10], r13
0093E006  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
0093E009  4C 89 6C C1 18                  mov qword ptr [rcx + rax*8 + 0x18], r13
0093E00E  FF 41 10                        inc dword ptr [rcx + 0x10]
0093E011  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
0093E015  49 8B CD                        mov rcx, r13
0093E018  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0093E01D  44 8B 44 24 78                  mov r8d, dword ptr [rsp + 0x78]
0093E022  4D 8D 24 C4                     lea r12, [r12 + rax*8]
0093E026  41 8B 45 2C                     mov eax, dword ptr [r13 + 0x2c]
0093E02A  48 8D 04 C2                     lea rax, [rdx + rax*8]
0093E02E  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0093E032  E8 A9 A2 A0 FF                  call 0x1403482e0
0093E037  49 8B CD                        mov rcx, r13
0093E03A  48 8B D8                        mov rbx, rax
0093E03D  E8 D6 66 AC FF                  call 0x140404718
0093E042  8B C8                           mov ecx, eax
0093E044  2B CB                           sub ecx, ebx
0093E046  F7 C1 FF 0F 00 00               test ecx, 0xfff
0093E04C  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0093E051  75 4D                           jne 0x14093e0a0
0093E053  48 83 65 E8 00                  and qword ptr [rbp - 0x18], 0
0093E058  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
0093E05C  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0093E060  48 85 D2                        test rdx, rdx
0093E063  0F 84 70 FC FF FF               je 0x14093dcd9
0093E069  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
0093E06E  4C 8B C1                        mov r8, rcx
0093E071  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
0093E075  8B C3                           mov eax, ebx
0093E077  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
0093E07B  33 41 0C                        xor eax, dword ptr [rcx + 0xc]
0093E07E  25 FF 01 00 00                  and eax, 0x1ff
0093E083  33 C3                           xor eax, ebx
0093E085  0F BA E8 09                     bts eax, 9
0093E089  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
0093E08D  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
0093E092  E9 46 FC FF FF                  jmp 0x14093dcdd
0093E097  4C 8B 65 90                     mov r12, qword ptr [rbp - 0x70]
0093E09B  E9 1A F9 FF FF                  jmp 0x14093d9ba
0093E0A0  48 2B C3                        sub rax, rbx
0093E0A3  48 05 FF 0F 00 00               add rax, 0xfff
0093E0A9  48 C1 E8 0C                     shr rax, 0xc
0093E0AD  48 FF C8                        dec rax
0093E0B0  48 8D 04 C1                     lea rax, [rcx + rax*8]
0093E0B4  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0093E0B8  EB 9E                           jmp 0x14093e058
0093E0BA  4C 8D 61 F8                     lea r12, [rcx - 8]
0093E0BE  E9 F5 FC FF FF                  jmp 0x14093ddb8
0093E0C3  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0093E0C7  B8 01 00 00 00                  mov eax, 1
0093E0CC  44 8B C0                        mov r8d, eax
0093E0CF  8B D0                           mov edx, eax
0093E0D1  E8 52 F8 A2 FF                  call 0x14036d928
0093E0D6  4C 8B 65 90                     mov r12, qword ptr [rbp - 0x70]
0093E0DA  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
0093E0DE  4D 85 E4                        test r12, r12
0093E0E1  0F 85 D7 F8 FF FF               jne 0x14093d9be
0093E0E7  41 BE 17 00 00 C0               mov r14d, 0xc0000017
0093E0ED  E9 CC F8 FF FF                  jmp 0x14093d9be
0093E0F2  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
0093E0F8  E9 0D FA FF FF                  jmp 0x14093db0a
0093E0FD  49 83 C8 01                     or r8, 1
0093E101  4D 89 01                        mov qword ptr [r9], r8
0093E104  E9 44 FC FF FF                  jmp 0x14093dd4d
0093E109  48 3B F1                        cmp rsi, rcx
0093E10C  48 8B F9                        mov rdi, rcx
0093E10F  B9 42 00 00 00                  mov ecx, 0x42
0093E114  41 B8 4D 69 68 6C               mov r8d, 0x6c68694d
0093E11A  48 0F 46 FE                     cmovbe rdi, rsi
0093E11E  48 8D 14 FD 10 00 00 00         lea rdx, [rdi*8 + 0x10]
0093E126  E8 15 D4 A1 FF                  call 0x14035b540
0093E12B  33 F6                           xor esi, esi
0093E12D  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0093E131  48 85 C0                        test rax, rax
0093E134  0F 85 DA 70 1E 00               jne 0x140b25214
0093E13A  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
0093E140  E9 B3 F9 FF FF                  jmp 0x14093daf8
0093E145  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
0093E149  48 85 D2                        test rdx, rdx
0093E14C  0F 84 94 F9 FF FF               je 0x14093dae6
0093E152  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0093E156  41 B8 01 00 00 00               mov r8d, 1
0093E15C  E8 C7 F7 A2 FF                  call 0x14036d928
0093E161  E9 80 F9 FF FF                  jmp 0x14093dae6
0093E166  48 8B D7                        mov rdx, rdi
0093E169  45 8B C6                        mov r8d, r14d
0093E16C  48 2B D3                        sub rdx, rbx
0093E16F  48 8B CE                        mov rcx, rsi
0093E172  E8 B1 F7 A2 FF                  call 0x14036d928
0093E177  48 2B DF                        sub rbx, rdi
0093E17A  4C 03 E3                        add r12, rbx
0093E17D  0F 85 14 F9 FF FF               jne 0x14093da97
0093E183  41 BE 17 00 00 C0               mov r14d, 0xc0000017
0093E189  E9 58 F9 FF FF                  jmp 0x14093dae6
0093E18E  83 7B 04 00                     cmp dword ptr [rbx + 4], 0
0093E192  0F 84 07 71 1E 00               je 0x140b2529f
0093E198  48 8B CB                        mov rcx, rbx
0093E19B  E8 BC 7F B0 FF                  call 0x14044615c
0093E1A0  90                              nop
0093E1A1  E9 F9 70 1E 00                  jmp 0x140b2529f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPfPrepareSequentialReadList(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, __int64 a8, __int64 a9)
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
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned int v_stack_m1A4;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned int v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned int v_stack_m218;
    unsigned int v_stack_m220;
    unsigned int v_stack_m228;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (528);
    result = (*(unsigned __int64 *)(v_rip + 5033522)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r13 = 0;
    v_stack_m1D0 = (unsigned int)((unsigned int)(a7));
    v_stack_m128 = a8;
    v_stack_m158 = a1;
    a1 = 0;
    v_stack_m120 = a4;
    v_stack_m1C0 = a2;
    *(unsigned __int64 *)(a9) = 0;
    v_stack_m118 = a9;
    v_stack_m110 = v_xmm0;
    v_stack_m58 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m50 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m180 = 0;
    v_stack_m68 = v_xmm0;
    if (((*(unsigned int *)(a2 + 56)) & (0x400ULL)) != 0) goto loc_0093D998;
    if ((*(unsigned __int64 *)(a2 + 64)) != 0) goto loc_0093DB38;
loc_0093D998:
    goto loc_0093DB0A;
loc_0093D9A3:
    result = (unsigned int)((unsigned int)((unsigned int)(0xC00000EFULL)));
    if (v_stack_m1B8 == 0) { result = (unsigned int)((unsigned int)(0xC000009AULL)); }
loc_0093D9BA:
loc_0093D9BE:
    if (v_stack_m158 != 0) goto loc_0093DEE5;
loc_0093D9CB:
    if (v_stack_m1B8 == 0) goto loc_0093DAE6;
    if (v_stack_m188 == 0) goto loc_0093DA97;
    a2 = 0;
    result = memset(v_stack_mF8, a2, a2 + 112, a4);
    result = MiInitializeDemandCoalesceContext(v_stack_m88, 1 + 15, 1, 1);
    result = MiProtectionToCacheAttribute((unsigned int)(v_stack_m178), 1 + 15, 1, 1);
    v_stack_m1E8 = v_stack_mF8;
    a4 = 0;
    v_stack_m1F0 = v_stack_m188;
    v_stack_m200 = 9;
    v_stack_m208 = v_stack_m88;
    v_stack_m220 = (unsigned int)(result);
    v_stack_m228 = (unsigned int)(v_rsi + 1);
    result = MiInitializePageChainPacket(v_stack_m1B0, v_stack_m130, 1 + 1, a4);
    result = MiGetPageChain(v_stack_mF8, v_stack_m130, 1 + 1, a4);
    if (v_stack_m90 != 0) {
        a1 = a4 + 40;
        a2 = v_stack_mA0;
        result = MiAppendPageChain(a1, a2, 1 + 1, a4);
    }
    if (v_stack_m90 != v_stack_m188) goto loc_0093E166;
loc_0093DA97:
    result = (v_stack_m150) - (0);
    result = (result) - (240);
    result = (result) >> (3);
    *(unsigned int *)(a4 + 196) = (unsigned int)(result);
    *(unsigned __int64 *)(a4 + 200) = v_stack_m1C8;
    result = MiPfAllocateMdls(0, (unsigned int)(v_stack_m1D0), v_stack_m120, v_stack_m128);
    result = a4 + 224;
    v_r14 = (unsigned int)((unsigned int)(result));
    v_r15 = a4;
    if ((*(unsigned __int64 *)(a4 + 224)) != (a4 + 224)) {
        result = v_stack_m118;
        *(unsigned __int64 *)(result) = 0;
        v_r15 = 0;
        v_r14 = 0;
    }
    if (v_stack_m180 != 0) goto loc_0093E18E;
    if (0 != 0) {
        a1 = 0;
        result = MiReleaseReadListResources(a1, (unsigned int)(v_stack_m1D0), v_stack_m120, v_stack_m128);
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, v_stack_m120, v_stack_m128);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m120, v_stack_m128);
    v_rsp = (v_rsp) + (528);
    return result;
loc_0093DB38:
    result = MiGetControlAreaPtes(v_stack_m1B8, a2, v_stack_m120, v_stack_m128);
    if (a5 == 0) goto loc_0093DEC7;
    a2 = (a5) >> (12);
    v_stack_m148 = a2;
    if (a2 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_0093DF79;
    if (((unsigned int)((unsigned int)(a2))) > result) goto loc_0093DF79;
loc_0093DB77:
    if (0 == 0) goto loc_0093DB95;
    result = (v_stack_p20) >> (12);
    result = (unsigned int)((result) & (63));
    result = (result) + ((unsigned int)((unsigned int)(a2)));
    if (result > 64) goto loc_0093DF79;
loc_0093DB95:
    result = MiAllocateReadList((unsigned int)((unsigned int)(a2)), a2, v_stack_m120, v_stack_m128);
    if (result == 0) goto loc_0093E0F2;
    *(unsigned __int64 *)(result + 8) = v_stack_m1B8;
    if (((*(unsigned int *)(v_rip + 6852349)) & (0x200000ULL)) != 0) goto loc_0093E109;
    v_rsi = 0;
    v_stack_m170 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1B8 + 128 + 32))) >> (1));
    result = (unsigned int)((result) & (31));
    v_stack_m1B8 = 0;
    v_stack_m188 = 0;
    v_stack_m1C8 = 0;
    v_stack_m140 = 0;
    v_stack_m178 = (unsigned int)(result);
    v_r13 = v_stack_m1B8 + 128;
    if (a5 != 0) {
        a3 = v_stack_m170;
        a2 = v_stack_p20;
        a1 = v_stack_m1B8;
        result = MiOffsetToProtos(a1, a2, a3, v_stack_m128);
        v_r13 = result;
    }
    result = MiGetControlAreaPartition(v_stack_m1B8, a2, a3, v_stack_m128);
    v_stack_m1B0 = result;
    result = MiGetAvailablePagesExcludeSlists(result, a2, a3, v_stack_m128);
    v_stack_m138 = result;
    v_stack_m168 = 0;
    v_stack_m160 = 0;
    v_stack_m190 = 0;
    if (v_stack_m188 != 0) goto loc_0093DF09;
    v_stack_m198 = 0;
loc_0093DC39:
    v_stack_m150 = result + 240;
    *(unsigned int *)(result + 184) = (unsigned int)((unsigned int)(a6));
    *(unsigned int *)(result + 188) = 5;
    *(unsigned int *)(result + 192) = 7;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1C0 + 56))) >> (20));
    a3 = (unsigned int)((a3) & (127));
    v_stack_m1A8 = 0;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    v_stack_m130 = result;
    result = MiInitializePageColorBase(result, 3, a3, v_stack_m110);
    result = MiColorBaseToNode(v_stack_m110, 3, a3, v_stack_m110);
    v_r10 = 0;
    v_r14 = 0;
    v_stack_m1A0 = 0;
    result = 0;
loc_0093DCBC:
    v_stack_m1A4 = 0;
    if (0 >= v_stack_m148) goto loc_0093E097;
    if (0 >= v_stack_m168) goto loc_0093DE41;
loc_0093DCD9:
loc_0093DCDD:
    if ((((unsigned __int8)(*(unsigned __int64 *)(0))) & (1)) != 0) goto loc_0093DE2A;
    if (condition_is_above_or_equal) goto loc_0093DDEC;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m1C0 + 62)) & (12));
    if (((unsigned __int8)(result)) == 4) goto loc_0093DF42;
    if (v_stack_m198 != 0) goto loc_0093DE05;
loc_0093DD0F:
    result = v_stack_m150;
    if (v_stack_m1C8 != 0) { result = v_stack_m1C8; }
    v_stack_m1C8 = result;
    *(unsigned __int64 *)(v_stack_m150) = 0;
    if (0 == v_r13) goto loc_0093DDCA;
loc_0093DD34:
    a3 = (0) | (2);
    v_stack_m1A0 = v_r13;
    *(unsigned __int64 *)(v_stack_m150) = a3;
loc_0093DD3F:
    v_stack_m140 = 0;
    if (0 == v_stack_m160) goto loc_0093E0FD;
loc_0093DD4D:
    a4 = (v_stack_m150) + (8);
    v_stack_m150 = a4;
    result = MiObtainFaultCharges(v_stack_m1B0, 1, 1, a4);
    if (result == 0) goto loc_0093D9A3;
    v_stack_p20 = v_stack_m1A8;
    result = MiUseSlabAllocator(v_stack_m1B0, v_r13, *(unsigned __int64 *)(0), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if ((unsigned int)(result) != 0) goto loc_0093DF31;
loc_0093DD92:
    result = (v_stack_m138) + (160);
    if (v_stack_m188 > result) goto loc_0093E0C3;
    a1 = (v_stack_m188) + 1;
    v_stack_m188 = a1;
loc_0093DDB4:
loc_0093DDB8:
    result = (unsigned int)(((unsigned int)(v_stack_m1A4)) + 1);
    v_r12 = (0) + (8);
    goto loc_0093DCBC;
loc_0093DDCA:
    result = MiGetPteAddress(v_stack_m140, v_r13, *(unsigned __int64 *)(0), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    result = MiGetPteAddress(v_r12, result, *(unsigned __int64 *)(0), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (result != result) goto loc_0093DD34;
    goto loc_0093DD3F;
loc_0093DDEC:
    if (result < result) goto loc_0093DE2A;
    result = IS_PTE_NOT_DEMAND_ZERO(v_stack_m1C0, result, *(unsigned __int64 *)(0), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if ((unsigned int)(result) != 0) goto loc_0093DD0F;
    goto loc_0093DDB4;
loc_0093DE05:
    v_stack_m190 = v_r12;
    result = (v_r12) - (*(unsigned __int64 *)(0));
    result = (result) >> (3);
    result = (result) << (12);
    v_rdi = (0) + (result);
    *(unsigned __int64 *)(result) = v_rdi;
    a2 = (result) + (8);
    v_stack_m198 = a2;
    goto loc_0093DD0F;
loc_0093DE2A:
    result = MiUpdatePfnForPrefetchByPte(v_r12, (unsigned int)(a6), v_stack_m180, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_0093DDB4;
loc_0093DE41:
    if (v_r12 != 0) goto loc_0093DEF2;
loc_0093DE4A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1C0 + 56)))) & (32)) != 0) goto loc_0093DFA1;
    result = MiAddViewsForSection(v_r13, (unsigned int)(*(unsigned int *)(v_r13 + 44)), 4, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (sign_flag) goto loc_0093E145;
    v_stack_p70 = *(unsigned __int64 *)(v_r13 + 8);
    if ((*(unsigned __int64 *)(result + 24)) == (result + 24)) goto loc_0093DE92;
    if ((*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 16)) != 5) goto loc_0093DFFB;
loc_0093DE92:
    result = MiAllocatePool(256, 64, (unsigned int)(0x6C536D4DULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (result == 0) goto loc_0093DF84;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24 + 8))) == (result + 24)) goto loc_0093DFED;
loc_0093DEC7:
    if (3 >= (*(unsigned __int64 *)(result + 24 + 8))) goto loc_0093DF79;
    v_stack_m148 = 3;
    goto loc_0093DB77;
loc_0093DEE5:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 24 + 8) + 24) = v_stack_m198;
    goto loc_0093D9CB;
loc_0093DEF2:
    if (*(unsigned __int64 *)(v_r13 + 16) == 0) goto loc_0093E097;
    goto loc_0093DE4A;
loc_0093DF09:
    v_stack_m198 = *(unsigned __int64 *)(v_rdi + 32);
    v_stack_p70 = (unsigned int)((unsigned int)(result));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 12))) & (511));
    v_stack_p70 = (unsigned int)(a1);
    goto loc_0093DC39;
loc_0093DF31:
    if (((unsigned int)((unsigned int)(v_stack_m1A8))) > 4) goto loc_0093DD92;
loc_0093DF42:
    result = MiRefillPurgedExtents(*(unsigned __int64 *)(v_r13 + 16), *(unsigned __int64 *)(v_r13 + 8), (unsigned int)(v_stack_p78), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (!sign_flag) goto loc_0093DDB4;
    if (v_stack_m1B8 != 0) goto loc_0093D9BE;
    goto loc_0093D9BE;
loc_0093DF79:
    goto loc_0093DB0A;
loc_0093DF84:
    result = MiRemoveViewsFromSectionWithPfn(v_stack_m1C8, (unsigned int)(*(unsigned int *)(v_stack_m1C8 + 44)), 4, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_0093DAE6;
loc_0093DFA1:
    v_stack_p70 = *(unsigned __int64 *)(v_stack_m1C8 + 8);
    if (condition_is_above_or_equal) goto loc_0093E011;
    if (((*(unsigned int *)((unsigned int)(v_stack_m1A8) + 56)) & (0x8000000ULL)) == 0) goto loc_0093E011;
    if ((*(unsigned __int64 *)(v_stack_m1C8 + 24)) == 0) goto loc_0093E0BA;
    result = MiGetSharedProtos((unsigned int)(v_stack_m1A8), (unsigned int)(v_stack_p78), v_stack_m1C8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_r12 = (v_stack_m168) + (-8);
    goto loc_0093DDB8;
loc_0093DFED:
    *(unsigned __int64 *)((unsigned int)(v_stack_m1A8)) = (unsigned int)(v_stack_m1A8);
    *(unsigned __int64 *)((unsigned int)(v_stack_m1A8) + 8) = result;
    *(unsigned __int64 *)(result) = (unsigned int)(v_stack_m1A8);
    *(unsigned __int64 *)((unsigned int)(v_stack_m1A8) + 8) = (unsigned int)(v_stack_m1A8);
loc_0093DFFB:
    if ((*(unsigned __int64 *)(result + 16)) == 0) {
        *(unsigned __int64 *)(result + 16) = v_stack_m1C8;
    }
    *(unsigned __int64 *)((unsigned int)(v_stack_m1A8) + (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m1A8) + 16)) * 8 + 24) = v_stack_m1C8;
loc_0093E011:
    v_stack_m168 = v_stack_p70 + (unsigned int)(*(unsigned int *)(v_stack_m1C8 + 44)) * 8;
    result = MiStartingOffset(v_stack_m1C8, v_stack_p70, (unsigned int)(v_stack_p78), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    result = MiEndingOffsetWithLock(v_stack_m1C8, v_stack_p70, (unsigned int)(v_stack_p78), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) - ((unsigned int)(result)));
    if ((((unsigned int)(a1)) & (0xFFFULL)) != 0) goto loc_0093E0A0;
loc_0093E058:
    if (v_stack_m198 == 0) goto loc_0093DCD9;
    v_stack_p70 = result;
    v_stack_m190 = v_stack_p70;
    result = (unsigned int)(((unsigned int)((unsigned int)(result))) ^ (*(unsigned int *)(v_stack_m158 + 12)));
    result = (unsigned int)((result) & (511));
    result = (unsigned int)((result) ^ ((unsigned int)(result)));
    v_stack_p70 = (unsigned int)(result);
    goto loc_0093DCDD;
loc_0093E097:
    goto loc_0093D9BA;
loc_0093E0A0:
    result = (result) - (result);
    result = (result) + (0xFFFULL);
    result = (result) >> (12);
    result = (result) - 1;
    v_stack_m160 = v_stack_m158 + result * 8;
    goto loc_0093E058;
loc_0093E0BA:
    goto loc_0093DDB8;
loc_0093E0C3:
    result = MiReturnFaultCharges(v_stack_m1B0, 1, 1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (v_stack_m1B8 != 0) goto loc_0093D9BE;
    goto loc_0093D9BE;
loc_0093E0F2:
    goto loc_0093DB0A;
loc_0093E0FD:
    a3 = (1) | (1);
    *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) = a3;
    goto loc_0093DD4D;
loc_0093E109:
    v_rdi = v_stack_m1B0;
    if (((unsigned int)((unsigned int)(result))) <= v_stack_m1B0) { v_rdi = (unsigned int)((unsigned int)(result)); }
    result = MiAllocatePool(66, v_rdi * 8 + 16, (unsigned int)(0x6C68694DULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_rsi = 0;
    v_stack_m180 = result;
    goto loc_0093DAF8;
loc_0093E145:
    if (v_stack_m188 == 0) goto loc_0093DAE6;
    result = MiReturnFaultCharges(v_stack_m1B0, v_stack_m188, 1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_0093DAE6;
loc_0093E166:
    a2 = (v_rdi) - (result);
    result = MiReturnFaultCharges(0, a2, (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_rbx = (result) - (v_rdi);
    v_r12 = (v_stack_m1B8) + (v_rbx);
    if (condition_is_not_equal) goto loc_0093DA97;
    goto loc_0093DAE6;
loc_0093E18E:
    result = MiIssuePageHeatList(v_rbx, a2, (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
}
```

## 5. (Beta) C Style

```c
int64_t MiPfPrepareSequentialReadList(int64_t Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, int64_t Arg8, void *Arg9)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg9 = (uint8_t *)Arg9;

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
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint32_t v_stack_m1A4;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint32_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint32_t v_stack_m218;
    uint32_t v_stack_m220;
    uint32_t v_stack_m228;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (528);
    result = (*(uint64_t *)(v_rip + 0x4CCE32)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r13 = 0;
    v_stack_m1D0 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m128 = Arg8;
    v_stack_m158 = Arg1;
    Arg1 = 0;
    v_stack_m120 = Arg4;
    v_stack_m1C0 = Arg2;
    *(uint64_t *)(arg9) = 0;
    v_stack_m118 = Arg9;
    v_stack_m110 = v_xmm0;
    v_stack_m58 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m50 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m180 = 0;
    v_stack_m68 = v_xmm0;
    if (((*(uint32_t *)(arg2 + 0x38)) & (0x400ULL)) != 0) goto loc_0093D998;
    if ((*(uint64_t *)(arg2 + 0x40)) != 0) goto loc_0093DB38;
loc_0093D998:
    goto loc_0093DB0A;
loc_0093D9A3:
    result = (uint32_t)((uint32_t)((uint32_t)(0xC00000EFULL)));
    if (v_stack_m1B8 == 0) { result = (uint32_t)((uint32_t)(0xC000009AULL)); }
loc_0093D9BA:
loc_0093D9BE:
    if (v_stack_m158 != 0) goto loc_0093DEE5;
loc_0093D9CB:
    if (v_stack_m1B8 == 0) goto loc_0093DAE6;
    if (v_stack_m188 == 0) goto loc_0093DA97;
    Arg2 = 0;
    result = memset(v_stack_mF8, Arg2, Arg2 + 112, Arg4);
    result = MiInitializeDemandCoalesceContext(v_stack_m88, 1 + 15, 1, 1);
    result = MiProtectionToCacheAttribute((uint32_t)(v_stack_m178), 1 + 15, 1, 1);
    v_stack_m1E8 = v_stack_mF8;
    Arg4 = 0;
    v_stack_m1F0 = v_stack_m188;
    v_stack_m200 = 9;
    v_stack_m208 = v_stack_m88;
    v_stack_m220 = (uint32_t)(result);
    v_stack_m228 = (uint32_t)(local_rsi + 1);
    result = MiInitializePageChainPacket(v_stack_m1B0, v_stack_m130, 1 + 1, Arg4);
    result = MiGetPageChain(v_stack_mF8, v_stack_m130, 1 + 1, Arg4);
    if (v_stack_m90 != 0) {
        Arg1 = Arg4 + 40;
        Arg2 = v_stack_mA0;
        result = MiAppendPageChain(Arg1, Arg2, 1 + 1, Arg4);
    }
    if (v_stack_m90 != v_stack_m188) goto loc_0093E166;
loc_0093DA97:
    result = (v_stack_m150) - (0);
    result = (result) - (240);
    result = (result) >> (3);
    *(uint32_t *)(Arg4 + 0xC4) = (uint32_t)(result);
    *(uint64_t *)(Arg4 + 0xC8) = v_stack_m1C8;
    result = MiPfAllocateMdls(0, (uint32_t)(v_stack_m1D0), v_stack_m120, v_stack_m128);
    result = Arg4 + 224;
    local_r14 = (uint32_t)((uint32_t)(result));
    local_r15 = Arg4;
    if ((*(uint64_t *)(Arg4 + 0xE0)) != (Arg4 + 224)) {
        result = v_stack_m118;
        *(uint64_t *)(result) = 0;
        local_r15 = 0;
        local_r14 = 0;
    }
    if (v_stack_m180 != 0) goto loc_0093E18E;
    if (0 != 0) {
        Arg1 = 0;
        result = MiReleaseReadListResources(Arg1, (uint32_t)(v_stack_m1D0), v_stack_m120, v_stack_m128);
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m120, v_stack_m128);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m120, v_stack_m128);
    local_rsp = (local_rsp) + (528);
    return result;
loc_0093DB38:
    result = MiGetControlAreaPtes(v_stack_m1B8, Arg2, v_stack_m120, v_stack_m128);
    if (Arg5 == 0) goto loc_0093DEC7;
    Arg2 = (Arg5) >> (12);
    v_stack_m148 = Arg2;
    if (Arg2 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_0093DF79;
    if (((uint32_t)((uint32_t)(Arg2))) > result) goto loc_0093DF79;
loc_0093DB77:
    if (0 == 0) goto loc_0093DB95;
    result = (v_stack_p20) >> (12);
    result = (uint32_t)((result) & (63));
    result = (result) + ((uint32_t)((uint32_t)(Arg2)));
    if (result > 64) goto loc_0093DF79;
loc_0093DB95:
    result = MiAllocateReadList((uint32_t)((uint32_t)(Arg2)), Arg2, v_stack_m120, v_stack_m128);
    if (result == 0) goto loc_0093E0F2;
    *(uint64_t *)(result + 0x8) = v_stack_m1B8;
    if (((*(uint32_t *)(v_rip + 0x688EFD)) & (0x200000ULL)) != 0) goto loc_0093E109;
    local_rsi = 0;
    v_stack_m170 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1B8 + 0x80 + 0x20))) >> (1));
    result = (uint32_t)((result) & (31));
    v_stack_m1B8 = 0;
    v_stack_m188 = 0;
    v_stack_m1C8 = 0;
    v_stack_m140 = 0;
    v_stack_m178 = (uint32_t)(result);
    local_r13 = v_stack_m1B8 + 128;
    if (Arg5 != 0) {
        Arg3 = v_stack_m170;
        Arg2 = v_stack_p20;
        Arg1 = v_stack_m1B8;
        result = MiOffsetToProtos(Arg1, Arg2, Arg3, v_stack_m128);
        local_r13 = result;
    }
    result = MiGetControlAreaPartition(v_stack_m1B8, Arg2, Arg3, v_stack_m128);
    v_stack_m1B0 = result;
    result = MiGetAvailablePagesExcludeSlists(result, Arg2, Arg3, v_stack_m128);
    v_stack_m138 = result;
    v_stack_m168 = 0;
    v_stack_m160 = 0;
    v_stack_m190 = 0;
    if (v_stack_m188 != 0) goto loc_0093DF09;
    v_stack_m198 = 0;
loc_0093DC39:
    v_stack_m150 = result + 240;
    *(uint32_t *)(result + 0xB8) = (uint32_t)((uint32_t)(Arg6));
    *(uint32_t *)(result + 0xBC) = 5;
    *(uint32_t *)(result + 0xC0) = 7;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1C0 + 0x38))) >> (20));
    Arg3 = (uint32_t)((Arg3) & (127));
    v_stack_m1A8 = 0;
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    v_stack_m130 = result;
    result = MiInitializePageColorBase(result, 3, Arg3, v_stack_m110);
    result = MiColorBaseToNode(v_stack_m110, 3, Arg3, v_stack_m110);
    local_r10 = 0;
    local_r14 = 0;
    v_stack_m1A0 = 0;
    result = 0;
loc_0093DCBC:
    v_stack_m1A4 = 0;
    if (0 >= v_stack_m148) goto loc_0093E097;
    if (0 >= v_stack_m168) goto loc_0093DE41;
loc_0093DCD9:
loc_0093DCDD:
    if ((((uint8_t)(*(uint64_t *)(0))) & (1)) != 0) goto loc_0093DE2A;
    if (condition_is_above_or_equal) goto loc_0093DDEC;
    result = (uint8_t)((*(uint8_t *)(v_stack_m1C0 + 0x3E)) & (12));
    if (((uint8_t)(result)) == 4) goto loc_0093DF42;
    if (v_stack_m198 != 0) goto loc_0093DE05;
loc_0093DD0F:
    result = v_stack_m150;
    if (v_stack_m1C8 != 0) { result = v_stack_m1C8; }
    v_stack_m1C8 = result;
    *(uint64_t *)(v_stack_m150) = 0;
    if (0 == local_r13) goto loc_0093DDCA;
loc_0093DD34:
    Arg3 = (0) | (2);
    v_stack_m1A0 = local_r13;
    *(uint64_t *)(v_stack_m150) = Arg3;
loc_0093DD3F:
    v_stack_m140 = 0;
    if (0 == v_stack_m160) goto loc_0093E0FD;
loc_0093DD4D:
    Arg4 = (v_stack_m150) + (8);
    v_stack_m150 = Arg4;
    result = MiObtainFaultCharges(v_stack_m1B0, 1, 1, Arg4);
    if (result == 0) goto loc_0093D9A3;
    v_stack_p20 = v_stack_m1A8;
    result = MiUseSlabAllocator(v_stack_m1B0, local_r13, *(uint64_t *)(0), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if ((uint32_t)(result) != 0) goto loc_0093DF31;
loc_0093DD92:
    result = (v_stack_m138) + (160);
    if (v_stack_m188 > result) goto loc_0093E0C3;
    Arg1 = (v_stack_m188) + 1;
    v_stack_m188 = Arg1;
loc_0093DDB4:
loc_0093DDB8:
    result = (uint32_t)(((uint32_t)(v_stack_m1A4)) + 1);
    local_r12 = (0) + (8);
    goto loc_0093DCBC;
loc_0093DDCA:
    result = MiGetPteAddress(v_stack_m140, local_r13, *(uint64_t *)(0), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    result = MiGetPteAddress(local_r12, result, *(uint64_t *)(0), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (result != result) goto loc_0093DD34;
    goto loc_0093DD3F;
loc_0093DDEC:
    if (result < result) goto loc_0093DE2A;
    result = IS_PTE_NOT_DEMAND_ZERO(v_stack_m1C0, result, *(uint64_t *)(0), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if ((uint32_t)(result) != 0) goto loc_0093DD0F;
    goto loc_0093DDB4;
loc_0093DE05:
    v_stack_m190 = local_r12;
    result = (local_r12) - (*(uint64_t *)(0));
    result = (result) >> (3);
    result = (result) << (12);
    local_rdi = (0) + (result);
    *(uint64_t *)(result) = local_rdi;
    Arg2 = (result) + (8);
    v_stack_m198 = Arg2;
    goto loc_0093DD0F;
loc_0093DE2A:
    result = MiUpdatePfnForPrefetchByPte(local_r12, (uint32_t)(Arg6), v_stack_m180, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_0093DDB4;
loc_0093DE41:
    if (local_r12 != 0) goto loc_0093DEF2;
loc_0093DE4A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1C0 + 0x38)))) & (32)) != 0) goto loc_0093DFA1;
    result = MiAddViewsForSection(local_r13, (uint32_t)(*(uint32_t *)(local_r13 + 0x2C)), 4, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (sign_flag) goto loc_0093E145;
    v_stack_p70 = *(uint64_t *)(local_r13 + 0x8);
    if ((*(uint64_t *)(result + 0x18)) == (result + 24)) goto loc_0093DE92;
    if ((*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x10)) != 5) goto loc_0093DFFB;
loc_0093DE92:
    result = MiAllocatePool(256, 64, (uint32_t)(0x6C536D4DULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (result == 0) goto loc_0093DF84;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x18 + 0x8))) == (result + 24)) goto loc_0093DFED;
loc_0093DEC7:
    if (3 >= (*(uint64_t *)(result + 0x18 + 0x8))) goto loc_0093DF79;
    v_stack_m148 = 3;
    goto loc_0093DB77;
loc_0093DEE5:
    *(uint64_t *)(*(uint64_t *)(result + 0x18 + 0x8) + 0x18) = v_stack_m198;
    goto loc_0093D9CB;
loc_0093DEF2:
    if (*(uint64_t *)(local_r13 + 0x10) == 0) goto loc_0093E097;
    goto loc_0093DE4A;
loc_0093DF09:
    v_stack_m198 = *(uint64_t *)(local_rdi + 0x20);
    v_stack_p70 = (uint32_t)((uint32_t)(result));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0xC))) & (511));
    v_stack_p70 = (uint32_t)(Arg1);
    goto loc_0093DC39;
loc_0093DF31:
    if (((uint32_t)((uint32_t)(v_stack_m1A8))) > 4) goto loc_0093DD92;
loc_0093DF42:
    result = MiRefillPurgedExtents(*(uint64_t *)(local_r13 + 0x10), *(uint64_t *)(local_r13 + 0x8), (uint32_t)(v_stack_p78), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (!sign_flag) goto loc_0093DDB4;
    if (v_stack_m1B8 != 0) goto loc_0093D9BE;
    goto loc_0093D9BE;
loc_0093DF79:
    goto loc_0093DB0A;
loc_0093DF84:
    result = MiRemoveViewsFromSectionWithPfn(v_stack_m1C8, (uint32_t)(*(uint32_t *)(v_stack_m1C8 + 0x2C)), 4, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_0093DAE6;
loc_0093DFA1:
    v_stack_p70 = *(uint64_t *)(v_stack_m1C8 + 0x8);
    if (condition_is_above_or_equal) goto loc_0093E011;
    if (((*(uint32_t *)((uint32_t)(v_stack_m1A8) + 0x38)) & (0x8000000ULL)) == 0) goto loc_0093E011;
    if ((*(uint64_t *)(v_stack_m1C8 + 0x18)) == 0) goto loc_0093E0BA;
    result = MiGetSharedProtos((uint32_t)(v_stack_m1A8), (uint32_t)(v_stack_p78), v_stack_m1C8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    local_r12 = (v_stack_m168) + (-8);
    goto loc_0093DDB8;
loc_0093DFED:
    *(uint64_t *)((uint32_t)(v_stack_m1A8)) = (uint32_t)(v_stack_m1A8);
    *(uint64_t *)((uint32_t)(v_stack_m1A8) + 0x8) = result;
    *(uint64_t *)(result) = (uint32_t)(v_stack_m1A8);
    *(uint64_t *)((uint32_t)(v_stack_m1A8) + 0x8) = (uint32_t)(v_stack_m1A8);
loc_0093DFFB:
    if ((*(uint64_t *)(result + 0x10)) == 0) {
        *(uint64_t *)(result + 0x10) = v_stack_m1C8;
    }
    *(uint64_t *)((uint32_t)(v_stack_m1A8) + (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m1A8) + 0x10)) * 8 + 0x18) = v_stack_m1C8;
loc_0093E011:
    v_stack_m168 = v_stack_p70 + (uint32_t)(*(uint32_t *)(v_stack_m1C8 + 0x2C)) * 8;
    result = MiStartingOffset(v_stack_m1C8, v_stack_p70, (uint32_t)(v_stack_p78), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    result = MiEndingOffsetWithLock(v_stack_m1C8, v_stack_p70, (uint32_t)(v_stack_p78), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) - ((uint32_t)(result)));
    if ((((uint32_t)(Arg1)) & (0xFFFULL)) != 0) goto loc_0093E0A0;
loc_0093E058:
    if (v_stack_m198 == 0) goto loc_0093DCD9;
    v_stack_p70 = result;
    v_stack_m190 = v_stack_p70;
    result = (uint32_t)(((uint32_t)((uint32_t)(result))) ^ (*(uint32_t *)(v_stack_m158 + 0xC)));
    result = (uint32_t)((result) & (511));
    result = (uint32_t)((result) ^ ((uint32_t)(result)));
    v_stack_p70 = (uint32_t)(result);
    goto loc_0093DCDD;
loc_0093E097:
    goto loc_0093D9BA;
loc_0093E0A0:
    result = (result) - (result);
    result = (result) + (0xFFFULL);
    result = (result) >> (12);
    result = (result) - 1;
    v_stack_m160 = v_stack_m158 + result * 8;
    goto loc_0093E058;
loc_0093E0BA:
    goto loc_0093DDB8;
loc_0093E0C3:
    result = MiReturnFaultCharges(v_stack_m1B0, 1, 1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (v_stack_m1B8 != 0) goto loc_0093D9BE;
    goto loc_0093D9BE;
loc_0093E0F2:
    goto loc_0093DB0A;
loc_0093E0FD:
    Arg3 = (1) | (1);
    *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) = Arg3;
    goto loc_0093DD4D;
loc_0093E109:
    local_rdi = v_stack_m1B0;
    if (((uint32_t)((uint32_t)(result))) <= v_stack_m1B0) { local_rdi = (uint32_t)((uint32_t)(result)); }
    result = MiAllocatePool(66, local_rdi * 8 + 16, (uint32_t)(0x6C68694DULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    local_rsi = 0;
    v_stack_m180 = result;
    goto loc_0093DAF8;
loc_0093E145:
    if (v_stack_m188 == 0) goto loc_0093DAE6;
    result = MiReturnFaultCharges(v_stack_m1B0, v_stack_m188, 1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_0093DAE6;
loc_0093E166:
    Arg2 = (local_rdi) - (result);
    result = MiReturnFaultCharges(0, Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    local_rbx = (result) - (local_rdi);
    local_r12 = (v_stack_m1B8) + (local_rbx);
    if (condition_is_not_equal) goto loc_0093DA97;
    goto loc_0093DAE6;
loc_0093E18E:
    result = MiIssuePageHeatList(local_rbx, Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x38` | `32` | `R` |
| `Arg2` | `+ 0x40` | `64` | `R` |
| `Arg9` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0093D8E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
