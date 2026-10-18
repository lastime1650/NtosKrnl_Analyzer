# MiZeroCfgSystemWideBitmapWorker

- RVA: `0x00367060`–`0x003677C4` (길이 `1,892` bytes)
- VA: `0x0000000140367060`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00079FBC`
- 디코드: `471`개 명령, `1,892/1,892` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x003670D9` → [MiLocatePagefileSubsection](MiLocatePagefileSubsection_function_00367AC0.md) (function, `0x00367AC0`)
- `0x00367105` → [MiLocatePagefileSubsection](MiLocatePagefileSubsection_function_00367AC0.md) (function, `0x00367AC0`)
- `0x0036719C` → [MiLockLeafPage](MiLockLeafPage_function_003658C0.md) (function, `0x003658C0`)
- `0x0036721F` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x00367263` → [MiTransferSoftwarePte](../38/MiTransferSoftwarePte_function_003821F0.md) (function, `0x003821F0`)
- `0x003672A6` → [MiDecrementShareCountEx](../33/MiDecrementShareCountEx_function_00333F70.md) (function, `0x00333F70`)
- `0x003672C2` → [MiInsertPageInFreeOrZeroedList](../33/MiInsertPageInFreeOrZeroedList_function_00334D20.md) (function, `0x00334D20`)
- `0x003672F0` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x0036733F` → [MiTransferSoftwarePte](../38/MiTransferSoftwarePte_function_003821F0.md) (function, `0x003821F0`)
- `0x00367351` → [MiReleasePageFileSpace](../28/MiReleasePageFileSpace_function_00285980.md) (function, `0x00285980`)
- `0x0036738D` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x003673C0` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x003673E4` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0036742C` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x0036746D` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00367481` → [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) (function, `0x002B8B80`)
- `0x003674B6` → [KeZeroSinglePage](../6B/KeZeroSinglePage_function_006BA030.md) (function, `0x006BA030`)
- `0x003674C5` → [MiDiscardTransitionPteEx](../37/MiDiscardTransitionPteEx_function_00375954.md) (function, `0x00375954`)
- `0x003674F7` → [MiDetermineModifiedPageListHead](../2B/MiDetermineModifiedPageListHead_function_002BAB00.md) (function, `0x002BAB00`)
- `0x00367503` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x00367513` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x00367537` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003675CA` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x003675E4` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x00367642` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x00367659` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x00367669` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x0036772A` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0036773A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- [MiZeroCfgSystemWideBitmap](MiZeroCfgSystemWideBitmap_function_003677CC.md) at `0x003677FC`

### Static image references
- `0x003670AB` → RVA `0x00E30088` (`.data`; read)
- `0x003671C7` → RVA `0x00E2DC80` (`.data`; read)
- `0x0036735E` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00367422` → RVA `0x00010880` (`.rdata`; read)
- `0x00367581` → RVA `0x00E3014C` (`.data`; read)
- `0x0036758A` → RVA `0x00E301A8` (`.data`; read)
- `0x0036771C` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00367602` → [sub_006E3560](../6E/Unknown_function_006E3560.md) (`tail-transfer`)
  - `0x00367620` → [sub_006E3560 + 0x8](../6E/Unknown_function_006E3560.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00367060  40 55                           push rbp
00367062  53                              push rbx
00367063  56                              push rsi
00367064  57                              push rdi
00367065  41 54                           push r12
00367067  41 55                           push r13
00367069  41 56                           push r14
0036706B  41 57                           push r15
0036706D  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00367072  48 81 EC 98 00 00 00            sub rsp, 0x98
00367079  48 8B 01                        mov rax, qword ptr [rcx]
0036707C  48 8B DA                        mov rbx, rdx
0036707F  48 C1 EB 03                     shr rbx, 3
00367083  48 8D 55 EF                     lea rdx, [rbp - 0x11]
00367087  49 C1 E8 03                     shr r8, 3
0036708B  48 8B F9                        mov rdi, rcx
0036708E  B9 FF 0F 00 00                  mov ecx, 0xfff
00367093  44 8B FB                        mov r15d, ebx
00367096  44 0F B7 48 3C                  movzx r9d, word ptr [rax + 0x3c]
0036709B  44 23 F9                        and r15d, ecx
0036709E  B8 FF 03 00 00                  mov eax, 0x3ff
003670A3  44 89 7D 77                     mov dword ptr [rbp + 0x77], r15d
003670A7  66 44 23 C8                     and r9w, ax
003670AB  48 8B 05 D6 8F AC 00            mov rax, qword ptr [rip + 0xac8fd6]
003670B2  45 0F B7 C9                     movzx r9d, r9w
003670B6  4A 8B 04 C8                     mov rax, qword ptr [rax + r9*8]
003670BA  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
003670BE  41 8D 04 18                     lea eax, [r8 + rbx]
003670C2  23 C1                           and eax, ecx
003670C4  48 8B CF                        mov rcx, rdi
003670C7  89 45 6F                        mov dword ptr [rbp + 0x6f], eax
003670CA  49 8D 40 FF                     lea rax, [r8 - 1]
003670CE  48 03 C3                        add rax, rbx
003670D1  48 C1 E8 0C                     shr rax, 0xc
003670D5  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
003670D9  E8 E2 09 00 00                  call 0x140367ac0
003670DE  4C 8B E0                        mov r12, rax
003670E1  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
003670E5  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
003670E9  48 8D 55 D7                     lea rdx, [rbp - 0x29]
003670ED  48 C1 EB 0C                     shr rbx, 0xc
003670F1  48 89 45 F7                     mov qword ptr [rbp - 9], rax
003670F5  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
003670FA  48 89 5D D7                     mov qword ptr [rbp - 0x29], rbx
003670FE  4C 8D 34 C1                     lea r14, [rcx + rax*8]
00367102  48 8B CF                        mov rcx, rdi
00367105  E8 B6 09 00 00                  call 0x140367ac0
0036710A  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
0036710E  4C 8B E8                        mov r13, rax
00367111  45 33 DB                        xor r11d, r11d
00367114  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00367118  48 85 C9                        test rcx, rcx
0036711B  0F 84 04 05 00 00               je 0x140367625
00367121  48 8D 34 D1                     lea rsi, [rcx + rdx*8]
00367125  4D 3B EC                        cmp r13, r12
00367128  0F 85 7D 06 00 00               jne 0x1403677ab
0036712E  49 8B D6                        mov rdx, r14
00367131  44 8B 45 6F                     mov r8d, dword ptr [rbp + 0x6f]
00367135  41 8B C7                        mov eax, r15d
00367138  F7 D8                           neg eax
0036713A  48 89 55 A7                     mov qword ptr [rbp - 0x59], rdx
0036713E  49 8B CB                        mov rcx, r11
00367141  C6 45 67 11                     mov byte ptr [rbp + 0x67], 0x11
00367145  48 1B C0                        sbb rax, rax
00367148  48 89 4D CF                     mov qword ptr [rbp - 0x31], rcx
0036714C  48 23 C6                        and rax, rsi
0036714F  4C 89 5D B7                     mov qword ptr [rbp - 0x49], r11
00367153  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
00367157  49 8B FB                        mov rdi, r11
0036715A  41 8B C0                        mov eax, r8d
0036715D  F7 D8                           neg eax
0036715F  4D 1B FF                        sbb r15, r15
00367162  4D 23 FE                        and r15, r14
00367165  4C 89 7D BF                     mov qword ptr [rbp - 0x41], r15
00367169  48 3B F2                        cmp rsi, rdx
0036716C  0F 83 0A 02 00 00               jae 0x14036737c
00367172  48 8B DE                        mov rbx, rsi
00367175  48 8B C7                        mov rax, rdi
00367178  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
0036717F  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
00367185  48 3B C3                        cmp rax, rbx
00367188  0F 85 11 03 00 00               jne 0x14036749f
0036718E  48 85 C9                        test rcx, rcx
00367191  0F 84 E3 02 00 00               je 0x14036747a
00367197  33 D2                           xor edx, edx
00367199  48 8B CE                        mov rcx, rsi
0036719C  E8 1F E7 FF FF                  call 0x1403658c0
003671A1  48 8B 3E                        mov rdi, qword ptr [rsi]
003671A4  4C 8B F0                        mov r14, rax
003671A7  40 F6 C7 01                     test dil, 1
003671AB  0F 85 F6 01 00 00               jne 0x1403673a7
003671B1  48 0F BA E7 0A                  bt rdi, 0xa
003671B6  0F 82 39 01 00 00               jb 0x1403672f5
003671BC  48 0F BA E7 0B                  bt rdi, 0xb
003671C1  0F 83 50 01 00 00               jae 0x140367317
003671C7  48 8B 05 B2 6A AC 00            mov rax, qword ptr [rip + 0xac6ab2]
003671CE  45 33 DB                        xor r11d, r11d
003671D1  48 85 C0                        test rax, rax
003671D4  74 10                           je 0x1403671e6
003671D6  40 F6 C7 10                     test dil, 0x10
003671DA  0F 85 2E 01 00 00               jne 0x14036730e
003671E0  48 F7 D0                        not rax
003671E3  48 23 F8                        and rdi, rax
003671E6  48 C1 EF 0C                     shr rdi, 0xc
003671EA  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
003671F4  48 23 F8                        and rdi, rax
003671F7  49 8B DB                        mov rbx, r11
003671FA  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
003671FE  66 85 C0                        test ax, ax
00367201  0F 85 C8 00 00 00               jne 0x1403672cf
00367207  48 3B 75 C7                     cmp rsi, qword ptr [rbp - 0x39]
0036720B  0F 84 CD 02 00 00               je 0x1403674de
00367211  49 3B F7                        cmp rsi, r15
00367214  0F 84 C4 02 00 00               je 0x1403674de
0036721A  33 D2                           xor edx, edx
0036721C  49 8B CE                        mov rcx, r14
0036721F  E8 6C 03 F2 FF                  call 0x140287590
00367224  A8 03                           test al, 3
00367226  0F 85 94 02 00 00               jne 0x1403674c0
0036722C  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00367230  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00367234  C0 E8 02                        shr al, 2
00367237  A8 01                           test al, 1
00367239  0F 85 FF 03 00 00               jne 0x14036763e
0036723F  48 89 5D DF                     mov qword ptr [rbp - 0x21], rbx
00367243  4D 8B 46 10                     mov r8, qword ptr [r14 + 0x10]
00367247  45 33 E4                        xor r12d, r12d
0036724A  41 8A C0                        mov al, r8b
0036724D  D0 E8                           shr al, 1
0036724F  A8 01                           test al, 1
00367251  0F 85 24 04 00 00               jne 0x14036767b
00367257  45 33 C9                        xor r9d, r9d
0036725A  45 33 C0                        xor r8d, r8d
0036725D  33 D2                           xor edx, edx
0036725F  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00367263  E8 88 AF 01 00                  call 0x1403821f0
00367268  4C 8B C8                        mov r9, rax
0036726B  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00367275  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00367279  48 23 C1                        and rax, rcx
0036727C  4C 8D 3C 40                     lea r15, [rax + rax*2]
00367280  49 C1 E7 04                     shl r15, 4
00367284  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0036728E  4C 03 F8                        add r15, rax
00367291  4C 89 0E                        mov qword ptr [rsi], r9
00367294  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
0036729B  0F 82 BA 00 00 00               jb 0x14036735b
003672A1  33 D2                           xor edx, edx
003672A3  49 8B CF                        mov rcx, r15
003672A6  E8 C5 CC FC FF                  call 0x140333f70
003672AB  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003672B5  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
003672BA  BA 02 00 00 00                  mov edx, 2
003672BF  48 8B CF                        mov rcx, rdi
003672C2  E8 59 DA FC FF                  call 0x140334d20
003672C7  4C 8B 7D BF                     mov r15, qword ptr [rbp - 0x41]
003672CB  4C 8B 65 E7                     mov r12, qword ptr [rbp - 0x19]
003672CF  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003672D9  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
003672DE  48 85 DB                        test rbx, rbx
003672E1  74 12                           je 0x1403672f5
003672E3  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
003672E7  48 8B D3                        mov rdx, rbx
003672EA  41 B8 01 00 00 00               mov r8d, 1
003672F0  E8 DB CC F1 FF                  call 0x140283fd0
003672F5  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
003672F9  48 83 C6 08                     add rsi, 8
003672FD  48 8B 7D B7                     mov rdi, qword ptr [rbp - 0x49]
00367301  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00367305  44 8B 45 6F                     mov r8d, dword ptr [rbp + 0x6f]
00367309  E9 5B FE FF FF                  jmp 0x140367169
0036730E  48 83 E7 EF                     and rdi, 0xffffffffffffffef
00367312  E9 CF FE FF FF                  jmp 0x1403671e6
00367317  48 85 FF                        test rdi, rdi
0036731A  74 D9                           je 0x1403672f5
0036731C  48 3B 75 C7                     cmp rsi, qword ptr [rbp - 0x39]
00367320  74 D3                           je 0x1403672f5
00367322  49 3B F7                        cmp rsi, r15
00367325  74 CE                           je 0x1403672f5
00367327  40 8A C7                        mov al, dil
0036732A  D0 E8                           shr al, 1
0036732C  A8 01                           test al, 1
0036732E  0F 85 84 03 00 00               jne 0x1403676b8
00367334  45 33 C9                        xor r9d, r9d
00367337  45 33 C0                        xor r8d, r8d
0036733A  33 D2                           xor edx, edx
0036733C  48 8B CF                        mov rcx, rdi
0036733F  E8 AC AE 01 00                  call 0x1403821f0
00367344  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
00367348  45 33 C0                        xor r8d, r8d
0036734B  48 8B D7                        mov rdx, rdi
0036734E  48 8B D8                        mov rbx, rax
00367351  E8 2A E6 F1 FF                  call 0x140285980
00367356  48 89 1E                        mov qword ptr [rsi], rbx
00367359  EB 9A                           jmp 0x1403672f5
0036735B  41 FF C4                        inc r12d
0036735E  44 85 25 47 DF C5 00            test dword ptr [rip + 0xc5df47], r12d
00367365  0F 84 B1 03 00 00               je 0x14036771c
0036736B  F3 90                           pause
0036736D  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00367371  48 85 C0                        test rax, rax
00367374  0F 89 1A FF FF FF               jns 0x140367294
0036737A  EB DF                           jmp 0x14036735b
0036737C  4D 3B EC                        cmp r13, r12
0036737F  0F 85 69 02 00 00               jne 0x1403675ee
00367385  48 85 C9                        test rcx, rcx
00367388  74 08                           je 0x140367392
0036738A  8A 55 67                        mov dl, byte ptr [rbp + 0x67]
0036738D  E8 FE EC ED FF                  call 0x140246090
00367392  48 81 C4 98 00 00 00            add rsp, 0x98
00367399  41 5F                           pop r15
0036739B  41 5E                           pop r14
0036739D  41 5D                           pop r13
0036739F  41 5C                           pop r12
003673A1  5F                              pop rdi
003673A2  5E                              pop rsi
003673A3  5B                              pop rbx
003673A4  5D                              pop rbp
003673A5  C3                              ret
003673A6  CC                              int3
003673A7  48 C1 EF 0C                     shr rdi, 0xc
003673AB  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
003673B5  48 23 CF                        and rcx, rdi
003673B8  33 D2                           xor edx, edx
003673BA  41 B8 00 00 00 80               mov r8d, 0x80000000
003673C0  E8 4B B7 FC FF                  call 0x140332b10
003673C5  48 8B D8                        mov rbx, rax
003673C8  48 3B 75 C7                     cmp rsi, qword ptr [rbp - 0x39]
003673CC  0F 85 D8 00 00 00               jne 0x1403674aa
003673D2  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
003673D5  41 B8 00 10 00 00               mov r8d, 0x1000
003673DB  44 2B C0                        sub r8d, eax
003673DE  48 8D 0C 03                     lea rcx, [rbx + rax]
003673E2  33 D2                           xor edx, edx
003673E4  E8 57 F8 35 00                  call 0x1406c6c40
003673E9  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003673F3  48 C1 EB 09                     shr rbx, 9
003673F7  48 23 D8                        and rbx, rax
003673FA  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00367404  48 8B C0                        mov rax, rax
00367407  48 03 D8                        add rbx, rax
0036740A  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00367413  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
0036741A  33 C0                           xor eax, eax
0036741C  48 89 01                        mov qword ptr [rcx], rax
0036741F  49 8B CE                        mov rcx, r14
00367422  48 8B 05 57 94 CA FF            mov rax, qword ptr [rip - 0x356ba9]
00367429  48 89 03                        mov qword ptr [rbx], rax
0036742C  E8 9F 99 00 00                  call 0x140370dd0
00367431  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
0036743B  F0 49 21 4E 18                  lock and qword ptr [r14 + 0x18], rcx
00367440  48 85 C0                        test rax, rax
00367443  0F 84 AC FE FF FF               je 0x1403672f5
00367449  49 8B 4E 28                     mov rcx, qword ptr [r14 + 0x28]
0036744D  48 8B D0                        mov rdx, rax
00367450  48 8B 05 31 8C AC 00            mov rax, qword ptr [rip + 0xac8c31]
00367457  48 C1 E9 2B                     shr rcx, 0x2b
0036745B  81 E1 FF 03 00 00               and ecx, 0x3ff
00367461  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
00367465  E9 80 FE FF FF                  jmp 0x1403672ea
0036746A  8A 55 67                        mov dl, byte ptr [rbp + 0x67]
0036746D  E8 1E EC ED FF                  call 0x140246090
00367472  33 C0                           xor eax, eax
00367474  8B F8                           mov edi, eax
00367476  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0036747A  48 8D 55 67                     lea rdx, [rbp + 0x67]
0036747E  48 8B CE                        mov rcx, rsi
00367481  E8 FA 16 F5 FF                  call 0x1402b8b80
00367486  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
0036748A  48 8B C8                        mov rcx, rax
0036748D  48 85 C0                        test rax, rax
00367490  0F 84 22 03 00 00               je 0x1403677b8
00367496  48 89 75 B7                     mov qword ptr [rbp - 0x49], rsi
0036749A  E9 F8 FC FF FF                  jmp 0x140367197
0036749F  48 85 FF                        test rdi, rdi
003674A2  0F 84 E6 FC FF FF               je 0x14036718e
003674A8  EB C0                           jmp 0x14036746a
003674AA  48 8B CB                        mov rcx, rbx
003674AD  49 3B F7                        cmp rsi, r15
003674B0  0F 84 94 02 00 00               je 0x14036774a
003674B6  E8 75 2B 35 00                  call 0x1406ba030
003674BB  E9 29 FF FF FF                  jmp 0x1403673e9
003674C0  49 8B CE                        mov rcx, r14
003674C3  33 D2                           xor edx, edx
003674C5  E8 8A E4 00 00                  call 0x140375954
003674CA  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003674D4  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
003674D9  E9 17 FE FF FF                  jmp 0x1403672f5
003674DE  41 F6 46 22 10                  test byte ptr [r14 + 0x22], 0x10
003674E3  49 8B CE                        mov rcx, r14
003674E6  44 89 5D 7F                     mov dword ptr [rbp + 0x7f], r11d
003674EA  0F 84 60 01 00 00               je 0x140367650
003674F0  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
003674F4  45 33 C0                        xor r8d, r8d
003674F7  E8 04 36 F5 FF                  call 0x1402bab00
003674FC  4C 8B E0                        mov r12, rax
003674FF  48 8D 48 20                     lea rcx, [rax + 0x20]
00367503  E8 28 19 EE FF                  call 0x140248e30
00367508  33 D2                           xor edx, edx
0036750A  41 B8 00 00 00 80               mov r8d, 0x80000000
00367510  48 8B CF                        mov rcx, rdi
00367513  E8 F8 B5 FC FF                  call 0x140332b10
00367518  33 D2                           xor edx, edx
0036751A  4C 8B F8                        mov r15, rax
0036751D  48 3B 75 C7                     cmp rsi, qword ptr [rbp - 0x39]
00367521  0F 85 D4 01 00 00               jne 0x1403676fb
00367527  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
0036752A  41 B8 00 10 00 00               mov r8d, 0x1000
00367530  44 2B C0                        sub r8d, eax
00367533  49 8D 0C 07                     lea rcx, [r15 + rax]
00367537  E8 04 F7 35 00                  call 0x1406c6c40
0036753C  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
00367546  49 C1 EF 09                     shr r15, 9
0036754A  4C 23 F8                        and r15, rax
0036754D  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00367557  48 8B C0                        mov rax, rax
0036755A  4C 03 F8                        add r15, rax
0036755D  45 33 DB                        xor r11d, r11d
00367560  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00367569  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
00367570  48 8B 05 09 93 CA FF            mov rax, qword ptr [rip - 0x356cf7]
00367577  4C 89 19                        mov qword ptr [rcx], r11
0036757A  49 89 07                        mov qword ptr [r15], rax
0036757D  45 8D 7B 01                     lea r15d, [r11 + 1]
00367581  44 39 3D C4 8B AC 00            cmp dword ptr [rip + 0xac8bc4], r15d
00367588  75 36                           jne 0x1403675c0
0036758A  48 8B 05 17 8C AC 00            mov rax, qword ptr [rip + 0xac8c17]
00367591  4C 8B D7                        mov r10, rdi
00367594  41 83 E2 1F                     and r10d, 0x1f
00367598  48 8B CF                        mov rcx, rdi
0036759B  48 C1 E9 05                     shr rcx, 5
0036759F  45 8B CF                        mov r9d, r15d
003675A2  4C 8D 04 88                     lea r8, [rax + rcx*4]
003675A6  49 8D 42 01                     lea rax, [r10 + 1]
003675AA  48 83 F8 20                     cmp rax, 0x20
003675AE  0F 87 53 01 00 00               ja 0x140367707
003675B4  41 8B CA                        mov ecx, r10d
003675B7  41 8B C7                        mov eax, r15d
003675BA  D3 E0                           shl eax, cl
003675BC  F0 41 09 00                     lock or dword ptr [r8], eax
003675C0  4D 85 E4                        test r12, r12
003675C3  74 0D                           je 0x1403675d2
003675C5  49 8D 4C 24 20                  lea rcx, [r12 + 0x20]
003675CA  E8 C1 2F EE FF                  call 0x14024a590
003675CF  45 33 DB                        xor r11d, r11d
003675D2  44 39 5D 7F                     cmp dword ptr [rbp + 0x7f], r11d
003675D6  0F 84 EB FC FF FF               je 0x1403672c7
003675DC  BA 08 00 00 00                  mov edx, 8
003675E1  49 8B CE                        mov rcx, r14
003675E4  E8 17 2A F5 FF                  call 0x1402ba000
003675E9  E9 D9 FC FF FF                  jmp 0x1403672c7
003675EE  4D 8B 6D 10                     mov r13, qword ptr [r13 + 0x10]
003675F2  49 8B 75 08                     mov rsi, qword ptr [r13 + 8]
003675F6  48 85 F6                        test rsi, rsi
003675F9  0F 84 7D FD FF FF               je 0x14036737c
003675FF  4D 3B EC                        cmp r13, r12
00367602  0F 85 58 BF 37 00               jne 0x1406e3560
00367608  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
0036760D  45 85 C0                        test r8d, r8d
00367610  48 8B 55 F7                     mov rdx, qword ptr [rbp - 9]
00367614  48 8D 14 D0                     lea rdx, [rax + rdx*8]
00367618  4C 0F 45 FA                     cmovne r15, rdx
0036761C  4C 89 7D BF                     mov qword ptr [rbp - 0x41], r15
00367620  E9 43 BF 37 00                  jmp 0x1406e3568
00367625  4D 3B EC                        cmp r13, r12
00367628  0F 84 64 FD FF FF               je 0x140367392
0036762E  4D 8B 6D 10                     mov r13, qword ptr [r13 + 0x10]
00367632  49 8B D3                        mov rdx, r11
00367635  48 89 55 D7                     mov qword ptr [rbp - 0x29], rdx
00367639  E9 D6 FA FF FF                  jmp 0x140367114
0036763E  48 8D 4D DF                     lea rcx, [rbp - 0x21]
00367642  E8 45 40 FC FF                  call 0x14032b68c
00367647  48 8B 5D DF                     mov rbx, qword ptr [rbp - 0x21]
0036764B  E9 F3 FB FF FF                  jmp 0x140367243
00367650  33 D2                           xor edx, edx
00367652  C7 45 7F 01 00 00 00            mov dword ptr [rbp + 0x7f], 1
00367659  E8 32 FF F1 FF                  call 0x140287590
0036765E  49 8B CE                        mov rcx, r14
00367661  A8 03                           test al, 3
00367663  0F 85 5A FE FF FF               jne 0x1403674c3
00367669  E8 62 97 00 00                  call 0x140370dd0
0036766E  48 8B D8                        mov rbx, rax
00367671  33 C0                           xor eax, eax
00367673  44 8B E0                        mov r12d, eax
00367676  E9 8D FE FF FF                  jmp 0x140367508
0036767B  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
0036767F  49 8B C0                        mov rax, r8
00367682  48 C1 E8 0C                     shr rax, 0xc
00367686  83 E0 0F                        and eax, 0xf
00367689  48 8B 94 C1 60 48 00 00         mov rdx, qword ptr [rcx + rax*8 + 0x4860]
00367691  48 8B 05 E8 65 AC 00            mov rax, qword ptr [rip + 0xac65e8]
00367698  48 85 C0                        test rax, rax
0036769B  74 0C                           je 0x1403676a9
0036769D  41 F6 C0 10                     test r8b, 0x10
003676A1  75 06                           jne 0x1403676a9
003676A3  48 F7 D0                        not rax
003676A6  4C 23 C0                        and r8, rax
003676A9  49 C1 E8 20                     shr r8, 0x20
003676AD  41 B9 02 00 00 00               mov r9d, 2
003676B3  E9 A7 FB FF FF                  jmp 0x14036725f
003676B8  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
003676BC  48 8B C7                        mov rax, rdi
003676BF  48 C1 E8 0C                     shr rax, 0xc
003676C3  4C 8B C7                        mov r8, rdi
003676C6  83 E0 0F                        and eax, 0xf
003676C9  48 8B 94 C1 60 48 00 00         mov rdx, qword ptr [rcx + rax*8 + 0x4860]
003676D1  48 8B 05 A8 65 AC 00            mov rax, qword ptr [rip + 0xac65a8]
003676D8  48 85 C0                        test rax, rax
003676DB  74 0F                           je 0x1403676ec
003676DD  40 F6 C7 10                     test dil, 0x10
003676E1  75 61                           jne 0x140367744
003676E3  4C 8B C0                        mov r8, rax
003676E6  49 F7 D0                        not r8
003676E9  4C 23 C7                        and r8, rdi
003676EC  49 C1 E8 20                     shr r8, 0x20
003676F0  41 B9 02 00 00 00               mov r9d, 2
003676F6  E9 41 FC FF FF                  jmp 0x14036733c
003676FB  44 8B 45 6F                     mov r8d, dword ptr [rbp + 0x6f]
003676FF  49 8B CF                        mov rcx, r15
00367702  E9 30 FE FF FF                  jmp 0x140367537
00367707  4D 85 D2                        test r10, r10
0036770A  75 47                           jne 0x140367753
0036770C  49 8B C9                        mov rcx, r9
0036770F  41 8B C7                        mov eax, r15d
00367712  D3 E0                           shl eax, cl
00367714  41 2B C7                        sub eax, r15d
00367717  E9 A0 FE FF FF                  jmp 0x1403675bc
0036771C  8B 05 96 F3 C5 00               mov eax, dword ptr [rip + 0xc5f396]
00367722  A8 40                           test al, 0x40
00367724  0F 84 41 FC FF FF               je 0x14036736b
0036772A  E8 61 7D FA FF                  call 0x14030f490
0036772F  84 C0                           test al, al
00367731  0F 84 34 FC FF FF               je 0x14036736b
00367737  41 8B CC                        mov ecx, r12d
0036773A  E8 21 7D FA FF                  call 0x14030f460
0036773F  E9 29 FC FF FF                  jmp 0x14036736d
00367744  49 83 E0 EF                     and r8, 0xffffffffffffffef
00367748  EB A2                           jmp 0x1403676ec
0036774A  44 8B 45 6F                     mov r8d, dword ptr [rbp + 0x6f]
0036774E  E9 8F FC FF FF                  jmp 0x1403673e2
00367753  83 E7 1F                        and edi, 0x1f
00367756  BA 20 00 00 00                  mov edx, 0x20
0036775B  2B D7                           sub edx, edi
0036775D  41 8B C7                        mov eax, r15d
00367760  8B CA                           mov ecx, edx
00367762  D3 E0                           shl eax, cl
00367764  49 8B CA                        mov rcx, r10
00367767  41 2B C7                        sub eax, r15d
0036776A  D3 E0                           shl eax, cl
0036776C  F0 41 09 00                     lock or dword ptr [r8], eax
00367770  8B C2                           mov eax, edx
00367772  49 83 C0 04                     add r8, 4
00367776  4C 2B C8                        sub r9, rax
00367779  49 83 F9 20                     cmp r9, 0x20
0036777D  72 1E                           jb 0x14036779d
0036777F  49 8B D1                        mov rdx, r9
00367782  48 C1 EA 05                     shr rdx, 5
00367786  48 6B C2 E0                     imul rax, rdx, -0x20
0036778A  4C 03 C8                        add r9, rax
0036778D  41 C7 00 FF FF FF FF            mov dword ptr [r8], 0xffffffff
00367794  49 83 C0 04                     add r8, 4
00367798  49 2B D7                        sub rdx, r15
0036779B  75 F0                           jne 0x14036778d
0036779D  4D 85 C9                        test r9, r9
003677A0  0F 84 1A FE FF FF               je 0x1403675c0
003677A6  E9 61 FF FF FF                  jmp 0x14036770c
003677AB  41 8B 45 2C                     mov eax, dword ptr [r13 + 0x2c]
003677AF  48 8D 14 C1                     lea rdx, [rcx + rax*8]
003677B3  E9 79 F9 FF FF                  jmp 0x140367131
003677B8  48 8D B3 00 10 00 00            lea rsi, [rbx + 0x1000]
003677BF  E9 3D FB FF FF                  jmp 0x140367301
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiZeroCfgSystemWideBitmapWorker(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m5F;
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
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_rsp = (v_rsp) - (152);
    v_rbx = (a2) >> (3);
    a3 = (a3) >> (3);
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & ((unsigned int)((unsigned int)(0xFFFULL))));
    v_stack_p18 = (unsigned int)(v_r15);
    a4 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 60)) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    v_stack_mB0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11309014) + (unsigned __int16)(a4) * 8);
    result = (unsigned int)((a3 + v_rbx * 1) & ((unsigned int)((unsigned int)(0xFFFULL))));
    v_stack_p10 = (unsigned int)(result);
    result = (a3 - 1) + (v_rbx);
    result = (result) >> (12);
    v_stack_m70 = result;
    result = MiLocatePagefileSubsection(a1, v_stack_m70, a3, (unsigned __int16)(a4));
    v_stack_m78 = result;
    v_rbx = (v_rbx) >> (12);
    v_stack_m68 = v_stack_m70;
    v_stack_m88 = v_rbx;
    result = MiLocatePagefileSubsection(a1, v_stack_m88, a3, (unsigned __int16)(a4));
    v_r11 = 0;
loc_00367114:
    if (*(unsigned __int64 *)(result + 8) == 0) goto loc_00367625;
    if (result != result) goto loc_003677AB;
loc_00367131:
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_r15))));
    v_stack_mB8 = *(unsigned __int64 *)(result + 8) + v_stack_m70 * 8;
    v_stack_p8 = 17;
    v_stack_m90 = 0;
    result = (result) & (*(unsigned __int64 *)(result + 8) + v_stack_m88 * 8);
    v_stack_mA8 = 0;
    v_stack_m98 = result;
    result = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))));
    v_r15 = (v_r15) & (*(unsigned __int64 *)(result + 8) + v_stack_m70 * 8);
    v_stack_mA0 = v_r15;
loc_00367169:
    if ((*(unsigned __int64 *)(result + 8) + v_stack_m88 * 8) >= (*(unsigned __int64 *)(result + 8) + v_stack_m70 * 8)) goto loc_0036737C;
    v_rbx = (*(unsigned __int64 *)(result + 8) + v_stack_m88 * 8) & (0xFFFFFFFFFFFFF000ULL);
    result = (0) & (0xFFFFFFFFFFFFF000ULL);
    if (result != v_rbx) goto loc_0036749F;
loc_0036718E:
    if (0 == 0) goto loc_0036747A;
loc_00367197:
    a2 = 0;
    result = MiLockLeafPage(*(unsigned __int64 *)(result + 8) + v_stack_m88 * 8, a2, (unsigned int)(v_stack_p10), (unsigned __int16)(a4));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + v_stack_m88 * 8))) & (1)) != 0) goto loc_003673A7;
    if (condition_is_below) goto loc_003672F5;
    if (condition_is_above_or_equal) goto loc_00367317;
    v_r11 = 0;
    if (*(unsigned __int64 *)(v_rip + 11299506) == 0) goto loc_003671E6;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + v_stack_m88 * 8))) & (16)) != 0) goto loc_0036730E;
    result = ~(*(unsigned __int64 *)(v_rip + 11299506));
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + v_stack_m88 * 8)) & (result);
loc_003671E6:
    v_rdi = (v_rdi) >> (12);
    v_rdi = (v_rdi) & (result);
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 32))) != 0) goto loc_003672CF;
    if ((*(unsigned __int64 *)(result + 8) + v_stack_m88 * 8) == v_stack_m98) goto loc_003674DE;
    if ((*(unsigned __int64 *)(result + 8) + v_stack_m88 * 8) == v_r15) goto loc_003674DE;
    a2 = 0;
    result = MiUnlinkPageFromListEx(result, a2, (unsigned int)(v_stack_p10), (unsigned __int16)(a4));
    if ((((unsigned __int8)(result)) & (3)) != 0) goto loc_003674C0;
    v_stack_m80 = *(unsigned __int64 *)(result + 16);
    result = (unsigned __int8)((*(unsigned __int64 *)(result + 16)) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0036763E;
    v_stack_m80 = 0;
loc_00367243:
    v_r12 = 0;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(result + 16))) >> (1));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0036767B;
    a4 = 0;
    a3 = 0;
    a2 = 0;
loc_0036725F:
    result = MiTransferSoftwarePte(*(unsigned __int64 *)(result + 16), a2, a3, a4);
    result = (*(unsigned __int64 *)(result + 40)) & (*(unsigned __int64 *)(result + 16));
    v_r15 = (result + result * 2) << (4);
    v_r15 = (v_r15) + (result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + v_stack_m88 * 8) = result;
loc_00367294:
    if (condition_is_below) goto loc_0036735B;
    a2 = 0;
    result = MiDecrementShareCountEx(v_r15, a2, a3, result);
    result = MiInsertPageInFreeOrZeroedList(v_rdi, 2, a3, result);
loc_003672C7:
loc_003672CF:
    if (0 == 0) goto loc_003672F5;
loc_003672EA:
    result = MiReleasePageFileInfo(v_stack_mB0, 0, 1, result);
loc_003672F5:
    v_rsi = (*(unsigned __int64 *)(result + 8) + v_stack_m88 * 8) + (8);
loc_00367301:
    goto loc_00367169;
loc_0036730E:
    v_rdi = (v_stack_mA8) & (-17);
    goto loc_003671E6;
loc_00367317:
    if (v_rdi == 0) goto loc_003672F5;
    if (v_rsi == v_stack_m98) goto loc_003672F5;
    if (v_rsi == v_stack_mA0) goto loc_003672F5;
    result = (unsigned __int8)(((unsigned __int8)(v_rdi)) >> (1));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_003676B8;
    a4 = 0;
    a3 = 0;
    a2 = 0;
loc_0036733C:
    result = MiTransferSoftwarePte(v_rdi, a2, a3, a4);
    a3 = 0;
    result = MiReleasePageFileSpace(v_stack_mB0, v_rdi, a3, a4);
    *(unsigned __int64 *)(v_rsi) = result;
    goto loc_003672F5;
loc_0036735B:
    v_r12 = (unsigned int)((v_stack_m78) + 1);
    if (((*(unsigned int *)(v_rip + 12967751)) & ((unsigned int)(v_r12))) == 0) goto loc_0036771C;
loc_0036736B:
loc_0036736D:
    if (!sign_flag) goto loc_00367294;
    goto loc_0036735B;
loc_0036737C:
    if (result != v_r12) goto loc_003675EE;
    result = *(unsigned __int64 *)(v_stack_mA0 + 24);
    if (v_stack_mB0 != 0) {
        a2 = v_stack_p8;
        result = MiUnlockProtoPoolPage(v_stack_mB0, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (152);
    return result;
loc_003673A7:
    v_rdi = (v_rdi) >> (12);
    a1 = (v_stack_mB0) & (v_rdi);
    a2 = 0;
    result = MiMapPageInHyperSpaceWorker(a1, a2, (unsigned int)(0x80000000ULL), a4);
    if (v_rsi != v_stack_m98) goto loc_003674AA;
    a3 = (unsigned int)(((unsigned int)(0x1000ULL)) - ((unsigned int)((unsigned int)(v_stack_p18))));
loc_003673E2:
    a2 = 0;
    result = memset(result + (unsigned int)(v_stack_p18) * 1, a2, a3, a4);
loc_003673E9:
    v_rbx = (result) >> (9);
    v_rbx = (v_rbx) & (result);
    v_rbx = (v_rbx) + (result);
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872)) = 0;
    *(unsigned __int64 *)(v_rbx) = *(unsigned __int64 *)(v_rip - 3500969);
    result = MiCaptureDirtyBitToPfn(0, a2, a3, a4);
    if (result == 0) goto loc_003672F5;
    a1 = (*(unsigned __int64 *)(result + 40)) >> (43);
    a1 = (unsigned int)((a1) & (0x3FFULL));
    goto loc_003672EA;
loc_0036746A:
    result = MiUnlockProtoPoolPage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11308081) + a1 * 8), v_stack_p8, a3, a4);
    result = 0;
    v_stack_mA8 = 0;
loc_0036747A:
    result = MiLockProtoPoolPage(v_rsi, v_stack_p8, a3, a4);
    v_stack_m90 = result;
    if (result == 0) goto loc_003677B8;
    v_stack_mA8 = v_rsi;
    goto loc_00367197;
loc_0036749F:
    if (0 == 0) goto loc_0036718E;
    goto loc_0036746A;
loc_003674AA:
    if (v_rsi == v_stack_mA0) goto loc_0036774A;
    result = KeZeroSinglePage(v_rbx, v_stack_p8, a3, a4);
    goto loc_003673E9;
loc_003674C0:
loc_003674C3:
    a2 = 0;
    result = MiDiscardTransitionPteEx(result, a2, a3, a4);
    goto loc_003672F5;
loc_003674DE:
    v_stack_p20 = 0;
    if (((*(unsigned __int8 *)(result + 34)) & (16)) == 0) goto loc_00367650;
    a3 = 0;
    result = MiDetermineModifiedPageListHead(result, v_stack_mB0, a3, a4);
    result = ExAcquireSpinLockSharedAtDpcLevel(result + 32, v_stack_mB0, a3, a4);
loc_00367508:
    a2 = 0;
    result = MiMapPageInHyperSpaceWorker(0, a2, (unsigned int)(0x80000000ULL), a4);
    a2 = 0;
    if (v_rsi != v_stack_m98) goto loc_003676FB;
    a3 = (unsigned int)(((unsigned int)(0x1000ULL)) - ((unsigned int)((unsigned int)(v_stack_p18))));
loc_00367537:
    result = memset(result + (unsigned int)(v_stack_p18) * 1, a2, a3, a4);
    v_r15 = (result) >> (9);
    v_r15 = (v_r15) & (result);
    v_r15 = (v_r15) + (result);
    v_r11 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872)) = 0;
    *(unsigned __int64 *)(v_r15) = *(unsigned __int64 *)(v_rip - 3501303);
    if ((*(unsigned int *)(v_rip + 11307972)) != ((unsigned int)(v_r11 + 1))) goto loc_003675C0;
    v_r10 = (unsigned int)((0) & (31));
    a1 = (0) >> (5);
    if ((v_r10 + 1) > 32) goto loc_00367707;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r11 + 1))) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r10)))));
loc_003675BC:
loc_003675C0:
    if (result != 0) {
        a1 = result + 32;
        result = ExReleaseSpinLockSharedFromDpcLevel(a1, a2, *(unsigned __int64 *)(v_rip + 11308055) + a1 * 4, (unsigned int)((unsigned int)(v_r11 + 1)));
        v_r11 = 0;
    }
    if (v_stack_p20 == 0) goto loc_003672C7;
    result = MiInsertPageInList(result, 8, *(unsigned __int64 *)(v_rip + 11308055) + a1 * 4, (unsigned int)((unsigned int)(v_r11 + 1)));
    goto loc_003672C7;
loc_003675EE:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) == 0) goto loc_0036737C;
    v_r15 = v_r11 + 1;
    if ((unsigned int)(*(unsigned __int64 *)(v_rip + 11308055) + a1 * 4) != 0) { v_r15 = *(unsigned __int64 *)(result + 8) + v_stack_m68 * 8; }
    v_stack_mA0 = v_r15;
loc_00367625:
    if ((*(unsigned __int64 *)(result + 16)) == result) goto loc_00367392;
    v_stack_m88 = 0;
    goto loc_00367114;
loc_0036763E:
    result = MiClearPageFileReservation(v_stack_m80, 0, *(unsigned __int64 *)(v_rip + 11308055) + a1 * 4, (unsigned int)((unsigned int)(v_r11 + 1)));
    goto loc_00367243;
loc_00367650:
    a2 = 0;
    v_stack_p20 = 1;
    result = MiUnlinkPageFromListEx(v_stack_m80, a2, *(unsigned __int64 *)(v_rip + 11308055) + a1 * 4, (unsigned int)((unsigned int)(v_r11 + 1)));
    if ((((unsigned __int8)(result)) & (3)) != 0) goto loc_003674C3;
    result = MiCaptureDirtyBitToPfn(result, a2, *(unsigned __int64 *)(v_rip + 11308055) + a1 * 4, (unsigned int)((unsigned int)(v_r11 + 1)));
    result = 0;
    goto loc_00367508;
loc_0036767B:
    result = (*(unsigned __int64 *)(v_rip + 11308055) + a1 * 4) >> (12);
    result = (unsigned int)((result) & (15));
    if (*(unsigned __int64 *)(v_rip + 11298280) == 0) goto loc_003676A9;
    result = *(unsigned __int64 *)(v_rip + 11298280);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 11308055) + a1 * 4)) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 11298280));
        a3 = (*(unsigned __int64 *)(v_rip + 11308055) + a1 * 4) & (result);
    }
    a3 = (a3) >> (32);
    goto loc_0036725F;
loc_003676B8:
    result = (0) >> (12);
    result = (unsigned int)((result) & (15));
    if (*(unsigned __int64 *)(v_rip + 11298216) == 0) goto loc_003676EC;
    if (((0) & (16)) != 0) goto loc_00367744;
    a3 = ~(*(unsigned __int64 *)(v_rip + 11298216));
    a3 = (a3) & (0);
loc_003676EC:
    a3 = (a3) >> (32);
    goto loc_0036733C;
loc_003676FB:
    goto loc_00367537;
loc_00367707:
    if (v_r10 != 0) goto loc_00367753;
loc_0036770C:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) << (2));
    result = (unsigned int)((result) - ((unsigned int)(v_r15)));
    goto loc_003675BC;
loc_0036771C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12972950)))) & (64)) == 0) goto loc_0036736B;
    result = KiCheckVpBackingLongSpinWaitHypercall(2, *(unsigned __int64 *)(v_stack_mB0 + result * 8 + 18528), (unsigned int)(v_stack_p10), 2);
    if ((unsigned __int8)(result) == 0) goto loc_0036736B;
    result = HvlNotifyLongSpinWait(0, *(unsigned __int64 *)(v_stack_mB0 + result * 8 + 18528), (unsigned int)(v_stack_p10), 2);
    goto loc_0036736D;
loc_00367744:
    a3 = ((unsigned int)(v_stack_p10)) & (-17);
    goto loc_003676EC;
loc_0036774A:
    goto loc_003673E2;
loc_00367753:
    v_rdi = (unsigned int)((0) & (31));
    a2 = (unsigned int)((32) - ((unsigned int)(v_rdi)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    result = (unsigned int)((result) - ((unsigned int)(v_r15)));
    result = (unsigned int)((result) << ((unsigned __int8)(v_r10)));
    a3 = ((unsigned int)(v_stack_p10)) + (4);
    a4 = (2) - ((unsigned int)((unsigned int)(a2)));
    if (a4 < 32) goto loc_0036779D;
    a2 = (a4) >> (5);
    result = ((unsigned int)((unsigned int)(a2))) * (a2);
    a4 = (a4) + (result);
loc_0036778D:
    *(unsigned int *)(a3) = 0xFFFFFFFFULL;
    a3 = (a3) + (4);
    a2 = (a2) - (v_r15);
    if (condition_is_not_equal) goto loc_0036778D;
loc_0036779D:
    if (a4 == 0) goto loc_003675C0;
    goto loc_0036770C;
loc_003677AB:
    goto loc_00367131;
loc_003677B8:
    goto loc_00367301;
}
```

## 5. (Beta) C Style

```c
int64_t MiZeroCfgSystemWideBitmapWorker(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m5F;
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
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p8;

    local_rsp = (local_rsp) - (152);
    local_rbx = (Arg2) >> (3);
    Arg3 = (Arg3) >> (3);
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & ((uint32_t)((uint32_t)(0xFFFULL))));
    v_stack_p18 = (uint32_t)(local_r15);
    a4 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(arg1) + 0x3C)) & ((uint16_t)((uint32_t)(0x3FFULL))));
    v_stack_mB0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAC8FD6) + (uint16_t)(a4) * 8);
    result = (uint32_t)((Arg3 + local_rbx * 1) & ((uint32_t)((uint32_t)(0xFFFULL))));
    v_stack_p10 = (uint32_t)(result);
    result = (Arg3 - 1) + (local_rbx);
    result = (result) >> (12);
    v_stack_m70 = result;
    result = MiLocatePagefileSubsection(Arg1, v_stack_m70, Arg3, (uint16_t)(a4));
    v_stack_m78 = result;
    local_rbx = (local_rbx) >> (12);
    v_stack_m68 = v_stack_m70;
    v_stack_m88 = local_rbx;
    result = MiLocatePagefileSubsection(Arg1, v_stack_m88, Arg3, (uint16_t)(a4));
    local_r11 = 0;
loc_00367114:
    if (*(uint64_t *)(result + 0x8) == 0) goto loc_00367625;
    if (result != result) goto loc_003677AB;
loc_00367131:
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_r15))));
    v_stack_mB8 = *(uint64_t *)(result + 0x8) + v_stack_m70 * 8;
    v_stack_p8 = 17;
    v_stack_m90 = 0;
    result = (result) & (*(uint64_t *)(result + 0x8) + v_stack_m88 * 8);
    v_stack_mA8 = 0;
    v_stack_m98 = result;
    result = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))));
    local_r15 = (local_r15) & (*(uint64_t *)(result + 0x8) + v_stack_m70 * 8);
    v_stack_mA0 = local_r15;
loc_00367169:
    if ((*(uint64_t *)(result + 0x8) + v_stack_m88 * 8) >= (*(uint64_t *)(result + 0x8) + v_stack_m70 * 8)) goto loc_0036737C;
    local_rbx = (*(uint64_t *)(result + 0x8) + v_stack_m88 * 8) & (0xFFFFFFFFFFFFF000ULL);
    result = (0) & (0xFFFFFFFFFFFFF000ULL);
    if (result != local_rbx) goto loc_0036749F;
loc_0036718E:
    if (0 == 0) goto loc_0036747A;
loc_00367197:
    Arg2 = 0;
    result = MiLockLeafPage(*(uint64_t *)(result + 0x8) + v_stack_m88 * 8, Arg2, (uint32_t)(v_stack_p10), (uint16_t)(a4));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + v_stack_m88 * 8))) & (1)) != 0) goto loc_003673A7;
    if (condition_is_below) goto loc_003672F5;
    if (condition_is_above_or_equal) goto loc_00367317;
    local_r11 = 0;
    if (*(uint64_t *)(v_rip + 0xAC6AB2) == 0) goto loc_003671E6;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + v_stack_m88 * 8))) & (16)) != 0) goto loc_0036730E;
    result = ~(*(uint64_t *)(v_rip + 0xAC6AB2));
    local_rdi = (*(uint64_t *)(*(uint64_t *)(result + 0x8) + v_stack_m88 * 8)) & (result);
loc_003671E6:
    local_rdi = (local_rdi) >> (12);
    local_rdi = (local_rdi) & (result);
    if ((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x20))) != 0) goto loc_003672CF;
    if ((*(uint64_t *)(result + 0x8) + v_stack_m88 * 8) == v_stack_m98) goto loc_003674DE;
    if ((*(uint64_t *)(result + 0x8) + v_stack_m88 * 8) == local_r15) goto loc_003674DE;
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(result, Arg2, (uint32_t)(v_stack_p10), (uint16_t)(a4));
    if ((((uint8_t)(result)) & (3)) != 0) goto loc_003674C0;
    v_stack_m80 = *(uint64_t *)(result + 0x10);
    result = (uint8_t)((*(uint64_t *)(result + 0x10)) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0036763E;
    v_stack_m80 = 0;
loc_00367243:
    local_r12 = 0;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(result + 0x10))) >> (1));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0036767B;
    a4 = 0;
    Arg3 = 0;
    Arg2 = 0;
loc_0036725F:
    result = MiTransferSoftwarePte(*(uint64_t *)(result + 0x10), Arg2, Arg3, a4);
    result = (*(uint64_t *)(result + 0x28)) & (*(uint64_t *)(result + 0x10));
    local_r15 = (result + result * 2) << (4);
    local_r15 = (local_r15) + (result);
    *(uint64_t *)(*(uint64_t *)(result + 0x8) + v_stack_m88 * 8) = result;
loc_00367294:
    if (condition_is_below) goto loc_0036735B;
    Arg2 = 0;
    result = MiDecrementShareCountEx(local_r15, Arg2, Arg3, result);
    result = MiInsertPageInFreeOrZeroedList(local_rdi, 2, Arg3, result);
loc_003672C7:
loc_003672CF:
    if (0 == 0) goto loc_003672F5;
loc_003672EA:
    result = MiReleasePageFileInfo(v_stack_mB0, 0, 1, result);
loc_003672F5:
    local_rsi = (*(uint64_t *)(result + 0x8) + v_stack_m88 * 8) + (8);
loc_00367301:
    goto loc_00367169;
loc_0036730E:
    local_rdi = (v_stack_mA8) & (-17);
    goto loc_003671E6;
loc_00367317:
    if (local_rdi == 0) goto loc_003672F5;
    if (local_rsi == v_stack_m98) goto loc_003672F5;
    if (local_rsi == v_stack_mA0) goto loc_003672F5;
    result = (uint8_t)(((uint8_t)(local_rdi)) >> (1));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_003676B8;
    a4 = 0;
    Arg3 = 0;
    Arg2 = 0;
loc_0036733C:
    result = MiTransferSoftwarePte(local_rdi, Arg2, Arg3, a4);
    Arg3 = 0;
    result = MiReleasePageFileSpace(v_stack_mB0, local_rdi, Arg3, a4);
    *(uint64_t *)(local_rsi) = result;
    goto loc_003672F5;
loc_0036735B:
    local_r12 = (uint32_t)((v_stack_m78) + 1);
    if (((*(uint32_t *)(v_rip + 0xC5DF47)) & ((uint32_t)(local_r12))) == 0) goto loc_0036771C;
loc_0036736B:
loc_0036736D:
    if (!sign_flag) goto loc_00367294;
    goto loc_0036735B;
loc_0036737C:
    if (result != local_r12) goto loc_003675EE;
    result = *(uint64_t *)(v_stack_mA0 + 0x18);
    if (v_stack_mB0 != 0) {
        Arg2 = v_stack_p8;
        result = MiUnlockProtoPoolPage(v_stack_mB0, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (152);
    return result;
loc_003673A7:
    local_rdi = (local_rdi) >> (12);
    Arg1 = (v_stack_mB0) & (local_rdi);
    Arg2 = 0;
    result = MiMapPageInHyperSpaceWorker(Arg1, Arg2, (uint32_t)(0x80000000ULL), a4);
    if (local_rsi != v_stack_m98) goto loc_003674AA;
    Arg3 = (uint32_t)(((uint32_t)(0x1000ULL)) - ((uint32_t)((uint32_t)(v_stack_p18))));
loc_003673E2:
    Arg2 = 0;
    result = memset(result + (uint32_t)(v_stack_p18) * 1, Arg2, Arg3, a4);
loc_003673E9:
    local_rbx = (result) >> (9);
    local_rbx = (local_rbx) & (result);
    local_rbx = (local_rbx) + (result);
    result = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838)) = 0;
    *(uint64_t *)(local_rbx) = *(uint64_t *)(v_rip - 0x356BA9);
    result = MiCaptureDirtyBitToPfn(0, Arg2, Arg3, a4);
    if (result == 0) goto loc_003672F5;
    Arg1 = (*(uint64_t *)(result + 0x28)) >> (43);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    goto loc_003672EA;
loc_0036746A:
    result = MiUnlockProtoPoolPage(*(uint64_t *)(*(uint64_t *)(v_rip + 0xAC8C31) + arg1 * 8), v_stack_p8, Arg3, a4);
    result = 0;
    v_stack_mA8 = 0;
loc_0036747A:
    result = MiLockProtoPoolPage(local_rsi, v_stack_p8, Arg3, a4);
    v_stack_m90 = result;
    if (result == 0) goto loc_003677B8;
    v_stack_mA8 = local_rsi;
    goto loc_00367197;
loc_0036749F:
    if (0 == 0) goto loc_0036718E;
    goto loc_0036746A;
loc_003674AA:
    if (local_rsi == v_stack_mA0) goto loc_0036774A;
    result = KeZeroSinglePage(local_rbx, v_stack_p8, Arg3, a4);
    goto loc_003673E9;
loc_003674C0:
loc_003674C3:
    Arg2 = 0;
    result = MiDiscardTransitionPteEx(result, Arg2, Arg3, a4);
    goto loc_003672F5;
loc_003674DE:
    v_stack_p20 = 0;
    if (((*(uint8_t *)(result + 0x22)) & (16)) == 0) goto loc_00367650;
    Arg3 = 0;
    result = MiDetermineModifiedPageListHead(result, v_stack_mB0, Arg3, a4);
    result = ExAcquireSpinLockSharedAtDpcLevel(result + 32, v_stack_mB0, Arg3, a4);
loc_00367508:
    Arg2 = 0;
    result = MiMapPageInHyperSpaceWorker(0, Arg2, (uint32_t)(0x80000000ULL), a4);
    Arg2 = 0;
    if (local_rsi != v_stack_m98) goto loc_003676FB;
    Arg3 = (uint32_t)(((uint32_t)(0x1000ULL)) - ((uint32_t)((uint32_t)(v_stack_p18))));
loc_00367537:
    result = memset(result + (uint32_t)(v_stack_p18) * 1, Arg2, Arg3, a4);
    local_r15 = (result) >> (9);
    local_r15 = (local_r15) & (result);
    local_r15 = (local_r15) + (result);
    local_r11 = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838)) = 0;
    *(uint64_t *)(local_r15) = *(uint64_t *)(v_rip - 0x356CF7);
    if ((*(uint32_t *)(v_rip + 0xAC8BC4)) != ((uint32_t)(local_r11 + 1))) goto loc_003675C0;
    local_r10 = (uint32_t)((0) & (31));
    Arg1 = (0) >> (5);
    if ((local_r10 + 1) > 32) goto loc_00367707;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r11 + 1))) << ((uint8_t)((uint32_t)((uint32_t)(local_r10)))));
loc_003675BC:
loc_003675C0:
    if (result != 0) {
        Arg1 = result + 32;
        result = ExReleaseSpinLockSharedFromDpcLevel(Arg1, Arg2, *(uint64_t *)(v_rip + 0xAC8C17) + Arg1 * 4, (uint32_t)((uint32_t)(local_r11 + 1)));
        local_r11 = 0;
    }
    if (v_stack_p20 == 0) goto loc_003672C7;
    result = MiInsertPageInList(result, 8, *(uint64_t *)(v_rip + 0xAC8C17) + Arg1 * 4, (uint32_t)((uint32_t)(local_r11 + 1)));
    goto loc_003672C7;
loc_003675EE:
    if (*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) == 0) goto loc_0036737C;
    local_r15 = local_r11 + 1;
    if ((uint32_t)(*(uint64_t *)(v_rip + 0xAC8C17) + Arg1 * 4) != 0) { local_r15 = *(uint64_t *)(result + 0x8) + v_stack_m68 * 8; }
    v_stack_mA0 = local_r15;
loc_00367625:
    if ((*(uint64_t *)(result + 0x10)) == result) goto loc_00367392;
    v_stack_m88 = 0;
    goto loc_00367114;
loc_0036763E:
    result = MiClearPageFileReservation(v_stack_m80, 0, *(uint64_t *)(v_rip + 0xAC8C17) + Arg1 * 4, (uint32_t)((uint32_t)(local_r11 + 1)));
    goto loc_00367243;
loc_00367650:
    Arg2 = 0;
    v_stack_p20 = 1;
    result = MiUnlinkPageFromListEx(v_stack_m80, Arg2, *(uint64_t *)(v_rip + 0xAC8C17) + Arg1 * 4, (uint32_t)((uint32_t)(local_r11 + 1)));
    if ((((uint8_t)(result)) & (3)) != 0) goto loc_003674C3;
    result = MiCaptureDirtyBitToPfn(result, Arg2, *(uint64_t *)(v_rip + 0xAC8C17) + Arg1 * 4, (uint32_t)((uint32_t)(local_r11 + 1)));
    result = 0;
    goto loc_00367508;
loc_0036767B:
    result = (*(uint64_t *)(v_rip + 0xAC8C17) + Arg1 * 4) >> (12);
    result = (uint32_t)((result) & (15));
    if (*(uint64_t *)(v_rip + 0xAC65E8) == 0) goto loc_003676A9;
    result = *(uint64_t *)(v_rip + 0xAC65E8);
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0xAC8C17) + Arg1 * 4)) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xAC65E8));
        Arg3 = (*(uint64_t *)(v_rip + 0xAC8C17) + Arg1 * 4) & (result);
    }
    Arg3 = (Arg3) >> (32);
    goto loc_0036725F;
loc_003676B8:
    result = (0) >> (12);
    result = (uint32_t)((result) & (15));
    if (*(uint64_t *)(v_rip + 0xAC65A8) == 0) goto loc_003676EC;
    if (((0) & (16)) != 0) goto loc_00367744;
    Arg3 = ~(*(uint64_t *)(v_rip + 0xAC65A8));
    Arg3 = (Arg3) & (0);
loc_003676EC:
    Arg3 = (Arg3) >> (32);
    goto loc_0036733C;
loc_003676FB:
    goto loc_00367537;
loc_00367707:
    if (local_r10 != 0) goto loc_00367753;
loc_0036770C:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) << (2));
    result = (uint32_t)((result) - ((uint32_t)(local_r15)));
    goto loc_003675BC;
loc_0036771C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC5F396)))) & (64)) == 0) goto loc_0036736B;
    result = KiCheckVpBackingLongSpinWaitHypercall(2, *(uint64_t *)(v_stack_mB0 + result * 8 + 0x4860), (uint32_t)(v_stack_p10), 2);
    if ((uint8_t)(result) == 0) goto loc_0036736B;
    result = HvlNotifyLongSpinWait(0, *(uint64_t *)(v_stack_mB0 + result * 8 + 0x4860), (uint32_t)(v_stack_p10), 2);
    goto loc_0036736D;
loc_00367744:
    Arg3 = ((uint32_t)(v_stack_p10)) & (-17);
    goto loc_003676EC;
loc_0036774A:
    goto loc_003673E2;
loc_00367753:
    local_rdi = (uint32_t)((0) & (31));
    Arg2 = (uint32_t)((32) - ((uint32_t)(local_rdi)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) << ((uint8_t)((uint32_t)((uint32_t)(Arg2)))));
    result = (uint32_t)((result) - ((uint32_t)(local_r15)));
    result = (uint32_t)((result) << ((uint8_t)(local_r10)));
    Arg3 = ((uint32_t)(v_stack_p10)) + (4);
    a4 = (2) - ((uint32_t)((uint32_t)(Arg2)));
    if (a4 < 32) goto loc_0036779D;
    Arg2 = (a4) >> (5);
    result = ((uint32_t)((uint32_t)(Arg2))) * (Arg2);
    a4 = (a4) + (result);
loc_0036778D:
    *(uint32_t *)(Arg3) = 0xFFFFFFFFULL;
    Arg3 = (Arg3) + (4);
    Arg2 = (Arg2) - (local_r15);
    if (condition_is_not_equal) goto loc_0036778D;
loc_0036779D:
    if (a4 == 0) goto loc_003675C0;
    goto loc_0036770C;
loc_003677AB:
    goto loc_00367131;
loc_003677B8:
    goto loc_00367301;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00367060&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
