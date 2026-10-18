# IoWriteCrashDump

- RVA: `0x005936D8`–`0x00593E4E` (길이 `1,910` bytes)
- VA: `0x00000001405936D8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC7B4`
- 디코드: `447`개 명령, `1,910/1,910` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **25**

### Outgoing calls
- `0x0059373F` → [KdCheckForDebugBreak](../39/KdCheckForDebugBreak_function_0039DED8.md) (function, `0x0039DED8`)
- `0x00593777` → [IopWriteCapsuleTriageDumpToFirmware](IopWriteCapsuleTriageDumpToFirmware_function_005967AC.md) (function, `0x005967AC`)
- `0x00593797` → [IoSetBugCheckProgressFlag](IoSetBugCheckProgressFlag_function_005931C0.md) (function, `0x005931C0`)
- `0x005937C5` → [MmSnapTriageDumpInformation](../67/MmSnapTriageDumpInformation_function_0067DE28.md) (function, `0x0067DE28`)
- `0x00593838` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00593891` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0059389E` → [IoSaveBugCheckProgress](IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x00593AD8` → [IopCollectTriageDumpData](IopCollectTriageDumpData_function_00594754.md) (function, `0x00594754`)
- `0x00593AF2` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00593B50` → [IoAddPagesForPartialKernelDump](../5A/IoAddPagesForPartialKernelDump_function_005A0F3C.md) (function, `0x005A0F3C`)
- `0x00593BDD` → [IopDumpCallAddPagesCallbacks](IopDumpCallAddPagesCallbacks_function_005949FC.md) (function, `0x005949FC`)
- `0x00593BE7` → [IoSaveBugCheckProgress](IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x00593BF8` → [MmGetDumpRange](../67/MmGetDumpRange_function_0067DA68.md) (function, `0x0067DA68`)
- `0x00593C02` → [IoSaveBugCheckProgress](IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x00593C0A` → [IopDumpCallRemovePagesCallbacks](IopDumpCallRemovePagesCallbacks_function_00594B44.md) (function, `0x00594B44`)
- `0x00593C14` → [IoSaveBugCheckProgress](IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x00593C1D` → [RtlNumberOfSetBitsEx](../41/RtlNumberOfSetBitsEx_function_00418CA0.md) (function, `0x00418CA0`)
- `0x00593C43` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00593C6C` → [IoSaveBugCheckProgress](IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x00593CA9` → [IoAddPagesForPartialKernelDump](../5A/IoAddPagesForPartialKernelDump_function_005A0F3C.md) (function, `0x005A0F3C`)
- `0x00593CC9` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00593CEA` → [IoSetBugCheckProgressFlag](IoSetBugCheckProgressFlag_function_005931C0.md) (function, `0x005931C0`)
- `0x00593D3B` → [IopCollectTriageDumpData](IopCollectTriageDumpData_function_00594754.md) (function, `0x00594754`)
- `0x00593D57` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00593D63` → [IoSaveBugCheckProgress](IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x00593D84` → [IoSaveBugCheckProgress](IoSaveBugCheckProgress_function_00592E10.md) (function, `0x00592E10`)
- `0x00593D92` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00593DA4` → [IoSetBugCheckProgressFlag](IoSetBugCheckProgressFlag_function_005931C0.md) (function, `0x005931C0`)
- `0x00593DAE` → [KeStallExecutionProcessor](../44/KeStallExecutionProcessor_function_0044F620.md) (function, `0x0044F620`)
- `0x00593DFF` → [IoUpdateBugCheckProgressEnvVariable](IoUpdateBugCheckProgressEnvVariable_function_005933E0.md) (function, `0x005933E0`)
- `0x00593E12` → [IopWriteTriageDumpToFirmware](IopWriteTriageDumpToFirmware_function_00596984.md) (function, `0x00596984`)
- `0x00593E1E` → [IoSetBugCheckProgressFlag](IoSetBugCheckProgressFlag_function_005931C0.md) (function, `0x005931C0`)
- `0x00593E34` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IoRetryAsMiniDump](IoRetryAsMiniDump_function_00592CA0.md) at `0x00592D7F`
- [KiBugCheckWriteCrashDump](../5B/KiBugCheckWriteCrashDump_function_005B4148.md) at `0x005B4194`

### Static image references
- `0x005936F1` → RVA `0x00E0A740` (`.data`; read)
- `0x00593744` → RVA `0x00E65F60` (`.data`; read)
- `0x00593781` → RVA `0x00E661BC` (`.data`; read)
- `0x00593789` → RVA `0x00E661B4` (`.data`; read)
- `0x005937CA` → RVA `0x00E66050` (`.data`; read)
- `0x00593829` → RVA `0x00E66000` (`.data`; read)
- `0x0059385D` → RVA `0x00FC6A84` (`ALMOSTRO`; read)
- `0x00593866` → RVA `0x00F8ECA8` (`.data`; read)
- `0x0059386E` → RVA `0x00F8ECA8` (`.data`; write)
- `0x00593881` → RVA `0x00E66030` (`.data`; read)
- `0x0059388B` → RVA `0x00F03FA4` (`.data`; write)
- `0x00593973` → RVA `0x00E01060` (`.data`; read)
- `0x0059398C` → RVA `0x00F067C0` (`.data`; read)
- `0x005939A1` → RVA `0x00EF54C0` (`.data`; read)
- `0x005939BD` → RVA `0x00FC6C38` (`ALMOSTRO`; read)
- `0x005939CB` → RVA `0x00F234A0` (`.data`; read)
- `0x005939DD` → RVA `0x00F23490` (`.data`; read)
- `0x00593A9D` → RVA `0x00E65EE8` (`.data`; read)
- `0x00593B8B` → RVA `0x005931F0` (`IoSetDumpRange`; read)
- `0x00593B96` → RVA `0x005927B0` (`IoFreeDumpRange`; read)
- `0x00593C32` → RVA `0x00E66008` (`.data`; read)
- `0x00593D01` → RVA `0x00E65EE8` (`.data`; write)
- `0x00593D68` → RVA `0x00E65EFC` (`.data`; read)
- `0x00593D89` → RVA `0x00E00B38` (`.data`; read)
- `0x00593DB3` → RVA `0x00E65F00` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005936D8  40 55                           push rbp
005936DA  53                              push rbx
005936DB  56                              push rsi
005936DC  57                              push rdi
005936DD  41 54                           push r12
005936DF  41 55                           push r13
005936E1  41 56                           push r14
005936E3  41 57                           push r15
005936E5  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
005936EA  48 81 EC E8 00 00 00            sub rsp, 0xe8
005936F1  48 8B 05 48 70 87 00            mov rax, qword ptr [rip + 0x877048]
005936F8  48 33 C4                        xor rax, rsp
005936FB  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
005936FF  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00593703  33 FF                           xor edi, edi
00593705  4C 8B A5 87 00 00 00            mov r12, qword ptr [rbp + 0x87]
0059370C  4D 8B E8                        mov r13, r8
0059370F  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00593714  4D 85 E4                        test r12, r12
00593717  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0059371B  4C 8B F2                        mov r14, rdx
0059371E  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
00593722  0F 94 44 24 50                  sete byte ptr [rsp + 0x50]
00593727  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
0059372C  44 8B F9                        mov r15d, ecx
0059372F  4C 89 45 8F                     mov qword ptr [rbp - 0x71], r8
00593733  8B F7                           mov esi, edi
00593735  48 89 55 97                     mov qword ptr [rbp - 0x69], rdx
00593739  8B DF                           mov ebx, edi
0059373B  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
0059373F  E8 94 A7 E0 FF                  call 0x14039ded8
00593744  80 3D 15 28 8D 00 01            cmp byte ptr [rip + 0x8d2815], 1
0059374B  75 34                           jne 0x140593781
0059374D  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
00593751  4D 8B C5                        mov r8, r13
00593754  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
00593759  49 8B D6                        mov rdx, r14
0059375C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00593761  41 8B CF                        mov ecx, r15d
00593764  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00593769  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0059376E  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00593772  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00593777  E8 30 30 00 00                  call 0x1405967ac
0059377C  E9 AC 06 00 00                  jmp 0x140593e2d
00593781  39 3D 35 2A 8D 00               cmp dword ptr [rip + 0x8d2a35], edi
00593787  74 1A                           je 0x1405937a3
00593789  40 38 3D 24 2A 8D 00            cmp byte ptr [rip + 0x8d2a24], dil
00593790  75 11                           jne 0x1405937a3
00593792  B9 00 00 40 00                  mov ecx, 0x400000
00593797  E8 24 FA FF FF                  call 0x1405931c0
0059379C  32 C0                           xor al, al
0059379E  E9 8A 06 00 00                  jmp 0x140593e2d
005937A3  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
005937A8  48 8D 55 CF                     lea rdx, [rbp - 0x31]
005937AC  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
005937B0  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
005937B5  4C 89 4D DF                     mov qword ptr [rbp - 0x21], r9
005937B9  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
005937BD  4C 89 75 CF                     mov qword ptr [rbp - 0x31], r14
005937C1  4C 89 6D D7                     mov qword ptr [rbp - 0x29], r13
005937C5  E8 5E A6 0E 00                  call 0x14067de28
005937CA  48 8B 0D 7F 28 8D 00            mov rcx, qword ptr [rip + 0x8d287f]
005937D1  48 85 C9                        test rcx, rcx
005937D4  0F 84 50 06 00 00               je 0x140593e2a
005937DA  8B 81 58 05 00 00               mov eax, dword ptr [rcx + 0x558]
005937E0  41 BD 01 00 00 00               mov r13d, 1
005937E6  41 84 C5                        test r13b, al
005937E9  74 2B                           je 0x140593816
005937EB  83 B9 38 05 00 00 06            cmp dword ptr [rcx + 0x538], 6
005937F2  75 22                           jne 0x140593816
005937F4  8B D7                           mov edx, edi
005937F6  83 FA 08                        cmp edx, 8
005937F9  73 1B                           jae 0x140593816
005937FB  8B C2                           mov eax, edx
005937FD  44 39 BC 81 5C 05 00 00         cmp dword ptr [rcx + rax*4 + 0x55c], r15d
00593805  74 05                           je 0x14059380c
00593807  41 03 D5                        add edx, r13d
0059380A  EB EA                           jmp 0x1405937f6
0059380C  C7 81 38 05 00 00 05 00 00 00   mov dword ptr [rcx + 0x538], 5
00593816  4D 85 E4                        test r12, r12
00593819  75 0E                           jne 0x140593829
0059381B  48 8B 05 2E 28 8D 00            mov rax, qword ptr [rip + 0x8d282e]
00593822  41 8B F5                        mov esi, r13d
00593825  48 89 78 08                     mov qword ptr [rax + 8], rdi
00593829  48 8B 05 D0 27 8D 00            mov rax, qword ptr [rip + 0x8d27d0]
00593830  44 8B C6                        mov r8d, esi
00593833  33 D2                           xor edx, edx
00593835  41 8B CD                        mov ecx, r13d
00593838  E8 93 72 12 00                  call 0x1406baad0
0059383D  48 8B 0D 0C 28 8D 00            mov rcx, qword ptr [rip + 0x8d280c]
00593844  8B 81 58 05 00 00               mov eax, dword ptr [rcx + 0x558]
0059384A  A8 02                           test al, 2
0059384C  75 0C                           jne 0x14059385a
0059384E  83 B9 38 05 00 00 05            cmp dword ptr [rcx + 0x538], 5
00593855  41 8A CD                        mov cl, r13b
00593858  74 03                           je 0x14059385d
0059385A  40 8A CF                        mov cl, dil
0059385D  40 38 3D 20 32 A3 00            cmp byte ptr [rip + 0xa33220], dil
00593864  74 1B                           je 0x140593881
00593866  8B 05 3C B4 9F 00               mov eax, dword ptr [rip + 0x9fb43c]
0059386C  03 C0                           add eax, eax
0059386E  89 05 34 B4 9F 00               mov dword ptr [rip + 0x9fb434], eax
00593874  84 C9                           test cl, cl
00593876  74 09                           je 0x140593881
00593878  41 0B C5                        or eax, r13d
0059387B  89 05 27 B4 9F 00               mov dword ptr [rip + 0x9fb427], eax
00593881  48 8B 05 A8 27 8D 00            mov rax, qword ptr [rip + 0x8d27a8]
00593888  41 8A CD                        mov cl, r13b
0059388B  89 3D 13 07 97 00               mov dword ptr [rip + 0x970713], edi
00593891  E8 3A 72 12 00                  call 0x1406baad0
00593896  B9 20 00 00 00                  mov ecx, 0x20
0059389B  44 8A E8                        mov r13b, al
0059389E  E8 6D F5 FF FF                  call 0x140592e10
005938A3  48 8B 05 A6 27 8D 00            mov rax, qword ptr [rip + 0x8d27a6]
005938AA  BA 09 00 00 00                  mov edx, 9
005938AF  48 8B 75 8F                     mov rsi, qword ptr [rbp - 0x71]
005938B3  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
005938B8  4C 8B 5D 6F                     mov r11, qword ptr [rbp + 0x6f]
005938BC  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
005938C1  44 8D 52 77                     lea r10d, [rdx + 0x77]
005938C5  44 89 78 18                     mov dword ptr [rax + 0x18], r15d
005938C9  49 8B C9                        mov rcx, r9
005938CC  48 8B 05 7D 27 8D 00            mov rax, qword ptr [rip + 0x8d277d]
005938D3  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
005938D7  48 8B 05 72 27 8D 00            mov rax, qword ptr [rip + 0x8d2772]
005938DE  48 89 70 28                     mov qword ptr [rax + 0x28], rsi
005938E2  48 8B 05 67 27 8D 00            mov rax, qword ptr [rip + 0x8d2767]
005938E9  4C 89 40 30                     mov qword ptr [rax + 0x30], r8
005938ED  48 8B 05 5C 27 8D 00            mov rax, qword ptr [rip + 0x8d275c]
005938F4  4C 89 58 38                     mov qword ptr [rax + 0x38], r11
005938F8  48 8B 05 51 27 8D 00            mov rax, qword ptr [rip + 0x8d2751]
005938FF  48 83 C0 40                     add rax, 0x40
00593903  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00593906  0F 11 00                        movups xmmword ptr [rax], xmm0
00593909  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
0059390D  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00593911  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
00593915  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00593919  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
0059391D  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
00593921  0F 10 41 40                     movups xmm0, xmmword ptr [rcx + 0x40]
00593925  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
00593929  0F 10 49 50                     movups xmm1, xmmword ptr [rcx + 0x50]
0059392D  0F 11 48 50                     movups xmmword ptr [rax + 0x50], xmm1
00593931  0F 10 41 60                     movups xmm0, xmmword ptr [rcx + 0x60]
00593935  0F 11 40 60                     movups xmmword ptr [rax + 0x60], xmm0
00593939  49 03 C2                        add rax, r10
0059393C  0F 10 49 70                     movups xmm1, xmmword ptr [rcx + 0x70]
00593940  49 03 CA                        add rcx, r10
00593943  0F 11 48 F0                     movups xmmword ptr [rax - 0x10], xmm1
00593947  48 83 EA 01                     sub rdx, 1
0059394B  75 B6                           jne 0x140593903
0059394D  4C 8B 55 87                     mov r10, qword ptr [rbp - 0x79]
00593951  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00593954  0F 11 00                        movups xmmword ptr [rax], xmm0
00593957  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
0059395B  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
0059395F  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
00593963  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00593967  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
0059396B  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
0059396F  0F 10 41 40                     movups xmm0, xmmword ptr [rcx + 0x40]
00593973  48 8D 0D E6 D6 86 00            lea rcx, [rip + 0x86d6e6]
0059397A  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
0059397E  48 8B 05 CB 26 8D 00            mov rax, qword ptr [rip + 0x8d26cb]
00593985  48 89 88 10 05 00 00            mov qword ptr [rax + 0x510], rcx
0059398C  48 8D 0D 2D 2E 97 00            lea rcx, [rip + 0x972e2d]
00593993  48 8B 05 B6 26 8D 00            mov rax, qword ptr [rip + 0x8d26b6]
0059399A  48 89 88 18 05 00 00            mov qword ptr [rax + 0x518], rcx
005939A1  48 8D 0D 18 1B 96 00            lea rcx, [rip + 0x961b18]
005939A8  48 8B 05 A1 26 8D 00            mov rax, qword ptr [rip + 0x8d26a1]
005939AF  48 89 88 20 05 00 00            mov qword ptr [rax + 0x520], rcx
005939B6  48 8B 0D 93 26 8D 00            mov rcx, qword ptr [rip + 0x8d2693]
005939BD  48 8B 05 74 32 A3 00            mov rax, qword ptr [rip + 0xa33274]
005939C4  48 89 81 28 05 00 00            mov qword ptr [rcx + 0x528], rax
005939CB  48 8D 0D CE FA 98 00            lea rcx, [rip + 0x98face]
005939D2  48 8B 05 77 26 8D 00            mov rax, qword ptr [rip + 0x8d2677]
005939D9  48 89 48 10                     mov qword ptr [rax + 0x10], rcx
005939DD  48 8D 0D AC FA 98 00            lea rcx, [rip + 0x98faac]
005939E4  48 8B 05 65 26 8D 00            mov rax, qword ptr [rip + 0x8d2665]
005939EB  48 89 88 88 05 00 00            mov qword ptr [rax + 0x588], rcx
005939F2  48 8B 05 57 26 8D 00            mov rax, qword ptr [rip + 0x8d2657]
005939F9  C6 80 98 05 00 00 04            mov byte ptr [rax + 0x598], 4
00593A00  4D 85 E4                        test r12, r12
00593A03  74 0D                           je 0x140593a12
00593A05  49 8B 82 B8 00 00 00            mov rax, qword ptr [r10 + 0xb8]
00593A0C  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00593A10  EB 03                           jmp 0x140593a15
00593A12  0F 20 D9                        mov rcx, cr3
00593A15  48 8B 05 34 26 8D 00            mov rax, qword ptr [rip + 0x8d2634]
00593A1C  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00593A23  48 89 88 40 05 00 00            mov qword ptr [rax + 0x540], rcx
00593A2A  48 8B 0D 1F 26 8D 00            mov rcx, qword ptr [rip + 0x8d261f]
00593A31  48 8B 91 30 05 00 00            mov rdx, qword ptr [rcx + 0x530]
00593A38  48 85 D2                        test rdx, rdx
00593A3B  75 0F                           jne 0x140593a4c
00593A3D  41 80 FD 01                     cmp r13b, 1
00593A41  75 0F                           jne 0x140593a52
00593A43  4D 85 E4                        test r12, r12
00593A46  0F 85 B9 00 00 00               jne 0x140593b05
00593A4C  41 80 FD 01                     cmp r13b, 1
00593A50  74 26                           je 0x140593a78
00593A52  48 8B 81 50 05 00 00            mov rax, qword ptr [rcx + 0x550]
00593A59  48 85 C0                        test rax, rax
00593A5C  74 1A                           je 0x140593a78
00593A5E  48 05 1C 30 00 00               add rax, 0x301c
00593A64  48 89 81 30 05 00 00            mov qword ptr [rcx + 0x530], rax
00593A6B  48 8B 05 DE 25 8D 00            mov rax, qword ptr [rip + 0x8d25de]
00593A72  48 89 78 08                     mov qword ptr [rax + 8], rdi
00593A76  EB 1E                           jmp 0x140593a96
00593A78  48 85 D2                        test rdx, rdx
00593A7B  75 19                           jne 0x140593a96
00593A7D  4D 85 E4                        test r12, r12
00593A80  75 14                           jne 0x140593a96
00593A82  48 8B 81 50 05 00 00            mov rax, qword ptr [rcx + 0x550]
00593A89  48 05 00 20 00 00               add rax, 0x2000
00593A8F  48 89 81 30 05 00 00            mov qword ptr [rcx + 0x530], rax
00593A96  48 8B 05 B3 25 8D 00            mov rax, qword ptr [rip + 0x8d25b3]
00593A9D  48 8B 15 44 24 8D 00            mov rdx, qword ptr [rip + 0x8d2444]
00593AA4  48 8B 88 30 05 00 00            mov rcx, qword ptr [rax + 0x530]
00593AAB  48 85 D2                        test rdx, rdx
00593AAE  75 39                           jne 0x140593ae9
00593AB0  8A 44 24 50                     mov al, byte ptr [rsp + 0x50]
00593AB4  49 8B D6                        mov rdx, r14
00593AB7  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00593ABC  41 8B CF                        mov ecx, r15d
00593ABF  88 44 24 38                     mov byte ptr [rsp + 0x38], al
00593AC3  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
00593AC8  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
00593ACD  4D 8B C8                        mov r9, r8
00593AD0  4C 8B C6                        mov r8, rsi
00593AD3  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00593AD8  E8 77 0C 00 00                  call 0x140594754
00593ADD  8B D8                           mov ebx, eax
00593ADF  85 C0                           test eax, eax
00593AE1  0F 88 43 03 00 00               js 0x140593e2a
00593AE7  EB 0E                           jmp 0x140593af7
00593AE9  48 3B D1                        cmp rdx, rcx
00593AEC  74 17                           je 0x140593b05
00593AEE  44 8B 42 04                     mov r8d, dword ptr [rdx + 4]
00593AF2  E8 49 2D 13 00                  call 0x1406c6840
00593AF7  4C 8B 5D 6F                     mov r11, qword ptr [rbp + 0x6f]
00593AFB  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
00593B00  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00593B05  48 8B 0D 44 25 8D 00            mov rcx, qword ptr [rip + 0x8d2544]
00593B0C  8B 81 58 05 00 00               mov eax, dword ptr [rcx + 0x558]
00593B12  8B D0                           mov edx, eax
00593B14  83 E2 02                        and edx, 2
00593B17  74 43                           je 0x140593b5c
00593B19  83 B9 38 05 00 00 06            cmp dword ptr [rcx + 0x538], 6
00593B20  75 3A                           jne 0x140593b5c
00593B22  48 39 79 08                     cmp qword ptr [rcx + 8], rdi
00593B26  74 34                           je 0x140593b5c
00593B28  83 C8 04                        or eax, 4
00593B2B  49 8B D6                        mov rdx, r14
00593B2E  89 81 58 05 00 00               mov dword ptr [rcx + 0x558], eax
00593B34  41 8B CF                        mov ecx, r15d
00593B37  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
00593B3B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00593B40  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
00593B45  4D 8B C8                        mov r9, r8
00593B48  4C 8B C6                        mov r8, rsi
00593B4B  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00593B50  E8 E7 D3 00 00                  call 0x1405a0f3c
00593B55  8B D8                           mov ebx, eax
00593B57  E9 D2 00 00 00                  jmp 0x140593c2e
00593B5C  48 8B 71 08                     mov rsi, qword ptr [rcx + 8]
00593B60  48 85 F6                        test rsi, rsi
00593B63  0F 84 C1 00 00 00               je 0x140593c2a
00593B69  48 89 7D C7                     mov qword ptr [rbp - 0x39], rdi
00593B6D  41 BE 01 00 00 00               mov r14d, 1
00593B73  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00593B77  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00593B7B  48 8D 46 38                     lea rax, [rsi + 0x38]
00593B7F  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00593B83  48 8D 45 CF                     lea rax, [rbp - 0x31]
00593B87  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00593B8B  48 8D 05 5E F6 FF FF            lea rax, [rip - 0x9a2]
00593B92  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
00593B96  48 8D 05 13 EC FF FF            lea rax, [rip - 0x13ed]
00593B9D  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00593BA1  48 89 75 B7                     mov qword ptr [rbp - 0x49], rsi
00593BA5  48 89 7D BF                     mov qword ptr [rbp - 0x41], rdi
00593BA9  8B 81 38 05 00 00               mov eax, dword ptr [rcx + 0x538]
00593BAF  83 F8 06                        cmp eax, 6
00593BB2  75 12                           jne 0x140593bc6
00593BB4  40 38 BD 8F 00 00 00            cmp byte ptr [rbp + 0x8f], dil
00593BBB  8B C7                           mov eax, edi
00593BBD  0F 95 C0                        setne al
00593BC0  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00593BC4  EB 11                           jmp 0x140593bd7
00593BC6  83 F8 05                        cmp eax, 5
00593BC9  75 0F                           jne 0x140593bda
00593BCB  85 D2                           test edx, edx
00593BCD  74 0B                           je 0x140593bda
00593BCF  C7 44 24 54 02 00 00 00         mov dword ptr [rsp + 0x54], 2
00593BD7  44 8B F7                        mov r14d, edi
00593BDA  41 8B CF                        mov ecx, r15d
00593BDD  E8 1A 0E 00 00                  call 0x1405949fc
00593BE2  B9 21 00 00 00                  mov ecx, 0x21
00593BE7  E8 24 F2 FF FF                  call 0x140592e10
00593BEC  44 8B 44 24 54                  mov r8d, dword ptr [rsp + 0x54]
00593BF1  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
00593BF5  41 8B D6                        mov edx, r14d
00593BF8  E8 6B 9E 0E 00                  call 0x14067da68
00593BFD  B9 2B 00 00 00                  mov ecx, 0x2b
00593C02  E8 09 F2 FF FF                  call 0x140592e10
00593C07  41 8B CF                        mov ecx, r15d
00593C0A  E8 35 0F 00 00                  call 0x140594b44
00593C0F  B9 22 00 00 00                  mov ecx, 0x22
00593C14  E8 F7 F1 FF FF                  call 0x140592e10
00593C19  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00593C1D  E8 7E 50 E8 FF                  call 0x140418ca0
00593C22  4C 8B 75 97                     mov r14, qword ptr [rbp - 0x69]
00593C26  48 89 46 28                     mov qword ptr [rsi + 0x28], rax
00593C2A  48 8B 75 8F                     mov rsi, qword ptr [rbp - 0x71]
00593C2E  85 DB                           test ebx, ebx
00593C30  78 18                           js 0x140593c4a
00593C32  48 8B 05 CF 23 8D 00            mov rax, qword ptr [rip + 0x8d23cf]
00593C39  49 8B D4                        mov rdx, r12
00593C3C  48 8B 0D 0D 24 8D 00            mov rcx, qword ptr [rip + 0x8d240d]
00593C43  E8 88 6E 12 00                  call 0x1406baad0
00593C48  8B D8                           mov ebx, eax
00593C4A  81 FB 2D 02 00 C0               cmp ebx, 0xc000022d
00593C50  0F 85 12 01 00 00               jne 0x140593d68
00593C56  48 8B 0D F3 23 8D 00            mov rcx, qword ptr [rip + 0x8d23f3]
00593C5D  8B 81 58 05 00 00               mov eax, dword ptr [rcx + 0x558]
00593C63  A8 04                           test al, 4
00593C65  74 71                           je 0x140593cd8
00593C67  B9 27 00 00 00                  mov ecx, 0x27
00593C6C  E8 9F F1 FF FF                  call 0x140592e10
00593C71  48 8B 05 D8 23 8D 00            mov rax, qword ptr [rip + 0x8d23d8]
00593C78  4C 8B C6                        mov r8, rsi
00593C7B  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
00593C80  49 8B D6                        mov rdx, r14
00593C83  41 8B CF                        mov ecx, r15d
00593C86  83 88 58 05 00 00 08            or dword ptr [rax + 0x558], 8
00593C8D  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
00593C91  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00593C96  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00593C9B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00593CA0  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00593CA4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00593CA9  E8 8E D2 00 00                  call 0x1405a0f3c
00593CAE  8B D8                           mov ebx, eax
00593CB0  85 C0                           test eax, eax
00593CB2  0F 88 B0 00 00 00               js 0x140593d68
00593CB8  48 8B 05 49 23 8D 00            mov rax, qword ptr [rip + 0x8d2349]
00593CBF  49 8B D4                        mov rdx, r12
00593CC2  48 8B 0D 87 23 8D 00            mov rcx, qword ptr [rip + 0x8d2387]
00593CC9  E8 02 6E 12 00                  call 0x1406baad0
00593CCE  B9 26 00 00 00                  mov ecx, 0x26
00593CD3  E9 89 00 00 00                  jmp 0x140593d61
00593CD8  48 39 B9 30 05 00 00            cmp qword ptr [rcx + 0x530], rdi
00593CDF  0F 84 83 00 00 00               je 0x140593d68
00593CE5  B9 00 04 00 00                  mov ecx, 0x400
00593CEA  E8 D1 F4 FF FF                  call 0x1405931c0
00593CEF  48 8B 05 5A 23 8D 00            mov rax, qword ptr [rip + 0x8d235a]
00593CF6  4C 8B C6                        mov r8, rsi
00593CF9  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
00593CFE  49 8B D6                        mov rdx, r14
00593D01  48 89 3D E0 21 8D 00            mov qword ptr [rip + 0x8d21e0], rdi
00593D08  48 8B 88 30 05 00 00            mov rcx, qword ptr [rax + 0x530]
00593D0F  8A 44 24 50                     mov al, byte ptr [rsp + 0x50]
00593D13  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00593D18  41 8B CF                        mov ecx, r15d
00593D1B  88 44 24 38                     mov byte ptr [rsp + 0x38], al
00593D1F  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
00593D23  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00593D28  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00593D2D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00593D32  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00593D36  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00593D3B  E8 14 0A 00 00                  call 0x140594754
00593D40  8B D8                           mov ebx, eax
00593D42  85 C0                           test eax, eax
00593D44  78 22                           js 0x140593d68
00593D46  48 8B 05 BB 22 8D 00            mov rax, qword ptr [rip + 0x8d22bb]
00593D4D  49 8B D4                        mov rdx, r12
00593D50  48 8B 0D F9 22 8D 00            mov rcx, qword ptr [rip + 0x8d22f9]
00593D57  E8 74 6D 12 00                  call 0x1406baad0
00593D5C  B9 23 00 00 00                  mov ecx, 0x23
00593D61  8B D8                           mov ebx, eax
00593D63  E8 A8 F0 FF FF                  call 0x140592e10
00593D68  8B 05 8E 21 8D 00               mov eax, dword ptr [rip + 0x8d218e]
00593D6E  A8 01                           test al, 1
00593D70  74 04                           je 0x140593d76
00593D72  85 DB                           test ebx, ebx
00593D74  78 09                           js 0x140593d7f
00593D76  A8 02                           test al, 2
00593D78  74 41                           je 0x140593dbb
00593D7A  45 84 ED                        test r13b, r13b
00593D7D  75 3C                           jne 0x140593dbb
00593D7F  B9 24 00 00 00                  mov ecx, 0x24
00593D84  E8 87 F0 FF FF                  call 0x140592e10
00593D89  48 8B 05 A8 CD 86 00            mov rax, qword ptr [rip + 0x86cda8]
00593D90  33 C9                           xor ecx, ecx
00593D92  E8 39 6D 12 00                  call 0x1406baad0
00593D97  85 C0                           test eax, eax
00593D99  0F 88 8B 00 00 00               js 0x140593e2a
00593D9F  B9 00 10 00 00                  mov ecx, 0x1000
00593DA4  E8 17 F4 FF FF                  call 0x1405931c0
00593DA9  B9 40 42 0F 00                  mov ecx, 0xf4240
00593DAE  E8 6D B8 EB FF                  call 0x14044f620
00593DB3  FF 05 47 21 8D 00               inc dword ptr [rip + 0x8d2147]
00593DB9  EB EE                           jmp 0x140593da9
00593DBB  85 DB                           test ebx, ebx
00593DBD  78 6B                           js 0x140593e2a
00593DBF  41 80 FD 01                     cmp r13b, 1
00593DC3  74 62                           je 0x140593e27
00593DC5  48 8B 0D 84 22 8D 00            mov rcx, qword ptr [rip + 0x8d2284]
00593DCC  48 39 B9 50 05 00 00            cmp qword ptr [rcx + 0x550], rdi
00593DD3  74 52                           je 0x140593e27
00593DD5  8B 81 7C 05 00 00               mov eax, dword ptr [rcx + 0x57c]
00593DDB  A9 00 00 86 00                  test eax, 0x860000
00593DE0  75 0E                           jne 0x140593df0
00593DE2  25 25 FE FF FF                  and eax, 0xfffffe25
00593DE7  83 C8 25                        or eax, 0x25
00593DEA  89 81 7C 05 00 00               mov dword ptr [rcx + 0x57c], eax
00593DF0  48 8B 05 59 22 8D 00            mov rax, qword ptr [rip + 0x8d2259]
00593DF7  0F BA A8 7C 05 00 00 0B         bts dword ptr [rax + 0x57c], 0xb
00593DFF  E8 DC F5 FF FF                  call 0x1405933e0
00593E04  48 8B 0D 45 22 8D 00            mov rcx, qword ptr [rip + 0x8d2245]
00593E0B  48 8B 89 50 05 00 00            mov rcx, qword ptr [rcx + 0x550]
00593E12  E8 6D 2B 00 00                  call 0x140596984
00593E17  B9 00 00 00 10                  mov ecx, 0x10000000
00593E1C  8B D8                           mov ebx, eax
00593E1E  E8 9D F3 FF FF                  call 0x1405931c0
00593E23  85 DB                           test ebx, ebx
00593E25  78 03                           js 0x140593e2a
00593E27  40 B7 01                        mov dil, 1
00593E2A  40 8A C7                        mov al, dil
00593E2D  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
00593E31  48 33 CC                        xor rcx, rsp
00593E34  E8 07 88 11 00                  call 0x1406ac640
00593E39  48 81 C4 E8 00 00 00            add rsp, 0xe8
00593E40  41 5F                           pop r15
00593E42  41 5E                           pop r14
00593E44  41 5D                           pop r13
00593E46  41 5C                           pop r12
00593E48  5F                              pop rdi
00593E49  5E                              pop rsi
00593E4A  5B                              pop rbx
00593E4B  5D                              pop rbp
00593E4C  C3                              ret
00593E4D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoWriteCrashDump(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, unsigned __int8 a9)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m47;
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
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int8 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (232);
    result = (*(unsigned __int64 *)(v_rip + 8876104)) ^ (v_rsp);
    v_stack_m58 = result;
    v_rdi = 0;
    v_stack_mD0 = a6;
    v_stack_mC0 = a7;
    v_stack_mC8 = a4;
    v_stack_mB8 = a3;
    v_stack_mB0 = a2;
    v_stack_mD4 = 0;
    result = KdCheckForDebugBreak(a1, a2, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 9250837)) != 1) goto loc_00593781;
    v_stack_mF8 = v_stack_mC0;
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = a5;
    result = IopWriteCapsuleTriageDumpToFirmware((unsigned int)((unsigned int)((unsigned int)(a1))), a2, a3, v_stack_mC8);
    goto loc_00593E2D;
loc_00593781:
    if ((*(unsigned int *)(v_rip + 9251381)) == 0) goto loc_005937A3;
    if ((*(unsigned __int8 *)(v_rip + 9251364)) != 0) goto loc_005937A3;
    result = IoSetBugCheckProgressFlag((unsigned int)(0x400000ULL), a2, a3, v_stack_mC8);
    result = 0;
    goto loc_00593E2D;
loc_005937A3:
    v_stack_m68 = v_stack_mC8;
    v_stack_m60 = a5;
    v_stack_m78 = a2;
    v_stack_m70 = a3;
    result = MmSnapTriageDumpInformation(v_stack_mD0, v_stack_m78, a3, v_stack_mC8);
    if (*(unsigned __int64 *)(v_rip + 9250943) == 0) goto loc_00593E2A;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9250943) + 1368))))) == 0) goto loc_00593816;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9250943) + 1336)) != 6) goto loc_00593816;
loc_005937F6:
    if (0 >= 8) goto loc_00593816;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9250943) + 0 * 4 + 1372)) == ((unsigned int)((unsigned int)(a1)))) goto loc_0059380C;
    a2 = (unsigned int)((0) + (1));
    goto loc_005937F6;
loc_0059380C:
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 9250943) + 1336) = 5;
loc_00593816:
    result = 0;
    v_rsi = 0;
    if (a8 == 0) {
        result = *(unsigned __int64 *)(v_rip + 9250862);
        v_rsi = 1;
        *(unsigned __int64 *)(result + 8) = 0;
    }
    a2 = 0;
    result = guard_dispatch_icall(1, a2, (unsigned int)((unsigned int)(v_rsi)), v_stack_mC8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9250828) + 1368)))) & (2)) != 0) goto loc_0059385A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9250828) + 1336)) != 5) {
        a1 = 0;
    }
    if ((*(unsigned __int8 *)(v_rip + 10695200)) == 0) goto loc_00593881;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10466364))) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10466364)))));
    *(unsigned int *)(v_rip + 10466356) = (unsigned int)(result);
    if ((unsigned __int8)(a1) != 0) {
        result = (unsigned int)((result) | (1));
        *(unsigned int *)(v_rip + 10466343) = (unsigned int)(result);
    }
    *(unsigned int *)(v_rip + 9897747) = 0;
    result = guard_dispatch_icall(1, a2, (unsigned int)((unsigned int)(v_rsi)), v_stack_mC8);
    result = IoSaveBugCheckProgress(32, a2, (unsigned int)((unsigned int)(v_rsi)), v_stack_mC8);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 9250726) + 24) = (unsigned int)((unsigned int)(a1));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250685) + 32) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250674) + 40) = v_stack_mB8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250663) + 48) = v_stack_mC8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250652) + 56) = a5;
    result = (*(unsigned __int64 *)(v_rip + 9250641)) + (64);
loc_00593903:
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    *(unsigned __int64 *)(result + 64) = v_xmm0;
    *(unsigned __int64 *)(result + 80) = v_xmm1;
    *(unsigned __int64 *)(result + 96) = v_xmm0;
    result = (result) + (9 + 119);
    a1 = (v_stack_mD0) + (9 + 119);
    *(unsigned __int64 *)(result - 16) = v_xmm1;
    a2 = (9) - (1);
    if (condition_is_not_equal) goto loc_00593903;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    *(unsigned __int64 *)(result + 64) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250507) + 1296) = v_rip + 8836838;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250486) + 1304) = v_rip + 9907757;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250465) + 1312) = v_rip + 9837336;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250451) + 1320) = *(unsigned __int64 *)(v_rip + 10695284);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250423) + 16) = v_rip + 10025678;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250405) + 1416) = v_rip + 10025644;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9250391) + 1432) = 4;
    if (a8 == 0) goto loc_00593A12;
    goto loc_00593A15;
loc_00593A12:
loc_00593A15:
    a1 = (v_cr3) & (0xFFFFFFFFFFFFF000ULL);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250356) + 1344) = a1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250335) + 1328) != 0) goto loc_00593A4C;
    if (((unsigned __int8)((unsigned __int8)(result))) != 1) goto loc_00593A52;
    if (a8 != 0) goto loc_00593B05;
loc_00593A4C:
    if (((unsigned __int8)((unsigned __int8)(result))) == 1) goto loc_00593A78;
loc_00593A52:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250335) + 1360) == 0) goto loc_00593A78;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250335) + 1360)) + (0x301CULL);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250335) + 1328) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250270) + 8) = 0;
    goto loc_00593A96;
loc_00593A78:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250335) + 1328) != 0) goto loc_00593A96;
    result = *(unsigned __int64 *)(v_rip + 9250270);
    if (a8 == 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250335) + 1360);
        result = (result) + (0x2000ULL);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250335) + 1328) = result;
    }
    if (*(unsigned __int64 *)(v_rip + 9249860) != 0) goto loc_00593AE9;
    v_stack_mE0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250227) + 1328);
    v_stack_mF0 = (unsigned __int8)(v_stack_mD8);
    v_stack_mF8 = v_stack_mC0;
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = a5;
    result = IopCollectTriageDumpData((unsigned int)((unsigned int)((unsigned int)(a1))), a2, v_stack_mB8, v_stack_mC8);
    if (sign_flag) goto loc_00593E2A;
    goto loc_00593AF7;
loc_00593AE9:
    if (a2 == ((unsigned int)((unsigned int)((unsigned int)(a1))))) goto loc_00593B05;
    result = memcpy((unsigned int)((unsigned int)((unsigned int)(a1))), a2, (unsigned int)(*(unsigned int *)(a2 + 4)), v_stack_mC8);
loc_00593AF7:
loc_00593B05:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9250116) + 1368))))) & (2));
    if (condition_is_equal) goto loc_00593B5C;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9250116) + 1336)) != 6) goto loc_00593B5C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9250116) + 8)) == 0) goto loc_00593B5C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9250116) + 1368))) | (4));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 9250116) + 1368) = (unsigned int)(result);
    v_stack_mF8 = v_stack_mC0;
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = a5;
    result = IoAddPagesForPartialKernelDump((unsigned int)((unsigned int)((unsigned int)(a1))), a2, v_stack_mB8, v_stack_mC8);
    goto loc_00593C2E;
loc_00593B5C:
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(a1))) + 8) == 0) goto loc_00593C2A;
    v_stack_m80 = 0;
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(a1))) + 8) + 48);
    v_stack_m70 = *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(a1))) + 8) + 56;
    v_stack_m98 = v_stack_m78;
    v_stack_mA8 = v_rip - 2466;
    v_stack_mA0 = v_rip - 5101;
    v_stack_m90 = *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(a1))) + 8);
    v_stack_m88 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)(a1))) + 1336)))) != 6) goto loc_00593BC6;
    result = (a9 != 0) ? 1 : 0;
    v_stack_mD4 = (unsigned int)(result);
    goto loc_00593BD7;
loc_00593BC6:
    if (((unsigned int)(result)) != 5) goto loc_00593BDA;
    if ((unsigned int)(a2) == 0) goto loc_00593BDA;
    v_stack_mD4 = 2;
loc_00593BD7:
loc_00593BDA:
    result = IopDumpCallAddPagesCallbacks((unsigned int)((unsigned int)((unsigned int)(a1))), a2, v_stack_mB8, v_stack_mC8);
    result = IoSaveBugCheckProgress(33, a2, v_stack_mB8, v_stack_mC8);
    result = MmGetDumpRange(v_stack_mA8, 0, (unsigned int)(v_stack_mD4), v_stack_mC8);
    result = IoSaveBugCheckProgress(43, 0, (unsigned int)(v_stack_mD4), v_stack_mC8);
    result = IopDumpCallRemovePagesCallbacks((unsigned int)((unsigned int)((unsigned int)(a1))), 0, (unsigned int)(v_stack_mD4), v_stack_mC8);
    result = IoSaveBugCheckProgress(34, 0, (unsigned int)(v_stack_mD4), v_stack_mC8);
    result = RtlNumberOfSetBitsEx(v_stack_m78, 0, (unsigned int)(v_stack_mD4), v_stack_mC8);
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(a1))) + 8) + 40) = result;
loc_00593C2A:
loc_00593C2E:
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        result = *(unsigned __int64 *)(v_rip + 9249743);
        a2 = a8;
        a1 = *(unsigned __int64 *)(v_rip + 9249805);
        result = guard_dispatch_icall(a1, a2, (unsigned int)(v_stack_mD4), v_stack_mC8);
        v_rbx = (unsigned int)(result);
    }
    if (((unsigned int)(v_rbx)) != 0xC000022DULL) goto loc_00593D68;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9249779) + 1368)))) & (4)) == 0) goto loc_00593CD8;
    result = IoSaveBugCheckProgress(39, a2, (unsigned int)(v_stack_mD4), v_stack_mC8);
    v_stack_mF8 = v_stack_mC0;
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = a5;
    result = IoAddPagesForPartialKernelDump((unsigned int)((unsigned int)((unsigned int)(a1))), v_stack_mB0, v_stack_mB8, v_stack_mC8);
    if (sign_flag) goto loc_00593D68;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 9249671), a8, v_stack_mB8, v_stack_mC8);
    goto loc_00593D61;
loc_00593CD8:
    if ((*(unsigned __int64 *)(38 + 1328)) == 0) goto loc_00593D68;
    result = IoSetBugCheckProgressFlag((unsigned int)(0x400ULL), a8, v_stack_mB8, v_stack_mC8);
    *(unsigned __int64 *)(v_rip + 9249248) = 0;
    v_stack_mE0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9249626) + 1328);
    v_stack_mF0 = (unsigned __int8)(v_stack_mD8);
    v_stack_mF8 = v_stack_mC0;
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = a5;
    result = IopCollectTriageDumpData((unsigned int)((unsigned int)((unsigned int)(a1))), v_stack_mB0, v_stack_mB8, v_stack_mC8);
    if (sign_flag) goto loc_00593D68;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 9249529), a8, v_stack_mB8, v_stack_mC8);
loc_00593D61:
    result = IoSaveBugCheckProgress(35, a8, v_stack_mB8, v_stack_mC8);
loc_00593D68:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9249166)))) & (1)) == 0) goto loc_00593D76;
    if (sign_flag) goto loc_00593D7F;
loc_00593D76:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9249166)))) & (2)) == 0) goto loc_00593DBB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_00593DBB;
loc_00593D7F:
    result = IoSaveBugCheckProgress(36, a8, v_stack_mB8, v_stack_mC8);
    a1 = 0;
    result = guard_dispatch_icall(a1, a8, v_stack_mB8, v_stack_mC8);
    if (sign_flag) goto loc_00593E2A;
    result = IoSetBugCheckProgressFlag((unsigned int)(0x1000ULL), a8, v_stack_mB8, v_stack_mC8);
loc_00593DA9:
    result = KeStallExecutionProcessor((unsigned int)(0xF4240ULL), a8, v_stack_mB8, v_stack_mC8);
    goto loc_00593DA9;
loc_00593DBB:
    if (sign_flag) goto loc_00593E2A;
    if (((unsigned __int8)((unsigned __int8)(result))) == 1) goto loc_00593E27;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9249412) + 1360)) == 0) goto loc_00593E27;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9249412) + 1404));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9249412) + 1404)))) & (0x860000ULL)) == 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9249412) + 1404))) & (0xFFFFFE25ULL));
        result = (unsigned int)((result) | (37));
        *(unsigned int *)(*(unsigned __int64 *)(v_rip + 9249412) + 1404) = (unsigned int)(result);
    }
    result = IoUpdateBugCheckProgressEnvVariable(*(unsigned __int64 *)(v_rip + 9249412), a8, v_stack_mB8, v_stack_mC8);
    result = IopWriteTriageDumpToFirmware(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9249349) + 1360), a8, v_stack_mB8, v_stack_mC8);
    result = IoSetBugCheckProgressFlag((unsigned int)(0x10000000ULL), a8, v_stack_mB8, v_stack_mC8);
    if (!(sign_flag)) {
        v_rdi = 1;
    }
loc_00593E2D:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a8, v_stack_mB8, v_stack_mC8);
    v_rsp = (v_rsp) + (232);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoWriteCrashDump(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, uint8_t Arg9)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m47;
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
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint8_t v_stack_mF0;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (232);
    result = (*(uint64_t *)(v_rip + 0x877048)) ^ (local_rsp);
    v_stack_m58 = result;
    local_rdi = 0;
    v_stack_mD0 = Arg6;
    v_stack_mC0 = Arg7;
    v_stack_mC8 = Arg4;
    v_stack_mB8 = Arg3;
    v_stack_mB0 = Arg2;
    v_stack_mD4 = 0;
    result = KdCheckForDebugBreak(Arg1, Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(v_rip + 0x8D2815)) != 1) goto loc_00593781;
    v_stack_mF8 = v_stack_mC0;
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = Arg5;
    result = IopWriteCapsuleTriageDumpToFirmware((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, Arg3, v_stack_mC8);
    goto loc_00593E2D;
loc_00593781:
    if ((*(uint32_t *)(v_rip + 0x8D2A35)) == 0) goto loc_005937A3;
    if ((*(uint8_t *)(v_rip + 0x8D2A24)) != 0) goto loc_005937A3;
    result = IoSetBugCheckProgressFlag((uint32_t)(0x400000ULL), Arg2, Arg3, v_stack_mC8);
    result = 0;
    goto loc_00593E2D;
loc_005937A3:
    v_stack_m68 = v_stack_mC8;
    v_stack_m60 = Arg5;
    v_stack_m78 = Arg2;
    v_stack_m70 = Arg3;
    result = MmSnapTriageDumpInformation(v_stack_mD0, v_stack_m78, Arg3, v_stack_mC8);
    if (*(uint64_t *)(v_rip + 0x8D287F) == 0) goto loc_00593E2A;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8D287F) + 0x558))))) == 0) goto loc_00593816;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x8D287F) + 0x538)) != 6) goto loc_00593816;
loc_005937F6:
    if (0 >= 8) goto loc_00593816;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x8D287F) + 0x0 * 4 + 0x55C)) == ((uint32_t)((uint32_t)(Arg1)))) goto loc_0059380C;
    Arg2 = (uint32_t)((0) + (1));
    goto loc_005937F6;
loc_0059380C:
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x8D287F) + 0x538) = 5;
loc_00593816:
    result = 0;
    local_rsi = 0;
    if (Arg8 == 0) {
        result = *(uint64_t *)(v_rip + 0x8D282E);
        local_rsi = 1;
        *(uint64_t *)(result + 0x8) = 0;
    }
    Arg2 = 0;
    result = guard_dispatch_icall(1, Arg2, (uint32_t)((uint32_t)(local_rsi)), v_stack_mC8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8D280C) + 0x558)))) & (2)) != 0) goto loc_0059385A;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x8D280C) + 0x538)) != 5) {
        Arg1 = 0;
    }
    if ((*(uint8_t *)(v_rip + 0xA33220)) == 0) goto loc_00593881;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9FB43C))) + ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9FB43C)))));
    *(uint32_t *)(v_rip + 0x9FB434) = (uint32_t)(result);
    if ((uint8_t)(Arg1) != 0) {
        result = (uint32_t)((result) | (1));
        *(uint32_t *)(v_rip + 0x9FB427) = (uint32_t)(result);
    }
    *(uint32_t *)(v_rip + 0x970713) = 0;
    result = guard_dispatch_icall(1, Arg2, (uint32_t)((uint32_t)(local_rsi)), v_stack_mC8);
    result = IoSaveBugCheckProgress(32, Arg2, (uint32_t)((uint32_t)(local_rsi)), v_stack_mC8);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x8D27A6) + 0x18) = (uint32_t)((uint32_t)(Arg1));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D277D) + 0x20) = 0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D2772) + 0x28) = v_stack_mB8;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D2767) + 0x30) = v_stack_mC8;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D275C) + 0x38) = Arg5;
    result = (*(uint64_t *)(v_rip + 0x8D2751)) + (64);
loc_00593903:
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    *(uint64_t *)(result + 0x40) = v_xmm0;
    *(uint64_t *)(result + 0x50) = v_xmm1;
    *(uint64_t *)(result + 0x60) = v_xmm0;
    result = (result) + (9 + 119);
    Arg1 = (v_stack_mD0) + (9 + 119);
    *(uint64_t *)(result - 0x10) = v_xmm1;
    Arg2 = (9) - (1);
    if (condition_is_not_equal) goto loc_00593903;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    *(uint64_t *)(result + 0x40) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D26CB) + 0x510) = v_rip + 8836838;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D26B6) + 0x518) = v_rip + 9907757;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D26A1) + 0x520) = v_rip + 9837336;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D2693) + 0x528) = *(uint64_t *)(v_rip + 0xA33274);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D2677) + 0x10) = v_rip + 10025678;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D2665) + 0x588) = v_rip + 10025644;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x8D2657) + 0x598) = 4;
    if (Arg8 == 0) goto loc_00593A12;
    goto loc_00593A15;
loc_00593A12:
loc_00593A15:
    Arg1 = (v_cr3) & (0xFFFFFFFFFFFFF000ULL);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D2634) + 0x540) = Arg1;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8D261F) + 0x530) != 0) goto loc_00593A4C;
    if (((uint8_t)((uint8_t)(result))) != 1) goto loc_00593A52;
    if (Arg8 != 0) goto loc_00593B05;
loc_00593A4C:
    if (((uint8_t)((uint8_t)(result))) == 1) goto loc_00593A78;
loc_00593A52:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8D261F) + 0x550) == 0) goto loc_00593A78;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8D261F) + 0x550)) + (0x301CULL);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D261F) + 0x530) = result;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D25DE) + 0x8) = 0;
    goto loc_00593A96;
loc_00593A78:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8D261F) + 0x530) != 0) goto loc_00593A96;
    result = *(uint64_t *)(v_rip + 0x8D25DE);
    if (Arg8 == 0) {
        result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D261F) + 0x550);
        result = (result) + (0x2000ULL);
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D261F) + 0x530) = result;
    }
    if (*(uint64_t *)(v_rip + 0x8D2444) != 0) goto loc_00593AE9;
    v_stack_mE0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D25B3) + 0x530);
    v_stack_mF0 = (uint8_t)(v_stack_mD8);
    v_stack_mF8 = v_stack_mC0;
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = Arg5;
    result = IopCollectTriageDumpData((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, v_stack_mB8, v_stack_mC8);
    if (sign_flag) goto loc_00593E2A;
    goto loc_00593AF7;
loc_00593AE9:
    if (Arg2 == ((uint32_t)((uint32_t)((uint32_t)(Arg1))))) goto loc_00593B05;
    result = memcpy((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, (uint32_t)(*(uint32_t *)(Arg2 + 0x4)), v_stack_mC8);
loc_00593AF7:
loc_00593B05:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8D2544) + 0x558))))) & (2));
    if (condition_is_equal) goto loc_00593B5C;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x8D2544) + 0x538)) != 6) goto loc_00593B5C;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x8D2544) + 0x8)) == 0) goto loc_00593B5C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8D2544) + 0x558))) | (4));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x8D2544) + 0x558) = (uint32_t)(result);
    v_stack_mF8 = v_stack_mC0;
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = Arg5;
    result = IoAddPagesForPartialKernelDump((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, v_stack_mB8, v_stack_mC8);
    goto loc_00593C2E;
loc_00593B5C:
    if (*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(Arg1))) + 0x8) == 0) goto loc_00593C2A;
    v_stack_m80 = 0;
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(Arg1))) + 0x8) + 0x30);
    v_stack_m70 = *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(Arg1))) + 0x8) + 56;
    v_stack_m98 = v_stack_m78;
    v_stack_mA8 = v_rip - 2466;
    v_stack_mA0 = v_rip - 5101;
    v_stack_m90 = *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(Arg1))) + 0x8);
    v_stack_m88 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)(Arg1))) + 0x538)))) != 6) goto loc_00593BC6;
    result = (Arg9 != 0) ? 1 : 0;
    v_stack_mD4 = (uint32_t)(result);
    goto loc_00593BD7;
loc_00593BC6:
    if (((uint32_t)(result)) != 5) goto loc_00593BDA;
    if ((uint32_t)(Arg2) == 0) goto loc_00593BDA;
    v_stack_mD4 = 2;
loc_00593BD7:
loc_00593BDA:
    result = IopDumpCallAddPagesCallbacks((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, v_stack_mB8, v_stack_mC8);
    result = IoSaveBugCheckProgress(33, Arg2, v_stack_mB8, v_stack_mC8);
    result = MmGetDumpRange(v_stack_mA8, 0, (uint32_t)(v_stack_mD4), v_stack_mC8);
    result = IoSaveBugCheckProgress(43, 0, (uint32_t)(v_stack_mD4), v_stack_mC8);
    result = IopDumpCallRemovePagesCallbacks((uint32_t)((uint32_t)((uint32_t)(Arg1))), 0, (uint32_t)(v_stack_mD4), v_stack_mC8);
    result = IoSaveBugCheckProgress(34, 0, (uint32_t)(v_stack_mD4), v_stack_mC8);
    result = RtlNumberOfSetBitsEx(v_stack_m78, 0, (uint32_t)(v_stack_mD4), v_stack_mC8);
    *(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(Arg1))) + 0x8) + 0x28) = result;
loc_00593C2A:
loc_00593C2E:
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        result = *(uint64_t *)(v_rip + 0x8D23CF);
        Arg2 = Arg8;
        Arg1 = *(uint64_t *)(v_rip + 0x8D240D);
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)(v_stack_mD4), v_stack_mC8);
        local_rbx = (uint32_t)(result);
    }
    if (((uint32_t)(local_rbx)) != 0xC000022DULL) goto loc_00593D68;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8D23F3) + 0x558)))) & (4)) == 0) goto loc_00593CD8;
    result = IoSaveBugCheckProgress(39, Arg2, (uint32_t)(v_stack_mD4), v_stack_mC8);
    v_stack_mF8 = v_stack_mC0;
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = Arg5;
    result = IoAddPagesForPartialKernelDump((uint32_t)((uint32_t)((uint32_t)(Arg1))), v_stack_mB0, v_stack_mB8, v_stack_mC8);
    if (sign_flag) goto loc_00593D68;
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0x8D2387), Arg8, v_stack_mB8, v_stack_mC8);
    goto loc_00593D61;
loc_00593CD8:
    if ((*(uint64_t *)(38 + 0x530)) == 0) goto loc_00593D68;
    result = IoSetBugCheckProgressFlag((uint32_t)(0x400ULL), Arg8, v_stack_mB8, v_stack_mC8);
    *(uint64_t *)(v_rip + 0x8D21E0) = 0;
    v_stack_mE0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D235A) + 0x530);
    v_stack_mF0 = (uint8_t)(v_stack_mD8);
    v_stack_mF8 = v_stack_mC0;
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = Arg5;
    result = IopCollectTriageDumpData((uint32_t)((uint32_t)((uint32_t)(Arg1))), v_stack_mB0, v_stack_mB8, v_stack_mC8);
    if (sign_flag) goto loc_00593D68;
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0x8D22F9), Arg8, v_stack_mB8, v_stack_mC8);
loc_00593D61:
    result = IoSaveBugCheckProgress(35, Arg8, v_stack_mB8, v_stack_mC8);
loc_00593D68:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8D218E)))) & (1)) == 0) goto loc_00593D76;
    if (sign_flag) goto loc_00593D7F;
loc_00593D76:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8D218E)))) & (2)) == 0) goto loc_00593DBB;
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_00593DBB;
loc_00593D7F:
    result = IoSaveBugCheckProgress(36, Arg8, v_stack_mB8, v_stack_mC8);
    Arg1 = 0;
    result = guard_dispatch_icall(Arg1, Arg8, v_stack_mB8, v_stack_mC8);
    if (sign_flag) goto loc_00593E2A;
    result = IoSetBugCheckProgressFlag((uint32_t)(0x1000ULL), Arg8, v_stack_mB8, v_stack_mC8);
loc_00593DA9:
    result = KeStallExecutionProcessor((uint32_t)(0xF4240ULL), Arg8, v_stack_mB8, v_stack_mC8);
    goto loc_00593DA9;
loc_00593DBB:
    if (sign_flag) goto loc_00593E2A;
    if (((uint8_t)((uint8_t)(result))) == 1) goto loc_00593E27;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x8D2284) + 0x550)) == 0) goto loc_00593E27;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8D2284) + 0x57C));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8D2284) + 0x57C)))) & (0x860000ULL)) == 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8D2284) + 0x57C))) & (0xFFFFFE25ULL));
        result = (uint32_t)((result) | (37));
        *(uint32_t *)(*(uint64_t *)(v_rip + 0x8D2284) + 0x57C) = (uint32_t)(result);
    }
    result = IoUpdateBugCheckProgressEnvVariable(*(uint64_t *)(v_rip + 0x8D2284), Arg8, v_stack_mB8, v_stack_mC8);
    result = IopWriteTriageDumpToFirmware(*(uint64_t *)(*(uint64_t *)(v_rip + 0x8D2245) + 0x550), Arg8, v_stack_mB8, v_stack_mC8);
    result = IoSetBugCheckProgressFlag((uint32_t)(0x10000000ULL), Arg8, v_stack_mB8, v_stack_mC8);
    if (!(sign_flag)) {
        local_rdi = 1;
    }
loc_00593E2D:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg8, v_stack_mB8, v_stack_mC8);
    local_rsp = (local_rsp) + (232);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005936D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
