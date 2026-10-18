# MiMarkHugePfnBad

- RVA: `0x00676744`–`0x00676BAA` (길이 `1,126` bytes)
- VA: `0x0000000140676744`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE498`
- 디코드: `291`개 명령, `1,126/1,126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00676785` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x006767AC` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x006767D8` → [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x006767F4` → [MiHugePfnPartition](../43/MiHugePfnPartition_function_004371B4.md) (function, `0x004371B4`)
- `0x00676810` → [MiLockDynamicMemoryShared](../3B/MiLockDynamicMemoryShared_function_003B8AA8.md) (function, `0x003B8AA8`)
- `0x00676818` → [MiHugePfnPartition](../43/MiHugePfnPartition_function_004371B4.md) (function, `0x004371B4`)
- `0x00676828` → [MiUnlockDynamicMemoryShared](../3B/MiUnlockDynamicMemoryShared_function_003B8A48.md) (function, `0x003B8A48`)
- `0x0067685D` → [MiLockHugePfn](MiLockHugePfn_function_006765FC.md) (function, `0x006765FC`)
- `0x00676873` → [MiIsPageInHugePfn](../2A/MiIsPageInHugePfn_function_002AB770.md) (function, `0x002AB770`)
- `0x00676895` → [MiUnlockHugePfn](../4D/MiUnlockHugePfn_function_004D90E4.md) (function, `0x004D90E4`)
- `0x006768AC` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x006768C6` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x006768E5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0067690F` → [MiLockHugeRangeColorHeadAtDpc](../4F/MiLockHugeRangeColorHeadAtDpc_function_004FAD14.md) (function, `0x004FAD14`)
- `0x00676927` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x00676971` → [RtlAvlInsertNodeEx](../26/RtlAvlInsertNodeEx_function_00265790.md) (function, `0x00265790`)
- `0x0067698E` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x00676A24` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x00676A5C` → [MiHugePfnPartition](../43/MiHugePfnPartition_function_004371B4.md) (function, `0x004371B4`)
- `0x00676A67` → [MiLockHugeRangeColorHeadAtDpc](../4F/MiLockHugeRangeColorHeadAtDpc_function_004FAD14.md) (function, `0x004FAD14`)
- `0x00676A75` → [MiUnlinkHugeRange](../43/MiUnlinkHugeRange_function_00436EF0.md) (function, `0x00436EF0`)
- `0x00676A8A` → [MiInsertHugeRangeInList](../43/MiInsertHugeRangeInList_function_004371E8.md) (function, `0x004371E8`)
- `0x00676A99` → [MiUnlockHugePfn](../4D/MiUnlockHugePfn_function_004D90E4.md) (function, `0x004D90E4`)
- `0x00676AA9` → [MiUnlockHugePfn](../4D/MiUnlockHugePfn_function_004D90E4.md) (function, `0x004D90E4`)
- `0x00676ACC` → [MiUnlockDynamicMemoryShared](../3B/MiUnlockDynamicMemoryShared_function_003B8A48.md) (function, `0x003B8A48`)
- `0x00676AE8` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00676AF4` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00676B11` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00676B21` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00676B2B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00676B40` → [KeDelayExecutionThread](../20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x00676B60` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00676B6C` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00676B8E` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)

### Direct callers
- [MmMarkPhysicalMemoryAsBad](MmMarkPhysicalMemoryAsBad_function_0067AA50.md) at `0x0067AB3B`

### Static image references
- `0x0067679A` → RVA `0x00E30048` (`.data`; read)
- `0x006767E6` → RVA `0x00E300C0` (`.data`; read)
- `0x00676920` → RVA `0x00E2FFD0` (`.data`; read)
- `0x0067692C` → RVA `0x00E30020` (`.data`; read)
- `0x006769E0` → RVA `0x00E30028` (`.data`; read/write)
- `0x00676B35` → RVA `0x000134D0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x006768E5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00676B21` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00676B2B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00676744  48 8B C4                        mov rax, rsp
00676747  89 50 10                        mov dword ptr [rax + 0x10], edx
0067674A  48 89 48 08                     mov qword ptr [rax + 8], rcx
0067674E  53                              push rbx
0067674F  55                              push rbp
00676750  56                              push rsi
00676751  57                              push rdi
00676752  41 54                           push r12
00676754  41 55                           push r13
00676756  41 56                           push r14
00676758  41 57                           push r15
0067675A  48 83 EC 58                     sub rsp, 0x58
0067675E  45 33 ED                        xor r13d, r13d
00676761  48 8B F9                        mov rdi, rcx
00676764  0F 57 C0                        xorps xmm0, xmm0
00676767  48 C1 EF 12                     shr rdi, 0x12
0067676B  0F 57 C9                        xorps xmm1, xmm1
0067676E  81 E7 FF FF 3F 00               and edi, 0x3fffff
00676774  0F 11 40 90                     movups xmmword ptr [rax - 0x70], xmm0
00676778  41 8B ED                        mov ebp, r13d
0067677B  45 8B FD                        mov r15d, r13d
0067677E  0F 11 48 A0                     movups xmmword ptr [rax - 0x60], xmm1
00676782  41 8B F5                        mov esi, r13d
00676785  E8 46 25 CC FF                  call 0x140338cd0
0067678A  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
00676793  45 8D 65 01                     lea r12d, [r13 + 1]
00676797  45 33 C0                        xor r8d, r8d
0067679A  48 8D 0D A7 98 7B 00            lea rcx, [rip + 0x7b98a7]
006767A1  33 D2                           xor edx, edx
006767A3  66 45 29 A6 E6 01 00 00         sub word ptr [r14 + 0x1e6], r12w
006767AB  90                              nop
006767AC  E8 7F 9A B9 FF                  call 0x140210230
006767B1  48 8B D8                        mov rbx, rax
006767B4  41 8D 55 11                     lea edx, [r13 + 0x11]
006767B8  33 C0                           xor eax, eax
006767BA  F0 48 0F B1 15 85 98 7B 00      lock cmpxchg qword ptr [rip + 0x7b9885], rdx
006767C3  74 18                           je 0x1406767dd
006767C5  4C 8D 0D 7C 98 7B 00            lea r9, [rip + 0x7b987c]
006767CC  4C 8B C3                        mov r8, rbx
006767CF  33 D2                           xor edx, edx
006767D1  48 8D 0D 70 98 7B 00            lea rcx, [rip + 0x7b9870]
006767D8  E8 6F 9C B9 FF                  call 0x14021044c
006767DD  48 85 DB                        test rbx, rbx
006767E0  74 04                           je 0x1406767e6
006767E2  44 88 63 0A                     mov byte ptr [rbx + 0xa], r12b
006767E6  48 8B 05 D3 98 7B 00            mov rax, qword ptr [rip + 0x7b98d3]
006767ED  48 8D 1C F8                     lea rbx, [rax + rdi*8]
006767F1  48 8B CB                        mov rcx, rbx
006767F4  E8 BB 09 DC FF                  call 0x1404371b4
006767F9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006767FE  4C 8B E0                        mov r12, rax
00676801  48 85 C0                        test rax, rax
00676804  0F 84 3F 03 00 00               je 0x140676b49
0067680A  49 8B D6                        mov rdx, r14
0067680D  48 8B C8                        mov rcx, rax
00676810  E8 93 22 D4 FF                  call 0x1403b8aa8
00676815  48 8B CB                        mov rcx, rbx
00676818  E8 97 09 DC FF                  call 0x1404371b4
0067681D  4C 3B E0                        cmp r12, rax
00676820  74 0D                           je 0x14067682f
00676822  49 8B D6                        mov rdx, r14
00676825  49 8B CC                        mov rcx, r12
00676828  E8 1B 22 D4 FF                  call 0x1403b8a48
0067682D  EB C2                           jmp 0x1406767f1
0067682F  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
00676834  BB 01 00 00 00                  mov ebx, 1
00676839  41 BC 34 04 00 C0               mov r12d, 0xc0000434
0067683F  84 C3                           test bl, al
00676841  0F 85 7A 02 00 00               jne 0x140676ac1
00676847  4C 89 AC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r13
0067684F  48 8B 05 6A 98 7B 00            mov rax, qword ptr [rip + 0x7b986a]
00676856  4C 8D 2C F8                     lea r13, [rax + rdi*8]
0067685A  49 8B CD                        mov rcx, r13
0067685D  E8 9A FD FF FF                  call 0x1406765fc
00676862  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0067686A  8A D0                           mov dl, al
0067686C  88 84 24 B0 00 00 00            mov byte ptr [rsp + 0xb0], al
00676873  E8 F8 4E C3 FF                  call 0x1402ab770
00676878  85 C0                           test eax, eax
0067687A  0F 84 26 02 00 00               je 0x140676aa6
00676880  49 8B 5D 00                     mov rbx, qword ptr [r13]
00676884  F6 C3 08                        test bl, 8
00676887  0F 85 F3 00 00 00               jne 0x140676980
0067688D  48 85 F6                        test rsi, rsi
00676890  75 67                           jne 0x1406768f9
00676892  49 8B CD                        mov rcx, r13
00676895  E8 4A 28 E6 FF                  call 0x1404d90e4
0067689A  BE 4D 69 48 70                  mov esi, 0x7048694d
0067689F  BA 00 00 01 00                  mov edx, 0x10000
006768A4  44 8B C6                        mov r8d, esi
006768A7  B9 40 00 00 00                  mov ecx, 0x40
006768AC  E8 8F 4C CE FF                  call 0x14035b540
006768B1  45 33 ED                        xor r13d, r13d
006768B4  48 8B D8                        mov rbx, rax
006768B7  48 85 C0                        test rax, rax
006768BA  74 2E                           je 0x1406768ea
006768BC  41 8D 55 28                     lea edx, [r13 + 0x28]
006768C0  44 8B C6                        mov r8d, esi
006768C3  8D 4A 18                        lea ecx, [rdx + 0x18]
006768C6  E8 75 4C CE FF                  call 0x14035b540
006768CB  48 8B F0                        mov rsi, rax
006768CE  48 85 C0                        test rax, rax
006768D1  74 0D                           je 0x1406768e0
006768D3  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
006768D7  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
006768DB  E9 6F FF FF FF                  jmp 0x14067684f
006768E0  33 D2                           xor edx, edx
006768E2  48 8B CB                        mov rcx, rbx
006768E5  E8 86 BF 50 00                  call 0x140b82870
006768EA  BD 9A 00 00 C0                  mov ebp, 0xc000009a
006768EF  BB 01 00 00 00                  mov ebx, 1
006768F4  E9 CB 01 00 00                  jmp 0x140676ac4
006768F9  48 8B C3                        mov rax, rbx
006768FC  B9 01 00 00 00                  mov ecx, 1
00676901  83 E0 07                        and eax, 7
00676904  48 2B C1                        sub rax, rcx
00676907  48 3B C1                        cmp rax, rcx
0067690A  77 14                           ja 0x140676920
0067690C  49 8B CD                        mov rcx, r13
0067690F  E8 00 44 E8 FF                  call 0x1404fad14
00676914  49 8B 5D 00                     mov rbx, qword ptr [r13]
00676918  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00676920  48 8D 0D A9 96 7B 00            lea rcx, [rip + 0x7b96a9]
00676927  E8 54 25 BD FF                  call 0x140248e80
0067692C  48 8B 15 ED 96 7B 00            mov rdx, qword ptr [rip + 0x7b96ed]
00676933  45 32 C0                        xor r8b, r8b
00676936  48 85 D2                        test rdx, rdx
00676939  74 2C                           je 0x140676967
0067693B  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
0067693F  25 FF FF 3F 00                  and eax, 0x3fffff
00676944  48 3B F8                        cmp rdi, rax
00676947  73 0A                           jae 0x140676953
00676949  48 8B 02                        mov rax, qword ptr [rdx]
0067694C  48 85 C0                        test rax, rax
0067694F  74 16                           je 0x140676967
00676951  EB 09                           jmp 0x14067695c
00676953  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00676957  48 85 C0                        test rax, rax
0067695A  74 05                           je 0x140676961
0067695C  48 8B D0                        mov rdx, rax
0067695F  EB DA                           jmp 0x14067693b
00676961  41 B8 01 00 00 00               mov r8d, 1
00676967  4C 8B CE                        mov r9, rsi
0067696A  48 8D 0D AF 96 7B 00            lea rcx, [rip + 0x7b96af]
00676971  E8 1A EE BE FF                  call 0x140265790
00676976  48 83 CB 08                     or rbx, 8
0067697A  49 89 5D 00                     mov qword ptr [r13], rbx
0067697E  EB 3A                           jmp 0x1406769ba
00676980  48 85 F6                        test rsi, rsi
00676983  48 8D 0D 46 96 7B 00            lea rcx, [rip + 0x7b9646]
0067698A  4C 0F 45 FE                     cmovne r15, rsi
0067698E  E8 ED 24 BD FF                  call 0x140248e80
00676993  48 8B 35 86 96 7B 00            mov rsi, qword ptr [rip + 0x7b9686]
0067699A  EB 19                           jmp 0x1406769b5
0067699C  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
006769A0  25 FF FF 3F 00                  and eax, 0x3fffff
006769A5  48 3B F8                        cmp rdi, rax
006769A8  76 06                           jbe 0x1406769b0
006769AA  48 8B 76 08                     mov rsi, qword ptr [rsi + 8]
006769AE  EB 05                           jmp 0x1406769b5
006769B0  73 08                           jae 0x1406769ba
006769B2  48 8B 36                        mov rsi, qword ptr [rsi]
006769B5  48 85 F6                        test rsi, rsi
006769B8  75 E2                           jne 0x14067699c
006769BA  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
006769C2  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
006769C6  81 E2 FF FF 03 00               and edx, 0x3ffff
006769CC  48 0F A3 11                     bt qword ptr [rcx], rdx
006769D0  0F 92 C0                        setb al
006769D3  84 C0                           test al, al
006769D5  75 10                           jne 0x1406769e7
006769D7  48 0F AB 11                     bts qword ptr [rcx], rdx
006769DB  B8 01 00 00 00                  mov eax, 1
006769E0  48 01 05 41 96 7B 00            add qword ptr [rip + 0x7b9641], rax
006769E7  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
006769EB  48 0F A3 90 00 80 00 00         bt qword ptr [rax + 0x8000], rdx
006769F3  0F 92 C1                        setb cl
006769F6  F7 84 24 A8 00 00 00 00 00 00 10  test dword ptr [rsp + 0xa8], 0x10000000
00676A01  74 0E                           je 0x140676a11
00676A03  84 C9                           test cl, cl
00676A05  75 16                           jne 0x140676a1d
00676A07  48 0F AB 90 00 80 00 00         bts qword ptr [rax + 0x8000], rdx
00676A0F  EB 0C                           jmp 0x140676a1d
00676A11  84 C9                           test cl, cl
00676A13  74 08                           je 0x140676a1d
00676A15  48 0F B3 90 00 80 00 00         btr qword ptr [rax + 0x8000], rdx
00676A1D  48 8D 0D AC 95 7B 00            lea rcx, [rip + 0x7b95ac]
00676A24  E8 B7 2D BD FF                  call 0x1402497e0
00676A29  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00676A31  48 85 C0                        test rax, rax
00676A34  74 05                           je 0x140676a3b
00676A36  F0 48 83 20 F7                  lock and qword ptr [rax], 0xfffffffffffffff7
00676A3B  83 E3 07                        and ebx, 7
00676A3E  B9 01 00 00 00                  mov ecx, 1
00676A43  48 8D 43 FF                     lea rax, [rbx - 1]
00676A47  48 3B C1                        cmp rax, rcx
00676A4A  76 0D                           jbe 0x140676a59
00676A4C  48 83 FB 04                     cmp rbx, 4
00676A50  74 3D                           je 0x140676a8f
00676A52  BD 03 01 00 00                  mov ebp, 0x103
00676A57  EB 36                           jmp 0x140676a8f
00676A59  49 8B CD                        mov rcx, r13
00676A5C  E8 53 07 DC FF                  call 0x1404371b4
00676A61  49 8B CD                        mov rcx, r13
00676A64  48 8B D8                        mov rbx, rax
00676A67  E8 A8 42 E8 FF                  call 0x1404fad14
00676A6C  48 8B D7                        mov rdx, rdi
00676A6F  48 8B CB                        mov rcx, rbx
00676A72  48 8B F0                        mov rsi, rax
00676A75  E8 76 04 DC FF                  call 0x140436ef0
00676A7A  F0 48 83 26 F7                  lock and qword ptr [rsi], 0xfffffffffffffff7
00676A7F  41 B8 04 00 00 00               mov r8d, 4
00676A85  48 8B D7                        mov rdx, rdi
00676A88  33 C9                           xor ecx, ecx
00676A8A  E8 59 07 DC FF                  call 0x1404371e8
00676A8F  8A 94 24 B0 00 00 00            mov dl, byte ptr [rsp + 0xb0]
00676A96  49 8B CD                        mov rcx, r13
00676A99  E8 46 26 E6 FF                  call 0x1404d90e4
00676A9E  45 33 ED                        xor r13d, r13d
00676AA1  E9 49 FE FF FF                  jmp 0x1406768ef
00676AA6  49 8B CD                        mov rcx, r13
00676AA9  E8 36 26 E6 FF                  call 0x1404d90e4
00676AAE  48 8B C6                        mov rax, rsi
00676AB1  48 F7 D8                        neg rax
00676AB4  4D 1B FF                        sbb r15, r15
00676AB7  4C 23 FE                        and r15, rsi
00676ABA  45 33 ED                        xor r13d, r13d
00676ABD  41 8D 5D 01                     lea ebx, [r13 + 1]
00676AC1  41 8B EC                        mov ebp, r12d
00676AC4  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
00676AC9  49 8B D6                        mov rdx, r14
00676ACC  E8 77 1F D4 FF                  call 0x1403b8a48
00676AD1  B8 11 00 00 00                  mov eax, 0x11
00676AD6  F0 4C 0F B1 2D 69 95 7B 00      lock cmpxchg qword ptr [rip + 0x7b9569], r13
00676ADF  74 0C                           je 0x140676aed
00676AE1  48 8D 0D 60 95 7B 00            lea rcx, [rip + 0x7b9560]
00676AE8  E8 53 C9 BE FF                  call 0x140263440
00676AED  48 8D 0D 54 95 7B 00            lea rcx, [rip + 0x7b9554]
00676AF4  E8 07 AB C6 FF                  call 0x1402e1600
00676AF9  90                              nop
00676AFA  66 41 01 9E E6 01 00 00         add word ptr [r14 + 0x1e6], bx
00676B02  75 12                           jne 0x140676b16
00676B04  49 8D 86 98 00 00 00            lea rax, [r14 + 0x98]
00676B0B  90                              nop
00676B0C  48 39 00                        cmp qword ptr [rax], rax
00676B0F  74 05                           je 0x140676b16
00676B11  E8 6A C1 C6 FF                  call 0x1402e2c80
00676B16  4D 85 FF                        test r15, r15
00676B19  74 15                           je 0x140676b30
00676B1B  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
00676B1F  33 D2                           xor edx, edx
00676B21  E8 4A BD 50 00                  call 0x140b82870
00676B26  33 D2                           xor edx, edx
00676B28  49 8B CF                        mov rcx, r15
00676B2B  E8 40 BD 50 00                  call 0x140b82870
00676B30  41 3B EC                        cmp ebp, r12d
00676B33  75 10                           jne 0x140676b45
00676B35  4C 8D 05 94 C9 99 FF            lea r8, [rip - 0x66366c]
00676B3C  33 D2                           xor edx, edx
00676B3E  33 C9                           xor ecx, ecx
00676B40  E8 0B 2A B9 FF                  call 0x140209550
00676B45  8B C5                           mov eax, ebp
00676B47  EB 4F                           jmp 0x140676b98
00676B49  B8 11 00 00 00                  mov eax, 0x11
00676B4E  F0 4C 0F B1 2D F1 94 7B 00      lock cmpxchg qword ptr [rip + 0x7b94f1], r13
00676B57  74 0C                           je 0x140676b65
00676B59  48 8D 0D E8 94 7B 00            lea rcx, [rip + 0x7b94e8]
00676B60  E8 DB C8 BE FF                  call 0x140263440
00676B65  48 8D 0D DC 94 7B 00            lea rcx, [rip + 0x7b94dc]
00676B6C  E8 8F AA C6 FF                  call 0x1402e1600
00676B71  B9 01 00 00 00                  mov ecx, 1
00676B76  90                              nop
00676B77  66 41 01 8E E6 01 00 00         add word ptr [r14 + 0x1e6], cx
00676B7F  75 12                           jne 0x140676b93
00676B81  49 8D 86 98 00 00 00            lea rax, [r14 + 0x98]
00676B88  90                              nop
00676B89  48 39 00                        cmp qword ptr [rax], rax
00676B8C  74 05                           je 0x140676b93
00676B8E  E8 ED C0 C6 FF                  call 0x1402e2c80
00676B93  B8 34 04 00 C0                  mov eax, 0xc0000434
00676B98  48 83 C4 58                     add rsp, 0x58
00676B9C  41 5F                           pop r15
00676B9E  41 5E                           pop r14
00676BA0  41 5D                           pop r13
00676BA2  41 5C                           pop r12
00676BA4  5F                              pop rdi
00676BA5  5E                              pop rsi
00676BA6  5D                              pop rbp
00676BA7  5B                              pop rbx
00676BA8  C3                              ret
00676BA9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMarkHugePfnBad(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (88);
    v_r13 = 0;
    v_rdi = (a1) >> (18);
    v_rdi = (unsigned int)((v_rdi) & (0x3FFFFFULL));
    *(unsigned __int64 *)(v_rsp - 112) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm1;
    result = MiPageToNode(a1, a2, a3, a4);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 8100007, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 8099964;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 8099952;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_r13 + 1);
    }
loc_006767F1:
    result = MiHugePfnPartition(*(unsigned __int64 *)(v_rip + 8100051) + v_rdi * 8, a2, a3, a4);
    v_stack_m78 = result;
    if (result == 0) goto loc_00676B49;
    result = MiLockDynamicMemoryShared(result, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    result = MiHugePfnPartition(*(unsigned __int64 *)(v_rip + 8100051) + v_rdi * 8, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    if (result == result) goto loc_0067682F;
    result = MiUnlockDynamicMemoryShared(result, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    goto loc_006767F1;
loc_0067682F:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 4))))) != 0) goto loc_00676AC1;
    v_stack_p20 = 0;
loc_0067684F:
    result = MiLockHugePfn(*(unsigned __int64 *)(v_rip + 8099946) + v_rdi * 8, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    v_stack_p18 = (unsigned __int8)(result);
    result = MiIsPageInHugePfn(v_stack_p8, (unsigned __int8)(result), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00676AA6;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8099946) + v_rdi * 8))) & (8)) != 0) goto loc_00676980;
    if (0 != 0) goto loc_006768F9;
    result = MiUnlockHugePfn(*(unsigned __int64 *)(v_rip + 8099946) + v_rdi * 8, (unsigned __int8)(result), a3, a4);
    result = MiAllocatePool(64, (unsigned int)(0x10000ULL), (unsigned int)((unsigned int)((unsigned int)(0x7048694DULL))), a4);
    v_r13 = 0;
    if (result == 0) goto loc_006768EA;
    result = MiAllocatePool(v_r13 + 40 + 24, v_r13 + 40, (unsigned int)((unsigned int)((unsigned int)(0x7048694DULL))), a4);
    if (result == 0) goto loc_006768E0;
    *(unsigned __int64 *)(result + 24) = v_rdi;
    *(unsigned __int64 *)(result + 32) = result;
    goto loc_0067684F;
loc_006768E0:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)((unsigned int)((unsigned int)(0x7048694DULL))), a4);
loc_006768EA:
loc_006768EF:
    goto loc_00676AC4;
loc_006768F9:
    result = (unsigned int)((1) & (7));
    result = (result) - (1);
    v_rbx = 1;
    if (result <= 1) {
        a1 = 0;
        result = MiLockHugeRangeColorHeadAtDpc(a1, a2, (unsigned int)((unsigned int)((unsigned int)(0x7048694DULL))), a4);
        v_rbx = *(unsigned __int64 *)(v_r13);
        v_stack_p20 = result;
    }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 8099497, a2, (unsigned int)((unsigned int)((unsigned int)(0x7048694DULL))), a4);
    a3 = 0;
    if (*(unsigned __int64 *)(v_rip + 8099565) == 0) goto loc_00676967;
loc_0067693B:
    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8099565) + 24)) & (0x3FFFFFULL));
    if (v_rdi >= result) goto loc_00676953;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8099565)) == 0) goto loc_00676967;
    goto loc_0067695C;
loc_00676953:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8099565) + 8) == 0) goto loc_00676961;
loc_0067695C:
    goto loc_0067693B;
loc_00676961:
loc_00676967:
    result = RtlAvlInsertNodeEx(v_rip + 8099503, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8099565) + 8), 1, result);
    v_rbx = (v_rbx) | (8);
    *(unsigned __int64 *)(v_r13) = v_rbx;
    goto loc_006769BA;
loc_00676980:
    v_r15 = 0;
    if (result != 0) { v_r15 = result; }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 8099398, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8099565) + 8), 1, result);
    goto loc_006769B5;
loc_0067699C:
    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8099462) + 24)) & (0x3FFFFFULL));
    if (v_rdi <= result) goto loc_006769B0;
    goto loc_006769B5;
loc_006769B0:
    if (v_rdi >= result) goto loc_006769BA;
loc_006769B5:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8099462) + 8)) != 0) goto loc_0067699C;
loc_006769BA:
    a2 = (unsigned int)((v_stack_p8) & (0x3FFFFULL));
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) {
        result = 1;
    }
    a1 = (condition_is_below) ? 1 : 0;
    if (((v_stack_p10) & (0x10000000ULL)) == 0) goto loc_00676A11;
    if ((unsigned __int8)(a1) != 0) goto loc_00676A1D;
    goto loc_00676A1D;
loc_00676A11:
    if ((unsigned __int8)(a1) != 0) {
    }
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 8099244, a2, 1, result);
    if (v_stack_p20 != 0) {
    }
    v_rbx = (unsigned int)((v_rbx) & (7));
    if ((v_rbx - 1) <= 1) goto loc_00676A59;
    if (v_rbx == 4) goto loc_00676A8F;
    goto loc_00676A8F;
loc_00676A59:
    result = MiHugePfnPartition(0, a2, 1, result);
    result = MiLockHugeRangeColorHeadAtDpc(0, a2, 1, result);
    result = MiUnlinkHugeRange(result, v_rdi, 1, result);
    a1 = 0;
    result = MiInsertHugeRangeInList(a1, v_rdi, 4, result);
loc_00676A8F:
    result = MiUnlockHugePfn(0, v_stack_p18, 4, result);
    v_r13 = 0;
    goto loc_006768EF;
loc_00676AA6:
    result = MiUnlockHugePfn(0, v_stack_p18, 4, result);
    result = -(result);
    v_r15 = (v_r15) & (result);
    v_r13 = 0;
loc_00676AC1:
loc_00676AC4:
    result = MiUnlockDynamicMemoryShared(v_stack_m78, *(unsigned __int64 *)(gs_base + (0 + 392)), 4, result);
    result = 17;
    if (!(condition_is_equal)) {
        a1 = v_rip + 8099168;
        result = ExfReleasePushLockShared(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), 4, result);
    }
    result = KeAbPostRelease(v_rip + 8099156, *(unsigned __int64 *)(gs_base + (0 + 392)), 4, result);
    if (condition_is_not_equal) goto loc_00676B16;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 8099156, *(unsigned __int64 *)(gs_base + (0 + 392)), 4, result);
    }
    if (v_r15 != 0) {
        a1 = *(unsigned __int64 *)(v_r15 + 32);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, 4, result);
        a2 = 0;
        a1 = v_r15;
        result = ExFreePoolWithTag(a1, a2, 4, result);
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000434ULL))))) == ((unsigned int)((unsigned int)(0xC0000434ULL)))) {
        a3 = v_rip - 6698604;
        a2 = 0;
        a1 = 0;
        result = KeDelayExecutionThread(a1, a2, a3, result);
    }
    goto loc_00676B98;
loc_00676B49:
    result = 17;
    if (!(condition_is_equal)) {
        a1 = v_rip + 8099048;
        result = ExfReleasePushLockShared(a1, a2, a3, result);
    }
    result = KeAbPostRelease(v_rip + 8099036, a2, a3, result);
    if (condition_is_not_equal) goto loc_00676B93;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, a2, a3, result);
    }
loc_00676B98:
    v_rsp = (v_rsp) + (88);
    return (unsigned int)(0xC0000434ULL);
}
```

## 5. (Beta) C Style

```c
int64_t MiMarkHugePfnBad(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m78;
    uint32_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (88);
    local_r13 = 0;
    local_rdi = (Arg1) >> (18);
    local_rdi = (uint32_t)((local_rdi) & (0x3FFFFFULL));
    *(uint64_t *)(local_rsp - 0x70) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm1;
    result = MiPageToNode(Arg1, Arg2, Arg3, a4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 8100007, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 8099964;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 8099952;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_r13 + 1);
    }
loc_006767F1:
    result = MiHugePfnPartition(*(uint64_t *)(v_rip + 0x7B98D3) + local_rdi * 8, Arg2, Arg3, a4);
    v_stack_m78 = result;
    if (result == 0) goto loc_00676B49;
    result = MiLockDynamicMemoryShared(result, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, a4);
    result = MiHugePfnPartition(*(uint64_t *)(v_rip + 0x7B98D3) + local_rdi * 8, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, a4);
    if (result == result) goto loc_0067682F;
    result = MiUnlockDynamicMemoryShared(result, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, a4);
    goto loc_006767F1;
loc_0067682F:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x4))))) != 0) goto loc_00676AC1;
    v_stack_p20 = 0;
loc_0067684F:
    result = MiLockHugePfn(*(uint64_t *)(v_rip + 0x7B986A) + local_rdi * 8, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, a4);
    v_stack_p18 = (uint8_t)(result);
    result = MiIsPageInHugePfn(v_stack_p8, (uint8_t)(result), Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_00676AA6;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7B986A) + local_rdi * 8))) & (8)) != 0) goto loc_00676980;
    if (0 != 0) goto loc_006768F9;
    result = MiUnlockHugePfn(*(uint64_t *)(v_rip + 0x7B986A) + local_rdi * 8, (uint8_t)(result), Arg3, a4);
    result = MiAllocatePool(64, (uint32_t)(0x10000ULL), (uint32_t)((uint32_t)((uint32_t)(0x7048694DULL))), a4);
    local_r13 = 0;
    if (result == 0) goto loc_006768EA;
    result = MiAllocatePool(local_r13 + 40 + 24, local_r13 + 40, (uint32_t)((uint32_t)((uint32_t)(0x7048694DULL))), a4);
    if (result == 0) goto loc_006768E0;
    *(uint64_t *)(result + 0x18) = local_rdi;
    *(uint64_t *)(result + 0x20) = result;
    goto loc_0067684F;
loc_006768E0:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x7048694DULL))), a4);
loc_006768EA:
loc_006768EF:
    goto loc_00676AC4;
loc_006768F9:
    result = (uint32_t)((1) & (7));
    result = (result) - (1);
    local_rbx = 1;
    if (result <= 1) {
        Arg1 = 0;
        result = MiLockHugeRangeColorHeadAtDpc(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x7048694DULL))), a4);
        local_rbx = *(uint64_t *)(local_r13);
        v_stack_p20 = result;
    }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 8099497, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x7048694DULL))), a4);
    Arg3 = 0;
    if (*(uint64_t *)(v_rip + 0x7B96ED) == 0) goto loc_00676967;
loc_0067693B:
    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_rip + 0x7B96ED) + 0x18)) & (0x3FFFFFULL));
    if (local_rdi >= result) goto loc_00676953;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x7B96ED)) == 0) goto loc_00676967;
    goto loc_0067695C;
loc_00676953:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x7B96ED) + 0x8) == 0) goto loc_00676961;
loc_0067695C:
    goto loc_0067693B;
loc_00676961:
loc_00676967:
    result = RtlAvlInsertNodeEx(v_rip + 8099503, *(uint64_t *)(*(uint64_t *)(v_rip + 0x7B96ED) + 0x8), 1, result);
    local_rbx = (local_rbx) | (8);
    *(uint64_t *)(local_r13) = local_rbx;
    goto loc_006769BA;
loc_00676980:
    local_r15 = 0;
    if (result != 0) { local_r15 = result; }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 8099398, *(uint64_t *)(*(uint64_t *)(v_rip + 0x7B96ED) + 0x8), 1, result);
    goto loc_006769B5;
loc_0067699C:
    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_rip + 0x7B9686) + 0x18)) & (0x3FFFFFULL));
    if (local_rdi <= result) goto loc_006769B0;
    goto loc_006769B5;
loc_006769B0:
    if (local_rdi >= result) goto loc_006769BA;
loc_006769B5:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7B9686) + 0x8)) != 0) goto loc_0067699C;
loc_006769BA:
    Arg2 = (uint32_t)((v_stack_p8) & (0x3FFFFULL));
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) == 0) {
        result = 1;
    }
    Arg1 = (condition_is_below) ? 1 : 0;
    if (((v_stack_p10) & (0x10000000ULL)) == 0) goto loc_00676A11;
    if ((uint8_t)(Arg1) != 0) goto loc_00676A1D;
    goto loc_00676A1D;
loc_00676A11:
    if ((uint8_t)(Arg1) != 0) {
    }
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 8099244, Arg2, 1, result);
    if (v_stack_p20 != 0) {
    }
    local_rbx = (uint32_t)((local_rbx) & (7));
    if ((local_rbx - 1) <= 1) goto loc_00676A59;
    if (local_rbx == 4) goto loc_00676A8F;
    goto loc_00676A8F;
loc_00676A59:
    result = MiHugePfnPartition(0, Arg2, 1, result);
    result = MiLockHugeRangeColorHeadAtDpc(0, Arg2, 1, result);
    result = MiUnlinkHugeRange(result, local_rdi, 1, result);
    Arg1 = 0;
    result = MiInsertHugeRangeInList(Arg1, local_rdi, 4, result);
loc_00676A8F:
    result = MiUnlockHugePfn(0, v_stack_p18, 4, result);
    local_r13 = 0;
    goto loc_006768EF;
loc_00676AA6:
    result = MiUnlockHugePfn(0, v_stack_p18, 4, result);
    result = -(result);
    local_r15 = (local_r15) & (result);
    local_r13 = 0;
loc_00676AC1:
loc_00676AC4:
    result = MiUnlockDynamicMemoryShared(v_stack_m78, *(uint64_t *)(gs_base + (0 + 0x188)), 4, result);
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = v_rip + 8099168;
        result = ExfReleasePushLockShared(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), 4, result);
    }
    result = KeAbPostRelease(v_rip + 8099156, *(uint64_t *)(gs_base + (0 + 0x188)), 4, result);
    if (condition_is_not_equal) goto loc_00676B16;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 8099156, *(uint64_t *)(gs_base + (0 + 0x188)), 4, result);
    }
    if (local_r15 != 0) {
        Arg1 = *(uint64_t *)(local_r15 + 0x20);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, 4, result);
        Arg2 = 0;
        Arg1 = local_r15;
        result = ExFreePoolWithTag(Arg1, Arg2, 4, result);
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000434ULL))))) == ((uint32_t)((uint32_t)(0xC0000434ULL)))) {
        Arg3 = v_rip - 6698604;
        Arg2 = 0;
        Arg1 = 0;
        result = KeDelayExecutionThread(Arg1, Arg2, Arg3, result);
    }
    goto loc_00676B98;
loc_00676B49:
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = v_rip + 8099048;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, result);
    }
    result = KeAbPostRelease(v_rip + 8099036, Arg2, Arg3, result);
    if (condition_is_not_equal) goto loc_00676B93;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(1, Arg2, Arg3, result);
    }
loc_00676B98:
    local_rsp = (local_rsp) + (88);
    return (uint32_t)(0xC0000434ULL);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00676744&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
