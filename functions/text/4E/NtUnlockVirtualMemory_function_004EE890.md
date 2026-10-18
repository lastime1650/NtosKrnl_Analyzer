# NtUnlockVirtualMemory

- RVA: `0x004EE890`–`0x004EEFC4` (길이 `1,844` bytes)
- VA: `0x00000001404EE890`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D8CDC`
- 디코드: `465`개 명령, `1,844/1,844` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **56**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004EE90E` → [MiLockUnlockCommon](../../page/9E/MiLockUnlockCommon_function_009EA5D0.md) (function, `0x009EA5D0`)
- `0x004EE941` → [MiVmAccessLoggingEnabled](../36/MiVmAccessLoggingEnabled_function_003629D4.md) (function, `0x003629D4`)
- `0x004EE989` → [KiStackAttachProcess](../21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x004EE9A8` → [MiLockVadRange](../../page/87/MiLockVadRange_function_0087F670.md) (function, `0x0087F670`)
- `0x004EE9C4` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x004EE9F2` → [MiWorkingSetIsContended](../2A/MiWorkingSetIsContended_function_002AE520.md) (function, `0x002AE520`)
- `0x004EEA06` → [MiPageTableLockIsContended](../2A/MiPageTableLockIsContended_function_002AE650.md) (function, `0x002AE650`)
- `0x004EEA0F` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x004EEA2D` → [MiFreeWsleList](../24/MiFreeWsleList_function_00241168.md) (function, `0x00241168`)
- `0x004EEA32` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x004EEA45` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004EEA54` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x004EEA5C` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x004EEA82` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x004EEA8C` → [MiGetNextVad](../29/MiGetNextVad_function_00297224.md) (function, `0x00297224`)
- `0x004EEAB5` → [MiVadPagesTradable](../40/MiVadPagesTradable_function_00409360.md) (function, `0x00409360`)
- `0x004EEB3D` → [MiFreeWsleList](../24/MiFreeWsleList_function_00241168.md) (function, `0x00241168`)
- `0x004EEB42` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x004EEB50` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004EEB66` → [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) (function, `0x00280D10`)
- `0x004EEB7B` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004EEC1B` → [MiRotatedToFrameBuffer](../2C/MiRotatedToFrameBuffer_function_002C5FE4.md) (function, `0x002C5FE4`)
- `0x004EEC5B` → [MiDemoteCombinedPte](../22/MiDemoteCombinedPte_function_0022ABAC.md) (function, `0x0022ABAC`)
- `0x004EEC63` → [MiGetWsleContents](../31/MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x004EEC79` → [MI_WSLE_LOG_ACCESS](../29/MI_WSLE_LOG_ACCESS_function_00294400.md) (function, `0x00294400`)
- `0x004EEC83` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x004EECA7` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x004EECB9` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x004EECD6` → [MiFreeWsleList](../24/MiFreeWsleList_function_00241168.md) (function, `0x00241168`)
- `0x004EECDB` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x004EED22` → [MiFreeWsleList](../24/MiFreeWsleList_function_00241168.md) (function, `0x00241168`)
- `0x004EED27` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x004EED37` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004EED50` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x004EED98` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x004EEDA2` → [MiGetNextVad](../29/MiGetNextVad_function_00297224.md) (function, `0x00297224`)
- `0x004EEDAD` → [MiVadPagesTradable](../40/MiVadPagesTradable_function_00409360.md) (function, `0x00409360`)
- `0x004EEE1F` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004EEE35` → [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) (function, `0x00280D10`)
- `0x004EEE43` → [MiUnlockVa](../40/MiUnlockVa_function_00407F24.md) (function, `0x00407F24`)
- `0x004EEE5D` → [MiWorkingSetIsContended](../2A/MiWorkingSetIsContended_function_002AE520.md) (function, `0x002AE520`)
- `0x004EEE6C` → [MiPageTableLockIsContended](../2A/MiPageTableLockIsContended_function_002AE650.md) (function, `0x002AE650`)
- `0x004EEE75` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x004EEE84` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004EEE91` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x004EEE99` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x004EEEBE` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x004EEECA` → [MiUnlockWorkingSetShared](../27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x004EEEE4` → [MiUnlockVadRange](../../page/87/MiUnlockVadRange_function_0087F590.md) (function, `0x0087F590`)
- `0x004EEEF8` → [KiUnstackDetachProcess](../21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x004EEF07` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004EEF5B` → [MiUnlockVadRange](../../page/87/MiUnlockVadRange_function_0087F590.md) (function, `0x0087F590`)
- `0x004EEF73` → [MiLogUnlockVmTrim](../68/MiLogUnlockVmTrim_function_00689C7C.md) (function, `0x00689C7C`)
- `0x004EEF87` → [KiUnstackDetachProcess](../21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x004EEF96` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004EEFAB` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004EE8A5` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x004EE90E` → [MiLockUnlockCommon](../../page/9E/MiLockUnlockCommon_function_009EA5D0.md) (`.text` → `PAGE`)
  - `0x004EE9A8` → [MiLockVadRange](../../page/87/MiLockVadRange_function_0087F670.md) (`.text` → `PAGE`)
  - `0x004EEEE4` → [MiUnlockVadRange](../../page/87/MiUnlockVadRange_function_0087F590.md) (`.text` → `PAGE`)
  - `0x004EEF5B` → [MiUnlockVadRange](../../page/87/MiUnlockVadRange_function_0087F590.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004EE890  4C 8B DC                        mov r11, rsp
004EE893  53                              push rbx
004EE894  56                              push rsi
004EE895  57                              push rdi
004EE896  41 54                           push r12
004EE898  41 55                           push r13
004EE89A  41 56                           push r14
004EE89C  41 57                           push r15
004EE89E  48 81 EC F0 00 00 00            sub rsp, 0xf0
004EE8A5  48 8B 05 94 BE 91 00            mov rax, qword ptr [rip + 0x91be94]
004EE8AC  48 33 C4                        xor rax, rsp
004EE8AF  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
004EE8B7  4C 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r8
004EE8BF  48 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdx
004EE8C7  4C 8B F1                        mov r14, rcx
004EE8CA  33 DB                           xor ebx, ebx
004EE8CC  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
004EE8D1  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
004EE8D6  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
004EE8DB  0F 57 C0                        xorps xmm0, xmm0
004EE8DE  41 0F 11 43 88                  movups xmmword ptr [r11 - 0x78], xmm0
004EE8E3  41 0F 11 43 98                  movups xmmword ptr [r11 - 0x68], xmm0
004EE8E8  41 0F 11 43 A8                  movups xmmword ptr [r11 - 0x58], xmm0
004EE8ED  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
004EE8F2  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
004EE8F7  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
004EE8FC  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
004EE901  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
004EE906  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
004EE90B  49 8B CE                        mov rcx, r14
004EE90E  E8 BD BC 4F 00                  call 0x1409ea5d0
004EE913  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
004EE917  85 C0                           test eax, eax
004EE919  0F 88 81 06 00 00               js 0x1404eefa0
004EE91F  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
004EE924  49 8D B1 00 04 00 00            lea rsi, [r9 + 0x400]
004EE92B  44 8B E3                        mov r12d, ebx
004EE92E  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
004EE936  44 8B FB                        mov r15d, ebx
004EE939  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
004EE93E  48 8B CE                        mov rcx, rsi
004EE941  E8 8E 40 E7 FF                  call 0x1403629d4
004EE946  F7 D8                           neg eax
004EE948  1B DB                           sbb ebx, ebx
004EE94A  83 E3 08                        and ebx, 8
004EE94D  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
004EE951  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
004EE956  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
004EE95B  49 FF CD                        dec r13
004EE95E  4C 03 EF                        add r13, rdi
004EE961  48 C7 C0 00 F0 FF FF            mov rax, 0xfffffffffffff000
004EE968  4C 23 E8                        and r13, rax
004EE96B  4C 89 AC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r13
004EE973  48 23 F8                        and rdi, rax
004EE976  49 83 FE FF                     cmp r14, -1
004EE97A  74 19                           je 0x1404ee995
004EE97C  4C 8D 84 24 B0 00 00 00         lea r8, [rsp + 0xb0]
004EE984  33 D2                           xor edx, edx
004EE986  49 8B C9                        mov rcx, r9
004EE989  E8 92 7E D2 FF                  call 0x140216820
004EE98E  83 CB 02                        or ebx, 2
004EE991  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
004EE995  4C 21 64 24 60                  and qword ptr [rsp + 0x60], r12
004EE99A  45 33 C9                        xor r9d, r9d
004EE99D  4D 8B C5                        mov r8, r13
004EE9A0  48 8B D7                        mov rdx, rdi
004EE9A3  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
004EE9A8  E8 C3 0C 39 00                  call 0x14087f670
004EE9AD  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
004EE9B5  48 85 C0                        test rax, rax
004EE9B8  0F 84 8A 05 00 00               je 0x1404eef48
004EE9BE  45 33 F6                        xor r14d, r14d
004EE9C1  48 8B CE                        mov rcx, rsi
004EE9C4  E8 27 E2 D8 FF                  call 0x14027cbf0
004EE9C9  88 44 24 40                     mov byte ptr [rsp + 0x40], al
004EE9CD  49 3B FD                        cmp rdi, r13
004EE9D0  0F 87 37 03 00 00               ja 0x1404eed0d
004EE9D6  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
004EE9E0  48 8B C7                        mov rax, rdi
004EE9E3  48 C1 E8 0C                     shr rax, 0xc
004EE9E7  FE C0                           inc al
004EE9E9  A8 0F                           test al, 0xf
004EE9EB  75 7E                           jne 0x1404eea6b
004EE9ED  33 D2                           xor edx, edx
004EE9EF  48 8B CE                        mov rcx, rsi
004EE9F2  E8 29 FB DB FF                  call 0x1402ae520
004EE9F7  85 C0                           test eax, eax
004EE9F9  75 1D                           jne 0x1404eea18
004EE9FB  4D 85 F6                        test r14, r14
004EE9FE  74 0F                           je 0x1404eea0f
004EEA00  49 8B D6                        mov rdx, r14
004EEA03  48 8B CE                        mov rcx, rsi
004EEA06  E8 45 FC DB FF                  call 0x1402ae650
004EEA0B  85 C0                           test eax, eax
004EEA0D  75 09                           jne 0x1404eea18
004EEA0F  E8 CC 89 D8 FF                  call 0x1402773e0
004EEA14  85 C0                           test eax, eax
004EEA16  74 49                           je 0x1404eea61
004EEA18  4D 85 FF                        test r15, r15
004EEA1B  74 1D                           je 0x1404eea3a
004EEA1D  41 83 7F 1C 00                  cmp dword ptr [r15 + 0x1c], 0
004EEA22  74 0E                           je 0x1404eea32
004EEA24  45 33 C0                        xor r8d, r8d
004EEA27  49 8B D7                        mov rdx, r15
004EEA2A  48 8B CE                        mov rcx, rsi
004EEA2D  E8 36 27 D5 FF                  call 0x140241168
004EEA32  E8 39 52 E2 FF                  call 0x140313c70
004EEA37  45 33 FF                        xor r15d, r15d
004EEA3A  4D 85 F6                        test r14, r14
004EEA3D  74 0E                           je 0x1404eea4d
004EEA3F  49 8B D6                        mov rdx, r14
004EEA42  48 8B CE                        mov rcx, rsi
004EEA45  E8 76 84 D2 FF                  call 0x140216ec0
004EEA4A  45 33 F6                        xor r14d, r14d
004EEA4D  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
004EEA51  48 8B CE                        mov rcx, rsi
004EEA54  E8 37 EC D8 FF                  call 0x14027d690
004EEA59  48 8B CE                        mov rcx, rsi
004EEA5C  E8 8F E1 D8 FF                  call 0x14027cbf0
004EEA61  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
004EEA6B  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
004EEA70  49 3B FC                        cmp rdi, r12
004EEA73  77 05                           ja 0x1404eea7a
004EEA75  4D 85 C0                        test r8, r8
004EEA78  75 64                           jne 0x1404eeade
004EEA7A  4D 85 C0                        test r8, r8
004EEA7D  75 0A                           jne 0x1404eea89
004EEA7F  48 8B CF                        mov rcx, rdi
004EEA82  E8 49 7E E2 FF                  call 0x1403168d0
004EEA87  EB 08                           jmp 0x1404eea91
004EEA89  49 8B C8                        mov rcx, r8
004EEA8C  E8 93 87 DA FF                  call 0x140297224
004EEA91  4C 8B C0                        mov r8, rax
004EEA94  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
004EEA99  83 E3 FB                        and ebx, 0xfffffffb
004EEA9C  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
004EEAA0  8B 40 30                        mov eax, dword ptr [rax + 0x30]
004EEAA3  24 70                           and al, 0x70
004EEAA5  3C 40                           cmp al, 0x40
004EEAA7  75 09                           jne 0x1404eeab2
004EEAA9  83 CB 04                        or ebx, 4
004EEAAC  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
004EEAB0  EB 10                           jmp 0x1404eeac2
004EEAB2  49 8B C8                        mov rcx, r8
004EEAB5  E8 A6 A8 F1 FF                  call 0x140409360
004EEABA  85 C0                           test eax, eax
004EEABC  0F 84 4B 02 00 00               je 0x1404eed0d
004EEAC2  41 0F B6 48 21                  movzx ecx, byte ptr [r8 + 0x21]
004EEAC7  48 C1 E1 20                     shl rcx, 0x20
004EEACB  41 8B 40 1C                     mov eax, dword ptr [r8 + 0x1c]
004EEACF  48 0B C8                        or rcx, rax
004EEAD2  48 C1 E1 0C                     shl rcx, 0xc
004EEAD6  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
004EEADE  4C 8B E7                        mov r12, rdi
004EEAE1  49 C1 EC 09                     shr r12, 9
004EEAE5  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
004EEAEF  4C 23 E0                        and r12, rax
004EEAF2  49 8B C3                        mov rax, r11
004EEAF5  4C 03 E0                        add r12, rax
004EEAF8  48 8B CF                        mov rcx, rdi
004EEAFB  48 C1 E9 12                     shr rcx, 0x12
004EEAFF  81 E1 F8 FF FF 3F               and ecx, 0x3ffffff8
004EEB05  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
004EEB0F  48 8B C0                        mov rax, rax
004EEB12  48 03 C1                        add rax, rcx
004EEB15  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004EEB1A  4C 3B F0                        cmp r14, rax
004EEB1D  0F 84 A0 00 00 00               je 0x1404eebc3
004EEB23  4D 85 F6                        test r14, r14
004EEB26  74 2D                           je 0x1404eeb55
004EEB28  4D 85 FF                        test r15, r15
004EEB2B  74 1D                           je 0x1404eeb4a
004EEB2D  41 83 7F 1C 00                  cmp dword ptr [r15 + 0x1c], 0
004EEB32  74 0E                           je 0x1404eeb42
004EEB34  45 33 C0                        xor r8d, r8d
004EEB37  49 8B D7                        mov rdx, r15
004EEB3A  48 8B CE                        mov rcx, rsi
004EEB3D  E8 26 26 D5 FF                  call 0x140241168
004EEB42  E8 29 51 E2 FF                  call 0x140313c70
004EEB47  45 33 FF                        xor r15d, r15d
004EEB4A  49 8B D6                        mov rdx, r14
004EEB4D  48 8B CE                        mov rcx, rsi
004EEB50  E8 6B 83 D2 FF                  call 0x140216ec0
004EEB55  45 33 C9                        xor r9d, r9d
004EEB58  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
004EEB60  49 8B D4                        mov rdx, r12
004EEB63  48 8B CE                        mov rcx, rsi
004EEB66  E8 A5 21 D9 FF                  call 0x140280d10
004EEB6B  4C 8B F0                        mov r14, rax
004EEB6E  48 3B 44 24 68                  cmp rax, qword ptr [rsp + 0x68]
004EEB73  74 4E                           je 0x1404eebc3
004EEB75  48 8B D0                        mov rdx, rax
004EEB78  48 8B CE                        mov rcx, rsi
004EEB7B  E8 40 83 D2 FF                  call 0x140216ec0
004EEB80  45 33 F6                        xor r14d, r14d
004EEB83  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
004EEB8D  49 8B C3                        mov rax, r11
004EEB90  48 C1 E0 19                     shl rax, 0x19
004EEB94  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
004EEB99  48 C1 E7 19                     shl rdi, 0x19
004EEB9D  48 2B F8                        sub rdi, rax
004EEBA0  48 81 C7 00 00 00 10            add rdi, 0x10000000
004EEBA7  48 C1 FF 10                     sar rdi, 0x10
004EEBAB  48 C1 E7 19                     shl rdi, 0x19
004EEBAF  48 2B F8                        sub rdi, rax
004EEBB2  48 C1 FF 10                     sar rdi, 0x10
004EEBB6  C7 44 24 44 2A 00 00 C0         mov dword ptr [rsp + 0x44], 0xc000002a
004EEBBE  E9 39 01 00 00                  jmp 0x1404eecfc
004EEBC3  49 8B 04 24                     mov rax, qword ptr [r12]
004EEBC7  A8 01                           test al, 1
004EEBC9  0F 84 14 01 00 00               je 0x1404eece3
004EEBCF  48 C1 E8 0C                     shr rax, 0xc
004EEBD3  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
004EEBDD  48 23 C1                        and rax, rcx
004EEBE0  48 8D 0C 40                     lea rcx, [rax + rax*2]
004EEBE4  48 C1 E1 04                     shl rcx, 4
004EEBE8  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
004EEBF2  48 03 C8                        add rcx, rax
004EEBF5  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
004EEBFA  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
004EEBFE  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
004EEC08  48 0B D0                        or rdx, rax
004EEC0B  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
004EEC13  F6 C3 04                        test bl, 4
004EEC16  74 1D                           je 0x1404eec35
004EEC18  49 8B CC                        mov rcx, r12
004EEC1B  E8 C4 73 DD FF                  call 0x1402c5fe4
004EEC20  85 C0                           test eax, eax
004EEC22  0F 85 C3 00 00 00               jne 0x1404eeceb
004EEC28  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
004EEC2D  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
004EEC35  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
004EEC39  48 0F BA E0 28                  bt rax, 0x28
004EEC3E  72 20                           jb 0x1404eec60
004EEC40  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
004EEC44  48 85 C0                        test rax, rax
004EEC47  78 17                           js 0x1404eec60
004EEC49  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
004EEC4D  48 85 C0                        test rax, rax
004EEC50  74 0E                           je 0x1404eec60
004EEC52  4C 8B C2                        mov r8, rdx
004EEC55  49 8B D4                        mov rdx, r12
004EEC58  48 8B CE                        mov rcx, rsi
004EEC5B  E8 4C BF D3 FF                  call 0x14022abac
004EEC60  48 8B D7                        mov rdx, rdi
004EEC63  E8 D8 78 E2 FF                  call 0x140316540
004EEC68  24 0F                           and al, 0xf
004EEC6A  3C 08                           cmp al, 8
004EEC6C  74 7D                           je 0x1404eeceb
004EEC6E  F6 C3 08                        test bl, 8
004EEC71  74 0B                           je 0x1404eec7e
004EEC73  49 8B D4                        mov rdx, r12
004EEC76  48 8B CE                        mov rcx, rsi
004EEC79  E8 82 57 DA FF                  call 0x140294400
004EEC7E  4D 85 FF                        test r15, r15
004EEC81  75 29                           jne 0x1404eecac
004EEC83  E8 08 40 D5 FF                  call 0x140242c90
004EEC88  4C 8D B8 28 10 00 00            lea r15, [rax + 0x1028]
004EEC8F  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
004EEC97  41 B9 02 00 00 00               mov r9d, 2
004EEC9D  45 8B 47 0C                     mov r8d, dword ptr [r15 + 0xc]
004EECA1  48 8B D6                        mov rdx, rsi
004EECA4  49 8B CF                        mov rcx, r15
004EECA7  E8 54 62 DA FF                  call 0x140294f00
004EECAC  45 33 C9                        xor r9d, r9d
004EECAF  45 8D 41 01                     lea r8d, [r9 + 1]
004EECB3  48 8B D7                        mov rdx, rdi
004EECB6  49 8B CF                        mov rcx, r15
004EECB9  E8 B2 49 DA FF                  call 0x140293670
004EECBE  48 FF 44 24 70                  inc qword ptr [rsp + 0x70]
004EECC3  41 8B 47 0C                     mov eax, dword ptr [r15 + 0xc]
004EECC7  41 39 47 1C                     cmp dword ptr [r15 + 0x1c], eax
004EECCB  75 16                           jne 0x1404eece3
004EECCD  45 33 C0                        xor r8d, r8d
004EECD0  49 8B D7                        mov rdx, r15
004EECD3  48 8B CE                        mov rcx, rsi
004EECD6  E8 8D 24 D5 FF                  call 0x140241168
004EECDB  E8 90 4F E2 FF                  call 0x140313c70
004EECE0  45 33 FF                        xor r15d, r15d
004EECE3  C7 44 24 44 2A 00 00 C0         mov dword ptr [rsp + 0x44], 0xc000002a
004EECEB  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
004EECF5  48 81 C7 00 10 00 00            add rdi, 0x1000
004EECFC  49 3B FD                        cmp rdi, r13
004EECFF  4C 8B A4 24 88 00 00 00         mov r12, qword ptr [rsp + 0x88]
004EED07  0F 86 D3 FC FF FF               jbe 0x1404ee9e0
004EED0D  4D 85 FF                        test r15, r15
004EED10  74 1A                           je 0x1404eed2c
004EED12  41 83 7F 1C 00                  cmp dword ptr [r15 + 0x1c], 0
004EED17  74 0E                           je 0x1404eed27
004EED19  45 33 C0                        xor r8d, r8d
004EED1C  49 8B D7                        mov rdx, r15
004EED1F  48 8B CE                        mov rcx, rsi
004EED22  E8 41 24 D5 FF                  call 0x140241168
004EED27  E8 44 4F E2 FF                  call 0x140313c70
004EED2C  4D 85 F6                        test r14, r14
004EED2F  74 0E                           je 0x1404eed3f
004EED31  49 8B D6                        mov rdx, r14
004EED34  48 8B CE                        mov rcx, rsi
004EED37  E8 84 81 D2 FF                  call 0x140216ec0
004EED3C  45 33 F6                        xor r14d, r14d
004EED3F  81 7C 24 44 2A 00 00 C0         cmp dword ptr [rsp + 0x44], 0xc000002a
004EED47  75 1E                           jne 0x1404eed67
004EED49  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
004EED4D  48 8B CE                        mov rcx, rsi
004EED50  E8 3B E9 D8 FF                  call 0x14027d690
004EED55  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
004EED5A  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
004EED62  E9 E1 01 00 00                  jmp 0x1404eef48
004EED67  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
004EED6C  48 81 E7 00 F0 FF FF            and rdi, 0xfffffffffffff000
004EED73  45 33 E4                        xor r12d, r12d
004EED76  45 33 FF                        xor r15d, r15d
004EED79  49 3B FD                        cmp rdi, r13
004EED7C  0F 87 31 01 00 00               ja 0x1404eeeb3
004EED82  8A 5C 24 40                     mov bl, byte ptr [rsp + 0x40]
004EED86  49 3B FC                        cmp rdi, r12
004EED89  77 05                           ja 0x1404eed90
004EED8B  4D 85 FF                        test r15, r15
004EED8E  75 3E                           jne 0x1404eedce
004EED90  4D 85 FF                        test r15, r15
004EED93  75 0A                           jne 0x1404eed9f
004EED95  48 8B CF                        mov rcx, rdi
004EED98  E8 33 7B E2 FF                  call 0x1403168d0
004EED9D  EB 08                           jmp 0x1404eeda7
004EED9F  49 8B CF                        mov rcx, r15
004EEDA2  E8 7D 84 DA FF                  call 0x140297224
004EEDA7  4C 8B F8                        mov r15, rax
004EEDAA  48 8B C8                        mov rcx, rax
004EEDAD  E8 AE A5 F1 FF                  call 0x140409360
004EEDB2  85 C0                           test eax, eax
004EEDB4  0F 84 F5 00 00 00               je 0x1404eeeaf
004EEDBA  45 0F B6 67 21                  movzx r12d, byte ptr [r15 + 0x21]
004EEDBF  49 C1 E4 20                     shl r12, 0x20
004EEDC3  41 8B 47 1C                     mov eax, dword ptr [r15 + 0x1c]
004EEDC7  4C 0B E0                        or r12, rax
004EEDCA  49 C1 E4 0C                     shl r12, 0xc
004EEDCE  4C 8B EF                        mov r13, rdi
004EEDD1  49 C1 ED 09                     shr r13, 9
004EEDD5  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
004EEDDF  4C 23 E8                        and r13, rax
004EEDE2  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
004EEDEC  48 8B C0                        mov rax, rax
004EEDEF  4C 03 E8                        add r13, rax
004EEDF2  48 8B CF                        mov rcx, rdi
004EEDF5  48 C1 E9 12                     shr rcx, 0x12
004EEDF9  81 E1 F8 FF FF 3F               and ecx, 0x3ffffff8
004EEDFF  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
004EEE09  48 8B C0                        mov rax, rax
004EEE0C  48 03 C8                        add rcx, rax
004EEE0F  4C 3B F1                        cmp r14, rcx
004EEE12  74 29                           je 0x1404eee3d
004EEE14  4D 85 F6                        test r14, r14
004EEE17  74 0B                           je 0x1404eee24
004EEE19  49 8B D6                        mov rdx, r14
004EEE1C  48 8B CE                        mov rcx, rsi
004EEE1F  E8 9C 80 D2 FF                  call 0x140216ec0
004EEE24  45 33 C9                        xor r9d, r9d
004EEE27  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
004EEE2F  49 8B D5                        mov rdx, r13
004EEE32  48 8B CE                        mov rcx, rsi
004EEE35  E8 D6 1E D9 FF                  call 0x140280d10
004EEE3A  4C 8B F0                        mov r14, rax
004EEE3D  48 8B D7                        mov rdx, rdi
004EEE40  48 8B CE                        mov rcx, rsi
004EEE43  E8 DC 90 F1 FF                  call 0x140407f24
004EEE48  48 81 C7 00 10 00 00            add rdi, 0x1000
004EEE4F  48 F7 C7 00 F0 00 00            test rdi, 0xf000
004EEE56  75 46                           jne 0x1404eee9e
004EEE58  33 D2                           xor edx, edx
004EEE5A  48 8B CE                        mov rcx, rsi
004EEE5D  E8 BE F6 DB FF                  call 0x1402ae520
004EEE62  85 C0                           test eax, eax
004EEE64  75 18                           jne 0x1404eee7e
004EEE66  49 8B D6                        mov rdx, r14
004EEE69  48 8B CE                        mov rcx, rsi
004EEE6C  E8 DF F7 DB FF                  call 0x1402ae650
004EEE71  85 C0                           test eax, eax
004EEE73  75 09                           jne 0x1404eee7e
004EEE75  E8 66 85 D8 FF                  call 0x1402773e0
004EEE7A  85 C0                           test eax, eax
004EEE7C  74 20                           je 0x1404eee9e
004EEE7E  49 8B D6                        mov rdx, r14
004EEE81  48 8B CE                        mov rcx, rsi
004EEE84  E8 37 80 D2 FF                  call 0x140216ec0
004EEE89  45 33 F6                        xor r14d, r14d
004EEE8C  8A D3                           mov dl, bl
004EEE8E  48 8B CE                        mov rcx, rsi
004EEE91  E8 FA E7 D8 FF                  call 0x14027d690
004EEE96  48 8B CE                        mov rcx, rsi
004EEE99  E8 52 DD D8 FF                  call 0x14027cbf0
004EEE9E  4C 8B AC 24 98 00 00 00         mov r13, qword ptr [rsp + 0x98]
004EEEA6  49 3B FD                        cmp rdi, r13
004EEEA9  0F 86 D7 FE FF FF               jbe 0x1404eed86
004EEEAF  8B 5C 24 48                     mov ebx, dword ptr [rsp + 0x48]
004EEEB3  4D 85 F6                        test r14, r14
004EEEB6  74 0B                           je 0x1404eeec3
004EEEB8  49 8B D6                        mov rdx, r14
004EEEBB  48 8B CE                        mov rcx, rsi
004EEEBE  E8 FD 7F D2 FF                  call 0x140216ec0
004EEEC3  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
004EEEC7  48 8B CE                        mov rcx, rsi
004EEECA  E8 C1 E7 D8 FF                  call 0x14027d690
004EEECF  45 33 C9                        xor r9d, r9d
004EEED2  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
004EEEDA  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
004EEEDF  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
004EEEE4  E8 A7 06 39 00                  call 0x14087f590
004EEEE9  F6 C3 02                        test bl, 2
004EEEEC  74 0F                           je 0x1404eeefd
004EEEEE  33 D2                           xor edx, edx
004EEEF0  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
004EEEF8  E8 33 8E D2 FF                  call 0x140217d30
004EEEFD  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
004EEF02  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
004EEF07  E8 D4 89 E0 FF                  call 0x1402f78e0
004EEF0C  90                              nop
004EEF0D  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
004EEF12  48 8B C7                        mov rax, rdi
004EEF15  48 C7 C1 00 F0 FF FF            mov rcx, 0xfffffffffffff000
004EEF1C  48 23 C1                        and rax, rcx
004EEF1F  4C 2B E8                        sub r13, rax
004EEF22  49 81 C5 00 10 00 00            add r13, 0x1000
004EEF29  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
004EEF31  4C 89 28                        mov qword ptr [rax], r13
004EEF34  48 23 F9                        and rdi, rcx
004EEF37  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
004EEF3F  48 89 38                        mov qword ptr [rax], rdi
004EEF42  33 C0                           xor eax, eax
004EEF44  EB 5A                           jmp 0x1404eefa0
004EEF46  EB 58                           jmp 0x1404eefa0
004EEF48  45 33 C9                        xor r9d, r9d
004EEF4B  4C 8B C0                        mov r8, rax
004EEF4E  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
004EEF53  48 8B D7                        mov rdx, rdi
004EEF56  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
004EEF5B  E8 30 06 39 00                  call 0x14087f590
004EEF60  4D 85 FF                        test r15, r15
004EEF63  74 13                           je 0x1404eef78
004EEF65  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
004EEF6A  4C 8B C7                        mov r8, rdi
004EEF6D  49 8B D7                        mov rdx, r15
004EEF70  48 8B CE                        mov rcx, rsi
004EEF73  E8 04 AD 19 00                  call 0x140689c7c
004EEF78  F6 C3 02                        test bl, 2
004EEF7B  74 0F                           je 0x1404eef8c
004EEF7D  33 D2                           xor edx, edx
004EEF7F  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
004EEF87  E8 A4 8D D2 FF                  call 0x140217d30
004EEF8C  BA 4D 6D 56 6D                  mov edx, 0x6d566d4d
004EEF91  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
004EEF96  E8 45 89 E0 FF                  call 0x1402f78e0
004EEF9B  B8 2A 00 00 C0                  mov eax, 0xc000002a
004EEFA0  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
004EEFA8  48 33 CC                        xor rcx, rsp
004EEFAB  E8 90 D6 1B 00                  call 0x1406ac640
004EEFB0  48 81 C4 F0 00 00 00            add rsp, 0xf0
004EEFB7  41 5F                           pop r15
004EEFB9  41 5E                           pop r14
004EEFBB  41 5D                           pop r13
004EEFBD  41 5C                           pop r12
004EEFBF  5F                              pop rdi
004EEFC0  5E                              pop rsi
004EEFC1  5B                              pop rbx
004EEFC2  C3                              ret
004EEFC3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtUnlockVirtualMemory(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int8 v_stack_mE8;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 9551508)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m88 = a3;
    v_stack_m80 = a2;
    v_rbx = 0;
    v_stack_mB0 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm0;
    v_stack_mF8 = v_stack_mD8;
    v_stack_m100 = v_stack_mB0;
    v_stack_m108 = v_stack_mD0;
    result = MiLockUnlockCommon(a1, a2, a3, a4);
    v_stack_mE4 = (unsigned int)(result);
    if (sign_flag) goto loc_004EEFA0;
    v_stack_mA0 = 0;
    v_stack_mB8 = 0;
    result = MiVmAccessLoggingEnabled(v_stack_mD8 + 1024, a2, a3, v_stack_mD8);
    result = (unsigned int)(-(result));
    v_rbx = (unsigned int)((v_rbx) & (8));
    v_stack_mE0 = (unsigned int)(v_rbx);
    v_r13 = (v_stack_mB0) - 1;
    v_r13 = (v_r13) + (v_stack_mD0);
    v_r13 = (v_r13) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m90 = v_r13;
    v_rdi = (v_stack_mD0) & (0xFFFFFFFFFFFFF000ULL);
    result = 0xFFFFFFFFFFFFF000ULL;
    if (a1 != -1) {
        a3 = v_stack_m78;
        a2 = 0;
        a1 = v_stack_mD8;
        result = KiStackAttachProcess(a1, a2, a3, v_stack_mD8);
        v_rbx = (unsigned int)((v_rbx) | (2));
        v_stack_mE0 = (unsigned int)(v_rbx);
    }
    a4 = 0;
    result = MiLockVadRange(v_stack_mD8, v_rdi, v_r13, a4);
    v_stack_m98 = result;
    if (result == 0) goto loc_004EEF48;
    v_r14 = 0;
    result = MiLockWorkingSetShared(v_stack_mD8 + 1024, v_rdi, v_r13, a4);
    v_stack_mE8 = (unsigned __int8)(result);
    if (v_rdi > v_r13) goto loc_004EED0D;
loc_004EE9E0:
    result = (v_rdi) >> (12);
    result = (unsigned __int8)((result) + 1);
    if ((((unsigned __int8)(result)) & (15)) != 0) goto loc_004EEA6B;
    a2 = 0;
    result = MiWorkingSetIsContended(v_stack_mD8 + 1024, a2, v_r13, a4);
    if ((unsigned int)(result) != 0) goto loc_004EEA18;
    if (0 == 0) goto loc_004EEA0F;
    result = MiPageTableLockIsContended(v_stack_mD8 + 1024, 0, v_r13, a4);
    if ((unsigned int)(result) != 0) goto loc_004EEA18;
loc_004EEA0F:
    result = KeShouldYieldProcessor(v_stack_mD8 + 1024, 0, v_r13, a4);
    if ((unsigned int)(result) == 0) goto loc_004EEA61;
loc_004EEA18:
    if (0 == 0) goto loc_004EEA3A;
    if ((*(unsigned int *)(0 + 28)) != 0) {
        a3 = 0;
        a2 = 0;
        a1 = v_stack_mD8 + 1024;
        result = MiFreeWsleList(a1, a2, a3, a4);
    }
    result = MiReleaseProcessorFlushList(a1, a2, a3, a4);
    v_r15 = 0;
loc_004EEA3A:
    if (0 != 0) {
        a2 = 0;
        a1 = v_stack_mD8 + 1024;
        result = MiUnlockPageTable(a1, a2, a3, a4);
        v_r14 = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_mD8 + 1024, v_stack_mE8, a3, a4);
    result = MiLockWorkingSetShared(v_stack_mD8 + 1024, v_stack_mE8, a3, a4);
loc_004EEA61:
loc_004EEA6B:
    if (v_rdi > 0) goto loc_004EEA7A;
    if (v_stack_mC8 != 0) goto loc_004EEADE;
loc_004EEA7A:
    if (v_stack_mC8 != 0) goto loc_004EEA89;
    result = MiLocateAddress(v_rdi, v_stack_mE8, v_stack_mC8, a4);
    goto loc_004EEA91;
loc_004EEA89:
    result = MiGetNextVad(v_stack_mC8, v_stack_mE8, v_stack_mC8, a4);
loc_004EEA91:
    v_stack_mC8 = result;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFBULL));
    v_stack_mE0 = (unsigned int)(v_rbx);
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(result + 48))) & (112));
    if (((unsigned __int8)(result)) != 64) goto loc_004EEAB2;
    v_rbx = (unsigned int)((v_rbx) | (4));
    v_stack_mE0 = (unsigned int)(v_rbx);
    goto loc_004EEAC2;
loc_004EEAB2:
    result = MiVadPagesTradable(result, v_stack_mE8, result, a4);
    if ((unsigned int)(result) == 0) goto loc_004EED0D;
loc_004EEAC2:
    a1 = (*(unsigned __int8 *)(result + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(result + 28)));
    a1 = (a1) << (12);
    v_stack_mA0 = a1;
loc_004EEADE:
    v_r12 = (v_rdi) >> (9);
    v_r12 = (v_r12) & ((unsigned int)(*(unsigned int *)(result + 28)));
    v_r12 = (v_r12) + (v_rsp);
    a1 = (v_rdi) >> (18);
    a1 = (unsigned int)((a1) & (0x3FFFFFF8ULL));
    result = (v_rsp) + (a1);
    v_stack_mC0 = result;
    if (0 == result) goto loc_004EEBC3;
    if (0 == 0) goto loc_004EEB55;
    if (0 == 0) goto loc_004EEB4A;
    if ((*(unsigned int *)(v_r15 + 28)) != 0) {
        a3 = 0;
        a2 = 0;
        a1 = v_stack_mD8 + 1024;
        result = MiFreeWsleList(a1, a2, a3, a4);
    }
    result = MiReleaseProcessorFlushList(a1, a2, a3, a4);
    v_r15 = 0;
loc_004EEB4A:
    result = MiUnlockPageTable(v_stack_mD8 + 1024, 0, a3, a4);
loc_004EEB55:
    a4 = 0;
    result = MiLockLowestValidPageTableEx(v_stack_mD8 + 1024, v_r12, v_stack_mA8, a4);
    if (result == v_stack_mC0) goto loc_004EEBC3;
    result = MiUnlockPageTable(v_stack_mD8 + 1024, result, v_stack_mA8, a4);
    v_r14 = 0;
    result = (v_rsp) << (25);
    v_rdi = (v_stack_mC0) << (25);
    v_rdi = (v_rdi) - (result);
    v_rdi = (v_rdi) + (0x10000000ULL);
    v_rdi = (v_rdi) >> (16);
    v_rdi = (v_rdi) << (25);
    v_rdi = (v_rdi) - (result);
    v_rdi = (v_rdi) >> (16);
    v_stack_mE4 = 0xC000002AULL;
    goto loc_004EECFC;
loc_004EEBC3:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r12))) & (1)) == 0) goto loc_004EECE3;
    result = (*(unsigned __int64 *)(v_r12)) >> (12);
    result = (result) & (v_stack_mD8 + 1024);
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    v_stack_mC0 = a1;
    a2 = (*(unsigned __int64 *)(a1 + 8)) | (result);
    v_stack_mA8 = a2;
    if ((((unsigned __int8)(v_rbx)) & (4)) == 0) goto loc_004EEC35;
    result = MiRotatedToFrameBuffer(v_r12, a2, v_stack_mA8, a4);
    if ((unsigned int)(result) != 0) goto loc_004EECEB;
loc_004EEC35:
    if (condition_is_below) goto loc_004EEC60;
    if (sign_flag) goto loc_004EEC60;
    result = *(unsigned __int64 *)(v_stack_mC0 + 8);
    if (*(unsigned __int64 *)(v_stack_mC0 + 8) != 0) {
        a3 = v_stack_mA8;
        a2 = v_r12;
        a1 = v_stack_mD8 + 1024;
        result = MiDemoteCombinedPte(a1, a2, a3, a4);
    }
    result = MiGetWsleContents(a1, v_rdi, a3, a4);
    result = (unsigned __int8)((result) & (15));
    if (((unsigned __int8)(result)) == 8) goto loc_004EECEB;
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) {
        a2 = v_r12;
        a1 = v_stack_mD8 + 1024;
        result = MI_WSLE_LOG_ACCESS(a1, a2, a3, a4);
    }
    if (0 == 0) {
        result = MiGetProcessorFlushList(a1, a2, a3, a4);
        v_r15 = result + 4136;
        v_stack_m108 = 1;
        a4 = 2;
        a3 = *(unsigned int *)(v_r15 + 12);
        a2 = v_stack_mD8 + 1024;
        a1 = v_r15;
        result = MiInitializeTbFlushList(a1, a2, a3, a4);
    }
    a4 = 0;
    result = MiInsertTbFlushEntry(v_r15, v_rdi, a4 + 1, a4);
    result = (unsigned int)(*(unsigned int *)(v_r15 + 12));
    if ((*(unsigned int *)(v_r15 + 28)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 12))))) {
        a3 = 0;
        a2 = v_r15;
        a1 = v_stack_mD8 + 1024;
        result = MiFreeWsleList(a1, a2, a3, a4);
        result = MiReleaseProcessorFlushList(a1, a2, a3, a4);
        v_r15 = 0;
    }
    v_stack_mE4 = 0xC000002AULL;
loc_004EECEB:
    v_rdi = (v_rdi) + (0x1000ULL);
loc_004EECFC:
    if (v_rdi <= v_r13) goto loc_004EE9E0;
loc_004EED0D:
    if (0 == 0) goto loc_004EED2C;
    if ((*(unsigned int *)(v_r15 + 28)) != 0) {
        a3 = 0;
        a2 = 0;
        a1 = v_stack_mD8 + 1024;
        result = MiFreeWsleList(a1, a2, a3, a4);
    }
    result = MiReleaseProcessorFlushList(a1, a2, a3, a4);
loc_004EED2C:
    if (0 != 0) {
        a2 = 0;
        a1 = v_stack_mD8 + 1024;
        result = MiUnlockPageTable(a1, a2, a3, a4);
        v_r14 = 0;
    }
    if (v_stack_mE4 != 0xC000002AULL) goto loc_004EED67;
    result = MiUnlockWorkingSetShared(v_stack_mD8 + 1024, v_stack_mE8, a3, a4);
    goto loc_004EEF48;
loc_004EED67:
    v_rdi = (v_stack_mD0) & (0xFFFFFFFFFFFFF000ULL);
    v_r12 = 0;
    v_r15 = 0;
    if (v_rdi > v_r13) goto loc_004EEEB3;
loc_004EED86:
    if (v_rdi > 0) goto loc_004EED90;
    if (0 != 0) goto loc_004EEDCE;
loc_004EED90:
    if (0 != 0) goto loc_004EED9F;
    result = MiLocateAddress(v_rdi, v_stack_mE8, a3, a4);
    goto loc_004EEDA7;
loc_004EED9F:
    result = MiGetNextVad(0, v_stack_mE8, a3, a4);
loc_004EEDA7:
    result = MiVadPagesTradable(result, v_stack_mE8, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_004EEEAF;
    v_r12 = (*(unsigned __int8 *)(result + 33)) << (32);
    v_r12 = (v_r12) | ((unsigned int)(*(unsigned int *)(result + 28)));
    v_r12 = (v_r12) << (12);
loc_004EEDCE:
    v_r13 = (v_rdi) >> (9);
    v_r13 = (v_r13) & ((unsigned int)(*(unsigned int *)(result + 28)));
    v_r13 = (v_r13) + ((unsigned int)(*(unsigned int *)(result + 28)));
    a1 = (v_rdi) >> (18);
    a1 = (unsigned int)((a1) & (0x3FFFFFF8ULL));
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(result + 28)));
    if (0 == a1) goto loc_004EEE3D;
    result = (unsigned int)(*(unsigned int *)(result + 28));
    if (0 != 0) {
        a2 = 0;
        a1 = v_stack_mD8 + 1024;
        result = MiUnlockPageTable(a1, a2, a3, a4);
    }
    a4 = 0;
    result = MiLockLowestValidPageTableEx(v_stack_mD8 + 1024, v_r13, v_stack_mA8, a4);
loc_004EEE3D:
    result = MiUnlockVa(v_stack_mD8 + 1024, v_rdi, v_stack_mA8, a4);
    v_rdi = (v_rdi) + (0x1000ULL);
    if (((v_rdi) & (0xF000ULL)) != 0) goto loc_004EEE9E;
    a2 = 0;
    result = MiWorkingSetIsContended(v_stack_mD8 + 1024, a2, v_stack_mA8, a4);
    if ((unsigned int)(result) != 0) goto loc_004EEE7E;
    result = MiPageTableLockIsContended(v_stack_mD8 + 1024, result, v_stack_mA8, a4);
    if ((unsigned int)(result) != 0) goto loc_004EEE7E;
    result = KeShouldYieldProcessor(v_stack_mD8 + 1024, result, v_stack_mA8, a4);
    v_r14 = result;
    if ((unsigned int)(result) != 0) {
        a2 = result;
        a1 = v_stack_mD8 + 1024;
        result = MiUnlockPageTable(a1, a2, v_stack_mA8, a4);
        v_r14 = 0;
        a2 = (unsigned __int8)(v_stack_mE8);
        a1 = v_stack_mD8 + 1024;
        result = MiUnlockWorkingSetShared(a1, a2, v_stack_mA8, a4);
        a1 = v_stack_mD8 + 1024;
        result = MiLockWorkingSetShared(a1, a2, v_stack_mA8, a4);
    }
    if (v_rdi <= v_stack_m90) goto loc_004EED86;
loc_004EEEAF:
loc_004EEEB3:
    if (0 != 0) {
        a2 = 0;
        a1 = v_stack_mD8 + 1024;
        result = MiUnlockPageTable(a1, a2, v_stack_mA8, a4);
    }
    result = MiUnlockWorkingSetShared(v_stack_mD8 + 1024, v_stack_mE8, v_stack_mA8, a4);
    a4 = 0;
    result = MiUnlockVadRange(v_stack_mD8, v_stack_mD0, v_stack_m98, a4);
    if ((((unsigned __int8)((unsigned int)(v_stack_mE0))) & (2)) != 0) {
        a2 = 0;
        a1 = v_stack_m78;
        result = KiUnstackDetachProcess(a1, a2, v_stack_m98, a4);
    }
    result = ObfDereferenceObjectWithTag(v_stack_mD8, (unsigned int)(0x6D566D4DULL), v_stack_m98, a4);
    result = (v_stack_mD0) & (0xFFFFFFFFFFFFF000ULL);
    v_r13 = (v_stack_m90) - (result);
    v_r13 = (v_r13) + (0x1000ULL);
    *(unsigned __int64 *)(v_stack_m88) = v_r13;
    v_rdi = (v_stack_mD0) & (0xFFFFFFFFFFFFF000ULL);
    *(unsigned __int64 *)(v_stack_m80) = v_rdi;
    result = 0;
    goto loc_004EEFA0;
loc_004EEF48:
    a4 = 0;
    result = MiUnlockVadRange(v_stack_mD8, v_stack_mD0, 0, a4);
    if (result != 0) {
        a4 = v_stack_mB0;
        a3 = v_stack_mD0;
        a2 = result;
        a1 = v_stack_mD8 + 1024;
        result = MiLogUnlockVmTrim(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)((unsigned int)(v_stack_mE0))) & (2)) != 0) {
        a2 = 0;
        a1 = v_stack_m78;
        result = KiUnstackDetachProcess(a1, a2, a3, a4);
    }
    result = ObfDereferenceObjectWithTag(v_stack_mD8, (unsigned int)(0x6D566D4DULL), a3, a4);
loc_004EEFA0:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x6D566D4DULL), a3, a4);
    v_rsp = (v_rsp) + (240);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtUnlockVirtualMemory(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m48;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint8_t v_stack_mE8;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0x91BE94)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m88 = Arg3;
    v_stack_m80 = Arg2;
    local_rbx = 0;
    v_stack_mB0 = 0;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    *(uint64_t *)(local_rsp - 0x78) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm0;
    v_stack_mF8 = v_stack_mD8;
    v_stack_m100 = v_stack_mB0;
    v_stack_m108 = v_stack_mD0;
    result = MiLockUnlockCommon(Arg1, Arg2, Arg3, a4);
    v_stack_mE4 = (uint32_t)(result);
    if (sign_flag) goto loc_004EEFA0;
    v_stack_mA0 = 0;
    v_stack_mB8 = 0;
    result = MiVmAccessLoggingEnabled(v_stack_mD8 + 1024, Arg2, Arg3, v_stack_mD8);
    result = (uint32_t)(-(result));
    local_rbx = (uint32_t)((local_rbx) & (8));
    v_stack_mE0 = (uint32_t)(local_rbx);
    local_r13 = (v_stack_mB0) - 1;
    local_r13 = (local_r13) + (v_stack_mD0);
    local_r13 = (local_r13) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m90 = local_r13;
    local_rdi = (v_stack_mD0) & (0xFFFFFFFFFFFFF000ULL);
    result = 0xFFFFFFFFFFFFF000ULL;
    if (Arg1 != -1) {
        Arg3 = v_stack_m78;
        Arg2 = 0;
        Arg1 = v_stack_mD8;
        result = KiStackAttachProcess(Arg1, Arg2, Arg3, v_stack_mD8);
        local_rbx = (uint32_t)((local_rbx) | (2));
        v_stack_mE0 = (uint32_t)(local_rbx);
    }
    a4 = 0;
    result = MiLockVadRange(v_stack_mD8, local_rdi, local_r13, a4);
    v_stack_m98 = result;
    if (result == 0) goto loc_004EEF48;
    local_r14 = 0;
    result = MiLockWorkingSetShared(v_stack_mD8 + 1024, local_rdi, local_r13, a4);
    v_stack_mE8 = (uint8_t)(result);
    if (local_rdi > local_r13) goto loc_004EED0D;
loc_004EE9E0:
    result = (local_rdi) >> (12);
    result = (uint8_t)((result) + 1);
    if ((((uint8_t)(result)) & (15)) != 0) goto loc_004EEA6B;
    Arg2 = 0;
    result = MiWorkingSetIsContended(v_stack_mD8 + 1024, Arg2, local_r13, a4);
    if ((uint32_t)(result) != 0) goto loc_004EEA18;
    if (0 == 0) goto loc_004EEA0F;
    result = MiPageTableLockIsContended(v_stack_mD8 + 1024, 0, local_r13, a4);
    if ((uint32_t)(result) != 0) goto loc_004EEA18;
loc_004EEA0F:
    result = KeShouldYieldProcessor(v_stack_mD8 + 1024, 0, local_r13, a4);
    if ((uint32_t)(result) == 0) goto loc_004EEA61;
loc_004EEA18:
    if (0 == 0) goto loc_004EEA3A;
    if ((*(uint32_t *)(0 + 0x1C)) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_mD8 + 1024;
        result = MiFreeWsleList(Arg1, Arg2, Arg3, a4);
    }
    result = MiReleaseProcessorFlushList(Arg1, Arg2, Arg3, a4);
    local_r15 = 0;
loc_004EEA3A:
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mD8 + 1024;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, a4);
        local_r14 = 0;
    }
    result = MiUnlockWorkingSetShared(v_stack_mD8 + 1024, v_stack_mE8, Arg3, a4);
    result = MiLockWorkingSetShared(v_stack_mD8 + 1024, v_stack_mE8, Arg3, a4);
loc_004EEA61:
loc_004EEA6B:
    if (local_rdi > 0) goto loc_004EEA7A;
    if (v_stack_mC8 != 0) goto loc_004EEADE;
loc_004EEA7A:
    if (v_stack_mC8 != 0) goto loc_004EEA89;
    result = MiLocateAddress(local_rdi, v_stack_mE8, v_stack_mC8, a4);
    goto loc_004EEA91;
loc_004EEA89:
    result = MiGetNextVad(v_stack_mC8, v_stack_mE8, v_stack_mC8, a4);
loc_004EEA91:
    v_stack_mC8 = result;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFBULL));
    v_stack_mE0 = (uint32_t)(local_rbx);
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (112));
    if (((uint8_t)(result)) != 64) goto loc_004EEAB2;
    local_rbx = (uint32_t)((local_rbx) | (4));
    v_stack_mE0 = (uint32_t)(local_rbx);
    goto loc_004EEAC2;
loc_004EEAB2:
    result = MiVadPagesTradable(result, v_stack_mE8, result, a4);
    if ((uint32_t)(result) == 0) goto loc_004EED0D;
loc_004EEAC2:
    Arg1 = (*(uint8_t *)(result + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    Arg1 = (Arg1) << (12);
    v_stack_mA0 = Arg1;
loc_004EEADE:
    local_r12 = (local_rdi) >> (9);
    local_r12 = (local_r12) & ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    local_r12 = (local_r12) + (local_rsp);
    Arg1 = (local_rdi) >> (18);
    Arg1 = (uint32_t)((Arg1) & (0x3FFFFFF8ULL));
    result = (local_rsp) + (Arg1);
    v_stack_mC0 = result;
    if (0 == result) goto loc_004EEBC3;
    if (0 == 0) goto loc_004EEB55;
    if (0 == 0) goto loc_004EEB4A;
    if ((*(uint32_t *)(local_r15 + 0x1C)) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_mD8 + 1024;
        result = MiFreeWsleList(Arg1, Arg2, Arg3, a4);
    }
    result = MiReleaseProcessorFlushList(Arg1, Arg2, Arg3, a4);
    local_r15 = 0;
loc_004EEB4A:
    result = MiUnlockPageTable(v_stack_mD8 + 1024, 0, Arg3, a4);
loc_004EEB55:
    a4 = 0;
    result = MiLockLowestValidPageTableEx(v_stack_mD8 + 1024, local_r12, v_stack_mA8, a4);
    if (result == v_stack_mC0) goto loc_004EEBC3;
    result = MiUnlockPageTable(v_stack_mD8 + 1024, result, v_stack_mA8, a4);
    local_r14 = 0;
    result = (local_rsp) << (25);
    local_rdi = (v_stack_mC0) << (25);
    local_rdi = (local_rdi) - (result);
    local_rdi = (local_rdi) + (0x10000000ULL);
    local_rdi = (local_rdi) >> (16);
    local_rdi = (local_rdi) << (25);
    local_rdi = (local_rdi) - (result);
    local_rdi = (local_rdi) >> (16);
    v_stack_mE4 = 0xC000002AULL;
    goto loc_004EECFC;
loc_004EEBC3:
    if ((((uint8_t)(*(uint64_t *)(local_r12))) & (1)) == 0) goto loc_004EECE3;
    result = (*(uint64_t *)(local_r12)) >> (12);
    result = (result) & (v_stack_mD8 + 1024);
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    v_stack_mC0 = Arg1;
    Arg2 = (*(uint64_t *)(Arg1 + 0x8)) | (result);
    v_stack_mA8 = Arg2;
    if ((((uint8_t)(local_rbx)) & (4)) == 0) goto loc_004EEC35;
    result = MiRotatedToFrameBuffer(local_r12, Arg2, v_stack_mA8, a4);
    if ((uint32_t)(result) != 0) goto loc_004EECEB;
loc_004EEC35:
    if (condition_is_below) goto loc_004EEC60;
    if (sign_flag) goto loc_004EEC60;
    result = *(uint64_t *)(v_stack_mC0 + 0x8);
    if (*(uint64_t *)(v_stack_mC0 + 0x8) != 0) {
        Arg3 = v_stack_mA8;
        Arg2 = local_r12;
        Arg1 = v_stack_mD8 + 1024;
        result = MiDemoteCombinedPte(Arg1, Arg2, Arg3, a4);
    }
    result = MiGetWsleContents(Arg1, local_rdi, Arg3, a4);
    result = (uint8_t)((result) & (15));
    if (((uint8_t)(result)) == 8) goto loc_004EECEB;
    if ((((uint8_t)(local_rbx)) & (8)) != 0) {
        Arg2 = local_r12;
        Arg1 = v_stack_mD8 + 1024;
        result = MI_WSLE_LOG_ACCESS(Arg1, Arg2, Arg3, a4);
    }
    if (0 == 0) {
        result = MiGetProcessorFlushList(Arg1, Arg2, Arg3, a4);
        local_r15 = result + 4136;
        v_stack_m108 = 1;
        a4 = 2;
        Arg3 = *(uint32_t *)(local_r15 + 0xC);
        Arg2 = v_stack_mD8 + 1024;
        Arg1 = local_r15;
        result = MiInitializeTbFlushList(Arg1, Arg2, Arg3, a4);
    }
    a4 = 0;
    result = MiInsertTbFlushEntry(local_r15, local_rdi, a4 + 1, a4);
    result = (uint32_t)(*(uint32_t *)(local_r15 + 0xC));
    if ((*(uint32_t *)(local_r15 + 0x1C)) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0xC))))) {
        Arg3 = 0;
        Arg2 = local_r15;
        Arg1 = v_stack_mD8 + 1024;
        result = MiFreeWsleList(Arg1, Arg2, Arg3, a4);
        result = MiReleaseProcessorFlushList(Arg1, Arg2, Arg3, a4);
        local_r15 = 0;
    }
    v_stack_mE4 = 0xC000002AULL;
loc_004EECEB:
    local_rdi = (local_rdi) + (0x1000ULL);
loc_004EECFC:
    if (local_rdi <= local_r13) goto loc_004EE9E0;
loc_004EED0D:
    if (0 == 0) goto loc_004EED2C;
    if ((*(uint32_t *)(local_r15 + 0x1C)) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_mD8 + 1024;
        result = MiFreeWsleList(Arg1, Arg2, Arg3, a4);
    }
    result = MiReleaseProcessorFlushList(Arg1, Arg2, Arg3, a4);
loc_004EED2C:
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mD8 + 1024;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, a4);
        local_r14 = 0;
    }
    if (v_stack_mE4 != 0xC000002AULL) goto loc_004EED67;
    result = MiUnlockWorkingSetShared(v_stack_mD8 + 1024, v_stack_mE8, Arg3, a4);
    goto loc_004EEF48;
loc_004EED67:
    local_rdi = (v_stack_mD0) & (0xFFFFFFFFFFFFF000ULL);
    local_r12 = 0;
    local_r15 = 0;
    if (local_rdi > local_r13) goto loc_004EEEB3;
loc_004EED86:
    if (local_rdi > 0) goto loc_004EED90;
    if (0 != 0) goto loc_004EEDCE;
loc_004EED90:
    if (0 != 0) goto loc_004EED9F;
    result = MiLocateAddress(local_rdi, v_stack_mE8, Arg3, a4);
    goto loc_004EEDA7;
loc_004EED9F:
    result = MiGetNextVad(0, v_stack_mE8, Arg3, a4);
loc_004EEDA7:
    result = MiVadPagesTradable(result, v_stack_mE8, Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_004EEEAF;
    local_r12 = (*(uint8_t *)(result + 0x21)) << (32);
    local_r12 = (local_r12) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    local_r12 = (local_r12) << (12);
loc_004EEDCE:
    local_r13 = (local_rdi) >> (9);
    local_r13 = (local_r13) & ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    local_r13 = (local_r13) + ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    Arg1 = (local_rdi) >> (18);
    Arg1 = (uint32_t)((Arg1) & (0x3FFFFFF8ULL));
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    if (0 == Arg1) goto loc_004EEE3D;
    result = (uint32_t)(*(uint32_t *)(result + 0x1C));
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mD8 + 1024;
        result = MiUnlockPageTable(Arg1, Arg2, Arg3, a4);
    }
    a4 = 0;
    result = MiLockLowestValidPageTableEx(v_stack_mD8 + 1024, local_r13, v_stack_mA8, a4);
loc_004EEE3D:
    result = MiUnlockVa(v_stack_mD8 + 1024, local_rdi, v_stack_mA8, a4);
    local_rdi = (local_rdi) + (0x1000ULL);
    if (((local_rdi) & (0xF000ULL)) != 0) goto loc_004EEE9E;
    Arg2 = 0;
    result = MiWorkingSetIsContended(v_stack_mD8 + 1024, Arg2, v_stack_mA8, a4);
    if ((uint32_t)(result) != 0) goto loc_004EEE7E;
    result = MiPageTableLockIsContended(v_stack_mD8 + 1024, result, v_stack_mA8, a4);
    if ((uint32_t)(result) != 0) goto loc_004EEE7E;
    result = KeShouldYieldProcessor(v_stack_mD8 + 1024, result, v_stack_mA8, a4);
    local_r14 = result;
    if ((uint32_t)(result) != 0) {
        Arg2 = result;
        Arg1 = v_stack_mD8 + 1024;
        result = MiUnlockPageTable(Arg1, Arg2, v_stack_mA8, a4);
        local_r14 = 0;
        Arg2 = (uint8_t)(v_stack_mE8);
        Arg1 = v_stack_mD8 + 1024;
        result = MiUnlockWorkingSetShared(Arg1, Arg2, v_stack_mA8, a4);
        Arg1 = v_stack_mD8 + 1024;
        result = MiLockWorkingSetShared(Arg1, Arg2, v_stack_mA8, a4);
    }
    if (local_rdi <= v_stack_m90) goto loc_004EED86;
loc_004EEEAF:
loc_004EEEB3:
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mD8 + 1024;
        result = MiUnlockPageTable(Arg1, Arg2, v_stack_mA8, a4);
    }
    result = MiUnlockWorkingSetShared(v_stack_mD8 + 1024, v_stack_mE8, v_stack_mA8, a4);
    a4 = 0;
    result = MiUnlockVadRange(v_stack_mD8, v_stack_mD0, v_stack_m98, a4);
    if ((((uint8_t)((uint32_t)(v_stack_mE0))) & (2)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m78;
        result = KiUnstackDetachProcess(Arg1, Arg2, v_stack_m98, a4);
    }
    result = ObfDereferenceObjectWithTag(v_stack_mD8, (uint32_t)(0x6D566D4DULL), v_stack_m98, a4);
    result = (v_stack_mD0) & (0xFFFFFFFFFFFFF000ULL);
    local_r13 = (v_stack_m90) - (result);
    local_r13 = (local_r13) + (0x1000ULL);
    *(uint64_t *)(v_stack_m88) = local_r13;
    local_rdi = (v_stack_mD0) & (0xFFFFFFFFFFFFF000ULL);
    *(uint64_t *)(v_stack_m80) = local_rdi;
    result = 0;
    goto loc_004EEFA0;
loc_004EEF48:
    a4 = 0;
    result = MiUnlockVadRange(v_stack_mD8, v_stack_mD0, 0, a4);
    if (result != 0) {
        a4 = v_stack_mB0;
        Arg3 = v_stack_mD0;
        Arg2 = result;
        Arg1 = v_stack_mD8 + 1024;
        result = MiLogUnlockVmTrim(Arg1, Arg2, Arg3, a4);
    }
    if ((((uint8_t)((uint32_t)(v_stack_mE0))) & (2)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m78;
        result = KiUnstackDetachProcess(Arg1, Arg2, Arg3, a4);
    }
    result = ObfDereferenceObjectWithTag(v_stack_mD8, (uint32_t)(0x6D566D4DULL), Arg3, a4);
loc_004EEFA0:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x6D566D4DULL), Arg3, a4);
    local_rsp = (local_rsp) + (240);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004EE890&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
