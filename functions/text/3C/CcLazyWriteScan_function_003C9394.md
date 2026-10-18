# CcLazyWriteScan

- RVA: `0x003C9394`–`0x003C9ADE` (길이 `1,866` bytes)
- VA: `0x00000001403C9394`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008F610`
- 디코드: `447`개 명령, `1,866/1,866` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x003C940C` → [CcScanLogHandleList](../38/CcScanLogHandleList_function_0038A26C.md) (function, `0x0038A26C`)
- `0x003C941C` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003C942D` → [CcSetLazyWriteScanQueuedInternal](CcSetLazyWriteScanQueuedInternal_function_003C9F60.md) (function, `0x003C9F60`)
- `0x003C94DA` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003C94E9` → [CcRescheduleLazyWriteScan](CcRescheduleLazyWriteScan_function_003CA134.md) (function, `0x003CA134`)
- `0x003C94F2` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003C957C` → [CcCalculatePagesToWrite](../38/CcCalculatePagesToWrite_function_003895AC.md) (function, `0x003895AC`)
- `0x003C9596` → [CcAdjustThrottleForPartition](../57/CcAdjustThrottleForPartition_function_0057B4BC.md) (function, `0x0057B4BC`)
- `0x003C965C` → [CcPerfLogLazyWriteScan](../4A/CcPerfLogLazyWriteScan_function_004ABD64.md) (function, `0x004ABD64`)
- `0x003C96BD` → [CcShouldLazyWriteCacheMap](../38/CcShouldLazyWriteCacheMap_function_003897A0.md) (function, `0x003897A0`)
- `0x003C96D4` → [CcGetNodeForLazyWrite](../40/CcGetNodeForLazyWrite_function_004031AC.md) (function, `0x004031AC`)
- `0x003C9837` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003C9848` → [CcAllocateWorkQueueEntry](../35/CcAllocateWorkQueueEntry_function_0035710C.md) (function, `0x0035710C`)
- `0x003C9873` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003C98BC` → [CcPostWorkQueue](../35/CcPostWorkQueue_function_00356808.md) (function, `0x00356808`)
- `0x003C98E2` → [CcIncrementWriteBehindPriority](../57/CcIncrementWriteBehindPriority_function_0057B8AC.md) (function, `0x0057B8AC`)
- `0x003C990F` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003C9922` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003C9995` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003C99F8` → [CcPostWorkQueue](../35/CcPostWorkQueue_function_00356808.md) (function, `0x00356808`)
- `0x003C9A37` → [CcComputeNextScanTime](../4A/CcComputeNextScanTime_function_004A2574.md) (function, `0x004A2574`)
- `0x003C9A56` → [CcRescheduleLazyWriteScan](CcRescheduleLazyWriteScan_function_003CA134.md) (function, `0x003CA134`)
- `0x003C9A7F` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003C9A8D` → [CcUpdateTimeOnLogHandles](../4C/CcUpdateTimeOnLogHandles_function_004C6D0C.md) (function, `0x004C6D0C`)
- `0x003C9AA7` → [CcPerfLogLoggedStreamsStats](../4B/CcPerfLogLoggedStreamsStats_function_004B2400.md) (function, `0x004B2400`)
- `0x003C9ABD` → [CcPostDeferredWrites](../35/CcPostDeferredWrites_function_003590FC.md) (function, `0x003590FC`)

### Direct callers
- [CcWorkerThread](../48/CcWorkerThread_function_0048F0F0.md) at `0x0048F39B`

### Static image references
- `0x003C93D5` → RVA `0x00FC6EA0` (`ALMOSTRO`; read)
- `0x003C95DB` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x003C95EB` → RVA `0x00E65B8C` (`.data`; read)
- `0x003C978A` → RVA `0x00E65B14` (`.data`; read/write)
- `0x003C9A0A` → RVA `0x00FC521C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003C9394  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003C9399  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
003C939E  55                              push rbp
003C939F  56                              push rsi
003C93A0  57                              push rdi
003C93A1  41 54                           push r12
003C93A3  41 55                           push r13
003C93A5  41 56                           push r14
003C93A7  41 57                           push r15
003C93A9  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
003C93AE  48 81 EC B0 00 00 00            sub rsp, 0xb0
003C93B5  33 F6                           xor esi, esi
003C93B7  33 C0                           xor eax, eax
003C93B9  48 89 45 FF                     mov qword ptr [rbp - 1], rax
003C93BD  0F 57 C0                        xorps xmm0, xmm0
003C93C0  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003C93CA  40 88 75 D7                     mov byte ptr [rbp - 0x29], sil
003C93CE  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
003C93D2  41 8B D9                        mov ebx, r9d
003C93D5  48 8B 05 C4 DA BF 00            mov rax, qword ptr [rip + 0xbfdac4]
003C93DC  4D 8B E8                        mov r13, r8
003C93DF  4C 8B FA                        mov r15, rdx
003C93E2  40 88 75 67                     mov byte ptr [rbp + 0x67], sil
003C93E6  48 8B F9                        mov rdi, rcx
003C93E9  89 75 DB                        mov dword ptr [rbp - 0x25], esi
003C93EC  44 8B E6                        mov r12d, esi
003C93EF  40 88 75 D9                     mov byte ptr [rbp - 0x27], sil
003C93F3  40 88 75 D8                     mov byte ptr [rbp - 0x28], sil
003C93F7  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
003C93FB  48 3B 48 08                     cmp rcx, qword ptr [rax + 8]
003C93FF  75 10                           jne 0x1403c9411
003C9401  4C 8D 4D 17                     lea r9, [rbp + 0x17]
003C9405  44 8B C3                        mov r8d, ebx
003C9408  48 8D 55 DB                     lea rdx, [rbp - 0x25]
003C940C  E8 5B 0E FC FF                  call 0x14038a26c
003C9411  48 8D 8F 00 03 00 00            lea rcx, [rdi + 0x300]
003C9418  48 8D 55 EF                     lea rdx, [rbp - 0x11]
003C941C  E8 7F C3 EA FF                  call 0x1402757a0
003C9421  48 8D 8F D8 03 00 00            lea rcx, [rdi + 0x3d8]
003C9428  45 33 C0                        xor r8d, r8d
003C942B  8B D3                           mov edx, ebx
003C942D  E8 2E 0B 00 00                  call 0x1403c9f60
003C9432  44 8B 8F 68 04 00 00            mov r9d, dword ptr [rdi + 0x468]
003C9439  4C 8D B7 20 04 00 00            lea r14, [rdi + 0x420]
003C9440  48 8B 87 58 04 00 00            mov rax, qword ptr [rdi + 0x458]
003C9447  33 D2                           xor edx, edx
003C9449  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
003C944D  49 F7 F1                        div r9
003C9450  33 D2                           xor edx, edx
003C9452  48 89 87 78 04 00 00            mov qword ptr [rdi + 0x478], rax
003C9459  4C 8B D0                        mov r10, rax
003C945C  48 8B 87 60 04 00 00            mov rax, qword ptr [rdi + 0x460]
003C9463  49 F7 F1                        div r9
003C9466  48 89 87 80 04 00 00            mov qword ptr [rdi + 0x480], rax
003C946D  4C 8B D8                        mov r11, rax
003C9470  4C 8B 01                        mov r8, qword ptr [rcx]
003C9473  B8 01 00 00 00                  mov eax, 1
003C9478  44 3B C8                        cmp r9d, eax
003C947B  76 1D                           jbe 0x1403c949a
003C947D  49 8B 06                        mov rax, qword ptr [r14]
003C9480  41 8D 49 FF                     lea ecx, [r9 - 1]
003C9484  8B D1                           mov edx, ecx
003C9486  49 0F AF CA                     imul rcx, r10
003C948A  49 0F AF D3                     imul rdx, r11
003C948E  49 03 88 00 49 00 00            add rcx, qword ptr [r8 + 0x4900]
003C9495  48 03 D0                        add rdx, rax
003C9498  EB 0D                           jmp 0x1403c94a7
003C949A  49 8B 16                        mov rdx, qword ptr [r14]
003C949D  49 8B 88 00 49 00 00            mov rcx, qword ptr [r8 + 0x4900]
003C94A4  48 8B C2                        mov rax, rdx
003C94A7  48 89 8F 58 04 00 00            mov qword ptr [rdi + 0x458], rcx
003C94AE  48 89 97 60 04 00 00            mov qword ptr [rdi + 0x460], rdx
003C94B5  48 85 C0                        test rax, rax
003C94B8  75 42                           jne 0x1403c94fc
003C94BA  40 38 B7 1A 04 00 00            cmp byte ptr [rdi + 0x41a], sil
003C94C1  75 39                           jne 0x1403c94fc
003C94C3  48 8D 87 90 04 00 00            lea rax, [rdi + 0x490]
003C94CA  48 39 00                        cmp qword ptr [rax], rax
003C94CD  75 15                           jne 0x1403c94e4
003C94CF  48 8D 4D EF                     lea rcx, [rbp - 0x11]
003C94D3  40 88 B7 19 04 00 00            mov byte ptr [rdi + 0x419], sil
003C94DA  E8 01 98 F7 FF                  call 0x140342ce0
003C94DF  E9 DE 05 00 00                  jmp 0x1403c9ac2
003C94E4  33 D2                           xor edx, edx
003C94E6  48 8B CF                        mov rcx, rdi
003C94E9  E8 46 0C 00 00                  call 0x1403ca134
003C94EE  48 8D 4D EF                     lea rcx, [rbp - 0x11]
003C94F2  E8 E9 97 F7 FF                  call 0x140342ce0
003C94F7  E9 BC 05 00 00                  jmp 0x1403c9ab8
003C94FC  48 8D 45 DF                     lea rax, [rbp - 0x21]
003C9500  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
003C9504  48 8D 8F 50 03 00 00            lea rcx, [rdi + 0x350]
003C950B  48 8D 45 DF                     lea rax, [rbp - 0x21]
003C950F  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
003C9513  48 8B 01                        mov rax, qword ptr [rcx]
003C9516  48 3B C1                        cmp rax, rcx
003C9519  74 43                           je 0x1403c955e
003C951B  48 39 48 08                     cmp qword ptr [rax + 8], rcx
003C951F  0F 85 DE 04 00 00               jne 0x1403c9a03
003C9525  48 8B 10                        mov rdx, qword ptr [rax]
003C9528  48 39 42 08                     cmp qword ptr [rdx + 8], rax
003C952C  0F 85 D1 04 00 00               jne 0x1403c9a03
003C9532  48 89 11                        mov qword ptr [rcx], rdx
003C9535  4C 8D 45 DF                     lea r8, [rbp - 0x21]
003C9539  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
003C953D  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
003C9541  4C 39 02                        cmp qword ptr [rdx], r8
003C9544  0F 85 B9 04 00 00               jne 0x1403c9a03
003C954A  48 89 50 08                     mov qword ptr [rax + 8], rdx
003C954E  4C 8D 45 DF                     lea r8, [rbp - 0x21]
003C9552  4C 89 00                        mov qword ptr [rax], r8
003C9555  48 89 02                        mov qword ptr [rdx], rax
003C9558  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
003C955C  EB B5                           jmp 0x1403c9513
003C955E  44 21 64 24 20                  and dword ptr [rsp + 0x20], r12d
003C9563  4D 8B C6                        mov r8, r14
003C9566  40 88 B7 1A 04 00 00            mov byte ptr [rdi + 0x41a], sil
003C956D  8B D3                           mov edx, ebx
003C956F  48 8D B7 38 04 00 00            lea rsi, [rdi + 0x438]
003C9576  48 8B CF                        mov rcx, rdi
003C9579  4C 8B CE                        mov r9, rsi
003C957C  E8 2B 00 FC FF                  call 0x1403895ac
003C9581  44 8B 8F D0 03 00 00            mov r9d, dword ptr [rdi + 0x3d0]
003C9588  4C 8B C6                        mov r8, rsi
003C958B  49 8B D6                        mov rdx, r14
003C958E  89 45 DB                        mov dword ptr [rbp - 0x25], eax
003C9591  48 8B CF                        mov rcx, rdi
003C9594  8B D8                           mov ebx, eax
003C9596  E8 21 1F 1B 00                  call 0x14057b4bc
003C959B  4C 8B 87 20 04 00 00            mov r8, qword ptr [rdi + 0x420]
003C95A2  48 8B 8F 70 04 00 00            mov rcx, qword ptr [rdi + 0x470]
003C95A9  44 8B 75 7F                     mov r14d, dword ptr [rbp + 0x7f]
003C95AD  4C 89 87 28 04 00 00            mov qword ptr [rdi + 0x428], r8
003C95B4  89 9F 30 04 00 00               mov dword ptr [rdi + 0x430], ebx
003C95BA  89 9F D0 03 00 00               mov dword ptr [rdi + 0x3d0], ebx
003C95C0  41 8B 97 98 00 00 00            mov edx, dword ptr [r15 + 0x98]
003C95C7  89 1C D1                        mov dword ptr [rcx + rdx*8], ebx
003C95CA  48 A1 14 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000014]
003C95D4  49 89 87 D8 00 00 00            mov qword ptr [r15 + 0xd8], rax
003C95DB  F7 05 2B D5 BF 00 00 00 02 00   test dword ptr [rip + 0xbfd52b], 0x20000
003C95E5  74 7A                           je 0x1403c9661
003C95E7  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
003C95EB  8B 0D 9B C5 A9 00               mov ecx, dword ptr [rip + 0xa9c59b]
003C95F1  4C 8B 8F 20 04 00 00            mov r9, qword ptr [rdi + 0x420]
003C95F8  44 8B 87 D0 03 00 00            mov r8d, dword ptr [rdi + 0x3d0]
003C95FF  48 8B 10                        mov rdx, qword ptr [rax]
003C9602  8B 87 08 03 00 00               mov eax, dword ptr [rdi + 0x308]
003C9608  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003C960D  48 8B 87 80 04 00 00            mov rax, qword ptr [rdi + 0x480]
003C9614  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003C9619  48 8B 87 78 04 00 00            mov rax, qword ptr [rdi + 0x478]
003C9620  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
003C9625  48 8B 87 48 04 00 00            mov rax, qword ptr [rdi + 0x448]
003C962C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003C9631  48 8B 87 40 04 00 00            mov rax, qword ptr [rdi + 0x440]
003C9638  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003C963D  48 8B 06                        mov rax, qword ptr [rsi]
003C9640  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
003C9645  49 8B CD                        mov rcx, r13
003C9648  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003C964D  48 8B 82 00 49 00 00            mov rax, qword ptr [rdx + 0x4900]
003C9654  41 8B D6                        mov edx, r14d
003C9657  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003C965C  E8 03 27 0E 00                  call 0x1404abd64
003C9661  44 8B 7D DB                     mov r15d, dword ptr [rbp - 0x25]
003C9665  48 8D B7 B8 02 00 00            lea rsi, [rdi + 0x2b8]
003C966C  48 8B 1E                        mov rbx, qword ptr [rsi]
003C966F  48 81 EB 88 00 00 00            sub rbx, 0x88
003C9676  33 C9                           xor ecx, ecx
003C9678  48 3B D9                        cmp rbx, rcx
003C967B  0F 84 2A 03 00 00               je 0x1403c99ab
003C9681  48 8D 83 88 00 00 00            lea rax, [rbx + 0x88]
003C9688  48 3B C6                        cmp rax, rsi
003C968B  0F 84 1A 03 00 00               je 0x1403c99ab
003C9691  48 85 C9                        test rcx, rcx
003C9694  45 8B CF                        mov r9d, r15d
003C9697  48 8B C3                        mov rax, rbx
003C969A  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
003C969F  48 0F 45 C1                     cmovne rax, rcx
003C96A3  48 8B D7                        mov rdx, rdi
003C96A6  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
003C96AA  45 33 C0                        xor r8d, r8d
003C96AD  48 8B 43 60                     mov rax, qword ptr [rbx + 0x60]
003C96B1  48 8B CB                        mov rcx, rbx
003C96B4  48 83 E0 F0                     and rax, 0xfffffffffffffff0
003C96B8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003C96BD  E8 DE 00 FC FF                  call 0x1403897a0
003C96C2  84 C0                           test al, al
003C96C4  0F 84 01 02 00 00               je 0x1403c98cb
003C96CA  45 33 E4                        xor r12d, r12d
003C96CD  48 8B CB                        mov rcx, rbx
003C96D0  4C 89 65 07                     mov qword ptr [rbp + 7], r12
003C96D4  E8 D3 9A 03 00                  call 0x1404031ac
003C96D9  0F BA A3 98 00 00 00 18         bt dword ptr [rbx + 0x98], 0x18
003C96E1  45 8D 44 24 01                  lea r8d, [r12 + 1]
003C96E6  4C 8B E8                        mov r13, rax
003C96E9  73 5E                           jae 0x1403c9749
003C96EB  48 A1 20 03 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000320]
003C96F5  48 8B 8B F8 00 00 00            mov rcx, qword ptr [rbx + 0xf8]
003C96FC  44 88 45 D9                     mov byte ptr [rbp - 0x27], r8b
003C9700  44 09 81 90 00 00 00            or dword ptr [rcx + 0x90], r8d
003C9707  48 8B 8B F8 00 00 00            mov rcx, qword ptr [rbx + 0xf8]
003C970E  48 8B 83 08 01 00 00            mov rax, qword ptr [rbx + 0x108]
003C9715  48 3B 41 70                     cmp rax, qword ptr [rcx + 0x70]
003C9719  7E 2A                           jle 0x1403c9745
003C971B  48 89 41 70                     mov qword ptr [rcx + 0x70], rax
003C971F  F7 05 E7 D3 BF 00 00 00 02 00   test dword ptr [rip + 0xbfd3e7], 0x20000
003C9729  74 1A                           je 0x1403c9745
003C972B  48 8B 43 60                     mov rax, qword ptr [rbx + 0x60]
003C972F  48 8B 8B F8 00 00 00            mov rcx, qword ptr [rbx + 0xf8]
003C9736  48 83 E0 F0                     and rax, 0xfffffffffffffff0
003C973A  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
003C973E  48 89 81 80 00 00 00            mov qword ptr [rcx + 0x80], rax
003C9745  44 8B 7D DB                     mov r15d, dword ptr [rbp - 0x25]
003C9749  8B 8B 98 00 00 00               mov ecx, dword ptr [rbx + 0x98]
003C974F  0F BA E1 09                     bt ecx, 9
003C9753  8B 43 70                        mov eax, dword ptr [rbx + 0x70]
003C9756  89 83 C8 00 00 00               mov dword ptr [rbx + 0xc8], eax
003C975C  73 3E                           jae 0x1403c979c
003C975E  83 F8 40                        cmp eax, 0x40
003C9761  72 39                           jb 0x1403c979c
003C9763  0F BA E1 18                     bt ecx, 0x18
003C9767  73 2A                           jae 0x1403c9793
003C9769  48 8B 93 F8 00 00 00            mov rdx, qword ptr [rbx + 0xf8]
003C9770  8B 4A 68                        mov ecx, dword ptr [rdx + 0x68]
003C9773  85 C9                           test ecx, ecx
003C9775  74 1C                           je 0x1403c9793
003C9777  3B C1                           cmp eax, ecx
003C9779  76 05                           jbe 0x1403c9780
003C977B  41 8B CC                        mov ecx, r12d
003C977E  EB 02                           jmp 0x1403c9782
003C9780  2B C8                           sub ecx, eax
003C9782  B8 68 00 00 00                  mov eax, 0x68
003C9787  89 0C 10                        mov dword ptr [rax + rdx], ecx
003C978A  44 01 05 83 C3 A9 00            add dword ptr [rip + 0xa9c383], r8d
003C9791  EB 09                           jmp 0x1403c979c
003C9793  C1 E8 03                        shr eax, 3
003C9796  89 83 C8 00 00 00               mov dword ptr [rbx + 0xc8], eax
003C979C  44 38 65 D7                     cmp byte ptr [rbp - 0x29], r12b
003C97A0  0F 85 82 00 00 00               jne 0x1403c9828
003C97A6  8B 83 C8 00 00 00               mov eax, dword ptr [rbx + 0xc8]
003C97AC  41 3B C7                        cmp eax, r15d
003C97AF  72 70                           jb 0x1403c9821
003C97B1  0F BA A3 98 00 00 00 09         bt dword ptr [rbx + 0x98], 9
003C97B9  72 55                           jb 0x1403c9810
003C97BB  48 39 5D 0F                     cmp qword ptr [rbp + 0xf], rbx
003C97BF  75 0A                           jne 0x1403c97cb
003C97C1  8B 83 14 01 00 00               mov eax, dword ptr [rbx + 0x114]
003C97C7  A8 0F                           test al, 0xf
003C97C9  74 45                           je 0x1403c9810
003C97CB  48 8B 06                        mov rax, qword ptr [rsi]
003C97CE  48 39 70 08                     cmp qword ptr [rax + 8], rsi
003C97D2  0F 85 2B 02 00 00               jne 0x1403c9a03
003C97D8  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
003C97DC  48 39 31                        cmp qword ptr [rcx], rsi
003C97DF  0F 85 1E 02 00 00               jne 0x1403c9a03
003C97E5  48 89 01                        mov qword ptr [rcx], rax
003C97E8  48 89 48 08                     mov qword ptr [rax + 8], rcx
003C97EC  48 8D 83 88 00 00 00            lea rax, [rbx + 0x88]
003C97F3  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
003C97F7  48 39 01                        cmp qword ptr [rcx], rax
003C97FA  0F 85 03 02 00 00               jne 0x1403c9a03
003C9800  48 89 06                        mov qword ptr [rsi], rax
003C9803  48 89 4E 08                     mov qword ptr [rsi + 8], rcx
003C9807  48 89 31                        mov qword ptr [rcx], rsi
003C980A  48 89 70 08                     mov qword ptr [rax + 8], rsi
003C980E  EB 04                           jmp 0x1403c9814
003C9810  44 88 45 67                     mov byte ptr [rbp + 0x67], r8b
003C9814  45 8B FC                        mov r15d, r12d
003C9817  44 89 65 DB                     mov dword ptr [rbp - 0x25], r12d
003C981B  44 88 45 D7                     mov byte ptr [rbp - 0x29], r8b
003C981F  EB 07                           jmp 0x1403c9828
003C9821  44 2B F8                        sub r15d, eax
003C9824  44 89 7D DB                     mov dword ptr [rbp - 0x25], r15d
003C9828  83 8B 98 00 00 00 20            or dword ptr [rbx + 0x98], 0x20
003C982F  48 8D 4D EF                     lea rcx, [rbp - 0x11]
003C9833  44 01 43 70                     add dword ptr [rbx + 0x70], r8d
003C9837  E8 A4 94 F7 FF                  call 0x140342ce0
003C983C  4C 8D 4D 07                     lea r9, [rbp + 7]
003C9840  4D 8B C5                        mov r8, r13
003C9843  33 D2                           xor edx, edx
003C9845  48 8B CF                        mov rcx, rdi
003C9848  E8 BF D8 F8 FF                  call 0x14035710c
003C984D  48 8D 55 EF                     lea rdx, [rbp - 0x11]
003C9851  48 8D 8F 00 03 00 00            lea rcx, [rdi + 0x300]
003C9858  85 C0                           test eax, eax
003C985A  0F 88 35 01 00 00               js 0x1403c9995
003C9860  4C 8B 75 07                     mov r14, qword ptr [rbp + 7]
003C9864  41 C7 86 80 00 00 00 02 00 00 00  mov dword ptr [r14 + 0x80], 2
003C986F  49 89 5E 10                     mov qword ptr [r14 + 0x10], rbx
003C9873  E8 28 BF EA FF                  call 0x1402757a0
003C9878  8B 4B 70                        mov ecx, dword ptr [rbx + 0x70]
003C987B  FF C9                           dec ecx
003C987D  F7 83 98 00 00 00 00 00 01 00   test dword ptr [rbx + 0x98], 0x10000
003C9887  89 4B 70                        mov dword ptr [rbx + 0x70], ecx
003C988A  74 14                           je 0x1403c98a0
003C988C  49 8B C6                        mov rax, r14
003C988F  49 8D 55 48                     lea rdx, [r13 + 0x48]
003C9893  48 83 C8 01                     or rax, 1
003C9897  48 89 83 F8 01 00 00            mov qword ptr [rbx + 0x1f8], rax
003C989E  EB 19                           jmp 0x1403c98b9
003C98A0  44 39 63 04                     cmp dword ptr [rbx + 4], r12d
003C98A4  75 08                           jne 0x1403c98ae
003C98A6  49 8D 55 78                     lea rdx, [r13 + 0x78]
003C98AA  85 C9                           test ecx, ecx
003C98AC  74 04                           je 0x1403c98b2
003C98AE  49 8D 55 68                     lea rdx, [r13 + 0x68]
003C98B2  4C 89 B3 F8 01 00 00            mov qword ptr [rbx + 0x1f8], r14
003C98B9  49 8B CE                        mov rcx, r14
003C98BC  E8 47 CF F8 FF                  call 0x140356808
003C98C1  44 8B 75 7F                     mov r14d, dword ptr [rbp + 0x7f]
003C98C5  C6 45 D8 01                     mov byte ptr [rbp - 0x28], 1
003C98C9  EB 66                           jmp 0x1403c9931
003C98CB  8B 8B 98 00 00 00               mov ecx, dword ptr [rbx + 0x98]
003C98D1  8B C1                           mov eax, ecx
003C98D3  25 20 00 01 00                  and eax, 0x10020
003C98D8  3D 20 00 01 00                  cmp eax, 0x10020
003C98DD  75 0A                           jne 0x1403c98e9
003C98DF  48 8B CB                        mov rcx, rbx
003C98E2  E8 C5 1F 1B 00                  call 0x14057b8ac
003C98E7  EB 48                           jmp 0x1403c9931
003C98E9  BA 01 00 00 00                  mov edx, 1
003C98EE  44 03 E2                        add r12d, edx
003C98F1  41 83 FC 14                     cmp r12d, 0x14
003C98F5  72 3A                           jb 0x1403c9931
003C98F7  F7 C1 20 08 00 00               test ecx, 0x820
003C98FD  75 32                           jne 0x1403c9931
003C98FF  01 53 70                        add dword ptr [rbx + 0x70], edx
003C9902  83 C9 20                        or ecx, 0x20
003C9905  89 8B 98 00 00 00               mov dword ptr [rbx + 0x98], ecx
003C990B  48 8D 4D EF                     lea rcx, [rbp - 0x11]
003C990F  E8 CC 93 F7 FF                  call 0x140342ce0
003C9914  48 8D 55 EF                     lea rdx, [rbp - 0x11]
003C9918  45 33 E4                        xor r12d, r12d
003C991B  48 8D 8F 00 03 00 00            lea rcx, [rdi + 0x300]
003C9922  E8 79 BE EA FF                  call 0x1402757a0
003C9927  83 A3 98 00 00 00 DF            and dword ptr [rbx + 0x98], 0xffffffdf
003C992E  FF 4B 70                        dec dword ptr [rbx + 0x70]
003C9931  80 7D 67 00                     cmp byte ptr [rbp + 0x67], 0
003C9935  48 8B 83 88 00 00 00            mov rax, qword ptr [rbx + 0x88]
003C993C  74 47                           je 0x1403c9985
003C993E  48 8B 0E                        mov rcx, qword ptr [rsi]
003C9941  48 39 71 08                     cmp qword ptr [rcx + 8], rsi
003C9945  0F 85 B8 00 00 00               jne 0x1403c9a03
003C994B  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
003C994F  48 39 32                        cmp qword ptr [rdx], rsi
003C9952  0F 85 AB 00 00 00               jne 0x1403c9a03
003C9958  48 89 0A                        mov qword ptr [rdx], rcx
003C995B  48 81 C3 88 00 00 00            add rbx, 0x88
003C9962  48 89 51 08                     mov qword ptr [rcx + 8], rdx
003C9966  48 8B 0B                        mov rcx, qword ptr [rbx]
003C9969  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
003C996D  0F 85 90 00 00 00               jne 0x1403c9a03
003C9973  48 89 0E                        mov qword ptr [rsi], rcx
003C9976  48 89 5E 08                     mov qword ptr [rsi + 8], rbx
003C997A  48 89 71 08                     mov qword ptr [rcx + 8], rsi
003C997E  48 89 33                        mov qword ptr [rbx], rsi
003C9981  C6 45 67 00                     mov byte ptr [rbp + 0x67], 0
003C9985  48 8B 4D 0F                     mov rcx, qword ptr [rbp + 0xf]
003C9989  48 8D 98 78 FF FF FF            lea rbx, [rax - 0x88]
003C9990  E9 E3 FC FF FF                  jmp 0x1403c9678
003C9995  E8 06 BE EA FF                  call 0x1402757a0
003C999A  83 A3 98 00 00 00 DF            and dword ptr [rbx + 0x98], 0xffffffdf
003C99A1  BA 01 00 00 00                  mov edx, 1
003C99A6  29 53 70                        sub dword ptr [rbx + 0x70], edx
003C99A9  EB 08                           jmp 0x1403c99b3
003C99AB  BA 01 00 00 00                  mov edx, 1
003C99B0  45 33 E4                        xor r12d, r12d
003C99B3  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
003C99B7  48 8D 45 DF                     lea rax, [rbp - 0x21]
003C99BB  0F B6 5D D8                     movzx ebx, byte ptr [rbp - 0x28]
003C99BF  48 3B C8                        cmp rcx, rax
003C99C2  0F 45 DA                        cmovne ebx, edx
003C99C5  48 8D 45 DF                     lea rax, [rbp - 0x21]
003C99C9  48 3B C8                        cmp rcx, rax
003C99CC  74 3C                           je 0x1403c9a0a
003C99CE  48 8D 45 DF                     lea rax, [rbp - 0x21]
003C99D2  48 39 41 08                     cmp qword ptr [rcx + 8], rax
003C99D6  75 2B                           jne 0x1403c9a03
003C99D8  48 8B 01                        mov rax, qword ptr [rcx]
003C99DB  48 39 48 08                     cmp qword ptr [rax + 8], rcx
003C99DF  75 22                           jne 0x1403c9a03
003C99E1  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
003C99E5  48 8D 55 DF                     lea rdx, [rbp - 0x21]
003C99E9  48 89 50 08                     mov qword ptr [rax + 8], rdx
003C99ED  48 8B 91 98 00 00 00            mov rdx, qword ptr [rcx + 0x98]
003C99F4  48 83 C2 68                     add rdx, 0x68
003C99F8  E8 0B CE F8 FF                  call 0x140356808
003C99FD  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
003C9A01  EB C2                           jmp 0x1403c99c5
003C9A03  B9 03 00 00 00                  mov ecx, 3
003C9A08  CD 29                           int 0x29
003C9A0A  44 38 25 0B B8 BF 00            cmp byte ptr [rip + 0xbfb80b], r12b
003C9A11  49 8B C4                        mov rax, r12
003C9A14  48 89 45 67                     mov qword ptr [rbp + 0x67], rax
003C9A18  75 26                           jne 0x1403c9a40
003C9A1A  84 DB                           test bl, bl
003C9A1C  75 22                           jne 0x1403c9a40
003C9A1E  48 8D 8F 90 04 00 00            lea rcx, [rdi + 0x490]
003C9A25  48 39 09                        cmp qword ptr [rcx], rcx
003C9A28  75 16                           jne 0x1403c9a40
003C9A2A  4C 8D 4D 67                     lea r9, [rbp + 0x67]
003C9A2E  33 D2                           xor edx, edx
003C9A30  4C 8D 45 17                     lea r8, [rbp + 0x17]
003C9A34  48 8B CF                        mov rcx, rdi
003C9A37  E8 38 8B 0D 00                  call 0x1404a2574
003C9A3C  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
003C9A40  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
003C9A4A  48 3B C1                        cmp rax, rcx
003C9A4D  74 1E                           je 0x1403c9a6d
003C9A4F  48 8D 55 67                     lea rdx, [rbp + 0x67]
003C9A53  48 8B CF                        mov rcx, rdi
003C9A56  E8 D9 06 00 00                  call 0x1403ca134
003C9A5B  44 38 A7 0C 03 00 00            cmp byte ptr [rdi + 0x30c], r12b
003C9A62  74 17                           je 0x1403c9a7b
003C9A64  44 88 A7 0C 03 00 00            mov byte ptr [rdi + 0x30c], r12b
003C9A6B  EB 0E                           jmp 0x1403c9a7b
003C9A6D  C6 87 0C 03 00 00 01            mov byte ptr [rdi + 0x30c], 1
003C9A74  44 88 A7 19 04 00 00            mov byte ptr [rdi + 0x419], r12b
003C9A7B  48 8D 4D EF                     lea rcx, [rbp - 0x11]
003C9A7F  E8 5C 92 F7 FF                  call 0x140342ce0
003C9A84  80 7D D9 00                     cmp byte ptr [rbp - 0x27], 0
003C9A88  74 08                           je 0x1403c9a92
003C9A8A  48 8B CF                        mov rcx, rdi
003C9A8D  E8 7A D2 0F 00                  call 0x1404c6d0c
003C9A92  F7 05 74 D0 BF 00 00 00 02 00   test dword ptr [rip + 0xbfd074], 0x20000
003C9A9C  74 0E                           je 0x1403c9aac
003C9A9E  8B 97 D0 03 00 00               mov edx, dword ptr [rdi + 0x3d0]
003C9AA4  41 8B CE                        mov ecx, r14d
003C9AA7  E8 54 89 0E 00                  call 0x1404b2400
003C9AAC  48 8D 87 90 04 00 00            lea rax, [rdi + 0x490]
003C9AB3  48 39 00                        cmp qword ptr [rax], rax
003C9AB6  74 0A                           je 0x1403c9ac2
003C9AB8  33 D2                           xor edx, edx
003C9ABA  48 8B CF                        mov rcx, rdi
003C9ABD  E8 3A F6 F8 FF                  call 0x1403590fc
003C9AC2  48 8B 9C 24 F8 00 00 00         mov rbx, qword ptr [rsp + 0xf8]
003C9ACA  48 81 C4 B0 00 00 00            add rsp, 0xb0
003C9AD1  41 5F                           pop r15
003C9AD3  41 5E                           pop r14
003C9AD5  41 5D                           pop r13
003C9AD7  41 5C                           pop r12
003C9AD9  5F                              pop rdi
003C9ADA  5E                              pop rsi
003C9ADB  5D                              pop rbp
003C9ADC  C3                              ret
003C9ADD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcLazyWriteScan(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned __int8 v_stack_m86;
    unsigned __int8 v_stack_m87;
    unsigned __int8 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (176);
    v_rsi = 0;
    result = 0;
    v_stack_m60 = 0;
    v_stack_m88 = 0;
    v_stack_m48 = 0;
    v_stack_p8 = 0;
    v_stack_m84 = 0;
    v_stack_m86 = 0;
    v_stack_m87 = 0;
    v_stack_m70 = v_xmm0;
    result = *(unsigned __int64 *)(v_rip + 12573380);
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12573380) + 8))) {
        a4 = v_stack_m48;
        a3 = (unsigned int)((unsigned int)(a4));
        a2 = v_stack_m84;
        result = CcScanLogHandleList(a1, a2, a3, a4);
    }
    result = KeAcquireInStackQueuedSpinLock(a1 + 768, v_stack_m70, a3, a4);
    a3 = 0;
    result = CcSetLazyWriteScanQueuedInternal(a1 + 984, (unsigned int)((unsigned int)((unsigned int)(a4))), a3, a4);
    a2 = 0;
    a2 = 0;
    *(unsigned __int64 *)(a1 + 1144) = *(unsigned __int64 *)(a1 + 1112);
    *(unsigned __int64 *)(a1 + 1152) = *(unsigned __int64 *)(a1 + 1120);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1128)))) <= 1) goto loc_003C949A;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 1128)) - 1) * (*(unsigned __int64 *)(a1 + 1112));
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1128)) - 1))) * (*(unsigned __int64 *)(a1 + 1120));
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) + 18688));
    a2 = (a2) + (*(unsigned __int64 *)(a1 + 1056));
    goto loc_003C94A7;
loc_003C949A:
loc_003C94A7:
    *(unsigned __int64 *)(a1 + 1112) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) + 18688);
    *(unsigned __int64 *)(a1 + 1120) = *(unsigned __int64 *)(a1 + 1056);
    if (*(unsigned __int64 *)(a1 + 1056) != 0) goto loc_003C94FC;
    if ((*(unsigned __int8 *)(a1 + 1050)) != 0) goto loc_003C94FC;
    if ((*(unsigned __int64 *)(a1 + 1168)) != (a1 + 1168)) goto loc_003C94E4;
    *(unsigned __int8 *)(a1 + 1049) = 0;
    result = KeReleaseInStackQueuedSpinLock(v_stack_m70, *(unsigned __int64 *)(a1 + 1056), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)), (unsigned int)(*(unsigned int *)(a1 + 1128)));
    goto loc_003C9AC2;
loc_003C94E4:
    a2 = 0;
    result = CcRescheduleLazyWriteScan(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)), (unsigned int)(*(unsigned int *)(a1 + 1128)));
    result = KeReleaseInStackQueuedSpinLock(v_stack_m70, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)), (unsigned int)(*(unsigned int *)(a1 + 1128)));
    goto loc_003C9AB8;
loc_003C94FC:
    v_stack_m78 = v_stack_m80;
    v_stack_m80 = v_stack_m80;
loc_003C9513:
    if ((*(unsigned __int64 *)(a1 + 848)) == (a1 + 848)) goto loc_003C955E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 848) + 8)) != (a1 + 848)) goto loc_003C9A03;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 848)) + 8)) != (*(unsigned __int64 *)(a1 + 848))) goto loc_003C9A03;
    *(unsigned __int64 *)(a1 + 848) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 848));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 848)) + 8) = a1 + 848;
    if ((*(unsigned __int64 *)(v_stack_m78)) != v_stack_m80) goto loc_003C9A03;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 848) + 8) = v_stack_m78;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 848)) = v_stack_m80;
    *(unsigned __int64 *)(v_stack_m78) = *(unsigned __int64 *)(a1 + 848);
    v_stack_m78 = *(unsigned __int64 *)(a1 + 848);
    goto loc_003C9513;
loc_003C955E:
    *(unsigned __int8 *)(a1 + 1050) = 0;
    result = CcCalculatePagesToWrite(a1, (unsigned int)((unsigned int)((unsigned int)(a4))), a1 + 1056, a1 + 1080);
    v_stack_m84 = (unsigned int)(result);
    result = CcAdjustThrottleForPartition(a1, a1 + 1056, a1 + 1080, (unsigned int)(*(unsigned int *)(a1 + 976)));
    *(unsigned __int64 *)(a1 + 1064) = *(unsigned __int64 *)(a1 + 1056);
    *(unsigned int *)(a1 + 1072) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(a1 + 976) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 1136) + (unsigned int)(*(unsigned int *)(a2 + 152)) * 8) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(a2 + 216) = result;
    if (((*(unsigned int *)(v_rip + 12571947)) & (0x20000ULL)) != 0) {
        result = *(unsigned __int64 *)(a1 + 8);
        a1 = *(unsigned int *)(v_rip + 11126171);
        a4 = *(unsigned __int64 *)(a1 + 1056);
        a3 = *(unsigned int *)(a1 + 976);
        a2 = *(unsigned __int64 *)(result);
        result = *(unsigned int *)(a1 + 776);
        v_stack_m90 = result;
        result = *(unsigned __int64 *)(a1 + 1152);
        v_stack_m98 = result;
        result = *(unsigned __int64 *)(a1 + 1144);
        v_stack_mA0 = result;
        result = *(unsigned __int64 *)(a1 + 1096);
        v_stack_mA8 = result;
        result = *(unsigned __int64 *)(a1 + 1088);
        v_stack_mB0 = result;
        result = *(unsigned __int64 *)(a1 + 1080);
        v_stack_mB8 = a1;
        a1 = a3;
        v_stack_mC0 = result;
        result = *(unsigned __int64 *)(a2 + 18688);
        a2 = (unsigned int)((unsigned int)(v_stack_p20));
        v_stack_mC8 = result;
        result = CcPerfLogLazyWriteScan(a1, a2, a3, a4);
    }
    v_rbx = (*(unsigned __int64 *)(a1 + 696)) - (136);
    a1 = 0;
loc_003C9678:
    if (v_rbx == 0) goto loc_003C99AB;
    if ((v_rbx + 136) == (a1 + 696)) goto loc_003C99AB;
    v_stack_mC0 = (unsigned int)((unsigned int)(v_stack_p20));
    result = v_rbx;
    if (0 != 0) { result = 0; }
    v_stack_m50 = result;
    a3 = 0;
    result = (*(unsigned __int64 *)(v_rbx + 96)) & (-16);
    v_stack_mC8 = result;
    result = CcShouldLazyWriteCacheMap(v_rbx, 0, a3, (unsigned int)((unsigned int)((unsigned int)(v_stack_m84))));
    if ((unsigned __int8)(result) == 0) goto loc_003C98CB;
    v_r12 = 0;
    v_stack_m58 = 0;
    result = CcGetNodeForLazyWrite(v_rbx, 0, a3, (unsigned int)((unsigned int)((unsigned int)(v_stack_m84))));
    if (condition_is_above_or_equal) goto loc_003C9749;
    v_stack_m86 = (unsigned __int8)(v_r12 + 1);
    if ((*(unsigned __int64 *)(v_rbx + 264)) <= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 248) + 112))) goto loc_003C9745;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 248) + 112) = *(unsigned __int64 *)(v_rbx + 264);
    result = *(unsigned __int64 *)(v_rbx + 264);
    if (((*(unsigned int *)(v_rip + 12571623)) & (0x20000ULL)) != 0) {
        result = *(unsigned __int64 *)(v_rbx + 96);
        a1 = *(unsigned __int64 *)(v_rbx + 248);
        result = (result) & (-16);
        result = *(unsigned __int64 *)(result + 24);
        *(unsigned __int64 *)(a1 + 128) = result;
    }
loc_003C9749:
    *(unsigned int *)(v_rbx + 200) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 112)));
    if (condition_is_above_or_equal) goto loc_003C979C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 112)))) < 64) goto loc_003C979C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 112)))) >= 64) goto loc_003C9793;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 248) + 104))) == 0) goto loc_003C9793;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 112)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 248) + 104))))) goto loc_003C9780;
    goto loc_003C9782;
loc_003C9780:
    a1 = (unsigned int)((0) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 112)))));
loc_003C9782:
    *(unsigned int *)(104 + *(unsigned __int64 *)(v_rbx + 248) * 1) = (unsigned int)(a1);
    goto loc_003C979C;
loc_003C9793:
    result = (unsigned int)((104) >> (3));
    *(unsigned int *)(v_rbx + 200) = (unsigned int)(result);
loc_003C979C:
    if (v_stack_m88 != 0) goto loc_003C9828;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 200)))) < ((unsigned int)((unsigned int)(v_stack_m84)))) goto loc_003C9821;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 200)))) < ((unsigned int)((unsigned int)(v_stack_m84)))) goto loc_003C9810;
    if (v_stack_m50 != v_rbx) goto loc_003C97CB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 276)))) & (15)) == 0) goto loc_003C9810;
loc_003C97CB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 696) + 8)) != (a1 + 696)) goto loc_003C9A03;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 696 + 8))) != (a1 + 696)) goto loc_003C9A03;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 696 + 8)) = *(unsigned __int64 *)(a1 + 696);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 696) + 8) = *(unsigned __int64 *)(a1 + 696 + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 136 + 8))) != (v_rbx + 136)) goto loc_003C9A03;
    *(unsigned __int64 *)(a1 + 696) = v_rbx + 136;
    *(unsigned __int64 *)(a1 + 696 + 8) = *(unsigned __int64 *)(v_rbx + 136 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 136 + 8)) = a1 + 696;
    *(unsigned __int64 *)(v_rbx + 136 + 8) = a1 + 696;
    goto loc_003C9814;
loc_003C9810:
    v_stack_p8 = (unsigned __int8)(v_r12 + 1);
loc_003C9814:
    v_stack_m84 = 0;
    v_stack_m88 = (unsigned __int8)(v_r12 + 1);
    goto loc_003C9828;
loc_003C9821:
    v_r15 = (unsigned int)((0) - ((unsigned int)(v_rbx + 136)));
    v_stack_m84 = (unsigned int)(v_r15);
loc_003C9828:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m70, *(unsigned __int64 *)(v_rbx + 248), v_r12 + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m84))));
    a2 = 0;
    result = CcAllocateWorkQueueEntry(a1, a2, result, v_stack_m58);
    if (sign_flag) goto loc_003C9995;
    *(unsigned int *)(v_stack_m58 + 128) = 2;
    *(unsigned __int64 *)(v_stack_m58 + 16) = v_rbx;
    result = KeAcquireInStackQueuedSpinLock(a1 + 768, v_stack_m70, result, v_stack_m58);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 112))) - 1);
    *(unsigned int *)(v_rbx + 112) = (unsigned int)(a1);
    if (((*(unsigned int *)(v_rbx + 152)) & (0x10000ULL)) == 0) goto loc_003C98A0;
    result = (v_stack_m58) | (1);
    *(unsigned __int64 *)(v_rbx + 504) = result;
    goto loc_003C98B9;
loc_003C98A0:
    if ((*(unsigned int *)(v_rbx + 4)) != 0) goto loc_003C98AE;
    if ((unsigned int)(a1) != 0) {
        a2 = result + 104;
    }
    *(unsigned __int64 *)(v_rbx + 504) = v_stack_m58;
loc_003C98B9:
    result = CcPostWorkQueue(v_stack_m58, a2, result, v_stack_m58);
    v_stack_m87 = 1;
    goto loc_003C9931;
loc_003C98CB:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 152))))) & (0x10020ULL));
    if (((unsigned int)(result)) != 0x10020ULL) goto loc_003C98E9;
    result = CcIncrementWriteBehindPriority(v_rbx, a2, result, v_stack_m58);
    goto loc_003C9931;
loc_003C98E9:
    v_r12 = (unsigned int)((v_r12) + (1));
    if (((unsigned int)(v_r12)) < 20) goto loc_003C9931;
    if ((((unsigned int)(v_rbx)) & (0x820ULL)) == 0) {
        a1 = (unsigned int)((v_rbx) | (32));
        *(unsigned int *)(v_rbx + 152) = (unsigned int)(a1);
        a1 = v_stack_m70;
        result = KeReleaseInStackQueuedSpinLock(a1, 1, result, v_stack_m58);
        a2 = v_stack_m70;
        v_r12 = 0;
        a1 = a1 + 768;
        result = KeAcquireInStackQueuedSpinLock(a1, a2, result, v_stack_m58);
    }
    if (v_stack_p8 == 0) goto loc_003C9985;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 696) + 8)) != (a1 + 696)) goto loc_003C9A03;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 696 + 8))) != (a1 + 696)) goto loc_003C9A03;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 696 + 8)) = *(unsigned __int64 *)(a1 + 696);
    v_rbx = (v_rbx) + (136);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 696) + 8) = *(unsigned __int64 *)(a1 + 696 + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx) + 8)) != v_rbx) goto loc_003C9A03;
    *(unsigned __int64 *)(a1 + 696) = *(unsigned __int64 *)(v_rbx);
    *(unsigned __int64 *)(a1 + 696 + 8) = v_rbx;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx) + 8) = a1 + 696;
    *(unsigned __int64 *)(v_rbx) = a1 + 696;
    v_stack_p8 = 0;
loc_003C9985:
    goto loc_003C9678;
loc_003C9995:
    result = KeAcquireInStackQueuedSpinLock(v_stack_m50, *(unsigned __int64 *)(a1 + 696 + 8), result, v_stack_m58);
    goto loc_003C99B3;
loc_003C99AB:
    v_r12 = 0;
loc_003C99B3:
    v_rbx = v_stack_m87;
    if (v_stack_m80 != v_stack_m80) { v_rbx = 1; }
loc_003C99C5:
    if (v_stack_m80 == v_stack_m80) goto loc_003C9A0A;
    if ((*(unsigned __int64 *)(v_stack_m80 + 8)) != v_stack_m80) goto loc_003C9A03;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80) + 8)) != v_stack_m80) goto loc_003C9A03;
    v_stack_m80 = *(unsigned __int64 *)(v_stack_m80);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80) + 8) = v_stack_m80;
    a2 = (*(unsigned __int64 *)(v_stack_m80 + 152)) + (104);
    result = CcPostWorkQueue(v_stack_m80, a2, result, v_stack_m58);
    goto loc_003C99C5;
loc_003C9A03:
loc_003C9A0A:
    v_stack_p8 = 0;
    if ((*(unsigned __int8 *)(v_rip + 12564491)) != 0) goto loc_003C9A40;
    if ((unsigned __int8)(v_rbx) != 0) goto loc_003C9A40;
    result = 0;
    if ((*(unsigned __int64 *)(a1 + 1168)) == (a1 + 1168)) {
        a4 = v_stack_p8;
        a2 = 0;
        a3 = v_stack_m48;
        a1 = a1;
        result = CcComputeNextScanTime(a1, a2, a3, a4);
        result = v_stack_p8;
    }
    if (result == a1) goto loc_003C9A6D;
    result = CcRescheduleLazyWriteScan(a1, v_stack_p8, a3, a4);
    if ((*(unsigned __int8 *)(a1 + 780)) == 0) goto loc_003C9A7B;
    *(unsigned __int8 *)(a1 + 780) = 0;
    goto loc_003C9A7B;
loc_003C9A6D:
    *(unsigned __int8 *)(a1 + 780) = 1;
    *(unsigned __int8 *)(a1 + 1049) = 0;
loc_003C9A7B:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m70, v_stack_p8, a3, a4);
    if (v_stack_m86 != 0) {
        a1 = a1;
        result = CcUpdateTimeOnLogHandles(a1, v_stack_p8, a3, a4);
    }
    if (((*(unsigned int *)(v_rip + 12570740)) & (0x20000ULL)) != 0) {
        a2 = *(unsigned int *)(a1 + 976);
        a1 = (unsigned int)((unsigned int)(v_stack_p20));
        result = CcPerfLogLoggedStreamsStats(a1, a2, a3, a4);
    }
    result = a1 + 1168;
    if ((*(unsigned __int64 *)(a1 + 1168)) != (a1 + 1168)) {
        a2 = 0;
        a1 = a1;
        result = CcPostDeferredWrites(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (176);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcLazyWriteScan(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint8_t v_stack_m86;
    uint8_t v_stack_m87;
    uint8_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (176);
    local_rsi = 0;
    result = 0;
    v_stack_m60 = 0;
    v_stack_m88 = 0;
    v_stack_m48 = 0;
    v_stack_p8 = 0;
    v_stack_m84 = 0;
    v_stack_m86 = 0;
    v_stack_m87 = 0;
    v_stack_m70 = v_xmm0;
    result = *(uint64_t *)(v_rip + 0xBFDAC4);
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBFDAC4) + 0x8))) {
        Arg4 = v_stack_m48;
        Arg3 = (uint32_t)((uint32_t)(Arg4));
        Arg2 = v_stack_m84;
        result = CcScanLogHandleList(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAcquireInStackQueuedSpinLock(Arg1 + 768, v_stack_m70, Arg3, Arg4);
    Arg3 = 0;
    result = CcSetLazyWriteScanQueuedInternal(Arg1 + 984, (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg3, Arg4);
    Arg2 = 0;
    Arg2 = 0;
    *(uint64_t *)(arg1 + 0x478) = *(uint64_t *)(arg1 + 0x458);
    *(uint64_t *)(arg1 + 0x480) = *(uint64_t *)(arg1 + 0x460);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x468)))) <= 1) goto loc_003C949A;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x468)) - 1) * (*(uint64_t *)(arg1 + 0x458));
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x468)) - 1))) * (*(uint64_t *)(arg1 + 0x460));
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) + 0x4900));
    Arg2 = (Arg2) + (*(uint64_t *)(arg1 + 0x420));
    goto loc_003C94A7;
loc_003C949A:
loc_003C94A7:
    *(uint64_t *)(arg1 + 0x458) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) + 0x4900);
    *(uint64_t *)(arg1 + 0x460) = *(uint64_t *)(arg1 + 0x420);
    if (*(uint64_t *)(arg1 + 0x420) != 0) goto loc_003C94FC;
    if ((*(uint8_t *)(arg1 + 0x41A)) != 0) goto loc_003C94FC;
    if ((*(uint64_t *)(arg1 + 0x490)) != (Arg1 + 1168)) goto loc_003C94E4;
    *(uint8_t *)(arg1 + 0x419) = 0;
    result = KeReleaseInStackQueuedSpinLock(v_stack_m70, *(uint64_t *)(arg1 + 0x420), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8)), (uint32_t)(*(uint32_t *)(arg1 + 0x468)));
    goto loc_003C9AC2;
loc_003C94E4:
    Arg2 = 0;
    result = CcRescheduleLazyWriteScan(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8)), (uint32_t)(*(uint32_t *)(arg1 + 0x468)));
    result = KeReleaseInStackQueuedSpinLock(v_stack_m70, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8)), (uint32_t)(*(uint32_t *)(arg1 + 0x468)));
    goto loc_003C9AB8;
loc_003C94FC:
    v_stack_m78 = v_stack_m80;
    v_stack_m80 = v_stack_m80;
loc_003C9513:
    if ((*(uint64_t *)(arg1 + 0x350)) == (Arg1 + 848)) goto loc_003C955E;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x350) + 0x8)) != (Arg1 + 848)) goto loc_003C9A03;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x350)) + 0x8)) != (*(uint64_t *)(arg1 + 0x350))) goto loc_003C9A03;
    *(uint64_t *)(arg1 + 0x350) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x350));
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x350)) + 0x8) = Arg1 + 848;
    if ((*(uint64_t *)(v_stack_m78)) != v_stack_m80) goto loc_003C9A03;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x350) + 0x8) = v_stack_m78;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x350)) = v_stack_m80;
    *(uint64_t *)(v_stack_m78) = *(uint64_t *)(arg1 + 0x350);
    v_stack_m78 = *(uint64_t *)(arg1 + 0x350);
    goto loc_003C9513;
loc_003C955E:
    *(uint8_t *)(arg1 + 0x41A) = 0;
    result = CcCalculatePagesToWrite(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg1 + 1056, Arg1 + 1080);
    v_stack_m84 = (uint32_t)(result);
    result = CcAdjustThrottleForPartition(Arg1, Arg1 + 1056, Arg1 + 1080, (uint32_t)(*(uint32_t *)(arg1 + 0x3D0)));
    *(uint64_t *)(arg1 + 0x428) = *(uint64_t *)(arg1 + 0x420);
    *(uint32_t *)(arg1 + 0x430) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(arg1 + 0x3D0) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x470) + (uint32_t)(*(uint32_t *)(arg2 + 0x98)) * 8) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(arg2 + 0xD8) = result;
    if (((*(uint32_t *)(v_rip + 0xBFD52B)) & (0x20000ULL)) != 0) {
        result = *(uint64_t *)(arg1 + 0x8);
        Arg1 = *(uint32_t *)(v_rip + 0xA9C59B);
        Arg4 = *(uint64_t *)(arg1 + 0x420);
        Arg3 = *(uint32_t *)(arg1 + 0x3D0);
        Arg2 = *(uint64_t *)(result);
        result = *(uint32_t *)(arg1 + 0x308);
        v_stack_m90 = result;
        result = *(uint64_t *)(arg1 + 0x480);
        v_stack_m98 = result;
        result = *(uint64_t *)(arg1 + 0x478);
        v_stack_mA0 = result;
        result = *(uint64_t *)(arg1 + 0x448);
        v_stack_mA8 = result;
        result = *(uint64_t *)(arg1 + 0x440);
        v_stack_mB0 = result;
        result = *(uint64_t *)(arg1 + 0x438);
        v_stack_mB8 = Arg1;
        Arg1 = Arg3;
        v_stack_mC0 = result;
        result = *(uint64_t *)(arg2 + 0x4900);
        Arg2 = (uint32_t)((uint32_t)(v_stack_p20));
        v_stack_mC8 = result;
        result = CcPerfLogLazyWriteScan(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = (*(uint64_t *)(arg1 + 0x2B8)) - (136);
    Arg1 = 0;
loc_003C9678:
    if (local_rbx == 0) goto loc_003C99AB;
    if ((local_rbx + 136) == (Arg1 + 696)) goto loc_003C99AB;
    v_stack_mC0 = (uint32_t)((uint32_t)(v_stack_p20));
    result = local_rbx;
    if (0 != 0) { result = 0; }
    v_stack_m50 = result;
    Arg3 = 0;
    result = (*(uint64_t *)(local_rbx + 0x60)) & (-16);
    v_stack_mC8 = result;
    result = CcShouldLazyWriteCacheMap(local_rbx, 0, Arg3, (uint32_t)((uint32_t)((uint32_t)(v_stack_m84))));
    if ((uint8_t)(result) == 0) goto loc_003C98CB;
    local_r12 = 0;
    v_stack_m58 = 0;
    result = CcGetNodeForLazyWrite(local_rbx, 0, Arg3, (uint32_t)((uint32_t)((uint32_t)(v_stack_m84))));
    if (condition_is_above_or_equal) goto loc_003C9749;
    v_stack_m86 = (uint8_t)(local_r12 + 1);
    if ((*(uint64_t *)(local_rbx + 0x108)) <= (*(uint64_t *)(*(uint64_t *)(local_rbx + 0xF8) + 0x70))) goto loc_003C9745;
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0xF8) + 0x70) = *(uint64_t *)(local_rbx + 0x108);
    result = *(uint64_t *)(local_rbx + 0x108);
    if (((*(uint32_t *)(v_rip + 0xBFD3E7)) & (0x20000ULL)) != 0) {
        result = *(uint64_t *)(local_rbx + 0x60);
        Arg1 = *(uint64_t *)(local_rbx + 0xF8);
        result = (result) & (-16);
        result = *(uint64_t *)(result + 0x18);
        *(uint64_t *)(arg1 + 0x80) = result;
    }
loc_003C9749:
    *(uint32_t *)(local_rbx + 0xC8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x70)));
    if (condition_is_above_or_equal) goto loc_003C979C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x70)))) < 64) goto loc_003C979C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x70)))) >= 64) goto loc_003C9793;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + 0xF8) + 0x68))) == 0) goto loc_003C9793;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x70)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + 0xF8) + 0x68))))) goto loc_003C9780;
    goto loc_003C9782;
loc_003C9780:
    Arg1 = (uint32_t)((0) - ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x70)))));
loc_003C9782:
    *(uint32_t *)(104 + *(uint64_t *)(local_rbx + 0xF8) * 1) = (uint32_t)(Arg1);
    goto loc_003C979C;
loc_003C9793:
    result = (uint32_t)((104) >> (3));
    *(uint32_t *)(local_rbx + 0xC8) = (uint32_t)(result);
loc_003C979C:
    if (v_stack_m88 != 0) goto loc_003C9828;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0xC8)))) < ((uint32_t)((uint32_t)(v_stack_m84)))) goto loc_003C9821;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0xC8)))) < ((uint32_t)((uint32_t)(v_stack_m84)))) goto loc_003C9810;
    if (v_stack_m50 != local_rbx) goto loc_003C97CB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x114)))) & (15)) == 0) goto loc_003C9810;
loc_003C97CB:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x2B8) + 0x8)) != (Arg1 + 696)) goto loc_003C9A03;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x2B8 + 0x8))) != (Arg1 + 696)) goto loc_003C9A03;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x2B8 + 0x8)) = *(uint64_t *)(arg1 + 0x2B8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x2B8) + 0x8) = *(uint64_t *)(arg1 + 0x2B8 + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x88 + 0x8))) != (local_rbx + 136)) goto loc_003C9A03;
    *(uint64_t *)(arg1 + 0x2B8) = local_rbx + 136;
    *(uint64_t *)(arg1 + 0x2B8 + 0x8) = *(uint64_t *)(local_rbx + 0x88 + 0x8);
    *(void **)(*(uint64_t *)(local_rbx + 0x88 + 0x8)) = Arg1 + 696;
    *(void **)(local_rbx + 0x88 + 0x8) = Arg1 + 696;
    goto loc_003C9814;
loc_003C9810:
    v_stack_p8 = (uint8_t)(local_r12 + 1);
loc_003C9814:
    v_stack_m84 = 0;
    v_stack_m88 = (uint8_t)(local_r12 + 1);
    goto loc_003C9828;
loc_003C9821:
    local_r15 = (uint32_t)((0) - ((uint32_t)(local_rbx + 136)));
    v_stack_m84 = (uint32_t)(local_r15);
loc_003C9828:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m70, *(uint64_t *)(local_rbx + 0xF8), local_r12 + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m84))));
    Arg2 = 0;
    result = CcAllocateWorkQueueEntry(Arg1, Arg2, result, v_stack_m58);
    if (sign_flag) goto loc_003C9995;
    *(uint32_t *)(v_stack_m58 + 0x80) = 2;
    *(uint64_t *)(v_stack_m58 + 0x10) = local_rbx;
    result = KeAcquireInStackQueuedSpinLock(Arg1 + 768, v_stack_m70, result, v_stack_m58);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x70))) - 1);
    *(uint32_t *)(local_rbx + 0x70) = (uint32_t)(Arg1);
    if (((*(uint32_t *)(local_rbx + 0x98)) & (0x10000ULL)) == 0) goto loc_003C98A0;
    result = (v_stack_m58) | (1);
    *(uint64_t *)(local_rbx + 0x1F8) = result;
    goto loc_003C98B9;
loc_003C98A0:
    if ((*(uint32_t *)(local_rbx + 0x4)) != 0) goto loc_003C98AE;
    if ((uint32_t)(Arg1) != 0) {
        Arg2 = result + 104;
    }
    *(uint64_t *)(local_rbx + 0x1F8) = v_stack_m58;
loc_003C98B9:
    result = CcPostWorkQueue(v_stack_m58, Arg2, result, v_stack_m58);
    v_stack_m87 = 1;
    goto loc_003C9931;
loc_003C98CB:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x98))))) & (0x10020ULL));
    if (((uint32_t)(result)) != 0x10020ULL) goto loc_003C98E9;
    result = CcIncrementWriteBehindPriority(local_rbx, Arg2, result, v_stack_m58);
    goto loc_003C9931;
loc_003C98E9:
    local_r12 = (uint32_t)((local_r12) + (1));
    if (((uint32_t)(local_r12)) < 20) goto loc_003C9931;
    if ((((uint32_t)(local_rbx)) & (0x820ULL)) == 0) {
        Arg1 = (uint32_t)((local_rbx) | (32));
        *(uint32_t *)(local_rbx + 0x98) = (uint32_t)(Arg1);
        Arg1 = v_stack_m70;
        result = KeReleaseInStackQueuedSpinLock(Arg1, 1, result, v_stack_m58);
        Arg2 = v_stack_m70;
        local_r12 = 0;
        Arg1 = Arg1 + 768;
        result = KeAcquireInStackQueuedSpinLock(Arg1, Arg2, result, v_stack_m58);
    }
    if (v_stack_p8 == 0) goto loc_003C9985;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x2B8) + 0x8)) != (Arg1 + 696)) goto loc_003C9A03;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x2B8 + 0x8))) != (Arg1 + 696)) goto loc_003C9A03;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x2B8 + 0x8)) = *(uint64_t *)(arg1 + 0x2B8);
    local_rbx = (local_rbx) + (136);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x2B8) + 0x8) = *(uint64_t *)(arg1 + 0x2B8 + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx) + 0x8)) != local_rbx) goto loc_003C9A03;
    *(uint64_t *)(arg1 + 0x2B8) = *(uint64_t *)(local_rbx);
    *(uint64_t *)(arg1 + 0x2B8 + 0x8) = local_rbx;
    *(void **)(*(uint64_t *)(local_rbx) + 0x8) = Arg1 + 696;
    *(void **)(local_rbx) = Arg1 + 696;
    v_stack_p8 = 0;
loc_003C9985:
    goto loc_003C9678;
loc_003C9995:
    result = KeAcquireInStackQueuedSpinLock(v_stack_m50, *(uint64_t *)(arg1 + 0x2B8 + 0x8), result, v_stack_m58);
    goto loc_003C99B3;
loc_003C99AB:
    local_r12 = 0;
loc_003C99B3:
    local_rbx = v_stack_m87;
    if (v_stack_m80 != v_stack_m80) { local_rbx = 1; }
loc_003C99C5:
    if (v_stack_m80 == v_stack_m80) goto loc_003C9A0A;
    if ((*(uint64_t *)(v_stack_m80 + 0x8)) != v_stack_m80) goto loc_003C9A03;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m80) + 0x8)) != v_stack_m80) goto loc_003C9A03;
    v_stack_m80 = *(uint64_t *)(v_stack_m80);
    *(uint64_t *)(*(uint64_t *)(v_stack_m80) + 0x8) = v_stack_m80;
    Arg2 = (*(uint64_t *)(v_stack_m80 + 0x98)) + (104);
    result = CcPostWorkQueue(v_stack_m80, Arg2, result, v_stack_m58);
    goto loc_003C99C5;
loc_003C9A03:
loc_003C9A0A:
    v_stack_p8 = 0;
    if ((*(uint8_t *)(v_rip + 0xBFB80B)) != 0) goto loc_003C9A40;
    if ((uint8_t)(local_rbx) != 0) goto loc_003C9A40;
    result = 0;
    if ((*(uint64_t *)(arg1 + 0x490)) == (Arg1 + 1168)) {
        Arg4 = v_stack_p8;
        Arg2 = 0;
        Arg3 = v_stack_m48;
        Arg1 = Arg1;
        result = CcComputeNextScanTime(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_p8;
    }
    if (result == Arg1) goto loc_003C9A6D;
    result = CcRescheduleLazyWriteScan(Arg1, v_stack_p8, Arg3, Arg4);
    if ((*(uint8_t *)(arg1 + 0x30C)) == 0) goto loc_003C9A7B;
    *(uint8_t *)(arg1 + 0x30C) = 0;
    goto loc_003C9A7B;
loc_003C9A6D:
    *(uint8_t *)(arg1 + 0x30C) = 1;
    *(uint8_t *)(arg1 + 0x419) = 0;
loc_003C9A7B:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m70, v_stack_p8, Arg3, Arg4);
    if (v_stack_m86 != 0) {
        Arg1 = Arg1;
        result = CcUpdateTimeOnLogHandles(Arg1, v_stack_p8, Arg3, Arg4);
    }
    if (((*(uint32_t *)(v_rip + 0xBFD074)) & (0x20000ULL)) != 0) {
        Arg2 = *(uint32_t *)(arg1 + 0x3D0);
        Arg1 = (uint32_t)((uint32_t)(v_stack_p20));
        result = CcPerfLogLoggedStreamsStats(Arg1, Arg2, Arg3, Arg4);
    }
    result = Arg1 + 1168;
    if ((*(uint64_t *)(arg1 + 0x490)) != (Arg1 + 1168)) {
        Arg2 = 0;
        Arg1 = Arg1;
        result = CcPostDeferredWrites(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (176);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x2B8` | `64` | `R` |
| `Arg1` | `+ 0x300` | `64` | `R` |
| `Arg1` | `+ 0x308` | `32` | `R` |
| `Arg1` | `+ 0x30C` | `8` | `R` |
| `Arg1` | `+ 0x30C` | `8` | `W` |
| `Arg1` | `+ 0x350` | `64` | `R` |
| `Arg1` | `+ 0x3D0` | `32` | `R` |
| `Arg1` | `+ 0x3D0` | `32` | `W` |
| `Arg1` | `+ 0x3D8` | `64` | `R` |
| `Arg1` | `+ 0x419` | `8` | `W` |
| `Arg1` | `+ 0x41A` | `8` | `R` |
| `Arg1` | `+ 0x41A` | `8` | `W` |
| `Arg1` | `+ 0x420` | `64` | `R` |
| `Arg1` | `+ 0x428` | `64` | `W` |
| `Arg1` | `+ 0x430` | `32` | `W` |
| `Arg1` | `+ 0x438` | `64` | `R` |
| `Arg1` | `+ 0x440` | `64` | `R` |
| `Arg1` | `+ 0x448` | `64` | `R` |
| `Arg1` | `+ 0x458` | `64` | `R` |
| `Arg1` | `+ 0x458` | `64` | `W` |
| `Arg1` | `+ 0x460` | `64` | `R` |
| `Arg1` | `+ 0x460` | `64` | `W` |
| `Arg1` | `+ 0x468` | `32` | `R` |
| `Arg1` | `+ 0x470` | `64` | `R` |
| `Arg1` | `+ 0x478` | `64` | `R` |
| `Arg1` | `+ 0x478` | `64` | `W` |
| `Arg1` | `+ 0x480` | `64` | `R` |
| `Arg1` | `+ 0x480` | `64` | `W` |

추가 오프셋 3개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C9394&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
