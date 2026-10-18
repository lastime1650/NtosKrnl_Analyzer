# MiCaptureDeleteHierarchy

- RVA: `0x0027F5F0`–`0x0027FDBB` (길이 `1,995` bytes)
- VA: `0x000000014027F5F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006668C`
- 디코드: `457`개 명령, `1,995/1,995` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0027F731` → [MiMakeSystemAddressValid](MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x0027F9D1` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0027F9F4` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0027FA8A` → [MiFastLockLeafPageTable](MiFastLockLeafPageTable_function_00276340.md) (function, `0x00276340`)
- `0x0027FB10` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x0027FC17` → [ExReleaseSpinLockRegardlessFromDpcLevel](../23/ExReleaseSpinLockRegardlessFromDpcLevel_function_0023A330.md) (function, `0x0023A330`)
- `0x0027FC48` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0027FD32` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x0027FD51` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0027FD6D` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x0027FDA2` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)

### Direct callers
- [MiRemoveVad](../29/MiRemoveVad_function_00295C78.md) at `0x00295D85`
- [MiDeleteEmptyPageTableCommit](../48/MiDeleteEmptyPageTableCommit_function_004834F4.md) at `0x00483692`

### Static image references
- `0x0027F885` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0027F965` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0027FA58` → RVA `0x00E2CB40` (`.data`; read)
- `0x0027FAF7` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0027F5F0  4C 8B DC                        mov r11, rsp
0027F5F3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0027F5F7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0027F5FB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0027F5FF  57                              push rdi
0027F600  41 54                           push r12
0027F602  41 55                           push r13
0027F604  41 56                           push r14
0027F606  41 57                           push r15
0027F608  48 83 EC 70                     sub rsp, 0x70
0027F60C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027F615  4D 8B E9                        mov r13, r9
0027F618  45 0F B6 E0                     movzx r12d, r8b
0027F61C  48 C1 E9 09                     shr rcx, 9
0027F620  45 33 C9                        xor r9d, r9d
0027F623  48 BD 00 00 00 00 80 F6 FF FF   movabs rbp, 0xfffff68000000000
0027F62D  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
0027F637  4C 8B B8 B8 00 00 00            mov r15, qword ptr [rax + 0xb8]
0027F63E  49 23 C8                        and rcx, r8
0027F641  49 81 C7 00 04 00 00            add r15, 0x400
0027F648  45 89 4D 00                     mov dword ptr [r13], r9d
0027F64C  48 8B C5                        mov rax, rbp
0027F64F  48 03 C8                        add rcx, rax
0027F652  49 89 4B 98                     mov qword ptr [r11 - 0x68], rcx
0027F656  48 C1 E9 09                     shr rcx, 9
0027F65A  49 23 C8                        and rcx, r8
0027F65D  48 8B C5                        mov rax, rbp
0027F660  48 03 C8                        add rcx, rax
0027F663  49 89 4B A0                     mov qword ptr [r11 - 0x60], rcx
0027F667  48 C1 E9 09                     shr rcx, 9
0027F66B  49 23 C8                        and rcx, r8
0027F66E  48 8B C5                        mov rax, rbp
0027F671  48 03 C8                        add rcx, rax
0027F674  49 89 4B A8                     mov qword ptr [r11 - 0x58], rcx
0027F678  48 C1 E9 09                     shr rcx, 9
0027F67C  49 23 C8                        and rcx, r8
0027F67F  48 8B C5                        mov rax, rbp
0027F682  48 03 C8                        add rcx, rax
0027F685  48 C1 EA 09                     shr rdx, 9
0027F689  49 89 4B B0                     mov qword ptr [r11 - 0x50], rcx
0027F68D  49 23 D0                        and rdx, r8
0027F690  48 8B C5                        mov rax, rbp
0027F693  48 03 D0                        add rdx, rax
0027F696  49 89 53 B8                     mov qword ptr [r11 - 0x48], rdx
0027F69A  48 C1 EA 09                     shr rdx, 9
0027F69E  49 23 D0                        and rdx, r8
0027F6A1  48 8B C5                        mov rax, rbp
0027F6A4  48 03 D0                        add rdx, rax
0027F6A7  49 89 53 C0                     mov qword ptr [r11 - 0x40], rdx
0027F6AB  48 C1 EA 09                     shr rdx, 9
0027F6AF  49 23 D0                        and rdx, r8
0027F6B2  48 8B C5                        mov rax, rbp
0027F6B5  48 03 D0                        add rdx, rax
0027F6B8  49 89 53 C8                     mov qword ptr [r11 - 0x38], rdx
0027F6BC  48 C1 EA 09                     shr rdx, 9
0027F6C0  49 23 D0                        and rdx, r8
0027F6C3  48 8B C5                        mov rax, rbp
0027F6C6  48 03 D0                        add rdx, rax
0027F6C9  41 8B F9                        mov edi, r9d
0027F6CC  49 89 53 D0                     mov qword ptr [r11 - 0x30], rdx
0027F6D0  83 FF 02                        cmp edi, 2
0027F6D3  72 1F                           jb 0x14027f6f4
0027F6D5  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0027F6DA  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0027F6DE  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
0027F6E2  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0027F6E6  49 8B E3                        mov rsp, r11
0027F6E9  41 5F                           pop r15
0027F6EB  41 5E                           pop r14
0027F6ED  41 5D                           pop r13
0027F6EF  41 5C                           pop r12
0027F6F1  5F                              pop rdi
0027F6F2  C3                              ret
0027F6F3  CC                              int3
0027F6F4  8B C7                           mov eax, edi
0027F6F6  4C 8D 74 24 30                  lea r14, [rsp + 0x30]
0027F6FB  48 C1 E0 05                     shl rax, 5
0027F6FF  BE 03 00 00 00                  mov esi, 3
0027F704  4C 03 F0                        add r14, rax
0027F707  83 FE 01                        cmp esi, 1
0027F70A  0F 8C 6E 01 00 00               jl 0x14027f87e
0027F710  48 63 C6                        movsxd rax, esi
0027F713  49 8B 1C C6                     mov rbx, qword ptr [r14 + rax*8]
0027F717  83 FE 03                        cmp esi, 3
0027F71A  0F 84 4C 03 00 00               je 0x14027fa6c
0027F720  33 C0                           xor eax, eax
0027F722  41 B9 08 00 00 00               mov r9d, 8
0027F728  8B D0                           mov edx, eax
0027F72A  45 0F B6 C4                     movzx r8d, r12b
0027F72E  48 8B CB                        mov rcx, rbx
0027F731  E8 3A 08 00 00                  call 0x14027ff70
0027F736  45 33 DB                        xor r11d, r11d
0027F739  44 8B C8                        mov r9d, eax
0027F73C  85 C0                           test eax, eax
0027F73E  0F 88 6E 05 00 00               js 0x14027fcb2
0027F744  48 8B D3                        mov rdx, rbx
0027F747  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0027F751  48 C1 EA 09                     shr rdx, 9
0027F755  48 23 D0                        and rdx, rax
0027F758  48 8B CD                        mov rcx, rbp
0027F75B  48 03 D1                        add rdx, rcx
0027F75E  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
0027F768  48 8B 0B                        mov rcx, qword ptr [rbx]
0027F76B  48 8B C0                        mov rax, rax
0027F76E  48 3B D8                        cmp rbx, rax
0027F771  72 2D                           jb 0x14027f7a0
0027F773  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
0027F77D  48 8B C0                        mov rax, rax
0027F780  48 3B D8                        cmp rbx, rax
0027F783  77 1B                           ja 0x14027f7a0
0027F785  F6 C1 01                        test cl, 1
0027F788  74 16                           je 0x14027f7a0
0027F78A  F6 C1 42                        test cl, 0x42
0027F78D  41 0F 95 C0                     setne r8b
0027F791  F6 C1 20                        test cl, 0x20
0027F794  0F 95 C0                        setne al
0027F797  44 84 C0                        test al, r8b
0027F79A  0F 84 E5 00 00 00               je 0x14027f885
0027F7A0  48 85 C9                        test rcx, rcx
0027F7A3  0F 84 0C 05 00 00               je 0x14027fcb5
0027F7A9  41 8B EB                        mov ebp, r11d
0027F7AC  85 FF                           test edi, edi
0027F7AE  75 72                           jne 0x14027f822
0027F7B0  83 FE 01                        cmp esi, 1
0027F7B3  75 6D                           jne 0x14027f822
0027F7B5  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0027F7BA  49 8B C0                        mov rax, r8
0027F7BD  48 33 C3                        xor rax, rbx
0027F7C0  48 A9 00 F0 FF FF               test rax, -0x1000
0027F7C6  75 5A                           jne 0x14027f822
0027F7C8  4C 8D 74 24 50                  lea r14, [rsp + 0x50]
0027F7CD  8B FE                           mov edi, esi
0027F7CF  45 85 C9                        test r9d, r9d
0027F7D2  78 4A                           js 0x14027f81e
0027F7D4  49 8B 00                        mov rax, qword ptr [r8]
0027F7D7  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
0027F7E1  48 8B C9                        mov rcx, rcx
0027F7E4  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0027F7E9  4C 3B C1                        cmp r8, rcx
0027F7EC  72 2B                           jb 0x14027f819
0027F7EE  48 B9 F8 D7 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed7f8
0027F7F8  48 8B C9                        mov rcx, rcx
0027F7FB  4C 3B C1                        cmp r8, rcx
0027F7FE  77 19                           ja 0x14027f819
0027F800  40 84 C7                        test dil, al
0027F803  74 14                           je 0x14027f819
0027F805  A8 42                           test al, 0x42
0027F807  41 0F 95 C0                     setne r8b
0027F80B  A8 20                           test al, 0x20
0027F80D  0F 95 C1                        setne cl
0027F810  44 84 C1                        test cl, r8b
0027F813  0F 84 3B 03 00 00               je 0x14027fb54
0027F819  48 85 C0                        test rax, rax
0027F81C  75 04                           jne 0x14027f822
0027F81E  41 88 7D 01                     mov byte ptr [r13 + 1], dil
0027F822  48 85 D2                        test rdx, rdx
0027F825  74 42                           je 0x14027f869
0027F827  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
0027F831  48 8B C0                        mov rax, rax
0027F834  48 3B D0                        cmp rdx, rax
0027F837  0F 84 3D 01 00 00               je 0x14027f97a
0027F83D  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
0027F844  A8 0F                           test al, 0xf
0027F846  0F 84 A2 00 00 00               je 0x14027f8ee
0027F84C  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
0027F853  A8 0F                           test al, 0xf
0027F855  0F 85 A3 01 00 00               jne 0x14027f9fe
0027F85B  48 B8 FF FF FF FF FF FF FF CF   movabs rax, 0xcfffffffffffffff
0027F865  F0 48 21 02                     lock and qword ptr [rdx], rax
0027F869  85 ED                           test ebp, ebp
0027F86B  48 BD 00 00 00 00 80 F6 FF FF   movabs rbp, 0xfffff68000000000
0027F875  75 07                           jne 0x14027f87e
0027F877  FF CE                           dec esi
0027F879  E9 89 FE FF FF                  jmp 0x14027f707
0027F87E  FF C7                           inc edi
0027F880  E9 4B FE FF FF                  jmp 0x14027f6d0
0027F885  48 F7 05 F8 71 D4 00 00 00 60 00  test qword ptr [rip + 0xd471f8], 0x600000
0027F890  0F 84 0A FF FF FF               je 0x14027f7a0
0027F896  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027F89F  4C 8B 80 B8 00 00 00            mov r8, qword ptr [rax + 0xb8]
0027F8A6  41 80 B8 60 01 00 00 01         cmp byte ptr [r8 + 0x160], 1
0027F8AE  0F 84 EC FE FF FF               je 0x14027f7a0
0027F8B4  4D 8B 90 08 05 00 00            mov r10, qword ptr [r8 + 0x508]
0027F8BB  4D 85 D2                        test r10, r10
0027F8BE  0F 84 DC FE FF FF               je 0x14027f7a0
0027F8C4  48 8B C3                        mov rax, rbx
0027F8C7  48 C1 E8 03                     shr rax, 3
0027F8CB  25 FF 01 00 00                  and eax, 0x1ff
0027F8D0  49 8B 04 C2                     mov rax, qword ptr [r10 + rax*8]
0027F8D4  A8 20                           test al, 0x20
0027F8D6  74 04                           je 0x14027f8dc
0027F8D8  48 83 C9 20                     or rcx, 0x20
0027F8DC  4C 8B C1                        mov r8, rcx
0027F8DF  48 83 C9 42                     or rcx, 0x42
0027F8E3  A8 42                           test al, 0x42
0027F8E5  49 0F 44 C8                     cmove rcx, r8
0027F8E9  E9 B2 FE FF FF                  jmp 0x14027f7a0
0027F8EE  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
0027F8F8  48 8B C0                        mov rax, rax
0027F8FB  48 3B D0                        cmp rdx, rax
0027F8FE  0F 82 48 FF FF FF               jb 0x14027f84c
0027F904  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0027F90E  48 8B C0                        mov rax, rax
0027F911  48 3B D0                        cmp rdx, rax
0027F914  0F 87 32 FF FF FF               ja 0x14027f84c
0027F91A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027F923  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0027F92A  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
0027F931  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
0027F938  48 85 C9                        test rcx, rcx
0027F93B  0F 84 0B FF FF FF               je 0x14027f84c
0027F941  48 C1 EA 03                     shr rdx, 3
0027F945  81 E2 FF 01 00 00               and edx, 0x1ff
0027F94B  8B 04 91                        mov eax, dword ptr [rcx + rdx*4]
0027F94E  48 8D 0C 91                     lea rcx, [rcx + rdx*4]
0027F952  A9 FF FF FF 3F                  test eax, 0x3fffffff
0027F957  0F 85 BD 01 00 00               jne 0x14027fb1a
0027F95D  85 C0                           test eax, eax
0027F95F  0F 89 D7 03 00 00               jns 0x14027fd3c
0027F965  F6 05 9A 71 D4 00 01            test byte ptr [rip + 0xd4719a], 1
0027F96C  0F 85 E5 03 00 00               jne 0x14027fd57
0027F972  44 89 19                        mov dword ptr [rcx], r11d
0027F975  E9 EF FE FF FF                  jmp 0x14027f869
0027F97A  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0027F983  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
0027F98A  24 0F                           and al, 0xf
0027F98C  0F 85 A4 01 00 00               jne 0x14027fb36
0027F992  B9 30 00 00 00                  mov ecx, 0x30
0027F997  45 33 C9                        xor r9d, r9d
0027F99A  48 8D 9A 40 9C 00 00            lea rbx, [rdx + 0x9c40]
0027F9A1  48 03 D9                        add rbx, rcx
0027F9A4  F6 05 5B 71 D4 00 01            test byte ptr [rip + 0xd4715b], 1
0027F9AB  0F 85 46 01 00 00               jne 0x14027faf7
0027F9B1  0F 0D 0B                        prefetchw byte ptr [rbx]
0027F9B4  48 8B 03                        mov rax, qword ptr [rbx]
0027F9B7  48 85 C0                        test rax, rax
0027F9BA  75 1D                           jne 0x14027f9d9
0027F9BC  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0027F9C0  48 8B C3                        mov rax, rbx
0027F9C3  F0 4C 0F B1 09                  lock cmpxchg qword ptr [rcx], r9
0027F9C8  0F 84 9B FE FF FF               je 0x14027f869
0027F9CE  48 8B CB                        mov rcx, rbx
0027F9D1  E8 CA 80 F9 FF                  call 0x140217aa0
0027F9D6  45 33 C9                        xor r9d, r9d
0027F9D9  48 8D 48 08                     lea rcx, [rax + 8]
0027F9DD  4C 89 0B                        mov qword ptr [rbx], r9
0027F9E0  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
0027F9E4  48 8B C2                        mov rax, rdx
0027F9E7  48 87 01                        xchg qword ptr [rcx], rax
0027F9EA  32 C2                           xor al, dl
0027F9EC  A8 04                           test al, 4
0027F9EE  0F 84 75 FE FF FF               je 0x14027f869
0027F9F4  E8 27 82 F9 FF                  call 0x140217c20
0027F9F9  E9 6B FE FF FF                  jmp 0x14027f869
0027F9FE  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
0027FA08  48 8B C1                        mov rax, rcx
0027FA0B  48 3B D0                        cmp rdx, rax
0027FA0E  0F 82 47 FE FF FF               jb 0x14027f85b
0027FA14  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0027FA1E  48 8B C0                        mov rax, rax
0027FA21  48 3B D0                        cmp rdx, rax
0027FA24  0F 87 31 FE FF FF               ja 0x14027f85b
0027FA2A  48 8B C1                        mov rax, rcx
0027FA2D  48 2B D0                        sub rdx, rax
0027FA30  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
0027FA37  48 C1 FA 03                     sar rdx, 3
0027FA3B  44 8D 04 12                     lea r8d, [rdx + rdx]
0027FA3F  BA 02 00 00 00                  mov edx, 2
0027FA44  41 8B C8                        mov ecx, r8d
0027FA47  41 8B C0                        mov eax, r8d
0027FA4A  83 E1 1F                        and ecx, 0x1f
0027FA4D  D3 E2                           shl edx, cl
0027FA4F  F7 D2                           not edx
0027FA51  0F B3 CA                        btr edx, ecx
0027FA54  48 C1 E8 05                     shr rax, 5
0027FA58  48 8D 0D E1 D0 BA 00            lea rcx, [rip + 0xbad0e1]
0027FA5F  F0 21 94 81 6C 26 00 00         lock and dword ptr [rcx + rax*4 + 0x266c], edx
0027FA67  E9 FD FD FF FF                  jmp 0x14027f869
0027FA6C  49 8B 16                        mov rdx, qword ptr [r14]
0027FA6F  48 C1 E2 19                     shl rdx, 0x19
0027FA73  48 8B C5                        mov rax, rbp
0027FA76  48 C1 E0 19                     shl rax, 0x19
0027FA7A  41 B8 08 00 00 00               mov r8d, 8
0027FA80  48 2B D0                        sub rdx, rax
0027FA83  49 8B CF                        mov rcx, r15
0027FA86  48 C1 FA 10                     sar rdx, 0x10
0027FA8A  E8 B1 68 FF FF                  call 0x140276340
0027FA8F  85 C0                           test eax, eax
0027FA91  0F 84 89 FC FF FF               je 0x14027f720
0027FA97  83 F8 03                        cmp eax, 3
0027FA9A  0F 84 D7 02 00 00               je 0x14027fd77
0027FAA0  48 98                           cdqe
0027FAA2  49 8B 14 C6                     mov rdx, qword ptr [r14 + rax*8]
0027FAA6  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
0027FAB0  48 8B C0                        mov rax, rax
0027FAB3  48 3B D0                        cmp rdx, rax
0027FAB6  0F 84 65 01 00 00               je 0x14027fc21
0027FABC  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
0027FAC3  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
0027FACD  A8 0F                           test al, 0xf
0027FACF  0F 84 EC 00 00 00               je 0x14027fbc1
0027FAD5  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
0027FADC  A8 0F                           test al, 0xf
0027FADE  0F 85 6E 01 00 00               jne 0x14027fc52
0027FAE4  48 B8 FF FF FF FF FF FF FF CF   movabs rax, 0xcfffffffffffffff
0027FAEE  F0 48 21 02                     lock and qword ptr [rdx], rax
0027FAF2  E9 29 FC FF FF                  jmp 0x14027f720
0027FAF7  8B 05 5B E3 C8 00               mov eax, dword ptr [rip + 0xc8e35b]
0027FAFD  85 C0                           test eax, eax
0027FAFF  0F 85 AC FE FF FF               jne 0x14027f9b1
0027FB05  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0027FB0D  48 8B CB                        mov rcx, rbx
0027FB10  E8 DB 7E F9 FF                  call 0x1402179f0
0027FB15  E9 4F FD FF FF                  jmp 0x14027f869
0027FB1A  F6 05 E5 6F D4 00 01            test byte ptr [rip + 0xd46fe5], 1
0027FB21  0F 85 65 02 00 00               jne 0x14027fd8c
0027FB27  F0 81 21 FF FF FF BF            lock and dword ptr [rcx], 0xbfffffff
0027FB2E  F0 FF 09                        lock dec dword ptr [rcx]
0027FB31  E9 33 FD FF FF                  jmp 0x14027f869
0027FB36  3C 07                           cmp al, 7
0027FB38  0F 84 D8 01 00 00               je 0x14027fd16
0027FB3E  3C 05                           cmp al, 5
0027FB40  B9 48 00 00 00                  mov ecx, 0x48
0027FB45  41 B9 00 00 00 00               mov r9d, 0
0027FB4B  41 0F 44 C9                     cmove ecx, r9d
0027FB4F  E9 46 FE FF FF                  jmp 0x14027f99a
0027FB54  48 F7 05 29 6F D4 00 00 00 60 00  test qword ptr [rip + 0xd46f29], 0x600000
0027FB5F  0F 84 B4 FC FF FF               je 0x14027f819
0027FB65  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0027FB6E  4C 8B 81 B8 00 00 00            mov r8, qword ptr [rcx + 0xb8]
0027FB75  41 38 B8 60 01 00 00            cmp byte ptr [r8 + 0x160], dil
0027FB7C  0F 84 97 FC FF FF               je 0x14027f819
0027FB82  4D 8B 88 08 05 00 00            mov r9, qword ptr [r8 + 0x508]
0027FB89  4D 85 C9                        test r9, r9
0027FB8C  0F 84 87 FC FF FF               je 0x14027f819
0027FB92  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0027FB97  48 C1 E9 03                     shr rcx, 3
0027FB9B  81 E1 FF 01 00 00               and ecx, 0x1ff
0027FBA1  49 8B 0C C9                     mov rcx, qword ptr [r9 + rcx*8]
0027FBA5  F6 C1 20                        test cl, 0x20
0027FBA8  74 04                           je 0x14027fbae
0027FBAA  48 83 C8 20                     or rax, 0x20
0027FBAE  4C 8B C0                        mov r8, rax
0027FBB1  48 83 C8 42                     or rax, 0x42
0027FBB5  F6 C1 42                        test cl, 0x42
0027FBB8  49 0F 44 C0                     cmove rax, r8
0027FBBC  E9 58 FC FF FF                  jmp 0x14027f819
0027FBC1  48 8B C1                        mov rax, rcx
0027FBC4  48 3B D0                        cmp rdx, rax
0027FBC7  0F 82 08 FF FF FF               jb 0x14027fad5
0027FBCD  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0027FBD7  48 8B C0                        mov rax, rax
0027FBDA  48 3B D0                        cmp rdx, rax
0027FBDD  0F 87 F2 FE FF FF               ja 0x14027fad5
0027FBE3  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0027FBEC  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0027FBF3  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
0027FBFA  48 8B 88 68 05 00 00            mov rcx, qword ptr [rax + 0x568]
0027FC01  48 85 C9                        test rcx, rcx
0027FC04  0F 84 A2 01 00 00               je 0x14027fdac
0027FC0A  C1 EA 03                        shr edx, 3
0027FC0D  81 E2 FF 01 00 00               and edx, 0x1ff
0027FC13  48 8D 0C 91                     lea rcx, [rcx + rdx*4]
0027FC17  E8 14 A7 FB FF                  call 0x14023a330
0027FC1C  E9 FF FA FF FF                  jmp 0x14027f720
0027FC21  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0027FC2A  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
0027FC31  24 0F                           and al, 0xf
0027FC33  0F 85 C5 00 00 00               jne 0x14027fcfe
0027FC39  B9 30 00 00 00                  mov ecx, 0x30
0027FC3E  48 81 C2 40 9C 00 00            add rdx, 0x9c40
0027FC45  48 03 CA                        add rcx, rdx
0027FC48  E8 63 75 F9 FF                  call 0x1402171b0
0027FC4D  E9 CE FA FF FF                  jmp 0x14027f720
0027FC52  48 8B C1                        mov rax, rcx
0027FC55  48 3B D0                        cmp rdx, rax
0027FC58  0F 82 86 FE FF FF               jb 0x14027fae4
0027FC5E  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
0027FC68  48 8B C0                        mov rax, rax
0027FC6B  48 3B D0                        cmp rdx, rax
0027FC6E  0F 87 70 FE FF FF               ja 0x14027fae4
0027FC74  48 8B C1                        mov rax, rcx
0027FC77  48 2B D0                        sub rdx, rax
0027FC7A  41 8B 87 B8 00 00 00            mov eax, dword ptr [r15 + 0xb8]
0027FC81  48 C1 FA 03                     sar rdx, 3
0027FC85  03 D2                           add edx, edx
0027FC87  8B C2                           mov eax, edx
0027FC89  8B CA                           mov ecx, edx
0027FC8B  48 C1 E8 05                     shr rax, 5
0027FC8F  48 8D 15 AA CE BA 00            lea rdx, [rip + 0xbaceaa]
0027FC96  83 E1 1F                        and ecx, 0x1f
0027FC99  48 8D 14 82                     lea rdx, [rdx + rax*4]
0027FC9D  B8 03 00 00 00                  mov eax, 3
0027FCA2  D3 E0                           shl eax, cl
0027FCA4  F7 D0                           not eax
0027FCA6  F0 21 82 6C 26 00 00            lock and dword ptr [rdx + 0x266c], eax
0027FCAD  E9 6E FA FF FF                  jmp 0x14027f720
0027FCB2  49 8B D3                        mov rdx, r11
0027FCB5  8D 4E FF                        lea ecx, [rsi - 1]
0027FCB8  8B C7                           mov eax, edi
0027FCBA  41 B8 01 00 00 00               mov r8d, 1
0027FCC0  BD 01 00 00 00                  mov ebp, 1
0027FCC5  41 D2 E0                        shl r8b, cl
0027FCC8  46 88 04 28                     mov byte ptr [rax + r13], r8b
0027FCCC  85 FF                           test edi, edi
0027FCCE  0F 85 4E FB FF FF               jne 0x14027f822
0027FCD4  48 85 D2                        test rdx, rdx
0027FCD7  0F 85 D3 FA FF FF               jne 0x14027f7b0
0027FCDD  48 63 C6                        movsxd rax, esi
0027FCE0  48 8B CB                        mov rcx, rbx
0027FCE3  48 33 4C C4 50                  xor rcx, qword ptr [rsp + rax*8 + 0x50]
0027FCE8  48 F7 C1 00 F0 FF FF            test rcx, -0x1000
0027FCEF  0F 85 BB FA FF FF               jne 0x14027f7b0
0027FCF5  45 88 45 01                     mov byte ptr [r13 + 1], r8b
0027FCF9  E9 D7 F9 FF FF                  jmp 0x14027f6d5
0027FCFE  3C 07                           cmp al, 7
0027FD00  74 21                           je 0x14027fd23
0027FD02  3C 05                           cmp al, 5
0027FD04  B9 48 00 00 00                  mov ecx, 0x48
0027FD09  B8 00 00 00 00                  mov eax, 0
0027FD0E  0F 44 C8                        cmove ecx, eax
0027FD11  E9 28 FF FF FF                  jmp 0x14027fc3e
0027FD16  B9 18 00 00 00                  mov ecx, 0x18
0027FD1B  45 33 C9                        xor r9d, r9d
0027FD1E  E9 77 FC FF FF                  jmp 0x14027f99a
0027FD23  48 81 C2 40 9C 00 00            add rdx, 0x9c40
0027FD2A  B9 18 00 00 00                  mov ecx, 0x18
0027FD2F  48 03 CA                        add rcx, rdx
0027FD32  E8 79 74 F9 FF                  call 0x1402171b0
0027FD37  E9 E4 F9 FF FF                  jmp 0x14027f720
0027FD3C  45 33 C9                        xor r9d, r9d
0027FD3F  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
0027FD44  48 8B D1                        mov rdx, rcx
0027FD47  41 B8 00 01 00 00               mov r8d, 0x100
0027FD4D  41 8D 49 10                     lea ecx, [r9 + 0x10]
0027FD51  E8 0A D9 27 00                  call 0x1404fd660
0027FD56  CC                              int3
0027FD57  8B 05 FB E0 C8 00               mov eax, dword ptr [rip + 0xc8e0fb]
0027FD5D  85 C0                           test eax, eax
0027FD5F  0F 85 0D FC FF FF               jne 0x14027f972
0027FD65  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0027FD6D  E8 D2 11 04 00                  call 0x1402c0f44
0027FD72  E9 F2 FA FF FF                  jmp 0x14027f869
0027FD77  8D 70 FF                        lea esi, [rax - 1]
0027FD7A  45 33 DB                        xor r11d, r11d
0027FD7D  48 63 C6                        movsxd rax, esi
0027FD80  45 8B CB                        mov r9d, r11d
0027FD83  49 8B 1C C6                     mov rbx, qword ptr [r14 + rax*8]
0027FD87  E9 B8 F9 FF FF                  jmp 0x14027f744
0027FD8C  8B 05 C6 E0 C8 00               mov eax, dword ptr [rip + 0xc8e0c6]
0027FD92  85 C0                           test eax, eax
0027FD94  0F 85 8D FD FF FF               jne 0x14027fb27
0027FD9A  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0027FDA2  E8 A1 11 07 00                  call 0x1402f0f48
0027FDA7  E9 BD FA FF FF                  jmp 0x14027f869
0027FDAC  48 B9 00 D0 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed000
0027FDB6  E9 1A FD FF FF                  jmp 0x14027fad5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCaptureDeleteHierarchy(__int64 a1, __int64 a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_p28;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (112);
    a1 = (a1) >> (9);
    a4 = 0;
    a1 = (a1) & (a3);
    v_r15 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    *(unsigned int *)(a4) = 0;
    a1 = (a1) + (v_rbp);
    *(unsigned __int64 *)(v_rsp - 104) = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (a3);
    a1 = (a1) + (v_rbp);
    *(unsigned __int64 *)(v_rsp - 96) = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (a3);
    a1 = (a1) + (v_rbp);
    *(unsigned __int64 *)(v_rsp - 88) = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (a3);
    a1 = (a1) + (v_rbp);
    a2 = (a2) >> (9);
    *(unsigned __int64 *)(v_rsp - 80) = a1;
    a2 = (a2) & (a3);
    a2 = (a2) + (v_rbp);
    *(unsigned __int64 *)(v_rsp - 72) = a2;
    a2 = (a2) >> (9);
    a2 = (a2) & (a3);
    a2 = (a2) + (v_rbp);
    *(unsigned __int64 *)(v_rsp - 64) = a2;
    a2 = (a2) >> (9);
    a2 = (a2) & (a3);
    a2 = (a2) + (v_rbp);
    *(unsigned __int64 *)(v_rsp - 56) = a2;
    a2 = (a2) >> (9);
    a2 = (a2) & (a3);
    a2 = (a2) + (v_rbp);
    *(unsigned __int64 *)(v_rsp - 48) = a2;
loc_0027F6D0:
    if (0 < 2) goto loc_0027F6F4;
loc_0027F6D5:
    return v_rbp;
loc_0027F6F4:
    result = (0) << (5);
    v_r14 = (v_stack_m40) + (result);
loc_0027F707:
    if (3 < 1) goto loc_0027F87E;
    if (3 == 3) goto loc_0027FA6C;
loc_0027F720:
    result = 0;
    result = MiMakeSystemAddressValid(*(unsigned __int64 *)(v_r14 + (int)(3) * 8), 0, a3, 8);
    v_r11 = 0;
    if (sign_flag) goto loc_0027FCB2;
loc_0027F744:
    a2 = (*(unsigned __int64 *)(v_r14 + (int)(3) * 8)) >> (9);
    a2 = (a2) & (result);
    a2 = (a2) + (*(unsigned __int64 *)(v_stack_m28 + 56));
    if ((*(unsigned __int64 *)(v_r14 + (int)(3) * 8)) < result) goto loc_0027F7A0;
    if ((*(unsigned __int64 *)(v_r14 + (int)(3) * 8)) > result) goto loc_0027F7A0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + (int)(3) * 8)))) & (1)) == 0) goto loc_0027F7A0;
    a3 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + (int)(3) * 8)))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + (int)(3) * 8)))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & (a3)) == 0) goto loc_0027F885;
loc_0027F7A0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + (int)(3) * 8)) == 0) goto loc_0027FCB5;
    if (0 != 0) goto loc_0027F822;
loc_0027F7B0:
    if (3 != 1) goto loc_0027F822;
    result = (v_stack_m18) ^ (*(unsigned __int64 *)(v_r14 + (int)(3) * 8));
    if (((result) & (0xFFFFFFFFFFFFF000ULL)) != 0) goto loc_0027F822;
    if (sign_flag) goto loc_0027F81E;
    if (v_stack_m18 < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + (int)(3) * 8)))) goto loc_0027F819;
    if (v_stack_m18 > (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + (int)(3) * 8)))) goto loc_0027F819;
    if (((3) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m18)))) == 0) goto loc_0027F819;
    a3 = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m18))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m18))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & (a3)) == 0) goto loc_0027FB54;
loc_0027F819:
    if (*(unsigned __int64 *)(v_stack_m18) == 0) {
        *(unsigned __int8 *)(a4 + 1) = 3;
    }
    if (a2 == 0) goto loc_0027F869;
    if (a2 == (*(unsigned __int64 *)(v_stack_m18))) goto loc_0027F97A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r15 + 184)))) & (15)) == 0) goto loc_0027F8EE;
loc_0027F84C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r15 + 184)))) & (15)) != 0) goto loc_0027F9FE;
loc_0027F85B:
loc_0027F869:
    if (0 != 0) goto loc_0027F87E;
    v_rsi = (unsigned int)((3) - 1);
    goto loc_0027F707;
loc_0027F87E:
    v_rdi = (unsigned int)((3) + 1);
    goto loc_0027F6D0;
loc_0027F885:
    if (((*(unsigned __int64 *)(v_rip + 13922808)) & (0x600000ULL)) == 0) goto loc_0027F7A0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_0027F7A0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_0027F7A0;
    result = (*(unsigned __int64 *)(v_r14 + (int)(3) * 8)) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (32)) != 0) {
        a1 = (a1) | (32);
    }
    a1 = (a1) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) & (66)) == 0) { a1 = a1; }
    goto loc_0027F7A0;
loc_0027F8EE:
    if (a2 < (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) goto loc_0027F84C;
    if (a2 > (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + result * 8))) goto loc_0027F84C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_0027F84C;
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) & (511));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + a2 * 4)))) & (0x3FFFFFFFULL)) != 0) goto loc_0027FB1A;
    if (!sign_flag) goto loc_0027FD3C;
    if (((*(unsigned __int8 *)(v_rip + 13922714)) & (1)) != 0) goto loc_0027FD57;
loc_0027F972:
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + a2 * 4) = 0;
    goto loc_0027F869;
loc_0027F97A:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_r15 + 184))) & (15));
    if (condition_is_not_equal) goto loc_0027FB36;
    a4 = 0;
loc_0027F99A:
    v_rbx = (*(unsigned __int64 *)(gs_base + (0 + 32)) + 40000) + (48);
    if (((*(unsigned __int8 *)(v_rip + 13922651)) & (1)) != 0) goto loc_0027FAF7;
loc_0027F9B1:
    if (*(unsigned __int64 *)(v_rbx) != 0) goto loc_0027F9D9;
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_0027F869;
    result = KxWaitForLockChainValid(v_rbx, *(unsigned __int64 *)(gs_base + (0 + 32)), a1, a4);
    a4 = 0;
loc_0027F9D9:
    *(unsigned __int64 *)(v_rbx) = 0;
    result = (unsigned __int8)((*(unsigned __int64 *)(v_rbx + 8)) ^ ((unsigned __int8)(*(unsigned __int64 *)(v_rbx + 8))));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0027F869;
    result = KeWakeAddressAll(result + 8, *(unsigned __int64 *)(v_rbx + 8), a1, a4);
    goto loc_0027F869;
loc_0027F9FE:
    if ((*(unsigned __int64 *)(v_rbx + 8)) < (result + 8)) goto loc_0027F85B;
    if ((*(unsigned __int64 *)(v_rbx + 8)) > (result + 8)) goto loc_0027F85B;
    a2 = (*(unsigned __int64 *)(v_rbx + 8)) - (result + 8);
    a2 = (a2) >> (3);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2 + a2 * 1))) & (31));
    a2 = (unsigned int)((2) << ((unsigned __int8)(a1)));
    a2 = (unsigned int)(~(a2));
    result = ((unsigned int)((unsigned int)(a2 + a2 * 1))) >> (5);
    goto loc_0027F869;
loc_0027FA6C:
    a2 = (*(unsigned __int64 *)(v_stack_m20)) << (25);
    result = (0) << (25);
    a2 = (a2) - (result);
    a2 = (a2) >> (16);
    result = MiFastLockLeafPageTable(v_r15, a2, 8, a4);
    if ((unsigned int)(result) == 0) goto loc_0027F720;
    if (((unsigned int)(result)) == 3) goto loc_0027FD77;
    if ((*(unsigned __int64 *)(v_stack_m20 + result * 8)) == result) goto loc_0027FC21;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r15 + 184)))) & (15)) == 0) goto loc_0027FBC1;
loc_0027FAD5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r15 + 184)))) & (15)) != 0) goto loc_0027FC52;
loc_0027FAE4:
    goto loc_0027F720;
loc_0027FAF7:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13165403))) != 0) goto loc_0027F9B1;
    result = KiReleaseQueuedSpinLockInstrumented(v_rbx, v_stack_p28, 8, a4);
    goto loc_0027F869;
loc_0027FB1A:
    if (((*(unsigned __int8 *)(v_rip + 13922277)) & (1)) != 0) goto loc_0027FD8C;
loc_0027FB27:
    goto loc_0027F869;
loc_0027FB36:
    if (((unsigned __int8)(result)) == 7) goto loc_0027FD16;
    a1 = 72;
    if (((unsigned __int8)(result)) == 5) { a1 = 0; }
    goto loc_0027F99A;
loc_0027FB54:
    if (((*(unsigned __int64 *)(v_rip + 13922089)) & (0x600000ULL)) == 0) goto loc_0027F819;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == ((unsigned __int8)(v_rdi))) goto loc_0027F819;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_0027F819;
    a1 = (v_stack_m18) >> (3);
    a1 = (unsigned int)((a1) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (66)) == 0) { result = result; }
    goto loc_0027F819;
loc_0027FBC1:
    if (v_stack_p28 < (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) goto loc_0027FAD5;
    if (v_stack_p28 > (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) goto loc_0027FAD5;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) == 0) goto loc_0027FDAC;
    a2 = (unsigned int)((v_stack_p28) >> (3));
    a2 = (unsigned int)((a2) & (511));
    result = ExReleaseSpinLockRegardlessFromDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040) + 1384) + a2 * 4, a2, result, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288));
    goto loc_0027F720;
loc_0027FC21:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_r15 + 184))) & (15));
    if (condition_is_not_equal) goto loc_0027FCFE;
loc_0027FC3E:
    a2 = (*(unsigned __int64 *)(gs_base + (0 + 32))) + (0x9C40ULL);
    a1 = (48) + (a2);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, a2, result, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288));
    goto loc_0027F720;
loc_0027FC52:
    if (a2 < a1) goto loc_0027FAE4;
    if (a2 > a1) goto loc_0027FAE4;
    a2 = (a2) - (a1);
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) + ((unsigned int)(a2)));
    result = ((unsigned int)((unsigned int)(a2))) >> (5);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a2))) & (31));
    result = (unsigned int)((3) << ((unsigned __int8)(a1)));
    result = (unsigned int)(~(result));
    goto loc_0027F720;
loc_0027FCB2:
loc_0027FCB5:
    a3 = (unsigned __int8)((1) << ((unsigned __int8)(v_rsi - 1)));
    *(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + a4 * 1) = a3;
    if ((unsigned int)(v_rdi) != 0) goto loc_0027F822;
    if (0 != 0) goto loc_0027F7B0;
    a1 = (v_rbx) ^ (*(unsigned __int64 *)(v_stack_m28 + (int)((unsigned int)(v_rsi)) * 8 + 80));
    if (((a1) & (0xFFFFFFFFFFFFF000ULL)) != 0) goto loc_0027F7B0;
    *(unsigned __int8 *)(a4 + 1) = a3;
    goto loc_0027F6D5;
loc_0027FCFE:
    if (((unsigned __int8)((int)((unsigned int)(v_rsi)))) == 7) goto loc_0027FD23;
    a1 = 72;
    if (((unsigned __int8)((int)((unsigned int)(v_rsi)))) == 5) { a1 = 0; }
    goto loc_0027FC3E;
loc_0027FD16:
    a4 = 0;
    goto loc_0027F99A;
loc_0027FD23:
    a2 = (0) + (0x9C40ULL);
    a1 = (24) + (a2);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(a1, a2, a3, a4);
    goto loc_0027F720;
loc_0027FD3C:
    a4 = 0;
    v_stack_m50 = 0;
    result = KeBugCheckEx(a4 + 16, a1, 256, a4);
loc_0027FD57:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13164795))) != 0) goto loc_0027F972;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(a4 + 16, v_stack_p28, 256, a4);
    goto loc_0027F869;
loc_0027FD77:
    v_r11 = 0;
    goto loc_0027F744;
loc_0027FD8C:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13164742))) != 0) goto loc_0027FB27;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(a4 + 16, v_stack_p28, 256, 0);
    goto loc_0027F869;
loc_0027FDAC:
    goto loc_0027FAD5;
}
```

## 5. (Beta) C Style

```c
int64_t MiCaptureDeleteHierarchy(int64_t Arg1, int64_t Arg2, uint8_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_p28;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (112);
    Arg1 = (Arg1) >> (9);
    Arg4 = 0;
    Arg1 = (Arg1) & (Arg3);
    local_r15 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    *(uint32_t *)(arg4) = 0;
    Arg1 = (Arg1) + (local_rbp);
    *(uint64_t *)(local_rsp - 0x68) = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (Arg3);
    Arg1 = (Arg1) + (local_rbp);
    *(uint64_t *)(local_rsp - 0x60) = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (Arg3);
    Arg1 = (Arg1) + (local_rbp);
    *(uint64_t *)(local_rsp - 0x58) = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (Arg3);
    Arg1 = (Arg1) + (local_rbp);
    Arg2 = (Arg2) >> (9);
    *(uint64_t *)(local_rsp - 0x50) = Arg1;
    Arg2 = (Arg2) & (Arg3);
    Arg2 = (Arg2) + (local_rbp);
    *(uint64_t *)(local_rsp - 0x48) = Arg2;
    Arg2 = (Arg2) >> (9);
    Arg2 = (Arg2) & (Arg3);
    Arg2 = (Arg2) + (local_rbp);
    *(uint64_t *)(local_rsp - 0x40) = Arg2;
    Arg2 = (Arg2) >> (9);
    Arg2 = (Arg2) & (Arg3);
    Arg2 = (Arg2) + (local_rbp);
    *(uint64_t *)(local_rsp - 0x38) = Arg2;
    Arg2 = (Arg2) >> (9);
    Arg2 = (Arg2) & (Arg3);
    Arg2 = (Arg2) + (local_rbp);
    *(uint64_t *)(local_rsp - 0x30) = Arg2;
loc_0027F6D0:
    if (0 < 2) goto loc_0027F6F4;
loc_0027F6D5:
    return local_rbp;
loc_0027F6F4:
    result = (0) << (5);
    local_r14 = (v_stack_m40) + (result);
loc_0027F707:
    if (3 < 1) goto loc_0027F87E;
    if (3 == 3) goto loc_0027FA6C;
loc_0027F720:
    result = 0;
    result = MiMakeSystemAddressValid(*(uint64_t *)(local_r14 + (int32_t)(3) * 8), 0, Arg3, 8);
    local_r11 = 0;
    if (sign_flag) goto loc_0027FCB2;
loc_0027F744:
    Arg2 = (*(uint64_t *)(local_r14 + (int32_t)(3) * 8)) >> (9);
    Arg2 = (Arg2) & (result);
    Arg2 = (Arg2) + (*(uint64_t *)(v_stack_m28 + 0x38));
    if ((*(uint64_t *)(local_r14 + (int32_t)(3) * 8)) < result) goto loc_0027F7A0;
    if ((*(uint64_t *)(local_r14 + (int32_t)(3) * 8)) > result) goto loc_0027F7A0;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_r14 + (int32_t)(3) * 8)))) & (1)) == 0) goto loc_0027F7A0;
    Arg3 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_r14 + (int32_t)(3) * 8)))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_r14 + (int32_t)(3) * 8)))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & (Arg3)) == 0) goto loc_0027F885;
loc_0027F7A0:
    if (*(uint64_t *)(*(uint64_t *)(local_r14 + (int32_t)(3) * 8)) == 0) goto loc_0027FCB5;
    if (0 != 0) goto loc_0027F822;
loc_0027F7B0:
    if (3 != 1) goto loc_0027F822;
    result = (v_stack_m18) ^ (*(uint64_t *)(local_r14 + (int32_t)(3) * 8));
    if (((result) & (0xFFFFFFFFFFFFF000ULL)) != 0) goto loc_0027F822;
    if (sign_flag) goto loc_0027F81E;
    if (v_stack_m18 < (*(uint64_t *)(*(uint64_t *)(local_r14 + (int32_t)(3) * 8)))) goto loc_0027F819;
    if (v_stack_m18 > (*(uint64_t *)(*(uint64_t *)(local_r14 + (int32_t)(3) * 8)))) goto loc_0027F819;
    if (((3) & ((uint8_t)(*(uint64_t *)(v_stack_m18)))) == 0) goto loc_0027F819;
    Arg3 = ((((uint8_t)(*(uint64_t *)(v_stack_m18))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(v_stack_m18))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & (Arg3)) == 0) goto loc_0027FB54;
loc_0027F819:
    if (*(uint64_t *)(v_stack_m18) == 0) {
        *(uint8_t *)(arg4 + 0x1) = 3;
    }
    if (Arg2 == 0) goto loc_0027F869;
    if (Arg2 == (*(uint64_t *)(v_stack_m18))) goto loc_0027F97A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r15 + 0xB8)))) & (15)) == 0) goto loc_0027F8EE;
loc_0027F84C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r15 + 0xB8)))) & (15)) != 0) goto loc_0027F9FE;
loc_0027F85B:
loc_0027F869:
    if (0 != 0) goto loc_0027F87E;
    local_rsi = (uint32_t)((3) - 1);
    goto loc_0027F707;
loc_0027F87E:
    local_rdi = (uint32_t)((3) + 1);
    goto loc_0027F6D0;
loc_0027F885:
    if (((*(uint64_t *)(v_rip + 0xD471F8)) & (0x600000ULL)) == 0) goto loc_0027F7A0;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_0027F7A0;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_0027F7A0;
    result = (*(uint64_t *)(local_r14 + (int32_t)(3) * 8)) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (32)) != 0) {
        Arg1 = (Arg1) | (32);
    }
    Arg1 = (Arg1) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) & (66)) == 0) { Arg1 = Arg1; }
    goto loc_0027F7A0;
loc_0027F8EE:
    if (Arg2 < (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) goto loc_0027F84C;
    if (Arg2 > (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + result * 8))) goto loc_0027F84C;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_0027F84C;
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) & (511));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + Arg2 * 4)))) & (0x3FFFFFFFULL)) != 0) goto loc_0027FB1A;
    if (!sign_flag) goto loc_0027FD3C;
    if (((*(uint8_t *)(v_rip + 0xD4719A)) & (1)) != 0) goto loc_0027FD57;
loc_0027F972:
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + Arg2 * 4) = 0;
    goto loc_0027F869;
loc_0027F97A:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_0027FB36;
    Arg4 = 0;
loc_0027F99A:
    local_rbx = (*(uint64_t *)(gs_base + (0 + 0x20)) + 40000) + (48);
    if (((*(uint8_t *)(v_rip + 0xD4715B)) & (1)) != 0) goto loc_0027FAF7;
loc_0027F9B1:
    if (*(uint64_t *)(local_rbx) != 0) goto loc_0027F9D9;
    if (*(uint64_t *)(local_rbx) == 0) goto loc_0027F869;
    result = KxWaitForLockChainValid(local_rbx, *(uint64_t *)(gs_base + (0 + 0x20)), Arg1, Arg4);
    Arg4 = 0;
loc_0027F9D9:
    *(uint64_t *)(local_rbx) = 0;
    result = (uint8_t)((*(uint64_t *)(local_rbx + 0x8)) ^ ((uint8_t)(*(uint64_t *)(local_rbx + 0x8))));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0027F869;
    result = KeWakeAddressAll(result + 8, *(uint64_t *)(local_rbx + 0x8), Arg1, Arg4);
    goto loc_0027F869;
loc_0027F9FE:
    if ((*(uint64_t *)(local_rbx + 0x8)) < (result + 8)) goto loc_0027F85B;
    if ((*(uint64_t *)(local_rbx + 0x8)) > (result + 8)) goto loc_0027F85B;
    Arg2 = (*(uint64_t *)(local_rbx + 0x8)) - (result + 8);
    Arg2 = (Arg2) >> (3);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2 + Arg2 * 1))) & (31));
    Arg2 = (uint32_t)((2) << ((uint8_t)(Arg1)));
    Arg2 = (uint32_t)(~(Arg2));
    result = ((uint32_t)((uint32_t)(Arg2 + Arg2 * 1))) >> (5);
    goto loc_0027F869;
loc_0027FA6C:
    Arg2 = (*(uint64_t *)(v_stack_m20)) << (25);
    result = (0) << (25);
    Arg2 = (Arg2) - (result);
    Arg2 = (Arg2) >> (16);
    result = MiFastLockLeafPageTable(local_r15, Arg2, 8, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0027F720;
    if (((uint32_t)(result)) == 3) goto loc_0027FD77;
    if ((*(uint64_t *)(v_stack_m20 + result * 8)) == result) goto loc_0027FC21;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r15 + 0xB8)))) & (15)) == 0) goto loc_0027FBC1;
loc_0027FAD5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r15 + 0xB8)))) & (15)) != 0) goto loc_0027FC52;
loc_0027FAE4:
    goto loc_0027F720;
loc_0027FAF7:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8E35B))) != 0) goto loc_0027F9B1;
    result = KiReleaseQueuedSpinLockInstrumented(local_rbx, v_stack_p28, 8, Arg4);
    goto loc_0027F869;
loc_0027FB1A:
    if (((*(uint8_t *)(v_rip + 0xD46FE5)) & (1)) != 0) goto loc_0027FD8C;
loc_0027FB27:
    goto loc_0027F869;
loc_0027FB36:
    if (((uint8_t)(result)) == 7) goto loc_0027FD16;
    Arg1 = 72;
    if (((uint8_t)(result)) == 5) { Arg1 = 0; }
    goto loc_0027F99A;
loc_0027FB54:
    if (((*(uint64_t *)(v_rip + 0xD46F29)) & (0x600000ULL)) == 0) goto loc_0027F819;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == ((uint8_t)(local_rdi))) goto loc_0027F819;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_0027F819;
    Arg1 = (v_stack_m18) >> (3);
    Arg1 = (uint32_t)((Arg1) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg1 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg1 * 8))) & (66)) == 0) { result = result; }
    goto loc_0027F819;
loc_0027FBC1:
    if (v_stack_p28 < (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg1 * 8))) goto loc_0027FAD5;
    if (v_stack_p28 > (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg1 * 8))) goto loc_0027FAD5;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) == 0) goto loc_0027FDAC;
    Arg2 = (uint32_t)((v_stack_p28) >> (3));
    Arg2 = (uint32_t)((Arg2) & (511));
    result = ExReleaseSpinLockRegardlessFromDpcLevel(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410) + 0x568) + Arg2 * 4, Arg2, result, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508));
    goto loc_0027F720;
loc_0027FC21:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0xB8))) & (15));
    if (condition_is_not_equal) goto loc_0027FCFE;
loc_0027FC3E:
    Arg2 = (*(uint64_t *)(gs_base + (0 + 0x20))) + (0x9C40ULL);
    Arg1 = (48) + (Arg2);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(Arg1, Arg2, result, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508));
    goto loc_0027F720;
loc_0027FC52:
    if (Arg2 < Arg1) goto loc_0027FAE4;
    if (Arg2 > Arg1) goto loc_0027FAE4;
    Arg2 = (Arg2) - (Arg1);
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg2)));
    result = ((uint32_t)((uint32_t)(Arg2))) >> (5);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) & (31));
    result = (uint32_t)((3) << ((uint8_t)(Arg1)));
    result = (uint32_t)(~(result));
    goto loc_0027F720;
loc_0027FCB2:
loc_0027FCB5:
    Arg3 = (uint8_t)((1) << ((uint8_t)(local_rsi - 1)));
    *(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + arg4 * 1) = Arg3;
    if ((uint32_t)(local_rdi) != 0) goto loc_0027F822;
    if (0 != 0) goto loc_0027F7B0;
    Arg1 = (local_rbx) ^ (*(uint64_t *)(v_stack_m28 + (int32_t)((uint32_t)(local_rsi)) * 8 + 0x50));
    if (((Arg1) & (0xFFFFFFFFFFFFF000ULL)) != 0) goto loc_0027F7B0;
    *(uint8_t *)(arg4 + 0x1) = Arg3;
    goto loc_0027F6D5;
loc_0027FCFE:
    if (((uint8_t)((int32_t)((uint32_t)(local_rsi)))) == 7) goto loc_0027FD23;
    Arg1 = 72;
    if (((uint8_t)((int32_t)((uint32_t)(local_rsi)))) == 5) { Arg1 = 0; }
    goto loc_0027FC3E;
loc_0027FD16:
    Arg4 = 0;
    goto loc_0027F99A;
loc_0027FD23:
    Arg2 = (0) + (0x9C40ULL);
    Arg1 = (24) + (Arg2);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(Arg1, Arg2, Arg3, Arg4);
    goto loc_0027F720;
loc_0027FD3C:
    Arg4 = 0;
    v_stack_m50 = 0;
    result = KeBugCheckEx(Arg4 + 16, Arg1, 256, Arg4);
loc_0027FD57:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8E0FB))) != 0) goto loc_0027F972;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(Arg4 + 16, v_stack_p28, 256, Arg4);
    goto loc_0027F869;
loc_0027FD77:
    local_r11 = 0;
    goto loc_0027F744;
loc_0027FD8C:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8E0C6))) != 0) goto loc_0027FB27;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(Arg4 + 16, v_stack_p28, 256, 0);
    goto loc_0027F869;
loc_0027FDAC:
    goto loc_0027FAD5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `32` | `W` |
| `Arg4` | `+ 0x1` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0027F5F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
