# PopFxActivateComponentDependents

- RVA: `0x002BE9F0`–`0x002BEF10` (길이 `1,312` bytes)
- VA: `0x00000001402BE9F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E424`
- 디코드: `309`개 명령, `1,312/1,312` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x002BEA53` → [KiAcquireSpinLockInstrumented](../20/KiAcquireSpinLockInstrumented_function_002084F0.md) (function, `0x002084F0`)
- `0x002BEABD` → [KxWaitForSpinLockAndAcquire](../20/KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)
- `0x002BEB24` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002BEB57` → [PopQueueQuerySetIrp](PopQueueQuerySetIrp_function_002BEF18.md) (function, `0x002BEF18`)
- `0x002BEB97` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x002BEBBC` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x002BEBD2` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002BEC3A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002BEC71` → [PopPepProcessEvent](../24/PopPepProcessEvent_function_0024B930.md) (function, `0x0024B930`)
- `0x002BEC98` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002BECAF` → [PopFxBugCheck](PopFxBugCheck_function_002BFC6C.md) (function, `0x002BFC6C`)
- `0x002BECDF` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x002BECF3` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x002BED2E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002BED51` → [PopFxBugCheck](PopFxBugCheck_function_002BFC6C.md) (function, `0x002BFC6C`)
- `0x002BED70` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x002BEE30` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x002BEE4A` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x002BEE5B` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x002BEE86` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x002BEE95` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x002BEEC3` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x002BEECD` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x002BEEE5` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x002BEF09` → [PopPluginComponentActive](../24/PopPluginComponentActive_function_0024B800.md) (function, `0x0024B800`)

### Direct callers
- [PopFxCompleteComponentActivation](PopFxCompleteComponentActivation_function_002BDDE4.md) at `0x002BDE56`

### Static image references
- `0x002BEA30` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002BEA3D` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x002BEA46` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x002BED2E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002BE9F0  40 53                           push rbx
002BE9F2  55                              push rbp
002BE9F3  56                              push rsi
002BE9F4  57                              push rdi
002BE9F5  41 54                           push r12
002BE9F7  41 55                           push r13
002BE9F9  41 56                           push r14
002BE9FB  41 57                           push r15
002BE9FD  48 83 EC 68                     sub rsp, 0x68
002BEA01  48 8B 69 50                     mov rbp, qword ptr [rcx + 0x50]
002BEA05  33 F6                           xor esi, esi
002BEA07  0F 57 C0                        xorps xmm0, xmm0
002BEA0A  48 8B F9                        mov rdi, rcx
002BEA0D  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
002BEA12  8D 46 02                        lea eax, [rsi + 2]
002BEA15  39 B1 BC 00 00 00               cmp dword ptr [rcx + 0xbc], esi
002BEA1B  0F 87 4F 01 00 00               ja 0x1402beb70
002BEA21  48 8D B7 80 00 00 00            lea rsi, [rdi + 0x80]
002BEA28  44 0F 20 C5                     mov rbp, cr8
002BEA2C  44 0F 22 C0                     mov cr8, rax
002BEA30  83 3D E9 82 D0 00 00            cmp dword ptr [rip + 0xd082e9], 0
002BEA37  0F 85 55 02 00 00               jne 0x1402bec92
002BEA3D  F6 05 C2 80 D0 00 21            test byte ptr [rip + 0xd080c2], 0x21
002BEA44  74 6C                           je 0x1402beab2
002BEA46  8B 05 0C F4 C4 00               mov eax, dword ptr [rip + 0xc4f40c]
002BEA4C  85 C0                           test eax, eax
002BEA4E  75 62                           jne 0x1402beab2
002BEA50  48 8B CE                        mov rcx, rsi
002BEA53  E8 98 9A F4 FF                  call 0x1402084f0
002BEA58  48 8D 44 24 30                  lea rax, [rsp + 0x30]
002BEA5D  45 33 F6                        xor r14d, r14d
002BEA60  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002BEA65  48 8D 9F B8 01 00 00            lea rbx, [rdi + 0x1b8]
002BEA6C  48 8D 44 24 30                  lea rax, [rsp + 0x30]
002BEA71  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002BEA76  48 8B 3B                        mov rdi, qword ptr [rbx]
002BEA79  48 3B FB                        cmp rdi, rbx
002BEA7C  0F 85 52 02 00 00               jne 0x1402becd4
002BEA82  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
002BEA87  48 8D 44 24 30                  lea rax, [rsp + 0x30]
002BEA8C  48 3B C8                        cmp rcx, rax
002BEA8F  74 70                           je 0x1402beb01
002BEA91  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
002BEA96  48 8D 44 24 30                  lea rax, [rsp + 0x30]
002BEA9B  48 39 41 08                     cmp qword ptr [rcx + 8], rax
002BEA9F  75 0A                           jne 0x1402beaab
002BEAA1  48 8D 44 24 30                  lea rax, [rsp + 0x30]
002BEAA6  48 39 02                        cmp qword ptr [rdx], rax
002BEAA9  74 19                           je 0x1402beac4
002BEAAB  B9 03 00 00 00                  mov ecx, 3
002BEAB0  CD 29                           int 0x29
002BEAB2  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
002BEAB8  73 9E                           jae 0x1402bea58
002BEABA  48 8B CE                        mov rcx, rsi
002BEABD  E8 FE 9A F4 FF                  call 0x1402085c0
002BEAC2  EB 94                           jmp 0x1402bea58
002BEAC4  48 89 0A                        mov qword ptr [rdx], rcx
002BEAC7  48 89 51 08                     mov qword ptr [rcx + 8], rdx
002BEACB  48 8B 03                        mov rax, qword ptr [rbx]
002BEACE  4C 8B 43 08                     mov r8, qword ptr [rbx + 8]
002BEAD2  48 39 58 08                     cmp qword ptr [rax + 8], rbx
002BEAD6  75 D3                           jne 0x1402beaab
002BEAD8  49 39 18                        cmp qword ptr [r8], rbx
002BEADB  75 CE                           jne 0x1402beaab
002BEADD  48 8B 01                        mov rax, qword ptr [rcx]
002BEAE0  48 39 48 08                     cmp qword ptr [rax + 8], rcx
002BEAE4  75 C5                           jne 0x1402beaab
002BEAE6  48 39 0A                        cmp qword ptr [rdx], rcx
002BEAE9  75 C0                           jne 0x1402beaab
002BEAEB  49 89 08                        mov qword ptr [r8], rcx
002BEAEE  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
002BEAF2  48 89 43 08                     mov qword ptr [rbx + 8], rax
002BEAF6  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
002BEAFA  48 89 18                        mov qword ptr [rax], rbx
002BEAFD  4C 89 41 08                     mov qword ptr [rcx + 8], r8
002BEB01  F6 05 FE 7F D0 00 01            test byte ptr [rip + 0xd07ffe], 1
002BEB08  0F 85 49 02 00 00               jne 0x1402bed57
002BEB0E  F0 48 83 26 00                  lock and qword ptr [rsi], 0
002BEB13  83 3D 06 82 D0 00 00            cmp dword ptr [rip + 0xd08206], 0
002BEB1A  74 0D                           je 0x1402beb29
002BEB1C  44 0F 20 C1                     mov rcx, cr8
002BEB20  40 0F B6 D5                     movzx edx, bpl
002BEB24  E8 6F 6B 23 00                  call 0x1404f5698
002BEB29  40 0F B6 C5                     movzx eax, bpl
002BEB2D  44 0F 22 C0                     mov cr8, rax
002BEB31  4D 85 F6                        test r14, r14
002BEB34  75 1A                           jne 0x1402beb50
002BEB36  48 83 C4 68                     add rsp, 0x68
002BEB3A  41 5F                           pop r15
002BEB3C  41 5E                           pop r14
002BEB3E  41 5D                           pop r13
002BEB40  41 5C                           pop r12
002BEB42  5F                              pop rdi
002BEB43  5E                              pop rsi
002BEB44  5D                              pop rbp
002BEB45  5B                              pop rbx
002BEB46  C3                              ret
002BEB47  CC                              int3
002BEB48  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
002BEB50  49 8B CE                        mov rcx, r14
002BEB53  4D 8B 76 78                     mov r14, qword ptr [r14 + 0x78]
002BEB57  E8 BC 03 00 00                  call 0x1402bef18
002BEB5C  4D 85 F6                        test r14, r14
002BEB5F  74 D5                           je 0x1402beb36
002BEB61  EB ED                           jmp 0x1402beb50
002BEB63  0F 1F 40 00                     nop dword ptr [rax]
002BEB67  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
002BEB70  48 8B 87 C0 00 00 00            mov rax, qword ptr [rdi + 0xc0]
002BEB77  8B 14 F0                        mov edx, dword ptr [rax + rsi*8]
002BEB7A  8B 5C F0 04                     mov ebx, dword ptr [rax + rsi*8 + 4]
002BEB7E  48 8B 85 68 03 00 00            mov rax, qword ptr [rbp + 0x368]
002BEB85  89 94 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], edx
002BEB8C  4C 8B 2C D0                     mov r13, qword ptr [rax + rdx*8]
002BEB90  49 8D 8D 80 00 00 00            lea rcx, [r13 + 0x80]
002BEB97  E8 D4 98 F4 FF                  call 0x140208470
002BEB9C  49 8B 95 B0 00 00 00            mov rdx, qword ptr [r13 + 0xb0]
002BEBA3  45 32 E4                        xor r12b, r12b
002BEBA6  44 0F B6 F0                     movzx r14d, al
002BEBAA  44 38 64 DA 04                  cmp byte ptr [rdx + rbx*8 + 4], r12b
002BEBAF  0F 85 00 01 00 00               jne 0x1402becb5
002BEBB5  49 8D 8D 80 00 00 00            lea rcx, [r13 + 0x80]
002BEBBC  E8 AF 7A F4 FF                  call 0x140206670
002BEBC1  83 3D 58 81 D0 00 00            cmp dword ptr [rip + 0xd08158], 0
002BEBC8  74 0D                           je 0x1402bebd7
002BEBCA  44 0F 20 C1                     mov rcx, cr8
002BEBCE  41 0F B6 D6                     movzx edx, r14b
002BEBD2  E8 C1 6A 23 00                  call 0x1404f5698
002BEBD7  45 0F 22 C6                     mov cr8, r14
002BEBDB  45 84 E4                        test r12b, r12b
002BEBDE  0F 84 96 00 00 00               je 0x1402bec7a
002BEBE4  48 8B 5D 38                     mov rbx, qword ptr [rbp + 0x38]
002BEBE8  44 8B BC 24 B0 00 00 00         mov r15d, dword ptr [rsp + 0xb0]
002BEBF0  80 7B 7C 00                     cmp byte ptr [rbx + 0x7c], 0
002BEBF4  74 51                           je 0x1402bec47
002BEBF6  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
002BEBFA  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
002BEBFF  0F 57 C0                        xorps xmm0, xmm0
002BEC02  B9 07 00 00 00                  mov ecx, 7
002BEC07  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
002BEC0C  44 89 7C 24 48                  mov dword ptr [rsp + 0x48], r15d
002BEC11  4C 8B 70 40                     mov r14, qword ptr [rax + 0x40]
002BEC15  48 8B 40 48                     mov rax, qword ptr [rax + 0x48]
002BEC19  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
002BEC1E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002BEC23  C6 44 24 4C 01                  mov byte ptr [rsp + 0x4c], 1
002BEC28  48 C7 44 24 50 00 00 00 00      mov qword ptr [rsp + 0x50], 0
002BEC31  C6 44 24 58 00                  mov byte ptr [rsp + 0x58], 0
002BEC36  49 8B 46 60                     mov rax, qword ptr [r14 + 0x60]
002BEC3A  E8 91 BE 3F 00                  call 0x1406baad0
002BEC3F  84 C0                           test al, al
002BEC41  0F 85 F1 00 00 00               jne 0x1402bed38
002BEC47  41 8B C7                        mov eax, r15d
002BEC4A  41 B9 02 00 00 00               mov r9d, 2
002BEC50  48 69 D0 D0 00 00 00            imul rdx, rax, 0xd0
002BEC57  48 8B CB                        mov rcx, rbx
002BEC5A  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
002BEC63  48 81 C2 C0 00 00 00            add rdx, 0xc0
002BEC6A  45 8D 41 04                     lea r8d, [r9 + 4]
002BEC6E  48 03 D3                        add rdx, rbx
002BEC71  E8 BA CC F8 FF                  call 0x14024b930
002BEC76  84 C0                           test al, al
002BEC78  75 28                           jne 0x1402beca2
002BEC7A  FF C6                           inc esi
002BEC7C  3B B7 BC 00 00 00               cmp esi, dword ptr [rdi + 0xbc]
002BEC82  0F 82 E8 FE FF FF               jb 0x1402beb70
002BEC88  B8 02 00 00 00                  mov eax, 2
002BEC8D  E9 8F FD FF FF                  jmp 0x1402bea21
002BEC92  B2 02                           mov dl, 2
002BEC94  40 0F B6 CD                     movzx ecx, bpl
002BEC98  E8 5F 6A 23 00                  call 0x1404f56fc
002BEC9D  E9 9B FD FF FF                  jmp 0x1402bea3d
002BECA2  45 33 C9                        xor r9d, r9d
002BECA5  45 33 C0                        xor r8d, r8d
002BECA8  33 D2                           xor edx, edx
002BECAA  B9 12 06 00 00                  mov ecx, 0x612
002BECAF  E8 B8 0F 00 00                  call 0x1402bfc6c
002BECB4  CC                              int3
002BECB5  44 88 64 DA 04                  mov byte ptr [rdx + rbx*8 + 4], r12b
002BECBA  B8 01 00 00 00                  mov eax, 1
002BECBF  41 83 85 B8 00 00 00 FF         add dword ptr [r13 + 0xb8], -1
002BECC7  45 0F B6 E4                     movzx r12d, r12b
002BECCB  44 0F 44 E0                     cmove r12d, eax
002BECCF  E9 E1 FE FF FF                  jmp 0x1402bebb5
002BECD4  4C 8D 7F E0                     lea r15, [rdi - 0x20]
002BECD8  4D 8D 67 08                     lea r12, [r15 + 8]
002BECDC  49 8B CC                        mov rcx, r12
002BECDF  E8 4C 97 F4 FF                  call 0x140208430
002BECE4  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
002BECE8  A8 08                           test al, 8
002BECEA  0F 85 8A 00 00 00               jne 0x1402bed7a
002BECF0  49 8B CC                        mov rcx, r12
002BECF3  E8 78 79 F4 FF                  call 0x140206670
002BECF8  41 83 67 10 FB                  and dword ptr [r15 + 0x10], 0xfffffffb
002BECFD  49 C7 47 18 00 00 00 00         mov qword ptr [r15 + 0x18], 0
002BED05  48 8B 0F                        mov rcx, qword ptr [rdi]
002BED08  48 39 79 08                     cmp qword ptr [rcx + 8], rdi
002BED0C  0F 85 99 FD FF FF               jne 0x1402beaab
002BED12  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
002BED16  48 39 38                        cmp qword ptr [rax], rdi
002BED19  0F 85 8C FD FF FF               jne 0x1402beaab
002BED1F  48 89 08                        mov qword ptr [rax], rcx
002BED22  BA 50 46 58 4D                  mov edx, 0x4d584650
002BED27  48 89 41 08                     mov qword ptr [rcx + 8], rax
002BED2B  49 8B CF                        mov rcx, r15
002BED2E  E8 3D 3B 8C 00                  call 0x140b82870
002BED33  E9 3E FD FF FF                  jmp 0x1402bea76
002BED38  80 7C 24 58 00                  cmp byte ptr [rsp + 0x58], 0
002BED3D  0F 84 04 FF FF FF               je 0x1402bec47
002BED43  45 33 C9                        xor r9d, r9d
002BED46  45 33 C0                        xor r8d, r8d
002BED49  49 8B D6                        mov rdx, r14
002BED4C  B9 12 06 00 00                  mov ecx, 0x612
002BED51  E8 16 0F 00 00                  call 0x1402bfc6c
002BED56  CC                              int3
002BED57  8B 05 FB F0 C4 00               mov eax, dword ptr [rip + 0xc4f0fb]
002BED5D  85 C0                           test eax, eax
002BED5F  0F 85 A9 FD FF FF               jne 0x1402beb0e
002BED65  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
002BED6D  48 8B CE                        mov rcx, rsi
002BED70  E8 7B 41 0D 00                  call 0x140392ef0
002BED75  E9 99 FD FF FF                  jmp 0x1402beb13
002BED7A  48 8B 07                        mov rax, qword ptr [rdi]
002BED7D  48 39 78 08                     cmp qword ptr [rax + 8], rdi
002BED81  0F 85 24 FD FF FF               jne 0x1402beaab
002BED87  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
002BED8B  48 39 39                        cmp qword ptr [rcx], rdi
002BED8E  0F 85 17 FD FF FF               jne 0x1402beaab
002BED94  48 89 01                        mov qword ptr [rcx], rax
002BED97  48 89 48 08                     mov qword ptr [rax + 8], rcx
002BED9B  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
002BEDA0  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
002BEDA5  48 39 08                        cmp qword ptr [rax], rcx
002BEDA8  0F 85 FD FC FF FF               jne 0x1402beaab
002BEDAE  48 89 47 08                     mov qword ptr [rdi + 8], rax
002BEDB2  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
002BEDB7  48 89 0F                        mov qword ptr [rdi], rcx
002BEDBA  48 89 38                        mov qword ptr [rax], rdi
002BEDBD  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
002BEDC2  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
002BEDC6  0F B6 C8                        movzx ecx, al
002BEDC9  80 E1 01                        and cl, 1
002BEDCC  83 E0 FE                        and eax, 0xfffffffe
002BEDCF  88 8C 24 B0 00 00 00            mov byte ptr [rsp + 0xb0], cl
002BEDD6  41 89 47 10                     mov dword ptr [r15 + 0x10], eax
002BEDDA  84 C9                           test cl, cl
002BEDDC  74 07                           je 0x1402bede5
002BEDDE  83 C8 02                        or eax, 2
002BEDE1  41 89 47 10                     mov dword ptr [r15 + 0x10], eax
002BEDE5  49 8B 7F 30                     mov rdi, qword ptr [r15 + 0x30]
002BEDE9  45 33 ED                        xor r13d, r13d
002BEDEC  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
002BEDF4  45 39 2F                        cmp dword ptr [r15], r13d
002BEDF7  0F 85 A5 00 00 00               jne 0x1402beea2
002BEDFD  4C 8D AF 00 FB FF FF            lea r13, [rdi - 0x500]
002BEE04  48 C7 84 24 C0 00 00 00 10 00 00 00  mov qword ptr [rsp + 0xc0], 0x10
002BEE10  BF 80 00 00 00                  mov edi, 0x80
002BEE15  48 C7 84 24 C8 00 00 00 50 00 00 00  mov qword ptr [rsp + 0xc8], 0x50
002BEE21  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
002BEE29  44 8D 7F 38                     lea r15d, [rdi + 0x38]
002BEE2D  49 8B CC                        mov rcx, r12
002BEE30  E8 3B 78 F4 FF                  call 0x140206670
002BEE35  80 BC 24 B0 00 00 00 00         cmp byte ptr [rsp + 0xb0], 0
002BEE3D  0F 84 33 FC FF FF               je 0x1402bea76
002BEE43  40 0F B6 D5                     movzx edx, bpl
002BEE47  48 8B CE                        mov rcx, rsi
002BEE4A  E8 51 3D 0D 00                  call 0x140392ba0
002BEE4F  4D 85 ED                        test r13, r13
002BEE52  74 76                           je 0x1402beeca
002BEE54  49 8D 8D 00 05 00 00            lea rcx, [r13 + 0x500]
002BEE5B  E8 10 96 F4 FF                  call 0x140208470
002BEE60  41 83 85 08 05 00 00 FF         add dword ptr [r13 + 0x508], -1
002BEE68  49 8D 8D 00 05 00 00            lea rcx, [r13 + 0x500]
002BEE6F  0F B6 D0                        movzx edx, al
002BEE72  75 4F                           jne 0x1402beec3
002BEE74  49 8B BD 10 05 00 00            mov rdi, qword ptr [r13 + 0x510]
002BEE7B  49 C7 85 10 05 00 00 00 00 00 00  mov qword ptr [r13 + 0x510], 0
002BEE86  E8 15 3D 0D 00                  call 0x140392ba0
002BEE8B  4C 89 77 78                     mov qword ptr [rdi + 0x78], r14
002BEE8F  4C 8B F7                        mov r14, rdi
002BEE92  48 8B CE                        mov rcx, rsi
002BEE95  E8 D6 95 F4 FF                  call 0x140208470
002BEE9A  0F B6 E8                        movzx ebp, al
002BEE9D  E9 D4 FB FF FF                  jmp 0x1402bea76
002BEEA2  48 8D 47 90                     lea rax, [rdi - 0x70]
002BEEA6  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
002BEEAE  4C 8D 7F 38                     lea r15, [rdi + 0x38]
002BEEB2  48 8D 47 D0                     lea rax, [rdi - 0x30]
002BEEB6  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
002BEEBE  E9 6A FF FF FF                  jmp 0x1402bee2d
002BEEC3  E8 D8 3C 0D 00                  call 0x140392ba0
002BEEC8  EB C8                           jmp 0x1402bee92
002BEECA  48 8B CF                        mov rcx, rdi
002BEECD  E8 9E 95 F4 FF                  call 0x140208470
002BEED2  41 8B 3F                        mov edi, dword ptr [r15]
002BEED5  0F B6 D0                        movzx edx, al
002BEED8  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
002BEEE0  FF CF                           dec edi
002BEEE2  41 89 3F                        mov dword ptr [r15], edi
002BEEE5  E8 B6 3C 0D 00                  call 0x140392ba0
002BEEEA  85 FF                           test edi, edi
002BEEEC  75 A4                           jne 0x1402bee92
002BEEEE  48 8B 94 24 C0 00 00 00         mov rdx, qword ptr [rsp + 0xc0]
002BEEF6  45 33 C9                        xor r9d, r9d
002BEEF9  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
002BEF01  41 B0 01                        mov r8b, 1
002BEF04  8B 12                           mov edx, dword ptr [rdx]
002BEF06  48 8B 09                        mov rcx, qword ptr [rcx]
002BEF09  E8 F2 C8 F8 FF                  call 0x14024b800
002BEF0E  EB 82                           jmp 0x1402bee92
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxActivateComponentDependents(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int8 v_stack_p4C;
    unsigned __int64 v_stack_p50;
    unsigned __int8 v_stack_p58;
    unsigned __int64 v_stack_pA8;
    unsigned int v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;

    v_rsp = (v_rsp) - (104);
    v_rsi = 0;
    v_stack_m78 = v_xmm0;
    if ((*(unsigned int *)(a1 + 188)) > 0) goto loc_002BEB70;
loc_002BEA21:
    if ((*(unsigned int *)(v_rip + 13665001)) != 0) goto loc_002BEC92;
loc_002BEA3D:
    if (((*(unsigned __int8 *)(v_rip + 13664450)) & (33)) == 0) goto loc_002BEAB2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12907532))) != 0) goto loc_002BEAB2;
    result = KiAcquireSpinLockInstrumented(a1 + 128, a2, a3, a4);
loc_002BEA58:
    v_r14 = 0;
    v_stack_m70 = v_stack_m78;
    v_stack_m78 = v_stack_m78;
loc_002BEA76:
    if ((*(unsigned __int64 *)(a1 + 440)) != (a1 + 440)) goto loc_002BECD4;
    if (v_stack_m78 == v_stack_m78) goto loc_002BEB01;
    if ((*(unsigned __int64 *)(v_stack_m78 + 8)) != v_stack_m78) goto loc_002BEAAB;
    if ((*(unsigned __int64 *)(v_stack_m70)) == v_stack_m78) goto loc_002BEAC4;
loc_002BEAAB:
loc_002BEAB2:
    if ((*(unsigned __int64 *)(v_stack_m70)) >= v_stack_m78) goto loc_002BEA58;
    result = KxWaitForSpinLockAndAcquire(a1 + 128, v_stack_m70, a3, a4);
    goto loc_002BEA58;
loc_002BEAC4:
    *(unsigned __int64 *)(v_stack_m70) = a1 + 128;
    *(unsigned __int64 *)(a1 + 128 + 8) = v_stack_m70;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 8)) != (a1 + 440)) goto loc_002BEAAB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440 + 8))) != (a1 + 440)) goto loc_002BEAAB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 128) + 8)) != (a1 + 128)) goto loc_002BEAAB;
    if ((*(unsigned __int64 *)(v_stack_m70)) != (a1 + 128)) goto loc_002BEAAB;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440 + 8)) = a1 + 128;
    *(unsigned __int64 *)(a1 + 440 + 8) = *(unsigned __int64 *)(a1 + 128 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 128 + 8)) = a1 + 440;
    *(unsigned __int64 *)(a1 + 128 + 8) = *(unsigned __int64 *)(a1 + 440 + 8);
loc_002BEB01:
    if (((*(unsigned __int8 *)(v_rip + 13664254)) & (1)) != 0) goto loc_002BED57;
loc_002BEB0E:
loc_002BEB13:
    result = *(unsigned __int64 *)(a1 + 128 + 8);
    if ((*(unsigned int *)(v_rip + 13664774)) != 0) {
        a1 = v_rsi + 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(a1 + 440 + 8), a4);
    }
    if (0 != 0) goto loc_002BEB50;
loc_002BEB36:
    v_rsp = (v_rsp) + (104);
    return (unsigned __int8)(v_cr8);
loc_002BEB50:
    result = PopQueueQuerySetIrp(0, a2, *(unsigned __int64 *)(a1 + 440 + 8), a4);
    if (*(unsigned __int64 *)(v_r14 + 120) == 0) goto loc_002BEB36;
    goto loc_002BEB50;
loc_002BEB70:
    v_stack_pB0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 192) + a1 + 128 * 8)));
    result = KeAcquireSpinLockRaiseToDpc(*(unsigned __int64 *)(*(unsigned __int64 *)(v_cr8 + 872) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 192) + a1 + 128 * 8)) * 8) + 128, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 192) + a1 + 128 * 8)), *(unsigned __int64 *)(a1 + 440 + 8), a4);
    v_r12 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_cr8 + 872) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 192) + a1 + 128 * 8)) * 8) + 176) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 192) + a1 + 128 * 8 + 4)) * 8 + 4)) != 0) goto loc_002BECB5;
loc_002BEBB5:
    result = KxReleaseSpinLock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_cr8 + 872) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 192) + a1 + 128 * 8)) * 8) + 128, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_cr8 + 872) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 192) + a1 + 128 * 8)) * 8) + 176), *(unsigned __int64 *)(a1 + 440 + 8), a4);
    if ((*(unsigned int *)(v_rip + 13664600)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(a1 + 440 + 8), a4);
    }
    if (0 == 0) goto loc_002BEC7A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_cr8 + 56) + 124)) == 0) goto loc_002BEC47;
    v_stack_p40 = v_xmm0;
    v_stack_p48 = (unsigned int)((unsigned int)(v_stack_pB0));
    v_stack_p50 = v_xmm0;
    v_stack_p40 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_cr8 + 56) + 32) + 72);
    v_stack_p4C = 1;
    v_stack_p50 = 0;
    v_stack_p58 = 0;
    result = guard_dispatch_icall(7, v_stack_p40, *(unsigned __int64 *)(a1 + 440 + 8), a4);
    if ((unsigned __int8)(result) != 0) goto loc_002BED38;
loc_002BEC47:
    a2 = (v_stack_p40) * ((unsigned int)((unsigned int)((unsigned int)(v_stack_pB0))));
    v_stack_p28 = 0;
    a2 = (a2) + (192);
    a2 = (a2) + (*(unsigned __int64 *)(v_cr8 + 56));
    result = PopPepProcessEvent(*(unsigned __int64 *)(v_cr8 + 56), a2, 2 + 4, 2);
    if ((unsigned __int8)(result) != 0) goto loc_002BECA2;
loc_002BEC7A:
    v_rsi = (unsigned int)((a1 + 128) + 1);
    if (((unsigned int)(v_rsi)) < (*(unsigned int *)(*(unsigned __int64 *)(a1 + 440) + 188))) goto loc_002BEB70;
    goto loc_002BEA21;
loc_002BEC92:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), 2, 2 + 4, 2);
    goto loc_002BEA3D;
loc_002BECA2:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = PopFxBugCheck((unsigned int)(0x612ULL), a2, a3, a4);
loc_002BECB5:
    *(unsigned __int8 *)(a2 + *(unsigned __int64 *)(v_cr8 + 56) * 8 + 4) = 0;
    v_r12 = 0;
    if (condition_is_equal) { v_r12 = 1; }
    goto loc_002BEBB5;
loc_002BECD4:
    result = KeAcquireSpinLockAtDpcLevel(*(unsigned __int64 *)(a1 + 440) - 32 + 8, a2, a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 440) - 32 + 16)))) & (8)) != 0) goto loc_002BED7A;
    result = KxReleaseSpinLock(*(unsigned __int64 *)(a1 + 440) - 32 + 8, a2, a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 24) = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440)) + 8)) != (*(unsigned __int64 *)(a1 + 440))) goto loc_002BEAAB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 8))) != (*(unsigned __int64 *)(a1 + 440))) goto loc_002BEAAB;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 8);
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 440) - 32, (unsigned int)(0x4D584650ULL), a3, a4);
    goto loc_002BEA76;
loc_002BED38:
    if (v_stack_p58 == 0) goto loc_002BEC47;
    a4 = 0;
    a3 = 0;
    result = PopFxBugCheck((unsigned int)(0x612ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_cr8 + 56) + 32) + 64), a3, a4);
loc_002BED57:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12906747))) != 0) goto loc_002BEB0E;
    result = KiReleaseSpinLockInstrumented(v_rsi, v_stack_pA8, a3, a4);
    goto loc_002BEB13;
loc_002BED7A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440)) + 8)) != (*(unsigned __int64 *)(a1 + 440))) goto loc_002BEAAB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 8))) != (*(unsigned __int64 *)(a1 + 440))) goto loc_002BEAAB;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 8);
    if ((*(unsigned __int64 *)(v_stack_p38)) != v_stack_p30) goto loc_002BEAAB;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) + 8) = v_stack_p38;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440)) = v_stack_p30;
    *(unsigned __int64 *)(v_stack_p38) = *(unsigned __int64 *)(a1 + 440);
    v_stack_p38 = *(unsigned __int64 *)(a1 + 440);
    a1 = (unsigned __int8)(((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 440) - 32 + 16)))) & (1));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 440) - 32 + 16))) & (0xFFFFFFFEULL));
    v_stack_pB0 = (unsigned __int8)(a1);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 440) - 32 + 16) = (unsigned int)(result);
    if ((unsigned __int8)(a1) != 0) {
        result = (unsigned int)((result) | (2));
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 440) - 32 + 16) = (unsigned int)(result);
    }
    v_r13 = 0;
    v_stack_pB8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 48);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 440) - 32)) != 0) goto loc_002BEEA2;
    v_stack_pC0 = 16;
    v_stack_pC8 = 80;
    v_stack_pB8 = 128;
loc_002BEE2D:
    result = KxReleaseSpinLock(*(unsigned __int64 *)(a1 + 440) - 32 + 8, v_stack_pA8, a3, a4);
    if (v_stack_pB0 == 0) goto loc_002BEA76;
    result = KeReleaseSpinLock(v_rsi, (unsigned __int8)(v_cr8), a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 48) - 1280 == 0) goto loc_002BEECA;
    result = KeAcquireSpinLockRaiseToDpc(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 48) - 1280 + 1280, (unsigned __int8)(v_cr8), a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 48) - 1280 != 0) goto loc_002BEEC3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 48) - 1280 + 1296) = 0;
    result = KeReleaseSpinLock(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 48) - 1280 + 1280, (unsigned __int8)(result), a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 48) - 1280 + 1296) + 120) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_cr8 + 56) + 32) + 64);
loc_002BEE92:
    result = KeAcquireSpinLockRaiseToDpc(v_rsi, (unsigned __int8)(result), a3, a4);
    goto loc_002BEA76;
loc_002BEEA2:
    v_stack_pC0 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 48) - 1280 + 1296) - 112;
    v_stack_pC8 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 48) - 1280 + 1296) - 48;
    goto loc_002BEE2D;
loc_002BEEC3:
    result = KeReleaseSpinLock(v_rsi, (unsigned __int8)(result), a3, a4);
    goto loc_002BEE92;
loc_002BEECA:
    result = KeAcquireSpinLockRaiseToDpc(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 48) - 1280 + 1296), (unsigned __int8)(result), a3, a4);
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 48) - 1280 + 1296) + 56))) - 1);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 440) - 32 + 48) - 1280 + 1296) + 56) = (unsigned int)(v_rdi);
    result = KeReleaseSpinLock(v_stack_pB8, (unsigned __int8)(result), a3, a4);
    if ((unsigned int)(v_rdi) != 0) goto loc_002BEE92;
    a4 = 0;
    result = PopPluginComponentActive(*(unsigned __int64 *)(v_stack_pC8), (unsigned int)(*(unsigned int *)(v_stack_pC0)), 1, a4);
    goto loc_002BEE92;
}
```

## 5. (Beta) C Style

```c
int64_t PopFxActivateComponentDependents(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint8_t v_stack_p4C;
    uint64_t v_stack_p50;
    uint8_t v_stack_p58;
    uint64_t v_stack_pA8;
    uint32_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;

    local_rsp = (local_rsp) - (104);
    local_rsi = 0;
    v_stack_m78 = v_xmm0;
    if ((*(uint32_t *)(arg1 + 0xBC)) > 0) goto loc_002BEB70;
loc_002BEA21:
    if ((*(uint32_t *)(v_rip + 0xD082E9)) != 0) goto loc_002BEC92;
loc_002BEA3D:
    if (((*(uint8_t *)(v_rip + 0xD080C2)) & (33)) == 0) goto loc_002BEAB2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC4F40C))) != 0) goto loc_002BEAB2;
    result = KiAcquireSpinLockInstrumented(Arg1 + 128, a2, a3, a4);
loc_002BEA58:
    local_r14 = 0;
    v_stack_m70 = v_stack_m78;
    v_stack_m78 = v_stack_m78;
loc_002BEA76:
    if ((*(uint64_t *)(arg1 + 0x1B8)) != (Arg1 + 440)) goto loc_002BECD4;
    if (v_stack_m78 == v_stack_m78) goto loc_002BEB01;
    if ((*(uint64_t *)(v_stack_m78 + 0x8)) != v_stack_m78) goto loc_002BEAAB;
    if ((*(uint64_t *)(v_stack_m70)) == v_stack_m78) goto loc_002BEAC4;
loc_002BEAAB:
loc_002BEAB2:
    if ((*(uint64_t *)(v_stack_m70)) >= v_stack_m78) goto loc_002BEA58;
    result = KxWaitForSpinLockAndAcquire(Arg1 + 128, v_stack_m70, a3, a4);
    goto loc_002BEA58;
loc_002BEAC4:
    *(void **)(v_stack_m70) = Arg1 + 128;
    *(uint64_t *)(arg1 + 0x80 + 0x8) = v_stack_m70;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0x8)) != (Arg1 + 440)) goto loc_002BEAAB;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8 + 0x8))) != (Arg1 + 440)) goto loc_002BEAAB;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x80) + 0x8)) != (Arg1 + 128)) goto loc_002BEAAB;
    if ((*(uint64_t *)(v_stack_m70)) != (Arg1 + 128)) goto loc_002BEAAB;
    *(void **)(*(uint64_t *)(arg1 + 0x1B8 + 0x8)) = Arg1 + 128;
    *(uint64_t *)(arg1 + 0x1B8 + 0x8) = *(uint64_t *)(arg1 + 0x80 + 0x8);
    *(void **)(*(uint64_t *)(arg1 + 0x80 + 0x8)) = Arg1 + 440;
    *(uint64_t *)(arg1 + 0x80 + 0x8) = *(uint64_t *)(arg1 + 0x1B8 + 0x8);
loc_002BEB01:
    if (((*(uint8_t *)(v_rip + 0xD07FFE)) & (1)) != 0) goto loc_002BED57;
loc_002BEB0E:
loc_002BEB13:
    result = *(uint64_t *)(arg1 + 0x80 + 0x8);
    if ((*(uint32_t *)(v_rip + 0xD08206)) != 0) {
        Arg1 = local_rsi + 2;
        a2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, a2, *(uint64_t *)(arg1 + 0x1B8 + 0x8), a4);
    }
    if (0 != 0) goto loc_002BEB50;
loc_002BEB36:
    local_rsp = (local_rsp) + (104);
    return (uint8_t)(v_cr8);
loc_002BEB50:
    result = PopQueueQuerySetIrp(0, a2, *(uint64_t *)(arg1 + 0x1B8 + 0x8), a4);
    if (*(uint64_t *)(local_r14 + 0x78) == 0) goto loc_002BEB36;
    goto loc_002BEB50;
loc_002BEB70:
    v_stack_pB0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0xC0) + arg1 + 0x80 * 8)));
    result = KeAcquireSpinLockRaiseToDpc(*(uint64_t *)(*(uint64_t *)(v_cr8 + 0x368) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0xC0) + arg1 + 0x80 * 8)) * 8) + 128, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0xC0) + arg1 + 0x80 * 8)), *(uint64_t *)(arg1 + 0x1B8 + 0x8), a4);
    local_r12 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_cr8 + 0x368) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0xC0) + arg1 + 0x80 * 8)) * 8) + 0xB0) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0xC0) + arg1 + 0x80 * 8 + 0x4)) * 8 + 0x4)) != 0) goto loc_002BECB5;
loc_002BEBB5:
    result = KxReleaseSpinLock(*(uint64_t *)(*(uint64_t *)(v_cr8 + 0x368) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0xC0) + arg1 + 0x80 * 8)) * 8) + 128, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_cr8 + 0x368) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0xC0) + arg1 + 0x80 * 8)) * 8) + 0xB0), *(uint64_t *)(arg1 + 0x1B8 + 0x8), a4);
    if ((*(uint32_t *)(v_rip + 0xD08158)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        a2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, a2, *(uint64_t *)(arg1 + 0x1B8 + 0x8), a4);
    }
    if (0 == 0) goto loc_002BEC7A;
    if ((*(uint8_t *)(*(uint64_t *)(v_cr8 + 0x38) + 0x7C)) == 0) goto loc_002BEC47;
    v_stack_p40 = v_xmm0;
    v_stack_p48 = (uint32_t)((uint32_t)(v_stack_pB0));
    v_stack_p50 = v_xmm0;
    v_stack_p40 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_cr8 + 0x38) + 0x20) + 0x48);
    v_stack_p4C = 1;
    v_stack_p50 = 0;
    v_stack_p58 = 0;
    result = guard_dispatch_icall(7, v_stack_p40, *(uint64_t *)(arg1 + 0x1B8 + 0x8), a4);
    if ((uint8_t)(result) != 0) goto loc_002BED38;
loc_002BEC47:
    a2 = (v_stack_p40) * ((uint32_t)((uint32_t)((uint32_t)(v_stack_pB0))));
    v_stack_p28 = 0;
    a2 = (a2) + (192);
    a2 = (a2) + (*(uint64_t *)(v_cr8 + 0x38));
    result = PopPepProcessEvent(*(uint64_t *)(v_cr8 + 0x38), a2, 2 + 4, 2);
    if ((uint8_t)(result) != 0) goto loc_002BECA2;
loc_002BEC7A:
    local_rsi = (uint32_t)((Arg1 + 128) + 1);
    if (((uint32_t)(local_rsi)) < (*(uint32_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0xBC))) goto loc_002BEB70;
    goto loc_002BEA21;
loc_002BEC92:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), 2, 2 + 4, 2);
    goto loc_002BEA3D;
loc_002BECA2:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = PopFxBugCheck((uint32_t)(0x612ULL), a2, a3, a4);
loc_002BECB5:
    *(uint8_t *)(a2 + *(uint64_t *)(v_cr8 + 0x38) * 8 + 0x4) = 0;
    local_r12 = 0;
    if (condition_is_equal) { local_r12 = 1; }
    goto loc_002BEBB5;
loc_002BECD4:
    result = KeAcquireSpinLockAtDpcLevel(*(uint64_t *)(arg1 + 0x1B8) - 32 + 8, a2, a3, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x10)))) & (8)) != 0) goto loc_002BED7A;
    result = KxReleaseSpinLock(*(uint64_t *)(arg1 + 0x1B8) - 32 + 8, a2, a3, a4);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x18) = 0;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x1B8))) goto loc_002BEAAB;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0x8))) != (*(uint64_t *)(arg1 + 0x1B8))) goto loc_002BEAAB;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8)) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0x8);
    result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x1B8) - 32, (uint32_t)(0x4D584650ULL), a3, a4);
    goto loc_002BEA76;
loc_002BED38:
    if (v_stack_p58 == 0) goto loc_002BEC47;
    a4 = 0;
    a3 = 0;
    result = PopFxBugCheck((uint32_t)(0x612ULL), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_cr8 + 0x38) + 0x20) + 0x40), a3, a4);
loc_002BED57:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC4F0FB))) != 0) goto loc_002BEB0E;
    result = KiReleaseSpinLockInstrumented(local_rsi, v_stack_pA8, a3, a4);
    goto loc_002BEB13;
loc_002BED7A:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8)) + 0x8)) != (*(uint64_t *)(arg1 + 0x1B8))) goto loc_002BEAAB;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0x8))) != (*(uint64_t *)(arg1 + 0x1B8))) goto loc_002BEAAB;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0x8)) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8)) + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0x8);
    if ((*(uint64_t *)(v_stack_p38)) != v_stack_p30) goto loc_002BEAAB;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) + 0x8) = v_stack_p38;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8)) = v_stack_p30;
    *(uint64_t *)(v_stack_p38) = *(uint64_t *)(arg1 + 0x1B8);
    v_stack_p38 = *(uint64_t *)(arg1 + 0x1B8);
    Arg1 = (uint8_t)(((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x10)))) & (1));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x10))) & (0xFFFFFFFEULL));
    v_stack_pB0 = (uint8_t)(Arg1);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x10) = (uint32_t)(result);
    if ((uint8_t)(Arg1) != 0) {
        result = (uint32_t)((result) | (2));
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x10) = (uint32_t)(result);
    }
    local_r13 = 0;
    v_stack_pB8 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x30);
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20)) != 0) goto loc_002BEEA2;
    v_stack_pC0 = 16;
    v_stack_pC8 = 80;
    v_stack_pB8 = 128;
loc_002BEE2D:
    result = KxReleaseSpinLock(*(uint64_t *)(arg1 + 0x1B8) - 32 + 8, v_stack_pA8, a3, a4);
    if (v_stack_pB0 == 0) goto loc_002BEA76;
    result = KeReleaseSpinLock(local_rsi, (uint8_t)(v_cr8), a3, a4);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x30) - 1280 == 0) goto loc_002BEECA;
    result = KeAcquireSpinLockRaiseToDpc(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x30) - 1280 + 1280, (uint8_t)(v_cr8), a3, a4);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x30) - 1280 != 0) goto loc_002BEEC3;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x30) - 0x500 + 0x510) = 0;
    result = KeReleaseSpinLock(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x30) - 1280 + 1280, (uint8_t)(result), a3, a4);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x30) - 0x500 + 0x510) + 0x78) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_cr8 + 0x38) + 0x20) + 0x40);
loc_002BEE92:
    result = KeAcquireSpinLockRaiseToDpc(local_rsi, (uint8_t)(result), a3, a4);
    goto loc_002BEA76;
loc_002BEEA2:
    v_stack_pC0 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x30) - 0x500 + 0x510) - 112;
    v_stack_pC8 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x30) - 0x500 + 0x510) - 48;
    goto loc_002BEE2D;
loc_002BEEC3:
    result = KeReleaseSpinLock(local_rsi, (uint8_t)(result), a3, a4);
    goto loc_002BEE92;
loc_002BEECA:
    result = KeAcquireSpinLockRaiseToDpc(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x30) - 0x500 + 0x510), (uint8_t)(result), a3, a4);
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x30) - 0x500 + 0x510) + 0x38))) - 1);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x1B8) - 0x20 + 0x30) - 0x500 + 0x510) + 0x38) = (uint32_t)(local_rdi);
    result = KeReleaseSpinLock(v_stack_pB8, (uint8_t)(result), a3, a4);
    if ((uint32_t)(local_rdi) != 0) goto loc_002BEE92;
    a4 = 0;
    result = PopPluginComponentActive(*(uint64_t *)(v_stack_pC8), (uint32_t)(*(uint32_t *)(v_stack_pC0)), 1, a4);
    goto loc_002BEE92;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0xBC` | `32` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002BE9F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
