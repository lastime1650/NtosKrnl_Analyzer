# KiInterruptDispatchCommon

- RVA: `0x0039F3D0`–`0x0039F7FC` (길이 `1,068` bytes)
- VA: `0x000000014039F3D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00081CC8`
- 디코드: `264`개 명령, `1,068/1,068` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0039F499` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x0039F4FC` → [KeSetSystemGroupAffinityThread](KeSetSystemGroupAffinityThread_function_00399140.md) (function, `0x00399140`)
- `0x0039F51B` → [KiGetInterruptObjectFromVector](KiGetInterruptObjectFromVector_function_0039F2B8.md) (function, `0x0039F2B8`)
- `0x0039F5B2` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0039F5CA` → [KiInvokeInterruptServiceRoutine](KiInvokeInterruptServiceRoutine_function_0039F8E0.md) (function, `0x0039F8E0`)
- `0x0039F5FF` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x0039F61B` → [KiProcessPendingDisconnect](KiProcessPendingDisconnect_function_0039F374.md) (function, `0x0039F374`)
- `0x0039F67A` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0039F68C` → [KeRevertToUserGroupAffinityThread](KeRevertToUserGroupAffinityThread_function_00398EC0.md) (function, `0x00398EC0`)
- `0x0039F69C` → [IoProcessPassiveInterrupts](IoProcessPassiveInterrupts_function_0039F85C.md) (function, `0x0039F85C`)
- `0x0039F6AB` → [KiProcessDisconnectList](KiProcessDisconnectList_function_0039F804.md) (function, `0x0039F804`)
- `0x0039F6CB` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0039F6F4` → [HalpReleaseHighLevelLock](../2D/HalpReleaseHighLevelLock_function_002D1C58.md) (function, `0x002D1C58`)
- `0x0039F718` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039F72A` → [HalpReleaseHighLevelLock](../2D/HalpReleaseHighLevelLock_function_002D1C58.md) (function, `0x002D1C58`)
- `0x0039F737` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039F746` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039F778` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0039F7EF` → [KiDisconnectInterruptInternal](../2D/KiDisconnectInterruptInternal_function_002D38C0.md) (function, `0x002D38C0`)

### Direct callers
- [IopPassiveInterruptWorker](../45/IopPassiveInterruptWorker_function_0045F3A0.md) at `0x0045F418`
- [KeDispatchSecondaryInterrupt](../47/KeDispatchSecondaryInterrupt_function_0047F920.md) at `0x0047F969`

### Static image references
- `0x0039F3E7` → RVA `0x00E0A740` (`.data`; read)
- `0x0039F45E` → RVA `0x00F11028` (`.data`; read)
- `0x0039F48A` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0039F7E9` → [sub_006E622C](../6E/Unknown_function_006E622C.md) (`tail-transfer`)
  - `0x0039F7F7` → [sub_006E622C + 0x5](../6E/Unknown_function_006E622C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0039F3D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0039F3D5  55                              push rbp
0039F3D6  56                              push rsi
0039F3D7  57                              push rdi
0039F3D8  41 54                           push r12
0039F3DA  41 55                           push r13
0039F3DC  41 56                           push r14
0039F3DE  41 57                           push r15
0039F3E0  48 81 EC 90 00 00 00            sub rsp, 0x90
0039F3E7  48 8B 05 52 B3 A6 00            mov rax, qword ptr [rip + 0xa6b352]
0039F3EE  48 33 C4                        xor rax, rsp
0039F3F1  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0039F3F9  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0039F401  44 8B E1                        mov r12d, ecx
0039F404  89 4C 24 24                     mov dword ptr [rsp + 0x24], ecx
0039F408  0F 57 C0                        xorps xmm0, xmm0
0039F40B  33 C9                           xor ecx, ecx
0039F40D  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
0039F411  44 8B E9                        mov r13d, ecx
0039F414  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0039F419  45 8B F0                        mov r14d, r8d
0039F41C  8B DA                           mov ebx, edx
0039F41E  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
0039F423  44 0F 20 C0                     mov rax, cr8
0039F427  4D 85 C9                        test r9, r9
0039F42A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0039F42F  4C 8D 7C 24 60                  lea r15, [rsp + 0x60]
0039F434  88 4C 24 21                     mov byte ptr [rsp + 0x21], cl
0039F438  4D 0F 45 F9                     cmovne r15, r9
0039F43C  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
0039F440  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0039F444  40 8A E9                        mov bpl, cl
0039F447  8D 51 0C                        lea edx, [rcx + 0xc]
0039F44A  8D 79 0F                        lea edi, [rcx + 0xf]
0039F44D  4D 89 7F 08                     mov qword ptr [r15 + 8], r15
0039F451  4D 89 3F                        mov qword ptr [r15], r15
0039F454  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0039F459  45 85 E4                        test r12d, r12d
0039F45C  74 62                           je 0x14039f4c0
0039F45E  48 8B 3D C3 1B B7 00            mov rdi, qword ptr [rip + 0xb71bc3]
0039F465  8D AB 00 FF FF FF               lea ebp, [rbx - 0x100]
0039F46B  48 8D 1C 6D 00 00 00 00         lea rbx, [rbp*2]
0039F473  48 03 DD                        add rbx, rbp
0039F476  48 C1 E3 04                     shl rbx, 4
0039F47A  48 03 FB                        add rdi, rbx
0039F47D  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0039F482  44 0F 20 C6                     mov rsi, cr8
0039F486  44 0F 22 C2                     mov cr8, rdx
0039F48A  39 0D 90 78 C2 00               cmp dword ptr [rip + 0xc27890], ecx
0039F490  0F 85 9E 02 00 00               jne 0x14039f734
0039F496  48 8B CF                        mov rcx, rdi
0039F499  E8 92 8F E6 FF                  call 0x140208430
0039F49E  45 33 DB                        xor r11d, r11d
0039F4A1  41 8B FB                        mov edi, r11d
0039F4A4  81 FD 00 01 00 00               cmp ebp, 0x100
0039F4AA  73 0F                           jae 0x14039f4bb
0039F4AC  0F AE E8                        lfence
0039F4AF  48 8B 05 72 1B B7 00            mov rax, qword ptr [rip + 0xb71b72]
0039F4B6  48 8B 7C 03 28                  mov rdi, qword ptr [rbx + rax + 0x28]
0039F4BB  41 8A EB                        mov bpl, r11b
0039F4BE  EB 63                           jmp 0x14039f523
0039F4C0  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0039F4C5  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
0039F4CA  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0039F4D3  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
0039F4D8  0F B6 81 D0 00 00 00            movzx eax, byte ptr [rcx + 0xd0]
0039F4DF  8A 89 D1 00 00 00               mov cl, byte ptr [rcx + 0xd1]
0039F4E5  66 89 44 24 58                  mov word ptr [rsp + 0x58], ax
0039F4EA  B8 01 00 00 00                  mov eax, 1
0039F4EF  48 D3 E0                        shl rax, cl
0039F4F2  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0039F4F7  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0039F4FC  E8 3F 9C FF FF                  call 0x140399140
0039F501  44 0F 20 C6                     mov rsi, cr8
0039F505  44 0F 22 C7                     mov cr8, rdi
0039F509  45 33 DB                        xor r11d, r11d
0039F50C  44 39 1D 0D 78 C2 00            cmp dword ptr [rip + 0xc2780d], r11d
0039F513  0F 85 59 02 00 00               jne 0x14039f772
0039F519  8B CB                           mov ecx, ebx
0039F51B  E8 98 FD FF FF                  call 0x14039f2b8
0039F520  48 8B F8                        mov rdi, rax
0039F523  48 85 FF                        test rdi, rdi
0039F526  0F 84 35 01 00 00               je 0x14039f661
0039F52C  B9 01 00 00 00                  mov ecx, 1
0039F531  BA FF FF 00 00                  mov edx, 0xffff
0039F536  66 01 4F 66                     add word ptr [rdi + 0x66], cx
0039F53A  48 8B DF                        mov rbx, rdi
0039F53D  44 84 F1                        test cl, r14b
0039F540  74 2A                           je 0x14039f56c
0039F542  44 38 5B 5D                     cmp byte ptr [rbx + 0x5d], r11b
0039F546  74 1B                           je 0x14039f563
0039F548  48 8B 5B 08                     mov rbx, qword ptr [rbx + 8]
0039F54C  48 85 DB                        test rbx, rbx
0039F54F  74 0F                           je 0x14039f560
0039F551  48 83 C3 F8                     add rbx, -8
0039F555  48 3B DF                        cmp rbx, rdi
0039F558  75 E8                           jne 0x14039f542
0039F55A  44 38 5B 5D                     cmp byte ptr [rbx + 0x5d], r11b
0039F55E  74 03                           je 0x14039f563
0039F560  49 8B DB                        mov rbx, r11
0039F563  48 85 DB                        test rbx, rbx
0039F566  0F 84 E2 00 00 00               je 0x14039f64e
0039F56C  8B 47 6C                        mov eax, dword ptr [rdi + 0x6c]
0039F56F  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
0039F573  45 8A F3                        mov r14b, r11b
0039F576  45 8B E3                        mov r12d, r11d
0039F579  80 7C 24 40 02                  cmp byte ptr [rsp + 0x40], 2
0039F57E  0F 87 CC 01 00 00               ja 0x14039f750
0039F584  8B 43 68                        mov eax, dword ptr [rbx + 0x68]
0039F587  84 C1                           test cl, al
0039F589  0F 85 F6 01 00 00               jne 0x14039f785
0039F58F  66 01 4B 66                     add word ptr [rbx + 0x66], cx
0039F593  44 03 E1                        add r12d, ecx
0039F596  8B 6C 24 24                     mov ebp, dword ptr [rsp + 0x24]
0039F59A  85 ED                           test ebp, ebp
0039F59C  0F 85 4A 01 00 00               jne 0x14039f6ec
0039F5A2  44 39 1D 77 77 C2 00            cmp dword ptr [rip + 0xc27777], r11d
0039F5A9  74 0C                           je 0x14039f5b7
0039F5AB  44 0F 20 C1                     mov rcx, cr8
0039F5AF  40 8A D6                        mov dl, sil
0039F5B2  E8 E1 60 15 00                  call 0x1404f5698
0039F5B7  40 0F B6 C6                     movzx eax, sil
0039F5BB  44 0F 22 C0                     mov cr8, rax
0039F5BF  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
0039F5C4  40 8A D6                        mov dl, sil
0039F5C7  48 8B CB                        mov rcx, rbx
0039F5CA  E8 11 03 00 00                  call 0x14039f8e0
0039F5CF  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0039F5D3  41 BD 02 00 00 00               mov r13d, 2
0039F5D9  44 0F 20 C6                     mov rsi, cr8
0039F5DD  33 C0                           xor eax, eax
0039F5DF  85 ED                           test ebp, ebp
0039F5E1  0F 84 17 01 00 00               je 0x14039f6fe
0039F5E7  8D 48 0C                        lea ecx, [rax + 0xc]
0039F5EA  44 0F 22 C1                     mov cr8, rcx
0039F5EE  39 05 2C 77 C2 00               cmp dword ptr [rip + 0xc2772c], eax
0039F5F4  0F 85 47 01 00 00               jne 0x14039f741
0039F5FA  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0039F5FF  E8 2C 8E E6 FF                  call 0x140208430
0039F604  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
0039F608  B8 FF FF 00 00                  mov eax, 0xffff
0039F60D  66 01 43 66                     add word ptr [rbx + 0x66], ax
0039F611  4D 8B C7                        mov r8, r15
0039F614  48 8B 6B 08                     mov rbp, qword ptr [rbx + 8]
0039F618  48 8B D3                        mov rdx, rbx
0039F61B  E8 54 FD FF FF                  call 0x14039f374
0039F620  45 33 DB                        xor r11d, r11d
0039F623  41 8D 4B 01                     lea ecx, [r11 + 1]
0039F627  48 8D 5D F8                     lea rbx, [rbp - 8]
0039F62B  40 8A 6C 24 20                  mov bpl, byte ptr [rsp + 0x20]
0039F630  44 39 5C 24 3C                  cmp dword ptr [rsp + 0x3c], r11d
0039F635  0F 85 53 01 00 00               jne 0x14039f78e
0039F63B  40 84 ED                        test bpl, bpl
0039F63E  0F 84 7D 01 00 00               je 0x14039f7c1
0039F644  44 8B 64 24 24                  mov r12d, dword ptr [rsp + 0x24]
0039F649  BA FF FF 00 00                  mov edx, 0xffff
0039F64E  66 01 57 66                     add word ptr [rdi + 0x66], dx
0039F652  8B 47 68                        mov eax, dword ptr [rdi + 0x68]
0039F655  0F B7 4F 66                     movzx ecx, word ptr [rdi + 0x66]
0039F659  A8 02                           test al, 2
0039F65B  0F 85 6E 01 00 00               jne 0x14039f7cf
0039F661  45 85 E4                        test r12d, r12d
0039F664  0F 85 B8 00 00 00               jne 0x14039f722
0039F66A  44 39 1D AF 76 C2 00            cmp dword ptr [rip + 0xc276af], r11d
0039F671  74 0C                           je 0x14039f67f
0039F673  44 0F 20 C1                     mov rcx, cr8
0039F677  40 8A D6                        mov dl, sil
0039F67A  E8 19 60 15 00                  call 0x1404f5698
0039F67F  40 0F B6 C6                     movzx eax, sil
0039F683  44 0F 22 C0                     mov cr8, rax
0039F687  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0039F68C  E8 2F 98 FF FF                  call 0x140398ec0
0039F691  80 7C 24 21 00                  cmp byte ptr [rsp + 0x21], 0
0039F696  74 09                           je 0x14039f6a1
0039F698  8B 4C 24 28                     mov ecx, dword ptr [rsp + 0x28]
0039F69C  E8 BB 01 00 00                  call 0x14039f85c
0039F6A1  80 7C 24 40 02                  cmp byte ptr [rsp + 0x40], 2
0039F6A6  73 08                           jae 0x14039f6b0
0039F6A8  49 8B CF                        mov rcx, r15
0039F6AB  E8 54 01 00 00                  call 0x14039f804
0039F6B0  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0039F6B5  48 85 C0                        test rax, rax
0039F6B8  74 03                           je 0x14039f6bd
0039F6BA  44 89 28                        mov dword ptr [rax], r13d
0039F6BD  40 8A C5                        mov al, bpl
0039F6C0  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0039F6C8  48 33 CC                        xor rcx, rsp
0039F6CB  E8 70 CF 30 00                  call 0x1406ac640
0039F6D0  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
0039F6D8  48 81 C4 90 00 00 00            add rsp, 0x90
0039F6DF  41 5F                           pop r15
0039F6E1  41 5E                           pop r14
0039F6E3  41 5D                           pop r13
0039F6E5  41 5C                           pop r12
0039F6E7  5F                              pop rdi
0039F6E8  5E                              pop rsi
0039F6E9  5D                              pop rbp
0039F6EA  C3                              ret
0039F6EB  CC                              int3
0039F6EC  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0039F6F1  40 8A D6                        mov dl, sil
0039F6F4  E8 5F 25 F3 FF                  call 0x1402d1c58
0039F6F9  E9 C1 FE FF FF                  jmp 0x14039f5bf
0039F6FE  B9 0F 00 00 00                  mov ecx, 0xf
0039F703  44 0F 22 C1                     mov cr8, rcx
0039F707  39 05 13 76 C2 00               cmp dword ptr [rip + 0xc27613], eax
0039F70D  0F 84 F1 FE FF FF               je 0x14039f604
0039F713  8A D1                           mov dl, cl
0039F715  40 8A CE                        mov cl, sil
0039F718  E8 DF 5F 15 00                  call 0x1404f56fc
0039F71D  E9 E2 FE FF FF                  jmp 0x14039f604
0039F722  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0039F727  40 8A D6                        mov dl, sil
0039F72A  E8 29 25 F3 FF                  call 0x1402d1c58
0039F72F  E9 5D FF FF FF                  jmp 0x14039f691
0039F734  40 8A CE                        mov cl, sil
0039F737  E8 C0 5F 15 00                  call 0x1404f56fc
0039F73C  E9 55 FD FF FF                  jmp 0x14039f496
0039F741  8A D1                           mov dl, cl
0039F743  40 8A CE                        mov cl, sil
0039F746  E8 B1 5F 15 00                  call 0x1404f56fc
0039F74B  E9 AA FE FF FF                  jmp 0x14039f5fa
0039F750  44 38 5B 5D                     cmp byte ptr [rbx + 0x5d], r11b
0039F754  0F 85 2A FE FF FF               jne 0x14039f584
0039F75A  8B 43 58                        mov eax, dword ptr [rbx + 0x58]
0039F75D  41 83 FD 02                     cmp r13d, 2
0039F761  88 4C 24 21                     mov byte ptr [rsp + 0x21], cl
0039F765  44 0F 45 E9                     cmovne r13d, ecx
0039F769  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0039F76D  E9 D2 FE FF FF                  jmp 0x14039f644
0039F772  40 8A D7                        mov dl, dil
0039F775  40 8A CE                        mov cl, sil
0039F778  E8 7F 5F 15 00                  call 0x1404f56fc
0039F77D  45 33 DB                        xor r11d, r11d
0039F780  E9 94 FD FF FF                  jmp 0x14039f519
0039F785  48 8B 6B 08                     mov rbp, qword ptr [rbx + 8]
0039F789  E9 99 FE FF FF                  jmp 0x14039f627
0039F78E  40 84 ED                        test bpl, bpl
0039F791  45 0F B6 F6                     movzx r14d, r14b
0039F795  44 0F 45 F1                     cmovne r14d, ecx
0039F799  48 3B DF                        cmp rbx, rdi
0039F79C  0F 85 D7 FD FF FF               jne 0x14039f579
0039F7A2  45 84 F6                        test r14b, r14b
0039F7A5  74 05                           je 0x14039f7ac
0039F7A7  44 3B E1                        cmp r12d, ecx
0039F7AA  77 08                           ja 0x14039f7b4
0039F7AC  40 8A E9                        mov bpl, cl
0039F7AF  E9 90 FE FF FF                  jmp 0x14039f644
0039F7B4  41 8A EB                        mov bpl, r11b
0039F7B7  44 88 5C 24 20                  mov byte ptr [rsp + 0x20], r11b
0039F7BC  E9 B2 FD FF FF                  jmp 0x14039f573
0039F7C1  48 3B DF                        cmp rbx, rdi
0039F7C4  0F 84 7A FE FF FF               je 0x14039f644
0039F7CA  E9 AA FD FF FF                  jmp 0x14039f579
0039F7CF  66 85 C9                        test cx, cx
0039F7D2  0F 85 89 FE FF FF               jne 0x14039f661
0039F7D8  48 8B 9F 90 00 00 00            mov rbx, qword ptr [rdi + 0x90]
0039F7DF  48 8B CF                        mov rcx, rdi
0039F7E2  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
0039F7E6  45 85 E4                        test r12d, r12d
0039F7E9  0F 85 3D 6A 34 00               jne 0x1406e622c
0039F7EF  E8 CC 40 F3 FF                  call 0x1402d38c0
0039F7F4  45 33 DB                        xor r11d, r11d
0039F7F7  E9 35 6A 34 00                  jmp 0x1406e6231
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiInterruptDispatchCommon(int a1, int a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int16 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int8 v_stack_mA7;
    unsigned __int8 v_stack_mA8;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p21;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 10924882)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mA4 = a1;
    a1 = 0;
    v_stack_m90 = a2;
    v_stack_m80 = a5;
    v_stack_m68 = v_xmm0;
    v_stack_m88 = v_cr8;
    v_stack_mA7 = 0;
    v_r15 = v_stack_m68;
    if (a4 != 0) { v_r15 = a4; }
    v_stack_mA8 = 0;
    v_stack_mA0 = 0;
    *(unsigned __int64 *)(v_r15 + 8) = v_r15;
    *(unsigned __int64 *)(v_r15) = v_r15;
    v_stack_m58 = v_xmm0;
    if ((unsigned int)((unsigned int)(a1)) == 0) goto loc_0039F4C0;
    v_rbx = ((unsigned int)(a2) - 256 * 2) + ((unsigned int)(a2) - 256);
    v_rbx = (v_rbx) << (4);
    v_rdi = (*(unsigned __int64 *)(v_rip + 12000195)) + (v_rbx);
    v_stack_m98 = v_rdi;
    if ((*(unsigned int *)(v_rip + 12744848)) != 0) goto loc_0039F734;
loc_0039F496:
    result = KeAcquireSpinLockAtDpcLevel(v_rdi, a1 + 12, a3, a4);
    v_r11 = 0;
    v_rdi = 0;
    if (((unsigned int)((unsigned int)(a2) - 256)) < 256) {
        result = *(unsigned __int64 *)(v_rip + 12000114);
        v_rdi = *(unsigned __int64 *)(v_rbx + result * 1 + 40);
    }
    goto loc_0039F523;
loc_0039F4C0:
    v_stack_m98 = v_rdi;
    v_stack_m78 = v_xmm0;
    v_stack_m70 = (unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 208));
    result = (1) << ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 209)));
    v_stack_m78 = result;
    result = KeSetSystemGroupAffinityThread(v_stack_m78, v_stack_m58, a3, a4);
    v_r11 = 0;
    if ((*(unsigned int *)(v_rip + 12744717)) != 0) goto loc_0039F772;
loc_0039F519:
    result = KiGetInterruptObjectFromVector((unsigned int)((unsigned int)(v_rbx)), v_stack_m58, a3, a4);
loc_0039F523:
    if (result == 0) goto loc_0039F661;
    if (((1) & ((unsigned __int8)((unsigned int)(a3)))) == 0) goto loc_0039F56C;
loc_0039F542:
    if ((*(unsigned __int8 *)(result + 93)) == 0) goto loc_0039F563;
    if (*(unsigned __int64 *)(result + 8) == 0) goto loc_0039F560;
    v_rbx = (*(unsigned __int64 *)(result + 8)) + (-8);
    if (v_rbx != result) goto loc_0039F542;
    if ((*(unsigned __int8 *)(v_rbx + 93)) != 0) {
        v_rbx = 0;
    }
    if (v_rbx == 0) goto loc_0039F64E;
loc_0039F56C:
    v_stack_m8C = (unsigned int)((unsigned int)(*(unsigned int *)(result + 108)));
loc_0039F573:
loc_0039F579:
    if (v_stack_m88 > 2) goto loc_0039F750;
loc_0039F584:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 104))))) != 0) goto loc_0039F785;
    v_r12 = (unsigned int)((0) + (1));
    if ((unsigned int)((unsigned int)(v_stack_mA4)) != 0) goto loc_0039F6EC;
    result = (unsigned int)(*(unsigned int *)(v_rbx + 104));
    if ((*(unsigned int *)(v_rip + 12744567)) != 0) {
        a1 = v_rdi;
        a2 = (unsigned __int8)(a1 + 12);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_0039F5BF:
    result = KiInvokeInterruptServiceRoutine(v_rbx, (unsigned __int8)(a1 + 12), (unsigned int)(v_stack_m90), a4);
    v_stack_mA8 = (unsigned __int8)(result);
    result = 0;
    if ((unsigned int)((unsigned int)(v_stack_mA4)) == 0) goto loc_0039F6FE;
    if ((*(unsigned int *)(v_rip + 12744492)) != 0) goto loc_0039F741;
loc_0039F5FA:
    result = KeAcquireSpinLockAtDpcLevel(v_stack_m98, (unsigned __int8)(a1 + 12), (unsigned int)(v_stack_m90), a4);
loc_0039F604:
    result = KiProcessPendingDisconnect((unsigned int)(v_stack_mA4), v_rbx, v_r15, a4);
    v_r11 = 0;
loc_0039F627:
    if (v_stack_m8C != 0) goto loc_0039F78E;
    if ((unsigned __int8)(v_stack_mA8) == 0) goto loc_0039F7C1;
loc_0039F644:
loc_0039F64E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 104)))) & (2)) != 0) goto loc_0039F7CF;
loc_0039F661:
    if ((unsigned int)((unsigned int)(v_stack_mA4)) != 0) goto loc_0039F722;
    result = (unsigned int)(*(unsigned int *)(result + 104));
    if ((*(unsigned int *)(v_rip + 12744367)) != 0) {
        a1 = result + 12;
        a2 = (unsigned __int8)((unsigned __int8)(a1 + 12));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_r15, a4);
    }
    result = KeRevertToUserGroupAffinityThread(v_stack_m58, a2, v_r15, a4);
loc_0039F691:
    if (v_stack_mA7 != 0) {
        a1 = v_stack_mA0;
        result = IoProcessPassiveInterrupts(a1, a2, v_r15, a4);
    }
    if (v_stack_m88 < 2) {
        a1 = v_r15;
        result = KiProcessDisconnectList(a1, a2, v_r15, a4);
    }
    if (v_stack_m80 != 0) {
        *(unsigned int *)(v_stack_m80) = 2;
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_r15, a4);
    v_rsp = (v_rsp) + (144);
    return result;
loc_0039F6EC:
    result = HalpReleaseHighLevelLock(v_stack_p30, (unsigned __int8)((unsigned __int8)(a1 + 12)), v_r15, a4);
    goto loc_0039F5BF;
loc_0039F6FE:
    if ((*(unsigned int *)(v_rip + 12744211)) == ((unsigned int)(result))) goto loc_0039F604;
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)(a1 + 12)), 15, v_r15, a4);
    goto loc_0039F604;
loc_0039F722:
    result = HalpReleaseHighLevelLock(v_stack_p30, (unsigned __int8)((unsigned __int8)(a1 + 12)), v_r15, a4);
    goto loc_0039F691;
loc_0039F734:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)(a1 + 12)), (unsigned __int8)((unsigned __int8)(a1 + 12)), v_r15, a4);
    goto loc_0039F496;
loc_0039F741:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)(a1 + 12)), (unsigned __int8)((unsigned __int8)((unsigned __int8)(a1 + 12))), v_r15, a4);
    goto loc_0039F5FA;
loc_0039F750:
    if ((*(unsigned __int8 *)(v_stack_p8 + 93)) != 0) goto loc_0039F584;
    v_stack_p21 = (unsigned __int8)((unsigned __int8)((unsigned __int8)(a1 + 12)));
    v_r13 = 2;
    if (2 != 2) { v_r13 = (unsigned int)((unsigned __int8)((unsigned __int8)(a1 + 12))); }
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 88)));
    goto loc_0039F644;
loc_0039F772:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)(a1 + 12)), (unsigned __int8)(result), v_r15, a4);
    v_r11 = 0;
    goto loc_0039F519;
loc_0039F785:
    goto loc_0039F627;
loc_0039F78E:
    v_r14 = 0;
    if ((unsigned __int8)(*(unsigned __int64 *)(v_stack_p8 + 8)) != 0) { v_r14 = (unsigned int)((unsigned __int8)((unsigned __int8)(a1 + 12))); }
    if (v_stack_p8 != result) goto loc_0039F579;
    if ((unsigned __int8)(v_r14) == 0) goto loc_0039F7AC;
    if (((unsigned int)((unsigned int)(v_stack_mA4))) > ((unsigned int)((unsigned __int8)((unsigned __int8)(a1 + 12))))) goto loc_0039F7B4;
loc_0039F7AC:
    goto loc_0039F644;
loc_0039F7B4:
    v_stack_p20 = 0;
    goto loc_0039F573;
loc_0039F7C1:
    if (v_stack_p8 == result) goto loc_0039F644;
    goto loc_0039F579;
loc_0039F7CF:
    if ((unsigned __int16)((unsigned __int8)((unsigned __int8)(a1 + 12))) != 0) goto loc_0039F661;
    result = KiDisconnectInterruptInternal(result, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 144) + 8), v_r15, a4);
    v_r11 = 0;
}
```

## 5. (Beta) C Style

```c
int64_t KiInterruptDispatchCommon(int32_t Arg1, void *Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint16_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint8_t v_stack_mA7;
    uint8_t v_stack_mA8;
    uint8_t v_stack_p20;
    uint8_t v_stack_p21;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0xA6B352)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mA4 = Arg1;
    Arg1 = 0;
    v_stack_m90 = Arg2;
    v_stack_m80 = Arg5;
    v_stack_m68 = v_xmm0;
    v_stack_m88 = v_cr8;
    v_stack_mA7 = 0;
    local_r15 = v_stack_m68;
    if (Arg4 != 0) { local_r15 = Arg4; }
    v_stack_mA8 = 0;
    v_stack_mA0 = 0;
    *(uint64_t *)(local_r15 + 0x8) = local_r15;
    *(uint64_t *)(local_r15) = local_r15;
    v_stack_m58 = v_xmm0;
    if ((uint32_t)((uint32_t)(Arg1)) == 0) goto loc_0039F4C0;
    local_rbx = ((uint32_t)(Arg2) - 256 * 2) + ((uint32_t)(Arg2) - 256);
    local_rbx = (local_rbx) << (4);
    local_rdi = (*(uint64_t *)(v_rip + 0xB71BC3)) + (local_rbx);
    v_stack_m98 = local_rdi;
    if ((*(uint32_t *)(v_rip + 0xC27890)) != 0) goto loc_0039F734;
loc_0039F496:
    result = KeAcquireSpinLockAtDpcLevel(local_rdi, Arg1 + 12, Arg3, Arg4);
    local_r11 = 0;
    local_rdi = 0;
    if (((uint32_t)((uint32_t)(Arg2) - 256)) < 256) {
        result = *(uint64_t *)(v_rip + 0xB71B72);
        local_rdi = *(uint64_t *)(local_rbx + result * 1 + 0x28);
    }
    goto loc_0039F523;
loc_0039F4C0:
    v_stack_m98 = local_rdi;
    v_stack_m78 = v_xmm0;
    v_stack_m70 = (uint16_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD0));
    result = (1) << ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD1)));
    v_stack_m78 = result;
    result = KeSetSystemGroupAffinityThread(v_stack_m78, v_stack_m58, Arg3, Arg4);
    local_r11 = 0;
    if ((*(uint32_t *)(v_rip + 0xC2780D)) != 0) goto loc_0039F772;
loc_0039F519:
    result = KiGetInterruptObjectFromVector((uint32_t)((uint32_t)(local_rbx)), v_stack_m58, Arg3, Arg4);
loc_0039F523:
    if (result == 0) goto loc_0039F661;
    if (((1) & ((uint8_t)((uint32_t)(Arg3)))) == 0) goto loc_0039F56C;
loc_0039F542:
    if ((*(uint8_t *)(result + 0x5D)) == 0) goto loc_0039F563;
    if (*(uint64_t *)(result + 0x8) == 0) goto loc_0039F560;
    local_rbx = (*(uint64_t *)(result + 0x8)) + (-8);
    if (local_rbx != result) goto loc_0039F542;
    if ((*(uint8_t *)(local_rbx + 0x5D)) != 0) {
        local_rbx = 0;
    }
    if (local_rbx == 0) goto loc_0039F64E;
loc_0039F56C:
    v_stack_m8C = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x6C)));
loc_0039F573:
loc_0039F579:
    if (v_stack_m88 > 2) goto loc_0039F750;
loc_0039F584:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x68))))) != 0) goto loc_0039F785;
    local_r12 = (uint32_t)((0) + (1));
    if ((uint32_t)((uint32_t)(v_stack_mA4)) != 0) goto loc_0039F6EC;
    result = (uint32_t)(*(uint32_t *)(local_rbx + 0x68));
    if ((*(uint32_t *)(v_rip + 0xC27777)) != 0) {
        Arg1 = local_rdi;
        Arg2 = (uint8_t)(Arg1 + 12);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
loc_0039F5BF:
    result = KiInvokeInterruptServiceRoutine(local_rbx, (uint8_t)(Arg1 + 12), (uint32_t)(v_stack_m90), Arg4);
    v_stack_mA8 = (uint8_t)(result);
    result = 0;
    if ((uint32_t)((uint32_t)(v_stack_mA4)) == 0) goto loc_0039F6FE;
    if ((*(uint32_t *)(v_rip + 0xC2772C)) != 0) goto loc_0039F741;
loc_0039F5FA:
    result = KeAcquireSpinLockAtDpcLevel(v_stack_m98, (uint8_t)(Arg1 + 12), (uint32_t)(v_stack_m90), Arg4);
loc_0039F604:
    result = KiProcessPendingDisconnect((uint32_t)(v_stack_mA4), local_rbx, local_r15, Arg4);
    local_r11 = 0;
loc_0039F627:
    if (v_stack_m8C != 0) goto loc_0039F78E;
    if ((uint8_t)(v_stack_mA8) == 0) goto loc_0039F7C1;
loc_0039F644:
loc_0039F64E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x68)))) & (2)) != 0) goto loc_0039F7CF;
loc_0039F661:
    if ((uint32_t)((uint32_t)(v_stack_mA4)) != 0) goto loc_0039F722;
    result = (uint32_t)(*(uint32_t *)(result + 0x68));
    if ((*(uint32_t *)(v_rip + 0xC276AF)) != 0) {
        Arg1 = result + 12;
        Arg2 = (uint8_t)((uint8_t)(Arg1 + 12));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, local_r15, Arg4);
    }
    result = KeRevertToUserGroupAffinityThread(v_stack_m58, Arg2, local_r15, Arg4);
loc_0039F691:
    if (v_stack_mA7 != 0) {
        Arg1 = v_stack_mA0;
        result = IoProcessPassiveInterrupts(Arg1, Arg2, local_r15, Arg4);
    }
    if (v_stack_m88 < 2) {
        Arg1 = local_r15;
        result = KiProcessDisconnectList(Arg1, Arg2, local_r15, Arg4);
    }
    if (v_stack_m80 != 0) {
        *(uint32_t *)(v_stack_m80) = 2;
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, local_r15, Arg4);
    local_rsp = (local_rsp) + (144);
    return result;
loc_0039F6EC:
    result = HalpReleaseHighLevelLock(v_stack_p30, (uint8_t)((uint8_t)(Arg1 + 12)), local_r15, Arg4);
    goto loc_0039F5BF;
loc_0039F6FE:
    if ((*(uint32_t *)(v_rip + 0xC27613)) == ((uint32_t)(result))) goto loc_0039F604;
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)(Arg1 + 12)), 15, local_r15, Arg4);
    goto loc_0039F604;
loc_0039F722:
    result = HalpReleaseHighLevelLock(v_stack_p30, (uint8_t)((uint8_t)(Arg1 + 12)), local_r15, Arg4);
    goto loc_0039F691;
loc_0039F734:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)(Arg1 + 12)), (uint8_t)((uint8_t)(Arg1 + 12)), local_r15, Arg4);
    goto loc_0039F496;
loc_0039F741:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)(Arg1 + 12)), (uint8_t)((uint8_t)((uint8_t)(Arg1 + 12))), local_r15, Arg4);
    goto loc_0039F5FA;
loc_0039F750:
    if ((*(uint8_t *)(v_stack_p8 + 0x5D)) != 0) goto loc_0039F584;
    v_stack_p21 = (uint8_t)((uint8_t)((uint8_t)(Arg1 + 12)));
    local_r13 = 2;
    if (2 != 2) { local_r13 = (uint32_t)((uint8_t)((uint8_t)(Arg1 + 12))); }
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58)));
    goto loc_0039F644;
loc_0039F772:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)(Arg1 + 12)), (uint8_t)(result), local_r15, Arg4);
    local_r11 = 0;
    goto loc_0039F519;
loc_0039F785:
    goto loc_0039F627;
loc_0039F78E:
    local_r14 = 0;
    if ((uint8_t)(*(uint64_t *)(v_stack_p8 + 0x8)) != 0) { local_r14 = (uint32_t)((uint8_t)((uint8_t)(Arg1 + 12))); }
    if (v_stack_p8 != result) goto loc_0039F579;
    if ((uint8_t)(local_r14) == 0) goto loc_0039F7AC;
    if (((uint32_t)((uint32_t)(v_stack_mA4))) > ((uint32_t)((uint8_t)((uint8_t)(Arg1 + 12))))) goto loc_0039F7B4;
loc_0039F7AC:
    goto loc_0039F644;
loc_0039F7B4:
    v_stack_p20 = 0;
    goto loc_0039F573;
loc_0039F7C1:
    if (v_stack_p8 == result) goto loc_0039F644;
    goto loc_0039F579;
loc_0039F7CF:
    if ((uint16_t)((uint8_t)((uint8_t)(Arg1 + 12))) != 0) goto loc_0039F661;
    result = KiDisconnectInterruptInternal(result, *(uint64_t *)(*(uint64_t *)(result + 0x90) + 0x8), local_r15, Arg4);
    local_r11 = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x100` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0039F3D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
