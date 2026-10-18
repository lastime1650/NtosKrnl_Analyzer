# sub_0025FB5C

- RVA: `0x0025FB5C`–`0x00260117` (길이 `1,467` bytes)
- VA: `0x000000014025FB5C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006434C`
- 디코드: `345`개 명령, `1,467/1,467` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x0025FC1B` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0025FCE1` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0025FD13` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x0025FD26` → [KiHaltOnAddressWakeEntireList](../21/KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)
- `0x0025FD63` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0025FD7D` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0025FE1F` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0025FE78` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0025FE92` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0025FF57` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0025FF93` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00260092` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x002600C8` → [KeDisableInterrupts](../21/KeDisableInterrupts_function_00217BE0.md) (function, `0x00217BE0`)
- `0x002600DB` → [KiHaltOnAddressWakeEntireList](../21/KiHaltOnAddressWakeEntireList_function_00217AF4.md) (function, `0x00217AF4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0025FBB1` → RVA `0x00FC6F88` (`ALMOSTRO`; read)
- `0x0025FC04` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x0025FCA3` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0025FD08` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0025FD4C` → RVA `0x00F0DE58` (`.data`; read)
- `0x0025FD68` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0025FE42` → RVA `0x00FC6B06` (`ALMOSTRO`; reference)
- `0x0025FF37` → RVA `0x00E68468` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0025FF57` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0025FF93` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **22**
  - `0x0025FBBA` → [sub_00260D5A + 0x16F](../26/Unknown_function_00260D5A.md) (`tail-transfer`)
  - `0x0025FBC6` → [sub_00261078](../26/Unknown_function_00261078.md) (`tail-transfer`)
  - `0x0025FBD6` → [sub_0026118A](../26/Unknown_function_0026118A.md) (`tail-transfer`)
  - `0x0025FC31` → [sub_00260D5A + 0x20](../26/Unknown_function_00260D5A.md) (`tail-transfer`)
  - `0x0025FD43` → [sub_00260366 + 0x74E](../26/Unknown_function_00260366.md) (`tail-transfer`)
  - `0x0025FDA1` → [sub_00260129 + 0xAA](../26/Unknown_function_00260129.md) (`tail-transfer`)
  - `0x0025FDC6` → [sub_00260366 + 0x747](../26/Unknown_function_00260366.md) (`tail-transfer`)
  - `0x0025FDDF` → [sub_00260366 + 0x18](../26/Unknown_function_00260366.md) (`tail-transfer`)
  - `0x0025FDF0` → [sub_00260129](../26/Unknown_function_00260129.md) (`tail-transfer`)
  - `0x0025FE06` → [sub_00260129 + 0x2D](../26/Unknown_function_00260129.md) (`tail-transfer`)
  - `0x0025FE28` → [sub_00260129 + 0x6C](../26/Unknown_function_00260129.md) (`tail-transfer`)
  - `0x0025FEA7` → [sub_0026029A + 0x4D](../26/Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x0025FF03` → [sub_0026029A + 0x4D](../26/Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x0025FF29` → [sub_0026029A + 0x4D](../26/Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x0025FF62` → [sub_0026029A + 0x4D](../26/Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x00260005` → [sub_0026029A + 0x4D](../26/Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x0026000E` → [sub_0026029A + 0x4A](../26/Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x00260022` → [sub_0026118A + 0x186](../26/Unknown_function_0026118A.md) (`tail-transfer`)
  - `0x00260034` → [sub_0026029A](../26/Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x00260041` → [sub_0026029A + 0x4D](../26/Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x0026004E` → [sub_0026029A + 0x4D](../26/Unknown_function_0026029A.md) (`tail-transfer`)
  - `0x002600FC` → [sub_00260366 + 0x605](../26/Unknown_function_00260366.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0025FB5C  8B 4B 38                        mov ecx, dword ptr [rbx + 0x38]
0025FB5F  41 BC 01 00 00 00               mov r12d, 1
0025FB65  8B C1                           mov eax, ecx
0025FB67  83 E1 07                        and ecx, 7
0025FB6A  C1 E8 03                        shr eax, 3
0025FB6D  44 8D 2C C5 F8 FF FF FF         lea r13d, [rax*8 - 8]
0025FB75  44 0B E9                        or r13d, ecx
0025FB78  44 89 6B 38                     mov dword ptr [rbx + 0x38], r13d
0025FB7C  41 C1 ED 03                     shr r13d, 3
0025FB80  45 85 ED                        test r13d, r13d
0025FB83  0F 85 B9 02 00 00               jne 0x14025fe42
0025FB89  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0025FB8C  48 8B 7B 30                     mov rdi, qword ptr [rbx + 0x30]
0025FB90  41 84 C7                        test r15b, al
0025FB93  0F 84 6F 05 00 00               je 0x140260108
0025FB99  48 83 E7 FC                     and rdi, 0xfffffffffffffffc
0025FB9D  48 85 FF                        test rdi, rdi
0025FBA0  0F 84 95 00 00 00               je 0x14025fc3b
0025FBA6  41 84 C4                        test r12b, al
0025FBA9  74 40                           je 0x14025fbeb
0025FBAB  45 32 F6                        xor r14b, r14b
0025FBAE  45 32 E4                        xor r12b, r12b
0025FBB1  39 35 D1 73 D6 00               cmp dword ptr [rip + 0xd673d1], esi
0025FBB7  4C 8B EE                        mov r13, rsi
0025FBBA  0F 85 09 13 00 00               jne 0x140260ec9
0025FBC0  39 B7 E0 05 00 00               cmp dword ptr [rdi + 0x5e0], esi
0025FBC6  0F 84 AC 14 00 00               je 0x140261078
0025FBCC  F0 FF 8F E0 05 00 00            lock dec dword ptr [rdi + 0x5e0]
0025FBD3  45 84 F6                        test r14b, r14b
0025FBD6  0F 85 AE 15 00 00               jne 0x14026118a
0025FBDC  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0025FBDF  41 BC 01 00 00 00               mov r12d, 1
0025FBE5  83 E0 FE                        and eax, 0xfffffffe
0025FBE8  89 43 38                        mov dword ptr [rbx + 0x38], eax
0025FBEB  A8 04                           test al, 4
0025FBED  74 10                           je 0x14025fbff
0025FBEF  F0 FF 8F E4 05 00 00            lock dec dword ptr [rdi + 0x5e4]
0025FBF6  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0025FBF9  83 E0 FB                        and eax, 0xfffffffb
0025FBFC  89 43 38                        mov dword ptr [rbx + 0x38], eax
0025FBFF  41 84 C7                        test r15b, al
0025FC02  74 37                           je 0x14025fc3b
0025FC04  39 35 06 54 D6 00               cmp dword ptr [rip + 0xd65406], esi
0025FC0A  74 14                           je 0x14025fc20
0025FC0C  41 B9 44 66 6C 74               mov r9d, 0x746c6644
0025FC12  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0025FC16  45 8B C4                        mov r8d, r12d
0025FC19  33 D2                           xor edx, edx
0025FC1B  E8 C4 0D FB FF                  call 0x1402109e4
0025FC20  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0025FC27  F0 48 0F C1 47 D0               lock xadd qword ptr [rdi - 0x30], rax
0025FC2D  48 83 E8 01                     sub rax, 1
0025FC31  0F 8E 43 11 00 00               jle 0x140260d7a
0025FC37  83 63 38 FD                     and dword ptr [rbx + 0x38], 0xfffffffd
0025FC3B  48 89 73 30                     mov qword ptr [rbx + 0x30], rsi
0025FC3F  4C 8B F6                        mov r14, rsi
0025FC42  8B 4B 48                        mov ecx, dword ptr [rbx + 0x48]
0025FC45  8B 43 44                        mov eax, dword ptr [rbx + 0x44]
0025FC48  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0025FC4C  85 C9                           test ecx, ecx
0025FC4E  0F 84 D1 01 00 00               je 0x14025fe25
0025FC54  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
0025FC58  BA 7F FF 00 00                  mov edx, 0xff7f
0025FC5D  48 89 73 20                     mov qword ptr [rbx + 0x20], rsi
0025FC61  66 21 53 1A                     and word ptr [rbx + 0x1a], dx
0025FC65  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0025FC69  89 73 48                        mov dword ptr [rbx + 0x48], esi
0025FC6C  8B 53 40                        mov edx, dword ptr [rbx + 0x40]
0025FC6F  FF CA                           dec edx
0025FC71  03 D1                           add edx, ecx
0025FC73  89 53 40                        mov dword ptr [rbx + 0x40], edx
0025FC76  39 73 4C                        cmp dword ptr [rbx + 0x4c], esi
0025FC79  75 0E                           jne 0x14025fc89
0025FC7B  39 73 48                        cmp dword ptr [rbx + 0x48], esi
0025FC7E  75 09                           jne 0x14025fc89
0025FC80  B9 F9 00 00 00                  mov ecx, 0xf9
0025FC85  66 21 4B 1A                     and word ptr [rbx + 0x1a], cx
0025FC89  44 0F B6 6B 1B                  movzx r13d, byte ptr [rbx + 0x1b]
0025FC8E  4D 85 F6                        test r14, r14
0025FC91  74 10                           je 0x14025fca3
0025FC93  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
0025FC96  83 E0 07                        and eax, 7
0025FC99  4C 89 73 30                     mov qword ptr [rbx + 0x30], r14
0025FC9D  83 C8 08                        or eax, 8
0025FCA0  89 43 38                        mov dword ptr [rbx + 0x38], eax
0025FCA3  F6 05 5C 6E D6 00 01            test byte ptr [rip + 0xd66e5c], 1
0025FCAA  0F 85 9C 00 00 00               jne 0x14025fd4c
0025FCB0  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
0025FCB5  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0025FCBA  48 85 C0                        test rax, rax
0025FCBD  75 27                           jne 0x14025fce6
0025FCBF  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0025FCC4  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0025FCC9  F0 48 0F B1 31                  lock cmpxchg qword ptr [rcx], rsi
0025FCCE  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025FCD3  48 3B C1                        cmp rax, rcx
0025FCD6  0F 84 8C 00 00 00               je 0x14025fd68
0025FCDC  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025FCE1  E8 BA 7D FB FF                  call 0x140217aa0
0025FCE6  4C 8D 40 08                     lea r8, [rax + 8]
0025FCEA  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0025FCEF  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0025FCF4  48 8B C1                        mov rax, rcx
0025FCF7  49 87 00                        xchg qword ptr [r8], rax
0025FCFA  32 C1                           xor al, cl
0025FCFC  A8 04                           test al, 4
0025FCFE  74 68                           je 0x14025fd68
0025FD00  F0 09 34 24                     lock or dword ptr [rsp], esi
0025FD04  49 C1 E8 05                     shr r8, 5
0025FD08  4C 8D 15 F1 02 DA FF            lea r10, [rip - 0x25fd0f]
0025FD0F  41 83 E0 7F                     and r8d, 0x7f
0025FD13  E8 C8 7E FB FF                  call 0x140217be0
0025FD18  48 8B D6                        mov rdx, rsi
0025FD1B  0F B6 F8                        movzx edi, al
0025FD1E  4B 87 94 C2 20 1B F2 00         xchg qword ptr [r10 + r8*8 + 0xf21b20], rdx
0025FD26  E8 C9 7D FB FF                  call 0x140217af4
0025FD2B  40 84 FF                        test dil, dil
0025FD2E  74 38                           je 0x14025fd68
0025FD30  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0025FD39  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0025FD40  4D 85 C0                        test r8, r8
0025FD43  0F 85 6B 0D 00 00               jne 0x140260ab4
0025FD49  FB                              sti
0025FD4A  EB 1C                           jmp 0x14025fd68
0025FD4C  8B 05 06 E1 CA 00               mov eax, dword ptr [rip + 0xcae106]
0025FD52  85 C0                           test eax, eax
0025FD54  0F 85 56 FF FF FF               jne 0x14025fcb0
0025FD5A  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0025FD5E  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025FD63  E8 88 7C FB FF                  call 0x1402179f0
0025FD68  39 35 B2 6F D6 00               cmp dword ptr [rip + 0xd66fb2], esi
0025FD6E  0F B6 7C 24 58                  movzx edi, byte ptr [rsp + 0x58]
0025FD73  74 0D                           je 0x14025fd82
0025FD75  44 0F 20 C1                     mov rcx, cr8
0025FD79  40 0F B6 D7                     movzx edx, dil
0025FD7D  E8 16 59 29 00                  call 0x1404f5698
0025FD82  44 0F 22 C7                     mov cr8, rdi
0025FD86  4D 85 F6                        test r14, r14
0025FD89  B8 01 00 00 00                  mov eax, 1
0025FD8E  8B F8                           mov edi, eax
0025FD90  41 BC 03 00 00 00               mov r12d, 3
0025FD96  41 0F 45 FC                     cmovne edi, r12d
0025FD9A  44 8B F0                        mov r14d, eax
0025FD9D  48 39 75 90                     cmp qword ptr [rbp - 0x70], rsi
0025FDA1  0F 85 2C 04 00 00               jne 0x1402601d3
0025FDA7  41 BE 22 00 01 00               mov r14d, 0x10022
0025FDAD  44 8B EE                        mov r13d, esi
0025FDB0  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
0025FDB5  E9 E1 00 00 00                  jmp 0x14025fe9b
0025FDBA  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
0025FDBE  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
0025FDC2  41 F6 C6 03                     test r14b, 3
0025FDC6  0F 85 E1 0C 00 00               jne 0x140260aad
0025FDCC  41 0F B6 86 60 04 00 00         movzx eax, byte ptr [r14 + 0x460]
0025FDD4  48 8B 53 30                     mov rdx, qword ptr [rbx + 0x30]
0025FDD8  48 8D 7B 30                     lea rdi, [rbx + 0x30]
0025FDDC  49 3B D6                        cmp rdx, r14
0025FDDF  0F 84 99 05 00 00               je 0x14026037e
0025FDE5  48 85 D2                        test rdx, rdx
0025FDE8  48 8B CE                        mov rcx, rsi
0025FDEB  0F 95 C1                        setne cl
0025FDEE  85 C0                           test eax, eax
0025FDF0  0F 85 33 03 00 00               jne 0x140260129
0025FDF6  8B 53 48                        mov edx, dword ptr [rbx + 0x48]
0025FDF9  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
0025FDFC  48 8B 7B 10                     mov rdi, qword ptr [rbx + 0x10]
0025FE00  48 03 D0                        add rdx, rax
0025FE03  48 85 FF                        test rdi, rdi
0025FE06  0F 85 4A 03 00 00               jne 0x140260156
0025FE0C  4C 8B CF                        mov r9, rdi
0025FE0F  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0025FE14  4D 8B C6                        mov r8, r14
0025FE17  48 8B D3                        mov rdx, rbx
0025FE1A  B9 E3 00 00 00                  mov ecx, 0xe3
0025FE1F  E8 3C D8 29 00                  call 0x1404fd660
0025FE24  CC                              int3
0025FE25  39 73 4C                        cmp dword ptr [rbx + 0x4c], esi
0025FE28  0F 85 67 03 00 00               jne 0x140260195
0025FE2E  BA 7F FF 00 00                  mov edx, 0xff7f
0025FE33  66 89 73 18                     mov word ptr [rbx + 0x18], si
0025FE37  66 21 53 1A                     and word ptr [rbx + 0x1a], dx
0025FE3B  8B D6                           mov edx, esi
0025FE3D  E9 31 FE FF FF                  jmp 0x14025fc73
0025FE42  44 84 25 BD 6C D6 00            test byte ptr [rip + 0xd66cbd], r12b
0025FE49  41 BE 32 00 01 00               mov r14d, 0x10032
0025FE4F  8B 43 44                        mov eax, dword ptr [rbx + 0x44]
0025FE52  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
0025FE57  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0025FE5B  0F 84 00 02 00 00               je 0x140260061
0025FE61  8B 05 F1 DF CA 00               mov eax, dword ptr [rip + 0xcadff1]
0025FE67  85 C0                           test eax, eax
0025FE69  0F 85 F2 01 00 00               jne 0x140260061
0025FE6F  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
0025FE73  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0025FE78  E8 73 7B FB FF                  call 0x1402179f0
0025FE7D  39 35 9D 6E D6 00               cmp dword ptr [rip + 0xd66e9d], esi
0025FE83  0F B6 7C 24 58                  movzx edi, byte ptr [rsp + 0x58]
0025FE88  74 0D                           je 0x14025fe97
0025FE8A  44 0F 20 C1                     mov rcx, cr8
0025FE8E  40 0F B6 D7                     movzx edx, dil
0025FE92  E8 01 58 29 00                  call 0x1404f5698
0025FE97  44 0F 22 C7                     mov cr8, rdi
0025FE9B  65 FF 04 25 6C 90 00 00         inc dword ptr gs:[0x906c]
0025FEA3  39 74 24 60                     cmp dword ptr [rsp + 0x60], esi
0025FEA7  0F 84 3A 04 00 00               je 0x1402602e7
0025FEAD  0F 57 C0                        xorps xmm0, xmm0
0025FEB0  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
0025FEB4  0F 11 45 B8                     movups xmmword ptr [rbp - 0x48], xmm0
0025FEB8  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
0025FEBC  0F 31                           rdtsc
0025FEBE  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
0025FEC7  48 C1 E2 20                     shl rdx, 0x20
0025FECB  48 0B C2                        or rax, rdx
0025FECE  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0025FED3  41 FF 87 70 8F 00 00            inc dword ptr [r15 + 0x8f70]
0025FEDA  41 0F B6 87 D0 00 00 00         movzx eax, byte ptr [r15 + 0xd0]
0025FEE2  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0025FEEB  66 89 44 24 70                  mov word ptr [rsp + 0x70], ax
0025FEF0  41 0F B6 87 D1 00 00 00         movzx eax, byte ptr [r15 + 0xd1]
0025FEF8  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0025FEFC  48 39 B1 20 06 00 00            cmp qword ptr [rcx + 0x620], rsi
0025FF03  0F 84 DE 03 00 00               je 0x1402602e7
0025FF09  65 4C 8B 24 25 88 01 00 00      mov r12, qword ptr gs:[0x188]
0025FF12  41 8B CE                        mov ecx, r14d
0025FF15  81 E1 00 00 FF FF               and ecx, 0xffff0000
0025FF1B  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0025FF1F  41 8B 84 24 A0 05 00 00         mov eax, dword ptr [r12 + 0x5a0]
0025FF27  A8 01                           test al, 1
0025FF29  0F 85 B8 03 00 00               jne 0x1402602e7
0025FF2F  4D 8B B4 24 20 06 00 00         mov r14, qword ptr [r12 + 0x620]
0025FF37  44 8B 05 2A 85 C0 00            mov r8d, dword ptr [rip + 0xc0852a]
0025FF3E  44 89 44 24 60                  mov dword ptr [rsp + 0x60], r8d
0025FF43  4D 85 F6                        test r14, r14
0025FF46  75 59                           jne 0x14025ffa1
0025FF48  BA 00 02 00 00                  mov edx, 0x200
0025FF4D  41 8D 4E 48                     lea ecx, [r14 + 0x48]
0025FF51  41 B8 52 65 54 72               mov r8d, 0x72546552
0025FF57  E8 94 21 92 00                  call 0x140b820f0
0025FF5C  48 8B F8                        mov rdi, rax
0025FF5F  48 85 C0                        test rax, rax
0025FF62  0F 84 7F 03 00 00               je 0x1402602e7
0025FF68  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0025FF6C  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0025FF70  89 47 1C                        mov dword ptr [rdi + 0x1c], eax
0025FF73  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0025FF77  89 47 28                        mov dword ptr [rdi + 0x28], eax
0025FF7A  33 C0                           xor eax, eax
0025FF7C  89 77 20                        mov dword ptr [rdi + 0x20], esi
0025FF7F  F0 49 0F B1 BC 24 20 06 00 00   lock cmpxchg qword ptr [r12 + 0x620], rdi
0025FF89  4C 8B F0                        mov r14, rax
0025FF8C  74 7D                           je 0x14026000b
0025FF8E  33 D2                           xor edx, edx
0025FF90  48 8B CF                        mov rcx, rdi
0025FF93  E8 D8 28 92 00                  call 0x140b82870
0025FF98  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
0025FF9C  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
0025FFA1  48 8B C6                        mov rax, rsi
0025FFA4  8B D6                           mov edx, esi
0025FFA6  83 FA 08                        cmp edx, 8
0025FFA9  73 30                           jae 0x14025ffdb
0025FFAB  45 8B 4E 1C                     mov r9d, dword ptr [r14 + 0x1c]
0025FFAF  44 3B C9                        cmp r9d, ecx
0025FFB2  75 0C                           jne 0x14025ffc0
0025FFB4  49 39 5E 10                     cmp qword ptr [r14 + 0x10], rbx
0025FFB8  75 06                           jne 0x14025ffc0
0025FFBA  45 39 46 28                     cmp dword ptr [r14 + 0x28], r8d
0025FFBE  74 3F                           je 0x14025ffff
0025FFC0  48 85 C0                        test rax, rax
0025FFC3  0F 85 8D 00 00 00               jne 0x140260056
0025FFC9  45 85 C9                        test r9d, r9d
0025FFCC  0F 84 81 00 00 00               je 0x140260053
0025FFD2  45 39 46 28                     cmp dword ptr [r14 + 0x28], r8d
0025FFD6  7D 7E                           jge 0x140260056
0025FFD8  49 8B C6                        mov rax, r14
0025FFDB  4C 8B F0                        mov r14, rax
0025FFDE  48 85 C0                        test rax, rax
0025FFE1  74 1C                           je 0x14025ffff
0025FFE3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0025FFE7  89 48 1C                        mov dword ptr [rax + 0x1c], ecx
0025FFEA  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
0025FFEE  48 89 30                        mov qword ptr [rax], rsi
0025FFF1  48 89 70 08                     mov qword ptr [rax + 8], rsi
0025FFF5  89 70 18                        mov dword ptr [rax + 0x18], esi
0025FFF8  44 89 40 28                     mov dword ptr [rax + 0x28], r8d
0025FFFC  89 70 2C                        mov dword ptr [rax + 0x2c], esi
0025FFFF  49 8B FE                        mov rdi, r14
00260002  4D 85 F6                        test r14, r14
00260005  0F 84 DC 02 00 00               je 0x1402602e7
0026000B  39 77 20                        cmp dword ptr [rdi + 0x20], esi
0026000E  0F 84 D0 02 00 00               je 0x1402602e4
00260014  41 FF 87 74 8F 00 00            inc dword ptr [r15 + 0x8f74]
0026001B  41 FF C5                        inc r13d
0026001E  44 39 6F 24                     cmp dword ptr [rdi + 0x24], r13d
00260022  0F 82 E8 12 00 00               jb 0x140261310
00260028  44 8B 44 24 68                  mov r8d, dword ptr [rsp + 0x68]
0026002D  41 81 F8 22 00 01 00            cmp r8d, 0x10022
00260034  0F 84 60 02 00 00               je 0x14026029a
0026003A  41 81 F8 32 00 01 00            cmp r8d, 0x10032
00260041  0F 85 A0 02 00 00               jne 0x1402602e7
00260047  C7 47 20 02 00 00 00            mov dword ptr [rdi + 0x20], 2
0026004E  E9 94 02 00 00                  jmp 0x1402602e7
00260053  49 8B C6                        mov rax, r14
00260056  49 83 C6 40                     add r14, 0x40
0026005A  FF C2                           inc edx
0026005C  E9 45 FF FF FF                  jmp 0x14025ffa6
00260061  0F 0D 4C 24 48                  prefetchw byte ptr [rsp + 0x48]
00260066  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0026006B  48 85 C0                        test rax, rax
0026006E  75 27                           jne 0x140260097
00260070  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00260075  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0026007A  F0 48 0F B1 31                  lock cmpxchg qword ptr [rcx], rsi
0026007F  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00260084  48 3B C1                        cmp rax, rcx
00260087  0F 84 F0 FD FF FF               je 0x14025fe7d
0026008D  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00260092  E8 09 7A FB FF                  call 0x140217aa0
00260097  4C 8D 40 08                     lea r8, [rax + 8]
0026009B  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
002600A0  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002600A5  48 8B C1                        mov rax, rcx
002600A8  49 87 00                        xchg qword ptr [r8], rax
002600AB  32 C1                           xor al, cl
002600AD  A8 04                           test al, 4
002600AF  0F 84 C8 FD FF FF               je 0x14025fe7d
002600B5  F0 09 34 24                     lock or dword ptr [rsp], esi
002600B9  49 C1 E8 05                     shr r8, 5
002600BD  4C 8D 15 3C FF D9 FF            lea r10, [rip - 0x2600c4]
002600C4  41 83 E0 7F                     and r8d, 0x7f
002600C8  E8 13 7B FB FF                  call 0x140217be0
002600CD  48 8B D6                        mov rdx, rsi
002600D0  0F B6 F8                        movzx edi, al
002600D3  4B 87 94 C2 20 1B F2 00         xchg qword ptr [r10 + r8*8 + 0xf21b20], rdx
002600DB  E8 14 7A FB FF                  call 0x140217af4
002600E0  40 84 FF                        test dil, dil
002600E3  0F 84 94 FD FF FF               je 0x14025fe7d
002600E9  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
002600F2  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
002600F9  4D 85 C0                        test r8, r8
002600FC  0F 85 69 08 00 00               jne 0x14026096b
00260102  FB                              sti
00260103  E9 75 FD FF FF                  jmp 0x14025fe7d
00260108  40 F6 C7 03                     test dil, 3
0026010C  0F 85 29 FB FF FF               jne 0x14025fc3b
00260112  E9 86 FA FF FF                  jmp 0x14025fb9d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0025FB5C(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, unsigned __int8 a9, __int64 a10, unsigned __int8 a11, unsigned int a12, unsigned int a13)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p60;
    unsigned int v_stack_p68;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;

    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 56))) & (7));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 56))))) >> (3));
    v_r13 = (unsigned int)((result * 8 - 8) | ((unsigned int)(a1)));
    *(unsigned int *)(v_rbx + 56) = (unsigned int)(v_r13);
    v_r13 = (unsigned int)((v_r13) >> (3));
    if ((unsigned int)(v_r13) != 0) goto loc_0025FE42;
    if ((((unsigned __int8)(v_r15)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 56))))) == 0) goto loc_00260108;
    v_rdi = (*(unsigned __int64 *)(v_rbx + 48)) & (-4);
loc_0025FB9D:
    if (v_rdi == 0) goto loc_0025FC3B;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 56))))) == 0) goto loc_0025FBEB;
    v_r14 = 0;
    v_r12 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 56))) & (0xFFFFFFFEULL));
    *(unsigned int *)(v_rbx + 56) = (unsigned int)(result);
loc_0025FBEB:
    if ((((unsigned __int8)(result)) & (4)) != 0) {
        result = *(unsigned int *)(v_rbx + 56);
        result = (unsigned int)((result) & (0xFFFFFFFBULL));
        *(unsigned int *)(v_rbx + 56) = (unsigned int)(result);
    }
    if ((((unsigned __int8)(v_r15)) & ((unsigned __int8)(result))) == 0) goto loc_0025FC3B;
    if ((*(unsigned int *)(v_rip + 14046214)) != ((unsigned int)(v_rsi))) {
        a4 = 0x746C6644ULL;
        a1 = v_rdi - 48;
        a3 = 1;
        a2 = 0;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
loc_0025FC3B:
    *(unsigned __int64 *)(v_rbx + 48) = v_rsi;
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 68)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 72))) == 0) goto loc_0025FE25;
    *(unsigned __int64 *)(v_rbx + 32) = v_rsi;
    *(unsigned __int64 *)(v_rbp - 112) = *(unsigned __int64 *)(v_rbx + 32);
    *(unsigned int *)(v_rbx + 72) = (unsigned int)(v_rsi);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 64))) - 1);
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 72)))));
loc_0025FC73:
    *(unsigned int *)(v_rbx + 64) = a2;
    if ((*(unsigned int *)(v_rbx + 76)) != ((unsigned int)(v_rsi))) goto loc_0025FC89;
    if ((*(unsigned int *)(v_rbx + 72)) == ((unsigned int)(v_rsi))) {
        a1 = 249;
    }
    result = *(unsigned __int64 *)(v_rbx + 32);
    if (v_rsi != 0) {
        result = *(unsigned int *)(v_rbx + 56);
        result = (unsigned int)((result) & (7));
        *(unsigned __int64 *)(v_rbx + 48) = v_rsi;
        result = (unsigned int)((result) | (8));
        *(unsigned int *)(v_rbx + 56) = (unsigned int)(result);
    }
    if (((*(unsigned __int8 *)(v_rip + 14052956)) & (1)) != 0) goto loc_0025FD4C;
loc_0025FCB0:
    if (a9 != 0) goto loc_0025FCE6;
    if (a9 == a9) goto loc_0025FD68;
    result = KxWaitForLockChainValid(a9, a2, a3, a4);
loc_0025FCE6:
    v_stack_p48 = v_rsi;
    result = (unsigned __int8)((a10) ^ ((unsigned __int8)(a10)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0025FD68;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(a10, a2, a3, a4);
    result = KiHaltOnAddressWakeEntireList(a10, v_rsi, a3, a4);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0025FD68;
    goto loc_0025FD68;
loc_0025FD4C:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13295878))) != 0) goto loc_0025FCB0;
    result = KiReleaseQueuedSpinLockInstrumented(a9, *(unsigned __int64 *)(v_rbp + 72), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
loc_0025FD68:
    if ((*(unsigned int *)(v_rip + 14053298)) != ((unsigned int)(v_rsi))) {
        a1 = v_cr8;
        a2 = a11;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    }
    v_rdi = 1;
    if (v_rsi != 0) { v_rdi = 3; }
    v_stack_p68 = (unsigned int)((unsigned int)(0x10022ULL));
    goto loc_0025FE9B;
loc_0025FE25:
    *(unsigned __int16 *)(v_rbx + 24) = (unsigned __int16)(v_rsi);
    goto loc_0025FC73;
loc_0025FE42:
    v_stack_p68 = (unsigned int)((unsigned int)(0x10032ULL));
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 68)));
    if (((*(unsigned __int8 *)(v_rip + 14052541)) & (3)) == 0) goto loc_00260061;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13295601))) != 0) goto loc_00260061;
    result = KiReleaseQueuedSpinLockInstrumented(a9, *(unsigned __int64 *)(v_rbp + 72), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
loc_0025FE7D:
    if ((*(unsigned int *)(v_rip + 14053021)) != ((unsigned int)(v_rsi))) {
        a1 = a11;
        a2 = a11;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    }
loc_0025FE9B:
    *(unsigned __int64 *)(v_rbp - 88) = v_xmm0;
    *(unsigned __int64 *)(v_rbp - 72) = v_xmm0;
    *(unsigned __int64 *)(v_rbp - 56) = v_xmm0;
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_stack_p78 = result;
    v_stack_p70 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    v_stack_p30 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x10032ULL)))) & (0xFFFF0000ULL));
    v_stack_p38 = (unsigned int)(a1);
    v_stack_p60 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12617002)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) != 0) goto loc_0025FFA1;
    result = ExAllocatePool2(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1568) + 72, 512, (unsigned int)(0x72546552ULL), a4);
    *(unsigned __int64 *)(result + 16) = v_rbx;
    *(unsigned int *)(result + 28) = (unsigned int)((unsigned int)(a7));
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(a12));
    result = 0;
    *(unsigned int *)(result + 32) = (unsigned int)(v_rsi);
    if (condition_is_equal) goto loc_0026000B;
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, (unsigned int)(0x72546552ULL), a4);
loc_0025FFA1:
loc_0025FFA6:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rsi)))) >= 8) goto loc_0025FFDB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)))) != ((unsigned int)((unsigned int)(a7)))) goto loc_0025FFC0;
    if ((*(unsigned __int64 *)(0 + 16)) != v_rbx) goto loc_0025FFC0;
    if ((*(unsigned int *)(0 + 40)) == ((unsigned int)((unsigned int)(a12)))) goto loc_0025FFFF;
loc_0025FFC0:
    if (v_rsi != 0) goto loc_00260056;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 28))) == 0) goto loc_00260053;
    if ((*(unsigned int *)(0 + 40)) >= ((unsigned int)((unsigned int)(a12)))) goto loc_00260056;
loc_0025FFDB:
    if (0 != 0) {
        *(unsigned __int64 *)(0 + 16) = v_rbx;
        *(unsigned int *)(0 + 28) = (unsigned int)((unsigned int)(a7));
        *(unsigned __int64 *)(0 + 32) = v_rsi;
        *(unsigned __int64 *)(0) = v_rsi;
        *(unsigned __int64 *)(0 + 8) = v_rsi;
        *(unsigned int *)(0 + 24) = (unsigned int)(v_rsi);
        *(unsigned int *)(0 + 40) = (unsigned int)((unsigned int)(a12));
        *(unsigned int *)(0 + 44) = (unsigned int)(v_rsi);
    }
loc_0026000B:
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) + 1);
    *(unsigned int *)(0 + 32) = 2;
loc_00260053:
loc_00260056:
    v_r14 = (0) + (64);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) + 1);
    goto loc_0025FFA6;
loc_00260061:
    if (a9 != 0) goto loc_00260097;
    if (a9 == a9) goto loc_0025FE7D;
    result = KxWaitForLockChainValid(a9, a2, (unsigned int)(a13), (unsigned int)(*(unsigned int *)(0 + 28)));
loc_00260097:
    v_stack_p48 = v_rsi;
    result = (unsigned __int8)((a10) ^ ((unsigned __int8)(a10)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0025FE7D;
    a3 = (result + 8) >> (5);
    a3 = (unsigned int)((a3) & (127));
    result = KeDisableInterrupts(a10, a2, a3, (unsigned int)(*(unsigned int *)(0 + 28)));
    result = KiHaltOnAddressWakeEntireList(a10, v_rsi, a3, (unsigned int)(*(unsigned int *)(0 + 28)));
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0025FE7D;
    goto loc_0025FE7D;
loc_00260108:
    if ((((unsigned __int8)((unsigned __int8)(result))) & (3)) != 0) goto loc_0025FC3B;
    goto loc_0025FB9D;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0025FB5C(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint32_t Arg7, uint64_t Arg8, uint8_t Arg9, void *Arg10, uint8_t Arg11, uint32_t Arg12, uint32_t Arg13)
{
    uint8_t *arg10 = (uint8_t *)Arg10;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    uint32_t v_stack_p0;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p60;
    uint32_t v_stack_p68;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;

    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x38))) & (7));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x38))))) >> (3));
    local_r13 = (uint32_t)((result * 8 - 8) | ((uint32_t)(Arg1)));
    *(uint32_t *)(local_rbx + 0x38) = (uint32_t)(local_r13);
    local_r13 = (uint32_t)((local_r13) >> (3));
    if ((uint32_t)(local_r13) != 0) goto loc_0025FE42;
    if ((((uint8_t)(local_r15)) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x38))))) == 0) goto loc_00260108;
    local_rdi = (*(uint64_t *)(local_rbx + 0x30)) & (-4);
loc_0025FB9D:
    if (local_rdi == 0) goto loc_0025FC3B;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x38))))) == 0) goto loc_0025FBEB;
    local_r14 = 0;
    local_r12 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x38))) & (0xFFFFFFFEULL));
    *(uint32_t *)(local_rbx + 0x38) = (uint32_t)(result);
loc_0025FBEB:
    if ((((uint8_t)(result)) & (4)) != 0) {
        result = *(uint32_t *)(local_rbx + 0x38);
        result = (uint32_t)((result) & (0xFFFFFFFBULL));
        *(uint32_t *)(local_rbx + 0x38) = (uint32_t)(result);
    }
    if ((((uint8_t)(local_r15)) & ((uint8_t)(result))) == 0) goto loc_0025FC3B;
    if ((*(uint32_t *)(v_rip + 0xD65406)) != ((uint32_t)(local_rsi))) {
        Arg4 = 0x746C6644ULL;
        Arg1 = local_rdi - 48;
        Arg3 = 1;
        Arg2 = 0;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (-1) - (1);
loc_0025FC3B:
    *(uint64_t *)(local_rbx + 0x30) = local_rsi;
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x44)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x48))) == 0) goto loc_0025FE25;
    *(uint64_t *)(local_rbx + 0x20) = local_rsi;
    *(uint64_t *)(local_rbp - 0x70) = *(uint64_t *)(local_rbx + 0x20);
    *(uint32_t *)(local_rbx + 0x48) = (uint32_t)(local_rsi);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x40))) - 1);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x48)))));
loc_0025FC73:
    *(uint32_t *)(local_rbx + 0x40) = Arg2;
    if ((*(uint32_t *)(local_rbx + 0x4C)) != ((uint32_t)(local_rsi))) goto loc_0025FC89;
    if ((*(uint32_t *)(local_rbx + 0x48)) == ((uint32_t)(local_rsi))) {
        Arg1 = 249;
    }
    result = *(uint64_t *)(local_rbx + 0x20);
    if (local_rsi != 0) {
        result = *(uint32_t *)(local_rbx + 0x38);
        result = (uint32_t)((result) & (7));
        *(uint64_t *)(local_rbx + 0x30) = local_rsi;
        result = (uint32_t)((result) | (8));
        *(uint32_t *)(local_rbx + 0x38) = (uint32_t)(result);
    }
    if (((*(uint8_t *)(v_rip + 0xD66E5C)) & (1)) != 0) goto loc_0025FD4C;
loc_0025FCB0:
    if (Arg9 != 0) goto loc_0025FCE6;
    if (Arg9 == Arg9) goto loc_0025FD68;
    result = KxWaitForLockChainValid(Arg9, Arg2, Arg3, Arg4);
loc_0025FCE6:
    v_stack_p48 = local_rsi;
    result = (uint8_t)((Arg10) ^ ((uint8_t)(Arg10)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0025FD68;
    Arg3 = (result + 8) >> (5);
    Arg3 = (uint32_t)((Arg3) & (127));
    result = KeDisableInterrupts(Arg10, Arg2, Arg3, Arg4);
    result = KiHaltOnAddressWakeEntireList(Arg10, local_rsi, Arg3, Arg4);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0025FD68;
    goto loc_0025FD68;
loc_0025FD4C:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAE106))) != 0) goto loc_0025FCB0;
    result = KiReleaseQueuedSpinLockInstrumented(Arg9, *(uint64_t *)(local_rbp + 0x48), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
loc_0025FD68:
    if ((*(uint32_t *)(v_rip + 0xD66FB2)) != ((uint32_t)(local_rsi))) {
        Arg1 = v_cr8;
        Arg2 = Arg11;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    }
    local_rdi = 1;
    if (local_rsi != 0) { local_rdi = 3; }
    v_stack_p68 = (uint32_t)((uint32_t)(0x10022ULL));
    goto loc_0025FE9B;
loc_0025FE25:
    *(uint16_t *)(local_rbx + 0x18) = (uint16_t)(local_rsi);
    goto loc_0025FC73;
loc_0025FE42:
    v_stack_p68 = (uint32_t)((uint32_t)(0x10032ULL));
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x44)));
    if (((*(uint8_t *)(v_rip + 0xD66CBD)) & (3)) == 0) goto loc_00260061;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCADFF1))) != 0) goto loc_00260061;
    result = KiReleaseQueuedSpinLockInstrumented(Arg9, *(uint64_t *)(local_rbp + 0x48), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
loc_0025FE7D:
    if ((*(uint32_t *)(v_rip + 0xD66E9D)) != ((uint32_t)(local_rsi))) {
        Arg1 = Arg11;
        Arg2 = Arg11;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), Arg4);
    }
loc_0025FE9B:
    *(uint64_t *)(local_rbp - 0x58) = v_xmm0;
    *(uint64_t *)(local_rbp - 0x48) = v_xmm0;
    *(uint64_t *)(local_rbp - 0x38) = v_xmm0;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    v_stack_p78 = result;
    v_stack_p70 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    v_stack_p30 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x10032ULL)))) & (0xFFFF0000ULL));
    v_stack_p38 = (uint32_t)(Arg1);
    v_stack_p60 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC0852A)));
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) != 0) goto loc_0025FFA1;
    result = ExAllocatePool2(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x620) + 72, 512, (uint32_t)(0x72546552ULL), Arg4);
    *(uint64_t *)(result + 0x10) = local_rbx;
    *(uint32_t *)(result + 0x1C) = (uint32_t)((uint32_t)(Arg7));
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(Arg12));
    result = 0;
    *(uint32_t *)(result + 0x20) = (uint32_t)(local_rsi);
    if (condition_is_equal) goto loc_0026000B;
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, (uint32_t)(0x72546552ULL), Arg4);
loc_0025FFA1:
loc_0025FFA6:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rsi)))) >= 8) goto loc_0025FFDB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)))) != ((uint32_t)((uint32_t)(Arg7)))) goto loc_0025FFC0;
    if ((*(uint64_t *)(0 + 0x10)) != local_rbx) goto loc_0025FFC0;
    if ((*(uint32_t *)(0 + 0x28)) == ((uint32_t)((uint32_t)(Arg12)))) goto loc_0025FFFF;
loc_0025FFC0:
    if (local_rsi != 0) goto loc_00260056;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C))) == 0) goto loc_00260053;
    if ((*(uint32_t *)(0 + 0x28)) >= ((uint32_t)((uint32_t)(Arg12)))) goto loc_00260056;
loc_0025FFDB:
    if (0 != 0) {
        *(uint64_t *)(0 + 0x10) = local_rbx;
        *(uint32_t *)(0 + 0x1C) = (uint32_t)((uint32_t)(Arg7));
        *(uint64_t *)(0 + 0x20) = local_rsi;
        *(uint64_t *)(0) = local_rsi;
        *(uint64_t *)(0 + 0x8) = local_rsi;
        *(uint32_t *)(0 + 0x18) = (uint32_t)(local_rsi);
        *(uint32_t *)(0 + 0x28) = (uint32_t)((uint32_t)(Arg12));
        *(uint32_t *)(0 + 0x2C) = (uint32_t)(local_rsi);
    }
loc_0026000B:
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) + 1);
    *(uint32_t *)(0 + 0x20) = 2;
loc_00260053:
loc_00260056:
    local_r14 = (0) + (64);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) + 1);
    goto loc_0025FFA6;
loc_00260061:
    if (Arg9 != 0) goto loc_00260097;
    if (Arg9 == Arg9) goto loc_0025FE7D;
    result = KxWaitForLockChainValid(Arg9, Arg2, (uint32_t)(Arg13), (uint32_t)(*(uint32_t *)(0 + 0x1C)));
loc_00260097:
    v_stack_p48 = local_rsi;
    result = (uint8_t)((Arg10) ^ ((uint8_t)(Arg10)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0025FE7D;
    Arg3 = (result + 8) >> (5);
    Arg3 = (uint32_t)((Arg3) & (127));
    result = KeDisableInterrupts(Arg10, Arg2, Arg3, (uint32_t)(*(uint32_t *)(0 + 0x1C)));
    result = KiHaltOnAddressWakeEntireList(Arg10, local_rsi, Arg3, (uint32_t)(*(uint32_t *)(0 + 0x1C)));
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0025FE7D;
    goto loc_0025FE7D;
loc_00260108:
    if ((((uint8_t)((uint8_t)(result))) & (3)) != 0) goto loc_0025FC3B;
    goto loc_0025FB9D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg10` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0025FB5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
