# ObCreateObjectEx

- RVA: `0x0089B1E0`–`0x0089B921` (길이 `1,857` bytes)
- VA: `0x000000014089B1E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007E744`
- 디코드: `435`개 명령, `1,857/1,857` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **47**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x0089B24C` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x0089B269` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x0089B287` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0089B2BE` → [ObpCaptureObjectCreateInformation](ObpCaptureObjectCreateInformation_function_0089B930.md) (function, `0x0089B930`)
- `0x0089B328` → [ObpAllocateObject](ObpAllocateObject_function_00899FF0.md) (function, `0x00899FF0`)
- `0x0089B37A` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x0089B390` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0089B3C0` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x0089B3CE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0089B436` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x0089B493` → [SepPrivilegeCheck](../../text/40/SepPrivilegeCheck_function_0040B6B0.md) (function, `0x0040B6B0`)
- `0x0089B4C5` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x0089B539` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0089B58E` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x0089B59A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0089B5B9` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x0089B5D4` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x0089B604` → [SepAdtPrivilegedServiceAuditAlarm](../87/SepAdtPrivilegedServiceAuditAlarm_function_008714F0.md) (function, `0x008714F0`)
- `0x0089B629` → [PspLockThreadSecurityShared](../../text/3C/PspLockThreadSecurityShared_function_003C4720.md) (function, `0x003C4720`)
- `0x0089B64F` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0089B667` → [PspUnlockThreadSecurityShared](../../text/3C/PspUnlockThreadSecurityShared_function_003C2E40.md) (function, `0x003C2E40`)
- `0x0089B687` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0089B779` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x0089B7B1` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x0089B81A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0089B8D4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0089B8F2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0089B8FF` → [ObpRegisterObject](../AC/ObpRegisterObject_function_00ACF3EC.md) (function, `0x00ACF3EC`)
- `0x0089B917` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)

### Direct callers
- [HalpDmaAllocateChildAdapterV3](../70/HalpDmaAllocateChildAdapterV3_function_007066A0.md) at `0x0070683F`
- [HalpDmaAllocateChildAdapterV2](../70/HalpDmaAllocateChildAdapterV2_function_0070A200.md) at `0x0070A295`
- [IoCreateController](../71/IoCreateController_function_0071D190.md) at `0x0071D20E`
- [NtCreateIoRing](../72/NtCreateIoRing_function_00720530.md) at `0x00720736`
- [PopEtEnergyTrackerCreate](../76/PopEtEnergyTrackerCreate_function_00769EE0.md) at `0x00769FCC`
- [TtmiCreateTerminal](../77/TtmiCreateTerminal_function_0077C748.md) at `0x0077C83D`
- [TtmiCreateEventQueue](../77/TtmiCreateEventQueue_function_0077DA14.md) at `0x0077DAA2`
- [NtCreateProcessStateChange](../78/NtCreateProcessStateChange_function_007830C0.md) at `0x007831B1`
- [PsCreateCpuPartition](../78/PsCreateCpuPartition_function_00783A8C.md) at `0x00783B13`
- [PspAllocatePartition](../78/PspAllocatePartition_function_0078802C.md) at `0x007880B3`
- [PspSessionObjectCreate](../78/PspSessionObjectCreate_function_007892A8.md) at `0x007894A3`
- [EtwpRegisterPrivateSession](../7B/EtwpRegisterPrivateSession_function_007BC92C.md) at `0x007BCB7B`
- [EtwpSetCoverageSamplerInformation](../7C/EtwpSetCoverageSamplerInformation_function_007C288C.md) at `0x007C2D44`
- [ExpProfileCreate](../7D/ExpProfileCreate_function_007D1AB8.md) at `0x007D1E99`
- [NtCreateKeyedEvent](../7D/NtCreateKeyedEvent_function_007D4CF0.md) at `0x007D4D7F`
- [CmpDoAccessCheckOnKCB](../7E/CmpDoAccessCheckOnKCB_function_007EB348.md) at `0x007EB3DD`
- [SepDuplicateToken](../8B/SepDuplicateToken_function_008B87EC.md) at `0x008B8944`
- [WmipCreateGuidObject](../8C/WmipCreateGuidObject_function_008C7930.md) at `0x008C7A75`
- [NtCreateJobObject](../91/NtCreateJobObject_function_009177E0.md) at `0x00917897`
- [AlpcpCreateClientPort](../92/AlpcpCreateClientPort_function_009270AC.md) at `0x0092725A`
- [VrpHandleIoctlInitializeJobForVreg](../93/VrpHandleIoctlInitializeJobForVreg_function_00937254.md) at `0x009372CF`
- [PspSchedulerSharedDataRegionCreate](../98/PspSchedulerSharedDataRegionCreate_function_009825DC.md) at `0x0098267B`
- [MiFinishCreateSection](../98/MiFinishCreateSection_function_009844FC.md) at `0x0098463F`
- [IopLoadDriver](../99/IopLoadDriver_function_00997B54.md) at `0x0099806D`
- [IoCreateDevice](../9A/IoCreateDevice_function_009A4B00.md) at `0x009A4CAC`
- [sub_009A5974](../9A/Unknown_function_009A5974.md) at `0x009A59DF`
- [NtCreateWorkerFactory](../9A/NtCreateWorkerFactory_function_009A7E10.md) at `0x009A7FD5`
- [SepFilterToken](../9C/SepFilterToken_function_009C6B80.md) at `0x009C6DB6`
- [NtCreatePrivateNamespace](../9C/NtCreatePrivateNamespace_function_009CA6D0.md) at `0x009CA78E`
- [AlpcpCreatePort](../9E/AlpcpCreatePort_function_009E7358.md) at `0x009E738C`
- [PsCreateSiloContext](../9E/PsCreateSiloContext_function_009E8110.md) at `0x009E817A`
- [PspAllocateThread](../9E/PspAllocateThread_function_009EF72C.md) at `0x009EFA0E`
- [NtCreateTimer](../9F/NtCreateTimer_function_009FF010.md) at `0x009FF0A6`
- [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A14070`
- [NtCreateTimer2](../A2/NtCreateTimer2_function_00A2C660.md) at `0x00A2C747`
- [NtCreateIoCompletion](../A2/NtCreateIoCompletion_function_00A2CA60.md) at `0x00A2CAD3`
- [ObCreateSymbolicLink](../A3/ObCreateSymbolicLink_function_00A33B98.md) at `0x00A33C21`
- [ObpCreateDirectoryObject](../A5/ObpCreateDirectoryObject_function_00A56230.md) at `0x00A56310`
- [NtCreateRegistryTransaction](../A6/NtCreateRegistryTransaction_function_00A61370.md) at `0x00A6144A`
- [EtwpRealtimeConnect](../A6/EtwpRealtimeConnect_function_00A65C88.md) at `0x00A65F40`
- [NtAllocateReserveObject](../A6/NtAllocateReserveObject_function_00A687A0.md) at `0x00A68828`
- [NtCreateThreadStateChange](../A7/NtCreateThreadStateChange_function_00A77110.md) at `0x00A771F7`
- [ExCreateCallback](../A7/ExCreateCallback_function_00A7B9D0.md) at `0x00A7BB55`
- [EtwpCreateUmReplyObject](../A8/EtwpCreateUmReplyObject_function_00A8DBE4.md) at `0x00A8DC97`
- [PspCreateActivityReference](../A8/PspCreateActivityReference_function_00A8F110.md) at `0x00A8F19A`
- [NtCreateDebugObject](../AC/NtCreateDebugObject_function_00AC2270.md) at `0x00AC2311`
- [IoCreateDriver](../AC/IoCreateDriver_function_00AC9D70.md) at `0x00AC9EC4`

### Static image references
- `0x0089B1FC` → RVA `0x00E0A740` (`.data`; read)
- `0x0089B33B` → RVA `0x00B82850` (`ExFreePool`; read)
- `0x0089B3EF` → RVA `0x00FD9BD0` (`PAGEDATA`; read)
- `0x0089B43B` → RVA `0x00FD8010` (`PAGEDATA`; read)
- `0x0089B4BB` → RVA `0x00E67D58` (`.data`; read)
- `0x0089B520` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x0089B5A4` → RVA `0x00FD9AA0` (`PAGEDATA`; read)
- `0x0089B5EE` → RVA `0x000013A8` (`.rdata`; read)
- `0x0089B6B2` → RVA `0x00FD8238` (`PAGEDATA`; read)
- `0x0089B70A` → RVA `0x00B4BE28` (`SepServicesFilterPrivileges`; read)
- `0x0089B841` → RVA `0x00E67B90` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **25**
  - `0x0089B24C` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x0089B269` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x0089B287` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0089B37A` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x0089B390` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0089B3C0` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x0089B3CE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0089B436` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x0089B493` → [SepPrivilegeCheck](../../text/40/SepPrivilegeCheck_function_0040B6B0.md) (`PAGE` → `.text`)
  - `0x0089B4C5` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x0089B539` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
  - `0x0089B58E` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x0089B59A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0089B5B9` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x0089B5D4` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x0089B629` → [PspLockThreadSecurityShared](../../text/3C/PspLockThreadSecurityShared_function_003C4720.md) (`PAGE` → `.text`)
  - `0x0089B64F` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0089B667` → [PspUnlockThreadSecurityShared](../../text/3C/PspUnlockThreadSecurityShared_function_003C2E40.md) (`PAGE` → `.text`)
  - `0x0089B687` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0089B779` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x0089B7B1` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x0089B81A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0089B8D4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0089B8F2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0089B917` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0089B1E0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0089B1E5  55                              push rbp
0089B1E6  56                              push rsi
0089B1E7  57                              push rdi
0089B1E8  41 54                           push r12
0089B1EA  41 55                           push r13
0089B1EC  41 56                           push r14
0089B1EE  41 57                           push r15
0089B1F0  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
0089B1F5  48 81 EC B0 00 00 00            sub rsp, 0xb0
0089B1FC  48 8B 05 3D F5 56 00            mov rax, qword ptr [rip + 0x56f53d]
0089B203  48 33 C4                        xor rax, rsp
0089B206  48 89 45 FF                     mov qword ptr [rbp - 1], rax
0089B20A  65 48 8B 34 25 20 00 00 00      mov rsi, qword ptr gs:[0x20]
0089B213  44 0F B6 E1                     movzx r12d, cl
0089B217  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
0089B21E  0F 57 C0                        xorps xmm0, xmm0
0089B221  45 0F B6 E9                     movzx r13d, r9b
0089B225  44 88 4D 97                     mov byte ptr [rbp - 0x69], r9b
0089B229  4D 8B F8                        mov r15, r8
0089B22C  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0089B230  48 8B 9E 40 08 00 00            mov rbx, qword ptr [rsi + 0x840]
0089B237  4C 8B F2                        mov r14, rdx
0089B23A  48 8B CB                        mov rcx, rbx
0089B23D  48 C7 45 D7 00 00 00 00         mov qword ptr [rbp - 0x29], 0
0089B245  0F 11 45 C7                     movups xmmword ptr [rbp - 0x39], xmm0
0089B249  FF 43 14                        inc dword ptr [rbx + 0x14]
0089B24C  E8 1F F3 E1 FF                  call 0x1406ba570
0089B251  48 8B F8                        mov rdi, rax
0089B254  48 85 C0                        test rax, rax
0089B257  75 3B                           jne 0x14089b294
0089B259  FF 43 18                        inc dword ptr [rbx + 0x18]
0089B25C  48 8B 9E 48 08 00 00            mov rbx, qword ptr [rsi + 0x848]
0089B263  48 8B CB                        mov rcx, rbx
0089B266  FF 43 14                        inc dword ptr [rbx + 0x14]
0089B269  E8 02 F3 E1 FF                  call 0x1406ba570
0089B26E  48 8B F8                        mov rdi, rax
0089B271  48 85 C0                        test rax, rax
0089B274  75 1E                           jne 0x14089b294
0089B276  8B 53 2C                        mov edx, dword ptr [rbx + 0x2c]
0089B279  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
0089B27D  44 8B 43 28                     mov r8d, dword ptr [rbx + 0x28]
0089B281  8B 4B 24                        mov ecx, dword ptr [rbx + 0x24]
0089B284  FF 43 18                        inc dword ptr [rbx + 0x18]
0089B287  E8 44 F8 E1 FF                  call 0x1406baad0
0089B28C  48 8B F8                        mov rdi, rax
0089B28F  48 85 C0                        test rax, rax
0089B292  74 05                           je 0x14089b299
0089B294  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
0089B297  89 07                           mov dword ptr [rdi], eax
0089B299  48 85 FF                        test rdi, rdi
0089B29C  0F 84 82 05 00 00               je 0x14089b824
0089B2A2  C7 44 24 28 00 00 00 00         mov dword ptr [rsp + 0x28], 0
0089B2AA  4C 8D 4D C7                     lea r9, [rbp - 0x39]
0089B2AE  4D 8B C7                        mov r8, r15
0089B2B1  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0089B2B6  41 0F B6 D5                     movzx edx, r13b
0089B2BA  41 0F B6 CC                     movzx ecx, r12b
0089B2BE  E8 6D 06 00 00                  call 0x14089b930
0089B2C3  8B D8                           mov ebx, eax
0089B2C5  85 C0                           test eax, eax
0089B2C7  0F 88 98 02 00 00               js 0x14089b565
0089B2CD  8B 0F                           mov ecx, dword ptr [rdi]
0089B2CF  41 85 4E 48                     test dword ptr [r14 + 0x48], ecx
0089B2D3  0F 85 05 06 00 00               jne 0x14089b8de
0089B2D9  F6 C1 10                        test cl, 0x10
0089B2DC  0F 85 0D 01 00 00               jne 0x14089b3ef
0089B2E2  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
0089B2E5  85 C0                           test eax, eax
0089B2E7  75 04                           jne 0x14089b2ed
0089B2E9  41 8B 46 68                     mov eax, dword ptr [r14 + 0x68]
0089B2ED  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
0089B2F0  85 C9                           test ecx, ecx
0089B2F2  75 04                           jne 0x14089b2f8
0089B2F4  41 8B 4E 6C                     mov ecx, dword ptr [r14 + 0x6c]
0089B2F8  89 47 14                        mov dword ptr [rdi + 0x14], eax
0089B2FB  4C 8D 4D C7                     lea r9, [rbp - 0x39]
0089B2FF  48 8B 85 8F 00 00 00            mov rax, qword ptr [rbp + 0x8f]
0089B306  4D 8B C6                        mov r8, r14
0089B309  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089B30E  41 0F B6 D5                     movzx edx, r13b
0089B312  48 8D 45 D7                     lea rax, [rbp - 0x29]
0089B316  89 4F 18                        mov dword ptr [rdi + 0x18], ecx
0089B319  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0089B31E  48 8B CF                        mov rcx, rdi
0089B321  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
0089B324  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0089B328  E8 C3 EC FF FF                  call 0x140899ff0
0089B32D  8B D8                           mov ebx, eax
0089B32F  85 C0                           test eax, eax
0089B331  0F 89 5A 03 00 00               jns 0x14089b691
0089B337  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
0089B33B  48 8D 35 0E 75 2E 00            lea rsi, [rip + 0x2e750e]
0089B342  48 85 C9                        test rcx, rcx
0089B345  74 38                           je 0x14089b37f
0089B347  B8 F8 00 00 00                  mov eax, 0xf8
0089B34C  66 39 45 C9                     cmp word ptr [rbp - 0x37], ax
0089B350  0F 85 42 02 00 00               jne 0x14089b598
0089B356  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0089B35F  48 8B 8A 50 08 00 00            mov rcx, qword ptr [rdx + 0x850]
0089B366  FF 41 1C                        inc dword ptr [rcx + 0x1c]
0089B369  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
0089B36D  66 39 01                        cmp word ptr [rcx], ax
0089B370  0F 83 0D 04 00 00               jae 0x14089b783
0089B376  48 8B 55 CF                     mov rdx, qword ptr [rbp - 0x31]
0089B37A  E8 31 F2 E1 FF                  call 0x1406ba5b0
0089B37F  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0089B383  48 85 C9                        test rcx, rcx
0089B386  74 15                           je 0x14089b39d
0089B388  80 7F 10 01                     cmp byte ptr [rdi + 0x10], 1
0089B38C  77 07                           ja 0x14089b395
0089B38E  33 D2                           xor edx, edx
0089B390  E8 DB 74 2E 00                  call 0x140b82870
0089B395  48 C7 47 20 00 00 00 00         mov qword ptr [rdi + 0x20], 0
0089B39D  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0089B3A6  48 8B 8A 40 08 00 00            mov rcx, qword ptr [rdx + 0x840]
0089B3AD  FF 41 1C                        inc dword ptr [rcx + 0x1c]
0089B3B0  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
0089B3B4  66 39 01                        cmp word ptr [rcx], ax
0089B3B7  0F 83 8F 03 00 00               jae 0x14089b74c
0089B3BD  48 8B D7                        mov rdx, rdi
0089B3C0  E8 EB F1 E1 FF                  call 0x1406ba5b0
0089B3C5  8B C3                           mov eax, ebx
0089B3C7  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
0089B3CB  48 33 CC                        xor rcx, rsp
0089B3CE  E8 6D 12 E1 FF                  call 0x1406ac640
0089B3D3  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
0089B3DB  48 81 C4 B0 00 00 00            add rsp, 0xb0
0089B3E2  41 5F                           pop r15
0089B3E4  41 5E                           pop r14
0089B3E6  41 5D                           pop r13
0089B3E8  41 5C                           pop r12
0089B3EA  5F                              pop rdi
0089B3EB  5E                              pop rsi
0089B3EC  5D                              pop rbp
0089B3ED  C3                              ret
0089B3EE  CC                              int3
0089B3EF  48 8B 1D DA E7 73 00            mov rbx, qword ptr [rip + 0x73e7da]
0089B3F6  0F 57 C0                        xorps xmm0, xmm0
0089B3F9  F3 0F 7F 45 A7                  movdqu xmmword ptr [rbp - 0x59], xmm0
0089B3FE  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
0089B407  4C 8B AE B8 00 00 00            mov r13, qword ptr [rsi + 0xb8]
0089B40E  49 8B 85 D0 01 00 00            mov rax, qword ptr [r13 + 0x1d0]
0089B415  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0089B419  8B 86 A0 05 00 00               mov eax, dword ptr [rsi + 0x5a0]
0089B41F  A8 08                           test al, 8
0089B421  0F 85 EF 01 00 00               jne 0x14089b616
0089B427  45 33 FF                        xor r15d, r15d
0089B42A  BA 53 65 53 75                  mov edx, 0x75536553
0089B42F  4C 89 7D 9F                     mov qword ptr [rbp - 0x61], r15
0089B433  49 8B CD                        mov rcx, r13
0089B436  E8 45 4B 97 FF                  call 0x14020ff80
0089B43B  83 3D CE CB 73 00 00            cmp dword ptr [rip + 0x73cbce], 0
0089B442  4C 8B F8                        mov r15, rax
0089B445  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
0089B449  0F 85 32 04 00 00               jne 0x14089b881
0089B44F  48 8B 75 9F                     mov rsi, qword ptr [rbp - 0x61]
0089B453  48 89 5D EF                     mov qword ptr [rbp - 0x11], rbx
0089B457  41 BD 01 00 00 00               mov r13d, 1
0089B45D  44 89 6D E7                     mov dword ptr [rbp - 0x19], r13d
0089B461  44 89 6D EB                     mov dword ptr [rbp - 0x15], r13d
0089B465  C7 45 F7 00 00 00 00            mov dword ptr [rbp - 9], 0
0089B46C  45 84 E4                        test r12b, r12b
0089B46F  0F 84 94 03 00 00               je 0x14089b809
0089B475  48 85 F6                        test rsi, rsi
0089B478  0F 85 F3 01 00 00               jne 0x14089b671
0089B47E  49 8B F7                        mov rsi, r15
0089B481  45 8B CD                        mov r9d, r13d
0089B484  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
0089B489  45 8B C5                        mov r8d, r13d
0089B48C  48 8D 55 EF                     lea rdx, [rbp - 0x11]
0089B490  48 8B CE                        mov rcx, rsi
0089B493  E8 18 02 B7 FF                  call 0x14040b6b0
0089B498  4C 8B 7D AF                     mov r15, qword ptr [rbp - 0x51]
0089B49C  0F B6 D8                        movzx ebx, al
0089B49F  48 8B 75 9F                     mov rsi, qword ptr [rbp - 0x61]
0089B4A3  44 8B 6D E7                     mov r13d, dword ptr [rbp - 0x19]
0089B4A7  48 85 F6                        test rsi, rsi
0089B4AA  49 8B CF                        mov rcx, r15
0089B4AD  48 0F 45 CE                     cmovne rcx, rsi
0089B4B1  48 8B 89 98 00 00 00            mov rcx, qword ptr [rcx + 0x98]
0089B4B8  4C 8B 21                        mov r12, qword ptr [rcx]
0089B4BB  48 8B 0D 96 C8 5C 00            mov rcx, qword ptr [rip + 0x5cc896]
0089B4C2  49 8B D4                        mov rdx, r12
0089B4C5  E8 06 56 B6 FF                  call 0x140400ad0
0089B4CA  84 C0                           test al, al
0089B4CC  0F 84 D2 00 00 00               je 0x14089b5a4
0089B4D2  83 3D 37 CB 73 00 00            cmp dword ptr [rip + 0x73cb37], 0
0089B4D9  0F 85 4F 03 00 00               jne 0x14089b82e
0089B4DF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0089B4E8  4C 8B 45 AF                     mov r8, qword ptr [rbp - 0x51]
0089B4EC  48 8B 90 B8 00 00 00            mov rdx, qword ptr [rax + 0xb8]
0089B4F3  0F 0D 8A 48 02 00 00            prefetchw byte ptr [rdx + 0x248]
0089B4FA  48 8B 82 48 02 00 00            mov rax, qword ptr [rdx + 0x248]
0089B501  48 8B C8                        mov rcx, rax
0089B504  49 33 C8                        xor rcx, r8
0089B507  48 83 F9 0F                     cmp rcx, 0xf
0089B50B  0F 83 01 03 00 00               jae 0x14089b812
0089B511  48 8D 48 01                     lea rcx, [rax + 1]
0089B515  F0 48 0F B1 8A 48 02 00 00      lock cmpxchg qword ptr [rdx + 0x248], rcx
0089B51E  75 E1                           jne 0x14089b501
0089B520  83 3D E9 9A 72 00 00            cmp dword ptr [rip + 0x729ae9], 0
0089B527  74 15                           je 0x14089b53e
0089B529  33 D2                           xor edx, edx
0089B52B  49 8D 48 D0                     lea rcx, [r8 - 0x30]
0089B52F  41 B9 53 65 53 75               mov r9d, 0x75536553
0089B535  44 8D 42 01                     lea r8d, [rdx + 1]
0089B539  E8 A6 54 97 FF                  call 0x1402109e4
0089B53E  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
0089B542  48 C7 45 AF 00 00 00 00         mov qword ptr [rbp - 0x51], 0
0089B54A  48 85 C9                        test rcx, rcx
0089B54D  0F 85 2F 01 00 00               jne 0x14089b682
0089B553  84 DB                           test bl, bl
0089B555  0F 85 8D 03 00 00               jne 0x14089b8e8
0089B55B  BB 61 00 00 C0                  mov ebx, 0xc0000061
0089B560  E9 D2 FD FF FF                  jmp 0x14089b337
0089B565  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0089B56E  4C 8B 80 40 08 00 00            mov r8, qword ptr [rax + 0x840]
0089B575  41 FF 40 1C                     inc dword ptr [r8 + 0x1c]
0089B579  41 0F B7 48 10                  movzx ecx, word ptr [r8 + 0x10]
0089B57E  66 41 39 08                     cmp word ptr [r8], cx
0089B582  0F 83 4F 02 00 00               jae 0x14089b7d7
0089B588  48 8B D7                        mov rdx, rdi
0089B58B  49 8B C8                        mov rcx, r8
0089B58E  E8 1D F0 E1 FF                  call 0x1406ba5b0
0089B593  E9 2D FE FF FF                  jmp 0x14089b3c5
0089B598  33 D2                           xor edx, edx
0089B59A  E8 D1 72 2E 00                  call 0x140b82870
0089B59F  E9 DB FD FF FF                  jmp 0x14089b37f
0089B5A4  48 8B 05 F5 E4 73 00            mov rax, qword ptr [rip + 0x73e4f5]
0089B5AB  49 8B D4                        mov rdx, r12
0089B5AE  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0089B5B2  48 8B 88 88 01 00 00            mov rcx, qword ptr [rax + 0x188]
0089B5B9  E8 12 55 B6 FF                  call 0x140400ad0
0089B5BE  84 C0                           test al, al
0089B5C0  0F 85 EC 00 00 00               jne 0x14089b6b2
0089B5C6  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
0089B5CA  49 8B D4                        mov rdx, r12
0089B5CD  48 8B 89 80 01 00 00            mov rcx, qword ptr [rcx + 0x180]
0089B5D4  E8 F7 54 B6 FF                  call 0x140400ad0
0089B5D9  84 C0                           test al, al
0089B5DB  0F 85 D1 00 00 00               jne 0x14089b6b2
0089B5E1  48 8D 45 E7                     lea rax, [rbp - 0x19]
0089B5E5  88 5C 24 30                     mov byte ptr [rsp + 0x30], bl
0089B5E9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0089B5EE  48 8D 15 B3 5D 76 FF            lea rdx, [rip - 0x89a24d]
0089B5F5  4C 8B CE                        mov r9, rsi
0089B5F8  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0089B5FD  45 33 C0                        xor r8d, r8d
0089B600  48 8D 4D 9F                     lea rcx, [rbp - 0x61]
0089B604  E8 E7 5E FD FF                  call 0x1408714f0
0089B609  4C 8B 7D AF                     mov r15, qword ptr [rbp - 0x51]
0089B60D  48 8B 75 9F                     mov rsi, qword ptr [rbp - 0x61]
0089B611  E9 BC FE FF FF                  jmp 0x14089b4d2
0089B616  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0089B61F  48 8B CE                        mov rcx, rsi
0089B622  48 8B D0                        mov rdx, rax
0089B625  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0089B629  E8 F2 90 B2 FF                  call 0x1403c4720
0089B62E  8B 86 A0 05 00 00               mov eax, dword ptr [rsi + 0x5a0]
0089B634  A8 08                           test al, 8
0089B636  0F 84 93 01 00 00               je 0x14089b7cf
0089B63C  4C 8B BE 38 05 00 00            mov r15, qword ptr [rsi + 0x538]
0089B643  BA 53 65 53 75                  mov edx, 0x75536553
0089B648  49 83 E7 F8                     and r15, 0xfffffffffffffff8
0089B64C  49 8B CF                        mov rcx, r15
0089B64F  E8 BC 50 97 FF                  call 0x140210710
0089B654  8B 86 38 05 00 00               mov eax, dword ptr [rsi + 0x538]
0089B65A  83 E0 03                        and eax, 3
0089B65D  89 45 A7                        mov dword ptr [rbp - 0x59], eax
0089B660  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
0089B664  48 8B CE                        mov rcx, rsi
0089B667  E8 D4 77 B2 FF                  call 0x1403c2e40
0089B66C  E9 B9 FD FF FF                  jmp 0x14089b42a
0089B671  83 7D A7 02                     cmp dword ptr [rbp - 0x59], 2
0089B675  0F 8D 06 FE FF FF               jge 0x14089b481
0089B67B  32 DB                           xor bl, bl
0089B67D  E9 25 FE FF FF                  jmp 0x14089b4a7
0089B682  BA 53 65 53 75                  mov edx, 0x75536553
0089B687  E8 54 C2 A5 FF                  call 0x1402f78e0
0089B68C  E9 C2 FE FF FF                  jmp 0x14089b553
0089B691  83 3D 78 99 72 00 00            cmp dword ptr [rip + 0x729978], 0
0089B698  48 8B 7D D7                     mov rdi, qword ptr [rbp - 0x29]
0089B69C  0F 85 5A 02 00 00               jne 0x14089b8fc
0089B6A2  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
0089B6A6  48 8D 47 30                     lea rax, [rdi + 0x30]
0089B6AA  48 89 01                        mov qword ptr [rcx], rax
0089B6AD  E9 13 FD FF FF                  jmp 0x14089b3c5
0089B6B2  4C 8B 1D 7F CB 73 00            mov r11, qword ptr [rip + 0x73cb7f]
0089B6B9  45 33 D2                        xor r10d, r10d
0089B6BC  45 85 ED                        test r13d, r13d
0089B6BF  0F 84 0D FE FF FF               je 0x14089b4d2
0089B6C5  48 8D 55 EF                     lea rdx, [rbp - 0x11]
0089B6C9  45 8B CD                        mov r9d, r13d
0089B6CC  44 8B 02                        mov r8d, dword ptr [rdx]
0089B6CF  49 8B CB                        mov rcx, r11
0089B6D2  49 8B 03                        mov rax, qword ptr [r11]
0089B6D5  44 3B 00                        cmp r8d, dword ptr [rax]
0089B6D8  74 0F                           je 0x14089b6e9
0089B6DA  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0089B6DE  48 83 C1 08                     add rcx, 8
0089B6E2  48 85 C0                        test rax, rax
0089B6E5  75 EE                           jne 0x14089b6d5
0089B6E7  EB 0B                           jmp 0x14089b6f4
0089B6E9  8B 40 04                        mov eax, dword ptr [rax + 4]
0089B6EC  39 42 04                        cmp dword ptr [rdx + 4], eax
0089B6EF  75 E9                           jne 0x14089b6da
0089B6F1  41 FF C2                        inc r10d
0089B6F4  48 83 C2 0C                     add rdx, 0xc
0089B6F8  49 83 E9 01                     sub r9, 1
0089B6FC  75 CE                           jne 0x14089b6cc
0089B6FE  45 85 ED                        test r13d, r13d
0089B701  74 3B                           je 0x14089b73e
0089B703  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0089B707  45 8B C5                        mov r8d, r13d
0089B70A  4C 8D 1D 17 07 2B 00            lea r11, [rip + 0x2b0717]
0089B711  44 8B 09                        mov r9d, dword ptr [rcx]
0089B714  49 8B D3                        mov rdx, r11
0089B717  48 8B 05 0A 07 2B 00            mov rax, qword ptr [rip + 0x2b070a]
0089B71E  44 3B 08                        cmp r9d, dword ptr [rax]
0089B721  0F 84 94 00 00 00               je 0x14089b7bb
0089B727  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0089B72B  48 83 C2 08                     add rdx, 8
0089B72F  48 85 C0                        test rax, rax
0089B732  75 EA                           jne 0x14089b71e
0089B734  48 83 C1 0C                     add rcx, 0xc
0089B738  49 83 E8 01                     sub r8, 1
0089B73C  75 D3                           jne 0x14089b711
0089B73E  45 3B D5                        cmp r10d, r13d
0089B741  0F 84 8B FD FF FF               je 0x14089b4d2
0089B747  E9 95 FE FF FF                  jmp 0x14089b5e1
0089B74C  FF 41 20                        inc dword ptr [rcx + 0x20]
0089B74F  48 8B 8A 48 08 00 00            mov rcx, qword ptr [rdx + 0x848]
0089B756  FF 41 1C                        inc dword ptr [rcx + 0x1c]
0089B759  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
0089B75D  66 39 01                        cmp word ptr [rcx], ax
0089B760  0F 82 57 FC FF FF               jb 0x14089b3bd
0089B766  FF 41 20                        inc dword ptr [rcx + 0x20]
0089B769  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
0089B76D  48 8B CF                        mov rcx, rdi
0089B770  48 3B C6                        cmp rax, rsi
0089B773  0F 85 5B 01 00 00               jne 0x14089b8d4
0089B779  E8 D2 70 2E 00                  call 0x140b82850
0089B77E  E9 42 FC FF FF                  jmp 0x14089b3c5
0089B783  FF 41 20                        inc dword ptr [rcx + 0x20]
0089B786  48 8B 8A 58 08 00 00            mov rcx, qword ptr [rdx + 0x858]
0089B78D  FF 41 1C                        inc dword ptr [rcx + 0x1c]
0089B790  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
0089B794  66 39 01                        cmp word ptr [rcx], ax
0089B797  0F 82 D9 FB FF FF               jb 0x14089b376
0089B79D  FF 41 20                        inc dword ptr [rcx + 0x20]
0089B7A0  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
0089B7A4  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
0089B7A8  48 3B C6                        cmp rax, rsi
0089B7AB  0F 85 41 01 00 00               jne 0x14089b8f2
0089B7B1  E8 9A 70 2E 00                  call 0x140b82850
0089B7B6  E9 C4 FB FF FF                  jmp 0x14089b37f
0089B7BB  8B 40 04                        mov eax, dword ptr [rax + 4]
0089B7BE  39 41 04                        cmp dword ptr [rcx + 4], eax
0089B7C1  0F 85 60 FF FF FF               jne 0x14089b727
0089B7C7  41 FF C2                        inc r10d
0089B7CA  E9 65 FF FF FF                  jmp 0x14089b734
0089B7CF  45 33 FF                        xor r15d, r15d
0089B7D2  E9 89 FE FF FF                  jmp 0x14089b660
0089B7D7  41 FF 40 20                     inc dword ptr [r8 + 0x20]
0089B7DB  4C 8B 80 48 08 00 00            mov r8, qword ptr [rax + 0x848]
0089B7E2  41 FF 40 1C                     inc dword ptr [r8 + 0x1c]
0089B7E6  41 0F B7 40 10                  movzx eax, word ptr [r8 + 0x10]
0089B7EB  66 41 39 00                     cmp word ptr [r8], ax
0089B7EF  0F 82 93 FD FF FF               jb 0x14089b588
0089B7F5  41 FF 40 20                     inc dword ptr [r8 + 0x20]
0089B7F9  48 8D 35 50 70 2E 00            lea rsi, [rip + 0x2e7050]
0089B800  49 8B 40 38                     mov rax, qword ptr [r8 + 0x38]
0089B804  E9 64 FF FF FF                  jmp 0x14089b76d
0089B809  41 0F B6 DD                     movzx ebx, r13b
0089B80D  E9 C0 FC FF FF                  jmp 0x14089b4d2
0089B812  BA 53 65 53 75                  mov edx, 0x75536553
0089B817  49 8B C8                        mov rcx, r8
0089B81A  E8 C1 C0 A5 FF                  call 0x1402f78e0
0089B81F  E9 1A FD FF FF                  jmp 0x14089b53e
0089B824  B8 9A 00 00 C0                  mov eax, 0xc000009a
0089B829  E9 99 FB FF FF                  jmp 0x14089b3c7
0089B82E  4D 85 FF                        test r15, r15
0089B831  74 20                           je 0x14089b853
0089B833  49 8B 87 78 04 00 00            mov rax, qword ptr [r15 + 0x478]
0089B83A  F0 FF 88 1C 01 00 00            lock dec dword ptr [rax + 0x11c]
0089B841  48 8B 05 48 C3 5C 00            mov rax, qword ptr [rip + 0x5cc348]
0089B848  48 39 45 AF                     cmp qword ptr [rbp - 0x51], rax
0089B84C  75 01                           jne 0x14089b84f
0089B84E  CC                              int3
0089B84F  48 8B 75 9F                     mov rsi, qword ptr [rbp - 0x61]
0089B853  48 85 F6                        test rsi, rsi
0089B856  0F 84 83 FC FF FF               je 0x14089b4df
0089B85C  48 8B 86 78 04 00 00            mov rax, qword ptr [rsi + 0x478]
0089B863  F0 FF 88 1C 01 00 00            lock dec dword ptr [rax + 0x11c]
0089B86A  48 8B 05 1F C3 5C 00            mov rax, qword ptr [rip + 0x5cc31f]
0089B871  48 39 45 9F                     cmp qword ptr [rbp - 0x61], rax
0089B875  0F 85 64 FC FF FF               jne 0x14089b4df
0089B87B  CC                              int3
0089B87C  E9 5E FC FF FF                  jmp 0x14089b4df
0089B881  48 85 C0                        test rax, rax
0089B884  74 1C                           je 0x14089b8a2
0089B886  48 8B 80 78 04 00 00            mov rax, qword ptr [rax + 0x478]
0089B88D  F0 FF 80 1C 01 00 00            lock inc dword ptr [rax + 0x11c]
0089B894  4C 8B 7D AF                     mov r15, qword ptr [rbp - 0x51]
0089B898  4C 3B 3D F1 C2 5C 00            cmp r15, qword ptr [rip + 0x5cc2f1]
0089B89F  75 01                           jne 0x14089b8a2
0089B8A1  CC                              int3
0089B8A2  48 8B 75 9F                     mov rsi, qword ptr [rbp - 0x61]
0089B8A6  48 85 F6                        test rsi, rsi
0089B8A9  0F 84 A4 FB FF FF               je 0x14089b453
0089B8AF  48 8B 86 78 04 00 00            mov rax, qword ptr [rsi + 0x478]
0089B8B6  F0 FF 80 1C 01 00 00            lock inc dword ptr [rax + 0x11c]
0089B8BD  48 8B 75 9F                     mov rsi, qword ptr [rbp - 0x61]
0089B8C1  48 3B 35 C8 C2 5C 00            cmp rsi, qword ptr [rip + 0x5cc2c8]
0089B8C8  75 01                           jne 0x14089b8cb
0089B8CA  CC                              int3
0089B8CB  4C 8B 7D AF                     mov r15, qword ptr [rbp - 0x51]
0089B8CF  E9 7F FB FF FF                  jmp 0x14089b453
0089B8D4  E8 F7 F1 E1 FF                  call 0x1406baad0
0089B8D9  E9 E7 FA FF FF                  jmp 0x14089b3c5
0089B8DE  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0089B8E3  E9 4F FA FF FF                  jmp 0x14089b337
0089B8E8  44 0F B6 6D 97                  movzx r13d, byte ptr [rbp - 0x69]
0089B8ED  E9 F0 F9 FF FF                  jmp 0x14089b2e2
0089B8F2  E8 D9 F1 E1 FF                  call 0x1406baad0
0089B8F7  E9 83 FA FF FF                  jmp 0x14089b37f
0089B8FC  48 8B CF                        mov rcx, rdi
0089B8FF  E8 E8 3A 23 00                  call 0x140acf3ec
0089B904  41 B8 01 00 00 00               mov r8d, 1
0089B90A  41 B9 44 66 6C 74               mov r9d, 0x746c6644
0089B910  41 0F B6 D0                     movzx edx, r8b
0089B914  48 8B CF                        mov rcx, rdi
0089B917  E8 C8 50 97 FF                  call 0x1402109e4
0089B91C  E9 81 FD FF FF                  jmp 0x14089b6a2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObCreateObjectEx(unsigned __int8 a1, __int64 a2, __int64 a3, unsigned __int8 a4, __int64 a5, unsigned int a6, unsigned int a7, unsigned int a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3F;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int16 v_stack_m76;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int8 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 5698877)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_mA8 = a4;
    v_stack_m60 = a9;
    v_stack_m68 = 0;
    v_stack_m78 = v_xmm0;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), a2, a3, a4);
    if (result != 0) goto loc_0089B294;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120), a2, a3, a4);
    if (result != 0) goto loc_0089B294;
    result = guard_dispatch_icall((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 36)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 44)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2120) + 40)), a4);
    if (result != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36);
        *(unsigned int *)(result) = (unsigned int)(result);
    }
    if (result == 0) goto loc_0089B824;
    v_stack_mC0 = 0;
    v_stack_mC8 = result;
    result = ObpCaptureObjectCreateInformation(a1, a4, a3, v_stack_m78);
    if (sign_flag) goto loc_0089B565;
    if (((*(unsigned int *)(a2 + 72)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result))))) != 0) goto loc_0089B8DE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result)))) & (16)) != 0) goto loc_0089B3EF;
loc_0089B2E2:
    result = (unsigned int)(a7);
    if ((unsigned int)((unsigned int)(a7)) == 0) {
        result = *(unsigned int *)(a2 + 104);
    }
    if ((unsigned int)((unsigned int)(a8)) == 0) {
        a1 = *(unsigned int *)(a2 + 108);
    }
    *(unsigned int *)(result + 20) = (unsigned int)(result);
    v_stack_mB8 = a10;
    *(unsigned int *)(result + 24) = a1;
    v_stack_mC0 = v_stack_m68;
    v_stack_mC8 = (unsigned int)((unsigned int)(a6));
    result = ObpAllocateObject(result, a4, a2, v_stack_m78);
    if (!sign_flag) goto loc_0089B691;
loc_0089B337:
    if (v_stack_m70 == 0) goto loc_0089B37F;
    if (v_stack_m76 != 248) goto loc_0089B598;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2128))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2128) + 16)))) goto loc_0089B783;
loc_0089B376:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2128), v_stack_m70, a2, v_stack_m78);
loc_0089B37F:
    if (*(unsigned __int64 *)(result + 32) == 0) goto loc_0089B39D;
    if ((*(unsigned __int8 *)(result + 16)) <= 1) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 32), a2, a2, v_stack_m78);
    }
    *(unsigned __int64 *)(result + 32) = 0;
loc_0089B39D:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 16)))) goto loc_0089B74C;
loc_0089B3BD:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), result, a2, v_stack_m78);
loc_0089B3C5:
loc_0089B3C7:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, result, a2, v_stack_m78);
    v_rsp = (v_rsp) + (176);
    return result;
loc_0089B3EF:
    v_stack_m98 = v_xmm0;
    v_stack_m88 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 464);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (8)) != 0) goto loc_0089B616;
    v_r15 = 0;
loc_0089B42A:
    v_stack_mA0 = 0;
    result = PsReferencePrimaryTokenWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)(0x75536553ULL), a2, v_stack_m78);
    v_stack_m90 = result;
    if ((*(unsigned int *)(v_rip + 7588814)) != 0) goto loc_0089B881;
loc_0089B453:
    v_stack_m50 = *(unsigned __int64 *)(v_rip + 7595994);
    v_stack_m58 = 1;
    v_stack_m54 = 1;
    v_stack_m48 = 0;
    if (a1 == 0) goto loc_0089B809;
    if (v_stack_mA0 != 0) goto loc_0089B671;
loc_0089B481:
    v_stack_p20 = a1;
    result = SepPrivilegeCheck(result, v_stack_m50, 1, 1);
loc_0089B4A7:
    a1 = v_stack_m90;
    if (v_stack_mA0 != 0) { a1 = v_stack_mA0; }
    result = RtlEqualSid(*(unsigned __int64 *)(v_rip + 6080662), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)), 1, 1);
    if ((unsigned __int8)(result) == 0) goto loc_0089B5A4;
loc_0089B4D2:
    if ((*(unsigned int *)(v_rip + 7588663)) != 0) goto loc_0089B82E;
loc_0089B4DF:
loc_0089B501:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 584)) ^ (v_stack_m90);
    if (a1 >= 15) goto loc_0089B812;
    if (a1 != 15) goto loc_0089B501;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 584);
    if ((*(unsigned int *)(v_rip + 7510761)) != 0) {
        a2 = 0;
        a1 = v_stack_m90 - 48;
        a4 = 0x75536553ULL;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    v_stack_m90 = 0;
    if (v_stack_mA0 != 0) goto loc_0089B682;
loc_0089B553:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0089B8E8;
    goto loc_0089B337;
loc_0089B565:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 16)))) goto loc_0089B7D7;
loc_0089B588:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), result, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), a4);
    goto loc_0089B3C5;
loc_0089B598:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), a4);
    goto loc_0089B37F;
loc_0089B5A4:
    v_stack_m80 = *(unsigned __int64 *)(v_rip + 7595253);
    result = RtlEqualSid(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7595253) + 392), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0089B6B2;
    result = RtlEqualSid(*(unsigned __int64 *)(v_stack_m80 + 384), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0089B6B2;
loc_0089B5E1:
    v_stack_p30 = (unsigned __int8)((unsigned int)(0xC0000061ULL));
    v_stack_p28 = v_stack_m58;
    v_stack_p20 = v_stack_m90;
    a3 = 0;
    result = SepAdtPrivilegedServiceAuditAlarm(v_stack_mA0, v_rip - 9019981, a3, v_stack_mA0);
    goto loc_0089B4D2;
loc_0089B616:
    v_stack_m80 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = PspLockThreadSecurityShared(v_stack_mA0, *(unsigned __int64 *)(gs_base + (0 + 392)), a3, v_stack_mA0);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mA0 + 1440)))) & (8)) == 0) goto loc_0089B7CF;
    v_r15 = (*(unsigned __int64 *)(v_stack_mA0 + 1336)) & (-8);
    result = ObfReferenceObjectWithTag(v_r15, (unsigned int)(0x75536553ULL), a3, v_stack_mA0);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mA0 + 1336))) & (3));
    v_stack_m98 = (unsigned int)(result);
loc_0089B660:
    result = PspUnlockThreadSecurityShared(v_stack_mA0, v_stack_m80, a3, v_stack_mA0);
    goto loc_0089B42A;
loc_0089B671:
    if (v_stack_m98 >= 2) goto loc_0089B481;
    v_rbx = 0;
    goto loc_0089B4A7;
loc_0089B682:
    result = ObfDereferenceObjectWithTag(v_stack_mA0, (unsigned int)(0x75536553ULL), a3, v_stack_mA0);
    goto loc_0089B553;
loc_0089B691:
    if ((*(unsigned int *)(v_rip + 7510392)) != 0) goto loc_0089B8FC;
loc_0089B6A2:
    *(unsigned __int64 *)(v_stack_m60) = v_stack_m68 + 48;
    goto loc_0089B3C5;
loc_0089B6B2:
    v_r10 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m58)) == 0) goto loc_0089B4D2;
loc_0089B6CC:
loc_0089B6D5:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m50)))) == (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7588735))))) goto loc_0089B6E9;
loc_0089B6DA:
    a1 = (*(unsigned __int64 *)(v_rip + 7588735)) + (8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7588735) + 8) != 0) goto loc_0089B6D5;
    goto loc_0089B6F4;
loc_0089B6E9:
    if ((*(unsigned int *)(v_stack_m50 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7588735) + 8) + 4))))) goto loc_0089B6DA;
    v_r10 = (unsigned int)((v_r10) + 1);
loc_0089B6F4:
    a2 = (v_stack_m50) + (12);
    a4 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m58)))) - (1);
    if (condition_is_not_equal) goto loc_0089B6CC;
    if ((unsigned int)((unsigned int)(v_stack_m58)) == 0) goto loc_0089B73E;
loc_0089B711:
loc_0089B71E:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m50)))) == (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 2819850)))) goto loc_0089B7BB;
loc_0089B727:
    a2 = (v_rip + 2819863) + (8);
    if (*(unsigned __int64 *)(v_rip + 2819863 + 8) != 0) goto loc_0089B71E;
loc_0089B734:
    a1 = (v_stack_m50) + (12);
    a3 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m58)))) - (1);
    if (condition_is_not_equal) goto loc_0089B711;
loc_0089B73E:
    if (((unsigned int)(v_r10)) == ((unsigned int)((unsigned int)(v_stack_m58)))) goto loc_0089B4D2;
    goto loc_0089B5E1;
loc_0089B74C:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2120))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2120) + 16)))) goto loc_0089B3BD;
loc_0089B76D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2120) + 56)) != v_stack_mA0) goto loc_0089B8D4;
    result = ExFreePool(v_stack_m68, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m50)));
    goto loc_0089B3C5;
loc_0089B783:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2136))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2136) + 16)))) goto loc_0089B376;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2136) + 56)) != v_stack_mA0) goto loc_0089B8F2;
    result = ExFreePool(v_stack_m70, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m50)));
    goto loc_0089B37F;
loc_0089B7BB:
    if ((*(unsigned int *)(v_stack_m70 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 4))))) goto loc_0089B727;
    v_r10 = (unsigned int)((v_r10) + 1);
    goto loc_0089B734;
loc_0089B7CF:
    v_r15 = 0;
    goto loc_0089B660;
loc_0089B7D7:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 4)) + 2120))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 4)) + 2120) + 16)))) goto loc_0089B588;
    goto loc_0089B76D;
loc_0089B809:
    goto loc_0089B4D2;
loc_0089B812:
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 4)) + 2120), (unsigned int)(0x75536553ULL), *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 4)) + 2120), (unsigned int)(*(unsigned int *)(v_stack_m50)));
    goto loc_0089B53E;
loc_0089B824:
    goto loc_0089B3C7;
loc_0089B82E:
    if (0 == 0) goto loc_0089B853;
    if (v_stack_m90 == (*(unsigned __int64 *)(v_rip + 6079304))) {
    }
loc_0089B853:
    if (v_stack_mA0 == 0) goto loc_0089B4DF;
    if (v_stack_mA0 != (*(unsigned __int64 *)(v_rip + 6079263))) goto loc_0089B4DF;
    goto loc_0089B4DF;
loc_0089B881:
    if (*(unsigned __int64 *)(v_rip + 6079263) == 0) goto loc_0089B8A2;
    if (v_stack_m90 == (*(unsigned __int64 *)(v_rip + 6079217))) {
    }
    if (v_stack_mA0 == 0) goto loc_0089B453;
    if (v_stack_mA0 == (*(unsigned __int64 *)(v_rip + 6079176))) {
    }
    goto loc_0089B453;
loc_0089B8D4:
    result = guard_dispatch_icall(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 4)) + 2120), (unsigned int)(0x75536553ULL), *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 4)) + 2120), (unsigned int)(*(unsigned int *)(v_stack_m50)));
    goto loc_0089B3C5;
loc_0089B8DE:
    goto loc_0089B337;
loc_0089B8E8:
    goto loc_0089B2E2;
loc_0089B8F2:
    result = guard_dispatch_icall(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 4)) + 2120), (unsigned int)(0x75536553ULL), *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 4)) + 2120), (unsigned int)(*(unsigned int *)(v_stack_m50)));
    goto loc_0089B37F;
loc_0089B8FC:
    result = ObpRegisterObject(v_stack_m68, (unsigned int)(0x75536553ULL), *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(result + 4)) + 2120), (unsigned int)(*(unsigned int *)(v_stack_m50)));
    result = ObpPushStackInfo(v_stack_m68, 1, 1, (unsigned int)(0x746C6644ULL));
    goto loc_0089B6A2;
}
```

## 5. (Beta) C Style

```c
int64_t ObCreateObjectEx(uint8_t Arg1, void *Arg2, int64_t Arg3, uint8_t Arg4, uint64_t Arg5, uint32_t Arg6, uint32_t Arg7, uint32_t Arg8, int64_t Arg9, int64_t Arg10)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m3F;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint16_t v_stack_m76;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint8_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x56F53D)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_mA8 = Arg4;
    v_stack_m60 = Arg9;
    v_stack_m68 = 0;
    v_stack_m78 = v_xmm0;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), Arg2, Arg3, Arg4);
    if (result != 0) goto loc_0089B294;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848), Arg2, Arg3, Arg4);
    if (result != 0) goto loc_0089B294;
    result = guard_dispatch_icall((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x24)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x2C)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x848) + 0x28)), Arg4);
    if (result != 0) {
        result = *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24);
        *(uint32_t *)(result) = (uint32_t)(result);
    }
    if (result == 0) goto loc_0089B824;
    v_stack_mC0 = 0;
    v_stack_mC8 = result;
    result = ObpCaptureObjectCreateInformation(Arg1, Arg4, Arg3, v_stack_m78);
    if (sign_flag) goto loc_0089B565;
    if (((*(uint32_t *)(arg2 + 0x48)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result))))) != 0) goto loc_0089B8DE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result)))) & (16)) != 0) goto loc_0089B3EF;
loc_0089B2E2:
    result = (uint32_t)(Arg7);
    if ((uint32_t)((uint32_t)(Arg7)) == 0) {
        result = *(uint32_t *)(arg2 + 0x68);
    }
    if ((uint32_t)((uint32_t)(Arg8)) == 0) {
        Arg1 = *(uint32_t *)(arg2 + 0x6C);
    }
    *(uint32_t *)(result + 0x14) = (uint32_t)(result);
    v_stack_mB8 = Arg10;
    *(uint32_t *)(result + 0x18) = Arg1;
    v_stack_mC0 = v_stack_m68;
    v_stack_mC8 = (uint32_t)((uint32_t)(Arg6));
    result = ObpAllocateObject(result, Arg4, Arg2, v_stack_m78);
    if (!sign_flag) goto loc_0089B691;
loc_0089B337:
    if (v_stack_m70 == 0) goto loc_0089B37F;
    if (v_stack_m76 != 248) goto loc_0089B598;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x850))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x850) + 0x10)))) goto loc_0089B783;
loc_0089B376:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x850), v_stack_m70, Arg2, v_stack_m78);
loc_0089B37F:
    if (*(uint64_t *)(result + 0x20) == 0) goto loc_0089B39D;
    if ((*(uint8_t *)(result + 0x10)) <= 1) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(result + 0x20), Arg2, Arg2, v_stack_m78);
    }
    *(uint64_t *)(result + 0x20) = 0;
loc_0089B39D:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x10)))) goto loc_0089B74C;
loc_0089B3BD:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), result, Arg2, v_stack_m78);
loc_0089B3C5:
loc_0089B3C7:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, result, Arg2, v_stack_m78);
    local_rsp = (local_rsp) + (176);
    return result;
loc_0089B3EF:
    v_stack_m98 = v_xmm0;
    v_stack_m88 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1D0);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (8)) != 0) goto loc_0089B616;
    local_r15 = 0;
loc_0089B42A:
    v_stack_mA0 = 0;
    result = PsReferencePrimaryTokenWithTag(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)(0x75536553ULL), Arg2, v_stack_m78);
    v_stack_m90 = result;
    if ((*(uint32_t *)(v_rip + 0x73CBCE)) != 0) goto loc_0089B881;
loc_0089B453:
    v_stack_m50 = *(uint64_t *)(v_rip + 0x73E7DA);
    v_stack_m58 = 1;
    v_stack_m54 = 1;
    v_stack_m48 = 0;
    if (Arg1 == 0) goto loc_0089B809;
    if (v_stack_mA0 != 0) goto loc_0089B671;
loc_0089B481:
    v_stack_p20 = Arg1;
    result = SepPrivilegeCheck(result, v_stack_m50, 1, 1);
loc_0089B4A7:
    Arg1 = v_stack_m90;
    if (v_stack_mA0 != 0) { Arg1 = v_stack_mA0; }
    result = RtlEqualSid(*(uint64_t *)(v_rip + 0x5CC896), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x98)), 1, 1);
    if ((uint8_t)(result) == 0) goto loc_0089B5A4;
loc_0089B4D2:
    if ((*(uint32_t *)(v_rip + 0x73CB37)) != 0) goto loc_0089B82E;
loc_0089B4DF:
loc_0089B501:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x248)) ^ (v_stack_m90);
    if (Arg1 >= 15) goto loc_0089B812;
    if (Arg1 != 15) goto loc_0089B501;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x248);
    if ((*(uint32_t *)(v_rip + 0x729AE9)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m90 - 48;
        Arg4 = 0x75536553ULL;
        Arg3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m90 = 0;
    if (v_stack_mA0 != 0) goto loc_0089B682;
loc_0089B553:
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0089B8E8;
    goto loc_0089B337;
loc_0089B565:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x10)))) goto loc_0089B7D7;
loc_0089B588:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), result, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), Arg4);
    goto loc_0089B3C5;
loc_0089B598:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), Arg4);
    goto loc_0089B37F;
loc_0089B5A4:
    v_stack_m80 = *(uint64_t *)(v_rip + 0x73E4F5);
    result = RtlEqualSid(*(uint64_t *)(*(uint64_t *)(v_rip + 0x73E4F5) + 0x188), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x98)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0089B6B2;
    result = RtlEqualSid(*(uint64_t *)(v_stack_m80 + 0x180), *(uint64_t *)(*(uint64_t *)(Arg1 + 0x98)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0089B6B2;
loc_0089B5E1:
    v_stack_p30 = (uint8_t)((uint32_t)(0xC0000061ULL));
    v_stack_p28 = v_stack_m58;
    v_stack_p20 = v_stack_m90;
    Arg3 = 0;
    result = SepAdtPrivilegedServiceAuditAlarm(v_stack_mA0, v_rip - 9019981, Arg3, v_stack_mA0);
    goto loc_0089B4D2;
loc_0089B616:
    v_stack_m80 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = PspLockThreadSecurityShared(v_stack_mA0, *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, v_stack_mA0);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x5A0)))) & (8)) == 0) goto loc_0089B7CF;
    local_r15 = (*(uint64_t *)(v_stack_mA0 + 0x538)) & (-8);
    result = ObfReferenceObjectWithTag(local_r15, (uint32_t)(0x75536553ULL), Arg3, v_stack_mA0);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x538))) & (3));
    v_stack_m98 = (uint32_t)(result);
loc_0089B660:
    result = PspUnlockThreadSecurityShared(v_stack_mA0, v_stack_m80, Arg3, v_stack_mA0);
    goto loc_0089B42A;
loc_0089B671:
    if (v_stack_m98 >= 2) goto loc_0089B481;
    local_rbx = 0;
    goto loc_0089B4A7;
loc_0089B682:
    result = ObfDereferenceObjectWithTag(v_stack_mA0, (uint32_t)(0x75536553ULL), Arg3, v_stack_mA0);
    goto loc_0089B553;
loc_0089B691:
    if ((*(uint32_t *)(v_rip + 0x729978)) != 0) goto loc_0089B8FC;
loc_0089B6A2:
    *(uint64_t *)(v_stack_m60) = v_stack_m68 + 48;
    goto loc_0089B3C5;
loc_0089B6B2:
    local_r10 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m58)) == 0) goto loc_0089B4D2;
loc_0089B6CC:
loc_0089B6D5:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m50)))) == (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x73CB7F))))) goto loc_0089B6E9;
loc_0089B6DA:
    Arg1 = (*(uint64_t *)(v_rip + 0x73CB7F)) + (8);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x73CB7F) + 0x8) != 0) goto loc_0089B6D5;
    goto loc_0089B6F4;
loc_0089B6E9:
    if ((*(uint32_t *)(v_stack_m50 + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x73CB7F) + 0x8) + 0x4))))) goto loc_0089B6DA;
    local_r10 = (uint32_t)((local_r10) + 1);
loc_0089B6F4:
    Arg2 = (v_stack_m50) + (12);
    Arg4 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m58)))) - (1);
    if (condition_is_not_equal) goto loc_0089B6CC;
    if ((uint32_t)((uint32_t)(v_stack_m58)) == 0) goto loc_0089B73E;
loc_0089B711:
loc_0089B71E:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m50)))) == (*(uint32_t *)(*(uint64_t *)(v_rip + 0x2B070A)))) goto loc_0089B7BB;
loc_0089B727:
    Arg2 = (v_rip + 2819863) + (8);
    if (*(uint64_t *)(v_rip + 0x2B0717 + 0x8) != 0) goto loc_0089B71E;
loc_0089B734:
    Arg1 = (v_stack_m50) + (12);
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m58)))) - (1);
    if (condition_is_not_equal) goto loc_0089B711;
loc_0089B73E:
    if (((uint32_t)(local_r10)) == ((uint32_t)((uint32_t)(v_stack_m58)))) goto loc_0089B4D2;
    goto loc_0089B5E1;
loc_0089B74C:
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x848))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x848) + 0x10)))) goto loc_0089B3BD;
loc_0089B76D:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x848) + 0x38)) != v_stack_mA0) goto loc_0089B8D4;
    result = ExFreePool(v_stack_m68, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m50)));
    goto loc_0089B3C5;
loc_0089B783:
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x858))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x858) + 0x10)))) goto loc_0089B376;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x858) + 0x38)) != v_stack_mA0) goto loc_0089B8F2;
    result = ExFreePool(v_stack_m70, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m50)));
    goto loc_0089B37F;
loc_0089B7BB:
    if ((*(uint32_t *)(v_stack_m70 + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))))) goto loc_0089B727;
    local_r10 = (uint32_t)((local_r10) + 1);
    goto loc_0089B734;
loc_0089B7CF:
    local_r15 = 0;
    goto loc_0089B660;
loc_0089B7D7:
    if ((*(uint16_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x4)) + 0x848))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x4)) + 0x848) + 0x10)))) goto loc_0089B588;
    goto loc_0089B76D;
loc_0089B809:
    goto loc_0089B4D2;
loc_0089B812:
    result = ObfDereferenceObjectWithTag(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x4)) + 0x848), (uint32_t)(0x75536553ULL), *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x4)) + 0x848), (uint32_t)(*(uint32_t *)(v_stack_m50)));
    goto loc_0089B53E;
loc_0089B824:
    goto loc_0089B3C7;
loc_0089B82E:
    if (0 == 0) goto loc_0089B853;
    if (v_stack_m90 == (*(uint64_t *)(v_rip + 0x5CC348))) {
    }
loc_0089B853:
    if (v_stack_mA0 == 0) goto loc_0089B4DF;
    if (v_stack_mA0 != (*(uint64_t *)(v_rip + 0x5CC31F))) goto loc_0089B4DF;
    goto loc_0089B4DF;
loc_0089B881:
    if (*(uint64_t *)(v_rip + 0x5CC31F) == 0) goto loc_0089B8A2;
    if (v_stack_m90 == (*(uint64_t *)(v_rip + 0x5CC2F1))) {
    }
    if (v_stack_mA0 == 0) goto loc_0089B453;
    if (v_stack_mA0 == (*(uint64_t *)(v_rip + 0x5CC2C8))) {
    }
    goto loc_0089B453;
loc_0089B8D4:
    result = guard_dispatch_icall(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x4)) + 0x848), (uint32_t)(0x75536553ULL), *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x4)) + 0x848), (uint32_t)(*(uint32_t *)(v_stack_m50)));
    goto loc_0089B3C5;
loc_0089B8DE:
    goto loc_0089B337;
loc_0089B8E8:
    goto loc_0089B2E2;
loc_0089B8F2:
    result = guard_dispatch_icall(*(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x4)) + 0x848), (uint32_t)(0x75536553ULL), *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x4)) + 0x848), (uint32_t)(*(uint32_t *)(v_stack_m50)));
    goto loc_0089B37F;
loc_0089B8FC:
    result = ObpRegisterObject(v_stack_m68, (uint32_t)(0x75536553ULL), *(uint64_t *)((uint32_t)(*(uint32_t *)(result + 0x4)) + 0x848), (uint32_t)(*(uint32_t *)(v_stack_m50)));
    result = ObpPushStackInfo(v_stack_m68, 1, 1, (uint32_t)(0x746C6644ULL));
    goto loc_0089B6A2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x48` | `32` | `R` |
| `Arg2` | `+ 0x68` | `32` | `R` |
| `Arg2` | `+ 0x6C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0089B1E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
