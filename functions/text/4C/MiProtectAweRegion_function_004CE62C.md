# MiProtectAweRegion

- RVA: `0x004CE62C`–`0x004CEE33` (길이 `2,055` bytes)
- VA: `0x00000001404CE62C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BDA64`
- 디코드: `528`개 명령, `2,055/2,055` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004CE6D3` → [MiLockAweVadsShared](MiLockAweVadsShared_function_004CEE3C.md) (function, `0x004CEE3C`)
- `0x004CE6DE` → [MiGetAweNode](../4F/MiGetAweNode_function_004F600C.md) (function, `0x004F600C`)
- `0x004CE719` → [MiGetVadCacheAttribute](../4A/MiGetVadCacheAttribute_function_004AF624.md) (function, `0x004AF624`)
- `0x004CE797` → [MI_GET_GRAPHICS_PROTECTION_FROM_VAD](../43/MI_GET_GRAPHICS_PROTECTION_FROM_VAD_function_00438CA0.md) (function, `0x00438CA0`)
- `0x004CE815` → [MiUnlockAwePagesShared](MiUnlockAwePagesShared_function_004C66C4.md) (function, `0x004C66C4`)
- `0x004CE848` → [MiUnlockAwePagesShared](MiUnlockAwePagesShared_function_004C66C4.md) (function, `0x004C66C4`)
- `0x004CE87C` → [MiGetAweViewPageSize](MiGetAweViewPageSize_function_004C51AC.md) (function, `0x004C51AC`)
- `0x004CE893` → [MiPageSizeToPteLevel](../41/MiPageSizeToPteLevel_function_0041F57C.md) (function, `0x0041F57C`)
- `0x004CE94D` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x004CE98F` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x004CE994` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x004CE9C6` → [MiFlushGraphicsPtes](../4E/MiFlushGraphicsPtes_function_004E1374.md) (function, `0x004E1374`)
- `0x004CE9D8` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004CE9E4` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x004CE9EE` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x004CEA06` → [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) (function, `0x00280D10`)
- `0x004CEA81` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x004CEB1F` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x004CEB66` → [MiCaptureWriteWatchDirtyBit](../46/MiCaptureWriteWatchDirtyBit_function_00465224.md) (function, `0x00465224`)
- `0x004CEBBC` → [MiMakeTransitionPte](../36/MiMakeTransitionPte_function_00363F70.md) (function, `0x00363F70`)
- `0x004CEBDE` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x004CEC00` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x004CEC15` → [MiMakeValidPte](../2C/MiMakeValidPte_function_002C5590.md) (function, `0x002C5590`)
- `0x004CEC27` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x004CEC54` → [MiRewritePteWithLockBit](../32/MiRewritePteWithLockBit_function_00322FEC.md) (function, `0x00322FEC`)
- `0x004CEC8D` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x004CEC9C` → [MiInsertLargeTbFlushEntry](../37/MiInsertLargeTbFlushEntry_function_0037827C.md) (function, `0x0037827C`)
- `0x004CECEC` → [MiMakeTransitionPteValid](../28/MiMakeTransitionPteValid_function_00283D60.md) (function, `0x00283D60`)
- `0x004CED10` → [MiPteInShadowRange](../23/MiPteInShadowRange_function_0023FB00.md) (function, `0x0023FB00`)
- `0x004CED21` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x004CED6B` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x004CED7D` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)
- `0x004CEDB7` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x004CEDBC` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x004CEDE9` → [MiFlushGraphicsPtes](../4E/MiFlushGraphicsPtes_function_004E1374.md) (function, `0x004E1374`)
- `0x004CEDF6` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004CEE02` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)

### Direct callers
- [MmProtectVirtualMemory](../../page/88/MmProtectVirtualMemory_function_00881050.md) at `0x0088183E`

### Static image references
- `0x004CED30` → RVA `0x00FC6A88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004CE62C  48 8B C4                        mov rax, rsp
004CE62F  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
004CE633  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
004CE637  55                              push rbp
004CE638  56                              push rsi
004CE639  57                              push rdi
004CE63A  41 54                           push r12
004CE63C  41 55                           push r13
004CE63E  41 56                           push r14
004CE640  41 57                           push r15
004CE642  48 81 EC D0 00 00 00            sub rsp, 0xd0
004CE649  48 83 60 88 00                  and qword ptr [rax - 0x78], 0
004CE64E  33 FF                           xor edi, edi
004CE650  65 48 8B 2C 25 88 01 00 00      mov rbp, qword ptr gs:[0x188]
004CE659  33 C0                           xor eax, eax
004CE65B  21 44 24 4C                     and dword ptr [rsp + 0x4c], eax
004CE65F  4C 8B E2                        mov r12, rdx
004CE662  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
004CE667  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
004CE671  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
004CE676  48 8B F9                        mov rdi, rcx
004CE679  48 8B 85 B8 00 00 00            mov rax, qword ptr [rbp + 0xb8]
004CE680  48 8B D9                        mov rbx, rcx
004CE683  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
004CE68B  41 8B F1                        mov esi, r9d
004CE68E  48 05 00 04 00 00               add rax, 0x400
004CE694  48 C1 EF 09                     shr rdi, 9
004CE698  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004CE69D  45 8B E8                        mov r13d, r8d
004CE6A0  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
004CE6A8  48 23 FA                        and rdi, rdx
004CE6AB  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
004CE6B5  48 8B C1                        mov rax, rcx
004CE6B8  49 C1 EC 09                     shr r12, 9
004CE6BC  48 03 F8                        add rdi, rax
004CE6BF  4C 23 E2                        and r12, rdx
004CE6C2  48 8B C1                        mov rax, rcx
004CE6C5  4C 03 E0                        add r12, rax
004CE6C8  48 8B CD                        mov rcx, rbp
004CE6CB  4C 89 A4 24 18 01 00 00         mov qword ptr [rsp + 0x118], r12
004CE6D3  E8 64 07 00 00                  call 0x1404cee3c
004CE6D8  48 8B CB                        mov rcx, rbx
004CE6DB  4C 8B D8                        mov r11, rax
004CE6DE  E8 29 79 02 00                  call 0x1404f600c
004CE6E3  41 B9 18 00 00 00               mov r9d, 0x18
004CE6E9  4C 8B F8                        mov r15, rax
004CE6EC  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
004CE6F0  4C 8B 70 20                     mov r14, qword ptr [rax + 0x20]
004CE6F4  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
004CE6FC  C6 40 40 00                     mov byte ptr [rax + 0x40], 0
004CE700  45 3B E9                        cmp r13d, r9d
004CE703  74 43                           je 0x1404ce748
004CE705  41 83 E5 07                     and r13d, 7
004CE709  41 83 FD 01                     cmp r13d, 1
004CE70D  74 0A                           je 0x1404ce719
004CE70F  41 83 FD 04                     cmp r13d, 4
004CE713  0F 85 F6 00 00 00               jne 0x1404ce80f
004CE719  E8 06 0F FE FF                  call 0x1404af624
004CE71E  44 8B C0                        mov r8d, eax
004CE721  85 C0                           test eax, eax
004CE723  75 06                           jne 0x1404ce72b
004CE725  41 8D 40 08                     lea eax, [r8 + 8]
004CE729  EB 0A                           jmp 0x1404ce735
004CE72B  33 C0                           xor eax, eax
004CE72D  41 83 F8 02                     cmp r8d, 2
004CE731  41 0F 44 C1                     cmove eax, r9d
004CE735  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
004CE73D  44 0B E8                        or r13d, eax
004CE740  44 89 AC 24 20 01 00 00         mov dword ptr [rsp + 0x120], r13d
004CE748  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
004CE74C  48 8D 59 30                     lea rbx, [rcx + 0x30]
004CE750  BA 01 00 00 00                  mov edx, 1
004CE755  84 C2                           test dl, al
004CE757  74 0D                           je 0x1404ce766
004CE759  C7 44 24 58 04 00 00 00         mov dword ptr [rsp + 0x58], 4
004CE761  E9 DC 00 00 00                  jmp 0x1404ce842
004CE766  44 8B 0B                        mov r9d, dword ptr [rbx]
004CE769  45 8B E1                        mov r12d, r9d
004CE76C  41 C1 EC 07                     shr r12d, 7
004CE770  41 83 E4 1F                     and r12d, 0x1f
004CE774  41 8B C4                        mov eax, r12d
004CE777  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
004CE77C  24 07                           and al, 7
004CE77E  3A C2                           cmp al, dl
004CE780  75 0D                           jne 0x1404ce78f
004CE782  41 8B C5                        mov eax, r13d
004CE785  24 07                           and al, 7
004CE787  3A C2                           cmp al, dl
004CE789  0F 85 80 00 00 00               jne 0x1404ce80f
004CE78F  85 F6                           test esi, esi
004CE791  0F 84 92 00 00 00               je 0x1404ce829
004CE797  E8 04 A5 F6 FF                  call 0x140438ca0
004CE79C  44 8B C0                        mov r8d, eax
004CE79F  B9 00 00 02 00                  mov ecx, 0x20000
004CE7A4  8B C6                           mov eax, esi
004CE7A6  23 C1                           and eax, ecx
004CE7A8  44 85 C1                        test ecx, r8d
004CE7AB  74 06                           je 0x1404ce7b3
004CE7AD  85 C0                           test eax, eax
004CE7AF  75 06                           jne 0x1404ce7b7
004CE7B1  EB 5C                           jmp 0x1404ce80f
004CE7B3  85 C0                           test eax, eax
004CE7B5  75 58                           jne 0x1404ce80f
004CE7B7  B9 00 00 04 00                  mov ecx, 0x40000
004CE7BC  8B C6                           mov eax, esi
004CE7BE  23 C1                           and eax, ecx
004CE7C0  44 85 C1                        test ecx, r8d
004CE7C3  74 06                           je 0x1404ce7cb
004CE7C5  85 C0                           test eax, eax
004CE7C7  75 06                           jne 0x1404ce7cf
004CE7C9  EB 44                           jmp 0x1404ce80f
004CE7CB  85 C0                           test eax, eax
004CE7CD  75 40                           jne 0x1404ce80f
004CE7CF  41 81 E0 FF FF F9 FF            and r8d, 0xfff9ffff
004CE7D6  B8 00 C0 01 00                  mov eax, 0x1c000
004CE7DB  44 85 C0                        test eax, r8d
004CE7DE  0F 94 C1                        sete cl
004CE7E1  85 F0                           test eax, esi
004CE7E3  0F 95 C0                        setne al
004CE7E6  84 C8                           test al, cl
004CE7E8  75 25                           jne 0x1404ce80f
004CE7EA  B8 00 20 01 00                  mov eax, 0x12000
004CE7EF  44 85 C0                        test eax, r8d
004CE7F2  0F 94 C2                        sete dl
004CE7F5  85 F0                           test eax, esi
004CE7F7  0F 95 C0                        setne al
004CE7FA  84 D0                           test al, dl
004CE7FC  75 11                           jne 0x1404ce80f
004CE7FE  41 81 F8 00 08 00 00            cmp r8d, 0x800
004CE805  75 1D                           jne 0x1404ce824
004CE807  F7 C6 FF F7 F9 FF               test esi, 0xfff9f7ff
004CE80D  74 15                           je 0x1404ce824
004CE80F  49 8B D3                        mov rdx, r11
004CE812  48 8B CD                        mov rcx, rbp
004CE815  E8 AA 7E FF FF                  call 0x1404c66c4
004CE81A  B8 18 00 00 C0                  mov eax, 0xc0000018
004CE81F  E9 F3 05 00 00                  jmp 0x1404cee17
004CE824  BA 01 00 00 00                  mov edx, 1
004CE829  4C 8B A4 24 18 01 00 00         mov r12, qword ptr [rsp + 0x118]
004CE831  B8 00 00 20 04                  mov eax, 0x4200000
004CE836  44 23 C8                        and r9d, eax
004CE839  44 3B C8                        cmp r9d, eax
004CE83C  75 04                           jne 0x1404ce842
004CE83E  89 54 24 4C                     mov dword ptr [rsp + 0x4c], edx
004CE842  49 8B D3                        mov rdx, r11
004CE845  48 8B CD                        mov rcx, rbp
004CE848  E8 77 7E FF FF                  call 0x1404c66c4
004CE84D  8B 0B                           mov ecx, dword ptr [rbx]
004CE84F  BA 00 00 60 00                  mov edx, 0x600000
004CE854  4D 8B 56 10                     mov r10, qword ptr [r14 + 0x10]
004CE858  23 CA                           and ecx, edx
004CE85A  8B C1                           mov eax, ecx
004CE85C  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
004CE860  2B C2                           sub eax, edx
004CE862  4C 89 54 24 70                  mov qword ptr [rsp + 0x70], r10
004CE867  F7 D8                           neg eax
004CE869  49 8B CF                        mov rcx, r15
004CE86C  45 1B C9                        sbb r9d, r9d
004CE86F  33 C0                           xor eax, eax
004CE871  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
004CE875  41 81 E1 00 00 00 80            and r9d, 0x80000000
004CE87C  E8 2B 69 FF FF                  call 0x1404c51ac
004CE881  48 85 C0                        test rax, rax
004CE884  49 8B CA                        mov rcx, r10
004CE887  48 0F 45 C8                     cmovne rcx, rax
004CE88B  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
004CE893  E8 E4 0C F5 FF                  call 0x14041f57c
004CE898  41 B8 01 00 00 00               mov r8d, 1
004CE89E  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
004CE8A2  8B E8                           mov ebp, eax
004CE8A4  41 3B C0                        cmp eax, r8d
004CE8A7  7C 0C                           jl 0x1404ce8b5
004CE8A9  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
004CE8AE  41 0F BA E9 1A                  bts r9d, 0x1a
004CE8B3  EB 05                           jmp 0x1404ce8ba
004CE8B5  4C 89 54 24 78                  mov qword ptr [rsp + 0x78], r10
004CE8BA  44 89 4C 24 48                  mov dword ptr [rsp + 0x48], r9d
004CE8BF  4D 3B D0                        cmp r10, r8
004CE8C2  74 33                           je 0x1404ce8f7
004CE8C4  33 D2                           xor edx, edx
004CE8C6  48 8B C7                        mov rax, rdi
004CE8C9  48 C1 E8 03                     shr rax, 3
004CE8CD  25 FF 01 00 00                  and eax, 0x1ff
004CE8D2  48 F7 F1                        div rcx
004CE8D5  48 85 D2                        test rdx, rdx
004CE8D8  0F 85 3C FF FF FF               jne 0x1404ce81a
004CE8DE  49 8B C4                        mov rax, r12
004CE8E1  48 2B C7                        sub rax, rdi
004CE8E4  48 C1 F8 03                     sar rax, 3
004CE8E8  49 03 C0                        add rax, r8
004CE8EB  48 F7 F1                        div rcx
004CE8EE  48 85 D2                        test rdx, rdx
004CE8F1  0F 85 23 FF FF FF               jne 0x1404ce81a
004CE8F7  8B CD                           mov ecx, ebp
004CE8F9  85 ED                           test ebp, ebp
004CE8FB  74 3B                           je 0x1404ce938
004CE8FD  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
004CE907  49 B9 F8 FF FF FF 7F 00 00 00   movabs r9, 0x7ffffffff8
004CE911  48 C1 EF 09                     shr rdi, 9
004CE915  49 23 F9                        and rdi, r9
004CE918  48 8B C2                        mov rax, rdx
004CE91B  49 C1 EC 09                     shr r12, 9
004CE91F  48 03 F8                        add rdi, rax
004CE922  4D 23 E1                        and r12, r9
004CE925  48 8B C2                        mov rax, rdx
004CE928  4C 03 E0                        add r12, rax
004CE92B  41 2B C8                        sub ecx, r8d
004CE92E  75 E1                           jne 0x1404ce911
004CE930  4C 89 A4 24 18 01 00 00         mov qword ptr [rsp + 0x118], r12
004CE938  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
004CE93D  45 33 E4                        xor r12d, r12d
004CE940  33 F6                           xor esi, esi
004CE942  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
004CE94A  4C 8B F7                        mov r14, rdi
004CE94D  E8 9E E2 DA FF                  call 0x14027cbf0
004CE952  8A D8                           mov bl, al
004CE954  88 84 24 10 01 00 00            mov byte ptr [rsp + 0x110], al
004CE95B  48 3B BC 24 18 01 00 00         cmp rdi, qword ptr [rsp + 0x118]
004CE963  0F 87 92 04 00 00               ja 0x1404cedfb
004CE969  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
004CE96E  8B D6                           mov edx, esi
004CE970  48 85 D2                        test rdx, rdx
004CE973  74 0D                           je 0x1404ce982
004CE975  48 F7 C7 FF 0F 00 00            test rdi, 0xfff
004CE97C  0F 85 CA 00 00 00               jne 0x1404cea4c
004CE982  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
004CE987  48 85 C0                        test rax, rax
004CE98A  74 19                           je 0x1404ce9a5
004CE98C  48 8B C8                        mov rcx, rax
004CE98F  E8 2C 36 E4 FF                  call 0x140311fc0
004CE994  E8 D7 52 E4 FF                  call 0x140313c70
004CE999  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
004CE99E  33 C0                           xor eax, eax
004CE9A0  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
004CE9A5  48 85 D2                        test rdx, rdx
004CE9A8  74 49                           je 0x1404ce9f3
004CE9AA  4D 85 E4                        test r12, r12
004CE9AD  74 24                           je 0x1404ce9d3
004CE9AF  83 7C 24 4C 00                  cmp dword ptr [rsp + 0x4c], 0
004CE9B4  74 1A                           je 0x1404ce9d0
004CE9B6  48 8B D6                        mov rdx, rsi
004CE9B9  49 8B CC                        mov rcx, r12
004CE9BC  49 2B D4                        sub rdx, r12
004CE9BF  48 C1 FA 03                     sar rdx, 3
004CE9C3  48 FF C2                        inc rdx
004CE9C6  E8 A9 29 01 00                  call 0x1404e1374
004CE9CB  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
004CE9D0  45 33 E4                        xor r12d, r12d
004CE9D3  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
004CE9D8  E8 E3 84 D4 FF                  call 0x140216ec0
004CE9DD  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
004CE9E2  8A D3                           mov dl, bl
004CE9E4  E8 A7 EC DA FF                  call 0x14027d690
004CE9E9  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
004CE9EE  E8 FD E1 DA FF                  call 0x14027cbf0
004CE9F3  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
004CE9F8  4C 8D 84 24 90 00 00 00         lea r8, [rsp + 0x90]
004CEA00  45 33 C9                        xor r9d, r9d
004CEA03  48 8B D7                        mov rdx, rdi
004CEA06  E8 05 23 DB FF                  call 0x140280d10
004CEA0B  48 8B D0                        mov rdx, rax
004CEA0E  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
004CEA13  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
004CEA1D  48 8B CF                        mov rcx, rdi
004CEA20  48 C1 E9 09                     shr rcx, 9
004CEA24  48 23 C8                        and rcx, rax
004CEA27  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
004CEA31  48 8B C0                        mov rax, rax
004CEA34  48 03 C8                        add rcx, rax
004CEA37  48 3B D1                        cmp rdx, rcx
004CEA3A  74 10                           je 0x1404cea4c
004CEA3C  48 83 E7 F8                     and rdi, 0xfffffffffffffff8
004CEA40  48 81 CF F8 0F 00 00            or rdi, 0xff8
004CEA47  E9 4C 03 00 00                  jmp 0x1404ced98
004CEA4C  81 7C 24 44 00 00 60 00         cmp dword ptr [rsp + 0x44], 0x600000
004CEA54  75 28                           jne 0x1404cea7e
004CEA56  B8 01 00 00 00                  mov eax, 1
004CEA5B  48 39 44 24 78                  cmp qword ptr [rsp + 0x78], rax
004CEA60  74 16                           je 0x1404cea78
004CEA62  33 D2                           xor edx, edx
004CEA64  48 8B C7                        mov rax, rdi
004CEA67  48 C1 E8 03                     shr rax, 3
004CEA6B  25 FF 01 00 00                  and eax, 0x1ff
004CEA70  49 F7 F7                        div r15
004CEA73  48 85 D2                        test rdx, rdx
004CEA76  75 06                           jne 0x1404cea7e
004CEA78  33 C0                           xor eax, eax
004CEA7A  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
004CEA7E  48 8B CF                        mov rcx, rdi
004CEA81  E8 1A 3E DB FF                  call 0x1402828a0
004CEA86  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
004CEA8E  48 8B D8                        mov rbx, rax
004CEA91  48 85 C0                        test rax, rax
004CEA94  0F 84 F2 02 00 00               je 0x1404ced8c
004CEA9A  41 B8 01 00 00 00               mov r8d, 1
004CEAA0  41 84 D8                        test r8b, bl
004CEAA3  0F 84 FD 01 00 00               je 0x1404ceca6
004CEAA9  4D 85 E4                        test r12, r12
004CEAAC  48 8B F7                        mov rsi, rdi
004CEAAF  4C 0F 44 E7                     cmove r12, rdi
004CEAB3  49 3B FE                        cmp rdi, r14
004CEAB6  75 42                           jne 0x1404ceafa
004CEAB8  8B 54 24 58                     mov edx, dword ptr [rsp + 0x58]
004CEABC  25 00 08 00 00                  and eax, 0x800
004CEAC1  48 F7 D8                        neg rax
004CEAC4  8B C2                           mov eax, edx
004CEAC6  1B C9                           sbb ecx, ecx
004CEAC8  C1 E8 03                        shr eax, 3
004CEACB  83 E1 02                        and ecx, 2
004CEACE  83 C1 02                        add ecx, 2
004CEAD1  41 3B C0                        cmp eax, r8d
004CEAD4  75 08                           jne 0x1404ceade
004CEAD6  8B D1                           mov edx, ecx
004CEAD8  0F BA EA 09                     bts edx, 9
004CEADC  EB 18                           jmp 0x1404ceaf6
004CEADE  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
004CEAE2  83 F8 03                        cmp eax, 3
004CEAE5  75 13                           jne 0x1404ceafa
004CEAE7  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
004CEAEB  F6 C2 07                        test dl, 7
004CEAEE  74 0A                           je 0x1404ceafa
004CEAF0  8B D1                           mov edx, ecx
004CEAF2  0F BA EA 0A                     bts edx, 0xa
004CEAF6  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
004CEAFA  81 7C 24 44 00 00 60 00         cmp dword ptr [rsp + 0x44], 0x600000
004CEB02  0F 85 97 00 00 00               jne 0x1404ceb9f
004CEB08  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
004CEB0D  0F 85 8C 00 00 00               jne 0x1404ceb9f
004CEB13  F6 C3 42                        test bl, 0x42
004CEB16  0F 84 83 00 00 00               je 0x1404ceb9f
004CEB1C  48 8B CF                        mov rcx, rdi
004CEB1F  E8 7C D5 DA FF                  call 0x14027c0a0
004CEB24  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
004CEB29  4C 8B F0                        mov r14, rax
004CEB2C  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
004CEB34  33 D2                           xor edx, edx
004CEB36  48 F7 F1                        div rcx
004CEB39  4C 8B F8                        mov r15, rax
004CEB3C  48 85 C0                        test rax, rax
004CEB3F  74 49                           je 0x1404ceb8a
004CEB41  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
004CEB49  48 8B E9                        mov rbp, rcx
004CEB4C  48 8B B4 24 A0 00 00 00         mov rsi, qword ptr [rsp + 0xa0]
004CEB54  BB 01 00 00 00                  mov ebx, 1
004CEB59  48 C1 E5 0C                     shl rbp, 0xc
004CEB5D  4D 8B C5                        mov r8, r13
004CEB60  49 8B D6                        mov rdx, r14
004CEB63  48 8B CE                        mov rcx, rsi
004CEB66  E8 B9 66 F9 FF                  call 0x140465224
004CEB6B  4C 03 F5                        add r14, rbp
004CEB6E  4C 2B FB                        sub r15, rbx
004CEB71  75 EA                           jne 0x1404ceb5d
004CEB73  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
004CEB7B  48 8B F7                        mov rsi, rdi
004CEB7E  44 8B AC 24 20 01 00 00         mov r13d, dword ptr [rsp + 0x120]
004CEB86  8B 6C 24 68                     mov ebp, dword ptr [rsp + 0x68]
004CEB8A  4C 8B B4 24 B8 00 00 00         mov r14, qword ptr [rsp + 0xb8]
004CEB92  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
004CEB97  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
004CEB9F  48 C1 EB 0C                     shr rbx, 0xc
004CEBA3  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
004CEBAD  48 23 D8                        and rbx, rax
004CEBB0  41 83 FD 18                     cmp r13d, 0x18
004CEBB4  75 51                           jne 0x1404cec07
004CEBB6  41 8B D5                        mov edx, r13d
004CEBB9  48 8B CB                        mov rcx, rbx
004CEBBC  E8 AF 53 E9 FF                  call 0x140363f70
004CEBC1  48 8B D8                        mov rbx, rax
004CEBC4  85 ED                           test ebp, ebp
004CEBC6  75 7C                           jne 0x1404cec44
004CEBC8  48 89 07                        mov qword ptr [rdi], rax
004CEBCB  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
004CEBD0  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
004CEBD5  48 85 C9                        test rcx, rcx
004CEBD8  0F 85 80 00 00 00               jne 0x1404cec5e
004CEBDE  E8 AD 40 D7 FF                  call 0x140242c90
004CEBE3  41 BB 01 00 00 00               mov r11d, 1
004CEBE9  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
004CEBEE  48 8B C8                        mov rcx, rax
004CEBF1  44 89 5C 24 20                  mov dword ptr [rsp + 0x20], r11d
004CEBF6  45 33 C9                        xor r9d, r9d
004CEBF9  48 8B D3                        mov rdx, rbx
004CEBFC  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
004CEC00  E8 FB 62 DC FF                  call 0x140294f00
004CEC05  EB 5D                           jmp 0x1404cec64
004CEC07  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
004CEC0C  48 8B D3                        mov rdx, rbx
004CEC0F  45 0B C5                        or r8d, r13d
004CEC12  48 8B CF                        mov rcx, rdi
004CEC15  E8 76 69 DF FF                  call 0x1402c5590
004CEC1A  48 8B D8                        mov rbx, rax
004CEC1D  85 ED                           test ebp, ebp
004CEC1F  75 0B                           jne 0x1404cec2c
004CEC21  48 8B D0                        mov rdx, rax
004CEC24  48 8B CF                        mov rcx, rdi
004CEC27  E8 E4 2B DB FF                  call 0x140281810
004CEC2C  41 F6 C5 04                     test r13b, 4
004CEC30  74 0E                           je 0x1404cec40
004CEC32  81 7C 24 44 00 00 60 00         cmp dword ptr [rsp + 0x44], 0x600000
004CEC3A  74 04                           je 0x1404cec40
004CEC3C  48 83 CB 42                     or rbx, 0x42
004CEC40  85 ED                           test ebp, ebp
004CEC42  74 87                           je 0x1404cebcb
004CEC44  4C 8B CB                        mov r9, rbx
004CEC47  4C 8B C7                        mov r8, rdi
004CEC4A  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
004CEC4F  33 D2                           xor edx, edx
004CEC51  48 8B CB                        mov rcx, rbx
004CEC54  E8 93 43 E5 FF                  call 0x140322fec
004CEC59  E9 72 FF FF FF                  jmp 0x1404cebd0
004CEC5E  41 BB 01 00 00 00               mov r11d, 1
004CEC64  85 ED                           test ebp, ebp
004CEC66  75 2F                           jne 0x1404cec97
004CEC68  48 8B D7                        mov rdx, rdi
004CEC6B  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
004CEC75  48 C1 E2 19                     shl rdx, 0x19
004CEC79  48 8B C0                        mov rax, rax
004CEC7C  48 C1 E0 19                     shl rax, 0x19
004CEC80  45 33 C9                        xor r9d, r9d
004CEC83  48 2B D0                        sub rdx, rax
004CEC86  4D 8B C3                        mov r8, r11
004CEC89  48 C1 FA 10                     sar rdx, 0x10
004CEC8D  E8 DE 49 DC FF                  call 0x140293670
004CEC92  E9 F5 00 00 00                  jmp 0x1404ced8c
004CEC97  4C 8B C7                        mov r8, rdi
004CEC9A  8B D5                           mov edx, ebp
004CEC9C  E8 DB 95 EA FF                  call 0x14037827c
004CECA1  E9 E6 00 00 00                  jmp 0x1404ced8c
004CECA6  25 00 0C 00 00                  and eax, 0xc00
004CECAB  48 3D 00 08 00 00               cmp rax, 0x800
004CECB1  0F 85 D5 00 00 00               jne 0x1404ced8c
004CECB7  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
004CECBB  49 3B FE                        cmp rdi, r14
004CECBE  41 0F 44 C0                     cmove eax, r8d
004CECC2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004CECC6  41 83 FD 18                     cmp r13d, 0x18
004CECCA  0F 84 BC 00 00 00               je 0x1404ced8c
004CECD0  41 8B CD                        mov ecx, r13d
004CECD3  48 C1 E1 05                     shl rcx, 5
004CECD7  48 8B C1                        mov rax, rcx
004CECDA  48 33 C3                        xor rax, rbx
004CECDD  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
004CECE3  48 33 C1                        xor rax, rcx
004CECE6  48 8B CF                        mov rcx, rdi
004CECE9  48 89 07                        mov qword ptr [rdi], rax
004CECEC  E8 6F 50 DB FF                  call 0x140283d60
004CECF1  F7 44 24 48 00 00 00 04         test dword ptr [rsp + 0x48], 0x4000000
004CECF9  48 8B D8                        mov rbx, rax
004CECFC  74 05                           je 0x1404ced03
004CECFE  48 0F BA EB 07                  bts rbx, 7
004CED03  48 8B CF                        mov rcx, rdi
004CED06  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
004CED0E  33 F6                           xor esi, esi
004CED10  E8 EB 0D D7 FF                  call 0x14023fb00
004CED15  85 C0                           test eax, eax
004CED17  74 17                           je 0x1404ced30
004CED19  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
004CED21  E8 42 5E DC FF                  call 0x140294b68
004CED26  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
004CED2E  8B F0                           mov esi, eax
004CED30  48 0F BA 25 4F 7D AF 00 24      bt qword ptr [rip + 0xaf7d4f], 0x24
004CED39  73 35                           jae 0x1404ced70
004CED3B  F6 C3 20                        test bl, 0x20
004CED3E  75 30                           jne 0x1404ced70
004CED40  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
004CED4A  48 8B C8                        mov rcx, rax
004CED4D  48 B8 00 00 00 00 40 00 00 00   movabs rax, 0x4000000000
004CED57  48 03 C8                        add rcx, rax
004CED5A  48 3B F9                        cmp rdi, rcx
004CED5D  72 11                           jb 0x1404ced70
004CED5F  41 B8 80 00 00 00               mov r8d, 0x80
004CED65  48 8B D3                        mov rdx, rbx
004CED68  48 8B CF                        mov rcx, rdi
004CED6B  E8 10 40 DC FF                  call 0x140292d80
004CED70  48 89 1F                        mov qword ptr [rdi], rbx
004CED73  85 F6                           test esi, esi
004CED75  74 0B                           je 0x1404ced82
004CED77  48 8B D3                        mov rdx, rbx
004CED7A  48 8B CF                        mov rcx, rdi
004CED7D  E8 2A 61 DC FF                  call 0x140294eac
004CED82  4D 85 E4                        test r12, r12
004CED85  48 8B F7                        mov rsi, rdi
004CED88  4C 0F 44 E7                     cmove r12, rdi
004CED8C  8A 9C 24 10 01 00 00            mov bl, byte ptr [rsp + 0x110]
004CED93  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
004CED98  48 83 C7 08                     add rdi, 8
004CED9C  48 3B BC 24 18 01 00 00         cmp rdi, qword ptr [rsp + 0x118]
004CEDA4  0F 86 C6 FB FF FF               jbe 0x1404ce970
004CEDAA  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
004CEDAF  48 85 C0                        test rax, rax
004CEDB2  74 0D                           je 0x1404cedc1
004CEDB4  48 8B C8                        mov rcx, rax
004CEDB7  E8 04 32 E4 FF                  call 0x140311fc0
004CEDBC  E8 AF 4E E4 FF                  call 0x140313c70
004CEDC1  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
004CEDC6  48 85 FF                        test rdi, rdi
004CEDC9  74 30                           je 0x1404cedfb
004CEDCB  83 7C 24 4C 00                  cmp dword ptr [rsp + 0x4c], 0
004CEDD0  74 1C                           je 0x1404cedee
004CEDD2  4D 85 E4                        test r12, r12
004CEDD5  74 17                           je 0x1404cedee
004CEDD7  49 2B F4                        sub rsi, r12
004CEDDA  BA 01 00 00 00                  mov edx, 1
004CEDDF  48 C1 FE 03                     sar rsi, 3
004CEDE3  49 8B CC                        mov rcx, r12
004CEDE6  48 03 D6                        add rdx, rsi
004CEDE9  E8 86 25 01 00                  call 0x1404e1374
004CEDEE  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
004CEDF3  48 8B D7                        mov rdx, rdi
004CEDF6  E8 C5 80 D4 FF                  call 0x140216ec0
004CEDFB  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
004CEE00  8A D3                           mov dl, bl
004CEE02  E8 89 E8 DA FF                  call 0x14027d690
004CEE07  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
004CEE0F  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
004CEE13  89 08                           mov dword ptr [rax], ecx
004CEE15  33 C0                           xor eax, eax
004CEE17  48 8B 9C 24 28 01 00 00         mov rbx, qword ptr [rsp + 0x128]
004CEE1F  48 81 C4 D0 00 00 00            add rsp, 0xd0
004CEE26  41 5F                           pop r15
004CEE28  41 5E                           pop r14
004CEE2A  41 5D                           pop r13
004CEE2C  41 5C                           pop r12
004CEE2E  5F                              pop rdi
004CEE2F  5E                              pop rsi
004CEE30  5D                              pop rbp
004CEE31  C3                              ret
004CEE32  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiProtectAweRegion(__int64 a1, __int64 a2, int a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (208);
    v_rdi = 0;
    result = 0;
    v_stack_mB8 = 0;
    v_stack_mA8 = 0;
    v_stack_m68 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    v_rdi = (a1) >> (9);
    v_stack_mD0 = result;
    v_stack_mD8 = 1;
    v_rdi = (v_rdi) & (a2);
    v_r12 = (a2) >> (9);
    v_rdi = (v_rdi) + (a1);
    v_r12 = (v_r12) & (a2);
    v_r12 = (v_r12) + (a1);
    v_stack_p10 = v_r12;
    result = MiLockAweVadsShared(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    result = MiGetAweNode(a1, a2, a3, a4);
    v_stack_m88 = *(unsigned __int64 *)(result + 24);
    *(unsigned __int8 *)(result + 64) = 0;
    if (((unsigned int)((unsigned int)(a3))) == 24) goto loc_004CE748;
    v_r13 = (unsigned int)(((unsigned int)(a3)) & (7));
    if (((unsigned int)(v_r13)) == 1) goto loc_004CE719;
    if (((unsigned int)(v_r13)) != 4) goto loc_004CE80F;
loc_004CE719:
    result = MiGetVadCacheAttribute(*(unsigned __int64 *)(result + 24), a2, a3, 24);
    if ((unsigned int)(result) != 0) goto loc_004CE72B;
    goto loc_004CE735;
loc_004CE72B:
    result = 0;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 2) { result = 24; }
loc_004CE735:
    v_r13 = (unsigned int)((v_r13) | ((unsigned int)(result)));
    v_stack_p18 = (unsigned int)(v_r13);
loc_004CE748:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 8))))) == 0) goto loc_004CE766;
    v_stack_mB0 = 4;
    goto loc_004CE842;
loc_004CE766:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m88 + 48))))) >> (7));
    v_r12 = (unsigned int)((v_r12) & (31));
    v_stack_mB0 = (unsigned int)(v_r12);
    result = (unsigned __int8)(((unsigned int)((unsigned int)(v_r12))) & (7));
    if (((unsigned __int8)(result)) != 1) goto loc_004CE78F;
    result = (unsigned __int8)(((unsigned int)((unsigned int)(v_r13))) & (7));
    if (((unsigned __int8)(result)) != 1) goto loc_004CE80F;
loc_004CE78F:
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_004CE829;
    result = MI_GET_GRAPHICS_PROTECTION_FROM_VAD(v_stack_m88, 1, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(v_stack_m88 + 48)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & ((unsigned int)((unsigned int)(0x20000ULL))));
    if ((((unsigned int)((unsigned int)(0x20000ULL))) & ((unsigned int)((unsigned int)((unsigned int)(result))))) == 0) goto loc_004CE7B3;
    if ((unsigned int)(result) != 0) goto loc_004CE7B7;
    goto loc_004CE80F;
loc_004CE7B3:
    if ((unsigned int)(result) != 0) goto loc_004CE80F;
loc_004CE7B7:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & ((unsigned int)((unsigned int)(0x40000ULL))));
    if ((((unsigned int)((unsigned int)(0x40000ULL))) & ((unsigned int)((unsigned int)((unsigned int)(result))))) == 0) goto loc_004CE7CB;
    if ((unsigned int)(result) != 0) goto loc_004CE7CF;
    goto loc_004CE80F;
loc_004CE7CB:
    if ((unsigned int)(result) != 0) goto loc_004CE80F;
loc_004CE7CF:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0xFFF9FFFFULL));
    a1 = ((((unsigned int)((unsigned int)(0x1C000ULL))) & (a3)) == 0) ? 1 : 0;
    result = ((((unsigned int)((unsigned int)(0x1C000ULL))) & ((unsigned int)((unsigned int)(a4)))) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_004CE80F;
    a2 = ((((unsigned int)((unsigned int)(0x12000ULL))) & (a3)) == 0) ? 1 : 0;
    result = ((((unsigned int)((unsigned int)(0x12000ULL))) & ((unsigned int)((unsigned int)(a4)))) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a2))) != 0) goto loc_004CE80F;
    if (a3 != 0x800ULL) goto loc_004CE824;
    if ((((unsigned int)((unsigned int)(a4))) & (0xFFF9F7FFULL)) == 0) goto loc_004CE824;
loc_004CE80F:
    result = MiUnlockAwePagesShared(*(unsigned __int64 *)(gs_base + (0 + 392)), result, a3, (unsigned int)(*(unsigned int *)(v_stack_m88 + 48)));
loc_004CE81A:
    goto loc_004CEE17;
loc_004CE824:
loc_004CE829:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m88 + 48))) & ((unsigned int)((unsigned int)(0x4200000ULL))));
    if (a4 == ((unsigned int)((unsigned int)(0x4200000ULL)))) {
        v_stack_mBC = 1;
    }
    result = MiUnlockAwePagesShared(*(unsigned __int64 *)(gs_base + (0 + 392)), result, a3, a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m88 + 48))) & ((unsigned int)((unsigned int)(0x600000ULL))));
    v_stack_mC4 = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)((unsigned int)(0x600000ULL))));
    v_stack_m98 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 16);
    result = (unsigned int)(-(result));
    result = 0;
    v_stack_mC8 = 0;
    a4 = (unsigned int)((a4) & (0x80000000ULL));
    result = MiGetAweViewPageSize(result, (unsigned int)(0x600000ULL), a3, a4);
    a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 16);
    if (result != 0) { a1 = result; }
    v_stack_m70 = a1;
    result = MiPageSizeToPteLevel(a1, (unsigned int)(0x600000ULL), a3, a4);
    v_stack_mA0 = (unsigned int)(result);
    if (((unsigned int)(result)) < 1) goto loc_004CE8B5;
    v_stack_m90 = 1;
    goto loc_004CE8BA;
loc_004CE8B5:
    v_stack_m90 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 16);
loc_004CE8BA:
    v_stack_mC0 = a4;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 16)) == 1) goto loc_004CE8F7;
    a2 = 0;
    result = (v_rdi) >> (3);
    result = (unsigned int)((result) & (511));
    if (0 != 0) goto loc_004CE81A;
    result = (v_stack_p10) - (v_rdi);
    result = (result) >> (3);
    result = (result) + (1);
    if (0 != 0) goto loc_004CE81A;
loc_004CE8F7:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_004CE938;
loc_004CE911:
    v_rdi = (v_rdi) >> (9);
    v_rdi = (v_rdi) & (a4);
    v_r12 = (v_stack_p10) >> (9);
    v_rdi = (v_rdi) + (0);
    v_r12 = (v_r12) & (a4);
    v_r12 = (v_r12) + (0);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) - (1));
    if (condition_is_not_equal) goto loc_004CE911;
    v_stack_p10 = v_r12;
loc_004CE938:
    v_r12 = 0;
    v_rsi = 0;
    v_stack_m50 = v_rdi;
    result = MiLockWorkingSetShared(v_stack_mD0, a2, 1, a4);
    v_stack_p8 = (unsigned __int8)(result);
    if (v_rdi > v_stack_p10) goto loc_004CEDFB;
loc_004CE970:
    if (0 == 0) goto loc_004CE982;
    if (((v_rdi) & (0xFFFULL)) != 0) goto loc_004CEA4C;
loc_004CE982:
    result = v_stack_mA8;
    if (v_stack_mA8 != 0) {
        a1 = v_stack_mA8;
        result = MiFlushTbList(a1, 0, 1, a4);
        result = MiReleaseProcessorFlushList(a1, 0, 1, a4);
        a2 = v_stack_mB8;
        result = 0;
        v_stack_mA8 = 0;
    }
    if (a2 == 0) goto loc_004CE9F3;
    if (0 == 0) goto loc_004CE9D3;
    if (v_stack_mBC != 0) {
        a2 = 0;
        a1 = 0;
        a2 = (a2) - (0);
        a2 = (a2) >> (3);
        a2 = (a2) + 1;
        result = MiFlushGraphicsPtes(a1, a2, 1, a4);
        a2 = v_stack_mB8;
    }
    v_r12 = 0;
loc_004CE9D3:
    result = MiUnlockPageTable(v_stack_mD0, a2, 1, a4);
    result = MiUnlockWorkingSetShared(v_stack_mD0, (unsigned __int8)((unsigned __int8)(result)), 1, a4);
    result = MiLockWorkingSetShared(v_stack_mD0, (unsigned __int8)((unsigned __int8)(result)), 1, a4);
loc_004CE9F3:
    a4 = 0;
    result = MiLockLowestValidPageTableEx(v_stack_mD0, v_rdi, v_stack_m78, a4);
    v_stack_mB8 = result;
    a1 = (v_rdi) >> (9);
    a1 = (a1) & (result);
    a1 = (a1) + (result);
    if (result == a1) goto loc_004CEA4C;
    v_rdi = (v_rdi) & (-8);
    v_rdi = (v_rdi) | (0xFF8ULL);
    goto loc_004CED98;
loc_004CEA4C:
    if (v_stack_mC4 != 0x600000ULL) goto loc_004CEA7E;
    if (v_stack_m90 == 1) goto loc_004CEA78;
    a2 = 0;
    result = (v_rdi) >> (3);
    result = (unsigned int)((result) & (511));
    if (0 == 0) {
        result = 0;
        v_stack_mC8 = 0;
    }
    result = MI_READ_PTE_LOCK_FREE(v_rdi, a2, v_stack_m78, a4);
    v_stack_m58 = result;
    if (result == 0) goto loc_004CED8C;
    if (((1) & ((unsigned __int8)(result))) == 0) goto loc_004CECA6;
    if (0 == 0) { v_r12 = v_rdi; }
    if (v_rdi != v_rdi) goto loc_004CEAFA;
    result = (unsigned int)((result) & (0x800ULL));
    result = -(result);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mB0)))) >> (3));
    a1 = (unsigned int)((v_rdi) & (2));
    a1 = (unsigned int)((a1) + (2));
    if (((unsigned int)(result)) != 1) goto loc_004CEADE;
    goto loc_004CEAF6;
loc_004CEADE:
    v_stack_mD8 = (unsigned int)(a1);
    if (((unsigned int)(result)) != 3) goto loc_004CEAFA;
    v_stack_mD8 = (unsigned int)(a1);
    if ((((unsigned __int8)((unsigned int)((unsigned int)(a1)))) & (7)) == 0) goto loc_004CEAFA;
loc_004CEAF6:
    v_stack_mD8 = (unsigned int)((unsigned int)((unsigned int)(a1)));
loc_004CEAFA:
    if (v_stack_mC4 != 0x600000ULL) goto loc_004CEB9F;
    if (v_stack_mC8 != 0) goto loc_004CEB9F;
    if ((((unsigned __int8)(result)) & (66)) == 0) goto loc_004CEB9F;
    result = MiGetLeafVa(v_rdi, (unsigned int)((unsigned int)(a1)), 1, a4);
    a2 = 0;
    if (v_stack_m70 == 0) goto loc_004CEB8A;
    v_rbp = (v_stack_m98) << (12);
loc_004CEB5D:
    result = MiCaptureWriteWatchDirtyBit(v_stack_m68, result, v_stack_m88, a4);
    v_r14 = (result) + (v_rbp);
    v_r15 = (v_stack_m70) - (1);
    if (condition_is_not_equal) goto loc_004CEB5D;
loc_004CEB8A:
    v_stack_mC8 = 1;
loc_004CEB9F:
    v_rbx = (v_stack_m58) >> (12);
    v_rbx = (v_rbx) & (result);
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 24) goto loc_004CEC07;
    result = MiMakeTransitionPte(v_rbx, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), v_stack_m88, a4);
    if ((unsigned int)((unsigned int)(v_stack_mA0)) != 0) goto loc_004CEC44;
    *(unsigned __int64 *)(v_rdi) = result;
loc_004CEBCB:
loc_004CEBD0:
    if (v_stack_mA8 != 0) goto loc_004CEC5E;
    result = MiGetProcessorFlushList(v_stack_mA8, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), v_stack_m88, a4);
    v_stack_mA8 = result;
    v_stack_mE8 = 1;
    a4 = 0;
    result = MiInitializeTbFlushList(result, v_stack_mD0, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    goto loc_004CEC64;
loc_004CEC07:
    a3 = (unsigned int)(((unsigned int)(v_stack_mC0)) | ((unsigned int)((unsigned int)(v_stack_p18))));
    result = MiMakeValidPte(v_rdi, v_stack_mD0, a3, a4);
    if ((unsigned int)((unsigned int)(v_stack_mA0)) == 0) {
        a2 = result;
        a1 = v_rdi;
        result = MiWriteValidPteNewProtection(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)((unsigned int)(v_stack_p18))) & (4)) == 0) goto loc_004CEC40;
    v_rbx = result;
    if (v_stack_mC4 != 0x600000ULL) {
        v_rbx = (result) | (66);
    }
    if ((unsigned int)((unsigned int)(v_stack_mA0)) == 0) goto loc_004CEBCB;
loc_004CEC44:
    a2 = 0;
    result = MiRewritePteWithLockBit(v_stack_mD0, a2, v_rdi, v_rbx);
    goto loc_004CEBD0;
loc_004CEC5E:
loc_004CEC64:
    if ((unsigned int)((unsigned int)(v_stack_mA0)) != 0) goto loc_004CEC97;
    a2 = (v_rdi) << (25);
    result = (result) << (25);
    a4 = 0;
    a2 = (a2) - (result);
    a2 = (a2) >> (16);
    result = MiInsertTbFlushEntry(v_stack_mD0, a2, 1, a4);
    goto loc_004CED8C;
loc_004CEC97:
    result = MiInsertLargeTbFlushEntry(v_stack_mD0, (unsigned int)((unsigned int)((unsigned int)(v_stack_mA0))), v_rdi, a4);
    goto loc_004CED8C;
loc_004CECA6:
    result = (unsigned int)((result) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_004CED8C;
    result = (unsigned int)(v_stack_mD8);
    if (v_rdi == v_stack_m50) { result = (unsigned int)(v_rdi); }
    v_stack_mD8 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(v_stack_p18))) == 24) goto loc_004CED8C;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))) << (5);
    result = (a1) ^ (v_stack_mD0);
    result = (result) & (-993);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_rdi) = result;
    result = MiMakeTransitionPteValid(v_rdi, (unsigned int)((unsigned int)((unsigned int)(v_stack_mA0))), v_rdi, a4);
    if (((v_stack_mC0) & (0x4000000ULL)) != 0) {
    }
    v_stack_m80 = result;
    v_rsi = 0;
    result = MiPteInShadowRange(v_rdi, (unsigned int)((unsigned int)((unsigned int)(v_stack_mA0))), v_rdi, a4);
    v_rbx = result;
    if ((unsigned int)(result) != 0) {
        a2 = v_stack_m80;
        result = MiSanitizeShadowPxe(v_rdi, a2, v_rdi, a4);
        v_rbx = v_stack_m80;
        v_rsi = (unsigned int)(result);
    }
    if (condition_is_above_or_equal) goto loc_004CED70;
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_004CED70;
    a1 = (result) + (result);
    if (v_rdi >= a1) {
        a3 = 128;
        a2 = v_rbx;
        a1 = v_rdi;
        result = MiCheckLinearProtectedPteAccessedBit(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rdi) = v_rbx;
    if ((unsigned int)(v_rsi) != 0) {
        a2 = v_rbx;
        a1 = v_rdi;
        result = MiWritePteShadow(a1, a2, a3, a4);
    }
    if (v_r12 == 0) { v_r12 = v_rdi; }
loc_004CED8C:
loc_004CED98:
    v_rdi = (v_rdi) + (8);
    if (v_rdi <= v_stack_p10) goto loc_004CE970;
    result = v_stack_mA8;
    if (v_stack_mA8 != 0) {
        a1 = v_stack_mA8;
        result = MiFlushTbList(a1, v_stack_mB8, a3, a4);
        result = MiReleaseProcessorFlushList(a1, v_stack_mB8, a3, a4);
    }
    if (v_stack_mB8 == 0) goto loc_004CEDFB;
    if (v_stack_mBC == 0) goto loc_004CEDEE;
    v_rsi = v_rdi;
    if (v_r12 != 0) {
        v_rsi = (v_rdi) - (v_r12);
        a2 = 1;
        v_rsi = (v_rsi) >> (3);
        a1 = v_r12;
        a2 = (a2) + (v_rsi);
        result = MiFlushGraphicsPtes(a1, a2, a3, a4);
    }
    result = MiUnlockPageTable(v_stack_mD0, v_stack_mB8, a3, a4);
loc_004CEDFB:
    result = MiUnlockWorkingSetShared(v_stack_mD0, (unsigned __int8)(v_stack_p8), a3, a4);
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(v_stack_mD8));
    result = 0;
loc_004CEE17:
    v_rsp = (v_rsp) + (208);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiProtectAweRegion(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (208);
    local_rdi = 0;
    result = 0;
    v_stack_mB8 = 0;
    v_stack_mA8 = 0;
    v_stack_m68 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    local_rdi = (Arg1) >> (9);
    v_stack_mD0 = result;
    v_stack_mD8 = 1;
    local_rdi = (local_rdi) & (Arg2);
    local_r12 = (Arg2) >> (9);
    local_rdi = (local_rdi) + (Arg1);
    local_r12 = (local_r12) & (Arg2);
    local_r12 = (local_r12) + (Arg1);
    v_stack_p10 = local_r12;
    result = MiLockAweVadsShared(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    result = MiGetAweNode(Arg1, Arg2, Arg3, Arg4);
    v_stack_m88 = *(uint64_t *)(result + 0x18);
    *(uint8_t *)(result + 0x40) = 0;
    if (((uint32_t)((uint32_t)(Arg3))) == 24) goto loc_004CE748;
    local_r13 = (uint32_t)(((uint32_t)(Arg3)) & (7));
    if (((uint32_t)(local_r13)) == 1) goto loc_004CE719;
    if (((uint32_t)(local_r13)) != 4) goto loc_004CE80F;
loc_004CE719:
    result = MiGetVadCacheAttribute(*(uint64_t *)(result + 0x18), Arg2, Arg3, 24);
    if ((uint32_t)(result) != 0) goto loc_004CE72B;
    goto loc_004CE735;
loc_004CE72B:
    result = 0;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 2) { result = 24; }
loc_004CE735:
    local_r13 = (uint32_t)((local_r13) | ((uint32_t)(result)));
    v_stack_p18 = (uint32_t)(local_r13);
loc_004CE748:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x8))))) == 0) goto loc_004CE766;
    v_stack_mB0 = 4;
    goto loc_004CE842;
loc_004CE766:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x30))))) >> (7));
    local_r12 = (uint32_t)((local_r12) & (31));
    v_stack_mB0 = (uint32_t)(local_r12);
    result = (uint8_t)(((uint32_t)((uint32_t)(local_r12))) & (7));
    if (((uint8_t)(result)) != 1) goto loc_004CE78F;
    result = (uint8_t)(((uint32_t)((uint32_t)(local_r13))) & (7));
    if (((uint8_t)(result)) != 1) goto loc_004CE80F;
loc_004CE78F:
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_004CE829;
    result = MI_GET_GRAPHICS_PROTECTION_FROM_VAD(v_stack_m88, 1, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(v_stack_m88 + 0x30)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & ((uint32_t)((uint32_t)(0x20000ULL))));
    if ((((uint32_t)((uint32_t)(0x20000ULL))) & ((uint32_t)((uint32_t)((uint32_t)(result))))) == 0) goto loc_004CE7B3;
    if ((uint32_t)(result) != 0) goto loc_004CE7B7;
    goto loc_004CE80F;
loc_004CE7B3:
    if ((uint32_t)(result) != 0) goto loc_004CE80F;
loc_004CE7B7:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & ((uint32_t)((uint32_t)(0x40000ULL))));
    if ((((uint32_t)((uint32_t)(0x40000ULL))) & ((uint32_t)((uint32_t)((uint32_t)(result))))) == 0) goto loc_004CE7CB;
    if ((uint32_t)(result) != 0) goto loc_004CE7CF;
    goto loc_004CE80F;
loc_004CE7CB:
    if ((uint32_t)(result) != 0) goto loc_004CE80F;
loc_004CE7CF:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0xFFF9FFFFULL));
    Arg1 = ((((uint32_t)((uint32_t)(0x1C000ULL))) & (Arg3)) == 0) ? 1 : 0;
    result = ((((uint32_t)((uint32_t)(0x1C000ULL))) & ((uint32_t)((uint32_t)(Arg4)))) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_004CE80F;
    Arg2 = ((((uint32_t)((uint32_t)(0x12000ULL))) & (Arg3)) == 0) ? 1 : 0;
    result = ((((uint32_t)((uint32_t)(0x12000ULL))) & ((uint32_t)((uint32_t)(Arg4)))) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg2))) != 0) goto loc_004CE80F;
    if (Arg3 != 0x800ULL) goto loc_004CE824;
    if ((((uint32_t)((uint32_t)(Arg4))) & (0xFFF9F7FFULL)) == 0) goto loc_004CE824;
loc_004CE80F:
    result = MiUnlockAwePagesShared(*(uint64_t *)(gs_base + (0 + 0x188)), result, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m88 + 0x30)));
loc_004CE81A:
    goto loc_004CEE17;
loc_004CE824:
loc_004CE829:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x30))) & ((uint32_t)((uint32_t)(0x4200000ULL))));
    if (Arg4 == ((uint32_t)((uint32_t)(0x4200000ULL)))) {
        v_stack_mBC = 1;
    }
    result = MiUnlockAwePagesShared(*(uint64_t *)(gs_base + (0 + 0x188)), result, Arg3, Arg4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x30))) & ((uint32_t)((uint32_t)(0x600000ULL))));
    v_stack_mC4 = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)((uint32_t)(0x600000ULL))));
    v_stack_m98 = *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x10);
    result = (uint32_t)(-(result));
    result = 0;
    v_stack_mC8 = 0;
    Arg4 = (uint32_t)((Arg4) & (0x80000000ULL));
    result = MiGetAweViewPageSize(result, (uint32_t)(0x600000ULL), Arg3, Arg4);
    Arg1 = *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x10);
    if (result != 0) { Arg1 = result; }
    v_stack_m70 = Arg1;
    result = MiPageSizeToPteLevel(Arg1, (uint32_t)(0x600000ULL), Arg3, Arg4);
    v_stack_mA0 = (uint32_t)(result);
    if (((uint32_t)(result)) < 1) goto loc_004CE8B5;
    v_stack_m90 = 1;
    goto loc_004CE8BA;
loc_004CE8B5:
    v_stack_m90 = *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x10);
loc_004CE8BA:
    v_stack_mC0 = Arg4;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x10)) == 1) goto loc_004CE8F7;
    Arg2 = 0;
    result = (local_rdi) >> (3);
    result = (uint32_t)((result) & (511));
    if (0 != 0) goto loc_004CE81A;
    result = (v_stack_p10) - (local_rdi);
    result = (result) >> (3);
    result = (result) + (1);
    if (0 != 0) goto loc_004CE81A;
loc_004CE8F7:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_004CE938;
loc_004CE911:
    local_rdi = (local_rdi) >> (9);
    local_rdi = (local_rdi) & (Arg4);
    local_r12 = (v_stack_p10) >> (9);
    local_rdi = (local_rdi) + (0);
    local_r12 = (local_r12) & (Arg4);
    local_r12 = (local_r12) + (0);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) - (1));
    if (condition_is_not_equal) goto loc_004CE911;
    v_stack_p10 = local_r12;
loc_004CE938:
    local_r12 = 0;
    local_rsi = 0;
    v_stack_m50 = local_rdi;
    result = MiLockWorkingSetShared(v_stack_mD0, Arg2, 1, Arg4);
    v_stack_p8 = (uint8_t)(result);
    if (local_rdi > v_stack_p10) goto loc_004CEDFB;
loc_004CE970:
    if (0 == 0) goto loc_004CE982;
    if (((local_rdi) & (0xFFFULL)) != 0) goto loc_004CEA4C;
loc_004CE982:
    result = v_stack_mA8;
    if (v_stack_mA8 != 0) {
        Arg1 = v_stack_mA8;
        result = MiFlushTbList(Arg1, 0, 1, Arg4);
        result = MiReleaseProcessorFlushList(Arg1, 0, 1, Arg4);
        Arg2 = v_stack_mB8;
        result = 0;
        v_stack_mA8 = 0;
    }
    if (Arg2 == 0) goto loc_004CE9F3;
    if (0 == 0) goto loc_004CE9D3;
    if (v_stack_mBC != 0) {
        Arg2 = 0;
        Arg1 = 0;
        Arg2 = (Arg2) - (0);
        Arg2 = (Arg2) >> (3);
        Arg2 = (Arg2) + 1;
        result = MiFlushGraphicsPtes(Arg1, Arg2, 1, Arg4);
        Arg2 = v_stack_mB8;
    }
    local_r12 = 0;
loc_004CE9D3:
    result = MiUnlockPageTable(v_stack_mD0, Arg2, 1, Arg4);
    result = MiUnlockWorkingSetShared(v_stack_mD0, (uint8_t)((uint8_t)(result)), 1, Arg4);
    result = MiLockWorkingSetShared(v_stack_mD0, (uint8_t)((uint8_t)(result)), 1, Arg4);
loc_004CE9F3:
    Arg4 = 0;
    result = MiLockLowestValidPageTableEx(v_stack_mD0, local_rdi, v_stack_m78, Arg4);
    v_stack_mB8 = result;
    Arg1 = (local_rdi) >> (9);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) + (result);
    if (result == Arg1) goto loc_004CEA4C;
    local_rdi = (local_rdi) & (-8);
    local_rdi = (local_rdi) | (0xFF8ULL);
    goto loc_004CED98;
loc_004CEA4C:
    if (v_stack_mC4 != 0x600000ULL) goto loc_004CEA7E;
    if (v_stack_m90 == 1) goto loc_004CEA78;
    Arg2 = 0;
    result = (local_rdi) >> (3);
    result = (uint32_t)((result) & (511));
    if (0 == 0) {
        result = 0;
        v_stack_mC8 = 0;
    }
    result = MI_READ_PTE_LOCK_FREE(local_rdi, Arg2, v_stack_m78, Arg4);
    v_stack_m58 = result;
    if (result == 0) goto loc_004CED8C;
    if (((1) & ((uint8_t)(result))) == 0) goto loc_004CECA6;
    if (0 == 0) { local_r12 = local_rdi; }
    if (local_rdi != local_rdi) goto loc_004CEAFA;
    result = (uint32_t)((result) & (0x800ULL));
    result = -(result);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mB0)))) >> (3));
    Arg1 = (uint32_t)((local_rdi) & (2));
    Arg1 = (uint32_t)((Arg1) + (2));
    if (((uint32_t)(result)) != 1) goto loc_004CEADE;
    goto loc_004CEAF6;
loc_004CEADE:
    v_stack_mD8 = (uint32_t)(Arg1);
    if (((uint32_t)(result)) != 3) goto loc_004CEAFA;
    v_stack_mD8 = (uint32_t)(Arg1);
    if ((((uint8_t)((uint32_t)((uint32_t)(Arg1)))) & (7)) == 0) goto loc_004CEAFA;
loc_004CEAF6:
    v_stack_mD8 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
loc_004CEAFA:
    if (v_stack_mC4 != 0x600000ULL) goto loc_004CEB9F;
    if (v_stack_mC8 != 0) goto loc_004CEB9F;
    if ((((uint8_t)(result)) & (66)) == 0) goto loc_004CEB9F;
    result = MiGetLeafVa(local_rdi, (uint32_t)((uint32_t)(Arg1)), 1, Arg4);
    Arg2 = 0;
    if (v_stack_m70 == 0) goto loc_004CEB8A;
    local_rbp = (v_stack_m98) << (12);
loc_004CEB5D:
    result = MiCaptureWriteWatchDirtyBit(v_stack_m68, result, v_stack_m88, Arg4);
    local_r14 = (result) + (local_rbp);
    local_r15 = (v_stack_m70) - (1);
    if (condition_is_not_equal) goto loc_004CEB5D;
loc_004CEB8A:
    v_stack_mC8 = 1;
loc_004CEB9F:
    local_rbx = (v_stack_m58) >> (12);
    local_rbx = (local_rbx) & (result);
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 24) goto loc_004CEC07;
    result = MiMakeTransitionPte(local_rbx, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), v_stack_m88, Arg4);
    if ((uint32_t)((uint32_t)(v_stack_mA0)) != 0) goto loc_004CEC44;
    *(uint64_t *)(local_rdi) = result;
loc_004CEBCB:
loc_004CEBD0:
    if (v_stack_mA8 != 0) goto loc_004CEC5E;
    result = MiGetProcessorFlushList(v_stack_mA8, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), v_stack_m88, Arg4);
    v_stack_mA8 = result;
    v_stack_mE8 = 1;
    Arg4 = 0;
    result = MiInitializeTbFlushList(result, v_stack_mD0, (uint32_t)(*(uint32_t *)(result + 0xC)), Arg4);
    goto loc_004CEC64;
loc_004CEC07:
    Arg3 = (uint32_t)(((uint32_t)(v_stack_mC0)) | ((uint32_t)((uint32_t)(v_stack_p18))));
    result = MiMakeValidPte(local_rdi, v_stack_mD0, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(v_stack_mA0)) == 0) {
        Arg2 = result;
        Arg1 = local_rdi;
        result = MiWriteValidPteNewProtection(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint8_t)((uint32_t)(v_stack_p18))) & (4)) == 0) goto loc_004CEC40;
    local_rbx = result;
    if (v_stack_mC4 != 0x600000ULL) {
        local_rbx = (result) | (66);
    }
    if ((uint32_t)((uint32_t)(v_stack_mA0)) == 0) goto loc_004CEBCB;
loc_004CEC44:
    Arg2 = 0;
    result = MiRewritePteWithLockBit(v_stack_mD0, Arg2, local_rdi, local_rbx);
    goto loc_004CEBD0;
loc_004CEC5E:
loc_004CEC64:
    if ((uint32_t)((uint32_t)(v_stack_mA0)) != 0) goto loc_004CEC97;
    Arg2 = (local_rdi) << (25);
    result = (result) << (25);
    Arg4 = 0;
    Arg2 = (Arg2) - (result);
    Arg2 = (Arg2) >> (16);
    result = MiInsertTbFlushEntry(v_stack_mD0, Arg2, 1, Arg4);
    goto loc_004CED8C;
loc_004CEC97:
    result = MiInsertLargeTbFlushEntry(v_stack_mD0, (uint32_t)((uint32_t)((uint32_t)(v_stack_mA0))), local_rdi, Arg4);
    goto loc_004CED8C;
loc_004CECA6:
    result = (uint32_t)((result) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_004CED8C;
    result = (uint32_t)(v_stack_mD8);
    if (local_rdi == v_stack_m50) { result = (uint32_t)(local_rdi); }
    v_stack_mD8 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(v_stack_p18))) == 24) goto loc_004CED8C;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))) << (5);
    result = (Arg1) ^ (v_stack_mD0);
    result = (result) & (-993);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_rdi) = result;
    result = MiMakeTransitionPteValid(local_rdi, (uint32_t)((uint32_t)((uint32_t)(v_stack_mA0))), local_rdi, Arg4);
    if (((v_stack_mC0) & (0x4000000ULL)) != 0) {
    }
    v_stack_m80 = result;
    local_rsi = 0;
    result = MiPteInShadowRange(local_rdi, (uint32_t)((uint32_t)((uint32_t)(v_stack_mA0))), local_rdi, Arg4);
    local_rbx = result;
    if ((uint32_t)(result) != 0) {
        Arg2 = v_stack_m80;
        result = MiSanitizeShadowPxe(local_rdi, Arg2, local_rdi, Arg4);
        local_rbx = v_stack_m80;
        local_rsi = (uint32_t)(result);
    }
    if (condition_is_above_or_equal) goto loc_004CED70;
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_004CED70;
    Arg1 = (result) + (result);
    if (local_rdi >= Arg1) {
        Arg3 = 128;
        Arg2 = local_rbx;
        Arg1 = local_rdi;
        result = MiCheckLinearProtectedPteAccessedBit(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(local_rdi) = local_rbx;
    if ((uint32_t)(local_rsi) != 0) {
        Arg2 = local_rbx;
        Arg1 = local_rdi;
        result = MiWritePteShadow(Arg1, Arg2, Arg3, Arg4);
    }
    if (local_r12 == 0) { local_r12 = local_rdi; }
loc_004CED8C:
loc_004CED98:
    local_rdi = (local_rdi) + (8);
    if (local_rdi <= v_stack_p10) goto loc_004CE970;
    result = v_stack_mA8;
    if (v_stack_mA8 != 0) {
        Arg1 = v_stack_mA8;
        result = MiFlushTbList(Arg1, v_stack_mB8, Arg3, Arg4);
        result = MiReleaseProcessorFlushList(Arg1, v_stack_mB8, Arg3, Arg4);
    }
    if (v_stack_mB8 == 0) goto loc_004CEDFB;
    if (v_stack_mBC == 0) goto loc_004CEDEE;
    local_rsi = local_rdi;
    if (local_r12 != 0) {
        local_rsi = (local_rdi) - (local_r12);
        Arg2 = 1;
        local_rsi = (local_rsi) >> (3);
        Arg1 = local_r12;
        Arg2 = (Arg2) + (local_rsi);
        result = MiFlushGraphicsPtes(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiUnlockPageTable(v_stack_mD0, v_stack_mB8, Arg3, Arg4);
loc_004CEDFB:
    result = MiUnlockWorkingSetShared(v_stack_mD0, (uint8_t)(v_stack_p8), Arg3, Arg4);
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(v_stack_mD8));
    result = 0;
loc_004CEE17:
    local_rsp = (local_rsp) + (208);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004CE62C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
