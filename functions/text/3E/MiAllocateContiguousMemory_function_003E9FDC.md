# MiAllocateContiguousMemory

- RVA: `0x003E9FDC`–`0x003EA650` (길이 `1,652` bytes)
- VA: `0x00000001403E9FDC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000958EC`
- 디코드: `389`개 명령, `1,652/1,652` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x003EA042` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003EA049` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x003EA0D4` → [MiProtectionToCacheAttribute](../2B/MiProtectionToCacheAttribute_function_002B8530.md) (function, `0x002B8530`)
- `0x003EA159` → [MiFreeContiguousPages](../3F/MiFreeContiguousPages_function_003F7178.md) (function, `0x003F7178`)
- `0x003EA1C8` → [ExAllocateContiguousHeapPool](../2E/ExAllocateContiguousHeapPool_function_002EE960.md) (function, `0x002EE960`)
- `0x003EA263` → [MiFindContiguousPagesEx](../28/MiFindContiguousPagesEx_function_0028BDE0.md) (function, `0x0028BDE0`)
- `0x003EA2A3` → [MiMapContiguousMemory](../32/MiMapContiguousMemory_function_0032787C.md) (function, `0x0032787C`)
- `0x003EA335` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003EA37C` → [VfPtIsAptEnabledOnKernel](VfPtIsAptEnabledOnKernel_function_003EA660.md) (function, `0x003EA660`)
- `0x003EA3D5` → [EtwTraceContAllocationEvent](EtwTraceContAllocationEvent_function_003EA680.md) (function, `0x003EA680`)
- `0x003EA3E4` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003EA4AF` → [ExInsertPoolTag](../2E/ExInsertPoolTag_function_002EF3AC.md) (function, `0x002EF3AC`)
- `0x003EA4E3` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003EA51F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x003EA5C3` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003EA5D3` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003EA615` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003EA62C` → [MiLogPerfMemoryRangeEvent](../4D/MiLogPerfMemoryRangeEvent_function_004D9D7C.md) (function, `0x004D9D7C`)
- `0x003EA646` → [VfPtMiscPoolNotification](../3F/VfPtMiscPoolNotification_function_003FF310.md) (function, `0x003FF310`)

### Direct callers
- [MmAllocateContiguousMemoryEx](MmAllocateContiguousMemoryEx_function_003E9B80.md) at `0x003E9C84`
- [MmAllocateContiguousNodeMemory](MmAllocateContiguousNodeMemory_function_003E9E40.md) at `0x003E9ED0`
- [MmAllocateContiguousMemory](../67/MmAllocateContiguousMemory_function_006744C0.md) at `0x00674512`

### Static image references
- `0x003E9FF5` → RVA `0x00E0A740` (`.data`; read)
- `0x003EA05D` → RVA `0x00FC6C14` (`ALMOSTRO`; read)
- `0x003EA0D9` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x003EA113` → RVA `0x00E2DBD0` (`.data`; read)
- `0x003EA16F` → RVA `0x00E38D00` (`.data`; read)
- `0x003EA308` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003EA34B` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x003EA41F` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x003EA4F0` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003EA560` → RVA `0x00E2DCE0` (`.data`; read)
- `0x003EA58B` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x003EA5B5` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x003EA51F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x003EA4C1` → [sub_006EACA8](../6E/Unknown_function_006EACA8.md) (`tail-transfer`)
  - `0x003EA4CE` → [sub_006EACA8](../6E/Unknown_function_006EACA8.md) (`tail-transfer`)
  - `0x003EA608` → [sub_006EACA8 + 0x17](../6E/Unknown_function_006EACA8.md) (`tail-transfer`)
  - `0x003EA61B` → [sub_006EACA8 + 0x17](../6E/Unknown_function_006EACA8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003E9FDC  40 55                           push rbp
003E9FDE  53                              push rbx
003E9FDF  56                              push rsi
003E9FE0  57                              push rdi
003E9FE1  41 54                           push r12
003E9FE3  41 55                           push r13
003E9FE5  41 56                           push r14
003E9FE7  41 57                           push r15
003E9FE9  48 8D 6C 24 A8                  lea rbp, [rsp - 0x58]
003E9FEE  48 81 EC 58 01 00 00            sub rsp, 0x158
003E9FF5  48 8B 05 44 07 A2 00            mov rax, qword ptr [rip + 0xa20744]
003E9FFC  48 33 C4                        xor rax, rsp
003E9FFF  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
003EA003  48 8B 85 D0 00 00 00            mov rax, qword ptr [rbp + 0xd0]
003EA00A  4C 8B EA                        mov r13, rdx
003EA00D  8B 9D C8 00 00 00               mov ebx, dword ptr [rbp + 0xc8]
003EA013  4C 8B F9                        mov r15, rcx
003EA016  44 8B B5 C0 00 00 00            mov r14d, dword ptr [rbp + 0xc0]
003EA01D  8B F3                           mov esi, ebx
003EA01F  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
003EA023  33 D2                           xor edx, edx
003EA025  4C 89 45 A8                     mov qword ptr [rbp - 0x58], r8
003EA029  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
003EA02D  48 8D 4D E0                     lea rcx, [rbp - 0x20]
003EA031  4C 89 4D 98                     mov qword ptr [rbp - 0x68], r9
003EA035  44 8D 42 58                     lea r8d, [rdx + 0x58]
003EA039  44 89 74 24 74                  mov dword ptr [rsp + 0x74], r14d
003EA03E  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
003EA042  E8 F9 CB 2D 00                  call 0x1406c6c40
003EA047  33 C9                           xor ecx, ecx
003EA049  E8 92 47 F9 FF                  call 0x14037e7e0
003EA04E  48 83 4D A0 FF                  or qword ptr [rbp - 0x60], 0xffffffffffffffff
003EA053  45 33 E4                        xor r12d, r12d
003EA056  4C 21 65 C0                     and qword ptr [rbp - 0x40], r12
003EA05A  45 33 C0                        xor r8d, r8d
003EA05D  44 39 05 B0 CB BD 00            cmp dword ptr [rip + 0xbdcbb0], r8d
003EA064  48 8B F8                        mov rdi, rax
003EA067  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
003EA06B  49 8B 07                        mov rax, qword ptr [r15]
003EA06E  41 0F 95 C0                     setne r8b
003EA072  48 A9 FF 0F 00 00               test rax, 0xfff
003EA078  C6 44 24 70 00                  mov byte ptr [rsp + 0x70], 0
003EA07D  45 8B FC                        mov r15d, r12d
003EA080  44 89 44 24 78                  mov dword ptr [rsp + 0x78], r8d
003EA085  41 0F 95 C7                     setne r15b
003EA089  48 C1 E8 0C                     shr rax, 0xc
003EA08D  4C 03 F8                        add r15, rax
003EA090  41 8D 44 24 02                  lea eax, [r12 + 2]
003EA095  44 84 F0                        test al, r14b
003EA098  0F 85 81 03 00 00               jne 0x1403ea41f
003EA09E  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
003EA0A2  4D 85 DB                        test r11, r11
003EA0A5  0F 85 53 03 00 00               jne 0x1403ea3fe
003EA0AB  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
003EA0AF  4C 3B E9                        cmp r13, rcx
003EA0B2  0F 87 4F 03 00 00               ja 0x1403ea407
003EA0B8  4B 8D 04 2F                     lea rax, [r15 + r13]
003EA0BC  49 3B C5                        cmp rax, r13
003EA0BF  0F 86 42 03 00 00               jbe 0x1403ea407
003EA0C5  48 FF C8                        dec rax
003EA0C8  48 3B C1                        cmp rax, rcx
003EA0CB  0F 87 36 03 00 00               ja 0x1403ea407
003EA0D1  41 8B CE                        mov ecx, r14d
003EA0D4  E8 57 E4 EC FF                  call 0x1402b8530
003EA0D9  0F B7 0D 20 AF BD 00            movzx ecx, word ptr [rip + 0xbdaf20]
003EA0E0  44 8B C8                        mov r9d, eax
003EA0E3  89 45 88                        mov dword ptr [rbp - 0x78], eax
003EA0E6  41 BD 00 00 00 80               mov r13d, 0x80000000
003EA0EC  B8 01 00 00 00                  mov eax, 1
003EA0F1  66 3B C8                        cmp cx, ax
003EA0F4  0F 87 76 04 00 00               ja 0x1403ea570
003EA0FA  45 33 D2                        xor r10d, r10d
003EA0FD  44 89 95 C8 00 00 00            mov dword ptr [rbp + 0xc8], r10d
003EA104  41 8B DA                        mov ebx, r10d
003EA107  44 3B D1                        cmp r10d, ecx
003EA10A  73 52                           jae 0x1403ea15e
003EA10C  0F B7 15 ED AE BD 00            movzx edx, word ptr [rip + 0xbdaeed]
003EA113  48 8B 05 B6 3A A4 00            mov rax, qword ptr [rip + 0xa43ab6]
003EA11A  8B CA                           mov ecx, edx
003EA11C  0F AF CB                        imul ecx, ebx
003EA11F  45 3B D5                        cmp r10d, r13d
003EA122  4C 8D 34 88                     lea r14, [rax + rcx*4]
003EA126  4D 8D 2C 96                     lea r13, [r14 + rdx*4]
003EA12A  75 3D                           jne 0x1403ea169
003EA12C  F6 44 24 74 02                  test byte ptr [rsp + 0x74], 2
003EA131  4C 8B 55 80                     mov r10, qword ptr [rbp - 0x80]
003EA135  4C 89 6D B8                     mov qword ptr [rbp - 0x48], r13
003EA139  74 34                           je 0x1403ea16f
003EA13B  F6 85 E0 00 00 00 01            test byte ptr [rbp + 0xe0], 1
003EA142  0F 84 AB 00 00 00               je 0x1403ea1f3
003EA148  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
003EA14C  48 83 F9 FF                     cmp rcx, -1
003EA150  74 0C                           je 0x1403ea15e
003EA152  48 8B 55 C0                     mov rdx, qword ptr [rbp - 0x40]
003EA156  45 33 C0                        xor r8d, r8d
003EA159  E8 1A D0 00 00                  call 0x1403f7178
003EA15E  8B 9D C8 00 00 00               mov ebx, dword ptr [rbp + 0xc8]
003EA164  E9 9E 02 00 00                  jmp 0x1403ea407
003EA169  4D 8D 6E 04                     lea r13, [r14 + 4]
003EA16D  EB BD                           jmp 0x1403ea12c
003EA16F  48 8D 05 8A EB A4 00            lea rax, [rip + 0xa4eb8a]
003EA176  4C 3B D0                        cmp r10, rax
003EA179  75 C0                           jne 0x1403ea13b
003EA17B  45 85 C0                        test r8d, r8d
003EA17E  75 BB                           jne 0x1403ea13b
003EA180  41 83 F9 01                     cmp r9d, 1
003EA184  75 B5                           jne 0x1403ea13b
003EA186  49 81 FF 00 02 00 00            cmp r15, 0x200
003EA18D  77 AC                           ja 0x1403ea13b
003EA18F  81 BD D8 00 00 00 43 6F 6E 54   cmp dword ptr [rbp + 0xd8], 0x546e6f43
003EA199  41 BC 43 6F 6E 74               mov r12d, 0x746e6f43
003EA19F  49 8B F7                        mov rsi, r15
003EA1A2  44 0F 45 A5 D8 00 00 00         cmovne r12d, dword ptr [rbp + 0xd8]
003EA1AA  48 C1 E6 0C                     shl rsi, 0xc
003EA1AE  41 8B 06                        mov eax, dword ptr [r14]
003EA1B1  4C 8B CE                        mov r9, rsi
003EA1B4  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
003EA1B8  4D 8B C3                        mov r8, r11
003EA1BB  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
003EA1BF  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
003EA1C4  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003EA1C8  E8 93 47 F0 FF                  call 0x1402ee960
003EA1CD  48 85 C0                        test rax, rax
003EA1D0  0F 85 FD 02 00 00               jne 0x1403ea4d3
003EA1D6  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
003EA1DA  49 83 C6 04                     add r14, 4
003EA1DE  4D 3B F5                        cmp r14, r13
003EA1E1  75 CB                           jne 0x1403ea1ae
003EA1E3  44 8B 4D 88                     mov r9d, dword ptr [rbp - 0x78]
003EA1E7  4C 8B E0                        mov r12, rax
003EA1EA  4C 8B 55 80                     mov r10, qword ptr [rbp - 0x80]
003EA1EE  E9 48 FF FF FF                  jmp 0x1403ea13b
003EA1F3  0F B7 0D 06 AE BD 00            movzx ecx, word ptr [rip + 0xbdae06]
003EA1FA  41 BE 00 00 10 08               mov r14d, 0x8100000
003EA200  48 8B 05 C9 39 A4 00            mov rax, qword ptr [rip + 0xa439c9]
003EA207  0F AF CB                        imul ecx, ebx
003EA20A  48 8D 34 88                     lea rsi, [rax + rcx*4]
003EA20E  33 DB                           xor ebx, ebx
003EA210  4D 3B DF                        cmp r11, r15
003EA213  0F 84 10 03 00 00               je 0x1403ea529
003EA219  8B 06                           mov eax, dword ptr [rsi]
003EA21B  48 8D 4D A0                     lea rcx, [rbp - 0x60]
003EA21F  4C 8B 45 A8                     mov r8, qword ptr [rbp - 0x58]
003EA223  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
003EA227  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
003EA22C  49 8B CA                        mov rcx, r10
003EA22F  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
003EA234  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
003EA23A  C7 44 24 50 02 00 00 00         mov dword ptr [rsp + 0x50], 2
003EA242  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
003EA247  C6 44 24 40 FF                  mov byte ptr [rsp + 0x40], 0xff
003EA24C  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
003EA250  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
003EA255  4D 8B CB                        mov r9, r11
003EA258  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
003EA25D  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
003EA263  E8 78 1B EA FF                  call 0x14028bde0
003EA268  44 8B E8                        mov r13d, eax
003EA26B  48 85 DB                        test rbx, rbx
003EA26E  0F 85 99 02 00 00               jne 0x1403ea50d
003EA274  45 85 ED                        test r13d, r13d
003EA277  0F 88 60 03 00 00               js 0x1403ea5dd
003EA27D  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
003EA281  49 8B F7                        mov rsi, r15
003EA284  8B 5C 24 78                     mov ebx, dword ptr [rsp + 0x78]
003EA288  44 8B 4C 24 74                  mov r9d, dword ptr [rsp + 0x74]
003EA28D  48 C1 E6 0C                     shl rsi, 0xc
003EA291  4C 8B C6                        mov r8, rsi
003EA294  48 C1 E1 0C                     shl rcx, 0xc
003EA298  48 8B D6                        mov rdx, rsi
003EA29B  4C 89 7D C0                     mov qword ptr [rbp - 0x40], r15
003EA29F  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
003EA2A3  E8 D4 D5 F3 FF                  call 0x14032787c
003EA2A8  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
003EA2AC  4C 8B E0                        mov r12, rax
003EA2AF  48 85 C0                        test rax, rax
003EA2B2  0F 85 E7 01 00 00               jne 0x1403ea49f
003EA2B8  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
003EA2BC  4C 8D 34 40                     lea r14, [rax + rax*2]
003EA2C0  49 C1 E6 04                     shl r14, 4
003EA2C4  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003EA2CE  4C 03 F0                        add r14, rax
003EA2D1  4D 85 E4                        test r12, r12
003EA2D4  0F 84 3E 01 00 00               je 0x1403ea418
003EA2DA  49 8B DC                        mov rbx, r12
003EA2DD  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003EA2E7  48 C1 EB 09                     shr rbx, 9
003EA2EB  48 23 D8                        and rbx, rax
003EA2EE  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003EA2F8  48 03 D8                        add rbx, rax
003EA2FB  45 0F 20 C5                     mov r13, cr8
003EA2FF  B8 02 00 00 00                  mov eax, 2
003EA304  44 0F 22 C0                     mov cr8, rax
003EA308  83 3D 11 CA BD 00 00            cmp dword ptr [rip + 0xbdca11], 0
003EA30F  0F 85 C9 01 00 00               jne 0x1403ea4de
003EA315  33 C9                           xor ecx, ecx
003EA317  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
003EA31C  4D 85 FF                        test r15, r15
003EA31F  0F 85 19 01 00 00               jne 0x1403ea43e
003EA325  83 3D F4 C9 BD 00 00            cmp dword ptr [rip + 0xbdc9f4], 0
003EA32C  74 0C                           je 0x1403ea33a
003EA32E  44 0F 20 C1                     mov rcx, cr8
003EA332  41 8A D5                        mov dl, r13b
003EA335  E8 5E B3 10 00                  call 0x1404f5698
003EA33A  41 0F B6 C5                     movzx eax, r13b
003EA33E  44 0F 22 C0                     mov cr8, rax
003EA342  4D 85 E4                        test r12, r12
003EA345  0F 84 FD FD FF FF               je 0x1403ea148
003EA34B  8B 05 B3 C7 BD 00               mov eax, dword ptr [rip + 0xbdc7b3]
003EA351  A8 01                           test al, 1
003EA353  0F 85 C7 02 00 00               jne 0x1403ea620
003EA359  44 8A 6C 24 70                  mov r13b, byte ptr [rsp + 0x70]
003EA35E  45 84 ED                        test r13b, r13b
003EA361  75 0C                           jne 0x1403ea36f
003EA363  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
003EA367  F0 4C 01 B8 C8 4C 00 00         lock add qword ptr [rax + 0x4cc8], r15
003EA36F  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
003EA373  8B 9D C8 00 00 00               mov ebx, dword ptr [rbp + 0xc8]
003EA379  49 89 36                        mov qword ptr [r14], rsi
003EA37C  E8 DF 02 00 00                  call 0x1403ea660
003EA381  84 C0                           test al, al
003EA383  0F 85 AD 02 00 00               jne 0x1403ea636
003EA389  8B 8D E0 00 00 00               mov ecx, dword ptr [rbp + 0xe0]
003EA38F  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
003EA393  4C 8B 4D 98                     mov r9, qword ptr [rbp - 0x68]
003EA397  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
003EA39B  49 8B 16                        mov rdx, qword ptr [r14]
003EA39E  0F B7 00                        movzx eax, word ptr [rax]
003EA3A1  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
003EA3A6  44 88 6C 24 50                  mov byte ptr [rsp + 0x50], r13b
003EA3AB  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
003EA3AF  8B 8D D8 00 00 00               mov ecx, dword ptr [rbp + 0xd8]
003EA3B5  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
003EA3B9  49 8B CC                        mov rcx, r12
003EA3BC  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
003EA3C0  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
003EA3C4  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
003EA3C8  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
003EA3CC  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
003EA3D1  4C 8B 4D A8                     mov r9, qword ptr [rbp - 0x58]
003EA3D5  E8 A6 02 00 00                  call 0x1403ea680
003EA3DA  49 8B C4                        mov rax, r12
003EA3DD  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
003EA3E1  48 33 CC                        xor rcx, rsp
003EA3E4  E8 57 22 2C 00                  call 0x1406ac640
003EA3E9  48 81 C4 58 01 00 00            add rsp, 0x158
003EA3F0  41 5F                           pop r15
003EA3F2  41 5E                           pop r14
003EA3F4  41 5D                           pop r13
003EA3F6  41 5C                           pop r12
003EA3F8  5F                              pop rdi
003EA3F9  5E                              pop rsi
003EA3FA  5B                              pop rbx
003EA3FB  5D                              pop rbp
003EA3FC  C3                              ret
003EA3FD  CC                              int3
003EA3FE  4D 3B FB                        cmp r15, r11
003EA401  0F 86 A4 FC FF FF               jbe 0x1403ea0ab
003EA407  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
003EA40B  44 8A 6C 24 70                  mov r13b, byte ptr [rsp + 0x70]
003EA410  49 8B 36                        mov rsi, qword ptr [r14]
003EA413  E9 64 FF FF FF                  jmp 0x1403ea37c
003EA418  33 DB                           xor ebx, ebx
003EA41A  E9 DC FE FF FF                  jmp 0x1403ea2fb
003EA41F  48 F7 05 5E C6 BD 00 00 80 00 00  test qword ptr [rip + 0xbdc65e], 0x8000
003EA42A  0F 84 6E FC FF FF               je 0x1403ea09e
003EA430  41 83 E6 FD                     and r14d, 0xfffffffd
003EA434  44 89 74 24 74                  mov dword ptr [rsp + 0x74], r14d
003EA439  E9 60 FC FF FF                  jmp 0x1403ea09e
003EA43E  49 83 C6 18                     add r14, 0x18
003EA442  BF 02 00 00 00                  mov edi, 2
003EA447  45 33 E4                        xor r12d, r12d
003EA44A  F0 49 0F BA 2E 3F               lock bts qword ptr [r14], 0x3f
003EA450  0F 82 97 00 00 00               jb 0x1403ea4ed
003EA456  49 89 5E F0                     mov qword ptr [r14 - 0x10], rbx
003EA45A  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003EA464  F0 49 21 06                     lock and qword ptr [r14], rax
003EA468  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
003EA46D  48 FF C0                        inc rax
003EA470  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
003EA475  48 8B C8                        mov rcx, rax
003EA478  A8 3F                           test al, 0x3f
003EA47A  0F 84 81 01 00 00               je 0x1403ea601
003EA480  49 83 C6 30                     add r14, 0x30
003EA484  48 85 DB                        test rbx, rbx
003EA487  74 04                           je 0x1403ea48d
003EA489  48 83 C3 08                     add rbx, 8
003EA48D  49 3B CF                        cmp rcx, r15
003EA490  72 B5                           jb 0x1403ea447
003EA492  48 8B 7D D0                     mov rdi, qword ptr [rbp - 0x30]
003EA496  4C 8B 65 90                     mov r12, qword ptr [rbp - 0x70]
003EA49A  E9 86 FE FF FF                  jmp 0x1403ea325
003EA49F  8B 8D D8 00 00 00               mov ecx, dword ptr [rbp + 0xd8]
003EA4A5  4C 8B C6                        mov r8, rsi
003EA4A8  49 8B D4                        mov rdx, r12
003EA4AB  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
003EA4AF  E8 F8 4E F0 FF                  call 0x1402ef3ac
003EA4B4  85 C0                           test eax, eax
003EA4B6  0F 85 FC FD FF FF               jne 0x1403ea2b8
003EA4BC  48 8B D6                        mov rdx, rsi
003EA4BF  85 DB                           test ebx, ebx
003EA4C1  0F 84 E1 07 30 00               je 0x1406eaca8
003EA4C7  48 81 C2 00 10 00 00            add rdx, 0x1000
003EA4CE  E9 D5 07 30 00                  jmp 0x1406eaca8
003EA4D3  41 B5 01                        mov r13b, 1
003EA4D6  4C 8B E0                        mov r12, rax
003EA4D9  E9 80 FE FF FF                  jmp 0x1403ea35e
003EA4DE  8A D0                           mov dl, al
003EA4E0  41 8A CD                        mov cl, r13b
003EA4E3  E8 14 B2 10 00                  call 0x1404f56fc
003EA4E8  E9 28 FE FF FF                  jmp 0x1403ea315
003EA4ED  41 FF C4                        inc r12d
003EA4F0  44 85 25 B5 AD BD 00            test dword ptr [rip + 0xbdadb5], r12d
003EA4F7  0F 84 B8 00 00 00               je 0x1403ea5b5
003EA4FD  F3 90                           pause
003EA4FF  49 8B 06                        mov rax, qword ptr [r14]
003EA502  48 85 C0                        test rax, rax
003EA505  0F 89 3F FF FF FF               jns 0x1403ea44a
003EA50B  EB E0                           jmp 0x1403ea4ed
003EA50D  48 8D 45 E0                     lea rax, [rbp - 0x20]
003EA511  48 3B D8                        cmp rbx, rax
003EA514  0F 84 5A FD FF FF               je 0x1403ea274
003EA51A  33 D2                           xor edx, edx
003EA51C  48 8B CB                        mov rcx, rbx
003EA51F  E8 4C 83 79 00                  call 0x140b82870
003EA524  E9 4B FD FF FF                  jmp 0x1403ea274
003EA529  49 83 FF 10                     cmp r15, 0x10
003EA52D  74 16                           je 0x1403ea545
003EA52F  49 81 FF 00 02 00 00            cmp r15, 0x200
003EA536  74 0D                           je 0x1403ea545
003EA538  49 81 FF 00 00 04 00            cmp r15, 0x40000
003EA53F  0F 85 D4 FC FF FF               jne 0x1403ea219
003EA545  48 83 65 E4 00                  and qword ptr [rbp - 0x1c], 0
003EA54A  49 8D 47 FF                     lea rax, [r15 - 1]
003EA54E  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
003EA552  48 8D 5D E0                     lea rbx, [rbp - 0x20]
003EA556  48 F7 D0                        not rax
003EA559  C7 45 E0 08 00 00 00            mov dword ptr [rbp - 0x20], 8
003EA560  48 23 05 79 37 A4 00            and rax, qword ptr [rip + 0xa43779]
003EA567  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
003EA56B  E9 A9 FC FF FF                  jmp 0x1403ea219
003EA570  89 B5 C8 00 00 00               mov dword ptr [rbp + 0xc8], esi
003EA576  44 8B D6                        mov r10d, esi
003EA579  41 3B F5                        cmp esi, r13d
003EA57C  0F 85 82 FB FF FF               jne 0x1403ea104
003EA582  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003EA58B  48 8D 0D AE E6 BD 00            lea rcx, [rip + 0xbde6ae]
003EA592  89 B5 C8 00 00 00               mov dword ptr [rbp + 0xc8], esi
003EA598  8B 80 4C 02 00 00               mov eax, dword ptr [rax + 0x24c]
003EA59E  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
003EA5A2  48 8B 88 C0 00 00 00            mov rcx, qword ptr [rax + 0xc0]
003EA5A9  0F B7 99 8A 00 00 00            movzx ebx, word ptr [rcx + 0x8a]
003EA5B0  E9 57 FB FF FF                  jmp 0x1403ea10c
003EA5B5  8B 05 FD C4 BD 00               mov eax, dword ptr [rip + 0xbdc4fd]
003EA5BB  A8 40                           test al, 0x40
003EA5BD  0F 84 3A FF FF FF               je 0x1403ea4fd
003EA5C3  E8 C8 4E F2 FF                  call 0x14030f490
003EA5C8  84 C0                           test al, al
003EA5CA  0F 84 2D FF FF FF               je 0x1403ea4fd
003EA5D0  41 8B CC                        mov ecx, r12d
003EA5D3  E8 88 4E F2 FF                  call 0x14030f460
003EA5D8  E9 22 FF FF FF                  jmp 0x1403ea4ff
003EA5DD  48 83 C6 04                     add rsi, 4
003EA5E1  48 3B 75 B8                     cmp rsi, qword ptr [rbp - 0x48]
003EA5E5  0F 84 5D FB FF FF               je 0x1403ea148
003EA5EB  44 8B 4D 88                     mov r9d, dword ptr [rbp - 0x78]
003EA5EF  41 0F BA F6 1B                  btr r14d, 0x1b
003EA5F4  4C 8B 5D 98                     mov r11, qword ptr [rbp - 0x68]
003EA5F8  4C 8B 55 80                     mov r10, qword ptr [rbp - 0x80]
003EA5FC  E9 0D FC FF FF                  jmp 0x1403ea20e
003EA601  83 3D 18 C7 BD 00 00            cmp dword ptr [rip + 0xbdc718], 0
003EA608  0F 84 B1 06 30 00               je 0x1406eacbf
003EA60E  44 0F 20 C1                     mov rcx, cr8
003EA612  41 8A D5                        mov dl, r13b
003EA615  E8 7E B0 10 00                  call 0x1404f5698
003EA61A  90                              nop
003EA61B  E9 9F 06 30 00                  jmp 0x1406eacbf
003EA620  33 D2                           xor edx, edx
003EA622  4D 8B CF                        mov r9, r15
003EA625  49 8B CC                        mov rcx, r12
003EA628  44 8D 42 0D                     lea r8d, [rdx + 0xd]
003EA62C  E8 4B F7 0E 00                  call 0x1404d9d7c
003EA631  E9 23 FD FF FF                  jmp 0x1403ea359
003EA636  44 8B 85 D8 00 00 00            mov r8d, dword ptr [rbp + 0xd8]
003EA63D  45 33 C9                        xor r9d, r9d
003EA640  48 8B D6                        mov rdx, rsi
003EA643  49 8B CC                        mov rcx, r12
003EA646  E8 C5 4C 01 00                  call 0x1403ff310
003EA64B  E9 39 FD FF FF                  jmp 0x1403ea389
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateContiguousMemory(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, __int64 a7, unsigned int a8, unsigned __int8 a9)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned int v_stack_m124;
    unsigned __int8 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int8 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned int v_stack_m168;
    unsigned int v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned __int64 v_stack_mB4;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p70;
    unsigned int v_stack_p74;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (344);
    result = (*(unsigned __int64 *)(v_rip + 10618692)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_mE8 = a2;
    a2 = 0;
    v_stack_mF0 = a3;
    v_stack_mD0 = a1;
    v_stack_m100 = a4;
    v_stack_m124 = (unsigned int)((unsigned int)(a5));
    v_stack_m118 = a7;
    result = memset(v_stack_mB8, a2, a2 + 88, a4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a2 + 88, a4);
    v_r12 = 0;
    a3 = 0;
    v_stack_mC8 = result;
    a3 = ((*(unsigned int *)(v_rip + 12438448)) != 0) ? 1 : 0;
    v_stack_m128 = 0;
    v_stack_m120 = (unsigned int)(a3);
    v_r15 = (((*(unsigned __int64 *)(a1)) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (*(unsigned __int64 *)(a1)) >> (12);
    v_r15 = (v_r15) + (result);
    if ((((unsigned __int8)(v_r12 + 2)) & ((unsigned __int8)((unsigned int)(a5)))) != 0) goto loc_003EA41F;
loc_003EA09E:
    if (v_stack_m100 != 0) goto loc_003EA3FE;
loc_003EA0AB:
    if (0 > v_stack_mF0) goto loc_003EA407;
    if ((v_r15 + a2 * 1) <= 0) goto loc_003EA407;
    result = (v_r15 + a2 * 1) - 1;
    if (result > v_stack_mF0) goto loc_003EA407;
    result = MiProtectionToCacheAttribute((unsigned int)((unsigned int)((unsigned int)(a5))), a2, a3, a4);
    v_stack_m110 = (unsigned int)(result);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 12431136))) > 1) goto loc_003EA570;
    v_r10 = 0;
    v_stack_p30 = 0;
loc_003EA104:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 12431136)))) goto loc_003EA15E;
loc_003EA10C:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 12431085)))) * (0));
    if (0 != ((unsigned int)((unsigned int)(0x80000000ULL)))) goto loc_003EA169;
loc_003EA12C:
    v_stack_mE0 = *(unsigned __int64 *)(v_rip + 10762934) + a1 * 4 + *(unsigned __int16 *)(v_rip + 12431085) * 4;
    if (((v_stack_m124) & (2)) == 0) goto loc_003EA16F;
loc_003EA13B:
    if (((a9) & (1)) == 0) goto loc_003EA1F3;
loc_003EA148:
    result = *(unsigned __int64 *)(v_rip + 10762934);
    if (v_stack_mF8 != -1) {
        a2 = v_stack_mD8;
        a3 = 0;
        result = MiFreeContiguousPages(v_stack_mF8, a2, a3, (unsigned int)((unsigned int)(result)));
    }
    goto loc_003EA407;
loc_003EA169:
    goto loc_003EA12C;
loc_003EA16F:
    if (v_stack_m118 != (v_rip + 10808202)) goto loc_003EA13B;
    if (0 != 0) goto loc_003EA13B;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 1) goto loc_003EA13B;
    if (v_r15 > 512) goto loc_003EA13B;
    v_r12 = (unsigned int)(0x746E6F43ULL);
    if (a8 != 0x546E6F43ULL) { v_r12 = a8; }
    v_rsi = (v_r15) << (12);
loc_003EA1AE:
    v_stack_m170 = (unsigned int)(v_r12);
    v_stack_m178 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10762934) + a1 * 4)));
    result = ExAllocateContiguousHeapPool(v_stack_mE8, v_stack_mF0, v_stack_m100, v_rsi);
    if (result != 0) goto loc_003EA4D3;
    v_r14 = (*(unsigned __int64 *)(v_rip + 10762934) + a1 * 4) + (4);
    if (v_r14 != (*(unsigned __int64 *)(v_rip + 10762934) + a1 * 4 + 4)) goto loc_003EA1AE;
    goto loc_003EA13B;
loc_003EA1F3:
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rip + 12430854)) * ((unsigned int)((unsigned int)(a6))));
loc_003EA20E:
    v_rbx = 0;
    if (v_stack_m100 == v_r15) goto loc_003EA529;
loc_003EA219:
    v_stack_m130 = v_stack_mF8;
    v_stack_m138 = 0;
    v_stack_m148 = 2;
    v_stack_m150 = (unsigned int)((unsigned int)(0x8100000ULL));
    v_stack_m158 = 255;
    v_stack_m160 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10762697) + a1 * 4)));
    v_stack_m168 = (unsigned int)((unsigned int)(v_stack_m110));
    v_stack_m170 = v_r15;
    result = MiFindContiguousPagesEx(v_stack_m118, v_stack_mE8, v_stack_mF0, v_stack_m100);
    if (0 != 0) goto loc_003EA50D;
loc_003EA274:
    if (sign_flag) goto loc_003EA5DD;
    v_rsi = (v_r15) << (12);
    a1 = (v_stack_mF8) << (12);
    v_stack_mD8 = v_r15;
    v_stack_m178 = (unsigned int)((unsigned int)(v_stack_m120));
    result = MiMapContiguousMemory(a1, v_rsi, v_rsi, (unsigned int)(v_stack_m124));
    v_stack_m108 = result;
    if (result != 0) goto loc_003EA49F;
loc_003EA2B8:
    v_r14 = (v_stack_mF8 + v_stack_mF8 * 2) << (4);
    v_r14 = (v_r14) + (v_stack_mF8);
    if (result == 0) goto loc_003EA418;
    v_rbx = (result) >> (9);
    v_rbx = (v_rbx) & (v_stack_mF8);
    v_rbx = (v_rbx) + (v_stack_mF8);
loc_003EA2FB:
    if ((*(unsigned int *)(v_rip + 12438033)) != 0) goto loc_003EA4DE;
loc_003EA315:
    a1 = 0;
    v_stack_m120 = 0;
    if (v_r15 != 0) goto loc_003EA43E;
loc_003EA325:
    result = 2;
    if ((*(unsigned int *)(v_rip + 12438004)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_rsi, (unsigned int)(v_stack_m124));
    }
    if (result == 0) goto loc_003EA148;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12437427)))) & (1)) != 0) goto loc_003EA620;
loc_003EA359:
loc_003EA35E:
    result = (unsigned int)(*(unsigned int *)(v_rip + 12437427));
    if ((unsigned __int8)(v_stack_m128) == 0) {
        result = v_stack_m118;
    }
    *(unsigned __int64 *)(v_stack_mD0) = v_rsi;
loc_003EA37C:
    result = VfPtIsAptEnabledOnKernel(a1, a2, v_rsi, (unsigned int)(v_stack_m124));
    if ((unsigned __int8)(result) != 0) goto loc_003EA636;
loc_003EA389:
    v_stack_m138 = result;
    v_stack_m148 = (unsigned __int8)(v_stack_m128);
    v_stack_m150 = (unsigned int)((unsigned int)(a9));
    v_stack_m158 = (unsigned int)((unsigned int)(a8));
    v_stack_m160 = (unsigned int)(*(unsigned __int16 *)(v_stack_m118));
    v_stack_m168 = (unsigned int)((unsigned int)(a6));
    v_stack_m170 = (unsigned int)((unsigned int)(v_stack_m124));
    v_stack_m178 = v_stack_m100;
    result = EtwTraceContAllocationEvent(result, *(unsigned __int64 *)(v_stack_mD0), v_stack_mE8, v_stack_mF0);
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(v_stack_mD0), v_stack_mE8, v_stack_mF0);
    v_rsp = (v_rsp) + (344);
    return result;
loc_003EA3FE:
    if (v_r15 <= v_stack_m100) goto loc_003EA0AB;
loc_003EA407:
    goto loc_003EA37C;
loc_003EA418:
    v_rbx = 0;
    goto loc_003EA2FB;
loc_003EA41F:
    if (((*(unsigned __int64 *)(v_rip + 12437086)) & (0x8000ULL)) == 0) goto loc_003EA09E;
    v_r14 = (unsigned int)((v_stack_mD0) & (0xFFFFFFFDULL));
    v_stack_p74 = (unsigned int)(v_r14);
    goto loc_003EA09E;
loc_003EA43E:
    v_r14 = (v_r14) + (24);
loc_003EA447:
    v_r12 = 0;
loc_003EA44A:
    if (condition_is_below) goto loc_003EA4ED;
    *(unsigned __int64 *)(v_r14 - 16) = 0;
    result = (v_stack_p78) + 1;
    v_stack_p78 = result;
    if ((((unsigned __int8)(result)) & (63)) == 0) goto loc_003EA601;
    v_r14 = (v_r14) + (48);
    if (0 != 0) {
        v_rbx = (v_rbx) + (8);
    }
    if (result < v_r15) goto loc_003EA447;
    goto loc_003EA325;
loc_003EA49F:
    v_stack_p20 = (unsigned int)(v_rbx);
    result = ExInsertPoolTag((unsigned int)(a8), v_stack_m108, *(unsigned __int64 *)(v_stack_mD0), v_stack_mF0);
    if ((unsigned int)(result) != 0) goto loc_003EA2B8;
    a2 = (*(unsigned __int64 *)(v_stack_mD0)) + (0x1000ULL);
loc_003EA4D3:
    goto loc_003EA35E;
loc_003EA4DE:
    result = KiRaiseIrqlProcessIrqlFlags(1, (unsigned __int8)(result), *(unsigned __int64 *)(v_stack_mD0), v_stack_mF0);
    goto loc_003EA315;
loc_003EA4ED:
    v_r12 = (unsigned int)((result) + 1);
    if (((*(unsigned int *)(v_rip + 12430773)) & ((unsigned int)(v_r12))) == 0) goto loc_003EA5B5;
loc_003EA4FD:
loc_003EA4FF:
    if (!sign_flag) goto loc_003EA44A;
    goto loc_003EA4ED;
loc_003EA50D:
    if (v_rbx == v_stack_mB8) goto loc_003EA274;
    a2 = 0;
    result = ExFreePoolWithTag(v_rbx, a2, *(unsigned __int64 *)(v_stack_mD0), v_stack_mF0);
    goto loc_003EA274;
loc_003EA529:
    if (v_r15 == 16) goto loc_003EA545;
    if (v_r15 == 512) goto loc_003EA545;
    if (v_r15 != 0x40000ULL) goto loc_003EA219;
loc_003EA545:
    result = ~(v_r15 - 1);
    v_stack_mB8 = 8;
    result = (result) & (*(unsigned __int64 *)(v_rip + 10762105));
    v_stack_mA8 = result;
    goto loc_003EA219;
loc_003EA570:
    v_stack_p30 = (unsigned int)(*(unsigned __int64 *)(v_stack_mD0));
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_mD0))) != 1) goto loc_003EA104;
    v_stack_p30 = (unsigned int)(*(unsigned __int64 *)(v_stack_mD0));
    goto loc_003EA10C;
loc_003EA5B5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12436733)))) & (64)) == 0) goto loc_003EA4FD;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12445358 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 588)) * 8) + 192), a2, *(unsigned __int64 *)(v_stack_mD0), v_stack_mF0);
    if ((unsigned __int8)(result) == 0) goto loc_003EA4FD;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), a2, *(unsigned __int64 *)(v_stack_mD0), v_stack_mF0);
    goto loc_003EA4FF;
loc_003EA5DD:
    v_rsi = (*(unsigned __int64 *)(v_stack_mD0)) + (4);
    if (v_rsi == v_stack_mE0) goto loc_003EA148;
    goto loc_003EA20E;
loc_003EA601:
    result = KiLowerIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), 1, *(unsigned __int64 *)(v_stack_mD0), (unsigned int)(v_stack_m110));
loc_003EA620:
    a2 = 0;
    result = MiLogPerfMemoryRangeEvent(v_r12, a2, a2 + 13, v_r15);
    goto loc_003EA359;
loc_003EA636:
    a4 = 0;
    result = VfPtMiscPoolNotification(v_r12, v_rsi, (unsigned int)(a8), a4);
    goto loc_003EA389;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateContiguousMemory(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, int64_t Arg7, uint32_t Arg8, uint8_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint32_t v_stack_m124;
    uint8_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint32_t v_stack_m150;
    uint8_t v_stack_m158;
    uint32_t v_stack_m160;
    uint32_t v_stack_m168;
    uint32_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m58;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint64_t v_stack_mB4;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p20;
    uint32_t v_stack_p30;
    uint8_t v_stack_p70;
    uint32_t v_stack_p74;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (344);
    result = (*(uint64_t *)(v_rip + 0xA20744)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_mE8 = Arg2;
    Arg2 = 0;
    v_stack_mF0 = Arg3;
    v_stack_mD0 = Arg1;
    v_stack_m100 = Arg4;
    v_stack_m124 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m118 = Arg7;
    result = memset(v_stack_mB8, Arg2, Arg2 + 88, Arg4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg2 + 88, Arg4);
    local_r12 = 0;
    Arg3 = 0;
    v_stack_mC8 = result;
    Arg3 = ((*(uint32_t *)(v_rip + 0xBDCBB0)) != 0) ? 1 : 0;
    v_stack_m128 = 0;
    v_stack_m120 = (uint32_t)(Arg3);
    local_r15 = (((*(uint64_t *)(arg1)) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (*(uint64_t *)(arg1)) >> (12);
    local_r15 = (local_r15) + (result);
    if ((((uint8_t)(local_r12 + 2)) & ((uint8_t)((uint32_t)(Arg5)))) != 0) goto loc_003EA41F;
loc_003EA09E:
    if (v_stack_m100 != 0) goto loc_003EA3FE;
loc_003EA0AB:
    if (0 > v_stack_mF0) goto loc_003EA407;
    if ((local_r15 + Arg2 * 1) <= 0) goto loc_003EA407;
    result = (local_r15 + Arg2 * 1) - 1;
    if (result > v_stack_mF0) goto loc_003EA407;
    result = MiProtectionToCacheAttribute((uint32_t)((uint32_t)((uint32_t)(Arg5))), Arg2, Arg3, Arg4);
    v_stack_m110 = (uint32_t)(result);
    if (((uint16_t)(*(uint16_t *)(v_rip + 0xBDAF20))) > 1) goto loc_003EA570;
    local_r10 = 0;
    v_stack_p30 = 0;
loc_003EA104:
    if (0 >= ((uint32_t)(*(uint16_t *)(v_rip + 0xBDAF20)))) goto loc_003EA15E;
loc_003EA10C:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0xBDAEED)))) * (0));
    if (0 != ((uint32_t)((uint32_t)(0x80000000ULL)))) goto loc_003EA169;
loc_003EA12C:
    v_stack_mE0 = *(uint64_t *)(v_rip + 0xA43AB6) + Arg1 * 4 + *(uint16_t *)(v_rip + 0xBDAEED) * 4;
    if (((v_stack_m124) & (2)) == 0) goto loc_003EA16F;
loc_003EA13B:
    if (((Arg9) & (1)) == 0) goto loc_003EA1F3;
loc_003EA148:
    result = *(uint64_t *)(v_rip + 0xA43AB6);
    if (v_stack_mF8 != -1) {
        Arg2 = v_stack_mD8;
        Arg3 = 0;
        result = MiFreeContiguousPages(v_stack_mF8, Arg2, Arg3, (uint32_t)((uint32_t)(result)));
    }
    goto loc_003EA407;
loc_003EA169:
    goto loc_003EA12C;
loc_003EA16F:
    if (v_stack_m118 != (v_rip + 10808202)) goto loc_003EA13B;
    if (0 != 0) goto loc_003EA13B;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 1) goto loc_003EA13B;
    if (local_r15 > 512) goto loc_003EA13B;
    local_r12 = (uint32_t)(0x746E6F43ULL);
    if (Arg8 != 0x546E6F43ULL) { local_r12 = Arg8; }
    local_rsi = (local_r15) << (12);
loc_003EA1AE:
    v_stack_m170 = (uint32_t)(local_r12);
    v_stack_m178 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA43AB6) + arg1 * 4)));
    result = ExAllocateContiguousHeapPool(v_stack_mE8, v_stack_mF0, v_stack_m100, local_rsi);
    if (result != 0) goto loc_003EA4D3;
    local_r14 = (*(uint64_t *)(v_rip + 0xA43AB6) + Arg1 * 4) + (4);
    if (local_r14 != (*(uint64_t *)(v_rip + 0xA43AB6) + Arg1 * 4 + 4)) goto loc_003EA1AE;
    goto loc_003EA13B;
loc_003EA1F3:
    Arg1 = (uint32_t)((*(uint16_t *)(v_rip + 0xBDAE06)) * ((uint32_t)((uint32_t)(Arg6))));
loc_003EA20E:
    local_rbx = 0;
    if (v_stack_m100 == local_r15) goto loc_003EA529;
loc_003EA219:
    v_stack_m130 = v_stack_mF8;
    v_stack_m138 = 0;
    v_stack_m148 = 2;
    v_stack_m150 = (uint32_t)((uint32_t)(0x8100000ULL));
    v_stack_m158 = 255;
    v_stack_m160 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA439C9) + arg1 * 4)));
    v_stack_m168 = (uint32_t)((uint32_t)(v_stack_m110));
    v_stack_m170 = local_r15;
    result = MiFindContiguousPagesEx(v_stack_m118, v_stack_mE8, v_stack_mF0, v_stack_m100);
    if (0 != 0) goto loc_003EA50D;
loc_003EA274:
    if (sign_flag) goto loc_003EA5DD;
    local_rsi = (local_r15) << (12);
    Arg1 = (v_stack_mF8) << (12);
    v_stack_mD8 = local_r15;
    v_stack_m178 = (uint32_t)((uint32_t)(v_stack_m120));
    result = MiMapContiguousMemory(Arg1, local_rsi, local_rsi, (uint32_t)(v_stack_m124));
    v_stack_m108 = result;
    if (result != 0) goto loc_003EA49F;
loc_003EA2B8:
    local_r14 = (v_stack_mF8 + v_stack_mF8 * 2) << (4);
    local_r14 = (local_r14) + (v_stack_mF8);
    if (result == 0) goto loc_003EA418;
    local_rbx = (result) >> (9);
    local_rbx = (local_rbx) & (v_stack_mF8);
    local_rbx = (local_rbx) + (v_stack_mF8);
loc_003EA2FB:
    if ((*(uint32_t *)(v_rip + 0xBDCA11)) != 0) goto loc_003EA4DE;
loc_003EA315:
    Arg1 = 0;
    v_stack_m120 = 0;
    if (local_r15 != 0) goto loc_003EA43E;
loc_003EA325:
    result = 2;
    if ((*(uint32_t *)(v_rip + 0xBDC9F4)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, local_rsi, (uint32_t)(v_stack_m124));
    }
    if (result == 0) goto loc_003EA148;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBDC7B3)))) & (1)) != 0) goto loc_003EA620;
loc_003EA359:
loc_003EA35E:
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xBDC7B3));
    if ((uint8_t)(v_stack_m128) == 0) {
        result = v_stack_m118;
    }
    *(uint64_t *)(v_stack_mD0) = local_rsi;
loc_003EA37C:
    result = VfPtIsAptEnabledOnKernel(Arg1, Arg2, local_rsi, (uint32_t)(v_stack_m124));
    if ((uint8_t)(result) != 0) goto loc_003EA636;
loc_003EA389:
    v_stack_m138 = result;
    v_stack_m148 = (uint8_t)(v_stack_m128);
    v_stack_m150 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m158 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m160 = (uint32_t)(*(uint16_t *)(v_stack_m118));
    v_stack_m168 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m170 = (uint32_t)((uint32_t)(v_stack_m124));
    v_stack_m178 = v_stack_m100;
    result = EtwTraceContAllocationEvent(result, *(uint64_t *)(v_stack_mD0), v_stack_mE8, v_stack_mF0);
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(v_stack_mD0), v_stack_mE8, v_stack_mF0);
    local_rsp = (local_rsp) + (344);
    return result;
loc_003EA3FE:
    if (local_r15 <= v_stack_m100) goto loc_003EA0AB;
loc_003EA407:
    goto loc_003EA37C;
loc_003EA418:
    local_rbx = 0;
    goto loc_003EA2FB;
loc_003EA41F:
    if (((*(uint64_t *)(v_rip + 0xBDC65E)) & (0x8000ULL)) == 0) goto loc_003EA09E;
    local_r14 = (uint32_t)((v_stack_mD0) & (0xFFFFFFFDULL));
    v_stack_p74 = (uint32_t)(local_r14);
    goto loc_003EA09E;
loc_003EA43E:
    local_r14 = (local_r14) + (24);
loc_003EA447:
    local_r12 = 0;
loc_003EA44A:
    if (condition_is_below) goto loc_003EA4ED;
    *(uint64_t *)(local_r14 - 0x10) = 0;
    result = (v_stack_p78) + 1;
    v_stack_p78 = result;
    if ((((uint8_t)(result)) & (63)) == 0) goto loc_003EA601;
    local_r14 = (local_r14) + (48);
    if (0 != 0) {
        local_rbx = (local_rbx) + (8);
    }
    if (result < local_r15) goto loc_003EA447;
    goto loc_003EA325;
loc_003EA49F:
    v_stack_p20 = (uint32_t)(local_rbx);
    result = ExInsertPoolTag((uint32_t)(Arg8), v_stack_m108, *(uint64_t *)(v_stack_mD0), v_stack_mF0);
    if ((uint32_t)(result) != 0) goto loc_003EA2B8;
    Arg2 = (*(uint64_t *)(v_stack_mD0)) + (0x1000ULL);
loc_003EA4D3:
    goto loc_003EA35E;
loc_003EA4DE:
    result = KiRaiseIrqlProcessIrqlFlags(1, (uint8_t)(result), *(uint64_t *)(v_stack_mD0), v_stack_mF0);
    goto loc_003EA315;
loc_003EA4ED:
    local_r12 = (uint32_t)((result) + 1);
    if (((*(uint32_t *)(v_rip + 0xBDADB5)) & ((uint32_t)(local_r12))) == 0) goto loc_003EA5B5;
loc_003EA4FD:
loc_003EA4FF:
    if (!sign_flag) goto loc_003EA44A;
    goto loc_003EA4ED;
loc_003EA50D:
    if (local_rbx == v_stack_mB8) goto loc_003EA274;
    Arg2 = 0;
    result = ExFreePoolWithTag(local_rbx, Arg2, *(uint64_t *)(v_stack_mD0), v_stack_mF0);
    goto loc_003EA274;
loc_003EA529:
    if (local_r15 == 16) goto loc_003EA545;
    if (local_r15 == 512) goto loc_003EA545;
    if (local_r15 != 0x40000ULL) goto loc_003EA219;
loc_003EA545:
    result = ~(local_r15 - 1);
    v_stack_mB8 = 8;
    result = (result) & (*(uint64_t *)(v_rip + 0xA43779));
    v_stack_mA8 = result;
    goto loc_003EA219;
loc_003EA570:
    v_stack_p30 = (uint32_t)(*(uint64_t *)(v_stack_mD0));
    if (((uint32_t)(*(uint64_t *)(v_stack_mD0))) != 1) goto loc_003EA104;
    v_stack_p30 = (uint32_t)(*(uint64_t *)(v_stack_mD0));
    goto loc_003EA10C;
loc_003EA5B5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBDC4FD)))) & (64)) == 0) goto loc_003EA4FD;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBDE6AE + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24C)) * 8) + 0xC0), Arg2, *(uint64_t *)(v_stack_mD0), v_stack_mF0);
    if ((uint8_t)(result) == 0) goto loc_003EA4FD;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), Arg2, *(uint64_t *)(v_stack_mD0), v_stack_mF0);
    goto loc_003EA4FF;
loc_003EA5DD:
    local_rsi = (*(uint64_t *)(v_stack_mD0)) + (4);
    if (local_rsi == v_stack_mE0) goto loc_003EA148;
    goto loc_003EA20E;
loc_003EA601:
    result = KiLowerIrqlProcessIrqlFlags((uint8_t)(v_cr8), 1, *(uint64_t *)(v_stack_mD0), (uint32_t)(v_stack_m110));
loc_003EA620:
    Arg2 = 0;
    result = MiLogPerfMemoryRangeEvent(local_r12, Arg2, Arg2 + 13, local_r15);
    goto loc_003EA359;
loc_003EA636:
    Arg4 = 0;
    result = VfPtMiscPoolNotification(local_r12, local_rsi, (uint32_t)(Arg8), Arg4);
    goto loc_003EA389;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E9FDC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
