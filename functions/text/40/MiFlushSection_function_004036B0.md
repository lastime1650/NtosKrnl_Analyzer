# MiFlushSection

- RVA: `0x004036B0`–`0x0040465B` (길이 `4,011` bytes)
- VA: `0x00000001404036B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009A750`
- 디코드: `867`개 명령, `4,011/4,011` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **34**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x0040373D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004037C4` → [MiReferenceControlAreaFileWithTag](../34/MiReferenceControlAreaFileWithTag_function_00348390.md) (function, `0x00348390`)
- `0x004037E5` → [PsGetIoPriorityThread](../34/PsGetIoPriorityThread_function_00343930.md) (function, `0x00343930`)
- `0x00403851` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x004038DA` → [MiIncrementSubsectionViewCount](../24/MiIncrementSubsectionViewCount_function_00249440.md) (function, `0x00249440`)
- `0x004038E6` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00403ACB` → [MiAddPageToFlushMdl](../28/MiAddPageToFlushMdl_function_00286930.md) (function, `0x00286930`)
- `0x00403AE5` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00403B2C` → [MiExpandFlushMdl](MiExpandFlushMdl_function_00404A30.md) (function, `0x00404A30`)
- `0x00403B65` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00403BB5` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00403BC8` → [MiCheckProtoPtePageState](../31/MiCheckProtoPtePageState_function_003183E0.md) (function, `0x003183E0`)
- `0x00403C25` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00403C62` → [MiReadyFlushMdlToWrite](MiReadyFlushMdlToWrite_function_00404664.md) (function, `0x00404664`)
- `0x00403CE8` → [MiIssueSynchronousFlush](../29/MiIssueSynchronousFlush_function_0029A588.md) (function, `0x0029A588`)
- `0x00403CFB` → [MiUnlockFlushMdl](MiUnlockFlushMdl_function_00404874.md) (function, `0x00404874`)
- `0x00403D2D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00403D8E` → [MiIssueAsynchronousFlush](../29/MiIssueAsynchronousFlush_function_00299898.md) (function, `0x00299898`)
- `0x00403DBF` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00403DE0` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00403DFD` → [MiDecrementSubsectionViewCount](../29/MiDecrementSubsectionViewCount_function_00298E90.md) (function, `0x00298E90`)
- `0x00403E35` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00403E65` → [ObFastDereferenceObjectDeferDelete](../23/ObFastDereferenceObjectDeferDelete_function_002378C0.md) (function, `0x002378C0`)
- `0x00403E83` → [IoDiskIoAttributionDereference](../34/IoDiskIoAttributionDereference_function_00349978.md) (function, `0x00349978`)
- `0x00403E90` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00403ED0` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00403EEE` → [MiLockSpecialPurposeMemoryCachedPage](MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x00403F21` → [MiEndingOffset](../2A/MiEndingOffset_function_002ACEC8.md) (function, `0x002ACEC8`)
- `0x00403F61` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00403F71` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00403FCF` → [MiFlushSection](MiFlushSection_function_004036B0.md) (function, `0x004036B0`)
- `0x004040AC` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x004040CC` → [ObFastDereferenceObjectDeferDelete](../23/ObFastDereferenceObjectDeferDelete_function_002378C0.md) (function, `0x002378C0`)
- `0x004040D9` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x004040F5` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00404339` → [MiWaitForAsynchronousFlushes](../4D/MiWaitForAsynchronousFlushes_function_004D8FC0.md) (function, `0x004D8FC0`)
- `0x00404368` → [MiFlushWaitForReadInProgress](MiFlushWaitForReadInProgress_function_004032E0.md) (function, `0x004032E0`)
- `0x004043CE` → [MiEndingOffset](../2A/MiEndingOffset_function_002ACEC8.md) (function, `0x002ACEC8`)
- `0x00404440` → [MiWaitForPageWriteCompletion](../2C/MiWaitForPageWriteCompletion_function_002C9EBC.md) (function, `0x002C9EBC`)
- `0x0040447B` → [KeDelayExecutionThread](../20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x004044D3` → [MiInsertUnusedSubsection](../29/MiInsertUnusedSubsection_function_00298D50.md) (function, `0x00298D50`)
- `0x004044EE` → [MiIsRetryIoStatus](MiIsRetryIoStatus_function_00408640.md) (function, `0x00408640`)
- `0x00404549` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0040459A` → [MiFlushFileOnlyMdl](MiFlushFileOnlyMdl_function_00403208.md) (function, `0x00403208`)
- `0x004045AF` → [KeDelayExecutionThread](../20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x004045E9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00404640` → [MiReturnCrossPartitionSectionCharges](../4B/MiReturnCrossPartitionSectionCharges_function_004BA61C.md) (function, `0x004BA61C`)

### Direct callers
- [MmFlushSection](../23/MmFlushSection_function_002375E4.md) at `0x00237721`
- [MmFlushSection](../23/MmFlushSection_function_002375E4.md) at `0x002377D8`
- [MiDeleteCachedSubsection](../29/MiDeleteCachedSubsection_function_00297888.md) at `0x00297A77`
- [MiFlushSection](MiFlushSection_function_004036B0.md) at `0x00403FCF`
- [MiCleanSection](../46/MiCleanSection_function_00462E1C.md) at `0x00462EEB`
- [MmFlushVirtualMemory](../../page/9D/MmFlushVirtualMemory_function_009D6F5C.md) at `0x009D7181`

### Static image references
- `0x004036C3` → RVA `0x00E0A740` (`.data`; read)
- `0x00403943` → RVA `0x00E2DC80` (`.data`; read)
- `0x00403985` → RVA `0x00E2DCE0` (`.data`; read)
- `0x004039E5` → RVA `0x00E30088` (`.data`; read)
- `0x00403A83` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00403F53` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00404470` → RVA `0x000134D0` (`.rdata`; read)
- `0x004045A4` → RVA `0x00011C80` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00403B65` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00403D2D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00404549` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004045E9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00404340` → [sub_006EC360](../6E/Unknown_function_006EC360.md) (`tail-transfer`)
  - `0x00404349` → [sub_006EC360](../6E/Unknown_function_006EC360.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
004036B0  40 53                           push rbx
004036B2  56                              push rsi
004036B3  57                              push rdi
004036B4  41 54                           push r12
004036B6  41 55                           push r13
004036B8  41 56                           push r14
004036BA  41 57                           push r15
004036BC  48 81 EC E0 01 00 00            sub rsp, 0x1e0
004036C3  48 8B 05 76 70 A0 00            mov rax, qword ptr [rip + 0xa07076]
004036CA  48 33 C4                        xor rax, rsp
004036CD  48 89 84 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rax
004036D5  4C 8B BC 24 58 02 00 00         mov r15, qword ptr [rsp + 0x258]
004036DD  4D 8B F0                        mov r14, r8
004036E0  4C 8B AC 24 40 02 00 00         mov r13, qword ptr [rsp + 0x240]
004036E8  48 8B 9C 24 50 02 00 00         mov rbx, qword ptr [rsp + 0x250]
004036F0  4C 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r8
004036F8  41 B8 B8 00 00 00               mov r8d, 0xb8
004036FE  48 89 94 24 00 01 00 00         mov qword ptr [rsp + 0x100], rdx
00403706  48 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rcx
0040370E  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00403716  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
0040371E  33 D2                           xor edx, edx
00403720  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
00403725  4C 89 AC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r13
0040372D  48 89 9C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rbx
00403735  4C 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r9
0040373D  E8 FE 34 2C 00                  call 0x1406c6c40
00403742  33 D2                           xor edx, edx
00403744  48 85 DB                        test rbx, rbx
00403747  0F 85 E7 0D 00 00               jne 0x140404534
0040374D  8B 84 24 48 02 00 00            mov eax, dword ptr [rsp + 0x248]
00403754  4C 8D A4 24 10 01 00 00         lea r12, [rsp + 0x110]
0040375C  41 89 17                        mov dword ptr [r15], edx
0040375F  8B F8                           mov edi, eax
00403761  49 89 57 08                     mov qword ptr [r15 + 8], rdx
00403765  F7 D7                           not edi
00403767  4D 8B 36                        mov r14, qword ptr [r14]
0040376A  83 E7 02                        and edi, 2
0040376D  8B C8                           mov ecx, eax
0040376F  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
00403777  83 C9 04                        or ecx, 4
0040377A  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
00403782  4D 85 ED                        test r13, r13
00403785  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
0040378A  48 8B F2                        mov rsi, rdx
0040378D  0F 44 C8                        cmove ecx, eax
00403790  8B D9                           mov ebx, ecx
00403792  83 E3 FB                        and ebx, 0xfffffffb
00403795  41 F6 46 3E 0C                  test byte ptr [r14 + 0x3e], 0xc
0040379A  0F 44 D9                        cmove ebx, ecx
0040379D  89 9C 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], ebx
004037A4  F6 C3 04                        test bl, 4
004037A7  0F 85 38 09 00 00               jne 0x1404040e5
004037AD  45 33 FF                        xor r15d, r15d
004037B0  48 83 84 24 B8 00 00 00 08      add qword ptr [rsp + 0xb8], 8
004037B9  45 33 C0                        xor r8d, r8d
004037BC  BA 4D 6D 53 63                  mov edx, 0x63536d4d
004037C1  49 8B CE                        mov rcx, r14
004037C4  E8 C7 4B F4 FF                  call 0x140348390
004037C9  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
004037D2  49 8B C9                        mov rcx, r9
004037D5  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
004037DD  4C 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r9
004037E5  E8 46 01 F4 FF                  call 0x140343930
004037EA  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
004037F1  83 F8 02                        cmp eax, 2
004037F4  0F 8C 0C 08 00 00               jl 0x140404006
004037FA  85 DB                           test ebx, ebx
004037FC  0F 88 3A 0D 00 00               js 0x14040453c
00403802  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
0040380A  49 8D 4E 48                     lea rcx, [r14 + 0x48]
0040380E  4D 89 3C 24                     mov qword ptr [r12], r15
00403812  83 CF 20                        or edi, 0x20
00403815  66 45 89 7C 24 0A               mov word ptr [r12 + 0xa], r15w
0040381B  4D 89 7C 24 20                  mov qword ptr [r12 + 0x20], r15
00403820  49 C7 44 24 28 00 00 00 00      mov qword ptr [r12 + 0x28], 0
00403829  66 41 FF 89 E4 01 00 00         dec word ptr [r9 + 0x1e4]
00403831  90                              nop
00403832  44 89 7C 24 68                  mov dword ptr [rsp + 0x68], r15d
00403837  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
0040383C  4C 8B BC 24 E0 00 00 00         mov r15, qword ptr [rsp + 0xe0]
00403844  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
00403849  C7 44 24 44 10 00 00 00         mov dword ptr [rsp + 0x44], 0x10
00403851  E8 3A 4E E4 FF                  call 0x140248690
00403856  49 83 7E 20 00                  cmp qword ptr [r14 + 0x20], 0
0040385B  0F B6 D8                        movzx ebx, al
0040385E  0F 84 41 08 00 00               je 0x1404040a5
00403864  49 8B 76 78                     mov rsi, qword ptr [r14 + 0x78]
00403868  48 83 E6 F8                     and rsi, 0xfffffffffffffff8
0040386C  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
00403871  74 18                           je 0x14040388b
00403873  B8 01 00 00 00                  mov eax, 1
00403878  F0 48 0F C1 46 20               lock xadd qword ptr [rsi + 0x20], rax
0040387E  48 FF C0                        inc rax
00403881  48 83 F8 01                     cmp rax, 1
00403885  0F 8E 9D 0C 00 00               jle 0x140404528
0040388B  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00403893  33 D2                           xor edx, edx
00403895  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
0040389D  49 8D 55 08                     lea rdx, [r13 + 8]
004038A1  4C 3B E9                        cmp r13, rcx
004038A4  0F 85 D9 0A 00 00               jne 0x140404383
004038AA  4C 8B AC 24 B8 00 00 00         mov r13, qword ptr [rsp + 0xb8]
004038B2  4D 85 FF                        test r15, r15
004038B5  0F 84 AF 0C 00 00               je 0x14040456a
004038BB  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
004038C0  41 83 78 68 00                  cmp dword ptr [r8 + 0x68], 0
004038C5  0F 84 98 07 00 00               je 0x140404063
004038CB  48 83 3A 00                     cmp qword ptr [rdx], 0
004038CF  0F 84 8E 07 00 00               je 0x140404063
004038D5  33 D2                           xor edx, edx
004038D7  49 8B C8                        mov rcx, r8
004038DA  E8 61 5B E4 FF                  call 0x140249440
004038DF  0F B6 D3                        movzx edx, bl
004038E2  49 8D 4E 48                     lea rcx, [r14 + 0x48]
004038E6  E8 D5 49 E4 FF                  call 0x1402482c0
004038EB  33 D2                           xor edx, edx
004038ED  4C 89 BC 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r15
004038F5  8B C2                           mov eax, edx
004038F7  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
004038FC  C6 44 24 40 11                  mov byte ptr [rsp + 0x40], 0x11
00403901  4D 3B FD                        cmp r15, r13
00403904  0F 83 A8 04 00 00               jae 0x140403db2
0040390A  49 F7 C7 FF 0F 00 00            test r15, 0xfff
00403911  0F 84 91 02 00 00               je 0x140403ba8
00403917  80 7C 24 40 11                  cmp byte ptr [rsp + 0x40], 0x11
0040391C  0F 84 98 02 00 00               je 0x140403bba
00403922  49 8B 1F                        mov rbx, qword ptr [r15]
00403925  48 8B C3                        mov rax, rbx
00403928  F6 C3 01                        test bl, 1
0040392B  75 47                           jne 0x140403974
0040392D  25 00 0C 00 00                  and eax, 0xc00
00403932  48 3D 00 08 00 00               cmp rax, 0x800
00403938  0F 85 F3 00 00 00               jne 0x140403a31
0040393E  48 85 DB                        test rbx, rbx
00403941  74 10                           je 0x140403953
00403943  48 8B 05 36 A3 A2 00            mov rax, qword ptr [rip + 0xa2a336]
0040394A  48 85 C0                        test rax, rax
0040394D  0F 85 16 01 00 00               jne 0x140403a69
00403953  48 8B 0D 26 A3 A2 00            mov rcx, qword ptr [rip + 0xa2a326]
0040395A  48 8B C3                        mov rax, rbx
0040395D  48 85 C9                        test rcx, rcx
00403960  74 12                           je 0x140403974
00403962  F6 C3 10                        test bl, 0x10
00403965  0F 85 36 01 00 00               jne 0x140403aa1
0040396B  48 8B C1                        mov rax, rcx
0040396E  48 F7 D0                        not rax
00403971  48 23 C3                        and rax, rbx
00403974  48 C1 E8 0C                     shr rax, 0xc
00403978  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00403982  48 23 C1                        and rax, rcx
00403985  48 3B 05 54 A3 A2 00            cmp rax, qword ptr [rip + 0xa2a354]
0040398C  77 94                           ja 0x140403922
0040398E  48 8D 0C 40                     lea rcx, [rax + rax*2]
00403992  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
0040399C  48 03 C9                        add rcx, rcx
0040399F  48 8B C0                        mov rax, rax
004039A2  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
004039A6  48 C1 E8 36                     shr rax, 0x36
004039AA  0F BA E0 00                     bt eax, 0
004039AE  0F 83 6E FF FF FF               jae 0x140403922
004039B4  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004039BE  48 8B C0                        mov rax, rax
004039C1  48 8D 34 C8                     lea rsi, [rax + rcx*8]
004039C5  44 8B F2                        mov r14d, edx
004039C8  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
004039CF  0F 82 AB 00 00 00               jb 0x140403a80
004039D5  49 8B 07                        mov rax, qword ptr [r15]
004039D8  48 3B C3                        cmp rax, rbx
004039DB  0F 85 B1 01 00 00               jne 0x140403b92
004039E1  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
004039E5  48 8B 0D 9C C6 A2 00            mov rcx, qword ptr [rip + 0xa2c69c]
004039EC  48 C1 E8 2B                     shr rax, 0x2b
004039F0  25 FF 03 00 00                  and eax, 0x3ff
004039F5  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
004039F9  8B 40 04                        mov eax, dword ptr [rax + 4]
004039FC  84 C0                           test al, al
004039FE  0F 88 E5 04 00 00               js 0x140403ee9
00403A04  48 85 F6                        test rsi, rsi
00403A07  74 28                           je 0x140403a31
00403A09  49 8B 07                        mov rax, qword ptr [r15]
00403A0C  0F B6 4E 22                     movzx ecx, byte ptr [rsi + 0x22]
00403A10  F6 C1 08                        test cl, 8
00403A13  0F 85 DA 01 00 00               jne 0x140403bf3
00403A19  F6 C1 10                        test cl, 0x10
00403A1C  0F 85 88 00 00 00               jne 0x140403aaa
00403A22  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00403A2C  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00403A31  41 83 7C 24 28 00               cmp dword ptr [r12 + 0x28], 0
00403A37  74 03                           je 0x140403a3c
00403A39  83 CF 04                        or edi, 4
00403A3C  49 83 C7 08                     add r15, 8
00403A40  40 F6 C7 04                     test dil, 4
00403A44  0F 85 C4 01 00 00               jne 0x140403c0e
00403A4A  4D 3B FD                        cmp r15, r13
00403A4D  0F 84 A2 05 00 00               je 0x140403ff5
00403A53  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00403A58  33 D2                           xor edx, edx
00403A5A  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00403A5F  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00403A64  E9 98 FE FF FF                  jmp 0x140403901
00403A69  48 85 D8                        test rax, rbx
00403A6C  0F 84 B0 FE FF FF               je 0x140403922
00403A72  E9 DC FE FF FF                  jmp 0x140403953
00403A77  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00403A80  41 FF C6                        inc r14d
00403A83  44 85 35 22 18 BC 00            test dword ptr [rip + 0xbc1822], r14d
00403A8A  0F 84 C3 04 00 00               je 0x140403f53
00403A90  F3 90                           pause
00403A92  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00403A96  48 85 C0                        test rax, rax
00403A99  0F 89 29 FF FF FF               jns 0x1404039c8
00403A9F  EB DF                           jmp 0x140403a80
00403AA1  48 83 E0 EF                     and rax, 0xffffffffffffffef
00403AA5  E9 CA FE FF FF                  jmp 0x140403974
00403AAA  F6 C1 20                        test cl, 0x20
00403AAD  0F 85 9B 08 00 00               jne 0x14040434e
00403AB3  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00403AB8  48 8B D6                        mov rdx, rsi
00403ABB  44 8B 4C 24 44                  mov r9d, dword ptr [rsp + 0x44]
00403AC0  4D 8B C6                        mov r8, r14
00403AC3  49 8B CC                        mov rcx, r12
00403AC6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00403ACB  E8 60 2E E8 FF                  call 0x140286930
00403AD0  8B D8                           mov ebx, eax
00403AD2  83 F8 01                        cmp eax, 1
00403AD5  0F 8C 61 FF FF FF               jl 0x140403a3c
00403ADB  0F B6 54 24 40                  movzx edx, byte ptr [rsp + 0x40]
00403AE0  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00403AE5  E8 A6 25 E4 FF                  call 0x140246090
00403AEA  C6 44 24 40 11                  mov byte ptr [rsp + 0x40], 0x11
00403AEF  83 FB 03                        cmp ebx, 3
00403AF2  0F 84 37 01 00 00               je 0x140403c2f
00403AF8  83 FB 02                        cmp ebx, 2
00403AFB  0F 84 55 09 00 00               je 0x140404456
00403B01  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
00403B05  83 F9 01                        cmp ecx, 1
00403B08  0F 84 48 09 00 00               je 0x140404456
00403B0E  49 8D 77 08                     lea rsi, [r15 + 8]
00403B12  49 3B F5                        cmp rsi, r13
00403B15  0F 83 3B 09 00 00               jae 0x140404456
00403B1B  FF C9                           dec ecx
00403B1D  49 8B D5                        mov rdx, r13
00403B20  49 2B D7                        sub rdx, r15
00403B23  48 C1 FA 03                     sar rdx, 3
00403B27  03 D1                           add edx, ecx
00403B29  49 8B CC                        mov rcx, r12
00403B2C  E8 FF 0E 00 00                  call 0x140404a30
00403B31  48 8B D8                        mov rbx, rax
00403B34  48 85 C0                        test rax, rax
00403B37  0F 84 35 0A 00 00               je 0x140404572
00403B3D  48 8B B4 24 90 00 00 00         mov rsi, qword ptr [rsp + 0x90]
00403B45  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
00403B4D  4C 3B E0                        cmp r12, rax
00403B50  74 18                           je 0x140403b6a
00403B52  48 85 F6                        test rsi, rsi
00403B55  74 09                           je 0x140403b60
00403B57  48 8D 46 50                     lea rax, [rsi + 0x50]
00403B5B  4C 3B E0                        cmp r12, rax
00403B5E  74 0A                           je 0x140403b6a
00403B60  33 D2                           xor edx, edx
00403B62  49 8B CC                        mov rcx, r12
00403B65  E8 06 ED 77 00                  call 0x140b82870
00403B6A  4C 8B E3                        mov r12, rbx
00403B6D  48 85 F6                        test rsi, rsi
00403B70  74 04                           je 0x140403b76
00403B72  48 89 5E 48                     mov qword ptr [rsi + 0x48], rbx
00403B76  8B 43 2C                        mov eax, dword ptr [rbx + 0x2c]
00403B79  49 83 C7 08                     add r15, 8
00403B7D  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00403B82  33 D2                           xor edx, edx
00403B84  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00403B88  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00403B8D  E9 6F FD FF FF                  jmp 0x140403901
00403B92  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00403B9C  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00403BA1  33 D2                           xor edx, edx
00403BA3  E9 7A FD FF FF                  jmp 0x140403922
00403BA8  0F B6 54 24 40                  movzx edx, byte ptr [rsp + 0x40]
00403BAD  80 FA 11                        cmp dl, 0x11
00403BB0  74 08                           je 0x140403bba
00403BB2  48 8B C8                        mov rcx, rax
00403BB5  E8 D6 24 E4 FF                  call 0x140246090
00403BBA  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00403BBF  45 33 C0                        xor r8d, r8d
00403BC2  49 8B D7                        mov rdx, r15
00403BC5  49 8B CE                        mov rcx, r14
00403BC8  E8 13 48 F1 FF                  call 0x1403183e0
00403BCD  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00403BD2  48 85 C0                        test rax, rax
00403BD5  75 CA                           jne 0x140403ba1
00403BD7  49 81 E7 00 F0 FF FF            and r15, 0xfffffffffffff000
00403BDE  49 81 C7 00 10 00 00            add r15, 0x1000
00403BE5  41 39 44 24 28                  cmp dword ptr [r12 + 0x28], eax
00403BEA  75 2C                           jne 0x140403c18
00403BEC  33 D2                           xor edx, edx
00403BEE  E9 0E FD FF FF                  jmp 0x140403901
00403BF3  41 83 7C 24 28 00               cmp dword ptr [r12 + 0x28], 0
00403BF9  0F 84 21 08 00 00               je 0x140404420
00403BFF  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00403C09  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00403C0E  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00403C13  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00403C18  0F B6 54 24 40                  movzx edx, byte ptr [rsp + 0x40]
00403C1D  80 FA 11                        cmp dl, 0x11
00403C20  74 0D                           je 0x140403c2f
00403C22  48 8B C8                        mov rcx, rax
00403C25  E8 66 24 E4 FF                  call 0x140246090
00403C2A  C6 44 24 40 11                  mov byte ptr [rsp + 0x40], 0x11
00403C2F  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
00403C37  83 E7 FB                        and edi, 0xfffffffb
00403C3A  48 85 C9                        test rcx, rcx
00403C3D  0F 85 40 09 00 00               jne 0x140404583
00403C43  41 8B 44 24 28                  mov eax, dword ptr [r12 + 0x28]
00403C48  49 8B CC                        mov rcx, r12
00403C4B  8B 9C 24 8C 00 00 00            mov ebx, dword ptr [rsp + 0x8c]
00403C52  44 8B C3                        mov r8d, ebx
00403C55  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00403C5A  C1 E0 0C                        shl eax, 0xc
00403C5D  41 89 44 24 28                  mov dword ptr [r12 + 0x28], eax
00403C62  E8 FD 09 00 00                  call 0x140404664
00403C67  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
00403C6F  4C 8B C0                        mov r8, rax
00403C72  48 85 D2                        test rdx, rdx
00403C75  0F 85 D5 00 00 00               jne 0x140403d50
00403C7B  49 8B 44 24 30                  mov rax, qword ptr [r12 + 0x30]
00403C80  0F 57 C0                        xorps xmm0, xmm0
00403C83  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
00403C8B  48 8D 0C 40                     lea rcx, [rax + rax*2]
00403C8F  48 B8 08 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000008
00403C99  48 03 C9                        add rcx, rcx
00403C9C  48 8B C0                        mov rax, rax
00403C9F  48 8B 34 C8                     mov rsi, qword ptr [rax + rcx*8]
00403CA3  49 8B D4                        mov rdx, r12
00403CA6  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
00403CB0  48 0B F0                        or rsi, rax
00403CB3  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
00403CBB  41 F6 46 3E 0C                  test byte ptr [r14 + 0x3e], 0xc
00403CC0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00403CC5  0F 85 C5 08 00 00               jne 0x140404590
00403CCB  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00403CD0  44 8B CB                        mov r9d, ebx
00403CD3  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00403CDB  41 C1 E9 02                     shr r9d, 2
00403CDF  41 80 E1 04                     and r9b, 4
00403CE3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00403CE8  E8 9B 68 E9 FF                  call 0x14029a588
00403CED  4C 8D 84 24 C0 00 00 00         lea r8, [rsp + 0xc0]
00403CF5  49 8B D6                        mov rdx, r14
00403CF8  49 8B CC                        mov rcx, r12
00403CFB  E8 74 0B 00 00                  call 0x140404874
00403D00  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
00403D07  85 DB                           test ebx, ebx
00403D09  0F 88 50 07 00 00               js 0x14040445f
00403D0F  33 D2                           xor edx, edx
00403D11  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
00403D19  89 54 24 68                     mov dword ptr [rsp + 0x68], edx
00403D1D  4C 3B E0                        cmp r12, rax
00403D20  74 1A                           je 0x140403d3c
00403D22  49 8B CC                        mov rcx, r12
00403D25  C7 44 24 44 10 00 00 00         mov dword ptr [rsp + 0x44], 0x10
00403D2D  E8 3E EB 77 00                  call 0x140b82870
00403D32  33 D2                           xor edx, edx
00403D34  4C 8D A4 24 10 01 00 00         lea r12, [rsp + 0x110]
00403D3C  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00403D41  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00403D46  41 89 54 24 28                  mov dword ptr [r12 + 0x28], edx
00403D4B  E9 B1 FB FF FF                  jmp 0x140403901
00403D50  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
00403D57  8B CB                           mov ecx, ebx
00403D59  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00403D5E  4C 8B 8C 24 A0 00 00 00         mov r9, qword ptr [rsp + 0xa0]
00403D66  C1 E9 02                        shr ecx, 2
00403D69  80 E1 04                        and cl, 4
00403D6C  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00403D71  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00403D75  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
00403D79  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00403D81  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00403D86  4C 8B 84 24 80 00 00 00         mov r8, qword ptr [rsp + 0x80]
00403D8E  E8 05 5B E9 FF                  call 0x140299898
00403D93  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00403D9B  48 85 C0                        test rax, rax
00403D9E  0F 85 A2 02 00 00               jne 0x140404046
00403DA4  83 E7 DF                        and edi, 0xffffffdf
00403DA7  4D 8B FD                        mov r15, r13
00403DAA  83 CF 01                        or edi, 1
00403DAD  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00403DB2  0F B6 54 24 40                  movzx edx, byte ptr [rsp + 0x40]
00403DB7  80 FA 11                        cmp dl, 0x11
00403DBA  74 08                           je 0x140403dc4
00403DBC  48 8B C8                        mov rcx, rax
00403DBF  E8 CC 22 E4 FF                  call 0x140246090
00403DC4  49 8B C7                        mov rax, r15
00403DC7  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00403DCB  48 2B 84 24 F8 00 00 00         sub rax, qword ptr [rsp + 0xf8]
00403DD3  48 C1 F8 03                     sar rax, 3
00403DD7  48 C1 E0 0C                     shl rax, 0xc
00403DDB  48 01 44 24 60                  add qword ptr [rsp + 0x60], rax
00403DE0  E8 AB 48 E4 FF                  call 0x140248690
00403DE5  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
00403DEA  0F B6 D8                        movzx ebx, al
00403DED  49 83 7D 10 00                  cmp qword ptr [r13 + 0x10], 0
00403DF2  0F 84 03 01 00 00               je 0x140403efb
00403DF8  33 D2                           xor edx, edx
00403DFA  49 8B CD                        mov rcx, r13
00403DFD  E8 8E 50 E9 FF                  call 0x140298e90
00403E02  48 01 84 24 98 00 00 00         add qword ptr [rsp + 0x98], rax
00403E0A  49 83 7D 50 00                  cmp qword ptr [r13 + 0x50], 0
00403E0F  0F 84 AD 06 00 00               je 0x1404044c2
00403E15  8B C7                           mov eax, edi
00403E17  24 28                           and al, 0x28
00403E19  3C 20                           cmp al, 0x20
00403E1B  75 11                           jne 0x140403e2e
00403E1D  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00403E25  4C 3B E9                        cmp r13, rcx
00403E28  0F 85 C6 05 00 00               jne 0x1404043f4
00403E2E  49 8D 4E 48                     lea rcx, [r14 + 0x48]
00403E32  0F B6 D3                        movzx edx, bl
00403E35  E8 86 44 E4 FF                  call 0x1402482c0
00403E3A  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
00403E42  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
00403E4A  48 85 DB                        test rbx, rbx
00403E4D  0F 85 DA 04 00 00               jne 0x14040432d
00403E53  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
00403E5B  49 8D 4E 40                     lea rcx, [r14 + 0x40]
00403E5F  41 B8 4D 6D 53 63               mov r8d, 0x63536d4d
00403E65  E8 56 3A E3 FF                  call 0x1402378c0
00403E6A  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00403E72  48 85 C9                        test rcx, rcx
00403E75  0F 85 A8 07 00 00               jne 0x140404623
00403E7B  48 85 F6                        test rsi, rsi
00403E7E  74 08                           je 0x140403e88
00403E80  48 8B CE                        mov rcx, rsi
00403E83  E8 F0 5A F4 FF                  call 0x140349978
00403E88  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00403E90  E8 5B B1 E5 FF                  call 0x14025eff0
00403E95  40 F6 C7 01                     test dil, 1
00403E99  0F 85 DC 00 00 00               jne 0x140403f7b
00403E9F  40 F6 C7 08                     test dil, 8
00403EA3  0F 85 A1 07 00 00               jne 0x14040464a
00403EA9  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00403EAE  8B 00                           mov eax, dword ptr [rax]
00403EB0  85 C0                           test eax, eax
00403EB2  0F 88 8C 00 00 00               js 0x140403f44
00403EB8  33 D2                           xor edx, edx
00403EBA  8B CA                           mov ecx, edx
00403EBC  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00403EC1  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00403EC5  48 8B 8C 24 D0 01 00 00         mov rcx, qword ptr [rsp + 0x1d0]
00403ECD  48 33 CC                        xor rcx, rsp
00403ED0  E8 6B 87 2A 00                  call 0x1406ac640
00403ED5  48 81 C4 E0 01 00 00            add rsp, 0x1e0
00403EDC  41 5F                           pop r15
00403EDE  41 5E                           pop r14
00403EE0  41 5D                           pop r13
00403EE2  41 5C                           pop r12
00403EE4  5F                              pop rdi
00403EE5  5E                              pop rsi
00403EE6  5B                              pop rbx
00403EE7  C3                              ret
00403EE8  CC                              int3
00403EE9  33 D2                           xor edx, edx
00403EEB  48 8B CE                        mov rcx, rsi
00403EEE  E8 FD 0A 00 00                  call 0x1404049f0
00403EF3  48 8B F0                        mov rsi, rax
00403EF6  E9 09 FB FF FF                  jmp 0x140403a04
00403EFB  41 8B 4D 34                     mov ecx, dword ptr [r13 + 0x34]
00403EFF  41 8B 45 2C                     mov eax, dword ptr [r13 + 0x2c]
00403F03  81 E1 FF FF FF 3F               and ecx, 0x3fffffff
00403F09  2B C1                           sub eax, ecx
00403F0B  8B C8                           mov ecx, eax
00403F0D  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
00403F11  48 8D 0C C8                     lea rcx, [rax + rcx*8]
00403F15  4C 3B F9                        cmp r15, rcx
00403F18  0F 85 DA FE FF FF               jne 0x140403df8
00403F1E  49 8B CD                        mov rcx, r13
00403F21  E8 A2 8F EA FF                  call 0x1402acec8
00403F26  25 FF 0F 00 00                  and eax, 0xfff
00403F2B  0F 84 C7 FE FF FF               je 0x140403df8
00403F31  B9 00 10 00 00                  mov ecx, 0x1000
00403F36  2B C8                           sub ecx, eax
00403F38  8B C1                           mov eax, ecx
00403F3A  48 29 44 24 60                  sub qword ptr [rsp + 0x60], rax
00403F3F  E9 B4 FE FF FF                  jmp 0x140403df8
00403F44  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00403F49  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00403F4E  E9 6E FF FF FF                  jmp 0x140403ec1
00403F53  8B 05 5F 2B BC 00               mov eax, dword ptr [rip + 0xbc2b5f]
00403F59  A8 40                           test al, 0x40
00403F5B  0F 84 2F FB FF FF               je 0x140403a90
00403F61  E8 2A B5 F0 FF                  call 0x14030f490
00403F66  84 C0                           test al, al
00403F68  0F 84 22 FB FF FF               je 0x140403a90
00403F6E  41 8B CE                        mov ecx, r14d
00403F71  E8 EA B4 F0 FF                  call 0x14030f460
00403F76  E9 17 FB FF FF                  jmp 0x140403a92
00403F7B  8B 84 24 8C 00 00 00            mov eax, dword ptr [rsp + 0x8c]
00403F82  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00403F8A  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
00403F92  33 D2                           xor edx, edx
00403F94  4C 8B 84 24 D8 00 00 00         mov r8, qword ptr [rsp + 0xd8]
00403F9C  83 E0 FB                        and eax, 0xfffffffb
00403F9F  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
00403FA7  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00403FAC  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00403FB1  48 8B 94 24 00 01 00 00         mov rdx, qword ptr [rsp + 0x100]
00403FB9  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00403FBE  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00403FC6  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00403FCA  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00403FCF  E8 DC F6 FF FF                  call 0x1404036b0
00403FD4  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
00403FDC  48 85 D2                        test rdx, rdx
00403FDF  0F 84 E0 FE FF FF               je 0x140403ec5
00403FE5  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00403FED  48 01 0A                        add qword ptr [rdx], rcx
00403FF0  E9 D0 FE FF FF                  jmp 0x140403ec5
00403FF5  41 83 7C 24 28 00               cmp dword ptr [r12 + 0x28], 0
00403FFB  0F 84 52 FA FF FF               je 0x140403a53
00404001  E9 08 FC FF FF                  jmp 0x140403c0e
00404006  41 F7 41 74 00 04 00 00         test dword ptr [r9 + 0x74], 0x400
0040400E  0F 85 E6 F7 FF FF               jne 0x1404037fa
00404014  41 80 B9 32 02 00 00 01         cmp byte ptr [r9 + 0x232], 1
0040401C  0F 84 D8 F7 FF FF               je 0x1404037fa
00404022  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0040402B  BA 02 00 00 00                  mov edx, 2
00404030  48 39 91 50 05 00 00            cmp qword ptr [rcx + 0x550], rdx
00404037  0F 45 C2                        cmovne eax, edx
0040403A  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
00404041  E9 B4 F7 FF FF                  jmp 0x1404037fa
00404046  4C 8B 60 48                     mov r12, qword ptr [rax + 0x48]
0040404A  33 D2                           xor edx, edx
0040404C  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00404051  C7 44 24 44 10 00 00 00         mov dword ptr [rsp + 0x44], 0x10
00404059  41 89 54 24 28                  mov dword ptr [r12 + 0x28], edx
0040405E  E9 9E F8 FF FF                  jmp 0x140403901
00404063  49 8B C5                        mov rax, r13
00404066  49 2B C7                        sub rax, r15
00404069  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
0040406E  48 C1 F8 03                     sar rax, 3
00404072  48 C1 E0 0C                     shl rax, 0xc
00404076  4C 03 F8                        add r15, rax
00404079  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
0040407D  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
00404082  48 85 C0                        test rax, rax
00404085  0F 84 1E 03 00 00               je 0x1404043a9
0040408B  49 3B C8                        cmp rcx, r8
0040408E  0F 84 9A FD FF FF               je 0x140403e2e
00404094  4C 8B 78 08                     mov r15, qword ptr [rax + 8]
00404098  4C 8B E8                        mov r13, rax
0040409B  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
004040A0  E9 F8 F7 FF FF                  jmp 0x14040389d
004040A5  0F B6 D0                        movzx edx, al
004040A8  49 8D 4E 48                     lea rcx, [r14 + 0x48]
004040AC  E8 0F 42 E4 FF                  call 0x1402482c0
004040B1  48 85 F6                        test rsi, rsi
004040B4  0F 85 8A 04 00 00               jne 0x140404544
004040BA  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
004040C2  49 8D 4E 40                     lea rcx, [r14 + 0x40]
004040C6  41 B8 4D 6D 53 63               mov r8d, 0x63536d4d
004040CC  E8 EF 37 E3 FF                  call 0x1402378c0
004040D1  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
004040D9  E8 12 AF E5 FF                  call 0x14025eff0
004040DE  33 C0                           xor eax, eax
004040E0  E9 E0 FD FF FF                  jmp 0x140403ec5
004040E5  BA 00 0A 00 00                  mov edx, 0xa00
004040EA  B9 40 00 00 00                  mov ecx, 0x40
004040EF  41 B8 4D 6D 46 61               mov r8d, 0x61466d4d
004040F5  E8 46 74 F5 FF                  call 0x14035b540
004040FA  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00404102  48 8B F0                        mov rsi, rax
00404105  4D 85 ED                        test r13, r13
00404108  74 0F                           je 0x140404119
0040410A  48 85 C0                        test rax, rax
0040410D  0F 84 FC 02 00 00               je 0x14040440f
00404113  49 89 45 28                     mov qword ptr [r13 + 0x28], rax
00404117  EB 09                           jmp 0x140404122
00404119  48 85 F6                        test rsi, rsi
0040411C  0F 84 8B F6 FF FF               je 0x1404037ad
00404122  66 C7 40 30 00 00               mov word ptr [rax + 0x30], 0
00404128  48 8D 48 30                     lea rcx, [rax + 0x30]
0040412C  C6 41 02 06                     mov byte ptr [rcx + 2], 6
00404130  4C 8D 60 50                     lea r12, [rax + 0x50]
00404134  45 33 FF                        xor r15d, r15d
00404137  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
0040413F  44 89 79 04                     mov dword ptr [rcx + 4], r15d
00404143  48 8D 41 08                     lea rax, [rcx + 8]
00404147  48 89 40 08                     mov qword ptr [rax + 8], rax
0040414B  48 89 00                        mov qword ptr [rax], rax
0040414E  4C 89 6E 28                     mov qword ptr [rsi + 0x28], r13
00404152  4C 89 76 20                     mov qword ptr [rsi + 0x20], r14
00404156  4C 89 66 48                     mov qword ptr [rsi + 0x48], r12
0040415A  48 89 8E 40 08 00 00            mov qword ptr [rsi + 0x840], rcx
00404161  48 8D 8E 38 01 00 00            lea rcx, [rsi + 0x138]
00404168  66 44 89 39                     mov word ptr [rcx], r15w
0040416C  48 8D 41 08                     lea rax, [rcx + 8]
00404170  C6 41 02 06                     mov byte ptr [rcx + 2], 6
00404174  44 89 79 04                     mov dword ptr [rcx + 4], r15d
00404178  48 89 40 08                     mov qword ptr [rax + 8], rax
0040417C  48 89 00                        mov qword ptr [rax], rax
0040417F  48 8D 86 58 01 00 00            lea rax, [rsi + 0x158]
00404186  48 89 86 50 01 00 00            mov qword ptr [rsi + 0x150], rax
0040418D  4C 89 AE 30 01 00 00            mov qword ptr [rsi + 0x130], r13
00404194  4C 89 B6 28 01 00 00            mov qword ptr [rsi + 0x128], r14
0040419B  48 89 8E 48 08 00 00            mov qword ptr [rsi + 0x848], rcx
004041A2  48 8D 8E 40 02 00 00            lea rcx, [rsi + 0x240]
004041A9  66 44 89 39                     mov word ptr [rcx], r15w
004041AD  48 8D 41 08                     lea rax, [rcx + 8]
004041B1  C6 41 02 06                     mov byte ptr [rcx + 2], 6
004041B5  44 89 79 04                     mov dword ptr [rcx + 4], r15d
004041B9  48 89 40 08                     mov qword ptr [rax + 8], rax
004041BD  48 89 00                        mov qword ptr [rax], rax
004041C0  48 8D 86 60 02 00 00            lea rax, [rsi + 0x260]
004041C7  48 89 86 58 02 00 00            mov qword ptr [rsi + 0x258], rax
004041CE  4C 89 AE 38 02 00 00            mov qword ptr [rsi + 0x238], r13
004041D5  4C 89 B6 30 02 00 00            mov qword ptr [rsi + 0x230], r14
004041DC  48 89 8E 50 08 00 00            mov qword ptr [rsi + 0x850], rcx
004041E3  48 8D 8E 48 03 00 00            lea rcx, [rsi + 0x348]
004041EA  66 44 89 39                     mov word ptr [rcx], r15w
004041EE  48 8D 41 08                     lea rax, [rcx + 8]
004041F2  C6 41 02 06                     mov byte ptr [rcx + 2], 6
004041F6  44 89 79 04                     mov dword ptr [rcx + 4], r15d
004041FA  48 89 40 08                     mov qword ptr [rax + 8], rax
004041FE  48 89 00                        mov qword ptr [rax], rax
00404201  48 8D 86 68 03 00 00            lea rax, [rsi + 0x368]
00404208  48 89 86 60 03 00 00            mov qword ptr [rsi + 0x360], rax
0040420F  4C 89 AE 40 03 00 00            mov qword ptr [rsi + 0x340], r13
00404216  4C 89 B6 38 03 00 00            mov qword ptr [rsi + 0x338], r14
0040421D  48 89 8E 58 08 00 00            mov qword ptr [rsi + 0x858], rcx
00404224  48 8D 8E 50 04 00 00            lea rcx, [rsi + 0x450]
0040422B  66 44 89 39                     mov word ptr [rcx], r15w
0040422F  48 8D 41 08                     lea rax, [rcx + 8]
00404233  C6 41 02 06                     mov byte ptr [rcx + 2], 6
00404237  44 89 79 04                     mov dword ptr [rcx + 4], r15d
0040423B  48 89 40 08                     mov qword ptr [rax + 8], rax
0040423F  48 89 00                        mov qword ptr [rax], rax
00404242  48 8D 86 70 04 00 00            lea rax, [rsi + 0x470]
00404249  48 89 86 68 04 00 00            mov qword ptr [rsi + 0x468], rax
00404250  4C 89 AE 48 04 00 00            mov qword ptr [rsi + 0x448], r13
00404257  4C 89 B6 40 04 00 00            mov qword ptr [rsi + 0x440], r14
0040425E  48 89 8E 60 08 00 00            mov qword ptr [rsi + 0x860], rcx
00404265  48 8D 8E 58 05 00 00            lea rcx, [rsi + 0x558]
0040426C  66 44 89 39                     mov word ptr [rcx], r15w
00404270  48 8D 41 08                     lea rax, [rcx + 8]
00404274  C6 41 02 06                     mov byte ptr [rcx + 2], 6
00404278  44 89 79 04                     mov dword ptr [rcx + 4], r15d
0040427C  48 89 40 08                     mov qword ptr [rax + 8], rax
00404280  48 89 00                        mov qword ptr [rax], rax
00404283  48 8D 86 78 05 00 00            lea rax, [rsi + 0x578]
0040428A  48 89 86 70 05 00 00            mov qword ptr [rsi + 0x570], rax
00404291  4C 89 AE 50 05 00 00            mov qword ptr [rsi + 0x550], r13
00404298  4C 89 B6 48 05 00 00            mov qword ptr [rsi + 0x548], r14
0040429F  48 89 8E 68 08 00 00            mov qword ptr [rsi + 0x868], rcx
004042A6  48 8D 8E 60 06 00 00            lea rcx, [rsi + 0x660]
004042AD  66 44 89 39                     mov word ptr [rcx], r15w
004042B1  48 8D 41 08                     lea rax, [rcx + 8]
004042B5  C6 41 02 06                     mov byte ptr [rcx + 2], 6
004042B9  44 89 79 04                     mov dword ptr [rcx + 4], r15d
004042BD  48 89 40 08                     mov qword ptr [rax + 8], rax
004042C1  48 89 00                        mov qword ptr [rax], rax
004042C4  4C 89 AE 58 06 00 00            mov qword ptr [rsi + 0x658], r13
004042CB  48 8D 86 80 06 00 00            lea rax, [rsi + 0x680]
004042D2  48 89 86 78 06 00 00            mov qword ptr [rsi + 0x678], rax
004042D9  4C 89 B6 50 06 00 00            mov qword ptr [rsi + 0x650], r14
004042E0  48 89 8E 70 08 00 00            mov qword ptr [rsi + 0x870], rcx
004042E7  48 8D 8E 68 07 00 00            lea rcx, [rsi + 0x768]
004042EE  66 44 89 39                     mov word ptr [rcx], r15w
004042F2  48 8D 41 08                     lea rax, [rcx + 8]
004042F6  C6 41 02 06                     mov byte ptr [rcx + 2], 6
004042FA  44 89 79 04                     mov dword ptr [rcx + 4], r15d
004042FE  48 89 40 08                     mov qword ptr [rax + 8], rax
00404302  48 89 00                        mov qword ptr [rax], rax
00404305  48 8D 86 88 07 00 00            lea rax, [rsi + 0x788]
0040430C  48 89 86 80 07 00 00            mov qword ptr [rsi + 0x780], rax
00404313  4C 89 AE 60 07 00 00            mov qword ptr [rsi + 0x760], r13
0040431A  4C 89 B6 58 07 00 00            mov qword ptr [rsi + 0x758], r14
00404321  48 89 8E 78 08 00 00            mov qword ptr [rsi + 0x878], rcx
00404328  E9 83 F4 FF FF                  jmp 0x1404037b0
0040432D  4D 85 FF                        test r15, r15
00404330  0F 85 1D FB FF FF               jne 0x140403e53
00404336  48 8B CB                        mov rcx, rbx
00404339  E8 82 4C 0D 00                  call 0x1404d8fc0
0040433E  85 C0                           test eax, eax
00404340  0F 89 1A 80 2E 00               jns 0x1406ec360
00404346  83 CF 01                        or edi, 1
00404349  E9 12 80 2E 00                  jmp 0x1406ec360
0040434E  41 83 7C 24 28 00               cmp dword ptr [r12 + 0x28], 0
00404354  0F 85 A5 F8 FF FF               jne 0x140403bff
0040435A  44 0F B6 44 24 40               movzx r8d, byte ptr [rsp + 0x40]
00404360  48 8B CE                        mov rcx, rsi
00404363  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00404368  E8 73 EF FF FF                  call 0x1404032e0
0040436D  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00404372  33 D2                           xor edx, edx
00404374  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00404379  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0040437E  E9 79 F5 FF FF                  jmp 0x1404038fc
00404383  41 8B 4D 34                     mov ecx, dword ptr [r13 + 0x34]
00404387  41 8B 45 2C                     mov eax, dword ptr [r13 + 0x2c]
0040438B  81 E1 FF FF FF 3F               and ecx, 0x3fffffff
00404391  2B C1                           sub eax, ecx
00404393  8B C8                           mov ecx, eax
00404395  48 8B 02                        mov rax, qword ptr [rdx]
00404398  4C 8D 2C C8                     lea r13, [rax + rcx*8]
0040439C  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
004043A4  E9 09 F5 FF FF                  jmp 0x1404038b2
004043A9  41 8B 48 34                     mov ecx, dword ptr [r8 + 0x34]
004043AD  41 8B 40 2C                     mov eax, dword ptr [r8 + 0x2c]
004043B1  81 E1 FF FF FF 3F               and ecx, 0x3fffffff
004043B7  2B C1                           sub eax, ecx
004043B9  8B C8                           mov ecx, eax
004043BB  48 8B 02                        mov rax, qword ptr [rdx]
004043BE  48 8D 0C C8                     lea rcx, [rax + rcx*8]
004043C2  4C 3B E9                        cmp r13, rcx
004043C5  0F 85 63 FA FF FF               jne 0x140403e2e
004043CB  49 8B C8                        mov rcx, r8
004043CE  E8 F5 8A EA FF                  call 0x1402acec8
004043D3  25 FF 0F 00 00                  and eax, 0xfff
004043D8  0F 84 50 FA FF FF               je 0x140403e2e
004043DE  B9 00 10 00 00                  mov ecx, 0x1000
004043E3  2B C8                           sub ecx, eax
004043E5  8B C1                           mov eax, ecx
004043E7  4C 2B F8                        sub r15, rax
004043EA  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
004043EF  E9 3A FA FF FF                  jmp 0x140403e2e
004043F4  4D 8B 6D 10                     mov r13, qword ptr [r13 + 0x10]
004043F8  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
004043FD  4D 85 ED                        test r13, r13
00404400  0F 84 28 FA FF FF               je 0x140403e2e
00404406  4D 8B 7D 08                     mov r15, qword ptr [r13 + 8]
0040440A  E9 8E F4 FF FF                  jmp 0x14040389d
0040440F  41 C7 07 9A 00 00 C0            mov dword ptr [r15], 0xc000009a
00404416  B8 9A 00 00 C0                  mov eax, 0xc000009a
0040441B  E9 A5 FA FF FF                  jmp 0x140403ec5
00404420  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00404425  40 F6 C7 02                     test dil, 2
00404429  0F 84 D5 01 00 00               je 0x140404604
0040442F  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
00404435  49 8B D6                        mov rdx, r14
00404438  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
0040443D  48 8B CE                        mov rcx, rsi
00404440  E8 77 5A EC FF                  call 0x1402c9ebc
00404445  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0040444A  33 D2                           xor edx, edx
0040444C  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00404451  E9 A6 F4 FF FF                  jmp 0x1404038fc
00404456  49 83 C7 08                     add r15, 8
0040445A  E9 D0 F7 FF FF                  jmp 0x140403c2f
0040445F  4C 8B FE                        mov r15, rsi
00404462  81 FB 54 00 00 C0               cmp ebx, 0xc0000054
00404468  75 7B                           jne 0x1404044e5
0040446A  40 F6 C7 10                     test dil, 0x10
0040446E  74 75                           je 0x1404044e5
00404470  4C 8D 05 59 F0 C0 FF            lea r8, [rip - 0x3f0fa7]
00404477  33 D2                           xor edx, edx
00404479  33 C9                           xor ecx, ecx
0040447B  E8 D0 50 E0 FF                  call 0x140209550
00404480  33 D2                           xor edx, edx
00404482  B8 20 00 00 00                  mov eax, 0x20
00404487  8B DA                           mov ebx, edx
00404489  89 94 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], edx
00404490  83 E7 DF                        and edi, 0xffffffdf
00404493  0B F8                           or edi, eax
00404495  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
0040449D  4C 3B E0                        cmp r12, rax
004044A0  0F 85 2B 01 00 00               jne 0x1404045d1
004044A6  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
004044AB  41 89 54 24 28                  mov dword ptr [r12 + 0x28], edx
004044B0  40 F6 C7 20                     test dil, 0x20
004044B4  75 68                           jne 0x14040451e
004044B6  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
004044BB  89 18                           mov dword ptr [rax], ebx
004044BD  E9 EB F8 FF FF                  jmp 0x140403dad
004044C2  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
004044C6  0F BA E0 10                     bt eax, 0x10
004044CA  0F 82 45 F9 FF FF               jb 0x140403e15
004044D0  49 8B CD                        mov rcx, r13
004044D3  E8 78 48 E9 FF                  call 0x140298d50
004044D8  48 01 84 24 98 00 00 00         add qword ptr [rsp + 0x98], rax
004044E0  E9 30 F9 FF FF                  jmp 0x140403e15
004044E5  41 8B 74 24 28                  mov esi, dword ptr [r12 + 0x28]
004044EA  8B CB                           mov ecx, ebx
004044EC  8B D6                           mov edx, esi
004044EE  E8 4D 41 00 00                  call 0x140408640
004044F3  85 C0                           test eax, eax
004044F5  74 1E                           je 0x140404515
004044F7  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
004044FB  FF C8                           dec eax
004044FD  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00404501  A8 1F                           test al, 0x1f
00404503  0F 85 9B 00 00 00               jne 0x1404045a4
00404509  81 FE 00 10 00 00               cmp esi, 0x1000
0040450F  0F 87 A4 00 00 00               ja 0x1404045b9
00404515  33 D2                           xor edx, edx
00404517  8B C2                           mov eax, edx
00404519  E9 72 FF FF FF                  jmp 0x140404490
0040451E  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00404523  E9 D9 F3 FF FF                  jmp 0x140403901
00404528  B9 0E 00 00 00                  mov ecx, 0xe
0040452D  CD 29                           int 0x29
0040452F  E9 57 F3 FF FF                  jmp 0x14040388b
00404534  48 89 13                        mov qword ptr [rbx], rdx
00404537  E9 11 F2 FF FF                  jmp 0x14040374d
0040453C  83 CF 10                        or edi, 0x10
0040453F  E9 BE F2 FF FF                  jmp 0x140403802
00404544  33 D2                           xor edx, edx
00404546  48 8B CE                        mov rcx, rsi
00404549  E8 22 E3 77 00                  call 0x140b82870
0040454E  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00404556  48 85 C0                        test rax, rax
00404559  0F 84 5B FB FF FF               je 0x1404040ba
0040455F  33 D2                           xor edx, edx
00404561  48 89 50 28                     mov qword ptr [rax + 0x28], rdx
00404565  E9 50 FB FF FF                  jmp 0x1404040ba
0040456A  4C 8B 3A                        mov r15, qword ptr [rdx]
0040456D  E9 49 F3 FF FF                  jmp 0x1404038bb
00404572  41 8B 44 24 2C                  mov eax, dword ptr [r12 + 0x2c]
00404577  4C 8B FE                        mov r15, rsi
0040457A  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0040457E  E9 AC F6 FF FF                  jmp 0x140403c2f
00404583  41 8B 44 24 28                  mov eax, dword ptr [r12 + 0x28]
00404588  48 01 01                        add qword ptr [rcx], rax
0040458B  E9 B3 F6 FF FF                  jmp 0x140403c43
00404590  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00404595  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0040459A  E8 69 EC FF FF                  call 0x140403208
0040459F  E9 49 F7 FF FF                  jmp 0x140403ced
004045A4  4C 8D 05 D5 D6 C0 FF            lea r8, [rip - 0x3f292b]
004045AB  33 D2                           xor edx, edx
004045AD  33 C9                           xor ecx, ecx
004045AF  E8 9C 4F E0 FF                  call 0x140209550
004045B4  E9 C7 FE FF FF                  jmp 0x140404480
004045B9  83 7C 24 44 01                  cmp dword ptr [rsp + 0x44], 1
004045BE  0F 84 51 FF FF FF               je 0x140404515
004045C4  C7 44 24 44 01 00 00 00         mov dword ptr [rsp + 0x44], 1
004045CC  E9 AF FE FF FF                  jmp 0x140404480
004045D1  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
004045D5  B9 10 00 00 00                  mov ecx, 0x10
004045DA  83 F8 01                        cmp eax, 1
004045DD  0F 45 C1                        cmovne eax, ecx
004045E0  33 D2                           xor edx, edx
004045E2  49 8B CC                        mov rcx, r12
004045E5  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
004045E9  E8 82 E2 77 00                  call 0x140b82870
004045EE  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
004045F5  4C 8D A4 24 10 01 00 00         lea r12, [rsp + 0x110]
004045FD  33 D2                           xor edx, edx
004045FF  E9 A2 FE FF FF                  jmp 0x1404044a6
00404604  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0040460E  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00404613  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00404618  4D 8B FD                        mov r15, r13
0040461B  83 CF 08                        or edi, 8
0040461E  E9 8A F7 FF FF                  jmp 0x140403dad
00404623  41 0F B7 46 3C                  movzx eax, word ptr [r14 + 0x3c]
00404628  4C 8B C1                        mov r8, rcx
0040462B  48 8B 0D 56 BA A2 00            mov rcx, qword ptr [rip + 0xa2ba56]
00404632  25 FF 03 00 00                  and eax, 0x3ff
00404637  BA 01 00 00 00                  mov edx, 1
0040463C  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00404640  E8 D7 5F 0B 00                  call 0x1404ba61c
00404645  E9 31 F8 FF FF                  jmp 0x140403e7b
0040464A  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0040464F  B8 33 04 00 C0                  mov eax, 0xc0000433
00404654  89 02                           mov dword ptr [rdx], eax
00404656  E9 EE F8 FF FF                  jmp 0x140403f49
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFlushSection(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m18C;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned int v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned int v_stack_m1D4;
    unsigned __int8 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned int v_stack_p88;
    unsigned int v_stack_p8C;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned int v_stack_pC0;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;

    v_rsp = (v_rsp) - (480);
    result = (*(unsigned __int64 *)(v_rip + 10514550)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m140 = a3;
    v_stack_m118 = a2;
    v_stack_m138 = a1;
    v_stack_m160 = a2;
    a2 = 0;
    v_stack_m1A0 = a8;
    v_stack_m178 = a5;
    v_stack_m130 = a7;
    v_stack_m168 = a4;
    result = memset(v_stack_m108, a2, 184, a4);
    a2 = 0;
    if (a7 != 0) goto loc_00404534;
loc_0040374D:
    *(unsigned int *)(a8) = 0;
    *(unsigned __int64 *)(a8 + 8) = 0;
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)(a6)))));
    v_rdi = (unsigned int)((v_rdi) & (2));
    v_stack_m198 = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) | (4));
    v_stack_m188 = 0;
    v_stack_m1C0 = *(unsigned __int64 *)(a3);
    if (a5 == 0) { a1 = (unsigned int)((unsigned int)(a6)); }
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (0xFFFFFFFBULL));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a3) + 62)) & (12)) == 0) { v_rbx = (unsigned int)(a1); }
    v_stack_m18C = (unsigned int)(v_rbx);
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) goto loc_004040E5;
loc_004037AD:
    v_r15 = 0;
loc_004037B0:
    a3 = 0;
    result = MiReferenceControlAreaFileWithTag(*(unsigned __int64 *)(a3), (unsigned int)(0x63536D4DULL), a3, a4);
    v_stack_m170 = result;
    v_stack_m148 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = PsGetIoPriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x63536D4DULL), a3, *(unsigned __int64 *)(gs_base + (0 + 392)));
    v_stack_m190 = (unsigned int)(result);
    if (((unsigned int)(result)) < 2) goto loc_00404006;
loc_004037FA:
    if (sign_flag) goto loc_0040453C;
loc_00403802:
    *(unsigned __int64 *)(v_stack_m108) = 0;
    v_rdi = (unsigned int)((v_rdi) | (32));
    *(unsigned __int16 *)(v_stack_m108 + 10) = 0;
    *(unsigned __int64 *)(v_stack_m108 + 32) = 0;
    *(unsigned __int64 *)(v_stack_m108 + 40) = 0;
    v_stack_m1B0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1A8 = v_stack_m140;
    v_stack_m1D4 = 16;
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(a3) + 72, (unsigned int)(0x63536D4DULL), a3, *(unsigned __int64 *)(gs_base + (0 + 392)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 32)) == 0) goto loc_004040A5;
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 120)) & (-8);
    v_stack_m1C8 = v_rsi;
    if (condition_is_equal) goto loc_0040388B;
    result = (1) + 1;
    if (result <= 1) goto loc_00404528;
loc_0040388B:
    a2 = 0;
    v_stack_m180 = 0;
loc_0040389D:
    if (v_stack_m140 != v_stack_m168) goto loc_00404383;
loc_004038B2:
    if (v_stack_m138 == 0) goto loc_0040456A;
loc_004038BB:
    if ((*(unsigned int *)(v_stack_m1A8 + 104)) == 0) goto loc_00404063;
    if ((*(unsigned __int64 *)(v_stack_m140 + 8)) == 0) goto loc_00404063;
    a2 = 0;
    result = MiIncrementSubsectionViewCount(v_stack_m1A8, a2, v_stack_m1A8, *(unsigned __int64 *)(gs_base + (0 + 392)));
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(a3) + 72, (unsigned __int8)((unsigned __int8)(result)), v_stack_m1A8, *(unsigned __int64 *)(gs_base + (0 + 392)));
    a2 = 0;
    v_stack_m120 = v_stack_m138;
    v_stack_m1D0 = 0;
loc_004038FC:
    v_stack_m1D8 = 17;
loc_00403901:
    if (v_stack_m138 >= v_stack_m160) goto loc_00403DB2;
    if (((v_stack_m138) & (0xFFFULL)) == 0) goto loc_00403BA8;
    if (v_stack_m1D8 == 17) goto loc_00403BBA;
loc_00403922:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m138))) & (1)) != 0) goto loc_00403974;
    result = (unsigned int)((*(unsigned __int64 *)(v_stack_m138)) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_00403A31;
    if (*(unsigned __int64 *)(v_stack_m138) == 0) goto loc_00403953;
    if (*(unsigned __int64 *)(v_rip + 10658614) != 0) goto loc_00403A69;
loc_00403953:
    if (*(unsigned __int64 *)(v_rip + 10658598) == 0) goto loc_00403974;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m138))) & (16)) != 0) goto loc_00403AA1;
    result = ~(*(unsigned __int64 *)(v_rip + 10658598));
    result = (result) & (*(unsigned __int64 *)(v_stack_m138));
loc_00403974:
    result = (result) >> (12);
    result = (result) & (*(unsigned __int64 *)(v_rip + 10658598));
    if (result > (*(unsigned __int64 *)(v_rip + 10658644))) goto loc_00403922;
    a1 = (result + result * 2) + (result + result * 2);
    result = (*(unsigned __int64 *)(result + a1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_00403922;
loc_004039C8:
    if (condition_is_below) goto loc_00403A80;
    if ((*(unsigned __int64 *)(v_stack_m138)) != (*(unsigned __int64 *)(v_stack_m138))) goto loc_00403B92;
    result = (*(unsigned __int64 *)(result + a1 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_00403EE9;
loc_00403A04:
    if (result + a1 * 8 == 0) goto loc_00403A31;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + a1 * 8 + 34))) & (8)) != 0) goto loc_00403BF3;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + a1 * 8 + 34))) & (16)) != 0) goto loc_00403AAA;
loc_00403A31:
    if ((*(unsigned int *)(v_stack_m108 + 40)) != 0) {
        v_rdi = (unsigned int)((v_rdi) | (4));
    }
    v_r15 = (v_stack_m138) + (8);
    if ((((unsigned __int8)(v_rdi)) & (4)) != 0) goto loc_00403C0E;
    if (v_r15 == v_stack_m160) goto loc_00403FF5;
loc_00403A53:
    a2 = 0;
    goto loc_00403901;
loc_00403A69:
    if (((v_stack_m1D0) & (*(unsigned __int64 *)(v_stack_m138))) == 0) goto loc_00403922;
    goto loc_00403953;
loc_00403A80:
    v_r14 = (unsigned int)((v_stack_m1C0) + 1);
    if (((*(unsigned int *)(v_rip + 12326946)) & ((unsigned int)(v_r14))) == 0) goto loc_00403F53;
loc_00403A90:
loc_00403A92:
    if (!sign_flag) goto loc_004039C8;
    goto loc_00403A80;
loc_00403AA1:
    result = (*(unsigned __int64 *)(v_stack_m1C8 + 24)) & (-17);
    goto loc_00403974;
loc_00403AAA:
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + a1 * 8 + 34))) & (32)) != 0) goto loc_0040434E;
    v_stack_m1F8 = result;
    result = MiAddPageToFlushMdl(v_stack_m108, v_stack_m1C8, v_stack_m1C0, (unsigned int)(v_stack_m1D4));
    if (((unsigned int)(result)) < 1) goto loc_00403A3C;
    result = MiUnlockProtoPoolPage(v_stack_m1D0, v_stack_m1D8, v_stack_m1C0, (unsigned int)(v_stack_m1D4));
    v_stack_m1D8 = 17;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 3) goto loc_00403C2F;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 2) goto loc_00404456;
    if (((unsigned int)((unsigned int)(v_stack_m1D4))) == 1) goto loc_00404456;
    if ((v_r15 + 8) >= v_stack_m160) goto loc_00404456;
    a1 = (unsigned int)(((unsigned int)(v_stack_m1D4)) - 1);
    a2 = (v_stack_m160) - (v_r15);
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) + ((unsigned int)(a1)));
    result = MiExpandFlushMdl(v_stack_m108, a2, v_stack_m1C0, (unsigned int)(v_stack_m1D4));
    if (result == 0) goto loc_00404572;
    if (v_stack_m108 == v_stack_m108) goto loc_00403B6A;
    if (v_stack_m188 == 0) goto loc_00403B60;
    result = v_stack_m188 + 80;
    if (v_stack_m108 != (v_stack_m188 + 80)) {
        a2 = 0;
        a1 = v_stack_m108;
        result = ExFreePoolWithTag(a1, a2, v_stack_m1C0, (unsigned int)(v_stack_m1D4));
    }
    if (v_stack_m188 != 0) {
        *(unsigned __int64 *)(v_stack_m188 + 72) = result;
    }
    v_r15 = (v_r15) + (8);
    a2 = 0;
    v_stack_m1D4 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 44)));
    goto loc_00403901;
loc_00403B92:
loc_00403BA1:
    a2 = 0;
    goto loc_00403922;
loc_00403BA8:
    result = v_stack_m1D0;
    if (((unsigned __int8)(v_stack_m1D8)) != 17) {
        a1 = v_stack_m1D0;
        result = MiUnlockProtoPoolPage(a1, v_stack_m1D8, v_stack_m1C0, (unsigned int)(v_stack_m1D4));
    }
    a3 = 0;
    result = MiCheckProtoPtePageState(v_stack_m1C0, v_r15, a3, v_stack_m1D8);
    v_stack_m1D0 = result;
    if (result != 0) goto loc_00403BA1;
    v_r15 = (v_r15) & (0xFFFFFFFFFFFFF000ULL);
    v_r15 = (v_r15) + (0x1000ULL);
    if ((*(unsigned int *)(result + 40)) != ((unsigned int)(result))) goto loc_00403C18;
    a2 = 0;
    goto loc_00403901;
loc_00403BF3:
    if ((*(unsigned int *)(result + 40)) == 0) goto loc_00404420;
loc_00403BFF:
loc_00403C0E:
loc_00403C18:
    result = v_stack_m1D0;
    if (((unsigned __int8)(v_stack_m1D8)) != 17) {
        a1 = v_stack_m1D0;
        result = MiUnlockProtoPoolPage(a1, v_stack_m1D8, a3, v_stack_m1D8);
        v_stack_m1D8 = 17;
    }
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFBULL));
    if (v_stack_m130 != 0) goto loc_00404583;
loc_00403C43:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 40))) << (12));
    *(unsigned int *)(result + 40) = (unsigned int)(result);
    result = MiReadyFlushMdlToWrite(result, v_stack_m1A8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m18C))), v_stack_m1D8);
    if (v_stack_m188 != 0) goto loc_00403D50;
    v_stack_m158 = v_xmm0;
    a1 = (*(unsigned __int64 *)(result + 48) + *(unsigned __int64 *)(result + 48) * 2) + (*(unsigned __int64 *)(result + 48) + *(unsigned __int64 *)(result + 48) * 2);
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) + a1 * 8)) | (*(unsigned __int64 *)(result + 48));
    v_stack_m1F0 = v_stack_m158;
    if (((*(unsigned __int8 *)(v_stack_m1C0 + 62)) & (12)) != 0) goto loc_00404590;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m18C)))) >> (2));
    a4 = (unsigned __int8)((a4) & (4));
    v_stack_m1F8 = v_stack_m1C8;
    result = MiIssueSynchronousFlush(v_stack_m170, result, result, a4);
loc_00403CED:
    result = MiUnlockFlushMdl(result, v_stack_m1C0, v_stack_m158, a4);
    if (sign_flag) goto loc_0040445F;
    a2 = 0;
    v_stack_m1B0 = 0;
    result = v_stack_m108;
    v_r12 = result;
    if (result != v_stack_m108) {
        a1 = result;
        v_stack_m1D4 = 16;
        result = ExFreePoolWithTag(a1, a2, v_stack_m158, a4);
        a2 = 0;
        v_r12 = v_stack_m108;
    }
    *(unsigned int *)(v_r12 + 40) = 0;
    goto loc_00403901;
loc_00403D50:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m158)))) >> (2));
    a1 = (unsigned __int8)((a1) & (4));
    v_stack_m1E0 = v_stack_m1C8;
    v_stack_m1E8 = (unsigned int)((unsigned int)(v_stack_m190));
    v_stack_m1F0 = (unsigned __int8)(a1);
    v_stack_m1F8 = v_stack_m158;
    result = MiIssueAsynchronousFlush(v_stack_m170, a2, v_stack_m198, v_stack_m178);
    v_stack_m188 = result;
    if (result != 0) goto loc_00404046;
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFDFULL));
    v_rdi = (unsigned int)((v_rdi) | (1));
loc_00403DAD:
loc_00403DB2:
    result = v_stack_m1D0;
    if (((unsigned __int8)(v_stack_m1D8)) != 17) {
        a1 = v_stack_m1D0;
        result = MiUnlockProtoPoolPage(a1, v_stack_m1D8, v_stack_m198, v_stack_m178);
    }
    result = (v_stack_m160) - (v_stack_m120);
    result = (result) >> (3);
    result = (result) << (12);
    result = ExAcquireSpinLockExclusive(v_stack_m1C0 + 72, v_stack_m1D8, v_stack_m198, v_stack_m178);
    if ((*(unsigned __int64 *)(v_stack_m1A8 + 16)) == 0) goto loc_00403EFB;
loc_00403DF8:
    a2 = 0;
    result = MiDecrementSubsectionViewCount(v_stack_m1A8, a2, v_stack_m198, v_stack_m178);
    if ((*(unsigned __int64 *)(v_stack_m1A8 + 80)) == 0) goto loc_004044C2;
loc_00403E15:
    result = (unsigned __int8)(((unsigned int)((unsigned int)(v_rdi))) & (40));
    if (((unsigned __int8)(result)) != 32) goto loc_00403E2E;
    if (v_stack_m1A8 != v_stack_m168) goto loc_004043F4;
loc_00403E2E:
    result = MiReleaseSpinLockExclusive(v_stack_m1C0 + 72, (unsigned __int8)((unsigned __int8)(result)), v_stack_m198, v_stack_m178);
    if (v_stack_m198 != 0) goto loc_0040432D;
loc_00403E53:
    result = ObFastDereferenceObjectDeferDelete(v_stack_m1C0 + 64, v_stack_m170, (unsigned int)(0x63536D4DULL), v_stack_m178);
    if (v_stack_m180 != 0) goto loc_00404623;
loc_00403E7B:
    if (v_stack_m1C8 != 0) {
        a1 = v_stack_m1C8;
        result = IoDiskIoAttributionDereference(a1, v_stack_m170, (unsigned int)(0x63536D4DULL), v_stack_m178);
    }
    result = KeLeaveCriticalRegionThread(v_stack_m148, v_stack_m170, (unsigned int)(0x63536D4DULL), v_stack_m178);
    if ((((unsigned __int8)(v_rdi)) & (1)) != 0) goto loc_00403F7B;
    if ((((unsigned __int8)(v_rdi)) & (8)) != 0) goto loc_0040464A;
    if (sign_flag) goto loc_00403F44;
    a2 = 0;
loc_00403EC1:
    *(unsigned __int64 *)(v_stack_m1A0 + 8) = 0;
loc_00403EC5:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m1A0, (unsigned int)(0x63536D4DULL), v_stack_m178);
    v_rsp = (v_rsp) + (480);
    return result;
loc_00403EE9:
    a2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(v_stack_m1C8, a2, (unsigned int)(0x63536D4DULL), v_stack_m178);
    goto loc_00403A04;
loc_00403EFB:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 52))) & (0x3FFFFFFFULL));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1A8 + 44))) - ((unsigned int)(a1)));
    if (v_stack_m178 != (*(unsigned __int64 *)(v_stack_m1A8 + 8) + (unsigned int)((unsigned int)(result)) * 8)) goto loc_00403DF8;
    result = MiEndingOffset(v_stack_m1A8, a2, (unsigned int)(0x63536D4DULL), v_stack_m178);
    result = (unsigned int)((result) & (0xFFFULL));
    if (condition_is_equal) goto loc_00403DF8;
    a1 = (unsigned int)(((unsigned int)(0x1000ULL)) - ((unsigned int)(result)));
    goto loc_00403DF8;
loc_00403F44:
loc_00403F49:
    goto loc_00403EC1;
loc_00403F53:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12331871)))) & (64)) == 0) goto loc_00403A90;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p60, v_stack_p78, (unsigned int)(0x63536D4DULL), v_stack_m178);
    if ((unsigned __int8)(result) == 0) goto loc_00403A90;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_m1C0)), v_stack_p78, (unsigned int)(0x63536D4DULL), v_stack_m178);
    goto loc_00403A92;
loc_00403F7B:
    a2 = 0;
    result = (unsigned int)(((unsigned int)(v_stack_p8C)) & (0xFFFFFFFBULL));
    v_stack_p80 = 0;
    v_stack_p38 = v_stack_p78;
    v_stack_p30 = v_stack_p80;
    v_stack_p28 = (unsigned int)(result);
    v_stack_p20 = v_stack_m178;
    result = MiFlushSection(v_stack_pE0, v_stack_p100, v_stack_pD8, v_stack_pB0);
    if (v_stack_pE8 == 0) goto loc_00403EC5;
    goto loc_00403EC5;
loc_00403FF5:
    if ((*(unsigned int *)(v_r12 + 40)) == 0) goto loc_00403A53;
    goto loc_00403C0E;
loc_00404006:
    if (((*(unsigned int *)(v_stack_pB0 + 116)) & (0x400ULL)) != 0) goto loc_004037FA;
    if ((*(unsigned __int8 *)(v_stack_pB0 + 562)) == 1) goto loc_004037FA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1360)) != 2) { result = 2; }
    v_stack_p88 = (unsigned int)(result);
    goto loc_004037FA;
loc_00404046:
    a2 = 0;
    v_stack_p44 = 16;
    *(unsigned int *)(*(unsigned __int64 *)(result + 72) + 40) = 0;
    goto loc_00403901;
loc_00404063:
    result = (v_stack_m1A8) - (v_stack_m178);
    result = (result) >> (3);
    result = (result) << (12);
    v_r15 = (v_stack_p60) + (result);
    v_stack_p60 = v_r15;
    if (*(unsigned __int64 *)(v_stack_pD8 + 16) == 0) goto loc_004043A9;
    if ((*(unsigned __int64 *)(gs_base + (0 + 392))) == v_stack_pD8) goto loc_00403E2E;
    v_stack_p70 = *(unsigned __int64 *)(v_stack_pD8 + 16);
    goto loc_0040389D;
loc_004040A5:
    result = MiReleaseSpinLockExclusive(v_stack_m1C0 + 72, (unsigned __int8)(*(unsigned __int64 *)(v_stack_pD8 + 16)), v_stack_pD8, v_stack_pB0);
    if (result != 0) goto loc_00404544;
loc_004040BA:
    result = ObFastDereferenceObjectDeferDelete(v_stack_m1C0 + 64, v_stack_pA8, (unsigned int)(0x63536D4DULL), v_stack_pB0);
    result = KeLeaveCriticalRegionThread(v_stack_pD0, v_stack_pA8, (unsigned int)(0x63536D4DULL), v_stack_pB0);
    result = 0;
    goto loc_00403EC5;
loc_004040E5:
    result = MiAllocatePool(64, (unsigned int)(0xA00ULL), (unsigned int)(0x61466D4DULL), v_stack_pB0);
    v_stack_p80 = result;
    if (*(unsigned __int64 *)(v_stack_pD8 + 16) == 0) goto loc_00404119;
    if (result == 0) goto loc_0040440F;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pD8 + 16) + 40) = result;
    goto loc_00404122;
loc_00404119:
    if (result == 0) goto loc_004037AD;
loc_00404122:
    *(unsigned __int16 *)(result + 48) = 0;
    *(unsigned __int8 *)(result + 48 + 2) = 6;
    v_r15 = 0;
    v_stack_p90 = result;
    *(unsigned int *)(result + 48 + 4) = 0;
    *(unsigned __int64 *)(result + 48 + 8 + 8) = result + 48 + 8;
    *(unsigned __int64 *)(result + 48 + 8) = result + 48 + 8;
    *(unsigned __int64 *)(result + 40) = *(unsigned __int64 *)(v_stack_pD8 + 16);
    *(unsigned __int64 *)(result + 32) = v_stack_m1C0;
    *(unsigned __int64 *)(result + 72) = result + 80;
    *(unsigned __int64 *)(result + 2112) = result + 48;
    *(unsigned __int16 *)(result + 312) = 0;
    *(unsigned __int8 *)(result + 312 + 2) = 6;
    *(unsigned int *)(result + 312 + 4) = 0;
    *(unsigned __int64 *)(result + 312 + 8 + 8) = result + 312 + 8;
    *(unsigned __int64 *)(result + 312 + 8) = result + 312 + 8;
    *(unsigned __int64 *)(result + 336) = result + 344;
    *(unsigned __int64 *)(result + 304) = *(unsigned __int64 *)(v_stack_pD8 + 16);
    *(unsigned __int64 *)(result + 296) = v_stack_m1C0;
    *(unsigned __int64 *)(result + 2120) = result + 312;
    *(unsigned __int16 *)(result + 576) = 0;
    *(unsigned __int8 *)(result + 576 + 2) = 6;
    *(unsigned int *)(result + 576 + 4) = 0;
    *(unsigned __int64 *)(result + 576 + 8 + 8) = result + 576 + 8;
    *(unsigned __int64 *)(result + 576 + 8) = result + 576 + 8;
    *(unsigned __int64 *)(result + 600) = result + 608;
    *(unsigned __int64 *)(result + 568) = *(unsigned __int64 *)(v_stack_pD8 + 16);
    *(unsigned __int64 *)(result + 560) = v_stack_m1C0;
    *(unsigned __int64 *)(result + 2128) = result + 576;
    *(unsigned __int16 *)(result + 840) = 0;
    *(unsigned __int8 *)(result + 840 + 2) = 6;
    *(unsigned int *)(result + 840 + 4) = 0;
    *(unsigned __int64 *)(result + 840 + 8 + 8) = result + 840 + 8;
    *(unsigned __int64 *)(result + 840 + 8) = result + 840 + 8;
    *(unsigned __int64 *)(result + 864) = result + 872;
    *(unsigned __int64 *)(result + 832) = *(unsigned __int64 *)(v_stack_pD8 + 16);
    *(unsigned __int64 *)(result + 824) = v_stack_m1C0;
    *(unsigned __int64 *)(result + 2136) = result + 840;
    *(unsigned __int16 *)(result + 1104) = 0;
    *(unsigned __int8 *)(result + 1104 + 2) = 6;
    *(unsigned int *)(result + 1104 + 4) = 0;
    *(unsigned __int64 *)(result + 1104 + 8 + 8) = result + 1104 + 8;
    *(unsigned __int64 *)(result + 1104 + 8) = result + 1104 + 8;
    *(unsigned __int64 *)(result + 1128) = result + 1136;
    *(unsigned __int64 *)(result + 1096) = *(unsigned __int64 *)(v_stack_pD8 + 16);
    *(unsigned __int64 *)(result + 1088) = v_stack_m1C0;
    *(unsigned __int64 *)(result + 2144) = result + 1104;
    *(unsigned __int16 *)(result + 1368) = 0;
    *(unsigned __int8 *)(result + 1368 + 2) = 6;
    *(unsigned int *)(result + 1368 + 4) = 0;
    *(unsigned __int64 *)(result + 1368 + 8 + 8) = result + 1368 + 8;
    *(unsigned __int64 *)(result + 1368 + 8) = result + 1368 + 8;
    *(unsigned __int64 *)(result + 1392) = result + 1400;
    *(unsigned __int64 *)(result + 1360) = *(unsigned __int64 *)(v_stack_pD8 + 16);
    *(unsigned __int64 *)(result + 1352) = v_stack_m1C0;
    *(unsigned __int64 *)(result + 2152) = result + 1368;
    *(unsigned __int16 *)(result + 1632) = 0;
    *(unsigned __int8 *)(result + 1632 + 2) = 6;
    *(unsigned int *)(result + 1632 + 4) = 0;
    *(unsigned __int64 *)(result + 1632 + 8 + 8) = result + 1632 + 8;
    *(unsigned __int64 *)(result + 1632 + 8) = result + 1632 + 8;
    *(unsigned __int64 *)(result + 1624) = *(unsigned __int64 *)(v_stack_pD8 + 16);
    *(unsigned __int64 *)(result + 1656) = result + 1664;
    *(unsigned __int64 *)(result + 1616) = v_stack_m1C0;
    *(unsigned __int64 *)(result + 2160) = result + 1632;
    *(unsigned __int16 *)(result + 1896) = 0;
    *(unsigned __int8 *)(result + 1896 + 2) = 6;
    *(unsigned int *)(result + 1896 + 4) = 0;
    *(unsigned __int64 *)(result + 1896 + 8 + 8) = result + 1896 + 8;
    *(unsigned __int64 *)(result + 1896 + 8) = result + 1896 + 8;
    *(unsigned __int64 *)(result + 1920) = result + 1928;
    *(unsigned __int64 *)(result + 1888) = *(unsigned __int64 *)(v_stack_pD8 + 16);
    *(unsigned __int64 *)(result + 1880) = v_stack_m1C0;
    *(unsigned __int64 *)(result + 2168) = result + 1896;
    goto loc_004037B0;
loc_0040432D:
    if (0 != 0) goto loc_00403E53;
    result = MiWaitForAsynchronousFlushes(v_stack_m198, (unsigned int)(0xA00ULL), (unsigned int)(0x61466D4DULL), v_stack_pB0);
    v_rdi = (unsigned int)((v_rdi) | (1));
loc_0040434E:
    if ((*(unsigned int *)(result + 80 + 40)) != 0) goto loc_00403BFF;
    result = MiFlushWaitForReadInProgress(result, v_stack_p48, v_stack_p40, v_stack_pB0);
    a2 = 0;
    goto loc_004038FC;
loc_00404383:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pD8 + 16) + 52))) & (0x3FFFFFFFULL));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pD8 + 16) + 44))) - ((unsigned int)(a1)));
    goto loc_004038B2;
loc_004043A9:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p40 + 52))) & (0x3FFFFFFFULL));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p40 + 44))) - ((unsigned int)(a1)));
    if ((*(unsigned __int64 *)(a2) + (unsigned int)((unsigned int)(result)) * 8) != (*(unsigned __int64 *)(a2) + (unsigned int)((unsigned int)(result)) * 8)) goto loc_00403E2E;
    result = MiEndingOffset(v_stack_p40, a2, v_stack_p40, v_stack_pB0);
    result = (unsigned int)((result) & (0xFFFULL));
    if (condition_is_equal) goto loc_00403E2E;
    a1 = (unsigned int)(((unsigned int)(0x1000ULL)) - ((unsigned int)(result)));
    v_r15 = (v_r15) - ((unsigned int)((unsigned int)(a1)));
    v_stack_p60 = v_r15;
    goto loc_00403E2E;
loc_004043F4:
    v_stack_p70 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + (unsigned int)((unsigned int)(result)) * 8 + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + (unsigned int)((unsigned int)(result)) * 8 + 16) == 0) goto loc_00403E2E;
    goto loc_0040389D;
loc_0040440F:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + (unsigned int)((unsigned int)(result)) * 8 + 16) + 8)) = 0xC000009AULL;
    goto loc_00403EC5;
loc_00404420:
    if ((((unsigned __int8)(v_rdi)) & (2)) == 0) goto loc_00404604;
    result = MiWaitForPageWriteCompletion(v_stack_p50, v_stack_p58, v_stack_p48, v_stack_p40);
    a2 = 0;
    goto loc_004038FC;
loc_00404456:
    v_r15 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + (unsigned int)((unsigned int)(result)) * 8 + 16) + 8)) + (8);
    goto loc_00403C2F;
loc_0040445F:
    if (((unsigned int)(v_stack_m198)) != 0xC0000054ULL) goto loc_004044E5;
    if ((((unsigned __int8)(v_rdi)) & (16)) == 0) goto loc_004044E5;
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_rip - 4132775, v_stack_p40);
loc_00404480:
    a2 = 0;
    v_stack_pC0 = 0;
loc_00404490:
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFDFULL));
    v_rdi = (unsigned int)((v_rdi) | (32));
    if ((result + 80) != v_stack_p110) goto loc_004045D1;
loc_004044A6:
    *(unsigned int *)(result + 80 + 40) = 0;
    if ((((unsigned __int8)(v_rdi)) & (32)) != 0) goto loc_0040451E;
    *(unsigned int *)(v_stack_p78) = 0;
    goto loc_00403DAD;
loc_004044C2:
    if (condition_is_below) goto loc_00403E15;
    result = MiInsertUnusedSubsection(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + (unsigned int)((unsigned int)(result)) * 8 + 16), a2, v_rip - 4132775, v_stack_p40);
    goto loc_00403E15;
loc_004044E5:
    result = MiIsRetryIoStatus(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 80 + 40)))), v_rip - 4132775, v_stack_p40);
    if ((unsigned int)(result) == 0) goto loc_00404515;
    result = (unsigned int)(((unsigned int)(v_stack_p68)) - 1);
    v_stack_p68 = (unsigned int)(result);
    if ((((unsigned __int8)(result)) & (31)) != 0) goto loc_004045A4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 80 + 40)))) > 0x1000ULL) goto loc_004045B9;
loc_00404515:
    a2 = 0;
    goto loc_00404490;
loc_0040451E:
    goto loc_00403901;
loc_00404528:
    goto loc_0040388B;
loc_00404534:
    *(unsigned __int64 *)(0) = 0;
    goto loc_0040374D;
loc_0040453C:
    v_rdi = (unsigned int)((v_rdi) | (16));
    goto loc_00403802;
loc_00404544:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)(*(unsigned int *)(result + 80 + 40)), a2, v_rip - 4132775, v_stack_p40);
    if (v_stack_pA0 == 0) goto loc_004040BA;
    a2 = 0;
    *(unsigned __int64 *)(v_stack_pA0 + 40) = 0;
    goto loc_004040BA;
loc_0040456A:
    goto loc_004038BB;
loc_00404572:
    v_stack_p44 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 80 + 44)));
    goto loc_00403C2F;
loc_00404583:
    goto loc_00403C43;
loc_00404590:
    v_stack_p20 = v_stack_p70;
    result = MiFlushFileOnlyMdl((unsigned int)(*(unsigned int *)(result + 80 + 40)), a2, v_rip - 4132775, v_stack_p40);
    goto loc_00403CED;
loc_004045A4:
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_rip - 4139307, v_stack_p40);
    goto loc_00404480;
loc_004045B9:
    if (v_stack_p44 == 1) goto loc_00404515;
    v_stack_p44 = 1;
    goto loc_00404480;
loc_004045D1:
    result = (unsigned int)(v_stack_p44);
    if (((unsigned int)((unsigned int)(v_stack_p44))) != 1) { result = 16; }
    a2 = 0;
    v_stack_p44 = (unsigned int)(result);
    result = ExFreePoolWithTag(result + 80, a2, v_rip - 4139307, v_stack_p40);
    a2 = 0;
    goto loc_004044A6;
loc_00404604:
    v_rdi = (unsigned int)((v_rdi) | (8));
    goto loc_00403DAD;
loc_00404623:
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_p58 + 60)) & (0x3FFULL));
    result = MiReturnCrossPartitionSectionCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10664534) + result * 8), 1, result + 80, v_stack_p40);
    goto loc_00403E7B;
loc_0040464A:
    *(unsigned int *)(v_stack_p78) = (unsigned int)((unsigned int)(0xC0000433ULL));
    goto loc_00403F49;
}
```

## 5. (Beta) C Style

```c
int64_t MiFlushSection(int64_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7, void *Arg8)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m18C;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint32_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint32_t v_stack_m1D4;
    uint8_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m48;
    uint64_t v_stack_p100;
    uint64_t v_stack_p110;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint32_t v_stack_p88;
    uint32_t v_stack_p8C;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint32_t v_stack_pC0;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;

    local_rsp = (local_rsp) - (480);
    result = (*(uint64_t *)(v_rip + 0xA07076)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m140 = Arg3;
    v_stack_m118 = Arg2;
    v_stack_m138 = Arg1;
    v_stack_m160 = Arg2;
    Arg2 = 0;
    v_stack_m1A0 = Arg8;
    v_stack_m178 = Arg5;
    v_stack_m130 = Arg7;
    v_stack_m168 = Arg4;
    result = memset(v_stack_m108, Arg2, 184, Arg4);
    Arg2 = 0;
    if (Arg7 != 0) goto loc_00404534;
loc_0040374D:
    *(uint32_t *)(arg8) = 0;
    *(uint64_t *)(arg8 + 0x8) = 0;
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)(Arg6)))));
    local_rdi = (uint32_t)((local_rdi) & (2));
    v_stack_m198 = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) | (4));
    v_stack_m188 = 0;
    v_stack_m1C0 = *(uint64_t *)(arg3);
    if (Arg5 == 0) { Arg1 = (uint32_t)((uint32_t)(Arg6)); }
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (0xFFFFFFFBULL));
    if (((*(uint8_t *)(*(uint64_t *)(arg3) + 0x3E)) & (12)) == 0) { local_rbx = (uint32_t)(Arg1); }
    v_stack_m18C = (uint32_t)(local_rbx);
    if ((((uint8_t)(local_rbx)) & (4)) != 0) goto loc_004040E5;
loc_004037AD:
    local_r15 = 0;
loc_004037B0:
    Arg3 = 0;
    result = MiReferenceControlAreaFileWithTag(*(uint64_t *)(arg3), (uint32_t)(0x63536D4DULL), Arg3, Arg4);
    v_stack_m170 = result;
    v_stack_m148 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = PsGetIoPriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x63536D4DULL), Arg3, *(uint64_t *)(gs_base + (0 + 0x188)));
    v_stack_m190 = (uint32_t)(result);
    if (((uint32_t)(result)) < 2) goto loc_00404006;
loc_004037FA:
    if (sign_flag) goto loc_0040453C;
loc_00403802:
    *(uint64_t *)(v_stack_m108) = 0;
    local_rdi = (uint32_t)((local_rdi) | (32));
    *(uint16_t *)(v_stack_m108 + 0xA) = 0;
    *(uint64_t *)(v_stack_m108 + 0x20) = 0;
    *(uint64_t *)(v_stack_m108 + 0x28) = 0;
    v_stack_m1B0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1A8 = v_stack_m140;
    v_stack_m1D4 = 16;
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(arg3) + 72, (uint32_t)(0x63536D4DULL), Arg3, *(uint64_t *)(gs_base + (0 + 0x188)));
    if ((*(uint64_t *)(*(uint64_t *)(arg3) + 0x20)) == 0) goto loc_004040A5;
    local_rsi = (*(uint64_t *)(*(uint64_t *)(arg3) + 0x78)) & (-8);
    v_stack_m1C8 = local_rsi;
    if (condition_is_equal) goto loc_0040388B;
    result = (1) + 1;
    if (result <= 1) goto loc_00404528;
loc_0040388B:
    Arg2 = 0;
    v_stack_m180 = 0;
loc_0040389D:
    if (v_stack_m140 != v_stack_m168) goto loc_00404383;
loc_004038B2:
    if (v_stack_m138 == 0) goto loc_0040456A;
loc_004038BB:
    if ((*(uint32_t *)(v_stack_m1A8 + 0x68)) == 0) goto loc_00404063;
    if ((*(uint64_t *)(v_stack_m140 + 0x8)) == 0) goto loc_00404063;
    Arg2 = 0;
    result = MiIncrementSubsectionViewCount(v_stack_m1A8, Arg2, v_stack_m1A8, *(uint64_t *)(gs_base + (0 + 0x188)));
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(arg3) + 72, (uint8_t)((uint8_t)(result)), v_stack_m1A8, *(uint64_t *)(gs_base + (0 + 0x188)));
    Arg2 = 0;
    v_stack_m120 = v_stack_m138;
    v_stack_m1D0 = 0;
loc_004038FC:
    v_stack_m1D8 = 17;
loc_00403901:
    if (v_stack_m138 >= v_stack_m160) goto loc_00403DB2;
    if (((v_stack_m138) & (0xFFFULL)) == 0) goto loc_00403BA8;
    if (v_stack_m1D8 == 17) goto loc_00403BBA;
loc_00403922:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m138))) & (1)) != 0) goto loc_00403974;
    result = (uint32_t)((*(uint64_t *)(v_stack_m138)) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_00403A31;
    if (*(uint64_t *)(v_stack_m138) == 0) goto loc_00403953;
    if (*(uint64_t *)(v_rip + 0xA2A336) != 0) goto loc_00403A69;
loc_00403953:
    if (*(uint64_t *)(v_rip + 0xA2A326) == 0) goto loc_00403974;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m138))) & (16)) != 0) goto loc_00403AA1;
    result = ~(*(uint64_t *)(v_rip + 0xA2A326));
    result = (result) & (*(uint64_t *)(v_stack_m138));
loc_00403974:
    result = (result) >> (12);
    result = (result) & (*(uint64_t *)(v_rip + 0xA2A326));
    if (result > (*(uint64_t *)(v_rip + 0xA2A354))) goto loc_00403922;
    Arg1 = (result + result * 2) + (result + result * 2);
    result = (*(uint64_t *)(result + Arg1 * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_00403922;
loc_004039C8:
    if (condition_is_below) goto loc_00403A80;
    if ((*(uint64_t *)(v_stack_m138)) != (*(uint64_t *)(v_stack_m138))) goto loc_00403B92;
    result = (*(uint64_t *)(result + Arg1 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_00403EE9;
loc_00403A04:
    if (result + Arg1 * 8 == 0) goto loc_00403A31;
    if ((((uint8_t)(*(uint8_t *)(result + Arg1 * 8 + 0x22))) & (8)) != 0) goto loc_00403BF3;
    if ((((uint8_t)(*(uint8_t *)(result + Arg1 * 8 + 0x22))) & (16)) != 0) goto loc_00403AAA;
loc_00403A31:
    if ((*(uint32_t *)(v_stack_m108 + 0x28)) != 0) {
        local_rdi = (uint32_t)((local_rdi) | (4));
    }
    local_r15 = (v_stack_m138) + (8);
    if ((((uint8_t)(local_rdi)) & (4)) != 0) goto loc_00403C0E;
    if (local_r15 == v_stack_m160) goto loc_00403FF5;
loc_00403A53:
    Arg2 = 0;
    goto loc_00403901;
loc_00403A69:
    if (((v_stack_m1D0) & (*(uint64_t *)(v_stack_m138))) == 0) goto loc_00403922;
    goto loc_00403953;
loc_00403A80:
    local_r14 = (uint32_t)((v_stack_m1C0) + 1);
    if (((*(uint32_t *)(v_rip + 0xBC1822)) & ((uint32_t)(local_r14))) == 0) goto loc_00403F53;
loc_00403A90:
loc_00403A92:
    if (!sign_flag) goto loc_004039C8;
    goto loc_00403A80;
loc_00403AA1:
    result = (*(uint64_t *)(v_stack_m1C8 + 0x18)) & (-17);
    goto loc_00403974;
loc_00403AAA:
    if ((((uint8_t)(*(uint8_t *)(result + Arg1 * 8 + 0x22))) & (32)) != 0) goto loc_0040434E;
    v_stack_m1F8 = result;
    result = MiAddPageToFlushMdl(v_stack_m108, v_stack_m1C8, v_stack_m1C0, (uint32_t)(v_stack_m1D4));
    if (((uint32_t)(result)) < 1) goto loc_00403A3C;
    result = MiUnlockProtoPoolPage(v_stack_m1D0, v_stack_m1D8, v_stack_m1C0, (uint32_t)(v_stack_m1D4));
    v_stack_m1D8 = 17;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 3) goto loc_00403C2F;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 2) goto loc_00404456;
    if (((uint32_t)((uint32_t)(v_stack_m1D4))) == 1) goto loc_00404456;
    if ((local_r15 + 8) >= v_stack_m160) goto loc_00404456;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m1D4)) - 1);
    Arg2 = (v_stack_m160) - (local_r15);
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg1)));
    result = MiExpandFlushMdl(v_stack_m108, Arg2, v_stack_m1C0, (uint32_t)(v_stack_m1D4));
    if (result == 0) goto loc_00404572;
    if (v_stack_m108 == v_stack_m108) goto loc_00403B6A;
    if (v_stack_m188 == 0) goto loc_00403B60;
    result = v_stack_m188 + 80;
    if (v_stack_m108 != (v_stack_m188 + 80)) {
        Arg2 = 0;
        Arg1 = v_stack_m108;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m1C0, (uint32_t)(v_stack_m1D4));
    }
    if (v_stack_m188 != 0) {
        *(uint64_t *)(v_stack_m188 + 0x48) = result;
    }
    local_r15 = (local_r15) + (8);
    Arg2 = 0;
    v_stack_m1D4 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x2C)));
    goto loc_00403901;
loc_00403B92:
loc_00403BA1:
    Arg2 = 0;
    goto loc_00403922;
loc_00403BA8:
    result = v_stack_m1D0;
    if (((uint8_t)(v_stack_m1D8)) != 17) {
        Arg1 = v_stack_m1D0;
        result = MiUnlockProtoPoolPage(Arg1, v_stack_m1D8, v_stack_m1C0, (uint32_t)(v_stack_m1D4));
    }
    Arg3 = 0;
    result = MiCheckProtoPtePageState(v_stack_m1C0, local_r15, Arg3, v_stack_m1D8);
    v_stack_m1D0 = result;
    if (result != 0) goto loc_00403BA1;
    local_r15 = (local_r15) & (0xFFFFFFFFFFFFF000ULL);
    local_r15 = (local_r15) + (0x1000ULL);
    if ((*(uint32_t *)(result + 0x28)) != ((uint32_t)(result))) goto loc_00403C18;
    Arg2 = 0;
    goto loc_00403901;
loc_00403BF3:
    if ((*(uint32_t *)(result + 0x28)) == 0) goto loc_00404420;
loc_00403BFF:
loc_00403C0E:
loc_00403C18:
    result = v_stack_m1D0;
    if (((uint8_t)(v_stack_m1D8)) != 17) {
        Arg1 = v_stack_m1D0;
        result = MiUnlockProtoPoolPage(Arg1, v_stack_m1D8, Arg3, v_stack_m1D8);
        v_stack_m1D8 = 17;
    }
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFBULL));
    if (v_stack_m130 != 0) goto loc_00404583;
loc_00403C43:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x28))) << (12));
    *(uint32_t *)(result + 0x28) = (uint32_t)(result);
    result = MiReadyFlushMdlToWrite(result, v_stack_m1A8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m18C))), v_stack_m1D8);
    if (v_stack_m188 != 0) goto loc_00403D50;
    v_stack_m158 = v_xmm0;
    Arg1 = (*(uint64_t *)(result + 0x30) + *(uint64_t *)(result + 0x30) * 2) + (*(uint64_t *)(result + 0x30) + *(uint64_t *)(result + 0x30) * 2);
    local_rsi = (*(uint64_t *)(*(uint64_t *)(result + 0x30) + Arg1 * 8)) | (*(uint64_t *)(result + 0x30));
    v_stack_m1F0 = v_stack_m158;
    if (((*(uint8_t *)(v_stack_m1C0 + 0x3E)) & (12)) != 0) goto loc_00404590;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m18C)))) >> (2));
    Arg4 = (uint8_t)((Arg4) & (4));
    v_stack_m1F8 = v_stack_m1C8;
    result = MiIssueSynchronousFlush(v_stack_m170, result, result, Arg4);
loc_00403CED:
    result = MiUnlockFlushMdl(result, v_stack_m1C0, v_stack_m158, Arg4);
    if (sign_flag) goto loc_0040445F;
    Arg2 = 0;
    v_stack_m1B0 = 0;
    result = v_stack_m108;
    local_r12 = result;
    if (result != v_stack_m108) {
        Arg1 = result;
        v_stack_m1D4 = 16;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m158, Arg4);
        Arg2 = 0;
        local_r12 = v_stack_m108;
    }
    *(uint32_t *)(local_r12 + 0x28) = 0;
    goto loc_00403901;
loc_00403D50:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m158)))) >> (2));
    Arg1 = (uint8_t)((Arg1) & (4));
    v_stack_m1E0 = v_stack_m1C8;
    v_stack_m1E8 = (uint32_t)((uint32_t)(v_stack_m190));
    v_stack_m1F0 = (uint8_t)(Arg1);
    v_stack_m1F8 = v_stack_m158;
    result = MiIssueAsynchronousFlush(v_stack_m170, Arg2, v_stack_m198, v_stack_m178);
    v_stack_m188 = result;
    if (result != 0) goto loc_00404046;
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFDFULL));
    local_rdi = (uint32_t)((local_rdi) | (1));
loc_00403DAD:
loc_00403DB2:
    result = v_stack_m1D0;
    if (((uint8_t)(v_stack_m1D8)) != 17) {
        Arg1 = v_stack_m1D0;
        result = MiUnlockProtoPoolPage(Arg1, v_stack_m1D8, v_stack_m198, v_stack_m178);
    }
    result = (v_stack_m160) - (v_stack_m120);
    result = (result) >> (3);
    result = (result) << (12);
    result = ExAcquireSpinLockExclusive(v_stack_m1C0 + 72, v_stack_m1D8, v_stack_m198, v_stack_m178);
    if ((*(uint64_t *)(v_stack_m1A8 + 0x10)) == 0) goto loc_00403EFB;
loc_00403DF8:
    Arg2 = 0;
    result = MiDecrementSubsectionViewCount(v_stack_m1A8, Arg2, v_stack_m198, v_stack_m178);
    if ((*(uint64_t *)(v_stack_m1A8 + 0x50)) == 0) goto loc_004044C2;
loc_00403E15:
    result = (uint8_t)(((uint32_t)((uint32_t)(local_rdi))) & (40));
    if (((uint8_t)(result)) != 32) goto loc_00403E2E;
    if (v_stack_m1A8 != v_stack_m168) goto loc_004043F4;
loc_00403E2E:
    result = MiReleaseSpinLockExclusive(v_stack_m1C0 + 72, (uint8_t)((uint8_t)(result)), v_stack_m198, v_stack_m178);
    if (v_stack_m198 != 0) goto loc_0040432D;
loc_00403E53:
    result = ObFastDereferenceObjectDeferDelete(v_stack_m1C0 + 64, v_stack_m170, (uint32_t)(0x63536D4DULL), v_stack_m178);
    if (v_stack_m180 != 0) goto loc_00404623;
loc_00403E7B:
    if (v_stack_m1C8 != 0) {
        Arg1 = v_stack_m1C8;
        result = IoDiskIoAttributionDereference(Arg1, v_stack_m170, (uint32_t)(0x63536D4DULL), v_stack_m178);
    }
    result = KeLeaveCriticalRegionThread(v_stack_m148, v_stack_m170, (uint32_t)(0x63536D4DULL), v_stack_m178);
    if ((((uint8_t)(local_rdi)) & (1)) != 0) goto loc_00403F7B;
    if ((((uint8_t)(local_rdi)) & (8)) != 0) goto loc_0040464A;
    if (sign_flag) goto loc_00403F44;
    Arg2 = 0;
loc_00403EC1:
    *(uint64_t *)(v_stack_m1A0 + 0x8) = 0;
loc_00403EC5:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m1A0, (uint32_t)(0x63536D4DULL), v_stack_m178);
    local_rsp = (local_rsp) + (480);
    return result;
loc_00403EE9:
    Arg2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(v_stack_m1C8, Arg2, (uint32_t)(0x63536D4DULL), v_stack_m178);
    goto loc_00403A04;
loc_00403EFB:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x34))) & (0x3FFFFFFFULL));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1A8 + 0x2C))) - ((uint32_t)(Arg1)));
    if (v_stack_m178 != (*(uint64_t *)(v_stack_m1A8 + 0x8) + (uint32_t)((uint32_t)(result)) * 8)) goto loc_00403DF8;
    result = MiEndingOffset(v_stack_m1A8, Arg2, (uint32_t)(0x63536D4DULL), v_stack_m178);
    result = (uint32_t)((result) & (0xFFFULL));
    if (condition_is_equal) goto loc_00403DF8;
    Arg1 = (uint32_t)(((uint32_t)(0x1000ULL)) - ((uint32_t)(result)));
    goto loc_00403DF8;
loc_00403F44:
loc_00403F49:
    goto loc_00403EC1;
loc_00403F53:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBC2B5F)))) & (64)) == 0) goto loc_00403A90;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p60, v_stack_p78, (uint32_t)(0x63536D4DULL), v_stack_m178);
    if ((uint8_t)(result) == 0) goto loc_00403A90;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_m1C0)), v_stack_p78, (uint32_t)(0x63536D4DULL), v_stack_m178);
    goto loc_00403A92;
loc_00403F7B:
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)(v_stack_p8C)) & (0xFFFFFFFBULL));
    v_stack_p80 = 0;
    v_stack_p38 = v_stack_p78;
    v_stack_p30 = v_stack_p80;
    v_stack_p28 = (uint32_t)(result);
    v_stack_p20 = v_stack_m178;
    result = MiFlushSection(v_stack_pE0, v_stack_p100, v_stack_pD8, v_stack_pB0);
    if (v_stack_pE8 == 0) goto loc_00403EC5;
    goto loc_00403EC5;
loc_00403FF5:
    if ((*(uint32_t *)(local_r12 + 0x28)) == 0) goto loc_00403A53;
    goto loc_00403C0E;
loc_00404006:
    if (((*(uint32_t *)(v_stack_pB0 + 0x74)) & (0x400ULL)) != 0) goto loc_004037FA;
    if ((*(uint8_t *)(v_stack_pB0 + 0x232)) == 1) goto loc_004037FA;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x550)) != 2) { result = 2; }
    v_stack_p88 = (uint32_t)(result);
    goto loc_004037FA;
loc_00404046:
    Arg2 = 0;
    v_stack_p44 = 16;
    *(uint32_t *)(*(uint64_t *)(result + 0x48) + 0x28) = 0;
    goto loc_00403901;
loc_00404063:
    result = (v_stack_m1A8) - (v_stack_m178);
    result = (result) >> (3);
    result = (result) << (12);
    local_r15 = (v_stack_p60) + (result);
    v_stack_p60 = local_r15;
    if (*(uint64_t *)(v_stack_pD8 + 0x10) == 0) goto loc_004043A9;
    if ((*(uint64_t *)(gs_base + (0 + 0x188))) == v_stack_pD8) goto loc_00403E2E;
    v_stack_p70 = *(uint64_t *)(v_stack_pD8 + 0x10);
    goto loc_0040389D;
loc_004040A5:
    result = MiReleaseSpinLockExclusive(v_stack_m1C0 + 72, (uint8_t)(*(uint64_t *)(v_stack_pD8 + 0x10)), v_stack_pD8, v_stack_pB0);
    if (result != 0) goto loc_00404544;
loc_004040BA:
    result = ObFastDereferenceObjectDeferDelete(v_stack_m1C0 + 64, v_stack_pA8, (uint32_t)(0x63536D4DULL), v_stack_pB0);
    result = KeLeaveCriticalRegionThread(v_stack_pD0, v_stack_pA8, (uint32_t)(0x63536D4DULL), v_stack_pB0);
    result = 0;
    goto loc_00403EC5;
loc_004040E5:
    result = MiAllocatePool(64, (uint32_t)(0xA00ULL), (uint32_t)(0x61466D4DULL), v_stack_pB0);
    v_stack_p80 = result;
    if (*(uint64_t *)(v_stack_pD8 + 0x10) == 0) goto loc_00404119;
    if (result == 0) goto loc_0040440F;
    *(uint64_t *)(*(uint64_t *)(v_stack_pD8 + 0x10) + 0x28) = result;
    goto loc_00404122;
loc_00404119:
    if (result == 0) goto loc_004037AD;
loc_00404122:
    *(uint16_t *)(result + 0x30) = 0;
    *(uint8_t *)(result + 0x30 + 0x2) = 6;
    local_r15 = 0;
    v_stack_p90 = result;
    *(uint32_t *)(result + 0x30 + 0x4) = 0;
    *(uint64_t *)(result + 0x30 + 0x8 + 0x8) = result + 48 + 8;
    *(uint64_t *)(result + 0x30 + 0x8) = result + 48 + 8;
    *(uint64_t *)(result + 0x28) = *(uint64_t *)(v_stack_pD8 + 0x10);
    *(uint64_t *)(result + 0x20) = v_stack_m1C0;
    *(uint64_t *)(result + 0x48) = result + 80;
    *(uint64_t *)(result + 0x840) = result + 48;
    *(uint16_t *)(result + 0x138) = 0;
    *(uint8_t *)(result + 0x138 + 0x2) = 6;
    *(uint32_t *)(result + 0x138 + 0x4) = 0;
    *(uint64_t *)(result + 0x138 + 0x8 + 0x8) = result + 312 + 8;
    *(uint64_t *)(result + 0x138 + 0x8) = result + 312 + 8;
    *(uint64_t *)(result + 0x150) = result + 344;
    *(uint64_t *)(result + 0x130) = *(uint64_t *)(v_stack_pD8 + 0x10);
    *(uint64_t *)(result + 0x128) = v_stack_m1C0;
    *(uint64_t *)(result + 0x848) = result + 312;
    *(uint16_t *)(result + 0x240) = 0;
    *(uint8_t *)(result + 0x240 + 0x2) = 6;
    *(uint32_t *)(result + 0x240 + 0x4) = 0;
    *(uint64_t *)(result + 0x240 + 0x8 + 0x8) = result + 576 + 8;
    *(uint64_t *)(result + 0x240 + 0x8) = result + 576 + 8;
    *(uint64_t *)(result + 0x258) = result + 608;
    *(uint64_t *)(result + 0x238) = *(uint64_t *)(v_stack_pD8 + 0x10);
    *(uint64_t *)(result + 0x230) = v_stack_m1C0;
    *(uint64_t *)(result + 0x850) = result + 576;
    *(uint16_t *)(result + 0x348) = 0;
    *(uint8_t *)(result + 0x348 + 0x2) = 6;
    *(uint32_t *)(result + 0x348 + 0x4) = 0;
    *(uint64_t *)(result + 0x348 + 0x8 + 0x8) = result + 840 + 8;
    *(uint64_t *)(result + 0x348 + 0x8) = result + 840 + 8;
    *(uint64_t *)(result + 0x360) = result + 872;
    *(uint64_t *)(result + 0x340) = *(uint64_t *)(v_stack_pD8 + 0x10);
    *(uint64_t *)(result + 0x338) = v_stack_m1C0;
    *(uint64_t *)(result + 0x858) = result + 840;
    *(uint16_t *)(result + 0x450) = 0;
    *(uint8_t *)(result + 0x450 + 0x2) = 6;
    *(uint32_t *)(result + 0x450 + 0x4) = 0;
    *(uint64_t *)(result + 0x450 + 0x8 + 0x8) = result + 1104 + 8;
    *(uint64_t *)(result + 0x450 + 0x8) = result + 1104 + 8;
    *(uint64_t *)(result + 0x468) = result + 1136;
    *(uint64_t *)(result + 0x448) = *(uint64_t *)(v_stack_pD8 + 0x10);
    *(uint64_t *)(result + 0x440) = v_stack_m1C0;
    *(uint64_t *)(result + 0x860) = result + 1104;
    *(uint16_t *)(result + 0x558) = 0;
    *(uint8_t *)(result + 0x558 + 0x2) = 6;
    *(uint32_t *)(result + 0x558 + 0x4) = 0;
    *(uint64_t *)(result + 0x558 + 0x8 + 0x8) = result + 1368 + 8;
    *(uint64_t *)(result + 0x558 + 0x8) = result + 1368 + 8;
    *(uint64_t *)(result + 0x570) = result + 1400;
    *(uint64_t *)(result + 0x550) = *(uint64_t *)(v_stack_pD8 + 0x10);
    *(uint64_t *)(result + 0x548) = v_stack_m1C0;
    *(uint64_t *)(result + 0x868) = result + 1368;
    *(uint16_t *)(result + 0x660) = 0;
    *(uint8_t *)(result + 0x660 + 0x2) = 6;
    *(uint32_t *)(result + 0x660 + 0x4) = 0;
    *(uint64_t *)(result + 0x660 + 0x8 + 0x8) = result + 1632 + 8;
    *(uint64_t *)(result + 0x660 + 0x8) = result + 1632 + 8;
    *(uint64_t *)(result + 0x658) = *(uint64_t *)(v_stack_pD8 + 0x10);
    *(uint64_t *)(result + 0x678) = result + 1664;
    *(uint64_t *)(result + 0x650) = v_stack_m1C0;
    *(uint64_t *)(result + 0x870) = result + 1632;
    *(uint16_t *)(result + 0x768) = 0;
    *(uint8_t *)(result + 0x768 + 0x2) = 6;
    *(uint32_t *)(result + 0x768 + 0x4) = 0;
    *(uint64_t *)(result + 0x768 + 0x8 + 0x8) = result + 1896 + 8;
    *(uint64_t *)(result + 0x768 + 0x8) = result + 1896 + 8;
    *(uint64_t *)(result + 0x780) = result + 1928;
    *(uint64_t *)(result + 0x760) = *(uint64_t *)(v_stack_pD8 + 0x10);
    *(uint64_t *)(result + 0x758) = v_stack_m1C0;
    *(uint64_t *)(result + 0x878) = result + 1896;
    goto loc_004037B0;
loc_0040432D:
    if (0 != 0) goto loc_00403E53;
    result = MiWaitForAsynchronousFlushes(v_stack_m198, (uint32_t)(0xA00ULL), (uint32_t)(0x61466D4DULL), v_stack_pB0);
    local_rdi = (uint32_t)((local_rdi) | (1));
loc_0040434E:
    if ((*(uint32_t *)(result + 0x50 + 0x28)) != 0) goto loc_00403BFF;
    result = MiFlushWaitForReadInProgress(result, v_stack_p48, v_stack_p40, v_stack_pB0);
    Arg2 = 0;
    goto loc_004038FC;
loc_00404383:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pD8 + 0x10) + 0x34))) & (0x3FFFFFFFULL));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pD8 + 0x10) + 0x2C))) - ((uint32_t)(Arg1)));
    goto loc_004038B2;
loc_004043A9:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x34))) & (0x3FFFFFFFULL));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p40 + 0x2C))) - ((uint32_t)(Arg1)));
    if ((*(uint64_t *)(Arg2) + (uint32_t)((uint32_t)(result)) * 8) != (*(uint64_t *)(Arg2) + (uint32_t)((uint32_t)(result)) * 8)) goto loc_00403E2E;
    result = MiEndingOffset(v_stack_p40, Arg2, v_stack_p40, v_stack_pB0);
    result = (uint32_t)((result) & (0xFFFULL));
    if (condition_is_equal) goto loc_00403E2E;
    Arg1 = (uint32_t)(((uint32_t)(0x1000ULL)) - ((uint32_t)(result)));
    local_r15 = (local_r15) - ((uint32_t)((uint32_t)(Arg1)));
    v_stack_p60 = local_r15;
    goto loc_00403E2E;
loc_004043F4:
    v_stack_p70 = *(uint64_t *)(*(uint64_t *)(Arg2) + (uint32_t)((uint32_t)(result)) * 8 + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(Arg2) + (uint32_t)((uint32_t)(result)) * 8 + 0x10) == 0) goto loc_00403E2E;
    goto loc_0040389D;
loc_0040440F:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2) + (uint32_t)((uint32_t)(result)) * 8 + 0x10) + 0x8)) = 0xC000009AULL;
    goto loc_00403EC5;
loc_00404420:
    if ((((uint8_t)(local_rdi)) & (2)) == 0) goto loc_00404604;
    result = MiWaitForPageWriteCompletion(v_stack_p50, v_stack_p58, v_stack_p48, v_stack_p40);
    Arg2 = 0;
    goto loc_004038FC;
loc_00404456:
    local_r15 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2) + (uint32_t)((uint32_t)(result)) * 8 + 0x10) + 0x8)) + (8);
    goto loc_00403C2F;
loc_0040445F:
    if (((uint32_t)(v_stack_m198)) != 0xC0000054ULL) goto loc_004044E5;
    if ((((uint8_t)(local_rdi)) & (16)) == 0) goto loc_004044E5;
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_rip - 4132775, v_stack_p40);
loc_00404480:
    Arg2 = 0;
    v_stack_pC0 = 0;
loc_00404490:
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFDFULL));
    local_rdi = (uint32_t)((local_rdi) | (32));
    if ((result + 80) != v_stack_p110) goto loc_004045D1;
loc_004044A6:
    *(uint32_t *)(result + 0x50 + 0x28) = 0;
    if ((((uint8_t)(local_rdi)) & (32)) != 0) goto loc_0040451E;
    *(uint32_t *)(v_stack_p78) = 0;
    goto loc_00403DAD;
loc_004044C2:
    if (condition_is_below) goto loc_00403E15;
    result = MiInsertUnusedSubsection(*(uint64_t *)(*(uint64_t *)(Arg2) + (uint32_t)((uint32_t)(result)) * 8 + 0x10), Arg2, v_rip - 4132775, v_stack_p40);
    goto loc_00403E15;
loc_004044E5:
    result = MiIsRetryIoStatus(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x50 + 0x28)))), v_rip - 4132775, v_stack_p40);
    if ((uint32_t)(result) == 0) goto loc_00404515;
    result = (uint32_t)(((uint32_t)(v_stack_p68)) - 1);
    v_stack_p68 = (uint32_t)(result);
    if ((((uint8_t)(result)) & (31)) != 0) goto loc_004045A4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x50 + 0x28)))) > 0x1000ULL) goto loc_004045B9;
loc_00404515:
    Arg2 = 0;
    goto loc_00404490;
loc_0040451E:
    goto loc_00403901;
loc_00404528:
    goto loc_0040388B;
loc_00404534:
    *(uint64_t *)(0) = 0;
    goto loc_0040374D;
loc_0040453C:
    local_rdi = (uint32_t)((local_rdi) | (16));
    goto loc_00403802;
loc_00404544:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)(*(uint32_t *)(result + 0x50 + 0x28)), Arg2, v_rip - 4132775, v_stack_p40);
    if (v_stack_pA0 == 0) goto loc_004040BA;
    Arg2 = 0;
    *(uint64_t *)(v_stack_pA0 + 0x28) = 0;
    goto loc_004040BA;
loc_0040456A:
    goto loc_004038BB;
loc_00404572:
    v_stack_p44 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x50 + 0x2C)));
    goto loc_00403C2F;
loc_00404583:
    goto loc_00403C43;
loc_00404590:
    v_stack_p20 = v_stack_p70;
    result = MiFlushFileOnlyMdl((uint32_t)(*(uint32_t *)(result + 0x50 + 0x28)), Arg2, v_rip - 4132775, v_stack_p40);
    goto loc_00403CED;
loc_004045A4:
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_rip - 4139307, v_stack_p40);
    goto loc_00404480;
loc_004045B9:
    if (v_stack_p44 == 1) goto loc_00404515;
    v_stack_p44 = 1;
    goto loc_00404480;
loc_004045D1:
    result = (uint32_t)(v_stack_p44);
    if (((uint32_t)((uint32_t)(v_stack_p44))) != 1) { result = 16; }
    Arg2 = 0;
    v_stack_p44 = (uint32_t)(result);
    result = ExFreePoolWithTag(result + 80, Arg2, v_rip - 4139307, v_stack_p40);
    Arg2 = 0;
    goto loc_004044A6;
loc_00404604:
    local_rdi = (uint32_t)((local_rdi) | (8));
    goto loc_00403DAD;
loc_00404623:
    result = (uint32_t)((*(uint16_t *)(v_stack_p58 + 0x3C)) & (0x3FFULL));
    result = MiReturnCrossPartitionSectionCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA2BA56) + result * 8), 1, result + 80, v_stack_p40);
    goto loc_00403E7B;
loc_0040464A:
    *(uint32_t *)(v_stack_p78) = (uint32_t)((uint32_t)(0xC0000433ULL));
    goto loc_00403F49;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg8` | `+ 0x0` | `32` | `W` |
| `Arg8` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004036B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
