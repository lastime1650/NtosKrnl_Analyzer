# NtLockVirtualMemory

- RVA: `0x004088A0`–`0x00409353` (길이 `2,739` bytes)
- VA: `0x00000001404088A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009AB98`
- 디코드: `619`개 명령, `2,739/2,739` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **64**; 고유 호출 대상: **35**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00408931` → [MiLockUnlockCommon](../../page/9E/MiLockUnlockCommon_function_009EA5D0.md) (function, `0x009EA5D0`)
- `0x004089A5` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x004089D3` → [KiStackAttachProcess](../21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00408A43` → [MiLockVadRange](../../page/87/MiLockVadRange_function_0087F670.md) (function, `0x0087F670`)
- `0x00408A5F` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x00408A7D` → [MiVadPureReserve](../2C/MiVadPureReserve_function_002C34C0.md) (function, `0x002C34C0`)
- `0x00408AAB` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00408B28` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00408B3B` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00408B5B` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00408BA3` → [MiGetWsleContents](../31/MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x00408C0A` → [MiLockPageTablePage](../23/MiLockPageTablePage_function_0023E120.md) (function, `0x0023E120`)
- `0x00408C60` → [MiChargeCommit](../28/MiChargeCommit_function_00286EB0.md) (function, `0x00286EB0`)
- `0x00408C89` → [MiSetVaAgeList](../29/MiSetVaAgeList_function_00290A20.md) (function, `0x00290A20`)
- `0x00408C9E` → [MiGetEffectivePagePriorityThread](../36/MiGetEffectivePagePriorityThread_function_003626E0.md) (function, `0x003626E0`)
- `0x00408CC9` → [MiUpdatePfnPriority](../2B/MiUpdatePfnPriority_function_002B8570.md) (function, `0x002B8570`)
- `0x00408D4B` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00408D57` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00408D61` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00408DA7` → [MiGetNextPageTable](../2C/MiGetNextPageTable_function_002C2EE0.md) (function, `0x002C2EE0`)
- `0x00408E18` → [MiGetNextVad](../29/MiGetNextVad_function_00297224.md) (function, `0x00297224`)
- `0x00408E25` → [MiVadPureReserve](../2C/MiVadPureReserve_function_002C34C0.md) (function, `0x002C34C0`)
- `0x00408E3E` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00408E4E` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00408E6B` → [MiUnlockVadRange](../../page/87/MiUnlockVadRange_function_0087F590.md) (function, `0x0087F590`)
- `0x00408E83` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00408E92` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00408EE1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00408EFD` → [MiVadPagesTradable](MiVadPagesTradable_function_00409360.md) (function, `0x00409360`)
- `0x00408F0D` → [MiGetNextVad](../29/MiGetNextVad_function_00297224.md) (function, `0x00297224`)
- `0x00408F28` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x00408F5C` → [MiLockPageTablePage](../23/MiLockPageTablePage_function_0023E120.md) (function, `0x0023E120`)
- `0x00408F85` → [MiWorkingSetIsContended](../2A/MiWorkingSetIsContended_function_002AE520.md) (function, `0x002AE520`)
- `0x00408F98` → [MiPageTableLockIsContended](../2A/MiPageTableLockIsContended_function_002AE650.md) (function, `0x002AE650`)
- `0x00408FA5` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x00408FBB` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x00408FE5` → [MiGetPagingFileOffset](../36/MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x00408FF8` → [MiLockPageAndSetDirty](../28/MiLockPageAndSetDirty_function_002857A0.md) (function, `0x002857A0`)
- `0x0040900C` → [KiUnstackDetachProcess](../21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0040902F` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0040904B` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00409073` → [MiUnlockVadRange](../../page/87/MiUnlockVadRange_function_0087F590.md) (function, `0x0087F590`)
- `0x00409087` → [KiUnstackDetachProcess](../21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00409096` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004090A0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004090B2` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004090C3` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00409140` → [MiUnlockVa](MiUnlockVa_function_00407F24.md) (function, `0x00407F24`)
- `0x00409194` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x004091A5` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x004091B4` → [MiWorkingSetIsContended](../2A/MiWorkingSetIsContended_function_002AE520.md) (function, `0x002AE520`)
- `0x004091CC` → [MiPageTableLockIsContended](../2A/MiPageTableLockIsContended_function_002AE650.md) (function, `0x002AE650`)
- `0x004091D9` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x00409237` → [MiUnlockPageTableCharges](MiUnlockPageTableCharges_function_00408140.md) (function, `0x00408140`)
- `0x00409248` → [MiUnlockPageTableCharges](MiUnlockPageTableCharges_function_00408140.md) (function, `0x00408140`)
- `0x0040926A` → [MiUnlockPageTableCharges](MiUnlockPageTableCharges_function_00408140.md) (function, `0x00408140`)
- `0x0040929B` → [MiUnlockPageTableCharges](MiUnlockPageTableCharges_function_00408140.md) (function, `0x00408140`)
- `0x004092D6` → [MiUnlockPageTableCharges](MiUnlockPageTableCharges_function_00408140.md) (function, `0x00408140`)
- `0x004092F7` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x0040930C` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0040931A` → [MiLockNestedPageTable](../23/MiLockNestedPageTable_function_0023E890.md) (function, `0x0023E890`)
- `0x0040932F` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x0040933C` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x00409344` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004088B5` → RVA `0x00E0A740` (`.data`; read)
- `0x00408C44` → RVA `0x00E30088` (`.data`; read)
- `0x00408DF8` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00409186` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00408931` → [MiLockUnlockCommon](../../page/9E/MiLockUnlockCommon_function_009EA5D0.md) (`.text` → `PAGE`)
  - `0x00408A43` → [MiLockVadRange](../../page/87/MiLockVadRange_function_0087F670.md) (`.text` → `PAGE`)
  - `0x00408E6B` → [MiUnlockVadRange](../../page/87/MiUnlockVadRange_function_0087F590.md) (`.text` → `PAGE`)
  - `0x00408E92` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00409073` → [MiUnlockVadRange](../../page/87/MiUnlockVadRange_function_0087F590.md) (`.text` → `PAGE`)
  - `0x004090A0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004088A0  4C 8B DC                        mov r11, rsp
004088A3  53                              push rbx
004088A4  56                              push rsi
004088A5  57                              push rdi
004088A6  41 54                           push r12
004088A8  41 55                           push r13
004088AA  41 56                           push r14
004088AC  41 57                           push r15
004088AE  48 81 EC 30 01 00 00            sub rsp, 0x130
004088B5  48 8B 05 84 1E A0 00            mov rax, qword ptr [rip + 0xa01e84]
004088BC  48 33 C4                        xor rax, rsp
004088BF  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
004088C7  4C 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r8
004088CF  48 89 94 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rdx
004088D7  48 8B F9                        mov rdi, rcx
004088DA  0F 57 C0                        xorps xmm0, xmm0
004088DD  41 0F 11 43 88                  movups xmmword ptr [r11 - 0x78], xmm0
004088E2  41 0F 11 43 98                  movups xmmword ptr [r11 - 0x68], xmm0
004088E7  41 0F 11 43 A8                  movups xmmword ptr [r11 - 0x58], xmm0
004088EC  49 83 A3 40 FF FF FF 00         and qword ptr [r11 - 0xc0], 0
004088F4  49 83 A3 30 FF FF FF 00         and qword ptr [r11 - 0xd0], 0
004088FC  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
00408902  33 DB                           xor ebx, ebx
00408904  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00408908  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
0040890C  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00408911  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00408916  49 8D 8B 40 FF FF FF            lea rcx, [r11 - 0xc0]
0040891D  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00408922  49 8D 8B 30 FF FF FF            lea rcx, [r11 - 0xd0]
00408929  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0040892E  48 8B CF                        mov rcx, rdi
00408931  E8 9A 1C 5E 00                  call 0x1409ea5d0
00408936  85 C0                           test eax, eax
00408938  0F 88 98 05 00 00               js 0x140408ed6
0040893E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00408947  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
0040894F  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
00408957  4C 8B AC 24 98 00 00 00         mov r13, qword ptr [rsp + 0x98]
0040895F  49 FF CC                        dec r12
00408962  4D 03 E5                        add r12, r13
00408965  48 C7 C0 00 F0 FF FF            mov rax, 0xfffffffffffff000
0040896C  4C 23 E0                        and r12, rax
0040896F  4C 23 E8                        and r13, rax
00408972  49 8B C4                        mov rax, r12
00408975  49 2B C5                        sub rax, r13
00408978  48 C1 E8 0C                     shr rax, 0xc
0040897C  44 8D 7B 01                     lea r15d, [rbx + 1]
00408980  49 03 C7                        add rax, r15
00408983  33 C9                           xor ecx, ecx
00408985  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0040898A  A8 3F                           test al, 0x3f
0040898C  8B D1                           mov edx, ecx
0040898E  0F 95 C2                        setne dl
00408991  48 C1 E8 06                     shr rax, 6
00408995  48 03 D0                        add rdx, rax
00408998  48 C1 E2 03                     shl rdx, 3
0040899C  8D 4B 40                        lea ecx, [rbx + 0x40]
0040899F  41 B8 4D 6D 6C 6B               mov r8d, 0x6b6c6d4d
004089A5  E8 96 2B F5 FF                  call 0x14035b540
004089AA  4C 8B F0                        mov r14, rax
004089AD  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
004089B5  48 85 C0                        test rax, rax
004089B8  0F 84 FB 06 00 00               je 0x1404090b9
004089BE  48 83 FF FF                     cmp rdi, -1
004089C2  74 20                           je 0x1404089e4
004089C4  4C 8D 84 24 F0 00 00 00         lea r8, [rsp + 0xf0]
004089CC  33 D2                           xor edx, edx
004089CE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
004089D3  E8 48 DE E0 FF                  call 0x140216820
004089D8  41 8D 5F 01                     lea ebx, [r15 + 1]
004089DC  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
004089E0  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
004089E4  48 8B B4 24 98 00 00 00         mov rsi, qword ptr [rsp + 0x98]
004089EC  48 C1 EE 09                     shr rsi, 9
004089F0  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
004089FA  49 23 F0                        and rsi, r8
004089FD  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
00408A07  48 8B C2                        mov rax, rdx
00408A0A  48 03 F0                        add rsi, rax
00408A0D  48 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], rsi
00408A15  4C 89 AC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r13
00408A1D  49 8B CC                        mov rcx, r12
00408A20  48 C1 E9 09                     shr rcx, 9
00408A24  49 23 C8                        and rcx, r8
00408A27  48 8B C2                        mov rax, rdx
00408A2A  48 03 C8                        add rcx, rax
00408A2D  48 89 8C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rcx
00408A35  45 33 C9                        xor r9d, r9d
00408A38  4D 8B C4                        mov r8, r12
00408A3B  49 8B D5                        mov rdx, r13
00408A3E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00408A43  E8 28 6C 47 00                  call 0x14087f670
00408A48  4C 8B D8                        mov r11, rax
00408A4B  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00408A53  48 85 C0                        test rax, rax
00408A56  0F 84 20 07 00 00               je 0x14040917c
00408A5C  49 8B CD                        mov rcx, r13
00408A5F  E8 6C DE F0 FF                  call 0x1403168d0
00408A64  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00408A69  45 33 C0                        xor r8d, r8d
00408A6C  4C 8B C8                        mov r9, rax
00408A6F  4D 3B C3                        cmp r8, r11
00408A72  0F 82 82 04 00 00               jb 0x140408efa
00408A78  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00408A7D  E8 3E AA EB FF                  call 0x1402c34c0
00408A82  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00408A86  33 FF                           xor edi, edi
00408A88  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00408A8D  49 81 C6 00 04 00 00            add r14, 0x400
00408A94  4C 89 B4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r14
00408A9C  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00408AA0  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00408AA8  49 8B CE                        mov rcx, r14
00408AAB  E8 40 41 E7 FF                  call 0x14027cbf0
00408AB0  44 8A C0                        mov r8b, al
00408AB3  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00408AB7  49 BB 00 00 00 00 00 DE FF FF   movabs r11, 0xffffde0000000000
00408AC1  49 BA 00 00 00 40 FB F6 FF FF   movabs r10, 0xfffff6fb40000000
00408ACB  4D 3B EC                        cmp r13, r12
00408ACE  0F 87 5F 03 00 00               ja 0x140408e33
00408AD4  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
00408AD9  41 0F B6 51 21                  movzx edx, byte ptr [r9 + 0x21]
00408ADE  48 C1 E2 20                     shl rdx, 0x20
00408AE2  41 8B 41 1C                     mov eax, dword ptr [r9 + 0x1c]
00408AE6  48 0B D0                        or rdx, rax
00408AE9  49 8B C5                        mov rax, r13
00408AEC  48 C1 E8 0C                     shr rax, 0xc
00408AF0  48 3B C2                        cmp rax, rdx
00408AF3  0F 87 1C 03 00 00               ja 0x140408e15
00408AF9  49 8B CD                        mov rcx, r13
00408AFC  48 C1 E9 12                     shr rcx, 0x12
00408B00  81 E1 F8 FF FF 3F               and ecx, 0x3ffffff8
00408B06  49 8B C2                        mov rax, r10
00408B09  48 03 C1                        add rax, rcx
00408B0C  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00408B11  48 3B F8                        cmp rdi, rax
00408B14  0F 85 5E 02 00 00               jne 0x140408d78
00408B1A  48 8B 06                        mov rax, qword ptr [rsi]
00408B1D  41 84 C7                        test r15b, al
00408B20  75 5F                           jne 0x140408b81
00408B22  48 8B D7                        mov rdx, rdi
00408B25  49 8B CE                        mov rcx, r14
00408B28  E8 93 E3 E0 FF                  call 0x140216ec0
00408B2D  33 FF                           xor edi, edi
00408B2F  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00408B34  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
00408B38  49 8B CE                        mov rcx, r14
00408B3B  E8 50 4B E7 FF                  call 0x14027d690
00408B40  90                              nop
00408B41  41 8A 45 00                     mov al, byte ptr [r13]
00408B45  E9 5E FF FF FF                  jmp 0x140408aa8
00408B4A  8B F0                           mov esi, eax
00408B4C  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00408B50  4C 8B B4 24 C8 00 00 00         mov r14, qword ptr [rsp + 0xc8]
00408B58  49 8B CE                        mov rcx, r14
00408B5B  E8 90 40 E7 FF                  call 0x14027cbf0
00408B60  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00408B64  41 BF 01 00 00 00               mov r15d, 1
00408B6A  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
00408B6F  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00408B74  8B 5C 24 68                     mov ebx, dword ptr [rsp + 0x68]
00408B78  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00408B7C  E9 A3 04 00 00                  jmp 0x140409024
00408B81  48 C1 E8 0C                     shr rax, 0xc
00408B85  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00408B8F  48 23 C1                        and rax, rcx
00408B92  48 8D 34 40                     lea rsi, [rax + rax*2]
00408B96  48 C1 E6 04                     shl rsi, 4
00408B9A  49 8B C3                        mov rax, r11
00408B9D  48 03 F0                        add rsi, rax
00408BA0  49 8B D5                        mov rdx, r13
00408BA3  E8 98 D9 F0 FF                  call 0x140316540
00408BA8  24 0F                           and al, 0xf
00408BAA  3C 08                           cmp al, 8
00408BAC  0F 84 1A 04 00 00               je 0x140408fcc
00408BB2  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00408BBA  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
00408BBE  48 83 C0 06                     add rax, 6
00408BC2  49 39 46 70                     cmp qword ptr [r14 + 0x70], rax
00408BC6  0F 86 4A 04 00 00               jbe 0x140409016
00408BCC  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00408BD0  48 85 C0                        test rax, rax
00408BD3  0F 88 7D 03 00 00               js 0x140408f56
00408BD9  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00408BDE  48 8B 00                        mov rax, qword ptr [rax]
00408BE1  48 C1 E8 0C                     shr rax, 0xc
00408BE5  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00408BEF  48 23 C1                        and rax, rcx
00408BF2  48 8D 0C 40                     lea rcx, [rax + rax*2]
00408BF6  48 C1 E1 04                     shl rcx, 4
00408BFA  49 8B C3                        mov rax, r11
00408BFD  48 03 C8                        add rcx, rax
00408C00  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00408C05  BA 02 00 00 00                  mov edx, 2
00408C0A  E8 11 55 E3 FF                  call 0x14023e120
00408C0F  85 C0                           test eax, eax
00408C11  0F 84 EB 05 00 00               je 0x140409202
00408C17  48 83 A4 24 80 00 00 00 00      and qword ptr [rsp + 0x80], 0
00408C20  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
00408C23  48 0F BA E0 0A                  bt rax, 0xa
00408C28  0F 83 B3 03 00 00               jae 0x140408fe1
00408C2E  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00408C32  48 85 C0                        test rax, rax
00408C35  79 46                           jns 0x140408c7d
00408C37  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00408C3B  48 C1 E8 2B                     shr rax, 0x2b
00408C3F  25 FF 03 00 00                  and eax, 0x3ff
00408C44  48 8B 15 3D 74 A2 00            mov rdx, qword ptr [rip + 0xa2743d]
00408C4B  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
00408C4F  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00408C57  45 33 C0                        xor r8d, r8d
00408C5A  49 8B D7                        mov rdx, r15
00408C5D  48 8B C8                        mov rcx, rax
00408C60  E8 4B E2 E7 FF                  call 0x140286eb0
00408C65  85 C0                           test eax, eax
00408C67  0F 84 F3 05 00 00               je 0x140409260
00408C6D  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00408C75  F0 4C 01 B8 B0 4C 00 00         lock add qword ptr [rax + 0x4cb0], r15
00408C7D  41 B1 08                        mov r9b, 8
00408C80  45 8B C7                        mov r8d, r15d
00408C83  49 8B D5                        mov rdx, r13
00408C86  49 8B CE                        mov rcx, r14
00408C89  E8 92 7D E8 FF                  call 0x140290a20
00408C8E  85 C0                           test eax, eax
00408C90  0F 84 A8 05 00 00               je 0x14040923e
00408C96  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00408C9E  E8 3D 9A F5 FF                  call 0x1403626e0
00408CA3  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
00408CAA  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
00408CAF  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
00408CB6  0F 82 31 01 00 00               jb 0x140408ded
00408CBC  45 33 C0                        xor r8d, r8d
00408CBF  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
00408CC6  48 8B CE                        mov rcx, rsi
00408CC9  E8 A2 F8 EA FF                  call 0x1402b8570
00408CCE  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00408CD8  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00408CDD  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00408CE2  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00408CEA  48 0F AB 01                     bts qword ptr [rcx], rax
00408CEE  49 03 C7                        add rax, r15
00408CF1  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00408CF6  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00408CFE  48 83 C0 08                     add rax, 8
00408D02  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00408D0A  49 81 C5 00 10 00 00            add r13, 0x1000
00408D11  33 F6                           xor esi, esi
00408D13  4D 3B EC                        cmp r13, r12
00408D16  0F 86 5C 02 00 00               jbe 0x140408f78
00408D1C  85 F6                           test esi, esi
00408D1E  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00408D26  44 8A 44 24 40                  mov r8b, byte ptr [rsp + 0x40]
00408D2B  49 BA 00 00 00 40 FB F6 FF FF   movabs r10, 0xfffff6fb40000000
00408D35  49 BB 00 00 00 00 00 DE FF FF   movabs r11, 0xffffde0000000000
00408D3F  0F 84 86 FD FF FF               je 0x140408acb
00408D45  48 8B D7                        mov rdx, rdi
00408D48  49 8B CE                        mov rcx, r14
00408D4B  E8 70 E1 E0 FF                  call 0x140216ec0
00408D50  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
00408D54  49 8B CE                        mov rcx, r14
00408D57  E8 34 49 E7 FF                  call 0x14027d690
00408D5C  33 FF                           xor edi, edi
00408D5E  49 8B CE                        mov rcx, r14
00408D61  E8 8A 3E E7 FF                  call 0x14027cbf0
00408D66  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
00408D6E  44 8A 44 24 40                  mov r8b, byte ptr [rsp + 0x40]
00408D73  E9 3F FD FF FF                  jmp 0x140408ab7
00408D78  48 85 FF                        test rdi, rdi
00408D7B  0F 85 34 02 00 00               jne 0x140408fb5
00408D81  45 33 C9                        xor r9d, r9d
00408D84  48 8B CE                        mov rcx, rsi
00408D87  44 39 4C 24 78                  cmp dword ptr [rsp + 0x78], r9d
00408D8C  0F 84 88 01 00 00               je 0x140408f1a
00408D92  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
00408D9A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00408D9F  48 8B 94 24 C0 00 00 00         mov rdx, qword ptr [rsp + 0xc0]
00408DA7  E8 34 A1 EB FF                  call 0x1402c2ee0
00408DAC  48 85 C0                        test rax, rax
00408DAF  74 24                           je 0x140408dd5
00408DB1  48 8B F8                        mov rdi, rax
00408DB4  48 C1 EF 09                     shr rdi, 9
00408DB8  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
00408DC2  48 23 F9                        and rdi, rcx
00408DC5  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
00408DCF  48 8B C9                        mov rcx, rcx
00408DD2  48 03 F9                        add rdi, rcx
00408DD5  48 3B C6                        cmp rax, rsi
00408DD8  0F 85 1A 04 00 00               jne 0x1404091f8
00408DDE  49 BB 00 00 00 00 00 DE FF FF   movabs r11, 0xffffde0000000000
00408DE8  E9 2D FD FF FF                  jmp 0x140408b1a
00408DED  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
00408DF1  41 03 CF                        add ecx, r15d
00408DF4  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
00408DF8  85 0D AE C4 BB 00               test dword ptr [rip + 0xbbc4ae], ecx
00408DFE  0F 84 82 03 00 00               je 0x140409186
00408E04  F3 90                           pause
00408E06  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00408E0A  48 85 C0                        test rax, rax
00408E0D  0F 89 9C FE FF FF               jns 0x140408caf
00408E13  EB D8                           jmp 0x140408ded
00408E15  49 8B C9                        mov rcx, r9
00408E18  E8 07 E4 E8 FF                  call 0x140297224
00408E1D  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00408E22  48 8B C8                        mov rcx, rax
00408E25  E8 96 A6 EB FF                  call 0x1402c34c0
00408E2A  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00408E2E  E9 C6 FC FF FF                  jmp 0x140408af9
00408E33  48 85 FF                        test rdi, rdi
00408E36  74 10                           je 0x140408e48
00408E38  48 8B D7                        mov rdx, rdi
00408E3B  49 8B CE                        mov rcx, r14
00408E3E  E8 7D E0 E0 FF                  call 0x140216ec0
00408E43  44 8A 44 24 40                  mov r8b, byte ptr [rsp + 0x40]
00408E48  41 8A D0                        mov dl, r8b
00408E4B  49 8B CE                        mov rcx, r14
00408E4E  E8 3D 48 E7 FF                  call 0x14027d690
00408E53  45 33 C9                        xor r9d, r9d
00408E56  4C 8B 84 24 B0 00 00 00         mov r8, qword ptr [rsp + 0xb0]
00408E5E  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
00408E66  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00408E6B  E8 20 67 47 00                  call 0x14087f590
00408E70  F6 C3 02                        test bl, 2
00408E73  0F 85 89 01 00 00               jne 0x140409002
00408E79  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
00408E7E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00408E83  E8 58 EA EE FF                  call 0x1402f78e0
00408E88  33 D2                           xor edx, edx
00408E8A  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00408E92  E8 D9 99 77 00                  call 0x140b82870
00408E97  90                              nop
00408E98  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00408EA0  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
00408EA6  4C 2B E0                        sub r12, rax
00408EA9  49 81 C4 00 10 00 00            add r12, 0x1000
00408EB0  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00408EB8  4C 89 21                        mov qword ptr [rcx], r12
00408EBB  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
00408EC3  48 89 01                        mov qword ptr [rcx], rax
00408EC6  EB 02                           jmp 0x140408eca
00408EC8  EB 0C                           jmp 0x140408ed6
00408ECA  41 22 DF                        and bl, r15b
00408ECD  F6 DB                           neg bl
00408ECF  1B C0                           sbb eax, eax
00408ED1  25 19 00 00 40                  and eax, 0x40000019
00408ED6  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
00408EDE  48 33 CC                        xor rcx, rsp
00408EE1  E8 5A 37 2A 00                  call 0x1406ac640
00408EE6  48 81 C4 30 01 00 00            add rsp, 0x130
00408EED  41 5F                           pop r15
00408EEF  41 5E                           pop r14
00408EF1  41 5D                           pop r13
00408EF3  41 5C                           pop r12
00408EF5  5F                              pop rdi
00408EF6  5E                              pop rsi
00408EF7  5B                              pop rbx
00408EF8  C3                              ret
00408EF9  CC                              int3
00408EFA  49 8B C9                        mov rcx, r9
00408EFD  E8 5E 04 00 00                  call 0x140409360
00408F02  85 C0                           test eax, eax
00408F04  0F 84 E4 02 00 00               je 0x1404091ee
00408F0A  49 8B C9                        mov rcx, r9
00408F0D  E8 12 E3 E8 FF                  call 0x140297224
00408F12  4D 03 C7                        add r8, r15
00408F15  E9 52 FB FF FF                  jmp 0x140408a6c
00408F1A  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00408F1F  8B 52 30                        mov edx, dword ptr [rdx + 0x30]
00408F22  C1 EA 0C                        shr edx, 0xc
00408F25  83 E2 7F                        and edx, 0x7f
00408F28  E8 43 70 E7 FF                  call 0x14027ff70
00408F2D  48 8B FE                        mov rdi, rsi
00408F30  48 C1 EF 09                     shr rdi, 9
00408F34  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00408F3E  48 23 F8                        and rdi, rax
00408F41  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00408F4B  48 8B C0                        mov rax, rax
00408F4E  48 03 F8                        add rdi, rax
00408F51  E9 88 FE FF FF                  jmp 0x140408dde
00408F56  41 8B D7                        mov edx, r15d
00408F59  48 8B CE                        mov rcx, rsi
00408F5C  E8 BF 51 E3 FF                  call 0x14023e120
00408F61  85 C0                           test eax, eax
00408F63  0F 84 ED 02 00 00               je 0x140409256
00408F69  49 BB 00 00 00 00 00 DE FF FF   movabs r11, 0xffffde0000000000
00408F73  E9 61 FC FF FF                  jmp 0x140408bd9
00408F78  A8 78                           test al, 0x78
00408F7A  0F 85 9C FD FF FF               jne 0x140408d1c
00408F80  33 D2                           xor edx, edx
00408F82  49 8B CE                        mov rcx, r14
00408F85  E8 96 55 EA FF                  call 0x1402ae520
00408F8A  85 C0                           test eax, eax
00408F8C  0F 85 B3 FD FF FF               jne 0x140408d45
00408F92  48 8B D7                        mov rdx, rdi
00408F95  49 8B CE                        mov rcx, r14
00408F98  E8 B3 56 EA FF                  call 0x1402ae650
00408F9D  85 C0                           test eax, eax
00408F9F  0F 85 A0 FD FF FF               jne 0x140408d45
00408FA5  E8 36 E4 E6 FF                  call 0x1402773e0
00408FAA  85 C0                           test eax, eax
00408FAC  41 0F 45 F7                     cmovne esi, r15d
00408FB0  E9 67 FD FF FF                  jmp 0x140408d1c
00408FB5  48 8B D7                        mov rdx, rdi
00408FB8  49 8B CE                        mov rcx, r14
00408FBB  E8 00 DF E0 FF                  call 0x140216ec0
00408FC0  33 FF                           xor edi, edi
00408FC2  44 8A 44 24 40                  mov r8b, byte ptr [rsp + 0x40]
00408FC7  E9 B5 FD FF FF                  jmp 0x140408d81
00408FCC  41 0B DF                        or ebx, r15d
00408FCF  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00408FD3  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
00408FD7  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00408FDC  E9 0D FD FF FF                  jmp 0x140408cee
00408FE1  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
00408FE5  E8 46 65 F6 FF                  call 0x14036f530
00408FEA  85 C0                           test eax, eax
00408FEC  0F 84 8B FC FF FF               je 0x140408c7d
00408FF2  41 8B D7                        mov edx, r15d
00408FF5  48 8B CE                        mov rcx, rsi
00408FF8  E8 A3 C7 E7 FF                  call 0x1402857a0
00408FFD  E9 7B FC FF FF                  jmp 0x140408c7d
00409002  33 D2                           xor edx, edx
00409004  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
0040900C  E8 1F ED E0 FF                  call 0x140217d30
00409011  E9 63 FE FF FF                  jmp 0x140408e79
00409016  BE A1 00 00 C0                  mov esi, 0xc00000a1
0040901B  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00409020  89 74 24 44                     mov dword ptr [rsp + 0x44], esi
00409024  48 85 FF                        test rdi, rdi
00409027  74 0D                           je 0x140409036
00409029  48 8B D7                        mov rdx, rdi
0040902C  49 8B CE                        mov rcx, r14
0040902F  E8 8C DE E0 FF                  call 0x140216ec0
00409034  33 FF                           xor edi, edi
00409036  4D 85 E4                        test r12, r12
00409039  0F 85 93 00 00 00               jne 0x1404090d2
0040903F  48 85 FF                        test rdi, rdi
00409042  75 68                           jne 0x1404090ac
00409044  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
00409048  49 8B CE                        mov rcx, r14
0040904B  E8 40 46 E7 FF                  call 0x14027d690
00409050  4C 8B B4 24 90 00 00 00         mov r14, qword ptr [rsp + 0x90]
00409058  4C 8B 9C 24 B0 00 00 00         mov r11, qword ptr [rsp + 0xb0]
00409060  45 33 C9                        xor r9d, r9d
00409063  4D 8B C3                        mov r8, r11
00409066  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
0040906E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00409073  E8 18 65 47 00                  call 0x14087f590
00409078  F6 C3 02                        test bl, 2
0040907B  74 0F                           je 0x14040908c
0040907D  33 D2                           xor edx, edx
0040907F  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
00409087  E8 A4 EC E0 FF                  call 0x140217d30
0040908C  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
00409091  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00409096  E8 45 E8 EE FF                  call 0x1402f78e0
0040909B  33 D2                           xor edx, edx
0040909D  49 8B CE                        mov rcx, r14
004090A0  E8 CB 97 77 00                  call 0x140b82870
004090A5  8B C6                           mov eax, esi
004090A7  E9 2A FE FF FF                  jmp 0x140408ed6
004090AC  48 8B D7                        mov rdx, rdi
004090AF  49 8B CE                        mov rcx, r14
004090B2  E8 09 DE E0 FF                  call 0x140216ec0
004090B7  EB 8B                           jmp 0x140409044
004090B9  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
004090BE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
004090C3  E8 18 E8 EE FF                  call 0x1402f78e0
004090C8  B8 9A 00 00 C0                  mov eax, 0xc000009a
004090CD  E9 04 FE FF FF                  jmp 0x140408ed6
004090D2  49 8D 4C 24 FF                  lea rcx, [r12 - 1]
004090D7  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
004090DC  49 8B C4                        mov rax, r12
004090DF  48 C1 E0 0C                     shl rax, 0xc
004090E3  4C 8B AC 24 A0 00 00 00         mov r13, qword ptr [rsp + 0xa0]
004090EB  49 81 C5 00 F0 FF FF            add r13, -0x1000
004090F2  4C 03 E8                        add r13, rax
004090F5  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
004090FA  40 8A 74 24 40                  mov sil, byte ptr [rsp + 0x40]
004090FF  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
00409107  48 0F A3 08                     bt qword ptr [rax], rcx
0040910B  0F 92 C0                        setb al
0040910E  41 3A C7                        cmp al, r15b
00409111  75 37                           jne 0x14040914a
00409113  4D 8B E5                        mov r12, r13
00409116  49 C1 EC 12                     shr r12, 0x12
0040911A  41 81 E4 F8 FF FF 3F            and r12d, 0x3ffffff8
00409121  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
0040912B  48 8B C0                        mov rax, rax
0040912E  4C 03 E0                        add r12, rax
00409131  49 3B FC                        cmp rdi, r12
00409134  0F 85 C7 01 00 00               jne 0x140409301
0040913A  49 8B D5                        mov rdx, r13
0040913D  49 8B CE                        mov rcx, r14
00409140  E8 DF ED FF FF                  call 0x140407f24
00409145  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0040914A  45 33 E4                        xor r12d, r12d
0040914D  F6 C1 0F                        test cl, 0xf
00409150  74 5D                           je 0x1404091af
00409152  45 85 E4                        test r12d, r12d
00409155  0F 85 C9 01 00 00               jne 0x140409324
0040915B  49 81 ED 00 10 00 00            sub r13, 0x1000
00409162  49 2B CF                        sub rcx, r15
00409165  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0040916A  49 2B DF                        sub rbx, r15
0040916D  75 90                           jne 0x1404090ff
0040916F  8B 5C 24 50                     mov ebx, dword ptr [rsp + 0x50]
00409173  8B 74 24 44                     mov esi, dword ptr [rsp + 0x44]
00409177  E9 C3 FE FF FF                  jmp 0x14040903f
0040917C  BE 05 00 00 C0                  mov esi, 0xc0000005
00409181  E9 DA FE FF FF                  jmp 0x140409060
00409186  8B 05 2C D9 BB 00               mov eax, dword ptr [rip + 0xbbd92c]
0040918C  A8 40                           test al, 0x40
0040918E  0F 84 70 FC FF FF               je 0x140408e04
00409194  E8 F7 62 F0 FF                  call 0x14030f490
00409199  84 C0                           test al, al
0040919B  0F 84 63 FC FF FF               je 0x140408e04
004091A1  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
004091A5  E8 B6 62 F0 FF                  call 0x14030f460
004091AA  E9 57 FC FF FF                  jmp 0x140408e06
004091AF  33 D2                           xor edx, edx
004091B1  49 8B CE                        mov rcx, r14
004091B4  E8 67 53 EA FF                  call 0x1402ae520
004091B9  85 C0                           test eax, eax
004091BB  0F 85 63 01 00 00               jne 0x140409324
004091C1  48 85 FF                        test rdi, rdi
004091C4  74 13                           je 0x1404091d9
004091C6  48 8B D7                        mov rdx, rdi
004091C9  49 8B CE                        mov rcx, r14
004091CC  E8 7F 54 EA FF                  call 0x1402ae650
004091D1  85 C0                           test eax, eax
004091D3  0F 85 4B 01 00 00               jne 0x140409324
004091D9  E8 02 E2 E6 FF                  call 0x1402773e0
004091DE  85 C0                           test eax, eax
004091E0  45 0F 45 E7                     cmovne r12d, r15d
004091E4  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
004091E9  E9 64 FF FF FF                  jmp 0x140409152
004091EE  BE 4D 00 00 C0                  mov esi, 0xc000004d
004091F3  E9 68 FE FF FF                  jmp 0x140409060
004091F8  BE 05 00 00 C0                  mov esi, 0xc0000005
004091FD  E9 19 FE FF FF                  jmp 0x14040901b
00409202  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00409206  48 85 C0                        test rax, rax
00409209  79 4B                           jns 0x140409256
0040920B  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0040920F  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00409219  48 23 C1                        and rax, rcx
0040921C  48 8D 0C 40                     lea rcx, [rax + rax*2]
00409220  48 C1 E1 04                     shl rcx, 4
00409224  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0040922E  48 8B C0                        mov rax, rax
00409231  48 03 C8                        add rcx, rax
00409234  41 8B D7                        mov edx, r15d
00409237  E8 04 EF FF FF                  call 0x140408140
0040923C  EB 18                           jmp 0x140409256
0040923E  BA 02 00 00 00                  mov edx, 2
00409243  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00409248  E8 F3 EE FF FF                  call 0x140408140
0040924D  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00409251  48 85 C0                        test rax, rax
00409254  78 54                           js 0x1404092aa
00409256  BE 9A 00 00 C0                  mov esi, 0xc000009a
0040925B  E9 BB FD FF FF                  jmp 0x14040901b
00409260  BA 02 00 00 00                  mov edx, 2
00409265  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0040926A  E8 D1 EE FF FF                  call 0x140408140
0040926F  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00409273  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
0040927D  48 23 C1                        and rax, rcx
00409280  48 8D 0C 40                     lea rcx, [rax + rax*2]
00409284  48 C1 E1 04                     shl rcx, 4
00409288  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00409292  48 8B C0                        mov rax, rax
00409295  48 03 C8                        add rcx, rax
00409298  41 8B D7                        mov edx, r15d
0040929B  E8 A0 EE FF FF                  call 0x140408140
004092A0  BE 2D 01 00 C0                  mov esi, 0xc000012d
004092A5  E9 71 FD FF FF                  jmp 0x14040901b
004092AA  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
004092AE  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
004092B8  48 23 C1                        and rax, rcx
004092BB  48 8D 0C 40                     lea rcx, [rax + rax*2]
004092BF  48 C1 E1 04                     shl rcx, 4
004092C3  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004092CD  48 8B C0                        mov rax, rax
004092D0  48 03 C8                        add rcx, rax
004092D3  41 8B D7                        mov edx, r15d
004092D6  E8 65 EE FF FF                  call 0x140408140
004092DB  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
004092DE  48 0F BA E0 0A                  bt rax, 0xa
004092E3  0F 83 6D FF FF FF               jae 0x140409256
004092E9  45 33 C0                        xor r8d, r8d
004092EC  49 8B D7                        mov rdx, r15
004092EF  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
004092F7  E8 14 F1 E3 FF                  call 0x140248410
004092FC  E9 55 FF FF FF                  jmp 0x140409256
00409301  48 85 FF                        test rdi, rdi
00409304  74 0B                           je 0x140409311
00409306  48 8B D7                        mov rdx, rdi
00409309  49 8B CE                        mov rcx, r14
0040930C  E8 AF DB E0 FF                  call 0x140216ec0
00409311  49 8B FC                        mov rdi, r12
00409314  49 8B D4                        mov rdx, r12
00409317  49 8B CE                        mov rcx, r14
0040931A  E8 71 55 E3 FF                  call 0x14023e890
0040931F  E9 16 FE FF FF                  jmp 0x14040913a
00409324  48 85 FF                        test rdi, rdi
00409327  74 0D                           je 0x140409336
00409329  48 8B D7                        mov rdx, rdi
0040932C  49 8B CE                        mov rcx, r14
0040932F  E8 8C DB E0 FF                  call 0x140216ec0
00409334  33 FF                           xor edi, edi
00409336  40 8A D6                        mov dl, sil
00409339  49 8B CE                        mov rcx, r14
0040933C  E8 4F 43 E7 FF                  call 0x14027d690
00409341  49 8B CE                        mov rcx, r14
00409344  E8 A7 38 E7 FF                  call 0x14027cbf0
00409349  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0040934E  E9 08 FE FF FF                  jmp 0x14040915b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtLockVirtualMemory(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m124;
    unsigned __int8 v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m48;
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
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pF0;

    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 10493572)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m88 = a3;
    v_stack_m80 = a2;
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm0;
    v_rbx = 0;
    v_stack_m118 = 0;
    v_stack_m100 = 0;
    v_stack_m138 = v_stack_m110;
    v_stack_m140 = v_rsp - 192;
    v_stack_m148 = v_rsp - 208;
    result = MiLockUnlockCommon(a1, a2, a3, a4);
    if (sign_flag) goto loc_00408ED6;
    v_stack_m90 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_r12 = (v_stack_mC0) - 1;
    v_r12 = (v_r12) + (v_stack_mD0);
    v_r12 = (v_r12) & (0xFFFFFFFFFFFFF000ULL);
    v_r13 = (v_stack_mD0) & (0xFFFFFFFFFFFFF000ULL);
    result = (v_r12) - (v_r13);
    result = (result) >> (12);
    result = (result) + (v_rbx + 1);
    a1 = 0;
    v_stack_m120 = 0;
    a2 = ((((unsigned __int8)(result)) & (63)) != 0) ? 1 : 0;
    result = (result) >> (6);
    a2 = (a2) + (result);
    a2 = (a2) << (3);
    result = MiAllocatePool(v_rbx + 64, a2, (unsigned int)(0x6B6C6D4DULL), a4);
    v_stack_mD8 = result;
    if (result == 0) goto loc_004090B9;
    if (0 != -1) {
        a3 = v_stack_m78;
        a2 = 0;
        a1 = v_stack_m110;
        result = KiStackAttachProcess(a1, a2, a3, a4);
        v_rbx = v_rbx + 1 + 1;
        v_stack_m118 = (unsigned int)(v_rbx);
        v_stack_m100 = (unsigned int)(v_rbx);
    }
    v_rsi = (v_stack_mD0) >> (9);
    v_rsi = (v_rsi) & (a3);
    v_rsi = (v_rsi) + (0);
    v_stack_mE0 = v_rsi;
    v_stack_mC8 = v_r13;
    a1 = (v_r12) >> (9);
    a1 = (a1) & (a3);
    a1 = (a1) + (0);
    v_stack_mA8 = a1;
    a4 = 0;
    result = MiLockVadRange(v_stack_m110, v_r13, v_r12, a4);
    v_stack_mB8 = result;
    if (result == 0) goto loc_0040917C;
    result = MiLocateAddress(v_r13, v_r13, v_r12, a4);
    v_stack_m108 = result;
    a3 = 0;
loc_00408A6C:
    if (0 < result) goto loc_00408EFA;
    result = MiVadPureReserve(v_stack_m108, v_r13, a3, result);
    v_stack_mF0 = (unsigned int)(result);
    v_rdi = 0;
    v_r14 = (v_stack_m110) + (0x400ULL);
    v_stack_mA0 = v_r14;
    v_stack_m98 = *(unsigned __int64 *)(v_r14 + 16);
loc_00408AA8:
    result = MiLockWorkingSetShared(v_r14, v_r13, a3, result);
    v_stack_m128 = (unsigned __int8)(result);
loc_00408AB7:
loc_00408ACB:
    if (v_r13 > v_r12) goto loc_00408E33;
    a2 = (*(unsigned __int8 *)(v_stack_m108 + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(v_stack_m108 + 28)));
    result = (v_r13) >> (12);
    if (result > a2) goto loc_00408E15;
loc_00408AF9:
    a1 = (v_r13) >> (18);
    a1 = (unsigned int)((a1) & (0x3FFFFFF8ULL));
    result = (v_r10) + (a1);
    v_stack_mF8 = result;
    if (0 != result) goto loc_00408D78;
loc_00408B1A:
    if ((((unsigned __int8)(v_rbx + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rsi)))) != 0) goto loc_00408B81;
    result = MiUnlockPageTable(v_r14, 0, (unsigned __int8)(result), v_stack_m108);
    v_rdi = 0;
    v_stack_mF8 = 0;
    result = MiUnlockWorkingSetShared(v_r14, v_stack_m128, (unsigned __int8)(result), v_stack_m108);
    goto loc_00408AA8;
loc_00408B81:
    result = (*(unsigned __int8 *)(v_r13)) >> (12);
    result = (result) & (v_r14);
    v_rsi = (result + result * 2) << (4);
    v_rsi = (v_rsi) + (result);
    result = MiGetWsleContents(v_r14, v_r13, (unsigned __int8)(result), v_stack_m108);
    result = (unsigned __int8)((result) & (15));
    if (((unsigned __int8)(result)) == 8) goto loc_00408FCC;
    result = (*(unsigned __int64 *)(v_stack_m98 + 32)) + (6);
    if ((*(unsigned __int64 *)(v_r14 + 112)) <= result) goto loc_00409016;
    if (sign_flag) goto loc_00408F56;
loc_00408BD9:
    result = (*(unsigned __int64 *)(v_stack_mF8)) >> (12);
    result = (result) & (v_r14);
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    v_stack_mF8 = a1;
    result = MiLockPageTablePage(a1, 2, (unsigned __int8)(result), v_stack_m108);
    if ((unsigned int)(result) == 0) goto loc_00409202;
    if (condition_is_above_or_equal) goto loc_00408FE1;
    if (!sign_flag) goto loc_00408C7D;
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_mE8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10646589) + result * 8);
    a3 = 0;
    result = MiChargeCommit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10646589) + result * 8), v_rbx + 1, a3, v_stack_m108);
    if ((unsigned int)(result) == 0) goto loc_00409260;
loc_00408C7D:
    result = MiSetVaAgeList(v_r14, v_r13, (unsigned int)((unsigned int)(v_rbx + 1)), 8);
    if ((unsigned int)(result) == 0) goto loc_0040923E;
    result = MiGetEffectivePagePriorityThread(v_stack_m90, v_r13, (unsigned int)((unsigned int)(v_rbx + 1)), 8);
    v_stack_mE8 = (unsigned int)(result);
loc_00408CAF:
    if (condition_is_below) goto loc_00408DED;
    a3 = 0;
    result = MiUpdatePfnPriority(v_rsi, (unsigned int)(v_stack_mE8), a3, 8);
loc_00408CEE:
    result = (v_stack_m120) + (v_rbx + 1);
    v_stack_m120 = result;
    result = (v_stack_mE0) + (8);
    v_stack_mE0 = result;
    v_r13 = (v_r13) + (0x1000ULL);
    v_rsi = 0;
    if (v_r13 <= v_r12) goto loc_00408F78;
loc_00408D1C:
    if (0 == 0) goto loc_00408ACB;
loc_00408D45:
    result = MiUnlockPageTable(v_r14, 0, v_stack_m128, 8);
    result = MiUnlockWorkingSetShared(v_r14, v_stack_m128, v_stack_m128, 8);
    v_rdi = 0;
    result = MiLockWorkingSetShared(v_r14, v_stack_m128, v_stack_m128, 8);
    goto loc_00408AB7;
loc_00408D78:
    if (0 != 0) goto loc_00408FB5;
loc_00408D81:
    a4 = 0;
    if (v_stack_mF0 == 0) goto loc_00408F1A;
    v_stack_m148 = v_stack_mB0;
    result = MiGetNextPageTable(v_stack_mE0, v_stack_mA8, v_stack_m128, a4);
    if (result != 0) {
        v_rdi = result;
        v_rdi = (v_rdi) >> (9);
        v_rdi = (v_rdi) & (v_stack_mE0);
        a1 = v_stack_mE0;
        v_rdi = (v_rdi) + (a1);
    }
    if (result != v_stack_mE0) goto loc_004091F8;
loc_00408DDE:
    goto loc_00408B1A;
loc_00408DED:
    a1 = (unsigned int)(((unsigned int)(v_stack_m124)) + ((unsigned int)(v_rbx + 1)));
    v_stack_m124 = (unsigned int)(a1);
    if (((*(unsigned int *)(v_rip + 12305582)) & ((unsigned int)(a1))) == 0) goto loc_00409186;
loc_00408E04:
loc_00408E06:
    if (!sign_flag) goto loc_00408CAF;
    goto loc_00408DED;
loc_00408E15:
    result = MiGetNextVad(0, v_stack_mA8, v_stack_m128, a4);
    v_stack_m108 = result;
    result = MiVadPureReserve(result, v_stack_mA8, v_stack_m128, a4);
    v_stack_mF0 = (unsigned int)(result);
    goto loc_00408AF9;
loc_00408E33:
    if (v_rdi != 0) {
        a2 = v_rdi;
        a1 = v_r14;
        result = MiUnlockPageTable(a1, a2, v_stack_m128, a4);
        a3 = v_stack_m128;
    }
    result = MiUnlockWorkingSetShared(v_r14, (unsigned __int8)(a3), a3, a4);
    a4 = 0;
    result = MiUnlockVadRange(v_stack_m110, v_stack_mC8, v_stack_mB8, a4);
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_00409002;
loc_00408E79:
    result = ObfDereferenceObjectWithTag(v_stack_m110, (unsigned int)(0x6D566D4DULL), v_stack_mB8, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mD8, a2, v_stack_mB8, a4);
    result = (v_stack_mD0) & (0xFFFFFFFFFFFFF000ULL);
    v_r12 = (v_r12) - (result);
    v_r12 = (v_r12) + (0x1000ULL);
    *(unsigned __int64 *)(v_stack_m88) = v_r12;
    *(unsigned __int64 *)(v_stack_m80) = result;
    goto loc_00408ECA;
loc_00408ECA:
    v_rbx = (unsigned __int8)((v_rbx) & ((unsigned __int8)(v_rbx + 1)));
    v_rbx = (unsigned __int8)(-(v_rbx));
    result = (unsigned int)((result) & (0x40000019ULL));
loc_00408ED6:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_mB8, a4);
    v_rsp = (v_rsp) + (304);
    return result;
loc_00408EFA:
    result = MiVadPagesTradable(0, a2, v_stack_mB8, a4);
    if ((unsigned int)(result) == 0) goto loc_004091EE;
    result = MiGetNextVad(0, a2, v_stack_mB8, a4);
    a3 = (v_stack_mB8) + (v_rbx + 1);
    goto loc_00408A6C;
loc_00408F1A:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p60 + 48))) >> (12));
    a2 = (unsigned int)((a2) & (127));
    result = MiMakeSystemAddressValid(0, a2, a3, a4);
    v_rdi = (v_stack_mE0) >> (9);
    v_rdi = (v_rdi) & (result);
    v_rdi = (v_rdi) + (result);
    goto loc_00408DDE;
loc_00408F56:
    result = MiLockPageTablePage(v_stack_mE0, (unsigned int)((unsigned int)(v_rbx + 1)), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00409256;
    goto loc_00408BD9;
loc_00408F78:
    if ((((unsigned __int8)(result)) & (120)) != 0) goto loc_00408D1C;
    a2 = 0;
    result = MiWorkingSetIsContended(v_r14, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00408D45;
    result = MiPageTableLockIsContended(v_r14, v_rdi, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00408D45;
    result = KeShouldYieldProcessor(v_r14, v_rdi, a3, a4);
    v_rsi = v_stack_mE0;
    if ((unsigned int)(result) != 0) { v_rsi = (unsigned int)(v_rbx + 1); }
    goto loc_00408D1C;
loc_00408FB5:
    result = MiUnlockPageTable(v_r14, v_rdi, a3, a4);
    v_rdi = 0;
    goto loc_00408D81;
loc_00408FCC:
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(v_rbx + 1)));
    v_stack_p50 = (unsigned int)(v_rbx);
    v_stack_p68 = (unsigned int)(v_rbx);
    goto loc_00408CEE;
loc_00408FE1:
    result = MiGetPagingFileOffset(*(unsigned __int64 *)(v_rsi + 16), v_rdi, v_stack_p40, a4);
    if ((unsigned int)(result) == 0) goto loc_00408C7D;
    result = MiLockPageAndSetDirty(v_rsi, (unsigned int)((unsigned int)(v_rbx + 1)), v_stack_p40, a4);
    goto loc_00408C7D;
loc_00409002:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF0, a2, v_stack_p40, a4);
    goto loc_00408E79;
loc_00409016:
loc_0040901B:
    v_stack_p44 = (unsigned int)((unsigned int)(0xC00000A1ULL));
loc_00409024:
    if (0 != 0) {
        a2 = 0;
        a1 = v_r14;
        result = MiUnlockPageTable(a1, a2, v_stack_p40, a4);
        v_rdi = 0;
    }
    if (v_stack_p48 != 0) goto loc_004090D2;
loc_0040903F:
    if (0 != 0) goto loc_004090AC;
loc_00409044:
    result = MiUnlockWorkingSetShared(v_r14, v_stack_p40, v_stack_p40, a4);
loc_00409060:
    a4 = 0;
    result = MiUnlockVadRange(v_stack_p58, v_stack_pA0, v_stack_pB0, a4);
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) {
        a2 = 0;
        a1 = v_stack_pF0;
        result = KiUnstackDetachProcess(a1, a2, v_stack_pB0, a4);
    }
    result = ObfDereferenceObjectWithTag(v_stack_p58, (unsigned int)(0x6D566D4DULL), v_stack_pB0, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p90, a2, v_stack_pB0, a4);
    goto loc_00408ED6;
loc_004090AC:
    result = MiUnlockPageTable(v_stack_p90, 0, v_stack_pB0, a4);
    goto loc_00409044;
loc_004090B9:
    result = ObfDereferenceObjectWithTag(v_stack_p58, (unsigned int)(0x6D566D4DULL), v_stack_pB0, a4);
    goto loc_00408ED6;
loc_004090D2:
    v_stack_p60 = v_stack_p48 - 1;
    result = (v_stack_p48) << (12);
    v_r13 = (v_stack_pA0) + (0xFFFFFFFFFFFFF000ULL);
    v_r13 = (v_r13) + (result);
loc_004090FF:
    result = (condition_is_below) ? 1 : 0;
    if (((unsigned __int8)(result)) != ((unsigned __int8)(v_rbx + 1))) goto loc_0040914A;
    v_r12 = (v_r13) >> (18);
    v_r12 = (unsigned int)((v_r12) & (0x3FFFFFF8ULL));
    v_r12 = (v_r12) + (result);
    if (0 != v_r12) goto loc_00409301;
loc_0040913A:
    result = MiUnlockVa(v_stack_p90, v_r13, v_stack_pB0, a4);
loc_0040914A:
    v_r12 = 0;
    if ((((unsigned __int8)(v_stack_p60)) & (15)) == 0) goto loc_004091AF;
loc_00409152:
    if (0 != 0) goto loc_00409324;
loc_0040915B:
    v_r13 = (v_r13) - (0x1000ULL);
    a1 = (v_stack_p60) - (v_rbx + 1);
    v_stack_p60 = a1;
    v_rbx = (v_stack_p48) - (v_rbx + 1);
    if (condition_is_not_equal) goto loc_004090FF;
    goto loc_0040903F;
loc_0040917C:
    goto loc_00409060;
loc_00409186:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12310828)))) & (64)) == 0) goto loc_00408E04;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, v_r13, v_stack_pB0, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00408E04;
    result = HvlNotifyLongSpinWait((unsigned int)(v_stack_p44), v_r13, v_stack_pB0, a4);
    goto loc_00408E06;
loc_004091AF:
    a2 = 0;
    result = MiWorkingSetIsContended(v_stack_p90, a2, v_stack_pB0, a4);
    if ((unsigned int)(result) != 0) goto loc_00409324;
    if (0 == 0) goto loc_004091D9;
    result = MiPageTableLockIsContended(v_stack_p90, 0, v_stack_pB0, a4);
    if ((unsigned int)(result) != 0) goto loc_00409324;
loc_004091D9:
    result = KeShouldYieldProcessor(v_stack_p90, 0, v_stack_pB0, a4);
    if ((unsigned int)(result) != 0) { v_r12 = (unsigned int)(v_rbx + 1); }
    goto loc_00409152;
loc_004091EE:
    goto loc_00409060;
loc_004091F8:
    goto loc_0040901B;
loc_00409202:
    if (!sign_flag) goto loc_00409256;
    result = (*(unsigned __int64 *)((unsigned int)(0xC0000005ULL) + 40)) & (v_stack_p60);
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    result = MiUnlockPageTableCharges(a1, (unsigned int)((unsigned int)(v_rbx + 1)), v_stack_pB0, a4);
    goto loc_00409256;
loc_0040923E:
    result = MiUnlockPageTableCharges(v_stack_p70, 2, v_stack_pB0, a4);
    if (sign_flag) goto loc_004092AA;
loc_00409256:
    goto loc_0040901B;
loc_00409260:
    result = MiUnlockPageTableCharges(v_stack_p70, 2, v_stack_pB0, a4);
    result = (*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 40)) & (v_stack_p70);
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    result = MiUnlockPageTableCharges(a1, (unsigned int)((unsigned int)(v_rbx + 1)), v_stack_pB0, a4);
    goto loc_0040901B;
loc_004092AA:
    result = (*(unsigned __int64 *)((unsigned int)(0xC000012DULL) + 40)) & (a1);
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    result = MiUnlockPageTableCharges(a1, (unsigned int)((unsigned int)(v_rbx + 1)), v_stack_pB0, a4);
    if (condition_is_above_or_equal) goto loc_00409256;
    a3 = 0;
    result = MiReturnCommit(v_stack_p80, v_rbx + 1, a3, a4);
    goto loc_00409256;
loc_00409301:
    if (0 != 0) {
        a2 = 0;
        a1 = v_stack_p90;
        result = MiUnlockPageTable(a1, a2, a3, a4);
    }
    result = MiLockNestedPageTable(v_stack_p90, v_r12, a3, a4);
    goto loc_0040913A;
loc_00409324:
    v_rdi = v_r12;
    if (v_r12 != 0) {
        a2 = v_r12;
        a1 = v_stack_p90;
        result = MiUnlockPageTable(a1, a2, a3, a4);
        v_rdi = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_p90, (unsigned __int8)((unsigned int)(0xC000012DULL)), a3, a4);
    result = MiLockWorkingSetShared(v_stack_p90, (unsigned __int8)((unsigned int)(0xC000012DULL)), a3, a4);
    goto loc_0040915B;
}
```

## 5. (Beta) C Style

```c
int64_t NtLockVirtualMemory(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m124;
    uint8_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m48;
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
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint8_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p80;
    uint64_t v_stack_p90;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pF0;

    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0xA01E84)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m88 = Arg3;
    v_stack_m80 = Arg2;
    *(uint64_t *)(local_rsp - 0x78) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm0;
    local_rbx = 0;
    v_stack_m118 = 0;
    v_stack_m100 = 0;
    v_stack_m138 = v_stack_m110;
    v_stack_m140 = local_rsp - 192;
    v_stack_m148 = local_rsp - 208;
    result = MiLockUnlockCommon(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00408ED6;
    v_stack_m90 = *(uint64_t *)(gs_base + (0 + 0x188));
    local_r12 = (v_stack_mC0) - 1;
    local_r12 = (local_r12) + (v_stack_mD0);
    local_r12 = (local_r12) & (0xFFFFFFFFFFFFF000ULL);
    local_r13 = (v_stack_mD0) & (0xFFFFFFFFFFFFF000ULL);
    result = (local_r12) - (local_r13);
    result = (result) >> (12);
    result = (result) + (local_rbx + 1);
    Arg1 = 0;
    v_stack_m120 = 0;
    Arg2 = ((((uint8_t)(result)) & (63)) != 0) ? 1 : 0;
    result = (result) >> (6);
    Arg2 = (Arg2) + (result);
    Arg2 = (Arg2) << (3);
    result = MiAllocatePool(local_rbx + 64, Arg2, (uint32_t)(0x6B6C6D4DULL), Arg4);
    v_stack_mD8 = result;
    if (result == 0) goto loc_004090B9;
    if (0 != -1) {
        Arg3 = v_stack_m78;
        Arg2 = 0;
        Arg1 = v_stack_m110;
        result = KiStackAttachProcess(Arg1, Arg2, Arg3, Arg4);
        local_rbx = local_rbx + 1 + 1;
        v_stack_m118 = (uint32_t)(local_rbx);
        v_stack_m100 = (uint32_t)(local_rbx);
    }
    local_rsi = (v_stack_mD0) >> (9);
    local_rsi = (local_rsi) & (Arg3);
    local_rsi = (local_rsi) + (0);
    v_stack_mE0 = local_rsi;
    v_stack_mC8 = local_r13;
    Arg1 = (local_r12) >> (9);
    Arg1 = (Arg1) & (Arg3);
    Arg1 = (Arg1) + (0);
    v_stack_mA8 = Arg1;
    Arg4 = 0;
    result = MiLockVadRange(v_stack_m110, local_r13, local_r12, Arg4);
    v_stack_mB8 = result;
    if (result == 0) goto loc_0040917C;
    result = MiLocateAddress(local_r13, local_r13, local_r12, Arg4);
    v_stack_m108 = result;
    Arg3 = 0;
loc_00408A6C:
    if (0 < result) goto loc_00408EFA;
    result = MiVadPureReserve(v_stack_m108, local_r13, Arg3, result);
    v_stack_mF0 = (uint32_t)(result);
    local_rdi = 0;
    local_r14 = (v_stack_m110) + (0x400ULL);
    v_stack_mA0 = local_r14;
    v_stack_m98 = *(uint64_t *)(local_r14 + 0x10);
loc_00408AA8:
    result = MiLockWorkingSetShared(local_r14, local_r13, Arg3, result);
    v_stack_m128 = (uint8_t)(result);
loc_00408AB7:
loc_00408ACB:
    if (local_r13 > local_r12) goto loc_00408E33;
    Arg2 = (*(uint8_t *)(v_stack_m108 + 0x21)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(v_stack_m108 + 0x1C)));
    result = (local_r13) >> (12);
    if (result > Arg2) goto loc_00408E15;
loc_00408AF9:
    Arg1 = (local_r13) >> (18);
    Arg1 = (uint32_t)((Arg1) & (0x3FFFFFF8ULL));
    result = (local_r10) + (Arg1);
    v_stack_mF8 = result;
    if (0 != result) goto loc_00408D78;
loc_00408B1A:
    if ((((uint8_t)(local_rbx + 1)) & ((uint8_t)(*(uint64_t *)(local_rsi)))) != 0) goto loc_00408B81;
    result = MiUnlockPageTable(local_r14, 0, (uint8_t)(result), v_stack_m108);
    local_rdi = 0;
    v_stack_mF8 = 0;
    result = MiUnlockWorkingSetShared(local_r14, v_stack_m128, (uint8_t)(result), v_stack_m108);
    goto loc_00408AA8;
loc_00408B81:
    result = (*(uint8_t *)(local_r13)) >> (12);
    result = (result) & (local_r14);
    local_rsi = (result + result * 2) << (4);
    local_rsi = (local_rsi) + (result);
    result = MiGetWsleContents(local_r14, local_r13, (uint8_t)(result), v_stack_m108);
    result = (uint8_t)((result) & (15));
    if (((uint8_t)(result)) == 8) goto loc_00408FCC;
    result = (*(uint64_t *)(v_stack_m98 + 0x20)) + (6);
    if ((*(uint64_t *)(local_r14 + 0x70)) <= result) goto loc_00409016;
    if (sign_flag) goto loc_00408F56;
loc_00408BD9:
    result = (*(uint64_t *)(v_stack_mF8)) >> (12);
    result = (result) & (local_r14);
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    v_stack_mF8 = Arg1;
    result = MiLockPageTablePage(Arg1, 2, (uint8_t)(result), v_stack_m108);
    if ((uint32_t)(result) == 0) goto loc_00409202;
    if (condition_is_above_or_equal) goto loc_00408FE1;
    if (!sign_flag) goto loc_00408C7D;
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_mE8 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xA2743D) + result * 8);
    Arg3 = 0;
    result = MiChargeCommit(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA2743D) + result * 8), local_rbx + 1, Arg3, v_stack_m108);
    if ((uint32_t)(result) == 0) goto loc_00409260;
loc_00408C7D:
    result = MiSetVaAgeList(local_r14, local_r13, (uint32_t)((uint32_t)(local_rbx + 1)), 8);
    if ((uint32_t)(result) == 0) goto loc_0040923E;
    result = MiGetEffectivePagePriorityThread(v_stack_m90, local_r13, (uint32_t)((uint32_t)(local_rbx + 1)), 8);
    v_stack_mE8 = (uint32_t)(result);
loc_00408CAF:
    if (condition_is_below) goto loc_00408DED;
    Arg3 = 0;
    result = MiUpdatePfnPriority(local_rsi, (uint32_t)(v_stack_mE8), Arg3, 8);
loc_00408CEE:
    result = (v_stack_m120) + (local_rbx + 1);
    v_stack_m120 = result;
    result = (v_stack_mE0) + (8);
    v_stack_mE0 = result;
    local_r13 = (local_r13) + (0x1000ULL);
    local_rsi = 0;
    if (local_r13 <= local_r12) goto loc_00408F78;
loc_00408D1C:
    if (0 == 0) goto loc_00408ACB;
loc_00408D45:
    result = MiUnlockPageTable(local_r14, 0, v_stack_m128, 8);
    result = MiUnlockWorkingSetShared(local_r14, v_stack_m128, v_stack_m128, 8);
    local_rdi = 0;
    result = MiLockWorkingSetShared(local_r14, v_stack_m128, v_stack_m128, 8);
    goto loc_00408AB7;
loc_00408D78:
    if (0 != 0) goto loc_00408FB5;
loc_00408D81:
    Arg4 = 0;
    if (v_stack_mF0 == 0) goto loc_00408F1A;
    v_stack_m148 = v_stack_mB0;
    result = MiGetNextPageTable(v_stack_mE0, v_stack_mA8, v_stack_m128, Arg4);
    if (result != 0) {
        local_rdi = result;
        local_rdi = (local_rdi) >> (9);
        local_rdi = (local_rdi) & (v_stack_mE0);
        Arg1 = v_stack_mE0;
        local_rdi = (local_rdi) + (Arg1);
    }
    if (result != v_stack_mE0) goto loc_004091F8;
loc_00408DDE:
    goto loc_00408B1A;
loc_00408DED:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m124)) + ((uint32_t)(local_rbx + 1)));
    v_stack_m124 = (uint32_t)(Arg1);
    if (((*(uint32_t *)(v_rip + 0xBBC4AE)) & ((uint32_t)(Arg1))) == 0) goto loc_00409186;
loc_00408E04:
loc_00408E06:
    if (!sign_flag) goto loc_00408CAF;
    goto loc_00408DED;
loc_00408E15:
    result = MiGetNextVad(0, v_stack_mA8, v_stack_m128, Arg4);
    v_stack_m108 = result;
    result = MiVadPureReserve(result, v_stack_mA8, v_stack_m128, Arg4);
    v_stack_mF0 = (uint32_t)(result);
    goto loc_00408AF9;
loc_00408E33:
    if (local_rdi != 0) {
        Arg2 = local_rdi;
        Arg1 = local_r14;
        result = MiUnlockPageTable(Arg1, Arg2, v_stack_m128, Arg4);
        Arg3 = v_stack_m128;
    }
    result = MiUnlockWorkingSetShared(local_r14, (uint8_t)(Arg3), Arg3, Arg4);
    Arg4 = 0;
    result = MiUnlockVadRange(v_stack_m110, v_stack_mC8, v_stack_mB8, Arg4);
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_00409002;
loc_00408E79:
    result = ObfDereferenceObjectWithTag(v_stack_m110, (uint32_t)(0x6D566D4DULL), v_stack_mB8, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mD8, Arg2, v_stack_mB8, Arg4);
    result = (v_stack_mD0) & (0xFFFFFFFFFFFFF000ULL);
    local_r12 = (local_r12) - (result);
    local_r12 = (local_r12) + (0x1000ULL);
    *(uint64_t *)(v_stack_m88) = local_r12;
    *(uint64_t *)(v_stack_m80) = result;
    goto loc_00408ECA;
loc_00408ECA:
    local_rbx = (uint8_t)((local_rbx) & ((uint8_t)(local_rbx + 1)));
    local_rbx = (uint8_t)(-(local_rbx));
    result = (uint32_t)((result) & (0x40000019ULL));
loc_00408ED6:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_mB8, Arg4);
    local_rsp = (local_rsp) + (304);
    return result;
loc_00408EFA:
    result = MiVadPagesTradable(0, Arg2, v_stack_mB8, Arg4);
    if ((uint32_t)(result) == 0) goto loc_004091EE;
    result = MiGetNextVad(0, Arg2, v_stack_mB8, Arg4);
    Arg3 = (v_stack_mB8) + (local_rbx + 1);
    goto loc_00408A6C;
loc_00408F1A:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p60 + 0x30))) >> (12));
    Arg2 = (uint32_t)((Arg2) & (127));
    result = MiMakeSystemAddressValid(0, Arg2, Arg3, Arg4);
    local_rdi = (v_stack_mE0) >> (9);
    local_rdi = (local_rdi) & (result);
    local_rdi = (local_rdi) + (result);
    goto loc_00408DDE;
loc_00408F56:
    result = MiLockPageTablePage(v_stack_mE0, (uint32_t)((uint32_t)(local_rbx + 1)), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00409256;
    goto loc_00408BD9;
loc_00408F78:
    if ((((uint8_t)(result)) & (120)) != 0) goto loc_00408D1C;
    Arg2 = 0;
    result = MiWorkingSetIsContended(local_r14, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00408D45;
    result = MiPageTableLockIsContended(local_r14, local_rdi, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00408D45;
    result = KeShouldYieldProcessor(local_r14, local_rdi, Arg3, Arg4);
    local_rsi = v_stack_mE0;
    if ((uint32_t)(result) != 0) { local_rsi = (uint32_t)(local_rbx + 1); }
    goto loc_00408D1C;
loc_00408FB5:
    result = MiUnlockPageTable(local_r14, local_rdi, Arg3, Arg4);
    local_rdi = 0;
    goto loc_00408D81;
loc_00408FCC:
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(local_rbx + 1)));
    v_stack_p50 = (uint32_t)(local_rbx);
    v_stack_p68 = (uint32_t)(local_rbx);
    goto loc_00408CEE;
loc_00408FE1:
    result = MiGetPagingFileOffset(*(uint64_t *)(local_rsi + 0x10), local_rdi, v_stack_p40, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00408C7D;
    result = MiLockPageAndSetDirty(local_rsi, (uint32_t)((uint32_t)(local_rbx + 1)), v_stack_p40, Arg4);
    goto loc_00408C7D;
loc_00409002:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_pF0, Arg2, v_stack_p40, Arg4);
    goto loc_00408E79;
loc_00409016:
loc_0040901B:
    v_stack_p44 = (uint32_t)((uint32_t)(0xC00000A1ULL));
loc_00409024:
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = local_r14;
        result = MiUnlockPageTable(Arg1, Arg2, v_stack_p40, Arg4);
        local_rdi = 0;
    }
    if (v_stack_p48 != 0) goto loc_004090D2;
loc_0040903F:
    if (0 != 0) goto loc_004090AC;
loc_00409044:
    result = MiUnlockWorkingSetShared(local_r14, v_stack_p40, v_stack_p40, Arg4);
loc_00409060:
    Arg4 = 0;
    result = MiUnlockVadRange(v_stack_p58, v_stack_pA0, v_stack_pB0, Arg4);
    if ((((uint8_t)(local_rbx)) & (2)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_pF0;
        result = KiUnstackDetachProcess(Arg1, Arg2, v_stack_pB0, Arg4);
    }
    result = ObfDereferenceObjectWithTag(v_stack_p58, (uint32_t)(0x6D566D4DULL), v_stack_pB0, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p90, Arg2, v_stack_pB0, Arg4);
    goto loc_00408ED6;
loc_004090AC:
    result = MiUnlockPageTable(v_stack_p90, 0, v_stack_pB0, Arg4);
    goto loc_00409044;
loc_004090B9:
    result = ObfDereferenceObjectWithTag(v_stack_p58, (uint32_t)(0x6D566D4DULL), v_stack_pB0, Arg4);
    goto loc_00408ED6;
loc_004090D2:
    v_stack_p60 = v_stack_p48 - 1;
    result = (v_stack_p48) << (12);
    local_r13 = (v_stack_pA0) + (0xFFFFFFFFFFFFF000ULL);
    local_r13 = (local_r13) + (result);
loc_004090FF:
    result = (condition_is_below) ? 1 : 0;
    if (((uint8_t)(result)) != ((uint8_t)(local_rbx + 1))) goto loc_0040914A;
    local_r12 = (local_r13) >> (18);
    local_r12 = (uint32_t)((local_r12) & (0x3FFFFFF8ULL));
    local_r12 = (local_r12) + (result);
    if (0 != local_r12) goto loc_00409301;
loc_0040913A:
    result = MiUnlockVa(v_stack_p90, local_r13, v_stack_pB0, Arg4);
loc_0040914A:
    local_r12 = 0;
    if ((((uint8_t)(v_stack_p60)) & (15)) == 0) goto loc_004091AF;
loc_00409152:
    if (0 != 0) goto loc_00409324;
loc_0040915B:
    local_r13 = (local_r13) - (0x1000ULL);
    Arg1 = (v_stack_p60) - (local_rbx + 1);
    v_stack_p60 = Arg1;
    local_rbx = (v_stack_p48) - (local_rbx + 1);
    if (condition_is_not_equal) goto loc_004090FF;
    goto loc_0040903F;
loc_0040917C:
    goto loc_00409060;
loc_00409186:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBBD92C)))) & (64)) == 0) goto loc_00408E04;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, local_r13, v_stack_pB0, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00408E04;
    result = HvlNotifyLongSpinWait((uint32_t)(v_stack_p44), local_r13, v_stack_pB0, Arg4);
    goto loc_00408E06;
loc_004091AF:
    Arg2 = 0;
    result = MiWorkingSetIsContended(v_stack_p90, Arg2, v_stack_pB0, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00409324;
    if (0 == 0) goto loc_004091D9;
    result = MiPageTableLockIsContended(v_stack_p90, 0, v_stack_pB0, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00409324;
loc_004091D9:
    result = KeShouldYieldProcessor(v_stack_p90, 0, v_stack_pB0, Arg4);
    if ((uint32_t)(result) != 0) { local_r12 = (uint32_t)(local_rbx + 1); }
    goto loc_00409152;
loc_004091EE:
    goto loc_00409060;
loc_004091F8:
    goto loc_0040901B;
loc_00409202:
    if (!sign_flag) goto loc_00409256;
    result = (*(uint64_t *)((uint32_t)(0xC0000005ULL) + 0x28)) & (v_stack_p60);
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = MiUnlockPageTableCharges(Arg1, (uint32_t)((uint32_t)(local_rbx + 1)), v_stack_pB0, Arg4);
    goto loc_00409256;
loc_0040923E:
    result = MiUnlockPageTableCharges(v_stack_p70, 2, v_stack_pB0, Arg4);
    if (sign_flag) goto loc_004092AA;
loc_00409256:
    goto loc_0040901B;
loc_00409260:
    result = MiUnlockPageTableCharges(v_stack_p70, 2, v_stack_pB0, Arg4);
    result = (*(uint64_t *)((uint32_t)(0xC000009AULL) + 0x28)) & (v_stack_p70);
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = MiUnlockPageTableCharges(Arg1, (uint32_t)((uint32_t)(local_rbx + 1)), v_stack_pB0, Arg4);
    goto loc_0040901B;
loc_004092AA:
    result = (*(uint64_t *)((uint32_t)(0xC000012DULL) + 0x28)) & (Arg1);
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = MiUnlockPageTableCharges(Arg1, (uint32_t)((uint32_t)(local_rbx + 1)), v_stack_pB0, Arg4);
    if (condition_is_above_or_equal) goto loc_00409256;
    Arg3 = 0;
    result = MiReturnCommit(v_stack_p80, local_rbx + 1, Arg3, Arg4);
    goto loc_00409256;
loc_00409301:
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_p90;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiLockNestedPageTable(v_stack_p90, local_r12, Arg3, Arg4);
    goto loc_0040913A;
loc_00409324:
    local_rdi = local_r12;
    if (local_r12 != 0) {
        Arg2 = local_r12;
        Arg1 = v_stack_p90;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, Arg4);
        local_rdi = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_p90, (uint8_t)((uint32_t)(0xC000012DULL)), Arg3, Arg4);
    result = MiLockWorkingSetShared(v_stack_p90, (uint8_t)((uint32_t)(0xC000012DULL)), Arg3, Arg4);
    goto loc_0040915B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004088A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
