# MiReturnLockedVadOrNextVa

- RVA: `0x00316980`–`0x00316DD9` (길이 `1,113` bytes)
- VA: `0x0000000140316980`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000749C8`
- 디코드: `272`개 명령, `1,113/1,113` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00316A1C` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](../27/ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x00316AEC` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x00316B08` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00316B2D` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00316B92` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00316BA5` → [MiLockVadShared](MiLockVadShared_function_00316DE0.md) (function, `0x00316DE0`)
- `0x00316BCD` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00316C44` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x00316C75` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00316C92` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00316CA8` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00316CC4` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00316CE6` → [MiWaitForVadDeletion](MiWaitForVadDeletion_function_00316F1C.md) (function, `0x00316F1C`)
- `0x00316CEE` → [MiUnlockAndDereferenceVad](MiUnlockAndDereferenceVad_function_00316E60.md) (function, `0x00316E60`)
- `0x00316D18` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00316D28` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00316D35` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x00316D45` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x00316D62` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00316D79` → [MiGetNextVad](../29/MiGetNextVad_function_00297224.md) (function, `0x00297224`)
- `0x00316DB4` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x00316DC2` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00316DCF` → [MiUnlockAndDereferenceVadShared](../2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)

### Direct callers
- [MmQueryVirtualMemory](../../page/9D/MmQueryVirtualMemory_function_009D9280.md) at `0x009D992F`

### Static image references
- `0x003169ED` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003169FA` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00316A07` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00316980  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00316985  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0031698A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0031698F  57                              push rdi
00316990  41 54                           push r12
00316992  41 55                           push r13
00316994  41 56                           push r14
00316996  41 57                           push r15
00316998  48 83 EC 20                     sub rsp, 0x20
0031699C  33 FF                           xor edi, edi
0031699E  4D 8B E0                        mov r12, r8
003169A1  49 89 38                        mov qword ptr [r8], rdi
003169A4  4C 8B F2                        mov r14, rdx
003169A7  65 48 8B 2C 25 88 01 00 00      mov rbp, qword ptr gs:[0x188]
003169B0  4C 8B E9                        mov r13, rcx
003169B3  4C 8B BD B8 00 00 00            mov r15, qword ptr [rbp + 0xb8]
003169BA  BA 02 00 00 00                  mov edx, 2
003169BF  66 FF 8D E6 01 00 00            dec word ptr [rbp + 0x1e6]
003169C6  90                              nop
003169C7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003169D0  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003169D7  48 8B 99 10 04 00 00            mov rbx, qword ptr [rcx + 0x410]
003169DE  48 81 C3 EC 03 00 00            add rbx, 0x3ec
003169E5  44 0F 20 C6                     mov rsi, cr8
003169E9  44 0F 22 C2                     mov cr8, rdx
003169ED  83 3D 2C 03 CB 00 00            cmp dword ptr [rip + 0xcb032c], 0
003169F4  0F 85 28 03 00 00               jne 0x140316d22
003169FA  F6 05 05 01 CB 00 21            test byte ptr [rip + 0xcb0105], 0x21
00316A01  0F 84 1C 02 00 00               je 0x140316c23
00316A07  8B 05 4B 74 BF 00               mov eax, dword ptr [rip + 0xbf744b]
00316A0D  85 C0                           test eax, eax
00316A0F  0F 85 0E 02 00 00               jne 0x140316c23
00316A15  40 0F B6 D6                     movzx edx, sil
00316A19  48 8B CB                        mov rcx, rbx
00316A1C  E8 FF 62 F6 FF                  call 0x14027cd20
00316A21  41 8B 87 F4 01 00 00            mov eax, dword ptr [r15 + 0x1f4]
00316A28  A8 20                           test al, 0x20
00316A2A  0F 85 0F 03 00 00               jne 0x140316d3f
00316A30  49 8B 9F 58 05 00 00            mov rbx, qword ptr [r15 + 0x558]
00316A37  48 85 DB                        test rbx, rbx
00316A3A  0F 84 84 00 00 00               je 0x140316ac4
00316A40  49 8B FD                        mov rdi, r13
00316A43  48 C1 EF 0C                     shr rdi, 0xc
00316A47  4C 8B C3                        mov r8, rbx
00316A4A  48 85 DB                        test rbx, rbx
00316A4D  74 75                           je 0x140316ac4
00316A4F  0F B6 53 20                     movzx edx, byte ptr [rbx + 0x20]
00316A53  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
00316A56  48 C1 E2 20                     shl rdx, 0x20
00316A5A  48 0B D0                        or rdx, rax
00316A5D  48 3B FA                        cmp rdi, rdx
00316A60  72 1E                           jb 0x140316a80
00316A62  0F B6 4B 21                     movzx ecx, byte ptr [rbx + 0x21]
00316A66  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
00316A69  48 C1 E1 20                     shl rcx, 0x20
00316A6D  48 0B C8                        or rcx, rax
00316A70  48 3B F9                        cmp rdi, rcx
00316A73  76 3E                           jbe 0x140316ab3
00316A75  48 3B FA                        cmp rdi, rdx
00316A78  72 06                           jb 0x140316a80
00316A7A  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00316A7E  EB 03                           jmp 0x140316a83
00316A80  48 8B 03                        mov rax, qword ptr [rbx]
00316A83  48 8B D8                        mov rbx, rax
00316A86  48 85 C0                        test rax, rax
00316A89  75 BC                           jne 0x140316a47
00316A8B  41 0F B6 58 20                  movzx ebx, byte ptr [r8 + 0x20]
00316A90  41 8B 48 18                     mov ecx, dword ptr [r8 + 0x18]
00316A94  8B C3                           mov eax, ebx
00316A96  48 C1 E0 20                     shl rax, 0x20
00316A9A  48 0B C1                        or rax, rcx
00316A9D  48 3B C7                        cmp rax, rdi
00316AA0  0F 82 D0 02 00 00               jb 0x140316d76
00316AA6  48 C1 E3 20                     shl rbx, 0x20
00316AAA  48 0B D9                        or rbx, rcx
00316AAD  48 C1 E3 0C                     shl rbx, 0xc
00316AB1  EB 1B                           jmp 0x140316ace
00316AB3  F0 FF 43 24                     lock inc dword ptr [rbx + 0x24]
00316AB7  0F 85 83 00 00 00               jne 0x140316b40
00316ABD  B9 0E 00 00 00                  mov ecx, 0xe
00316AC2  CD 29                           int 0x29
00316AC4  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00316ACE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00316AD7  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00316ADE  48 8B 89 10 04 00 00            mov rcx, qword ptr [rcx + 0x410]
00316AE5  48 81 C1 EC 03 00 00            add rcx, 0x3ec
00316AEC  E8 9F 3A F3 FF                  call 0x14024a590
00316AF1  40 80 FE 11                     cmp sil, 0x11
00316AF5  74 1E                           je 0x140316b15
00316AF7  83 3D 22 02 CB 00 00            cmp dword ptr [rip + 0xcb0222], 0
00316AFE  74 0D                           je 0x140316b0d
00316B00  44 0F 20 C1                     mov rcx, cr8
00316B04  40 0F B6 D6                     movzx edx, sil
00316B08  E8 8B EB 1D 00                  call 0x1404f5698
00316B0D  40 0F B6 C6                     movzx eax, sil
00316B11  44 0F 22 C0                     mov cr8, rax
00316B15  90                              nop
00316B16  66 83 85 E6 01 00 00 01         add word ptr [rbp + 0x1e6], 1
00316B1E  75 12                           jne 0x140316b32
00316B20  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
00316B27  90                              nop
00316B28  48 39 00                        cmp qword ptr [rax], rax
00316B2B  74 05                           je 0x140316b32
00316B2D  E8 4E C1 FC FF                  call 0x1402e2c80
00316B32  33 C0                           xor eax, eax
00316B34  49 89 1C 24                     mov qword ptr [r12], rbx
00316B38  49 89 06                        mov qword ptr [r14], rax
00316B3B  E9 C5 00 00 00                  jmp 0x140316c05
00316B40  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00316B49  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00316B50  4C 8B 81 10 04 00 00            mov r8, qword ptr [rcx + 0x410]
00316B57  49 81 C0 EC 03 00 00            add r8, 0x3ec
00316B5E  40 80 FE 11                     cmp sil, 0x11
00316B62  0F 84 CA 01 00 00               je 0x140316d32
00316B68  F6 05 97 FF CA 00 01            test byte ptr [rip + 0xcaff97], 1
00316B6F  0F 85 29 02 00 00               jne 0x140316d9e
00316B75  F0 41 81 20 FF FF FF BF         lock and dword ptr [r8], 0xbfffffff
00316B7D  F0 41 FF 08                     lock dec dword ptr [r8]
00316B81  83 3D 98 01 CB 00 00            cmp dword ptr [rip + 0xcb0198], 0
00316B88  74 0D                           je 0x140316b97
00316B8A  44 0F 20 C1                     mov rcx, cr8
00316B8E  40 0F B6 D6                     movzx edx, sil
00316B92  E8 01 EB 1D 00                  call 0x1404f5698
00316B97  40 0F B6 C6                     movzx eax, sil
00316B9B  44 0F 22 C0                     mov cr8, rax
00316B9F  48 8B D3                        mov rdx, rbx
00316BA2  48 8B CD                        mov rcx, rbp
00316BA5  E8 36 02 00 00                  call 0x140316de0
00316BAA  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
00316BAD  A8 04                           test al, 4
00316BAF  0F 85 99 00 00 00               jne 0x140316c4e
00316BB5  90                              nop
00316BB6  66 83 85 E6 01 00 00 01         add word ptr [rbp + 0x1e6], 1
00316BBE  75 12                           jne 0x140316bd2
00316BC0  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
00316BC7  90                              nop
00316BC8  48 39 00                        cmp qword ptr [rax], rax
00316BCB  74 05                           je 0x140316bd2
00316BCD  E8 AE C0 FC FF                  call 0x1402e2c80
00316BD2  0F B6 4B 20                     movzx ecx, byte ptr [rbx + 0x20]
00316BD6  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
00316BD9  48 C1 E1 20                     shl rcx, 0x20
00316BDD  48 0B C8                        or rcx, rax
00316BE0  48 3B F9                        cmp rdi, rcx
00316BE3  0F 82 E3 01 00 00               jb 0x140316dcc
00316BE9  0F B6 4B 21                     movzx ecx, byte ptr [rbx + 0x21]
00316BED  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
00316BF0  48 C1 E1 20                     shl rcx, 0x20
00316BF4  48 0B C8                        or rcx, rax
00316BF7  48 3B F9                        cmp rdi, rcx
00316BFA  0F 87 CC 01 00 00               ja 0x140316dcc
00316C00  49 89 1E                        mov qword ptr [r14], rbx
00316C03  33 C0                           xor eax, eax
00316C05  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00316C0A  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00316C0F  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00316C14  48 83 C4 20                     add rsp, 0x20
00316C18  41 5F                           pop r15
00316C1A  41 5E                           pop r14
00316C1C  41 5D                           pop r13
00316C1E  41 5C                           pop r12
00316C20  5F                              pop rdi
00316C21  C3                              ret
00316C22  CC                              int3
00316C23  0F 0D 0B                        prefetchw byte ptr [rbx]
00316C26  8B 03                           mov eax, dword ptr [rbx]
00316C28  0F BA F0 1F                     btr eax, 0x1f
00316C2C  8D 48 01                        lea ecx, [rax + 1]
00316C2F  F0 0F B1 0B                     lock cmpxchg dword ptr [rbx], ecx
00316C33  0F 84 E8 FD FF FF               je 0x140316a21
00316C39  85 C0                           test eax, eax
00316C3B  79 EF                           jns 0x140316c2c
00316C3D  40 0F B6 D6                     movzx edx, sil
00316C41  48 8B CB                        mov rcx, rbx
00316C44  E8 37 B7 04 00                  call 0x140362380
00316C49  E9 D3 FD FF FF                  jmp 0x140316a21
00316C4E  8B 85 A8 05 00 00               mov eax, dword ptr [rbp + 0x5a8]
00316C54  0F BA F0 0E                     btr eax, 0xe
00316C58  89 85 A8 05 00 00               mov dword ptr [rbp + 0x5a8], eax
00316C5E  33 C9                           xor ecx, ecx
00316C60  B8 11 00 00 00                  mov eax, 0x11
00316C65  F0 48 0F B1 4B 28               lock cmpxchg qword ptr [rbx + 0x28], rcx
00316C6B  0F 85 4D 01 00 00               jne 0x140316dbe
00316C71  48 8D 4B 28                     lea rcx, [rbx + 0x28]
00316C75  E8 86 A9 FC FF                  call 0x1402e1600
00316C7A  90                              nop
00316C7B  66 83 85 E6 01 00 00 01         add word ptr [rbp + 0x1e6], 1
00316C83  75 12                           jne 0x140316c97
00316C85  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
00316C8C  90                              nop
00316C8D  48 39 00                        cmp qword ptr [rax], rax
00316C90  74 05                           je 0x140316c97
00316C92  E8 E9 BF FC FF                  call 0x1402e2c80
00316C97  66 FF 8D E6 01 00 00            dec word ptr [rbp + 0x1e6]
00316C9E  48 8D 4B 28                     lea rcx, [rbx + 0x28]
00316CA2  45 33 C0                        xor r8d, r8d
00316CA5  33 D2                           xor edx, edx
00316CA7  90                              nop
00316CA8  E8 83 95 EF FF                  call 0x140210230
00316CAD  F0 48 0F BA 6B 28 00            lock bts qword ptr [rbx + 0x28], 0
00316CB4  48 8B F0                        mov rsi, rax
00316CB7  73 10                           jae 0x140316cc9
00316CB9  4C 8D 43 28                     lea r8, [rbx + 0x28]
00316CBD  48 8B D0                        mov rdx, rax
00316CC0  48 8D 4B 28                     lea rcx, [rbx + 0x28]
00316CC4  E8 C7 8F EF FF                  call 0x14020fc90
00316CC9  48 85 F6                        test rsi, rsi
00316CCC  74 04                           je 0x140316cd2
00316CCE  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
00316CD2  8B 85 A8 05 00 00               mov eax, dword ptr [rbp + 0x5a8]
00316CD8  48 8B CB                        mov rcx, rbx
00316CDB  0F BA E8 07                     bts eax, 7
00316CDF  89 85 A8 05 00 00               mov dword ptr [rbp + 0x5a8], eax
00316CE5  90                              nop
00316CE6  E8 31 02 00 00                  call 0x140316f1c
00316CEB  48 8B CB                        mov rcx, rbx
00316CEE  E8 6D 01 00 00                  call 0x140316e60
00316CF3  90                              nop
00316CF4  BA 02 00 00 00                  mov edx, 2
00316CF9  66 83 85 E6 01 00 00 01         add word ptr [rbp + 0x1e6], 1
00316D01  0F 85 B8 FC FF FF               jne 0x1403169bf
00316D07  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
00316D0E  90                              nop
00316D0F  48 39 00                        cmp qword ptr [rax], rax
00316D12  0F 84 A7 FC FF FF               je 0x1403169bf
00316D18  E8 63 BF FC FF                  call 0x1402e2c80
00316D1D  E9 98 FC FF FF                  jmp 0x1403169ba
00316D22  B2 02                           mov dl, 2
00316D24  40 0F B6 CE                     movzx ecx, sil
00316D28  E8 CF E9 1D 00                  call 0x1404f56fc
00316D2D  E9 C8 FC FF FF                  jmp 0x1403169fa
00316D32  49 8B C8                        mov rcx, r8
00316D35  E8 56 38 F3 FF                  call 0x14024a590
00316D3A  E9 60 FE FF FF                  jmp 0x140316b9f
00316D3F  40 0F B6 D6                     movzx edx, sil
00316D43  33 C9                           xor ecx, ecx
00316D45  E8 D6 02 F8 FF                  call 0x140297020
00316D4A  90                              nop
00316D4B  66 83 85 E6 01 00 00 01         add word ptr [rbp + 0x1e6], 1
00316D53  75 12                           jne 0x140316d67
00316D55  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
00316D5C  90                              nop
00316D5D  48 39 00                        cmp qword ptr [rax], rax
00316D60  74 05                           je 0x140316d67
00316D62  E8 19 BF FC FF                  call 0x1402e2c80
00316D67  33 C0                           xor eax, eax
00316D69  49 89 06                        mov qword ptr [r14], rax
00316D6C  B8 0A 01 00 C0                  mov eax, 0xc000010a
00316D71  E9 8F FE FF FF                  jmp 0x140316c05
00316D76  49 8B C8                        mov rcx, r8
00316D79  E8 A6 04 F8 FF                  call 0x140297224
00316D7E  48 85 C0                        test rax, rax
00316D81  0F 84 3D FD FF FF               je 0x140316ac4
00316D87  0F B6 58 20                     movzx ebx, byte ptr [rax + 0x20]
00316D8B  8B 40 18                        mov eax, dword ptr [rax + 0x18]
00316D8E  48 C1 E3 20                     shl rbx, 0x20
00316D92  48 0B D8                        or rbx, rax
00316D95  48 C1 E3 0C                     shl rbx, 0xc
00316D99  E9 30 FD FF FF                  jmp 0x140316ace
00316D9E  8B 05 B4 70 BF 00               mov eax, dword ptr [rip + 0xbf70b4]
00316DA4  85 C0                           test eax, eax
00316DA6  0F 85 C9 FD FF FF               jne 0x140316b75
00316DAC  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00316DB1  49 8B C8                        mov rcx, r8
00316DB4  E8 8F A1 FD FF                  call 0x1402f0f48
00316DB9  E9 C3 FD FF FF                  jmp 0x140316b81
00316DBE  48 8D 4B 28                     lea rcx, [rbx + 0x28]
00316DC2  E8 79 C6 F4 FF                  call 0x140263440
00316DC7  E9 A5 FE FF FF                  jmp 0x140316c71
00316DCC  48 8B CB                        mov rcx, rbx
00316DCF  E8 3C 81 F9 FF                  call 0x1402aef10
00316DD4  E9 E1 FB FF FF                  jmp 0x1403169ba
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReturnLockedVadOrNextVa(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rdi = 0;
    *(unsigned __int64 *)(a3) = 0;
loc_003169BA:
loc_003169BF:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040)) + (0x3ECULL);
    if ((*(unsigned int *)(v_rip + 13304620)) != 0) goto loc_00316D22;
loc_003169FA:
    if (((*(unsigned __int8 *)(v_rip + 13304069)) & (33)) == 0) goto loc_00316C23;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12547147))) != 0) goto loc_00316C23;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(v_rbx, (unsigned __int8)(v_cr8), a3, a4);
loc_00316A21:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 500)))) & (32)) != 0) goto loc_00316D3F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) == 0) goto loc_00316AC4;
    v_rdi = (a1) >> (12);
loc_00316A47:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) == 0) goto loc_00316AC4;
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 32)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 24)));
    if (v_rdi < a2) goto loc_00316A80;
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 28)));
    if (v_rdi <= a1) goto loc_00316AB3;
    if (v_rdi < a2) goto loc_00316A80;
    goto loc_00316A83;
loc_00316A80:
loc_00316A83:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368)) != 0) goto loc_00316A47;
    result = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 32)))) << (32);
    result = (result) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 24)));
    if (result < v_rdi) goto loc_00316D76;
    v_rbx = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 32)) << (32);
    v_rbx = (v_rbx) | ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368) + 24)));
    v_rbx = (v_rbx) << (12);
    goto loc_00316ACE;
loc_00316AB3:
    if (condition_is_not_equal) goto loc_00316B40;
loc_00316AC4:
loc_00316ACE:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040)) + (0x3ECULL);
    result = ExReleaseSpinLockSharedFromDpcLevel(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), a4);
    if (((unsigned __int8)(v_cr8)) == 17) goto loc_00316B15;
    if ((*(unsigned int *)(v_rip + 13304354)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), a4);
    }
loc_00316B15:
    if ((*(unsigned int *)(v_rip + 13304354)) != 0) goto loc_00316B32;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1368), a4);
    }
    result = 0;
    *(unsigned __int64 *)(a3) = v_rbx;
    *(unsigned __int64 *)(a2) = 0;
    goto loc_00316C05;
loc_00316B40:
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040)) + (0x3ECULL);
    if (((unsigned __int8)(v_cr8)) == 17) goto loc_00316D32;
    if (((*(unsigned __int8 *)(v_rip + 13303703)) & (1)) != 0) goto loc_00316D9E;
loc_00316B75:
loc_00316B81:
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned int *)(v_rip + 13304216)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_00316B9F:
    result = MiLockVadShared(*(unsigned __int64 *)(gs_base + (0 + 392)), v_rbx, a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 48)))) & (4)) != 0) goto loc_00316C4E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 48)))) & (4)) != 0) goto loc_00316BD2;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(gs_base + (0 + 392)), v_rbx, a3, a4);
    }
    a1 = (*(unsigned __int8 *)(v_rbx + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(v_rbx + 24)));
    if (v_rdi < a1) goto loc_00316DCC;
    a1 = (*(unsigned __int8 *)(v_rbx + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(v_rbx + 28)));
    if (v_rdi > a1) goto loc_00316DCC;
    *(unsigned __int64 *)(a2) = v_rbx;
    result = 0;
loc_00316C05:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00316C23:
loc_00316C2C:
    if (condition_is_equal) goto loc_00316A21;
    if (!sign_flag) goto loc_00316C2C;
    result = ExpWaitForSpinLockSharedAndAcquire(v_stack_p8, (unsigned __int8)(v_stack_p20), a3, a4);
    goto loc_00316A21;
loc_00316C4E:
    *(unsigned int *)(v_stack_p10 + 1448) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 1448)));
    a1 = 0;
    if (condition_is_not_equal) goto loc_00316DBE;
loc_00316C71:
    result = KeAbPostRelease(v_stack_p8 + 40, (unsigned __int8)(v_stack_p20), a3, a4);
    if (condition_is_not_equal) goto loc_00316C97;
    result = v_stack_p10 + 152;
    if ((*(unsigned __int64 *)(v_stack_p10 + 152)) != (v_stack_p10 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_p8 + 40, (unsigned __int8)(v_stack_p20), a3, a4);
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_p8 + 40, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_stack_p8 + 40;
        a2 = result;
        a1 = v_stack_p8 + 40;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned int *)(v_stack_p10 + 1448) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + 1448)));
    result = MiWaitForVadDeletion(v_stack_p8, a2, a3, a4);
    result = MiUnlockAndDereferenceVad(v_stack_p8, a2, a3, a4);
    if (result != 0) goto loc_003169BF;
    if ((*(unsigned __int64 *)(v_stack_p10 + 152)) == (v_stack_p10 + 152)) goto loc_003169BF;
    result = KiCheckForKernelApcDelivery(v_stack_p8, 2, a3, a4);
    goto loc_003169BA;
loc_00316D22:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(result), 2, a3, a4);
    goto loc_003169FA;
loc_00316D32:
    result = ExReleaseSpinLockSharedFromDpcLevel(a3, 2, a3, a4);
    goto loc_00316B9F;
loc_00316D3F:
    a1 = 0;
    result = MiUnlockVadTree(a1, (unsigned __int8)(result), a3, a4);
    if (condition_is_not_equal) goto loc_00316D67;
    result = v_stack_p10 + 152;
    if ((*(unsigned __int64 *)(v_stack_p10 + 152)) != (v_stack_p10 + 152)) {
        result = KiCheckForKernelApcDelivery(a1, (unsigned __int8)(result), a3, a4);
    }
    result = 0;
    *(unsigned __int64 *)(a2) = 0;
    goto loc_00316C05;
loc_00316D76:
    result = MiGetNextVad(a3, (unsigned __int8)(result), a3, a4);
    if (result == 0) goto loc_00316AC4;
    v_rbx = (*(unsigned __int8 *)(result + 32)) << (32);
    v_rbx = (v_rbx) | ((unsigned int)(*(unsigned int *)(result + 24)));
    v_rbx = (v_rbx) << (12);
    goto loc_00316ACE;
loc_00316D9E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12546228))) != 0) goto loc_00316B75;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(a3, v_stack_p48, a3, a4);
    goto loc_00316B81;
loc_00316DBE:
    result = ExfReleasePushLockShared(v_rbx + 40, v_stack_p48, a3, a4);
    goto loc_00316C71;
loc_00316DCC:
    result = MiUnlockAndDereferenceVadShared(v_rbx, v_stack_p48, a3, a4);
    goto loc_003169BA;
}
```

## 5. (Beta) C Style

```c
int64_t MiReturnLockedVadOrNextVa(int64_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
    *(uint64_t *)(arg3) = 0;
loc_003169BA:
loc_003169BF:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410)) + (0x3ECULL);
    if ((*(uint32_t *)(v_rip + 0xCB032C)) != 0) goto loc_00316D22;
loc_003169FA:
    if (((*(uint8_t *)(v_rip + 0xCB0105)) & (33)) == 0) goto loc_00316C23;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF744B))) != 0) goto loc_00316C23;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(local_rbx, (uint8_t)(v_cr8), Arg3, a4);
loc_00316A21:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1F4)))) & (32)) != 0) goto loc_00316D3F;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) == 0) goto loc_00316AC4;
    local_rdi = (Arg1) >> (12);
loc_00316A47:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) == 0) goto loc_00316AC4;
    Arg2 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x20)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x18)));
    if (local_rdi < Arg2) goto loc_00316A80;
    Arg1 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x1C)));
    if (local_rdi <= Arg1) goto loc_00316AB3;
    if (local_rdi < Arg2) goto loc_00316A80;
    goto loc_00316A83;
loc_00316A80:
loc_00316A83:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558)) != 0) goto loc_00316A47;
    result = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x20)))) << (32);
    result = (result) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x18)));
    if (result < local_rdi) goto loc_00316D76;
    local_rbx = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x20)) << (32);
    local_rbx = (local_rbx) | ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558) + 0x18)));
    local_rbx = (local_rbx) << (12);
    goto loc_00316ACE;
loc_00316AB3:
    if (condition_is_not_equal) goto loc_00316B40;
loc_00316AC4:
loc_00316ACE:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410)) + (0x3ECULL);
    result = ExReleaseSpinLockSharedFromDpcLevel(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), a4);
    if (((uint8_t)(v_cr8)) == 17) goto loc_00316B15;
    if ((*(uint32_t *)(v_rip + 0xCB0222)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), a4);
    }
loc_00316B15:
    if ((*(uint32_t *)(v_rip + 0xCB0222)) != 0) goto loc_00316B32;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x558), a4);
    }
    result = 0;
    *(uint64_t *)(arg3) = local_rbx;
    *(uint64_t *)(arg2) = 0;
    goto loc_00316C05;
loc_00316B40:
    Arg3 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410)) + (0x3ECULL);
    if (((uint8_t)(v_cr8)) == 17) goto loc_00316D32;
    if (((*(uint8_t *)(v_rip + 0xCAFF97)) & (1)) != 0) goto loc_00316D9E;
loc_00316B75:
loc_00316B81:
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint32_t *)(v_rip + 0xCB0198)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, a4);
    }
loc_00316B9F:
    result = MiLockVadShared(*(uint64_t *)(gs_base + (0 + 0x188)), local_rbx, Arg3, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x30)))) & (4)) != 0) goto loc_00316C4E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x30)))) & (4)) != 0) goto loc_00316BD2;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(uint64_t *)(gs_base + (0 + 0x188)), local_rbx, Arg3, a4);
    }
    Arg1 = (*(uint8_t *)(local_rbx + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(local_rbx + 0x18)));
    if (local_rdi < Arg1) goto loc_00316DCC;
    Arg1 = (*(uint8_t *)(local_rbx + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(local_rbx + 0x1C)));
    if (local_rdi > Arg1) goto loc_00316DCC;
    *(uint64_t *)(arg2) = local_rbx;
    result = 0;
loc_00316C05:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00316C23:
loc_00316C2C:
    if (condition_is_equal) goto loc_00316A21;
    if (!sign_flag) goto loc_00316C2C;
    result = ExpWaitForSpinLockSharedAndAcquire(v_stack_p8, (uint8_t)(v_stack_p20), Arg3, a4);
    goto loc_00316A21;
loc_00316C4E:
    *(uint32_t *)(v_stack_p10 + 0x5A8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x5A8)));
    Arg1 = 0;
    if (condition_is_not_equal) goto loc_00316DBE;
loc_00316C71:
    result = KeAbPostRelease(v_stack_p8 + 40, (uint8_t)(v_stack_p20), Arg3, a4);
    if (condition_is_not_equal) goto loc_00316C97;
    result = v_stack_p10 + 152;
    if ((*(uint64_t *)(v_stack_p10 + 0x98)) != (v_stack_p10 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_p8 + 40, (uint8_t)(v_stack_p20), Arg3, a4);
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_p8 + 40, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_stack_p8 + 40;
        Arg2 = result;
        Arg1 = v_stack_p8 + 40;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint32_t *)(v_stack_p10 + 0x5A8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + 0x5A8)));
    result = MiWaitForVadDeletion(v_stack_p8, Arg2, Arg3, a4);
    result = MiUnlockAndDereferenceVad(v_stack_p8, Arg2, Arg3, a4);
    if (result != 0) goto loc_003169BF;
    if ((*(uint64_t *)(v_stack_p10 + 0x98)) == (v_stack_p10 + 152)) goto loc_003169BF;
    result = KiCheckForKernelApcDelivery(v_stack_p8, 2, Arg3, a4);
    goto loc_003169BA;
loc_00316D22:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(result), 2, Arg3, a4);
    goto loc_003169FA;
loc_00316D32:
    result = ExReleaseSpinLockSharedFromDpcLevel(Arg3, 2, Arg3, a4);
    goto loc_00316B9F;
loc_00316D3F:
    Arg1 = 0;
    result = MiUnlockVadTree(Arg1, (uint8_t)(result), Arg3, a4);
    if (condition_is_not_equal) goto loc_00316D67;
    result = v_stack_p10 + 152;
    if ((*(uint64_t *)(v_stack_p10 + 0x98)) != (v_stack_p10 + 152)) {
        result = KiCheckForKernelApcDelivery(Arg1, (uint8_t)(result), Arg3, a4);
    }
    result = 0;
    *(uint64_t *)(arg2) = 0;
    goto loc_00316C05;
loc_00316D76:
    result = MiGetNextVad(Arg3, (uint8_t)(result), Arg3, a4);
    if (result == 0) goto loc_00316AC4;
    local_rbx = (*(uint8_t *)(result + 0x20)) << (32);
    local_rbx = (local_rbx) | ((uint32_t)(*(uint32_t *)(result + 0x18)));
    local_rbx = (local_rbx) << (12);
    goto loc_00316ACE;
loc_00316D9E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF70B4))) != 0) goto loc_00316B75;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(Arg3, v_stack_p48, Arg3, a4);
    goto loc_00316B81;
loc_00316DBE:
    result = ExfReleasePushLockShared(local_rbx + 40, v_stack_p48, Arg3, a4);
    goto loc_00316C71;
loc_00316DCC:
    result = MiUnlockAndDereferenceVadShared(local_rbx, v_stack_p48, Arg3, a4);
    goto loc_003169BA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00316980&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
