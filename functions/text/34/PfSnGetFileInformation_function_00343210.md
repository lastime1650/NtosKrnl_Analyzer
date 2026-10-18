# PfSnGetFileInformation

- RVA: `0x00343210`–`0x0034374D` (길이 `1,341` bytes)
- VA: `0x0000000140343210`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077AFC`
- 디코드: `330`개 명령, `1,341/1,341` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0034329C` → [ExAcquireSpinLockShared](../24/ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)
- `0x003432FA` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x00343310` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0034332E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00343355` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00343369` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x003433D3` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003433F9` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00343416` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00343447` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0034348B` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00343519` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x00343528` → [ExReleaseSpinLockExclusive](../2C/ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)
- `0x00343564` → [ExReleaseRundownProtection](ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x003435AB` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00343603` → [KeAreInterruptsEnabled](../2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x00343631` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x0034363C` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x00343646` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00343673` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x0034368D` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x003436F8` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x00343743` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [PfSnLogPageFaultCommon](PfSnLogPageFaultCommon_function_00343070.md) at `0x0034308C`

### Static image references
- `0x003432FF` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003433AC` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x003433DC` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x0034349F` → RVA `0x002C0E20` (`PfSnNameQueryWorker`; read)
- `0x00343579` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00343599` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0034367A` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x0034332E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00343416` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00343631` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x0034363C` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
  - `0x00343646` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00343673` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00343210  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00343215  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0034321A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0034321F  57                              push rdi
00343220  41 54                           push r12
00343222  41 55                           push r13
00343224  41 56                           push r14
00343226  41 57                           push r15
00343228  48 83 EC 30                     sub rsp, 0x30
0034322C  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00343230  45 32 E4                        xor r12b, r12b
00343233  48 8B 7A 18                     mov rdi, qword ptr [rdx + 0x18]
00343237  45 33 ED                        xor r13d, r13d
0034323A  48 8B F2                        mov rsi, rdx
0034323D  4C 8B F1                        mov r14, rcx
00343240  44 8B 40 34                     mov r8d, dword ptr [rax + 0x34]
00343244  41 F6 C0 10                     test r8b, 0x10
00343248  0F 85 87 03 00 00               jne 0x1403435d5
0034324E  48 8D 81 E8 01 00 00            lea rax, [rcx + 0x1e8]
00343255  48 8D 50 20                     lea rdx, [rax + 0x20]
00343259  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00343260  48 3B C2                        cmp rax, rdx
00343263  73 30                           jae 0x140343295
00343265  48 8B 08                        mov rcx, qword ptr [rax]
00343268  48 3B CF                        cmp rcx, rdi
0034326B  74 06                           je 0x140343273
0034326D  48 83 C0 08                     add rax, 8
00343271  EB ED                           jmp 0x140343260
00343273  33 FF                           xor edi, edi
00343275  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0034327A  8B C7                           mov eax, edi
0034327C  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00343281  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00343286  48 83 C4 30                     add rsp, 0x30
0034328A  41 5F                           pop r15
0034328C  41 5E                           pop r14
0034328E  41 5D                           pop r13
00343290  41 5C                           pop r12
00343292  5F                              pop rdi
00343293  C3                              ret
00343294  CC                              int3
00343295  49 8D 8E 40 02 00 00            lea rcx, [r14 + 0x240]
0034329C  E8 3F AA F0 FF                  call 0x14024dce0
003432A1  49 8D 8E 08 02 00 00            lea rcx, [r14 + 0x208]
003432A8  0F B6 E8                        movzx ebp, al
003432AB  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
003432AF  48 8B 19                        mov rbx, qword ptr [rcx]
003432B2  A8 01                           test al, 1
003432B4  0F 85 EF 03 00 00               jne 0x1403436a9
003432BA  0F B6 C8                        movzx ecx, al
003432BD  83 E1 01                        and ecx, 1
003432C0  48 85 DB                        test rbx, rbx
003432C3  74 2E                           je 0x1403432f3
003432C5  48 39 7B 18                     cmp qword ptr [rbx + 0x18], rdi
003432C9  77 14                           ja 0x1403432df
003432CB  73 26                           jae 0x1403432f3
003432CD  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
003432D1  85 C9                           test ecx, ecx
003432D3  74 16                           je 0x1403432eb
003432D5  48 85 C0                        test rax, rax
003432D8  74 11                           je 0x1403432eb
003432DA  48 33 D8                        xor rbx, rax
003432DD  EB 0F                           jmp 0x1403432ee
003432DF  48 8B 03                        mov rax, qword ptr [rbx]
003432E2  85 C9                           test ecx, ecx
003432E4  74 05                           je 0x1403432eb
003432E6  48 85 C0                        test rax, rax
003432E9  75 EF                           jne 0x1403432da
003432EB  48 8B D8                        mov rbx, rax
003432EE  48 85 DB                        test rbx, rbx
003432F1  75 D2                           jne 0x1403432c5
003432F3  49 8D 8E 40 02 00 00            lea rcx, [r14 + 0x240]
003432FA  E8 91 72 F0 FF                  call 0x14024a590
003432FF  44 39 2D 1A 3A C8 00            cmp dword ptr [rip + 0xc83a1a], r13d
00343306  74 0D                           je 0x140343315
00343308  44 0F 20 C1                     mov rcx, cr8
0034330C  40 0F B6 D5                     movzx edx, bpl
00343310  E8 83 23 1B 00                  call 0x1404f5698
00343315  44 0F 22 C5                     mov cr8, rbp
00343319  48 85 DB                        test rbx, rbx
0034331C  0F 85 E0 03 00 00               jne 0x140343702
00343322  8D 53 30                        lea edx, [rbx + 0x30]
00343325  41 B8 43 63 50 6E               mov r8d, 0x6e506343
0034332B  8D 4B 40                        lea ecx, [rbx + 0x40]
0034332E  E8 BD ED 83 00                  call 0x140b820f0
00343333  48 8B E8                        mov rbp, rax
00343336  48 85 C0                        test rax, rax
00343339  0F 84 99 03 00 00               je 0x1403436d8
0034333F  0F 57 C0                        xorps xmm0, xmm0
00343342  BA 44 66 6C 74                  mov edx, 0x746c6644
00343347  0F 11 00                        movups xmmword ptr [rax], xmm0
0034334A  48 8B CE                        mov rcx, rsi
0034334D  0F 11 40 10                     movups xmmword ptr [rax + 0x10], xmm0
00343351  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00343355  E8 B6 D3 EC FF                  call 0x140210710
0034335A  49 8D 8E 40 02 00 00            lea rcx, [r14 + 0x240]
00343361  48 89 75 28                     mov qword ptr [rbp + 0x28], rsi
00343365  48 89 7D 18                     mov qword ptr [rbp + 0x18], rdi
00343369  E8 22 53 F0 FF                  call 0x140248690
0034336E  49 8D B6 08 02 00 00            lea rsi, [r14 + 0x208]
00343375  0F B6 D8                        movzx ebx, al
00343378  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0034337C  48 8B 0E                        mov rcx, qword ptr [rsi]
0034337F  A8 01                           test al, 1
00343381  0F 85 33 03 00 00               jne 0x1403436ba
00343387  0F B6 D0                        movzx edx, al
0034338A  83 E2 01                        and edx, 1
0034338D  48 85 C9                        test rcx, rcx
00343390  0F 84 E1 00 00 00               je 0x140343477
00343396  48 39 79 18                     cmp qword ptr [rcx + 0x18], rdi
0034339A  0F 82 AD 00 00 00               jb 0x14034344d
003433A0  0F 87 B9 00 00 00               ja 0x14034345f
003433A6  45 33 FF                        xor r15d, r15d
003433A9  41 8B FF                        mov edi, r15d
003433AC  F6 05 53 37 C8 00 01            test byte ptr [rip + 0xc83753], 1
003433B3  49 8D 8E 40 02 00 00            lea rcx, [r14 + 0x240]
003433BA  0F 85 BA 02 00 00               jne 0x14034367a
003433C0  44 89 39                        mov dword ptr [rcx], r15d
003433C3  44 39 2D 56 39 C8 00            cmp dword ptr [rip + 0xc83956], r13d
003433CA  74 0C                           je 0x1403433d8
003433CC  44 0F 20 C1                     mov rcx, cr8
003433D0  0F B6 D3                        movzx edx, bl
003433D3  E8 C0 22 1B 00                  call 0x1404f5698
003433D8  44 0F 22 C3                     mov cr8, rbx
003433DC  44 39 2D 2D 1C C8 00            cmp dword ptr [rip + 0xc81c2d], r13d
003433E3  48 8B 75 28                     mov rsi, qword ptr [rbp + 0x28]
003433E7  74 15                           je 0x1403433fe
003433E9  33 D2                           xor edx, edx
003433EB  48 8D 4E D0                     lea rcx, [rsi - 0x30]
003433EF  41 B9 44 66 6C 74               mov r9d, 0x746c6644
003433F5  44 8D 42 01                     lea r8d, [rdx + 1]
003433F9  E8 E6 D5 EC FF                  call 0x1402109e4
003433FE  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00343405  F0 48 0F C1 46 D0               lock xadd qword ptr [rsi - 0x30], rax
0034340B  48 83 E8 01                     sub rax, 1
0034340F  7E 0F                           jle 0x140343420
00343411  33 D2                           xor edx, edx
00343413  48 8B CD                        mov rcx, rbp
00343416  E8 55 F4 83 00                  call 0x140b82870
0034341B  E9 55 FE FF FF                  jmp 0x140343275
00343420  48 8B 4E D8                     mov rcx, qword ptr [rsi - 0x28]
00343424  48 85 C9                        test rcx, rcx
00343427  0F 85 41 01 00 00               jne 0x14034356e
0034342D  48 85 C0                        test rax, rax
00343430  0F 89 B6 01 00 00               jns 0x1403435ec
00343436  33 D2                           xor edx, edx
00343438  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0034343D  44 8D 49 02                     lea r9d, [rcx + 2]
00343441  4C 8B C6                        mov r8, rsi
00343444  8D 4A 18                        lea ecx, [rdx + 0x18]
00343447  E8 14 A2 1B 00                  call 0x1404fd660
0034344C  CC                              int3
0034344D  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00343451  85 D2                           test edx, edx
00343453  74 16                           je 0x14034346b
00343455  48 85 C0                        test rax, rax
00343458  74 11                           je 0x14034346b
0034345A  48 33 C8                        xor rcx, rax
0034345D  EB 0F                           jmp 0x14034346e
0034345F  48 8B 01                        mov rax, qword ptr [rcx]
00343462  85 D2                           test edx, edx
00343464  74 05                           je 0x14034346b
00343466  48 85 C0                        test rax, rax
00343469  75 EF                           jne 0x14034345a
0034346B  48 8B C8                        mov rcx, rax
0034346E  48 85 C9                        test rcx, rcx
00343471  0F 85 1F FF FF FF               jne 0x140343396
00343477  4D 39 AE 38 02 00 00            cmp qword ptr [r14 + 0x238], r13
0034347E  0F 85 13 02 00 00               jne 0x140343697
00343484  49 8D 8E 68 01 00 00            lea rcx, [r14 + 0x168]
0034348B  E8 90 31 ED FF                  call 0x140216620
00343490  45 33 FF                        xor r15d, r15d
00343493  44 0F B6 E0                     movzx r12d, al
00343497  84 C0                           test al, al
00343499  0F 84 00 02 00 00               je 0x14034369f
0034349F  48 8D 05 7A D9 F7 FF            lea rax, [rip - 0x82686]
003434A6  4D 89 B6 38 02 00 00            mov qword ptr [r14 + 0x238], r14
003434AD  49 89 86 30 02 00 00            mov qword ptr [r14 + 0x230], rax
003434B4  45 8D 6F 01                     lea r13d, [r15 + 1]
003434B8  4D 89 BE 20 02 00 00            mov qword ptr [r14 + 0x220], r15
003434BF  49 8B 86 18 02 00 00            mov rax, qword ptr [r14 + 0x218]
003434C6  48 8D 4D 20                     lea rcx, [rbp + 0x20]
003434CA  48 89 01                        mov qword ptr [rcx], rax
003434CD  49 89 8E 18 02 00 00            mov qword ptr [r14 + 0x218], rcx
003434D4  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
003434D8  48 8B 16                        mov rdx, qword ptr [rsi]
003434DB  A8 01                           test al, 1
003434DD  0F 85 E8 01 00 00               jne 0x1403436cb
003434E3  0F B6 C8                        movzx ecx, al
003434E6  45 32 C0                        xor r8b, r8b
003434E9  83 E1 01                        and ecx, 1
003434EC  48 85 D2                        test rdx, rdx
003434EF  74 22                           je 0x140343513
003434F1  48 39 7A 18                     cmp qword ptr [rdx + 0x18], rdi
003434F5  0F 87 B6 00 00 00               ja 0x1403435b1
003434FB  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
003434FF  85 C9                           test ecx, ecx
00343501  0F 84 DB 00 00 00               je 0x1403435e2
00343507  48 85 C0                        test rax, rax
0034350A  0F 85 CF 00 00 00               jne 0x1403435df
00343510  41 B0 01                        mov r8b, 1
00343513  4C 8B CD                        mov r9, rbp
00343516  48 8B CE                        mov rcx, rsi
00343519  E8 52 10 FA FF                  call 0x1402e4570
0034351E  49 8D 8E 40 02 00 00            lea rcx, [r14 + 0x240]
00343525  0F B6 D3                        movzx edx, bl
00343528  E8 C3 D9 F7 FF                  call 0x1402c0ef0
0034352D  45 85 ED                        test r13d, r13d
00343530  0F 85 FE 01 00 00               jne 0x140343734
00343536  41 FE 86 44 02 00 00            inc byte ptr [r14 + 0x244]
0034353D  90                              nop
0034353E  41 0F B6 86 44 02 00 00         movzx eax, byte ptr [r14 + 0x244]
00343546  83 E0 03                        and eax, 3
00343549  49 89 BC C6 E8 01 00 00         mov qword ptr [r14 + rax*8 + 0x1e8], rdi
00343551  41 8B FF                        mov edi, r15d
00343554  45 84 E4                        test r12b, r12b
00343557  0F 84 18 FD FF FF               je 0x140343275
0034355D  49 8D 8E 68 01 00 00            lea rcx, [r14 + 0x168]
00343564  E8 17 69 00 00                  call 0x140349e80
00343569  E9 07 FD FF FF                  jmp 0x140343275
0034356E  41 B9 01 00 00 00               mov r9d, 1
00343574  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00343579  4C 8D 15 80 CA CB FF            lea r10, [rip - 0x343580]
00343580  4C 8B C6                        mov r8, rsi
00343583  48 8D 46 D0                     lea rax, [rsi - 0x30]
00343587  48 C1 E8 08                     shr rax, 8
0034358B  0F B6 D0                        movzx edx, al
0034358E  41 8D 49 17                     lea ecx, [r9 + 0x17]
00343592  0F B6 46 E8                     movzx eax, byte ptr [rsi - 0x18]
00343596  48 33 D0                        xor rdx, rax
00343599  0F B6 05 AC 38 C8 00            movzx eax, byte ptr [rip + 0xc838ac]
003435A0  48 33 D0                        xor rdx, rax
003435A3  49 8B 94 D2 00 78 FC 00         mov rdx, qword ptr [r10 + rdx*8 + 0xfc7800]
003435AB  E8 B0 A0 1B 00                  call 0x1404fd660
003435B0  CC                              int3
003435B1  48 8B 02                        mov rax, qword ptr [rdx]
003435B4  85 C9                           test ecx, ecx
003435B6  74 0C                           je 0x1403435c4
003435B8  48 85 C0                        test rax, rax
003435BB  0F 84 52 FF FF FF               je 0x140343513
003435C1  48 33 C2                        xor rax, rdx
003435C4  48 85 C0                        test rax, rax
003435C7  0F 84 46 FF FF FF               je 0x140343513
003435CD  48 8B D0                        mov rdx, rax
003435D0  E9 1C FF FF FF                  jmp 0x1403434f1
003435D5  BF BB 00 00 C0                  mov edi, 0xc00000bb
003435DA  E9 96 FC FF FF                  jmp 0x140343275
003435DF  48 33 C2                        xor rax, rdx
003435E2  48 85 C0                        test rax, rax
003435E5  75 E6                           jne 0x1403435cd
003435E7  E9 24 FF FF FF                  jmp 0x140343510
003435EC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003435F5  66 44 39 A8 E6 01 00 00         cmp word ptr [rax + 0x1e6], r13w
003435FD  0F 85 F1 00 00 00               jne 0x1403436f4
00343603  E8 58 4A FB FF                  call 0x1402f8060
00343608  84 C0                           test al, al
0034360A  0F 84 E4 00 00 00               je 0x1403436f4
00343610  44 0F 20 C0                     mov rax, cr8
00343614  3C 01                           cmp al, 1
00343616  0F 83 D8 00 00 00               jae 0x1403436f4
0034361C  0F B6 46 EA                     movzx eax, byte ptr [rsi - 0x16]
00343620  A8 40                           test al, 0x40
00343622  75 2C                           jne 0x140343650
00343624  44 39 2D E5 19 C8 00            cmp dword ptr [rip + 0xc819e5], r13d
0034362B  74 09                           je 0x140343636
0034362D  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00343631  E8 42 49 69 00                  call 0x1409d7f78
00343636  33 D2                           xor edx, edx
00343638  48 8D 4E D0                     lea rcx, [rsi - 0x30]
0034363C  E8 1F 14 52 00                  call 0x140864a60
00343641  33 D2                           xor edx, edx
00343643  48 8B CD                        mov rcx, rbp
00343646  E8 25 F2 83 00                  call 0x140b82870
0034364B  E9 25 FC FF FF                  jmp 0x140343275
00343650  83 E0 7F                        and eax, 0x7f
00343653  4C 8D 15 A6 C9 CB FF            lea r10, [rip - 0x34365a]
0034365A  48 8D 4E D0                     lea rcx, [rsi - 0x30]
0034365E  42 0F B6 84 10 80 FF F0 00      movzx eax, byte ptr [rax + r10 + 0xf0ff80]
00343667  48 2B C8                        sub rcx, rax
0034366A  48 8B 09                        mov rcx, qword ptr [rcx]
0034366D  44 38 69 18                     cmp byte ptr [rcx + 0x18], r13b
00343671  74 B1                           je 0x140343624
00343673  E8 B8 47 69 00                  call 0x1409d7e30
00343678  EB AA                           jmp 0x140343624
0034367A  8B 05 D8 A7 BC 00               mov eax, dword ptr [rip + 0xbca7d8]
00343680  85 C0                           test eax, eax
00343682  0F 85 38 FD FF FF               jne 0x1403433c0
00343688  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0034368D  E8 B2 D8 F7 FF                  call 0x1402c0f44
00343692  E9 2C FD FF FF                  jmp 0x1403433c3
00343697  45 33 FF                        xor r15d, r15d
0034369A  E9 20 FE FF FF                  jmp 0x1403434bf
0034369F  BF 89 01 00 C0                  mov edi, 0xc0000189
003436A4  E9 03 FD FF FF                  jmp 0x1403433ac
003436A9  48 85 DB                        test rbx, rbx
003436AC  0F 84 41 FC FF FF               je 0x1403432f3
003436B2  48 33 D9                        xor rbx, rcx
003436B5  E9 00 FC FF FF                  jmp 0x1403432ba
003436BA  48 85 C9                        test rcx, rcx
003436BD  0F 84 B4 FD FF FF               je 0x140343477
003436C3  48 33 CE                        xor rcx, rsi
003436C6  E9 BC FC FF FF                  jmp 0x140343387
003436CB  48 85 D2                        test rdx, rdx
003436CE  74 1C                           je 0x1403436ec
003436D0  48 33 D6                        xor rdx, rsi
003436D3  E9 0B FE FF FF                  jmp 0x1403434e3
003436D8  41 F6 86 E4 01 00 00 02         test byte ptr [r14 + 0x1e4], 2
003436E0  74 46                           je 0x140343728
003436E2  BF 9A 00 00 C0                  mov edi, 0xc000009a
003436E7  E9 89 FB FF FF                  jmp 0x140343275
003436EC  45 32 C0                        xor r8b, r8b
003436EF  E9 1F FE FF FF                  jmp 0x140343513
003436F4  48 8D 4E D0                     lea rcx, [rsi - 0x30]
003436F8  E8 97 EC 05 00                  call 0x1403a2394
003436FD  E9 0F FD FF FF                  jmp 0x140343411
00343702  41 FE 86 44 02 00 00            inc byte ptr [r14 + 0x244]
00343709  90                              nop
0034370A  41 0F B6 86 44 02 00 00         movzx eax, byte ptr [r14 + 0x244]
00343712  83 E0 03                        and eax, 3
00343715  45 33 FF                        xor r15d, r15d
00343718  49 89 BC C6 E8 01 00 00         mov qword ptr [r14 + rax*8 + 0x1e8], rdi
00343720  41 8B FF                        mov edi, r15d
00343723  E9 4D FB FF FF                  jmp 0x140343275
00343728  66 F0 41 83 8E E4 01 00 00 02   lock or word ptr [r14 + 0x1e4], 2
00343732  EB AE                           jmp 0x1403436e2
00343734  45 32 E4                        xor r12b, r12b
00343737  49 8D 8E 20 02 00 00            lea rcx, [r14 + 0x220]
0034373E  BA 01 00 00 00                  mov edx, 1
00343743  E8 D8 5D FB FF                  call 0x1402f9520
00343748  E9 E9 FD FF FF                  jmp 0x140343536
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfSnGetFileInformation(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_r12 = 0;
    v_r13 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 52)))) & (16)) != 0) goto loc_003435D5;
loc_00343260:
    if ((a1 + 488) >= (a1 + 488 + 32)) goto loc_00343295;
    if ((*(unsigned __int64 *)(a1 + 488)) == (*(unsigned __int64 *)(a2 + 24))) goto loc_00343273;
    result = (a1 + 488) + (8);
    goto loc_00343260;
loc_00343273:
    v_rdi = 0;
loc_00343275:
    v_rsp = (v_rsp) + (48);
    return 0;
loc_00343295:
    result = ExAcquireSpinLockShared(a1 + 576, a1 + 488 + 32, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 52)), a4);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 520 + 8))) & (1)) != 0) goto loc_003436A9;
loc_003432BA:
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(a1 + 520 + 8))) & (1));
    if (*(unsigned __int64 *)(a1 + 520) == 0) goto loc_003432F3;
loc_003432C5:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 520) + 24)) > 0) goto loc_003432DF;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 520) + 24)) >= 0) goto loc_003432F3;
    if ((unsigned int)(a1) == 0) goto loc_003432EB;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 520) + 8) == 0) goto loc_003432EB;
loc_003432DA:
    v_rbx = (*(unsigned __int64 *)(a1 + 520)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 520) + 8));
    goto loc_003432EE;
loc_003432DF:
    if ((unsigned int)(a1) == 0) goto loc_003432EB;
    if (*(unsigned __int64 *)(v_rbx) != 0) goto loc_003432DA;
loc_003432EB:
loc_003432EE:
    if (*(unsigned __int64 *)(v_rbx) != 0) goto loc_003432C5;
loc_003432F3:
    result = ExReleaseSpinLockSharedFromDpcLevel(a1 + 576, a1 + 488 + 32, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 52)), a4);
    if ((*(unsigned int *)(v_rip + 13122074)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 8) + 52)), a4);
    }
    if (*(unsigned __int64 *)(v_rbx) != 0) goto loc_00343702;
    result = ExAllocatePool2(*(unsigned __int64 *)(v_rbx) + 64, *(unsigned __int64 *)(v_rbx) + 48, (unsigned int)(0x6E506343ULL), a4);
    if (result == 0) goto loc_003436D8;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    result = ObfReferenceObjectWithTag(v_stack_p18, (unsigned int)(0x746C6644ULL), (unsigned int)(0x6E506343ULL), a4);
    *(unsigned __int64 *)(result + 40) = v_stack_p18;
    *(unsigned __int64 *)(result + 24) = 0;
    result = ExAcquireSpinLockExclusive(a1 + 576, (unsigned int)(0x746C6644ULL), (unsigned int)(0x6E506343ULL), a4);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 520 + 8))) & (1)) != 0) goto loc_003436BA;
loc_00343387:
    a2 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(a1 + 520 + 8))) & (1));
    if (*(unsigned __int64 *)(a1 + 520) == 0) goto loc_00343477;
loc_00343396:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 520) + 24)) < 0) goto loc_0034344D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 520) + 24)) > 0) goto loc_0034345F;
    v_r15 = 0;
loc_003433AC:
    if (((*(unsigned __int8 *)(v_rip + 13121363)) & (1)) != 0) goto loc_0034367A;
loc_003433C0:
    *(unsigned int *)(a1 + 576) = 0;
loc_003433C3:
    result = *(unsigned __int64 *)(a1 + 520 + 8);
    if ((*(unsigned int *)(v_rip + 13121878)) != 0) {
        a1 = (unsigned __int8)(result);
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, (unsigned int)(0x6E506343ULL), a4);
    }
    if ((*(unsigned int *)(v_rip + 13114413)) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(result + 40) - 48;
        a4 = 0x746C6644ULL;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_00343420;
loc_00343411:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    goto loc_00343275;
loc_00343420:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) - 40) != 0) goto loc_0034356E;
    if (!sign_flag) goto loc_003435EC;
    a2 = 0;
    v_stack_p20 = result;
    result = KeBugCheckEx(a2 + 24, a2, *(unsigned __int64 *)(result + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) - 40) + 2);
loc_0034344D:
    if (0 == 0) goto loc_0034346B;
    if (*(unsigned __int64 *)(a2 + 24 + 8) == 0) goto loc_0034346B;
loc_0034345A:
    a1 = (a2 + 24) ^ (*(unsigned __int64 *)(a2 + 24 + 8));
    goto loc_0034346E;
loc_0034345F:
    if (0 == 0) goto loc_0034346B;
    if (*(unsigned __int64 *)(a1) != 0) goto loc_0034345A;
loc_0034346B:
loc_0034346E:
    if (*(unsigned __int64 *)(a1) != 0) goto loc_00343396;
loc_00343477:
    if ((*(unsigned __int64 *)(a1 + 568)) != 0) goto loc_00343697;
    result = ExAcquireRundownProtection(a1 + 360, a2, *(unsigned __int64 *)(result + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) - 40) + 2);
    v_r15 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0034369F;
    *(unsigned __int64 *)(a1 + 568) = a1;
    *(unsigned __int64 *)(a1 + 560) = v_rip - 534150;
    *(unsigned __int64 *)(a1 + 544) = 0;
loc_003434BF:
    *(unsigned __int64 *)(result + 32) = *(unsigned __int64 *)(a1 + 536);
    *(unsigned __int64 *)(a1 + 536) = result + 32;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) + 8))) & (1)) != 0) goto loc_003436CB;
loc_003434E3:
    a3 = 0;
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) + 8))) & (1));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40)) == 0) goto loc_00343513;
loc_003434F1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40)) + 24)) > 0) goto loc_003435B1;
    if ((unsigned int)(a1) == 0) goto loc_003435E2;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40)) + 8) != 0) goto loc_003435DF;
loc_00343510:
loc_00343513:
    result = RtlRbInsertNodeEx(*(unsigned __int64 *)(result + 40), *(unsigned __int64 *)(*(unsigned __int64 *)(result + 40)), 1, result);
    result = ExReleaseSpinLockExclusive(a1 + 576, (unsigned __int8)((unsigned __int8)(result)), 1, result);
    if ((unsigned int)(v_r15 + 1) != 0) goto loc_00343734;
loc_00343536:
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 580)) & (3));
    *(unsigned __int64 *)(a1 + result * 8 + 488) = 0;
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_00343275;
    result = ExReleaseRundownProtection(a1 + 360, (unsigned __int8)((unsigned __int8)(result)), 1, result);
    goto loc_00343275;
loc_0034356E:
    v_stack_p20 = a1 + 360;
    result = (*(unsigned __int64 *)(result + 40) - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(result + 40) - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 13121708));
    result = KeBugCheckEx(1 + 23, *(unsigned __int64 *)(v_rip - 3421568 + a2 * 8 + 16545792), *(unsigned __int64 *)(result + 40), 1);
loc_003435B1:
    if ((unsigned int)(1 + 23) == 0) goto loc_003435C4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3421568 + a2 * 8 + 16545792)) == 0) goto loc_00343513;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 3421568 + a2 * 8 + 16545792))) ^ (*(unsigned __int64 *)(v_rip - 3421568 + a2 * 8 + 16545792));
loc_003435C4:
    if (result == 0) goto loc_00343513;
loc_003435CD:
    goto loc_003434F1;
loc_003435D5:
    goto loc_00343275;
loc_003435DF:
    result = (result) ^ (result);
loc_003435E2:
    if (result != 0) goto loc_003435CD;
    goto loc_00343510;
loc_003435EC:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != ((unsigned __int16)(v_r15 + 1))) goto loc_003436F4;
    result = KeAreInterruptsEnabled(1 + 23, result, *(unsigned __int64 *)(result + 40), 1);
    if ((unsigned __int8)(result) == 0) goto loc_003436F4;
    if (((unsigned __int8)((unsigned __int8)(result))) >= 1) goto loc_003436F4;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 40) - 22))) & (64)) != 0) goto loc_00343650;
loc_00343624:
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(result + 40) - 22);
    if ((*(unsigned int *)(v_rip + 13113829)) != ((unsigned int)(v_r15 + 1))) {
        a1 = *(unsigned __int64 *)(result + 40) - 48;
        result = ObpDeregisterObject(a1, result, *(unsigned __int64 *)(result + 40), 1);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(*(unsigned __int64 *)(result + 40) - 48, a2, *(unsigned __int64 *)(result + 40), 1);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, *(unsigned __int64 *)(result + 40), 1);
    goto loc_00343275;
loc_00343650:
    result = (unsigned int)((result) & (127));
    a1 = (*(unsigned __int64 *)(result + 40) - 48) - (*(unsigned __int8 *)(result + v_rip - 3421786 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == ((unsigned __int8)(v_r15 + 1))) goto loc_00343624;
    result = ObpHandleRevocationBlockRemoveObject(*(unsigned __int64 *)(a1), a2, *(unsigned __int64 *)(result + 40), 1);
    goto loc_00343624;
loc_0034367A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12363736))) != 0) goto loc_003433C0;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(*(unsigned __int64 *)(a1), v_stack_p58, *(unsigned __int64 *)(result + 40), 1);
    goto loc_003433C3;
loc_00343697:
    v_r15 = 0;
    goto loc_003434BF;
loc_0034369F:
    goto loc_003433AC;
loc_003436A9:
    if ((unsigned __int8)(result) == 0) goto loc_003432F3;
    v_rbx = ((unsigned __int8)(result)) ^ (*(unsigned __int64 *)(a1));
    goto loc_003432BA;
loc_003436BA:
    if (*(unsigned __int64 *)(a1) == 0) goto loc_00343477;
    a1 = (*(unsigned __int64 *)(a1)) ^ (*(unsigned __int64 *)(result + 40));
    goto loc_00343387;
loc_003436CB:
    if (v_stack_p58 == 0) goto loc_003436EC;
    a2 = (v_stack_p58) ^ (*(unsigned __int64 *)(result + 40));
    goto loc_003434E3;
loc_003436D8:
    if (((*(unsigned __int8 *)(a1 + 484)) & (2)) == 0) goto loc_00343728;
loc_003436E2:
    goto loc_00343275;
loc_003436EC:
    a3 = 0;
    goto loc_00343513;
loc_003436F4:
    result = ObpDeferObjectDeletion(*(unsigned __int64 *)(result + 40) - 48, a2, a3, 1);
    goto loc_00343411;
loc_00343702:
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 580)) & (3));
    v_r15 = 0;
    *(unsigned __int64 *)(a1 + result * 8 + 488) = (unsigned int)(0xC000009AULL);
    goto loc_00343275;
loc_00343728:
    goto loc_003436E2;
loc_00343734:
    v_r12 = 0;
    result = ExQueueWorkItem(a1 + 544, 1, a3, 1);
    goto loc_00343536;
}
```

## 5. (Beta) C Style

```c
int64_t PfSnGetFileInformation(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p58;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    local_r12 = 0;
    local_r13 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x34)))) & (16)) != 0) goto loc_003435D5;
loc_00343260:
    if ((Arg1 + 488) >= (Arg1 + 488 + 32)) goto loc_00343295;
    if ((*(uint64_t *)(arg1 + 0x1E8)) == (*(uint64_t *)(arg2 + 0x18))) goto loc_00343273;
    result = (Arg1 + 488) + (8);
    goto loc_00343260;
loc_00343273:
    local_rdi = 0;
loc_00343275:
    local_rsp = (local_rsp) + (48);
    return 0;
loc_00343295:
    result = ExAcquireSpinLockShared(Arg1 + 576, Arg1 + 488 + 32, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x34)), a4);
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x208 + 0x8))) & (1)) != 0) goto loc_003436A9;
loc_003432BA:
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(arg1 + 0x208 + 0x8))) & (1));
    if (*(uint64_t *)(arg1 + 0x208) == 0) goto loc_003432F3;
loc_003432C5:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x208) + 0x18)) > 0) goto loc_003432DF;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x208) + 0x18)) >= 0) goto loc_003432F3;
    if ((uint32_t)(Arg1) == 0) goto loc_003432EB;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x208) + 0x8) == 0) goto loc_003432EB;
loc_003432DA:
    local_rbx = (*(uint64_t *)(arg1 + 0x208)) ^ (*(uint64_t *)(*(uint64_t *)(arg1 + 0x208) + 0x8));
    goto loc_003432EE;
loc_003432DF:
    if ((uint32_t)(Arg1) == 0) goto loc_003432EB;
    if (*(uint64_t *)(local_rbx) != 0) goto loc_003432DA;
loc_003432EB:
loc_003432EE:
    if (*(uint64_t *)(local_rbx) != 0) goto loc_003432C5;
loc_003432F3:
    result = ExReleaseSpinLockSharedFromDpcLevel(Arg1 + 576, Arg1 + 488 + 32, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x34)), a4);
    if ((*(uint32_t *)(v_rip + 0xC83A1A)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x8) + 0x34)), a4);
    }
    if (*(uint64_t *)(local_rbx) != 0) goto loc_00343702;
    result = ExAllocatePool2(*(uint64_t *)(local_rbx) + 64, *(uint64_t *)(local_rbx) + 48, (uint32_t)(0x6E506343ULL), a4);
    if (result == 0) goto loc_003436D8;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    result = ObfReferenceObjectWithTag(v_stack_p18, (uint32_t)(0x746C6644ULL), (uint32_t)(0x6E506343ULL), a4);
    *(uint64_t *)(result + 0x28) = v_stack_p18;
    *(uint64_t *)(result + 0x18) = 0;
    result = ExAcquireSpinLockExclusive(Arg1 + 576, (uint32_t)(0x746C6644ULL), (uint32_t)(0x6E506343ULL), a4);
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x208 + 0x8))) & (1)) != 0) goto loc_003436BA;
loc_00343387:
    Arg2 = (uint32_t)(((uint8_t)(*(uint64_t *)(arg1 + 0x208 + 0x8))) & (1));
    if (*(uint64_t *)(arg1 + 0x208) == 0) goto loc_00343477;
loc_00343396:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x208) + 0x18)) < 0) goto loc_0034344D;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x208) + 0x18)) > 0) goto loc_0034345F;
    local_r15 = 0;
loc_003433AC:
    if (((*(uint8_t *)(v_rip + 0xC83753)) & (1)) != 0) goto loc_0034367A;
loc_003433C0:
    *(uint32_t *)(arg1 + 0x240) = 0;
loc_003433C3:
    result = *(uint64_t *)(arg1 + 0x208 + 0x8);
    if ((*(uint32_t *)(v_rip + 0xC83956)) != 0) {
        Arg1 = (uint8_t)(result);
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)(0x6E506343ULL), a4);
    }
    if ((*(uint32_t *)(v_rip + 0xC81C2D)) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(result + 0x28) - 48;
        a4 = 0x746C6644ULL;
        a3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, a3, a4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_00343420;
loc_00343411:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, a3, a4);
    goto loc_00343275;
loc_00343420:
    if (*(uint64_t *)(*(uint64_t *)(result + 0x28) - 0x28) != 0) goto loc_0034356E;
    if (!sign_flag) goto loc_003435EC;
    Arg2 = 0;
    v_stack_p20 = result;
    result = KeBugCheckEx(Arg2 + 24, Arg2, *(uint64_t *)(result + 0x28), *(uint64_t *)(*(uint64_t *)(result + 0x28) - 0x28) + 2);
loc_0034344D:
    if (0 == 0) goto loc_0034346B;
    if (*(uint64_t *)(arg2 + 0x18 + 0x8) == 0) goto loc_0034346B;
loc_0034345A:
    Arg1 = (Arg2 + 24) ^ (*(uint64_t *)(arg2 + 0x18 + 0x8));
    goto loc_0034346E;
loc_0034345F:
    if (0 == 0) goto loc_0034346B;
    if (*(uint64_t *)(arg1) != 0) goto loc_0034345A;
loc_0034346B:
loc_0034346E:
    if (*(uint64_t *)(arg1) != 0) goto loc_00343396;
loc_00343477:
    if ((*(uint64_t *)(arg1 + 0x238)) != 0) goto loc_00343697;
    result = ExAcquireRundownProtection(Arg1 + 360, Arg2, *(uint64_t *)(result + 0x28), *(uint64_t *)(*(uint64_t *)(result + 0x28) - 0x28) + 2);
    local_r15 = 0;
    if ((uint8_t)(result) == 0) goto loc_0034369F;
    *(void **)(arg1 + 0x238) = Arg1;
    *(uint64_t *)(arg1 + 0x230) = v_rip - 534150;
    *(uint64_t *)(arg1 + 0x220) = 0;
loc_003434BF:
    *(uint64_t *)(result + 0x20) = *(uint64_t *)(arg1 + 0x218);
    *(uint64_t *)(arg1 + 0x218) = result + 32;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x28) + 0x8))) & (1)) != 0) goto loc_003436CB;
loc_003434E3:
    a3 = 0;
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x28) + 0x8))) & (1));
    if (*(uint64_t *)(*(uint64_t *)(result + 0x28)) == 0) goto loc_00343513;
loc_003434F1:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x28)) + 0x18)) > 0) goto loc_003435B1;
    if ((uint32_t)(Arg1) == 0) goto loc_003435E2;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x28)) + 0x8) != 0) goto loc_003435DF;
loc_00343510:
loc_00343513:
    result = RtlRbInsertNodeEx(*(uint64_t *)(result + 0x28), *(uint64_t *)(*(uint64_t *)(result + 0x28)), 1, result);
    result = ExReleaseSpinLockExclusive(Arg1 + 576, (uint8_t)((uint8_t)(result)), 1, result);
    if ((uint32_t)(local_r15 + 1) != 0) goto loc_00343734;
loc_00343536:
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x244)) & (3));
    *(uint64_t *)(arg1 + result * 8 + 0x1E8) = 0;
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_00343275;
    result = ExReleaseRundownProtection(Arg1 + 360, (uint8_t)((uint8_t)(result)), 1, result);
    goto loc_00343275;
loc_0034356E:
    v_stack_p20 = Arg1 + 360;
    result = (*(uint64_t *)(result + 0x28) - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(*(uint64_t *)(result + 0x28) - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xC838AC));
    result = KeBugCheckEx(1 + 23, *(uint64_t *)(v_rip - 0x343580 + arg2 * 8 + 0xFC7800), *(uint64_t *)(result + 0x28), 1);
loc_003435B1:
    if ((uint32_t)(1 + 23) == 0) goto loc_003435C4;
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x343580 + arg2 * 8 + 0xFC7800)) == 0) goto loc_00343513;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x343580 + arg2 * 8 + 0xFC7800))) ^ (*(uint64_t *)(v_rip - 0x343580 + arg2 * 8 + 0xFC7800));
loc_003435C4:
    if (result == 0) goto loc_00343513;
loc_003435CD:
    goto loc_003434F1;
loc_003435D5:
    goto loc_00343275;
loc_003435DF:
    result = (result) ^ (result);
loc_003435E2:
    if (result != 0) goto loc_003435CD;
    goto loc_00343510;
loc_003435EC:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != ((uint16_t)(local_r15 + 1))) goto loc_003436F4;
    result = KeAreInterruptsEnabled(1 + 23, result, *(uint64_t *)(result + 0x28), 1);
    if ((uint8_t)(result) == 0) goto loc_003436F4;
    if (((uint8_t)((uint8_t)(result))) >= 1) goto loc_003436F4;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(result + 0x28) - 0x16))) & (64)) != 0) goto loc_00343650;
loc_00343624:
    result = *(uint8_t *)(*(uint64_t *)(result + 0x28) - 0x16);
    if ((*(uint32_t *)(v_rip + 0xC819E5)) != ((uint32_t)(local_r15 + 1))) {
        Arg1 = *(uint64_t *)(result + 0x28) - 48;
        result = ObpDeregisterObject(Arg1, result, *(uint64_t *)(result + 0x28), 1);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(*(uint64_t *)(result + 0x28) - 48, Arg2, *(uint64_t *)(result + 0x28), 1);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, *(uint64_t *)(result + 0x28), 1);
    goto loc_00343275;
loc_00343650:
    result = (uint32_t)((result) & (127));
    Arg1 = (*(uint64_t *)(result + 0x28) - 48) - (*(uint8_t *)(result + v_rip - 0x34365A * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x18)) == ((uint8_t)(local_r15 + 1))) goto loc_00343624;
    result = ObpHandleRevocationBlockRemoveObject(*(uint64_t *)(arg1), Arg2, *(uint64_t *)(result + 0x28), 1);
    goto loc_00343624;
loc_0034367A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBCA7D8))) != 0) goto loc_003433C0;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(*(uint64_t *)(arg1), v_stack_p58, *(uint64_t *)(result + 0x28), 1);
    goto loc_003433C3;
loc_00343697:
    local_r15 = 0;
    goto loc_003434BF;
loc_0034369F:
    goto loc_003433AC;
loc_003436A9:
    if ((uint8_t)(result) == 0) goto loc_003432F3;
    local_rbx = ((uint8_t)(result)) ^ (*(uint64_t *)(arg1));
    goto loc_003432BA;
loc_003436BA:
    if (*(uint64_t *)(arg1) == 0) goto loc_00343477;
    Arg1 = (*(uint64_t *)(arg1)) ^ (*(uint64_t *)(result + 0x28));
    goto loc_00343387;
loc_003436CB:
    if (v_stack_p58 == 0) goto loc_003436EC;
    Arg2 = (v_stack_p58) ^ (*(uint64_t *)(result + 0x28));
    goto loc_003434E3;
loc_003436D8:
    if (((*(uint8_t *)(arg1 + 0x1E4)) & (2)) == 0) goto loc_00343728;
loc_003436E2:
    goto loc_00343275;
loc_003436EC:
    a3 = 0;
    goto loc_00343513;
loc_003436F4:
    result = ObpDeferObjectDeletion(*(uint64_t *)(result + 0x28) - 48, Arg2, a3, 1);
    goto loc_00343411;
loc_00343702:
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x244)) & (3));
    local_r15 = 0;
    *(uint64_t *)(arg1 + result * 8 + 0x1E8) = (uint32_t)(0xC000009AULL);
    goto loc_00343275;
loc_00343728:
    goto loc_003436E2;
loc_00343734:
    local_r12 = 0;
    result = ExQueueWorkItem(Arg1 + 544, 1, a3, 1);
    goto loc_00343536;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x168` | `64` | `R` |
| `Arg1` | `+ 0x1E4` | `8` | `R` |
| `Arg1` | `+ 0x1E4` | `16` | `R/W` |
| `Arg1` | `+ 0x1E8` | `64` | `R` |
| `Arg1` | `+ 0x1E8 + rax*8` | `64` | `W` |
| `Arg1` | `+ 0x208` | `64` | `R` |
| `Arg1` | `+ 0x218` | `64` | `R` |
| `Arg1` | `+ 0x218` | `64` | `W` |
| `Arg1` | `+ 0x220` | `64` | `R` |
| `Arg1` | `+ 0x220` | `64` | `W` |
| `Arg1` | `+ 0x230` | `64` | `W` |
| `Arg1` | `+ 0x238` | `64` | `R` |
| `Arg1` | `+ 0x238` | `64` | `W` |
| `Arg1` | `+ 0x240` | `64` | `R` |
| `Arg1` | `+ 0x244` | `8` | `R` |
| `Arg1` | `+ 0x244` | `8` | `R/W` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00343210&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
