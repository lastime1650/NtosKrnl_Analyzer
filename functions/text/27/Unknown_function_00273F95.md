# sub_00273F95

- RVA: `0x00273F95`–`0x0027456F` (길이 `1,498` bytes)
- VA: `0x0000000140273F95`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065DAC`
- 디코드: `351`개 명령, `1,498/1,498` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00274050` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0027411C` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0027414F` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x00274162` → [KiHaltOnAddressWakeEntireList](../21/KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)
- `0x0027419F` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x002741BA` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00274268` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002742C2` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x002742DD` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0027439A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x002743D8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002744DE` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x00274518` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0027452B` → [KiHaltOnAddressWakeEntireList](../21/KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00273FEE` → RVA `0x00FC6F88` (`ALMOSTRO`; read)
- `0x00274038` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x002740DE` → RVA `0x00FC6B06` (`ALMOSTRO`; reference)
- `0x00274144` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00274188` → RVA `0x00F0DE58` (`.data`; read)
- `0x002741A4` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002741F5` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0027437D` → RVA `0x00E68468` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0027439A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x002743D8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **22**
  - `0x00273FF4` → [sub_0027475D + 0xBEA](Unknown_function_0027475D.md) (`tail-transfer`)
  - `0x00274001` → [sub_0027475D + 0xD07](Unknown_function_0027475D.md) (`tail-transfer`)
  - `0x00274011` → [sub_0027475D + 0xDB3](Unknown_function_0027475D.md) (`tail-transfer`)
  - `0x00274065` → [sub_0027475D + 0xAA3](Unknown_function_0027475D.md) (`tail-transfer`)
  - `0x0027417F` → [sub_0027475D + 0x7AD](Unknown_function_0027475D.md) (`tail-transfer`)
  - `0x002741DC` → [sub_00274581 + 0xA7](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00274210` → [sub_0027475D + 0x7A5](Unknown_function_0027475D.md) (`tail-transfer`)
  - `0x00274228` → [sub_0027475D + 0x18](Unknown_function_0027475D.md) (`tail-transfer`)
  - `0x00274239` → [sub_00274581](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x0027424F` → [sub_00274581 + 0x2D](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x00274272` → [sub_00274581 + 0x6C](Unknown_function_00274581.md) (`tail-transfer`)
  - `0x002742F1` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x0027434E` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x00274370` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x002743A5` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x0027444D` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x00274457` → [sub_002746E8 + 0x4A](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x0027446B` → [sub_0027475D + 0xF37](Unknown_function_0027475D.md) (`tail-transfer`)
  - `0x0027447D` → [sub_002746E8](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x0027448A` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x00274497` → [sub_002746E8 + 0x4E](Unknown_function_002746E8.md) (`tail-transfer`)
  - `0x0027454C` → [sub_0027475D + 0x658](Unknown_function_0027475D.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00273F95  8B 4B 38                        mov ecx, dword ptr [rbx + 0x38]
00273F98  41 BD 01 00 00 00               mov r13d, 1
00273F9E  8B C1                           mov eax, ecx
00273FA0  83 E1 07                        and ecx, 7
00273FA3  C1 E8 03                        shr eax, 3
00273FA6  44 8D 3C C5 F8 FF FF FF         lea r15d, [rax*8 - 8]
00273FAE  44 0B F9                        or r15d, ecx
00273FB1  44 89 7B 38                     mov dword ptr [rbx + 0x38], r15d
00273FB5  41 C1 EF 03                     shr r15d, 3
00273FB9  45 85 FF                        test r15d, r15d
00273FBC  0F 85 CC 02 00 00               jne 0x14027428e
00273FC2  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
00273FC5  48 8B 7B 30                     mov rdi, qword ptr [rbx + 0x30]
00273FC9  A8 02                           test al, 2
00273FCB  0F 84 87 05 00 00               je 0x140274558
00273FD1  48 83 E7 FC                     and rdi, 0xfffffffffffffffc
00273FD5  48 85 FF                        test rdi, rdi
00273FD8  0F 84 91 00 00 00               je 0x14027406f
00273FDE  41 84 C5                        test r13b, al
00273FE1  74 3D                           je 0x140274020
00273FE3  33 C0                           xor eax, eax
00273FE5  40 32 F6                        xor sil, sil
00273FE8  45 32 F6                        xor r14b, r14b
00273FEB  44 8B F8                        mov r15d, eax
00273FEE  39 05 94 2F D5 00               cmp dword ptr [rip + 0xd52f94], eax
00273FF4  0F 85 4D 13 00 00               jne 0x140275347
00273FFA  83 BF E0 05 00 00 00            cmp dword ptr [rdi + 0x5e0], 0
00274001  0F 84 5D 14 00 00               je 0x140275464
00274007  F0 FF 8F E0 05 00 00            lock dec dword ptr [rdi + 0x5e0]
0027400E  40 84 F6                        test sil, sil
00274011  0F 85 F9 14 00 00               jne 0x140275510
00274017  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0027401A  83 E0 FE                        and eax, 0xfffffffe
0027401D  89 43 38                        mov dword ptr [rbx + 0x38], eax
00274020  A8 04                           test al, 4
00274022  74 10                           je 0x140274034
00274024  F0 FF 8F E4 05 00 00            lock dec dword ptr [rdi + 0x5e4]
0027402B  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0027402E  83 E0 FB                        and eax, 0xfffffffb
00274031  89 43 38                        mov dword ptr [rbx + 0x38], eax
00274034  A8 02                           test al, 2
00274036  74 37                           je 0x14027406f
00274038  83 3D D1 0F D5 00 00            cmp dword ptr [rip + 0xd50fd1], 0
0027403F  74 14                           je 0x140274055
00274041  41 B9 44 66 6C 74               mov r9d, 0x746c6644
00274047  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0027404B  45 8B C5                        mov r8d, r13d
0027404E  33 D2                           xor edx, edx
00274050  E8 8F C9 F9 FF                  call 0x1402109e4
00274055  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0027405C  F0 48 0F C1 47 D0               lock xadd qword ptr [rdi - 0x30], rax
00274062  49 2B C5                        sub rax, r13
00274065  0F 8E 95 11 00 00               jle 0x140275200
0027406B  83 63 38 FD                     and dword ptr [rbx + 0x38], 0xfffffffd
0027406F  45 33 F6                        xor r14d, r14d
00274072  4C 89 73 30                     mov qword ptr [rbx + 0x30], r14
00274076  41 8B F6                        mov esi, r14d
00274079  8B 4B 48                        mov ecx, dword ptr [rbx + 0x48]
0027407C  8B 43 44                        mov eax, dword ptr [rbx + 0x44]
0027407F  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00274083  85 C9                           test ecx, ecx
00274085  0F 84 E3 01 00 00               je 0x14027426e
0027408B  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
0027408F  BA 7F FF 00 00                  mov edx, 0xff7f
00274094  4C 89 73 20                     mov qword ptr [rbx + 0x20], r14
00274098  66 21 53 1A                     and word ptr [rbx + 0x1a], dx
0027409C  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
002740A1  44 89 73 48                     mov dword ptr [rbx + 0x48], r14d
002740A5  8B 53 40                        mov edx, dword ptr [rbx + 0x40]
002740A8  FF CA                           dec edx
002740AA  03 D1                           add edx, ecx
002740AC  89 53 40                        mov dword ptr [rbx + 0x40], edx
002740AF  44 39 73 4C                     cmp dword ptr [rbx + 0x4c], r14d
002740B3  75 0F                           jne 0x1402740c4
002740B5  44 39 73 48                     cmp dword ptr [rbx + 0x48], r14d
002740B9  75 09                           jne 0x1402740c4
002740BB  B9 F9 00 00 00                  mov ecx, 0xf9
002740C0  66 21 4B 1A                     and word ptr [rbx + 0x1a], cx
002740C4  44 0F B6 7B 1B                  movzx r15d, byte ptr [rbx + 0x1b]
002740C9  48 85 F6                        test rsi, rsi
002740CC  74 10                           je 0x1402740de
002740CE  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
002740D1  83 E0 07                        and eax, 7
002740D4  48 89 73 30                     mov qword ptr [rbx + 0x30], rsi
002740D8  83 C8 08                        or eax, 8
002740DB  89 43 38                        mov dword ptr [rbx + 0x38], eax
002740DE  44 84 2D 21 2A D5 00            test byte ptr [rip + 0xd52a21], r13b
002740E5  0F 85 9D 00 00 00               jne 0x140274188
002740EB  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
002740F0  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002740F5  48 85 C0                        test rax, rax
002740F8  75 27                           jne 0x140274121
002740FA  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002740FF  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00274104  F0 4C 0F B1 31                  lock cmpxchg qword ptr [rcx], r14
00274109  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0027410E  48 3B C1                        cmp rax, rcx
00274111  0F 84 8D 00 00 00               je 0x1402741a4
00274117  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0027411C  E8 7F 39 FA FF                  call 0x140217aa0
00274121  4C 8D 40 08                     lea r8, [rax + 8]
00274125  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0027412A  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0027412F  48 8B C1                        mov rax, rcx
00274132  49 87 00                        xchg qword ptr [r8], rax
00274135  32 C1                           xor al, cl
00274137  A8 04                           test al, 4
00274139  74 69                           je 0x1402741a4
0027413B  F0 44 09 34 24                  lock or dword ptr [rsp], r14d
00274140  49 C1 E8 05                     shr r8, 5
00274144  4C 8D 15 B5 BE D8 FF            lea r10, [rip - 0x27414b]
0027414B  41 83 E0 7F                     and r8d, 0x7f
0027414F  E8 8C 3A FA FF                  call 0x140217be0
00274154  49 8B D6                        mov rdx, r14
00274157  0F B6 F8                        movzx edi, al
0027415A  4B 87 94 C2 20 1B F2 00         xchg qword ptr [r10 + r8*8 + 0xf21b20], rdx
00274162  E8 8D 39 FA FF                  call 0x140217af4
00274167  40 84 FF                        test dil, dil
0027416A  74 38                           je 0x1402741a4
0027416C  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00274175  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0027417C  4D 85 C0                        test r8, r8
0027417F  0F 85 85 0D 00 00               jne 0x140274f0a
00274185  FB                              sti
00274186  EB 1C                           jmp 0x1402741a4
00274188  8B 05 CA 9C C9 00               mov eax, dword ptr [rip + 0xc99cca]
0027418E  85 C0                           test eax, eax
00274190  0F 85 55 FF FF FF               jne 0x1402740eb
00274196  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0027419A  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0027419F  E8 4C 38 FA FF                  call 0x1402179f0
002741A4  44 39 35 75 2B D5 00            cmp dword ptr [rip + 0xd52b75], r14d
002741AB  0F B6 7C 24 58                  movzx edi, byte ptr [rsp + 0x58]
002741B0  74 0D                           je 0x1402741bf
002741B2  44 0F 20 C1                     mov rcx, cr8
002741B6  40 0F B6 D7                     movzx edx, dil
002741BA  E8 D9 14 28 00                  call 0x1404f5698
002741BF  44 0F 22 C7                     mov cr8, rdi
002741C3  48 85 F6                        test rsi, rsi
002741C6  41 BE 03 00 00 00               mov r14d, 3
002741CC  41 8B FD                        mov edi, r13d
002741CF  41 8B F5                        mov esi, r13d
002741D2  41 0F 45 FE                     cmovne edi, r14d
002741D6  48 83 7C 24 70 00               cmp qword ptr [rsp + 0x70], 0
002741DC  0F 85 46 04 00 00               jne 0x140274628
002741E2  BE 22 00 01 00                  mov esi, 0x10022
002741E7  33 C0                           xor eax, eax
002741E9  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
002741ED  44 8B F8                        mov r15d, eax
002741F0  E9 F1 00 00 00                  jmp 0x1402742e6
002741F5  44 8B 2D 08 29 D5 00            mov r13d, dword ptr [rip + 0xd52908]
002741FC  41 81 E5 00 00 02 00            and r13d, 0x20000
00274203  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
00274207  44 89 6C 24 60                  mov dword ptr [rsp + 0x60], r13d
0027420C  40 F6 C6 03                     test sil, 3
00274210  0F 85 EC 0C 00 00               jne 0x140274f02
00274216  0F B6 86 60 04 00 00            movzx eax, byte ptr [rsi + 0x460]
0027421D  48 8B 53 30                     mov rdx, qword ptr [rbx + 0x30]
00274221  48 8D 7B 30                     lea rdi, [rbx + 0x30]
00274225  48 3B D6                        cmp rdx, rsi
00274228  0F 84 47 05 00 00               je 0x140274775
0027422E  48 85 D2                        test rdx, rdx
00274231  49 8B CF                        mov rcx, r15
00274234  0F 95 C1                        setne cl
00274237  85 C0                           test eax, eax
00274239  0F 85 42 03 00 00               jne 0x140274581
0027423F  8B 53 48                        mov edx, dword ptr [rbx + 0x48]
00274242  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00274245  48 8B 7B 10                     mov rdi, qword ptr [rbx + 0x10]
00274249  48 03 D0                        add rdx, rax
0027424C  48 85 FF                        test rdi, rdi
0027424F  0F 85 59 03 00 00               jne 0x1402745ae
00274255  4C 8B CF                        mov r9, rdi
00274258  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0027425D  4C 8B C6                        mov r8, rsi
00274260  48 8B D3                        mov rdx, rbx
00274263  B9 E3 00 00 00                  mov ecx, 0xe3
00274268  E8 F3 93 28 00                  call 0x1404fd660
0027426D  CC                              int3
0027426E  44 39 73 4C                     cmp dword ptr [rbx + 0x4c], r14d
00274272  0F 85 75 03 00 00               jne 0x1402745ed
00274278  BA 7F FF 00 00                  mov edx, 0xff7f
0027427D  66 44 89 73 18                  mov word ptr [rbx + 0x18], r14w
00274282  66 21 53 1A                     and word ptr [rbx + 0x1a], dx
00274286  41 8B D6                        mov edx, r14d
00274289  E9 1E FE FF FF                  jmp 0x1402740ac
0027428E  44 84 2D 71 28 D5 00            test byte ptr [rip + 0xd52871], r13b
00274295  BE 32 00 01 00                  mov esi, 0x10032
0027429A  8B 43 44                        mov eax, dword ptr [rbx + 0x44]
0027429D  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
002742A1  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
002742A5  0F 84 FF 01 00 00               je 0x1402744aa
002742AB  8B 05 A7 9B C9 00               mov eax, dword ptr [rip + 0xc99ba7]
002742B1  85 C0                           test eax, eax
002742B3  0F 85 F1 01 00 00               jne 0x1402744aa
002742B9  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
002742BD  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
002742C2  E8 29 37 FA FF                  call 0x1402179f0
002742C7  83 3D 52 2A D5 00 00            cmp dword ptr [rip + 0xd52a52], 0
002742CE  0F B6 7C 24 58                  movzx edi, byte ptr [rsp + 0x58]
002742D3  74 0D                           je 0x1402742e2
002742D5  44 0F 20 C1                     mov rcx, cr8
002742D9  40 0F B6 D7                     movzx edx, dil
002742DD  E8 B6 13 28 00                  call 0x1404f5698
002742E2  44 0F 22 C7                     mov cr8, rdi
002742E6  65 FF 04 25 6C 90 00 00         inc dword ptr gs:[0x906c]
002742EE  45 85 E4                        test r12d, r12d
002742F1  0F 84 3F 04 00 00               je 0x140274736
002742F7  0F 57 C0                        xorps xmm0, xmm0
002742FA  0F 11 45 98                     movups xmmword ptr [rbp - 0x68], xmm0
002742FE  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
00274302  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
00274306  0F 31                           rdtsc
00274308  65 4C 8B 34 25 20 00 00 00      mov r14, qword ptr gs:[0x20]
00274311  48 C1 E2 20                     shl rdx, 0x20
00274315  48 0B C2                        or rax, rdx
00274318  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0027431D  41 FF 86 70 8F 00 00            inc dword ptr [r14 + 0x8f70]
00274324  41 0F B6 86 D0 00 00 00         movzx eax, byte ptr [r14 + 0xd0]
0027432C  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00274335  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
0027433A  41 0F B6 86 D1 00 00 00         movzx eax, byte ptr [r14 + 0xd1]
00274342  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00274346  48 83 B9 20 06 00 00 00         cmp qword ptr [rcx + 0x620], 0
0027434E  0F 84 E2 03 00 00               je 0x140274736
00274354  65 4C 8B 2C 25 88 01 00 00      mov r13, qword ptr gs:[0x188]
0027435D  44 8B E6                        mov r12d, esi
00274360  41 81 E4 00 00 FF FF            and r12d, 0xffff0000
00274367  41 8B 85 A0 05 00 00            mov eax, dword ptr [r13 + 0x5a0]
0027436E  A8 01                           test al, 1
00274370  0F 85 C0 03 00 00               jne 0x140274736
00274376  49 8B B5 20 06 00 00            mov rsi, qword ptr [r13 + 0x620]
0027437D  8B 15 E5 40 BF 00               mov edx, dword ptr [rip + 0xbf40e5]
00274383  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
00274387  48 85 F6                        test rsi, rsi
0027438A  75 55                           jne 0x1402743e1
0027438C  BA 00 02 00 00                  mov edx, 0x200
00274391  8D 4E 48                        lea ecx, [rsi + 0x48]
00274394  41 B8 52 65 54 72               mov r8d, 0x72546552
0027439A  E8 51 DD 90 00                  call 0x140b820f0
0027439F  48 8B F8                        mov rdi, rax
002743A2  48 85 C0                        test rax, rax
002743A5  0F 84 8B 03 00 00               je 0x140274736
002743AB  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
002743AF  44 89 60 1C                     mov dword ptr [rax + 0x1c], r12d
002743B3  33 C0                           xor eax, eax
002743B5  89 47 20                        mov dword ptr [rdi + 0x20], eax
002743B8  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
002743BC  89 47 28                        mov dword ptr [rdi + 0x28], eax
002743BF  33 C0                           xor eax, eax
002743C1  F0 49 0F B1 BD 20 06 00 00      lock cmpxchg qword ptr [r13 + 0x620], rdi
002743CA  48 8B F0                        mov rsi, rax
002743CD  0F 84 94 01 00 00               je 0x140274567
002743D3  33 D2                           xor edx, edx
002743D5  48 8B CF                        mov rcx, rdi
002743D8  E8 93 E4 90 00                  call 0x140b82870
002743DD  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
002743E1  45 33 ED                        xor r13d, r13d
002743E4  41 8B C5                        mov eax, r13d
002743E7  41 8B CD                        mov ecx, r13d
002743EA  83 F9 08                        cmp ecx, 8
002743ED  73 32                           jae 0x140274421
002743EF  44 8B 46 1C                     mov r8d, dword ptr [rsi + 0x1c]
002743F3  45 3B C4                        cmp r8d, r12d
002743F6  75 0B                           jne 0x140274403
002743F8  48 39 5E 10                     cmp qword ptr [rsi + 0x10], rbx
002743FC  75 05                           jne 0x140274403
002743FE  39 56 28                        cmp dword ptr [rsi + 0x28], edx
00274401  74 44                           je 0x140274447
00274403  48 85 C0                        test rax, rax
00274406  0F 85 93 00 00 00               jne 0x14027449f
0027440C  45 85 C0                        test r8d, r8d
0027440F  0F 84 87 00 00 00               je 0x14027449c
00274415  39 56 28                        cmp dword ptr [rsi + 0x28], edx
00274418  0F 8D 81 00 00 00               jge 0x14027449f
0027441E  48 8B C6                        mov rax, rsi
00274421  48 8B F0                        mov rsi, rax
00274424  48 85 C0                        test rax, rax
00274427  74 1E                           je 0x140274447
00274429  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0027442D  44 89 60 1C                     mov dword ptr [rax + 0x1c], r12d
00274431  4C 89 68 20                     mov qword ptr [rax + 0x20], r13
00274435  4C 89 28                        mov qword ptr [rax], r13
00274438  4C 89 68 08                     mov qword ptr [rax + 8], r13
0027443C  44 89 68 18                     mov dword ptr [rax + 0x18], r13d
00274440  89 50 28                        mov dword ptr [rax + 0x28], edx
00274443  44 89 68 2C                     mov dword ptr [rax + 0x2c], r13d
00274447  48 8B FE                        mov rdi, rsi
0027444A  48 85 F6                        test rsi, rsi
0027444D  0F 84 E3 02 00 00               je 0x140274736
00274453  83 7F 20 00                     cmp dword ptr [rdi + 0x20], 0
00274457  0F 84 D5 02 00 00               je 0x140274732
0027445D  41 FF 86 74 8F 00 00            inc dword ptr [r14 + 0x8f74]
00274464  41 FF C7                        inc r15d
00274467  44 39 7F 24                     cmp dword ptr [rdi + 0x24], r15d
0027446B  0F 82 23 12 00 00               jb 0x140275694
00274471  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
00274476  41 81 F8 22 00 01 00            cmp r8d, 0x10022
0027447D  0F 84 65 02 00 00               je 0x1402746e8
00274483  41 81 F8 32 00 01 00            cmp r8d, 0x10032
0027448A  0F 85 A6 02 00 00               jne 0x140274736
00274490  C7 47 20 02 00 00 00            mov dword ptr [rdi + 0x20], 2
00274497  E9 9A 02 00 00                  jmp 0x140274736
0027449C  48 8B C6                        mov rax, rsi
0027449F  48 83 C6 40                     add rsi, 0x40
002744A3  FF C1                           inc ecx
002744A5  E9 40 FF FF FF                  jmp 0x1402743ea
002744AA  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
002744AF  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002744B4  48 85 C0                        test rax, rax
002744B7  75 2A                           jne 0x1402744e3
002744B9  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002744BE  48 8D 44 24 48                  lea rax, [rsp + 0x48]
002744C3  45 33 C9                        xor r9d, r9d
002744C6  F0 4C 0F B1 09                  lock cmpxchg qword ptr [rcx], r9
002744CB  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
002744D0  48 3B C1                        cmp rax, rcx
002744D3  0F 84 EE FD FF FF               je 0x1402742c7
002744D9  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
002744DE  E8 BD 35 FA FF                  call 0x140217aa0
002744E3  4C 8D 40 08                     lea r8, [rax + 8]
002744E7  45 33 C9                        xor r9d, r9d
002744EA  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
002744EF  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002744F4  48 8B C1                        mov rax, rcx
002744F7  49 87 00                        xchg qword ptr [r8], rax
002744FA  32 C1                           xor al, cl
002744FC  A8 04                           test al, 4
002744FE  0F 84 C3 FD FF FF               je 0x1402742c7
00274504  F0 44 09 0C 24                  lock or dword ptr [rsp], r9d
00274509  49 C1 E8 05                     shr r8, 5
0027450D  4C 8D 15 EC BA D8 FF            lea r10, [rip - 0x274514]
00274514  41 83 E0 7F                     and r8d, 0x7f
00274518  E8 C3 36 FA FF                  call 0x140217be0
0027451D  41 8B D1                        mov edx, r9d
00274520  0F B6 F8                        movzx edi, al
00274523  4B 87 94 C2 20 1B F2 00         xchg qword ptr [r10 + r8*8 + 0xf21b20], rdx
0027452B  E8 C4 35 FA FF                  call 0x140217af4
00274530  40 84 FF                        test dil, dil
00274533  0F 84 8E FD FF FF               je 0x1402742c7
00274539  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00274542  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00274549  4D 85 C0                        test r8, r8
0027454C  0F 85 63 08 00 00               jne 0x140274db5
00274552  FB                              sti
00274553  E9 6F FD FF FF                  jmp 0x1402742c7
00274558  40 F6 C7 03                     test dil, 3
0027455C  0F 85 0D FB FF FF               jne 0x14027406f
00274562  E9 6E FA FF FF                  jmp 0x140273fd5
00274567  45 33 ED                        xor r13d, r13d
0027456A  E9 E4 FE FF FF                  jmp 0x140274453
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00273F95(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, unsigned __int8 a9, __int64 a10, unsigned __int8 a11, unsigned int a12, __int64 a13, __int64 a14)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int16 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 56))) & (7));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 56))))) >> (3));
    v_r15 = (unsigned int)((result * 8 - 8) | ((unsigned int)(a1)));
    *(unsigned int *)(v_rbx + 56) = (unsigned int)(v_r15);
    v_r15 = (unsigned int)((v_r15) >> (3));
    if ((unsigned int)(v_r15) != 0) goto loc_0027428E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 56)))) & (2)) == 0) goto loc_00274558;
    v_rdi = (*(unsigned __int64 *)(v_rbx + 48)) & (-4);
loc_00273FD5:
    if (v_rdi == 0) goto loc_0027406F;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 56))))) == 0) goto loc_00274020;
    result = 0;
    v_rsi = 0;
    v_r14 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 56))) & (0xFFFFFFFEULL));
    *(unsigned int *)(v_rbx + 56) = (unsigned int)(result);
loc_00274020:
    if ((((unsigned __int8)(result)) & (4)) != 0) {
        result = *(unsigned int *)(v_rbx + 56);
        result = (unsigned int)((result) & (0xFFFFFFFBULL));
        *(unsigned int *)(v_rbx + 56) = (unsigned int)(result);
    }
    if ((((unsigned __int8)(result)) & (2)) == 0) goto loc_0027406F;
    if ((*(unsigned int *)(v_rip + 13963217)) != 0) {
        a4 = 0x746C6644ULL;
        a1 = v_rdi - 48;
        a3 = 1;
        a2 = 0;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
loc_0027406F:
    v_r14 = 0;
    *(unsigned __int64 *)(v_rbx + 48) = 0;
    v_stack_p44 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 68)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 72))) == 0) goto loc_0027426E;
    *(unsigned __int64 *)(v_rbx + 32) = 0;
    v_stack_p70 = *(unsigned __int64 *)(v_rbx + 32);
    *(unsigned int *)(v_rbx + 72) = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 64))) - 1);
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 72)))));
loc_002740AC:
    *(unsigned int *)(v_rbx + 64) = a2;
    if ((*(unsigned int *)(v_rbx + 76)) != 0) goto loc_002740C4;
    if ((*(unsigned int *)(v_rbx + 72)) == 0) {
        a1 = 249;
    }
    result = *(unsigned __int64 *)(v_rbx + 32);
    if (0 != 0) {
        result = *(unsigned int *)(v_rbx + 56);
        result = (unsigned int)((result) & (7));
        *(unsigned __int64 *)(v_rbx + 48) = 0;
        result = (unsigned int)((result) | (8));
        *(unsigned int *)(v_rbx + 56) = (unsigned int)(result);
    }
    if (((*(unsigned __int8 *)(v_rip + 13969953)) & (1)) != 0) goto loc_00274188;
loc_002740EB:
    if (a9 != 0) goto loc_00274121;
    if (a9 == a9) goto loc_002741A4;
    result = KxWaitForLockChainValid(a9, a2, a3, a4);
loc_00274121:
    v_stack_p48 = 0;
    result = (unsigned __int8)((a10) ^ ((unsigned __int8)(a10)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_002741A4;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(a10, a2, a3, a4);
    result = KiHaltOnAddressWakeEntireList(a10, 0, a3, a4);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_002741A4;
    goto loc_002741A4;
loc_00274188:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13212874))) != 0) goto loc_002740EB;
    result = KiReleaseQueuedSpinLockInstrumented(a9, *(unsigned __int64 *)(v_rbp + 72), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
loc_002741A4:
    if ((*(unsigned int *)(v_rip + 13970293)) != 0) {
        a1 = v_cr8;
        a2 = a11;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    }
    v_rdi = 1;
    if (0 != 0) { v_rdi = 3; }
    result = 0;
    v_stack_p38 = (unsigned int)((unsigned int)(0x10022ULL));
    goto loc_002742E6;
loc_0027426E:
    *(unsigned __int16 *)(v_rbx + 24) = 3;
    goto loc_002740AC;
loc_0027428E:
    v_stack_p38 = (unsigned int)((unsigned int)(0x10032ULL));
    v_stack_p44 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 68)));
    if (((*(unsigned __int8 *)(v_rip + 13969521)) & (1)) == 0) goto loc_002744AA;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13212583))) != 0) goto loc_002744AA;
    result = KiReleaseQueuedSpinLockInstrumented(a9, *(unsigned __int64 *)(v_rbp + 72), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
loc_002742C7:
    if ((*(unsigned int *)(v_rip + 13970002)) != 0) {
        a1 = a11;
        a2 = a11;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    }
loc_002742E6:
    *(unsigned __int64 *)(v_rbp - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rbp - 88) = v_xmm0;
    *(unsigned __int64 *)(v_rbp - 72) = v_xmm0;
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_stack_p78 = result;
    v_stack_p40 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_p30 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x10032ULL)))) & (0xFFFF0000ULL));
    v_stack_p60 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12533989)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_002743E1;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), a4);
    *(unsigned __int64 *)(result + 16) = v_rbx;
    *(unsigned int *)(result + 28) = (unsigned int)(v_r12);
    result = 0;
    *(unsigned int *)(result + 32) = 0;
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(a12));
    result = 0;
    if (condition_is_equal) goto loc_00274567;
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, (unsigned int)(0x72546552ULL), a4);
loc_002743E1:
    v_r13 = 0;
loc_002743EA:
    if (0 >= 8) goto loc_00274421;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != ((unsigned int)(v_r12))) goto loc_00274403;
    if ((*(unsigned __int64 *)(0 + 16)) != v_rbx) goto loc_00274403;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(a12)))) goto loc_00274447;
loc_00274403:
    if (0 != 0) goto loc_0027449F;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28))) == 0) goto loc_0027449C;
    if ((*(unsigned int *)(0 + 40)) >= ((unsigned int)((unsigned int)(a12)))) goto loc_0027449F;
loc_00274421:
    if (0 != 0) {
        *(unsigned __int64 *)(0 + 16) = v_rbx;
        *(unsigned int *)(0 + 28) = (unsigned int)(v_r12);
        *(unsigned __int64 *)(0 + 32) = 0;
        *(unsigned __int64 *)(0) = 0;
        *(unsigned __int64 *)(0 + 8) = 0;
        *(unsigned int *)(0 + 24) = 0;
        *(unsigned int *)(0 + 40) = (unsigned int)((unsigned int)(a12));
        *(unsigned int *)(0 + 44) = 0;
    }
loc_00274453:
    v_r15 = (unsigned int)((0) + 1);
    *(unsigned int *)(0 + 32) = 2;
loc_0027449C:
loc_0027449F:
    v_rsi = (0) + (64);
    a1 = (unsigned int)((0) + 1);
    goto loc_002743EA;
loc_002744AA:
    if (a9 != 0) goto loc_002744E3;
    a4 = 0;
    if (a9 == a9) goto loc_002742C7;
    result = KxWaitForLockChainValid(a9, (unsigned int)(a12), (unsigned int)(a7), a4);
loc_002744E3:
    a4 = 0;
    v_stack_p48 = 0;
    result = (unsigned __int8)((a10) ^ ((unsigned __int8)(a10)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_002742C7;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(a10, (unsigned int)(a12), a3, a4);
    result = KiHaltOnAddressWakeEntireList(a10, 0, a3, a4);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_002742C7;
    goto loc_002742C7;
loc_00274558:
    if ((((unsigned __int8)((unsigned __int8)(result))) & (3)) != 0) goto loc_0027406F;
    goto loc_00273FD5;
loc_00274567:
    v_r13 = 0;
    goto loc_00274453;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00273F95(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint32_t Arg7, uint64_t Arg8, uint8_t Arg9, void *Arg10, uint8_t Arg11, uint32_t Arg12, uint64_t Arg13, int64_t Arg14)
{
    uint8_t *arg10 = (uint8_t *)Arg10;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    uint32_t v_stack_p0;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint32_t v_stack_p38;
    uint16_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint32_t v_stack_p60;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x38))) & (7));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x38))))) >> (3));
    local_r15 = (uint32_t)((result * 8 - 8) | ((uint32_t)(Arg1)));
    *(uint32_t *)(local_rbx + 0x38) = (uint32_t)(local_r15);
    local_r15 = (uint32_t)((local_r15) >> (3));
    if ((uint32_t)(local_r15) != 0) goto loc_0027428E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x38)))) & (2)) == 0) goto loc_00274558;
    local_rdi = (*(uint64_t *)(local_rbx + 0x30)) & (-4);
loc_00273FD5:
    if (local_rdi == 0) goto loc_0027406F;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x38))))) == 0) goto loc_00274020;
    result = 0;
    local_rsi = 0;
    local_r14 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x38))) & (0xFFFFFFFEULL));
    *(uint32_t *)(local_rbx + 0x38) = (uint32_t)(result);
loc_00274020:
    if ((((uint8_t)(result)) & (4)) != 0) {
        result = *(uint32_t *)(local_rbx + 0x38);
        result = (uint32_t)((result) & (0xFFFFFFFBULL));
        *(uint32_t *)(local_rbx + 0x38) = (uint32_t)(result);
    }
    if ((((uint8_t)(result)) & (2)) == 0) goto loc_0027406F;
    if ((*(uint32_t *)(v_rip + 0xD50FD1)) != 0) {
        Arg4 = 0x746C6644ULL;
        Arg1 = local_rdi - 48;
        Arg3 = 1;
        Arg2 = 0;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (-1) - (1);
loc_0027406F:
    local_r14 = 0;
    *(uint64_t *)(local_rbx + 0x30) = 0;
    v_stack_p44 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x44)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x48))) == 0) goto loc_0027426E;
    *(uint64_t *)(local_rbx + 0x20) = 0;
    v_stack_p70 = *(uint64_t *)(local_rbx + 0x20);
    *(uint32_t *)(local_rbx + 0x48) = 0;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x40))) - 1);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x48)))));
loc_002740AC:
    *(uint32_t *)(local_rbx + 0x40) = Arg2;
    if ((*(uint32_t *)(local_rbx + 0x4C)) != 0) goto loc_002740C4;
    if ((*(uint32_t *)(local_rbx + 0x48)) == 0) {
        Arg1 = 249;
    }
    result = *(uint64_t *)(local_rbx + 0x20);
    if (0 != 0) {
        result = *(uint32_t *)(local_rbx + 0x38);
        result = (uint32_t)((result) & (7));
        *(uint64_t *)(local_rbx + 0x30) = 0;
        result = (uint32_t)((result) | (8));
        *(uint32_t *)(local_rbx + 0x38) = (uint32_t)(result);
    }
    if (((*(uint8_t *)(v_rip + 0xD52A21)) & (1)) != 0) goto loc_00274188;
loc_002740EB:
    if (Arg9 != 0) goto loc_00274121;
    if (Arg9 == Arg9) goto loc_002741A4;
    result = KxWaitForLockChainValid(Arg9, Arg2, Arg3, Arg4);
loc_00274121:
    v_stack_p48 = 0;
    result = (uint8_t)((Arg10) ^ ((uint8_t)(Arg10)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_002741A4;
    Arg3 = (result + 8) >> (5);
    Arg3 = (uint32_t)((Arg3) & (127));
    result = KeDisableInterrupts(Arg10, Arg2, Arg3, Arg4);
    result = KiHaltOnAddressWakeEntireList(Arg10, 0, Arg3, Arg4);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_002741A4;
    goto loc_002741A4;
loc_00274188:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC99CCA))) != 0) goto loc_002740EB;
    result = KiReleaseQueuedSpinLockInstrumented(Arg9, *(uint64_t *)(local_rbp + 0x48), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
loc_002741A4:
    if ((*(uint32_t *)(v_rip + 0xD52B75)) != 0) {
        Arg1 = v_cr8;
        Arg2 = Arg11;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    }
    local_rdi = 1;
    if (0 != 0) { local_rdi = 3; }
    result = 0;
    v_stack_p38 = (uint32_t)((uint32_t)(0x10022ULL));
    goto loc_002742E6;
loc_0027426E:
    *(uint16_t *)(local_rbx + 0x18) = 3;
    goto loc_002740AC;
loc_0027428E:
    v_stack_p38 = (uint32_t)((uint32_t)(0x10032ULL));
    v_stack_p44 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x44)));
    if (((*(uint8_t *)(v_rip + 0xD52871)) & (1)) == 0) goto loc_002744AA;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC99BA7))) != 0) goto loc_002744AA;
    result = KiReleaseQueuedSpinLockInstrumented(Arg9, *(uint64_t *)(local_rbp + 0x48), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
loc_002742C7:
    if ((*(uint32_t *)(v_rip + 0xD52A52)) != 0) {
        Arg1 = Arg11;
        Arg2 = Arg11;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    }
loc_002742E6:
    *(uint64_t *)(local_rbp - 0x68) = v_xmm0;
    *(uint64_t *)(local_rbp - 0x58) = v_xmm0;
    *(uint64_t *)(local_rbp - 0x48) = v_xmm0;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    v_stack_p78 = result;
    v_stack_p40 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_p30 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x10032ULL)))) & (0xFFFF0000ULL));
    v_stack_p60 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF40E5)));
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_002743E1;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), Arg4);
    *(uint64_t *)(result + 0x10) = local_rbx;
    *(uint32_t *)(result + 0x1C) = (uint32_t)(local_r12);
    result = 0;
    *(uint32_t *)(result + 0x20) = 0;
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(Arg12));
    result = 0;
    if (condition_is_equal) goto loc_00274567;
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, (uint32_t)(0x72546552ULL), Arg4);
loc_002743E1:
    local_r13 = 0;
loc_002743EA:
    if (0 >= 8) goto loc_00274421;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != ((uint32_t)(local_r12))) goto loc_00274403;
    if ((*(uint64_t *)(0 + 0x10)) != local_rbx) goto loc_00274403;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(Arg12)))) goto loc_00274447;
loc_00274403:
    if (0 != 0) goto loc_0027449F;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C))) == 0) goto loc_0027449C;
    if ((*(uint32_t *)(0 + 0x28)) >= ((uint32_t)((uint32_t)(Arg12)))) goto loc_0027449F;
loc_00274421:
    if (0 != 0) {
        *(uint64_t *)(0 + 0x10) = local_rbx;
        *(uint32_t *)(0 + 0x1C) = (uint32_t)(local_r12);
        *(uint64_t *)(0 + 0x20) = 0;
        *(uint64_t *)(0) = 0;
        *(uint64_t *)(0 + 0x8) = 0;
        *(uint32_t *)(0 + 0x18) = 0;
        *(uint32_t *)(0 + 0x28) = (uint32_t)((uint32_t)(Arg12));
        *(uint32_t *)(0 + 0x2C) = 0;
    }
loc_00274453:
    local_r15 = (uint32_t)((0) + 1);
    *(uint32_t *)(0 + 0x20) = 2;
loc_0027449C:
loc_0027449F:
    local_rsi = (0) + (64);
    Arg1 = (uint32_t)((0) + 1);
    goto loc_002743EA;
loc_002744AA:
    if (Arg9 != 0) goto loc_002744E3;
    Arg4 = 0;
    if (Arg9 == Arg9) goto loc_002742C7;
    result = KxWaitForLockChainValid(Arg9, (uint32_t)(Arg12), (uint32_t)(Arg7), Arg4);
loc_002744E3:
    Arg4 = 0;
    v_stack_p48 = 0;
    result = (uint8_t)((Arg10) ^ ((uint8_t)(Arg10)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_002742C7;
    Arg3 = (result + 8) >> (5);
    Arg3 = (uint32_t)((Arg3) & (127));
    result = KeDisableInterrupts(Arg10, (uint32_t)(Arg12), Arg3, Arg4);
    result = KiHaltOnAddressWakeEntireList(Arg10, 0, Arg3, Arg4);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_002742C7;
    goto loc_002742C7;
loc_00274558:
    if ((((uint8_t)((uint8_t)(result))) & (3)) != 0) goto loc_0027406F;
    goto loc_00273FD5;
loc_00274567:
    local_r13 = 0;
    goto loc_00274453;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg10` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00273F95&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
