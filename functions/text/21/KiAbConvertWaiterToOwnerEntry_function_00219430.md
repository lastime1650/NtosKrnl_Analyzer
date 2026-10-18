# KiAbConvertWaiterToOwnerEntry

- RVA: `0x00219430`–`0x00219B29` (길이 `1,785` bytes)
- VA: `0x0000000140219430`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005EBEC`
- 디코드: `447`개 명령, `1,785/1,785` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x002194F1` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x00219561` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x00219569` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x00219595` → [KiAbTryDecrementIoWaiterCounts](../27/KiAbTryDecrementIoWaiterCounts_function_00272330.md) (function, `0x00272330`)
- `0x002195B4` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x00219624` → [KiAbEntryGetLockedHeadEntry](../22/KiAbEntryGetLockedHeadEntry_function_002213C0.md) (function, `0x002213C0`)
- `0x0021964F` → [KiAbEntryUpdateOwnerTreePosition](../2E/KiAbEntryUpdateOwnerTreePosition_function_002E5970.md) (function, `0x002E5970`)
- `0x002196B5` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x00219702` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x0021971A` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0021975B` → [KiAbEntryUpdateWaiterTreePosition](../2E/KiAbEntryUpdateWaiterTreePosition_function_002E5AE0.md) (function, `0x002E5AE0`)
- `0x0021976C` → [KiAbDetermineMinOwnerCpuPriority](../41/KiAbDetermineMinOwnerCpuPriority_function_00419220.md) (function, `0x00419220`)
- `0x00219777` → [KiAbTryIncrementIoWaiterCounts](../41/KiAbTryIncrementIoWaiterCounts_function_004192A0.md) (function, `0x004192A0`)
- `0x00219782` → [KiAbEntryGetCpuPriorityKey](../22/KiAbEntryGetCpuPriorityKey_function_00222DD0.md) (function, `0x00222DD0`)
- `0x00219798` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x002197C1` → [KiAbIoBoostOwners](KiAbIoBoostOwners_function_0021FCB0.md) (function, `0x0021FCB0`)
- `0x002197E0` → [KiAbCpuBoostOwners](../22/KiAbCpuBoostOwners_function_00220680.md) (function, `0x00220680`)
- `0x002197E9` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x00219825` → [EtwTraceAutoBoostProcessLockEntry](../22/EtwTraceAutoBoostProcessLockEntry_function_00221C7C.md) (function, `0x00221C7C`)
- `0x0021985C` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0021986E` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x0021988A` → [KiAbOwnerComputeCpuPriorityKey](KiAbOwnerComputeCpuPriorityKey_function_0021F090.md) (function, `0x0021F090`)
- `0x002198F9` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x00219920` → [KiAbSetMinimumThreadPriority](KiAbSetMinimumThreadPriority_function_0021F190.md) (function, `0x0021F190`)
- `0x0021993C` → [KiAbEntryUpdateOwnerTreePosition](../2E/KiAbEntryUpdateOwnerTreePosition_function_002E5970.md) (function, `0x002E5970`)
- `0x00219990` → [KiAbProcessThreadLocks](../22/KiAbProcessThreadLocks_function_00221D30.md) (function, `0x00221D30`)
- `0x00219A34` → [ObReferenceObjectSafeWithTag](ObReferenceObjectSafeWithTag_function_00210EE0.md) (function, `0x00210EE0`)
- `0x00219A57` → [IoBoostThreadIoPriority](IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x00219A69` → [PsBoostThreadOutstandingIoQoS](PsBoostThreadOutstandingIoQoS_function_00215C54.md) (function, `0x00215C54`)
- `0x00219A76` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x00219AA2` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x00219ABB` → [KiAbThreadRemoveBoostsSlow](KiAbThreadRemoveBoostsSlow_function_00210BB0.md) (function, `0x00210BB0`)
- `0x00219AD6` → [KiAbThreadInsertList](KiAbThreadInsertList_function_0021F0E0.md) (function, `0x0021F0E0`)
- `0x00219AE6` → [KiAbQueueAutoBoostDpc](../20/KiAbQueueAutoBoostDpc_function_002074D0.md) (function, `0x002074D0`)
- `0x00219B08` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x00219B1F` → [EtwTraceAutoBoostConvertWaiterToOwner](../4D/EtwTraceAutoBoostConvertWaiterToOwner_function_004DAF98.md) (function, `0x004DAF98`)

### Direct callers
- [sub_00219EB5](Unknown_function_00219EB5.md) at `0x00219F38`
- [ExReleaseFastResource](../26/ExReleaseFastResource_function_002613D0.md) at `0x002618CD`
- [sub_00261DFE](../26/Unknown_function_00261DFE.md) at `0x0026203E`
- [sub_00262F80](../26/Unknown_function_00262F80.md) at `0x00262FF5`
- [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) at `0x00265F1F`
- [sub_00341147](../34/Unknown_function_00341147.md) at `0x0034116F`
- [KeWakeWaitChain](../34/KeWakeWaitChain_function_0034F8C0.md) at `0x0034F976`
- [KeAbPreWakeupThread](../35/KeAbPreWakeupThread_function_0035034C.md) at `0x0035047E`

### Static image references
- `0x002194BA` → RVA `0x00E17100` (`.data`; read)
- `0x002194E1` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002195C2` → RVA `0x00F10D60` (`.data`; read)
- `0x00219726` → RVA `0x00FC6B14` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00219AFE` → [sub_006D68CE](../6D/Unknown_function_006D68CE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00219430  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00219435  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0021943A  55                              push rbp
0021943B  53                              push rbx
0021943C  56                              push rsi
0021943D  57                              push rdi
0021943E  41 54                           push r12
00219440  41 55                           push r13
00219442  41 56                           push r14
00219444  41 57                           push r15
00219446  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
0021944B  48 81 EC 98 00 00 00            sub rsp, 0x98
00219452  4C 8B 22                        mov r12, qword ptr [rdx]
00219455  33 C0                           xor eax, eax
00219457  45 33 C9                        xor r9d, r9d
0021945A  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
0021945E  48 B8 FC FF FF FF FF FF FF 7F   movabs rax, 0x7ffffffffffffffc
00219468  4C 89 4D B7                     mov qword ptr [rbp - 0x49], r9
0021946C  4C 23 E0                        and r12, rax
0021946F  0F 57 C0                        xorps xmm0, xmm0
00219472  4C 8B E9                        mov r13, rcx
00219475  4C 89 65 C7                     mov qword ptr [rbp - 0x39], r12
00219479  48 8B F2                        mov rsi, rdx
0021947C  41 8B F9                        mov edi, r9d
0021947F  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00219483  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
0021948D  74 0D                           je 0x14021949c
0021948F  44 38 4A 08                     cmp byte ptr [rdx + 8], r9b
00219493  7C 07                           jl 0x14021949c
00219495  4C 0B E1                        or r12, rcx
00219498  4C 89 65 C7                     mov qword ptr [rbp - 0x39], r12
0021949C  48 8B 1A                        mov rbx, qword ptr [rdx]
0021949F  0F B6 4A 08                     movzx ecx, byte ptr [rdx + 8]
002194A3  48 23 D8                        and rbx, rax
002194A6  48 8B C3                        mov rax, rbx
002194A9  48 C1 E8 04                     shr rax, 4
002194AD  84 C9                           test cl, cl
002194AF  0F 88 13 02 00 00               js 0x1402196c8
002194B5  25 FF 03 00 00                  and eax, 0x3ff
002194BA  48 8D 0D 3F DC BF 00            lea rcx, [rip + 0xbfdc3f]
002194C1  48 C1 E0 06                     shl rax, 6
002194C5  4C 8D 79 10                     lea r15, [rcx + 0x10]
002194C9  4C 03 F8                        add r15, rax
002194CC  4C 8D 34 08                     lea r14, [rax + rcx]
002194D0  44 0F 20 C0                     mov rax, cr8
002194D4  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
002194D8  B9 02 00 00 00                  mov ecx, 2
002194DD  44 0F 22 C1                     mov cr8, rcx
002194E1  44 39 0D 38 D8 DA 00            cmp dword ptr [rip + 0xdad838], r9d
002194E8  0F 85 6A 03 00 00               jne 0x140219858
002194EE  49 8B CF                        mov rcx, r15
002194F1  E8 3A F9 02 00                  call 0x140248e30
002194F6  49 8B 06                        mov rax, qword ptr [r14]
002194F9  B9 01 00 00 00                  mov ecx, 1
002194FE  41 84 4E 08                     test byte ptr [r14 + 8], cl
00219502  0F 85 FE 04 00 00               jne 0x140219a06
00219508  41 0F B6 56 08                  movzx edx, byte ptr [r14 + 8]
0021950D  23 D1                           and edx, ecx
0021950F  48 85 C0                        test rax, rax
00219512  0F 84 E3 01 00 00               je 0x1402196fb
00219518  49 B8 FC FF FF FF FF FF FF 7F   movabs r8, 0x7ffffffffffffffc
00219522  48 8B 48 F0                     mov rcx, qword ptr [rax - 0x10]
00219526  49 23 C8                        and rcx, r8
00219529  48 3B CB                        cmp rcx, rbx
0021952C  0F 82 1D 03 00 00               jb 0x14021984f
00219532  76 18                           jbe 0x14021954c
00219534  48 8B 08                        mov rcx, qword ptr [rax]
00219537  85 D2                           test edx, edx
00219539  74 09                           je 0x140219544
0021953B  48 85 C9                        test rcx, rcx
0021953E  0F 85 BA 04 00 00               jne 0x1402199fe
00219544  48 8B C1                        mov rax, rcx
00219547  48 85 C0                        test rax, rax
0021954A  75 D6                           jne 0x140219522
0021954C  48 85 C0                        test rax, rax
0021954F  0F 84 A6 01 00 00               je 0x1402196fb
00219555  48 8D 58 F0                     lea rbx, [rax - 0x10]
00219559  48 8D 4B 48                     lea rcx, [rbx + 0x48]
0021955D  48 8D 55 FF                     lea rdx, [rbp - 1]
00219561  E8 DA C1 05 00                  call 0x140275740
00219566  49 8B CF                        mov rcx, r15
00219569  E8 22 10 03 00                  call 0x14024a590
0021956E  48 8B 06                        mov rax, qword ptr [rsi]
00219571  48 C1 E8 3F                     shr rax, 0x3f
00219575  84 C0                           test al, al
00219577  0F 84 1D 05 00 00               je 0x140219a9a
0021957D  4C 8B 75 67                     mov r14, qword ptr [rbp + 0x67]
00219581  B8 FF 00 00 00                  mov eax, 0xff
00219586  66 F0 41 01 86 18 03 00 00      lock add word ptr [r14 + 0x318], ax
0021958F  48 8B D3                        mov rdx, rbx
00219592  48 8B CE                        mov rcx, rsi
00219595  E8 96 8D 05 00                  call 0x140272330
0021959A  48 3B DE                        cmp rbx, rsi
0021959D  0F 85 C3 02 00 00               jne 0x140219866
002195A3  40 88 7E 09                     mov byte ptr [rsi + 9], dil
002195A7  BF 02 00 00 00                  mov edi, 2
002195AC  80 66 08 BF                     and byte ptr [rsi + 8], 0xbf
002195B0  48 8D 4D FF                     lea rcx, [rbp - 1]
002195B4  E8 F7 DB FF FF                  call 0x1402171b0
002195B9  65 4C 8B 2C 25 20 00 00 00      mov r13, qword ptr gs:[0x20]
002195C2  83 3D 97 77 CF 00 00            cmp dword ptr [rip + 0xcf7797], 0
002195C9  4C 89 6D DF                     mov qword ptr [rbp - 0x21], r13
002195CD  0F 84 F2 04 00 00               je 0x140219ac5
002195D3  48 83 65 BF 00                  and qword ptr [rbp - 0x41], 0
002195D8  4D 8D BD 70 91 00 00            lea r15, [r13 + 0x9170]
002195DF  4C 8B 26                        mov r12, qword ptr [rsi]
002195E2  33 C0                           xor eax, eax
002195E4  21 45 6F                        and dword ptr [rbp + 0x6f], eax
002195E7  0F 57 C0                        xorps xmm0, xmm0
002195EA  21 45 7F                        and dword ptr [rbp + 0x7f], eax
002195ED  48 89 45 F7                     mov qword ptr [rbp - 9], rax
002195F1  48 B8 FC FF FF FF FF FF FF 7F   movabs rax, 0x7ffffffffffffffc
002195FB  4C 89 7D D7                     mov qword ptr [rbp - 0x29], r15
002195FF  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
00219603  4C 23 E0                        and r12, rax
00219606  74 13                           je 0x14021961b
00219608  80 7E 08 00                     cmp byte ptr [rsi + 8], 0
0021960C  7C 0D                           jl 0x14021961b
0021960E  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
00219618  4C 0B E0                        or r12, rax
0021961B  4C 8D 45 E7                     lea r8, [rbp - 0x19]
0021961F  33 D2                           xor edx, edx
00219621  48 8B CE                        mov rcx, rsi
00219624  E8 97 7D 00 00                  call 0x1402213c0
00219629  4C 8B F0                        mov r14, rax
0021962C  48 85 C0                        test rax, rax
0021962F  0F 84 14 03 00 00               je 0x140219949
00219635  80 7E 09 00                     cmp byte ptr [rsi + 9], 0
00219639  0F 85 0C 01 00 00               jne 0x14021974b
0021963F  BB 80 01 00 00                  mov ebx, 0x180
00219644  48 3B F0                        cmp rsi, rax
00219647  74 10                           je 0x140219659
00219649  48 8B D0                        mov rdx, rax
0021964C  48 8B CE                        mov rcx, rsi
0021964F  E8 1C C3 0C 00                  call 0x1402e5970
00219654  BB 90 01 00 00                  mov ebx, 0x190
00219659  83 65 6F 00                     and dword ptr [rbp + 0x6f], 0
0021965D  B8 02 00 00 00                  mov eax, 2
00219662  0F B6 4D 70                     movzx ecx, byte ptr [rbp + 0x70]
00219666  41 8B 56 54                     mov edx, dword ptr [r14 + 0x54]
0021966A  84 D2                           test dl, dl
0021966C  4D 8B 46 40                     mov r8, qword ptr [r14 + 0x40]
00219670  0F 45 C8                        cmovne ecx, eax
00219673  0F B6 45 71                     movzx eax, byte ptr [rbp + 0x71]
00219677  F7 C2 00 7F 00 00               test edx, 0x7f00
0021967D  88 4D 70                        mov byte ptr [rbp + 0x70], cl
00219680  B9 01 00 00 00                  mov ecx, 1
00219685  0F 47 C1                        cmova eax, ecx
00219688  88 45 71                        mov byte ptr [rbp + 0x71], al
0021968B  4D 85 C0                        test r8, r8
0021968E  0F 84 EC 03 00 00               je 0x140219a80
00219694  45 8A 40 18                     mov r8b, byte ptr [r8 + 0x18]
00219698  44 88 45 6F                     mov byte ptr [rbp + 0x6f], r8b
0021969C  41 80 7E 09 00                  cmp byte ptr [r14 + 9], 0
002196A1  0F 85 19 03 00 00               jne 0x1402199c0
002196A7  83 7D 6F 00                     cmp dword ptr [rbp + 0x6f], 0
002196AB  0F 85 52 02 00 00               jne 0x140219903
002196B1  48 8D 4D E7                     lea rcx, [rbp - 0x19]
002196B5  E8 F6 DA FF FF                  call 0x1402171b0
002196BA  41 BE 01 00 00 00               mov r14d, 1
002196C0  41 0B DE                        or ebx, r14d
002196C3  E9 39 01 00 00                  jmp 0x140219801
002196C8  83 E1 3F                        and ecx, 0x3f
002196CB  48 6B D1 58                     imul rdx, rcx, 0x58
002196CF  48 8B CE                        mov rcx, rsi
002196D2  48 2B CA                        sub rcx, rdx
002196D5  33 D2                           xor edx, edx
002196D7  48 8B 49 F0                     mov rcx, qword ptr [rcx - 0x10]
002196DB  4C 8B 81 20 02 00 00            mov r8, qword ptr [rcx + 0x220]
002196E2  41 F7 70 60                     div dword ptr [r8 + 0x60]
002196E6  49 8B 40 58                     mov rax, qword ptr [r8 + 0x58]
002196EA  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
002196EE  4C 8D 34 C8                     lea r14, [rax + rcx*8]
002196F2  4D 8D 7E 10                     lea r15, [r14 + 0x10]
002196F6  E9 D5 FD FF FF                  jmp 0x1402194d0
002196FB  49 8B CF                        mov rcx, r15
002196FE  40 88 7E 09                     mov byte ptr [rsi + 9], dil
00219702  E8 89 0E 03 00                  call 0x14024a590
00219707  83 3D 12 D6 DA 00 00            cmp dword ptr [rip + 0xdad612], 0
0021970E  48 8B 5D CF                     mov rbx, qword ptr [rbp - 0x31]
00219712  74 0B                           je 0x14021971f
00219714  44 0F 20 C1                     mov rcx, cr8
00219718  8A D3                           mov dl, bl
0021971A  E8 79 BF 2D 00                  call 0x1404f5698
0021971F  0F B6 C3                        movzx eax, bl
00219722  44 0F 22 C0                     mov cr8, rax
00219726  F7 05 E4 D3 DA 00 00 10 00 00   test dword ptr [rip + 0xdad3e4], 0x1000
00219730  0F 85 E0 03 00 00               jne 0x140219b16
00219736  48 81 C4 98 00 00 00            add rsp, 0x98
0021973D  41 5F                           pop r15
0021973F  41 5E                           pop r14
00219741  41 5D                           pop r13
00219743  41 5C                           pop r12
00219745  5F                              pop rdi
00219746  5E                              pop rsi
00219747  5B                              pop rbx
00219748  5D                              pop rbp
00219749  C3                              ret
0021974A  CC                              int3
0021974B  BB 88 01 00 00                  mov ebx, 0x188
00219750  49 3B F6                        cmp rsi, r14
00219753  74 10                           je 0x140219765
00219755  49 8B D6                        mov rdx, r14
00219758  48 8B CE                        mov rcx, rsi
0021975B  E8 80 C3 0C 00                  call 0x1402e5ae0
00219760  BB A8 01 00 00                  mov ebx, 0x1a8
00219765  48 8D 55 6F                     lea rdx, [rbp + 0x6f]
00219769  49 8B CE                        mov rcx, r14
0021976C  E8 AF FA 1F 00                  call 0x140419220
00219771  49 8B D6                        mov rdx, r14
00219774  48 8B CE                        mov rcx, rsi
00219777  E8 24 FB 1F 00                  call 0x1404192a0
0021977C  48 8B CE                        mov rcx, rsi
0021977F  44 8B D0                        mov r10d, eax
00219782  E8 49 96 00 00                  call 0x140222dd0
00219787  44 8A F8                        mov r15b, al
0021978A  38 45 6F                        cmp byte ptr [rbp + 0x6f], al
0021978D  7C 13                           jl 0x1402197a2
0021978F  45 85 D2                        test r10d, r10d
00219792  75 13                           jne 0x1402197a7
00219794  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00219798  E8 13 DA FF FF                  call 0x1402171b0
0021979D  83 CB 02                        or ebx, 2
002197A0  EB 59                           jmp 0x1402197fb
002197A2  45 85 D2                        test r10d, r10d
002197A5  74 1F                           je 0x1402197c6
002197A7  49 8D 85 70 91 00 00            lea rax, [r13 + 0x9170]
002197AE  41 8B D2                        mov edx, r10d
002197B1  4C 8D 4D BF                     lea r9, [rbp - 0x41]
002197B5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002197BA  4C 8D 45 B7                     lea r8, [rbp - 0x49]
002197BE  49 8B CE                        mov rcx, r14
002197C1  E8 EA 64 00 00                  call 0x14021fcb0
002197C6  49 8D 85 70 91 00 00            lea rax, [r13 + 0x9170]
002197CD  41 8A D7                        mov dl, r15b
002197D0  4C 8D 4D BF                     lea r9, [rbp - 0x41]
002197D4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002197D9  4C 8D 45 B7                     lea r8, [rbp - 0x49]
002197DD  49 8B CE                        mov rcx, r14
002197E0  E8 9B 6E 00 00                  call 0x140220680
002197E5  48 8D 4D E7                     lea rcx, [rbp - 0x19]
002197E9  E8 C2 D9 FF FF                  call 0x1402171b0
002197EE  44 8B 75 7F                     mov r14d, dword ptr [rbp + 0x7f]
002197F2  45 85 F6                        test r14d, r14d
002197F5  0F 85 1C 02 00 00               jne 0x140219a17
002197FB  41 BE 01 00 00 00               mov r14d, 1
00219801  F7 05 09 D3 DA 00 00 10 00 00   test dword ptr [rip + 0xdad309], 0x1000
0021980B  74 1D                           je 0x14021982a
0021980D  0F B6 46 08                     movzx eax, byte ptr [rsi + 8]
00219811  44 8B C3                        mov r8d, ebx
00219814  83 E0 3F                        and eax, 0x3f
00219817  49 8B D4                        mov rdx, r12
0021981A  48 6B C8 58                     imul rcx, rax, 0x58
0021981E  48 2B F1                        sub rsi, rcx
00219821  48 8B 4E F0                     mov rcx, qword ptr [rsi - 0x10]
00219825  E8 52 84 00 00                  call 0x140221c7c
0021982A  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
0021982E  48 85 C9                        test rcx, rcx
00219831  0F 85 1C 01 00 00               jne 0x140219953
00219837  4C 8B 65 C7                     mov r12, qword ptr [rbp - 0x39]
0021983B  48 83 7D B7 00                  cmp qword ptr [rbp - 0x49], 0
00219840  0F 85 AD 02 00 00               jne 0x140219af3
00219846  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
0021984A  E9 B8 FE FF FF                  jmp 0x140219707
0021984F  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00219853  E9 DF FC FF FF                  jmp 0x140219537
00219858  8A D1                           mov dl, cl
0021985A  8A C8                           mov cl, al
0021985C  E8 9B BE 2D 00                  call 0x1404f56fc
00219861  E9 88 FC FF FF                  jmp 0x1402194ee
00219866  48 8D 56 10                     lea rdx, [rsi + 0x10]
0021986A  48 8D 4B 38                     lea rcx, [rbx + 0x38]
0021986E  E8 9D B3 0C 00                  call 0x1402e4c10
00219873  44 8B 46 50                     mov r8d, dword ptr [rsi + 0x50]
00219877  21 7E 50                        and dword ptr [rsi + 0x50], edi
0021987A  40 88 7E 09                     mov byte ptr [rsi + 9], dil
0021987E  45 85 C0                        test r8d, r8d
00219881  0F 85 2A 02 00 00               jne 0x140219ab1
00219887  48 8B CE                        mov rcx, rsi
0021988A  E8 01 58 00 00                  call 0x14021f090
0021988F  48 83 C3 28                     add rbx, 0x28
00219893  88 46 28                        mov byte ptr [rsi + 0x28], al
00219896  41 BA 01 00 00 00               mov r10d, 1
0021989C  44 8A C8                        mov r9b, al
0021989F  48 8B 13                        mov rdx, qword ptr [rbx]
002198A2  44 84 53 08                     test byte ptr [rbx + 8], r10b
002198A6  0F 85 DD 01 00 00               jne 0x140219a89
002198AC  0F B6 4B 08                     movzx ecx, byte ptr [rbx + 8]
002198B0  45 32 C0                        xor r8b, r8b
002198B3  41 23 CA                        and ecx, r10d
002198B6  48 85 D2                        test rdx, rdx
002198B9  74 37                           je 0x1402198f2
002198BB  44 38 4A 18                     cmp byte ptr [rdx + 0x18], r9b
002198BF  7E 19                           jle 0x1402198da
002198C1  48 8B 02                        mov rax, qword ptr [rdx]
002198C4  85 C9                           test ecx, ecx
002198C6  74 08                           je 0x1402198d0
002198C8  48 85 C0                        test rax, rax
002198CB  74 25                           je 0x1402198f2
002198CD  48 33 C2                        xor rax, rdx
002198D0  48 85 C0                        test rax, rax
002198D3  74 1D                           je 0x1402198f2
002198D5  48 8B D0                        mov rdx, rax
002198D8  EB E1                           jmp 0x1402198bb
002198DA  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
002198DE  85 C9                           test ecx, ecx
002198E0  0F 84 CC 00 00 00               je 0x1402199b2
002198E6  48 85 C0                        test rax, rax
002198E9  0F 85 C0 00 00 00               jne 0x1402199af
002198EF  45 8A C2                        mov r8b, r10b
002198F2  4C 8D 4E 10                     lea r9, [rsi + 0x10]
002198F6  48 8B CB                        mov rcx, rbx
002198F9  E8 72 AC 0C 00                  call 0x1402e4570
002198FE  E9 A9 FC FF FF                  jmp 0x1402195ac
00219903  48 8D 45 7F                     lea rax, [rbp + 0x7f]
00219907  48 8B CE                        mov rcx, rsi
0021990A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0021990F  4C 8D 4D BF                     lea r9, [rbp - 0x41]
00219913  4C 8D 45 B7                     lea r8, [rbp - 0x49]
00219917  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0021991C  48 8D 55 6F                     lea rdx, [rbp + 0x6f]
00219920  E8 6B 58 00 00                  call 0x14021f190
00219925  85 C0                           test eax, eax
00219927  0F 84 B8 FE FF FF               je 0x1402197e5
0021992D  49 3B F6                        cmp rsi, r14
00219930  0F 84 AF FE FF FF               je 0x1402197e5
00219936  49 8B D6                        mov rdx, r14
00219939  48 8B CE                        mov rcx, rsi
0021993C  E8 2F C0 0C 00                  call 0x1402e5970
00219941  83 CB 20                        or ebx, 0x20
00219944  E9 9C FE FF FF                  jmp 0x1402197e5
00219949  BB 80 01 00 00                  mov ebx, 0x180
0021994E  E9 A8 FE FF FF                  jmp 0x1402197fb
00219953  4C 8B 6D D7                     mov r13, qword ptr [rbp - 0x29]
00219957  48 8B 01                        mov rax, qword ptr [rcx]
0021995A  48 8D 99 D8 FC FF FF            lea rbx, [rcx - 0x328]
00219961  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00219965  4C 89 B3 28 03 00 00            mov qword ptr [rbx + 0x328], r14
0021996C  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00219971  8A 83 18 03 00 00               mov al, byte ptr [rbx + 0x318]
00219977  84 C0                           test al, al
00219979  74 1A                           je 0x140219995
0021997B  4C 8D 4D BF                     lea r9, [rbp - 0x41]
0021997F  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00219984  4C 8D 45 B7                     lea r8, [rbp - 0x49]
00219988  BA 04 00 00 00                  mov edx, 4
0021998D  48 8B CB                        mov rcx, rbx
00219990  E8 9B 83 00 00                  call 0x140221d30
00219995  66 F0 FF 8B 64 03 00 00         lock dec word ptr [rbx + 0x364]
0021999D  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
002199A1  48 85 C9                        test rcx, rcx
002199A4  75 B1                           jne 0x140219957
002199A6  4C 8B 6D DF                     mov r13, qword ptr [rbp - 0x21]
002199AA  E9 88 FE FF FF                  jmp 0x140219837
002199AF  48 33 C2                        xor rax, rdx
002199B2  48 85 C0                        test rax, rax
002199B5  0F 85 1A FF FF FF               jne 0x1402198d5
002199BB  E9 2F FF FF FF                  jmp 0x1402198ef
002199C0  41 0F B6 46 08                  movzx eax, byte ptr [r14 + 8]
002199C5  83 E0 3F                        and eax, 0x3f
002199C8  48 6B C8 58                     imul rcx, rax, 0x58
002199CC  49 8B C6                        mov rax, r14
002199CF  48 2B C1                        sub rax, rcx
002199D2  48 8B 40 F0                     mov rax, qword ptr [rax - 0x10]
002199D6  0F B6 88 C3 00 00 00            movzx ecx, byte ptr [rax + 0xc3]
002199DD  B8 1E 00 00 00                  mov eax, 0x1e
002199E2  3A C8                           cmp cl, al
002199E4  8B D1                           mov edx, ecx
002199E6  41 0F B6 C8                     movzx ecx, r8b
002199EA  0F 4F D0                        cmovg edx, eax
002199ED  41 3A D0                        cmp dl, r8b
002199F0  0F B6 C2                        movzx eax, dl
002199F3  0F 4F C8                        cmovg ecx, eax
002199F6  88 4D 6F                        mov byte ptr [rbp + 0x6f], cl
002199F9  E9 A9 FC FF FF                  jmp 0x1402196a7
002199FE  48 33 C1                        xor rax, rcx
00219A01  E9 41 FB FF FF                  jmp 0x140219547
00219A06  48 85 C0                        test rax, rax
00219A09  0F 84 F9 FA FF FF               je 0x140219508
00219A0F  49 33 C6                        xor rax, r14
00219A12  E9 F1 FA FF FF                  jmp 0x140219508
00219A17  0F B6 46 08                     movzx eax, byte ptr [rsi + 8]
00219A1B  BA 44 66 6C 74                  mov edx, 0x746c6644
00219A20  83 E0 3F                        and eax, 0x3f
00219A23  48 6B C8 58                     imul rcx, rax, 0x58
00219A27  48 8B C6                        mov rax, rsi
00219A2A  48 2B C1                        sub rax, rcx
00219A2D  4C 8B 78 F0                     mov r15, qword ptr [rax - 0x10]
00219A31  49 8B CF                        mov rcx, r15
00219A34  E8 A7 74 FF FF                  call 0x140210ee0
00219A39  84 C0                           test al, al
00219A3B  0F 84 BA FD FF FF               je 0x1402197fb
00219A41  B8 01 00 00 00                  mov eax, 1
00219A46  44 84 F0                        test al, r14b
00219A49  74 11                           je 0x140219a5c
00219A4B  8D 50 01                        lea edx, [rax + 1]
00219A4E  41 B8 00 00 00 80               mov r8d, 0x80000000
00219A54  49 8B CF                        mov rcx, r15
00219A57  E8 B4 C6 FF FF                  call 0x140216110
00219A5C  B8 02 00 00 00                  mov eax, 2
00219A61  44 84 F0                        test al, r14b
00219A64  74 08                           je 0x140219a6e
00219A66  49 8B CF                        mov rcx, r15
00219A69  E8 E6 C1 FF FF                  call 0x140215c54
00219A6E  BA 44 66 6C 74                  mov edx, 0x746c6644
00219A73  49 8B CF                        mov rcx, r15
00219A76  E8 25 A4 04 00                  call 0x140263ea0
00219A7B  E9 7B FD FF FF                  jmp 0x1402197fb
00219A80  44 8A 45 6F                     mov r8b, byte ptr [rbp + 0x6f]
00219A84  E9 13 FC FF FF                  jmp 0x14021969c
00219A89  48 85 D2                        test rdx, rdx
00219A8C  0F 84 1A FE FF FF               je 0x1402198ac
00219A92  48 33 D3                        xor rdx, rbx
00219A95  E9 12 FE FF FF                  jmp 0x1402198ac
00219A9A  48 8D 4D FF                     lea rcx, [rbp - 1]
00219A9E  40 88 7E 09                     mov byte ptr [rsi + 9], dil
00219AA2  E8 09 D7 FF FF                  call 0x1402171b0
00219AA7  BF 01 00 00 00                  mov edi, 1
00219AAC  E9 56 FC FF FF                  jmp 0x140219707
00219AB1  4C 8D 4D B7                     lea r9, [rbp - 0x49]
00219AB5  49 8B D4                        mov rdx, r12
00219AB8  49 8B CE                        mov rcx, r14
00219ABB  E8 F0 70 FF FF                  call 0x140210bb0
00219AC0  E9 C2 FD FF FF                  jmp 0x140219887
00219AC5  4D 8D 86 30 03 00 00            lea r8, [r14 + 0x330]
00219ACC  49 8B CE                        mov rcx, r14
00219ACF  49 8D 95 70 91 00 00            lea rdx, [r13 + 0x9170]
00219AD6  E8 05 56 00 00                  call 0x14021f0e0
00219ADB  85 C0                           test eax, eax
00219ADD  0F 84 58 FD FF FF               je 0x14021983b
00219AE3  49 8B CD                        mov rcx, r13
00219AE6  E8 E5 D9 FE FF                  call 0x1402074d0
00219AEB  83 CF 08                        or edi, 8
00219AEE  E9 48 FD FF FF                  jmp 0x14021983b
00219AF3  83 7D 77 00                     cmp dword ptr [rbp + 0x77], 0
00219AF7  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00219AFB  49 8B CD                        mov rcx, r13
00219AFE  0F 85 CA CD 4B 00               jne 0x1406d68ce
00219B04  4C 8B 45 CF                     mov r8, qword ptr [rbp - 0x31]
00219B08  E8 F3 6C 03 00                  call 0x140250800
00219B0D  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
00219B11  E9 10 FC FF FF                  jmp 0x140219726
00219B16  44 8B C7                        mov r8d, edi
00219B19  49 8B D4                        mov rdx, r12
00219B1C  49 8B CD                        mov rcx, r13
00219B1F  E8 74 14 2C 00                  call 0x1404daf98
00219B24  E9 0D FC FF FF                  jmp 0x140219736
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAbConvertWaiterToOwnerEntry(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_p0;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p11;
    unsigned __int8 v_stack_p12;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (152);
    result = 0;
    a4 = 0;
    v_stack_m50 = 0;
    v_stack_mA8 = 0;
    v_r12 = (*(unsigned __int64 *)(a2)) & (0);
    v_stack_m98 = v_r12;
    v_stack_m60 = v_xmm0;
    if (condition_is_equal) goto loc_0021949C;
    if ((*(unsigned __int8 *)(a2 + 8)) >= 0) {
        v_r12 = (v_r12) | (a1);
        v_stack_m98 = v_r12;
    }
    v_rbx = (*(unsigned __int64 *)(a2)) & (0);
    result = (v_rbx) >> (4);
    if (sign_flag) goto loc_002196C8;
    result = (unsigned int)((result) & (0x3FFULL));
    result = (result) << (6);
    v_r15 = (v_rip + 12573759 + 16) + (result);
loc_002194D0:
    v_stack_m90 = v_cr8;
    if ((*(unsigned int *)(v_rip + 14342200)) != 0) goto loc_00219858;
loc_002194EE:
    result = ExAcquireSpinLockSharedAtDpcLevel(v_r15, a2, a3, a4);
    if (((*(unsigned __int8 *)(result + v_rip + 12573759 * 1 + 8)) & (1)) != 0) goto loc_00219A06;
loc_00219508:
    a2 = (unsigned int)((*(unsigned __int8 *)(result + v_rip + 12573759 * 1 + 8)) & (1));
    if (*(unsigned __int64 *)(result + v_rip + 12573759 * 1) == 0) goto loc_002196FB;
loc_00219522:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12573759 * 1) - 16)) & (a3);
    if (a1 < v_rbx) goto loc_0021984F;
    if (a1 <= v_rbx) goto loc_0021954C;
loc_00219537:
    if ((unsigned int)(a2) == 0) goto loc_00219544;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12573759 * 1)) != 0) goto loc_002199FE;
loc_00219544:
loc_00219547:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12573759 * 1)) != 0) goto loc_00219522;
loc_0021954C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12573759 * 1)) == 0) goto loc_002196FB;
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12573759 * 1)) - 16 + 72, v_stack_m60, a3, a4);
    result = ExReleaseSpinLockSharedFromDpcLevel(v_r15, v_stack_m60, a3, a4);
    result = (*(unsigned __int64 *)(a2)) >> (63);
    if ((unsigned __int8)(result) == 0) goto loc_00219A9A;
    result = KiAbTryDecrementIoWaiterCounts(a2, *(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12573759 * 1)) - 16, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12573759 * 1)) - 16) != a2) goto loc_00219866;
    *(unsigned __int8 *)(a2 + 9) = 0;
loc_002195AC:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m60, *(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12573759 * 1)) - 16, a3, a4);
    v_stack_m80 = *(unsigned __int64 *)(gs_base + (0 + 32));
    if ((*(unsigned int *)(v_rip + 13596567)) == 0) goto loc_00219AC5;
    result = 0;
    v_stack_m68 = 0;
    v_stack_m88 = *(unsigned __int64 *)(gs_base + (0 + 32)) + 37232;
    v_stack_m78 = v_xmm0;
    v_r12 = (*(unsigned __int64 *)(a2)) & (0);
    if (condition_is_equal) goto loc_0021961B;
    if ((*(unsigned __int8 *)(a2 + 8)) >= 0) {
        v_r12 = (v_r12) | (0);
    }
    a2 = 0;
    result = KiAbEntryGetLockedHeadEntry(0, a2, v_stack_m78, a4);
    if (result == 0) goto loc_00219949;
    if ((*(unsigned __int8 *)(a2 + 9)) != 0) goto loc_0021974B;
    v_rbx = 384;
    if (0 != result) {
        a2 = result;
        a1 = a2;
        result = KiAbEntryUpdateOwnerTreePosition(a1, a2, v_stack_m78, a4);
        v_rbx = 400;
    }
    a1 = v_stack_p11;
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 84))) != 0) { a1 = 2; }
    v_stack_p11 = (unsigned __int8)(a1);
    result = v_stack_p12;
    if (condition_is_above) { result = 1; }
    v_stack_p12 = (unsigned __int8)(result);
    if (*(unsigned __int64 *)(result + 64) == 0) goto loc_00219A80;
    v_stack_p10 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 64) + 24));
loc_0021969C:
    if ((*(unsigned __int8 *)(result + 9)) != 0) goto loc_002199C0;
loc_002196A7:
    if (v_stack_p10 != 0) goto loc_00219903;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m78, (unsigned int)(*(unsigned int *)(result + 84)), *(unsigned __int8 *)(*(unsigned __int64 *)(result + 64) + 24), a4);
    v_rbx = (unsigned int)((v_rbx) | (1));
    goto loc_00219801;
loc_002196C8:
    a1 = (unsigned int)((v_stack_m78) & (63));
    a2 = ((unsigned int)(*(unsigned int *)(result + 84))) * (a1);
    a1 = (a2) - (a2);
    a2 = 0;
    goto loc_002194D0;
loc_002196FB:
    *(unsigned __int8 *)(a2 + 9) = 2;
    result = ExReleaseSpinLockSharedFromDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544), a4);
loc_00219707:
    if ((*(unsigned int *)(v_rip + 14341650)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_m90);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544), a4);
    }
loc_00219726:
    if (((*(unsigned int *)(v_rip + 14341092)) & (0x1000ULL)) != 0) goto loc_00219B16;
loc_00219736:
    v_rsp = (v_rsp) + (152);
    return (unsigned __int8)(v_stack_m90);
loc_0021974B:
    result = (unsigned __int8)(v_stack_m90);
    v_rbx = 392;
    if (a2 != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544) + 88) + a2 + a2 * 2 * 8)) {
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544) + 88) + a2 + a2 * 2 * 8;
        a1 = a2;
        result = KiAbEntryUpdateWaiterTreePosition(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544), a4);
        v_rbx = 424;
    }
    result = KiAbDetermineMinOwnerCpuPriority(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544) + 88) + a2 + a2 * 2 * 8, v_stack_p10, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544), a4);
    result = KiAbTryIncrementIoWaiterCounts(a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544) + 88) + a2 + a2 * 2 * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544), a4);
    result = KiAbEntryGetCpuPriorityKey(a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544) + 88) + a2 + a2 * 2 * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544), a4);
    if (v_stack_p10 < ((unsigned __int8)(result))) goto loc_002197A2;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_002197A7;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m78, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544) + 88) + a2 + a2 * 2 * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544), a4);
    v_rbx = (unsigned int)((v_rbx) | (2));
    goto loc_002197FB;
loc_002197A2:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 32)) + 37232;
        a2 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a4 = v_stack_mA0;
        v_stack_p20 = result;
        a3 = v_stack_mA8;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544) + 88) + a2 + a2 * 2 * 8;
        result = KiAbIoBoostOwners(a1, a2, a3, a4);
    }
    v_stack_p20 = *(unsigned __int64 *)(gs_base + (0 + 32)) + 37232;
    result = KiAbCpuBoostOwners(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 544) + 88) + a2 + a2 * 2 * 8, (unsigned __int8)((unsigned __int8)(result)), v_stack_mA8, v_stack_mA0);
loc_002197E5:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m78, (unsigned __int8)((unsigned __int8)(result)), v_stack_mA8, v_stack_mA0);
    if ((unsigned int)((unsigned int)(v_stack_p20)) != 0) goto loc_00219A17;
loc_002197FB:
loc_00219801:
    v_rsi = a2;
    if (((*(unsigned int *)(v_rip + 14340873)) & (0x1000ULL)) != 0) {
        result = *(unsigned __int8 *)(a2 + 8);
        a3 = (unsigned int)(v_rbx);
        result = (unsigned int)((result) & (63));
        a2 = v_r12;
        a1 = (v_stack_m78) * (result);
        v_rsi = (a2) - (a1);
        a1 = *(unsigned __int64 *)(v_rsi - 16);
        result = EtwTraceAutoBoostProcessLockEntry(a1, a2, a3, v_stack_mA0);
    }
    if (v_stack_mA0 != 0) goto loc_00219953;
loc_00219837:
loc_0021983B:
    if (v_stack_mA8 != 0) goto loc_00219AF3;
    goto loc_00219707;
loc_0021984F:
    goto loc_00219537;
loc_00219858:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), (unsigned __int8)(*(unsigned __int64 *)(result + 8)), a3, v_stack_mA0);
    goto loc_002194EE;
loc_00219866:
    result = RtlRbRemoveNode(v_rbx + 56, v_rsi + 16, a3, v_stack_mA0);
    *(unsigned __int8 *)(v_rsi + 9) = 2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 80))) != 0) goto loc_00219AB1;
loc_00219887:
    result = KiAbOwnerComputeCpuPriorityKey(v_rsi, v_rsi + 16, (unsigned int)(*(unsigned int *)(v_rsi + 80)), v_stack_mA0);
    v_rbx = (v_rbx) + (40);
    *(unsigned __int8 *)(v_rsi + 40) = (unsigned __int8)(result);
    if (((*(unsigned __int8 *)(v_rbx + 8)) & (1)) != 0) goto loc_00219A89;
loc_002198AC:
    a3 = 0;
    a1 = (unsigned int)((*(unsigned __int8 *)(v_rbx + 8)) & (1));
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_002198F2;
loc_002198BB:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbx) + 24)) <= ((unsigned __int8)((unsigned __int8)(result)))) goto loc_002198DA;
    if ((unsigned int)(a1) == 0) goto loc_002198D0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx)) == 0) goto loc_002198F2;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx))) ^ (*(unsigned __int64 *)(v_rbx));
loc_002198D0:
    if (result == 0) goto loc_002198F2;
loc_002198D5:
    goto loc_002198BB;
loc_002198DA:
    if ((unsigned int)(a1) == 0) goto loc_002199B2;
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_002199AF;
loc_002198EF:
loc_002198F2:
    result = RtlRbInsertNodeEx(v_rbx, result, 1, v_rsi + 16);
    goto loc_002195AC;
loc_00219903:
    v_stack_p28 = v_stack_p20;
    v_stack_p20 = (unsigned __int8)(result);
    result = KiAbSetMinimumThreadPriority(v_rsi, v_stack_p10, v_stack_mA8, v_stack_mA0);
    if ((unsigned int)(result) == 0) goto loc_002197E5;
    if (v_rsi == 1) goto loc_002197E5;
    result = KiAbEntryUpdateOwnerTreePosition(v_rsi, 1, v_stack_mA8, v_stack_mA0);
    v_rbx = (unsigned int)((v_rbx) | (32));
    goto loc_002197E5;
loc_00219949:
    goto loc_002197FB;
loc_00219953:
loc_00219957:
    v_stack_mA0 = *(unsigned __int64 *)(v_rsi);
    *(unsigned __int64 *)(v_rsi - 808 + 808) = 1;
    result = *(unsigned __int8 *)(v_rsi - 808 + 792);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsi - 808 + 792)) != 0) {
        a4 = v_stack_mA0;
        v_stack_p20 = v_stack_m88;
        a3 = v_stack_mA8;
        a2 = 4;
        a1 = v_rsi - 808;
        result = KiAbProcessThreadLocks(a1, a2, a3, a4);
    }
    if (v_stack_mA0 != 0) goto loc_00219957;
    goto loc_00219837;
loc_002199AF:
    result = (result) ^ (a2);
loc_002199B2:
    if (result != 0) goto loc_002198D5;
    goto loc_002198EF;
loc_002199C0:
    result = (unsigned int)((*(unsigned __int8 *)(1 + 8)) & (63));
    a1 = (v_stack_mA0) * (result);
    result = (1) - (a1);
    a2 = (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195)));
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result - 16) + 195))) > 30) { a2 = 30; }
    a1 = (unsigned __int8)(a3);
    if (((unsigned __int8)(a2)) > ((unsigned __int8)(a3))) { a1 = (unsigned int)((unsigned __int8)(a2)); }
    v_stack_p10 = (unsigned __int8)(a1);
    goto loc_002196A7;
loc_002199FE:
    result = ((unsigned __int8)(a2)) ^ (a1);
    goto loc_00219547;
loc_00219A06:
    if (result == 0) goto loc_00219508;
    result = (result) ^ (1);
    goto loc_00219508;
loc_00219A17:
    result = (unsigned int)((*(unsigned __int8 *)(v_rsi + 8)) & (63));
    a1 = (a1) * (result);
    result = (v_rsi) - (a1);
    result = ObReferenceObjectSafeWithTag(*(unsigned __int64 *)(result - 16), (unsigned int)(0x746C6644ULL), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002197FB;
    result = 1;
    if (1 != 0) {
        a2 = 1 + 1;
        a3 = 0x80000000ULL;
        a1 = *(unsigned __int64 *)(result - 16);
        result = IoBoostThreadIoPriority(a1, a2, a3, a4);
    }
    result = 2;
    if (((2) & (1)) != 0) {
        a1 = *(unsigned __int64 *)(result - 16);
        result = PsBoostThreadOutstandingIoQoS(a1, a2, a3, a4);
    }
    result = ObDereferenceObjectDeferDeleteWithTag(*(unsigned __int64 *)(result - 16), (unsigned int)(0x746C6644ULL), a3, a4);
    goto loc_002197FB;
loc_00219A80:
    goto loc_0021969C;
loc_00219A89:
    if ((unsigned int)(0x746C6644ULL) == 0) goto loc_002198AC;
    a2 = ((unsigned int)(0x746C6644ULL)) ^ (v_rsi - 808);
    goto loc_002198AC;
loc_00219A9A:
    *(unsigned __int8 *)(v_rsi + 9) = 2;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m60, a2, v_stack_p10, a4);
    goto loc_00219707;
loc_00219AB1:
    result = KiAbThreadRemoveBoostsSlow(1, v_stack_m98, v_stack_p10, v_stack_mA8);
    goto loc_00219887;
loc_00219AC5:
    result = KiAbThreadInsertList(1, v_stack_m80 + 37232, 1 + 816, v_stack_mA8);
    if ((unsigned int)(result) == 0) goto loc_0021983B;
    result = KiAbQueueAutoBoostDpc(v_stack_m80, v_stack_m80 + 37232, 1 + 816, v_stack_mA8);
    v_rdi = (unsigned int)((1) | (8));
    goto loc_0021983B;
loc_00219AF3:
    result = KiProcessDeferredReadyList(v_stack_m80, v_stack_mA8, v_stack_m90, v_stack_mA8);
    goto loc_00219726;
loc_00219B16:
    result = EtwTraceAutoBoostConvertWaiterToOwner(v_stack_p8, v_stack_m98, (unsigned int)((unsigned int)(v_rdi)), v_stack_mA8);
    goto loc_00219736;
}
```

## 5. (Beta) C Style

```c
int64_t KiAbConvertWaiterToOwnerEntry(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_p0;
    uint32_t v_stack_p10;
    uint8_t v_stack_p11;
    uint8_t v_stack_p12;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (152);
    result = 0;
    Arg4 = 0;
    v_stack_m50 = 0;
    v_stack_mA8 = 0;
    local_r12 = (*(uint64_t *)(arg2)) & (0);
    v_stack_m98 = local_r12;
    v_stack_m60 = v_xmm0;
    if (condition_is_equal) goto loc_0021949C;
    if ((*(uint8_t *)(arg2 + 0x8)) >= 0) {
        local_r12 = (local_r12) | (Arg1);
        v_stack_m98 = local_r12;
    }
    local_rbx = (*(uint64_t *)(arg2)) & (0);
    result = (local_rbx) >> (4);
    if (sign_flag) goto loc_002196C8;
    result = (uint32_t)((result) & (0x3FFULL));
    result = (result) << (6);
    local_r15 = (v_rip + 12573759 + 16) + (result);
loc_002194D0:
    v_stack_m90 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xDAD838)) != 0) goto loc_00219858;
loc_002194EE:
    result = ExAcquireSpinLockSharedAtDpcLevel(local_r15, Arg2, Arg3, Arg4);
    if (((*(uint8_t *)(result + v_rip + 0xBFDC3F * 1 + 0x8)) & (1)) != 0) goto loc_00219A06;
loc_00219508:
    Arg2 = (uint32_t)((*(uint8_t *)(result + v_rip + 0xBFDC3F * 1 + 0x8)) & (1));
    if (*(uint64_t *)(result + v_rip + 0xBFDC3F * 1) == 0) goto loc_002196FB;
loc_00219522:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBFDC3F * 1) - 0x10)) & (Arg3);
    if (Arg1 < local_rbx) goto loc_0021984F;
    if (Arg1 <= local_rbx) goto loc_0021954C;
loc_00219537:
    if ((uint32_t)(Arg2) == 0) goto loc_00219544;
    if (*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBFDC3F * 1)) != 0) goto loc_002199FE;
loc_00219544:
loc_00219547:
    if (*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBFDC3F * 1)) != 0) goto loc_00219522;
loc_0021954C:
    if (*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBFDC3F * 1)) == 0) goto loc_002196FB;
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBFDC3F * 1)) - 16 + 72, v_stack_m60, Arg3, Arg4);
    result = ExReleaseSpinLockSharedFromDpcLevel(local_r15, v_stack_m60, Arg3, Arg4);
    result = (*(uint64_t *)(arg2)) >> (63);
    if ((uint8_t)(result) == 0) goto loc_00219A9A;
    result = KiAbTryDecrementIoWaiterCounts(Arg2, *(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBFDC3F * 1)) - 16, Arg3, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBFDC3F * 1)) - 16) != Arg2) goto loc_00219866;
    *(uint8_t *)(arg2 + 0x9) = 0;
loc_002195AC:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m60, *(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBFDC3F * 1)) - 16, Arg3, Arg4);
    v_stack_m80 = *(uint64_t *)(gs_base + (0 + 0x20));
    if ((*(uint32_t *)(v_rip + 0xCF7797)) == 0) goto loc_00219AC5;
    result = 0;
    v_stack_m68 = 0;
    v_stack_m88 = *(uint64_t *)(gs_base + (0 + 0x20)) + 37232;
    v_stack_m78 = v_xmm0;
    local_r12 = (*(uint64_t *)(arg2)) & (0);
    if (condition_is_equal) goto loc_0021961B;
    if ((*(uint8_t *)(arg2 + 0x8)) >= 0) {
        local_r12 = (local_r12) | (0);
    }
    Arg2 = 0;
    result = KiAbEntryGetLockedHeadEntry(0, Arg2, v_stack_m78, Arg4);
    if (result == 0) goto loc_00219949;
    if ((*(uint8_t *)(arg2 + 0x9)) != 0) goto loc_0021974B;
    local_rbx = 384;
    if (0 != result) {
        Arg2 = result;
        Arg1 = Arg2;
        result = KiAbEntryUpdateOwnerTreePosition(Arg1, Arg2, v_stack_m78, Arg4);
        local_rbx = 400;
    }
    Arg1 = v_stack_p11;
    if ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x54))) != 0) { Arg1 = 2; }
    v_stack_p11 = (uint8_t)(Arg1);
    result = v_stack_p12;
    if (condition_is_above) { result = 1; }
    v_stack_p12 = (uint8_t)(result);
    if (*(uint64_t *)(result + 0x40) == 0) goto loc_00219A80;
    v_stack_p10 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(result + 0x40) + 0x18));
loc_0021969C:
    if ((*(uint8_t *)(result + 0x9)) != 0) goto loc_002199C0;
loc_002196A7:
    if (v_stack_p10 != 0) goto loc_00219903;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m78, (uint32_t)(*(uint32_t *)(result + 0x54)), *(uint8_t *)(*(uint64_t *)(result + 0x40) + 0x18), Arg4);
    local_rbx = (uint32_t)((local_rbx) | (1));
    goto loc_00219801;
loc_002196C8:
    Arg1 = (uint32_t)((v_stack_m78) & (63));
    Arg2 = ((uint32_t)(*(uint32_t *)(result + 0x54))) * (Arg1);
    Arg1 = (Arg2) - (Arg2);
    Arg2 = 0;
    goto loc_002194D0;
loc_002196FB:
    *(uint8_t *)(arg2 + 0x9) = 2;
    result = ExReleaseSpinLockSharedFromDpcLevel(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220) + 0x58) + Arg2 + Arg2 * 2 * 8 + 16, Arg2, *(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220), Arg4);
loc_00219707:
    if ((*(uint32_t *)(v_rip + 0xDAD612)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_m90);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220), Arg4);
    }
loc_00219726:
    if (((*(uint32_t *)(v_rip + 0xDAD3E4)) & (0x1000ULL)) != 0) goto loc_00219B16;
loc_00219736:
    local_rsp = (local_rsp) + (152);
    return (uint8_t)(v_stack_m90);
loc_0021974B:
    result = (uint8_t)(v_stack_m90);
    local_rbx = 392;
    if (Arg2 != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220) + 0x58) + Arg2 + Arg2 * 2 * 8)) {
        Arg2 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220) + 0x58) + Arg2 + Arg2 * 2 * 8;
        Arg1 = Arg2;
        result = KiAbEntryUpdateWaiterTreePosition(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220), Arg4);
        local_rbx = 424;
    }
    result = KiAbDetermineMinOwnerCpuPriority(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220) + 0x58) + Arg2 + Arg2 * 2 * 8, v_stack_p10, *(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220), Arg4);
    result = KiAbTryIncrementIoWaiterCounts(Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220) + 0x58) + Arg2 + Arg2 * 2 * 8, *(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220), Arg4);
    result = KiAbEntryGetCpuPriorityKey(Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220) + 0x58) + Arg2 + Arg2 * 2 * 8, *(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220), Arg4);
    if (v_stack_p10 < ((uint8_t)(result))) goto loc_002197A2;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_002197A7;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m78, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220) + 0x58) + Arg2 + Arg2 * 2 * 8, *(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220), Arg4);
    local_rbx = (uint32_t)((local_rbx) | (2));
    goto loc_002197FB;
loc_002197A2:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x20)) + 37232;
        Arg2 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg4 = v_stack_mA0;
        v_stack_p20 = result;
        Arg3 = v_stack_mA8;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220) + 0x58) + Arg2 + Arg2 * 2 * 8;
        result = KiAbIoBoostOwners(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_p20 = *(uint64_t *)(gs_base + (0 + 0x20)) + 37232;
    result = KiAbCpuBoostOwners(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 - 0x10) + 0x220) + 0x58) + Arg2 + Arg2 * 2 * 8, (uint8_t)((uint8_t)(result)), v_stack_mA8, v_stack_mA0);
loc_002197E5:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m78, (uint8_t)((uint8_t)(result)), v_stack_mA8, v_stack_mA0);
    if ((uint32_t)((uint32_t)(v_stack_p20)) != 0) goto loc_00219A17;
loc_002197FB:
loc_00219801:
    local_rsi = Arg2;
    if (((*(uint32_t *)(v_rip + 0xDAD309)) & (0x1000ULL)) != 0) {
        result = *(uint8_t *)(arg2 + 0x8);
        Arg3 = (uint32_t)(local_rbx);
        result = (uint32_t)((result) & (63));
        Arg2 = local_r12;
        Arg1 = (v_stack_m78) * (result);
        local_rsi = (Arg2) - (Arg1);
        Arg1 = *(uint64_t *)(local_rsi - 0x10);
        result = EtwTraceAutoBoostProcessLockEntry(Arg1, Arg2, Arg3, v_stack_mA0);
    }
    if (v_stack_mA0 != 0) goto loc_00219953;
loc_00219837:
loc_0021983B:
    if (v_stack_mA8 != 0) goto loc_00219AF3;
    goto loc_00219707;
loc_0021984F:
    goto loc_00219537;
loc_00219858:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), (uint8_t)(*(uint64_t *)(result + 0x8)), Arg3, v_stack_mA0);
    goto loc_002194EE;
loc_00219866:
    result = RtlRbRemoveNode(local_rbx + 56, local_rsi + 16, Arg3, v_stack_mA0);
    *(uint8_t *)(local_rsi + 0x9) = 2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x50))) != 0) goto loc_00219AB1;
loc_00219887:
    result = KiAbOwnerComputeCpuPriorityKey(local_rsi, local_rsi + 16, (uint32_t)(*(uint32_t *)(local_rsi + 0x50)), v_stack_mA0);
    local_rbx = (local_rbx) + (40);
    *(uint8_t *)(local_rsi + 0x28) = (uint8_t)(result);
    if (((*(uint8_t *)(local_rbx + 0x8)) & (1)) != 0) goto loc_00219A89;
loc_002198AC:
    Arg3 = 0;
    Arg1 = (uint32_t)((*(uint8_t *)(local_rbx + 0x8)) & (1));
    if (*(uint64_t *)(local_rbx) == 0) goto loc_002198F2;
loc_002198BB:
    if ((*(uint8_t *)(*(uint64_t *)(local_rbx) + 0x18)) <= ((uint8_t)((uint8_t)(result)))) goto loc_002198DA;
    if ((uint32_t)(Arg1) == 0) goto loc_002198D0;
    if (*(uint64_t *)(*(uint64_t *)(local_rbx)) == 0) goto loc_002198F2;
    result = (*(uint64_t *)(*(uint64_t *)(local_rbx))) ^ (*(uint64_t *)(local_rbx));
loc_002198D0:
    if (result == 0) goto loc_002198F2;
loc_002198D5:
    goto loc_002198BB;
loc_002198DA:
    if ((uint32_t)(Arg1) == 0) goto loc_002199B2;
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_002199AF;
loc_002198EF:
loc_002198F2:
    result = RtlRbInsertNodeEx(local_rbx, result, 1, local_rsi + 16);
    goto loc_002195AC;
loc_00219903:
    v_stack_p28 = v_stack_p20;
    v_stack_p20 = (uint8_t)(result);
    result = KiAbSetMinimumThreadPriority(local_rsi, v_stack_p10, v_stack_mA8, v_stack_mA0);
    if ((uint32_t)(result) == 0) goto loc_002197E5;
    if (local_rsi == 1) goto loc_002197E5;
    result = KiAbEntryUpdateOwnerTreePosition(local_rsi, 1, v_stack_mA8, v_stack_mA0);
    local_rbx = (uint32_t)((local_rbx) | (32));
    goto loc_002197E5;
loc_00219949:
    goto loc_002197FB;
loc_00219953:
loc_00219957:
    v_stack_mA0 = *(uint64_t *)(local_rsi);
    *(uint64_t *)(local_rsi - 0x328 + 0x328) = 1;
    result = *(uint8_t *)(local_rsi - 0x328 + 0x318);
    if ((uint8_t)(*(uint8_t *)(local_rsi - 0x328 + 0x318)) != 0) {
        Arg4 = v_stack_mA0;
        v_stack_p20 = v_stack_m88;
        Arg3 = v_stack_mA8;
        Arg2 = 4;
        Arg1 = local_rsi - 808;
        result = KiAbProcessThreadLocks(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_mA0 != 0) goto loc_00219957;
    goto loc_00219837;
loc_002199AF:
    result = (result) ^ (Arg2);
loc_002199B2:
    if (result != 0) goto loc_002198D5;
    goto loc_002198EF;
loc_002199C0:
    result = (uint32_t)((*(uint8_t *)(1 + 0x8)) & (63));
    Arg1 = (v_stack_mA0) * (result);
    result = (1) - (Arg1);
    Arg2 = (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3)));
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(result - 0x10) + 0xC3))) > 30) { Arg2 = 30; }
    Arg1 = (uint8_t)(Arg3);
    if (((uint8_t)(Arg2)) > ((uint8_t)(Arg3))) { Arg1 = (uint32_t)((uint8_t)(Arg2)); }
    v_stack_p10 = (uint8_t)(Arg1);
    goto loc_002196A7;
loc_002199FE:
    result = ((uint8_t)(Arg2)) ^ (Arg1);
    goto loc_00219547;
loc_00219A06:
    if (result == 0) goto loc_00219508;
    result = (result) ^ (1);
    goto loc_00219508;
loc_00219A17:
    result = (uint32_t)((*(uint8_t *)(local_rsi + 0x8)) & (63));
    Arg1 = (Arg1) * (result);
    result = (local_rsi) - (Arg1);
    result = ObReferenceObjectSafeWithTag(*(uint64_t *)(result - 0x10), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002197FB;
    result = 1;
    if (1 != 0) {
        Arg2 = 1 + 1;
        Arg3 = 0x80000000ULL;
        Arg1 = *(uint64_t *)(result - 0x10);
        result = IoBoostThreadIoPriority(Arg1, Arg2, Arg3, Arg4);
    }
    result = 2;
    if (((2) & (1)) != 0) {
        Arg1 = *(uint64_t *)(result - 0x10);
        result = PsBoostThreadOutstandingIoQoS(Arg1, Arg2, Arg3, Arg4);
    }
    result = ObDereferenceObjectDeferDeleteWithTag(*(uint64_t *)(result - 0x10), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    goto loc_002197FB;
loc_00219A80:
    goto loc_0021969C;
loc_00219A89:
    if ((uint32_t)(0x746C6644ULL) == 0) goto loc_002198AC;
    Arg2 = ((uint32_t)(0x746C6644ULL)) ^ (local_rsi - 808);
    goto loc_002198AC;
loc_00219A9A:
    *(uint8_t *)(local_rsi + 0x9) = 2;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m60, Arg2, v_stack_p10, Arg4);
    goto loc_00219707;
loc_00219AB1:
    result = KiAbThreadRemoveBoostsSlow(1, v_stack_m98, v_stack_p10, v_stack_mA8);
    goto loc_00219887;
loc_00219AC5:
    result = KiAbThreadInsertList(1, v_stack_m80 + 37232, 1 + 816, v_stack_mA8);
    if ((uint32_t)(result) == 0) goto loc_0021983B;
    result = KiAbQueueAutoBoostDpc(v_stack_m80, v_stack_m80 + 37232, 1 + 816, v_stack_mA8);
    local_rdi = (uint32_t)((1) | (8));
    goto loc_0021983B;
loc_00219AF3:
    result = KiProcessDeferredReadyList(v_stack_m80, v_stack_mA8, v_stack_m90, v_stack_mA8);
    goto loc_00219726;
loc_00219B16:
    result = EtwTraceAutoBoostConvertWaiterToOwner(v_stack_p8, v_stack_m98, (uint32_t)((uint32_t)(local_rdi)), v_stack_mA8);
    goto loc_00219736;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x10` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `8` | `R` |
| `Arg2` | `+ 0x8` | `8` | `R/W` |
| `Arg2` | `+ 0x9` | `8` | `R` |
| `Arg2` | `+ 0x9` | `8` | `W` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x28` | `8` | `W` |
| `Arg2` | `+ 0x50` | `32` | `R` |
| `Arg2` | `+ 0x50` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00219430&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
