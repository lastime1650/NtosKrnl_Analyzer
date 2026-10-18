# KeSetTracepoint

- RVA: `0x00747F80`–`0x007485A9` (길이 `1,577` bytes)
- VA: `0x0000000140747F80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB308`
- 디코드: `416`개 명령, `1,577/1,577` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x007480FE` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00748110` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0074818F` → [MmLockLoadedDataTableEntry](../../text/2A/MmLockLoadedDataTableEntry_function_002A437C.md) (function, `0x002A437C`)
- `0x007481B2` → [KiTpIsSupportedKernelTracepointLocation](KiTpIsSupportedKernelTracepointLocation_function_007488C8.md) (function, `0x007488C8`)
- `0x007481CA` → [KiTpCompletionContextSize](KiTpCompletionContextSize_function_0074899C.md) (function, `0x0074899C`)
- `0x007481DD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0074820F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00748234` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00748260` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00748293` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007482A3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0074835D` → [KiTpSetupCompletion](KiTpSetupCompletion_function_00748AC4.md) (function, `0x00748AC4`)
- `0x007483B4` → [KiTpSetupCompletion](KiTpSetupCompletion_function_00748AC4.md) (function, `0x00748AC4`)
- `0x0074844F` → [KiTpWriteBreakpoint](../../text/5C/KiTpWriteBreakpoint_function_005CAB18.md) (function, `0x005CAB18`)
- `0x007484E3` → [KiTpWriteBreakpoint](../../text/5C/KiTpWriteBreakpoint_function_005CAB18.md) (function, `0x005CAB18`)
- `0x00748560` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0074857D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00748589` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0074859F` → [MmUnlockLoadedDataTableEntry](../../text/2A/MmUnlockLoadedDataTableEntry_function_002A3C98.md) (function, `0x002A3C98`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00747F97` → RVA `0x00E0A740` (`.data`; read)
- `0x00747FF1` → RVA `0x00FC6C10` (`ALMOSTRO`; read)
- `0x007480E0` → RVA `0x00FC7400` (`ALMOSTRO`; read)
- `0x00748203` → RVA `0x00F10778` (`.data`; read)
- `0x00748214` → RVA `0x00F10778` (`.data`; read/write)
- `0x00748242` → RVA `0x00F107A0` (`.data`; read)
- `0x00748277` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x007482AF` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x007482D1` → RVA `0x00F107A0` (`.data`; write)
- `0x007483CA` → RVA `0x00F10780` (`.data`; read/write)
- `0x0074842A` → RVA `0x00F10788` (`.data`; read)
- `0x00748432` → RVA `0x00F10788` (`.data`; write)
- `0x0074843D` → RVA `0x00FC6D00` (`ALMOSTRO`; read/write)
- `0x00748473` → RVA `0x00F10788` (`.data`; read/write)
- `0x0074850A` → RVA `0x00F10784` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x007480FE` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00748110` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0074818F` → [MmLockLoadedDataTableEntry](../../text/2A/MmLockLoadedDataTableEntry_function_002A437C.md) (`PAGE` → `.text`)
  - `0x007481DD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0074820F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00748234` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00748260` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00748293` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007482A3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0074844F` → [KiTpWriteBreakpoint](../../text/5C/KiTpWriteBreakpoint_function_005CAB18.md) (`PAGE` → `.text`)
  - `0x007484E3` → [KiTpWriteBreakpoint](../../text/5C/KiTpWriteBreakpoint_function_005CAB18.md) (`PAGE` → `.text`)
  - `0x00748560` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0074857D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00748589` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0074859F` → [MmUnlockLoadedDataTableEntry](../../text/2A/MmUnlockLoadedDataTableEntry_function_002A3C98.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00747F80  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00747F85  55                              push rbp
00747F86  56                              push rsi
00747F87  57                              push rdi
00747F88  41 54                           push r12
00747F8A  41 55                           push r13
00747F8C  41 56                           push r14
00747F8E  41 57                           push r15
00747F90  48 81 EC A0 00 00 00            sub rsp, 0xa0
00747F97  48 8B 05 A2 27 6C 00            mov rax, qword ptr [rip + 0x6c27a2]
00747F9E  48 33 C4                        xor rax, rsp
00747FA1  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00747FA9  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
00747FB1  45 33 E4                        xor r12d, r12d
00747FB4  4C 21 64 24 40                  and qword ptr [rsp + 0x40], r12
00747FB9  48 83 CB FF                     or rbx, 0xffffffffffffffff
00747FBD  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00747FC2  48 8B F1                        mov rsi, rcx
00747FC5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00747FCE  49 8B F8                        mov rdi, r8
00747FD1  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00747FD6  45 8D 7C 24 01                  lea r15d, [r12 + 1]
00747FDB  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
00747FE0  45 8B E9                        mov r13d, r9d
00747FE3  45 33 C0                        xor r8d, r8d
00747FE6  40 8A EA                        mov bpl, dl
00747FE9  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
00747FF0  90                              nop
00747FF1  8B 05 19 EC 87 00               mov eax, dword ptr [rip + 0x87ec19]
00747FF7  8B C8                           mov ecx, eax
00747FF9  83 E1 02                        and ecx, 2
00747FFC  75 15                           jne 0x140748013
00747FFE  84 D2                           test dl, dl
00748000  74 07                           je 0x140748009
00748002  41 23 C7                        and eax, r15d
00748005  84 C0                           test al, al
00748007  75 0A                           jne 0x140748013
00748009  BF 22 00 00 C0                  mov edi, 0xc0000022
0074800E  E9 EB 00 00 00                  jmp 0x1407480fe
00748013  48 85 F6                        test rsi, rsi
00748016  75 09                           jne 0x140748021
00748018  40 84 ED                        test bpl, bpl
0074801B  0F 85 D8 00 00 00               jne 0x1407480f9
00748021  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
0074802B  48 3B F8                        cmp rdi, rax
0074802E  76 09                           jbe 0x140748039
00748030  41 3A EF                        cmp bpl, r15b
00748033  0F 84 C0 00 00 00               je 0x1407480f9
00748039  49 BA 00 00 00 00 00 80 FF FF   movabs r10, 0xffff800000000000
00748043  49 3B FA                        cmp rdi, r10
00748046  73 09                           jae 0x140748051
00748048  40 84 ED                        test bpl, bpl
0074804B  0F 84 A8 00 00 00               je 0x1407480f9
00748051  48 85 F6                        test rsi, rsi
00748054  74 1A                           je 0x140748070
00748056  48 8B 86 70 01 00 00            mov rax, qword ptr [rsi + 0x170]
0074805D  41 84 C7                        test r15b, al
00748060  75 05                           jne 0x140748067
00748062  48 85 C0                        test rax, rax
00748065  74 09                           je 0x140748070
00748067  40 84 ED                        test bpl, bpl
0074806A  75 9D                           jne 0x140748009
0074806C  85 C9                           test ecx, ecx
0074806E  74 99                           je 0x140748009
00748070  41 8D 41 FF                     lea eax, [r9 - 1]
00748074  41 3B C7                        cmp eax, r15d
00748077  76 0A                           jbe 0x140748083
00748079  45 33 F6                        xor r14d, r14d
0074807C  44 89 74 24 3C                  mov dword ptr [rsp + 0x3c], r14d
00748081  EB 0E                           jmp 0x140748091
00748083  44 89 7C 24 3C                  mov dword ptr [rsp + 0x3c], r15d
00748088  45 8B F7                        mov r14d, r15d
0074808B  41 83 FD 02                     cmp r13d, 2
0074808F  74 0A                           je 0x14074809b
00748091  41 83 FD 03                     cmp r13d, 3
00748095  74 04                           je 0x14074809b
00748097  33 C9                           xor ecx, ecx
00748099  EB 03                           jmp 0x14074809e
0074809B  41 8B CF                        mov ecx, r15d
0074809E  41 8D 41 FC                     lea eax, [r9 - 4]
007480A2  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
007480A6  41 3B C7                        cmp eax, r15d
007480A9  76 08                           jbe 0x1407480b3
007480AB  33 C0                           xor eax, eax
007480AD  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
007480B1  EB 0B                           jmp 0x1407480be
007480B3  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
007480B8  41 83 FD 05                     cmp r13d, 5
007480BC  74 0D                           je 0x1407480cb
007480BE  41 83 FD 06                     cmp r13d, 6
007480C2  74 07                           je 0x1407480cb
007480C4  44 21 44 24 34                  and dword ptr [rsp + 0x34], r8d
007480C9  EB 05                           jmp 0x1407480d0
007480CB  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
007480D0  85 C9                           test ecx, ecx
007480D2  0F 84 97 00 00 00               je 0x14074816f
007480D8  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
007480E0  4C 8D 0D 19 F3 87 00            lea r9, [rip + 0x87f319]
007480E7  48 85 C9                        test rcx, rcx
007480EA  75 45                           jne 0x140748131
007480EC  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
007480F4  48 85 C9                        test rcx, rcx
007480F7  75 5D                           jne 0x140748156
007480F9  BF 0D 00 00 C0                  mov edi, 0xc000000d
007480FE  E8 AD 57 B1 FF                  call 0x14025d8b0
00748103  8B C7                           mov eax, edi
00748105  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0074810D  48 33 CC                        xor rcx, rsp
00748110  E8 2B 45 F6 FF                  call 0x1406ac640
00748115  48 8B 9C 24 F8 00 00 00         mov rbx, qword ptr [rsp + 0xf8]
0074811D  48 81 C4 A0 00 00 00            add rsp, 0xa0
00748124  41 5F                           pop r15
00748126  41 5E                           pop r14
00748128  41 5D                           pop r13
0074812A  41 5C                           pop r12
0074812C  5F                              pop rdi
0074812D  5E                              pop rsi
0074812E  5D                              pop rbp
0074812F  C3                              ret
00748130  CC                              int3
00748131  B8 20 00 00 00                  mov eax, 0x20
00748136  40 84 ED                        test bpl, bpl
00748139  8D 50 10                        lea edx, [rax + 0x10]
0074813C  0F 45 C2                        cmovne eax, edx
0074813F  4A 3B 0C 08                     cmp rcx, qword ptr [rax + r9]
00748143  0F 85 C0 FE FF FF               jne 0x140748009
00748149  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
00748151  48 85 C9                        test rcx, rcx
00748154  74 31                           je 0x140748187
00748156  B8 28 00 00 00                  mov eax, 0x28
0074815B  40 84 ED                        test bpl, bpl
0074815E  8D 50 10                        lea edx, [rax + 0x10]
00748161  0F 45 C2                        cmovne eax, edx
00748164  4A 3B 0C 08                     cmp rcx, qword ptr [rax + r9]
00748168  74 1D                           je 0x140748187
0074816A  E9 9A FE FF FF                  jmp 0x140748009
0074816F  4C 39 84 24 00 01 00 00         cmp qword ptr [rsp + 0x100], r8
00748177  75 80                           jne 0x1407480f9
00748179  4C 39 84 24 10 01 00 00         cmp qword ptr [rsp + 0x110], r8
00748181  0F 85 72 FF FF FF               jne 0x1407480f9
00748187  49 3B FA                        cmp rdi, r10
0074818A  72 11                           jb 0x14074819d
0074818C  48 8B CF                        mov rcx, rdi
0074818F  E8 E8 C1 B5 FF                  call 0x1402a437c
00748194  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00748199  4C 8B 40 30                     mov r8, qword ptr [rax + 0x30]
0074819D  45 85 F6                        test r14d, r14d
007481A0  75 05                           jne 0x1407481a7
007481A2  45 85 ED                        test r13d, r13d
007481A5  75 59                           jne 0x140748200
007481A7  4D 85 C0                        test r8, r8
007481AA  74 19                           je 0x1407481c5
007481AC  48 8B D7                        mov rdx, rdi
007481AF  49 8B C8                        mov rcx, r8
007481B2  E8 11 07 00 00                  call 0x1407488c8
007481B7  85 C0                           test eax, eax
007481B9  75 0A                           jne 0x1407481c5
007481BB  BF BB 00 00 C0                  mov edi, 0xc00000bb
007481C0  E9 C9 03 00 00                  jmp 0x14074858e
007481C5  45 85 F6                        test r14d, r14d
007481C8  74 36                           je 0x140748200
007481CA  E8 CD 07 00 00                  call 0x14074899c
007481CF  B9 40 00 00 00                  mov ecx, 0x40
007481D4  41 B8 46 74 72 70               mov r8d, 0x70727446
007481DA  8D 50 34                        lea edx, [rax + 0x34]
007481DD  E8 0E 9F 43 00                  call 0x140b820f0
007481E2  4C 8B E0                        mov r12, rax
007481E5  48 85 C0                        test rax, rax
007481E8  75 0A                           jne 0x1407481f4
007481EA  BF 9A 00 00 C0                  mov edi, 0xc000009a
007481EF  E9 9A 03 00 00                  jmp 0x14074858e
007481F4  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
007481F8  40 88 68 32                     mov byte ptr [rax + 0x32], bpl
007481FC  48 89 78 08                     mov qword ptr [rax + 8], rdi
00748200  45 33 C0                        xor r8d, r8d
00748203  48 8D 0D 6E 85 7C 00            lea rcx, [rip + 0x7c856e]
0074820A  33 D2                           xor edx, edx
0074820C  49 8B F4                        mov rsi, r12
0074820F  E8 1C 80 AC FF                  call 0x140210230
00748214  F0 48 0F BA 2D 5A 85 7C 00 00   lock bts qword ptr [rip + 0x7c855a], 0
0074821E  48 8B F8                        mov rdi, rax
00748221  73 16                           jae 0x140748239
00748223  4C 8D 05 4E 85 7C 00            lea r8, [rip + 0x7c854e]
0074822A  48 8B D0                        mov rdx, rax
0074822D  48 8D 0D 44 85 7C 00            lea rcx, [rip + 0x7c8544]
00748234  E8 57 7A AC FF                  call 0x14020fc90
00748239  48 85 FF                        test rdi, rdi
0074823C  74 04                           je 0x140748242
0074823E  44 88 7F 0A                     mov byte ptr [rdi + 0xa], r15b
00748242  48 8B 3D 57 85 7C 00            mov rdi, qword ptr [rip + 0x7c8557]
00748249  48 85 FF                        test rdi, rdi
0074824C  0F 85 86 00 00 00               jne 0x1407482d8
00748252  BA 00 00 02 00                  mov edx, 0x20000
00748257  8D 4F 40                        lea ecx, [rdi + 0x40]
0074825A  41 B8 46 74 72 70               mov r8d, 0x70727446
00748260  E8 8B 9E 43 00                  call 0x140b820f0
00748265  48 8B F8                        mov rdi, rax
00748268  48 85 C0                        test rax, rax
0074826B  75 0A                           jne 0x140748277
0074826D  BF 9A 00 00 C0                  mov edi, 0xc000009a
00748272  E9 CE 02 00 00                  jmp 0x140748545
00748277  44 8B 35 02 E8 87 00            mov r14d, dword ptr [rip + 0x87e802]
0074827E  B9 40 00 00 00                  mov ecx, 0x40
00748283  49 69 D6 08 20 00 00            imul rdx, r14, 0x2008
0074828A  41 B8 46 74 72 70               mov r8d, 0x70727446
00748290  45 8B FE                        mov r15d, r14d
00748293  E8 58 9E 43 00                  call 0x140b820f0
00748298  48 8B D0                        mov rdx, rax
0074829B  48 85 C0                        test rax, rax
0074829E  75 0A                           jne 0x1407482aa
007482A0  48 8B CF                        mov rcx, rdi
007482A3  E8 C8 A5 43 00                  call 0x140b82870
007482A8  EB C3                           jmp 0x14074826d
007482AA  45 85 F6                        test r14d, r14d
007482AD  74 22                           je 0x1407482d1
007482AF  48 8D 0D 8A 09 88 00            lea rcx, [rip + 0x88098a]
007482B6  48 8B 01                        mov rax, qword ptr [rcx]
007482B9  48 8D 49 08                     lea rcx, [rcx + 8]
007482BD  48 89 90 98 00 00 00            mov qword ptr [rax + 0x98], rdx
007482C4  48 81 C2 08 20 00 00            add rdx, 0x2008
007482CB  49 83 EF 01                     sub r15, 1
007482CF  75 E5                           jne 0x1407482b6
007482D1  48 89 3D C8 84 7C 00            mov qword ptr [rip + 0x7c84c8], rdi
007482D8  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
007482DD  33 C0                           xor eax, eax
007482DF  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
007482E4  4D 8B F0                        mov r14, r8
007482E7  49 C1 EE 04                     shr r14, 4
007482EB  41 81 E6 FF 3F 00 00            and r14d, 0x3fff
007482F2  4E 8D 3C F7                     lea r15, [rdi + r14*8]
007482F6  33 FF                           xor edi, edi
007482F8  49 8B 0F                        mov rcx, qword ptr [r15]
007482FB  48 85 C9                        test rcx, rcx
007482FE  74 24                           je 0x140748324
00748300  4C 39 41 08                     cmp qword ptr [rcx + 8], r8
00748304  75 06                           jne 0x14074830c
00748306  4C 39 51 10                     cmp qword ptr [rcx + 0x10], r10
0074830A  74 05                           je 0x140748311
0074830C  4C 8B F9                        mov r15, rcx
0074830F  EB E7                           jmp 0x1407482f8
00748311  48 8B C1                        mov rax, rcx
00748314  40 38 69 32                     cmp byte ptr [rcx + 0x32], bpl
00748318  74 0A                           je 0x140748324
0074831A  BF 0D 00 00 C0                  mov edi, 0xc000000d
0074831F  E9 21 02 00 00                  jmp 0x140748545
00748324  45 85 ED                        test r13d, r13d
00748327  75 40                           jne 0x140748369
00748329  48 85 C0                        test rax, rax
0074832C  74 18                           je 0x140748346
0074832E  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00748333  48 85 C9                        test rcx, rcx
00748336  0F 84 09 02 00 00               je 0x140748545
0074833C  8A 40 33                        mov al, byte ptr [rax + 0x33]
0074833F  88 01                           mov byte ptr [rcx], al
00748341  E9 FF 01 00 00                  jmp 0x140748545
00748346  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0074834B  45 33 C9                        xor r9d, r9d
0074834E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00748353  40 8A D5                        mov dl, bpl
00748356  21 7C 24 20                     and dword ptr [rsp + 0x20], edi
0074835A  49 8B CA                        mov rcx, r10
0074835D  E8 62 07 00 00                  call 0x140748ac4
00748362  8B F8                           mov edi, eax
00748364  E9 DC 01 00 00                  jmp 0x140748545
00748369  39 7C 24 3C                     cmp dword ptr [rsp + 0x3c], edi
0074836D  0F 84 86 00 00 00               je 0x1407483f9
00748373  48 85 C0                        test rax, rax
00748376  74 1A                           je 0x140748392
00748378  40 38 78 18                     cmp byte ptr [rax + 0x18], dil
0074837C  75 0A                           jne 0x140748388
0074837E  40 38 78 19                     cmp byte ptr [rax + 0x19], dil
00748382  0F 84 85 00 00 00               je 0x14074840d
00748388  BF 18 07 00 C0                  mov edi, 0xc0000718
0074838D  E9 B3 01 00 00                  jmp 0x140748545
00748392  4D 8B 44 24 08                  mov r8, qword ptr [r12 + 8]
00748397  49 8D 44 24 34                  lea rax, [r12 + 0x34]
0074839C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007483A1  4D 8D 4C 24 33                  lea r9, [r12 + 0x33]
007483A6  40 8A D5                        mov dl, bpl
007483A9  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
007483B1  49 8B CA                        mov rcx, r10
007483B4  E8 0B 07 00 00                  call 0x140748ac4
007483B9  8B F8                           mov edi, eax
007483BB  85 C0                           test eax, eax
007483BD  0F 88 82 01 00 00               js 0x140748545
007483C3  48 8B 05 D6 83 7C 00            mov rax, qword ptr [rip + 0x7c83d6]
007483CA  FF 05 B0 83 7C 00               inc dword ptr [rip + 0x7c83b0]
007483D0  33 FF                           xor edi, edi
007483D2  4E 8D 3C F0                     lea r15, [rax + r14*8]
007483D6  49 8B 07                        mov rax, qword ptr [r15]
007483D9  49 89 04 24                     mov qword ptr [r12], rax
007483DD  4D 89 27                        mov qword ptr [r15], r12
007483E0  F0 09 3C 24                     lock or dword ptr [rsp], edi
007483E4  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
007483E8  8B C2                           mov eax, edx
007483EA  44 8B 6C 24 30                  mov r13d, dword ptr [rsp + 0x30]
007483EF  F7 D8                           neg eax
007483F1  48 1B C9                        sbb rcx, rcx
007483F4  4C 23 E1                        and r12, rcx
007483F7  EB 20                           jmp 0x140748419
007483F9  44 8B 6C 24 30                  mov r13d, dword ptr [rsp + 0x30]
007483FE  48 85 C0                        test rax, rax
00748401  75 0F                           jne 0x140748412
00748403  BF 25 02 00 C0                  mov edi, 0xc0000225
00748408  E9 38 01 00 00                  jmp 0x140748545
0074840D  44 8B 6C 24 30                  mov r13d, dword ptr [rsp + 0x30]
00748412  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
00748416  48 8B F0                        mov rsi, rax
00748419  4C 8D 76 30                     lea r14, [rsi + 0x30]
0074841D  85 D2                           test edx, edx
0074841F  0F 84 9A 00 00 00               je 0x1407484bf
00748425  41 38 3E                        cmp byte ptr [r14], dil
00748428  75 5A                           jne 0x140748484
0074842A  8B 05 58 83 7C 00               mov eax, dword ptr [rip + 0x7c8358]
00748430  FF C0                           inc eax
00748432  89 05 50 83 7C 00               mov dword ptr [rip + 0x7c8350], eax
00748438  83 F8 01                        cmp eax, 1
0074843B  75 08                           jne 0x140748445
0074843D  F0 83 0D BB E8 87 00 02         lock or dword ptr [rip + 0x87e8bb], 2
00748445  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
0074844A  B2 01                           mov dl, 1
0074844C  48 8B CE                        mov rcx, rsi
0074844F  E8 C4 26 E8 FF                  call 0x1405cab18
00748454  8B F8                           mov edi, eax
00748456  85 C0                           test eax, eax
00748458  79 24                           jns 0x14074847e
0074845A  83 CD FF                        or ebp, 0xffffffff
0074845D  49 3B F4                        cmp rsi, r12
00748460  75 11                           jne 0x140748473
00748462  48 8B 06                        mov rax, qword ptr [rsi]
00748465  49 89 07                        mov qword ptr [r15], rax
00748468  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0074846D  01 2D 0D 83 7C 00               add dword ptr [rip + 0x7c830d], ebp
00748473  01 2D 0F 83 7C 00               add dword ptr [rip + 0x7c830f], ebp
00748479  E9 C7 00 00 00                  jmp 0x140748545
0074847E  41 C6 06 01                     mov byte ptr [r14], 1
00748482  33 FF                           xor edi, edi
00748484  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
0074848C  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
00748490  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
00748498  48 89 46 28                     mov qword ptr [rsi + 0x28], rax
0074849C  F0 09 3C 24                     lock or dword ptr [rsp], edi
007484A0  48 39 BC 24 00 01 00 00         cmp qword ptr [rsp + 0x100], rdi
007484A8  4C 8B E7                        mov r12, rdi
007484AB  0F 95 C0                        setne al
007484AE  48 39 BC 24 10 01 00 00         cmp qword ptr [rsp + 0x110], rdi
007484B6  88 46 18                        mov byte ptr [rsi + 0x18], al
007484B9  0F 95 C0                        setne al
007484BC  88 46 19                        mov byte ptr [rsi + 0x19], al
007484BF  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
007484C3  83 CD FF                        or ebp, 0xffffffff
007484C6  85 C9                           test ecx, ecx
007484C8  74 05                           je 0x1407484cf
007484CA  41 38 3E                        cmp byte ptr [r14], dil
007484CD  75 0A                           jne 0x1407484d9
007484CF  45 85 ED                        test r13d, r13d
007484D2  74 48                           je 0x14074851c
007484D4  41 38 3E                        cmp byte ptr [r14], dil
007484D7  74 24                           je 0x1407484fd
007484D9  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
007484DE  33 D2                           xor edx, edx
007484E0  48 8B CE                        mov rcx, rsi
007484E3  E8 30 26 E8 FF                  call 0x1405cab18
007484E8  85 C0                           test eax, eax
007484EA  79 04                           jns 0x1407484f0
007484EC  8B CF                           mov ecx, edi
007484EE  EB 0D                           jmp 0x1407484fd
007484F0  01 2D 92 82 7C 00               add dword ptr [rip + 0x7c8292], ebp
007484F6  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
007484FA  41 88 3E                        mov byte ptr [r14], dil
007484FD  66 83 66 18 00                  and word ptr [rsi + 0x18], 0
00748502  F0 09 3C 24                     lock or dword ptr [rsp], edi
00748506  EB 02                           jmp 0x14074850a
00748508  F3 90                           pause
0074850A  8B 05 74 82 7C 00               mov eax, dword ptr [rip + 0x7c8274]
00748510  85 C0                           test eax, eax
00748512  75 F4                           jne 0x140748508
00748514  48 89 7E 20                     mov qword ptr [rsi + 0x20], rdi
00748518  48 89 7E 28                     mov qword ptr [rsi + 0x28], rdi
0074851C  85 C9                           test ecx, ecx
0074851E  74 14                           je 0x140748534
00748520  48 8B 06                        mov rax, qword ptr [rsi]
00748523  49 89 07                        mov qword ptr [r15], rax
00748526  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0074852B  01 2D 4F 82 7C 00               add dword ptr [rip + 0x7c824f], ebp
00748531  4C 8B E6                        mov r12, rsi
00748534  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00748539  48 85 C9                        test rcx, rcx
0074853C  74 05                           je 0x140748543
0074853E  8A 46 33                        mov al, byte ptr [rsi + 0x33]
00748541  88 01                           mov byte ptr [rcx], al
00748543  33 FF                           xor edi, edi
00748545  4D 85 E4                        test r12, r12
00748548  74 1B                           je 0x140748565
0074854A  EB 02                           jmp 0x14074854e
0074854C  F3 90                           pause
0074854E  8B 05 30 82 7C 00               mov eax, dword ptr [rip + 0x7c8230]
00748554  85 C0                           test eax, eax
00748556  75 F4                           jne 0x14074854c
00748558  BA 46 74 72 70                  mov edx, 0x70727446
0074855D  49 8B CC                        mov rcx, r12
00748560  E8 0B A3 43 00                  call 0x140b82870
00748565  F0 48 0F C1 1D 0A 82 7C 00      lock xadd qword ptr [rip + 0x7c820a], rbx
0074856E  80 E3 06                        and bl, 6
00748571  80 FB 02                        cmp bl, 2
00748574  75 0C                           jne 0x140748582
00748576  48 8D 0D FB 81 7C 00            lea rcx, [rip + 0x7c81fb]
0074857D  E8 4E D8 B1 FF                  call 0x140265dd0
00748582  48 8D 0D EF 81 7C 00            lea rcx, [rip + 0x7c81ef]
00748589  E8 72 90 B9 FF                  call 0x1402e1600
0074858E  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00748593  48 85 C0                        test rax, rax
00748596  0F 84 62 FB FF FF               je 0x1407480fe
0074859C  48 8B C8                        mov rcx, rax
0074859F  E8 F4 B6 B5 FF                  call 0x1402a3c98
007485A4  E9 55 FB FF FF                  jmp 0x1407480fe
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeSetTracepoint(__int64 a1, unsigned __int8 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned int v_stack_p3C;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 7088034)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r12 = 0;
    v_rbx = (v_rbx) | (-1);
    v_stack_m90 = a9;
    v_stack_m80 = a1;
    v_stack_m88 = a3;
    a3 = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8907801))))) & (2));
    if (condition_is_not_equal) goto loc_00748013;
    if (a2 == 0) goto loc_00748009;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 8907801))) & ((unsigned int)(v_r12 + 1)));
    if ((unsigned __int8)(result) != 0) goto loc_00748013;
loc_00748009:
    goto loc_007480FE;
loc_00748013:
    if (a1 != 0) goto loc_00748021;
    if (a2 != 0) goto loc_007480F9;
loc_00748021:
    if (((unsigned int)(0xC0000022ULL)) <= result) goto loc_00748039;
    if (a2 == ((unsigned __int8)(v_r12 + 1))) goto loc_007480F9;
loc_00748039:
    if (((unsigned int)(0xC0000022ULL)) >= v_r10) goto loc_00748051;
    if (a2 == 0) goto loc_007480F9;
loc_00748051:
    if (a1 == 0) goto loc_00748070;
    if ((((unsigned __int8)(v_r12 + 1)) & ((unsigned __int8)(*(unsigned __int64 *)(a1 + 368)))) != 0) goto loc_00748067;
    if (*(unsigned __int64 *)(a1 + 368) == 0) goto loc_00748070;
loc_00748067:
    if (a2 != 0) goto loc_00748009;
    if ((unsigned int)(a1) == 0) goto loc_00748009;
loc_00748070:
    if (((unsigned int)(a4 - 1)) <= ((unsigned int)(v_r12 + 1))) goto loc_00748083;
    v_r14 = 0;
    v_stack_m9C = 0;
    goto loc_00748091;
loc_00748083:
    v_stack_m9C = (unsigned int)(v_r12 + 1);
    if (((unsigned int)((unsigned int)((unsigned int)(a4)))) == 2) goto loc_0074809B;
loc_00748091:
    if (((unsigned int)((unsigned int)((unsigned int)(a4)))) == 3) goto loc_0074809B;
    a1 = 0;
    goto loc_0074809E;
loc_0074809B:
loc_0074809E:
    v_stack_mA0 = (unsigned int)((unsigned int)((unsigned int)(v_r12 + 1)));
    if (((unsigned int)(a4 - 4)) <= ((unsigned int)(v_r12 + 1))) goto loc_007480B3;
    result = 0;
    v_stack_mA8 = 0;
    goto loc_007480BE;
loc_007480B3:
    v_stack_mA8 = (unsigned int)(v_r12 + 1);
    if (((unsigned int)((unsigned int)((unsigned int)(a4)))) == 5) goto loc_007480CB;
loc_007480BE:
    if (((unsigned int)((unsigned int)((unsigned int)(a4)))) == 6) goto loc_007480CB;
    goto loc_007480D0;
loc_007480CB:
    v_stack_mA4 = (unsigned int)(v_r12 + 1);
loc_007480D0:
    if ((unsigned int)((unsigned int)((unsigned int)(v_r12 + 1))) == 0) goto loc_0074816F;
    if (a5 != 0) goto loc_00748131;
    if (a7 != 0) goto loc_00748156;
loc_007480F9:
loc_007480FE:
    result = KeLeaveCriticalRegion(a7, a2, a3, v_rip + 8909593);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, v_rip + 8909593);
    v_rsp = (v_rsp) + (160);
    return result;
loc_00748131:
    result = 32;
    if (a2 != 0) { result = (unsigned int)(32 + 16); }
    if (a1 != (*(unsigned __int64 *)(result + v_rip + 8909593 * 1))) goto loc_00748009;
    if (a7 == 0) goto loc_00748187;
loc_00748156:
    result = 40;
    if (a2 != 0) { result = (unsigned int)(40 + 16); }
    if (a7 == (*(unsigned __int64 *)(result + v_rip + 8909593 * 1))) goto loc_00748187;
    goto loc_00748009;
loc_0074816F:
    if (a5 != 0) goto loc_007480F9;
    if (a7 != 0) goto loc_007480F9;
loc_00748187:
    if (((unsigned int)(0xC000000DULL)) >= v_r10) {
        a1 = (unsigned int)(0xC000000DULL);
        result = MmLockLoadedDataTableEntry(a1, 40 + 16, a3, v_rip + 8909593);
        v_stack_p40 = result;
        a3 = *(unsigned __int64 *)(result + 48);
    }
    if ((unsigned int)((unsigned int)((unsigned int)(v_r12 + 1))) != 0) goto loc_007481A7;
    if ((unsigned int)((unsigned int)((unsigned int)(a4))) != 0) goto loc_00748200;
loc_007481A7:
    if (a3 == 0) goto loc_007481C5;
    result = KiTpIsSupportedKernelTracepointLocation(a3, (unsigned int)(0xC000000DULL), a3, v_rip + 8909593);
    if ((unsigned int)(result) != 0) goto loc_007481C5;
    goto loc_0074858E;
loc_007481C5:
    if ((unsigned int)((unsigned int)((unsigned int)(v_r12 + 1))) == 0) goto loc_00748200;
    result = KiTpCompletionContextSize(a3, (unsigned int)(0xC000000DULL), a3, v_rip + 8909593);
    result = ExAllocatePool2(64, result + 52, (unsigned int)(0x70727446ULL), v_rip + 8909593);
    if (result != 0) goto loc_007481F4;
    goto loc_0074858E;
loc_007481F4:
    *(unsigned __int64 *)(result + 16) = a1;
    *(unsigned __int8 *)(result + 50) = a2;
    *(unsigned __int64 *)(result + 8) = (unsigned int)(0xC000009AULL);
loc_00748200:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 8160622, a2, a3, v_rip + 8909593);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 8160590;
        a2 = result;
        a1 = v_rip + 8160580;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_rip + 8909593);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_r12 + 1);
    }
    if (*(unsigned __int64 *)(v_rip + 8160599) != 0) goto loc_007482D8;
    result = ExAllocatePool2(*(unsigned __int64 *)(v_rip + 8160599) + 64, (unsigned int)(0x20000ULL), (unsigned int)(0x70727446ULL), v_rip + 8909593);
    if (result != 0) goto loc_00748277;
loc_0074826D:
    goto loc_00748545;
loc_00748277:
    a2 = ((unsigned int)(0x20000ULL)) * ((unsigned int)(*(unsigned int *)(v_rip + 8906754)));
    result = ExAllocatePool2(64, a2, (unsigned int)(0x70727446ULL), v_rip + 8909593);
    if (result != 0) goto loc_007482AA;
    result = ExFreePoolWithTag((unsigned int)(0xC000009AULL), result, (unsigned int)(0x70727446ULL), v_rip + 8909593);
    goto loc_0074826D;
loc_007482AA:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8906754))) == 0) goto loc_007482D1;
loc_007482B6:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8915338) + 152) = result;
    a2 = (result) + (0x2008ULL);
    v_r15 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8906754))))) - (1);
    if (condition_is_not_equal) goto loc_007482B6;
loc_007482D1:
    *(unsigned __int64 *)(v_rip + 8160456) = (unsigned int)(0xC000009AULL);
loc_007482D8:
    result = 0;
    v_r14 = (v_stack_p50) >> (4);
    v_r14 = (unsigned int)((v_r14) & (0x3FFFULL));
    v_rdi = 0;
loc_007482F8:
    if (*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + v_r14 * 8) == 0) goto loc_00748324;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + v_r14 * 8) + 8)) != v_stack_p50) goto loc_0074830C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + v_r14 * 8) + 16)) == v_stack_p58) goto loc_00748311;
loc_0074830C:
    goto loc_007482F8;
loc_00748311:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + v_r14 * 8) + 50)) == a2) goto loc_00748324;
    goto loc_00748545;
loc_00748324:
    if ((unsigned int)((unsigned int)((unsigned int)(a4))) != 0) goto loc_00748369;
    if (*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + v_r14 * 8) == 0) goto loc_00748346;
    if (v_stack_p48 == 0) goto loc_00748545;
    *(unsigned __int8 *)(v_stack_p48) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + v_r14 * 8) + 51));
    goto loc_00748545;
loc_00748346:
    a4 = 0;
    v_stack_p28 = v_stack_p60;
    result = KiTpSetupCompletion(v_stack_p58, a2, v_stack_p50, a4);
    goto loc_00748545;
loc_00748369:
    if (v_stack_p3C == ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_007483F9;
    if (result == 0) goto loc_00748392;
    if ((*(unsigned __int8 *)(result + 24)) != ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_00748388;
    if ((*(unsigned __int8 *)(result + 25)) == ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_0074840D;
loc_00748388:
    goto loc_00748545;
loc_00748392:
    v_stack_p28 = result + 52;
    v_stack_p20 = 1;
    result = KiTpSetupCompletion(v_stack_p58, a2, *(unsigned __int64 *)(result + 8), result + 51);
    if (sign_flag) goto loc_00748545;
    v_rdi = 0;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8160214) + v_r14 * 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8160214) + v_r14 * 8) = result;
    result = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)(v_stack_p38)))));
    v_r12 = (result) & (v_stack_p58);
    goto loc_00748419;
loc_007483F9:
    if (result != 0) goto loc_00748412;
    goto loc_00748545;
loc_0074840D:
loc_00748412:
loc_00748419:
    if ((unsigned int)((unsigned int)(v_stack_p38)) == 0) goto loc_007484BF;
    if ((*(unsigned __int8 *)(result + 48)) != ((unsigned __int8)((unsigned int)(0xC0000225ULL)))) goto loc_00748484;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 8160088))) + 1);
    *(unsigned int *)(v_rip + 8160080) = (unsigned int)(result);
    if (((unsigned int)(result)) == 1) {
    }
    result = KiTpWriteBreakpoint(result, 1, v_stack_p40, result + 51);
    if (!sign_flag) goto loc_0074847E;
    v_rbp = (unsigned int)((a2) | (0xFFFFFFFFULL));
    if (result == v_r12) {
        result = *(unsigned __int64 *)(result);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8160214) + v_r14 * 8) = result;
    }
    goto loc_00748545;
loc_0074847E:
    *(unsigned __int8 *)(result + 48) = 1;
    v_rdi = 0;
loc_00748484:
    *(unsigned __int64 *)(result + 32) = a6;
    *(unsigned __int64 *)(result + 40) = a8;
    result = (a5 != 0) ? 1 : 0;
    *(unsigned __int8 *)(result + 24) = (unsigned __int8)(result);
    result = (a7 != 0) ? 1 : 0;
    *(unsigned __int8 *)(result + 25) = (unsigned __int8)(result);
loc_007484BF:
    v_rbp = (unsigned int)((v_rbp) | (0xFFFFFFFFULL));
    if ((unsigned int)((unsigned int)(v_stack_p34)) == 0) goto loc_007484CF;
    if ((*(unsigned __int8 *)(result + 48)) != 0) goto loc_007484D9;
loc_007484CF:
    if ((unsigned int)((unsigned int)(v_stack_p30)) == 0) goto loc_0074851C;
    if ((*(unsigned __int8 *)(result + 48)) == 0) goto loc_007484FD;
loc_007484D9:
    a2 = 0;
    result = KiTpWriteBreakpoint(result, a2, v_stack_p40, result + 51);
    if (!sign_flag) goto loc_007484F0;
    goto loc_007484FD;
loc_007484F0:
    *(unsigned __int8 *)(result + 48) = 0;
loc_007484FD:
    goto loc_0074850A;
loc_00748508:
loc_0074850A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8159860))) != 0) goto loc_00748508;
    *(unsigned __int64 *)(result + 32) = 0;
    *(unsigned __int64 *)(result + 40) = 0;
loc_0074851C:
    result = (unsigned int)(*(unsigned int *)(v_rip + 8159860));
    v_r12 = 0;
    if ((unsigned int)((unsigned int)(v_stack_p34)) != 0) {
        result = *(unsigned __int64 *)(result);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8160214) + v_r14 * 8) = result;
        v_r12 = result;
    }
    if (v_stack_p48 != 0) {
        result = *(unsigned __int8 *)(result + 51);
        *(unsigned __int8 *)(v_stack_p48) = (unsigned __int8)(result);
    }
    v_rdi = 0;
loc_00748545:
    if (v_r12 == 0) goto loc_00748565;
    goto loc_0074854E;
loc_0074854C:
loc_0074854E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8159792))) != 0) goto loc_0074854C;
    result = ExFreePoolWithTag(v_r12, (unsigned int)(0x70727446ULL), v_stack_p40, result + 51);
loc_00748565:
    v_rbx = (unsigned __int8)((v_stack_p20) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = v_rip + 8159739;
        result = ExfTryToWakePushLock(a1, (unsigned int)(0x70727446ULL), v_stack_p40, result + 51);
    }
    result = KeAbPostRelease(v_rip + 8159727, (unsigned int)(0x70727446ULL), v_stack_p40, result + 51);
loc_0074858E:
    if (v_stack_p40 == 0) goto loc_007480FE;
    result = MmUnlockLoadedDataTableEntry(v_stack_p40, (unsigned int)(0x70727446ULL), v_stack_p40, result + 51);
    goto loc_007480FE;
}
```

## 5. (Beta) C Style

```c
int64_t KeSetTracepoint(int64_t Arg1, uint8_t Arg2, int64_t Arg3, void *Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint32_t v_stack_p0;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint32_t v_stack_p3C;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x6C27A2)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r12 = 0;
    local_rbx = (local_rbx) | (-1);
    v_stack_m90 = Arg9;
    v_stack_m80 = Arg1;
    v_stack_m88 = Arg3;
    Arg3 = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x87EC19))))) & (2));
    if (condition_is_not_equal) goto loc_00748013;
    if (Arg2 == 0) goto loc_00748009;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x87EC19))) & ((uint32_t)(local_r12 + 1)));
    if ((uint8_t)(result) != 0) goto loc_00748013;
loc_00748009:
    goto loc_007480FE;
loc_00748013:
    if (Arg1 != 0) goto loc_00748021;
    if (Arg2 != 0) goto loc_007480F9;
loc_00748021:
    if (((uint32_t)(0xC0000022ULL)) <= result) goto loc_00748039;
    if (Arg2 == ((uint8_t)(local_r12 + 1))) goto loc_007480F9;
loc_00748039:
    if (((uint32_t)(0xC0000022ULL)) >= local_r10) goto loc_00748051;
    if (Arg2 == 0) goto loc_007480F9;
loc_00748051:
    if (Arg1 == 0) goto loc_00748070;
    if ((((uint8_t)(local_r12 + 1)) & ((uint8_t)(*(uint64_t *)(Arg1 + 0x170)))) != 0) goto loc_00748067;
    if (*(uint64_t *)(Arg1 + 0x170) == 0) goto loc_00748070;
loc_00748067:
    if (Arg2 != 0) goto loc_00748009;
    if ((uint32_t)(Arg1) == 0) goto loc_00748009;
loc_00748070:
    if (((uint32_t)(Arg4 - 1)) <= ((uint32_t)(local_r12 + 1))) goto loc_00748083;
    local_r14 = 0;
    v_stack_m9C = 0;
    goto loc_00748091;
loc_00748083:
    v_stack_m9C = (uint32_t)(local_r12 + 1);
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4)))) == 2) goto loc_0074809B;
loc_00748091:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4)))) == 3) goto loc_0074809B;
    Arg1 = 0;
    goto loc_0074809E;
loc_0074809B:
loc_0074809E:
    v_stack_mA0 = (uint32_t)((uint32_t)((uint32_t)(local_r12 + 1)));
    if (((uint32_t)(Arg4 - 4)) <= ((uint32_t)(local_r12 + 1))) goto loc_007480B3;
    result = 0;
    v_stack_mA8 = 0;
    goto loc_007480BE;
loc_007480B3:
    v_stack_mA8 = (uint32_t)(local_r12 + 1);
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4)))) == 5) goto loc_007480CB;
loc_007480BE:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4)))) == 6) goto loc_007480CB;
    goto loc_007480D0;
loc_007480CB:
    v_stack_mA4 = (uint32_t)(local_r12 + 1);
loc_007480D0:
    if ((uint32_t)((uint32_t)((uint32_t)(local_r12 + 1))) == 0) goto loc_0074816F;
    if (Arg5 != 0) goto loc_00748131;
    if (Arg7 != 0) goto loc_00748156;
loc_007480F9:
loc_007480FE:
    result = KeLeaveCriticalRegion(Arg7, Arg2, Arg3, v_rip + 8909593);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, v_rip + 8909593);
    local_rsp = (local_rsp) + (160);
    return result;
loc_00748131:
    result = 32;
    if (Arg2 != 0) { result = (uint32_t)(32 + 16); }
    if (Arg1 != (*(uint64_t *)(result + v_rip + 0x87F319 * 1))) goto loc_00748009;
    if (Arg7 == 0) goto loc_00748187;
loc_00748156:
    result = 40;
    if (Arg2 != 0) { result = (uint32_t)(40 + 16); }
    if (Arg7 == (*(uint64_t *)(result + v_rip + 0x87F319 * 1))) goto loc_00748187;
    goto loc_00748009;
loc_0074816F:
    if (Arg5 != 0) goto loc_007480F9;
    if (Arg7 != 0) goto loc_007480F9;
loc_00748187:
    if (((uint32_t)(0xC000000DULL)) >= local_r10) {
        Arg1 = (uint32_t)(0xC000000DULL);
        result = MmLockLoadedDataTableEntry(Arg1, 40 + 16, Arg3, v_rip + 8909593);
        v_stack_p40 = result;
        Arg3 = *(uint64_t *)(result + 0x30);
    }
    if ((uint32_t)((uint32_t)((uint32_t)(local_r12 + 1))) != 0) goto loc_007481A7;
    if ((uint32_t)((uint32_t)((uint32_t)(Arg4))) != 0) goto loc_00748200;
loc_007481A7:
    if (Arg3 == 0) goto loc_007481C5;
    result = KiTpIsSupportedKernelTracepointLocation(Arg3, (uint32_t)(0xC000000DULL), Arg3, v_rip + 8909593);
    if ((uint32_t)(result) != 0) goto loc_007481C5;
    goto loc_0074858E;
loc_007481C5:
    if ((uint32_t)((uint32_t)((uint32_t)(local_r12 + 1))) == 0) goto loc_00748200;
    result = KiTpCompletionContextSize(Arg3, (uint32_t)(0xC000000DULL), Arg3, v_rip + 8909593);
    result = ExAllocatePool2(64, result + 52, (uint32_t)(0x70727446ULL), v_rip + 8909593);
    if (result != 0) goto loc_007481F4;
    goto loc_0074858E;
loc_007481F4:
    *(uint64_t *)(result + 0x10) = Arg1;
    *(uint8_t *)(result + 0x32) = Arg2;
    *(uint64_t *)(result + 0x8) = (uint32_t)(0xC000009AULL);
loc_00748200:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 8160622, Arg2, Arg3, v_rip + 8909593);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 8160590;
        Arg2 = result;
        Arg1 = v_rip + 8160580;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_rip + 8909593);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_r12 + 1);
    }
    if (*(uint64_t *)(v_rip + 0x7C8557) != 0) goto loc_007482D8;
    result = ExAllocatePool2(*(uint64_t *)(v_rip + 0x7C8557) + 64, (uint32_t)(0x20000ULL), (uint32_t)(0x70727446ULL), v_rip + 8909593);
    if (result != 0) goto loc_00748277;
loc_0074826D:
    goto loc_00748545;
loc_00748277:
    Arg2 = ((uint32_t)(0x20000ULL)) * ((uint32_t)(*(uint32_t *)(v_rip + 0x87E802)));
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x70727446ULL), v_rip + 8909593);
    if (result != 0) goto loc_007482AA;
    result = ExFreePoolWithTag((uint32_t)(0xC000009AULL), result, (uint32_t)(0x70727446ULL), v_rip + 8909593);
    goto loc_0074826D;
loc_007482AA:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x87E802))) == 0) goto loc_007482D1;
loc_007482B6:
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x88098A) + 0x98) = result;
    Arg2 = (result) + (0x2008ULL);
    local_r15 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x87E802))))) - (1);
    if (condition_is_not_equal) goto loc_007482B6;
loc_007482D1:
    *(uint64_t *)(v_rip + 0x7C84C8) = (uint32_t)(0xC000009AULL);
loc_007482D8:
    result = 0;
    local_r14 = (v_stack_p50) >> (4);
    local_r14 = (uint32_t)((local_r14) & (0x3FFFULL));
    local_rdi = 0;
loc_007482F8:
    if (*(uint64_t *)((uint32_t)(0xC000009AULL) + local_r14 * 8) == 0) goto loc_00748324;
    if ((*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL) + local_r14 * 8) + 0x8)) != v_stack_p50) goto loc_0074830C;
    if ((*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL) + local_r14 * 8) + 0x10)) == v_stack_p58) goto loc_00748311;
loc_0074830C:
    goto loc_007482F8;
loc_00748311:
    if ((*(uint8_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL) + local_r14 * 8) + 0x32)) == Arg2) goto loc_00748324;
    goto loc_00748545;
loc_00748324:
    if ((uint32_t)((uint32_t)((uint32_t)(Arg4))) != 0) goto loc_00748369;
    if (*(uint64_t *)((uint32_t)(0xC000009AULL) + local_r14 * 8) == 0) goto loc_00748346;
    if (v_stack_p48 == 0) goto loc_00748545;
    *(uint8_t *)(v_stack_p48) = (uint8_t)(*(uint8_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL) + local_r14 * 8) + 0x33));
    goto loc_00748545;
loc_00748346:
    Arg4 = 0;
    v_stack_p28 = v_stack_p60;
    result = KiTpSetupCompletion(v_stack_p58, Arg2, v_stack_p50, Arg4);
    goto loc_00748545;
loc_00748369:
    if (v_stack_p3C == ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_007483F9;
    if (result == 0) goto loc_00748392;
    if ((*(uint8_t *)(result + 0x18)) != ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_00748388;
    if ((*(uint8_t *)(result + 0x19)) == ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_0074840D;
loc_00748388:
    goto loc_00748545;
loc_00748392:
    v_stack_p28 = result + 52;
    v_stack_p20 = 1;
    result = KiTpSetupCompletion(v_stack_p58, Arg2, *(uint64_t *)(result + 0x8), result + 51);
    if (sign_flag) goto loc_00748545;
    local_rdi = 0;
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x7C83D6) + local_r14 * 8);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x7C83D6) + local_r14 * 8) = result;
    result = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)(v_stack_p38)))));
    local_r12 = (result) & (v_stack_p58);
    goto loc_00748419;
loc_007483F9:
    if (result != 0) goto loc_00748412;
    goto loc_00748545;
loc_0074840D:
loc_00748412:
loc_00748419:
    if ((uint32_t)((uint32_t)(v_stack_p38)) == 0) goto loc_007484BF;
    if ((*(uint8_t *)(result + 0x30)) != ((uint8_t)((uint32_t)(0xC0000225ULL)))) goto loc_00748484;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x7C8358))) + 1);
    *(uint32_t *)(v_rip + 0x7C8350) = (uint32_t)(result);
    if (((uint32_t)(result)) == 1) {
    }
    result = KiTpWriteBreakpoint(result, 1, v_stack_p40, result + 51);
    if (!sign_flag) goto loc_0074847E;
    local_rbp = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    if (result == local_r12) {
        result = *(uint64_t *)(result);
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x7C83D6) + local_r14 * 8) = result;
    }
    goto loc_00748545;
loc_0074847E:
    *(uint8_t *)(result + 0x30) = 1;
    local_rdi = 0;
loc_00748484:
    *(uint64_t *)(result + 0x20) = Arg6;
    *(uint64_t *)(result + 0x28) = Arg8;
    result = (Arg5 != 0) ? 1 : 0;
    *(uint8_t *)(result + 0x18) = (uint8_t)(result);
    result = (Arg7 != 0) ? 1 : 0;
    *(uint8_t *)(result + 0x19) = (uint8_t)(result);
loc_007484BF:
    local_rbp = (uint32_t)((local_rbp) | (0xFFFFFFFFULL));
    if ((uint32_t)((uint32_t)(v_stack_p34)) == 0) goto loc_007484CF;
    if ((*(uint8_t *)(result + 0x30)) != 0) goto loc_007484D9;
loc_007484CF:
    if ((uint32_t)((uint32_t)(v_stack_p30)) == 0) goto loc_0074851C;
    if ((*(uint8_t *)(result + 0x30)) == 0) goto loc_007484FD;
loc_007484D9:
    Arg2 = 0;
    result = KiTpWriteBreakpoint(result, Arg2, v_stack_p40, result + 51);
    if (!sign_flag) goto loc_007484F0;
    goto loc_007484FD;
loc_007484F0:
    *(uint8_t *)(result + 0x30) = 0;
loc_007484FD:
    goto loc_0074850A;
loc_00748508:
loc_0074850A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7C8274))) != 0) goto loc_00748508;
    *(uint64_t *)(result + 0x20) = 0;
    *(uint64_t *)(result + 0x28) = 0;
loc_0074851C:
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x7C8274));
    local_r12 = 0;
    if ((uint32_t)((uint32_t)(v_stack_p34)) != 0) {
        result = *(uint64_t *)(result);
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x7C83D6) + local_r14 * 8) = result;
        local_r12 = result;
    }
    if (v_stack_p48 != 0) {
        result = *(uint8_t *)(result + 0x33);
        *(uint8_t *)(v_stack_p48) = (uint8_t)(result);
    }
    local_rdi = 0;
loc_00748545:
    if (local_r12 == 0) goto loc_00748565;
    goto loc_0074854E;
loc_0074854C:
loc_0074854E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7C8230))) != 0) goto loc_0074854C;
    result = ExFreePoolWithTag(local_r12, (uint32_t)(0x70727446ULL), v_stack_p40, result + 51);
loc_00748565:
    local_rbx = (uint8_t)((v_stack_p20) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = v_rip + 8159739;
        result = ExfTryToWakePushLock(Arg1, (uint32_t)(0x70727446ULL), v_stack_p40, result + 51);
    }
    result = KeAbPostRelease(v_rip + 8159727, (uint32_t)(0x70727446ULL), v_stack_p40, result + 51);
loc_0074858E:
    if (v_stack_p40 == 0) goto loc_007480FE;
    result = MmUnlockLoadedDataTableEntry(v_stack_p40, (uint32_t)(0x70727446ULL), v_stack_p40, result + 51);
    goto loc_007480FE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `- 0x4` | `32` | `R` |
| `Arg4` | `- 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00747F80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
