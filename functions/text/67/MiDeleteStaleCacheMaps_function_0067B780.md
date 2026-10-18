# MiDeleteStaleCacheMaps

- RVA: `0x0067B780`–`0x0067BC1E` (길이 `1,182` bytes)
- VA: `0x000000014067B780`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00085920`
- 디코드: `334`개 명령, `1,182/1,182` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0067B7F7` → [MiLockIoPfnTree](../2A/MiLockIoPfnTree_function_002AC8A4.md) (function, `0x002AC8A4`)
- `0x0067B8D8` → [MiConvertIoPfnTreeLockExclusiveToShared](../4C/MiConvertIoPfnTreeLockExclusiveToShared_function_004CEEC8.md) (function, `0x004CEEC8`)
- `0x0067B91B` → [MiIoPfnTreeLockContended](../49/MiIoPfnTreeLockContended_function_0049D06C.md) (function, `0x0049D06C`)
- `0x0067B92E` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x0067B956` → [MiIsPageInHugePfn](../2A/MiIsPageInHugePfn_function_002AB770.md) (function, `0x002AB770`)
- `0x0067B967` → [MiFlushEntireTbDueToAttributeChange](../30/MiFlushEntireTbDueToAttributeChange_function_00308AE0.md) (function, `0x00308AE0`)
- `0x0067B98A` → [MiTbFlushTimeStampMayNeedFlush](../45/MiTbFlushTimeStampMayNeedFlush_function_004584B8.md) (function, `0x004584B8`)
- `0x0067B996` → [MiFlushStaleCacheMap](MiFlushStaleCacheMap_function_0067BCB0.md) (function, `0x0067BCB0`)
- `0x0067B9BC` → [RtlAvlRemoveNode](../29/RtlAvlRemoveNode_function_00296650.md) (function, `0x00296650`)
- `0x0067B9C5` → [MiIsPageInIoHugeRangeTransition](../2A/MiIsPageInIoHugeRangeTransition_function_002AB7A0.md) (function, `0x002AB7A0`)
- `0x0067BA4B` → [MiIoPfnTreeLockContended](../49/MiIoPfnTreeLockContended_function_0049D06C.md) (function, `0x0049D06C`)
- `0x0067BA5E` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x0067BA79` → [MiUnlockIoPfnTree](../2A/MiUnlockIoPfnTree_function_002AC7F8.md) (function, `0x002AC7F8`)
- `0x0067BAA7` → [MiUnlockIoPfnTree](../2A/MiUnlockIoPfnTree_function_002AC7F8.md) (function, `0x002AC7F8`)
- `0x0067BAAE` → [MiLockIoPfnTree](../2A/MiLockIoPfnTree_function_002AC8A4.md) (function, `0x002AC8A4`)
- `0x0067BACB` → [MiUnlockIoPfnTree](../2A/MiUnlockIoPfnTree_function_002AC7F8.md) (function, `0x002AC7F8`)
- `0x0067BB46` → [MiUnlockIoPfnTree](../2A/MiUnlockIoPfnTree_function_002AC7F8.md) (function, `0x002AC7F8`)
- `0x0067BB9A` → [MiDereferenceIoHugeRange](MiDereferenceIoHugeRange_function_006753F8.md) (function, `0x006753F8`)
- `0x0067BBA4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0067BBB5` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0067BBE8` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0067BC07` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0067B79D` → RVA `0x00010850` (`.rdata`; read)
- `0x0067B7AD` → RVA `0x00E372A0` (`.data`; read)
- `0x0067B800` → RVA `0x00E37290` (`.data`; read)
- `0x0067BADF` → RVA `0x00FCF240` (`CACHEALI`; read)
- `0x0067BB64` → RVA `0x00E37320` (`.data`; read)
- `0x0067BBAB` → RVA `0x00E37310` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0067BBA4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0067B780  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0067B785  55                              push rbp
0067B786  53                              push rbx
0067B787  56                              push rsi
0067B788  57                              push rdi
0067B789  41 54                           push r12
0067B78B  41 55                           push r13
0067B78D  41 56                           push r14
0067B78F  41 57                           push r15
0067B791  48 8B EC                        mov rbp, rsp
0067B794  48 83 EC 78                     sub rsp, 0x78
0067B798  33 DB                           xor ebx, ebx
0067B79A  8D 73 01                        lea esi, [rbx + 1]
0067B79D  66 0F 6F 05 AB 50 99 FF         movdqa xmm0, xmmword ptr [rip - 0x66af55]
0067B7A5  48 8D 45 B8                     lea rax, [rbp - 0x48]
0067B7A9  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0067B7AD  48 8D 15 EC BA 7B 00            lea rdx, [rip + 0x7bbaec]
0067B7B4  48 8D 45 B8                     lea rax, [rbp - 0x48]
0067B7B8  89 5D A8                        mov dword ptr [rbp - 0x58], ebx
0067B7BB  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0067B7BF  44 8A FB                        mov r15b, bl
0067B7C2  89 5D B0                        mov dword ptr [rbp - 0x50], ebx
0067B7C5  48 8B CB                        mov rcx, rbx
0067B7C8  88 5D 58                        mov byte ptr [rbp + 0x58], bl
0067B7CB  41 B8 02 00 00 00               mov r8d, 2
0067B7D1  88 5D AC                        mov byte ptr [rbp - 0x54], bl
0067B7D4  89 5D 60                        mov dword ptr [rbp + 0x60], ebx
0067B7D7  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
0067B7DB  48 8B 02                        mov rax, qword ptr [rdx]
0067B7DE  48 8D 52 40                     lea rdx, [rdx + 0x40]
0067B7E2  48 89 44 0D E8                  mov qword ptr [rbp + rcx - 0x18], rax
0067B7E7  48 89 44 0D C8                  mov qword ptr [rbp + rcx - 0x38], rax
0067B7EC  48 8D 49 08                     lea rcx, [rcx + 8]
0067B7F0  4C 2B C6                        sub r8, rsi
0067B7F3  75 E6                           jne 0x14067b7db
0067B7F5  8B CE                           mov ecx, esi
0067B7F7  E8 A8 10 C3 FF                  call 0x1402ac8a4
0067B7FC  83 65 B4 00                     and dword ptr [rbp - 0x4c], 0
0067B800  4C 8D 25 89 BA 7B 00            lea r12, [rip + 0x7bba89]
0067B807  45 33 F6                        xor r14d, r14d
0067B80A  88 45 50                        mov byte ptr [rbp + 0x50], al
0067B80D  40 8A F8                        mov dil, al
0067B810  49 8B 4C 24 08                  mov rcx, qword ptr [r12 + 8]
0067B815  48 85 C9                        test rcx, rcx
0067B818  0F 84 03 03 00 00               je 0x14067bb21
0067B81E  4E 8B 6C 35 D8                  mov r13, qword ptr [rbp + r14 - 0x28]
0067B823  4C 3B E9                        cmp r13, rcx
0067B826  76 08                           jbe 0x14067b830
0067B828  4C 8B E9                        mov r13, rcx
0067B82B  4A 89 4C 35 D8                  mov qword ptr [rbp + r14 - 0x28], rcx
0067B830  49 8B 44 24 F8                  mov rax, qword ptr [r12 - 8]
0067B835  48 3D 00 04 00 00               cmp rax, 0x400
0067B83B  73 0D                           jae 0x14067b84a
0067B83D  49 8B 04 24                     mov rax, qword ptr [r12]
0067B841  48 85 C0                        test rax, rax
0067B844  0F 84 D7 02 00 00               je 0x14067bb21
0067B84A  49 8B 5C 24 F0                  mov rbx, qword ptr [r12 - 0x10]
0067B84F  4A 8B 4C 35 C8                  mov rcx, qword ptr [rbp + r14 - 0x38]
0067B854  48 85 DB                        test rbx, rbx
0067B857  0F 84 98 02 00 00               je 0x14067baf5
0067B85D  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0067B861  48 3B C8                        cmp rcx, rax
0067B864  73 05                           jae 0x14067b86b
0067B866  48 8B 03                        mov rax, qword ptr [rbx]
0067B869  EB 0F                           jmp 0x14067b87a
0067B86B  48 05 00 02 00 00               add rax, 0x200
0067B871  48 3B C8                        cmp rcx, rax
0067B874  72 0E                           jb 0x14067b884
0067B876  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0067B87A  48 85 C0                        test rax, rax
0067B87D  74 05                           je 0x14067b884
0067B87F  48 8B D8                        mov rbx, rax
0067B882  EB D9                           jmp 0x14067b85d
0067B884  48 85 DB                        test rbx, rbx
0067B887  0F 84 68 02 00 00               je 0x14067baf5
0067B88D  48 8B 73 08                     mov rsi, qword ptr [rbx + 8]
0067B891  48 8B CB                        mov rcx, rbx
0067B894  48 85 F6                        test rsi, rsi
0067B897  74 18                           je 0x14067b8b1
0067B899  48 8B 0E                        mov rcx, qword ptr [rsi]
0067B89C  48 85 C9                        test rcx, rcx
0067B89F  74 28                           je 0x14067b8c9
0067B8A1  48 8B 01                        mov rax, qword ptr [rcx]
0067B8A4  48 8B F1                        mov rsi, rcx
0067B8A7  48 8B C8                        mov rcx, rax
0067B8AA  48 85 C0                        test rax, rax
0067B8AD  75 F2                           jne 0x14067b8a1
0067B8AF  EB 18                           jmp 0x14067b8c9
0067B8B1  48 8B 73 10                     mov rsi, qword ptr [rbx + 0x10]
0067B8B5  EB 0C                           jmp 0x14067b8c3
0067B8B7  48 39 0E                        cmp qword ptr [rsi], rcx
0067B8BA  74 0D                           je 0x14067b8c9
0067B8BC  48 8B CE                        mov rcx, rsi
0067B8BF  48 8B 76 10                     mov rsi, qword ptr [rsi + 0x10]
0067B8C3  48 83 E6 FC                     and rsi, 0xfffffffffffffffc
0067B8C7  75 EE                           jne 0x14067b8b7
0067B8C9  8B 45 A8                        mov eax, dword ptr [rbp - 0x58]
0067B8CC  85 C0                           test eax, eax
0067B8CE  74 10                           je 0x14067b8e0
0067B8D0  83 C0 FF                        add eax, -1
0067B8D3  89 45 A8                        mov dword ptr [rbp - 0x58], eax
0067B8D6  75 08                           jne 0x14067b8e0
0067B8D8  E8 EB 35 E5 FF                  call 0x1404ceec8
0067B8DD  45 32 FF                        xor r15b, r15b
0067B8E0  83 7B 20 00                     cmp dword ptr [rbx + 0x20], 0
0067B8E4  41 8A FF                        mov dil, r15b
0067B8E7  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0067B8EB  74 5A                           je 0x14067b947
0067B8ED  48 05 00 02 00 00               add rax, 0x200
0067B8F3  4A 89 44 35 C8                  mov qword ptr [rbp + r14 - 0x38], rax
0067B8F8  B8 01 00 00 00                  mov eax, 1
0067B8FD  4C 2B E8                        sub r13, rax
0067B900  4E 89 6C 35 D8                  mov qword ptr [rbp + r14 - 0x28], r13
0067B905  0F 84 08 02 00 00               je 0x14067bb13
0067B90B  8B 5D 60                        mov ebx, dword ptr [rbp + 0x60]
0067B90E  03 D8                           add ebx, eax
0067B910  89 5D 60                        mov dword ptr [rbp + 0x60], ebx
0067B913  F6 C3 0F                        test bl, 0xf
0067B916  75 23                           jne 0x14067b93b
0067B918  41 8A CF                        mov cl, r15b
0067B91B  E8 4C 17 E2 FF                  call 0x14049d06c
0067B920  85 C0                           test eax, eax
0067B922  0F 85 5D 01 00 00               jne 0x14067ba85
0067B928  80 7D 50 11                     cmp byte ptr [rbp + 0x50], 0x11
0067B92C  74 0D                           je 0x14067b93b
0067B92E  E8 AD BA BF FF                  call 0x1402773e0
0067B933  85 C0                           test eax, eax
0067B935  0F 85 4A 01 00 00               jne 0x14067ba85
0067B93B  40 8A 7D 50                     mov dil, byte ptr [rbp + 0x50]
0067B93F  48 8B DE                        mov rbx, rsi
0067B942  E9 3D FF FF FF                  jmp 0x14067b884
0067B947  45 84 FF                        test r15b, r15b
0067B94A  0F 84 68 01 00 00               je 0x14067bab8
0067B950  FF 45 60                        inc dword ptr [rbp + 0x60]
0067B953  48 8B C8                        mov rcx, rax
0067B956  E8 15 FE C2 FF                  call 0x1402ab770
0067B95B  80 7D 58 00                     cmp byte ptr [rbp + 0x58], 0
0067B95F  8B F8                           mov edi, eax
0067B961  75 0D                           jne 0x14067b970
0067B963  85 C0                           test eax, eax
0067B965  75 09                           jne 0x14067b970
0067B967  E8 74 D1 C8 FF                  call 0x140308ae0
0067B96C  C6 45 58 01                     mov byte ptr [rbp + 0x58], 1
0067B970  80 7D AC 00                     cmp byte ptr [rbp - 0x54], 0
0067B974  75 3B                           jne 0x14067b9b1
0067B976  85 FF                           test edi, edi
0067B978  75 37                           jne 0x14067b9b1
0067B97A  40 38 7B 28                     cmp byte ptr [rbx + 0x28], dil
0067B97E  74 31                           je 0x14067b9b1
0067B980  8B 55 B0                        mov edx, dword ptr [rbp - 0x50]
0067B983  41 83 C8 FF                     or r8d, 0xffffffff
0067B987  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
0067B98A  E8 29 CB DD FF                  call 0x1404584b8
0067B98F  84 C0                           test al, al
0067B991  74 1E                           je 0x14067b9b1
0067B993  48 8B CB                        mov rcx, rbx
0067B996  E8 15 03 00 00                  call 0x14067bcb0
0067B99B  8B 4D AC                        mov ecx, dword ptr [rbp - 0x54]
0067B99E  85 C0                           test eax, eax
0067B9A0  0F B6 C9                        movzx ecx, cl
0067B9A3  8D 47 01                        lea eax, [rdi + 1]
0067B9A6  0F 45 C8                        cmovne ecx, eax
0067B9A9  89 7D 60                        mov dword ptr [rbp + 0x60], edi
0067B9AC  89 4D AC                        mov dword ptr [rbp - 0x54], ecx
0067B9AF  EB 03                           jmp 0x14067b9b4
0067B9B1  8B 7D 60                        mov edi, dword ptr [rbp + 0x60]
0067B9B4  49 8D 4C 24 F0                  lea rcx, [r12 - 0x10]
0067B9B9  48 8B D3                        mov rdx, rbx
0067B9BC  E8 8F AC C1 FF                  call 0x140296650
0067B9C1  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
0067B9C5  E8 D6 FD C2 FF                  call 0x1402ab7a0
0067B9CA  85 C0                           test eax, eax
0067B9CC  74 05                           je 0x14067b9d3
0067B9CE  F0 49 FF 0C 24                  lock dec qword ptr [r12]
0067B9D3  48 83 C9 FF                     or rcx, 0xffffffffffffffff
0067B9D7  F0 49 0F C1 4C 24 F8            lock xadd qword ptr [r12 - 8], rcx
0067B9DE  F0 49 FF 4C 24 08               lock dec qword ptr [r12 + 8]
0067B9E4  48 8D 55 B8                     lea rdx, [rbp - 0x48]
0067B9E8  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
0067B9EC  48 FF C9                        dec rcx
0067B9EF  48 39 50 08                     cmp qword ptr [rax + 8], rdx
0067B9F3  0F 85 F9 01 00 00               jne 0x14067bbf2
0067B9F9  48 89 03                        mov qword ptr [rbx], rax
0067B9FC  48 8D 55 B8                     lea rdx, [rbp - 0x48]
0067BA00  48 89 53 08                     mov qword ptr [rbx + 8], rdx
0067BA04  48 89 58 08                     mov qword ptr [rax + 8], rbx
0067BA08  48 89 5D B8                     mov qword ptr [rbp - 0x48], rbx
0067BA0C  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0067BA10  48 05 00 02 00 00               add rax, 0x200
0067BA16  4A 89 44 35 C8                  mov qword ptr [rbp + r14 - 0x38], rax
0067BA1B  48 81 F9 00 03 00 00            cmp rcx, 0x300
0067BA22  0F 86 F0 00 00 00               jbe 0x14067bb18
0067BA28  49 83 ED 01                     sub r13, 1
0067BA2C  4E 89 6C 35 D8                  mov qword ptr [rbp + r14 - 0x28], r13
0067BA31  0F 84 E1 00 00 00               je 0x14067bb18
0067BA37  40 F6 C7 0F                     test dil, 0xf
0067BA3B  48 8B DE                        mov rbx, rsi
0067BA3E  40 8A 7D 50                     mov dil, byte ptr [rbp + 0x50]
0067BA42  0F 85 3C FE FF FF               jne 0x14067b884
0067BA48  41 8A CF                        mov cl, r15b
0067BA4B  E8 1C 16 E2 FF                  call 0x14049d06c
0067BA50  85 C0                           test eax, eax
0067BA52  75 17                           jne 0x14067ba6b
0067BA54  40 80 FF 11                     cmp dil, 0x11
0067BA58  0F 84 26 FE FF FF               je 0x14067b884
0067BA5E  E8 7D B9 BF FF                  call 0x1402773e0
0067BA63  85 C0                           test eax, eax
0067BA65  0F 84 19 FE FF FF               je 0x14067b884
0067BA6B  33 C0                           xor eax, eax
0067BA6D  45 32 FF                        xor r15b, r15b
0067BA70  40 8A CF                        mov cl, dil
0067BA73  89 45 A8                        mov dword ptr [rbp - 0x58], eax
0067BA76  8D 50 02                        lea edx, [rax + 2]
0067BA79  E8 7A 0D C3 FF                  call 0x1402ac7f8
0067BA7E  BE 01 00 00 00                  mov esi, 1
0067BA83  EB 27                           jmp 0x14067baac
0067BA85  45 84 FF                        test r15b, r15b
0067BA88  74 08                           je 0x14067ba92
0067BA8A  45 32 FF                        xor r15b, r15b
0067BA8D  33 C0                           xor eax, eax
0067BA8F  89 45 A8                        mov dword ptr [rbp - 0x58], eax
0067BA92  40 F6 DF                        neg dil
0067BA95  BE 01 00 00 00                  mov esi, 1
0067BA9A  40 8A 7D 50                     mov dil, byte ptr [rbp + 0x50]
0067BA9E  1B D2                           sbb edx, edx
0067BAA0  40 8A CF                        mov cl, dil
0067BAA3  F7 DA                           neg edx
0067BAA5  03 D6                           add edx, esi
0067BAA7  E8 4C 0D C3 FF                  call 0x1402ac7f8
0067BAAC  8B CE                           mov ecx, esi
0067BAAE  E8 F1 0D C3 FF                  call 0x1402ac8a4
0067BAB3  E9 58 FD FF FF                  jmp 0x14067b810
0067BAB8  40 8A 7D 50                     mov dil, byte ptr [rbp + 0x50]
0067BABC  BE 01 00 00 00                  mov esi, 1
0067BAC1  8B D6                           mov edx, esi
0067BAC3  4A 89 44 35 C8                  mov qword ptr [rbp + r14 - 0x38], rax
0067BAC8  40 8A CF                        mov cl, dil
0067BACB  E8 28 0D C3 FF                  call 0x1402ac7f8
0067BAD0  44 8A FE                        mov r15b, sil
0067BAD3  C7 45 A8 40 00 00 00            mov dword ptr [rbp - 0x58], 0x40
0067BADA  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0067BADF  8B 05 5B 37 95 00               mov eax, dword ptr [rip + 0x95375b]
0067BAE5  8D 4E 01                        lea ecx, [rsi + 1]
0067BAE8  89 45 B0                        mov dword ptr [rbp - 0x50], eax
0067BAEB  C6 45 AC 00                     mov byte ptr [rbp - 0x54], 0
0067BAEF  C6 45 58 00                     mov byte ptr [rbp + 0x58], 0
0067BAF3  EB B9                           jmp 0x14067baae
0067BAF5  4A 83 7C 35 E8 00               cmp qword ptr [rbp + r14 - 0x18], 0
0067BAFB  BE 01 00 00 00                  mov esi, 1
0067BB00  74 1F                           je 0x14067bb21
0067BB02  4A 83 64 35 C8 00               and qword ptr [rbp + r14 - 0x38], 0
0067BB08  4A 83 64 35 E8 00               and qword ptr [rbp + r14 - 0x18], 0
0067BB0E  E9 FD FC FF FF                  jmp 0x14067b810
0067BB13  48 8B F0                        mov rsi, rax
0067BB16  EB 05                           jmp 0x14067bb1d
0067BB18  BE 01 00 00 00                  mov esi, 1
0067BB1D  40 8A 7D 50                     mov dil, byte ptr [rbp + 0x50]
0067BB21  8B 4D B4                        mov ecx, dword ptr [rbp - 0x4c]
0067BB24  49 83 C4 40                     add r12, 0x40
0067BB28  03 CE                           add ecx, esi
0067BB2A  49 83 C6 08                     add r14, 8
0067BB2E  89 4D B4                        mov dword ptr [rbp - 0x4c], ecx
0067BB31  83 F9 02                        cmp ecx, 2
0067BB34  0F 8C D6 FC FF FF               jl 0x14067b810
0067BB3A  41 F6 DF                        neg r15b
0067BB3D  40 8A CF                        mov cl, dil
0067BB40  1B D2                           sbb edx, edx
0067BB42  F7 DA                           neg edx
0067BB44  03 D6                           add edx, esi
0067BB46  E8 AD 0C C3 FF                  call 0x1402ac7f8
0067BB4B  48 8D 0D 4E B7 7B 00            lea rcx, [rip + 0x7bb74e]
0067BB52  48 8D 55 C8                     lea rdx, [rbp - 0x38]
0067BB56  48 8B 02                        mov rax, qword ptr [rdx]
0067BB59  48 8D 52 08                     lea rdx, [rdx + 8]
0067BB5D  48 89 01                        mov qword ptr [rcx], rax
0067BB60  48 83 C1 40                     add rcx, 0x40
0067BB64  48 8D 05 B5 B7 7B 00            lea rax, [rip + 0x7bb7b5]
0067BB6B  48 3B C8                        cmp rcx, rax
0067BB6E  7C E6                           jl 0x14067bb56
0067BB70  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
0067BB74  48 8D 45 B8                     lea rax, [rbp - 0x48]
0067BB78  48 3B D8                        cmp rbx, rax
0067BB7B  74 2E                           je 0x14067bbab
0067BB7D  48 8B 0B                        mov rcx, qword ptr [rbx]
0067BB80  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
0067BB84  75 6C                           jne 0x14067bbf2
0067BB86  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0067BB8A  48 39 18                        cmp qword ptr [rax], rbx
0067BB8D  75 63                           jne 0x14067bbf2
0067BB8F  48 89 08                        mov qword ptr [rax], rcx
0067BB92  48 89 41 08                     mov qword ptr [rcx + 8], rax
0067BB96  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
0067BB9A  E8 59 98 FF FF                  call 0x1406753f8
0067BB9F  33 D2                           xor edx, edx
0067BBA1  48 8B CB                        mov rcx, rbx
0067BBA4  E8 C7 6C 50 00                  call 0x140b82870
0067BBA9  EB C5                           jmp 0x14067bb70
0067BBAB  4C 8D 35 5E B7 7B 00            lea r14, [rip + 0x7bb75e]
0067BBB2  49 8B CE                        mov rcx, r14
0067BBB5  E8 D6 CA BC FF                  call 0x140248690
0067BBBA  48 8D 0D CF B6 7B 00            lea rcx, [rip + 0x7bb6cf]
0067BBC1  33 DB                           xor ebx, ebx
0067BBC3  49 3B CE                        cmp rcx, r14
0067BBC6  7D 31                           jge 0x14067bbf9
0067BBC8  48 8B 41 F8                     mov rax, qword ptr [rcx - 8]
0067BBCC  48 3D 00 04 00 00               cmp rax, 0x400
0067BBD2  73 0E                           jae 0x14067bbe2
0067BBD4  48 8B 01                        mov rax, qword ptr [rcx]
0067BBD7  48 85 C0                        test rax, rax
0067BBDA  75 06                           jne 0x14067bbe2
0067BBDC  48 83 C1 40                     add rcx, 0x40
0067BBE0  EB E1                           jmp 0x14067bbc3
0067BBE2  40 8A D7                        mov dl, dil
0067BBE5  49 8B CE                        mov rcx, r14
0067BBE8  E8 D3 C6 BC FF                  call 0x1402482c0
0067BBED  E9 AB FB FF FF                  jmp 0x14067b79d
0067BBF2  B9 03 00 00 00                  mov ecx, 3
0067BBF7  CD 29                           int 0x29
0067BBF9  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0067BBFD  40 8A D7                        mov dl, dil
0067BC00  49 8B CE                        mov rcx, r14
0067BC03  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
0067BC07  E8 B4 C6 BC FF                  call 0x1402482c0
0067BC0C  48 83 C4 78                     add rsp, 0x78
0067BC10  41 5F                           pop r15
0067BC12  41 5E                           pop r14
0067BC14  41 5D                           pop r13
0067BC16  41 5C                           pop r12
0067BC18  5F                              pop rdi
0067BC19  5E                              pop rsi
0067BC1A  5B                              pop rbx
0067BC1B  5D                              pop rbp
0067BC1C  C3                              ret
0067BC1D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeleteStaleCacheMaps(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int8 v_stack_m94;
    unsigned int v_stack_m98;
    unsigned int v_stack_mB8;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (120);
    v_rbx = 0;
loc_0067B79D:
    v_stack_m80 = v_stack_m88;
    v_stack_m98 = 0;
    v_stack_m88 = v_stack_m88;
    v_stack_m90 = 0;
    v_stack_p18 = 0;
    v_stack_m94 = 0;
    v_stack_p20 = 0;
    v_stack_m68 = v_xmm0;
loc_0067B7DB:
    *(unsigned __int64 *)(v_rsp + 0 * 1 - 24) = *(unsigned __int64 *)(v_rip + 8108780);
    *(unsigned __int64 *)(v_rsp + 0 * 1 - 56) = *(unsigned __int64 *)(v_rip + 8108780);
    a3 = (2) - (v_rbx + 1);
    if (condition_is_not_equal) goto loc_0067B7DB;
    result = MiLockIoPfnTree((unsigned int)((unsigned int)(v_rbx + 1)), v_rip + 8108780 + 64, a3, a4);
    v_r14 = 0;
    v_stack_p10 = (unsigned __int8)(result);
loc_0067B810:
    if (*(unsigned __int64 *)(v_rip + 8108681 + 8) == 0) goto loc_0067BB21;
    v_r13 = *(unsigned __int64 *)(v_rsp + v_r14 * 1 - 40);
    if ((*(unsigned __int64 *)(v_rsp + v_r14 * 1 - 40)) >= = (*(unsigned __int64 *)(v_rip + 8108681 + 8))) {
        v_r13 = *(unsigned __int64 *)(v_rip + 8108681 + 8);
        *(unsigned __int64 *)(v_rsp + v_r14 * 1 - 40) = *(unsigned __int64 *)(v_rip + 8108681 + 8);
    }
    if ((*(unsigned __int64 *)(v_rip + 8108681 - 8)) >= 0x400ULL) goto loc_0067B84A;
    if (*(unsigned __int64 *)(v_rip + 8108681) == 0) goto loc_0067BB21;
loc_0067B84A:
    if (*(unsigned __int64 *)(v_rip + 8108681 - 16) == 0) goto loc_0067BAF5;
loc_0067B85D:
    if ((*(unsigned __int64 *)(v_rsp + v_r14 * 1 - 56)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16) + 24))) goto loc_0067B86B;
    goto loc_0067B87A;
loc_0067B86B:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16))) + (512);
    if ((*(unsigned __int64 *)(v_rsp + v_r14 * 1 - 56)) < result) goto loc_0067B884;
loc_0067B87A:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16) + 8) == 0) goto loc_0067B884;
    goto loc_0067B85D;
loc_0067B884:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16) + 8) == 0) goto loc_0067BAF5;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16) + 8) + 8) == 0) goto loc_0067B8B1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16) + 8) + 8)) == 0) goto loc_0067B8C9;
loc_0067B8A1:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16) + 8) + 8))) != 0) goto loc_0067B8A1;
    goto loc_0067B8C9;
loc_0067B8B1:
    goto loc_0067B8C3;
loc_0067B8B7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16) + 8) + 16))) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16) + 8) + 8))))) goto loc_0067B8C9;
loc_0067B8C3:
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16) + 8) + 16) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_0067B8B7;
loc_0067B8C9:
    if ((unsigned int)((unsigned int)(v_stack_m98)) == 0) goto loc_0067B8E0;
    result = (unsigned int)(((unsigned int)(v_stack_m98)) + (-1));
    v_stack_m98 = (unsigned int)(result);
    v_r15 = 0;
    if (!(condition_is_not_equal)) {
        result = MiConvertIoPfnTreeLockExclusiveToShared(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16) + 8) + 16), v_rip + 8108780 + 64, a3, a4);
        v_r15 = 0;
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16) + 8) + 32)) == 0) goto loc_0067B947;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8108681 - 16) + 8) + 24)) + (512);
    *(unsigned __int64 *)(v_rsp + v_r14 * 1 - 56) = result;
    v_r13 = (v_r13) - (1);
    *(unsigned __int64 *)(v_rsp + v_r14 * 1 - 40) = v_r13;
    if (condition_is_equal) goto loc_0067BB13;
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p20)) + (1));
    v_stack_p20 = (unsigned int)(v_rbx);
    if ((((unsigned __int8)(v_rbx)) & (15)) != 0) goto loc_0067B93B;
    result = MiIoPfnTreeLockContended(0, v_rip + 8108780 + 64, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0067BA85;
    if (v_stack_p10 == 17) goto loc_0067B93B;
    result = KeShouldYieldProcessor(0, v_rip + 8108780 + 64, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0067BA85;
loc_0067B93B:
    goto loc_0067B884;
loc_0067B947:
    if (0 == 0) goto loc_0067BAB8;
    result = MiIsPageInHugePfn(result, v_rip + 8108780 + 64, a3, a4);
    if (v_stack_p18 != 0) goto loc_0067B970;
    if ((unsigned int)(result) == 0) {
        result = MiFlushEntireTbDueToAttributeChange(result, v_rip + 8108780 + 64, a3, a4);
        v_stack_p18 = 1;
    }
    if (v_stack_m94 != 0) goto loc_0067B9B1;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_0067B9B1;
    if ((*(unsigned __int8 *)(v_rsi + 40)) == ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_0067B9B1;
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    result = MiTbFlushTimeStampMayNeedFlush((unsigned int)(*(unsigned int *)(v_rsi + 36)), (unsigned int)(v_stack_m90), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0067B9B1;
    result = MiFlushStaleCacheMap(v_rsi, (unsigned int)(v_stack_m90), a3, a4);
    a1 = (unsigned __int8)((unsigned int)(v_stack_m94));
    if ((unsigned int)(result) != 0) { a1 = (unsigned int)((unsigned int)((unsigned int)(result)) + 1); }
    v_stack_p20 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_m94 = (unsigned int)(a1);
    goto loc_0067B9B4;
loc_0067B9B1:
loc_0067B9B4:
    result = RtlAvlRemoveNode(v_rip + 8108681 - 16, v_rsi, a3, a4);
    result = MiIsPageInIoHugeRangeTransition(*(unsigned __int64 *)(v_rsi + 24), v_rsi, a3, a4);
    if ((unsigned int)(result) != 0) {
    }
    a1 = (*(unsigned __int64 *)(v_rsi + 24)) | (-1);
    a1 = (a1) - 1;
    if ((*(unsigned __int64 *)(v_stack_m88 + 8)) != v_stack_m88) goto loc_0067BBF2;
    *(unsigned __int64 *)(v_rsi) = v_stack_m88;
    *(unsigned __int64 *)(v_rsi + 8) = v_stack_m88;
    *(unsigned __int64 *)(v_stack_m88 + 8) = v_rsi;
    v_stack_m88 = v_rsi;
    result = (*(unsigned __int64 *)(v_rsi + 24)) + (512);
    *(unsigned __int64 *)(v_rsp + v_r14 * 1 - 56) = result;
    if (a1 <= 768) goto loc_0067BB18;
    v_r13 = (v_r13) - (1);
    *(unsigned __int64 *)(v_rsp + v_r14 * 1 - 40) = v_r13;
    if (condition_is_equal) goto loc_0067BB18;
    if ((((unsigned __int8)((unsigned int)(v_stack_p20))) & (15)) != 0) goto loc_0067B884;
    result = MiIoPfnTreeLockContended(0, v_stack_m88, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0067BA6B;
    if (((unsigned __int8)(v_stack_p10)) == 17) goto loc_0067B884;
    result = KeShouldYieldProcessor(0, v_stack_m88, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0067B884;
loc_0067BA6B:
    result = 0;
    v_r15 = 0;
    v_stack_m98 = 0;
    result = MiUnlockIoPfnTree((unsigned __int8)(v_stack_p10), result + 2, a3, a4);
    goto loc_0067BAAC;
loc_0067BA85:
    if (0 != 0) {
        v_r15 = 0;
        result = 0;
        v_stack_m98 = 0;
    }
    v_rdi = (unsigned __int8)(-(v_stack_p10));
    a2 = (unsigned int)(-(result + 2));
    a2 = (unsigned int)((a2) + (1));
    result = MiUnlockIoPfnTree((unsigned __int8)(v_stack_p10), a2, a3, a4);
loc_0067BAAC:
loc_0067BAAE:
    result = MiLockIoPfnTree(1, a2, a3, a4);
    goto loc_0067B810;
loc_0067BAB8:
    *(unsigned __int64 *)(v_rsp + v_r14 * 1 - 56) = result;
    result = MiUnlockIoPfnTree((unsigned __int8)(v_stack_p10), 1, a3, a4);
    v_stack_m98 = 64;
    v_stack_m90 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9779035)));
    v_stack_m94 = 0;
    v_stack_p18 = 0;
    goto loc_0067BAAE;
loc_0067BAF5:
    if ((*(unsigned __int64 *)(v_rsp + v_r14 * 1 - 24)) == 0) goto loc_0067BB21;
    goto loc_0067B810;
loc_0067BB13:
    goto loc_0067BB1D;
loc_0067BB18:
loc_0067BB1D:
loc_0067BB21:
    v_r12 = (v_rip + 8108681) + (64);
    a1 = (unsigned int)(((unsigned int)(v_stack_m8C)) + (1));
    v_r14 = (v_r14) + (8);
    v_stack_m8C = (unsigned int)(a1);
    if (((unsigned int)(a1)) < 2) goto loc_0067B810;
    v_r15 = (unsigned __int8)(-(1));
    a2 = (unsigned int)(-(1));
    a2 = (unsigned int)((a2) + (1));
    result = MiUnlockIoPfnTree((unsigned __int8)(v_stack_p10), a2, a3, a4);
loc_0067BB56:
    *(unsigned __int64 *)(v_rip + 8107854) = *(unsigned __int64 *)(v_stack_m78);
    a1 = (v_rip + 8107854) + (64);
    if (a1 < (v_rip + 8107957)) goto loc_0067BB56;
loc_0067BB70:
    if (v_stack_m88 == v_stack_m88) goto loc_0067BBAB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88) + 8)) != v_stack_m88) goto loc_0067BBF2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88 + 8))) != v_stack_m88) goto loc_0067BBF2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88 + 8)) = *(unsigned __int64 *)(v_stack_m88);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88) + 8) = *(unsigned __int64 *)(v_stack_m88 + 8);
    result = MiDereferenceIoHugeRange(*(unsigned __int64 *)(v_stack_m88 + 24), v_stack_m78 + 8, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m88, a2, a3, a4);
    goto loc_0067BB70;
loc_0067BBAB:
    result = ExAcquireSpinLockExclusive(v_rip + 8107870, a2, a3, a4);
    v_rbx = 0;
loc_0067BBC3:
    if ((v_rip + 8107727) >= (v_rip + 8107870)) goto loc_0067BBF9;
    if ((*(unsigned __int64 *)(v_rip + 8107727 - 8)) >= 0x400ULL) goto loc_0067BBE2;
    if (*(unsigned __int64 *)(v_rip + 8107727) != 0) goto loc_0067BBE2;
    a1 = (v_rip + 8107727) + (64);
    goto loc_0067BBC3;
loc_0067BBE2:
    result = MiReleaseSpinLockExclusive(v_rip + 8107870, (unsigned __int8)(v_stack_p10), a3, a4);
    goto loc_0067B79D;
loc_0067BBF2:
loc_0067BBF9:
    *(unsigned __int64 *)(v_stack_p8 + 24) = 0;
    result = MiReleaseSpinLockExclusive(v_rip + 8107870, (unsigned __int8)(v_stack_p10), a3, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDeleteStaleCacheMaps(int64_t Arg1)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint8_t v_stack_m94;
    uint32_t v_stack_m98;
    uint32_t v_stack_mB8;
    uint8_t v_stack_p10;
    uint8_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (120);
    local_rbx = 0;
loc_0067B79D:
    v_stack_m80 = v_stack_m88;
    v_stack_m98 = 0;
    v_stack_m88 = v_stack_m88;
    v_stack_m90 = 0;
    v_stack_p18 = 0;
    v_stack_m94 = 0;
    v_stack_p20 = 0;
    v_stack_m68 = v_xmm0;
loc_0067B7DB:
    *(uint64_t *)(local_rsp + 0x0 * 1 - 0x18) = *(uint64_t *)(v_rip + 0x7BBAEC);
    *(uint64_t *)(local_rsp + 0x0 * 1 - 0x38) = *(uint64_t *)(v_rip + 0x7BBAEC);
    a3 = (2) - (local_rbx + 1);
    if (condition_is_not_equal) goto loc_0067B7DB;
    result = MiLockIoPfnTree((uint32_t)((uint32_t)(local_rbx + 1)), v_rip + 8108780 + 64, a3, a4);
    local_r14 = 0;
    v_stack_p10 = (uint8_t)(result);
loc_0067B810:
    if (*(uint64_t *)(v_rip + 0x7BBA89 + 0x8) == 0) goto loc_0067BB21;
    local_r13 = *(uint64_t *)(local_rsp + local_r14 * 1 - 0x28);
    if ((*(uint64_t *)(local_rsp + local_r14 * 1 - 0x28)) >= = (*(uint64_t *)(v_rip + 0x7BBA89 + 0x8))) {
        local_r13 = *(uint64_t *)(v_rip + 0x7BBA89 + 0x8);
        *(uint64_t *)(local_rsp + local_r14 * 1 - 0x28) = *(uint64_t *)(v_rip + 0x7BBA89 + 0x8);
    }
    if ((*(uint64_t *)(v_rip + 0x7BBA89 - 0x8)) >= 0x400ULL) goto loc_0067B84A;
    if (*(uint64_t *)(v_rip + 0x7BBA89) == 0) goto loc_0067BB21;
loc_0067B84A:
    if (*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) == 0) goto loc_0067BAF5;
loc_0067B85D:
    if ((*(uint64_t *)(local_rsp + local_r14 * 1 - 0x38)) >= (*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) + 0x18))) goto loc_0067B86B;
    goto loc_0067B87A;
loc_0067B86B:
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10))) + (512);
    if ((*(uint64_t *)(local_rsp + local_r14 * 1 - 0x38)) < result) goto loc_0067B884;
loc_0067B87A:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) + 0x8) == 0) goto loc_0067B884;
    goto loc_0067B85D;
loc_0067B884:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) + 0x8) == 0) goto loc_0067BAF5;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) + 0x8) + 0x8) == 0) goto loc_0067B8B1;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) + 0x8) + 0x8)) == 0) goto loc_0067B8C9;
loc_0067B8A1:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) + 0x8) + 0x8))) != 0) goto loc_0067B8A1;
    goto loc_0067B8C9;
loc_0067B8B1:
    goto loc_0067B8C3;
loc_0067B8B7:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) + 0x8) + 0x10))) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) + 0x8) + 0x8))))) goto loc_0067B8C9;
loc_0067B8C3:
    local_rsi = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) + 0x8) + 0x10) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_0067B8B7;
loc_0067B8C9:
    if ((uint32_t)((uint32_t)(v_stack_m98)) == 0) goto loc_0067B8E0;
    result = (uint32_t)(((uint32_t)(v_stack_m98)) + (-1));
    v_stack_m98 = (uint32_t)(result);
    local_r15 = 0;
    if (!(condition_is_not_equal)) {
        result = MiConvertIoPfnTreeLockExclusiveToShared(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) + 0x8) + 0x10), v_rip + 8108780 + 64, a3, a4);
        local_r15 = 0;
    }
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) + 0x8) + 0x20)) == 0) goto loc_0067B947;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x7BBA89 - 0x10) + 0x8) + 0x18)) + (512);
    *(uint64_t *)(local_rsp + local_r14 * 1 - 0x38) = result;
    local_r13 = (local_r13) - (1);
    *(uint64_t *)(local_rsp + local_r14 * 1 - 0x28) = local_r13;
    if (condition_is_equal) goto loc_0067BB13;
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p20)) + (1));
    v_stack_p20 = (uint32_t)(local_rbx);
    if ((((uint8_t)(local_rbx)) & (15)) != 0) goto loc_0067B93B;
    result = MiIoPfnTreeLockContended(0, v_rip + 8108780 + 64, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_0067BA85;
    if (v_stack_p10 == 17) goto loc_0067B93B;
    result = KeShouldYieldProcessor(0, v_rip + 8108780 + 64, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_0067BA85;
loc_0067B93B:
    goto loc_0067B884;
loc_0067B947:
    if (0 == 0) goto loc_0067BAB8;
    result = MiIsPageInHugePfn(result, v_rip + 8108780 + 64, a3, a4);
    if (v_stack_p18 != 0) goto loc_0067B970;
    if ((uint32_t)(result) == 0) {
        result = MiFlushEntireTbDueToAttributeChange(result, v_rip + 8108780 + 64, a3, a4);
        v_stack_p18 = 1;
    }
    if (v_stack_m94 != 0) goto loc_0067B9B1;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_0067B9B1;
    if ((*(uint8_t *)(local_rsi + 0x28)) == ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_0067B9B1;
    a3 = (uint32_t)((a3) | (0xFFFFFFFFULL));
    result = MiTbFlushTimeStampMayNeedFlush((uint32_t)(*(uint32_t *)(local_rsi + 0x24)), (uint32_t)(v_stack_m90), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0067B9B1;
    result = MiFlushStaleCacheMap(local_rsi, (uint32_t)(v_stack_m90), a3, a4);
    Arg1 = (uint8_t)((uint32_t)(v_stack_m94));
    if ((uint32_t)(result) != 0) { Arg1 = (uint32_t)((uint32_t)((uint32_t)(result)) + 1); }
    v_stack_p20 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_m94 = (uint32_t)(Arg1);
    goto loc_0067B9B4;
loc_0067B9B1:
loc_0067B9B4:
    result = RtlAvlRemoveNode(v_rip + 8108681 - 16, local_rsi, a3, a4);
    result = MiIsPageInIoHugeRangeTransition(*(uint64_t *)(local_rsi + 0x18), local_rsi, a3, a4);
    if ((uint32_t)(result) != 0) {
    }
    Arg1 = (*(uint64_t *)(local_rsi + 0x18)) | (-1);
    Arg1 = (Arg1) - 1;
    if ((*(uint64_t *)(v_stack_m88 + 0x8)) != v_stack_m88) goto loc_0067BBF2;
    *(uint64_t *)(local_rsi) = v_stack_m88;
    *(uint64_t *)(local_rsi + 0x8) = v_stack_m88;
    *(uint64_t *)(v_stack_m88 + 0x8) = local_rsi;
    v_stack_m88 = local_rsi;
    result = (*(uint64_t *)(local_rsi + 0x18)) + (512);
    *(uint64_t *)(local_rsp + local_r14 * 1 - 0x38) = result;
    if (Arg1 <= 768) goto loc_0067BB18;
    local_r13 = (local_r13) - (1);
    *(uint64_t *)(local_rsp + local_r14 * 1 - 0x28) = local_r13;
    if (condition_is_equal) goto loc_0067BB18;
    if ((((uint8_t)((uint32_t)(v_stack_p20))) & (15)) != 0) goto loc_0067B884;
    result = MiIoPfnTreeLockContended(0, v_stack_m88, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_0067BA6B;
    if (((uint8_t)(v_stack_p10)) == 17) goto loc_0067B884;
    result = KeShouldYieldProcessor(0, v_stack_m88, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_0067B884;
loc_0067BA6B:
    result = 0;
    local_r15 = 0;
    v_stack_m98 = 0;
    result = MiUnlockIoPfnTree((uint8_t)(v_stack_p10), result + 2, a3, a4);
    goto loc_0067BAAC;
loc_0067BA85:
    if (0 != 0) {
        local_r15 = 0;
        result = 0;
        v_stack_m98 = 0;
    }
    local_rdi = (uint8_t)(-(v_stack_p10));
    a2 = (uint32_t)(-(result + 2));
    a2 = (uint32_t)((a2) + (1));
    result = MiUnlockIoPfnTree((uint8_t)(v_stack_p10), a2, a3, a4);
loc_0067BAAC:
loc_0067BAAE:
    result = MiLockIoPfnTree(1, a2, a3, a4);
    goto loc_0067B810;
loc_0067BAB8:
    *(uint64_t *)(local_rsp + local_r14 * 1 - 0x38) = result;
    result = MiUnlockIoPfnTree((uint8_t)(v_stack_p10), 1, a3, a4);
    v_stack_m98 = 64;
    v_stack_m90 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x95375B)));
    v_stack_m94 = 0;
    v_stack_p18 = 0;
    goto loc_0067BAAE;
loc_0067BAF5:
    if ((*(uint64_t *)(local_rsp + local_r14 * 1 - 0x18)) == 0) goto loc_0067BB21;
    goto loc_0067B810;
loc_0067BB13:
    goto loc_0067BB1D;
loc_0067BB18:
loc_0067BB1D:
loc_0067BB21:
    local_r12 = (v_rip + 8108681) + (64);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m8C)) + (1));
    local_r14 = (local_r14) + (8);
    v_stack_m8C = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) < 2) goto loc_0067B810;
    local_r15 = (uint8_t)(-(1));
    a2 = (uint32_t)(-(1));
    a2 = (uint32_t)((a2) + (1));
    result = MiUnlockIoPfnTree((uint8_t)(v_stack_p10), a2, a3, a4);
loc_0067BB56:
    *(uint64_t *)(v_rip + 0x7BB74E) = *(uint64_t *)(v_stack_m78);
    Arg1 = (v_rip + 8107854) + (64);
    if (Arg1 < (v_rip + 8107957)) goto loc_0067BB56;
loc_0067BB70:
    if (v_stack_m88 == v_stack_m88) goto loc_0067BBAB;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m88) + 0x8)) != v_stack_m88) goto loc_0067BBF2;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m88 + 0x8))) != v_stack_m88) goto loc_0067BBF2;
    *(uint64_t *)(*(uint64_t *)(v_stack_m88 + 0x8)) = *(uint64_t *)(v_stack_m88);
    *(uint64_t *)(*(uint64_t *)(v_stack_m88) + 0x8) = *(uint64_t *)(v_stack_m88 + 0x8);
    result = MiDereferenceIoHugeRange(*(uint64_t *)(v_stack_m88 + 0x18), v_stack_m78 + 8, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m88, a2, a3, a4);
    goto loc_0067BB70;
loc_0067BBAB:
    result = ExAcquireSpinLockExclusive(v_rip + 8107870, a2, a3, a4);
    local_rbx = 0;
loc_0067BBC3:
    if ((v_rip + 8107727) >= (v_rip + 8107870)) goto loc_0067BBF9;
    if ((*(uint64_t *)(v_rip + 0x7BB6CF - 0x8)) >= 0x400ULL) goto loc_0067BBE2;
    if (*(uint64_t *)(v_rip + 0x7BB6CF) != 0) goto loc_0067BBE2;
    Arg1 = (v_rip + 8107727) + (64);
    goto loc_0067BBC3;
loc_0067BBE2:
    result = MiReleaseSpinLockExclusive(v_rip + 8107870, (uint8_t)(v_stack_p10), a3, a4);
    goto loc_0067B79D;
loc_0067BBF2:
loc_0067BBF9:
    *(uint64_t *)(v_stack_p8 + 0x18) = 0;
    result = MiReleaseSpinLockExclusive(v_rip + 8107870, (uint8_t)(v_stack_p10), a3, a4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0067B780&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
