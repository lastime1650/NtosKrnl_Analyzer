# MiCreatePrototypePtes

- RVA: `0x002950FC`–`0x00295682` (길이 `1,414` bytes)
- VA: `0x00000001402950FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00067818`
- 디코드: `359`개 명령, `1,414/1,414` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0029514E` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x002951C4` → [MiInitializePrototypePtes](../../page/98/MiInitializePrototypePtes_function_009829AC.md) (function, `0x009829AC`)
- `0x00295232` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0029526D` → [MiIncrementSubsectionViewCount](../24/MiIncrementSubsectionViewCount_function_00249440.md) (function, `0x00249440`)
- `0x002952C7` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00295302` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00295343` → [MiUpdateSystemProtoPtesTree](MiUpdateSystemProtoPtesTree_function_00295F0C.md) (function, `0x00295F0C`)
- `0x00295353` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00295371` → [MiControlAreaRequiresCharge](../3B/MiControlAreaRequiresCharge_function_003B36CC.md) (function, `0x003B36CC`)
- `0x002953DC` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x002953F5` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00295443` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00295471` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00295486` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x002954B5` → [MiAllocateFileExtents](../../page/AB/MiAllocateFileExtents_function_00ABDF54.md) (function, `0x00ABDF54`)
- `0x002954D7` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x002954F4` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0029553D` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00295578` → [MiReturnCrossPartitionSectionCharges](../4B/MiReturnCrossPartitionSectionCharges_function_004BA61C.md) (function, `0x004BA61C`)
- `0x0029558C` → [MiGetSubsectionCharges](../45/MiGetSubsectionCharges_function_00458A04.md) (function, `0x00458A04`)
- `0x002955A9` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x002955B9` → [MiChargeLargeProtoSubsection](../../page/80/MiChargeLargeProtoSubsection_function_00800A24.md) (function, `0x00800A24`)
- `0x002955D3` → [MiGetCommittedPages](../32/MiGetCommittedPages_function_00325CE0.md) (function, `0x00325CE0`)
- `0x002955E6` → [MiGetCommittedPages](../32/MiGetCommittedPages_function_00325CE0.md) (function, `0x00325CE0`)
- `0x0029560F` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0029564E` → [MiChargeLargeProtoSubsection](../../page/80/MiChargeLargeProtoSubsection_function_00800A24.md) (function, `0x00800A24`)
- `0x00295678` → [MiReturnCrossPartitionSectionCharges](../4B/MiReturnCrossPartitionSectionCharges_function_004BA61C.md) (function, `0x004BA61C`)

### Direct callers
- [MiAddViewsForSection](../32/MiAddViewsForSection_function_00324990.md) at `0x00324DA1`

### Static image references
- `0x0029555F` → RVA `0x00E30088` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x002951C4` → [MiInitializePrototypePtes](../../page/98/MiInitializePrototypePtes_function_009829AC.md) (`.text` → `PAGE`)
  - `0x00295302` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002954B5` → [MiAllocateFileExtents](../../page/AB/MiAllocateFileExtents_function_00ABDF54.md) (`.text` → `PAGE`)
  - `0x002955B9` → [MiChargeLargeProtoSubsection](../../page/80/MiChargeLargeProtoSubsection_function_00800A24.md) (`.text` → `PAGE`)
  - `0x0029564E` → [MiChargeLargeProtoSubsection](../../page/80/MiChargeLargeProtoSubsection_function_00800A24.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00295595` → [sub_006DA650 + 0x4F](../6D/Unknown_function_006DA650.md) (`tail-transfer`)
  - `0x002955C0` → [sub_006DA650](../6D/Unknown_function_006DA650.md) (`tail-transfer`)
  - `0x00295605` → [sub_006DA650 + 0xD](../6D/Unknown_function_006DA650.md) (`tail-transfer`)
  - `0x00295615` → [sub_006DA650 + 0xD](../6D/Unknown_function_006DA650.md) (`tail-transfer`)
  - `0x00295631` → [sub_006DA650 + 0x57](../6D/Unknown_function_006DA650.md) (`tail-transfer`)
  - `0x0029563A` → [sub_006DA650 + 0x57](../6D/Unknown_function_006DA650.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002950FC  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00295101  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00295106  55                              push rbp
00295107  56                              push rsi
00295108  57                              push rdi
00295109  41 54                           push r12
0029510B  41 55                           push r13
0029510D  41 56                           push r14
0029510F  41 57                           push r15
00295111  48 83 EC 60                     sub rsp, 0x60
00295115  65 4C 8B 2C 25 88 01 00 00      mov r13, qword ptr gs:[0x188]
0029511E  8B DA                           mov ebx, edx
00295120  4C 8B 31                        mov r14, qword ptr [rcx]
00295123  4C 8B F9                        mov r15, rcx
00295126  41 8B F9                        mov edi, r9d
00295129  33 ED                           xor ebp, ebp
0029512B  B9 12 01 00 00                  mov ecx, 0x112
00295130  89 6C 24 30                     mov dword ptr [rsp + 0x30], ebp
00295134  41 B8 4D 6D 53 74               mov r8d, 0x74536d4d
0029513A  89 AC 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], ebp
00295141  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
00295146  48 8D 14 FD 00 00 00 00         lea rdx, [rdi*8]
0029514E  E8 ED 63 0C 00                  call 0x14035b540
00295153  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00295158  4C 8B E0                        mov r12, rax
0029515B  48 85 C0                        test rax, rax
0029515E  0F 84 2F 02 00 00               je 0x140295393
00295164  49 8B 46 40                     mov rax, qword ptr [r14 + 0x40]
00295168  44 8D 45 01                     lea r8d, [rbp + 1]
0029516C  41 8A 56 3E                     mov dl, byte ptr [r14 + 0x3e]
00295170  8B F5                           mov esi, ebp
00295172  80 E2 0C                        and dl, 0xc
00295175  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0029517A  80 FA 04                        cmp dl, 4
0029517D  40 0F 95 C6                     setne sil
00295181  84 D2                           test dl, dl
00295183  0F 95 C1                        setne cl
00295186  0F BA E3 09                     bt ebx, 9
0029518A  0F 92 C0                        setb al
0029518D  84 C8                           test al, cl
0029518F  74 13                           je 0x1402951a4
00295191  80 FA 08                        cmp dl, 8
00295194  0F 85 19 04 00 00               jne 0x1402955b3
0029519A  BF 0D 00 00 C0                  mov edi, 0xc000000d
0029519F  E9 59 01 00 00                  jmp 0x1402952fd
002951A4  41 8A 46 3E                     mov al, byte ptr [r14 + 0x3e]
002951A8  8B EB                           mov ebp, ebx
002951AA  24 0C                           and al, 0xc
002951AC  83 CD 04                        or ebp, 4
002951AF  3C 04                           cmp al, 4
002951B1  44 8B CE                        mov r9d, esi
002951B4  4D 8B C7                        mov r8, r15
002951B7  48 8B D7                        mov rdx, rdi
002951BA  0F 45 EB                        cmovne ebp, ebx
002951BD  49 8B CC                        mov rcx, r12
002951C0  89 6C 24 38                     mov dword ptr [rsp + 0x38], ebp
002951C4  E8 E3 D7 6E 00                  call 0x1409829ac
002951C9  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
002951CE  33 C0                           xor eax, eax
002951D0  48 85 FF                        test rdi, rdi
002951D3  0F 84 C4 01 00 00               je 0x14029539d
002951D9  8B B4 24 B0 00 00 00            mov esi, dword ptr [rsp + 0xb0]
002951E0  8B C5                           mov eax, ebp
002951E2  48 83 CB FF                     or rbx, 0xffffffffffffffff
002951E6  25 80 00 00 00                  and eax, 0x80
002951EB  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
002951EF  40 F6 C5 04                     test bpl, 4
002951F3  0F 84 6E 01 00 00               je 0x140295367
002951F9  8D 43 02                        lea eax, [rbx + 2]
002951FC  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00295203  45 33 E4                        xor r12d, r12d
00295206  44 89 A4 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r12d
0029520E  83 F8 02                        cmp eax, 2
00295211  0F 84 66 03 00 00               je 0x14029557d
00295217  41 8B F4                        mov esi, r12d
0029521A  44 89 A4 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r12d
00295222  48 85 FF                        test rdi, rdi
00295225  0F 84 8E 01 00 00               je 0x1402953b9
0029522B  4D 8D 66 48                     lea r12, [r14 + 0x48]
0029522F  49 8B CC                        mov rcx, r12
00295232  E8 59 34 FB FF                  call 0x140248690
00295237  8B 94 24 A0 00 00 00            mov edx, dword ptr [rsp + 0xa0]
0029523E  44 8A E8                        mov r13b, al
00295241  83 FA 02                        cmp edx, 2
00295244  0F 84 B9 02 00 00               je 0x140295503
0029524A  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
0029524E  8B E8                           mov ebp, eax
00295250  83 CD 20                        or ebp, 0x20
00295253  83 FA 02                        cmp edx, 2
00295256  0F 84 BE 03 00 00               je 0x14029561a
0029525C  33 FF                           xor edi, edi
0029525E  49 39 7F 08                     cmp qword ptr [r15 + 8], rdi
00295262  0F 85 86 02 00 00               jne 0x1402954ee
00295268  8B D5                           mov edx, ebp
0029526A  49 8B CF                        mov rcx, r15
0029526D  E8 CE 41 FB FF                  call 0x140249440
00295272  44 8D 47 01                     lea r8d, [rdi + 1]
00295276  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
0029527A  41 3B C0                        cmp eax, r8d
0029527D  0F 84 CA 00 00 00               je 0x14029534d
00295283  83 F8 03                        cmp eax, 3
00295286  8B D7                           mov edx, edi
00295288  48 0F 44 F7                     cmove rsi, rdi
0029528C  41 F6 46 3E 0C                  test byte ptr [r14 + 0x3e], 0xc
00295291  0F 85 E4 01 00 00               jne 0x14029547b
00295297  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0029529C  48 85 C9                        test rcx, rcx
0029529F  74 0B                           je 0x1402952ac
002952A1  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
002952A5  41 0B C0                        or eax, r8d
002952A8  41 89 47 20                     mov dword ptr [r15 + 0x20], eax
002952AC  85 D2                           test edx, edx
002952AE  75 0A                           jne 0x1402952ba
002952B0  49 39 7F 08                     cmp qword ptr [r15 + 8], rdi
002952B4  0F 85 6A 03 00 00               jne 0x140295624
002952BA  41 F6 46 3E 0C                  test byte ptr [r14 + 0x3e], 0xc
002952BF  74 61                           je 0x140295322
002952C1  41 8A D5                        mov dl, r13b
002952C4  49 8B CC                        mov rcx, r12
002952C7  E8 F4 2F FB FF                  call 0x1402482c0
002952CC  4C 8B E7                        mov r12, rdi
002952CF  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
002952D3  33 C9                           xor ecx, ecx
002952D5  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
002952DA  4D 85 ED                        test r13, r13
002952DD  0F 84 3A 01 00 00               je 0x14029541d
002952E3  33 DB                           xor ebx, ebx
002952E5  39 5C 24 30                     cmp dword ptr [rsp + 0x30], ebx
002952E9  0F 85 5A 03 00 00               jne 0x140295649
002952EF  48 85 F6                        test rsi, rsi
002952F2  0F 85 60 03 00 00               jne 0x140295658
002952F8  4D 85 E4                        test r12, r12
002952FB  74 0A                           je 0x140295307
002952FD  33 D2                           xor edx, edx
002952FF  49 8B CC                        mov rcx, r12
00295302  E8 69 D5 8E 00                  call 0x140b82870
00295307  8B C7                           mov eax, edi
00295309  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
00295311  48 83 C4 60                     add rsp, 0x60
00295315  41 5F                           pop r15
00295317  41 5E                           pop r14
00295319  41 5D                           pop r13
0029531B  41 5C                           pop r12
0029531D  5F                              pop rdi
0029531E  5E                              pop rsi
0029531F  5D                              pop rbp
00295320  C3                              ret
00295321  CC                              int3
00295322  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00295327  BA 03 00 00 00                  mov edx, 3
0029532C  49 89 47 08                     mov qword ptr [r15 + 8], rax
00295330  48 8B C1                        mov rax, rcx
00295333  48 F7 D8                        neg rax
00295336  48 1B C9                        sbb rcx, rcx
00295339  83 E1 40                        and ecx, 0x40
0029533C  48 83 C1 38                     add rcx, 0x38
00295340  49 03 CF                        add rcx, r15
00295343  E8 C4 0B 00 00                  call 0x140295f0c
00295348  E9 74 FF FF FF                  jmp 0x1402952c1
0029534D  41 8A D5                        mov dl, r13b
00295350  49 8B CC                        mov rcx, r12
00295353  E8 68 2F FB FF                  call 0x1402482c0
00295358  BF 9A 00 00 C0                  mov edi, 0xc000009a
0029535D  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
00295362  E9 6C FF FF FF                  jmp 0x1402952d3
00295367  F7 D8                           neg eax
00295369  49 8B CE                        mov rcx, r14
0029536C  1B D2                           sbb edx, edx
0029536E  83 E2 02                        and edx, 2
00295371  E8 56 E3 11 00                  call 0x1403b36cc
00295376  33 C9                           xor ecx, ecx
00295378  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
0029537F  85 C0                           test eax, eax
00295381  0F 85 7C FE FF FF               jne 0x140295203
00295387  8B F1                           mov esi, ecx
00295389  BF 0B 06 00 C0                  mov edi, 0xc000060b
0029538E  E9 42 FF FF FF                  jmp 0x1402952d5
00295393  B8 9A 00 00 C0                  mov eax, 0xc000009a
00295398  E9 6C FF FF FF                  jmp 0x140295309
0029539D  49 39 46 40                     cmp qword ptr [r14 + 0x40], rax
002953A1  75 6E                           jne 0x140295411
002953A3  49 8B 76 78                     mov rsi, qword ptr [r14 + 0x78]
002953A7  48 B8 FF FF FF FF 0F 00 00 00   movabs rax, 0xfffffffff
002953B1  48 23 F0                        and rsi, rax
002953B4  E9 27 FE FF FF                  jmp 0x1402951e0
002953B9  66 41 01 9D E6 01 00 00         add word ptr [r13 + 0x1e6], bx
002953C1  45 33 C0                        xor r8d, r8d
002953C4  90                              nop
002953C5  C7 84 24 B8 00 00 00 01 00 00 00  mov dword ptr [rsp + 0xb8], 1
002953D0  49 8B 3E                        mov rdi, qword ptr [r14]
002953D3  33 D2                           xor edx, edx
002953D5  48 83 C7 28                     add rdi, 0x28
002953D9  48 8B CF                        mov rcx, rdi
002953DC  E8 4F AE F7 FF                  call 0x140210230
002953E1  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
002953E7  48 8B E8                        mov rbp, rax
002953EA  73 0E                           jae 0x1402953fa
002953EC  4C 8B C7                        mov r8, rdi
002953EF  48 8B D0                        mov rdx, rax
002953F2  48 8B CF                        mov rcx, rdi
002953F5  E8 96 A8 F7 FF                  call 0x14020fc90
002953FA  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
002953FF  48 85 ED                        test rbp, rbp
00295402  0F 84 23 FE FF FF               je 0x14029522b
00295408  C6 45 0A 01                     mov byte ptr [rbp + 0xa], 1
0029540C  E9 1A FE FF FF                  jmp 0x14029522b
00295411  49 8B 06                        mov rax, qword ptr [r14]
00295414  48 8B 70 10                     mov rsi, qword ptr [rax + 0x10]
00295418  E9 C3 FD FF FF                  jmp 0x1402951e0
0029541D  39 8C 24 B8 00 00 00            cmp dword ptr [rsp + 0xb8], ecx
00295424  0F 84 B9 FE FF FF               je 0x1402952e3
0029542A  49 8B 2E                        mov rbp, qword ptr [r14]
0029542D  F0 48 0F C1 5D 28               lock xadd qword ptr [rbp + 0x28], rbx
00295433  80 E3 06                        and bl, 6
00295436  80 FB 02                        cmp bl, 2
00295439  0F 84 66 01 00 00               je 0x1402955a5
0029543F  48 8D 4D 28                     lea rcx, [rbp + 0x28]
00295443  E8 B8 C1 04 00                  call 0x1402e1600
00295448  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0029544D  BA 01 00 00 00                  mov edx, 1
00295452  90                              nop
00295453  66 01 91 E6 01 00 00            add word ptr [rcx + 0x1e6], dx
0029545A  0F 85 83 FE FF FF               jne 0x1402952e3
00295460  48 8D 81 98 00 00 00            lea rax, [rcx + 0x98]
00295467  90                              nop
00295468  48 39 00                        cmp qword ptr [rax], rax
0029546B  0F 84 72 FE FF FF               je 0x1402952e3
00295471  E8 0A D8 04 00                  call 0x1402e2c80
00295476  E9 68 FE FF FF                  jmp 0x1402952e3
0029547B  41 8A D5                        mov dl, r13b
0029547E  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
00295483  49 8B CC                        mov rcx, r12
00295486  E8 35 2E FB FF                  call 0x1402482c0
0029548B  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0029548F  33 D2                           xor edx, edx
00295491  83 4C 24 28 FF                  or dword ptr [rsp + 0x28], 0xffffffff
00295496  25 00 02 00 00                  and eax, 0x200
0029549B  44 8B 8C 24 B0 00 00 00         mov r9d, dword ptr [rsp + 0xb0]
002954A3  83 C8 28                        or eax, 0x28
002954A6  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
002954AB  49 8B CF                        mov rcx, r15
002954AE  C1 E8 03                        shr eax, 3
002954B1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002954B5  E8 9A 8A 82 00                  call 0x140abdf54
002954BA  33 C9                           xor ecx, ecx
002954BC  8B F8                           mov edi, eax
002954BE  85 C0                           test eax, eax
002954C0  0F 88 79 01 00 00               js 0x14029563f
002954C6  41 8A 46 3E                     mov al, byte ptr [r14 + 0x3e]
002954CA  24 0C                           and al, 0xc
002954CC  3C 04                           cmp al, 4
002954CE  0F 84 33 FE FF FF               je 0x140295307
002954D4  49 8B CC                        mov rcx, r12
002954D7  E8 B4 31 FB FF                  call 0x140248690
002954DC  8B 54 24 34                     mov edx, dword ptr [rsp + 0x34]
002954E0  33 FF                           xor edi, edi
002954E2  44 8A E8                        mov r13b, al
002954E5  44 8D 47 01                     lea r8d, [rdi + 1]
002954E9  E9 A9 FD FF FF                  jmp 0x140295297
002954EE  41 8A D5                        mov dl, r13b
002954F1  49 8B CC                        mov rcx, r12
002954F4  E8 C7 2D FB FF                  call 0x1402482c0
002954F9  BF 0A 02 00 C0                  mov edi, 0xc000020a
002954FE  E9 5A FE FF FF                  jmp 0x14029535d
00295503  48 85 FF                        test rdi, rdi
00295506  0F 84 C4 00 00 00               je 0x1402955d0
0029550C  41 8B 47 2C                     mov eax, dword ptr [r15 + 0x2c]
00295510  41 B8 FF FF FF 3F               mov r8d, 0x3fffffff
00295516  41 8B 4F 34                     mov ecx, dword ptr [r15 + 0x34]
0029551A  41 23 C8                        and ecx, r8d
0029551D  2B C1                           sub eax, ecx
0029551F  48 3B F0                        cmp rsi, rax
00295522  0F 84 22 FD FF FF               je 0x14029524a
00295528  41 8B 4F 34                     mov ecx, dword ptr [r15 + 0x34]
0029552C  8B EE                           mov ebp, esi
0029552E  41 8B 77 2C                     mov esi, dword ptr [r15 + 0x2c]
00295532  41 23 C8                        and ecx, r8d
00295535  2B F1                           sub esi, ecx
00295537  41 8A D5                        mov dl, r13b
0029553A  49 8B CC                        mov rcx, r12
0029553D  E8 7E 2D FB FF                  call 0x1402482c0
00295542  45 33 E4                        xor r12d, r12d
00295545  48 85 FF                        test rdi, rdi
00295548  0F 84 A5 00 00 00               je 0x1402955f3
0029554E  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
00295553  85 ED                           test ebp, ebp
00295555  74 26                           je 0x14029557d
00295557  41 0F B7 46 3C                  movzx eax, word ptr [r14 + 0x3c]
0029555C  48 85 FF                        test rdi, rdi
0029555F  48 8B 0D 22 AB B9 00            mov rcx, qword ptr [rip + 0xb9ab22]
00295566  41 8B D4                        mov edx, r12d
00295569  0F 95 C2                        setne dl
0029556C  44 8B C5                        mov r8d, ebp
0029556F  25 FF 03 00 00                  and eax, 0x3ff
00295574  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00295578  E8 9F 50 22 00                  call 0x1404ba61c
0029557D  48 85 F6                        test rsi, rsi
00295580  0F 84 9C FC FF FF               je 0x140295222
00295586  48 8B D6                        mov rdx, rsi
00295589  49 8B CF                        mov rcx, r15
0029558C  E8 73 34 1C 00                  call 0x140458a04
00295591  8B F8                           mov edi, eax
00295593  85 C0                           test eax, eax
00295595  0F 88 04 51 44 00               js 0x1406da69f
0029559B  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
002955A0  E9 7D FC FF FF                  jmp 0x140295222
002955A5  48 8D 4D 28                     lea rcx, [rbp + 0x28]
002955A9  E8 22 08 FD FF                  call 0x140265dd0
002955AE  E9 8C FE FF FF                  jmp 0x14029543f
002955B3  41 8B D0                        mov edx, r8d
002955B6  49 8B CF                        mov rcx, r15
002955B9  E8 66 B4 56 00                  call 0x140800a24
002955BE  85 C0                           test eax, eax
002955C0  0F 85 8A 50 44 00               jne 0x1406da650
002955C6  BF 9A 00 00 C0                  mov edi, 0xc000009a
002955CB  E9 2D FD FF FF                  jmp 0x1402952fd
002955D0  49 8B CE                        mov rcx, r14
002955D3  E8 08 07 09 00                  call 0x140325ce0
002955D8  48 3B F0                        cmp rsi, rax
002955DB  0F 84 69 FC FF FF               je 0x14029524a
002955E1  49 8B CE                        mov rcx, r14
002955E4  8B EE                           mov ebp, esi
002955E6  E8 F5 06 09 00                  call 0x140325ce0
002955EB  48 8B F0                        mov rsi, rax
002955EE  E9 44 FF FF FF                  jmp 0x140295537
002955F3  49 8B 3E                        mov rdi, qword ptr [r14]
002955F6  48 8B D3                        mov rdx, rbx
002955F9  F0 48 0F C1 57 28               lock xadd qword ptr [rdi + 0x28], rdx
002955FF  80 E2 06                        and dl, 6
00295602  80 FA 02                        cmp dl, 2
00295605  0F 85 52 50 44 00               jne 0x1406da65d
0029560B  48 8D 4F 28                     lea rcx, [rdi + 0x28]
0029560F  E8 BC 07 FD FF                  call 0x140265dd0
00295614  90                              nop
00295615  E9 43 50 44 00                  jmp 0x1406da65d
0029561A  8B E8                           mov ebp, eax
0029561C  83 CD 28                        or ebp, 0x28
0029561F  E9 38 FC FF FF                  jmp 0x14029525c
00295624  83 BC 24 A0 00 00 00 02         cmp dword ptr [rsp + 0xa0], 2
0029562C  BF 0A 02 00 C0                  mov edi, 0xc000020a
00295631  0F 85 70 50 44 00               jne 0x1406da6a7
00295637  83 CD 10                        or ebp, 0x10
0029563A  E9 68 50 44 00                  jmp 0x1406da6a7
0029563F  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
00295644  E9 8C FC FF FF                  jmp 0x1402952d5
00295649  33 D2                           xor edx, edx
0029564B  49 8B CF                        mov rcx, r15
0029564E  E8 D1 B3 56 00                  call 0x140800a24
00295653  E9 97 FC FF FF                  jmp 0x1402952ef
00295658  41 0F B7 46 3C                  movzx eax, word ptr [r14 + 0x3c]
0029565D  4D 85 ED                        test r13, r13
00295660  48 8B 0D 21 AA B9 00            mov rcx, qword ptr [rip + 0xb9aa21]
00295667  8B D3                           mov edx, ebx
00295669  0F 95 C2                        setne dl
0029566C  4C 8B C6                        mov r8, rsi
0029566F  25 FF 03 00 00                  and eax, 0x3ff
00295674  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00295678  E8 9F 4F 22 00                  call 0x1404ba61c
0029567D  E9 76 FC FF FF                  jmp 0x1402952f8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCreatePrototypePtes(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p8;
    unsigned int v_stack_pA0;
    unsigned int v_stack_pB0;
    unsigned int v_stack_pB8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (96);
    v_rbp = 0;
    v_stack_m68 = 0;
    v_stack_p20 = 0;
    v_stack_m48 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = MiAllocatePool(274, (unsigned int)(a4) * 8, (unsigned int)(0x74536D4DULL), a4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00295393;
    a2 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62)) & (12));
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 64);
    v_rsi = (((unsigned __int8)(a2)) != 4) ? 1 : 0;
    a1 = ((unsigned __int8)(a2) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_002951A4;
    if (((unsigned __int8)(a2)) != 8) goto loc_002955B3;
    goto loc_002952FD;
loc_002951A4:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62)) & (12));
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) | (4));
    if (((unsigned __int8)(result)) != 4) { v_rbp = (unsigned int)((unsigned int)(a2)); }
    v_stack_m60 = (unsigned int)(v_rbp);
    result = MiInitializePrototypePtes(result, (unsigned int)(0xC000000DULL), a1, (unsigned int)((unsigned int)(v_rsi)));
    result = 0;
    if (v_stack_m50 == 0) goto loc_0029539D;
loc_002951E0:
    v_rbx = ((unsigned int)(a2)) | (-1);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) & (128));
    v_stack_m64 = (unsigned int)(result);
    if ((((unsigned __int8)(v_rbp)) & (4)) == 0) goto loc_00295367;
    v_stack_p8 = (unsigned int)(v_rbx + 2);
loc_00295203:
    v_r12 = 0;
    v_stack_p20 = 0;
    if (((unsigned int)(v_rbx + 2)) == 2) goto loc_0029557D;
    v_stack_p20 = 0;
loc_00295222:
    if (v_stack_m50 == 0) goto loc_002953B9;
loc_0029522B:
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(a1) + 72, (unsigned int)(0xC000000DULL), a1, (unsigned int)((unsigned int)(v_rsi)));
    if (((unsigned int)((unsigned int)(v_stack_p8))) == 2) goto loc_00295503;
loc_0029524A:
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m64)))) | (32));
    if (((unsigned int)((unsigned int)(v_stack_p8))) == 2) goto loc_0029561A;
loc_0029525C:
    v_rdi = 0;
    if ((*(unsigned __int64 *)(a1 + 8)) != 0) goto loc_002954EE;
    result = MiIncrementSubsectionViewCount(a1, (unsigned int)((unsigned int)(v_rbp)), a1, (unsigned int)((unsigned int)(v_rsi)));
    v_stack_m5C = (unsigned int)(result);
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi + 1))) goto loc_0029534D;
    v_rsi = 0;
    if (((unsigned int)(result)) == 3) { v_rsi = 0; }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62)) & (12)) != 0) goto loc_0029547B;
loc_00295297:
    if (v_stack_m50 != 0) {
        result = *(unsigned int *)(a1 + 32);
        result = (unsigned int)((result) | ((unsigned int)(v_rdi + 1)));
        *(unsigned int *)(a1 + 32) = (unsigned int)(result);
    }
    if (0 != 0) goto loc_002952BA;
    if ((*(unsigned __int64 *)(a1 + 8)) != 0) goto loc_00295624;
loc_002952BA:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62)) & (12)) == 0) goto loc_00295322;
loc_002952C1:
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(a1) + 72, (unsigned __int8)((unsigned __int8)(result)), v_rdi + 1, (unsigned int)((unsigned int)(v_rsi)));
    v_stack_m68 = 0;
loc_002952D3:
    a1 = 0;
loc_002952D5:
    if (v_stack_m50 == 0) goto loc_0029541D;
loc_002952E3:
    v_rbx = 0;
    if (v_stack_m68 != 0) goto loc_00295649;
loc_002952EF:
    if (v_rsi != 0) goto loc_00295658;
loc_002952F8:
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, v_rdi + 1, (unsigned int)((unsigned int)(v_rsi)));
    }
loc_00295309:
    v_rsp = (v_rsp) + (96);
    return 0;
loc_00295322:
    *(unsigned __int64 *)(a1 + 8) = v_stack_p40;
    result = -(a1);
    a1 = (unsigned int)((a1) & (64));
    a1 = (a1) + (56);
    a1 = (a1) + (a1);
    result = MiUpdateSystemProtoPtesTree(a1, 3, v_rdi + 1, (unsigned int)((unsigned int)(v_rsi)));
    goto loc_002952C1;
loc_0029534D:
    result = MiReleaseSpinLockExclusive(0, (unsigned __int8)(v_stack_m50), v_rdi + 1, (unsigned int)((unsigned int)(v_rsi)));
loc_0029535D:
    goto loc_002952D3;
loc_00295367:
    result = (unsigned int)(-(result));
    a2 = (unsigned int)(((unsigned __int8)(v_stack_m50)) & (2));
    result = MiControlAreaRequiresCharge(*(unsigned __int64 *)(a1), a2, v_rdi + 1, (unsigned int)((unsigned int)(v_rsi)));
    a1 = 0;
    v_stack_pA0 = (unsigned int)(result);
    if ((unsigned int)(result) != 0) goto loc_00295203;
    goto loc_002952D5;
loc_00295393:
    goto loc_00295309;
loc_0029539D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 64)) != ((unsigned int)(0xC000009AULL))) goto loc_00295411;
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 120)) & ((unsigned int)(0xC000009AULL));
    goto loc_002951E0;
loc_002953B9:
    a3 = 0;
    v_stack_pB8 = 1;
    a2 = 0;
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1))) + (40);
    result = KeAbPreAcquire(v_rdi, a2, a3, (unsigned int)((unsigned int)(v_rsi)));
    if (!(condition_is_above_or_equal)) {
        a3 = v_rdi;
        a2 = result;
        a1 = v_rdi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned int)((unsigned int)(v_rsi)));
    }
    if (result == 0) goto loc_0029522B;
    *(unsigned __int8 *)(result + 10) = 1;
    goto loc_0029522B;
loc_00295411:
    goto loc_002951E0;
loc_0029541D:
    if (v_stack_pB8 == ((unsigned int)(a1))) goto loc_002952E3;
    v_rbx = (unsigned __int8)((v_stack_p10) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_002955A5;
loc_0029543F:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 40, a2, a3, (unsigned int)((unsigned int)(v_rsi)));
    if (((unsigned __int8)(v_rbx)) != 2) goto loc_002952E3;
    if ((*(unsigned __int64 *)(v_stack_p50 + 152)) == (v_stack_p50 + 152)) goto loc_002952E3;
    result = KiCheckForKernelApcDelivery(v_stack_p50, 1, a3, (unsigned int)((unsigned int)(v_rsi)));
    goto loc_002952E3;
loc_0029547B:
    v_stack_p34 = a3;
    result = MiReleaseSpinLockExclusive(v_stack_p40, (unsigned __int8)(v_stack_m50), a3, (unsigned int)((unsigned int)(v_rsi)));
    a2 = 0;
    result = (unsigned int)(((unsigned int)(v_stack_p38)) & (512));
    result = (unsigned int)((result) | (40));
    result = (unsigned int)((result) >> (3));
    v_stack_p20 = (unsigned int)(result);
    result = MiAllocateFileExtents(a1, a2, v_stack_p40, (unsigned int)(v_stack_pB0));
    a1 = 0;
    if (sign_flag) goto loc_0029563F;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62)) & (12));
    if (((unsigned __int8)(result)) == 4) goto loc_00295307;
    result = ExAcquireSpinLockExclusive(v_stack_p40, a2, v_stack_p40, (unsigned int)(v_stack_pB0));
    v_rdi = 0;
    goto loc_00295297;
loc_002954EE:
    result = MiReleaseSpinLockExclusive(v_stack_p40, (unsigned __int8)((unsigned __int8)(result)), v_rdi + 1, (unsigned int)(v_stack_pB0));
    goto loc_0029535D;
loc_00295503:
    if ((unsigned int)(0xC000020AULL) == 0) goto loc_002955D0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 52))) & ((unsigned int)((unsigned int)(0x3FFFFFFFULL))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 44))) - ((unsigned int)(a1)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 16)) == result) goto loc_0029524A;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 52))) & ((unsigned int)((unsigned int)(0x3FFFFFFFULL))));
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 44))) - ((unsigned int)(a1)));
loc_00295537:
    result = MiReleaseSpinLockExclusive(v_stack_p40, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)(0x3FFFFFFFULL), (unsigned int)(v_stack_pB0));
    v_r12 = 0;
    if ((unsigned int)(0xC000020AULL) == 0) goto loc_002955F3;
    if ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 16)))) != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 60);
        a1 = *(unsigned __int64 *)(v_rip + 12167970);
        a2 = 0;
        a2 = ((unsigned int)(0xC000020AULL) != 0) ? 1 : 0;
        a3 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 16))));
        result = (unsigned int)((result) & (0x3FFULL));
        a1 = *(unsigned __int64 *)(a1 + result * 8);
        result = MiReturnCrossPartitionSectionCharges(a1, a2, a3, (unsigned int)(v_stack_pB0));
    }
    if (v_rsi == 0) goto loc_00295222;
    result = MiGetSubsectionCharges(a1, v_rsi, a3, (unsigned int)(v_stack_pB0));
    goto loc_00295222;
loc_002955A5:
    result = ExfTryToWakePushLock((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 16))) + 40, v_rsi, a3, (unsigned int)(v_stack_pB0));
    goto loc_0029543F;
loc_002955B3:
    result = MiChargeLargeProtoSubsection(a1, (unsigned int)(a3), a3, (unsigned int)(v_stack_pB0));
    goto loc_002952FD;
loc_002955D0:
    result = MiGetCommittedPages(*(unsigned __int64 *)(a1), (unsigned int)(a3), a3, (unsigned int)(v_stack_pB0));
    if (v_rsi == result) goto loc_0029524A;
    result = MiGetCommittedPages(*(unsigned __int64 *)(a1), (unsigned int)(a3), a3, (unsigned int)(v_stack_pB0));
    goto loc_00295537;
loc_002955F3:
    a2 = (unsigned __int8)((v_rbx) & (6));
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 40, a2, a3, (unsigned int)(v_stack_pB0));
loc_0029561A:
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(result))) | (40));
    goto loc_0029525C;
loc_00295624:
    v_rbp = (unsigned int)((v_rbp) | (16));
loc_0029563F:
    goto loc_002952D5;
loc_00295649:
    a2 = 0;
    result = MiChargeLargeProtoSubsection(a1, a2, a3, (unsigned int)(v_stack_pB0));
    goto loc_002952EF;
loc_00295658:
    a2 = (v_stack_p50 != 0) ? 1 : 0;
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 60)) & (0x3FFULL));
    result = MiReturnCrossPartitionSectionCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12167713) + result * 8), a2, result, (unsigned int)(v_stack_pB0));
    goto loc_002952F8;
}
```

## 5. (Beta) C Style

```c
int64_t MiCreatePrototypePtes(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint32_t v_stack_p8;
    uint32_t v_stack_pA0;
    uint32_t v_stack_pB0;
    uint32_t v_stack_pB8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (96);
    local_rbp = 0;
    v_stack_m68 = 0;
    v_stack_p20 = 0;
    v_stack_m48 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = MiAllocatePool(274, (uint32_t)(Arg4) * 8, (uint32_t)(0x74536D4DULL), Arg4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00295393;
    Arg2 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E)) & (12));
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(arg1) + 0x40);
    local_rsi = (((uint8_t)(Arg2)) != 4) ? 1 : 0;
    Arg1 = ((uint8_t)(Arg2) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_002951A4;
    if (((uint8_t)(Arg2)) != 8) goto loc_002955B3;
    goto loc_002952FD;
loc_002951A4:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E)) & (12));
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) | (4));
    if (((uint8_t)(result)) != 4) { local_rbp = (uint32_t)((uint32_t)(Arg2)); }
    v_stack_m60 = (uint32_t)(local_rbp);
    result = MiInitializePrototypePtes(result, (uint32_t)(0xC000000DULL), Arg1, (uint32_t)((uint32_t)(local_rsi)));
    result = 0;
    if (v_stack_m50 == 0) goto loc_0029539D;
loc_002951E0:
    local_rbx = ((uint32_t)(Arg2)) | (-1);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) & (128));
    v_stack_m64 = (uint32_t)(result);
    if ((((uint8_t)(local_rbp)) & (4)) == 0) goto loc_00295367;
    v_stack_p8 = (uint32_t)(local_rbx + 2);
loc_00295203:
    local_r12 = 0;
    v_stack_p20 = 0;
    if (((uint32_t)(local_rbx + 2)) == 2) goto loc_0029557D;
    v_stack_p20 = 0;
loc_00295222:
    if (v_stack_m50 == 0) goto loc_002953B9;
loc_0029522B:
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(arg1) + 72, (uint32_t)(0xC000000DULL), Arg1, (uint32_t)((uint32_t)(local_rsi)));
    if (((uint32_t)((uint32_t)(v_stack_p8))) == 2) goto loc_00295503;
loc_0029524A:
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m64)))) | (32));
    if (((uint32_t)((uint32_t)(v_stack_p8))) == 2) goto loc_0029561A;
loc_0029525C:
    local_rdi = 0;
    if ((*(uint64_t *)(arg1 + 0x8)) != 0) goto loc_002954EE;
    result = MiIncrementSubsectionViewCount(Arg1, (uint32_t)((uint32_t)(local_rbp)), Arg1, (uint32_t)((uint32_t)(local_rsi)));
    v_stack_m5C = (uint32_t)(result);
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi + 1))) goto loc_0029534D;
    local_rsi = 0;
    if (((uint32_t)(result)) == 3) { local_rsi = 0; }
    if (((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E)) & (12)) != 0) goto loc_0029547B;
loc_00295297:
    if (v_stack_m50 != 0) {
        result = *(uint32_t *)(arg1 + 0x20);
        result = (uint32_t)((result) | ((uint32_t)(local_rdi + 1)));
        *(uint32_t *)(arg1 + 0x20) = (uint32_t)(result);
    }
    if (0 != 0) goto loc_002952BA;
    if ((*(uint64_t *)(arg1 + 0x8)) != 0) goto loc_00295624;
loc_002952BA:
    if (((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E)) & (12)) == 0) goto loc_00295322;
loc_002952C1:
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(arg1) + 72, (uint8_t)((uint8_t)(result)), local_rdi + 1, (uint32_t)((uint32_t)(local_rsi)));
    v_stack_m68 = 0;
loc_002952D3:
    Arg1 = 0;
loc_002952D5:
    if (v_stack_m50 == 0) goto loc_0029541D;
loc_002952E3:
    local_rbx = 0;
    if (v_stack_m68 != 0) goto loc_00295649;
loc_002952EF:
    if (local_rsi != 0) goto loc_00295658;
loc_002952F8:
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, local_rdi + 1, (uint32_t)((uint32_t)(local_rsi)));
    }
loc_00295309:
    local_rsp = (local_rsp) + (96);
    return 0;
loc_00295322:
    *(uint64_t *)(arg1 + 0x8) = v_stack_p40;
    result = -(Arg1);
    Arg1 = (uint32_t)((Arg1) & (64));
    Arg1 = (Arg1) + (56);
    Arg1 = (Arg1) + (Arg1);
    result = MiUpdateSystemProtoPtesTree(Arg1, 3, local_rdi + 1, (uint32_t)((uint32_t)(local_rsi)));
    goto loc_002952C1;
loc_0029534D:
    result = MiReleaseSpinLockExclusive(0, (uint8_t)(v_stack_m50), local_rdi + 1, (uint32_t)((uint32_t)(local_rsi)));
loc_0029535D:
    goto loc_002952D3;
loc_00295367:
    result = (uint32_t)(-(result));
    Arg2 = (uint32_t)(((uint8_t)(v_stack_m50)) & (2));
    result = MiControlAreaRequiresCharge(*(uint64_t *)(arg1), Arg2, local_rdi + 1, (uint32_t)((uint32_t)(local_rsi)));
    Arg1 = 0;
    v_stack_pA0 = (uint32_t)(result);
    if ((uint32_t)(result) != 0) goto loc_00295203;
    goto loc_002952D5;
loc_00295393:
    goto loc_00295309;
loc_0029539D:
    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x40)) != ((uint32_t)(0xC000009AULL))) goto loc_00295411;
    local_rsi = (*(uint64_t *)(*(uint64_t *)(arg1) + 0x78)) & ((uint32_t)(0xC000009AULL));
    goto loc_002951E0;
loc_002953B9:
    Arg3 = 0;
    v_stack_pB8 = 1;
    Arg2 = 0;
    local_rdi = (*(uint64_t *)(*(uint64_t *)(arg1))) + (40);
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, (uint32_t)((uint32_t)(local_rsi)));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rdi;
        Arg2 = result;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(local_rsi)));
    }
    if (result == 0) goto loc_0029522B;
    *(uint8_t *)(result + 0xA) = 1;
    goto loc_0029522B;
loc_00295411:
    goto loc_002951E0;
loc_0029541D:
    if (v_stack_pB8 == ((uint32_t)(Arg1))) goto loc_002952E3;
    local_rbx = (uint8_t)((v_stack_p10) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_002955A5;
loc_0029543F:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(arg1)) + 40, Arg2, Arg3, (uint32_t)((uint32_t)(local_rsi)));
    if (((uint8_t)(local_rbx)) != 2) goto loc_002952E3;
    if ((*(uint64_t *)(v_stack_p50 + 0x98)) == (v_stack_p50 + 152)) goto loc_002952E3;
    result = KiCheckForKernelApcDelivery(v_stack_p50, 1, Arg3, (uint32_t)((uint32_t)(local_rsi)));
    goto loc_002952E3;
loc_0029547B:
    v_stack_p34 = Arg3;
    result = MiReleaseSpinLockExclusive(v_stack_p40, (uint8_t)(v_stack_m50), Arg3, (uint32_t)((uint32_t)(local_rsi)));
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)(v_stack_p38)) & (512));
    result = (uint32_t)((result) | (40));
    result = (uint32_t)((result) >> (3));
    v_stack_p20 = (uint32_t)(result);
    result = MiAllocateFileExtents(Arg1, Arg2, v_stack_p40, (uint32_t)(v_stack_pB0));
    Arg1 = 0;
    if (sign_flag) goto loc_0029563F;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E)) & (12));
    if (((uint8_t)(result)) == 4) goto loc_00295307;
    result = ExAcquireSpinLockExclusive(v_stack_p40, Arg2, v_stack_p40, (uint32_t)(v_stack_pB0));
    local_rdi = 0;
    goto loc_00295297;
loc_002954EE:
    result = MiReleaseSpinLockExclusive(v_stack_p40, (uint8_t)((uint8_t)(result)), local_rdi + 1, (uint32_t)(v_stack_pB0));
    goto loc_0029535D;
loc_00295503:
    if ((uint32_t)(0xC000020AULL) == 0) goto loc_002955D0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x34))) & ((uint32_t)((uint32_t)(0x3FFFFFFFULL))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x2C))) - ((uint32_t)(Arg1)));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1)) + 0x10)) == result) goto loc_0029524A;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x34))) & ((uint32_t)((uint32_t)(0x3FFFFFFFULL))));
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x2C))) - ((uint32_t)(Arg1)));
loc_00295537:
    result = MiReleaseSpinLockExclusive(v_stack_p40, (uint8_t)((uint8_t)(result)), (uint32_t)(0x3FFFFFFFULL), (uint32_t)(v_stack_pB0));
    local_r12 = 0;
    if ((uint32_t)(0xC000020AULL) == 0) goto loc_002955F3;
    if ((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1)) + 0x10)))) != 0) {
        result = *(uint16_t *)(*(uint64_t *)(arg1) + 0x3C);
        Arg1 = *(uint64_t *)(v_rip + 0xB9AB22);
        Arg2 = 0;
        Arg2 = ((uint32_t)(0xC000020AULL) != 0) ? 1 : 0;
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1)) + 0x10))));
        result = (uint32_t)((result) & (0x3FFULL));
        Arg1 = *(uint64_t *)(arg1 + result * 8);
        result = MiReturnCrossPartitionSectionCharges(Arg1, Arg2, Arg3, (uint32_t)(v_stack_pB0));
    }
    if (local_rsi == 0) goto loc_00295222;
    result = MiGetSubsectionCharges(Arg1, local_rsi, Arg3, (uint32_t)(v_stack_pB0));
    goto loc_00295222;
loc_002955A5:
    result = ExfTryToWakePushLock((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1)) + 0x10))) + 40, local_rsi, Arg3, (uint32_t)(v_stack_pB0));
    goto loc_0029543F;
loc_002955B3:
    result = MiChargeLargeProtoSubsection(Arg1, (uint32_t)(Arg3), Arg3, (uint32_t)(v_stack_pB0));
    goto loc_002952FD;
loc_002955D0:
    result = MiGetCommittedPages(*(uint64_t *)(arg1), (uint32_t)(Arg3), Arg3, (uint32_t)(v_stack_pB0));
    if (local_rsi == result) goto loc_0029524A;
    result = MiGetCommittedPages(*(uint64_t *)(arg1), (uint32_t)(Arg3), Arg3, (uint32_t)(v_stack_pB0));
    goto loc_00295537;
loc_002955F3:
    Arg2 = (uint8_t)((local_rbx) & (6));
    result = ExfTryToWakePushLock(*(uint64_t *)(*(uint64_t *)(arg1)) + 40, Arg2, Arg3, (uint32_t)(v_stack_pB0));
loc_0029561A:
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(result))) | (40));
    goto loc_0029525C;
loc_00295624:
    local_rbp = (uint32_t)((local_rbp) | (16));
loc_0029563F:
    goto loc_002952D5;
loc_00295649:
    Arg2 = 0;
    result = MiChargeLargeProtoSubsection(Arg1, Arg2, Arg3, (uint32_t)(v_stack_pB0));
    goto loc_002952EF;
loc_00295658:
    Arg2 = (v_stack_p50 != 0) ? 1 : 0;
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1) + 0x3C)) & (0x3FFULL));
    result = MiReturnCrossPartitionSectionCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB9AA21) + result * 8), Arg2, result, (uint32_t)(v_stack_pB0));
    goto loc_002952F8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x34` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002950FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
