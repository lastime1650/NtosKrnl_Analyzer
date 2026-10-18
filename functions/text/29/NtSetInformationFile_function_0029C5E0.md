# NtSetInformationFile

- RVA: `0x0029C5E0`–`0x0029D51B` (길이 `3,899` bytes)
- VA: `0x000000014029C5E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00067F48`
- 디코드: `879`개 명령, `3,899/3,899` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **57**; 고유 호출 대상: **43**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0029C730` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0029C735` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0029C76D` → [IopReferenceFileObject](IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x0029C831` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0029C85C` → [ObfReferenceObject](../20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0029C8A3` → [IopReleaseFileObjectLock](../25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x0029C8B2` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0029C93A` → [IopReleaseFileObjectLock](../25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x0029C962` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0029C9CB` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0029CA8F` → [SeCaptureSubjectContextEx](../../page/8C/SeCaptureSubjectContextEx_function_008C4C90.md) (function, `0x008C4C90`)
- `0x0029CAA0` → [RtlIsSandboxedToken](../../page/8B/RtlIsSandboxedToken_function_008B3AB0.md) (function, `0x008B3AB0`)
- `0x0029CAB0` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x0029CAFB` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0029CB31` → [IopResetEvent](IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x0029CB53` → [IopAllocateIrpExReturn](../20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x0029CC0A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0029CC26` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0029CC48` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x0029CC71` → [IopExceptionCleanupEx](../../page/8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x0029CC7F` → [KeSetKernelStackSwapEnable](../45/KeSetKernelStackSwapEnable_function_00450760.md) (function, `0x00450760`)
- `0x0029CCB0` → [IopQueueThreadIrp](../20/IopQueueThreadIrp_function_002075C0.md) (function, `0x002075C0`)
- `0x0029CD61` → [IopCallDriverReference](IopCallDriverReference_function_0029B1C0.md) (function, `0x0029B1C0`)
- `0x0029CDD8` → [IopCompleteRequest](../20/IopCompleteRequest_function_0020AF50.md) (function, `0x0020AF50`)
- `0x0029CDED` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0029CE03` → [IopReleaseFileObjectLock](../25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x0029CE3C` → [ObCloseHandle](../../page/8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x0029CE53` → [IopReleaseFileObjectLock](../25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x0029CE60` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0029CEA7` → [IopWaitForSynchronousIo](IopWaitForSynchronousIo_function_0029D6D0.md) (function, `0x0029D6D0`)
- `0x0029CEF8` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0029CF3B` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0029CF91` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x0029CFAB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0029CFC9` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0029D004` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x0029D04B` → [IopWaitAndAcquireFileObjectLock](../../page/8A/IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x0029D06E` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0029D0BF` → [IopAllocateIrpCleanup](../../page/A1/IopAllocateIrpCleanup_function_00A1E2D4.md) (function, `0x00A1E2D4`)
- `0x0029D140` → [IopOpenLinkOrRenameTarget](../../page/8A/IopOpenLinkOrRenameTarget_function_008AAC04.md) (function, `0x008AAC04`)
- `0x0029D174` → [KeAreInterruptsEnabled](../2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x0029D1A8` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x0029D1B2` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x0029D1D6` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x0029D261` → [IopReleaseFileObjectLock](../25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x0029D26E` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0029D284` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0029D2A5` → [IoGetAttachedDevice](../41/IoGetAttachedDevice_function_00410810.md) (function, `0x00410810`)
- `0x0029D302` → [IopTrackLink](../../page/A3/IopTrackLink_function_00A36764.md) (function, `0x00A36764`)
- `0x0029D36B` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x0029D3E0` → [IopAllocateFileObjectExtension](../41/IopAllocateFileObjectExtension_function_00418FB0.md) (function, `0x00418FB0`)
- `0x0029D454` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x0029D497` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x0029D4A1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0029D4B0` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0029D4D9` → [SeSinglePrivilegeCheck](../../page/87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x0029D511` → [IopCancelAlertedRequest](../../page/A9/IopCancelAlertedRequest_function_00A948F8.md) (function, `0x00A948F8`)

### Direct callers
- [DifNtSetInformationFileWrapper](../63/DifNtSetInformationFileWrapper_function_00637B30.md) at `0x00637C30`

### Static image references
- `0x0029C67A` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0029C946` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x0029CAD7` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0029CDA5` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0029CF68` → RVA `0x00FC6CC0` (`ALMOSTRO`; read)
- `0x0029D4D2` → RVA `0x00FD9AD0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x0029C730` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x0029C735` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
  - `0x0029CA8F` → [SeCaptureSubjectContextEx](../../page/8C/SeCaptureSubjectContextEx_function_008C4C90.md) (`.text` → `PAGE`)
  - `0x0029CAA0` → [RtlIsSandboxedToken](../../page/8B/RtlIsSandboxedToken_function_008B3AB0.md) (`.text` → `PAGE`)
  - `0x0029CAB0` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (`.text` → `PAGE`)
  - `0x0029CC0A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0029CC71` → [IopExceptionCleanupEx](../../page/8A/IopExceptionCleanupEx_function_008AE5C8.md) (`.text` → `PAGE`)
  - `0x0029CE3C` → [ObCloseHandle](../../page/8A/ObCloseHandle_function_008A1870.md) (`.text` → `PAGE`)
  - `0x0029CF91` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`.text` → `PAGE`)
  - `0x0029CFAB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0029D04B` → [IopWaitAndAcquireFileObjectLock](../../page/8A/IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (`.text` → `PAGE`)
  - `0x0029D0BF` → [IopAllocateIrpCleanup](../../page/A1/IopAllocateIrpCleanup_function_00A1E2D4.md) (`.text` → `PAGE`)
  - `0x0029D140` → [IopOpenLinkOrRenameTarget](../../page/8A/IopOpenLinkOrRenameTarget_function_008AAC04.md) (`.text` → `PAGE`)
  - `0x0029D1A8` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x0029D1B2` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
  - `0x0029D1D6` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
  - `0x0029D302` → [IopTrackLink](../../page/A3/IopTrackLink_function_00A36764.md) (`.text` → `PAGE`)
  - `0x0029D36B` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`.text` → `PAGE`)
  - `0x0029D4A1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0029D4D9` → [SeSinglePrivilegeCheck](../../page/87/SeSinglePrivilegeCheck_function_00871E20.md) (`.text` → `PAGE`)
  - `0x0029D511` → [IopCancelAlertedRequest](../../page/A9/IopCancelAlertedRequest_function_00A948F8.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x0029D0DC` → [sub_006DA8DA](../6D/Unknown_function_006DA8DA.md) (`tail-transfer`)
  - `0x0029D339` → [sub_006DA8DA + 0x87](../6D/Unknown_function_006DA8DA.md) (`tail-transfer`)
  - `0x0029D37B` → [sub_006DA8DA + 0x87](../6D/Unknown_function_006DA8DA.md) (`tail-transfer`)
  - `0x0029D4E0` → [sub_006DA8DA + 0xCC](../6D/Unknown_function_006DA8DA.md) (`tail-transfer`)
  - `0x0029D4EC` → [sub_006DA8DA + 0xEC](../6D/Unknown_function_006DA8DA.md) (`tail-transfer`)
  - `0x0029D4F8` → [sub_006DA8DA + 0xFE](../6D/Unknown_function_006DA8DA.md) (`tail-transfer`)
  - `0x0029D504` → [sub_006DA8DA + 0x117](../6D/Unknown_function_006DA8DA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0029C5E0  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0029C5E5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0029C5EA  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0029C5EF  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0029C5F4  53                              push rbx
0029C5F5  56                              push rsi
0029C5F6  57                              push rdi
0029C5F7  41 54                           push r12
0029C5F9  41 55                           push r13
0029C5FB  41 56                           push r14
0029C5FD  41 57                           push r15
0029C5FF  48 81 EC F0 00 00 00            sub rsp, 0xf0
0029C606  45 8B E9                        mov r13d, r9d
0029C609  4C 8B E1                        mov r12, rcx
0029C60C  45 33 F6                        xor r14d, r14d
0029C60F  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
0029C614  0F 57 C0                        xorps xmm0, xmm0
0029C617  33 C0                           xor eax, eax
0029C619  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
0029C61E  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0029C623  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
0029C62B  4C 89 B4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r14
0029C633  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0029C637  88 44 24 33                     mov byte ptr [rsp + 0x33], al
0029C63B  44 88 74 24 32                  mov byte ptr [rsp + 0x32], r14b
0029C640  44 88 74 24 41                  mov byte ptr [rsp + 0x41], r14b
0029C645  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
0029C64E  4C 89 54 24 78                  mov qword ptr [rsp + 0x78], r10
0029C653  45 0F B6 BA 32 02 00 00         movzx r15d, byte ptr [r10 + 0x232]
0029C65B  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
0029C660  45 84 FF                        test r15b, r15b
0029C663  0F 84 68 03 00 00               je 0x14029c9d1
0029C669  48 63 BC 24 50 01 00 00         movsxd rdi, dword ptr [rsp + 0x150]
0029C671  83 FF 54                        cmp edi, 0x54
0029C674  0F 83 B1 08 00 00               jae 0x14029cf2b
0029C67A  48 8D 1D 7F 39 D6 FF            lea rbx, [rip - 0x29c681]
0029C681  0F B6 84 1F E0 C8 B4 00         movzx eax, byte ptr [rdi + rbx + 0xb4c8e0]
0029C689  84 C0                           test al, al
0029C68B  0F 84 9A 08 00 00               je 0x14029cf2b
0029C691  44 3B E8                        cmp r13d, eax
0029C694  0F 82 CB 07 00 00               jb 0x14029ce65
0029C69A  49 BB 00 00 FF FF FF 7F 00 00   movabs r11, 0x7fffffff0000
0029C6A4  49 8B CB                        mov rcx, r11
0029C6A7  49 3B D3                        cmp rdx, r11
0029C6AA  48 0F 42 CA                     cmovb rcx, rdx
0029C6AE  8B 01                           mov eax, dword ptr [rcx]
0029C6B0  89 01                           mov dword ptr [rcx], eax
0029C6B2  49 8B 82 B8 00 00 00            mov rax, qword ptr [r10 + 0xb8]
0029C6B9  4C 39 B0 10 03 00 00            cmp qword ptr [rax + 0x310], r14
0029C6C0  74 45                           je 0x14029c707
0029C6C2  0F B7 88 EC 06 00 00            movzx ecx, word ptr [rax + 0x6ec]
0029C6C9  B8 4C 01 00 00                  mov eax, 0x14c
0029C6CE  66 3B C8                        cmp cx, ax
0029C6D1  75 2A                           jne 0x14029c6fd
0029C6D3  45 85 C9                        test r9d, r9d
0029C6D6  74 62                           je 0x14029c73a
0029C6D8  49 8B C6                        mov rax, r14
0029C6DB  B9 03 00 00 00                  mov ecx, 3
0029C6E0  41 83 FD 01                     cmp r13d, 1
0029C6E4  48 0F 45 C1                     cmovne rax, rcx
0029C6E8  49 85 C0                        test r8, rax
0029C6EB  75 43                           jne 0x14029c730
0029C6ED  4B 8D 0C 28                     lea rcx, [r8 + r13]
0029C6F1  49 3B CB                        cmp rcx, r11
0029C6F4  77 34                           ja 0x14029c72a
0029C6F6  49 3B C8                        cmp rcx, r8
0029C6F9  73 3F                           jae 0x14029c73a
0029C6FB  EB 2D                           jmp 0x14029c72a
0029C6FD  B8 C4 01 00 00                  mov eax, 0x1c4
0029C702  66 3B C8                        cmp cx, ax
0029C705  74 CC                           je 0x14029c6d3
0029C707  45 85 C9                        test r9d, r9d
0029C70A  74 2E                           je 0x14029c73a
0029C70C  0F B6 84 1F 20 C8 B4 00         movzx eax, byte ptr [rdi + rbx + 0xb4c820]
0029C714  48 FF C8                        dec rax
0029C717  49 85 C0                        test r8, rax
0029C71A  75 19                           jne 0x14029c735
0029C71C  4B 8D 0C 28                     lea rcx, [r8 + r13]
0029C720  49 3B CB                        cmp rcx, r11
0029C723  77 05                           ja 0x14029c72a
0029C725  49 3B C8                        cmp rcx, r8
0029C728  73 10                           jae 0x14029c73a
0029C72A  41 0F B6 03                     movzx eax, byte ptr [r11]
0029C72E  EB 0A                           jmp 0x14029c73a
0029C730  E8 9B D8 5F 00                  call 0x140899fd0
0029C735  E8 96 D8 5F 00                  call 0x140899fd0
0029C73A  EB 05                           jmp 0x14029c741
0029C73C  E9 3B 02 00 00                  jmp 0x14029c97c
0029C741  8B B4 BB 20 D9 B4 00            mov esi, dword ptr [rbx + rdi*4 + 0xb4d920]
0029C748  83 FF 48                        cmp edi, 0x48
0029C74B  0F 84 1C 03 00 00               je 0x14029ca6d
0029C751  83 FF 0B                        cmp edi, 0xb
0029C754  0F 84 13 03 00 00               je 0x14029ca6d
0029C75A  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0029C75F  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0029C764  45 0F B6 C7                     movzx r8d, r15b
0029C768  8B D6                           mov edx, esi
0029C76A  49 8B CC                        mov rcx, r12
0029C76D  E8 BE 0D 00 00                  call 0x14029d530
0029C772  44 8B F8                        mov r15d, eax
0029C775  85 C0                           test eax, eax
0029C777  0F 88 FF 01 00 00               js 0x14029c97c
0029C77D  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0029C782  F7 43 50 00 08 00 00            test dword ptr [rbx + 0x50], 0x800
0029C789  0F 85 12 0B 00 00               jne 0x14029d2a1
0029C78F  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0029C793  48 85 C9                        test rcx, rcx
0029C796  0F 85 F4 01 00 00               jne 0x14029c990
0029C79C  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0029C7A0  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
0029C7A4  48 85 C9                        test rcx, rcx
0029C7A7  0F 85 6E 08 00 00               jne 0x14029d01b
0029C7AD  48 8B C8                        mov rcx, rax
0029C7B0  48 83 79 18 00                  cmp qword ptr [rcx + 0x18], 0
0029C7B5  74 3A                           je 0x14029c7f1
0029C7B7  48 8B 83 D0 00 00 00            mov rax, qword ptr [rbx + 0xd0]
0029C7BE  48 85 C0                        test rax, rax
0029C7C1  74 0D                           je 0x14029c7d0
0029C7C3  4C 8B 40 10                     mov r8, qword ptr [rax + 0x10]
0029C7C7  4D 85 C0                        test r8, r8
0029C7CA  0F 85 72 02 00 00               jne 0x14029ca42
0029C7D0  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0029C7D4  48 85 C0                        test rax, rax
0029C7D7  74 13                           je 0x14029c7ec
0029C7D9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0029C7E0  48 8B C8                        mov rcx, rax
0029C7E3  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
0029C7E7  48 85 C0                        test rax, rax
0029C7EA  75 F4                           jne 0x14029c7e0
0029C7EC  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0029C7F1  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0029C7F6  4C 8D 63 50                     lea r12, [rbx + 0x50]
0029C7FA  41 8B 34 24                     mov esi, dword ptr [r12]
0029C7FE  40 F6 C6 02                     test sil, 2
0029C802  0F 84 F9 02 00 00               je 0x14029cb01
0029C808  C1 EE 02                        shr esi, 2
0029C80B  40 80 E6 01                     and sil, 1
0029C80F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0029C818  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0029C81F  90                              nop
0029C820  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0029C825  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
0029C82C  45 33 C0                        xor r8d, r8d
0029C82F  33 D2                           xor edx, edx
0029C831  E8 FA 39 F7 FF                  call 0x140210230
0029C836  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
0029C83B  B9 01 00 00 00                  mov ecx, 1
0029C840  87 4B 74                        xchg dword ptr [rbx + 0x74], ecx
0029C843  85 C9                           test ecx, ecx
0029C845  0F 85 E2 07 00 00               jne 0x14029d02d
0029C84B  48 85 C0                        test rax, rax
0029C84E  74 04                           je 0x14029c854
0029C850  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
0029C854  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0029C859  48 8B CB                        mov rcx, rbx
0029C85C  E8 BF 31 F7 FF                  call 0x14020fa20
0029C861  45 8B FE                        mov r15d, r14d
0029C864  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
0029C869  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
0029C86E  0F 85 7C 06 00 00               jne 0x14029cef0
0029C874  83 FF 0E                        cmp edi, 0xe
0029C877  0F 85 5B 06 00 00               jne 0x14029ced8
0029C87D  41 83 FD 08                     cmp r13d, 8
0029C881  0F 82 C9 05 00 00               jb 0x14029ce50
0029C887  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
0029C88F  48 8B 02                        mov rax, qword ptr [rdx]
0029C892  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
0029C89A  EB 22                           jmp 0x14029c8be
0029C89C  8B F8                           mov edi, eax
0029C89E  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0029C8A3  E8 E8 41 FB FF                  call 0x140250a90
0029C8A8  BA 44 66 6C 74                  mov edx, 0x746c6644
0029C8AD  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0029C8B2  E8 29 B0 05 00                  call 0x1402f78e0
0029C8B7  8B C7                           mov eax, edi
0029C8B9  E9 BE 00 00 00                  jmp 0x14029c97c
0029C8BE  41 8B 0C 24                     mov ecx, dword ptr [r12]
0029C8C2  F6 C1 08                        test cl, 8
0029C8C5  0F 85 5E 09 00 00               jne 0x14029d229
0029C8CB  48 8B C8                        mov rcx, rax
0029C8CE  48 C1 E9 20                     shr rcx, 0x20
0029C8D2  85 C9                           test ecx, ecx
0029C8D4  0F 88 51 01 00 00               js 0x14029ca2b
0029C8DA  48 89 43 68                     mov qword ptr [rbx + 0x68], rax
0029C8DE  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
0029C8E6  44 89 30                        mov dword ptr [rax], r14d
0029C8E9  4C 89 70 08                     mov qword ptr [rax + 8], r14
0029C8ED  BF 01 00 00 00                  mov edi, 1
0029C8F2  48 8D 35 07 37 D6 FF            lea rsi, [rip - 0x29c8f9]
0029C8F9  EB 1B                           jmp 0x14029c916
0029C8FB  45 33 F6                        xor r14d, r14d
0029C8FE  48 8D 35 FB 36 D6 FF            lea rsi, [rip - 0x29c905]
0029C905  41 8D 7E 01                     lea edi, [r14 + 1]
0029C909  44 8B AC 24 48 01 00 00         mov r13d, dword ptr [rsp + 0x148]
0029C911  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
0029C916  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0029C91F  41 8B CD                        mov ecx, r13d
0029C922  48 01 88 A8 03 00 00            add qword ptr [rax + 0x3a8], rcx
0029C929  65 48 01 0C 25 F8 2E 00 00      add qword ptr gs:[0x2ef8], rcx
0029C932  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0029C937  48 8B CB                        mov rcx, rbx
0029C93A  E8 51 41 FB FF                  call 0x140250a90
0029C93F  48 83 C3 D0                     add rbx, -0x30
0029C943  41 8B C6                        mov eax, r14d
0029C946  83 3D C3 86 D2 00 00            cmp dword ptr [rip + 0xd286c3], 0
0029C94D  0F 95 C0                        setne al
0029C950  85 C0                           test eax, eax
0029C952  74 13                           je 0x14029c967
0029C954  41 B9 44 66 6C 74               mov r9d, 0x746c6644
0029C95A  44 8B C7                        mov r8d, edi
0029C95D  33 D2                           xor edx, edx
0029C95F  48 8B CB                        mov rcx, rbx
0029C962  E8 7D 40 F7 FF                  call 0x1402109e4
0029C967  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0029C96E  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
0029C973  48 83 E8 01                     sub rax, 1
0029C977  7E 29                           jle 0x14029c9a2
0029C979  41 8B C7                        mov eax, r15d
0029C97C  48 81 C4 F0 00 00 00            add rsp, 0xf0
0029C983  41 5F                           pop r15
0029C985  41 5E                           pop r14
0029C987  41 5D                           pop r13
0029C989  41 5C                           pop r12
0029C98B  5F                              pop rdi
0029C98C  5E                              pop rsi
0029C98D  5B                              pop rbx
0029C98E  C3                              ret
0029C98F  CC                              int3
0029C990  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0029C994  48 85 C9                        test rcx, rcx
0029C997  0F 85 13 FE FF FF               jne 0x14029c7b0
0029C99D  E9 FA FD FF FF                  jmp 0x14029c79c
0029C9A2  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0029C9A6  48 85 C9                        test rcx, rcx
0029C9A9  0F 85 17 01 00 00               jne 0x14029cac6
0029C9AF  48 85 C0                        test rax, rax
0029C9B2  0F 89 A5 07 00 00               jns 0x14029d15d
0029C9B8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0029C9BD  44 8D 49 02                     lea r9d, [rcx + 2]
0029C9C1  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0029C9C6  33 D2                           xor edx, edx
0029C9C8  8D 4A 18                        lea ecx, [rdx + 0x18]
0029C9CB  E8 90 0C 26 00                  call 0x1404fd660
0029C9D0  CC                              int3
0029C9D1  8B BC 24 50 01 00 00            mov edi, dword ptr [rsp + 0x150]
0029C9D8  83 FF 38                        cmp edi, 0x38
0029C9DB  0F 84 A2 04 00 00               je 0x14029ce83
0029C9E1  83 FF 42                        cmp edi, 0x42
0029C9E4  0F 84 96 09 00 00               je 0x14029d380
0029C9EA  83 FF 39                        cmp edi, 0x39
0029C9ED  0F 84 C1 08 00 00               je 0x14029d2b4
0029C9F3  83 FF 49                        cmp edi, 0x49
0029C9F6  0F 84 AB 09 00 00               je 0x14029d3a7
0029C9FC  83 FF 4B                        cmp edi, 0x4b
0029C9FF  75 0A                           jne 0x14029ca0b
0029CA01  BF 47 00 00 00                  mov edi, 0x47
0029CA06  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
0029CA0B  48 63 C7                        movsxd rax, edi
0029CA0E  48 8D 0D EB 35 D6 FF            lea rcx, [rip - 0x29ca15]
0029CA15  8B B4 81 20 D9 B4 00            mov esi, dword ptr [rcx + rax*4 + 0xb4d920]
0029CA1C  E9 39 FD FF FF                  jmp 0x14029c75a
0029CA21  FF C9                           dec ecx
0029CA23  85 C8                           test eax, ecx
0029CA25  0F 84 A0 FE FF FF               je 0x14029c8cb
0029CA2B  BF 01 00 00 00                  mov edi, 1
0029CA30  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
0029CA36  48 8D 35 C3 35 D6 FF            lea rsi, [rip - 0x29ca3d]
0029CA3D  E9 D4 FE FF FF                  jmp 0x14029c916
0029CA42  4D 8B 00                        mov r8, qword ptr [r8]
0029CA45  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
0029CA4A  4D 85 C0                        test r8, r8
0029CA4D  0F 84 7D FD FF FF               je 0x14029c7d0
0029CA53  48 8B C1                        mov rax, rcx
0029CA56  49 3B C0                        cmp rax, r8
0029CA59  0F 84 E7 03 00 00               je 0x14029ce46
0029CA5F  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
0029CA63  48 85 C0                        test rax, rax
0029CA66  75 EE                           jne 0x14029ca56
0029CA68  E9 63 FD FF FF                  jmp 0x14029c7d0
0029CA6D  0F 11 84 24 B8 00 00 00         movups xmmword ptr [rsp + 0xb8], xmm0
0029CA75  0F 11 84 24 C8 00 00 00         movups xmmword ptr [rsp + 0xc8], xmm0
0029CA7D  4C 8D 84 24 B8 00 00 00         lea r8, [rsp + 0xb8]
0029CA85  49 8B 92 20 02 00 00            mov rdx, qword ptr [r10 + 0x220]
0029CA8C  49 8B CA                        mov rcx, r10
0029CA8F  E8 FC 81 62 00                  call 0x1408c4c90
0029CA94  41 0F B6 D7                     movzx edx, r15b
0029CA98  48 8D 8C 24 B8 00 00 00         lea rcx, [rsp + 0xb8]
0029CAA0  E8 0B 70 61 00                  call 0x1408b3ab0
0029CAA5  0F B6 D8                        movzx ebx, al
0029CAA8  48 8D 8C 24 B8 00 00 00         lea rcx, [rsp + 0xb8]
0029CAB0  E8 5B EC 5C 00                  call 0x14086b710
0029CAB5  84 DB                           test bl, bl
0029CAB7  0F 84 9D FC FF FF               je 0x14029c75a
0029CABD  0F BA EE 08                     bts esi, 8
0029CAC1  E9 94 FC FF FF                  jmp 0x14029c75a
0029CAC6  48 8B C3                        mov rax, rbx
0029CAC9  48 C1 E8 08                     shr rax, 8
0029CACD  0F B6 D0                        movzx edx, al
0029CAD0  0F B6 43 18                     movzx eax, byte ptr [rbx + 0x18]
0029CAD4  48 33 D0                        xor rdx, rax
0029CAD7  0F B6 05 6E A3 D2 00            movzx eax, byte ptr [rip + 0xd2a36e]
0029CADE  48 33 D0                        xor rdx, rax
0029CAE1  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0029CAE6  4C 8B CF                        mov r9, rdi
0029CAE9  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0029CAEE  48 8B 94 D6 00 78 FC 00         mov rdx, qword ptr [rsi + rdx*8 + 0xfc7800]
0029CAF6  B9 18 00 00 00                  mov ecx, 0x18
0029CAFB  E8 60 0B 26 00                  call 0x1404fd660
0029CB00  CC                              int3
0029CB01  66 C7 44 24 60 01 00            mov word ptr [rsp + 0x60], 1
0029CB08  C6 44 24 62 06                  mov byte ptr [rsp + 0x62], 6
0029CB0D  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
0029CB12  48 8D 44 24 68                  lea rax, [rsp + 0x68]
0029CB17  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0029CB1C  48 8D 44 24 68                  lea rax, [rsp + 0x68]
0029CB21  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0029CB26  40 32 F6                        xor sil, sil
0029CB29  40 88 74 24 31                  mov byte ptr [rsp + 0x31], sil
0029CB2E  48 8B CB                        mov rcx, rbx
0029CB31  E8 BA 0A 00 00                  call 0x14029d5f0
0029CB36  83 FF 24                        cmp edi, 0x24
0029CB39  0F 84 0F 07 00 00               je 0x14029d24e
0029CB3F  44 0F B6 C6                     movzx r8d, sil
0029CB43  41 80 F0 01                     xor r8b, 1
0029CB47  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0029CB4C  0F B6 50 4C                     movzx edx, byte ptr [rax + 0x4c]
0029CB50  48 8B C8                        mov rcx, rax
0029CB53  E8 C8 AB F6 FF                  call 0x140207720
0029CB58  48 8B F0                        mov rsi, rax
0029CB5B  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
0029CB63  48 85 C0                        test rax, rax
0029CB66  0F 84 4E 05 00 00               je 0x14029d0ba
0029CB6C  48 89 98 C0 00 00 00            mov qword ptr [rax + 0xc0], rbx
0029CB73  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0029CB78  48 89 86 98 00 00 00            mov qword ptr [rsi + 0x98], rax
0029CB7F  0F B6 44 24 30                  movzx eax, byte ptr [rsp + 0x30]
0029CB84  88 46 40                        mov byte ptr [rsi + 0x40], al
0029CB87  80 7C 24 31 00                  cmp byte ptr [rsp + 0x31], 0
0029CB8C  0F 85 DD 02 00 00               jne 0x14029ce6f
0029CB92  3C 01                           cmp al, 1
0029CB94  75 27                           jne 0x14029cbbd
0029CB96  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0029CB9F  8B 48 78                        mov ecx, dword ptr [rax + 0x78]
0029CBA2  C1 E9 06                        shr ecx, 6
0029CBA5  80 E1 01                        and cl, 1
0029CBA8  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
0029CBAC  74 06                           je 0x14029cbb4
0029CBAE  F0 0F BA 70 78 06               lock btr dword ptr [rax + 0x78], 6
0029CBB4  88 4C 24 33                     mov byte ptr [rsp + 0x33], cl
0029CBB8  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0029CBBD  C7 46 10 04 00 00 00            mov dword ptr [rsi + 0x10], 4
0029CBC4  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
0029CBCC  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0029CBD1  48 89 4E 50                     mov qword ptr [rsi + 0x50], rcx
0029CBD5  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
0029CBD9  4C 89 76 58                     mov qword ptr [rsi + 0x58], r14
0029CBDD  48 8B 86 B8 00 00 00            mov rax, qword ptr [rsi + 0xb8]
0029CBE4  48 83 E8 48                     sub rax, 0x48
0029CBE8  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0029CBED  C6 00 06                        mov byte ptr [rax], 6
0029CBF0  48 89 58 30                     mov qword ptr [rax + 0x30], rbx
0029CBF4  4C 89 76 18                     mov qword ptr [rsi + 0x18], r14
0029CBF8  4C 89 76 08                     mov qword ptr [rsi + 8], r14
0029CBFC  41 B8 49 6F 53 42               mov r8d, 0x42536f49
0029CC02  49 8B D5                        mov rdx, r13
0029CC05  B9 61 00 00 00                  mov ecx, 0x61
0029CC0A  E8 E1 54 8E 00                  call 0x140b820f0
0029CC0F  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0029CC14  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
0029CC18  4D 8B C5                        mov r8, r13
0029CC1B  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
0029CC23  48 8B C8                        mov rcx, rax
0029CC26  E8 15 9C 42 00                  call 0x1406c6840
0029CC2B  8D 4F ED                        lea ecx, [rdi - 0x13]
0029CC2E  83 F9 01                        cmp ecx, 1
0029CC31  76 05                           jbe 0x14029cc38
0029CC33  83 FF 0E                        cmp edi, 0xe
0029CC36  75 15                           jne 0x14029cc4d
0029CC38  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0029CC3D  83 78 04 00                     cmp dword ptr [rax + 4], 0
0029CC41  7D 0A                           jge 0x14029cc4d
0029CC43  B9 0D 00 00 C0                  mov ecx, 0xc000000d
0029CC48  E8 03 9E 05 00                  call 0x1402f6a50
0029CC4D  EB 3C                           jmp 0x14029cc8b
0029CC4F  8B D8                           mov ebx, eax
0029CC51  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0029CC56  0F B6 51 50                     movzx edx, byte ptr [rcx + 0x50]
0029CC5A  D1 EA                           shr edx, 1
0029CC5C  83 E2 01                        and edx, 1
0029CC5F  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
0029CC63  45 33 C9                        xor r9d, r9d
0029CC66  45 33 C0                        xor r8d, r8d
0029CC69  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
0029CC71  E8 52 19 61 00                  call 0x1408ae5c8
0029CC76  80 7C 24 33 00                  cmp byte ptr [rsp + 0x33], 0
0029CC7B  74 07                           je 0x14029cc84
0029CC7D  B1 01                           mov cl, 1
0029CC7F  E8 DC 3A 1B 00                  call 0x140450760
0029CC84  8B C3                           mov eax, ebx
0029CC86  E9 F1 FC FF FF                  jmp 0x14029c97c
0029CC8B  81 4E 10 30 08 00 00            or dword ptr [rsi + 0x10], 0x830
0029CC92  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0029CC97  44 89 6B 08                     mov dword ptr [rbx + 8], r13d
0029CC9B  89 7B 10                        mov dword ptr [rbx + 0x10], edi
0029CC9E  80 7C 24 41 00                  cmp byte ptr [rsp + 0x41], 0
0029CCA3  0F 84 37 02 00 00               je 0x14029cee0
0029CCA9  80 4B 02 01                     or byte ptr [rbx + 2], 1
0029CCAD  48 8B CE                        mov rcx, rsi
0029CCB0  E8 0B A9 F6 FF                  call 0x1402075c0
0029CCB5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0029CCBE  48 FF 80 90 03 00 00            inc qword ptr [rax + 0x390]
0029CCC5  65 FF 04 25 E4 2E 00 00         inc dword ptr gs:[0x2ee4]
0029CCCD  83 FF 10                        cmp edi, 0x10
0029CCD0  0F 84 F8 03 00 00               je 0x14029d0ce
0029CCD6  8D 47 F6                        lea eax, [rdi - 0xa]
0029CCD9  83 F8 3E                        cmp eax, 0x3e
0029CCDC  77 14                           ja 0x14029ccf2
0029CCDE  48 B9 03 00 20 00 00 00 80 40   movabs rcx, 0x4080000000200003
0029CCE8  48 0F A3 C1                     bt rcx, rax
0029CCEC  0F 82 C2 01 00 00               jb 0x14029ceb4
0029CCF2  83 FF 28                        cmp edi, 0x28
0029CCF5  0F 84 1C 07 00 00               je 0x14029d417
0029CCFB  83 FF 0D                        cmp edi, 0xd
0029CCFE  0F 84 FE 01 00 00               je 0x14029cf02
0029CD04  83 FF 40                        cmp edi, 0x40
0029CD07  0F 84 F5 01 00 00               je 0x14029cf02
0029CD0D  83 FF 1E                        cmp edi, 0x1e
0029CD10  0F 84 2F 02 00 00               je 0x14029cf45
0029CD16  83 FF 3D                        cmp edi, 0x3d
0029CD19  0F 84 FB 05 00 00               je 0x14029d31a
0029CD1F  83 FF 29                        cmp edi, 0x29
0029CD22  0F 84 B5 04 00 00               je 0x14029d1dd
0029CD28  83 FF 2A                        cmp edi, 0x2a
0029CD2B  0F 84 9C 07 00 00               je 0x14029d4cd
0029CD31  83 FF 2B                        cmp edi, 0x2b
0029CD34  0F 84 7C 06 00 00               je 0x14029d3b6
0029CD3A  83 FF 45                        cmp edi, 0x45
0029CD3D  0F 84 AE 07 00 00               je 0x14029d4f1
0029CD43  0F B6 7C 24 31                  movzx edi, byte ptr [rsp + 0x31]
0029CD48  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
0029CD50  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0029CD55  44 0F B6 C7                     movzx r8d, dil
0029CD59  48 8B D6                        mov rdx, rsi
0029CD5C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0029CD61  E8 5A E4 FF FF                  call 0x14029b1c0
0029CD66  44 8B F8                        mov r15d, eax
0029CD69  0F B6 44 24 30                  movzx eax, byte ptr [rsp + 0x30]
0029CD6E  41 81 FF 03 01 00 00            cmp r15d, 0x103
0029CD75  0F 84 17 01 00 00               je 0x14029ce92
0029CD7B  4C 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], r14
0029CD83  40 84 FF                        test dil, dil
0029CD86  75 04                           jne 0x14029cd8c
0029CD88  4C 89 76 50                     mov qword ptr [rsi + 0x50], r14
0029CD8C  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
0029CD94  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
0029CD98  44 0F 20 C3                     mov rbx, cr8
0029CD9C  B8 01 00 00 00                  mov eax, 1
0029CDA1  44 0F 22 C0                     mov cr8, rax
0029CDA5  83 3D 74 9F D2 00 00            cmp dword ptr [rip + 0xd29f74], 0
0029CDAC  0F 85 83 01 00 00               jne 0x14029cf35
0029CDB2  48 8D 4E 78                     lea rcx, [rsi + 0x78]
0029CDB6  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
0029CDBE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0029CDC3  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
0029CDC8  4C 8D 84 24 90 00 00 00         lea r8, [rsp + 0x90]
0029CDD0  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
0029CDD8  E8 73 E1 F6 FF                  call 0x14020af50
0029CDDD  83 3D 3C 9F D2 00 00            cmp dword ptr [rip + 0xd29f3c], 0
0029CDE4  74 0C                           je 0x14029cdf2
0029CDE6  44 0F 20 C1                     mov rcx, cr8
0029CDEA  0F B6 D3                        movzx edx, bl
0029CDED  E8 A6 88 25 00                  call 0x1404f5698
0029CDF2  0F B6 C3                        movzx eax, bl
0029CDF5  44 0F 22 C0                     mov cr8, rax
0029CDF9  40 84 FF                        test dil, dil
0029CDFC  74 0A                           je 0x14029ce08
0029CDFE  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0029CE03  E8 88 3C FB FF                  call 0x140250a90
0029CE08  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
0029CE0C  84 C0                           test al, al
0029CE0E  74 19                           je 0x14029ce29
0029CE10  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0029CE19  8B 41 78                        mov eax, dword ptr [rcx + 0x78]
0029CE1C  C1 E8 06                        shr eax, 6
0029CE1F  A8 01                           test al, 1
0029CE21  75 06                           jne 0x14029ce29
0029CE23  F0 0F BA 69 78 06               lock bts dword ptr [rcx + 0x78], 6
0029CE29  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
0029CE31  48 85 C9                        test rcx, rcx
0029CE34  0F 84 3F FB FF FF               je 0x14029c979
0029CE3A  33 D2                           xor edx, edx
0029CE3C  E8 2F 4A 60 00                  call 0x1408a1870
0029CE41  E9 33 FB FF FF                  jmp 0x14029c979
0029CE46  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0029CE4B  E9 A6 F9 FF FF                  jmp 0x14029c7f6
0029CE50  48 8B CB                        mov rcx, rbx
0029CE53  E8 38 3C FB FF                  call 0x140250a90
0029CE58  BA 44 66 6C 74                  mov edx, 0x746c6644
0029CE5D  48 8B CB                        mov rcx, rbx
0029CE60  E8 7B AA 05 00                  call 0x1402f78e0
0029CE65  B8 04 00 00 C0                  mov eax, 0xc0000004
0029CE6A  E9 0D FB FF FF                  jmp 0x14029c97c
0029CE6F  80 4E 47 02                     or byte ptr [rsi + 0x47], 2
0029CE73  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
0029CE7B  49 8B CE                        mov rcx, r14
0029CE7E  E9 4E FD FF FF                  jmp 0x14029cbd1
0029CE83  BF 0A 00 00 00                  mov edi, 0xa
0029CE88  C6 44 24 32 01                  mov byte ptr [rsp + 0x32], 1
0029CE8D  E9 79 FB FF FF                  jmp 0x14029ca0b
0029CE92  44 0F B6 C0                     movzx r8d, al
0029CE96  40 84 FF                        test dil, dil
0029CE99  0F 84 C0 01 00 00               je 0x14029d05f
0029CE9F  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0029CEA4  48 8B CE                        mov rcx, rsi
0029CEA7  E8 24 08 00 00                  call 0x14029d6d0
0029CEAC  44 8B F8                        mov r15d, eax
0029CEAF  E9 4A FF FF FF                  jmp 0x14029cdfe
0029CEB4  4C 8B 46 18                     mov r8, qword ptr [rsi + 0x18]
0029CEB8  41 8B 48 10                     mov ecx, dword ptr [r8 + 0x10]
0029CEBC  85 C9                           test ecx, ecx
0029CEBE  0F 85 29 02 00 00               jne 0x14029d0ed
0029CEC4  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
0029CECA  44 89 7E 30                     mov dword ptr [rsi + 0x30], r15d
0029CECE  0F B6 7C 24 31                  movzx edi, byte ptr [rsp + 0x31]
0029CED3  E9 91 FE FF FF                  jmp 0x14029cd69
0029CED8  40 B6 01                        mov sil, 1
0029CEDB  E9 49 FC FF FF                  jmp 0x14029cb29
0029CEE0  80 7C 24 32 00                  cmp byte ptr [rsp + 0x32], 0
0029CEE5  0F 85 BE FD FF FF               jne 0x14029cca9
0029CEEB  E9 BD FD FF FF                  jmp 0x14029ccad
0029CEF0  BA 44 66 6C 74                  mov edx, 0x746c6644
0029CEF5  48 8B CB                        mov rcx, rbx
0029CEF8  E8 E3 A9 05 00                  call 0x1402f78e0
0029CEFD  E9 77 FA FF FF                  jmp 0x14029c979
0029CF02  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0029CF06  0F B6 00                        movzx eax, byte ptr [rax]
0029CF09  83 FF 40                        cmp edi, 0x40
0029CF0C  0F 84 46 01 00 00               je 0x14029d058
0029CF12  84 C0                           test al, al
0029CF14  0F 84 29 FE FF FF               je 0x14029cd43
0029CF1A  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
0029CF22  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
0029CF26  E9 18 FE FF FF                  jmp 0x14029cd43
0029CF2B  B8 03 00 00 C0                  mov eax, 0xc0000003
0029CF30  E9 47 FA FF FF                  jmp 0x14029c97c
0029CF35  0F B6 D0                        movzx edx, al
0029CF38  0F B6 CB                        movzx ecx, bl
0029CF3B  E8 BC 87 25 00                  call 0x1404f56fc
0029CF40  E9 6D FE FF FF                  jmp 0x14029cdb2
0029CF45  48 8B 7E 18                     mov rdi, qword ptr [rsi + 0x18]
0029CF49  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0029CF4E  48 83 BB B0 00 00 00 00         cmp qword ptr [rbx + 0xb0], 0
0029CF56  0F 85 86 01 00 00               jne 0x14029d0e2
0029CF5C  41 8B 04 24                     mov eax, dword ptr [r12]
0029CF60  A8 02                           test al, 2
0029CF62  0F 85 7A 01 00 00               jne 0x14029d0e2
0029CF68  4C 8B 05 51 9D D2 00            mov r8, qword ptr [rip + 0xd29d51]
0029CF6F  48 8B 0F                        mov rcx, qword ptr [rdi]
0029CF72  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
0029CF77  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0029CF7C  48 8D 44 24 58                  lea rax, [rsp + 0x58]
0029CF81  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0029CF86  44 0F B6 4C 24 30               movzx r9d, byte ptr [rsp + 0x30]
0029CF8C  BA 02 00 00 00                  mov edx, 2
0029CF91  E8 1A BE 5C 00                  call 0x140868db0
0029CF96  44 8B F8                        mov r15d, eax
0029CF99  85 C0                           test eax, eax
0029CF9B  78 6C                           js 0x14029d009
0029CF9D  BA 18 00 00 00                  mov edx, 0x18
0029CFA2  8D 4A 28                        lea ecx, [rdx + 0x28]
0029CFA5  41 B8 49 6F 43 63               mov r8d, 0x63436f49
0029CFAB  E8 40 51 8E 00                  call 0x140b820f0
0029CFB0  4C 8B F8                        mov r15, rax
0029CFB3  48 85 C0                        test rax, rax
0029CFB6  0F 84 BE 02 00 00               je 0x14029d27a
0029CFBC  4C 8B EB                        mov r13, rbx
0029CFBF  49 81 C5 B8 00 00 00            add r13, 0xb8
0029CFC6  49 8B CD                        mov rcx, r13
0029CFC9  E8 A2 B4 F6 FF                  call 0x140208470
0029CFCE  49 8B CD                        mov rcx, r13
0029CFD1  48 83 BB B0 00 00 00 00         cmp qword ptr [rbx + 0xb0], 0
0029CFD9  0F 85 B5 04 00 00               jne 0x14029d494
0029CFDF  41 81 24 24 FF FB FF FF         and dword ptr [r12], 0xfffffbff
0029CFE7  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0029CFEC  49 89 17                        mov qword ptr [r15], rdx
0029CFEF  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
0029CFF3  49 89 57 08                     mov qword ptr [r15 + 8], rdx
0029CFF7  4C 89 BB B0 00 00 00            mov qword ptr [rbx + 0xb0], r15
0029CFFE  45 8B FE                        mov r15d, r14d
0029D001  0F B6 D0                        movzx edx, al
0029D004  E8 97 5B 0F 00                  call 0x140392ba0
0029D009  44 89 7E 30                     mov dword ptr [rsi + 0x30], r15d
0029D00D  4C 89 76 38                     mov qword ptr [rsi + 0x38], r14
0029D011  0F B6 7C 24 31                  movzx edi, byte ptr [rsp + 0x31]
0029D016  E9 4E FD FF FF                  jmp 0x14029cd69
0029D01B  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0029D01F  48 85 C9                        test rcx, rcx
0029D022  0F 85 88 F7 FF FF               jne 0x14029c7b0
0029D028  E9 80 F7 FF FF                  jmp 0x14029c7ad
0029D02D  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0029D032  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0029D037  4C 8B C8                        mov r9, rax
0029D03A  44 0F B6 C6                     movzx r8d, sil
0029D03E  0F B6 54 24 30                  movzx edx, byte ptr [rsp + 0x30]
0029D043  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0029D048  48 8B CB                        mov rcx, rbx
0029D04B  E8 88 16 61 00                  call 0x1408ae6d8
0029D050  44 8B F8                        mov r15d, eax
0029D053  E9 0C F8 FF FF                  jmp 0x14029c864
0029D058  24 01                           and al, 1
0029D05A  E9 B3 FE FF FF                  jmp 0x14029cf12
0029D05F  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0029D064  45 33 C9                        xor r9d, r9d
0029D067  33 D2                           xor edx, edx
0029D069  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0029D06E  E8 3D 16 F7 FF                  call 0x14020e6b0
0029D073  3D 01 01 00 00                  cmp eax, 0x101
0029D078  0F 84 8B 04 00 00               je 0x14029d509
0029D07E  3D C0 00 00 00                  cmp eax, 0xc0
0029D083  0F 84 80 04 00 00               je 0x14029d509
0029D089  44 8B BC 24 A0 00 00 00         mov r15d, dword ptr [rsp + 0xa0]
0029D091  0F 10 84 24 A0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xa0]
0029D099  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
0029D0A1  0F 11 00                        movups xmmword ptr [rax], xmm0
0029D0A4  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
0029D0A8  E9 5F FD FF FF                  jmp 0x14029ce0c
0029D0AD  44 8B F8                        mov r15d, eax
0029D0B0  0F B6 44 24 33                  movzx eax, byte ptr [rsp + 0x33]
0029D0B5  E9 52 FD FF FF                  jmp 0x14029ce0c
0029D0BA  33 D2                           xor edx, edx
0029D0BC  48 8B CB                        mov rcx, rbx
0029D0BF  E8 10 12 78 00                  call 0x140a1e2d4
0029D0C4  B8 9A 00 00 C0                  mov eax, 0xc000009a
0029D0C9  E9 AE F8 FF FF                  jmp 0x14029c97c
0029D0CE  4C 8B 4E 18                     mov r9, qword ptr [rsi + 0x18]
0029D0D2  45 8B 01                        mov r8d, dword ptr [r9]
0029D0D5  41 F7 C0 C9 FF FF FF            test r8d, 0xffffffc9
0029D0DC  0F 84 F8 D7 43 00               je 0x1406da8da
0029D0E2  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
0029D0E8  E9 1C FF FF FF                  jmp 0x14029d009
0029D0ED  F6 C1 01                        test cl, 1
0029D0F0  0F 85 CE FD FF FF               jne 0x14029cec4
0029D0F6  41 8D 45 EC                     lea eax, [r13 - 0x14]
0029D0FA  3B C1                           cmp eax, ecx
0029D0FC  0F 82 C2 FD FF FF               jb 0x14029cec4
0029D102  83 FF 1F                        cmp edi, 0x1f
0029D105  0F 84 B8 01 00 00               je 0x14029d2c3
0029D10B  83 FF 41                        cmp edi, 0x41
0029D10E  0F 84 2F 01 00 00               je 0x14029d243
0029D114  83 FF 48                        cmp edi, 0x48
0029D117  0F 84 26 01 00 00               je 0x14029d243
0029D11D  41 0F B6 00                     movzx eax, byte ptr [r8]
0029D121  88 43 20                        mov byte ptr [rbx + 0x20], al
0029D124  66 41 83 78 14 5C               cmp word ptr [r8 + 0x14], 0x5c
0029D12A  0F 85 54 03 00 00               jne 0x14029d484
0029D130  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
0029D135  48 8B D6                        mov rdx, rsi
0029D138  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
0029D140  E8 BF DA 60 00                  call 0x1408aac04
0029D145  44 8B F8                        mov r15d, eax
0029D148  0F B6 7C 24 31                  movzx edi, byte ptr [rsp + 0x31]
0029D14D  85 C0                           test eax, eax
0029D14F  0F 89 F3 FB FF FF               jns 0x14029cd48
0029D155  89 46 30                        mov dword ptr [rsi + 0x30], eax
0029D158  E9 0C FC FF FF                  jmp 0x14029cd69
0029D15D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0029D166  66 83 B8 E6 01 00 00 00         cmp word ptr [rax + 0x1e6], 0
0029D16E  0F 85 DD 02 00 00               jne 0x14029d451
0029D174  E8 E7 AE 05 00                  call 0x1402f8060
0029D179  84 C0                           test al, al
0029D17B  0F 84 D0 02 00 00               je 0x14029d451
0029D181  44 0F 20 C0                     mov rax, cr8
0029D185  3C 01                           cmp al, 1
0029D187  0F 83 C4 02 00 00               jae 0x14029d451
0029D18D  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
0029D191  A8 40                           test al, 0x40
0029D193  75 27                           jne 0x14029d1bc
0029D195  83 3D 74 7E D2 00 00            cmp dword ptr [rip + 0xd27e74], 0
0029D19C  41 0F 95 C6                     setne r14b
0029D1A0  45 85 F6                        test r14d, r14d
0029D1A3  74 08                           je 0x14029d1ad
0029D1A5  48 8B CB                        mov rcx, rbx
0029D1A8  E8 CB AD 73 00                  call 0x1409d7f78
0029D1AD  33 D2                           xor edx, edx
0029D1AF  48 8B CB                        mov rcx, rbx
0029D1B2  E8 A9 78 5C 00                  call 0x140864a60
0029D1B7  E9 BD F7 FF FF                  jmp 0x14029c979
0029D1BC  83 E0 7F                        and eax, 0x7f
0029D1BF  0F B6 84 30 80 FF F0 00         movzx eax, byte ptr [rax + rsi + 0xf0ff80]
0029D1C7  48 8B CB                        mov rcx, rbx
0029D1CA  48 2B C8                        sub rcx, rax
0029D1CD  48 8B 09                        mov rcx, qword ptr [rcx]
0029D1D0  80 79 18 00                     cmp byte ptr [rcx + 0x18], 0
0029D1D4  74 BF                           je 0x14029d195
0029D1D6  E8 55 AC 73 00                  call 0x1409d7e30
0029D1DB  EB B8                           jmp 0x14029d195
0029D1DD  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
0029D1E1  41 8B 0C 24                     mov ecx, dword ptr [r12]
0029D1E5  F6 C1 02                        test cl, 2
0029D1E8  0F 85 A1 01 00 00               jne 0x14029d38f
0029D1EE  45 8B FE                        mov r15d, r14d
0029D1F1  8B 02                           mov eax, dword ptr [rdx]
0029D1F3  A8 01                           test al, 1
0029D1F5  74 08                           je 0x14029d1ff
0029D1F7  0F BA E9 19                     bts ecx, 0x19
0029D1FB  41 89 0C 24                     mov dword ptr [r12], ecx
0029D1FF  8B 02                           mov eax, dword ptr [rdx]
0029D201  A8 02                           test al, 2
0029D203  74 08                           je 0x14029d20d
0029D205  0F BA E9 1A                     bts ecx, 0x1a
0029D209  41 89 0C 24                     mov dword ptr [r12], ecx
0029D20D  8B 02                           mov eax, dword ptr [rdx]
0029D20F  A8 04                           test al, 4
0029D211  0F 85 A9 02 00 00               jne 0x14029d4c0
0029D217  44 89 7E 30                     mov dword ptr [rsi + 0x30], r15d
0029D21B  4C 89 76 38                     mov qword ptr [rsi + 0x38], r14
0029D21F  0F B6 7C 24 31                  movzx edi, byte ptr [rsp + 0x31]
0029D224  E9 40 FB FF FF                  jmp 0x14029cd69
0029D229  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0029D22E  0F B7 89 30 01 00 00            movzx ecx, word ptr [rcx + 0x130]
0029D235  66 85 C9                        test cx, cx
0029D238  0F 84 8D F6 FF FF               je 0x14029c8cb
0029D23E  E9 DE F7 FF FF                  jmp 0x14029ca21
0029D243  41 0F B6 00                     movzx eax, byte ptr [r8]
0029D247  24 01                           and al, 1
0029D249  E9 D3 FE FF FF                  jmp 0x14029d121
0029D24E  41 83 FD 10                     cmp r13d, 0x10
0029D252  73 7A                           jae 0x14029d2ce
0029D254  BF 04 00 00 C0                  mov edi, 0xc0000004
0029D259  40 84 F6                        test sil, sil
0029D25C  74 08                           je 0x14029d266
0029D25E  48 8B CB                        mov rcx, rbx
0029D261  E8 2A 38 FB FF                  call 0x140250a90
0029D266  BA 44 66 6C 74                  mov edx, 0x746c6644
0029D26B  48 8B CB                        mov rcx, rbx
0029D26E  E8 6D A6 05 00                  call 0x1402f78e0
0029D273  8B C7                           mov eax, edi
0029D275  E9 02 F7 FF FF                  jmp 0x14029c97c
0029D27A  BA 44 66 6C 74                  mov edx, 0x746c6644
0029D27F  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0029D284  E8 57 A6 05 00                  call 0x1402f78e0
0029D289  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
0029D28F  44 89 7E 30                     mov dword ptr [rsi + 0x30], r15d
0029D293  4C 89 76 38                     mov qword ptr [rsi + 0x38], r14
0029D297  0F B6 7C 24 31                  movzx edi, byte ptr [rsp + 0x31]
0029D29C  E9 C8 FA FF FF                  jmp 0x14029cd69
0029D2A1  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0029D2A5  E8 66 35 17 00                  call 0x140410810
0029D2AA  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0029D2AF  E9 42 F5 FF FF                  jmp 0x14029c7f6
0029D2B4  BF 0B 00 00 00                  mov edi, 0xb
0029D2B9  C6 44 24 32 01                  mov byte ptr [rsp + 0x32], 1
0029D2BE  E9 48 F7 FF FF                  jmp 0x14029ca0b
0029D2C3  41 8B 00                        mov eax, dword ptr [r8]
0029D2C6  89 43 20                        mov dword ptr [rbx + 0x20], eax
0029D2C9  E9 56 FE FF FF                  jmp 0x14029d124
0029D2CE  40 84 F6                        test sil, sil
0029D2D1  0F 84 36 01 00 00               je 0x14029d40d
0029D2D7  48 8D 83 98 00 00 00            lea rax, [rbx + 0x98]
0029D2DE  0F B6 4C 24 30                  movzx ecx, byte ptr [rsp + 0x30]
0029D2E3  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
0029D2E7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0029D2EC  45 8B CD                        mov r9d, r13d
0029D2EF  4C 8B 84 24 40 01 00 00         mov r8, qword ptr [rsp + 0x140]
0029D2F7  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
0029D2FF  48 8B CB                        mov rcx, rbx
0029D302  E8 5D 94 79 00                  call 0x140a36764
0029D307  8B F8                           mov edi, eax
0029D309  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0029D30D  85 C0                           test eax, eax
0029D30F  0F 88 44 FF FF FF               js 0x14029d259
0029D315  E9 44 01 00 00                  jmp 0x14029d45e
0029D31A  48 8B 7E 18                     mov rdi, qword ptr [rsi + 0x18]
0029D31E  49 8B DE                        mov rbx, r14
0029D321  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0029D326  4C 39 B0 B0 00 00 00            cmp qword ptr [rax + 0xb0], r14
0029D32D  0F 84 AF FD FF FF               je 0x14029d0e2
0029D333  48 8B 0F                        mov rcx, qword ptr [rdi]
0029D336  48 85 C9                        test rcx, rcx
0029D339  0F 84 22 D6 43 00               je 0x1406da961
0029D33F  4C 8B 05 7A 99 D2 00            mov r8, qword ptr [rip + 0xd2997a]
0029D346  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
0029D34E  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0029D353  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
0029D35B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0029D360  44 0F B6 4C 24 30               movzx r9d, byte ptr [rsp + 0x30]
0029D366  BA 02 00 00 00                  mov edx, 2
0029D36B  E8 40 BA 5C 00                  call 0x140868db0
0029D370  44 8B F8                        mov r15d, eax
0029D373  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
0029D37B  E9 E1 D5 43 00                  jmp 0x1406da961
0029D380  BF 41 00 00 00                  mov edi, 0x41
0029D385  C6 44 24 32 01                  mov byte ptr [rsp + 0x32], 1
0029D38A  E9 7C F6 FF FF                  jmp 0x14029ca0b
0029D38F  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
0029D395  44 89 7E 30                     mov dword ptr [rsi + 0x30], r15d
0029D399  4C 89 76 38                     mov qword ptr [rsi + 0x38], r14
0029D39D  0F B6 7C 24 31                  movzx edi, byte ptr [rsp + 0x31]
0029D3A2  E9 C2 F9 FF FF                  jmp 0x14029cd69
0029D3A7  BF 48 00 00 00                  mov edi, 0x48
0029D3AC  C6 44 24 32 01                  mov byte ptr [rsp + 0x32], 1
0029D3B1  E9 55 F6 FF FF                  jmp 0x14029ca0b
0029D3B6  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0029D3BA  8B 08                           mov ecx, dword ptr [rax]
0029D3BC  83 F9 02                        cmp ecx, 2
0029D3BF  0F 87 1D FD FF FF               ja 0x14029d0e2
0029D3C5  8D 59 01                        lea ebx, [rcx + 1]
0029D3C8  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
0029D3D0  45 33 C0                        xor r8d, r8d
0029D3D3  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
0029D3DB  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0029D3E0  E8 CB BB 17 00                  call 0x140418fb0
0029D3E5  44 8B F8                        mov r15d, eax
0029D3E8  85 C0                           test eax, eax
0029D3EA  0F 88 19 FC FF FF               js 0x14029d009
0029D3F0  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0029D3F8  89 58 58                        mov dword ptr [rax + 0x58], ebx
0029D3FB  44 89 7E 30                     mov dword ptr [rsi + 0x30], r15d
0029D3FF  4C 89 76 38                     mov qword ptr [rsi + 0x38], r14
0029D403  0F B6 7C 24 31                  movzx edi, byte ptr [rsp + 0x31]
0029D408  E9 5C F9 FF FF                  jmp 0x14029cd69
0029D40D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0029D412  E9 C7 FE FF FF                  jmp 0x14029d2de
0029D417  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
0029D41B  41 8D 45 FC                     lea eax, [r13 - 4]
0029D41F  0F B6 7C 24 31                  movzx edi, byte ptr [rsp + 0x31]
0029D424  3B 01                           cmp eax, dword ptr [rcx]
0029D426  73 0F                           jae 0x14029d437
0029D428  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
0029D42E  44 89 7E 30                     mov dword ptr [rsi + 0x30], r15d
0029D432  E9 32 F9 FF FF                  jmp 0x14029cd69
0029D437  66 83 79 04 5C                  cmp word ptr [rcx + 4], 0x5c
0029D43C  0F 85 06 F9 FF FF               jne 0x14029cd48
0029D442  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
0029D448  44 89 7E 30                     mov dword ptr [rsi + 0x30], r15d
0029D44C  E9 18 F9 FF FF                  jmp 0x14029cd69
0029D451  48 8B CB                        mov rcx, rbx
0029D454  E8 3B 4F 10 00                  call 0x1403a2394
0029D459  E9 1B F5 FF FF                  jmp 0x14029c979
0029D45E  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
0029D466  4C 89 70 08                     mov qword ptr [rax + 8], r14
0029D46A  89 38                           mov dword ptr [rax], edi
0029D46C  E9 E8 FD FF FF                  jmp 0x14029d259
0029D471  8B 7C 24 50                     mov edi, dword ptr [rsp + 0x50]
0029D475  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0029D47A  0F B6 74 24 31                  movzx esi, byte ptr [rsp + 0x31]
0029D47F  E9 D5 FD FF FF                  jmp 0x14029d259
0029D484  49 83 78 08 00                  cmp qword ptr [r8 + 8], 0
0029D489  0F 84 B4 F8 FF FF               je 0x14029cd43
0029D48F  E9 9C FC FF FF                  jmp 0x14029d130
0029D494  0F B6 D0                        movzx edx, al
0029D497  E8 04 57 0F 00                  call 0x140392ba0
0029D49C  33 D2                           xor edx, edx
0029D49E  49 8B CF                        mov rcx, r15
0029D4A1  E8 CA 53 8E 00                  call 0x140b82870
0029D4A6  BA 44 66 6C 74                  mov edx, 0x746c6644
0029D4AB  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0029D4B0  E8 2B A4 05 00                  call 0x1402f78e0
0029D4B5  41 BF 48 00 00 C0               mov r15d, 0xc0000048
0029D4BB  E9 49 FB FF FF                  jmp 0x14029d009
0029D4C0  0F BA E9 1B                     bts ecx, 0x1b
0029D4C4  41 89 0C 24                     mov dword ptr [r12], ecx
0029D4C8  E9 4A FD FF FF                  jmp 0x14029d217
0029D4CD  0F B6 54 24 30                  movzx edx, byte ptr [rsp + 0x30]
0029D4D2  48 8B 0D F7 C5 D3 00            mov rcx, qword ptr [rip + 0xd3c5f7]
0029D4D9  E8 42 49 5D 00                  call 0x140871e20
0029D4DE  84 C0                           test al, al
0029D4E0  0F 85 C0 D4 43 00               jne 0x1406da9a6
0029D4E6  41 BF 61 00 00 C0               mov r15d, 0xc0000061
0029D4EC  E9 D5 D4 43 00                  jmp 0x1406da9c6
0029D4F1  0F B6 44 24 30                  movzx eax, byte ptr [rsp + 0x30]
0029D4F6  84 C0                           test al, al
0029D4F8  0F 84 DA D4 43 00               je 0x1406da9d8
0029D4FE  41 BF 22 00 00 C0               mov r15d, 0xc0000022
0029D504  E9 E8 D4 43 00                  jmp 0x1406da9f1
0029D509  48 8B D6                        mov rdx, rsi
0029D50C  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0029D511  E8 E2 73 7F 00                  call 0x140a948f8
0029D516  E9 6E FB FF FF                  jmp 0x14029d089
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetInformationFile(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int8 v_stack_mE7;
    unsigned __int8 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int8 v_stack_mF5;
    unsigned __int8 v_stack_mF6;
    unsigned __int8 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p138;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int8 v_stack_p31;
    unsigned __int8 v_stack_p32;
    unsigned __int8 v_stack_p33;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p41;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int16 v_stack_p60;
    unsigned __int8 v_stack_p62;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pE0;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (240);
    v_r14 = 0;
    v_stack_mF0 = 0;
    result = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m90 = 0;
    v_stack_mE4 = 0;
    v_stack_mF5 = 0;
    v_stack_mF6 = 0;
    v_stack_mE7 = 0;
    v_stack_mB0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_mF8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_0029C9D1;
    if (((unsigned int)((int)(a5))) >= 84) goto loc_0029CF2B;
    if ((unsigned __int8)(*(unsigned __int8 *)((int)(a5) + v_rip - 2737793 * 1 + 11847904)) == 0) goto loc_0029CF2B;
    if (((unsigned int)((unsigned int)(a4))) < ((unsigned int)(*(unsigned __int8 *)((int)(a5) + v_rip - 2737793 * 1 + 11847904)))) goto loc_0029CE65;
    a1 = v_r11;
    if (a2 < v_r11) { a1 = a2; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) == 0) goto loc_0029C707;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) != 332) goto loc_0029C6FD;
loc_0029C6D3:
    if (a4 == 0) goto loc_0029C73A;
    result = 0;
    if (((unsigned int)((unsigned int)(a4))) != 1) { result = 3; }
    if (((a3) & (result)) != 0) goto loc_0029C730;
    if ((a3 + (unsigned int)(a4) * 1) > v_r11) goto loc_0029C72A;
    if ((a3 + (unsigned int)(a4) * 1) >= a3) goto loc_0029C73A;
    goto loc_0029C72A;
loc_0029C6FD:
    if (((unsigned __int16)(a3 + (unsigned int)(a4) * 1)) == 452) goto loc_0029C6D3;
loc_0029C707:
    if (a4 == 0) goto loc_0029C73A;
    result = (*(unsigned __int8 *)((int)(a5) + v_rip - 2737793 * 1 + 11847712)) - 1;
    if (((a3) & (result)) != 0) goto loc_0029C735;
    if ((a3 + (unsigned int)(a4) * 1) > v_r11) goto loc_0029C72A;
    if ((a3 + (unsigned int)(a4) * 1) >= a3) goto loc_0029C73A;
loc_0029C72A:
    goto loc_0029C73A;
loc_0029C730:
    result = ExRaiseDatatypeMisalignment(a3 + (unsigned int)(a4) * 1, a2, a3, a4);
loc_0029C735:
    result = ExRaiseDatatypeMisalignment(a3 + (unsigned int)(a4) * 1, a2, a3, a4);
loc_0029C73A:
    goto loc_0029C741;
loc_0029C741:
    if (((unsigned int)((int)(a5))) == 72) goto loc_0029CA6D;
    if (((unsigned int)((int)(a5))) == 11) goto loc_0029CA6D;
loc_0029C75A:
    v_stack_m108 = 0;
    result = IopReferenceFileObject(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2737793 + (int)(a5) * 4 + 11852064)))), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mF0);
    if (sign_flag) goto loc_0029C97C;
    if (((*(unsigned int *)(v_stack_mF0 + 80)) & (0x800ULL)) != 0) goto loc_0029D2A1;
    if (*(unsigned __int64 *)(v_stack_mF0 + 16) != 0) goto loc_0029C990;
loc_0029C79C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 8) + 56) != 0) goto loc_0029D01B;
loc_0029C7AD:
loc_0029C7B0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 8) + 24)) == 0) goto loc_0029C7F1;
    if (*(unsigned __int64 *)(v_stack_mF0 + 208) == 0) goto loc_0029C7D0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 208) + 16) != 0) goto loc_0029CA42;
loc_0029C7D0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 8) + 24) == 0) goto loc_0029C7EC;
loc_0029C7E0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 8) + 24) + 24) != 0) goto loc_0029C7E0;
loc_0029C7EC:
loc_0029C7F1:
    v_stack_mE0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mF0 + 8) + 24);
loc_0029C7F6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 80)))) & (2)) == 0) goto loc_0029CB01;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mF0 + 80))) >> (2));
    v_rsi = (unsigned __int8)((v_rsi) & (1));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_mF0 + 128, a2, a3, v_stack_mF0);
    v_stack_mE8 = 0;
    if (1 != 0) goto loc_0029D02D;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(v_stack_mF0, a2, a3, v_stack_mF0);
loc_0029C864:
    v_stack_mD8 = 0;
    if (v_stack_mE8 != 0) goto loc_0029CEF0;
    if (((unsigned int)((int)(a5))) != 14) goto loc_0029CED8;
    if (((unsigned int)((unsigned int)(a4))) < 8) goto loc_0029CE50;
    v_stack_m50 = *(unsigned __int64 *)(v_stack_p18);
    goto loc_0029C8BE;
loc_0029C8BE:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 80)))) & (8)) != 0) goto loc_0029D229;
loc_0029C8CB:
    a1 = (*(unsigned __int64 *)(v_stack_p18)) >> (32);
    if (sign_flag) goto loc_0029CA2B;
    *(unsigned __int64 *)(v_stack_mF0 + 104) = *(unsigned __int64 *)(v_stack_p18);
    *(unsigned int *)(v_stack_p10) = 0;
    *(unsigned __int64 *)(v_stack_p10 + 8) = 0;
    goto loc_0029C916;
loc_0029C916:
    result = IopReleaseFileObjectLock(v_stack_mF0, v_stack_p18, a3, v_stack_mF0);
    v_rbx = (v_stack_mF0) + (-48);
    result = ((*(unsigned int *)(v_rip + 13797059)) != 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) {
        a4 = 0x746C6644ULL;
        a3 = 1;
        a2 = 0;
        a1 = v_rbx;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_0029C9A2;
loc_0029C979:
loc_0029C97C:
    v_rsp = (v_rsp) + (240);
    return 0;
loc_0029C990:
    if (*(unsigned __int64 *)(a1 + 8) != 0) goto loc_0029C7B0;
    goto loc_0029C79C;
loc_0029C9A2:
    if (*(unsigned __int64 *)(v_rbx + 8) != 0) goto loc_0029CAC6;
    if (!sign_flag) goto loc_0029D15D;
    v_stack_p20 = 0;
    a2 = 0;
    result = KeBugCheckEx(a2 + 24, a2, v_stack_p38, *(unsigned __int64 *)(v_rbx + 8) + 2);
loc_0029C9D1:
    if (((unsigned int)((unsigned int)(a5))) == 56) goto loc_0029CE83;
    if (((unsigned int)((unsigned int)(a5))) == 66) goto loc_0029D380;
    if (((unsigned int)((unsigned int)(a5))) == 57) goto loc_0029D2B4;
    if (((unsigned int)((unsigned int)(a5))) == 73) goto loc_0029D3A7;
    v_rdi = (unsigned int)(a5);
    if (((unsigned int)((unsigned int)(a5))) == 75) {
        v_rdi = 71;
        v_stack_p41 = 1;
    }
    goto loc_0029C75A;
loc_0029CA21:
    a1 = (unsigned int)((v_rip - 2738709) - 1);
    if ((((unsigned int)((int)((unsigned int)(v_rdi)))) & ((unsigned int)(a1))) == 0) goto loc_0029C8CB;
loc_0029CA2B:
    goto loc_0029C916;
loc_0029CA42:
    v_stack_p48 = *(unsigned __int64 *)(v_stack_p38);
    if (*(unsigned __int64 *)(v_stack_p38) == 0) goto loc_0029C7D0;
loc_0029CA56:
    if (a1 == (*(unsigned __int64 *)(v_stack_p38))) goto loc_0029CE46;
    if (*(unsigned __int64 *)(a1 + 24) != 0) goto loc_0029CA56;
    goto loc_0029C7D0;
loc_0029CA6D:
    v_stack_pB8 = v_xmm0;
    v_stack_pC8 = v_xmm0;
    result = SeCaptureSubjectContextEx(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), v_stack_pB8, *(unsigned __int64 *)(v_rbx + 8) + 2);
    result = RtlIsSandboxedToken(v_stack_pB8, (unsigned __int8)((unsigned int)(0xC000000DULL)), v_stack_pB8, *(unsigned __int64 *)(v_rbx + 8) + 2);
    result = SeReleaseSubjectContext(v_stack_pB8, (unsigned __int8)((unsigned int)(0xC000000DULL)), v_stack_pB8, *(unsigned __int64 *)(v_rbx + 8) + 2);
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0029C75A;
    goto loc_0029C75A;
loc_0029CAC6:
    result = ((unsigned __int8)(result)) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)((unsigned __int8)(result) + 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 13804398));
    v_stack_p20 = v_stack_pB8;
    result = KeBugCheckEx(24, *(unsigned __int64 *)(v_rip - 2738749 + a2 * 8 + 16545792), v_stack_p38, 1);
loc_0029CB01:
    v_stack_p60 = 1;
    v_stack_p62 = 6;
    v_stack_p64 = 0;
    v_stack_p70 = v_stack_p68;
    v_stack_p68 = v_stack_p68;
    v_rsi = 0;
loc_0029CB29:
    v_stack_p31 = 0;
    result = IopResetEvent((unsigned __int8)(result), *(unsigned __int64 *)(v_rip - 2738749 + a2 * 8 + 16545792), v_stack_p38, 1);
    if (1 == 36) goto loc_0029D24E;
    a3 = (unsigned __int8)((0) ^ (1));
    result = IopAllocateIrpExReturn(v_stack_p48, *(unsigned __int8 *)(v_stack_p48 + 76), a3, 1);
    v_stack_pB0 = result;
    if (result == 0) goto loc_0029D0BA;
    *(unsigned __int64 *)(result + 192) = (unsigned __int8)(result);
    *(unsigned __int64 *)(result + 152) = v_stack_p78;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)(v_stack_p30);
    if (v_stack_p31 != 0) goto loc_0029CE6F;
    if (((unsigned __int8)(v_stack_p30)) != 1) goto loc_0029CBBD;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120))) >> (6));
    a1 = (unsigned __int8)((a1) & (1));
    v_stack_p44 = (unsigned int)(a1);
    if (!(condition_is_equal)) {
    }
    v_stack_p33 = (unsigned __int8)(a1);
loc_0029CBBD:
    *(unsigned int *)(result + 16) = 4;
loc_0029CBD1:
    *(unsigned __int64 *)(result + 80) = v_stack_p60;
    *(unsigned __int64 *)(result + 72) = v_stack_pA0;
    *(unsigned __int64 *)(result + 88) = 0;
    result = (*(unsigned __int64 *)(result + 184)) - (72);
    v_stack_p50 = result;
    *(unsigned __int8 *)(result) = 6;
    *(unsigned __int64 *)(result + 48) = v_stack_p38;
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    result = ExAllocatePool2(97, (unsigned int)(a4), (unsigned int)(0x42536F49ULL), 1);
    v_stack_p78 = result;
    *(unsigned __int64 *)(result + 24) = result;
    result = memcpy(result, v_stack_p140, (unsigned int)(a4), 1);
    if (((unsigned int)(1 - 19)) <= 1) goto loc_0029CC38;
    if (1 != 14) goto loc_0029CC4D;
loc_0029CC38:
    result = v_stack_p78;
    if ((*(unsigned int *)(v_stack_p78 + 4)) < 0) {
        a1 = 0xC000000DULL;
        result = RtlRaiseStatus(a1, v_stack_p140, (unsigned int)(a4), 1);
    }
    goto loc_0029CC8B;
loc_0029CC8B:
    *(unsigned int *)(v_stack_p50 + 8) = (unsigned int)((unsigned int)(a4));
    *(unsigned int *)(v_stack_p50 + 16) = 1;
    if (v_stack_p41 == 0) goto loc_0029CEE0;
loc_0029CCA9:
loc_0029CCAD:
    result = IopQueueThreadIrp(result, v_stack_p140, (unsigned int)(a4), 1);
    if (1 == 16) goto loc_0029D0CE;
    if (((unsigned int)(1 - 10)) > 62) goto loc_0029CCF2;
    if (((unsigned int)(1 - 10)) < 62) goto loc_0029CEB4;
loc_0029CCF2:
    if (1 == 40) goto loc_0029D417;
    if (1 == 13) goto loc_0029CF02;
    if (1 == 64) goto loc_0029CF02;
    if (1 == 30) goto loc_0029CF45;
    if (1 == 61) goto loc_0029D31A;
    if (1 == 41) goto loc_0029D1DD;
    if (1 == 42) goto loc_0029D4CD;
    if (1 == 43) goto loc_0029D3B6;
    if (1 == 69) goto loc_0029D4F1;
loc_0029CD43:
loc_0029CD48:
    v_stack_p20 = 2;
    result = IopCallDriverReference(v_stack_p48, result, (unsigned __int8)(v_stack_p31), v_stack_p38);
loc_0029CD69:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 259) goto loc_0029CE92;
    v_stack_p90 = 0;
    if ((unsigned __int8)(v_stack_p31) == 0) {
        *(unsigned __int64 *)(result + 80) = 0;
    }
    *(unsigned __int64 *)(result + 72) = v_stack_p138;
    if ((*(unsigned int *)(v_rip + 13803380)) != 0) goto loc_0029CF35;
loc_0029CDB2:
    v_stack_p20 = v_stack_p90;
    result = IopCompleteRequest(result + 120, v_stack_pE0, v_stack_p90, v_stack_p38);
    if ((*(unsigned int *)(v_rip + 13803324)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_p90, v_stack_p38);
    }
    result = (unsigned __int8)(v_cr8);
    if ((unsigned __int8)(v_stack_p31) != 0) {
        a1 = v_stack_p38;
        result = IopReleaseFileObjectLock(a1, a2, v_stack_p90, v_stack_p38);
    }
loc_0029CE0C:
    if ((unsigned __int8)((unsigned int)(v_stack_p44)) == 0) goto loc_0029CE29;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120))) >> (6));
    if ((((unsigned __int8)(result)) & (1)) == 0) {
    }
    if (v_stack_p98 == 0) goto loc_0029C979;
    a2 = 0;
    result = ObCloseHandle(v_stack_p98, a2, v_stack_p90, v_stack_p38);
    goto loc_0029C979;
loc_0029CE46:
    goto loc_0029C7F6;
loc_0029CE50:
    result = IopReleaseFileObjectLock(v_stack_p38, a2, v_stack_p90, v_stack_p38);
    result = ObfDereferenceObjectWithTag(v_stack_p38, (unsigned int)(0x746C6644ULL), v_stack_p90, v_stack_p38);
loc_0029CE65:
    goto loc_0029C97C;
loc_0029CE6F:
    goto loc_0029CBD1;
loc_0029CE83:
    v_stack_p32 = 1;
    goto loc_0029CA0B;
loc_0029CE92:
    if (10 == 0) goto loc_0029D05F;
    result = IopWaitForSynchronousIo(result, v_stack_p38, (unsigned __int8)(v_stack_p138), v_stack_p38);
    goto loc_0029CDFE;
loc_0029CEB4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 24) + 16))) != 0) goto loc_0029D0ED;
loc_0029CEC4:
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_0029CD69;
loc_0029CED8:
    goto loc_0029CB29;
loc_0029CEE0:
    if (v_stack_p32 != 0) goto loc_0029CCA9;
    goto loc_0029CCAD;
loc_0029CEF0:
    result = ObfDereferenceObjectWithTag(v_stack_p38, (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(result + 24), v_stack_p38);
    goto loc_0029C979;
loc_0029CF02:
    if (((unsigned int)(v_stack_p31)) == 64) goto loc_0029D058;
loc_0029CF12:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(1 + 24))) == 0) goto loc_0029CD43;
    *(unsigned __int64 *)(v_stack_p38 + 32) = v_stack_p130;
    goto loc_0029CD43;
loc_0029CF2B:
    goto loc_0029C97C;
loc_0029CF35:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p38), (unsigned __int8)((unsigned int)(0xC0000003ULL)), *(unsigned __int64 *)(result + 24), v_stack_p38);
    goto loc_0029CDB2;
loc_0029CF45:
    if ((*(unsigned __int64 *)(v_stack_p38 + 176)) != 0) goto loc_0029D0E2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 80)))) & (2)) != 0) goto loc_0029D0E2;
    v_stack_p58 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p58;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(*(unsigned __int64 *)(1 + 24)), 2, *(unsigned __int64 *)(v_rip + 13802833), v_stack_p30);
    if (sign_flag) goto loc_0029D009;
    result = ExAllocatePool2(24 + 40, 24, (unsigned int)(0x63436F49ULL), v_stack_p30);
    if (result == 0) goto loc_0029D27A;
    v_r13 = (v_stack_p38) + (184);
    result = KeAcquireSpinLockRaiseToDpc(v_r13, 24, (unsigned int)(0x63436F49ULL), v_stack_p30);
    if ((*(unsigned __int64 *)(v_stack_p38 + 176)) != 0) goto loc_0029D494;
    *(unsigned __int64 *)(result) = v_stack_p58;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 24) + 8);
    *(unsigned __int64 *)(v_stack_p38 + 176) = result;
    result = KeReleaseSpinLock(v_r13, (unsigned __int8)(result), (unsigned int)(0x63436F49ULL), v_stack_p30);
loc_0029D009:
    *(unsigned int *)(1 + 48) = 0;
    *(unsigned __int64 *)(1 + 56) = 0;
    goto loc_0029CD69;
loc_0029D01B:
    if (*(unsigned __int64 *)(v_r13 + 8) != 0) goto loc_0029C7B0;
    goto loc_0029C7AD;
loc_0029D02D:
    v_stack_p20 = v_stack_p40;
    result = IopWaitAndAcquireFileObjectLock(v_stack_p38, v_stack_p30, 1, result);
    goto loc_0029C864;
loc_0029D058:
    result = (unsigned __int8)((result) & (1));
    goto loc_0029CF12;
loc_0029D05F:
    v_stack_p20 = 0;
    a4 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_stack_p60, a2, 1, a4);
    if (((unsigned int)(result)) == 257) goto loc_0029D509;
    if (((unsigned int)(result)) == 192) goto loc_0029D509;
loc_0029D089:
    *(unsigned __int64 *)(v_stack_p138) = v_xmm0;
    goto loc_0029CE0C;
loc_0029D0BA:
    a2 = 0;
    result = IopAllocateIrpCleanup(v_stack_p38, a2, 1, a4);
    goto loc_0029C97C;
loc_0029D0CE:
loc_0029D0E2:
    goto loc_0029D009;
loc_0029D0ED:
    if ((((unsigned __int8)(v_stack_p38)) & (1)) != 0) goto loc_0029CEC4;
    if (((unsigned int)(v_r13 - 20)) < ((unsigned int)(v_stack_p38))) goto loc_0029CEC4;
    if (((unsigned int)(v_stack_p31)) == 31) goto loc_0029D2C3;
    if (((unsigned int)(v_stack_p31)) == 65) goto loc_0029D243;
    if (((unsigned int)(v_stack_p31)) == 72) goto loc_0029D243;
loc_0029D121:
    *(unsigned __int8 *)(v_stack_p38 + 32) = (unsigned __int8)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24)))));
loc_0029D124:
    if ((*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))) + 20)) != 92) goto loc_0029D484;
loc_0029D130:
    result = IopOpenLinkOrRenameTarget(v_stack_p98, 1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))), v_stack_p38);
    if (!sign_flag) goto loc_0029CD48;
    *(unsigned int *)(1 + 48) = (unsigned int)(result);
    goto loc_0029CD69;
loc_0029D15D:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_0029D451;
    result = KeAreInterruptsEnabled(v_stack_p98, 1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))), v_stack_p38);
    if ((unsigned __int8)(result) == 0) goto loc_0029D451;
    if (((unsigned __int8)((unsigned __int8)(v_cr8))) >= 1) goto loc_0029D451;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p38 + 26))) & (64)) != 0) goto loc_0029D1BC;
loc_0029D195:
    v_r14 = ((*(unsigned int *)(v_rip + 13794932)) != 0) ? 1 : 0;
    result = *(unsigned __int8 *)(v_stack_p38 + 26);
    if ((unsigned int)(v_r14) != 0) {
        a1 = v_stack_p38;
        result = ObpDeregisterObject(a1, 1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))), v_stack_p38);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p38, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))), v_stack_p38);
    goto loc_0029C979;
loc_0029D1BC:
    result = (unsigned int)((result) & (127));
    a1 = (v_stack_p38) - (*(unsigned __int8 *)(result + 1 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == 0) goto loc_0029D195;
    result = ObpHandleRevocationBlockRemoveObject(*(unsigned __int64 *)(a1), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))), v_stack_p38);
    goto loc_0029D195;
loc_0029D1DD:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 80)))) & (2)) != 0) goto loc_0029D38F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))))) & (1)) != 0) {
        *(unsigned int *)(v_stack_mF0 + 80) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 80)));
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))))) & (2)) != 0) {
        *(unsigned int *)(v_stack_mF0 + 80) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 80)));
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))))) & (4)) != 0) goto loc_0029D4C0;
loc_0029D217:
    *(unsigned int *)(1 + 48) = (unsigned int)((unsigned int)((unsigned int)(v_r14)));
    *(unsigned __int64 *)(1 + 56) = v_r14;
    goto loc_0029CD69;
loc_0029D229:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_p48 + 304)) == 0) goto loc_0029C8CB;
    goto loc_0029CA21;
loc_0029D243:
    result = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))))) & (1));
    goto loc_0029D121;
loc_0029D24E:
    if (((unsigned int)(v_r13)) >= 16) goto loc_0029D2CE;
loc_0029D259:
    if (1 != 0) {
        a1 = v_stack_p38;
        result = IopReleaseFileObjectLock(a1, *(unsigned __int64 *)(1 + 24), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))), v_stack_p38);
    }
    result = ObfDereferenceObjectWithTag(v_stack_p38, (unsigned int)(0x746C6644ULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))), v_stack_p38);
    goto loc_0029C97C;
loc_0029D27A:
    result = ObfDereferenceObjectWithTag(v_stack_p58, (unsigned int)(0x746C6644ULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))), v_stack_p38);
    *(unsigned int *)(1 + 48) = (unsigned int)((unsigned int)(0xC000009AULL));
    *(unsigned __int64 *)(1 + 56) = v_r14;
    goto loc_0029CD69;
loc_0029D2A1:
    result = IoGetAttachedDevice(*(unsigned __int64 *)(v_stack_p38 + 8), (unsigned int)(0x746C6644ULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))), v_stack_p38);
    v_stack_p48 = result;
    goto loc_0029C7F6;
loc_0029D2B4:
    v_stack_p32 = 1;
    goto loc_0029CA0B;
loc_0029D2C3:
    *(unsigned int *)(v_stack_p38 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))))));
    goto loc_0029D124;
loc_0029D2CE:
    if (1 == 0) goto loc_0029D40D;
loc_0029D2DE:
    v_stack_p28 = (unsigned __int8)(v_stack_p30);
    v_stack_p20 = v_stack_p38 + 152;
    result = IopTrackLink(v_stack_p38, v_stack_pA0, v_stack_p140, (unsigned int)((unsigned int)(v_r13)));
    v_stack_p50 = (unsigned int)(result);
    if (sign_flag) goto loc_0029D259;
    goto loc_0029D45E;
loc_0029D31A:
    if ((*(unsigned __int64 *)(v_stack_p38 + 176)) == v_r14) goto loc_0029D0E2;
    v_stack_p80 = v_r14;
    v_stack_p28 = v_r14;
    v_stack_p20 = v_stack_p80;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(*(unsigned __int64 *)(1 + 24)), 2, *(unsigned __int64 *)(v_rip + 13801850), v_stack_p30);
loc_0029D380:
    v_stack_p32 = 1;
    goto loc_0029CA0B;
loc_0029D38F:
    *(unsigned int *)(1 + 48) = (unsigned int)((unsigned int)(0xC000000DULL));
    *(unsigned __int64 *)(1 + 56) = v_r14;
    goto loc_0029CD69;
loc_0029D3A7:
    v_stack_p32 = 1;
    goto loc_0029CA0B;
loc_0029D3B6:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))))) > 2) goto loc_0029D0E2;
    v_stack_p88 = v_r14;
    a3 = 0;
    result = IopAllocateFileObjectExtension(v_stack_p38, v_stack_p88, a3, v_stack_p30);
    if (sign_flag) goto loc_0029D009;
    *(unsigned int *)(v_stack_p88 + 88) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))) + 1);
    *(unsigned int *)(1 + 48) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(1 + 56) = v_r14;
    goto loc_0029CD69;
loc_0029D40D:
    goto loc_0029D2DE;
loc_0029D417:
    if (((unsigned int)(v_r13 - 4)) >= (*(unsigned int *)(*(unsigned __int64 *)(1 + 24)))) goto loc_0029D437;
    *(unsigned int *)(1 + 48) = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_0029CD69;
loc_0029D437:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(1 + 24) + 4)) != 92) goto loc_0029CD48;
    *(unsigned int *)(1 + 48) = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_0029CD69;
loc_0029D451:
    result = ObpDeferObjectDeletion((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))) + 1, v_stack_p88, a3, v_stack_p30);
    goto loc_0029C979;
loc_0029D45E:
    *(unsigned __int64 *)(v_stack_p138 + 8) = v_r14;
    *(unsigned int *)(v_stack_p138) = (unsigned int)(v_stack_p31);
    goto loc_0029D259;
loc_0029D484:
    if ((*(unsigned __int64 *)(a3 + 8)) == 0) goto loc_0029CD43;
    goto loc_0029D130;
loc_0029D494:
    result = KeReleaseSpinLock((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 24))) + 1, (unsigned __int8)(v_stack_p138), a3, v_stack_p30);
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)(0xC000000DULL), a2, a3, v_stack_p30);
    result = ObfDereferenceObjectWithTag(v_stack_p58, (unsigned int)(0x746C6644ULL), a3, v_stack_p30);
    goto loc_0029D009;
loc_0029D4C0:
    *(unsigned int *)(v_stack_mF0 + 80) = (unsigned int)(v_stack_p58);
    goto loc_0029D217;
loc_0029D4CD:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 13878775), v_stack_p30, a3, v_stack_p30);
loc_0029D4F1:
loc_0029D509:
    result = IopCancelAlertedRequest(v_stack_p60, 1, a3, v_stack_p30);
    goto loc_0029D089;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetInformationFile(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m50;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint8_t v_stack_mE7;
    uint8_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint8_t v_stack_mF5;
    uint8_t v_stack_mF6;
    uint8_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p130;
    uint64_t v_stack_p138;
    uint64_t v_stack_p140;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint8_t v_stack_p31;
    uint8_t v_stack_p32;
    uint8_t v_stack_p33;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p41;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint16_t v_stack_p60;
    uint8_t v_stack_p62;
    uint32_t v_stack_p64;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pE0;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (240);
    local_r14 = 0;
    v_stack_mF0 = 0;
    result = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = 0;
    v_stack_m88 = v_xmm0;
    v_stack_m90 = 0;
    v_stack_mE4 = 0;
    v_stack_mF5 = 0;
    v_stack_mF6 = 0;
    v_stack_mE7 = 0;
    v_stack_mB0 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_mF8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_0029C9D1;
    if (((uint32_t)((int32_t)(Arg5))) >= 84) goto loc_0029CF2B;
    if ((uint8_t)(*(uint8_t *)((int32_t)(Arg5) + v_rip - 0x29C681 * 1 + 0xB4C8E0)) == 0) goto loc_0029CF2B;
    if (((uint32_t)((uint32_t)(Arg4))) < ((uint32_t)(*(uint8_t *)((int32_t)(Arg5) + v_rip - 0x29C681 * 1 + 0xB4C8E0)))) goto loc_0029CE65;
    Arg1 = local_r11;
    if (Arg2 < local_r11) { Arg1 = Arg2; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) == 0) goto loc_0029C707;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) != 332) goto loc_0029C6FD;
loc_0029C6D3:
    if (Arg4 == 0) goto loc_0029C73A;
    result = 0;
    if (((uint32_t)((uint32_t)(Arg4))) != 1) { result = 3; }
    if (((Arg3) & (result)) != 0) goto loc_0029C730;
    if ((Arg3 + (uint32_t)(Arg4) * 1) > local_r11) goto loc_0029C72A;
    if ((Arg3 + (uint32_t)(Arg4) * 1) >= Arg3) goto loc_0029C73A;
    goto loc_0029C72A;
loc_0029C6FD:
    if (((uint16_t)(Arg3 + (uint32_t)(Arg4) * 1)) == 452) goto loc_0029C6D3;
loc_0029C707:
    if (Arg4 == 0) goto loc_0029C73A;
    result = (*(uint8_t *)((int32_t)(Arg5) + v_rip - 0x29C681 * 1 + 0xB4C820)) - 1;
    if (((Arg3) & (result)) != 0) goto loc_0029C735;
    if ((Arg3 + (uint32_t)(Arg4) * 1) > local_r11) goto loc_0029C72A;
    if ((Arg3 + (uint32_t)(Arg4) * 1) >= Arg3) goto loc_0029C73A;
loc_0029C72A:
    goto loc_0029C73A;
loc_0029C730:
    result = ExRaiseDatatypeMisalignment(Arg3 + (uint32_t)(Arg4) * 1, Arg2, Arg3, Arg4);
loc_0029C735:
    result = ExRaiseDatatypeMisalignment(Arg3 + (uint32_t)(Arg4) * 1, Arg2, Arg3, Arg4);
loc_0029C73A:
    goto loc_0029C741;
loc_0029C741:
    if (((uint32_t)((int32_t)(Arg5))) == 72) goto loc_0029CA6D;
    if (((uint32_t)((int32_t)(Arg5))) == 11) goto loc_0029CA6D;
loc_0029C75A:
    v_stack_m108 = 0;
    result = IopReferenceFileObject(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x29C681 + (int32_t)(Arg5) * 4 + 0xB4D920)))), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mF0);
    if (sign_flag) goto loc_0029C97C;
    if (((*(uint32_t *)(v_stack_mF0 + 0x50)) & (0x800ULL)) != 0) goto loc_0029D2A1;
    if (*(uint64_t *)(v_stack_mF0 + 0x10) != 0) goto loc_0029C990;
loc_0029C79C:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x8) + 0x38) != 0) goto loc_0029D01B;
loc_0029C7AD:
loc_0029C7B0:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x8) + 0x18)) == 0) goto loc_0029C7F1;
    if (*(uint64_t *)(v_stack_mF0 + 0xD0) == 0) goto loc_0029C7D0;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0xD0) + 0x10) != 0) goto loc_0029CA42;
loc_0029C7D0:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x8) + 0x18) == 0) goto loc_0029C7EC;
loc_0029C7E0:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x8) + 0x18) + 0x18) != 0) goto loc_0029C7E0;
loc_0029C7EC:
loc_0029C7F1:
    v_stack_mE0 = *(uint64_t *)(*(uint64_t *)(v_stack_mF0 + 0x8) + 0x18);
loc_0029C7F6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x50)))) & (2)) == 0) goto loc_0029CB01;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x50))) >> (2));
    local_rsi = (uint8_t)((local_rsi) & (1));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_mF0 + 128, Arg2, Arg3, v_stack_mF0);
    v_stack_mE8 = 0;
    if (1 != 0) goto loc_0029D02D;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(v_stack_mF0, Arg2, Arg3, v_stack_mF0);
loc_0029C864:
    v_stack_mD8 = 0;
    if (v_stack_mE8 != 0) goto loc_0029CEF0;
    if (((uint32_t)((int32_t)(Arg5))) != 14) goto loc_0029CED8;
    if (((uint32_t)((uint32_t)(Arg4))) < 8) goto loc_0029CE50;
    v_stack_m50 = *(uint64_t *)(v_stack_p18);
    goto loc_0029C8BE;
loc_0029C8BE:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x50)))) & (8)) != 0) goto loc_0029D229;
loc_0029C8CB:
    Arg1 = (*(uint64_t *)(v_stack_p18)) >> (32);
    if (sign_flag) goto loc_0029CA2B;
    *(uint64_t *)(v_stack_mF0 + 0x68) = *(uint64_t *)(v_stack_p18);
    *(uint32_t *)(v_stack_p10) = 0;
    *(uint64_t *)(v_stack_p10 + 0x8) = 0;
    goto loc_0029C916;
loc_0029C916:
    result = IopReleaseFileObjectLock(v_stack_mF0, v_stack_p18, Arg3, v_stack_mF0);
    local_rbx = (v_stack_mF0) + (-48);
    result = ((*(uint32_t *)(v_rip + 0xD286C3)) != 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) {
        Arg4 = 0x746C6644ULL;
        Arg3 = 1;
        Arg2 = 0;
        Arg1 = local_rbx;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_0029C9A2;
loc_0029C979:
loc_0029C97C:
    local_rsp = (local_rsp) + (240);
    return 0;
loc_0029C990:
    if (*(uint64_t *)(Arg1 + 0x8) != 0) goto loc_0029C7B0;
    goto loc_0029C79C;
loc_0029C9A2:
    if (*(uint64_t *)(local_rbx + 0x8) != 0) goto loc_0029CAC6;
    if (!sign_flag) goto loc_0029D15D;
    v_stack_p20 = 0;
    Arg2 = 0;
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_p38, *(uint64_t *)(local_rbx + 0x8) + 2);
loc_0029C9D1:
    if (((uint32_t)((uint32_t)(Arg5))) == 56) goto loc_0029CE83;
    if (((uint32_t)((uint32_t)(Arg5))) == 66) goto loc_0029D380;
    if (((uint32_t)((uint32_t)(Arg5))) == 57) goto loc_0029D2B4;
    if (((uint32_t)((uint32_t)(Arg5))) == 73) goto loc_0029D3A7;
    local_rdi = (uint32_t)(Arg5);
    if (((uint32_t)((uint32_t)(Arg5))) == 75) {
        local_rdi = 71;
        v_stack_p41 = 1;
    }
    goto loc_0029C75A;
loc_0029CA21:
    Arg1 = (uint32_t)((v_rip - 2738709) - 1);
    if ((((uint32_t)((int32_t)((uint32_t)(local_rdi)))) & ((uint32_t)(Arg1))) == 0) goto loc_0029C8CB;
loc_0029CA2B:
    goto loc_0029C916;
loc_0029CA42:
    v_stack_p48 = *(uint64_t *)(v_stack_p38);
    if (*(uint64_t *)(v_stack_p38) == 0) goto loc_0029C7D0;
loc_0029CA56:
    if (Arg1 == (*(uint64_t *)(v_stack_p38))) goto loc_0029CE46;
    if (*(uint64_t *)(Arg1 + 0x18) != 0) goto loc_0029CA56;
    goto loc_0029C7D0;
loc_0029CA6D:
    v_stack_pB8 = v_xmm0;
    v_stack_pC8 = v_xmm0;
    result = SeCaptureSubjectContextEx(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), v_stack_pB8, *(uint64_t *)(local_rbx + 0x8) + 2);
    result = RtlIsSandboxedToken(v_stack_pB8, (uint8_t)((uint32_t)(0xC000000DULL)), v_stack_pB8, *(uint64_t *)(local_rbx + 0x8) + 2);
    result = SeReleaseSubjectContext(v_stack_pB8, (uint8_t)((uint32_t)(0xC000000DULL)), v_stack_pB8, *(uint64_t *)(local_rbx + 0x8) + 2);
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0029C75A;
    goto loc_0029C75A;
loc_0029CAC6:
    result = ((uint8_t)(result)) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)((uint8_t)(result) + 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xD2A36E));
    v_stack_p20 = v_stack_pB8;
    result = KeBugCheckEx(24, *(uint64_t *)(v_rip - 0x29CA3D + Arg2 * 8 + 0xFC7800), v_stack_p38, 1);
loc_0029CB01:
    v_stack_p60 = 1;
    v_stack_p62 = 6;
    v_stack_p64 = 0;
    v_stack_p70 = v_stack_p68;
    v_stack_p68 = v_stack_p68;
    local_rsi = 0;
loc_0029CB29:
    v_stack_p31 = 0;
    result = IopResetEvent((uint8_t)(result), *(uint64_t *)(v_rip - 0x29CA3D + Arg2 * 8 + 0xFC7800), v_stack_p38, 1);
    if (1 == 36) goto loc_0029D24E;
    Arg3 = (uint8_t)((0) ^ (1));
    result = IopAllocateIrpExReturn(v_stack_p48, *(uint8_t *)(v_stack_p48 + 0x4C), Arg3, 1);
    v_stack_pB0 = result;
    if (result == 0) goto loc_0029D0BA;
    *(uint64_t *)(result + 0xC0) = (uint8_t)(result);
    *(uint64_t *)(result + 0x98) = v_stack_p78;
    *(uint8_t *)(result + 0x40) = (uint8_t)(v_stack_p30);
    if (v_stack_p31 != 0) goto loc_0029CE6F;
    if (((uint8_t)(v_stack_p30)) != 1) goto loc_0029CBBD;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78))) >> (6));
    Arg1 = (uint8_t)((Arg1) & (1));
    v_stack_p44 = (uint32_t)(Arg1);
    if (!(condition_is_equal)) {
    }
    v_stack_p33 = (uint8_t)(Arg1);
loc_0029CBBD:
    *(uint32_t *)(result + 0x10) = 4;
loc_0029CBD1:
    *(uint64_t *)(result + 0x50) = v_stack_p60;
    *(uint64_t *)(result + 0x48) = v_stack_pA0;
    *(uint64_t *)(result + 0x58) = 0;
    result = (*(uint64_t *)(result + 0xB8)) - (72);
    v_stack_p50 = result;
    *(uint8_t *)(result) = 6;
    *(uint64_t *)(result + 0x30) = v_stack_p38;
    *(uint64_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    result = ExAllocatePool2(97, (uint32_t)(Arg4), (uint32_t)(0x42536F49ULL), 1);
    v_stack_p78 = result;
    *(uint64_t *)(result + 0x18) = result;
    result = memcpy(result, v_stack_p140, (uint32_t)(Arg4), 1);
    if (((uint32_t)(1 - 19)) <= 1) goto loc_0029CC38;
    if (1 != 14) goto loc_0029CC4D;
loc_0029CC38:
    result = v_stack_p78;
    if ((*(uint32_t *)(v_stack_p78 + 0x4)) < 0) {
        Arg1 = 0xC000000DULL;
        result = RtlRaiseStatus(Arg1, v_stack_p140, (uint32_t)(Arg4), 1);
    }
    goto loc_0029CC8B;
loc_0029CC8B:
    *(uint32_t *)(v_stack_p50 + 0x8) = (uint32_t)((uint32_t)(Arg4));
    *(uint32_t *)(v_stack_p50 + 0x10) = 1;
    if (v_stack_p41 == 0) goto loc_0029CEE0;
loc_0029CCA9:
loc_0029CCAD:
    result = IopQueueThreadIrp(result, v_stack_p140, (uint32_t)(Arg4), 1);
    if (1 == 16) goto loc_0029D0CE;
    if (((uint32_t)(1 - 10)) > 62) goto loc_0029CCF2;
    if (((uint32_t)(1 - 10)) < 62) goto loc_0029CEB4;
loc_0029CCF2:
    if (1 == 40) goto loc_0029D417;
    if (1 == 13) goto loc_0029CF02;
    if (1 == 64) goto loc_0029CF02;
    if (1 == 30) goto loc_0029CF45;
    if (1 == 61) goto loc_0029D31A;
    if (1 == 41) goto loc_0029D1DD;
    if (1 == 42) goto loc_0029D4CD;
    if (1 == 43) goto loc_0029D3B6;
    if (1 == 69) goto loc_0029D4F1;
loc_0029CD43:
loc_0029CD48:
    v_stack_p20 = 2;
    result = IopCallDriverReference(v_stack_p48, result, (uint8_t)(v_stack_p31), v_stack_p38);
loc_0029CD69:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 259) goto loc_0029CE92;
    v_stack_p90 = 0;
    if ((uint8_t)(v_stack_p31) == 0) {
        *(uint64_t *)(result + 0x50) = 0;
    }
    *(uint64_t *)(result + 0x48) = v_stack_p138;
    if ((*(uint32_t *)(v_rip + 0xD29F74)) != 0) goto loc_0029CF35;
loc_0029CDB2:
    v_stack_p20 = v_stack_p90;
    result = IopCompleteRequest(result + 120, v_stack_pE0, v_stack_p90, v_stack_p38);
    if ((*(uint32_t *)(v_rip + 0xD29F3C)) != 0) {
        Arg1 = 1;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_p90, v_stack_p38);
    }
    result = (uint8_t)(v_cr8);
    if ((uint8_t)(v_stack_p31) != 0) {
        Arg1 = v_stack_p38;
        result = IopReleaseFileObjectLock(Arg1, Arg2, v_stack_p90, v_stack_p38);
    }
loc_0029CE0C:
    if ((uint8_t)((uint32_t)(v_stack_p44)) == 0) goto loc_0029CE29;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78))) >> (6));
    if ((((uint8_t)(result)) & (1)) == 0) {
    }
    if (v_stack_p98 == 0) goto loc_0029C979;
    Arg2 = 0;
    result = ObCloseHandle(v_stack_p98, Arg2, v_stack_p90, v_stack_p38);
    goto loc_0029C979;
loc_0029CE46:
    goto loc_0029C7F6;
loc_0029CE50:
    result = IopReleaseFileObjectLock(v_stack_p38, Arg2, v_stack_p90, v_stack_p38);
    result = ObfDereferenceObjectWithTag(v_stack_p38, (uint32_t)(0x746C6644ULL), v_stack_p90, v_stack_p38);
loc_0029CE65:
    goto loc_0029C97C;
loc_0029CE6F:
    goto loc_0029CBD1;
loc_0029CE83:
    v_stack_p32 = 1;
    goto loc_0029CA0B;
loc_0029CE92:
    if (10 == 0) goto loc_0029D05F;
    result = IopWaitForSynchronousIo(result, v_stack_p38, (uint8_t)(v_stack_p138), v_stack_p38);
    goto loc_0029CDFE;
loc_0029CEB4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x18) + 0x10))) != 0) goto loc_0029D0ED;
loc_0029CEC4:
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_0029CD69;
loc_0029CED8:
    goto loc_0029CB29;
loc_0029CEE0:
    if (v_stack_p32 != 0) goto loc_0029CCA9;
    goto loc_0029CCAD;
loc_0029CEF0:
    result = ObfDereferenceObjectWithTag(v_stack_p38, (uint32_t)(0x746C6644ULL), *(uint64_t *)(result + 0x18), v_stack_p38);
    goto loc_0029C979;
loc_0029CF02:
    if (((uint32_t)(v_stack_p31)) == 64) goto loc_0029D058;
loc_0029CF12:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(1 + 0x18))) == 0) goto loc_0029CD43;
    *(uint64_t *)(v_stack_p38 + 0x20) = v_stack_p130;
    goto loc_0029CD43;
loc_0029CF2B:
    goto loc_0029C97C;
loc_0029CF35:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p38), (uint8_t)((uint32_t)(0xC0000003ULL)), *(uint64_t *)(result + 0x18), v_stack_p38);
    goto loc_0029CDB2;
loc_0029CF45:
    if ((*(uint64_t *)(v_stack_p38 + 0xB0)) != 0) goto loc_0029D0E2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x50)))) & (2)) != 0) goto loc_0029D0E2;
    v_stack_p58 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p58;
    result = ObReferenceObjectByHandle(*(uint64_t *)(*(uint64_t *)(1 + 0x18)), 2, *(uint64_t *)(v_rip + 0xD29D51), v_stack_p30);
    if (sign_flag) goto loc_0029D009;
    result = ExAllocatePool2(24 + 40, 24, (uint32_t)(0x63436F49ULL), v_stack_p30);
    if (result == 0) goto loc_0029D27A;
    local_r13 = (v_stack_p38) + (184);
    result = KeAcquireSpinLockRaiseToDpc(local_r13, 24, (uint32_t)(0x63436F49ULL), v_stack_p30);
    if ((*(uint64_t *)(v_stack_p38 + 0xB0)) != 0) goto loc_0029D494;
    *(uint64_t *)(result) = v_stack_p58;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(*(uint64_t *)(1 + 0x18) + 0x8);
    *(uint64_t *)(v_stack_p38 + 0xB0) = result;
    result = KeReleaseSpinLock(local_r13, (uint8_t)(result), (uint32_t)(0x63436F49ULL), v_stack_p30);
loc_0029D009:
    *(uint32_t *)(1 + 0x30) = 0;
    *(uint64_t *)(1 + 0x38) = 0;
    goto loc_0029CD69;
loc_0029D01B:
    if (*(uint64_t *)(local_r13 + 0x8) != 0) goto loc_0029C7B0;
    goto loc_0029C7AD;
loc_0029D02D:
    v_stack_p20 = v_stack_p40;
    result = IopWaitAndAcquireFileObjectLock(v_stack_p38, v_stack_p30, 1, result);
    goto loc_0029C864;
loc_0029D058:
    result = (uint8_t)((result) & (1));
    goto loc_0029CF12;
loc_0029D05F:
    v_stack_p20 = 0;
    Arg4 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_stack_p60, Arg2, 1, Arg4);
    if (((uint32_t)(result)) == 257) goto loc_0029D509;
    if (((uint32_t)(result)) == 192) goto loc_0029D509;
loc_0029D089:
    *(uint64_t *)(v_stack_p138) = v_xmm0;
    goto loc_0029CE0C;
loc_0029D0BA:
    Arg2 = 0;
    result = IopAllocateIrpCleanup(v_stack_p38, Arg2, 1, Arg4);
    goto loc_0029C97C;
loc_0029D0CE:
loc_0029D0E2:
    goto loc_0029D009;
loc_0029D0ED:
    if ((((uint8_t)(v_stack_p38)) & (1)) != 0) goto loc_0029CEC4;
    if (((uint32_t)(local_r13 - 20)) < ((uint32_t)(v_stack_p38))) goto loc_0029CEC4;
    if (((uint32_t)(v_stack_p31)) == 31) goto loc_0029D2C3;
    if (((uint32_t)(v_stack_p31)) == 65) goto loc_0029D243;
    if (((uint32_t)(v_stack_p31)) == 72) goto loc_0029D243;
loc_0029D121:
    *(uint8_t *)(v_stack_p38 + 0x20) = (uint8_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18)))));
loc_0029D124:
    if ((*(uint16_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))) + 0x14)) != 92) goto loc_0029D484;
loc_0029D130:
    result = IopOpenLinkOrRenameTarget(v_stack_p98, 1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))), v_stack_p38);
    if (!sign_flag) goto loc_0029CD48;
    *(uint32_t *)(1 + 0x30) = (uint32_t)(result);
    goto loc_0029CD69;
loc_0029D15D:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_0029D451;
    result = KeAreInterruptsEnabled(v_stack_p98, 1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))), v_stack_p38);
    if ((uint8_t)(result) == 0) goto loc_0029D451;
    if (((uint8_t)((uint8_t)(v_cr8))) >= 1) goto loc_0029D451;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p38 + 0x1A))) & (64)) != 0) goto loc_0029D1BC;
loc_0029D195:
    local_r14 = ((*(uint32_t *)(v_rip + 0xD27E74)) != 0) ? 1 : 0;
    result = *(uint8_t *)(v_stack_p38 + 0x1A);
    if ((uint32_t)(local_r14) != 0) {
        Arg1 = v_stack_p38;
        result = ObpDeregisterObject(Arg1, 1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))), v_stack_p38);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p38, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))), v_stack_p38);
    goto loc_0029C979;
loc_0029D1BC:
    result = (uint32_t)((result) & (127));
    Arg1 = (v_stack_p38) - (*(uint8_t *)(result + 0x1 * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(Arg1) + 0x18)) == 0) goto loc_0029D195;
    result = ObpHandleRevocationBlockRemoveObject(*(uint64_t *)(Arg1), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))), v_stack_p38);
    goto loc_0029D195;
loc_0029D1DD:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x50)))) & (2)) != 0) goto loc_0029D38F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))))) & (1)) != 0) {
        *(uint32_t *)(v_stack_mF0 + 0x50) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x50)));
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))))) & (2)) != 0) {
        *(uint32_t *)(v_stack_mF0 + 0x50) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0x50)));
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))))) & (4)) != 0) goto loc_0029D4C0;
loc_0029D217:
    *(uint32_t *)(1 + 0x30) = (uint32_t)((uint32_t)((uint32_t)(local_r14)));
    *(uint64_t *)(1 + 0x38) = local_r14;
    goto loc_0029CD69;
loc_0029D229:
    if ((uint16_t)(*(uint16_t *)(v_stack_p48 + 0x130)) == 0) goto loc_0029C8CB;
    goto loc_0029CA21;
loc_0029D243:
    result = (uint8_t)((*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))))) & (1));
    goto loc_0029D121;
loc_0029D24E:
    if (((uint32_t)(local_r13)) >= 16) goto loc_0029D2CE;
loc_0029D259:
    if (1 != 0) {
        Arg1 = v_stack_p38;
        result = IopReleaseFileObjectLock(Arg1, *(uint64_t *)(1 + 0x18), (uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))), v_stack_p38);
    }
    result = ObfDereferenceObjectWithTag(v_stack_p38, (uint32_t)(0x746C6644ULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))), v_stack_p38);
    goto loc_0029C97C;
loc_0029D27A:
    result = ObfDereferenceObjectWithTag(v_stack_p58, (uint32_t)(0x746C6644ULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))), v_stack_p38);
    *(uint32_t *)(1 + 0x30) = (uint32_t)((uint32_t)(0xC000009AULL));
    *(uint64_t *)(1 + 0x38) = local_r14;
    goto loc_0029CD69;
loc_0029D2A1:
    result = IoGetAttachedDevice(*(uint64_t *)(v_stack_p38 + 0x8), (uint32_t)(0x746C6644ULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))), v_stack_p38);
    v_stack_p48 = result;
    goto loc_0029C7F6;
loc_0029D2B4:
    v_stack_p32 = 1;
    goto loc_0029CA0B;
loc_0029D2C3:
    *(uint32_t *)(v_stack_p38 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))))));
    goto loc_0029D124;
loc_0029D2CE:
    if (1 == 0) goto loc_0029D40D;
loc_0029D2DE:
    v_stack_p28 = (uint8_t)(v_stack_p30);
    v_stack_p20 = v_stack_p38 + 152;
    result = IopTrackLink(v_stack_p38, v_stack_pA0, v_stack_p140, (uint32_t)((uint32_t)(local_r13)));
    v_stack_p50 = (uint32_t)(result);
    if (sign_flag) goto loc_0029D259;
    goto loc_0029D45E;
loc_0029D31A:
    if ((*(uint64_t *)(v_stack_p38 + 0xB0)) == local_r14) goto loc_0029D0E2;
    v_stack_p80 = local_r14;
    v_stack_p28 = local_r14;
    v_stack_p20 = v_stack_p80;
    result = ObReferenceObjectByHandle(*(uint64_t *)(*(uint64_t *)(1 + 0x18)), 2, *(uint64_t *)(v_rip + 0xD2997A), v_stack_p30);
loc_0029D380:
    v_stack_p32 = 1;
    goto loc_0029CA0B;
loc_0029D38F:
    *(uint32_t *)(1 + 0x30) = (uint32_t)((uint32_t)(0xC000000DULL));
    *(uint64_t *)(1 + 0x38) = local_r14;
    goto loc_0029CD69;
loc_0029D3A7:
    v_stack_p32 = 1;
    goto loc_0029CA0B;
loc_0029D3B6:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))))) > 2) goto loc_0029D0E2;
    v_stack_p88 = local_r14;
    Arg3 = 0;
    result = IopAllocateFileObjectExtension(v_stack_p38, v_stack_p88, Arg3, v_stack_p30);
    if (sign_flag) goto loc_0029D009;
    *(uint32_t *)(v_stack_p88 + 0x58) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))) + 1);
    *(uint32_t *)(1 + 0x30) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(1 + 0x38) = local_r14;
    goto loc_0029CD69;
loc_0029D40D:
    goto loc_0029D2DE;
loc_0029D417:
    if (((uint32_t)(local_r13 - 4)) >= (*(uint32_t *)(*(uint64_t *)(1 + 0x18)))) goto loc_0029D437;
    *(uint32_t *)(1 + 0x30) = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_0029CD69;
loc_0029D437:
    if ((*(uint16_t *)(*(uint64_t *)(1 + 0x18) + 0x4)) != 92) goto loc_0029CD48;
    *(uint32_t *)(1 + 0x30) = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_0029CD69;
loc_0029D451:
    result = ObpDeferObjectDeletion((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))) + 1, v_stack_p88, Arg3, v_stack_p30);
    goto loc_0029C979;
loc_0029D45E:
    *(uint64_t *)(v_stack_p138 + 0x8) = local_r14;
    *(uint32_t *)(v_stack_p138) = (uint32_t)(v_stack_p31);
    goto loc_0029D259;
loc_0029D484:
    if ((*(uint64_t *)(Arg3 + 0x8)) == 0) goto loc_0029CD43;
    goto loc_0029D130;
loc_0029D494:
    result = KeReleaseSpinLock((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x18))) + 1, (uint8_t)(v_stack_p138), Arg3, v_stack_p30);
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)(0xC000000DULL), Arg2, Arg3, v_stack_p30);
    result = ObfDereferenceObjectWithTag(v_stack_p58, (uint32_t)(0x746C6644ULL), Arg3, v_stack_p30);
    goto loc_0029D009;
loc_0029D4C0:
    *(uint32_t *)(v_stack_mF0 + 0x50) = (uint32_t)(v_stack_p58);
    goto loc_0029D217;
loc_0029D4CD:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0xD3C5F7), v_stack_p30, Arg3, v_stack_p30);
loc_0029D4F1:
loc_0029D509:
    result = IopCancelAlertedRequest(v_stack_p60, 1, Arg3, v_stack_p30);
    goto loc_0029D089;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0029C5E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
