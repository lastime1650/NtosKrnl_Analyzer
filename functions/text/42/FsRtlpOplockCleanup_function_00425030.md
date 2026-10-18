# FsRtlpOplockCleanup

- RVA: `0x00425030`–`0x004256E3` (길이 `1,715` bytes)
- VA: `0x0000000140425030`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A0484`
- 디코드: `380`개 명령, `1,715/1,715` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x004250A6` → [IoGetOplockFullFoExt](IoGetOplockFullFoExt_function_00425944.md) (function, `0x00425944`)
- `0x00425137` → [FsRtlpRemoveAndCompleteRHIrp](FsRtlpRemoveAndCompleteRHIrp_function_00425964.md) (function, `0x00425964`)
- `0x0042513F` → [FsRtlpComputeShareableOplockState](FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x0042521C` → [tlgWriteTransfer_EtwWriteTransfer](tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00425275` → [FsRtlpRemoveAndCompleteReadOnlyIrp](../4B/FsRtlpRemoveAndCompleteReadOnlyIrp_function_004B495C.md) (function, `0x004B495C`)
- `0x004252F0` → [tlgWriteTransfer_EtwWriteTransfer](tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00425301` → [FsRtlpReleaseIrpsWaitingForRH](FsRtlpReleaseIrpsWaitingForRH_function_00425CBC.md) (function, `0x00425CBC`)
- `0x0042531B` → [FsRtlpOplockDequeueRH](FsRtlpOplockDequeueRH_function_004258FC.md) (function, `0x004258FC`)
- `0x0042535B` → [FsRtlpSyncWithAckTimeout](../4F/FsRtlpSyncWithAckTimeout_function_004F23C4.md) (function, `0x004F23C4`)
- `0x00425365` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0042542A` → [tlgWriteTransfer_EtwWriteTransfer](tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00425467` → [FsRtlpOplockPerfSendData](../../page/6F/FsRtlpOplockPerfSendData_function_006FDB80.md) (function, `0x006FDB80`)
- `0x0042547C` → [FsRtlpSyncWithAckTimeout](../4F/FsRtlpSyncWithAckTimeout_function_004F23C4.md) (function, `0x004F23C4`)
- `0x0042548A` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00425494` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004254B8` → [FsRtlpRemoveAndCompleteWaitingIrp](FsRtlpRemoveAndCompleteWaitingIrp_function_00425FC0.md) (function, `0x00425FC0`)
- `0x004254CD` → [FsRtlpComputeShareableOplockState](FsRtlpComputeShareableOplockState_function_004256EC.md) (function, `0x004256EC`)
- `0x004254F8` → [FsRtlpClearOwner](../26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x00425505` → [FsRtlpOplockDequeueRH](FsRtlpOplockDequeueRH_function_004258FC.md) (function, `0x004258FC`)
- `0x00425513` → [FsRtlpModifyThreadPriorities](../48/FsRtlpModifyThreadPriorities_function_0048B098.md) (function, `0x0048B098`)
- `0x0042551E` → [FsRtlpClearOwner](../26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x00425539` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00425542` → [FsRtlpOplockPerfSendData](../../page/6F/FsRtlpOplockPerfSendData_function_006FDB80.md) (function, `0x006FDB80`)
- `0x0042555C` → [FsRtlpSyncWithAckTimeout](../4F/FsRtlpSyncWithAckTimeout_function_004F23C4.md) (function, `0x004F23C4`)
- `0x00425566` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0042559D` → [KeAcquireQueuedSpinLock](../27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x004255B1` → [KeReleaseQueuedSpinLock](../27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x00425608` → [IofCompleteRequest](../29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x00425627` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00425643` → [FsRtlpModifyThreadPriorities](../48/FsRtlpModifyThreadPriorities_function_0048B098.md) (function, `0x0048B098`)
- `0x0042564D` → [FsRtlpClearOwner](../26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x00425684` → [FsRtlpSyncWithAckTimeout](../4F/FsRtlpSyncWithAckTimeout_function_004F23C4.md) (function, `0x004F23C4`)
- `0x00425690` → [FsRtlpOplockPerfSendData](../../page/6F/FsRtlpOplockPerfSendData_function_006FDB80.md) (function, `0x006FDB80`)
- `0x0042569F` → [FsRtlpRemoveAndCompleteWaitingIrp](FsRtlpRemoveAndCompleteWaitingIrp_function_00425FC0.md) (function, `0x00425FC0`)
- `0x004256B6` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [FsRtlCheckOplockEx2](../3F/FsRtlCheckOplockEx2_function_003F2BC0.md) at `0x003F30F9`
- [FsRtlpOplockAckTimeoutWorker](../58/FsRtlpOplockAckTimeoutWorker_function_00582950.md) at `0x005829D4`

### Static image references
- `0x0042504A` → RVA `0x00E0A740` (`.data`; read)
- `0x00425095` → RVA `0x00E06C50` (`.data`; read)
- `0x0042520E` → RVA `0x00045651` (`.rdata`; read)
- `0x004252E2` → RVA `0x0004560E` (`.rdata`; read)
- `0x0042541C` → RVA `0x00045598` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00425365` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00425467` → [FsRtlpOplockPerfSendData](../../page/6F/FsRtlpOplockPerfSendData_function_006FDB80.md) (`.text` → `PAGE`)
  - `0x00425494` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00425542` → [FsRtlpOplockPerfSendData](../../page/6F/FsRtlpOplockPerfSendData_function_006FDB80.md) (`.text` → `PAGE`)
  - `0x00425566` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00425690` → [FsRtlpOplockPerfSendData](../../page/6F/FsRtlpOplockPerfSendData_function_006FDB80.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00425030  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00425035  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0042503A  57                              push rdi
0042503B  41 54                           push r12
0042503D  41 55                           push r13
0042503F  41 56                           push r14
00425041  41 57                           push r15
00425043  48 81 EC 90 01 00 00            sub rsp, 0x190
0042504A  48 8B 05 EF 56 9E 00            mov rax, qword ptr [rip + 0x9e56ef]
00425051  48 33 C4                        xor rax, rsp
00425054  48 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], rax
0042505C  45 8A E0                        mov r12b, r8b
0042505F  44 88 44 24 40                  mov byte ptr [rsp + 0x40], r8b
00425064  4C 8B F2                        mov r14, rdx
00425067  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
0042506C  48 8B F9                        mov rdi, rcx
0042506F  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
00425077  33 F6                           xor esi, esi
00425079  44 0F B6 FE                     movzx r15d, sil
0042507D  44 88 7C 24 41                  mov byte ptr [rsp + 0x41], r15b
00425082  8B 81 90 00 00 00               mov eax, dword ptr [rcx + 0x90]
00425088  44 8D 4E 01                     lea r9d, [rsi + 1]
0042508C  41 3B C1                        cmp eax, r9d
0042508F  0F 84 11 06 00 00               je 0x1404256a6
00425095  83 3D B4 1B 9E 00 05            cmp dword ptr [rip + 0x9e1bb4], 5
0042509C  0F 87 ED 01 00 00               ja 0x14042528f
004250A2  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
004250A6  E8 99 08 00 00                  call 0x140425944
004250AB  4C 8B E8                        mov r13, rax
004250AE  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
004250B3  F7 87 90 00 00 00 00 00 00 01   test dword ptr [rdi + 0x90], 0x1000000
004250BD  0F 85 B4 02 00 00               jne 0x140425377
004250C3  48 8D 77 28                     lea rsi, [rdi + 0x28]
004250C7  48 8B 1E                        mov rbx, qword ptr [rsi]
004250CA  41 BC 16 02 00 00               mov r12d, 0x216
004250D0  48 3B DE                        cmp rbx, rsi
004250D3  0F 85 4D 01 00 00               jne 0x140425226
004250D9  33 F6                           xor esi, esi
004250DB  4D 85 ED                        test r13, r13
004250DE  0F 84 8C 04 00 00               je 0x140425570
004250E4  49 8B 5D 28                     mov rbx, qword ptr [r13 + 0x28]
004250E8  48 85 DB                        test rbx, rbx
004250EB  0F 84 7F 04 00 00               je 0x140425570
004250F1  F7 43 30 00 00 F0 00            test dword ptr [rbx + 0x30], 0xf00000
004250F8  0F 85 04 04 00 00               jne 0x140425502
004250FE  45 33 D2                        xor r10d, r10d
00425101  F7 87 90 00 00 00 00 00 01 00   test dword ptr [rdi + 0x90], 0x10000
0042510B  0F 85 FA 01 00 00               jne 0x14042530b
00425111  44 8A 6C 24 40                  mov r13b, byte ptr [rsp + 0x40]
00425116  44 88 6C 24 38                  mov byte ptr [rsp + 0x38], r13b
0042511B  66 44 89 54 24 30               mov word ptr [rsp + 0x30], r10w
00425121  44 89 54 24 28                  mov dword ptr [rsp + 0x28], r10d
00425126  44 89 54 24 20                  mov dword ptr [rsp + 0x20], r10d
0042512B  45 33 C9                        xor r9d, r9d
0042512E  45 8B C4                        mov r8d, r12d
00425131  48 8B D7                        mov rdx, rdi
00425134  48 8B CB                        mov rcx, rbx
00425137  E8 28 08 00 00                  call 0x140425964
0042513C  48 8B CF                        mov rcx, rdi
0042513F  E8 A8 05 00 00                  call 0x1404256ec
00425144  40 84 F6                        test sil, sil
00425147  0F 85 B1 01 00 00               jne 0x1404252fe
0042514D  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00425151  49 39 46 30                     cmp qword ptr [r14 + 0x30], rax
00425155  0F 84 1F 04 00 00               je 0x14042557a
0042515B  83 3D EE 1A 9E 00 05            cmp dword ptr [rip + 0x9e1aee], 5
00425162  0F 86 3E 05 00 00               jbe 0x1404256a6
00425168  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
0042516D  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00425172  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
0042517A  48 C7 84 24 B8 00 00 00 08 00 00 00  mov qword ptr [rsp + 0xb8], 8
00425186  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
0042518C  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00425190  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00425195  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
0042519D  48 C7 84 24 C8 00 00 00 04 00 00 00  mov qword ptr [rsp + 0xc8], 4
004251A9  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
004251AD  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
004251B5  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
004251BD  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
004251C5  48 C7 84 24 D8 00 00 00 08 00 00 00  mov qword ptr [rsp + 0xd8], 8
004251D1  48 8B 47 60                     mov rax, qword ptr [rdi + 0x60]
004251D5  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
004251DA  48 8D 44 24 58                  lea rax, [rsp + 0x58]
004251DF  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
004251E7  48 C7 84 24 E8 00 00 00 08 00 00 00  mov qword ptr [rsp + 0xe8], 8
004251F3  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
004251FB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00425200  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
00425208  45 33 C9                        xor r9d, r9d
0042520B  45 33 C0                        xor r8d, r8d
0042520E  48 8D 15 3C 04 C2 FF            lea rdx, [rip - 0x3dfbc4]
00425215  48 8D 0D 34 1A 9E 00            lea rcx, [rip + 0x9e1a34]
0042521C  E8 BF 0E 00 00                  call 0x1404260e0
00425221  E9 80 04 00 00                  jmp 0x1404256a6
00425226  45 33 C0                        xor r8d, r8d
00425229  45 8A F0                        mov r14b, r8b
0042522C  44 88 44 24 42                  mov byte ptr [rsp + 0x42], r8b
00425231  48 3B DE                        cmp rbx, rsi
00425234  0F 84 90 02 00 00               je 0x1404254ca
0042523A  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0042523E  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
00425242  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00425247  48 39 42 30                     cmp qword ptr [rdx + 0x30], rax
0042524B  75 3D                           jne 0x14042528a
0042524D  48 8B 5B 08                     mov rbx, qword ptr [rbx + 8]
00425251  45 0F B6 F6                     movzx r14d, r14b
00425255  81 79 18 40 02 09 00            cmp dword ptr [rcx + 0x18], 0x90240
0042525C  45 0F 44 F1                     cmove r14d, r9d
00425260  44 88 74 24 42                  mov byte ptr [rsp + 0x42], r14b
00425265  41 8B D4                        mov edx, r12d
00425268  41 0F 45 D0                     cmovne edx, r8d
0042526C  4C 8B CF                        mov r9, rdi
0042526F  45 33 C0                        xor r8d, r8d
00425272  48 8B 0B                        mov rcx, qword ptr [rbx]
00425275  E8 E2 F6 08 00                  call 0x1404b495c
0042527A  45 33 C0                        xor r8d, r8d
0042527D  45 84 F6                        test r14b, r14b
00425280  0F 85 44 02 00 00               jne 0x1404254ca
00425286  45 8D 48 01                     lea r9d, [r8 + 1]
0042528A  48 8B 1B                        mov rbx, qword ptr [rbx]
0042528D  EB A2                           jmp 0x140425231
0042528F  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00425294  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00425299  48 89 8C 24 60 01 00 00         mov qword ptr [rsp + 0x160], rcx
004252A1  48 C7 84 24 68 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x168], 8
004252AD  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
004252B1  48 8D 44 24 50                  lea rax, [rsp + 0x50]
004252B6  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
004252BE  BB 04 00 00 00                  mov ebx, 4
004252C3  48 89 9C 24 78 01 00 00         mov qword ptr [rsp + 0x178], rbx
004252CB  48 8D 84 24 40 01 00 00         lea rax, [rsp + 0x140]
004252D3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004252D8  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
004252DC  45 33 C9                        xor r9d, r9d
004252DF  45 33 C0                        xor r8d, r8d
004252E2  48 8D 15 25 03 C2 FF            lea rdx, [rip - 0x3dfcdb]
004252E9  48 8D 0D 60 19 9E 00            lea rcx, [rip + 0x9e1960]
004252F0  E8 EB 0D 00 00                  call 0x1404260e0
004252F5  44 8D 4B FD                     lea r9d, [rbx - 3]
004252F9  E9 A4 FD FF FF                  jmp 0x1404250a2
004252FE  48 8B CF                        mov rcx, rdi
00425301  E8 B6 09 00 00                  call 0x140425cbc
00425306  E9 42 FE FF FF                  jmp 0x14042514d
0042530B  4C 8D 4B 38                     lea r9, [rbx + 0x38]
0042530F  4D 39 11                        cmp qword ptr [r9], r10
00425312  0F 84 F9 FD FF FF               je 0x140425111
00425318  48 8B CB                        mov rcx, rbx
0042531B  E8 DC 05 00 00                  call 0x1404258fc
00425320  49 8B 09                        mov rcx, qword ptr [r9]
00425323  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
00425327  4C 39 49 08                     cmp qword ptr [rcx + 8], r9
0042532B  75 05                           jne 0x140425332
0042532D  4C 39 08                        cmp qword ptr [rax], r9
00425330  74 07                           je 0x140425339
00425332  B9 03 00 00 00                  mov ecx, 3
00425337  CD 29                           int 0x29
00425339  48 89 08                        mov qword ptr [rax], rcx
0042533C  48 89 41 08                     mov qword ptr [rcx + 8], rax
00425340  48 8D 47 78                     lea rax, [rdi + 0x78]
00425344  48 39 00                        cmp qword ptr [rax], rax
00425347  0F 84 8F 01 00 00               je 0x1404254dc
0042534D  4C 39 53 28                     cmp qword ptr [rbx + 0x28], r10
00425351  0F 85 9B 01 00 00               jne 0x1404254f2
00425357  48 8D 4B 58                     lea rcx, [rbx + 0x58]
0042535B  E8 64 D0 0C 00                  call 0x1404f23c4
00425360  33 D2                           xor edx, edx
00425362  48 8B CB                        mov rcx, rbx
00425365  E8 06 D5 75 00                  call 0x140b82870
0042536A  44 8A 6C 24 40                  mov r13b, byte ptr [rsp + 0x40]
0042536F  40 B6 01                        mov sil, 1
00425372  E9 C5 FD FF FF                  jmp 0x14042513c
00425377  48 8D 77 68                     lea rsi, [rdi + 0x68]
0042537B  48 8B 1E                        mov rbx, qword ptr [rsi]
0042537E  48 3B DE                        cmp rbx, rsi
00425381  0F 84 18 01 00 00               je 0x14042549f
00425387  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0042538B  49 39 46 30                     cmp qword ptr [r14 + 0x30], rax
0042538F  0F 85 2D 01 00 00               jne 0x1404254c2
00425395  83 3D B4 18 9E 00 05            cmp dword ptr [rip + 0x9e18b4], 5
0042539C  0F 86 8D 00 00 00               jbe 0x14042542f
004253A2  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004253A7  48 8D 44 24 68                  lea rax, [rsp + 0x68]
004253AC  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
004253B4  48 C7 84 24 18 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x118], 8
004253C0  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
004253C5  48 8D 44 24 70                  lea rax, [rsp + 0x70]
004253CA  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
004253D2  48 C7 84 24 28 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x128], 8
004253DE  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
004253E4  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
004253E8  48 8D 44 24 54                  lea rax, [rsp + 0x54]
004253ED  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
004253F5  48 C7 84 24 38 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x138], 4
00425401  48 8D 84 24 F0 00 00 00         lea rax, [rsp + 0xf0]
00425409  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0042540E  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
00425416  45 33 C9                        xor r9d, r9d
00425419  45 33 C0                        xor r8d, r8d
0042541C  48 8D 15 75 01 C2 FF            lea rdx, [rip - 0x3dfe8b]
00425423  48 8D 0D 26 18 9E 00            lea rcx, [rip + 0x9e1826]
0042542A  E8 B1 0C 00 00                  call 0x1404260e0
0042542F  48 8D 47 58                     lea rax, [rdi + 0x58]
00425433  48 8B 08                        mov rcx, qword ptr [rax]
00425436  48 3B C8                        cmp rcx, rax
00425439  75 7D                           jne 0x1404254b8
0042543B  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0042543F  48 8B 08                        mov rcx, qword ptr [rax]
00425442  48 8B 11                        mov rdx, qword ptr [rcx]
00425445  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00425449  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
0042544D  0F 85 DF FE FF FF               jne 0x140425332
00425453  48 39 08                        cmp qword ptr [rax], rcx
00425456  0F 85 D6 FE FF FF               jne 0x140425332
0042545C  48 89 10                        mov qword ptr [rax], rdx
0042545F  48 89 42 08                     mov qword ptr [rdx + 8], rax
00425463  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00425467  E8 14 87 2D 00                  call 0x1406fdb80
0042546C  48 8D 4B 28                     lea rcx, [rbx + 0x28]
00425470  33 C0                           xor eax, eax
00425472  45 84 E4                        test r12b, r12b
00425475  74 05                           je 0x14042547c
00425477  48 89 01                        mov qword ptr [rcx], rax
0042547A  EB 05                           jmp 0x140425481
0042547C  E8 43 CF 0C 00                  call 0x1404f23c4
00425481  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00425485  BA 44 66 6C 74                  mov edx, 0x746c6644
0042548A  E8 51 24 ED FF                  call 0x1402f78e0
0042548F  33 D2                           xor edx, edx
00425491  48 8B CB                        mov rcx, rbx
00425494  E8 D7 D3 75 00                  call 0x140b82870
00425499  41 B9 01 00 00 00               mov r9d, 1
0042549F  0F BA B7 90 00 00 00 18         btr dword ptr [rdi + 0x90], 0x18
004254A7  48 39 36                        cmp qword ptr [rsi], rsi
004254AA  45 0F 45 F9                     cmovne r15d, r9d
004254AE  44 88 7C 24 41                  mov byte ptr [rsp + 0x41], r15b
004254B3  E9 0B FC FF FF                  jmp 0x1404250c3
004254B8  E8 03 0B 00 00                  call 0x140425fc0
004254BD  E9 6D FF FF FF                  jmp 0x14042542f
004254C2  48 8B 1B                        mov rbx, qword ptr [rbx]
004254C5  E9 B4 FE FF FF                  jmp 0x14042537e
004254CA  48 8B CF                        mov rcx, rdi
004254CD  E8 1A 02 00 00                  call 0x1404256ec
004254D2  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
004254D7  E9 FD FB FF FF                  jmp 0x1404250d9
004254DC  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
004254E2  25 FF FF FC FF                  and eax, 0xfffcffff
004254E7  89 87 90 00 00 00               mov dword ptr [rdi + 0x90], eax
004254ED  E9 5B FE FF FF                  jmp 0x14042534d
004254F2  48 8B D3                        mov rdx, rbx
004254F5  48 8B CF                        mov rcx, rdi
004254F8  E8 EB 06 E4 FF                  call 0x140265be8
004254FD  E9 55 FE FF FF                  jmp 0x140425357
00425502  48 8B CB                        mov rcx, rbx
00425505  E8 F2 03 00 00                  call 0x1404258fc
0042550A  45 33 C0                        xor r8d, r8d
0042550D  48 8B D3                        mov rdx, rbx
00425510  48 8B CF                        mov rcx, rdi
00425513  E8 80 5B 06 00                  call 0x14048b098
00425518  48 8B D3                        mov rdx, rbx
0042551B  48 8B CF                        mov rcx, rdi
0042551E  E8 C5 06 E4 FF                  call 0x140265be8
00425523  48 8D 47 48                     lea rax, [rdi + 0x48]
00425527  48 39 00                        cmp qword ptr [rax], rax
0042552A  75 04                           jne 0x140425530
0042552C  40 88 77 20                     mov byte ptr [rdi + 0x20], sil
00425530  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00425534  BA 44 66 6C 74                  mov edx, 0x746c6644
00425539  E8 A2 23 ED FF                  call 0x1402f78e0
0042553E  48 8D 4B 48                     lea rcx, [rbx + 0x48]
00425542  E8 39 86 2D 00                  call 0x1406fdb80
00425547  48 8D 4B 58                     lea rcx, [rbx + 0x58]
0042554B  44 8A 6C 24 40                  mov r13b, byte ptr [rsp + 0x40]
00425550  33 C0                           xor eax, eax
00425552  45 84 ED                        test r13b, r13b
00425555  74 05                           je 0x14042555c
00425557  48 89 01                        mov qword ptr [rcx], rax
0042555A  EB 05                           jmp 0x140425561
0042555C  E8 63 CE 0C 00                  call 0x1404f23c4
00425561  33 D2                           xor edx, edx
00425563  48 8B CB                        mov rcx, rbx
00425566  E8 05 D3 75 00                  call 0x140b82870
0042556B  E9 FF FD FF FF                  jmp 0x14042536f
00425570  44 8A 6C 24 40                  mov r13b, byte ptr [rsp + 0x40]
00425575  E9 D3 FB FF FF                  jmp 0x14042514d
0042557A  F7 87 90 00 00 00 80 0F F0 01   test dword ptr [rdi + 0x90], 0x1f00f80
00425584  0F 85 85 00 00 00               jne 0x14042560f
0042558A  48 8B 37                        mov rsi, qword ptr [rdi]
0042558D  48 8B 9E B8 00 00 00            mov rbx, qword ptr [rsi + 0xb8]
00425594  41 BE 07 00 00 00               mov r14d, 7
0042559A  41 8B CE                        mov ecx, r14d
0042559D  E8 DE E7 E4 FF                  call 0x140273d80
004255A2  88 46 45                        mov byte ptr [rsi + 0x45], al
004255A5  33 C0                           xor eax, eax
004255A7  48 87 46 68                     xchg qword ptr [rsi + 0x68], rax
004255AB  8A 56 45                        mov dl, byte ptr [rsi + 0x45]
004255AE  41 8B CE                        mov ecx, r14d
004255B1  E8 8A CF E4 FF                  call 0x140272540
004255B6  81 7B 18 40 02 09 00            cmp dword ptr [rbx + 0x18], 0x90240
004255BD  41 8D 5E FA                     lea ebx, [r14 - 6]
004255C1  75 2E                           jne 0x1404255f1
004255C3  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
004255C7  0F 57 C0                        xorps xmm0, xmm0
004255CA  33 C0                           xor eax, eax
004255CC  0F 11 01                        movups xmmword ptr [rcx], xmm0
004255CF  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
004255D3  C7 01 01 00 18 00               mov dword ptr [rcx], 0x180001
004255D9  8D 53 17                        lea edx, [rbx + 0x17]
004255DC  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
004255E2  C1 E8 0C                        shr eax, 0xc
004255E5  41 23 C6                        and eax, r14d
004255E8  89 41 04                        mov dword ptr [rcx + 4], eax
004255EB  48 89 56 38                     mov qword ptr [rsi + 0x38], rdx
004255EF  EB 0B                           jmp 0x1404255fc
004255F1  48 C7 46 38 08 00 00 00         mov qword ptr [rsi + 0x38], 8
004255F9  45 33 E4                        xor r12d, r12d
004255FC  48 8B 07                        mov rax, qword ptr [rdi]
004255FF  44 89 60 30                     mov dword ptr [rax + 0x30], r12d
00425603  8A D3                           mov dl, bl
00425605  48 8B 0F                        mov rcx, qword ptr [rdi]
00425608  E8 B3 5F E7 FF                  call 0x14029b5c0
0042560D  EB 05                           jmp 0x140425614
0042560F  BB 01 00 00 00                  mov ebx, 1
00425614  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
0042561A  84 C0                           test al, al
0042561C  78 0E                           js 0x14042562c
0042561E  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00425622  BA 44 66 6C 74                  mov edx, 0x746c6644
00425627  E8 B4 22 ED FF                  call 0x1402f78e0
0042562C  33 F6                           xor esi, esi
0042562E  48 89 77 08                     mov qword ptr [rdi + 8], rsi
00425632  48 89 37                        mov qword ptr [rdi], rsi
00425635  48 39 77 18                     cmp qword ptr [rdi + 0x18], rsi
00425639  74 1B                           je 0x140425656
0042563B  45 33 C0                        xor r8d, r8d
0042563E  33 D2                           xor edx, edx
00425640  48 8B CF                        mov rcx, rdi
00425643  E8 50 5A 06 00                  call 0x14048b098
00425648  33 D2                           xor edx, edx
0042564A  48 8B CF                        mov rcx, rdi
0042564D  E8 96 05 E4 FF                  call 0x140265be8
00425652  40 88 77 20                     mov byte ptr [rdi + 0x20], sil
00425656  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
0042565C  83 E0 20                        and eax, 0x20
0042565F  0B C3                           or eax, ebx
00425661  89 87 90 00 00 00               mov dword ptr [rdi + 0x90], eax
00425667  48 8D 47 58                     lea rax, [rdi + 0x58]
0042566B  48 8B 08                        mov rcx, qword ptr [rax]
0042566E  48 3B C8                        cmp rcx, rax
00425671  75 2C                           jne 0x14042569f
00425673  48 8D 8F B8 00 00 00            lea rcx, [rdi + 0xb8]
0042567A  45 84 ED                        test r13b, r13b
0042567D  74 05                           je 0x140425684
0042567F  48 89 31                        mov qword ptr [rcx], rsi
00425682  EB 05                           jmp 0x140425689
00425684  E8 3B CD 0C 00                  call 0x1404f23c4
00425689  48 8D 8F A8 00 00 00            lea rcx, [rdi + 0xa8]
00425690  E8 EB 84 2D 00                  call 0x1406fdb80
00425695  44 8A 7C 24 41                  mov r15b, byte ptr [rsp + 0x41]
0042569A  E9 BC FA FF FF                  jmp 0x14042515b
0042569F  E8 1C 09 00 00                  call 0x140425fc0
004256A4  EB C1                           jmp 0x140425667
004256A6  45 84 FF                        test r15b, r15b
004256A9  75 2E                           jne 0x1404256d9
004256AB  48 8B 8C 24 80 01 00 00         mov rcx, qword ptr [rsp + 0x180]
004256B3  48 33 CC                        xor rcx, rsp
004256B6  E8 85 6F 28 00                  call 0x1406ac640
004256BB  4C 8D 9C 24 90 01 00 00         lea r11, [rsp + 0x190]
004256C3  49 8B 5B 40                     mov rbx, qword ptr [r11 + 0x40]
004256C7  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
004256CB  49 8B E3                        mov rsp, r11
004256CE  41 5F                           pop r15
004256D0  41 5E                           pop r14
004256D2  41 5D                           pop r13
004256D4  41 5C                           pop r12
004256D6  5F                              pop rdi
004256D7  C3                              ret
004256D8  CC                              int3
004256D9  0F BA AF 90 00 00 00 18         bts dword ptr [rdi + 0x90], 0x18
004256E1  EB C8                           jmp 0x1404256ab
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlpOplockCleanup(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m164;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int8 v_stack_m176;
    unsigned __int8 v_stack_m177;
    unsigned __int8 v_stack_m178;
    unsigned __int8 v_stack_m180;
    unsigned __int16 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = v_rbx;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 10376943)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m178 = a3;
    v_stack_m170 = a2;
    v_stack_m130 = a1;
    v_rsi = 0;
    v_stack_m177 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)))) == ((unsigned int)(v_rsi + 1))) goto loc_004256A6;
    if ((*(unsigned int *)(v_rip + 10361780)) > 5) goto loc_0042528F;
loc_004250A2:
    result = IoGetOplockFullFoExt(*(unsigned __int64 *)(a2 + 48), a2, a3, v_rsi + 1);
    v_stack_m160 = result;
    if (((*(unsigned int *)(a1 + 144)) & (0x1000000ULL)) != 0) goto loc_00425377;
loc_004250C3:
    if ((*(unsigned __int64 *)(a1 + 40)) != (a1 + 40)) goto loc_00425226;
loc_004250D9:
    v_rsi = 0;
    if (result == 0) goto loc_00425570;
    if (*(unsigned __int64 *)(result + 40) == 0) goto loc_00425570;
    if (((*(unsigned int *)(*(unsigned __int64 *)(result + 40) + 48)) & (0xF00000ULL)) != 0) goto loc_00425502;
    v_r10 = 0;
    if (((*(unsigned int *)(a1 + 144)) & (0x10000ULL)) != 0) goto loc_0042530B;
loc_00425111:
    v_stack_m180 = (unsigned __int8)(v_stack_m178);
    v_stack_m188 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = 0;
    a4 = 0;
    result = FsRtlpRemoveAndCompleteRHIrp(*(unsigned __int64 *)(result + 40), a1, 534, a4);
loc_0042513C:
    result = FsRtlpComputeShareableOplockState(a1, a1, 534, a4);
    if (0 != 0) goto loc_004252FE;
loc_0042514D:
    if ((*(unsigned __int64 *)(a2 + 48)) == (*(unsigned __int64 *)(a1 + 8))) goto loc_0042557A;
loc_0042515B:
    if ((*(unsigned int *)(v_rip + 10361582)) <= 5) goto loc_004256A6;
    v_stack_m140 = a1;
    v_stack_m108 = v_stack_m140;
    v_stack_m100 = 8;
    v_stack_m170 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)));
    v_stack_mF8 = v_stack_m170;
    v_stack_mF0 = 4;
    v_stack_m138 = *(unsigned __int64 *)(a1 + 88);
    v_stack_mE8 = v_stack_m138;
    v_stack_mE0 = 8;
    v_stack_m160 = *(unsigned __int64 *)(a1 + 96);
    v_stack_mD8 = v_stack_m160;
    v_stack_mD0 = 8;
    v_stack_m190 = v_stack_m128;
    v_stack_m198 = 6;
    a4 = 0;
    a3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 10361396, v_rip - 4062148, a3, a4);
    goto loc_004256A6;
loc_00425226:
    a3 = 0;
    v_stack_m176 = 0;
loc_00425231:
    if ((*(unsigned __int64 *)(result + 40)) == 0) goto loc_004254CA;
    if ((*(unsigned __int64 *)(v_stack_m170 + 48)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) + 16) + 48))) goto loc_0042528A;
    v_r14 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) + 16) + 24)) == 0x90240ULL) { v_r14 = 0; }
    v_stack_m176 = (unsigned __int8)(v_r14);
    a2 = 534;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) + 16) + 24)) != 0x90240ULL) { a2 = 0; }
    a3 = 0;
    result = FsRtlpRemoveAndCompleteReadOnlyIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) + 8)), a2, a3, a1);
    a3 = 0;
    if ((unsigned __int8)(v_r14) != 0) goto loc_004254CA;
loc_0042528A:
    goto loc_00425231;
loc_0042528F:
    v_stack_m158 = a1;
    v_stack_m58 = v_stack_m158;
    v_stack_m50 = 8;
    v_stack_m168 = (unsigned int)(result);
    v_stack_m48 = v_stack_m168;
    v_stack_m40 = 4;
    v_stack_m190 = v_stack_m78;
    v_stack_m198 = 4;
    a4 = 0;
    a3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 10361184, v_rip - 4062427, a3, a4);
    goto loc_004250A2;
loc_004252FE:
    result = FsRtlpReleaseIrpsWaitingForRH(a1, v_rip - 4062427, a3, 4 - 3);
    goto loc_0042514D;
loc_0042530B:
    if ((*(unsigned __int64 *)(4 + 56)) == 0) goto loc_00425111;
    result = FsRtlpOplockDequeueRH(4, v_rip - 4062427, a3, 4 + 56);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(4 + 56) + 8)) != (4 + 56)) goto loc_00425332;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(4 + 56 + 8))) != (4 + 56)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(4 + 56 + 8)) = a1;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(4 + 56 + 8);
    if ((*(unsigned __int64 *)(a1 + 120)) == (a1 + 120)) goto loc_004254DC;
loc_0042534D:
    if ((*(unsigned __int64 *)(4 + 40)) != 0) goto loc_004254F2;
loc_00425357:
    result = FsRtlpSyncWithAckTimeout(4 + 88, v_rip - 4062427, a3, 4 + 56);
    a2 = 0;
    result = ExFreePoolWithTag(4, a2, a3, 4 + 56);
loc_0042536F:
    goto loc_0042513C;
loc_00425377:
loc_0042537E:
    if ((*(unsigned __int64 *)(a1 + 104)) == (a1 + 104)) goto loc_0042549F;
    if ((*(unsigned __int64 *)(v_r14 + 48)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 16))) goto loc_004254C2;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 16);
    if ((*(unsigned int *)(v_rip + 10361012)) >= = 5) {
        v_stack_m150 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 16);
        result = v_stack_m150;
        v_stack_mA8 = result;
        v_stack_mA0 = 8;
        v_stack_m148 = a1;
        result = v_stack_m148;
        v_stack_m98 = result;
        v_stack_m90 = 8;
        result = *(unsigned int *)(a1 + 144);
        v_stack_m164 = (unsigned int)(result);
        result = v_stack_m164;
        v_stack_m88 = result;
        v_stack_m80 = 4;
        result = v_stack_mC8;
        v_stack_m190 = result;
        v_stack_m198 = 5;
        a4 = 0;
        a3 = 0;
        a2 = v_rip - 4062859;
        a1 = v_rip + 10360870;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(a1 + 88)) != (a1 + 88)) goto loc_004254B8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8))) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8)))) goto loc_00425332;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8)))) goto loc_00425332;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8)) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8))) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8)) + 8);
    result = FsRtlpOplockPerfSendData(*(unsigned __int64 *)(a1 + 104) + 24, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8))), a3, a4);
    result = 0;
    if (534 == 0) goto loc_0042547C;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 40) = 0;
    goto loc_00425481;
loc_0042547C:
    result = FsRtlpSyncWithAckTimeout(*(unsigned __int64 *)(a1 + 104) + 40, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 8))), a3, a4);
loc_00425481:
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 16), (unsigned int)(0x746C6644ULL), a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 104), a2, a3, a4);
loc_0042549F:
    v_r15 = 0;
    if ((*(unsigned __int64 *)(a1 + 104)) != (a1 + 104)) { v_r15 = 1; }
    v_stack_m177 = (unsigned __int8)(v_r15);
    goto loc_004250C3;
loc_004254B8:
    result = FsRtlpRemoveAndCompleteWaitingIrp(*(unsigned __int64 *)(a1 + 104), a2, a3, 1);
    goto loc_0042542F;
loc_004254C2:
    goto loc_0042537E;
loc_004254CA:
    result = FsRtlpComputeShareableOplockState(a1, a2, a3, 1);
    goto loc_004250D9;
loc_004254DC:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (0xFFFCFFFFULL));
    *(unsigned int *)(a1 + 144) = (unsigned int)(result);
    goto loc_0042534D;
loc_004254F2:
    result = FsRtlpClearOwner(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)), a3, 1);
    goto loc_00425357;
loc_00425502:
    result = FsRtlpOplockDequeueRH(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)), a3, 1);
    a3 = 0;
    result = FsRtlpModifyThreadPriorities(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)), a3, 1);
    result = FsRtlpClearOwner(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)), a3, 1);
    if ((*(unsigned __int64 *)(a1 + 72)) == (a1 + 72)) {
        *(unsigned __int8 *)(a1 + 32) = (unsigned __int8)(a1 + 104);
    }
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)) + 24), (unsigned int)(0x746C6644ULL), a3, 1);
    result = FsRtlpOplockPerfSendData(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)) + 72, (unsigned int)(0x746C6644ULL), a3, 1);
    result = 0;
    if ((unsigned __int8)(v_stack_m178) == 0) goto loc_0042555C;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)) + 88) = 0;
    goto loc_00425561;
loc_0042555C:
    result = FsRtlpSyncWithAckTimeout(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)) + 88, (unsigned int)(0x746C6644ULL), a3, 1);
loc_00425561:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)), a2, a3, 1);
    goto loc_0042536F;
loc_00425570:
    goto loc_0042514D;
loc_0042557A:
    if (((*(unsigned int *)(a1 + 144)) & (0x1F00F80ULL)) != 0) goto loc_0042560F;
    result = KeAcquireQueuedSpinLock(7, a2, a3, 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 69) = (unsigned __int8)(result);
    result = 0;
    result = KeReleaseQueuedSpinLock(7, *(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 69), a3, 1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 184) + 24)) != 0x90240ULL) goto loc_004255F1;
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 16) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24)) = 0x180001ULL;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) >> (12));
    result = (unsigned int)((result) & (7));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 24) + 4) = (unsigned int)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) = 7 - 6 + 23;
    goto loc_004255FC;
loc_004255F1:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56) = 8;
    v_r12 = 0;
loc_004255FC:
    *(unsigned int *)(*(unsigned __int64 *)(a1) + 48) = 0;
    result = IofCompleteRequest(*(unsigned __int64 *)(a1), (unsigned __int8)(7 - 6), a3, 1);
    goto loc_00425614;
loc_0042560F:
loc_00425614:
    result = (unsigned int)(*(unsigned int *)(a1 + 144));
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(a1 + 8);
        a2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(a1, a2, a3, 1);
    }
    v_rsi = 0;
    *(unsigned __int64 *)(a1 + 8) = 0;
    *(unsigned __int64 *)(a1) = 0;
    if ((*(unsigned __int64 *)(a1 + 24)) != 0) {
        a3 = 0;
        a2 = 0;
        a1 = a1;
        result = FsRtlpModifyThreadPriorities(a1, a2, a3, 1);
        a2 = 0;
        a1 = a1;
        result = FsRtlpClearOwner(a1, a2, a3, 1);
        *(unsigned __int8 *)(a1 + 32) = 0;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 144))) & (32));
    result = (unsigned int)((result) | (1));
    *(unsigned int *)(a1 + 144) = (unsigned int)(result);
loc_00425667:
    if ((*(unsigned __int64 *)(a1 + 88)) != (a1 + 88)) goto loc_0042569F;
    if ((unsigned __int8)(v_stack_m178) == 0) goto loc_00425684;
    *(unsigned __int64 *)(a1 + 184) = 0;
    goto loc_00425689;
loc_00425684:
    result = FsRtlpSyncWithAckTimeout(a1 + 184, a2, a3, 1);
loc_00425689:
    result = FsRtlpOplockPerfSendData(a1 + 168, a2, a3, 1);
    goto loc_0042515B;
loc_0042569F:
    result = FsRtlpRemoveAndCompleteWaitingIrp(a1 + 168, a2, a3, 1);
    goto loc_00425667;
loc_004256A6:
    if ((unsigned __int8)(v_stack_m177) != 0) goto loc_004256D9;
loc_004256AB:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, 1);
    return result;
loc_004256D9:
    goto loc_004256AB;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlpOplockCleanup(void *Arg1, void *Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m164;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint8_t v_stack_m176;
    uint8_t v_stack_m177;
    uint8_t v_stack_m178;
    uint8_t v_stack_m180;
    uint16_t v_stack_m188;
    uint32_t v_stack_m190;
    uint32_t v_stack_m198;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = local_rbx;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0x9E56EF)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m178 = Arg3;
    v_stack_m170 = Arg2;
    v_stack_m130 = Arg1;
    local_rsi = 0;
    v_stack_m177 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)))) == ((uint32_t)(local_rsi + 1))) goto loc_004256A6;
    if ((*(uint32_t *)(v_rip + 0x9E1BB4)) > 5) goto loc_0042528F;
loc_004250A2:
    result = IoGetOplockFullFoExt(*(uint64_t *)(arg2 + 0x30), Arg2, Arg3, local_rsi + 1);
    v_stack_m160 = result;
    if (((*(uint32_t *)(arg1 + 0x90)) & (0x1000000ULL)) != 0) goto loc_00425377;
loc_004250C3:
    if ((*(uint64_t *)(arg1 + 0x28)) != (Arg1 + 40)) goto loc_00425226;
loc_004250D9:
    local_rsi = 0;
    if (result == 0) goto loc_00425570;
    if (*(uint64_t *)(result + 0x28) == 0) goto loc_00425570;
    if (((*(uint32_t *)(*(uint64_t *)(result + 0x28) + 0x30)) & (0xF00000ULL)) != 0) goto loc_00425502;
    local_r10 = 0;
    if (((*(uint32_t *)(arg1 + 0x90)) & (0x10000ULL)) != 0) goto loc_0042530B;
loc_00425111:
    v_stack_m180 = (uint8_t)(v_stack_m178);
    v_stack_m188 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = 0;
    a4 = 0;
    result = FsRtlpRemoveAndCompleteRHIrp(*(uint64_t *)(result + 0x28), Arg1, 534, a4);
loc_0042513C:
    result = FsRtlpComputeShareableOplockState(Arg1, Arg1, 534, a4);
    if (0 != 0) goto loc_004252FE;
loc_0042514D:
    if ((*(uint64_t *)(arg2 + 0x30)) == (*(uint64_t *)(arg1 + 0x8))) goto loc_0042557A;
loc_0042515B:
    if ((*(uint32_t *)(v_rip + 0x9E1AEE)) <= 5) goto loc_004256A6;
    v_stack_m140 = Arg1;
    v_stack_m108 = v_stack_m140;
    v_stack_m100 = 8;
    v_stack_m170 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    v_stack_mF8 = v_stack_m170;
    v_stack_mF0 = 4;
    v_stack_m138 = *(uint64_t *)(arg1 + 0x58);
    v_stack_mE8 = v_stack_m138;
    v_stack_mE0 = 8;
    v_stack_m160 = *(uint64_t *)(arg1 + 0x60);
    v_stack_mD8 = v_stack_m160;
    v_stack_mD0 = 8;
    v_stack_m190 = v_stack_m128;
    v_stack_m198 = 6;
    a4 = 0;
    Arg3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 10361396, v_rip - 4062148, Arg3, a4);
    goto loc_004256A6;
loc_00425226:
    Arg3 = 0;
    v_stack_m176 = 0;
loc_00425231:
    if ((*(uint64_t *)(result + 0x28)) == 0) goto loc_004254CA;
    if ((*(uint64_t *)(v_stack_m170 + 0x30)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x28) + 0x10) + 0x30))) goto loc_0042528A;
    local_r14 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x28) + 0x10) + 0x18)) == 0x90240ULL) { local_r14 = 0; }
    v_stack_m176 = (uint8_t)(local_r14);
    Arg2 = 534;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x28) + 0x10) + 0x18)) != 0x90240ULL) { Arg2 = 0; }
    Arg3 = 0;
    result = FsRtlpRemoveAndCompleteReadOnlyIrp(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x28) + 0x8)), Arg2, Arg3, Arg1);
    Arg3 = 0;
    if ((uint8_t)(local_r14) != 0) goto loc_004254CA;
loc_0042528A:
    goto loc_00425231;
loc_0042528F:
    v_stack_m158 = Arg1;
    v_stack_m58 = v_stack_m158;
    v_stack_m50 = 8;
    v_stack_m168 = (uint32_t)(result);
    v_stack_m48 = v_stack_m168;
    v_stack_m40 = 4;
    v_stack_m190 = v_stack_m78;
    v_stack_m198 = 4;
    a4 = 0;
    Arg3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 10361184, v_rip - 4062427, Arg3, a4);
    goto loc_004250A2;
loc_004252FE:
    result = FsRtlpReleaseIrpsWaitingForRH(Arg1, v_rip - 4062427, Arg3, 4 - 3);
    goto loc_0042514D;
loc_0042530B:
    if ((*(uint64_t *)(4 + 0x38)) == 0) goto loc_00425111;
    result = FsRtlpOplockDequeueRH(4, v_rip - 4062427, Arg3, 4 + 56);
    if ((*(uint64_t *)(*(uint64_t *)(4 + 0x38) + 0x8)) != (4 + 56)) goto loc_00425332;
    if ((*(uint64_t *)(*(uint64_t *)(4 + 0x38 + 0x8))) != (4 + 56)) {
        Arg1 = 3;
    }
    *(void **)(*(uint64_t *)(4 + 0x38 + 0x8)) = Arg1;
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(4 + 0x38 + 0x8);
    if ((*(uint64_t *)(arg1 + 0x78)) == (Arg1 + 120)) goto loc_004254DC;
loc_0042534D:
    if ((*(uint64_t *)(4 + 0x28)) != 0) goto loc_004254F2;
loc_00425357:
    result = FsRtlpSyncWithAckTimeout(4 + 88, v_rip - 4062427, Arg3, 4 + 56);
    Arg2 = 0;
    result = ExFreePoolWithTag(4, Arg2, Arg3, 4 + 56);
loc_0042536F:
    goto loc_0042513C;
loc_00425377:
loc_0042537E:
    if ((*(uint64_t *)(arg1 + 0x68)) == (Arg1 + 104)) goto loc_0042549F;
    if ((*(uint64_t *)(local_r14 + 0x30)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x10))) goto loc_004254C2;
    result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x10);
    if ((*(uint32_t *)(v_rip + 0x9E18B4)) >= = 5) {
        v_stack_m150 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x10);
        result = v_stack_m150;
        v_stack_mA8 = result;
        v_stack_mA0 = 8;
        v_stack_m148 = Arg1;
        result = v_stack_m148;
        v_stack_m98 = result;
        v_stack_m90 = 8;
        result = *(uint32_t *)(arg1 + 0x90);
        v_stack_m164 = (uint32_t)(result);
        result = v_stack_m164;
        v_stack_m88 = result;
        v_stack_m80 = 4;
        result = v_stack_mC8;
        v_stack_m190 = result;
        v_stack_m198 = 5;
        a4 = 0;
        Arg3 = 0;
        Arg2 = v_rip - 4062859;
        Arg1 = v_rip + 10360870;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, a4);
    }
    if ((*(uint64_t *)(arg1 + 0x58)) != (Arg1 + 88)) goto loc_004254B8;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8))) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8)))) goto loc_00425332;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8)))) goto loc_00425332;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8)) + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8)));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8))) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8)) + 0x8);
    result = FsRtlpOplockPerfSendData(*(uint64_t *)(arg1 + 0x68) + 24, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8))), Arg3, a4);
    result = 0;
    if (534 == 0) goto loc_0042547C;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x28) = 0;
    goto loc_00425481;
loc_0042547C:
    result = FsRtlpSyncWithAckTimeout(*(uint64_t *)(arg1 + 0x68) + 40, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x8))), Arg3, a4);
loc_00425481:
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x10), (uint32_t)(0x746C6644ULL), Arg3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x68), Arg2, Arg3, a4);
loc_0042549F:
    local_r15 = 0;
    if ((*(uint64_t *)(arg1 + 0x68)) != (Arg1 + 104)) { local_r15 = 1; }
    v_stack_m177 = (uint8_t)(local_r15);
    goto loc_004250C3;
loc_004254B8:
    result = FsRtlpRemoveAndCompleteWaitingIrp(*(uint64_t *)(arg1 + 0x68), Arg2, Arg3, 1);
    goto loc_0042542F;
loc_004254C2:
    goto loc_0042537E;
loc_004254CA:
    result = FsRtlpComputeShareableOplockState(Arg1, Arg2, Arg3, 1);
    goto loc_004250D9;
loc_004254DC:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (0xFFFCFFFFULL));
    *(uint32_t *)(arg1 + 0x90) = (uint32_t)(result);
    goto loc_0042534D;
loc_004254F2:
    result = FsRtlpClearOwner(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x68)), Arg3, 1);
    goto loc_00425357;
loc_00425502:
    result = FsRtlpOplockDequeueRH(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x68)), Arg3, 1);
    Arg3 = 0;
    result = FsRtlpModifyThreadPriorities(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x68)), Arg3, 1);
    result = FsRtlpClearOwner(Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x68)), Arg3, 1);
    if ((*(uint64_t *)(arg1 + 0x48)) == (Arg1 + 72)) {
        *(uint8_t *)(arg1 + 0x20) = (uint8_t)(Arg1 + 104);
    }
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)) + 0x18), (uint32_t)(0x746C6644ULL), Arg3, 1);
    result = FsRtlpOplockPerfSendData(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)) + 72, (uint32_t)(0x746C6644ULL), Arg3, 1);
    result = 0;
    if ((uint8_t)(v_stack_m178) == 0) goto loc_0042555C;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)) + 0x58) = 0;
    goto loc_00425561;
loc_0042555C:
    result = FsRtlpSyncWithAckTimeout(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)) + 88, (uint32_t)(0x746C6644ULL), Arg3, 1);
loc_00425561:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)), Arg2, Arg3, 1);
    goto loc_0042536F;
loc_00425570:
    goto loc_0042514D;
loc_0042557A:
    if (((*(uint32_t *)(arg1 + 0x90)) & (0x1F00F80ULL)) != 0) goto loc_0042560F;
    result = KeAcquireQueuedSpinLock(7, Arg2, Arg3, 1);
    *(uint8_t *)(*(uint64_t *)(arg1) + 0x45) = (uint8_t)(result);
    result = 0;
    result = KeReleaseQueuedSpinLock(7, *(uint8_t *)(*(uint64_t *)(arg1) + 0x45), Arg3, 1);
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0xB8) + 0x18)) != 0x90240ULL) goto loc_004255F1;
    result = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x10) = 0;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18)) = 0x180001ULL;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) >> (12));
    result = (uint32_t)((result) & (7));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x18) + 0x4) = (uint32_t)(result);
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x38) = 7 - 6 + 23;
    goto loc_004255FC;
loc_004255F1:
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x38) = 8;
    local_r12 = 0;
loc_004255FC:
    *(uint32_t *)(*(uint64_t *)(arg1) + 0x30) = 0;
    result = IofCompleteRequest(*(uint64_t *)(arg1), (uint8_t)(7 - 6), Arg3, 1);
    goto loc_00425614;
loc_0042560F:
loc_00425614:
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x90));
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(arg1 + 0x8);
        Arg2 = 0x746C6644ULL;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, Arg3, 1);
    }
    local_rsi = 0;
    *(uint64_t *)(arg1 + 0x8) = 0;
    *(uint64_t *)(arg1) = 0;
    if ((*(uint64_t *)(arg1 + 0x18)) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1;
        result = FsRtlpModifyThreadPriorities(Arg1, Arg2, Arg3, 1);
        Arg2 = 0;
        Arg1 = Arg1;
        result = FsRtlpClearOwner(Arg1, Arg2, Arg3, 1);
        *(uint8_t *)(arg1 + 0x20) = 0;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x90))) & (32));
    result = (uint32_t)((result) | (1));
    *(uint32_t *)(arg1 + 0x90) = (uint32_t)(result);
loc_00425667:
    if ((*(uint64_t *)(arg1 + 0x58)) != (Arg1 + 88)) goto loc_0042569F;
    if ((uint8_t)(v_stack_m178) == 0) goto loc_00425684;
    *(uint64_t *)(arg1 + 0xB8) = 0;
    goto loc_00425689;
loc_00425684:
    result = FsRtlpSyncWithAckTimeout(Arg1 + 184, Arg2, Arg3, 1);
loc_00425689:
    result = FsRtlpOplockPerfSendData(Arg1 + 168, Arg2, Arg3, 1);
    goto loc_0042515B;
loc_0042569F:
    result = FsRtlpRemoveAndCompleteWaitingIrp(Arg1 + 168, Arg2, Arg3, 1);
    goto loc_00425667;
loc_004256A6:
    if ((uint8_t)(v_stack_m177) != 0) goto loc_004256D9;
loc_004256AB:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, 1);
    return result;
loc_004256D9:
    goto loc_004256AB;
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
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `8` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R` |
| `Arg1` | `+ 0x90` | `32` | `R` |
| `Arg1` | `+ 0x90` | `32` | `R/W` |
| `Arg1` | `+ 0x90` | `32` | `W` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00425030&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
