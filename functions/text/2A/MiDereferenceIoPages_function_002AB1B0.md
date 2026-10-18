# MiDereferenceIoPages

- RVA: `0x002AB1B0`–`0x002AB761` (길이 `1,457` bytes)
- VA: `0x00000001402AB1B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006D058`
- 디코드: `347`개 명령, `1,457/1,457` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x002AB257` → [MiIsPageInHugePfn](MiIsPageInHugePfn_function_002AB770.md) (function, `0x002AB770`)
- `0x002AB304` → [MiLockIoPfnTree](MiLockIoPfnTree_function_002AC8A4.md) (function, `0x002AC8A4`)
- `0x002AB3F7` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002AB415` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002AB4A3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002AB502` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x002AB52C` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002AB57B` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002AB5C7` → [MiIsPageInIoHugeRangeTransition](MiIsPageInIoHugeRangeTransition_function_002AB7A0.md) (function, `0x002AB7A0`)
- `0x002AB664` → [MiReleaseSpinLockShared](../34/MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x002AB672` → [MiLockIoPfnTree](MiLockIoPfnTree_function_002AC8A4.md) (function, `0x002AC8A4`)
- `0x002AB689` → [MiIoSpaceGetBounds](MiIoSpaceGetBounds_function_002AC728.md) (function, `0x002AC728`)
- `0x002AB6E7` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x002AB73B` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002AB75B` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [MiReferenceIoPages](../23/MiReferenceIoPages_function_0023C804.md) at `0x0023CDA7`
- [MiReferenceIoPages](../23/MiReferenceIoPages_function_0023C804.md) at `0x0023D0EC`
- [MiClearMappingAndDereferenceIoSpace](../24/MiClearMappingAndDereferenceIoSpace_function_00247DF0.md) at `0x0024800A`
- [MiClearMappingAndDereferenceIoSpace](../24/MiClearMappingAndDereferenceIoSpace_function_00247DF0.md) at `0x002481DA`
- [MiDereferenceIoPageRuns](MiDereferenceIoPageRuns_function_002AB08C.md) at `0x002AB0CA`
- [MiMapContiguousMemoryLarge](../3B/MiMapContiguousMemoryLarge_function_003B44CC.md) at `0x003B46AA`
- [MiUnmapMdlCommon](../3E/MiUnmapMdlCommon_function_003E7DF0.md) at `0x003E8146`
- [MiDecommitFreePagesTail](../41/MiDecommitFreePagesTail_function_0041ECE0.md) at `0x0041F0B3`
- [sub_006DAA8E](../6D/Unknown_function_006DAA8E.md) at `0x006DAADA`
- [MiRotateToFrameBuffer](../../page/A3/MiRotateToFrameBuffer_function_00A38214.md) at `0x00A3851C`
- [MiReplaceRotateWithDemandZero](../../page/A7/MiReplaceRotateWithDemandZero_function_00A7C010.md) at `0x00A7C1EE`
- [sub_00B2A492](../../page/B2/Unknown_function_00B2A492.md) at `0x00B2A4C3`
- [sub_00B2A4DA](../../page/B2/Unknown_function_00B2A4DA.md) at `0x00B2A51E`
- [sub_00B3A200](../../page/B3/Unknown_function_00B3A200.md) at `0x00B3A219`

### Static image references
- `0x002AB1DA` → RVA `0x00E2DC38` (`.data`; read)
- `0x002AB20C` → RVA `0x00E37280` (`.data`; read)
- `0x002AB22F` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002AB264` → RVA `0x00E37300` (`.data`; read)
- `0x002AB5A9` → RVA `0x00FCF240` (`CACHEALI`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002AB50F` → [sub_006DB2D0](../6D/Unknown_function_006DB2D0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002AB1B0  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
002AB1B5  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
002AB1B9  53                              push rbx
002AB1BA  55                              push rbp
002AB1BB  56                              push rsi
002AB1BC  57                              push rdi
002AB1BD  41 54                           push r12
002AB1BF  41 55                           push r13
002AB1C1  41 56                           push r14
002AB1C3  41 57                           push r15
002AB1C5  48 83 EC 68                     sub rsp, 0x68
002AB1C9  48 8B F2                        mov rsi, rdx
002AB1CC  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
002AB1D1  48 63 D1                        movsxd rdx, ecx
002AB1D4  41 BA 01 00 00 00               mov r10d, 1
002AB1DA  0F B6 0D 57 2A B8 00            movzx ecx, byte ptr [rip + 0xb82a57]
002AB1E1  33 DB                           xor ebx, ebx
002AB1E3  80 C1 F4                        add cl, 0xf4
002AB1E6  89 9C 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], ebx
002AB1ED  41 8B C2                        mov eax, r10d
002AB1F0  48 C7 44 24 40 00 04 00 00      mov qword ptr [rsp + 0x40], 0x400
002AB1F9  48 D3 E0                        shl rax, cl
002AB1FC  4C 8B EA                        mov r13, rdx
002AB1FF  48 FF C8                        dec rax
002AB202  49 C1 E5 06                     shl r13, 6
002AB206  48 23 F0                        and rsi, rax
002AB209  4D 8B E0                        mov r12, r8
002AB20C  48 8D 05 6D C0 B8 00            lea rax, [rip + 0xb8c06d]
002AB213  48 8B EE                        mov rbp, rsi
002AB216  4C 03 E8                        add r13, rax
002AB219  41 8B FA                        mov edi, r10d
002AB21C  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
002AB221  45 0F 20 C6                     mov r14, cr8
002AB225  41 B9 02 00 00 00               mov r9d, 2
002AB22B  45 0F 22 C1                     mov cr8, r9
002AB22F  39 1D EB BA D1 00               cmp dword ptr [rip + 0xd1baeb], ebx
002AB235  0F 85 38 03 00 00               jne 0x1402ab573
002AB23B  B8 11 00 00 00                  mov eax, 0x11
002AB240  45 0F B6 FE                     movzx r15d, r14b
002AB244  41 80 FE 02                     cmp r14b, 2
002AB248  48 8B CE                        mov rcx, rsi
002AB24B  44 0F 44 F8                     cmove r15d, eax
002AB24F  44 89 BC 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r15d
002AB257  E8 14 05 00 00                  call 0x1402ab770
002AB25C  85 C0                           test eax, eax
002AB25E  0F 85 40 04 00 00               jne 0x1402ab6a4
002AB264  48 8B 05 95 C0 B8 00            mov rax, qword ptr [rip + 0xb8c095]
002AB26B  48 85 C0                        test rax, rax
002AB26E  74 22                           je 0x1402ab292
002AB270  48 3B 70 18                     cmp rsi, qword ptr [rax + 0x18]
002AB274  0F 82 7F 04 00 00               jb 0x1402ab6f9
002AB27A  48 3B 70 20                     cmp rsi, qword ptr [rax + 0x20]
002AB27E  76 09                           jbe 0x1402ab289
002AB280  48 8B 40 08                     mov rax, qword ptr [rax + 8]
002AB284  48 85 C0                        test rax, rax
002AB287  75 E7                           jne 0x1402ab270
002AB289  48 85 C0                        test rax, rax
002AB28C  0F 85 6D 03 00 00               jne 0x1402ab5ff
002AB292  48 8D 8E FF FF 03 00            lea rcx, [rsi + 0x3ffff]
002AB299  48 81 E1 00 00 FC FF            and rcx, 0xfffffffffffc0000
002AB2A0  48 3B F1                        cmp rsi, rcx
002AB2A3  75 07                           jne 0x1402ab2ac
002AB2A5  48 8D 8E 00 00 04 00            lea rcx, [rsi + 0x40000]
002AB2AC  48 8B 05 4D C0 B8 00            mov rax, qword ptr [rip + 0xb8c04d]
002AB2B3  48 FF C9                        dec rcx
002AB2B6  48 85 C0                        test rax, rax
002AB2B9  74 27                           je 0x1402ab2e2
002AB2BB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
002AB2C0  48 3B 48 18                     cmp rcx, qword ptr [rax + 0x18]
002AB2C4  0F 82 37 04 00 00               jb 0x1402ab701
002AB2CA  48 3B 70 20                     cmp rsi, qword ptr [rax + 0x20]
002AB2CE  76 09                           jbe 0x1402ab2d9
002AB2D0  48 8B 40 08                     mov rax, qword ptr [rax + 8]
002AB2D4  48 85 C0                        test rax, rax
002AB2D7  75 E7                           jne 0x1402ab2c0
002AB2D9  48 85 C0                        test rax, rax
002AB2DC  0F 85 B1 03 00 00               jne 0x1402ab693
002AB2E2  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
002AB2E7  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
002AB2EC  C7 44 24 5C 03 00 00 00         mov dword ptr [rsp + 0x5c], 3
002AB2F4  83 7C 24 5C 03                  cmp dword ptr [rsp + 0x5c], 3
002AB2F9  0F 85 4C 02 00 00               jne 0x1402ab54b
002AB2FF  B9 05 00 00 00                  mov ecx, 5
002AB304  E8 9B 15 00 00                  call 0x1402ac8a4
002AB309  0F 1F 80 00 00 00 00            nop dword ptr [rax]
002AB310  4D 85 E4                        test r12, r12
002AB313  0F 84 CB 01 00 00               je 0x1402ab4e4
002AB319  48 3B 6C 24 48                  cmp rbp, qword ptr [rsp + 0x48]
002AB31E  0F 82 5D 03 00 00               jb 0x1402ab681
002AB324  48 3B 6C 24 50                  cmp rbp, qword ptr [rsp + 0x50]
002AB329  0F 87 52 03 00 00               ja 0x1402ab681
002AB32F  83 BC 24 B0 00 00 00 01         cmp dword ptr [rsp + 0xb0], 1
002AB337  0F 84 75 01 00 00               je 0x1402ab4b2
002AB33D  85 FF                           test edi, edi
002AB33F  74 2E                           je 0x1402ab36f
002AB341  49 8B 5D 00                     mov rbx, qword ptr [r13]
002AB345  48 85 DB                        test rbx, rbx
002AB348  74 23                           je 0x1402ab36d
002AB34A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
002AB350  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
002AB354  48 3B E8                        cmp rbp, rax
002AB357  72 40                           jb 0x1402ab399
002AB359  48 05 00 02 00 00               add rax, 0x200
002AB35F  48 3B E8                        cmp rbp, rax
002AB362  72 09                           jb 0x1402ab36d
002AB364  48 8B 5B 08                     mov rbx, qword ptr [rbx + 8]
002AB368  48 85 DB                        test rbx, rbx
002AB36B  75 E3                           jne 0x1402ab350
002AB36D  33 FF                           xor edi, edi
002AB36F  48 85 DB                        test rbx, rbx
002AB372  0F 84 C9 03 00 00               je 0x1402ab741
002AB378  4C 8B 73 08                     mov r14, qword ptr [rbx + 8]
002AB37C  48 8B CB                        mov rcx, rbx
002AB37F  4D 85 F6                        test r14, r14
002AB382  74 1A                           je 0x1402ab39e
002AB384  49 8B 06                        mov rax, qword ptr [r14]
002AB387  48 85 C0                        test rax, rax
002AB38A  74 2E                           je 0x1402ab3ba
002AB38C  4C 8B F0                        mov r14, rax
002AB38F  48 8B 00                        mov rax, qword ptr [rax]
002AB392  48 85 C0                        test rax, rax
002AB395  75 F5                           jne 0x1402ab38c
002AB397  EB 21                           jmp 0x1402ab3ba
002AB399  48 8B 1B                        mov rbx, qword ptr [rbx]
002AB39C  EB CA                           jmp 0x1402ab368
002AB39E  4C 8B 73 10                     mov r14, qword ptr [rbx + 0x10]
002AB3A2  49 83 E6 FC                     and r14, 0xfffffffffffffffc
002AB3A6  74 12                           je 0x1402ab3ba
002AB3A8  49 39 0E                        cmp qword ptr [r14], rcx
002AB3AB  74 0D                           je 0x1402ab3ba
002AB3AD  49 8B CE                        mov rcx, r14
002AB3B0  4D 8B 76 10                     mov r14, qword ptr [r14 + 0x10]
002AB3B4  49 83 E6 FC                     and r14, 0xfffffffffffffffc
002AB3B8  75 EE                           jne 0x1402ab3a8
002AB3BA  0F B6 0D 77 28 B8 00            movzx ecx, byte ptr [rip + 0xb82877]
002AB3C1  41 BF 01 00 00 00               mov r15d, 1
002AB3C7  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
002AB3CB  80 C1 F4                        add cl, 0xf4
002AB3CE  49 D3 E7                        shl r15, cl
002AB3D1  49 8D 0C 2C                     lea rcx, [r12 + rbp]
002AB3D5  49 FF CF                        dec r15
002AB3D8  4C 23 FD                        and r15, rbp
002AB3DB  4C 2B F8                        sub r15, rax
002AB3DE  48 05 00 02 00 00               add rax, 0x200
002AB3E4  48 3B C8                        cmp rcx, rax
002AB3E7  0F 87 07 02 00 00               ja 0x1402ab5f4
002AB3ED  4D 03 E7                        add r12, r15
002AB3F0  48 8D 8B AC 00 00 00            lea rcx, [rbx + 0xac]
002AB3F7  E8 84 DA F9 FF                  call 0x140248e80
002AB3FC  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
002AB401  4D 8D 4F 58                     lea r9, [r15 + 0x58]
002AB405  4E 8D 0C 4B                     lea r9, [rbx + r9*2]
002AB409  4D 3B FC                        cmp r15, r12
002AB40C  72 2F                           jb 0x1402ab43d
002AB40E  48 8D 8B AC 00 00 00            lea rcx, [rbx + 0xac]
002AB415  E8 C6 E3 F9 FF                  call 0x1402497e0
002AB41A  4C 8B 64 24 30                  mov r12, qword ptr [rsp + 0x30]
002AB41F  44 8B BC 24 B8 00 00 00         mov r15d, dword ptr [rsp + 0xb8]
002AB427  4D 85 E4                        test r12, r12
002AB42A  0F 85 EB 01 00 00               jne 0x1402ab61b
002AB430  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
002AB435  49 8B DE                        mov rbx, r14
002AB438  E9 D3 FE FF FF                  jmp 0x1402ab310
002AB43D  41 0F B7 01                     movzx eax, word ptr [r9]
002AB441  66 85 C0                        test ax, ax
002AB444  0F 84 D7 02 00 00               je 0x1402ab721
002AB44A  66 83 E8 01                     sub ax, 1
002AB44E  66 41 89 01                     mov word ptr [r9], ax
002AB452  75 23                           jne 0x1402ab477
002AB454  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
002AB457  85 C0                           test eax, eax
002AB459  74 4E                           je 0x1402ab4a9
002AB45B  33 C9                           xor ecx, ecx
002AB45D  3D 00 02 00 00                  cmp eax, 0x200
002AB462  77 2A                           ja 0x1402ab48e
002AB464  8D 51 01                        lea edx, [rcx + 1]
002AB467  85 C9                           test ecx, ecx
002AB469  75 23                           jne 0x1402ab48e
002AB46B  83 E8 01                        sub eax, 1
002AB46E  89 43 20                        mov dword ptr [rbx + 0x20], eax
002AB471  0F 84 27 01 00 00               je 0x1402ab59e
002AB477  48 FF C5                        inc rbp
002AB47A  49 83 C1 02                     add r9, 2
002AB47E  49 FF C7                        inc r15
002AB481  49 FF CB                        dec r11
002AB484  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
002AB489  E9 7B FF FF FF                  jmp 0x1402ab409
002AB48E  4C 8B C8                        mov r9, rax
002AB491  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
002AB496  4C 8B C3                        mov r8, rbx
002AB499  BA 4B 19 06 00                  mov edx, 0x6194b
002AB49E  B9 1A 00 00 00                  mov ecx, 0x1a
002AB4A3  E8 B8 21 25 00                  call 0x1404fd660
002AB4A8  CC                              int3
002AB4A9  BA 01 00 00 00                  mov edx, 1
002AB4AE  8B CA                           mov ecx, edx
002AB4B0  EB B5                           jmp 0x1402ab467
002AB4B2  83 7C 24 5C 03                  cmp dword ptr [rsp + 0x5c], 3
002AB4B7  0F 84 80 FE FF FF               je 0x1402ab33d
002AB4BD  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002AB4C2  BF 01 00 00 00                  mov edi, 1
002AB4C7  48 2B C5                        sub rax, rbp
002AB4CA  48 FF C0                        inc rax
002AB4CD  49 3B C4                        cmp rax, r12
002AB4D0  49 0F 47 C4                     cmova rax, r12
002AB4D4  48 03 E8                        add rbp, rax
002AB4D7  4C 2B E0                        sub r12, rax
002AB4DA  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
002AB4DF  E9 2C FE FF FF                  jmp 0x1402ab310
002AB4E4  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002AB4ED  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
002AB4F4  48 8B 89 48 01 00 00            mov rcx, qword ptr [rcx + 0x148]
002AB4FB  48 81 C1 80 02 00 00            add rcx, 0x280
002AB502  E8 89 F0 F9 FF                  call 0x14024a590
002AB507  83 BC 24 C8 00 00 00 00         cmp dword ptr [rsp + 0xc8], 0
002AB50F  0F 85 BB FD 42 00               jne 0x1406db2d0
002AB515  41 80 FF 11                     cmp r15b, 0x11
002AB519  74 1E                           je 0x1402ab539
002AB51B  83 3D FE B7 D1 00 00            cmp dword ptr [rip + 0xd1b7fe], 0
002AB522  74 0D                           je 0x1402ab531
002AB524  41 0F B6 D7                     movzx edx, r15b
002AB528  44 0F 20 C1                     mov rcx, cr8
002AB52C  E8 67 A1 24 00                  call 0x1404f5698
002AB531  41 0F B6 C7                     movzx eax, r15b
002AB535  44 0F 22 C0                     mov cr8, rax
002AB539  48 83 C4 68                     add rsp, 0x68
002AB53D  41 5F                           pop r15
002AB53F  41 5E                           pop r14
002AB541  41 5D                           pop r13
002AB543  41 5C                           pop r12
002AB545  5F                              pop rdi
002AB546  5E                              pop rsi
002AB547  5D                              pop rbp
002AB548  5B                              pop rbx
002AB549  C3                              ret
002AB54A  CC                              int3
002AB54B  3B D7                           cmp edx, edi
002AB54D  0F 85 AC FD FF FF               jne 0x1402ab2ff
002AB553  48 8D 46 FF                     lea rax, [rsi - 1]
002AB557  49 03 C0                        add rax, r8
002AB55A  48 3B 44 24 50                  cmp rax, qword ptr [rsp + 0x50]
002AB55F  0F 87 9A FD FF FF               ja 0x1402ab2ff
002AB565  41 80 FF 02                     cmp r15b, 2
002AB569  73 CE                           jae 0x1402ab539
002AB56B  39 1D AF B7 D1 00               cmp dword ptr [rip + 0xd1b7af], ebx
002AB571  EB AF                           jmp 0x1402ab522
002AB573  41 0F B6 D1                     movzx edx, r9b
002AB577  41 0F B6 CE                     movzx ecx, r14b
002AB57B  E8 7C A1 24 00                  call 0x1404f56fc
002AB580  8B 94 24 B0 00 00 00            mov edx, dword ptr [rsp + 0xb0]
002AB587  41 B9 02 00 00 00               mov r9d, 2
002AB58D  4C 8B 84 24 C0 00 00 00         mov r8, qword ptr [rsp + 0xc0]
002AB595  45 8D 51 FF                     lea r10d, [r9 - 1]
002AB599  E9 9D FC FF FF                  jmp 0x1402ab23b
002AB59E  80 7B 28 00                     cmp byte ptr [rbx + 0x28], 0
002AB5A2  74 0E                           je 0x1402ab5b2
002AB5A4  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
002AB5A9  8B 05 91 3C D2 00               mov eax, dword ptr [rip + 0xd23c91]
002AB5AF  89 43 24                        mov dword ptr [rbx + 0x24], eax
002AB5B2  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
002AB5B7  4C 8B D2                        mov r10, rdx
002AB5BA  F0 4C 0F C1 50 08               lock xadd qword ptr [rax + 8], r10
002AB5C0  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
002AB5C4  49 FF C2                        inc r10
002AB5C7  E8 D4 01 00 00                  call 0x1402ab7a0
002AB5CC  85 C0                           test eax, eax
002AB5CE  0F 85 35 01 00 00               jne 0x1402ab709
002AB5D4  8B 84 24 C8 00 00 00            mov eax, dword ptr [rsp + 0xc8]
002AB5DB  B9 01 00 00 00                  mov ecx, 1
002AB5E0  4C 3B 54 24 40                  cmp r10, qword ptr [rsp + 0x40]
002AB5E5  0F 43 C1                        cmovae eax, ecx
002AB5E8  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
002AB5EF  E9 83 FE FF FF                  jmp 0x1402ab477
002AB5F4  41 BC 00 02 00 00               mov r12d, 0x200
002AB5FA  E9 F1 FD FF FF                  jmp 0x1402ab3f0
002AB5FF  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
002AB603  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
002AB608  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
002AB60C  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
002AB611  44 89 4C 24 5C                  mov dword ptr [rsp + 0x5c], r9d
002AB616  E9 D9 FC FF FF                  jmp 0x1402ab2f4
002AB61B  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002AB624  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
002AB62B  48 8B 81 48 01 00 00            mov rax, qword ptr [rcx + 0x148]
002AB632  8B 88 80 02 00 00               mov ecx, dword ptr [rax + 0x280]
002AB638  0F BA E1 1E                     bt ecx, 0x1e
002AB63C  0F 83 9B 00 00 00               jae 0x1402ab6dd
002AB642  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002AB64B  41 0F B6 D7                     movzx edx, r15b
002AB64F  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
002AB656  48 8B 89 48 01 00 00            mov rcx, qword ptr [rcx + 0x148]
002AB65D  48 81 C1 80 02 00 00            add rcx, 0x280
002AB664  E8 87 D5 09 00                  call 0x140348bf0
002AB669  B8 01 00 00 00                  mov eax, 1
002AB66E  8B C8                           mov ecx, eax
002AB670  8B F8                           mov edi, eax
002AB672  E8 2D 12 00 00                  call 0x1402ac8a4
002AB677  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
002AB67C  E9 8F FC FF FF                  jmp 0x1402ab310
002AB681  48 8B D5                        mov rdx, rbp
002AB684  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
002AB689  E8 9A 10 00 00                  call 0x1402ac728
002AB68E  E9 9C FC FF FF                  jmp 0x1402ab32f
002AB693  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
002AB697  48 FF C8                        dec rax
002AB69A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002AB69F  E9 43 FC FF FF                  jmp 0x1402ab2e7
002AB6A4  48 8B C6                        mov rax, rsi
002AB6A7  48 25 00 00 FC FF               and rax, 0xfffffffffffc0000
002AB6AD  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
002AB6B2  48 8D 86 FF FF 03 00            lea rax, [rsi + 0x3ffff]
002AB6B9  48 25 00 00 FC FF               and rax, 0xfffffffffffc0000
002AB6BF  48 3B F0                        cmp rsi, rax
002AB6C2  75 07                           jne 0x1402ab6cb
002AB6C4  48 8D 86 00 00 04 00            lea rax, [rsi + 0x40000]
002AB6CB  48 FF C8                        dec rax
002AB6CE  44 89 54 24 5C                  mov dword ptr [rsp + 0x5c], r10d
002AB6D3  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002AB6D8  E9 17 FC FF FF                  jmp 0x1402ab2f4
002AB6DD  41 80 FF 11                     cmp r15b, 0x11
002AB6E1  0F 84 49 FD FF FF               je 0x1402ab430
002AB6E7  E8 F4 BC FC FF                  call 0x1402773e0
002AB6EC  85 C0                           test eax, eax
002AB6EE  0F 84 3C FD FF FF               je 0x1402ab430
002AB6F4  E9 49 FF FF FF                  jmp 0x1402ab642
002AB6F9  48 8B 00                        mov rax, qword ptr [rax]
002AB6FC  E9 83 FB FF FF                  jmp 0x1402ab284
002AB701  48 8B 00                        mov rax, qword ptr [rax]
002AB704  E9 CB FB FF FF                  jmp 0x1402ab2d4
002AB709  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
002AB70E  F0 48 FF 40 10                  lock inc qword ptr [rax + 0x10]
002AB713  48 C7 44 24 40 01 00 00 00      mov qword ptr [rsp + 0x40], 1
002AB71C  E9 B3 FE FF FF                  jmp 0x1402ab5d4
002AB721  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
002AB729  4C 8B C6                        mov r8, rsi
002AB72C  BA 4A 19 06 00                  mov edx, 0x6194a
002AB731  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
002AB736  B9 1A 00 00 00                  mov ecx, 0x1a
002AB73B  E8 20 1F 25 00                  call 0x1404fd660
002AB740  CC                              int3
002AB741  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
002AB749  4C 8B C6                        mov r8, rsi
002AB74C  BA 48 19 06 00                  mov edx, 0x61948
002AB751  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
002AB756  B9 1A 00 00 00                  mov ecx, 0x1a
002AB75B  E8 00 1F 25 00                  call 0x1404fd660
002AB760  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDereferenceIoPages(int a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m4C;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_p0;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p5C;
    unsigned int v_stack_p8;
    unsigned int v_stack_pB0;
    unsigned __int64 v_stack_pC0;
    unsigned int v_stack_pC8;

    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    v_stack_m78 = a3;
    v_rbx = 0;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 12069463)) + (244));
    v_stack_p20 = 0;
    v_stack_m68 = 0x400ULL;
    result = (1) << ((unsigned __int8)(a1));
    result = (result) - 1;
    v_r13 = ((int)(a1)) << (6);
    v_rsi = (a2) & (result);
    v_r13 = (v_r13) + (v_rip + 12107885);
    v_stack_m70 = v_r13;
    if ((*(unsigned int *)(v_rip + 13744875)) != 0) goto loc_002AB573;
loc_002AB23B:
    v_r15 = (unsigned __int8)(v_cr8);
    if (((unsigned __int8)(v_cr8)) == 2) { v_r15 = 17; }
    v_stack_p10 = (unsigned int)(v_r15);
    result = MiIsPageInHugePfn(v_rsi, (int)(a1), a3, 2);
    if ((unsigned int)(result) != 0) goto loc_002AB6A4;
    if (*(unsigned __int64 *)(v_rip + 12107925) == 0) goto loc_002AB292;
loc_002AB270:
    if (v_rsi < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12107925) + 24))) goto loc_002AB6F9;
    if (v_rsi <= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12107925) + 32))) goto loc_002AB289;
loc_002AB284:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12107925) + 8) != 0) goto loc_002AB270;
loc_002AB289:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12107925) + 8) != 0) goto loc_002AB5FF;
loc_002AB292:
    a1 = (v_rsi + 262143) & (0xFFFFFFFFFFFC0000ULL);
    if (v_rsi == a1) {
        a1 = v_rsi + 262144;
    }
    a1 = (a1) - 1;
    if (*(unsigned __int64 *)(v_rip + 12107853) == 0) goto loc_002AB2E2;
loc_002AB2C0:
    if (a1 < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12107853) + 24))) goto loc_002AB701;
    if (v_rsi <= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12107853) + 32))) goto loc_002AB2D9;
loc_002AB2D4:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12107853) + 8) != 0) goto loc_002AB2C0;
loc_002AB2D9:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12107853) + 8) != 0) goto loc_002AB693;
loc_002AB2E2:
    v_stack_m58 = a1;
loc_002AB2E7:
    v_stack_m60 = v_rsi;
    v_stack_m4C = 3;
loc_002AB2F4:
    if (v_stack_m4C != 3) goto loc_002AB54B;
loc_002AB2FF:
    result = MiLockIoPfnTree(5, (int)(a1), a3, 2);
loc_002AB310:
    if (a3 == 0) goto loc_002AB4E4;
    if (v_rsi < v_stack_m60) goto loc_002AB681;
    if (v_rsi > v_stack_m58) goto loc_002AB681;
loc_002AB32F:
    if (v_stack_p8 == 1) goto loc_002AB4B2;
loc_002AB33D:
    if (1 == 0) goto loc_002AB36F;
    if (*(unsigned __int64 *)(v_r13) == 0) goto loc_002AB36D;
loc_002AB350:
    if (v_rsi < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 24))) goto loc_002AB399;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 24)) + (512);
    if (v_rsi < result) goto loc_002AB36D;
loc_002AB368:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8) != 0) goto loc_002AB350;
loc_002AB36D:
    v_rdi = 0;
loc_002AB36F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8) == 0) goto loc_002AB741;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8) + 8) == 0) goto loc_002AB39E;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8) + 8)) == 0) goto loc_002AB3BA;
loc_002AB38C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8) + 8))) != 0) goto loc_002AB38C;
    goto loc_002AB3BA;
loc_002AB399:
    goto loc_002AB368;
loc_002AB39E:
    v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8)) + 16)) & (-4);
    if (condition_is_equal) goto loc_002AB3BA;
loc_002AB3A8:
    if ((*(unsigned __int64 *)(v_r14)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8))) goto loc_002AB3BA;
    v_r14 = (*(unsigned __int64 *)(v_r14 + 16)) & (-4);
    if (condition_is_not_equal) goto loc_002AB3A8;
loc_002AB3BA:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 12068983)) + (244));
    v_r15 = (1) << ((unsigned __int8)(a1));
    v_r15 = (v_r15) - 1;
    v_r15 = (v_r15) & (v_rsi);
    v_r15 = (v_r15) - (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8)) + 24));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8)) + 24)) + (512);
    if ((a3 + v_rsi * 1) > result) goto loc_002AB5F4;
    v_r12 = (a3) + (v_r15);
loc_002AB3F0:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8)) + 172, (int)(a1), a3, 2);
loc_002AB409:
    if (v_r15 < v_r12) goto loc_002AB43D;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8)) + 172, (int)(a1), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8)) + v_r15 + 88 * 2);
    if (v_stack_m78 != 0) goto loc_002AB61B;
loc_002AB430:
    goto loc_002AB310;
loc_002AB43D:
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8)) + v_r15 + 88 * 2)) == 0) goto loc_002AB721;
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8)) + v_r15 + 88 * 2)) - (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8)) + v_r15 + 88 * 2) = (unsigned __int16)(result);
    if (condition_is_not_equal) goto loc_002AB477;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32))) == 0) goto loc_002AB4A9;
    a1 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)))) > 512) goto loc_002AB48E;
loc_002AB467:
    if (0 != 0) goto loc_002AB48E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 32))) - (1));
    *(unsigned int *)(v_r14 + 32) = (unsigned int)(result);
    if (condition_is_equal) goto loc_002AB59E;
loc_002AB477:
    v_rbp = (v_rsi) + 1;
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 8)) + v_r15 + 88 * 2) + (2);
    v_r15 = ((unsigned int)(v_stack_p10)) + 1;
    v_r11 = (v_stack_m78) - 1;
    v_stack_m78 = v_r11;
    goto loc_002AB409;
loc_002AB48E:
    v_stack_m88 = v_rbp;
    result = KeBugCheckEx(26, (unsigned int)(0x6194BULL), v_r14, result);
loc_002AB4A9:
    goto loc_002AB467;
loc_002AB4B2:
    if (v_stack_m4C == 3) goto loc_002AB33D;
    result = (v_stack_m58) - (v_rbp);
    result = (result) + 1;
    if (result > v_stack_m78) { result = v_stack_m78; }
    v_rbp = (v_rbp) + (result);
    v_r12 = (v_stack_m78) - (result);
    v_stack_m78 = v_r12;
    goto loc_002AB310;
loc_002AB4E4:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 328)) + (640);
    result = ExReleaseSpinLockSharedFromDpcLevel(a1, 1, v_r14, result);
    if (((unsigned __int8)(v_r15)) == 17) goto loc_002AB539;
loc_002AB522:
    if ((*(unsigned int *)(v_rip + 13744126)) != 0) {
        a2 = (unsigned __int8)(v_r15);
        a1 = 2;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_r14, result);
    }
loc_002AB539:
    v_rsp = (v_rsp) + (104);
    return (unsigned __int8)(v_r15);
loc_002AB54B:
    if (((unsigned int)(a2)) != 1) goto loc_002AB2FF;
    result = (v_rsi - 1) + (v_r14);
    if (result > v_stack_p50) goto loc_002AB2FF;
    if (((unsigned __int8)(v_r15)) >= 2) goto loc_002AB539;
    goto loc_002AB522;
loc_002AB573:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_r14), (unsigned __int8)(result), v_r14, result);
    goto loc_002AB23B;
loc_002AB59E:
    if ((*(unsigned __int8 *)(v_r14 + 40)) != 0) {
        result = *(unsigned int *)(v_rip + 13778065);
        *(unsigned int *)(v_r14 + 36) = (unsigned int)(result);
    }
    v_r10 = ((unsigned int)(v_stack_pB0)) + 1;
    result = MiIsPageInIoHugeRangeTransition(*(unsigned __int64 *)(v_r14 + 24), (unsigned int)(v_stack_pB0), v_stack_pC0, 2);
    if ((unsigned int)(result) != 0) goto loc_002AB709;
loc_002AB5D4:
    result = (unsigned int)(v_stack_pC8);
    if (v_r10 >= v_stack_p40) { result = 1; }
    v_stack_pC8 = (unsigned int)(result);
    goto loc_002AB477;
loc_002AB5F4:
    goto loc_002AB3F0;
loc_002AB5FF:
    v_stack_p48 = *(unsigned __int64 *)(result + 24);
    v_stack_p50 = *(unsigned __int64 *)(result + 32);
    v_stack_p5C = 2;
    goto loc_002AB2F4;
loc_002AB61B:
    if (v_r10 >= v_stack_p40) goto loc_002AB6DD;
loc_002AB642:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34872) + 328)) + (640);
    result = MiReleaseSpinLockShared(a1, (unsigned __int8)(v_r15), v_stack_pC0, 2);
    result = MiLockIoPfnTree(1, (unsigned __int8)(v_r15), v_stack_pC0, 2);
    goto loc_002AB310;
loc_002AB681:
    result = MiIoSpaceGetBounds(v_stack_p48, v_rbp, v_stack_pC0, 2);
    goto loc_002AB32F;
loc_002AB693:
    result = (*(unsigned __int64 *)(result + 24)) - 1;
    v_stack_p50 = result;
    goto loc_002AB2E7;
loc_002AB6A4:
    result = (v_rsi) & (0xFFFFFFFFFFFC0000ULL);
    v_stack_p48 = result;
    result = (v_rsi + 262143) & (0xFFFFFFFFFFFC0000ULL);
    if (v_rsi == result) {
        result = v_rsi + 262144;
    }
    result = (result) - 1;
    v_stack_p5C = (unsigned int)(v_r10);
    v_stack_p50 = result;
    goto loc_002AB2F4;
loc_002AB6DD:
    if (((unsigned __int8)(v_r15)) == 17) goto loc_002AB430;
    result = KeShouldYieldProcessor(v_stack_p48, v_rbp, v_stack_pC0, 2);
    if ((unsigned int)(result) == 0) goto loc_002AB430;
    goto loc_002AB642;
loc_002AB6F9:
    goto loc_002AB284;
loc_002AB701:
    goto loc_002AB2D4;
loc_002AB709:
    v_stack_p40 = 1;
    goto loc_002AB5D4;
loc_002AB721:
    v_stack_p20 = v_rbp;
    result = KeBugCheckEx(26, (unsigned int)(0x6194AULL), v_rsi, v_stack_pC0);
loc_002AB741:
    v_stack_p20 = v_rbp;
    result = KeBugCheckEx(26, (unsigned int)(0x61948ULL), v_rsi, v_stack_pC0);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDereferenceIoPages(int32_t Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m4C;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint32_t v_stack_p0;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint32_t v_stack_p5C;
    uint32_t v_stack_p8;
    uint32_t v_stack_pB0;
    uint64_t v_stack_pC0;
    uint32_t v_stack_pC8;

    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    v_stack_m78 = Arg3;
    local_rbx = 0;
    Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0xB82A57)) + (244));
    v_stack_p20 = 0;
    v_stack_m68 = 0x400ULL;
    result = (1) << ((uint8_t)(Arg1));
    result = (result) - 1;
    local_r13 = ((int32_t)(Arg1)) << (6);
    local_rsi = (Arg2) & (result);
    local_r13 = (local_r13) + (v_rip + 12107885);
    v_stack_m70 = local_r13;
    if ((*(uint32_t *)(v_rip + 0xD1BAEB)) != 0) goto loc_002AB573;
loc_002AB23B:
    local_r15 = (uint8_t)(v_cr8);
    if (((uint8_t)(v_cr8)) == 2) { local_r15 = 17; }
    v_stack_p10 = (uint32_t)(local_r15);
    result = MiIsPageInHugePfn(local_rsi, (int32_t)(Arg1), Arg3, 2);
    if ((uint32_t)(result) != 0) goto loc_002AB6A4;
    if (*(uint64_t *)(v_rip + 0xB8C095) == 0) goto loc_002AB292;
loc_002AB270:
    if (local_rsi < (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB8C095) + 0x18))) goto loc_002AB6F9;
    if (local_rsi <= (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB8C095) + 0x20))) goto loc_002AB289;
loc_002AB284:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB8C095) + 0x8) != 0) goto loc_002AB270;
loc_002AB289:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB8C095) + 0x8) != 0) goto loc_002AB5FF;
loc_002AB292:
    Arg1 = (local_rsi + 262143) & (0xFFFFFFFFFFFC0000ULL);
    if (local_rsi == Arg1) {
        Arg1 = local_rsi + 262144;
    }
    Arg1 = (Arg1) - 1;
    if (*(uint64_t *)(v_rip + 0xB8C04D) == 0) goto loc_002AB2E2;
loc_002AB2C0:
    if (Arg1 < (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB8C04D) + 0x18))) goto loc_002AB701;
    if (local_rsi <= (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB8C04D) + 0x20))) goto loc_002AB2D9;
loc_002AB2D4:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB8C04D) + 0x8) != 0) goto loc_002AB2C0;
loc_002AB2D9:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB8C04D) + 0x8) != 0) goto loc_002AB693;
loc_002AB2E2:
    v_stack_m58 = Arg1;
loc_002AB2E7:
    v_stack_m60 = local_rsi;
    v_stack_m4C = 3;
loc_002AB2F4:
    if (v_stack_m4C != 3) goto loc_002AB54B;
loc_002AB2FF:
    result = MiLockIoPfnTree(5, (int32_t)(Arg1), Arg3, 2);
loc_002AB310:
    if (Arg3 == 0) goto loc_002AB4E4;
    if (local_rsi < v_stack_m60) goto loc_002AB681;
    if (local_rsi > v_stack_m58) goto loc_002AB681;
loc_002AB32F:
    if (v_stack_p8 == 1) goto loc_002AB4B2;
loc_002AB33D:
    if (1 == 0) goto loc_002AB36F;
    if (*(uint64_t *)(local_r13) == 0) goto loc_002AB36D;
loc_002AB350:
    if (local_rsi < (*(uint64_t *)(*(uint64_t *)(local_r13) + 0x18))) goto loc_002AB399;
    result = (*(uint64_t *)(*(uint64_t *)(local_r13) + 0x18)) + (512);
    if (local_rsi < result) goto loc_002AB36D;
loc_002AB368:
    if (*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8) != 0) goto loc_002AB350;
loc_002AB36D:
    local_rdi = 0;
loc_002AB36F:
    if (*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8) == 0) goto loc_002AB741;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8) + 0x8) == 0) goto loc_002AB39E;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8) + 0x8)) == 0) goto loc_002AB3BA;
loc_002AB38C:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8) + 0x8))) != 0) goto loc_002AB38C;
    goto loc_002AB3BA;
loc_002AB399:
    goto loc_002AB368;
loc_002AB39E:
    local_r14 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8)) + 0x10)) & (-4);
    if (condition_is_equal) goto loc_002AB3BA;
loc_002AB3A8:
    if ((*(uint64_t *)(local_r14)) == (*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8))) goto loc_002AB3BA;
    local_r14 = (*(uint64_t *)(local_r14 + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_002AB3A8;
loc_002AB3BA:
    Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0xB82877)) + (244));
    local_r15 = (1) << ((uint8_t)(Arg1));
    local_r15 = (local_r15) - 1;
    local_r15 = (local_r15) & (local_rsi);
    local_r15 = (local_r15) - (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8)) + 0x18));
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8)) + 0x18)) + (512);
    if ((Arg3 + local_rsi * 1) > result) goto loc_002AB5F4;
    local_r12 = (Arg3) + (local_r15);
loc_002AB3F0:
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8)) + 172, (int32_t)(Arg1), Arg3, 2);
loc_002AB409:
    if (local_r15 < local_r12) goto loc_002AB43D;
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8)) + 172, (int32_t)(Arg1), Arg3, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8)) + local_r15 + 88 * 2);
    if (v_stack_m78 != 0) goto loc_002AB61B;
loc_002AB430:
    goto loc_002AB310;
loc_002AB43D:
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8)) + local_r15 + 0x58 * 2)) == 0) goto loc_002AB721;
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8)) + local_r15 + 0x58 * 2)) - (1));
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8)) + local_r15 + 0x58 * 2) = (uint16_t)(result);
    if (condition_is_not_equal) goto loc_002AB477;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) == 0) goto loc_002AB4A9;
    Arg1 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)))) > 512) goto loc_002AB48E;
loc_002AB467:
    if (0 != 0) goto loc_002AB48E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) - (1));
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)(result);
    if (condition_is_equal) goto loc_002AB59E;
loc_002AB477:
    local_rbp = (local_rsi) + 1;
    a4 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r13) + 0x8)) + local_r15 + 88 * 2) + (2);
    local_r15 = ((uint32_t)(v_stack_p10)) + 1;
    local_r11 = (v_stack_m78) - 1;
    v_stack_m78 = local_r11;
    goto loc_002AB409;
loc_002AB48E:
    v_stack_m88 = local_rbp;
    result = KeBugCheckEx(26, (uint32_t)(0x6194BULL), local_r14, result);
loc_002AB4A9:
    goto loc_002AB467;
loc_002AB4B2:
    if (v_stack_m4C == 3) goto loc_002AB33D;
    result = (v_stack_m58) - (local_rbp);
    result = (result) + 1;
    if (result > v_stack_m78) { result = v_stack_m78; }
    local_rbp = (local_rbp) + (result);
    local_r12 = (v_stack_m78) - (result);
    v_stack_m78 = local_r12;
    goto loc_002AB310;
loc_002AB4E4:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x148)) + (640);
    result = ExReleaseSpinLockSharedFromDpcLevel(Arg1, 1, local_r14, result);
    if (((uint8_t)(local_r15)) == 17) goto loc_002AB539;
loc_002AB522:
    if ((*(uint32_t *)(v_rip + 0xD1B7FE)) != 0) {
        Arg2 = (uint8_t)(local_r15);
        Arg1 = 2;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, local_r14, result);
    }
loc_002AB539:
    local_rsp = (local_rsp) + (104);
    return (uint8_t)(local_r15);
loc_002AB54B:
    if (((uint32_t)(Arg2)) != 1) goto loc_002AB2FF;
    result = (local_rsi - 1) + (local_r14);
    if (result > v_stack_p50) goto loc_002AB2FF;
    if (((uint8_t)(local_r15)) >= 2) goto loc_002AB539;
    goto loc_002AB522;
loc_002AB573:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_r14), (uint8_t)(result), local_r14, result);
    goto loc_002AB23B;
loc_002AB59E:
    if ((*(uint8_t *)(local_r14 + 0x28)) != 0) {
        result = *(uint32_t *)(v_rip + 0xD23C91);
        *(uint32_t *)(local_r14 + 0x24) = (uint32_t)(result);
    }
    local_r10 = ((uint32_t)(v_stack_pB0)) + 1;
    result = MiIsPageInIoHugeRangeTransition(*(uint64_t *)(local_r14 + 0x18), (uint32_t)(v_stack_pB0), v_stack_pC0, 2);
    if ((uint32_t)(result) != 0) goto loc_002AB709;
loc_002AB5D4:
    result = (uint32_t)(v_stack_pC8);
    if (local_r10 >= v_stack_p40) { result = 1; }
    v_stack_pC8 = (uint32_t)(result);
    goto loc_002AB477;
loc_002AB5F4:
    goto loc_002AB3F0;
loc_002AB5FF:
    v_stack_p48 = *(uint64_t *)(result + 0x18);
    v_stack_p50 = *(uint64_t *)(result + 0x20);
    v_stack_p5C = 2;
    goto loc_002AB2F4;
loc_002AB61B:
    if (local_r10 >= v_stack_p40) goto loc_002AB6DD;
loc_002AB642:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8838) + 0x148)) + (640);
    result = MiReleaseSpinLockShared(Arg1, (uint8_t)(local_r15), v_stack_pC0, 2);
    result = MiLockIoPfnTree(1, (uint8_t)(local_r15), v_stack_pC0, 2);
    goto loc_002AB310;
loc_002AB681:
    result = MiIoSpaceGetBounds(v_stack_p48, local_rbp, v_stack_pC0, 2);
    goto loc_002AB32F;
loc_002AB693:
    result = (*(uint64_t *)(result + 0x18)) - 1;
    v_stack_p50 = result;
    goto loc_002AB2E7;
loc_002AB6A4:
    result = (local_rsi) & (0xFFFFFFFFFFFC0000ULL);
    v_stack_p48 = result;
    result = (local_rsi + 262143) & (0xFFFFFFFFFFFC0000ULL);
    if (local_rsi == result) {
        result = local_rsi + 262144;
    }
    result = (result) - 1;
    v_stack_p5C = (uint32_t)(local_r10);
    v_stack_p50 = result;
    goto loc_002AB2F4;
loc_002AB6DD:
    if (((uint8_t)(local_r15)) == 17) goto loc_002AB430;
    result = KeShouldYieldProcessor(v_stack_p48, local_rbp, v_stack_pC0, 2);
    if ((uint32_t)(result) == 0) goto loc_002AB430;
    goto loc_002AB642;
loc_002AB6F9:
    goto loc_002AB284;
loc_002AB701:
    goto loc_002AB2D4;
loc_002AB709:
    v_stack_p40 = 1;
    goto loc_002AB5D4;
loc_002AB721:
    v_stack_p20 = local_rbp;
    result = KeBugCheckEx(26, (uint32_t)(0x6194AULL), local_rsi, v_stack_pC0);
loc_002AB741:
    v_stack_p20 = local_rbp;
    result = KeBugCheckEx(26, (uint32_t)(0x61948ULL), local_rsi, v_stack_pC0);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x3FFFF` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002AB1B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
