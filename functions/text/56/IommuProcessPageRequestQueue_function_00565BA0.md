# IommuProcessPageRequestQueue

- RVA: `0x00565BA0`–`0x00566051` (길이 `1,201` bytes)
- VA: `0x0000000140565BA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4D9C`
- 디코드: `322`개 명령, `1,201/1,201` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00565C1F` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00565C3F` → [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00565C5A` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x00565C8A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00565CAE` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00565CCC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00565CEC` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00565CF5` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x00565D28` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00565D60` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00565D6A` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x00565D82` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00565DC0` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00565DD3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00565E4C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00565E98` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00565EB4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00565EE3` → [IommupHvValidatePageRequestGpa](IommupHvValidatePageRequestGpa_function_00567894.md) (function, `0x00567894`)
- `0x00565EEF` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x00565F53` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00565F7B` → [IommupHvDismissPageFault](IommupHvDismissPageFault_function_00567288.md) (function, `0x00567288`)
- `0x00565FBB` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00565FE3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00566008` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00566014` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00566028` → [ExfReleasePushLockShared](../26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00566030` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00565BBA` → RVA `0x00FC1710` (`.data`; read)
- `0x00565BD4` → RVA `0x00FC1740` (`.data`; read)
- `0x00565BFD` → RVA `0x00F8FAC8` (`.data`; read)
- `0x00565CC1` → RVA `0x00E06D28` (`.data`; read)
- `0x00565CDD` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00565BA0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00565BA5  55                              push rbp
00565BA6  56                              push rsi
00565BA7  57                              push rdi
00565BA8  41 54                           push r12
00565BAA  41 55                           push r13
00565BAC  41 56                           push r14
00565BAE  41 57                           push r15
00565BB0  48 8B EC                        mov rbp, rsp
00565BB3  48 83 EC 70                     sub rsp, 0x70
00565BB7  45 33 E4                        xor r12d, r12d
00565BBA  44 38 25 4F BB A5 00            cmp byte ptr [rip + 0xa5bb4f], r12b
00565BC1  44 89 65 D0                     mov dword ptr [rbp - 0x30], r12d
00565BC5  4C 89 65 E8                     mov qword ptr [rbp - 0x18], r12
00565BC9  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00565BCD  66 44 89 65 58                  mov word ptr [rbp + 0x58], r12w
00565BD2  75 23                           jne 0x140565bf7
00565BD4  48 8B 1D 65 BB A5 00            mov rbx, qword ptr [rip + 0xa5bb65]
00565BDB  85 C9                           test ecx, ecx
00565BDD  74 0B                           je 0x140565bea
00565BDF  8B C1                           mov eax, ecx
00565BE1  48 8B 1B                        mov rbx, qword ptr [rbx]
00565BE4  48 83 E8 01                     sub rax, 1
00565BE8  75 F7                           jne 0x140565be1
00565BEA  4C 8B 73 10                     mov r14, qword ptr [rbx + 0x10]
00565BEE  48 8D BB 90 01 00 00            lea rdi, [rbx + 0x190]
00565BF5  EB 14                           jmp 0x140565c0b
00565BF7  8B D9                           mov ebx, ecx
00565BF9  48 C1 E3 06                     shl rbx, 6
00565BFD  48 03 1D C4 9E A2 00            add rbx, qword ptr [rip + 0xa29ec4]
00565C04  4C 8B F3                        mov r14, rbx
00565C07  48 8D 7B 18                     lea rdi, [rbx + 0x18]
00565C0B  45 33 C0                        xor r8d, r8d
00565C0E  4C 89 75 F0                     mov qword ptr [rbp - 0x10], r14
00565C12  33 D2                           xor edx, edx
00565C14  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00565C18  48 8B CF                        mov rcx, rdi
00565C1B  44 88 65 50                     mov byte ptr [rbp + 0x50], r12b
00565C1F  E8 0C A6 CA FF                  call 0x140210230
00565C24  48 8B F0                        mov rsi, rax
00565C27  33 C0                           xor eax, eax
00565C29  44 8D 78 11                     lea r15d, [rax + 0x11]
00565C2D  F0 4C 0F B1 3F                  lock cmpxchg qword ptr [rdi], r15
00565C32  74 10                           je 0x140565c44
00565C34  4C 8B CF                        mov r9, rdi
00565C37  4C 8B C6                        mov r8, rsi
00565C3A  33 D2                           xor edx, edx
00565C3C  48 8B CF                        mov rcx, rdi
00565C3F  E8 08 A8 CA FF                  call 0x14021044c
00565C44  48 85 F6                        test rsi, rsi
00565C47  74 04                           je 0x140565c4d
00565C49  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
00565C4D  4C 8D 6F 08                     lea r13, [rdi + 8]
00565C51  41 BF 0F 00 00 00               mov r15d, 0xf
00565C57  49 8B CD                        mov rcx, r13
00565C5A  E8 11 28 CA FF                  call 0x140208470
00565C5F  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00565C63  88 45 48                        mov byte ptr [rbp + 0x48], al
00565C66  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00565C6B  4C 8D 4D 58                     lea r9, [rbp + 0x58]
00565C6F  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00565C73  40 8A F0                        mov sil, al
00565C76  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
00565C7A  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00565C7E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00565C83  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00565C87  49 8B CE                        mov rcx, r14
00565C8A  E8 41 4E 15 00                  call 0x1406baad0
00565C8F  85 C0                           test eax, eax
00565C91  0F 84 77 03 00 00               je 0x14056600e
00565C97  4C 8B 4D E0                     mov r9, qword ptr [rbp - 0x20]
00565C9B  C6 45 50 01                     mov byte ptr [rbp + 0x50], 1
00565C9F  41 F6 C1 20                     test r9b, 0x20
00565CA3  74 10                           je 0x140565cb5
00565CA5  FF 47 10                        inc dword ptr [rdi + 0x10]
00565CA8  40 8A D6                        mov dl, sil
00565CAB  49 8B CD                        mov rcx, r13
00565CAE  E8 ED CE E2 FF                  call 0x140392ba0
00565CB3  EB A2                           jmp 0x140565c57
00565CB5  8B 4D D0                        mov ecx, dword ptr [rbp - 0x30]
00565CB8  83 F9 FF                        cmp ecx, -1
00565CBB  0F 84 28 03 00 00               je 0x140565fe9
00565CC1  48 8B 05 60 10 8A 00            mov rax, qword ptr [rip + 0x8a1060]
00565CC8  48 8B 40 68                     mov rax, qword ptr [rax + 0x68]
00565CCC  E8 FF 4D 15 00                  call 0x1406baad0
00565CD1  48 8B 70 08                     mov rsi, qword ptr [rax + 8]
00565CD5  45 0F 20 C6                     mov r14, cr8
00565CD9  45 0F 22 C7                     mov cr8, r15
00565CDD  44 39 25 3C 10 A6 00            cmp dword ptr [rip + 0xa6103c], r12d
00565CE4  74 0B                           je 0x140565cf1
00565CE6  41 8A D7                        mov dl, r15b
00565CE9  41 8A CE                        mov cl, r14b
00565CEC  E8 0B FA F8 FF                  call 0x1404f56fc
00565CF1  48 8D 4E 18                     lea rcx, [rsi + 0x18]
00565CF5  E8 36 27 CA FF                  call 0x140208430
00565CFA  48 8D 4E 28                     lea rcx, [rsi + 0x28]
00565CFE  48 8B 01                        mov rax, qword ptr [rcx]
00565D01  EB 09                           jmp 0x140565d0c
00565D03  48 39 58 10                     cmp qword ptr [rax + 0x10], rbx
00565D07  74 25                           je 0x140565d2e
00565D09  48 8B 00                        mov rax, qword ptr [rax]
00565D0C  48 3B C1                        cmp rax, rcx
00565D0F  75 F2                           jne 0x140565d03
00565D11  44 8B 4D D0                     mov r9d, dword ptr [rbp - 0x30]
00565D15  BA 03 00 00 00                  mov edx, 3
00565D1A  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00565D1E  B9 59 01 00 00                  mov ecx, 0x159
00565D23  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00565D28  E8 33 79 F9 FF                  call 0x1404fd660
00565D2D  CC                              int3
00565D2E  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00565D32  48 8D 48 18                     lea rcx, [rax + 0x18]
00565D36  4C 8B 39                        mov r15, qword ptr [rcx]
00565D39  EB 0D                           jmp 0x140565d48
00565D3B  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00565D3F  4C 39 40 28                     cmp qword ptr [rax + 0x28], r8
00565D43  74 21                           je 0x140565d66
00565D45  4D 8B 3F                        mov r15, qword ptr [r15]
00565D48  4C 3B F9                        cmp r15, rcx
00565D4B  75 EE                           jne 0x140565d3b
00565D4D  44 8B 4D D0                     mov r9d, dword ptr [rbp - 0x30]
00565D51  BA 04 00 00 00                  mov edx, 4
00565D56  B9 59 01 00 00                  mov ecx, 0x159
00565D5B  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00565D60  E8 FB 78 F9 FF                  call 0x1404fd660
00565D65  CC                              int3
00565D66  48 8D 4E 18                     lea rcx, [rsi + 0x18]
00565D6A  E8 01 09 CA FF                  call 0x140206670
00565D6F  45 33 E4                        xor r12d, r12d
00565D72  44 39 25 A7 0F A6 00            cmp dword ptr [rip + 0xa60fa7], r12d
00565D79  74 0C                           je 0x140565d87
00565D7B  44 0F 20 C1                     mov rcx, cr8
00565D7F  41 8A D6                        mov dl, r14b
00565D82  E8 11 F9 F8 FF                  call 0x1404f5698
00565D87  41 0F B6 C6                     movzx eax, r14b
00565D8B  44 0F 22 C0                     mov cr8, rax
00565D8F  4C 8B 4D E0                     mov r9, qword ptr [rbp - 0x20]
00565D93  41 F6 C1 08                     test r9b, 8
00565D97  0F 85 24 02 00 00               jne 0x140565fc1
00565D9D  41 F6 C1 04                     test r9b, 4
00565DA1  74 11                           je 0x140565db4
00565DA3  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00565DA7  F7 40 20 00 00 02 00            test dword ptr [rax + 0x20], 0x20000
00565DAE  0F 84 E5 01 00 00               je 0x140565f99
00565DB4  45 38 67 38                     cmp byte ptr [r15 + 0x38], r12b
00565DB8  74 27                           je 0x140565de1
00565DBA  8A 55 48                        mov dl, byte ptr [rbp + 0x48]
00565DBD  49 8B CD                        mov rcx, r13
00565DC0  E8 DB CD E2 FF                  call 0x140392ba0
00565DC5  48 8B 05 5C 0F 8A 00            mov rax, qword ptr [rip + 0x8a0f5c]
00565DCC  8B 4D D0                        mov ecx, dword ptr [rbp - 0x30]
00565DCF  48 8B 40 70                     mov rax, qword ptr [rax + 0x70]
00565DD3  E8 F8 4C 15 00                  call 0x1406baad0
00565DD8  4C 8B 75 F0                     mov r14, qword ptr [rbp - 0x10]
00565DDC  E9 70 FE FF FF                  jmp 0x140565c51
00565DE1  49 8B 4F 28                     mov rcx, qword ptr [r15 + 0x28]
00565DE5  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00565DE8  39 41 50                        cmp dword ptr [rcx + 0x50], eax
00565DEB  74 26                           je 0x140565e13
00565DED  B9 58 00 00 00                  mov ecx, 0x58
00565DF2  BA 00 02 00 00                  mov edx, 0x200
00565DF7  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00565DFB  4C 89 24 01                     mov qword ptr [rcx + rax], r12
00565DFF  48 8D 49 08                     lea rcx, [rcx + 8]
00565E03  48 83 EA 01                     sub rdx, 1
00565E07  75 EE                           jne 0x140565df7
00565E09  49 8B 4F 28                     mov rcx, qword ptr [r15 + 0x28]
00565E0D  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00565E10  89 41 50                        mov dword ptr [rcx + 0x50], eax
00565E13  0F B7 75 58                     movzx esi, word ptr [rbp + 0x58]
00565E17  4D 8B 77 28                     mov r14, qword ptr [r15 + 0x28]
00565E1B  41 8B 4C F6 5C                  mov ecx, dword ptr [r14 + rsi*8 + 0x5c]
00565E20  F6 C1 01                        test cl, 1
00565E23  74 2D                           je 0x140565e52
00565E25  8B C1                           mov eax, ecx
00565E27  D1 E8                           shr eax, 1
00565E29  25 FF FF 0F 00                  and eax, 0xfffff
00565E2E  39 45 D0                        cmp dword ptr [rbp - 0x30], eax
00565E31  74 40                           je 0x140565e73
00565E33  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
00565E36  44 8B CE                        mov r9d, esi
00565E39  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00565E3D  BA 05 00 00 00                  mov edx, 5
00565E42  B9 59 01 00 00                  mov ecx, 0x159
00565E47  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00565E4C  E8 0F 78 F9 FF                  call 0x1404fd660
00565E51  CC                              int3
00565E52  83 C9 01                        or ecx, 1
00565E55  8B C1                           mov eax, ecx
00565E57  41 89 4C F6 5C                  mov dword ptr [r14 + rsi*8 + 0x5c], ecx
00565E5C  8B 4D D0                        mov ecx, dword ptr [rbp - 0x30]
00565E5F  25 01 00 E0 FF                  and eax, 0xffe00001
00565E64  81 E1 FF FF 0F 00               and ecx, 0xfffff
00565E6A  03 C9                           add ecx, ecx
00565E6C  0B C8                           or ecx, eax
00565E6E  41 89 4C F6 5C                  mov dword ptr [r14 + rsi*8 + 0x5c], ecx
00565E73  41 FF 44 F6 58                  inc dword ptr [r14 + rsi*8 + 0x58]
00565E78  44 8B E9                        mov r13d, ecx
00565E7B  41 81 E5 00 00 40 00            and r13d, 0x400000
00565E82  F6 45 E0 10                     test byte ptr [rbp - 0x20], 0x10
00565E86  74 09                           je 0x140565e91
00565E88  0F BA E9 15                     bts ecx, 0x15
00565E8C  41 89 4C F6 5C                  mov dword ptr [r14 + rsi*8 + 0x5c], ecx
00565E91  8A 55 48                        mov dl, byte ptr [rbp + 0x48]
00565E94  48 8D 4F 08                     lea rcx, [rdi + 8]
00565E98  E8 03 CD E2 FF                  call 0x140392ba0
00565E9D  48 8B 05 84 0E 8A 00            mov rax, qword ptr [rip + 0x8a0e84]
00565EA4  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
00565EA8  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
00565EAC  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00565EB0  48 8B 40 78                     mov rax, qword ptr [rax + 0x78]
00565EB4  E8 17 4C 15 00                  call 0x1406baad0
00565EB9  80 3D 50 B8 A5 00 00            cmp byte ptr [rip + 0xa5b850], 0
00565EC0  44 8B E0                        mov r12d, eax
00565EC3  74 26                           je 0x140565eeb
00565EC5  85 C0                           test eax, eax
00565EC7  78 22                           js 0x140565eeb
00565EC9  45 85 ED                        test r13d, r13d
00565ECC  75 1D                           jne 0x140565eeb
00565ECE  4C 8B 4D E0                     mov r9, qword ptr [rbp - 0x20]
00565ED2  41 F6 C1 10                     test r9b, 0x10
00565ED6  75 13                           jne 0x140565eeb
00565ED8  4C 8B 45 E8                     mov r8, qword ptr [rbp - 0x18]
00565EDC  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00565EE0  8B 4D D0                        mov ecx, dword ptr [rbp - 0x30]
00565EE3  E8 AC 19 00 00                  call 0x140567894
00565EE8  44 8B E0                        mov r12d, eax
00565EEB  48 8D 4F 08                     lea rcx, [rdi + 8]
00565EEF  E8 7C 25 CA FF                  call 0x140208470
00565EF4  44 8A E8                        mov r13b, al
00565EF7  45 85 E4                        test r12d, r12d
00565EFA  79 07                           jns 0x140565f03
00565EFC  41 0F BA 6C F6 5C 16            bts dword ptr [r14 + rsi*8 + 0x5c], 0x16
00565F03  83 CA FF                        or edx, 0xffffffff
00565F06  41 01 54 F6 58                  add dword ptr [r14 + rsi*8 + 0x58], edx
00565F0B  75 7D                           jne 0x140565f8a
00565F0D  41 8B 44 F6 5C                  mov eax, dword ptr [r14 + rsi*8 + 0x5c]
00565F12  0F BA E0 15                     bt eax, 0x15
00565F16  73 72                           jae 0x140565f8a
00565F18  0F BA E0 16                     bt eax, 0x16
00565F1C  B8 01 00 00 C0                  mov eax, 0xc0000001
00565F21  44 0F 42 E0                     cmovb r12d, eax
00565F25  80 3D E4 B7 A5 00 00            cmp byte ptr [rip + 0xa5b7e4], 0
00565F2C  75 2C                           jne 0x140565f5a
00565F2E  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00565F32  44 0F B7 4D 58                  movzx r9d, word ptr [rbp + 0x58]
00565F37  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00565F3B  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00565F3F  F7 40 30 00 00 02 00            test dword ptr [rax + 0x30], 0x20000
00565F46  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
00565F4A  0F 45 55 D0                     cmovne edx, dword ptr [rbp - 0x30]
00565F4E  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00565F53  E8 78 4B 15 00                  call 0x1406baad0
00565F58  EB 26                           jmp 0x140565f80
00565F5A  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00565F5E  45 8B CC                        mov r9d, r12d
00565F61  44 0F B7 45 58                  movzx r8d, word ptr [rbp + 0x58]
00565F66  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00565F6A  8B 4D D0                        mov ecx, dword ptr [rbp - 0x30]
00565F6D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00565F72  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00565F76  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00565F7B  E8 08 13 00 00                  call 0x140567288
00565F80  45 33 E4                        xor r12d, r12d
00565F83  4D 89 64 F6 58                  mov qword ptr [r14 + rsi*8 + 0x58], r12
00565F88  EB 03                           jmp 0x140565f8d
00565F8A  45 33 E4                        xor r12d, r12d
00565F8D  41 8A D5                        mov dl, r13b
00565F90  4C 8D 6F 08                     lea r13, [rdi + 8]
00565F94  E9 24 FE FF FF                  jmp 0x140565dbd
00565F99  0F B7 45 58                     movzx eax, word ptr [rbp + 0x58]
00565F9D  BA 02 00 00 00                  mov edx, 2
00565FA2  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00565FA6  B9 59 01 00 00                  mov ecx, 0x159
00565FAB  49 C1 E1 10                     shl r9, 0x10
00565FAF  4C 0B C8                        or r9, rax
00565FB2  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00565FB6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00565FBB  E8 A0 76 F9 FF                  call 0x1404fd660
00565FC0  CC                              int3
00565FC1  0F B7 45 58                     movzx eax, word ptr [rbp + 0x58]
00565FC5  BA 01 00 00 00                  mov edx, 1
00565FCA  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00565FCE  B9 59 01 00 00                  mov ecx, 0x159
00565FD3  49 C1 E1 10                     shl r9, 0x10
00565FD7  4C 0B C8                        or r9, rax
00565FDA  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00565FDE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00565FE3  E8 78 76 F9 FF                  call 0x1404fd660
00565FE8  CC                              int3
00565FE9  0F B7 45 58                     movzx eax, word ptr [rbp + 0x58]
00565FED  33 D2                           xor edx, edx
00565FEF  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00565FF3  B9 59 01 00 00                  mov ecx, 0x159
00565FF8  49 C1 E1 10                     shl r9, 0x10
00565FFC  4C 0B C8                        or r9, rax
00565FFF  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00566003  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00566008  E8 53 76 F9 FF                  call 0x1404fd660
0056600D  CC                              int3
0056600E  40 8A D6                        mov dl, sil
00566011  49 8B CD                        mov rcx, r13
00566014  E8 87 CB E2 FF                  call 0x140392ba0
00566019  B8 11 00 00 00                  mov eax, 0x11
0056601E  F0 4C 0F B1 27                  lock cmpxchg qword ptr [rdi], r12
00566023  74 08                           je 0x14056602d
00566025  48 8B CF                        mov rcx, rdi
00566028  E8 13 D4 CF FF                  call 0x140263440
0056602D  48 8B CF                        mov rcx, rdi
00566030  E8 CB B5 D7 FF                  call 0x1402e1600
00566035  8A 45 50                        mov al, byte ptr [rbp + 0x50]
00566038  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
00566040  48 83 C4 70                     add rsp, 0x70
00566044  41 5F                           pop r15
00566046  41 5E                           pop r14
00566048  41 5D                           pop r13
0056604A  41 5C                           pop r12
0056604C  5F                              pop rdi
0056604D  5E                              pop rsi
0056604E  5D                              pop rbp
0056604F  C3                              ret
00566050  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IommuProcessPageRequestQueue(int a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int8 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int16 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (112);
    v_r12 = 0;
    v_stack_m68 = 0;
    v_stack_m50 = 0;
    v_stack_m58 = 0;
    v_stack_p20 = 0;
    if ((*(unsigned __int8 *)(v_rip + 10861391)) != 0) goto loc_00565BF7;
    if (a1 == 0) goto loc_00565BEA;
loc_00565BE1:
    result = ((unsigned int)(a1)) - (1);
    if (condition_is_not_equal) goto loc_00565BE1;
loc_00565BEA:
    goto loc_00565C0B;
loc_00565BF7:
    v_rbx = ((unsigned int)(a1)) << (6);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 10657476));
loc_00565C0B:
    a3 = 0;
    v_stack_m48 = v_rbx;
    a2 = 0;
    v_stack_m60 = 0;
    v_stack_p18 = 0;
    result = KeAbPreAcquire(v_rbx + 24, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rbx + 24;
        a3 = 0;
        a2 = 0;
        a1 = v_rbx + 24;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_00565C51:
loc_00565C57:
    result = KeAcquireSpinLockRaiseToDpc(v_rbx + 24 + 8, a2, a3, a4);
    v_stack_p10 = (unsigned __int8)(result);
    v_stack_m80 = v_stack_m58;
    v_stack_m88 = v_stack_m50;
    result = guard_dispatch_icall(v_rbx, v_stack_m68, v_stack_m60, v_stack_p20);
    if ((unsigned int)(result) == 0) goto loc_0056600E;
    v_stack_p18 = 1;
    if ((((unsigned __int8)(v_stack_m58)) & (32)) == 0) goto loc_00565CB5;
    result = KeReleaseSpinLock(v_rbx + 24 + 8, (unsigned __int8)((unsigned __int8)(result)), v_stack_m60, v_stack_m58);
    goto loc_00565C57;
loc_00565CB5:
    if (((unsigned int)((unsigned int)(v_stack_m68))) == -1) goto loc_00565FE9;
    result = guard_dispatch_icall((unsigned int)(v_stack_m68), (unsigned __int8)((unsigned __int8)(result)), v_stack_m60, v_stack_m58);
    if ((*(unsigned int *)(v_rip + 10883132)) != 0) {
        a2 = 15;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, v_stack_m60, v_stack_m58);
    }
    result = KeAcquireSpinLockAtDpcLevel(*(unsigned __int64 *)(result + 8) + 24, a2, v_stack_m60, v_stack_m58);
    goto loc_00565D0C;
loc_00565D03:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 40) + 16)) == v_rbx) goto loc_00565D2E;
loc_00565D0C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 40))) != (*(unsigned __int64 *)(result + 8) + 40)) goto loc_00565D03;
    v_stack_m88 = v_rbx;
    result = KeBugCheckEx(345, 3, v_stack_m60, (unsigned int)(v_stack_m68));
loc_00565D2E:
    goto loc_00565D48;
loc_00565D3B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 40) + 40)) == v_stack_m60) goto loc_00565D66;
loc_00565D48:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24))) != (result + 24)) goto loc_00565D3B;
    v_stack_m88 = v_rbx;
    result = KeBugCheckEx(345, 4, v_stack_m60, (unsigned int)(v_stack_m68));
loc_00565D66:
    result = KxReleaseSpinLock(*(unsigned __int64 *)(result + 8) + 24, 4, v_stack_m60, (unsigned int)(v_stack_m68));
    v_r12 = 0;
    if ((*(unsigned int *)(v_rip + 10882983)) != 0) {
        a1 = 15;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_m60, (unsigned int)(v_stack_m68));
    }
    if ((((unsigned __int8)(v_stack_m58)) & (8)) != 0) goto loc_00565FC1;
    if ((((unsigned __int8)(v_stack_m58)) & (4)) == 0) goto loc_00565DB4;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) + 40) + 32)) & (0x20000ULL)) == 0) goto loc_00565F99;
loc_00565DB4:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) + 56)) == 0) goto loc_00565DE1;
loc_00565DBD:
    result = KeReleaseSpinLock(v_rbx + 24 + 8, v_stack_p10, v_stack_m60, v_stack_m58);
    result = guard_dispatch_icall((unsigned int)(v_stack_m68), v_stack_p10, v_stack_m60, v_stack_m58);
    goto loc_00565C51;
loc_00565DE1:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) + 40) + 80)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 24 + 16))))) goto loc_00565E13;
loc_00565DF7:
    *(unsigned __int64 *)(88 + *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) + 40) * 1) = 0;
    a2 = (512) - (1);
    if (condition_is_not_equal) goto loc_00565DF7;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) + 40) + 80) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 24 + 16)));
loc_00565E13:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) + 40) + v_stack_p20 * 8 + 92)))) & (1)) == 0) goto loc_00565E52;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) + 40) + v_stack_p20 * 8 + 92))))) >> (1));
    result = (unsigned int)((result) & (0xFFFFFULL));
    if (v_stack_m68 == ((unsigned int)(result))) goto loc_00565E73;
    v_stack_m88 = (unsigned int)(v_stack_m68);
    result = KeBugCheckEx(345, 5, v_stack_m60, (unsigned int)((unsigned int)(v_stack_p20)));
loc_00565E52:
    a1 = (unsigned int)((345) | (1));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) + 40) + v_stack_p20 * 8 + 92) = a1;
    result = (unsigned int)(((unsigned int)(a1)) & (0xFFE00001ULL));
    a1 = (unsigned int)(((unsigned int)(v_stack_m68)) & (0xFFFFFULL));
    a1 = (unsigned int)((a1) + (a1));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) + 40) + v_stack_p20 * 8 + 92) = a1;
loc_00565E73:
    v_r13 = (unsigned int)(((unsigned int)(a1)) & (0x400000ULL));
    if (((v_stack_m58) & (16)) != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) + 40) + v_stack_p20 * 8 + 92) = a1;
    }
    result = KeReleaseSpinLock(v_rbx + 24 + 8, v_stack_p10, v_stack_m60, (unsigned int)((unsigned int)(v_stack_p20)));
    result = guard_dispatch_icall(v_stack_m58, v_stack_m50, (unsigned int)(v_stack_m68), (unsigned int)((unsigned int)(v_stack_p20)));
    if ((*(unsigned __int8 *)(v_rip + 10860624)) == 0) goto loc_00565EEB;
    if (sign_flag) goto loc_00565EEB;
    if ((unsigned int)(v_r13) != 0) goto loc_00565EEB;
    v_r12 = (unsigned int)((unsigned int)(result));
    if ((((unsigned __int8)(v_stack_m58)) & (16)) == 0) {
        a3 = v_stack_m50;
        a2 = v_stack_m60;
        a1 = v_stack_m68;
        result = IommupHvValidatePageRequestGpa(a1, a2, a3, v_stack_m58);
        v_r12 = (unsigned int)(result);
    }
    result = KeAcquireSpinLockRaiseToDpc(v_rbx + 24 + 8, a2, a3, v_stack_m58);
    if (sign_flag) {
    }
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    if (condition_is_not_equal) goto loc_00565F8A;
    if (condition_is_above_or_equal) goto loc_00565F8A;
    if (condition_is_below) { v_r12 = (unsigned int)((unsigned int)(0xC0000001ULL)); }
    if ((*(unsigned __int8 *)(v_rip + 10860516)) != 0) goto loc_00565F5A;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) + 40) + 48)) & (0x20000ULL)) != 0) { a2 = v_stack_m68; }
    v_stack_m88 = (unsigned int)(v_r12);
    result = guard_dispatch_icall(v_stack_m48, a2, v_stack_m60, v_stack_p20);
    goto loc_00565F80;
loc_00565F5A:
    v_stack_m80 = v_stack_m58;
    v_stack_m88 = v_stack_m50;
    result = IommupHvDismissPageFault((unsigned int)(v_stack_m68), v_stack_m60, v_stack_p20, (unsigned int)((unsigned int)(v_r12)));
loc_00565F80:
    v_r12 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24)) + 40) + v_stack_p20 * 8 + 88) = 0;
    goto loc_00565F8D;
loc_00565F8A:
    v_r12 = 0;
loc_00565F8D:
    goto loc_00565DBD;
loc_00565F99:
    a4 = ((unsigned int)((unsigned int)(v_r12))) << (16);
    a4 = (a4) | (v_stack_p20);
    v_stack_m88 = v_stack_m50;
    result = KeBugCheckEx(345, 2, v_stack_m60, a4);
loc_00565FC1:
    a4 = (a4) << (16);
    a4 = (a4) | (v_stack_p20);
    v_stack_m88 = v_stack_m50;
    result = KeBugCheckEx(345, 1, v_stack_m60, a4);
loc_00565FE9:
    a2 = 0;
    a4 = (a4) << (16);
    a4 = (a4) | (v_stack_p20);
    v_stack_m88 = v_stack_m50;
    result = KeBugCheckEx(345, a2, v_stack_m60, a4);
loc_0056600E:
    result = KeReleaseSpinLock(v_rbx + 24 + 8, (unsigned __int8)(v_stack_p20), v_stack_m60, a4);
    result = 17;
    if (!(condition_is_equal)) {
        a1 = v_rbx + 24;
        result = ExfReleasePushLockShared(a1, (unsigned __int8)(v_stack_p20), v_stack_m60, a4);
    }
    result = KeAbPostRelease(v_rbx + 24, (unsigned __int8)(v_stack_p20), v_stack_m60, a4);
    v_rsp = (v_rsp) + (112);
    return v_stack_p18;
}
```

## 5. (Beta) C Style

```c
int64_t IommuProcessPageRequestQueue(int32_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint8_t v_stack_p10;
    uint8_t v_stack_p18;
    uint16_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (112);
    local_r12 = 0;
    v_stack_m68 = 0;
    v_stack_m50 = 0;
    v_stack_m58 = 0;
    v_stack_p20 = 0;
    if ((*(uint8_t *)(v_rip + 0xA5BB4F)) != 0) goto loc_00565BF7;
    if (Arg1 == 0) goto loc_00565BEA;
loc_00565BE1:
    result = ((uint32_t)(Arg1)) - (1);
    if (condition_is_not_equal) goto loc_00565BE1;
loc_00565BEA:
    goto loc_00565C0B;
loc_00565BF7:
    local_rbx = ((uint32_t)(Arg1)) << (6);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xA29EC4));
loc_00565C0B:
    Arg3 = 0;
    v_stack_m48 = local_rbx;
    Arg2 = 0;
    v_stack_m60 = 0;
    v_stack_p18 = 0;
    result = KeAbPreAcquire(local_rbx + 24, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = local_rbx + 24;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_rbx + 24;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_00565C51:
loc_00565C57:
    result = KeAcquireSpinLockRaiseToDpc(local_rbx + 24 + 8, Arg2, Arg3, a4);
    v_stack_p10 = (uint8_t)(result);
    v_stack_m80 = v_stack_m58;
    v_stack_m88 = v_stack_m50;
    result = guard_dispatch_icall(local_rbx, v_stack_m68, v_stack_m60, v_stack_p20);
    if ((uint32_t)(result) == 0) goto loc_0056600E;
    v_stack_p18 = 1;
    if ((((uint8_t)(v_stack_m58)) & (32)) == 0) goto loc_00565CB5;
    result = KeReleaseSpinLock(local_rbx + 24 + 8, (uint8_t)((uint8_t)(result)), v_stack_m60, v_stack_m58);
    goto loc_00565C57;
loc_00565CB5:
    if (((uint32_t)((uint32_t)(v_stack_m68))) == -1) goto loc_00565FE9;
    result = guard_dispatch_icall((uint32_t)(v_stack_m68), (uint8_t)((uint8_t)(result)), v_stack_m60, v_stack_m58);
    if ((*(uint32_t *)(v_rip + 0xA6103C)) != 0) {
        Arg2 = 15;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_m60, v_stack_m58);
    }
    result = KeAcquireSpinLockAtDpcLevel(*(uint64_t *)(result + 0x8) + 24, Arg2, v_stack_m60, v_stack_m58);
    goto loc_00565D0C;
loc_00565D03:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x28) + 0x10)) == local_rbx) goto loc_00565D2E;
loc_00565D0C:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x28))) != (*(uint64_t *)(result + 0x8) + 40)) goto loc_00565D03;
    v_stack_m88 = local_rbx;
    result = KeBugCheckEx(345, 3, v_stack_m60, (uint32_t)(v_stack_m68));
loc_00565D2E:
    goto loc_00565D48;
loc_00565D3B:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x28) + 0x28)) == v_stack_m60) goto loc_00565D66;
loc_00565D48:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x18))) != (result + 24)) goto loc_00565D3B;
    v_stack_m88 = local_rbx;
    result = KeBugCheckEx(345, 4, v_stack_m60, (uint32_t)(v_stack_m68));
loc_00565D66:
    result = KxReleaseSpinLock(*(uint64_t *)(result + 0x8) + 24, 4, v_stack_m60, (uint32_t)(v_stack_m68));
    local_r12 = 0;
    if ((*(uint32_t *)(v_rip + 0xA60FA7)) != 0) {
        Arg1 = 15;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_m60, (uint32_t)(v_stack_m68));
    }
    if ((((uint8_t)(v_stack_m58)) & (8)) != 0) goto loc_00565FC1;
    if ((((uint8_t)(v_stack_m58)) & (4)) == 0) goto loc_00565DB4;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18)) + 0x28) + 0x20)) & (0x20000ULL)) == 0) goto loc_00565F99;
loc_00565DB4:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18)) + 0x38)) == 0) goto loc_00565DE1;
loc_00565DBD:
    result = KeReleaseSpinLock(local_rbx + 24 + 8, v_stack_p10, v_stack_m60, v_stack_m58);
    result = guard_dispatch_icall((uint32_t)(v_stack_m68), v_stack_p10, v_stack_m60, v_stack_m58);
    goto loc_00565C51;
loc_00565DE1:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18)) + 0x28) + 0x50)) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x18 + 0x10))))) goto loc_00565E13;
loc_00565DF7:
    *(uint64_t *)(88 + *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18)) + 0x28) * 1) = 0;
    Arg2 = (512) - (1);
    if (condition_is_not_equal) goto loc_00565DF7;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18)) + 0x28) + 0x50) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x18 + 0x10)));
loc_00565E13:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18)) + 0x28) + v_stack_p20 * 8 + 0x5C)))) & (1)) == 0) goto loc_00565E52;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18)) + 0x28) + v_stack_p20 * 8 + 0x5C))))) >> (1));
    result = (uint32_t)((result) & (0xFFFFFULL));
    if (v_stack_m68 == ((uint32_t)(result))) goto loc_00565E73;
    v_stack_m88 = (uint32_t)(v_stack_m68);
    result = KeBugCheckEx(345, 5, v_stack_m60, (uint32_t)((uint32_t)(v_stack_p20)));
loc_00565E52:
    Arg1 = (uint32_t)((345) | (1));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18)) + 0x28) + v_stack_p20 * 8 + 0x5C) = Arg1;
    result = (uint32_t)(((uint32_t)(Arg1)) & (0xFFE00001ULL));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m68)) & (0xFFFFFULL));
    Arg1 = (uint32_t)((Arg1) + (Arg1));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18)) + 0x28) + v_stack_p20 * 8 + 0x5C) = Arg1;
loc_00565E73:
    local_r13 = (uint32_t)(((uint32_t)(Arg1)) & (0x400000ULL));
    if (((v_stack_m58) & (16)) != 0) {
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18)) + 0x28) + v_stack_p20 * 8 + 0x5C) = Arg1;
    }
    result = KeReleaseSpinLock(local_rbx + 24 + 8, v_stack_p10, v_stack_m60, (uint32_t)((uint32_t)(v_stack_p20)));
    result = guard_dispatch_icall(v_stack_m58, v_stack_m50, (uint32_t)(v_stack_m68), (uint32_t)((uint32_t)(v_stack_p20)));
    if ((*(uint8_t *)(v_rip + 0xA5B850)) == 0) goto loc_00565EEB;
    if (sign_flag) goto loc_00565EEB;
    if ((uint32_t)(local_r13) != 0) goto loc_00565EEB;
    local_r12 = (uint32_t)((uint32_t)(result));
    if ((((uint8_t)(v_stack_m58)) & (16)) == 0) {
        Arg3 = v_stack_m50;
        Arg2 = v_stack_m60;
        Arg1 = v_stack_m68;
        result = IommupHvValidatePageRequestGpa(Arg1, Arg2, Arg3, v_stack_m58);
        local_r12 = (uint32_t)(result);
    }
    result = KeAcquireSpinLockRaiseToDpc(local_rbx + 24 + 8, Arg2, Arg3, v_stack_m58);
    if (sign_flag) {
    }
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    if (condition_is_not_equal) goto loc_00565F8A;
    if (condition_is_above_or_equal) goto loc_00565F8A;
    if (condition_is_below) { local_r12 = (uint32_t)((uint32_t)(0xC0000001ULL)); }
    if ((*(uint8_t *)(v_rip + 0xA5B7E4)) != 0) goto loc_00565F5A;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18)) + 0x28) + 0x30)) & (0x20000ULL)) != 0) { Arg2 = v_stack_m68; }
    v_stack_m88 = (uint32_t)(local_r12);
    result = guard_dispatch_icall(v_stack_m48, Arg2, v_stack_m60, v_stack_p20);
    goto loc_00565F80;
loc_00565F5A:
    v_stack_m80 = v_stack_m58;
    v_stack_m88 = v_stack_m50;
    result = IommupHvDismissPageFault((uint32_t)(v_stack_m68), v_stack_m60, v_stack_p20, (uint32_t)((uint32_t)(local_r12)));
loc_00565F80:
    local_r12 = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18)) + 0x28) + v_stack_p20 * 8 + 0x58) = 0;
    goto loc_00565F8D;
loc_00565F8A:
    local_r12 = 0;
loc_00565F8D:
    goto loc_00565DBD;
loc_00565F99:
    a4 = ((uint32_t)((uint32_t)(local_r12))) << (16);
    a4 = (a4) | (v_stack_p20);
    v_stack_m88 = v_stack_m50;
    result = KeBugCheckEx(345, 2, v_stack_m60, a4);
loc_00565FC1:
    a4 = (a4) << (16);
    a4 = (a4) | (v_stack_p20);
    v_stack_m88 = v_stack_m50;
    result = KeBugCheckEx(345, 1, v_stack_m60, a4);
loc_00565FE9:
    Arg2 = 0;
    a4 = (a4) << (16);
    a4 = (a4) | (v_stack_p20);
    v_stack_m88 = v_stack_m50;
    result = KeBugCheckEx(345, Arg2, v_stack_m60, a4);
loc_0056600E:
    result = KeReleaseSpinLock(local_rbx + 24 + 8, (uint8_t)(v_stack_p20), v_stack_m60, a4);
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = local_rbx + 24;
        result = ExfReleasePushLockShared(Arg1, (uint8_t)(v_stack_p20), v_stack_m60, a4);
    }
    result = KeAbPostRelease(local_rbx + 24, (uint8_t)(v_stack_p20), v_stack_m60, a4);
    local_rsp = (local_rsp) + (112);
    return v_stack_p18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00565BA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
