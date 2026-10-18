# MiStoreWriteModifiedPages

- RVA: `0x002B46C4`–`0x002B54B3` (길이 `3,567` bytes)
- VA: `0x00000001402B46C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006D824`
- 디코드: `865`개 명령, `3,567/3,567` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **59**; 고유 호출 대상: **42**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x002B47EA` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x002B4994` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x002B499F` → [MiIsPfnOriginalPteLost](../37/MiIsPfnOriginalPteLost_function_00373B5C.md) (function, `0x00373B5C`)
- `0x002B49EE` → [MiStoreCheckCandidatePage](MiStoreCheckCandidatePage_function_002B54E8.md) (function, `0x002B54E8`)
- `0x002B4A38` → [ObpTraceObjectReferenceIfActive](../21/ObpTraceObjectReferenceIfActive_function_00210780.md) (function, `0x00210780`)
- `0x002B4A6E` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002B4A7D` → [MiStoreGetWriteSupport](../45/MiStoreGetWriteSupport_function_00456DF0.md) (function, `0x00456DF0`)
- `0x002B4B2C` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x002B4B6F` → [MiUpdatePagefilePeakUsage](MiUpdatePagefilePeakUsage_function_002B54BC.md) (function, `0x002B54BC`)
- `0x002B4B7A` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x002B4BC0` → [MiStoreLogNotCandidate](../46/MiStoreLogNotCandidate_function_00463678.md) (function, `0x00463678`)
- `0x002B4C08` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002B4C57` → [MiRefPageFileSpaceBitmaps](../40/MiRefPageFileSpaceBitmaps_function_00407DC4.md) (function, `0x00407DC4`)
- `0x002B4C9E` → [SmPageWrite](../34/SmPageWrite_function_0034B864.md) (function, `0x0034B864`)
- `0x002B4D63` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x002B4D79` → [MiTransferSoftwarePte](../38/MiTransferSoftwarePte_function_003821F0.md) (function, `0x003821F0`)
- `0x002B4D85` → [MiIsPfnOriginalPteLost](../37/MiIsPfnOriginalPteLost_function_00373B5C.md) (function, `0x00373B5C`)
- `0x002B4D96` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x002B4DA8` → [MiUpdatePfnBackingStore](../44/MiUpdatePfnBackingStore_function_004442B4.md) (function, `0x004442B4`)
- `0x002B4DF8` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002B4E62` → [MiTransferSoftwarePte](../38/MiTransferSoftwarePte_function_003821F0.md) (function, `0x003821F0`)
- `0x002B4F4F` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x002B4F59` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x002B4F7C` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002B5039` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x002B5049` → [MiSetPfnModified](../36/MiSetPfnModified_function_00362960.md) (function, `0x00362960`)
- `0x002B5054` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x002B508F` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x002B50CA` → [RtlClearBits](../3E/RtlClearBits_function_003E1A90.md) (function, `0x003E1A90`)
- `0x002B50E9` → [MiStoreDecrementOutstandingWrites](../48/MiStoreDecrementOutstandingWrites_function_0048EF68.md) (function, `0x0048EF68`)
- `0x002B510C` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x002B5114` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x002B5131` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x002B5143` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x002B5151` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002B51C1` → [MiTransferSoftwarePte](../38/MiTransferSoftwarePte_function_003821F0.md) (function, `0x003821F0`)
- `0x002B51D2` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x002B51DE` → [MiStoreFreeWriteSupport](../20/MiStoreFreeWriteSupport_function_00203A48.md) (function, `0x00203A48`)
- `0x002B5200` → [MiStoreLogWriteIssueFailure](../48/MiStoreLogWriteIssueFailure_function_0048EE4C.md) (function, `0x0048EE4C`)
- `0x002B5246` → [MiStoreModifiedWriteDereference](../20/MiStoreModifiedWriteDereference_function_00203E94.md) (function, `0x00203E94`)
- `0x002B5266` → [MiUpdatePageFileHighInPte](../36/MiUpdatePageFileHighInPte_function_0036D840.md) (function, `0x0036D840`)
- `0x002B527A` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x002B52A8` → [MmMapLockedPagesSpecifyCache](../31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x002B52C3` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B52D2` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B52E1` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002B5346` → [MiStoreLogWriteDisabled](../4B/MiStoreLogWriteDisabled_function_004B2D9C.md) (function, `0x004B2D9C`)
- `0x002B5375` → [MmUnmapLockedPages](../24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)
- `0x002B537F` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x002B538F` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002B53A4` → [MiStoreUpdatePagefileHash](../49/MiStoreUpdatePagefileHash_function_004920AC.md) (function, `0x004920AC`)
- `0x002B53BF` → [MiStoreExtendVirtualPagefile](../4F/MiStoreExtendVirtualPagefile_function_004F73AC.md) (function, `0x004F73AC`)
- `0x002B53CB` → [MiStoreLogFullPagefile](../4F/MiStoreLogFullPagefile_function_004FC7C8.md) (function, `0x004FC7C8`)
- `0x002B53F0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002B53FC` → [MiMakePageFilePte](../38/MiMakePageFilePte_function_003823C8.md) (function, `0x003823C8`)
- `0x002B541E` → [MiSetStoreVirtualPagefileValue](../37/MiSetStoreVirtualPagefileValue_function_00373B80.md) (function, `0x00373B80`)
- `0x002B5444` → [MiTransferSoftwarePte](../38/MiTransferSoftwarePte_function_003821F0.md) (function, `0x003821F0`)
- `0x002B5461` → [MiIsStoreVirtualPagefileFull](../4A/MiIsStoreVirtualPagefileFull_function_004ACB9C.md) (function, `0x004ACB9C`)
- `0x002B547A` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [MiGatherPagefilePages](../37/MiGatherPagefilePages_function_00372B08.md) at `0x00372F37`

### Static image references
- `0x002B4762` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x002B488B` → RVA `0x00E37478` (`.data`; read)
- `0x002B4A5E` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002B4E39` → RVA `0x00010880` (`.rdata`; read)
- `0x002B4F26` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002B5065` → RVA `0x00FC520C` (`ALMOSTRO`; read)
- `0x002B52B5` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x002B5151` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002B53F0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x002B5071` → [sub_006DB99C](../6D/Unknown_function_006DB99C.md) (`tail-transfer`)
  - `0x002B5459` → [sub_006DB99C + 0x66](../6D/Unknown_function_006DB99C.md) (`tail-transfer`)
  - `0x002B549E` → [sub_006DB99C + 0x66](../6D/Unknown_function_006DB99C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002B46C4  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
002B46C9  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
002B46CE  55                              push rbp
002B46CF  56                              push rsi
002B46D0  57                              push rdi
002B46D1  41 54                           push r12
002B46D3  41 55                           push r13
002B46D5  41 56                           push r14
002B46D7  41 57                           push r15
002B46D9  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
002B46DE  48 81 EC 00 01 00 00            sub rsp, 0x100
002B46E5  48 8B 41 40                     mov rax, qword ptr [rcx + 0x40]
002B46E9  48 8D 71 68                     lea rsi, [rcx + 0x68]
002B46ED  45 33 F6                        xor r14d, r14d
002B46F0  48 89 75 F7                     mov qword ptr [rbp - 9], rsi
002B46F4  8B DA                           mov ebx, edx
002B46F6  44 89 75 87                     mov dword ptr [rbp - 0x79], r14d
002B46FA  8B 56 28                        mov edx, dword ptr [rsi + 0x28]
002B46FD  0F 57 C0                        xorps xmm0, xmm0
002B4700  4C 8B B8 D8 00 00 00            mov r15, qword ptr [rax + 0xd8]
002B4707  0F 57 C9                        xorps xmm1, xmm1
002B470A  C1 EA 0C                        shr edx, 0xc
002B470D  4C 8B E1                        mov r12, rcx
002B4710  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
002B4714  4C 89 75 AF                     mov qword ptr [rbp - 0x51], r14
002B4718  41 8B 87 C4 04 00 00            mov eax, dword ptr [r15 + 0x4c4]
002B471F  4C 89 7D EF                     mov qword ptr [rbp - 0x11], r15
002B4723  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
002B4727  F3 0F 7F 4D 07                  movdqu xmmword ptr [rbp + 7], xmm1
002B472C  F3 0F 7F 45 17                  movdqu xmmword ptr [rbp + 0x17], xmm0
002B4731  85 C0                           test eax, eax
002B4733  0F 85 06 0C 00 00               jne 0x1402b533f
002B4739  41 8B 87 B4 04 00 00            mov eax, dword ptr [r15 + 0x4b4]
002B4740  49 8B BC C7 60 48 00 00         mov rdi, qword ptr [r15 + rax*8 + 0x4860]
002B4748  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
002B474D  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
002B4750  3B C2                           cmp eax, edx
002B4752  0F 82 61 0C 00 00               jb 0x1402b53b9
002B4758  41 BD 01 00 00 00               mov r13d, 1
002B475E  85 DB                           test ebx, ebx
002B4760  74 0E                           je 0x1402b4770
002B4762  66 44 39 2D 96 08 D1 00         cmp word ptr [rip + 0xd10896], r13w
002B476A  0F 87 F5 08 00 00               ja 0x1402b5065
002B4770  49 8B 5C 24 48                  mov rbx, qword ptr [r12 + 0x48]
002B4775  48 89 5D 97                     mov qword ptr [rbp - 0x69], rbx
002B4779  48 85 DB                        test rbx, rbx
002B477C  0F 84 F4 08 00 00               je 0x1402b5076
002B4782  65 4C 8B 2C 25 88 01 00 00      mov r13, qword ptr gs:[0x188]
002B478B  48 8D 45 FF                     lea rax, [rbp - 1]
002B478F  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
002B4793  48 83 C8 FF                     or rax, 0xffffffffffffffff
002B4797  4C 89 75 FF                     mov qword ptr [rbp - 1], r14
002B479B  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
002B47A0  66 41 01 85 E4 01 00 00         add word ptr [r13 + 0x1e4], ax
002B47A8  90                              nop
002B47A9  8D 48 02                        lea ecx, [rax + 2]
002B47AC  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
002B47B1  66 41 29 8D E6 01 00 00         sub word ptr [r13 + 0x1e6], cx
002B47B9  90                              nop
002B47BA  4C 89 6D BF                     mov qword ptr [rbp - 0x41], r13
002B47BE  4D 39 B7 18 05 00 00            cmp qword ptr [r15 + 0x518], r14
002B47C5  0F 85 20 0B 00 00               jne 0x1402b52eb
002B47CB  41 01 8F CC 04 00 00            add dword ptr [r15 + 0x4cc], ecx
002B47D2  90                              nop
002B47D3  66 41 01 8D E6 01 00 00         add word ptr [r13 + 0x1e6], cx
002B47DB  75 17                           jne 0x1402b47f4
002B47DD  49 8D 85 98 00 00 00            lea rax, [r13 + 0x98]
002B47E4  90                              nop
002B47E5  48 39 00                        cmp qword ptr [rax], rax
002B47E8  74 0A                           je 0x1402b47f4
002B47EA  E8 91 E4 02 00                  call 0x1402e2c80
002B47EF  B9 01 00 00 00                  mov ecx, 1
002B47F4  F6 46 0A 05                     test byte ptr [rsi + 0xa], 5
002B47F8  0F 84 92 0A 00 00               je 0x1402b5290
002B47FE  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
002B4802  45 33 DB                        xor r11d, r11d
002B4805  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
002B480A  48 85 C9                        test rcx, rcx
002B480D  0F 84 9B 0B 00 00               je 0x1402b53ae
002B4813  44 8B 6C 24 40                  mov r13d, dword ptr [rsp + 0x40]
002B4818  41 8B CB                        mov ecx, r11d
002B481B  44 89 5C 24 3C                  mov dword ptr [rsp + 0x3c], r11d
002B4820  40 B6 11                        mov sil, 0x11
002B4823  45 8B CB                        mov r9d, r11d
002B4826  44 89 5D 7F                     mov dword ptr [rbp + 0x7f], r11d
002B482A  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
002B482E  41 8D 45 01                     lea eax, [r13 + 1]
002B4832  89 43 58                        mov dword ptr [rbx + 0x58], eax
002B4835  41 8D 5B 01                     lea ebx, [r11 + 1]
002B4839  8B 57 58                        mov edx, dword ptr [rdi + 0x58]
002B483C  49 8B 87 90 05 00 00            mov rax, qword ptr [r15 + 0x590]
002B4843  4D 8B 54 24 58                  mov r10, qword ptr [r12 + 0x58]
002B4848  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
002B484C  49 8D 84 24 98 00 00 00         lea rax, [r12 + 0x98]
002B4854  49 C1 EA 0C                     shr r10, 0xc
002B4858  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
002B485C  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
002B4860  41 8B FB                        mov edi, r11d
002B4863  4C 89 55 B7                     mov qword ptr [rbp - 0x49], r10
002B4867  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
002B486B  41 B8 02 00 00 00               mov r8d, 2
002B4871  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
002B4875  49 BA FF FF FF FF FF FF FF 7F   movabs r10, 0x7fffffffffffffff
002B487F  41 3B FD                        cmp edi, r13d
002B4882  0F 83 E8 03 00 00               jae 0x1402b4c70
002B4888  4C 8B 20                        mov r12, qword ptr [rax]
002B488B  4C 3B 25 E6 2B B8 00            cmp r12, qword ptr [rip + 0xb82be6]
002B4892  0F 84 76 0A 00 00               je 0x1402b530e
002B4898  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
002B489D  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
002B48A0  85 C0                           test eax, eax
002B48A2  0F 84 75 03 00 00               je 0x1402b4c1d
002B48A8  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
002B48AC  48 3B 4B 50                     cmp rcx, qword ptr [rbx + 0x50]
002B48B0  0F 85 91 03 00 00               jne 0x1402b4c47
002B48B6  8B 7D 07                        mov edi, dword ptr [rbp + 7]
002B48B9  3B D7                           cmp edx, edi
002B48BB  4C 8B 4D 0F                     mov r9, qword ptr [rbp + 0xf]
002B48BF  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
002B48C4  45 1B C0                        sbb r8d, r8d
002B48C7  49 8B C9                        mov rcx, r9
002B48CA  44 23 C2                        and r8d, edx
002B48CD  83 E1 04                        and ecx, 4
002B48D0  8D 57 FF                        lea edx, [rdi - 1]
002B48D3  8B C1                           mov eax, ecx
002B48D5  48 F7 D8                        neg rax
002B48D8  45 1B D2                        sbb r10d, r10d
002B48DB  41 83 E2 20                     and r10d, 0x20
002B48DF  48 F7 D9                        neg rcx
002B48E2  48 1B C0                        sbb rax, rax
002B48E5  83 E0 04                        and eax, 4
002B48E8  4C 2B C8                        sub r9, rax
002B48EB  BB 01 00 00 00                  mov ebx, 1
002B48F0  44 89 5D A7                     mov dword ptr [rbp - 0x59], r11d
002B48F4  45 8D 1C 12                     lea r11d, [r10 + rdx]
002B48F8  41 8B C3                        mov eax, r11d
002B48FB  43 8D 0C 02                     lea ecx, [r10 + r8]
002B48FF  2B C1                           sub eax, ecx
002B4901  03 C3                           add eax, ebx
002B4903  3B C3                           cmp eax, ebx
002B4905  0F 82 1A 03 00 00               jb 0x1402b4c25
002B490B  8B D1                           mov edx, ecx
002B490D  80 E1 3F                        and cl, 0x3f
002B4910  48 C1 EA 06                     shr rdx, 6
002B4914  41 8B C3                        mov eax, r11d
002B4917  48 C1 E8 06                     shr rax, 6
002B491B  49 8D 34 C1                     lea rsi, [r9 + rax*8]
002B491F  8B C3                           mov eax, ebx
002B4921  48 D3 E0                        shl rax, cl
002B4924  48 2B C3                        sub rax, rbx
002B4927  49 8D 1C D1                     lea rbx, [r9 + rdx*8]
002B492B  48 8B 0B                        mov rcx, qword ptr [rbx]
002B492E  48 0B C8                        or rcx, rax
002B4931  48 83 F9 FF                     cmp rcx, -1
002B4935  75 12                           jne 0x1402b4949
002B4937  48 83 C3 08                     add rbx, 8
002B493B  48 3B DE                        cmp rbx, rsi
002B493E  0F 87 E1 02 00 00               ja 0x1402b4c25
002B4944  48 8B 0B                        mov rcx, qword ptr [rbx]
002B4947  EB E8                           jmp 0x1402b4931
002B4949  49 2B D9                        sub rbx, r9
002B494C  48 F7 D1                        not rcx
002B494F  48 0F BC C1                     bsf rax, rcx
002B4953  48 C1 FB 03                     sar rbx, 3
002B4957  C1 E3 06                        shl ebx, 6
002B495A  03 D8                           add ebx, eax
002B495C  89 45 A7                        mov dword ptr [rbp - 0x59], eax
002B495F  41 3B DB                        cmp ebx, r11d
002B4962  0F 87 BD 02 00 00               ja 0x1402b4c25
002B4968  83 FB FF                        cmp ebx, -1
002B496B  0F 84 B7 02 00 00               je 0x1402b4c28
002B4971  41 2B DA                        sub ebx, r10d
002B4974  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
002B4978  4F 8D 24 64                     lea r12, [r12 + r12*2]
002B497C  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B4986  49 C1 E4 04                     shl r12, 4
002B498A  48 8B C0                        mov rax, rax
002B498D  4D 8D 34 04                     lea r14, [r12 + rax]
002B4991  49 8B CE                        mov rcx, r14
002B4994  E8 A7 59 06 00                  call 0x14031a340
002B4999  49 8B CE                        mov rcx, r14
002B499C  0F B6 F0                        movzx esi, al
002B499F  E8 B8 F1 0B 00                  call 0x140373b5c
002B49A4  45 33 DB                        xor r11d, r11d
002B49A7  85 C0                           test eax, eax
002B49A9  0F 85 4B 0A 00 00               jne 0x1402b53fa
002B49AF  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
002B49B3  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
002B49B7  48 89 44 F9 60                  mov qword ptr [rcx + rdi*8 + 0x60], rax
002B49BC  83 FB FF                        cmp ebx, -1
002B49BF  0F 84 03 02 00 00               je 0x1402b4bc8
002B49C5  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B49C9  48 0F BA E0 3E                  bt rax, 0x3e
002B49CE  0F 82 F4 01 00 00               jb 0x1402b4bc8
002B49D4  48 8D 45 AF                     lea rax, [rbp - 0x51]
002B49D8  4C 89 5D AF                     mov qword ptr [rbp - 0x51], r11
002B49DC  4C 8D 4D D7                     lea r9, [rbp - 0x29]
002B49E0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002B49E5  4C 8D 45 87                     lea r8, [rbp - 0x79]
002B49E9  8B D3                           mov edx, ebx
002B49EB  49 8B CE                        mov rcx, r14
002B49EE  E8 F5 0A 00 00                  call 0x1402b54e8
002B49F3  45 33 DB                        xor r11d, r11d
002B49F6  85 C0                           test eax, eax
002B49F8  0F 88 BE 01 00 00               js 0x1402b4bbc
002B49FE  41 8D 43 03                     lea eax, [r11 + 3]
002B4A02  84 45 DF                        test byte ptr [rbp - 0x21], al
002B4A05  75 42                           jne 0x1402b4a49
002B4A07  4C 8B 4D D7                     mov r9, qword ptr [rbp - 0x29]
002B4A0B  41 0F 0D 49 D0                  prefetchw byte ptr [r9 - 0x30]
002B4A10  49 8B 41 D0                     mov rax, qword ptr [r9 - 0x30]
002B4A14  48 85 C0                        test rax, rax
002B4A17  0F 84 AB 01 00 00               je 0x1402b4bc8
002B4A1D  48 8D 48 01                     lea rcx, [rax + 1]
002B4A21  F0 49 0F B1 49 D0               lock cmpxchg qword ptr [r9 - 0x30], rcx
002B4A27  75 EB                           jne 0x1402b4a14
002B4A29  BA 01 00 00 00                  mov edx, 1
002B4A2E  49 8D 49 D0                     lea rcx, [r9 - 0x30]
002B4A32  41 B8 4D 6D 50 66               mov r8d, 0x66506d4d
002B4A38  E8 43 BD F5 FF                  call 0x140210780
002B4A3D  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
002B4A41  45 33 DB                        xor r11d, r11d
002B4A44  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002B4A49  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002B4A53  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
002B4A58  40 80 FE 02                     cmp sil, 2
002B4A5C  73 19                           jae 0x1402b4a77
002B4A5E  44 39 1D BB 22 D1 00            cmp dword ptr [rip + 0xd122bb], r11d
002B4A65  74 0C                           je 0x1402b4a73
002B4A67  44 0F 20 C1                     mov rcx, cr8
002B4A6B  40 8A D6                        mov dl, sil
002B4A6E  E8 25 0C 24 00                  call 0x1404f5698
002B4A73  44 0F 22 C6                     mov cr8, rsi
002B4A77  49 8B CF                        mov rcx, r15
002B4A7A  40 B6 11                        mov sil, 0x11
002B4A7D  E8 6E 23 1A 00                  call 0x140456df0
002B4A82  45 33 DB                        xor r11d, r11d
002B4A85  48 8B D0                        mov rdx, rax
002B4A88  48 85 C0                        test rax, rax
002B4A8B  0F 84 BA 09 00 00               je 0x1402b544b
002B4A91  4C 8B 45 8F                     mov r8, qword ptr [rbp - 0x71]
002B4A95  48 8D 4A 20                     lea rcx, [rdx + 0x20]
002B4A99  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002B4A9E  0F 10 45 D7                     movups xmm0, xmmword ptr [rbp - 0x29]
002B4AA2  48 89 42 18                     mov qword ptr [rdx + 0x18], rax
002B4AA6  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
002B4AAB  4C 89 19                        mov qword ptr [rcx], r11
002B4AAE  C7 41 08 38 00 00 00            mov dword ptr [rcx + 8], 0x38
002B4AB5  4C 89 59 20                     mov qword ptr [rcx + 0x20], r11
002B4AB9  48 C7 41 28 00 10 00 00         mov qword ptr [rcx + 0x28], 0x1000
002B4AC1  48 89 42 38                     mov qword ptr [rdx + 0x38], rax
002B4AC5  41 8D 43 03                     lea eax, [r11 + 3]
002B4AC9  66 09 42 2A                     or word ptr [rdx + 0x2a], ax
002B4ACD  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002B4AD7  49 C1 FC 04                     sar r12, 4
002B4ADB  4C 0F AF E0                     imul r12, rax
002B4ADF  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
002B4AE3  48 89 02                        mov qword ptr [rdx], rax
002B4AE6  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
002B4AEA  4C 89 62 50                     mov qword ptr [rdx + 0x50], r12
002B4AEE  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
002B4AF3  41 89 40 18                     mov dword ptr [r8 + 0x18], eax
002B4AF7  8B 45 87                        mov eax, dword ptr [rbp - 0x79]
002B4AFA  41 89 40 04                     mov dword ptr [r8 + 4], eax
002B4AFE  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
002B4B02  49 8D BC 24 C8 00 00 00         lea rdi, [r12 + 0xc8]
002B4B0A  49 89 40 20                     mov qword ptr [r8 + 0x20], rax
002B4B0E  48 8D 42 08                     lea rax, [rdx + 8]
002B4B12  49 89 48 28                     mov qword ptr [r8 + 0x28], rcx
002B4B16  48 8B CF                        mov rcx, rdi
002B4B19  49 89 40 38                     mov qword ptr [r8 + 0x38], rax
002B4B1D  4C 89 5C 24 50                  mov qword ptr [rsp + 0x50], r11
002B4B22  F3 41 0F 7F 40 08               movdqu xmmword ptr [r8 + 8], xmm0
002B4B28  49 89 50 30                     mov qword ptr [r8 + 0x30], rdx
002B4B2C  E8 5F 3B F9 FF                  call 0x140248690
002B4B31  49 8B 4C 24 50                  mov rcx, qword ptr [r12 + 0x50]
002B4B36  8B D3                           mov edx, ebx
002B4B38  44 8B CB                        mov r9d, ebx
002B4B3B  83 E2 07                        and edx, 7
002B4B3E  44 8A D0                        mov r10b, al
002B4B41  49 C1 E9 03                     shr r9, 3
002B4B45  8D 43 01                        lea eax, [rbx + 1]
002B4B48  4C 03 49 10                     add r9, qword ptr [rcx + 0x10]
002B4B4C  49 8B CC                        mov rcx, r12
002B4B4F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002B4B53  45 0F BE 01                     movsx r8d, byte ptr [r9]
002B4B57  41 0F AB D0                     bts r8d, edx
002B4B5B  45 88 01                        mov byte ptr [r9], r8b
002B4B5E  41 89 44 24 58                  mov dword ptr [r12 + 0x58], eax
002B4B63  41 8B 5C 24 0C                  mov ebx, dword ptr [r12 + 0xc]
002B4B68  FF CB                           dec ebx
002B4B6A  41 89 5C 24 0C                  mov dword ptr [r12 + 0xc], ebx
002B4B6F  E8 48 09 00 00                  call 0x1402b54bc
002B4B74  41 8A D2                        mov dl, r10b
002B4B77  48 8B CF                        mov rcx, rdi
002B4B7A  E8 41 37 F9 FF                  call 0x1402482c0
002B4B7F  85 DB                           test ebx, ebx
002B4B81  0F 84 D7 08 00 00               je 0x1402b545e
002B4B87  48 83 45 8F 40                  add qword ptr [rbp - 0x71], 0x40
002B4B8C  BB 01 00 00 00                  mov ebx, 1
002B4B91  44 8B 4D 7F                     mov r9d, dword ptr [rbp + 0x7f]
002B4B95  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
002B4B99  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
002B4B9D  03 FB                           add edi, ebx
002B4B9F  48 81 44 24 58 00 10 00 00      add qword ptr [rsp + 0x58], 0x1000
002B4BA8  48 83 C0 08                     add rax, 8
002B4BAC  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
002B4BB0  45 33 DB                        xor r11d, r11d
002B4BB3  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
002B4BB7  E9 AB FC FF FF                  jmp 0x1402b4867
002B4BBC  8B D3                           mov edx, ebx
002B4BBE  8B C8                           mov ecx, eax
002B4BC0  E8 B3 EA 1A 00                  call 0x140463678
002B4BC5  45 33 DB                        xor r11d, r11d
002B4BC8  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
002B4BCC  41 B8 02 00 00 00               mov r8d, 2
002B4BD2  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
002B4BD6  49 BA FF FF FF FF FF FF FF 7F   movabs r10, 0x7fffffffffffffff
002B4BE0  41 8D 58 FF                     lea ebx, [r8 - 1]
002B4BE4  40 80 FE 11                     cmp sil, 0x11
002B4BE8  0F 84 96 08 00 00               je 0x1402b5484
002B4BEE  F0 4D 21 56 18                  lock and qword ptr [r14 + 0x18], r10
002B4BF3  41 3A F0                        cmp sil, r8b
002B4BF6  73 1D                           jae 0x1402b4c15
002B4BF8  44 39 1D 21 21 D1 00            cmp dword ptr [rip + 0xd12121], r11d
002B4BFF  74 0C                           je 0x1402b4c0d
002B4C01  44 0F 20 C1                     mov rcx, cr8
002B4C05  40 8A D6                        mov dl, sil
002B4C08  E8 8B 0A 24 00                  call 0x1404f5698
002B4C0D  40 0F B6 C6                     movzx eax, sil
002B4C11  44 0F 22 C0                     mov cr8, rax
002B4C15  40 B6 11                        mov sil, 0x11
002B4C18  E9 37 08 00 00                  jmp 0x1402b5454
002B4C1D  83 CB FF                        or ebx, 0xffffffff
002B4C20  E9 53 FD FF FF                  jmp 0x1402b4978
002B4C25  83 CB FF                        or ebx, 0xffffffff
002B4C28  45 33 DB                        xor r11d, r11d
002B4C2B  45 85 C0                        test r8d, r8d
002B4C2E  0F 84 40 FD FF FF               je 0x1402b4974
002B4C34  41 8D 56 01                     lea edx, [r14 + 1]
002B4C38  45 8B C3                        mov r8d, r11d
002B4C3B  3B D7                           cmp edx, edi
002B4C3D  0F 47 D7                        cmova edx, edi
002B4C40  FF CA                           dec edx
002B4C42  E9 A4 FC FF FF                  jmp 0x1402b48eb
002B4C47  48 85 C9                        test rcx, rcx
002B4C4A  0F 85 8A 07 00 00               jne 0x1402b53da
002B4C50  48 8D 55 FF                     lea rdx, [rbp - 1]
002B4C54  48 8B CB                        mov rcx, rbx
002B4C57  E8 68 31 15 00                  call 0x140407dc4
002B4C5C  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
002B4C60  48 8D 45 FF                     lea rax, [rbp - 1]
002B4C64  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
002B4C68  45 33 DB                        xor r11d, r11d
002B4C6B  E9 46 FC FF FF                  jmp 0x1402b48b6
002B4C70  48 8B 5D 8F                     mov rbx, qword ptr [rbp - 0x71]
002B4C74  49 8B 97 90 05 00 00            mov rdx, qword ptr [r15 + 0x590]
002B4C7B  4C 8B C3                        mov r8, rbx
002B4C7E  4C 8B 6D BF                     mov r13, qword ptr [rbp - 0x41]
002B4C82  4C 2B C2                        sub r8, rdx
002B4C85  49 C1 F8 06                     sar r8, 6
002B4C89  44 89 5C 24 34                  mov dword ptr [rsp + 0x34], r11d
002B4C8E  45 85 C0                        test r8d, r8d
002B4C91  0F 84 75 01 00 00               je 0x1402b4e0c
002B4C97  49 8B 8F B8 00 00 00            mov rcx, qword ptr [r15 + 0xb8]
002B4C9E  E8 C1 6B 09 00                  call 0x14034b864
002B4CA3  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
002B4CA8  45 0F 20 C4                     mov r12, cr8
002B4CAC  BF 02 00 00 00                  mov edi, 2
002B4CB1  44 0F 22 C7                     mov cr8, rdi
002B4CB5  83 3D 64 20 D1 00 00            cmp dword ptr [rip + 0xd12064], 0
002B4CBC  0F 85 C7 06 00 00               jne 0x1402b5389
002B4CC2  4D 8B B7 90 05 00 00            mov r14, qword ptr [r15 + 0x590]
002B4CC9  4C 3B F3                        cmp r14, rbx
002B4CCC  0F 83 13 01 00 00               jae 0x1402b4de5
002B4CD2  44 8B 6C 24 30                  mov r13d, dword ptr [rsp + 0x30]
002B4CD7  BA 01 00 00 00                  mov edx, 1
002B4CDC  44 03 EA                        add r13d, edx
002B4CDF  41 F6 C5 0F                     test r13b, 0xf
002B4CE3  0F 84 70 02 00 00               je 0x1402b4f59
002B4CE9  41 8B 4E 18                     mov ecx, dword ptr [r14 + 0x18]
002B4CED  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
002B4CF1  8B F1                           mov esi, ecx
002B4CF3  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
002B4CF7  48 8D 3C 40                     lea rdi, [rax + rax*2]
002B4CFB  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B4D05  48 C1 E7 04                     shl rdi, 4
002B4D09  48 8B C0                        mov rax, rax
002B4D0C  41 8B 1E                        mov ebx, dword ptr [r14]
002B4D0F  48 03 F8                        add rdi, rax
002B4D12  45 8B 56 04                     mov r10d, dword ptr [r14 + 4]
002B4D16  44 89 54 24 30                  mov dword ptr [rsp + 0x30], r10d
002B4D1B  85 DB                           test ebx, ebx
002B4D1D  0F 88 5E 04 00 00               js 0x1402b5181
002B4D23  33 DB                           xor ebx, ebx
002B4D25  44 8D 7B 01                     lea r15d, [rbx + 1]
002B4D29  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
002B4D30  0F 82 ED 01 00 00               jb 0x1402b4f23
002B4D36  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
002B4D3A  48 8D 34 F0                     lea rsi, [rax + rsi*8]
002B4D3E  48 8B 5E 60                     mov rbx, qword ptr [rsi + 0x60]
002B4D42  8A C3                           mov al, bl
002B4D44  C0 E8 02                        shr al, 2
002B4D47  41 84 C7                        test r15b, al
002B4D4A  0F 85 53 02 00 00               jne 0x1402b4fa3
002B4D50  8A C3                           mov al, bl
002B4D52  D0 E8                           shr al, 1
002B4D54  41 22 C7                        and al, r15b
002B4D57  F6 D8                           neg al
002B4D59  48 1B C0                        sbb rax, rax
002B4D5C  48 23 D8                        and rbx, rax
002B4D5F  48 8D 4E 60                     lea rcx, [rsi + 0x60]
002B4D63  E8 24 69 07 00                  call 0x14032b68c
002B4D68  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
002B4D6D  45 8B CF                        mov r9d, r15d
002B4D70  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002B4D75  48 8B 4E 60                     mov rcx, qword ptr [rsi + 0x60]
002B4D79  E8 72 D4 0C 00                  call 0x1403821f0
002B4D7E  48 8B CF                        mov rcx, rdi
002B4D81  48 89 46 60                     mov qword ptr [rsi + 0x60], rax
002B4D85  E8 D2 ED 0B 00                  call 0x140373b5c
002B4D8A  4C 8B 7D EF                     mov r15, qword ptr [rbp - 0x11]
002B4D8E  85 C0                           test eax, eax
002B4D90  75 1B                           jne 0x1402b4dad
002B4D92  48 8D 4F 10                     lea rcx, [rdi + 0x10]
002B4D96  E8 F1 68 07 00                  call 0x14032b68c
002B4D9B  44 8B 44 24 30                  mov r8d, dword ptr [rsp + 0x30]
002B4DA0  48 8B CF                        mov rcx, rdi
002B4DA3  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002B4DA8  E8 07 F5 18 00                  call 0x1404442b4
002B4DAD  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002B4DB7  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
002B4DBC  48 85 DB                        test rbx, rbx
002B4DBF  0F 85 7E 01 00 00               jne 0x1402b4f43
002B4DC5  BA 01 00 00 00                  mov edx, 1
002B4DCA  01 54 24 34                     add dword ptr [rsp + 0x34], edx
002B4DCE  49 83 C6 40                     add r14, 0x40
002B4DD2  BF 02 00 00 00                  mov edi, 2
002B4DD7  4C 3B 75 8F                     cmp r14, qword ptr [rbp - 0x71]
002B4DDB  0F 82 FB FE FF FF               jb 0x1402b4cdc
002B4DE1  4C 8B 6D BF                     mov r13, qword ptr [rbp - 0x41]
002B4DE5  45 33 DB                        xor r11d, r11d
002B4DE8  44 39 1D 31 1F D1 00            cmp dword ptr [rip + 0xd11f31], r11d
002B4DEF  74 0F                           je 0x1402b4e00
002B4DF1  44 0F 20 C1                     mov rcx, cr8
002B4DF5  41 8A D4                        mov dl, r12b
002B4DF8  E8 9B 08 24 00                  call 0x1404f5698
002B4DFD  45 33 DB                        xor r11d, r11d
002B4E00  41 0F B6 C4                     movzx eax, r12b
002B4E04  44 0F 22 C0                     mov cr8, rax
002B4E08  44 8B 4D 7F                     mov r9d, dword ptr [rbp + 0x7f]
002B4E0C  44 39 5C 24 3C                  cmp dword ptr [rsp + 0x3c], r11d
002B4E11  0F 85 8C 06 00 00               jne 0x1402b54a3
002B4E17  48 8B 5D 97                     mov rbx, qword ptr [rbp - 0x69]
002B4E1B  41 8B C1                        mov eax, r9d
002B4E1E  F7 D8                           neg eax
002B4E20  F0 01 43 58                     lock add dword ptr [rbx + 0x58], eax
002B4E24  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
002B4E28  44 3B C9                        cmp r9d, ecx
002B4E2B  0F 84 8D 02 00 00               je 0x1402b50be
002B4E31  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
002B4E35  41 83 CC FF                     or r12d, 0xffffffff
002B4E39  48 8B 1D 40 BA D5 FF            mov rbx, qword ptr [rip - 0x2a45c0]
002B4E40  45 8B F4                        mov r14d, r12d
002B4E43  4C 89 5C 24 58                  mov qword ptr [rsp + 0x58], r11
002B4E48  48 8B 50 40                     mov rdx, qword ptr [rax + 0x40]
002B4E4C  F6 82 AC 00 00 00 40            test byte ptr [rdx + 0xac], 0x40
002B4E53  75 1C                           jne 0x1402b4e71
002B4E55  44 8B 45 B7                     mov r8d, dword ptr [rbp - 0x49]
002B4E59  41 B9 01 00 00 00               mov r9d, 1
002B4E5F  48 8B CB                        mov rcx, rbx
002B4E62  E8 89 D3 0C 00                  call 0x1403821f0
002B4E67  44 8B 4D 7F                     mov r9d, dword ptr [rbp + 0x7f]
002B4E6B  48 8B D8                        mov rbx, rax
002B4E6E  45 33 DB                        xor r11d, r11d
002B4E71  4C 8B 6D 97                     mov r13, qword ptr [rbp - 0x69]
002B4E75  45 85 C9                        test r9d, r9d
002B4E78  0F 84 91 03 00 00               je 0x1402b520f
002B4E7E  49 8B 87 88 05 00 00            mov rax, qword ptr [r15 + 0x588]
002B4E85  41 8D 76 01                     lea esi, [r14 + 1]
002B4E89  8B 38                           mov edi, dword ptr [rax]
002B4E8B  4C 8B 40 08                     mov r8, qword ptr [rax + 8]
002B4E8F  49 8B C8                        mov rcx, r8
002B4E92  83 E1 04                        and ecx, 4
002B4E95  8B C1                           mov eax, ecx
002B4E97  8D 57 FF                        lea edx, [rdi - 1]
002B4E9A  48 F7 D8                        neg rax
002B4E9D  45 1B D2                        sbb r10d, r10d
002B4EA0  41 83 E2 20                     and r10d, 0x20
002B4EA4  48 F7 D9                        neg rcx
002B4EA7  48 1B C0                        sbb rax, rax
002B4EAA  83 E0 04                        and eax, 4
002B4EAD  4C 2B C0                        sub r8, rax
002B4EB0  3B F7                           cmp esi, edi
002B4EB2  45 1B C9                        sbb r9d, r9d
002B4EB5  44 23 CE                        and r9d, esi
002B4EB8  41 BE 01 00 00 00               mov r14d, 1
002B4EBE  45 8D 1C 12                     lea r11d, [r10 + rdx]
002B4EC2  41 8B C3                        mov eax, r11d
002B4EC5  43 8D 0C 0A                     lea ecx, [r10 + r9]
002B4EC9  2B C1                           sub eax, ecx
002B4ECB  41 03 C6                        add eax, r14d
002B4ECE  41 3B C6                        cmp eax, r14d
002B4ED1  0F 82 46 04 00 00               jb 0x1402b531d
002B4ED7  41 8B D6                        mov edx, r14d
002B4EDA  41 8B C3                        mov eax, r11d
002B4EDD  48 C1 E8 06                     shr rax, 6
002B4EE1  4D 8D 24 C0                     lea r12, [r8 + rax*8]
002B4EE5  8B C1                           mov eax, ecx
002B4EE7  48 C1 E8 06                     shr rax, 6
002B4EEB  80 E1 3F                        and cl, 0x3f
002B4EEE  48 D3 E2                        shl rdx, cl
002B4EF1  49 2B D6                        sub rdx, r14
002B4EF4  4D 8D 34 C0                     lea r14, [r8 + rax*8]
002B4EF8  49 8B 06                        mov rax, qword ptr [r14]
002B4EFB  48 F7 D0                        not rax
002B4EFE  48 0B D0                        or rdx, rax
002B4F01  48 83 C8 FF                     or rax, 0xffffffffffffffff
002B4F05  48 3B D0                        cmp rdx, rax
002B4F08  0F 85 A6 00 00 00               jne 0x1402b4fb4
002B4F0E  49 83 C6 08                     add r14, 8
002B4F12  4D 3B F4                        cmp r14, r12
002B4F15  0F 87 FE 03 00 00               ja 0x1402b5319
002B4F1B  49 8B 16                        mov rdx, qword ptr [r14]
002B4F1E  48 F7 D2                        not rdx
002B4F21  EB E2                           jmp 0x1402b4f05
002B4F23  41 03 DF                        add ebx, r15d
002B4F26  85 1D 80 03 D1 00               test dword ptr [rip + 0xd10380], ebx
002B4F2C  0F 84 83 03 00 00               je 0x1402b52b5
002B4F32  F3 90                           pause
002B4F34  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
002B4F38  48 85 C0                        test rax, rax
002B4F3B  0F 89 E8 FD FF FF               jns 0x1402b4d29
002B4F41  EB E0                           jmp 0x1402b4f23
002B4F43  41 B8 03 00 00 00               mov r8d, 3
002B4F49  48 8B D3                        mov rdx, rbx
002B4F4C  49 8B CF                        mov rcx, r15
002B4F4F  E8 7C F0 FC FF                  call 0x140283fd0
002B4F54  E9 6C FE FF FF                  jmp 0x1402b4dc5
002B4F59  E8 82 24 FC FF                  call 0x1402773e0
002B4F5E  85 C0                           test eax, eax
002B4F60  75 0A                           jne 0x1402b4f6c
002B4F62  BA 01 00 00 00                  mov edx, 1
002B4F67  E9 7D FD FF FF                  jmp 0x1402b4ce9
002B4F6C  83 3D AD 1D D1 00 00            cmp dword ptr [rip + 0xd11dad], 0
002B4F73  74 0C                           je 0x1402b4f81
002B4F75  44 0F 20 C1                     mov rcx, cr8
002B4F79  41 8A D4                        mov dl, r12b
002B4F7C  E8 17 07 24 00                  call 0x1404f5698
002B4F81  41 0F B6 C4                     movzx eax, r12b
002B4F85  44 0F 22 C0                     mov cr8, rax
002B4F89  44 0F 20 C3                     mov rbx, cr8
002B4F8D  44 0F 22 C7                     mov cr8, rdi
002B4F91  83 3D 88 1D D1 00 00            cmp dword ptr [rip + 0xd11d88], 0
002B4F98  0F 85 3E 03 00 00               jne 0x1402b52dc
002B4F9E  44 8A E3                        mov r12b, bl
002B4FA1  EB BF                           jmp 0x1402b4f62
002B4FA3  48 8B 46 60                     mov rax, qword ptr [rsi + 0x60]
002B4FA7  48 83 E0 FB                     and rax, 0xfffffffffffffffb
002B4FAB  48 89 46 60                     mov qword ptr [rsi + 0x60], rax
002B4FAF  E9 AB FD FF FF                  jmp 0x1402b4d5f
002B4FB4  4D 2B F0                        sub r14, r8
002B4FB7  48 F7 D2                        not rdx
002B4FBA  49 C1 FE 03                     sar r14, 3
002B4FBE  41 83 CC FF                     or r12d, 0xffffffff
002B4FC2  48 0F BC C2                     bsf rax, rdx
002B4FC6  41 C1 E6 06                     shl r14d, 6
002B4FCA  44 03 F0                        add r14d, eax
002B4FCD  45 3B F3                        cmp r14d, r11d
002B4FD0  0F 87 47 03 00 00               ja 0x1402b531d
002B4FD6  45 3B F4                        cmp r14d, r12d
002B4FD9  0F 84 41 03 00 00               je 0x1402b5320
002B4FDF  45 2B F2                        sub r14d, r10d
002B4FE2  49 8B 87 88 05 00 00            mov rax, qword ptr [r15 + 0x588]
002B4FE9  44 01 65 7F                     add dword ptr [rbp + 0x7f], r12d
002B4FED  41 8B D6                        mov edx, r14d
002B4FF0  48 C1 EA 03                     shr rdx, 3
002B4FF4  48 03 50 08                     add rdx, qword ptr [rax + 8]
002B4FF8  41 8B C6                        mov eax, r14d
002B4FFB  83 E0 07                        and eax, 7
002B4FFE  41 8B FE                        mov edi, r14d
002B5001  0F BE 0A                        movsx ecx, byte ptr [rdx]
002B5004  0F B3 C1                        btr ecx, eax
002B5007  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
002B500B  88 0A                           mov byte ptr [rdx], cl
002B500D  48 8B 04 F8                     mov rax, qword ptr [rax + rdi*8]
002B5011  48 3B 05 60 24 B8 00            cmp rax, qword ptr [rip + 0xb82460]
002B5018  0F 84 3E 02 00 00               je 0x1402b525c
002B501E  48 8D 34 40                     lea rsi, [rax + rax*2]
002B5022  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B502C  48 C1 E6 04                     shl rsi, 4
002B5030  48 8B C0                        mov rax, rax
002B5033  48 03 F0                        add rsi, rax
002B5036  48 8B CE                        mov rcx, rsi
002B5039  E8 02 53 06 00                  call 0x14031a340
002B503E  BA 01 00 00 00                  mov edx, 1
002B5043  48 8B CE                        mov rcx, rsi
002B5046  40 8A F8                        mov dil, al
002B5049  E8 12 D9 0A 00                  call 0x140362960
002B504E  40 8A D7                        mov dl, dil
002B5051  48 8B CE                        mov rcx, rsi
002B5054  E8 87 53 06 00                  call 0x14031a3e0
002B5059  44 8B 4D 7F                     mov r9d, dword ptr [rbp + 0x7f]
002B505D  45 33 DB                        xor r11d, r11d
002B5060  E9 10 FE FF FF                  jmp 0x1402b4e75
002B5065  3B 15 A1 01 D1 00               cmp edx, dword ptr [rip + 0xd101a1]
002B506B  0F 85 FF F6 FF FF               jne 0x1402b4770
002B5071  E9 26 69 42 00                  jmp 0x1406db99c
002B5076  8B 05 90 01 D1 00               mov eax, dword ptr [rip + 0xd10190]
002B507C  B9 40 00 00 00                  mov ecx, 0x40
002B5081  41 B8 4D 6D 53 77               mov r8d, 0x77536d4d
002B5087  48 8D 14 C5 60 00 00 00         lea rdx, [rax*8 + 0x60]
002B508F  E8 AC 64 0A 00                  call 0x14035b540
002B5094  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
002B5098  48 8B D8                        mov rbx, rax
002B509B  49 89 44 24 48                  mov qword ptr [r12 + 0x48], rax
002B50A0  48 85 C0                        test rax, rax
002B50A3  0F 85 D9 F6 FF FF               jne 0x1402b4782
002B50A9  41 C7 87 C4 04 00 00 20 00 00 00  mov dword ptr [r15 + 0x4c4], 0x20
002B50B4  B8 9A 00 00 C0                  mov eax, 0xc000009a
002B50B9  E9 A7 00 00 00                  jmp 0x1402b5165
002B50BE  44 8B C1                        mov r8d, ecx
002B50C1  33 D2                           xor edx, edx
002B50C3  49 8B 8F 88 05 00 00            mov rcx, qword ptr [r15 + 0x588]
002B50CA  E8 C1 C9 12 00                  call 0x1403e1a90
002B50CF  83 63 58 00                     and dword ptr [rbx + 0x58], 0
002B50D3  41 BE 29 04 00 C0               mov r14d, 0xc0000429
002B50D9  48 83 C8 FF                     or rax, 0xffffffffffffffff
002B50DD  49 8B CF                        mov rcx, r15
002B50E0  66 41 01 85 E6 01 00 00         add word ptr [r13 + 0x1e6], ax
002B50E8  90                              nop
002B50E9  E8 7A 9E 1D 00                  call 0x14048ef68
002B50EE  41 BF 01 00 00 00               mov r15d, 1
002B50F4  90                              nop
002B50F5  66 45 01 BD E6 01 00 00         add word ptr [r13 + 0x1e6], r15w
002B50FD  75 12                           jne 0x1402b5111
002B50FF  49 8D 85 98 00 00 00            lea rax, [r13 + 0x98]
002B5106  90                              nop
002B5107  48 39 00                        cmp qword ptr [rax], rax
002B510A  74 05                           je 0x1402b5111
002B510C  E8 6F DB 02 00                  call 0x1402e2c80
002B5111  49 8B CD                        mov rcx, r13
002B5114  E8 D7 9E FA FF                  call 0x14025eff0
002B5119  48 8B 75 9F                     mov rsi, qword ptr [rbp - 0x61]
002B511D  48 8B 36                        mov rsi, qword ptr [rsi]
002B5120  48 85 F6                        test rsi, rsi
002B5123  74 31                           je 0x1402b5156
002B5125  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
002B512A  48 8D 8F C8 00 00 00            lea rcx, [rdi + 0xc8]
002B5131  E8 5A 35 F9 FF                  call 0x140248690
002B5136  FF 0E                           dec dword ptr [rsi]
002B5138  48 8D 8F C8 00 00 00            lea rcx, [rdi + 0xc8]
002B513F  8B 1E                           mov ebx, dword ptr [rsi]
002B5141  8A D0                           mov dl, al
002B5143  E8 78 31 F9 FF                  call 0x1402482c0
002B5148  85 DB                           test ebx, ebx
002B514A  75 0A                           jne 0x1402b5156
002B514C  33 D2                           xor edx, edx
002B514E  48 8B CE                        mov rcx, rsi
002B5151  E8 1A D7 8C 00                  call 0x140b82870
002B5156  48 83 7C 24 58 00               cmp qword ptr [rsp + 0x58], 0
002B515C  0F 85 FE 01 00 00               jne 0x1402b5360
002B5162  41 8B C6                        mov eax, r14d
002B5165  48 8B 9C 24 48 01 00 00         mov rbx, qword ptr [rsp + 0x148]
002B516D  48 81 C4 00 01 00 00            add rsp, 0x100
002B5174  41 5F                           pop r15
002B5176  41 5E                           pop r14
002B5178  41 5D                           pop r13
002B517A  41 5C                           pop r12
002B517C  5F                              pop rdi
002B517D  5E                              pop rsi
002B517E  5D                              pop rbp
002B517F  C3                              ret
002B5180  CC                              int3
002B5181  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
002B5185  44 8B CA                        mov r9d, edx
002B5188  81 FB 9A 00 00 C0               cmp ebx, 0xc000009a
002B518E  45 8B C2                        mov r8d, r10d
002B5191  0F 44 C2                        cmove eax, edx
002B5194  01 55 7F                        add dword ptr [rbp + 0x7f], edx
002B5197  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002B519C  83 E1 07                        and ecx, 7
002B519F  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
002B51A3  49 8B 87 88 05 00 00            mov rax, qword ptr [r15 + 0x588]
002B51AA  48 C1 EE 03                     shr rsi, 3
002B51AE  48 03 70 08                     add rsi, qword ptr [rax + 8]
002B51B2  0F BE 06                        movsx eax, byte ptr [rsi]
002B51B5  0F AB C8                        bts eax, ecx
002B51B8  48 8B 0D C1 B6 D5 FF            mov rcx, qword ptr [rip - 0x2a493f]
002B51BF  88 06                           mov byte ptr [rsi], al
002B51C1  E8 2A D0 0C 00                  call 0x1403821f0
002B51C6  41 B8 03 00 00 00               mov r8d, 3
002B51CC  48 8B D0                        mov rdx, rax
002B51CF  49 8B CF                        mov rcx, r15
002B51D2  E8 F9 ED FC FF                  call 0x140283fd0
002B51D7  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
002B51DB  49 8B D7                        mov rdx, r15
002B51DE  E8 65 E8 F4 FF                  call 0x140203a48
002B51E3  B8 01 00 00 00                  mov eax, 1
002B51E8  49 8D 56 08                     lea rdx, [r14 + 8]
002B51EC  41 01 87 C8 04 00 00            add dword ptr [r15 + 0x4c8], eax
002B51F3  8B CB                           mov ecx, ebx
002B51F5  45 8B 8F C8 04 00 00            mov r9d, dword ptr [r15 + 0x4c8]
002B51FC  45 8B 46 04                     mov r8d, dword ptr [r14 + 4]
002B5200  E8 47 9C 1D 00                  call 0x14048ee4c
002B5205  BA 01 00 00 00                  mov edx, 1
002B520A  E9 BF FB FF FF                  jmp 0x1402b4dce
002B520F  4C 8B 65 67                     mov r12, qword ptr [rbp + 0x67]
002B5213  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
002B5217  03 44 24 38                     add eax, dword ptr [rsp + 0x38]
002B521B  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
002B521F  41 83 4C 24 28 40               or dword ptr [r12 + 0x28], 0x40
002B5225  4C 8B 6D BF                     mov r13, qword ptr [rbp - 0x41]
002B5229  3B C1                           cmp eax, ecx
002B522B  0F 85 68 01 00 00               jne 0x1402b5399
002B5231  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002B5236  4C 39 98 B8 00 00 00            cmp qword ptr [rax + 0xb8], r11
002B523D  0F 85 56 01 00 00               jne 0x1402b5399
002B5243  49 8B CC                        mov rcx, r12
002B5246  E8 49 EC F4 FF                  call 0x140203e94
002B524B  41 BE 03 01 00 00               mov r14d, 0x103
002B5251  41 BF 01 00 00 00               mov r15d, 1
002B5257  E9 B5 FE FF FF                  jmp 0x1402b5111
002B525C  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
002B5260  48 8B CB                        mov rcx, rbx
002B5263  41 03 D6                        add edx, r14d
002B5266  E8 D5 85 0B 00                  call 0x14036d840
002B526B  48 8B D0                        mov rdx, rax
002B526E  49 8B CF                        mov rcx, r15
002B5271  41 B8 02 00 00 00               mov r8d, 2
002B5277  48 8B D8                        mov rbx, rax
002B527A  E8 51 ED FC FF                  call 0x140283fd0
002B527F  48 8B 05 FA B5 D5 FF            mov rax, qword ptr [rip - 0x2a4a06]
002B5286  49 89 44 FD 60                  mov qword ptr [r13 + rdi*8 + 0x60], rax
002B528B  E9 C9 FD FF FF                  jmp 0x1402b5059
002B5290  44 8B C1                        mov r8d, ecx
002B5293  C7 44 24 28 20 00 00 40         mov dword ptr [rsp + 0x28], 0x40000020
002B529B  48 8B CE                        mov rcx, rsi
002B529E  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
002B52A3  45 33 C9                        xor r9d, r9d
002B52A6  33 D2                           xor edx, edx
002B52A8  E8 53 35 06 00                  call 0x140318800
002B52AD  48 8B C8                        mov rcx, rax
002B52B0  E9 4D F5 FF FF                  jmp 0x1402b4802
002B52B5  8B 05 FD 17 D1 00               mov eax, dword ptr [rip + 0xd117fd]
002B52BB  A8 40                           test al, 0x40
002B52BD  0F 84 6F FC FF FF               je 0x1402b4f32
002B52C3  E8 C8 A1 05 00                  call 0x14030f490
002B52C8  84 C0                           test al, al
002B52CA  0F 84 62 FC FF FF               je 0x1402b4f32
002B52D0  8B CB                           mov ecx, ebx
002B52D2  E8 89 A1 05 00                  call 0x14030f460
002B52D7  E9 58 FC FF FF                  jmp 0x1402b4f34
002B52DC  40 8A D7                        mov dl, dil
002B52DF  8A CB                           mov cl, bl
002B52E1  E8 16 04 24 00                  call 0x1404f56fc
002B52E6  E9 B3 FC FF FF                  jmp 0x1402b4f9e
002B52EB  90                              nop
002B52EC  66 41 01 8D E6 01 00 00         add word ptr [r13 + 0x1e6], cx
002B52F4  75 0D                           jne 0x1402b5303
002B52F6  49 8D 85 98 00 00 00            lea rax, [r13 + 0x98]
002B52FD  90                              nop
002B52FE  48 39 00                        cmp qword ptr [rax], rax
002B5301  75 7C                           jne 0x1402b537f
002B5303  41 BE A0 04 00 C0               mov r14d, 0xc00004a0
002B5309  E9 43 FF FF FF                  jmp 0x1402b5251
002B530E  03 CB                           add ecx, ebx
002B5310  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
002B5314  E9 CB F8 FF FF                  jmp 0x1402b4be4
002B5319  41 83 CC FF                     or r12d, 0xffffffff
002B531D  45 8B F4                        mov r14d, r12d
002B5320  45 33 DB                        xor r11d, r11d
002B5323  45 85 C9                        test r9d, r9d
002B5326  0F 84 B6 FC FF FF               je 0x1402b4fe2
002B532C  8D 56 01                        lea edx, [rsi + 1]
002B532F  45 8B CB                        mov r9d, r11d
002B5332  3B D7                           cmp edx, edi
002B5334  0F 47 D7                        cmova edx, edi
002B5337  41 03 D4                        add edx, r12d
002B533A  E9 79 FB FF FF                  jmp 0x1402b4eb8
002B533F  41 8B 8F C4 04 00 00            mov ecx, dword ptr [r15 + 0x4c4]
002B5346  E8 51 DA 1F 00                  call 0x1404b2d9c
002B534B  41 8B 87 C4 04 00 00            mov eax, dword ptr [r15 + 0x4c4]
002B5352  FF C8                           dec eax
002B5354  41 89 87 C4 04 00 00            mov dword ptr [r15 + 0x4c4], eax
002B535B  E9 54 FD FF FF                  jmp 0x1402b50b4
002B5360  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
002B5364  44 84 78 0A                     test byte ptr [rax + 0xa], r15b
002B5368  0F 84 F4 FD FF FF               je 0x1402b5162
002B536E  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
002B5372  48 8B D0                        mov rdx, rax
002B5375  E8 E6 1A F9 FF                  call 0x140246e60
002B537A  E9 E3 FD FF FF                  jmp 0x1402b5162
002B537F  E8 FC D8 02 00                  call 0x1402e2c80
002B5384  E9 7A FF FF FF                  jmp 0x1402b5303
002B5389  40 8A D7                        mov dl, dil
002B538C  41 8A CC                        mov cl, r12b
002B538F  E8 68 03 24 00                  call 0x1404f56fc
002B5394  E9 29 F9 FF FF                  jmp 0x1402b4cc2
002B5399  44 8B C9                        mov r9d, ecx
002B539C  4D 8D 44 24 68                  lea r8, [r12 + 0x68]
002B53A1  49 8B D4                        mov rdx, r12
002B53A4  E8 03 CD 1D 00                  call 0x1404920ac
002B53A9  E9 95 FE FF FF                  jmp 0x1402b5243
002B53AE  41 BE 88 00 00 C0               mov r14d, 0xc0000088
002B53B4  E9 20 FD FF FF                  jmp 0x1402b50d9
002B53B9  48 8B D7                        mov rdx, rdi
002B53BC  49 8B CF                        mov rcx, r15
002B53BF  E8 E8 1F 24 00                  call 0x1404f73ac
002B53C4  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
002B53C7  85 C0                           test eax, eax
002B53C9  75 60                           jne 0x1402b542b
002B53CB  E8 F8 73 24 00                  call 0x1404fc7c8
002B53D0  B8 7F 00 00 C0                  mov eax, 0xc000007f
002B53D5  E9 8B FD FF FF                  jmp 0x1402b5165
002B53DA  FF 09                           dec dword ptr [rcx]
002B53DC  83 39 00                        cmp dword ptr [rcx], 0
002B53DF  0F 85 6B F8 FF FF               jne 0x1402b4c50
002B53E5  48 85 C9                        test rcx, rcx
002B53E8  0F 84 62 F8 FF FF               je 0x1402b4c50
002B53EE  33 D2                           xor edx, edx
002B53F0  E8 7B D4 8C 00                  call 0x140b82870
002B53F5  E9 56 F8 FF FF                  jmp 0x1402b4c50
002B53FA  33 C9                           xor ecx, ecx
002B53FC  E8 C7 CF 0C 00                  call 0x1403823c8
002B5401  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
002B5405  48 8B 51 40                     mov rdx, qword ptr [rcx + 0x40]
002B5409  F6 82 AC 00 00 00 40            test byte ptr [rdx + 0xac], 0x40
002B5410  74 22                           je 0x1402b5434
002B5412  41 B8 04 00 00 00               mov r8d, 4
002B5418  48 8B D0                        mov rdx, rax
002B541B  49 8B CF                        mov rcx, r15
002B541E  E8 5D E7 0B 00                  call 0x140373b80
002B5423  45 33 DB                        xor r11d, r11d
002B5426  E9 88 F5 FF FF                  jmp 0x1402b49b3
002B542B  8B 54 24 40                     mov edx, dword ptr [rsp + 0x40]
002B542F  E9 24 F3 FF FF                  jmp 0x1402b4758
002B5434  4C 8B 45 B7                     mov r8, qword ptr [rbp - 0x49]
002B5438  41 B9 01 00 00 00               mov r9d, 1
002B543E  44 03 C7                        add r8d, edi
002B5441  48 8B C8                        mov rcx, rax
002B5444  E8 A7 CD 0C 00                  call 0x1403821f0
002B5449  EB D8                           jmp 0x1402b5423
002B544B  BB 01 00 00 00                  mov ebx, 1
002B5450  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
002B5454  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
002B5459  E9 A4 65 42 00                  jmp 0x1406dba02
002B545E  49 8B CF                        mov rcx, r15
002B5461  E8 36 77 1F 00                  call 0x1404acb9c
002B5466  85 C0                           test eax, eax
002B5468  0F 84 19 F7 FF FF               je 0x1402b4b87
002B546E  49 8D 8F A0 03 00 00            lea rcx, [r15 + 0x3a0]
002B5475  45 33 C0                        xor r8d, r8d
002B5478  33 D2                           xor edx, edx
002B547A  E8 91 9E 08 00                  call 0x14033f310
002B547F  E9 03 F7 FF FF                  jmp 0x1402b4b87
002B5484  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
002B5488  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
002B548D  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
002B5491  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
002B5496  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
002B549A  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
002B549E  E9 5F 65 42 00                  jmp 0x1406dba02
002B54A3  41 C7 87 C4 04 00 00 20 00 00 00  mov dword ptr [r15 + 0x4c4], 0x20
002B54AE  E9 64 F9 FF FF                  jmp 0x1402b4e17
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiStoreWriteModifiedPages(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int8 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned int v_stack_p3C;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (256);
    v_r14 = 0;
    v_stack_m68 = a1 + 104;
    v_stack_mD8 = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 104 + 40))) >> (12));
    v_stack_m88 = v_xmm0;
    v_stack_mB0 = 0;
    v_stack_m70 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216);
    v_stack_mF8 = a2;
    v_stack_m58 = v_xmm1;
    v_stack_m48 = v_xmm0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1220))) != 0) goto loc_002B533F;
    v_stack_mF0 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1204)) * 8 + 18528);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1204)) * 8 + 18528) + 12)))) < a2) goto loc_002B53B9;
loc_002B4758:
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_002B4770;
    if ((*(unsigned __int16 *)(v_rip + 13699222)) > 1) goto loc_002B5065;
loc_002B4770:
    v_stack_mC8 = *(unsigned __int64 *)(a1 + 72);
    if (*(unsigned __int64 *)(a1 + 72) == 0) goto loc_002B5076;
loc_002B4782:
    v_stack_mC0 = v_stack_m60;
    result = (v_stack_m60) | (-1);
    v_stack_m60 = 0;
    v_stack_mE8 = 0;
    v_stack_mE0 = 0;
    v_stack_mA0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1304)) != 0) goto loc_002B52EB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1304)) != 0) goto loc_002B47F4;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(result + 2, a2, a3, a4);
        a1 = 1;
    }
    if (((*(unsigned __int8 *)(a1 + 104 + 10)) & (5)) == 0) goto loc_002B5290;
loc_002B4802:
    v_r11 = 0;
    v_stack_mE0 = *(unsigned __int64 *)(a1 + 104 + 24);
    if (*(unsigned __int64 *)(a1 + 104 + 24) == 0) goto loc_002B53AE;
    v_stack_mFC = 0;
    v_stack_p20 = 0;
    v_stack_m100 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 88) = (unsigned int)((unsigned int)(v_stack_mF8) + 1);
    v_stack_mD0 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424);
    v_r10 = (*(unsigned __int64 *)(a1 + 88)) >> (12);
    v_stack_m90 = a1 + 152;
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1204)) * 8 + 18528) + 88)));
    v_stack_mA8 = v_r10;
loc_002B4867:
    v_stack_m98 = a1 + 152;
    v_stack_m104 = 0;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_mF8)))) goto loc_002B4C70;
    if ((*(unsigned __int64 *)(a1 + 152)) == (*(unsigned __int64 *)(v_rip + 12069862))) goto loc_002B530E;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 12))) == 0) goto loc_002B4C1D;
    if (v_stack_m60 != (*(unsigned __int64 *)(v_stack_mF0 + 80))) goto loc_002B4C47;
loc_002B48B6:
    a3 = (unsigned int)((2) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1204)) * 8 + 18528) + 88)))));
    a1 = (unsigned int)((v_stack_m50) & (4));
    result = -((unsigned int)((unsigned int)(a1)));
    v_r10 = (unsigned int)((v_r10) & (32));
    a1 = -(a1);
    result = (unsigned int)((result) & (4));
    a4 = (v_stack_m50) - (result);
loc_002B48EB:
    v_stack_mB8 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r10 + (unsigned int)(v_stack_m58) - 1 * 1))) - ((unsigned int)(v_r10 + a3 * 1)));
    result = (unsigned int)((result) + (1));
    if (((unsigned int)(result)) < 1) goto loc_002B4C25;
    a1 = (unsigned __int8)((v_r10 + a3 * 1) & (63));
    a2 = ((unsigned int)((unsigned int)(v_r10 + a3 * 1))) >> (6);
    result = ((unsigned int)((unsigned int)(v_r10 + (unsigned int)(v_stack_m58) - 1 * 1))) >> (6);
    result = (1) << ((unsigned __int8)(a1));
    result = (result) - (1);
    a1 = (*(unsigned __int64 *)(a4 + a2 * 8)) | (result);
loc_002B4931:
    if (a1 != -1) goto loc_002B4949;
    v_rbx = (a4 + a2 * 8) + (8);
    if (v_rbx > (a4 + result * 8)) goto loc_002B4C25;
    goto loc_002B4931;
loc_002B4949:
    v_rbx = (v_rbx) - (a4);
    a1 = ~(*(unsigned __int64 *)(v_rbx));
    v_rbx = (v_rbx) >> (3);
    v_rbx = (unsigned int)((v_rbx) << (6));
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(result)));
    v_stack_mB8 = (unsigned int)(result);
    if (((unsigned int)(v_rbx)) > ((unsigned int)(v_r10 + (unsigned int)(v_stack_m58) - 1 * 1))) goto loc_002B4C25;
    if (((unsigned int)(v_rbx)) == -1) goto loc_002B4C28;
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(v_r10)));
loc_002B4974:
loc_002B4978:
    v_r12 = (*(unsigned __int64 *)(a1 + 152) + *(unsigned __int64 *)(a1 + 152) * 2) << (4);
    result = MiLockPageInline(v_r12 + result * 1, a2, a3, a4);
    result = MiIsPfnOriginalPteLost(v_r12 + result * 1, a2, a3, a4);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_002B53FA;
loc_002B49B3:
    *(unsigned __int64 *)(v_stack_mC8 + (unsigned int)(v_stack_m104) * 8 + 96) = *(unsigned __int64 *)(v_r12 + result * 1 + 16);
    if (((unsigned int)(v_rbx)) == -1) goto loc_002B4BC8;
    if (((unsigned int)(v_rbx)) < -1) goto loc_002B4BC8;
    v_stack_mB0 = 0;
    v_stack_m118 = v_stack_mB0;
    result = MiStoreCheckCandidatePage(v_r12 + result * 1, (unsigned int)((unsigned int)(v_rbx)), v_stack_mD8, v_stack_m88);
    v_r11 = 0;
    if (sign_flag) goto loc_002B4BBC;
    if (((v_stack_m80) & ((unsigned __int8)(v_r11 + 3))) != 0) goto loc_002B4A49;
loc_002B4A14:
    if (*(unsigned __int64 *)(v_stack_m88 - 48) == 0) goto loc_002B4BC8;
    if (*(unsigned __int64 *)(v_stack_m88 - 48) != 0) goto loc_002B4A14;
    result = ObpTraceObjectReferenceIfActive(v_stack_m88 - 48, 1, (unsigned int)(0x66506D4DULL), v_stack_m88);
    v_r11 = 0;
    v_stack_mE8 = v_stack_m88;
loc_002B4A49:
    if (((unsigned __int8)((unsigned __int8)(result))) >= 2) goto loc_002B4A77;
    result = v_stack_m88;
    if ((*(unsigned int *)(v_rip + 13705915)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(0x66506D4DULL), v_stack_m88);
    }
loc_002B4A77:
    result = MiStoreGetWriteSupport(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216), a2, (unsigned int)(0x66506D4DULL), v_stack_m88);
    v_r11 = 0;
    if (result == 0) goto loc_002B544B;
    *(unsigned __int64 *)(result + 24) = v_stack_mE8;
    *(unsigned __int64 *)(result + 32) = 0;
    *(unsigned int *)(result + 32 + 8) = 56;
    *(unsigned __int64 *)(result + 32 + 32) = 0;
    *(unsigned __int64 *)(result + 32 + 40) = 0x1000ULL;
    *(unsigned __int64 *)(result + 56) = v_stack_mE0;
    v_r12 = (v_r12) >> (4);
    v_r12 = (v_r12) * (v_r11 + 3);
    *(unsigned __int64 *)(result) = v_stack_p8;
    *(unsigned __int64 *)(result + 80) = v_r12;
    *(unsigned int *)(v_stack_mD0 + 24) = (unsigned int)((unsigned int)(v_stack_m104));
    *(unsigned int *)(v_stack_mD0 + 4) = (unsigned int)((unsigned int)(v_stack_mD8));
    *(unsigned __int64 *)(v_stack_mD0 + 32) = v_stack_mB0;
    *(unsigned __int64 *)(v_stack_mD0 + 40) = result + 32;
    *(unsigned __int64 *)(v_stack_mD0 + 56) = result + 8;
    v_stack_mE8 = 0;
    *(unsigned __int64 *)(v_stack_mD0 + 8) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mD0 + 48) = result;
    result = ExAcquireSpinLockExclusive(v_stack_mF0 + 200, result, v_stack_mD0, v_stack_m88);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (7));
    a4 = ((unsigned int)((unsigned int)(v_rbx))) >> (3);
    a4 = (a4) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 80) + 16));
    v_stack_m108 = (unsigned int)(v_rbx + 1);
    *(unsigned __int8 *)(a4) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(a4)));
    *(unsigned int *)(v_stack_mF0 + 88) = (unsigned int)(v_rbx + 1);
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mF0 + 12))) - 1);
    *(unsigned int *)(v_stack_mF0 + 12) = (unsigned int)(v_rbx);
    result = MiUpdatePagefilePeakUsage(v_stack_mF0, a2, (__int8)(*(unsigned __int8 *)(a4)), a4);
    result = MiReleaseSpinLockExclusive(v_stack_mF0 + 200, (unsigned __int8)((unsigned __int8)(result)), (__int8)(*(unsigned __int8 *)(a4)), a4);
    if ((unsigned int)(v_rbx) == 0) goto loc_002B545E;
loc_002B4B87:
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m104)) + (1));
    result = (v_stack_m98) + (8);
    v_r11 = 0;
    goto loc_002B4867;
loc_002B4BBC:
    result = MiStoreLogNotCandidate((unsigned int)((unsigned int)(result)), 1, (__int8)(*(unsigned __int8 *)(a4)), (unsigned int)(v_stack_p20));
    v_r11 = 0;
loc_002B4BC8:
loc_002B4BE4:
    if (17 == 17) goto loc_002B5484;
    if (17 >= 2) goto loc_002B4C15;
    if ((*(unsigned int *)(v_rip + 13705505)) != 0) {
        a1 = (unsigned __int8)(result);
        a2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 2, (unsigned int)(v_stack_p20));
    }
loc_002B4C15:
    goto loc_002B5454;
loc_002B4C1D:
    v_rbx = (unsigned int)((2 - 1) | (0xFFFFFFFFULL));
    goto loc_002B4978;
loc_002B4C25:
    v_rbx = (unsigned int)((v_rbx) | (0xFFFFFFFFULL));
loc_002B4C28:
    v_r11 = 0;
    if (2 == 0) goto loc_002B4974;
    a2 = v_r12 + result * 1 + 1;
    if (((unsigned int)(v_r12 + result * 1 + 1)) > ((unsigned int)(v_rdi))) { a2 = (unsigned int)(v_rdi); }
    a2 = (unsigned int)((a2) - 1);
    goto loc_002B48EB;
loc_002B4C47:
    if (a1 != 0) goto loc_002B53DA;
loc_002B4C50:
    result = MiRefPageFileSpaceBitmaps(v_rbx, v_stack_m60, 0, (unsigned int)(v_stack_p20));
    v_stack_mC0 = v_stack_m60;
    v_r11 = 0;
    goto loc_002B48B6;
loc_002B4C70:
    a3 = (v_stack_mD0) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424));
    a3 = (a3) >> (6);
    v_stack_m104 = 0;
    if ((unsigned int)(a3) == 0) goto loc_002B4E0C;
    result = SmPageWrite(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 184), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424), a3, (unsigned int)(v_stack_p20));
    if ((*(unsigned int *)(v_rip + 13705316)) != 0) goto loc_002B5389;
loc_002B4CC2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424)) >= v_stack_mD0) goto loc_002B4DE5;
loc_002B4CDC:
    v_r13 = (unsigned int)(((unsigned int)(v_stack_m108)) + (1));
    if ((((unsigned __int8)(v_r13)) & (15)) == 0) goto loc_002B4F59;
loc_002B4CE9:
    v_rdi = (*(unsigned __int64 *)(v_stack_m90 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424) + 24)) * 8) + *(unsigned __int64 *)(v_stack_m90 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424) + 24)) * 8) * 2) << (4);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_stack_m90 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424) + 24)) * 8));
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424) + 4)));
    if (sign_flag) goto loc_002B5181;
    v_rbx = 0;
loc_002B4D29:
    if (condition_is_below) goto loc_002B4F23;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_mC8 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424) + 24)))) * 8 + 96))) >> (2));
    if ((((unsigned __int8)(v_rbx + 1)) & ((unsigned __int8)(result))) != 0) goto loc_002B4FA3;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_stack_mC8 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424) + 24)))) * 8 + 96))) >> (1));
    result = (unsigned __int8)((result) & ((unsigned __int8)(v_rbx + 1)));
    result = (unsigned __int8)(-(result));
    v_rbx = (*(unsigned __int64 *)(v_stack_mC8 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424) + 24)))) * 8 + 96)) & (result);
loc_002B4D5F:
    result = MiClearPageFileReservation(v_stack_mC8 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424) + 24)))) * 8 + 96, 1, a3, (unsigned int)(v_stack_p20));
    result = MiTransferSoftwarePte(*(unsigned __int64 *)(v_stack_mC8 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424) + 24)))) * 8 + 96), v_stack_mF0, (unsigned int)(v_stack_m108), (unsigned int)((unsigned int)(v_rbx + 1)));
    *(unsigned __int64 *)(v_stack_mC8 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424) + 24)))) * 8 + 96) = result;
    result = MiIsPfnOriginalPteLost(v_rdi, v_stack_mF0, (unsigned int)(v_stack_m108), (unsigned int)((unsigned int)(v_rbx + 1)));
    if ((unsigned int)(result) == 0) {
        a1 = v_rdi + 16;
        result = MiClearPageFileReservation(a1, v_stack_mF0, (unsigned int)(v_stack_m108), (unsigned int)((unsigned int)(v_rbx + 1)));
        a3 = v_stack_m108;
        a1 = v_rdi;
        a2 = v_stack_mF0;
        result = MiUpdatePfnBackingStore(a1, a2, a3, (unsigned int)((unsigned int)(v_rbx + 1)));
    }
    if (v_rbx != 0) goto loc_002B4F43;
loc_002B4DC5:
loc_002B4DCE:
    v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424)) + (64);
    if (v_r14 < v_stack_mD0) goto loc_002B4CDC;
loc_002B4DE5:
    v_r11 = 0;
    if ((*(unsigned int *)(v_rip + 13705009)) != 0) {
        a1 = 2;
        a2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, (unsigned int)((unsigned int)(v_rbx + 1)));
        v_r11 = 0;
    }
loc_002B4E0C:
    if (v_stack_mFC != 0) goto loc_002B54A3;
loc_002B4E17:
    result = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)(v_stack_p20)))));
    if (((unsigned int)((unsigned int)(v_stack_p20))) == ((unsigned int)((unsigned int)(v_stack_mF8)))) goto loc_002B50BE;
    v_r12 = (unsigned int)((17) | (0xFFFFFFFFULL));
    v_stack_mE0 = 0;
    result = v_stack_p8;
    v_rbx = *(unsigned __int64 *)(v_rip - 2770368);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8 + 64) + 172)) & (64)) == 0) {
        a3 = v_stack_mA8;
        a4 = 1;
        a1 = *(unsigned __int64 *)(v_rip - 2770368);
        result = MiTransferSoftwarePte(a1, *(unsigned __int64 *)(v_stack_p8 + 64), a3, a4);
        a4 = v_stack_p20;
        v_rbx = result;
        v_r11 = 0;
    }
loc_002B4E75:
    if ((unsigned int)(a4) == 0) goto loc_002B520F;
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 1416) + 8)) & (4));
    result = -((unsigned int)((unsigned int)(a1)));
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1424) + 4))) & (32));
    a1 = -(a1);
    result = (unsigned int)((result) & (4));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 1416) + 8)) - (result);
    a4 = (unsigned int)((a4) & ((unsigned int)((unsigned int)((unsigned int)(v_r12)) + 1)));
loc_002B4EB8:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r10 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m70 + 1416))) - 1 * 1))) - ((unsigned int)(v_r10 + a4 * 1)));
    result = (unsigned int)((result) + (1));
    if (((unsigned int)(result)) < 1) goto loc_002B531D;
    result = ((unsigned int)((unsigned int)(v_r10 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m70 + 1416))) - 1 * 1))) >> (6);
    result = ((unsigned int)((unsigned int)(v_r10 + a4 * 1))) >> (6);
    a1 = (unsigned __int8)((v_r10 + a4 * 1) & (63));
    a2 = (1) << ((unsigned __int8)(a1));
    a2 = (a2) - (1);
    result = ~(*(unsigned __int64 *)(a3 + result * 8));
    a2 = (a2) | (result);
    result = (result) | (-1);
loc_002B4F05:
    if (a2 != result) goto loc_002B4FB4;
    v_r14 = (a3 + result * 8) + (8);
    if (v_r14 > (a3 + result * 8)) goto loc_002B5319;
    a2 = ~(*(unsigned __int64 *)(v_r14));
    goto loc_002B4F05;
loc_002B4F23:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_stack_m70)));
    if (((*(unsigned int *)(v_rip + 13697920)) & ((unsigned int)(v_rbx))) == 0) goto loc_002B52B5;
loc_002B4F32:
loc_002B4F34:
    if (!sign_flag) goto loc_002B4D29;
    goto loc_002B4F23;
loc_002B4F43:
    result = MiReleasePageFileInfo(v_stack_m70, v_rbx, 3, a4);
    goto loc_002B4DC5;
loc_002B4F59:
    result = KeShouldYieldProcessor(v_stack_m70, v_rbx, 3, a4);
    if ((unsigned int)(result) != 0) goto loc_002B4F6C;
loc_002B4F62:
    goto loc_002B4CE9;
loc_002B4F6C:
    if ((*(unsigned int *)(v_rip + 13704621)) != 0) {
        a1 = 17;
        a2 = (unsigned __int8)(a3 + result * 8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 3, a4);
    }
    if ((*(unsigned int *)(v_rip + 13704584)) != 0) goto loc_002B52DC;
loc_002B4F9E:
    goto loc_002B4F62;
loc_002B4FA3:
    result = (*(unsigned __int64 *)((unsigned int)((unsigned int)(v_r12)) + 1 + 96)) & (-5);
    *(unsigned __int64 *)((unsigned int)((unsigned int)(v_r12)) + 1 + 96) = result;
    goto loc_002B4D5F;
loc_002B4FB4:
    v_r14 = (v_r14) - (3);
    a2 = ~(a2);
    v_r14 = (v_r14) >> (3);
    v_r12 = (unsigned int)(((unsigned __int8)((unsigned __int8)(a3 + result * 8))) | (0xFFFFFFFFULL));
    v_r14 = (unsigned int)((v_r14) << (6));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(result)));
    if (((unsigned int)(v_r14)) > ((unsigned int)(v_r10 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m70 + 1416))) - 1 * 1))) goto loc_002B531D;
    if (((unsigned int)(v_r14)) == ((unsigned int)(v_r12))) goto loc_002B5320;
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)(v_r10)));
loc_002B4FE2:
    a2 = ((unsigned int)((unsigned int)(v_r14))) >> (3);
    a2 = (a2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 1416) + 8));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (7));
    *(unsigned __int8 *)(a2) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(a2)));
    if ((*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)(v_r14)) * 8)) == (*(unsigned __int64 *)(v_rip + 12067936))) goto loc_002B525C;
    v_rsi = (*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)(v_r14)) * 8) + *(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)(v_r14)) * 8) * 2) << (4);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_stack_m90 + (unsigned int)((unsigned int)(v_r14)) * 8));
    result = MiLockPageInline(v_rsi, a2, 3, a4);
    result = MiSetPfnModified(v_rsi, 1, 3, a4);
    result = MiUnlockPage(v_rsi, (unsigned __int8)((unsigned __int8)(result)), 3, a4);
loc_002B5059:
    v_r11 = 0;
    goto loc_002B4E75;
loc_002B5065:
    if (((unsigned int)((unsigned __int8)((unsigned __int8)(result)))) != (*(unsigned int *)(v_rip + 13697441))) goto loc_002B4770;
loc_002B5076:
    result = MiAllocatePool(64, (unsigned int)(*(unsigned int *)(v_rip + 13697424)) * 8 + 96, (unsigned int)(0x77536D4DULL), (unsigned int)(v_stack_p20));
    v_stack_mC8 = result;
    *(unsigned __int64 *)(v_r12 + 72) = result;
    if (result != 0) goto loc_002B4782;
    *(unsigned int *)(v_stack_m70 + 1220) = 32;
loc_002B50B4:
    goto loc_002B5165;
loc_002B50BE:
    a2 = 0;
    result = RtlClearBits(*(unsigned __int64 *)(v_stack_m70 + 1416), a2, 64, (unsigned int)(v_stack_p20));
loc_002B50D9:
    result = (result) | (-1);
    result = MiStoreDecrementOutstandingWrites(v_stack_m70, a2, 64, (unsigned int)(v_stack_p20));
    if (condition_is_not_equal) goto loc_002B5111;
    result = v_stack_mC8 + 152;
    if ((*(unsigned __int64 *)(v_stack_mC8 + 152)) != (v_stack_mC8 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_m70, a2, 64, (unsigned int)(v_stack_p20));
    }
    result = KeLeaveCriticalRegionThread(v_stack_mC8, a2, 64, (unsigned int)(v_stack_p20));
    if (*(unsigned __int64 *)(v_stack_mC0) == 0) goto loc_002B5156;
    result = ExAcquireSpinLockExclusive(v_stack_mF0 + 200, a2, 64, (unsigned int)(v_stack_p20));
    result = MiReleaseSpinLockExclusive(v_stack_mF0 + 200, (unsigned __int8)(result), 64, (unsigned int)(v_stack_p20));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC0)))) == 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_stack_mC0);
        result = ExFreePoolWithTag(a1, a2, 64, (unsigned int)(v_stack_p20));
    }
    if (v_stack_mE0 != 0) goto loc_002B5360;
loc_002B5162:
loc_002B5165:
    v_rsp = (v_rsp) + (256);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000429ULL)));
loc_002B5181:
    result = (unsigned int)(v_stack_p3C);
    if (((unsigned int)(v_stack_p10)) == 0xC000009AULL) { result = 0; }
    a1 = (unsigned int)((a1) & (7));
    v_stack_p3C = (unsigned int)(result);
    v_rsi = (*(unsigned __int64 *)(v_stack_mC0)) >> (3);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(*(unsigned __int64 *)(1 + 1416) + 8));
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rsi)));
    result = MiTransferSoftwarePte(*(unsigned __int64 *)(v_rip - 2771263), v_stack_p48, (unsigned int)((unsigned int)(v_r10)), 0);
    result = MiReleasePageFileInfo(1, result, 3, 0);
    result = MiStoreFreeWriteSupport(*(unsigned __int64 *)((unsigned int)(0xC0000429ULL) + 48), 1, 3, 0);
    result = MiStoreLogWriteIssueFailure((unsigned int)((unsigned int)(v_stack_p10)), (unsigned int)(0xC0000429ULL) + 8, (unsigned int)(*(unsigned int *)((unsigned int)(0xC0000429ULL) + 4)), (unsigned int)(*(unsigned int *)(1 + 1224)));
    goto loc_002B4DCE;
loc_002B520F:
    result = (unsigned int)(((unsigned int)(v_stack_p34)) + (v_stack_p38));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(v_stack_p40)))) goto loc_002B5399;
    if ((*(unsigned __int64 *)(v_stack_p48 + 184)) != 0) goto loc_002B5399;
loc_002B5243:
    result = MiStoreModifiedWriteDereference(v_stack_p8, 1, (unsigned int)(*(unsigned int *)((unsigned int)(0xC0000429ULL) + 4)), (unsigned int)(*(unsigned int *)(1 + 1224)));
loc_002B5251:
    goto loc_002B5111;
loc_002B525C:
    a2 = (unsigned int)((v_stack_mA8) + (259));
    result = MiUpdatePageFileHighInPte(v_stack_p10, a2, (unsigned int)(*(unsigned int *)((unsigned int)(0xC0000429ULL) + 4)), (unsigned int)(*(unsigned int *)(1 + 1224)));
    result = MiReleasePageFileInfo(1, result, 2, (unsigned int)(*(unsigned int *)(1 + 1224)));
    *(unsigned __int64 *)(v_stack_mA0 + v_stack_mF0 * 8 + 96) = *(unsigned __int64 *)(v_rip - 2771462);
    goto loc_002B5059;
loc_002B5290:
    v_stack_p28 = 0x40000020ULL;
    v_stack_p20 = 259;
    a4 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(v_rsi, a2, 1, a4);
    goto loc_002B4802;
loc_002B52B5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13703165)))) & (64)) == 0) goto loc_002B4F32;
    result = KiCheckVpBackingLongSpinWaitHypercall(result, a2, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002B4F32;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(result)), a2, 1, a4);
    goto loc_002B4F34;
loc_002B52DC:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), (unsigned __int8)(v_stack_mF0), 1, a4);
    goto loc_002B4F9E;
loc_002B52EB:
    if ((unsigned __int8)(result) != 0) goto loc_002B5303;
    if ((*(unsigned __int64 *)(v_stack_mA0 + 152)) != (v_stack_mA0 + 152)) goto loc_002B537F;
loc_002B5303:
    goto loc_002B5251;
loc_002B530E:
    a1 = (unsigned int)(((unsigned __int8)(result)) + ((unsigned int)(result)));
    v_stack_p38 = (unsigned int)(a1);
    goto loc_002B4BE4;
loc_002B5319:
    v_r12 = (unsigned int)((v_stack_p8) | (0xFFFFFFFFULL));
loc_002B531D:
loc_002B5320:
    v_r11 = 0;
    if (0 == 0) goto loc_002B4FE2;
    a2 = v_rsi + 1;
    if (((unsigned int)(v_rsi + 1)) > ((unsigned int)(v_stack_mF0))) { a2 = (unsigned int)(v_stack_mF0); }
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r12)));
    goto loc_002B4EB8;
loc_002B533F:
    result = MiStoreLogWriteDisabled((unsigned int)(*(unsigned int *)(1 + 1220)), a2, 1, 0);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 1220))) - 1);
    *(unsigned int *)(1 + 1220) = (unsigned int)(result);
    goto loc_002B50B4;
loc_002B5360:
    if (((*(unsigned __int8 *)(v_stack_m68 + 10)) & (1)) == 0) goto loc_002B5162;
    result = MmUnmapLockedPages(*(unsigned __int64 *)(v_stack_m68 + 24), v_stack_m68, 1, 0);
    goto loc_002B5162;
loc_002B537F:
    result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(v_stack_m68 + 24), v_stack_m68, 1, 0);
    goto loc_002B5303;
loc_002B5389:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_r12), (unsigned __int8)(v_stack_mF0), 1, 0);
    goto loc_002B4CC2;
loc_002B5399:
    result = MiStoreUpdatePagefileHash((unsigned __int8)(v_r12), v_r12, v_r12 + 104, (unsigned int)((unsigned int)((unsigned __int8)(v_r12))));
    goto loc_002B5243;
loc_002B53AE:
    goto loc_002B50D9;
loc_002B53B9:
    result = MiStoreExtendVirtualPagefile(1, v_stack_mF0, v_r12 + 104, (unsigned int)((unsigned int)((unsigned __int8)(v_r12))));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 12))) != 0) goto loc_002B542B;
    result = MiStoreLogFullPagefile(1, v_stack_mF0, v_r12 + 104, (unsigned int)((unsigned int)((unsigned __int8)(v_r12))));
    goto loc_002B5165;
loc_002B53DA:
    if ((*(unsigned int *)(1)) != 0) goto loc_002B4C50;
    if (1 == 0) goto loc_002B4C50;
    a2 = 0;
    result = ExFreePoolWithTag(1, a2, v_r12 + 104, (unsigned int)((unsigned int)((unsigned __int8)(v_r12))));
    goto loc_002B4C50;
loc_002B53FA:
    a1 = 0;
    result = MiMakePageFilePte(a1, a2, v_r12 + 104, (unsigned int)((unsigned int)((unsigned __int8)(v_r12))));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8 + 64) + 172)) & (64)) == 0) goto loc_002B5434;
    result = MiSetStoreVirtualPagefileValue(1, result, 4, (unsigned int)((unsigned int)((unsigned __int8)(v_r12))));
loc_002B5423:
    v_r11 = 0;
    goto loc_002B49B3;
loc_002B542B:
    goto loc_002B4758;
loc_002B5434:
    a3 = (unsigned int)((v_stack_mA8) + ((unsigned int)(v_stack_mF0)));
    result = MiTransferSoftwarePte(result, (unsigned int)(v_stack_p40), a3, 1);
    goto loc_002B5423;
loc_002B544B:
    v_stack_p3C = 1;
loc_002B5454:
loc_002B545E:
    result = MiIsStoreVirtualPagefileFull(1, (unsigned int)(v_stack_p40), v_stack_p50, 1);
    if ((unsigned int)(result) == 0) goto loc_002B4B87;
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(1 + 928, a2, a3, 1);
    goto loc_002B4B87;
loc_002B5484:
    v_stack_mC0 = v_stack_mC0;
    v_stack_p50 = v_stack_p50;
    v_stack_p30 = 0;
    v_stack_p38 = (unsigned int)(1 + 928);
loc_002B54A3:
    *(unsigned int *)(1 + 1220) = 32;
    goto loc_002B4E17;
}
```

## 5. (Beta) C Style

```c
int64_t MiStoreWriteModifiedPages(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint8_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint32_t v_stack_p3C;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (256);
    local_r14 = 0;
    v_stack_m68 = Arg1 + 104;
    v_stack_mD8 = 0;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x68 + 0x28))) >> (12));
    v_stack_m88 = v_xmm0;
    v_stack_mB0 = 0;
    v_stack_m70 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8);
    v_stack_mF8 = Arg2;
    v_stack_m58 = v_xmm1;
    v_stack_m48 = v_xmm0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4C4))) != 0) goto loc_002B533F;
    v_stack_mF0 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4B4)) * 8 + 0x4860);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4B4)) * 8 + 0x4860) + 0xC)))) < Arg2) goto loc_002B53B9;
loc_002B4758:
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_002B4770;
    if ((*(uint16_t *)(v_rip + 0xD10896)) > 1) goto loc_002B5065;
loc_002B4770:
    v_stack_mC8 = *(uint64_t *)(arg1 + 0x48);
    if (*(uint64_t *)(arg1 + 0x48) == 0) goto loc_002B5076;
loc_002B4782:
    v_stack_mC0 = v_stack_m60;
    result = (v_stack_m60) | (-1);
    v_stack_m60 = 0;
    v_stack_mE8 = 0;
    v_stack_mE0 = 0;
    v_stack_mA0 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x518)) != 0) goto loc_002B52EB;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x518)) != 0) goto loc_002B47F4;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(result + 2, Arg2, a3, a4);
        Arg1 = 1;
    }
    if (((*(uint8_t *)(arg1 + 0x68 + 0xA)) & (5)) == 0) goto loc_002B5290;
loc_002B4802:
    local_r11 = 0;
    v_stack_mE0 = *(uint64_t *)(arg1 + 0x68 + 0x18);
    if (*(uint64_t *)(arg1 + 0x68 + 0x18) == 0) goto loc_002B53AE;
    v_stack_mFC = 0;
    v_stack_p20 = 0;
    v_stack_m100 = 0;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x58) = (uint32_t)((uint32_t)(v_stack_mF8) + 1);
    v_stack_mD0 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590);
    local_r10 = (*(uint64_t *)(arg1 + 0x58)) >> (12);
    v_stack_m90 = Arg1 + 152;
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4B4)) * 8 + 0x4860) + 0x58)));
    v_stack_mA8 = local_r10;
loc_002B4867:
    v_stack_m98 = Arg1 + 152;
    v_stack_m104 = 0;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_mF8)))) goto loc_002B4C70;
    if ((*(uint64_t *)(arg1 + 0x98)) == (*(uint64_t *)(v_rip + 0xB82BE6))) goto loc_002B530E;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0xC))) == 0) goto loc_002B4C1D;
    if (v_stack_m60 != (*(uint64_t *)(v_stack_mF0 + 0x50))) goto loc_002B4C47;
loc_002B48B6:
    a3 = (uint32_t)((2) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4B4)) * 8 + 0x4860) + 0x58)))));
    Arg1 = (uint32_t)((v_stack_m50) & (4));
    result = -((uint32_t)((uint32_t)(Arg1)));
    local_r10 = (uint32_t)((local_r10) & (32));
    Arg1 = -(Arg1);
    result = (uint32_t)((result) & (4));
    a4 = (v_stack_m50) - (result);
loc_002B48EB:
    v_stack_mB8 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r10 + (uint32_t)(v_stack_m58) - 1 * 1))) - ((uint32_t)(local_r10 + a3 * 1)));
    result = (uint32_t)((result) + (1));
    if (((uint32_t)(result)) < 1) goto loc_002B4C25;
    Arg1 = (uint8_t)((local_r10 + a3 * 1) & (63));
    Arg2 = ((uint32_t)((uint32_t)(local_r10 + a3 * 1))) >> (6);
    result = ((uint32_t)((uint32_t)(local_r10 + (uint32_t)(v_stack_m58) - 1 * 1))) >> (6);
    result = (1) << ((uint8_t)(Arg1));
    result = (result) - (1);
    Arg1 = (*(uint64_t *)(a4 + Arg2 * 8)) | (result);
loc_002B4931:
    if (Arg1 != -1) goto loc_002B4949;
    local_rbx = (a4 + Arg2 * 8) + (8);
    if (local_rbx > (a4 + result * 8)) goto loc_002B4C25;
    goto loc_002B4931;
loc_002B4949:
    local_rbx = (local_rbx) - (a4);
    Arg1 = ~(*(uint64_t *)(local_rbx));
    local_rbx = (local_rbx) >> (3);
    local_rbx = (uint32_t)((local_rbx) << (6));
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(result)));
    v_stack_mB8 = (uint32_t)(result);
    if (((uint32_t)(local_rbx)) > ((uint32_t)(local_r10 + (uint32_t)(v_stack_m58) - 1 * 1))) goto loc_002B4C25;
    if (((uint32_t)(local_rbx)) == -1) goto loc_002B4C28;
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(local_r10)));
loc_002B4974:
loc_002B4978:
    local_r12 = (*(uint64_t *)(arg1 + 0x98) + *(uint64_t *)(arg1 + 0x98) * 2) << (4);
    result = MiLockPageInline(local_r12 + result * 1, Arg2, a3, a4);
    result = MiIsPfnOriginalPteLost(local_r12 + result * 1, Arg2, a3, a4);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_002B53FA;
loc_002B49B3:
    *(uint64_t *)(v_stack_mC8 + (uint32_t)(v_stack_m104) * 8 + 0x60) = *(uint64_t *)(local_r12 + result * 1 + 0x10);
    if (((uint32_t)(local_rbx)) == -1) goto loc_002B4BC8;
    if (((uint32_t)(local_rbx)) < -1) goto loc_002B4BC8;
    v_stack_mB0 = 0;
    v_stack_m118 = v_stack_mB0;
    result = MiStoreCheckCandidatePage(local_r12 + result * 1, (uint32_t)((uint32_t)(local_rbx)), v_stack_mD8, v_stack_m88);
    local_r11 = 0;
    if (sign_flag) goto loc_002B4BBC;
    if (((v_stack_m80) & ((uint8_t)(local_r11 + 3))) != 0) goto loc_002B4A49;
loc_002B4A14:
    if (*(uint64_t *)(v_stack_m88 - 0x30) == 0) goto loc_002B4BC8;
    if (*(uint64_t *)(v_stack_m88 - 0x30) != 0) goto loc_002B4A14;
    result = ObpTraceObjectReferenceIfActive(v_stack_m88 - 48, 1, (uint32_t)(0x66506D4DULL), v_stack_m88);
    local_r11 = 0;
    v_stack_mE8 = v_stack_m88;
loc_002B4A49:
    if (((uint8_t)((uint8_t)(result))) >= 2) goto loc_002B4A77;
    result = v_stack_m88;
    if ((*(uint32_t *)(v_rip + 0xD122BB)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(0x66506D4DULL), v_stack_m88);
    }
loc_002B4A77:
    result = MiStoreGetWriteSupport(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8), Arg2, (uint32_t)(0x66506D4DULL), v_stack_m88);
    local_r11 = 0;
    if (result == 0) goto loc_002B544B;
    *(uint64_t *)(result + 0x18) = v_stack_mE8;
    *(uint64_t *)(result + 0x20) = 0;
    *(uint32_t *)(result + 0x20 + 0x8) = 56;
    *(uint64_t *)(result + 0x20 + 0x20) = 0;
    *(uint64_t *)(result + 0x20 + 0x28) = 0x1000ULL;
    *(uint64_t *)(result + 0x38) = v_stack_mE0;
    local_r12 = (local_r12) >> (4);
    local_r12 = (local_r12) * (local_r11 + 3);
    *(uint64_t *)(result) = v_stack_p8;
    *(uint64_t *)(result + 0x50) = local_r12;
    *(uint32_t *)(v_stack_mD0 + 0x18) = (uint32_t)((uint32_t)(v_stack_m104));
    *(uint32_t *)(v_stack_mD0 + 0x4) = (uint32_t)((uint32_t)(v_stack_mD8));
    *(uint64_t *)(v_stack_mD0 + 0x20) = v_stack_mB0;
    *(uint64_t *)(v_stack_mD0 + 0x28) = result + 32;
    *(uint64_t *)(v_stack_mD0 + 0x38) = result + 8;
    v_stack_mE8 = 0;
    *(uint64_t *)(v_stack_mD0 + 0x8) = v_xmm0;
    *(uint64_t *)(v_stack_mD0 + 0x30) = result;
    result = ExAcquireSpinLockExclusive(v_stack_mF0 + 200, result, v_stack_mD0, v_stack_m88);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (7));
    a4 = ((uint32_t)((uint32_t)(local_rbx))) >> (3);
    a4 = (a4) + (*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x50) + 0x10));
    v_stack_m108 = (uint32_t)(local_rbx + 1);
    *(uint8_t *)(a4) = (uint8_t)((int8_t)(*(uint8_t *)(a4)));
    *(uint32_t *)(v_stack_mF0 + 0x58) = (uint32_t)(local_rbx + 1);
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0xC))) - 1);
    *(uint32_t *)(v_stack_mF0 + 0xC) = (uint32_t)(local_rbx);
    result = MiUpdatePagefilePeakUsage(v_stack_mF0, Arg2, (int8_t)(*(uint8_t *)(a4)), a4);
    result = MiReleaseSpinLockExclusive(v_stack_mF0 + 200, (uint8_t)((uint8_t)(result)), (int8_t)(*(uint8_t *)(a4)), a4);
    if ((uint32_t)(local_rbx) == 0) goto loc_002B545E;
loc_002B4B87:
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m104)) + (1));
    result = (v_stack_m98) + (8);
    local_r11 = 0;
    goto loc_002B4867;
loc_002B4BBC:
    result = MiStoreLogNotCandidate((uint32_t)((uint32_t)(result)), 1, (int8_t)(*(uint8_t *)(a4)), (uint32_t)(v_stack_p20));
    local_r11 = 0;
loc_002B4BC8:
loc_002B4BE4:
    if (17 == 17) goto loc_002B5484;
    if (17 >= 2) goto loc_002B4C15;
    if ((*(uint32_t *)(v_rip + 0xD12121)) != 0) {
        Arg1 = (uint8_t)(result);
        Arg2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 2, (uint32_t)(v_stack_p20));
    }
loc_002B4C15:
    goto loc_002B5454;
loc_002B4C1D:
    local_rbx = (uint32_t)((2 - 1) | (0xFFFFFFFFULL));
    goto loc_002B4978;
loc_002B4C25:
    local_rbx = (uint32_t)((local_rbx) | (0xFFFFFFFFULL));
loc_002B4C28:
    local_r11 = 0;
    if (2 == 0) goto loc_002B4974;
    Arg2 = local_r12 + result * 1 + 1;
    if (((uint32_t)(local_r12 + result * 1 + 1)) > ((uint32_t)(local_rdi))) { Arg2 = (uint32_t)(local_rdi); }
    Arg2 = (uint32_t)((Arg2) - 1);
    goto loc_002B48EB;
loc_002B4C47:
    if (Arg1 != NULL) goto loc_002B53DA;
loc_002B4C50:
    result = MiRefPageFileSpaceBitmaps(local_rbx, v_stack_m60, 0, (uint32_t)(v_stack_p20));
    v_stack_mC0 = v_stack_m60;
    local_r11 = 0;
    goto loc_002B48B6;
loc_002B4C70:
    a3 = (v_stack_mD0) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590));
    a3 = (a3) >> (6);
    v_stack_m104 = 0;
    if ((uint32_t)(a3) == 0) goto loc_002B4E0C;
    result = SmPageWrite(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0xB8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590), a3, (uint32_t)(v_stack_p20));
    if ((*(uint32_t *)(v_rip + 0xD12064)) != 0) goto loc_002B5389;
loc_002B4CC2:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590)) >= v_stack_mD0) goto loc_002B4DE5;
loc_002B4CDC:
    local_r13 = (uint32_t)(((uint32_t)(v_stack_m108)) + (1));
    if ((((uint8_t)(local_r13)) & (15)) == 0) goto loc_002B4F59;
loc_002B4CE9:
    local_rdi = (*(uint64_t *)(v_stack_m90 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590) + 0x18)) * 8) + *(uint64_t *)(v_stack_m90 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590) + 0x18)) * 8) * 2) << (4);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_stack_m90 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590) + 0x18)) * 8));
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590) + 0x4)));
    if (sign_flag) goto loc_002B5181;
    local_rbx = 0;
loc_002B4D29:
    if (condition_is_below) goto loc_002B4F23;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(v_stack_mC8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590) + 0x18)))) * 8 + 0x60))) >> (2));
    if ((((uint8_t)(local_rbx + 1)) & ((uint8_t)(result))) != 0) goto loc_002B4FA3;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(v_stack_mC8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590) + 0x18)))) * 8 + 0x60))) >> (1));
    result = (uint8_t)((result) & ((uint8_t)(local_rbx + 1)));
    result = (uint8_t)(-(result));
    local_rbx = (*(uint64_t *)(v_stack_mC8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590) + 0x18)))) * 8 + 0x60)) & (result);
loc_002B4D5F:
    result = MiClearPageFileReservation(v_stack_mC8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590) + 0x18)))) * 8 + 96, 1, a3, (uint32_t)(v_stack_p20));
    result = MiTransferSoftwarePte(*(uint64_t *)(v_stack_mC8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590) + 0x18)))) * 8 + 0x60), v_stack_mF0, (uint32_t)(v_stack_m108), (uint32_t)((uint32_t)(local_rbx + 1)));
    *(uint64_t *)(v_stack_mC8 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590) + 0x18)))) * 8 + 0x60) = result;
    result = MiIsPfnOriginalPteLost(local_rdi, v_stack_mF0, (uint32_t)(v_stack_m108), (uint32_t)((uint32_t)(local_rbx + 1)));
    if ((uint32_t)(result) == 0) {
        Arg1 = local_rdi + 16;
        result = MiClearPageFileReservation(Arg1, v_stack_mF0, (uint32_t)(v_stack_m108), (uint32_t)((uint32_t)(local_rbx + 1)));
        a3 = v_stack_m108;
        Arg1 = local_rdi;
        Arg2 = v_stack_mF0;
        result = MiUpdatePfnBackingStore(Arg1, Arg2, a3, (uint32_t)((uint32_t)(local_rbx + 1)));
    }
    if (local_rbx != 0) goto loc_002B4F43;
loc_002B4DC5:
loc_002B4DCE:
    local_r14 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590)) + (64);
    if (local_r14 < v_stack_mD0) goto loc_002B4CDC;
loc_002B4DE5:
    local_r11 = 0;
    if ((*(uint32_t *)(v_rip + 0xD11F31)) != 0) {
        Arg1 = 2;
        Arg2 = 17;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, a3, (uint32_t)((uint32_t)(local_rbx + 1)));
        local_r11 = 0;
    }
loc_002B4E0C:
    if (v_stack_mFC != 0) goto loc_002B54A3;
loc_002B4E17:
    result = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)(v_stack_p20)))));
    if (((uint32_t)((uint32_t)(v_stack_p20))) == ((uint32_t)((uint32_t)(v_stack_mF8)))) goto loc_002B50BE;
    local_r12 = (uint32_t)((17) | (0xFFFFFFFFULL));
    v_stack_mE0 = 0;
    result = v_stack_p8;
    local_rbx = *(uint64_t *)(v_rip - 0x2A45C0);
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_p8 + 0x40) + 0xAC)) & (64)) == 0) {
        a3 = v_stack_mA8;
        a4 = 1;
        Arg1 = *(uint64_t *)(v_rip - 0x2A45C0);
        result = MiTransferSoftwarePte(Arg1, *(uint64_t *)(v_stack_p8 + 0x40), a3, a4);
        a4 = v_stack_p20;
        local_rbx = result;
        local_r11 = 0;
    }
loc_002B4E75:
    if ((uint32_t)(a4) == 0) goto loc_002B520F;
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x588) + 0x8)) & (4));
    result = -((uint32_t)((uint32_t)(Arg1)));
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x590) + 0x4))) & (32));
    Arg1 = -(Arg1);
    result = (uint32_t)((result) & (4));
    a3 = (*(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x588) + 0x8)) - (result);
    a4 = (uint32_t)((a4) & ((uint32_t)((uint32_t)((uint32_t)(local_r12)) + 1)));
loc_002B4EB8:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r10 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m70 + 0x588))) - 1 * 1))) - ((uint32_t)(local_r10 + a4 * 1)));
    result = (uint32_t)((result) + (1));
    if (((uint32_t)(result)) < 1) goto loc_002B531D;
    result = ((uint32_t)((uint32_t)(local_r10 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m70 + 0x588))) - 1 * 1))) >> (6);
    result = ((uint32_t)((uint32_t)(local_r10 + a4 * 1))) >> (6);
    Arg1 = (uint8_t)((local_r10 + a4 * 1) & (63));
    Arg2 = (1) << ((uint8_t)(Arg1));
    Arg2 = (Arg2) - (1);
    result = ~(*(uint64_t *)(a3 + result * 8));
    Arg2 = (Arg2) | (result);
    result = (result) | (-1);
loc_002B4F05:
    if (Arg2 != result) goto loc_002B4FB4;
    local_r14 = (a3 + result * 8) + (8);
    if (local_r14 > (a3 + result * 8)) goto loc_002B5319;
    Arg2 = ~(*(uint64_t *)(local_r14));
    goto loc_002B4F05;
loc_002B4F23:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(v_stack_m70)));
    if (((*(uint32_t *)(v_rip + 0xD10380)) & ((uint32_t)(local_rbx))) == 0) goto loc_002B52B5;
loc_002B4F32:
loc_002B4F34:
    if (!sign_flag) goto loc_002B4D29;
    goto loc_002B4F23;
loc_002B4F43:
    result = MiReleasePageFileInfo(v_stack_m70, local_rbx, 3, a4);
    goto loc_002B4DC5;
loc_002B4F59:
    result = KeShouldYieldProcessor(v_stack_m70, local_rbx, 3, a4);
    if ((uint32_t)(result) != 0) goto loc_002B4F6C;
loc_002B4F62:
    goto loc_002B4CE9;
loc_002B4F6C:
    if ((*(uint32_t *)(v_rip + 0xD11DAD)) != 0) {
        Arg1 = 17;
        Arg2 = (uint8_t)(a3 + result * 8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 3, a4);
    }
    if ((*(uint32_t *)(v_rip + 0xD11D88)) != 0) goto loc_002B52DC;
loc_002B4F9E:
    goto loc_002B4F62;
loc_002B4FA3:
    result = (*(uint64_t *)((uint32_t)((uint32_t)(local_r12)) + 0x1 + 0x60)) & (-5);
    *(uint64_t *)((uint32_t)((uint32_t)(local_r12)) + 0x1 + 0x60) = result;
    goto loc_002B4D5F;
loc_002B4FB4:
    local_r14 = (local_r14) - (3);
    Arg2 = ~(Arg2);
    local_r14 = (local_r14) >> (3);
    local_r12 = (uint32_t)(((uint8_t)((uint8_t)(a3 + result * 8))) | (0xFFFFFFFFULL));
    local_r14 = (uint32_t)((local_r14) << (6));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(result)));
    if (((uint32_t)(local_r14)) > ((uint32_t)(local_r10 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m70 + 0x588))) - 1 * 1))) goto loc_002B531D;
    if (((uint32_t)(local_r14)) == ((uint32_t)(local_r12))) goto loc_002B5320;
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)(local_r10)));
loc_002B4FE2:
    Arg2 = ((uint32_t)((uint32_t)(local_r14))) >> (3);
    Arg2 = (Arg2) + (*(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x588) + 0x8));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (7));
    *(uint8_t *)(Arg2) = (uint8_t)((int8_t)(*(uint8_t *)(Arg2)));
    if ((*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)(local_r14)) * 8)) == (*(uint64_t *)(v_rip + 0xB82460))) goto loc_002B525C;
    local_rsi = (*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)(local_r14)) * 8) + *(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)(local_r14)) * 8) * 2) << (4);
    local_rsi = (local_rsi) + (*(uint64_t *)(v_stack_m90 + (uint32_t)((uint32_t)(local_r14)) * 8));
    result = MiLockPageInline(local_rsi, Arg2, 3, a4);
    result = MiSetPfnModified(local_rsi, 1, 3, a4);
    result = MiUnlockPage(local_rsi, (uint8_t)((uint8_t)(result)), 3, a4);
loc_002B5059:
    local_r11 = 0;
    goto loc_002B4E75;
loc_002B5065:
    if (((uint32_t)((uint8_t)((uint8_t)(result)))) != (*(uint32_t *)(v_rip + 0xD101A1))) goto loc_002B4770;
loc_002B5076:
    result = MiAllocatePool(64, (uint32_t)(*(uint32_t *)(v_rip + 0xD10190)) * 8 + 96, (uint32_t)(0x77536D4DULL), (uint32_t)(v_stack_p20));
    v_stack_mC8 = result;
    *(uint64_t *)(local_r12 + 0x48) = result;
    if (result != 0) goto loc_002B4782;
    *(uint32_t *)(v_stack_m70 + 0x4C4) = 32;
loc_002B50B4:
    goto loc_002B5165;
loc_002B50BE:
    Arg2 = 0;
    result = RtlClearBits(*(uint64_t *)(v_stack_m70 + 0x588), Arg2, 64, (uint32_t)(v_stack_p20));
loc_002B50D9:
    result = (result) | (-1);
    result = MiStoreDecrementOutstandingWrites(v_stack_m70, Arg2, 64, (uint32_t)(v_stack_p20));
    if (condition_is_not_equal) goto loc_002B5111;
    result = v_stack_mC8 + 152;
    if ((*(uint64_t *)(v_stack_mC8 + 0x98)) != (v_stack_mC8 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_m70, Arg2, 64, (uint32_t)(v_stack_p20));
    }
    result = KeLeaveCriticalRegionThread(v_stack_mC8, Arg2, 64, (uint32_t)(v_stack_p20));
    if (*(uint64_t *)(v_stack_mC0) == 0) goto loc_002B5156;
    result = ExAcquireSpinLockExclusive(v_stack_mF0 + 200, Arg2, 64, (uint32_t)(v_stack_p20));
    result = MiReleaseSpinLockExclusive(v_stack_mF0 + 200, (uint8_t)(result), 64, (uint32_t)(v_stack_p20));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC0)))) == 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_stack_mC0);
        result = ExFreePoolWithTag(Arg1, Arg2, 64, (uint32_t)(v_stack_p20));
    }
    if (v_stack_mE0 != 0) goto loc_002B5360;
loc_002B5162:
loc_002B5165:
    local_rsp = (local_rsp) + (256);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000429ULL)));
loc_002B5181:
    result = (uint32_t)(v_stack_p3C);
    if (((uint32_t)(v_stack_p10)) == 0xC000009AULL) { result = 0; }
    Arg1 = (uint32_t)((Arg1) & (7));
    v_stack_p3C = (uint32_t)(result);
    local_rsi = (*(uint64_t *)(v_stack_mC0)) >> (3);
    local_rsi = (local_rsi) + (*(uint64_t *)(*(uint64_t *)(1 + 0x588) + 0x8));
    *(uint8_t *)(local_rsi) = (uint8_t)((int8_t)(*(uint8_t *)(local_rsi)));
    result = MiTransferSoftwarePte(*(uint64_t *)(v_rip - 0x2A493F), v_stack_p48, (uint32_t)((uint32_t)(local_r10)), 0);
    result = MiReleasePageFileInfo(1, result, 3, 0);
    result = MiStoreFreeWriteSupport(*(uint64_t *)((uint32_t)(0xC0000429ULL) + 0x30), 1, 3, 0);
    result = MiStoreLogWriteIssueFailure((uint32_t)((uint32_t)(v_stack_p10)), (uint32_t)(0xC0000429ULL) + 8, (uint32_t)(*(uint32_t *)((uint32_t)(0xC0000429ULL) + 0x4)), (uint32_t)(*(uint32_t *)(1 + 0x4C8)));
    goto loc_002B4DCE;
loc_002B520F:
    result = (uint32_t)(((uint32_t)(v_stack_p34)) + (v_stack_p38));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(v_stack_p40)))) goto loc_002B5399;
    if ((*(uint64_t *)(v_stack_p48 + 0xB8)) != 0) goto loc_002B5399;
loc_002B5243:
    result = MiStoreModifiedWriteDereference(v_stack_p8, 1, (uint32_t)(*(uint32_t *)((uint32_t)(0xC0000429ULL) + 0x4)), (uint32_t)(*(uint32_t *)(1 + 0x4C8)));
loc_002B5251:
    goto loc_002B5111;
loc_002B525C:
    Arg2 = (uint32_t)((v_stack_mA8) + (259));
    result = MiUpdatePageFileHighInPte(v_stack_p10, Arg2, (uint32_t)(*(uint32_t *)((uint32_t)(0xC0000429ULL) + 0x4)), (uint32_t)(*(uint32_t *)(1 + 0x4C8)));
    result = MiReleasePageFileInfo(1, result, 2, (uint32_t)(*(uint32_t *)(1 + 0x4C8)));
    *(uint64_t *)(v_stack_mA0 + v_stack_mF0 * 8 + 0x60) = *(uint64_t *)(v_rip - 0x2A4A06);
    goto loc_002B5059;
loc_002B5290:
    v_stack_p28 = 0x40000020ULL;
    v_stack_p20 = 259;
    a4 = 0;
    Arg2 = 0;
    result = MmMapLockedPagesSpecifyCache(local_rsi, Arg2, 1, a4);
    goto loc_002B4802;
loc_002B52B5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD117FD)))) & (64)) == 0) goto loc_002B4F32;
    result = KiCheckVpBackingLongSpinWaitHypercall(result, Arg2, 1, a4);
    if ((uint8_t)(result) == 0) goto loc_002B4F32;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(result)), Arg2, 1, a4);
    goto loc_002B4F34;
loc_002B52DC:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), (uint8_t)(v_stack_mF0), 1, a4);
    goto loc_002B4F9E;
loc_002B52EB:
    if ((uint8_t)(result) != 0) goto loc_002B5303;
    if ((*(uint64_t *)(v_stack_mA0 + 0x98)) != (v_stack_mA0 + 152)) goto loc_002B537F;
loc_002B5303:
    goto loc_002B5251;
loc_002B530E:
    Arg1 = (uint32_t)(((uint8_t)(result)) + ((uint32_t)(result)));
    v_stack_p38 = (uint32_t)(Arg1);
    goto loc_002B4BE4;
loc_002B5319:
    local_r12 = (uint32_t)((v_stack_p8) | (0xFFFFFFFFULL));
loc_002B531D:
loc_002B5320:
    local_r11 = 0;
    if (0 == 0) goto loc_002B4FE2;
    Arg2 = local_rsi + 1;
    if (((uint32_t)(local_rsi + 1)) > ((uint32_t)(v_stack_mF0))) { Arg2 = (uint32_t)(v_stack_mF0); }
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12)));
    goto loc_002B4EB8;
loc_002B533F:
    result = MiStoreLogWriteDisabled((uint32_t)(*(uint32_t *)(1 + 0x4C4)), Arg2, 1, 0);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x4C4))) - 1);
    *(uint32_t *)(1 + 0x4C4) = (uint32_t)(result);
    goto loc_002B50B4;
loc_002B5360:
    if (((*(uint8_t *)(v_stack_m68 + 0xA)) & (1)) == 0) goto loc_002B5162;
    result = MmUnmapLockedPages(*(uint64_t *)(v_stack_m68 + 0x18), v_stack_m68, 1, 0);
    goto loc_002B5162;
loc_002B537F:
    result = KiCheckForKernelApcDelivery(*(uint64_t *)(v_stack_m68 + 0x18), v_stack_m68, 1, 0);
    goto loc_002B5303;
loc_002B5389:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_r12), (uint8_t)(v_stack_mF0), 1, 0);
    goto loc_002B4CC2;
loc_002B5399:
    result = MiStoreUpdatePagefileHash((uint8_t)(local_r12), local_r12, local_r12 + 104, (uint32_t)((uint32_t)((uint8_t)(local_r12))));
    goto loc_002B5243;
loc_002B53AE:
    goto loc_002B50D9;
loc_002B53B9:
    result = MiStoreExtendVirtualPagefile(1, v_stack_mF0, local_r12 + 104, (uint32_t)((uint32_t)((uint8_t)(local_r12))));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0xC))) != 0) goto loc_002B542B;
    result = MiStoreLogFullPagefile(1, v_stack_mF0, local_r12 + 104, (uint32_t)((uint32_t)((uint8_t)(local_r12))));
    goto loc_002B5165;
loc_002B53DA:
    if ((*(uint32_t *)(1)) != 0) goto loc_002B4C50;
    if (1 == 0) goto loc_002B4C50;
    Arg2 = 0;
    result = ExFreePoolWithTag(1, Arg2, local_r12 + 104, (uint32_t)((uint32_t)((uint8_t)(local_r12))));
    goto loc_002B4C50;
loc_002B53FA:
    Arg1 = 0;
    result = MiMakePageFilePte(Arg1, Arg2, local_r12 + 104, (uint32_t)((uint32_t)((uint8_t)(local_r12))));
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_p8 + 0x40) + 0xAC)) & (64)) == 0) goto loc_002B5434;
    result = MiSetStoreVirtualPagefileValue(1, result, 4, (uint32_t)((uint32_t)((uint8_t)(local_r12))));
loc_002B5423:
    local_r11 = 0;
    goto loc_002B49B3;
loc_002B542B:
    goto loc_002B4758;
loc_002B5434:
    a3 = (uint32_t)((v_stack_mA8) + ((uint32_t)(v_stack_mF0)));
    result = MiTransferSoftwarePte(result, (uint32_t)(v_stack_p40), a3, 1);
    goto loc_002B5423;
loc_002B544B:
    v_stack_p3C = 1;
loc_002B5454:
loc_002B545E:
    result = MiIsStoreVirtualPagefileFull(1, (uint32_t)(v_stack_p40), v_stack_p50, 1);
    if ((uint32_t)(result) == 0) goto loc_002B4B87;
    a3 = 0;
    Arg2 = 0;
    result = KeSetEvent(1 + 928, Arg2, a3, 1);
    goto loc_002B4B87;
loc_002B5484:
    v_stack_mC0 = v_stack_mC0;
    v_stack_p50 = v_stack_p50;
    v_stack_p30 = 0;
    v_stack_p38 = (uint32_t)(1 + 928);
loc_002B54A3:
    *(uint32_t *)(1 + 0x4C4) = 32;
    goto loc_002B4E17;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xA` | `8` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `W` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B46C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
