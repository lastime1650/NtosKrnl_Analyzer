# MmMarkPhysicalMemoryAsBad

- RVA: `0x0067AA50`–`0x0067AFF7` (길이 `1,447` bytes)
- VA: `0x000000014067AA50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CCBA4`
- 디코드: `388`개 명령, `1,447/1,447` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **44**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0067AB2C` → [MiIsPageInHugePfn](../2A/MiIsPageInHugePfn_function_002AB770.md) (function, `0x002AB770`)
- `0x0067AB3B` → [MiMarkHugePfnBad](MiMarkHugePfnBad_function_00676744.md) (function, `0x00676744`)
- `0x0067AB5F` → [MiSafeLockPage](../32/MiSafeLockPage_function_00321620.md) (function, `0x00321620`)
- `0x0067AB84` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0067AB8F` → [MiMarkFileOnlyPfnBad](../68/MiMarkFileOnlyPfnBad_function_006815C4.md) (function, `0x006815C4`)
- `0x0067ABA0` → [MiReferencePagePartition](MiReferencePagePartition_function_00679304.md) (function, `0x00679304`)
- `0x0067ABAB` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0067ABD9` → [MiAcquireNonPagedResources](../28/MiAcquireNonPagedResources_function_00286C60.md) (function, `0x00286C60`)
- `0x0067ABF4` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0067ABFF` → [MiSafeLockPage](../32/MiSafeLockPage_function_00321620.md) (function, `0x00321620`)
- `0x0067AC1A` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)
- `0x0067AC22` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x0067AC38` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0067AC68` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0067AC77` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)
- `0x0067AC7F` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x0067AC91` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0067ACD4` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0067ACE3` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)
- `0x0067ACEB` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x0067ACFD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0067AD21` → [MiIsPageOnBadList](../2B/MiIsPageOnBadList_function_002B1018.md) (function, `0x002B1018`)
- `0x0067AD31` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0067AD50` → [MiSetPfnRemovalRequested](MiSetPfnRemovalRequested_function_0067A4D0.md) (function, `0x0067A4D0`)
- `0x0067AD5E` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x0067AD6B` → [MiIsPfnFromChargedSlabAllocation](../2A/MiIsPfnFromChargedSlabAllocation_function_002A2968.md) (function, `0x002A2968`)
- `0x0067ADA8` → [MiIsPfnCommitNotCharged](../31/MiIsPfnCommitNotCharged_function_00317370.md) (function, `0x00317370`)
- `0x0067ADC1` → [MiStoreDiscardPoisonedPage](../69/MiStoreDiscardPoisonedPage_function_00692858.md) (function, `0x00692858`)
- `0x0067ADD9` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0067ADEC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0067AE04` → [KeGenericCallDpcEx](../2C/KeGenericCallDpcEx_function_002C99F4.md) (function, `0x002C99F4`)
- `0x0067AE58` → [MiFindContiguousPagesEx](../28/MiFindContiguousPagesEx_function_0028BDE0.md) (function, `0x0028BDE0`)
- `0x0067AE62` → [MiSafeLockPage](../32/MiSafeLockPage_function_00321620.md) (function, `0x00321620`)
- `0x0067AEA1` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x0067AEAE` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x0067AEB9` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0067AEC8` → [MiFreeContiguousPages](../3F/MiFreeContiguousPages_function_003F7178.md) (function, `0x003F7178`)
- `0x0067AECF` → [MiIsPageOnBadList](../2B/MiIsPageOnBadList_function_002B1018.md) (function, `0x002B1018`)
- `0x0067AEFF` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0067AF11` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)
- `0x0067AF19` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x0067AF5F` → [PsDereferencePartition](../34/PsDereferencePartition_function_00342E70.md) (function, `0x00342E70`)
- `0x0067AFA2` → [ZwUpdateWnfStateData](../6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x0067AFD6` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [WheaAttemptRowOffline](../65/WheaAttemptRowOffline_function_0065F050.md) at `0x0065F0EA`
- [MiScrubLargePage](../69/MiScrubLargePage_function_006942E8.md) at `0x00694870`
- [WheapAttemptPhysicalPageOffline](../../page/7D/WheapAttemptPhysicalPageOffline_function_007D79AC.md) at `0x007D7A4A`

### Static image references
- `0x0067AA6C` → RVA `0x00E0A740` (`.data`; read)
- `0x0067AAB5` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0067AC46` → RVA `0x00E30088` (`.data`; read)
- `0x0067ADF9` → RVA `0x0044C3C0` (`MiDemoteSlabEntriesDpc`; read)
- `0x0067AEED` → RVA `0x00E30250` (`.data`; write)
- `0x0067AF6F` → RVA `0x00E2FFAC` (`.data`; read)
- `0x0067AF89` → RVA `0x000209B0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0067AC38` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0067AC91` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0067ACFD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0067AA50  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0067AA55  55                              push rbp
0067AA56  56                              push rsi
0067AA57  57                              push rdi
0067AA58  41 54                           push r12
0067AA5A  41 55                           push r13
0067AA5C  41 56                           push r14
0067AA5E  41 57                           push r15
0067AA60  48 8D 6C 24 D0                  lea rbp, [rsp - 0x30]
0067AA65  48 81 EC 30 01 00 00            sub rsp, 0x130
0067AA6C  48 8B 05 CD FC 78 00            mov rax, qword ptr [rip + 0x78fccd]
0067AA73  48 33 C4                        xor rax, rsp
0067AA76  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
0067AA7A  44 8B 21                        mov r12d, dword ptr [rcx]
0067AA7D  45 33 ED                        xor r13d, r13d
0067AA80  4C 8B FA                        mov r15, rdx
0067AA83  48 89 55 A8                     mov qword ptr [rbp - 0x58], rdx
0067AA87  41 8B C4                        mov eax, r12d
0067AA8A  4C 89 6D 98                     mov qword ptr [rbp - 0x68], r13
0067AA8E  BA FF 0F 00 00                  mov edx, 0xfff
0067AA93  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
0067AA98  41 8D 5D 01                     lea ebx, [r13 + 1]
0067AA9C  23 C2                           and eax, edx
0067AA9E  3B C3                           cmp eax, ebx
0067AAA0  0F 87 24 05 00 00               ja 0x14067afca
0067AAA6  41 85 17                        test dword ptr [r15], edx
0067AAA9  74 0A                           je 0x14067aab5
0067AAAB  B8 F0 00 00 C0                  mov eax, 0xc00000f0
0067AAB0  E9 1A 05 00 00                  jmp 0x14067afcf
0067AAB5  48 F7 05 C8 BF 94 00 00 00 00 10  test qword ptr [rip + 0x94bfc8], 0x10000000
0067AAC0  75 0A                           jne 0x14067aacc
0067AAC2  B8 02 00 00 C0                  mov eax, 0xc0000002
0067AAC7  E9 03 05 00 00                  jmp 0x14067afcf
0067AACC  49 8B 37                        mov rsi, qword ptr [r15]
0067AACF  48 8B 39                        mov rdi, qword ptr [rcx]
0067AAD2  48 C1 EE 0C                     shr rsi, 0xc
0067AAD6  48 C1 EF 0C                     shr rdi, 0xc
0067AADA  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
0067AADE  4C 8D 3C 37                     lea r15, [rdi + rsi]
0067AAE2  4C 89 7D 88                     mov qword ptr [rbp - 0x78], r15
0067AAE6  49 3B FF                        cmp rdi, r15
0067AAE9  0F 83 DB 04 00 00               jae 0x14067afca
0067AAEF  41 F7 D4                        not r12d
0067AAF2  44 89 6D 94                     mov dword ptr [rbp - 0x6c], r13d
0067AAF6  44 23 E3                        and r12d, ebx
0067AAF9  44 89 6D 90                     mov dword ptr [rbp - 0x70], r13d
0067AAFD  41 C1 E4 1C                     shl r12d, 0x1c
0067AB01  48 8D 1C 7F                     lea rbx, [rdi + rdi*2]
0067AB05  41 81 C4 00 00 10 2C            add r12d, 0x2c100000
0067AB0C  48 C1 E3 04                     shl rbx, 4
0067AB10  45 8B F5                        mov r14d, r13d
0067AB13  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0067AB1D  48 03 D8                        add rbx, rax
0067AB20  49 3B FF                        cmp rdi, r15
0067AB23  0F 83 3D 04 00 00               jae 0x14067af66
0067AB29  48 8B CF                        mov rcx, rdi
0067AB2C  E8 3F 0C C3 FF                  call 0x1402ab770
0067AB31  48 8B CF                        mov rcx, rdi
0067AB34  85 C0                           test eax, eax
0067AB36  74 27                           je 0x14067ab5f
0067AB38  41 8B D4                        mov edx, r12d
0067AB3B  E8 04 BC FF FF                  call 0x140676744
0067AB40  44 8B F0                        mov r14d, eax
0067AB43  3D 34 04 00 C0                  cmp eax, 0xc0000434
0067AB48  B8 01 00 00 00                  mov eax, 1
0067AB4D  0F 85 E7 03 00 00               jne 0x14067af3a
0067AB53  48 2B F8                        sub rdi, rax
0067AB56  48 83 EB 30                     sub rbx, 0x30
0067AB5A  E9 DB 03 00 00                  jmp 0x14067af3a
0067AB5F  E8 BC 6A CA FF                  call 0x140321620
0067AB64  40 8A F0                        mov sil, al
0067AB67  3C 11                           cmp al, 0x11
0067AB69  75 0B                           jne 0x14067ab76
0067AB6B  41 BE F0 00 00 C0               mov r14d, 0xc00000f0
0067AB71  E9 BF 03 00 00                  jmp 0x14067af35
0067AB76  48 0F BA 63 28 35               bt qword ptr [rbx + 0x28], 0x35
0067AB7C  48 8B CB                        mov rcx, rbx
0067AB7F  73 15                           jae 0x14067ab96
0067AB81  40 8A D6                        mov dl, sil
0067AB84  E8 57 F8 C9 FF                  call 0x14031a3e0
0067AB89  41 8B D4                        mov edx, r12d
0067AB8C  48 8B CB                        mov rcx, rbx
0067AB8F  E8 30 6A 00 00                  call 0x1406815c4
0067AB94  EB AA                           jmp 0x14067ab40
0067AB96  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
0067AB9B  BA 01 00 00 00                  mov edx, 1
0067ABA0  E8 5F E7 FF FF                  call 0x140679304
0067ABA5  40 8A D6                        mov dl, sil
0067ABA8  48 8B CB                        mov rcx, rbx
0067ABAB  E8 30 F8 C9 FF                  call 0x14031a3e0
0067ABB0  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
0067ABB5  4D 85 FF                        test r15, r15
0067ABB8  75 0B                           jne 0x14067abc5
0067ABBA  41 BE 0A 01 00 C0               mov r14d, 0xc000010a
0067ABC0  E9 6C 03 00 00                  jmp 0x14067af31
0067ABC5  4D 8B AF B8 00 00 00            mov r13, qword ptr [r15 + 0xb8]
0067ABCC  45 33 C9                        xor r9d, r9d
0067ABCF  45 33 C0                        xor r8d, r8d
0067ABD2  49 8B CF                        mov rcx, r15
0067ABD5  41 8D 51 02                     lea edx, [r9 + 2]
0067ABD9  E8 82 C0 C0 FF                  call 0x140286c60
0067ABDE  85 C0                           test eax, eax
0067ABE0  0F 88 6C 03 00 00               js 0x14067af52
0067ABE6  BA 20 00 00 00                  mov edx, 0x20
0067ABEB  41 B8 4D 69 42 6C               mov r8d, 0x6c42694d
0067ABF1  8D 4A 20                        lea ecx, [rdx + 0x20]
0067ABF4  E8 47 09 CE FF                  call 0x14035b540
0067ABF9  48 8B CF                        mov rcx, rdi
0067ABFC  48 8B F0                        mov rsi, rax
0067ABFF  E8 1C 6A CA FF                  call 0x140321620
0067AC04  88 44 24 70                     mov byte ptr [rsp + 0x70], al
0067AC08  3C 11                           cmp al, 0x11
0067AC0A  75 36                           jne 0x14067ac42
0067AC0C  41 BE F0 00 00 C0               mov r14d, 0xc00000f0
0067AC12  49 8B CF                        mov rcx, r15
0067AC15  BA 02 00 00 00                  mov edx, 2
0067AC1A  E8 7D 7D CA FF                  call 0x14032299c
0067AC1F  49 8B CD                        mov rcx, r13
0067AC22  E8 49 82 CC FF                  call 0x140342e70
0067AC27  45 33 ED                        xor r13d, r13d
0067AC2A  48 85 F6                        test rsi, rsi
0067AC2D  0F 84 FE 02 00 00               je 0x14067af31
0067AC33  33 D2                           xor edx, edx
0067AC35  48 8B CE                        mov rcx, rsi
0067AC38  E8 33 7C 50 00                  call 0x140b82870
0067AC3D  E9 EF 02 00 00                  jmp 0x14067af31
0067AC42  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0067AC46  48 8B 0D 3B 54 7B 00            mov rcx, qword ptr [rip + 0x7b543b]
0067AC4D  48 C1 E8 2B                     shr rax, 0x2b
0067AC51  25 FF 03 00 00                  and eax, 0x3ff
0067AC56  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
0067AC5A  48 3B 54 24 78                  cmp rdx, qword ptr [rsp + 0x78]
0067AC5F  74 41                           je 0x14067aca2
0067AC61  8A 54 24 70                     mov dl, byte ptr [rsp + 0x70]
0067AC65  48 8B CB                        mov rcx, rbx
0067AC68  E8 73 F7 C9 FF                  call 0x14031a3e0
0067AC6D  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0067AC72  BA 02 00 00 00                  mov edx, 2
0067AC77  E8 20 7D CA FF                  call 0x14032299c
0067AC7C  49 8B CD                        mov rcx, r13
0067AC7F  E8 EC 81 CC FF                  call 0x140342e70
0067AC84  45 33 ED                        xor r13d, r13d
0067AC87  48 85 F6                        test rsi, rsi
0067AC8A  74 0A                           je 0x14067ac96
0067AC8C  33 D2                           xor edx, edx
0067AC8E  48 8B CE                        mov rcx, rsi
0067AC91  E8 DA 7B 50 00                  call 0x140b82870
0067AC96  48 FF CF                        dec rdi
0067AC99  48 83 EB 30                     sub rbx, 0x30
0067AC9D  E9 8F 02 00 00                  jmp 0x14067af31
0067ACA2  41 0F BA E4 1C                  bt r12d, 0x1c
0067ACA7  73 1A                           jae 0x14067acc3
0067ACA9  80 7B 23 00                     cmp byte ptr [rbx + 0x23], 0
0067ACAD  7C 14                           jl 0x14067acc3
0067ACAF  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0067ACB2  89 45 80                        mov dword ptr [rbp - 0x80], eax
0067ACB5  C1 E8 18                        shr eax, 0x18
0067ACB8  0C 80                           or al, 0x80
0067ACBA  88 45 83                        mov byte ptr [rbp - 0x7d], al
0067ACBD  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
0067ACC0  89 43 20                        mov dword ptr [rbx + 0x20], eax
0067ACC3  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0067ACC6  C1 E8 18                        shr eax, 0x18
0067ACC9  A8 40                           test al, 0x40
0067ACCB  74 40                           je 0x14067ad0d
0067ACCD  8A 54 24 70                     mov dl, byte ptr [rsp + 0x70]
0067ACD1  48 8B CB                        mov rcx, rbx
0067ACD4  E8 07 F7 C9 FF                  call 0x14031a3e0
0067ACD9  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0067ACDE  BA 02 00 00 00                  mov edx, 2
0067ACE3  E8 B4 7C CA FF                  call 0x14032299c
0067ACE8  49 8B CD                        mov rcx, r13
0067ACEB  E8 80 81 CC FF                  call 0x140342e70
0067ACF0  45 33 ED                        xor r13d, r13d
0067ACF3  48 85 F6                        test rsi, rsi
0067ACF6  74 0A                           je 0x14067ad02
0067ACF8  33 D2                           xor edx, edx
0067ACFA  48 8B CE                        mov rcx, rsi
0067ACFD  E8 6E 7B 50 00                  call 0x140b82870
0067AD02  41 BE 03 01 00 00               mov r14d, 0x103
0067AD08  E9 24 02 00 00                  jmp 0x14067af31
0067AD0D  8A 43 22                        mov al, byte ptr [rbx + 0x22]
0067AD10  24 07                           and al, 7
0067AD12  3C 05                           cmp al, 5
0067AD14  75 2A                           jne 0x14067ad40
0067AD16  48 0F BA 63 28 35               bt qword ptr [rbx + 0x28], 0x35
0067AD1C  72 0C                           jb 0x14067ad2a
0067AD1E  48 8B CB                        mov rcx, rbx
0067AD21  E8 F2 62 C3 FF                  call 0x1402b1018
0067AD26  85 C0                           test eax, eax
0067AD28  74 16                           je 0x14067ad40
0067AD2A  8A 54 24 70                     mov dl, byte ptr [rsp + 0x70]
0067AD2E  48 8B CB                        mov rcx, rbx
0067AD31  E8 AA F6 C9 FF                  call 0x14031a3e0
0067AD36  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0067AD3B  E9 D5 FE FF FF                  jmp 0x14067ac15
0067AD40  45 33 C0                        xor r8d, r8d
0067AD43  4C 8B CE                        mov r9, rsi
0067AD46  48 8B CB                        mov rcx, rbx
0067AD49  45 8D 78 01                     lea r15d, [r8 + 1]
0067AD4D  41 8B D7                        mov edx, r15d
0067AD50  E8 7B F7 FF FF                  call 0x14067a4d0
0067AD55  45 33 F6                        xor r14d, r14d
0067AD58  48 8B CB                        mov rcx, rbx
0067AD5B  41 8B F6                        mov esi, r14d
0067AD5E  E8 6D 35 C1 FF                  call 0x14028e2d0
0067AD63  83 F8 09                        cmp eax, 9
0067AD66  74 0E                           je 0x14067ad76
0067AD68  48 8B CB                        mov rcx, rbx
0067AD6B  E8 F8 7B C2 FF                  call 0x1402a2968
0067AD70  85 C0                           test eax, eax
0067AD72  41 0F 44 F7                     cmove esi, r15d
0067AD76  44 38 73 23                     cmp byte ptr [rbx + 0x23], r14b
0067AD7A  7D 4C                           jge 0x14067adc8
0067AD7C  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0067AD81  8B 80 B4 04 00 00               mov eax, dword ptr [rax + 0x4b4]
0067AD87  83 F8 FF                        cmp eax, -1
0067AD8A  74 3C                           je 0x14067adc8
0067AD8C  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
0067AD91  41 8B 87 AC 06 00 00            mov eax, dword ptr [r15 + 0x6ac]
0067AD98  A8 02                           test al, 2
0067AD9A  74 31                           je 0x14067adcd
0067AD9C  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0067ADA0  48 85 C0                        test rax, rax
0067ADA3  78 23                           js 0x14067adc8
0067ADA5  48 8B CB                        mov rcx, rbx
0067ADA8  E8 C3 C5 C9 FF                  call 0x140317370
0067ADAD  85 C0                           test eax, eax
0067ADAF  74 17                           je 0x14067adc8
0067ADB1  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
0067ADB6  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
0067ADBB  49 8B CF                        mov rcx, r15
0067ADBE  48 8B D3                        mov rdx, rbx
0067ADC1  E8 92 7A 01 00                  call 0x140692858
0067ADC6  EB 05                           jmp 0x14067adcd
0067ADC8  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
0067ADCD  8A 54 24 70                     mov dl, byte ptr [rsp + 0x70]
0067ADD1  80 FA 11                        cmp dl, 0x11
0067ADD4  74 08                           je 0x14067adde
0067ADD6  48 8B CB                        mov rcx, rbx
0067ADD9  E8 02 F6 C9 FF                  call 0x14031a3e0
0067ADDE  85 F6                           test esi, esi
0067ADE0  74 27                           je 0x14067ae09
0067ADE2  33 D2                           xor edx, edx
0067ADE4  48 8D 4D B8                     lea rcx, [rbp - 0x48]
0067ADE8  44 8D 42 58                     lea r8d, [rdx + 0x58]
0067ADEC  E8 4F BE 04 00                  call 0x1406c6c40
0067ADF1  48 8D 55 B0                     lea rdx, [rbp - 0x50]
0067ADF5  4C 89 7D B0                     mov qword ptr [rbp - 0x50], r15
0067ADF9  48 8D 0D C0 15 DD FF            lea rcx, [rip - 0x22ea40]
0067AE00  48 89 7D 10                     mov qword ptr [rbp + 0x10], rdi
0067AE04  E8 EB EB C4 FF                  call 0x1402c99f4
0067AE09  48 8D 4D 98                     lea rcx, [rbp - 0x68]
0067AE0D  41 8B C4                        mov eax, r12d
0067AE10  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0067AE15  0F BA E8 1C                     bts eax, 0x1c
0067AE19  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
0067AE1E  45 33 C9                        xor r9d, r9d
0067AE21  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
0067AE26  4C 8B C7                        mov r8, rdi
0067AE29  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
0067AE2E  48 8B D7                        mov rdx, rdi
0067AE31  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0067AE35  49 8B CF                        mov rcx, r15
0067AE38  C6 44 24 40 FF                  mov byte ptr [rsp + 0x40], 0xff
0067AE3D  B8 01 00 00 00                  mov eax, 1
0067AE42  C7 44 24 38 00 00 00 80         mov dword ptr [rsp + 0x38], 0x80000000
0067AE4A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0067AE4E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0067AE53  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0067AE58  E8 83 0F C1 FF                  call 0x14028bde0
0067AE5D  48 8B CF                        mov rcx, rdi
0067AE60  8B F0                           mov esi, eax
0067AE62  E8 B9 67 CA FF                  call 0x140321620
0067AE67  88 44 24 70                     mov byte ptr [rsp + 0x70], al
0067AE6B  3C 11                           cmp al, 0x11
0067AE6D  75 0B                           jne 0x14067ae7a
0067AE6F  41 BE F0 00 00 C0               mov r14d, 0xc00000f0
0067AE75  E9 8F 00 00 00                  jmp 0x14067af09
0067AE7A  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0067AE7E  33 D2                           xor edx, edx
0067AE80  48 8B CB                        mov rcx, rbx
0067AE83  85 F6                           test esi, esi
0067AE85  78 48                           js 0x14067aecf
0067AE87  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0067AE8A  C1 E8 18                        shr eax, 0x18
0067AE8D  A8 40                           test al, 0x40
0067AE8F  74 24                           je 0x14067aeb5
0067AE91  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0067AE94  89 45 80                        mov dword ptr [rbp - 0x80], eax
0067AE97  66 89 55 80                     mov word ptr [rbp - 0x80], dx
0067AE9B  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
0067AE9E  89 43 20                        mov dword ptr [rbx + 0x20], eax
0067AEA1  E8 1A 91 CE FF                  call 0x140363fc0
0067AEA6  BA 20 00 00 00                  mov edx, 0x20
0067AEAB  48 8B CB                        mov rcx, rbx
0067AEAE  E8 4D F1 C3 FF                  call 0x1402ba000
0067AEB3  EB 43                           jmp 0x14067aef8
0067AEB5  8A 54 24 70                     mov dl, byte ptr [rsp + 0x70]
0067AEB9  E8 22 F5 C9 FF                  call 0x14031a3e0
0067AEBE  45 33 C0                        xor r8d, r8d
0067AEC1  48 8B CF                        mov rcx, rdi
0067AEC4  41 8D 50 01                     lea edx, [r8 + 1]
0067AEC8  E8 AB C2 D7 FF                  call 0x1403f7178
0067AECD  EB 47                           jmp 0x14067af16
0067AECF  E8 44 61 C3 FF                  call 0x1402b1018
0067AED4  85 C0                           test eax, eax
0067AED6  75 1E                           jne 0x14067aef6
0067AED8  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0067AEDB  C1 E8 18                        shr eax, 0x18
0067AEDE  A8 40                           test al, 0x40
0067AEE0  74 16                           je 0x14067aef8
0067AEE2  B8 01 00 00 00                  mov eax, 1
0067AEE7  41 BE 03 01 00 00               mov r14d, 0x103
0067AEED  88 05 5D 53 7B 00               mov byte ptr [rip + 0x7b535d], al
0067AEF3  89 45 90                        mov dword ptr [rbp - 0x70], eax
0067AEF6  8B F2                           mov esi, edx
0067AEF8  8A 54 24 70                     mov dl, byte ptr [rsp + 0x70]
0067AEFC  48 8B CB                        mov rcx, rbx
0067AEFF  E8 DC F4 C9 FF                  call 0x14031a3e0
0067AF04  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
0067AF09  BA 01 00 00 00                  mov edx, 1
0067AF0E  49 8B CF                        mov rcx, r15
0067AF11  E8 86 7A CA FF                  call 0x14032299c
0067AF16  49 8B CD                        mov rcx, r13
0067AF19  E8 52 7F CC FF                  call 0x140342e70
0067AF1E  81 FE 2D 01 00 C0               cmp esi, 0xc000012d
0067AF24  74 20                           je 0x14067af46
0067AF26  81 FE 9A 00 00 C0               cmp esi, 0xc000009a
0067AF2C  74 18                           je 0x14067af46
0067AF2E  45 33 ED                        xor r13d, r13d
0067AF31  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
0067AF35  B8 01 00 00 00                  mov eax, 1
0067AF3A  48 03 F8                        add rdi, rax
0067AF3D  48 83 C3 30                     add rbx, 0x30
0067AF41  E9 DA FB FF FF                  jmp 0x14067ab20
0067AF46  44 8B F6                        mov r14d, esi
0067AF49  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
0067AF4D  45 33 ED                        xor r13d, r13d
0067AF50  EB 17                           jmp 0x14067af69
0067AF52  B8 9A 00 00 C0                  mov eax, 0xc000009a
0067AF57  49 8B CD                        mov rcx, r13
0067AF5A  44 8B F0                        mov r14d, eax
0067AF5D  8B F0                           mov esi, eax
0067AF5F  E8 0C 7F CC FF                  call 0x140342e70
0067AF64  EB E3                           jmp 0x14067af49
0067AF66  8B 75 94                        mov esi, dword ptr [rbp - 0x6c]
0067AF69  83 7D 90 00                     cmp dword ptr [rbp - 0x70], 0
0067AF6D  74 38                           je 0x14067afa7
0067AF6F  44 39 2D 36 50 7B 00            cmp dword ptr [rip + 0x7b5036], r13d
0067AF76  74 2F                           je 0x14067afa7
0067AF78  8A 05 0A BB 94 00               mov al, byte ptr [rip + 0x94bb0a]
0067AF7E  24 30                           and al, 0x30
0067AF80  3C 20                           cmp al, 0x20
0067AF82  72 23                           jb 0x14067afa7
0067AF84  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
0067AF89  48 8D 0D 20 5A 9A FF            lea rcx, [rip - 0x65a5e0]
0067AF90  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
0067AF95  45 33 C9                        xor r9d, r9d
0067AF98  45 33 C0                        xor r8d, r8d
0067AF9B  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0067AFA0  33 D2                           xor edx, edx
0067AFA2  E8 69 5D 03 00                  call 0x1406b0d10
0067AFA7  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
0067AFAB  49 2B FF                        sub rdi, r15
0067AFAE  48 03 7D A0                     add rdi, qword ptr [rbp - 0x60]
0067AFB2  48 C1 E7 0C                     shl rdi, 0xc
0067AFB6  48 89 38                        mov qword ptr [rax], rdi
0067AFB9  B8 01 00 00 00                  mov eax, 1
0067AFBE  48 39 45 A0                     cmp qword ptr [rbp - 0x60], rax
0067AFC2  41 0F 44 F6                     cmove esi, r14d
0067AFC6  8B C6                           mov eax, esi
0067AFC8  EB 05                           jmp 0x14067afcf
0067AFCA  B8 EF 00 00 C0                  mov eax, 0xc00000ef
0067AFCF  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
0067AFD3  48 33 CC                        xor rcx, rsp
0067AFD6  E8 65 16 03 00                  call 0x1406ac640
0067AFDB  48 8B 9C 24 80 01 00 00         mov rbx, qword ptr [rsp + 0x180]
0067AFE3  48 81 C4 30 01 00 00            add rsp, 0x130
0067AFEA  41 5F                           pop r15
0067AFEC  41 5E                           pop r14
0067AFEE  41 5D                           pop r13
0067AFF0  41 5C                           pop r12
0067AFF2  5F                              pop rdi
0067AFF3  5E                              pop rsi
0067AFF4  5D                              pop rbp
0067AFF5  C3                              ret
0067AFF6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmMarkPhysicalMemoryAsBad(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int8 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int8 v_stack_mE5;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int8 v_stack_mF8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 7929037)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r13 = 0;
    v_stack_mC0 = a2;
    v_stack_mD0 = 0;
    v_stack_mF0 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) & ((unsigned int)((unsigned int)(0xFFFULL))));
    if (((unsigned int)(result)) > ((unsigned int)(v_r13 + 1))) goto loc_0067AFCA;
    if (((*(unsigned int *)(a2)) & ((unsigned int)((unsigned int)(0xFFFULL)))) == 0) goto loc_0067AAB5;
    goto loc_0067AFCF;
loc_0067AAB5:
    if (((*(unsigned __int64 *)(v_rip + 9748424)) & (0x10000000ULL)) != 0) goto loc_0067AACC;
    goto loc_0067AFCF;
loc_0067AACC:
    v_rsi = (*(unsigned __int64 *)(a2)) >> (12);
    v_rdi = (*(unsigned __int64 *)(a1)) >> (12);
    v_stack_mC8 = v_rsi;
    v_stack_mE0 = v_rdi + v_rsi * 1;
    if (v_rdi >= (v_rdi + v_rsi * 1)) goto loc_0067AFCA;
    v_r12 = (unsigned int)(~((unsigned int)(*(unsigned int *)(a1))));
    v_stack_mD4 = 0;
    v_r12 = (unsigned int)((v_r12) & ((unsigned int)(v_r13 + 1)));
    v_stack_mD8 = 0;
    v_r12 = (unsigned int)((v_r12) << (28));
    v_r12 = (unsigned int)((v_r12) + (0x2C100000ULL));
    v_rbx = (v_rdi + v_rdi * 2) << (4);
    v_rbx = (v_rbx) + ((unsigned int)(0xC0000002ULL));
loc_0067AB20:
    if (v_rdi >= (v_rdi + v_rsi * 1)) goto loc_0067AF66;
    result = MiIsPageInHugePfn(v_rdi, (unsigned int)(0xFFFULL), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0067AB5F;
    result = MiMarkHugePfnBad(v_rdi, (unsigned int)((unsigned int)(v_r12)), a3, a4);
loc_0067AB40:
    if (((unsigned int)(result)) != 0xC0000434ULL) goto loc_0067AF3A;
    v_rdi = (v_rdi) - (1);
    v_rbx = (v_rbx) - (48);
    goto loc_0067AF3A;
loc_0067AB5F:
    result = MiSafeLockPage(v_rdi, (unsigned int)((unsigned int)(v_r12)), a3, a4);
    if (((unsigned __int8)(result)) != 17) goto loc_0067AB76;
    goto loc_0067AF35;
loc_0067AB76:
    if (((unsigned __int8)(result)) >= 17) goto loc_0067AB96;
    result = MiUnlockPage(v_rbx, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    result = MiMarkFileOnlyPfnBad(v_rbx, (unsigned int)((unsigned int)(v_r12)), a3, a4);
    goto loc_0067AB40;
loc_0067AB96:
    result = MiReferencePagePartition(v_rbx, 1, v_stack_mF0, a4);
    result = MiUnlockPage(v_rbx, (unsigned __int8)((unsigned __int8)(result)), v_stack_mF0, a4);
    if (v_stack_mF0 != 0) goto loc_0067ABC5;
    goto loc_0067AF31;
loc_0067ABC5:
    a4 = 0;
    a3 = 0;
    result = MiAcquireNonPagedResources(v_stack_mF0, a4 + 2, a3, a4);
    if (sign_flag) goto loc_0067AF52;
    result = MiAllocatePool(32 + 32, 32, (unsigned int)(0x6C42694DULL), a4);
    result = MiSafeLockPage(v_rdi, 32, (unsigned int)(0x6C42694DULL), a4);
    v_stack_mF8 = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) != 17) goto loc_0067AC42;
loc_0067AC15:
    result = MiReleaseNonPagedResources(v_stack_mF0, 2, (unsigned int)(0x6C42694DULL), a4);
    result = PsDereferencePartition(*(unsigned __int64 *)(v_stack_mF0 + 184), 2, (unsigned int)(0x6C42694DULL), a4);
    v_r13 = 0;
    if (result == 0) goto loc_0067AF31;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x6C42694DULL), a4);
    goto loc_0067AF31;
loc_0067AC42:
    result = (*(unsigned __int64 *)(v_rbx + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8082491) + result * 8)) == v_stack_mF0) goto loc_0067ACA2;
    result = MiUnlockPage(v_rbx, v_stack_mF8, (unsigned int)(0x6C42694DULL), a4);
    result = MiReleaseNonPagedResources(v_stack_mF0, 2, (unsigned int)(0x6C42694DULL), a4);
    result = PsDereferencePartition(0, 2, (unsigned int)(0x6C42694DULL), a4);
    v_r13 = 0;
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x6C42694DULL), a4);
    }
    v_rdi = (v_rdi) - 1;
    v_rbx = (v_rbx) - (48);
    goto loc_0067AF31;
loc_0067ACA2:
    if (condition_is_above_or_equal) goto loc_0067ACC3;
    if ((*(unsigned __int8 *)(v_rbx + 35)) >= 0) {
        result = *(unsigned int *)(v_rbx + 32);
        v_stack_mE8 = (unsigned int)(result);
        result = (unsigned int)((result) >> (24));
        result = (unsigned __int8)((result) | (128));
        v_stack_mE5 = (unsigned __int8)(result);
        result = v_stack_mE8;
        *(unsigned int *)(v_rbx + 32) = (unsigned int)(result);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) == 0) goto loc_0067AD0D;
    result = MiUnlockPage(v_rbx, v_stack_mF8, (unsigned int)(0x6C42694DULL), a4);
    result = MiReleaseNonPagedResources(v_stack_mF0, 2, (unsigned int)(0x6C42694DULL), a4);
    result = PsDereferencePartition(0, 2, (unsigned int)(0x6C42694DULL), a4);
    v_r13 = 0;
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x6C42694DULL), a4);
    }
    goto loc_0067AF31;
loc_0067AD0D:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rbx + 34)) & (7));
    if (((unsigned __int8)(result)) != 5) goto loc_0067AD40;
    if (((unsigned __int8)(result)) < 5) goto loc_0067AD2A;
    result = MiIsPageOnBadList(v_rbx, a2, (unsigned int)(0x6C42694DULL), a4);
    if ((unsigned int)(result) == 0) goto loc_0067AD40;
loc_0067AD2A:
    result = MiUnlockPage(v_rbx, v_stack_mF8, (unsigned int)(0x6C42694DULL), a4);
    goto loc_0067AC15;
loc_0067AD40:
    a3 = 0;
    result = MiSetPfnRemovalRequested(v_rbx, (unsigned int)((unsigned int)(a3 + 1)), a3, result);
    v_r14 = 0;
    result = MiGetPfnSlabType(v_rbx, (unsigned int)((unsigned int)(a3 + 1)), a3, result);
    v_rsi = 0;
    if (((unsigned int)(result)) != 9) {
        a1 = v_rbx;
        result = MiIsPfnFromChargedSlabAllocation(a1, (unsigned int)((unsigned int)(a3 + 1)), a3, result);
        v_rsi = 0;
        if ((unsigned int)(result) == 0) { v_rsi = (unsigned int)(a3 + 1); }
    }
    if ((*(unsigned __int8 *)(v_rbx + 35)) >= 0) goto loc_0067ADC8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 1204)))) == -1) goto loc_0067ADC8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 1708)))) & (2)) == 0) goto loc_0067ADCD;
    if (sign_flag) goto loc_0067ADC8;
    result = MiIsPfnCommitNotCharged(v_rbx, (unsigned int)((unsigned int)(a3 + 1)), a3, result);
    if ((unsigned int)(result) == 0) goto loc_0067ADC8;
    result = MiStoreDiscardPoisonedPage(v_stack_mF0, v_rbx, v_stack_mF8, result);
    goto loc_0067ADCD;
loc_0067ADC8:
loc_0067ADCD:
    if (((unsigned __int8)(v_stack_mF8)) != 17) {
        a1 = v_rbx;
        result = MiUnlockPage(a1, v_stack_mF8, v_stack_mF8, result);
    }
    if ((unsigned int)(v_rsi) != 0) {
        a2 = 0;
        a1 = v_stack_mB0;
        a3 = a2 + 88;
        result = memset(a1, a2, a3, result);
        a2 = v_stack_mB8;
        v_stack_mB8 = v_stack_mF0;
        a1 = v_rip - 2288192;
        v_stack_m58 = v_rdi;
        result = KeGenericCallDpcEx(a1, a2, a3, result);
    }
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = 0;
    a4 = 0;
    v_stack_m110 = 0;
    v_stack_m118 = 0;
    v_stack_m120 = (unsigned int)((unsigned int)((unsigned int)(v_r12)));
    v_stack_m128 = 255;
    v_stack_m130 = 0x80000000ULL;
    v_stack_m138 = 1;
    v_stack_m140 = 1;
    v_stack_m148 = 0;
    result = MiFindContiguousPagesEx(v_stack_mF0, v_rdi, v_rdi, a4);
    result = MiSafeLockPage(v_rdi, v_rdi, v_rdi, a4);
    v_stack_mF8 = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) != 17) goto loc_0067AE7A;
    goto loc_0067AF09;
loc_0067AE7A:
    a2 = 0;
    if (sign_flag) goto loc_0067AECF;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) == 0) goto loc_0067AEB5;
    v_stack_mE8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
    v_stack_mE8 = 0;
    *(unsigned int *)(v_rbx + 32) = (unsigned int)((unsigned int)(v_stack_mE8));
    result = MiSetPfnContainingFrame(v_rbx, a2, v_rdi, a4);
    result = MiInsertPageInList(v_rbx, 32, v_rdi, a4);
    goto loc_0067AEF8;
loc_0067AEB5:
    result = MiUnlockPage(v_rbx, v_stack_mF8, v_rdi, a4);
    a3 = 0;
    result = MiFreeContiguousPages(v_rdi, a3 + 1, a3, a4);
    goto loc_0067AF16;
loc_0067AECF:
    result = MiIsPageOnBadList(v_rdi, a3 + 1, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0067AEF6;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) == 0) goto loc_0067AEF8;
    *(unsigned __int8 *)(v_rip + 8082269) = 1;
    v_stack_mD8 = 1;
loc_0067AEF6:
loc_0067AEF8:
    result = MiUnlockPage(v_rbx, v_stack_mF8, a3, a4);
loc_0067AF09:
    result = MiReleaseNonPagedResources(v_stack_mF0, 1, a3, a4);
loc_0067AF16:
    result = PsDereferencePartition(0, 1, a3, a4);
    if (((unsigned int)((unsigned int)((unsigned int)(a3 + 1)))) == 0xC000012DULL) goto loc_0067AF46;
    if (((unsigned int)((unsigned int)((unsigned int)(a3 + 1)))) == 0xC000009AULL) goto loc_0067AF46;
    v_r13 = 0;
loc_0067AF31:
loc_0067AF35:
loc_0067AF3A:
    v_rdi = (v_rdi) + (1);
    v_rbx = (v_rbx) + (48);
    goto loc_0067AB20;
loc_0067AF46:
loc_0067AF49:
    v_r13 = 0;
    goto loc_0067AF69;
loc_0067AF52:
    result = PsDereferencePartition(0, 1, a3, a4);
    goto loc_0067AF49;
loc_0067AF66:
loc_0067AF69:
    if (v_stack_mD8 == 0) goto loc_0067AFA7;
    if ((*(unsigned int *)(v_rip + 8081462)) == 0) goto loc_0067AFA7;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 9747210)) & (48));
    if (((unsigned __int8)(result)) >= 32) {
        v_stack_m138 = 0;
        a1 = v_rip - 6661600;
        v_stack_m140 = 0;
        a4 = 0;
        a3 = 0;
        v_stack_m148 = 0;
        a2 = 0;
        result = ZwUpdateWnfStateData(a1, a2, a3, a4);
    }
    v_rdi = (v_rdi) - (v_stack_mE0);
    v_rdi = (v_rdi) + (v_stack_mC8);
    v_rdi = (v_rdi) << (12);
    *(unsigned __int64 *)(v_stack_mC0) = v_rdi;
    v_rsi = (unsigned int)(v_stack_mD4);
    if (v_stack_mC8 == 1) { v_rsi = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)))); }
    goto loc_0067AFCF;
loc_0067AFCA:
loc_0067AFCF:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (304);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmMarkPhysicalMemoryAsBad(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint32_t v_stack_m120;
    uint8_t v_stack_m128;
    uint32_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint8_t v_stack_mE5;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint8_t v_stack_mF8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x78FCCD)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r13 = 0;
    v_stack_mC0 = Arg2;
    v_stack_mD0 = 0;
    v_stack_mF0 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) & ((uint32_t)((uint32_t)(0xFFFULL))));
    if (((uint32_t)(result)) > ((uint32_t)(local_r13 + 1))) goto loc_0067AFCA;
    if (((*(uint32_t *)(arg2)) & ((uint32_t)((uint32_t)(0xFFFULL)))) == 0) goto loc_0067AAB5;
    goto loc_0067AFCF;
loc_0067AAB5:
    if (((*(uint64_t *)(v_rip + 0x94BFC8)) & (0x10000000ULL)) != 0) goto loc_0067AACC;
    goto loc_0067AFCF;
loc_0067AACC:
    local_rsi = (*(uint64_t *)(arg2)) >> (12);
    local_rdi = (*(uint64_t *)(arg1)) >> (12);
    v_stack_mC8 = local_rsi;
    v_stack_mE0 = local_rdi + local_rsi * 1;
    if (local_rdi >= (local_rdi + local_rsi * 1)) goto loc_0067AFCA;
    local_r12 = (uint32_t)(~((uint32_t)(*(uint32_t *)(arg1))));
    v_stack_mD4 = 0;
    local_r12 = (uint32_t)((local_r12) & ((uint32_t)(local_r13 + 1)));
    v_stack_mD8 = 0;
    local_r12 = (uint32_t)((local_r12) << (28));
    local_r12 = (uint32_t)((local_r12) + (0x2C100000ULL));
    local_rbx = (local_rdi + local_rdi * 2) << (4);
    local_rbx = (local_rbx) + ((uint32_t)(0xC0000002ULL));
loc_0067AB20:
    if (local_rdi >= (local_rdi + local_rsi * 1)) goto loc_0067AF66;
    result = MiIsPageInHugePfn(local_rdi, (uint32_t)(0xFFFULL), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0067AB5F;
    result = MiMarkHugePfnBad(local_rdi, (uint32_t)((uint32_t)(local_r12)), Arg3, Arg4);
loc_0067AB40:
    if (((uint32_t)(result)) != 0xC0000434ULL) goto loc_0067AF3A;
    local_rdi = (local_rdi) - (1);
    local_rbx = (local_rbx) - (48);
    goto loc_0067AF3A;
loc_0067AB5F:
    result = MiSafeLockPage(local_rdi, (uint32_t)((uint32_t)(local_r12)), Arg3, Arg4);
    if (((uint8_t)(result)) != 17) goto loc_0067AB76;
    goto loc_0067AF35;
loc_0067AB76:
    if (((uint8_t)(result)) >= 17) goto loc_0067AB96;
    result = MiUnlockPage(local_rbx, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    result = MiMarkFileOnlyPfnBad(local_rbx, (uint32_t)((uint32_t)(local_r12)), Arg3, Arg4);
    goto loc_0067AB40;
loc_0067AB96:
    result = MiReferencePagePartition(local_rbx, 1, v_stack_mF0, Arg4);
    result = MiUnlockPage(local_rbx, (uint8_t)((uint8_t)(result)), v_stack_mF0, Arg4);
    if (v_stack_mF0 != 0) goto loc_0067ABC5;
    goto loc_0067AF31;
loc_0067ABC5:
    Arg4 = 0;
    Arg3 = 0;
    result = MiAcquireNonPagedResources(v_stack_mF0, Arg4 + 2, Arg3, Arg4);
    if (sign_flag) goto loc_0067AF52;
    result = MiAllocatePool(32 + 32, 32, (uint32_t)(0x6C42694DULL), Arg4);
    result = MiSafeLockPage(local_rdi, 32, (uint32_t)(0x6C42694DULL), Arg4);
    v_stack_mF8 = (uint8_t)(result);
    if (((uint8_t)(result)) != 17) goto loc_0067AC42;
loc_0067AC15:
    result = MiReleaseNonPagedResources(v_stack_mF0, 2, (uint32_t)(0x6C42694DULL), Arg4);
    result = PsDereferencePartition(*(uint64_t *)(v_stack_mF0 + 0xB8), 2, (uint32_t)(0x6C42694DULL), Arg4);
    local_r13 = 0;
    if (result == 0) goto loc_0067AF31;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x6C42694DULL), Arg4);
    goto loc_0067AF31;
loc_0067AC42:
    result = (*(uint64_t *)(local_rbx + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x7B543B) + result * 8)) == v_stack_mF0) goto loc_0067ACA2;
    result = MiUnlockPage(local_rbx, v_stack_mF8, (uint32_t)(0x6C42694DULL), Arg4);
    result = MiReleaseNonPagedResources(v_stack_mF0, 2, (uint32_t)(0x6C42694DULL), Arg4);
    result = PsDereferencePartition(0, 2, (uint32_t)(0x6C42694DULL), Arg4);
    local_r13 = 0;
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x6C42694DULL), Arg4);
    }
    local_rdi = (local_rdi) - 1;
    local_rbx = (local_rbx) - (48);
    goto loc_0067AF31;
loc_0067ACA2:
    if (condition_is_above_or_equal) goto loc_0067ACC3;
    if ((*(uint8_t *)(local_rbx + 0x23)) >= 0) {
        result = *(uint32_t *)(local_rbx + 0x20);
        v_stack_mE8 = (uint32_t)(result);
        result = (uint32_t)((result) >> (24));
        result = (uint8_t)((result) | (128));
        v_stack_mE5 = (uint8_t)(result);
        result = v_stack_mE8;
        *(uint32_t *)(local_rbx + 0x20) = (uint32_t)(result);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) == 0) goto loc_0067AD0D;
    result = MiUnlockPage(local_rbx, v_stack_mF8, (uint32_t)(0x6C42694DULL), Arg4);
    result = MiReleaseNonPagedResources(v_stack_mF0, 2, (uint32_t)(0x6C42694DULL), Arg4);
    result = PsDereferencePartition(0, 2, (uint32_t)(0x6C42694DULL), Arg4);
    local_r13 = 0;
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x6C42694DULL), Arg4);
    }
    goto loc_0067AF31;
loc_0067AD0D:
    result = (uint8_t)((*(uint8_t *)(local_rbx + 0x22)) & (7));
    if (((uint8_t)(result)) != 5) goto loc_0067AD40;
    if (((uint8_t)(result)) < 5) goto loc_0067AD2A;
    result = MiIsPageOnBadList(local_rbx, Arg2, (uint32_t)(0x6C42694DULL), Arg4);
    if ((uint32_t)(result) == 0) goto loc_0067AD40;
loc_0067AD2A:
    result = MiUnlockPage(local_rbx, v_stack_mF8, (uint32_t)(0x6C42694DULL), Arg4);
    goto loc_0067AC15;
loc_0067AD40:
    Arg3 = 0;
    result = MiSetPfnRemovalRequested(local_rbx, (uint32_t)((uint32_t)(Arg3 + 1)), Arg3, result);
    local_r14 = 0;
    result = MiGetPfnSlabType(local_rbx, (uint32_t)((uint32_t)(Arg3 + 1)), Arg3, result);
    local_rsi = 0;
    if (((uint32_t)(result)) != 9) {
        Arg1 = local_rbx;
        result = MiIsPfnFromChargedSlabAllocation(Arg1, (uint32_t)((uint32_t)(Arg3 + 1)), Arg3, result);
        local_rsi = 0;
        if ((uint32_t)(result) == 0) { local_rsi = (uint32_t)(Arg3 + 1); }
    }
    if ((*(uint8_t *)(local_rbx + 0x23)) >= 0) goto loc_0067ADC8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x4B4)))) == -1) goto loc_0067ADC8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x6AC)))) & (2)) == 0) goto loc_0067ADCD;
    if (sign_flag) goto loc_0067ADC8;
    result = MiIsPfnCommitNotCharged(local_rbx, (uint32_t)((uint32_t)(Arg3 + 1)), Arg3, result);
    if ((uint32_t)(result) == 0) goto loc_0067ADC8;
    result = MiStoreDiscardPoisonedPage(v_stack_mF0, local_rbx, v_stack_mF8, result);
    goto loc_0067ADCD;
loc_0067ADC8:
loc_0067ADCD:
    if (((uint8_t)(v_stack_mF8)) != 17) {
        Arg1 = local_rbx;
        result = MiUnlockPage(Arg1, v_stack_mF8, v_stack_mF8, result);
    }
    if ((uint32_t)(local_rsi) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mB0;
        Arg3 = Arg2 + 88;
        result = memset(Arg1, Arg2, Arg3, result);
        Arg2 = v_stack_mB8;
        v_stack_mB8 = v_stack_mF0;
        Arg1 = v_rip - 2288192;
        v_stack_m58 = local_rdi;
        result = KeGenericCallDpcEx(Arg1, Arg2, Arg3, result);
    }
    v_stack_m100 = v_stack_mD0;
    v_stack_m108 = 0;
    Arg4 = 0;
    v_stack_m110 = 0;
    v_stack_m118 = 0;
    v_stack_m120 = (uint32_t)((uint32_t)((uint32_t)(local_r12)));
    v_stack_m128 = 255;
    v_stack_m130 = 0x80000000ULL;
    v_stack_m138 = 1;
    v_stack_m140 = 1;
    v_stack_m148 = 0;
    result = MiFindContiguousPagesEx(v_stack_mF0, local_rdi, local_rdi, Arg4);
    result = MiSafeLockPage(local_rdi, local_rdi, local_rdi, Arg4);
    v_stack_mF8 = (uint8_t)(result);
    if (((uint8_t)(result)) != 17) goto loc_0067AE7A;
    goto loc_0067AF09;
loc_0067AE7A:
    Arg2 = 0;
    if (sign_flag) goto loc_0067AECF;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) == 0) goto loc_0067AEB5;
    v_stack_mE8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
    v_stack_mE8 = 0;
    *(uint32_t *)(local_rbx + 0x20) = (uint32_t)((uint32_t)(v_stack_mE8));
    result = MiSetPfnContainingFrame(local_rbx, Arg2, local_rdi, Arg4);
    result = MiInsertPageInList(local_rbx, 32, local_rdi, Arg4);
    goto loc_0067AEF8;
loc_0067AEB5:
    result = MiUnlockPage(local_rbx, v_stack_mF8, local_rdi, Arg4);
    Arg3 = 0;
    result = MiFreeContiguousPages(local_rdi, Arg3 + 1, Arg3, Arg4);
    goto loc_0067AF16;
loc_0067AECF:
    result = MiIsPageOnBadList(local_rdi, Arg3 + 1, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_0067AEF6;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) == 0) goto loc_0067AEF8;
    *(uint8_t *)(v_rip + 0x7B535D) = 1;
    v_stack_mD8 = 1;
loc_0067AEF6:
loc_0067AEF8:
    result = MiUnlockPage(local_rbx, v_stack_mF8, Arg3, Arg4);
loc_0067AF09:
    result = MiReleaseNonPagedResources(v_stack_mF0, 1, Arg3, Arg4);
loc_0067AF16:
    result = PsDereferencePartition(0, 1, Arg3, Arg4);
    if (((uint32_t)((uint32_t)((uint32_t)(Arg3 + 1)))) == 0xC000012DULL) goto loc_0067AF46;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg3 + 1)))) == 0xC000009AULL) goto loc_0067AF46;
    local_r13 = 0;
loc_0067AF31:
loc_0067AF35:
loc_0067AF3A:
    local_rdi = (local_rdi) + (1);
    local_rbx = (local_rbx) + (48);
    goto loc_0067AB20;
loc_0067AF46:
loc_0067AF49:
    local_r13 = 0;
    goto loc_0067AF69;
loc_0067AF52:
    result = PsDereferencePartition(0, 1, Arg3, Arg4);
    goto loc_0067AF49;
loc_0067AF66:
loc_0067AF69:
    if (v_stack_mD8 == 0) goto loc_0067AFA7;
    if ((*(uint32_t *)(v_rip + 0x7B5036)) == 0) goto loc_0067AFA7;
    result = (uint8_t)((*(uint8_t *)(v_rip + 0x94BB0A)) & (48));
    if (((uint8_t)(result)) >= 32) {
        v_stack_m138 = 0;
        Arg1 = v_rip - 6661600;
        v_stack_m140 = 0;
        Arg4 = 0;
        Arg3 = 0;
        v_stack_m148 = 0;
        Arg2 = 0;
        result = ZwUpdateWnfStateData(Arg1, Arg2, Arg3, Arg4);
    }
    local_rdi = (local_rdi) - (v_stack_mE0);
    local_rdi = (local_rdi) + (v_stack_mC8);
    local_rdi = (local_rdi) << (12);
    *(uint64_t *)(v_stack_mC0) = local_rdi;
    local_rsi = (uint32_t)(v_stack_mD4);
    if (v_stack_mC8 == 1) { local_rsi = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)))); }
    goto loc_0067AFCF;
loc_0067AFCA:
loc_0067AFCF:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (304);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0067AA50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
