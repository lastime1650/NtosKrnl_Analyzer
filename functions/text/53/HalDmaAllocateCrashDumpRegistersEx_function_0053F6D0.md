# HalDmaAllocateCrashDumpRegistersEx

- RVA: `0x0053F6D0`–`0x0053FB66` (길이 `1,174` bytes)
- VA: `0x000000014053F6D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C39C4`
- 디코드: `279`개 명령, `1,174/1,174` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x0053F719` → [HalpDmaExtractFromVerifierShadowAdapter](../4B/HalpDmaExtractFromVerifierShadowAdapter_function_004B8DA4.md) (function, `0x004B8DA4`)
- `0x0053F7D2` → [HalpDmaAllocateMapRegisters](../3D/HalpDmaAllocateMapRegisters_function_003DDA0C.md) (function, `0x003DDA0C`)
- `0x0053F83C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0053F850` → [HalpIsHvPresent](../4A/HalpIsHvPresent_function_004AFA10.md) (function, `0x004AFA10`)
- `0x0053F872` → [HalpMmAllocCtxAlloc](../3E/HalpMmAllocCtxAlloc_function_003E10B8.md) (function, `0x003E10B8`)
- `0x0053F8CA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0053F8D9` → [HalpMmAllocCtxFree](../3E/HalpMmAllocCtxFree_function_003E1904.md) (function, `0x003E1904`)
- `0x0053F8F4` → [HalpDmaFreeMapRegisters](../3D/HalpDmaFreeMapRegisters_function_003DF5F4.md) (function, `0x003DF5F4`)
- `0x0053F921` → [HalpDmaFreeMapRegisters](../3D/HalpDmaFreeMapRegisters_function_003DF5F4.md) (function, `0x003DF5F4`)
- `0x0053F989` → [HalpDmaAllocateMapRegistersAtHighLevel](../55/HalpDmaAllocateMapRegistersAtHighLevel_function_005507A8.md) (function, `0x005507A8`)
- `0x0053F9C1` → [HalpDmaFreeMapRegisters](../3D/HalpDmaFreeMapRegisters_function_003DF5F4.md) (function, `0x003DF5F4`)
- `0x0053FA62` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0053FAC4` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x0053FADA` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0053FB32` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- [DifHalDmaAllocateCrashDumpRegistersExWrapper](../62/DifHalDmaAllocateCrashDumpRegistersExWrapper_function_00624330.md) at `0x00624434`

### Static image references
- `0x0053F813` → RVA `0x00FC1778` (`.data`; read)
- `0x0053F94E` → RVA `0x00FC3E68` (`.data`; read)
- `0x0053FA5B` → RVA `0x00FC3E80` (`.data`; read)
- `0x0053FA6A` → RVA `0x00FC3EA0` (`.data`; read)
- `0x0053FA8E` → RVA `0x00FC3EA8` (`.data`; read)
- `0x0053FAAF` → RVA `0x00FC3EA8` (`.data`; write)
- `0x0053FAD3` → RVA `0x00FC3EC8` (`.data`; read)
- `0x0053FAE2` → RVA `0x00FC3EB0` (`.data`; read)
- `0x0053FB03` → RVA `0x00FC3EB8` (`.data`; read)
- `0x0053FB1D` → RVA `0x00FC3EB8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0053F6D0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0053F6D5  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
0053F6DA  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0053F6DF  57                              push rdi
0053F6E0  41 54                           push r12
0053F6E2  41 55                           push r13
0053F6E4  41 56                           push r14
0053F6E6  41 57                           push r15
0053F6E8  48 83 EC 60                     sub rsp, 0x60
0053F6EC  33 C0                           xor eax, eax
0053F6EE  8B F2                           mov esi, edx
0053F6F0  0F 57 C0                        xorps xmm0, xmm0
0053F6F3  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
0053F6F7  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
0053F6FC  4D 8B F1                        mov r14, r9
0053F6FF  45 0F 20 C4                     mov r12, cr8
0053F703  45 33 D2                        xor r10d, r10d
0053F706  48 8B E9                        mov rbp, rcx
0053F709  81 79 10 56 44 6D 61            cmp dword ptr [rcx + 0x10], 0x616d4456
0053F710  49 0F 45 EA                     cmovne rbp, r10
0053F714  48 89 6C 24 40                  mov qword ptr [rsp + 0x40], rbp
0053F719  E8 86 96 F7 FF                  call 0x1404b8da4
0053F71E  48 8B D8                        mov rbx, rax
0053F721  48 85 C0                        test rax, rax
0053F724  0F 84 18 04 00 00               je 0x14053fb42
0053F72A  85 D2                           test edx, edx
0053F72C  0F 84 10 04 00 00               je 0x14053fb42
0053F732  4D 85 C9                        test r9, r9
0053F735  0F 84 07 04 00 00               je 0x14053fb42
0053F73B  4C 8B BC 24 B0 00 00 00         mov r15, qword ptr [rsp + 0xb0]
0053F743  4D 85 FF                        test r15, r15
0053F746  0F 84 F6 03 00 00               je 0x14053fb42
0053F74C  41 83 F8 01                     cmp r8d, 1
0053F750  0F 87 EC 03 00 00               ja 0x14053fb42
0053F756  44 38 90 B8 01 00 00            cmp byte ptr [rax + 0x1b8], r10b
0053F75D  75 35                           jne 0x14053f794
0053F75F  44 38 90 BD 01 00 00            cmp byte ptr [rax + 0x1bd], r10b
0053F766  74 2C                           je 0x14053f794
0053F768  4D 89 11                        mov qword ptr [r9], r10
0053F76B  41 89 37                        mov dword ptr [r15], esi
0053F76E  49 63 F8                        movsxd rdi, r8d
0053F771  4C 89 90 F0 00 00 00            mov qword ptr [rax + 0xf0], r10
0053F778  44 89 90 F8 00 00 00            mov dword ptr [rax + 0xf8], r10d
0053F77F  4C 89 94 F8 00 01 00 00         mov qword ptr [rax + rdi*8 + 0x100], r10
0053F787  44 89 94 B8 10 01 00 00         mov dword ptr [rax + rdi*4 + 0x110], r10d
0053F78F  E9 AF 02 00 00                  jmp 0x14053fa43
0053F794  49 63 F8                        movsxd rdi, r8d
0053F797  8B AC B8 10 01 00 00            mov ebp, dword ptr [rax + rdi*4 + 0x110]
0053F79E  3B F5                           cmp esi, ebp
0053F7A0  77 13                           ja 0x14053f7b5
0053F7A2  41 89 37                        mov dword ptr [r15], esi
0053F7A5  48 8B 84 F8 00 01 00 00         mov rax, qword ptr [rax + rdi*8 + 0x100]
0053F7AD  49 89 01                        mov qword ptr [r9], rax
0053F7B0  E9 89 02 00 00                  jmp 0x14053fa3e
0053F7B5  3B B0 E8 00 00 00               cmp esi, dword ptr [rax + 0xe8]
0053F7BB  0F 87 81 03 00 00               ja 0x14053fb42
0053F7C1  44 0F 20 C0                     mov rax, cr8
0053F7C5  84 C0                           test al, al
0053F7C7  0F 85 65 01 00 00               jne 0x14053f932
0053F7CD  8B D6                           mov edx, esi
0053F7CF  48 8B CB                        mov rcx, rbx
0053F7D2  E8 35 E2 E9 FF                  call 0x1403dda0c
0053F7D7  45 33 D2                        xor r10d, r10d
0053F7DA  48 8B E8                        mov rbp, rax
0053F7DD  48 85 C0                        test rax, rax
0053F7E0  75 0A                           jne 0x14053f7ec
0053F7E2  B8 9A 00 00 C0                  mov eax, 0xc000009a
0053F7E7  E9 5B 03 00 00                  jmp 0x14053fb47
0053F7EC  48 89 AC FB 00 01 00 00         mov qword ptr [rbx + rdi*8 + 0x100], rbp
0053F7F4  89 B4 BB 10 01 00 00            mov dword ptr [rbx + rdi*4 + 0x110], esi
0053F7FB  83 BB 08 02 00 00 03            cmp dword ptr [rbx + 0x208], 3
0053F802  0F 85 FD 00 00 00               jne 0x14053f905
0053F808  48 8B 8B 00 02 00 00            mov rcx, qword ptr [rbx + 0x200]
0053F80F  4C 8D 40 18                     lea r8, [rax + 0x18]
0053F813  48 8B 05 5E 1F A8 00            mov rax, qword ptr [rip + 0xa81f5e]
0053F81A  48 8B D6                        mov rdx, rsi
0053F81D  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0053F822  45 33 C9                        xor r9d, r9d
0053F825  48 C1 E2 0C                     shl rdx, 0xc
0053F829  45 33 C0                        xor r8d, r8d
0053F82C  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
0053F830  48 8B 80 80 00 00 00            mov rax, qword ptr [rax + 0x80]
0053F837  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
0053F83C  E8 8F B2 17 00                  call 0x1406baad0
0053F841  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
0053F848  85 C0                           test eax, eax
0053F84A  0F 88 C8 00 00 00               js 0x14053f918
0053F850  E8 BB 01 F7 FF                  call 0x1404afa10
0053F855  84 C0                           test al, al
0053F857  0F 84 A8 00 00 00               je 0x14053f905
0053F85D  48 8D 14 F5 00 00 00 00         lea rdx, [rsi*8]
0053F865  C7 44 24 48 02 00 00 00         mov dword ptr [rsp + 0x48], 2
0053F86D  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
0053F872  E8 41 18 EA FF                  call 0x1403e10b8
0053F877  4C 8B E8                        mov r13, rax
0053F87A  48 85 C0                        test rax, rax
0053F87D  0F 84 95 00 00 00               je 0x14053f918
0053F883  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0053F888  45 33 C9                        xor r9d, r9d
0053F88B  4C 8B C5                        mov r8, rbp
0053F88E  49 8B 10                        mov rdx, qword ptr [r8]
0053F891  48 C1 EA 0C                     shr rdx, 0xc
0053F895  4A 89 14 C8                     mov qword ptr [rax + r9*8], rdx
0053F899  41 FF C1                        inc r9d
0053F89C  4D 8B 40 08                     mov r8, qword ptr [r8 + 8]
0053F8A0  4D 85 C0                        test r8, r8
0053F8A3  75 E9                           jne 0x14053f88e
0053F8A5  48 8B 05 CC 1E A8 00            mov rax, qword ptr [rip + 0xa81ecc]
0053F8AC  48 8D 4D 18                     lea rcx, [rbp + 0x18]
0053F8B0  33 D2                           xor edx, edx
0053F8B2  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0053F8B7  48 8B 09                        mov rcx, qword ptr [rcx]
0053F8BA  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
0053F8BF  48 8B 80 90 00 00 00            mov rax, qword ptr [rax + 0x90]
0053F8C6  44 8D 42 03                     lea r8d, [rdx + 3]
0053F8CA  E8 01 B2 17 00                  call 0x1406baad0
0053F8CF  49 8B D5                        mov rdx, r13
0053F8D2  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
0053F8D9  E8 26 20 EA FF                  call 0x1403e1904
0053F8DE  44 8B AC 24 90 00 00 00         mov r13d, dword ptr [rsp + 0x90]
0053F8E6  45 85 ED                        test r13d, r13d
0053F8E9  79 16                           jns 0x14053f901
0053F8EB  44 8B C6                        mov r8d, esi
0053F8EE  48 8B D5                        mov rdx, rbp
0053F8F1  48 8B CB                        mov rcx, rbx
0053F8F4  E8 FB FC E9 FF                  call 0x1403df5f4
0053F8F9  41 8B C5                        mov eax, r13d
0053F8FC  E9 46 02 00 00                  jmp 0x14053fb47
0053F901  C6 45 40 01                     mov byte ptr [rbp + 0x40], 1
0053F905  41 89 37                        mov dword ptr [r15], esi
0053F908  48 8B 84 FB 00 01 00 00         mov rax, qword ptr [rbx + rdi*8 + 0x100]
0053F910  49 89 06                        mov qword ptr [r14], rax
0053F913  E9 26 01 00 00                  jmp 0x14053fa3e
0053F918  44 8B C6                        mov r8d, esi
0053F91B  48 8B D5                        mov rdx, rbp
0053F91E  48 8B CB                        mov rcx, rbx
0053F921  E8 CE FC E9 FF                  call 0x1403df5f4
0053F926  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
0053F92D  E9 15 02 00 00                  jmp 0x14053fb47
0053F932  48 8D 83 10 01 00 00            lea rax, [rbx + 0x110]
0053F939  48 85 C0                        test rax, rax
0053F93C  74 10                           je 0x14053f94e
0053F93E  44 38 93 BA 01 00 00            cmp byte ptr [rbx + 0x1ba], r10b
0053F945  75 07                           jne 0x14053f94e
0053F947  B9 9A 00 00 C0                  mov ecx, 0xc000009a
0053F94C  EB 0E                           jmp 0x14053f95c
0053F94E  83 3D 13 45 A8 00 01            cmp dword ptr [rip + 0xa84513], 1
0053F955  75 19                           jne 0x14053f970
0053F957  B9 BB 00 00 C0                  mov ecx, 0xc00000bb
0053F95C  4D 89 11                        mov qword ptr [r9], r10
0053F95F  8B 84 BB 10 01 00 00            mov eax, dword ptr [rbx + rdi*4 + 0x110]
0053F966  41 89 07                        mov dword ptr [r15], eax
0053F969  8B C1                           mov eax, ecx
0053F96B  E9 D7 01 00 00                  jmp 0x14053fb47
0053F970  44 8B EE                        mov r13d, esi
0053F973  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
0053F97B  44 2B ED                        sub r13d, ebp
0053F97E  48 8B CB                        mov rcx, rbx
0053F981  44 89 AC 24 90 00 00 00         mov dword ptr [rsp + 0x90], r13d
0053F989  E8 1A 0E 01 00                  call 0x1405507a8
0053F98E  45 33 D2                        xor r10d, r10d
0053F991  48 8B C8                        mov rcx, rax
0053F994  48 85 C0                        test rax, rax
0053F997  75 0B                           jne 0x14053f9a4
0053F999  4D 89 16                        mov qword ptr [r14], r10
0053F99C  41 89 2F                        mov dword ptr [r15], ebp
0053F99F  E9 3E FE FF FF                  jmp 0x14053f7e2
0053F9A4  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
0053F9AC  45 3B C5                        cmp r8d, r13d
0053F9AF  74 1A                           je 0x14053f9cb
0053F9B1  41 8D 04 28                     lea eax, [r8 + rbp]
0053F9B5  4D 89 16                        mov qword ptr [r14], r10
0053F9B8  48 8B D1                        mov rdx, rcx
0053F9BB  41 89 07                        mov dword ptr [r15], eax
0053F9BE  48 8B CB                        mov rcx, rbx
0053F9C1  E8 2E FC E9 FF                  call 0x1403df5f4
0053F9C6  E9 17 FE FF FF                  jmp 0x14053f7e2
0053F9CB  4C 39 94 FB 00 01 00 00         cmp qword ptr [rbx + rdi*8 + 0x100], r10
0053F9D3  74 3F                           je 0x14053fa14
0053F9D5  0F AE E8                        lfence
0053F9D8  8B 84 BB 10 01 00 00            mov eax, dword ptr [rbx + rdi*4 + 0x110]
0053F9DF  48 8B 94 FB 00 01 00 00         mov rdx, qword ptr [rbx + rdi*8 + 0x100]
0053F9E7  83 F8 01                        cmp eax, 1
0053F9EA  76 0E                           jbe 0x14053f9fa
0053F9EC  44 8D 40 FF                     lea r8d, [rax - 1]
0053F9F0  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
0053F9F4  49 83 E8 01                     sub r8, 1
0053F9F8  75 F6                           jne 0x14053f9f0
0053F9FA  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
0053FA01  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0053FA05  01 84 BB 10 01 00 00            add dword ptr [rbx + rdi*4 + 0x110], eax
0053FA0C  89 B3 F8 00 00 00               mov dword ptr [rbx + 0xf8], esi
0053FA12  EB 1C                           jmp 0x14053fa30
0053FA14  48 89 8B F0 00 00 00            mov qword ptr [rbx + 0xf0], rcx
0053FA1B  89 B3 F8 00 00 00               mov dword ptr [rbx + 0xf8], esi
0053FA21  48 89 8C FB 00 01 00 00         mov qword ptr [rbx + rdi*8 + 0x100], rcx
0053FA29  89 B4 BB 10 01 00 00            mov dword ptr [rbx + rdi*4 + 0x110], esi
0053FA30  48 8B 84 FB 00 01 00 00         mov rax, qword ptr [rbx + rdi*8 + 0x100]
0053FA38  49 89 06                        mov qword ptr [r14], rax
0053FA3B  41 89 37                        mov dword ptr [r15], esi
0053FA3E  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
0053FA43  49 8B 06                        mov rax, qword ptr [r14]
0053FA46  48 85 C0                        test rax, rax
0053FA49  74 04                           je 0x14053fa4f
0053FA4B  48 89 40 38                     mov qword ptr [rax + 0x38], rax
0053FA4F  FF 84 BB 18 01 00 00            inc dword ptr [rbx + rdi*4 + 0x118]
0053FA56  45 84 E4                        test r12b, r12b
0053FA59  75 0F                           jne 0x14053fa6a
0053FA5B  48 8D 0D 1E 44 A8 00            lea rcx, [rip + 0xa8441e]
0053FA62  E8 09 8A CC FF                  call 0x140208470
0053FA67  44 8A E0                        mov r12b, al
0053FA6A  48 8B 15 2F 44 A8 00            mov rdx, qword ptr [rip + 0xa8442f]
0053FA71  4C 8D 05 28 44 A8 00            lea r8, [rip + 0xa84428]
0053FA78  EB 0F                           jmp 0x14053fa89
0053FA7A  48 8D 8A E0 FE FF FF            lea rcx, [rdx - 0x120]
0053FA81  48 3B CB                        cmp rcx, rbx
0053FA84  74 30                           je 0x14053fab6
0053FA86  48 8B 12                        mov rdx, qword ptr [rdx]
0053FA89  49 3B D0                        cmp rdx, r8
0053FA8C  75 EC                           jne 0x14053fa7a
0053FA8E  48 8B 05 13 44 A8 00            mov rax, qword ptr [rip + 0xa84413]
0053FA95  48 81 C3 20 01 00 00            add rbx, 0x120
0053FA9C  4C 39 00                        cmp qword ptr [rax], r8
0053FA9F  0F 85 96 00 00 00               jne 0x14053fb3b
0053FAA5  4C 89 03                        mov qword ptr [rbx], r8
0053FAA8  48 89 43 08                     mov qword ptr [rbx + 8], rax
0053FAAC  48 89 18                        mov qword ptr [rax], rbx
0053FAAF  48 89 1D F2 43 A8 00            mov qword ptr [rip + 0xa843f2], rbx
0053FAB6  45 84 E4                        test r12b, r12b
0053FAB9  75 0E                           jne 0x14053fac9
0053FABB  33 D2                           xor edx, edx
0053FABD  48 8D 0D BC 43 A8 00            lea rcx, [rip + 0xa843bc]
0053FAC4  E8 D7 30 E5 FF                  call 0x140392ba0
0053FAC9  48 85 ED                        test rbp, rbp
0053FACC  74 69                           je 0x14053fb37
0053FACE  45 84 E4                        test r12b, r12b
0053FAD1  75 0F                           jne 0x14053fae2
0053FAD3  48 8D 0D EE 43 A8 00            lea rcx, [rip + 0xa843ee]
0053FADA  E8 91 89 CC FF                  call 0x140208470
0053FADF  44 8A E0                        mov r12b, al
0053FAE2  48 8B 0D C7 43 A8 00            mov rcx, qword ptr [rip + 0xa843c7]
0053FAE9  4C 8D 05 C0 43 A8 00            lea r8, [rip + 0xa843c0]
0053FAF0  EB 0C                           jmp 0x14053fafe
0053FAF2  48 8D 41 E0                     lea rax, [rcx - 0x20]
0053FAF6  48 3B C5                        cmp rax, rbp
0053FAF9  74 29                           je 0x14053fb24
0053FAFB  48 8B 09                        mov rcx, qword ptr [rcx]
0053FAFE  49 3B C8                        cmp rcx, r8
0053FB01  75 EF                           jne 0x14053faf2
0053FB03  48 8B 15 AE 43 A8 00            mov rdx, qword ptr [rip + 0xa843ae]
0053FB0A  48 8D 45 20                     lea rax, [rbp + 0x20]
0053FB0E  4C 39 02                        cmp qword ptr [rdx], r8
0053FB11  75 28                           jne 0x14053fb3b
0053FB13  4C 89 00                        mov qword ptr [rax], r8
0053FB16  48 89 50 08                     mov qword ptr [rax + 8], rdx
0053FB1A  48 89 02                        mov qword ptr [rdx], rax
0053FB1D  48 89 05 94 43 A8 00            mov qword ptr [rip + 0xa84394], rax
0053FB24  45 84 E4                        test r12b, r12b
0053FB27  75 0E                           jne 0x14053fb37
0053FB29  33 D2                           xor edx, edx
0053FB2B  48 8D 0D 96 43 A8 00            lea rcx, [rip + 0xa84396]
0053FB32  E8 69 30 E5 FF                  call 0x140392ba0
0053FB37  33 C0                           xor eax, eax
0053FB39  EB 0C                           jmp 0x14053fb47
0053FB3B  B9 03 00 00 00                  mov ecx, 3
0053FB40  CD 29                           int 0x29
0053FB42  B8 0D 00 00 C0                  mov eax, 0xc000000d
0053FB47  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
0053FB4C  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0053FB50  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
0053FB54  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
0053FB58  49 8B E3                        mov rsp, r11
0053FB5B  41 5F                           pop r15
0053FB5D  41 5E                           pop r14
0053FB5F  41 5D                           pop r13
0053FB61  41 5C                           pop r12
0053FB63  5F                              pop rdi
0053FB64  C3                              ret
0053FB65  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalDmaAllocateCrashDumpRegistersEx(__int64 a1, int a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (96);
    result = 0;
    v_stack_m30 = 0;
    v_stack_m40 = v_xmm0;
    v_r10 = 0;
    if ((*(unsigned int *)(a1 + 16)) != 0x616D4456ULL) { a1 = 0; }
    v_stack_m48 = a1;
    result = HalpDmaExtractFromVerifierShadowAdapter(a1, a2, a3, a4);
    if (result == 0) goto loc_0053FB42;
    if (a2 == 0) goto loc_0053FB42;
    if (a4 == 0) goto loc_0053FB42;
    if (a5 == 0) goto loc_0053FB42;
    if (a3 > 1) goto loc_0053FB42;
    if ((*(unsigned __int8 *)(result + 440)) != 0) goto loc_0053F794;
    if ((*(unsigned __int8 *)(result + 445)) == 0) goto loc_0053F794;
    *(unsigned __int64 *)(a4) = 0;
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(a2));
    *(unsigned __int64 *)(result + 240) = 0;
    *(unsigned int *)(result + 248) = 0;
    *(unsigned __int64 *)(result + (int)(a3) * 8 + 256) = 0;
    *(unsigned int *)(result + (int)(a3) * 4 + 272) = 0;
    goto loc_0053FA43;
loc_0053F794:
    if (((unsigned int)((unsigned int)(a2))) > ((unsigned int)((unsigned int)(*(unsigned int *)(result + (int)(a3) * 4 + 272))))) goto loc_0053F7B5;
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(a2));
    *(unsigned __int64 *)(a4) = *(unsigned __int64 *)(result + (int)(a3) * 8 + 256);
    goto loc_0053FA3E;
loc_0053F7B5:
    if (((unsigned int)((unsigned int)(a2))) > (*(unsigned int *)(*(unsigned __int64 *)(result + (int)(a3) * 8 + 256) + 232))) goto loc_0053FB42;
    if ((unsigned __int8)(v_cr8) != 0) goto loc_0053F932;
    result = HalpDmaAllocateMapRegisters(result, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_r10 = 0;
    if (result != 0) goto loc_0053F7EC;
loc_0053F7E2:
    goto loc_0053FB47;
loc_0053F7EC:
    *(unsigned __int64 *)(result + (int)(a3) * 8 + 256) = result;
    *(unsigned int *)(result + (int)(a3) * 4 + 272) = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned int *)(result + 520)) != 3) goto loc_0053F905;
    v_stack_m60 = (unsigned int)(0xC000009AULL) + 24;
    a4 = 0;
    a2 = ((unsigned int)(a2)) << (12);
    a3 = 0;
    v_stack_m68 = 0;
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 512) + 40), a2, a3, a4);
    v_stack_p8 = (unsigned int)(result);
    if (sign_flag) goto loc_0053F918;
    result = HalpIsHvPresent(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 512) + 40), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0053F905;
    v_stack_m40 = 2;
    v_stack_m30 = (unsigned int)(a2);
    result = HalpMmAllocCtxAlloc(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 512) + 40), (unsigned int)(a2) * 8, a3, a4);
    if (result == 0) goto loc_0053F918;
    v_stack_m38 = result;
    a4 = 0;
loc_0053F88E:
    a2 = (*(unsigned __int64 *)(result)) >> (12);
    *(unsigned __int64 *)(result + a4 * 8) = a2;
    a4 = (unsigned int)((a4) + 1);
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_0053F88E;
    a2 = 0;
    v_stack_m68 = result + 24;
    result = guard_dispatch_icall(*(unsigned __int64 *)(result + 24), a2, a2 + 3, v_stack_m40);
    v_stack_p8 = (unsigned int)(result);
    result = HalpMmAllocCtxFree(*(unsigned __int64 *)(result + 24), result, a2 + 3, v_stack_m40);
    if (!sign_flag) goto loc_0053F901;
    result = HalpDmaFreeMapRegisters(result, result, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_m40);
    goto loc_0053FB47;
loc_0053F901:
    *(unsigned __int8 *)(result + 64) = 1;
loc_0053F905:
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(a2));
    *(unsigned __int64 *)(a4) = *(unsigned __int64 *)(result + (int)(a3) * 8 + 256);
    goto loc_0053FA3E;
loc_0053F918:
    result = HalpDmaFreeMapRegisters(result, result, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_m40);
    goto loc_0053FB47;
loc_0053F932:
    if (result + 272 == 0) goto loc_0053F94E;
    if ((*(unsigned __int8 *)(result + 442)) != 0) goto loc_0053F94E;
    goto loc_0053F95C;
loc_0053F94E:
    if ((*(unsigned int *)(v_rip + 11027731)) != 1) goto loc_0053F970;
loc_0053F95C:
    *(unsigned __int64 *)(v_stack_m40) = 0;
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(*(unsigned int *)(result + (int)(a3) * 4 + 272)));
    goto loc_0053FB47;
loc_0053F970:
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)(result)));
    v_stack_p8 = (unsigned int)(v_r13);
    result = HalpDmaAllocateMapRegistersAtHighLevel(result, v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_m40);
    v_r10 = 0;
    if (result != 0) goto loc_0053F9A4;
    *(unsigned __int64 *)(a4) = 0;
    *(unsigned int *)(a5) = (unsigned int)(result);
    goto loc_0053F7E2;
loc_0053F9A4:
    if (((unsigned int)((unsigned int)(v_stack_p8))) == ((unsigned int)(v_r13))) goto loc_0053F9CB;
    *(unsigned __int64 *)(a4) = 0;
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(v_stack_p8) + result * 1);
    result = HalpDmaFreeMapRegisters(result, result, (unsigned int)(v_stack_p8), v_stack_m40);
    goto loc_0053F7E2;
loc_0053F9CB:
    if ((*(unsigned __int64 *)(result + (int)(a3) * 8 + 256)) == 0) goto loc_0053FA14;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + (int)(a3) * 4 + 272)))) <= 1) goto loc_0053F9FA;
loc_0053F9F0:
    a3 = ((unsigned int)(*(unsigned int *)(result + (int)(a3) * 4 + 272)) - 1) - (1);
    if (condition_is_not_equal) goto loc_0053F9F0;
loc_0053F9FA:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + (int)(a3) * 8 + 256) + 8) + 8) = result;
    *(unsigned int *)(result + 248) = (unsigned int)((unsigned int)(a2));
    goto loc_0053FA30;
loc_0053FA14:
    *(unsigned __int64 *)(result + 240) = result;
    *(unsigned int *)(result + 248) = (unsigned int)((unsigned int)(a2));
    *(unsigned __int64 *)(result + (int)(a3) * 8 + 256) = result;
    *(unsigned int *)(result + (int)(a3) * 4 + 272) = (unsigned int)((unsigned int)(a2));
loc_0053FA30:
    *(unsigned __int64 *)(a4) = *(unsigned __int64 *)(result + (int)(a3) * 8 + 256);
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(a2));
loc_0053FA3E:
loc_0053FA43:
    if (*(unsigned __int64 *)(a4) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 56) = *(unsigned __int64 *)(a4);
    }
    result = *(unsigned __int64 *)(a4);
    v_r12 = v_cr8;
    if ((unsigned __int8)(v_cr8) == 0) {
        a1 = v_rip + 11027486;
        result = KeAcquireSpinLockRaiseToDpc(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(result + (int)(a3) * 8 + 256) + 8), a3, v_stack_m40);
        v_r12 = (unsigned __int8)(result);
    }
    goto loc_0053FA89;
loc_0053FA7A:
    if ((*(unsigned __int64 *)(v_rip + 11027503) - 288) == result) goto loc_0053FAB6;
loc_0053FA89:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11027503))) != (v_rip + 11027496)) goto loc_0053FA7A;
    v_rbx = (result) + (288);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11027475))) != (v_rip + 11027496)) goto loc_0053FB3B;
    *(unsigned __int64 *)(v_rbx) = v_rip + 11027496;
    *(unsigned __int64 *)(v_rbx + 8) = *(unsigned __int64 *)(v_rip + 11027475);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11027475)) = v_rbx;
    *(unsigned __int64 *)(v_rip + 11027442) = v_rbx;
loc_0053FAB6:
    result = *(unsigned __int64 *)(v_rip + 11027475);
    if ((unsigned __int8)(v_r12) == 0) {
        a2 = 0;
        a1 = v_rip + 11027388;
        result = KeReleaseSpinLock(a1, a2, v_rip + 11027496, v_stack_m40);
    }
    if (v_stack_m48 == 0) goto loc_0053FB37;
    if ((unsigned __int8)(v_r12) == 0) {
        a1 = v_rip + 11027438;
        result = KeAcquireSpinLockRaiseToDpc(a1, a2, v_rip + 11027496, v_stack_m40);
        v_r12 = (unsigned __int8)(result);
    }
    goto loc_0053FAFE;
loc_0053FAF2:
    if ((*(unsigned __int64 *)(v_rip + 11027399) - 32) == v_stack_m48) goto loc_0053FB24;
loc_0053FAFE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11027399))) != (v_rip + 11027392)) goto loc_0053FAF2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11027374))) != (v_rip + 11027392)) goto loc_0053FB3B;
    *(unsigned __int64 *)(v_stack_m48 + 32) = v_rip + 11027392;
    *(unsigned __int64 *)(v_stack_m48 + 32 + 8) = *(unsigned __int64 *)(v_rip + 11027374);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11027374)) = v_stack_m48 + 32;
    *(unsigned __int64 *)(v_rip + 11027348) = v_stack_m48 + 32;
loc_0053FB24:
    result = v_stack_m48 + 32;
    if ((unsigned __int8)(v_r12) == 0) {
        a2 = 0;
        a1 = v_rip + 11027350;
        result = KeReleaseSpinLock(a1, a2, v_rip + 11027392, v_stack_m40);
    }
    result = 0;
    goto loc_0053FB47;
loc_0053FB3B:
loc_0053FB42:
loc_0053FB47:
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t HalDmaAllocateCrashDumpRegistersEx(void *Arg1, int32_t Arg2, int32_t Arg3, void *Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (96);
    result = 0;
    v_stack_m30 = 0;
    v_stack_m40 = v_xmm0;
    local_r10 = 0;
    if ((*(uint32_t *)(arg1 + 0x10)) != 0x616D4456ULL) { Arg1 = 0; }
    v_stack_m48 = Arg1;
    result = HalpDmaExtractFromVerifierShadowAdapter(Arg1, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0053FB42;
    if (Arg2 == 0) goto loc_0053FB42;
    if (Arg4 == NULL) goto loc_0053FB42;
    if (Arg5 == 0) goto loc_0053FB42;
    if (Arg3 > 1) goto loc_0053FB42;
    if ((*(uint8_t *)(result + 0x1B8)) != 0) goto loc_0053F794;
    if ((*(uint8_t *)(result + 0x1BD)) == 0) goto loc_0053F794;
    *(uint64_t *)(arg4) = 0;
    *(uint32_t *)(Arg5) = (uint32_t)((uint32_t)(Arg2));
    *(uint64_t *)(result + 0xF0) = 0;
    *(uint32_t *)(result + 0xF8) = 0;
    *(uint64_t *)(result + (int32_t)(Arg3) * 8 + 0x100) = 0;
    *(uint32_t *)(result + (int32_t)(Arg3) * 4 + 0x110) = 0;
    goto loc_0053FA43;
loc_0053F794:
    if (((uint32_t)((uint32_t)(Arg2))) > ((uint32_t)((uint32_t)(*(uint32_t *)(result + (int32_t)(Arg3) * 4 + 0x110))))) goto loc_0053F7B5;
    *(uint32_t *)(Arg5) = (uint32_t)((uint32_t)(Arg2));
    *(uint64_t *)(arg4) = *(uint64_t *)(result + (int32_t)(Arg3) * 8 + 0x100);
    goto loc_0053FA3E;
loc_0053F7B5:
    if (((uint32_t)((uint32_t)(Arg2))) > (*(uint32_t *)(*(uint64_t *)(result + (int32_t)(Arg3) * 8 + 0x100) + 0xE8))) goto loc_0053FB42;
    if ((uint8_t)(v_cr8) != 0) goto loc_0053F932;
    result = HalpDmaAllocateMapRegisters(result, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    local_r10 = 0;
    if (result != 0) goto loc_0053F7EC;
loc_0053F7E2:
    goto loc_0053FB47;
loc_0053F7EC:
    *(uint64_t *)(result + (int32_t)(Arg3) * 8 + 0x100) = result;
    *(uint32_t *)(result + (int32_t)(Arg3) * 4 + 0x110) = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint32_t *)(result + 0x208)) != 3) goto loc_0053F905;
    v_stack_m60 = (uint32_t)(0xC000009AULL) + 24;
    Arg4 = 0;
    Arg2 = ((uint32_t)(Arg2)) << (12);
    Arg3 = 0;
    v_stack_m68 = 0;
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(result + 0x200) + 0x28), Arg2, Arg3, Arg4);
    v_stack_p8 = (uint32_t)(result);
    if (sign_flag) goto loc_0053F918;
    result = HalpIsHvPresent(*(uint64_t *)(*(uint64_t *)(result + 0x200) + 0x28), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0053F905;
    v_stack_m40 = 2;
    v_stack_m30 = (uint32_t)(Arg2);
    result = HalpMmAllocCtxAlloc(*(uint64_t *)(*(uint64_t *)(result + 0x200) + 0x28), (uint32_t)(Arg2) * 8, Arg3, Arg4);
    if (result == 0) goto loc_0053F918;
    v_stack_m38 = result;
    Arg4 = 0;
loc_0053F88E:
    Arg2 = (*(uint64_t *)(result)) >> (12);
    *(uint64_t *)(result + arg4 * 8) = Arg2;
    Arg4 = (uint32_t)((Arg4) + 1);
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_0053F88E;
    Arg2 = 0;
    v_stack_m68 = result + 24;
    result = guard_dispatch_icall(*(uint64_t *)(result + 0x18), Arg2, Arg2 + 3, v_stack_m40);
    v_stack_p8 = (uint32_t)(result);
    result = HalpMmAllocCtxFree(*(uint64_t *)(result + 0x18), result, Arg2 + 3, v_stack_m40);
    if (!sign_flag) goto loc_0053F901;
    result = HalpDmaFreeMapRegisters(result, result, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_m40);
    goto loc_0053FB47;
loc_0053F901:
    *(uint8_t *)(result + 0x40) = 1;
loc_0053F905:
    *(uint32_t *)(Arg5) = (uint32_t)((uint32_t)(Arg2));
    *(uint64_t *)(arg4) = *(uint64_t *)(result + (int32_t)(Arg3) * 8 + 0x100);
    goto loc_0053FA3E;
loc_0053F918:
    result = HalpDmaFreeMapRegisters(result, result, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_m40);
    goto loc_0053FB47;
loc_0053F932:
    if (result + 272 == 0) goto loc_0053F94E;
    if ((*(uint8_t *)(result + 0x1BA)) != 0) goto loc_0053F94E;
    goto loc_0053F95C;
loc_0053F94E:
    if ((*(uint32_t *)(v_rip + 0xA84513)) != 1) goto loc_0053F970;
loc_0053F95C:
    *(uint64_t *)(v_stack_m40) = 0;
    *(uint32_t *)(Arg5) = (uint32_t)((uint32_t)(*(uint32_t *)(result + (int32_t)(Arg3) * 4 + 0x110)));
    goto loc_0053FB47;
loc_0053F970:
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)(result)));
    v_stack_p8 = (uint32_t)(local_r13);
    result = HalpDmaAllocateMapRegistersAtHighLevel(result, v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_m40);
    local_r10 = 0;
    if (result != 0) goto loc_0053F9A4;
    *(uint64_t *)(arg4) = 0;
    *(uint32_t *)(Arg5) = (uint32_t)(result);
    goto loc_0053F7E2;
loc_0053F9A4:
    if (((uint32_t)((uint32_t)(v_stack_p8))) == ((uint32_t)(local_r13))) goto loc_0053F9CB;
    *(uint64_t *)(arg4) = 0;
    *(uint32_t *)(Arg5) = (uint32_t)((uint32_t)(v_stack_p8) + result * 1);
    result = HalpDmaFreeMapRegisters(result, result, (uint32_t)(v_stack_p8), v_stack_m40);
    goto loc_0053F7E2;
loc_0053F9CB:
    if ((*(uint64_t *)(result + (int32_t)(Arg3) * 8 + 0x100)) == 0) goto loc_0053FA14;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + (int32_t)(Arg3) * 4 + 0x110)))) <= 1) goto loc_0053F9FA;
loc_0053F9F0:
    Arg3 = ((uint32_t)(*(uint32_t *)(result + (int32_t)(Arg3) * 4 + 0x110)) - 1) - (1);
    if (condition_is_not_equal) goto loc_0053F9F0;
loc_0053F9FA:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + (int32_t)(Arg3) * 8 + 0x100) + 0x8) + 0x8) = result;
    *(uint32_t *)(result + 0xF8) = (uint32_t)((uint32_t)(Arg2));
    goto loc_0053FA30;
loc_0053FA14:
    *(uint64_t *)(result + 0xF0) = result;
    *(uint32_t *)(result + 0xF8) = (uint32_t)((uint32_t)(Arg2));
    *(uint64_t *)(result + (int32_t)(Arg3) * 8 + 0x100) = result;
    *(uint32_t *)(result + (int32_t)(Arg3) * 4 + 0x110) = (uint32_t)((uint32_t)(Arg2));
loc_0053FA30:
    *(uint64_t *)(arg4) = *(uint64_t *)(result + (int32_t)(Arg3) * 8 + 0x100);
    *(uint32_t *)(Arg5) = (uint32_t)((uint32_t)(Arg2));
loc_0053FA3E:
loc_0053FA43:
    if (*(uint64_t *)(arg4) != 0) {
        *(uint64_t *)(*(uint64_t *)(arg4) + 0x38) = *(uint64_t *)(arg4);
    }
    result = *(uint64_t *)(arg4);
    local_r12 = v_cr8;
    if ((uint8_t)(v_cr8) == 0) {
        Arg1 = v_rip + 11027486;
        result = KeAcquireSpinLockRaiseToDpc(Arg1, *(uint64_t *)(*(uint64_t *)(result + (int32_t)(Arg3) * 8 + 0x100) + 0x8), Arg3, v_stack_m40);
        local_r12 = (uint8_t)(result);
    }
    goto loc_0053FA89;
loc_0053FA7A:
    if ((*(uint64_t *)(v_rip + 0xA8442F) - 288) == result) goto loc_0053FAB6;
loc_0053FA89:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA8442F))) != (v_rip + 11027496)) goto loc_0053FA7A;
    local_rbx = (result) + (288);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA84413))) != (v_rip + 11027496)) goto loc_0053FB3B;
    *(uint64_t *)(local_rbx) = v_rip + 11027496;
    *(uint64_t *)(local_rbx + 0x8) = *(uint64_t *)(v_rip + 0xA84413);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xA84413)) = local_rbx;
    *(uint64_t *)(v_rip + 0xA843F2) = local_rbx;
loc_0053FAB6:
    result = *(uint64_t *)(v_rip + 0xA84413);
    if ((uint8_t)(local_r12) == 0) {
        Arg2 = 0;
        Arg1 = v_rip + 11027388;
        result = KeReleaseSpinLock(Arg1, Arg2, v_rip + 11027496, v_stack_m40);
    }
    if (v_stack_m48 == 0) goto loc_0053FB37;
    if ((uint8_t)(local_r12) == 0) {
        Arg1 = v_rip + 11027438;
        result = KeAcquireSpinLockRaiseToDpc(Arg1, Arg2, v_rip + 11027496, v_stack_m40);
        local_r12 = (uint8_t)(result);
    }
    goto loc_0053FAFE;
loc_0053FAF2:
    if ((*(uint64_t *)(v_rip + 0xA843C7) - 32) == v_stack_m48) goto loc_0053FB24;
loc_0053FAFE:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA843C7))) != (v_rip + 11027392)) goto loc_0053FAF2;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA843AE))) != (v_rip + 11027392)) goto loc_0053FB3B;
    *(uint64_t *)(v_stack_m48 + 0x20) = v_rip + 11027392;
    *(uint64_t *)(v_stack_m48 + 0x20 + 0x8) = *(uint64_t *)(v_rip + 0xA843AE);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xA843AE)) = v_stack_m48 + 32;
    *(uint64_t *)(v_rip + 0xA84394) = v_stack_m48 + 32;
loc_0053FB24:
    result = v_stack_m48 + 32;
    if ((uint8_t)(local_r12) == 0) {
        Arg2 = 0;
        Arg1 = v_rip + 11027350;
        result = KeReleaseSpinLock(Arg1, Arg2, v_rip + 11027392, v_stack_m40);
    }
    result = 0;
    goto loc_0053FB47;
loc_0053FB3B:
loc_0053FB42:
loc_0053FB47:
    return (uint32_t)(0xC000000DULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0053F6D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
