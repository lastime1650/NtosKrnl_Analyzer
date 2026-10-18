# ExpAcquireSharedStarveExclusive

- RVA: `0x003411C0`–`0x003417F0` (길이 `1,584` bytes)
- VA: `0x00000001403411C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077570`
- 디코드: `397`개 명령, `1,584/1,584` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00341295` → [KeReleaseInStackQueuedSpinLock](KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00341334` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0034136E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0034147F` → [ExpGetThreadResourceHint](../21/ExpGetThreadResourceHint_function_002134C0.md) (function, `0x002134C0`)
- `0x00341514` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x0034155F` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003415AC` → [KeReleaseInStackQueuedSpinLock](KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003415D9` → [PerfLogExecutiveResourceAcquire](../47/PerfLogExecutiveResourceAcquire_function_004795E8.md) (function, `0x004795E8`)
- `0x0034166A` → [KeReleaseInStackQueuedSpinLock](KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00341672` → [ExpGetThreadResourceHint](../21/ExpGetThreadResourceHint_function_002134C0.md) (function, `0x002134C0`)
- `0x00341680` → [ExpBoostIoAfterAcquire](../21/ExpBoostIoAfterAcquire_function_00215CE0.md) (function, `0x00215CE0`)
- `0x003416A9` → [PerfLogExecutiveResourceAcquire](../47/PerfLogExecutiveResourceAcquire_function_004795E8.md) (function, `0x004795E8`)
- `0x003416BB` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x003416D2` → [ExpFindEmptyEntry](../3D/ExpFindEmptyEntry_function_003D4840.md) (function, `0x003D4840`)
- `0x003416EF` → [ExpExpandResourceOwnerTable](../3D/ExpExpandResourceOwnerTable_function_003D489C.md) (function, `0x003D489C`)
- `0x00341712` → [KeReleaseInStackQueuedSpinLock](KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0034173F` → [PerfLogExecutiveResourceAcquire](../47/PerfLogExecutiveResourceAcquire_function_004795E8.md) (function, `0x004795E8`)
- `0x00341752` → [KeReleaseInStackQueuedSpinLock](KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003417A4` → [RtlInsertHeadCircularList](../43/RtlInsertHeadCircularList_function_00433510.md) (function, `0x00433510`)
- `0x003417AD` → [KeReleaseInStackQueuedSpinLock](KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003417C2` → [ExpApplyPrewaitBoost](../21/ExpApplyPrewaitBoost_function_00213E50.md) (function, `0x00213E50`)
- `0x003417D4` → [ExpWaitForResource](../21/ExpWaitForResource_function_002166F0.md) (function, `0x002166F0`)
- `0x003417E9` → [PerfLogExecutiveResourceWait](../4B/PerfLogExecutiveResourceWait_function_004B9E90.md) (function, `0x004B9E90`)

### Direct callers
- [CcPinFileData](../33/CcPinFileData_function_0033FB40.md) at `0x0033FE80`
- [CcPinFileData](../33/CcPinFileData_function_0033FB40.md) at `0x003404FA`
- [ExAcquireSharedStarveExclusive](../3B/ExAcquireSharedStarveExclusive_function_003BDB00.md) at `0x003BDB2D`

### Static image references
- `0x0034120B` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0034123A` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00341247` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0034131A` → RVA `0x00E68468` (`.data`; read)
- `0x003414FF` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00341334` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0034136E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003411C0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003411C5  55                              push rbp
003411C6  56                              push rsi
003411C7  57                              push rdi
003411C8  41 54                           push r12
003411CA  41 55                           push r13
003411CC  41 56                           push r14
003411CE  41 57                           push r15
003411D0  48 8B EC                        mov rbp, rsp
003411D3  48 83 EC 70                     sub rsp, 0x70
003411D7  33 C0                           xor eax, eax
003411D9  48 8D 79 60                     lea rdi, [rcx + 0x60]
003411DD  0F 57 C9                        xorps xmm1, xmm1
003411E0  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
003411E4  0F 11 4D C8                     movups xmmword ptr [rbp - 0x38], xmm1
003411E8  48 89 45 F8                     mov qword ptr [rbp - 8], rax
003411EC  44 0F B6 E2                     movzx r12d, dl
003411F0  0F 11 4D D8                     movups xmmword ptr [rbp - 0x28], xmm1
003411F4  48 8B D9                        mov rbx, rcx
003411F7  0F 11 4D E8                     movups xmmword ptr [rbp - 0x18], xmm1
003411FB  0F 57 C0                        xorps xmm0, xmm0
003411FE  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00341202  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
0034120B  44 8B 3D F2 58 C8 00            mov r15d, dword ptr [rip + 0xc858f2]
00341212  41 81 E7 00 00 02 00            and r15d, 0x20000
00341219  65 FF 04 25 A4 90 00 00         inc dword ptr gs:[0x90a4]
00341221  45 33 ED                        xor r13d, r13d
00341224  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
00341228  4C 89 6D B0                     mov qword ptr [rbp - 0x50], r13
0034122C  90                              nop
0034122D  44 0F 20 C6                     mov rsi, cr8
00341231  B8 02 00 00 00                  mov eax, 2
00341236  44 0F 22 C0                     mov cr8, rax
0034123A  44 39 2D DF 5A C8 00            cmp dword ptr [rip + 0xc85adf], r13d
00341241  0F 85 11 03 00 00               jne 0x140341558
00341247  F6 05 B8 58 C8 00 21            test byte ptr [rip + 0xc858b8], 0x21
0034124E  40 88 75 C0                     mov byte ptr [rbp - 0x40], sil
00341252  0F 85 A7 02 00 00               jne 0x1403414ff
00341258  48 8D 55 B0                     lea rdx, [rbp - 0x50]
0034125C  48 87 17                        xchg qword ptr [rdi], rdx
0034125F  48 85 D2                        test rdx, rdx
00341262  0F 85 4F 04 00 00               jne 0x1403416b7
00341268  BF 01 00 00 00                  mov edi, 1
0034126D  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00341270  85 C0                           test eax, eax
00341272  0F 85 F4 01 00 00               jne 0x14034146c
00341278  FF C0                           inc eax
0034127A  66 89 7B 18                     mov word ptr [rbx + 0x18], di
0034127E  89 43 40                        mov dword ptr [rbx + 0x40], eax
00341281  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00341285  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
00341288  83 E0 07                        and eax, 7
0034128B  4C 89 73 30                     mov qword ptr [rbx + 0x30], r14
0034128F  83 C8 08                        or eax, 8
00341292  89 43 38                        mov dword ptr [rbx + 0x38], eax
00341295  E8 46 1A 00 00                  call 0x140342ce0
0034129A  65 FF 04 25 AC 90 00 00         inc dword ptr gs:[0x90ac]
003412A2  65 FF 04 25 64 90 00 00         inc dword ptr gs:[0x9064]
003412AA  45 85 FF                        test r15d, r15d
003412AD  0F 84 90 01 00 00               je 0x140341443
003412B3  8B 43 44                        mov eax, dword ptr [rbx + 0x44]
003412B6  45 33 C0                        xor r8d, r8d
003412B9  44 89 45 50                     mov dword ptr [rbp + 0x50], r8d
003412BD  89 45 58                        mov dword ptr [rbp + 0x58], eax
003412C0  0F 31                           rdtsc
003412C2  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
003412CB  48 C1 E2 20                     shl rdx, 0x20
003412CF  48 0B C2                        or rax, rdx
003412D2  44 88 45 53                     mov byte ptr [rbp + 0x53], r8b
003412D6  4C 8B F0                        mov r14, rax
003412D9  41 FF 87 70 8F 00 00            inc dword ptr [r15 + 0x8f70]
003412E0  41 0F B6 87 D1 00 00 00         movzx eax, byte ptr [r15 + 0xd1]
003412E8  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
003412F1  45 0F B6 AF D0 00 00 00         movzx r13d, byte ptr [r15 + 0xd0]
003412F9  66 44 89 6D 50                  mov word ptr [rbp + 0x50], r13w
003412FE  88 45 40                        mov byte ptr [rbp + 0x40], al
00341301  8B 8E A0 05 00 00               mov ecx, dword ptr [rsi + 0x5a0]
00341307  88 45 52                        mov byte ptr [rbp + 0x52], al
0034130A  40 84 CF                        test dil, cl
0034130D  0F 85 30 01 00 00               jne 0x140341443
00341313  48 8B BE 20 06 00 00            mov rdi, qword ptr [rsi + 0x620]
0034131A  44 8B 25 47 71 B2 00            mov r12d, dword ptr [rip + 0xb27147]
00341321  48 85 FF                        test rdi, rdi
00341324  75 50                           jne 0x140341376
00341326  BA 00 02 00 00                  mov edx, 0x200
0034132B  8D 4F 48                        lea ecx, [rdi + 0x48]
0034132E  41 B8 52 65 54 72               mov r8d, 0x72546552
00341334  E8 B7 0D 84 00                  call 0x140b820f0
00341339  48 8B C8                        mov rcx, rax
0034133C  48 85 C0                        test rax, rax
0034133F  0F 84 FE 00 00 00               je 0x140341443
00341345  45 33 C0                        xor r8d, r8d
00341348  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0034134C  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
00341354  44 89 60 28                     mov dword ptr [rax + 0x28], r12d
00341358  33 C0                           xor eax, eax
0034135A  F0 48 0F B1 8E 20 06 00 00      lock cmpxchg qword ptr [rsi + 0x620], rcx
00341363  48 8B F8                        mov rdi, rax
00341366  0F 84 80 00 00 00               je 0x1403413ec
0034136C  33 D2                           xor edx, edx
0034136E  E8 FD 14 84 00                  call 0x140b82870
00341373  45 33 C0                        xor r8d, r8d
00341376  49 8B C0                        mov rax, r8
00341379  41 8B D0                        mov edx, r8d
0034137C  83 FA 08                        cmp edx, 8
0034137F  73 35                           jae 0x1403413b6
00341381  8B 4F 1C                        mov ecx, dword ptr [rdi + 0x1c]
00341384  81 F9 00 00 01 00               cmp ecx, 0x10000
0034138A  75 0C                           jne 0x140341398
0034138C  48 39 5F 10                     cmp qword ptr [rdi + 0x10], rbx
00341390  75 06                           jne 0x140341398
00341392  44 39 67 28                     cmp dword ptr [rdi + 0x28], r12d
00341396  74 4C                           je 0x1403413e4
00341398  48 85 C0                        test rax, rax
0034139B  0F 85 C0 00 00 00               jne 0x140341461
003413A1  85 C9                           test ecx, ecx
003413A3  0F 84 B5 00 00 00               je 0x14034145e
003413A9  44 39 67 28                     cmp dword ptr [rdi + 0x28], r12d
003413AD  0F 8D AE 00 00 00               jge 0x140341461
003413B3  48 8B C7                        mov rax, rdi
003413B6  48 8B F8                        mov rdi, rax
003413B9  48 85 C0                        test rax, rax
003413BC  74 26                           je 0x1403413e4
003413BE  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
003413C2  48 C7 40 1C 00 00 01 00         mov qword ptr [rax + 0x1c], 0x10000
003413CA  44 89 40 24                     mov dword ptr [rax + 0x24], r8d
003413CE  4C 89 00                        mov qword ptr [rax], r8
003413D1  4C 89 40 08                     mov qword ptr [rax + 8], r8
003413D5  C7 40 18 00 00 00 00            mov dword ptr [rax + 0x18], 0
003413DC  44 89 60 28                     mov dword ptr [rax + 0x28], r12d
003413E0  44 89 40 2C                     mov dword ptr [rax + 0x2c], r8d
003413E4  48 8B CF                        mov rcx, rdi
003413E7  48 85 FF                        test rdi, rdi
003413EA  74 57                           je 0x140341443
003413EC  41 FF 87 74 8F 00 00            inc dword ptr [r15 + 0x8f74]
003413F3  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
003413F6  4C 89 71 08                     mov qword ptr [rcx + 8], r14
003413FA  85 C0                           test eax, eax
003413FC  0F 84 42 01 00 00               je 0x140341544
00341402  83 F8 04                        cmp eax, 4
00341405  0F 85 39 01 00 00               jne 0x140341544
0034140B  66 44 39 69 18                  cmp word ptr [rcx + 0x18], r13w
00341410  0F 85 36 01 00 00               jne 0x14034154c
00341416  0F B6 45 40                     movzx eax, byte ptr [rbp + 0x40]
0034141A  38 41 1A                        cmp byte ptr [rcx + 0x1a], al
0034141D  0F 85 29 01 00 00               jne 0x14034154c
00341423  4C 2B 31                        sub r14, qword ptr [rcx]
00341426  4C 89 31                        mov qword ptr [rcx], r14
00341429  8B 55 50                        mov edx, dword ptr [rbp + 0x50]
0034142C  89 51 18                        mov dword ptr [rcx + 0x18], edx
0034142F  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
00341432  89 51 2C                        mov dword ptr [rcx + 0x2c], edx
00341435  C7 41 20 01 00 00 00            mov dword ptr [rcx + 0x20], 1
0034143C  C7 41 24 01 00 00 00            mov dword ptr [rcx + 0x24], 1
00341443  B0 01                           mov al, 1
00341445  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
0034144D  48 83 C4 70                     add rsp, 0x70
00341451  41 5F                           pop r15
00341453  41 5E                           pop r14
00341455  41 5D                           pop r13
00341457  41 5C                           pop r12
00341459  5F                              pop rdi
0034145A  5E                              pop rsi
0034145B  5D                              pop rbp
0034145C  C3                              ret
0034145D  CC                              int3
0034145E  48 8B C7                        mov rax, rdi
00341461  48 83 C7 40                     add rdi, 0x40
00341465  FF C2                           inc edx
00341467  E9 10 FF FF FF                  jmp 0x14034137c
0034146C  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
00341470  84 C0                           test al, al
00341472  0F 88 4D 02 00 00               js 0x1403416c5
00341478  44 8B 4B 4C                     mov r9d, dword ptr [rbx + 0x4c]
0034147C  49 8B CE                        mov rcx, r14
0034147F  E8 3C 20 ED FF                  call 0x1402134c0
00341484  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00341488  48 8D 53 30                     lea rdx, [rbx + 0x30]
0034148C  49 3B CE                        cmp rcx, r14
0034148F  0F 84 EC 00 00 00               je 0x140341581
00341495  4D 8B C5                        mov r8, r13
00341498  4D 8B D5                        mov r10, r13
0034149B  48 85 C9                        test rcx, rcx
0034149E  0F 84 88 01 00 00               je 0x14034162c
003414A4  4C 8B C7                        mov r8, rdi
003414A7  85 C0                           test eax, eax
003414A9  75 73                           jne 0x14034151e
003414AB  8B 4B 48                        mov ecx, dword ptr [rbx + 0x48]
003414AE  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
003414B1  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
003414B5  48 03 C8                        add rcx, rax
003414B8  48 85 D2                        test rdx, rdx
003414BB  0F 85 22 01 00 00               jne 0x1403415e3
003414C1  4D 8B CD                        mov r9, r13
003414C4  4D 85 D2                        test r10, r10
003414C7  75 15                           jne 0x1403414de
003414C9  49 3B D1                        cmp rdx, r9
003414CC  0F 83 16 02 00 00               jae 0x1403416e8
003414D2  4C 8B D2                        mov r10, rdx
003414D5  48 85 D2                        test rdx, rdx
003414D8  0F 84 0A 02 00 00               je 0x1403416e8
003414DE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003414E7  41 8B CA                        mov ecx, r10d
003414EA  2B 4B 10                        sub ecx, dword ptr [rbx + 0x10]
003414ED  49 8B D2                        mov rdx, r10
003414F0  48 C1 F9 04                     sar rcx, 4
003414F4  88 88 60 04 00 00               mov byte ptr [rax + 0x460], cl
003414FA  E9 8B 00 00 00                  jmp 0x14034158a
003414FF  8B 05 53 C9 BC 00               mov eax, dword ptr [rip + 0xbcc953]
00341505  85 C0                           test eax, eax
00341507  0F 85 4B FD FF FF               jne 0x140341258
0034150D  48 8B D7                        mov rdx, rdi
00341510  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00341514  E8 37 43 F3 FF                  call 0x140275850
00341519  E9 4A FD FF FF                  jmp 0x140341268
0034151E  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00341522  48 85 C9                        test rcx, rcx
00341525  74 84                           je 0x1403414ab
00341527  3B 41 08                        cmp eax, dword ptr [rcx + 8]
0034152A  0F 83 7B FF FF FF               jae 0x1403414ab
00341530  8B D0                           mov edx, eax
00341532  48 C1 E2 04                     shl rdx, 4
00341536  48 03 D1                        add rdx, rcx
00341539  4C 39 32                        cmp qword ptr [rdx], r14
0034153C  0F 85 69 FF FF FF               jne 0x1403414ab
00341542  EB 3D                           jmp 0x140341581
00341544  4C 89 01                        mov qword ptr [rcx], r8
00341547  E9 DD FE FF FF                  jmp 0x140341429
0034154C  48 C7 01 01 00 00 00            mov qword ptr [rcx], 1
00341553  E9 D1 FE FF FF                  jmp 0x140341429
00341558  0F B6 D0                        movzx edx, al
0034155B  40 0F B6 CE                     movzx ecx, sil
0034155F  E8 98 41 1B 00                  call 0x1404f56fc
00341564  E9 DE FC FF FF                  jmp 0x140341247
00341569  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00341572  8B CA                           mov ecx, edx
00341574  2B 4B 10                        sub ecx, dword ptr [rbx + 0x10]
00341577  48 C1 F9 04                     sar rcx, 4
0034157B  88 88 60 04 00 00               mov byte ptr [rax + 0x460], cl
00341581  48 85 D2                        test rdx, rdx
00341584  0F 84 E3 FC FF FF               je 0x14034126d
0034158A  4C 39 32                        cmp qword ptr [rdx], r14
0034158D  0F 85 B1 00 00 00               jne 0x140341644
00341593  8B 42 08                        mov eax, dword ptr [rdx + 8]
00341596  8D 48 08                        lea ecx, [rax + 8]
00341599  8B F9                           mov edi, ecx
0034159B  33 F8                           xor edi, eax
0034159D  83 E7 07                        and edi, 7
003415A0  33 F9                           xor edi, ecx
003415A2  48 8D 4D B0                     lea rcx, [rbp - 0x50]
003415A6  89 7A 08                        mov dword ptr [rdx + 8], edi
003415A9  C1 EF 03                        shr edi, 3
003415AC  E8 2F 17 00 00                  call 0x140342ce0
003415B1  65 FF 04 25 B0 90 00 00         inc dword ptr gs:[0x90b0]
003415B9  65 FF 04 25 64 90 00 00         inc dword ptr gs:[0x9064]
003415C1  45 85 FF                        test r15d, r15d
003415C4  0F 84 79 FE FF FF               je 0x140341443
003415CA  44 8B 4B 44                     mov r9d, dword ptr [rbx + 0x44]
003415CE  44 8B C7                        mov r8d, edi
003415D1  48 8B D3                        mov rdx, rbx
003415D4  B9 51 00 01 00                  mov ecx, 0x10051
003415D9  E8 0A 80 13 00                  call 0x1404795e8
003415DE  E9 60 FE FF FF                  jmp 0x140341443
003415E3  44 8B 4A 08                     mov r9d, dword ptr [rdx + 8]
003415E7  49 C1 E1 04                     shl r9, 4
003415EB  4C 03 CA                        add r9, rdx
003415EE  48 83 C2 10                     add rdx, 0x10
003415F2  4C 3B C1                        cmp r8, rcx
003415F5  0F 83 C9 FE FF FF               jae 0x1403414c4
003415FB  48 8B 02                        mov rax, qword ptr [rdx]
003415FE  49 3B C6                        cmp rax, r14
00341601  0F 84 62 FF FF FF               je 0x140341569
00341607  48 85 C0                        test rax, rax
0034160A  74 16                           je 0x140341622
0034160C  49 FF C0                        inc r8
0034160F  4C 3B C1                        cmp r8, rcx
00341612  74 27                           je 0x14034163b
00341614  48 83 C2 10                     add rdx, 0x10
00341618  49 3B D1                        cmp rdx, r9
0034161B  75 DE                           jne 0x1403415fb
0034161D  E9 A2 FE FF FF                  jmp 0x1403414c4
00341622  4D 85 D2                        test r10, r10
00341625  75 ED                           jne 0x140341614
00341627  4C 8B D2                        mov r10, rdx
0034162A  EB E8                           jmp 0x140341614
0034162C  45 85 C9                        test r9d, r9d
0034162F  4C 8B D2                        mov r10, rdx
00341632  4D 0F 45 D5                     cmovne r10, r13
00341636  E9 6C FE FF FF                  jmp 0x1403414a7
0034163B  48 83 C2 10                     add rdx, 0x10
0034163F  E9 80 FE FF FF                  jmp 0x1403414c4
00341644  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
00341648  84 C0                           test al, al
0034164A  0F 88 F9 00 00 00               js 0x140341749
00341650  FF 43 40                        inc dword ptr [rbx + 0x40]
00341653  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00341657  66 89 7B 18                     mov word ptr [rbx + 0x18], di
0034165B  8B 42 08                        mov eax, dword ptr [rdx + 8]
0034165E  83 E0 07                        and eax, 7
00341661  4C 89 32                        mov qword ptr [rdx], r14
00341664  83 C8 08                        or eax, 8
00341667  89 42 08                        mov dword ptr [rdx + 8], eax
0034166A  E8 71 16 00 00                  call 0x140342ce0
0034166F  49 8B CE                        mov rcx, r14
00341672  E8 49 1E ED FF                  call 0x1402134c0
00341677  44 8B C0                        mov r8d, eax
0034167A  49 8B D6                        mov rdx, r14
0034167D  48 8B CB                        mov rcx, rbx
00341680  E8 5B 46 ED FF                  call 0x140215ce0
00341685  65 FF 04 25 AC 90 00 00         inc dword ptr gs:[0x90ac]
0034168D  65 FF 04 25 64 90 00 00         inc dword ptr gs:[0x9064]
00341695  45 85 FF                        test r15d, r15d
00341698  74 14                           je 0x1403416ae
0034169A  44 8B 4B 44                     mov r9d, dword ptr [rbx + 0x44]
0034169E  44 8B C7                        mov r8d, edi
003416A1  48 8B D3                        mov rdx, rbx
003416A4  B9 41 00 01 00                  mov ecx, 0x10041
003416A9  E8 3A 7F 13 00                  call 0x1404795e8
003416AE  40 0F B6 C7                     movzx eax, dil
003416B2  E9 8E FD FF FF                  jmp 0x140341445
003416B7  48 8D 4D B0                     lea rcx, [rbp - 0x50]
003416BB  E8 F0 67 F1 FF                  call 0x140257eb0
003416C0  E9 A3 FB FF FF                  jmp 0x140341268
003416C5  4C 39 73 30                     cmp qword ptr [rbx + 0x30], r14
003416C9  74 2E                           je 0x1403416f9
003416CB  48 8D 55 B0                     lea rdx, [rbp - 0x50]
003416CF  48 8B CB                        mov rcx, rbx
003416D2  E8 69 31 09 00                  call 0x1403d4840
003416D7  48 8B D0                        mov rdx, rax
003416DA  48 85 C0                        test rax, rax
003416DD  0F 85 A7 FE FF FF               jne 0x14034158a
003416E3  E9 85 FB FF FF                  jmp 0x14034126d
003416E8  48 8D 55 B0                     lea rdx, [rbp - 0x50]
003416EC  48 8B CB                        mov rcx, rbx
003416EF  E8 A8 31 09 00                  call 0x1403d489c
003416F4  E9 74 FB FF FF                  jmp 0x14034126d
003416F9  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
003416FC  8D 48 08                        lea ecx, [rax + 8]
003416FF  8B F9                           mov edi, ecx
00341701  33 F8                           xor edi, eax
00341703  83 E7 07                        and edi, 7
00341706  33 F9                           xor edi, ecx
00341708  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0034170C  89 7B 38                        mov dword ptr [rbx + 0x38], edi
0034170F  C1 EF 03                        shr edi, 3
00341712  E8 C9 15 00 00                  call 0x140342ce0
00341717  65 FF 04 25 A8 90 00 00         inc dword ptr gs:[0x90a8]
0034171F  65 FF 04 25 64 90 00 00         inc dword ptr gs:[0x9064]
00341727  45 85 FF                        test r15d, r15d
0034172A  0F 84 13 FD FF FF               je 0x140341443
00341730  44 8B 4B 44                     mov r9d, dword ptr [rbx + 0x44]
00341734  44 8B C7                        mov r8d, edi
00341737  48 8B D3                        mov rdx, rbx
0034173A  B9 31 00 01 00                  mov ecx, 0x10031
0034173F  E8 A4 7E 13 00                  call 0x1404795e8
00341744  E9 FA FC FF FF                  jmp 0x140341443
00341749  45 84 E4                        test r12b, r12b
0034174C  75 18                           jne 0x140341766
0034174E  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00341752  E8 89 15 00 00                  call 0x140342ce0
00341757  65 FF 04 25 B8 90 00 00         inc dword ptr gs:[0x90b8]
0034175F  32 C0                           xor al, al
00341761  E9 DF FC FF FF                  jmp 0x140341445
00341766  8B 42 08                        mov eax, dword ptr [rdx + 8]
00341769  48 8D 4B 20                     lea rcx, [rbx + 0x20]
0034176D  4C 89 32                        mov qword ptr [rdx], r14
00341770  83 E0 07                        and eax, 7
00341773  83 C8 08                        or eax, 8
00341776  89 42 08                        mov dword ptr [rdx + 8], eax
00341779  48 8D 45 E8                     lea rax, [rbp - 0x18]
0034177D  FF 43 48                        inc dword ptr [rbx + 0x48]
00341780  48 8D 55 C8                     lea rdx, [rbp - 0x38]
00341784  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00341788  48 8D 45 E8                     lea rax, [rbp - 0x18]
0034178C  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00341790  4C 89 6D D0                     mov qword ptr [rbp - 0x30], r13
00341794  48 C7 45 E0 01 00 06 00         mov qword ptr [rbp - 0x20], 0x60001
0034179C  4C 89 75 D8                     mov qword ptr [rbp - 0x28], r14
003417A0  4C 89 6D F8                     mov qword ptr [rbp - 8], r13
003417A4  E8 67 1D 0F 00                  call 0x140433510
003417A9  48 8D 4D B0                     lea rcx, [rbp - 0x50]
003417AD  E8 2E 15 00 00                  call 0x140342ce0
003417B2  65 FF 04 25 B4 90 00 00         inc dword ptr gs:[0x90b4]
003417BA  45 85 FF                        test r15d, r15d
003417BD  75 1F                           jne 0x1403417de
003417BF  48 8B CB                        mov rcx, rbx
003417C2  E8 89 26 ED FF                  call 0x140213e50
003417C7  41 B8 44 02 01 00               mov r8d, 0x10244
003417CD  48 8D 55 C8                     lea rdx, [rbp - 0x38]
003417D1  48 8B CB                        mov rcx, rbx
003417D4  E8 17 4F ED FF                  call 0x1402166f0
003417D9  E9 91 FE FF FF                  jmp 0x14034166f
003417DE  45 33 C0                        xor r8d, r8d
003417E1  48 8B D3                        mov rdx, rbx
003417E4  B9 44 00 01 00                  mov ecx, 0x10044
003417E9  E8 A2 86 17 00                  call 0x1404b9e90
003417EE  EB CF                           jmp 0x1403417bf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpAcquireSharedStarveExclusive(__int64 a1, unsigned __int8 a2, int a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p1A;
    unsigned __int8 v_stack_p1B;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_m78 = 0;
    v_stack_m70 = v_xmm1;
    v_stack_m40 = 0;
    v_stack_m60 = v_xmm1;
    v_stack_m50 = v_xmm1;
    v_stack_m88 = v_xmm0;
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13129970))) & (0x20000ULL));
    v_r13 = 0;
    v_stack_m80 = a1 + 96;
    v_stack_m88 = 0;
    if ((*(unsigned int *)(v_rip + 13130463)) != 0) goto loc_00341558;
loc_00341247:
    v_stack_m78 = (unsigned __int8)(v_cr8);
    if (((*(unsigned __int8 *)(v_rip + 13129912)) & (33)) != 0) goto loc_003414FF;
loc_00341258:
    if (v_stack_m88 != 0) goto loc_003416B7;
loc_00341268:
loc_0034126D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64))) != 0) goto loc_0034146C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 64))) + 1);
    *(unsigned __int16 *)(a1 + 24) = 1;
    *(unsigned int *)(a1 + 64) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 56))) & (7));
    *(unsigned __int64 *)(a1 + 48) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned int)((result) | (8));
    *(unsigned int *)(a1 + 56) = (unsigned int)(result);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m88, v_stack_m88, a3, a4);
    if ((unsigned int)(v_r15) == 0) goto loc_00341443;
    a3 = 0;
    v_stack_p18 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 68)));
    a2 = (v_stack_m88) << (32);
    result = ((unsigned int)(*(unsigned int *)(a1 + 68))) | (a2);
    v_stack_p1B = 0;
    v_stack_p18 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_p8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    v_stack_p1A = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440))))) != 0) goto loc_00341443;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_00341376;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), a4);
    if (result == 0) goto loc_00341443;
    a3 = 0;
    *(unsigned __int64 *)(result + 16) = a1;
    *(unsigned __int64 *)(result + 28) = 0x10000ULL;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11694407)));
    result = 0;
    if (condition_is_equal) goto loc_003413EC;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    a3 = 0;
loc_00341376:
loc_0034137C:
    if (0 >= 8) goto loc_003413B6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != 0x10000ULL) goto loc_00341398;
    if ((*(unsigned __int64 *)(0 + 16)) != a1) goto loc_00341398;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11694407))))) goto loc_003413E4;
loc_00341398:
    if (0 != 0) goto loc_00341461;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28))) == 0) goto loc_0034145E;
    if ((*(unsigned int *)(0 + 40)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11694407))))) goto loc_00341461;
loc_003413B6:
    if (0 != 0) {
        *(unsigned __int64 *)(0 + 16) = a1;
        *(unsigned __int64 *)(0 + 28) = 0x10000ULL;
        *(unsigned int *)(0 + 36) = 0;
        *(unsigned __int64 *)(0) = 0;
        *(unsigned __int64 *)(0 + 8) = 0;
        *(unsigned int *)(0 + 24) = 0;
        *(unsigned int *)(0 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11694407)));
        *(unsigned int *)(0 + 44) = 0;
    }
    if (0 == 0) goto loc_00341443;
loc_003413EC:
    *(unsigned __int64 *)(0 + 8) = result;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 32))) == 0) goto loc_00341544;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 32)))) != 4) goto loc_00341544;
    if ((*(unsigned __int16 *)(0 + 24)) != ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208)))) goto loc_0034154C;
    if ((*(unsigned __int8 *)(0 + 26)) != ((unsigned __int8)(v_stack_p8))) goto loc_0034154C;
    v_r14 = (result) - (*(unsigned __int64 *)(0));
    *(unsigned __int64 *)(0) = v_r14;
loc_00341429:
    *(unsigned int *)(0 + 24) = (unsigned int)((unsigned int)(v_stack_p18));
    *(unsigned int *)(0 + 44) = (unsigned int)((unsigned int)(v_stack_p20));
    *(unsigned int *)(0 + 32) = 1;
    *(unsigned int *)(0 + 36) = 1;
loc_00341443:
loc_00341445:
    v_rsp = (v_rsp) + (112);
    return 1;
loc_0034145E:
loc_00341461:
    v_rdi = (0) + (64);
    a2 = (unsigned int)(((unsigned int)(v_stack_p20)) + 1);
    goto loc_0034137C;
loc_0034146C:
    if (sign_flag) goto loc_003416C5;
    result = ExpGetThreadResourceHint(v_r14, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_p10 + 76)));
    if ((*(unsigned __int64 *)(v_stack_p10 + 48)) == v_r14) goto loc_00341581;
    if (*(unsigned __int64 *)(v_stack_p10 + 48) == 0) goto loc_0034162C;
loc_003414A7:
    if ((unsigned int)(result) != 0) goto loc_0034151E;
loc_003414AB:
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_p10 + 72))) + ((unsigned int)(*(unsigned int *)(v_stack_p10 + 64)));
    if (*(unsigned __int64 *)(v_stack_p10 + 16) != 0) goto loc_003415E3;
loc_003414C4:
    if (*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208) != 0) goto loc_003414DE;
    if ((*(unsigned __int64 *)(v_stack_p10 + 16)) >= (*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208))) goto loc_003416E8;
    if (*(unsigned __int64 *)(v_stack_p10 + 16) == 0) goto loc_003416E8;
loc_003414DE:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p10 + 16)))) - (*(unsigned int *)(v_stack_p10 + 16)));
    a1 = (a1) >> (4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120) = (unsigned __int8)(a1);
    goto loc_0034158A;
loc_003414FF:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12372307))) != 0) goto loc_00341258;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m88, v_rdi, v_rdi, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    goto loc_00341268;
loc_0034151E:
    if (*(unsigned __int64 *)(v_stack_p10 + 16) == 0) goto loc_003414AB;
    if (((unsigned int)(result)) >= (*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 16) + 8))) goto loc_003414AB;
    a2 = ((unsigned int)((unsigned int)(result))) << (4);
    a2 = (a2) + (*(unsigned __int64 *)(v_stack_p10 + 16));
    if ((*(unsigned __int64 *)(a2)) != v_r14) goto loc_003414AB;
    goto loc_00341581;
loc_00341544:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16)) = v_rdi;
    goto loc_00341429;
loc_0034154C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 16)) = 1;
    goto loc_00341429;
loc_00341558:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(*(unsigned __int64 *)(gs_base + (0 + 392))), (unsigned __int8)(result), v_rdi, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    goto loc_00341247;
loc_00341569:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(result)))) - (*(unsigned int *)(v_stack_p10 + 16)));
    a1 = (a1) >> (4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1120) = (unsigned __int8)(a1);
loc_00341581:
    if ((unsigned __int8)(result) == 0) goto loc_0034126D;
loc_0034158A:
    if ((*(unsigned __int64 *)((unsigned __int8)(result))) != v_r14) goto loc_00341644;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(result) + 8)) + 8))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(result) + 8)))));
    v_rdi = (unsigned int)((v_rdi) & (7));
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(result) + 8)) + 8)));
    *(unsigned int *)((unsigned __int8)(result) + 8) = (unsigned int)(v_rdi);
    v_rdi = (unsigned int)((v_rdi) >> (3));
    result = KeReleaseInStackQueuedSpinLock(v_stack_m88, (unsigned __int8)(result), v_rdi, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    if ((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32))) == 0) goto loc_00341443;
    result = PerfLogExecutiveResourceAcquire((unsigned int)(0x10051ULL), v_stack_p10, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(*(unsigned int *)(v_stack_p10 + 68)));
    goto loc_00341443;
loc_003415E3:
    a4 = ((unsigned int)(*(unsigned int *)(v_stack_p10 + 8))) << (4);
    a4 = (a4) + (v_stack_p10);
    a2 = (v_stack_p10) + (16);
    if (((unsigned int)((unsigned int)(v_rdi))) >= ((unsigned int)(0x10051ULL))) goto loc_003414C4;
loc_003415FB:
    if ((*(unsigned __int64 *)(a2)) == v_r14) goto loc_00341569;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00341622;
    a3 = ((unsigned int)((unsigned int)(v_rdi))) + 1;
    if (a3 == ((unsigned int)(0x10051ULL))) goto loc_0034163B;
loc_00341614:
    a2 = (a2) + (16);
    if (a2 != a4) goto loc_003415FB;
    goto loc_003414C4;
loc_00341622:
    if (*(unsigned __int64 *)(v_stack_p10 + 16) != 0) goto loc_00341614;
    goto loc_00341614;
loc_0034162C:
    if ((unsigned int)(a4) != 0) { a2 = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208); }
    goto loc_003414A7;
loc_0034163B:
    a2 = (a2) + (16);
    goto loc_003414C4;
loc_00341644:
    if (sign_flag) goto loc_00341749;
    *(unsigned __int16 *)(v_stack_p10 + 24) = (unsigned __int16)(v_rdi);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 8))) & (7));
    *(unsigned __int64 *)(a2) = v_r14;
    result = (unsigned int)((result) | (8));
    *(unsigned int *)(a2 + 8) = (unsigned int)(result);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m88, a2, a3, a4);
loc_0034166F:
    result = ExpGetThreadResourceHint(v_r14, a2, a3, a4);
    result = ExpBoostIoAfterAcquire(v_stack_p10, v_r14, (unsigned int)((unsigned int)(result)), a4);
    if ((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32))) != 0) {
        a4 = *(unsigned int *)(v_stack_p10 + 68);
        a3 = (unsigned int)(v_rdi);
        a2 = v_stack_p10;
        a1 = 0x10041ULL;
        result = PerfLogExecutiveResourceAcquire(a1, a2, a3, a4);
    }
    goto loc_00341445;
loc_003416B7:
    result = KxWaitForLockOwnerShip(v_stack_m88, a2, a3, a4);
    goto loc_00341268;
loc_003416C5:
    if ((*(unsigned __int64 *)(v_stack_p10 + 48)) == v_r14) goto loc_003416F9;
    result = ExpFindEmptyEntry(v_stack_p10, v_stack_m88, a3, a4);
    if (result != 0) goto loc_0034158A;
    goto loc_0034126D;
loc_003416E8:
    result = ExpExpandResourceOwnerTable(v_stack_p10, v_stack_m88, a3, a4);
    goto loc_0034126D;
loc_003416F9:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 56)) + 8))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 56)))));
    v_rdi = (unsigned int)((v_rdi) & (7));
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 56)) + 8)));
    *(unsigned int *)(v_stack_p10 + 56) = (unsigned int)(v_rdi);
    v_rdi = (unsigned int)((v_rdi) >> (3));
    result = KeReleaseInStackQueuedSpinLock(v_stack_m88, v_stack_m88, a3, a4);
    if ((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32))) == 0) goto loc_00341443;
    result = PerfLogExecutiveResourceAcquire((unsigned int)(0x10031ULL), v_stack_p10, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(*(unsigned int *)(v_stack_p10 + 68)));
    goto loc_00341443;
loc_00341749:
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11694407))) != 0) goto loc_00341766;
    result = KeReleaseInStackQueuedSpinLock(v_stack_m88, v_stack_p10, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(*(unsigned int *)(v_stack_p10 + 68)));
    result = 0;
    goto loc_00341445;
loc_00341766:
    *(unsigned __int64 *)(v_stack_p10) = v_r14;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10 + 8))) & (7));
    result = (unsigned int)((result) | (8));
    *(unsigned int *)(v_stack_p10 + 8) = (unsigned int)(result);
    v_stack_m48 = v_stack_m50;
    v_stack_m50 = v_stack_m50;
    v_stack_m68 = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208);
    v_stack_m58 = 0x60001ULL;
    v_stack_m60 = v_r14;
    v_stack_m40 = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208);
    result = RtlInsertHeadCircularList(v_stack_p10 + 32, v_stack_m70, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(*(unsigned int *)(v_stack_p10 + 68)));
    result = KeReleaseInStackQueuedSpinLock(v_stack_m88, v_stack_m70, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(*(unsigned int *)(v_stack_p10 + 68)));
    if ((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32))) != 0) goto loc_003417DE;
loc_003417BF:
    result = ExpApplyPrewaitBoost(v_stack_p10, v_stack_m70, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(*(unsigned int *)(v_stack_p10 + 68)));
    result = ExpWaitForResource(v_stack_p10, v_stack_m70, (unsigned int)(0x10244ULL), (unsigned int)(*(unsigned int *)(v_stack_p10 + 68)));
    goto loc_0034166F;
loc_003417DE:
    a3 = 0;
    result = PerfLogExecutiveResourceWait((unsigned int)(0x10044ULL), v_stack_p10, a3, (unsigned int)(*(unsigned int *)(v_stack_p10 + 68)));
    goto loc_003417BF;
}
```

## 5. (Beta) C Style

```c
int64_t ExpAcquireSharedStarveExclusive(void *Arg1, uint8_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint8_t v_stack_p1A;
    uint8_t v_stack_p1B;
    uint32_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_m78 = 0;
    v_stack_m70 = v_xmm1;
    v_stack_m40 = 0;
    v_stack_m60 = v_xmm1;
    v_stack_m50 = v_xmm1;
    v_stack_m88 = v_xmm0;
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xC858F2))) & (0x20000ULL));
    local_r13 = 0;
    v_stack_m80 = Arg1 + 96;
    v_stack_m88 = 0;
    if ((*(uint32_t *)(v_rip + 0xC85ADF)) != 0) goto loc_00341558;
loc_00341247:
    v_stack_m78 = (uint8_t)(v_cr8);
    if (((*(uint8_t *)(v_rip + 0xC858B8)) & (33)) != 0) goto loc_003414FF;
loc_00341258:
    if (v_stack_m88 != 0) goto loc_003416B7;
loc_00341268:
loc_0034126D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40))) != 0) goto loc_0034146C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x40))) + 1);
    *(uint16_t *)(arg1 + 0x18) = 1;
    *(uint32_t *)(arg1 + 0x40) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x38))) & (7));
    *(uint64_t *)(arg1 + 0x30) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint32_t)((result) | (8));
    *(uint32_t *)(arg1 + 0x38) = (uint32_t)(result);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m88, v_stack_m88, Arg3, a4);
    if ((uint32_t)(local_r15) == 0) goto loc_00341443;
    Arg3 = 0;
    v_stack_p18 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x44)));
    Arg2 = (v_stack_m88) << (32);
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x44))) | (Arg2);
    v_stack_p1B = 0;
    v_stack_p18 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_p8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    v_stack_p1A = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0))))) != 0) goto loc_00341443;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_00341376;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), a4);
    if (result == 0) goto loc_00341443;
    Arg3 = 0;
    *(void **)(result + 0x10) = Arg1;
    *(uint64_t *)(result + 0x1C) = 0x10000ULL;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB27147)));
    result = 0;
    if (condition_is_equal) goto loc_003413EC;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, a4);
    Arg3 = 0;
loc_00341376:
loc_0034137C:
    if (0 >= 8) goto loc_003413B6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != 0x10000ULL) goto loc_00341398;
    if ((*(uint64_t *)(0 + 0x10)) != Arg1) goto loc_00341398;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB27147))))) goto loc_003413E4;
loc_00341398:
    if (0 != 0) goto loc_00341461;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C))) == 0) goto loc_0034145E;
    if ((*(uint32_t *)(0 + 0x28)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB27147))))) goto loc_00341461;
loc_003413B6:
    if (0 != 0) {
        *(void **)(0 + 0x10) = Arg1;
        *(uint64_t *)(0 + 0x1C) = 0x10000ULL;
        *(uint32_t *)(0 + 0x24) = 0;
        *(uint64_t *)(0) = 0;
        *(uint64_t *)(0 + 0x8) = 0;
        *(uint32_t *)(0 + 0x18) = 0;
        *(uint32_t *)(0 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB27147)));
        *(uint32_t *)(0 + 0x2C) = 0;
    }
    if (0 == 0) goto loc_00341443;
loc_003413EC:
    *(uint64_t *)(0 + 0x8) = result;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x20))) == 0) goto loc_00341544;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x20)))) != 4) goto loc_00341544;
    if ((*(uint16_t *)(0 + 0x18)) != ((uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0)))) goto loc_0034154C;
    if ((*(uint8_t *)(0 + 0x1A)) != ((uint8_t)(v_stack_p8))) goto loc_0034154C;
    local_r14 = (result) - (*(uint64_t *)(0));
    *(uint64_t *)(0) = local_r14;
loc_00341429:
    *(uint32_t *)(0 + 0x18) = (uint32_t)((uint32_t)(v_stack_p18));
    *(uint32_t *)(0 + 0x2C) = (uint32_t)((uint32_t)(v_stack_p20));
    *(uint32_t *)(0 + 0x20) = 1;
    *(uint32_t *)(0 + 0x24) = 1;
loc_00341443:
loc_00341445:
    local_rsp = (local_rsp) + (112);
    return 1;
loc_0034145E:
loc_00341461:
    local_rdi = (0) + (64);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p20)) + 1);
    goto loc_0034137C;
loc_0034146C:
    if (sign_flag) goto loc_003416C5;
    result = ExpGetThreadResourceHint(local_r14, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x4C)));
    if ((*(uint64_t *)(v_stack_p10 + 0x30)) == local_r14) goto loc_00341581;
    if (*(uint64_t *)(v_stack_p10 + 0x30) == 0) goto loc_0034162C;
loc_003414A7:
    if ((uint32_t)(result) != 0) goto loc_0034151E;
loc_003414AB:
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x48))) + ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x40)));
    if (*(uint64_t *)(v_stack_p10 + 0x10) != 0) goto loc_003415E3;
loc_003414C4:
    if (*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0) != 0) goto loc_003414DE;
    if ((*(uint64_t *)(v_stack_p10 + 0x10)) >= (*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0))) goto loc_003416E8;
    if (*(uint64_t *)(v_stack_p10 + 0x10) == 0) goto loc_003416E8;
loc_003414DE:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p10 + 0x10)))) - (*(uint32_t *)(v_stack_p10 + 0x10)));
    Arg1 = (Arg1) >> (4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460) = (uint8_t)(Arg1);
    goto loc_0034158A;
loc_003414FF:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBCC953))) != 0) goto loc_00341258;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m88, local_rdi, local_rdi, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    goto loc_00341268;
loc_0034151E:
    if (*(uint64_t *)(v_stack_p10 + 0x10) == 0) goto loc_003414AB;
    if (((uint32_t)(result)) >= (*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x10) + 0x8))) goto loc_003414AB;
    Arg2 = ((uint32_t)((uint32_t)(result))) << (4);
    Arg2 = (Arg2) + (*(uint64_t *)(v_stack_p10 + 0x10));
    if ((*(uint64_t *)(Arg2)) != local_r14) goto loc_003414AB;
    goto loc_00341581;
loc_00341544:
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10)) = local_rdi;
    goto loc_00341429;
loc_0034154C:
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x10)) = 1;
    goto loc_00341429;
loc_00341558:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(*(uint64_t *)(gs_base + (0 + 0x188))), (uint8_t)(result), local_rdi, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    goto loc_00341247;
loc_00341569:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(result)))) - (*(uint32_t *)(v_stack_p10 + 0x10)));
    Arg1 = (Arg1) >> (4);
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x460) = (uint8_t)(Arg1);
loc_00341581:
    if ((uint8_t)(result) == 0) goto loc_0034126D;
loc_0034158A:
    if ((*(uint64_t *)((uint8_t)(result))) != local_r14) goto loc_00341644;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(result) + 0x8)) + 8))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(result) + 0x8)))));
    local_rdi = (uint32_t)((local_rdi) & (7));
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(result) + 0x8)) + 8)));
    *(uint32_t *)((uint8_t)(result) + 0x8) = (uint32_t)(local_rdi);
    local_rdi = (uint32_t)((local_rdi) >> (3));
    result = KeReleaseInStackQueuedSpinLock(v_stack_m88, (uint8_t)(result), local_rdi, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    if ((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20))) == 0) goto loc_00341443;
    result = PerfLogExecutiveResourceAcquire((uint32_t)(0x10051ULL), v_stack_p10, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x44)));
    goto loc_00341443;
loc_003415E3:
    a4 = ((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x8))) << (4);
    a4 = (a4) + (v_stack_p10);
    Arg2 = (v_stack_p10) + (16);
    if (((uint32_t)((uint32_t)(local_rdi))) >= ((uint32_t)(0x10051ULL))) goto loc_003414C4;
loc_003415FB:
    if ((*(uint64_t *)(Arg2)) == local_r14) goto loc_00341569;
    if (*(uint64_t *)(Arg2) == 0) goto loc_00341622;
    Arg3 = ((uint32_t)((uint32_t)(local_rdi))) + 1;
    if (Arg3 == ((uint32_t)(0x10051ULL))) goto loc_0034163B;
loc_00341614:
    Arg2 = (Arg2) + (16);
    if (Arg2 != a4) goto loc_003415FB;
    goto loc_003414C4;
loc_00341622:
    if (*(uint64_t *)(v_stack_p10 + 0x10) != 0) goto loc_00341614;
    goto loc_00341614;
loc_0034162C:
    if ((uint32_t)(a4) != 0) { Arg2 = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0); }
    goto loc_003414A7;
loc_0034163B:
    Arg2 = (Arg2) + (16);
    goto loc_003414C4;
loc_00341644:
    if (sign_flag) goto loc_00341749;
    *(uint16_t *)(v_stack_p10 + 0x18) = (uint16_t)(local_rdi);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x8))) & (7));
    *(uint64_t *)(Arg2) = local_r14;
    result = (uint32_t)((result) | (8));
    *(uint32_t *)(Arg2 + 0x8) = (uint32_t)(result);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m88, Arg2, Arg3, a4);
loc_0034166F:
    result = ExpGetThreadResourceHint(local_r14, Arg2, Arg3, a4);
    result = ExpBoostIoAfterAcquire(v_stack_p10, local_r14, (uint32_t)((uint32_t)(result)), a4);
    if ((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20))) != 0) {
        a4 = *(uint32_t *)(v_stack_p10 + 0x44);
        Arg3 = (uint32_t)(local_rdi);
        Arg2 = v_stack_p10;
        Arg1 = 0x10041ULL;
        result = PerfLogExecutiveResourceAcquire(Arg1, Arg2, Arg3, a4);
    }
    goto loc_00341445;
loc_003416B7:
    result = KxWaitForLockOwnerShip(v_stack_m88, Arg2, Arg3, a4);
    goto loc_00341268;
loc_003416C5:
    if ((*(uint64_t *)(v_stack_p10 + 0x30)) == local_r14) goto loc_003416F9;
    result = ExpFindEmptyEntry(v_stack_p10, v_stack_m88, Arg3, a4);
    if (result != 0) goto loc_0034158A;
    goto loc_0034126D;
loc_003416E8:
    result = ExpExpandResourceOwnerTable(v_stack_p10, v_stack_m88, Arg3, a4);
    goto loc_0034126D;
loc_003416F9:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x38)) + 8))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x38)))));
    local_rdi = (uint32_t)((local_rdi) & (7));
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x38)) + 8)));
    *(uint32_t *)(v_stack_p10 + 0x38) = (uint32_t)(local_rdi);
    local_rdi = (uint32_t)((local_rdi) >> (3));
    result = KeReleaseInStackQueuedSpinLock(v_stack_m88, v_stack_m88, Arg3, a4);
    if ((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20))) == 0) goto loc_00341443;
    result = PerfLogExecutiveResourceAcquire((uint32_t)(0x10031ULL), v_stack_p10, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x44)));
    goto loc_00341443;
loc_00341749:
    if ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB27147))) != 0) goto loc_00341766;
    result = KeReleaseInStackQueuedSpinLock(v_stack_m88, v_stack_p10, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x44)));
    result = 0;
    goto loc_00341445;
loc_00341766:
    *(uint64_t *)(v_stack_p10) = local_r14;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x8))) & (7));
    result = (uint32_t)((result) | (8));
    *(uint32_t *)(v_stack_p10 + 0x8) = (uint32_t)(result);
    v_stack_m48 = v_stack_m50;
    v_stack_m50 = v_stack_m50;
    v_stack_m68 = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0);
    v_stack_m58 = 0x60001ULL;
    v_stack_m60 = local_r14;
    v_stack_m40 = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0);
    result = RtlInsertHeadCircularList(v_stack_p10 + 32, v_stack_m70, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x44)));
    result = KeReleaseInStackQueuedSpinLock(v_stack_m88, v_stack_m70, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x44)));
    if ((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20))) != 0) goto loc_003417DE;
loc_003417BF:
    result = ExpApplyPrewaitBoost(v_stack_p10, v_stack_m70, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x44)));
    result = ExpWaitForResource(v_stack_p10, v_stack_m70, (uint32_t)(0x10244ULL), (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x44)));
    goto loc_0034166F;
loc_003417DE:
    Arg3 = 0;
    result = PerfLogExecutiveResourceWait((uint32_t)(0x10044ULL), v_stack_p10, Arg3, (uint32_t)(*(uint32_t *)(v_stack_p10 + 0x44)));
    goto loc_003417BF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `16` | `W` |
| `Arg1` | `+ 0x1A` | `8` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x38` | `32` | `W` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R/W` |
| `Arg1` | `+ 0x40` | `32` | `W` |
| `Arg1` | `+ 0x44` | `32` | `R` |
| `Arg1` | `+ 0x48` | `32` | `R` |
| `Arg1` | `+ 0x48` | `32` | `R/W` |
| `Arg1` | `+ 0x4C` | `32` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003411C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
