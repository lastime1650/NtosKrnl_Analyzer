# ExpAcquireFastResourceSharedSlow

- RVA: `0x00211260`–`0x00211BB9` (길이 `2,393` bytes)
- VA: `0x0000000140211260`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DE60`
- 디코드: `599`개 명령, `2,393/2,393` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0021149E` → [KxWaitForLockChainValid](KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x002114BB` → [KeWakeAddressAll](KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x00211517` → [KiReleaseQueuedSpinLockInstrumented](KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x002115B3` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x002115D7` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00211624` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00211632` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0021168C` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002116A9` → [ExpWaitForFastResource](../3B/ExpWaitForFastResource_function_003BE760.md) (function, `0x003BE760`)
- `0x002116F5` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00211758` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00211780` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0021178E` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0021186A` → [KiAbEntryRemoveFromTree](../26/KiAbEntryRemoveFromTree_function_00262410.md) (function, `0x00262410`)
- `0x00211886` → [ObfReferenceObjectWithTag](ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x002118F9` → [KeAbPostReleaseEx](../26/KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x002119B9` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x002119D4` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002119F7` → [KeAbMarkCrossThreadReleasable](../3B/KeAbMarkCrossThreadReleasable_function_003BE8AC.md) (function, `0x003BE8AC`)
- `0x00211A1F` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00211A40` → [ObfReferenceObjectWithTag](ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00211A64` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00211ACE` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00211AE4` → [KeAbMarkCrossThreadReleasable](../3B/KeAbMarkCrossThreadReleasable_function_003BE8AC.md) (function, `0x003BE8AC`)
- `0x00211B06` → [KeAbPostReleaseEx](../26/KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x00211B1A` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x00211B4D` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x00211B61` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x00211B8F` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x00211BA2` → [KeAbPreAcquire](KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00211BAF` → [KeAbMarkCrossThreadReleasable](../3B/KeAbMarkCrossThreadReleasable_function_003BE8AC.md) (function, `0x003BE8AC`)

### Direct callers
- [sub_00210F9D](Unknown_function_00210F9D.md) at `0x002110E3`
- [sub_00211C19](Unknown_function_00211C19.md) at `0x00211C98`
- [ExAcquireFastResourceSharedStarveExclusive](../3B/ExAcquireFastResourceSharedStarveExclusive_function_003BDC80.md) at `0x003BDED2`
- [ExAcquireFastResourceWithFlags](../65/ExAcquireFastResourceWithFlags_function_00658120.md) at `0x0065862F`

### Static image references
- `0x00211340` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00211384` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00211501` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00211260  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00211265  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0021126A  55                              push rbp
0021126B  56                              push rsi
0021126C  57                              push rdi
0021126D  41 54                           push r12
0021126F  41 55                           push r13
00211271  41 56                           push r14
00211273  41 57                           push r15
00211275  48 8B EC                        mov rbp, rsp
00211278  48 81 EC 80 00 00 00            sub rsp, 0x80
0021127F  33 C0                           xor eax, eax
00211281  0F 57 C9                        xorps xmm1, xmm1
00211284  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00211288  45 32 E4                        xor r12b, r12b
0021128B  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0021128F  40 32 F6                        xor sil, sil
00211292  8B 45 60                        mov eax, dword ptr [rbp + 0x60]
00211295  4D 8B D1                        mov r10, r9
00211298  44 8B F8                        mov r15d, eax
0021129B  4C 89 65 A8                     mov qword ptr [rbp - 0x58], r12
0021129F  83 E0 10                        and eax, 0x10
002112A2  41 83 E7 08                     and r15d, 8
002112A6  45 32 C9                        xor r9b, r9b
002112A9  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
002112AC  0F 57 C0                        xorps xmm0, xmm0
002112AF  44 88 4D 40                     mov byte ptr [rbp + 0x40], r9b
002112B3  49 8B F8                        mov rdi, r8
002112B6  4C 8B EA                        mov r13, rdx
002112B9  48 8B D9                        mov rbx, rcx
002112BC  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
002112C0  0F 11 4D C8                     movups xmmword ptr [rbp - 0x38], xmm1
002112C4  0F 11 4D D8                     movups xmmword ptr [rbp - 0x28], xmm1
002112C8  0F 11 4D E8                     movups xmmword ptr [rbp - 0x18], xmm1
002112CC  FA                              cli
002112CD  48 8B 01                        mov rax, qword ptr [rcx]
002112D0  41 B3 01                        mov r11b, 1
002112D3  45 33 F6                        xor r14d, r14d
002112D6  44 88 5D A0                     mov byte ptr [rbp - 0x60], r11b
002112DA  41 84 C3                        test r11b, al
002112DD  0F 85 DA 02 00 00               jne 0x1402115bd
002112E3  4D 8D 82 B8 06 00 00            lea r8, [r10 + 0x6b8]
002112EA  4D 8B CE                        mov r9, r14
002112ED  49 8B 08                        mov rcx, qword ptr [r8]
002112F0  49 8B D6                        mov rdx, r14
002112F3  49 3B C8                        cmp rcx, r8
002112F6  74 17                           je 0x14021130f
002112F8  F6 41 25 02                     test byte ptr [rcx + 0x25], 2
002112FC  0F 85 01 06 00 00               jne 0x140211903
00211302  48 39 59 18                     cmp qword ptr [rcx + 0x18], rbx
00211306  0F 85 F7 05 00 00               jne 0x140211903
0021130C  48 8B D1                        mov rdx, rcx
0021130F  45 32 C9                        xor r9b, r9b
00211312  48 83 FA 01                     cmp rdx, 1
00211316  0F 84 F7 05 00 00               je 0x140211913
0021131C  48 85 D2                        test rdx, rdx
0021131F  0F 85 6B 05 00 00               jne 0x140211890
00211325  45 85 FF                        test r15d, r15d
00211328  0F 84 26 05 00 00               je 0x140211854
0021132E  45 84 DB                        test r11b, r11b
00211331  74 44                           je 0x140211377
00211333  44 0F 20 C6                     mov rsi, cr8
00211337  B8 02 00 00 00                  mov eax, 2
0021133C  44 0F 22 C0                     mov cr8, rax
00211340  44 39 35 D9 59 DB 00            cmp dword ptr [rip + 0xdb59d9], r14d
00211347  0F 85 83 02 00 00               jne 0x1402115d0
0021134D  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00211356  44 0F B6 E6                     movzx r12d, sil
0021135A  4C 89 65 A8                     mov qword ptr [rbp - 0x58], r12
0021135E  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00211365  4D 85 C0                        test r8, r8
00211368  0F 85 98 02 00 00               jne 0x140211606
0021136E  FB                              sti
0021136F  C6 45 40 01                     mov byte ptr [rbp + 0x40], 1
00211373  44 88 75 A0                     mov byte ptr [rbp - 0x60], r14b
00211377  48 8D 4B 30                     lea rcx, [rbx + 0x30]
0021137B  4C 89 75 B0                     mov qword ptr [rbp - 0x50], r14
0021137F  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
00211383  90                              nop
00211384  F6 05 7B 57 DB 00 21            test byte ptr [rip + 0xdb577b], 0x21
0021138B  0F 85 0D 02 00 00               jne 0x14021159e
00211391  48 8D 55 B0                     lea rdx, [rbp - 0x50]
00211395  48 87 11                        xchg qword ptr [rcx], rdx
00211398  48 85 D2                        test rdx, rdx
0021139B  0F 85 8D 02 00 00               jne 0x14021162e
002113A1  0F 0D 0B                        prefetchw byte ptr [rbx]
002113A4  48 8B 03                        mov rax, qword ptr [rbx]
002113A7  44 8B 4D 60                     mov r9d, dword ptr [rbp + 0x60]
002113AB  45 32 C0                        xor r8b, r8b
002113AE  4C 39 73 10                     cmp qword ptr [rbx + 0x10], r14
002113B2  0F 84 33 01 00 00               je 0x1402114eb
002113B8  48 8B C8                        mov rcx, rax
002113BB  48 83 C9 02                     or rcx, 2
002113BF  48 8B D1                        mov rdx, rcx
002113C2  F6 C1 02                        test cl, 2
002113C5  0F 84 F7 00 00 00               je 0x1402114c2
002113CB  41 F6 C1 04                     test r9b, 4
002113CF  0F 85 F7 00 00 00               jne 0x1402114cc
002113D5  48 83 C9 02                     or rcx, 2
002113D9  48 3B C8                        cmp rcx, rax
002113DC  74 07                           je 0x1402113e5
002113DE  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
002113E3  75 C6                           jne 0x1402113ab
002113E5  45 84 C0                        test r8b, r8b
002113E8  0F 85 9C 03 00 00               jne 0x14021178a
002113EE  FF 43 38                        inc dword ptr [rbx + 0x38]
002113F1  48 85 FF                        test rdi, rdi
002113F4  74 23                           je 0x140211419
002113F6  0F B6 07                        movzx eax, byte ptr [rdi]
002113F9  0C 02                           or al, 2
002113FB  88 07                           mov byte ptr [rdi], al
002113FD  90                              nop
002113FE  48 8B 07                        mov rax, qword ptr [rdi]
00211401  48 C1 E8 3F                     shr rax, 0x3f
00211405  84 C0                           test al, al
00211407  0F 85 5A 04 00 00               jne 0x140211867
0021140D  C6 47 09 01                     mov byte ptr [rdi + 9], 1
00211411  90                              nop
00211412  0F B6 07                        movzx eax, byte ptr [rdi]
00211415  24 FD                           and al, 0xfd
00211417  88 07                           mov byte ptr [rdi], al
00211419  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
0021141D  48 8D 45 E8                     lea rax, [rbp - 0x18]
00211421  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00211425  48 8D 45 E8                     lea rax, [rbp - 0x18]
00211429  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0021142D  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00211431  4C 89 75 D0                     mov qword ptr [rbp - 0x30], r14
00211435  48 C7 45 E0 01 00 06 00         mov qword ptr [rbp - 0x20], 0x60001
0021143D  48 89 55 D8                     mov qword ptr [rbp - 0x28], rdx
00211441  48 89 7D F8                     mov qword ptr [rbp - 8], rdi
00211445  48 85 C0                        test rax, rax
00211448  0F 85 93 01 00 00               jne 0x1402115e1
0021144E  48 8D 45 C8                     lea rax, [rbp - 0x38]
00211452  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00211456  48 8D 45 C8                     lea rax, [rbp - 0x38]
0021145A  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0021145E  48 8D 45 C8                     lea rax, [rbp - 0x38]
00211462  48 89 43 08                     mov qword ptr [rbx + 8], rax
00211466  F6 05 99 56 DB 00 01            test byte ptr [rip + 0xdb5699], 1
0021146D  0F 85 8E 00 00 00               jne 0x140211501
00211473  0F 0D 4D B0                     prefetchw byte ptr [rbp - 0x50]
00211477  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
0021147B  48 85 C0                        test rax, rax
0021147E  75 23                           jne 0x1402114a3
00211480  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
00211484  48 8D 45 B0                     lea rax, [rbp - 0x50]
00211488  F0 4C 0F B1 31                  lock cmpxchg qword ptr [rcx], r14
0021148D  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00211491  48 3B C1                        cmp rax, rcx
00211494  0F 84 86 00 00 00               je 0x140211520
0021149A  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0021149E  E8 FD 65 00 00                  call 0x140217aa0
002114A3  48 8D 48 08                     lea rcx, [rax + 8]
002114A7  4C 89 75 B0                     mov qword ptr [rbp - 0x50], r14
002114AB  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
002114AF  48 8B C2                        mov rax, rdx
002114B2  48 87 01                        xchg qword ptr [rcx], rax
002114B5  32 C2                           xor al, dl
002114B7  A8 04                           test al, 4
002114B9  74 61                           je 0x14021151c
002114BB  E8 60 67 00 00                  call 0x140217c20
002114C0  EB 5A                           jmp 0x14021151c
002114C2  41 F6 C1 02                     test r9b, 2
002114C6  0F 84 FF FE FF FF               je 0x1402113cb
002114CC  F6 C1 01                        test cl, 1
002114CF  0F 85 00 FF FF FF               jne 0x1402113d5
002114D5  48 83 C1 04                     add rcx, 4
002114D9  41 B0 01                        mov r8b, 1
002114DC  48 33 CA                        xor rcx, rdx
002114DF  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
002114E3  48 33 CA                        xor rcx, rdx
002114E6  E9 EE FE FF FF                  jmp 0x1402113d9
002114EB  44 39 73 38                     cmp dword ptr [rbx + 0x38], r14d
002114EF  0F 87 C3 FE FF FF               ja 0x1402113b8
002114F5  48 8B C8                        mov rcx, rax
002114F8  48 83 E1 FD                     and rcx, 0xfffffffffffffffd
002114FC  E9 BE FE FF FF                  jmp 0x1402113bf
00211501  8B 05 51 C9 CF 00               mov eax, dword ptr [rip + 0xcfc951]
00211507  85 C0                           test eax, eax
00211509  0F 85 64 FF FF FF               jne 0x140211473
0021150F  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
00211513  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00211517  E8 D4 64 00 00                  call 0x1402179f0
0021151C  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
00211520  44 39 75 A4                     cmp dword ptr [rbp - 0x5c], r14d
00211524  B8 04 00 00 00                  mov eax, 4
00211529  45 8B E6                        mov r12d, r14d
0021152C  44 0F 45 E0                     cmovne r12d, eax
00211530  41 8B F4                        mov esi, r12d
00211533  45 8B FC                        mov r15d, r12d
00211536  23 F0                           and esi, eax
00211538  41 83 E7 02                     and r15d, 2
0021153C  48 8D 43 40                     lea rax, [rbx + 0x40]
00211540  41 83 E4 08                     and r12d, 8
00211544  4C 3B E8                        cmp r13, rax
00211547  74 04                           je 0x14021154d
00211549  49 89 5D 18                     mov qword ptr [r13 + 0x18], rbx
0021154D  85 F6                           test esi, esi
0021154F  41 C7 45 20 01 00 00 00         mov dword ptr [r13 + 0x20], 1
00211557  41 0F 95 C6                     setne r14b
0021155B  4C 0B F2                        or r14, rdx
0021155E  4D 89 75 10                     mov qword ptr [r13 + 0x10], r14
00211562  48 85 FF                        test rdi, rdi
00211565  74 0E                           je 0x140211575
00211567  0F B6 47 08                     movzx eax, byte ptr [rdi + 8]
0021156B  24 3F                           and al, 0x3f
0021156D  02 C0                           add al, al
0021156F  0C 01                           or al, 1
00211571  41 88 45 24                     mov byte ptr [r13 + 0x24], al
00211575  45 85 FF                        test r15d, r15d
00211578  74 01                           je 0x14021157b
0021157A  FA                              cli
0021157B  85 F6                           test esi, esi
0021157D  0F 85 D4 05 00 00               jne 0x140211b57
00211583  48 8D 82 B8 06 00 00            lea rax, [rdx + 0x6b8]
0021158A  48 8B 08                        mov rcx, qword ptr [rax]
0021158D  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00211591  0F 84 A5 00 00 00               je 0x14021163c
00211597  B9 03 00 00 00                  mov ecx, 3
0021159C  CD 29                           int 0x29
0021159E  8B 05 B4 C8 CF 00               mov eax, dword ptr [rip + 0xcfc8b4]
002115A4  85 C0                           test eax, eax
002115A6  0F 85 E5 FD FF FF               jne 0x140211391
002115AC  48 8B D1                        mov rdx, rcx
002115AF  48 8D 4D B0                     lea rcx, [rbp - 0x50]
002115B3  E8 98 42 06 00                  call 0x140275850
002115B8  E9 E4 FD FF FF                  jmp 0x1402113a1
002115BD  4C 39 51 50                     cmp qword ptr [rcx + 0x50], r10
002115C1  0F 85 1C FD FF FF               jne 0x1402112e3
002115C7  48 8D 51 40                     lea rdx, [rcx + 0x40]
002115CB  E9 42 FD FF FF                  jmp 0x140211312
002115D0  0F B6 D0                        movzx edx, al
002115D3  40 0F B6 CE                     movzx ecx, sil
002115D7  E8 20 41 2E 00                  call 0x1404f56fc
002115DC  E9 6C FD FF FF                  jmp 0x14021134d
002115E1  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
002115E5  48 39 01                        cmp qword ptr [rcx], rax
002115E8  75 AD                           jne 0x140211597
002115EA  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
002115EE  4C 8D 45 C8                     lea r8, [rbp - 0x38]
002115F2  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
002115F6  4C 89 01                        mov qword ptr [rcx], r8
002115F9  48 8D 4D C8                     lea rcx, [rbp - 0x38]
002115FD  48 89 48 08                     mov qword ptr [rax + 8], rcx
00211601  E9 58 FE FF FF                  jmp 0x14021145e
00211606  41 0F 0D 08                     prefetchw byte ptr [r8]
0021160A  41 8B 00                        mov eax, dword ptr [r8]
0021160D  8B D0                           mov edx, eax
0021160F  0F BA F2 15                     btr edx, 0x15
00211613  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00211618  75 F3                           jne 0x14021160d
0021161A  0F BA E0 15                     bt eax, 0x15
0021161E  0F 83 4A FD FF FF               jae 0x14021136e
00211624  E8 A7 1B 05 00                  call 0x1402631d0
00211629  E9 40 FD FF FF                  jmp 0x14021136e
0021162E  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00211632  E8 79 68 04 00                  call 0x140257eb0
00211637  E9 65 FD FF FF                  jmp 0x1402113a1
0021163C  49 89 4D 00                     mov qword ptr [r13], rcx
00211640  49 89 45 08                     mov qword ptr [r13 + 8], rax
00211644  4C 89 69 08                     mov qword ptr [rcx + 8], r13
00211648  4C 89 28                        mov qword ptr [rax], r13
0021164B  45 85 FF                        test r15d, r15d
0021164E  74 1A                           je 0x14021166a
00211650  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00211659  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00211660  4D 85 C0                        test r8, r8
00211663  0F 85 F9 00 00 00               jne 0x140211762
00211669  FB                              sti
0021166A  85 F6                           test esi, esi
0021166C  0F 85 02 02 00 00               jne 0x140211874
00211672  41 80 4D 25 04                  or byte ptr [r13 + 0x25], 4
00211677  83 3D A2 56 DB 00 00            cmp dword ptr [rip + 0xdb56a2], 0
0021167E  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
00211682  74 0D                           je 0x140211691
00211684  44 0F 20 C1                     mov rcx, cr8
00211688  41 0F B6 D6                     movzx edx, r14b
0021168C  E8 07 40 2E 00                  call 0x1404f5698
00211691  41 0F B6 C6                     movzx eax, r14b
00211695  44 0F 22 C0                     mov cr8, rax
00211699  41 B8 44 02 01 00               mov r8d, 0x10244
0021169F  48 8D 55 C8                     lea rdx, [rbp - 0x38]
002116A3  48 8B CB                        mov rcx, rbx
002116A6  45 32 FF                        xor r15b, r15b
002116A9  E8 B2 D0 1A 00                  call 0x1403be760
002116AE  41 80 65 25 FB                  and byte ptr [r13 + 0x25], 0xfb
002116B3  48 85 FF                        test rdi, rdi
002116B6  0F 85 DD 04 00 00               jne 0x140211b99
002116BC  44 0F B6 6D A0                  movzx r13d, byte ptr [rbp - 0x60]
002116C1  40 B6 01                        mov sil, 1
002116C4  45 84 ED                        test r13b, r13b
002116C7  74 16                           je 0x1402116df
002116C9  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
002116D2  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
002116D9  4D 85 C0                        test r8, r8
002116DC  75 60                           jne 0x14021173e
002116DE  FB                              sti
002116DF  45 84 FF                        test r15b, r15b
002116E2  74 1E                           je 0x140211702
002116E4  83 3D 35 56 DB 00 00            cmp dword ptr [rip + 0xdb5635], 0
002116EB  74 0D                           je 0x1402116fa
002116ED  44 0F 20 C1                     mov rcx, cr8
002116F1  41 0F B6 D6                     movzx edx, r14b
002116F5  E8 9E 3F 2E 00                  call 0x1404f5698
002116FA  41 0F B6 C6                     movzx eax, r14b
002116FE  44 0F 22 C0                     mov cr8, rax
00211702  48 85 FF                        test rdi, rdi
00211705  74 17                           je 0x14021171e
00211707  40 84 F6                        test sil, sil
0021170A  0F 84 E3 01 00 00               je 0x1402118f3
00211710  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
00211714  83 7D A4 00                     cmp dword ptr [rbp - 0x5c], 0
00211718  0F 85 8E 04 00 00               jne 0x140211bac
0021171E  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
00211726  40 0F B6 C6                     movzx eax, sil
0021172A  48 81 C4 80 00 00 00            add rsp, 0x80
00211731  41 5F                           pop r15
00211733  41 5E                           pop r14
00211735  41 5D                           pop r13
00211737  41 5C                           pop r12
00211739  5F                              pop rdi
0021173A  5E                              pop rsi
0021173B  5D                              pop rbp
0021173C  C3                              ret
0021173D  CC                              int3
0021173E  41 0F 0D 08                     prefetchw byte ptr [r8]
00211742  41 8B 00                        mov eax, dword ptr [r8]
00211745  8B D0                           mov edx, eax
00211747  0F BA F2 15                     btr edx, 0x15
0021174B  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00211750  75 F3                           jne 0x140211745
00211752  0F BA E0 15                     bt eax, 0x15
00211756  73 86                           jae 0x1402116de
00211758  E8 73 1A 05 00                  call 0x1402631d0
0021175D  E9 7C FF FF FF                  jmp 0x1402116de
00211762  41 0F 0D 08                     prefetchw byte ptr [r8]
00211766  41 8B 00                        mov eax, dword ptr [r8]
00211769  8B D0                           mov edx, eax
0021176B  0F BA F2 15                     btr edx, 0x15
0021176F  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00211774  75 F3                           jne 0x140211769
00211776  0F BA E0 15                     bt eax, 0x15
0021177A  0F 83 E9 FE FF FF               jae 0x140211669
00211780  E8 4B 1A 05 00                  call 0x1402631d0
00211785  E9 DF FE FF FF                  jmp 0x140211669
0021178A  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0021178E  E8 1D 5A 00 00                  call 0x1402171b0
00211793  44 39 75 A4                     cmp dword ptr [rbp - 0x5c], r14d
00211797  B8 0D 00 00 00                  mov eax, 0xd
0021179C  41 BC 01 00 00 00               mov r12d, 1
002117A2  44 0F 45 E0                     cmovne r12d, eax
002117A6  48 8D 43 40                     lea rax, [rbx + 0x40]
002117AA  45 8B FC                        mov r15d, r12d
002117AD  41 8B F4                        mov esi, r12d
002117B0  41 83 E7 02                     and r15d, 2
002117B4  83 E6 04                        and esi, 4
002117B7  41 83 E4 08                     and r12d, 8
002117BB  4C 3B E8                        cmp r13, rax
002117BE  74 04                           je 0x1402117c4
002117C0  49 89 5D 18                     mov qword ptr [r13 + 0x18], rbx
002117C4  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
002117C8  85 F6                           test esi, esi
002117CA  49 8B C6                        mov rax, r14
002117CD  41 C7 45 20 01 00 00 00         mov dword ptr [r13 + 0x20], 1
002117D5  0F 95 C0                        setne al
002117D8  48 0B C1                        or rax, rcx
002117DB  49 89 45 10                     mov qword ptr [r13 + 0x10], rax
002117DF  48 85 FF                        test rdi, rdi
002117E2  74 12                           je 0x1402117f6
002117E4  0F B6 47 08                     movzx eax, byte ptr [rdi + 8]
002117E8  24 3F                           and al, 0x3f
002117EA  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
002117EE  02 C0                           add al, al
002117F0  0C 01                           or al, 1
002117F2  41 88 45 24                     mov byte ptr [r13 + 0x24], al
002117F6  45 85 FF                        test r15d, r15d
002117F9  74 01                           je 0x1402117fc
002117FB  FA                              cli
002117FC  85 F6                           test esi, esi
002117FE  0F 85 0F 03 00 00               jne 0x140211b13
00211804  48 8D 81 B8 06 00 00            lea rax, [rcx + 0x6b8]
0021180B  48 8B 08                        mov rcx, qword ptr [rax]
0021180E  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00211812  0F 85 7F FD FF FF               jne 0x140211597
00211818  49 89 4D 00                     mov qword ptr [r13], rcx
0021181C  49 89 45 08                     mov qword ptr [r13 + 8], rax
00211820  4C 89 69 08                     mov qword ptr [rcx + 8], r13
00211824  4C 89 28                        mov qword ptr [rax], r13
00211827  45 85 FF                        test r15d, r15d
0021182A  74 1A                           je 0x140211846
0021182C  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00211835  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0021183C  4D 85 C0                        test r8, r8
0021183F  0F 85 56 01 00 00               jne 0x14021199b
00211845  FB                              sti
00211846  85 F6                           test esi, esi
00211848  0F 85 E0 01 00 00               jne 0x140211a2e
0021184E  49 8B FE                        mov rdi, r14
00211851  40 B6 01                        mov sil, 1
00211854  44 0F B6 6D A0                  movzx r13d, byte ptr [rbp - 0x60]
00211859  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0021185D  44 0F B6 7D 40                  movzx r15d, byte ptr [rbp + 0x40]
00211862  E9 5D FE FF FF                  jmp 0x1402116c4
00211867  48 8B CF                        mov rcx, rdi
0021186A  E8 A1 0B 05 00                  call 0x140262410
0021186F  E9 99 FB FF FF                  jmp 0x14021140d
00211874  45 85 E4                        test r12d, r12d
00211877  0F 85 6E 01 00 00               jne 0x1402119eb
0021187D  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
00211881  BA 44 66 6C 74                  mov edx, 0x746c6644
00211886  E8 85 EE FF FF                  call 0x140210710
0021188B  E9 E2 FD FF FF                  jmp 0x140211672
00211890  F6 42 25 04                     test byte ptr [rdx + 0x25], 4
00211894  0F 85 8B FA FF FF               jne 0x140211325
0021189A  48 8D 43 40                     lea rax, [rbx + 0x40]
0021189E  48 3B D0                        cmp rdx, rax
002118A1  0F 85 C7 01 00 00               jne 0x140211a6e
002118A7  FF 42 20                        inc dword ptr [rdx + 0x20]
002118AA  45 84 DB                        test r11b, r11b
002118AD  0F 84 3B 02 00 00               je 0x140211aee
002118B3  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
002118BC  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
002118C3  4D 85 C0                        test r8, r8
002118C6  0F 85 35 01 00 00               jne 0x140211a01
002118CC  FB                              sti
002118CD  45 32 ED                        xor r13b, r13b
002118D0  45 84 C9                        test r9b, r9b
002118D3  0F 85 EA 00 00 00               jne 0x1402119c3
002118D9  48 85 FF                        test rdi, rdi
002118DC  0F 85 1E 02 00 00               jne 0x140211b00
002118E2  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
002118E6  40 B6 01                        mov sil, 1
002118E9  44 0F B6 7D 40                  movzx r15d, byte ptr [rbp + 0x40]
002118EE  E9 D1 FD FF FF                  jmp 0x1402116c4
002118F3  48 8B D7                        mov rdx, rdi
002118F6  48 8B CB                        mov rcx, rbx
002118F9  E8 12 09 05 00                  call 0x140262210
002118FE  E9 11 FE FF FF                  jmp 0x140211714
00211903  48 8B 09                        mov rcx, qword ptr [rcx]
00211906  49 FF C1                        inc r9
00211909  49 83 F9 06                     cmp r9, 6
0021190D  0F 86 E0 F9 FF FF               jbe 0x1402112f3
00211913  45 0F 20 C4                     mov r12, cr8
00211917  4C 89 65 A8                     mov qword ptr [rbp - 0x58], r12
0021191B  B8 02 00 00 00                  mov eax, 2
00211920  44 0F 22 C0                     mov cr8, rax
00211924  44 39 35 F5 53 DB 00            cmp dword ptr [rip + 0xdb53f5], r14d
0021192B  0F 85 2C 01 00 00               jne 0x140211a5d
00211931  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0021193A  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00211941  4D 85 C0                        test r8, r8
00211944  0F 85 66 01 00 00               jne 0x140211ab0
0021194A  FB                              sti
0021194B  48 8B 03                        mov rax, qword ptr [rbx]
0021194E  41 B1 01                        mov r9b, 1
00211951  4C 8B 55 58                     mov r10, qword ptr [rbp + 0x58]
00211955  45 32 DB                        xor r11b, r11b
00211958  44 88 4D 40                     mov byte ptr [rbp + 0x40], r9b
0021195C  44 88 5D A0                     mov byte ptr [rbp - 0x60], r11b
00211960  41 84 C1                        test r9b, al
00211963  0F 85 E1 00 00 00               jne 0x140211a4a
00211969  4D 8D 82 B8 06 00 00            lea r8, [r10 + 0x6b8]
00211970  49 8B D6                        mov rdx, r14
00211973  49 8B 08                        mov rcx, qword ptr [r8]
00211976  49 3B C8                        cmp rcx, r8
00211979  0F 84 9D F9 FF FF               je 0x14021131c
0021197F  F6 41 25 02                     test byte ptr [rcx + 0x25], 2
00211983  0F 85 6F 01 00 00               jne 0x140211af8
00211989  48 39 59 18                     cmp qword ptr [rcx + 0x18], rbx
0021198D  0F 85 65 01 00 00               jne 0x140211af8
00211993  48 8B D1                        mov rdx, rcx
00211996  E9 81 F9 FF FF                  jmp 0x14021131c
0021199B  41 0F 0D 08                     prefetchw byte ptr [r8]
0021199F  41 8B 00                        mov eax, dword ptr [r8]
002119A2  8B D0                           mov edx, eax
002119A4  0F BA F2 15                     btr edx, 0x15
002119A8  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
002119AD  75 F3                           jne 0x1402119a2
002119AF  0F BA E0 15                     bt eax, 0x15
002119B3  0F 83 8C FE FF FF               jae 0x140211845
002119B9  E8 12 18 05 00                  call 0x1402631d0
002119BE  E9 82 FE FF FF                  jmp 0x140211845
002119C3  44 39 35 56 53 DB 00            cmp dword ptr [rip + 0xdb5356], r14d
002119CA  74 0D                           je 0x1402119d9
002119CC  44 0F 20 C1                     mov rcx, cr8
002119D0  41 0F B6 D4                     movzx edx, r12b
002119D4  E8 BF 3C 2E 00                  call 0x1404f5698
002119D9  41 0F B6 C4                     movzx eax, r12b
002119DD  44 0F 22 C0                     mov cr8, rax
002119E1  32 C0                           xor al, al
002119E3  88 45 40                        mov byte ptr [rbp + 0x40], al
002119E6  E9 EE FE FF FF                  jmp 0x1402118d9
002119EB  48 85 FF                        test rdi, rdi
002119EE  0F 84 89 FE FF FF               je 0x14021187d
002119F4  48 8B D7                        mov rdx, rdi
002119F7  E8 B0 CE 1A 00                  call 0x1403be8ac
002119FC  E9 7C FE FF FF                  jmp 0x14021187d
00211A01  41 0F 0D 08                     prefetchw byte ptr [r8]
00211A05  41 8B 00                        mov eax, dword ptr [r8]
00211A08  8B D0                           mov edx, eax
00211A0A  0F BA F2 15                     btr edx, 0x15
00211A0E  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00211A13  75 F3                           jne 0x140211a08
00211A15  0F BA E0 15                     bt eax, 0x15
00211A19  0F 83 AD FE FF FF               jae 0x1402118cc
00211A1F  E8 AC 17 05 00                  call 0x1402631d0
00211A24  44 0F B6 4D 40                  movzx r9d, byte ptr [rbp + 0x40]
00211A29  E9 9E FE FF FF                  jmp 0x1402118cc
00211A2E  45 85 E4                        test r12d, r12d
00211A31  0F 85 A1 00 00 00               jne 0x140211ad8
00211A37  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
00211A3B  BA 44 66 6C 74                  mov edx, 0x746c6644
00211A40  E8 CB EC FF FF                  call 0x140210710
00211A45  E9 04 FE FF FF                  jmp 0x14021184e
00211A4A  4C 39 53 50                     cmp qword ptr [rbx + 0x50], r10
00211A4E  0F 85 15 FF FF FF               jne 0x140211969
00211A54  48 8D 53 40                     lea rdx, [rbx + 0x40]
00211A58  E9 BF F8 FF FF                  jmp 0x14021131c
00211A5D  0F B6 D0                        movzx edx, al
00211A60  41 0F B6 CC                     movzx ecx, r12b
00211A64  E8 93 3C 2E 00                  call 0x1404f56fc
00211A69  E9 C3 FE FF FF                  jmp 0x140211931
00211A6E  F0 48 83 03 04                  lock add qword ptr [rbx], 4
00211A73  4C 3B E8                        cmp r13, rax
00211A76  74 04                           je 0x140211a7c
00211A78  49 89 5D 18                     mov qword ptr [r13 + 0x18], rbx
00211A7C  49 8D 82 B8 06 00 00            lea rax, [r10 + 0x6b8]
00211A83  4D 89 55 10                     mov qword ptr [r13 + 0x10], r10
00211A87  41 C7 45 20 01 00 00 00         mov dword ptr [r13 + 0x20], 1
00211A8F  48 8B 08                        mov rcx, qword ptr [rax]
00211A92  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00211A96  0F 85 FB FA FF FF               jne 0x140211597
00211A9C  49 89 4D 00                     mov qword ptr [r13], rcx
00211AA0  49 89 45 08                     mov qword ptr [r13 + 8], rax
00211AA4  4C 89 69 08                     mov qword ptr [rcx + 8], r13
00211AA8  4C 89 28                        mov qword ptr [rax], r13
00211AAB  E9 FA FD FF FF                  jmp 0x1402118aa
00211AB0  41 0F 0D 08                     prefetchw byte ptr [r8]
00211AB4  41 8B 00                        mov eax, dword ptr [r8]
00211AB7  8B D0                           mov edx, eax
00211AB9  0F BA F2 15                     btr edx, 0x15
00211ABD  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00211AC2  75 F3                           jne 0x140211ab7
00211AC4  0F BA E0 15                     bt eax, 0x15
00211AC8  0F 83 7C FE FF FF               jae 0x14021194a
00211ACE  E8 FD 16 05 00                  call 0x1402631d0
00211AD3  E9 72 FE FF FF                  jmp 0x14021194a
00211AD8  48 85 FF                        test rdi, rdi
00211ADB  0F 84 56 FF FF FF               je 0x140211a37
00211AE1  48 8B D7                        mov rdx, rdi
00211AE4  E8 C3 CD 1A 00                  call 0x1403be8ac
00211AE9  E9 49 FF FF FF                  jmp 0x140211a37
00211AEE  44 0F B6 6D A0                  movzx r13d, byte ptr [rbp - 0x60]
00211AF3  E9 D8 FD FF FF                  jmp 0x1402118d0
00211AF8  48 8B 09                        mov rcx, qword ptr [rcx]
00211AFB  E9 76 FE FF FF                  jmp 0x140211976
00211B00  48 8B D7                        mov rdx, rdi
00211B03  48 8B CB                        mov rcx, rbx
00211B06  E8 05 07 05 00                  call 0x140262210
00211B0B  49 8B FE                        mov rdi, r14
00211B0E  E9 CF FD FF FF                  jmp 0x1402118e2
00211B13  48 81 C1 C8 06 00 00            add rcx, 0x6c8
00211B1A  E8 11 69 FF FF                  call 0x140208430
00211B1F  4C 8B 45 58                     mov r8, qword ptr [rbp + 0x58]
00211B23  49 8D 80 D0 06 00 00            lea rax, [r8 + 0x6d0]
00211B2A  48 8B 10                        mov rdx, qword ptr [rax]
00211B2D  48 39 42 08                     cmp qword ptr [rdx + 8], rax
00211B31  0F 85 60 FA FF FF               jne 0x140211597
00211B37  49 89 55 00                     mov qword ptr [r13], rdx
00211B3B  49 8D 88 C8 06 00 00            lea rcx, [r8 + 0x6c8]
00211B42  49 89 45 08                     mov qword ptr [r13 + 8], rax
00211B46  4C 89 6A 08                     mov qword ptr [rdx + 8], r13
00211B4A  4C 89 28                        mov qword ptr [rax], r13
00211B4D  E8 1E 4B FF FF                  call 0x140206670
00211B52  E9 D0 FC FF FF                  jmp 0x140211827
00211B57  4C 8D B2 C8 06 00 00            lea r14, [rdx + 0x6c8]
00211B5E  49 8B CE                        mov rcx, r14
00211B61  E8 CA 68 FF FF                  call 0x140208430
00211B66  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00211B6A  48 05 D0 06 00 00               add rax, 0x6d0
00211B70  48 8B 08                        mov rcx, qword ptr [rax]
00211B73  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00211B77  0F 85 1A FA FF FF               jne 0x140211597
00211B7D  49 89 4D 00                     mov qword ptr [r13], rcx
00211B81  49 89 45 08                     mov qword ptr [r13 + 8], rax
00211B85  4C 89 69 08                     mov qword ptr [rcx + 8], r13
00211B89  49 8B CE                        mov rcx, r14
00211B8C  4C 89 28                        mov qword ptr [rax], r13
00211B8F  E8 DC 4A FF FF                  call 0x140206670
00211B94  E9 B2 FA FF FF                  jmp 0x14021164b
00211B99  45 33 C0                        xor r8d, r8d
00211B9C  48 8B D7                        mov rdx, rdi
00211B9F  48 8B CB                        mov rcx, rbx
00211BA2  E8 89 E6 FF FF                  call 0x140210230
00211BA7  E9 10 FB FF FF                  jmp 0x1402116bc
00211BAC  48 8B D7                        mov rdx, rdi
00211BAF  E8 F8 CC 1A 00                  call 0x1403be8ac
00211BB4  E9 65 FB FF FF                  jmp 0x14021171e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpAcquireFastResourceSharedSlow(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
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
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int8 v_stack_m98;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (128);
    result = 0;
    v_stack_m78 = 0;
    v_r12 = 0;
    v_stack_m40 = 0;
    v_rsi = 0;
    v_stack_m90 = 0;
    result = (unsigned int)(((unsigned int)(a5)) & (16));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (8));
    a4 = 0;
    v_stack_m94 = (unsigned int)(result);
    v_stack_p8 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m70 = v_xmm1;
    v_stack_m60 = v_xmm1;
    v_stack_m50 = v_xmm1;
    v_r14 = 0;
    v_stack_m98 = 1;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(a1)))) != 0) goto loc_002115BD;
loc_002112E3:
loc_002112F3:
    if ((*(unsigned __int64 *)(a4 + 1720)) == (a4 + 1720)) goto loc_0021130F;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a4 + 1720) + 37)) & (2)) != 0) goto loc_00211903;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 1720) + 24)) != a1) goto loc_00211903;
loc_0021130F:
    a4 = 0;
loc_00211312:
    if ((*(unsigned __int64 *)(a4 + 1720)) == 1) goto loc_00211913;
loc_0021131C:
    if (*(unsigned __int64 *)(a4 + 1720) != 0) goto loc_00211890;
loc_00211325:
    if ((unsigned int)(v_r15) == 0) goto loc_00211854;
    if (1 == 0) goto loc_00211377;
    if ((*(unsigned int *)(v_rip + 14375385)) != 0) goto loc_002115D0;
loc_0021134D:
    v_stack_m90 = (unsigned __int8)(v_cr8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00211606;
loc_0021136E:
    v_stack_p8 = 1;
    v_stack_m98 = 0;
loc_00211377:
    v_stack_m88 = 0;
    v_stack_m80 = a1 + 48;
    if (((*(unsigned __int8 *)(v_rip + 14374779)) & (33)) != 0) goto loc_0021159E;
loc_00211391:
    if (v_stack_m88 != 0) goto loc_0021162E;
loc_002113A1:
loc_002113AB:
    a3 = 0;
    if ((*(unsigned __int64 *)(a1 + 16)) == 0) goto loc_002114EB;
loc_002113B8:
    a1 = (*(unsigned __int64 *)(a1)) | (2);
loc_002113BF:
    if ((((unsigned __int8)(a1)) & (2)) == 0) goto loc_002114C2;
loc_002113CB:
    if ((((unsigned __int8)((unsigned int)(a5))) & (4)) != 0) goto loc_002114CC;
loc_002113D5:
    a1 = (a1) | (2);
loc_002113D9:
    if (a1 == (*(unsigned __int64 *)(a1))) goto loc_002113E5;
    if (a1 != (*(unsigned __int64 *)(a1))) goto loc_002113AB;
loc_002113E5:
    if (0 != 0) goto loc_0021178A;
    if (0 == 0) goto loc_00211419;
    result = (unsigned __int8)((*(unsigned __int8 *)(a3)) | (2));
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
    result = (*(unsigned __int64 *)(a3)) >> (63);
    if ((unsigned __int8)(result) != 0) goto loc_00211867;
loc_0021140D:
    *(unsigned __int8 *)(a3 + 9) = 1;
    result = (unsigned __int8)((*(unsigned __int8 *)(a3)) & (253));
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
loc_00211419:
    v_stack_m48 = v_stack_m50;
    v_stack_m50 = v_stack_m50;
    v_stack_m68 = 0;
    v_stack_m58 = 0x60001ULL;
    v_stack_m60 = v_stack_p20;
    v_stack_m40 = 0;
    if (*(unsigned __int64 *)(a1 + 8) != 0) goto loc_002115E1;
    v_stack_m68 = v_stack_m70;
    v_stack_m70 = v_stack_m70;
loc_0021145E:
    *(unsigned __int64 *)(a1 + 8) = v_stack_m70;
    if (((*(unsigned __int8 *)(v_rip + 14374553)) & (1)) != 0) goto loc_00211501;
loc_00211473:
    if (v_stack_m88 != 0) goto loc_002114A3;
    if (v_stack_m88 == v_stack_m88) goto loc_00211520;
    result = KxWaitForLockChainValid(v_stack_m88, v_stack_p20, a3, (unsigned int)(a5));
loc_002114A3:
    v_stack_m88 = 0;
    result = (unsigned __int8)((v_stack_m80) ^ ((unsigned __int8)(v_stack_m80)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0021151C;
    result = KeWakeAddressAll(result + 8, v_stack_m80, a3, (unsigned int)(a5));
    goto loc_0021151C;
loc_002114C2:
    if ((((unsigned __int8)((unsigned int)(a5))) & (2)) == 0) goto loc_002113CB;
loc_002114CC:
    if ((((unsigned __int8)(result + 8)) & (1)) != 0) goto loc_002113D5;
    a1 = (result + 8) + (4);
    a1 = (a1) ^ (v_stack_m80);
    a1 = (a1) & (-4);
    a1 = (a1) ^ (v_stack_m80);
    goto loc_002113D9;
loc_002114EB:
    if ((*(unsigned int *)(a1 + 56)) > 0) goto loc_002113B8;
    a1 = (result) & (-3);
    goto loc_002113BF;
loc_00211501:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13617489))) != 0) goto loc_00211473;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m88, v_stack_p0, 1, (unsigned int)(a5));
loc_0021151C:
loc_00211520:
    v_r12 = 0;
    if (v_stack_m94 != 0) { v_r12 = 4; }
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (4));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (2));
    v_r12 = (unsigned int)((v_r12) & (8));
    if (a2 != (a1 + 64)) {
        *(unsigned __int64 *)(a2 + 24) = a1;
    }
    *(unsigned int *)(a2 + 32) = 1;
    v_r14 = ((unsigned int)(v_rsi) != 0) ? 1 : 0;
    v_r14 = (v_r14) | (v_stack_p20);
    *(unsigned __int64 *)(a2 + 16) = v_r14;
    result = a1 + 64;
    if (0 != 0) {
        result = *(unsigned __int8 *)(a3 + 8);
        result = (unsigned __int8)((result) & (63));
        result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
        result = (unsigned __int8)((result) | (1));
        *(unsigned __int8 *)(a2 + 36) = (unsigned __int8)(result);
    }
    if ((unsigned int)(v_r15) != 0) {
    }
    if ((unsigned int)(v_rsi) != 0) goto loc_00211B57;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 1720) + 8)) == (v_stack_p20 + 1720)) goto loc_0021163C;
loc_00211597:
loc_0021159E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13617332))) != 0) goto loc_00211391;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m88, 3, 1, (unsigned int)(a5));
    goto loc_002113A1;
loc_002115BD:
    if ((*(unsigned __int64 *)(v_stack_m88 + 80)) != 0) goto loc_002112E3;
    goto loc_00211312;
loc_002115D0:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_rsi), (unsigned __int8)(result), 1, (unsigned int)(a5));
    goto loc_0021134D;
loc_002115E1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_00211597;
    v_stack_m68 = *(unsigned __int64 *)(result + 8);
    v_stack_m70 = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = v_stack_m70;
    *(unsigned __int64 *)(result + 8) = v_stack_m70;
    goto loc_0021145E;
loc_00211606:
loc_0021160D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_0021160D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) >= result) goto loc_0021136E;
    result = KiRemoveSystemWorkPriorityKick(v_stack_m70, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m70)))), v_stack_m70, (unsigned int)(a5));
    goto loc_0021136E;
loc_0021162E:
    result = KxWaitForLockOwnerShip(v_stack_m88, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m70)))), v_stack_m70, (unsigned int)(a5));
    goto loc_002113A1;
loc_0021163C:
    *(unsigned __int64 *)(a2) = v_stack_m88;
    *(unsigned __int64 *)(a2 + 8) = result;
    *(unsigned __int64 *)(v_stack_m88 + 8) = a2;
    *(unsigned __int64 *)(result) = a2;
loc_0021164B:
    if ((unsigned int)(v_r15) == 0) goto loc_0021166A;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00211762;
loc_00211669:
loc_0021166A:
    if ((unsigned int)(v_rsi) != 0) goto loc_00211874;
loc_00211672:
    if ((*(unsigned int *)(v_rip + 14374562)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_m90);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(a5));
    }
    v_r15 = 0;
    result = ExpWaitForFastResource(a1, v_stack_m70, (unsigned int)(0x10244ULL), (unsigned int)(a5));
    if (0 != 0) goto loc_00211B99;
loc_002116BC:
loc_002116C4:
    if ((unsigned __int8)(v_stack_m98) == 0) goto loc_002116DF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0021173E;
loc_002116DE:
loc_002116DF:
    if (0 == 0) goto loc_00211702;
    if ((*(unsigned int *)(v_rip + 14374453)) != 0) {
        a1 = (unsigned __int8)(v_stack_m90);
        a2 = (unsigned __int8)(v_stack_m90);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(a5));
    }
loc_00211702:
    if (0 == 0) goto loc_0021171E;
    if (1 == 0) goto loc_002118F3;
    *(unsigned __int8 *)(a3 + 10) = 1;
loc_00211714:
    if (v_stack_m94 != 0) goto loc_00211BAC;
loc_0021171E:
    v_rsp = (v_rsp) + (128);
    return 1;
loc_0021173E:
loc_00211745:
    if (condition_is_not_equal) goto loc_00211745;
    if (condition_is_above_or_equal) goto loc_002116DE;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(a5));
    goto loc_002116DE;
loc_00211762:
loc_00211769:
    if (condition_is_not_equal) goto loc_00211769;
    if (condition_is_above_or_equal) goto loc_00211669;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(a5));
    goto loc_00211669;
loc_0021178A:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m88, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(a5));
    v_r12 = 1;
    if (v_stack_m94 != ((unsigned int)(v_stack_m90))) { v_r12 = 13; }
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (2));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (4));
    v_r12 = (unsigned int)((v_r12) & (8));
    if (v_stack_m98 != (v_stack_p10 + 64)) {
        *(unsigned __int64 *)(v_stack_m98 + 24) = v_stack_p10;
    }
    *(unsigned int *)(v_stack_m98 + 32) = 1;
    result = ((unsigned int)(v_rsi) != 0) ? 1 : 0;
    result = (result) | (v_stack_p20);
    *(unsigned __int64 *)(v_stack_m98 + 16) = result;
    if (0 != 0) {
        result = *(unsigned __int8 *)(a3 + 8);
        result = (unsigned __int8)((result) & (63));
        *(unsigned __int8 *)(a3 + 10) = 1;
        result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
        result = (unsigned __int8)((result) | (1));
        *(unsigned __int8 *)(v_stack_m98 + 36) = (unsigned __int8)(result);
    }
    if ((unsigned int)(v_r15) != 0) {
    }
    if ((unsigned int)(v_rsi) != 0) goto loc_00211B13;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 1720) + 8)) != (v_stack_p20 + 1720)) goto loc_00211597;
    *(unsigned __int64 *)(v_stack_m98) = *(unsigned __int64 *)(v_stack_p20 + 1720);
    *(unsigned __int64 *)(v_stack_m98 + 8) = v_stack_p20 + 1720;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 1720) + 8) = v_stack_m98;
    *(unsigned __int64 *)(v_stack_p20 + 1720) = v_stack_m98;
loc_00211827:
    if ((unsigned int)(v_r15) == 0) goto loc_00211846;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0021199B;
loc_00211845:
loc_00211846:
    if ((unsigned int)(v_rsi) != 0) goto loc_00211A2E;
loc_0021184E:
loc_00211854:
    goto loc_002116C4;
loc_00211867:
    result = KiAbEntryRemoveFromTree(v_stack_m90, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(a5));
    goto loc_0021140D;
loc_00211874:
    if ((unsigned int)(v_r12) != 0) goto loc_002119EB;
loc_0021187D:
    result = ObfReferenceObjectWithTag(v_stack_p20, (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(a5));
    goto loc_00211672;
loc_00211890:
    if (((*(unsigned __int8 *)((unsigned int)(0x746C6644ULL) + 37)) & (4)) != 0) goto loc_00211325;
    if (((unsigned int)(0x746C6644ULL)) != (v_stack_p10 + 64)) goto loc_00211A6E;
loc_002118AA:
    if (1 == 0) goto loc_00211AEE;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00211A01;
loc_002118CC:
    v_r13 = 0;
loc_002118D0:
    if ((unsigned __int8)((unsigned int)(a5)) != 0) goto loc_002119C3;
loc_002118D9:
    if (v_stack_m90 != 0) goto loc_00211B00;
loc_002118E2:
    goto loc_002116C4;
loc_002118F3:
    result = KeAbPostReleaseEx(v_stack_p10, v_stack_m90, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(a5));
    goto loc_00211714;
loc_00211903:
    a4 = ((unsigned int)(a5)) + 1;
    if (a4 <= 6) goto loc_002112F3;
loc_00211913:
    v_stack_m90 = (unsigned __int8)(v_stack_m90);
    if ((*(unsigned int *)(v_rip + 14373877)) != ((unsigned int)(v_stack_m90))) goto loc_00211A5D;
loc_00211931:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00211AB0;
loc_0021194A:
    v_r11 = 0;
    v_stack_p8 = 1;
    v_stack_m98 = 0;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10)))) != 0) goto loc_00211A4A;
loc_00211969:
loc_00211976:
    if ((*(unsigned __int64 *)(v_stack_p20 + 1720)) == (v_stack_p20 + 1720)) goto loc_0021131C;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p20 + 1720) + 37)) & (2)) != 0) goto loc_00211AF8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 1720) + 24)) != v_stack_p10) goto loc_00211AF8;
    goto loc_0021131C;
loc_0021199B:
loc_002119A2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 1720) + 24)) != v_stack_p10) goto loc_002119A2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 1720) + 24)) >= v_stack_p10) goto loc_00211845;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(v_stack_p20 + 1720), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 1720)))), v_stack_p20 + 1720, 1);
    goto loc_00211845;
loc_002119C3:
    if ((*(unsigned int *)(v_rip + 14373718)) != ((unsigned int)(v_stack_m90))) {
        a1 = 2;
        a2 = (unsigned __int8)((unsigned __int8)(v_stack_m90));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_p20 + 1720, 1);
    }
    result = 0;
    v_stack_p8 = 0;
    goto loc_002118D9;
loc_002119EB:
    if (v_stack_m90 == 0) goto loc_0021187D;
    result = KeAbMarkCrossThreadReleasable(a1, v_stack_m90, v_stack_p20 + 1720, 1);
    goto loc_0021187D;
loc_00211A01:
loc_00211A08:
    if (v_stack_m90 != 0) goto loc_00211A08;
    if (condition_is_above_or_equal) goto loc_002118CC;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 1720)))), v_stack_p20 + 1720, 1);
    goto loc_002118CC;
loc_00211A2E:
    if ((unsigned int)((unsigned __int8)(v_stack_m90)) != 0) goto loc_00211AD8;
loc_00211A37:
    result = ObfReferenceObjectWithTag(v_stack_p20, (unsigned int)(0x746C6644ULL), v_stack_p20 + 1720, v_stack_p8);
    goto loc_0021184E;
loc_00211A4A:
    if ((*(unsigned __int64 *)(v_stack_p10 + 80)) != v_stack_p20) goto loc_00211969;
    goto loc_0021131C;
loc_00211A5D:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)(v_stack_m90)), (unsigned __int8)(result), v_stack_p20 + 1720, v_stack_p8);
    goto loc_00211931;
loc_00211A6E:
    if (0 != result) {
        *(unsigned __int64 *)(v_r13 + 24) = v_stack_p10;
    }
    *(unsigned __int64 *)(v_r13 + 16) = v_stack_p20;
    *(unsigned int *)(v_r13 + 32) = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 1720) + 8)) != (v_stack_p20 + 1720)) goto loc_00211597;
    *(unsigned __int64 *)(v_r13) = *(unsigned __int64 *)(v_stack_p20 + 1720);
    *(unsigned __int64 *)(v_r13 + 8) = v_stack_p20 + 1720;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 1720) + 8) = 0;
    *(unsigned __int64 *)(v_stack_p20 + 1720) = 0;
    goto loc_002118AA;
loc_00211AB0:
loc_00211AB7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 1720) + 8)) != (v_stack_p20 + 1720)) goto loc_00211AB7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 1720) + 8)) >= (v_stack_p20 + 1720)) goto loc_0021194A;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(v_stack_p20 + 1720), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 1720)))), v_stack_p20 + 1720, v_stack_p8);
    goto loc_0021194A;
loc_00211AD8:
    if (v_stack_m90 == 0) goto loc_00211A37;
    result = KeAbMarkCrossThreadReleasable(*(unsigned __int64 *)(v_stack_p20 + 1720), v_stack_m90, v_stack_p20 + 1720, v_stack_p8);
    goto loc_00211A37;
loc_00211AEE:
    goto loc_002118D0;
loc_00211AF8:
    goto loc_00211976;
loc_00211B00:
    result = KeAbPostReleaseEx(v_stack_p10, v_stack_m90, v_stack_p20 + 1720, v_stack_p8);
    goto loc_002118E2;
loc_00211B13:
    a1 = (v_stack_p10) + (0x6C8ULL);
    result = KeAcquireSpinLockAtDpcLevel(a1, v_stack_m90, v_stack_p20 + 1720, v_stack_p8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 1744) + 8)) != (v_stack_p20 + 1744)) goto loc_00211597;
    *(unsigned __int64 *)(v_stack_m98) = *(unsigned __int64 *)(v_stack_p20 + 1744);
    *(unsigned __int64 *)(v_stack_m98 + 8) = v_stack_p20 + 1744;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p20 + 1744) + 8) = v_stack_m98;
    *(unsigned __int64 *)(v_stack_p20 + 1744) = v_stack_m98;
    result = KxReleaseSpinLock(v_stack_p20 + 1736, *(unsigned __int64 *)(v_stack_p20 + 1744), v_stack_p20, v_stack_p8);
    goto loc_00211827;
loc_00211B57:
    result = KeAcquireSpinLockAtDpcLevel(*(unsigned __int64 *)(v_stack_p20 + 1744) + 1736, *(unsigned __int64 *)(v_stack_p20 + 1744), v_stack_p20, v_stack_p8);
    result = (v_stack_p20) + (0x6D0ULL);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) != result) goto loc_00211597;
    *(unsigned __int64 *)(v_stack_m98) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(v_stack_m98 + 8) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = v_stack_m98;
    *(unsigned __int64 *)(result) = v_stack_m98;
    result = KxReleaseSpinLock(*(unsigned __int64 *)(v_stack_p20 + 1744) + 1736, *(unsigned __int64 *)(v_stack_p20 + 1744), v_stack_p20, v_stack_p8);
    goto loc_0021164B;
loc_00211B99:
    a3 = 0;
    result = KeAbPreAcquire(v_stack_p10, v_stack_m90, a3, v_stack_p8);
    goto loc_002116BC;
loc_00211BAC:
    result = KeAbMarkCrossThreadReleasable(v_stack_p10, v_stack_m90, a3, v_stack_p8);
    goto loc_0021171E;
}
```

## 5. (Beta) C Style

```c
int64_t ExpAcquireFastResourceSharedSlow(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
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
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint8_t v_stack_m98;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (128);
    result = 0;
    v_stack_m78 = 0;
    local_r12 = 0;
    v_stack_m40 = 0;
    local_rsi = 0;
    v_stack_m90 = 0;
    result = (uint32_t)(((uint32_t)(Arg5)) & (16));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (8));
    Arg4 = 0;
    v_stack_m94 = (uint32_t)(result);
    v_stack_p8 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m70 = v_xmm1;
    v_stack_m60 = v_xmm1;
    v_stack_m50 = v_xmm1;
    local_r14 = 0;
    v_stack_m98 = 1;
    if (((1) & ((uint8_t)(*(uint64_t *)(arg1)))) != 0) goto loc_002115BD;
loc_002112E3:
loc_002112F3:
    if ((*(uint64_t *)(arg4 + 0x6B8)) == (Arg4 + 1720)) goto loc_0021130F;
    if (((*(uint8_t *)(*(uint64_t *)(arg4 + 0x6B8) + 0x25)) & (2)) != 0) goto loc_00211903;
    if ((*(uint64_t *)(*(uint64_t *)(arg4 + 0x6B8) + 0x18)) != Arg1) goto loc_00211903;
loc_0021130F:
    Arg4 = 0;
loc_00211312:
    if ((*(uint64_t *)(arg4 + 0x6B8)) == 1) goto loc_00211913;
loc_0021131C:
    if (*(uint64_t *)(arg4 + 0x6B8) != 0) goto loc_00211890;
loc_00211325:
    if ((uint32_t)(local_r15) == 0) goto loc_00211854;
    if (1 == 0) goto loc_00211377;
    if ((*(uint32_t *)(v_rip + 0xDB59D9)) != 0) goto loc_002115D0;
loc_0021134D:
    v_stack_m90 = (uint8_t)(v_cr8);
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00211606;
loc_0021136E:
    v_stack_p8 = 1;
    v_stack_m98 = 0;
loc_00211377:
    v_stack_m88 = 0;
    v_stack_m80 = Arg1 + 48;
    if (((*(uint8_t *)(v_rip + 0xDB577B)) & (33)) != 0) goto loc_0021159E;
loc_00211391:
    if (v_stack_m88 != 0) goto loc_0021162E;
loc_002113A1:
loc_002113AB:
    Arg3 = 0;
    if ((*(uint64_t *)(arg1 + 0x10)) == 0) goto loc_002114EB;
loc_002113B8:
    Arg1 = (*(uint64_t *)(arg1)) | (2);
loc_002113BF:
    if ((((uint8_t)(Arg1)) & (2)) == 0) goto loc_002114C2;
loc_002113CB:
    if ((((uint8_t)((uint32_t)(Arg5))) & (4)) != 0) goto loc_002114CC;
loc_002113D5:
    Arg1 = (Arg1) | (2);
loc_002113D9:
    if (Arg1 == (*(uint64_t *)(arg1))) goto loc_002113E5;
    if (Arg1 != (*(uint64_t *)(arg1))) goto loc_002113AB;
loc_002113E5:
    if (0 != 0) goto loc_0021178A;
    if (0 == 0) goto loc_00211419;
    result = (uint8_t)((*(uint8_t *)(Arg3)) | (2));
    *(uint8_t *)(Arg3) = (uint8_t)(result);
    result = (*(uint64_t *)(Arg3)) >> (63);
    if ((uint8_t)(result) != 0) goto loc_00211867;
loc_0021140D:
    *(uint8_t *)(Arg3 + 0x9) = 1;
    result = (uint8_t)((*(uint8_t *)(Arg3)) & (253));
    *(uint8_t *)(Arg3) = (uint8_t)(result);
loc_00211419:
    v_stack_m48 = v_stack_m50;
    v_stack_m50 = v_stack_m50;
    v_stack_m68 = 0;
    v_stack_m58 = 0x60001ULL;
    v_stack_m60 = v_stack_p20;
    v_stack_m40 = 0;
    if (*(uint64_t *)(arg1 + 0x8) != 0) goto loc_002115E1;
    v_stack_m68 = v_stack_m70;
    v_stack_m70 = v_stack_m70;
loc_0021145E:
    *(uint64_t *)(arg1 + 0x8) = v_stack_m70;
    if (((*(uint8_t *)(v_rip + 0xDB5699)) & (1)) != 0) goto loc_00211501;
loc_00211473:
    if (v_stack_m88 != 0) goto loc_002114A3;
    if (v_stack_m88 == v_stack_m88) goto loc_00211520;
    result = KxWaitForLockChainValid(v_stack_m88, v_stack_p20, Arg3, (uint32_t)(Arg5));
loc_002114A3:
    v_stack_m88 = 0;
    result = (uint8_t)((v_stack_m80) ^ ((uint8_t)(v_stack_m80)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0021151C;
    result = KeWakeAddressAll(result + 8, v_stack_m80, Arg3, (uint32_t)(Arg5));
    goto loc_0021151C;
loc_002114C2:
    if ((((uint8_t)((uint32_t)(Arg5))) & (2)) == 0) goto loc_002113CB;
loc_002114CC:
    if ((((uint8_t)(result + 8)) & (1)) != 0) goto loc_002113D5;
    Arg1 = (result + 8) + (4);
    Arg1 = (Arg1) ^ (v_stack_m80);
    Arg1 = (Arg1) & (-4);
    Arg1 = (Arg1) ^ (v_stack_m80);
    goto loc_002113D9;
loc_002114EB:
    if ((*(uint32_t *)(arg1 + 0x38)) > 0) goto loc_002113B8;
    Arg1 = (result) & (-3);
    goto loc_002113BF;
loc_00211501:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCFC951))) != 0) goto loc_00211473;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m88, v_stack_p0, 1, (uint32_t)(Arg5));
loc_0021151C:
loc_00211520:
    local_r12 = 0;
    if (v_stack_m94 != 0) { local_r12 = 4; }
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (4));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (2));
    local_r12 = (uint32_t)((local_r12) & (8));
    if (Arg2 != (Arg1 + 64)) {
        *(void **)(Arg2 + 0x18) = Arg1;
    }
    *(uint32_t *)(Arg2 + 0x20) = 1;
    local_r14 = ((uint32_t)(local_rsi) != 0) ? 1 : 0;
    local_r14 = (local_r14) | (v_stack_p20);
    *(uint64_t *)(Arg2 + 0x10) = local_r14;
    result = Arg1 + 64;
    if (0 != 0) {
        result = *(uint8_t *)(Arg3 + 0x8);
        result = (uint8_t)((result) & (63));
        result = (uint8_t)((result) + ((uint8_t)(result)));
        result = (uint8_t)((result) | (1));
        *(uint8_t *)(Arg2 + 0x24) = (uint8_t)(result);
    }
    if ((uint32_t)(local_r15) != 0) {
    }
    if ((uint32_t)(local_rsi) != 0) goto loc_00211B57;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x6B8) + 0x8)) == (v_stack_p20 + 1720)) goto loc_0021163C;
loc_00211597:
loc_0021159E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCFC8B4))) != 0) goto loc_00211391;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m88, 3, 1, (uint32_t)(Arg5));
    goto loc_002113A1;
loc_002115BD:
    if ((*(uint64_t *)(v_stack_m88 + 0x50)) != 0) goto loc_002112E3;
    goto loc_00211312;
loc_002115D0:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_rsi), (uint8_t)(result), 1, (uint32_t)(Arg5));
    goto loc_0021134D;
loc_002115E1:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_00211597;
    v_stack_m68 = *(uint64_t *)(result + 0x8);
    v_stack_m70 = result;
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = v_stack_m70;
    *(uint64_t *)(result + 0x8) = v_stack_m70;
    goto loc_0021145E;
loc_00211606:
loc_0021160D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_0021160D;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) >= result) goto loc_0021136E;
    result = KiRemoveSystemWorkPriorityKick(v_stack_m70, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m70)))), v_stack_m70, (uint32_t)(Arg5));
    goto loc_0021136E;
loc_0021162E:
    result = KxWaitForLockOwnerShip(v_stack_m88, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m70)))), v_stack_m70, (uint32_t)(Arg5));
    goto loc_002113A1;
loc_0021163C:
    *(uint64_t *)(Arg2) = v_stack_m88;
    *(uint64_t *)(Arg2 + 0x8) = result;
    *(uint64_t *)(v_stack_m88 + 0x8) = Arg2;
    *(uint64_t *)(result) = Arg2;
loc_0021164B:
    if ((uint32_t)(local_r15) == 0) goto loc_0021166A;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00211762;
loc_00211669:
loc_0021166A:
    if ((uint32_t)(local_rsi) != 0) goto loc_00211874;
loc_00211672:
    if ((*(uint32_t *)(v_rip + 0xDB56A2)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_m90);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(Arg5));
    }
    local_r15 = 0;
    result = ExpWaitForFastResource(Arg1, v_stack_m70, (uint32_t)(0x10244ULL), (uint32_t)(Arg5));
    if (0 != 0) goto loc_00211B99;
loc_002116BC:
loc_002116C4:
    if ((uint8_t)(v_stack_m98) == 0) goto loc_002116DF;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0021173E;
loc_002116DE:
loc_002116DF:
    if (0 == 0) goto loc_00211702;
    if ((*(uint32_t *)(v_rip + 0xDB5635)) != 0) {
        Arg1 = (uint8_t)(v_stack_m90);
        Arg2 = (uint8_t)(v_stack_m90);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(Arg5));
    }
loc_00211702:
    if (0 == 0) goto loc_0021171E;
    if (1 == 0) goto loc_002118F3;
    *(uint8_t *)(Arg3 + 0xA) = 1;
loc_00211714:
    if (v_stack_m94 != 0) goto loc_00211BAC;
loc_0021171E:
    local_rsp = (local_rsp) + (128);
    return 1;
loc_0021173E:
loc_00211745:
    if (condition_is_not_equal) goto loc_00211745;
    if (condition_is_above_or_equal) goto loc_002116DE;
    result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(Arg5));
    goto loc_002116DE;
loc_00211762:
loc_00211769:
    if (condition_is_not_equal) goto loc_00211769;
    if (condition_is_above_or_equal) goto loc_00211669;
    result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(Arg5));
    goto loc_00211669;
loc_0021178A:
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m88, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(Arg5));
    local_r12 = 1;
    if (v_stack_m94 != ((uint32_t)(v_stack_m90))) { local_r12 = 13; }
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (2));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (4));
    local_r12 = (uint32_t)((local_r12) & (8));
    if (v_stack_m98 != (v_stack_p10 + 64)) {
        *(uint64_t *)(v_stack_m98 + 0x18) = v_stack_p10;
    }
    *(uint32_t *)(v_stack_m98 + 0x20) = 1;
    result = ((uint32_t)(local_rsi) != 0) ? 1 : 0;
    result = (result) | (v_stack_p20);
    *(uint64_t *)(v_stack_m98 + 0x10) = result;
    if (0 != 0) {
        result = *(uint8_t *)(Arg3 + 0x8);
        result = (uint8_t)((result) & (63));
        *(uint8_t *)(Arg3 + 0xA) = 1;
        result = (uint8_t)((result) + ((uint8_t)(result)));
        result = (uint8_t)((result) | (1));
        *(uint8_t *)(v_stack_m98 + 0x24) = (uint8_t)(result);
    }
    if ((uint32_t)(local_r15) != 0) {
    }
    if ((uint32_t)(local_rsi) != 0) goto loc_00211B13;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x6B8) + 0x8)) != (v_stack_p20 + 1720)) goto loc_00211597;
    *(uint64_t *)(v_stack_m98) = *(uint64_t *)(v_stack_p20 + 0x6B8);
    *(uint64_t *)(v_stack_m98 + 0x8) = v_stack_p20 + 1720;
    *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x6B8) + 0x8) = v_stack_m98;
    *(uint64_t *)(v_stack_p20 + 0x6B8) = v_stack_m98;
loc_00211827:
    if ((uint32_t)(local_r15) == 0) goto loc_00211846;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0021199B;
loc_00211845:
loc_00211846:
    if ((uint32_t)(local_rsi) != 0) goto loc_00211A2E;
loc_0021184E:
loc_00211854:
    goto loc_002116C4;
loc_00211867:
    result = KiAbEntryRemoveFromTree(v_stack_m90, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(Arg5));
    goto loc_0021140D;
loc_00211874:
    if ((uint32_t)(local_r12) != 0) goto loc_002119EB;
loc_0021187D:
    result = ObfReferenceObjectWithTag(v_stack_p20, (uint32_t)(0x746C6644ULL), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(Arg5));
    goto loc_00211672;
loc_00211890:
    if (((*(uint8_t *)((uint32_t)(0x746C6644ULL) + 0x25)) & (4)) != 0) goto loc_00211325;
    if (((uint32_t)(0x746C6644ULL)) != (v_stack_p10 + 64)) goto loc_00211A6E;
loc_002118AA:
    if (1 == 0) goto loc_00211AEE;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00211A01;
loc_002118CC:
    local_r13 = 0;
loc_002118D0:
    if ((uint8_t)((uint32_t)(Arg5)) != 0) goto loc_002119C3;
loc_002118D9:
    if (v_stack_m90 != 0) goto loc_00211B00;
loc_002118E2:
    goto loc_002116C4;
loc_002118F3:
    result = KeAbPostReleaseEx(v_stack_p10, v_stack_m90, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(Arg5));
    goto loc_00211714;
loc_00211903:
    Arg4 = ((uint32_t)(Arg5)) + 1;
    if (Arg4 <= 6) goto loc_002112F3;
loc_00211913:
    v_stack_m90 = (uint8_t)(v_stack_m90);
    if ((*(uint32_t *)(v_rip + 0xDB53F5)) != ((uint32_t)(v_stack_m90))) goto loc_00211A5D;
loc_00211931:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00211AB0;
loc_0021194A:
    local_r11 = 0;
    v_stack_p8 = 1;
    v_stack_m98 = 0;
    if (((1) & ((uint8_t)(*(uint64_t *)(v_stack_p10)))) != 0) goto loc_00211A4A;
loc_00211969:
loc_00211976:
    if ((*(uint64_t *)(v_stack_p20 + 0x6B8)) == (v_stack_p20 + 1720)) goto loc_0021131C;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_p20 + 0x6B8) + 0x25)) & (2)) != 0) goto loc_00211AF8;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x6B8) + 0x18)) != v_stack_p10) goto loc_00211AF8;
    goto loc_0021131C;
loc_0021199B:
loc_002119A2:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x6B8) + 0x18)) != v_stack_p10) goto loc_002119A2;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x6B8) + 0x18)) >= v_stack_p10) goto loc_00211845;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(v_stack_p20 + 0x6B8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x6B8)))), v_stack_p20 + 1720, 1);
    goto loc_00211845;
loc_002119C3:
    if ((*(uint32_t *)(v_rip + 0xDB5356)) != ((uint32_t)(v_stack_m90))) {
        Arg1 = 2;
        Arg2 = (uint8_t)((uint8_t)(v_stack_m90));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_p20 + 1720, 1);
    }
    result = 0;
    v_stack_p8 = 0;
    goto loc_002118D9;
loc_002119EB:
    if (v_stack_m90 == 0) goto loc_0021187D;
    result = KeAbMarkCrossThreadReleasable(Arg1, v_stack_m90, v_stack_p20 + 1720, 1);
    goto loc_0021187D;
loc_00211A01:
loc_00211A08:
    if (v_stack_m90 != 0) goto loc_00211A08;
    if (condition_is_above_or_equal) goto loc_002118CC;
    result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x6B8)))), v_stack_p20 + 1720, 1);
    goto loc_002118CC;
loc_00211A2E:
    if ((uint32_t)((uint8_t)(v_stack_m90)) != 0) goto loc_00211AD8;
loc_00211A37:
    result = ObfReferenceObjectWithTag(v_stack_p20, (uint32_t)(0x746C6644ULL), v_stack_p20 + 1720, v_stack_p8);
    goto loc_0021184E;
loc_00211A4A:
    if ((*(uint64_t *)(v_stack_p10 + 0x50)) != v_stack_p20) goto loc_00211969;
    goto loc_0021131C;
loc_00211A5D:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)(v_stack_m90)), (uint8_t)(result), v_stack_p20 + 1720, v_stack_p8);
    goto loc_00211931;
loc_00211A6E:
    if (0 != result) {
        *(uint64_t *)(local_r13 + 0x18) = v_stack_p10;
    }
    *(uint64_t *)(local_r13 + 0x10) = v_stack_p20;
    *(uint32_t *)(local_r13 + 0x20) = 1;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x6B8) + 0x8)) != (v_stack_p20 + 1720)) goto loc_00211597;
    *(uint64_t *)(local_r13) = *(uint64_t *)(v_stack_p20 + 0x6B8);
    *(uint64_t *)(local_r13 + 0x8) = v_stack_p20 + 1720;
    *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x6B8) + 0x8) = 0;
    *(uint64_t *)(v_stack_p20 + 0x6B8) = 0;
    goto loc_002118AA;
loc_00211AB0:
loc_00211AB7:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x6B8) + 0x8)) != (v_stack_p20 + 1720)) goto loc_00211AB7;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x6B8) + 0x8)) >= (v_stack_p20 + 1720)) goto loc_0021194A;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(v_stack_p20 + 0x6B8), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x6B8)))), v_stack_p20 + 1720, v_stack_p8);
    goto loc_0021194A;
loc_00211AD8:
    if (v_stack_m90 == 0) goto loc_00211A37;
    result = KeAbMarkCrossThreadReleasable(*(uint64_t *)(v_stack_p20 + 0x6B8), v_stack_m90, v_stack_p20 + 1720, v_stack_p8);
    goto loc_00211A37;
loc_00211AEE:
    goto loc_002118D0;
loc_00211AF8:
    goto loc_00211976;
loc_00211B00:
    result = KeAbPostReleaseEx(v_stack_p10, v_stack_m90, v_stack_p20 + 1720, v_stack_p8);
    goto loc_002118E2;
loc_00211B13:
    Arg1 = (v_stack_p10) + (0x6C8ULL);
    result = KeAcquireSpinLockAtDpcLevel(Arg1, v_stack_m90, v_stack_p20 + 1720, v_stack_p8);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x6D0) + 0x8)) != (v_stack_p20 + 1744)) goto loc_00211597;
    *(uint64_t *)(v_stack_m98) = *(uint64_t *)(v_stack_p20 + 0x6D0);
    *(uint64_t *)(v_stack_m98 + 0x8) = v_stack_p20 + 1744;
    *(uint64_t *)(*(uint64_t *)(v_stack_p20 + 0x6D0) + 0x8) = v_stack_m98;
    *(uint64_t *)(v_stack_p20 + 0x6D0) = v_stack_m98;
    result = KxReleaseSpinLock(v_stack_p20 + 1736, *(uint64_t *)(v_stack_p20 + 0x6D0), v_stack_p20, v_stack_p8);
    goto loc_00211827;
loc_00211B57:
    result = KeAcquireSpinLockAtDpcLevel(*(uint64_t *)(v_stack_p20 + 0x6D0) + 1736, *(uint64_t *)(v_stack_p20 + 0x6D0), v_stack_p20, v_stack_p8);
    result = (v_stack_p20) + (0x6D0ULL);
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) != result) goto loc_00211597;
    *(uint64_t *)(v_stack_m98) = *(uint64_t *)(result);
    *(uint64_t *)(v_stack_m98 + 0x8) = result;
    *(uint64_t *)(*(uint64_t *)(result) + 0x8) = v_stack_m98;
    *(uint64_t *)(result) = v_stack_m98;
    result = KxReleaseSpinLock(*(uint64_t *)(v_stack_p20 + 0x6D0) + 1736, *(uint64_t *)(v_stack_p20 + 0x6D0), v_stack_p20, v_stack_p8);
    goto loc_0021164B;
loc_00211B99:
    Arg3 = 0;
    result = KeAbPreAcquire(v_stack_p10, v_stack_m90, Arg3, v_stack_p8);
    goto loc_002116BC;
loc_00211BAC:
    result = KeAbMarkCrossThreadReleasable(v_stack_p10, v_stack_m90, Arg3, v_stack_p8);
    goto loc_0021171E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x38` | `32` | `R/W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x6B8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00211260&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
