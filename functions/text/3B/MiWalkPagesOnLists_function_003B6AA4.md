# MiWalkPagesOnLists

- RVA: `0x003B6AA4`–`0x003B6F71` (길이 `1,229` bytes)
- VA: `0x00000001403B6AA4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008C778`
- 디코드: `278`개 명령, `1,229/1,229` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003B6B1B` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003B6B24` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x003B6B6E` → [MiMirrorAddPagesToBrownList](MiMirrorAddPagesToBrownList_function_003B648C.md) (function, `0x003B648C`)
- `0x003B6B9E` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x003B6BB3` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003B6C23` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003B6C37` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x003B6C79` → [MiMirrorAddPagesToBrownList](MiMirrorAddPagesToBrownList_function_003B648C.md) (function, `0x003B648C`)
- `0x003B6CA0` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x003B6CB5` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003B6D05` → [MiUpdateLargePageCandidateValue](../33/MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x003B6D23` → [MiUpdateLargePageCandidateValue](../33/MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x003B6D89` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x003B6E07` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x003B6E1F` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003B6E79` → [MiMirrorAddPagesToBrownList](MiMirrorAddPagesToBrownList_function_003B648C.md) (function, `0x003B648C`)
- `0x003B6E90` → [MiIsDecayPfn](../2B/MiIsDecayPfn_function_002B9240.md) (function, `0x002B9240`)
- `0x003B6ED6` → [MiUpdateLargePageCandidateValue](../33/MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x003B6EE3` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003B6EF6` → [MiMirrorNodeFreeZeroPages](../4F/MiMirrorNodeFreeZeroPages_function_004FC8CC.md) (function, `0x004FC8CC`)

### Direct callers
- [MiCreatePfnBitMaps](../../page/80/MiCreatePfnBitMaps_function_0080BBC8.md) at `0x0080BFEB`
- [MiMirrorBrownPhase](../../pagelk/B7/MiMirrorBrownPhase_function_00B7C6B4.md) at `0x00B7C783`

### Static image references
- `0x003B6B0C` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003B6E99` → RVA `0x00E2DC80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x003B6EA7` → [sub_006E753C](../6E/Unknown_function_006E753C.md) (`tail-transfer`)
  - `0x003B6EB0` → [sub_006E753C](../6E/Unknown_function_006E753C.md) (`tail-transfer`)
  - `0x003B6EBC` → [sub_006E753C](../6E/Unknown_function_006E753C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003B6AA4  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003B6AA9  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
003B6AAE  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
003B6AB3  55                              push rbp
003B6AB4  56                              push rsi
003B6AB5  57                              push rdi
003B6AB6  41 54                           push r12
003B6AB8  41 55                           push r13
003B6ABA  41 56                           push r14
003B6ABC  41 57                           push r15
003B6ABE  48 83 EC 50                     sub rsp, 0x50
003B6AC2  BD 02 00 00 00                  mov ebp, 2
003B6AC7  49 63 D8                        movsxd rbx, r8d
003B6ACA  45 33 ED                        xor r13d, r13d
003B6ACD  4C 8B FA                        mov r15, rdx
003B6AD0  4C 8B E1                        mov r12, rcx
003B6AD3  48 BF FF FF FF FF 3F 00 00 00   movabs rdi, 0x3fffffffff
003B6ADD  44 8D 75 0E                     lea r14d, [rbp + 0xe]
003B6AE1  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
003B6AE6  48 83 FB 04                     cmp rbx, 4
003B6AEA  0F 8E 3D 02 00 00               jle 0x1403b6d2d
003B6AF0  49 8D 9F 90 10 00 00            lea rbx, [r15 + 0x1090]
003B6AF7  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
003B6AFF  44 0F 20 C6                     mov rsi, cr8
003B6B03  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
003B6B08  44 0F 22 C5                     mov cr8, rbp
003B6B0C  44 39 2D 0D 02 C1 00            cmp dword ptr [rip + 0xc1020d], r13d
003B6B13  74 0B                           je 0x1403b6b20
003B6B15  40 8A D5                        mov dl, bpl
003B6B18  40 8A CE                        mov cl, sil
003B6B1B  E8 DC EB 13 00                  call 0x1404f56fc
003B6B20  48 8D 4B 10                     lea rcx, [rbx + 0x10]
003B6B24  E8 57 23 E9 FF                  call 0x140248e80
003B6B29  48 8B 0B                        mov rcx, qword ptr [rbx]
003B6B2C  48 3B CF                        cmp rcx, rdi
003B6B2F  74 69                           je 0x1403b6b9a
003B6B31  BE 01 00 00 00                  mov esi, 1
003B6B36  48 BB FF FF FF FF FF 00 00 00   movabs rbx, 0xffffffffff
003B6B40  49 BE FF FF FF FF 3F 00 00 00   movabs r14, 0x3fffffffff
003B6B4A  48 8D 3C 49                     lea rdi, [rcx + rcx*2]
003B6B4E  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003B6B58  48 C1 E7 04                     shl rdi, 4
003B6B5C  48 8B C0                        mov rax, rax
003B6B5F  48 03 F8                        add rdi, rax
003B6B62  4D 85 E4                        test r12, r12
003B6B65  0F 84 86 01 00 00               je 0x1403b6cf1
003B6B6B  48 8B D6                        mov rdx, rsi
003B6B6E  E8 19 F9 FF FF                  call 0x1403b648c
003B6B73  48 8B 0F                        mov rcx, qword ptr [rdi]
003B6B76  48 23 CB                        and rcx, rbx
003B6B79  49 3B CE                        cmp rcx, r14
003B6B7C  75 CC                           jne 0x1403b6b4a
003B6B7E  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
003B6B86  48 BF FF FF FF FF 3F 00 00 00   movabs rdi, 0x3fffffffff
003B6B90  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
003B6B95  4C 8B 74 24 30                  mov r14, qword ptr [rsp + 0x30]
003B6B9A  48 8D 4B 10                     lea rcx, [rbx + 0x10]
003B6B9E  E8 3D 2C E9 FF                  call 0x1402497e0
003B6BA3  44 39 2D 76 01 C1 00            cmp dword ptr [rip + 0xc10176], r13d
003B6BAA  74 0C                           je 0x1403b6bb8
003B6BAC  44 0F 20 C1                     mov rcx, cr8
003B6BB0  40 8A D6                        mov dl, sil
003B6BB3  E8 E0 EA 13 00                  call 0x1404f5698
003B6BB8  40 0F B6 C6                     movzx eax, sil
003B6BBC  44 0F 22 C0                     mov cr8, rax
003B6BC0  48 83 C3 58                     add rbx, 0x58
003B6BC4  49 83 EE 01                     sub r14, 1
003B6BC8  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
003B6BD0  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
003B6BD5  0F 85 24 FF FF FF               jne 0x1403b6aff
003B6BDB  41 8B FD                        mov edi, r13d
003B6BDE  44 89 AC 24 A8 00 00 00         mov dword ptr [rsp + 0xa8], r13d
003B6BE6  49 BE FF FF FF FF 3F 00 00 00   movabs r14, 0x3fffffffff
003B6BF0  8B C7                           mov eax, edi
003B6BF2  F7 D8                           neg eax
003B6BF4  48 1B DB                        sbb rbx, rbx
003B6BF7  81 E3 80 00 00 00               and ebx, 0x80
003B6BFD  48 81 C3 80 0F 00 00            add rbx, 0xf80
003B6C04  44 0F 20 C6                     mov rsi, cr8
003B6C08  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
003B6C10  44 0F 22 C5                     mov cr8, rbp
003B6C14  44 39 2D 05 01 C1 00            cmp dword ptr [rip + 0xc10105], r13d
003B6C1B  74 0B                           je 0x1403b6c28
003B6C1D  40 8A D5                        mov dl, bpl
003B6C20  40 8A CE                        mov cl, sil
003B6C23  E8 D4 EA 13 00                  call 0x1404f56fc
003B6C28  49 8D 6F 20                     lea rbp, [r15 + 0x20]
003B6C2C  48 03 EB                        add rbp, rbx
003B6C2F  48 8B CD                        mov rcx, rbp
003B6C32  48 89 6C 24 48                  mov qword ptr [rsp + 0x48], rbp
003B6C37  E8 44 22 E9 FF                  call 0x140248e80
003B6C3C  4A 8B 4C 3B 10                  mov rcx, qword ptr [rbx + r15 + 0x10]
003B6C41  49 3B CE                        cmp rcx, r14
003B6C44  74 57                           je 0x1403b6c9d
003B6C46  BE 01 00 00 00                  mov esi, 1
003B6C4B  48 BF 00 00 00 00 00 DE FF FF   movabs rdi, 0xffffde0000000000
003B6C55  48 BD FF FF FF FF FF 00 00 00   movabs rbp, 0xffffffffff
003B6C5F  48 8D 1C 49                     lea rbx, [rcx + rcx*2]
003B6C63  48 C1 E3 04                     shl rbx, 4
003B6C67  48 8B C7                        mov rax, rdi
003B6C6A  48 03 D8                        add rbx, rax
003B6C6D  4D 85 E4                        test r12, r12
003B6C70  0F 84 99 00 00 00               je 0x1403b6d0f
003B6C76  48 8B D6                        mov rdx, rsi
003B6C79  E8 0E F8 FF FF                  call 0x1403b648c
003B6C7E  48 8B 0B                        mov rcx, qword ptr [rbx]
003B6C81  48 23 CD                        and rcx, rbp
003B6C84  49 3B CE                        cmp rcx, r14
003B6C87  75 D6                           jne 0x1403b6c5f
003B6C89  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
003B6C90  48 8B B4 24 90 00 00 00         mov rsi, qword ptr [rsp + 0x90]
003B6C98  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
003B6C9D  48 8B CD                        mov rcx, rbp
003B6CA0  E8 3B 2B E9 FF                  call 0x1402497e0
003B6CA5  44 39 2D 74 00 C1 00            cmp dword ptr [rip + 0xc10074], r13d
003B6CAC  74 0C                           je 0x1403b6cba
003B6CAE  44 0F 20 C1                     mov rcx, cr8
003B6CB2  40 8A D6                        mov dl, sil
003B6CB5  E8 DE E9 13 00                  call 0x1404f5698
003B6CBA  40 0F B6 C6                     movzx eax, sil
003B6CBE  44 0F 22 C0                     mov cr8, rax
003B6CC2  FF C7                           inc edi
003B6CC4  BD 02 00 00 00                  mov ebp, 2
003B6CC9  89 BC 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], edi
003B6CD0  3B FD                           cmp edi, ebp
003B6CD2  0F 82 18 FF FF FF               jb 0x1403b6bf0
003B6CD8  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
003B6CE0  48 83 C4 50                     add rsp, 0x50
003B6CE4  41 5F                           pop r15
003B6CE6  41 5E                           pop r14
003B6CE8  41 5D                           pop r13
003B6CEA  41 5C                           pop r12
003B6CEC  5F                              pop rdi
003B6CED  5E                              pop rsi
003B6CEE  5D                              pop rbp
003B6CEF  C3                              ret
003B6CF0  CC                              int3
003B6CF1  41 B9 03 00 00 00               mov r9d, 3
003B6CF7  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
003B6CFC  48 8B D1                        mov rdx, rcx
003B6CFF  45 8B C1                        mov r8d, r9d
003B6D02  49 8B CF                        mov rcx, r15
003B6D05  E8 76 82 F8 FF                  call 0x14033ef80
003B6D0A  E9 64 FE FF FF                  jmp 0x1403b6b73
003B6D0F  41 B9 03 00 00 00               mov r9d, 3
003B6D15  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
003B6D1A  48 8B D1                        mov rdx, rcx
003B6D1D  45 8B C1                        mov r8d, r9d
003B6D20  49 8B CF                        mov rcx, r15
003B6D23  E8 58 82 F8 FF                  call 0x14033ef80
003B6D28  E9 51 FF FF FF                  jmp 0x1403b6c7e
003B6D2D  8B B4 24 B0 00 00 00            mov esi, dword ptr [rsp + 0xb0]
003B6D34  B8 01 00 00 00                  mov eax, 1
003B6D39  49 8B BC DF E0 1B 00 00         mov rdi, qword ptr [r15 + rbx*8 + 0x1be0]
003B6D41  48 3B D8                        cmp rbx, rax
003B6D44  0F 8E A3 01 00 00               jle 0x1403b6eed
003B6D4A  48 3B DD                        cmp rbx, rbp
003B6D4D  0F 85 B0 01 00 00               jne 0x1403b6f03
003B6D53  8B C6                           mov eax, esi
003B6D55  48 6B F8 58                     imul rdi, rax, 0x58
003B6D59  48 81 C7 C0 0C 00 00            add rdi, 0xcc0
003B6D60  49 03 FF                        add rdi, r15
003B6D63  45 0F 20 C4                     mov r12, cr8
003B6D67  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
003B6D6C  44 0F 22 C5                     mov cr8, rbp
003B6D70  44 39 2D A9 FF C0 00            cmp dword ptr [rip + 0xc0ffa9], r13d
003B6D77  0F 85 60 01 00 00               jne 0x1403b6edd
003B6D7D  4C 8D 6F 20                     lea r13, [rdi + 0x20]
003B6D81  49 8B CD                        mov rcx, r13
003B6D84  4C 89 6C 24 48                  mov qword ptr [rsp + 0x48], r13
003B6D89  E8 F2 20 E9 FF                  call 0x140248e80
003B6D8E  48 8B 7F 10                     mov rdi, qword ptr [rdi + 0x10]
003B6D92  49 B8 FF FF FF FF 3F 00 00 00   movabs r8, 0x3fffffffff
003B6D9C  49 3B F8                        cmp rdi, r8
003B6D9F  74 63                           je 0x1403b6e04
003B6DA1  4C 8B A4 24 90 00 00 00         mov r12, qword ptr [rsp + 0x90]
003B6DA9  48 BE FF FF FF FF FF 00 00 00   movabs rsi, 0xffffffffff
003B6DB3  41 BD 01 00 00 00               mov r13d, 1
003B6DB9  48 8D 2C 7F                     lea rbp, [rdi + rdi*2]
003B6DBD  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003B6DC7  48 C1 E5 04                     shl rbp, 4
003B6DCB  48 8B C0                        mov rax, rax
003B6DCE  48 03 E8                        add rbp, rax
003B6DD1  48 89 6C 24 38                  mov qword ptr [rsp + 0x38], rbp
003B6DD6  48 0F BA 65 28 35               bt qword ptr [rbp + 0x28], 0x35
003B6DDC  0F 83 86 00 00 00               jae 0x1403b6e68
003B6DE2  48 8B 7D 00                     mov rdi, qword ptr [rbp]
003B6DE6  48 23 FE                        and rdi, rsi
003B6DE9  49 3B F8                        cmp rdi, r8
003B6DEC  75 CB                           jne 0x1403b6db9
003B6DEE  8B B4 24 B0 00 00 00            mov esi, dword ptr [rsp + 0xb0]
003B6DF5  BD 02 00 00 00                  mov ebp, 2
003B6DFA  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
003B6DFF  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
003B6E04  49 8B CD                        mov rcx, r13
003B6E07  E8 D4 29 E9 FF                  call 0x1402497e0
003B6E0C  45 33 ED                        xor r13d, r13d
003B6E0F  44 39 2D 0A FF C0 00            cmp dword ptr [rip + 0xc0ff0a], r13d
003B6E16  74 0C                           je 0x1403b6e24
003B6E18  44 0F 20 C1                     mov rcx, cr8
003B6E1C  41 8A D4                        mov dl, r12b
003B6E1F  E8 74 E8 13 00                  call 0x1404f5698
003B6E24  41 0F B6 C4                     movzx eax, r12b
003B6E28  44 0F 22 C0                     mov cr8, rax
003B6E2C  48 3B DD                        cmp rbx, rbp
003B6E2F  0F 84 F7 00 00 00               je 0x1403b6f2c
003B6E35  48 83 FB 03                     cmp rbx, 3
003B6E39  0F 84 0E 01 00 00               je 0x1403b6f4d
003B6E3F  4C 8B A4 24 90 00 00 00         mov r12, qword ptr [rsp + 0x90]
003B6E47  B8 01 00 00 00                  mov eax, 1
003B6E4C  48 03 D8                        add rbx, rax
003B6E4F  48 83 FB 04                     cmp rbx, 4
003B6E53  0F 8E E0 FE FF FF               jle 0x1403b6d39
003B6E59  48 BF FF FF FF FF 3F 00 00 00   movabs rdi, 0x3fffffffff
003B6E63  E9 88 FC FF FF                  jmp 0x1403b6af0
003B6E68  48 83 FB 02                     cmp rbx, 2
003B6E6C  74 1F                           je 0x1403b6e8d
003B6E6E  4D 85 E4                        test r12, r12
003B6E71  74 4E                           je 0x1403b6ec1
003B6E73  49 8B D5                        mov rdx, r13
003B6E76  48 8B CF                        mov rcx, rdi
003B6E79  E8 0E F6 FF FF                  call 0x1403b648c
003B6E7E  49 B8 FF FF FF FF 3F 00 00 00   movabs r8, 0x3fffffffff
003B6E88  E9 55 FF FF FF                  jmp 0x1403b6de2
003B6E8D  48 8B CF                        mov rcx, rdi
003B6E90  E8 AB 23 F0 FF                  call 0x1402b9240
003B6E95  85 C0                           test eax, eax
003B6E97  74 D5                           je 0x1403b6e6e
003B6E99  48 8B 05 E0 6D A7 00            mov rax, qword ptr [rip + 0xa76de0]
003B6EA0  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
003B6EA4  48 85 C0                        test rax, rax
003B6EA7  0F 84 8F 06 33 00               je 0x1406e753c
003B6EAD  41 84 CE                        test r14b, cl
003B6EB0  0F 85 86 06 33 00               jne 0x1406e753c
003B6EB6  48 F7 D0                        not rax
003B6EB9  48 23 C8                        and rcx, rax
003B6EBC  E9 7B 06 33 00                  jmp 0x1406e753c
003B6EC1  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
003B6EC7  41 B9 03 00 00 00               mov r9d, 3
003B6ECD  45 8B C1                        mov r8d, r9d
003B6ED0  48 8B D7                        mov rdx, rdi
003B6ED3  49 8B CF                        mov rcx, r15
003B6ED6  E8 A5 80 F8 FF                  call 0x14033ef80
003B6EDB  EB A1                           jmp 0x1403b6e7e
003B6EDD  40 8A D5                        mov dl, bpl
003B6EE0  41 8A CC                        mov cl, r12b
003B6EE3  E8 14 E8 13 00                  call 0x1404f56fc
003B6EE8  E9 90 FE FF FF                  jmp 0x1403b6d7d
003B6EED  45 33 C0                        xor r8d, r8d
003B6EF0  49 8B D7                        mov rdx, r15
003B6EF3  49 8B CC                        mov rcx, r12
003B6EF6  E8 D1 59 14 00                  call 0x1404fc8cc
003B6EFB  48 8B DD                        mov rbx, rbp
003B6EFE  E9 31 FE FF FF                  jmp 0x1403b6d34
003B6F03  48 83 FB 03                     cmp rbx, 3
003B6F07  0F 85 56 FE FF FF               jne 0x1403b6d63
003B6F0D  48 8B 07                        mov rax, qword ptr [rdi]
003B6F10  49 3B 87 A0 4C 00 00            cmp rax, qword ptr [r15 + 0x4ca0]
003B6F17  0F 84 2A FF FF FF               je 0x1403b6e47
003B6F1D  8B C6                           mov eax, esi
003B6F1F  48 83 C0 40                     add rax, 0x40
003B6F23  48 6B F8 58                     imul rdi, rax, 0x58
003B6F27  E9 34 FE FF FF                  jmp 0x1403b6d60
003B6F2C  83 FE 07                        cmp esi, 7
003B6F2F  8D 46 01                        lea eax, [rsi + 1]
003B6F32  B9 01 00 00 00                  mov ecx, 1
003B6F37  41 0F 44 C5                     cmove eax, r13d
003B6F3B  48 0F 45 D9                     cmovne rbx, rcx
003B6F3F  8B F0                           mov esi, eax
003B6F41  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
003B6F48  E9 F2 FE FF FF                  jmp 0x1403b6e3f
003B6F4D  FF C6                           inc esi
003B6F4F  89 B4 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], esi
003B6F56  41 3B F6                        cmp esi, r14d
003B6F59  0F 84 E0 FE FF FF               je 0x1403b6e3f
003B6F5F  4C 8B A4 24 90 00 00 00         mov r12, qword ptr [rsp + 0x90]
003B6F67  BB 03 00 00 00                  mov ebx, 3
003B6F6C  E9 C3 FD FF FF                  jmp 0x1403b6d34
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWalkPagesOnLists(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p90;
    unsigned int v_stack_pB0;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (80);
    v_r13 = 0;
    v_stack_m58 = 2 + 14;
    if (((int)(a3)) <= 4) goto loc_003B6D2D;
loc_003B6AF0:
    v_stack_p8 = a2 + 4240;
loc_003B6AFF:
    v_stack_m40 = v_cr8;
    if ((*(unsigned int *)(v_rip + 12648973)) != 0) {
        a2 = 2;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(a2 + 4240 + 16, a2, a3, a4);
    if ((*(unsigned __int64 *)(a2 + 4240)) == v_rdi) goto loc_003B6B9A;
loc_003B6B4A:
    v_rdi = (*(unsigned __int64 *)(a2 + 4240) + *(unsigned __int64 *)(a2 + 4240) * 2) << (4);
    v_rdi = (v_rdi) + (result);
    if (a1 == 0) goto loc_003B6CF1;
    result = MiMirrorAddPagesToBrownList(*(unsigned __int64 *)(a2 + 4240), 1, a3, a4);
loc_003B6B73:
    a1 = (*(unsigned __int64 *)(v_rdi)) & (a2 + 4240);
    if (a1 != (2 + 14)) goto loc_003B6B4A;
loc_003B6B9A:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_p8 + 16, 1, a3, a4);
    if ((*(unsigned int *)(v_rip + 12648822)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_m40);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rbx = (v_stack_p8) + (88);
    v_r14 = (v_stack_m58) - (1);
    v_stack_p8 = v_rbx;
    v_stack_m58 = v_r14;
    if (condition_is_not_equal) goto loc_003B6AFF;
    v_stack_p20 = 0;
loc_003B6BF0:
    result = (unsigned int)(-(0));
    v_rbx = (unsigned int)((v_rbx) & (128));
    v_rbx = (v_rbx) + (0xF80ULL);
    v_stack_p8 = (unsigned __int8)(v_stack_m40);
    if ((*(unsigned int *)(v_rip + 12648709)) != 0) {
        a2 = 2;
        a1 = (unsigned __int8)((unsigned __int8)(v_stack_m40));
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rbp = (a2 + 32) + (v_rbx);
    v_stack_m40 = v_rbp;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rbp, a2, a3, a4);
    if ((*(unsigned __int64 *)(v_rbx + a2 * 1 + 16)) == v_r14) goto loc_003B6C9D;
loc_003B6C5F:
    v_rbx = (*(unsigned __int64 *)(v_rbx + a2 * 1 + 16) + *(unsigned __int64 *)(v_rbx + a2 * 1 + 16) * 2) << (4);
    v_rbx = (v_rbx) + (0);
    if (a1 == 0) goto loc_003B6D0F;
    result = MiMirrorAddPagesToBrownList(*(unsigned __int64 *)(v_rbx + a2 * 1 + 16), 1, a3, a4);
loc_003B6C7E:
    a1 = (*(unsigned __int64 *)(v_rbx)) & (v_rbp);
    if (a1 != v_r14) goto loc_003B6C5F;
loc_003B6C9D:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_m40, 1, a3, a4);
    if ((*(unsigned int *)(v_rip + 12648564)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_p8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rdi = (unsigned int)(((unsigned int)(v_stack_p20)) + 1);
    v_stack_p20 = (unsigned int)(v_rdi);
    if (((unsigned int)(v_rdi)) < 2) goto loc_003B6BF0;
    v_rsp = (v_rsp) + (80);
    return (unsigned __int8)(v_stack_p8);
loc_003B6CF1:
    v_stack_p20 = 0;
    result = MiUpdateLargePageCandidateValue(a2, a1, 3, 3);
    goto loc_003B6B73;
loc_003B6D0F:
    v_stack_p20 = 0;
    result = MiUpdateLargePageCandidateValue(a2, a2, 3, 3);
    goto loc_003B6C7E;
loc_003B6D2D:
loc_003B6D34:
loc_003B6D39:
    if (v_stack_p10 <= 1) goto loc_003B6EED;
    if (v_stack_p10 != 2) goto loc_003B6F03;
    v_rdi = (*(unsigned __int64 *)(a2 + v_stack_p10 * 8 + 7136)) * ((unsigned int)((unsigned int)((unsigned int)(a5))));
    v_rdi = (v_rdi) + (0xCC0ULL);
loc_003B6D60:
    v_rdi = (v_rdi) + (a2);
loc_003B6D63:
    v_stack_p40 = (unsigned __int8)(v_stack_p8);
    if ((*(unsigned int *)(v_rip + 12648361)) != 0) goto loc_003B6EDD;
loc_003B6D7D:
    v_stack_p48 = v_rdi + 32;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rdi + 32, a2, 3, 3);
    if ((*(unsigned __int64 *)(v_rdi + 16)) == 3) goto loc_003B6E04;
loc_003B6DB9:
    v_rbp = (*(unsigned __int64 *)(v_rdi + 16) + *(unsigned __int64 *)(v_rdi + 16) * 2) << (4);
    v_rbp = (v_rbp) + (result);
    v_stack_p38 = v_rbp;
    if (condition_is_above_or_equal) goto loc_003B6E68;
loc_003B6DE2:
    v_rdi = (*(unsigned __int64 *)(v_rbp)) & ((unsigned int)(a5));
    if (v_rdi != 3) goto loc_003B6DB9;
loc_003B6E04:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_p48, a2, 3, 3);
    v_r13 = 0;
    if ((*(unsigned int *)(v_rip + 12648202)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_p40);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 3, 3);
    }
    if (v_stack_p10 == 2) goto loc_003B6F2C;
    if (v_stack_p10 == 3) goto loc_003B6F4D;
loc_003B6E3F:
loc_003B6E47:
    v_rbx = (v_stack_p10) + (1);
    if (v_rbx <= 4) goto loc_003B6D39;
    goto loc_003B6AF0;
loc_003B6E68:
    if (v_rbx == 2) goto loc_003B6E8D;
loc_003B6E6E:
    if (v_stack_p90 == 0) goto loc_003B6EC1;
    result = MiMirrorAddPagesToBrownList(v_rdi, 0, 3, 3);
loc_003B6E7E:
    goto loc_003B6DE2;
loc_003B6E8D:
    result = MiIsDecayPfn(v_rdi, 0, 3, 3);
    if ((unsigned int)(result) == 0) goto loc_003B6E6E;
    result = ~(*(unsigned __int64 *)(v_rip + 10972640));
    a1 = (*(unsigned __int64 *)(2 + 16)) & (result);
loc_003B6EC1:
    result = MiUpdateLargePageCandidateValue(a2, v_rdi, 3, 3);
    goto loc_003B6E7E;
loc_003B6EDD:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p90), 2, 3, 3);
    goto loc_003B6D7D;
loc_003B6EED:
    a3 = 0;
    result = MiMirrorNodeFreeZeroPages(v_stack_p90, a2, a3, 3);
    goto loc_003B6D34;
loc_003B6F03:
    if (2 != 3) goto loc_003B6D63;
    if ((*(unsigned __int64 *)(v_rdi)) == (*(unsigned __int64 *)(a2 + 19616))) goto loc_003B6E47;
    result = ((unsigned int)((unsigned int)((unsigned int)(a5)))) + (64);
    v_rdi = (v_rdi) * (result);
    goto loc_003B6D60;
loc_003B6F2C:
    result = (unsigned int)(a5) + 1;
    if (((unsigned int)((unsigned int)(a5))) == 7) { result = 0; }
    v_rbx = 2;
    if (((unsigned int)((unsigned int)(a5))) != 7) { v_rbx = 1; }
    v_stack_pB0 = (unsigned int)(result);
    goto loc_003B6E3F;
loc_003B6F4D:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) + 1);
    v_stack_pB0 = (unsigned int)(v_rsi);
    if (((unsigned int)(v_rsi)) == ((unsigned int)(v_r14))) goto loc_003B6E3F;
    goto loc_003B6D34;
}
```

## 5. (Beta) C Style

```c
int64_t MiWalkPagesOnLists(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;
    uint64_t v_stack_p90;
    uint32_t v_stack_pB0;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (80);
    local_r13 = 0;
    v_stack_m58 = 2 + 14;
    if (((int32_t)(Arg3)) <= 4) goto loc_003B6D2D;
loc_003B6AF0:
    v_stack_p8 = Arg2 + 4240;
loc_003B6AFF:
    v_stack_m40 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xC1020D)) != 0) {
        Arg2 = 2;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExAcquireSpinLockExclusiveAtDpcLevel(Arg2 + 4240 + 16, Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(arg2 + 0x1090)) == local_rdi) goto loc_003B6B9A;
loc_003B6B4A:
    local_rdi = (*(uint64_t *)(arg2 + 0x1090) + *(uint64_t *)(arg2 + 0x1090) * 2) << (4);
    local_rdi = (local_rdi) + (result);
    if (Arg1 == 0) goto loc_003B6CF1;
    result = MiMirrorAddPagesToBrownList(*(uint64_t *)(arg2 + 0x1090), 1, Arg3, Arg4);
loc_003B6B73:
    Arg1 = (*(uint64_t *)(local_rdi)) & (Arg2 + 4240);
    if (Arg1 != (2 + 14)) goto loc_003B6B4A;
loc_003B6B9A:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_p8 + 16, 1, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0xC10176)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_m40);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = (v_stack_p8) + (88);
    local_r14 = (v_stack_m58) - (1);
    v_stack_p8 = local_rbx;
    v_stack_m58 = local_r14;
    if (condition_is_not_equal) goto loc_003B6AFF;
    v_stack_p20 = 0;
loc_003B6BF0:
    result = (uint32_t)(-(0));
    local_rbx = (uint32_t)((local_rbx) & (128));
    local_rbx = (local_rbx) + (0xF80ULL);
    v_stack_p8 = (uint8_t)(v_stack_m40);
    if ((*(uint32_t *)(v_rip + 0xC10105)) != 0) {
        Arg2 = 2;
        Arg1 = (uint8_t)((uint8_t)(v_stack_m40));
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbp = (Arg2 + 32) + (local_rbx);
    v_stack_m40 = local_rbp;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(local_rbp, Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(local_rbx + arg2 * 1 + 0x10)) == local_r14) goto loc_003B6C9D;
loc_003B6C5F:
    local_rbx = (*(uint64_t *)(local_rbx + arg2 * 1 + 0x10) + *(uint64_t *)(local_rbx + arg2 * 1 + 0x10) * 2) << (4);
    local_rbx = (local_rbx) + (0);
    if (Arg1 == 0) goto loc_003B6D0F;
    result = MiMirrorAddPagesToBrownList(*(uint64_t *)(local_rbx + arg2 * 1 + 0x10), 1, Arg3, Arg4);
loc_003B6C7E:
    Arg1 = (*(uint64_t *)(local_rbx)) & (local_rbp);
    if (Arg1 != local_r14) goto loc_003B6C5F;
loc_003B6C9D:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_m40, 1, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0xC10074)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_p8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
    local_rdi = (uint32_t)(((uint32_t)(v_stack_p20)) + 1);
    v_stack_p20 = (uint32_t)(local_rdi);
    if (((uint32_t)(local_rdi)) < 2) goto loc_003B6BF0;
    local_rsp = (local_rsp) + (80);
    return (uint8_t)(v_stack_p8);
loc_003B6CF1:
    v_stack_p20 = 0;
    result = MiUpdateLargePageCandidateValue(Arg2, Arg1, 3, 3);
    goto loc_003B6B73;
loc_003B6D0F:
    v_stack_p20 = 0;
    result = MiUpdateLargePageCandidateValue(Arg2, Arg2, 3, 3);
    goto loc_003B6C7E;
loc_003B6D2D:
loc_003B6D34:
loc_003B6D39:
    if (v_stack_p10 <= 1) goto loc_003B6EED;
    if (v_stack_p10 != 2) goto loc_003B6F03;
    local_rdi = (*(uint64_t *)(arg2 + v_stack_p10 * 8 + 0x1BE0)) * ((uint32_t)((uint32_t)((uint32_t)(Arg5))));
    local_rdi = (local_rdi) + (0xCC0ULL);
loc_003B6D60:
    local_rdi = (local_rdi) + (Arg2);
loc_003B6D63:
    v_stack_p40 = (uint8_t)(v_stack_p8);
    if ((*(uint32_t *)(v_rip + 0xC0FFA9)) != 0) goto loc_003B6EDD;
loc_003B6D7D:
    v_stack_p48 = local_rdi + 32;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(local_rdi + 32, Arg2, 3, 3);
    if ((*(uint64_t *)(local_rdi + 0x10)) == 3) goto loc_003B6E04;
loc_003B6DB9:
    local_rbp = (*(uint64_t *)(local_rdi + 0x10) + *(uint64_t *)(local_rdi + 0x10) * 2) << (4);
    local_rbp = (local_rbp) + (result);
    v_stack_p38 = local_rbp;
    if (condition_is_above_or_equal) goto loc_003B6E68;
loc_003B6DE2:
    local_rdi = (*(uint64_t *)(local_rbp)) & ((uint32_t)(Arg5));
    if (local_rdi != 3) goto loc_003B6DB9;
loc_003B6E04:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_stack_p48, Arg2, 3, 3);
    local_r13 = 0;
    if ((*(uint32_t *)(v_rip + 0xC0FF0A)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_p40);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 3, 3);
    }
    if (v_stack_p10 == 2) goto loc_003B6F2C;
    if (v_stack_p10 == 3) goto loc_003B6F4D;
loc_003B6E3F:
loc_003B6E47:
    local_rbx = (v_stack_p10) + (1);
    if (local_rbx <= 4) goto loc_003B6D39;
    goto loc_003B6AF0;
loc_003B6E68:
    if (local_rbx == 2) goto loc_003B6E8D;
loc_003B6E6E:
    if (v_stack_p90 == 0) goto loc_003B6EC1;
    result = MiMirrorAddPagesToBrownList(local_rdi, 0, 3, 3);
loc_003B6E7E:
    goto loc_003B6DE2;
loc_003B6E8D:
    result = MiIsDecayPfn(local_rdi, 0, 3, 3);
    if ((uint32_t)(result) == 0) goto loc_003B6E6E;
    result = ~(*(uint64_t *)(v_rip + 0xA76DE0));
    Arg1 = (*(uint64_t *)(2 + 0x10)) & (result);
loc_003B6EC1:
    result = MiUpdateLargePageCandidateValue(Arg2, local_rdi, 3, 3);
    goto loc_003B6E7E;
loc_003B6EDD:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p90), 2, 3, 3);
    goto loc_003B6D7D;
loc_003B6EED:
    Arg3 = 0;
    result = MiMirrorNodeFreeZeroPages(v_stack_p90, Arg2, Arg3, 3);
    goto loc_003B6D34;
loc_003B6F03:
    if (2 != 3) goto loc_003B6D63;
    if ((*(uint64_t *)(local_rdi)) == (*(uint64_t *)(arg2 + 0x4CA0))) goto loc_003B6E47;
    result = ((uint32_t)((uint32_t)((uint32_t)(Arg5)))) + (64);
    local_rdi = (local_rdi) * (result);
    goto loc_003B6D60;
loc_003B6F2C:
    result = (uint32_t)(Arg5) + 1;
    if (((uint32_t)((uint32_t)(Arg5))) == 7) { result = 0; }
    local_rbx = 2;
    if (((uint32_t)((uint32_t)(Arg5))) != 7) { local_rbx = 1; }
    v_stack_pB0 = (uint32_t)(result);
    goto loc_003B6E3F;
loc_003B6F4D:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) + 1);
    v_stack_pB0 = (uint32_t)(local_rsi);
    if (((uint32_t)(local_rsi)) == ((uint32_t)(local_r14))) goto loc_003B6E3F;
    goto loc_003B6D34;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x1090` | `64` | `R` |
| `Arg2` | `+ 0x1BE0 + rbx*8` | `64` | `R` |
| `Arg2` | `+ 0x4CA0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003B6AA4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
