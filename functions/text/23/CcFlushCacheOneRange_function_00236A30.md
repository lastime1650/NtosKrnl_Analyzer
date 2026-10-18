# CcFlushCacheOneRange

- RVA: `0x00236A30`–`0x00236F18` (길이 `1,256` bytes)
- VA: `0x0000000140236A30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060918`
- 디코드: `293`개 명령, `1,256/1,256` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00236AFF` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00236B23` → [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00236BB7` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00236BD6` → [MmSetAddressRangeModifiedEx](MmSetAddressRangeModifiedEx_function_00236F20.md) (function, `0x00236F20`)
- `0x00236C45` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x00236C9B` → [CcReferenceSharedCacheMapFileObject](CcReferenceSharedCacheMapFileObject_function_002379BC.md) (function, `0x002379BC`)
- `0x00236CB9` → [ObFastDereferenceObjectDeferDelete](ObFastDereferenceObjectDeferDelete_function_002378C0.md) (function, `0x002378C0`)
- `0x00236D26` → [EtwTraceKernelEvent](EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x00236D63` → [MmFlushSection](MmFlushSection_function_002375E4.md) (function, `0x002375E4`)
- `0x00236D7F` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00236E53` → [ExfReleasePushLock](../26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00236E6E` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x00236E97` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00236EE1` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [CcWriteBehindAsync](../35/CcWriteBehindAsync_function_003549E8.md) at `0x00354AC1`
- [CcWriteBehindInternal](../35/CcWriteBehindInternal_function_00357540.md) at `0x00357630`
- [CcFlushCachePriv](../35/CcFlushCachePriv_function_0035B040.md) at `0x0035B172`
- [CcWriteBehindAsyncFlushOneRange](../57/CcWriteBehindAsyncFlushOneRange_function_0057FAEC.md) at `0x0057FB3A`

### Static image references
- `0x00236A4F` → RVA `0x00E0A740` (`.data`; read)
- `0x00236C76` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x00236E7A` → RVA `0x00E65B88` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00236A30  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00236A35  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00236A3A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00236A3F  57                              push rdi
00236A40  41 54                           push r12
00236A42  41 55                           push r13
00236A44  41 56                           push r14
00236A46  41 57                           push r15
00236A48  48 81 EC C0 00 00 00            sub rsp, 0xc0
00236A4F  48 8B 05 EA 3C BD 00            mov rax, qword ptr [rip + 0xbd3cea]
00236A56  48 33 C4                        xor rax, rsp
00236A59  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
00236A61  4C 8B 69 10                     mov r13, qword ptr [rcx + 0x10]
00236A65  33 C0                           xor eax, eax
00236A67  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00236A6C  33 F6                           xor esi, esi
00236A6E  0F 57 C0                        xorps xmm0, xmm0
00236A71  48 8B 01                        mov rax, qword ptr [rcx]
00236A74  48 8B D9                        mov rbx, rcx
00236A77  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00236A7C  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00236A80  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00236A88  0F B6 81 84 00 00 00            movzx eax, byte ptr [rcx + 0x84]
00236A8F  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00236A93  0F B6 81 85 00 00 00            movzx eax, byte ptr [rcx + 0x85]
00236A9A  88 44 24 31                     mov byte ptr [rsp + 0x31], al
00236A9E  48 8B 41 48                     mov rax, qword ptr [rcx + 0x48]
00236AA2  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00236AA7  48 8B 41 70                     mov rax, qword ptr [rcx + 0x70]
00236AAB  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00236AB0  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00236AB4  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00236AB9  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00236ABE  40 38 B1 C8 00 00 00            cmp byte ptr [rcx + 0xc8], sil
00236AC5  0F 85 43 03 00 00               jne 0x140236e0e
00236ACB  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
00236ACE  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00236AD2  89 71 3C                        mov dword ptr [rcx + 0x3c], esi
00236AD5  8B 6B 30                        mov ebp, dword ptr [rbx + 0x30]
00236AD8  49 8D 4D 68                     lea rcx, [r13 + 0x68]
00236ADC  48 2B E8                        sub rbp, rax
00236ADF  41 BC 00 00 04 00               mov r12d, 0x40000
00236AE5  48 03 6B 28                     add rbp, qword ptr [rbx + 0x28]
00236AE9  45 33 C0                        xor r8d, r8d
00236AEC  8B C5                           mov eax, ebp
00236AEE  33 D2                           xor edx, edx
00236AF0  25 FF FF 03 00                  and eax, 0x3ffff
00236AF5  4C 8B F6                        mov r14, rsi
00236AF8  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00236AFC  44 2B E0                        sub r12d, eax
00236AFF  E8 2C 97 FD FF                  call 0x140210230
00236B04  48 8B F8                        mov rdi, rax
00236B07  B9 11 00 00 00                  mov ecx, 0x11
00236B0C  33 C0                           xor eax, eax
00236B0E  F0 49 0F B1 4D 68               lock cmpxchg qword ptr [r13 + 0x68], rcx
00236B14  74 12                           je 0x140236b28
00236B16  4D 8D 4D 68                     lea r9, [r13 + 0x68]
00236B1A  4C 8B C7                        mov r8, rdi
00236B1D  33 D2                           xor edx, edx
00236B1F  49 8D 4D 68                     lea rcx, [r13 + 0x68]
00236B23  E8 24 99 FD FF                  call 0x14021044c
00236B28  48 85 FF                        test rdi, rdi
00236B2B  74 04                           je 0x140236b31
00236B2D  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
00236B31  4D 8B 4D 20                     mov r9, qword ptr [r13 + 0x20]
00236B35  49 8B 7D 58                     mov rdi, qword ptr [r13 + 0x58]
00236B39  49 81 F9 00 00 00 02            cmp r9, 0x2000000
00236B40  0F 8F 60 02 00 00               jg 0x140236da6
00236B46  8B C5                           mov eax, ebp
00236B48  48 C1 E8 12                     shr rax, 0x12
00236B4C  48 8B 3C C7                     mov rdi, qword ptr [rdi + rax*8]
00236B50  48 85 FF                        test rdi, rdi
00236B53  74 2E                           je 0x140236b83
00236B55  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00236B59  B8 01 00 00 00                  mov eax, 1
00236B5E  F0 0F C1 47 10                  lock xadd dword ptr [rdi + 0x10], eax
00236B63  FF C0                           inc eax
00236B65  66 85 C0                        test ax, ax
00236B68  0F 84 5B 03 00 00               je 0x140236ec9
00236B6E  66 83 F8 01                     cmp ax, 1
00236B72  75 07                           jne 0x140236b7b
00236B74  F0 FF 81 28 02 00 00            lock inc dword ptr [rcx + 0x228]
00236B7B  44 8B 74 24 38                  mov r14d, dword ptr [rsp + 0x38]
00236B80  4C 03 37                        add r14, qword ptr [rdi]
00236B83  41 0F 0D 4D 68                  prefetchw byte ptr [r13 + 0x68]
00236B88  49 8B 45 68                     mov rax, qword ptr [r13 + 0x68]
00236B8C  48 8B C8                        mov rcx, rax
00236B8F  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00236B93  48 83 F9 10                     cmp rcx, 0x10
00236B97  48 8D 50 F0                     lea rdx, [rax - 0x10]
00236B9B  48 0F 46 D6                     cmovbe rdx, rsi
00236B9F  A8 02                           test al, 2
00236BA1  0F 85 A8 02 00 00               jne 0x140236e4f
00236BA7  F0 49 0F B1 55 68               lock cmpxchg qword ptr [r13 + 0x68], rdx
00236BAD  0F 85 9C 02 00 00               jne 0x140236e4f
00236BB3  49 8D 4D 68                     lea rcx, [r13 + 0x68]
00236BB7  E8 44 AA 0A 00                  call 0x1402e1600
00236BBC  4D 85 F6                        test r14, r14
00236BBF  0F 84 6D 02 00 00               je 0x140236e32
00236BC5  44 3B 64 24 34                  cmp r12d, dword ptr [rsp + 0x34]
00236BCA  49 8B CE                        mov rcx, r14
00236BCD  44 0F 47 64 24 34               cmova r12d, dword ptr [rsp + 0x34]
00236BD3  41 8B D4                        mov edx, r12d
00236BD6  E8 45 03 00 00                  call 0x140236f20
00236BDB  84 C0                           test al, al
00236BDD  0F 84 BE 02 00 00               je 0x140236ea1
00236BE3  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
00236BE6  48 03 43 28                     add rax, qword ptr [rbx + 0x28]
00236BEA  49 3B 45 28                     cmp rax, qword ptr [r13 + 0x28]
00236BEE  7D 2A                           jge 0x140236c1a
00236BF0  41 8B 85 14 01 00 00            mov eax, dword ptr [r13 + 0x114]
00236BF7  A8 0F                           test al, 0xf
00236BF9  74 1F                           je 0x140236c1a
00236BFB  40 38 74 24 30                  cmp byte ptr [rsp + 0x30], sil
00236C00  74 18                           je 0x140236c1a
00236C02  40 38 74 24 31                  cmp byte ptr [rsp + 0x31], sil
00236C07  75 11                           jne 0x140236c1a
00236C09  41 F7 85 98 00 00 00 00 02 00 00  test dword ptr [r13 + 0x98], 0x200
00236C14  0F 84 95 02 00 00               je 0x140236eaf
00236C1A  8B C6                           mov eax, esi
00236C1C  89 43 3C                        mov dword ptr [rbx + 0x3c], eax
00236C1F  B8 FF FF FF FF                  mov eax, 0xffffffff
00236C24  48 8B 6F 08                     mov rbp, qword ptr [rdi + 8]
00236C28  F0 0F C1 47 10                  lock xadd dword ptr [rdi + 0x10], eax
00236C2D  FF C8                           dec eax
00236C2F  66 85 C0                        test ax, ax
00236C32  75 1D                           jne 0x140236c51
00236C34  48 8B 8D C0 00 00 00            mov rcx, qword ptr [rbp + 0xc0]
00236C3B  48 85 C9                        test rcx, rcx
00236C3E  74 0A                           je 0x140236c4a
00236C40  45 33 C0                        xor r8d, r8d
00236C43  33 D2                           xor edx, edx
00236C45  E8 C6 86 10 00                  call 0x14033f310
00236C4A  F0 FF 8D 28 02 00 00            lock dec dword ptr [rbp + 0x228]
00236C51  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00236C55  41 2B C4                        sub eax, r12d
00236C58  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00236C5C  0F 85 73 FE FF FF               jne 0x140236ad5
00236C62  8B 43 3C                        mov eax, dword ptr [rbx + 0x3c]
00236C65  65 01 04 25 68 89 00 00         add dword ptr gs:[0x8968], eax
00236C6D  39 73 3C                        cmp dword ptr [rbx + 0x3c], esi
00236C70  0F 85 E7 01 00 00               jne 0x140236e5d
00236C76  F7 05 90 FE D8 00 00 00 02 00   test dword ptr [rip + 0xd8fe90], 0x20000
00236C80  0F 84 A5 00 00 00               je 0x140236d2b
00236C86  8B 6B 38                        mov ebp, dword ptr [rbx + 0x38]
00236C89  48 8D 7B 28                     lea rdi, [rbx + 0x28]
00236C8D  44 8B 73 30                     mov r14d, dword ptr [rbx + 0x30]
00236C91  49 8B CD                        mov rcx, r13
00236C94  4C 8B BB B0 00 00 00            mov r15, qword ptr [rbx + 0xb0]
00236C9B  E8 1C 0D 00 00                  call 0x1402379bc
00236CA0  41 B8 43 63 53 63               mov r8d, 0x63536343
00236CA6  48 8B D0                        mov rdx, rax
00236CA9  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00236CAD  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
00236CB5  49 8D 4D 60                     lea rcx, [r13 + 0x60]
00236CB9  E8 02 0C 00 00                  call 0x1402378c0
00236CBE  48 85 FF                        test rdi, rdi
00236CC1  0F 84 7B 01 00 00               je 0x140236e42
00236CC7  48 8B 07                        mov rax, qword ptr [rdi]
00236CCA  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00236CD2  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00236CDA  4C 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r15
00236CE2  41 B9 0A 16 00 00               mov r9d, 0x160a
00236CE8  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00236CF0  BA 01 00 00 00                  mov edx, 1
00236CF5  44 89 B4 24 A8 00 00 00         mov dword ptr [rsp + 0xa8], r14d
00236CFD  41 B8 00 00 02 80               mov r8d, 0x80020000
00236D03  89 AC 24 AC 00 00 00            mov dword ptr [rsp + 0xac], ebp
00236D0A  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00236D12  48 C7 84 24 88 00 00 00 20 00 00 00  mov qword ptr [rsp + 0x88], 0x20
00236D1E  C7 44 24 20 02 19 50 00         mov dword ptr [rsp + 0x20], 0x501902
00236D26  E8 25 E6 FF FF                  call 0x140235350
00236D2B  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00236D30  0F B6 6C 24 30                  movzx ebp, byte ptr [rsp + 0x30]
00236D35  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
00236D3A  40 0F B6 C5                     movzx eax, bpl
00236D3E  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00236D43  F6 D8                           neg al
00236D45  1B D2                           sbb edx, edx
00236D47  81 E2 16 00 00 80               and edx, 0x80000016
00236D4D  89 17                           mov dword ptr [rdi], edx
00236D4F  48 8D 53 28                     lea rdx, [rbx + 0x28]
00236D53  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
00236D56  44 8B 43 30                     mov r8d, dword ptr [rbx + 0x30]
00236D5A  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00236D5E  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00236D63  E8 7C 08 00 00                  call 0x1402375e4
00236D68  8B F0                           mov esi, eax
00236D6A  85 C0                           test eax, eax
00236D6C  0F 88 7E 01 00 00               js 0x140236ef0
00236D72  8B C6                           mov eax, esi
00236D74  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00236D7C  48 33 CC                        xor rcx, rsp
00236D7F  E8 BC 58 47 00                  call 0x1406ac640
00236D84  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
00236D8C  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00236D90  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
00236D94  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00236D98  49 8B E3                        mov rsp, r11
00236D9B  41 5F                           pop r15
00236D9D  41 5E                           pop r14
00236D9F  41 5D                           pop r13
00236DA1  41 5C                           pop r12
00236DA3  5F                              pop rdi
00236DA4  C3                              ret
00236DA5  CC                              int3
00236DA6  8B D6                           mov edx, esi
00236DA8  B9 19 00 00 00                  mov ecx, 0x19
00236DAD  44 8B C1                        mov r8d, ecx
00236DB0  B8 01 00 00 00                  mov eax, 1
00236DB5  83 C1 07                        add ecx, 7
00236DB8  FF C2                           inc edx
00236DBA  48 D3 E0                        shl rax, cl
00236DBD  4C 3B C8                        cmp r9, rax
00236DC0  7F EB                           jg 0x140236dad
00236DC2  48 8B C5                        mov rax, rbp
00236DC5  41 8B C8                        mov ecx, r8d
00236DC8  48 D3 F8                        sar rax, cl
00236DCB  48 8B 3C C7                     mov rdi, qword ptr [rdi + rax*8]
00236DCF  48 85 FF                        test rdi, rdi
00236DD2  0F 84 AB FD FF FF               je 0x140236b83
00236DD8  85 D2                           test edx, edx
00236DDA  0F 84 70 FD FF FF               je 0x140236b50
00236DE0  41 8B C8                        mov ecx, r8d
00236DE3  B8 01 00 00 00                  mov eax, 1
00236DE8  48 D3 E0                        shl rax, cl
00236DEB  41 83 C0 F9                     add r8d, -7
00236DEF  48 FF C8                        dec rax
00236DF2  41 8B C8                        mov ecx, r8d
00236DF5  48 23 E8                        and rbp, rax
00236DF8  FF CA                           dec edx
00236DFA  48 8B C5                        mov rax, rbp
00236DFD  48 D3 F8                        sar rax, cl
00236E00  48 8B 3C C7                     mov rdi, qword ptr [rdi + rax*8]
00236E04  48 85 FF                        test rdi, rdi
00236E07  75 CF                           jne 0x140236dd8
00236E09  E9 42 FD FF FF                  jmp 0x140236b50
00236E0E  40 38 B1 C9 00 00 00            cmp byte ptr [rcx + 0xc9], sil
00236E15  0F 85 B0 FC FF FF               jne 0x140236acb
00236E1B  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00236E1F  48 89 81 D0 00 00 00            mov qword ptr [rcx + 0xd0], rax
00236E26  C6 81 C9 00 00 00 01            mov byte ptr [rcx + 0xc9], 1
00236E2D  E9 99 FC FF FF                  jmp 0x140236acb
00236E32  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00236E36  44 3B E0                        cmp r12d, eax
00236E39  44 0F 47 E0                     cmova r12d, eax
00236E3D  E9 13 FE FF FF                  jmp 0x140236c55
00236E42  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
00236E4A  E9 83 FE FF FF                  jmp 0x140236cd2
00236E4F  49 8D 4D 68                     lea rcx, [r13 + 0x68]
00236E53  E8 78 CA 02 00                  call 0x1402638d0
00236E58  E9 56 FD FF FF                  jmp 0x140236bb3
00236E5D  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00236E62  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00236E67  48 8D 8F 00 03 00 00            lea rcx, [rdi + 0x300]
00236E6E  E8 2D E9 03 00                  call 0x1402757a0
00236E73  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
00236E76  48 C1 E8 0C                     shr rax, 0xc
00236E7A  40 38 35 07 ED C2 00            cmp byte ptr [rip + 0xc2ed07], sil
00236E81  74 64                           je 0x140236ee7
00236E83  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00236E8B  48 01 81 48 04 00 00            add qword ptr [rcx + 0x448], rax
00236E92  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00236E97  E8 44 BE 10 00                  call 0x140342ce0
00236E9C  E9 D1 FE FF FF                  jmp 0x140236d72
00236EA1  39 73 3C                        cmp dword ptr [rbx + 0x3c], esi
00236EA4  0F 85 39 FD FF FF               jne 0x140236be3
00236EAA  E9 6B FD FF FF                  jmp 0x140236c1a
00236EAF  48 8B 83 C0 00 00 00            mov rax, qword ptr [rbx + 0xc0]
00236EB6  40 38 30                        cmp byte ptr [rax], sil
00236EB9  0F 85 5B FD FF FF               jne 0x140236c1a
00236EBF  B8 01 00 00 00                  mov eax, 1
00236EC4  E9 53 FD FF FF                  jmp 0x140236c1c
00236EC9  45 33 C9                        xor r9d, r9d
00236ECC  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00236ED1  BA AC 0B 00 00                  mov edx, 0xbac
00236ED6  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
00236EDD  41 8D 49 34                     lea ecx, [r9 + 0x34]
00236EE1  E8 7A 67 2C 00                  call 0x1404fd660
00236EE6  CC                              int3
00236EE7  48 01 87 88 04 00 00            add qword ptr [rdi + 0x488], rax
00236EEE  EB A2                           jmp 0x140236e92
00236EF0  8B 07                           mov eax, dword ptr [rdi]
00236EF2  40 84 ED                        test bpl, bpl
00236EF5  74 12                           je 0x140236f09
00236EF7  3D 16 00 00 80                  cmp eax, 0x80000016
00236EFC  0F 85 70 FE FF FF               jne 0x140236d72
00236F02  89 37                           mov dword ptr [rdi], esi
00236F04  E9 69 FE FF FF                  jmp 0x140236d72
00236F09  85 C0                           test eax, eax
00236F0B  0F 85 61 FE FF FF               jne 0x140236d72
00236F11  89 37                           mov dword ptr [rdi], esi
00236F13  E9 5A FE FF FF                  jmp 0x140236d72
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcFlushCacheOneRange(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int8 v_stack_mB7;
    unsigned __int8 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 12401898)) ^ (v_rsp);
    v_stack_m38 = result;
    result = 0;
    v_stack_m78 = 0;
    v_rsi = 0;
    v_stack_m90 = *(unsigned __int64 *)(a1);
    v_stack_m68 = *(unsigned __int64 *)(a1 + 8);
    v_stack_mB8 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 132));
    v_stack_mB7 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 133));
    v_stack_mA0 = *(unsigned __int64 *)(a1 + 72);
    v_stack_mA8 = *(unsigned __int64 *)(a1 + 112);
    v_stack_m98 = *(unsigned __int64 *)(a1 + 24);
    v_stack_m88 = v_xmm0;
    if ((*(unsigned __int8 *)(a1 + 200)) != 0) goto loc_00236E0E;
loc_00236ACB:
    v_stack_mB4 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
    *(unsigned int *)(a1 + 60) = 0;
loc_00236AD5:
    v_rbp = ((unsigned int)(*(unsigned int *)(a1 + 48))) - ((unsigned int)(*(unsigned int *)(a1 + 48)));
    v_rbp = (v_rbp) + (*(unsigned __int64 *)(a1 + 40));
    a3 = 0;
    a2 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) & (0x3FFFFULL));
    v_stack_mB0 = (unsigned int)(result);
    v_r12 = (unsigned int)(((unsigned int)(0x40000ULL)) - ((unsigned int)(result)));
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 16) + 104, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(a1 + 16) + 104;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1 + 16) + 104;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32)) > 0x2000000ULL) goto loc_00236DA6;
    result = ((unsigned int)((unsigned int)(v_rbp))) >> (18);
loc_00236B50:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 88) + result * 8) == 0) goto loc_00236B83;
    result = (unsigned int)((1) + 1);
    if ((unsigned __int16)(result) == 0) goto loc_00236EC9;
    if (((unsigned __int16)(result)) == 1) {
    }
    v_r14 = ((unsigned int)(v_stack_mB0)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 88) + result * 8)));
loc_00236B83:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 104)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 104) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 104))) & (2)) != 0) goto loc_00236E4F;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 104))) & (2)) != 0) goto loc_00236E4F;
loc_00236BB3:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 16) + 104, a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32));
    if (v_r14 == 0) goto loc_00236E32;
    if (((unsigned int)(v_r12)) > v_stack_mB4) { v_r12 = v_stack_mB4; }
    result = MmSetAddressRangeModifiedEx(v_r14, (unsigned int)((unsigned int)(v_r12)), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32));
    if ((unsigned __int8)(result) == 0) goto loc_00236EA1;
loc_00236BE3:
    result = ((unsigned int)(*(unsigned int *)(a1 + 48))) + (*(unsigned __int64 *)(a1 + 40));
    if (result >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 40))) goto loc_00236C1A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 276)))) & (15)) == 0) goto loc_00236C1A;
    if (v_stack_mB8 == 0) goto loc_00236C1A;
    if (v_stack_mB7 != 0) goto loc_00236C1A;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 152)) & (512)) == 0) goto loc_00236EAF;
loc_00236C1A:
loc_00236C1C:
    *(unsigned int *)(a1 + 60) = 0;
    result = (unsigned int)(((unsigned int)(0xFFFFFFFFULL)) - 1);
    if ((unsigned __int16)(result) != 0) goto loc_00236C51;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 88) + result * 8) + 8) + 192) != 0) {
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 88) + result * 8) + 8) + 192), a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32));
    }
loc_00236C51:
loc_00236C55:
    result = (unsigned int)(((unsigned int)(v_stack_mB4)) - ((unsigned int)(v_r12)));
    v_stack_mB4 = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_00236AD5;
    if ((*(unsigned int *)(a1 + 60)) != 0) goto loc_00236E5D;
    if (((*(unsigned int *)(v_rip + 14220944)) & (0x20000ULL)) == 0) goto loc_00236D2B;
    result = CcReferenceSharedCacheMapFileObject(*(unsigned __int64 *)(a1 + 16), a2, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32));
    v_stack_m50 = *(unsigned __int64 *)(result + 24);
    result = ObFastDereferenceObjectDeferDelete(*(unsigned __int64 *)(a1 + 16) + 96, result, (unsigned int)(0x63536343ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 32));
    if (a1 + 40 == 0) goto loc_00236E42;
    v_stack_m48 = *(unsigned __int64 *)(a1 + 40);
loc_00236CD2:
    v_stack_m58 = *(unsigned __int64 *)(a1 + 176);
    v_stack_m68 = v_stack_m58;
    v_stack_m40 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
    v_stack_m3C = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)));
    v_stack_m60 = 32;
    v_stack_mC8 = 0x501902ULL;
    result = EtwTraceKernelEvent(v_stack_m68, 1, (unsigned int)(0x80020000ULL), (unsigned int)(0x160AULL));
loc_00236D2B:
    result = (unsigned __int8)(-((unsigned __int8)(v_stack_mB8)));
    a2 = (unsigned int)((1) & (0x80000016ULL));
    *(unsigned int *)(v_stack_mA8) = a2;
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)));
    v_stack_mC8 = v_stack_mA8;
    result = MmFlushSection(v_stack_m98, a1 + 40, (unsigned int)(*(unsigned int *)(a1 + 48)), v_stack_mA0);
    if (sign_flag) goto loc_00236EF0;
loc_00236D72:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a1 + 40, (unsigned int)(*(unsigned int *)(a1 + 48)), v_stack_mA0);
    return result;
loc_00236DA6:
loc_00236DAD:
    a1 = (unsigned int)((25) + (7));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72)))) + 1);
    result = (1) << ((unsigned __int8)(a1));
    if (v_stack_mA0 > result) goto loc_00236DAD;
    result = (*(unsigned __int64 *)(v_stack_m28 + 64)) >> (25);
    if (*(unsigned __int64 *)(v_stack_mA8 + result * 8) == 0) goto loc_00236B83;
loc_00236DD8:
    if (a2 == 0) goto loc_00236B50;
    result = (1) << (25);
    a3 = (unsigned int)((25) + (-7));
    result = (result) - 1;
    v_rbp = (*(unsigned __int64 *)(v_stack_m28 + 64)) & (result);
    a2 = (unsigned int)((a2) - 1);
    result = (v_rbp) >> ((unsigned __int8)((unsigned int)(a3)));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA8 + result * 8) + result * 8) != 0) goto loc_00236DD8;
    goto loc_00236B50;
loc_00236E0E:
    if ((*(unsigned __int8 *)((unsigned int)(a3) + 201)) != ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 72)))) goto loc_00236ACB;
    *(unsigned __int64 *)((unsigned int)(a3) + 208) = *(unsigned __int64 *)((unsigned int)(a3) + 40);
    *(unsigned __int8 *)((unsigned int)(a3) + 201) = 1;
    goto loc_00236ACB;
loc_00236E32:
    if (((unsigned int)(v_r12)) > ((unsigned int)((unsigned int)(v_stack_m8C)))) { v_r12 = (unsigned int)((unsigned int)(v_stack_m8C)); }
    goto loc_00236C55;
loc_00236E42:
    v_stack_m20 = *(unsigned __int64 *)(v_stack_m28 + 72);
    goto loc_00236CD2;
loc_00236E4F:
    result = ExfReleasePushLock(*(unsigned __int64 *)(a1 + 16) + 104, a2, a3, v_stack_mA0);
    goto loc_00236BB3;
loc_00236E5D:
    result = KeAcquireInStackQueuedSpinLock(v_stack_m68 + 768, v_stack_m60, a3, v_stack_mA0);
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 48))) >> (12);
    if ((*(unsigned __int8 *)(v_rip + 12774663)) == ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 72)))) goto loc_00236EE7;
loc_00236E92:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m60, v_stack_m60, a3, v_stack_mA0);
    goto loc_00236D72;
loc_00236EA1:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 60)) != ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72)))) goto loc_00236BE3;
    goto loc_00236C1A;
loc_00236EAF:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 192))) != ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 72)))) goto loc_00236C1A;
    goto loc_00236C1C;
loc_00236EC9:
    a4 = 0;
    v_stack_mA0 = *(unsigned __int64 *)(v_stack_m28 + 72);
    result = KeBugCheckEx(a4 + 52, (unsigned int)(0xBACULL), 0xFFFFFFFFC0000420ULL, a4);
loc_00236EE7:
    goto loc_00236E92;
loc_00236EF0:
    if ((unsigned __int8)(v_rbp) == 0) goto loc_00236F09;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68)))) != 0x80000016ULL) goto loc_00236D72;
    *(unsigned int *)(v_stack_m68) = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    goto loc_00236D72;
loc_00236F09:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68))) != 0) goto loc_00236D72;
    *(unsigned int *)(v_stack_m68) = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    goto loc_00236D72;
}
```

## 5. (Beta) C Style

```c
int64_t CcFlushCacheOneRange(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint8_t v_stack_mB7;
    uint8_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0xBD3CEA)) ^ (local_rsp);
    v_stack_m38 = result;
    result = 0;
    v_stack_m78 = 0;
    local_rsi = 0;
    v_stack_m90 = *(uint64_t *)(arg1);
    v_stack_m68 = *(uint64_t *)(arg1 + 0x8);
    v_stack_mB8 = (uint8_t)(*(uint8_t *)(arg1 + 0x84));
    v_stack_mB7 = (uint8_t)(*(uint8_t *)(arg1 + 0x85));
    v_stack_mA0 = *(uint64_t *)(arg1 + 0x48);
    v_stack_mA8 = *(uint64_t *)(arg1 + 0x70);
    v_stack_m98 = *(uint64_t *)(arg1 + 0x18);
    v_stack_m88 = v_xmm0;
    if ((*(uint8_t *)(arg1 + 0xC8)) != 0) goto loc_00236E0E;
loc_00236ACB:
    v_stack_mB4 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    *(uint32_t *)(arg1 + 0x3C) = 0;
loc_00236AD5:
    local_rbp = ((uint32_t)(*(uint32_t *)(arg1 + 0x30))) - ((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    local_rbp = (local_rbp) + (*(uint64_t *)(arg1 + 0x28));
    Arg3 = 0;
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) & (0x3FFFFULL));
    v_stack_mB0 = (uint32_t)(result);
    local_r12 = (uint32_t)(((uint32_t)(0x40000ULL)) - ((uint32_t)(result)));
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0x10) + 104, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(uint64_t *)(arg1 + 0x10) + 104;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x10) + 104;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20)) > 0x2000000ULL) goto loc_00236DA6;
    result = ((uint32_t)((uint32_t)(local_rbp))) >> (18);
loc_00236B50:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x58) + result * 8) == 0) goto loc_00236B83;
    result = (uint32_t)((1) + 1);
    if ((uint16_t)(result) == 0) goto loc_00236EC9;
    if (((uint16_t)(result)) == 1) {
    }
    local_r14 = ((uint32_t)(v_stack_mB0)) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x58) + result * 8)));
loc_00236B83:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x68)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x68) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x68))) & (2)) != 0) goto loc_00236E4F;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x68))) & (2)) != 0) goto loc_00236E4F;
loc_00236BB3:
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x10) + 104, Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20));
    if (local_r14 == 0) goto loc_00236E32;
    if (((uint32_t)(local_r12)) > v_stack_mB4) { local_r12 = v_stack_mB4; }
    result = MmSetAddressRangeModifiedEx(local_r14, (uint32_t)((uint32_t)(local_r12)), Arg3, *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20));
    if ((uint8_t)(result) == 0) goto loc_00236EA1;
loc_00236BE3:
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x30))) + (*(uint64_t *)(arg1 + 0x28));
    if (result >= (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x28))) goto loc_00236C1A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x114)))) & (15)) == 0) goto loc_00236C1A;
    if (v_stack_mB8 == 0) goto loc_00236C1A;
    if (v_stack_mB7 != 0) goto loc_00236C1A;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x98)) & (512)) == 0) goto loc_00236EAF;
loc_00236C1A:
loc_00236C1C:
    *(uint32_t *)(arg1 + 0x3C) = 0;
    result = (uint32_t)(((uint32_t)(0xFFFFFFFFULL)) - 1);
    if ((uint16_t)(result) != 0) goto loc_00236C51;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x58) + result * 8) + 0x8) + 0xC0) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        result = KeSetEvent(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x58) + result * 8) + 0x8) + 0xC0), Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20));
    }
loc_00236C51:
loc_00236C55:
    result = (uint32_t)(((uint32_t)(v_stack_mB4)) - ((uint32_t)(local_r12)));
    v_stack_mB4 = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_00236AD5;
    if ((*(uint32_t *)(arg1 + 0x3C)) != 0) goto loc_00236E5D;
    if (((*(uint32_t *)(v_rip + 0xD8FE90)) & (0x20000ULL)) == 0) goto loc_00236D2B;
    result = CcReferenceSharedCacheMapFileObject(*(uint64_t *)(arg1 + 0x10), Arg2, Arg3, *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20));
    v_stack_m50 = *(uint64_t *)(result + 0x18);
    result = ObFastDereferenceObjectDeferDelete(*(uint64_t *)(arg1 + 0x10) + 96, result, (uint32_t)(0x63536343ULL), *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x20));
    if (Arg1 + 40 == 0) goto loc_00236E42;
    v_stack_m48 = *(uint64_t *)(arg1 + 0x28);
loc_00236CD2:
    v_stack_m58 = *(uint64_t *)(arg1 + 0xB0);
    v_stack_m68 = v_stack_m58;
    v_stack_m40 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    v_stack_m3C = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)));
    v_stack_m60 = 32;
    v_stack_mC8 = 0x501902ULL;
    result = EtwTraceKernelEvent(v_stack_m68, 1, (uint32_t)(0x80020000ULL), (uint32_t)(0x160AULL));
loc_00236D2B:
    result = (uint8_t)(-((uint8_t)(v_stack_mB8)));
    Arg2 = (uint32_t)((1) & (0x80000016ULL));
    *(uint32_t *)(v_stack_mA8) = Arg2;
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)));
    v_stack_mC8 = v_stack_mA8;
    result = MmFlushSection(v_stack_m98, Arg1 + 40, (uint32_t)(*(uint32_t *)(arg1 + 0x30)), v_stack_mA0);
    if (sign_flag) goto loc_00236EF0;
loc_00236D72:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg1 + 40, (uint32_t)(*(uint32_t *)(arg1 + 0x30)), v_stack_mA0);
    return result;
loc_00236DA6:
loc_00236DAD:
    Arg1 = (uint32_t)((25) + (7));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48)))) + 1);
    result = (1) << ((uint8_t)(Arg1));
    if (v_stack_mA0 > result) goto loc_00236DAD;
    result = (*(uint64_t *)(v_stack_m28 + 0x40)) >> (25);
    if (*(uint64_t *)(v_stack_mA8 + result * 8) == 0) goto loc_00236B83;
loc_00236DD8:
    if (Arg2 == 0) goto loc_00236B50;
    result = (1) << (25);
    Arg3 = (uint32_t)((25) + (-7));
    result = (result) - 1;
    local_rbp = (*(uint64_t *)(v_stack_m28 + 0x40)) & (result);
    Arg2 = (uint32_t)((Arg2) - 1);
    result = (local_rbp) >> ((uint8_t)((uint32_t)(Arg3)));
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mA8 + result * 8) + result * 8) != 0) goto loc_00236DD8;
    goto loc_00236B50;
loc_00236E0E:
    if ((*(uint8_t *)((uint32_t)(Arg3) + 0xC9)) != ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x48)))) goto loc_00236ACB;
    *(uint64_t *)((uint32_t)(Arg3) + 0xD0) = *(uint64_t *)((uint32_t)(Arg3) + 0x28);
    *(uint8_t *)((uint32_t)(Arg3) + 0xC9) = 1;
    goto loc_00236ACB;
loc_00236E32:
    if (((uint32_t)(local_r12)) > ((uint32_t)((uint32_t)(v_stack_m8C)))) { local_r12 = (uint32_t)((uint32_t)(v_stack_m8C)); }
    goto loc_00236C55;
loc_00236E42:
    v_stack_m20 = *(uint64_t *)(v_stack_m28 + 0x48);
    goto loc_00236CD2;
loc_00236E4F:
    result = ExfReleasePushLock(*(uint64_t *)(arg1 + 0x10) + 104, Arg2, Arg3, v_stack_mA0);
    goto loc_00236BB3;
loc_00236E5D:
    result = KeAcquireInStackQueuedSpinLock(v_stack_m68 + 768, v_stack_m60, Arg3, v_stack_mA0);
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x30))) >> (12);
    if ((*(uint8_t *)(v_rip + 0xC2ED07)) == ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x48)))) goto loc_00236EE7;
loc_00236E92:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m60, v_stack_m60, Arg3, v_stack_mA0);
    goto loc_00236D72;
loc_00236EA1:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x3C)) != ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48)))) goto loc_00236BE3;
    goto loc_00236C1A;
loc_00236EAF:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0xC0))) != ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x48)))) goto loc_00236C1A;
    goto loc_00236C1C;
loc_00236EC9:
    a4 = 0;
    v_stack_mA0 = *(uint64_t *)(v_stack_m28 + 0x48);
    result = KeBugCheckEx(a4 + 52, (uint32_t)(0xBACULL), 0xFFFFFFFFC0000420ULL, a4);
loc_00236EE7:
    goto loc_00236E92;
loc_00236EF0:
    if ((uint8_t)(local_rbp) == 0) goto loc_00236F09;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68)))) != 0x80000016ULL) goto loc_00236D72;
    *(uint32_t *)(v_stack_m68) = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    goto loc_00236D72;
loc_00236F09:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68))) != 0) goto loc_00236D72;
    *(uint32_t *)(v_stack_m68) = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    goto loc_00236D72;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x38` | `32` | `R` |
| `Arg1` | `+ 0x3C` | `32` | `R` |
| `Arg1` | `+ 0x3C` | `32` | `W` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x84` | `8` | `R` |
| `Arg1` | `+ 0x85` | `8` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0xC8` | `8` | `R` |
| `Arg1` | `+ 0xC9` | `8` | `R` |
| `Arg1` | `+ 0xC9` | `8` | `W` |
| `Arg1` | `+ 0xD0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00236A30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
