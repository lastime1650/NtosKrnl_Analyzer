# IopCheckVpbMounted

- RVA: `0x00270540`–`0x0027095B` (길이 `1,051` bytes)
- VA: `0x0000000140270540`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065A40`
- 디코드: `265`개 명령, `1,051/1,051` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00270614` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x00270630` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x00270649` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0027065F` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002706FC` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x00270712` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0027075C` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x00270778` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0027078D` → [KiAcquireQueuedSpinLockInstrumented](KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x002707A5` → [KiAcquireQueuedSpinLockInstrumented](KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x002707CB` → [IopCompleteUnloadOrDelete](IopCompleteUnloadOrDelete_function_00270BC8.md) (function, `0x00270BC8`)
- `0x002707DD` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002707EF` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002707FC` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00270809` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0027081C` → [KeReleaseQueuedSpinLock](KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x0027084A` → [IopMountVolume](../../page/A3/IopMountVolume_function_00A329D0.md) (function, `0x00A329D0`)
- `0x00270875` → [KeAcquireQueuedSpinLock](KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x00270894` → [IopDecrementDeviceObjectRef](IopDecrementDeviceObjectRef_function_00270970.md) (function, `0x00270970`)
- `0x002708CD` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x002708E4` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x002708F9` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00270914` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00270928` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00270939` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00270955` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x0089E900`

### Static image references
- `0x00270576` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00270597` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00270637` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0027084A` → [IopMountVolume](../../page/A3/IopMountVolume_function_00A329D0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00270540  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00270545  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
0027054A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0027054F  57                              push rdi
00270550  41 54                           push r12
00270552  41 55                           push r13
00270554  41 56                           push r14
00270556  41 57                           push r15
00270558  48 83 EC 30                     sub rsp, 0x30
0027055C  4D 8B F9                        mov r15, r9
0027055F  4D 8B F0                        mov r14, r8
00270562  48 8B EA                        mov rbp, rdx
00270565  48 8B D9                        mov rbx, rcx
00270568  44 0F 20 C6                     mov rsi, cr8
0027056C  41 BC 02 00 00 00               mov r12d, 2
00270572  45 0F 22 C4                     mov cr8, r12
00270576  83 3D A3 67 D5 00 00            cmp dword ptr [rip + 0xd567a3], 0
0027057D  0F 85 52 02 00 00               jne 0x1402707d5
00270583  65 48 8B 0C 25 28 00 00 00      mov rcx, qword ptr gs:[0x28]
0027058C  48 81 C1 90 00 00 00            add rcx, 0x90
00270593  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00270597  F6 05 68 65 D5 00 21            test byte ptr [rip + 0xd56568], 0x21
0027059E  0F 85 DB 01 00 00               jne 0x14027077f
002705A4  48 8B C1                        mov rax, rcx
002705A7  48 87 02                        xchg qword ptr [rdx], rax
002705AA  48 85 C0                        test rax, rax
002705AD  0F 85 46 02 00 00               jne 0x1402707f9
002705B3  45 33 ED                        xor r13d, r13d
002705B6  48 8B 7D 38                     mov rdi, qword ptr [rbp + 0x38]
002705BA  0F B7 47 04                     movzx eax, word ptr [rdi + 4]
002705BE  A8 01                           test al, 1
002705C0  0F 84 4D 02 00 00               je 0x140270813
002705C6  41 84 C4                        test r12b, al
002705C9  0F 85 E1 02 00 00               jne 0x1402708b0
002705CF  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
002705D2  FF C0                           inc eax
002705D4  89 47 1C                        mov dword ptr [rdi + 0x1c], eax
002705D7  85 C0                           test eax, eax
002705D9  0F 8E E0 02 00 00               jle 0x1402708bf
002705DF  65 48 8B 1C 25 28 00 00 00      mov rbx, qword ptr gs:[0x28]
002705E8  48 81 C3 90 00 00 00            add rbx, 0x90
002705EF  F6 05 10 65 D5 00 01            test byte ptr [rip + 0xd56510], 1
002705F6  75 3F                           jne 0x140270637
002705F8  0F 0D 0B                        prefetchw byte ptr [rbx]
002705FB  48 8B 03                        mov rax, qword ptr [rbx]
002705FE  48 85 C0                        test rax, rax
00270601  75 16                           jne 0x140270619
00270603  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00270607  48 8B C3                        mov rax, rbx
0027060A  F0 4C 0F B1 29                  lock cmpxchg qword ptr [rcx], r13
0027060F  74 3D                           je 0x14027064e
00270611  48 8B CB                        mov rcx, rbx
00270614  E8 87 74 FA FF                  call 0x140217aa0
00270619  48 8D 48 08                     lea rcx, [rax + 8]
0027061D  4C 89 2B                        mov qword ptr [rbx], r13
00270620  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00270624  48 8B C2                        mov rax, rdx
00270627  48 87 01                        xchg qword ptr [rcx], rax
0027062A  32 C2                           xor al, dl
0027062C  A8 04                           test al, 4
0027062E  74 1E                           je 0x14027064e
00270630  E8 EB 75 FA FF                  call 0x140217c20
00270635  EB 17                           jmp 0x14027064e
00270637  8B 05 1B D8 C9 00               mov eax, dword ptr [rip + 0xc9d81b]
0027063D  85 C0                           test eax, eax
0027063F  75 B7                           jne 0x1402705f8
00270641  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00270646  48 8B CB                        mov rcx, rbx
00270649  E8 A2 73 FA FF                  call 0x1402179f0
0027064E  44 39 2D CB 66 D5 00            cmp dword ptr [rip + 0xd566cb], r13d
00270655  74 0D                           je 0x140270664
00270657  44 0F 20 C1                     mov rcx, cr8
0027065B  40 0F B6 D6                     movzx edx, sil
0027065F  E8 34 50 28 00                  call 0x1404f5698
00270664  40 0F B6 C6                     movzx eax, sil
00270668  44 0F 22 C0                     mov cr8, rax
0027066C  48 85 FF                        test rdi, rdi
0027066F  0F 85 AA 00 00 00               jne 0x14027071f
00270675  44 0F 20 C6                     mov rsi, cr8
00270679  45 0F 22 C4                     mov cr8, r12
0027067D  44 39 2D 9C 66 D5 00            cmp dword ptr [rip + 0xd5669c], r13d
00270684  0F 85 5D 01 00 00               jne 0x1402707e7
0027068A  65 48 8B 0C 25 28 00 00 00      mov rcx, qword ptr gs:[0x28]
00270693  48 81 C1 A0 00 00 00            add rcx, 0xa0
0027069A  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
0027069E  F6 05 61 64 D5 00 21            test byte ptr [rip + 0xd56461], 0x21
002706A5  0F 85 EC 00 00 00               jne 0x140270797
002706AB  48 8B C1                        mov rax, rcx
002706AE  48 87 02                        xchg qword ptr [rdx], rax
002706B1  48 85 C0                        test rax, rax
002706B4  0F 85 4C 01 00 00               jne 0x140270806
002706BA  8B 45 04                        mov eax, dword ptr [rbp + 4]
002706BD  83 E8 01                        sub eax, 1
002706C0  89 45 04                        mov dword ptr [rbp + 4], eax
002706C3  0F 88 51 02 00 00               js 0x14027091a
002706C9  85 C0                           test eax, eax
002706CB  0F 84 DE 00 00 00               je 0x1402707af
002706D1  65 48 8B 1C 25 28 00 00 00      mov rbx, qword ptr gs:[0x28]
002706DA  48 81 C3 A0 00 00 00            add rbx, 0xa0
002706E1  F6 05 1E 64 D5 00 01            test byte ptr [rip + 0xd5641e], 1
002706E8  74 56                           je 0x140270740
002706EA  8B 05 68 D7 C9 00               mov eax, dword ptr [rip + 0xc9d768]
002706F0  85 C0                           test eax, eax
002706F2  75 4C                           jne 0x140270740
002706F4  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
002706F9  48 8B CB                        mov rcx, rbx
002706FC  E8 EF 72 FA FF                  call 0x1402179f0
00270701  44 39 2D 18 66 D5 00            cmp dword ptr [rip + 0xd56618], r13d
00270708  74 0D                           je 0x140270717
0027070A  44 0F 20 C1                     mov rcx, cr8
0027070E  40 0F B6 D6                     movzx edx, sil
00270712  E8 81 4F 28 00                  call 0x1404f5698
00270717  40 0F B6 C6                     movzx eax, sil
0027071B  44 0F 22 C0                     mov cr8, rax
0027071F  48 8B C7                        mov rax, rdi
00270722  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00270727  48 8B 6C 24 70                  mov rbp, qword ptr [rsp + 0x70]
0027072C  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00270731  48 83 C4 30                     add rsp, 0x30
00270735  41 5F                           pop r15
00270737  41 5E                           pop r14
00270739  41 5D                           pop r13
0027073B  41 5C                           pop r12
0027073D  5F                              pop rdi
0027073E  C3                              ret
0027073F  CC                              int3
00270740  0F 0D 0B                        prefetchw byte ptr [rbx]
00270743  48 8B 03                        mov rax, qword ptr [rbx]
00270746  48 85 C0                        test rax, rax
00270749  75 16                           jne 0x140270761
0027074B  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0027074F  48 8B C3                        mov rax, rbx
00270752  F0 4C 0F B1 29                  lock cmpxchg qword ptr [rcx], r13
00270757  74 A8                           je 0x140270701
00270759  48 8B CB                        mov rcx, rbx
0027075C  E8 3F 73 FA FF                  call 0x140217aa0
00270761  48 8D 48 08                     lea rcx, [rax + 8]
00270765  4C 89 2B                        mov qword ptr [rbx], r13
00270768  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
0027076C  48 8B C2                        mov rax, rdx
0027076F  48 87 01                        xchg qword ptr [rcx], rax
00270772  32 C2                           xor al, dl
00270774  A8 04                           test al, 4
00270776  74 89                           je 0x140270701
00270778  E8 A3 74 FA FF                  call 0x140217c20
0027077D  EB 82                           jmp 0x140270701
0027077F  8B 05 D3 D6 C9 00               mov eax, dword ptr [rip + 0xc9d6d3]
00270785  85 C0                           test eax, eax
00270787  0F 85 17 FE FF FF               jne 0x1402705a4
0027078D  E8 BE 50 00 00                  call 0x140275850
00270792  E9 1C FE FF FF                  jmp 0x1402705b3
00270797  8B 05 BB D6 C9 00               mov eax, dword ptr [rip + 0xc9d6bb]
0027079D  85 C0                           test eax, eax
0027079F  0F 85 06 FF FF FF               jne 0x1402706ab
002707A5  E8 A6 50 00 00                  call 0x140275850
002707AA  E9 0B FF FF FF                  jmp 0x1402706ba
002707AF  48 8B 85 38 01 00 00            mov rax, qword ptr [rbp + 0x138]
002707B6  8B 48 20                        mov ecx, dword ptr [rax + 0x20]
002707B9  F6 C1 07                        test cl, 7
002707BC  0F 84 0F FF FF FF               je 0x1402706d1
002707C2  44 0F B6 C6                     movzx r8d, sil
002707C6  33 D2                           xor edx, edx
002707C8  48 8B CD                        mov rcx, rbp
002707CB  E8 F8 03 00 00                  call 0x140270bc8
002707D0  E9 4A FF FF FF                  jmp 0x14027071f
002707D5  41 0F B6 D4                     movzx edx, r12b
002707D9  40 0F B6 CE                     movzx ecx, sil
002707DD  E8 1A 4F 28 00                  call 0x1404f56fc
002707E2  E9 9C FD FF FF                  jmp 0x140270583
002707E7  41 0F B6 D4                     movzx edx, r12b
002707EB  40 0F B6 CE                     movzx ecx, sil
002707EF  E8 08 4F 28 00                  call 0x1404f56fc
002707F4  E9 91 FE FF FF                  jmp 0x14027068a
002707F9  48 8B D0                        mov rdx, rax
002707FC  E8 AF 76 FE FF                  call 0x140257eb0
00270801  E9 AD FD FF FF                  jmp 0x1402705b3
00270806  48 8B D0                        mov rdx, rax
00270809  E8 A2 76 FE FF                  call 0x140257eb0
0027080E  E9 A7 FE FF FF                  jmp 0x1402706ba
00270813  40 0F B6 D6                     movzx edx, sil
00270817  B9 09 00 00 00                  mov ecx, 9
0027081C  E8 1F 1D 00 00                  call 0x140272540
00270821  44 8B 4B 40                     mov r9d, dword ptr [rbx + 0x40]
00270825  41 C1 E9 04                     shr r9d, 4
00270829  41 80 E1 01                     and r9b, 1
0027082D  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
00270832  66 45 39 2E                     cmp word ptr [r14], r13w
00270836  74 4A                           je 0x140270882
00270838  33 D2                           xor edx, edx
0027083A  48 8D 44 24 68                  lea rax, [rsp + 0x68]
0027083F  45 33 C0                        xor r8d, r8d
00270842  48 8B CD                        mov rcx, rbp
00270845  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0027084A  E8 81 21 7C 00                  call 0x140a329d0
0027084F  41 89 07                        mov dword ptr [r15], eax
00270852  85 C0                           test eax, eax
00270854  78 36                           js 0x14027088c
00270856  3D 01 01 00 00                  cmp eax, 0x101
0027085B  74 2F                           je 0x14027088c
0027085D  3D C0 00 00 00                  cmp eax, 0xc0
00270862  74 28                           je 0x14027088c
00270864  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00270869  48 85 C0                        test rax, rax
0027086C  0F 85 B0 FE FF FF               jne 0x140270722
00270872  8D 48 09                        lea ecx, [rax + 9]
00270875  E8 06 35 00 00                  call 0x140273d80
0027087A  0F B6 F0                        movzx esi, al
0027087D  E9 34 FD FF FF                  jmp 0x1402705b6
00270882  4C 39 6B 28                     cmp qword ptr [rbx + 0x28], r13
00270886  75 B0                           jne 0x140270838
00270888  B2 01                           mov dl, 1
0027088A  EB AE                           jmp 0x14027083a
0027088C  45 33 C0                        xor r8d, r8d
0027088F  33 D2                           xor edx, edx
00270891  48 8B CD                        mov rcx, rbp
00270894  E8 D7 00 00 00                  call 0x140270970
00270899  33 C0                           xor eax, eax
0027089B  45 39 2F                        cmp dword ptr [r15], r13d
0027089E  0F 8C 7E FE FF FF               jl 0x140270722
002708A4  41 C7 07 12 00 00 C0            mov dword ptr [r15], 0xc0000012
002708AB  E9 72 FE FF FF                  jmp 0x140270722
002708B0  41 C7 07 22 00 00 C0            mov dword ptr [r15], 0xc0000022
002708B7  49 8B FD                        mov rdi, r13
002708BA  E9 20 FD FF FF                  jmp 0x1402705df
002708BF  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
002708C3  48 85 C9                        test rcx, rcx
002708C6  74 36                           je 0x1402708fe
002708C8  BA 50 01 00 00                  mov edx, 0x150
002708CD  E8 A2 7A 1B 00                  call 0x140428374
002708D2  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
002708D6  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
002708DA  48 85 C9                        test rcx, rcx
002708DD  74 1F                           je 0x1402708fe
002708DF  BA 50 01 00 00                  mov edx, 0x150
002708E4  E8 8B 7A 1B 00                  call 0x140428374
002708E9  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
002708ED  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
002708F1  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
002708F5  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
002708F9  E8 76 7A 1B 00                  call 0x140428374
002708FE  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
00270901  33 D2                           xor edx, edx
00270903  41 B9 07 00 00 00               mov r9d, 7
00270909  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0027090E  4C 8B C7                        mov r8, rdi
00270911  8D 4A 18                        lea ecx, [rdx + 0x18]
00270914  E8 47 CD 28 00                  call 0x1404fd660
00270919  CC                              int3
0027091A  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
0027091E  48 85 C9                        test rcx, rcx
00270921  74 1B                           je 0x14027093e
00270923  BA 50 01 00 00                  mov edx, 0x150
00270928  E8 47 7A 1B 00                  call 0x140428374
0027092D  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
00270931  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00270935  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00270939  E8 36 7A 1B 00                  call 0x140428374
0027093E  48 63 45 04                     movsxd rax, dword ptr [rbp + 4]
00270942  33 D2                           xor edx, edx
00270944  41 B9 06 00 00 00               mov r9d, 6
0027094A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0027094F  4C 8B C5                        mov r8, rbp
00270952  8D 4A 18                        lea ecx, [rdx + 0x18]
00270955  E8 06 CD 28 00                  call 0x1404fd660
0027095A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopCheckVpbMounted(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (48);
    if ((*(unsigned int *)(v_rip + 13985699)) != 0) goto loc_002707D5;
loc_00270583:
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 40))) + (144);
    if (((*(unsigned __int8 *)(v_rip + 13985128)) & (33)) != 0) goto loc_0027077F;
loc_002705A4:
    if (a1 != 0) goto loc_002707F9;
loc_002705B3:
    v_r13 = 0;
loc_002705B6:
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 56) + 4))) & (1)) == 0) goto loc_00270813;
    if (((2) & ((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 56) + 4)))) != 0) goto loc_002708B0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 56) + 28))) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 56) + 28) = (unsigned int)(result);
    if (condition_is_less_or_equal) goto loc_002708BF;
loc_002705DF:
    v_rbx = (*(unsigned __int64 *)(gs_base + (0 + 40))) + (144);
    if (((*(unsigned __int8 *)(v_rip + 13985040)) & (1)) != 0) goto loc_00270637;
loc_002705F8:
    if (*(unsigned __int64 *)(v_rbx) != 0) goto loc_00270619;
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_0027064E;
    result = KxWaitForLockChainValid(v_rbx, *(unsigned __int64 *)(a1 + 8), a3, a4);
loc_00270619:
    *(unsigned __int64 *)(v_rbx) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_rbx + 8)) ^ ((unsigned __int8)(*(unsigned __int64 *)(v_rbx + 8))));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0027064E;
    result = KeWakeAddressAll(result + 8, *(unsigned __int64 *)(v_rbx + 8), a3, a4);
    goto loc_0027064E;
loc_00270637:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13228059))) != 0) goto loc_002705F8;
    result = KiReleaseQueuedSpinLockInstrumented(v_rbx, v_stack_p0, a3, a4);
loc_0027064E:
    if ((*(unsigned int *)(v_rip + 13985483)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(a2 + 56) != 0) goto loc_0027071F;
    if ((*(unsigned int *)(v_rip + 13985436)) != 0) goto loc_002707E7;
loc_0027068A:
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 40))) + (160);
    if (((*(unsigned __int8 *)(v_rip + 13984865)) & (33)) != 0) goto loc_00270797;
loc_002706AB:
    if (a1 != 0) goto loc_00270806;
loc_002706BA:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) - (1));
    *(unsigned int *)(a2 + 4) = (unsigned int)(result);
    if (sign_flag) goto loc_0027091A;
    if ((unsigned int)(result) == 0) goto loc_002707AF;
loc_002706D1:
    v_rbx = (*(unsigned __int64 *)(gs_base + (0 + 40))) + (160);
    if (((*(unsigned __int8 *)(v_rip + 13984798)) & (1)) == 0) goto loc_00270740;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13227880))) != 0) goto loc_00270740;
    result = KiReleaseQueuedSpinLockInstrumented(v_rbx, v_stack_p0, a3, a4);
loc_00270701:
    if ((*(unsigned int *)(v_rip + 13985304)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_0027071F:
loc_00270722:
    v_rsp = (v_rsp) + (48);
    return *(unsigned __int64 *)(a2 + 56);
loc_00270740:
    if (*(unsigned __int64 *)(v_stack_p8) != 0) goto loc_00270761;
    if (*(unsigned __int64 *)(v_stack_p8) == 0) goto loc_00270701;
    result = KxWaitForLockChainValid(v_stack_p8, a2, a3, a4);
loc_00270761:
    *(unsigned __int64 *)(v_stack_p8) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_stack_p8 + 8)) ^ ((unsigned __int8)(*(unsigned __int64 *)(v_stack_p8 + 8))));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_00270701;
    result = KeWakeAddressAll(result + 8, *(unsigned __int64 *)(v_stack_p8 + 8), a3, a4);
    goto loc_00270701;
loc_0027077F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13227731))) != 0) goto loc_002705A4;
    result = KiAcquireQueuedSpinLockInstrumented(result + 8, *(unsigned __int64 *)(v_stack_p8 + 8), a3, a4);
    goto loc_002705B3;
loc_00270797:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13227707))) != 0) goto loc_002706AB;
    result = KiAcquireQueuedSpinLockInstrumented(result + 8, *(unsigned __int64 *)(v_stack_p8 + 8), a3, a4);
    goto loc_002706BA;
loc_002707AF:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 312) + 32)))) & (7)) == 0) goto loc_002706D1;
    a2 = 0;
    result = IopCompleteUnloadOrDelete(v_stack_p18, a2, (unsigned __int8)(v_stack_p20), a4);
    goto loc_0027071F;
loc_002707D5:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p20), 2, (unsigned __int8)(v_stack_p20), a4);
    goto loc_00270583;
loc_002707E7:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p20), 2, (unsigned __int8)(v_stack_p20), a4);
    goto loc_0027068A;
loc_002707F9:
    result = KxWaitForLockOwnerShip((unsigned __int8)(v_stack_p20), result, (unsigned __int8)(v_stack_p20), a4);
    goto loc_002705B3;
loc_00270806:
    result = KxWaitForLockOwnerShip((unsigned __int8)(v_stack_p20), result, (unsigned __int8)(v_stack_p20), a4);
    goto loc_002706BA;
loc_00270813:
    result = KeReleaseQueuedSpinLock(9, (unsigned __int8)(v_stack_p20), (unsigned __int8)(v_stack_p20), a4);
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 64))) >> (4));
    a4 = (unsigned __int8)((a4) & (1));
    v_stack_p68 = 0;
    if ((*(unsigned __int16 *)(a3)) == 0) goto loc_00270882;
loc_00270838:
    a2 = 0;
loc_0027083A:
    a3 = 0;
    v_stack_p20 = v_stack_p68;
    result = IopMountVolume(v_stack_p18, a2, a3, a4);
    *(unsigned int *)(a4) = (unsigned int)(result);
    if (sign_flag) goto loc_0027088C;
    if (((unsigned int)(result)) == 257) goto loc_0027088C;
    if (((unsigned int)(result)) == 192) goto loc_0027088C;
    if (v_stack_p68 != 0) goto loc_00270722;
    result = KeAcquireQueuedSpinLock(v_stack_p68 + 9, a2, a3, a4);
    goto loc_002705B6;
loc_00270882:
    if ((*(unsigned __int64 *)(v_stack_p8 + 40)) != 0) goto loc_00270838;
    goto loc_0027083A;
loc_0027088C:
    a3 = 0;
    a2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_p18, a2, a3, a4);
    result = 0;
    if ((*(unsigned int *)(a4)) < 0) goto loc_00270722;
    *(unsigned int *)(a4) = 0xC0000012ULL;
    goto loc_00270722;
loc_002708B0:
    *(unsigned int *)(a4) = 0xC0000022ULL;
    goto loc_002705DF;
loc_002708BF:
    if (*(unsigned __int64 *)(0 + 8) == 0) goto loc_002708FE;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(0 + 8), 336, a3, a4);
    result = *(unsigned __int64 *)(0 + 8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 8) != 0) {
        a2 = 336;
        result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 8), a2, a3, a4);
        result = *(unsigned __int64 *)(0 + 8);
        a1 = *(unsigned __int64 *)(result + 8);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    a2 = 0;
    v_stack_p20 = (unsigned int)(*(unsigned int *)(0 + 28));
    result = KeBugCheckEx(a2 + 24, a2, 0, 7);
loc_0027091A:
    if (*(unsigned __int64 *)(v_stack_p18 + 8) != 0) {
        a2 = 336;
        result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(v_stack_p18 + 8), a2, 0, 7);
        a1 = *(unsigned __int64 *)(v_stack_p18 + 8);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, 0, 7);
    }
    a2 = 0;
    v_stack_p20 = (int)(*(unsigned int *)(v_stack_p18 + 4));
    result = KeBugCheckEx(a2 + 24, a2, v_stack_p18, 6);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopCheckVpbMounted(void *Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p0;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p68;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (48);
    if ((*(uint32_t *)(v_rip + 0xD567A3)) != 0) goto loc_002707D5;
loc_00270583:
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x28))) + (144);
    if (((*(uint8_t *)(v_rip + 0xD56568)) & (33)) != 0) goto loc_0027077F;
loc_002705A4:
    if (Arg1 != NULL) goto loc_002707F9;
loc_002705B3:
    local_r13 = 0;
loc_002705B6:
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x38) + 0x4))) & (1)) == 0) goto loc_00270813;
    if (((2) & ((uint8_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x38) + 0x4)))) != 0) goto loc_002708B0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x38) + 0x1C))) + 1);
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x38) + 0x1C) = (uint32_t)(result);
    if (condition_is_less_or_equal) goto loc_002708BF;
loc_002705DF:
    local_rbx = (*(uint64_t *)(gs_base + (0 + 0x28))) + (144);
    if (((*(uint8_t *)(v_rip + 0xD56510)) & (1)) != 0) goto loc_00270637;
loc_002705F8:
    if (*(uint64_t *)(local_rbx) != 0) goto loc_00270619;
    if (*(uint64_t *)(local_rbx) == 0) goto loc_0027064E;
    result = KxWaitForLockChainValid(local_rbx, *(uint64_t *)(arg1 + 0x8), Arg3, Arg4);
loc_00270619:
    *(uint64_t *)(local_rbx) = 0;
    result = (uint8_t)((*(uint64_t *)(local_rbx + 0x8)) ^ ((uint8_t)(*(uint64_t *)(local_rbx + 0x8))));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0027064E;
    result = KeWakeAddressAll(result + 8, *(uint64_t *)(local_rbx + 0x8), Arg3, Arg4);
    goto loc_0027064E;
loc_00270637:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC9D81B))) != 0) goto loc_002705F8;
    result = KiReleaseQueuedSpinLockInstrumented(local_rbx, v_stack_p0, Arg3, Arg4);
loc_0027064E:
    if ((*(uint32_t *)(v_rip + 0xD566CB)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(arg2 + 0x38) != 0) goto loc_0027071F;
    if ((*(uint32_t *)(v_rip + 0xD5669C)) != 0) goto loc_002707E7;
loc_0027068A:
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x28))) + (160);
    if (((*(uint8_t *)(v_rip + 0xD56461)) & (33)) != 0) goto loc_00270797;
loc_002706AB:
    if (Arg1 != NULL) goto loc_00270806;
loc_002706BA:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x4))) - (1));
    *(uint32_t *)(arg2 + 0x4) = (uint32_t)(result);
    if (sign_flag) goto loc_0027091A;
    if ((uint32_t)(result) == 0) goto loc_002707AF;
loc_002706D1:
    local_rbx = (*(uint64_t *)(gs_base + (0 + 0x28))) + (160);
    if (((*(uint8_t *)(v_rip + 0xD5641E)) & (1)) == 0) goto loc_00270740;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC9D768))) != 0) goto loc_00270740;
    result = KiReleaseQueuedSpinLockInstrumented(local_rbx, v_stack_p0, Arg3, Arg4);
loc_00270701:
    if ((*(uint32_t *)(v_rip + 0xD56618)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
loc_0027071F:
loc_00270722:
    local_rsp = (local_rsp) + (48);
    return *(uint64_t *)(arg2 + 0x38);
loc_00270740:
    if (*(uint64_t *)(v_stack_p8) != 0) goto loc_00270761;
    if (*(uint64_t *)(v_stack_p8) == 0) goto loc_00270701;
    result = KxWaitForLockChainValid(v_stack_p8, Arg2, Arg3, Arg4);
loc_00270761:
    *(uint64_t *)(v_stack_p8) = 0;
    result = (uint8_t)((*(uint64_t *)(v_stack_p8 + 0x8)) ^ ((uint8_t)(*(uint64_t *)(v_stack_p8 + 0x8))));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_00270701;
    result = KeWakeAddressAll(result + 8, *(uint64_t *)(v_stack_p8 + 0x8), Arg3, Arg4);
    goto loc_00270701;
loc_0027077F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC9D6D3))) != 0) goto loc_002705A4;
    result = KiAcquireQueuedSpinLockInstrumented(result + 8, *(uint64_t *)(v_stack_p8 + 0x8), Arg3, Arg4);
    goto loc_002705B3;
loc_00270797:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC9D6BB))) != 0) goto loc_002706AB;
    result = KiAcquireQueuedSpinLockInstrumented(result + 8, *(uint64_t *)(v_stack_p8 + 0x8), Arg3, Arg4);
    goto loc_002706BA;
loc_002707AF:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0x138) + 0x20)))) & (7)) == 0) goto loc_002706D1;
    Arg2 = 0;
    result = IopCompleteUnloadOrDelete(v_stack_p18, Arg2, (uint8_t)(v_stack_p20), Arg4);
    goto loc_0027071F;
loc_002707D5:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p20), 2, (uint8_t)(v_stack_p20), Arg4);
    goto loc_00270583;
loc_002707E7:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p20), 2, (uint8_t)(v_stack_p20), Arg4);
    goto loc_0027068A;
loc_002707F9:
    result = KxWaitForLockOwnerShip((uint8_t)(v_stack_p20), result, (uint8_t)(v_stack_p20), Arg4);
    goto loc_002705B3;
loc_00270806:
    result = KxWaitForLockOwnerShip((uint8_t)(v_stack_p20), result, (uint8_t)(v_stack_p20), Arg4);
    goto loc_002706BA;
loc_00270813:
    result = KeReleaseQueuedSpinLock(9, (uint8_t)(v_stack_p20), (uint8_t)(v_stack_p20), Arg4);
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x40))) >> (4));
    Arg4 = (uint8_t)((Arg4) & (1));
    v_stack_p68 = 0;
    if ((*(uint16_t *)(arg3)) == 0) goto loc_00270882;
loc_00270838:
    Arg2 = 0;
loc_0027083A:
    Arg3 = 0;
    v_stack_p20 = v_stack_p68;
    result = IopMountVolume(v_stack_p18, Arg2, Arg3, Arg4);
    *(uint32_t *)(arg4) = (uint32_t)(result);
    if (sign_flag) goto loc_0027088C;
    if (((uint32_t)(result)) == 257) goto loc_0027088C;
    if (((uint32_t)(result)) == 192) goto loc_0027088C;
    if (v_stack_p68 != 0) goto loc_00270722;
    result = KeAcquireQueuedSpinLock(v_stack_p68 + 9, Arg2, Arg3, Arg4);
    goto loc_002705B6;
loc_00270882:
    if ((*(uint64_t *)(v_stack_p8 + 0x28)) != 0) goto loc_00270838;
    goto loc_0027083A;
loc_0027088C:
    Arg3 = 0;
    Arg2 = 0;
    result = IopDecrementDeviceObjectRef(v_stack_p18, Arg2, Arg3, Arg4);
    result = 0;
    if ((*(uint32_t *)(arg4)) < 0) goto loc_00270722;
    *(uint32_t *)(arg4) = 0xC0000012ULL;
    goto loc_00270722;
loc_002708B0:
    *(uint32_t *)(arg4) = 0xC0000022ULL;
    goto loc_002705DF;
loc_002708BF:
    if (*(uint64_t *)(0 + 0x8) == 0) goto loc_002708FE;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(0 + 0x8), 336, Arg3, Arg4);
    result = *(uint64_t *)(0 + 0x8);
    if (*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x8) != 0) {
        Arg2 = 336;
        result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x8), Arg2, Arg3, Arg4);
        result = *(uint64_t *)(0 + 0x8);
        Arg1 = *(uint64_t *)(result + 0x8);
        Arg2 = *(uint16_t *)(arg1 + 0x38);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    v_stack_p20 = (uint32_t)(*(uint32_t *)(0 + 0x1C));
    result = KeBugCheckEx(Arg2 + 24, Arg2, 0, 7);
loc_0027091A:
    if (*(uint64_t *)(v_stack_p18 + 0x8) != 0) {
        Arg2 = 336;
        result = IoAddTriageDumpDataBlock(*(uint64_t *)(v_stack_p18 + 0x8), Arg2, 0, 7);
        Arg1 = *(uint64_t *)(v_stack_p18 + 0x8);
        Arg2 = *(uint16_t *)(arg1 + 0x38);
        Arg1 = *(uint64_t *)(arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, 0, 7);
    }
    Arg2 = 0;
    v_stack_p20 = (int32_t)(*(uint32_t *)(v_stack_p18 + 0x4));
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_p18, 6);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg2` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0x4` | `32` | `W` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x138` | `64` | `R` |
| `Arg3` | `+ 0x0` | `16` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00270540&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
