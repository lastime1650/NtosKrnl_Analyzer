# ExpAddTagForBigPages

- RVA: `0x002EF570`–`0x002EF97F` (길이 `1,039` bytes)
- VA: `0x00000001402EF570`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071AD8`
- 디코드: `240`개 명령, `1,039/1,039` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x002EF5FB` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](../27/ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x002EF6DC` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002EF7C3` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x002EF7D2` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x002EF7F6` → [ExpTryConvertSharedSpinLockExclusiveInstrumented](ExpTryConvertSharedSpinLockExclusiveInstrumented_function_002EF988.md) (function, `0x002EF988`)
- `0x002EF804` → [ExpResizeBigPageTable](ExpResizeBigPageTable_function_002EE1B4.md) (function, `0x002EE1B4`)
- `0x002EF82E` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002EF859` → [ExReleaseSpinLockShared](../2F/ExReleaseSpinLockShared_function_002F0EF0.md) (function, `0x002F0EF0`)
- `0x002EF87D` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x002EF89D` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x002EF8BF` → [ExTryConvertSharedSpinLockExclusive](ExTryConvertSharedSpinLockExclusive_function_002EF4C0.md) (function, `0x002EF4C0`)
- `0x002EF8CE` → [ExpResizeBigPageTable](ExpResizeBigPageTable_function_002EE1B4.md) (function, `0x002EE1B4`)
- `0x002EF8DD` → [ExReleaseSpinLockExclusive](../2C/ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)
- `0x002EF8FB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002EF918` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002EF927` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002EF93B` → [ExReleaseSpinLockShared](../2F/ExReleaseSpinLockShared_function_002F0EF0.md) (function, `0x002F0EF0`)
- `0x002EF96B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [ExAllocateContiguousHeapPool](ExAllocateContiguousHeapPool_function_002EE960.md) at `0x002EEA72`
- [ExInsertPoolTag](ExInsertPoolTag_function_002EF3AC.md) at `0x002EF410`
- [ExAllocateHeapPool](../35/ExAllocateHeapPool_function_0035BA30.md) at `0x0035C158`

### Static image references
- `0x002EF5C9` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002EF5D6` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x002EF5E3` → RVA `0x00F0DE58` (`.data`; read)
- `0x002EF5F4` → RVA `0x00EFACF8` (`.data`; read)
- `0x002EF600` → RVA `0x00EFED30` (`.data`; read)
- `0x002EF607` → RVA `0x00EFED38` (`.data`; read)
- `0x002EF617` → RVA `0x00FCF100` (`CACHEALI`; read)
- `0x002EF691` → RVA `0x00FC7228` (`ALMOSTRO`; read)
- `0x002EF69C` → RVA `0x00FCF100` (`CACHEALI`; read/write)
- `0x002EF6BA` → RVA `0x00EFACF8` (`.data`; read/write)
- `0x002EF770` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002EF814` → RVA `0x00EFACF8` (`.data`; write)
- `0x002EF842` → RVA `0x00EFED24` (`.data`; read/write)
- `0x002EF90A` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x002EF8FB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002EF96B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002EF570  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
002EF575  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
002EF57A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
002EF57F  57                              push rdi
002EF580  41 54                           push r12
002EF582  41 55                           push r13
002EF584  41 56                           push r14
002EF586  41 57                           push r15
002EF588  48 83 EC 20                     sub rsp, 0x20
002EF58C  48 8B C1                        mov rax, rcx
002EF58F  48 C7 44 24 50 00 00 00 00      mov qword ptr [rsp + 0x50], 0
002EF598  48 C1 E8 0C                     shr rax, 0xc
002EF59C  45 33 F6                        xor r14d, r14d
002EF59F  4C 69 D0 5F 9E 00 00            imul r10, rax, 0x9e5f
002EF5A6  4D 8B F9                        mov r15, r9
002EF5A9  4D 8B E0                        mov r12, r8
002EF5AC  49 8B EA                        mov rbp, r10
002EF5AF  44 8B EA                        mov r13d, edx
002EF5B2  48 C1 ED 20                     shr rbp, 0x20
002EF5B6  48 8B F9                        mov rdi, rcx
002EF5B9  49 33 EA                        xor rbp, r10
002EF5BC  B8 02 00 00 00                  mov eax, 2
002EF5C1  44 0F 20 C3                     mov rbx, cr8
002EF5C5  44 0F 22 C0                     mov cr8, rax
002EF5C9  83 3D 50 77 CD 00 00            cmp dword ptr [rip + 0xcd7750], 0
002EF5D0  0F 85 F7 01 00 00               jne 0x1402ef7cd
002EF5D6  F6 05 29 75 CD 00 21            test byte ptr [rip + 0xcd7529], 0x21
002EF5DD  0F 84 B0 01 00 00               je 0x1402ef793
002EF5E3  8B 05 6F E8 C1 00               mov eax, dword ptr [rip + 0xc1e86f]
002EF5E9  85 C0                           test eax, eax
002EF5EB  0F 85 A2 01 00 00               jne 0x1402ef793
002EF5F1  0F B6 D3                        movzx edx, bl
002EF5F4  48 8D 0D FD B6 C0 00            lea rcx, [rip + 0xc0b6fd]
002EF5FB  E8 20 D7 F8 FF                  call 0x14027cd20
002EF600  48 8B 15 29 F7 C0 00            mov rdx, qword ptr [rip + 0xc0f729]
002EF607  4C 8B 05 2A F7 C0 00            mov r8, qword ptr [rip + 0xc0f72a]
002EF60E  48 85 D2                        test rdx, rdx
002EF611  0F 84 11 01 00 00               je 0x1402ef728
002EF617  48 63 05 E2 FA CD 00            movsxd rax, dword ptr [rip + 0xcdfae2]
002EF61E  49 3B C0                        cmp rax, r8
002EF621  0F 84 01 01 00 00               je 0x1402ef728
002EF627  49 8D 48 FF                     lea rcx, [r8 - 1]
002EF62B  4D 8B C8                        mov r9, r8
002EF62E  48 23 CD                        and rcx, rbp
002EF631  49 C1 E1 05                     shl r9, 5
002EF635  8B C9                           mov ecx, ecx
002EF637  48 C1 E1 05                     shl rcx, 5
002EF63B  48 03 CA                        add rcx, rdx
002EF63E  4C 8B D1                        mov r10, rcx
002EF641  4C 03 CA                        add r9, rdx
002EF644  48 8B 01                        mov rax, qword ptr [rcx]
002EF647  A8 01                           test al, 1
002EF649  0F 84 BC 00 00 00               je 0x1402ef70b
002EF64F  F0 48 0F B1 39                  lock cmpxchg qword ptr [rcx], rdi
002EF654  0F 85 B1 00 00 00               jne 0x1402ef70b
002EF65A  0F B6 44 24 78                  movzx eax, byte ptr [rsp + 0x78]
002EF65F  88 41 0C                        mov byte ptr [rcx + 0xc], al
002EF662  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
002EF665  0F B6 D0                        movzx edx, al
002EF668  41 8B C7                        mov eax, r15d
002EF66B  C1 E0 08                        shl eax, 8
002EF66E  33 D0                           xor edx, eax
002EF670  44 89 69 08                     mov dword ptr [rcx + 8], r13d
002EF674  0F B7 44 24 70                  movzx eax, word ptr [rsp + 0x70]
002EF679  81 E2 FF FF 0F 00               and edx, 0xfffff
002EF67F  C1 E0 14                        shl eax, 0x14
002EF682  0B D0                           or edx, eax
002EF684  4C 89 61 10                     mov qword ptr [rcx + 0x10], r12
002EF688  89 51 0C                        mov dword ptr [rcx + 0xc], edx
002EF68B  41 F6 C7 01                     test r15b, 1
002EF68F  74 0B                           je 0x1402ef69c
002EF691  48 33 3D 90 7B CD 00            xor rdi, qword ptr [rip + 0xcd7b90]
002EF698  48 89 79 18                     mov qword ptr [rcx + 0x18], rdi
002EF69C  F0 FF 05 5D FA CD 00            lock inc dword ptr [rip + 0xcdfa5d]
002EF6A3  41 83 FE 10                     cmp r14d, 0x10
002EF6A7  0F 83 FA 01 00 00               jae 0x1402ef8a7
002EF6AD  F6 05 52 74 CD 00 01            test byte ptr [rip + 0xcd7452], 1
002EF6B4  0F 85 A9 01 00 00               jne 0x1402ef863
002EF6BA  F0 81 25 33 B6 C0 00 FF FF FF BF  lock and dword ptr [rip + 0xc0b633], 0xbfffffff
002EF6C5  F0 FF 0D 2C B6 C0 00            lock dec dword ptr [rip + 0xc0b62c]
002EF6CC  83 3D 4D 76 CD 00 00            cmp dword ptr [rip + 0xcd764d], 0
002EF6D3  74 0C                           je 0x1402ef6e1
002EF6D5  44 0F 20 C1                     mov rcx, cr8
002EF6D9  0F B6 D3                        movzx edx, bl
002EF6DC  E8 B7 5F 20 00                  call 0x1404f5698
002EF6E1  0F B6 C3                        movzx eax, bl
002EF6E4  44 0F 22 C0                     mov cr8, rax
002EF6E8  B8 01 00 00 00                  mov eax, 1
002EF6ED  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
002EF6F2  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
002EF6F7  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
002EF6FC  48 83 C4 20                     add rsp, 0x20
002EF700  41 5F                           pop r15
002EF702  41 5E                           pop r14
002EF704  41 5D                           pop r13
002EF706  41 5C                           pop r12
002EF708  5F                              pop rdi
002EF709  C3                              ret
002EF70A  CC                              int3
002EF70B  48 83 C1 20                     add rcx, 0x20
002EF70F  41 FF C6                        inc r14d
002EF712  49 3B C9                        cmp rcx, r9
002EF715  48 8B C2                        mov rax, rdx
002EF718  48 0F 42 C1                     cmovb rax, rcx
002EF71C  48 8B C8                        mov rcx, rax
002EF71F  49 3B C2                        cmp rax, r10
002EF722  0F 85 1C FF FF FF               jne 0x1402ef644
002EF728  33 F6                           xor esi, esi
002EF72A  F6 05 D5 73 CD 00 21            test byte ptr [rip + 0xcd73d5], 0x21
002EF731  0F 85 A5 00 00 00               jne 0x1402ef7dc
002EF737  F0 0F BA 2D B8 B5 C0 00 1F      lock bts dword ptr [rip + 0xc0b5b8], 0x1f
002EF740  0F 82 09 01 00 00               jb 0x1402ef84f
002EF746  8B 0D AC B5 C0 00               mov ecx, dword ptr [rip + 0xc0b5ac]
002EF74C  8B C1                           mov eax, ecx
002EF74E  0F BA F0 1E                     btr eax, 0x1e
002EF752  3D 01 00 00 80                  cmp eax, 0x80000001
002EF757  0F 84 A2 00 00 00               je 0x1402ef7ff
002EF75D  0F BA E1 1E                     bt ecx, 0x1e
002EF761  72 0B                           jb 0x1402ef76e
002EF763  F0 81 0D 8A B5 C0 00 00 00 00 40  lock or dword ptr [rip + 0xc0b58a], 0x40000000
002EF76E  FF C6                           inc esi
002EF770  85 35 36 5B CD 00               test dword ptr [rip + 0xcd5b36], esi
002EF776  0F 84 8E 01 00 00               je 0x1402ef90a
002EF77C  F3 90                           pause
002EF77E  8B 0D 74 B5 C0 00               mov ecx, dword ptr [rip + 0xc0b574]
002EF784  8B C1                           mov eax, ecx
002EF786  0F BA F0 1E                     btr eax, 0x1e
002EF78A  3D 01 00 00 80                  cmp eax, 0x80000001
002EF78F  75 CC                           jne 0x1402ef75d
002EF791  EB 6C                           jmp 0x1402ef7ff
002EF793  0F 0D 0D 5E B5 C0 00            prefetchw byte ptr [rip + 0xc0b55e]
002EF79A  8B 05 58 B5 C0 00               mov eax, dword ptr [rip + 0xc0b558]
002EF7A0  0F BA F0 1F                     btr eax, 0x1f
002EF7A4  8D 48 01                        lea ecx, [rax + 1]
002EF7A7  F0 0F B1 0D 49 B5 C0 00         lock cmpxchg dword ptr [rip + 0xc0b549], ecx
002EF7AF  0F 84 4B FE FF FF               je 0x1402ef600
002EF7B5  85 C0                           test eax, eax
002EF7B7  79 EB                           jns 0x1402ef7a4
002EF7B9  0F B6 D3                        movzx edx, bl
002EF7BC  48 8D 0D 35 B5 C0 00            lea rcx, [rip + 0xc0b535]
002EF7C3  E8 B8 2B 07 00                  call 0x140362380
002EF7C8  E9 33 FE FF FF                  jmp 0x1402ef600
002EF7CD  B2 02                           mov dl, 2
002EF7CF  0F B6 CB                        movzx ecx, bl
002EF7D2  E8 25 5F 20 00                  call 0x1404f56fc
002EF7D7  E9 FA FD FF FF                  jmp 0x1402ef5d6
002EF7DC  8B 05 76 E6 C1 00               mov eax, dword ptr [rip + 0xc1e676]
002EF7E2  85 C0                           test eax, eax
002EF7E4  0F 85 4D FF FF FF               jne 0x1402ef737
002EF7EA  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002EF7EF  48 8D 0D 02 B5 C0 00            lea rcx, [rip + 0xc0b502]
002EF7F6  E8 8D 01 00 00                  call 0x1402ef988
002EF7FB  85 C0                           test eax, eax
002EF7FD  74 50                           je 0x1402ef84f
002EF7FF  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
002EF804  E8 AB E9 FF FF                  call 0x1402ee1b4
002EF809  F6 05 F6 72 CD 00 01            test byte ptr [rip + 0xcd72f6], 1
002EF810  8B F0                           mov esi, eax
002EF812  75 73                           jne 0x1402ef887
002EF814  C7 05 DA B4 C0 00 00 00 00 00   mov dword ptr [rip + 0xc0b4da], 0
002EF81E  83 3D FB 74 CD 00 00            cmp dword ptr [rip + 0xcd74fb], 0
002EF825  74 0C                           je 0x1402ef833
002EF827  44 0F 20 C1                     mov rcx, cr8
002EF82B  0F B6 D3                        movzx edx, bl
002EF82E  E8 65 5E 20 00                  call 0x1404f5698
002EF833  0F B6 C3                        movzx eax, bl
002EF836  44 0F 22 C0                     mov cr8, rax
002EF83A  85 F6                           test esi, esi
002EF83C  0F 85 03 01 00 00               jne 0x1402ef945
002EF842  FF 05 DC F4 C0 00               inc dword ptr [rip + 0xc0f4dc]
002EF848  33 C0                           xor eax, eax
002EF84A  E9 9E FE FF FF                  jmp 0x1402ef6ed
002EF84F  0F B6 D3                        movzx edx, bl
002EF852  48 8D 0D 9F B4 C0 00            lea rcx, [rip + 0xc0b49f]
002EF859  E8 92 16 00 00                  call 0x1402f0ef0
002EF85E  E9 59 FD FF FF                  jmp 0x1402ef5bc
002EF863  8B 05 EF E5 C1 00               mov eax, dword ptr [rip + 0xc1e5ef]
002EF869  85 C0                           test eax, eax
002EF86B  0F 85 49 FE FF FF               jne 0x1402ef6ba
002EF871  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002EF876  48 8D 0D 7B B4 C0 00            lea rcx, [rip + 0xc0b47b]
002EF87D  E8 C6 16 00 00                  call 0x1402f0f48
002EF882  E9 45 FE FF FF                  jmp 0x1402ef6cc
002EF887  8B 0D CB E5 C1 00               mov ecx, dword ptr [rip + 0xc1e5cb]
002EF88D  85 C9                           test ecx, ecx
002EF88F  75 83                           jne 0x1402ef814
002EF891  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002EF896  48 8D 0D 5B B4 C0 00            lea rcx, [rip + 0xc0b45b]
002EF89D  E8 A2 16 FD FF                  call 0x1402c0f44
002EF8A2  E9 77 FF FF FF                  jmp 0x1402ef81e
002EF8A7  49 C1 E8 02                     shr r8, 2
002EF8AB  44 39 05 4E F8 CD 00            cmp dword ptr [rip + 0xcdf84e], r8d
002EF8B2  0F 86 F5 FD FF FF               jbe 0x1402ef6ad
002EF8B8  48 8D 0D 39 B4 C0 00            lea rcx, [rip + 0xc0b439]
002EF8BF  E8 FC FB FF FF                  call 0x1402ef4c0
002EF8C4  83 F8 01                        cmp eax, 1
002EF8C7  75 68                           jne 0x1402ef931
002EF8C9  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
002EF8CE  E8 E1 E8 FF FF                  call 0x1402ee1b4
002EF8D3  0F B6 D3                        movzx edx, bl
002EF8D6  48 8D 0D 1B B4 C0 00            lea rcx, [rip + 0xc0b41b]
002EF8DD  E8 0E 16 FD FF                  call 0x1402c0ef0
002EF8E2  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
002EF8E7  48 85 FF                        test rdi, rdi
002EF8EA  0F 84 F8 FD FF FF               je 0x1402ef6e8
002EF8F0  48 8B 1F                        mov rbx, qword ptr [rdi]
002EF8F3  48 8B CF                        mov rcx, rdi
002EF8F6  33 D2                           xor edx, edx
002EF8F8  48 8B FB                        mov rdi, rbx
002EF8FB  E8 70 2F 89 00                  call 0x140b82870
002EF900  48 85 DB                        test rbx, rbx
002EF903  75 EB                           jne 0x1402ef8f0
002EF905  E9 DE FD FF FF                  jmp 0x1402ef6e8
002EF90A  8B 05 A8 71 CD 00               mov eax, dword ptr [rip + 0xcd71a8]
002EF910  A8 40                           test al, 0x40
002EF912  0F 84 64 FE FF FF               je 0x1402ef77c
002EF918  E8 73 FB 01 00                  call 0x14030f490
002EF91D  84 C0                           test al, al
002EF91F  0F 84 57 FE FF FF               je 0x1402ef77c
002EF925  8B CE                           mov ecx, esi
002EF927  E8 34 FB 01 00                  call 0x14030f460
002EF92C  E9 4D FE FF FF                  jmp 0x1402ef77e
002EF931  0F B6 D3                        movzx edx, bl
002EF934  48 8D 0D BD B3 C0 00            lea rcx, [rip + 0xc0b3bd]
002EF93B  E8 B0 15 00 00                  call 0x1402f0ef0
002EF940  E9 A3 FD FF FF                  jmp 0x1402ef6e8
002EF945  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
002EF94A  B8 02 00 00 00                  mov eax, 2
002EF94F  48 85 F6                        test rsi, rsi
002EF952  0F 84 69 FC FF FF               je 0x1402ef5c1
002EF958  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
002EF960  48 8B 1E                        mov rbx, qword ptr [rsi]
002EF963  48 8B CE                        mov rcx, rsi
002EF966  33 D2                           xor edx, edx
002EF968  48 8B F3                        mov rsi, rbx
002EF96B  E8 00 2F 89 00                  call 0x140b82870
002EF970  48 85 DB                        test rbx, rbx
002EF973  75 EB                           jne 0x1402ef960
002EF975  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
002EF97A  E9 3D FC FF FF                  jmp 0x1402ef5bc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpAddTagForBigPages(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned __int16 a5, unsigned __int8 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_stack_p8 = 0;
    result = (a1) >> (12);
    v_r14 = 0;
    v_r10 = (v_r10) * (result);
    v_rbp = (v_r10) >> (32);
    v_rbp = (v_rbp) ^ (v_r10);
loc_002EF5BC:
loc_002EF5C1:
    if ((*(unsigned int *)(v_rip + 13465424)) != 0) goto loc_002EF7CD;
loc_002EF5D6:
    if (((*(unsigned __int8 *)(v_rip + 13464873)) & (33)) == 0) goto loc_002EF793;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12707951))) != 0) goto loc_002EF793;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(v_rip + 12629757, (unsigned __int8)(v_cr8), a3, a4);
loc_002EF600:
    if (*(unsigned __int64 *)(v_rip + 12646185) == 0) goto loc_002EF728;
    if (((int)(*(unsigned int *)(v_rip + 13499106))) == (*(unsigned __int64 *)(v_rip + 12646186))) goto loc_002EF728;
    a1 = (*(unsigned __int64 *)(v_rip + 12646186) - 1) & (v_rbp);
    a4 = (*(unsigned __int64 *)(v_rip + 12646186)) << (5);
    a1 = ((unsigned int)((unsigned int)(a1))) << (5);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 12646185));
    a4 = (a4) + (*(unsigned __int64 *)(v_rip + 12646185));
loc_002EF644:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (1)) == 0) goto loc_002EF70B;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (1)) != 0) goto loc_002EF70B;
    *(unsigned __int8 *)(a1 + 12) = a6;
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) << (8));
    a2 = (unsigned int)(((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 12)))) ^ ((unsigned int)(result)));
    *(unsigned int *)(a1 + 8) = (unsigned int)((unsigned int)(a2));
    a2 = (unsigned int)((a2) & (0xFFFFFULL));
    result = (unsigned int)((a5) << (20));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    *(unsigned __int64 *)(a1 + 16) = a3;
    *(unsigned int *)(a1 + 12) = a2;
    v_rdi = a1;
    if ((((unsigned __int8)(a4)) & (1)) != 0) {
        v_rdi = (a1) ^ (*(unsigned __int64 *)(v_rip + 13466512));
        *(unsigned __int64 *)(a1 + 24) = v_rdi;
    }
    if (0 >= 16) goto loc_002EF8A7;
loc_002EF6AD:
    if (((*(unsigned __int8 *)(v_rip + 13464658)) & (1)) != 0) goto loc_002EF863;
loc_002EF6BA:
loc_002EF6CC:
    if ((*(unsigned int *)(v_rip + 13465165)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_rip + 12646186), a4);
    }
loc_002EF6E8:
loc_002EF6ED:
    v_rsp = (v_rsp) + (32);
    return 1;
loc_002EF70B:
    a1 = (a1) + (32);
    v_r14 = (unsigned int)((v_r14) + 1);
    if (a1 < a4) { a2 = a1; }
    if (a2 != a1) goto loc_002EF644;
loc_002EF728:
    v_rsi = 0;
    if (((*(unsigned __int8 *)(v_rip + 13464533)) & (33)) != 0) goto loc_002EF7DC;
loc_002EF737:
    if (condition_is_below) goto loc_002EF84F;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12629420)))))) == 0x80000001ULL) goto loc_002EF7FF;
loc_002EF75D:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12629420)))))) >= 0x80000001ULL) {
    }
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 13458230)) & ((unsigned int)(v_rsi))) == 0) goto loc_002EF90A;
loc_002EF77C:
loc_002EF77E:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12629364)))))) != 0x80000001ULL) goto loc_002EF75D;
    goto loc_002EF7FF;
loc_002EF793:
loc_002EF7A4:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12629364)))))) == 0x80000001ULL) goto loc_002EF600;
    if (!sign_flag) goto loc_002EF7A4;
    result = ExpWaitForSpinLockSharedAndAcquire(v_rip + 12629301, (unsigned __int8)(v_stack_p10), *(unsigned __int64 *)(v_rip + 12646186), a4);
    goto loc_002EF600;
loc_002EF7CD:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p10), 2, *(unsigned __int64 *)(v_rip + 12646186), a4);
    goto loc_002EF5D6;
loc_002EF7DC:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12707446))) != 0) goto loc_002EF737;
    result = ExpTryConvertSharedSpinLockExclusiveInstrumented(v_rip + 12629250, v_stack_p48, *(unsigned __int64 *)(v_rip + 12646186), a4);
    if ((unsigned int)(result) == 0) goto loc_002EF84F;
loc_002EF7FF:
    result = ExpResizeBigPageTable(v_rip + 12629250, v_stack_p48, v_stack_p50, a4);
    if (((*(unsigned __int8 *)(v_rip + 13464310)) & (1)) != 0) goto loc_002EF887;
loc_002EF814:
    *(unsigned int *)(v_rip + 12629210) = 0;
loc_002EF81E:
    if ((*(unsigned int *)(v_rip + 13464827)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        a2 = (unsigned __int8)(v_stack_p10);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_p50, a4);
    }
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_002EF945;
    result = 0;
    goto loc_002EF6ED;
loc_002EF84F:
    result = ExReleaseSpinLockShared(v_rip + 12629151, (unsigned __int8)(v_stack_p10), v_stack_p50, a4);
    goto loc_002EF5BC;
loc_002EF863:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12707311))) != 0) goto loc_002EF6BA;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(v_rip + 12629115, v_stack_p48, v_stack_p50, a4);
    goto loc_002EF6CC;
loc_002EF887:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12707275))) != 0) goto loc_002EF814;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rip + 12629083, v_stack_p48, v_stack_p50, a4);
    goto loc_002EF81E;
loc_002EF8A7:
    a3 = (v_stack_p50) >> (2);
    if ((*(unsigned int *)(v_rip + 13498446)) <= ((unsigned int)(a3))) goto loc_002EF6AD;
    result = ExTryConvertSharedSpinLockExclusive(v_rip + 12629049, v_stack_p48, a3, a4);
    if (((unsigned int)(result)) != 1) goto loc_002EF931;
    result = ExpResizeBigPageTable(v_rip + 12629049, v_stack_p48, v_stack_p50, a4);
    result = ExReleaseSpinLockExclusive(v_rip + 12629019, (unsigned __int8)(v_stack_p10), v_stack_p50, a4);
    if (v_stack_p50 == 0) goto loc_002EF6E8;
loc_002EF8F0:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p50, a2, v_stack_p50, a4);
    if (*(unsigned __int64 *)(v_stack_p50) != 0) goto loc_002EF8F0;
    goto loc_002EF6E8;
loc_002EF90A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13463976)))) & (64)) == 0) goto loc_002EF77C;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p50, a2, v_stack_p50, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002EF77C;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a2, v_stack_p50, a4);
    goto loc_002EF77E;
loc_002EF931:
    result = ExReleaseSpinLockShared(v_rip + 12628925, (unsigned __int8)(*(unsigned __int64 *)(v_stack_p50)), v_stack_p50, a4);
    goto loc_002EF6E8;
loc_002EF945:
    if (v_stack_p50 == 0) goto loc_002EF5C1;
loc_002EF960:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p50, a2, v_stack_p50, a4);
    if (*(unsigned __int64 *)(v_stack_p50) != 0) goto loc_002EF960;
    v_stack_p50 = *(unsigned __int64 *)(v_stack_p50);
    goto loc_002EF5BC;
}
```

## 5. (Beta) C Style

```c
int64_t ExpAddTagForBigPages(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint16_t Arg5, uint8_t Arg6)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    v_stack_p8 = 0;
    result = (Arg1) >> (12);
    local_r14 = 0;
    local_r10 = (local_r10) * (result);
    local_rbp = (local_r10) >> (32);
    local_rbp = (local_rbp) ^ (local_r10);
loc_002EF5BC:
loc_002EF5C1:
    if ((*(uint32_t *)(v_rip + 0xCD7750)) != 0) goto loc_002EF7CD;
loc_002EF5D6:
    if (((*(uint8_t *)(v_rip + 0xCD7529)) & (33)) == 0) goto loc_002EF793;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC1E86F))) != 0) goto loc_002EF793;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(v_rip + 12629757, (uint8_t)(v_cr8), Arg3, Arg4);
loc_002EF600:
    if (*(uint64_t *)(v_rip + 0xC0F729) == 0) goto loc_002EF728;
    if (((int32_t)(*(uint32_t *)(v_rip + 0xCDFAE2))) == (*(uint64_t *)(v_rip + 0xC0F72A))) goto loc_002EF728;
    Arg1 = (*(uint64_t *)(v_rip + 0xC0F72A) - 1) & (local_rbp);
    Arg4 = (*(uint64_t *)(v_rip + 0xC0F72A)) << (5);
    Arg1 = ((uint32_t)((uint32_t)(Arg1))) << (5);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xC0F729));
    Arg4 = (Arg4) + (*(uint64_t *)(v_rip + 0xC0F729));
loc_002EF644:
    if ((((uint8_t)(*(uint64_t *)(Arg1))) & (1)) == 0) goto loc_002EF70B;
    if ((((uint8_t)(*(uint64_t *)(Arg1))) & (1)) != 0) goto loc_002EF70B;
    *(uint8_t *)(Arg1 + 0xC) = Arg6;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) << (8));
    Arg2 = (uint32_t)(((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0xC)))) ^ ((uint32_t)(result)));
    *(uint32_t *)(Arg1 + 0x8) = (uint32_t)((uint32_t)(Arg2));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFULL));
    result = (uint32_t)((Arg5) << (20));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    *(uint64_t *)(Arg1 + 0x10) = Arg3;
    *(uint32_t *)(Arg1 + 0xC) = Arg2;
    local_rdi = Arg1;
    if ((((uint8_t)(Arg4)) & (1)) != 0) {
        local_rdi = (Arg1) ^ (*(uint64_t *)(v_rip + 0xCD7B90));
        *(uint64_t *)(Arg1 + 0x18) = local_rdi;
    }
    if (0 >= 16) goto loc_002EF8A7;
loc_002EF6AD:
    if (((*(uint8_t *)(v_rip + 0xCD7452)) & (1)) != 0) goto loc_002EF863;
loc_002EF6BA:
loc_002EF6CC:
    if ((*(uint32_t *)(v_rip + 0xCD764D)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(v_rip + 0xC0F72A), Arg4);
    }
loc_002EF6E8:
loc_002EF6ED:
    local_rsp = (local_rsp) + (32);
    return 1;
loc_002EF70B:
    Arg1 = (Arg1) + (32);
    local_r14 = (uint32_t)((local_r14) + 1);
    if (Arg1 < Arg4) { Arg2 = Arg1; }
    if (Arg2 != Arg1) goto loc_002EF644;
loc_002EF728:
    local_rsi = 0;
    if (((*(uint8_t *)(v_rip + 0xCD73D5)) & (33)) != 0) goto loc_002EF7DC;
loc_002EF737:
    if (condition_is_below) goto loc_002EF84F;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC0B5AC)))))) == 0x80000001ULL) goto loc_002EF7FF;
loc_002EF75D:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC0B5AC)))))) >= 0x80000001ULL) {
    }
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xCD5B36)) & ((uint32_t)(local_rsi))) == 0) goto loc_002EF90A;
loc_002EF77C:
loc_002EF77E:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC0B574)))))) != 0x80000001ULL) goto loc_002EF75D;
    goto loc_002EF7FF;
loc_002EF793:
loc_002EF7A4:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC0B574)))))) == 0x80000001ULL) goto loc_002EF600;
    if (!sign_flag) goto loc_002EF7A4;
    result = ExpWaitForSpinLockSharedAndAcquire(v_rip + 12629301, (uint8_t)(v_stack_p10), *(uint64_t *)(v_rip + 0xC0F72A), Arg4);
    goto loc_002EF600;
loc_002EF7CD:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p10), 2, *(uint64_t *)(v_rip + 0xC0F72A), Arg4);
    goto loc_002EF5D6;
loc_002EF7DC:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC1E676))) != 0) goto loc_002EF737;
    result = ExpTryConvertSharedSpinLockExclusiveInstrumented(v_rip + 12629250, v_stack_p48, *(uint64_t *)(v_rip + 0xC0F72A), Arg4);
    if ((uint32_t)(result) == 0) goto loc_002EF84F;
loc_002EF7FF:
    result = ExpResizeBigPageTable(v_rip + 12629250, v_stack_p48, v_stack_p50, Arg4);
    if (((*(uint8_t *)(v_rip + 0xCD72F6)) & (1)) != 0) goto loc_002EF887;
loc_002EF814:
    *(uint32_t *)(v_rip + 0xC0B4DA) = 0;
loc_002EF81E:
    if ((*(uint32_t *)(v_rip + 0xCD74FB)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        Arg2 = (uint8_t)(v_stack_p10);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_p50, Arg4);
    }
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_002EF945;
    result = 0;
    goto loc_002EF6ED;
loc_002EF84F:
    result = ExReleaseSpinLockShared(v_rip + 12629151, (uint8_t)(v_stack_p10), v_stack_p50, Arg4);
    goto loc_002EF5BC;
loc_002EF863:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC1E5EF))) != 0) goto loc_002EF6BA;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(v_rip + 12629115, v_stack_p48, v_stack_p50, Arg4);
    goto loc_002EF6CC;
loc_002EF887:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC1E5CB))) != 0) goto loc_002EF814;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rip + 12629083, v_stack_p48, v_stack_p50, Arg4);
    goto loc_002EF81E;
loc_002EF8A7:
    Arg3 = (v_stack_p50) >> (2);
    if ((*(uint32_t *)(v_rip + 0xCDF84E)) <= ((uint32_t)(Arg3))) goto loc_002EF6AD;
    result = ExTryConvertSharedSpinLockExclusive(v_rip + 12629049, v_stack_p48, Arg3, Arg4);
    if (((uint32_t)(result)) != 1) goto loc_002EF931;
    result = ExpResizeBigPageTable(v_rip + 12629049, v_stack_p48, v_stack_p50, Arg4);
    result = ExReleaseSpinLockExclusive(v_rip + 12629019, (uint8_t)(v_stack_p10), v_stack_p50, Arg4);
    if (v_stack_p50 == 0) goto loc_002EF6E8;
loc_002EF8F0:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p50, Arg2, v_stack_p50, Arg4);
    if (*(uint64_t *)(v_stack_p50) != 0) goto loc_002EF8F0;
    goto loc_002EF6E8;
loc_002EF90A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCD71A8)))) & (64)) == 0) goto loc_002EF77C;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p50, Arg2, v_stack_p50, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002EF77C;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg2, v_stack_p50, Arg4);
    goto loc_002EF77E;
loc_002EF931:
    result = ExReleaseSpinLockShared(v_rip + 12628925, (uint8_t)(*(uint64_t *)(v_stack_p50)), v_stack_p50, Arg4);
    goto loc_002EF6E8;
loc_002EF945:
    if (v_stack_p50 == 0) goto loc_002EF5C1;
loc_002EF960:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_p50, Arg2, v_stack_p50, Arg4);
    if (*(uint64_t *)(v_stack_p50) != 0) goto loc_002EF960;
    v_stack_p50 = *(uint64_t *)(v_stack_p50);
    goto loc_002EF5BC;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002EF570&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
