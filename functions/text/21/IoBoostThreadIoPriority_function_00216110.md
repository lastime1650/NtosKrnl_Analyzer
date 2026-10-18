# IoBoostThreadIoPriority

- RVA: `0x00216110`–`0x00216610` (길이 `1,280` bytes)
- VA: `0x0000000140216110`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005E2F0`
- 디코드: `304`개 명령, `1,280/1,280` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0021615E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0021616D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00216188` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x002161B3` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x002161C9` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002161D9` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00216216` → [ExReferenceCallBackBlock](../2F/ExReferenceCallBackBlock_function_002F0040.md) (function, `0x002F0040`)
- `0x002162B4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00216313` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x0021637A` → [ObfReferenceObjectWithTag](ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00216387` → [ObfReferenceObjectWithTag](ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x002163AC` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x002163C4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00216405` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0021640F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00216428` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00216457` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x002164F8` → [KxAcquireQueuedSpinLock](../27/KxAcquireQueuedSpinLock_function_00273E20.md) (function, `0x00273E20`)
- `0x0021652C` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0021654C` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x002165A4` → [ObfReferenceObjectWithTag](ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x002165B3` → [ObfReferenceObjectWithTag](ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x002165E8` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x002165FE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- [ExpAcquireResourceSharedLite](ExpAcquireResourceSharedLite_function_00212040.md) at `0x00212ED8`
- [sub_002142F9](Unknown_function_002142F9.md) at `0x00214374`
- [sub_002142F9](Unknown_function_002142F9.md) at `0x0021466E`
- [sub_00215166](Unknown_function_00215166.md) at `0x00215573`
- [sub_00215E53](Unknown_function_00215E53.md) at `0x00215EA1`
- [KiAbConvertWaiterToOwnerEntry](KiAbConvertWaiterToOwnerEntry_function_00219430.md) at `0x00219A57`
- [sub_00221FB6](../22/Unknown_function_00221FB6.md) at `0x00222C8A`
- [sub_00221FB6](../22/Unknown_function_00221FB6.md) at `0x00222CEE`
- [KiAbDeferredProcessingWorker](../30/KiAbDeferredProcessingWorker_function_0030DEB0.md) at `0x0030E751`
- [KiAbDeferredProcessingWorker](../30/KiAbDeferredProcessingWorker_function_0030DEB0.md) at `0x0030E7B9`
- [PspNotifyProcessEffectiveIoLimitChanged](../3E/PspNotifyProcessEffectiveIoLimitChanged_function_003EC9C0.md) at `0x003ECB09`
- [FsRtlpWaitForIoAtEof](../41/FsRtlpWaitForIoAtEof_function_00415298.md) at `0x0041531D`
- [MiModifiedPageWriter](../47/MiModifiedPageWriter_function_0047E5F0.md) at `0x0047EA98`
- [MiModifiedPageWriter](../47/MiModifiedPageWriter_function_0047E5F0.md) at `0x0047EC02`
- [MiModifiedPageWriter](../47/MiModifiedPageWriter_function_0047E5F0.md) at `0x0047EC4F`
- [FsRtlpDoBoost](../48/FsRtlpDoBoost_function_0048B198.md) at `0x0048B264`
- [IoBoostThreadIo](../4B/IoBoostThreadIo_function_004BE560.md) at `0x004BE5A8`
- [CcBoostLowPriorityWorkerThread](../57/CcBoostLowPriorityWorkerThread_function_0057B704.md) at `0x0057B7C4`
- [NtSetInformationThread](../../page/8C/NtSetInformationThread_function_008C9F60.md) at `0x008CB6DD`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE6AF7`

### Static image references
- `0x00216134` → RVA `0x00E0A740` (`.data`; read)
- `0x002161B8` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00216206` → RVA `0x00F8D1A0` (`.data`; read)
- `0x0021627D` → RVA `0x00F8D1F0` (`.data`; read/write)
- `0x002165C0` → RVA `0x00F8D180` (`.data`; read/write)
- `0x00216608` → RVA `0x00F8D17C` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x002163C4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0021640F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00216566` → [sub_006D6740](../6D/Unknown_function_006D6740.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00216110  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00216115  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0021611A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0021611F  55                              push rbp
00216120  41 54                           push r12
00216122  41 55                           push r13
00216124  41 56                           push r14
00216126  41 57                           push r15
00216128  48 8D 6C 24 C0                  lea rbp, [rsp - 0x40]
0021612D  48 81 EC 40 01 00 00            sub rsp, 0x140
00216134  48 8B 05 05 46 BF 00            mov rax, qword ptr [rip + 0xbf4605]
0021613B  48 33 C4                        xor rax, rsp
0021613E  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00216142  89 54 24 24                     mov dword ptr [rsp + 0x24], edx
00216146  41 8B D8                        mov ebx, r8d
00216149  33 D2                           xor edx, edx
0021614B  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00216150  4C 8B E1                        mov r12, rcx
00216153  45 32 FF                        xor r15b, r15b
00216156  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0021615A  44 8D 42 40                     lea r8d, [rdx + 0x40]
0021615E  E8 DD 0A 4B 00                  call 0x1406c6c40
00216163  33 D2                           xor edx, edx
00216165  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00216169  44 8D 42 40                     lea r8d, [rdx + 0x40]
0021616D  E8 CE 0A 4B 00                  call 0x1406c6c40
00216172  45 33 F6                        xor r14d, r14d
00216175  45 8B EE                        mov r13d, r14d
00216178  85 DB                           test ebx, ebx
0021617A  0F 88 80 00 00 00               js 0x140216200
00216180  49 8D 8C 24 18 06 00 00         lea rcx, [r12 + 0x618]
00216188  E8 E3 22 FF FF                  call 0x140208470
0021618D  49 8D 8C 24 40 05 00 00         lea rcx, [r12 + 0x540]
00216195  0F B6 F8                        movzx edi, al
00216198  48 39 09                        cmp qword ptr [rcx], rcx
0021619B  0F 85 7B 02 00 00               jne 0x14021641c
002161A1  0F BA E3 1E                     bt ebx, 0x1e
002161A5  0F 82 6E 02 00 00               jb 0x140216419
002161AB  49 8D 8C 24 18 06 00 00         lea rcx, [r12 + 0x618]
002161B3  E8 B8 04 FF FF                  call 0x140206670
002161B8  44 39 35 61 0B DB 00            cmp dword ptr [rip + 0xdb0b61], r14d
002161BF  74 0D                           je 0x1402161ce
002161C1  44 0F 20 C1                     mov rcx, cr8
002161C5  40 0F B6 D7                     movzx edx, dil
002161C9  E8 CA F4 2D 00                  call 0x1404f5698
002161CE  44 0F 22 C7                     mov cr8, rdi
002161D2  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
002161D6  48 33 CC                        xor rcx, rsp
002161D9  E8 62 64 49 00                  call 0x1406ac640
002161DE  4C 8D 9C 24 40 01 00 00         lea r11, [rsp + 0x140]
002161E6  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
002161EA  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
002161EE  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
002161F2  49 8B E3                        mov rsp, r11
002161F5  41 5F                           pop r15
002161F7  41 5E                           pop r14
002161F9  41 5D                           pop r13
002161FB  41 5C                           pop r12
002161FD  5D                              pop rbp
002161FE  C3                              ret
002161FF  CC                              int3
00216200  41 B7 01                        mov r15b, 1
00216203  49 8B DE                        mov rbx, r14
00216206  4C 8D 25 93 6F D7 00            lea r12, [rip + 0xd76f93]
0021620D  BF 08 00 00 00                  mov edi, 8
00216212  4A 8D 0C 23                     lea rcx, [rbx + r12]
00216216  E8 25 9E 0D 00                  call 0x1402f0040
0021621B  48 89 44 1D B0                  mov qword ptr [rbp + rbx - 0x50], rax
00216220  48 85 C0                        test rax, rax
00216223  74 09                           je 0x14021622e
00216225  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00216229  48 89 44 1D F0                  mov qword ptr [rbp + rbx - 0x10], rax
0021622E  48 83 C3 08                     add rbx, 8
00216232  48 83 EF 01                     sub rdi, 1
00216236  75 DA                           jne 0x140216212
00216238  44 8D 67 08                     lea r12d, [rdi + 8]
0021623C  41 80 FF 01                     cmp r15b, 1
00216240  0F 85 EC 01 00 00               jne 0x140216432
00216246  41 0F B7 DE                     movzx ebx, r14w
0021624A  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
0021624F  49 8B FE                        mov rdi, r14
00216252  48 8B 74 3D B0                  mov rsi, qword ptr [rbp + rdi - 0x50]
00216257  48 85 F6                        test rsi, rsi
0021625A  0F 85 AE 00 00 00               jne 0x14021630e
00216260  48 83 C7 08                     add rdi, 8
00216264  66 FF C3                        inc bx
00216267  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0021626C  66 83 FB 08                     cmp bx, 8
00216270  72 E0                           jb 0x140216252
00216272  41 BC 08 00 00 00               mov r12d, 8
00216278  45 85 ED                        test r13d, r13d
0021627B  74 06                           je 0x140216283
0021627D  FF 05 6D 6F D7 00               inc dword ptr [rip + 0xd76f6d]
00216283  41 0F B7 FE                     movzx edi, r14w
00216287  45 85 ED                        test r13d, r13d
0021628A  74 38                           je 0x1402162c4
0021628C  45 33 C0                        xor r8d, r8d
0021628F  66 83 FF 02                     cmp di, 2
00216293  0F 83 55 01 00 00               jae 0x1402163ee
00216299  0F B7 C7                        movzx eax, di
0021629C  48 8D 0C 40                     lea rcx, [rax + rax*2]
002162A0  48 03 C9                        add rcx, rcx
002162A3  4C 8B 4C CC 50                  mov r9, qword ptr [rsp + rcx*8 + 0x50]
002162A8  48 8D 54 CC 58                  lea rdx, [rsp + rcx*8 + 0x58]
002162AD  49 8B C9                        mov rcx, r9
002162B0  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
002162B4  E8 17 48 4A 00                  call 0x1406baad0
002162B9  66 FF C7                        inc di
002162BC  0F B7 C7                        movzx eax, di
002162BF  41 3B C5                        cmp eax, r13d
002162C2  72 C8                           jb 0x14021628c
002162C4  48 8D 1D D5 6E D7 00            lea rbx, [rip + 0xd76ed5]
002162CB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
002162D0  4A 8B 54 35 B0                  mov rdx, qword ptr [rbp + r14 - 0x50]
002162D5  48 85 D2                        test rdx, rdx
002162D8  74 25                           je 0x1402162ff
002162DA  41 0F 0D 0C 1E                  prefetchw byte ptr [r14 + rbx]
002162DF  49 8B 04 1E                     mov rax, qword ptr [r14 + rbx]
002162E3  48 8B C8                        mov rcx, rax
002162E6  48 33 CA                        xor rcx, rdx
002162E9  48 83 F9 0F                     cmp rcx, 0xf
002162ED  0F 83 08 03 00 00               jae 0x1402165fb
002162F3  48 8D 48 01                     lea rcx, [rax + 1]
002162F7  F0 49 0F B1 0C 1E               lock cmpxchg qword ptr [r14 + rbx], rcx
002162FD  75 E4                           jne 0x1402162e3
002162FF  49 83 C6 08                     add r14, 8
00216303  49 83 EC 01                     sub r12, 1
00216307  75 C7                           jne 0x1402162d0
00216309  E9 C4 FE FF FF                  jmp 0x1402161d2
0021630E  B9 0A 00 00 00                  mov ecx, 0xa
00216313  E8 68 DA 05 00                  call 0x140273d80
00216318  48 8B 4C 3D F0                  mov rcx, qword ptr [rbp + rdi - 0x10]
0021631D  44 0F B6 E0                     movzx r12d, al
00216321  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00216325  48 8B 51 20                     mov rdx, qword ptr [rcx + 0x20]
00216329  4C 8B 7A 08                     mov r15, qword ptr [rdx + 8]
0021632D  4D 85 FF                        test r15, r15
00216330  74 71                           je 0x1402163a3
00216332  4C 8B 64 24 30                  mov r12, qword ptr [rsp + 0x30]
00216337  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
0021633B  41 F7 47 30 00 00 00 01         test dword ptr [r15 + 0x30], 0x1000000
00216343  74 4A                           je 0x14021638f
00216345  41 83 FD 02                     cmp r13d, 2
00216349  73 6B                           jae 0x1402163b6
0021634B  41 8B C5                        mov eax, r13d
0021634E  48 8D 0C 40                     lea rcx, [rax + rax*2]
00216352  48 03 C9                        add rcx, rcx
00216355  48 89 74 CC 50                  mov qword ptr [rsp + rcx*8 + 0x50], rsi
0021635A  66 89 5C CC 78                  mov word ptr [rsp + rcx*8 + 0x78], bx
0021635F  4C 89 7C CC 58                  mov qword ptr [rsp + rcx*8 + 0x58], r15
00216364  4C 89 64 CC 60                  mov qword ptr [rsp + rcx*8 + 0x60], r12
00216369  89 7C CC 68                     mov dword ptr [rsp + rcx*8 + 0x68], edi
0021636D  4C 89 74 CC 70                  mov qword ptr [rsp + rcx*8 + 0x70], r14
00216372  BA 44 66 6C 74                  mov edx, 0x746c6644
00216377  49 8B CF                        mov rcx, r15
0021637A  E8 91 A3 FF FF                  call 0x140210710
0021637F  BA 44 66 6C 74                  mov edx, 0x746c6644
00216384  49 8B CC                        mov rcx, r12
00216387  E8 84 A3 FF FF                  call 0x140210710
0021638C  41 FF C5                        inc r13d
0021638F  4D 8B 7F 10                     mov r15, qword ptr [r15 + 0x10]
00216393  4D 85 FF                        test r15, r15
00216396  75 A3                           jne 0x14021633b
00216398  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0021639D  44 0F B6 64 24 20               movzx r12d, byte ptr [rsp + 0x20]
002163A3  41 0F B6 D4                     movzx edx, r12b
002163A7  B9 0A 00 00 00                  mov ecx, 0xa
002163AC  E8 8F C1 05 00                  call 0x140272540
002163B1  E9 AA FE FF FF                  jmp 0x140216260
002163B6  BA 30 00 00 00                  mov edx, 0x30
002163BB  41 B8 49 6F 42 43               mov r8d, 0x43426f49
002163C1  8D 4A 10                        lea ecx, [rdx + 0x10]
002163C4  E8 27 BD 96 00                  call 0x140b820f0
002163C9  48 85 C0                        test rax, rax
002163CC  74 CA                           je 0x140216398
002163CE  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
002163D2  48 89 48 20                     mov qword ptr [rax + 0x20], rcx
002163D6  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
002163DA  48 89 30                        mov qword ptr [rax], rsi
002163DD  66 89 58 28                     mov word ptr [rax + 0x28], bx
002163E1  4C 89 78 08                     mov qword ptr [rax + 8], r15
002163E5  4C 89 60 10                     mov qword ptr [rax + 0x10], r12
002163E9  89 78 18                        mov dword ptr [rax + 0x18], edi
002163EC  EB 84                           jmp 0x140216372
002163EE  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
002163F2  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
002163F6  48 8D 53 08                     lea rdx, [rbx + 8]
002163FA  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
002163FE  48 8B 0B                        mov rcx, qword ptr [rbx]
00216401  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00216405  E8 C6 46 4A 00                  call 0x1406baad0
0021640A  33 D2                           xor edx, edx
0021640C  48 8B CB                        mov rcx, rbx
0021640F  E8 5C C4 96 00                  call 0x140b82870
00216414  E9 A0 FE FF FF                  jmp 0x1402162b9
00216419  41 B7 01                        mov r15b, 1
0021641C  40 0F B6 D7                     movzx edx, dil
00216420  49 8D 8C 24 18 06 00 00         lea rcx, [r12 + 0x618]
00216428  E8 73 C7 17 00                  call 0x140392ba0
0021642D  E9 D1 FD FF FF                  jmp 0x140216203
00216432  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00216437  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
0021643C  48 8D 98 18 06 00 00            lea rbx, [rax + 0x618]
00216443  4C 8D B8 40 05 00 00            lea r15, [rax + 0x540]
0021644A  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0021644F  48 8B CB                        mov rcx, rbx
00216452  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00216457  E8 14 20 FF FF                  call 0x140208470
0021645C  4D 8B 3F                        mov r15, qword ptr [r15]
0021645F  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00216463  4C 3B 7C 24 28                  cmp r15, qword ptr [rsp + 0x28]
00216468  0F 84 74 01 00 00               je 0x1402165e2
0021646E  4C 8B 64 24 28                  mov r12, qword ptr [rsp + 0x28]
00216473  49 0F BE 4F 22                  movsx rcx, byte ptr [r15 + 0x22]
00216478  41 38 4F 23                     cmp byte ptr [r15 + 0x23], cl
0021647C  0F 8F 44 01 00 00               jg 0x1402165c6
00216482  49 8B 97 98 00 00 00            mov rdx, qword ptr [r15 + 0x98]
00216489  48 8D 0C C9                     lea rcx, [rcx + rcx*8]
0021648D  48 8D 49 16                     lea rcx, [rcx + 0x16]
00216491  49 8D 0C CF                     lea rcx, [r15 + rcx*8]
00216495  48 3B D1                        cmp rdx, rcx
00216498  0F 83 28 01 00 00               jae 0x1402165c6
0021649E  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
002164A2  48 85 C0                        test rax, rax
002164A5  0F 84 1B 01 00 00               je 0x1402165c6
002164AB  48 8B 4A 28                     mov rcx, qword ptr [rdx + 0x28]
002164AF  41 0F B7 DE                     movzx ebx, r14w
002164B3  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
002164B8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
002164C0  66 83 FB 08                     cmp bx, 8
002164C4  0F 83 FC 00 00 00               jae 0x1402165c6
002164CA  0F B7 C3                        movzx eax, bx
002164CD  48 8D 3C C5 00 00 00 00         lea rdi, [rax*8]
002164D5  48 8B 74 3D B0                  mov rsi, qword ptr [rbp + rdi - 0x50]
002164DA  48 85 F6                        test rsi, rsi
002164DD  75 05                           jne 0x1402164e4
002164DF  66 FF C3                        inc bx
002164E2  EB DC                           jmp 0x1402164c0
002164E4  65 48 8B 0C 25 28 00 00 00      mov rcx, qword ptr gs:[0x28]
002164ED  48 81 C1 A0 00 00 00            add rcx, 0xa0
002164F4  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
002164F8  E8 23 D9 05 00                  call 0x140273e20
002164FD  48 8B 44 3D F0                  mov rax, qword ptr [rbp + rdi - 0x10]
00216502  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00216506  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
0021650A  48 85 D2                        test rdx, rdx
0021650D  74 0D                           je 0x14021651c
0021650F  48 3B 54 24 28                  cmp rdx, qword ptr [rsp + 0x28]
00216514  74 1D                           je 0x140216533
00216516  48 8B 52 10                     mov rdx, qword ptr [rdx + 0x10]
0021651A  EB EE                           jmp 0x14021650a
0021651C  65 48 8B 0C 25 28 00 00 00      mov rcx, qword ptr gs:[0x28]
00216525  48 81 C1 A0 00 00 00            add rcx, 0xa0
0021652C  E8 7F 0C 00 00                  call 0x1402171b0
00216531  EB AC                           jmp 0x1402164df
00216533  F7 42 30 00 00 00 01            test dword ptr [rdx + 0x30], 0x1000000
0021653A  74 DA                           je 0x140216516
0021653C  65 48 8B 0C 25 28 00 00 00      mov rcx, qword ptr gs:[0x28]
00216545  48 81 C1 A0 00 00 00            add rcx, 0xa0
0021654C  E8 5F 0C 00 00                  call 0x1402171b0
00216551  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
00216556  48 39 4C 24 38                  cmp qword ptr [rsp + 0x38], rcx
0021655B  74 82                           je 0x1402164df
0021655D  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00216562  41 83 FD 02                     cmp r13d, 2
00216566  0F 83 D4 01 4C 00               jae 0x1406d6740
0021656C  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
00216571  41 8B C5                        mov eax, r13d
00216574  48 8D 14 40                     lea rdx, [rax + rax*2]
00216578  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
0021657C  48 03 D2                        add rdx, rdx
0021657F  48 89 74 D4 50                  mov qword ptr [rsp + rdx*8 + 0x50], rsi
00216584  66 89 5C D4 78                  mov word ptr [rsp + rdx*8 + 0x78], bx
00216589  48 89 4C D4 58                  mov qword ptr [rsp + rdx*8 + 0x58], rcx
0021658E  4C 89 44 D4 60                  mov qword ptr [rsp + rdx*8 + 0x60], r8
00216593  89 44 D4 68                     mov dword ptr [rsp + rdx*8 + 0x68], eax
00216597  4C 89 74 D4 70                  mov qword ptr [rsp + rdx*8 + 0x70], r14
0021659C  BA 44 66 6C 74                  mov edx, 0x746c6644
002165A1  41 FF C5                        inc r13d
002165A4  E8 67 A1 FF FF                  call 0x140210710
002165A9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
002165AE  BA 44 66 6C 74                  mov edx, 0x746c6644
002165B3  E8 58 A1 FF FF                  call 0x140210710
002165B8  41 8B 47 F0                     mov eax, dword ptr [r15 - 0x10]
002165BC  A8 02                           test al, 2
002165BE  74 48                           je 0x140216608
002165C0  FF 05 BA 6B D7 00               inc dword ptr [rip + 0xd76bba]
002165C6  4D 8B 3F                        mov r15, qword ptr [r15]
002165C9  4D 3B FC                        cmp r15, r12
002165CC  0F 85 A1 FE FF FF               jne 0x140216473
002165D2  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
002165D7  41 BC 08 00 00 00               mov r12d, 8
002165DD  0F B6 44 24 20                  movzx eax, byte ptr [rsp + 0x20]
002165E2  0F B6 D0                        movzx edx, al
002165E5  48 8B CB                        mov rcx, rbx
002165E8  E8 B3 C5 17 00                  call 0x140392ba0
002165ED  45 85 ED                        test r13d, r13d
002165F0  0F 84 50 FC FF FF               je 0x140216246
002165F6  E9 88 FC FF FF                  jmp 0x140216283
002165FB  48 8B CA                        mov rcx, rdx
002165FE  E8 7D 38 13 00                  call 0x140349e80
00216603  E9 F7 FC FF FF                  jmp 0x1402162ff
00216608  FF 05 6E 6B D7 00               inc dword ptr [rip + 0xd76b6e]
0021660E  EB B6                           jmp 0x1402165c6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoBoostThreadIoPriority(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned __int8 v_stack_m120;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m144;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 12535301)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m144 = a2;
    a2 = 0;
    v_stack_m138 = a1;
    v_r15 = 0;
    result = memset(v_stack_mB8, a2, a2 + 64, a4);
    a2 = 0;
    result = memset(v_stack_m78, a2, a2 + 64, a4);
    v_r14 = 0;
    if (sign_flag) goto loc_00216200;
    result = KeAcquireSpinLockRaiseToDpc(a1 + 1560, a2, a2 + 64, a4);
    if ((*(unsigned __int64 *)(a1 + 1344)) != (a1 + 1344)) goto loc_0021641C;
    if ((*(unsigned __int64 *)(a1 + 1344)) < (a1 + 1344)) goto loc_00216419;
    result = KxReleaseSpinLock(a1 + 1560, a2, a2 + 64, a4);
    if ((*(unsigned int *)(v_rip + 14355297)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a2 + 64, a4);
    }
loc_002161D2:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a2 + 64, a4);
    return result;
loc_00216200:
loc_00216203:
loc_00216212:
    result = ExReferenceCallBackBlock(0 + v_rip + 14118803 * 1, a2, a2 + 64, a4);
    *(unsigned __int64 *)(v_stack_m68 + 0 * 1 - 80) = result;
    if (result != 0) {
        result = *(unsigned __int64 *)(result + 16);
        *(unsigned __int64 *)(v_stack_m68 + 0 * 1 - 16) = result;
    }
    v_rbx = (0) + (8);
    v_rdi = (8) - (1);
    if (condition_is_not_equal) goto loc_00216212;
    if (1 != 1) goto loc_00216432;
loc_00216246:
    v_stack_m108 = 0;
loc_00216252:
    if (*(unsigned __int64 *)(v_stack_m68 + 0 * 1 - 80) != 0) goto loc_0021630E;
loc_00216260:
    v_rdi = (0) + (8);
    v_rbx = (unsigned __int16)((0) + 1);
    v_stack_m108 = v_rdi;
    if (((unsigned __int16)(v_rbx)) < 8) goto loc_00216252;
    if (0 != 0) {
    }
    if (0 == 0) goto loc_002162C4;
loc_0021628C:
    a3 = 0;
    if (0 >= 2) goto loc_002163EE;
    a1 = (0 + 0 * 2) + (0 + 0 * 2);
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80), v_stack_m28 + a1 * 8 + 88, a3, *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
loc_002162B9:
    v_rdi = (unsigned __int16)((0) + 1);
    if (((unsigned int)((unsigned __int16)(v_rdi))) < 0) goto loc_0021628C;
loc_002162C4:
loc_002162D0:
    if (*(unsigned __int64 *)(v_stack_m68 + v_r14 * 1 - 80) == 0) goto loc_002162FF;
loc_002162E3:
    a1 = (*(unsigned __int64 *)(v_r14 + v_rip + 14118613 * 1)) ^ (*(unsigned __int64 *)(v_stack_m68 + v_r14 * 1 - 80));
    if (a1 >= 15) goto loc_002165FB;
    if (a1 != 15) goto loc_002162E3;
loc_002162FF:
    v_r14 = (v_r14) + (8);
    v_r12 = (8) - (1);
    if (condition_is_not_equal) goto loc_002162D0;
    goto loc_002161D2;
loc_0021630E:
    result = KeAcquireQueuedSpinLock(10, *(unsigned __int64 *)(v_stack_m68 + v_r14 * 1 - 80), a3, *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    v_stack_m120 = (unsigned __int8)(result);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + v_rdi * 1 - 16) + 32) + 8) == 0) goto loc_002163A3;
loc_0021633B:
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + v_rdi * 1 - 16) + 32) + 8) + 48)) & (0x1000000ULL)) == 0) goto loc_0021638F;
    if (0 >= 2) goto loc_002163B6;
    a1 = (0 + 0 * 2) + (0 + 0 * 2);
    *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80) = *(unsigned __int64 *)(v_stack_m68 + 0 * 1 - 80);
    *(unsigned __int16 *)(v_stack_m28 + a1 * 8 + 120) = (unsigned __int16)(v_rip + 14118613);
    *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 88) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + v_rdi * 1 - 16) + 32) + 8);
    *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 96) = v_stack_m110;
    *(unsigned int *)(v_stack_m28 + a1 * 8 + 104) = (unsigned int)((unsigned int)(v_stack_m11C));
    *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 112) = v_r14;
loc_00216372:
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + v_rdi * 1 - 16) + 32) + 8), (unsigned int)(0x746C6644ULL), a3, *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    result = ObfReferenceObjectWithTag(v_stack_m110, (unsigned int)(0x746C6644ULL), a3, *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    v_r13 = (unsigned int)((0) + 1);
loc_0021638F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + v_rdi * 1 - 16) + 32) + 8) + 16) != 0) goto loc_0021633B;
loc_00216398:
loc_002163A3:
    result = KeReleaseQueuedSpinLock(10, (unsigned __int8)(v_stack_m120), a3, *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    goto loc_00216260;
loc_002163B6:
    result = ExAllocatePool2(48 + 16, 48, (unsigned int)(0x43426F49ULL), *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    if (result == 0) goto loc_00216398;
    *(unsigned __int64 *)(result + 32) = v_stack_mC8;
    v_stack_mC8 = result;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(v_stack_m68 + 0 * 1 - 80);
    *(unsigned __int16 *)(result + 40) = (unsigned __int16)(v_rip + 14118613);
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + v_rdi * 1 - 16) + 32) + 8) + 16);
    *(unsigned __int64 *)(result + 16) = v_stack_m120;
    *(unsigned int *)(result + 24) = (unsigned int)(v_stack_m108);
    goto loc_00216372;
loc_002163EE:
    v_stack_mC8 = *(unsigned __int64 *)(v_stack_mC8 + 32);
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_stack_mC8), v_stack_mC8 + 8, (unsigned int)(0x43426F49ULL), *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mC8, a2, (unsigned int)(0x43426F49ULL), *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    goto loc_002162B9;
loc_00216419:
loc_0021641C:
    result = KeReleaseSpinLock(v_stack_m120 + 1560, (unsigned __int8)(v_stack_m108), (unsigned int)(0x43426F49ULL), *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    goto loc_00216203;
loc_00216432:
    v_stack_m108 = v_r14;
    v_stack_m100 = v_stack_m110 + 1560;
    v_stack_m118 = v_stack_m110 + 1344;
    result = KeAcquireSpinLockRaiseToDpc(v_stack_m110 + 1560, (unsigned __int8)(v_stack_m108), (unsigned int)(0x43426F49ULL), *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    v_stack_m120 = (unsigned __int8)(result);
    if ((*(unsigned __int64 *)(v_stack_m110 + 1344)) == v_stack_m118) goto loc_002165E2;
loc_00216473:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m110 + 1344) + 35)) > ((unsigned __int8)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m110 + 1344) + 34))))) goto loc_002165C6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110 + 1344) + 152)) >= (*(unsigned __int64 *)(v_stack_m110 + 1344) + (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m110 + 1344) + 34)) + (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m110 + 1344) + 34)) * 8 + 22 * 8)) goto loc_002165C6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110 + 1344) + 152) + 40) == 0) goto loc_002165C6;
    v_stack_m118 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110 + 1344) + 152) + 40);
loc_002164C0:
    if (((unsigned __int16)((unsigned __int16)(v_r14))) >= 8) goto loc_002165C6;
    if (*(unsigned __int64 *)(v_stack_m68 + (unsigned __int16)((unsigned __int16)(v_r14)) * 8 * 1 - 80) != 0) goto loc_002164E4;
loc_002164DF:
    v_rbx = (unsigned __int16)(((unsigned __int16)(v_r14)) + 1);
    goto loc_002164C0;
loc_002164E4:
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 40))) + (160);
    result = KxAcquireQueuedSpinLock(a1, *(unsigned __int64 *)(a1 + 8), (unsigned int)(0x43426F49ULL), *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
loc_0021650A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + (unsigned __int16)((unsigned __int16)(v_r14)) * 8 * 1 - 16) + 32) + 8) == 0) goto loc_0021651C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + (unsigned __int16)((unsigned __int16)(v_r14)) * 8 * 1 - 16) + 32) + 8)) == v_stack_m118) goto loc_00216533;
loc_00216516:
    goto loc_0021650A;
loc_0021651C:
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 40))) + (160);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + (unsigned __int16)((unsigned __int16)(v_r14)) * 8 * 1 - 16) + 32) + 8) + 16), (unsigned int)(0x43426F49ULL), *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    goto loc_002164DF;
loc_00216533:
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + (unsigned __int16)((unsigned __int16)(v_r14)) * 8 * 1 - 16) + 32) + 8) + 16) + 48)) & (0x1000000ULL)) == 0) goto loc_00216516;
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 40))) + (160);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + (unsigned __int16)((unsigned __int16)(v_r14)) * 8 * 1 - 16) + 32) + 8) + 16), (unsigned int)(0x43426F49ULL), *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    if (v_stack_m108 == v_stack_m118) goto loc_002164DF;
    v_stack_m108 = v_stack_m118;
    a2 = ((unsigned int)((unsigned int)(v_r13)) + (unsigned int)((unsigned int)(v_r13)) * 2) + ((unsigned int)((unsigned int)(v_r13)) + (unsigned int)((unsigned int)(v_r13)) * 2);
    *(unsigned __int64 *)(v_stack_m28 + a2 * 8 + 80) = *(unsigned __int64 *)(v_stack_m68 + (unsigned __int16)((unsigned __int16)(v_r14)) * 8 * 1 - 80);
    *(unsigned __int16 *)(v_stack_m28 + a2 * 8 + 120) = (unsigned __int16)(v_rbx);
    *(unsigned __int64 *)(v_stack_m28 + a2 * 8 + 88) = v_stack_m118;
    *(unsigned __int64 *)(v_stack_m28 + a2 * 8 + 96) = v_stack_m110;
    *(unsigned int *)(v_stack_m28 + a2 * 8 + 104) = (unsigned int)((unsigned int)(v_stack_m11C));
    *(unsigned __int64 *)(v_stack_m28 + a2 * 8 + 112) = v_r14;
    v_r13 = (unsigned int)((v_r13) + 1);
    result = ObfReferenceObjectWithTag(v_stack_m118, (unsigned int)(0x746C6644ULL), v_stack_m110, *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    result = ObfReferenceObjectWithTag(v_stack_m110, (unsigned int)(0x746C6644ULL), v_stack_m110, *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m110 + 1344) - 16)))) & (2)) == 0) goto loc_00216608;
loc_002165C6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110 + 1344))) != v_stack_m118) goto loc_00216473;
loc_002165E2:
    result = KeReleaseSpinLock(v_stack_m100, (unsigned __int8)(v_stack_m120), v_stack_m110, *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    if ((unsigned int)(v_r13) == 0) goto loc_00216246;
    goto loc_00216283;
loc_002165FB:
    result = ExReleaseRundownProtection((unsigned __int8)(v_stack_m120), (unsigned __int8)(v_stack_m120), v_stack_m110, *(unsigned __int64 *)(v_stack_m28 + a1 * 8 + 80));
    goto loc_002162FF;
loc_00216608:
    goto loc_002165C6;
}
```

## 5. (Beta) C Style

```c
int64_t IoBoostThreadIoPriority(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint8_t v_stack_m120;
    uint64_t v_stack_m138;
    uint32_t v_stack_m144;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0xBF4605)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m144 = Arg2;
    Arg2 = 0;
    v_stack_m138 = Arg1;
    local_r15 = 0;
    result = memset(v_stack_mB8, Arg2, Arg2 + 64, a4);
    Arg2 = 0;
    result = memset(v_stack_m78, Arg2, Arg2 + 64, a4);
    local_r14 = 0;
    if (sign_flag) goto loc_00216200;
    result = KeAcquireSpinLockRaiseToDpc(Arg1 + 1560, Arg2, Arg2 + 64, a4);
    if ((*(uint64_t *)(arg1 + 0x540)) != (Arg1 + 1344)) goto loc_0021641C;
    if ((*(uint64_t *)(arg1 + 0x540)) < (Arg1 + 1344)) goto loc_00216419;
    result = KxReleaseSpinLock(Arg1 + 1560, Arg2, Arg2 + 64, a4);
    if ((*(uint32_t *)(v_rip + 0xDB0B61)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg2 + 64, a4);
    }
loc_002161D2:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg2 + 64, a4);
    return result;
loc_00216200:
loc_00216203:
loc_00216212:
    result = ExReferenceCallBackBlock(0 + v_rip + 14118803 * 1, Arg2, Arg2 + 64, a4);
    *(uint64_t *)(v_stack_m68 + 0x0 * 1 - 0x50) = result;
    if (result != 0) {
        result = *(uint64_t *)(result + 0x10);
        *(uint64_t *)(v_stack_m68 + 0x0 * 1 - 0x10) = result;
    }
    local_rbx = (0) + (8);
    local_rdi = (8) - (1);
    if (condition_is_not_equal) goto loc_00216212;
    if (1 != 1) goto loc_00216432;
loc_00216246:
    v_stack_m108 = 0;
loc_00216252:
    if (*(uint64_t *)(v_stack_m68 + 0x0 * 1 - 0x50) != 0) goto loc_0021630E;
loc_00216260:
    local_rdi = (0) + (8);
    local_rbx = (uint16_t)((0) + 1);
    v_stack_m108 = local_rdi;
    if (((uint16_t)(local_rbx)) < 8) goto loc_00216252;
    if (0 != 0) {
    }
    if (0 == 0) goto loc_002162C4;
loc_0021628C:
    Arg3 = 0;
    if (0 >= 2) goto loc_002163EE;
    Arg1 = (0 + 0 * 2) + (0 + 0 * 2);
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50), v_stack_m28 + Arg1 * 8 + 88, Arg3, *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
loc_002162B9:
    local_rdi = (uint16_t)((0) + 1);
    if (((uint32_t)((uint16_t)(local_rdi))) < 0) goto loc_0021628C;
loc_002162C4:
loc_002162D0:
    if (*(uint64_t *)(v_stack_m68 + local_r14 * 1 - 0x50) == 0) goto loc_002162FF;
loc_002162E3:
    Arg1 = (*(uint64_t *)(local_r14 + v_rip + 0xD76ED5 * 1)) ^ (*(uint64_t *)(v_stack_m68 + local_r14 * 1 - 0x50));
    if (Arg1 >= 15) goto loc_002165FB;
    if (Arg1 != 15) goto loc_002162E3;
loc_002162FF:
    local_r14 = (local_r14) + (8);
    local_r12 = (8) - (1);
    if (condition_is_not_equal) goto loc_002162D0;
    goto loc_002161D2;
loc_0021630E:
    result = KeAcquireQueuedSpinLock(10, *(uint64_t *)(v_stack_m68 + local_r14 * 1 - 0x50), Arg3, *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    v_stack_m120 = (uint8_t)(result);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68 + local_rdi * 1 - 0x10) + 0x20) + 0x8) == 0) goto loc_002163A3;
loc_0021633B:
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68 + local_rdi * 1 - 0x10) + 0x20) + 0x8) + 0x30)) & (0x1000000ULL)) == 0) goto loc_0021638F;
    if (0 >= 2) goto loc_002163B6;
    Arg1 = (0 + 0 * 2) + (0 + 0 * 2);
    *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50) = *(uint64_t *)(v_stack_m68 + 0x0 * 1 - 0x50);
    *(uint16_t *)(v_stack_m28 + arg1 * 8 + 0x78) = (uint16_t)(v_rip + 14118613);
    *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x58) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68 + local_rdi * 1 - 0x10) + 0x20) + 0x8);
    *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x60) = v_stack_m110;
    *(uint32_t *)(v_stack_m28 + arg1 * 8 + 0x68) = (uint32_t)((uint32_t)(v_stack_m11C));
    *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x70) = local_r14;
loc_00216372:
    result = ObfReferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68 + local_rdi * 1 - 0x10) + 0x20) + 0x8), (uint32_t)(0x746C6644ULL), Arg3, *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    result = ObfReferenceObjectWithTag(v_stack_m110, (uint32_t)(0x746C6644ULL), Arg3, *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    local_r13 = (uint32_t)((0) + 1);
loc_0021638F:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68 + local_rdi * 1 - 0x10) + 0x20) + 0x8) + 0x10) != 0) goto loc_0021633B;
loc_00216398:
loc_002163A3:
    result = KeReleaseQueuedSpinLock(10, (uint8_t)(v_stack_m120), Arg3, *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    goto loc_00216260;
loc_002163B6:
    result = ExAllocatePool2(48 + 16, 48, (uint32_t)(0x43426F49ULL), *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    if (result == 0) goto loc_00216398;
    *(uint64_t *)(result + 0x20) = v_stack_mC8;
    v_stack_mC8 = result;
    *(uint64_t *)(result) = *(uint64_t *)(v_stack_m68 + 0x0 * 1 - 0x50);
    *(uint16_t *)(result + 0x28) = (uint16_t)(v_rip + 14118613);
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68 + local_rdi * 1 - 0x10) + 0x20) + 0x8) + 0x10);
    *(uint64_t *)(result + 0x10) = v_stack_m120;
    *(uint32_t *)(result + 0x18) = (uint32_t)(v_stack_m108);
    goto loc_00216372;
loc_002163EE:
    v_stack_mC8 = *(uint64_t *)(v_stack_mC8 + 0x20);
    result = guard_dispatch_icall(*(uint64_t *)(v_stack_mC8), v_stack_mC8 + 8, (uint32_t)(0x43426F49ULL), *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mC8, Arg2, (uint32_t)(0x43426F49ULL), *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    goto loc_002162B9;
loc_00216419:
loc_0021641C:
    result = KeReleaseSpinLock(v_stack_m120 + 1560, (uint8_t)(v_stack_m108), (uint32_t)(0x43426F49ULL), *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    goto loc_00216203;
loc_00216432:
    v_stack_m108 = local_r14;
    v_stack_m100 = v_stack_m110 + 1560;
    v_stack_m118 = v_stack_m110 + 1344;
    result = KeAcquireSpinLockRaiseToDpc(v_stack_m110 + 1560, (uint8_t)(v_stack_m108), (uint32_t)(0x43426F49ULL), *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    v_stack_m120 = (uint8_t)(result);
    if ((*(uint64_t *)(v_stack_m110 + 0x540)) == v_stack_m118) goto loc_002165E2;
loc_00216473:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m110 + 0x540) + 0x23)) > ((uint8_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m110 + 0x540) + 0x22))))) goto loc_002165C6;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m110 + 0x540) + 0x98)) >= (*(uint64_t *)(v_stack_m110 + 0x540) + (int8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m110 + 0x540) + 0x22)) + (int8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m110 + 0x540) + 0x22)) * 8 + 22 * 8)) goto loc_002165C6;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m110 + 0x540) + 0x98) + 0x28) == 0) goto loc_002165C6;
    v_stack_m118 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m110 + 0x540) + 0x98) + 0x28);
loc_002164C0:
    if (((uint16_t)((uint16_t)(local_r14))) >= 8) goto loc_002165C6;
    if (*(uint64_t *)(v_stack_m68 + (uint16_t)((uint16_t)(local_r14)) * 8 * 1 - 0x50) != 0) goto loc_002164E4;
loc_002164DF:
    local_rbx = (uint16_t)(((uint16_t)(local_r14)) + 1);
    goto loc_002164C0;
loc_002164E4:
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x28))) + (160);
    result = KxAcquireQueuedSpinLock(Arg1, *(uint64_t *)(arg1 + 0x8), (uint32_t)(0x43426F49ULL), *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
loc_0021650A:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68 + (uint16_t)((uint16_t)(local_r14)) * 8 * 1 - 0x10) + 0x20) + 0x8) == 0) goto loc_0021651C;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68 + (uint16_t)((uint16_t)(local_r14)) * 8 * 1 - 0x10) + 0x20) + 0x8)) == v_stack_m118) goto loc_00216533;
loc_00216516:
    goto loc_0021650A;
loc_0021651C:
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x28))) + (160);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68 + (uint16_t)((uint16_t)(local_r14)) * 8 * 1 - 0x10) + 0x20) + 0x8) + 0x10), (uint32_t)(0x43426F49ULL), *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    goto loc_002164DF;
loc_00216533:
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68 + (uint16_t)((uint16_t)(local_r14)) * 8 * 1 - 0x10) + 0x20) + 0x8) + 0x10) + 0x30)) & (0x1000000ULL)) == 0) goto loc_00216516;
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x28))) + (160);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68 + (uint16_t)((uint16_t)(local_r14)) * 8 * 1 - 0x10) + 0x20) + 0x8) + 0x10), (uint32_t)(0x43426F49ULL), *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    if (v_stack_m108 == v_stack_m118) goto loc_002164DF;
    v_stack_m108 = v_stack_m118;
    Arg2 = ((uint32_t)((uint32_t)(local_r13)) + (uint32_t)((uint32_t)(local_r13)) * 2) + ((uint32_t)((uint32_t)(local_r13)) + (uint32_t)((uint32_t)(local_r13)) * 2);
    *(uint64_t *)(v_stack_m28 + Arg2 * 8 + 0x50) = *(uint64_t *)(v_stack_m68 + (uint16_t)((uint16_t)(local_r14)) * 8 * 1 - 0x50);
    *(uint16_t *)(v_stack_m28 + Arg2 * 8 + 0x78) = (uint16_t)(local_rbx);
    *(uint64_t *)(v_stack_m28 + Arg2 * 8 + 0x58) = v_stack_m118;
    *(uint64_t *)(v_stack_m28 + Arg2 * 8 + 0x60) = v_stack_m110;
    *(uint32_t *)(v_stack_m28 + Arg2 * 8 + 0x68) = (uint32_t)((uint32_t)(v_stack_m11C));
    *(uint64_t *)(v_stack_m28 + Arg2 * 8 + 0x70) = local_r14;
    local_r13 = (uint32_t)((local_r13) + 1);
    result = ObfReferenceObjectWithTag(v_stack_m118, (uint32_t)(0x746C6644ULL), v_stack_m110, *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    result = ObfReferenceObjectWithTag(v_stack_m110, (uint32_t)(0x746C6644ULL), v_stack_m110, *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m110 + 0x540) - 0x10)))) & (2)) == 0) goto loc_00216608;
loc_002165C6:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m110 + 0x540))) != v_stack_m118) goto loc_00216473;
loc_002165E2:
    result = KeReleaseSpinLock(v_stack_m100, (uint8_t)(v_stack_m120), v_stack_m110, *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    if ((uint32_t)(local_r13) == 0) goto loc_00216246;
    goto loc_00216283;
loc_002165FB:
    result = ExReleaseRundownProtection((uint8_t)(v_stack_m120), (uint8_t)(v_stack_m120), v_stack_m110, *(uint64_t *)(v_stack_m28 + arg1 * 8 + 0x50));
    goto loc_002162FF;
loc_00216608:
    goto loc_002165C6;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x540` | `64` | `R` |
| `Arg1` | `+ 0x618` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00216110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
