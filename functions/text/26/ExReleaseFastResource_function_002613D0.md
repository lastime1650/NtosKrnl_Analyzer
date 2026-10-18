# ExReleaseFastResource

- RVA: `0x002613D0`–`0x00261BE6` (길이 `2,070` bytes)
- VA: `0x00000001402613D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000644C4`
- 디코드: `537`개 명령, `2,070/2,070` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00261413` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0026144D` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0026147A` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002614AB` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002614D3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00261567` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002616B9` → [KeAbPostReleaseEx](KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x002616F1` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x0026175B` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0026177A` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x00261798` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0026180C` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0026183C` → [KiRemoveSystemWorkPriorityKick](KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0026184E` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002618CD` → [KiAbConvertWaiterToOwnerEntry](../21/KiAbConvertWaiterToOwnerEntry_function_00219430.md) (function, `0x00219430`)
- `0x002618D9` → [KiAcquireKobjectLockSafe](../25/KiAcquireKobjectLockSafe_function_00251C90.md) (function, `0x00251C90`)
- `0x0026193A` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x0026197C` → [KiRemoveBoostThread](../21/KiRemoveBoostThread_function_00219128.md) (function, `0x00219128`)
- `0x0026199D` → [KiExitDispatcher](../25/KiExitDispatcher_function_00251CF0.md) (function, `0x00251CF0`)
- `0x002619AC` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x002619F3` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00261A11` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x00261A54` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00261B0A` → [KeAbPostReleaseEx](KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x00261B1B` → [ExpReleaseFastResourceExclusiveSlow](ExpReleaseFastResourceExclusiveSlow_function_00262CF0.md) (function, `0x00262CF0`)
- `0x00261B37` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00261B57` → [KiRemoveSystemWorkPriorityKick](KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x00261B77` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00261B9F` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00261BC3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00261BDC` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)

### Direct callers
- [sub_0025D903](../25/Unknown_function_0025D903.md) at `0x0025E59E`
- [sub_00260301](Unknown_function_00260301.md) at `0x00260335`
- [ExpFastResourceLegacyRelease](../47/ExpFastResourceLegacyRelease_function_00474224.md) at `0x004742F7`
- [DifExReleaseFastResourceWrapper](../62/DifExReleaseFastResourceWrapper_function_006229E0.md) at `0x00622AB7`

### Static image references
- `0x00261583` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002615A1` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x002616DB` → RVA `0x00F0DE58` (`.data`; read)
- `0x00261725` → RVA `0x00FC6B06` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002613D0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
002613D5  55                              push rbp
002613D6  56                              push rsi
002613D7  57                              push rdi
002613D8  41 54                           push r12
002613DA  41 55                           push r13
002613DC  41 56                           push r14
002613DE  41 57                           push r15
002613E0  48 83 EC 60                     sub rsp, 0x60
002613E4  48 8B 01                        mov rax, qword ptr [rcx]
002613E7  48 8B F1                        mov rsi, rcx
002613EA  0F B7 49 1A                     movzx ecx, word ptr [rcx + 0x1a]
002613EE  48 8B DA                        mov rbx, rdx
002613F1  66 83 E1 01                     and cx, 1
002613F5  A8 01                           test al, 1
002613F7  75 20                           jne 0x140261419
002613F9  66 85 C9                        test cx, cx
002613FC  75 55                           jne 0x140261453
002613FE  33 FF                           xor edi, edi
00261400  45 33 C9                        xor r9d, r9d
00261403  4C 8B C6                        mov r8, rsi
00261406  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0026140B  B9 C6 01 00 00                  mov ecx, 0x1c6
00261410  8D 57 03                        lea edx, [rdi + 3]
00261413  E8 48 C2 29 00                  call 0x1404fd660
00261418  CC                              int3
00261419  4C 8D 46 40                     lea r8, [rsi + 0x40]
0026141D  66 85 C9                        test cx, cx
00261420  74 DC                           je 0x1402613fe
00261422  44 0F 20 C0                     mov rax, cr8
00261426  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0026142F  3C 02                           cmp al, 2
00261431  0F 86 E4 05 00 00               jbe 0x140261a1b
00261437  33 FF                           xor edi, edi
00261439  44 0F B6 C0                     movzx r8d, al
0026143D  33 D2                           xor edx, edx
0026143F  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00261444  B9 C6 01 00 00                  mov ecx, 0x1c6
00261449  44 8D 4F 02                     lea r9d, [rdi + 2]
0026144D  E8 0E C2 29 00                  call 0x1404fd660
00261452  CC                              int3
00261453  44 0F 20 C0                     mov rax, cr8
00261457  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00261460  3C 02                           cmp al, 2
00261462  76 1C                           jbe 0x140261480
00261464  33 FF                           xor edi, edi
00261466  44 0F B6 C0                     movzx r8d, al
0026146A  33 D2                           xor edx, edx
0026146C  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00261471  B9 C6 01 00 00                  mov ecx, 0x1c6
00261476  44 8D 4F 02                     lea r9d, [rdi + 2]
0026147A  E8 E1 C1 29 00                  call 0x1404fd660
0026147F  CC                              int3
00261480  3C 01                           cmp al, 1
00261482  73 2D                           jae 0x1402614b1
00261484  F7 41 74 00 04 00 00            test dword ptr [rcx + 0x74], 0x400
0026148B  75 24                           jne 0x1402614b1
0026148D  83 B9 E4 01 00 00 00            cmp dword ptr [rcx + 0x1e4], 0
00261494  75 1B                           jne 0x1402614b1
00261496  33 FF                           xor edi, edi
00261498  45 33 C9                        xor r9d, r9d
0026149B  45 33 C0                        xor r8d, r8d
0026149E  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
002614A3  B9 C6 01 00 00                  mov ecx, 0x1c6
002614A8  8D 57 07                        lea edx, [rdi + 7]
002614AB  E8 B0 C1 29 00                  call 0x1404fd660
002614B0  CC                              int3
002614B1  48 8B 52 10                     mov rdx, qword ptr [rdx + 0x10]
002614B5  4C 8B CA                        mov r9, rdx
002614B8  49 83 E1 FE                     and r9, 0xfffffffffffffffe
002614BC  4C 3B C9                        cmp r9, rcx
002614BF  74 18                           je 0x1402614d9
002614C1  33 FF                           xor edi, edi
002614C3  4C 8B C3                        mov r8, rbx
002614C6  B9 C6 01 00 00                  mov ecx, 0x1c6
002614CB  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
002614D0  8D 57 09                        lea edx, [rdi + 9]
002614D3  E8 88 C1 29 00                  call 0x1404fd660
002614D8  CC                              int3
002614D9  F6 43 25 02                     test byte ptr [rbx + 0x25], 2
002614DD  75 0D                           jne 0x1402614ec
002614DF  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
002614E3  48 3B C6                        cmp rax, rsi
002614E6  0F 85 95 06 00 00               jne 0x140261b81
002614EC  F6 C2 01                        test dl, 1
002614EF  75 61                           jne 0x140261552
002614F1  FF 4B 20                        dec dword ptr [rbx + 0x20]
002614F4  33 C0                           xor eax, eax
002614F6  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002614FB  0F 57 C0                        xorps xmm0, xmm0
002614FE  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00261501  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00261506  85 C0                           test eax, eax
00261508  0F 8F B4 01 00 00               jg 0x1402616c2
0026150E  0F 0D 0E                        prefetchw byte ptr [rsi]
00261511  48 8B 06                        mov rax, qword ptr [rsi]
00261514  48 8B C8                        mov rcx, rax
00261517  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0026151B  48 FF C9                        dec rcx
0026151E  48 33 C8                        xor rcx, rax
00261521  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
00261525  48 33 C8                        xor rcx, rax
00261528  F6 C1 02                        test cl, 2
0026152B  75 40                           jne 0x14026156d
0026152D  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
00261532  75 E0                           jne 0x140261514
00261534  FA                              cli
00261535  48 8B 0B                        mov rcx, qword ptr [rbx]
00261538  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0026153C  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
00261540  75 09                           jne 0x14026154b
00261542  48 39 18                        cmp qword ptr [rax], rbx
00261545  0F 84 33 01 00 00               je 0x14026167e
0026154B  B9 03 00 00 00                  mov ecx, 3
00261550  CD 29                           int 0x29
00261552  33 FF                           xor edi, edi
00261554  45 33 C9                        xor r9d, r9d
00261557  4C 8B C3                        mov r8, rbx
0026155A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0026155F  B9 C6 01 00 00                  mov ecx, 0x1c6
00261564  8D 57 0A                        lea edx, [rdi + 0xa]
00261567  E8 F4 C0 29 00                  call 0x1404fd660
0026156C  CC                              int3
0026156D  48 F7 C1 FC FF FF FF            test rcx, -4
00261574  7F B7                           jg 0x14026152d
00261576  45 0F 20 C4                     mov r12, cr8
0026157A  BD 02 00 00 00                  mov ebp, 2
0026157F  44 0F 22 C5                     mov cr8, rbp
00261583  83 3D 96 57 D6 00 00            cmp dword ptr [rip + 0xd65796], 0
0026158A  0F 85 B6 02 00 00               jne 0x140261846
00261590  33 FF                           xor edi, edi
00261592  48 8D 4E 30                     lea rcx, [rsi + 0x30]
00261596  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0026159B  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
002615A0  90                              nop
002615A1  F6 05 5E 55 D6 00 21            test byte ptr [rip + 0xd6555e], 0x21
002615A8  0F 85 2D 01 00 00               jne 0x1402616db
002615AE  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
002615B3  48 87 11                        xchg qword ptr [rcx], rdx
002615B6  48 85 D2                        test rdx, rdx
002615B9  0F 85 E8 03 00 00               jne 0x1402619a7
002615BF  0F 0D 0E                        prefetchw byte ptr [rsi]
002615C2  48 8B 16                        mov rdx, qword ptr [rsi]
002615C5  41 BD 01 00 00 00               mov r13d, 1
002615CB  4C 8B 4E 10                     mov r9, qword ptr [rsi + 0x10]
002615CF  4C 8B C2                        mov r8, rdx
002615D2  49 C1 F8 02                     sar r8, 2
002615D6  49 FF C8                        dec r8
002615D9  4D 85 C9                        test r9, r9
002615DC  0F 84 19 01 00 00               je 0x1402616fb
002615E2  41 8B C5                        mov eax, r13d
002615E5  44 8B F8                        mov r15d, eax
002615E8  48 8B CA                        mov rcx, rdx
002615EB  48 83 E1 FD                     and rcx, 0xfffffffffffffffd
002615EF  48 03 C0                        add rax, rax
002615F2  48 0B C1                        or rax, rcx
002615F5  48 8B C8                        mov rcx, rax
002615F8  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
002615FC  48 FF C9                        dec rcx
002615FF  48 33 C8                        xor rcx, rax
00261602  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
00261606  48 33 C8                        xor rcx, rax
00261609  4C 8B D1                        mov r10, rcx
0026160C  4D 3B C5                        cmp r8, r13
0026160F  73 0C                           jae 0x14026161d
00261611  4D 85 C9                        test r9, r9
00261614  0F 84 B4 03 00 00               je 0x1402619ce
0026161A  49 0B CD                        or rcx, r13
0026161D  48 3B CA                        cmp rcx, rdx
00261620  74 0D                           je 0x14026162f
00261622  48 8B C2                        mov rax, rdx
00261625  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
0026162A  48 8B D0                        mov rdx, rax
0026162D  75 9C                           jne 0x1402615cb
0026162F  4C 8B F7                        mov r14, rdi
00261632  4D 3B C5                        cmp r8, r13
00261635  0F 83 84 03 00 00               jae 0x1402619bf
0026163B  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
0026163F  48 85 C9                        test rcx, rcx
00261642  0F 84 6E 03 00 00               je 0x1402619b6
00261648  48 8B 11                        mov rdx, qword ptr [rcx]
0026164B  48 3B D1                        cmp rdx, rcx
0026164E  0F 84 B7 00 00 00               je 0x14026170b
00261654  48 89 56 10                     mov qword ptr [rsi + 0x10], rdx
00261658  4C 8B 01                        mov r8, qword ptr [rcx]
0026165B  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
0026165F  49 39 48 08                     cmp qword ptr [r8 + 8], rcx
00261663  0F 85 E2 FE FF FF               jne 0x14026154b
00261669  48 39 0A                        cmp qword ptr [rdx], rcx
0026166C  0F 85 D9 FE FF FF               jne 0x14026154b
00261672  4C 89 02                        mov qword ptr [rdx], r8
00261675  49 89 50 08                     mov qword ptr [r8 + 8], rdx
00261679  E9 91 00 00 00                  jmp 0x14026170f
0026167E  48 89 08                        mov qword ptr [rax], rcx
00261681  33 FF                           xor edi, edi
00261683  48 89 41 08                     mov qword ptr [rcx + 8], rax
00261687  48 89 3B                        mov qword ptr [rbx], rdi
0026168A  48 89 7B 08                     mov qword ptr [rbx + 8], rdi
0026168E  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00261697  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0026169E  4D 85 C0                        test r8, r8
002616A1  0F 85 77 01 00 00               jne 0x14026181e
002616A7  FB                              sti
002616A8  48 89 7B 18                     mov qword ptr [rbx + 0x18], rdi
002616AC  0F B6 43 24                     movzx eax, byte ptr [rbx + 0x24]
002616B0  84 C0                           test al, al
002616B2  74 0E                           je 0x1402616c2
002616B4  8B D0                           mov edx, eax
002616B6  48 8B CE                        mov rcx, rsi
002616B9  E8 52 0B 00 00                  call 0x140262210
002616BE  40 88 7B 24                     mov byte ptr [rbx + 0x24], dil
002616C2  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
002616CA  48 83 C4 60                     add rsp, 0x60
002616CE  41 5F                           pop r15
002616D0  41 5E                           pop r14
002616D2  41 5D                           pop r13
002616D4  41 5C                           pop r12
002616D6  5F                              pop rdi
002616D7  5E                              pop rsi
002616D8  5D                              pop rbp
002616D9  C3                              ret
002616DA  CC                              int3
002616DB  8B 05 77 C7 CA 00               mov eax, dword ptr [rip + 0xcac777]
002616E1  85 C0                           test eax, eax
002616E3  0F 85 C5 FE FF FF               jne 0x1402615ae
002616E9  48 8B D1                        mov rdx, rcx
002616EC  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
002616F1  E8 5A 41 01 00                  call 0x140275850
002616F6  E9 C4 FE FF FF                  jmp 0x1402615bf
002616FB  39 7E 38                        cmp dword ptr [rsi + 0x38], edi
002616FE  0F 87 DE FE FF FF               ja 0x1402615e2
00261704  8B C7                           mov eax, edi
00261706  E9 DA FE FF FF                  jmp 0x1402615e5
0026170B  48 89 7E 10                     mov qword ptr [rsi + 0x10], rdi
0026170F  4C 8B 71 10                     mov r14, qword ptr [rcx + 0x10]
00261713  48 89 49 08                     mov qword ptr [rcx + 8], rcx
00261717  48 89 09                        mov qword ptr [rcx], rcx
0026171A  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
00261722  45 03 FF                        add r15d, r15d
00261725  44 84 2D DA 53 D6 00            test byte ptr [rip + 0xd653da], r13b
0026172C  75 53                           jne 0x140261781
0026172E  0F 0D 4C 24 40                  prefetchw byte ptr [rsp + 0x40]
00261733  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00261738  48 85 C0                        test rax, rax
0026173B  75 23                           jne 0x140261760
0026173D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00261742  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00261747  F0 48 0F B1 39                  lock cmpxchg qword ptr [rcx], rdi
0026174C  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00261751  48 3B C1                        cmp rax, rcx
00261754  74 47                           je 0x14026179d
00261756  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0026175B  E8 40 63 FB FF                  call 0x140217aa0
00261760  48 8D 48 08                     lea rcx, [rax + 8]
00261764  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00261769  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0026176E  48 8B C2                        mov rax, rdx
00261771  48 87 01                        xchg qword ptr [rcx], rax
00261774  32 C2                           xor al, dl
00261776  A8 04                           test al, 4
00261778  74 23                           je 0x14026179d
0026177A  E8 A1 64 FB FF                  call 0x140217c20
0026177F  EB 1C                           jmp 0x14026179d
00261781  8B 05 D1 C6 CA 00               mov eax, dword ptr [rip + 0xcac6d1]
00261787  85 C0                           test eax, eax
00261789  75 A3                           jne 0x14026172e
0026178B  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
00261793  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00261798  E8 53 62 FB FF                  call 0x1402179f0
0026179D  4D 85 F6                        test r14, r14
002617A0  B9 03 00 00 00                  mov ecx, 3
002617A5  41 8B C7                        mov eax, r15d
002617A8  41 0F 44 CD                     cmove ecx, r13d
002617AC  23 C5                           and eax, ebp
002617AE  4D 85 F6                        test r14, r14
002617B1  44 8B F1                        mov r14d, ecx
002617B4  41 0F 44 C7                     cmove eax, r15d
002617B8  41 83 CE 04                     or r14d, 4
002617BC  85 C0                           test eax, eax
002617BE  44 0F 44 F1                     cmove r14d, ecx
002617C2  48 39 BC 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rdi
002617CA  0F 85 88 00 00 00               jne 0x140261858
002617D0  48 8B 0B                        mov rcx, qword ptr [rbx]
002617D3  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
002617D7  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
002617DB  0F 85 6A FD FF FF               jne 0x14026154b
002617E1  48 39 18                        cmp qword ptr [rax], rbx
002617E4  0F 85 61 FD FF FF               jne 0x14026154b
002617EA  48 89 08                        mov qword ptr [rax], rcx
002617ED  48 89 41 08                     mov qword ptr [rcx + 8], rax
002617F1  48 89 3B                        mov qword ptr [rbx], rdi
002617F4  48 89 7B 08                     mov qword ptr [rbx + 8], rdi
002617F8  48 89 7B 18                     mov qword ptr [rbx + 0x18], rdi
002617FC  39 3D 1E 55 D6 00               cmp dword ptr [rip + 0xd6551e], edi
00261802  74 0D                           je 0x140261811
00261804  44 0F 20 C1                     mov rcx, cr8
00261808  41 0F B6 D4                     movzx edx, r12b
0026180C  E8 87 3E 29 00                  call 0x1404f5698
00261811  41 0F B6 C4                     movzx eax, r12b
00261815  44 0F 22 C0                     mov cr8, rax
00261819  E9 8E FE FF FF                  jmp 0x1402616ac
0026181E  41 0F 0D 08                     prefetchw byte ptr [r8]
00261822  41 8B 00                        mov eax, dword ptr [r8]
00261825  8B D0                           mov edx, eax
00261827  0F BA F2 15                     btr edx, 0x15
0026182B  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00261830  75 F3                           jne 0x140261825
00261832  0F BA E0 15                     bt eax, 0x15
00261836  0F 83 6B FE FF FF               jae 0x1402616a7
0026183C  E8 8F 19 00 00                  call 0x1402631d0
00261841  E9 61 FE FF FF                  jmp 0x1402616a7
00261846  40 0F B6 D5                     movzx edx, bpl
0026184A  41 0F B6 CC                     movzx ecx, r12b
0026184E  E8 A9 3E 29 00                  call 0x1404f56fc
00261853  E9 38 FD FF FF                  jmp 0x140261590
00261858  44 0F 20 C0                     mov rax, cr8
0026185C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00261861  44 0F 22 C5                     mov cr8, rbp
00261865  39 3D B5 54 D6 00               cmp dword ptr [rip + 0xd654b5], edi
0026186B  0F 85 7B 01 00 00               jne 0x1402619ec
00261871  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0026187A  41 8B CE                        mov ecx, r14d
0026187D  83 E1 04                        and ecx, 4
00261880  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00261888  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00261890  89 8C 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], ecx
00261897  4C 8D 28                        lea r13, [rax]
0026189A  48 8B 00                        mov rax, qword ptr [rax]
0026189D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002618A2  85 C9                           test ecx, ecx
002618A4  74 2C                           je 0x1402618d2
002618A6  49 8B 55 30                     mov rdx, qword ptr [r13 + 0x30]
002618AA  48 85 D2                        test rdx, rdx
002618AD  74 23                           je 0x1402618d2
002618AF  48 8B 02                        mov rax, qword ptr [rdx]
002618B2  48 8B CA                        mov rcx, rdx
002618B5  0F B6 42 08                     movzx eax, byte ptr [rdx + 8]
002618B9  83 E0 3F                        and eax, 0x3f
002618BC  4C 6B C0 58                     imul r8, rax, 0x58
002618C0  49 2B C8                        sub rcx, r8
002618C3  41 B8 01 00 00 00               mov r8d, 1
002618C9  48 8B 49 F0                     mov rcx, qword ptr [rcx - 0x10]
002618CD  E8 5E 7B FB FF                  call 0x140219430
002618D2  49 8D 6D 18                     lea rbp, [r13 + 0x18]
002618D6  48 8B CD                        mov rcx, rbp
002618D9  E8 B2 03 FF FF                  call 0x140251c90
002618DE  48 83 C5 08                     add rbp, 8
002618E2  41 C7 45 1C 01 00 00 00         mov dword ptr [r13 + 0x1c], 1
002618EA  4C 8B 7D 00                     mov r15, qword ptr [rbp]
002618EE  4C 3B FD                        cmp r15, rbp
002618F1  74 57                           je 0x14026194a
002618F3  49 8B 0F                        mov rcx, qword ptr [r15]
002618F6  49 8B C7                        mov rax, r15
002618F9  4C 8B F9                        mov r15, rcx
002618FC  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00261900  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00261904  0F 85 41 FC FF FF               jne 0x14026154b
0026190A  48 39 02                        cmp qword ptr [rdx], rax
0026190D  0F 85 38 FC FF FF               jne 0x14026154b
00261913  48 89 0A                        mov qword ptr [rdx], rcx
00261916  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0026191A  0F B6 48 10                     movzx ecx, byte ptr [rax + 0x10]
0026191E  80 F9 01                        cmp cl, 1
00261921  0F 85 D6 00 00 00               jne 0x1402619fd
00261927  44 0F B7 40 12                  movzx r8d, word ptr [rax + 0x12]
0026192C  45 33 C9                        xor r9d, r9d
0026192F  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00261937  48 8B D0                        mov rdx, rax
0026193A  E8 91 ED 0E 00                  call 0x1403506d0
0026193F  84 C0                           test al, al
00261941  74 AB                           je 0x1402618ee
00261943  41 83 6D 1C 01                  sub dword ptr [r13 + 0x1c], 1
00261948  75 A4                           jne 0x1402618ee
0026194A  F0 41 81 65 18 7F FF FF FF      lock and dword ptr [r13 + 0x18], 0xffffff7f
00261953  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00261958  8B 8C 24 A0 00 00 00            mov ecx, dword ptr [rsp + 0xa0]
0026195F  48 3B 84 24 B0 00 00 00         cmp rax, qword ptr [rsp + 0xb0]
00261967  0F 85 2A FF FF FF               jne 0x140261897
0026196D  48 8B AC 24 B8 00 00 00         mov rbp, qword ptr [rsp + 0xb8]
00261975  48 8B CD                        mov rcx, rbp
00261978  48 8B 55 08                     mov rdx, qword ptr [rbp + 8]
0026197C  E8 A7 77 FB FF                  call 0x140219128
00261981  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00261986  33 D2                           xor edx, edx
00261988  41 D1 EE                        shr r14d, 1
0026198B  48 8B CD                        mov rcx, rbp
0026198E  41 83 E6 01                     and r14d, 1
00261992  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00261996  45 8B CE                        mov r9d, r14d
00261999  44 8D 42 01                     lea r8d, [rdx + 1]
0026199D  E8 4E 03 FF FF                  call 0x140251cf0
002619A2  E9 29 FE FF FF                  jmp 0x1402617d0
002619A7  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
002619AC  E8 FF 64 FF FF                  call 0x140257eb0
002619B1  E9 09 FC FF FF                  jmp 0x1402615bf
002619B6  39 7E 38                        cmp dword ptr [rsi + 0x38], edi
002619B9  0F 85 9B 00 00 00               jne 0x140261a5a
002619BF  33 C0                           xor eax, eax
002619C1  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
002619C9  E9 54 FD FF FF                  jmp 0x140261722
002619CE  8B 46 38                        mov eax, dword ptr [rsi + 0x38]
002619D1  85 C0                           test eax, eax
002619D3  0F 84 44 FC FF FF               je 0x14026161d
002619D9  48 8D 0C 81                     lea rcx, [rcx + rax*4]
002619DD  49 33 CA                        xor rcx, r10
002619E0  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
002619E4  49 33 CA                        xor rcx, r10
002619E7  E9 31 FC FF FF                  jmp 0x14026161d
002619EC  40 0F B6 D5                     movzx edx, bpl
002619F0  0F B6 C8                        movzx ecx, al
002619F3  E8 04 3D 29 00                  call 0x1404f56fc
002619F8  E9 74 FE FF FF                  jmp 0x140261871
002619FD  80 F9 02                        cmp cl, 2
00261A00  0F 85 58 01 00 00               jne 0x140261b5e
00261A06  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00261A0A  48 8B D0                        mov rdx, rax
00261A0D  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00261A11  E8 1A 81 FB FF                  call 0x140219b30
00261A16  E9 28 FF FF FF                  jmp 0x140261943
00261A1B  3C 01                           cmp al, 1
00261A1D  73 16                           jae 0x140261a35
00261A1F  F7 41 74 00 04 00 00            test dword ptr [rcx + 0x74], 0x400
00261A26  75 0D                           jne 0x140261a35
00261A28  83 B9 E4 01 00 00 00            cmp dword ptr [rcx + 0x1e4], 0
00261A2F  0F 84 61 FA FF FF               je 0x140261496
00261A35  49 8B 50 10                     mov rdx, qword ptr [r8 + 0x10]
00261A39  4C 8B CA                        mov r9, rdx
00261A3C  49 83 E1 FE                     and r9, 0xfffffffffffffffe
00261A40  4C 3B C9                        cmp r9, rcx
00261A43  74 2D                           je 0x140261a72
00261A45  33 FF                           xor edi, edi
00261A47  B9 C6 01 00 00                  mov ecx, 0x1c6
00261A4C  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00261A51  8D 57 09                        lea edx, [rdi + 9]
00261A54  E8 07 BC 29 00                  call 0x1404fd660
00261A59  CC                              int3
00261A5A  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00261A5E  48 89 7E 08                     mov qword ptr [rsi + 8], rdi
00261A62  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00261A6A  89 7E 38                        mov dword ptr [rsi + 0x38], edi
00261A6D  E9 B0 FC FF FF                  jmp 0x140261722
00261A72  41 F6 40 25 02                  test byte ptr [r8 + 0x25], 2
00261A77  75 0D                           jne 0x140261a86
00261A79  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
00261A7D  48 3B C6                        cmp rax, rsi
00261A80  0F 85 1F 01 00 00               jne 0x140261ba5
00261A86  F6 C2 01                        test dl, 1
00261A89  0F 85 96 00 00 00               jne 0x140261b25
00261A8F  83 6E 60 01                     sub dword ptr [rsi + 0x60], 1
00261A93  48 8D 5E 40                     lea rbx, [rsi + 0x40]
00261A97  0F 85 25 FC FF FF               jne 0x1402616c2
00261A9D  0F B6 6B 24                     movzx ebp, byte ptr [rbx + 0x24]
00261AA1  FA                              cli
00261AA2  48 8B 0B                        mov rcx, qword ptr [rbx]
00261AA5  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00261AA9  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
00261AAD  0F 85 98 FA FF FF               jne 0x14026154b
00261AB3  48 39 18                        cmp qword ptr [rax], rbx
00261AB6  0F 85 8F FA FF FF               jne 0x14026154b
00261ABC  48 89 08                        mov qword ptr [rax], rcx
00261ABF  33 FF                           xor edi, edi
00261AC1  48 89 41 08                     mov qword ptr [rcx + 8], rax
00261AC5  48 89 3B                        mov qword ptr [rbx], rdi
00261AC8  48 89 7B 08                     mov qword ptr [rbx + 8], rdi
00261ACC  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00261AD5  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
00261ADC  4D 85 C0                        test r8, r8
00261ADF  75 5C                           jne 0x140261b3d
00261AE1  FB                              sti
00261AE2  48 89 7B 10                     mov qword ptr [rbx + 0x10], rdi
00261AE6  40 88 7B 24                     mov byte ptr [rbx + 0x24], dil
00261AEA  0F 0D 0E                        prefetchw byte ptr [rsi]
00261AED  48 8B 06                        mov rax, qword ptr [rsi]
00261AF0  A8 02                           test al, 2
00261AF2  75 20                           jne 0x140261b14
00261AF4  F0 48 0F B1 3E                  lock cmpxchg qword ptr [rsi], rdi
00261AF9  75 F5                           jne 0x140261af0
00261AFB  40 84 ED                        test bpl, bpl
00261AFE  0F 84 BE FB FF FF               je 0x1402616c2
00261B04  48 8B D5                        mov rdx, rbp
00261B07  48 8B CE                        mov rcx, rsi
00261B0A  E8 01 07 00 00                  call 0x140262210
00261B0F  E9 AE FB FF FF                  jmp 0x1402616c2
00261B14  40 0F B6 D5                     movzx edx, bpl
00261B18  48 8B CE                        mov rcx, rsi
00261B1B  E8 D0 11 00 00                  call 0x140262cf0
00261B20  E9 9D FB FF FF                  jmp 0x1402616c2
00261B25  33 FF                           xor edi, edi
00261B27  45 33 C9                        xor r9d, r9d
00261B2A  B9 C6 01 00 00                  mov ecx, 0x1c6
00261B2F  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00261B34  8D 57 0A                        lea edx, [rdi + 0xa]
00261B37  E8 24 BB 29 00                  call 0x1404fd660
00261B3C  CC                              int3
00261B3D  41 0F 0D 08                     prefetchw byte ptr [r8]
00261B41  41 8B 00                        mov eax, dword ptr [r8]
00261B44  8B D0                           mov edx, eax
00261B46  0F BA F2 15                     btr edx, 0x15
00261B4A  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
00261B4F  75 F3                           jne 0x140261b44
00261B51  0F BA E0 15                     bt eax, 0x15
00261B55  73 8A                           jae 0x140261ae1
00261B57  E8 74 16 00 00                  call 0x1402631d0
00261B5C  EB 83                           jmp 0x140261ae1
00261B5E  80 F9 04                        cmp cl, 4
00261B61  74 66                           je 0x140261bc9
00261B63  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00261B6B  45 33 C9                        xor r9d, r9d
00261B6E  41 B8 00 01 00 00               mov r8d, 0x100
00261B74  48 8B D0                        mov rdx, rax
00261B77  E8 54 EB 0E 00                  call 0x1403506d0
00261B7C  E9 6D FD FF FF                  jmp 0x1402618ee
00261B81  48 85 C0                        test rax, rax
00261B84  0F 84 62 F9 FF FF               je 0x1402614ec
00261B8A  4C 8B CB                        mov r9, rbx
00261B8D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00261B92  4C 8B C6                        mov r8, rsi
00261B95  BA 08 00 00 00                  mov edx, 8
00261B9A  B9 C6 01 00 00                  mov ecx, 0x1c6
00261B9F  E8 BC BA 29 00                  call 0x1404fd660
00261BA4  CC                              int3
00261BA5  48 85 C0                        test rax, rax
00261BA8  0F 84 D8 FE FF FF               je 0x140261a86
00261BAE  4D 8B C8                        mov r9, r8
00261BB1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00261BB6  4C 8B C6                        mov r8, rsi
00261BB9  BA 08 00 00 00                  mov edx, 8
00261BBE  B9 C6 01 00 00                  mov ecx, 0x1c6
00261BC3  E8 98 BA 29 00                  call 0x1404fd660
00261BC8  CC                              int3
00261BC9  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00261BCD  49 8D 55 18                     lea rdx, [r13 + 0x18]
00261BD1  41 89 7D 1C                     mov dword ptr [r13 + 0x1c], edi
00261BD5  4C 8B C0                        mov r8, rax
00261BD8  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00261BDC  E8 6F 60 FA FF                  call 0x140207c50
00261BE1  E9 08 FD FF FF                  jmp 0x1402618ee
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExReleaseFastResource(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p98;
    unsigned int v_stack_pA0;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (96);
    a1 = (unsigned __int16)((*(unsigned __int16 *)(a1 + 26)) & (1));
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (1)) != 0) goto loc_00261419;
    if ((unsigned __int16)(a1) != 0) goto loc_00261453;
loc_002613FE:
    v_rdi = 0;
    a4 = 0;
    v_stack_m78 = 0;
    result = KeBugCheckEx(454, v_rdi + 3, a1, a4);
loc_00261419:
    if (454 == 0) goto loc_002613FE;
    if (((unsigned __int8)(v_cr8)) <= 2) goto loc_00261A1B;
    v_rdi = 0;
    a2 = 0;
    v_stack_m78 = 0;
    result = KeBugCheckEx(454, a2, (unsigned __int8)(v_cr8), v_rdi + 2);
loc_00261453:
    result = v_cr8;
    if (((unsigned __int8)(v_cr8)) >= = 2) {
        v_rdi = 0;
        a3 = (unsigned __int8)(v_cr8);
        a2 = 0;
        v_stack_m78 = 0;
        a1 = 454;
        a4 = v_rdi + 2;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((unsigned __int8)(result)) >= 1) goto loc_002614B1;
    if (((*(unsigned int *)(a1 + 116)) & (0x400ULL)) != 0) goto loc_002614B1;
    if ((*(unsigned int *)(a1 + 484)) == 0) {
        v_rdi = 0;
        a4 = 0;
        a3 = 0;
        v_stack_m78 = 0;
        a1 = 454;
        a2 = v_rdi + 7;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a4 = (*(unsigned __int64 *)(a2 + 16)) & (-2);
    if (a4 != a1) {
        v_rdi = 0;
        a3 = a2;
        a1 = 454;
        v_stack_m78 = 0;
        a2 = v_rdi + 9;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(a2 + 37)) & (2)) != 0) goto loc_002614EC;
    if ((*(unsigned __int64 *)(a2 + 24)) != a1) goto loc_00261B81;
loc_002614EC:
    if ((((unsigned __int8)(a2)) & (1)) != 0) goto loc_00261552;
    result = 0;
    v_stack_m48 = 0;
    v_stack_m58 = v_xmm0;
    if (condition_is_greater) goto loc_002616C2;
loc_00261514:
    a1 = (*(unsigned __int64 *)(a1)) & (-4);
    a1 = (a1) - 1;
    a1 = (a1) ^ (*(unsigned __int64 *)(a1));
    a1 = (a1) & (-4);
    a1 = (a1) ^ (*(unsigned __int64 *)(a1));
    if ((((unsigned __int8)(a1)) & (2)) != 0) goto loc_0026156D;
loc_0026152D:
    if ((((unsigned __int8)(a1)) & (2)) != 0) goto loc_00261514;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 8)) != a2) goto loc_0026154B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8))) == a2) goto loc_0026167E;
loc_0026154B:
loc_00261552:
    v_rdi = 0;
    a4 = 0;
    v_stack_m78 = 0;
    result = KeBugCheckEx(454, v_rdi + 10, a2, a4);
loc_0026156D:
    if (condition_is_greater) goto loc_0026152D;
    if ((*(unsigned int *)(v_rip + 14047126)) != 0) goto loc_00261846;
loc_00261590:
    v_rdi = 0;
    v_stack_m50 = a1 + 48;
    v_stack_m58 = 0;
    if (((*(unsigned __int8 *)(v_rip + 14046558)) & (33)) != 0) goto loc_002616DB;
loc_002615AE:
    if (v_stack_m58 != 0) goto loc_002619A7;
loc_002615BF:
loc_002615CB:
    a3 = (*(unsigned __int64 *)(a1)) >> (2);
    a3 = (a3) - 1;
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_002616FB;
loc_002615E2:
loc_002615E5:
    a1 = (*(unsigned __int64 *)(a1)) & (-3);
    result = (1) + (1);
    result = (result) | (a1);
    a1 = (result) & (-4);
    a1 = (a1) - 1;
    a1 = (a1) ^ (result);
    a1 = (a1) & (-4);
    a1 = (a1) ^ (result);
    if (a3 >= 1) goto loc_0026161D;
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_002619CE;
    a1 = (a1) | (1);
loc_0026161D:
    if (a1 == (*(unsigned __int64 *)(a1))) goto loc_0026162F;
    if (a1 != (*(unsigned __int64 *)(a1))) goto loc_002615CB;
loc_0026162F:
    if (a3 >= 1) goto loc_002619BF;
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_002619B6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16))) == (*(unsigned __int64 *)(a1 + 16))) goto loc_0026170B;
    *(unsigned __int64 *)(a1 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)) + 8)) != (*(unsigned __int64 *)(a1 + 16))) goto loc_0026154B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8))) != (*(unsigned __int64 *)(a1 + 16))) goto loc_0026154B;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8);
    goto loc_0026170F;
loc_0026167E:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1)) = *(unsigned __int64 *)(a1 + 16);
    v_rdi = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(a2) = 0;
    *(unsigned __int64 *)(a2 + 8) = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0026181E;
loc_002616A7:
    *(unsigned __int64 *)(a2 + 24) = 0;
loc_002616AC:
    result = *(unsigned __int8 *)(a2 + 36);
    if ((unsigned __int8)(*(unsigned __int8 *)(a2 + 36)) != 0) {
        a2 = (unsigned int)(*(unsigned __int8 *)(a2 + 36));
        a1 = a1;
        result = KeAbPostReleaseEx(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(a1 + 16));
        *(unsigned __int8 *)(a2 + 36) = 0;
    }
    v_rsp = (v_rsp) + (96);
    return result;
loc_002616DB:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13289335))) != 0) goto loc_002615AE;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_p40, a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(a1 + 16));
    goto loc_002615BF;
loc_002616FB:
    if ((*(unsigned int *)(a1 + 56)) > 0) goto loc_002615E2;
    goto loc_002615E5;
loc_0026170B:
    *(unsigned __int64 *)(a1 + 16) = 0;
loc_0026170F:
    *(unsigned __int64 *)(v_stack_p40 + 8) = v_stack_p40;
    *(unsigned __int64 *)(v_stack_p40) = v_stack_p40;
    v_stack_pB0 = v_stack_p40;
loc_00261722:
    v_r15 = (unsigned int)((1) + (1));
    if (((*(unsigned __int8 *)(v_rip + 14046170)) & (1)) != 0) goto loc_00261781;
loc_0026172E:
    if (v_stack_p40 != 0) goto loc_00261760;
    if (v_stack_p40 == v_stack_p40) goto loc_0026179D;
    result = KxWaitForLockChainValid(v_stack_p40, a1, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(a1 + 16));
loc_00261760:
    v_stack_p40 = 0;
    result = (unsigned __int8)((v_stack_p48) ^ ((unsigned __int8)(v_stack_p48)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0026179D;
    result = KeWakeAddressAll(result + 8, v_stack_p48, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(a1 + 16));
    goto loc_0026179D;
loc_00261781:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13289169))) != 0) goto loc_0026172E;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_p40, v_stack_p98, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(a1 + 16));
loc_0026179D:
    a1 = 3;
    if (*(unsigned __int64 *)(v_stack_p40 + 16) == 0) { a1 = 1; }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (2));
    if (*(unsigned __int64 *)(v_stack_p40 + 16) == 0) { result = (unsigned int)(v_r15); }
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (4));
    if ((unsigned int)(result) == 0) { v_r14 = (unsigned int)(a1); }
    if (v_stack_pB0 != 0) goto loc_00261858;
loc_002617D0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10) + 8)) != v_stack_p10) goto loc_0026154B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 8))) != v_stack_p10) goto loc_0026154B;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 8)) = *(unsigned __int64 *)(v_stack_p10);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10) + 8) = *(unsigned __int64 *)(v_stack_p10 + 8);
    *(unsigned __int64 *)(v_stack_p10) = 0;
    *(unsigned __int64 *)(v_stack_p10 + 8) = 0;
    *(unsigned __int64 *)(v_stack_p10 + 24) = 0;
    result = *(unsigned __int64 *)(v_stack_p10 + 8);
    if ((*(unsigned int *)(v_rip + 14046494)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(a1 + 16));
    }
    goto loc_002616AC;
loc_0026181E:
loc_00261825:
    if ((*(unsigned int *)(v_rip + 14046494)) != 0) goto loc_00261825;
    if ((*(unsigned int *)(v_rip + 14046494)) >= 0) goto loc_002616A7;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(a1 + 16));
    goto loc_002616A7;
loc_00261846:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), 2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), *(unsigned __int64 *)(a1 + 16));
    goto loc_00261590;
loc_00261858:
    v_stack_p38 = (unsigned __int8)(v_cr8);
    if ((*(unsigned int *)(v_rip + 14046389)) != 0) goto loc_002619EC;
loc_00261871:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (4));
    v_stack_pB8 = *(unsigned __int64 *)(gs_base + (0 + 32));
    v_stack_pA0 = (unsigned int)(a1);
loc_00261897:
    v_stack_p30 = *(unsigned __int64 *)(v_stack_pB0);
    if ((unsigned int)(a1) == 0) goto loc_002618D2;
    result = *(unsigned __int64 *)(v_stack_pB0);
    if (*(unsigned __int64 *)(v_stack_pB0 + 48) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pB0 + 48));
        a1 = *(unsigned __int64 *)(v_stack_pB0 + 48);
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_pB0 + 48) + 8);
        result = (unsigned int)((result) & (63));
        a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536)) * (result);
        a1 = (a1) - (a3);
        a3 = 1;
        a1 = *(unsigned __int64 *)(a1 - 16);
        result = KiAbConvertWaiterToOwnerEntry(a1, *(unsigned __int64 *)(v_stack_pB0 + 48), a3, *(unsigned __int64 *)(a1 + 16));
    }
    result = KiAcquireKobjectLockSafe(v_stack_pB0 + 24, *(unsigned __int64 *)(v_stack_pB0 + 48), a3, *(unsigned __int64 *)(a1 + 16));
    v_rbp = (v_stack_pB0 + 24) + (8);
    *(unsigned int *)(v_stack_pB0 + 28) = 1;
loc_002618EE:
    if ((*(unsigned __int64 *)(v_rbp)) == v_rbp) goto loc_0026194A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp)) + 8)) != (*(unsigned __int64 *)(v_rbp))) goto loc_0026154B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp) + 8))) != (*(unsigned __int64 *)(v_rbp))) goto loc_0026154B;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp) + 8);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp) + 16))) != 1) goto loc_002619FD;
    a4 = 0;
    result = KiTryUnwaitThread(v_stack_pB8, *(unsigned __int64 *)(v_rbp), *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp) + 18), a4);
    if ((unsigned __int8)(result) == 0) goto loc_002618EE;
loc_00261943:
    if ((unsigned __int8)(result) != 0) goto loc_002618EE;
loc_0026194A:
    if (v_stack_p30 != v_stack_pB0) goto loc_00261897;
    result = KiRemoveBoostThread(v_stack_pB8, *(unsigned __int64 *)(v_stack_pB8 + 8), *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp) + 18), a4);
    a2 = 0;
    v_r14 = (unsigned int)((v_r14) >> (1));
    v_r14 = (unsigned int)((v_r14) & (1));
    v_stack_p20 = (unsigned __int8)(v_stack_p38);
    result = KiExitDispatcher(v_stack_pB8, a2, a2 + 1, (unsigned int)((unsigned int)(v_r14)));
    goto loc_002617D0;
loc_002619A7:
    result = KxWaitForLockOwnerShip(v_stack_p40, a2, a2 + 1, (unsigned int)((unsigned int)(v_r14)));
    goto loc_002615BF;
loc_002619B6:
    if ((*(unsigned int *)(a1 + 56)) != 0) goto loc_00261A5A;
loc_002619BF:
    result = 0;
    v_stack_pB0 = 0;
    goto loc_00261722;
loc_002619CE:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56))) == 0) goto loc_0026161D;
    a1 = (v_stack_p40 + (unsigned int)(*(unsigned int *)(a1 + 56)) * 4) ^ (a1);
    a1 = (a1) & (-4);
    a1 = (a1) ^ (a1);
    goto loc_0026161D;
loc_002619EC:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 56))), (unsigned __int8)(v_stack_pB8), a2 + 1, (unsigned int)((unsigned int)(v_r14)));
    goto loc_00261871;
loc_002619FD:
    if (((unsigned __int8)((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 56))))) != 2) goto loc_00261B5E;
    *(unsigned __int8 *)(result + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(result + 24), result, a2 + 1, (unsigned int)((unsigned int)(v_r14)));
    goto loc_00261943;
loc_00261A1B:
    if (((unsigned __int8)(result)) >= 1) goto loc_00261A35;
    if (((*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 116)) & (0x400ULL)) != 0) goto loc_00261A35;
    if ((*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 484)) == 0) goto loc_00261496;
loc_00261A35:
    a4 = (*(unsigned __int64 *)(a2 + 1 + 16)) & (-2);
    if (a4 == (*(unsigned __int64 *)(result + 24))) goto loc_00261A72;
    v_rdi = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(454, v_rdi + 9, a2 + 1, a4);
loc_00261A5A:
    *(unsigned __int64 *)(a1 + 8) = 0;
    v_stack_pB0 = *(unsigned __int64 *)(a1 + 8);
    *(unsigned int *)(a1 + 56) = 0;
    goto loc_00261722;
loc_00261A72:
    if (((*(unsigned __int8 *)(a2 + 1 + 37)) & (2)) != 0) goto loc_00261A86;
    if ((*(unsigned __int64 *)(a2 + 1 + 24)) != a1) goto loc_00261BA5;
loc_00261A86:
    if ((((unsigned __int8)(v_rdi + 9)) & (1)) != 0) goto loc_00261B25;
    if ((((unsigned __int8)(v_rdi + 9)) & (1)) != 0) goto loc_002616C2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 8)) != (a1 + 64)) goto loc_0026154B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64 + 8))) != (a1 + 64)) goto loc_0026154B;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64 + 8)) = *(unsigned __int64 *)(a1 + 64);
    v_rdi = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 8) = *(unsigned __int64 *)(a1 + 64 + 8);
    *(unsigned __int64 *)(a1 + 64) = 0;
    *(unsigned __int64 *)(a1 + 64 + 8) = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_00261B3D;
loc_00261AE1:
    *(unsigned __int64 *)(a1 + 64 + 16) = 0;
    *(unsigned __int8 *)(a1 + 64 + 36) = 0;
loc_00261AF0:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (2)) != 0) goto loc_00261B14;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (2)) != 0) goto loc_00261AF0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 64 + 36)) == 0) goto loc_002616C2;
    result = KeAbPostReleaseEx(a1, *(unsigned __int8 *)(a1 + 64 + 36), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_002616C2;
loc_00261B14:
    result = ExpReleaseFastResourceExclusiveSlow(a1, (unsigned __int8)(*(unsigned __int8 *)(a1 + 64 + 36)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_002616C2;
loc_00261B25:
    v_rdi = 0;
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(454, v_rdi + 10, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
loc_00261B3D:
loc_00261B44:
    if (condition_is_not_equal) goto loc_00261B44;
    if (condition_is_above_or_equal) goto loc_00261AE1;
    result = KiRemoveSystemWorkPriorityKick(454, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_00261AE1;
loc_00261B5E:
    if (454 == 4) goto loc_00261BC9;
    a4 = 0;
    result = KiTryUnwaitThread(v_stack_pB8, result, 256, a4);
    goto loc_002618EE;
loc_00261B81:
    if (result == 0) goto loc_002614EC;
    v_stack_p20 = result;
    result = KeBugCheckEx(454, 8, a1, a1 + 64);
loc_00261BA5:
    if (result == 0) goto loc_00261A86;
    v_stack_p20 = result;
    result = KeBugCheckEx(454, 8, a1, a1);
loc_00261BC9:
    *(unsigned __int8 *)(result + 17) = 5;
    *(unsigned int *)(v_stack_pB0 + 28) = 0;
    result = KeInsertQueueDpc(*(unsigned __int64 *)(result + 24), v_stack_pB0 + 24, result, a1);
    goto loc_002618EE;
}
```

## 5. (Beta) C Style

```c
int64_t ExReleaseFastResource(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint8_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p98;
    uint32_t v_stack_pA0;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (96);
    Arg1 = (uint16_t)((*(uint16_t *)(arg1 + 0x1A)) & (1));
    if ((((uint8_t)(*(uint64_t *)(arg1))) & (1)) != 0) goto loc_00261419;
    if ((uint16_t)(Arg1) != 0) goto loc_00261453;
loc_002613FE:
    local_rdi = 0;
    Arg4 = 0;
    v_stack_m78 = 0;
    result = KeBugCheckEx(454, local_rdi + 3, Arg1, Arg4);
loc_00261419:
    if (454 == 0) goto loc_002613FE;
    if (((uint8_t)(v_cr8)) <= 2) goto loc_00261A1B;
    local_rdi = 0;
    Arg2 = 0;
    v_stack_m78 = 0;
    result = KeBugCheckEx(454, Arg2, (uint8_t)(v_cr8), local_rdi + 2);
loc_00261453:
    result = v_cr8;
    if (((uint8_t)(v_cr8)) >= = 2) {
        local_rdi = 0;
        Arg3 = (uint8_t)(v_cr8);
        Arg2 = 0;
        v_stack_m78 = 0;
        Arg1 = 454;
        Arg4 = local_rdi + 2;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint8_t)(result)) >= 1) goto loc_002614B1;
    if (((*(uint32_t *)(arg1 + 0x74)) & (0x400ULL)) != 0) goto loc_002614B1;
    if ((*(uint32_t *)(arg1 + 0x1E4)) == 0) {
        local_rdi = 0;
        Arg4 = 0;
        Arg3 = 0;
        v_stack_m78 = 0;
        Arg1 = 454;
        Arg2 = local_rdi + 7;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg4 = (*(uint64_t *)(arg2 + 0x10)) & (-2);
    if (Arg4 != Arg1) {
        local_rdi = 0;
        Arg3 = Arg2;
        Arg1 = 454;
        v_stack_m78 = 0;
        Arg2 = local_rdi + 9;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint8_t *)(arg2 + 0x25)) & (2)) != 0) goto loc_002614EC;
    if ((*(uint64_t *)(arg2 + 0x18)) != Arg1) goto loc_00261B81;
loc_002614EC:
    if ((((uint8_t)(Arg2)) & (1)) != 0) goto loc_00261552;
    result = 0;
    v_stack_m48 = 0;
    v_stack_m58 = v_xmm0;
    if (condition_is_greater) goto loc_002616C2;
loc_00261514:
    Arg1 = (*(uint64_t *)(arg1)) & (-4);
    Arg1 = (Arg1) - 1;
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1));
    Arg1 = (Arg1) & (-4);
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1));
    if ((((uint8_t)(Arg1)) & (2)) != 0) goto loc_0026156D;
loc_0026152D:
    if ((((uint8_t)(Arg1)) & (2)) != 0) goto loc_00261514;
    if ((*(uint64_t *)(*(uint64_t *)(arg2) + 0x8)) != Arg2) goto loc_0026154B;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x8))) == Arg2) goto loc_0026167E;
loc_0026154B:
loc_00261552:
    local_rdi = 0;
    Arg4 = 0;
    v_stack_m78 = 0;
    result = KeBugCheckEx(454, local_rdi + 10, Arg2, Arg4);
loc_0026156D:
    if (condition_is_greater) goto loc_0026152D;
    if ((*(uint32_t *)(v_rip + 0xD65796)) != 0) goto loc_00261846;
loc_00261590:
    local_rdi = 0;
    v_stack_m50 = Arg1 + 48;
    v_stack_m58 = 0;
    if (((*(uint8_t *)(v_rip + 0xD6555E)) & (33)) != 0) goto loc_002616DB;
loc_002615AE:
    if (v_stack_m58 != 0) goto loc_002619A7;
loc_002615BF:
loc_002615CB:
    Arg3 = (*(uint64_t *)(arg1)) >> (2);
    Arg3 = (Arg3) - 1;
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_002616FB;
loc_002615E2:
loc_002615E5:
    Arg1 = (*(uint64_t *)(arg1)) & (-3);
    result = (1) + (1);
    result = (result) | (Arg1);
    Arg1 = (result) & (-4);
    Arg1 = (Arg1) - 1;
    Arg1 = (Arg1) ^ (result);
    Arg1 = (Arg1) & (-4);
    Arg1 = (Arg1) ^ (result);
    if (Arg3 >= 1) goto loc_0026161D;
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_002619CE;
    Arg1 = (Arg1) | (1);
loc_0026161D:
    if (Arg1 == (*(uint64_t *)(arg1))) goto loc_0026162F;
    if (Arg1 != (*(uint64_t *)(arg1))) goto loc_002615CB;
loc_0026162F:
    if (Arg3 >= 1) goto loc_002619BF;
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_002619B6;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x10))) == (*(uint64_t *)(arg1 + 0x10))) goto loc_0026170B;
    *(uint64_t *)(arg1 + 0x10) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)) + 0x8)) != (*(uint64_t *)(arg1 + 0x10))) goto loc_0026154B;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8))) != (*(uint64_t *)(arg1 + 0x10))) goto loc_0026154B;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10)) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8);
    goto loc_0026170F;
loc_0026167E:
    *(uint64_t *)(*(uint64_t *)(arg1)) = *(uint64_t *)(arg1 + 0x10);
    local_rdi = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) = *(uint64_t *)(arg1);
    *(uint64_t *)(arg2) = 0;
    *(uint64_t *)(arg2 + 0x8) = 0;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0026181E;
loc_002616A7:
    *(uint64_t *)(arg2 + 0x18) = 0;
loc_002616AC:
    result = *(uint8_t *)(arg2 + 0x24);
    if ((uint8_t)(*(uint8_t *)(arg2 + 0x24)) != 0) {
        Arg2 = (uint32_t)(*(uint8_t *)(arg2 + 0x24));
        Arg1 = Arg1;
        result = KeAbPostReleaseEx(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(arg1 + 0x10));
        *(uint8_t *)(arg2 + 0x24) = 0;
    }
    local_rsp = (local_rsp) + (96);
    return result;
loc_002616DB:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAC777))) != 0) goto loc_002615AE;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_p40, Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(arg1 + 0x10));
    goto loc_002615BF;
loc_002616FB:
    if ((*(uint32_t *)(arg1 + 0x38)) > 0) goto loc_002615E2;
    goto loc_002615E5;
loc_0026170B:
    *(uint64_t *)(arg1 + 0x10) = 0;
loc_0026170F:
    *(uint64_t *)(v_stack_p40 + 0x8) = v_stack_p40;
    *(uint64_t *)(v_stack_p40) = v_stack_p40;
    v_stack_pB0 = v_stack_p40;
loc_00261722:
    local_r15 = (uint32_t)((1) + (1));
    if (((*(uint8_t *)(v_rip + 0xD653DA)) & (1)) != 0) goto loc_00261781;
loc_0026172E:
    if (v_stack_p40 != 0) goto loc_00261760;
    if (v_stack_p40 == v_stack_p40) goto loc_0026179D;
    result = KxWaitForLockChainValid(v_stack_p40, Arg1, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(arg1 + 0x10));
loc_00261760:
    v_stack_p40 = 0;
    result = (uint8_t)((v_stack_p48) ^ ((uint8_t)(v_stack_p48)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0026179D;
    result = KeWakeAddressAll(result + 8, v_stack_p48, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(arg1 + 0x10));
    goto loc_0026179D;
loc_00261781:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAC6D1))) != 0) goto loc_0026172E;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_p40, v_stack_p98, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(arg1 + 0x10));
loc_0026179D:
    Arg1 = 3;
    if (*(uint64_t *)(v_stack_p40 + 0x10) == 0) { Arg1 = 1; }
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (2));
    if (*(uint64_t *)(v_stack_p40 + 0x10) == 0) { result = (uint32_t)(local_r15); }
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (4));
    if ((uint32_t)(result) == 0) { local_r14 = (uint32_t)(Arg1); }
    if (v_stack_pB0 != 0) goto loc_00261858;
loc_002617D0:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p10) + 0x8)) != v_stack_p10) goto loc_0026154B;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x8))) != v_stack_p10) goto loc_0026154B;
    *(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x8)) = *(uint64_t *)(v_stack_p10);
    *(uint64_t *)(*(uint64_t *)(v_stack_p10) + 0x8) = *(uint64_t *)(v_stack_p10 + 0x8);
    *(uint64_t *)(v_stack_p10) = 0;
    *(uint64_t *)(v_stack_p10 + 0x8) = 0;
    *(uint64_t *)(v_stack_p10 + 0x18) = 0;
    result = *(uint64_t *)(v_stack_p10 + 0x8);
    if ((*(uint32_t *)(v_rip + 0xD6551E)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(arg1 + 0x10));
    }
    goto loc_002616AC;
loc_0026181E:
loc_00261825:
    if ((*(uint32_t *)(v_rip + 0xD6551E)) != 0) goto loc_00261825;
    if ((*(uint32_t *)(v_rip + 0xD6551E)) >= 0) goto loc_002616A7;
    result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(arg1 + 0x10));
    goto loc_002616A7;
loc_00261846:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), 2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), *(uint64_t *)(arg1 + 0x10));
    goto loc_00261590;
loc_00261858:
    v_stack_p38 = (uint8_t)(v_cr8);
    if ((*(uint32_t *)(v_rip + 0xD654B5)) != 0) goto loc_002619EC;
loc_00261871:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (4));
    v_stack_pB8 = *(uint64_t *)(gs_base + (0 + 0x20));
    v_stack_pA0 = (uint32_t)(Arg1);
loc_00261897:
    v_stack_p30 = *(uint64_t *)(v_stack_pB0);
    if ((uint32_t)(Arg1) == 0) goto loc_002618D2;
    result = *(uint64_t *)(v_stack_pB0);
    if (*(uint64_t *)(v_stack_pB0 + 0x30) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(v_stack_pB0 + 0x30));
        Arg1 = *(uint64_t *)(v_stack_pB0 + 0x30);
        result = *(uint8_t *)(*(uint64_t *)(v_stack_pB0 + 0x30) + 0x8);
        result = (uint32_t)((result) & (63));
        Arg3 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8)) * (result);
        Arg1 = (Arg1) - (Arg3);
        Arg3 = 1;
        Arg1 = *(uint64_t *)(arg1 - 0x10);
        result = KiAbConvertWaiterToOwnerEntry(Arg1, *(uint64_t *)(v_stack_pB0 + 0x30), Arg3, *(uint64_t *)(arg1 + 0x10));
    }
    result = KiAcquireKobjectLockSafe(v_stack_pB0 + 24, *(uint64_t *)(v_stack_pB0 + 0x30), Arg3, *(uint64_t *)(arg1 + 0x10));
    local_rbp = (v_stack_pB0 + 24) + (8);
    *(uint32_t *)(v_stack_pB0 + 0x1C) = 1;
loc_002618EE:
    if ((*(uint64_t *)(local_rbp)) == local_rbp) goto loc_0026194A;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp)) + 0x8)) != (*(uint64_t *)(local_rbp))) goto loc_0026154B;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp) + 0x8))) != (*(uint64_t *)(local_rbp))) goto loc_0026154B;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp) + 0x8)) = *(uint64_t *)(*(uint64_t *)(local_rbp));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp)) + 0x8) = *(uint64_t *)(*(uint64_t *)(local_rbp) + 0x8);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_rbp) + 0x10))) != 1) goto loc_002619FD;
    Arg4 = 0;
    result = KiTryUnwaitThread(v_stack_pB8, *(uint64_t *)(local_rbp), *(uint16_t *)(*(uint64_t *)(local_rbp) + 0x12), Arg4);
    if ((uint8_t)(result) == 0) goto loc_002618EE;
loc_00261943:
    if ((uint8_t)(result) != 0) goto loc_002618EE;
loc_0026194A:
    if (v_stack_p30 != v_stack_pB0) goto loc_00261897;
    result = KiRemoveBoostThread(v_stack_pB8, *(uint64_t *)(v_stack_pB8 + 0x8), *(uint16_t *)(*(uint64_t *)(local_rbp) + 0x12), Arg4);
    Arg2 = 0;
    local_r14 = (uint32_t)((local_r14) >> (1));
    local_r14 = (uint32_t)((local_r14) & (1));
    v_stack_p20 = (uint8_t)(v_stack_p38);
    result = KiExitDispatcher(v_stack_pB8, Arg2, Arg2 + 1, (uint32_t)((uint32_t)(local_r14)));
    goto loc_002617D0;
loc_002619A7:
    result = KxWaitForLockOwnerShip(v_stack_p40, Arg2, Arg2 + 1, (uint32_t)((uint32_t)(local_r14)));
    goto loc_002615BF;
loc_002619B6:
    if ((*(uint32_t *)(arg1 + 0x38)) != 0) goto loc_00261A5A;
loc_002619BF:
    result = 0;
    v_stack_pB0 = 0;
    goto loc_00261722;
loc_002619CE:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38))) == 0) goto loc_0026161D;
    Arg1 = (v_stack_p40 + (uint32_t)(*(uint32_t *)(arg1 + 0x38)) * 4) ^ (Arg1);
    Arg1 = (Arg1) & (-4);
    Arg1 = (Arg1) ^ (Arg1);
    goto loc_0026161D;
loc_002619EC:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38))), (uint8_t)(v_stack_pB8), Arg2 + 1, (uint32_t)((uint32_t)(local_r14)));
    goto loc_00261871;
loc_002619FD:
    if (((uint8_t)((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38))))) != 2) goto loc_00261B5E;
    *(uint8_t *)(result + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(result + 0x18), result, Arg2 + 1, (uint32_t)((uint32_t)(local_r14)));
    goto loc_00261943;
loc_00261A1B:
    if (((uint8_t)(result)) >= 1) goto loc_00261A35;
    if (((*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x74)) & (0x400ULL)) != 0) goto loc_00261A35;
    if ((*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x1E4)) == 0) goto loc_00261496;
loc_00261A35:
    Arg4 = (*(uint64_t *)(arg2 + 0x1 + 0x10)) & (-2);
    if (Arg4 == (*(uint64_t *)(result + 0x18))) goto loc_00261A72;
    local_rdi = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(454, local_rdi + 9, Arg2 + 1, Arg4);
loc_00261A5A:
    *(uint64_t *)(arg1 + 0x8) = 0;
    v_stack_pB0 = *(uint64_t *)(arg1 + 0x8);
    *(uint32_t *)(arg1 + 0x38) = 0;
    goto loc_00261722;
loc_00261A72:
    if (((*(uint8_t *)(arg2 + 0x1 + 0x25)) & (2)) != 0) goto loc_00261A86;
    if ((*(uint64_t *)(arg2 + 0x1 + 0x18)) != Arg1) goto loc_00261BA5;
loc_00261A86:
    if ((((uint8_t)(local_rdi + 9)) & (1)) != 0) goto loc_00261B25;
    if ((((uint8_t)(local_rdi + 9)) & (1)) != 0) goto loc_002616C2;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x8)) != (Arg1 + 64)) goto loc_0026154B;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x40 + 0x8))) != (Arg1 + 64)) goto loc_0026154B;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x40 + 0x8)) = *(uint64_t *)(arg1 + 0x40);
    local_rdi = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x8) = *(uint64_t *)(arg1 + 0x40 + 0x8);
    *(uint64_t *)(arg1 + 0x40) = 0;
    *(uint64_t *)(arg1 + 0x40 + 0x8) = 0;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_00261B3D;
loc_00261AE1:
    *(uint64_t *)(arg1 + 0x40 + 0x10) = 0;
    *(uint8_t *)(arg1 + 0x40 + 0x24) = 0;
loc_00261AF0:
    if ((((uint8_t)(*(uint64_t *)(arg1))) & (2)) != 0) goto loc_00261B14;
    if ((((uint8_t)(*(uint64_t *)(arg1))) & (2)) != 0) goto loc_00261AF0;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x40 + 0x24)) == 0) goto loc_002616C2;
    result = KeAbPostReleaseEx(Arg1, *(uint8_t *)(arg1 + 0x40 + 0x24), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    goto loc_002616C2;
loc_00261B14:
    result = ExpReleaseFastResourceExclusiveSlow(Arg1, (uint8_t)(*(uint8_t *)(arg1 + 0x40 + 0x24)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    goto loc_002616C2;
loc_00261B25:
    local_rdi = 0;
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(454, local_rdi + 10, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
loc_00261B3D:
loc_00261B44:
    if (condition_is_not_equal) goto loc_00261B44;
    if (condition_is_above_or_equal) goto loc_00261AE1;
    result = KiRemoveSystemWorkPriorityKick(454, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    goto loc_00261AE1;
loc_00261B5E:
    if (454 == 4) goto loc_00261BC9;
    Arg4 = 0;
    result = KiTryUnwaitThread(v_stack_pB8, result, 256, Arg4);
    goto loc_002618EE;
loc_00261B81:
    if (result == 0) goto loc_002614EC;
    v_stack_p20 = result;
    result = KeBugCheckEx(454, 8, Arg1, Arg1 + 64);
loc_00261BA5:
    if (result == 0) goto loc_00261A86;
    v_stack_p20 = result;
    result = KeBugCheckEx(454, 8, Arg1, Arg1);
loc_00261BC9:
    *(uint8_t *)(result + 0x11) = 5;
    *(uint32_t *)(v_stack_pB0 + 0x1C) = 0;
    result = KeInsertQueueDpc(*(uint64_t *)(result + 0x18), v_stack_pB0 + 24, result, Arg1);
    goto loc_002618EE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x1A` | `16` | `R` |
| `Arg1` | `+ 0x24` | `8` | `R` |
| `Arg1` | `+ 0x25` | `8` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x38` | `32` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x60` | `32` | `R/W` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `R/W` |
| `Arg2` | `+ 0x25` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002613D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
