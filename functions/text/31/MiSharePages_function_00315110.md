# MiSharePages

- RVA: `0x00315110`–`0x00316137` (길이 `4,135` bytes)
- VA: `0x0000000140315110`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074908`
- 디코드: `894`개 명령, `4,135/4,135` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **66**; 고유 호출 대상: **52**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x003151AD` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x003151FA` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0031520D` → [MiPrepareAttachThread](../2B/MiPrepareAttachThread_function_002B4650.md) (function, `0x002B4650`)
- `0x00315226` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0031525D` → [KiStackAttachProcess](../21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x003152C7` → [MiAllocateCombineBlock](MiAllocateCombineBlock_function_00317294.md) (function, `0x00317294`)
- `0x003152E5` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00315308` → [MiProcessSuitableForCombining](../2B/MiProcessSuitableForCombining_function_002B6294.md) (function, `0x002B6294`)
- `0x0031535C` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x003153E2` → [MiReplenishCombineResources](MiReplenishCombineResources_function_00316140.md) (function, `0x00316140`)
- `0x00315477` → [MiCombineCandidate](MiCombineCandidate_function_00316290.md) (function, `0x00316290`)
- `0x003154CA` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x00315582` → [MiGetWsleContents](MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x003155AA` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x003155B7` → [MiLocateAddress](MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x003155DD` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x0031560B` → [MiVadSupportsPrivateCommit](MiVadSupportsPrivateCommit_function_00316FD0.md) (function, `0x00316FD0`)
- `0x0031568F` → [MiCrcStillIntact](MiCrcStillIntact_function_00317028.md) (function, `0x00317028`)
- `0x003156D1` → [MiCrcStillIntact](MiCrcStillIntact_function_00317028.md) (function, `0x00317028`)
- `0x00315702` → [MiFlushTbList](MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00315707` → [MiReleaseProcessorFlushList](MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00315729` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00315736` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00315743` → [MiFreeDeferredCrcPages](MiFreeDeferredCrcPages_function_00315018.md) (function, `0x00315018`)
- `0x0031577D` → [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) (function, `0x00280D10`)
- `0x00315796` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x003157DD` → [MiPageMightBeZero](../45/MiPageMightBeZero_function_0045FEFC.md) (function, `0x0045FEFC`)
- `0x003157FC` → [MiConfirmPageIsZero](../33/MiConfirmPageIsZero_function_00334380.md) (function, `0x00334380`)
- `0x00315826` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x003158DE` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x003158EC` → [MiFreeWsleList](../24/MiFreeWsleList_function_00241168.md) (function, `0x00241168`)
- `0x003158F5` → [MiReleaseProcessorFlushList](MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x00315999` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x003159D3` → [KiLeaveCriticalRegionUnsafe](../25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x003159F4` → [KeForceDetachProcess](../3C/KeForceDetachProcess_function_003C7770.md) (function, `0x003C7770`)
- `0x00315A00` → [MiAttachThreadDone](../28/MiAttachThreadDone_function_0028F3E0.md) (function, `0x0028F3E0`)
- `0x00315A15` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)
- `0x00315A3C` → [MiFreeCombineBlock](../37/MiFreeCombineBlock_function_00372000.md) (function, `0x00372000`)
- `0x00315A66` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00315B10` → [MiGetUltraMapping](../32/MiGetUltraMapping_function_00323270.md) (function, `0x00323270`)
- `0x00315B41` → [MiGetUltraMapping](../32/MiGetUltraMapping_function_00323270.md) (function, `0x00323270`)
- `0x00315B78` → [MiConvertPrivateToProto](../22/MiConvertPrivateToProto_function_0022B0E4.md) (function, `0x0022B0E4`)
- `0x00315BEA` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x00315C8F` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x00315CB8` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x00315CE8` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00315CF5` → [KiLeaveCriticalRegionUnsafe](../25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00315D4E` → [MiConvertStandbyToProto](../22/MiConvertStandbyToProto_function_0022A330.md) (function, `0x0022A330`)
- `0x00315DA7` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00315DBD` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x00315E47` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00315EFB` → [MiGetCombineDomain](../46/MiGetCombineDomain_function_00465790.md) (function, `0x00465790`)
- `0x00315F1F` → [MiCheckProcessCombineSequence](../46/MiCheckProcessCombineSequence_function_004657A8.md) (function, `0x004657A8`)
- `0x00315F85` → [MiMakeCombineCandidateClean](../46/MiMakeCombineCandidateClean_function_00465170.md) (function, `0x00465170`)
- `0x00315FA1` → [MiFlushSingleTbEntry](../28/MiFlushSingleTbEntry_function_0028E730.md) (function, `0x0028E730`)
- `0x00315FB9` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00315FC8` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00315FF4` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00316003` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00316014` → [MiReplenishSlabAllocator](../37/MiReplenishSlabAllocator_function_003788E4.md) (function, `0x003788E4`)
- `0x00316032` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x00316070` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00316093` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003160A2` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003160EB` → [MiWorkingSetIsContended](../2A/MiWorkingSetIsContended_function_002AE520.md) (function, `0x002AE520`)
- `0x00316107` → [MiPageTableLockIsContended](../2A/MiPageTableLockIsContended_function_002AE650.md) (function, `0x002AE650`)

### Direct callers
- [MiProcessCrcList](../../page/9F/MiProcessCrcList_function_009F6F94.md) at `0x009F7469`

### Static image references
- `0x00315127` → RVA `0x00E0A740` (`.data`; read)
- `0x003151F3` → RVA `0x00E374C0` (`.data`; read)
- `0x00315410` → RVA `0x00E2DCE0` (`.data`; read)
- `0x003155EF` → RVA `0x00014578` (`.rdata`; read)
- `0x0031562F` → RVA `0x00E37468` (`.data`; read)
- `0x00315942` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00315A8F` → RVA `0x00E2FF10` (`.data`; read)
- `0x00315DC6` → RVA `0x00E2DC80` (`.data`; read)
- `0x00315E59` → RVA `0x00E30088` (`.data`; read)
- `0x00315FAB` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00315110  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00315115  55                              push rbp
00315116  56                              push rsi
00315117  57                              push rdi
00315118  41 54                           push r12
0031511A  41 55                           push r13
0031511C  41 56                           push r14
0031511E  41 57                           push r15
00315120  48 81 EC F0 01 00 00            sub rsp, 0x1f0
00315127  48 8B 05 12 56 AF 00            mov rax, qword ptr [rip + 0xaf5612]
0031512E  48 33 C4                        xor rax, rsp
00315131  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
00315139  48 8B 01                        mov rax, qword ptr [rcx]
0031513C  4C 8D 89 40 01 00 00            lea r9, [rcx + 0x140]
00315143  4C 8B 7A 20                     mov r15, qword ptr [rdx + 0x20]
00315147  33 FF                           xor edi, edi
00315149  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
00315151  0F 57 C0                        xorps xmm0, xmm0
00315154  8B 81 8C 00 00 00               mov eax, dword ptr [rcx + 0x8c]
0031515A  41 8B F0                        mov esi, r8d
0031515D  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00315164  48 8B DA                        mov rbx, rdx
00315167  48 8B 41 68                     mov rax, qword ptr [rcx + 0x68]
0031516B  8D 57 03                        lea edx, [rdi + 3]
0031516E  4C 8B F1                        mov r14, rcx
00315171  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00315176  49 8B CF                        mov rcx, r15
00315179  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00315181  41 FF C0                        inc r8d
00315184  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
00315188  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
00315190  48 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdi
00315198  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
003151A0  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
003151A5  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
003151AD  E8 5E B2 00 00                  call 0x140320410
003151B2  4C 8B 63 30                     mov r12, qword ptr [rbx + 0x30]
003151B6  8B EF                           mov ebp, edi
003151B8  89 BC 24 80 00 00 00            mov dword ptr [rsp + 0x80], edi
003151BF  44 8B EF                        mov r13d, edi
003151C2  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
003151C7  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
003151CC  48 8B 7B 28                     mov rdi, qword ptr [rbx + 0x28]
003151D0  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
003151D8  48 85 FF                        test rdi, rdi
003151DB  0F 84 81 00 00 00               je 0x140315262
003151E1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003151EA  48 3B B8 B8 00 00 00            cmp rdi, qword ptr [rax + 0xb8]
003151F1  74 6F                           je 0x140315262
003151F3  48 8D 0D C6 22 B2 00            lea rcx, [rip + 0xb222c6]
003151FA  E8 91 34 F3 FF                  call 0x140248690
003151FF  48 8D 97 00 04 00 00            lea rdx, [rdi + 0x400]
00315206  48 8B CF                        mov rcx, rdi
00315209  44 0F B6 C8                     movzx r9d, al
0031520D  E8 3E F4 F9 FF                  call 0x1402b4650
00315212  41 0F B6 D1                     movzx edx, r9b
00315216  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
0031521D  48 8D 0D 9C 22 B2 00            lea rcx, [rip + 0xb2229c]
00315224  8B D8                           mov ebx, eax
00315226  E8 95 30 F3 FF                  call 0x1402482c0
0031522B  85 DB                           test ebx, ebx
0031522D  0F 84 D2 07 00 00               je 0x140315a05
00315233  0F 57 C0                        xorps xmm0, xmm0
00315236  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
0031523E  41 8D 55 01                     lea edx, [r13 + 1]
00315242  48 8B CF                        mov rcx, rdi
00315245  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
0031524D  0F 11 84 24 20 01 00 00         movups xmmword ptr [rsp + 0x120], xmm0
00315255  0F 11 84 24 30 01 00 00         movups xmmword ptr [rsp + 0x130], xmm0
0031525D  E8 BE 15 F0 FF                  call 0x140216820
00315262  33 DB                           xor ebx, ebx
00315264  49 89 9E 38 01 00 00            mov qword ptr [r14 + 0x138], rbx
0031526B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00315274  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
0031527C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00315283  90                              nop
00315284  49 8B 8E 38 01 00 00            mov rcx, qword ptr [r14 + 0x138]
0031528B  48 89 9C 24 40 01 00 00         mov qword ptr [rsp + 0x140], rbx
00315293  48 89 9C 24 68 01 00 00         mov qword ptr [rsp + 0x168], rbx
0031529B  48 89 9C 24 90 01 00 00         mov qword ptr [rsp + 0x190], rbx
003152A3  48 89 9C 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], rbx
003152AB  48 83 F9 01                     cmp rcx, 1
003152AF  0F 87 58 0D 00 00               ja 0x14031600d
003152B5  49 83 BE 28 01 00 00 00         cmp qword ptr [r14 + 0x128], 0
003152BD  75 14                           jne 0x1403152d3
003152BF  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
003152C7  E8 C8 1F 00 00                  call 0x140317294
003152CC  49 89 86 28 01 00 00            mov qword ptr [r14 + 0x128], rax
003152D3  32 DB                           xor bl, bl
003152D5  48 C7 44 24 38 00 00 00 00      mov qword ptr [rsp + 0x38], 0
003152DE  49 8B CF                        mov rcx, r15
003152E1  88 5C 24 34                     mov byte ptr [rsp + 0x34], bl
003152E5  E8 06 79 F6 FF                  call 0x14027cbf0
003152EA  49 83 BE 28 01 00 00 00         cmp qword ptr [r14 + 0x128], 0
003152F2  44 0F B6 C0                     movzx r8d, al
003152F6  88 44 24 50                     mov byte ptr [rsp + 0x50], al
003152FA  0F 84 E1 09 00 00               je 0x140315ce1
00315300  48 85 FF                        test rdi, rdi
00315303  74 10                           je 0x140315315
00315305  48 8B CF                        mov rcx, rdi
00315308  E8 87 0F FA FF                  call 0x1402b6294
0031530D  85 C0                           test eax, eax
0031530F  0F 84 CC 09 00 00               je 0x140315ce1
00315315  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0031531A  8D 45 01                        lea eax, [rbp + 1]
0031531D  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
00315325  33 ED                           xor ebp, ebp
00315327  40 32 FF                        xor dil, dil
0031532A  84 DB                           test bl, bl
0031532C  0F 44 E8                        cmove ebp, eax
0031532F  49 83 BE 28 01 00 00 00         cmp qword ptr [r14 + 0x128], 0
00315337  89 6C 24 30                     mov dword ptr [rsp + 0x30], ebp
0031533B  74 28                           je 0x140315365
0031533D  49 83 BE 38 01 00 00 01         cmp qword ptr [r14 + 0x138], 1
00315345  77 1E                           ja 0x140315365
00315347  40 38 7C 24 34                  cmp byte ptr [rsp + 0x34], dil
0031534C  0F 85 1B 0A 00 00               jne 0x140315d6d
00315352  40 F6 C5 07                     test bpl, 7
00315356  0F 84 8A 0D 00 00               je 0x1403160e6
0031535C  E8 7F 20 F6 FF                  call 0x1402773e0
00315361  85 C0                           test eax, eax
00315363  74 03                           je 0x140315368
00315365  40 B7 01                        mov dil, 1
00315368  4D 85 E4                        test r12, r12
0031536B  0F 84 FB 02 00 00               je 0x14031566c
00315371  40 84 FF                        test dil, dil
00315374  0F 85 F6 02 00 00               jne 0x140315670
0031537A  49 8B 4C 24 10                  mov rcx, qword ptr [r12 + 0x10]
0031537F  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
00315389  49 8B 04 24                     mov rax, qword ptr [r12]
0031538D  4C 8B F9                        mov r15, rcx
00315390  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00315395  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
0031539A  49 C1 EF 09                     shr r15, 9
0031539E  4D 23 F8                        and r15, r8
003153A1  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
003153A9  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
003153B1  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
003153BB  48 8B C2                        mov rax, rdx
003153BE  4C 03 F8                        add r15, rax
003153C1  49 8B DF                        mov rbx, r15
003153C4  48 C1 EB 09                     shr rbx, 9
003153C8  49 23 D8                        and rbx, r8
003153CB  48 8B C2                        mov rax, rdx
003153CE  48 03 D8                        add rbx, rax
003153D1  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
003153D6  48 3B C3                        cmp rax, rbx
003153D9  0F 85 7F 03 00 00               jne 0x14031575e
003153DF  49 8B CE                        mov rcx, r14
003153E2  E8 59 0D 00 00                  call 0x140316140
003153E7  85 C0                           test eax, eax
003153E9  0F 88 D8 0A 00 00               js 0x140315ec7
003153EF  49 8B 3F                        mov rdi, qword ptr [r15]
003153F2  40 F6 C7 01                     test dil, 1
003153F6  0F 84 92 09 00 00               je 0x140315d8e
003153FC  4C 8B F7                        mov r14, rdi
003153FF  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00315409  49 C1 EE 0C                     shr r14, 0xc
0031540D  4C 23 F0                        and r14, rax
00315410  4C 3B 35 C9 88 B1 00            cmp r14, qword ptr [rip + 0xb188c9]
00315417  0F 87 FC 0C 00 00               ja 0x140316119
0031541D  4B 8D 0C 76                     lea rcx, [r14 + r14*2]
00315421  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
0031542B  48 03 C9                        add rcx, rcx
0031542E  48 8B C0                        mov rax, rax
00315431  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00315435  B3 00                           mov bl, 0
00315437  48 C1 E8 36                     shr rax, 0x36
0031543B  0F BA E0 00                     bt eax, 0
0031543F  0F 83 D6 0C 00 00               jae 0x14031611b
00315445  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0031544F  48 8B C0                        mov rax, rax
00315452  48 8D 2C C8                     lea rbp, [rax + rcx*8]
00315456  33 DB                           xor ebx, ebx
00315458  F0 48 0F BA 6D 18 3F            lock bts qword ptr [rbp + 0x18], 0x3f
0031545F  0F 82 DB 04 00 00               jb 0x140315940
00315465  8B 94 24 A0 00 00 00            mov edx, dword ptr [rsp + 0xa0]
0031546C  4C 8B C5                        mov r8, rbp
0031546F  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00315477  E8 14 0E 00 00                  call 0x140316290
0031547C  44 8B E8                        mov r13d, eax
0031547F  85 C0                           test eax, eax
00315481  0F 84 78 08 00 00               je 0x140315cff
00315487  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0031548C  4C 89 B0 90 00 00 00            mov qword ptr [rax + 0x90], r14
00315493  44 89 A8 98 00 00 00            mov dword ptr [rax + 0x98], r13d
0031549A  41 8B 44 24 20                  mov eax, dword ptr [r12 + 0x20]
0031549F  8B D0                           mov edx, eax
003154A1  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
003154A5  48 C1 E9 05                     shr rcx, 5
003154A9  33 D1                           xor edx, ecx
003154AB  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
003154B0  83 E2 1F                        and edx, 0x1f
003154B3  49 8B CE                        mov rcx, r14
003154B6  33 D0                           xor edx, eax
003154B8  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
003154BD  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
003154C5  41 89 54 24 20                  mov dword ptr [r12 + 0x20], edx
003154CA  E8 01 38 02 00                  call 0x140338cd0
003154CF  3B C6                           cmp eax, esi
003154D1  0F 85 28 08 00 00               jne 0x140315cff
003154D7  44 0F B6 65 22                  movzx r12d, byte ptr [rbp + 0x22]
003154DC  32 DB                           xor bl, bl
003154DE  41 80 E4 07                     and r12b, 7
003154E2  41 80 FC 06                     cmp r12b, 6
003154E6  0F 85 2F 06 00 00               jne 0x140315b1b
003154EC  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003154F6  F0 48 21 45 18                  lock and qword ptr [rbp + 0x18], rax
003154FB  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
003154FF  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
00315509  48 0B C1                        or rax, rcx
0031550C  4C 3B F8                        cmp r15, rax
0031550F  0F 85 00 04 00 00               jne 0x140315915
00315515  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
00315519  48 85 C0                        test rax, rax
0031551C  0F 88 F3 03 00 00               js 0x140315915
00315522  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
00315526  48 0F BA E0 28                  bt rax, 0x28
0031552B  0F 82 E4 03 00 00               jb 0x140315915
00315531  8B 45 20                        mov eax, dword ptr [rbp + 0x20]
00315534  C1 E8 18                        shr eax, 0x18
00315537  A8 08                           test al, 8
00315539  0F 85 D6 03 00 00               jne 0x140315915
0031553F  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
00315543  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
0031554D  48 23 C1                        and rax, rcx
00315550  48 B9 FE FF FF FF 3F 00 00 00   movabs rcx, 0x3ffffffffe
0031555A  48 3B C1                        cmp rax, rcx
0031555D  0F 84 B2 03 00 00               je 0x140315915
00315563  49 8B D7                        mov rdx, r15
00315566  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00315570  48 C1 E2 19                     shl rdx, 0x19
00315574  48 8B C0                        mov rax, rax
00315577  48 C1 E0 19                     shl rax, 0x19
0031557B  48 2B D0                        sub rdx, rax
0031557E  48 C1 FA 10                     sar rdx, 0x10
00315582  E8 B9 0F 00 00                  call 0x140316540
00315587  24 0F                           and al, 0xf
00315589  3C 08                           cmp al, 8
0031558B  0F 84 84 03 00 00               je 0x140315915
00315591  8B 45 20                        mov eax, dword ptr [rbp + 0x20]
00315594  66 83 F8 01                     cmp ax, 1
00315598  0F 85 77 03 00 00               jne 0x140315915
0031559E  45 33 F6                        xor r14d, r14d
003155A1  41 83 FD 01                     cmp r13d, 1
003155A5  75 71                           jne 0x140315618
003155A7  41 8B CD                        mov ecx, r13d
003155AA  E8 41 6B F6 FF                  call 0x14027c0f0
003155AF  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
003155B7  E8 14 13 00 00                  call 0x1403168d0
003155BC  4C 8B F0                        mov r14, rax
003155BF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003155C8  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003155CF  48 8B 89 10 04 00 00            mov rcx, qword ptr [rcx + 0x410]
003155D6  48 81 C1 EC 03 00 00            add rcx, 0x3ec
003155DD  E8 AE 4F F3 FF                  call 0x14024a590
003155E2  4D 85 F6                        test r14, r14
003155E5  0F 84 2A 03 00 00               je 0x140315915
003155EB  41 8B 46 30                     mov eax, dword ptr [r14 + 0x30]
003155EF  48 8D 0D 82 EF CF FF            lea rcx, [rip - 0x30107e]
003155F6  48 C1 E8 13                     shr rax, 0x13
003155FA  83 E0 03                        and eax, 3
003155FD  48 83 3C C1 10                  cmp qword ptr [rcx + rax*8], 0x10
00315602  0F 84 0D 03 00 00               je 0x140315915
00315608  49 8B CE                        mov rcx, r14
0031560B  E8 C0 19 00 00                  call 0x140316fd0
00315610  85 C0                           test eax, eax
00315612  0F 84 FD 02 00 00               je 0x140315915
00315618  BB 04 00 00 00                  mov ebx, 4
0031561D  40 F6 C7 42                     test dil, 0x42
00315621  0F 85 38 03 00 00               jne 0x14031595f
00315627  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0031562F  48 3B 15 32 1E B2 00            cmp rdx, qword ptr [rip + 0xb21e32]
00315636  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
0031563B  0F 85 46 04 00 00               jne 0x140315a87
00315641  41 F6 C6 18                     test r14b, 0x18
00315645  0F 94 C1                        sete cl
00315648  40 F6 C7 20                     test dil, 0x20
0031564C  0F 95 C0                        setne al
0031564F  84 C8                           test al, cl
00315651  0F 84 6B 01 00 00               je 0x1403157c2
00315657  83 7C 24 60 03                  cmp dword ptr [rsp + 0x60], 3
0031565C  0F 83 60 01 00 00               jae 0x1403157c2
00315662  BB 03 00 00 00                  mov ebx, 3
00315667  E9 0D 03 00 00                  jmp 0x140315979
0031566C  FF 44 24 60                     inc dword ptr [rsp + 0x60]
00315670  48 8B 9C 24 90 01 00 00         mov rbx, qword ptr [rsp + 0x190]
00315678  48 85 DB                        test rbx, rbx
0031567B  74 29                           je 0x1403156a6
0031567D  48 8B 3B                        mov rdi, qword ptr [rbx]
00315680  41 B9 02 00 00 00               mov r9d, 2
00315686  4C 8B C3                        mov r8, rbx
00315689  49 8B D5                        mov rdx, r13
0031568C  49 8B CE                        mov rcx, r14
0031568F  E8 94 19 00 00                  call 0x140317028
00315694  85 C0                           test eax, eax
00315696  74 06                           je 0x14031569e
00315698  4C 89 23                        mov qword ptr [rbx], r12
0031569B  4C 8B E3                        mov r12, rbx
0031569E  48 8B DF                        mov rbx, rdi
003156A1  48 85 FF                        test rdi, rdi
003156A4  75 D7                           jne 0x14031567d
003156A6  48 8B 9C 24 B8 01 00 00         mov rbx, qword ptr [rsp + 0x1b8]
003156AE  48 C7 84 24 90 01 00 00 00 00 00 00  mov qword ptr [rsp + 0x190], 0
003156BA  48 85 DB                        test rbx, rbx
003156BD  74 29                           je 0x1403156e8
003156BF  48 8B 3B                        mov rdi, qword ptr [rbx]
003156C2  41 B9 03 00 00 00               mov r9d, 3
003156C8  4C 8B C3                        mov r8, rbx
003156CB  49 8B D5                        mov rdx, r13
003156CE  49 8B CE                        mov rcx, r14
003156D1  E8 52 19 00 00                  call 0x140317028
003156D6  85 C0                           test eax, eax
003156D8  74 06                           je 0x1403156e0
003156DA  4C 89 23                        mov qword ptr [rbx], r12
003156DD  4C 8B E3                        mov r12, rbx
003156E0  48 8B DF                        mov rbx, rdi
003156E3  48 85 FF                        test rdi, rdi
003156E6  75 D7                           jne 0x1403156bf
003156E8  33 DB                           xor ebx, ebx
003156EA  48 89 9C 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], rbx
003156F2  4D 85 ED                        test r13, r13
003156F5  74 22                           je 0x140315719
003156F7  41 81 65 14 7F FF FF FF         and dword ptr [r13 + 0x14], 0xffffff7f
003156FF  49 8B CD                        mov rcx, r13
00315702  E8 B9 C8 FF FF                  call 0x140311fc0
00315707  E8 64 E5 FF FF                  call 0x140313c70
0031570C  44 8B EB                        mov r13d, ebx
0031570F  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00315714  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
00315719  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0031571E  48 85 C0                        test rax, rax
00315721  74 0B                           je 0x14031572e
00315723  48 8B D0                        mov rdx, rax
00315726  49 8B CF                        mov rcx, r15
00315729  E8 92 17 F0 FF                  call 0x140216ec0
0031572E  0F B6 54 24 50                  movzx edx, byte ptr [rsp + 0x50]
00315733  49 8B CF                        mov rcx, r15
00315736  E8 55 7F F6 FF                  call 0x14027d690
0031573B  48 8D 8C 24 40 01 00 00         lea rcx, [rsp + 0x140]
00315743  E8 D0 F8 FF FF                  call 0x140315018
00315748  4D 85 E4                        test r12, r12
0031574B  0F 84 7A 02 00 00               je 0x1403159cb
00315751  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
00315759  E9 26 FB FF FF                  jmp 0x140315284
0031575E  48 85 C0                        test rax, rax
00315761  0F 85 10 06 00 00               jne 0x140315d77
00315767  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0031576C  4C 8D 84 24 D8 00 00 00         lea r8, [rsp + 0xd8]
00315774  48 8B CF                        mov rcx, rdi
00315777  45 33 C9                        xor r9d, r9d
0031577A  49 8B D7                        mov rdx, r15
0031577D  E8 8E B5 F6 FF                  call 0x140280d10
00315782  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00315787  48 3B C3                        cmp rax, rbx
0031578A  0F 84 4F FC FF FF               je 0x1403153df
00315790  48 8B D0                        mov rdx, rax
00315793  48 8B CF                        mov rcx, rdi
00315796  E8 25 17 F0 FF                  call 0x140216ec0
0031579B  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
003157A0  45 33 C9                        xor r9d, r9d
003157A3  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
003157A8  32 DB                           xor bl, bl
003157AA  4C 8B E1                        mov r12, rcx
003157AD  4C 8B FF                        mov r15, rdi
003157B0  E9 65 FB FF FF                  jmp 0x14031531a
003157B5  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
003157BA  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
003157C2  48 3B 15 9F 1C B2 00            cmp rdx, qword ptr [rip + 0xb21c9f]
003157C9  0F 85 B8 02 00 00               jne 0x140315a87
003157CF  4D 8B C7                        mov r8, r15
003157D2  48 8B D5                        mov rdx, rbp
003157D5  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
003157DA  49 8B CF                        mov rcx, r15
003157DD  E8 1A A7 14 00                  call 0x14045fefc
003157E2  85 C0                           test eax, eax
003157E4  0F 84 9D 02 00 00               je 0x140315a87
003157EA  33 DB                           xor ebx, ebx
003157EC  F0 48 0F BA 6D 18 3F            lock bts qword ptr [rbp + 0x18], 0x3f
003157F3  0F 82 C9 04 00 00               jb 0x140315cc2
003157F9  48 8B CD                        mov rcx, rbp
003157FC  E8 7F EB 01 00                  call 0x140334380
00315801  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
0031580B  F0 48 21 4D 18                  lock and qword ptr [rbp + 0x18], rcx
00315810  85 C0                           test eax, eax
00315812  0F 84 6F 02 00 00               je 0x140315a87
00315818  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
0031581D  4D 85 F6                        test r14, r14
00315820  0F 85 2B 07 00 00               jne 0x140315f51
00315826  E8 65 D4 F2 FF                  call 0x140242c90
0031582B  BA 01 00 00 00                  mov edx, 1
00315830  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00315835  8B FA                           mov edi, edx
00315837  4C 8B F0                        mov r14, rax
0031583A  33 ED                           xor ebp, ebp
0031583C  49 8D 9E 28 10 00 00            lea rbx, [r14 + 0x1028]
00315843  C7 43 10 02 00 00 00            mov dword ptr [rbx + 0x10], 2
0031584A  89 53 14                        mov dword ptr [rbx + 0x14], edx
0031584D  4C 89 3B                        mov qword ptr [rbx], r15
00315850  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
00315857  C1 E8 08                        shr eax, 8
0031585A  C0 E8 03                        shr al, 3
0031585D  24 01                           and al, 1
0031585F  41 88 86 40 10 00 00            mov byte ptr [r14 + 0x1040], al
00315866  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
0031586D  A8 0F                           test al, 0xf
0031586F  75 20                           jne 0x140315891
00315871  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0031587A  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00315881  48 81 C1 00 04 00 00            add rcx, 0x400
00315888  4C 3B F9                        cmp r15, rcx
0031588B  0F 85 E5 07 00 00               jne 0x140316076
00315891  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
00315898  8B CD                           mov ecx, ebp
0031589A  A8 0F                           test al, 0xf
0031589C  0F 44 CA                        cmove ecx, edx
0031589F  41 83 A6 38 10 00 00 DB         and dword ptr [r14 + 0x1038], 0xffffffdb
003158A7  4C 8B C2                        mov r8, rdx
003158AA  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
003158B2  45 33 C9                        xor r9d, r9d
003158B5  41 89 8E 30 10 00 00            mov dword ptr [r14 + 0x1030], ecx
003158BC  48 8B CB                        mov rcx, rbx
003158BF  66 41 C7 86 41 10 00 00 00 00   mov word ptr [r14 + 0x1041], 0
003158C9  41 89 AE 44 10 00 00            mov dword ptr [r14 + 0x1044], ebp
003158D0  49 89 AE 48 10 00 00            mov qword ptr [r14 + 0x1048], rbp
003158D7  49 89 AE 50 10 00 00            mov qword ptr [r14 + 0x1050], rbp
003158DE  E8 8D DD F7 FF                  call 0x140293670
003158E3  45 33 C0                        xor r8d, r8d
003158E6  48 8B D3                        mov rdx, rbx
003158E9  49 8B CF                        mov rcx, r15
003158EC  E8 77 B8 F2 FF                  call 0x140241168
003158F1  85 FF                           test edi, edi
003158F3  74 0A                           je 0x1403158ff
003158F5  E8 76 E3 FF FF                  call 0x140313c70
003158FA  48 89 6C 24 68                  mov qword ptr [rsp + 0x68], rbp
003158FF  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00315907  48 FF 84 24 B0 00 00 00         inc qword ptr [rsp + 0xb0]
0031590F  48 FF 40 08                     inc qword ptr [rax + 8]
00315913  32 DB                           xor bl, bl
00315915  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
0031591A  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
0031591F  8B 6C 24 30                     mov ebp, dword ptr [rsp + 0x30]
00315923  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
00315928  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0031592D  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
00315932  4C 8B E1                        mov r12, rcx
00315935  E9 E0 F9 FF FF                  jmp 0x14031531a
0031593A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
00315940  FF C3                           inc ebx
00315942  85 1D 64 F9 CA 00               test dword ptr [rip + 0xcaf964], ebx
00315948  0F 84 5D 06 00 00               je 0x140315fab
0031594E  F3 90                           pause
00315950  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
00315954  48 85 C0                        test rax, rax
00315957  0F 89 FB FA FF FF               jns 0x140315458
0031595D  EB E1                           jmp 0x140315940
0031595F  83 7C 24 60 08                  cmp dword ptr [rsp + 0x60], 8
00315964  0F 83 15 06 00 00               jae 0x140315f7f
0031596A  BB 02 00 00 00                  mov ebx, 2
0031596F  48 83 FB 04                     cmp rbx, 4
00315973  0F 84 3C FE FF FF               je 0x1403157b5
00315979  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
0031597E  4D 85 ED                        test r13, r13
00315981  0F 84 59 02 00 00               je 0x140315be0
00315987  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
0031598F  45 33 C9                        xor r9d, r9d
00315992  49 8B CD                        mov rcx, r13
00315995  45 8D 41 01                     lea r8d, [r9 + 1]
00315999  E8 D2 DC F7 FF                  call 0x140293670
0031599E  48 8B BC 24 98 00 00 00         mov rdi, qword ptr [rsp + 0x98]
003159A6  48 8D 04 9B                     lea rax, [rbx + rbx*4]
003159AA  48 8D 8C 24 40 01 00 00         lea rcx, [rsp + 0x140]
003159B2  48 8D 0C C1                     lea rcx, [rcx + rax*8]
003159B6  48 8B 01                        mov rax, qword ptr [rcx]
003159B9  48 89 07                        mov qword ptr [rdi], rax
003159BC  48 89 39                        mov qword ptr [rcx], rdi
003159BF  32 DB                           xor bl, bl
003159C1  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
003159C6  E9 54 FF FF FF                  jmp 0x14031591f
003159CB  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
003159D3  E8 38 96 F4 FF                  call 0x14025f010
003159D8  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
003159E0  83 BC 24 80 00 00 00 00         cmp dword ptr [rsp + 0x80], 0
003159E8  74 1B                           je 0x140315a05
003159EA  33 D2                           xor edx, edx
003159EC  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
003159F4  E8 77 1D 0B 00                  call 0x1403c7770
003159F9  48 8D 8F 00 04 00 00            lea rcx, [rdi + 0x400]
00315A00  E8 DB 99 F7 FF                  call 0x14028f3e0
00315A05  49 8B 8E 30 01 00 00            mov rcx, qword ptr [r14 + 0x130]
00315A0C  48 85 C9                        test rcx, rcx
00315A0F  0F 84 CA 06 00 00               je 0x1403160df
00315A15  E8 C6 F0 01 00                  call 0x140334ae0
00315A1A  33 DB                           xor ebx, ebx
00315A1C  49 89 9E 30 01 00 00            mov qword ptr [r14 + 0x130], rbx
00315A23  49 8B 86 28 01 00 00            mov rax, qword ptr [r14 + 0x128]
00315A2A  48 85 C0                        test rax, rax
00315A2D  74 19                           je 0x140315a48
00315A2F  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
00315A33  33 D2                           xor edx, edx
00315A35  49 8B 8E 28 01 00 00            mov rcx, qword ptr [r14 + 0x128]
00315A3C  E8 BF C5 05 00                  call 0x140372000
00315A41  49 89 9E 28 01 00 00            mov qword ptr [r14 + 0x128], rbx
00315A48  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00315A50  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00315A58  48 01 08                        add qword ptr [rax], rcx
00315A5B  48 8B 8C 24 E0 01 00 00         mov rcx, qword ptr [rsp + 0x1e0]
00315A63  48 33 CC                        xor rcx, rsp
00315A66  E8 D5 6B 39 00                  call 0x1406ac640
00315A6B  48 8B 9C 24 48 02 00 00         mov rbx, qword ptr [rsp + 0x248]
00315A73  48 81 C4 F0 01 00 00            add rsp, 0x1f0
00315A7A  41 5F                           pop r15
00315A7C  41 5E                           pop r14
00315A7E  41 5D                           pop r13
00315A80  41 5C                           pop r12
00315A82  5F                              pop rdi
00315A83  5E                              pop rsi
00315A84  5D                              pop rbp
00315A85  C3                              ret
00315A86  CC                              int3
00315A87  4C 8B BC 24 B8 00 00 00         mov r15, qword ptr [rsp + 0xb8]
00315A8F  4C 3B 3D 7A A4 B1 00            cmp r15, qword ptr [rip + 0xb1a47a]
00315A96  0F 84 AB 04 00 00               je 0x140315f47
00315A9C  41 83 FD 01                     cmp r13d, 1
00315AA0  0F 85 A1 04 00 00               jne 0x140315f47
00315AA6  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00315AAB  48 8B 80 60 03 00 00            mov rax, qword ptr [rax + 0x360]
00315AB2  4C 3B F8                        cmp r15, rax
00315AB5  0F 85 58 FE FF FF               jne 0x140315913
00315ABB  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00315AC3  F7 82 54 07 00 00 00 10 00 00   test dword ptr [rdx + 0x754], 0x1000
00315ACD  0F 85 40 FE FF FF               jne 0x140315913
00315AD3  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00315AD8  8B 82 A4 07 00 00               mov eax, dword ptr [rdx + 0x7a4]
00315ADE  8B 8F 20 01 00 00               mov ecx, dword ptr [rdi + 0x120]
00315AE4  41 3B C5                        cmp eax, r13d
00315AE7  0F 85 CC 05 00 00               jne 0x1403160b9
00315AED  32 DB                           xor bl, bl
00315AEF  41 F6 C6 18                     test r14b, 0x18
00315AF3  74 38                           je 0x140315b2d
00315AF5  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
00315AFA  BA 03 00 00 00                  mov edx, 3
00315AFF  B3 01                           mov bl, 1
00315B01  49 8D 8E 00 01 00 00            lea rcx, [r14 + 0x100]
00315B08  44 8D 4A 01                     lea r9d, [rdx + 1]
00315B0C  44 8D 42 FF                     lea r8d, [rdx - 1]
00315B10  E8 5B D7 00 00                  call 0x140323270
00315B15  49 89 46 60                     mov qword ptr [r14 + 0x60], rax
00315B19  EB 3E                           jmp 0x140315b59
00315B1B  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
00315B20  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00315B25  4C 8B BC 24 B8 00 00 00         mov r15, qword ptr [rsp + 0xb8]
00315B2D  BA 03 00 00 00                  mov edx, 3
00315B32  48 8D 8F 00 01 00 00            lea rcx, [rdi + 0x100]
00315B39  44 8D 4A 01                     lea r9d, [rdx + 1]
00315B3D  44 8D 42 FF                     lea r8d, [rdx - 1]
00315B41  E8 2A D7 00 00                  call 0x140323270
00315B46  48 89 47 60                     mov qword ptr [rdi + 0x60], rax
00315B4A  41 80 FC 06                     cmp r12b, 6
00315B4E  0F 85 BF 01 00 00               jne 0x140315d13
00315B54  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
00315B59  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00315B5E  4D 85 ED                        test r13, r13
00315B61  0F 84 1E 01 00 00               je 0x140315c85
00315B67  48 8B BC 24 98 00 00 00         mov rdi, qword ptr [rsp + 0x98]
00315B6F  4D 8B C5                        mov r8, r13
00315B72  48 8B D7                        mov rdx, rdi
00315B75  49 8B CE                        mov rcx, r14
00315B78  E8 67 55 F1 FF                  call 0x14022b0e4
00315B7D  85 C0                           test eax, eax
00315B7F  0F 88 D3 01 00 00               js 0x140315d58
00315B85  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
00315B8D  48 89 07                        mov qword ptr [rdi], rax
00315B90  49 C7 46 60 00 00 00 00         mov qword ptr [r14 + 0x60], 0
00315B98  48 89 BC 24 40 01 00 00         mov qword ptr [rsp + 0x140], rdi
00315BA0  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00315BA8  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00315BAD  8B 6C 24 30                     mov ebp, dword ptr [rsp + 0x30]
00315BB1  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
00315BB6  48 FF 40 08                     inc qword ptr [rax + 8]
00315BBA  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00315BC2  48 85 C0                        test rax, rax
00315BC5  0F 84 62 FD FF FF               je 0x14031592d
00315BCB  F0 48 FF 88 88 02 00 00         lock dec qword ptr [rax + 0x288]
00315BD3  4C 8B E1                        mov r12, rcx
00315BD6  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
00315BDB  E9 3A F7 FF FF                  jmp 0x14031531a
00315BE0  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00315BE5  4D 85 C0                        test r8, r8
00315BE8  75 0D                           jne 0x140315bf7
00315BEA  E8 A1 D0 F2 FF                  call 0x140242c90
00315BEF  4C 8B C0                        mov r8, rax
00315BF2  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00315BF7  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00315BFC  45 33 C9                        xor r9d, r9d
00315BFF  45 89 48 10                     mov dword ptr [r8 + 0x10], r9d
00315C03  4D 8B E8                        mov r13, r8
00315C06  41 C7 40 14 80 00 00 00         mov dword ptr [r8 + 0x14], 0x80
00315C0E  49 89 10                        mov qword ptr [r8], rdx
00315C11  8B 8A B8 00 00 00               mov ecx, dword ptr [rdx + 0xb8]
00315C17  C1 E9 08                        shr ecx, 8
00315C1A  C0 E9 03                        shr cl, 3
00315C1D  80 E1 01                        and cl, 1
00315C20  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00315C25  41 88 48 18                     mov byte ptr [r8 + 0x18], cl
00315C29  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
00315C2F  A8 0F                           test al, 0xf
00315C31  75 20                           jne 0x140315c53
00315C33  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00315C3C  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00315C43  48 81 C1 00 04 00 00            add rcx, 0x400
00315C4A  48 3B D1                        cmp rdx, rcx
00315C4D  0F 85 59 04 00 00               jne 0x1403160ac
00315C53  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
00315C59  41 8B C9                        mov ecx, r9d
00315C5C  A8 0F                           test al, 0xf
00315C5E  B8 01 00 00 00                  mov eax, 1
00315C63  0F 44 C8                        cmove ecx, eax
00315C66  41 83 60 10 DB                  and dword ptr [r8 + 0x10], 0xffffffdb
00315C6B  41 89 48 08                     mov dword ptr [r8 + 8], ecx
00315C6F  66 45 89 48 19                  mov word ptr [r8 + 0x19], r9w
00315C74  45 89 48 1C                     mov dword ptr [r8 + 0x1c], r9d
00315C78  4D 89 48 20                     mov qword ptr [r8 + 0x20], r9
00315C7C  4D 89 48 28                     mov qword ptr [r8 + 0x28], r9
00315C80  E9 02 FD FF FF                  jmp 0x140315987
00315C85  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00315C8A  48 85 C0                        test rax, rax
00315C8D  75 0A                           jne 0x140315c99
00315C8F  E8 FC CF F2 FF                  call 0x140242c90
00315C94  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00315C99  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
00315C9D  45 33 C9                        xor r9d, r9d
00315CA0  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00315CA5  48 8B C8                        mov rcx, rax
00315CA8  4C 8B E8                        mov r13, rax
00315CAB  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00315CB0  C7 44 24 20 80 00 00 00         mov dword ptr [rsp + 0x20], 0x80
00315CB8  E8 43 F2 F7 FF                  call 0x140294f00
00315CBD  E9 A5 FE FF FF                  jmp 0x140315b67
00315CC2  FF C3                           inc ebx
00315CC4  85 1D E2 F5 CA 00               test dword ptr [rip + 0xcaf5e2], ebx
00315CCA  0F 84 16 03 00 00               je 0x140315fe6
00315CD0  F3 90                           pause
00315CD2  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
00315CD6  48 85 C0                        test rax, rax
00315CD9  0F 89 0D FB FF FF               jns 0x1403157ec
00315CDF  EB E1                           jmp 0x140315cc2
00315CE1  41 0F B6 D0                     movzx edx, r8b
00315CE5  49 8B CF                        mov rcx, r15
00315CE8  E8 A3 79 F6 FF                  call 0x14027d690
00315CED  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00315CF5  E8 16 93 F4 FF                  call 0x14025f010
00315CFA  E9 E1 FC FF FF                  jmp 0x1403159e0
00315CFF  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00315D09  F0 48 21 45 18                  lock and qword ptr [rbp + 0x18], rax
00315D0E  E9 00 FC FF FF                  jmp 0x140315913
00315D13  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00315D1D  F0 48 21 45 18                  lock and qword ptr [rbp + 0x18], rax
00315D22  4C 3B 3D E7 A1 B1 00            cmp r15, qword ptr [rip + 0xb1a1e7]
00315D29  0F 85 BA 01 00 00               jne 0x140315ee9
00315D2F  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
00315D37  41 F6 C6 18                     test r14b, 0x18
00315D3B  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
00315D40  B8 01 00 00 00                  mov eax, 1
00315D45  0F B6 DB                        movzx ebx, bl
00315D48  49 8B CE                        mov rcx, r14
00315D4B  0F 45 D8                        cmovne ebx, eax
00315D4E  E8 DD 45 F1 FF                  call 0x14022a330
00315D53  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00315D58  49 C7 46 60 00 00 00 00         mov qword ptr [r14 + 0x60], 0
00315D60  85 C0                           test eax, eax
00315D62  0F 89 38 FE FF FF               jns 0x140315ba0
00315D68  E9 B2 FB FF FF                  jmp 0x14031591f
00315D6D  40 88 7C 24 34                  mov byte ptr [rsp + 0x34], dil
00315D72  E9 EE F5 FF FF                  jmp 0x140315365
00315D77  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
00315D7C  49 8B CC                        mov rcx, r12
00315D7F  C6 44 24 34 01                  mov byte ptr [rsp + 0x34], 1
00315D84  32 DB                           xor bl, bl
00315D86  4C 8B C8                        mov r9, rax
00315D89  E9 8C F5 FF FF                  jmp 0x14031531a
00315D8E  48 8B C7                        mov rax, rdi
00315D91  32 DB                           xor bl, bl
00315D93  25 00 0C 00 00                  and eax, 0xc00
00315D98  48 3D 00 08 00 00               cmp rax, 0x800
00315D9E  0F 85 7F FB FF FF               jne 0x140315923
00315DA4  49 8B CF                        mov rcx, r15
00315DA7  E8 F4 CA F6 FF                  call 0x1402828a0
00315DAC  48 8B D8                        mov rbx, rax
00315DAF  48 0F BA E0 0B                  bt rax, 0xb
00315DB4  0F 83 05 FC FF FF               jae 0x1403159bf
00315DBA  48 8B C8                        mov rcx, rax
00315DBD  E8 4E CC 05 00                  call 0x140372a10
00315DC2  85 C0                           test eax, eax
00315DC4  74 DE                           je 0x140315da4
00315DC6  48 8B 05 B3 7E B1 00            mov rax, qword ptr [rip + 0xb17eb3]
00315DCD  48 85 C0                        test rax, rax
00315DD0  74 12                           je 0x140315de4
00315DD2  F6 C3 10                        test bl, 0x10
00315DD5  0F 85 63 01 00 00               jne 0x140315f3e
00315DDB  48 8B C8                        mov rcx, rax
00315DDE  48 F7 D1                        not rcx
00315DE1  48 23 CB                        and rcx, rbx
00315DE4  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00315DEE  48 C1 E9 0C                     shr rcx, 0xc
00315DF2  48 23 C8                        and rcx, rax
00315DF5  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00315DFF  48 8D 14 49                     lea rdx, [rcx + rcx*2]
00315E03  48 03 D2                        add rdx, rdx
00315E06  48 8B C0                        mov rax, rax
00315E09  48 3B 0D D0 7E B1 00            cmp rcx, qword ptr [rip + 0xb17ed0]
00315E10  4C 8D 34 D0                     lea r14, [rax + rdx*8]
00315E14  77 8E                           ja 0x140315da4
00315E16  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00315E20  48 8B C0                        mov rax, rax
00315E23  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
00315E27  48 C1 E8 36                     shr rax, 0x36
00315E2B  0F BA E0 00                     bt eax, 0
00315E2F  0F 83 6F FF FF FF               jae 0x140315da4
00315E35  33 ED                           xor ebp, ebp
00315E37  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00315E3E  0F 82 1C 01 00 00               jb 0x140315f60
00315E44  49 8B CF                        mov rcx, r15
00315E47  E8 54 CA F6 FF                  call 0x1402828a0
00315E4C  48 3B C3                        cmp rax, rbx
00315E4F  0F 85 7D 01 00 00               jne 0x140315fd2
00315E55  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00315E59  48 8B 0D 28 A2 B1 00            mov rcx, qword ptr [rip + 0xb1a228]
00315E60  48 C1 E8 2B                     shr rax, 0x2b
00315E64  25 FF 03 00 00                  and eax, 0x3ff
00315E69  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00315E6D  8B 40 04                        mov eax, dword ptr [rax + 4]
00315E70  84 C0                           test al, al
00315E72  0F 88 B5 01 00 00               js 0x14031602d
00315E78  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00315E7C  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
00315E86  48 0B C1                        or rax, rcx
00315E89  49 3B C7                        cmp rax, r15
00315E8C  0F 85 B6 01 00 00               jne 0x140316048
00315E92  32 DB                           xor bl, bl
00315E94  49 8B EE                        mov rbp, r14
00315E97  4D 85 F6                        test r14, r14
00315E9A  0F 84 21 FB FF FF               je 0x1403159c1
00315EA0  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00315EAA  48 8B C0                        mov rax, rax
00315EAD  4C 2B F0                        sub r14, rax
00315EB0  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00315EBA  49 C1 FE 04                     sar r14, 4
00315EBE  4C 0F AF F0                     imul r14, rax
00315EC2  E9 9E F5 FF FF                  jmp 0x140315465
00315EC7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00315ECC  3D 2D 02 00 C0                  cmp eax, 0xc000022d
00315ED1  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
00315ED6  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
00315EDB  49 0F 44 CC                     cmove rcx, r12
00315EDF  4C 8B E1                        mov r12, rcx
00315EE2  32 DB                           xor bl, bl
00315EE4  E9 31 F4 FF FF                  jmp 0x14031531a
00315EE9  41 83 FD 01                     cmp r13d, 1
00315EED  0F 85 3C FE FF FF               jne 0x140315d2f
00315EF3  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00315EF8  41 8B CD                        mov ecx, r13d
00315EFB  E8 90 F8 14 00                  call 0x140465790
00315F00  4C 3B F8                        cmp r15, rax
00315F03  75 27                           jne 0x140315f2c
00315F05  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00315F0D  F7 81 54 07 00 00 00 10 00 00   test dword ptr [rcx + 0x754], 0x1000
00315F17  75 13                           jne 0x140315f2c
00315F19  8B 97 20 01 00 00               mov edx, dword ptr [rdi + 0x120]
00315F1F  E8 84 F8 14 00                  call 0x1404657a8
00315F24  85 C0                           test eax, eax
00315F26  0F 85 03 FE FF FF               jne 0x140315d2f
00315F2C  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
00315F31  49 C7 46 60 00 00 00 00         mov qword ptr [r14 + 0x60], 0
00315F39  E9 DC F9 FF FF                  jmp 0x14031591a
00315F3E  48 83 E1 EF                     and rcx, 0xffffffffffffffef
00315F42  E9 9D FE FF FF                  jmp 0x140315de4
00315F47  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00315F4C  E9 9C FB FF FF                  jmp 0x140315aed
00315F51  33 ED                           xor ebp, ebp
00315F53  8B FD                           mov edi, ebp
00315F55  8D 55 01                        lea edx, [rbp + 1]
00315F58  E9 DF F8 FF FF                  jmp 0x14031583c
00315F5D  0F 1F 00                        nop dword ptr [rax]
00315F60  FF C5                           inc ebp
00315F62  85 2D 44 F3 CA 00               test dword ptr [rip + 0xcaf344], ebp
00315F68  0F 84 17 01 00 00               je 0x140316085
00315F6E  F3 90                           pause
00315F70  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00315F74  48 85 C0                        test rax, rax
00315F77  0F 89 BA FE FF FF               jns 0x140315e37
00315F7D  EB E1                           jmp 0x140315f60
00315F7F  49 8B D6                        mov rdx, r14
00315F82  49 8B CF                        mov rcx, r15
00315F85  E8 E6 F1 14 00                  call 0x140465170
00315F8A  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00315F92  33 D2                           xor edx, edx
00315F94  41 83 FD 01                     cmp r13d, 1
00315F98  41 B8 0A 00 00 00               mov r8d, 0xa
00315F9E  0F 95 C2                        setne dl
00315FA1  E8 8A 87 F7 FF                  call 0x14028e730
00315FA6  E9 C4 F9 FF FF                  jmp 0x14031596f
00315FAB  8B 05 07 0B CB 00               mov eax, dword ptr [rip + 0xcb0b07]
00315FB1  A8 40                           test al, 0x40
00315FB3  0F 84 95 F9 FF FF               je 0x14031594e
00315FB9  E8 D2 94 FF FF                  call 0x14030f490
00315FBE  84 C0                           test al, al
00315FC0  0F 84 88 F9 FF FF               je 0x14031594e
00315FC6  8B CB                           mov ecx, ebx
00315FC8  E8 93 94 FF FF                  call 0x14030f460
00315FCD  E9 7E F9 FF FF                  jmp 0x140315950
00315FD2  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00315FDC  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
00315FE1  E9 BE FD FF FF                  jmp 0x140315da4
00315FE6  8B 05 CC 0A CB 00               mov eax, dword ptr [rip + 0xcb0acc]
00315FEC  A8 40                           test al, 0x40
00315FEE  0F 84 DC FC FF FF               je 0x140315cd0
00315FF4  E8 97 94 FF FF                  call 0x14030f490
00315FF9  84 C0                           test al, al
00315FFB  0F 84 CF FC FF FF               je 0x140315cd0
00316001  8B CB                           mov ecx, ebx
00316003  E8 58 94 FF FF                  call 0x14030f460
00316008  E9 C5 FC FF FF                  jmp 0x140315cd2
0031600D  45 33 C0                        xor r8d, r8d
00316010  41 8D 50 10                     lea edx, [r8 + 0x10]
00316014  E8 CB 28 06 00                  call 0x1403788e4
00316019  48 8B CB                        mov rcx, rbx
0031601C  85 C0                           test eax, eax
0031601E  0F 94 C1                        sete cl
00316021  49 89 8E 38 01 00 00            mov qword ptr [r14 + 0x138], rcx
00316028  E9 88 F2 FF FF                  jmp 0x1403152b5
0031602D  33 D2                           xor edx, edx
0031602F  49 8B CE                        mov rcx, r14
00316032  E8 B9 E9 0E 00                  call 0x1404049f0
00316037  4C 8B F0                        mov r14, rax
0031603A  48 85 C0                        test rax, rax
0031603D  0F 84 7C F9 FF FF               je 0x1403159bf
00316043  E9 30 FE FF FF                  jmp 0x140315e78
00316048  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
0031604C  48 0F BA E0 28                  bt rax, 0x28
00316051  0F 82 3B FE FF FF               jb 0x140315e92
00316057  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0031605B  4C 8B CB                        mov r9, rbx
0031605E  4D 8B C7                        mov r8, r15
00316061  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00316066  BA 11 04 00 00                  mov edx, 0x411
0031606B  B9 1A 00 00 00                  mov ecx, 0x1a
00316070  E8 EB 75 1E 00                  call 0x1404fd660
00316075  CC                              int3
00316076  41 83 8E 38 10 00 00 09         or dword ptr [r14 + 0x1038], 9
0031607E  8B CD                           mov ecx, ebp
00316080  E9 1A F8 FF FF                  jmp 0x14031589f
00316085  8B 05 2D 0A CB 00               mov eax, dword ptr [rip + 0xcb0a2d]
0031608B  A8 40                           test al, 0x40
0031608D  0F 84 DB FE FF FF               je 0x140315f6e
00316093  E8 F8 93 FF FF                  call 0x14030f490
00316098  84 C0                           test al, al
0031609A  0F 84 CE FE FF FF               je 0x140315f6e
003160A0  8B CD                           mov ecx, ebp
003160A2  E8 B9 93 FF FF                  call 0x14030f460
003160A7  E9 C4 FE FF FF                  jmp 0x140315f70
003160AC  41 83 48 10 09                  or dword ptr [r8 + 0x10], 9
003160B1  41 8B C9                        mov ecx, r9d
003160B4  E9 AD FB FF FF                  jmp 0x140315c66
003160B9  3B C1                           cmp eax, ecx
003160BB  0F 84 2C FA FF FF               je 0x140315aed
003160C1  83 F8 02                        cmp eax, 2
003160C4  0F 83 49 F8 FF FF               jae 0x140315913
003160CA  33 C0                           xor eax, eax
003160CC  F0 0F B1 8A A4 07 00 00         lock cmpxchg dword ptr [rdx + 0x7a4], ecx
003160D4  0F 84 13 FA FF FF               je 0x140315aed
003160DA  E9 34 F8 FF FF                  jmp 0x140315913
003160DF  33 DB                           xor ebx, ebx
003160E1  E9 3D F9 FF FF                  jmp 0x140315a23
003160E6  33 D2                           xor edx, edx
003160E8  49 8B CF                        mov rcx, r15
003160EB  E8 30 84 F9 FF                  call 0x1402ae520
003160F0  85 C0                           test eax, eax
003160F2  0F 85 6D F2 FF FF               jne 0x140315365
003160F8  4D 85 C9                        test r9, r9
003160FB  0F 84 5B F2 FF FF               je 0x14031535c
00316101  49 8B D1                        mov rdx, r9
00316104  49 8B CF                        mov rcx, r15
00316107  E8 44 85 F9 FF                  call 0x1402ae650
0031610C  85 C0                           test eax, eax
0031610E  0F 85 51 F2 FF FF               jne 0x140315365
00316114  E9 43 F2 FF FF                  jmp 0x14031535c
00316119  32 DB                           xor bl, bl
0031611B  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00316120  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
00316125  4C 8B E1                        mov r12, rcx
00316128  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0031612D  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
00316132  E9 E3 F1 FF FF                  jmp 0x14031531a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSharePages(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int8 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int8 v_stack_m1F4;
    unsigned int v_stack_m1F8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p34;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pD0;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (496);
    result = (*(unsigned __int64 *)(v_rip + 11490834)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rdi = 0;
    v_stack_m168 = *(unsigned __int64 *)(a1);
    v_stack_m188 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 140)));
    v_stack_m1E8 = a1;
    v_stack_m180 = *(unsigned __int64 *)(a1 + 104);
    a3 = (unsigned int)((a3) + 1);
    v_stack_m1C8 = 0;
    v_stack_m148 = v_xmm0;
    v_stack_m178 = 0;
    v_stack_m138 = v_xmm0;
    v_stack_m1B0 = *(unsigned __int64 *)(a2 + 32);
    v_stack_m128 = v_xmm0;
    result = MiInitializePageColorBase(*(unsigned __int64 *)(a2 + 32), v_rdi + 3, a3, a1 + 320);
    v_stack_m1A8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1A0 = *(unsigned __int64 *)(a2 + 40);
    if (*(unsigned __int64 *)(a2 + 40) == 0) goto loc_00315262;
    if ((*(unsigned __int64 *)(a2 + 40)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) goto loc_00315262;
    result = ExAcquireSpinLockExclusive(v_rip + 11674310, v_rdi + 3, a3, a1 + 320);
    result = MiPrepareAttachThread(*(unsigned __int64 *)(a2 + 40), *(unsigned __int64 *)(a2 + 40) + 1024, a3, (unsigned __int8)(result));
    v_stack_m1A8 = (unsigned int)(result);
    result = MiReleaseSpinLockExclusive(v_rip + 11674268, (unsigned __int8)((unsigned __int8)(result)), a3, (unsigned __int8)(result));
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00315A05;
    v_stack_m118 = v_xmm0;
    v_stack_m108 = v_xmm0;
    v_stack_mF8 = v_xmm0;
    result = KiStackAttachProcess(*(unsigned __int64 *)(a2 + 40), 0 + 1, v_stack_m148, (unsigned __int8)(result));
loc_00315262:
    v_rbx = 0;
    *(unsigned __int64 *)(a1 + 312) = 0;
    v_stack_m158 = *(unsigned __int64 *)(gs_base + (0 + 392));
loc_00315284:
    v_stack_mE8 = 0;
    v_stack_mC0 = 0;
    v_stack_m98 = 0;
    v_stack_m70 = 0;
    if ((*(unsigned __int64 *)(a1 + 312)) > 1) goto loc_0031600D;
loc_003152B5:
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(a1 + 296)) == 0) {
        a1 = v_stack_m168;
        result = MiAllocateCombineBlock(a1, 0 + 1, v_stack_m148, (unsigned __int8)(result));
        *(unsigned __int64 *)(a1 + 296) = result;
    }
    v_rbx = 0;
    v_stack_m1F0 = 0;
    v_stack_m1F4 = 0;
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(a2 + 32), 0 + 1, v_stack_m148, (unsigned __int8)(result));
    v_stack_m1D8 = (unsigned __int8)(result);
    if ((*(unsigned __int64 *)(a1 + 296)) == 0) goto loc_00315CE1;
    if (*(unsigned __int64 *)(a2 + 40) == 0) goto loc_00315315;
    result = MiProcessSuitableForCombining(*(unsigned __int64 *)(a2 + 40), 0 + 1, (unsigned __int8)(result), (unsigned __int8)(result));
    if ((unsigned int)(result) == 0) goto loc_00315CE1;
loc_00315315:
loc_0031531A:
    v_stack_m190 = *(unsigned __int64 *)(a2 + 48);
    v_rbp = 0;
    v_rdi = 0;
    if (0 == 0) { v_rbp = (unsigned int)(0 + 1); }
    v_stack_m1F8 = (unsigned int)(v_rbp);
    if ((*(unsigned __int64 *)(a1 + 296)) == 0) goto loc_00315365;
    if ((*(unsigned __int64 *)(a1 + 312)) > 1) goto loc_00315365;
    if (v_stack_m1F4 != 0) goto loc_00315D6D;
    if ((((unsigned __int8)(v_rbp)) & (7)) == 0) goto loc_003160E6;
loc_0031535C:
    result = KeShouldYieldProcessor(*(unsigned __int64 *)(a2 + 40), 0 + 1, (unsigned __int8)(result), v_stack_m1F0);
    if ((unsigned int)(result) != 0) {
        v_rdi = 1;
    }
    if (*(unsigned __int64 *)(a2 + 48) == 0) goto loc_0031566C;
    if ((unsigned __int8)(v_rdi) != 0) goto loc_00315670;
    v_stack_m1E0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 48));
    v_r15 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 48) + 16)) >> (9);
    v_r15 = (v_r15) & ((unsigned __int8)(result));
    v_stack_m198 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 48) + 16);
    v_stack_m160 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 48) + 8);
    v_r15 = (v_r15) + (0 + 1);
    v_rbx = (v_r15) >> (9);
    v_rbx = (v_rbx) & ((unsigned __int8)(result));
    v_rbx = (v_rbx) + (0 + 1);
    if (v_stack_m1F0 != v_rbx) goto loc_0031575E;
loc_003153DF:
    result = MiReplenishCombineResources(a1, 0 + 1, (unsigned __int8)(result), v_stack_m1F0);
    if (sign_flag) goto loc_00315EC7;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) == 0) goto loc_00315D8E;
    v_r14 = (*(unsigned __int64 *)(v_r15)) >> (12);
    v_r14 = (v_r14) & (result);
    if (v_r14 > (*(unsigned __int64 *)(v_rip + 11634889))) goto loc_00316119;
    a1 = (v_r14 + v_r14 * 2) + (v_r14 + v_r14 * 2);
    result = (*(unsigned __int64 *)(result + a1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_0031611B;
    v_rbx = 0;
loc_00315458:
    if (condition_is_below) goto loc_00315940;
loc_00315465:
    result = MiCombineCandidate(v_stack_m168, (unsigned int)(v_stack_m188), result + a1 * 8, v_stack_m1F0);
    if ((unsigned int)(result) == 0) goto loc_00315CFF;
    *(unsigned __int64 *)(v_stack_m1E8 + 144) = v_r14;
    *(unsigned int *)(v_stack_m1E8 + 152) = (unsigned int)((unsigned int)((unsigned int)(result)));
    a1 = (*(unsigned __int64 *)(result + a1 * 8 + 16)) >> (5);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 48) + 32))))) ^ ((unsigned int)(a1)));
    v_stack_m1B8 = a1;
    a2 = (unsigned int)((a2) & (31));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 48) + 32)))));
    v_stack_m170 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 48) + 24);
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 48) + 32) = (unsigned int)(a2);
    result = MiPageToNode(v_r14, a2, result + a1 * 8, v_stack_m1F0);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(a3)))) goto loc_00315CFF;
    v_rbx = 0;
    v_r12 = (unsigned __int8)((*(unsigned __int8 *)(result + a1 * 8 + 34)) & (7));
    if (((unsigned __int8)(v_r12)) != 6) goto loc_00315B1B;
    result = (*(unsigned __int64 *)(result + a1 * 8 + 8)) | (v_r14);
    if (v_r15 != result) goto loc_00315915;
    if (sign_flag) goto loc_00315915;
    if (condition_is_below) goto loc_00315915;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + a1 * 8 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_00315915;
    result = (*(unsigned __int64 *)(result + a1 * 8 + 40)) & (v_r14);
    if (result == v_r14) goto loc_00315915;
    a2 = (v_r15) << (25);
    result = (result) << (25);
    a2 = (a2) - (result);
    a2 = (a2) >> (16);
    result = MiGetWsleContents(v_r14, a2, result + a1 * 8, v_stack_m1F0);
    result = (unsigned __int8)((result) & (15));
    if (((unsigned __int8)(result)) == 8) goto loc_00315915;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(result + a1 * 8 + 32)))) != 1) goto loc_00315915;
    v_r14 = 0;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 1) goto loc_00315618;
    result = MiLockVadTree((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a2, result + a1 * 8, v_stack_m1F0);
    result = MiLocateAddress(v_stack_m198, a2, result + a1 * 8, v_stack_m1F0);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040)) + (0x3ECULL);
    result = ExReleaseSpinLockSharedFromDpcLevel(a1, a2, result + a1 * 8, v_stack_m1F0);
    if (result == 0) goto loc_00315915;
    result = ((unsigned int)(*(unsigned int *)(result + 48))) >> (19);
    result = (unsigned int)((result) & (3));
    if ((*(unsigned __int64 *)(v_rip - 3149950 + result * 8)) == 16) goto loc_00315915;
    result = MiVadSupportsPrivateCommit(result, a2, result + a1 * 8, v_stack_m1F0);
    if ((unsigned int)(result) == 0) goto loc_00315915;
loc_00315618:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (66)) != 0) goto loc_0031595F;
    if (v_stack_m160 != (*(unsigned __int64 *)(v_rip + 11673138))) goto loc_00315A87;
    a1 = ((((unsigned __int8)(v_stack_m1B8)) & (24)) == 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_003157C2;
    if (v_stack_m1C8 >= 3) goto loc_003157C2;
    goto loc_00315979;
loc_0031566C:
loc_00315670:
    if (v_stack_m98 == 0) goto loc_003156A6;
loc_0031567D:
    result = MiCrcStillIntact(v_stack_m1B8, (unsigned int)((unsigned int)(result)), v_stack_m98, 2);
    if ((unsigned int)(result) != 0) {
        *(unsigned __int64 *)(v_stack_m98) = v_r12;
        v_r12 = v_stack_m98;
    }
    if (*(unsigned __int64 *)(v_stack_m98) != 0) goto loc_0031567D;
loc_003156A6:
    v_stack_m98 = 0;
    if (v_stack_m70 == 0) goto loc_003156E8;
loc_003156BF:
    result = MiCrcStillIntact(v_stack_m1B8, (unsigned int)((unsigned int)(result)), v_stack_m70, 3);
    if ((unsigned int)(result) != 0) {
        *(unsigned __int64 *)(v_stack_m70) = v_r12;
        v_r12 = v_stack_m70;
    }
    if (*(unsigned __int64 *)(v_stack_m70) != 0) goto loc_003156BF;
loc_003156E8:
    v_rbx = 0;
    v_stack_m70 = 0;
    v_r13 = (unsigned int)((unsigned int)(result));
    if ((unsigned int)((unsigned int)(result)) != 0) {
        a1 = (unsigned int)((unsigned int)(result));
        result = MiFlushTbList(a1, (unsigned int)((unsigned int)(result)), v_stack_m70, 3);
        result = MiReleaseProcessorFlushList(a1, (unsigned int)((unsigned int)(result)), v_stack_m70, 3);
        v_r13 = 0;
        v_stack_m1D0 = 0;
        v_stack_m1C0 = 0;
    }
    result = v_stack_m1F0;
    if (v_stack_m1F0 != 0) {
        a2 = v_stack_m1F0;
        a1 = v_r15;
        result = MiUnlockPageTable(a1, a2, v_stack_m70, 3);
    }
    result = MiUnlockWorkingSetShared(v_r15, v_stack_m1D8, v_stack_m70, 3);
    result = MiFreeDeferredCrcPages(v_stack_mE8, v_stack_m1D8, v_stack_m70, 3);
    if (v_r12 == 0) goto loc_003159CB;
    goto loc_00315284;
loc_0031575E:
    if (result != 0) goto loc_00315D77;
    a4 = 0;
    result = MiLockLowestValidPageTableEx(v_stack_m1B0, v_r15, v_stack_m150, a4);
    v_stack_m1F0 = result;
    if (result == 0) goto loc_003153DF;
    result = MiUnlockPageTable(v_stack_m1B0, result, v_stack_m150, a4);
    a4 = 0;
    v_stack_m1F0 = 0;
    v_rbx = 0;
    goto loc_0031531A;
loc_003157B5:
loc_003157C2:
    if (v_stack_m160 != (*(unsigned __int64 *)(v_rip + 11672735))) goto loc_00315A87;
    result = MiPageMightBeZero(v_stack_m1B0, result + a1 * 8, v_stack_m1B0, a4);
    if ((unsigned int)(result) == 0) goto loc_00315A87;
    v_rbx = 0;
loc_003157EC:
    if (condition_is_below) goto loc_00315CC2;
    result = MiConfirmPageIsZero(result + a1 * 8, result + a1 * 8, v_stack_m1B0, a4);
    if ((unsigned int)(result) == 0) goto loc_00315A87;
    if (v_stack_m1C0 != 0) goto loc_00315F51;
    result = MiGetProcessorFlushList(result + a1 * 8, result + a1 * 8, v_stack_m1B0, a4);
    v_stack_m1C0 = result;
    v_rbp = 0;
loc_0031583C:
    *(unsigned int *)(result + 4136 + 16) = 2;
    *(unsigned int *)(result + 4136 + 20) = 1;
    *(unsigned __int64 *)(result + 4136) = v_stack_m1B0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1B0 + 184))) >> (8));
    result = (unsigned __int8)((result) >> (3));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int8 *)(result + 4160) = (unsigned __int8)(result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1B0 + 184)))) & (15)) != 0) goto loc_00315891;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    if (v_stack_m1B0 != a1) goto loc_00316076;
loc_00315891:
    a1 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1B0 + 184)))) & (15)) == 0) { a1 = 1; }
loc_0031589F:
    a4 = 0;
    *(unsigned int *)(result + 4144) = (unsigned int)(a1);
    *(unsigned __int16 *)(result + 4161) = 0;
    *(unsigned int *)(result + 4164) = 0;
    *(unsigned __int64 *)(result + 4168) = 0;
    *(unsigned __int64 *)(result + 4176) = 0;
    result = MiInsertTbFlushEntry(result + 4136, v_stack_m198, 1, a4);
    a3 = 0;
    result = MiFreeWsleList(v_stack_m1B0, result + 4136, a3, a4);
    if (1 != 0) {
        result = MiReleaseProcessorFlushList(v_stack_m1B0, result + 4136, a3, a4);
        v_stack_m1C0 = 0;
    }
loc_00315913:
    v_rbx = 0;
loc_00315915:
loc_0031591A:
loc_0031591F:
loc_00315923:
loc_0031592D:
    goto loc_0031531A;
loc_00315940:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 13302116)) & ((unsigned int)(v_rbx))) == 0) goto loc_00315FAB;
loc_0031594E:
loc_00315950:
    if (!sign_flag) goto loc_00315458;
    goto loc_00315940;
loc_0031595F:
    if (v_stack_m1C8 >= 8) goto loc_00315F7F;
loc_0031596F:
    if (2 == 4) goto loc_003157B5;
loc_00315979:
    if (v_stack_m1D0 == 0) goto loc_00315BE0;
loc_00315987:
    a4 = 0;
    result = MiInsertTbFlushEntry(v_stack_m1D0, v_stack_m198, a4 + 1, a4);
    *(unsigned __int64 *)(v_stack_m190) = *(unsigned __int64 *)(v_stack_mE8 + 2 + 2 * 4 * 8);
    *(unsigned __int64 *)(v_stack_mE8 + 2 + 2 * 4 * 8) = v_stack_m190;
loc_003159BF:
    v_rbx = 0;
loc_003159C1:
    goto loc_0031591F;
loc_003159CB:
    result = KiLeaveCriticalRegionUnsafe(v_stack_m158, v_stack_m198, a4 + 1, a4);
loc_003159E0:
    if (v_stack_m1A8 != 0) {
        a2 = 0;
        a1 = v_stack_m148;
        result = KeForceDetachProcess(a1, a2, a4 + 1, a4);
        a1 = v_stack_m1A0 + 1024;
        result = MiAttachThreadDone(a1, a2, a4 + 1, a4);
    }
    if (*(unsigned __int64 *)(v_stack_m1E8 + 304) == 0) goto loc_003160DF;
    result = MiReleaseFreshPage(*(unsigned __int64 *)(v_stack_m1E8 + 304), a2, a4 + 1, a4);
    v_rbx = 0;
    *(unsigned __int64 *)(v_stack_m1E8 + 304) = 0;
loc_00315A23:
    result = *(unsigned __int64 *)(v_stack_m1E8 + 296);
    if (*(unsigned __int64 *)(v_stack_m1E8 + 296) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1E8 + 296) + 24) = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_stack_m1E8 + 296);
        result = MiFreeCombineBlock(a1, a2, a4 + 1, a4);
        *(unsigned __int64 *)(v_stack_m1E8 + 296) = 0;
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a4 + 1, a4);
    v_rsp = (v_rsp) + (496);
    return result;
loc_00315A87:
    if (v_stack_pB8 == (*(unsigned __int64 *)(v_rip + 11641978))) goto loc_00315F47;
    if (((unsigned int)(v_stack_m1D0)) != 1) goto loc_00315F47;
    if (v_stack_pB8 != (*(unsigned __int64 *)(v_stack_p78 + 864))) goto loc_00315913;
    if (((*(unsigned int *)(v_stack_p88 + 1876)) & (0x1000ULL)) != 0) goto loc_00315913;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p88 + 1956)))) != ((unsigned int)(v_stack_m1D0))) goto loc_003160B9;
loc_00315AED:
    v_rbx = 0;
    if ((((unsigned __int8)(v_stack_m1E8)) & (24)) == 0) goto loc_00315B2D;
    result = MiGetUltraMapping(v_stack_p40 + 256, 3, 3 - 1, 3 + 1);
    *(unsigned __int64 *)(v_stack_p40 + 96) = result;
    goto loc_00315B59;
loc_00315B1B:
loc_00315B2D:
    result = MiGetUltraMapping(v_stack_p40 + 256, 3, 3 - 1, 3 + 1);
    *(unsigned __int64 *)(v_stack_p40 + 96) = result;
    if (((unsigned __int8)(v_stack_m1E0)) != 6) goto loc_00315D13;
loc_00315B59:
    if (v_stack_p58 == 0) goto loc_00315C85;
loc_00315B67:
    result = MiConvertPrivateToProto(v_stack_p40, v_stack_p98, v_stack_p58, 3 + 1);
    if (sign_flag) goto loc_00315D58;
    *(unsigned __int64 *)(v_stack_p98) = v_stack_p140;
    *(unsigned __int64 *)(v_stack_p40 + 96) = 0;
    v_stack_p140 = v_stack_p98;
loc_00315BA0:
    if (v_stack_p88 == 0) goto loc_0031592D;
    goto loc_0031531A;
loc_00315BE0:
    result = v_stack_p88;
    if (v_stack_p68 == 0) {
        result = MiGetProcessorFlushList(v_stack_p48, v_stack_p98, v_stack_p68, v_stack_p38);
        a3 = result;
        v_stack_p68 = result;
    }
    a4 = 0;
    *(unsigned int *)(a3 + 16) = 0;
    *(unsigned int *)(a3 + 20) = 128;
    *(unsigned __int64 *)(a3) = v_stack_p78;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p78 + 184))) >> (8));
    a1 = (unsigned __int8)((a1) >> (3));
    a1 = (unsigned __int8)((a1) & (1));
    v_stack_p58 = a3;
    *(unsigned __int8 *)(a3 + 24) = (unsigned __int8)(a1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p78 + 184)))) & (15)) != 0) goto loc_00315C53;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    if (v_stack_p78 != a1) goto loc_003160AC;
loc_00315C53:
    a1 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p78 + 184)))) & (15)) == 0) { a1 = 1; }
loc_00315C66:
    *(unsigned int *)(a3 + 8) = (unsigned int)(a1);
    *(unsigned __int16 *)(a3 + 25) = 0;
    *(unsigned int *)(a3 + 28) = 0;
    *(unsigned __int64 *)(a3 + 32) = 0;
    *(unsigned __int64 *)(a3 + 40) = 0;
    goto loc_00315987;
loc_00315C85:
    result = v_stack_p68;
    if (v_stack_p68 == 0) {
        result = MiGetProcessorFlushList(a1, v_stack_p78, a3, a4);
        v_stack_p68 = result;
    }
    a4 = 0;
    v_stack_p58 = result;
    v_stack_p20 = 128;
    result = MiInitializeTbFlushList(result, v_stack_p78, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    goto loc_00315B67;
loc_00315CC2:
    v_rbx = (unsigned int)((1) + 1);
    if (((*(unsigned int *)(v_rip + 13301218)) & ((unsigned int)(v_rbx))) == 0) goto loc_00315FE6;
loc_00315CD0:
loc_00315CD2:
    if (!sign_flag) goto loc_003157EC;
    goto loc_00315CC2;
loc_00315CE1:
    result = MiUnlockWorkingSetShared(v_stack_p78, (unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12))), (unsigned int)(*(unsigned int *)(result + 12)), a4);
    result = KiLeaveCriticalRegionUnsafe(v_stack_pD0, (unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12))), (unsigned int)(*(unsigned int *)(result + 12)), a4);
    goto loc_003159E0;
loc_00315CFF:
    goto loc_00315913;
loc_00315D13:
    if (v_stack_p78 != (*(unsigned __int64 *)(v_rip + 11641319))) goto loc_00315EE9;
loc_00315D2F:
    v_rbx = (unsigned __int8)(v_rbx);
    if ((((unsigned __int8)(v_stack_p40)) & (24)) != 0) { v_rbx = 1; }
    result = MiConvertStandbyToProto(v_stack_p40, v_stack_p98, (unsigned int)(*(unsigned int *)(result + 12)), a4);
loc_00315D58:
    *(unsigned __int64 *)(v_stack_p40 + 96) = 0;
    if (!sign_flag) goto loc_00315BA0;
    goto loc_0031591F;
loc_00315D6D:
    v_stack_p34 = (unsigned __int8)(v_stack_p98);
    goto loc_00315365;
loc_00315D77:
    v_stack_p34 = 1;
    v_rbx = 0;
    goto loc_0031531A;
loc_00315D8E:
    v_rbx = 0;
    result = (unsigned int)((v_stack_p98) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_00315923;
loc_00315DA4:
    result = MI_READ_PTE_LOCK_FREE(v_stack_p78, v_stack_p98, (unsigned int)(*(unsigned int *)(result + 12)), result);
    if (result >= 0x800ULL) goto loc_003159BF;
    result = MiInvalidPteConforms(result, v_stack_p98, (unsigned int)(*(unsigned int *)(result + 12)), result);
    if ((unsigned int)(result) == 0) goto loc_00315DA4;
    if (*(unsigned __int64 *)(v_rip + 11632307) == 0) goto loc_00315DE4;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_00315F3E;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11632307));
    a1 = (a1) & (result);
loc_00315DE4:
    a1 = (a1) >> (12);
    a1 = (a1) & (*(unsigned __int64 *)(v_rip + 11632307));
    a2 = (a1 + a1 * 2) + (a1 + a1 * 2);
    if (a1 > (*(unsigned __int64 *)(v_rip + 11632336))) goto loc_00315DA4;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11632307) + a2 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_00315DA4;
    v_rbp = 0;
loc_00315E37:
    if (condition_is_below) goto loc_00315F60;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p78, a2, (unsigned int)(*(unsigned int *)(result + 12)), result);
    if (result != result) goto loc_00315FD2;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11632307) + a2 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_0031602D;
loc_00315E78:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11632307) + a2 * 8 + 8)) | (*(unsigned __int64 *)(v_rip + 11641384));
    if (result != v_stack_p78) goto loc_00316048;
loc_00315E92:
    v_rbx = 0;
    if (*(unsigned __int64 *)(v_rip + 11632307) + a2 * 8 == 0) goto loc_003159C1;
    v_r14 = (*(unsigned __int64 *)(v_rip + 11632307) + a2 * 8) - (result);
    v_r14 = (v_r14) >> (4);
    v_r14 = (v_r14) * (result);
    goto loc_00315465;
loc_00315EC7:
    a1 = v_stack_p48;
    if (((unsigned int)(result)) == 0xC000022DULL) { a1 = v_stack_p48; }
    v_rbx = 0;
    goto loc_0031531A;
loc_00315EE9:
    if (((unsigned int)(v_stack_p58)) != 1) goto loc_00315D2F;
    result = MiGetCombineDomain((unsigned int)((unsigned int)(v_stack_p58)), v_stack_p78, (unsigned int)(*(unsigned int *)(result + 12)), v_stack_p38);
    if (v_stack_p78 != result) goto loc_00315F2C;
    if (((*(unsigned int *)(v_stack_p88 + 1876)) & (0x1000ULL)) != 0) goto loc_00315F2C;
    result = MiCheckProcessCombineSequence(v_stack_p88, (unsigned int)(*(unsigned int *)(v_stack_p98 + 288)), (unsigned int)(*(unsigned int *)(result + 12)), v_stack_p38);
    if ((unsigned int)(result) != 0) goto loc_00315D2F;
loc_00315F2C:
    *(unsigned __int64 *)(v_stack_p40 + 96) = 0;
    goto loc_0031591A;
loc_00315F3E:
    a1 = (v_stack_p88) & (-17);
    goto loc_00315DE4;
loc_00315F47:
    goto loc_00315AED;
loc_00315F51:
    v_rbp = 0;
    goto loc_0031583C;
loc_00315F60:
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((*(unsigned int *)(v_rip + 13300548)) & ((unsigned int)(v_rbp))) == 0) goto loc_00316085;
loc_00315F6E:
loc_00315F70:
    if (!sign_flag) goto loc_00315E37;
    goto loc_00315F60;
loc_00315F7F:
    result = MiMakeCombineCandidateClean(v_stack_p78, v_stack_p40, (unsigned int)(*(unsigned int *)(result + 12)), v_stack_p38);
    a2 = 0;
    a2 = (((unsigned int)(v_stack_p58)) != 1) ? 1 : 0;
    result = MiFlushSingleTbEntry(v_stack_p90, a2, 10, v_stack_p38);
    goto loc_0031596F;
loc_00315FAB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13306631)))) & (64)) == 0) goto loc_0031594E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p90, a2, 10, v_stack_p38);
    if ((unsigned __int8)(result) == 0) goto loc_0031594E;
    result = HvlNotifyLongSpinWait(0, a2, 10, v_stack_p38);
    goto loc_00315950;
loc_00315FD2:
    goto loc_00315DA4;
loc_00315FE6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13306572)))) & (64)) == 0) goto loc_00315CD0;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, a2, 10, v_stack_p38);
    if ((unsigned __int8)(result) == 0) goto loc_00315CD0;
    result = HvlNotifyLongSpinWait(0, a2, 10, v_stack_p38);
    goto loc_00315CD2;
loc_0031600D:
    a3 = 0;
    result = MiReplenishSlabAllocator(0, a3 + 16, a3, v_stack_p38);
    a1 = ((unsigned int)(result) == 0) ? 1 : 0;
    *(unsigned __int64 *)(v_stack_p40 + 312) = a1;
    goto loc_003152B5;
loc_0031602D:
    a2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(v_stack_p40, a2, a3, v_stack_p38);
    if (result == 0) goto loc_003159BF;
    goto loc_00315E78;
loc_00316048:
    if (condition_is_below) goto loc_00315E92;
    v_stack_p20 = *(unsigned __int64 *)(result + 8);
    result = KeBugCheckEx(26, (unsigned int)(0x411ULL), v_stack_p78, 0);
loc_00316076:
    goto loc_0031589F;
loc_00316085:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13306413)))) & (64)) == 0) goto loc_00315F6E;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbp)), (unsigned int)(0x411ULL), v_stack_p78, 0);
    if ((unsigned __int8)(result) == 0) goto loc_00315F6E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), (unsigned int)(0x411ULL), v_stack_p78, 0);
    goto loc_00315F70;
loc_003160AC:
    goto loc_00315C66;
loc_003160B9:
    if (((unsigned int)(result)) == 0) goto loc_00315AED;
    if (((unsigned int)(result)) >= 2) goto loc_00315913;
    result = 0;
    if (condition_is_equal) goto loc_00315AED;
    goto loc_00315913;
loc_003160DF:
    v_rbx = 0;
    goto loc_00315A23;
loc_003160E6:
    a2 = 0;
    result = MiWorkingSetIsContended(v_stack_p78, a2, v_stack_p78, 0);
    if ((unsigned int)(result) != 0) goto loc_00315365;
    if (0 == 0) goto loc_0031535C;
    result = MiPageTableLockIsContended(v_stack_p78, 0, v_stack_p78, 0);
    if ((unsigned int)(result) != 0) goto loc_00315365;
    goto loc_0031535C;
loc_00316119:
    v_rbx = 0;
loc_0031611B:
    goto loc_0031531A;
}
```

## 5. (Beta) C Style

```c
int64_t MiSharePages(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint8_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint8_t v_stack_m1F4;
    uint32_t v_stack_m1F8;
    uint64_t v_stack_m48;
    uint64_t v_stack_m70;
    uint64_t v_stack_m98;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p140;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint8_t v_stack_p34;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pD0;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (496);
    result = (*(uint64_t *)(v_rip + 0xAF5612)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rdi = 0;
    v_stack_m168 = *(uint64_t *)(arg1);
    v_stack_m188 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8C)));
    v_stack_m1E8 = Arg1;
    v_stack_m180 = *(uint64_t *)(arg1 + 0x68);
    Arg3 = (uint32_t)((Arg3) + 1);
    v_stack_m1C8 = 0;
    v_stack_m148 = v_xmm0;
    v_stack_m178 = 0;
    v_stack_m138 = v_xmm0;
    v_stack_m1B0 = *(uint64_t *)(arg2 + 0x20);
    v_stack_m128 = v_xmm0;
    result = MiInitializePageColorBase(*(uint64_t *)(arg2 + 0x20), local_rdi + 3, Arg3, Arg1 + 320);
    v_stack_m1A8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1A0 = *(uint64_t *)(arg2 + 0x28);
    if (*(uint64_t *)(arg2 + 0x28) == 0) goto loc_00315262;
    if ((*(uint64_t *)(arg2 + 0x28)) == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) goto loc_00315262;
    result = ExAcquireSpinLockExclusive(v_rip + 11674310, local_rdi + 3, Arg3, Arg1 + 320);
    result = MiPrepareAttachThread(*(uint64_t *)(arg2 + 0x28), *(uint64_t *)(arg2 + 0x28) + 1024, Arg3, (uint8_t)(result));
    v_stack_m1A8 = (uint32_t)(result);
    result = MiReleaseSpinLockExclusive(v_rip + 11674268, (uint8_t)((uint8_t)(result)), Arg3, (uint8_t)(result));
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00315A05;
    v_stack_m118 = v_xmm0;
    v_stack_m108 = v_xmm0;
    v_stack_mF8 = v_xmm0;
    result = KiStackAttachProcess(*(uint64_t *)(arg2 + 0x28), 0 + 1, v_stack_m148, (uint8_t)(result));
loc_00315262:
    local_rbx = 0;
    *(uint64_t *)(arg1 + 0x138) = 0;
    v_stack_m158 = *(uint64_t *)(gs_base + (0 + 0x188));
loc_00315284:
    v_stack_mE8 = 0;
    v_stack_mC0 = 0;
    v_stack_m98 = 0;
    v_stack_m70 = 0;
    if ((*(uint64_t *)(arg1 + 0x138)) > 1) goto loc_0031600D;
loc_003152B5:
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(arg1 + 0x128)) == 0) {
        Arg1 = v_stack_m168;
        result = MiAllocateCombineBlock(Arg1, 0 + 1, v_stack_m148, (uint8_t)(result));
        *(uint64_t *)(arg1 + 0x128) = result;
    }
    local_rbx = 0;
    v_stack_m1F0 = 0;
    v_stack_m1F4 = 0;
    result = MiLockWorkingSetShared(*(uint64_t *)(arg2 + 0x20), 0 + 1, v_stack_m148, (uint8_t)(result));
    v_stack_m1D8 = (uint8_t)(result);
    if ((*(uint64_t *)(arg1 + 0x128)) == 0) goto loc_00315CE1;
    if (*(uint64_t *)(arg2 + 0x28) == 0) goto loc_00315315;
    result = MiProcessSuitableForCombining(*(uint64_t *)(arg2 + 0x28), 0 + 1, (uint8_t)(result), (uint8_t)(result));
    if ((uint32_t)(result) == 0) goto loc_00315CE1;
loc_00315315:
loc_0031531A:
    v_stack_m190 = *(uint64_t *)(arg2 + 0x30);
    local_rbp = 0;
    local_rdi = 0;
    if (0 == 0) { local_rbp = (uint32_t)(0 + 1); }
    v_stack_m1F8 = (uint32_t)(local_rbp);
    if ((*(uint64_t *)(arg1 + 0x128)) == 0) goto loc_00315365;
    if ((*(uint64_t *)(arg1 + 0x138)) > 1) goto loc_00315365;
    if (v_stack_m1F4 != 0) goto loc_00315D6D;
    if ((((uint8_t)(local_rbp)) & (7)) == 0) goto loc_003160E6;
loc_0031535C:
    result = KeShouldYieldProcessor(*(uint64_t *)(arg2 + 0x28), 0 + 1, (uint8_t)(result), v_stack_m1F0);
    if ((uint32_t)(result) != 0) {
        local_rdi = 1;
    }
    if (*(uint64_t *)(arg2 + 0x30) == 0) goto loc_0031566C;
    if ((uint8_t)(local_rdi) != 0) goto loc_00315670;
    v_stack_m1E0 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x30));
    local_r15 = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x30) + 0x10)) >> (9);
    local_r15 = (local_r15) & ((uint8_t)(result));
    v_stack_m198 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x30) + 0x10);
    v_stack_m160 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x30) + 0x8);
    local_r15 = (local_r15) + (0 + 1);
    local_rbx = (local_r15) >> (9);
    local_rbx = (local_rbx) & ((uint8_t)(result));
    local_rbx = (local_rbx) + (0 + 1);
    if (v_stack_m1F0 != local_rbx) goto loc_0031575E;
loc_003153DF:
    result = MiReplenishCombineResources(Arg1, 0 + 1, (uint8_t)(result), v_stack_m1F0);
    if (sign_flag) goto loc_00315EC7;
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) == 0) goto loc_00315D8E;
    local_r14 = (*(uint64_t *)(local_r15)) >> (12);
    local_r14 = (local_r14) & (result);
    if (local_r14 > (*(uint64_t *)(v_rip + 0xB188C9))) goto loc_00316119;
    Arg1 = (local_r14 + local_r14 * 2) + (local_r14 + local_r14 * 2);
    result = (*(uint64_t *)(result + arg1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_0031611B;
    local_rbx = 0;
loc_00315458:
    if (condition_is_below) goto loc_00315940;
loc_00315465:
    result = MiCombineCandidate(v_stack_m168, (uint32_t)(v_stack_m188), result + Arg1 * 8, v_stack_m1F0);
    if ((uint32_t)(result) == 0) goto loc_00315CFF;
    *(uint64_t *)(v_stack_m1E8 + 0x90) = local_r14;
    *(uint32_t *)(v_stack_m1E8 + 0x98) = (uint32_t)((uint32_t)((uint32_t)(result)));
    Arg1 = (*(uint64_t *)(result + arg1 * 8 + 0x10)) >> (5);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x30) + 0x20))))) ^ ((uint32_t)(Arg1)));
    v_stack_m1B8 = Arg1;
    Arg2 = (uint32_t)((Arg2) & (31));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x30) + 0x20)))));
    v_stack_m170 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x30) + 0x18);
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x30) + 0x20) = (uint32_t)(Arg2);
    result = MiPageToNode(local_r14, Arg2, result + Arg1 * 8, v_stack_m1F0);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(Arg3)))) goto loc_00315CFF;
    local_rbx = 0;
    local_r12 = (uint8_t)((*(uint8_t *)(result + arg1 * 8 + 0x22)) & (7));
    if (((uint8_t)(local_r12)) != 6) goto loc_00315B1B;
    result = (*(uint64_t *)(result + arg1 * 8 + 0x8)) | (local_r14);
    if (local_r15 != result) goto loc_00315915;
    if (sign_flag) goto loc_00315915;
    if (condition_is_below) goto loc_00315915;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + arg1 * 8 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_00315915;
    result = (*(uint64_t *)(result + arg1 * 8 + 0x28)) & (local_r14);
    if (result == local_r14) goto loc_00315915;
    Arg2 = (local_r15) << (25);
    result = (result) << (25);
    Arg2 = (Arg2) - (result);
    Arg2 = (Arg2) >> (16);
    result = MiGetWsleContents(local_r14, Arg2, result + Arg1 * 8, v_stack_m1F0);
    result = (uint8_t)((result) & (15));
    if (((uint8_t)(result)) == 8) goto loc_00315915;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(result + arg1 * 8 + 0x20)))) != 1) goto loc_00315915;
    local_r14 = 0;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 1) goto loc_00315618;
    result = MiLockVadTree((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg2, result + Arg1 * 8, v_stack_m1F0);
    result = MiLocateAddress(v_stack_m198, Arg2, result + Arg1 * 8, v_stack_m1F0);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410)) + (0x3ECULL);
    result = ExReleaseSpinLockSharedFromDpcLevel(Arg1, Arg2, result + Arg1 * 8, v_stack_m1F0);
    if (result == 0) goto loc_00315915;
    result = ((uint32_t)(*(uint32_t *)(result + 0x30))) >> (19);
    result = (uint32_t)((result) & (3));
    if ((*(uint64_t *)(v_rip - 0x30107E + result * 8)) == 16) goto loc_00315915;
    result = MiVadSupportsPrivateCommit(result, Arg2, result + Arg1 * 8, v_stack_m1F0);
    if ((uint32_t)(result) == 0) goto loc_00315915;
loc_00315618:
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (66)) != 0) goto loc_0031595F;
    if (v_stack_m160 != (*(uint64_t *)(v_rip + 0xB21E32))) goto loc_00315A87;
    Arg1 = ((((uint8_t)(v_stack_m1B8)) & (24)) == 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(local_r15))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_003157C2;
    if (v_stack_m1C8 >= 3) goto loc_003157C2;
    goto loc_00315979;
loc_0031566C:
loc_00315670:
    if (v_stack_m98 == 0) goto loc_003156A6;
loc_0031567D:
    result = MiCrcStillIntact(v_stack_m1B8, (uint32_t)((uint32_t)(result)), v_stack_m98, 2);
    if ((uint32_t)(result) != 0) {
        *(uint64_t *)(v_stack_m98) = local_r12;
        local_r12 = v_stack_m98;
    }
    if (*(uint64_t *)(v_stack_m98) != 0) goto loc_0031567D;
loc_003156A6:
    v_stack_m98 = 0;
    if (v_stack_m70 == 0) goto loc_003156E8;
loc_003156BF:
    result = MiCrcStillIntact(v_stack_m1B8, (uint32_t)((uint32_t)(result)), v_stack_m70, 3);
    if ((uint32_t)(result) != 0) {
        *(uint64_t *)(v_stack_m70) = local_r12;
        local_r12 = v_stack_m70;
    }
    if (*(uint64_t *)(v_stack_m70) != 0) goto loc_003156BF;
loc_003156E8:
    local_rbx = 0;
    v_stack_m70 = 0;
    local_r13 = (uint32_t)((uint32_t)(result));
    if ((uint32_t)((uint32_t)(result)) != 0) {
        Arg1 = (uint32_t)((uint32_t)(result));
        result = MiFlushTbList(Arg1, (uint32_t)((uint32_t)(result)), v_stack_m70, 3);
        result = MiReleaseProcessorFlushList(Arg1, (uint32_t)((uint32_t)(result)), v_stack_m70, 3);
        local_r13 = 0;
        v_stack_m1D0 = 0;
        v_stack_m1C0 = 0;
    }
    result = v_stack_m1F0;
    if (v_stack_m1F0 != 0) {
        Arg2 = v_stack_m1F0;
        Arg1 = local_r15;
        result = MiUnlockPageTable(Arg1, Arg2, v_stack_m70, 3);
    }
    result = MiUnlockWorkingSetShared(local_r15, v_stack_m1D8, v_stack_m70, 3);
    result = MiFreeDeferredCrcPages(v_stack_mE8, v_stack_m1D8, v_stack_m70, 3);
    if (local_r12 == 0) goto loc_003159CB;
    goto loc_00315284;
loc_0031575E:
    if (result != 0) goto loc_00315D77;
    a4 = 0;
    result = MiLockLowestValidPageTableEx(v_stack_m1B0, local_r15, v_stack_m150, a4);
    v_stack_m1F0 = result;
    if (result == 0) goto loc_003153DF;
    result = MiUnlockPageTable(v_stack_m1B0, result, v_stack_m150, a4);
    a4 = 0;
    v_stack_m1F0 = 0;
    local_rbx = 0;
    goto loc_0031531A;
loc_003157B5:
loc_003157C2:
    if (v_stack_m160 != (*(uint64_t *)(v_rip + 0xB21C9F))) goto loc_00315A87;
    result = MiPageMightBeZero(v_stack_m1B0, result + Arg1 * 8, v_stack_m1B0, a4);
    if ((uint32_t)(result) == 0) goto loc_00315A87;
    local_rbx = 0;
loc_003157EC:
    if (condition_is_below) goto loc_00315CC2;
    result = MiConfirmPageIsZero(result + Arg1 * 8, result + Arg1 * 8, v_stack_m1B0, a4);
    if ((uint32_t)(result) == 0) goto loc_00315A87;
    if (v_stack_m1C0 != 0) goto loc_00315F51;
    result = MiGetProcessorFlushList(result + Arg1 * 8, result + Arg1 * 8, v_stack_m1B0, a4);
    v_stack_m1C0 = result;
    local_rbp = 0;
loc_0031583C:
    *(uint32_t *)(result + 0x1028 + 0x10) = 2;
    *(uint32_t *)(result + 0x1028 + 0x14) = 1;
    *(uint64_t *)(result + 0x1028) = v_stack_m1B0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0xB8))) >> (8));
    result = (uint8_t)((result) >> (3));
    result = (uint8_t)((result) & (1));
    *(uint8_t *)(result + 0x1040) = (uint8_t)(result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0xB8)))) & (15)) != 0) goto loc_00315891;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    if (v_stack_m1B0 != Arg1) goto loc_00316076;
loc_00315891:
    Arg1 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1B0 + 0xB8)))) & (15)) == 0) { Arg1 = 1; }
loc_0031589F:
    a4 = 0;
    *(uint32_t *)(result + 0x1030) = (uint32_t)(Arg1);
    *(uint16_t *)(result + 0x1041) = 0;
    *(uint32_t *)(result + 0x1044) = 0;
    *(uint64_t *)(result + 0x1048) = 0;
    *(uint64_t *)(result + 0x1050) = 0;
    result = MiInsertTbFlushEntry(result + 4136, v_stack_m198, 1, a4);
    Arg3 = 0;
    result = MiFreeWsleList(v_stack_m1B0, result + 4136, Arg3, a4);
    if (1 != 0) {
        result = MiReleaseProcessorFlushList(v_stack_m1B0, result + 4136, Arg3, a4);
        v_stack_m1C0 = 0;
    }
loc_00315913:
    local_rbx = 0;
loc_00315915:
loc_0031591A:
loc_0031591F:
loc_00315923:
loc_0031592D:
    goto loc_0031531A;
loc_00315940:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xCAF964)) & ((uint32_t)(local_rbx))) == 0) goto loc_00315FAB;
loc_0031594E:
loc_00315950:
    if (!sign_flag) goto loc_00315458;
    goto loc_00315940;
loc_0031595F:
    if (v_stack_m1C8 >= 8) goto loc_00315F7F;
loc_0031596F:
    if (2 == 4) goto loc_003157B5;
loc_00315979:
    if (v_stack_m1D0 == 0) goto loc_00315BE0;
loc_00315987:
    a4 = 0;
    result = MiInsertTbFlushEntry(v_stack_m1D0, v_stack_m198, a4 + 1, a4);
    *(uint64_t *)(v_stack_m190) = *(uint64_t *)(v_stack_mE8 + 0x2 + 0x2 * 4 * 8);
    *(uint64_t *)(v_stack_mE8 + 0x2 + 0x2 * 4 * 8) = v_stack_m190;
loc_003159BF:
    local_rbx = 0;
loc_003159C1:
    goto loc_0031591F;
loc_003159CB:
    result = KiLeaveCriticalRegionUnsafe(v_stack_m158, v_stack_m198, a4 + 1, a4);
loc_003159E0:
    if (v_stack_m1A8 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m148;
        result = KeForceDetachProcess(Arg1, Arg2, a4 + 1, a4);
        Arg1 = v_stack_m1A0 + 1024;
        result = MiAttachThreadDone(Arg1, Arg2, a4 + 1, a4);
    }
    if (*(uint64_t *)(v_stack_m1E8 + 0x130) == 0) goto loc_003160DF;
    result = MiReleaseFreshPage(*(uint64_t *)(v_stack_m1E8 + 0x130), Arg2, a4 + 1, a4);
    local_rbx = 0;
    *(uint64_t *)(v_stack_m1E8 + 0x130) = 0;
loc_00315A23:
    result = *(uint64_t *)(v_stack_m1E8 + 0x128);
    if (*(uint64_t *)(v_stack_m1E8 + 0x128) != 0) {
        *(uint64_t *)(*(uint64_t *)(v_stack_m1E8 + 0x128) + 0x18) = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_stack_m1E8 + 0x128);
        result = MiFreeCombineBlock(Arg1, Arg2, a4 + 1, a4);
        *(uint64_t *)(v_stack_m1E8 + 0x128) = 0;
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a4 + 1, a4);
    local_rsp = (local_rsp) + (496);
    return result;
loc_00315A87:
    if (v_stack_pB8 == (*(uint64_t *)(v_rip + 0xB1A47A))) goto loc_00315F47;
    if (((uint32_t)(v_stack_m1D0)) != 1) goto loc_00315F47;
    if (v_stack_pB8 != (*(uint64_t *)(v_stack_p78 + 0x360))) goto loc_00315913;
    if (((*(uint32_t *)(v_stack_p88 + 0x754)) & (0x1000ULL)) != 0) goto loc_00315913;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p88 + 0x7A4)))) != ((uint32_t)(v_stack_m1D0))) goto loc_003160B9;
loc_00315AED:
    local_rbx = 0;
    if ((((uint8_t)(v_stack_m1E8)) & (24)) == 0) goto loc_00315B2D;
    result = MiGetUltraMapping(v_stack_p40 + 256, 3, 3 - 1, 3 + 1);
    *(uint64_t *)(v_stack_p40 + 0x60) = result;
    goto loc_00315B59;
loc_00315B1B:
loc_00315B2D:
    result = MiGetUltraMapping(v_stack_p40 + 256, 3, 3 - 1, 3 + 1);
    *(uint64_t *)(v_stack_p40 + 0x60) = result;
    if (((uint8_t)(v_stack_m1E0)) != 6) goto loc_00315D13;
loc_00315B59:
    if (v_stack_p58 == 0) goto loc_00315C85;
loc_00315B67:
    result = MiConvertPrivateToProto(v_stack_p40, v_stack_p98, v_stack_p58, 3 + 1);
    if (sign_flag) goto loc_00315D58;
    *(uint64_t *)(v_stack_p98) = v_stack_p140;
    *(uint64_t *)(v_stack_p40 + 0x60) = 0;
    v_stack_p140 = v_stack_p98;
loc_00315BA0:
    if (v_stack_p88 == 0) goto loc_0031592D;
    goto loc_0031531A;
loc_00315BE0:
    result = v_stack_p88;
    if (v_stack_p68 == 0) {
        result = MiGetProcessorFlushList(v_stack_p48, v_stack_p98, v_stack_p68, v_stack_p38);
        Arg3 = result;
        v_stack_p68 = result;
    }
    a4 = 0;
    *(uint32_t *)(Arg3 + 0x10) = 0;
    *(uint32_t *)(Arg3 + 0x14) = 128;
    *(uint64_t *)(Arg3) = v_stack_p78;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p78 + 0xB8))) >> (8));
    Arg1 = (uint8_t)((Arg1) >> (3));
    Arg1 = (uint8_t)((Arg1) & (1));
    v_stack_p58 = Arg3;
    *(uint8_t *)(Arg3 + 0x18) = (uint8_t)(Arg1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p78 + 0xB8)))) & (15)) != 0) goto loc_00315C53;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    if (v_stack_p78 != Arg1) goto loc_003160AC;
loc_00315C53:
    Arg1 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p78 + 0xB8)))) & (15)) == 0) { Arg1 = 1; }
loc_00315C66:
    *(uint32_t *)(Arg3 + 0x8) = (uint32_t)(Arg1);
    *(uint16_t *)(Arg3 + 0x19) = 0;
    *(uint32_t *)(Arg3 + 0x1C) = 0;
    *(uint64_t *)(Arg3 + 0x20) = 0;
    *(uint64_t *)(Arg3 + 0x28) = 0;
    goto loc_00315987;
loc_00315C85:
    result = v_stack_p68;
    if (v_stack_p68 == 0) {
        result = MiGetProcessorFlushList(Arg1, v_stack_p78, Arg3, a4);
        v_stack_p68 = result;
    }
    a4 = 0;
    v_stack_p58 = result;
    v_stack_p20 = 128;
    result = MiInitializeTbFlushList(result, v_stack_p78, (uint32_t)(*(uint32_t *)(result + 0xC)), a4);
    goto loc_00315B67;
loc_00315CC2:
    local_rbx = (uint32_t)((1) + 1);
    if (((*(uint32_t *)(v_rip + 0xCAF5E2)) & ((uint32_t)(local_rbx))) == 0) goto loc_00315FE6;
loc_00315CD0:
loc_00315CD2:
    if (!sign_flag) goto loc_003157EC;
    goto loc_00315CC2;
loc_00315CE1:
    result = MiUnlockWorkingSetShared(v_stack_p78, (uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC))), (uint32_t)(*(uint32_t *)(result + 0xC)), a4);
    result = KiLeaveCriticalRegionUnsafe(v_stack_pD0, (uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC))), (uint32_t)(*(uint32_t *)(result + 0xC)), a4);
    goto loc_003159E0;
loc_00315CFF:
    goto loc_00315913;
loc_00315D13:
    if (v_stack_p78 != (*(uint64_t *)(v_rip + 0xB1A1E7))) goto loc_00315EE9;
loc_00315D2F:
    local_rbx = (uint8_t)(local_rbx);
    if ((((uint8_t)(v_stack_p40)) & (24)) != 0) { local_rbx = 1; }
    result = MiConvertStandbyToProto(v_stack_p40, v_stack_p98, (uint32_t)(*(uint32_t *)(result + 0xC)), a4);
loc_00315D58:
    *(uint64_t *)(v_stack_p40 + 0x60) = 0;
    if (!sign_flag) goto loc_00315BA0;
    goto loc_0031591F;
loc_00315D6D:
    v_stack_p34 = (uint8_t)(v_stack_p98);
    goto loc_00315365;
loc_00315D77:
    v_stack_p34 = 1;
    local_rbx = 0;
    goto loc_0031531A;
loc_00315D8E:
    local_rbx = 0;
    result = (uint32_t)((v_stack_p98) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_00315923;
loc_00315DA4:
    result = MI_READ_PTE_LOCK_FREE(v_stack_p78, v_stack_p98, (uint32_t)(*(uint32_t *)(result + 0xC)), result);
    if (result >= 0x800ULL) goto loc_003159BF;
    result = MiInvalidPteConforms(result, v_stack_p98, (uint32_t)(*(uint32_t *)(result + 0xC)), result);
    if ((uint32_t)(result) == 0) goto loc_00315DA4;
    if (*(uint64_t *)(v_rip + 0xB17EB3) == 0) goto loc_00315DE4;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_00315F3E;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xB17EB3));
    Arg1 = (Arg1) & (result);
loc_00315DE4:
    Arg1 = (Arg1) >> (12);
    Arg1 = (Arg1) & (*(uint64_t *)(v_rip + 0xB17EB3));
    Arg2 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xB17ED0))) goto loc_00315DA4;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB17EB3) + arg2 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_00315DA4;
    local_rbp = 0;
loc_00315E37:
    if (condition_is_below) goto loc_00315F60;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p78, Arg2, (uint32_t)(*(uint32_t *)(result + 0xC)), result);
    if (result != result) goto loc_00315FD2;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB17EB3) + arg2 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_0031602D;
loc_00315E78:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB17EB3) + arg2 * 8 + 0x8)) | (*(uint64_t *)(v_rip + 0xB1A228));
    if (result != v_stack_p78) goto loc_00316048;
loc_00315E92:
    local_rbx = 0;
    if (*(uint64_t *)(v_rip + 0xB17EB3) + Arg2 * 8 == 0) goto loc_003159C1;
    local_r14 = (*(uint64_t *)(v_rip + 0xB17EB3) + Arg2 * 8) - (result);
    local_r14 = (local_r14) >> (4);
    local_r14 = (local_r14) * (result);
    goto loc_00315465;
loc_00315EC7:
    Arg1 = v_stack_p48;
    if (((uint32_t)(result)) == 0xC000022DULL) { Arg1 = v_stack_p48; }
    local_rbx = 0;
    goto loc_0031531A;
loc_00315EE9:
    if (((uint32_t)(v_stack_p58)) != 1) goto loc_00315D2F;
    result = MiGetCombineDomain((uint32_t)((uint32_t)(v_stack_p58)), v_stack_p78, (uint32_t)(*(uint32_t *)(result + 0xC)), v_stack_p38);
    if (v_stack_p78 != result) goto loc_00315F2C;
    if (((*(uint32_t *)(v_stack_p88 + 0x754)) & (0x1000ULL)) != 0) goto loc_00315F2C;
    result = MiCheckProcessCombineSequence(v_stack_p88, (uint32_t)(*(uint32_t *)(v_stack_p98 + 0x120)), (uint32_t)(*(uint32_t *)(result + 0xC)), v_stack_p38);
    if ((uint32_t)(result) != 0) goto loc_00315D2F;
loc_00315F2C:
    *(uint64_t *)(v_stack_p40 + 0x60) = 0;
    goto loc_0031591A;
loc_00315F3E:
    Arg1 = (v_stack_p88) & (-17);
    goto loc_00315DE4;
loc_00315F47:
    goto loc_00315AED;
loc_00315F51:
    local_rbp = 0;
    goto loc_0031583C;
loc_00315F60:
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((*(uint32_t *)(v_rip + 0xCAF344)) & ((uint32_t)(local_rbp))) == 0) goto loc_00316085;
loc_00315F6E:
loc_00315F70:
    if (!sign_flag) goto loc_00315E37;
    goto loc_00315F60;
loc_00315F7F:
    result = MiMakeCombineCandidateClean(v_stack_p78, v_stack_p40, (uint32_t)(*(uint32_t *)(result + 0xC)), v_stack_p38);
    Arg2 = 0;
    Arg2 = (((uint32_t)(v_stack_p58)) != 1) ? 1 : 0;
    result = MiFlushSingleTbEntry(v_stack_p90, Arg2, 10, v_stack_p38);
    goto loc_0031596F;
loc_00315FAB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB0B07)))) & (64)) == 0) goto loc_0031594E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p90, Arg2, 10, v_stack_p38);
    if ((uint8_t)(result) == 0) goto loc_0031594E;
    result = HvlNotifyLongSpinWait(0, Arg2, 10, v_stack_p38);
    goto loc_00315950;
loc_00315FD2:
    goto loc_00315DA4;
loc_00315FE6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB0ACC)))) & (64)) == 0) goto loc_00315CD0;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, Arg2, 10, v_stack_p38);
    if ((uint8_t)(result) == 0) goto loc_00315CD0;
    result = HvlNotifyLongSpinWait(0, Arg2, 10, v_stack_p38);
    goto loc_00315CD2;
loc_0031600D:
    Arg3 = 0;
    result = MiReplenishSlabAllocator(0, Arg3 + 16, Arg3, v_stack_p38);
    Arg1 = ((uint32_t)(result) == 0) ? 1 : 0;
    *(void **)(v_stack_p40 + 0x138) = Arg1;
    goto loc_003152B5;
loc_0031602D:
    Arg2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(v_stack_p40, Arg2, Arg3, v_stack_p38);
    if (result == 0) goto loc_003159BF;
    goto loc_00315E78;
loc_00316048:
    if (condition_is_below) goto loc_00315E92;
    v_stack_p20 = *(uint64_t *)(result + 0x8);
    result = KeBugCheckEx(26, (uint32_t)(0x411ULL), v_stack_p78, 0);
loc_00316076:
    goto loc_0031589F;
loc_00316085:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB0A2D)))) & (64)) == 0) goto loc_00315F6E;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbp)), (uint32_t)(0x411ULL), v_stack_p78, 0);
    if ((uint8_t)(result) == 0) goto loc_00315F6E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), (uint32_t)(0x411ULL), v_stack_p78, 0);
    goto loc_00315F70;
loc_003160AC:
    goto loc_00315C66;
loc_003160B9:
    if (((uint32_t)(result)) == 0) goto loc_00315AED;
    if (((uint32_t)(result)) >= 2) goto loc_00315913;
    result = 0;
    if (condition_is_equal) goto loc_00315AED;
    goto loc_00315913;
loc_003160DF:
    local_rbx = 0;
    goto loc_00315A23;
loc_003160E6:
    Arg2 = 0;
    result = MiWorkingSetIsContended(v_stack_p78, Arg2, v_stack_p78, 0);
    if ((uint32_t)(result) != 0) goto loc_00315365;
    if (0 == 0) goto loc_0031535C;
    result = MiPageTableLockIsContended(v_stack_p78, 0, v_stack_p78, 0);
    if ((uint32_t)(result) != 0) goto loc_00315365;
    goto loc_0031535C;
loc_00316119:
    local_rbx = 0;
loc_0031611B:
    goto loc_0031531A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x8C` | `32` | `R` |
| `Arg1` | `+ 0x138` | `64` | `W` |
| `Arg1` | `+ 0x140` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00315110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
