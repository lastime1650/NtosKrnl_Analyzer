# ExpAcquireFastResourceExclusiveSlow

- RVA: `0x003BE2E0`–`0x003BE75A` (길이 `1,146` bytes)
- VA: `0x00000001403BE2E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008DE08`
- 디코드: `306`개 명령, `1,146/1,146` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x003BE41A` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x003BE42F` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003BE44C` → [ExpWaitForFastResource](ExpWaitForFastResource_function_003BE760.md) (function, `0x003BE760`)
- `0x003BE4FB` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x003BE57D` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x003BE59E` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x003BE5AF` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003BE5ED` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x003BE60E` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x003BE62A` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x003BE638` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x003BE689` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003BE6C9` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x003BE6D3` → [KiAbEntryRemoveFromTree](../26/KiAbEntryRemoveFromTree_function_00262410.md) (function, `0x00262410`)
- `0x003BE6EA` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x003BE6F8` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x003BE72E` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x003BE740` → [KeAbMarkCrossThreadReleasable](KeAbMarkCrossThreadReleasable_function_003BE8AC.md) (function, `0x003BE8AC`)
- `0x003BE750` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)

### Direct callers
- [sub_00215166](../21/Unknown_function_00215166.md) at `0x002159CE`
- [sub_003BE10A](Unknown_function_003BE10A.md) at `0x003BE1CD`
- [ExAcquireFastResourceWithFlags](../65/ExAcquireFastResourceWithFlags_function_00658120.md) at `0x0065834C`

### Static image references
- `0x003BE33A` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003BE356` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x003BE404` → RVA `0x00F0DE58` (`.data`; read)
- `0x003BE545` → RVA `0x00FC6B06` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003BE2E0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003BE2E5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
003BE2EA  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
003BE2EF  55                              push rbp
003BE2F0  56                              push rsi
003BE2F1  57                              push rdi
003BE2F2  41 54                           push r12
003BE2F4  41 55                           push r13
003BE2F6  41 56                           push r14
003BE2F8  41 57                           push r15
003BE2FA  48 8B EC                        mov rbp, rsp
003BE2FD  48 83 EC 70                     sub rsp, 0x70
003BE301  0F 57 C0                        xorps xmm0, xmm0
003BE304  48 8D 51 40                     lea rdx, [rcx + 0x40]
003BE308  33 C0                           xor eax, eax
003BE30A  48 89 55 48                     mov qword ptr [rbp + 0x48], rdx
003BE30E  33 F6                           xor esi, esi
003BE310  48 89 45 F8                     mov qword ptr [rbp - 8], rax
003BE314  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
003BE318  49 8B D9                        mov rbx, r9
003BE31B  4D 8B F8                        mov r15, r8
003BE31E  48 8B F9                        mov rdi, rcx
003BE321  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
003BE325  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
003BE329  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
003BE32D  45 0F 20 C6                     mov r14, cr8
003BE331  B8 02 00 00 00                  mov eax, 2
003BE336  44 0F 22 C0                     mov cr8, rax
003BE33A  39 35 E0 89 C0 00               cmp dword ptr [rip + 0xc089e0], esi
003BE340  0F 85 62 02 00 00               jne 0x1403be5a8
003BE346  48 8D 4F 30                     lea rcx, [rdi + 0x30]
003BE34A  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
003BE34E  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
003BE352  41 B5 01                        mov r13b, 1
003BE355  90                              nop
003BE356  F6 05 A9 87 C0 00 21            test byte ptr [rip + 0xc087a9], 0x21
003BE35D  0F 85 83 01 00 00               jne 0x1403be4e6
003BE363  48 8D 55 B0                     lea rdx, [rbp - 0x50]
003BE367  48 87 11                        xchg qword ptr [rcx], rdx
003BE36A  48 85 D2                        test rdx, rdx
003BE36D  0F 85 C1 02 00 00               jne 0x1403be634
003BE373  0F 0D 0F                        prefetchw byte ptr [rdi]
003BE376  48 8B 07                        mov rax, qword ptr [rdi]
003BE379  41 BC 01 00 00 00               mov r12d, 1
003BE37F  48 85 C0                        test rax, rax
003BE382  74 77                           je 0x1403be3fb
003BE384  48 8B C8                        mov rcx, rax
003BE387  32 D2                           xor dl, dl
003BE389  48 83 C9 02                     or rcx, 2
003BE38D  48 3B C8                        cmp rcx, rax
003BE390  74 0F                           je 0x1403be3a1
003BE392  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
003BE397  75 E6                           jne 0x1403be37f
003BE399  84 D2                           test dl, dl
003BE39B  0F 85 18 02 00 00               jne 0x1403be5b9
003BE3A1  48 8D 45 E8                     lea rax, [rbp - 0x18]
003BE3A5  48 89 75 D0                     mov qword ptr [rbp - 0x30], rsi
003BE3A9  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
003BE3AD  48 8D 45 E8                     lea rax, [rbp - 0x18]
003BE3B1  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
003BE3B5  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003BE3B9  48 C7 45 E0 01 00 06 00         mov qword ptr [rbp - 0x20], 0x60001
003BE3C1  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
003BE3C5  48 89 5D F8                     mov qword ptr [rbp - 8], rbx
003BE3C9  48 85 C0                        test rax, rax
003BE3CC  0F 84 33 01 00 00               je 0x1403be505
003BE3D2  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
003BE3D6  48 39 01                        cmp qword ptr [rcx], rax
003BE3D9  0F 85 00 01 00 00               jne 0x1403be4df
003BE3DF  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
003BE3E3  48 8D 55 C8                     lea rdx, [rbp - 0x38]
003BE3E7  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
003BE3EB  48 89 11                        mov qword ptr [rcx], rdx
003BE3EE  48 8D 4D C8                     lea rcx, [rbp - 0x38]
003BE3F2  48 89 48 08                     mov qword ptr [rax + 8], rcx
003BE3F6  E9 22 01 00 00                  jmp 0x1403be51d
003BE3FB  49 8B CC                        mov rcx, r12
003BE3FE  41 0F B6 D4                     movzx edx, r12b
003BE402  EB 8E                           jmp 0x1403be392
003BE404  8B 05 4E FA B4 00               mov eax, dword ptr [rip + 0xb4fa4e]
003BE40A  85 C0                           test eax, eax
003BE40C  0F 85 40 01 00 00               jne 0x1403be552
003BE412  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
003BE416  48 8D 4D B0                     lea rcx, [rbp - 0x50]
003BE41A  E8 D1 95 E5 FF                  call 0x1402179f0
003BE41F  39 35 FB 88 C0 00               cmp dword ptr [rip + 0xc088fb], esi
003BE425  74 0D                           je 0x1403be434
003BE427  44 0F 20 C1                     mov rcx, cr8
003BE42B  41 0F B6 D6                     movzx edx, r14b
003BE42F  E8 64 72 13 00                  call 0x1404f5698
003BE434  41 0F B6 C6                     movzx eax, r14b
003BE438  44 0F 22 C0                     mov cr8, rax
003BE43C  41 B8 24 02 01 00               mov r8d, 0x10224
003BE442  48 8D 55 C8                     lea rdx, [rbp - 0x38]
003BE446  48 8B CF                        mov rcx, rdi
003BE449  45 32 ED                        xor r13b, r13b
003BE44C  E8 0F 03 00 00                  call 0x1403be760
003BE451  48 85 DB                        test rbx, rbx
003BE454  0F 85 ED 02 00 00               jne 0x1403be747
003BE45A  F6 45 60 10                     test byte ptr [rbp + 0x60], 0x10
003BE45E  B8 0D 00 00 00                  mov eax, 0xd
003BE463  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
003BE467  41 0F 44 C4                     cmove eax, r12d
003BE46B  44 8B E0                        mov r12d, eax
003BE46E  41 83 CC 02                     or r12d, 2
003BE472  45 84 ED                        test r13b, r13b
003BE475  C7 42 20 01 00 00 00            mov dword ptr [rdx + 0x20], 1
003BE47C  44 0F 45 E0                     cmovne r12d, eax
003BE480  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
003BE484  45 8B FC                        mov r15d, r12d
003BE487  41 8B FC                        mov edi, r12d
003BE48A  41 C0 EC 03                     shr r12b, 3
003BE48E  41 83 E7 02                     and r15d, 2
003BE492  41 80 E4 01                     and r12b, 1
003BE496  83 E7 04                        and edi, 4
003BE499  40 0F 95 C6                     setne sil
003BE49D  48 0B F0                        or rsi, rax
003BE4A0  48 89 72 10                     mov qword ptr [rdx + 0x10], rsi
003BE4A4  48 85 DB                        test rbx, rbx
003BE4A7  74 15                           je 0x1403be4be
003BE4A9  0F B6 43 08                     movzx eax, byte ptr [rbx + 8]
003BE4AD  24 3F                           and al, 0x3f
003BE4AF  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
003BE4B3  02 C0                           add al, al
003BE4B5  0C 01                           or al, 1
003BE4B7  88 42 24                        mov byte ptr [rdx + 0x24], al
003BE4BA  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
003BE4BE  45 85 FF                        test r15d, r15d
003BE4C1  74 01                           je 0x1403be4c4
003BE4C3  FA                              cli
003BE4C4  85 FF                           test edi, edi
003BE4C6  0F 85 25 02 00 00               jne 0x1403be6f1
003BE4CC  48 05 B8 06 00 00               add rax, 0x6b8
003BE4D2  48 8B 08                        mov rcx, qword ptr [rax]
003BE4D5  48 39 41 08                     cmp qword ptr [rcx + 8], rax
003BE4D9  0F 84 63 01 00 00               je 0x1403be642
003BE4DF  B9 03 00 00 00                  mov ecx, 3
003BE4E4  CD 29                           int 0x29
003BE4E6  8B 05 6C F9 B4 00               mov eax, dword ptr [rip + 0xb4f96c]
003BE4EC  85 C0                           test eax, eax
003BE4EE  0F 85 6F FE FF FF               jne 0x1403be363
003BE4F4  48 8B D1                        mov rdx, rcx
003BE4F7  48 8D 4D B0                     lea rcx, [rbp - 0x50]
003BE4FB  E8 50 73 EB FF                  call 0x140275850
003BE500  E9 6E FE FF FF                  jmp 0x1403be373
003BE505  48 8D 45 C8                     lea rax, [rbp - 0x38]
003BE509  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
003BE50D  48 8D 45 C8                     lea rax, [rbp - 0x38]
003BE511  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
003BE515  48 8D 45 C8                     lea rax, [rbp - 0x38]
003BE519  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
003BE51D  48 85 DB                        test rbx, rbx
003BE520  74 23                           je 0x1403be545
003BE522  0F B6 03                        movzx eax, byte ptr [rbx]
003BE525  0C 02                           or al, 2
003BE527  88 03                           mov byte ptr [rbx], al
003BE529  90                              nop
003BE52A  48 8B 03                        mov rax, qword ptr [rbx]
003BE52D  48 C1 E8 3F                     shr rax, 0x3f
003BE531  84 C0                           test al, al
003BE533  0F 85 97 01 00 00               jne 0x1403be6d0
003BE539  44 88 63 09                     mov byte ptr [rbx + 9], r12b
003BE53D  90                              nop
003BE53E  0F B6 03                        movzx eax, byte ptr [rbx]
003BE541  24 FD                           and al, 0xfd
003BE543  88 03                           mov byte ptr [rbx], al
003BE545  44 84 25 BA 85 C0 00            test byte ptr [rip + 0xc085ba], r12b
003BE54C  0F 85 B2 FE FF FF               jne 0x1403be404
003BE552  0F 0D 4D B0                     prefetchw byte ptr [rbp - 0x50]
003BE556  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
003BE55A  48 85 C0                        test rax, rax
003BE55D  75 23                           jne 0x1403be582
003BE55F  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
003BE563  48 8D 45 B0                     lea rax, [rbp - 0x50]
003BE567  F0 48 0F B1 31                  lock cmpxchg qword ptr [rcx], rsi
003BE56C  48 8D 4D B0                     lea rcx, [rbp - 0x50]
003BE570  48 3B C1                        cmp rax, rcx
003BE573  0F 84 A6 FE FF FF               je 0x1403be41f
003BE579  48 8D 4D B0                     lea rcx, [rbp - 0x50]
003BE57D  E8 1E 95 E5 FF                  call 0x140217aa0
003BE582  48 8D 48 08                     lea rcx, [rax + 8]
003BE586  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
003BE58A  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
003BE58E  48 8B C2                        mov rax, rdx
003BE591  48 87 01                        xchg qword ptr [rcx], rax
003BE594  32 C2                           xor al, dl
003BE596  A8 04                           test al, 4
003BE598  0F 84 81 FE FF FF               je 0x1403be41f
003BE59E  E8 7D 96 E5 FF                  call 0x140217c20
003BE5A3  E9 77 FE FF FF                  jmp 0x1403be41f
003BE5A8  0F B6 D0                        movzx edx, al
003BE5AB  41 0F B6 CE                     movzx ecx, r14b
003BE5AF  E8 48 71 13 00                  call 0x1404f56fc
003BE5B4  E9 8D FD FF FF                  jmp 0x1403be346
003BE5B9  44 84 25 46 85 C0 00            test byte ptr [rip + 0xc08546], r12b
003BE5C0  75 56                           jne 0x1403be618
003BE5C2  0F 0D 4D B0                     prefetchw byte ptr [rbp - 0x50]
003BE5C6  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
003BE5CA  48 85 C0                        test rax, rax
003BE5CD  75 23                           jne 0x1403be5f2
003BE5CF  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
003BE5D3  48 8D 45 B0                     lea rax, [rbp - 0x50]
003BE5D7  F0 48 0F B1 31                  lock cmpxchg qword ptr [rcx], rsi
003BE5DC  48 8D 4D B0                     lea rcx, [rbp - 0x50]
003BE5E0  48 3B C1                        cmp rax, rcx
003BE5E3  0F 84 71 FE FF FF               je 0x1403be45a
003BE5E9  48 8D 4D B0                     lea rcx, [rbp - 0x50]
003BE5ED  E8 AE 94 E5 FF                  call 0x140217aa0
003BE5F2  48 8D 48 08                     lea rcx, [rax + 8]
003BE5F6  48 89 75 B0                     mov qword ptr [rbp - 0x50], rsi
003BE5FA  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
003BE5FE  48 8B C2                        mov rax, rdx
003BE601  48 87 01                        xchg qword ptr [rcx], rax
003BE604  32 C2                           xor al, dl
003BE606  A8 04                           test al, 4
003BE608  0F 84 4C FE FF FF               je 0x1403be45a
003BE60E  E8 0D 96 E5 FF                  call 0x140217c20
003BE613  E9 42 FE FF FF                  jmp 0x1403be45a
003BE618  8B 05 3A F8 B4 00               mov eax, dword ptr [rip + 0xb4f83a]
003BE61E  85 C0                           test eax, eax
003BE620  75 A0                           jne 0x1403be5c2
003BE622  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
003BE626  48 8D 4D B0                     lea rcx, [rbp - 0x50]
003BE62A  E8 C1 93 E5 FF                  call 0x1402179f0
003BE62F  E9 26 FE FF FF                  jmp 0x1403be45a
003BE634  48 8D 4D B0                     lea rcx, [rbp - 0x50]
003BE638  E8 73 98 E9 FF                  call 0x140257eb0
003BE63D  E9 31 FD FF FF                  jmp 0x1403be373
003BE642  48 8B 75 50                     mov rsi, qword ptr [rbp + 0x50]
003BE646  48 89 0A                        mov qword ptr [rdx], rcx
003BE649  48 89 42 08                     mov qword ptr [rdx + 8], rax
003BE64D  48 89 51 08                     mov qword ptr [rcx + 8], rdx
003BE651  48 89 10                        mov qword ptr [rax], rdx
003BE654  45 85 FF                        test r15d, r15d
003BE657  74 16                           je 0x1403be66f
003BE659  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003BE662  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
003BE669  4D 85 C0                        test r8, r8
003BE66C  75 41                           jne 0x1403be6af
003BE66E  FB                              sti
003BE66F  85 FF                           test edi, edi
003BE671  75 6A                           jne 0x1403be6dd
003BE673  45 84 ED                        test r13b, r13b
003BE676  74 1E                           je 0x1403be696
003BE678  83 3D A1 86 C0 00 00            cmp dword ptr [rip + 0xc086a1], 0
003BE67F  74 0D                           je 0x1403be68e
003BE681  44 0F 20 C1                     mov rcx, cr8
003BE685  41 0F B6 D6                     movzx edx, r14b
003BE689  E8 0A 70 13 00                  call 0x1404f5698
003BE68E  41 0F B6 C6                     movzx eax, r14b
003BE692  44 0F 22 C0                     mov cr8, rax
003BE696  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
003BE69E  48 83 C4 70                     add rsp, 0x70
003BE6A2  41 5F                           pop r15
003BE6A4  41 5E                           pop r14
003BE6A6  41 5D                           pop r13
003BE6A8  41 5C                           pop r12
003BE6AA  5F                              pop rdi
003BE6AB  5E                              pop rsi
003BE6AC  5D                              pop rbp
003BE6AD  C3                              ret
003BE6AE  CC                              int3
003BE6AF  41 0F 0D 08                     prefetchw byte ptr [r8]
003BE6B3  41 8B 00                        mov eax, dword ptr [r8]
003BE6B6  8B D0                           mov edx, eax
003BE6B8  0F BA F2 15                     btr edx, 0x15
003BE6BC  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
003BE6C1  75 F3                           jne 0x1403be6b6
003BE6C3  0F BA E0 15                     bt eax, 0x15
003BE6C7  73 A5                           jae 0x1403be66e
003BE6C9  E8 02 4B EA FF                  call 0x1402631d0
003BE6CE  EB 9E                           jmp 0x1403be66e
003BE6D0  48 8B CB                        mov rcx, rbx
003BE6D3  E8 38 3D EA FF                  call 0x140262410
003BE6D8  E9 5C FE FF FF                  jmp 0x1403be539
003BE6DD  45 84 E4                        test r12b, r12b
003BE6E0  75 56                           jne 0x1403be738
003BE6E2  BA 44 66 6C 74                  mov edx, 0x746c6644
003BE6E7  48 8B CE                        mov rcx, rsi
003BE6EA  E8 21 20 E5 FF                  call 0x140210710
003BE6EF  EB 82                           jmp 0x1403be673
003BE6F1  48 8D 88 C8 06 00 00            lea rcx, [rax + 0x6c8]
003BE6F8  E8 33 9D E4 FF                  call 0x140208430
003BE6FD  48 8B 75 50                     mov rsi, qword ptr [rbp + 0x50]
003BE701  48 8D 86 D0 06 00 00            lea rax, [rsi + 0x6d0]
003BE708  48 8B 08                        mov rcx, qword ptr [rax]
003BE70B  48 39 41 08                     cmp qword ptr [rcx + 8], rax
003BE70F  0F 85 CA FD FF FF               jne 0x1403be4df
003BE715  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
003BE719  48 89 0A                        mov qword ptr [rdx], rcx
003BE71C  48 89 42 08                     mov qword ptr [rdx + 8], rax
003BE720  48 89 51 08                     mov qword ptr [rcx + 8], rdx
003BE724  48 8D 8E C8 06 00 00            lea rcx, [rsi + 0x6c8]
003BE72B  48 89 10                        mov qword ptr [rax], rdx
003BE72E  E8 3D 7F E4 FF                  call 0x140206670
003BE733  E9 1C FF FF FF                  jmp 0x1403be654
003BE738  48 85 DB                        test rbx, rbx
003BE73B  74 A5                           je 0x1403be6e2
003BE73D  48 8B D3                        mov rdx, rbx
003BE740  E8 67 01 00 00                  call 0x1403be8ac
003BE745  EB 9B                           jmp 0x1403be6e2
003BE747  45 33 C0                        xor r8d, r8d
003BE74A  48 8B D3                        mov rdx, rbx
003BE74D  48 8B CF                        mov rcx, rdi
003BE750  E8 DB 1A E5 FF                  call 0x140210230
003BE755  E9 00 FD FF FF                  jmp 0x1403be45a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpAcquireFastResourceExclusiveSlow(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
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
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_p10 = a1 + 64;
    v_rsi = 0;
    v_stack_m40 = 0;
    v_stack_m78 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if ((*(unsigned int *)(v_rip + 12618208)) != 0) goto loc_003BE5A8;
loc_003BE346:
    v_stack_m88 = 0;
    v_stack_m80 = a1 + 48;
    if (((*(unsigned __int8 *)(v_rip + 12617641)) & (33)) != 0) goto loc_003BE4E6;
loc_003BE363:
    if (v_stack_m88 != 0) goto loc_003BE634;
loc_003BE373:
loc_003BE37F:
    if (*(unsigned __int64 *)(a1) == 0) goto loc_003BE3FB;
    a2 = 0;
    a1 = (*(unsigned __int64 *)(a1)) | (2);
    if (a1 == (*(unsigned __int64 *)(a1))) goto loc_003BE3A1;
loc_003BE392:
    if (a1 != (*(unsigned __int64 *)(a1))) goto loc_003BE37F;
    if (0 != 0) goto loc_003BE5B9;
loc_003BE3A1:
    v_stack_m68 = 0;
    v_stack_m48 = v_stack_m50;
    v_stack_m50 = v_stack_m50;
    v_stack_m58 = 0x60001ULL;
    v_stack_m60 = a3;
    v_stack_m40 = a4;
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_003BE505;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8))) != (*(unsigned __int64 *)(a1 + 16))) goto loc_003BE4DF;
    v_stack_m68 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8);
    v_stack_m70 = *(unsigned __int64 *)(a1 + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8)) = v_stack_m70;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) = v_stack_m70;
    goto loc_003BE51D;
loc_003BE3FB:
    goto loc_003BE392;
loc_003BE404:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11860558))) != 0) goto loc_003BE552;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m88, v_stack_p0, a3, a4);
loc_003BE41F:
    if ((*(unsigned int *)(v_rip + 12617979)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_r13 = 0;
    result = ExpWaitForFastResource(a1, v_stack_m70, (unsigned int)(0x10224ULL), a4);
    if (a4 != 0) goto loc_003BE747;
loc_003BE45A:
    result = 13;
    if (((a5) & (16)) == 0) { result = 1; }
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(result))) | (2));
    *(unsigned int *)(v_stack_p10 + 32) = 1;
    if (0 != 0) { v_r12 = (unsigned int)(result); }
    v_r12 = (unsigned __int8)((v_r12) >> (3));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (2));
    v_r12 = (unsigned __int8)((v_r12) & (1));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (4));
    v_rsi = (condition_is_not_equal) ? 1 : 0;
    v_rsi = (v_rsi) | (v_stack_p18);
    *(unsigned __int64 *)(v_stack_p10 + 16) = v_rsi;
    result = v_stack_p18;
    if (a4 != 0) {
        result = *(unsigned __int8 *)(a4 + 8);
        result = (unsigned __int8)((result) & (63));
        *(unsigned __int8 *)(a4 + 10) = 1;
        result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
        result = (unsigned __int8)((result) | (1));
        *(unsigned __int8 *)(v_stack_p10 + 36) = (unsigned __int8)(result);
        result = v_stack_p18;
    }
    if ((unsigned int)(v_r15) != 0) {
    }
    if ((unsigned int)(v_rdi) != 0) goto loc_003BE6F1;
    result = (result) + (0x6B8ULL);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) == result) goto loc_003BE642;
loc_003BE4DF:
loc_003BE4E6:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11860332))) != 0) goto loc_003BE363;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m88, 3, (unsigned int)(0x10224ULL), a4);
    goto loc_003BE373;
loc_003BE505:
    v_stack_m68 = v_stack_m70;
    v_stack_m70 = v_stack_m70;
    *(unsigned __int64 *)(v_rdi + 16) = v_stack_m70;
loc_003BE51D:
    if (a4 == 0) goto loc_003BE545;
    result = (unsigned __int8)((*(unsigned __int8 *)(a4)) | (2));
    *(unsigned __int8 *)(a4) = (unsigned __int8)(result);
    result = (*(unsigned __int64 *)(a4)) >> (63);
    if ((unsigned __int8)(result) != 0) goto loc_003BE6D0;
loc_003BE539:
    *(unsigned __int8 *)(a4 + 9) = (unsigned __int8)(v_r12);
    result = (unsigned __int8)((*(unsigned __int8 *)(a4)) & (253));
    *(unsigned __int8 *)(a4) = (unsigned __int8)(result);
loc_003BE545:
    if (((*(unsigned __int8 *)(v_rip + 12617146)) & ((unsigned __int8)(v_r12))) != 0) goto loc_003BE404;
loc_003BE552:
    if (v_stack_m88 != 0) goto loc_003BE582;
    if (v_stack_m88 == v_stack_m88) goto loc_003BE41F;
    result = KxWaitForLockChainValid(v_stack_m88, 3, (unsigned int)(0x10224ULL), a4);
loc_003BE582:
    v_stack_m88 = v_rsi;
    result = (unsigned __int8)((v_stack_m80) ^ ((unsigned __int8)(v_stack_m80)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_003BE41F;
    result = KeWakeAddressAll(result + 8, v_stack_m80, (unsigned int)(0x10224ULL), a4);
    goto loc_003BE41F;
loc_003BE5A8:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), (unsigned __int8)(result), (unsigned int)(0x10224ULL), a4);
    goto loc_003BE346;
loc_003BE5B9:
    if (((*(unsigned __int8 *)(v_rip + 12617030)) & ((unsigned __int8)(v_r12))) != 0) goto loc_003BE618;
loc_003BE5C2:
    if (v_stack_m88 != 0) goto loc_003BE5F2;
    if (v_stack_m88 == v_stack_m88) goto loc_003BE45A;
    result = KxWaitForLockChainValid(v_stack_m88, (unsigned __int8)(result), (unsigned int)(0x10224ULL), a4);
loc_003BE5F2:
    v_stack_m88 = v_rsi;
    result = (unsigned __int8)((v_stack_m80) ^ ((unsigned __int8)(v_stack_m80)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_003BE45A;
    result = KeWakeAddressAll(result + 8, v_stack_m80, (unsigned int)(0x10224ULL), a4);
    goto loc_003BE45A;
loc_003BE618:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11860026))) != 0) goto loc_003BE5C2;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m88, v_stack_p0, (unsigned int)(0x10224ULL), a4);
    goto loc_003BE45A;
loc_003BE634:
    result = KxWaitForLockOwnerShip(v_stack_m88, v_stack_p0, (unsigned int)(0x10224ULL), a4);
    goto loc_003BE373;
loc_003BE642:
    *(unsigned __int64 *)(v_stack_p0) = v_stack_m88;
    *(unsigned __int64 *)(v_stack_p0 + 8) = result;
    *(unsigned __int64 *)(v_stack_m88 + 8) = v_stack_p0;
    *(unsigned __int64 *)(result) = v_stack_p0;
loc_003BE654:
    if ((unsigned int)(v_r15) == 0) goto loc_003BE66F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_003BE6AF;
loc_003BE66E:
loc_003BE66F:
    if ((unsigned int)(v_rdi) != 0) goto loc_003BE6DD;
loc_003BE673:
    if (0 == 0) goto loc_003BE696;
    if ((*(unsigned int *)(v_rip + 12617377)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    }
loc_003BE696:
    v_rsp = (v_rsp) + (112);
    return (unsigned __int8)(v_cr8);
loc_003BE6AF:
loc_003BE6B6:
    if (condition_is_not_equal) goto loc_003BE6B6;
    if (condition_is_above_or_equal) goto loc_003BE66E;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_003BE66E;
loc_003BE6D0:
    result = KiAbEntryRemoveFromTree(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536))))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_003BE539;
loc_003BE6DD:
    if ((unsigned __int8)(v_r12) != 0) goto loc_003BE738;
loc_003BE6E2:
    result = ObfReferenceObjectWithTag(v_stack_p18, (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_003BE673;
loc_003BE6F1:
    result = KeAcquireSpinLockAtDpcLevel(result + 1736, (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 1744) + 8)) != (v_stack_p18 + 1744)) goto loc_003BE4DF;
    *(unsigned __int64 *)(v_stack_p10) = *(unsigned __int64 *)(v_stack_p18 + 1744);
    *(unsigned __int64 *)(v_stack_p10 + 8) = v_stack_p18 + 1744;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18 + 1744) + 8) = v_stack_p10;
    *(unsigned __int64 *)(v_stack_p18 + 1744) = v_stack_p10;
    result = KxReleaseSpinLock(v_stack_p18 + 1736, v_stack_p10, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_003BE654;
loc_003BE738:
    if (v_stack_p8 == 0) goto loc_003BE6E2;
    result = KeAbMarkCrossThreadReleasable(v_stack_p18 + 1736, v_stack_p8, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_003BE6E2;
loc_003BE747:
    a3 = 0;
    result = KeAbPreAcquire(v_rdi, v_stack_p8, a3, a4);
    goto loc_003BE45A;
}
```

## 5. (Beta) C Style

```c
int64_t ExpAcquireFastResourceExclusiveSlow(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
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
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_p10 = Arg1 + 64;
    local_rsi = 0;
    v_stack_m40 = 0;
    v_stack_m78 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if ((*(uint32_t *)(v_rip + 0xC089E0)) != 0) goto loc_003BE5A8;
loc_003BE346:
    v_stack_m88 = 0;
    v_stack_m80 = Arg1 + 48;
    if (((*(uint8_t *)(v_rip + 0xC087A9)) & (33)) != 0) goto loc_003BE4E6;
loc_003BE363:
    if (v_stack_m88 != 0) goto loc_003BE634;
loc_003BE373:
loc_003BE37F:
    if (*(uint64_t *)(arg1) == 0) goto loc_003BE3FB;
    Arg2 = 0;
    Arg1 = (*(uint64_t *)(arg1)) | (2);
    if (Arg1 == (*(uint64_t *)(arg1))) goto loc_003BE3A1;
loc_003BE392:
    if (Arg1 != (*(uint64_t *)(arg1))) goto loc_003BE37F;
    if (0 != 0) goto loc_003BE5B9;
loc_003BE3A1:
    v_stack_m68 = 0;
    v_stack_m48 = v_stack_m50;
    v_stack_m50 = v_stack_m50;
    v_stack_m58 = 0x60001ULL;
    v_stack_m60 = Arg3;
    v_stack_m40 = Arg4;
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_003BE505;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8))) != (*(uint64_t *)(arg1 + 0x10))) goto loc_003BE4DF;
    v_stack_m68 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8);
    v_stack_m70 = *(uint64_t *)(arg1 + 0x10);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8)) = v_stack_m70;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) = v_stack_m70;
    goto loc_003BE51D;
loc_003BE3FB:
    goto loc_003BE392;
loc_003BE404:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB4FA4E))) != 0) goto loc_003BE552;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m88, v_stack_p0, Arg3, Arg4);
loc_003BE41F:
    if ((*(uint32_t *)(v_rip + 0xC088FB)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    local_r13 = 0;
    result = ExpWaitForFastResource(Arg1, v_stack_m70, (uint32_t)(0x10224ULL), Arg4);
    if (Arg4 != 0) goto loc_003BE747;
loc_003BE45A:
    result = 13;
    if (((Arg5) & (16)) == 0) { result = 1; }
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(result))) | (2));
    *(uint32_t *)(v_stack_p10 + 0x20) = 1;
    if (0 != 0) { local_r12 = (uint32_t)(result); }
    local_r12 = (uint8_t)((local_r12) >> (3));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (2));
    local_r12 = (uint8_t)((local_r12) & (1));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (4));
    local_rsi = (condition_is_not_equal) ? 1 : 0;
    local_rsi = (local_rsi) | (v_stack_p18);
    *(uint64_t *)(v_stack_p10 + 0x10) = local_rsi;
    result = v_stack_p18;
    if (Arg4 != 0) {
        result = *(uint8_t *)(Arg4 + 0x8);
        result = (uint8_t)((result) & (63));
        *(uint8_t *)(Arg4 + 0xA) = 1;
        result = (uint8_t)((result) + ((uint8_t)(result)));
        result = (uint8_t)((result) | (1));
        *(uint8_t *)(v_stack_p10 + 0x24) = (uint8_t)(result);
        result = v_stack_p18;
    }
    if ((uint32_t)(local_r15) != 0) {
    }
    if ((uint32_t)(local_rdi) != 0) goto loc_003BE6F1;
    result = (result) + (0x6B8ULL);
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) == result) goto loc_003BE642;
loc_003BE4DF:
loc_003BE4E6:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB4F96C))) != 0) goto loc_003BE363;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m88, 3, (uint32_t)(0x10224ULL), Arg4);
    goto loc_003BE373;
loc_003BE505:
    v_stack_m68 = v_stack_m70;
    v_stack_m70 = v_stack_m70;
    *(uint64_t *)(local_rdi + 0x10) = v_stack_m70;
loc_003BE51D:
    if (Arg4 == 0) goto loc_003BE545;
    result = (uint8_t)((*(uint8_t *)(Arg4)) | (2));
    *(uint8_t *)(Arg4) = (uint8_t)(result);
    result = (*(uint64_t *)(Arg4)) >> (63);
    if ((uint8_t)(result) != 0) goto loc_003BE6D0;
loc_003BE539:
    *(uint8_t *)(Arg4 + 0x9) = (uint8_t)(local_r12);
    result = (uint8_t)((*(uint8_t *)(Arg4)) & (253));
    *(uint8_t *)(Arg4) = (uint8_t)(result);
loc_003BE545:
    if (((*(uint8_t *)(v_rip + 0xC085BA)) & ((uint8_t)(local_r12))) != 0) goto loc_003BE404;
loc_003BE552:
    if (v_stack_m88 != 0) goto loc_003BE582;
    if (v_stack_m88 == v_stack_m88) goto loc_003BE41F;
    result = KxWaitForLockChainValid(v_stack_m88, 3, (uint32_t)(0x10224ULL), Arg4);
loc_003BE582:
    v_stack_m88 = local_rsi;
    result = (uint8_t)((v_stack_m80) ^ ((uint8_t)(v_stack_m80)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_003BE41F;
    result = KeWakeAddressAll(result + 8, v_stack_m80, (uint32_t)(0x10224ULL), Arg4);
    goto loc_003BE41F;
loc_003BE5A8:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), (uint8_t)(result), (uint32_t)(0x10224ULL), Arg4);
    goto loc_003BE346;
loc_003BE5B9:
    if (((*(uint8_t *)(v_rip + 0xC08546)) & ((uint8_t)(local_r12))) != 0) goto loc_003BE618;
loc_003BE5C2:
    if (v_stack_m88 != 0) goto loc_003BE5F2;
    if (v_stack_m88 == v_stack_m88) goto loc_003BE45A;
    result = KxWaitForLockChainValid(v_stack_m88, (uint8_t)(result), (uint32_t)(0x10224ULL), Arg4);
loc_003BE5F2:
    v_stack_m88 = local_rsi;
    result = (uint8_t)((v_stack_m80) ^ ((uint8_t)(v_stack_m80)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_003BE45A;
    result = KeWakeAddressAll(result + 8, v_stack_m80, (uint32_t)(0x10224ULL), Arg4);
    goto loc_003BE45A;
loc_003BE618:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB4F83A))) != 0) goto loc_003BE5C2;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m88, v_stack_p0, (uint32_t)(0x10224ULL), Arg4);
    goto loc_003BE45A;
loc_003BE634:
    result = KxWaitForLockOwnerShip(v_stack_m88, v_stack_p0, (uint32_t)(0x10224ULL), Arg4);
    goto loc_003BE373;
loc_003BE642:
    *(uint64_t *)(v_stack_p0) = v_stack_m88;
    *(uint64_t *)(v_stack_p0 + 0x8) = result;
    *(uint64_t *)(v_stack_m88 + 0x8) = v_stack_p0;
    *(uint64_t *)(result) = v_stack_p0;
loc_003BE654:
    if ((uint32_t)(local_r15) == 0) goto loc_003BE66F;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_003BE6AF;
loc_003BE66E:
loc_003BE66F:
    if ((uint32_t)(local_rdi) != 0) goto loc_003BE6DD;
loc_003BE673:
    if (0 == 0) goto loc_003BE696;
    if ((*(uint32_t *)(v_rip + 0xC086A1)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    }
loc_003BE696:
    local_rsp = (local_rsp) + (112);
    return (uint8_t)(v_cr8);
loc_003BE6AF:
loc_003BE6B6:
    if (condition_is_not_equal) goto loc_003BE6B6;
    if (condition_is_above_or_equal) goto loc_003BE66E;
    result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    goto loc_003BE66E;
loc_003BE6D0:
    result = KiAbEntryRemoveFromTree(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8))))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    goto loc_003BE539;
loc_003BE6DD:
    if ((uint8_t)(local_r12) != 0) goto loc_003BE738;
loc_003BE6E2:
    result = ObfReferenceObjectWithTag(v_stack_p18, (uint32_t)(0x746C6644ULL), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    goto loc_003BE673;
loc_003BE6F1:
    result = KeAcquireSpinLockAtDpcLevel(result + 1736, (uint32_t)(0x746C6644ULL), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x6D0) + 0x8)) != (v_stack_p18 + 1744)) goto loc_003BE4DF;
    *(uint64_t *)(v_stack_p10) = *(uint64_t *)(v_stack_p18 + 0x6D0);
    *(uint64_t *)(v_stack_p10 + 0x8) = v_stack_p18 + 1744;
    *(uint64_t *)(*(uint64_t *)(v_stack_p18 + 0x6D0) + 0x8) = v_stack_p10;
    *(uint64_t *)(v_stack_p18 + 0x6D0) = v_stack_p10;
    result = KxReleaseSpinLock(v_stack_p18 + 1736, v_stack_p10, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    goto loc_003BE654;
loc_003BE738:
    if (v_stack_p8 == 0) goto loc_003BE6E2;
    result = KeAbMarkCrossThreadReleasable(v_stack_p18 + 1736, v_stack_p8, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    goto loc_003BE6E2;
loc_003BE747:
    Arg3 = 0;
    result = KeAbPreAcquire(local_rdi, v_stack_p8, Arg3, Arg4);
    goto loc_003BE45A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003BE2E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
