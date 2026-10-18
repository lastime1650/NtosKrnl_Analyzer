# AlpcpSendMessage

- RVA: `0x0088BD40`–`0x0088CD0F` (길이 `4,047` bytes)
- VA: `0x000000014088BD40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007D3F0`
- 디코드: `911`개 명령, `4,047/4,047` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **53**; 고유 호출 대상: **35**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0088BE3F` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x0088BEE5` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x0088BF4C` → [AlpcpValidateDataInformation](../AD/AlpcpValidateDataInformation_function_00ADA7C8.md) (function, `0x00ADA7C8`)
- `0x0088C094` → [ExpLookupHandleTableEntry](../86/ExpLookupHandleTableEntry_function_00869DB0.md) (function, `0x00869DB0`)
- `0x0088C0DA` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (function, `0x00430C90`)
- `0x0088C137` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088C153` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0088C19A` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x0088C25C` → [AlpcpChargePagedPoolQuota](../92/AlpcpChargePagedPoolQuota_function_00922EA4.md) (function, `0x00922EA4`)
- `0x0088C272` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0088C2A7` → [ExAllocateFromPagedLookasideList](../../text/3F/ExAllocateFromPagedLookasideList_function_003FB730.md) (function, `0x003FB730`)
- `0x0088C2F4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088C310` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0088C34F` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0088C393` → [AlpcpEnterAllocationEventMessageLog](AlpcpEnterAllocationEventMessageLog_function_0088B840.md) (function, `0x0088B840`)
- `0x0088C3E8` → [AlpcpCaptureAttributes](AlpcpCaptureAttributes_function_0088CD20.md) (function, `0x0088CD20`)
- `0x0088C458` → [PspChargeProcessWakeCounter](PspChargeProcessWakeCounter_function_0088D2A0.md) (function, `0x0088D2A0`)
- `0x0088C4A2` → [PspChargeProcessWakeCounter](PspChargeProcessWakeCounter_function_0088D2A0.md) (function, `0x0088D2A0`)
- `0x0088C5CE` → [AlpcpDispatchReplyToWaitingThread](AlpcpDispatchReplyToWaitingThread_function_0088D7F0.md) (function, `0x0088D7F0`)
- `0x0088C5DE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0088C606` → [ExpBlockOnLockedHandleEntry](../86/ExpBlockOnLockedHandleEntry_function_00868838.md) (function, `0x00868838`)
- `0x0088C635` → [AlpcpReleaseAttributes](AlpcpReleaseAttributes_function_0088D750.md) (function, `0x0088D750`)
- `0x0088C646` → [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)
- `0x0088C680` → [AlpcpReleaseAttributes](AlpcpReleaseAttributes_function_0088D750.md) (function, `0x0088D750`)
- `0x0088C6AC` → [AlpcpDispatchNewMessage](AlpcpDispatchNewMessage_function_0088DD20.md) (function, `0x0088DD20`)
- `0x0088C6CB` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x0088C790` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0088C7BF` → [AlpcpChargePagedPoolQuota](../92/AlpcpChargePagedPoolQuota_function_00922EA4.md) (function, `0x00922EA4`)
- `0x0088C7DA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0088C7F4` → [AlpcpReleasePagedPoolQuota](../92/AlpcpReleasePagedPoolQuota_function_00922EE8.md) (function, `0x00922EE8`)
- `0x0088C81E` → [ExHandleLogBadReference](../../text/44/ExHandleLogBadReference_function_00440580.md) (function, `0x00440580`)
- `0x0088C84B` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0088C8B3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0088C91A` → [AlpcpDispatchReplyToPort](AlpcpDispatchReplyToPort_function_0088F880.md) (function, `0x0088F880`)
- `0x0088C961` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0088C9E7` → [AlpcReferenceBlobByHandle](AlpcReferenceBlobByHandle_function_00889F00.md) (function, `0x00889F00`)
- `0x0088C9FF` → [AlpcpLockForCachedReferenceBlob](AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x0088CAC7` → [AlpcpReleasePagedPoolQuota](../92/AlpcpReleasePagedPoolQuota_function_00922EE8.md) (function, `0x00922EE8`)
- `0x0088CADA` → [PsReturnProcessPagedPoolQuota](../../text/2A/PsReturnProcessPagedPoolQuota_function_002A6860.md) (function, `0x002A6860`)
- `0x0088CAF2` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0088CB05` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0088CB25` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0088CB3E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0088CBCA` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0088CBF0` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0088CBFA` → [AlpcpDereferenceBlobEx](AlpcpDereferenceBlobEx_function_0088AF00.md) (function, `0x0088AF00`)
- `0x0088CC18` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088CC3C` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0088CC8B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088CCDC` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0088CCE6` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0088CCF0` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0088CD05` → [ExUnlockHandleTableEntry](../94/ExUnlockHandleTableEntry_function_0094D2D0.md) (function, `0x0094D2D0`)

### Direct callers
- [NtWaitForWorkViaWorkerFactory](../../text/39/NtWaitForWorkViaWorkerFactory_function_00394270.md) at `0x00394856`
- [sub_00868255](../86/Unknown_function_00868255.md) at `0x00868289`
- [LpcRequestPort](LpcRequestPort_function_0088A940.md) at `0x0088A98C`
- [NtReplyWaitReceivePortEx](../89/NtReplyWaitReceivePortEx_function_00895850.md) at `0x00895A2E`
- [AlpcpProcessSynchronousRequest](../92/AlpcpProcessSynchronousRequest_function_00921FCC.md) at `0x009220B5`
- [AlpcpSendLegacySynchronousRequest](../92/AlpcpSendLegacySynchronousRequest_function_0092376C.md) at `0x00923BF1`
- [NtReplyPort](../9F/NtReplyPort_function_009F5BE0.md) at `0x009F5CD2`
- [NtRequestPort](../A9/NtRequestPort_function_00A98DA0.md) at `0x00A98E47`

### Static image references
- `0x0088BD55` → RVA `0x00E0A740` (`.data`; read)
- `0x0088C058` → RVA `0x00FC6F68` (`ALMOSTRO`; read)
- `0x0088C2A0` → RVA `0x00E27180` (`.data`; read)
- `0x0088C373` → RVA `0x00FCF300` (`CACHEALI`; read/write)
- `0x0088C387` → RVA `0x00F100D0` (`.data`; read)
- `0x0088C9E0` → RVA `0x000014D8` (`.rdata`; read)
- `0x0088CCA2` → RVA `0x00FC5130` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x0088BE3F` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x0088BEE5` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x0088C0DA` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (`PAGE` → `.text`)
  - `0x0088C137` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088C153` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0088C19A` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x0088C2A7` → [ExAllocateFromPagedLookasideList](../../text/3F/ExAllocateFromPagedLookasideList_function_003FB730.md) (`PAGE` → `.text`)
  - `0x0088C2F4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088C310` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0088C34F` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0088C5DE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0088C6CB` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x0088C790` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0088C7DA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0088C81E` → [ExHandleLogBadReference](../../text/44/ExHandleLogBadReference_function_00440580.md) (`PAGE` → `.text`)
  - `0x0088C8B3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0088C961` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0088CADA` → [PsReturnProcessPagedPoolQuota](../../text/2A/PsReturnProcessPagedPoolQuota_function_002A6860.md) (`PAGE` → `.text`)
  - `0x0088CB25` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0088CB3E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0088CBCA` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0088CC18` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088CC3C` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0088CC8B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088CCDC` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0088CCE6` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0088BD40  4C 8B DC                        mov r11, rsp
0088BD43  53                              push rbx
0088BD44  56                              push rsi
0088BD45  57                              push rdi
0088BD46  41 54                           push r12
0088BD48  41 55                           push r13
0088BD4A  41 56                           push r14
0088BD4C  41 57                           push r15
0088BD4E  48 81 EC 10 01 00 00            sub rsp, 0x110
0088BD55  48 8B 05 E4 E9 57 00            mov rax, qword ptr [rip + 0x57e9e4]
0088BD5C  48 33 C4                        xor rax, rsp
0088BD5F  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
0088BD67  45 0F B6 D1                     movzx r10d, r9b
0088BD6B  44 88 4C 24 40                  mov byte ptr [rsp + 0x40], r9b
0088BD70  4C 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], r8
0088BD78  48 8B FA                        mov rdi, rdx
0088BD7B  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
0088BD83  48 8B C1                        mov rax, rcx
0088BD86  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
0088BD8E  0F 57 C0                        xorps xmm0, xmm0
0088BD91  33 C9                           xor ecx, ecx
0088BD93  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
0088BD98  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
0088BD9D  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
0088BDA2  0F 57 C9                        xorps xmm1, xmm1
0088BDA5  0F 11 8C 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm1
0088BDAD  0F 11 8C 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm1
0088BDB5  0F 11 8C 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm1
0088BDBD  41 0F 11 4B 88                  movups xmmword ptr [r11 - 0x78], xmm1
0088BDC2  49 89 4B 98                     mov qword ptr [r11 - 0x68], rcx
0088BDC6  48 8B 30                        mov rsi, qword ptr [rax]
0088BDC9  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
0088BDCE  8B 58 30                        mov ebx, dword ptr [rax + 0x30]
0088BDD1  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
0088BDD5  8B 86 A0 01 00 00               mov eax, dword ptr [rsi + 0x1a0]
0088BDDB  A8 10                           test al, 0x10
0088BDDD  0F 85 1E 0A 00 00               jne 0x14088c801
0088BDE3  A8 08                           test al, 8
0088BDE5  0F 85 A2 0D 00 00               jne 0x14088cb8d
0088BDEB  A8 20                           test al, 0x20
0088BDED  0F 85 B7 0C 00 00               jne 0x14088caaa
0088BDF3  45 84 C9                        test r9b, r9b
0088BDF6  0F 84 E8 08 00 00               je 0x14088c6e4
0088BDFC  33 C0                           xor eax, eax
0088BDFE  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
0088BE06  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
0088BE0E  8B C3                           mov eax, ebx
0088BE10  25 00 00 00 C0                  and eax, 0xc0000000
0088BE15  3D 00 00 00 80                  cmp eax, 0x80000000
0088BE1A  0F 84 A3 00 00 00               je 0x14088bec3
0088BE20  49 BE 00 00 FF FF FF 7F 00 00   movabs r14, 0x7fffffff0000
0088BE2A  49 8B D6                        mov rdx, r14
0088BE2D  49 3B FE                        cmp rdi, r14
0088BE30  48 0F 42 D7                     cmovb rdx, rdi
0088BE34  41 B8 28 00 00 00               mov r8d, 0x28
0088BE3A  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0088BE3F  E8 8C 0B E3 FF                  call 0x1406bc9d0
0088BE44  44 0F B7 44 24 52               movzx r8d, word ptr [rsp + 0x52]
0088BE4A  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
0088BE4F  F7 86 00 01 00 00 00 10 00 00   test dword ptr [rsi + 0x100], 0x1000
0088BE59  75 50                           jne 0x14088beab
0088BE5B  F6 C3 02                        test bl, 2
0088BE5E  75 4B                           jne 0x14088beab
0088BE60  32 C9                           xor cl, cl
0088BE62  88 4C 24 41                     mov byte ptr [rsp + 0x41], cl
0088BE66  8D 42 28                        lea eax, [rdx + 0x28]
0088BE69  66 3B D0                        cmp dx, ax
0088BE6C  0F 83 F0 00 00 00               jae 0x14088bf62
0088BE72  41 0F B7 C0                     movzx eax, r8w
0088BE76  84 C9                           test cl, cl
0088BE78  0F B7 CA                        movzx ecx, dx
0088BE7B  75 32                           jne 0x14088beaf
0088BE7D  48 83 C1 28                     add rcx, 0x28
0088BE81  48 3B C8                        cmp rcx, rax
0088BE84  0F 85 D8 00 00 00               jne 0x14088bf62
0088BE8A  B8 FF 7F 00 00                  mov eax, 0x7fff
0088BE8F  66 21 44 24 54                  and word ptr [rsp + 0x54], ax
0088BE94  66 83 7C 24 56 00               cmp word ptr [rsp + 0x56], 0
0088BE9A  0F 85 A4 00 00 00               jne 0x14088bf44
0088BEA0  44 0F B6 54 24 40               movzx r10d, byte ptr [rsp + 0x40]
0088BEA6  E9 C6 00 00 00                  jmp 0x14088bf71
0088BEAB  B1 01                           mov cl, 1
0088BEAD  EB B3                           jmp 0x14088be62
0088BEAF  48 83 C1 28                     add rcx, 0x28
0088BEB3  48 3B C8                        cmp rcx, rax
0088BEB6  0F 87 A6 00 00 00               ja 0x14088bf62
0088BEBC  66 89 4C 24 52                  mov word ptr [rsp + 0x52], cx
0088BEC1  EB C7                           jmp 0x14088be8a
0088BEC3  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
0088BECD  48 8B D0                        mov rdx, rax
0088BED0  48 3B F8                        cmp rdi, rax
0088BED3  48 0F 42 D7                     cmovb rdx, rdi
0088BED7  41 B8 18 00 00 00               mov r8d, 0x18
0088BEDD  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
0088BEE5  E8 E6 0A E3 FF                  call 0x1406bc9d0
0088BEEA  0F B7 94 24 F0 00 00 00         movzx edx, word ptr [rsp + 0xf0]
0088BEF2  66 89 54 24 50                  mov word ptr [rsp + 0x50], dx
0088BEF7  44 8D 42 28                     lea r8d, [rdx + 0x28]
0088BEFB  66 44 89 44 24 52               mov word ptr [rsp + 0x52], r8w
0088BF01  8B 84 24 F4 00 00 00            mov eax, dword ptr [rsp + 0xf4]
0088BF08  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
0088BF0C  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
0088BF13  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0088BF18  8B 84 24 FC 00 00 00            mov eax, dword ptr [rsp + 0xfc]
0088BF1F  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0088BF24  8B 84 24 00 01 00 00            mov eax, dword ptr [rsp + 0x100]
0088BF2B  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
0088BF2F  8B 8C 24 04 01 00 00            mov ecx, dword ptr [rsp + 0x104]
0088BF36  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
0088BF3B  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
0088BF3F  E9 0B FF FF FF                  jmp 0x14088be4f
0088BF44  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
0088BF49  48 8B CF                        mov rcx, rdi
0088BF4C  E8 77 E8 24 00                  call 0x140ada7c8
0088BF51  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0088BF55  85 C0                           test eax, eax
0088BF57  0F 89 43 FF FF FF               jns 0x14088bea0
0088BF5D  E9 71 06 00 00                  jmp 0x14088c5d3
0088BF62  B8 0D 00 00 C0                  mov eax, 0xc000000d
0088BF67  E9 67 06 00 00                  jmp 0x14088c5d3
0088BF6C  E9 62 06 00 00                  jmp 0x14088c5d3
0088BF71  F7 86 00 01 00 00 00 10 00 00   test dword ptr [rsi + 0x100], 0x1000
0088BF7B  0F 85 8A 08 00 00               jne 0x14088c80b
0088BF81  F6 C3 02                        test bl, 2
0088BF84  0F 85 81 08 00 00               jne 0x14088c80b
0088BF8A  32 C0                           xor al, al
0088BF8C  0F B7 4C 24 54                  movzx ecx, word ptr [rsp + 0x54]
0088BF91  0F B7 D1                        movzx edx, cx
0088BF94  41 B8 FF 00 00 00               mov r8d, 0xff
0088BF9A  66 41 23 D0                     and dx, r8w
0088BF9E  41 B8 00 FF 00 00               mov r8d, 0xff00
0088BFA4  66 41 23 C8                     and cx, r8w
0088BFA8  44 8B 64 24 68                  mov r12d, dword ptr [rsp + 0x68]
0088BFAD  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
0088BFB6  84 C0                           test al, al
0088BFB8  0F 85 9C 08 00 00               jne 0x14088c85a
0088BFBE  66 83 FA 07                     cmp dx, 7
0088BFC2  0F 84 CF 0A 00 00               je 0x14088ca97
0088BFC8  45 85 E4                        test r12d, r12d
0088BFCB  0F 85 AD 02 00 00               jne 0x14088c27e
0088BFD1  BF 01 00 00 00                  mov edi, 1
0088BFD6  0F BA E3 10                     bt ebx, 0x10
0088BFDA  0F 83 FC 06 00 00               jae 0x14088c6dc
0088BFE0  8D 57 02                        lea edx, [rdi + 2]
0088BFE3  45 33 FF                        xor r15d, r15d
0088BFE6  44 8B 64 24 68                  mov r12d, dword ptr [rsp + 0x68]
0088BFEB  45 85 E4                        test r12d, r12d
0088BFEE  0F 84 5B 06 00 00               je 0x14088c64f
0088BFF4  41 0F 10 81 08 05 00 00         movups xmm0, xmmword ptr [r9 + 0x508]
0088BFFC  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
0088C001  B8 FF EF 00 00                  mov eax, 0xefff
0088C006  66 23 C8                        and cx, ax
0088C009  66 0B CA                        or cx, dx
0088C00C  66 89 4C 24 54                  mov word ptr [rsp + 0x54], cx
0088C011  0F B7 44 24 52                  movzx eax, word ptr [rsp + 0x52]
0088C016  48 3B 86 10 01 00 00            cmp rax, qword ptr [rsi + 0x110]
0088C01D  0F 87 74 0B 00 00               ja 0x14088cb97
0088C023  0F BA E3 11                     bt ebx, 0x11
0088C027  0F 82 5D 06 00 00               jb 0x14088c68a
0088C02D  41 8B C4                        mov eax, r12d
0088C030  45 85 E4                        test r12d, r12d
0088C033  0F 84 67 02 00 00               je 0x14088c2a0
0088C039  83 CB 10                        or ebx, 0x10
0088C03C  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
0088C040  44 8B 7C 24 70                  mov r15d, dword ptr [rsp + 0x70]
0088C045  85 C0                           test eax, eax
0088C047  0F 88 79 09 00 00               js 0x14088c9c6
0088C04D  A9 00 00 00 FC                  test eax, 0xfc000000
0088C052  0F 85 4A 0C 00 00               jne 0x14088cca2
0088C058  4C 8B 35 09 AF 73 00            mov r14, qword ptr [rip + 0x73af09]
0088C05F  4D 85 F6                        test r14, r14
0088C062  0F 84 68 06 00 00               je 0x14088c6d0
0088C068  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0088C071  0F B6 B0 32 02 00 00            movzx esi, byte ptr [rax + 0x232]
0088C078  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0088C07D  81 E7 FF FF FF 03               and edi, 0x3ffffff
0088C083  F7 C7 FC 03 00 00               test edi, 0x3fc
0088C089  0F 84 83 07 00 00               je 0x14088c812
0088C08F  8B D7                           mov edx, edi
0088C091  49 8B CE                        mov rcx, r14
0088C094  E8 17 DD FD FF                  call 0x140869db0
0088C099  48 8B D8                        mov rbx, rax
0088C09C  48 85 C0                        test rax, rax
0088C09F  0F 84 6D 07 00 00               je 0x14088c812
0088C0A5  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
0088C0B0  0F 0D 0B                        prefetchw byte ptr [rbx]
0088C0B3  4C 8B 03                        mov r8, qword ptr [rbx]
0088C0B6  41 F6 C0 01                     test r8b, 1
0088C0BA  0F 84 37 05 00 00               je 0x14088c5f7
0088C0C0  49 8D 48 FF                     lea rcx, [r8 - 1]
0088C0C4  49 8B C0                        mov rax, r8
0088C0C7  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
0088C0CC  75 E2                           jne 0x14088c0b0
0088C0CE  48 85 DB                        test rbx, rbx
0088C0D1  0F 84 F9 05 00 00               je 0x14088c6d0
0088C0D7  48 8B CB                        mov rcx, rbx
0088C0DA  E8 B1 4B BA FF                  call 0x140430c90
0088C0DF  4C 8B E8                        mov r13, rax
0088C0E2  44 39 A0 08 01 00 00            cmp dword ptr [rax + 0x108], r12d
0088C0E9  0F 85 C7 05 00 00               jne 0x14088c6b6
0088C0EF  45 85 FF                        test r15d, r15d
0088C0F2  74 0D                           je 0x14088c101
0088C0F4  44 39 B8 10 01 00 00            cmp dword ptr [rax + 0x110], r15d
0088C0FB  0F 85 B5 05 00 00               jne 0x14088c6b6
0088C101  0F 0D 48 E8                     prefetchw byte ptr [rax - 0x18]
0088C105  48 8B 40 E8                     mov rax, qword ptr [rax - 0x18]
0088C109  48 85 C0                        test rax, rax
0088C10C  0F 8E B5 0B 00 00               jle 0x14088ccc7
0088C112  48 8B D0                        mov rdx, rax
0088C115  48 8D 48 01                     lea rcx, [rax + 1]
0088C119  F0 49 0F B1 4D E8               lock cmpxchg qword ptr [r13 - 0x18], rcx
0088C11F  48 3B C2                        cmp rax, rdx
0088C122  75 E5                           jne 0x14088c109
0088C124  48 83 C0 01                     add rax, 1
0088C128  0F 84 D1 0B 00 00               je 0x14088ccff
0088C12E  45 33 C0                        xor r8d, r8d
0088C131  33 D2                           xor edx, edx
0088C133  49 8D 4D F0                     lea rcx, [r13 - 0x10]
0088C137  E8 F4 40 98 FF                  call 0x140210230
0088C13C  48 8B F0                        mov rsi, rax
0088C13F  F0 49 0F BA 6D F0 00            lock bts qword ptr [r13 - 0x10], 0
0088C146  73 10                           jae 0x14088c158
0088C148  4D 8D 45 F0                     lea r8, [r13 - 0x10]
0088C14C  48 8B D0                        mov rdx, rax
0088C14F  49 8D 4D F0                     lea rcx, [r13 - 0x10]
0088C153  E8 38 3B 98 FF                  call 0x14020fc90
0088C158  48 85 F6                        test rsi, rsi
0088C15B  74 04                           je 0x14088c161
0088C15D  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0088C161  41 80 4D E0 01                  or byte ptr [r13 - 0x20], 1
0088C166  B8 00 00 01 00                  mov eax, 0x10000
0088C16B  F0 49 0F C1 45 E8               lock xadd qword ptr [r13 - 0x18], rax
0088C171  48 05 00 00 01 00               add rax, 0x10000
0088C177  48 85 C0                        test rax, rax
0088C17A  0F 8E 92 09 00 00               jle 0x14088cb12
0088C180  66 41 FF 4D E2                  dec word ptr [r13 - 0x1e]
0088C185  F0 48 FF 03                     lock inc qword ptr [rbx]
0088C189  49 8D 4E 30                     lea rcx, [r14 + 0x30]
0088C18D  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0088C192  48 83 39 00                     cmp qword ptr [rcx], 0
0088C196  74 07                           je 0x14088c19f
0088C198  33 D2                           xor edx, edx
0088C19A  E8 41 7E A1 FF                  call 0x1402a3fe0
0088C19F  45 39 A5 08 01 00 00            cmp dword ptr [r13 + 0x108], r12d
0088C1A6  0F 85 43 09 00 00               jne 0x14088caef
0088C1AC  45 85 FF                        test r15d, r15d
0088C1AF  74 0D                           je 0x14088c1be
0088C1B1  45 39 BD 10 01 00 00            cmp dword ptr [r13 + 0x110], r15d
0088C1B8  0F 85 31 09 00 00               jne 0x14088caef
0088C1BE  49 83 7D 18 00                  cmp qword ptr [r13 + 0x18], 0
0088C1C3  0F 84 1B 09 00 00               je 0x14088cae4
0088C1C9  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
0088C1CE  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
0088C1D2  49 39 85 B8 00 00 00            cmp qword ptr [r13 + 0xb8], rax
0088C1D9  74 0D                           je 0x14088c1e8
0088C1DB  49 39 B5 C0 00 00 00            cmp qword ptr [r13 + 0xc0], rsi
0088C1E2  0F 85 05 0B 00 00               jne 0x14088cced
0088C1E8  45 33 FF                        xor r15d, r15d
0088C1EB  41 8B DF                        mov ebx, r15d
0088C1EE  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
0088C1F2  41 8B 4D 28                     mov ecx, dword ptr [r13 + 0x28]
0088C1F6  84 C9                           test cl, cl
0088C1F8  0F 88 A9 01 00 00               js 0x14088c3a7
0088C1FE  49 8B 7D 18                     mov rdi, qword ptr [r13 + 0x18]
0088C202  48 85 FF                        test rdi, rdi
0088C205  0F 85 1D 06 00 00               jne 0x14088c828
0088C20B  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
0088C210  49 83 7D 20 00                  cmp qword ptr [r13 + 0x20], 0
0088C215  0F 84 91 01 00 00               je 0x14088c3ac
0088C21B  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
0088C21F  49 83 7D 30 00                  cmp qword ptr [r13 + 0x30], 0
0088C224  0F 85 86 01 00 00               jne 0x14088c3b0
0088C22A  F7 C6 00 00 03 00               test esi, 0x30000
0088C230  0F 85 7A 01 00 00               jne 0x14088c3b0
0088C236  BA 18 03 00 00                  mov edx, 0x318
0088C23B  49 83 BD E0 00 00 00 00         cmp qword ptr [r13 + 0xe0], 0
0088C243  74 07                           je 0x14088c24c
0088C245  49 03 95 E8 00 00 00            add rdx, qword ptr [r13 + 0xe8]
0088C24C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0088C255  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0088C25C  E8 43 6C 09 00                  call 0x140922ea4
0088C261  8B D8                           mov ebx, eax
0088C263  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0088C267  85 C0                           test eax, eax
0088C269  0F 89 32 09 00 00               jns 0x14088cba1
0088C26F  49 8B CD                        mov rcx, r13
0088C272  E8 69 B8 00 00                  call 0x140897ae0
0088C277  8B C3                           mov eax, ebx
0088C279  E9 55 03 00 00                  jmp 0x14088c5d3
0088C27E  0F 88 4D FD FF FF               js 0x14088bfd1
0088C284  0F BA E3 10                     bt ebx, 0x10
0088C288  41 BF 00 00 00 00               mov r15d, 0
0088C28E  41 8B C7                        mov eax, r15d
0088C291  0F 92 C0                        setb al
0088C294  8D 50 01                        lea edx, [rax + 1]
0088C297  41 8D 7F 01                     lea edi, [r15 + 1]
0088C29B  E9 46 FD FF FF                  jmp 0x14088bfe6
0088C2A0  48 8D 0D D9 AE 59 00            lea rcx, [rip + 0x59aed9]
0088C2A7  E8 84 F4 B6 FF                  call 0x1403fb730
0088C2AC  48 8B D8                        mov rbx, rax
0088C2AF  48 85 C0                        test rax, rax
0088C2B2  0F 84 B8 07 00 00               je 0x14088ca70
0088C2B8  66 C7 40 10 00 02               mov word ptr [rax + 0x10], 0x200
0088C2BE  44 89 78 12                     mov dword ptr [rax + 0x12], r15d
0088C2C2  66 44 89 78 16                  mov word ptr [rax + 0x16], r15w
0088C2C7  4C 89 78 28                     mov qword ptr [rax + 0x28], r15
0088C2CB  4C 89 78 20                     mov qword ptr [rax + 0x20], r15
0088C2CF  48 89 40 08                     mov qword ptr [rax + 8], rax
0088C2D3  48 89 00                        mov qword ptr [rax], rax
0088C2D6  80 48 10 02                     or byte ptr [rax + 0x10], 2
0088C2DA  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0088C2DE  4C 8D 68 30                     lea r13, [rax + 0x30]
0088C2E2  4D 85 ED                        test r13, r13
0088C2E5  0F 84 85 07 00 00               je 0x14088ca70
0088C2EB  45 33 C0                        xor r8d, r8d
0088C2EE  33 D2                           xor edx, edx
0088C2F0  48 8D 48 20                     lea rcx, [rax + 0x20]
0088C2F4  E8 37 3F 98 FF                  call 0x140210230
0088C2F9  4C 8B F0                        mov r14, rax
0088C2FC  F0 48 0F BA 6B 20 00            lock bts qword ptr [rbx + 0x20], 0
0088C303  73 10                           jae 0x14088c315
0088C305  4C 8D 43 20                     lea r8, [rbx + 0x20]
0088C309  48 8B D0                        mov rdx, rax
0088C30C  48 8D 4B 20                     lea rcx, [rbx + 0x20]
0088C310  E8 7B 39 98 FF                  call 0x14020fc90
0088C315  4D 85 F6                        test r14, r14
0088C318  74 05                           je 0x14088c31f
0088C31A  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
0088C31F  80 4B 10 01                     or byte ptr [rbx + 0x10], 1
0088C323  B8 00 00 01 00                  mov eax, 0x10000
0088C328  F0 48 0F C1 43 18               lock xadd qword ptr [rbx + 0x18], rax
0088C32E  48 05 00 00 01 00               add rax, 0x10000
0088C334  48 85 C0                        test rax, rax
0088C337  0F 8E EE 07 00 00               jle 0x14088cb2b
0088C33D  41 8B 9D 08 01 00 00            mov ebx, dword ptr [r13 + 0x108]
0088C344  33 D2                           xor edx, edx
0088C346  41 B8 18 01 00 00               mov r8d, 0x118
0088C34C  49 8B CD                        mov rcx, r13
0088C34F  E8 EC A8 E3 FF                  call 0x1406c6c40
0088C354  BE 28 00 00 00                  mov esi, 0x28
0088C359  66 41 89 B5 F2 00 00 00         mov word ptr [r13 + 0xf2], si
0088C361  66 41 FF 4D E2                  dec word ptr [r13 - 0x1e]
0088C366  0F BA F3 1F                     btr ebx, 0x1f
0088C36A  41 89 9D 08 01 00 00            mov dword ptr [r13 + 0x108], ebx
0088C371  8B C7                           mov eax, edi
0088C373  F0 0F C1 05 85 2F 74 00         lock xadd dword ptr [rip + 0x742f85], eax
0088C37B  83 C0 01                        add eax, 1
0088C37E  74 F1                           je 0x14088c371
0088C380  41 89 85 10 01 00 00            mov dword ptr [r13 + 0x110], eax
0088C387  83 3D 42 3D 68 00 00            cmp dword ptr [rip + 0x683d42], 0
0088C38E  74 08                           je 0x14088c398
0088C390  49 8B CD                        mov rcx, r13
0088C393  E8 A8 F4 FF FF                  call 0x14088b840
0088C398  66 41 89 B5 F2 00 00 00         mov word ptr [r13 + 0xf2], si
0088C3A0  41 8B DF                        mov ebx, r15d
0088C3A3  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
0088C3A7  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
0088C3AC  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
0088C3B0  85 DB                           test ebx, ebx
0088C3B2  0F 88 1D 03 00 00               js 0x14088c6d5
0088C3B8  49 8B FF                        mov rdi, r15
0088C3BB  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0088C3C3  48 85 C9                        test rcx, rcx
0088C3C6  74 33                           je 0x14088c3fb
0088C3C8  48 8D BC 24 A0 00 00 00         lea rdi, [rsp + 0xa0]
0088C3D0  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
0088C3D8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0088C3DD  4D 8B CD                        mov r9, r13
0088C3E0  4C 8B C1                        mov r8, rcx
0088C3E3  8B D6                           mov edx, esi
0088C3E5  49 8B CE                        mov rcx, r14
0088C3E8  E8 33 09 00 00                  call 0x14088cd20
0088C3ED  8B D8                           mov ebx, eax
0088C3EF  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0088C3F3  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0088C3FB  45 85 E4                        test r12d, r12d
0088C3FE  0F 85 0C 02 00 00               jne 0x14088c610
0088C404  85 DB                           test ebx, ebx
0088C406  0F 88 63 FE FF FF               js 0x14088c26f
0088C40C  45 85 E4                        test r12d, r12d
0088C40F  0F 84 99 00 00 00               je 0x14088c4ae
0088C415  49 8B 8D D0 00 00 00            mov rcx, qword ptr [r13 + 0xd0]
0088C41C  BB 02 00 00 00                  mov ebx, 2
0088C421  48 85 C9                        test rcx, rcx
0088C424  74 3E                           je 0x14088c464
0088C426  45 8B 8D 08 01 00 00            mov r9d, dword ptr [r13 + 0x108]
0088C42D  8B C1                           mov eax, ecx
0088C42F  83 E0 07                        and eax, 7
0088C432  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
0088C436  45 8B C7                        mov r8d, r15d
0088C439  83 F8 07                        cmp eax, 7
0088C43C  44 0F 45 C0                     cmovne r8d, eax
0088C440  8B D3                           mov edx, ebx
0088C442  41 0F 45 D7                     cmovne edx, r15d
0088C446  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0088C44B  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
0088C450  C7 44 24 20 FF FF FF FF         mov dword ptr [rsp + 0x20], 0xffffffff
0088C458  E8 43 0E 00 00                  call 0x14088d2a0
0088C45D  4D 89 BD D0 00 00 00            mov qword ptr [r13 + 0xd0], r15
0088C464  49 8B 8D D8 00 00 00            mov rcx, qword ptr [r13 + 0xd8]
0088C46B  48 85 C9                        test rcx, rcx
0088C46E  74 3E                           je 0x14088c4ae
0088C470  45 8B 8D 08 01 00 00            mov r9d, dword ptr [r13 + 0x108]
0088C477  8B C1                           mov eax, ecx
0088C479  83 E0 07                        and eax, 7
0088C47C  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
0088C480  45 8B C7                        mov r8d, r15d
0088C483  83 F8 07                        cmp eax, 7
0088C486  44 0F 45 C0                     cmovne r8d, eax
0088C48A  41 0F 45 DF                     cmovne ebx, r15d
0088C48E  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0088C493  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
0088C498  C7 44 24 20 FF FF FF FF         mov dword ptr [rsp + 0x20], 0xffffffff
0088C4A0  8B D3                           mov edx, ebx
0088C4A2  E8 F9 0D 00 00                  call 0x14088d2a0
0088C4A7  4D 89 BD D8 00 00 00            mov qword ptr [r13 + 0xd8], r15
0088C4AE  49 8B DF                        mov rbx, r15
0088C4B1  45 85 E4                        test r12d, r12d
0088C4B4  0F 85 AB 01 00 00               jne 0x14088c665
0088C4BA  48 85 FF                        test rdi, rdi
0088C4BD  74 37                           je 0x14088c4f6
0088C4BF  0F 10 07                        movups xmm0, xmmword ptr [rdi]
0088C4C2  41 0F 11 45 68                  movups xmmword ptr [r13 + 0x68], xmm0
0088C4C7  0F 10 4F 10                     movups xmm1, xmmword ptr [rdi + 0x10]
0088C4CB  41 0F 11 4D 78                  movups xmmword ptr [r13 + 0x78], xmm1
0088C4D0  0F 10 47 20                     movups xmm0, xmmword ptr [rdi + 0x20]
0088C4D4  41 0F 11 85 88 00 00 00         movups xmmword ptr [r13 + 0x88], xmm0
0088C4DC  0F 10 4F 30                     movups xmm1, xmmword ptr [rdi + 0x30]
0088C4E0  41 0F 11 8D 98 00 00 00         movups xmmword ptr [r13 + 0x98], xmm1
0088C4E8  F2 0F 10 47 40                  movsd xmm0, qword ptr [rdi + 0x40]
0088C4ED  F2 41 0F 11 85 A8 00 00 00      movsd qword ptr [r13 + 0xa8], xmm0
0088C4F6  48 85 DB                        test rbx, rbx
0088C4F9  74 07                           je 0x14088c502
0088C4FB  49 89 9D A0 00 00 00            mov qword ptr [r13 + 0xa0], rbx
0088C502  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
0088C507  81 E6 00 00 00 C0               and esi, 0xc0000000
0088C50D  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0088C515  81 FE 00 00 00 80               cmp esi, 0x80000000
0088C51B  0F 84 B0 05 00 00               je 0x14088cad1
0088C521  48 83 C1 28                     add rcx, 0x28
0088C525  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
0088C52A  74 17                           je 0x14088c543
0088C52C  48 8D 04 11                     lea rax, [rcx + rdx]
0088C530  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
0088C53A  49 3B C0                        cmp rax, r8
0088C53D  0F 87 B9 05 00 00               ja 0x14088cafc
0088C543  49 89 8D B0 00 00 00            mov qword ptr [r13 + 0xb0], rcx
0088C54A  49 8B 45 60                     mov rax, qword ptr [r13 + 0x60]
0088C54E  BF 00 02 00 00                  mov edi, 0x200
0088C553  48 85 C0                        test rax, rax
0088C556  0F 85 9D 03 00 00               jne 0x14088c8f9
0088C55C  8B CF                           mov ecx, edi
0088C55E  48 8B DA                        mov rbx, rdx
0088C561  48 3B D1                        cmp rdx, rcx
0088C564  76 22                           jbe 0x14088c588
0088C566  48 85 C0                        test rax, rax
0088C569  0F 85 97 03 00 00               jne 0x14088c906
0088C56F  48 3B DF                        cmp rbx, rdi
0088C572  0F 87 D6 01 00 00               ja 0x14088c74e
0088C578  49 8B 8D E0 00 00 00            mov rcx, qword ptr [r13 + 0xe0]
0088C57F  48 85 C9                        test rcx, rcx
0088C582  0F 85 26 03 00 00               jne 0x14088c8ae
0088C588  45 85 FF                        test r15d, r15d
0088C58B  0F 88 71 05 00 00               js 0x14088cb02
0088C591  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0088C599  4C 89 69 08                     mov qword ptr [rcx + 8], r13
0088C59D  0F B7 44 24 52                  movzx eax, word ptr [rsp + 0x52]
0088C5A2  66 89 41 34                     mov word ptr [rcx + 0x34], ax
0088C5A6  0F B7 44 24 54                  movzx eax, word ptr [rsp + 0x54]
0088C5AB  66 89 41 36                     mov word ptr [rcx + 0x36], ax
0088C5AF  0F B7 44 24 56                  movzx eax, word ptr [rsp + 0x56]
0088C5B4  66 89 41 38                     mov word ptr [rcx + 0x38], ax
0088C5B8  49 83 7D 18 00                  cmp qword ptr [r13 + 0x18], 0
0088C5BD  0F 84 E9 00 00 00               je 0x14088c6ac
0088C5C3  49 83 7D 20 00                  cmp qword ptr [r13 + 0x20], 0
0088C5C8  0F 84 4C 03 00 00               je 0x14088c91a
0088C5CE  E8 1D 12 00 00                  call 0x14088d7f0
0088C5D3  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
0088C5DB  48 33 CC                        xor rcx, rsp
0088C5DE  E8 5D 00 E2 FF                  call 0x1406ac640
0088C5E3  48 81 C4 10 01 00 00            add rsp, 0x110
0088C5EA  41 5F                           pop r15
0088C5EC  41 5E                           pop r14
0088C5EE  41 5D                           pop r13
0088C5F0  41 5C                           pop r12
0088C5F2  5F                              pop rdi
0088C5F3  5E                              pop rsi
0088C5F4  5B                              pop rbx
0088C5F5  C3                              ret
0088C5F6  CC                              int3
0088C5F7  4D 85 C0                        test r8, r8
0088C5FA  0F 84 12 02 00 00               je 0x14088c812
0088C600  48 8B D3                        mov rdx, rbx
0088C603  49 8B CE                        mov rcx, r14
0088C606  E8 2D C2 FD FF                  call 0x140868838
0088C60B  E9 A0 FA FF FF                  jmp 0x14088c0b0
0088C610  41 8B 45 28                     mov eax, dword ptr [r13 + 0x28]
0088C614  A9 80 02 00 00                  test eax, 0x280
0088C619  0F 84 E5 FD FF FF               je 0x14088c404
0088C61F  24 80                           and al, 0x80
0088C621  F6 D8                           neg al
0088C623  1B DB                           sbb ebx, ebx
0088C625  81 E3 03 07 00 C0               and ebx, 0xc0000703
0088C62B  48 85 C9                        test rcx, rcx
0088C62E  74 0A                           je 0x14088c63a
0088C630  48 8B D7                        mov rdx, rdi
0088C633  33 C9                           xor ecx, ecx
0088C635  E8 16 11 00 00                  call 0x14088d750
0088C63A  41 B8 00 00 01 00               mov r8d, 0x10000
0088C640  49 8B D5                        mov rdx, r13
0088C643  49 8B CE                        mov rcx, r14
0088C646  E8 D5 7A 00 00                  call 0x140894120
0088C64B  8B C3                           mov eax, ebx
0088C64D  EB 84                           jmp 0x14088c5d3
0088C64F  48 83 7C 24 58 00               cmp qword ptr [rsp + 0x58], 0
0088C655  75 79                           jne 0x14088c6d0
0088C657  48 83 7C 24 60 00               cmp qword ptr [rsp + 0x60], 0
0088C65D  0F 84 91 F9 FF FF               je 0x14088bff4
0088C663  EB 6B                           jmp 0x14088c6d0
0088C665  0F 88 4F FE FF FF               js 0x14088c4ba
0088C66B  49 8B 9D A0 00 00 00            mov rbx, qword ptr [r13 + 0xa0]
0088C672  4D 89 BD A0 00 00 00            mov qword ptr [r13 + 0xa0], r15
0088C679  49 8D 55 68                     lea rdx, [r13 + 0x68]
0088C67D  49 8B CD                        mov rcx, r13
0088C680  E8 CB 10 00 00                  call 0x14088d750
0088C685  E9 30 FE FF FF                  jmp 0x14088c4ba
0088C68A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0088C693  8B 88 A4 05 00 00               mov ecx, dword ptr [rax + 0x5a4]
0088C699  F6 C1 20                        test cl, 0x20
0088C69C  0F 85 E1 04 00 00               jne 0x14088cb83
0088C6A2  44 8B 64 24 68                  mov r12d, dword ptr [rsp + 0x68]
0088C6A7  E9 81 F9 FF FF                  jmp 0x14088c02d
0088C6AC  E8 6F 16 00 00                  call 0x14088dd20
0088C6B1  E9 1D FF FF FF                  jmp 0x14088c5d3
0088C6B6  F0 48 FF 03                     lock inc qword ptr [rbx]
0088C6BA  49 8D 4E 30                     lea rcx, [r14 + 0x30]
0088C6BE  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0088C6C3  48 83 39 00                     cmp qword ptr [rcx], 0
0088C6C7  74 07                           je 0x14088c6d0
0088C6C9  33 D2                           xor edx, edx
0088C6CB  E8 10 79 A1 FF                  call 0x1402a3fe0
0088C6D0  BB 02 07 00 C0                  mov ebx, 0xc0000702
0088C6D5  8B C3                           mov eax, ebx
0088C6D7  E9 F7 FE FF FF                  jmp 0x14088c5d3
0088C6DC  0F B7 D7                        movzx edx, di
0088C6DF  E9 FF F8 FF FF                  jmp 0x14088bfe3
0088C6E4  0F 10 02                        movups xmm0, xmmword ptr [rdx]
0088C6E7  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
0088C6EC  0F 10 4A 10                     movups xmm1, xmmword ptr [rdx + 0x10]
0088C6F0  0F 11 4C 24 60                  movups xmmword ptr [rsp + 0x60], xmm1
0088C6F5  F2 0F 10 42 20                  movsd xmm0, qword ptr [rdx + 0x20]
0088C6FA  F2 0F 11 44 24 70               movsd qword ptr [rsp + 0x70], xmm0
0088C700  F7 86 00 01 00 00 00 10 00 00   test dword ptr [rsi + 0x100], 0x1000
0088C70A  0F 85 03 02 00 00               jne 0x14088c913
0088C710  F6 C3 02                        test bl, 2
0088C713  0F 85 FA 01 00 00               jne 0x14088c913
0088C719  32 C0                           xor al, al
0088C71B  0F B7 54 24 50                  movzx edx, word ptr [rsp + 0x50]
0088C720  44 8D 42 28                     lea r8d, [rdx + 0x28]
0088C724  66 41 3B D0                     cmp dx, r8w
0088C728  73 1A                           jae 0x14088c744
0088C72A  84 C0                           test al, al
0088C72C  0F 85 F2 01 00 00               jne 0x14088c924
0088C732  48 8D 4A 28                     lea rcx, [rdx + 0x28]
0088C736  0F B7 44 24 52                  movzx eax, word ptr [rsp + 0x52]
0088C73B  48 3B C8                        cmp rcx, rax
0088C73E  0F 84 2D F8 FF FF               je 0x14088bf71
0088C744  B8 0D 00 00 C0                  mov eax, 0xc000000d
0088C749  E9 85 FE FF FF                  jmp 0x14088c5d3
0088C74E  48 81 FB D7 FF 00 00            cmp rbx, 0xffd7
0088C755  0F 87 17 02 00 00               ja 0x14088c972
0088C75B  49 8B B5 E8 00 00 00            mov rsi, qword ptr [r13 + 0xe8]
0088C762  48 8D 04 37                     lea rax, [rdi + rsi]
0088C766  48 3B D8                        cmp rbx, rax
0088C769  0F 86 19 FE FF FF               jbe 0x14088c588
0088C76F  49 8B 8D E0 00 00 00            mov rcx, qword ptr [r13 + 0xe0]
0088C776  48 85 C9                        test rcx, rcx
0088C779  0F 85 DD 01 00 00               jne 0x14088c95c
0088C77F  48 2B DF                        sub rbx, rdi
0088C782  41 B8 41 6C 45 42               mov r8d, 0x42456c41
0088C788  48 8B D3                        mov rdx, rbx
0088C78B  B9 00 01 00 00                  mov ecx, 0x100
0088C790  E8 5B 59 2F 00                  call 0x140b820f0
0088C795  49 89 85 E0 00 00 00            mov qword ptr [r13 + 0xe0], rax
0088C79C  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
0088C7A0  48 85 C0                        test rax, rax
0088C7A3  0F 84 9F 01 00 00               je 0x14088c948
0088C7A9  49 89 9D E8 00 00 00            mov qword ptr [r13 + 0xe8], rbx
0088C7B0  48 85 C9                        test rcx, rcx
0088C7B3  0F 84 CF FD FF FF               je 0x14088c588
0088C7B9  48 2B DE                        sub rbx, rsi
0088C7BC  48 8B D3                        mov rdx, rbx
0088C7BF  E8 E0 66 09 00                  call 0x140922ea4
0088C7C4  8B D8                           mov ebx, eax
0088C7C6  85 C0                           test eax, eax
0088C7C8  0F 89 BA FD FF FF               jns 0x14088c588
0088C7CE  BA 41 6C 45 42                  mov edx, 0x42456c41
0088C7D3  49 8B 8D E0 00 00 00            mov rcx, qword ptr [r13 + 0xe0]
0088C7DA  E8 91 60 2F 00                  call 0x140b82870
0088C7DF  4D 89 BD E0 00 00 00            mov qword ptr [r13 + 0xe0], r15
0088C7E6  4D 89 BD E8 00 00 00            mov qword ptr [r13 + 0xe8], r15
0088C7ED  48 8B D6                        mov rdx, rsi
0088C7F0  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
0088C7F4  E8 EF 66 09 00                  call 0x140922ee8
0088C7F9  44 8B FB                        mov r15d, ebx
0088C7FC  E9 87 FD FF FF                  jmp 0x14088c588
0088C801  B8 41 00 00 C0                  mov eax, 0xc0000041
0088C806  E9 C8 FD FF FF                  jmp 0x14088c5d3
0088C80B  B0 01                           mov al, 1
0088C80D  E9 7A F7 FF FF                  jmp 0x14088bf8c
0088C812  33 DB                           xor ebx, ebx
0088C814  44 0F B6 C6                     movzx r8d, sil
0088C818  48 8B D7                        mov rdx, rdi
0088C81B  49 8B CE                        mov rcx, r14
0088C81E  E8 5D 3D BB FF                  call 0x140440580
0088C823  E9 A6 F8 FF FF                  jmp 0x14088c0ce
0088C828  49 8B 55 10                     mov rdx, qword ptr [r13 + 0x10]
0088C82C  48 3B D6                        cmp rdx, rsi
0088C82F  0F 85 06 02 00 00               jne 0x14088ca3b
0088C835  8B C1                           mov eax, ecx
0088C837  83 E0 07                        and eax, 7
0088C83A  3C 03                           cmp al, 3
0088C83C  75 0A                           jne 0x14088c848
0088C83E  0F BA E1 0D                     bt ecx, 0xd
0088C842  0F 83 C3 F9 FF FF               jae 0x14088c20b
0088C848  49 8B CD                        mov rcx, r13
0088C84B  E8 90 B2 00 00                  call 0x140897ae0
0088C850  B8 22 00 00 C0                  mov eax, 0xc0000022
0088C855  E9 79 FD FF FF                  jmp 0x14088c5d3
0088C85A  F6 C3 01                        test bl, 1
0088C85D  0F 85 19 02 00 00               jne 0x14088ca7c
0088C863  44 0F B7 C2                     movzx r8d, dx
0088C867  0F BA E3 10                     bt ebx, 0x10
0088C86B  0F 83 0C 01 00 00               jae 0x14088c97d
0088C871  45 85 C0                        test r8d, r8d
0088C874  0F 85 19 01 00 00               jne 0x14088c993
0088C87A  41 8D 50 03                     lea edx, [r8 + 3]
0088C87E  BF 01 00 00 00                  mov edi, 1
0088C883  45 33 FF                        xor r15d, r15d
0088C886  45 8B E7                        mov r12d, r15d
0088C889  41 0F 10 81 08 05 00 00         movups xmm0, xmmword ptr [r9 + 0x508]
0088C891  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
0088C896  44 89 64 24 68                  mov dword ptr [rsp + 0x68], r12d
0088C89B  45 84 D2                        test r10b, r10b
0088C89E  0F 85 5D F7 FF FF               jne 0x14088c001
0088C8A4  44 89 7C 24 70                  mov dword ptr [rsp + 0x70], r15d
0088C8A9  E9 53 F7 FF FF                  jmp 0x14088c001
0088C8AE  BA 41 6C 45 42                  mov edx, 0x42456c41
0088C8B3  E8 B8 5F 2F 00                  call 0x140b82870
0088C8B8  4D 89 BD E0 00 00 00            mov qword ptr [r13 + 0xe0], r15
0088C8BF  49 8B 4D 30                     mov rcx, qword ptr [r13 + 0x30]
0088C8C3  48 85 C9                        test rcx, rcx
0088C8C6  74 25                           je 0x14088c8ed
0088C8C8  49 8B 95 E8 00 00 00            mov rdx, qword ptr [r13 + 0xe8]
0088C8CF  48 8B 81 98 05 00 00            mov rax, qword ptr [rcx + 0x598]
0088C8D6  48 03 C2                        add rax, rdx
0088C8D9  48 3D 00 10 00 00               cmp rax, 0x1000
0088C8DF  0F 83 F5 01 00 00               jae 0x14088cada
0088C8E5  F0 48 01 91 98 05 00 00         lock add qword ptr [rcx + 0x598], rdx
0088C8ED  4D 89 BD E8 00 00 00            mov qword ptr [r13 + 0xe8], r15
0088C8F4  E9 8F FC FF FF                  jmp 0x14088c588
0088C8F9  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
0088C8FD  48 83 E9 28                     sub rcx, 0x28
0088C901  E9 58 FC FF FF                  jmp 0x14088c55e
0088C906  48 8B 78 20                     mov rdi, qword ptr [rax + 0x20]
0088C90A  48 83 EF 28                     sub rdi, 0x28
0088C90E  E9 5C FC FF FF                  jmp 0x14088c56f
0088C913  B0 01                           mov al, 1
0088C915  E9 01 FE FF FF                  jmp 0x14088c71b
0088C91A  E8 61 2F 00 00                  call 0x14088f880
0088C91F  E9 AF FC FF FF                  jmp 0x14088c5d3
0088C924  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0088C929  48 C1 E8 10                     shr rax, 0x10
0088C92D  0F B7 C8                        movzx ecx, ax
0088C930  48 8D 42 28                     lea rax, [rdx + 0x28]
0088C934  48 3B C1                        cmp rax, rcx
0088C937  0F 87 07 FE FF FF               ja 0x14088c744
0088C93D  66 44 89 44 24 52               mov word ptr [rsp + 0x52], r8w
0088C943  E9 29 F6 FF FF                  jmp 0x14088bf71
0088C948  48 85 C9                        test rcx, rcx
0088C94B  0F 85 73 01 00 00               jne 0x14088cac4
0088C951  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
0088C957  E9 2C FC FF FF                  jmp 0x14088c588
0088C95C  BA 41 6C 45 42                  mov edx, 0x42456c41
0088C961  E8 0A 5F 2F 00                  call 0x140b82870
0088C966  4D 89 BD E8 00 00 00            mov qword ptr [r13 + 0xe8], r15
0088C96D  E9 0D FE FF FF                  jmp 0x14088c77f
0088C972  41 BF 05 00 00 80               mov r15d, 0x80000005
0088C978  E9 0B FC FF FF                  jmp 0x14088c588
0088C97D  45 85 C0                        test r8d, r8d
0088C980  0F 85 BE 01 00 00               jne 0x14088cb44
0088C986  BF 01 00 00 00                  mov edi, 1
0088C98B  0F B7 D7                        movzx edx, di
0088C98E  E9 F0 FE FF FF                  jmp 0x14088c883
0088C993  41 83 E8 03                     sub r8d, 3
0088C997  74 18                           je 0x14088c9b1
0088C999  41 83 E8 01                     sub r8d, 1
0088C99D  74 12                           je 0x14088c9b1
0088C99F  41 83 E8 01                     sub r8d, 1
0088C9A3  74 0C                           je 0x14088c9b1
0088C9A5  41 83 E8 01                     sub r8d, 1
0088C9A9  74 06                           je 0x14088c9b1
0088C9AB  41 83 F8 07                     cmp r8d, 7
0088C9AF  75 09                           jne 0x14088c9ba
0088C9B1  F6 C3 02                        test bl, 2
0088C9B4  0F 85 C4 FE FF FF               jne 0x14088c87e
0088C9BA  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0088C9BF  8B C3                           mov eax, ebx
0088C9C1  E9 0D FC FF FF                  jmp 0x14088c5d3
0088C9C6  45 33 FF                        xor r15d, r15d
0088C9C9  41 8B DF                        mov ebx, r15d
0088C9CC  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
0088C9D0  48 85 C9                        test rcx, rcx
0088C9D3  74 1A                           je 0x14088c9ef
0088C9D5  48 8B D0                        mov rdx, rax
0088C9D8  0F BA F2 1F                     btr edx, 0x1f
0088C9DC  48 83 C1 28                     add rcx, 0x28
0088C9E0  4C 8D 05 F1 4A 77 FF            lea r8, [rip - 0x88b50f]
0088C9E7  E8 14 D5 FF FF                  call 0x140889f00
0088C9EC  48 8B D8                        mov rbx, rax
0088C9EF  48 85 DB                        test rbx, rbx
0088C9F2  0F 84 7F 01 00 00               je 0x14088cb77
0088C9F8  4C 8B 6B 18                     mov r13, qword ptr [rbx + 0x18]
0088C9FC  49 8B CD                        mov rcx, r13
0088C9FF  E8 AC DE FF FF                  call 0x14088a8b0
0088CA04  33 C0                           xor eax, eax
0088CA06  F0 0F B1 7B 28                  lock cmpxchg dword ptr [rbx + 0x28], edi
0088CA0B  0F 85 DC 01 00 00               jne 0x14088cbed
0088CA11  41 81 A5 08 01 00 00 FF FF FF 7F  and dword ptr [r13 + 0x108], 0x7fffffff
0088CA1C  0F 1F 40 00                     nop dword ptr [rax]
0088CA20  8B C7                           mov eax, edi
0088CA22  F0 0F C1 05 D6 28 74 00         lock xadd dword ptr [rip + 0x7428d6], eax
0088CA2A  83 C0 01                        add eax, 1
0088CA2D  74 F1                           je 0x14088ca20
0088CA2F  41 89 85 10 01 00 00            mov dword ptr [r13 + 0x110], eax
0088CA36  E9 B0 F7 FF FF                  jmp 0x14088c1eb
0088CA3B  F6 C1 07                        test cl, 7
0088CA3E  0F 84 C7 01 00 00               je 0x14088cc0b
0088CA44  8B 86 A0 01 00 00               mov eax, dword ptr [rsi + 0x1a0]
0088CA4A  83 E0 06                        and eax, 6
0088CA4D  3C 06                           cmp al, 6
0088CA4F  0F 85 F3 FD FF FF               jne 0x14088c848
0088CA55  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
0088CA59  48 85 C0                        test rax, rax
0088CA5C  0F 84 E6 FD FF FF               je 0x14088c848
0088CA62  48 39 10                        cmp qword ptr [rax], rdx
0088CA65  0F 84 CA FD FF FF               je 0x14088c835
0088CA6B  E9 D8 FD FF FF                  jmp 0x14088c848
0088CA70  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0088CA75  8B C3                           mov eax, ebx
0088CA77  E9 57 FB FF FF                  jmp 0x14088c5d3
0088CA7C  45 85 E4                        test r12d, r12d
0088CA7F  0F 84 35 FF FF FF               je 0x14088c9ba
0088CA85  45 33 FF                        xor r15d, r15d
0088CA88  41 8B CF                        mov ecx, r15d
0088CA8B  41 8D 57 02                     lea edx, [r15 + 2]
0088CA8F  8D 7A FF                        lea edi, [rdx - 1]
0088CA92  E9 FF FD FF FF                  jmp 0x14088c896
0088CA97  45 84 D2                        test r10b, r10b
0088CA9A  0F 85 28 F5 FF FF               jne 0x14088bfc8
0088CAA0  BF 01 00 00 00                  mov edi, 1
0088CAA5  E9 39 F5 FF FF                  jmp 0x14088bfe3
0088CAAA  F7 86 00 01 00 00 00 10 00 00   test dword ptr [rsi + 0x100], 0x1000
0088CAB4  0F 85 39 F3 FF FF               jne 0x14088bdf3
0088CABA  B8 37 00 00 C0                  mov eax, 0xc0000037
0088CABF  E9 0F FB FF FF                  jmp 0x14088c5d3
0088CAC4  48 8B D6                        mov rdx, rsi
0088CAC7  E8 1C 64 09 00                  call 0x140922ee8
0088CACC  E9 80 FE FF FF                  jmp 0x14088c951
0088CAD1  48 83 C1 18                     add rcx, 0x18
0088CAD5  E9 4B FA FF FF                  jmp 0x14088c525
0088CADA  E8 81 9D A1 FF                  call 0x1402a6860
0088CADF  E9 09 FE FF FF                  jmp 0x14088c8ed
0088CAE4  49 83 7D 10 00                  cmp qword ptr [r13 + 0x10], 0
0088CAE9  0F 85 DA F6 FF FF               jne 0x14088c1c9
0088CAEF  49 8B CD                        mov rcx, r13
0088CAF2  E8 E9 AF 00 00                  call 0x140897ae0
0088CAF7  E9 D4 FB FF FF                  jmp 0x14088c6d0
0088CAFC  41 BF 05 00 00 C0               mov r15d, 0xc0000005
0088CB02  49 8B CD                        mov rcx, r13
0088CB05  E8 D6 AF 00 00                  call 0x140897ae0
0088CB0A  41 8B C7                        mov eax, r15d
0088CB0D  E9 C1 FA FF FF                  jmp 0x14088c5d3
0088CB12  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0088CB17  41 B9 26 00 00 00               mov r9d, 0x26
0088CB1D  4D 8B C5                        mov r8, r13
0088CB20  33 D2                           xor edx, edx
0088CB22  8D 4A 18                        lea ecx, [rdx + 0x18]
0088CB25  E8 36 0B C7 FF                  call 0x1404fd660
0088CB2A  CC                              int3
0088CB2B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0088CB30  41 B9 26 00 00 00               mov r9d, 0x26
0088CB36  4D 8B C5                        mov r8, r13
0088CB39  33 D2                           xor edx, edx
0088CB3B  8D 4A 18                        lea ecx, [rdx + 0x18]
0088CB3E  E8 1D 0B C7 FF                  call 0x1404fd660
0088CB43  CC                              int3
0088CB44  41 83 E8 01                     sub r8d, 1
0088CB48  0F 84 8A 00 00 00               je 0x14088cbd8
0088CB4E  41 83 E8 06                     sub r8d, 6
0088CB52  74 10                           je 0x14088cb64
0088CB54  41 83 E8 01                     sub r8d, 1
0088CB58  74 0A                           je 0x14088cb64
0088CB5A  41 83 F8 01                     cmp r8d, 1
0088CB5E  0F 85 56 FE FF FF               jne 0x14088c9ba
0088CB64  F6 C3 02                        test bl, 2
0088CB67  0F 84 4D FE FF FF               je 0x14088c9ba
0088CB6D  BF 01 00 00 00                  mov edi, 1
0088CB72  E9 0C FD FF FF                  jmp 0x14088c883
0088CB77  BB F0 02 00 C0                  mov ebx, 0xc00002f0
0088CB7C  8B C3                           mov eax, ebx
0088CB7E  E9 50 FA FF FF                  jmp 0x14088c5d3
0088CB83  B8 01 00 00 C0                  mov eax, 0xc0000001
0088CB88  E9 46 FA FF FF                  jmp 0x14088c5d3
0088CB8D  B8 07 07 00 C0                  mov eax, 0xc0000707
0088CB92  E9 3C FA FF FF                  jmp 0x14088c5d3
0088CB97  B8 2F 00 00 C0                  mov eax, 0xc000002f
0088CB9C  E9 32 FA FF FF                  jmp 0x14088c5d3
0088CBA1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0088CBAA  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0088CBB1  49 89 4D 30                     mov qword ptr [r13 + 0x30], rcx
0088CBB5  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0088CBBE  BA 41 6C 70 63                  mov edx, 0x63706c41
0088CBC3  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0088CBCA  E8 41 3B 98 FF                  call 0x140210710
0088CBCF  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
0088CBD3  E9 D8 F7 FF FF                  jmp 0x14088c3b0
0088CBD8  45 85 E4                        test r12d, r12d
0088CBDB  0F 84 D9 FD FF FF               je 0x14088c9ba
0088CBE1  45 33 FF                        xor r15d, r15d
0088CBE4  41 8D 7F 01                     lea edi, [r15 + 1]
0088CBE8  E9 9C FC FF FF                  jmp 0x14088c889
0088CBED  49 8B CD                        mov rcx, r13
0088CBF0  E8 EB AE 00 00                  call 0x140897ae0
0088CBF5  8B D7                           mov edx, edi
0088CBF7  48 8B CB                        mov rcx, rbx
0088CBFA  E8 01 E3 FF FF                  call 0x14088af00
0088CBFF  BB 08 07 00 C0                  mov ebx, 0xc0000708
0088CC04  8B C3                           mov eax, ebx
0088CC06  E9 C8 F9 FF FF                  jmp 0x14088c5d3
0088CC0B  48 8B 5F 10                     mov rbx, qword ptr [rdi + 0x10]
0088CC0F  45 33 C0                        xor r8d, r8d
0088CC12  33 D2                           xor edx, edx
0088CC14  48 8D 4B F0                     lea rcx, [rbx - 0x10]
0088CC18  E8 13 36 98 FF                  call 0x140210230
0088CC1D  48 8B F0                        mov rsi, rax
0088CC20  B9 11 00 00 00                  mov ecx, 0x11
0088CC25  33 C0                           xor eax, eax
0088CC27  F0 48 0F B1 4B F0               lock cmpxchg qword ptr [rbx - 0x10], rcx
0088CC2D  74 17                           je 0x14088cc46
0088CC2F  4C 8D 4B F0                     lea r9, [rbx - 0x10]
0088CC33  4C 8B C6                        mov r8, rsi
0088CC36  33 D2                           xor edx, edx
0088CC38  48 8D 4B F0                     lea rcx, [rbx - 0x10]
0088CC3C  E8 0B 38 98 FF                  call 0x14021044c
0088CC41  B9 11 00 00 00                  mov ecx, 0x11
0088CC46  48 85 F6                        test rsi, rsi
0088CC49  74 04                           je 0x14088cc4f
0088CC4B  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0088CC4F  8B 87 A0 01 00 00               mov eax, dword ptr [rdi + 0x1a0]
0088CC55  D1 E8                           shr eax, 1
0088CC57  83 E0 03                        and eax, 3
0088CC5A  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
0088CC5F  83 F8 02                        cmp eax, 2
0088CC62  75 10                           jne 0x14088cc74
0088CC64  4C 39 33                        cmp qword ptr [rbx], r14
0088CC67  74 4D                           je 0x14088ccb6
0088CC69  4C 39 73 08                     cmp qword ptr [rbx + 8], r14
0088CC6D  74 47                           je 0x14088ccb6
0088CC6F  40 32 FF                        xor dil, dil
0088CC72  EB 08                           jmp 0x14088cc7c
0088CC74  4C 39 73 10                     cmp qword ptr [rbx + 0x10], r14
0088CC78  40 0F 94 C7                     sete dil
0088CC7C  48 8B C1                        mov rax, rcx
0088CC7F  F0 4C 0F B1 7B F0               lock cmpxchg qword ptr [rbx - 0x10], r15
0088CC85  75 5B                           jne 0x14088cce2
0088CC87  48 8D 4B F0                     lea rcx, [rbx - 0x10]
0088CC8B  E8 70 49 A5 FF                  call 0x1402e1600
0088CC90  40 84 FF                        test dil, dil
0088CC93  0F 84 AF FB FF FF               je 0x14088c848
0088CC99  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
0088CC9D  E9 6E F5 FF FF                  jmp 0x14088c210
0088CCA2  48 8B 0D 87 84 73 00            mov rcx, qword ptr [rip + 0x738487]
0088CCA9  48 85 C9                        test rcx, rcx
0088CCAC  75 0D                           jne 0x14088ccbb
0088CCAE  45 33 F6                        xor r14d, r14d
0088CCB1  E9 A9 F3 FF FF                  jmp 0x14088c05f
0088CCB6  40 B7 01                        mov dil, 1
0088CCB9  EB C1                           jmp 0x14088cc7c
0088CCBB  C1 E8 1A                        shr eax, 0x1a
0088CCBE  4C 8B 34 C1                     mov r14, qword ptr [rcx + rax*8]
0088CCC2  E9 98 F3 FF FF                  jmp 0x14088c05f
0088CCC7  74 36                           je 0x14088ccff
0088CCC9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0088CCCE  41 B9 20 00 00 00               mov r9d, 0x20
0088CCD4  4D 8B C5                        mov r8, r13
0088CCD7  33 D2                           xor edx, edx
0088CCD9  8D 4A 18                        lea ecx, [rdx + 0x18]
0088CCDC  E8 7F 09 C7 FF                  call 0x1404fd660
0088CCE1  CC                              int3
0088CCE2  48 8D 4B F0                     lea rcx, [rbx - 0x10]
0088CCE6  E8 55 67 9D FF                  call 0x140263440
0088CCEB  EB 9A                           jmp 0x14088cc87
0088CCED  49 8B CD                        mov rcx, r13
0088CCF0  E8 EB AD 00 00                  call 0x140897ae0
0088CCF5  BB 22 00 00 C0                  mov ebx, 0xc0000022
0088CCFA  E9 D6 F9 FF FF                  jmp 0x14088c6d5
0088CCFF  48 8B D3                        mov rdx, rbx
0088CD02  49 8B CE                        mov rcx, r14
0088CD05  E8 C6 05 0C 00                  call 0x14094d2d0
0088CD0A  E9 C1 F9 FF FF                  jmp 0x14088c6d0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpSendMessage(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned __int8 v_stack_m107;
    unsigned __int8 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int8 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int16 v_stack_mF2;
    unsigned __int16 v_stack_mF4;
    unsigned __int16 v_stack_mF6;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p50;
    unsigned __int16 v_stack_p52;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 5761508)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m108 = a4;
    v_stack_mC8 = a3;
    v_stack_mC0 = a2;
    v_stack_mB8 = a1;
    a1 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm0;
    v_stack_mD8 = 0;
    v_stack_mA8 = v_xmm1;
    v_stack_m98 = v_xmm1;
    v_stack_m88 = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 120) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    v_stack_mD0 = *(unsigned __int64 *)(a1);
    v_stack_m100 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 416)))) & (16)) != 0) goto loc_0088C801;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 416)))) & (8)) != 0) goto loc_0088CB8D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 416)))) & (32)) != 0) goto loc_0088CAAA;
loc_0088BDF3:
    if (a4 == 0) goto loc_0088C6E4;
    result = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) & (0xC0000000ULL));
    if (((unsigned int)(result)) == 0x80000000ULL) goto loc_0088BEC3;
    a2 = v_r14;
    if (a2 < v_r14) { a2 = a2; }
    result = RtlCopyVolatileMemory(v_stack_mF8, a2, 40, a4);
loc_0088BE4F:
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1) + 256)) & (0x1000ULL)) != 0) goto loc_0088BEAB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 48)))) & (2)) != 0) goto loc_0088BEAB;
    a1 = 0;
loc_0088BE62:
    v_stack_m107 = 0;
    if (((unsigned __int16)(v_stack_mF8)) >= ((unsigned __int16)(v_stack_mF8 + 40))) goto loc_0088BF62;
    if (0 != 0) goto loc_0088BEAF;
    a1 = ((unsigned __int16)(v_stack_mF8)) + (40);
    if (a1 != ((unsigned __int16)(v_stack_mF6))) goto loc_0088BF62;
loc_0088BE8A:
    if (v_stack_mF2 != 0) goto loc_0088BF44;
loc_0088BEA0:
    goto loc_0088BF71;
loc_0088BEAB:
    goto loc_0088BE62;
loc_0088BEAF:
    a1 = (1) + (40);
    if (a1 > ((unsigned int)(0x7FFFULL))) goto loc_0088BF62;
    v_stack_mF6 = (unsigned __int16)(a1);
    goto loc_0088BE8A;
loc_0088BEC3:
    a2 = (unsigned int)(0x7FFFULL);
    if (a2 < ((unsigned int)(0x7FFFULL))) { a2 = a2; }
    result = RtlCopyVolatileMemory(v_stack_m58, a2, 24, a4);
    v_stack_mF8 = (unsigned __int16)(v_stack_m58);
    v_stack_mF6 = (unsigned __int16)(v_stack_m58 + 40);
    v_stack_mF4 = (unsigned int)((unsigned int)(v_stack_m54));
    v_stack_mF0 = (unsigned int)(v_stack_m50);
    v_stack_mE8 = (unsigned int)(v_stack_m4C);
    v_stack_mE0 = (unsigned int)((unsigned int)(v_stack_m48));
    v_stack_mD8 = (unsigned int)(v_stack_m44);
    v_stack_mD8 = (unsigned int)((unsigned int)(v_stack_m44));
    goto loc_0088BE4F;
loc_0088BF44:
    result = AlpcpValidateDataInformation(a2, v_stack_mF8, v_stack_m58 + 40, a4);
    v_stack_m104 = (unsigned int)(result);
    if (!sign_flag) goto loc_0088BEA0;
    goto loc_0088C5D3;
loc_0088BF62:
    goto loc_0088C5D3;
loc_0088BF71:
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1) + 256)) & (0x1000ULL)) != 0) goto loc_0088C80B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 48)))) & (2)) != 0) goto loc_0088C80B;
    result = 0;
loc_0088BF8C:
    a2 = (unsigned __int16)(((unsigned __int16)(v_stack_mF4)) & (255));
    a1 = (unsigned __int16)((v_stack_mF4) & ((unsigned __int16)((unsigned int)(0xFF00ULL))));
    if (0 != 0) goto loc_0088C85A;
    if (((unsigned __int16)(a2)) == 7) goto loc_0088CA97;
loc_0088BFC8:
    if ((unsigned int)((unsigned int)(v_stack_mE0)) != 0) goto loc_0088C27E;
loc_0088BFD1:
    if (condition_is_above_or_equal) goto loc_0088C6DC;
loc_0088BFE3:
    v_r15 = 0;
loc_0088BFE6:
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_0088C64F;
loc_0088BFF4:
    v_stack_mF0 = v_xmm0;
loc_0088C001:
    a1 = (unsigned __int16)((a1) & ((unsigned __int16)((unsigned int)(0xEFFFULL))));
    a1 = (unsigned __int16)((a1) | ((unsigned __int16)(1 + 2)));
    v_stack_mF4 = (unsigned __int16)(a1);
    if (v_stack_mF6 > (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 272))) goto loc_0088CB97;
    if (v_stack_mF6 < (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 272))) goto loc_0088C68A;
loc_0088C02D:
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_0088C2A0;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) | (16));
    v_stack_m100 = (unsigned int)(v_rbx);
    if (sign_flag) goto loc_0088C9C6;
    if ((((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mE0))))) & (0xFC000000ULL)) != 0) goto loc_0088CCA2;
loc_0088C05F:
    if (*(unsigned __int64 *)(v_rip + 7581449) == 0) goto loc_0088C6D0;
    v_rdi = (unsigned int)((v_stack_mE0) & (0x3FFFFFFULL));
    if ((((unsigned int)(v_rdi)) & (0x3FCULL)) == 0) goto loc_0088C812;
    result = ExpLookupHandleTableEntry(*(unsigned __int64 *)(v_rip + 7581449), (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0xFF00ULL), *(unsigned __int64 *)(gs_base + (0 + 392)));
    if (result == 0) goto loc_0088C812;
loc_0088C0B0:
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (1)) == 0) goto loc_0088C5F7;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (1)) != 0) goto loc_0088C0B0;
loc_0088C0CE:
    if (result == 0) goto loc_0088C6D0;
    result = ExGetHandlePointer(result, (unsigned int)((unsigned int)(v_rdi)), *(unsigned __int64 *)(result), *(unsigned __int64 *)(gs_base + (0 + 392)));
    if ((*(unsigned int *)(result + 264)) != ((unsigned int)((unsigned int)(v_stack_mE0)))) goto loc_0088C6B6;
    if ((unsigned int)((unsigned int)(v_stack_mD8)) == 0) goto loc_0088C101;
    if ((*(unsigned int *)(result + 272)) != ((unsigned int)((unsigned int)(v_stack_mD8)))) goto loc_0088C6B6;
loc_0088C101:
loc_0088C109:
    if (condition_is_less_or_equal) goto loc_0088CCC7;
    if ((*(unsigned __int64 *)(result - 24)) != (*(unsigned __int64 *)(result - 24))) goto loc_0088C109;
    result = (*(unsigned __int64 *)(result - 24)) + (1);
    if (condition_is_equal) goto loc_0088CCFF;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result - 16, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 392)));
    if (!(condition_is_above_or_equal)) {
        a3 = result - 16;
        a2 = result;
        a1 = result - 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 392)));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ((unsigned int)(0x10000ULL)) + (0x10000ULL);
    if (condition_is_less_or_equal) goto loc_0088CB12;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7581449) + 48)) != 0) {
        a2 = 0;
        result = ExfUnblockPushLock(*(unsigned __int64 *)(v_rip + 7581449) + 48, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 392)));
    }
    if ((*(unsigned int *)(result + 264)) != ((unsigned int)((unsigned int)(v_stack_mE0)))) goto loc_0088CAEF;
    if ((unsigned int)((unsigned int)(v_stack_mD8)) == 0) goto loc_0088C1BE;
    if ((*(unsigned int *)(result + 272)) != ((unsigned int)((unsigned int)(v_stack_mD8)))) goto loc_0088CAEF;
loc_0088C1BE:
    if ((*(unsigned __int64 *)(result + 24)) == 0) goto loc_0088CAE4;
loc_0088C1C9:
    if ((*(unsigned __int64 *)(result + 184)) == (*(unsigned __int64 *)(v_stack_mD0 + 16))) goto loc_0088C1E8;
    if ((*(unsigned __int64 *)(result + 192)) != v_stack_mD0) goto loc_0088CCED;
loc_0088C1E8:
    v_r15 = 0;
loc_0088C1EB:
    v_stack_m104 = 0;
    if (sign_flag) goto loc_0088C3A7;
    if (*(unsigned __int64 *)(result + 24) != 0) goto loc_0088C828;
loc_0088C20B:
loc_0088C210:
    if ((*(unsigned __int64 *)(result + 32)) == 0) goto loc_0088C3AC;
    if ((*(unsigned __int64 *)(result + 48)) != 0) goto loc_0088C3B0;
    if ((((unsigned int)((unsigned int)(v_stack_m100))) & (0x30000ULL)) != 0) goto loc_0088C3B0;
    if ((*(unsigned __int64 *)(result + 224)) != 0) {
        a2 = (792) + (*(unsigned __int64 *)(result + 232));
    }
    result = AlpcpChargePagedPoolQuota(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, a3, *(unsigned __int64 *)(gs_base + (0 + 392)));
    v_stack_m104 = (unsigned int)(result);
    if (!sign_flag) goto loc_0088CBA1;
loc_0088C26F:
    result = AlpcpUnlockMessage(result, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 392)));
    goto loc_0088C5D3;
loc_0088C27E:
    if (sign_flag) goto loc_0088BFD1;
    result = (condition_is_below) ? 1 : 0;
    goto loc_0088BFE6;
loc_0088C2A0:
    result = ExAllocateFromPagedLookasideList(v_rip + 5877465, result + 1, a3, *(unsigned __int64 *)(gs_base + (0 + 392)));
    if (result == 0) goto loc_0088CA70;
    *(unsigned __int16 *)(result + 16) = 512;
    *(unsigned int *)(result + 18) = 0;
    *(unsigned __int16 *)(result + 22) = 0;
    *(unsigned __int64 *)(result + 40) = 0;
    *(unsigned __int64 *)(result + 32) = 0;
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    *(unsigned __int64 *)(result + 24) = 0 + 1;
    if (result + 48 == 0) goto loc_0088CA70;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 32, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 392)));
    if (!(condition_is_above_or_equal)) {
        a3 = result + 32;
        a2 = result;
        a1 = result + 32;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int64 *)(gs_base + (0 + 392)));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ((unsigned int)(0x10000ULL)) + (0x10000ULL);
    if (condition_is_less_or_equal) goto loc_0088CB2B;
    a2 = 0;
    result = memset(result + 48, a2, 280, *(unsigned __int64 *)(gs_base + (0 + 392)));
    *(unsigned __int16 *)(result + 48 + 242) = 40;
    *(unsigned int *)(result + 48 + 264) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 48 + 264)));
loc_0088C371:
    result = (unsigned int)(((unsigned int)((unsigned int)(0 + 1))) + (1));
    if (condition_is_equal) goto loc_0088C371;
    *(unsigned int *)(result + 48 + 272) = (unsigned int)(result);
    if ((*(unsigned int *)(v_rip + 6831426)) != 0) {
        a1 = result + 48;
        result = AlpcpEnterAllocationEventMessageLog(a1, a2, 280, *(unsigned __int64 *)(gs_base + (0 + 392)));
    }
    *(unsigned __int16 *)(result + 48 + 242) = 40;
    v_stack_m104 = 0;
loc_0088C3A7:
loc_0088C3AC:
loc_0088C3B0:
    if (sign_flag) goto loc_0088C6D5;
    v_rbx = 0;
    v_rdi = 0;
    if (v_stack_mC8 != 0) {
        v_rdi = v_stack_mA8;
        result = v_stack_mA8;
        v_stack_m128 = result;
        a4 = result + 48;
        a3 = v_stack_mC8;
        a2 = (unsigned int)((unsigned int)(v_stack_m100));
        a1 = v_stack_mD0;
        result = AlpcpCaptureAttributes(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
        v_stack_m104 = (unsigned int)(result);
        a1 = v_stack_mC8;
    }
    if ((unsigned int)((unsigned int)(v_stack_mE0)) != 0) goto loc_0088C610;
loc_0088C404:
    if (sign_flag) goto loc_0088C26F;
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_0088C4AE;
    if (*(unsigned __int64 *)(result + 48 + 208) != 0) {
        a4 = *(unsigned int *)(result + 48 + 264);
        result = (unsigned int)(*(unsigned __int64 *)(result + 48 + 208));
        result = (unsigned int)((result) & (7));
        a1 = (*(unsigned __int64 *)(result + 48 + 208)) & (-8);
        a3 = 0;
        if (((unsigned int)(result)) != 7) { a3 = (unsigned int)(result); }
        a2 = 2;
        if (((unsigned int)(result)) != 7) { a2 = 0; }
        v_stack_m118 = 0;
        v_stack_m120 = 1;
        v_stack_m128 = 0xFFFFFFFFULL;
        result = PspChargeProcessWakeCounter(a1, a2, a3, a4);
        *(unsigned __int64 *)(result + 48 + 208) = 0;
    }
    v_rbx = 2;
    if (*(unsigned __int64 *)(result + 48 + 216) != 0) {
        a4 = *(unsigned int *)(result + 48 + 264);
        result = (unsigned int)(*(unsigned __int64 *)(result + 48 + 216));
        result = (unsigned int)((result) & (7));
        a1 = (*(unsigned __int64 *)(result + 48 + 216)) & (-8);
        a3 = 0;
        if (((unsigned int)(result)) != 7) { a3 = (unsigned int)(result); }
        v_rbx = 2;
        if (((unsigned int)(result)) != 7) { v_rbx = 0; }
        v_stack_m118 = 0;
        v_stack_m120 = 1;
        v_stack_m128 = 0xFFFFFFFFULL;
        a2 = (unsigned int)(v_rbx);
        result = PspChargeProcessWakeCounter(a1, a2, a3, a4);
        *(unsigned __int64 *)(result + 48 + 216) = 0;
    }
    if ((unsigned int)((unsigned int)(v_stack_mE0)) != 0) goto loc_0088C665;
loc_0088C4BA:
    if (v_rdi != 0) {
        *(unsigned __int64 *)(result + 48 + 104) = v_xmm0;
        *(unsigned __int64 *)(result + 48 + 120) = v_xmm1;
        *(unsigned __int64 *)(result + 48 + 136) = v_xmm0;
        *(unsigned __int64 *)(result + 48 + 152) = v_xmm1;
        *(unsigned __int64 *)(result + 48 + 168) = v_xmm0;
    }
    if (0 != 0) {
        *(unsigned __int64 *)(result + 48 + 160) = 0;
    }
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m100)) & (0xC0000000ULL));
    if (((unsigned int)(v_rsi)) == 0x80000000ULL) goto loc_0088CAD1;
    a1 = (v_stack_mC0) + (40);
loc_0088C525:
    if (v_stack_m108 == 0) goto loc_0088C543;
    if ((a1 + v_stack_mF8 * 1) > a3) goto loc_0088CAFC;
loc_0088C543:
    *(unsigned __int64 *)(result + 48 + 176) = a1;
    if (*(unsigned __int64 *)(result + 48 + 96) != 0) goto loc_0088C8F9;
loc_0088C55E:
    if (v_stack_mF8 <= 512) goto loc_0088C588;
    if (*(unsigned __int64 *)(result + 48 + 96) != 0) goto loc_0088C906;
loc_0088C56F:
    if (v_stack_mF8 > 512) goto loc_0088C74E;
    if (*(unsigned __int64 *)(result + 48 + 224) != 0) goto loc_0088C8AE;
loc_0088C588:
    if (sign_flag) goto loc_0088CB02;
    *(unsigned __int64 *)(v_stack_mB8 + 8) = result + 48;
    *(unsigned __int16 *)(v_stack_mB8 + 52) = (unsigned __int16)(v_stack_mF6);
    *(unsigned __int16 *)(v_stack_mB8 + 54) = (unsigned __int16)(v_stack_mF4);
    *(unsigned __int16 *)(v_stack_mB8 + 56) = (unsigned __int16)(v_stack_mF2);
    if ((*(unsigned __int64 *)(result + 48 + 24)) == 0) goto loc_0088C6AC;
    if ((*(unsigned __int64 *)(result + 48 + 32)) == 0) goto loc_0088C91A;
    result = AlpcpDispatchReplyToWaitingThread(v_stack_mB8, v_stack_mF8, a3, a4);
loc_0088C5D3:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_mF8, a3, a4);
    v_rsp = (v_rsp) + (272);
    return result;
loc_0088C5F7:
    if (a3 == 0) goto loc_0088C812;
    result = ExpBlockOnLockedHandleEntry(v_stack_mD0, v_stack_mF8, a3, a4);
    goto loc_0088C0B0;
loc_0088C610:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + 48 + 40)))) & (640)) == 0) goto loc_0088C404;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(result + 48 + 40))) & (128));
    result = (unsigned __int8)(-(result));
    v_rbx = (unsigned int)((v_stack_mF8) & (0xC0000703ULL));
    if (v_stack_mD0 != 0) {
        a2 = 512;
        a1 = 0;
        result = AlpcpReleaseAttributes(a1, a2, a3, a4);
    }
    result = AlpcpCancelMessage(v_stack_mD0, result + 48, (unsigned int)(0x10000ULL), a4);
    goto loc_0088C5D3;
loc_0088C64F:
    if (v_stack_p58 != 0) goto loc_0088C6D0;
    if (v_stack_p60 == 0) goto loc_0088BFF4;
    goto loc_0088C6D0;
loc_0088C665:
    if (sign_flag) goto loc_0088C4BA;
    *(unsigned __int64 *)(result + 48 + 160) = 0;
    result = AlpcpReleaseAttributes(result + 48, result + 48 + 104, (unsigned int)(0x10000ULL), a4);
    goto loc_0088C4BA;
loc_0088C68A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444)))) & (32)) != 0) goto loc_0088CB83;
    goto loc_0088C02D;
loc_0088C6AC:
    result = AlpcpDispatchNewMessage((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444)), result + 48 + 104, (unsigned int)(0x10000ULL), a4);
    goto loc_0088C5D3;
loc_0088C6B6:
    if ((*(unsigned __int64 *)(v_stack_mD0 + 48)) != 0) {
        a2 = 0;
        result = ExfUnblockPushLock(v_stack_mD0 + 48, a2, (unsigned int)(0x10000ULL), a4);
    }
loc_0088C6D5:
    goto loc_0088C5D3;
loc_0088C6DC:
    goto loc_0088BFE3;
loc_0088C6E4:
    v_stack_p50 = v_xmm0;
    v_stack_p60 = v_xmm1;
    v_stack_p70 = v_xmm0;
    if (((*(unsigned int *)(v_rsi + 256)) & (0x1000ULL)) != 0) goto loc_0088C913;
    if ((((unsigned __int8)((unsigned int)(0xC0000702ULL))) & (2)) != 0) goto loc_0088C913;
    result = 0;
loc_0088C71B:
    if (((unsigned __int16)(v_stack_p50)) >= ((unsigned __int16)(v_stack_p50 + 40))) goto loc_0088C744;
    if (0 != 0) goto loc_0088C924;
    if ((v_stack_p50 + 40) == v_stack_p52) goto loc_0088BF71;
loc_0088C744:
    goto loc_0088C5D3;
loc_0088C74E:
    if (((unsigned int)(0xC0000702ULL)) > 0xFFD7ULL) goto loc_0088C972;
    if (((unsigned int)(0xC0000702ULL)) <= (512 + *(unsigned __int64 *)(result + 48 + 232) * 1)) goto loc_0088C588;
    if (*(unsigned __int64 *)(result + 48 + 224) != 0) goto loc_0088C95C;
loc_0088C77F:
    v_rbx = ((unsigned int)(0xC0000702ULL)) - (512);
    result = ExAllocatePool2(256, v_rbx, (unsigned int)(0x42456C41ULL), a4);
    *(unsigned __int64 *)(result + 48 + 224) = result;
    if (result == 0) goto loc_0088C948;
    *(unsigned __int64 *)(result + 48 + 232) = v_rbx;
    if (*(unsigned __int64 *)(result + 48 + 48) == 0) goto loc_0088C588;
    v_rbx = (v_rbx) - (*(unsigned __int64 *)(result + 48 + 232));
    result = AlpcpChargePagedPoolQuota(*(unsigned __int64 *)(result + 48 + 48), v_rbx, (unsigned int)(0x42456C41ULL), a4);
    if (!sign_flag) goto loc_0088C588;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 48 + 224), (unsigned int)(0x42456C41ULL), (unsigned int)(0x42456C41ULL), a4);
    *(unsigned __int64 *)(result + 48 + 224) = 0;
    *(unsigned __int64 *)(result + 48 + 232) = 0;
    result = AlpcpReleasePagedPoolQuota(*(unsigned __int64 *)(result + 48 + 48), *(unsigned __int64 *)(result + 48 + 232), (unsigned int)(0x42456C41ULL), a4);
    goto loc_0088C588;
loc_0088C801:
    goto loc_0088C5D3;
loc_0088C80B:
    goto loc_0088BF8C;
loc_0088C812:
    v_rbx = 0;
    result = ExHandleLogBadReference(v_stack_mD0, 512, (unsigned __int8)(*(unsigned __int64 *)(result + 48 + 232)), a4);
    goto loc_0088C0CE;
loc_0088C828:
    if ((*(unsigned __int64 *)(result + 48 + 16)) != (*(unsigned __int64 *)(result + 48 + 232))) goto loc_0088CA3B;
loc_0088C835:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mD0))) & (7));
    if (((unsigned __int8)(result)) != 3) goto loc_0088C848;
    if (((unsigned __int8)(result)) >= 3) goto loc_0088C20B;
loc_0088C848:
    result = AlpcpUnlockMessage(result + 48, *(unsigned __int64 *)(result + 48 + 16), (unsigned __int8)(*(unsigned __int64 *)(result + 48 + 232)), a4);
    goto loc_0088C5D3;
loc_0088C85A:
    if (((0) & (1)) != 0) goto loc_0088CA7C;
    if (condition_is_above_or_equal) goto loc_0088C97D;
    if ((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(result + 48 + 16))) != 0) goto loc_0088C993;
loc_0088C87E:
loc_0088C883:
    v_r15 = 0;
loc_0088C889:
    v_stack_p58 = v_xmm0;
loc_0088C896:
    v_stack_p68 = 0;
    if ((unsigned __int8)(v_stack_m108) != 0) goto loc_0088C001;
    v_stack_p70 = 0;
    goto loc_0088C001;
loc_0088C8AE:
    result = ExFreePoolWithTag(result + 48, (unsigned int)(0x42456C41ULL), (unsigned __int16)(*(unsigned __int64 *)(result + 48 + 16)), a4);
    *(unsigned __int64 *)(result + 48 + 224) = 0;
    if (*(unsigned __int64 *)(result + 48 + 48) == 0) goto loc_0088C8ED;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48 + 48) + 1432)) + (*(unsigned __int64 *)(result + 48 + 232));
    if (result >= 0x1000ULL) goto loc_0088CADA;
loc_0088C8ED:
    *(unsigned __int64 *)(result + 48 + 232) = 0;
    goto loc_0088C588;
loc_0088C8F9:
    a1 = (*(unsigned __int64 *)(result + 32)) - (40);
    goto loc_0088C55E;
loc_0088C906:
    v_rdi = (*(unsigned __int64 *)(result + 32)) - (40);
    goto loc_0088C56F;
loc_0088C913:
    goto loc_0088C71B;
loc_0088C91A:
    result = AlpcpDispatchReplyToPort(a1, *(unsigned __int64 *)(result + 48 + 232), (unsigned __int16)(*(unsigned __int64 *)(result + 48 + 16)), a4);
    goto loc_0088C5D3;
loc_0088C924:
    result = (v_stack_p50) >> (16);
    if ((*(unsigned __int64 *)(result + 48 + 232) + 40) > ((unsigned __int16)(result))) goto loc_0088C744;
    v_stack_p52 = (unsigned __int16)((unsigned __int16)(*(unsigned __int64 *)(result + 48 + 16)));
    goto loc_0088BF71;
loc_0088C948:
    if ((unsigned __int16)(result) != 0) goto loc_0088CAC4;
loc_0088C951:
    goto loc_0088C588;
loc_0088C95C:
    result = ExFreePoolWithTag((unsigned __int16)(result), (unsigned int)(0x42456C41ULL), (unsigned __int16)(*(unsigned __int64 *)(result + 48 + 16)), a4);
    *(unsigned __int64 *)(result + 48 + 232) = (unsigned int)(0xC000009AULL);
    goto loc_0088C77F;
loc_0088C972:
    goto loc_0088C588;
loc_0088C97D:
    if ((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(result + 48 + 16))) != 0) goto loc_0088CB44;
    goto loc_0088C883;
loc_0088C993:
    a3 = (unsigned int)(((unsigned __int16)(*(unsigned __int64 *)(result + 48 + 16))) - (3));
    if (condition_is_equal) goto loc_0088C9B1;
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_equal) goto loc_0088C9B1;
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_equal) goto loc_0088C9B1;
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_equal) goto loc_0088C9B1;
    if (((unsigned int)(a3)) != 7) goto loc_0088C9BA;
loc_0088C9B1:
    if (((0) & (2)) != 0) goto loc_0088C87E;
loc_0088C9BA:
    goto loc_0088C5D3;
loc_0088C9C6:
    v_r15 = 0;
    result = (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
    v_rbx = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48 + 232) + 16) != 0) {
        a2 = (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
        a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48 + 232) + 16)) + (40);
        a3 = v_rip - 8959247;
        result = AlpcReferenceBlobByHandle(a1, a2, a3, a4);
        v_rbx = result;
    }
    if (v_rbx == 0) goto loc_0088CB77;
    result = AlpcpLockForCachedReferenceBlob(*(unsigned __int64 *)(v_rbx + 24), a2, a3, a4);
    result = 0;
    if (condition_is_not_equal) goto loc_0088CBED;
loc_0088CA20:
    result = (unsigned int)((1) + (1));
    if (condition_is_equal) goto loc_0088CA20;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbx + 24) + 272) = (unsigned int)(result);
    goto loc_0088C1EB;
loc_0088CA3B:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx + 24))) & (7)) == 0) goto loc_0088CC0B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 48 + 232) + 416))) & (6));
    if (((unsigned __int8)(result)) != 6) goto loc_0088C848;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48 + 232) + 16) == 0) goto loc_0088C848;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48 + 232) + 16))) == a2) goto loc_0088C835;
    goto loc_0088C848;
loc_0088CA70:
    goto loc_0088C5D3;
loc_0088CA7C:
    if (0 == 0) goto loc_0088C9BA;
    v_r15 = 0;
    goto loc_0088C896;
loc_0088CA97:
    if ((unsigned __int8)(v_stack_m108) != 0) goto loc_0088BFC8;
    goto loc_0088BFE3;
loc_0088CAAA:
    if (((*(unsigned int *)(*(unsigned __int64 *)(result + 48 + 232) + 256)) & (0x1000ULL)) != 0) goto loc_0088BDF3;
    goto loc_0088C5D3;
loc_0088CAC4:
    result = AlpcpReleasePagedPoolQuota(0, *(unsigned __int64 *)(result + 48 + 232), a3, a4);
    goto loc_0088C951;
loc_0088CAD1:
    a1 = (0) + (24);
    goto loc_0088C525;
loc_0088CADA:
    result = PsReturnProcessPagedPoolQuota(a1, *(unsigned __int64 *)(result + 48 + 232), a3, a4);
    goto loc_0088C8ED;
loc_0088CAE4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 24) + 16)) != 0) goto loc_0088C1C9;
loc_0088CAEF:
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(v_rbx + 24), *(unsigned __int64 *)(result + 48 + 232), a3, a4);
    goto loc_0088C6D0;
loc_0088CAFC:
loc_0088CB02:
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(v_rbx + 24), *(unsigned __int64 *)(result + 48 + 232), a3, a4);
    goto loc_0088C5D3;
loc_0088CB12:
    v_stack_p20 = (unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL)));
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, *(unsigned __int64 *)(v_rbx + 24), 38);
loc_0088CB2B:
    v_stack_p20 = result;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, *(unsigned __int64 *)(v_rbx + 24), 38);
loc_0088CB44:
    a3 = (unsigned int)((*(unsigned __int64 *)(v_rbx + 24)) - (1));
    if (condition_is_equal) goto loc_0088CBD8;
    a3 = (unsigned int)((a3) - (6));
    if (condition_is_equal) goto loc_0088CB64;
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_equal) goto loc_0088CB64;
    if (((unsigned int)(a3)) != 1) goto loc_0088C9BA;
loc_0088CB64:
    if ((((unsigned __int8)((unsigned int)(0xC000009AULL))) & (2)) == 0) goto loc_0088C9BA;
    goto loc_0088C883;
loc_0088CB77:
    goto loc_0088C5D3;
loc_0088CB83:
    goto loc_0088C5D3;
loc_0088CB8D:
    goto loc_0088C5D3;
loc_0088CB97:
    goto loc_0088C5D3;
loc_0088CBA1:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 24) + 48) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)(0x63706C41ULL), a3, 38);
    goto loc_0088C3B0;
loc_0088CBD8:
    if (0 == 0) goto loc_0088C9BA;
    v_r15 = 0;
    goto loc_0088C889;
loc_0088CBED:
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(v_rbx + 24), (unsigned int)(0x63706C41ULL), a3, 38);
    result = AlpcpDereferenceBlobEx((unsigned int)(v_stack_p44), (unsigned int)((unsigned int)(v_r15 + 1)), a3, 38);
    goto loc_0088C5D3;
loc_0088CC0B:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_r15 + 1 + 16) - 16, a2, a3, 38);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(v_r15 + 1 + 16) - 16;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_r15 + 1 + 16) - 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a1 = 17;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 1 + 416))) >> (1));
    result = (unsigned int)((result) & (3));
    if (((unsigned int)(result)) != 2) goto loc_0088CC74;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 1 + 16))) == v_stack_p78) goto loc_0088CCB6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 1 + 16) + 8)) == v_stack_p78) goto loc_0088CCB6;
    v_rdi = 0;
    goto loc_0088CC7C;
loc_0088CC74:
    v_rdi = ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 1 + 16) + 16)) == v_stack_p78) ? 1 : 0;
loc_0088CC7C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 1 + 16) + 16)) != v_stack_p78) goto loc_0088CCE2;
loc_0088CC87:
    result = KeAbPostRelease(*(unsigned __int64 *)(v_r15 + 1 + 16) - 16, a2, a3, a4);
    if ((unsigned __int8)(v_rdi) == 0) goto loc_0088C848;
    goto loc_0088C210;
loc_0088CCA2:
    if (*(unsigned __int64 *)(v_rip + 7570567) != 0) goto loc_0088CCBB;
    v_r14 = 0;
    goto loc_0088C05F;
loc_0088CCB6:
    goto loc_0088CC7C;
loc_0088CCBB:
    result = (unsigned int)((result) >> (26));
    goto loc_0088C05F;
loc_0088CCC7:
    if (condition_is_equal) goto loc_0088CCFF;
    v_stack_p20 = result;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, *(unsigned __int64 *)(v_rbx + 24), 32);
loc_0088CCE2:
    result = ExfReleasePushLockShared((unsigned int)(v_stack_p44) - 16, a2, *(unsigned __int64 *)(v_rbx + 24), 32);
    goto loc_0088CC87;
loc_0088CCED:
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(v_rbx + 24), a2, *(unsigned __int64 *)(v_rbx + 24), 32);
    goto loc_0088C6D5;
loc_0088CCFF:
    result = ExUnlockHandleTableEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7570567) + result * 8), (unsigned int)(0xC0000022ULL), *(unsigned __int64 *)(v_rbx + 24), 32);
    goto loc_0088C6D0;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpSendMessage(void *Arg1, void *Arg2, int64_t Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint8_t v_stack_m107;
    uint8_t v_stack_m108;
    uint64_t v_stack_m118;
    uint8_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m148;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint64_t v_stack_m58;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint16_t v_stack_mF2;
    uint16_t v_stack_mF4;
    uint16_t v_stack_mF6;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p0;
    uint64_t v_stack_p20;
    uint32_t v_stack_p44;
    uint64_t v_stack_p50;
    uint16_t v_stack_p52;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x57E9E4)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m108 = Arg4;
    v_stack_mC8 = Arg3;
    v_stack_mC0 = Arg2;
    v_stack_mB8 = Arg1;
    Arg1 = 0;
    v_stack_mF8 = v_xmm0;
    v_stack_mE8 = v_xmm0;
    v_stack_mD8 = 0;
    v_stack_mA8 = v_xmm1;
    v_stack_m98 = v_xmm1;
    v_stack_m88 = v_xmm1;
    *(uint64_t *)(local_rsp - 0x78) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    v_stack_mD0 = *(uint64_t *)(arg1);
    v_stack_m100 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x1A0)))) & (16)) != 0) goto loc_0088C801;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x1A0)))) & (8)) != 0) goto loc_0088CB8D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x1A0)))) & (32)) != 0) goto loc_0088CAAA;
loc_0088BDF3:
    if (Arg4 == 0) goto loc_0088C6E4;
    result = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) & (0xC0000000ULL));
    if (((uint32_t)(result)) == 0x80000000ULL) goto loc_0088BEC3;
    Arg2 = local_r14;
    if (Arg2 < local_r14) { Arg2 = Arg2; }
    result = RtlCopyVolatileMemory(v_stack_mF8, Arg2, 40, Arg4);
loc_0088BE4F:
    if (((*(uint32_t *)(*(uint64_t *)(arg1) + 0x100)) & (0x1000ULL)) != 0) goto loc_0088BEAB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) & (2)) != 0) goto loc_0088BEAB;
    Arg1 = 0;
loc_0088BE62:
    v_stack_m107 = 0;
    if (((uint16_t)(v_stack_mF8)) >= ((uint16_t)(v_stack_mF8 + 40))) goto loc_0088BF62;
    if (0 != 0) goto loc_0088BEAF;
    Arg1 = ((uint16_t)(v_stack_mF8)) + (40);
    if (Arg1 != ((uint16_t)(v_stack_mF6))) goto loc_0088BF62;
loc_0088BE8A:
    if (v_stack_mF2 != 0) goto loc_0088BF44;
loc_0088BEA0:
    goto loc_0088BF71;
loc_0088BEAB:
    goto loc_0088BE62;
loc_0088BEAF:
    Arg1 = (1) + (40);
    if (Arg1 > ((uint32_t)(0x7FFFULL))) goto loc_0088BF62;
    v_stack_mF6 = (uint16_t)(Arg1);
    goto loc_0088BE8A;
loc_0088BEC3:
    Arg2 = (uint32_t)(0x7FFFULL);
    if (Arg2 < ((uint32_t)(0x7FFFULL))) { Arg2 = Arg2; }
    result = RtlCopyVolatileMemory(v_stack_m58, Arg2, 24, Arg4);
    v_stack_mF8 = (uint16_t)(v_stack_m58);
    v_stack_mF6 = (uint16_t)(v_stack_m58 + 40);
    v_stack_mF4 = (uint32_t)((uint32_t)(v_stack_m54));
    v_stack_mF0 = (uint32_t)(v_stack_m50);
    v_stack_mE8 = (uint32_t)(v_stack_m4C);
    v_stack_mE0 = (uint32_t)((uint32_t)(v_stack_m48));
    v_stack_mD8 = (uint32_t)(v_stack_m44);
    v_stack_mD8 = (uint32_t)((uint32_t)(v_stack_m44));
    goto loc_0088BE4F;
loc_0088BF44:
    result = AlpcpValidateDataInformation(Arg2, v_stack_mF8, v_stack_m58 + 40, Arg4);
    v_stack_m104 = (uint32_t)(result);
    if (!sign_flag) goto loc_0088BEA0;
    goto loc_0088C5D3;
loc_0088BF62:
    goto loc_0088C5D3;
loc_0088BF71:
    if (((*(uint32_t *)(*(uint64_t *)(arg1) + 0x100)) & (0x1000ULL)) != 0) goto loc_0088C80B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30)))) & (2)) != 0) goto loc_0088C80B;
    result = 0;
loc_0088BF8C:
    Arg2 = (uint16_t)(((uint16_t)(v_stack_mF4)) & (255));
    Arg1 = (uint16_t)((v_stack_mF4) & ((uint16_t)((uint32_t)(0xFF00ULL))));
    if (0 != 0) goto loc_0088C85A;
    if (((uint16_t)(Arg2)) == 7) goto loc_0088CA97;
loc_0088BFC8:
    if ((uint32_t)((uint32_t)(v_stack_mE0)) != 0) goto loc_0088C27E;
loc_0088BFD1:
    if (condition_is_above_or_equal) goto loc_0088C6DC;
loc_0088BFE3:
    local_r15 = 0;
loc_0088BFE6:
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_0088C64F;
loc_0088BFF4:
    v_stack_mF0 = v_xmm0;
loc_0088C001:
    Arg1 = (uint16_t)((Arg1) & ((uint16_t)((uint32_t)(0xEFFFULL))));
    Arg1 = (uint16_t)((Arg1) | ((uint16_t)(1 + 2)));
    v_stack_mF4 = (uint16_t)(Arg1);
    if (v_stack_mF6 > (*(uint64_t *)(*(uint64_t *)(arg1) + 0x110))) goto loc_0088CB97;
    if (v_stack_mF6 < (*(uint64_t *)(*(uint64_t *)(arg1) + 0x110))) goto loc_0088C68A;
loc_0088C02D:
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_0088C2A0;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) | (16));
    v_stack_m100 = (uint32_t)(local_rbx);
    if (sign_flag) goto loc_0088C9C6;
    if ((((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mE0))))) & (0xFC000000ULL)) != 0) goto loc_0088CCA2;
loc_0088C05F:
    if (*(uint64_t *)(v_rip + 0x73AF09) == 0) goto loc_0088C6D0;
    local_rdi = (uint32_t)((v_stack_mE0) & (0x3FFFFFFULL));
    if ((((uint32_t)(local_rdi)) & (0x3FCULL)) == 0) goto loc_0088C812;
    result = ExpLookupHandleTableEntry(*(uint64_t *)(v_rip + 0x73AF09), (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0xFF00ULL), *(uint64_t *)(gs_base + (0 + 0x188)));
    if (result == 0) goto loc_0088C812;
loc_0088C0B0:
    if ((((uint8_t)(*(uint64_t *)(result))) & (1)) == 0) goto loc_0088C5F7;
    if ((((uint8_t)(*(uint64_t *)(result))) & (1)) != 0) goto loc_0088C0B0;
loc_0088C0CE:
    if (result == 0) goto loc_0088C6D0;
    result = ExGetHandlePointer(result, (uint32_t)((uint32_t)(local_rdi)), *(uint64_t *)(result), *(uint64_t *)(gs_base + (0 + 0x188)));
    if ((*(uint32_t *)(result + 0x108)) != ((uint32_t)((uint32_t)(v_stack_mE0)))) goto loc_0088C6B6;
    if ((uint32_t)((uint32_t)(v_stack_mD8)) == 0) goto loc_0088C101;
    if ((*(uint32_t *)(result + 0x110)) != ((uint32_t)((uint32_t)(v_stack_mD8)))) goto loc_0088C6B6;
loc_0088C101:
loc_0088C109:
    if (condition_is_less_or_equal) goto loc_0088CCC7;
    if ((*(uint64_t *)(result - 0x18)) != (*(uint64_t *)(result - 0x18))) goto loc_0088C109;
    result = (*(uint64_t *)(result - 0x18)) + (1);
    if (condition_is_equal) goto loc_0088CCFF;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result - 16, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x188)));
    if (!(condition_is_above_or_equal)) {
        Arg3 = result - 16;
        Arg2 = result;
        Arg1 = result - 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x188)));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ((uint32_t)(0x10000ULL)) + (0x10000ULL);
    if (condition_is_less_or_equal) goto loc_0088CB12;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x73AF09) + 0x30)) != 0) {
        Arg2 = 0;
        result = ExfUnblockPushLock(*(uint64_t *)(v_rip + 0x73AF09) + 48, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x188)));
    }
    if ((*(uint32_t *)(result + 0x108)) != ((uint32_t)((uint32_t)(v_stack_mE0)))) goto loc_0088CAEF;
    if ((uint32_t)((uint32_t)(v_stack_mD8)) == 0) goto loc_0088C1BE;
    if ((*(uint32_t *)(result + 0x110)) != ((uint32_t)((uint32_t)(v_stack_mD8)))) goto loc_0088CAEF;
loc_0088C1BE:
    if ((*(uint64_t *)(result + 0x18)) == 0) goto loc_0088CAE4;
loc_0088C1C9:
    if ((*(uint64_t *)(result + 0xB8)) == (*(uint64_t *)(v_stack_mD0 + 0x10))) goto loc_0088C1E8;
    if ((*(uint64_t *)(result + 0xC0)) != v_stack_mD0) goto loc_0088CCED;
loc_0088C1E8:
    local_r15 = 0;
loc_0088C1EB:
    v_stack_m104 = 0;
    if (sign_flag) goto loc_0088C3A7;
    if (*(uint64_t *)(result + 0x18) != 0) goto loc_0088C828;
loc_0088C20B:
loc_0088C210:
    if ((*(uint64_t *)(result + 0x20)) == 0) goto loc_0088C3AC;
    if ((*(uint64_t *)(result + 0x30)) != 0) goto loc_0088C3B0;
    if ((((uint32_t)((uint32_t)(v_stack_m100))) & (0x30000ULL)) != 0) goto loc_0088C3B0;
    if ((*(uint64_t *)(result + 0xE0)) != 0) {
        Arg2 = (792) + (*(uint64_t *)(result + 0xE8));
    }
    result = AlpcpChargePagedPoolQuota(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x188)));
    v_stack_m104 = (uint32_t)(result);
    if (!sign_flag) goto loc_0088CBA1;
loc_0088C26F:
    result = AlpcpUnlockMessage(result, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x188)));
    goto loc_0088C5D3;
loc_0088C27E:
    if (sign_flag) goto loc_0088BFD1;
    result = (condition_is_below) ? 1 : 0;
    goto loc_0088BFE6;
loc_0088C2A0:
    result = ExAllocateFromPagedLookasideList(v_rip + 5877465, result + 1, Arg3, *(uint64_t *)(gs_base + (0 + 0x188)));
    if (result == 0) goto loc_0088CA70;
    *(uint16_t *)(result + 0x10) = 512;
    *(uint32_t *)(result + 0x12) = 0;
    *(uint16_t *)(result + 0x16) = 0;
    *(uint64_t *)(result + 0x28) = 0;
    *(uint64_t *)(result + 0x20) = 0;
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    *(uint64_t *)(result + 0x18) = 0 + 1;
    if (result + 48 == 0) goto loc_0088CA70;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 32, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x188)));
    if (!(condition_is_above_or_equal)) {
        Arg3 = result + 32;
        Arg2 = result;
        Arg1 = result + 32;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, *(uint64_t *)(gs_base + (0 + 0x188)));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ((uint32_t)(0x10000ULL)) + (0x10000ULL);
    if (condition_is_less_or_equal) goto loc_0088CB2B;
    Arg2 = 0;
    result = memset(result + 48, Arg2, 280, *(uint64_t *)(gs_base + (0 + 0x188)));
    *(uint16_t *)(result + 0x30 + 0xF2) = 40;
    *(uint32_t *)(result + 0x30 + 0x108) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30 + 0x108)));
loc_0088C371:
    result = (uint32_t)(((uint32_t)((uint32_t)(0 + 1))) + (1));
    if (condition_is_equal) goto loc_0088C371;
    *(uint32_t *)(result + 0x30 + 0x110) = (uint32_t)(result);
    if ((*(uint32_t *)(v_rip + 0x683D42)) != 0) {
        Arg1 = result + 48;
        result = AlpcpEnterAllocationEventMessageLog(Arg1, Arg2, 280, *(uint64_t *)(gs_base + (0 + 0x188)));
    }
    *(uint16_t *)(result + 0x30 + 0xF2) = 40;
    v_stack_m104 = 0;
loc_0088C3A7:
loc_0088C3AC:
loc_0088C3B0:
    if (sign_flag) goto loc_0088C6D5;
    local_rbx = 0;
    local_rdi = 0;
    if (v_stack_mC8 != 0) {
        local_rdi = v_stack_mA8;
        result = v_stack_mA8;
        v_stack_m128 = result;
        Arg4 = result + 48;
        Arg3 = v_stack_mC8;
        Arg2 = (uint32_t)((uint32_t)(v_stack_m100));
        Arg1 = v_stack_mD0;
        result = AlpcpCaptureAttributes(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
        v_stack_m104 = (uint32_t)(result);
        Arg1 = v_stack_mC8;
    }
    if ((uint32_t)((uint32_t)(v_stack_mE0)) != 0) goto loc_0088C610;
loc_0088C404:
    if (sign_flag) goto loc_0088C26F;
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_0088C4AE;
    if (*(uint64_t *)(result + 0x30 + 0xD0) != 0) {
        Arg4 = *(uint32_t *)(result + 0x30 + 0x108);
        result = (uint32_t)(*(uint64_t *)(result + 0x30 + 0xD0));
        result = (uint32_t)((result) & (7));
        Arg1 = (*(uint64_t *)(result + 0x30 + 0xD0)) & (-8);
        Arg3 = 0;
        if (((uint32_t)(result)) != 7) { Arg3 = (uint32_t)(result); }
        Arg2 = 2;
        if (((uint32_t)(result)) != 7) { Arg2 = 0; }
        v_stack_m118 = 0;
        v_stack_m120 = 1;
        v_stack_m128 = 0xFFFFFFFFULL;
        result = PspChargeProcessWakeCounter(Arg1, Arg2, Arg3, Arg4);
        *(uint64_t *)(result + 0x30 + 0xD0) = 0;
    }
    local_rbx = 2;
    if (*(uint64_t *)(result + 0x30 + 0xD8) != 0) {
        Arg4 = *(uint32_t *)(result + 0x30 + 0x108);
        result = (uint32_t)(*(uint64_t *)(result + 0x30 + 0xD8));
        result = (uint32_t)((result) & (7));
        Arg1 = (*(uint64_t *)(result + 0x30 + 0xD8)) & (-8);
        Arg3 = 0;
        if (((uint32_t)(result)) != 7) { Arg3 = (uint32_t)(result); }
        local_rbx = 2;
        if (((uint32_t)(result)) != 7) { local_rbx = 0; }
        v_stack_m118 = 0;
        v_stack_m120 = 1;
        v_stack_m128 = 0xFFFFFFFFULL;
        Arg2 = (uint32_t)(local_rbx);
        result = PspChargeProcessWakeCounter(Arg1, Arg2, Arg3, Arg4);
        *(uint64_t *)(result + 0x30 + 0xD8) = 0;
    }
    if ((uint32_t)((uint32_t)(v_stack_mE0)) != 0) goto loc_0088C665;
loc_0088C4BA:
    if (local_rdi != 0) {
        *(uint64_t *)(result + 0x30 + 0x68) = v_xmm0;
        *(uint64_t *)(result + 0x30 + 0x78) = v_xmm1;
        *(uint64_t *)(result + 0x30 + 0x88) = v_xmm0;
        *(uint64_t *)(result + 0x30 + 0x98) = v_xmm1;
        *(uint64_t *)(result + 0x30 + 0xA8) = v_xmm0;
    }
    if (0 != 0) {
        *(uint64_t *)(result + 0x30 + 0xA0) = 0;
    }
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m100)) & (0xC0000000ULL));
    if (((uint32_t)(local_rsi)) == 0x80000000ULL) goto loc_0088CAD1;
    Arg1 = (v_stack_mC0) + (40);
loc_0088C525:
    if (v_stack_m108 == 0) goto loc_0088C543;
    if ((Arg1 + v_stack_mF8 * 1) > Arg3) goto loc_0088CAFC;
loc_0088C543:
    *(void **)(result + 0x30 + 0xB0) = Arg1;
    if (*(uint64_t *)(result + 0x30 + 0x60) != 0) goto loc_0088C8F9;
loc_0088C55E:
    if (v_stack_mF8 <= 512) goto loc_0088C588;
    if (*(uint64_t *)(result + 0x30 + 0x60) != 0) goto loc_0088C906;
loc_0088C56F:
    if (v_stack_mF8 > 512) goto loc_0088C74E;
    if (*(uint64_t *)(result + 0x30 + 0xE0) != 0) goto loc_0088C8AE;
loc_0088C588:
    if (sign_flag) goto loc_0088CB02;
    *(uint64_t *)(v_stack_mB8 + 0x8) = result + 48;
    *(uint16_t *)(v_stack_mB8 + 0x34) = (uint16_t)(v_stack_mF6);
    *(uint16_t *)(v_stack_mB8 + 0x36) = (uint16_t)(v_stack_mF4);
    *(uint16_t *)(v_stack_mB8 + 0x38) = (uint16_t)(v_stack_mF2);
    if ((*(uint64_t *)(result + 0x30 + 0x18)) == 0) goto loc_0088C6AC;
    if ((*(uint64_t *)(result + 0x30 + 0x20)) == 0) goto loc_0088C91A;
    result = AlpcpDispatchReplyToWaitingThread(v_stack_mB8, v_stack_mF8, Arg3, Arg4);
loc_0088C5D3:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_mF8, Arg3, Arg4);
    local_rsp = (local_rsp) + (272);
    return result;
loc_0088C5F7:
    if (Arg3 == 0) goto loc_0088C812;
    result = ExpBlockOnLockedHandleEntry(v_stack_mD0, v_stack_mF8, Arg3, Arg4);
    goto loc_0088C0B0;
loc_0088C610:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30 + 0x28)))) & (640)) == 0) goto loc_0088C404;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(result + 0x30 + 0x28))) & (128));
    result = (uint8_t)(-(result));
    local_rbx = (uint32_t)((v_stack_mF8) & (0xC0000703ULL));
    if (v_stack_mD0 != 0) {
        Arg2 = 512;
        Arg1 = 0;
        result = AlpcpReleaseAttributes(Arg1, Arg2, Arg3, Arg4);
    }
    result = AlpcpCancelMessage(v_stack_mD0, result + 48, (uint32_t)(0x10000ULL), Arg4);
    goto loc_0088C5D3;
loc_0088C64F:
    if (v_stack_p58 != 0) goto loc_0088C6D0;
    if (v_stack_p60 == 0) goto loc_0088BFF4;
    goto loc_0088C6D0;
loc_0088C665:
    if (sign_flag) goto loc_0088C4BA;
    *(uint64_t *)(result + 0x30 + 0xA0) = 0;
    result = AlpcpReleaseAttributes(result + 48, result + 48 + 104, (uint32_t)(0x10000ULL), Arg4);
    goto loc_0088C4BA;
loc_0088C68A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4)))) & (32)) != 0) goto loc_0088CB83;
    goto loc_0088C02D;
loc_0088C6AC:
    result = AlpcpDispatchNewMessage((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4)), result + 48 + 104, (uint32_t)(0x10000ULL), Arg4);
    goto loc_0088C5D3;
loc_0088C6B6:
    if ((*(uint64_t *)(v_stack_mD0 + 0x30)) != 0) {
        Arg2 = 0;
        result = ExfUnblockPushLock(v_stack_mD0 + 48, Arg2, (uint32_t)(0x10000ULL), Arg4);
    }
loc_0088C6D5:
    goto loc_0088C5D3;
loc_0088C6DC:
    goto loc_0088BFE3;
loc_0088C6E4:
    v_stack_p50 = v_xmm0;
    v_stack_p60 = v_xmm1;
    v_stack_p70 = v_xmm0;
    if (((*(uint32_t *)(local_rsi + 0x100)) & (0x1000ULL)) != 0) goto loc_0088C913;
    if ((((uint8_t)((uint32_t)(0xC0000702ULL))) & (2)) != 0) goto loc_0088C913;
    result = 0;
loc_0088C71B:
    if (((uint16_t)(v_stack_p50)) >= ((uint16_t)(v_stack_p50 + 40))) goto loc_0088C744;
    if (0 != 0) goto loc_0088C924;
    if ((v_stack_p50 + 40) == v_stack_p52) goto loc_0088BF71;
loc_0088C744:
    goto loc_0088C5D3;
loc_0088C74E:
    if (((uint32_t)(0xC0000702ULL)) > 0xFFD7ULL) goto loc_0088C972;
    if (((uint32_t)(0xC0000702ULL)) <= (512 + *(uint64_t *)(result + 0x30 + 0xE8) * 1)) goto loc_0088C588;
    if (*(uint64_t *)(result + 0x30 + 0xE0) != 0) goto loc_0088C95C;
loc_0088C77F:
    local_rbx = ((uint32_t)(0xC0000702ULL)) - (512);
    result = ExAllocatePool2(256, local_rbx, (uint32_t)(0x42456C41ULL), Arg4);
    *(uint64_t *)(result + 0x30 + 0xE0) = result;
    if (result == 0) goto loc_0088C948;
    *(uint64_t *)(result + 0x30 + 0xE8) = local_rbx;
    if (*(uint64_t *)(result + 0x30 + 0x30) == 0) goto loc_0088C588;
    local_rbx = (local_rbx) - (*(uint64_t *)(result + 0x30 + 0xE8));
    result = AlpcpChargePagedPoolQuota(*(uint64_t *)(result + 0x30 + 0x30), local_rbx, (uint32_t)(0x42456C41ULL), Arg4);
    if (!sign_flag) goto loc_0088C588;
    result = ExFreePoolWithTag(*(uint64_t *)(result + 0x30 + 0xE0), (uint32_t)(0x42456C41ULL), (uint32_t)(0x42456C41ULL), Arg4);
    *(uint64_t *)(result + 0x30 + 0xE0) = 0;
    *(uint64_t *)(result + 0x30 + 0xE8) = 0;
    result = AlpcpReleasePagedPoolQuota(*(uint64_t *)(result + 0x30 + 0x30), *(uint64_t *)(result + 0x30 + 0xE8), (uint32_t)(0x42456C41ULL), Arg4);
    goto loc_0088C588;
loc_0088C801:
    goto loc_0088C5D3;
loc_0088C80B:
    goto loc_0088BF8C;
loc_0088C812:
    local_rbx = 0;
    result = ExHandleLogBadReference(v_stack_mD0, 512, (uint8_t)(*(uint64_t *)(result + 0x30 + 0xE8)), Arg4);
    goto loc_0088C0CE;
loc_0088C828:
    if ((*(uint64_t *)(result + 0x30 + 0x10)) != (*(uint64_t *)(result + 0x30 + 0xE8))) goto loc_0088CA3B;
loc_0088C835:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mD0))) & (7));
    if (((uint8_t)(result)) != 3) goto loc_0088C848;
    if (((uint8_t)(result)) >= 3) goto loc_0088C20B;
loc_0088C848:
    result = AlpcpUnlockMessage(result + 48, *(uint64_t *)(result + 0x30 + 0x10), (uint8_t)(*(uint64_t *)(result + 0x30 + 0xE8)), Arg4);
    goto loc_0088C5D3;
loc_0088C85A:
    if (((0) & (1)) != 0) goto loc_0088CA7C;
    if (condition_is_above_or_equal) goto loc_0088C97D;
    if ((uint32_t)((uint16_t)(*(uint64_t *)(result + 0x30 + 0x10))) != 0) goto loc_0088C993;
loc_0088C87E:
loc_0088C883:
    local_r15 = 0;
loc_0088C889:
    v_stack_p58 = v_xmm0;
loc_0088C896:
    v_stack_p68 = 0;
    if ((uint8_t)(v_stack_m108) != 0) goto loc_0088C001;
    v_stack_p70 = 0;
    goto loc_0088C001;
loc_0088C8AE:
    result = ExFreePoolWithTag(result + 48, (uint32_t)(0x42456C41ULL), (uint16_t)(*(uint64_t *)(result + 0x30 + 0x10)), Arg4);
    *(uint64_t *)(result + 0x30 + 0xE0) = 0;
    if (*(uint64_t *)(result + 0x30 + 0x30) == 0) goto loc_0088C8ED;
    result = (*(uint64_t *)(*(uint64_t *)(result + 0x30 + 0x30) + 0x598)) + (*(uint64_t *)(result + 0x30 + 0xE8));
    if (result >= 0x1000ULL) goto loc_0088CADA;
loc_0088C8ED:
    *(uint64_t *)(result + 0x30 + 0xE8) = 0;
    goto loc_0088C588;
loc_0088C8F9:
    Arg1 = (*(uint64_t *)(result + 0x20)) - (40);
    goto loc_0088C55E;
loc_0088C906:
    local_rdi = (*(uint64_t *)(result + 0x20)) - (40);
    goto loc_0088C56F;
loc_0088C913:
    goto loc_0088C71B;
loc_0088C91A:
    result = AlpcpDispatchReplyToPort(Arg1, *(uint64_t *)(result + 0x30 + 0xE8), (uint16_t)(*(uint64_t *)(result + 0x30 + 0x10)), Arg4);
    goto loc_0088C5D3;
loc_0088C924:
    result = (v_stack_p50) >> (16);
    if ((*(uint64_t *)(result + 0x30 + 0xE8) + 40) > ((uint16_t)(result))) goto loc_0088C744;
    v_stack_p52 = (uint16_t)((uint16_t)(*(uint64_t *)(result + 0x30 + 0x10)));
    goto loc_0088BF71;
loc_0088C948:
    if ((uint16_t)(result) != 0) goto loc_0088CAC4;
loc_0088C951:
    goto loc_0088C588;
loc_0088C95C:
    result = ExFreePoolWithTag((uint16_t)(result), (uint32_t)(0x42456C41ULL), (uint16_t)(*(uint64_t *)(result + 0x30 + 0x10)), Arg4);
    *(uint64_t *)(result + 0x30 + 0xE8) = (uint32_t)(0xC000009AULL);
    goto loc_0088C77F;
loc_0088C972:
    goto loc_0088C588;
loc_0088C97D:
    if ((uint32_t)((uint16_t)(*(uint64_t *)(result + 0x30 + 0x10))) != 0) goto loc_0088CB44;
    goto loc_0088C883;
loc_0088C993:
    Arg3 = (uint32_t)(((uint16_t)(*(uint64_t *)(result + 0x30 + 0x10))) - (3));
    if (condition_is_equal) goto loc_0088C9B1;
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_equal) goto loc_0088C9B1;
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_equal) goto loc_0088C9B1;
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_equal) goto loc_0088C9B1;
    if (((uint32_t)(Arg3)) != 7) goto loc_0088C9BA;
loc_0088C9B1:
    if (((0) & (2)) != 0) goto loc_0088C87E;
loc_0088C9BA:
    goto loc_0088C5D3;
loc_0088C9C6:
    local_r15 = 0;
    result = (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
    local_rbx = 0;
    if (*(uint64_t *)(*(uint64_t *)(result + 0x30 + 0xE8) + 0x10) != 0) {
        Arg2 = (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
        Arg1 = (*(uint64_t *)(*(uint64_t *)(result + 0x30 + 0xE8) + 0x10)) + (40);
        Arg3 = v_rip - 8959247;
        result = AlpcReferenceBlobByHandle(Arg1, Arg2, Arg3, Arg4);
        local_rbx = result;
    }
    if (local_rbx == 0) goto loc_0088CB77;
    result = AlpcpLockForCachedReferenceBlob(*(uint64_t *)(local_rbx + 0x18), Arg2, Arg3, Arg4);
    result = 0;
    if (condition_is_not_equal) goto loc_0088CBED;
loc_0088CA20:
    result = (uint32_t)((1) + (1));
    if (condition_is_equal) goto loc_0088CA20;
    *(uint32_t *)(*(uint64_t *)(local_rbx + 0x18) + 0x110) = (uint32_t)(result);
    goto loc_0088C1EB;
loc_0088CA3B:
    if ((((uint8_t)(*(uint64_t *)(local_rbx + 0x18))) & (7)) == 0) goto loc_0088CC0B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x30 + 0xE8) + 0x1A0))) & (6));
    if (((uint8_t)(result)) != 6) goto loc_0088C848;
    if (*(uint64_t *)(*(uint64_t *)(result + 0x30 + 0xE8) + 0x10) == 0) goto loc_0088C848;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x30 + 0xE8) + 0x10))) == Arg2) goto loc_0088C835;
    goto loc_0088C848;
loc_0088CA70:
    goto loc_0088C5D3;
loc_0088CA7C:
    if (0 == 0) goto loc_0088C9BA;
    local_r15 = 0;
    goto loc_0088C896;
loc_0088CA97:
    if ((uint8_t)(v_stack_m108) != 0) goto loc_0088BFC8;
    goto loc_0088BFE3;
loc_0088CAAA:
    if (((*(uint32_t *)(*(uint64_t *)(result + 0x30 + 0xE8) + 0x100)) & (0x1000ULL)) != 0) goto loc_0088BDF3;
    goto loc_0088C5D3;
loc_0088CAC4:
    result = AlpcpReleasePagedPoolQuota(0, *(uint64_t *)(result + 0x30 + 0xE8), Arg3, Arg4);
    goto loc_0088C951;
loc_0088CAD1:
    Arg1 = (0) + (24);
    goto loc_0088C525;
loc_0088CADA:
    result = PsReturnProcessPagedPoolQuota(Arg1, *(uint64_t *)(result + 0x30 + 0xE8), Arg3, Arg4);
    goto loc_0088C8ED;
loc_0088CAE4:
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x18) + 0x10)) != 0) goto loc_0088C1C9;
loc_0088CAEF:
    result = AlpcpUnlockMessage(*(uint64_t *)(local_rbx + 0x18), *(uint64_t *)(result + 0x30 + 0xE8), Arg3, Arg4);
    goto loc_0088C6D0;
loc_0088CAFC:
loc_0088CB02:
    result = AlpcpUnlockMessage(*(uint64_t *)(local_rbx + 0x18), *(uint64_t *)(result + 0x30 + 0xE8), Arg3, Arg4);
    goto loc_0088C5D3;
loc_0088CB12:
    v_stack_p20 = (uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL)));
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, *(uint64_t *)(local_rbx + 0x18), 38);
loc_0088CB2B:
    v_stack_p20 = result;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, *(uint64_t *)(local_rbx + 0x18), 38);
loc_0088CB44:
    Arg3 = (uint32_t)((*(uint64_t *)(local_rbx + 0x18)) - (1));
    if (condition_is_equal) goto loc_0088CBD8;
    Arg3 = (uint32_t)((Arg3) - (6));
    if (condition_is_equal) goto loc_0088CB64;
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_equal) goto loc_0088CB64;
    if (((uint32_t)(Arg3)) != 1) goto loc_0088C9BA;
loc_0088CB64:
    if ((((uint8_t)((uint32_t)(0xC000009AULL))) & (2)) == 0) goto loc_0088C9BA;
    goto loc_0088C883;
loc_0088CB77:
    goto loc_0088C5D3;
loc_0088CB83:
    goto loc_0088C5D3;
loc_0088CB8D:
    goto loc_0088C5D3;
loc_0088CB97:
    goto loc_0088C5D3;
loc_0088CBA1:
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x18) + 0x30) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    result = ObfReferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)(0x63706C41ULL), Arg3, 38);
    goto loc_0088C3B0;
loc_0088CBD8:
    if (0 == 0) goto loc_0088C9BA;
    local_r15 = 0;
    goto loc_0088C889;
loc_0088CBED:
    result = AlpcpUnlockMessage(*(uint64_t *)(local_rbx + 0x18), (uint32_t)(0x63706C41ULL), Arg3, 38);
    result = AlpcpDereferenceBlobEx((uint32_t)(v_stack_p44), (uint32_t)((uint32_t)(local_r15 + 1)), Arg3, 38);
    goto loc_0088C5D3;
loc_0088CC0B:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(local_r15 + 0x1 + 0x10) - 16, Arg2, Arg3, 38);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = *(uint64_t *)(local_r15 + 0x1 + 0x10) - 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(local_r15 + 0x1 + 0x10) - 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        Arg1 = 17;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x1 + 0x1A0))) >> (1));
    result = (uint32_t)((result) & (3));
    if (((uint32_t)(result)) != 2) goto loc_0088CC74;
    if ((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x1 + 0x10))) == v_stack_p78) goto loc_0088CCB6;
    if ((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x1 + 0x10) + 0x8)) == v_stack_p78) goto loc_0088CCB6;
    local_rdi = 0;
    goto loc_0088CC7C;
loc_0088CC74:
    local_rdi = ((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x1 + 0x10) + 0x10)) == v_stack_p78) ? 1 : 0;
loc_0088CC7C:
    if ((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x1 + 0x10) + 0x10)) != v_stack_p78) goto loc_0088CCE2;
loc_0088CC87:
    result = KeAbPostRelease(*(uint64_t *)(local_r15 + 0x1 + 0x10) - 16, Arg2, Arg3, Arg4);
    if ((uint8_t)(local_rdi) == 0) goto loc_0088C848;
    goto loc_0088C210;
loc_0088CCA2:
    if (*(uint64_t *)(v_rip + 0x738487) != 0) goto loc_0088CCBB;
    local_r14 = 0;
    goto loc_0088C05F;
loc_0088CCB6:
    goto loc_0088CC7C;
loc_0088CCBB:
    result = (uint32_t)((result) >> (26));
    goto loc_0088C05F;
loc_0088CCC7:
    if (condition_is_equal) goto loc_0088CCFF;
    v_stack_p20 = result;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, *(uint64_t *)(local_rbx + 0x18), 32);
loc_0088CCE2:
    result = ExfReleasePushLockShared((uint32_t)(v_stack_p44) - 16, Arg2, *(uint64_t *)(local_rbx + 0x18), 32);
    goto loc_0088CC87;
loc_0088CCED:
    result = AlpcpUnlockMessage(*(uint64_t *)(local_rbx + 0x18), Arg2, *(uint64_t *)(local_rbx + 0x18), 32);
    goto loc_0088C6D5;
loc_0088CCFF:
    result = ExUnlockHandleTableEntry(*(uint64_t *)(*(uint64_t *)(v_rip + 0x738487) + result * 8), (uint32_t)(0xC0000022ULL), *(uint64_t *)(local_rbx + 0x18), 32);
    goto loc_0088C6D0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x10` | `128` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0088BD40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
