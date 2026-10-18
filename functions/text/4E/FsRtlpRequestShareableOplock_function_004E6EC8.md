# FsRtlpRequestShareableOplock

- RVA: `0x004E6EC8`–`0x004E7991` (길이 `2,761` bytes)
- VA: `0x00000001404E6EC8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5FE8`
- 디코드: `675`개 명령, `2,761/2,761` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x004E6F3B` → [FsRtlpAllocateOplock](../../page/9F/FsRtlpAllocateOplock_function_009F1C74.md) (function, `0x009F1C74`)
- `0x004E6F6D` → [ExAcquireFastMutexUnsafe](../3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x004E6FA4` → [FsRtlpCallerIsAtomicRequestor](../47/FsRtlpCallerIsAtomicRequestor_function_00477E50.md) (function, `0x00477E50`)
- `0x004E6FC3` → [FsRtlpOplockDequeueRH](../42/FsRtlpOplockDequeueRH_function_004258FC.md) (function, `0x004258FC`)
- `0x004E7004` → [FsRtlpClearOwner](../26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x004E700E` → [FsRtlpFreeRHOpContext](../4F/FsRtlpFreeRHOpContext_function_004F2394.md) (function, `0x004F2394`)
- `0x004E701E` → [FsRtlpComputeShareableOplockState](../42/FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x004E7052` → [FsRtlpRemoveAndCompleteWaitingIrp](../42/FsRtlpRemoveAndCompleteWaitingIrp_function_00425FC0.md) (function, `0x00425FC0`)
- `0x004E7067` → [FsRtlpOplockDequeueRH](../42/FsRtlpOplockDequeueRH_function_004258FC.md) (function, `0x004258FC`)
- `0x004E70B0` → [FsRtlpClearOwner](../26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x004E70BA` → [FsRtlpFreeRHOpContext](../4F/FsRtlpFreeRHOpContext_function_004F2394.md) (function, `0x004F2394`)
- `0x004E70CA` → [FsRtlpComputeShareableOplockState](../42/FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x004E70E7` → [FsRtlpOplockUpperLowerCompatible](../../page/A2/FsRtlpOplockUpperLowerCompatible_function_00A21E04.md) (function, `0x00A21E04`)
- `0x004E711E` → [MmDoesFileHaveUserWritableReferences](../2B/MmDoesFileHaveUserWritableReferences_function_002BB690.md) (function, `0x002BB690`)
- `0x004E7179` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x004E722E` → [tlgWriteAgg](../2F/tlgWriteAgg_function_002F0F7C.md) (function, `0x002F0F7C`)
- `0x004E730B` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E733C` → [FsRtlpRemoveAndCompleteReadOnlyIrp](../4B/FsRtlpRemoveAndCompleteReadOnlyIrp_function_004B495C.md) (function, `0x004B495C`)
- `0x004E7373` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E73BA` → [FsRtlpRemoveAndCompleteRHIrp](../42/FsRtlpRemoveAndCompleteRHIrp_function_00425964.md) (function, `0x00425964`)
- `0x004E73E4` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E745A` → [FsRtlpOplockEnqueueRH](../38/FsRtlpOplockEnqueueRH_function_0038F534.md) (function, `0x0038F534`)
- `0x004E747D` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x004E7500` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x004E753E` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x004E754C` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x004E7578` → [FsRtlpCancelOplockRHIrp](../4A/FsRtlpCancelOplockRHIrp_function_004A55F0.md) (function, `0x004A55F0`)
- `0x004E7598` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x004E766B` → [tlgWriteTransfer_EtwWriteTransfer](../42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x004E7673` → [FsRtlpComputeShareableOplockState](../42/FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x004E7678` → [Feature_3244801339__private_IsEnabledDeviceUsageNoInline](../58/Feature_3244801339__private_IsEnabledDeviceUsageNoInline_function_00581C88.md) (function, `0x00581C88`)
- `0x004E76A5` → [FsRtlpOplockTryPrepForAckTimeout](../../page/71/FsRtlpOplockTryPrepForAckTimeout_function_007156C0.md) (function, `0x007156C0`)
- `0x004E76AA` → [Feature_3244801339__private_IsEnabledDeviceUsageNoInline](../58/Feature_3244801339__private_IsEnabledDeviceUsageNoInline_function_00581C88.md) (function, `0x00581C88`)
- `0x004E76D4` → [Feature_3244801339__private_IsEnabledDeviceUsageNoInline](../58/Feature_3244801339__private_IsEnabledDeviceUsageNoInline_function_00581C88.md) (function, `0x00581C88`)
- `0x004E7704` → [FsRtlpOplockTryPrepForAckTimeout](../../page/71/FsRtlpOplockTryPrepForAckTimeout_function_007156C0.md) (function, `0x007156C0`)
- `0x004E77B1` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E77E0` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E7854` → [FsRtlpOplockKeysEqual](../3F/FsRtlpOplockKeysEqual_function_003F26B0.md) (function, `0x003F26B0`)
- `0x004E7876` → [FsRtlpRemoveAndCompleteReadOnlyIrp](../4B/FsRtlpRemoveAndCompleteReadOnlyIrp_function_004B495C.md) (function, `0x004B495C`)
- `0x004E78CA` → [FsRtlpComputeShareableOplockState](../42/FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x004E78EA` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x004E78F8` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x004E790B` → [FsRtlpCancelReadOnlyOplockIrp](../58/FsRtlpCancelReadOnlyOplockIrp_function_00582380.md) (function, `0x00582380`)
- `0x004E7923` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x004E7949` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x004E7966` → [ExReleaseFastMutexUnsafe](../25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x004E7978` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [FsRtlpAcknowledgeOplockBreakByCacheFlags](../3F/FsRtlpAcknowledgeOplockBreakByCacheFlags_function_003F1988.md) at `0x003F20C3`
- [FsRtlpGrantAnyOplockFromExclusive](../58/FsRtlpGrantAnyOplockFromExclusive_function_00582540.md) at `0x00582801`
- [FsRtlpOplockFsctrlInternal](../../page/9F/FsRtlpOplockFsctrlInternal_function_009F1640.md) at `0x009F17A4`
- [FsRtlpOplockFsctrlInternal](../../page/9F/FsRtlpOplockFsctrlInternal_function_009F1640.md) at `0x009F1899`
- [sub_00B3115E](../../page/B3/Unknown_function_00B3115E.md) at `0x00B31223`

### Static image references
- `0x004E6EDB` → RVA `0x00E0A740` (`.data`; read)
- `0x004E715B` → RVA `0x00E06C50` (`.data`; read)
- `0x004E7220` → RVA `0x000453C0` (`.rdata`; read)
- `0x004E7587` → RVA `0x004A55D0` (`FsRtlpOplockRHIrpCancelRoutine`; read)
- `0x004E765D` → RVA `0x00045358` (`.rdata`; read)
- `0x004E7912` → RVA `0x00582AF0` (`FsRtlpReadOnlyOplockIrpCancelRoutine`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x004E6F3B` → [FsRtlpAllocateOplock](../../page/9F/FsRtlpAllocateOplock_function_009F1C74.md) (`.text` → `PAGE`)
  - `0x004E70E7` → [FsRtlpOplockUpperLowerCompatible](../../page/A2/FsRtlpOplockUpperLowerCompatible_function_00A21E04.md) (`.text` → `PAGE`)
  - `0x004E76A5` → [FsRtlpOplockTryPrepForAckTimeout](../../page/71/FsRtlpOplockTryPrepForAckTimeout_function_007156C0.md) (`.text` → `PAGE`)
  - `0x004E7704` → [FsRtlpOplockTryPrepForAckTimeout](../../page/71/FsRtlpOplockTryPrepForAckTimeout_function_007156C0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004E6EC8  40 53                           push rbx
004E6ECA  56                              push rsi
004E6ECB  57                              push rdi
004E6ECC  41 54                           push r12
004E6ECE  41 55                           push r13
004E6ED0  41 56                           push r14
004E6ED2  41 57                           push r15
004E6ED4  48 81 EC 80 01 00 00            sub rsp, 0x180
004E6EDB  48 8B 05 5E 38 92 00            mov rax, qword ptr [rip + 0x92385e]
004E6EE2  48 33 C4                        xor rax, rsp
004E6EE5  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
004E6EED  45 8B F1                        mov r14d, r9d
004E6EF0  49 8B F0                        mov rsi, r8
004E6EF3  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
004E6EF8  4C 8B F9                        mov r15, rcx
004E6EFB  44 89 4C 24 70                  mov dword ptr [rsp + 0x70], r9d
004E6F00  48 8B 84 24 E0 01 00 00         mov rax, qword ptr [rsp + 0x1e0]
004E6F08  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
004E6F0D  45 33 D2                        xor r10d, r10d
004E6F10  41 8B DA                        mov ebx, r10d
004E6F13  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
004E6F17  4C 89 54 24 60                  mov qword ptr [rsp + 0x60], r10
004E6F1C  4C 89 54 24 78                  mov qword ptr [rsp + 0x78], r10
004E6F21  44 88 54 24 44                  mov byte ptr [rsp + 0x44], r10b
004E6F26  45 8A EA                        mov r13b, r10b
004E6F29  44 88 54 24 45                  mov byte ptr [rsp + 0x45], r10b
004E6F2E  44 88 54 24 58                  mov byte ptr [rsp + 0x58], r10b
004E6F33  48 8B 39                        mov rdi, qword ptr [rcx]
004E6F36  48 85 FF                        test rdi, rdi
004E6F39  75 0E                           jne 0x1404e6f49
004E6F3B  E8 34 AD 50 00                  call 0x1409f1c74
004E6F40  48 8B F8                        mov rdi, rax
004E6F43  49 89 07                        mov qword ptr [r15], rax
004E6F46  45 33 D2                        xor r10d, r10d
004E6F49  41 BC 00 00 01 00               mov r12d, 0x10000
004E6F4F  44 38 94 24 F0 01 00 00         cmp byte ptr [rsp + 0x1f0], r10b
004E6F57  75 21                           jne 0x1404e6f7a
004E6F59  45 3B F4                        cmp r14d, r12d
004E6F5C  74 1C                           je 0x1404e6f7a
004E6F5E  48 8B 87 98 00 00 00            mov rax, qword ptr [rdi + 0x98]
004E6F65  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
004E6F6A  48 8B C8                        mov rcx, rax
004E6F6D  E8 AE C7 F0 FF                  call 0x1403f3720
004E6F72  C6 44 24 44 01                  mov byte ptr [rsp + 0x44], 1
004E6F77  45 33 D2                        xor r10d, r10d
004E6F7A  44 8B 9F 90 00 00 00            mov r11d, dword ptr [rdi + 0x90]
004E6F81  45 85 DC                        test r12d, r11d
004E6F84  0F 84 4D 01 00 00               je 0x1404e70d7
004E6F8A  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004E6F8F  80 38 0D                        cmp byte ptr [rax], 0xd
004E6F92  0F 85 3F 01 00 00               jne 0x1404e70d7
004E6F98  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004E6F9D  48 8B 50 30                     mov rdx, qword ptr [rax + 0x30]
004E6FA1  48 8B CF                        mov rcx, rdi
004E6FA4  E8 A7 0E F9 FF                  call 0x140477e50
004E6FA9  45 33 D2                        xor r10d, r10d
004E6FAC  84 C0                           test al, al
004E6FAE  0F 84 23 01 00 00               je 0x1404e70d7
004E6FB4  41 0F BA E3 11                  bt r11d, 0x11
004E6FB9  73 74                           jae 0x1404e702f
004E6FBB  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
004E6FC0  48 8B CB                        mov rcx, rbx
004E6FC3  E8 34 E9 F3 FF                  call 0x1404258fc
004E6FC8  4C 8D 4B 38                     lea r9, [rbx + 0x38]
004E6FCC  49 8B 09                        mov rcx, qword ptr [r9]
004E6FCF  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
004E6FD3  4C 39 49 08                     cmp qword ptr [rcx + 8], r9
004E6FD7  75 4F                           jne 0x1404e7028
004E6FD9  4C 39 08                        cmp qword ptr [rax], r9
004E6FDC  75 4A                           jne 0x1404e7028
004E6FDE  48 89 08                        mov qword ptr [rax], rcx
004E6FE1  48 89 41 08                     mov qword ptr [rcx + 8], rax
004E6FE5  48 8D 47 78                     lea rax, [rdi + 0x78]
004E6FE9  48 39 00                        cmp qword ptr [rax], rax
004E6FEC  75 0A                           jne 0x1404e6ff8
004E6FEE  81 A7 90 00 00 00 FF FF FC FF   and dword ptr [rdi + 0x90], 0xfffcffff
004E6FF8  4C 39 53 28                     cmp qword ptr [rbx + 0x28], r10
004E6FFC  74 0B                           je 0x1404e7009
004E6FFE  48 8B D3                        mov rdx, rbx
004E7001  48 8B CF                        mov rcx, rdi
004E7004  E8 DF EB D7 FF                  call 0x140265be8
004E7009  B2 01                           mov dl, 1
004E700B  48 8B CB                        mov rcx, rbx
004E700E  E8 81 B3 00 00                  call 0x1404f2394
004E7013  45 33 ED                        xor r13d, r13d
004E7016  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
004E701B  48 8B CF                        mov rcx, rdi
004E701E  E8 C9 E6 F3 FF                  call 0x1404256ec
004E7023  E9 14 09 00 00                  jmp 0x1404e793c
004E7028  B9 03 00 00 00                  mov ecx, 3
004E702D  CD 29                           int 0x29
004E702F  4C 8D 6F 58                     lea r13, [rdi + 0x58]
004E7033  4D 8B 7D 00                     mov r15, qword ptr [r13]
004E7037  4D 3B FD                        cmp r15, r13
004E703A  74 23                           je 0x1404e705f
004E703C  49 8B CF                        mov rcx, r15
004E703F  45 38 57 35                     cmp byte ptr [r15 + 0x35], r10b
004E7043  74 09                           je 0x1404e704e
004E7045  41 81 FE 00 30 00 00            cmp r14d, 0x3000
004E704C  74 0C                           je 0x1404e705a
004E704E  4D 8B 7F 08                     mov r15, qword ptr [r15 + 8]
004E7052  E8 69 EF F3 FF                  call 0x140425fc0
004E7057  45 33 D2                        xor r10d, r10d
004E705A  4D 8B 3F                        mov r15, qword ptr [r15]
004E705D  EB D8                           jmp 0x1404e7037
004E705F  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
004E7064  49 8B CF                        mov rcx, r15
004E7067  E8 90 E8 F3 FF                  call 0x1404258fc
004E706C  4D 8D 4F 38                     lea r9, [r15 + 0x38]
004E7070  49 8B 09                        mov rcx, qword ptr [r9]
004E7073  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
004E7077  4C 39 49 08                     cmp qword ptr [rcx + 8], r9
004E707B  0F 85 BC 00 00 00               jne 0x1404e713d
004E7081  4C 39 08                        cmp qword ptr [rax], r9
004E7084  0F 85 B3 00 00 00               jne 0x1404e713d
004E708A  48 89 08                        mov qword ptr [rax], rcx
004E708D  48 89 41 08                     mov qword ptr [rcx + 8], rax
004E7091  48 8D 47 78                     lea rax, [rdi + 0x78]
004E7095  48 39 00                        cmp qword ptr [rax], rax
004E7098  75 0A                           jne 0x1404e70a4
004E709A  81 A7 90 00 00 00 FF FF FC FF   and dword ptr [rdi + 0x90], 0xfffcffff
004E70A4  4D 39 57 28                     cmp qword ptr [r15 + 0x28], r10
004E70A8  74 0B                           je 0x1404e70b5
004E70AA  49 8B D7                        mov rdx, r15
004E70AD  48 8B CF                        mov rcx, rdi
004E70B0  E8 33 EB D7 FF                  call 0x140265be8
004E70B5  B2 01                           mov dl, 1
004E70B7  49 8B CF                        mov rcx, r15
004E70BA  E8 D5 B2 00 00                  call 0x1404f2394
004E70BF  45 33 ED                        xor r13d, r13d
004E70C2  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
004E70C7  48 8B CF                        mov rcx, rdi
004E70CA  E8 1D E6 F3 FF                  call 0x1404256ec
004E70CF  44 8A 6C 24 45                  mov r13b, byte ptr [rsp + 0x45]
004E70D4  45 33 D2                        xor r10d, r10d
004E70D7  41 BF 00 30 00 00               mov r15d, 0x3000
004E70DD  8B 94 24 F8 01 00 00            mov edx, dword ptr [rsp + 0x1f8]
004E70E4  41 8B CE                        mov ecx, r14d
004E70E7  E8 18 AD 53 00                  call 0x140a21e04
004E70EC  84 C0                           test al, al
004E70EE  0F 84 48 08 00 00               je 0x1404e793c
004E70F4  41 B9 00 10 00 00               mov r9d, 0x1000
004E70FA  45 85 F1                        test r9d, r14d
004E70FD  75 09                           jne 0x1404e7108
004E70FF  45 3B F4                        cmp r14d, r12d
004E7102  0F 85 36 01 00 00               jne 0x1404e723e
004E7108  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
004E710D  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
004E7111  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
004E7115  48 85 C9                        test rcx, rcx
004E7118  0F 84 25 01 00 00               je 0x1404e7243
004E711E  E8 6D 45 DD FF                  call 0x1402bb690
004E7123  45 33 D2                        xor r10d, r10d
004E7126  85 C0                           test eax, eax
004E7128  0F 84 0A 01 00 00               je 0x1404e7238
004E712E  45 3B F4                        cmp r14d, r12d
004E7131  75 11                           jne 0x1404e7144
004E7133  BB E2 00 00 C0                  mov ebx, 0xc00000e2
004E7138  E9 14 08 00 00                  jmp 0x1404e7951
004E713D  B9 03 00 00 00                  mov ecx, 3
004E7142  CD 29                           int 0x29
004E7144  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
004E7148  44 89 51 08                     mov dword ptr [rcx + 8], r10d
004E714C  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
004E714F  41 B8 04 00 00 00               mov r8d, 4
004E7155  41 0B C0                        or eax, r8d
004E7158  89 41 0C                        mov dword ptr [rcx + 0xc], eax
004E715B  83 3D EE FA 91 00 05            cmp dword ptr [rip + 0x91faee], 5
004E7162  0F 86 D4 07 00 00               jbe 0x1404e793c
004E7168  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
004E7172  48 8D 0D D7 FA 91 00            lea rcx, [rip + 0x91fad7]
004E7179  E8 22 79 F4 FF                  call 0x14042eaa0
004E717E  84 C0                           test al, al
004E7180  0F 84 B6 07 00 00               je 0x1404e793c
004E7186  48 C7 84 24 88 00 00 00 01 00 00 00  mov qword ptr [rsp + 0x88], 1
004E7192  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
004E719A  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
004E71A2  48 C7 84 24 D8 00 00 00 08 00 00 00  mov qword ptr [rsp + 0xd8], 8
004E71AE  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
004E71B3  48 8D 44 24 68                  lea rax, [rsp + 0x68]
004E71B8  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
004E71C0  4C 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r8
004E71C8  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
004E71CE  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
004E71D2  48 8D 44 24 50                  lea rax, [rsp + 0x50]
004E71D7  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
004E71DF  4C 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r8
004E71E7  48 C7 84 24 90 00 00 00 00 00 00 01  mov qword ptr [rsp + 0x90], 0x1000000
004E71F3  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
004E71FB  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
004E7203  48 C7 84 24 08 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x108], 8
004E720F  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
004E7217  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004E721C  45 8D 48 02                     lea r9d, [r8 + 2]
004E7220  48 8D 15 99 E1 B5 FF            lea rdx, [rip - 0x4a1e67]
004E7227  48 8D 0D 22 FA 91 00            lea rcx, [rip + 0x91fa22]
004E722E  E8 49 9D E0 FF                  call 0x1402f0f7c
004E7233  E9 04 07 00 00                  jmp 0x1404e793c
004E7238  41 B9 00 10 00 00               mov r9d, 0x1000
004E723E  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
004E7243  8A 94 24 F0 01 00 00            mov dl, byte ptr [rsp + 0x1f0]
004E724A  84 D2                           test dl, dl
004E724C  75 1D                           jne 0x1404e726b
004E724E  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
004E7254  A8 40                           test al, 0x40
004E7256  74 13                           je 0x1404e726b
004E7258  45 3B F4                        cmp r14d, r12d
004E725B  0F 85 DB 06 00 00               jne 0x1404e793c
004E7261  BB 09 09 00 C0                  mov ebx, 0xc0000909
004E7266  E9 E6 06 00 00                  jmp 0x1404e7951
004E726B  41 83 FE 10                     cmp r14d, 0x10
004E726F  0F 84 99 04 00 00               je 0x1404e770e
004E7275  45 3B F1                        cmp r14d, r9d
004E7278  0F 84 B4 04 00 00               je 0x1404e7732
004E727E  45 3B F7                        cmp r14d, r15d
004E7281  74 09                           je 0x1404e728c
004E7283  45 3B F4                        cmp r14d, r12d
004E7286  0F 85 AB 06 00 00               jne 0x1404e7937
004E728C  84 D2                           test dl, dl
004E728E  75 36                           jne 0x1404e72c6
004E7290  8B 8F 90 00 00 00               mov ecx, dword ptr [rdi + 0x90]
004E7296  F6 C1 01                        test cl, 1
004E7299  75 2B                           jne 0x1404e72c6
004E729B  8B C1                           mov eax, ecx
004E729D  25 DF FF F0 01                  and eax, 0x1f0ffdf
004E72A2  41 3B C1                        cmp eax, r9d
004E72A5  74 1F                           je 0x1404e72c6
004E72A7  41 3B C7                        cmp eax, r15d
004E72AA  74 1A                           je 0x1404e72c6
004E72AC  3D 00 B0 00 00                  cmp eax, 0xb000
004E72B1  74 13                           je 0x1404e72c6
004E72B3  3D 00 30 10 00                  cmp eax, 0x103000
004E72B8  74 0C                           je 0x1404e72c6
004E72BA  3D 00 30 80 00                  cmp eax, 0x803000
004E72BF  74 05                           je 0x1404e72c6
004E72C1  41 85 CC                        test r12d, ecx
004E72C4  74 92                           je 0x1404e7258
004E72C6  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
004E72CA  44 38 50 49                     cmp byte ptr [rax + 0x49], r10b
004E72CE  75 88                           jne 0x1404e7258
004E72D0  84 D2                           test dl, dl
004E72D2  0F 85 54 01 00 00               jne 0x1404e742c
004E72D8  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
004E72DE  25 DF FF F0 01                  and eax, 0x1f0ffdf
004E72E3  41 3B C1                        cmp eax, r9d
004E72E6  74 07                           je 0x1404e72ef
004E72E8  3D 00 B0 00 00                  cmp eax, 0xb000
004E72ED  75 57                           jne 0x1404e7346
004E72EF  48 8B 5F 28                     mov rbx, qword ptr [rdi + 0x28]
004E72F3  48 8D 47 28                     lea rax, [rdi + 0x28]
004E72F7  48 3B D8                        cmp rbx, rax
004E72FA  74 4A                           je 0x1404e7346
004E72FC  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
004E7300  48 8B 50 30                     mov rdx, qword ptr [rax + 0x30]
004E7304  49 8B 48 30                     mov rcx, qword ptr [r8 + 0x30]
004E7308  45 33 C0                        xor r8d, r8d
004E730B  E8 A0 B3 F0 FF                  call 0x1403f26b0
004E7310  45 33 D2                        xor r10d, r10d
004E7313  84 C0                           test al, al
004E7315  0F 84 E8 00 00 00               je 0x1404e7403
004E731B  45 3B F4                        cmp r14d, r12d
004E731E  75 0A                           jne 0x1404e732a
004E7320  BB E3 00 00 C0                  mov ebx, 0xc00000e3
004E7325  E9 27 06 00 00                  jmp 0x1404e7951
004E732A  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
004E732E  4C 8B CF                        mov r9, rdi
004E7331  45 8B C7                        mov r8d, r15d
004E7334  BA 15 02 00 00                  mov edx, 0x215
004E7339  48 8B 09                        mov rcx, qword ptr [rcx]
004E733C  E8 1B D6 FC FF                  call 0x1404b495c
004E7341  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
004E7346  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
004E734C  25 DF FF F0 01                  and eax, 0x1f0ffdf
004E7351  41 2B C7                        sub eax, r15d
004E7354  A9 FF 7F FF FF                  test eax, 0xffff7fff
004E7359  75 64                           jne 0x1404e73bf
004E735B  48 8B 5F 38                     mov rbx, qword ptr [rdi + 0x38]
004E735F  48 8D 47 38                     lea rax, [rdi + 0x38]
004E7363  48 3B D8                        cmp rbx, rax
004E7366  74 57                           je 0x1404e73bf
004E7368  48 8B 53 18                     mov rdx, qword ptr [rbx + 0x18]
004E736C  49 8B 48 30                     mov rcx, qword ptr [r8 + 0x30]
004E7370  45 33 C0                        xor r8d, r8d
004E7373  E8 38 B3 F0 FF                  call 0x1403f26b0
004E7378  45 33 D2                        xor r10d, r10d
004E737B  84 C0                           test al, al
004E737D  0F 84 8D 00 00 00               je 0x1404e7410
004E7383  4C 39 53 38                     cmp qword ptr [rbx + 0x38], r10
004E7387  0F 85 83 00 00 00               jne 0x1404e7410
004E738D  45 3B F4                        cmp r14d, r12d
004E7390  74 8E                           je 0x1404e7320
004E7392  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
004E7396  44 88 54 24 38                  mov byte ptr [rsp + 0x38], r10b
004E739B  66 44 89 54 24 30               mov word ptr [rsp + 0x30], r10w
004E73A1  44 89 54 24 28                  mov dword ptr [rsp + 0x28], r10d
004E73A6  44 89 54 24 20                  mov dword ptr [rsp + 0x20], r10d
004E73AB  45 8B CF                        mov r9d, r15d
004E73AE  41 B8 15 02 00 00               mov r8d, 0x215
004E73B4  48 8B D7                        mov rdx, rdi
004E73B7  48 8B 09                        mov rcx, qword ptr [rcx]
004E73BA  E8 A5 E5 F3 FF                  call 0x140425964
004E73BF  48 8D 47 48                     lea rax, [rdi + 0x48]
004E73C3  48 8B 18                        mov rbx, qword ptr [rax]
004E73C6  48 3B D8                        cmp rbx, rax
004E73C9  74 57                           je 0x1404e7422
004E73CB  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
004E73D0  48 8D 47 48                     lea rax, [rdi + 0x48]
004E73D4  48 3B D8                        cmp rbx, rax
004E73D7  74 50                           je 0x1404e7429
004E73D9  48 8B 53 18                     mov rdx, qword ptr [rbx + 0x18]
004E73DD  49 8B 4F 30                     mov rcx, qword ptr [r15 + 0x30]
004E73E1  45 33 C0                        xor r8d, r8d
004E73E4  E8 C7 B2 F0 FF                  call 0x1403f26b0
004E73E9  45 33 D2                        xor r10d, r10d
004E73EC  84 C0                           test al, al
004E73EE  74 2D                           je 0x1404e741d
004E73F0  BB E2 00 00 C0                  mov ebx, 0xc00000e2
004E73F5  45 3B F4                        cmp r14d, r12d
004E73F8  0F 84 53 05 00 00               je 0x1404e7951
004E73FE  E9 3E 05 00 00                  jmp 0x1404e7941
004E7403  48 8B 1B                        mov rbx, qword ptr [rbx]
004E7406  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
004E740B  E9 E3 FE FF FF                  jmp 0x1404e72f3
004E7410  48 8B 1B                        mov rbx, qword ptr [rbx]
004E7413  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
004E7418  E9 42 FF FF FF                  jmp 0x1404e735f
004E741D  48 8B 1B                        mov rbx, qword ptr [rbx]
004E7420  EB AE                           jmp 0x1404e73d0
004E7422  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
004E7427  EB 03                           jmp 0x1404e742c
004E7429  4D 8B C7                        mov r8, r15
004E742C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004E7435  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
004E743C  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
004E7441  48 8B 02                        mov rax, qword ptr [rdx]
004E7444  48 89 48 20                     mov qword ptr [rax + 0x20], rcx
004E7448  49 8B 48 30                     mov rcx, qword ptr [r8 + 0x30]
004E744C  48 8B 02                        mov rax, qword ptr [rdx]
004E744F  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
004E7453  48 8D 4F 38                     lea rcx, [rdi + 0x38]
004E7457  48 8B 12                        mov rdx, qword ptr [rdx]
004E745A  E8 D5 80 EA FF                  call 0x14038f534
004E745F  8B D8                           mov ebx, eax
004E7461  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
004E7465  45 33 D2                        xor r10d, r10d
004E7468  85 C0                           test eax, eax
004E746A  79 1E                           jns 0x1404e748a
004E746C  45 3B F4                        cmp r14d, r12d
004E746F  0F 84 E0 04 00 00               je 0x1404e7955
004E7475  89 46 30                        mov dword ptr [rsi + 0x30], eax
004E7478  B2 01                           mov dl, 1
004E747A  48 8B CE                        mov rcx, rsi
004E747D  E8 3E 41 DB FF                  call 0x14029b5c0
004E7482  45 33 D2                        xor r10d, r10d
004E7485  E9 CB 04 00 00                  jmp 0x1404e7955
004E748A  45 8A EA                        mov r13b, r10b
004E748D  4D 8B FA                        mov r15, r10
004E7490  4C 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], r10
004E7498  45 3B F4                        cmp r14d, r12d
004E749B  75 3A                           jne 0x1404e74d7
004E749D  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
004E74A2  48 8B 00                        mov rax, qword ptr [rax]
004E74A5  48 83 C0 38                     add rax, 0x38
004E74A9  48 8D 4F 78                     lea rcx, [rdi + 0x78]
004E74AD  48 8B 11                        mov rdx, qword ptr [rcx]
004E74B0  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
004E74B4  74 07                           je 0x1404e74bd
004E74B6  B9 03 00 00 00                  mov ecx, 3
004E74BB  CD 29                           int 0x29
004E74BD  48 89 10                        mov qword ptr [rax], rdx
004E74C0  48 89 48 08                     mov qword ptr [rax + 8], rcx
004E74C4  48 89 42 08                     mov qword ptr [rdx + 8], rax
004E74C8  48 89 01                        mov qword ptr [rcx], rax
004E74CB  41 8B DA                        mov ebx, r10d
004E74CE  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
004E74D2  E9 D2 00 00 00                  jmp 0x1404e75a9
004E74D7  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
004E74E0  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
004E74E8  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
004E74ED  49 8B 07                        mov rax, qword ptr [r15]
004E74F0  48 89 48 28                     mov qword ptr [rax + 0x28], rcx
004E74F4  49 8B 07                        mov rax, qword ptr [r15]
004E74F7  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
004E74FB  BA 44 66 6C 74                  mov edx, 0x746c6644
004E7500  E8 0B 92 D2 FF                  call 0x140210710
004E7505  49 8B 07                        mov rax, qword ptr [r15]
004E7508  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
004E750C  48 8B 86 B8 00 00 00            mov rax, qword ptr [rsi + 0xb8]
004E7513  80 48 03 01                     or byte ptr [rax + 3], 1
004E7517  BB 03 01 00 00                  mov ebx, 0x103
004E751C  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
004E7520  33 C0                           xor eax, eax
004E7522  89 46 30                        mov dword ptr [rsi + 0x30], eax
004E7525  48 89 7E 38                     mov qword ptr [rsi + 0x38], rdi
004E7529  38 84 24 E8 01 00 00            cmp byte ptr [rsp + 0x1e8], al
004E7530  74 11                           je 0x1404e7543
004E7532  49 8B 07                        mov rax, qword ptr [r15]
004E7535  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
004E7539  BA 44 66 6C 74                  mov edx, 0x746c6644
004E753E  E8 CD 91 D2 FF                  call 0x140210710
004E7543  41 BF 07 00 00 00               mov r15d, 7
004E7549  41 8B CF                        mov ecx, r15d
004E754C  E8 2F C8 D8 FF                  call 0x140273d80
004E7551  88 46 45                        mov byte ptr [rsi + 0x45], al
004E7554  33 C0                           xor eax, eax
004E7556  38 46 44                        cmp byte ptr [rsi + 0x44], al
004E7559  74 2C                           je 0x1404e7587
004E755B  38 84 24 E8 01 00 00            cmp byte ptr [rsp + 0x1e8], al
004E7562  74 0C                           je 0x1404e7570
004E7564  38 84 24 F0 01 00 00            cmp byte ptr [rsp + 0x1f0], al
004E756B  44 8A C0                        mov r8b, al
004E756E  75 03                           jne 0x1404e7573
004E7570  41 B0 01                        mov r8b, 1
004E7573  B2 01                           mov dl, 1
004E7575  48 8B CE                        mov rcx, rsi
004E7578  E8 73 E0 FB FF                  call 0x1404a55f0
004E757D  4C 8B BC 24 80 00 00 00         mov r15, qword ptr [rsp + 0x80]
004E7585  EB 25                           jmp 0x1404e75ac
004E7587  48 8D 05 42 E0 FB FF            lea rax, [rip - 0x41fbe]
004E758E  48 87 46 68                     xchg qword ptr [rsi + 0x68], rax
004E7592  8A 56 45                        mov dl, byte ptr [rsi + 0x45]
004E7595  49 8B CF                        mov rcx, r15
004E7598  E8 A3 AF D8 FF                  call 0x140272540
004E759D  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
004E75A1  4C 8B BC 24 80 00 00 00         mov r15, qword ptr [rsp + 0x80]
004E75A9  41 B5 01                        mov r13b, 1
004E75AC  83 3D 9D F6 91 00 05            cmp dword ptr [rip + 0x91f69d], 5
004E75B3  0F 86 B7 00 00 00               jbe 0x1404e7670
004E75B9  44 89 74 24 6C                  mov dword ptr [rsp + 0x6c], r14d
004E75BE  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
004E75C3  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
004E75CB  48 C7 84 24 38 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x138], 4
004E75D7  8A 84 24 F0 01 00 00            mov al, byte ptr [rsp + 0x1f0]
004E75DE  88 44 24 45                     mov byte ptr [rsp + 0x45], al
004E75E2  48 8D 44 24 45                  lea rax, [rsp + 0x45]
004E75E7  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
004E75EF  48 C7 84 24 48 01 00 00 01 00 00 00  mov qword ptr [rsp + 0x148], 1
004E75FB  48 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdi
004E7603  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
004E760B  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
004E7613  48 C7 84 24 58 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x158], 8
004E761F  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
004E7625  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
004E7629  48 8D 44 24 48                  lea rax, [rsp + 0x48]
004E762E  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
004E7636  48 C7 84 24 68 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x168], 4
004E7642  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
004E764A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004E764F  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
004E7657  45 33 C9                        xor r9d, r9d
004E765A  45 33 C0                        xor r8d, r8d
004E765D  48 8D 15 F4 DC B5 FF            lea rdx, [rip - 0x4a230c]
004E7664  48 8D 0D E5 F5 91 00            lea rcx, [rip + 0x91f5e5]
004E766B  E8 70 EA F3 FF                  call 0x1404260e0
004E7670  48 8B CF                        mov rcx, rdi
004E7673  E8 74 E0 F3 FF                  call 0x1404256ec
004E7678  E8 0B A6 09 00                  call 0x140581c88
004E767D  85 C0                           test eax, eax
004E767F  75 29                           jne 0x1404e76aa
004E7681  45 84 ED                        test r13b, r13b
004E7684  74 24                           je 0x1404e76aa
004E7686  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
004E768B  48 8B 10                        mov rdx, qword ptr [rax]
004E768E  48 8D 42 58                     lea rax, [rdx + 0x58]
004E7692  4C 8D 4A 48                     lea r9, [rdx + 0x48]
004E7696  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004E769B  4C 8B C6                        mov r8, rsi
004E769E  48 8B 52 18                     mov rdx, qword ptr [rdx + 0x18]
004E76A2  48 8B CF                        mov rcx, rdi
004E76A5  E8 16 E0 22 00                  call 0x1407156c0
004E76AA  E8 D9 A5 09 00                  call 0x140581c88
004E76AF  33 C9                           xor ecx, ecx
004E76B1  85 C0                           test eax, eax
004E76B3  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
004E76B8  74 03                           je 0x1404e76bd
004E76BA  4C 8B 38                        mov r15, qword ptr [rax]
004E76BD  48 89 08                        mov qword ptr [rax], rcx
004E76C0  45 3B F4                        cmp r14d, r12d
004E76C3  75 0F                           jne 0x1404e76d4
004E76C5  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
004E76CB  41 0B C4                        or eax, r12d
004E76CE  89 87 90 00 00 00               mov dword ptr [rdi + 0x90], eax
004E76D4  E8 AF A5 09 00                  call 0x140581c88
004E76D9  45 33 D2                        xor r10d, r10d
004E76DC  85 C0                           test eax, eax
004E76DE  0F 84 71 02 00 00               je 0x1404e7955
004E76E4  45 84 ED                        test r13b, r13b
004E76E7  0F 84 68 02 00 00               je 0x1404e7955
004E76ED  49 8D 47 58                     lea rax, [r15 + 0x58]
004E76F1  4D 8D 4F 48                     lea r9, [r15 + 0x48]
004E76F5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004E76FA  4C 8B C6                        mov r8, rsi
004E76FD  49 8B 57 18                     mov rdx, qword ptr [r15 + 0x18]
004E7701  48 8B CF                        mov rcx, rdi
004E7704  E8 B7 DF 22 00                  call 0x1407156c0
004E7709  E9 74 FD FF FF                  jmp 0x1404e7482
004E770E  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
004E7714  A8 01                           test al, 1
004E7716  75 1A                           jne 0x1404e7732
004E7718  25 DF FF F0 01                  and eax, 0x1f0ffdf
004E771D  83 F8 10                        cmp eax, 0x10
004E7720  74 10                           je 0x1404e7732
004E7722  41 3B C1                        cmp eax, r9d
004E7725  74 0B                           je 0x1404e7732
004E7727  3D 10 10 00 00                  cmp eax, 0x1010
004E772C  0F 85 0A 02 00 00               jne 0x1404e793c
004E7732  84 D2                           test dl, dl
004E7734  0F 85 44 01 00 00               jne 0x1404e787e
004E773A  8B 8F 90 00 00 00               mov ecx, dword ptr [rdi + 0x90]
004E7740  F6 C1 01                        test cl, 1
004E7743  75 3B                           jne 0x1404e7780
004E7745  8B C1                           mov eax, ecx
004E7747  25 DF FF F0 01                  and eax, 0x1f0ffdf
004E774C  83 F8 10                        cmp eax, 0x10
004E774F  74 2F                           je 0x1404e7780
004E7751  41 3B C1                        cmp eax, r9d
004E7754  74 2A                           je 0x1404e7780
004E7756  3D 10 10 00 00                  cmp eax, 0x1010
004E775B  74 23                           je 0x1404e7780
004E775D  41 3B C7                        cmp eax, r15d
004E7760  74 1E                           je 0x1404e7780
004E7762  3D 00 B0 00 00                  cmp eax, 0xb000
004E7767  74 17                           je 0x1404e7780
004E7769  3D 00 30 10 00                  cmp eax, 0x103000
004E776E  74 10                           je 0x1404e7780
004E7770  3D 00 30 80 00                  cmp eax, 0x803000
004E7775  74 09                           je 0x1404e7780
004E7777  41 85 CC                        test r12d, ecx
004E777A  0F 84 BC 01 00 00               je 0x1404e793c
004E7780  84 D2                           test dl, dl
004E7782  0F 85 F6 00 00 00               jne 0x1404e787e
004E7788  48 8D 47 38                     lea rax, [rdi + 0x38]
004E778C  48 8B 18                        mov rbx, qword ptr [rax]
004E778F  48 3B D8                        cmp rbx, rax
004E7792  75 09                           jne 0x1404e779d
004E7794  48 8D 47 48                     lea rax, [rdi + 0x48]
004E7798  48 39 00                        cmp qword ptr [rax], rax
004E779B  74 63                           je 0x1404e7800
004E779D  48 8D 47 38                     lea rax, [rdi + 0x38]
004E77A1  48 3B D8                        cmp rbx, rax
004E77A4  74 22                           je 0x1404e77c8
004E77A6  48 8B 53 18                     mov rdx, qword ptr [rbx + 0x18]
004E77AA  49 8B 48 30                     mov rcx, qword ptr [r8 + 0x30]
004E77AE  45 33 C0                        xor r8d, r8d
004E77B1  E8 FA AE F0 FF                  call 0x1403f26b0
004E77B6  84 C0                           test al, al
004E77B8  0F 85 7E 01 00 00               jne 0x1404e793c
004E77BE  48 8B 1B                        mov rbx, qword ptr [rbx]
004E77C1  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
004E77C6  EB D5                           jmp 0x1404e779d
004E77C8  48 8B 5F 48                     mov rbx, qword ptr [rdi + 0x48]
004E77CC  48 8D 47 48                     lea rax, [rdi + 0x48]
004E77D0  48 3B D8                        cmp rbx, rax
004E77D3  74 22                           je 0x1404e77f7
004E77D5  48 8B 53 18                     mov rdx, qword ptr [rbx + 0x18]
004E77D9  49 8B 48 30                     mov rcx, qword ptr [r8 + 0x30]
004E77DD  45 33 C0                        xor r8d, r8d
004E77E0  E8 CB AE F0 FF                  call 0x1403f26b0
004E77E5  84 C0                           test al, al
004E77E7  0F 85 4F 01 00 00               jne 0x1404e793c
004E77ED  48 8B 1B                        mov rbx, qword ptr [rbx]
004E77F0  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
004E77F5  EB D5                           jmp 0x1404e77cc
004E77F7  45 33 D2                        xor r10d, r10d
004E77FA  41 B9 00 10 00 00               mov r9d, 0x1000
004E7800  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
004E7806  25 DF FF F0 01                  and eax, 0x1f0ffdf
004E780B  83 F8 10                        cmp eax, 0x10
004E780E  74 13                           je 0x1404e7823
004E7810  41 3B C1                        cmp eax, r9d
004E7813  74 0E                           je 0x1404e7823
004E7815  3D 10 10 00 00                  cmp eax, 0x1010
004E781A  74 07                           je 0x1404e7823
004E781C  3D 00 B0 00 00                  cmp eax, 0xb000
004E7821  75 5B                           jne 0x1404e787e
004E7823  48 8B 5F 28                     mov rbx, qword ptr [rdi + 0x28]
004E7827  48 8D 47 28                     lea rax, [rdi + 0x28]
004E782B  48 3B D8                        cmp rbx, rax
004E782E  74 4B                           je 0x1404e787b
004E7830  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
004E7834  48 8D 50 30                     lea rdx, [rax + 0x30]
004E7838  81 78 18 40 02 09 00            cmp dword ptr [rax + 0x18], 0x90240
004E783F  74 09                           je 0x1404e784a
004E7841  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
004E7845  48 39 02                        cmp qword ptr [rdx], rax
004E7848  74 63                           je 0x1404e78ad
004E784A  48 8B 12                        mov rdx, qword ptr [rdx]
004E784D  49 8B 48 30                     mov rcx, qword ptr [r8 + 0x30]
004E7851  45 33 C0                        xor r8d, r8d
004E7854  E8 57 AE F0 FF                  call 0x1403f26b0
004E7859  84 C0                           test al, al
004E785B  74 4B                           je 0x1404e78a8
004E785D  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
004E7861  45 8B C6                        mov r8d, r14d
004E7864  41 81 E0 00 70 00 00            and r8d, 0x7000
004E786B  4C 8B CF                        mov r9, rdi
004E786E  BA 15 02 00 00                  mov edx, 0x215
004E7873  48 8B 09                        mov rcx, qword ptr [rcx]
004E7876  E8 E1 D0 FC FF                  call 0x1404b495c
004E787B  45 33 D2                        xor r10d, r10d
004E787E  48 8B 86 B8 00 00 00            mov rax, qword ptr [rsi + 0xb8]
004E7885  80 48 03 01                     or byte ptr [rax + 3], 1
004E7889  44 89 56 30                     mov dword ptr [rsi + 0x30], r10d
004E788D  48 8D 86 A8 00 00 00            lea rax, [rsi + 0xa8]
004E7894  48 8D 4F 28                     lea rcx, [rdi + 0x28]
004E7898  48 8B 11                        mov rdx, qword ptr [rcx]
004E789B  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
004E789F  74 14                           je 0x1404e78b5
004E78A1  B9 03 00 00 00                  mov ecx, 3
004E78A6  CD 29                           int 0x29
004E78A8  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
004E78AD  48 8B 1B                        mov rbx, qword ptr [rbx]
004E78B0  E9 72 FF FF FF                  jmp 0x1404e7827
004E78B5  48 89 10                        mov qword ptr [rax], rdx
004E78B8  48 89 48 08                     mov qword ptr [rax + 8], rcx
004E78BC  48 89 42 08                     mov qword ptr [rdx + 8], rax
004E78C0  48 89 01                        mov qword ptr [rcx], rax
004E78C3  48 89 7E 38                     mov qword ptr [rsi + 0x38], rdi
004E78C7  48 8B CF                        mov rcx, rdi
004E78CA  E8 1D DE F3 FF                  call 0x1404256ec
004E78CF  45 33 ED                        xor r13d, r13d
004E78D2  44 38 AC 24 E8 01 00 00         cmp byte ptr [rsp + 0x1e8], r13b
004E78DA  74 13                           je 0x1404e78ef
004E78DC  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
004E78E1  49 8B 4F 30                     mov rcx, qword ptr [r15 + 0x30]
004E78E5  BA 44 66 6C 74                  mov edx, 0x746c6644
004E78EA  E8 21 8E D2 FF                  call 0x140210710
004E78EF  41 BF 07 00 00 00               mov r15d, 7
004E78F5  41 8B CF                        mov ecx, r15d
004E78F8  E8 83 C4 D8 FF                  call 0x140273d80
004E78FD  88 46 45                        mov byte ptr [rsi + 0x45], al
004E7900  44 38 6E 44                     cmp byte ptr [rsi + 0x44], r13b
004E7904  74 0C                           je 0x1404e7912
004E7906  B2 01                           mov dl, 1
004E7908  48 8B CE                        mov rcx, rsi
004E790B  E8 70 AA 09 00                  call 0x140582380
004E7910  EB 16                           jmp 0x1404e7928
004E7912  48 8D 05 D7 B1 09 00            lea rax, [rip + 0x9b1d7]
004E7919  48 87 46 68                     xchg qword ptr [rsi + 0x68], rax
004E791D  8A 56 45                        mov dl, byte ptr [rsi + 0x45]
004E7920  49 8B CF                        mov rcx, r15
004E7923  E8 18 AC D8 FF                  call 0x140272540
004E7928  41 B5 01                        mov r13b, 1
004E792B  BB 03 01 00 00                  mov ebx, 0x103
004E7930  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
004E7934  45 33 D2                        xor r10d, r10d
004E7937  45 84 ED                        test r13b, r13b
004E793A  75 19                           jne 0x1404e7955
004E793C  BB E2 00 00 C0                  mov ebx, 0xc00000e2
004E7941  89 5E 30                        mov dword ptr [rsi + 0x30], ebx
004E7944  B2 01                           mov dl, 1
004E7946  48 8B CE                        mov rcx, rsi
004E7949  E8 72 3C DB FF                  call 0x14029b5c0
004E794E  45 33 D2                        xor r10d, r10d
004E7951  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
004E7955  44 38 54 24 44                  cmp byte ptr [rsp + 0x44], r10b
004E795A  74 0F                           je 0x1404e796b
004E795C  45 3B F4                        cmp r14d, r12d
004E795F  74 0A                           je 0x1404e796b
004E7961  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
004E7966  E8 35 8A D6 FF                  call 0x1402503a0
004E796B  8B C3                           mov eax, ebx
004E796D  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
004E7975  48 33 CC                        xor rcx, rsp
004E7978  E8 C3 4C 1C 00                  call 0x1406ac640
004E797D  48 81 C4 80 01 00 00            add rsp, 0x180
004E7984  41 5F                           pop r15
004E7986  41 5E                           pop r14
004E7988  41 5D                           pop r13
004E798A  41 5C                           pop r12
004E798C  5F                              pop rdi
004E798D  5E                              pop rsi
004E798E  5B                              pop rbx
004E798F  C3                              ret
004E7990  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlpRequestShareableOplock(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, unsigned __int8 a6, unsigned __int8 a7, unsigned int a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int8 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int8 v_stack_m173;
    unsigned __int8 v_stack_m174;
    unsigned int v_stack_m178;
    unsigned __int8 v_stack_m180;
    unsigned __int16 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
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
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;

    v_rsp = (v_rsp) - (384);
    result = (*(unsigned __int64 *)(v_rip + 9582686)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m170 = a2;
    v_stack_m148 = a4;
    v_stack_m168 = a5;
    v_r10 = 0;
    v_stack_m178 = 0;
    v_stack_m158 = 0;
    v_stack_m140 = 0;
    v_stack_m174 = 0;
    v_stack_m173 = 0;
    v_stack_m160 = 0;
    result = a5;
    v_rdi = *(unsigned __int64 *)(a1);
    if (*(unsigned __int64 *)(a1) == 0) {
        result = FsRtlpAllocateOplock(a1, a2, a3, a4);
        v_rdi = result;
        *(unsigned __int64 *)(a1) = result;
        v_r10 = 0;
    }
    if (a7 != 0) goto loc_004E6F7A;
    if (((unsigned int)((unsigned int)(a4))) != ((unsigned int)((unsigned int)(0x10000ULL)))) {
        result = *(unsigned __int64 *)(v_rdi + 152);
        v_stack_m140 = result;
        a1 = result;
        result = ExAcquireFastMutexUnsafe(a1, a2, a3, a4);
        v_stack_m174 = 1;
        v_r10 = 0;
    }
    if ((((unsigned int)((unsigned int)(0x10000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 144))))) == 0) goto loc_004E70D7;
    if ((*(unsigned __int8 *)(v_stack_m170)) != 13) goto loc_004E70D7;
    result = FsRtlpCallerIsAtomicRequestor(v_rdi, *(unsigned __int64 *)(v_stack_m170 + 48), v_stack_m158, a4);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_004E70D7;
    if (condition_is_above_or_equal) goto loc_004E702F;
    result = FsRtlpOplockDequeueRH(v_stack_m158, *(unsigned __int64 *)(v_stack_m170 + 48), v_stack_m158, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m158 + 56) + 8)) != (v_stack_m158 + 56)) goto loc_004E7028;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m158 + 56 + 8))) != (v_stack_m158 + 56)) goto loc_004E7028;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m158 + 56 + 8)) = *(unsigned __int64 *)(v_stack_m158 + 56);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m158 + 56) + 8) = *(unsigned __int64 *)(v_stack_m158 + 56 + 8);
    if ((*(unsigned __int64 *)(v_rdi + 120)) == (v_rdi + 120)) {
    }
    result = v_rdi + 120;
    if ((*(unsigned __int64 *)(v_stack_m158 + 40)) != 0) {
        a2 = v_stack_m158;
        a1 = v_rdi;
        result = FsRtlpClearOwner(a1, a2, v_stack_m158, v_stack_m158 + 56);
    }
    result = FsRtlpFreeRHOpContext(v_stack_m158, 1, v_stack_m158, v_stack_m158 + 56);
    v_r13 = 0;
    v_stack_m158 = 0;
    result = FsRtlpComputeShareableOplockState(v_rdi, 1, v_stack_m158, v_stack_m158 + 56);
    goto loc_004E793C;
loc_004E7028:
loc_004E702F:
loc_004E7037:
    if ((*(unsigned __int64 *)(v_rdi + 88)) == (v_rdi + 88)) goto loc_004E705F;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rdi + 88) + 53)) == 0) goto loc_004E704E;
    v_r15 = *(unsigned __int64 *)(v_rdi + 88);
    if (((unsigned int)((unsigned int)(a4))) != 0x3000ULL) {
        v_r15 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 88) + 8);
        result = FsRtlpRemoveAndCompleteWaitingIrp(*(unsigned __int64 *)(v_rdi + 88), 1, v_stack_m158, v_stack_m158 + 56);
        v_r10 = 0;
    }
    goto loc_004E7037;
loc_004E705F:
    result = FsRtlpOplockDequeueRH(v_stack_m158, 1, v_stack_m158, v_stack_m158 + 56);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m158 + 56) + 8)) != (v_stack_m158 + 56)) goto loc_004E713D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m158 + 56 + 8))) != (v_stack_m158 + 56)) goto loc_004E713D;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m158 + 56 + 8)) = *(unsigned __int64 *)(v_stack_m158 + 56);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m158 + 56) + 8) = *(unsigned __int64 *)(v_stack_m158 + 56 + 8);
    if ((*(unsigned __int64 *)(v_rdi + 120)) == (v_rdi + 120)) {
    }
    result = v_rdi + 120;
    if ((*(unsigned __int64 *)(v_stack_m158 + 40)) != 0) {
        a2 = v_stack_m158;
        a1 = v_rdi;
        result = FsRtlpClearOwner(a1, a2, v_stack_m158, v_stack_m158 + 56);
    }
    result = FsRtlpFreeRHOpContext(v_stack_m158, 1, v_stack_m158, v_stack_m158 + 56);
    v_r13 = 0;
    v_stack_m158 = 0;
    result = FsRtlpComputeShareableOplockState(v_rdi, 1, v_stack_m158, v_stack_m158 + 56);
    v_r10 = 0;
loc_004E70D7:
    result = FsRtlpOplockUpperLowerCompatible((unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(a8), v_stack_m158, v_stack_m158 + 56);
    if ((unsigned __int8)(result) == 0) goto loc_004E793C;
    if ((((unsigned int)((unsigned int)(0x1000ULL))) & ((unsigned int)((unsigned int)(a4)))) != 0) goto loc_004E7108;
    if (((unsigned int)((unsigned int)(a4))) != ((unsigned int)((unsigned int)(0x10000ULL)))) goto loc_004E723E;
loc_004E7108:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 48) + 40) == 0) goto loc_004E7243;
    result = MmDoesFileHaveUserWritableReferences(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m170 + 48) + 40), (unsigned int)(a8), v_stack_m170, (unsigned int)(0x1000ULL));
    v_r10 = 0;
    if ((unsigned int)(result) == 0) goto loc_004E7238;
    if (((unsigned int)((unsigned int)(a4))) != ((unsigned int)((unsigned int)(0x10000ULL)))) goto loc_004E7144;
    goto loc_004E7951;
loc_004E713D:
loc_004E7144:
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 8) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 12))) | (4));
    *(unsigned int *)(*(unsigned __int64 *)(a3 + 24) + 12) = (unsigned int)(result);
    if ((*(unsigned int *)(v_rip + 9566958)) <= 5) goto loc_004E793C;
    result = tlgKeywordOn(v_rip + 9566935, (unsigned int)(a8), 4, (unsigned int)(0x1000ULL));
    if ((unsigned __int8)(result) == 0) goto loc_004E793C;
    v_stack_m130 = 1;
    v_stack_mE8 = v_stack_m130;
    v_stack_mE0 = 8;
    v_stack_m150 = (unsigned int)((unsigned int)(a4));
    v_stack_mD8 = v_stack_m150;
    v_stack_mD0 = 4;
    v_stack_m168 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 144)));
    v_stack_mC8 = v_stack_m168;
    v_stack_mC0 = 4;
    v_stack_m128 = 0x1000000ULL;
    v_stack_mB8 = v_stack_m128;
    v_stack_mB0 = 8;
    v_stack_m198 = v_stack_m108;
    result = tlgWriteAgg(v_rip + 9566754, v_rip - 4857447, 4, 4 + 2);
    goto loc_004E793C;
loc_004E7238:
loc_004E723E:
loc_004E7243:
    if (a7 != 0) goto loc_004E726B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 144)))) & (64)) == 0) goto loc_004E726B;
loc_004E7258:
    if (((unsigned int)((unsigned int)(a4))) != ((unsigned int)((unsigned int)(0x10000ULL)))) goto loc_004E793C;
    goto loc_004E7951;
loc_004E726B:
    if (((unsigned int)((unsigned int)(a4))) == 16) goto loc_004E770E;
    if (((unsigned int)((unsigned int)(a4))) == ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_004E7732;
    if (((unsigned int)((unsigned int)(a4))) == ((unsigned int)((unsigned int)(0x3000ULL)))) goto loc_004E728C;
    if (((unsigned int)((unsigned int)(a4))) != ((unsigned int)((unsigned int)(0x10000ULL)))) goto loc_004E7937;
loc_004E728C:
    if (a7 != 0) goto loc_004E72C6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 144)))) & (1)) != 0) goto loc_004E72C6;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 144))))) & (0x1F0FFDFULL));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_004E72C6;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x3000ULL)))) goto loc_004E72C6;
    if (((unsigned int)(result)) == 0xB000ULL) goto loc_004E72C6;
    if (((unsigned int)(result)) == 0x103000ULL) goto loc_004E72C6;
    if (((unsigned int)(result)) == 0x803000ULL) goto loc_004E72C6;
    if ((((unsigned int)((unsigned int)(0x10000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 144))))) == 0) goto loc_004E7258;
loc_004E72C6:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m170 + 48) + 73)) != 0) goto loc_004E7258;
    if (a7 != 0) goto loc_004E742C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 144))) & (0x1F0FFDFULL));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_004E72EF;
    if (((unsigned int)(result)) != 0xB000ULL) goto loc_004E7346;
loc_004E72EF:
loc_004E72F3:
    if ((*(unsigned __int64 *)(v_rdi + 40)) == (v_rdi + 40)) goto loc_004E7346;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_m170 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 40) + 16) + 48), a3, (unsigned int)(0x1000ULL));
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_004E7403;
    if (((unsigned int)((unsigned int)(a4))) != ((unsigned int)((unsigned int)(0x10000ULL)))) goto loc_004E732A;
loc_004E7320:
    goto loc_004E7951;
loc_004E732A:
    result = FsRtlpRemoveAndCompleteReadOnlyIrp(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC00000E3ULL) + 8)), 533, (unsigned int)((unsigned int)((unsigned int)(0x3000ULL))), v_rdi);
loc_004E7346:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 144))) & (0x1F0FFDFULL));
    result = (unsigned int)((result) - ((unsigned int)((unsigned int)(0x3000ULL))));
    if ((((unsigned int)(result)) & (0xFFFF7FFFULL)) != 0) goto loc_004E73BF;
loc_004E735F:
    if ((*(unsigned __int64 *)(v_rdi + 56)) == (v_rdi + 56)) goto loc_004E73BF;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_m170 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 56) + 24), a3, v_rdi);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_004E7410;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 56) + 56)) != 0) goto loc_004E7410;
    if (((unsigned int)((unsigned int)(a4))) == ((unsigned int)((unsigned int)(0x10000ULL)))) goto loc_004E7320;
    v_stack_m180 = 0;
    v_stack_m188 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = 0;
    result = FsRtlpRemoveAndCompleteRHIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 56) + 8)), v_rdi, 533, (unsigned int)((unsigned int)((unsigned int)(0x3000ULL))));
loc_004E73BF:
    if ((*(unsigned __int64 *)(v_rdi + 72)) == (v_rdi + 72)) goto loc_004E7422;
loc_004E73D0:
    if ((*(unsigned __int64 *)(v_rdi + 72)) == (v_rdi + 72)) goto loc_004E7429;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_m170 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 72) + 24), a3, (unsigned int)((unsigned int)((unsigned int)(0x3000ULL))));
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_004E741D;
    if (((unsigned int)((unsigned int)(a4))) == ((unsigned int)((unsigned int)(0x10000ULL)))) goto loc_004E7951;
    goto loc_004E7941;
loc_004E7403:
    goto loc_004E72F3;
loc_004E7410:
    goto loc_004E735F;
loc_004E741D:
    goto loc_004E73D0;
loc_004E7422:
    goto loc_004E742C;
loc_004E7429:
loc_004E742C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m168) + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m168) + 24) = *(unsigned __int64 *)(v_stack_m170 + 48);
    result = FsRtlpOplockEnqueueRH(v_rdi + 56, *(unsigned __int64 *)(v_stack_m168), v_stack_m170, (unsigned int)((unsigned int)((unsigned int)(0x3000ULL))));
    v_stack_m178 = (unsigned int)(result);
    v_r10 = 0;
    if (!sign_flag) goto loc_004E748A;
    if (((unsigned int)((unsigned int)(a4))) == ((unsigned int)((unsigned int)(0x10000ULL)))) goto loc_004E7955;
    *(unsigned int *)(a3 + 48) = (unsigned int)(result);
    result = IofCompleteRequest(0, 1, v_stack_m170, (unsigned int)((unsigned int)((unsigned int)(0x3000ULL))));
loc_004E7482:
    v_r10 = 0;
    goto loc_004E7955;
loc_004E748A:
    v_stack_m138 = 0;
    if (((unsigned int)((unsigned int)(a4))) != ((unsigned int)((unsigned int)(0x10000ULL)))) goto loc_004E74D7;
    result = (*(unsigned __int64 *)(v_stack_m168)) + (56);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 120) + 8)) != (v_rdi + 120)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(v_rdi + 120);
    *(unsigned __int64 *)(result + 8) = a1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 120) + 8) = result;
    *(unsigned __int64 *)(a1) = result;
    v_stack_m178 = 0;
    goto loc_004E75A9;
loc_004E74D7:
    v_stack_m118 = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m168) + 40) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m168) + 40), (unsigned int)(0x746C6644ULL), v_stack_m170, (unsigned int)((unsigned int)((unsigned int)(0x3000ULL))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m168) + 16) = 0;
    v_stack_m178 = 259;
    result = 0;
    *(unsigned int *)(a3 + 48) = 0;
    *(unsigned __int64 *)(a3 + 56) = v_rdi;
    if (a6 != 0) {
        result = *(unsigned __int64 *)(v_stack_m168);
        a1 = *(unsigned __int64 *)(result + 24);
        a2 = 0x746C6644ULL;
        result = ObfReferenceObjectWithTag(a1, a2, v_stack_m170, (unsigned int)((unsigned int)((unsigned int)(0x3000ULL))));
    }
    result = KeAcquireQueuedSpinLock(7, a2, v_stack_m170, (unsigned int)((unsigned int)((unsigned int)(0x3000ULL))));
    *(unsigned __int8 *)(a3 + 69) = (unsigned __int8)(result);
    result = 0;
    if ((*(unsigned __int8 *)(a3 + 68)) == 0) goto loc_004E7587;
    if (a6 == 0) goto loc_004E7570;
    if (a7 == 0) {
        a3 = 1;
    }
    result = FsRtlpCancelOplockRHIrp(a3, 1, a3, (unsigned int)((unsigned int)((unsigned int)(0x3000ULL))));
    goto loc_004E75AC;
loc_004E7587:
    result = KeReleaseQueuedSpinLock(v_stack_m138, *(unsigned __int8 *)(a3 + 69), a3, (unsigned int)((unsigned int)((unsigned int)(0x3000ULL))));
loc_004E75A9:
loc_004E75AC:
    if ((*(unsigned int *)(v_rip + 9565853)) >= = 5) {
        v_stack_m14C = (unsigned int)((unsigned int)(a4));
        result = v_stack_m14C;
        v_stack_m88 = result;
        v_stack_m80 = 4;
        result = a7;
        v_stack_m173 = (unsigned __int8)(result);
        result = v_stack_m173;
        v_stack_m78 = result;
        v_stack_m70 = 1;
        v_stack_m120 = v_rdi;
        result = v_stack_m120;
        v_stack_m68 = result;
        v_stack_m60 = 8;
        result = *(unsigned int *)(v_rdi + 144);
        v_stack_m170 = (unsigned int)(result);
        result = v_stack_m170;
        v_stack_m58 = result;
        v_stack_m50 = 4;
        result = v_stack_mA8;
        v_stack_m190 = result;
        v_stack_m198 = 6;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4858636;
        a1 = v_rip + 9565669;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    result = FsRtlpComputeShareableOplockState(v_rdi, a2, a3, a4);
    result = Feature_3244801339__private_IsEnabledDeviceUsageNoInline(v_rdi, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_004E76AA;
    if (1 != 0) {
        result = v_stack_m168;
        a2 = *(unsigned __int64 *)(result);
        result = a2 + 88;
        a4 = a2 + 72;
        v_stack_m198 = result;
        a3 = 0;
        a2 = *(unsigned __int64 *)(a2 + 24);
        a1 = v_rdi;
        result = FsRtlpOplockTryPrepForAckTimeout(a1, a2, a3, a4);
    }
    result = Feature_3244801339__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    a1 = 0;
    v_r15 = v_stack_m138;
    if ((unsigned int)(result) != 0) {
        v_r15 = *(unsigned __int64 *)(v_stack_m168);
    }
    *(unsigned __int64 *)(v_stack_m168) = 0;
    result = v_stack_m168;
    if (((unsigned int)((unsigned int)(a4))) == ((unsigned int)((unsigned int)(0x10000ULL)))) {
        result = *(unsigned int *)(v_rdi + 144);
        result = (unsigned int)((result) | ((unsigned int)((unsigned int)(0x10000ULL))));
        *(unsigned int *)(v_rdi + 144) = (unsigned int)(result);
    }
    result = Feature_3244801339__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    v_r10 = 0;
    if ((unsigned int)(result) == 0) goto loc_004E7955;
    if (1 == 0) goto loc_004E7955;
    v_stack_m198 = v_r15 + 88;
    result = FsRtlpOplockTryPrepForAckTimeout(v_rdi, *(unsigned __int64 *)(v_r15 + 24), a3, v_r15 + 72);
    goto loc_004E7482;
loc_004E770E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 144)))) & (1)) != 0) goto loc_004E7732;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 144))) & (0x1F0FFDFULL));
    if (((unsigned int)(result)) == 16) goto loc_004E7732;
    if (((unsigned int)(result)) == ((unsigned int)(v_r15 + 72))) goto loc_004E7732;
    if (((unsigned int)(result)) != 0x1010ULL) goto loc_004E793C;
loc_004E7732:
    if ((unsigned __int8)(*(unsigned __int64 *)(v_r15 + 24)) != 0) goto loc_004E787E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 144)))) & (1)) != 0) goto loc_004E7780;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 144))))) & (0x1F0FFDFULL));
    if (((unsigned int)(result)) == 16) goto loc_004E7780;
    if (((unsigned int)(result)) == ((unsigned int)(v_r15 + 72))) goto loc_004E7780;
    if (((unsigned int)(result)) == 0x1010ULL) goto loc_004E7780;
    if (((unsigned int)(result)) == ((unsigned int)(v_r15))) goto loc_004E7780;
    if (((unsigned int)(result)) == 0xB000ULL) goto loc_004E7780;
    if (((unsigned int)(result)) == 0x103000ULL) goto loc_004E7780;
    if (((unsigned int)(result)) == 0x803000ULL) goto loc_004E7780;
    if ((((unsigned int)((unsigned int)(0x10000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 144))))) == 0) goto loc_004E793C;
loc_004E7780:
    if ((unsigned __int8)(*(unsigned __int64 *)(v_r15 + 24)) != 0) goto loc_004E787E;
    if ((*(unsigned __int64 *)(v_rdi + 56)) != (v_rdi + 56)) goto loc_004E779D;
    if ((*(unsigned __int64 *)(v_rdi + 72)) == (v_rdi + 72)) goto loc_004E7800;
loc_004E779D:
    if ((*(unsigned __int64 *)(v_rdi + 56)) == (v_rdi + 56)) goto loc_004E77C8;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(a3 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 56) + 24), a3, v_r15 + 72);
    if ((unsigned __int8)(result) != 0) goto loc_004E793C;
    goto loc_004E779D;
loc_004E77C8:
loc_004E77CC:
    if ((*(unsigned __int64 *)(v_rdi + 72)) == (v_rdi + 72)) goto loc_004E77F7;
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_m170 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 72) + 24), a3, v_r15 + 72);
    if ((unsigned __int8)(result) != 0) goto loc_004E793C;
    goto loc_004E77CC;
loc_004E77F7:
    v_r10 = 0;
loc_004E7800:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 144))) & (0x1F0FFDFULL));
    if (((unsigned int)(result)) == 16) goto loc_004E7823;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_004E7823;
    if (((unsigned int)(result)) == 0x1010ULL) goto loc_004E7823;
    if (((unsigned int)(result)) != 0xB000ULL) goto loc_004E787E;
loc_004E7823:
loc_004E7827:
    if ((*(unsigned __int64 *)(v_rdi + 40)) == (v_rdi + 40)) goto loc_004E787B;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 40) + 16) + 24)) == 0x90240ULL) goto loc_004E784A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 40) + 16) + 48)) == (*(unsigned __int64 *)(v_stack_m170 + 48))) goto loc_004E78AD;
loc_004E784A:
    a3 = 0;
    result = FsRtlpOplockKeysEqual(*(unsigned __int64 *)(v_stack_m170 + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 40) + 16) + 48), a3, (unsigned int)(0x1000ULL));
    if ((unsigned __int8)(result) == 0) goto loc_004E78A8;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (0x7000ULL));
    result = FsRtlpRemoveAndCompleteReadOnlyIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 40) + 8)), 533, a3, v_rdi);
loc_004E787B:
    v_r10 = 0;
loc_004E787E:
    *(unsigned int *)(a3 + 48) = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 40) + 8)) == (v_rdi + 40)) goto loc_004E78B5;
loc_004E78A8:
loc_004E78AD:
    goto loc_004E7827;
loc_004E78B5:
    *(unsigned __int64 *)(a3 + 168) = *(unsigned __int64 *)(v_rdi + 40);
    *(unsigned __int64 *)(a3 + 168 + 8) = 3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 40) + 8) = a3 + 168;
    *(unsigned __int64 *)(3) = a3 + 168;
    *(unsigned __int64 *)(a3 + 56) = v_rdi;
    result = FsRtlpComputeShareableOplockState(v_rdi, *(unsigned __int64 *)(v_rdi + 40), v_stack_m170, v_rdi);
    v_r13 = 0;
    if (a6 != 0) {
        v_r15 = v_stack_m170;
        a1 = *(unsigned __int64 *)(v_r15 + 48);
        a2 = 0x746C6644ULL;
        result = ObfReferenceObjectWithTag(a1, a2, v_stack_m170, v_rdi);
    }
    result = KeAcquireQueuedSpinLock(7, a2, v_stack_m170, v_rdi);
    *(unsigned __int8 *)(a3 + 69) = (unsigned __int8)(result);
    if ((*(unsigned __int8 *)(a3 + 68)) == 0) goto loc_004E7912;
    result = FsRtlpCancelReadOnlyOplockIrp(a3, 1, v_stack_m170, v_rdi);
    goto loc_004E7928;
loc_004E7912:
    result = KeReleaseQueuedSpinLock(7, *(unsigned __int8 *)(a3 + 69), v_stack_m170, v_rdi);
loc_004E7928:
    v_stack_m178 = 259;
    v_r10 = 0;
loc_004E7937:
    if (1 != 0) goto loc_004E7955;
loc_004E793C:
loc_004E7941:
    *(unsigned int *)(a3 + 48) = (unsigned int)((unsigned int)(0xC00000E2ULL));
    result = IofCompleteRequest(a3, 1, v_stack_m170, v_rdi);
    v_r10 = 0;
loc_004E7951:
    v_stack_m178 = (unsigned int)((unsigned int)(0xC00000E2ULL));
loc_004E7955:
    if (v_stack_m174 == 0) goto loc_004E796B;
    if (((unsigned int)((unsigned int)(a4))) != ((unsigned int)((unsigned int)(0x10000ULL)))) {
        a1 = v_stack_m140;
        result = ExReleaseFastMutexUnsafe(a1, 1, v_stack_m170, v_rdi);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, v_stack_m170, v_rdi);
    v_rsp = (v_rsp) + (384);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlpRequestShareableOplock(void *Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, int64_t Arg5, uint8_t Arg6, uint8_t Arg7, uint32_t Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint8_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint8_t v_stack_m173;
    uint8_t v_stack_m174;
    uint32_t v_stack_m178;
    uint8_t v_stack_m180;
    uint16_t v_stack_m188;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
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
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;

    local_rsp = (local_rsp) - (384);
    result = (*(uint64_t *)(v_rip + 0x92385E)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m170 = Arg2;
    v_stack_m148 = Arg4;
    v_stack_m168 = Arg5;
    local_r10 = 0;
    v_stack_m178 = 0;
    v_stack_m158 = 0;
    v_stack_m140 = 0;
    v_stack_m174 = 0;
    v_stack_m173 = 0;
    v_stack_m160 = 0;
    result = Arg5;
    local_rdi = *(uint64_t *)(arg1);
    if (*(uint64_t *)(arg1) == 0) {
        result = FsRtlpAllocateOplock(Arg1, Arg2, Arg3, Arg4);
        local_rdi = result;
        *(uint64_t *)(arg1) = result;
        local_r10 = 0;
    }
    if (Arg7 != 0) goto loc_004E6F7A;
    if (((uint32_t)((uint32_t)(Arg4))) != ((uint32_t)((uint32_t)(0x10000ULL)))) {
        result = *(uint64_t *)(local_rdi + 0x98);
        v_stack_m140 = result;
        Arg1 = result;
        result = ExAcquireFastMutexUnsafe(Arg1, Arg2, Arg3, Arg4);
        v_stack_m174 = 1;
        local_r10 = 0;
    }
    if ((((uint32_t)((uint32_t)(0x10000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x90))))) == 0) goto loc_004E70D7;
    if ((*(uint8_t *)(v_stack_m170)) != 13) goto loc_004E70D7;
    result = FsRtlpCallerIsAtomicRequestor(local_rdi, *(uint64_t *)(v_stack_m170 + 0x30), v_stack_m158, Arg4);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_004E70D7;
    if (condition_is_above_or_equal) goto loc_004E702F;
    result = FsRtlpOplockDequeueRH(v_stack_m158, *(uint64_t *)(v_stack_m170 + 0x30), v_stack_m158, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m158 + 0x38) + 0x8)) != (v_stack_m158 + 56)) goto loc_004E7028;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m158 + 0x38 + 0x8))) != (v_stack_m158 + 56)) goto loc_004E7028;
    *(uint64_t *)(*(uint64_t *)(v_stack_m158 + 0x38 + 0x8)) = *(uint64_t *)(v_stack_m158 + 0x38);
    *(uint64_t *)(*(uint64_t *)(v_stack_m158 + 0x38) + 0x8) = *(uint64_t *)(v_stack_m158 + 0x38 + 0x8);
    if ((*(uint64_t *)(local_rdi + 0x78)) == (local_rdi + 120)) {
    }
    result = local_rdi + 120;
    if ((*(uint64_t *)(v_stack_m158 + 0x28)) != 0) {
        Arg2 = v_stack_m158;
        Arg1 = local_rdi;
        result = FsRtlpClearOwner(Arg1, Arg2, v_stack_m158, v_stack_m158 + 56);
    }
    result = FsRtlpFreeRHOpContext(v_stack_m158, 1, v_stack_m158, v_stack_m158 + 56);
    local_r13 = 0;
    v_stack_m158 = 0;
    result = FsRtlpComputeShareableOplockState(local_rdi, 1, v_stack_m158, v_stack_m158 + 56);
    goto loc_004E793C;
loc_004E7028:
loc_004E702F:
loc_004E7037:
    if ((*(uint64_t *)(local_rdi + 0x58)) == (local_rdi + 88)) goto loc_004E705F;
    if ((*(uint8_t *)(*(uint64_t *)(local_rdi + 0x58) + 0x35)) == 0) goto loc_004E704E;
    local_r15 = *(uint64_t *)(local_rdi + 0x58);
    if (((uint32_t)((uint32_t)(Arg4))) != 0x3000ULL) {
        local_r15 = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x58) + 0x8);
        result = FsRtlpRemoveAndCompleteWaitingIrp(*(uint64_t *)(local_rdi + 0x58), 1, v_stack_m158, v_stack_m158 + 56);
        local_r10 = 0;
    }
    goto loc_004E7037;
loc_004E705F:
    result = FsRtlpOplockDequeueRH(v_stack_m158, 1, v_stack_m158, v_stack_m158 + 56);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m158 + 0x38) + 0x8)) != (v_stack_m158 + 56)) goto loc_004E713D;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m158 + 0x38 + 0x8))) != (v_stack_m158 + 56)) goto loc_004E713D;
    *(uint64_t *)(*(uint64_t *)(v_stack_m158 + 0x38 + 0x8)) = *(uint64_t *)(v_stack_m158 + 0x38);
    *(uint64_t *)(*(uint64_t *)(v_stack_m158 + 0x38) + 0x8) = *(uint64_t *)(v_stack_m158 + 0x38 + 0x8);
    if ((*(uint64_t *)(local_rdi + 0x78)) == (local_rdi + 120)) {
    }
    result = local_rdi + 120;
    if ((*(uint64_t *)(v_stack_m158 + 0x28)) != 0) {
        Arg2 = v_stack_m158;
        Arg1 = local_rdi;
        result = FsRtlpClearOwner(Arg1, Arg2, v_stack_m158, v_stack_m158 + 56);
    }
    result = FsRtlpFreeRHOpContext(v_stack_m158, 1, v_stack_m158, v_stack_m158 + 56);
    local_r13 = 0;
    v_stack_m158 = 0;
    result = FsRtlpComputeShareableOplockState(local_rdi, 1, v_stack_m158, v_stack_m158 + 56);
    local_r10 = 0;
loc_004E70D7:
    result = FsRtlpOplockUpperLowerCompatible((uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(Arg8), v_stack_m158, v_stack_m158 + 56);
    if ((uint8_t)(result) == 0) goto loc_004E793C;
    if ((((uint32_t)((uint32_t)(0x1000ULL))) & ((uint32_t)((uint32_t)(Arg4)))) != 0) goto loc_004E7108;
    if (((uint32_t)((uint32_t)(Arg4))) != ((uint32_t)((uint32_t)(0x10000ULL)))) goto loc_004E723E;
loc_004E7108:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x30) + 0x28) == 0) goto loc_004E7243;
    result = MmDoesFileHaveUserWritableReferences(*(uint64_t *)(*(uint64_t *)(v_stack_m170 + 0x30) + 0x28), (uint32_t)(Arg8), v_stack_m170, (uint32_t)(0x1000ULL));
    local_r10 = 0;
    if ((uint32_t)(result) == 0) goto loc_004E7238;
    if (((uint32_t)((uint32_t)(Arg4))) != ((uint32_t)((uint32_t)(0x10000ULL)))) goto loc_004E7144;
    goto loc_004E7951;
loc_004E713D:
loc_004E7144:
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0x8) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0xC))) | (4));
    *(uint32_t *)(*(uint64_t *)(arg3 + 0x18) + 0xC) = (uint32_t)(result);
    if ((*(uint32_t *)(v_rip + 0x91FAEE)) <= 5) goto loc_004E793C;
    result = tlgKeywordOn(v_rip + 9566935, (uint32_t)(Arg8), 4, (uint32_t)(0x1000ULL));
    if ((uint8_t)(result) == 0) goto loc_004E793C;
    v_stack_m130 = 1;
    v_stack_mE8 = v_stack_m130;
    v_stack_mE0 = 8;
    v_stack_m150 = (uint32_t)((uint32_t)(Arg4));
    v_stack_mD8 = v_stack_m150;
    v_stack_mD0 = 4;
    v_stack_m168 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x90)));
    v_stack_mC8 = v_stack_m168;
    v_stack_mC0 = 4;
    v_stack_m128 = 0x1000000ULL;
    v_stack_mB8 = v_stack_m128;
    v_stack_mB0 = 8;
    v_stack_m198 = v_stack_m108;
    result = tlgWriteAgg(v_rip + 9566754, v_rip - 4857447, 4, 4 + 2);
    goto loc_004E793C;
loc_004E7238:
loc_004E723E:
loc_004E7243:
    if (Arg7 != 0) goto loc_004E726B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x90)))) & (64)) == 0) goto loc_004E726B;
loc_004E7258:
    if (((uint32_t)((uint32_t)(Arg4))) != ((uint32_t)((uint32_t)(0x10000ULL)))) goto loc_004E793C;
    goto loc_004E7951;
loc_004E726B:
    if (((uint32_t)((uint32_t)(Arg4))) == 16) goto loc_004E770E;
    if (((uint32_t)((uint32_t)(Arg4))) == ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_004E7732;
    if (((uint32_t)((uint32_t)(Arg4))) == ((uint32_t)((uint32_t)(0x3000ULL)))) goto loc_004E728C;
    if (((uint32_t)((uint32_t)(Arg4))) != ((uint32_t)((uint32_t)(0x10000ULL)))) goto loc_004E7937;
loc_004E728C:
    if (Arg7 != 0) goto loc_004E72C6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x90)))) & (1)) != 0) goto loc_004E72C6;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x90))))) & (0x1F0FFDFULL));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_004E72C6;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x3000ULL)))) goto loc_004E72C6;
    if (((uint32_t)(result)) == 0xB000ULL) goto loc_004E72C6;
    if (((uint32_t)(result)) == 0x103000ULL) goto loc_004E72C6;
    if (((uint32_t)(result)) == 0x803000ULL) goto loc_004E72C6;
    if ((((uint32_t)((uint32_t)(0x10000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x90))))) == 0) goto loc_004E7258;
loc_004E72C6:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m170 + 0x30) + 0x49)) != 0) goto loc_004E7258;
    if (Arg7 != 0) goto loc_004E742C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x90))) & (0x1F0FFDFULL));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_004E72EF;
    if (((uint32_t)(result)) != 0xB000ULL) goto loc_004E7346;
loc_004E72EF:
loc_004E72F3:
    if ((*(uint64_t *)(local_rdi + 0x28)) == (local_rdi + 40)) goto loc_004E7346;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_m170 + 0x30), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0x28) + 0x10) + 0x30), Arg3, (uint32_t)(0x1000ULL));
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_004E7403;
    if (((uint32_t)((uint32_t)(Arg4))) != ((uint32_t)((uint32_t)(0x10000ULL)))) goto loc_004E732A;
loc_004E7320:
    goto loc_004E7951;
loc_004E732A:
    result = FsRtlpRemoveAndCompleteReadOnlyIrp(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC00000E3ULL) + 0x8)), 533, (uint32_t)((uint32_t)((uint32_t)(0x3000ULL))), local_rdi);
loc_004E7346:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x90))) & (0x1F0FFDFULL));
    result = (uint32_t)((result) - ((uint32_t)((uint32_t)(0x3000ULL))));
    if ((((uint32_t)(result)) & (0xFFFF7FFFULL)) != 0) goto loc_004E73BF;
loc_004E735F:
    if ((*(uint64_t *)(local_rdi + 0x38)) == (local_rdi + 56)) goto loc_004E73BF;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_m170 + 0x30), *(uint64_t *)(*(uint64_t *)(local_rdi + 0x38) + 0x18), Arg3, local_rdi);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_004E7410;
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x38) + 0x38)) != 0) goto loc_004E7410;
    if (((uint32_t)((uint32_t)(Arg4))) == ((uint32_t)((uint32_t)(0x10000ULL)))) goto loc_004E7320;
    v_stack_m180 = 0;
    v_stack_m188 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = 0;
    result = FsRtlpRemoveAndCompleteRHIrp(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0x38) + 0x8)), local_rdi, 533, (uint32_t)((uint32_t)((uint32_t)(0x3000ULL))));
loc_004E73BF:
    if ((*(uint64_t *)(local_rdi + 0x48)) == (local_rdi + 72)) goto loc_004E7422;
loc_004E73D0:
    if ((*(uint64_t *)(local_rdi + 0x48)) == (local_rdi + 72)) goto loc_004E7429;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_m170 + 0x30), *(uint64_t *)(*(uint64_t *)(local_rdi + 0x48) + 0x18), Arg3, (uint32_t)((uint32_t)((uint32_t)(0x3000ULL))));
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_004E741D;
    if (((uint32_t)((uint32_t)(Arg4))) == ((uint32_t)((uint32_t)(0x10000ULL)))) goto loc_004E7951;
    goto loc_004E7941;
loc_004E7403:
    goto loc_004E72F3;
loc_004E7410:
    goto loc_004E735F;
loc_004E741D:
    goto loc_004E73D0;
loc_004E7422:
    goto loc_004E742C;
loc_004E7429:
loc_004E742C:
    *(uint64_t *)(*(uint64_t *)(v_stack_m168) + 0x20) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    *(uint64_t *)(*(uint64_t *)(v_stack_m168) + 0x18) = *(uint64_t *)(v_stack_m170 + 0x30);
    result = FsRtlpOplockEnqueueRH(local_rdi + 56, *(uint64_t *)(v_stack_m168), v_stack_m170, (uint32_t)((uint32_t)((uint32_t)(0x3000ULL))));
    v_stack_m178 = (uint32_t)(result);
    local_r10 = 0;
    if (!sign_flag) goto loc_004E748A;
    if (((uint32_t)((uint32_t)(Arg4))) == ((uint32_t)((uint32_t)(0x10000ULL)))) goto loc_004E7955;
    *(uint32_t *)(arg3 + 0x30) = (uint32_t)(result);
    result = IofCompleteRequest(0, 1, v_stack_m170, (uint32_t)((uint32_t)((uint32_t)(0x3000ULL))));
loc_004E7482:
    local_r10 = 0;
    goto loc_004E7955;
loc_004E748A:
    v_stack_m138 = 0;
    if (((uint32_t)((uint32_t)(Arg4))) != ((uint32_t)((uint32_t)(0x10000ULL)))) goto loc_004E74D7;
    result = (*(uint64_t *)(v_stack_m168)) + (56);
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x78) + 0x8)) != (local_rdi + 120)) {
        Arg1 = 3;
    }
    *(uint64_t *)(result) = *(uint64_t *)(local_rdi + 0x78);
    *(void **)(result + 0x8) = Arg1;
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x78) + 0x8) = result;
    *(uint64_t *)(arg1) = result;
    v_stack_m178 = 0;
    goto loc_004E75A9;
loc_004E74D7:
    v_stack_m118 = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(*(uint64_t *)(v_stack_m168) + 0x28) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = ObfReferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(v_stack_m168) + 0x28), (uint32_t)(0x746C6644ULL), v_stack_m170, (uint32_t)((uint32_t)((uint32_t)(0x3000ULL))));
    *(uint64_t *)(*(uint64_t *)(v_stack_m168) + 0x10) = 0;
    v_stack_m178 = 259;
    result = 0;
    *(uint32_t *)(arg3 + 0x30) = 0;
    *(uint64_t *)(arg3 + 0x38) = local_rdi;
    if (Arg6 != 0) {
        result = *(uint64_t *)(v_stack_m168);
        Arg1 = *(uint64_t *)(result + 0x18);
        Arg2 = 0x746C6644ULL;
        result = ObfReferenceObjectWithTag(Arg1, Arg2, v_stack_m170, (uint32_t)((uint32_t)((uint32_t)(0x3000ULL))));
    }
    result = KeAcquireQueuedSpinLock(7, Arg2, v_stack_m170, (uint32_t)((uint32_t)((uint32_t)(0x3000ULL))));
    *(uint8_t *)(arg3 + 0x45) = (uint8_t)(result);
    result = 0;
    if ((*(uint8_t *)(arg3 + 0x44)) == 0) goto loc_004E7587;
    if (Arg6 == 0) goto loc_004E7570;
    if (Arg7 == 0) {
        Arg3 = 1;
    }
    result = FsRtlpCancelOplockRHIrp(Arg3, 1, Arg3, (uint32_t)((uint32_t)((uint32_t)(0x3000ULL))));
    goto loc_004E75AC;
loc_004E7587:
    result = KeReleaseQueuedSpinLock(v_stack_m138, *(uint8_t *)(arg3 + 0x45), Arg3, (uint32_t)((uint32_t)((uint32_t)(0x3000ULL))));
loc_004E75A9:
loc_004E75AC:
    if ((*(uint32_t *)(v_rip + 0x91F69D)) >= = 5) {
        v_stack_m14C = (uint32_t)((uint32_t)(Arg4));
        result = v_stack_m14C;
        v_stack_m88 = result;
        v_stack_m80 = 4;
        result = Arg7;
        v_stack_m173 = (uint8_t)(result);
        result = v_stack_m173;
        v_stack_m78 = result;
        v_stack_m70 = 1;
        v_stack_m120 = local_rdi;
        result = v_stack_m120;
        v_stack_m68 = result;
        v_stack_m60 = 8;
        result = *(uint32_t *)(local_rdi + 0x90);
        v_stack_m170 = (uint32_t)(result);
        result = v_stack_m170;
        v_stack_m58 = result;
        v_stack_m50 = 4;
        result = v_stack_mA8;
        v_stack_m190 = result;
        v_stack_m198 = 6;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4858636;
        Arg1 = v_rip + 9565669;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    result = FsRtlpComputeShareableOplockState(local_rdi, Arg2, Arg3, Arg4);
    result = Feature_3244801339__private_IsEnabledDeviceUsageNoInline(local_rdi, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_004E76AA;
    if (1 != 0) {
        result = v_stack_m168;
        Arg2 = *(uint64_t *)(result);
        result = Arg2 + 88;
        Arg4 = Arg2 + 72;
        v_stack_m198 = result;
        Arg3 = 0;
        Arg2 = *(uint64_t *)(Arg2 + 0x18);
        Arg1 = local_rdi;
        result = FsRtlpOplockTryPrepForAckTimeout(Arg1, Arg2, Arg3, Arg4);
    }
    result = Feature_3244801339__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    Arg1 = 0;
    local_r15 = v_stack_m138;
    if ((uint32_t)(result) != 0) {
        local_r15 = *(uint64_t *)(v_stack_m168);
    }
    *(uint64_t *)(v_stack_m168) = 0;
    result = v_stack_m168;
    if (((uint32_t)((uint32_t)(Arg4))) == ((uint32_t)((uint32_t)(0x10000ULL)))) {
        result = *(uint32_t *)(local_rdi + 0x90);
        result = (uint32_t)((result) | ((uint32_t)((uint32_t)(0x10000ULL))));
        *(uint32_t *)(local_rdi + 0x90) = (uint32_t)(result);
    }
    result = Feature_3244801339__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    local_r10 = 0;
    if ((uint32_t)(result) == 0) goto loc_004E7955;
    if (1 == 0) goto loc_004E7955;
    v_stack_m198 = local_r15 + 88;
    result = FsRtlpOplockTryPrepForAckTimeout(local_rdi, *(uint64_t *)(local_r15 + 0x18), Arg3, local_r15 + 72);
    goto loc_004E7482;
loc_004E770E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x90)))) & (1)) != 0) goto loc_004E7732;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x90))) & (0x1F0FFDFULL));
    if (((uint32_t)(result)) == 16) goto loc_004E7732;
    if (((uint32_t)(result)) == ((uint32_t)(local_r15 + 72))) goto loc_004E7732;
    if (((uint32_t)(result)) != 0x1010ULL) goto loc_004E793C;
loc_004E7732:
    if ((uint8_t)(*(uint64_t *)(local_r15 + 0x18)) != 0) goto loc_004E787E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x90)))) & (1)) != 0) goto loc_004E7780;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x90))))) & (0x1F0FFDFULL));
    if (((uint32_t)(result)) == 16) goto loc_004E7780;
    if (((uint32_t)(result)) == ((uint32_t)(local_r15 + 72))) goto loc_004E7780;
    if (((uint32_t)(result)) == 0x1010ULL) goto loc_004E7780;
    if (((uint32_t)(result)) == ((uint32_t)(local_r15))) goto loc_004E7780;
    if (((uint32_t)(result)) == 0xB000ULL) goto loc_004E7780;
    if (((uint32_t)(result)) == 0x103000ULL) goto loc_004E7780;
    if (((uint32_t)(result)) == 0x803000ULL) goto loc_004E7780;
    if ((((uint32_t)((uint32_t)(0x10000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x90))))) == 0) goto loc_004E793C;
loc_004E7780:
    if ((uint8_t)(*(uint64_t *)(local_r15 + 0x18)) != 0) goto loc_004E787E;
    if ((*(uint64_t *)(local_rdi + 0x38)) != (local_rdi + 56)) goto loc_004E779D;
    if ((*(uint64_t *)(local_rdi + 0x48)) == (local_rdi + 72)) goto loc_004E7800;
loc_004E779D:
    if ((*(uint64_t *)(local_rdi + 0x38)) == (local_rdi + 56)) goto loc_004E77C8;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(arg3 + 0x30), *(uint64_t *)(*(uint64_t *)(local_rdi + 0x38) + 0x18), Arg3, local_r15 + 72);
    if ((uint8_t)(result) != 0) goto loc_004E793C;
    goto loc_004E779D;
loc_004E77C8:
loc_004E77CC:
    if ((*(uint64_t *)(local_rdi + 0x48)) == (local_rdi + 72)) goto loc_004E77F7;
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_m170 + 0x30), *(uint64_t *)(*(uint64_t *)(local_rdi + 0x48) + 0x18), Arg3, local_r15 + 72);
    if ((uint8_t)(result) != 0) goto loc_004E793C;
    goto loc_004E77CC;
loc_004E77F7:
    local_r10 = 0;
loc_004E7800:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x90))) & (0x1F0FFDFULL));
    if (((uint32_t)(result)) == 16) goto loc_004E7823;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_004E7823;
    if (((uint32_t)(result)) == 0x1010ULL) goto loc_004E7823;
    if (((uint32_t)(result)) != 0xB000ULL) goto loc_004E787E;
loc_004E7823:
loc_004E7827:
    if ((*(uint64_t *)(local_rdi + 0x28)) == (local_rdi + 40)) goto loc_004E787B;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0x28) + 0x10) + 0x18)) == 0x90240ULL) goto loc_004E784A;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0x28) + 0x10) + 0x30)) == (*(uint64_t *)(v_stack_m170 + 0x30))) goto loc_004E78AD;
loc_004E784A:
    Arg3 = 0;
    result = FsRtlpOplockKeysEqual(*(uint64_t *)(v_stack_m170 + 0x30), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0x28) + 0x10) + 0x30), Arg3, (uint32_t)(0x1000ULL));
    if ((uint8_t)(result) == 0) goto loc_004E78A8;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (0x7000ULL));
    result = FsRtlpRemoveAndCompleteReadOnlyIrp(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rdi + 0x28) + 0x8)), 533, Arg3, local_rdi);
loc_004E787B:
    local_r10 = 0;
loc_004E787E:
    *(uint32_t *)(arg3 + 0x30) = 0;
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x28) + 0x8)) == (local_rdi + 40)) goto loc_004E78B5;
loc_004E78A8:
loc_004E78AD:
    goto loc_004E7827;
loc_004E78B5:
    *(uint64_t *)(arg3 + 0xA8) = *(uint64_t *)(local_rdi + 0x28);
    *(uint64_t *)(arg3 + 0xA8 + 0x8) = 3;
    *(void **)(*(uint64_t *)(local_rdi + 0x28) + 0x8) = Arg3 + 168;
    *(void **)(3) = Arg3 + 168;
    *(uint64_t *)(arg3 + 0x38) = local_rdi;
    result = FsRtlpComputeShareableOplockState(local_rdi, *(uint64_t *)(local_rdi + 0x28), v_stack_m170, local_rdi);
    local_r13 = 0;
    if (Arg6 != 0) {
        local_r15 = v_stack_m170;
        Arg1 = *(uint64_t *)(local_r15 + 0x30);
        Arg2 = 0x746C6644ULL;
        result = ObfReferenceObjectWithTag(Arg1, Arg2, v_stack_m170, local_rdi);
    }
    result = KeAcquireQueuedSpinLock(7, Arg2, v_stack_m170, local_rdi);
    *(uint8_t *)(arg3 + 0x45) = (uint8_t)(result);
    if ((*(uint8_t *)(arg3 + 0x44)) == 0) goto loc_004E7912;
    result = FsRtlpCancelReadOnlyOplockIrp(Arg3, 1, v_stack_m170, local_rdi);
    goto loc_004E7928;
loc_004E7912:
    result = KeReleaseQueuedSpinLock(7, *(uint8_t *)(arg3 + 0x45), v_stack_m170, local_rdi);
loc_004E7928:
    v_stack_m178 = 259;
    local_r10 = 0;
loc_004E7937:
    if (1 != 0) goto loc_004E7955;
loc_004E793C:
loc_004E7941:
    *(uint32_t *)(arg3 + 0x30) = (uint32_t)((uint32_t)(0xC00000E2ULL));
    result = IofCompleteRequest(Arg3, 1, v_stack_m170, local_rdi);
    local_r10 = 0;
loc_004E7951:
    v_stack_m178 = (uint32_t)((uint32_t)(0xC00000E2ULL));
loc_004E7955:
    if (v_stack_m174 == 0) goto loc_004E796B;
    if (((uint32_t)((uint32_t)(Arg4))) != ((uint32_t)((uint32_t)(0x10000ULL)))) {
        Arg1 = v_stack_m140;
        result = ExReleaseFastMutexUnsafe(Arg1, 1, v_stack_m170, local_rdi);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, v_stack_m170, local_rdi);
    local_rsp = (local_rsp) + (384);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x30` | `32` | `W` |
| `Arg3` | `+ 0x38` | `64` | `W` |
| `Arg3` | `+ 0x44` | `8` | `R` |
| `Arg3` | `+ 0x45` | `8` | `R` |
| `Arg3` | `+ 0x45` | `8` | `W` |
| `Arg3` | `+ 0x68` | `64` | `R/W` |
| `Arg3` | `+ 0xA8` | `64` | `R` |
| `Arg3` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004E6EC8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
