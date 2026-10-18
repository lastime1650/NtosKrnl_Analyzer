# KiChooseTargetProcessor

- RVA: `0x002556D8`–`0x002560BE` (길이 `2,534` bytes)
- VA: `0x00000001402556D8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000637E0`
- 디코드: `573`개 명령, `2,534/2,534` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00255783` → [KiTryLocalThreadSchedule](../3F/KiTryLocalThreadSchedule_function_003FDDA0.md) (function, `0x003FDDA0`)
- `0x0025579A` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x002557A4` → [KiIsIsolationUnitIdleByHandle](KiIsIsolationUnitIdleByHandle_function_00256C70.md) (function, `0x00256C70`)
- `0x002557D9` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00255815` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0025589E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002558B4` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x0025590F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00255975` → [RtlCopyVolatileMemory](../6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x00255984` → [KiReduceAffinityToRankListMinimums](../39/KiReduceAffinityToRankListMinimums_function_0039EFA0.md) (function, `0x0039EFA0`)
- `0x00255A43` → [KiSelectProcessorToPreempt](../42/KiSelectProcessorToPreempt_function_0042F9E0.md) (function, `0x0042F9E0`)
- `0x00255A5C` → [KiAcquirePrcbLocksForPreemptionAttempt](../30/KiAcquirePrcbLocksForPreemptionAttempt_function_0030EC40.md) (function, `0x0030EC40`)
- `0x00255ABE` → [KiIsIsolationUnitIdleByHandle](KiIsIsolationUnitIdleByHandle_function_00256C70.md) (function, `0x00256C70`)
- `0x00255B42` → [RtlCopyVolatileMemory](../6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x00255B4B` → [KeIsEmptyGroupMask](KeIsEmptyGroupMask_function_002553B0.md) (function, `0x002553B0`)
- `0x00255B5F` → [KeFindFirstSetRightGroupMask](KeFindFirstSetRightGroupMask_function_00256BE4.md) (function, `0x00256BE4`)
- `0x00255C6B` → [KiReduceByEffectiveIdleSmtSet](KiReduceByEffectiveIdleSmtSet_function_00256E00.md) (function, `0x00256E00`)
- `0x00255C84` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x00255CAD` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x00255D4D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00255DA9` → [KiFindRankBiasedIdleSmtSet](../3F/KiFindRankBiasedIdleSmtSet_function_003FE40C.md) (function, `0x003FE40C`)
- `0x00255DE3` → [KiReduceByEffectiveIdleSmtSet](KiReduceByEffectiveIdleSmtSet_function_00256E00.md) (function, `0x00256E00`)
- `0x00255E56` → [RtlCopyVolatileMemory](../6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x00255E5F` → [KeIsEmptyGroupMask](KeIsEmptyGroupMask_function_002553B0.md) (function, `0x002553B0`)
- `0x00255E73` → [KeFindFirstSetRightGroupMask](KeFindFirstSetRightGroupMask_function_00256BE4.md) (function, `0x00256BE4`)
- `0x00255EBE` → [RtlCopyVolatileMemory](../6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x00255ECD` → [KiReduceAffinityToRankListMinimums](../39/KiReduceAffinityToRankListMinimums_function_0039EFA0.md) (function, `0x0039EFA0`)
- `0x00255FC7` → [KiFindRankBiasedIdleSmtSet](../3F/KiFindRankBiasedIdleSmtSet_function_003FE40C.md) (function, `0x003FE40C`)
- `0x0025606A` → [KiIsIsolationUnitIdleByHandle](KiIsIsolationUnitIdleByHandle_function_00256C70.md) (function, `0x00256C70`)
- `0x00256083` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x0025609F` → [KiSelectCandidateProcessor](../43/KiSelectCandidateProcessor_function_00434690.md) (function, `0x00434690`)
- `0x002560A9` → [KiIsIsolationUnitIdleByHandle](KiIsIsolationUnitIdleByHandle_function_00256C70.md) (function, `0x00256C70`)

### Direct callers
- [sub_0025308F](Unknown_function_0025308F.md) at `0x0025334B`

### Static image references
- `0x002556F4` → RVA `0x00E0A740` (`.data`; read)
- `0x00255711` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x002557F5` → RVA `0x00FC6B38` (`ALMOSTRO`; read)
- `0x00255BD0` → RVA `0x00FC5084` (`ALMOSTRO`; read)
- `0x00255C0F` → RVA `0x00F231B8` (`.data`; read)
- `0x00255E9B` → RVA `0x00FC6D18` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x002557FF` → [sub_006D831E + 0x4AD](../6D/Unknown_function_006D831E.md) (`tail-transfer`)
  - `0x00255AF7` → [sub_006D831E + 0x37D](../6D/Unknown_function_006D831E.md) (`tail-transfer`)
  - `0x00255B7F` → [sub_006D831E](../6D/Unknown_function_006D831E.md) (`tail-transfer`)
  - `0x00255E91` → [sub_006D831E + 0x79](../6D/Unknown_function_006D831E.md) (`tail-transfer`)
  - `0x00256039` → [sub_006D831E + 0xF2](../6D/Unknown_function_006D831E.md) (`tail-transfer`)
  - `0x0025604C` → [sub_006D831E + 0xF2](../6D/Unknown_function_006D831E.md) (`tail-transfer`)
  - `0x00256052` → [sub_006D831E + 0xF5](../6D/Unknown_function_006D831E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002556D8  40 55                           push rbp
002556DA  53                              push rbx
002556DB  56                              push rsi
002556DC  57                              push rdi
002556DD  41 54                           push r12
002556DF  41 55                           push r13
002556E1  41 56                           push r14
002556E3  41 57                           push r15
002556E5  48 8D AC 24 48 FC FF FF         lea rbp, [rsp - 0x3b8]
002556ED  48 81 EC B8 04 00 00            sub rsp, 0x4b8
002556F4  48 8B 05 45 50 BB 00            mov rax, qword ptr [rip + 0xbb5045]
002556FB  48 33 C4                        xor rax, rsp
002556FE  48 89 85 A0 03 00 00            mov qword ptr [rbp + 0x3a0], rax
00255705  8B 82 4C 02 00 00               mov eax, dword ptr [rdx + 0x24c]
0025570B  4D 8B E0                        mov r12, r8
0025570E  8B 7A 78                        mov edi, dword ptr [rdx + 0x78]
00255711  4C 8D 05 E8 A8 DA FF            lea r8, [rip - 0x255718]
00255718  D1 EF                           shr edi, 1
0025571A  4C 8B FA                        mov r15, rdx
0025571D  4C 89 4D 80                     mov qword ptr [rbp - 0x80], r9
00255721  4C 8B E9                        mov r13, rcx
00255724  49 8B 9C C0 40 8C FC 00         mov rbx, qword ptr [r8 + rax*8 + 0xfc8c40]
0025572C  33 C0                           xor eax, eax
0025572E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00255733  83 E7 01                        and edi, 1
00255736  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0025573B  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0025573F  8A 85 20 04 00 00               mov al, byte ptr [rbp + 0x420]
00255745  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00255749  48 89 55 88                     mov qword ptr [rbp - 0x78], rdx
0025574D  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00255752  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
00255756  41 8B 87 18 02 00 00            mov eax, dword ptr [r15 + 0x218]
0025575D  4D 8B CC                        mov r9, r12
00255760  0F BA F0 1F                     btr eax, 0x1f
00255764  49 8B CD                        mov rcx, r13
00255767  4D 8B B4 C0 40 8C FC 00         mov r14, qword ptr [r8 + rax*8 + 0xfc8c40]
0025576F  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00255774  49 8B D6                        mov rdx, r14
00255777  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0025577C  4D 8B C7                        mov r8, r15
0025577F  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
00255783  E8 18 86 1A 00                  call 0x1403fdda0
00255788  48 8B F0                        mov rsi, rax
0025578B  48 85 C0                        test rax, rax
0025578E  74 63                           je 0x1402557f3
00255790  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00255795  8B D7                           mov edx, edi
00255797  48 8B CE                        mov rcx, rsi
0025579A  E8 C1 95 0B 00                  call 0x14030ed60
0025579F  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
002557A4  E8 C7 14 00 00                  call 0x140256c70
002557A9  85 C0                           test eax, eax
002557AB  0F 84 CE 04 00 00               je 0x140255c7f
002557B1  F6 46 23 10                     test byte ptr [rsi + 0x23], 0x10
002557B5  0F 85 C4 04 00 00               jne 0x140255c7f
002557BB  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
002557BF  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002557C4  48 89 01                        mov qword ptr [rcx], rax
002557C7  48 C7 41 08 01 00 00 00         mov qword ptr [rcx + 8], 1
002557CF  48 8B 8D A0 03 00 00            mov rcx, qword ptr [rbp + 0x3a0]
002557D6  48 33 CC                        xor rcx, rsp
002557D9  E8 62 6E 45 00                  call 0x1406ac640
002557DE  48 81 C4 B8 04 00 00            add rsp, 0x4b8
002557E5  41 5F                           pop r15
002557E7  41 5E                           pop r14
002557E9  41 5D                           pop r13
002557EB  41 5C                           pop r12
002557ED  5F                              pop rdi
002557EE  5E                              pop rsi
002557EF  5B                              pop rbx
002557F0  5D                              pop rbp
002557F1  C3                              ret
002557F2  CC                              int3
002557F3  33 D2                           xor edx, edx
002557F5  F7 05 39 13 D7 00 00 00 80 00   test dword ptr [rip + 0xd71339], 0x800000
002557FF  0F 84 C6 2F 48 00               je 0x1406d87cb
00255805  41 BF 00 01 00 00               mov r15d, 0x100
0025580B  48 8D 8D 88 00 00 00            lea rcx, [rbp + 0x88]
00255812  45 8B C7                        mov r8d, r15d
00255815  E8 26 14 47 00                  call 0x1406c6c40
0025581A  49 8B 95 C0 00 00 00            mov rdx, qword ptr [r13 + 0xc0]
00255821  4C 8D 0D D8 A7 DA FF            lea r9, [rip - 0x255828]
00255828  48 8B 9B C0 00 00 00            mov rbx, qword ptr [rbx + 0xc0]
0025582F  48 8D 8D 88 00 00 00            lea rcx, [rbp + 0x88]
00255836  4D 8B B6 C0 00 00 00            mov r14, qword ptr [r14 + 0xc0]
0025583D  45 33 C0                        xor r8d, r8d
00255840  4C 89 45 A8                     mov qword ptr [rbp - 0x58], r8
00255844  41 8B F0                        mov esi, r8d
00255847  4C 89 45 F0                     mov qword ptr [rbp - 0x10], r8
0025584B  45 8B C7                        mov r8d, r15d
0025584E  0F B7 83 8A 00 00 00            movzx eax, word ptr [rbx + 0x8a]
00255855  48 89 55 98                     mov qword ptr [rbp - 0x68], rdx
00255859  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
0025585E  48 C7 85 80 00 00 00 01 00 20 00  mov qword ptr [rbp + 0x80], 0x200001
00255869  49 8B 84 C1 C0 F6 FC 00         mov rax, qword ptr [r9 + rax*8 + 0xfcf6c0]
00255871  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00255875  41 0F B7 86 8A 00 00 00         movzx eax, word ptr [r14 + 0x8a]
0025587D  49 8B 84 C1 C0 F6 FC 00         mov rax, qword ptr [r9 + rax*8 + 0xfcf6c0]
00255885  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00255889  0F B7 82 8A 00 00 00            movzx eax, word ptr [rdx + 0x8a]
00255890  33 D2                           xor edx, edx
00255892  49 8B 84 C1 C0 F6 FC 00         mov rax, qword ptr [r9 + rax*8 + 0xfcf6c0]
0025589A  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0025589E  E8 9D 13 47 00                  call 0x1406c6c40
002558A3  0F B7 95 82 00 00 00            movzx edx, word ptr [rbp + 0x82]
002558AA  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
002558B1  4D 8B C4                        mov r8, r12
002558B4  E8 A7 8F 07 00                  call 0x1402ce860
002558B9  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
002558BE  49 3B DE                        cmp rbx, r14
002558C1  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
002558C5  0F 57 C0                        xorps xmm0, xmm0
002558C8  48 0F 44 75 C8                  cmove rsi, qword ptr [rbp - 0x38]
002558CD  33 C0                           xor eax, eax
002558CF  48 89 45 08                     mov qword ptr [rbp + 8], rax
002558D3  45 33 DB                        xor r11d, r11d
002558D6  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
002558DA  41 8B DB                        mov ebx, r11d
002558DD  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
002558E1  0F B6 40 0A                     movzx eax, byte ptr [rax + 0xa]
002558E5  C1 E8 03                        shr eax, 3
002558E8  83 E0 01                        and eax, 1
002558EB  3B C7                           cmp eax, edi
002558ED  0F 4F F8                        cmovg edi, eax
002558F0  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
002558F4  89 45 90                        mov dword ptr [rbp - 0x70], eax
002558F7  4C 39 5C 24 68                  cmp qword ptr [rsp + 0x68], r11
002558FC  0F 84 22 02 00 00               je 0x140255b24
00255902  33 D2                           xor edx, edx
00255904  48 8D 8D A0 02 00 00            lea rcx, [rbp + 0x2a0]
0025590B  44 8D 42 40                     lea r8d, [rdx + 0x40]
0025590F  E8 2C 13 47 00                  call 0x1406c6c40
00255914  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00255919  45 33 DB                        xor r11d, r11d
0025591C  41 0F B7 80 88 00 00 00         movzx eax, word ptr [r8 + 0x88]
00255924  66 41 3B 04 24                  cmp ax, word ptr [r12]
00255929  0F 83 A3 03 00 00               jae 0x140255cd2
0025592F  49 8B 4C C4 08                  mov rcx, qword ptr [r12 + rax*8 + 8]
00255934  49 8B 78 08                     mov rdi, qword ptr [r8 + 8]
00255938  48 63 44 24 34                  movsxd rax, dword ptr [rsp + 0x34]
0025593D  49 8B 5C C0 10                  mov rbx, qword ptr [r8 + rax*8 + 0x10]
00255942  48 23 DF                        and rbx, rdi
00255945  48 23 D9                        and rbx, rcx
00255948  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
0025594D  0F 84 A4 06 00 00               je 0x140255ff7
00255953  41 F6 80 B8 00 00 00 01         test byte ptr [r8 + 0xb8], 1
0025595B  0F 85 D1 02 00 00               jne 0x140255c32
00255961  49 8D 90 40 02 00 00            lea rdx, [r8 + 0x240]
00255968  41 B8 40 00 00 00               mov r8d, 0x40
0025596E  48 8D 8D A0 02 00 00            lea rcx, [rbp + 0x2a0]
00255975  E8 56 70 46 00                  call 0x1406bc9d0
0025597A  48 8D 95 A0 02 00 00            lea rdx, [rbp + 0x2a0]
00255981  48 8B CB                        mov rcx, rbx
00255984  E8 17 96 14 00                  call 0x14039efa0
00255989  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0025598E  45 33 DB                        xor r11d, r11d
00255991  4C 8B C0                        mov r8, rax
00255994  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00255999  48 85 83 C8 00 00 00            test qword ptr [rbx + 0xc8], rax
002559A0  0F 84 DE 01 00 00               je 0x140255b84
002559A6  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
002559AB  48 85 DB                        test rbx, rbx
002559AE  0F 84 48 01 00 00               je 0x140255afc
002559B4  8B 7C 24 40                     mov edi, dword ptr [rsp + 0x40]
002559B8  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
002559BC  48 85 DB                        test rbx, rbx
002559BF  75 43                           jne 0x140255a04
002559C1  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
002559C6  49 3B D6                        cmp rdx, r14
002559C9  0F 85 2C 03 00 00               jne 0x140255cfb
002559CF  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
002559D3  48 3B C2                        cmp rax, rdx
002559D6  0F 85 36 06 00 00               jne 0x140256012
002559DC  41 0F B7 CB                     movzx ecx, r11w
002559E0  BE 01 00 00 00                  mov esi, 1
002559E5  66 3B 8D 80 00 00 00            cmp cx, word ptr [rbp + 0x80]
002559EC  73 16                           jae 0x140255a04
002559EE  0F B7 C1                        movzx eax, cx
002559F1  4C 39 9C C5 88 00 00 00         cmp qword ptr [rbp + rax*8 + 0x88], r11
002559F9  0F 85 E9 00 00 00               jne 0x140255ae8
002559FF  66 03 CE                        add cx, si
00255A02  EB E1                           jmp 0x1402559e5
00255A04  48 8B F3                        mov rsi, rbx
00255A07  48 85 DB                        test rbx, rbx
00255A0A  0F 85 47 06 00 00               jne 0x140256057
00255A10  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00255A15  0F B6 81 D0 00 00 00            movzx eax, byte ptr [rcx + 0xd0]
00255A1C  66 41 3B 04 24                  cmp ax, word ptr [r12]
00255A21  0F 83 A3 02 00 00               jae 0x140255cca
00255A27  0F AE E8                        lfence
00255A2A  49 8B 74 C4 08                  mov rsi, qword ptr [r12 + rax*8 + 8]
00255A2F  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
00255A33  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
00255A37  48 8B D1                        mov rdx, rcx
00255A3A  49 8B CF                        mov rcx, r15
00255A3D  45 33 C9                        xor r9d, r9d
00255A40  4C 8B C6                        mov r8, rsi
00255A43  E8 98 9F 1D 00                  call 0x14042f9e0
00255A48  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00255A4D  8B D7                           mov edx, edi
00255A4F  48 8B C8                        mov rcx, rax
00255A52  48 8B D8                        mov rbx, rax
00255A55  4C 8B B0 C0 00 00 00            mov r14, qword ptr [rax + 0xc0]
00255A5C  E8 DF 91 0B 00                  call 0x14030ec40
00255A61  33 C0                           xor eax, eax
00255A63  38 85 20 04 00 00               cmp byte ptr [rbp + 0x420], al
00255A69  0F 85 F6 05 00 00               jne 0x140256065
00255A6F  4D 8B 5E 08                     mov r11, qword ptr [r14 + 8]
00255A73  48 63 4C 24 34                  movsxd rcx, dword ptr [rsp + 0x34]
00255A78  49 8B 54 CE 10                  mov rdx, qword ptr [r14 + rcx*8 + 0x10]
00255A7D  4C 23 DA                        and r11, rdx
00255A80  4C 85 DE                        test rsi, r11
00255A83  0F 85 1F 02 00 00               jne 0x140255ca8
00255A89  F6 43 23 10                     test byte ptr [rbx + 0x23], 0x10
00255A8D  74 2A                           je 0x140255ab9
00255A8F  45 33 F6                        xor r14d, r14d
00255A92  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
00255A96  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
00255A9A  44 89 76 08                     mov dword ptr [rsi + 8], r14d
00255A9E  F6 43 23 10                     test byte ptr [rbx + 0x23], 0x10
00255AA2  0F 85 D6 05 00 00               jne 0x14025607e
00255AA8  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00255AAD  48 89 06                        mov qword ptr [rsi], rax
00255AB0  44 89 76 0C                     mov dword ptr [rsi + 0xc], r14d
00255AB4  E9 16 FD FF FF                  jmp 0x1402557cf
00255AB9  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00255ABE  E8 AD 11 00 00                  call 0x140256c70
00255AC3  45 33 F6                        xor r14d, r14d
00255AC6  85 C0                           test eax, eax
00255AC8  74 C8                           je 0x140255a92
00255ACA  48 89 75 80                     mov qword ptr [rbp - 0x80], rsi
00255ACE  48 8D 45 80                     lea rax, [rbp - 0x80]
00255AD2  4C 89 5D 80                     mov qword ptr [rbp - 0x80], r11
00255AD6  41 8D 4E 21                     lea ecx, [r14 + 0x21]
00255ADA  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00255ADE  48 8D 45 80                     lea rax, [rbp - 0x80]
00255AE2  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00255AE6  CD 29                           int 0x29
00255AE8  0F B7 82 8A 00 00 00            movzx eax, word ptr [rdx + 0x8a]
00255AEF  66 89 45 A8                     mov word ptr [rbp - 0x58], ax
00255AF3  44 89 5D AC                     mov dword ptr [rbp - 0x54], r11d
00255AF7  E9 9F 2B 48 00                  jmp 0x1406d869b
00255AFC  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00255B01  41 0F B7 80 88 00 00 00         movzx eax, word ptr [r8 + 0x88]
00255B09  49 8B 88 80 00 00 00            mov rcx, qword ptr [r8 + 0x80]
00255B10  66 39 85 80 00 00 00            cmp word ptr [rbp + 0x80], ax
00255B17  76 0B                           jbe 0x140255b24
00255B19  48 F7 D1                        not rcx
00255B1C  48 21 8C C5 88 00 00 00         and qword ptr [rbp + rax*8 + 0x88], rcx
00255B24  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00255B28  48 8D 4D 00                     lea rcx, [rbp]
00255B2C  0F 57 C0                        xorps xmm0, xmm0
00255B2F  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00255B33  41 B8 10 00 00 00               mov r8d, 0x10
00255B39  F3 0F 7F 45 00                  movdqu xmmword ptr [rbp], xmm0
00255B3E  48 8D 50 10                     lea rdx, [rax + 0x10]
00255B42  E8 89 6E 46 00                  call 0x1406bc9d0
00255B47  48 8D 4D 00                     lea rcx, [rbp]
00255B4B  E8 60 F8 FF FF                  call 0x1402553b0
00255B50  45 33 DB                        xor r11d, r11d
00255B53  85 C0                           test eax, eax
00255B55  0F 85 9F 02 00 00               jne 0x140255dfa
00255B5B  48 8D 4D 00                     lea rcx, [rbp]
00255B5F  E8 80 10 00 00                  call 0x140256be4
00255B64  0F B7 C8                        movzx ecx, ax
00255B67  48 8D 45 00                     lea rax, [rbp]
00255B6B  48 0F B3 08                     btr qword ptr [rax], rcx
00255B6F  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
00255B73  48 8B 7C C8 20                  mov rdi, qword ptr [rax + rcx*8 + 0x20]
00255B78  48 3B 7C 24 68                  cmp rdi, qword ptr [rsp + 0x68]
00255B7D  74 C8                           je 0x140255b47
00255B7F  E9 9A 27 48 00                  jmp 0x1406d831e
00255B84  48 85 F6                        test rsi, rsi
00255B87  74 0D                           je 0x140255b96
00255B89  4C 85 86 C8 00 00 00            test qword ptr [rsi + 0xc8], r8
00255B90  0F 85 27 01 00 00               jne 0x140255cbd
00255B96  48 8B 83 60 8E 00 00            mov rax, qword ptr [rbx + 0x8e60]
00255B9D  49 23 C0                        and rax, r8
00255BA0  75 48                           jne 0x140255bea
00255BA2  48 85 F6                        test rsi, rsi
00255BA5  74 0C                           je 0x140255bb3
00255BA7  48 8B 86 60 8E 00 00            mov rax, qword ptr [rsi + 0x8e60]
00255BAE  49 23 C0                        and rax, r8
00255BB1  75 37                           jne 0x140255bea
00255BB3  49 8B C0                        mov rax, r8
00255BB6  48 23 83 78 8E 00 00            and rax, qword ptr [rbx + 0x8e78]
00255BBD  75 2B                           jne 0x140255bea
00255BBF  48 85 F6                        test rsi, rsi
00255BC2  74 0C                           je 0x140255bd0
00255BC4  49 8B C0                        mov rax, r8
00255BC7  48 23 86 60 8E 00 00            and rax, qword ptr [rsi + 0x8e60]
00255BCE  75 1A                           jne 0x140255bea
00255BD0  8B 05 AE F4 D6 00               mov eax, dword ptr [rip + 0xd6f4ae]
00255BD6  A8 01                           test al, 1
00255BD8  74 18                           je 0x140255bf2
00255BDA  49 8B C0                        mov rax, r8
00255BDD  48 23 83 70 8E 00 00            and rax, qword ptr [rbx + 0x8e70]
00255BE4  0F 84 F0 00 00 00               je 0x140255cda
00255BEA  4C 8B C0                        mov r8, rax
00255BED  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00255BF2  0F B6 8B D1 00 00 00            movzx ecx, byte ptr [rbx + 0xd1]
00255BF9  0F B6 93 D0 00 00 00            movzx edx, byte ptr [rbx + 0xd0]
00255C00  49 D3 C8                        ror r8, cl
00255C03  49 0F BC C0                     bsf rax, r8
00255C07  C1 E2 06                        shl edx, 6
00255C0A  03 C8                           add ecx, eax
00255C0C  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00255C0F  48 8B 05 A2 D5 CC 00            mov rax, qword ptr [rip + 0xccd5a2]
00255C16  83 E1 3F                        and ecx, 0x3f
00255C19  03 D1                           add edx, ecx
00255C1B  48 8D 0D DE A3 DA FF            lea rcx, [rip - 0x255c22]
00255C22  8B 04 90                        mov eax, dword ptr [rax + rdx*4]
00255C25  48 8B 9C C1 40 8C FC 00         mov rbx, qword ptr [rcx + rax*8 + 0xfc8c40]
00255C2D  E9 74 FD FF FF                  jmp 0x1402559a6
00255C32  44 38 5C 24 30                  cmp byte ptr [rsp + 0x30], r11b
00255C37  0F 85 82 03 00 00               jne 0x140255fbf
00255C3D  49 8B 48 18                     mov rcx, qword ptr [r8 + 0x18]
00255C41  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00255C46  48 23 CB                        and rcx, rbx
00255C49  75 4A                           jne 0x140255c95
00255C4B  44 38 5C 24 30                  cmp byte ptr [rsp + 0x30], r11b
00255C50  0F 85 A1 03 00 00               jne 0x140255ff7
00255C56  4D 39 85 C0 00 00 00            cmp qword ptr [r13 + 0xc0], r8
00255C5D  0F 85 FE FC FF FF               jne 0x140255961
00255C63  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00255C68  49 8B CD                        mov rcx, r13
00255C6B  E8 90 11 00 00                  call 0x140256e00
00255C70  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00255C75  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00255C7A  E9 E2 FC FF FF                  jmp 0x140255961
00255C7F  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00255C84  E8 C7 3F 14 00                  call 0x140399c50
00255C89  4C 8D 05 70 A3 DA FF            lea r8, [rip - 0x255c90]
00255C90  E9 C1 FA FF FF                  jmp 0x140255756
00255C95  44 38 5C 24 30                  cmp byte ptr [rsp + 0x30], r11b
00255C9A  0F 85 46 03 00 00               jne 0x140255fe6
00255CA0  48 8B D9                        mov rbx, rcx
00255CA3  E9 B9 FC FF FF                  jmp 0x140255961
00255CA8  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00255CAD  E8 9E 3F 14 00                  call 0x140399c50
00255CB2  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
00255CB6  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00255CBB  EB CC                           jmp 0x140255c89
00255CBD  8B 7C 24 40                     mov edi, dword ptr [rsp + 0x40]
00255CC1  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
00255CC5  E9 92 03 00 00                  jmp 0x14025605c
00255CCA  49 8B F3                        mov rsi, r11
00255CCD  E9 61 FD FF FF                  jmp 0x140255a33
00255CD2  49 8B CB                        mov rcx, r11
00255CD5  E9 5A FC FF FF                  jmp 0x140255934
00255CDA  48 85 F6                        test rsi, rsi
00255CDD  0F 84 0F FF FF FF               je 0x140255bf2
00255CE3  49 8B C0                        mov rax, r8
00255CE6  48 23 86 70 8E 00 00            and rax, qword ptr [rsi + 0x8e70]
00255CED  4C 0F 45 C0                     cmovne r8, rax
00255CF1  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00255CF6  E9 F7 FE FF FF                  jmp 0x140255bf2
00255CFB  33 C0                           xor eax, eax
00255CFD  0F 57 C0                        xorps xmm0, xmm0
00255D00  F7 05 2E 0E D7 00 00 00 80 00   test dword ptr [rip + 0xd70e2e], 0x800000
00255D0A  49 8B DB                        mov rbx, r11
00255D0D  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
00255D11  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00255D15  0F 84 D7 00 00 00               je 0x140255df2
00255D1B  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00255D1F  BE 01 00 00 00                  mov esi, 1
00255D24  F6 40 0A 08                     test byte ptr [rax + 0xa], 8
00255D28  0F 84 C4 00 00 00               je 0x140255df2
00255D2E  3B F7                           cmp esi, edi
00255D30  0F 4F FE                        cmovg edi, esi
00255D33  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
00255D37  4D 85 F6                        test r14, r14
00255D3A  0F 84 F8 00 00 00               je 0x140255e38
00255D40  33 D2                           xor edx, edx
00255D42  48 8D 8D E0 02 00 00            lea rcx, [rbp + 0x2e0]
00255D49  44 8D 42 40                     lea r8d, [rdx + 0x40]
00255D4D  E8 EE 0E 47 00                  call 0x1406c6c40
00255D52  41 0F B7 86 88 00 00 00         movzx eax, word ptr [r14 + 0x88]
00255D5A  45 33 DB                        xor r11d, r11d
00255D5D  66 41 3B 04 24                  cmp ax, word ptr [r12]
00255D62  0F 83 97 02 00 00               jae 0x140255fff
00255D68  49 8B 4C C4 08                  mov rcx, qword ptr [r12 + rax*8 + 8]
00255D6D  49 8B 7E 08                     mov rdi, qword ptr [r14 + 8]
00255D71  48 63 44 24 34                  movsxd rax, dword ptr [rsp + 0x34]
00255D76  49 8B 5C C6 10                  mov rbx, qword ptr [r14 + rax*8 + 0x10]
00255D7B  48 23 DF                        and rbx, rdi
00255D7E  48 23 D9                        and rbx, rcx
00255D81  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00255D86  0F 84 86 00 00 00               je 0x140255e12
00255D8C  41 F6 86 B8 00 00 00 01         test byte ptr [r14 + 0xb8], 1
00255D94  0F 84 10 01 00 00               je 0x140255eaa
00255D9A  44 38 5C 24 30                  cmp byte ptr [rsp + 0x30], r11b
00255D9F  74 14                           je 0x140255db5
00255DA1  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00255DA6  49 8B CE                        mov rcx, r14
00255DA9  E8 5E 86 1A 00                  call 0x1403fe40c
00255DAE  45 33 DB                        xor r11d, r11d
00255DB1  84 C0                           test al, al
00255DB3  75 33                           jne 0x140255de8
00255DB5  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
00255DB9  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00255DBE  48 23 CB                        and rcx, rbx
00255DC1  0F 85 99 01 00 00               jne 0x140255f60
00255DC7  44 38 5C 24 30                  cmp byte ptr [rsp + 0x30], r11b
00255DCC  75 44                           jne 0x140255e12
00255DCE  4D 39 B5 C0 00 00 00            cmp qword ptr [r13 + 0xc0], r14
00255DD5  0F 85 CF 00 00 00               jne 0x140255eaa
00255DDB  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00255DE0  49 8B CD                        mov rcx, r13
00255DE3  E8 18 10 00 00                  call 0x140256e00
00255DE8  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00255DED  E9 B8 00 00 00                  jmp 0x140255eaa
00255DF2  41 8B F3                        mov esi, r11d
00255DF5  E9 34 FF FF FF                  jmp 0x140255d2e
00255DFA  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
00255DFD  3B 44 24 40                     cmp eax, dword ptr [rsp + 0x40]
00255E01  0F 8E AD FB FF FF               jle 0x1402559b4
00255E07  FF C8                           dec eax
00255E09  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00255E0D  E9 E2 FA FF FF                  jmp 0x1402558f4
00255E12  49 8B DB                        mov rbx, r11
00255E15  41 0F B7 86 88 00 00 00         movzx eax, word ptr [r14 + 0x88]
00255E1D  49 8B 8E 80 00 00 00            mov rcx, qword ptr [r14 + 0x80]
00255E24  66 39 85 80 00 00 00            cmp word ptr [rbp + 0x80], ax
00255E2B  76 0B                           jbe 0x140255e38
00255E2D  48 F7 D1                        not rcx
00255E30  48 21 8C C5 88 00 00 00         and qword ptr [rbp + rax*8 + 0x88], rcx
00255E38  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00255E3C  48 8D 4D 18                     lea rcx, [rbp + 0x18]
00255E40  0F 57 C0                        xorps xmm0, xmm0
00255E43  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00255E47  41 B8 10 00 00 00               mov r8d, 0x10
00255E4D  F3 0F 7F 45 18                  movdqu xmmword ptr [rbp + 0x18], xmm0
00255E52  48 8D 50 10                     lea rdx, [rax + 0x10]
00255E56  E8 75 6B 46 00                  call 0x1406bc9d0
00255E5B  48 8D 4D 18                     lea rcx, [rbp + 0x18]
00255E5F  E8 4C F5 FF FF                  call 0x1402553b0
00255E64  45 33 DB                        xor r11d, r11d
00255E67  85 C0                           test eax, eax
00255E69  0F 85 3F 01 00 00               jne 0x140255fae
00255E6F  48 8D 4D 18                     lea rcx, [rbp + 0x18]
00255E73  E8 6C 0D 00 00                  call 0x140256be4
00255E78  0F B7 C8                        movzx ecx, ax
00255E7B  48 8D 45 18                     lea rax, [rbp + 0x18]
00255E7F  48 0F B3 08                     btr qword ptr [rax], rcx
00255E83  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
00255E87  48 8B 7C C8 20                  mov rdi, qword ptr [rax + rcx*8 + 0x20]
00255E8C  49 3B FE                        cmp rdi, r14
00255E8F  74 CA                           je 0x140255e5b
00255E91  E9 01 25 48 00                  jmp 0x1406d8397
00255E96  F3 48 0F B8 C7                  popcnt rax, rdi
00255E9B  3B 05 77 0E D7 00               cmp eax, dword ptr [rip + 0xd70e77]
00255EA1  0F 82 6B FF FF FF               jb 0x140255e12
00255EA7  48 8B D9                        mov rbx, rcx
00255EAA  49 8D 96 40 02 00 00            lea rdx, [r14 + 0x240]
00255EB1  41 B8 40 00 00 00               mov r8d, 0x40
00255EB7  48 8D 8D E0 02 00 00            lea rcx, [rbp + 0x2e0]
00255EBE  E8 0D 6B 46 00                  call 0x1406bc9d0
00255EC3  48 8D 95 E0 02 00 00            lea rdx, [rbp + 0x2e0]
00255ECA  48 8B CB                        mov rcx, rbx
00255ECD  E8 CE 90 14 00                  call 0x14039efa0
00255ED2  4C 8B 4D C8                     mov r9, qword ptr [rbp - 0x38]
00255ED6  48 8B D0                        mov rdx, rax
00255ED9  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00255EDE  49 85 81 C8 00 00 00            test qword ptr [r9 + 0xc8], rax
00255EE5  0F 85 1C 01 00 00               jne 0x140256007
00255EEB  4D 8B 81 60 8E 00 00            mov r8, qword ptr [r9 + 0x8e60]
00255EF2  4C 23 C0                        and r8, rax
00255EF5  74 79                           je 0x140255f70
00255EF7  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
00255EFC  41 0F B6 89 D1 00 00 00         movzx ecx, byte ptr [r9 + 0xd1]
00255F04  45 33 DB                        xor r11d, r11d
00255F07  41 0F B6 91 D0 00 00 00         movzx edx, byte ptr [r9 + 0xd0]
00255F0F  49 D3 C8                        ror r8, cl
00255F12  49 0F BC C0                     bsf rax, r8
00255F16  C1 E2 06                        shl edx, 6
00255F19  03 C8                           add ecx, eax
00255F1B  89 45 DC                        mov dword ptr [rbp - 0x24], eax
00255F1E  48 8B 05 93 D2 CC 00            mov rax, qword ptr [rip + 0xccd293]
00255F25  83 E1 3F                        and ecx, 0x3f
00255F28  03 D1                           add edx, ecx
00255F2A  48 8D 0D CF A0 DA FF            lea rcx, [rip - 0x255f31]
00255F31  8B 04 90                        mov eax, dword ptr [rax + rdx*4]
00255F34  48 8B 9C C1 40 8C FC 00         mov rbx, qword ptr [rcx + rax*8 + 0xfc8c40]
00255F3C  48 85 DB                        test rbx, rbx
00255F3F  0F 84 D0 FE FF FF               je 0x140255e15
00255F45  8B 7C 24 40                     mov edi, dword ptr [rsp + 0x40]
00255F49  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
00255F4D  48 85 DB                        test rbx, rbx
00255F50  0F 85 AE FA FF FF               jne 0x140255a04
00255F56  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00255F5B  E9 6F FA FF FF                  jmp 0x1402559cf
00255F60  44 38 5C 24 30                  cmp byte ptr [rsp + 0x30], r11b
00255F65  0F 84 3C FF FF FF               je 0x140255ea7
00255F6B  E9 26 FF FF FF                  jmp 0x140255e96
00255F70  4D 8B 81 78 8E 00 00            mov r8, qword ptr [r9 + 0x8e78]
00255F77  4C 23 C2                        and r8, rdx
00255F7A  0F 85 77 FF FF FF               jne 0x140255ef7
00255F80  8B 05 FE F0 D6 00               mov eax, dword ptr [rip + 0xd6f0fe]
00255F86  4C 8B C2                        mov r8, rdx
00255F89  A8 01                           test al, 1
00255F8B  0F 84 6B FF FF FF               je 0x140255efc
00255F91  49 8B 81 70 8E 00 00            mov rax, qword ptr [r9 + 0x8e70]
00255F98  48 23 C2                        and rax, rdx
00255F9B  0F 84 5B FF FF FF               je 0x140255efc
00255FA1  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00255FA6  4C 8B C0                        mov r8, rax
00255FA9  E9 4E FF FF FF                  jmp 0x140255efc
00255FAE  3B 74 24 40                     cmp esi, dword ptr [rsp + 0x40]
00255FB2  7E 91                           jle 0x140255f45
00255FB4  FF CE                           dec esi
00255FB6  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
00255FBA  E9 78 FD FF FF                  jmp 0x140255d37
00255FBF  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00255FC4  49 8B C8                        mov rcx, r8
00255FC7  E8 40 84 1A 00                  call 0x1403fe40c
00255FCC  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00255FD1  45 33 DB                        xor r11d, r11d
00255FD4  84 C0                           test al, al
00255FD6  0F 84 61 FC FF FF               je 0x140255c3d
00255FDC  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00255FE1  E9 7B F9 FF FF                  jmp 0x140255961
00255FE6  F3 48 0F B8 C7                  popcnt rax, rdi
00255FEB  3B 05 27 0D D7 00               cmp eax, dword ptr [rip + 0xd70d27]
00255FF1  0F 83 A9 FC FF FF               jae 0x140255ca0
00255FF7  49 8B DB                        mov rbx, r11
00255FFA  E9 02 FB FF FF                  jmp 0x140255b01
00255FFF  49 8B CB                        mov rcx, r11
00256002  E9 66 FD FF FF                  jmp 0x140255d6d
00256007  49 8B D9                        mov rbx, r9
0025600A  45 33 DB                        xor r11d, r11d
0025600D  E9 2A FF FF FF                  jmp 0x140255f3c
00256012  49 3B C6                        cmp rax, r14
00256015  0F 84 C1 F9 FF FF               je 0x1402559dc
0025601B  33 C0                           xor eax, eax
0025601D  4C 89 5D E8                     mov qword ptr [rbp - 0x18], r11
00256021  F7 05 0D 0B D7 00 00 00 80 00   test dword ptr [rip + 0xd70b0d], 0x800000
0025602B  0F 57 C0                        xorps xmm0, xmm0
0025602E  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
00256032  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00256036  49 8B DB                        mov rbx, r11
00256039  0F 84 D1 23 48 00               je 0x1406d8410
0025603F  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00256043  BE 01 00 00 00                  mov esi, 1
00256048  F6 40 0A 08                     test byte ptr [rax + 0xa], 8
0025604C  0F 84 BE 23 48 00               je 0x1406d8410
00256052  E9 BC 23 48 00                  jmp 0x1406d8413
00256057  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0025605C  4C 8B 7D 88                     mov r15, qword ptr [rbp - 0x78]
00256060  E9 2B F7 FF FF                  jmp 0x140255790
00256065  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0025606A  E8 01 0C 00 00                  call 0x140256c70
0025606F  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
00256073  45 33 F6                        xor r14d, r14d
00256076  89 46 08                        mov dword ptr [rsi + 8], eax
00256079  E9 20 FA FF FF                  jmp 0x140255a9e
0025607E  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00256083  E8 C8 3B 14 00                  call 0x140399c50
00256088  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0025608D  44 8B CF                        mov r9d, edi
00256090  49 83 C8 FF                     or r8, 0xffffffffffffffff
00256094  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00256099  49 8B D7                        mov rdx, r15
0025609C  48 8B CB                        mov rcx, rbx
0025609F  E8 EC E5 1D 00                  call 0x140434690
002560A4  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
002560A9  E8 C2 0B 00 00                  call 0x140256c70
002560AE  41 8B CE                        mov ecx, r14d
002560B1  85 C0                           test eax, eax
002560B3  0F 95 C1                        setne cl
002560B6  89 4E 08                        mov dword ptr [rsi + 8], ecx
002560B9  E9 EA F9 FF FF                  jmp 0x140255aa8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiChooseTargetProcessor(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m370;
    unsigned __int16 v_stack_m376;
    unsigned __int64 v_stack_m378;
    unsigned __int64 v_stack_m3C0;
    unsigned __int64 v_stack_m3D0;
    unsigned __int64 v_stack_m3D8;
    unsigned __int64 v_stack_m3E0;
    unsigned __int64 v_stack_m3E8;
    unsigned __int64 v_stack_m3F0;
    unsigned __int64 v_stack_m3F8;
    unsigned __int64 v_stack_m400;
    unsigned __int64 v_stack_m408;
    unsigned __int64 v_stack_m410;
    unsigned int v_stack_m41C;
    unsigned int v_stack_m420;
    unsigned __int64 v_stack_m430;
    unsigned __int64 v_stack_m438;
    unsigned __int64 v_stack_m440;
    unsigned __int64 v_stack_m448;
    unsigned int v_stack_m44C;
    unsigned __int64 v_stack_m450;
    unsigned __int64 v_stack_m458;
    unsigned __int64 v_stack_m460;
    unsigned int v_stack_m468;
    unsigned __int64 v_stack_m470;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m4A8;
    unsigned __int64 v_stack_m4B0;
    unsigned int v_stack_m4C0;
    unsigned int v_stack_m4C4;
    unsigned __int64 v_stack_m4C8;
    unsigned __int64 v_stack_m4D8;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;

    v_rsp = (v_rsp) - (0x4B8ULL);
    result = (*(unsigned __int64 *)(v_rip + 12275781)) ^ (v_rsp);
    v_stack_m58 = result;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 120))) >> (1));
    v_stack_m478 = a4;
    result = 0;
    v_stack_m4C8 = 0;
    v_rdi = (unsigned int)((v_rdi) & (1));
    v_stack_m4A8 = 0;
    v_stack_m4C0 = 0;
    v_stack_m4C8 = a5;
    v_stack_m470 = a2;
    v_stack_m4B0 = *(unsigned __int64 *)(v_rip - 2447128 + (unsigned int)(*(unsigned int *)(a2 + 588)) * 8 + 16550976);
    v_stack_m4C4 = (unsigned int)(v_rdi);
loc_00255756:
    v_stack_m4D8 = v_stack_m4C8;
    v_stack_m430 = *(unsigned __int64 *)(v_rip - 2447128 + (unsigned int)(*(unsigned int *)(a2 + 536)) * 8 + 16550976);
    result = KiTryLocalThreadSchedule(a1, *(unsigned __int64 *)(v_rip - 2447128 + (unsigned int)(*(unsigned int *)(a2 + 536)) * 8 + 16550976), a2, a3);
    if (result == 0) goto loc_002557F3;
loc_00255790:
    result = KiAcquirePrcbLocksForIsolationUnit(result, (unsigned int)((unsigned int)(v_rdi)), v_stack_m4A8, a3);
    result = KiIsIsolationUnitIdleByHandle(v_stack_m4A8, (unsigned int)((unsigned int)(v_rdi)), v_stack_m4A8, a3);
    if ((unsigned int)(result) == 0) goto loc_00255C7F;
    if (((*(unsigned __int8 *)(result + 35)) & (16)) != 0) goto loc_00255C7F;
    *(unsigned __int64 *)(v_stack_m478) = v_stack_m4A8;
    *(unsigned __int64 *)(v_stack_m478 + 8) = 1;
loc_002557CF:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)((unsigned int)(v_rdi)), v_stack_m4A8, a3);
    v_rsp = (v_rsp) + (0x4B8ULL);
    return result;
loc_002557F3:
    a2 = 0;
    result = memset(v_stack_m370, a2, 256, a3);
    a3 = 0;
    v_stack_m450 = 0;
    v_stack_m408 = 0;
    v_stack_m460 = *(unsigned __int64 *)(a1 + 192);
    v_stack_p68 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2447128 + (unsigned int)(*(unsigned int *)(a2 + 588)) * 8 + 16550976) + 192);
    v_stack_m378 = 0x200001ULL;
    v_stack_m438 = *(unsigned __int64 *)(v_rip - 2447400 + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2447128 + (unsigned int)(*(unsigned int *)(a2 + 588)) * 8 + 16550976) + 192) + 138) * 8 + 16578240);
    v_stack_m440 = *(unsigned __int64 *)(v_rip - 2447400 + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2447128 + (unsigned int)(*(unsigned int *)(a2 + 536)) * 8 + 16550976) + 192) + 138) * 8 + 16578240);
    a2 = 0;
    v_stack_m448 = *(unsigned __int64 *)(v_rip - 2447400 + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 192) + 138) * 8 + 16578240);
    result = memset(v_stack_m370, a2, 256, v_rip - 2447400);
    result = KiCopyAffinityEx(v_stack_m378, v_stack_m376, 0, v_rip - 2447400);
    v_stack_p40 = (unsigned int)(v_rdi);
    v_rsi = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2447128 + (unsigned int)(*(unsigned int *)(a2 + 588)) * 8 + 16550976) + 192)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2447128 + (unsigned int)(*(unsigned int *)(a2 + 536)) * 8 + 16550976) + 192))) { v_rsi = v_stack_m430; }
    result = 0;
    v_stack_m3F0 = 0;
    v_r11 = 0;
    v_stack_m400 = v_xmm0;
    result = (unsigned int)((*(unsigned __int8 *)(v_stack_m438 + 10)) >> (3));
    result = (unsigned int)((result) & (1));
    if (((unsigned int)(result)) > ((unsigned int)(v_rdi))) { v_rdi = (unsigned int)(result); }
    v_stack_p34 = (unsigned int)(v_rdi);
loc_002558F4:
    v_stack_m468 = (unsigned int)(result);
    if (v_stack_p68 == 0) goto loc_00255B24;
    a2 = 0;
    result = memset(v_stack_m158, a2, a2 + 64, v_rip - 2447400);
    v_r11 = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_p68 + 136))) >= (*(unsigned __int16 *)(a3))) goto loc_00255CD2;
loc_00255934:
    v_rbx = (*(unsigned __int64 *)(v_stack_p68 + (int)(v_stack_p34) * 8 + 16)) & (*(unsigned __int64 *)(v_stack_p68 + 8));
    v_rbx = (v_rbx) & (*(unsigned __int64 *)(a3 + *(unsigned __int16 *)(v_stack_p68 + 136) * 8 + 8));
    v_stack_p58 = v_rbx;
    if (condition_is_equal) goto loc_00255FF7;
    if (((*(unsigned __int8 *)(v_stack_p68 + 184)) & (1)) != 0) goto loc_00255C32;
loc_00255961:
    result = RtlCopyVolatileMemory(v_stack_m158, v_stack_p68 + 576, 64, v_rip - 2447400);
    result = KiReduceAffinityToRankListMinimums(v_rbx, v_stack_m158, 64, v_rip - 2447400);
    v_r11 = 0;
    v_stack_p58 = result;
    if (((*(unsigned __int64 *)(v_stack_p48 + 200)) & (result)) == 0) goto loc_00255B84;
loc_002559A6:
    if (v_stack_p48 == 0) goto loc_00255AFC;
loc_002559B4:
    v_stack_p34 = (unsigned int)((unsigned int)(v_stack_p40));
    if (v_stack_p48 != 0) goto loc_00255A04;
    if (v_stack_p68 != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2447128 + (unsigned int)(*(unsigned int *)(a2 + 536)) * 8 + 16550976) + 192))) goto loc_00255CFB;
loc_002559CF:
    if (v_stack_m460 != v_stack_p68) goto loc_00256012;
loc_002559DC:
loc_002559E5:
    if (0 >= v_stack_m378) goto loc_00255A04;
    if ((*(unsigned __int64 *)(v_stack_m3F8 + 0 * 8 + 136)) != 0) goto loc_00255AE8;
    a1 = (unsigned __int16)((0) + (1));
    goto loc_002559E5;
loc_00255A04:
    if (v_stack_p48 != 0) goto loc_00256057;
    if (((unsigned __int16)(*(unsigned __int8 *)(v_stack_p48 + 208))) >= (*(unsigned __int16 *)(a3))) goto loc_00255CCA;
loc_00255A33:
    a4 = 0;
    result = KiSelectProcessorToPreempt(v_stack_m470, v_stack_p48, *(unsigned __int64 *)(a3 + *(unsigned __int8 *)(v_stack_p48 + 208) * 8 + 8), a4);
    result = KiAcquirePrcbLocksForPreemptionAttempt(result, (unsigned int)((unsigned int)((unsigned int)(v_stack_p34))), v_stack_p50, a4);
    result = 0;
    if (a5 != 0) goto loc_00256065;
    v_r11 = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 192) + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 192) + (int)(v_stack_p34) * 8 + 16));
    if (((*(unsigned __int64 *)(a3 + *(unsigned __int8 *)(v_stack_p48 + 208) * 8 + 8)) & (v_r11)) != 0) goto loc_00255CA8;
    if (((*(unsigned __int8 *)(result + 35)) & (16)) == 0) goto loc_00255AB9;
    v_r14 = 0;
loc_00255A92:
    *(unsigned int *)(v_stack_m478 + 8) = 0;
loc_00255A9E:
    if (((*(unsigned __int8 *)(result + 35)) & (16)) != 0) goto loc_0025607E;
loc_00255AA8:
    *(unsigned __int64 *)(v_stack_m478) = v_stack_p50;
    *(unsigned int *)(v_stack_m478 + 12) = 0;
    goto loc_002557CF;
loc_00255AB9:
    result = KiIsIsolationUnitIdleByHandle(v_stack_p50, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 192) + (int)(v_stack_p34) * 8 + 16), v_stack_p50, a4);
    v_r14 = 0;
    if ((unsigned int)(result) == 0) goto loc_00255A92;
    v_stack_m478 = v_stack_m478;
    v_stack_m478 = v_r11;
    v_stack_m458 = v_stack_m478;
    v_stack_m458 = v_stack_m478;
loc_00255AE8:
    v_stack_m450 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 192) + (int)(v_stack_p34) * 8 + 16) + 138));
    v_stack_m44C = (unsigned int)(v_r11);
loc_00255AFC:
loc_00255B01:
    if (v_stack_m378 >= = ((unsigned __int16)(*(unsigned __int16 *)(v_stack_p68 + 136)))) {
        a1 = ~(*(unsigned __int64 *)(v_stack_p68 + 128));
    }
    v_stack_m400 = v_stack_m438;
    v_stack_m3F8 = v_xmm0;
    result = RtlCopyVolatileMemory(v_stack_m3F8, v_stack_m438 + 16, 16, a4);
loc_00255B47:
    result = KeIsEmptyGroupMask(v_stack_m3F8, v_stack_m438 + 16, 16, a4);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_00255DFA;
    result = KeFindFirstSetRightGroupMask(v_stack_m3F8, v_stack_m438 + 16, 16, a4);
    if ((*(unsigned __int64 *)(v_stack_m400 + (unsigned __int16)(result) * 8 + 32)) == v_stack_p68) goto loc_00255B47;
loc_00255B84:
    if (v_stack_m478 == 0) goto loc_00255B96;
    if (((*(unsigned __int64 *)(v_stack_m478 + 200)) & (16)) != 0) goto loc_00255CBD;
loc_00255B96:
    result = (*(unsigned __int64 *)(result + 36448)) & (16);
    if (condition_is_not_equal) goto loc_00255BEA;
    if (v_stack_m478 == 0) goto loc_00255BB3;
    result = (*(unsigned __int64 *)(v_stack_m478 + 36448)) & (16);
    if (condition_is_not_equal) goto loc_00255BEA;
loc_00255BB3:
    result = (16) & (*(unsigned __int64 *)(result + 36472));
    if (condition_is_not_equal) goto loc_00255BEA;
    if (v_stack_m478 == 0) goto loc_00255BD0;
    result = (16) & (*(unsigned __int64 *)(v_stack_m478 + 36448));
    if (condition_is_not_equal) goto loc_00255BEA;
loc_00255BD0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14087342)))) & (1)) == 0) goto loc_00255BF2;
    result = (16) & (*(unsigned __int64 *)(result + 36464));
    if (condition_is_equal) goto loc_00255CDA;
loc_00255BEA:
    v_stack_p58 = result;
loc_00255BF2:
    a2 = (unsigned int)((*(unsigned __int8 *)(result + 208)) << (6));
    a1 = (unsigned int)((*(unsigned __int8 *)(result + 209)) + ((unsigned int)(result)));
    v_stack_m420 = (unsigned int)(result);
    a1 = (unsigned int)((a1) & (63));
    a2 = (unsigned int)((a2) + ((unsigned int)(a1)));
    goto loc_002559A6;
loc_00255C32:
    if (v_stack_p30 != 0) goto loc_00255FBF;
loc_00255C3D:
    a1 = (*(unsigned __int64 *)(result + 24)) & (v_stack_p58);
    if (condition_is_not_equal) goto loc_00255C95;
    if (v_stack_p30 != 0) goto loc_00255FF7;
    if ((*(unsigned __int64 *)(a1 + 192)) != result) goto loc_00255961;
    result = KiReduceByEffectiveIdleSmtSet(a1, v_stack_p58, result, a4);
    goto loc_00255961;
loc_00255C7F:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p50, v_stack_p58, v_stack_p68, a4);
loc_00255C89:
    goto loc_00255756;
loc_00255C95:
    if (v_stack_p30 != 0) goto loc_00255FE6;
loc_00255CA0:
    goto loc_00255961;
loc_00255CA8:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p50, v_stack_p58, v_rip - 2448528, a4);
    goto loc_00255C89;
loc_00255CBD:
    v_stack_p34 = (unsigned int)((unsigned int)(v_stack_p40));
    goto loc_0025605C;
loc_00255CCA:
    goto loc_00255A33;
loc_00255CD2:
    goto loc_00255934;
loc_00255CDA:
    if (0 == 0) goto loc_00255BF2;
    result = (v_rip - 2448528) & (*(unsigned __int64 *)(0 + 36464));
    a3 = v_rip - 2448528;
    if (condition_is_not_equal) { a3 = result; }
    v_stack_p58 = a3;
    goto loc_00255BF2;
loc_00255CFB:
    result = 0;
    v_stack_m3E8 = v_xmm0;
    v_stack_m3D8 = 0;
    if (((*(unsigned int *)(v_rip + 14093870)) & (0x800000ULL)) == 0) goto loc_00255DF2;
    if (((*(unsigned __int8 *)(v_stack_m440 + 10)) & (8)) == 0) goto loc_00255DF2;
loc_00255D2E:
    v_rdi = (unsigned int)(v_stack_p40);
    if (1 > ((unsigned int)((unsigned int)(v_stack_p40)))) { v_rdi = 1; }
    v_stack_p34 = (unsigned int)(v_rdi);
loc_00255D37:
    if (0 == 0) goto loc_00255E38;
    a2 = 0;
    result = memset(v_stack_m118, a2, a2 + 64, a4);
    v_r11 = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14 + 136))) >= (*(unsigned __int16 *)(a3))) goto loc_00255FFF;
loc_00255D6D:
    v_rbx = (*(unsigned __int64 *)(v_r14 + (int)(v_stack_p34) * 8 + 16)) & (*(unsigned __int64 *)(v_r14 + 8));
    v_rbx = (v_rbx) & (*(unsigned __int64 *)(a3 + *(unsigned __int16 *)(v_r14 + 136) * 8 + 8));
    v_stack_p70 = v_rbx;
    if (condition_is_equal) goto loc_00255E12;
    if (((*(unsigned __int8 *)(v_r14 + 184)) & (1)) == 0) goto loc_00255EAA;
    if (v_stack_p30 == 0) goto loc_00255DB5;
    result = KiFindRankBiasedIdleSmtSet(0, v_stack_p70, a2 + 64, a4);
    v_r11 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00255DE8;
loc_00255DB5:
    a1 = (*(unsigned __int64 *)(v_r14 + 24)) & (v_stack_p70);
    if (condition_is_not_equal) goto loc_00255F60;
    if (v_stack_p30 != 0) goto loc_00255E12;
    if ((*(unsigned __int64 *)(a1 + 192)) != 0) goto loc_00255EAA;
    result = KiReduceByEffectiveIdleSmtSet(a1, v_stack_p70, a2 + 64, a4);
loc_00255DE8:
    goto loc_00255EAA;
loc_00255DF2:
    goto loc_00255D2E;
loc_00255DFA:
    if (((unsigned int)((unsigned int)(v_stack_m468))) <= v_stack_p40) goto loc_002559B4;
    result = (unsigned int)(((unsigned int)(v_stack_m468)) - 1);
    v_stack_p34 = (unsigned int)(result);
    goto loc_002558F4;
loc_00255E12:
loc_00255E15:
    if (v_stack_m378 >= = ((unsigned __int16)(*(unsigned __int16 *)(v_r14 + 136)))) {
        a1 = ~(*(unsigned __int64 *)(v_r14 + 128));
    }
    v_stack_m3E8 = v_stack_m440;
    v_stack_m3E0 = v_xmm0;
    result = RtlCopyVolatileMemory(v_stack_m3E0, v_stack_m440 + 16, 16, a4);
loc_00255E5B:
    result = KeIsEmptyGroupMask(v_stack_m3E0, v_stack_m440 + 16, 16, a4);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_00255FAE;
    result = KeFindFirstSetRightGroupMask(v_stack_m3E0, v_stack_m440 + 16, 16, a4);
    if ((*(unsigned __int64 *)(v_stack_m3E8 + (unsigned __int16)(result) * 8 + 32)) == 0) goto loc_00255E5B;
loc_00255E96:
    if (((unsigned int)(v_stack_m3E8)) < (*(unsigned int *)(v_rip + 14093943))) goto loc_00255E12;
loc_00255EA7:
loc_00255EAA:
    result = RtlCopyVolatileMemory(v_stack_m118, v_r14 + 576, 64, a4);
    result = KiReduceAffinityToRankListMinimums((unsigned __int16)(result), v_stack_m118, 64, a4);
    v_stack_p70 = result;
    if (((*(unsigned __int64 *)(v_stack_m430 + 200)) & (result)) != 0) goto loc_00256007;
    a3 = (*(unsigned __int64 *)(v_stack_m430 + 36448)) & (result);
    if (condition_is_equal) goto loc_00255F70;
loc_00255EF7:
    v_stack_p70 = a3;
loc_00255EFC:
    v_r11 = 0;
    a2 = (unsigned int)((*(unsigned __int8 *)(v_stack_m430 + 208)) << (6));
    a1 = (unsigned int)((*(unsigned __int8 *)(v_stack_m430 + 209)) + ((unsigned int)(result)));
    v_stack_m41C = (unsigned int)(result);
    a1 = (unsigned int)((a1) & (63));
    a2 = (unsigned int)((a2) + ((unsigned int)(a1)));
loc_00255F3C:
    if (*(unsigned __int64 *)(v_rip - 2449201 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13423251) + a2 * 4)) * 8 + 16550976) == 0) goto loc_00255E15;
loc_00255F45:
    v_stack_p34 = (unsigned int)((unsigned int)(v_stack_p40));
    if (*(unsigned __int64 *)(v_rip - 2449201 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 13423251) + a2 * 4)) * 8 + 16550976) != 0) goto loc_00255A04;
    goto loc_002559CF;
loc_00255F60:
    if (v_stack_p30 == 0) goto loc_00255EA7;
    goto loc_00255E96;
loc_00255F70:
    a3 = (*(unsigned __int64 *)(v_stack_m430 + 36472)) & (v_stack_p68);
    if (condition_is_not_equal) goto loc_00255EF7;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14086398)))) & (1)) == 0) goto loc_00255EFC;
    result = (*(unsigned __int64 *)(v_stack_m430 + 36464)) & (v_stack_p68);
    if (condition_is_equal) goto loc_00255EFC;
    v_stack_p70 = result;
    goto loc_00255EFC;
loc_00255FAE:
    if (0 <= v_stack_p40) goto loc_00255F45;
    v_rsi = (unsigned int)((0) - 1);
    v_stack_p34 = (unsigned int)(v_rsi);
    goto loc_00255D37;
loc_00255FBF:
    result = KiFindRankBiasedIdleSmtSet(result, v_stack_p58, result, v_stack_m430);
    v_r11 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00255C3D;
    goto loc_00255961;
loc_00255FE6:
    if (((unsigned int)(result)) >= (*(unsigned int *)(v_rip + 14093607))) goto loc_00255CA0;
loc_00255FF7:
    goto loc_00255B01;
loc_00255FFF:
    goto loc_00255D6D;
loc_00256007:
    v_r11 = 0;
    goto loc_00255F3C;
loc_00256012:
    if (result == 0) goto loc_002559DC;
    result = 0;
    v_stack_m410 = 0;
    v_stack_m3D0 = v_xmm0;
    v_stack_m3C0 = 0;
loc_00256057:
loc_0025605C:
    goto loc_00255790;
loc_00256065:
    result = KiIsIsolationUnitIdleByHandle(v_stack_p50, v_stack_p58, v_stack_p68, v_stack_m430);
    v_r14 = 0;
    *(unsigned int *)(v_stack_m478 + 8) = (unsigned int)(result);
    goto loc_00255A9E;
loc_0025607E:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p50, v_stack_p58, v_stack_p68, v_stack_m430);
    a3 = (v_stack_p68) | (-1);
    v_stack_p20 = v_stack_p50;
    result = KiSelectCandidateProcessor(v_stack_p48, v_stack_m470, a3, (unsigned int)((unsigned int)((unsigned int)(v_stack_p40))));
    result = KiIsIsolationUnitIdleByHandle(v_stack_p50, v_stack_m470, a3, (unsigned int)((unsigned int)((unsigned int)(v_stack_p40))));
    a1 = ((unsigned int)(result) != 0) ? 1 : 0;
    *(unsigned int *)(v_stack_m478 + 8) = (unsigned int)(a1);
    goto loc_00255AA8;
}
```

## 5. (Beta) C Style

```c
int64_t KiChooseTargetProcessor(void *Arg1, void *Arg2, void *Arg3, int64_t Arg4, uint8_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m118;
    uint64_t v_stack_m158;
    uint64_t v_stack_m370;
    uint16_t v_stack_m376;
    uint64_t v_stack_m378;
    uint64_t v_stack_m3C0;
    uint64_t v_stack_m3D0;
    uint64_t v_stack_m3D8;
    uint64_t v_stack_m3E0;
    uint64_t v_stack_m3E8;
    uint64_t v_stack_m3F0;
    uint64_t v_stack_m3F8;
    uint64_t v_stack_m400;
    uint64_t v_stack_m408;
    uint64_t v_stack_m410;
    uint32_t v_stack_m41C;
    uint32_t v_stack_m420;
    uint64_t v_stack_m430;
    uint64_t v_stack_m438;
    uint64_t v_stack_m440;
    uint64_t v_stack_m448;
    uint32_t v_stack_m44C;
    uint64_t v_stack_m450;
    uint64_t v_stack_m458;
    uint64_t v_stack_m460;
    uint32_t v_stack_m468;
    uint64_t v_stack_m470;
    uint64_t v_stack_m478;
    uint64_t v_stack_m4A8;
    uint64_t v_stack_m4B0;
    uint32_t v_stack_m4C0;
    uint32_t v_stack_m4C4;
    uint64_t v_stack_m4C8;
    uint64_t v_stack_m4D8;
    uint64_t v_stack_m58;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;

    local_rsp = (local_rsp) - (0x4B8ULL);
    result = (*(uint64_t *)(v_rip + 0xBB5045)) ^ (local_rsp);
    v_stack_m58 = result;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x78))) >> (1));
    v_stack_m478 = Arg4;
    result = 0;
    v_stack_m4C8 = 0;
    local_rdi = (uint32_t)((local_rdi) & (1));
    v_stack_m4A8 = 0;
    v_stack_m4C0 = 0;
    v_stack_m4C8 = Arg5;
    v_stack_m470 = Arg2;
    v_stack_m4B0 = *(uint64_t *)(v_rip - 0x255718 + (uint32_t)(*(uint32_t *)(arg2 + 0x24C)) * 8 + 0xFC8C40);
    v_stack_m4C4 = (uint32_t)(local_rdi);
loc_00255756:
    v_stack_m4D8 = v_stack_m4C8;
    v_stack_m430 = *(uint64_t *)(v_rip - 0x255718 + (uint32_t)(*(uint32_t *)(arg2 + 0x218)) * 8 + 0xFC8C40);
    result = KiTryLocalThreadSchedule(Arg1, *(uint64_t *)(v_rip - 0x255718 + (uint32_t)(*(uint32_t *)(arg2 + 0x218)) * 8 + 0xFC8C40), Arg2, Arg3);
    if (result == 0) goto loc_002557F3;
loc_00255790:
    result = KiAcquirePrcbLocksForIsolationUnit(result, (uint32_t)((uint32_t)(local_rdi)), v_stack_m4A8, Arg3);
    result = KiIsIsolationUnitIdleByHandle(v_stack_m4A8, (uint32_t)((uint32_t)(local_rdi)), v_stack_m4A8, Arg3);
    if ((uint32_t)(result) == 0) goto loc_00255C7F;
    if (((*(uint8_t *)(result + 0x23)) & (16)) != 0) goto loc_00255C7F;
    *(uint64_t *)(v_stack_m478) = v_stack_m4A8;
    *(uint64_t *)(v_stack_m478 + 0x8) = 1;
loc_002557CF:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)((uint32_t)(local_rdi)), v_stack_m4A8, Arg3);
    local_rsp = (local_rsp) + (0x4B8ULL);
    return result;
loc_002557F3:
    Arg2 = 0;
    result = memset(v_stack_m370, Arg2, 256, Arg3);
    Arg3 = 0;
    v_stack_m450 = 0;
    v_stack_m408 = 0;
    v_stack_m460 = *(uint64_t *)(arg1 + 0xC0);
    v_stack_p68 = *(uint64_t *)(*(uint64_t *)(v_rip - 0x255718 + (uint32_t)(*(uint32_t *)(arg2 + 0x24C)) * 8 + 0xFC8C40) + 0xC0);
    v_stack_m378 = 0x200001ULL;
    v_stack_m438 = *(uint64_t *)(v_rip - 0x255828 + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x255718 + (uint32_t)(*(uint32_t *)(arg2 + 0x24C)) * 8 + 0xFC8C40) + 0xC0) + 0x8A) * 8 + 0xFCF6C0);
    v_stack_m440 = *(uint64_t *)(v_rip - 0x255828 + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x255718 + (uint32_t)(*(uint32_t *)(arg2 + 0x218)) * 8 + 0xFC8C40) + 0xC0) + 0x8A) * 8 + 0xFCF6C0);
    Arg2 = 0;
    v_stack_m448 = *(uint64_t *)(v_rip - 0x255828 + *(uint16_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x8A) * 8 + 0xFCF6C0);
    result = memset(v_stack_m370, Arg2, 256, v_rip - 2447400);
    result = KiCopyAffinityEx(v_stack_m378, v_stack_m376, 0, v_rip - 2447400);
    v_stack_p40 = (uint32_t)(local_rdi);
    local_rsi = 0;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x255718 + (uint32_t)(*(uint32_t *)(arg2 + 0x24C)) * 8 + 0xFC8C40) + 0xC0)) == (*(uint64_t *)(*(uint64_t *)(v_rip - 0x255718 + (uint32_t)(*(uint32_t *)(arg2 + 0x218)) * 8 + 0xFC8C40) + 0xC0))) { local_rsi = v_stack_m430; }
    result = 0;
    v_stack_m3F0 = 0;
    local_r11 = 0;
    v_stack_m400 = v_xmm0;
    result = (uint32_t)((*(uint8_t *)(v_stack_m438 + 0xA)) >> (3));
    result = (uint32_t)((result) & (1));
    if (((uint32_t)(result)) > ((uint32_t)(local_rdi))) { local_rdi = (uint32_t)(result); }
    v_stack_p34 = (uint32_t)(local_rdi);
loc_002558F4:
    v_stack_m468 = (uint32_t)(result);
    if (v_stack_p68 == 0) goto loc_00255B24;
    Arg2 = 0;
    result = memset(v_stack_m158, Arg2, Arg2 + 64, v_rip - 2447400);
    local_r11 = 0;
    if (((uint16_t)(*(uint16_t *)(v_stack_p68 + 0x88))) >= (*(uint16_t *)(arg3))) goto loc_00255CD2;
loc_00255934:
    local_rbx = (*(uint64_t *)(v_stack_p68 + (int32_t)(v_stack_p34) * 8 + 0x10)) & (*(uint64_t *)(v_stack_p68 + 0x8));
    local_rbx = (local_rbx) & (*(uint64_t *)(arg3 + *(uint16_t *)(v_stack_p68 + 0x88) * 8 + 0x8));
    v_stack_p58 = local_rbx;
    if (condition_is_equal) goto loc_00255FF7;
    if (((*(uint8_t *)(v_stack_p68 + 0xB8)) & (1)) != 0) goto loc_00255C32;
loc_00255961:
    result = RtlCopyVolatileMemory(v_stack_m158, v_stack_p68 + 576, 64, v_rip - 2447400);
    result = KiReduceAffinityToRankListMinimums(local_rbx, v_stack_m158, 64, v_rip - 2447400);
    local_r11 = 0;
    v_stack_p58 = result;
    if (((*(uint64_t *)(v_stack_p48 + 0xC8)) & (result)) == 0) goto loc_00255B84;
loc_002559A6:
    if (v_stack_p48 == 0) goto loc_00255AFC;
loc_002559B4:
    v_stack_p34 = (uint32_t)((uint32_t)(v_stack_p40));
    if (v_stack_p48 != 0) goto loc_00255A04;
    if (v_stack_p68 != (*(uint64_t *)(*(uint64_t *)(v_rip - 0x255718 + (uint32_t)(*(uint32_t *)(arg2 + 0x218)) * 8 + 0xFC8C40) + 0xC0))) goto loc_00255CFB;
loc_002559CF:
    if (v_stack_m460 != v_stack_p68) goto loc_00256012;
loc_002559DC:
loc_002559E5:
    if (0 >= v_stack_m378) goto loc_00255A04;
    if ((*(uint64_t *)(v_stack_m3F8 + 0x0 * 8 + 0x88)) != 0) goto loc_00255AE8;
    Arg1 = (uint16_t)((0) + (1));
    goto loc_002559E5;
loc_00255A04:
    if (v_stack_p48 != 0) goto loc_00256057;
    if (((uint16_t)(*(uint8_t *)(v_stack_p48 + 0xD0))) >= (*(uint16_t *)(arg3))) goto loc_00255CCA;
loc_00255A33:
    Arg4 = 0;
    result = KiSelectProcessorToPreempt(v_stack_m470, v_stack_p48, *(uint64_t *)(arg3 + *(uint8_t *)(v_stack_p48 + 0xD0) * 8 + 0x8), Arg4);
    result = KiAcquirePrcbLocksForPreemptionAttempt(result, (uint32_t)((uint32_t)((uint32_t)(v_stack_p34))), v_stack_p50, Arg4);
    result = 0;
    if (Arg5 != 0) goto loc_00256065;
    local_r11 = (*(uint64_t *)(*(uint64_t *)(result + 0xC0) + 0x8)) & (*(uint64_t *)(*(uint64_t *)(result + 0xC0) + (int32_t)(v_stack_p34) * 8 + 0x10));
    if (((*(uint64_t *)(arg3 + *(uint8_t *)(v_stack_p48 + 0xD0) * 8 + 0x8)) & (local_r11)) != 0) goto loc_00255CA8;
    if (((*(uint8_t *)(result + 0x23)) & (16)) == 0) goto loc_00255AB9;
    local_r14 = 0;
loc_00255A92:
    *(uint32_t *)(v_stack_m478 + 0x8) = 0;
loc_00255A9E:
    if (((*(uint8_t *)(result + 0x23)) & (16)) != 0) goto loc_0025607E;
loc_00255AA8:
    *(uint64_t *)(v_stack_m478) = v_stack_p50;
    *(uint32_t *)(v_stack_m478 + 0xC) = 0;
    goto loc_002557CF;
loc_00255AB9:
    result = KiIsIsolationUnitIdleByHandle(v_stack_p50, *(uint64_t *)(*(uint64_t *)(result + 0xC0) + (int32_t)(v_stack_p34) * 8 + 0x10), v_stack_p50, Arg4);
    local_r14 = 0;
    if ((uint32_t)(result) == 0) goto loc_00255A92;
    v_stack_m478 = v_stack_m478;
    v_stack_m478 = local_r11;
    v_stack_m458 = v_stack_m478;
    v_stack_m458 = v_stack_m478;
loc_00255AE8:
    v_stack_m450 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(result + 0xC0) + (int32_t)(v_stack_p34) * 8 + 0x10) + 0x8A));
    v_stack_m44C = (uint32_t)(local_r11);
loc_00255AFC:
loc_00255B01:
    if (v_stack_m378 >= = ((uint16_t)(*(uint16_t *)(v_stack_p68 + 0x88)))) {
        Arg1 = ~(*(uint64_t *)(v_stack_p68 + 0x80));
    }
    v_stack_m400 = v_stack_m438;
    v_stack_m3F8 = v_xmm0;
    result = RtlCopyVolatileMemory(v_stack_m3F8, v_stack_m438 + 16, 16, Arg4);
loc_00255B47:
    result = KeIsEmptyGroupMask(v_stack_m3F8, v_stack_m438 + 16, 16, Arg4);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_00255DFA;
    result = KeFindFirstSetRightGroupMask(v_stack_m3F8, v_stack_m438 + 16, 16, Arg4);
    if ((*(uint64_t *)(v_stack_m400 + (uint16_t)(result) * 8 + 0x20)) == v_stack_p68) goto loc_00255B47;
loc_00255B84:
    if (v_stack_m478 == 0) goto loc_00255B96;
    if (((*(uint64_t *)(v_stack_m478 + 0xC8)) & (16)) != 0) goto loc_00255CBD;
loc_00255B96:
    result = (*(uint64_t *)(result + 0x8E60)) & (16);
    if (condition_is_not_equal) goto loc_00255BEA;
    if (v_stack_m478 == 0) goto loc_00255BB3;
    result = (*(uint64_t *)(v_stack_m478 + 0x8E60)) & (16);
    if (condition_is_not_equal) goto loc_00255BEA;
loc_00255BB3:
    result = (16) & (*(uint64_t *)(result + 0x8E78));
    if (condition_is_not_equal) goto loc_00255BEA;
    if (v_stack_m478 == 0) goto loc_00255BD0;
    result = (16) & (*(uint64_t *)(v_stack_m478 + 0x8E60));
    if (condition_is_not_equal) goto loc_00255BEA;
loc_00255BD0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD6F4AE)))) & (1)) == 0) goto loc_00255BF2;
    result = (16) & (*(uint64_t *)(result + 0x8E70));
    if (condition_is_equal) goto loc_00255CDA;
loc_00255BEA:
    v_stack_p58 = result;
loc_00255BF2:
    Arg2 = (uint32_t)((*(uint8_t *)(result + 0xD0)) << (6));
    Arg1 = (uint32_t)((*(uint8_t *)(result + 0xD1)) + ((uint32_t)(result)));
    v_stack_m420 = (uint32_t)(result);
    Arg1 = (uint32_t)((Arg1) & (63));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg1)));
    goto loc_002559A6;
loc_00255C32:
    if (v_stack_p30 != 0) goto loc_00255FBF;
loc_00255C3D:
    Arg1 = (*(uint64_t *)(result + 0x18)) & (v_stack_p58);
    if (condition_is_not_equal) goto loc_00255C95;
    if (v_stack_p30 != 0) goto loc_00255FF7;
    if ((*(uint64_t *)(arg1 + 0xC0)) != result) goto loc_00255961;
    result = KiReduceByEffectiveIdleSmtSet(Arg1, v_stack_p58, result, Arg4);
    goto loc_00255961;
loc_00255C7F:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p50, v_stack_p58, v_stack_p68, Arg4);
loc_00255C89:
    goto loc_00255756;
loc_00255C95:
    if (v_stack_p30 != 0) goto loc_00255FE6;
loc_00255CA0:
    goto loc_00255961;
loc_00255CA8:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p50, v_stack_p58, v_rip - 2448528, Arg4);
    goto loc_00255C89;
loc_00255CBD:
    v_stack_p34 = (uint32_t)((uint32_t)(v_stack_p40));
    goto loc_0025605C;
loc_00255CCA:
    goto loc_00255A33;
loc_00255CD2:
    goto loc_00255934;
loc_00255CDA:
    if (0 == 0) goto loc_00255BF2;
    result = (v_rip - 2448528) & (*(uint64_t *)(0 + 0x8E70));
    Arg3 = v_rip - 2448528;
    if (condition_is_not_equal) { Arg3 = result; }
    v_stack_p58 = Arg3;
    goto loc_00255BF2;
loc_00255CFB:
    result = 0;
    v_stack_m3E8 = v_xmm0;
    v_stack_m3D8 = 0;
    if (((*(uint32_t *)(v_rip + 0xD70E2E)) & (0x800000ULL)) == 0) goto loc_00255DF2;
    if (((*(uint8_t *)(v_stack_m440 + 0xA)) & (8)) == 0) goto loc_00255DF2;
loc_00255D2E:
    local_rdi = (uint32_t)(v_stack_p40);
    if (1 > ((uint32_t)((uint32_t)(v_stack_p40)))) { local_rdi = 1; }
    v_stack_p34 = (uint32_t)(local_rdi);
loc_00255D37:
    if (0 == 0) goto loc_00255E38;
    Arg2 = 0;
    result = memset(v_stack_m118, Arg2, Arg2 + 64, Arg4);
    local_r11 = 0;
    if (((uint16_t)(*(uint16_t *)(local_r14 + 0x88))) >= (*(uint16_t *)(arg3))) goto loc_00255FFF;
loc_00255D6D:
    local_rbx = (*(uint64_t *)(local_r14 + (int32_t)(v_stack_p34) * 8 + 0x10)) & (*(uint64_t *)(local_r14 + 0x8));
    local_rbx = (local_rbx) & (*(uint64_t *)(arg3 + *(uint16_t *)(local_r14 + 0x88) * 8 + 0x8));
    v_stack_p70 = local_rbx;
    if (condition_is_equal) goto loc_00255E12;
    if (((*(uint8_t *)(local_r14 + 0xB8)) & (1)) == 0) goto loc_00255EAA;
    if (v_stack_p30 == 0) goto loc_00255DB5;
    result = KiFindRankBiasedIdleSmtSet(0, v_stack_p70, Arg2 + 64, Arg4);
    local_r11 = 0;
    if ((uint8_t)(result) != 0) goto loc_00255DE8;
loc_00255DB5:
    Arg1 = (*(uint64_t *)(local_r14 + 0x18)) & (v_stack_p70);
    if (condition_is_not_equal) goto loc_00255F60;
    if (v_stack_p30 != 0) goto loc_00255E12;
    if ((*(uint64_t *)(arg1 + 0xC0)) != 0) goto loc_00255EAA;
    result = KiReduceByEffectiveIdleSmtSet(Arg1, v_stack_p70, Arg2 + 64, Arg4);
loc_00255DE8:
    goto loc_00255EAA;
loc_00255DF2:
    goto loc_00255D2E;
loc_00255DFA:
    if (((uint32_t)((uint32_t)(v_stack_m468))) <= v_stack_p40) goto loc_002559B4;
    result = (uint32_t)(((uint32_t)(v_stack_m468)) - 1);
    v_stack_p34 = (uint32_t)(result);
    goto loc_002558F4;
loc_00255E12:
loc_00255E15:
    if (v_stack_m378 >= = ((uint16_t)(*(uint16_t *)(local_r14 + 0x88)))) {
        Arg1 = ~(*(uint64_t *)(local_r14 + 0x80));
    }
    v_stack_m3E8 = v_stack_m440;
    v_stack_m3E0 = v_xmm0;
    result = RtlCopyVolatileMemory(v_stack_m3E0, v_stack_m440 + 16, 16, Arg4);
loc_00255E5B:
    result = KeIsEmptyGroupMask(v_stack_m3E0, v_stack_m440 + 16, 16, Arg4);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_00255FAE;
    result = KeFindFirstSetRightGroupMask(v_stack_m3E0, v_stack_m440 + 16, 16, Arg4);
    if ((*(uint64_t *)(v_stack_m3E8 + (uint16_t)(result) * 8 + 0x20)) == 0) goto loc_00255E5B;
loc_00255E96:
    if (((uint32_t)(v_stack_m3E8)) < (*(uint32_t *)(v_rip + 0xD70E77))) goto loc_00255E12;
loc_00255EA7:
loc_00255EAA:
    result = RtlCopyVolatileMemory(v_stack_m118, local_r14 + 576, 64, Arg4);
    result = KiReduceAffinityToRankListMinimums((uint16_t)(result), v_stack_m118, 64, Arg4);
    v_stack_p70 = result;
    if (((*(uint64_t *)(v_stack_m430 + 0xC8)) & (result)) != 0) goto loc_00256007;
    Arg3 = (*(uint64_t *)(v_stack_m430 + 0x8E60)) & (result);
    if (condition_is_equal) goto loc_00255F70;
loc_00255EF7:
    v_stack_p70 = Arg3;
loc_00255EFC:
    local_r11 = 0;
    Arg2 = (uint32_t)((*(uint8_t *)(v_stack_m430 + 0xD0)) << (6));
    Arg1 = (uint32_t)((*(uint8_t *)(v_stack_m430 + 0xD1)) + ((uint32_t)(result)));
    v_stack_m41C = (uint32_t)(result);
    Arg1 = (uint32_t)((Arg1) & (63));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg1)));
loc_00255F3C:
    if (*(uint64_t *)(v_rip - 0x255F31 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCCD293) + arg2 * 4)) * 8 + 0xFC8C40) == 0) goto loc_00255E15;
loc_00255F45:
    v_stack_p34 = (uint32_t)((uint32_t)(v_stack_p40));
    if (*(uint64_t *)(v_rip - 0x255F31 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xCCD293) + arg2 * 4)) * 8 + 0xFC8C40) != 0) goto loc_00255A04;
    goto loc_002559CF;
loc_00255F60:
    if (v_stack_p30 == 0) goto loc_00255EA7;
    goto loc_00255E96;
loc_00255F70:
    Arg3 = (*(uint64_t *)(v_stack_m430 + 0x8E78)) & (v_stack_p68);
    if (condition_is_not_equal) goto loc_00255EF7;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD6F0FE)))) & (1)) == 0) goto loc_00255EFC;
    result = (*(uint64_t *)(v_stack_m430 + 0x8E70)) & (v_stack_p68);
    if (condition_is_equal) goto loc_00255EFC;
    v_stack_p70 = result;
    goto loc_00255EFC;
loc_00255FAE:
    if (0 <= v_stack_p40) goto loc_00255F45;
    local_rsi = (uint32_t)((0) - 1);
    v_stack_p34 = (uint32_t)(local_rsi);
    goto loc_00255D37;
loc_00255FBF:
    result = KiFindRankBiasedIdleSmtSet(result, v_stack_p58, result, v_stack_m430);
    local_r11 = 0;
    if ((uint8_t)(result) == 0) goto loc_00255C3D;
    goto loc_00255961;
loc_00255FE6:
    if (((uint32_t)(result)) >= (*(uint32_t *)(v_rip + 0xD70D27))) goto loc_00255CA0;
loc_00255FF7:
    goto loc_00255B01;
loc_00255FFF:
    goto loc_00255D6D;
loc_00256007:
    local_r11 = 0;
    goto loc_00255F3C;
loc_00256012:
    if (result == 0) goto loc_002559DC;
    result = 0;
    v_stack_m410 = 0;
    v_stack_m3D0 = v_xmm0;
    v_stack_m3C0 = 0;
loc_00256057:
loc_0025605C:
    goto loc_00255790;
loc_00256065:
    result = KiIsIsolationUnitIdleByHandle(v_stack_p50, v_stack_p58, v_stack_p68, v_stack_m430);
    local_r14 = 0;
    *(uint32_t *)(v_stack_m478 + 0x8) = (uint32_t)(result);
    goto loc_00255A9E;
loc_0025607E:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p50, v_stack_p58, v_stack_p68, v_stack_m430);
    Arg3 = (v_stack_p68) | (-1);
    v_stack_p20 = v_stack_p50;
    result = KiSelectCandidateProcessor(v_stack_p48, v_stack_m470, Arg3, (uint32_t)((uint32_t)((uint32_t)(v_stack_p40))));
    result = KiIsIsolationUnitIdleByHandle(v_stack_p50, v_stack_m470, Arg3, (uint32_t)((uint32_t)((uint32_t)(v_stack_p40))));
    Arg1 = ((uint32_t)(result) != 0) ? 1 : 0;
    *(uint32_t *)(v_stack_m478 + 0x8) = (uint32_t)(Arg1);
    goto loc_00255AA8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg2` | `+ 0x78` | `32` | `R` |
| `Arg2` | `+ 0x24C` | `32` | `R` |
| `Arg3` | `+ 0x0` | `16` | `R` |
| `Arg3` | `+ 0x8 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002556D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
