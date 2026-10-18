# KiAdjustUserIsolationDomainThread

- RVA: `0x005C3B54`–`0x005C3F7F` (길이 `1,067` bytes)
- VA: `0x00000001405C3B54`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CA9A8`
- 디코드: `255`개 명령, `1,067/1,067` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x005C3B9E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005C3BCE` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x005C3C91` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x005C3CE2` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x005C3D60` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x005C3D7C` → [KeYieldProcessorEx](../3F/KeYieldProcessorEx_function_003FBD00.md) (function, `0x003FBD00`)
- `0x005C3DFC` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x005C3E32` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x005C3E50` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x005C3E76` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x005C3EBA` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005C3EC7` → [KeAddProcessorAffinityEx](../25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x005C3EE2` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x005C3F0A` → [KiIpiSendPacket](../47/KiIpiSendPacket_function_004711DC.md) (function, `0x004711DC`)
- `0x005C3F0F` → [KiIpiStallOnPacketTargets](../47/KiIpiStallOnPacketTargets_function_004718D8.md) (function, `0x004718D8`)
- `0x005C3F24` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x005C3F42` → [KiReleaseThreadStateLock](../21/KiReleaseThreadStateLock_function_00217910.md) (function, `0x00217910`)
- `0x005C3F5E` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PspSynchronizeThreadIsolationDomains](../3C/PspSynchronizeThreadIsolationDomains_function_003C479C.md) at `0x003C4807`
- [KeEnableCoreIsolationMitigationPolicyThread](KeEnableCoreIsolationMitigationPolicyThread_function_005C35B4.md) at `0x005C3612`

### Static image references
- `0x005C3B75` → RVA `0x00E0A740` (`.data`; read)
- `0x005C3C1E` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x005C3D2C` → RVA `0x00FC6B38` (`ALMOSTRO`; read)
- `0x005C3ED9` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x005C3EFC` → RVA `0x005C44D0` (`KiIpiUpdateUserIsolationDomain`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005C3B54  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
005C3B59  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
005C3B5E  55                              push rbp
005C3B5F  56                              push rsi
005C3B60  57                              push rdi
005C3B61  41 54                           push r12
005C3B63  41 55                           push r13
005C3B65  41 56                           push r14
005C3B67  41 57                           push r15
005C3B69  48 8D 6C 24 80                  lea rbp, [rsp - 0x80]
005C3B6E  48 81 EC 80 01 00 00            sub rsp, 0x180
005C3B75  48 8B 05 C4 6B 84 00            mov rax, qword ptr [rip + 0x846bc4]
005C3B7C  48 33 C4                        xor rax, rsp
005C3B7F  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
005C3B83  45 8A E8                        mov r13b, r8b
005C3B86  44 88 44 24 30                  mov byte ptr [rsp + 0x30], r8b
005C3B8B  48 8B FA                        mov rdi, rdx
005C3B8E  48 8B D9                        mov rbx, rcx
005C3B91  33 D2                           xor edx, edx
005C3B93  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
005C3B98  41 B8 08 01 00 00               mov r8d, 0x108
005C3B9E  E8 9D 30 10 00                  call 0x1406c6c40
005C3BA3  45 33 C0                        xor r8d, r8d
005C3BA6  0F 57 C0                        xorps xmm0, xmm0
005C3BA9  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
005C3BAE  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
005C3BB3  45 84 ED                        test r13b, r13b
005C3BB6  75 35                           jne 0x1405c3bed
005C3BB8  45 33 ED                        xor r13d, r13d
005C3BBB  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
005C3BC0  F0 48 0F BA 6B 40 00            lock bts qword ptr [rbx + 0x40], 0
005C3BC7  73 15                           jae 0x1405c3bde
005C3BC9  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
005C3BCE  E8 2D 81 E3 FF                  call 0x1403fbd00
005C3BD3  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
005C3BD7  48 85 C0                        test rax, rax
005C3BDA  75 ED                           jne 0x1405c3bc9
005C3BDC  EB E2                           jmp 0x1405c3bc0
005C3BDE  48 8B BD C8 00 00 00            mov rdi, qword ptr [rbp + 0xc8]
005C3BE5  45 33 C0                        xor r8d, r8d
005C3BE8  44 8A 6C 24 30                  mov r13b, byte ptr [rsp + 0x30]
005C3BED  4C 8B A3 18 07 00 00            mov r12, qword ptr [rbx + 0x718]
005C3BF4  4C 3B E7                        cmp r12, rdi
005C3BF7  0F 84 4A 03 00 00               je 0x1405c3f47
005C3BFD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
005C3C06  48 3B D8                        cmp rbx, rax
005C3C09  75 13                           jne 0x1405c3c1e
005C3C0B  48 8B 85 C8 00 00 00            mov rax, qword ptr [rbp + 0xc8]
005C3C12  48 89 83 18 07 00 00            mov qword ptr [rbx + 0x718], rax
005C3C19  E9 29 03 00 00                  jmp 0x1405c3f47
005C3C1E  4C 8D 15 1B 50 A0 00            lea r10, [rip + 0xa0501b]
005C3C25  41 B9 01 00 00 00               mov r9d, 1
005C3C2B  BA 02 00 00 00                  mov edx, 2
005C3C30  44 0F B6 BB 84 01 00 00         movzx r15d, byte ptr [rbx + 0x184]
005C3C38  49 8B F8                        mov rdi, r8
005C3C3B  41 8B CF                        mov ecx, r15d
005C3C3E  49 8B F0                        mov rsi, r8
005C3C41  83 E9 01                        sub ecx, 1
005C3C44  0F 84 CB 00 00 00               je 0x1405c3d15
005C3C4A  83 E9 01                        sub ecx, 1
005C3C4D  74 28                           je 0x1405c3c77
005C3C4F  83 E9 01                        sub ecx, 1
005C3C52  74 70                           je 0x1405c3cc4
005C3C54  3B CA                           cmp ecx, edx
005C3C56  0F 85 2A 02 00 00               jne 0x1405c3e86
005C3C5C  8A 43 70                        mov al, byte ptr [rbx + 0x70]
005C3C5F  24 07                           and al, 7
005C3C61  41 3A C1                        cmp al, r9b
005C3C64  0F 84 1C 02 00 00               je 0x1405c3e86
005C3C6A  2C 03                           sub al, 3
005C3C6C  3C 03                           cmp al, 3
005C3C6E  0F 86 12 02 00 00               jbe 0x1405c3e86
005C3C74  44 8A FA                        mov r15b, dl
005C3C77  44 8B B3 18 02 00 00            mov r14d, dword ptr [rbx + 0x218]
005C3C7E  45 85 F6                        test r14d, r14d
005C3C81  78 AD                           js 0x1405c3c30
005C3C83  4B 8B 3C F2                     mov rdi, qword ptr [r10 + r14*8]
005C3C87  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
005C3C8C  48 8B CF                        mov rcx, rdi
005C3C8F  33 D2                           xor edx, edx
005C3C91  E8 CA B0 D4 FF                  call 0x14030ed60
005C3C96  48 3B 5F 08                     cmp rbx, qword ptr [rdi + 8]
005C3C9A  0F 84 E6 01 00 00               je 0x1405c3e86
005C3CA0  8A 83 84 01 00 00               mov al, byte ptr [rbx + 0x184]
005C3CA6  3C 02                           cmp al, 2
005C3CA8  0F 85 C3 01 00 00               jne 0x1405c3e71
005C3CAE  8B 83 18 02 00 00               mov eax, dword ptr [rbx + 0x218]
005C3CB4  41 3B C6                        cmp eax, r14d
005C3CB7  0F 85 B4 01 00 00               jne 0x1405c3e71
005C3CBD  B9 4A 00 00 00                  mov ecx, 0x4a
005C3CC2  CD 29                           int 0x29
005C3CC4  44 8B B3 18 02 00 00            mov r14d, dword ptr [rbx + 0x218]
005C3CCB  45 85 F6                        test r14d, r14d
005C3CCE  0F 88 5C FF FF FF               js 0x1405c3c30
005C3CD4  4B 8B 3C F2                     mov rdi, qword ptr [r10 + r14*8]
005C3CD8  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
005C3CDD  48 8B CF                        mov rcx, rdi
005C3CE0  33 D2                           xor edx, edx
005C3CE2  E8 79 B0 D4 FF                  call 0x14030ed60
005C3CE7  48 3B 5F 10                     cmp rbx, qword ptr [rdi + 0x10]
005C3CEB  0F 84 95 01 00 00               je 0x1405c3e86
005C3CF1  8A 83 84 01 00 00               mov al, byte ptr [rbx + 0x184]
005C3CF7  3C 03                           cmp al, 3
005C3CF9  0F 85 72 01 00 00               jne 0x1405c3e71
005C3CFF  8B 83 18 02 00 00               mov eax, dword ptr [rbx + 0x218]
005C3D05  41 3B C6                        cmp eax, r14d
005C3D08  0F 85 63 01 00 00               jne 0x1405c3e71
005C3D0E  B9 1E 00 00 00                  mov ecx, 0x1e
005C3D13  CD 29                           int 0x29
005C3D15  44 8B B3 18 02 00 00            mov r14d, dword ptr [rbx + 0x218]
005C3D1C  45 85 F6                        test r14d, r14d
005C3D1F  0F 89 1D 01 00 00               jns 0x1405c3e42
005C3D25  41 8B C6                        mov eax, r14d
005C3D28  0F BA F0 1F                     btr eax, 0x1f
005C3D2C  F7 05 02 2E A0 00 00 00 20 00   test dword ptr [rip + 0xa02e02], 0x200000
005C3D36  49 8B 04 C2                     mov rax, qword ptr [r10 + rax*8]
005C3D3A  48 8B B0 48 8E 00 00            mov rsi, qword ptr [rax + 0x8e48]
005C3D41  74 24                           je 0x1405c3d67
005C3D43  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
005C3D48  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
005C3D4D  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
005C3D52  90                              nop
005C3D53  48 87 16                        xchg qword ptr [rsi], rdx
005C3D56  48 85 D2                        test rdx, rdx
005C3D59  74 45                           je 0x1405c3da0
005C3D5B  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
005C3D60  E8 4B 41 C9 FF                  call 0x140257eb0
005C3D65  EB 29                           jmp 0x1405c3d90
005C3D67  45 33 ED                        xor r13d, r13d
005C3D6A  44 89 6C 24 54                  mov dword ptr [rsp + 0x54], r13d
005C3D6F  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
005C3D75  73 14                           jae 0x1405c3d8b
005C3D77  48 8D 4C 24 54                  lea rcx, [rsp + 0x54]
005C3D7C  E8 7F 7F E3 FF                  call 0x1403fbd00
005C3D81  48 8B 06                        mov rax, qword ptr [rsi]
005C3D84  48 85 C0                        test rax, rax
005C3D87  75 EE                           jne 0x1405c3d77
005C3D89  EB E4                           jmp 0x1405c3d6f
005C3D8B  44 8A 6C 24 30                  mov r13b, byte ptr [rsp + 0x30]
005C3D90  4C 8D 15 A9 4E A0 00            lea r10, [rip + 0xa04ea9]
005C3D97  41 B9 01 00 00 00               mov r9d, 1
005C3D9D  45 33 C0                        xor r8d, r8d
005C3DA0  8A 83 84 01 00 00               mov al, byte ptr [rbx + 0x184]
005C3DA6  41 3A C1                        cmp al, r9b
005C3DA9  75 0F                           jne 0x1405c3dba
005C3DAB  8B 83 18 02 00 00               mov eax, dword ptr [rbx + 0x218]
005C3DB1  41 3B C6                        cmp eax, r14d
005C3DB4  0F 84 C9 00 00 00               je 0x1405c3e83
005C3DBA  F7 05 74 2D A0 00 00 00 20 00   test dword ptr [rip + 0xa02d74], 0x200000
005C3DC4  74 73                           je 0x1405c3e39
005C3DC6  0F 0D 4C 24 40                  prefetchw byte ptr [rsp + 0x40]
005C3DCB  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
005C3DD0  48 85 C0                        test rax, rax
005C3DD3  75 33                           jne 0x1405c3e08
005C3DD5  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
005C3DDA  48 8D 44 24 40                  lea rax, [rsp + 0x40]
005C3DDF  F0 4C 0F B1 01                  lock cmpxchg qword ptr [rcx], r8
005C3DE4  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
005C3DE9  BA 02 00 00 00                  mov edx, 2
005C3DEE  48 3B C1                        cmp rax, rcx
005C3DF1  0F 84 39 FE FF FF               je 0x1405c3c30
005C3DF7  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
005C3DFC  E8 9F 3C C5 FF                  call 0x140217aa0
005C3E01  45 33 C0                        xor r8d, r8d
005C3E04  45 8D 48 01                     lea r9d, [r8 + 1]
005C3E08  48 8D 48 08                     lea rcx, [rax + 8]
005C3E0C  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
005C3E11  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
005C3E16  4C 8D 15 23 4E A0 00            lea r10, [rip + 0xa04e23]
005C3E1D  48 8B C2                        mov rax, rdx
005C3E20  48 87 01                        xchg qword ptr [rcx], rax
005C3E23  32 C2                           xor al, dl
005C3E25  BA 02 00 00 00                  mov edx, 2
005C3E2A  A8 04                           test al, 4
005C3E2C  0F 84 FE FD FF FF               je 0x1405c3c30
005C3E32  E8 E9 3D C5 FF                  call 0x140217c20
005C3E37  EB 42                           jmp 0x1405c3e7b
005C3E39  F0 4C 21 06                     lock and qword ptr [rsi], r8
005C3E3D  E9 E9 FD FF FF                  jmp 0x1405c3c2b
005C3E42  4B 8B 3C F2                     mov rdi, qword ptr [r10 + r14*8]
005C3E46  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
005C3E4B  48 8B CF                        mov rcx, rdi
005C3E4E  33 D2                           xor edx, edx
005C3E50  E8 0B AF D4 FF                  call 0x14030ed60
005C3E55  8A 83 84 01 00 00               mov al, byte ptr [rbx + 0x184]
005C3E5B  41 B9 01 00 00 00               mov r9d, 1
005C3E61  41 3A C1                        cmp al, r9b
005C3E64  75 0B                           jne 0x1405c3e71
005C3E66  8B 83 18 02 00 00               mov eax, dword ptr [rbx + 0x218]
005C3E6C  41 3B C6                        cmp eax, r14d
005C3E6F  74 15                           je 0x1405c3e86
005C3E71  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
005C3E76  E8 D5 5D DD FF                  call 0x140399c50
005C3E7B  45 33 C0                        xor r8d, r8d
005C3E7E  E9 9B FD FF FF                  jmp 0x1405c3c1e
005C3E83  49 8B F8                        mov rdi, r8
005C3E86  41 BE 02 00 00 00               mov r14d, 2
005C3E8C  45 3A FE                        cmp r15b, r14b
005C3E8F  74 13                           je 0x1405c3ea4
005C3E91  48 8B 85 C8 00 00 00            mov rax, qword ptr [rbp + 0xc8]
005C3E98  48 89 83 18 07 00 00            mov qword ptr [rbx + 0x718], rax
005C3E9F  E9 89 00 00 00                  jmp 0x1405c3f2d
005C3EA4  33 D2                           xor edx, edx
005C3EA6  48 C7 44 24 60 01 00 20 00      mov qword ptr [rsp + 0x60], 0x200001
005C3EAF  41 B8 00 01 00 00               mov r8d, 0x100
005C3EB5  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
005C3EBA  E8 81 2D 10 00                  call 0x1406c6c40
005C3EBF  8B 57 24                        mov edx, dword ptr [rdi + 0x24]
005C3EC2  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
005C3EC7  E8 24 78 C9 FF                  call 0x14025b6f0
005C3ECC  44 0F 20 C1                     mov rcx, cr8
005C3ED0  BA 0C 00 00 00                  mov edx, 0xc
005C3ED5  44 0F 22 C2                     mov cr8, rdx
005C3ED9  83 3D 40 2E A0 00 00            cmp dword ptr [rip + 0xa02e40], 0
005C3EE0  74 05                           je 0x1405c3ee7
005C3EE2  E8 15 18 F3 FF                  call 0x1404f56fc
005C3EE7  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005C3EED  48 8D 85 C8 00 00 00            lea rax, [rbp + 0xc8]
005C3EF4  4C 8B CB                        mov r9, rbx
005C3EF7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005C3EFC  4C 8D 05 CD 05 00 00            lea r8, [rip + 0x5cd]
005C3F03  33 C9                           xor ecx, ecx
005C3F05  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
005C3F0A  E8 CD D2 EA FF                  call 0x1404711dc
005C3F0F  E8 C4 D9 EA FF                  call 0x1404718d8
005C3F14  83 3D 05 2E A0 00 00            cmp dword ptr [rip + 0xa02e05], 0
005C3F1B  74 0C                           je 0x1405c3f29
005C3F1D  44 0F 20 C1                     mov rcx, cr8
005C3F21  41 8A D6                        mov dl, r14b
005C3F24  E8 6F 17 F3 FF                  call 0x1404f5698
005C3F29  45 0F 22 C6                     mov cr8, r14
005C3F2D  48 8D 44 24 40                  lea rax, [rsp + 0x40]
005C3F32  4C 8B CE                        mov r9, rsi
005C3F35  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
005C3F3A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005C3F3F  48 8B D7                        mov rdx, rdi
005C3F42  E8 C9 39 C5 FF                  call 0x140217910
005C3F47  45 84 ED                        test r13b, r13b
005C3F4A  75 08                           jne 0x1405c3f54
005C3F4C  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
005C3F54  49 8B C4                        mov rax, r12
005C3F57  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
005C3F5B  48 33 CC                        xor rcx, rsp
005C3F5E  E8 DD 86 0E 00                  call 0x1406ac640
005C3F63  48 8B 9C 24 D0 01 00 00         mov rbx, qword ptr [rsp + 0x1d0]
005C3F6B  48 81 C4 80 01 00 00            add rsp, 0x180
005C3F72  41 5F                           pop r15
005C3F74  41 5E                           pop r14
005C3F76  41 5D                           pop r13
005C3F78  41 5C                           pop r12
005C3F7A  5F                              pop rdi
005C3F7B  5E                              pop rsi
005C3F7C  5D                              pop rbp
005C3F7D  C3                              ret
005C3F7E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAdjustUserIsolationDomainThread(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rsp;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m164;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int8 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (384);
    result = (*(unsigned __int64 *)(v_rip + 8678340)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m188 = a3;
    a2 = 0;
    result = memset(v_stack_m158, a2, 264, a4);
    a3 = 0;
    v_stack_m180 = 0;
    v_stack_m178 = v_xmm0;
    if (0 != 0) goto loc_005C3BED;
    v_r13 = 0;
    v_stack_m168 = 0;
loc_005C3BC0:
    if (condition_is_above_or_equal) goto loc_005C3BDE;
loc_005C3BC9:
    result = KeYieldProcessorEx(v_stack_m168, a2, a3, a4);
    if (*(unsigned __int64 *)(a1 + 64) != 0) goto loc_005C3BC9;
    goto loc_005C3BC0;
loc_005C3BDE:
    a3 = 0;
loc_005C3BED:
    if ((*(unsigned __int64 *)(a1 + 1816)) == v_stack_p10) goto loc_005C3F47;
    if (a1 != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_005C3C1E;
    *(unsigned __int64 *)(a1 + 1816) = v_stack_p10;
    goto loc_005C3F47;
loc_005C3C1E:
loc_005C3C2B:
loc_005C3C30:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 388)))) - (1));
    if (condition_is_equal) goto loc_005C3D15;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005C3C77;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005C3CC4;
    if (((unsigned int)(a1)) != 2) goto loc_005C3E86;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 112)) & (7));
    if (((unsigned __int8)(result)) == 1) goto loc_005C3E86;
    result = (unsigned __int8)((result) - (3));
    if (((unsigned __int8)(result)) <= 3) goto loc_005C3E86;
loc_005C3C77:
    if (sign_flag) goto loc_005C3C30;
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(v_rip + 10506267 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), a2, v_stack_m180, 1);
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10506267 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 8))) goto loc_005C3E86;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 2) goto loc_005C3E71;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_005C3E71;
loc_005C3CC4:
    if (sign_flag) goto loc_005C3C30;
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(v_rip + 10506267 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), a2, v_stack_m180, 1);
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10506267 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 16))) goto loc_005C3E86;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 3) goto loc_005C3E71;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_005C3E71;
loc_005C3D15:
    if (!sign_flag) goto loc_005C3E42;
    if (((*(unsigned int *)(v_rip + 10497538)) & (0x200000ULL)) == 0) goto loc_005C3D67;
    v_stack_m170 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10506267 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) * 8) + 36424);
    v_stack_m178 = v_stack_m180;
    if (v_stack_m178 == 0) goto loc_005C3DA0;
    result = KxWaitForLockOwnerShip(v_stack_m178, v_stack_m178, v_stack_m180, 1);
    goto loc_005C3D90;
loc_005C3D67:
    v_r13 = 0;
    v_stack_m164 = 0;
loc_005C3D6F:
    if (condition_is_above_or_equal) goto loc_005C3D8B;
loc_005C3D77:
    result = KeYieldProcessorEx(v_stack_m164, v_stack_m178, v_stack_m180, 1);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10506267 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) * 8) + 36424)) != 0) goto loc_005C3D77;
    goto loc_005C3D6F;
loc_005C3D8B:
loc_005C3D90:
    a3 = 0;
loc_005C3DA0:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 1) goto loc_005C3DBA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_005C3E83;
loc_005C3DBA:
    if (((*(unsigned int *)(v_rip + 10497396)) & (0x200000ULL)) == 0) goto loc_005C3E39;
    if (v_stack_m178 != 0) goto loc_005C3E08;
    if (v_stack_m178 == v_stack_m178) goto loc_005C3C30;
    result = KxWaitForLockChainValid(v_stack_m178, 2, a3, 1);
    a3 = 0;
loc_005C3E08:
    v_stack_m178 = 0;
    result = (unsigned __int8)((v_stack_m170) ^ ((unsigned __int8)(v_stack_m170)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_005C3C30;
    result = KeWakeAddressAll(result + 8, 2, a3, a3 + 1);
    goto loc_005C3E7B;
loc_005C3E39:
    goto loc_005C3C2B;
loc_005C3E42:
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(v_rip + 10505763 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), a2, v_stack_m180, a3 + 1);
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 1) goto loc_005C3E71;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_005C3E86;
loc_005C3E71:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m180, a2, v_stack_m180, 1);
loc_005C3E7B:
    a3 = 0;
    goto loc_005C3C1E;
loc_005C3E83:
loc_005C3E86:
    if (2 == 2) goto loc_005C3EA4;
    *(unsigned __int64 *)(a1 + 1816) = v_stack_p10;
    goto loc_005C3F2D;
loc_005C3EA4:
    a2 = 0;
    v_stack_m158 = 0x200001ULL;
    result = memset(v_stack_m150, a2, 256, 1);
    result = KeAddProcessorAffinityEx(v_stack_m158, (unsigned int)(*(unsigned int *)(0 + 36)), 256, 1);
    if ((*(unsigned int *)(v_rip + 10497600)) != 0) {
        result = KiRaiseIrqlProcessIrqlFlags(v_cr8, 12, 256, 1);
    }
    v_stack_m198 = v_stack_p10;
    a1 = 0;
    result = KiIpiSendPacket(a1, v_stack_m158, v_rip + 1485, a1);
    result = KiIpiStallOnPacketTargets(a1, v_stack_m158, v_rip + 1485, a1);
    if ((*(unsigned int *)(v_rip + 10497541)) != 0) {
        a1 = 12;
        a2 = 2;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_rip + 1485, a1);
    }
loc_005C3F2D:
    v_stack_m198 = v_stack_m178;
    result = KiReleaseThreadStateLock(a1, 0, v_stack_m180, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10506267 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) * 8) + 36424));
loc_005C3F47:
    if ((unsigned __int8)(v_stack_m188) == 0) {
        *(unsigned __int64 *)(a1 + 64) = 0;
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, 0, v_stack_m180, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10506267 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) * 8) + 36424));
    v_rsp = (v_rsp) + (384);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiAdjustUserIsolationDomainThread(void *Arg1, int64_t Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rsp;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m164;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint8_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m48;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (384);
    result = (*(uint64_t *)(v_rip + 0x846BC4)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m188 = Arg3;
    Arg2 = 0;
    result = memset(v_stack_m158, Arg2, 264, a4);
    Arg3 = 0;
    v_stack_m180 = 0;
    v_stack_m178 = v_xmm0;
    if (0 != 0) goto loc_005C3BED;
    local_r13 = 0;
    v_stack_m168 = 0;
loc_005C3BC0:
    if (condition_is_above_or_equal) goto loc_005C3BDE;
loc_005C3BC9:
    result = KeYieldProcessorEx(v_stack_m168, Arg2, Arg3, a4);
    if (*(uint64_t *)(arg1 + 0x40) != 0) goto loc_005C3BC9;
    goto loc_005C3BC0;
loc_005C3BDE:
    Arg3 = 0;
loc_005C3BED:
    if ((*(uint64_t *)(arg1 + 0x718)) == v_stack_p10) goto loc_005C3F47;
    if (Arg1 != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_005C3C1E;
    *(uint64_t *)(arg1 + 0x718) = v_stack_p10;
    goto loc_005C3F47;
loc_005C3C1E:
loc_005C3C2B:
loc_005C3C30:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x184)))) - (1));
    if (condition_is_equal) goto loc_005C3D15;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005C3C77;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005C3CC4;
    if (((uint32_t)(Arg1)) != 2) goto loc_005C3E86;
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x70)) & (7));
    if (((uint8_t)(result)) == 1) goto loc_005C3E86;
    result = (uint8_t)((result) - (3));
    if (((uint8_t)(result)) <= 3) goto loc_005C3E86;
loc_005C3C77:
    if (sign_flag) goto loc_005C3C30;
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(v_rip + 0xA0501B + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8), Arg2, v_stack_m180, 1);
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA0501B + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x8))) goto loc_005C3E86;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x184))) != 2) goto loc_005C3E71;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218))))) goto loc_005C3E71;
loc_005C3CC4:
    if (sign_flag) goto loc_005C3C30;
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(v_rip + 0xA0501B + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8), Arg2, v_stack_m180, 1);
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA0501B + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8) + 0x10))) goto loc_005C3E86;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x184))) != 3) goto loc_005C3E71;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218))))) goto loc_005C3E71;
loc_005C3D15:
    if (!sign_flag) goto loc_005C3E42;
    if (((*(uint32_t *)(v_rip + 0xA02E02)) & (0x200000ULL)) == 0) goto loc_005C3D67;
    v_stack_m170 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xA0501B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) * 8) + 0x8E48);
    v_stack_m178 = v_stack_m180;
    if (v_stack_m178 == 0) goto loc_005C3DA0;
    result = KxWaitForLockOwnerShip(v_stack_m178, v_stack_m178, v_stack_m180, 1);
    goto loc_005C3D90;
loc_005C3D67:
    local_r13 = 0;
    v_stack_m164 = 0;
loc_005C3D6F:
    if (condition_is_above_or_equal) goto loc_005C3D8B;
loc_005C3D77:
    result = KeYieldProcessorEx(v_stack_m164, v_stack_m178, v_stack_m180, 1);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xA0501B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) * 8) + 0x8E48)) != 0) goto loc_005C3D77;
    goto loc_005C3D6F;
loc_005C3D8B:
loc_005C3D90:
    Arg3 = 0;
loc_005C3DA0:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x184))) != 1) goto loc_005C3DBA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218))))) goto loc_005C3E83;
loc_005C3DBA:
    if (((*(uint32_t *)(v_rip + 0xA02D74)) & (0x200000ULL)) == 0) goto loc_005C3E39;
    if (v_stack_m178 != 0) goto loc_005C3E08;
    if (v_stack_m178 == v_stack_m178) goto loc_005C3C30;
    result = KxWaitForLockChainValid(v_stack_m178, 2, Arg3, 1);
    Arg3 = 0;
loc_005C3E08:
    v_stack_m178 = 0;
    result = (uint8_t)((v_stack_m170) ^ ((uint8_t)(v_stack_m170)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_005C3C30;
    result = KeWakeAddressAll(result + 8, 2, Arg3, Arg3 + 1);
    goto loc_005C3E7B;
loc_005C3E39:
    goto loc_005C3C2B;
loc_005C3E42:
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(v_rip + 0xA04E23 + (uint32_t)(*(uint32_t *)(arg1 + 0x218)) * 8), Arg2, v_stack_m180, Arg3 + 1);
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x184))) != 1) goto loc_005C3E71;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218))))) goto loc_005C3E86;
loc_005C3E71:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_m180, Arg2, v_stack_m180, 1);
loc_005C3E7B:
    Arg3 = 0;
    goto loc_005C3C1E;
loc_005C3E83:
loc_005C3E86:
    if (2 == 2) goto loc_005C3EA4;
    *(uint64_t *)(arg1 + 0x718) = v_stack_p10;
    goto loc_005C3F2D;
loc_005C3EA4:
    Arg2 = 0;
    v_stack_m158 = 0x200001ULL;
    result = memset(v_stack_m150, Arg2, 256, 1);
    result = KeAddProcessorAffinityEx(v_stack_m158, (uint32_t)(*(uint32_t *)(0 + 0x24)), 256, 1);
    if ((*(uint32_t *)(v_rip + 0xA02E40)) != 0) {
        result = KiRaiseIrqlProcessIrqlFlags(v_cr8, 12, 256, 1);
    }
    v_stack_m198 = v_stack_p10;
    Arg1 = 0;
    result = KiIpiSendPacket(Arg1, v_stack_m158, v_rip + 1485, Arg1);
    result = KiIpiStallOnPacketTargets(Arg1, v_stack_m158, v_rip + 1485, Arg1);
    if ((*(uint32_t *)(v_rip + 0xA02E05)) != 0) {
        Arg1 = 12;
        Arg2 = 2;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_rip + 1485, Arg1);
    }
loc_005C3F2D:
    v_stack_m198 = v_stack_m178;
    result = KiReleaseThreadStateLock(Arg1, 0, v_stack_m180, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA0501B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) * 8) + 0x8E48));
loc_005C3F47:
    if ((uint8_t)(v_stack_m188) == 0) {
        *(uint64_t *)(arg1 + 0x40) = 0;
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 0, v_stack_m180, *(uint64_t *)(*(uint64_t *)(v_rip + 0xA0501B + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x218)))) * 8) + 0x8E48));
    local_rsp = (local_rsp) + (384);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R/W` |
| `Arg1` | `+ 0x718` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005C3B54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
