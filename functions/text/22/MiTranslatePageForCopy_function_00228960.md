# MiTranslatePageForCopy

- RVA: `0x00228960`–`0x00228E9E` (길이 `1,342` bytes)
- VA: `0x0000000140228960`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005FC60`
- 디코드: `324`개 명령, `1,342/1,342` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x002289B7` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002289C7` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002289F7` → [MiInitializePageFaultPacket](MiInitializePageFaultPacket_function_00228EB0.md) (function, `0x00228EB0`)
- `0x00228A6E` → [MiVaIsUltra](MiVaIsUltra_function_002284F0.md) (function, `0x002284F0`)
- `0x00228A8B` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x00228A9E` → [MiSystemVaTypeToVm](../28/MiSystemVaTypeToVm_function_0028EB50.md) (function, `0x0028EB50`)
- `0x00228AC2` → [MiSynchronizeSystemVa](../28/MiSynchronizeSystemVa_function_0028ECB8.md) (function, `0x0028ECB8`)
- `0x00228BB7` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00228C03` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x00228C1E` → [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) (function, `0x00280D10`)
- `0x00228C95` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00228D40` → [MiUnlockSystemVa](../34/MiUnlockSystemVa_function_0034B800.md) (function, `0x0034B800`)
- `0x00228D54` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00228D60` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00228D71` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00228D7D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00228DB6` → [MiIsPrototypePteVadLookup](../32/MiIsPrototypePteVadLookup_function_00328B70.md) (function, `0x00328B70`)
- `0x00228DC7` → [MiLockProtoPoolPage](../2B/MiLockProtoPoolPage_function_002B8B80.md) (function, `0x002B8B80`)
- `0x00228DE7` → [MiGetAnyMultiplexedVm](../44/MiGetAnyMultiplexedVm_function_00448BD0.md) (function, `0x00448BD0`)
- `0x00228E3A` → [MiCheckVirtualAddress](../32/MiCheckVirtualAddress_function_0032E4F0.md) (function, `0x0032E4F0`)
- `0x00228E54` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x00228E64` → [MiLockLeafPage](../36/MiLockLeafPage_function_003658C0.md) (function, `0x003658C0`)
- `0x00228E6F` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)

### Direct callers
- [MmCopyMemory](MmCopyMemory_function_002285B0.md) at `0x0022877F`

### Static image references
- `0x00228979` → RVA `0x00E0A740` (`.data`; read)
- `0x00228A37` → RVA `0x00E2DCE0` (`.data`; read)
- `0x00228A7B` → RVA `0x00E2F380` (`.data`; read)
- `0x00228BD8` → RVA `0x00E2F390` (`.data`; read)
- `0x00228D0A` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00228D4A` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00228D93` → RVA `0x00E2DC80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x00228D89` → [sub_006D6E94](../6D/Unknown_function_006D6E94.md) (`tail-transfer`)
  - `0x00228E08` → [sub_006D6E94 + 0xE0](../6D/Unknown_function_006D6E94.md) (`tail-transfer`)
  - `0x00228E10` → [sub_006D6E94 + 0xE0](../6D/Unknown_function_006D6E94.md) (`tail-transfer`)
  - `0x00228E1F` → [sub_006D6E94 + 0xE0](../6D/Unknown_function_006D6E94.md) (`tail-transfer`)
  - `0x00228E47` → [sub_006D6E94 + 0x10C](../6D/Unknown_function_006D6E94.md) (`tail-transfer`)
  - `0x00228E5A` → [sub_006D6E94 + 0x10C](../6D/Unknown_function_006D6E94.md) (`tail-transfer`)
  - `0x00228E76` → [sub_006D6E94 + 0x15F](../6D/Unknown_function_006D6E94.md) (`tail-transfer`)
  - `0x00228E8F` → [sub_006D6E94 + 0x140](../6D/Unknown_function_006D6E94.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00228960  40 55                           push rbp
00228962  53                              push rbx
00228963  56                              push rsi
00228964  57                              push rdi
00228965  41 54                           push r12
00228967  41 55                           push r13
00228969  41 56                           push r14
0022896B  41 57                           push r15
0022896D  48 8D 6C 24 E8                  lea rbp, [rsp - 0x18]
00228972  48 81 EC 18 01 00 00            sub rsp, 0x118
00228979  48 8B 05 C0 1D BE 00            mov rax, qword ptr [rip + 0xbe1dc0]
00228980  48 33 C4                        xor rax, rsp
00228983  48 89 45 00                     mov qword ptr [rbp], rax
00228987  4C 8B A5 80 00 00 00            mov r12, qword ptr [rbp + 0x80]
0022898E  49 8B D9                        mov rbx, r9
00228991  48 83 64 24 50 00               and qword ptr [rsp + 0x50], 0
00228997  4D 8B F8                        mov r15, r8
0022899A  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
0022899F  4C 8B EA                        mov r13, rdx
002289A2  4C 8B F1                        mov r14, rcx
002289A5  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
002289AA  33 D2                           xor edx, edx
002289AC  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
002289B1  41 B8 98 00 00 00               mov r8d, 0x98
002289B7  E8 84 E2 49 00                  call 0x1406c6c40
002289BC  33 D2                           xor edx, edx
002289BE  41 B8 80 00 00 00               mov r8d, 0x80
002289C4  49 8B CD                        mov rcx, r13
002289C7  E8 74 E2 49 00                  call 0x1406c6c40
002289CC  48 8D 44 24 60                  lea rax, [rsp + 0x60]
002289D1  48 83 CF FF                     or rdi, 0xffffffffffffffff
002289D5  49 89 3F                        mov qword ptr [r15], rdi
002289D8  45 33 C9                        xor r9d, r9d
002289DB  48 83 23 00                     and qword ptr [rbx], 0
002289DF  45 33 C0                        xor r8d, r8d
002289E2  49 83 24 24 00                  and qword ptr [r12], 0
002289E7  49 8B D6                        mov rdx, r14
002289EA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002289EF  33 C9                           xor ecx, ecx
002289F1  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
002289F7  E8 B4 04 00 00                  call 0x140228eb0
002289FC  8D 5F 02                        lea ebx, [rdi + 2]
002289FF  4D 8B C6                        mov r8, r14
00228A02  49 C1 F8 2F                     sar r8, 0x2f
00228A06  4C 03 C3                        add r8, rbx
00228A09  4C 3B C3                        cmp r8, rbx
00228A0C  0F 87 BF 01 00 00               ja 0x140228bd1
00228A12  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00228A1C  4C 3B F0                        cmp r14, rax
00228A1F  0F 83 3F 02 00 00               jae 0x140228c64
00228A25  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00228A2F  48 8B C0                        mov rax, rax
00228A32  4C 3B F0                        cmp r14, rax
00228A35  72 25                           jb 0x140228a5c
00228A37  48 8B 05 A2 52 C0 00            mov rax, qword ptr [rip + 0xc052a2]
00228A3E  48 8D 0C 40                     lea rcx, [rax + rax*2]
00228A42  48 C1 E1 04                     shl rcx, 4
00228A46  48 B8 30 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000030
00228A50  48 03 C8                        add rcx, rax
00228A53  4C 3B F1                        cmp r14, rcx
00228A56  0F 82 75 01 00 00               jb 0x140228bd1
00228A5C  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00228A66  4C 3B F0                        cmp r14, rax
00228A69  72 10                           jb 0x140228a7b
00228A6B  49 8B CE                        mov rcx, r14
00228A6E  E8 7D FA FF FF                  call 0x1402284f0
00228A73  85 C0                           test eax, eax
00228A75  0F 85 56 01 00 00               jne 0x140228bd1
00228A7B  4C 3B 35 FE 68 C0 00            cmp r14, qword ptr [rip + 0xc068fe]
00228A82  0F 83 50 01 00 00               jae 0x140228bd8
00228A88  49 8B CE                        mov rcx, r14
00228A8B  E8 F0 61 06 00                  call 0x14028ec80
00228A90  44 8B D0                        mov r10d, eax
00228A93  83 F8 10                        cmp eax, 0x10
00228A96  0F 84 E0 01 00 00               je 0x140228c7c
00228A9C  8B C8                           mov ecx, eax
00228A9E  E8 AD 60 06 00                  call 0x14028eb50
00228AA3  48 85 C0                        test rax, rax
00228AA6  0F 84 36 03 00 00               je 0x140228de2
00228AAC  41 83 4D 04 04                  or dword ptr [r13 + 4], 4
00228AB1  45 33 C9                        xor r9d, r9d
00228AB4  45 8B C2                        mov r8d, r10d
00228AB7  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00228ABC  49 8B D6                        mov rdx, r14
00228ABF  48 8B C8                        mov rcx, rax
00228AC2  E8 F1 61 06 00                  call 0x14028ecb8
00228AC7  85 C0                           test eax, eax
00228AC9  0F 84 AD 01 00 00               je 0x140228c7c
00228ACF  41 0F 10 45 18                  movups xmm0, xmmword ptr [r13 + 0x18]
00228AD4  49 63 45 10                     movsxd rax, dword ptr [r13 + 0x10]
00228AD8  F2 41 0F 10 4D 28               movsd xmm1, qword ptr [r13 + 0x28]
00228ADE  F2 0F 11 4D A8                  movsd qword ptr [rbp - 0x58], xmm1
00228AE3  0F 11 45 98                     movups xmmword ptr [rbp - 0x68], xmm0
00228AE7  85 C0                           test eax, eax
00228AE9  0F 84 97 01 00 00               je 0x140228c86
00228AEF  48 8B 4C C4 78                  mov rcx, qword ptr [rsp + rax*8 + 0x78]
00228AF4  48 8B D3                        mov rdx, rbx
00228AF7  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00228B01  48 8B 39                        mov rdi, qword ptr [rcx]
00228B04  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00228B09  45 8B 45 10                     mov r8d, dword ptr [r13 + 0x10]
00228B0D  48 C1 EF 0C                     shr rdi, 0xc
00228B11  48 23 F8                        and rdi, rax
00228B14  48 C1 E9 0C                     shr rcx, 0xc
00228B18  45 85 C0                        test r8d, r8d
00228B1B  74 1C                           je 0x140228b39
00228B1D  48 8B C1                        mov rax, rcx
00228B20  48 C1 E9 09                     shr rcx, 9
00228B24  25 FF 01 00 00                  and eax, 0x1ff
00228B29  48 0F AF C2                     imul rax, rdx
00228B2D  48 C1 E2 09                     shl rdx, 9
00228B31  48 03 F8                        add rdi, rax
00228B34  44 2B C3                        sub r8d, ebx
00228B37  75 E4                           jne 0x140228b1d
00228B39  48 3B 3D A0 51 C0 00            cmp rdi, qword ptr [rip + 0xc051a0]
00228B40  0F 87 AB 02 00 00               ja 0x140228df1
00228B46  48 8D 34 7F                     lea rsi, [rdi + rdi*2]
00228B4A  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00228B54  48 C1 E6 04                     shl rsi, 4
00228B58  48 8B C0                        mov rax, rax
00228B5B  48 8B 04 06                     mov rax, qword ptr [rsi + rax]
00228B5F  48 C1 E8 36                     shr rax, 0x36
00228B63  85 C3                           test ebx, eax
00228B65  0F 84 86 02 00 00               je 0x140228df1
00228B6B  33 DB                           xor ebx, ebx
00228B6D  48 B8 18 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000018
00228B77  45 33 F6                        xor r14d, r14d
00228B7A  4C 8B F8                        mov r15, rax
00228B7D  F0 4A 0F BA 2C 3E 3F            lock bts qword ptr [rsi + r15], 0x3f
00228B84  0F 82 96 01 00 00               jb 0x140228d20
00228B8A  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
00228B8F  F2 0F 10 4D A8                  movsd xmm1, qword ptr [rbp - 0x58]
00228B94  0F 10 45 98                     movups xmm0, xmmword ptr [rbp - 0x68]
00228B98  41 0F 11 45 18                  movups xmmword ptr [r13 + 0x18], xmm0
00228B9D  F2 41 0F 11 4D 28               movsd qword ptr [r13 + 0x28], xmm1
00228BA3  85 DB                           test ebx, ebx
00228BA5  0F 88 92 01 00 00               js 0x140228d3d
00228BAB  49 89 3F                        mov qword ptr [r15], rdi
00228BAE  8B C3                           mov eax, ebx
00228BB0  48 8B 4D 00                     mov rcx, qword ptr [rbp]
00228BB4  48 33 CC                        xor rcx, rsp
00228BB7  E8 84 3A 48 00                  call 0x1406ac640
00228BBC  48 81 C4 18 01 00 00            add rsp, 0x118
00228BC3  41 5F                           pop r15
00228BC5  41 5E                           pop r14
00228BC7  41 5D                           pop r13
00228BC9  41 5C                           pop r12
00228BCB  5F                              pop rdi
00228BCC  5E                              pop rsi
00228BCD  5B                              pop rbx
00228BCE  5D                              pop rbp
00228BCF  C3                              ret
00228BD0  CC                              int3
00228BD1  B8 EF 00 00 C0                  mov eax, 0xc00000ef
00228BD6  EB D8                           jmp 0x140228bb0
00228BD8  4C 3B 35 B1 67 C0 00            cmp r14, qword ptr [rip + 0xc067b1]
00228BDF  0F 87 A3 FE FF FF               ja 0x140228a88
00228BE5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00228BEE  48 8B 98 B8 00 00 00            mov rbx, qword ptr [rax + 0xb8]
00228BF5  48 81 C3 00 04 00 00            add rbx, 0x400
00228BFC  48 8B CB                        mov rcx, rbx
00228BFF  48 89 5D 98                     mov qword ptr [rbp - 0x68], rbx
00228C03  E8 E8 3F 05 00                  call 0x14027cbf0
00228C08  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
00228C0D  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00228C12  49 8B D7                        mov rdx, r15
00228C15  88 45 A4                        mov byte ptr [rbp - 0x5c], al
00228C18  45 33 C9                        xor r9d, r9d
00228C1B  48 8B CB                        mov rcx, rbx
00228C1E  E8 ED 80 05 00                  call 0x140280d10
00228C23  49 8B CE                        mov rcx, r14
00228C26  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00228C2A  48 C1 E9 12                     shr rcx, 0x12
00228C2E  81 E1 F8 FF FF 3F               and ecx, 0x3ffffff8
00228C34  48 BA 00 00 00 40 FB F6 FF FF   movabs rdx, 0xfffff6fb40000000
00228C3E  48 03 CA                        add rcx, rdx
00228C41  48 3B C1                        cmp rax, rcx
00228C44  74 45                           je 0x140228c8b
00228C46  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00228C4B  48 8B 08                        mov rcx, qword ptr [rax]
00228C4E  48 F7 D9                        neg rcx
00228C51  1B DB                           sbb ebx, ebx
00228C53  81 E3 D3 00 00 00               and ebx, 0xd3
00228C59  81 C3 05 00 00 C0               add ebx, 0xc0000005
00228C5F  E9 26 FF FF FF                  jmp 0x140228b8a
00228C64  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
00228C6E  4C 3B F0                        cmp r14, rax
00228C71  0F 87 AE FD FF FF               ja 0x140228a25
00228C77  E9 55 FF FF FF                  jmp 0x140228bd1
00228C7C  B8 A0 00 00 C0                  mov eax, 0xc00000a0
00228C81  E9 2A FF FF FF                  jmp 0x140228bb0
00228C86  4C 8B 7C 24 78                  mov r15, qword ptr [rsp + 0x78]
00228C8B  C6 44 24 30 11                  mov byte ptr [rsp + 0x30], 0x11
00228C90  33 DB                           xor ebx, ebx
00228C92  49 8B CF                        mov rcx, r15
00228C95  E8 06 9C 05 00                  call 0x1402828a0
00228C9A  A8 01                           test al, 1
00228C9C  0F 84 E2 00 00 00               je 0x140228d84
00228CA2  48 8B F8                        mov rdi, rax
00228CA5  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00228CAF  48 C1 EF 0C                     shr rdi, 0xc
00228CB3  48 23 F8                        and rdi, rax
00228CB6  48 3B 3D 23 50 C0 00            cmp rdi, qword ptr [rip + 0xc05023]
00228CBD  0F 87 D1 01 00 00               ja 0x140228e94
00228CC3  48 8D 34 7F                     lea rsi, [rdi + rdi*2]
00228CC7  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
00228CD1  48 C1 E6 04                     shl rsi, 4
00228CD5  48 8B C0                        mov rax, rax
00228CD8  48 8B 04 06                     mov rax, qword ptr [rsi + rax]
00228CDC  48 C1 E8 36                     shr rax, 0x36
00228CE0  0F BA E0 00                     bt eax, 0
00228CE4  0F 83 AA 01 00 00               jae 0x140228e94
00228CEA  45 33 F6                        xor r14d, r14d
00228CED  48 B8 18 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000018
00228CF7  4C 8B F8                        mov r15, rax
00228CFA  F0 4A 0F BA 2C 3E 3F            lock bts qword ptr [rsi + r15], 0x3f
00228D01  0F 83 83 FE FF FF               jae 0x140228b8a
00228D07  41 FF C6                        inc r14d
00228D0A  44 85 35 9B C5 D9 00            test dword ptr [rip + 0xd9c59b], r14d
00228D11  74 54                           je 0x140228d67
00228D13  F3 90                           pause
00228D15  4A 8B 04 3E                     mov rax, qword ptr [rsi + r15]
00228D19  48 85 C0                        test rax, rax
00228D1C  79 DC                           jns 0x140228cfa
00228D1E  EB E7                           jmp 0x140228d07
00228D20  41 FF C6                        inc r14d
00228D23  44 85 35 82 C5 D9 00            test dword ptr [rip + 0xd9c582], r14d
00228D2A  74 1E                           je 0x140228d4a
00228D2C  F3 90                           pause
00228D2E  4A 8B 04 3E                     mov rax, qword ptr [rsi + r15]
00228D32  48 85 C0                        test rax, rax
00228D35  0F 89 42 FE FF FF               jns 0x140228b7d
00228D3B  EB E3                           jmp 0x140228d20
00228D3D  49 8B CD                        mov rcx, r13
00228D40  E8 BB 2A 12 00                  call 0x14034b800
00228D45  E9 64 FE FF FF                  jmp 0x140228bae
00228D4A  8B 05 68 DD D9 00               mov eax, dword ptr [rip + 0xd9dd68]
00228D50  A8 40                           test al, 0x40
00228D52  74 D8                           je 0x140228d2c
00228D54  E8 37 67 0E 00                  call 0x14030f490
00228D59  84 C0                           test al, al
00228D5B  74 CF                           je 0x140228d2c
00228D5D  41 8B CE                        mov ecx, r14d
00228D60  E8 FB 66 0E 00                  call 0x14030f460
00228D65  EB C7                           jmp 0x140228d2e
00228D67  8B 05 4B DD D9 00               mov eax, dword ptr [rip + 0xd9dd4b]
00228D6D  A8 40                           test al, 0x40
00228D6F  74 A2                           je 0x140228d13
00228D71  E8 1A 67 0E 00                  call 0x14030f490
00228D76  84 C0                           test al, al
00228D78  74 99                           je 0x140228d13
00228D7A  41 8B CE                        mov ecx, r14d
00228D7D  E8 DE 66 0E 00                  call 0x14030f460
00228D82  EB 91                           jmp 0x140228d15
00228D84  48 0F BA E0 0A                  bt rax, 0xa
00228D89  0F 83 05 E1 4A 00               jae 0x1406d6e94
00228D8F  A8 02                           test al, 2
00228D91  75 68                           jne 0x140228dfb
00228D93  48 8B 0D E6 4E C0 00            mov rcx, qword ptr [rip + 0xc04ee6]
00228D9A  48 8B F0                        mov rsi, rax
00228D9D  48 85 C9                        test rcx, rcx
00228DA0  74 0D                           je 0x140228daf
00228DA2  A8 10                           test al, 0x10
00228DA4  75 09                           jne 0x140228daf
00228DA6  48 8B F1                        mov rsi, rcx
00228DA9  48 F7 D6                        not rsi
00228DAC  48 23 F0                        and rsi, rax
00228DAF  48 8B C8                        mov rcx, rax
00228DB2  48 C1 FE 10                     sar rsi, 0x10
00228DB6  E8 B5 FD 0F 00                  call 0x140328b70
00228DBB  85 C0                           test eax, eax
00228DBD  75 65                           jne 0x140228e24
00228DBF  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00228DC4  48 8B CE                        mov rcx, rsi
00228DC7  E8 B4 FD 08 00                  call 0x1402b8b80
00228DCC  4C 8B F0                        mov r14, rax
00228DCF  48 85 C0                        test rax, rax
00228DD2  0F 85 87 00 00 00               jne 0x140228e5f
00228DD8  BB D8 00 00 C0                  mov ebx, 0xc00000d8
00228DDD  E9 A8 FD FF FF                  jmp 0x140228b8a
00228DE2  B9 06 00 00 00                  mov ecx, 6
00228DE7  E8 E4 FD 21 00                  call 0x140448bd0
00228DEC  E9 BB FC FF FF                  jmp 0x140228aac
00228DF1  BB 41 01 00 C0                  mov ebx, 0xc0000141
00228DF6  E9 94 FD FF FF                  jmp 0x140228b8f
00228DFB  48 8B 15 7E 4E C0 00            mov rdx, qword ptr [rip + 0xc04e7e]
00228E02  48 8B C8                        mov rcx, rax
00228E05  48 85 D2                        test rdx, rdx
00228E08  0F 84 66 E1 4A 00               je 0x1406d6f74
00228E0E  A8 10                           test al, 0x10
00228E10  0F 85 5E E1 4A 00               jne 0x1406d6f74
00228E16  48 8B CA                        mov rcx, rdx
00228E19  48 F7 D1                        not rcx
00228E1C  48 23 C8                        and rcx, rax
00228E1F  E9 50 E1 4A 00                  jmp 0x1406d6f74
00228E24  48 21 5C 24 58                  and qword ptr [rsp + 0x58], rbx
00228E29  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00228E2E  21 5C 24 40                     and dword ptr [rsp + 0x40], ebx
00228E32  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00228E37  49 8B CE                        mov rcx, r14
00228E3A  E8 B1 56 10 00                  call 0x14032e4f0
00228E3F  48 8B F0                        mov rsi, rax
00228E42  48 39 5C 24 58                  cmp qword ptr [rsp + 0x58], rbx
00228E47  0F 84 53 E1 4A 00               je 0x1406d6fa0
00228E4D  B2 11                           mov dl, 0x11
00228E4F  B9 01 00 00 00                  mov ecx, 1
00228E54  E8 C7 E1 06 00                  call 0x140297020
00228E59  90                              nop
00228E5A  E9 41 E1 4A 00                  jmp 0x1406d6fa0
00228E5F  33 D2                           xor edx, edx
00228E61  48 8B CE                        mov rcx, rsi
00228E64  E8 57 CA 13 00                  call 0x1403658c0
00228E69  48 8B CE                        mov rcx, rsi
00228E6C  4C 8B F8                        mov r15, rax
00228E6F  E8 2C 9A 05 00                  call 0x1402828a0
00228E74  A8 01                           test al, 1
00228E76  0F 84 77 E1 4A 00               je 0x1406d6ff3
00228E7C  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00228E86  48 8B C8                        mov rcx, rax
00228E89  49 8B FF                        mov rdi, r15
00228E8C  48 2B F9                        sub rdi, rcx
00228E8F  E9 40 E1 4A 00                  jmp 0x1406d6fd4
00228E94  BB 41 01 00 C0                  mov ebx, 0xc0000141
00228E99  E9 EC FC FF FF                  jmp 0x140228b8a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiTranslatePageForCopy(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mB0;
    unsigned __int8 v_stack_mB4;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mF8;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (280);
    result = (*(unsigned __int64 *)(v_rip + 12459456)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m110 = a3;
    v_stack_m120 = a4;
    a2 = 0;
    result = memset(v_stack_mF8, a2, 152, a4);
    a2 = 0;
    result = memset(0, a2, 128, a4);
    v_rdi = (v_rdi) | (-1);
    *(unsigned __int64 *)(a3) = v_rdi;
    a4 = 0;
    a3 = 0;
    v_stack_m130 = v_stack_mF8;
    a1 = 0;
    result = MiInitializePageFaultPacket(a1, a1, a3, a4);
    a3 = (0) >> (47);
    a3 = (a3) + (v_rdi + 2);
    if (a3 > (v_rdi + 2)) goto loc_00228BD1;
    if (0 >= result) goto loc_00228C64;
loc_00228A25:
    if (0 < result) goto loc_00228A5C;
    a1 = (*(unsigned __int64 *)(v_rip + 12604066) + *(unsigned __int64 *)(v_rip + 12604066) * 2) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 12604066));
    if (a1 < a1) goto loc_00228BD1;
loc_00228A5C:
    if (a1 < (*(unsigned __int64 *)(v_rip + 12604066))) goto loc_00228A7B;
    result = MiVaIsUltra(a1, a1, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00228BD1;
loc_00228A7B:
    if (a1 >= (*(unsigned __int64 *)(v_rip + 12609790))) goto loc_00228BD8;
loc_00228A88:
    result = MiGetSystemRegionType(a1, a1, a3, a4);
    if (((unsigned int)(result)) == 16) goto loc_00228C7C;
    result = MiSystemVaTypeToVm((unsigned int)((unsigned int)(result)), a1, a3, a4);
    if (result == 0) goto loc_00228DE2;
loc_00228AAC:
    a4 = 0;
    v_stack_m138 = 0;
    result = MiSynchronizeSystemVa(result, a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    if ((unsigned int)(result) == 0) goto loc_00228C7C;
    v_stack_mB0 = v_xmm1;
    v_stack_mC0 = v_xmm0;
    if ((unsigned int)((int)(*(unsigned int *)(a2 + 16))) == 0) goto loc_00228C86;
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (int)(*(unsigned int *)(a2 + 16)) * 8 + 120))) >> (12);
    v_rdi = (v_rdi) & ((int)(*(unsigned int *)(a2 + 16)));
    a1 = (v_stack_mF8) >> (12);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16))) == 0) goto loc_00228B39;
loc_00228B1D:
    a1 = (a1) >> (9);
    result = (unsigned int)((a1) & (511));
    result = (result) * (v_rdi + 2);
    a2 = (v_rdi + 2) << (9);
    v_rdi = (v_rdi) + (result);
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) - ((unsigned int)(v_rdi + 2)));
    if (condition_is_not_equal) goto loc_00228B1D;
loc_00228B39:
    if (v_rdi > (*(unsigned __int64 *)(v_rip + 12603808))) goto loc_00228DF1;
    v_rsi = (v_rdi + v_rdi * 2) << (4);
    result = (*(unsigned __int64 *)(v_rsi + result * 1)) >> (54);
    if ((((unsigned int)(v_rdi + 2)) & ((unsigned int)(result))) == 0) goto loc_00228DF1;
    v_rbx = 0;
    v_r14 = 0;
loc_00228B7D:
    if (condition_is_below) goto loc_00228D20;
loc_00228B8A:
loc_00228B8F:
    *(unsigned __int64 *)(a2 + 24) = v_xmm0;
    *(unsigned __int64 *)(a2 + 40) = v_xmm1;
    if (sign_flag) goto loc_00228D3D;
    *(unsigned __int64 *)(v_stack_m110) = v_rdi;
loc_00228BAE:
loc_00228BB0:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (280);
    return result;
loc_00228BD1:
    goto loc_00228BB0;
loc_00228BD8:
    if (0 > (*(unsigned __int64 *)(v_rip + 12609457))) goto loc_00228A88;
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    v_stack_mC0 = v_rbx;
    result = MiLockWorkingSetShared(v_rbx, a2, a3, a4);
    v_stack_mB4 = (unsigned __int8)(result);
    a4 = 0;
    result = MiLockLowestValidPageTableEx(v_rbx, v_stack_p78, v_stack_p50, a4);
    v_stack_mB0 = result;
    a1 = (0) >> (18);
    a1 = (unsigned int)((a1) & (0x3FFFFFF8ULL));
    a1 = (a1) + (v_stack_p78);
    if (result == a1) goto loc_00228C8B;
    a1 = -(*(unsigned __int64 *)(v_stack_p50));
    v_rbx = (unsigned int)((v_rbx) & (211));
    v_rbx = (unsigned int)((v_rbx) + (0xC0000005ULL));
    goto loc_00228B8A;
loc_00228C64:
    if (0 > v_stack_p50) goto loc_00228A25;
    goto loc_00228BD1;
loc_00228C7C:
    goto loc_00228BB0;
loc_00228C86:
loc_00228C8B:
    v_stack_p30 = 17;
    v_rbx = 0;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p78, v_stack_p78, v_stack_p50, a4);
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00228D84;
    v_rdi = (result) >> (12);
    v_rdi = (v_rdi) & (result);
    if (v_rdi > (*(unsigned __int64 *)(v_rip + 12603427))) goto loc_00228E94;
    v_rsi = (v_rdi + v_rdi * 2) << (4);
    result = (*(unsigned __int64 *)(v_rsi + result * 1)) >> (54);
    if (condition_is_above_or_equal) goto loc_00228E94;
    v_r14 = 0;
loc_00228CFA:
    if (condition_is_above_or_equal) goto loc_00228B8A;
loc_00228D07:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 14271899)) & ((unsigned int)(v_r14))) == 0) goto loc_00228D67;
loc_00228D13:
loc_00228D15:
    if (!sign_flag) goto loc_00228CFA;
    goto loc_00228D07;
loc_00228D20:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 14271874)) & ((unsigned int)(v_r14))) == 0) goto loc_00228D4A;
loc_00228D2C:
loc_00228D2E:
    if (!sign_flag) goto loc_00228B7D;
    goto loc_00228D20;
loc_00228D3D:
    result = MiUnlockSystemVa(a2, v_stack_p78, v_stack_p50, a4);
    goto loc_00228BAE;
loc_00228D4A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14277992)))) & (64)) == 0) goto loc_00228D2C;
    result = KiCheckVpBackingLongSpinWaitHypercall(a2, v_stack_p78, v_stack_p50, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00228D2C;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), v_stack_p78, v_stack_p50, a4);
    goto loc_00228D2E;
loc_00228D67:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14277963)))) & (64)) == 0) goto loc_00228D13;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r14)), v_stack_p78, v_stack_p50, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00228D13;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), v_stack_p78, v_stack_p50, a4);
    goto loc_00228D15;
loc_00228D84:
    if ((((unsigned __int8)(result)) & (2)) != 0) goto loc_00228DFB;
    if (*(unsigned __int64 *)(v_rip + 12603110) == 0) goto loc_00228DAF;
    v_rsi = result;
    if ((((unsigned __int8)(result)) & (16)) == 0) {
        v_rsi = *(unsigned __int64 *)(v_rip + 12603110);
        v_rsi = ~(v_rsi);
        v_rsi = (v_rsi) & (result);
    }
    v_rsi = (v_rsi) >> (16);
    result = MiIsPrototypePteVadLookup(result, v_stack_p78, v_stack_p50, a4);
    if ((unsigned int)(result) != 0) goto loc_00228E24;
    result = MiLockProtoPoolPage(v_rsi, v_stack_p30, v_stack_p50, a4);
    if (result != 0) goto loc_00228E5F;
    goto loc_00228B8A;
loc_00228DE2:
    result = MiGetAnyMultiplexedVm(6, v_stack_p30, v_stack_p50, a4);
    goto loc_00228AAC;
loc_00228DF1:
    goto loc_00228B8F;
loc_00228DFB:
    a1 = ~(*(unsigned __int64 *)(v_rip + 12603006));
    a1 = (a1) & (result);
loc_00228E24:
    result = MiCheckVirtualAddress(result, v_stack_p40, v_stack_p58, a4);
    result = MiUnlockVadTree(1, 17, v_stack_p58, a4);
loc_00228E5F:
    a2 = 0;
    result = MiLockLeafPage(result, a2, v_stack_p58, a4);
    result = MI_READ_PTE_LOCK_FREE(result, a2, v_stack_p58, a4);
    v_rdi = (result) - (result);
loc_00228E94:
    goto loc_00228B8A;
}
```

## 5. (Beta) C Style

```c
int64_t MiTranslatePageForCopy(int64_t Arg1, void *Arg2, void *Arg3, void *Arg4, void *Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m120;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m58;
    uint64_t v_stack_mB0;
    uint8_t v_stack_mB4;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mF8;
    uint8_t v_stack_p30;
    uint32_t v_stack_p40;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (280);
    result = (*(uint64_t *)(v_rip + 0xBE1DC0)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m110 = Arg3;
    v_stack_m120 = Arg4;
    Arg2 = 0;
    result = memset(v_stack_mF8, Arg2, 152, Arg4);
    Arg2 = 0;
    result = memset(0, Arg2, 128, Arg4);
    local_rdi = (local_rdi) | (-1);
    *(uint64_t *)(arg3) = local_rdi;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_m130 = v_stack_mF8;
    Arg1 = 0;
    result = MiInitializePageFaultPacket(Arg1, Arg1, Arg3, Arg4);
    Arg3 = (0) >> (47);
    Arg3 = (Arg3) + (local_rdi + 2);
    if (Arg3 > (local_rdi + 2)) goto loc_00228BD1;
    if (0 >= result) goto loc_00228C64;
loc_00228A25:
    if (0 < result) goto loc_00228A5C;
    Arg1 = (*(uint64_t *)(v_rip + 0xC052A2) + *(uint64_t *)(v_rip + 0xC052A2) * 2) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xC052A2));
    if (Arg1 < Arg1) goto loc_00228BD1;
loc_00228A5C:
    if (Arg1 < (*(uint64_t *)(v_rip + 0xC052A2))) goto loc_00228A7B;
    result = MiVaIsUltra(Arg1, Arg1, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00228BD1;
loc_00228A7B:
    if (Arg1 >= (*(uint64_t *)(v_rip + 0xC068FE))) goto loc_00228BD8;
loc_00228A88:
    result = MiGetSystemRegionType(Arg1, Arg1, Arg3, Arg4);
    if (((uint32_t)(result)) == 16) goto loc_00228C7C;
    result = MiSystemVaTypeToVm((uint32_t)((uint32_t)(result)), Arg1, Arg3, Arg4);
    if (result == 0) goto loc_00228DE2;
loc_00228AAC:
    Arg4 = 0;
    v_stack_m138 = 0;
    result = MiSynchronizeSystemVa(result, Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00228C7C;
    v_stack_mB0 = v_xmm1;
    v_stack_mC0 = v_xmm0;
    if ((uint32_t)((int32_t)(*(uint32_t *)(arg2 + 0x10))) == 0) goto loc_00228C86;
    local_rdi = (*(uint64_t *)(*(uint64_t *)(local_rsp + (int32_t)(*(uint32_t *)(arg2 + 0x10)) * 8 + 0x78))) >> (12);
    local_rdi = (local_rdi) & ((int32_t)(*(uint32_t *)(arg2 + 0x10)));
    Arg1 = (v_stack_mF8) >> (12);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))) == 0) goto loc_00228B39;
loc_00228B1D:
    Arg1 = (Arg1) >> (9);
    result = (uint32_t)((Arg1) & (511));
    result = (result) * (local_rdi + 2);
    Arg2 = (local_rdi + 2) << (9);
    local_rdi = (local_rdi) + (result);
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10))) - ((uint32_t)(local_rdi + 2)));
    if (condition_is_not_equal) goto loc_00228B1D;
loc_00228B39:
    if (local_rdi > (*(uint64_t *)(v_rip + 0xC051A0))) goto loc_00228DF1;
    local_rsi = (local_rdi + local_rdi * 2) << (4);
    result = (*(uint64_t *)(local_rsi + result * 1)) >> (54);
    if ((((uint32_t)(local_rdi + 2)) & ((uint32_t)(result))) == 0) goto loc_00228DF1;
    local_rbx = 0;
    local_r14 = 0;
loc_00228B7D:
    if (condition_is_below) goto loc_00228D20;
loc_00228B8A:
loc_00228B8F:
    *(uint64_t *)(arg2 + 0x18) = v_xmm0;
    *(uint64_t *)(arg2 + 0x28) = v_xmm1;
    if (sign_flag) goto loc_00228D3D;
    *(uint64_t *)(v_stack_m110) = local_rdi;
loc_00228BAE:
loc_00228BB0:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (280);
    return result;
loc_00228BD1:
    goto loc_00228BB0;
loc_00228BD8:
    if (0 > (*(uint64_t *)(v_rip + 0xC067B1))) goto loc_00228A88;
    local_rbx = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    v_stack_mC0 = local_rbx;
    result = MiLockWorkingSetShared(local_rbx, Arg2, Arg3, Arg4);
    v_stack_mB4 = (uint8_t)(result);
    Arg4 = 0;
    result = MiLockLowestValidPageTableEx(local_rbx, v_stack_p78, v_stack_p50, Arg4);
    v_stack_mB0 = result;
    Arg1 = (0) >> (18);
    Arg1 = (uint32_t)((Arg1) & (0x3FFFFFF8ULL));
    Arg1 = (Arg1) + (v_stack_p78);
    if (result == Arg1) goto loc_00228C8B;
    Arg1 = -(*(uint64_t *)(v_stack_p50));
    local_rbx = (uint32_t)((local_rbx) & (211));
    local_rbx = (uint32_t)((local_rbx) + (0xC0000005ULL));
    goto loc_00228B8A;
loc_00228C64:
    if (0 > v_stack_p50) goto loc_00228A25;
    goto loc_00228BD1;
loc_00228C7C:
    goto loc_00228BB0;
loc_00228C86:
loc_00228C8B:
    v_stack_p30 = 17;
    local_rbx = 0;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p78, v_stack_p78, v_stack_p50, Arg4);
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00228D84;
    local_rdi = (result) >> (12);
    local_rdi = (local_rdi) & (result);
    if (local_rdi > (*(uint64_t *)(v_rip + 0xC05023))) goto loc_00228E94;
    local_rsi = (local_rdi + local_rdi * 2) << (4);
    result = (*(uint64_t *)(local_rsi + result * 1)) >> (54);
    if (condition_is_above_or_equal) goto loc_00228E94;
    local_r14 = 0;
loc_00228CFA:
    if (condition_is_above_or_equal) goto loc_00228B8A;
loc_00228D07:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xD9C59B)) & ((uint32_t)(local_r14))) == 0) goto loc_00228D67;
loc_00228D13:
loc_00228D15:
    if (!sign_flag) goto loc_00228CFA;
    goto loc_00228D07;
loc_00228D20:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xD9C582)) & ((uint32_t)(local_r14))) == 0) goto loc_00228D4A;
loc_00228D2C:
loc_00228D2E:
    if (!sign_flag) goto loc_00228B7D;
    goto loc_00228D20;
loc_00228D3D:
    result = MiUnlockSystemVa(Arg2, v_stack_p78, v_stack_p50, Arg4);
    goto loc_00228BAE;
loc_00228D4A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9DD68)))) & (64)) == 0) goto loc_00228D2C;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg2, v_stack_p78, v_stack_p50, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00228D2C;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), v_stack_p78, v_stack_p50, Arg4);
    goto loc_00228D2E;
loc_00228D67:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9DD4B)))) & (64)) == 0) goto loc_00228D13;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r14)), v_stack_p78, v_stack_p50, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00228D13;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), v_stack_p78, v_stack_p50, Arg4);
    goto loc_00228D15;
loc_00228D84:
    if ((((uint8_t)(result)) & (2)) != 0) goto loc_00228DFB;
    if (*(uint64_t *)(v_rip + 0xC04EE6) == 0) goto loc_00228DAF;
    local_rsi = result;
    if ((((uint8_t)(result)) & (16)) == 0) {
        local_rsi = *(uint64_t *)(v_rip + 0xC04EE6);
        local_rsi = ~(local_rsi);
        local_rsi = (local_rsi) & (result);
    }
    local_rsi = (local_rsi) >> (16);
    result = MiIsPrototypePteVadLookup(result, v_stack_p78, v_stack_p50, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00228E24;
    result = MiLockProtoPoolPage(local_rsi, v_stack_p30, v_stack_p50, Arg4);
    if (result != 0) goto loc_00228E5F;
    goto loc_00228B8A;
loc_00228DE2:
    result = MiGetAnyMultiplexedVm(6, v_stack_p30, v_stack_p50, Arg4);
    goto loc_00228AAC;
loc_00228DF1:
    goto loc_00228B8F;
loc_00228DFB:
    Arg1 = ~(*(uint64_t *)(v_rip + 0xC04E7E));
    Arg1 = (Arg1) & (result);
loc_00228E24:
    result = MiCheckVirtualAddress(result, v_stack_p40, v_stack_p58, Arg4);
    result = MiUnlockVadTree(1, 17, v_stack_p58, Arg4);
loc_00228E5F:
    Arg2 = 0;
    result = MiLockLeafPage(result, Arg2, v_stack_p58, Arg4);
    result = MI_READ_PTE_LOCK_FREE(result, Arg2, v_stack_p58, Arg4);
    local_rdi = (result) - (result);
loc_00228E94:
    goto loc_00228B8A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x4` | `32` | `R/W` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x18` | `128` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `W` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x0` | `64` | `R/W` |
| `Arg5` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00228960&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
