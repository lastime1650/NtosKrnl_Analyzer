# NtEnumerateBootEntries

- RVA: `0x00A25040`–`0x00A2568F` (길이 `1,615` bytes)
- VA: `0x0000000140A25040`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AB938`
- 디코드: `392`개 명령, `1,615/1,615` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00A25086` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00A25105` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00A25119` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00A25179` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x00A25191` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A251BB` → [IoEnumerateEnvironmentVariablesEx](IoEnumerateEnvironmentVariablesEx_function_00A2592C.md) (function, `0x00A2592C`)
- `0x00A251D6` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x00A251DB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A2523B` → [ExpTranslateBootEntryNameToId](ExpTranslateBootEntryNameToId_function_00A25718.md) (function, `0x00A25718`)
- `0x00A2527E` → [ExpSafeWcslen](ExpSafeWcslen_function_00A25698.md) (function, `0x00A25698`)
- `0x00A2532F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A2533F` → [ExpVerifyFilePath](ExpVerifyFilePath_function_00A257F0.md) (function, `0x00A257F0`)
- `0x00A253C2` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A25422` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A25448` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A2548A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A25497` → [ExpIsDevicePathForRemovableMedia](../../text/4A/ExpIsDevicePathForRemovableMedia_function_004A5880.md) (function, `0x004A5880`)
- `0x00A2550D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A25568` → [strcmp](../../text/6C/strcmp_function_006C7000.md) (function, `0x006C7000`)
- `0x00A2557C` → [ExpVerifyWindowsOsOptions](ExpVerifyWindowsOsOptions_function_00A24CD8.md) (function, `0x00A24CD8`)
- `0x00A255F9` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x00A25625` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2567B` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (function, `0x0029F258`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A25069` → RVA `0x00EFF050` (`.data`; read)
- `0x00A25112` → RVA `0x00FD9AB8` (`PAGEDATA`; read)
- `0x00A25172` → RVA `0x00EFAB40` (`.data`; read)
- `0x00A251AF` → RVA `0x00A256D0` (`ExpIsBootEntry`; read)
- `0x00A25203` → RVA `0x00019EF8` (`.rdata`; read)
- `0x00A2520A` → RVA `0x00019EF0` (`.rdata`; read)
- `0x00A2555D` → RVA `0x00B08730` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x00A25086` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00A25179` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (`PAGE` → `.text`)
  - `0x00A25191` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A251D6` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x00A251DB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A2532F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A253C2` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A25422` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A25448` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A2548A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A25497` → [ExpIsDevicePathForRemovableMedia](../../text/4A/ExpIsDevicePathForRemovableMedia_function_004A5880.md) (`PAGE` → `.text`)
  - `0x00A2550D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A25568` → [strcmp](../../text/6C/strcmp_function_006C7000.md) (`PAGE` → `.text`)
  - `0x00A25625` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A2567B` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00A2561A` → [sub_00B37D12](../B3/Unknown_function_00B37D12.md) (`tail-transfer`)
  - `0x00A2562E` → [sub_00B37D12](../B3/Unknown_function_00B37D12.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A25040  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00A25045  53                              push rbx
00A25046  56                              push rsi
00A25047  57                              push rdi
00A25048  41 54                           push r12
00A2504A  41 55                           push r13
00A2504C  41 56                           push r14
00A2504E  41 57                           push r15
00A25050  48 81 EC D0 00 00 00            sub rsp, 0xd0
00A25057  4C 8B E2                        mov r12, rdx
00A2505A  48 8B F9                        mov rdi, rcx
00A2505D  48 83 64 24 70 00               and qword ptr [rsp + 0x70], 0
00A25063  48 83 64 24 78 00               and qword ptr [rsp + 0x78], 0
00A25069  83 3D E0 9F 4D 00 02            cmp dword ptr [rip + 0x4d9fe0], 2
00A25070  0F 85 0F 06 00 00               jne 0x140a25685
00A25076  48 8B C1                        mov rax, rcx
00A25079  48 83 E0 FC                     and rax, 0xfffffffffffffffc
00A2507D  48 3B C1                        cmp rax, rcx
00A25080  0F 85 47 05 00 00               jne 0x140a255cd
00A25086  E8 55 12 A1 FF                  call 0x1404362e0
00A2508B  84 C0                           test al, al
00A2508D  0F 85 F2 05 00 00               jne 0x140a25685
00A25093  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A2509C  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
00A250A4  40 8A B0 32 02 00 00            mov sil, byte ptr [rax + 0x232]
00A250AB  40 88 74 24 34                  mov byte ptr [rsp + 0x34], sil
00A250B0  40 84 F6                        test sil, sil
00A250B3  75 18                           jne 0x140a250cd
00A250B5  41 8B 0C 24                     mov ecx, dword ptr [r12]
00A250B9  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
00A250BD  48 8B C7                        mov rax, rdi
00A250C0  48 F7 D8                        neg rax
00A250C3  1B DB                           sbb ebx, ebx
00A250C5  23 D9                           and ebx, ecx
00A250C7  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00A250CB  EB 66                           jmp 0x140a25133
00A250CD  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00A250D7  4C 3B E1                        cmp r12, rcx
00A250DA  49 0F 42 CC                     cmovb rcx, r12
00A250DE  8B 01                           mov eax, dword ptr [rcx]
00A250E0  89 01                           mov dword ptr [rcx], eax
00A250E2  41 8B 0C 24                     mov ecx, dword ptr [r12]
00A250E6  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
00A250EA  48 8B C7                        mov rax, rdi
00A250ED  48 F7 D8                        neg rax
00A250F0  1B DB                           sbb ebx, ebx
00A250F2  23 D9                           and ebx, ecx
00A250F4  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00A250F8  74 10                           je 0x140a2510a
00A250FA  8B D3                           mov edx, ebx
00A250FC  41 B8 04 00 00 00               mov r8d, 4
00A25102  48 8B CF                        mov rcx, rdi
00A25105  E8 B6 40 EC FF                  call 0x1408e91c0
00A2510A  40 8A 74 24 34                  mov sil, byte ptr [rsp + 0x34]
00A2510F  40 8A D6                        mov dl, sil
00A25112  48 8B 0D 9F 49 5B 00            mov rcx, qword ptr [rip + 0x5b499f]
00A25119  E8 02 CD E4 FF                  call 0x140871e20
00A2511E  88 84 24 28 01 00 00            mov byte ptr [rsp + 0x128], al
00A25125  84 C0                           test al, al
00A25127  75 0A                           jne 0x140a25133
00A25129  B8 61 00 00 C0                  mov eax, 0xc0000061
00A2512E  E9 00 04 00 00                  jmp 0x140a25533
00A25133  EB 05                           jmp 0x140a2513a
00A25135  E9 F9 03 00 00                  jmp 0x140a25533
00A2513A  85 DB                           test ebx, ebx
00A2513C  0F 85 95 04 00 00               jne 0x140a255d7
00A25142  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
00A25147  33 C0                           xor eax, eax
00A25149  85 DB                           test ebx, ebx
00A2514B  0F 95 C0                        setne al
00A2514E  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A25152  45 33 ED                        xor r13d, r13d
00A25155  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
00A2515A  33 C0                           xor eax, eax
00A2515C  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A25161  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A2516A  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00A25171  90                              nop
00A25172  48 8D 0D C7 59 4D 00            lea rcx, [rip + 0x4d59c7]
00A25179  E8 A2 E5 9C FF                  call 0x1403f3720
00A2517E  BA 00 20 00 00                  mov edx, 0x2000
00A25183  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00A25187  41 8D 4D 40                     lea ecx, [r13 + 0x40]
00A2518B  41 B8 45 6E 76 72               mov r8d, 0x72766e45
00A25191  E8 5A CF 15 00                  call 0x140b820f0
00A25196  4C 8B F8                        mov r15, rax
00A25199  48 85 C0                        test rax, rax
00A2519C  75 05                           jne 0x140a251a3
00A2519E  44 21 6C 24 30                  and dword ptr [rsp + 0x30], r13d
00A251A3  8B 74 24 30                     mov esi, dword ptr [rsp + 0x30]
00A251A7  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00A251AC  4C 8B C0                        mov r8, rax
00A251AF  48 8D 15 1A 05 00 00            lea rdx, [rip + 0x51a]
00A251B6  B9 02 00 00 00                  mov ecx, 2
00A251BB  E8 6C 07 00 00                  call 0x140a2592c
00A251C0  8B F8                           mov edi, eax
00A251C2  B8 23 00 00 C0                  mov eax, 0xc0000023
00A251C7  3B F8                           cmp edi, eax
00A251C9  0F 84 3C 04 00 00               je 0x140a2560b
00A251CF  48 8D 0D 6A 59 4D 00            lea rcx, [rip + 0x4d596a]
00A251D6  E8 C5 B1 82 FF                  call 0x1402503a0
00A251DB  E8 D0 86 83 FF                  call 0x14025d8b0
00A251E0  85 FF                           test edi, edi
00A251E2  0F 85 D1 03 00 00               jne 0x140a255b9
00A251E8  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00A251EC  85 C0                           test eax, eax
00A251EE  0F 84 C5 03 00 00               je 0x140a255b9
00A251F4  4D 8B E7                        mov r12, r15
00A251F7  49 8D 34 47                     lea rsi, [r15 + rax*2]
00A251FB  48 89 B4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rsi
00A25203  48 8B 0D EE 4C 5F FF            mov rcx, qword ptr [rip - 0xa0b312]
00A2520A  48 8B 15 DF 4C 5F FF            mov rdx, qword ptr [rip - 0xa0b321]
00A25211  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
00A25216  49 8B 44 24 10                  mov rax, qword ptr [r12 + 0x10]
00A2521B  48 2B C2                        sub rax, rdx
00A2521E  75 08                           jne 0x140a25228
00A25220  49 8B 44 24 18                  mov rax, qword ptr [r12 + 0x18]
00A25225  48 2B C1                        sub rax, rcx
00A25228  48 85 C0                        test rax, rax
00A2522B  0F 85 A0 02 00 00               jne 0x140a254d1
00A25231  49 8D 4C 24 20                  lea rcx, [r12 + 0x20]
00A25236  48 8D 54 24 4C                  lea rdx, [rsp + 0x4c]
00A2523B  E8 D8 04 00 00                  call 0x140a25718
00A25240  85 C0                           test eax, eax
00A25242  0F 84 7B 02 00 00               je 0x140a254c3
00A25248  45 8B 6C 24 08                  mov r13d, dword ptr [r12 + 8]
00A2524D  41 83 FD 08                     cmp r13d, 8
00A25251  0F 82 6C 02 00 00               jb 0x140a254c3
00A25257  45 8B 44 24 04                  mov r8d, dword ptr [r12 + 4]
00A2525C  4D 03 C4                        add r8, r12
00A2525F  4C 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], r8
00A25267  45 0F B7 48 04                  movzx r9d, word ptr [r8 + 4]
00A2526C  49 8D 40 06                     lea rax, [r8 + 6]
00A25270  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00A25278  48 8B D6                        mov rdx, rsi
00A2527B  48 8B C8                        mov rcx, rax
00A2527E  E8 15 04 00 00                  call 0x140a25698
00A25283  8B F0                           mov esi, eax
00A25285  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
00A25289  83 F8 FF                        cmp eax, -1
00A2528C  74 0B                           je 0x140a25299
00A2528E  8D 34 45 02 00 00 00            lea esi, [rax*2 + 2]
00A25295  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
00A25299  8D 46 06                        lea eax, [rsi + 6]
00A2529C  41 03 C1                        add eax, r9d
00A2529F  83 FE FF                        cmp esi, -1
00A252A2  0F 84 1B 02 00 00               je 0x140a254c3
00A252A8  45 3B CD                        cmp r9d, r13d
00A252AB  0F 83 12 02 00 00               jae 0x140a254c3
00A252B1  44 3B E8                        cmp r13d, eax
00A252B4  0F 82 09 02 00 00               jb 0x140a254c3
00A252BA  C6 84 24 20 01 00 00 01         mov byte ptr [rsp + 0x120], 1
00A252C2  8B CE                           mov ecx, esi
00A252C4  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
00A252CC  48 8D 51 06                     lea rdx, [rcx + 6]
00A252D0  49 03 D0                        add rdx, r8
00A252D3  48 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdx
00A252DB  4D 8B C1                        mov r8, r9
00A252DE  4C 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r9
00A252E6  49 8D 0C 11                     lea rcx, [r9 + rdx]
00A252EA  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
00A252F2  44 2B E8                        sub r13d, eax
00A252F5  49 8D 46 03                     lea rax, [r14 + 3]
00A252F9  48 83 E0 FC                     and rax, 0xfffffffffffffffc
00A252FD  49 3B C6                        cmp rax, r14
00A25300  0F 85 8C 02 00 00               jne 0x140a25592
00A25306  41 8D 49 0C                     lea ecx, [r9 + 0xc]
00A2530A  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00A2530E  49 8D 76 04                     lea rsi, [r14 + 4]
00A25312  3B D9                           cmp ebx, ecx
00A25314  0F 82 19 03 00 00               jb 0x140a25633
00A2531A  41 C7 06 01 00 00 00            mov dword ptr [r14], 1
00A25321  89 0E                           mov dword ptr [rsi], ecx
00A25323  41 C7 46 08 04 00 00 00         mov dword ptr [r14 + 8], 4
00A2532B  49 8D 4E 0C                     lea rcx, [r14 + 0xc]
00A2532F  E8 0C 15 CA FF                  call 0x1406c6840
00A25334  48 8B C6                        mov rax, rsi
00A25337  8B 10                           mov edx, dword ptr [rax]
00A25339  49 03 D6                        add rdx, r14
00A2533C  49 8B CE                        mov rcx, r14
00A2533F  E8 AC 04 00 00                  call 0x140a257f0
00A25344  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
00A25349  85 C0                           test eax, eax
00A2534B  0F 88 F4 02 00 00               js 0x140a25645
00A25351  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
00A25355  41 8D 55 1F                     lea edx, [r13 + 0x1f]
00A25359  41 B9 FC FF FF FF               mov r9d, 0xfffffffc
00A2535F  41 23 D1                        and edx, r9d
00A25362  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00A25366  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
00A2536A  83 C0 03                        add eax, 3
00A2536D  03 D0                           add edx, eax
00A2536F  41 23 D1                        and edx, r9d
00A25372  89 54 24 3C                     mov dword ptr [rsp + 0x3c], edx
00A25376  03 D1                           add edx, ecx
00A25378  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
00A2537C  83 C2 04                        add edx, 4
00A2537F  89 54 24 58                     mov dword ptr [rsp + 0x58], edx
00A25383  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00A25387  3B DA                           cmp ebx, edx
00A25389  B9 23 00 00 C0                  mov ecx, 0xc0000023
00A2538E  0F 42 C1                        cmovb eax, ecx
00A25391  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00A25395  33 C0                           xor eax, eax
00A25397  3B DA                           cmp ebx, edx
00A25399  41 0F 43 C0                     cmovae eax, r8d
00A2539D  44 8B C0                        mov r8d, eax
00A253A0  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A253A4  8B CB                           mov ecx, ebx
00A253A6  8B C3                           mov eax, ebx
00A253A8  2B C2                           sub eax, edx
00A253AA  33 DB                           xor ebx, ebx
00A253AC  3B CA                           cmp ecx, edx
00A253AE  0F 43 D8                        cmovae ebx, eax
00A253B1  45 85 C0                        test r8d, r8d
00A253B4  0F 84 04 01 00 00               je 0x140a254be
00A253BA  44 8B C2                        mov r8d, edx
00A253BD  33 D2                           xor edx, edx
00A253BF  49 8B CE                        mov rcx, r14
00A253C2  E8 79 18 CA FF                  call 0x1406c6c40
00A253C7  41 B8 01 00 00 00               mov r8d, 1
00A253CD  44 89 06                        mov dword ptr [rsi], r8d
00A253D0  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00A253D4  89 46 04                        mov dword ptr [rsi + 4], eax
00A253D7  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
00A253DB  89 46 08                        mov dword ptr [rsi + 8], eax
00A253DE  83 66 0C 00                     and dword ptr [rsi + 0xc], 0
00A253E2  33 D2                           xor edx, edx
00A253E4  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00A253EC  8B 01                           mov eax, dword ptr [rcx]
00A253EE  41 84 C0                        test r8b, al
00A253F1  0F 85 64 02 00 00               jne 0x140a2565b
00A253F7  8B 01                           mov eax, dword ptr [rcx]
00A253F9  A8 08                           test al, 8
00A253FB  0F 85 66 02 00 00               jne 0x140a25667
00A25401  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00A25405  89 46 10                        mov dword ptr [rsi + 0x10], eax
00A25408  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
00A2540C  89 46 14                        mov dword ptr [rsi + 0x14], eax
00A2540F  44 89 6E 18                     mov dword ptr [rsi + 0x18], r13d
00A25413  48 8D 4E 1C                     lea rcx, [rsi + 0x1c]
00A25417  45 8B C5                        mov r8d, r13d
00A2541A  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00A25422  E8 19 14 CA FF                  call 0x1406c6840
00A25427  41 83 FD 14                     cmp r13d, 0x14
00A2542B  0F 87 2C 01 00 00               ja 0x140a2555d
00A25431  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
00A25435  48 03 CE                        add rcx, rsi
00A25438  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
00A25440  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
00A25448  E8 F3 13 CA FF                  call 0x1406c6840
00A2544D  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
00A25451  48 03 C6                        add rax, rsi
00A25454  C7 00 01 00 00 00               mov dword ptr [rax], 1
00A2545A  8B 54 24 48                     mov edx, dword ptr [rsp + 0x48]
00A2545E  89 50 04                        mov dword ptr [rax + 4], edx
00A25461  C7 40 08 04 00 00 00            mov dword ptr [rax + 8], 4
00A25468  48 8D 48 0C                     lea rcx, [rax + 0xc]
00A2546C  80 BC 24 20 01 00 00 00         cmp byte ptr [rsp + 0x120], 0
00A25474  0F 84 CD 00 00 00               je 0x140a25547
00A2547A  4C 8B 84 24 A0 00 00 00         mov r8, qword ptr [rsp + 0xa0]
00A25482  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
00A2548A  E8 B1 13 CA FF                  call 0x1406c6840
00A2548F  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00A25497  E8 E4 03 A8 FF                  call 0x1404a5880
00A2549C  85 C0                           test eax, eax
00A2549E  0F 85 CE 01 00 00               jne 0x140a25672
00A254A4  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00A254A9  48 85 C9                        test rcx, rcx
00A254AC  74 07                           je 0x140a254b5
00A254AE  41 8B C6                        mov eax, r14d
00A254B1  2B C1                           sub eax, ecx
00A254B3  89 01                           mov dword ptr [rcx], eax
00A254B5  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
00A254BA  8B 54 24 58                     mov edx, dword ptr [rsp + 0x58]
00A254BE  8B C2                           mov eax, edx
00A254C0  4C 03 F0                        add r14, rax
00A254C3  48 8B 15 26 4A 5F FF            mov rdx, qword ptr [rip - 0xa0b5da]
00A254CA  48 8B 0D 27 4A 5F FF            mov rcx, qword ptr [rip - 0xa0b5d9]
00A254D1  41 8B 04 24                     mov eax, dword ptr [r12]
00A254D5  85 C0                           test eax, eax
00A254D7  74 10                           je 0x140a254e9
00A254D9  4C 03 E0                        add r12, rax
00A254DC  48 8B B4 24 B0 00 00 00         mov rsi, qword ptr [rsp + 0xb0]
00A254E4  E9 28 FD FF FF                  jmp 0x140a25211
00A254E9  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00A254EE  4C 8B A4 24 18 01 00 00         mov r12, qword ptr [rsp + 0x118]
00A254F6  44 8B 6C 24 38                  mov r13d, dword ptr [rsp + 0x38]
00A254FB  48 85 C0                        test rax, rax
00A254FE  74 03                           je 0x140a25503
00A25500  83 20 00                        and dword ptr [rax], 0
00A25503  4D 85 FF                        test r15, r15
00A25506  74 0A                           je 0x140a25512
00A25508  33 D2                           xor edx, edx
00A2550A  49 8B CF                        mov rcx, r15
00A2550D  E8 5E D3 15 00                  call 0x140b82870
00A25512  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00A25517  48 85 C9                        test rcx, rcx
00A2551A  0F 85 5B 01 00 00               jne 0x140a2567b
00A25520  85 FF                           test edi, edi
00A25522  41 0F 49 FD                     cmovns edi, r13d
00A25526  44 2B 74 24 70                  sub r14d, dword ptr [rsp + 0x70]
00A2552B  45 89 34 24                     mov dword ptr [r12], r14d
00A2552F  8B C7                           mov eax, edi
00A25531  EB 00                           jmp 0x140a25533
00A25533  48 81 C4 D0 00 00 00            add rsp, 0xd0
00A2553A  41 5F                           pop r15
00A2553C  41 5E                           pop r14
00A2553E  41 5D                           pop r13
00A25540  41 5C                           pop r12
00A25542  5F                              pop rdi
00A25543  5E                              pop rsi
00A25544  5B                              pop rbx
00A25545  C3                              ret
00A25546  CC                              int3
00A25547  83 4E 0C 20                     or dword ptr [rsi + 0xc], 0x20
00A2554B  C6 01 7F                        mov byte ptr [rcx], 0x7f
00A2554E  66 C7 40 0D FF 04               mov word ptr [rax + 0xd], 0x4ff
00A25554  C6 40 0F 00                     mov byte ptr [rax + 0xf], 0
00A25558  E9 47 FF FF FF                  jmp 0x140a254a4
00A2555D  48 8D 15 CC 31 0E 00            lea rdx, [rip + 0xe31cc]
00A25564  48 8D 4E 1C                     lea rcx, [rsi + 0x1c]
00A25568  E8 93 1A CA FF                  call 0x1406c7000
00A2556D  85 C0                           test eax, eax
00A2556F  0F 85 BC FE FF FF               jne 0x140a25431
00A25575  41 8B D5                        mov edx, r13d
00A25578  48 8D 4E 1C                     lea rcx, [rsi + 0x1c]
00A2557C  E8 57 F7 FF FF                  call 0x140a24cd8
00A25581  85 C0                           test eax, eax
00A25583  0F 88 A8 FE FF FF               js 0x140a25431
00A25589  83 4E 0C 04                     or dword ptr [rsi + 0xc], 4
00A2558D  E9 9F FE FF FF                  jmp 0x140a25431
00A25592  8B C8                           mov ecx, eax
00A25594  41 2B CE                        sub ecx, r14d
00A25597  4C 8B F0                        mov r14, rax
00A2559A  3B D9                           cmp ebx, ecx
00A2559C  73 14                           jae 0x140a255b2
00A2559E  83 64 24 40 00                  and dword ptr [rsp + 0x40], 0
00A255A3  33 DB                           xor ebx, ebx
00A255A5  C7 44 24 38 23 00 00 C0         mov dword ptr [rsp + 0x38], 0xc0000023
00A255AD  E9 54 FD FF FF                  jmp 0x140a25306
00A255B2  2B D9                           sub ebx, ecx
00A255B4  E9 4D FD FF FF                  jmp 0x140a25306
00A255B9  B8 06 02 00 C0                  mov eax, 0xc0000206
00A255BE  B9 23 00 00 C0                  mov ecx, 0xc0000023
00A255C3  3B F9                           cmp edi, ecx
00A255C5  0F 44 F8                        cmove edi, eax
00A255C8  E9 36 FF FF FF                  jmp 0x140a25503
00A255CD  B8 0D 00 00 C0                  mov eax, 0xc000000d
00A255D2  E9 5C FF FF FF                  jmp 0x140a25533
00A255D7  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00A255DC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A255E1  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00A255E6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A255EB  41 B9 01 00 00 00               mov r9d, 1
00A255F1  44 8A C6                        mov r8b, sil
00A255F4  8B D3                           mov edx, ebx
00A255F6  48 8B CF                        mov rcx, rdi
00A255F9  E8 BA DD F2 FF                  call 0x1409533b8
00A255FE  85 C0                           test eax, eax
00A25600  0F 88 2D FF FF FF               js 0x140a25533
00A25606  E9 37 FB FF FF                  jmp 0x140a25142
00A2560B  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00A2560F  3B F0                           cmp esi, eax
00A25611  0F 83 B8 FB FF FF               jae 0x140a251cf
00A25617  4D 85 FF                        test r15, r15
00A2561A  0F 84 F2 26 11 00               je 0x140b37d12
00A25620  33 D2                           xor edx, edx
00A25622  49 8B CF                        mov rcx, r15
00A25625  E8 46 D2 15 00                  call 0x140b82870
00A2562A  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00A2562E  E9 DF 26 11 00                  jmp 0x140b37d12
00A25633  33 DB                           xor ebx, ebx
00A25635  45 33 C0                        xor r8d, r8d
00A25638  C7 44 24 38 23 00 00 C0         mov dword ptr [rsp + 0x38], 0xc0000023
00A25640  E9 10 FD FF FF                  jmp 0x140a25355
00A25645  C6 84 24 20 01 00 00 00         mov byte ptr [rsp + 0x120], 0
00A2564D  B9 10 00 00 00                  mov ecx, 0x10
00A25652  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00A25656  E9 FA FC FF FF                  jmp 0x140a25355
00A2565B  44 89 46 0C                     mov dword ptr [rsi + 0xc], r8d
00A2565F  41 8B D0                        mov edx, r8d
00A25662  E9 90 FD FF FF                  jmp 0x140a253f7
00A25667  83 CA 10                        or edx, 0x10
00A2566A  89 56 0C                        mov dword ptr [rsi + 0xc], edx
00A2566D  E9 8F FD FF FF                  jmp 0x140a25401
00A25672  83 4E 0C 08                     or dword ptr [rsi + 0xc], 8
00A25676  E9 29 FE FF FF                  jmp 0x140a254a4
00A2567B  E8 D8 9B 87 FF                  call 0x14029f258
00A25680  E9 9B FE FF FF                  jmp 0x140a25520
00A25685  B8 02 00 00 C0                  mov eax, 0xc0000002
00A2568A  E9 A4 FE FF FF                  jmp 0x140a25533
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtEnumerateBootEntries(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
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
    unsigned int v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int8 v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p120;
    unsigned __int8 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (208);
    if ((*(unsigned int *)(v_rip + 5087200)) != 2) goto loc_00A25685;
    result = (a1) & (-4);
    if (result != a1) goto loc_00A255CD;
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A25685;
    v_stack_m40 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_mD4 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_00A250CD;
    v_stack_mC4 = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    result = -(a1);
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2)))));
    v_stack_mC4 = (unsigned int)(v_rbx);
    goto loc_00A25133;
loc_00A250CD:
    a1 = (unsigned int)(*(unsigned int *)(a2));
    if (a2 < ((unsigned int)(*(unsigned int *)(a2)))) { a1 = a2; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_mC4 = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    result = -(a1);
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2)))));
    v_stack_mC4 = (unsigned int)(v_rbx);
    if (!(condition_is_equal)) {
        a2 = (unsigned int)(v_rbx);
        a3 = 4;
        a1 = a1;
        result = ProbeForWrite(a1, a2, a3, a4);
    }
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5982623), (unsigned __int8)(v_stack_mD4), a3, a4);
    v_stack_p20 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) goto loc_00A25133;
    goto loc_00A25533;
loc_00A25133:
    goto loc_00A2513A;
loc_00A2513A:
    if ((unsigned int)(v_rbx) != 0) goto loc_00A255D7;
loc_00A25142:
    result = 0;
    result = ((unsigned int)(v_rbx) != 0) ? 1 : 0;
    v_stack_mC8 = (unsigned int)(result);
    v_r13 = 0;
    v_stack_mD0 = 0;
    result = 0;
    v_stack_mA0 = 0;
    result = ExAcquireFastMutexUnsafe(v_rip + 5069255, (unsigned __int8)(v_stack_mD4), a3, a4);
    v_stack_mD8 = (unsigned int)((unsigned int)(0x2000ULL));
    result = ExAllocatePool2(v_r13 + 64, (unsigned int)(0x2000ULL), (unsigned int)(0x72766E45ULL), a4);
    if (result == 0) {
    }
    result = IoEnumerateEnvironmentVariablesEx(2, v_rip + 1306, result, v_stack_mD8);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_00A2560B;
loc_00A251CF:
    result = ExReleaseFastMutexUnsafe(v_rip + 5069162, v_rip + 1306, result, v_stack_mD8);
    result = KeLeaveCriticalRegion(v_rip + 5069162, v_rip + 1306, result, v_stack_mD8);
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_00A255B9;
    if ((unsigned int)((unsigned int)(v_stack_mD8)) == 0) goto loc_00A255B9;
    v_stack_m58 = result + (unsigned int)(v_stack_mD8) * 2;
loc_00A25211:
    result = (*(unsigned __int64 *)(result + 16)) - (*(unsigned __int64 *)(v_rip - 10531617));
    if (!(condition_is_not_equal)) {
        result = *(unsigned __int64 *)(result + 24);
        result = (result) - (*(unsigned __int64 *)(v_rip - 10531602));
    }
    if (result != 0) goto loc_00A254D1;
    result = ExpTranslateBootEntryNameToId(result + 32, v_stack_mBC, result, v_stack_mD8);
    if ((unsigned int)(result) == 0) goto loc_00A254C3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))) < 8) goto loc_00A254C3;
    a3 = ((unsigned int)(*(unsigned int *)(result + 4))) + (result);
    v_stack_m88 = a3;
    v_stack_m70 = a3 + 6;
    result = ExpSafeWcslen(a3 + 6, result + (unsigned int)(v_stack_mD8) * 2, a3, *(unsigned __int16 *)(a3 + 4));
    v_stack_mCC = (unsigned int)(result);
    v_rsi = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) != -1) {
        v_rsi = result * 2 + 2;
        v_stack_mCC = (unsigned int)(v_rsi);
    }
    result = (unsigned int)((v_rsi + 6) + ((unsigned int)(*(unsigned __int16 *)(a3 + 4))));
    if (((unsigned int)(v_rsi)) == -1) goto loc_00A254C3;
    if (((unsigned int)(*(unsigned __int16 *)(a3 + 4))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(result + 8))))) goto loc_00A254C3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))) < ((unsigned int)(result))) goto loc_00A254C3;
    v_stack_p18 = 1;
    v_stack_m78 = (unsigned int)((unsigned int)(v_rsi));
    a2 = ((unsigned int)((unsigned int)(v_rsi)) + 6) + (a3);
    v_stack_m60 = a2;
    v_stack_m68 = *(unsigned __int16 *)(a3 + 4);
    v_stack_m80 = *(unsigned __int16 *)(a3 + 4) + a2 * 1;
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 8))) - ((unsigned int)(result)));
    result = (v_stack_m98 + 3) & (-4);
    if (result != v_stack_m98) goto loc_00A25592;
loc_00A25306:
    v_stack_mC0 = (unsigned int)(*(unsigned __int16 *)(a3 + 4) + 12);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int16 *)(a3 + 4) + 12))) goto loc_00A25633;
    *(unsigned int *)(v_stack_m98) = 1;
    *(unsigned int *)(v_stack_m98 + 4) = (unsigned int)(*(unsigned __int16 *)(a3 + 4) + 12);
    *(unsigned int *)(v_stack_m98 + 8) = 4;
    result = memcpy(v_stack_m98 + 12, a2, *(unsigned __int16 *)(a3 + 4), *(unsigned __int16 *)(a3 + 4));
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_m98 + 4))) + (v_stack_m98);
    result = ExpVerifyFilePath(v_stack_m98, a2, *(unsigned __int16 *)(a3 + 4), *(unsigned __int16 *)(a3 + 4));
    if (sign_flag) goto loc_00A25645;
loc_00A25355:
    a2 = (unsigned int)((v_r13 + 31) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    v_stack_mB8 = (unsigned int)(a2);
    result = (unsigned int)(((unsigned int)(v_stack_mCC)) + (3));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    a2 = (unsigned int)((a2) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    v_stack_mCC = (unsigned int)(a2);
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(v_stack_mC0))));
    v_stack_mA8 = (unsigned int)(a2);
    a2 = (unsigned int)((a2) + (4));
    v_stack_mB0 = (unsigned int)(a2);
    result = (unsigned int)(v_stack_mD0);
    if (((unsigned int)(v_rbx)) < ((unsigned int)(a2))) { result = (unsigned int)((unsigned int)(0xC0000023ULL)); }
    v_stack_mD0 = (unsigned int)(result);
    result = 0;
    if (((unsigned int)(v_rbx)) >= ((unsigned int)(a2))) { result = (unsigned int)((unsigned int)(v_stack_mC8)); }
    v_stack_mC8 = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(a2)));
    v_rbx = 0;
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbx)))) >= ((unsigned int)(a2))) { v_rbx = (unsigned int)(result); }
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00A254BE;
    a2 = 0;
    result = memset(v_stack_m98, a2, (unsigned int)((unsigned int)(a2)), (unsigned int)(0xFFFFFFFCULL));
    *(unsigned int *)(v_stack_m98 + 4) = 1;
    *(unsigned int *)(v_stack_m98 + 4 + 4) = (unsigned int)((unsigned int)(v_stack_mA8));
    *(unsigned int *)(v_stack_m98 + 4 + 8) = (unsigned int)((unsigned int)(v_stack_mBC));
    a2 = 0;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m88))))) != 0) goto loc_00A2565B;
loc_00A253F7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m88)))) & (8)) != 0) goto loc_00A25667;
loc_00A25401:
    *(unsigned int *)(v_stack_m98 + 4 + 16) = (unsigned int)((unsigned int)(v_stack_mB8));
    *(unsigned int *)(v_stack_m98 + 4 + 20) = (unsigned int)((unsigned int)(v_stack_mCC));
    *(unsigned int *)(v_stack_m98 + 4 + 24) = (unsigned int)(v_r13);
    result = memcpy(v_stack_m98 + 4 + 28, v_stack_m80, (unsigned int)((unsigned int)(v_r13)), (unsigned int)(0xFFFFFFFCULL));
    if (((unsigned int)(v_r13)) > 20) goto loc_00A2555D;
loc_00A25431:
    a1 = ((unsigned int)(v_stack_mB8)) + (v_stack_m98 + 4);
    result = memcpy(a1, v_stack_m70, v_stack_m78, (unsigned int)(0xFFFFFFFCULL));
    result = ((unsigned int)(v_stack_mCC)) + (v_stack_m98 + 4);
    *(unsigned int *)(result) = 1;
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)(v_stack_mC0));
    *(unsigned int *)(result + 8) = 4;
    if (v_stack_p18 == 0) goto loc_00A25547;
    result = memcpy(result + 12, v_stack_m60, v_stack_m68, (unsigned int)(0xFFFFFFFCULL));
    result = ExpIsDevicePathForRemovableMedia(v_stack_m60, v_stack_m60, v_stack_m68, (unsigned int)(0xFFFFFFFCULL));
    if ((unsigned int)(result) != 0) goto loc_00A25672;
loc_00A254A4:
    if (v_stack_mA0 != 0) {
        result = (unsigned int)(v_stack_m98);
        result = (unsigned int)((result) - ((unsigned int)(v_stack_mA0)));
        *(unsigned int *)(v_stack_mA0) = (unsigned int)(result);
    }
    v_stack_mA0 = v_stack_m98;
loc_00A254BE:
    v_r14 = (v_stack_m98) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_mB0))));
loc_00A254C3:
loc_00A254D1:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result))) == 0) goto loc_00A254E9;
    v_r12 = (result) + ((unsigned int)(*(unsigned int *)(result)));
    goto loc_00A25211;
loc_00A254E9:
    if (v_stack_mA0 != 0) {
    }
    result = v_stack_mA0;
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, v_stack_m68, (unsigned int)(0xFFFFFFFCULL));
    }
    if (v_stack_m90 != 0) goto loc_00A2567B;
loc_00A25520:
    v_rdi = (unsigned int)((unsigned int)(result));
    if (!sign_flag) { v_rdi = (unsigned int)((unsigned int)(v_stack_mD0)); }
    v_r14 = (unsigned int)((v_r14) - (v_stack_m98));
    *(unsigned int *)(v_stack_p10) = (unsigned int)(v_r14);
    goto loc_00A25533;
loc_00A25533:
    v_rsp = (v_rsp) + (208);
    return (unsigned int)((unsigned int)(v_rdi));
loc_00A25547:
    *(unsigned __int8 *)(v_stack_m90) = 127;
    *(unsigned __int16 *)((unsigned int)((unsigned int)(v_rdi)) + 13) = 0x4FFULL;
    *(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + 15) = 0;
    goto loc_00A254A4;
loc_00A2555D:
    result = strcmp(v_stack_m58 + 28, v_rip + 930252, v_stack_m68, (unsigned int)(0xFFFFFFFCULL));
    if ((unsigned int)(result) != 0) goto loc_00A25431;
    result = ExpVerifyWindowsOsOptions(v_stack_m58 + 28, (unsigned int)((unsigned int)((unsigned int)(v_stack_mD0))), v_stack_m68, (unsigned int)(0xFFFFFFFCULL));
    if (sign_flag) goto loc_00A25431;
    goto loc_00A25431;
loc_00A25592:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) - ((unsigned int)(v_r14)));
    if (((unsigned int)(v_rbx)) >= ((unsigned int)(a1))) goto loc_00A255B2;
    v_rbx = 0;
    v_stack_p38 = 0xC0000023ULL;
    goto loc_00A25306;
loc_00A255B2:
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(a1)));
    goto loc_00A25306;
loc_00A255B9:
    if (((unsigned int)(v_rdi)) == ((unsigned int)((unsigned int)(0xC0000023ULL)))) { v_rdi = (unsigned int)((unsigned int)(0xC0000206ULL)); }
    goto loc_00A25503;
loc_00A255CD:
    goto loc_00A25533;
loc_00A255D7:
    v_stack_p28 = v_stack_p78;
    v_stack_p20 = v_stack_p70;
    result = ExLockUserBuffer(v_rdi, (unsigned int)((unsigned int)(v_rbx)), (unsigned __int8)(v_stack_m58), 1);
    if (sign_flag) goto loc_00A25533;
    goto loc_00A25142;
loc_00A2560B:
    if (((unsigned int)(v_stack_m58)) >= ((unsigned int)((unsigned int)(v_stack_p30)))) goto loc_00A251CF;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned __int8)(v_stack_m58), 1);
loc_00A25633:
    v_rbx = 0;
    a3 = 0;
    v_stack_p38 = 0xC0000023ULL;
    goto loc_00A25355;
loc_00A25645:
    v_stack_p120 = 0;
    v_stack_p48 = 16;
    goto loc_00A25355;
loc_00A2565B:
    *(unsigned int *)(v_stack_m58 + 12) = 0;
    goto loc_00A253F7;
loc_00A25667:
    a2 = (unsigned int)((0) | (16));
    *(unsigned int *)(v_stack_m58 + 12) = (unsigned int)(a2);
    goto loc_00A25401;
loc_00A25672:
    goto loc_00A254A4;
loc_00A2567B:
    result = ExUnlockUserBuffer(16, a2, a3, 1);
    goto loc_00A25520;
loc_00A25685:
    goto loc_00A25533;
}
```

## 5. (Beta) C Style

```c
int64_t NtEnumerateBootEntries(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
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
    uint32_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint8_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_p10;
    uint8_t v_stack_p120;
    uint8_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (208);
    if ((*(uint32_t *)(v_rip + 0x4D9FE0)) != 2) goto loc_00A25685;
    result = (Arg1) & (-4);
    if (result != Arg1) goto loc_00A255CD;
    result = PsIsCurrentThreadInServerSilo(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00A25685;
    v_stack_m40 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_mD4 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_00A250CD;
    v_stack_mC4 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    result = -(Arg1);
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))));
    v_stack_mC4 = (uint32_t)(local_rbx);
    goto loc_00A25133;
loc_00A250CD:
    Arg1 = (uint32_t)(*(uint32_t *)(arg2));
    if (Arg2 < ((uint32_t)(*(uint32_t *)(arg2)))) { Arg1 = Arg2; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    v_stack_mC4 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    result = -(Arg1);
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg2)))));
    v_stack_mC4 = (uint32_t)(local_rbx);
    if (!(condition_is_equal)) {
        Arg2 = (uint32_t)(local_rbx);
        a3 = 4;
        Arg1 = Arg1;
        result = ProbeForWrite(Arg1, Arg2, a3, a4);
    }
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x5B499F), (uint8_t)(v_stack_mD4), a3, a4);
    v_stack_p20 = (uint8_t)(result);
    if ((uint8_t)(result) != 0) goto loc_00A25133;
    goto loc_00A25533;
loc_00A25133:
    goto loc_00A2513A;
loc_00A2513A:
    if ((uint32_t)(local_rbx) != 0) goto loc_00A255D7;
loc_00A25142:
    result = 0;
    result = ((uint32_t)(local_rbx) != 0) ? 1 : 0;
    v_stack_mC8 = (uint32_t)(result);
    local_r13 = 0;
    v_stack_mD0 = 0;
    result = 0;
    v_stack_mA0 = 0;
    result = ExAcquireFastMutexUnsafe(v_rip + 5069255, (uint8_t)(v_stack_mD4), a3, a4);
    v_stack_mD8 = (uint32_t)((uint32_t)(0x2000ULL));
    result = ExAllocatePool2(local_r13 + 64, (uint32_t)(0x2000ULL), (uint32_t)(0x72766E45ULL), a4);
    if (result == 0) {
    }
    result = IoEnumerateEnvironmentVariablesEx(2, v_rip + 1306, result, v_stack_mD8);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_00A2560B;
loc_00A251CF:
    result = ExReleaseFastMutexUnsafe(v_rip + 5069162, v_rip + 1306, result, v_stack_mD8);
    result = KeLeaveCriticalRegion(v_rip + 5069162, v_rip + 1306, result, v_stack_mD8);
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_00A255B9;
    if ((uint32_t)((uint32_t)(v_stack_mD8)) == 0) goto loc_00A255B9;
    v_stack_m58 = result + (uint32_t)(v_stack_mD8) * 2;
loc_00A25211:
    result = (*(uint64_t *)(result + 0x10)) - (*(uint64_t *)(v_rip - 0xA0B321));
    if (!(condition_is_not_equal)) {
        result = *(uint64_t *)(result + 0x18);
        result = (result) - (*(uint64_t *)(v_rip - 0xA0B312));
    }
    if (result != 0) goto loc_00A254D1;
    result = ExpTranslateBootEntryNameToId(result + 32, v_stack_mBC, result, v_stack_mD8);
    if ((uint32_t)(result) == 0) goto loc_00A254C3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))) < 8) goto loc_00A254C3;
    a3 = ((uint32_t)(*(uint32_t *)(result + 0x4))) + (result);
    v_stack_m88 = a3;
    v_stack_m70 = a3 + 6;
    result = ExpSafeWcslen(a3 + 6, result + (uint32_t)(v_stack_mD8) * 2, a3, *(uint16_t *)(a3 + 0x4));
    v_stack_mCC = (uint32_t)(result);
    local_rsi = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) != -1) {
        local_rsi = result * 2 + 2;
        v_stack_mCC = (uint32_t)(local_rsi);
    }
    result = (uint32_t)((local_rsi + 6) + ((uint32_t)(*(uint16_t *)(a3 + 0x4))));
    if (((uint32_t)(local_rsi)) == -1) goto loc_00A254C3;
    if (((uint32_t)(*(uint16_t *)(a3 + 0x4))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8))))) goto loc_00A254C3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))) < ((uint32_t)(result))) goto loc_00A254C3;
    v_stack_p18 = 1;
    v_stack_m78 = (uint32_t)((uint32_t)(local_rsi));
    Arg2 = ((uint32_t)((uint32_t)(local_rsi)) + 6) + (a3);
    v_stack_m60 = Arg2;
    v_stack_m68 = *(uint16_t *)(a3 + 0x4);
    v_stack_m80 = *(uint16_t *)(a3 + 0x4) + Arg2 * 1;
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x8))) - ((uint32_t)(result)));
    result = (v_stack_m98 + 3) & (-4);
    if (result != v_stack_m98) goto loc_00A25592;
loc_00A25306:
    v_stack_mC0 = (uint32_t)(*(uint16_t *)(a3 + 0x4) + 12);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint16_t *)(a3 + 0x4) + 12))) goto loc_00A25633;
    *(uint32_t *)(v_stack_m98) = 1;
    *(uint32_t *)(v_stack_m98 + 0x4) = (uint32_t)(*(uint16_t *)(a3 + 0x4) + 12);
    *(uint32_t *)(v_stack_m98 + 0x8) = 4;
    result = memcpy(v_stack_m98 + 12, Arg2, *(uint16_t *)(a3 + 0x4), *(uint16_t *)(a3 + 0x4));
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_m98 + 0x4))) + (v_stack_m98);
    result = ExpVerifyFilePath(v_stack_m98, Arg2, *(uint16_t *)(a3 + 0x4), *(uint16_t *)(a3 + 0x4));
    if (sign_flag) goto loc_00A25645;
loc_00A25355:
    Arg2 = (uint32_t)((local_r13 + 31) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    v_stack_mB8 = (uint32_t)(Arg2);
    result = (uint32_t)(((uint32_t)(v_stack_mCC)) + (3));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    v_stack_mCC = (uint32_t)(Arg2);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(v_stack_mC0))));
    v_stack_mA8 = (uint32_t)(Arg2);
    Arg2 = (uint32_t)((Arg2) + (4));
    v_stack_mB0 = (uint32_t)(Arg2);
    result = (uint32_t)(v_stack_mD0);
    if (((uint32_t)(local_rbx)) < ((uint32_t)(Arg2))) { result = (uint32_t)((uint32_t)(0xC0000023ULL)); }
    v_stack_mD0 = (uint32_t)(result);
    result = 0;
    if (((uint32_t)(local_rbx)) >= ((uint32_t)(Arg2))) { result = (uint32_t)((uint32_t)(v_stack_mC8)); }
    v_stack_mC8 = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(Arg2)));
    local_rbx = 0;
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbx)))) >= ((uint32_t)(Arg2))) { local_rbx = (uint32_t)(result); }
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00A254BE;
    Arg2 = 0;
    result = memset(v_stack_m98, Arg2, (uint32_t)((uint32_t)(Arg2)), (uint32_t)(0xFFFFFFFCULL));
    *(uint32_t *)(v_stack_m98 + 0x4) = 1;
    *(uint32_t *)(v_stack_m98 + 0x4 + 0x4) = (uint32_t)((uint32_t)(v_stack_mA8));
    *(uint32_t *)(v_stack_m98 + 0x4 + 0x8) = (uint32_t)((uint32_t)(v_stack_mBC));
    Arg2 = 0;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m88))))) != 0) goto loc_00A2565B;
loc_00A253F7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m88)))) & (8)) != 0) goto loc_00A25667;
loc_00A25401:
    *(uint32_t *)(v_stack_m98 + 0x4 + 0x10) = (uint32_t)((uint32_t)(v_stack_mB8));
    *(uint32_t *)(v_stack_m98 + 0x4 + 0x14) = (uint32_t)((uint32_t)(v_stack_mCC));
    *(uint32_t *)(v_stack_m98 + 0x4 + 0x18) = (uint32_t)(local_r13);
    result = memcpy(v_stack_m98 + 4 + 28, v_stack_m80, (uint32_t)((uint32_t)(local_r13)), (uint32_t)(0xFFFFFFFCULL));
    if (((uint32_t)(local_r13)) > 20) goto loc_00A2555D;
loc_00A25431:
    Arg1 = ((uint32_t)(v_stack_mB8)) + (v_stack_m98 + 4);
    result = memcpy(Arg1, v_stack_m70, v_stack_m78, (uint32_t)(0xFFFFFFFCULL));
    result = ((uint32_t)(v_stack_mCC)) + (v_stack_m98 + 4);
    *(uint32_t *)(result) = 1;
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)(v_stack_mC0));
    *(uint32_t *)(result + 0x8) = 4;
    if (v_stack_p18 == 0) goto loc_00A25547;
    result = memcpy(result + 12, v_stack_m60, v_stack_m68, (uint32_t)(0xFFFFFFFCULL));
    result = ExpIsDevicePathForRemovableMedia(v_stack_m60, v_stack_m60, v_stack_m68, (uint32_t)(0xFFFFFFFCULL));
    if ((uint32_t)(result) != 0) goto loc_00A25672;
loc_00A254A4:
    if (v_stack_mA0 != 0) {
        result = (uint32_t)(v_stack_m98);
        result = (uint32_t)((result) - ((uint32_t)(v_stack_mA0)));
        *(uint32_t *)(v_stack_mA0) = (uint32_t)(result);
    }
    v_stack_mA0 = v_stack_m98;
loc_00A254BE:
    local_r14 = (v_stack_m98) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_mB0))));
loc_00A254C3:
loc_00A254D1:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result))) == 0) goto loc_00A254E9;
    local_r12 = (result) + ((uint32_t)(*(uint32_t *)(result)));
    goto loc_00A25211;
loc_00A254E9:
    if (v_stack_mA0 != 0) {
    }
    result = v_stack_mA0;
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m68, (uint32_t)(0xFFFFFFFCULL));
    }
    if (v_stack_m90 != 0) goto loc_00A2567B;
loc_00A25520:
    local_rdi = (uint32_t)((uint32_t)(result));
    if (!sign_flag) { local_rdi = (uint32_t)((uint32_t)(v_stack_mD0)); }
    local_r14 = (uint32_t)((local_r14) - (v_stack_m98));
    *(uint32_t *)(v_stack_p10) = (uint32_t)(local_r14);
    goto loc_00A25533;
loc_00A25533:
    local_rsp = (local_rsp) + (208);
    return (uint32_t)((uint32_t)(local_rdi));
loc_00A25547:
    *(uint8_t *)(v_stack_m90) = 127;
    *(uint16_t *)((uint32_t)((uint32_t)(local_rdi)) + 0xD) = 0x4FFULL;
    *(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + 0xF) = 0;
    goto loc_00A254A4;
loc_00A2555D:
    result = strcmp(v_stack_m58 + 28, v_rip + 930252, v_stack_m68, (uint32_t)(0xFFFFFFFCULL));
    if ((uint32_t)(result) != 0) goto loc_00A25431;
    result = ExpVerifyWindowsOsOptions(v_stack_m58 + 28, (uint32_t)((uint32_t)((uint32_t)(v_stack_mD0))), v_stack_m68, (uint32_t)(0xFFFFFFFCULL));
    if (sign_flag) goto loc_00A25431;
    goto loc_00A25431;
loc_00A25592:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) - ((uint32_t)(local_r14)));
    if (((uint32_t)(local_rbx)) >= ((uint32_t)(Arg1))) goto loc_00A255B2;
    local_rbx = 0;
    v_stack_p38 = 0xC0000023ULL;
    goto loc_00A25306;
loc_00A255B2:
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(Arg1)));
    goto loc_00A25306;
loc_00A255B9:
    if (((uint32_t)(local_rdi)) == ((uint32_t)((uint32_t)(0xC0000023ULL)))) { local_rdi = (uint32_t)((uint32_t)(0xC0000206ULL)); }
    goto loc_00A25503;
loc_00A255CD:
    goto loc_00A25533;
loc_00A255D7:
    v_stack_p28 = v_stack_p78;
    v_stack_p20 = v_stack_p70;
    result = ExLockUserBuffer(local_rdi, (uint32_t)((uint32_t)(local_rbx)), (uint8_t)(v_stack_m58), 1);
    if (sign_flag) goto loc_00A25533;
    goto loc_00A25142;
loc_00A2560B:
    if (((uint32_t)(v_stack_m58)) >= ((uint32_t)((uint32_t)(v_stack_p30)))) goto loc_00A251CF;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint8_t)(v_stack_m58), 1);
loc_00A25633:
    local_rbx = 0;
    a3 = 0;
    v_stack_p38 = 0xC0000023ULL;
    goto loc_00A25355;
loc_00A25645:
    v_stack_p120 = 0;
    v_stack_p48 = 16;
    goto loc_00A25355;
loc_00A2565B:
    *(uint32_t *)(v_stack_m58 + 0xC) = 0;
    goto loc_00A253F7;
loc_00A25667:
    Arg2 = (uint32_t)((0) | (16));
    *(uint32_t *)(v_stack_m58 + 0xC) = (uint32_t)(Arg2);
    goto loc_00A25401;
loc_00A25672:
    goto loc_00A254A4;
loc_00A2567B:
    result = ExUnlockUserBuffer(16, Arg2, a3, 1);
    goto loc_00A25520;
loc_00A25685:
    goto loc_00A25533;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A25040&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
