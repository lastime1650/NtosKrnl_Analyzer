# ExAcquireFastResourceWithFlags

- RVA: `0x00658120`–`0x00658658` (길이 `1,336` bytes)
- VA: `0x0000000140658120`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C2BC`
- 디코드: `376`개 명령, `1,336/1,336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006581A0` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00658200` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00658279` → [ExpAddFastOwnerEntryToThreadList](../41/ExpAddFastOwnerEntryToThreadList_function_00411E50.md) (function, `0x00411E50`)
- `0x0065828A` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x00658298` → [ExpAddFastOwnerEntryToThreadList](../41/ExpAddFastOwnerEntryToThreadList_function_00411E50.md) (function, `0x00411E50`)
- `0x006582A0` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x006582D9` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0065831A` → [KeAbPostReleaseEx](../26/KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x00658334` → [KeAbPostReleaseEx](../26/KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x0065834C` → [ExpAcquireFastResourceExclusiveSlow](../3B/ExpAcquireFastResourceExclusiveSlow_function_003BE2E0.md) (function, `0x003BE2E0`)
- `0x006583A4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x006583D1` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00658400` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0065842C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0065845E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00658484` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x006584B2` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x006584EE` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00658592` → [ExpAddFastOwnerEntryToThreadList](../41/ExpAddFastOwnerEntryToThreadList_function_00411E50.md) (function, `0x00411E50`)
- `0x006585A3` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x006585B1` → [ExpAddFastOwnerEntryToThreadList](../41/ExpAddFastOwnerEntryToThreadList_function_00411E50.md) (function, `0x00411E50`)
- `0x006585B9` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x006585F2` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0065860A` → [KeAbMarkCrossThreadReleasable](../3B/KeAbMarkCrossThreadReleasable_function_003BE8AC.md) (function, `0x003BE8AC`)
- `0x00658617` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0065862F` → [ExpAcquireFastResourceSharedSlow](../21/ExpAcquireFastResourceSharedSlow_function_00211260.md) (function, `0x00211260`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00658120  4C 8B DC                        mov r11, rsp
00658123  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
00658127  49 89 6B 18                     mov qword ptr [r11 + 0x18], rbp
0065812B  49 89 73 20                     mov qword ptr [r11 + 0x20], rsi
0065812F  57                              push rdi
00658130  41 54                           push r12
00658132  41 55                           push r13
00658134  41 56                           push r14
00658136  41 57                           push r15
00658138  48 83 EC 30                     sub rsp, 0x30
0065813C  BF 01 00 00 00                  mov edi, 1
00658141  45 8B E0                        mov r12d, r8d
00658144  48 8B F2                        mov rsi, rdx
00658147  48 8B D9                        mov rbx, rcx
0065814A  44 84 C7                        test dil, r8b
0065814D  0F 84 03 02 00 00               je 0x140658356
00658153  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
0065815C  45 8B F0                        mov r14d, r8d
0065815F  44 0F B7 49 1A                  movzx r9d, word ptr [rcx + 0x1a]
00658164  41 83 E6 08                     and r14d, 8
00658168  41 8B C6                        mov eax, r14d
0065816B  F7 D8                           neg eax
0065816D  1A D2                           sbb dl, dl
0065816F  80 C2 02                        add dl, 2
00658172  44 84 CF                        test dil, r9b
00658175  0F 84 14 02 00 00               je 0x14065838f
0065817B  44 0F 20 C1                     mov rcx, cr8
0065817F  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
00658188  3A CA                           cmp cl, dl
0065818A  76 1A                           jbe 0x1406581a6
0065818C  49 83 63 C8 00                  and qword ptr [r11 - 0x38], 0
00658191  44 0F B6 CA                     movzx r9d, dl
00658195  33 D2                           xor edx, edx
00658197  44 0F B6 C1                     movzx r8d, cl
0065819B  B9 C6 01 00 00                  mov ecx, 0x1c6
006581A0  E8 BB 54 EA FF                  call 0x1404fd660
006581A5  CC                              int3
006581A6  80 F9 02                        cmp cl, 2
006581A9  72 13                           jb 0x1406581be
006581AB  65 8B 04 25 3C 3A 00 00         mov eax, dword ptr gs:[0x3a3c]
006581B3  A9 01 00 01 00                  test eax, 0x10001
006581B8  0F 85 2D 02 00 00               jne 0x1406583eb
006581BE  41 F6 C1 08                     test r9b, 8
006581C2  75 10                           jne 0x1406581d4
006581C4  41 0F B6 80 C0 00 00 00         movzx eax, byte ptr [r8 + 0xc0]
006581CC  A8 02                           test al, 2
006581CE  0F 85 43 02 00 00               jne 0x140658417
006581D4  40 3A CF                        cmp cl, dil
006581D7  73 18                           jae 0x1406581f1
006581D9  41 F7 40 74 00 04 00 00         test dword ptr [r8 + 0x74], 0x400
006581E1  75 0E                           jne 0x1406581f1
006581E3  41 83 B8 E4 01 00 00 00         cmp dword ptr [r8 + 0x1e4], 0
006581EB  0F 84 58 02 00 00               je 0x140658449
006581F1  45 33 C0                        xor r8d, r8d
006581F4  48 8B CB                        mov rcx, rbx
006581F7  45 85 F6                        test r14d, r14d
006581FA  41 0F 94 C0                     sete r8b
006581FE  33 D2                           xor edx, edx
00658200  E8 2B 80 BB FF                  call 0x140210230
00658205  48 8B F0                        mov rsi, rax
00658208  33 C0                           xor eax, eax
0065820A  F0 48 0F B1 3B                  lock cmpxchg qword ptr [rbx], rdi
0065820F  48 8D 6B 40                     lea rbp, [rbx + 0x40]
00658213  0F 85 E9 00 00 00               jne 0x140658302
00658219  41 F6 C4 10                     test r12b, 0x10
0065821D  89 7D 20                        mov dword ptr [rbp + 0x20], edi
00658220  41 BE 03 00 00 00               mov r14d, 3
00658226  41 8D 46 0C                     lea eax, [r14 + 0xc]
0065822A  44 0F 45 F0                     cmovne r14d, eax
0065822E  33 C0                           xor eax, eax
00658230  45 8B E6                        mov r12d, r14d
00658233  45 8B EE                        mov r13d, r14d
00658236  41 C0 EE 03                     shr r14b, 3
0065823A  41 83 E4 02                     and r12d, 2
0065823E  44 22 F7                        and r14b, dil
00658241  41 83 E5 04                     and r13d, 4
00658245  0F 95 C0                        setne al
00658248  49 0B C7                        or rax, r15
0065824B  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0065824F  48 85 F6                        test rsi, rsi
00658252  74 11                           je 0x140658265
00658254  8A 46 08                        mov al, byte ptr [rsi + 8]
00658257  24 3F                           and al, 0x3f
00658259  40 88 7E 0A                     mov byte ptr [rsi + 0xa], dil
0065825D  02 C0                           add al, al
0065825F  40 0A C7                        or al, dil
00658262  88 45 24                        mov byte ptr [rbp + 0x24], al
00658265  45 85 E4                        test r12d, r12d
00658268  74 01                           je 0x14065826b
0065826A  FA                              cli
0065826B  45 85 ED                        test r13d, r13d
0065826E  75 10                           jne 0x140658280
00658270  4C 8B CD                        mov r9, rbp
00658273  45 33 C0                        xor r8d, r8d
00658276  49 8B CF                        mov rcx, r15
00658279  E8 D2 9B DB FF                  call 0x140411e50
0065827E  EB 25                           jmp 0x1406582a5
00658280  49 8D 9F C8 06 00 00            lea rbx, [r15 + 0x6c8]
00658287  48 8B CB                        mov rcx, rbx
0065828A  E8 A1 01 BB FF                  call 0x140208430
0065828F  4C 8B CD                        mov r9, rbp
00658292  44 8A C7                        mov r8b, dil
00658295  49 8B CF                        mov rcx, r15
00658298  E8 B3 9B DB FF                  call 0x140411e50
0065829D  48 8B CB                        mov rcx, rbx
006582A0  E8 CB E3 BA FF                  call 0x140206670
006582A5  45 85 E4                        test r12d, r12d
006582A8  74 35                           je 0x1406582df
006582AA  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
006582B3  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
006582BA  4D 85 C0                        test r8, r8
006582BD  74 1F                           je 0x1406582de
006582BF  41 0F 0D 08                     prefetchw byte ptr [r8]
006582C3  41 8B 00                        mov eax, dword ptr [r8]
006582C6  8B D0                           mov edx, eax
006582C8  0F BA F2 15                     btr edx, 0x15
006582CC  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
006582D1  75 F3                           jne 0x1406582c6
006582D3  0F BA E0 15                     bt eax, 0x15
006582D7  73 05                           jae 0x1406582de
006582D9  E8 F2 AE C0 FF                  call 0x1402631d0
006582DE  FB                              sti
006582DF  45 85 ED                        test r13d, r13d
006582E2  0F 84 4F 03 00 00               je 0x140658637
006582E8  45 84 F6                        test r14b, r14b
006582EB  0F 84 1E 03 00 00               je 0x14065860f
006582F1  48 85 F6                        test rsi, rsi
006582F4  0F 84 15 03 00 00               je 0x14065860f
006582FA  48 8B D6                        mov rdx, rsi
006582FD  E9 08 03 00 00                  jmp 0x14065860a
00658302  4C 39 7D 10                     cmp qword ptr [rbp + 0x10], r15
00658306  75 1C                           jne 0x140658324
00658308  01 7D 20                        add dword ptr [rbp + 0x20], edi
0065830B  48 85 F6                        test rsi, rsi
0065830E  0F 84 23 03 00 00               je 0x140658637
00658314  48 8B D6                        mov rdx, rsi
00658317  48 8B CB                        mov rcx, rbx
0065831A  E8 F1 9E C0 FF                  call 0x140262210
0065831F  E9 13 03 00 00                  jmp 0x140658637
00658324  45 85 F6                        test r14d, r14d
00658327  75 12                           jne 0x14065833b
00658329  48 85 F6                        test rsi, rsi
0065832C  74 2E                           je 0x14065835c
0065832E  48 8B D6                        mov rdx, rsi
00658331  48 8B CB                        mov rcx, rbx
00658334  E8 D7 9E C0 FF                  call 0x140262210
00658339  EB 21                           jmp 0x14065835c
0065833B  4C 8B CE                        mov r9, rsi
0065833E  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00658343  4D 8B C7                        mov r8, r15
00658346  48 8B D0                        mov rdx, rax
00658349  48 8B CB                        mov rcx, rbx
0065834C  E8 8F 5F D6 FF                  call 0x1403be2e0
00658351  E9 E1 02 00 00                  jmp 0x140658637
00658356  41 F6 C4 06                     test r12b, 6
0065835A  75 08                           jne 0x140658364
0065835C  40 32 FF                        xor dil, dil
0065835F  E9 D3 02 00 00                  jmp 0x140658637
00658364  44 0F B7 49 1A                  movzx r9d, word ptr [rcx + 0x1a]
00658369  45 8B D4                        mov r10d, r12d
0065836C  41 83 E2 08                     and r10d, 8
00658370  45 8B F4                        mov r14d, r12d
00658373  41 83 E6 04                     and r14d, 4
00658377  45 8B EC                        mov r13d, r12d
0065837A  41 83 E5 10                     and r13d, 0x10
0065837E  41 8B C2                        mov eax, r10d
00658381  F7 D8                           neg eax
00658383  45 1A C0                        sbb r8b, r8b
00658386  41 80 C0 02                     add r8b, 2
0065838A  44 84 CF                        test dil, r9b
0065838D  75 1B                           jne 0x1406583aa
0065838F  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00658395  45 33 C9                        xor r9d, r9d
00658398  4C 8B C3                        mov r8, rbx
0065839B  B9 C6 01 00 00                  mov ecx, 0x1c6
006583A0  41 8D 51 03                     lea edx, [r9 + 3]
006583A4  E8 B7 52 EA FF                  call 0x1404fd660
006583A9  CC                              int3
006583AA  44 0F 20 C1                     mov rcx, cr8
006583AE  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
006583B7  41 3A C8                        cmp cl, r8b
006583BA  76 1B                           jbe 0x1406583d7
006583BC  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
006583C2  33 D2                           xor edx, edx
006583C4  45 0F B6 C8                     movzx r9d, r8b
006583C8  44 0F B6 C1                     movzx r8d, cl
006583CC  B9 C6 01 00 00                  mov ecx, 0x1c6
006583D1  E8 8A 52 EA FF                  call 0x1404fd660
006583D6  CC                              int3
006583D7  80 F9 02                        cmp cl, 2
006583DA  72 2A                           jb 0x140658406
006583DC  65 8B 04 25 3C 3A 00 00         mov eax, dword ptr gs:[0x3a3c]
006583E4  A9 01 00 01 00                  test eax, 0x10001
006583E9  74 1B                           je 0x140658406
006583EB  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
006583F1  45 33 C9                        xor r9d, r9d
006583F4  45 33 C0                        xor r8d, r8d
006583F7  B9 C6 01 00 00                  mov ecx, 0x1c6
006583FC  41 8D 51 05                     lea edx, [r9 + 5]
00658400  E8 5B 52 EA FF                  call 0x1404fd660
00658405  CC                              int3
00658406  41 F6 C1 08                     test r9b, 8
0065840A  75 26                           jne 0x140658432
0065840C  0F B6 82 C0 00 00 00            movzx eax, byte ptr [rdx + 0xc0]
00658413  A8 02                           test al, 2
00658415  74 1B                           je 0x140658432
00658417  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0065841D  45 33 C9                        xor r9d, r9d
00658420  45 33 C0                        xor r8d, r8d
00658423  B9 C6 01 00 00                  mov ecx, 0x1c6
00658428  41 8D 51 06                     lea edx, [r9 + 6]
0065842C  E8 2F 52 EA FF                  call 0x1404fd660
00658431  CC                              int3
00658432  40 3A CF                        cmp cl, dil
00658435  73 2D                           jae 0x140658464
00658437  F7 42 74 00 04 00 00            test dword ptr [rdx + 0x74], 0x400
0065843E  75 24                           jne 0x140658464
00658440  83 BA E4 01 00 00 00            cmp dword ptr [rdx + 0x1e4], 0
00658447  75 1B                           jne 0x140658464
00658449  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0065844F  45 33 C9                        xor r9d, r9d
00658452  45 33 C0                        xor r8d, r8d
00658455  B9 C6 01 00 00                  mov ecx, 0x1c6
0065845A  41 8D 51 07                     lea edx, [r9 + 7]
0065845E  E8 FD 51 EA FF                  call 0x1404fd660
00658463  CC                              int3
00658464  4C 8B 4E 10                     mov r9, qword ptr [rsi + 0x10]
00658468  49 83 E1 FE                     and r9, 0xfffffffffffffffe
0065846C  4C 3B CA                        cmp r9, rdx
0065846F  74 19                           je 0x14065848a
00658471  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00658477  4C 8B C6                        mov r8, rsi
0065847A  BA 09 00 00 00                  mov edx, 9
0065847F  B9 C6 01 00 00                  mov ecx, 0x1c6
00658484  E8 D7 51 EA FF                  call 0x1404fd660
00658489  CC                              int3
0065848A  8A 46 25                        mov al, byte ptr [rsi + 0x25]
0065848D  A8 02                           test al, 2
0065848F  75 27                           jne 0x1406584b8
00658491  4C 8B 4E 18                     mov r9, qword ptr [rsi + 0x18]
00658495  4D 85 C9                        test r9, r9
00658498  74 1E                           je 0x1406584b8
0065849A  4C 3B CB                        cmp r9, rbx
0065849D  74 19                           je 0x1406584b8
0065849F  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
006584A5  4C 8B C6                        mov r8, rsi
006584A8  BA 02 00 00 00                  mov edx, 2
006584AD  B9 C6 01 00 00                  mov ecx, 0x1c6
006584B2  E8 A9 51 EA FF                  call 0x1404fd660
006584B7  CC                              int3
006584B8  8B 4E 20                        mov ecx, dword ptr [rsi + 0x20]
006584BB  85 C9                           test ecx, ecx
006584BD  74 0F                           je 0x1406584ce
006584BF  A8 04                           test al, 4
006584C1  75 0B                           jne 0x1406584ce
006584C3  8D 41 01                        lea eax, [rcx + 1]
006584C6  89 46 20                        mov dword ptr [rsi + 0x20], eax
006584C9  E9 69 01 00 00                  jmp 0x140658637
006584CE  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
006584D7  45 33 C0                        xor r8d, r8d
006584DA  45 85 D2                        test r10d, r10d
006584DD  41 0F 94 C0                     sete r8b
006584E1  33 ED                           xor ebp, ebp
006584E3  40 38 6E 24                     cmp byte ptr [rsi + 0x24], bpl
006584E7  75 0D                           jne 0x1406584f6
006584E9  33 D2                           xor edx, edx
006584EB  48 8B CB                        mov rcx, rbx
006584EE  E8 3D 7D BB FF                  call 0x140210230
006584F3  48 8B E8                        mov rbp, rax
006584F6  0F 0D 0B                        prefetchw byte ptr [rbx]
006584F9  48 8B 03                        mov rax, qword ptr [rbx]
006584FC  40 84 C7                        test dil, al
006584FF  0F 85 19 01 00 00               jne 0x14065861e
00658505  45 85 F6                        test r14d, r14d
00658508  75 08                           jne 0x140658512
0065850A  A8 02                           test al, 2
0065850C  0F 85 0C 01 00 00               jne 0x14065861e
00658512  48 8D 48 04                     lea rcx, [rax + 4]
00658516  48 33 C8                        xor rcx, rax
00658519  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0065851D  48 33 C8                        xor rcx, rax
00658520  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
00658525  75 CF                           jne 0x1406584f6
00658527  45 85 ED                        test r13d, r13d
0065852A  B8 0F 00 00 00                  mov eax, 0xf
0065852F  44 8D 70 F4                     lea r14d, [rax - 0xc]
00658533  44 0F 45 F0                     cmovne r14d, eax
00658537  48 8D 43 40                     lea rax, [rbx + 0x40]
0065853B  45 8B EE                        mov r13d, r14d
0065853E  45 8B E6                        mov r12d, r14d
00658541  41 83 E5 02                     and r13d, 2
00658545  41 83 E4 04                     and r12d, 4
00658549  41 83 E6 08                     and r14d, 8
0065854D  48 3B F0                        cmp rsi, rax
00658550  74 04                           je 0x140658556
00658552  48 89 5E 18                     mov qword ptr [rsi + 0x18], rbx
00658556  33 C0                           xor eax, eax
00658558  89 7E 20                        mov dword ptr [rsi + 0x20], edi
0065855B  45 85 E4                        test r12d, r12d
0065855E  0F 95 C0                        setne al
00658561  49 0B C7                        or rax, r15
00658564  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
00658568  48 85 ED                        test rbp, rbp
0065856B  74 11                           je 0x14065857e
0065856D  8A 45 08                        mov al, byte ptr [rbp + 8]
00658570  24 3F                           and al, 0x3f
00658572  40 88 7D 0A                     mov byte ptr [rbp + 0xa], dil
00658576  02 C0                           add al, al
00658578  40 0A C7                        or al, dil
0065857B  88 46 24                        mov byte ptr [rsi + 0x24], al
0065857E  45 85 ED                        test r13d, r13d
00658581  74 01                           je 0x140658584
00658583  FA                              cli
00658584  45 85 E4                        test r12d, r12d
00658587  75 10                           jne 0x140658599
00658589  4C 8B CE                        mov r9, rsi
0065858C  45 33 C0                        xor r8d, r8d
0065858F  49 8B CF                        mov rcx, r15
00658592  E8 B9 98 DB FF                  call 0x140411e50
00658597  EB 25                           jmp 0x1406585be
00658599  49 8D 9F C8 06 00 00            lea rbx, [r15 + 0x6c8]
006585A0  48 8B CB                        mov rcx, rbx
006585A3  E8 88 FE BA FF                  call 0x140208430
006585A8  4C 8B CE                        mov r9, rsi
006585AB  44 8A C7                        mov r8b, dil
006585AE  49 8B CF                        mov rcx, r15
006585B1  E8 9A 98 DB FF                  call 0x140411e50
006585B6  48 8B CB                        mov rcx, rbx
006585B9  E8 B2 E0 BA FF                  call 0x140206670
006585BE  45 85 ED                        test r13d, r13d
006585C1  74 35                           je 0x1406585f8
006585C3  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
006585CC  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
006585D3  4D 85 C0                        test r8, r8
006585D6  74 1F                           je 0x1406585f7
006585D8  41 0F 0D 08                     prefetchw byte ptr [r8]
006585DC  41 8B 00                        mov eax, dword ptr [r8]
006585DF  8B D0                           mov edx, eax
006585E1  0F BA F2 15                     btr edx, 0x15
006585E5  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
006585EA  75 F3                           jne 0x1406585df
006585EC  0F BA E0 15                     bt eax, 0x15
006585F0  73 05                           jae 0x1406585f7
006585F2  E8 D9 AB C0 FF                  call 0x1402631d0
006585F7  FB                              sti
006585F8  45 85 E4                        test r12d, r12d
006585FB  74 3A                           je 0x140658637
006585FD  45 85 F6                        test r14d, r14d
00658600  74 0D                           je 0x14065860f
00658602  48 85 ED                        test rbp, rbp
00658605  74 08                           je 0x14065860f
00658607  48 8B D5                        mov rdx, rbp
0065860A  E8 9D 62 D6 FF                  call 0x1403be8ac
0065860F  BA 44 66 6C 74                  mov edx, 0x746c6644
00658614  49 8B CF                        mov rcx, r15
00658617  E8 F4 80 BB FF                  call 0x140210710
0065861C  EB 19                           jmp 0x140658637
0065861E  4D 8B CF                        mov r9, r15
00658621  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00658626  4C 8B C5                        mov r8, rbp
00658629  48 8B D6                        mov rdx, rsi
0065862C  48 8B CB                        mov rcx, rbx
0065862F  E8 2C 8C BB FF                  call 0x140211260
00658634  40 8A F8                        mov dil, al
00658637  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0065863C  40 8A C7                        mov al, dil
0065863F  48 8B 6C 24 70                  mov rbp, qword ptr [rsp + 0x70]
00658644  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00658649  48 83 C4 30                     add rsp, 0x30
0065864D  41 5F                           pop r15
0065864F  41 5E                           pop r14
00658651  41 5D                           pop r13
00658653  41 5C                           pop r12
00658655  5F                              pop rdi
00658656  C3                              ret
00658657  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExAcquireFastResourceWithFlags(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    v_rsp = (v_rsp) - (48);
    if (((1) & ((unsigned __int8)(a3))) == 0) goto loc_00658356;
    v_r14 = (unsigned int)(((unsigned int)(a3)) & (8));
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_r14))));
    a2 = (unsigned __int8)((a2) + (2));
    if (((1) & ((unsigned __int8)(*(unsigned __int16 *)(a1 + 26)))) == 0) goto loc_0065838F;
    if (((unsigned __int8)(v_cr8)) >= = ((unsigned __int8)(a2))) {
        a4 = (unsigned __int8)(a2);
        a2 = 0;
        a3 = (unsigned __int8)(v_cr8);
        a1 = 454;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((unsigned __int8)(a1)) < 2) goto loc_006581BE;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 14908))))) & (0x10001ULL)) != 0) goto loc_006583EB;
loc_006581BE:
    if ((((unsigned __int8)(a4)) & (8)) != 0) goto loc_006581D4;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3 + 192))) & (2)) != 0) goto loc_00658417;
loc_006581D4:
    if (((unsigned __int8)(a1)) >= 1) goto loc_006581F1;
    if (((*(unsigned int *)(a3 + 116)) & (0x400ULL)) != 0) goto loc_006581F1;
    if ((*(unsigned int *)(a3 + 484)) == 0) goto loc_00658449;
loc_006581F1:
    a3 = 0;
    a3 = ((unsigned int)(v_r14) == 0) ? 1 : 0;
    a2 = 0;
    result = KeAbPreAcquire(a1, a2, a3, a4);
    result = 0;
    if (condition_is_not_equal) goto loc_00658302;
    *(unsigned int *)(a1 + 64 + 32) = 1;
    v_r14 = 3;
    if ((((unsigned __int8)((unsigned int)(a3))) & (16)) != 0) { v_r14 = (unsigned int)(3 + 12); }
    result = 0;
    v_r14 = (unsigned __int8)((v_r14) >> (3));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (2));
    v_r14 = (unsigned __int8)((v_r14) & (1));
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (4));
    result = (condition_is_not_equal) ? 1 : 0;
    result = (result) | (*(unsigned __int64 *)(gs_base + (0 + 392)));
    *(unsigned __int64 *)(a1 + 64 + 16) = result;
    if (result != 0) {
        result = *(unsigned __int8 *)(result + 8);
        result = (unsigned __int8)((result) & (63));
        *(unsigned __int8 *)(result + 10) = 1;
        result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
        result = (unsigned __int8)((result) | (1));
        *(unsigned __int8 *)(a1 + 64 + 36) = (unsigned __int8)(result);
    }
    if ((unsigned int)(v_r12) != 0) {
    }
    if ((unsigned int)(v_r13) != 0) goto loc_00658280;
    a3 = 0;
    result = ExpAddFastOwnerEntryToThreadList(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a1 + 64);
    goto loc_006582A5;
loc_00658280:
    result = KeAcquireSpinLockAtDpcLevel(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736, a2, a3, a1 + 64);
    result = ExpAddFastOwnerEntryToThreadList(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, 1, a1 + 64);
    result = KxReleaseSpinLock(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736, a2, 1, a1 + 64);
loc_006582A5:
    if ((unsigned int)(v_r12) == 0) goto loc_006582DF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) == 0) goto loc_006582DE;
loc_006582C6:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_006582C6;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536)));
    if (!(condition_is_above_or_equal)) {
        result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a1 + 64);
    }
loc_006582DF:
    if ((unsigned int)(v_r13) == 0) goto loc_00658637;
    if ((unsigned __int8)(v_r14) == 0) goto loc_0065860F;
    if (result == 0) goto loc_0065860F;
    goto loc_0065860A;
loc_00658302:
    if ((*(unsigned __int64 *)(a1 + 64 + 16)) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00658324;
    if (result == 0) goto loc_00658637;
    result = KeAbPostReleaseEx(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736, result, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a1 + 64);
    goto loc_00658637;
loc_00658324:
    if ((unsigned int)(v_r14) != 0) goto loc_0065833B;
    if (result == 0) goto loc_0065835C;
    result = KeAbPostReleaseEx(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736, result, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a1 + 64);
    goto loc_0065835C;
loc_0065833B:
    v_stack_m38 = (unsigned int)(v_r12);
    result = ExpAcquireFastResourceExclusiveSlow(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736, result, *(unsigned __int64 *)(gs_base + (0 + 392)), result);
    goto loc_00658637;
loc_00658356:
    if ((((unsigned __int8)(v_r12)) & (6)) != 0) goto loc_00658364;
loc_0065835C:
    v_rdi = 0;
    goto loc_00658637;
loc_00658364:
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (8));
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (4));
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (16));
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_r10))));
    a3 = (unsigned __int8)((*(unsigned __int64 *)(gs_base + (0 + 392))) + (2));
    if (((0) & ((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736 + 26)))) == 0) {
        a4 = 0;
        a3 = *(unsigned __int64 *)(gs_base + (0 + 392)) + 1736;
        a1 = 454;
        a2 = a4 + 3;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((unsigned __int8)(v_cr8)) >= = ((unsigned __int8)(a3))) {
        a2 = 0;
        a4 = (unsigned __int8)(a3);
        a3 = (unsigned __int8)(v_cr8);
        a1 = 454;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((unsigned __int8)(a1)) < 2) goto loc_00658406;
    result = (unsigned int)(*(unsigned int *)(gs_base + (0 + 14908)));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 14908))))) & (0x10001ULL)) != 0) {
        a4 = 0;
        a3 = 0;
        a1 = 454;
        a2 = a4 + 5;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((0) & (8)) != 0) goto loc_00658432;
    result = *(unsigned __int8 *)(a2 + 192);
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 + 192))) & (2)) != 0) {
        a4 = 0;
        a3 = 0;
        a1 = 454;
        a2 = a4 + 6;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((unsigned __int8)(a1)) >= 0) goto loc_00658464;
    if (((*(unsigned int *)(a2 + 116)) & (0x400ULL)) != 0) goto loc_00658464;
    if ((*(unsigned int *)(a2 + 484)) == 0) {
        a4 = 0;
        a3 = 0;
        a1 = 454;
        a2 = a4 + 7;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a4 = (*(unsigned __int64 *)(result + 16)) & (-2);
    if (a4 != a2) {
        a3 = result;
        a2 = 9;
        a1 = 454;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 37))) & (2)) != 0) goto loc_006584B8;
    if (*(unsigned __int64 *)(result + 24) == 0) goto loc_006584B8;
    result = *(unsigned __int8 *)(result + 37);
    if ((*(unsigned __int64 *)(result + 24)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736)) {
        a3 = result;
        a2 = 2;
        a1 = 454;
        result = KeBugCheckEx(a1, a2, a3, *(unsigned __int64 *)(result + 24));
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 32))) == 0) goto loc_006584CE;
    if ((((unsigned __int8)(result)) & (4)) != 0) goto loc_006584CE;
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 32)) + 1);
    goto loc_00658637;
loc_006584CE:
    a3 = 0;
    a3 = ((unsigned int)(v_r10) == 0) ? 1 : 0;
    v_rbp = 0;
    result = (unsigned int)(*(unsigned int *)(result + 32)) + 1;
    if ((*(unsigned __int8 *)(result + 36)) == 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392)) + 1736;
        result = KeAbPreAcquire(a1, a2, a3, *(unsigned __int64 *)(result + 24));
        v_rbp = result;
    }
    if (((0) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736)))) != 0) goto loc_0065861E;
    if ((unsigned int)(v_r14) != 0) goto loc_00658512;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736))) & (2)) != 0) goto loc_0065861E;
loc_00658512:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736) + 4) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736));
    a1 = (a1) & (-4);
    a1 = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736));
    if (condition_is_not_equal) goto loc_006584F6;
    v_r14 = 15 - 12;
    if ((unsigned int)(v_r13) != 0) { v_r14 = 15; }
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (2));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (4));
    v_r14 = (unsigned int)((v_r14) & (8));
    if (result != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736 + 64)) {
        *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(gs_base + (0 + 392)) + 1736;
    }
    result = 0;
    *(unsigned int *)(result + 32) = 0;
    result = ((unsigned int)(v_r12) != 0) ? 1 : 0;
    result = (result) | (*(unsigned __int64 *)(gs_base + (0 + 392)));
    *(unsigned __int64 *)(result + 16) = result;
    if (v_rbp != 0) {
        result = *(unsigned __int8 *)(v_rbp + 8);
        result = (unsigned __int8)((result) & (63));
        *(unsigned __int8 *)(v_rbp + 10) = 0;
        result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
        result = (unsigned __int8)((result) | (0));
        *(unsigned __int8 *)(result + 36) = (unsigned __int8)(result);
    }
    if ((unsigned int)(v_r13) != 0) {
    }
    if ((unsigned int)(v_r12) != 0) goto loc_00658599;
    a3 = 0;
    result = ExpAddFastOwnerEntryToThreadList(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, result);
    goto loc_006585BE;
loc_00658599:
    result = KeAcquireSpinLockAtDpcLevel(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736, a2, a3, result);
    result = ExpAddFastOwnerEntryToThreadList(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, 0, result);
    result = KxReleaseSpinLock(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736, a2, 0, result);
loc_006585BE:
    if ((unsigned int)(v_r13) == 0) goto loc_006585F8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) == 0) goto loc_006585F7;
loc_006585DF:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_006585DF;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536)));
    if (!(condition_is_above_or_equal)) {
        result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), result);
    }
loc_006585F8:
    if ((unsigned int)(v_r12) == 0) goto loc_00658637;
    if ((unsigned int)(v_r14) == 0) goto loc_0065860F;
    if (v_rbp == 0) goto loc_0065860F;
loc_0065860A:
    result = KeAbMarkCrossThreadReleasable(*(unsigned __int64 *)(gs_base + (0 + 32)), v_rbp, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), result);
loc_0065860F:
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), result);
    goto loc_00658637;
loc_0065861E:
    v_stack_m38 = (unsigned int)(v_r12);
    result = ExpAcquireFastResourceSharedSlow(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1736, result, v_rbp, *(unsigned __int64 *)(gs_base + (0 + 392)));
loc_00658637:
    v_rsp = (v_rsp) + (48);
    return (unsigned __int8)((unsigned __int8)(result));
}
```

## 5. (Beta) C Style

```c
int64_t ExAcquireFastResourceWithFlags(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rbp;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    local_rsp = (local_rsp) - (48);
    if (((1) & ((uint8_t)(Arg3))) == 0) goto loc_00658356;
    local_r14 = (uint32_t)(((uint32_t)(Arg3)) & (8));
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_r14))));
    Arg2 = (uint8_t)((Arg2) + (2));
    if (((1) & ((uint8_t)(*(uint16_t *)(arg1 + 0x1A)))) == 0) goto loc_0065838F;
    if (((uint8_t)(v_cr8)) >= = ((uint8_t)(Arg2))) {
        a4 = (uint8_t)(Arg2);
        Arg2 = 0;
        Arg3 = (uint8_t)(v_cr8);
        Arg1 = 454;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    if (((uint8_t)(Arg1)) < 2) goto loc_006581BE;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x3A3C))))) & (0x10001ULL)) != 0) goto loc_006583EB;
loc_006581BE:
    if ((((uint8_t)(a4)) & (8)) != 0) goto loc_006581D4;
    if ((((uint8_t)(*(uint8_t *)(Arg3 + 0xC0))) & (2)) != 0) goto loc_00658417;
loc_006581D4:
    if (((uint8_t)(Arg1)) >= 1) goto loc_006581F1;
    if (((*(uint32_t *)(Arg3 + 0x74)) & (0x400ULL)) != 0) goto loc_006581F1;
    if ((*(uint32_t *)(Arg3 + 0x1E4)) == 0) goto loc_00658449;
loc_006581F1:
    Arg3 = 0;
    Arg3 = ((uint32_t)(local_r14) == 0) ? 1 : 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1, Arg2, Arg3, a4);
    result = 0;
    if (condition_is_not_equal) goto loc_00658302;
    *(uint32_t *)(arg1 + 0x40 + 0x20) = 1;
    local_r14 = 3;
    if ((((uint8_t)((uint32_t)(Arg3))) & (16)) != 0) { local_r14 = (uint32_t)(3 + 12); }
    result = 0;
    local_r14 = (uint8_t)((local_r14) >> (3));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (2));
    local_r14 = (uint8_t)((local_r14) & (1));
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (4));
    result = (condition_is_not_equal) ? 1 : 0;
    result = (result) | (*(uint64_t *)(gs_base + (0 + 0x188)));
    *(uint64_t *)(arg1 + 0x40 + 0x10) = result;
    if (result != 0) {
        result = *(uint8_t *)(result + 0x8);
        result = (uint8_t)((result) & (63));
        *(uint8_t *)(result + 0xA) = 1;
        result = (uint8_t)((result) + ((uint8_t)(result)));
        result = (uint8_t)((result) | (1));
        *(uint8_t *)(arg1 + 0x40 + 0x24) = (uint8_t)(result);
    }
    if ((uint32_t)(local_r12) != 0) {
    }
    if ((uint32_t)(local_r13) != 0) goto loc_00658280;
    Arg3 = 0;
    result = ExpAddFastOwnerEntryToThreadList(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg1 + 64);
    goto loc_006582A5;
loc_00658280:
    result = KeAcquireSpinLockAtDpcLevel(*(uint64_t *)(gs_base + (0 + 0x188)) + 1736, Arg2, Arg3, Arg1 + 64);
    result = ExpAddFastOwnerEntryToThreadList(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, 1, Arg1 + 64);
    result = KxReleaseSpinLock(*(uint64_t *)(gs_base + (0 + 0x188)) + 1736, Arg2, 1, Arg1 + 64);
loc_006582A5:
    if ((uint32_t)(local_r12) == 0) goto loc_006582DF;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) == 0) goto loc_006582DE;
loc_006582C6:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_006582C6;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8)));
    if (!(condition_is_above_or_equal)) {
        result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg1 + 64);
    }
loc_006582DF:
    if ((uint32_t)(local_r13) == 0) goto loc_00658637;
    if ((uint8_t)(local_r14) == 0) goto loc_0065860F;
    if (result == 0) goto loc_0065860F;
    goto loc_0065860A;
loc_00658302:
    if ((*(uint64_t *)(arg1 + 0x40 + 0x10)) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00658324;
    if (result == 0) goto loc_00658637;
    result = KeAbPostReleaseEx(*(uint64_t *)(gs_base + (0 + 0x188)) + 1736, result, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg1 + 64);
    goto loc_00658637;
loc_00658324:
    if ((uint32_t)(local_r14) != 0) goto loc_0065833B;
    if (result == 0) goto loc_0065835C;
    result = KeAbPostReleaseEx(*(uint64_t *)(gs_base + (0 + 0x188)) + 1736, result, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg1 + 64);
    goto loc_0065835C;
loc_0065833B:
    v_stack_m38 = (uint32_t)(local_r12);
    result = ExpAcquireFastResourceExclusiveSlow(*(uint64_t *)(gs_base + (0 + 0x188)) + 1736, result, *(uint64_t *)(gs_base + (0 + 0x188)), result);
    goto loc_00658637;
loc_00658356:
    if ((((uint8_t)(local_r12)) & (6)) != 0) goto loc_00658364;
loc_0065835C:
    local_rdi = 0;
    goto loc_00658637;
loc_00658364:
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (8));
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (4));
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (16));
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_r10))));
    Arg3 = (uint8_t)((*(uint64_t *)(gs_base + (0 + 0x188))) + (2));
    if (((0) & ((uint8_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6C8 + 0x1A)))) == 0) {
        a4 = 0;
        Arg3 = *(uint64_t *)(gs_base + (0 + 0x188)) + 1736;
        Arg1 = 454;
        Arg2 = a4 + 3;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    if (((uint8_t)(v_cr8)) >= = ((uint8_t)(Arg3))) {
        Arg2 = 0;
        a4 = (uint8_t)(Arg3);
        Arg3 = (uint8_t)(v_cr8);
        Arg1 = 454;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    if (((uint8_t)(Arg1)) < 2) goto loc_00658406;
    result = (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x3A3C)));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x3A3C))))) & (0x10001ULL)) != 0) {
        a4 = 0;
        Arg3 = 0;
        Arg1 = 454;
        Arg2 = a4 + 5;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    if (((0) & (8)) != 0) goto loc_00658432;
    result = *(uint8_t *)(arg2 + 0xC0);
    if ((((uint8_t)(*(uint8_t *)(arg2 + 0xC0))) & (2)) != 0) {
        a4 = 0;
        Arg3 = 0;
        Arg1 = 454;
        Arg2 = a4 + 6;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    if (((uint8_t)(Arg1)) >= 0) goto loc_00658464;
    if (((*(uint32_t *)(arg2 + 0x74)) & (0x400ULL)) != 0) goto loc_00658464;
    if ((*(uint32_t *)(arg2 + 0x1E4)) == 0) {
        a4 = 0;
        Arg3 = 0;
        Arg1 = 454;
        Arg2 = a4 + 7;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    a4 = (*(uint64_t *)(result + 0x10)) & (-2);
    if (a4 != Arg2) {
        Arg3 = result;
        Arg2 = 9;
        Arg1 = 454;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    if ((((uint8_t)(*(uint8_t *)(result + 0x25))) & (2)) != 0) goto loc_006584B8;
    if (*(uint64_t *)(result + 0x18) == 0) goto loc_006584B8;
    result = *(uint8_t *)(result + 0x25);
    if ((*(uint64_t *)(result + 0x18)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 1736)) {
        Arg3 = result;
        Arg2 = 2;
        Arg1 = 454;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, *(uint64_t *)(result + 0x18));
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20))) == 0) goto loc_006584CE;
    if ((((uint8_t)(result)) & (4)) != 0) goto loc_006584CE;
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20)) + 1);
    goto loc_00658637;
loc_006584CE:
    Arg3 = 0;
    Arg3 = ((uint32_t)(local_r10) == 0) ? 1 : 0;
    local_rbp = 0;
    result = (uint32_t)(*(uint32_t *)(result + 0x20)) + 1;
    if ((*(uint8_t *)(result + 0x24)) == 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188)) + 1736;
        result = KeAbPreAcquire(Arg1, Arg2, Arg3, *(uint64_t *)(result + 0x18));
        local_rbp = result;
    }
    if (((0) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6C8)))) != 0) goto loc_0065861E;
    if ((uint32_t)(local_r14) != 0) goto loc_00658512;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6C8))) & (2)) != 0) goto loc_0065861E;
loc_00658512:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6C8) + 4) ^ (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6C8));
    Arg1 = (Arg1) & (-4);
    Arg1 = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6C8));
    if (condition_is_not_equal) goto loc_006584F6;
    local_r14 = 15 - 12;
    if ((uint32_t)(local_r13) != 0) { local_r14 = 15; }
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (2));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (4));
    local_r14 = (uint32_t)((local_r14) & (8));
    if (result != (*(uint64_t *)(gs_base + (0 + 0x188)) + 1736 + 64)) {
        *(uint64_t *)(result + 0x18) = *(uint64_t *)(gs_base + (0 + 0x188)) + 1736;
    }
    result = 0;
    *(uint32_t *)(result + 0x20) = 0;
    result = ((uint32_t)(local_r12) != 0) ? 1 : 0;
    result = (result) | (*(uint64_t *)(gs_base + (0 + 0x188)));
    *(uint64_t *)(result + 0x10) = result;
    if (local_rbp != 0) {
        result = *(uint8_t *)(local_rbp + 0x8);
        result = (uint8_t)((result) & (63));
        *(uint8_t *)(local_rbp + 0xA) = 0;
        result = (uint8_t)((result) + ((uint8_t)(result)));
        result = (uint8_t)((result) | (0));
        *(uint8_t *)(result + 0x24) = (uint8_t)(result);
    }
    if ((uint32_t)(local_r13) != 0) {
    }
    if ((uint32_t)(local_r12) != 0) goto loc_00658599;
    Arg3 = 0;
    result = ExpAddFastOwnerEntryToThreadList(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, result);
    goto loc_006585BE;
loc_00658599:
    result = KeAcquireSpinLockAtDpcLevel(*(uint64_t *)(gs_base + (0 + 0x188)) + 1736, Arg2, Arg3, result);
    result = ExpAddFastOwnerEntryToThreadList(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, 0, result);
    result = KxReleaseSpinLock(*(uint64_t *)(gs_base + (0 + 0x188)) + 1736, Arg2, 0, result);
loc_006585BE:
    if ((uint32_t)(local_r13) == 0) goto loc_006585F8;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) == 0) goto loc_006585F7;
loc_006585DF:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_006585DF;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8)));
    if (!(condition_is_above_or_equal)) {
        result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(gs_base + (0 + 0x20)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), result);
    }
loc_006585F8:
    if ((uint32_t)(local_r12) == 0) goto loc_00658637;
    if ((uint32_t)(local_r14) == 0) goto loc_0065860F;
    if (local_rbp == 0) goto loc_0065860F;
loc_0065860A:
    result = KeAbMarkCrossThreadReleasable(*(uint64_t *)(gs_base + (0 + 0x20)), local_rbp, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), result);
loc_0065860F:
    result = ObfReferenceObjectWithTag(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x746C6644ULL), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), result);
    goto loc_00658637;
loc_0065861E:
    v_stack_m38 = (uint32_t)(local_r12);
    result = ExpAcquireFastResourceSharedSlow(*(uint64_t *)(gs_base + (0 + 0x188)) + 1736, result, local_rbp, *(uint64_t *)(gs_base + (0 + 0x188)));
loc_00658637:
    local_rsp = (local_rsp) + (48);
    return (uint8_t)((uint8_t)(result));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x1A` | `16` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R/W` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg1` | `+ 0x24` | `8` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `W` |
| `Arg2` | `+ 0x24` | `8` | `R` |
| `Arg2` | `+ 0x25` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00658120&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
