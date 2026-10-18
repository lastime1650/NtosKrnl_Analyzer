# sub_002E0B15

- RVA: `0x002E0B15`–`0x002E10CE` (길이 `1,465` bytes)
- VA: `0x00000001402E0B15`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070C90`
- 디코드: `349`개 명령, `1,465/1,465` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x002E0BB4` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x002E0C33` → [MiViewMayContainPage](MiViewMayContainPage_function_002E11F0.md) (function, `0x002E11F0`)
- `0x002E0CC0` → [ExpWaitForSpinLockExclusiveAndAcquire](../32/ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) (function, `0x003239A0`)
- `0x002E0D77` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002E0DF1` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002E0ED7` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002E0EF0` → [MiInsertUnusedSubsection](../29/MiInsertUnusedSubsection_function_00298D50.md) (function, `0x00298D50`)
- `0x002E0F13` → [ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented](../32/ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_00323A70.md) (function, `0x00323A70`)
- `0x002E0F39` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002E0F4A` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002E0F5C` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x002E0F71` → [MiGetSharedProtos](../34/MiGetSharedProtos_function_00348D58.md) (function, `0x00348D58`)
- `0x002E0FAE` → [MiGetSharedProtos](../34/MiGetSharedProtos_function_00348D58.md) (function, `0x00348D58`)
- `0x002E0FF5` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002E1004` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002E1015` → [MiReleaseSpinLockShared](../34/MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x002E101D` → [MiUnlockControlAreaFileObjectShared](../2D/MiUnlockControlAreaFileObjectShared_function_002DFCB4.md) (function, `0x002DFCB4`)
- `0x002E104B` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x002E106E` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x002E1089` → [MiAnyProtosAreMapped](../46/MiAnyProtosAreMapped_function_00465464.md) (function, `0x00465464`)
- `0x002E10B4` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002E0C92` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002E0C9F` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x002E0CE8` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002E0E35` → RVA `0x00E30088` (`.data`; read)
- `0x002E0EFF` → RVA `0x00F0DE58` (`.data`; read)
- `0x002E0FE7` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **21**
  - `0x002E0B51` → [sub_002E087E + 0x4D](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E0B8B` → [sub_002E087E + 0x99](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E0BA3` → [sub_002E087E + 0x13E](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E0BB9` → [sub_002E087E + 0x13A](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E0BC3` → [sub_002E087E + 0x1A2](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E0BE0` → [sub_002E10F7 + 0x5A](Unknown_function_002E10F7.md) (`tail-transfer`)
  - `0x002E0D87` → [sub_002E10F7 + 0xBE](Unknown_function_002E10F7.md) (`tail-transfer`)
  - `0x002E0E52` → [sub_002E10F7](Unknown_function_002E10F7.md) (`tail-transfer`)
  - `0x002E0E7D` → [sub_002E10F7 + 0xC](Unknown_function_002E10F7.md) (`tail-transfer`)
  - `0x002E0F27` → [sub_002E087E + 0x1FB](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E0F2D` → [sub_002E087E + 0x1A2](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E0F42` → [sub_002E087E + 0x113](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E0F61` → [sub_002E087E + 0x196](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E0F9E` → [sub_002E087E + 0x4D](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E0FD6` → [sub_002E087E + 0x99](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E1024` → [sub_002E087E + 0x275](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E102D` → [sub_002E087E + 0x273](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E10A3` → [sub_002E087E + 0x16C](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E10B9` → [sub_002E087E + 0x178](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E10C1` → [sub_002E087E + 0x2F](Unknown_function_002E087E.md) (`tail-transfer`)
  - `0x002E10C9` → [sub_002E087E + 0x7F](Unknown_function_002E087E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002E0B15  48 3B FA                        cmp rdi, rdx
002E0B18  0F 82 48 04 00 00               jb 0x1402e0f66
002E0B1E  41 8B 44 24 2C                  mov eax, dword ptr [r12 + 0x2c]
002E0B23  48 8D 0C C2                     lea rcx, [rdx + rax*8]
002E0B27  48 3B F9                        cmp rdi, rcx
002E0B2A  0F 83 36 04 00 00               jae 0x1402e0f66
002E0B30  41 8B 44 24 24                  mov eax, dword ptr [r12 + 0x24]
002E0B35  48 8B EF                        mov rbp, rdi
002E0B38  48 C1 E5 09                     shl rbp, 9
002E0B3C  48 C1 E2 09                     shl rdx, 9
002E0B40  48 2B EA                        sub rbp, rdx
002E0B43  48 C1 E0 09                     shl rax, 9
002E0B47  48 81 E5 00 F0 FF FF            and rbp, 0xfffffffffffff000
002E0B4E  48 03 E8                        add rbp, rax
002E0B51  E9 75 FD FF FF                  jmp 0x1402e08cb
002E0B56  48 3B FA                        cmp rdi, rdx
002E0B59  0F 82 44 04 00 00               jb 0x1402e0fa3
002E0B5F  8B 46 2C                        mov eax, dword ptr [rsi + 0x2c]
002E0B62  48 8D 0C C2                     lea rcx, [rdx + rax*8]
002E0B66  48 3B F9                        cmp rdi, rcx
002E0B69  0F 83 34 04 00 00               jae 0x1402e0fa3
002E0B6F  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
002E0B72  48 C1 E7 09                     shl rdi, 9
002E0B76  48 C1 E2 09                     shl rdx, 9
002E0B7A  48 2B FA                        sub rdi, rdx
002E0B7D  48 C1 E0 09                     shl rax, 9
002E0B81  48 81 E7 00 F0 FF FF            and rdi, 0xfffffffffffff000
002E0B88  48 03 F8                        add rdi, rax
002E0B8B  E9 87 FD FF FF                  jmp 0x1402e0917
002E0B90  41 0F 0D 08                     prefetchw byte ptr [r8]
002E0B94  41 8B 00                        mov eax, dword ptr [r8]
002E0B97  0F BA F0 1F                     btr eax, 0x1f
002E0B9B  8D 48 01                        lea ecx, [rax + 1]
002E0B9E  F0 41 0F B1 08                  lock cmpxchg dword ptr [r8], ecx
002E0BA3  0F 84 13 FE FF FF               je 0x1402e09bc
002E0BA9  85 C0                           test eax, eax
002E0BAB  79 EE                           jns 0x1402e0b9b
002E0BAD  40 0F B6 D7                     movzx edx, dil
002E0BB1  49 8B C8                        mov rcx, r8
002E0BB4  E8 C7 17 08 00                  call 0x140362380
002E0BB9  E9 FA FD FF FF                  jmp 0x1402e09b8
002E0BBE  49 83 7D 40 00                  cmp qword ptr [r13 + 0x40], 0
002E0BC3  0F 84 57 FE FF FF               je 0x1402e0a20
002E0BC9  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
002E0BD1  C7 84 24 08 01 00 00 01 00 00 00  mov dword ptr [rsp + 0x108], 1
002E0BDC  4C 3B 60 18                     cmp r12, qword ptr [rax + 0x18]
002E0BE0  0F 85 6B 05 00 00               jne 0x1402e1151
002E0BE6  83 7C 24 58 00                  cmp dword ptr [rsp + 0x58], 0
002E0BEB  0F 85 92 04 00 00               jne 0x1402e1083
002E0BF1  F6 C3 20                        test bl, 0x20
002E0BF4  0F 85 89 04 00 00               jne 0x1402e1083
002E0BFA  49 8B 7C 24 58                  mov rdi, qword ptr [r12 + 0x58]
002E0BFF  4D 8D 7C 24 58                  lea r15, [r12 + 0x58]
002E0C04  49 3B FF                        cmp rdi, r15
002E0C07  74 5C                           je 0x1402e0c65
002E0C09  48 8B 94 24 F8 00 00 00         mov rdx, qword ptr [rsp + 0xf8]
002E0C11  48 8D 44 24 50                  lea rax, [rsp + 0x50]
002E0C16  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002E0C1B  4C 8B CF                        mov r9, rdi
002E0C1E  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
002E0C23  44 8B C3                        mov r8d, ebx
002E0C26  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002E0C2B  49 8B CD                        mov rcx, r13
002E0C2E  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
002E0C33  E8 B8 05 00 00                  call 0x1402e11f0
002E0C38  8B F0                           mov esi, eax
002E0C3A  85 C0                           test eax, eax
002E0C3C  78 15                           js 0x1402e0c53
002E0C3E  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002E0C43  48 85 C0                        test rax, rax
002E0C46  74 06                           je 0x1402e0c4e
002E0C48  4C 89 30                        mov qword ptr [rax], r14
002E0C4B  4C 8B F0                        mov r14, rax
002E0C4E  48 8B 3F                        mov rdi, qword ptr [rdi]
002E0C51  EB B1                           jmp 0x1402e0c04
002E0C53  4C 8B A4 24 F0 00 00 00         mov r12, qword ptr [rsp + 0xf0]
002E0C5B  4D 8B 64 24 20                  mov r12, qword ptr [r12 + 0x20]
002E0C60  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
002E0C65  83 BC 24 08 01 00 00 02         cmp dword ptr [rsp + 0x108], 2
002E0C6D  0F 85 24 01 00 00               jne 0x1402e0d97
002E0C73  49 8B 04 24                     mov rax, qword ptr [r12]
002E0C77  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
002E0C7C  4C 8D 78 48                     lea r15, [rax + 0x48]
002E0C80  44 0F 20 C1                     mov rcx, cr8
002E0C84  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
002E0C89  B8 02 00 00 00                  mov eax, 2
002E0C8E  44 0F 22 C0                     mov cr8, rax
002E0C92  83 3D 87 60 CE 00 00            cmp dword ptr [rip + 0xce6087], 0
002E0C99  0F 85 A8 02 00 00               jne 0x1402e0f47
002E0C9F  F6 05 60 5E CE 00 21            test byte ptr [rip + 0xce5e60], 0x21
002E0CA6  0F 85 53 02 00 00               jne 0x1402e0eff
002E0CAC  45 33 C9                        xor r9d, r9d
002E0CAF  F0 41 0F BA 2F 1F               lock bts dword ptr [r15], 0x1f
002E0CB5  41 8B F9                        mov edi, r9d
002E0CB8  73 0D                           jae 0x1402e0cc7
002E0CBA  0F B6 D1                        movzx edx, cl
002E0CBD  49 8B CF                        mov rcx, r15
002E0CC0  E8 DB 2C 04 00                  call 0x1403239a0
002E0CC5  8B F8                           mov edi, eax
002E0CC7  41 8B 17                        mov edx, dword ptr [r15]
002E0CCA  8B CA                           mov ecx, edx
002E0CCC  0F BA F1 1E                     btr ecx, 0x1e
002E0CD0  81 F9 00 00 00 80               cmp ecx, 0x80000000
002E0CD6  74 2E                           je 0x1402e0d06
002E0CD8  0F BA E2 1E                     bt edx, 0x1e
002E0CDC  72 08                           jb 0x1402e0ce6
002E0CDE  F0 41 81 0F 00 00 00 40         lock or dword ptr [r15], 0x40000000
002E0CE6  FF C7                           inc edi
002E0CE8  85 3D BE 45 CE 00               test dword ptr [rip + 0xce45be], edi
002E0CEE  0F 84 F3 02 00 00               je 0x1402e0fe7
002E0CF4  F3 90                           pause
002E0CF6  41 8B 17                        mov edx, dword ptr [r15]
002E0CF9  8B C2                           mov eax, edx
002E0CFB  0F BA F0 1E                     btr eax, 0x1e
002E0CFF  3D 00 00 00 80                  cmp eax, 0x80000000
002E0D04  75 D2                           jne 0x1402e0cd8
002E0D06  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
002E0D0B  33 C9                           xor ecx, ecx
002E0D0D  48 8B F8                        mov rdi, rax
002E0D10  44 8B E1                        mov r12d, ecx
002E0D13  44 8B E9                        mov r13d, ecx
002E0D16  48 8B 00                        mov rax, qword ptr [rax]
002E0D19  48 8B 50 40                     mov rdx, qword ptr [rax + 0x40]
002E0D1D  48 8B C7                        mov rax, rdi
002E0D20  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
002E0D25  48 83 7F 08 00                  cmp qword ptr [rdi + 8], 0
002E0D2A  0F 85 88 00 00 00               jne 0x1402e0db8
002E0D30  48 3B F8                        cmp rdi, rax
002E0D33  74 12                           je 0x1402e0d47
002E0D35  48 8B 7F 10                     mov rdi, qword ptr [rdi + 0x10]
002E0D39  48 85 D2                        test rdx, rdx
002E0D3C  75 04                           jne 0x1402e0d42
002E0D3E  41 83 E4 F7                     and r12d, 0xfffffff7
002E0D42  48 85 FF                        test rdi, rdi
002E0D45  75 DE                           jne 0x1402e0d25
002E0D47  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
002E0D4C  40 80 FF 11                     cmp dil, 0x11
002E0D50  0F 84 A1 00 00 00               je 0x1402e0df7
002E0D56  F6 05 A9 5D CE 00 01            test byte ptr [rip + 0xce5da9], 1
002E0D5D  0F 85 CF 02 00 00               jne 0x1402e1032
002E0D63  41 89 0F                        mov dword ptr [r15], ecx
002E0D66  83 3D B3 5F CE 00 00            cmp dword ptr [rip + 0xce5fb3], 0
002E0D6D  74 0D                           je 0x1402e0d7c
002E0D6F  44 0F 20 C1                     mov rcx, cr8
002E0D73  40 0F B6 D7                     movzx edx, dil
002E0D77  E8 1C 49 21 00                  call 0x1404f5698
002E0D7C  40 0F B6 C7                     movzx eax, dil
002E0D80  44 0F 22 C0                     mov cr8, rax
002E0D84  4D 85 ED                        test r13, r13
002E0D87  0F 85 28 04 00 00               jne 0x1402e11b5
002E0D8D  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
002E0D92  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
002E0D97  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
002E0D9F  4C 3B 60 20                     cmp r12, qword ptr [rax + 0x20]
002E0DA3  0F 84 74 01 00 00               je 0x1402e0f1d
002E0DA9  4D 8B 64 24 10                  mov r12, qword ptr [r12 + 0x10]
002E0DAE  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
002E0DB3  E9 19 FE FF FF                  jmp 0x1402e0bd1
002E0DB8  4C 8B 07                        mov r8, qword ptr [rdi]
002E0DBB  4C 8B D7                        mov r10, rdi
002E0DBE  49 83 78 40 00                  cmp qword ptr [r8 + 0x40], 0
002E0DC3  74 47                           je 0x1402e0e0c
002E0DC5  41 8B 40 38                     mov eax, dword ptr [r8 + 0x38]
002E0DC9  A8 20                           test al, 0x20
002E0DCB  75 3F                           jne 0x1402e0e0c
002E0DCD  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
002E0DD0  0F BA E0 10                     bt eax, 0x10
002E0DD4  72 36                           jb 0x1402e0e0c
002E0DD6  48 83 7F 50 00                  cmp qword ptr [rdi + 0x50], 0
002E0DDB  75 2F                           jne 0x1402e0e0c
002E0DDD  45 33 C9                        xor r9d, r9d
002E0DE0  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
002E0DE5  4C 8B C7                        mov r8, rdi
002E0DE8  BA 01 20 04 00                  mov edx, 0x42001
002E0DED  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
002E0DF1  E8 6A C8 21 00                  call 0x1404fd660
002E0DF6  CC                              int3
002E0DF7  F6 05 08 5D CE 00 01            test byte ptr [rip + 0xce5d08], 1
002E0DFE  0F 85 51 02 00 00               jne 0x1402e1055
002E0E04  41 89 0F                        mov dword ptr [r15], ecx
002E0E07  E9 78 FF FF FF                  jmp 0x1402e0d84
002E0E0C  41 8B C4                        mov eax, r12d
002E0E0F  4C 8B D9                        mov r11, rcx
002E0E12  24 0C                           and al, 0xc
002E0E14  3C 08                           cmp al, 8
002E0E16  75 70                           jne 0x1402e0e88
002E0E18  41 F6 40 3E 0C                  test byte ptr [r8 + 0x3e], 0xc
002E0E1D  75 69                           jne 0x1402e0e88
002E0E1F  49 83 78 40 00                  cmp qword ptr [r8 + 0x40], 0
002E0E24  75 0A                           jne 0x1402e0e30
002E0E26  41 F7 40 5C 00 00 01 00         test dword ptr [r8 + 0x5c], 0x10000
002E0E2E  75 58                           jne 0x1402e0e88
002E0E30  41 0F B7 40 3C                  movzx eax, word ptr [r8 + 0x3c]
002E0E35  48 8B 0D 4C F2 B4 00            mov rcx, qword ptr [rip + 0xb4f24c]
002E0E3C  25 FF 03 00 00                  and eax, 0x3ff
002E0E41  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
002E0E45  41 F6 C4 10                     test r12b, 0x10
002E0E49  0F 85 29 02 00 00               jne 0x1402e1078
002E0E4F  45 84 E4                        test r12b, r12b
002E0E52  0F 88 9F 02 00 00               js 0x1402e10f7
002E0E58  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002E0E61  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002E0E68  0F B7 81 AE 04 00 00            movzx eax, word ptr [rcx + 0x4ae]
002E0E6F  48 8B 0D 12 F2 B4 00            mov rcx, qword ptr [rip + 0xb4f212]
002E0E76  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
002E0E7A  48 3B C2                        cmp rax, rdx
002E0E7D  0F 85 80 02 00 00               jne 0x1402e1103
002E0E83  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002E0E88  49 83 78 40 00                  cmp qword ptr [r8 + 0x40], 0
002E0E8D  75 14                           jne 0x1402e0ea3
002E0E8F  4D 03 EB                        add r13, r11
002E0E92  48 85 D2                        test rdx, rdx
002E0E95  75 46                           jne 0x1402e0edd
002E0E97  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
002E0E9C  33 C9                           xor ecx, ecx
002E0E9E  E9 8D FE FF FF                  jmp 0x1402e0d30
002E0EA3  41 8B 48 38                     mov ecx, dword ptr [r8 + 0x38]
002E0EA7  F6 C1 20                        test cl, 0x20
002E0EAA  75 E3                           jne 0x1402e0e8f
002E0EAC  41 8B 4A 20                     mov ecx, dword ptr [r10 + 0x20]
002E0EB0  0F BA E1 10                     bt ecx, 0x10
002E0EB4  72 D9                           jb 0x1402e0e8f
002E0EB6  49 8B 42 50                     mov rax, qword ptr [r10 + 0x50]
002E0EBA  48 85 C0                        test rax, rax
002E0EBD  0F 85 18 01 00 00               jne 0x1402e0fdb
002E0EC3  45 33 C9                        xor r9d, r9d
002E0EC6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002E0ECB  4D 8B C2                        mov r8, r10
002E0ECE  BA 01 20 04 00                  mov edx, 0x42001
002E0ED3  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
002E0ED7  E8 84 C7 21 00                  call 0x1404fd660
002E0EDC  CC                              int3
002E0EDD  48 83 7F 50 00                  cmp qword ptr [rdi + 0x50], 0
002E0EE2  75 B3                           jne 0x1402e0e97
002E0EE4  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
002E0EE7  0F BA E0 10                     bt eax, 0x10
002E0EEB  72 AA                           jb 0x1402e0e97
002E0EED  48 8B CF                        mov rcx, rdi
002E0EF0  E8 5B 7E FB FF                  call 0x140298d50
002E0EF5  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002E0EFA  4C 03 E8                        add r13, rax
002E0EFD  EB 98                           jmp 0x1402e0e97
002E0EFF  8B 05 53 CF C2 00               mov eax, dword ptr [rip + 0xc2cf53]
002E0F05  85 C0                           test eax, eax
002E0F07  0F 85 9F FD FF FF               jne 0x1402e0cac
002E0F0D  0F B6 D1                        movzx edx, cl
002E0F10  49 8B CF                        mov rcx, r15
002E0F13  E8 58 2B 04 00                  call 0x140323a70
002E0F18  E9 E9 FD FF FF                  jmp 0x1402e0d06
002E0F1D  4C 8B BC 24 F8 00 00 00         mov r15, qword ptr [rsp + 0xf8]
002E0F25  85 F6                           test esi, esi
002E0F27  0F 88 4C FB FF FF               js 0x1402e0a79
002E0F2D  E9 EE FA FF FF                  jmp 0x1402e0a20
002E0F32  0F B6 D0                        movzx edx, al
002E0F35  40 0F B6 CF                     movzx ecx, dil
002E0F39  E8 BE 47 21 00                  call 0x1404f56fc
002E0F3E  4D 8D 45 48                     lea r8, [r13 + 0x48]
002E0F42  E9 4A FA FF FF                  jmp 0x1402e0991
002E0F47  0F B6 D0                        movzx edx, al
002E0F4A  E8 AD 47 21 00                  call 0x1404f56fc
002E0F4F  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
002E0F54  E9 46 FD FF FF                  jmp 0x1402e0c9f
002E0F59  49 8B C8                        mov rcx, r8
002E0F5C  E8 2F 96 F6 FF                  call 0x14024a590
002E0F61  E9 AE FA FF FF                  jmp 0x1402e0a14
002E0F66  4D 8B C4                        mov r8, r12
002E0F69  BA FF FF FF FF                  mov edx, 0xffffffff
002E0F6E  49 8B CD                        mov rcx, r13
002E0F71  E8 E2 7D 06 00                  call 0x140348d58
002E0F76  48 8B EF                        mov rbp, rdi
002E0F79  48 C1 E5 09                     shl rbp, 9
002E0F7D  48 8B 48 48                     mov rcx, qword ptr [rax + 0x48]
002E0F81  41 8B 44 24 24                  mov eax, dword ptr [r12 + 0x24]
002E0F86  48 C1 E1 09                     shl rcx, 9
002E0F8A  48 2B E9                        sub rbp, rcx
002E0F8D  48 C1 E0 09                     shl rax, 9
002E0F91  48 81 E5 00 F0 FF FF            and rbp, 0xfffffffffffff000
002E0F98  48 03 E8                        add rbp, rax
002E0F9B  45 33 C0                        xor r8d, r8d
002E0F9E  E9 28 F9 FF FF                  jmp 0x1402e08cb
002E0FA3  4C 8B C6                        mov r8, rsi
002E0FA6  BA FF FF FF FF                  mov edx, 0xffffffff
002E0FAB  49 8B C9                        mov rcx, r9
002E0FAE  E8 A5 7D 06 00                  call 0x140348d58
002E0FB3  48 C1 E7 09                     shl rdi, 9
002E0FB7  48 8B 48 48                     mov rcx, qword ptr [rax + 0x48]
002E0FBB  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
002E0FBE  48 C1 E1 09                     shl rcx, 9
002E0FC2  48 2B F9                        sub rdi, rcx
002E0FC5  48 C1 E0 09                     shl rax, 9
002E0FC9  48 81 E7 00 F0 FF FF            and rdi, 0xfffffffffffff000
002E0FD0  48 03 F8                        add rdi, rax
002E0FD3  45 33 C0                        xor r8d, r8d
002E0FD6  E9 3C F9 FF FF                  jmp 0x1402e0917
002E0FDB  48 FF C8                        dec rax
002E0FDE  49 89 42 50                     mov qword ptr [r10 + 0x50], rax
002E0FE2  E9 A8 FE FF FF                  jmp 0x1402e0e8f
002E0FE7  8B 05 CB 5A CE 00               mov eax, dword ptr [rip + 0xce5acb]
002E0FED  A8 40                           test al, 0x40
002E0FEF  0F 84 FF FC FF FF               je 0x1402e0cf4
002E0FF5  E8 96 E4 02 00                  call 0x14030f490
002E0FFA  84 C0                           test al, al
002E0FFC  0F 84 F2 FC FF FF               je 0x1402e0cf4
002E1002  8B CF                           mov ecx, edi
002E1004  E8 57 E4 02 00                  call 0x14030f460
002E1009  E9 E8 FC FF FF                  jmp 0x1402e0cf6
002E100E  40 0F B6 D7                     movzx edx, dil
002E1012  49 8B C8                        mov rcx, r8
002E1015  E8 D6 7B 06 00                  call 0x140348bf0
002E101A  49 8B CD                        mov rcx, r13
002E101D  E8 92 EC FF FF                  call 0x1402dfcb4
002E1022  33 C0                           xor eax, eax
002E1024  E9 CA FA FF FF                  jmp 0x1402e0af3
002E1029  4D 89 77 08                     mov qword ptr [r15 + 8], r14
002E102D  E9 BF FA FF FF                  jmp 0x1402e0af1
002E1032  8B 05 20 CE C2 00               mov eax, dword ptr [rip + 0xc2ce20]
002E1038  85 C0                           test eax, eax
002E103A  0F 85 23 FD FF FF               jne 0x1402e0d63
002E1040  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
002E1048  49 8B CF                        mov rcx, r15
002E104B  E8 F4 FE FD FF                  call 0x1402c0f44
002E1050  E9 11 FD FF FF                  jmp 0x1402e0d66
002E1055  8B 05 FD CD C2 00               mov eax, dword ptr [rip + 0xc2cdfd]
002E105B  85 C0                           test eax, eax
002E105D  0F 85 A1 FD FF FF               jne 0x1402e0e04
002E1063  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
002E106B  49 8B CF                        mov rcx, r15
002E106E  E8 D1 FE FD FF                  call 0x1402c0f44
002E1073  E9 0C FD FF FF                  jmp 0x1402e0d84
002E1078  45 33 C9                        xor r9d, r9d
002E107B  41 8B C1                        mov eax, r9d
002E107E  E9 F7 FD FF FF                  jmp 0x1402e0e7a
002E1083  48 8B D0                        mov rdx, rax
002E1086  49 8B CC                        mov rcx, r12
002E1089  E8 D6 43 18 00                  call 0x140465464
002E108E  85 C0                           test eax, eax
002E1090  0F 85 64 FB FF FF               jne 0x1402e0bfa
002E1096  E9 FC FC FF FF                  jmp 0x1402e0d97
002E109B  8B 05 B7 CD C2 00               mov eax, dword ptr [rip + 0xc2cdb7]
002E10A1  85 C0                           test eax, eax
002E10A3  0F 85 41 F9 FF FF               jne 0x1402e09ea
002E10A9  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
002E10B1  49 8B C8                        mov rcx, r8
002E10B4  E8 8F FE 00 00                  call 0x1402f0f48
002E10B9  E9 38 F9 FF FF                  jmp 0x1402e09f6
002E10BE  49 8B C8                        mov rcx, r8
002E10C1  E9 E7 F7 FF FF                  jmp 0x1402e08ad
002E10C6  49 8B C8                        mov rcx, r8
002E10C9  E9 2F F8 FF FF                  jmp 0x1402e08fd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002E0B15(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbp;
    unsigned int v_stack_p108;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_pE8;
    unsigned __int64 v_stack_pF0;
    unsigned __int64 v_stack_pF8;

    if (v_rdi < a2) goto loc_002E0F66;
    if (v_rdi >= (a2 + (unsigned int)(*(unsigned int *)(v_r12 + 44)) * 8)) goto loc_002E0F66;
    v_rbp = (v_rdi) << (9);
    a2 = (a2) << (9);
    v_rbp = (v_rbp) - (a2);
    result = ((unsigned int)(*(unsigned int *)(v_r12 + 36))) << (9);
    v_rbp = (v_rbp) & (0xFFFFFFFFFFFFF000ULL);
    v_rbp = (v_rbp) + (result);
loc_002E0F66:
    result = MiGetSharedProtos(v_r13, (unsigned int)(0xFFFFFFFFULL), v_r12, a4);
    v_rbp = (v_rdi) << (9);
    a1 = (*(unsigned __int64 *)(result + 72)) << (9);
    v_rbp = (v_rbp) - (a1);
    result = ((unsigned int)(*(unsigned int *)(v_r12 + 36))) << (9);
    v_rbp = (v_rbp) & (0xFFFFFFFFFFFFF000ULL);
    v_rbp = (v_rbp) + (result);
    a3 = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002E0B15(int64_t Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbp;
    uint32_t v_stack_p108;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_pE8;
    uint64_t v_stack_pF0;
    uint64_t v_stack_pF8;

    if (local_rdi < Arg2) goto loc_002E0F66;
    if (local_rdi >= (Arg2 + (uint32_t)(*(uint32_t *)(local_r12 + 0x2C)) * 8)) goto loc_002E0F66;
    local_rbp = (local_rdi) << (9);
    Arg2 = (Arg2) << (9);
    local_rbp = (local_rbp) - (Arg2);
    result = ((uint32_t)(*(uint32_t *)(local_r12 + 0x24))) << (9);
    local_rbp = (local_rbp) & (0xFFFFFFFFFFFFF000ULL);
    local_rbp = (local_rbp) + (result);
loc_002E0F66:
    result = MiGetSharedProtos(local_r13, (uint32_t)(0xFFFFFFFFULL), local_r12, a4);
    local_rbp = (local_rdi) << (9);
    Arg1 = (*(uint64_t *)(result + 0x48)) << (9);
    local_rbp = (local_rbp) - (Arg1);
    result = ((uint32_t)(*(uint32_t *)(local_r12 + 0x24))) << (9);
    local_rbp = (local_rbp) & (0xFFFFFFFFFFFFF000ULL);
    local_rbp = (local_rbp) + (result);
    Arg3 = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E0B15&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
