# MiInitializeReadInProgressPfn

- RVA: `0x002B6990`–`0x002B6F0A` (길이 `1,402` bytes)
- VA: `0x00000001402B6990`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006DA0C`
- 디코드: `331`개 명령, `1,402/1,402` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x002B6A0E` → [MiInPageSkipPage](MiInPageSkipPage_function_002B7820.md) (function, `0x002B7820`)
- `0x002B6A8B` → [MiProtectionToCacheAttribute](MiProtectionToCacheAttribute_function_002B8530.md) (function, `0x002B8530`)
- `0x002B6AA5` → [MiGetContainingPageTable](../34/MiGetContainingPageTable_function_003467F0.md) (function, `0x003467F0`)
- `0x002B6B58` → [MiChangePageAttribute](../33/MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x002B6B66` → [MiSetPfnTbFlushStamp](MiSetPfnTbFlushStamp_function_002B7A70.md) (function, `0x002B7A70`)
- `0x002B6D7E` → [MiSwizzleInvalidPte](../28/MiSwizzleInvalidPte_function_0028F5E0.md) (function, `0x0028F5E0`)
- `0x002B6D96` → [MiIsPrototypePteVadLookup](../32/MiIsPrototypePteVadLookup_function_00328B70.md) (function, `0x00328B70`)
- `0x002B6E05` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x002B6E20` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B6E2F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B6E47` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B6E56` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B6E76` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x002B6E7E` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x002B6E8D` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)

### Direct callers
- [MiPfPutPagesInTransition](../36/MiPfPutPagesInTransition_function_003640EC.md) at `0x00364541`
- [MiPrivateFixup](../36/MiPrivateFixup_function_003693E8.md) at `0x003695E0`
- [MiResolvePageFileFault](../36/MiResolvePageFileFault_function_0036D968.md) at `0x0036E0BB`
- [sub_006E313A](../6E/Unknown_function_006E313A.md) at `0x006E3219`

### Static image references
- `0x002B6D0F` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002B6DA2` → RVA `0x00E2DC80` (`.data`; read)
- `0x002B6DF5` → RVA `0x00011070` (`.rdata`; read)
- `0x002B6E12` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002B6990  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
002B6995  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
002B699A  53                              push rbx
002B699B  55                              push rbp
002B699C  56                              push rsi
002B699D  57                              push rdi
002B699E  41 54                           push r12
002B69A0  41 55                           push r13
002B69A2  41 56                           push r14
002B69A4  41 57                           push r15
002B69A6  48 83 EC 58                     sub rsp, 0x58
002B69AA  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
002B69B4  4C 8B E2                        mov r12, rdx
002B69B7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002B69BC  33 D2                           xor edx, edx
002B69BE  4D 8B D1                        mov r10, r9
002B69C1  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
002B69C6  4C 8B C8                        mov r9, rax
002B69C9  45 33 FF                        xor r15d, r15d
002B69CC  41 8B C0                        mov eax, r8d
002B69CF  4C 8B E9                        mov r13, rcx
002B69D2  49 8D 04 C4                     lea rax, [r12 + rax*8]
002B69D6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002B69DB  4C 3B E0                        cmp r12, rax
002B69DE  0F 83 0C 03 00 00               jae 0x1402b6cf0
002B69E4  8B B4 24 C8 00 00 00            mov esi, dword ptr [rsp + 0xc8]
002B69EB  44 8D 5A 01                     lea r11d, [rdx + 1]
002B69EF  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
002B69F9  49 8B 04 24                     mov rax, qword ptr [r12]
002B69FD  4C 8D 34 40                     lea r14, [rax + rax*2]
002B6A01  49 C1 E6 04                     shl r14, 4
002B6A05  48 8B C1                        mov rax, rcx
002B6A08  4C 03 F0                        add r14, rax
002B6A0B  49 8B CE                        mov rcx, r14
002B6A0E  E8 0D 0E 00 00                  call 0x1402b7820
002B6A13  85 C0                           test eax, eax
002B6A15  0F 85 6B 02 00 00               jne 0x1402b6c86
002B6A1B  49 8B 3A                        mov rdi, qword ptr [r10]
002B6A1E  44 8A C6                        mov r8b, sil
002B6A21  41 C0 E8 06                     shr r8b, 6
002B6A25  33 ED                           xor ebp, ebp
002B6A27  45 22 C3                        and r8b, r11b
002B6A2A  48 8B DF                        mov rbx, rdi
002B6A2D  44 88 84 24 B0 00 00 00         mov byte ptr [rsp + 0xb0], r8b
002B6A35  0F 85 58 03 00 00               jne 0x1402b6d93
002B6A3B  48 8B C7                        mov rax, rdi
002B6A3E  25 00 0C 00 00                  and eax, 0xc00
002B6A43  48 3D 00 08 00 00               cmp rax, 0x800
002B6A49  0F 84 69 04 00 00               je 0x1402b6eb8
002B6A4F  49 89 5E 10                     mov qword ptr [r14 + 0x10], rbx
002B6A53  45 84 C0                        test r8b, r8b
002B6A56  0F 85 D0 02 00 00               jne 0x1402b6d2c
002B6A5C  48 C1 EB 05                     shr rbx, 5
002B6A60  83 E3 1F                        and ebx, 0x1f
002B6A63  40 F6 C6 10                     test sil, 0x10
002B6A67  74 15                           je 0x1402b6a7e
002B6A69  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002B6A6D  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
002B6A77  48 0B C1                        or rax, rcx
002B6A7A  49 89 46 28                     mov qword ptr [r14 + 0x28], rax
002B6A7E  8B CB                           mov ecx, ebx
002B6A80  8B EB                           mov ebp, ebx
002B6A82  83 FB 18                        cmp ebx, 0x18
002B6A85  0F 84 D5 03 00 00               je 0x1402b6e60
002B6A8B  E8 A0 1A 00 00                  call 0x1402b8530
002B6A90  44 8B E8                        mov r13d, eax
002B6A93  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
002B6A9D  4C 3B C8                        cmp r9, rax
002B6AA0  75 25                           jne 0x1402b6ac7
002B6AA2  49 8B CA                        mov rcx, r10
002B6AA5  E8 46 FD 08 00                  call 0x1403467f0
002B6AAA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002B6AAF  4C 8D 3C 40                     lea r15, [rax + rax*2]
002B6AB3  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B6ABD  49 C1 E7 04                     shl r15, 4
002B6AC1  48 8B C8                        mov rcx, rax
002B6AC4  4C 03 F9                        add r15, rcx
002B6AC7  49 8B C2                        mov rax, r10
002B6ACA  48 BA FF FF FF FF FF FF FF 7F   movabs rdx, 0x7fffffffffffffff
002B6AD4  48 23 C2                        and rax, rdx
002B6AD7  40 F6 C6 20                     test sil, 0x20
002B6ADB  49 0F 44 C2                     cmove rax, r10
002B6ADF  33 DB                           xor ebx, ebx
002B6AE1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002B6AE6  8D 73 01                        lea esi, [rbx + 1]
002B6AE9  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
002B6AF0  0F 82 17 02 00 00               jb 0x1402b6d0d
002B6AF6  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B6AFA  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
002B6B02  8B B4 24 C8 00 00 00            mov esi, dword ptr [rsp + 0xc8]
002B6B09  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
002B6B10  C1 E8 10                        shr eax, 0x10
002B6B13  0C 20                           or al, 0x20
002B6B15  48 8D 51 20                     lea rdx, [rcx + 0x20]
002B6B19  88 84 24 AA 00 00 00            mov byte ptr [rsp + 0xaa], al
002B6B20  8B 84 24 A8 00 00 00            mov eax, dword ptr [rsp + 0xa8]
002B6B27  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002B6B2B  48 8B C1                        mov rax, rcx
002B6B2E  48 F7 D8                        neg rax
002B6B31  48 1B C9                        sbb rcx, rcx
002B6B34  48 23 CA                        and rcx, rdx
002B6B37  49 89 0E                        mov qword ptr [r14], rcx
002B6B3A  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B6B3E  C1 E8 10                        shr eax, 0x10
002B6B41  0F B6 C8                        movzx ecx, al
002B6B44  C1 E9 06                        shr ecx, 6
002B6B47  41 3B CD                        cmp ecx, r13d
002B6B4A  74 11                           je 0x1402b6b5d
002B6B4C  41 B8 01 00 00 00               mov r8d, 1
002B6B52  41 8B D5                        mov edx, r13d
002B6B55  49 8B CE                        mov rcx, r14
002B6B58  E8 6F C3 07 00                  call 0x140332ecc
002B6B5D  33 D2                           xor edx, edx
002B6B5F  49 8B CE                        mov rcx, r14
002B6B62  44 8D 42 01                     lea r8d, [rdx + 1]
002B6B66  E8 05 0F 00 00                  call 0x1402b7a70
002B6B6B  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B6B6F  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
002B6B79  48 23 C1                        and rax, rcx
002B6B7C  41 BB 01 00 00 00               mov r11d, 1
002B6B82  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
002B6B86  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B6B8A  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
002B6B91  66 44 89 9C 24 A8 00 00 00      mov word ptr [rsp + 0xa8], r11w
002B6B9A  8B 84 24 A8 00 00 00            mov eax, dword ptr [rsp + 0xa8]
002B6BA1  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002B6BA5  40 F6 C6 08                     test sil, 8
002B6BA9  74 2A                           je 0x1402b6bd5
002B6BAB  41 8B 4E 20                     mov ecx, dword ptr [r14 + 0x20]
002B6BAF  40 8A C6                        mov al, sil
002B6BB2  89 8C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ecx
002B6BB9  24 07                           and al, 7
002B6BBB  C1 E9 18                        shr ecx, 0x18
002B6BBE  80 E1 F8                        and cl, 0xf8
002B6BC1  0A C8                           or cl, al
002B6BC3  88 8C 24 AB 00 00 00            mov byte ptr [rsp + 0xab], cl
002B6BCA  8B 84 24 A8 00 00 00            mov eax, dword ptr [rsp + 0xa8]
002B6BD1  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002B6BD5  49 8B 4E 28                     mov rcx, qword ptr [r14 + 0x28]
002B6BD9  48 BB 00 00 00 00 00 FF FF FF   movabs rbx, 0xffffff0000000000
002B6BE3  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
002B6BE8  48 8B D1                        mov rdx, rcx
002B6BEB  48 8B C1                        mov rax, rcx
002B6BEE  49 33 D1                        xor rdx, r9
002B6BF1  48 23 D3                        and rdx, rbx
002B6BF4  49 33 D1                        xor rdx, r9
002B6BF7  F0 49 0F B1 56 28               lock cmpxchg qword ptr [r14 + 0x28], rdx
002B6BFD  48 3B C8                        cmp rcx, rax
002B6C00  0F 85 FC 00 00 00               jne 0x1402b6d02
002B6C06  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
002B6C0B  49 89 46 08                     mov qword ptr [r14 + 8], rax
002B6C0F  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B6C13  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
002B6C1A  C1 E8 10                        shr eax, 0x10
002B6C1D  24 FA                           and al, 0xfa
002B6C1F  0C 02                           or al, 2
002B6C21  88 84 24 AA 00 00 00            mov byte ptr [rsp + 0xaa], al
002B6C28  8B 84 24 A8 00 00 00            mov eax, dword ptr [rsp + 0xa8]
002B6C2F  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002B6C33  40 84 F6                        test sil, sil
002B6C36  79 05                           jns 0x1402b6c3d
002B6C38  41 80 4E 23 20                  or byte ptr [r14 + 0x23], 0x20
002B6C3D  49 B8 FF FF FF FF FF FF FF 7F   movabs r8, 0x7fffffffffffffff
002B6C47  F0 4D 21 46 18                  lock and qword ptr [r14 + 0x18], r8
002B6C4C  81 E7 00 0C 00 00               and edi, 0xc00
002B6C52  48 81 FF 00 08 00 00            cmp rdi, 0x800
002B6C59  0F 85 FA 00 00 00               jne 0x1402b6d59
002B6C5F  4C 8B 94 24 B8 00 00 00         mov r10, qword ptr [rsp + 0xb8]
002B6C67  80 BC 24 B0 00 00 00 00         cmp byte ptr [rsp + 0xb0], 0
002B6C6F  48 8B 54 24 20                  mov rdx, qword ptr [rsp + 0x20]
002B6C74  4C 8B AC 24 A0 00 00 00         mov r13, qword ptr [rsp + 0xa0]
002B6C7C  75 08                           jne 0x1402b6c86
002B6C7E  49 03 D3                        add rdx, r11
002B6C81  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
002B6C86  49 83 C2 08                     add r10, 8
002B6C8A  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
002B6C94  49 83 C4 08                     add r12, 8
002B6C98  4C 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r10
002B6CA0  4C 3B 64 24 38                  cmp r12, qword ptr [rsp + 0x38]
002B6CA5  0F 82 4E FD FF FF               jb 0x1402b69f9
002B6CAB  48 85 D2                        test rdx, rdx
002B6CAE  74 40                           je 0x1402b6cf0
002B6CB0  33 DB                           xor ebx, ebx
002B6CB2  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
002B6CB9  72 78                           jb 0x1402b6d33
002B6CBB  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B6CBF  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
002B6CC4  48 03 C8                        add rcx, rax
002B6CC7  48 8B D1                        mov rdx, rcx
002B6CCA  48 33 D0                        xor rdx, rax
002B6CCD  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
002B6CD7  48 23 D0                        and rdx, rax
002B6CDA  48 33 D1                        xor rdx, rcx
002B6CDD  49 89 57 18                     mov qword ptr [r15 + 0x18], rdx
002B6CE1  48 BA FF FF FF FF FF FF FF 7F   movabs rdx, 0x7fffffffffffffff
002B6CEB  F0 49 21 57 18                  lock and qword ptr [r15 + 0x18], rdx
002B6CF0  48 83 C4 58                     add rsp, 0x58
002B6CF4  41 5F                           pop r15
002B6CF6  41 5E                           pop r14
002B6CF8  41 5D                           pop r13
002B6CFA  41 5C                           pop r12
002B6CFC  5F                              pop rdi
002B6CFD  5E                              pop rsi
002B6CFE  5D                              pop rbp
002B6CFF  5B                              pop rbx
002B6D00  C3                              ret
002B6D01  CC                              int3
002B6D02  48 8B C8                        mov rcx, rax
002B6D05  48 8B D0                        mov rdx, rax
002B6D08  E9 E1 FE FF FF                  jmp 0x1402b6bee
002B6D0D  03 DE                           add ebx, esi
002B6D0F  85 1D 97 E5 D0 00               test dword ptr [rip + 0xd0e597], ebx
002B6D15  0F 84 F7 00 00 00               je 0x1402b6e12
002B6D1B  F3 90                           pause
002B6D1D  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B6D21  48 85 C0                        test rax, rax
002B6D24  0F 89 BF FD FF FF               jns 0x1402b6ae9
002B6D2A  EB E1                           jmp 0x1402b6d0d
002B6D2C  8B CD                           mov ecx, ebp
002B6D2E  E9 58 FD FF FF                  jmp 0x1402b6a8b
002B6D33  41 03 DB                        add ebx, r11d
002B6D36  85 1D 70 E5 D0 00               test dword ptr [rip + 0xd0e570], ebx
002B6D3C  0F 84 F7 00 00 00               je 0x1402b6e39
002B6D42  F3 90                           pause
002B6D44  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B6D48  41 BB 01 00 00 00               mov r11d, 1
002B6D4E  48 85 C0                        test rax, rax
002B6D51  0F 89 5B FF FF FF               jns 0x1402b6cb2
002B6D57  EB DA                           jmp 0x1402b6d33
002B6D59  49 8B 0C 24                     mov rcx, qword ptr [r12]
002B6D5D  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
002B6D67  48 23 C8                        and rcx, rax
002B6D6A  8B C5                           mov eax, ebp
002B6D6C  48 C1 E1 07                     shl rcx, 7
002B6D70  83 E0 1F                        and eax, 0x1f
002B6D73  48 0B C8                        or rcx, rax
002B6D76  48 83 C9 40                     or rcx, 0x40
002B6D7A  48 C1 E1 05                     shl rcx, 5
002B6D7E  E8 5D 88 FD FF                  call 0x14028f5e0
002B6D83  4C 8B 94 24 B8 00 00 00         mov r10, qword ptr [rsp + 0xb8]
002B6D8B  49 89 02                        mov qword ptr [r10], rax
002B6D8E  E9 D4 FE FF FF                  jmp 0x1402b6c67
002B6D93  48 8B CF                        mov rcx, rdi
002B6D96  E8 D5 1D 07 00                  call 0x140328b70
002B6D9B  85 C0                           test eax, eax
002B6D9D  48 8B C7                        mov rax, rdi
002B6DA0  75 4F                           jne 0x1402b6df1
002B6DA2  48 8B 0D D7 6E B7 00            mov rcx, qword ptr [rip + 0xb76ed7]
002B6DA9  48 85 C9                        test rcx, rcx
002B6DAC  74 13                           je 0x1402b6dc1
002B6DAE  40 F6 C7 10                     test dil, 0x10
002B6DB2  0F 85 F7 00 00 00               jne 0x1402b6eaf
002B6DB8  48 8B C1                        mov rax, rcx
002B6DBB  48 F7 D0                        not rax
002B6DBE  48 23 C7                        and rax, rdi
002B6DC1  48 C1 F8 10                     sar rax, 0x10
002B6DC5  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002B6DCF  48 8B 00                        mov rax, qword ptr [rax]
002B6DD2  48 C1 E8 0C                     shr rax, 0xc
002B6DD6  48 23 C1                        and rax, rcx
002B6DD9  48 8D 0C 40                     lea rcx, [rax + rax*2]
002B6DDD  48 B8 10 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000010
002B6DE7  48 03 C9                        add rcx, rcx
002B6DEA  48 8B C0                        mov rax, rax
002B6DED  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
002B6DF1  48 C1 E8 05                     shr rax, 5
002B6DF5  48 8D 2D 74 A2 D5 FF            lea rbp, [rip - 0x2a5d8c]
002B6DFC  83 E0 1F                        and eax, 0x1f
002B6DFF  8B 6C 85 00                     mov ebp, dword ptr [rbp + rax*4]
002B6E03  8B CD                           mov ecx, ebp
002B6E05  E8 F6 0B 08 00                  call 0x140337a00
002B6E0A  48 8B D8                        mov rbx, rax
002B6E0D  E9 3D FC FF FF                  jmp 0x1402b6a4f
002B6E12  8B 05 A0 FC D0 00               mov eax, dword ptr [rip + 0xd0fca0]
002B6E18  A8 40                           test al, 0x40
002B6E1A  0F 84 FB FE FF FF               je 0x1402b6d1b
002B6E20  E8 6B 86 05 00                  call 0x14030f490
002B6E25  84 C0                           test al, al
002B6E27  0F 84 EE FE FF FF               je 0x1402b6d1b
002B6E2D  8B CB                           mov ecx, ebx
002B6E2F  E8 2C 86 05 00                  call 0x14030f460
002B6E34  E9 E4 FE FF FF                  jmp 0x1402b6d1d
002B6E39  8B 05 79 FC D0 00               mov eax, dword ptr [rip + 0xd0fc79]
002B6E3F  A8 40                           test al, 0x40
002B6E41  0F 84 FB FE FF FF               je 0x1402b6d42
002B6E47  E8 44 86 05 00                  call 0x14030f490
002B6E4C  84 C0                           test al, al
002B6E4E  0F 84 EE FE FF FF               je 0x1402b6d42
002B6E54  8B CB                           mov ecx, ebx
002B6E56  E8 05 86 05 00                  call 0x14030f460
002B6E5B  E9 E4 FE FF FF                  jmp 0x1402b6d44
002B6E60  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
002B6E6A  4C 3B E8                        cmp r13, rax
002B6E6D  0F 87 18 FC FF FF               ja 0x1402b6a8b
002B6E73  41 8B CB                        mov ecx, r11d
002B6E76  E8 75 52 FC FF                  call 0x14027c0f0
002B6E7B  49 8B CD                        mov rcx, r13
002B6E7E  E8 4D FA 05 00                  call 0x1403168d0
002B6E83  B2 11                           mov dl, 0x11
002B6E85  B9 01 00 00 00                  mov ecx, 1
002B6E8A  48 8B E8                        mov rbp, rax
002B6E8D  E8 8E 01 FE FF                  call 0x140297020
002B6E92  8B 4D 30                        mov ecx, dword ptr [rbp + 0x30]
002B6E95  8B EB                           mov ebp, ebx
002B6E97  4C 8B 94 24 B8 00 00 00         mov r10, qword ptr [rsp + 0xb8]
002B6E9F  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
002B6EA4  C1 E9 07                        shr ecx, 7
002B6EA7  83 E1 1F                        and ecx, 0x1f
002B6EAA  E9 DC FB FF FF                  jmp 0x1402b6a8b
002B6EAF  48 83 E0 EF                     and rax, 0xffffffffffffffef
002B6EB3  E9 09 FF FF FF                  jmp 0x1402b6dc1
002B6EB8  48 8B 0D C1 6D B7 00            mov rcx, qword ptr [rip + 0xb76dc1]
002B6EBF  48 8B C7                        mov rax, rdi
002B6EC2  48 85 C9                        test rcx, rcx
002B6EC5  74 0F                           je 0x1402b6ed6
002B6EC7  40 F6 C7 10                     test dil, 0x10
002B6ECB  75 37                           jne 0x1402b6f04
002B6ECD  48 8B C1                        mov rax, rcx
002B6ED0  48 F7 D0                        not rax
002B6ED3  48 23 C7                        and rax, rdi
002B6ED6  48 C1 E8 0C                     shr rax, 0xc
002B6EDA  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002B6EE4  48 23 C1                        and rax, rcx
002B6EE7  48 8D 0C 40                     lea rcx, [rax + rax*2]
002B6EEB  48 B8 10 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000010
002B6EF5  48 03 C9                        add rcx, rcx
002B6EF8  48 8B D8                        mov rbx, rax
002B6EFB  48 8B 1C CB                     mov rbx, qword ptr [rbx + rcx*8]
002B6EFF  E9 4B FB FF FF                  jmp 0x1402b6a4f
002B6F04  48 83 E0 EF                     and rax, 0xffffffffffffffef
002B6F08  EB CC                           jmp 0x1402b6ed6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitializeReadInProgressPfn(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p12;
    unsigned __int8 v_stack_p13;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pB8;

    v_stack_p20 = a4;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (88);
    v_stack_m70 = result;
    a2 = 0;
    v_stack_m78 = 0;
    v_r15 = 0;
    v_stack_m60 = a2 + (unsigned int)(a3) * 8;
    if (0 >= (a2 + (unsigned int)(a3) * 8)) goto loc_002B6CF0;
loc_002B69F9:
    v_r14 = (*(unsigned __int64 *)(a2) + *(unsigned __int64 *)(a2) * 2) << (4);
    v_r14 = (v_r14) + (a1);
    result = MiInPageSkipPage(v_r14, a2, a3, result);
    if ((unsigned int)(result) != 0) goto loc_002B6C86;
    a3 = (unsigned __int8)(((unsigned __int8)((unsigned int)(a6))) >> (6));
    v_rbp = 0;
    a3 = (unsigned __int8)((a3) & ((unsigned __int8)(a2 + 1)));
    v_stack_p18 = (unsigned __int8)(a3);
    if (condition_is_not_equal) goto loc_002B6D93;
    result = (unsigned int)((*(unsigned __int64 *)(a4)) & (0xC00ULL));
    if (result == 0x800ULL) goto loc_002B6EB8;
loc_002B6A4F:
    *(unsigned __int64 *)(v_r14 + 16) = *(unsigned __int64 *)(a4);
    if ((unsigned __int8)(a3) != 0) goto loc_002B6D2C;
    v_rbx = (*(unsigned __int64 *)(a4)) >> (5);
    v_rbx = (unsigned int)((v_rbx) & (31));
    if ((((unsigned __int8)((unsigned int)(a6))) & (16)) != 0) {
        result = *(unsigned __int64 *)(v_r14 + 40);
        result = (result) | (v_r14);
        *(unsigned __int64 *)(v_r14 + 40) = result;
    }
    if (((unsigned int)(v_rbx)) == 24) goto loc_002B6E60;
loc_002B6A8B:
    result = MiProtectionToCacheAttribute((unsigned int)((unsigned int)(v_rbx)), a2, a3, result);
    if (result == result) {
        a1 = a4;
        result = MiGetContainingPageTable(a1, a2, a3, result);
        v_stack_m70 = result;
        v_r15 = result + result * 2;
        v_r15 = (v_r15) << (4);
        a1 = result;
        v_r15 = (v_r15) + (a1);
    }
    result = (a4) & (0);
    if ((((unsigned __int8)((unsigned int)(a6))) & (32)) == 0) { result = a4; }
    v_rbx = 0;
    v_stack_m68 = result;
loc_002B6AE9:
    if (condition_is_below) goto loc_002B6D0D;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 32))) >> (16));
    result = (unsigned __int8)((result) | (32));
    v_stack_p12 = (unsigned __int8)(result);
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_p10));
    result = -(a5);
    a1 = (a5) & (a5 + 32);
    *(unsigned __int64 *)(v_r14) = a1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 32))) >> (16));
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)((unsigned int)(result))))) {
        a3 = 1;
        a2 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = v_r14;
        result = MiChangePageAttribute(a1, a2, a3, result);
    }
    a2 = 0;
    result = MiSetPfnTbFlushStamp(v_r14, a2, a2 + 1, result);
    result = (*(unsigned __int64 *)(v_r14 + 24)) & (v_r14);
    *(unsigned __int64 *)(v_r14 + 24) = result;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    v_stack_p10 = 1;
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_p10));
    result = (unsigned int)(v_stack_p10);
    if ((((unsigned __int8)((unsigned int)(a6))) & (8)) != 0) {
        a1 = *(unsigned int *)(v_r14 + 32);
        result = (unsigned __int8)((unsigned int)(a6));
        v_stack_p10 = (unsigned int)(a1);
        result = (unsigned __int8)((result) & (7));
        a1 = (unsigned int)((a1) >> (24));
        a1 = (unsigned __int8)((a1) & (248));
        a1 = (unsigned __int8)((a1) | ((unsigned __int8)(result)));
        v_stack_p13 = (unsigned __int8)(a1);
        result = v_stack_p10;
        *(unsigned int *)(v_r14 + 32) = (unsigned int)(result);
    }
loc_002B6BEE:
    a2 = (*(unsigned __int64 *)(v_r14 + 40)) ^ (v_stack_m70);
    a2 = (a2) & (0);
    a2 = (a2) ^ (v_stack_m70);
    if ((*(unsigned __int64 *)(v_r14 + 40)) != (*(unsigned __int64 *)(v_r14 + 40))) goto loc_002B6D02;
    *(unsigned __int64 *)(v_r14 + 8) = v_stack_m68;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 32))) >> (16));
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (2));
    v_stack_p12 = (unsigned __int8)(result);
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(v_stack_p10));
    if (sign_flag) {
    }
    v_rdi = (unsigned int)((*(unsigned __int64 *)(a4)) & (0xC00ULL));
    if (v_rdi != 0x800ULL) goto loc_002B6D59;
loc_002B6C67:
    if (v_stack_p18 == 0) {
        a2 = (v_stack_m78) + (1);
        v_stack_m78 = a2;
    }
    v_r10 = (v_stack_p20) + (8);
    v_r12 = (a2) + (8);
    v_stack_p20 = v_r10;
    if (v_r12 < v_stack_m60) goto loc_002B69F9;
    if (a2 == 0) goto loc_002B6CF0;
    v_rbx = 0;
loc_002B6CB2:
    if (condition_is_below) goto loc_002B6D33;
    a1 = (v_stack_m78) + (*(unsigned __int64 *)(v_r15 + 24));
    a2 = (a1) ^ (*(unsigned __int64 *)(v_r15 + 24));
    a2 = (a2) & (*(unsigned __int64 *)(v_r15 + 24));
    a2 = (a2) ^ (a1);
    *(unsigned __int64 *)(v_r15 + 24) = a2;
loc_002B6CF0:
    v_rsp = (v_rsp) + (88);
    return *(unsigned __int64 *)(v_r15 + 24);
loc_002B6D02:
    goto loc_002B6BEE;
loc_002B6D0D:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)((unsigned int)(a6))));
    if (((*(unsigned int *)(v_rip + 13690263)) & ((unsigned int)(v_rbx))) == 0) goto loc_002B6E12;
loc_002B6D1B:
loc_002B6D1D:
    if (!sign_flag) goto loc_002B6AE9;
    goto loc_002B6D0D;
loc_002B6D2C:
    goto loc_002B6A8B;
loc_002B6D33:
    v_rbx = (unsigned int)((v_rbx) + (1));
    if (((*(unsigned int *)(v_rip + 13690224)) & ((unsigned int)(v_rbx))) == 0) goto loc_002B6E39;
loc_002B6D42:
loc_002B6D44:
    if (!sign_flag) goto loc_002B6CB2;
    goto loc_002B6D33;
loc_002B6D59:
    a1 = (*(unsigned __int64 *)(v_r12)) & (*(unsigned __int64 *)(v_r15 + 24));
    a1 = (a1) << (7);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx))))) & (31));
    a1 = (a1) | (result);
    a1 = (a1) | (64);
    a1 = (a1) << (5);
    result = MiSwizzleInvalidPte(a1, *(unsigned __int64 *)(v_r15 + 24), a2 + 1, v_stack_m70);
    *(unsigned __int64 *)(v_stack_pB8) = result;
    goto loc_002B6C67;
loc_002B6D93:
    result = MiIsPrototypePteVadLookup(v_rdi, *(unsigned __int64 *)(v_r15 + 24), a2 + 1, v_stack_m70);
    if ((unsigned int)(result) != 0) goto loc_002B6DF1;
    if (*(unsigned __int64 *)(v_rip + 12021463) == 0) goto loc_002B6DC1;
    if ((((unsigned __int8)(v_rdi)) & (16)) != 0) goto loc_002B6EAF;
    result = ~(*(unsigned __int64 *)(v_rip + 12021463));
    result = (result) & (v_rdi);
loc_002B6DC1:
    result = (result) >> (16);
    result = (*(unsigned __int64 *)(result)) >> (12);
    result = (result) & (*(unsigned __int64 *)(v_rip + 12021463));
    a1 = (result + result * 2) + (result + result * 2);
loc_002B6DF1:
    result = (*(unsigned __int64 *)(result + a1 * 8)) >> (5);
    result = (unsigned int)((result) & (31));
    result = MiMakeDemandZeroPte((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2776460 + result * 4)))), *(unsigned __int64 *)(v_r15 + 24), a2 + 1, v_stack_m70);
    goto loc_002B6A4F;
loc_002B6E12:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13696160)))) & (64)) == 0) goto loc_002B6D1B;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2776460 + result * 4)))), *(unsigned __int64 *)(v_r15 + 24), a2 + 1, v_stack_m70);
    if ((unsigned __int8)(result) == 0) goto loc_002B6D1B;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_r15 + 24), a2 + 1, v_stack_m70);
    goto loc_002B6D1D;
loc_002B6E39:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13696121)))) & (64)) == 0) goto loc_002B6D42;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_r15 + 24), a2 + 1, v_stack_m70);
    if ((unsigned __int8)(result) == 0) goto loc_002B6D42;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(v_r15 + 24), a2 + 1, v_stack_m70);
    goto loc_002B6D44;
loc_002B6E60:
    if (v_stack_p8 > result) goto loc_002B6A8B;
    result = MiLockVadTree(1, *(unsigned __int64 *)(v_r15 + 24), a2 + 1, v_stack_m70);
    result = MiLocateAddress(v_stack_p8, *(unsigned __int64 *)(v_r15 + 24), a2 + 1, v_stack_m70);
    result = MiUnlockVadTree(1, 17, a2 + 1, v_stack_m70);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) >> (7));
    a1 = (unsigned int)((a1) & (31));
    goto loc_002B6A8B;
loc_002B6EAF:
    result = (result) & (-17);
    goto loc_002B6DC1;
loc_002B6EB8:
    if (*(unsigned __int64 *)(v_rip + 12021185) == 0) goto loc_002B6ED6;
    if ((((unsigned __int8)(v_rdi)) & (16)) != 0) goto loc_002B6F04;
    result = ~(*(unsigned __int64 *)(v_rip + 12021185));
    result = (result) & (v_rdi);
loc_002B6ED6:
    result = (result) >> (12);
    result = (result) & (*(unsigned __int64 *)(v_rip + 12021185));
    a1 = (result + result * 2) + (result + result * 2);
    goto loc_002B6A4F;
loc_002B6F04:
    result = (result) & (-17);
    goto loc_002B6ED6;
}
```

## 5. (Beta) C Style

```c
int64_t MiInitializeReadInProgressPfn(int64_t Arg1, void *Arg2, int32_t Arg3, int64_t Arg4, void *Arg5, uint32_t Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_p10;
    uint8_t v_stack_p12;
    uint8_t v_stack_p13;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;
    uint64_t v_stack_pB8;

    v_stack_p20 = Arg4;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (88);
    v_stack_m70 = result;
    Arg2 = 0;
    v_stack_m78 = 0;
    local_r15 = 0;
    v_stack_m60 = Arg2 + (uint32_t)(Arg3) * 8;
    if (0 >= (Arg2 + (uint32_t)(Arg3) * 8)) goto loc_002B6CF0;
loc_002B69F9:
    local_r14 = (*(uint64_t *)(arg2) + *(uint64_t *)(arg2) * 2) << (4);
    local_r14 = (local_r14) + (Arg1);
    result = MiInPageSkipPage(local_r14, Arg2, Arg3, result);
    if ((uint32_t)(result) != 0) goto loc_002B6C86;
    Arg3 = (uint8_t)(((uint8_t)((uint32_t)(Arg6))) >> (6));
    local_rbp = 0;
    Arg3 = (uint8_t)((Arg3) & ((uint8_t)(Arg2 + 1)));
    v_stack_p18 = (uint8_t)(Arg3);
    if (condition_is_not_equal) goto loc_002B6D93;
    result = (uint32_t)((*(uint64_t *)(Arg4)) & (0xC00ULL));
    if (result == 0x800ULL) goto loc_002B6EB8;
loc_002B6A4F:
    *(uint64_t *)(local_r14 + 0x10) = *(uint64_t *)(Arg4);
    if ((uint8_t)(Arg3) != 0) goto loc_002B6D2C;
    local_rbx = (*(uint64_t *)(Arg4)) >> (5);
    local_rbx = (uint32_t)((local_rbx) & (31));
    if ((((uint8_t)((uint32_t)(Arg6))) & (16)) != 0) {
        result = *(uint64_t *)(local_r14 + 0x28);
        result = (result) | (local_r14);
        *(uint64_t *)(local_r14 + 0x28) = result;
    }
    if (((uint32_t)(local_rbx)) == 24) goto loc_002B6E60;
loc_002B6A8B:
    result = MiProtectionToCacheAttribute((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, result);
    if (result == result) {
        Arg1 = Arg4;
        result = MiGetContainingPageTable(Arg1, Arg2, Arg3, result);
        v_stack_m70 = result;
        local_r15 = result + result * 2;
        local_r15 = (local_r15) << (4);
        Arg1 = result;
        local_r15 = (local_r15) + (Arg1);
    }
    result = (Arg4) & (0);
    if ((((uint8_t)((uint32_t)(Arg6))) & (32)) == 0) { result = Arg4; }
    local_rbx = 0;
    v_stack_m68 = result;
loc_002B6AE9:
    if (condition_is_below) goto loc_002B6D0D;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) >> (16));
    result = (uint8_t)((result) | (32));
    v_stack_p12 = (uint8_t)(result);
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_p10));
    result = -(Arg5);
    Arg1 = (Arg5) & (Arg5 + 32);
    *(uint64_t *)(local_r14) = Arg1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) >> (16));
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)((uint32_t)(result))))) {
        Arg3 = 1;
        Arg2 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = local_r14;
        result = MiChangePageAttribute(Arg1, Arg2, Arg3, result);
    }
    Arg2 = 0;
    result = MiSetPfnTbFlushStamp(local_r14, Arg2, Arg2 + 1, result);
    result = (*(uint64_t *)(local_r14 + 0x18)) & (local_r14);
    *(uint64_t *)(local_r14 + 0x18) = result;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    v_stack_p10 = 1;
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_p10));
    result = (uint32_t)(v_stack_p10);
    if ((((uint8_t)((uint32_t)(Arg6))) & (8)) != 0) {
        Arg1 = *(uint32_t *)(local_r14 + 0x20);
        result = (uint8_t)((uint32_t)(Arg6));
        v_stack_p10 = (uint32_t)(Arg1);
        result = (uint8_t)((result) & (7));
        Arg1 = (uint32_t)((Arg1) >> (24));
        Arg1 = (uint8_t)((Arg1) & (248));
        Arg1 = (uint8_t)((Arg1) | ((uint8_t)(result)));
        v_stack_p13 = (uint8_t)(Arg1);
        result = v_stack_p10;
        *(uint32_t *)(local_r14 + 0x20) = (uint32_t)(result);
    }
loc_002B6BEE:
    Arg2 = (*(uint64_t *)(local_r14 + 0x28)) ^ (v_stack_m70);
    Arg2 = (Arg2) & (0);
    Arg2 = (Arg2) ^ (v_stack_m70);
    if ((*(uint64_t *)(local_r14 + 0x28)) != (*(uint64_t *)(local_r14 + 0x28))) goto loc_002B6D02;
    *(uint64_t *)(local_r14 + 0x8) = v_stack_m68;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) >> (16));
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (2));
    v_stack_p12 = (uint8_t)(result);
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(v_stack_p10));
    if (sign_flag) {
    }
    local_rdi = (uint32_t)((*(uint64_t *)(Arg4)) & (0xC00ULL));
    if (local_rdi != 0x800ULL) goto loc_002B6D59;
loc_002B6C67:
    if (v_stack_p18 == 0) {
        Arg2 = (v_stack_m78) + (1);
        v_stack_m78 = Arg2;
    }
    local_r10 = (v_stack_p20) + (8);
    local_r12 = (Arg2) + (8);
    v_stack_p20 = local_r10;
    if (local_r12 < v_stack_m60) goto loc_002B69F9;
    if (Arg2 == NULL) goto loc_002B6CF0;
    local_rbx = 0;
loc_002B6CB2:
    if (condition_is_below) goto loc_002B6D33;
    Arg1 = (v_stack_m78) + (*(uint64_t *)(local_r15 + 0x18));
    Arg2 = (Arg1) ^ (*(uint64_t *)(local_r15 + 0x18));
    Arg2 = (Arg2) & (*(uint64_t *)(local_r15 + 0x18));
    Arg2 = (Arg2) ^ (Arg1);
    *(void **)(local_r15 + 0x18) = Arg2;
loc_002B6CF0:
    local_rsp = (local_rsp) + (88);
    return *(uint64_t *)(local_r15 + 0x18);
loc_002B6D02:
    goto loc_002B6BEE;
loc_002B6D0D:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)((uint32_t)(Arg6))));
    if (((*(uint32_t *)(v_rip + 0xD0E597)) & ((uint32_t)(local_rbx))) == 0) goto loc_002B6E12;
loc_002B6D1B:
loc_002B6D1D:
    if (!sign_flag) goto loc_002B6AE9;
    goto loc_002B6D0D;
loc_002B6D2C:
    goto loc_002B6A8B;
loc_002B6D33:
    local_rbx = (uint32_t)((local_rbx) + (1));
    if (((*(uint32_t *)(v_rip + 0xD0E570)) & ((uint32_t)(local_rbx))) == 0) goto loc_002B6E39;
loc_002B6D42:
loc_002B6D44:
    if (!sign_flag) goto loc_002B6CB2;
    goto loc_002B6D33;
loc_002B6D59:
    Arg1 = (*(uint64_t *)(local_r12)) & (*(uint64_t *)(local_r15 + 0x18));
    Arg1 = (Arg1) << (7);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx))))) & (31));
    Arg1 = (Arg1) | (result);
    Arg1 = (Arg1) | (64);
    Arg1 = (Arg1) << (5);
    result = MiSwizzleInvalidPte(Arg1, *(uint64_t *)(local_r15 + 0x18), Arg2 + 1, v_stack_m70);
    *(uint64_t *)(v_stack_pB8) = result;
    goto loc_002B6C67;
loc_002B6D93:
    result = MiIsPrototypePteVadLookup(local_rdi, *(uint64_t *)(local_r15 + 0x18), Arg2 + 1, v_stack_m70);
    if ((uint32_t)(result) != 0) goto loc_002B6DF1;
    if (*(uint64_t *)(v_rip + 0xB76ED7) == 0) goto loc_002B6DC1;
    if ((((uint8_t)(local_rdi)) & (16)) != 0) goto loc_002B6EAF;
    result = ~(*(uint64_t *)(v_rip + 0xB76ED7));
    result = (result) & (local_rdi);
loc_002B6DC1:
    result = (result) >> (16);
    result = (*(uint64_t *)(result)) >> (12);
    result = (result) & (*(uint64_t *)(v_rip + 0xB76ED7));
    Arg1 = (result + result * 2) + (result + result * 2);
loc_002B6DF1:
    result = (*(uint64_t *)(result + Arg1 * 8)) >> (5);
    result = (uint32_t)((result) & (31));
    result = MiMakeDemandZeroPte((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x2A5D8C + result * 4)))), *(uint64_t *)(local_r15 + 0x18), Arg2 + 1, v_stack_m70);
    goto loc_002B6A4F;
loc_002B6E12:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD0FCA0)))) & (64)) == 0) goto loc_002B6D1B;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x2A5D8C + result * 4)))), *(uint64_t *)(local_r15 + 0x18), Arg2 + 1, v_stack_m70);
    if ((uint8_t)(result) == 0) goto loc_002B6D1B;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(result)), *(uint64_t *)(local_r15 + 0x18), Arg2 + 1, v_stack_m70);
    goto loc_002B6D1D;
loc_002B6E39:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD0FC79)))) & (64)) == 0) goto loc_002B6D42;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(result)), *(uint64_t *)(local_r15 + 0x18), Arg2 + 1, v_stack_m70);
    if ((uint8_t)(result) == 0) goto loc_002B6D42;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(result)), *(uint64_t *)(local_r15 + 0x18), Arg2 + 1, v_stack_m70);
    goto loc_002B6D44;
loc_002B6E60:
    if (v_stack_p8 > result) goto loc_002B6A8B;
    result = MiLockVadTree(1, *(uint64_t *)(local_r15 + 0x18), Arg2 + 1, v_stack_m70);
    result = MiLocateAddress(v_stack_p8, *(uint64_t *)(local_r15 + 0x18), Arg2 + 1, v_stack_m70);
    result = MiUnlockVadTree(1, 17, Arg2 + 1, v_stack_m70);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) >> (7));
    Arg1 = (uint32_t)((Arg1) & (31));
    goto loc_002B6A8B;
loc_002B6EAF:
    result = (result) & (-17);
    goto loc_002B6DC1;
loc_002B6EB8:
    if (*(uint64_t *)(v_rip + 0xB76DC1) == 0) goto loc_002B6ED6;
    if ((((uint8_t)(local_rdi)) & (16)) != 0) goto loc_002B6F04;
    result = ~(*(uint64_t *)(v_rip + 0xB76DC1));
    result = (result) & (local_rdi);
loc_002B6ED6:
    result = (result) >> (12);
    result = (result) & (*(uint64_t *)(v_rip + 0xB76DC1));
    Arg1 = (result + result * 2) + (result + result * 2);
    goto loc_002B6A4F;
loc_002B6F04:
    result = (result) & (-17);
    goto loc_002B6ED6;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg5` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B6990&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
