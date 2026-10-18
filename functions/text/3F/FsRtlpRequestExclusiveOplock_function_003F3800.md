# FsRtlpRequestExclusiveOplock

- RVA: `0x003F3800`–`0x003F4074` (길이 `2,164` bytes)
- VA: `0x00000001403F3800`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097104`
- 디코드: `513`개 명령, `2,164/2,164` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x003F384F` → [FsRtlpAllocateOplock](../../page/9F/FsRtlpAllocateOplock_function_009F1C74.md) (function, `0x009F1C74`)
- `0x003F3866` → [ExAcquireFastMutexUnsafe](ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x003F38DC` → [FsRtlpOplockDequeueRH](../42/FsRtlpOplockDequeueRH_function_004258FC.md) (function, `0x004258FC`)
- `0x003F3922` → [FsRtlpClearOwner](../26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x003F392D` → [FsRtlpFreeRHOpContext](../4F/FsRtlpFreeRHOpContext_function_004F2394.md) (function, `0x004F2394`)
- `0x003F393C` → [FsRtlpComputeShareableOplockState](../42/FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x003F394F` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x003F397A` → [FsRtlpRemoveAndCompleteWaitingIrp](../42/FsRtlpRemoveAndCompleteWaitingIrp_function_00425FC0.md) (function, `0x00425FC0`)
- `0x003F398E` → [FsRtlpOplockDequeueRH](../42/FsRtlpOplockDequeueRH_function_004258FC.md) (function, `0x004258FC`)
- `0x003F39D4` → [FsRtlpClearOwner](../26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x003F39E5` → [FsRtlpFreeRHOpContext](../4F/FsRtlpFreeRHOpContext_function_004F2394.md) (function, `0x004F2394`)
- `0x003F39F4` → [FsRtlpComputeShareableOplockState](../42/FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x003F3A0E` → [FsRtlpOplockUpperLowerCompatible](../../page/A2/FsRtlpOplockUpperLowerCompatible_function_00A21E04.md) (function, `0x00A21E04`)
- `0x003F3A37` → [MmDoesFileHaveUserWritableReferences](../2B/MmDoesFileHaveUserWritableReferences_function_002BB690.md) (function, `0x002BB690`)
- `0x003F3A7A` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x003F3B1F` → [tlgWriteAgg](../2F/tlgWriteAgg_function_002F0F7C.md) (function, `0x002F0F7C`)
- `0x003F3BA8` → [FsRtlpOplockKeysEqual](FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x003F3BE2` → [FsRtlpRemoveAndCompleteReadOnlyIrp](../4B/FsRtlpRemoveAndCompleteReadOnlyIrp_function_004B495C.md) (function, `0x004B495C`)
- `0x003F3CDF` → [FsRtlpOplockKeysEqual](FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x003F3D03` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x003F3D18` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x003F3D86` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x003F3D99` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x003F3DD0` → [FsRtlpOplockKeysEqual](FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x003F3E4F` → [FsRtlpRemoveAndCompleteRHIrp](../42/FsRtlpRemoveAndCompleteRHIrp_function_00425964.md) (function, `0x00425964`)
- `0x003F3E8F` → [FsRtlpOplockKeysEqual](FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x003F3EF2` → [FsRtlpRemoveAndCompleteReadOnlyIrp](../4B/FsRtlpRemoveAndCompleteReadOnlyIrp_function_004B495C.md) (function, `0x004B495C`)
- `0x003F3F2C` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x003F3F71` → [ObDereferenceObjectDeferDeleteWithTag](../26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x003F3FAC` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x003F3FD1` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x003F3FE8` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x003F3FFE` → [FsRtlpCancelExclusiveIrp](../4F/FsRtlpCancelExclusiveIrp_function_004F96CC.md) (function, `0x004F96CC`)
- `0x003F4016` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x003F4038` → [FsRtlpOplockTryPrepForAckTimeout](../../page/71/FsRtlpOplockTryPrepForAckTimeout_function_007156C0.md) (function, `0x007156C0`)
- `0x003F4049` → [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x003F405B` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [FsRtlpOplockFsctrlInternal](../../page/9F/FsRtlpOplockFsctrlInternal_function_009F1640.md) at `0x009F1964`
- [FsRtlpOplockFsctrlInternal](../../page/9F/FsRtlpOplockFsctrlInternal_function_009F1640.md) at `0x009F1B0E`
- [sub_00B3115E](../../page/B3/Unknown_function_00B3115E.md) at `0x00B311B1`

### Static image references
- `0x003F3813` → RVA `0x00E0A740` (`.data`; read)
- `0x003F3A5C` → RVA `0x00E06C50` (`.data`; read)
- `0x003F3B11` → RVA `0x00045522` (`.rdata`; read)
- `0x003F4005` → RVA `0x00582520` (`FsRtlpExclusiveIrpCancelRoutine`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x003F384F` → [FsRtlpAllocateOplock](../../page/9F/FsRtlpAllocateOplock_function_009F1C74.md) (`.text` → `PAGE`)
  - `0x003F3A0E` → [FsRtlpOplockUpperLowerCompatible](../../page/A2/FsRtlpOplockUpperLowerCompatible_function_00A21E04.md) (`.text` → `PAGE`)
  - `0x003F4038` → [FsRtlpOplockTryPrepForAckTimeout](../../page/71/FsRtlpOplockTryPrepForAckTimeout_function_007156C0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003F3800  40 53                           push rbx
003F3802  56                              push rsi
003F3803  57                              push rdi
003F3804  41 54                           push r12
003F3806  41 55                           push r13
003F3808  41 56                           push r14
003F380A  41 57                           push r15
003F380C  48 81 EC 10 01 00 00            sub rsp, 0x110
003F3813  48 8B 05 26 6F A1 00            mov rax, qword ptr [rip + 0xa16f26]
003F381A  48 33 C4                        xor rax, rsp
003F381D  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
003F3825  44 89 4C 24 48                  mov dword ptr [rsp + 0x48], r9d
003F382A  49 8B F8                        mov rdi, r8
003F382D  4C 8B EA                        mov r13, rdx
003F3830  4C 8B F9                        mov r15, rcx
003F3833  33 C0                           xor eax, eax
003F3835  8B D8                           mov ebx, eax
003F3837  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
003F383B  88 44 24 40                     mov byte ptr [rsp + 0x40], al
003F383F  44 8B F0                        mov r14d, eax
003F3842  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003F3847  48 8B 31                        mov rsi, qword ptr [rcx]
003F384A  48 85 F6                        test rsi, rsi
003F384D  75 0B                           jne 0x1403f385a
003F384F  E8 20 E4 5F 00                  call 0x1409f1c74
003F3854  48 8B F0                        mov rsi, rax
003F3857  49 89 07                        mov qword ptr [r15], rax
003F385A  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
003F385F  48 8B 8E 98 00 00 00            mov rcx, qword ptr [rsi + 0x98]
003F3866  E8 B5 FE FF FF                  call 0x1403f3720
003F386B  41 BF 01 00 00 00               mov r15d, 1
003F3871  F7 86 90 00 00 00 00 00 01 00   test dword ptr [rsi + 0x90], 0x10000
003F387B  0F 84 78 01 00 00               je 0x1403f39f9
003F3881  45 33 D2                        xor r10d, r10d
003F3884  41 80 7D 00 0D                  cmp byte ptr [r13], 0xd
003F3889  0F 85 6D 01 00 00               jne 0x1403f39fc
003F388F  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
003F3894  4D 8B 45 30                     mov r8, qword ptr [r13 + 0x30]
003F3898  41 8A D2                        mov dl, r10b
003F389B  4C 8D 66 78                     lea r12, [rsi + 0x78]
003F389F  49 8B 04 24                     mov rax, qword ptr [r12]
003F38A3  49 3B C4                        cmp rax, r12
003F38A6  74 19                           je 0x1403f38c1
003F38A8  48 8D 48 C8                     lea rcx, [rax - 0x38]
003F38AC  4C 3B 41 18                     cmp r8, qword ptr [rcx + 0x18]
003F38B0  0F 85 A3 00 00 00               jne 0x1403f3959
003F38B6  41 8A D7                        mov dl, r15b
003F38B9  49 89 09                        mov qword ptr [r9], rcx
003F38BC  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
003F38C1  84 D2                           test dl, dl
003F38C3  0F 84 33 01 00 00               je 0x1403f39fc
003F38C9  F7 86 90 00 00 00 00 00 02 00   test dword ptr [rsi + 0x90], 0x20000
003F38D3  0F 84 88 00 00 00               je 0x1403f3961
003F38D9  49 8B CE                        mov rcx, r14
003F38DC  E8 1B 20 03 00                  call 0x1404258fc
003F38E1  4D 8D 4E 38                     lea r9, [r14 + 0x38]
003F38E5  49 8B 09                        mov rcx, qword ptr [r9]
003F38E8  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
003F38EC  4C 39 49 08                     cmp qword ptr [rcx + 8], r9
003F38F0  0F 85 33 02 00 00               jne 0x1403f3b29
003F38F6  4C 39 08                        cmp qword ptr [rax], r9
003F38F9  0F 85 2A 02 00 00               jne 0x1403f3b29
003F38FF  48 89 08                        mov qword ptr [rax], rcx
003F3902  48 89 41 08                     mov qword ptr [rcx + 8], rax
003F3906  4D 39 24 24                     cmp qword ptr [r12], r12
003F390A  75 0A                           jne 0x1403f3916
003F390C  81 A6 90 00 00 00 FF FF FC FF   and dword ptr [rsi + 0x90], 0xfffcffff
003F3916  4D 39 56 28                     cmp qword ptr [r14 + 0x28], r10
003F391A  74 0B                           je 0x1403f3927
003F391C  49 8B D6                        mov rdx, r14
003F391F  48 8B CE                        mov rcx, rsi
003F3922  E8 C1 22 E7 FF                  call 0x140265be8
003F3927  41 8A D7                        mov dl, r15b
003F392A  49 8B CE                        mov rcx, r14
003F392D  E8 62 EA 0F 00                  call 0x1404f2394
003F3932  33 C0                           xor eax, eax
003F3934  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003F3939  48 8B CE                        mov rcx, rsi
003F393C  E8 AB 1D 03 00                  call 0x1404256ec
003F3941  BB E2 00 00 C0                  mov ebx, 0xc00000e2
003F3946  41 8A D7                        mov dl, r15b
003F3949  89 5F 30                        mov dword ptr [rdi + 0x30], ebx
003F394C  48 8B CF                        mov rcx, rdi
003F394F  E8 6C 7C EA FF                  call 0x14029b5c0
003F3954  E9 E9 06 00 00                  jmp 0x1403f4042
003F3959  48 8B 00                        mov rax, qword ptr [rax]
003F395C  E9 42 FF FF FF                  jmp 0x1403f38a3
003F3961  48 8D 46 58                     lea rax, [rsi + 0x58]
003F3965  4C 8B 38                        mov r15, qword ptr [rax]
003F3968  4C 3B F8                        cmp r15, rax
003F396B  74 1E                           je 0x1403f398b
003F396D  49 8B CF                        mov rcx, r15
003F3970  45 38 57 35                     cmp byte ptr [r15 + 0x35], r10b
003F3974  75 10                           jne 0x1403f3986
003F3976  4D 8B 7F 08                     mov r15, qword ptr [r15 + 8]
003F397A  E8 41 26 03 00                  call 0x140425fc0
003F397F  48 8D 46 58                     lea rax, [rsi + 0x58]
003F3983  45 33 D2                        xor r10d, r10d
003F3986  4D 8B 3F                        mov r15, qword ptr [r15]
003F3989  EB DD                           jmp 0x1403f3968
003F398B  49 8B CE                        mov rcx, r14
003F398E  E8 69 1F 03 00                  call 0x1404258fc
003F3993  4D 8D 4E 38                     lea r9, [r14 + 0x38]
003F3997  49 8B 09                        mov rcx, qword ptr [r9]
003F399A  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
003F399E  4C 39 49 08                     cmp qword ptr [rcx + 8], r9
003F39A2  0F 85 81 01 00 00               jne 0x1403f3b29
003F39A8  4C 39 08                        cmp qword ptr [rax], r9
003F39AB  0F 85 78 01 00 00               jne 0x1403f3b29
003F39B1  48 89 08                        mov qword ptr [rax], rcx
003F39B4  48 89 41 08                     mov qword ptr [rcx + 8], rax
003F39B8  4D 39 24 24                     cmp qword ptr [r12], r12
003F39BC  75 0A                           jne 0x1403f39c8
003F39BE  81 A6 90 00 00 00 FF FF FC FF   and dword ptr [rsi + 0x90], 0xfffcffff
003F39C8  4D 39 56 28                     cmp qword ptr [r14 + 0x28], r10
003F39CC  74 0B                           je 0x1403f39d9
003F39CE  49 8B D6                        mov rdx, r14
003F39D1  48 8B CE                        mov rcx, rsi
003F39D4  E8 0F 22 E7 FF                  call 0x140265be8
003F39D9  41 BF 01 00 00 00               mov r15d, 1
003F39DF  41 8A D7                        mov dl, r15b
003F39E2  49 8B CE                        mov rcx, r14
003F39E5  E8 AA E9 0F 00                  call 0x1404f2394
003F39EA  33 C0                           xor eax, eax
003F39EC  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003F39F1  48 8B CE                        mov rcx, rsi
003F39F4  E8 F3 1C 03 00                  call 0x1404256ec
003F39F9  45 33 D2                        xor r10d, r10d
003F39FC  8B 94 24 80 01 00 00            mov edx, dword ptr [rsp + 0x180]
003F3A03  44 8B B4 24 78 01 00 00         mov r14d, dword ptr [rsp + 0x178]
003F3A0B  41 8B CE                        mov ecx, r14d
003F3A0E  E8 F1 E3 62 00                  call 0x140a21e04
003F3A13  84 C0                           test al, al
003F3A15  0F 84 26 FF FF FF               je 0x1403f3941
003F3A1B  41 0F BA E6 0C                  bt r14d, 0xc
003F3A20  0F 83 0A 01 00 00               jae 0x1403f3b30
003F3A26  49 8B 45 30                     mov rax, qword ptr [r13 + 0x30]
003F3A2A  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
003F3A2E  48 85 C9                        test rcx, rcx
003F3A31  0F 84 F9 00 00 00               je 0x1403f3b30
003F3A37  E8 54 7C EC FF                  call 0x1402bb690
003F3A3C  45 33 D2                        xor r10d, r10d
003F3A3F  85 C0                           test eax, eax
003F3A41  0F 84 E9 00 00 00               je 0x1403f3b30
003F3A47  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
003F3A4B  44 89 51 08                     mov dword ptr [rcx + 8], r10d
003F3A4F  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
003F3A52  45 8D 42 04                     lea r8d, [r10 + 4]
003F3A56  41 0B C0                        or eax, r8d
003F3A59  89 41 0C                        mov dword ptr [rcx + 0xc], eax
003F3A5C  83 3D ED 31 A1 00 05            cmp dword ptr [rip + 0xa131ed], 5
003F3A63  0F 86 D8 FE FF FF               jbe 0x1403f3941
003F3A69  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
003F3A73  48 8D 0D D6 31 A1 00            lea rcx, [rip + 0xa131d6]
003F3A7A  E8 21 B0 03 00                  call 0x14042eaa0
003F3A7F  84 C0                           test al, al
003F3A81  0F 84 BA FE FF FF               je 0x1403f3941
003F3A87  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
003F3A8C  48 8D 44 24 70                  lea rax, [rsp + 0x70]
003F3A91  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
003F3A99  48 C7 84 24 C8 00 00 00 08 00 00 00  mov qword ptr [rsp + 0xc8], 8
003F3AA5  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
003F3AAA  48 8D 44 24 50                  lea rax, [rsp + 0x50]
003F3AAF  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
003F3AB7  4C 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r8
003F3ABF  8B 86 90 00 00 00               mov eax, dword ptr [rsi + 0x90]
003F3AC5  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
003F3AC9  48 8D 44 24 48                  lea rax, [rsp + 0x48]
003F3ACE  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
003F3AD6  4C 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r8
003F3ADE  48 C7 44 24 68 00 00 00 01      mov qword ptr [rsp + 0x68], 0x1000000
003F3AE7  48 8D 44 24 68                  lea rax, [rsp + 0x68]
003F3AEC  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
003F3AF4  48 C7 84 24 F8 00 00 00 08 00 00 00  mov qword ptr [rsp + 0xf8], 8
003F3B00  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
003F3B08  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003F3B0D  45 8D 4A 06                     lea r9d, [r10 + 6]
003F3B11  48 8D 15 0A 1A C5 FF            lea rdx, [rip - 0x3ae5f6]
003F3B18  48 8D 0D 31 31 A1 00            lea rcx, [rip + 0xa13131]
003F3B1F  E8 58 D4 EF FF                  call 0x1402f0f7c
003F3B24  E9 18 FE FF FF                  jmp 0x1403f3941
003F3B29  B9 03 00 00 00                  mov ecx, 3
003F3B2E  CD 29                           int 0x29
003F3B30  B9 C8 00 00 00                  mov ecx, 0xc8
003F3B35  44 3B F1                        cmp r14d, ecx
003F3B38  75 25                           jne 0x1403f3b5f
003F3B3A  48 89 3E                        mov qword ptr [rsi], rdi
003F3B3D  49 8B 45 30                     mov rax, qword ptr [r13 + 0x30]
003F3B41  48 89 46 08                     mov qword ptr [rsi + 8], rax
003F3B45  8B 86 90 00 00 00               mov eax, dword ptr [rsi + 0x90]
003F3B4B  83 E0 20                        and eax, 0x20
003F3B4E  0B C1                           or eax, ecx
003F3B50  89 86 90 00 00 00               mov dword ptr [rsi + 0x90], eax
003F3B56  8B 5C 24 50                     mov ebx, dword ptr [rsp + 0x50]
003F3B5A  E9 D9 03 00 00                  jmp 0x1403f3f38
003F3B5F  8B 96 90 00 00 00               mov edx, dword ptr [rsi + 0x90]
003F3B65  41 BC 00 70 00 00               mov r12d, 0x7000
003F3B6B  F6 C2 91                        test dl, 0x91
003F3B6E  0F 84 C9 00 00 00               je 0x1403f3c3d
003F3B74  45 85 F4                        test r12d, r14d
003F3B77  0F 95 C1                        setne cl
003F3B7A  F6 C2 10                        test dl, 0x10
003F3B7D  0F 95 C0                        setne al
003F3B80  84 C8                           test al, cl
003F3B82  74 15                           je 0x1403f3b99
003F3B84  41 0F BA E6 10                  bt r14d, 0x10
003F3B89  0F 83 B2 FD FF FF               jae 0x1403f3941
003F3B8F  BB 09 09 00 C0                  mov ebx, 0xc0000909
003F3B94  E9 A9 04 00 00                  jmp 0x1403f4042
003F3B99  84 D2                           test dl, dl
003F3B9B  79 1B                           jns 0x1403f3bb8
003F3B9D  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
003F3BA1  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
003F3BA5  45 33 C0                        xor r8d, r8d
003F3BA8  E8 03 EB FF FF                  call 0x1403f26b0
003F3BAD  88 44 24 41                     mov byte ptr [rsp + 0x41], al
003F3BB1  45 33 D2                        xor r10d, r10d
003F3BB4  84 C0                           test al, al
003F3BB6  74 CC                           je 0x1403f3b84
003F3BB8  8B 86 90 00 00 00               mov eax, dword ptr [rsi + 0x90]
003F3BBE  25 DF FF F0 01                  and eax, 0x1f0ffdf
003F3BC3  83 F8 10                        cmp eax, 0x10
003F3BC6  74 0E                           je 0x1403f3bd6
003F3BC8  3D 00 10 00 00                  cmp eax, 0x1000
003F3BCD  74 07                           je 0x1403f3bd6
003F3BCF  3D 10 10 00 00                  cmp eax, 0x1010
003F3BD4  75 14                           jne 0x1403f3bea
003F3BD6  4C 8B CE                        mov r9, rsi
003F3BD9  45 33 C0                        xor r8d, r8d
003F3BDC  33 D2                           xor edx, edx
003F3BDE  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
003F3BE2  E8 75 0D 0C 00                  call 0x1404b495c
003F3BE7  45 33 D2                        xor r10d, r10d
003F3BEA  44 39 7C 24 48                  cmp dword ptr [rsp + 0x48], r15d
003F3BEF  76 2C                           jbe 0x1403f3c1d
003F3BF1  44 84 BE 90 00 00 00            test byte ptr [rsi + 0x90], r15b
003F3BF8  0F 95 C1                        setne cl
003F3BFB  44 84 BC 24 70 01 00 00         test byte ptr [rsp + 0x170], r15b
003F3C03  0F 94 C0                        sete al
003F3C06  84 C8                           test al, cl
003F3C08  74 13                           je 0x1403f3c1d
003F3C0A  BB E2 00 00 C0                  mov ebx, 0xc00000e2
003F3C0F  48 85 FF                        test rdi, rdi
003F3C12  0F 84 2A 04 00 00               je 0x1403f4042
003F3C18  E9 29 FD FF FF                  jmp 0x1403f3946
003F3C1D  49 8B 45 30                     mov rax, qword ptr [r13 + 0x30]
003F3C21  44 38 50 49                     cmp byte ptr [rax + 0x49], r10b
003F3C25  74 0B                           je 0x1403f3c32
003F3C27  41 0F BA E6 0D                  bt r14d, 0xd
003F3C2C  0F 82 52 FF FF FF               jb 0x1403f3b84
003F3C32  41 BC 01 00 00 00               mov r12d, 1
003F3C38  E9 0D 03 00 00                  jmp 0x1403f3f4a
003F3C3D  41 85 D4                        test r12d, edx
003F3C40  0F 95 C1                        setne cl
003F3C43  F7 C2 00 0F F0 01               test edx, 0x1f00f00
003F3C49  0F 94 C0                        sete al
003F3C4C  84 C8                           test al, cl
003F3C4E  0F 84 BA 02 00 00               je 0x1403f3f0e
003F3C54  48 8D 46 48                     lea rax, [rsi + 0x48]
003F3C58  48 39 00                        cmp qword ptr [rax], rax
003F3C5B  0F 85 AD 02 00 00               jne 0x1403f3f0e
003F3C61  41 0F BA E6 10                  bt r14d, 0x10
003F3C66  0F 82 23 FF FF FF               jb 0x1403f3b8f
003F3C6C  45 85 F4                        test r12d, r14d
003F3C6F  0F 84 CC FC FF FF               je 0x1403f3941
003F3C75  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
003F3C79  44 38 51 49                     cmp byte ptr [rcx + 0x49], r10b
003F3C7D  74 0B                           je 0x1403f3c8a
003F3C7F  41 0F BA E6 0D                  bt r14d, 0xd
003F3C84  0F 82 B7 FC FF FF               jb 0x1403f3941
003F3C8A  81 E2 DF FF F0 01               and edx, 0x1f0ffdf
003F3C90  81 FA 00 10 00 00               cmp edx, 0x1000
003F3C96  0F 84 C0 01 00 00               je 0x1403f3e5c
003F3C9C  81 FA 00 30 00 00               cmp edx, 0x3000
003F3CA2  0F 84 02 01 00 00               je 0x1403f3daa
003F3CA8  81 FA 40 50 00 00               cmp edx, 0x5040
003F3CAE  74 16                           je 0x1403f3cc6
003F3CB0  B8 40 70 00 00                  mov eax, 0x7040
003F3CB5  3B D0                           cmp edx, eax
003F3CB7  0F 85 84 FC FF FF               jne 0x1403f3941
003F3CBD  44 3B F0                        cmp r14d, eax
003F3CC0  0F 85 7B FC FF FF               jne 0x1403f3941
003F3CC6  41 8D 86 C0 AF FF FF            lea eax, [r14 - 0x5040]
003F3CCD  A9 FF DF FF FF                  test eax, 0xffffdfff
003F3CD2  0F 85 69 FC FF FF               jne 0x1403f3941
003F3CD8  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
003F3CDC  45 33 C0                        xor r8d, r8d
003F3CDF  E8 CC E9 FF FF                  call 0x1403f26b0
003F3CE4  88 44 24 41                     mov byte ptr [rsp + 0x41], al
003F3CE8  45 33 E4                        xor r12d, r12d
003F3CEB  84 C0                           test al, al
003F3CED  0F 84 4E FC FF FF               je 0x1403f3941
003F3CF3  48 8B 1E                        mov rbx, qword ptr [rsi]
003F3CF6  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
003F3CFB  45 8D 7C 24 07                  lea r15d, [r12 + 7]
003F3D00  41 8B CF                        mov ecx, r15d
003F3D03  E8 78 00 E8 FF                  call 0x140273d80
003F3D08  88 43 45                        mov byte ptr [rbx + 0x45], al
003F3D0B  41 8B C4                        mov eax, r12d
003F3D0E  48 87 43 68                     xchg qword ptr [rbx + 0x68], rax
003F3D12  8A 53 45                        mov dl, byte ptr [rbx + 0x45]
003F3D15  41 8B CF                        mov ecx, r15d
003F3D18  E8 23 E8 E7 FF                  call 0x140272540
003F3D1D  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
003F3D22  44 38 61 44                     cmp byte ptr [rcx + 0x44], r12b
003F3D26  74 0D                           je 0x1403f3d35
003F3D28  4C 89 63 38                     mov qword ptr [rbx + 0x38], r12
003F3D2C  C7 43 30 20 01 00 C0            mov dword ptr [rbx + 0x30], 0xc0000120
003F3D33  EB 48                           jmp 0x1403f3d7d
003F3D35  48 8B 51 18                     mov rdx, qword ptr [rcx + 0x18]
003F3D39  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
003F3D41  0F 57 C0                        xorps xmm0, xmm0
003F3D44  33 C0                           xor eax, eax
003F3D46  0F 11 02                        movups xmmword ptr [rdx], xmm0
003F3D49  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
003F3D4D  C7 02 01 00 18 00               mov dword ptr [rdx], 0x180001
003F3D53  44 8D 40 18                     lea r8d, [rax + 0x18]
003F3D57  8B 86 90 00 00 00               mov eax, dword ptr [rsi + 0x90]
003F3D5D  C1 E8 0C                        shr eax, 0xc
003F3D60  41 23 C7                        and eax, r15d
003F3D63  89 42 04                        mov dword ptr [rdx + 4], eax
003F3D66  41 8B C6                        mov eax, r14d
003F3D69  C1 E8 0C                        shr eax, 0xc
003F3D6C  41 23 C7                        and eax, r15d
003F3D6F  89 42 08                        mov dword ptr [rdx + 8], eax
003F3D72  4C 89 43 38                     mov qword ptr [rbx + 0x38], r8
003F3D76  C7 43 30 15 02 00 00            mov dword ptr [rbx + 0x30], 0x215
003F3D7D  41 BC 01 00 00 00               mov r12d, 1
003F3D83  41 8A D4                        mov dl, r12b
003F3D86  E8 35 78 EA FF                  call 0x14029b5c0
003F3D8B  33 C0                           xor eax, eax
003F3D8D  48 89 06                        mov qword ptr [rsi], rax
003F3D90  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
003F3D94  BA 44 66 6C 74                  mov edx, 0x746c6644
003F3D99  E8 42 3B F0 FF                  call 0x1402f78e0
003F3D9E  45 33 D2                        xor r10d, r10d
003F3DA1  4C 89 56 08                     mov qword ptr [rsi + 8], r10
003F3DA5  E9 A6 01 00 00                  jmp 0x1403f3f50
003F3DAA  B8 40 70 00 00                  mov eax, 0x7040
003F3DAF  44 3B F0                        cmp r14d, eax
003F3DB2  0F 85 89 FB FF FF               jne 0x1403f3941
003F3DB8  48 8B 5E 38                     mov rbx, qword ptr [rsi + 0x38]
003F3DBC  48 8D 46 38                     lea rax, [rsi + 0x38]
003F3DC0  48 3B D8                        cmp rbx, rax
003F3DC3  74 34                           je 0x1403f3df9
003F3DC5  48 8B 53 18                     mov rdx, qword ptr [rbx + 0x18]
003F3DC9  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
003F3DCD  45 33 C0                        xor r8d, r8d
003F3DD0  E8 DB E8 FF FF                  call 0x1403f26b0
003F3DD5  88 44 24 41                     mov byte ptr [rsp + 0x41], al
003F3DD9  45 33 D2                        xor r10d, r10d
003F3DDC  84 C0                           test al, al
003F3DDE  0F 84 5D FB FF FF               je 0x1403f3941
003F3DE4  4C 39 53 38                     cmp qword ptr [rbx + 0x38], r10
003F3DE8  74 0A                           je 0x1403f3df4
003F3DEA  BB E3 00 00 C0                  mov ebx, 0xc00000e3
003F3DEF  E9 52 FB FF FF                  jmp 0x1403f3946
003F3DF4  48 8B 1B                        mov rbx, qword ptr [rbx]
003F3DF7  EB C3                           jmp 0x1403f3dbc
003F3DF9  44 39 7C 24 48                  cmp dword ptr [rsp + 0x48], r15d
003F3DFE  76 0E                           jbe 0x1403f3e0e
003F3E00  44 84 BC 24 70 01 00 00         test byte ptr [rsp + 0x170], r15b
003F3E08  0F 84 33 FB FF FF               je 0x1403f3941
003F3E0E  48 8B 4E 38                     mov rcx, qword ptr [rsi + 0x38]
003F3E12  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
003F3E17  48 8D 46 38                     lea rax, [rsi + 0x38]
003F3E1B  48 3B C8                        cmp rcx, rax
003F3E1E  0F 84 0E FE FF FF               je 0x1403f3c32
003F3E24  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
003F3E28  45 8B CE                        mov r9d, r14d
003F3E2B  45 23 CC                        and r9d, r12d
003F3E2E  44 88 54 24 38                  mov byte ptr [rsp + 0x38], r10b
003F3E33  66 44 89 54 24 30               mov word ptr [rsp + 0x30], r10w
003F3E39  44 89 54 24 28                  mov dword ptr [rsp + 0x28], r10d
003F3E3E  44 89 54 24 20                  mov dword ptr [rsp + 0x20], r10d
003F3E43  41 B8 15 02 00 00               mov r8d, 0x215
003F3E49  48 8B D6                        mov rdx, rsi
003F3E4C  48 8B 0B                        mov rcx, qword ptr [rbx]
003F3E4F  E8 10 1B 03 00                  call 0x140425964
003F3E54  48 8B 0B                        mov rcx, qword ptr [rbx]
003F3E57  45 33 D2                        xor r10d, r10d
003F3E5A  EB B6                           jmp 0x1403f3e12
003F3E5C  41 8D 86 C0 AF FF FF            lea eax, [r14 - 0x5040]
003F3E63  A9 FF DF FF FF                  test eax, 0xffffdfff
003F3E68  0F 85 D3 FA FF FF               jne 0x1403f3941
003F3E6E  4C 8B 7E 28                     mov r15, qword ptr [rsi + 0x28]
003F3E72  48 8D 46 28                     lea rax, [rsi + 0x28]
003F3E76  4C 3B F8                        cmp r15, rax
003F3E79  74 35                           je 0x1403f3eb0
003F3E7B  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
003F3E7F  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
003F3E84  48 8B 50 30                     mov rdx, qword ptr [rax + 0x30]
003F3E88  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
003F3E8C  45 33 C0                        xor r8d, r8d
003F3E8F  E8 1C E8 FF FF                  call 0x1403f26b0
003F3E94  88 44 24 41                     mov byte ptr [rsp + 0x41], al
003F3E98  84 C0                           test al, al
003F3E9A  75 0F                           jne 0x1403f3eab
003F3E9C  BB E2 00 00 C0                  mov ebx, 0xc00000e2
003F3EA1  BA 01 00 00 00                  mov edx, 1
003F3EA6  E9 9E FA FF FF                  jmp 0x1403f3949
003F3EAB  4D 8B 3F                        mov r15, qword ptr [r15]
003F3EAE  EB C2                           jmp 0x1403f3e72
003F3EB0  41 BF 01 00 00 00               mov r15d, 1
003F3EB6  44 39 7C 24 48                  cmp dword ptr [rsp + 0x48], r15d
003F3EBB  76 0E                           jbe 0x1403f3ecb
003F3EBD  44 84 BC 24 70 01 00 00         test byte ptr [rsp + 0x170], r15b
003F3EC5  0F 84 76 FA FF FF               je 0x1403f3941
003F3ECB  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
003F3ECF  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
003F3ED4  48 8D 46 28                     lea rax, [rsi + 0x28]
003F3ED8  48 3B C8                        cmp rcx, rax
003F3EDB  74 1F                           je 0x1403f3efc
003F3EDD  4C 8B 79 08                     mov r15, qword ptr [rcx + 8]
003F3EE1  45 8B C6                        mov r8d, r14d
003F3EE4  45 23 C4                        and r8d, r12d
003F3EE7  4C 8B CE                        mov r9, rsi
003F3EEA  BA 15 02 00 00                  mov edx, 0x215
003F3EEF  49 8B 0F                        mov rcx, qword ptr [r15]
003F3EF2  E8 65 0A 0C 00                  call 0x1404b495c
003F3EF7  49 8B 0F                        mov rcx, qword ptr [r15]
003F3EFA  EB D3                           jmp 0x1403f3ecf
003F3EFC  41 BC 01 00 00 00               mov r12d, 1
003F3F02  41 8A C4                        mov al, r12b
003F3F05  88 44 24 40                     mov byte ptr [rsp + 0x40], al
003F3F09  45 33 D2                        xor r10d, r10d
003F3F0C  EB 34                           jmp 0x1403f3f42
003F3F0E  41 0F BA E6 10                  bt r14d, 0x10
003F3F13  0F 82 76 FC FF FF               jb 0x1403f3b8f
003F3F19  BB E2 00 00 C0                  mov ebx, 0xc00000e2
003F3F1E  48 85 FF                        test rdi, rdi
003F3F21  74 11                           je 0x1403f3f34
003F3F23  89 5F 30                        mov dword ptr [rdi + 0x30], ebx
003F3F26  41 8A D7                        mov dl, r15b
003F3F29  48 8B CF                        mov rcx, rdi
003F3F2C  E8 8F 76 EA FF                  call 0x14029b5c0
003F3F31  45 33 D2                        xor r10d, r10d
003F3F34  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
003F3F38  41 BC 01 00 00 00               mov r12d, 1
003F3F3E  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
003F3F42  84 C0                           test al, al
003F3F44  0F 84 F8 00 00 00               je 0x1403f4042
003F3F4A  41 BF 07 00 00 00               mov r15d, 7
003F3F50  48 89 3E                        mov qword ptr [rsi], rdi
003F3F53  49 8B 45 30                     mov rax, qword ptr [r13 + 0x30]
003F3F57  48 89 46 08                     mov qword ptr [rsi + 8], rax
003F3F5B  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
003F3F5F  4C 89 56 18                     mov qword ptr [rsi + 0x18], r10
003F3F63  4C 89 56 10                     mov qword ptr [rsi + 0x10], r10
003F3F67  48 85 C9                        test rcx, rcx
003F3F6A  74 0A                           je 0x1403f3f76
003F3F6C  BA 44 66 6C 74                  mov edx, 0x746c6644
003F3F71  E8 2A FF E6 FF                  call 0x140263ea0
003F3F76  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003F3F7F  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
003F3F87  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
003F3F8E  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
003F3F92  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
003F3F9B  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
003F3FA3  48 89 4E 18                     mov qword ptr [rsi + 0x18], rcx
003F3FA7  BA 44 66 6C 74                  mov edx, 0x746c6644
003F3FAC  E8 5F C7 E1 FF                  call 0x140210710
003F3FB1  33 DB                           xor ebx, ebx
003F3FB3  88 5E 20                        mov byte ptr [rsi + 0x20], bl
003F3FB6  8B 86 90 00 00 00               mov eax, dword ptr [rsi + 0x90]
003F3FBC  83 E0 20                        and eax, 0x20
003F3FBF  41 0B C6                        or eax, r14d
003F3FC2  89 86 90 00 00 00               mov dword ptr [rsi + 0x90], eax
003F3FC8  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
003F3FCC  BA 44 66 6C 74                  mov edx, 0x746c6644
003F3FD1  E8 3A C7 E1 FF                  call 0x140210710
003F3FD6  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
003F3FDD  44 08 60 03                     or byte ptr [rax + 3], r12b
003F3FE1  48 89 77 38                     mov qword ptr [rdi + 0x38], rsi
003F3FE5  49 8B CF                        mov rcx, r15
003F3FE8  E8 93 FD E7 FF                  call 0x140273d80
003F3FED  88 47 45                        mov byte ptr [rdi + 0x45], al
003F3FF0  38 5F 44                        cmp byte ptr [rdi + 0x44], bl
003F3FF3  74 10                           je 0x1403f4005
003F3FF5  45 8A C4                        mov r8b, r12b
003F3FF8  41 8A D4                        mov dl, r12b
003F3FFB  48 8B CF                        mov rcx, rdi
003F3FFE  E8 C9 56 10 00                  call 0x1404f96cc
003F4003  EB 38                           jmp 0x1403f403d
003F4005  48 8D 05 14 E5 18 00            lea rax, [rip + 0x18e514]
003F400C  48 87 47 68                     xchg qword ptr [rdi + 0x68], rax
003F4010  8A 57 45                        mov dl, byte ptr [rdi + 0x45]
003F4013  49 8B CF                        mov rcx, r15
003F4016  E8 25 E5 E7 FF                  call 0x140272540
003F401B  48 8D 86 B8 00 00 00            lea rax, [rsi + 0xb8]
003F4022  4C 8D 8E A8 00 00 00            lea r9, [rsi + 0xa8]
003F4029  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003F402E  4C 8B C7                        mov r8, rdi
003F4031  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
003F4035  48 8B CE                        mov rcx, rsi
003F4038  E8 83 16 32 00                  call 0x1407156c0
003F403D  BB 03 01 00 00                  mov ebx, 0x103
003F4042  48 8B 8E 98 00 00 00            mov rcx, qword ptr [rsi + 0x98]
003F4049  E8 52 C3 E5 FF                  call 0x1402503a0
003F404E  8B C3                           mov eax, ebx
003F4050  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
003F4058  48 33 CC                        xor rcx, rsp
003F405B  E8 E0 85 2B 00                  call 0x1406ac640
003F4060  48 81 C4 10 01 00 00            add rsp, 0x110
003F4067  41 5F                           pop r15
003F4069  41 5E                           pop r14
003F406B  41 5D                           pop r13
003F406D  41 5C                           pop r12
003F406F  5F                              pop rdi
003F4070  5E                              pop rsi
003F4071  5B                              pop rbx
003F4072  C3                              ret
003F4073  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlpRequestExclusiveOplock(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, unsigned int a6, unsigned int a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int8 v_stack_m107;
    unsigned __int8 v_stack_m108;
    unsigned __int8 v_stack_m110;
    unsigned __int16 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned __int8 v_stack_p28;

    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 10579750)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m100 = a4;
    result = 0;
    v_stack_mF8 = 0;
    v_stack_m108 = 0;
    v_stack_mF0 = 0;
    v_rsi = *(unsigned __int64 *)(a1);
    if (*(unsigned __int64 *)(a1) == 0) {
        result = FsRtlpAllocateOplock(a1, a2, a3, a4);
        v_rsi = result;
        *(unsigned __int64 *)(a1) = result;
    }
    v_stack_mE8 = v_rsi;
    result = ExAcquireFastMutexUnsafe(*(unsigned __int64 *)(v_rsi + 152), a2, a3, a4);
    if (((*(unsigned int *)(v_rsi + 144)) & (0x10000ULL)) == 0) goto loc_003F39F9;
    v_r10 = 0;
    if ((*(unsigned __int8 *)(a2)) != 13) goto loc_003F39FC;
loc_003F38A3:
    if ((*(unsigned __int64 *)(v_rsi + 120)) == (v_rsi + 120)) goto loc_003F38C1;
    if ((*(unsigned __int64 *)(a2 + 48)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 120) - 56 + 24))) goto loc_003F3959;
    *(unsigned __int64 *)(v_stack_mF0) = *(unsigned __int64 *)(v_rsi + 120) - 56;
loc_003F38C1:
    if (1 == 0) goto loc_003F39FC;
    if (((*(unsigned int *)(v_rsi + 144)) & (0x20000ULL)) == 0) goto loc_003F3961;
    result = FsRtlpOplockDequeueRH(v_stack_mF0, 1, *(unsigned __int64 *)(a2 + 48), v_stack_mF0);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 56) + 8)) != (v_stack_mF0 + 56)) goto loc_003F3B29;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 56 + 8))) != (v_stack_mF0 + 56)) goto loc_003F3B29;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 56 + 8)) = *(unsigned __int64 *)(v_stack_mF0 + 56);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 56) + 8) = *(unsigned __int64 *)(v_stack_mF0 + 56 + 8);
    if ((*(unsigned __int64 *)(v_rsi + 120)) == (v_rsi + 120)) {
    }
    result = *(unsigned __int64 *)(v_stack_mF0 + 56 + 8);
    if ((*(unsigned __int64 *)(v_stack_mF0 + 40)) != 0) {
        a2 = v_stack_mF0;
        a1 = v_rsi;
        result = FsRtlpClearOwner(a1, a2, *(unsigned __int64 *)(a2 + 48), v_stack_mF0 + 56);
    }
    result = FsRtlpFreeRHOpContext(v_stack_mF0, 1, *(unsigned __int64 *)(a2 + 48), v_stack_mF0 + 56);
    result = 0;
    v_stack_mF0 = 0;
    result = FsRtlpComputeShareableOplockState(v_rsi, 1, *(unsigned __int64 *)(a2 + 48), v_stack_mF0 + 56);
loc_003F3941:
loc_003F3946:
loc_003F3949:
    *(unsigned int *)(a3 + 48) = (unsigned int)((unsigned int)(0xC00000E2ULL));
    result = IofCompleteRequest(a3, 1, *(unsigned __int64 *)(a2 + 48), v_stack_mF0 + 56);
    goto loc_003F4042;
loc_003F3959:
    goto loc_003F38A3;
loc_003F3961:
loc_003F3968:
    if ((*(unsigned __int64 *)(v_rsi + 88)) == (v_rsi + 88)) goto loc_003F398B;
    result = v_rsi + 88;
    v_r15 = *(unsigned __int64 *)(v_rsi + 88);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rsi + 88) + 53)) == 0) {
        v_r15 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 88) + 8);
        result = FsRtlpRemoveAndCompleteWaitingIrp(*(unsigned __int64 *)(v_rsi + 88), 1, *(unsigned __int64 *)(a2 + 48), v_stack_mF0 + 56);
        result = v_rsi + 88;
        v_r10 = 0;
    }
    goto loc_003F3968;
loc_003F398B:
    result = FsRtlpOplockDequeueRH(v_stack_mF0, 1, *(unsigned __int64 *)(a2 + 48), v_stack_mF0 + 56);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 56) + 8)) != (v_stack_mF0 + 56)) goto loc_003F3B29;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 56 + 8))) != (v_stack_mF0 + 56)) goto loc_003F3B29;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 56 + 8)) = *(unsigned __int64 *)(v_stack_mF0 + 56);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 56) + 8) = *(unsigned __int64 *)(v_stack_mF0 + 56 + 8);
    if ((*(unsigned __int64 *)(v_rsi + 120)) == (v_rsi + 120)) {
    }
    result = *(unsigned __int64 *)(v_stack_mF0 + 56 + 8);
    if ((*(unsigned __int64 *)(v_stack_mF0 + 40)) != 0) {
        a2 = v_stack_mF0;
        a1 = v_rsi;
        result = FsRtlpClearOwner(a1, a2, *(unsigned __int64 *)(a2 + 48), v_stack_mF0 + 56);
    }
    result = FsRtlpFreeRHOpContext(v_stack_mF0, 1, *(unsigned __int64 *)(a2 + 48), v_stack_mF0 + 56);
    result = 0;
    v_stack_mF0 = 0;
    result = FsRtlpComputeShareableOplockState(v_rsi, 1, *(unsigned __int64 *)(a2 + 48), v_stack_mF0 + 56);
loc_003F39F9:
    v_r10 = 0;
loc_003F39FC:
    result = FsRtlpOplockUpperLowerCompatible((unsigned int)((unsigned int)((unsigned int)(a6))), (unsigned int)(a7), *(unsigned __int64 *)(a2 + 48), v_stack_mF0 + 56);
    if ((unsigned __int8)(result) == 0) goto loc_003F3941;
    if (condition_is_above_or_equal) goto loc_003F3B30;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 48) + 40) == 0) goto loc_003F3B30;
    result = MmDoesFileHaveUserWritableReferences(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 48) + 40), (unsigned int)(a7), *(unsigned __int64 *)(a2 + 48), v_stack_mF0 + 56);
    v_r10 = 0;
    if ((unsigned int)(result) == 0) goto loc_003F3B30;
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 8) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 12))) | ((unsigned int)(v_r10 + 4)));
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 12) = (unsigned int)(result);
    if ((*(unsigned int *)(v_rip + 10564077)) <= 5) goto loc_003F3941;
    result = tlgKeywordOn(v_rip + 10564054, (unsigned int)(a7), v_r10 + 4, v_stack_mF0 + 56);
    if ((unsigned __int8)(result) == 0) goto loc_003F3941;
    v_stack_mD8 = 1;
    v_stack_m88 = v_stack_mD8;
    v_stack_m80 = 8;
    v_stack_mF8 = (unsigned int)((unsigned int)(a6));
    v_stack_m78 = v_stack_mF8;
    v_stack_m70 = v_r10 + 4;
    v_stack_m100 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 144)));
    v_stack_m68 = v_stack_m100;
    v_stack_m60 = v_r10 + 4;
    v_stack_mE0 = 0x1000000ULL;
    v_stack_m58 = v_stack_mE0;
    v_stack_m50 = 8;
    v_stack_m128 = v_stack_mA8;
    result = tlgWriteAgg(v_rip + 10563889, v_rip - 3859958, v_r10 + 4, v_r10 + 6);
    goto loc_003F3941;
loc_003F3B29:
loc_003F3B30:
    if (((unsigned int)((unsigned int)(a6))) != 200) goto loc_003F3B5F;
    *(unsigned __int64 *)(v_rsi) = a3;
    *(unsigned __int64 *)(v_rsi + 8) = *(unsigned __int64 *)(a2 + 48);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 144))) & (32));
    result = (unsigned int)((result) | (200));
    *(unsigned int *)(v_rsi + 144) = (unsigned int)(result);
    goto loc_003F3F38;
loc_003F3B5F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 144)))) & (145)) == 0) goto loc_003F3C3D;
    a1 = ((((unsigned int)((unsigned int)(0x7000ULL))) & ((unsigned int)((unsigned int)(a6)))) != 0) ? 1 : 0;
    result = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 144)))) & (16)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_003F3B99;
loc_003F3B84:
    if (condition_is_above_or_equal) goto loc_003F3941;
loc_003F3B8F:
    goto loc_003F4042;
loc_003F3B99:
    if (!sign_flag) goto loc_003F3BB8;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(a2 + 48), *(unsigned __int64 *)(v_rsi + 8), a3, v_r10 + 6);
    v_stack_m107 = (unsigned __int8)(result);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_003F3B84;
loc_003F3BB8:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 144))) & (0x1F0FFDFULL));
    if (((unsigned int)(result)) == 16) goto loc_003F3BD6;
    if (((unsigned int)(result)) == 0x1000ULL) goto loc_003F3BD6;
    if (((unsigned int)(result)) == 0x1010ULL) {
        a4 = v_rsi;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rsi + 40);
        result = FsRtlpRemoveAndCompleteReadOnlyIrp(a1, a2, a3, a4);
        v_r10 = 0;
    }
    if (v_stack_m100 <= 1) goto loc_003F3C1D;
    a1 = (((*(unsigned __int8 *)(v_rsi + 144)) & (1)) != 0) ? 1 : 0;
    result = (((v_stack_p28) & (1)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_003F3C1D;
    if (0 == 0) goto loc_003F4042;
    goto loc_003F3946;
loc_003F3C1D:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 48) + 73)) == 0) goto loc_003F3C32;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 48) + 73)) < 0) goto loc_003F3B84;
loc_003F3C32:
    goto loc_003F3F4A;
loc_003F3C3D:
    a1 = (((1) & (0)) != 0) ? 1 : 0;
    result = (((0) & (0x1F00F00ULL)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_003F3F0E;
    if ((*(unsigned __int64 *)(v_rsi + 72)) != (v_rsi + 72)) goto loc_003F3F0E;
    if ((*(unsigned __int64 *)(v_rsi + 72)) < (v_rsi + 72)) goto loc_003F3B8F;
    if (((1) & ((unsigned int)((unsigned int)(a6)))) == 0) goto loc_003F3941;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 48) + 73)) == 0) goto loc_003F3C8A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 48) + 73)) < 0) goto loc_003F3941;
loc_003F3C8A:
    a2 = (unsigned int)((a2) & (0x1F0FFDFULL));
    if (((unsigned int)(a2)) == 0x1000ULL) goto loc_003F3E5C;
    if (((unsigned int)(a2)) == 0x3000ULL) goto loc_003F3DAA;
    if (((unsigned int)(a2)) == 0x5040ULL) goto loc_003F3CC6;
    if (((unsigned int)(a2)) != ((unsigned int)((unsigned int)(0x7040ULL)))) goto loc_003F3941;
    if (((unsigned int)((unsigned int)(a6))) != ((unsigned int)((unsigned int)(0x7040ULL)))) goto loc_003F3941;
loc_003F3CC6:
    if ((((unsigned int)((unsigned int)(a6) - 20544)) & (0xFFFFDFFFULL)) != 0) goto loc_003F3941;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(a2 + 48), *(unsigned __int64 *)(v_rsi + 8), a3, a4);
    v_stack_m107 = (unsigned __int8)(result);
    v_r12 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_003F3941;
    v_stack_mD0 = *(unsigned __int64 *)(v_rsi);
    result = KeAcquireQueuedSpinLock((unsigned int)((unsigned int)(v_r12 + 7)), *(unsigned __int64 *)(v_rsi + 8), a3, a4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsi) + 69) = (unsigned __int8)(result);
    result = KeReleaseQueuedSpinLock((unsigned int)((unsigned int)(v_r12 + 7)), *(unsigned __int8 *)(*(unsigned __int64 *)(v_rsi) + 69), a3, a4);
    if ((*(unsigned __int8 *)(v_stack_mD0 + 68)) == 0) goto loc_003F3D35;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 56) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi) + 48) = 0xC0000120ULL;
    goto loc_003F3D7D;
loc_003F3D35:
    v_stack_mC8 = *(unsigned __int64 *)(v_stack_mD0 + 24);
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 24)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0 + 24) + 16) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_mD0 + 24)) = 0x180001ULL;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 144))) >> (12));
    result = (unsigned int)((result) & ((unsigned int)(v_r12 + 7)));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_mD0 + 24) + 4) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) >> (12));
    result = (unsigned int)((result) & ((unsigned int)(v_r12 + 7)));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_mD0 + 24) + 8) = (unsigned int)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + 56) = result + 24;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsi) + 48) = 533;
loc_003F3D7D:
    result = IofCompleteRequest(v_stack_mD0, 1, result + 24, a4);
    result = 0;
    *(unsigned __int64 *)(v_rsi) = 0;
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_rsi + 8), (unsigned int)(0x746C6644ULL), result + 24, a4);
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsi + 8) = 0;
    goto loc_003F3F50;
loc_003F3DAA:
    if (((unsigned int)((unsigned int)(a6))) != ((unsigned int)((unsigned int)(0x7040ULL)))) goto loc_003F3941;
loc_003F3DBC:
    if ((*(unsigned __int64 *)(v_rsi + 56)) == (v_rsi + 56)) goto loc_003F3DF9;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(a2 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 56) + 24), a3, a4);
    v_stack_m107 = (unsigned __int8)(result);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_003F3941;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 56) + 56)) == 0) goto loc_003F3DF4;
    goto loc_003F3946;
loc_003F3DF4:
    goto loc_003F3DBC;
loc_003F3DF9:
    if (v_stack_m100 <= ((unsigned int)(v_r12 + 7))) goto loc_003F3E0E;
    if (((v_stack_p28) & ((unsigned __int8)(v_r12 + 7))) == 0) goto loc_003F3941;
loc_003F3E0E:
loc_003F3E12:
    v_stack_m100 = *(unsigned __int64 *)(v_rsi + 56);
    if ((*(unsigned __int64 *)(v_rsi + 56)) == (v_rsi + 56)) goto loc_003F3C32;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (1));
    v_stack_m110 = 0;
    v_stack_m118 = 0;
    v_stack_m120 = 0;
    v_stack_m128 = 0;
    result = FsRtlpRemoveAndCompleteRHIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 56) + 8)), v_rsi, 533, a4);
    v_r10 = 0;
    goto loc_003F3E12;
loc_003F3E5C:
    if ((((unsigned int)((unsigned int)(a6) - 20544)) & (0xFFFFDFFFULL)) != 0) goto loc_003F3941;
loc_003F3E72:
    if ((*(unsigned __int64 *)(v_rsi + 40)) == (v_rsi + 40)) goto loc_003F3EB0;
    v_stack_mE0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 40) + 16);
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(a2 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 40) + 16) + 48), a3, a4);
    v_stack_m107 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) goto loc_003F3EAB;
    goto loc_003F3949;
loc_003F3EAB:
    goto loc_003F3E72;
loc_003F3EB0:
    if (v_stack_m100 <= 1) goto loc_003F3ECB;
    if (((v_stack_p28) & (1)) == 0) goto loc_003F3941;
loc_003F3ECB:
loc_003F3ECF:
    v_stack_m100 = *(unsigned __int64 *)(v_rsi + 40);
    if ((*(unsigned __int64 *)(v_rsi + 40)) == (v_rsi + 40)) goto loc_003F3EFC;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (1));
    result = FsRtlpRemoveAndCompleteReadOnlyIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 40) + 8)), 533, a3, v_rsi);
    goto loc_003F3ECF;
loc_003F3EFC:
    v_stack_m108 = 1;
    v_r10 = 0;
    goto loc_003F3F42;
loc_003F3F0E:
    if (condition_is_below) goto loc_003F3B8F;
    result = 1;
    if (a3 != 0) {
        *(unsigned int *)(a3 + 48) = (unsigned int)((unsigned int)(0xC00000E2ULL));
        a2 = (unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 40) + 8));
        a1 = a3;
        result = IofCompleteRequest(a1, a2, a3, v_rsi);
        v_r10 = 0;
    }
    v_stack_mF8 = (unsigned int)((unsigned int)(0xC00000E2ULL));
loc_003F3F38:
loc_003F3F42:
    if ((unsigned __int8)(v_stack_m108) == 0) goto loc_003F4042;
loc_003F3F4A:
loc_003F3F50:
    *(unsigned __int64 *)(v_rsi) = a3;
    *(unsigned __int64 *)(v_rsi + 8) = *(unsigned __int64 *)(a2 + 48);
    *(unsigned __int64 *)(v_rsi + 24) = 0;
    *(unsigned __int64 *)(v_rsi + 16) = 0;
    result = *(unsigned __int64 *)(a2 + 48);
    if (*(unsigned __int64 *)(v_rsi + 24) != 0) {
        a2 = 0x746C6644ULL;
        result = ObDereferenceObjectDeferDeleteWithTag(*(unsigned __int64 *)(v_rsi + 24), a2, a3, v_rsi);
    }
    v_stack_mC0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(v_rsi + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_mB8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(v_rsi + 24) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x746C6644ULL), a3, v_rsi);
    v_rbx = 0;
    *(unsigned __int8 *)(v_rsi + 32) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 144))) & (32));
    result = (unsigned int)((result) | ((unsigned int)((unsigned int)(a6))));
    *(unsigned int *)(v_rsi + 144) = (unsigned int)(result);
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(a2 + 48), (unsigned int)(0x746C6644ULL), a3, v_rsi);
    *(unsigned __int64 *)(a3 + 56) = v_rsi;
    result = KeAcquireQueuedSpinLock(7, (unsigned int)(0x746C6644ULL), a3, v_rsi);
    *(unsigned __int8 *)(a3 + 69) = (unsigned __int8)(result);
    if ((*(unsigned __int8 *)(a3 + 68)) == 0) goto loc_003F4005;
    result = FsRtlpCancelExclusiveIrp(a3, 1, 1, v_rsi);
    goto loc_003F403D;
loc_003F4005:
    result = KeReleaseQueuedSpinLock(7, *(unsigned __int8 *)(a3 + 69), 1, v_rsi);
    v_stack_m128 = v_rsi + 184;
    result = FsRtlpOplockTryPrepForAckTimeout(v_rsi, *(unsigned __int64 *)(v_rsi + 8), a3, v_rsi + 168);
loc_003F403D:
loc_003F4042:
    result = ExReleaseFastMutexUnsafe(*(unsigned __int64 *)(v_rsi + 152), *(unsigned __int64 *)(v_rsi + 8), a3, v_rsi + 168);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(v_rsi + 8), a3, v_rsi + 168);
    v_rsp = (v_rsp) + (272);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlpRequestExclusiveOplock(void *Arg1, void *Arg2, void *Arg3, int32_t Arg4, uint64_t Arg5, uint32_t Arg6, uint32_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint8_t v_stack_m107;
    uint8_t v_stack_m108;
    uint8_t v_stack_m110;
    uint16_t v_stack_m118;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint8_t v_stack_p28;

    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0xA16F26)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m100 = Arg4;
    result = 0;
    v_stack_mF8 = 0;
    v_stack_m108 = 0;
    v_stack_mF0 = 0;
    local_rsi = *(uint64_t *)(arg1);
    if (*(uint64_t *)(arg1) == 0) {
        result = FsRtlpAllocateOplock(Arg1, Arg2, Arg3, Arg4);
        local_rsi = result;
        *(uint64_t *)(arg1) = result;
    }
    v_stack_mE8 = local_rsi;
    result = ExAcquireFastMutexUnsafe(*(uint64_t *)(local_rsi + 0x98), Arg2, Arg3, Arg4);
    if (((*(uint32_t *)(local_rsi + 0x90)) & (0x10000ULL)) == 0) goto loc_003F39F9;
    local_r10 = 0;
    if ((*(uint8_t *)(arg2)) != 13) goto loc_003F39FC;
loc_003F38A3:
    if ((*(uint64_t *)(local_rsi + 0x78)) == (local_rsi + 120)) goto loc_003F38C1;
    if ((*(uint64_t *)(arg2 + 0x30)) != (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x78) - 0x38 + 0x18))) goto loc_003F3959;
    *(uint64_t *)(v_stack_mF0) = *(uint64_t *)(local_rsi + 0x78) - 56;
loc_003F38C1:
    if (1 == 0) goto loc_003F39FC;
    if (((*(uint32_t *)(local_rsi + 0x90)) & (0x20000ULL)) == 0) goto loc_003F3961;
    result = FsRtlpOplockDequeueRH(v_stack_mF0, 1, *(uint64_t *)(arg2 + 0x30), v_stack_mF0);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x38) + 0x8)) != (v_stack_mF0 + 56)) goto loc_003F3B29;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x38 + 0x8))) != (v_stack_mF0 + 56)) goto loc_003F3B29;
    *(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x38 + 0x8)) = *(uint64_t *)(v_stack_mF0 + 0x38);
    *(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x38) + 0x8) = *(uint64_t *)(v_stack_mF0 + 0x38 + 0x8);
    if ((*(uint64_t *)(local_rsi + 0x78)) == (local_rsi + 120)) {
    }
    result = *(uint64_t *)(v_stack_mF0 + 0x38 + 0x8);
    if ((*(uint64_t *)(v_stack_mF0 + 0x28)) != 0) {
        Arg2 = v_stack_mF0;
        Arg1 = local_rsi;
        result = FsRtlpClearOwner(Arg1, Arg2, *(uint64_t *)(arg2 + 0x30), v_stack_mF0 + 56);
    }
    result = FsRtlpFreeRHOpContext(v_stack_mF0, 1, *(uint64_t *)(arg2 + 0x30), v_stack_mF0 + 56);
    result = 0;
    v_stack_mF0 = 0;
    result = FsRtlpComputeShareableOplockState(local_rsi, 1, *(uint64_t *)(arg2 + 0x30), v_stack_mF0 + 56);
loc_003F3941:
loc_003F3946:
loc_003F3949:
    *(uint32_t *)(arg3 + 0x30) = (uint32_t)((uint32_t)(0xC00000E2ULL));
    result = IofCompleteRequest(Arg3, 1, *(uint64_t *)(arg2 + 0x30), v_stack_mF0 + 56);
    goto loc_003F4042;
loc_003F3959:
    goto loc_003F38A3;
loc_003F3961:
loc_003F3968:
    if ((*(uint64_t *)(local_rsi + 0x58)) == (local_rsi + 88)) goto loc_003F398B;
    result = local_rsi + 88;
    local_r15 = *(uint64_t *)(local_rsi + 0x58);
    if ((*(uint8_t *)(*(uint64_t *)(local_rsi + 0x58) + 0x35)) == 0) {
        local_r15 = *(uint64_t *)(*(uint64_t *)(local_rsi + 0x58) + 0x8);
        result = FsRtlpRemoveAndCompleteWaitingIrp(*(uint64_t *)(local_rsi + 0x58), 1, *(uint64_t *)(arg2 + 0x30), v_stack_mF0 + 56);
        result = local_rsi + 88;
        local_r10 = 0;
    }
    goto loc_003F3968;
loc_003F398B:
    result = FsRtlpOplockDequeueRH(v_stack_mF0, 1, *(uint64_t *)(arg2 + 0x30), v_stack_mF0 + 56);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x38) + 0x8)) != (v_stack_mF0 + 56)) goto loc_003F3B29;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x38 + 0x8))) != (v_stack_mF0 + 56)) goto loc_003F3B29;
    *(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x38 + 0x8)) = *(uint64_t *)(v_stack_mF0 + 0x38);
    *(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x38) + 0x8) = *(uint64_t *)(v_stack_mF0 + 0x38 + 0x8);
    if ((*(uint64_t *)(local_rsi + 0x78)) == (local_rsi + 120)) {
    }
    result = *(uint64_t *)(v_stack_mF0 + 0x38 + 0x8);
    if ((*(uint64_t *)(v_stack_mF0 + 0x28)) != 0) {
        Arg2 = v_stack_mF0;
        Arg1 = local_rsi;
        result = FsRtlpClearOwner(Arg1, Arg2, *(uint64_t *)(arg2 + 0x30), v_stack_mF0 + 56);
    }
    result = FsRtlpFreeRHOpContext(v_stack_mF0, 1, *(uint64_t *)(arg2 + 0x30), v_stack_mF0 + 56);
    result = 0;
    v_stack_mF0 = 0;
    result = FsRtlpComputeShareableOplockState(local_rsi, 1, *(uint64_t *)(arg2 + 0x30), v_stack_mF0 + 56);
loc_003F39F9:
    local_r10 = 0;
loc_003F39FC:
    result = FsRtlpOplockUpperLowerCompatible((uint32_t)((uint32_t)((uint32_t)(Arg6))), (uint32_t)(Arg7), *(uint64_t *)(arg2 + 0x30), v_stack_mF0 + 56);
    if ((uint8_t)(result) == 0) goto loc_003F3941;
    if (condition_is_above_or_equal) goto loc_003F3B30;
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x30) + 0x28) == 0) goto loc_003F3B30;
    result = MmDoesFileHaveUserWritableReferences(*(uint64_t *)(*(uint64_t *)(arg2 + 0x30) + 0x28), (uint32_t)(Arg7), *(uint64_t *)(arg2 + 0x30), v_stack_mF0 + 56);
    local_r10 = 0;
    if ((uint32_t)(result) == 0) goto loc_003F3B30;
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0x8) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0xC))) | ((uint32_t)(local_r10 + 4)));
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0xC) = (uint32_t)(result);
    if ((*(uint32_t *)(v_rip + 0xA131ED)) <= 5) goto loc_003F3941;
    result = tlgKeywordOn(v_rip + 10564054, (uint32_t)(Arg7), local_r10 + 4, v_stack_mF0 + 56);
    if ((uint8_t)(result) == 0) goto loc_003F3941;
    v_stack_mD8 = 1;
    v_stack_m88 = v_stack_mD8;
    v_stack_m80 = 8;
    v_stack_mF8 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m78 = v_stack_mF8;
    v_stack_m70 = local_r10 + 4;
    v_stack_m100 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x90)));
    v_stack_m68 = v_stack_m100;
    v_stack_m60 = local_r10 + 4;
    v_stack_mE0 = 0x1000000ULL;
    v_stack_m58 = v_stack_mE0;
    v_stack_m50 = 8;
    v_stack_m128 = v_stack_mA8;
    result = tlgWriteAgg(v_rip + 10563889, v_rip - 3859958, local_r10 + 4, local_r10 + 6);
    goto loc_003F3941;
loc_003F3B29:
loc_003F3B30:
    if (((uint32_t)((uint32_t)(Arg6))) != 200) goto loc_003F3B5F;
    *(void **)(local_rsi) = Arg3;
    *(uint64_t *)(local_rsi + 0x8) = *(uint64_t *)(arg2 + 0x30);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x90))) & (32));
    result = (uint32_t)((result) | (200));
    *(uint32_t *)(local_rsi + 0x90) = (uint32_t)(result);
    goto loc_003F3F38;
loc_003F3B5F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x90)))) & (145)) == 0) goto loc_003F3C3D;
    Arg1 = ((((uint32_t)((uint32_t)(0x7000ULL))) & ((uint32_t)((uint32_t)(Arg6)))) != 0) ? 1 : 0;
    result = ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x90)))) & (16)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_003F3B99;
loc_003F3B84:
    if (condition_is_above_or_equal) goto loc_003F3941;
loc_003F3B8F:
    goto loc_003F4042;
loc_003F3B99:
    if (!sign_flag) goto loc_003F3BB8;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(arg2 + 0x30), *(uint64_t *)(local_rsi + 0x8), Arg3, local_r10 + 6);
    v_stack_m107 = (uint8_t)(result);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_003F3B84;
loc_003F3BB8:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x90))) & (0x1F0FFDFULL));
    if (((uint32_t)(result)) == 16) goto loc_003F3BD6;
    if (((uint32_t)(result)) == 0x1000ULL) goto loc_003F3BD6;
    if (((uint32_t)(result)) == 0x1010ULL) {
        Arg4 = local_rsi;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_rsi + 0x28);
        result = FsRtlpRemoveAndCompleteReadOnlyIrp(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
    if (v_stack_m100 <= 1) goto loc_003F3C1D;
    Arg1 = (((*(uint8_t *)(local_rsi + 0x90)) & (1)) != 0) ? 1 : 0;
    result = (((v_stack_p28) & (1)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_003F3C1D;
    if (0 == 0) goto loc_003F4042;
    goto loc_003F3946;
loc_003F3C1D:
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x30) + 0x49)) == 0) goto loc_003F3C32;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x30) + 0x49)) < 0) goto loc_003F3B84;
loc_003F3C32:
    goto loc_003F3F4A;
loc_003F3C3D:
    Arg1 = (((1) & (0)) != 0) ? 1 : 0;
    result = (((0) & (0x1F00F00ULL)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_003F3F0E;
    if ((*(uint64_t *)(local_rsi + 0x48)) != (local_rsi + 72)) goto loc_003F3F0E;
    if ((*(uint64_t *)(local_rsi + 0x48)) < (local_rsi + 72)) goto loc_003F3B8F;
    if (((1) & ((uint32_t)((uint32_t)(Arg6)))) == 0) goto loc_003F3941;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x30) + 0x49)) == 0) goto loc_003F3C8A;
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x30) + 0x49)) < 0) goto loc_003F3941;
loc_003F3C8A:
    Arg2 = (uint32_t)((Arg2) & (0x1F0FFDFULL));
    if (((uint32_t)(Arg2)) == 0x1000ULL) goto loc_003F3E5C;
    if (((uint32_t)(Arg2)) == 0x3000ULL) goto loc_003F3DAA;
    if (((uint32_t)(Arg2)) == 0x5040ULL) goto loc_003F3CC6;
    if (((uint32_t)(Arg2)) != ((uint32_t)((uint32_t)(0x7040ULL)))) goto loc_003F3941;
    if (((uint32_t)((uint32_t)(Arg6))) != ((uint32_t)((uint32_t)(0x7040ULL)))) goto loc_003F3941;
loc_003F3CC6:
    if ((((uint32_t)((uint32_t)(Arg6) - 20544)) & (0xFFFFDFFFULL)) != 0) goto loc_003F3941;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(arg2 + 0x30), *(uint64_t *)(local_rsi + 0x8), Arg3, Arg4);
    v_stack_m107 = (uint8_t)(result);
    local_r12 = 0;
    if ((uint8_t)(result) == 0) goto loc_003F3941;
    v_stack_mD0 = *(uint64_t *)(local_rsi);
    result = KeAcquireQueuedSpinLock((uint32_t)((uint32_t)(local_r12 + 7)), *(uint64_t *)(local_rsi + 0x8), Arg3, Arg4);
    *(uint8_t *)(*(uint64_t *)(local_rsi) + 0x45) = (uint8_t)(result);
    result = KeReleaseQueuedSpinLock((uint32_t)((uint32_t)(local_r12 + 7)), *(uint8_t *)(*(uint64_t *)(local_rsi) + 0x45), Arg3, Arg4);
    if ((*(uint8_t *)(v_stack_mD0 + 0x44)) == 0) goto loc_003F3D35;
    *(uint64_t *)(*(uint64_t *)(local_rsi) + 0x38) = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsi) + 0x30) = 0xC0000120ULL;
    goto loc_003F3D7D;
loc_003F3D35:
    v_stack_mC8 = *(uint64_t *)(v_stack_mD0 + 0x18);
    result = 0;
    *(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x18)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_stack_mD0 + 0x18) + 0x10) = 0;
    *(uint32_t *)(*(uint64_t *)(v_stack_mD0 + 0x18)) = 0x180001ULL;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x90))) >> (12));
    result = (uint32_t)((result) & ((uint32_t)(local_r12 + 7)));
    *(uint32_t *)(*(uint64_t *)(v_stack_mD0 + 0x18) + 0x4) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) >> (12));
    result = (uint32_t)((result) & ((uint32_t)(local_r12 + 7)));
    *(uint32_t *)(*(uint64_t *)(v_stack_mD0 + 0x18) + 0x8) = (uint32_t)(result);
    *(uint64_t *)(*(uint64_t *)(local_rsi) + 0x38) = result + 24;
    *(uint32_t *)(*(uint64_t *)(local_rsi) + 0x30) = 533;
loc_003F3D7D:
    result = IofCompleteRequest(v_stack_mD0, 1, result + 24, Arg4);
    result = 0;
    *(uint64_t *)(local_rsi) = 0;
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(local_rsi + 0x8), (uint32_t)(0x746C6644ULL), result + 24, Arg4);
    local_r10 = 0;
    *(uint64_t *)(local_rsi + 0x8) = 0;
    goto loc_003F3F50;
loc_003F3DAA:
    if (((uint32_t)((uint32_t)(Arg6))) != ((uint32_t)((uint32_t)(0x7040ULL)))) goto loc_003F3941;
loc_003F3DBC:
    if ((*(uint64_t *)(local_rsi + 0x38)) == (local_rsi + 56)) goto loc_003F3DF9;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(arg2 + 0x30), *(uint64_t *)(*(uint64_t *)(local_rsi + 0x38) + 0x18), Arg3, Arg4);
    v_stack_m107 = (uint8_t)(result);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_003F3941;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi + 0x38) + 0x38)) == 0) goto loc_003F3DF4;
    goto loc_003F3946;
loc_003F3DF4:
    goto loc_003F3DBC;
loc_003F3DF9:
    if (v_stack_m100 <= ((uint32_t)(local_r12 + 7))) goto loc_003F3E0E;
    if (((v_stack_p28) & ((uint8_t)(local_r12 + 7))) == 0) goto loc_003F3941;
loc_003F3E0E:
loc_003F3E12:
    v_stack_m100 = *(uint64_t *)(local_rsi + 0x38);
    if ((*(uint64_t *)(local_rsi + 0x38)) == (local_rsi + 56)) goto loc_003F3C32;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (1));
    v_stack_m110 = 0;
    v_stack_m118 = 0;
    v_stack_m120 = 0;
    v_stack_m128 = 0;
    result = FsRtlpRemoveAndCompleteRHIrp(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsi + 0x38) + 0x8)), local_rsi, 533, Arg4);
    local_r10 = 0;
    goto loc_003F3E12;
loc_003F3E5C:
    if ((((uint32_t)((uint32_t)(Arg6) - 20544)) & (0xFFFFDFFFULL)) != 0) goto loc_003F3941;
loc_003F3E72:
    if ((*(uint64_t *)(local_rsi + 0x28)) == (local_rsi + 40)) goto loc_003F3EB0;
    v_stack_mE0 = *(uint64_t *)(*(uint64_t *)(local_rsi + 0x28) + 0x10);
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(arg2 + 0x30), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsi + 0x28) + 0x10) + 0x30), Arg3, Arg4);
    v_stack_m107 = (uint8_t)(result);
    if ((uint8_t)(result) != 0) goto loc_003F3EAB;
    goto loc_003F3949;
loc_003F3EAB:
    goto loc_003F3E72;
loc_003F3EB0:
    if (v_stack_m100 <= 1) goto loc_003F3ECB;
    if (((v_stack_p28) & (1)) == 0) goto loc_003F3941;
loc_003F3ECB:
loc_003F3ECF:
    v_stack_m100 = *(uint64_t *)(local_rsi + 0x28);
    if ((*(uint64_t *)(local_rsi + 0x28)) == (local_rsi + 40)) goto loc_003F3EFC;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (1));
    result = FsRtlpRemoveAndCompleteReadOnlyIrp(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsi + 0x28) + 0x8)), 533, Arg3, local_rsi);
    goto loc_003F3ECF;
loc_003F3EFC:
    v_stack_m108 = 1;
    local_r10 = 0;
    goto loc_003F3F42;
loc_003F3F0E:
    if (condition_is_below) goto loc_003F3B8F;
    result = 1;
    if (Arg3 != NULL) {
        *(uint32_t *)(arg3 + 0x30) = (uint32_t)((uint32_t)(0xC00000E2ULL));
        Arg2 = (uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsi + 0x28) + 0x8));
        Arg1 = Arg3;
        result = IofCompleteRequest(Arg1, Arg2, Arg3, local_rsi);
        local_r10 = 0;
    }
    v_stack_mF8 = (uint32_t)((uint32_t)(0xC00000E2ULL));
loc_003F3F38:
loc_003F3F42:
    if ((uint8_t)(v_stack_m108) == 0) goto loc_003F4042;
loc_003F3F4A:
loc_003F3F50:
    *(void **)(local_rsi) = Arg3;
    *(uint64_t *)(local_rsi + 0x8) = *(uint64_t *)(arg2 + 0x30);
    *(uint64_t *)(local_rsi + 0x18) = 0;
    *(uint64_t *)(local_rsi + 0x10) = 0;
    result = *(uint64_t *)(arg2 + 0x30);
    if (*(uint64_t *)(local_rsi + 0x18) != 0) {
        Arg2 = 0x746C6644ULL;
        result = ObDereferenceObjectDeferDeleteWithTag(*(uint64_t *)(local_rsi + 0x18), Arg2, Arg3, local_rsi);
    }
    v_stack_mC0 = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(local_rsi + 0x10) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_mB8 = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(local_rsi + 0x18) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = ObfReferenceObjectWithTag(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x746C6644ULL), Arg3, local_rsi);
    local_rbx = 0;
    *(uint8_t *)(local_rsi + 0x20) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x90))) & (32));
    result = (uint32_t)((result) | ((uint32_t)((uint32_t)(Arg6))));
    *(uint32_t *)(local_rsi + 0x90) = (uint32_t)(result);
    result = ObfReferenceObjectWithTag(*(uint64_t *)(arg2 + 0x30), (uint32_t)(0x746C6644ULL), Arg3, local_rsi);
    *(uint64_t *)(arg3 + 0x38) = local_rsi;
    result = KeAcquireQueuedSpinLock(7, (uint32_t)(0x746C6644ULL), Arg3, local_rsi);
    *(uint8_t *)(arg3 + 0x45) = (uint8_t)(result);
    if ((*(uint8_t *)(arg3 + 0x44)) == 0) goto loc_003F4005;
    result = FsRtlpCancelExclusiveIrp(Arg3, 1, 1, local_rsi);
    goto loc_003F403D;
loc_003F4005:
    result = KeReleaseQueuedSpinLock(7, *(uint8_t *)(arg3 + 0x45), 1, local_rsi);
    v_stack_m128 = local_rsi + 184;
    result = FsRtlpOplockTryPrepForAckTimeout(local_rsi, *(uint64_t *)(local_rsi + 0x8), Arg3, local_rsi + 168);
loc_003F403D:
loc_003F4042:
    result = ExReleaseFastMutexUnsafe(*(uint64_t *)(local_rsi + 0x98), *(uint64_t *)(local_rsi + 0x8), Arg3, local_rsi + 168);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(local_rsi + 0x8), Arg3, local_rsi + 168);
    local_rsp = (local_rsp) + (272);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F3800&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
