# PipProcessDevNodeTree

- RVA: `0x008F9068`–`0x008F9901` (길이 `2,201` bytes)
- VA: `0x00000001408F9068`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00087C2C`
- 디코드: `543`개 명령, `2,201/2,201` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **49**; 고유 호출 대상: **33**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x008F90CF` → [PiCollapseEnumRequests](../../text/4E/PiCollapseEnumRequests_function_004E8890.md) (function, `0x004E8890`)
- `0x008F9125` → [PnpProcessAssignResources](../A2/PnpProcessAssignResources_function_00A2A950.md) (function, `0x00A2A950`)
- `0x008F91A8` → [PnpCheckForActiveDependencies](../A0/PnpCheckForActiveDependencies_function_00A06DA4.md) (function, `0x00A06DA4`)
- `0x008F9232` → [PnpDeviceCompletionQueueIsEmpty](../../text/48/PnpDeviceCompletionQueueIsEmpty_function_0048A070.md) (function, `0x0048A070`)
- `0x008F9266` → [PnpDeviceCompletionQueueIsEmpty](../../text/48/PnpDeviceCompletionQueueIsEmpty_function_0048A070.md) (function, `0x0048A070`)
- `0x008F9305` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008F933A` → [PpDevCfgTraceDeviceStart](PpDevCfgTraceDeviceStart_function_008F9908.md) (function, `0x008F9908`)
- `0x008F93B7` → [PoFxIdleDevice](../../text/48/PoFxIdleDevice_function_00483EE8.md) (function, `0x00483EE8`)
- `0x008F93C7` → [PipEnumerateCompleted](PipEnumerateCompleted_function_008F7B1C.md) (function, `0x008F7B1C`)
- `0x008F93F5` → [PnpDeviceCompletionQueueIsEmpty](../../text/48/PnpDeviceCompletionQueueIsEmpty_function_0048A070.md) (function, `0x0048A070`)
- `0x008F9430` → [PipProcessDevNodeTree](PipProcessDevNodeTree_function_008F9068.md) (function, `0x008F9068`)
- `0x008F943E` → [IopAllocateUnicodeString](../95/IopAllocateUnicodeString_function_00951F0C.md) (function, `0x00951F0C`)
- `0x008F9455` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (function, `0x003FEF30`)
- `0x008F945E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008F946A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008F9476` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008F947B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008F9480` → [PnpSynchronizeDeviceEventQueue](../AA/PnpSynchronizeDeviceEventQueue_function_00AA4F60.md) (function, `0x00AA4F60`)
- `0x008F94A4` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x008F94B2` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008F94C0` → [PnpDeviceObjectFromDeviceInstanceWithTag](../8E/PnpDeviceObjectFromDeviceInstanceWithTag_function_008E7490.md) (function, `0x008E7490`)
- `0x008F94D1` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008F951C` → [PipEnumerateDevice](PipEnumerateDevice_function_008F99E4.md) (function, `0x008F99E4`)
- `0x008F955B` → [PipCallDriverAddDevice](../A2/PipCallDriverAddDevice_function_00A272E0.md) (function, `0x00A272E0`)
- `0x008F95CC` → [PnpDeviceCompletionQueueGetCompletedRequest](../../text/4B/PnpDeviceCompletionQueueGetCompletedRequest_function_004BE224.md) (function, `0x004BE224`)
- `0x008F95D4` → [PnpDeviceCompletionProcessCompletedRequest](PnpDeviceCompletionProcessCompletedRequest_function_008FB654.md) (function, `0x008FB654`)
- `0x008F95E7` → [PnpDeviceCompletionQueueIsEmpty](../../text/48/PnpDeviceCompletionQueueIsEmpty_function_0048A070.md) (function, `0x0048A070`)
- `0x008F9652` → [PnpCheckForActiveDependencies](../A0/PnpCheckForActiveDependencies_function_00A06DA4.md) (function, `0x00A06DA4`)
- `0x008F9666` → [PiProcessNewDeviceNodeAsync](../A2/PiProcessNewDeviceNodeAsync_function_00A28EA8.md) (function, `0x00A28EA8`)
- `0x008F9698` → [PnpPoFxActivateDevice](PnpPoFxActivateDevice_function_008FB29C.md) (function, `0x008FB29C`)
- `0x008F96A8` → [PipProcessStartPhase1](PipProcessStartPhase1_function_008FE1F8.md) (function, `0x008FE1F8`)
- `0x008F96C2` → [PoFxPrepareDevice](../../text/49/PoFxPrepareDevice_function_00499F0C.md) (function, `0x00499F0C`)
- `0x008F96D5` → [PipProcessStartPhase2](../94/PipProcessStartPhase2_function_0094EE60.md) (function, `0x0094EE60`)
- `0x008F96F4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008F9714` → [PipProcessStartPhase3](PipProcessStartPhase3_function_008FBAF8.md) (function, `0x008FBAF8`)
- `0x008F9754` → [PnpDeviceCompletionQueueGetCompletedRequest](../../text/4B/PnpDeviceCompletionQueueGetCompletedRequest_function_004BE224.md) (function, `0x004BE224`)
- `0x008F975C` → [PnpDeviceCompletionProcessCompletedRequest](PnpDeviceCompletionProcessCompletedRequest_function_008FB654.md) (function, `0x008FB654`)
- `0x008F9761` → [PnpDeviceCompletionQueueIsEmpty](../../text/48/PnpDeviceCompletionQueueIsEmpty_function_0048A070.md) (function, `0x0048A070`)
- `0x008F9790` → [PnpDeviceCompletionQueueGetCompletedRequest](../../text/4B/PnpDeviceCompletionQueueGetCompletedRequest_function_004BE224.md) (function, `0x004BE224`)
- `0x008F9798` → [PnpDeviceCompletionProcessCompletedRequest](PnpDeviceCompletionProcessCompletedRequest_function_008FB654.md) (function, `0x008FB654`)
- `0x008F97AF` → [PnpDeviceCompletionQueueIsEmpty](../../text/48/PnpDeviceCompletionQueueIsEmpty_function_0048A070.md) (function, `0x0048A070`)
- `0x008F97C8` → [McTemplateK0z_EtwWriteTransfer](../../text/4D/McTemplateK0z_EtwWriteTransfer_function_004DEF6C.md) (function, `0x004DEF6C`)
- `0x008F97DD` → [McTemplateK0z_EtwWriteTransfer](../../text/4D/McTemplateK0z_EtwWriteTransfer_function_004DEF6C.md) (function, `0x004DEF6C`)
- `0x008F9807` → [PipProcessDevNodeTree](PipProcessDevNodeTree_function_008F9068.md) (function, `0x008F9068`)
- `0x008F9835` → [PipSetDevNodeProblem](PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x008F9842` → [PipProcessRestartPhase2](../74/PipProcessRestartPhase2_function_007408B8.md) (function, `0x007408B8`)
- `0x008F9857` → [PipProcessRestartPhase1](../74/PipProcessRestartPhase1_function_007407EC.md) (function, `0x007407EC`)
- `0x008F9892` → [PipSetDevNodeProblem](PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x008F98E6` → [PnpDeviceCompletionProcessCompletedRequests](PnpDeviceCompletionProcessCompletedRequests_function_008FC0D0.md) (function, `0x008FC0D0`)

### Direct callers
- [PnpProcessRebalance](../../text/5A/PnpProcessRebalance_function_005AA7C8.md) at `0x005AA8D6`
- [sub_006F45AA](../../text/6F/Unknown_function_006F45AA.md) at `0x006F45F8`
- [PiProcessResourceRequirementsChanged](../72/PiProcessResourceRequirementsChanged_function_0072D504.md) at `0x0072D607`
- [PiProcessStartSystemDevices](../72/PiProcessStartSystemDevices_function_0072D7D4.md) at `0x0072D82F`
- [PipProcessDevNodeTree](PipProcessDevNodeTree_function_008F9068.md) at `0x008F9430`
- [PipProcessDevNodeTree](PipProcessDevNodeTree_function_008F9068.md) at `0x008F9807`
- [PiProcessReenumeration](../A5/PiProcessReenumeration_function_00A51818.md) at `0x00A518B2`
- [PiRestartDevice](../AC/PiRestartDevice_function_00ACFA1C.md) at `0x00ACFAD5`

### Static image references
- `0x008F90D4` → RVA `0x00F8C438` (`.data`; read)
- `0x008F910A` → RVA `0x00EF012B` (`.data`; read)
- `0x008F9344` → RVA `0x00E0AA18` (`.data`; read)
- `0x008F9463` → RVA `0x00F8C560` (`.data`; read)
- `0x008F946F` → RVA `0x00F8C4E0` (`.data`; read)
- `0x008F95C3` → RVA `0x00F8C32C` (`.data`; read)
- `0x008F97C1` → RVA `0x00026D20` (`.rdata`; read)
- `0x008F97D6` → RVA `0x00026F50` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x008F90CF` → [PiCollapseEnumRequests](../../text/4E/PiCollapseEnumRequests_function_004E8890.md) (`PAGE` → `.text`)
  - `0x008F9232` → [PnpDeviceCompletionQueueIsEmpty](../../text/48/PnpDeviceCompletionQueueIsEmpty_function_0048A070.md) (`PAGE` → `.text`)
  - `0x008F9266` → [PnpDeviceCompletionQueueIsEmpty](../../text/48/PnpDeviceCompletionQueueIsEmpty_function_0048A070.md) (`PAGE` → `.text`)
  - `0x008F9305` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008F93B7` → [PoFxIdleDevice](../../text/48/PoFxIdleDevice_function_00483EE8.md) (`PAGE` → `.text`)
  - `0x008F93F5` → [PnpDeviceCompletionQueueIsEmpty](../../text/48/PnpDeviceCompletionQueueIsEmpty_function_0048A070.md) (`PAGE` → `.text`)
  - `0x008F9455` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (`PAGE` → `.text`)
  - `0x008F945E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008F946A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008F9476` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008F947B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008F94A4` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x008F94B2` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008F94D1` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008F95CC` → [PnpDeviceCompletionQueueGetCompletedRequest](../../text/4B/PnpDeviceCompletionQueueGetCompletedRequest_function_004BE224.md) (`PAGE` → `.text`)
  - `0x008F95E7` → [PnpDeviceCompletionQueueIsEmpty](../../text/48/PnpDeviceCompletionQueueIsEmpty_function_0048A070.md) (`PAGE` → `.text`)
  - `0x008F96C2` → [PoFxPrepareDevice](../../text/49/PoFxPrepareDevice_function_00499F0C.md) (`PAGE` → `.text`)
  - `0x008F96F4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008F9754` → [PnpDeviceCompletionQueueGetCompletedRequest](../../text/4B/PnpDeviceCompletionQueueGetCompletedRequest_function_004BE224.md) (`PAGE` → `.text`)
  - `0x008F9761` → [PnpDeviceCompletionQueueIsEmpty](../../text/48/PnpDeviceCompletionQueueIsEmpty_function_0048A070.md) (`PAGE` → `.text`)
  - `0x008F9790` → [PnpDeviceCompletionQueueGetCompletedRequest](../../text/4B/PnpDeviceCompletionQueueGetCompletedRequest_function_004BE224.md) (`PAGE` → `.text`)
  - `0x008F97AF` → [PnpDeviceCompletionQueueIsEmpty](../../text/48/PnpDeviceCompletionQueueIsEmpty_function_0048A070.md) (`PAGE` → `.text`)
  - `0x008F97C8` → [McTemplateK0z_EtwWriteTransfer](../../text/4D/McTemplateK0z_EtwWriteTransfer_function_004DEF6C.md) (`PAGE` → `.text`)
  - `0x008F97DD` → [McTemplateK0z_EtwWriteTransfer](../../text/4D/McTemplateK0z_EtwWriteTransfer_function_004DEF6C.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008F9618` → [sub_00B1F212](../B1/Unknown_function_00B1F212.md) (`tail-transfer`)
  - `0x008F9626` → [sub_00B1F212](../B1/Unknown_function_00B1F212.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008F9068  48 8B C4                        mov rax, rsp
008F906B  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
008F906F  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
008F9073  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
008F9077  48 89 48 08                     mov qword ptr [rax + 8], rcx
008F907B  55                              push rbp
008F907C  53                              push rbx
008F907D  56                              push rsi
008F907E  57                              push rdi
008F907F  41 54                           push r12
008F9081  41 55                           push r13
008F9083  41 56                           push r14
008F9085  41 57                           push r15
008F9087  48 8D 68 B9                     lea rbp, [rax - 0x47]
008F908B  48 81 EC 88 00 00 00            sub rsp, 0x88
008F9092  44 8A 65 7F                     mov r12b, byte ptr [rbp + 0x7f]
008F9096  0F 57 C0                        xorps xmm0, xmm0
008F9099  C6 45 C1 00                     mov byte ptr [rbp - 0x3f], 0
008F909D  41 8B F1                        mov esi, r9d
008F90A0  48 89 4D D7                     mov qword ptr [rbp - 0x29], rcx
008F90A4  48 8B FA                        mov rdi, rdx
008F90A7  4C 8B E9                        mov r13, rcx
008F90AA  4C 8B F1                        mov r14, rcx
008F90AD  41 B8 01 00 00 00               mov r8d, 1
008F90B3  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
008F90B7  48 85 D2                        test rdx, rdx
008F90BA  74 2F                           je 0x1408f90eb
008F90BC  80 7A 1C 00                     cmp byte ptr [rdx + 0x1c], 0
008F90C0  75 29                           jne 0x1408f90eb
008F90C2  45 3B C8                        cmp r9d, r8d
008F90C5  74 24                           je 0x1408f90eb
008F90C7  45 84 E4                        test r12b, r12b
008F90CA  75 1F                           jne 0x1408f90eb
008F90CC  48 8B CA                        mov rcx, rdx
008F90CF  E8 BC F7 BE FF                  call 0x1404e8890
008F90D4  48 8B 0D 5D 33 69 00            mov rcx, qword ptr [rip + 0x69335d]
008F90DB  84 C0                           test al, al
008F90DD  41 B8 01 00 00 00               mov r8d, 1
008F90E3  4C 0F 45 E9                     cmovne r13, rcx
008F90E7  4C 89 6D 4F                     mov qword ptr [rbp + 0x4f], r13
008F90EB  33 C0                           xor eax, eax
008F90ED  32 C9                           xor cl, cl
008F90EF  89 45 DF                        mov dword ptr [rbp - 0x21], eax
008F90F2  45 32 FF                        xor r15b, r15b
008F90F5  88 45 C2                        mov byte ptr [rbp - 0x3e], al
008F90F8  41 8A C0                        mov al, r8b
008F90FB  88 45 BF                        mov byte ptr [rbp - 0x41], al
008F90FE  89 4D CB                        mov dword ptr [rbp - 0x35], ecx
008F9101  44 89 7D C7                     mov dword ptr [rbp - 0x39], r15d
008F9105  45 84 E4                        test r12b, r12b
008F9108  75 46                           jne 0x1408f9150
008F910A  F6 05 1A 70 5F 00 10            test byte ptr [rip + 0x5f701a], 0x10
008F9111  0F 85 A6 06 00 00               jne 0x1408f97bd
008F9117  8A 55 6F                        mov dl, byte ptr [rbp + 0x6f]
008F911A  4C 8D 45 C0                     lea r8, [rbp - 0x40]
008F911E  49 8B CD                        mov rcx, r13
008F9121  C6 45 C0 00                     mov byte ptr [rbp - 0x40], 0
008F9125  E8 26 18 13 00                  call 0x140a2a950
008F912A  F6 05 FA 6F 5F 00 10            test byte ptr [rip + 0x5f6ffa], 0x10
008F9131  88 45 C2                        mov byte ptr [rbp - 0x3e], al
008F9134  0F 85 98 06 00 00               jne 0x1408f97d2
008F913A  80 7D C0 00                     cmp byte ptr [rbp - 0x40], 0
008F913E  0F 85 A3 06 00 00               jne 0x1408f97e7
008F9144  8B 4D CB                        mov ecx, dword ptr [rbp - 0x35]
008F9147  41 B8 01 00 00 00               mov r8d, 1
008F914D  8A 45 BF                        mov al, byte ptr [rbp - 0x41]
008F9150  49 8B DD                        mov rbx, r13
008F9153  C6 45 C0 00                     mov byte ptr [rbp - 0x40], 0
008F9157  48 89 5D CF                     mov qword ptr [rbp - 0x31], rbx
008F915B  44 88 45 C3                     mov byte ptr [rbp - 0x3d], r8b
008F915F  41 8B F0                        mov esi, r8d
008F9162  84 C9                           test cl, cl
008F9164  0F 85 83 02 00 00               jne 0x1408f93ed
008F916A  84 C0                           test al, al
008F916C  74 16                           je 0x1408f9184
008F916E  8B 83 C0 02 00 00               mov eax, dword ptr [rbx + 0x2c0]
008F9174  0F BA E0 10                     bt eax, 0x10
008F9178  73 0A                           jae 0x1408f9184
008F917A  0F BA F0 10                     btr eax, 0x10
008F917E  89 83 C0 02 00 00               mov dword ptr [rbx + 0x2c0], eax
008F9184  8B 83 2C 01 00 00               mov eax, dword ptr [rbx + 0x12c]
008F918A  2D 01 03 00 00                  sub eax, 0x301
008F918F  41 3B C0                        cmp eax, r8d
008F9192  76 27                           jbe 0x1408f91bb
008F9194  F7 83 8C 01 00 00 00 60 00 00   test dword ptr [rbx + 0x18c], 0x6000
008F919E  75 1B                           jne 0x1408f91bb
008F91A0  BA 02 00 00 00                  mov edx, 2
008F91A5  48 8B CB                        mov rcx, rbx
008F91A8  E8 F7 DB 10 00                  call 0x140a06da4
008F91AD  84 C0                           test al, al
008F91AF  0F 85 76 06 00 00               jne 0x1408f982b
008F91B5  41 B8 01 00 00 00               mov r8d, 1
008F91BB  8B 93 8C 01 00 00               mov edx, dword ptr [rbx + 0x18c]
008F91C1  F7 C2 00 60 00 00               test edx, 0x6000
008F91C7  0F 85 CC 00 00 00               jne 0x1408f9299
008F91CD  8B 8B 2C 01 00 00               mov ecx, dword ptr [rbx + 0x12c]
008F91D3  81 E9 01 03 00 00               sub ecx, 0x301
008F91D9  0F 84 5A 04 00 00               je 0x1408f9639
008F91DF  83 E9 03                        sub ecx, 3
008F91E2  0F 84 53 03 00 00               je 0x1408f953b
008F91E8  83 E9 02                        sub ecx, 2
008F91EB  0F 84 96 04 00 00               je 0x1408f9687
008F91F1  83 E9 02                        sub ecx, 2
008F91F4  0F 84 D8 04 00 00               je 0x1408f96d2
008F91FA  83 E9 01                        sub ecx, 1
008F91FD  0F 84 FD 04 00 00               je 0x1408f9700
008F9203  83 E9 01                        sub ecx, 1
008F9206  0F 85 80 01 00 00               jne 0x1408f938c
008F920C  44 39 45 67                     cmp dword ptr [rbp + 0x67], r8d
008F9210  0F 84 15 04 00 00               je 0x1408f962b
008F9216  BE 02 00 00 00                  mov esi, 2
008F921B  45 84 E4                        test r12b, r12b
008F921E  75 09                           jne 0x1408f9229
008F9220  F6 C2 08                        test dl, 8
008F9223  0F 85 E8 02 00 00               jne 0x1408f9511
008F9229  C6 45 C1 00                     mov byte ptr [rbp - 0x3f], 0
008F922D  33 FF                           xor edi, edi
008F922F  45 32 F6                        xor r14b, r14b
008F9232  E8 39 0E B9 FF                  call 0x14048a070
008F9237  85 C0                           test eax, eax
008F9239  0F 84 78 03 00 00               je 0x1408f95b7
008F923F  B8 CE 02 00 C0                  mov eax, 0xc00002ce
008F9244  3B F8                           cmp edi, eax
008F9246  0F 84 6A 06 00 00               je 0x1408f98b6
008F924C  45 84 F6                        test r14b, r14b
008F924F  75 06                           jne 0x1408f9257
008F9251  44 38 75 C0                     cmp byte ptr [rbp - 0x40], r14b
008F9255  75 06                           jne 0x1408f925d
008F9257  4C 8B 75 D7                     mov r14, qword ptr [rbp - 0x29]
008F925B  EB 3C                           jmp 0x1408f9299
008F925D  C6 45 C1 00                     mov byte ptr [rbp - 0x3f], 0
008F9261  33 FF                           xor edi, edi
008F9263  45 32 F6                        xor r14b, r14b
008F9266  E8 05 0E B9 FF                  call 0x14048a070
008F926B  85 C0                           test eax, eax
008F926D  0F 84 FC 04 00 00               je 0x1408f976f
008F9273  41 F6 DE                        neg r14b
008F9276  C6 45 C0 00                     mov byte ptr [rbp - 0x40], 0
008F927A  41 BE CE 02 00 C0               mov r14d, 0xc00002ce
008F9280  1A C0                           sbb al, al
008F9282  22 45 C7                        and al, byte ptr [rbp - 0x39]
008F9285  44 8A F8                        mov r15b, al
008F9288  41 3B FE                        cmp edi, r14d
008F928B  4C 8B 75 D7                     mov r14, qword ptr [rbp - 0x29]
008F928F  44 89 7D C7                     mov dword ptr [rbp - 0x39], r15d
008F9293  0F 84 47 01 00 00               je 0x1408f93e0
008F9299  45 84 E4                        test r12b, r12b
008F929C  0F 84 80 00 00 00               je 0x1408f9322
008F92A2  B9 01 00 00 00                  mov ecx, 1
008F92A7  45 84 FF                        test r15b, r15b
008F92AA  0F 85 D2 00 00 00               jne 0x1408f9382
008F92B0  83 EE 01                        sub esi, 1
008F92B3  0F 84 99 00 00 00               je 0x1408f9352
008F92B9  83 FE 01                        cmp esi, 1
008F92BC  75 14                           jne 0x1408f92d2
008F92BE  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008F92C2  48 85 C0                        test rax, rax
008F92C5  0F 84 87 00 00 00               je 0x1408f9352
008F92CB  48 8B D8                        mov rbx, rax
008F92CE  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
008F92D2  8A 45 BF                        mov al, byte ptr [rbp - 0x41]
008F92D5  41 B8 01 00 00 00               mov r8d, 1
008F92DB  8B 75 67                        mov esi, dword ptr [rbp + 0x67]
008F92DE  80 7D C3 00                     cmp byte ptr [rbp - 0x3d], 0
008F92E2  48 8B 7D 57                     mov rdi, qword ptr [rbp + 0x57]
008F92E6  8B 4D CB                        mov ecx, dword ptr [rbp - 0x35]
008F92E9  0F 85 70 FE FF FF               jne 0x1408f915f
008F92EF  80 7D C2 00                     cmp byte ptr [rbp - 0x3e], 0
008F92F3  8A 45 BF                        mov al, byte ptr [rbp - 0x41]
008F92F6  0F 85 09 FE FF FF               jne 0x1408f9105
008F92FC  45 84 E4                        test r12b, r12b
008F92FF  75 09                           jne 0x1408f930a
008F9301  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
008F9305  E8 46 00 A0 FF                  call 0x1402f9350
008F930A  8B 45 DF                        mov eax, dword ptr [rbp - 0x21]
008F930D  48 81 C4 88 00 00 00            add rsp, 0x88
008F9314  41 5F                           pop r15
008F9316  41 5E                           pop r14
008F9318  41 5D                           pop r13
008F931A  41 5C                           pop r12
008F931C  5F                              pop rdi
008F931D  5E                              pop rsi
008F931E  5B                              pop rbx
008F931F  5D                              pop rbp
008F9320  C3                              ret
008F9321  CC                              int3
008F9322  8B 83 C0 02 00 00               mov eax, dword ptr [rbx + 0x2c0]
008F9328  B9 01 00 00 00                  mov ecx, 1
008F932D  84 C1                           test cl, al
008F932F  0F 84 72 FF FF FF               je 0x1408f92a7
008F9335  33 D2                           xor edx, edx
008F9337  48 8B CB                        mov rcx, rbx
008F933A  E8 C9 05 00 00                  call 0x1408f9908
008F933F  E9 5E FF FF FF                  jmp 0x1408f92a2
008F9344  8B 05 CE 16 51 00               mov eax, dword ptr [rip + 0x5116ce]
008F934A  85 C0                           test eax, eax
008F934C  0F 88 5E FF FF FF               js 0x1408f92b0
008F9352  49 3B DD                        cmp rbx, r13
008F9355  0F 84 31 02 00 00               je 0x1408f958c
008F935B  48 8B 03                        mov rax, qword ptr [rbx]
008F935E  48 85 C0                        test rax, rax
008F9361  0F 85 64 FF FF FF               jne 0x1408f92cb
008F9367  45 84 FF                        test r15b, r15b
008F936A  0F 85 8D 02 00 00               jne 0x1408f95fd
008F9370  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
008F9374  48 85 C0                        test rax, rax
008F9377  74 D9                           je 0x1408f9352
008F9379  48 8B D8                        mov rbx, rax
008F937C  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
008F9380  EB D0                           jmp 0x1408f9352
008F9382  85 F6                           test esi, esi
008F9384  0F 84 26 FF FF FF               je 0x1408f92b0
008F938A  EB B8                           jmp 0x1408f9344
008F938C  83 E9 02                        sub ecx, 2
008F938F  0F 84 B7 04 00 00               je 0x1408f984c
008F9395  83 E9 01                        sub ecx, 1
008F9398  0F 84 A1 04 00 00               je 0x1408f983f
008F939E  83 F9 02                        cmp ecx, 2
008F93A1  0F 85 82 FE FF FF               jne 0x1408f9229
008F93A7  F7 83 C0 02 00 00 00 02 00 00   test dword ptr [rbx + 0x2c0], 0x200
008F93B1  74 11                           je 0x1408f93c4
008F93B3  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
008F93B7  E8 2C AB B8 FF                  call 0x140483ee8
008F93BC  0F BA B3 C0 02 00 00 09         btr dword ptr [rbx + 0x2c0], 9
008F93C4  48 8B CB                        mov rcx, rbx
008F93C7  E8 50 E7 FF FF                  call 0x1408f7b1c
008F93CC  8B F8                           mov edi, eax
008F93CE  BE 02 00 00 00                  mov esi, 2
008F93D3  B8 CE 02 00 C0                  mov eax, 0xc00002ce
008F93D8  3B F8                           cmp edi, eax
008F93DA  0F 85 49 FE FF FF               jne 0x1408f9229
008F93E0  45 84 E4                        test r12b, r12b
008F93E3  0F 85 D6 04 00 00               jne 0x1408f98bf
008F93E9  48 8B 7D 57                     mov rdi, qword ptr [rbp + 0x57]
008F93ED  C6 45 CB 00                     mov byte ptr [rbp - 0x35], 0
008F93F1  C6 45 C1 00                     mov byte ptr [rbp - 0x3f], 0
008F93F5  E8 76 0C B9 FF                  call 0x14048a070
008F93FA  85 C0                           test eax, eax
008F93FC  0F 84 4A 03 00 00               je 0x1408f974c
008F9402  8A 45 77                        mov al, byte ptr [rbp + 0x77]
008F9405  45 32 FF                        xor r15b, r15b
008F9408  8B 75 67                        mov esi, dword ptr [rbp + 0x67]
008F940B  48 8B D7                        mov rdx, rdi
008F940E  4C 8B 45 5F                     mov r8, qword ptr [rbp + 0x5f]
008F9412  44 8B CE                        mov r9d, esi
008F9415  48 8B 0D 1C 30 69 00            mov rcx, qword ptr [rip + 0x69301c]
008F941C  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
008F9421  88 44 24 28                     mov byte ptr [rsp + 0x28], al
008F9425  8A 45 6F                        mov al, byte ptr [rbp + 0x6f]
008F9428  88 44 24 20                     mov byte ptr [rsp + 0x20], al
008F942C  44 89 7D C7                     mov dword ptr [rbp - 0x39], r15d
008F9430  E8 33 FC FF FF                  call 0x1408f9068
008F9435  41 0F B7 55 28                  movzx edx, word ptr [r13 + 0x28]
008F943A  48 8D 4D E7                     lea rcx, [rbp - 0x19]
008F943E  E8 C9 8A 05 00                  call 0x140951f0c
008F9443  8B D8                           mov ebx, eax
008F9445  85 C0                           test eax, eax
008F9447  0F 88 A3 02 00 00               js 0x1408f96f0
008F944D  49 8D 55 28                     lea rdx, [r13 + 0x28]
008F9451  48 8D 4D E7                     lea rcx, [rbp - 0x19]
008F9455  E8 D6 5A B0 FF                  call 0x1403fef30
008F945A  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
008F945E  E8 ED FE 9F FF                  call 0x1402f9350
008F9463  48 8D 0D F6 30 69 00            lea rcx, [rip + 0x6930f6]
008F946A  E8 A1 65 96 FF                  call 0x14025fa10
008F946F  48 8D 0D 6A 30 69 00            lea rcx, [rip + 0x69306a]
008F9476  E8 95 65 96 FF                  call 0x14025fa10
008F947B  E8 30 44 96 FF                  call 0x14025d8b0
008F9480  E8 DB BA 1A 00                  call 0x140aa4f60
008F9485  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008F948E  48 8D 0D 4B 30 69 00            lea rcx, [rip + 0x69304b]
008F9495  BB 01 00 00 00                  mov ebx, 1
008F949A  8A D3                           mov dl, bl
008F949C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008F94A3  90                              nop
008F94A4  E8 77 B9 91 FF                  call 0x140214e20
008F94A9  8A D3                           mov dl, bl
008F94AB  48 8D 0D AE 30 69 00            lea rcx, [rip + 0x6930ae]
008F94B2  E8 09 87 91 FF                  call 0x140211bc0
008F94B7  BA 44 66 6C 74                  mov edx, 0x746c6644
008F94BC  48 8D 4D E7                     lea rcx, [rbp - 0x19]
008F94C0  E8 CB DF FE FF                  call 0x1408e7490
008F94C5  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
008F94C9  48 8B D8                        mov rbx, rax
008F94CC  48 85 C9                        test rcx, rcx
008F94CF  74 0C                           je 0x1408f94dd
008F94D1  E8 7A 93 28 00                  call 0x140b82850
008F94D6  0F 57 C0                        xorps xmm0, xmm0
008F94D9  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
008F94DD  48 85 DB                        test rbx, rbx
008F94E0  0F 84 11 04 00 00               je 0x1408f98f7
008F94E6  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
008F94ED  41 B8 01 00 00 00               mov r8d, 1
008F94F3  4C 8B 68 28                     mov r13, qword ptr [rax + 0x28]
008F94F7  8A 45 BF                        mov al, byte ptr [rbp - 0x41]
008F94FA  49 8B DD                        mov rbx, r13
008F94FD  48 89 5D CF                     mov qword ptr [rbp - 0x31], rbx
008F9501  4D 8B F5                        mov r14, r13
008F9504  4C 89 6D 4F                     mov qword ptr [rbp + 0x4f], r13
008F9508  4C 89 6D D7                     mov qword ptr [rbp - 0x29], r13
008F950C  E9 CD FD FF FF                  jmp 0x1408f92de
008F9511  0F B6 55 77                     movzx edx, byte ptr [rbp + 0x77]
008F9515  48 8B CB                        mov rcx, rbx
008F9518  45 0F B6 C7                     movzx r8d, r15b
008F951C  E8 C3 04 00 00                  call 0x1408f99e4
008F9521  8B F0                           mov esi, eax
008F9523  8B F8                           mov edi, eax
008F9525  3D 03 01 00 00                  cmp eax, 0x103
008F952A  0F 84 EB 01 00 00               je 0x1408f971b
008F9530  C1 FE 1F                        sar esi, 0x1f
008F9533  83 E6 02                        and esi, 2
008F9536  E9 98 FE FF FF                  jmp 0x1408f93d3
008F953B  45 84 E4                        test r12b, r12b
008F953E  0F 85 E5 FC FF FF               jne 0x1408f9229
008F9544  F7 83 C0 02 00 00 00 00 01 00   test dword ptr [rbx + 0x2c0], 0x10000
008F954E  0F 85 D5 FC FF FF               jne 0x1408f9229
008F9554  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
008F9558  48 8B CB                        mov rcx, rbx
008F955B  E8 80 DD 12 00                  call 0x140a272e0
008F9560  8B F8                           mov edi, eax
008F9562  85 C0                           test eax, eax
008F9564  0F 89 53 01 00 00               jns 0x1408f96bd
008F956A  81 BB 2C 01 00 00 04 03 00 00   cmp dword ptr [rbx + 0x12c], 0x304
008F9574  B8 CE 02 00 C0                  mov eax, 0xc00002ce
008F9579  0F 85 59 FE FF FF               jne 0x1408f93d8
008F957F  0F BA AB C0 02 00 00 10         bts dword ptr [rbx + 0x2c0], 0x10
008F9587  E9 4C FE FF FF                  jmp 0x1408f93d8
008F958C  8B 05 86 14 51 00               mov eax, dword ptr [rip + 0x511486]
008F9592  A8 04                           test al, 4
008F9594  0F 85 2D 03 00 00               jne 0x1408f98c7
008F959A  45 84 FF                        test r15b, r15b
008F959D  75 04                           jne 0x1408f95a3
008F959F  C6 45 C3 00                     mov byte ptr [rbp - 0x3d], 0
008F95A3  41 B8 01 00 00 00               mov r8d, 1
008F95A9  32 C0                           xor al, al
008F95AB  44 88 45 C0                     mov byte ptr [rbp - 0x40], r8b
008F95AF  88 45 BF                        mov byte ptr [rbp - 0x41], al
008F95B2  E9 24 FD FF FF                  jmp 0x1408f92db
008F95B7  41 BD 01 00 00 00               mov r13d, 1
008F95BD  41 BC CE 02 00 C0               mov r12d, 0xc00002ce
008F95C3  83 3D 62 2D 69 00 00            cmp dword ptr [rip + 0x692d62], 0
008F95CA  74 24                           je 0x1408f95f0
008F95CC  E8 53 4C BC FF                  call 0x1404be224
008F95D1  48 8B C8                        mov rcx, rax
008F95D4  E8 7B 20 00 00                  call 0x1408fb654
008F95D9  41 3B C4                        cmp eax, r12d
008F95DC  44 88 6D C1                     mov byte ptr [rbp - 0x3f], r13b
008F95E0  45 8A F5                        mov r14b, r13b
008F95E3  41 0F 44 FC                     cmove edi, r12d
008F95E7  E8 84 0A B9 FF                  call 0x14048a070
008F95EC  85 C0                           test eax, eax
008F95EE  74 D3                           je 0x1408f95c3
008F95F0  4C 8B 6D 4F                     mov r13, qword ptr [rbp + 0x4f]
008F95F4  44 8A 65 7F                     mov r12b, byte ptr [rbp + 0x7f]
008F95F8  E9 42 FC FF FF                  jmp 0x1408f923f
008F95FD  8B 05 15 14 51 00               mov eax, dword ptr [rip + 0x511415]
008F9603  85 C0                           test eax, eax
008F9605  0F 84 65 FD FF FF               je 0x1408f9370
008F960B  0F 88 5F FD FF FF               js 0x1408f9370
008F9611  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
008F9615  48 85 C0                        test rax, rax
008F9618  0F 84 F4 5B 22 00               je 0x140b1f212
008F961E  48 8B 58 08                     mov rbx, qword ptr [rax + 8]
008F9622  48 89 5D CF                     mov qword ptr [rbp - 0x31], rbx
008F9626  E9 E7 5B 22 00                  jmp 0x140b1f212
008F962B  49 3B DD                        cmp rbx, r13
008F962E  0F 85 F5 FB FF FF               jne 0x1408f9229
008F9634  E9 DD FB FF FF                  jmp 0x1408f9216
008F9639  83 7D 67 03                     cmp dword ptr [rbp + 0x67], 3
008F963D  0F 84 EB 00 00 00               je 0x1408f972e
008F9643  45 84 E4                        test r12b, r12b
008F9646  0F 85 DD FB FF FF               jne 0x1408f9229
008F964C  41 8B D0                        mov edx, r8d
008F964F  48 8B CB                        mov rcx, rbx
008F9652  E8 4D D7 10 00                  call 0x140a06da4
008F9657  48 8B CB                        mov rcx, rbx
008F965A  84 C0                           test al, al
008F965C  0F 85 29 02 00 00               jne 0x1408f988b
008F9662  0F B6 55 77                     movzx edx, byte ptr [rbp + 0x77]
008F9666  E8 3D F8 12 00                  call 0x140a28ea8
008F966B  8B F8                           mov edi, eax
008F966D  3D 03 01 00 00                  cmp eax, 0x103
008F9672  0F 85 C5 00 00 00               jne 0x1408f973d
008F9678  41 BF 01 00 00 00               mov r15d, 1
008F967E  44 89 7D C7                     mov dword ptr [rbp - 0x39], r15d
008F9682  E9 A2 FB FF FF                  jmp 0x1408f9229
008F9687  45 84 E4                        test r12b, r12b
008F968A  0F 85 99 FB FF FF               jne 0x1408f9229
008F9690  BA 00 02 00 00                  mov edx, 0x200
008F9695  48 8B CB                        mov rcx, rbx
008F9698  E8 FF 1B 00 00                  call 0x1408fb29c
008F969D  0F B6 55 77                     movzx edx, byte ptr [rbp + 0x77]
008F96A1  48 8B CB                        mov rcx, rbx
008F96A4  45 0F B6 C7                     movzx r8d, r15b
008F96A8  E8 4B 4B 00 00                  call 0x1408fe1f8
008F96AD  8B F8                           mov edi, eax
008F96AF  3D 03 01 00 00                  cmp eax, 0x103
008F96B4  74 C2                           je 0x1408f9678
008F96B6  33 F6                           xor esi, esi
008F96B8  E9 16 FD FF FF                  jmp 0x1408f93d3
008F96BD  33 D2                           xor edx, edx
008F96BF  48 8B CB                        mov rcx, rbx
008F96C2  E8 45 08 BA FF                  call 0x140499f0c
008F96C7  33 F6                           xor esi, esi
008F96C9  C6 45 C2 01                     mov byte ptr [rbp - 0x3e], 1
008F96CD  E9 57 FB FF FF                  jmp 0x1408f9229
008F96D2  48 8B CB                        mov rcx, rbx
008F96D5  E8 86 57 05 00                  call 0x14094ee60
008F96DA  85 C0                           test eax, eax
008F96DC  8B F0                           mov esi, eax
008F96DE  8B F8                           mov edi, eax
008F96E0  B8 CE 02 00 C0                  mov eax, 0xc00002ce
008F96E5  0F 48 F8                        cmovs edi, eax
008F96E8  C1 EE 1F                        shr esi, 0x1f
008F96EB  E9 E8 FC FF FF                  jmp 0x1408f93d8
008F96F0  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
008F96F4  E8 57 FC 9F FF                  call 0x1402f9350
008F96F9  8B C3                           mov eax, ebx
008F96FB  E9 0D FC FF FF                  jmp 0x1408f930d
008F9700  85 D2                           test edx, edx
008F9702  0F 88 7B 01 00 00               js 0x1408f9883
008F9708  33 D2                           xor edx, edx
008F970A  48 8B CB                        mov rcx, rbx
008F970D  44 39 45 67                     cmp dword ptr [rbp + 0x67], r8d
008F9711  0F 95 C2                        setne dl
008F9714  E8 DF 23 00 00                  call 0x1408fbaf8
008F9719  EB BF                           jmp 0x1408f96da
008F971B  B8 01 00 00 00                  mov eax, 1
008F9720  44 8A F8                        mov r15b, al
008F9723  8B F0                           mov esi, eax
008F9725  44 89 7D C7                     mov dword ptr [rbp - 0x39], r15d
008F9729  E9 FB FA FF FF                  jmp 0x1408f9229
008F972E  0F BA E2 19                     bt edx, 0x19
008F9732  0F 83 0B FF FF FF               jae 0x1408f9643
008F9738  E9 EC FA FF FF                  jmp 0x1408f9229
008F973D  85 C0                           test eax, eax
008F973F  0F 88 8E FC FF FF               js 0x1408f93d3
008F9745  33 F6                           xor esi, esi
008F9747  E9 DD FA FF FF                  jmp 0x1408f9229
008F974C  B8 01 00 00 00                  mov eax, 1
008F9751  88 45 C1                        mov byte ptr [rbp - 0x3f], al
008F9754  E8 CB 4A BC FF                  call 0x1404be224
008F9759  48 8B C8                        mov rcx, rax
008F975C  E8 F3 1E 00 00                  call 0x1408fb654
008F9761  E8 0A 09 B9 FF                  call 0x14048a070
008F9766  85 C0                           test eax, eax
008F9768  74 EA                           je 0x1408f9754
008F976A  E9 93 FC FF FF                  jmp 0x1408f9402
008F976F  45 32 E4                        xor r12b, r12b
008F9772  BB CE 02 00 C0                  mov ebx, 0xc00002ce
008F9777  45 32 FF                        xor r15b, r15b
008F977A  41 BD 01 00 00 00               mov r13d, 1
008F9780  83 3D A5 2B 69 00 00            cmp dword ptr [rip + 0x692ba5], 0
008F9787  45 8A F7                        mov r14b, r15b
008F978A  0F 84 0C 01 00 00               je 0x1408f989c
008F9790  E8 8F 4A BC FF                  call 0x1404be224
008F9795  48 8B C8                        mov rcx, rax
008F9798  E8 B7 1E 00 00                  call 0x1408fb654
008F979D  3B C3                           cmp eax, ebx
008F979F  44 88 6D C1                     mov byte ptr [rbp - 0x3f], r13b
008F97A3  45 8A E5                        mov r12b, r13b
008F97A6  45 8A FD                        mov r15b, r13b
008F97A9  0F 44 FB                        cmove edi, ebx
008F97AC  45 8A F5                        mov r14b, r13b
008F97AF  E8 BC 08 B9 FF                  call 0x14048a070
008F97B4  85 C0                           test eax, eax
008F97B6  74 C8                           je 0x1408f9780
008F97B8  E9 E8 00 00 00                  jmp 0x1408f98a5
008F97BD  4D 8B 4D 30                     mov r9, qword ptr [r13 + 0x30]
008F97C1  48 8D 15 58 D5 72 FF            lea rdx, [rip - 0x8d2aa8]
008F97C8  E8 9F 57 BE FF                  call 0x1404def6c
008F97CD  E9 45 F9 FF FF                  jmp 0x1408f9117
008F97D2  4D 8B 4D 30                     mov r9, qword ptr [r13 + 0x30]
008F97D6  48 8D 15 73 D7 72 FF            lea rdx, [rip - 0x8d288d]
008F97DD  E8 8A 57 BE FF                  call 0x1404def6c
008F97E2  E9 53 F9 FF FF                  jmp 0x1408f913a
008F97E7  4C 8B 45 5F                     mov r8, qword ptr [rbp + 0x5f]
008F97EB  44 8B CE                        mov r9d, esi
008F97EE  48 8B 0D 43 2C 69 00            mov rcx, qword ptr [rip + 0x692c43]
008F97F5  48 8B D7                        mov rdx, rdi
008F97F8  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
008F97FD  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
008F9802  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
008F9807  E8 5C F8 FF FF                  call 0x1408f9068
008F980C  8B 4D CB                        mov ecx, dword ptr [rbp - 0x35]
008F980F  BA CE 02 00 C0                  mov edx, 0xc00002ce
008F9814  3B C2                           cmp eax, edx
008F9816  0F B6 C9                        movzx ecx, cl
008F9819  41 B8 01 00 00 00               mov r8d, 1
008F981F  41 0F 44 C8                     cmove ecx, r8d
008F9823  89 4D CB                        mov dword ptr [rbp - 0x35], ecx
008F9826  E9 22 F9 FF FF                  jmp 0x1408f914d
008F982B  45 33 C0                        xor r8d, r8d
008F982E  48 8B CB                        mov rcx, rbx
008F9831  41 8D 50 33                     lea edx, [r8 + 0x33]
008F9835  E8 D2 45 00 00                  call 0x1408fde0c
008F983A  E9 76 F9 FF FF                  jmp 0x1408f91b5
008F983F  48 8B CB                        mov rcx, rbx
008F9842  E8 71 70 E4 FF                  call 0x1407408b8
008F9847  E9 8E FE FF FF                  jmp 0x1408f96da
008F984C  0F B6 55 77                     movzx edx, byte ptr [rbp + 0x77]
008F9850  48 8B CB                        mov rcx, rbx
008F9853  45 0F B6 C7                     movzx r8d, r15b
008F9857  E8 90 6F E4 FF                  call 0x1407407ec
008F985C  B9 03 01 00 00                  mov ecx, 0x103
008F9861  45 0F B6 FF                     movzx r15d, r15b
008F9865  3B C1                           cmp eax, ecx
008F9867  8B F8                           mov edi, eax
008F9869  B8 01 00 00 00                  mov eax, 1
008F986E  44 0F 44 F8                     cmove r15d, eax
008F9872  33 F6                           xor esi, esi
008F9874  3B F9                           cmp edi, ecx
008F9876  44 89 7D C7                     mov dword ptr [rbp - 0x39], r15d
008F987A  40 0F 94 C6                     sete sil
008F987E  E9 50 FB FF FF                  jmp 0x1408f93d3
008F9883  41 8B F0                        mov esi, r8d
008F9886  E9 9E F9 FF FF                  jmp 0x1408f9229
008F988B  45 33 C0                        xor r8d, r8d
008F988E  41 8D 50 33                     lea edx, [r8 + 0x33]
008F9892  E8 75 45 00 00                  call 0x1408fde0c
008F9897  E9 8D F9 FF FF                  jmp 0x1408f9229
008F989C  45 84 E4                        test r12b, r12b
008F989F  0F 84 EB FE FF FF               je 0x1408f9790
008F98A5  48 8B 5D CF                     mov rbx, qword ptr [rbp - 0x31]
008F98A9  4C 8B 6D 4F                     mov r13, qword ptr [rbp + 0x4f]
008F98AD  44 8A 65 7F                     mov r12b, byte ptr [rbp + 0x7f]
008F98B1  E9 BD F9 FF FF                  jmp 0x1408f9273
008F98B6  4C 8B 75 D7                     mov r14, qword ptr [rbp - 0x29]
008F98BA  E9 21 FB FF FF                  jmp 0x1408f93e0
008F98BF  89 7D DF                        mov dword ptr [rbp - 0x21], edi
008F98C2  E9 DB F9 FF FF                  jmp 0x1408f92a2
008F98C7  F7 83 8C 01 00 00 00 60 00 00   test dword ptr [rbx + 0x18c], 0x6000
008F98D1  0F 84 C3 FC FF FF               je 0x1408f959a
008F98D7  45 84 FF                        test r15b, r15b
008F98DA  0F 84 BF FC FF FF               je 0x1408f959f
008F98E0  4C 8D 45 C1                     lea r8, [rbp - 0x3f]
008F98E4  8B D1                           mov edx, ecx
008F98E6  E8 E5 27 00 00                  call 0x1408fc0d0
008F98EB  45 32 FF                        xor r15b, r15b
008F98EE  44 89 7D C7                     mov dword ptr [rbp - 0x39], r15d
008F98F2  E9 A8 FC FF FF                  jmp 0x1408f959f
008F98F7  B8 01 00 00 C0                  mov eax, 0xc0000001
008F98FC  E9 0C FA FF FF                  jmp 0x1408f930d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipProcessDevNodeTree(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned __int8 v_stack_p30;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (136);
    *(unsigned __int8 *)(v_rsp - 71 - 63) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 41) = a1;
    *(unsigned __int64 *)(v_rsp - 71 - 25) = v_xmm0;
    if (a2 == 0) goto loc_008F90EB;
    if ((*(unsigned __int8 *)(a2 + 28)) != 0) goto loc_008F90EB;
    if (a4 == 1) goto loc_008F90EB;
    result = v_rsp;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 + 127)) == 0) {
        a1 = a2;
        result = PiCollapseEnumRequests(a1, a2, 1, a4);
        a1 = *(unsigned __int64 *)(v_rip + 6894429);
        a3 = 1;
        if ((unsigned __int8)(result) != 0) { a1 = a1; }
        *(unsigned __int64 *)(v_rsp - 71 + 79) = a1;
    }
    result = 0;
    a1 = 0;
    *(unsigned int *)(v_rsp - 71 - 33) = 0;
    v_r15 = 0;
    *(unsigned __int8 *)(v_rsp - 71 - 62) = 0;
    *(unsigned __int8 *)(v_rsp - 71 - 65) = (unsigned __int8)((unsigned __int8)(a3));
    *(unsigned int *)(v_rsp - 71 - 53) = 0;
    *(unsigned int *)(v_rsp - 71 - 57) = 0;
loc_008F9105:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 + 127)) != 0) goto loc_008F9150;
    if (((*(unsigned __int8 *)(v_rip + 6254618)) & (16)) != 0) goto loc_008F97BD;
loc_008F9117:
    *(unsigned __int8 *)(v_rsp - 71 - 64) = 0;
    result = PnpProcessAssignResources(0, *(unsigned __int8 *)(v_rsp - 71 + 111), v_rsp - 71 - 64, a4);
    *(unsigned __int8 *)(v_rsp - 71 - 62) = (unsigned __int8)(result);
    if (((*(unsigned __int8 *)(v_rip + 6254586)) & (16)) != 0) goto loc_008F97D2;
loc_008F913A:
    if ((*(unsigned __int8 *)(v_rsp - 71 - 64)) != 0) goto loc_008F97E7;
loc_008F914D:
loc_008F9150:
    *(unsigned __int8 *)(v_rsp - 71 - 64) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 49) = 0;
    *(unsigned __int8 *)(v_rsp - 71 - 61) = 1;
loc_008F915F:
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 53))) != 0) goto loc_008F93ED;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 - 65)) == 0) goto loc_008F9184;
    if (!(condition_is_above_or_equal)) {
        *(unsigned int *)(0 + 704) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 704)));
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 300))) - (769));
    if (((unsigned int)(result)) <= 1) goto loc_008F91BB;
    if (((*(unsigned int *)(0 + 396)) & (0x6000ULL)) != 0) goto loc_008F91BB;
    result = PnpCheckForActiveDependencies(0, 2, 1, a4);
    if ((unsigned __int8)(result) != 0) goto loc_008F982B;
loc_008F91B5:
loc_008F91BB:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(0 + 396)))) & (0x6000ULL)) != 0) goto loc_008F9299;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 300))) - (769));
    if (condition_is_equal) goto loc_008F9639;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_008F953B;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_008F9687;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_008F96D2;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008F9700;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_008F938C;
    if ((*(unsigned int *)(v_rsp - 71 + 103)) == 1) goto loc_008F962B;
loc_008F9216:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 + 127)) != 0) goto loc_008F9229;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(0 + 396)))) & (8)) != 0) goto loc_008F9511;
loc_008F9229:
    *(unsigned __int8 *)(v_rsp - 71 - 63) = 0;
    v_rdi = 0;
    v_r14 = 0;
    result = PnpDeviceCompletionQueueIsEmpty(a1, (unsigned int)(*(unsigned int *)(0 + 396)), 1, a4);
    if ((unsigned int)(result) == 0) goto loc_008F95B7;
loc_008F923F:
    if (0 == ((unsigned int)((unsigned int)(0xC00002CEULL)))) goto loc_008F98B6;
    if (0 != 0) goto loc_008F9257;
    if ((*(unsigned __int8 *)(v_rsp - 71 - 64)) != 0) goto loc_008F925D;
loc_008F9257:
    goto loc_008F9299;
loc_008F925D:
    *(unsigned __int8 *)(v_rsp - 71 - 63) = 0;
    v_rdi = 0;
    v_r14 = 0;
    result = PnpDeviceCompletionQueueIsEmpty(a1, (unsigned int)(*(unsigned int *)(0 + 396)), 1, a4);
    if ((unsigned int)(result) == 0) goto loc_008F976F;
loc_008F9273:
    v_r14 = (unsigned __int8)(-(v_r14));
    *(unsigned __int8 *)(v_rsp - 71 - 64) = 0;
    result = (unsigned __int8)((result) & (*(unsigned __int8 *)(v_rsp - 71 - 57)));
    *(unsigned int *)(v_rsp - 71 - 57) = (unsigned int)((unsigned __int8)(result));
    if (0 == ((unsigned int)((unsigned int)(0xC00002CEULL)))) goto loc_008F93E0;
loc_008F9299:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 + 127)) == 0) goto loc_008F9322;
loc_008F92A2:
loc_008F92A7:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_008F9382;
loc_008F92B0:
    v_rsi = (unsigned int)((2) - (1));
    if (condition_is_equal) goto loc_008F9352;
    if (((unsigned int)(v_rsi)) != 1) goto loc_008F92D2;
    if (*(unsigned __int64 *)(0 + 8) == 0) goto loc_008F9352;
loc_008F92CB:
    *(unsigned __int64 *)(v_rsp - 71 - 49) = *(unsigned __int64 *)(0 + 8);
loc_008F92D2:
loc_008F92DB:
loc_008F92DE:
    if ((*(unsigned __int8 *)(v_rsp - 71 - 61)) != 0) goto loc_008F915F;
    if ((*(unsigned __int8 *)(v_rsp - 71 - 62)) != 0) goto loc_008F9105;
    result = *(unsigned __int8 *)(v_rsp - 71 - 65);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 + 127)) == 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 - 41) + 32);
        result = ObfDereferenceObject(a1, (unsigned int)(*(unsigned int *)(0 + 396)), 1, a4);
    }
loc_008F930D:
    v_rsp = (v_rsp) + (136);
    return (unsigned int)(*(unsigned int *)(v_rsp - 71 - 33));
loc_008F9322:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(0 + 8) + 704))))) == 0) goto loc_008F92A7;
    a2 = 0;
    result = PpDevCfgTraceDeviceStart(*(unsigned __int64 *)(0 + 8), a2, 1, a4);
    goto loc_008F92A2;
loc_008F9344:
    if (sign_flag) goto loc_008F92B0;
loc_008F9352:
    if ((*(unsigned __int64 *)(0 + 8)) == a1) goto loc_008F958C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8)) != 0) goto loc_008F92CB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_008F95FD;
loc_008F9370:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 16) == 0) goto loc_008F9352;
    *(unsigned __int64 *)(v_rsp - 71 - 49) = *(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 16);
    goto loc_008F9352;
loc_008F9382:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103))) == 0) goto loc_008F92B0;
    goto loc_008F9344;
loc_008F938C:
    a1 = (unsigned int)((*(unsigned __int64 *)(0 + 8)) - (2));
    if (condition_is_equal) goto loc_008F984C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008F983F;
    if (((unsigned int)(a1)) != 2) goto loc_008F9229;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 16);
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 16) + 704)) & (512)) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 16) + 32);
        result = PoFxIdleDevice(a1, a2, 1, a4);
    }
    result = PipEnumerateCompleted(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 16), a2, 1, a4);
loc_008F93D3:
loc_008F93D8:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)(0xC00002CEULL)))) goto loc_008F9229;
loc_008F93E0:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 + 127)) != 0) goto loc_008F98BF;
loc_008F93ED:
    *(unsigned __int8 *)(v_rsp - 71 - 53) = 0;
    *(unsigned __int8 *)(v_rsp - 71 - 63) = 0;
    result = PnpDeviceCompletionQueueIsEmpty(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 16), a2, 1, a4);
    if ((unsigned int)(result) == 0) goto loc_008F974C;
loc_008F9402:
    v_r15 = 0;
    v_stack_p30 = 1;
    v_stack_p28 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 + 119));
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 + 111));
    *(unsigned int *)(v_rsp - 71 - 57) = 0;
    result = PipProcessDevNodeTree(*(unsigned __int64 *)(v_rip + 6893596), *(unsigned __int64 *)(v_rsp - 71 + 87), *(unsigned __int64 *)(v_rsp - 71 + 95), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = IopAllocateUnicodeString(v_rsp - 71 - 25, *(unsigned __int16 *)(a1 + 40), *(unsigned __int64 *)(v_rsp - 71 + 95), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    if (sign_flag) goto loc_008F96F0;
    result = RtlCopyUnicodeString(v_rsp - 71 - 25, a1 + 40, *(unsigned __int64 *)(v_rsp - 71 + 95), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = ObfDereferenceObject(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 - 41) + 32), a1 + 40, *(unsigned __int64 *)(v_rsp - 71 + 95), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = ExReleaseResourceLite(v_rip + 6893814, a1 + 40, *(unsigned __int64 *)(v_rsp - 71 + 95), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = ExReleaseResourceLite(v_rip + 6893674, a1 + 40, *(unsigned __int64 *)(v_rsp - 71 + 95), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = KeLeaveCriticalRegion(v_rip + 6893674, a1 + 40, *(unsigned __int64 *)(v_rsp - 71 + 95), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = PnpSynchronizeDeviceEventQueue(v_rip + 6893674, a1 + 40, *(unsigned __int64 *)(v_rsp - 71 + 95), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = ExAcquireResourceExclusiveLite(v_rip + 6893643, 1, *(unsigned __int64 *)(v_rsp - 71 + 95), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = ExAcquireResourceSharedLite(v_rip + 6893742, 1, *(unsigned __int64 *)(v_rsp - 71 + 95), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = PnpDeviceObjectFromDeviceInstanceWithTag(v_rsp - 71 - 25, (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(v_rsp - 71 + 95), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    if (*(unsigned __int64 *)(v_rsp - 71 - 17) != 0) {
        result = ExFreePool(*(unsigned __int64 *)(v_rsp - 71 - 17), (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(v_rsp - 71 + 95), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
        *(unsigned __int64 *)(v_rsp - 71 - 25) = v_xmm0;
    }
    if (result == 0) goto loc_008F98F7;
    *(unsigned __int64 *)(v_rsp - 71 - 49) = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40);
    *(unsigned __int64 *)(v_rsp - 71 + 79) = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40);
    *(unsigned __int64 *)(v_rsp - 71 - 41) = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40);
    goto loc_008F92DE;
loc_008F9511:
    result = PipEnumerateDevice(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40), *(unsigned __int8 *)(v_rsp - 71 + 119), 0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    if (((unsigned int)(result)) == 259) goto loc_008F971B;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (31));
    v_rsi = (unsigned int)((v_rsi) & (2));
    goto loc_008F93D3;
loc_008F953B:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 + 127)) != 0) goto loc_008F9229;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 704)) & (0x10000ULL)) != 0) goto loc_008F9229;
    result = PipCallDriverAddDevice(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40), *(unsigned __int64 *)(v_rsp - 71 + 95), 0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    if (!sign_flag) goto loc_008F96BD;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 300)) != 772) goto loc_008F93D8;
    goto loc_008F93D8;
loc_008F958C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5313670)))) & (4)) != 0) goto loc_008F98C7;
loc_008F959A:
    if (0 == 0) {
        *(unsigned __int8 *)(v_rsp - 71 - 61) = 0;
    }
    result = 0;
    *(unsigned __int8 *)(v_rsp - 71 - 64) = 1;
    *(unsigned __int8 *)(v_rsp - 71 - 65) = 0;
    goto loc_008F92DB;
loc_008F95B7:
loc_008F95C3:
    if ((*(unsigned int *)(v_rip + 6892898)) == 0) goto loc_008F95F0;
    result = PnpDeviceCompletionQueueGetCompletedRequest(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40), *(unsigned __int64 *)(v_rsp - 71 + 95), 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = PnpDeviceCompletionProcessCompletedRequest(result, *(unsigned __int64 *)(v_rsp - 71 + 95), 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    *(unsigned __int8 *)(v_rsp - 71 - 63) = 1;
    v_rdi = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC00002CEULL)))) { v_rdi = (unsigned int)((unsigned int)(0xC00002CEULL)); }
    result = PnpDeviceCompletionQueueIsEmpty(result, *(unsigned __int64 *)(v_rsp - 71 + 95), 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    if ((unsigned int)(result) == 0) goto loc_008F95C3;
loc_008F95F0:
    goto loc_008F923F;
loc_008F95FD:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5313557))) == 0) goto loc_008F9370;
    if (sign_flag) goto loc_008F9370;
    *(unsigned __int64 *)(v_rsp - 71 - 49) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 16) + 8);
loc_008F962B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 16) + 8)) != (*(unsigned __int64 *)(v_rsp - 71 + 79))) goto loc_008F9229;
    goto loc_008F9216;
loc_008F9639:
    if ((*(unsigned int *)(v_rsp - 71 + 103)) == 3) goto loc_008F972E;
loc_008F9643:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 + 127)) != 0) goto loc_008F9229;
    result = PnpCheckForActiveDependencies(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 16) + 8), 1, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    if ((unsigned __int8)(result) != 0) goto loc_008F988B;
    result = PiProcessNewDeviceNodeAsync(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 16) + 8), *(unsigned __int8 *)(v_rsp - 71 + 119), 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    if (((unsigned int)(result)) != 259) goto loc_008F973D;
loc_008F9678:
    *(unsigned int *)(v_rsp - 71 - 57) = 1;
    goto loc_008F9229;
loc_008F9687:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 71 + 127)) != 0) goto loc_008F9229;
    result = PnpPoFxActivateDevice(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 16) + 8), 512, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = PipProcessStartPhase1(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 16) + 8), *(unsigned __int8 *)(v_rsp - 71 + 119), 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    if (((unsigned int)(result)) == 259) goto loc_008F9678;
    v_rsi = 0;
    goto loc_008F93D3;
loc_008F96BD:
    a2 = 0;
    result = PoFxPrepareDevice(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 16) + 8), a2, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    v_rsi = 0;
    *(unsigned __int8 *)(v_rsp - 71 - 62) = 1;
    goto loc_008F9229;
loc_008F96D2:
    result = PipProcessStartPhase2(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 16) + 8), a2, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
loc_008F96DA:
    v_rdi = (unsigned int)((unsigned int)(result));
    if (sign_flag) { v_rdi = (unsigned int)((unsigned int)(0xC00002CEULL)); }
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (31));
    goto loc_008F93D8;
loc_008F96F0:
    result = ObfDereferenceObject(*(unsigned __int64 *)(1 + 32), a2, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    goto loc_008F930D;
loc_008F9700:
    if (sign_flag) goto loc_008F9883;
    a2 = 0;
    a2 = ((*(unsigned int *)(v_rsp - 71 + 103)) != 1) ? 1 : 0;
    result = PipProcessStartPhase3(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 16) + 8), a2, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    goto loc_008F96DA;
loc_008F971B:
    *(unsigned int *)(v_rsp - 71 - 57) = 1;
    goto loc_008F9229;
loc_008F972E:
    if ((*(unsigned int *)(v_rsp - 71 + 103)) >= 1) goto loc_008F9643;
    goto loc_008F9229;
loc_008F973D:
    if (sign_flag) goto loc_008F93D3;
    v_rsi = 0;
    goto loc_008F9229;
loc_008F974C:
    *(unsigned __int8 *)(v_rsp - 71 - 63) = 1;
loc_008F9754:
    result = PnpDeviceCompletionQueueGetCompletedRequest(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 312) + 40) + 16) + 8), a2, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = PnpDeviceCompletionProcessCompletedRequest(result, a2, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = PnpDeviceCompletionQueueIsEmpty(result, a2, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    if ((unsigned int)(result) == 0) goto loc_008F9754;
    goto loc_008F9402;
loc_008F976F:
    v_r12 = 0;
    v_r15 = 0;
loc_008F9780:
    if ((*(unsigned int *)(v_rip + 6892453)) == 0) goto loc_008F989C;
loc_008F9790:
    result = PnpDeviceCompletionQueueGetCompletedRequest(result, a2, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    result = PnpDeviceCompletionProcessCompletedRequest(result, a2, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    *(unsigned __int8 *)(v_rsp - 71 - 63) = 1;
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC00002CEULL)))) { v_rdi = (unsigned int)((unsigned int)(0xC00002CEULL)); }
    result = PnpDeviceCompletionQueueIsEmpty(result, a2, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 + 103)))));
    if ((unsigned int)(result) == 0) goto loc_008F9780;
    goto loc_008F98A5;
loc_008F97BD:
    result = McTemplateK0z_EtwWriteTransfer(result, v_rip - 9251496, 1, *(unsigned __int64 *)(1 + 48));
    goto loc_008F9117;
loc_008F97D2:
    result = McTemplateK0z_EtwWriteTransfer(result, v_rip - 9250957, 1, *(unsigned __int64 *)(1 + 48));
    goto loc_008F913A;
loc_008F97E7:
    v_stack_p30 = 1;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = PipProcessDevNodeTree(*(unsigned __int64 *)(v_rip + 6892611), v_rdi, *(unsigned __int64 *)(v_rsp - 71 + 95), 0);
    a1 = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 53)));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC00002CEULL)))) { a1 = 1; }
    *(unsigned int *)(v_rsp - 71 - 53) = (unsigned int)(a1);
    goto loc_008F914D;
loc_008F982B:
    a3 = 0;
    result = PipSetDevNodeProblem((unsigned int)(0xC00002CEULL), a3 + 51, a3, 0);
    goto loc_008F91B5;
loc_008F983F:
    result = PipProcessRestartPhase2((unsigned int)(0xC00002CEULL), a3 + 51, a3, 0);
    goto loc_008F96DA;
loc_008F984C:
    result = PipProcessRestartPhase1((unsigned int)(0xC00002CEULL), *(unsigned __int8 *)(v_rsp - 71 + 119), 1, 0);
    v_r15 = 1;
    if (((unsigned int)(result)) == 259) { v_r15 = 1; }
    v_rsi = 0;
    *(unsigned int *)(v_rsp - 71 - 57) = (unsigned int)(v_r15);
    v_rsi = (((unsigned int)((unsigned int)((unsigned int)(result)))) == 259) ? 1 : 0;
    goto loc_008F93D3;
loc_008F9883:
    goto loc_008F9229;
loc_008F988B:
    a3 = 0;
    result = PipSetDevNodeProblem(259, a3 + 51, a3, 0);
    goto loc_008F9229;
loc_008F989C:
    if (1 == 0) goto loc_008F9790;
loc_008F98A5:
    goto loc_008F9273;
loc_008F98B6:
    goto loc_008F93E0;
loc_008F98BF:
    *(unsigned int *)(v_rsp - 71 - 33) = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_008F92A2;
loc_008F98C7:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 - 49) + 396)) & (0x6000ULL)) == 0) goto loc_008F959A;
    if ((unsigned __int8)(v_r15) == 0) goto loc_008F959F;
    result = PnpDeviceCompletionProcessCompletedRequests(259, 259, v_rsp - 71 - 63, 0);
    v_r15 = 0;
    *(unsigned int *)(v_rsp - 71 - 57) = 0;
    goto loc_008F959F;
loc_008F98F7:
    goto loc_008F930D;
}
```

## 5. (Beta) C Style

```c
int64_t PipProcessDevNodeTree(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_p20;
    uint8_t v_stack_p28;
    uint8_t v_stack_p30;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (136);
    *(uint8_t *)(local_rsp - 0x47 - 0x3F) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x29) = Arg1;
    *(uint64_t *)(local_rsp - 0x47 - 0x19) = v_xmm0;
    if (Arg2 == 0) goto loc_008F90EB;
    if ((*(uint8_t *)(Arg2 + 0x1C)) != 0) goto loc_008F90EB;
    if (Arg4 == 1) goto loc_008F90EB;
    result = local_rsp;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x47 + 0x7F)) == 0) {
        Arg1 = Arg2;
        result = PiCollapseEnumRequests(Arg1, Arg2, 1, Arg4);
        Arg1 = *(uint64_t *)(v_rip + 0x69335D);
        Arg3 = 1;
        if ((uint8_t)(result) != 0) { Arg1 = Arg1; }
        *(uint64_t *)(local_rsp - 0x47 + 0x4F) = Arg1;
    }
    result = 0;
    Arg1 = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x21) = 0;
    local_r15 = 0;
    *(uint8_t *)(local_rsp - 0x47 - 0x3E) = 0;
    *(uint8_t *)(local_rsp - 0x47 - 0x41) = (uint8_t)((uint8_t)(Arg3));
    *(uint32_t *)(local_rsp - 0x47 - 0x35) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = 0;
loc_008F9105:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x47 + 0x7F)) != 0) goto loc_008F9150;
    if (((*(uint8_t *)(v_rip + 0x5F701A)) & (16)) != 0) goto loc_008F97BD;
loc_008F9117:
    *(uint8_t *)(local_rsp - 0x47 - 0x40) = 0;
    result = PnpProcessAssignResources(0, *(uint8_t *)(local_rsp - 0x47 + 0x6F), local_rsp - 71 - 64, Arg4);
    *(uint8_t *)(local_rsp - 0x47 - 0x3E) = (uint8_t)(result);
    if (((*(uint8_t *)(v_rip + 0x5F6FFA)) & (16)) != 0) goto loc_008F97D2;
loc_008F913A:
    if ((*(uint8_t *)(local_rsp - 0x47 - 0x40)) != 0) goto loc_008F97E7;
loc_008F914D:
loc_008F9150:
    *(uint8_t *)(local_rsp - 0x47 - 0x40) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x31) = 0;
    *(uint8_t *)(local_rsp - 0x47 - 0x3D) = 1;
loc_008F915F:
    if ((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x35))) != 0) goto loc_008F93ED;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x47 - 0x41)) == 0) goto loc_008F9184;
    if (!(condition_is_above_or_equal)) {
        *(uint32_t *)(0 + 0x2C0) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x2C0)));
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x12C))) - (769));
    if (((uint32_t)(result)) <= 1) goto loc_008F91BB;
    if (((*(uint32_t *)(0 + 0x18C)) & (0x6000ULL)) != 0) goto loc_008F91BB;
    result = PnpCheckForActiveDependencies(0, 2, 1, Arg4);
    if ((uint8_t)(result) != 0) goto loc_008F982B;
loc_008F91B5:
loc_008F91BB:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x18C)))) & (0x6000ULL)) != 0) goto loc_008F9299;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x12C))) - (769));
    if (condition_is_equal) goto loc_008F9639;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_008F953B;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_008F9687;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_008F96D2;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008F9700;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_008F938C;
    if ((*(uint32_t *)(local_rsp - 0x47 + 0x67)) == 1) goto loc_008F962B;
loc_008F9216:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x47 + 0x7F)) != 0) goto loc_008F9229;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(0 + 0x18C)))) & (8)) != 0) goto loc_008F9511;
loc_008F9229:
    *(uint8_t *)(local_rsp - 0x47 - 0x3F) = 0;
    local_rdi = 0;
    local_r14 = 0;
    result = PnpDeviceCompletionQueueIsEmpty(Arg1, (uint32_t)(*(uint32_t *)(0 + 0x18C)), 1, Arg4);
    if ((uint32_t)(result) == 0) goto loc_008F95B7;
loc_008F923F:
    if (0 == ((uint32_t)((uint32_t)(0xC00002CEULL)))) goto loc_008F98B6;
    if (0 != 0) goto loc_008F9257;
    if ((*(uint8_t *)(local_rsp - 0x47 - 0x40)) != 0) goto loc_008F925D;
loc_008F9257:
    goto loc_008F9299;
loc_008F925D:
    *(uint8_t *)(local_rsp - 0x47 - 0x3F) = 0;
    local_rdi = 0;
    local_r14 = 0;
    result = PnpDeviceCompletionQueueIsEmpty(Arg1, (uint32_t)(*(uint32_t *)(0 + 0x18C)), 1, Arg4);
    if ((uint32_t)(result) == 0) goto loc_008F976F;
loc_008F9273:
    local_r14 = (uint8_t)(-(local_r14));
    *(uint8_t *)(local_rsp - 0x47 - 0x40) = 0;
    result = (uint8_t)((result) & (*(uint8_t *)(local_rsp - 0x47 - 0x39)));
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = (uint32_t)((uint8_t)(result));
    if (0 == ((uint32_t)((uint32_t)(0xC00002CEULL)))) goto loc_008F93E0;
loc_008F9299:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x47 + 0x7F)) == 0) goto loc_008F9322;
loc_008F92A2:
loc_008F92A7:
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_008F9382;
loc_008F92B0:
    local_rsi = (uint32_t)((2) - (1));
    if (condition_is_equal) goto loc_008F9352;
    if (((uint32_t)(local_rsi)) != 1) goto loc_008F92D2;
    if (*(uint64_t *)(0 + 0x8) == 0) goto loc_008F9352;
loc_008F92CB:
    *(uint64_t *)(local_rsp - 0x47 - 0x31) = *(uint64_t *)(0 + 0x8);
loc_008F92D2:
loc_008F92DB:
loc_008F92DE:
    if ((*(uint8_t *)(local_rsp - 0x47 - 0x3D)) != 0) goto loc_008F915F;
    if ((*(uint8_t *)(local_rsp - 0x47 - 0x3E)) != 0) goto loc_008F9105;
    result = *(uint8_t *)(local_rsp - 0x47 - 0x41);
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x47 + 0x7F)) == 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x29) + 0x20);
        result = ObfDereferenceObject(Arg1, (uint32_t)(*(uint32_t *)(0 + 0x18C)), 1, Arg4);
    }
loc_008F930D:
    local_rsp = (local_rsp) + (136);
    return (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x21));
loc_008F9322:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(0 + 0x8) + 0x2C0))))) == 0) goto loc_008F92A7;
    Arg2 = 0;
    result = PpDevCfgTraceDeviceStart(*(uint64_t *)(0 + 0x8), Arg2, 1, Arg4);
    goto loc_008F92A2;
loc_008F9344:
    if (sign_flag) goto loc_008F92B0;
loc_008F9352:
    if ((*(uint64_t *)(0 + 0x8)) == Arg1) goto loc_008F958C;
    if (*(uint64_t *)(*(uint64_t *)(0 + 0x8)) != 0) goto loc_008F92CB;
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_008F95FD;
loc_008F9370:
    if (*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x10) == 0) goto loc_008F9352;
    *(uint64_t *)(local_rsp - 0x47 - 0x31) = *(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x10);
    goto loc_008F9352;
loc_008F9382:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67))) == 0) goto loc_008F92B0;
    goto loc_008F9344;
loc_008F938C:
    Arg1 = (uint32_t)((*(uint64_t *)(0 + 0x8)) - (2));
    if (condition_is_equal) goto loc_008F984C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008F983F;
    if (((uint32_t)(Arg1)) != 2) goto loc_008F9229;
    result = *(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x10);
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x10) + 0x2C0)) & (512)) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x10) + 0x20);
        result = PoFxIdleDevice(Arg1, Arg2, 1, Arg4);
    }
    result = PipEnumerateCompleted(*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x10), Arg2, 1, Arg4);
loc_008F93D3:
loc_008F93D8:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)(0xC00002CEULL)))) goto loc_008F9229;
loc_008F93E0:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x47 + 0x7F)) != 0) goto loc_008F98BF;
loc_008F93ED:
    *(uint8_t *)(local_rsp - 0x47 - 0x35) = 0;
    *(uint8_t *)(local_rsp - 0x47 - 0x3F) = 0;
    result = PnpDeviceCompletionQueueIsEmpty(*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x10), Arg2, 1, Arg4);
    if ((uint32_t)(result) == 0) goto loc_008F974C;
loc_008F9402:
    local_r15 = 0;
    v_stack_p30 = 1;
    v_stack_p28 = (uint8_t)(*(uint8_t *)(local_rsp - 0x47 + 0x77));
    v_stack_p20 = (uint8_t)(*(uint8_t *)(local_rsp - 0x47 + 0x6F));
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = 0;
    result = PipProcessDevNodeTree(*(uint64_t *)(v_rip + 0x69301C), *(uint64_t *)(local_rsp - 0x47 + 0x57), *(uint64_t *)(local_rsp - 0x47 + 0x5F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = IopAllocateUnicodeString(local_rsp - 71 - 25, *(uint16_t *)(Arg1 + 0x28), *(uint64_t *)(local_rsp - 0x47 + 0x5F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    if (sign_flag) goto loc_008F96F0;
    result = RtlCopyUnicodeString(local_rsp - 71 - 25, Arg1 + 40, *(uint64_t *)(local_rsp - 0x47 + 0x5F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = ObfDereferenceObject(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x29) + 0x20), Arg1 + 40, *(uint64_t *)(local_rsp - 0x47 + 0x5F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = ExReleaseResourceLite(v_rip + 6893814, Arg1 + 40, *(uint64_t *)(local_rsp - 0x47 + 0x5F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = ExReleaseResourceLite(v_rip + 6893674, Arg1 + 40, *(uint64_t *)(local_rsp - 0x47 + 0x5F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = KeLeaveCriticalRegion(v_rip + 6893674, Arg1 + 40, *(uint64_t *)(local_rsp - 0x47 + 0x5F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = PnpSynchronizeDeviceEventQueue(v_rip + 6893674, Arg1 + 40, *(uint64_t *)(local_rsp - 0x47 + 0x5F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = ExAcquireResourceExclusiveLite(v_rip + 6893643, 1, *(uint64_t *)(local_rsp - 0x47 + 0x5F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = ExAcquireResourceSharedLite(v_rip + 6893742, 1, *(uint64_t *)(local_rsp - 0x47 + 0x5F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = PnpDeviceObjectFromDeviceInstanceWithTag(local_rsp - 71 - 25, (uint32_t)(0x746C6644ULL), *(uint64_t *)(local_rsp - 0x47 + 0x5F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    if (*(uint64_t *)(local_rsp - 0x47 - 0x11) != 0) {
        result = ExFreePool(*(uint64_t *)(local_rsp - 0x47 - 0x11), (uint32_t)(0x746C6644ULL), *(uint64_t *)(local_rsp - 0x47 + 0x5F), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
        *(uint64_t *)(local_rsp - 0x47 - 0x19) = v_xmm0;
    }
    if (result == 0) goto loc_008F98F7;
    *(uint64_t *)(local_rsp - 0x47 - 0x31) = *(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28);
    *(uint64_t *)(local_rsp - 0x47 + 0x4F) = *(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28);
    *(uint64_t *)(local_rsp - 0x47 - 0x29) = *(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28);
    goto loc_008F92DE;
loc_008F9511:
    result = PipEnumerateDevice(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28), *(uint8_t *)(local_rsp - 0x47 + 0x77), 0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    if (((uint32_t)(result)) == 259) goto loc_008F971B;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (31));
    local_rsi = (uint32_t)((local_rsi) & (2));
    goto loc_008F93D3;
loc_008F953B:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x47 + 0x7F)) != 0) goto loc_008F9229;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x2C0)) & (0x10000ULL)) != 0) goto loc_008F9229;
    result = PipCallDriverAddDevice(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28), *(uint64_t *)(local_rsp - 0x47 + 0x5F), 0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    if (!sign_flag) goto loc_008F96BD;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x12C)) != 772) goto loc_008F93D8;
    goto loc_008F93D8;
loc_008F958C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x511486)))) & (4)) != 0) goto loc_008F98C7;
loc_008F959A:
    if (0 == 0) {
        *(uint8_t *)(local_rsp - 0x47 - 0x3D) = 0;
    }
    result = 0;
    *(uint8_t *)(local_rsp - 0x47 - 0x40) = 1;
    *(uint8_t *)(local_rsp - 0x47 - 0x41) = 0;
    goto loc_008F92DB;
loc_008F95B7:
loc_008F95C3:
    if ((*(uint32_t *)(v_rip + 0x692D62)) == 0) goto loc_008F95F0;
    result = PnpDeviceCompletionQueueGetCompletedRequest(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28), *(uint64_t *)(local_rsp - 0x47 + 0x5F), 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = PnpDeviceCompletionProcessCompletedRequest(result, *(uint64_t *)(local_rsp - 0x47 + 0x5F), 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    *(uint8_t *)(local_rsp - 0x47 - 0x3F) = 1;
    local_rdi = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC00002CEULL)))) { local_rdi = (uint32_t)((uint32_t)(0xC00002CEULL)); }
    result = PnpDeviceCompletionQueueIsEmpty(result, *(uint64_t *)(local_rsp - 0x47 + 0x5F), 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    if ((uint32_t)(result) == 0) goto loc_008F95C3;
loc_008F95F0:
    goto loc_008F923F;
loc_008F95FD:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x511415))) == 0) goto loc_008F9370;
    if (sign_flag) goto loc_008F9370;
    *(uint64_t *)(local_rsp - 0x47 - 0x31) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x10) + 0x8);
loc_008F962B:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x10) + 0x8)) != (*(uint64_t *)(local_rsp - 0x47 + 0x4F))) goto loc_008F9229;
    goto loc_008F9216;
loc_008F9639:
    if ((*(uint32_t *)(local_rsp - 0x47 + 0x67)) == 3) goto loc_008F972E;
loc_008F9643:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x47 + 0x7F)) != 0) goto loc_008F9229;
    result = PnpCheckForActiveDependencies(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x10) + 0x8), 1, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    if ((uint8_t)(result) != 0) goto loc_008F988B;
    result = PiProcessNewDeviceNodeAsync(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x10) + 0x8), *(uint8_t *)(local_rsp - 0x47 + 0x77), 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    if (((uint32_t)(result)) != 259) goto loc_008F973D;
loc_008F9678:
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = 1;
    goto loc_008F9229;
loc_008F9687:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x47 + 0x7F)) != 0) goto loc_008F9229;
    result = PnpPoFxActivateDevice(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x10) + 0x8), 512, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = PipProcessStartPhase1(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x10) + 0x8), *(uint8_t *)(local_rsp - 0x47 + 0x77), 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    if (((uint32_t)(result)) == 259) goto loc_008F9678;
    local_rsi = 0;
    goto loc_008F93D3;
loc_008F96BD:
    Arg2 = 0;
    result = PoFxPrepareDevice(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x10) + 0x8), Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    local_rsi = 0;
    *(uint8_t *)(local_rsp - 0x47 - 0x3E) = 1;
    goto loc_008F9229;
loc_008F96D2:
    result = PipProcessStartPhase2(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x10) + 0x8), Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
loc_008F96DA:
    local_rdi = (uint32_t)((uint32_t)(result));
    if (sign_flag) { local_rdi = (uint32_t)((uint32_t)(0xC00002CEULL)); }
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (31));
    goto loc_008F93D8;
loc_008F96F0:
    result = ObfDereferenceObject(*(uint64_t *)(1 + 0x20), Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    goto loc_008F930D;
loc_008F9700:
    if (sign_flag) goto loc_008F9883;
    Arg2 = 0;
    Arg2 = ((*(uint32_t *)(local_rsp - 0x47 + 0x67)) != 1) ? 1 : 0;
    result = PipProcessStartPhase3(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x10) + 0x8), Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    goto loc_008F96DA;
loc_008F971B:
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = 1;
    goto loc_008F9229;
loc_008F972E:
    if ((*(uint32_t *)(local_rsp - 0x47 + 0x67)) >= 1) goto loc_008F9643;
    goto loc_008F9229;
loc_008F973D:
    if (sign_flag) goto loc_008F93D3;
    local_rsi = 0;
    goto loc_008F9229;
loc_008F974C:
    *(uint8_t *)(local_rsp - 0x47 - 0x3F) = 1;
loc_008F9754:
    result = PnpDeviceCompletionQueueGetCompletedRequest(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x138) + 0x28) + 0x10) + 0x8), Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = PnpDeviceCompletionProcessCompletedRequest(result, Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = PnpDeviceCompletionQueueIsEmpty(result, Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    if ((uint32_t)(result) == 0) goto loc_008F9754;
    goto loc_008F9402;
loc_008F976F:
    local_r12 = 0;
    local_r15 = 0;
loc_008F9780:
    if ((*(uint32_t *)(v_rip + 0x692BA5)) == 0) goto loc_008F989C;
loc_008F9790:
    result = PnpDeviceCompletionQueueGetCompletedRequest(result, Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    result = PnpDeviceCompletionProcessCompletedRequest(result, Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    *(uint8_t *)(local_rsp - 0x47 - 0x3F) = 1;
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC00002CEULL)))) { local_rdi = (uint32_t)((uint32_t)(0xC00002CEULL)); }
    result = PnpDeviceCompletionQueueIsEmpty(result, Arg2, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x67)))));
    if ((uint32_t)(result) == 0) goto loc_008F9780;
    goto loc_008F98A5;
loc_008F97BD:
    result = McTemplateK0z_EtwWriteTransfer(result, v_rip - 9251496, 1, *(uint64_t *)(1 + 0x30));
    goto loc_008F9117;
loc_008F97D2:
    result = McTemplateK0z_EtwWriteTransfer(result, v_rip - 9250957, 1, *(uint64_t *)(1 + 0x30));
    goto loc_008F913A;
loc_008F97E7:
    v_stack_p30 = 1;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = PipProcessDevNodeTree(*(uint64_t *)(v_rip + 0x692C43), local_rdi, *(uint64_t *)(local_rsp - 0x47 + 0x5F), 0);
    Arg1 = (uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x35)));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC00002CEULL)))) { Arg1 = 1; }
    *(uint32_t *)(local_rsp - 0x47 - 0x35) = (uint32_t)(Arg1);
    goto loc_008F914D;
loc_008F982B:
    Arg3 = 0;
    result = PipSetDevNodeProblem((uint32_t)(0xC00002CEULL), Arg3 + 51, Arg3, 0);
    goto loc_008F91B5;
loc_008F983F:
    result = PipProcessRestartPhase2((uint32_t)(0xC00002CEULL), Arg3 + 51, Arg3, 0);
    goto loc_008F96DA;
loc_008F984C:
    result = PipProcessRestartPhase1((uint32_t)(0xC00002CEULL), *(uint8_t *)(local_rsp - 0x47 + 0x77), 1, 0);
    local_r15 = 1;
    if (((uint32_t)(result)) == 259) { local_r15 = 1; }
    local_rsi = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = (uint32_t)(local_r15);
    local_rsi = (((uint32_t)((uint32_t)((uint32_t)(result)))) == 259) ? 1 : 0;
    goto loc_008F93D3;
loc_008F9883:
    goto loc_008F9229;
loc_008F988B:
    Arg3 = 0;
    result = PipSetDevNodeProblem(259, Arg3 + 51, Arg3, 0);
    goto loc_008F9229;
loc_008F989C:
    if (1 == 0) goto loc_008F9790;
loc_008F98A5:
    goto loc_008F9273;
loc_008F98B6:
    goto loc_008F93E0;
loc_008F98BF:
    *(uint32_t *)(local_rsp - 0x47 - 0x21) = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_008F92A2;
loc_008F98C7:
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 - 0x31) + 0x18C)) & (0x6000ULL)) == 0) goto loc_008F959A;
    if ((uint8_t)(local_r15) == 0) goto loc_008F959F;
    result = PnpDeviceCompletionProcessCompletedRequests(259, 259, local_rsp - 71 - 63, 0);
    local_r15 = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = 0;
    goto loc_008F959F;
loc_008F98F7:
    goto loc_008F930D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F9068&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
