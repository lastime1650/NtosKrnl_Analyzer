# PipCallDriverAddDevice

- RVA: `0x00A272E0`–`0x00A27B49` (길이 `2,153` bytes)
- VA: `0x0000000140A272E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000ABFA0`
- 디코드: `476`개 명령, `2,153/2,153` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00A27351` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A273C5` → [_CmOpenDeviceRegKey](../8E/_CmOpenDeviceRegKey_function_008EE540.md) (function, `0x008EE540`)
- `0x00A2744C` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A274D6` → [PnpGetObjectProperty](../8E/PnpGetObjectProperty_function_008E2180.md) (function, `0x008E2180`)
- `0x00A27538` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00A27586` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00A275BE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A275DE` → [PnpGetStableSystemBootTime](PnpGetStableSystemBootTime_function_00A27C10.md) (function, `0x00A27C10`)
- `0x00A2763A` → [PiDmaGuardProcessPreAddDevice](PiDmaGuardProcessPreAddDevice_function_00A27B50.md) (function, `0x00A27B50`)
- `0x00A27655` → [IoGetAttachedDeviceReferenceWithTag](../../text/27/IoGetAttachedDeviceReferenceWithTag_function_00273B84.md) (function, `0x00273B84`)
- `0x00A276B2` → [IovUtilMarkStack](../../text/4B/IovUtilMarkStack_function_004B7734.md) (function, `0x004B7734`)
- `0x00A276CD` → [PipChangeDeviceObjectFromRegistryProperties](../99/PipChangeDeviceObjectFromRegistryProperties_function_00994FD0.md) (function, `0x00994FD0`)
- `0x00A276E4` → [PnpRequestDeviceRemoval](../8F/PnpRequestDeviceRemoval_function_008FC294.md) (function, `0x008FC294`)
- `0x00A27705` → [PnpCallAddDevice](../8F/PnpCallAddDevice_function_008FC164.md) (function, `0x008FC164`)
- `0x00A27752` → [IopQueryLegacyBusInformation](IopQueryLegacyBusInformation_function_00A28078.md) (function, `0x00A28078`)
- `0x00A27767` → [IopInsertLegacyBusDeviceNode](IopInsertLegacyBusDeviceNode_function_00A28154.md) (function, `0x00A28154`)
- `0x00A27776` → [PnpRaiseNtPlugPlayDevicePropertyChangeEvent](../8F/PnpRaiseNtPlugPlayDevicePropertyChangeEvent_function_008F7D80.md) (function, `0x008F7D80`)
- `0x00A2778A` → [PiProcessDriversLoadedOnSecureDevice](PiProcessDriversLoadedOnSecureDevice_function_00A27F9C.md) (function, `0x00A27F9C`)
- `0x00A277B3` → [PipDmgEnforceEnumerationPolicy](../73/PipDmgEnforceEnumerationPolicy_function_0073BEB4.md) (function, `0x0073BEB4`)
- `0x00A277D5` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (function, `0x00470708`)
- `0x00A27831` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A27857` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A2789D` → [PnpCallDriverQueryServiceHelper](../99/PnpCallDriverQueryServiceHelper_function_00995FB0.md) (function, `0x00995FB0`)
- `0x00A27904` → [PipClearDevNodeProblem](PipClearDevNodeProblem_function_00A27C8C.md) (function, `0x00A27C8C`)
- `0x00A27941` → [PipSetDevNodeProblem](../8F/PipSetDevNodeProblem_function_008FDE0C.md) (function, `0x008FDE0C`)
- `0x00A279B1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A27A20` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A27A65` → [PnpSetObjectProperty](../8F/PnpSetObjectProperty_function_008F66E8.md) (function, `0x008F66E8`)
- `0x00A27A8F` → [PipSetDevNodeFlags](../8F/PipSetDevNodeFlags_function_008FC048.md) (function, `0x008FC048`)
- `0x00A27AA9` → [IoGetAttachedDeviceReferenceWithTag](../../text/27/IoGetAttachedDeviceReferenceWithTag_function_00273B84.md) (function, `0x00273B84`)
- `0x00A27AD1` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (function, `0x00470708`)
- `0x00A27AF7` → [IovUtilMarkStack](../../text/4B/IovUtilMarkStack_function_004B7734.md) (function, `0x004B7734`)
- `0x00A27B11` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A27B1B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A27B2D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00A27B3F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [PiProcessAddBootDevices](../72/PiProcessAddBootDevices_function_0072D434.md) at `0x0072D48F`
- [PipProcessDevNodeTree](../8F/PipProcessDevNodeTree_function_008F9068.md) at `0x008F955B`

### Static image references
- `0x00A272FC` → RVA `0x00E0A740` (`.data`; read)
- `0x00A273AD` → RVA `0x00E66398` (`.data`; read)
- `0x00A273F7` → RVA `0x00E66320` (`.data`; read)
- `0x00A2743B` → RVA `0x00019F28` (`.rdata`; read)
- `0x00A274C5` → RVA `0x00019F10` (`.rdata`; read)
- `0x00A2760C` → RVA `0x00E0A9E0` (`.data`; read)
- `0x00A27795` → RVA `0x00F8A9AC` (`.data`; read)
- `0x00A2786D` → RVA `0x00014170` (`.rdata`; read)
- `0x00A27A07` → RVA `0x00027C68` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x00A27351` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A275BE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A27655` → [IoGetAttachedDeviceReferenceWithTag](../../text/27/IoGetAttachedDeviceReferenceWithTag_function_00273B84.md) (`PAGE` → `.text`)
  - `0x00A276B2` → [IovUtilMarkStack](../../text/4B/IovUtilMarkStack_function_004B7734.md) (`PAGE` → `.text`)
  - `0x00A277D5` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (`PAGE` → `.text`)
  - `0x00A27831` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A27857` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A279B1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A27AA9` → [IoGetAttachedDeviceReferenceWithTag](../../text/27/IoGetAttachedDeviceReferenceWithTag_function_00273B84.md) (`PAGE` → `.text`)
  - `0x00A27AD1` → [PipSetDevNodeState](../../text/47/PipSetDevNodeState_function_00470708.md) (`PAGE` → `.text`)
  - `0x00A27AF7` → [IovUtilMarkStack](../../text/4B/IovUtilMarkStack_function_004B7734.md) (`PAGE` → `.text`)
  - `0x00A27B11` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A27B1B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A27B2D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00A27B3F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **10**
  - `0x00A273E4` → [sub_00B3807C](../B3/Unknown_function_00B3807C.md) (`tail-transfer`)
  - `0x00A2753F` → [sub_00B3807C + 0x81](../B3/Unknown_function_00B3807C.md) (`tail-transfer`)
  - `0x00A275CA` → [sub_00B3807C + 0x1C8](../B3/Unknown_function_00B3807C.md) (`tail-transfer`)
  - `0x00A27684` → [sub_00B3807C + 0x5D3](../B3/Unknown_function_00B3807C.md) (`tail-transfer`)
  - `0x00A277BF` → [sub_00B3807C + 0x68B](../B3/Unknown_function_00B3807C.md) (`tail-transfer`)
  - `0x00A278C9` → [sub_00B3807C + 0x477](../B3/Unknown_function_00B3807C.md) (`tail-transfer`)
  - `0x00A2791D` → [sub_00B3807C + 0x4E3](../B3/Unknown_function_00B3807C.md) (`tail-transfer`)
  - `0x00A27923` → [sub_00B3807C + 0x547](../B3/Unknown_function_00B3807C.md) (`tail-transfer`)
  - `0x00A2794D` → [sub_00B3807C + 0x547](../B3/Unknown_function_00B3807C.md) (`tail-transfer`)
  - `0x00A27992` → [sub_00B3807C + 0x68B](../B3/Unknown_function_00B3807C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A272E0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00A272E5  55                              push rbp
00A272E6  56                              push rsi
00A272E7  57                              push rdi
00A272E8  41 54                           push r12
00A272EA  41 55                           push r13
00A272EC  41 56                           push r14
00A272EE  41 57                           push r15
00A272F0  48 8D 6C 24 80                  lea rbp, [rsp - 0x80]
00A272F5  48 81 EC 80 01 00 00            sub rsp, 0x180
00A272FC  48 8B 05 3D 34 3E 00            mov rax, qword ptr [rip + 0x3e343d]
00A27303  48 33 C4                        xor rax, rsp
00A27306  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00A2730A  45 33 F6                        xor r14d, r14d
00A2730D  48 8B F2                        mov rsi, rdx
00A27310  48 8B F9                        mov rdi, rcx
00A27313  44 88 74 24 68                  mov byte ptr [rsp + 0x68], r14b
00A27318  33 D2                           xor edx, edx
00A2731A  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
00A2731E  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00A27322  44 89 74 24 6C                  mov dword ptr [rsp + 0x6c], r14d
00A27327  45 8D 46 40                     lea r8d, [r14 + 0x40]
00A2732B  44 89 75 80                     mov dword ptr [rbp - 0x80], r14d
00A2732F  45 8A E6                        mov r12b, r14b
00A27332  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
00A27337  45 8A EE                        mov r13b, r14b
00A2733A  66 44 89 75 84                  mov word ptr [rbp - 0x7c], r14w
00A2733F  4C 89 75 D0                     mov qword ptr [rbp - 0x30], r14
00A27343  44 89 74 24 60                  mov dword ptr [rsp + 0x60], r14d
00A27348  44 89 74 24 70                  mov dword ptr [rsp + 0x70], r14d
00A2734D  44 89 75 A0                     mov dword ptr [rbp - 0x60], r14d
00A27351  E8 EA F8 C9 FF                  call 0x1406c6c40
00A27356  41 8D 46 06                     lea eax, [r14 + 6]
00A2735A  0F 57 C0                        xorps xmm0, xmm0
00A2735D  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00A27361  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00A27365  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
00A2736A  4C 89 75 B0                     mov qword ptr [rbp - 0x50], r14
00A2736E  44 89 75 88                     mov dword ptr [rbp - 0x78], r14d
00A27372  66 44 89 75 20                  mov word ptr [rbp + 0x20], r14w
00A27377  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
00A2737B  4C 89 75 A8                     mov qword ptr [rbp - 0x58], r14
00A2737F  4C 89 75 B8                     mov qword ptr [rbp - 0x48], r14
00A27383  44 38 B7 B0 02 00 00            cmp byte ptr [rdi + 0x2b0], r14b
00A2738A  0F 85 F3 05 00 00               jne 0x140a27983
00A27390  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A27394  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00A27399  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00A2739E  45 33 C9                        xor r9d, r9d
00A273A1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A273A6  44 88 B7 B0 02 00 00            mov byte ptr [rdi + 0x2b0], r14b
00A273AD  48 8B 0D E4 EF 43 00            mov rcx, qword ptr [rip + 0x43efe4]
00A273B4  45 8D 41 10                     lea r8d, [r9 + 0x10]
00A273B8  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
00A273BD  C7 44 24 20 19 00 02 00         mov dword ptr [rsp + 0x20], 0x20019
00A273C5  E8 76 71 EC FF                  call 0x1408ee540
00A273CA  8B D8                           mov ebx, eax
00A273CC  85 C0                           test eax, eax
00A273CE  0F 88 E6 03 00 00               js 0x140a277ba
00A273D4  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
00A273D8  BB 04 00 00 00                  mov ebx, 4
00A273DD  F7 40 30 00 00 00 02            test dword ptr [rax + 0x30], 0x2000000
00A273E4  0F 85 92 0C 11 00               jne 0x140b3807c
00A273EA  83 BF 94 02 00 00 FF            cmp dword ptr [rdi + 0x294], -1
00A273F1  0F 85 8F 00 00 00               jne 0x140a27486
00A273F7  4C 39 35 22 EF 43 00            cmp qword ptr [rip + 0x43ef22], r14
00A273FE  74 59                           je 0x140a27459
00A27400  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
00A27405  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00A2740A  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A2740E  41 B8 01 00 00 00               mov r8d, 1
00A27414  48 8B 0D 7D EF 43 00            mov rcx, qword ptr [rip + 0x43ef7d]
00A2741B  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
00A27420  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A27425  48 8D 45 80                     lea rax, [rbp - 0x80]
00A27429  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00A2742D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A27432  48 8D 45 88                     lea rax, [rbp - 0x78]
00A27436  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A2743B  48 8D 05 E6 2A 5F FF            lea rax, [rip - 0xa0d51a]
00A27442  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A27447  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00A2744C  E8 2F AD EB FF                  call 0x1408e2180
00A27451  85 C0                           test eax, eax
00A27453  0F 89 3E 05 00 00               jns 0x140a27997
00A27459  8B 87 94 02 00 00               mov eax, dword ptr [rdi + 0x294]
00A2745F  83 F8 FF                        cmp eax, -1
00A27462  75 19                           jne 0x140a2747d
00A27464  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00A27468  48 85 C0                        test rax, rax
00A2746B  0F 84 5C 05 00 00               je 0x140a279cd
00A27471  8B 80 94 02 00 00               mov eax, dword ptr [rax + 0x294]
00A27477  89 87 94 02 00 00               mov dword ptr [rdi + 0x294], eax
00A2747D  83 F8 FE                        cmp eax, -2
00A27480  0F 85 56 05 00 00               jne 0x140a279dc
00A27486  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
00A2748B  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00A27490  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A27494  41 B8 01 00 00 00               mov r8d, 1
00A2749A  48 8B 0D F7 EE 43 00            mov rcx, qword ptr [rip + 0x43eef7]
00A274A1  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
00A274A6  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A274AB  48 8D 45 D0                     lea rax, [rbp - 0x30]
00A274AF  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
00A274B7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A274BC  48 8D 45 88                     lea rax, [rbp - 0x78]
00A274C0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A274C5  48 8D 05 44 2A 5F FF            lea rax, [rip - 0xa0d5bc]
00A274CC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A274D1  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00A274D6  E8 A5 AC EB FF                  call 0x1408e2180
00A274DB  B9 00 00 00 80                  mov ecx, 0x80000000
00A274E0  8B D8                           mov ebx, eax
00A274E2  03 C1                           add eax, ecx
00A274E4  85 C1                           test ecx, eax
00A274E6  0F 85 EE 00 00 00               jne 0x140a275da
00A274EC  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
00A274F2  0F 84 E2 00 00 00               je 0x140a275da
00A274F8  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00A274FD  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A27502  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A27506  41 B9 09 00 00 00               mov r9d, 9
00A2750C  48 8B 0D 85 EE 43 00            mov rcx, qword ptr [rip + 0x43ee85]
00A27513  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00A27518  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A2751D  48 8D 45 20                     lea rax, [rbp + 0x20]
00A27521  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A27526  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00A2752B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A27530  C7 44 24 60 4E 00 00 00         mov dword ptr [rsp + 0x60], 0x4e
00A27538  E8 33 63 EC FF                  call 0x1408ed870
00A2753D  85 C0                           test eax, eax
00A2753F  0F 89 B8 0B 11 00               jns 0x140b380fd
00A27545  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
00A2754A  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A2754F  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A27553  41 B9 0B 00 00 00               mov r9d, 0xb
00A27559  48 8B 0D 38 EE 43 00            mov rcx, qword ptr [rip + 0x43ee38]
00A27560  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00A27565  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A2756A  48 8D 44 24 6C                  lea rax, [rsp + 0x6c]
00A2756F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A27574  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00A27579  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A2757E  C7 44 24 60 04 00 00 00         mov dword ptr [rsp + 0x60], 4
00A27586  E8 E5 62 EC FF                  call 0x1408ed870
00A2758B  85 C0                           test eax, eax
00A2758D  0F 89 DC 04 00 00               jns 0x140a27a6f
00A27593  44 89 74 24 6C                  mov dword ptr [rsp + 0x6c], r14d
00A27598  BA 00 02 00 00                  mov edx, 0x200
00A2759D  48 89 7D E0                     mov qword ptr [rbp - 0x20], rdi
00A275A1  41 8B DE                        mov ebx, r14d
00A275A4  48 89 75 E8                     mov qword ptr [rbp - 0x18], rsi
00A275A8  41 BE 50 70 65 6E               mov r14d, 0x6e657050
00A275AE  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
00A275B2  41 BF 00 01 00 00               mov r15d, 0x100
00A275B8  45 8B C6                        mov r8d, r14d
00A275BB  41 8B CF                        mov ecx, r15d
00A275BE  E8 2D AB 15 00                  call 0x140b820f0
00A275C3  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00A275C7  48 85 C0                        test rax, rax
00A275CA  0F 85 74 0C 11 00               jne 0x140b38244
00A275D0  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00A275D5  E9 FA 02 00 00                  jmp 0x140a278d4
00A275DA  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00A275DE  E8 2D 06 00 00                  call 0x140a27c10
00A275E3  85 C0                           test eax, eax
00A275E5  0F 88 0D FF FF FF               js 0x140a274f8
00A275EB  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
00A275F1  0F 84 33 04 00 00               je 0x140a27a2a
00A275F7  83 7D 88 10                     cmp dword ptr [rbp - 0x78], 0x10
00A275FB  0F 85 29 04 00 00               jne 0x140a27a2a
00A27601  83 7C 24 64 08                  cmp dword ptr [rsp + 0x64], 8
00A27606  0F 85 1E 04 00 00               jne 0x140a27a2a
00A2760C  44 38 35 CD 33 3E 00            cmp byte ptr [rip + 0x3e33cd], r14b
00A27613  0F 85 11 04 00 00               jne 0x140a27a2a
00A27619  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00A2761D  48 39 45 B0                     cmp qword ptr [rbp - 0x50], rax
00A27621  0F 85 03 04 00 00               jne 0x140a27a2a
00A27627  BB 01 00 00 C0                  mov ebx, 0xc0000001
00A2762C  E9 89 01 00 00                  jmp 0x140a277ba
00A27631  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00A27636  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00A2763A  E8 11 05 00 00                  call 0x140a27b50
00A2763F  8B D8                           mov ebx, eax
00A27641  85 C0                           test eax, eax
00A27643  0F 88 71 01 00 00               js 0x140a277ba
00A27649  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A2764D  BA 50 6E 70 65                  mov edx, 0x65706e50
00A27652  45 33 F6                        xor r14d, r14d
00A27655  E8 2A C5 84 FF                  call 0x140273b84
00A2765A  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00A2765E  32 DB                           xor bl, bl
00A27660  80 FB 06                        cmp bl, 6
00A27663  73 29                           jae 0x140a2768e
00A27665  80 FB 03                        cmp bl, 3
00A27668  0F 84 32 04 00 00               je 0x140a27aa0
00A2766E  4C 8B 65 B8                     mov r12, qword ptr [rbp - 0x48]
00A27672  0F B6 CB                        movzx ecx, bl
00A27675  4C 8B 7C CD F0                  mov r15, qword ptr [rbp + rcx*8 - 0x10]
00A2767A  49 8B F7                        mov rsi, r15
00A2767D  48 85 F6                        test rsi, rsi
00A27680  75 71                           jne 0x140a276f3
00A27682  84 DB                           test bl, bl
00A27684  0F 84 C5 0F 11 00               je 0x140b3864f
00A2768A  FE C3                           inc bl
00A2768C  EB D2                           jmp 0x140a27660
00A2768E  4D 85 F6                        test r14, r14
00A27691  0F 84 98 00 00 00               je 0x140a2772f
00A27697  45 84 ED                        test r13b, r13b
00A2769A  0F 85 8F 00 00 00               jne 0x140a2772f
00A276A0  45 33 C9                        xor r9d, r9d
00A276A3  4C 8B 7D A8                     mov r15, qword ptr [rbp - 0x58]
00A276A7  4D 8B C6                        mov r8, r14
00A276AA  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A276AE  49 8B 57 18                     mov rdx, qword ptr [r15 + 0x18]
00A276B2  E8 7D 00 A9 FF                  call 0x1404b7734
00A276B7  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00A276BC  4C 8D 45 20                     lea r8, [rbp + 0x20]
00A276C0  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A276C4  4C 8B 4D 98                     mov r9, qword ptr [rbp - 0x68]
00A276C8  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
00A276CD  E8 FE D8 F6 FF                  call 0x140994fd0
00A276D2  85 C0                           test eax, eax
00A276D4  79 64                           jns 0x140a2773a
00A276D6  44 8B C8                        mov r9d, eax
00A276D9  41 B8 32 00 00 00               mov r8d, 0x32
00A276DF  33 D2                           xor edx, edx
00A276E1  48 8B CF                        mov rcx, rdi
00A276E4  E8 AB 4B ED FF                  call 0x1408fc294
00A276E9  BB CE 02 00 C0                  mov ebx, 0xc00002ce
00A276EE  E9 C7 00 00 00                  jmp 0x140a277ba
00A276F3  48 8B 16                        mov rdx, qword ptr [rsi]
00A276F6  48 8B CF                        mov rcx, rdi
00A276F9  44 0F B6 CB                     movzx r9d, bl
00A276FD  48 8B 42 30                     mov rax, qword ptr [rdx + 0x30]
00A27701  4C 8B 40 08                     mov r8, qword ptr [rax + 8]
00A27705  E8 5A 4A ED FF                  call 0x1408fc164
00A2770A  48 8B 0E                        mov rcx, qword ptr [rsi]
00A2770D  44 8B D8                        mov r11d, eax
00A27710  0F BA 69 10 0A                  bts dword ptr [rcx + 0x10], 0xa
00A27715  85 C0                           test eax, eax
00A27717  0F 89 A7 00 00 00               jns 0x140a277c4
00A2771D  80 FB 03                        cmp bl, 3
00A27720  0F 84 BF 03 00 00               je 0x140a27ae5
00A27726  48 8B 76 08                     mov rsi, qword ptr [rsi + 8]
00A2772A  E9 4E FF FF FF                  jmp 0x140a2767d
00A2772F  41 B9 01 00 00 00               mov r9d, 1
00A27735  E9 69 FF FF FF                  jmp 0x140a276a3
00A2773A  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A2773E  48 8D 9F C4 01 00 00            lea rbx, [rdi + 0x1c4]
00A27745  48 8D B7 C0 01 00 00            lea rsi, [rdi + 0x1c0]
00A2774C  4C 8B CB                        mov r9, rbx
00A2774F  4C 8B C6                        mov r8, rsi
00A27752  E8 21 09 00 00                  call 0x140a28078
00A27757  85 C0                           test eax, eax
00A27759  0F 88 80 00 00 00               js 0x140a277df
00A2775F  44 8B 03                        mov r8d, dword ptr [rbx]
00A27762  48 8B CF                        mov rcx, rdi
00A27765  8B 16                           mov edx, dword ptr [rsi]
00A27767  E8 E8 09 00 00                  call 0x140a28154
00A2776C  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A27770  41 B8 17 00 00 00               mov r8d, 0x17
00A27776  E8 05 06 ED FF                  call 0x1408f7d80
00A2777B  F7 87 30 02 00 00 00 00 10 00   test dword ptr [rdi + 0x230], 0x100000
00A27785  74 0E                           je 0x140a27795
00A27787  48 8B CF                        mov rcx, rdi
00A2778A  E8 0D 08 00 00                  call 0x140a27f9c
00A2778F  8B D8                           mov ebx, eax
00A27791  85 C0                           test eax, eax
00A27793  78 25                           js 0x140a277ba
00A27795  83 3D 10 32 56 00 00            cmp dword ptr [rip + 0x563210], 0
00A2779C  0F 84 F7 02 00 00               je 0x140a27a99
00A277A2  48 83 BF D0 02 00 00 00         cmp qword ptr [rdi + 0x2d0], 0
00A277AA  0F 84 E9 02 00 00               je 0x140a27a99
00A277B0  48 8B CF                        mov rcx, rdi
00A277B3  E8 FC 46 D1 FF                  call 0x14073beb4
00A277B8  8B D8                           mov ebx, eax
00A277BA  B8 06 00 00 00                  mov eax, 6
00A277BF  E9 43 0F 11 00                  jmp 0x140b38707
00A277C4  80 FB 03                        cmp bl, 3
00A277C7  0F 84 0E 03 00 00               je 0x140a27adb
00A277CD  BA 05 03 00 00                  mov edx, 0x305
00A277D2  48 8B CF                        mov rcx, rdi
00A277D5  E8 2E 8F A4 FF                  call 0x140470708
00A277DA  E9 47 FF FF FF                  jmp 0x140a27726
00A277DF  83 0E FF                        or dword ptr [rsi], 0xffffffff
00A277E2  C7 03 F0 FF FF FF               mov dword ptr [rbx], 0xfffffff0
00A277E8  EB 82                           jmp 0x140a2776c
00A277EA  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00A277EF  4C 8B 7D A8                     mov r15, qword ptr [rbp - 0x58]
00A277F3  48 85 C9                        test rcx, rcx
00A277F6  0F 85 15 03 00 00               jne 0x140a27b11
00A277FC  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00A27800  48 85 C9                        test rcx, rcx
00A27803  0F 85 12 03 00 00               jne 0x140a27b1b
00A27809  4D 85 FF                        test r15, r15
00A2780C  0F 85 13 03 00 00               jne 0x140a27b25
00A27812  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00A27816  48 85 C0                        test rax, rax
00A27819  0F 85 18 03 00 00               jne 0x140a27b37
00A2781F  48 8B 75 90                     mov rsi, qword ptr [rbp - 0x70]
00A27823  48 85 F6                        test rsi, rsi
00A27826  75 2A                           jne 0x140a27852
00A27828  8B C3                           mov eax, ebx
00A2782A  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
00A2782E  48 33 CC                        xor rcx, rsp
00A27831  E8 0A 4E C8 FF                  call 0x1406ac640
00A27836  48 8B 9C 24 D0 01 00 00         mov rbx, qword ptr [rsp + 0x1d0]
00A2783E  48 81 C4 80 01 00 00            add rsp, 0x180
00A27845  41 5F                           pop r15
00A27847  41 5E                           pop r14
00A27849  41 5D                           pop r13
00A2784B  41 5C                           pop r12
00A2784D  5F                              pop rdi
00A2784E  5E                              pop rsi
00A2784F  5D                              pop rbp
00A27850  C3                              ret
00A27851  CC                              int3
00A27852  33 D2                           xor edx, edx
00A27854  48 8B CE                        mov rcx, rsi
00A27857  E8 14 B0 15 00                  call 0x140b82870
00A2785C  EB CA                           jmp 0x140a27828
00A2785E  48 8D 45 E0                     lea rax, [rbp - 0x20]
00A27862  41 B8 13 00 00 00               mov r8d, 0x13
00A27868  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A2786D  4C 8D 0D FC C8 5E FF            lea r9, [rip - 0xa13704]
00A27874  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00A27879  48 8D 45 20                     lea rax, [rbp + 0x20]
00A2787D  C7 44 24 38 02 00 00 00         mov dword ptr [rsp + 0x38], 2
00A27885  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00A2788A  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00A2788F  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00A27894  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00A27898  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A2789D  E8 0E E7 F6 FF                  call 0x140995fb0
00A278A2  8B D8                           mov ebx, eax
00A278A4  3D 34 00 00 C0                  cmp eax, 0xc0000034
00A278A9  0F 84 DB 01 00 00               je 0x140a27a8a
00A278AF  3D 25 02 00 C0                  cmp eax, 0xc0000225
00A278B4  0F 84 D0 01 00 00               je 0x140a27a8a
00A278BA  85 C0                           test eax, eax
00A278BC  78 16                           js 0x140a278d4
00A278BE  BE 00 00 00 10                  mov esi, 0x10000000
00A278C3  85 B7 8C 01 00 00               test dword ptr [rdi + 0x18c], esi
00A278C9  0F 84 24 0C 11 00               je 0x140b384f3
00A278CF  BB 34 00 00 C0                  mov ebx, 0xc0000034
00A278D4  F7 87 8C 01 00 00 00 10 00 00   test dword ptr [rdi + 0x18c], 0x1000
00A278DE  0F 85 B5 01 00 00               jne 0x140a27a99
00A278E4  85 DB                           test ebx, ebx
00A278E6  79 40                           jns 0x140a27928
00A278E8  81 FB 34 00 00 C0               cmp ebx, 0xc0000034
00A278EE  0F 85 C6 FE FF FF               jne 0x140a277ba
00A278F4  44 85 BF 30 02 00 00            test dword ptr [rdi + 0x230], r15d
00A278FB  0F 84 26 FD FF FF               je 0x140a27627
00A27901  48 8B CF                        mov rcx, rdi
00A27904  E8 83 03 00 00                  call 0x140a27c8c
00A27909  41 B5 01                        mov r13b, 1
00A2790C  BE 00 00 00 20                  mov esi, 0x20000000
00A27911  41 BE 12 00 00 00               mov r14d, 0x12
00A27917  85 B7 8C 01 00 00               test dword ptr [rdi + 0x18c], esi
00A2791D  0F 84 3C 0C 11 00               je 0x140b3855f
00A27923  E9 9B 0C 11 00                  jmp 0x140b385c3
00A27928  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
00A2792C  48 83 78 08 00                  cmp qword ptr [rax + 8], 0
00A27931  74 D9                           je 0x140a2790c
00A27933  BA 13 00 00 00                  mov edx, 0x13
00A27938  41 B8 82 01 00 C0               mov r8d, 0xc0000182
00A2793E  48 8B CF                        mov rcx, rdi
00A27941  E8 C6 64 ED FF                  call 0x1408fde0c
00A27946  E9 DC FC FF FF                  jmp 0x140a27627
00A2794B  85 C0                           test eax, eax
00A2794D  0F 89 70 0C 11 00               jns 0x140b385c3
00A27953  E9 62 FE FF FF                  jmp 0x140a277ba
00A27958  85 DB                           test ebx, ebx
00A2795A  0F 88 74 FF FF FF               js 0x140a278d4
00A27960  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00A27964  48 85 C9                        test rcx, rcx
00A27967  0F 84 51 FF FF FF               je 0x140a278be
00A2796D  BE 00 00 00 08                  mov esi, 0x8000000
00A27972  85 B7 8C 01 00 00               test dword ptr [rdi + 0x18c], esi
00A27978  0F 85 40 FF FF FF               jne 0x140a278be
00A2797E  E9 DB FE FF FF                  jmp 0x140a2785e
00A27983  44 38 76 04                     cmp byte ptr [rsi + 4], r14b
00A27987  0F 85 03 FA FF FF               jne 0x140a27390
00A2798D  BB 01 00 00 C0                  mov ebx, 0xc0000001
00A27992  E9 70 0D 11 00                  jmp 0x140b38707
00A27997  8B 4D 80                        mov ecx, dword ptr [rbp - 0x80]
00A2799A  81 F9 FF 00 00 00               cmp ecx, 0xff
00A279A0  0F 87 B3 FA FF FF               ja 0x140a27459
00A279A6  48 8B 05 73 E9 43 00            mov rax, qword ptr [rip + 0x43e973]
00A279AD  48 8D 55 84                     lea rdx, [rbp - 0x7c]
00A279B1  E8 1A 31 C9 FF                  call 0x1406baad0
00A279B6  85 C0                           test eax, eax
00A279B8  0F 88 9B FA FF FF               js 0x140a27459
00A279BE  0F B7 45 84                     movzx eax, word ptr [rbp - 0x7c]
00A279C2  89 87 94 02 00 00               mov dword ptr [rdi + 0x294], eax
00A279C8  E9 8C FA FF FF                  jmp 0x140a27459
00A279CD  C7 87 94 02 00 00 FE FF FF FF   mov dword ptr [rdi + 0x294], 0xfffffffe
00A279D7  E9 AA FA FF FF                  jmp 0x140a27486
00A279DC  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
00A279E1  41 B8 01 00 00 00               mov r8d, 1
00A279E7  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A279EB  48 8B 0D A6 E9 43 00            mov rcx, qword ptr [rip + 0x43e9a6]
00A279F2  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A279F7  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00A279FB  89 45 80                        mov dword ptr [rbp - 0x80], eax
00A279FE  48 8D 45 80                     lea rax, [rbp - 0x80]
00A27A02  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A27A07  48 8D 05 5A 02 60 FF            lea rax, [rip - 0x9ffda6]
00A27A0E  C7 44 24 30 07 00 00 00         mov dword ptr [rsp + 0x30], 7
00A27A16  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A27A1B  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00A27A20  E8 C3 EC EC FF                  call 0x1408f66e8
00A27A25  E9 5C FA FF FF                  jmp 0x140a27486
00A27A2A  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
00A27A2F  48 8D 05 DA 24 5F FF            lea rax, [rip - 0xa0db26]
00A27A36  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00A27A3A  41 B8 01 00 00 00               mov r8d, 1
00A27A40  48 8B 0D 51 E9 43 00            mov rcx, qword ptr [rip + 0x43e951]
00A27A47  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A27A4C  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
00A27A51  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00A27A56  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00A27A5B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A27A60  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00A27A65  E8 7E EC EC FF                  call 0x1408f66e8
00A27A6A  E9 89 FA FF FF                  jmp 0x140a274f8
00A27A6F  83 7C 24 70 04                  cmp dword ptr [rsp + 0x70], 4
00A27A74  0F 85 19 FB FF FF               jne 0x140a27593
00A27A7A  83 7C 24 60 04                  cmp dword ptr [rsp + 0x60], 4
00A27A7F  0F 84 13 FB FF FF               je 0x140a27598
00A27A85  E9 09 FB FF FF                  jmp 0x140a27593
00A27A8A  8B D6                           mov edx, esi
00A27A8C  48 8B CF                        mov rcx, rdi
00A27A8F  E8 B4 45 ED FF                  call 0x1408fc048
00A27A94  E9 25 FE FF FF                  jmp 0x140a278be
00A27A99  33 DB                           xor ebx, ebx
00A27A9B  E9 1A FD FF FF                  jmp 0x140a277ba
00A27AA0  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A27AA4  BA 50 6E 70 65                  mov edx, 0x65706e50
00A27AA9  E8 D6 C0 84 FF                  call 0x140273b84
00A27AAE  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00A27AB2  4C 8B E0                        mov r12, rax
00A27AB5  45 84 ED                        test r13b, r13b
00A27AB8  0F 84 B4 FB FF FF               je 0x140a27672
00A27ABE  48 83 7D 08 00                  cmp qword ptr [rbp + 8], 0
00A27AC3  0F 85 A9 FB FF FF               jne 0x140a27672
00A27AC9  BA 05 03 00 00                  mov edx, 0x305
00A27ACE  48 8B CF                        mov rcx, rdi
00A27AD1  E8 32 8C A4 FF                  call 0x140470708
00A27AD6  E9 97 FB FF FF                  jmp 0x140a27672
00A27ADB  4D 8B 74 24 18                  mov r14, qword ptr [r12 + 0x18]
00A27AE0  E9 E8 FC FF FF                  jmp 0x140a277cd
00A27AE5  4C 8B 7D A8                     mov r15, qword ptr [rbp - 0x58]
00A27AE9  45 33 C9                        xor r9d, r9d
00A27AEC  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00A27AF0  4D 8B C6                        mov r8, r14
00A27AF3  49 8B 57 18                     mov rdx, qword ptr [r15 + 0x18]
00A27AF7  E8 38 FC A8 FF                  call 0x1404b7734
00A27AFC  41 B8 1F 00 00 00               mov r8d, 0x1f
00A27B02  44 89 9F 88 01 00 00            mov dword ptr [rdi + 0x188], r11d
00A27B09  45 8B CB                        mov r9d, r11d
00A27B0C  E9 CE FB FF FF                  jmp 0x140a276df
00A27B11  E8 9A 57 C8 FF                  call 0x1406ad2b0
00A27B16  E9 E1 FC FF FF                  jmp 0x140a277fc
00A27B1B  E8 90 57 C8 FF                  call 0x1406ad2b0
00A27B20  E9 E4 FC FF FF                  jmp 0x140a27809
00A27B25  BA 50 6E 70 65                  mov edx, 0x65706e50
00A27B2A  49 8B CF                        mov rcx, r15
00A27B2D  E8 AE FD 8C FF                  call 0x1402f78e0
00A27B32  E9 DB FC FF FF                  jmp 0x140a27812
00A27B37  BA 50 6E 70 65                  mov edx, 0x65706e50
00A27B3C  48 8B C8                        mov rcx, rax
00A27B3F  E8 9C FD 8C FF                  call 0x1402f78e0
00A27B44  E9 D6 FC FF FF                  jmp 0x140a2781f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipCallDriverAddDevice(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned __int16 v_stack_m134;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned __int8 v_stack_m150;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int8 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m48;
    unsigned __int16 v_stack_m98;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (384);
    result = (*(unsigned __int64 *)(v_rip + 4076605)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r14 = 0;
    v_stack_m150 = 0;
    a2 = 0;
    v_stack_m120 = 0;
    v_stack_m14C = 0;
    v_stack_m138 = 0;
    v_stack_m140 = 0;
    v_stack_m134 = 0;
    v_stack_mE8 = 0;
    v_stack_m158 = 0;
    v_stack_m148 = 0;
    v_stack_m118 = 0;
    result = memset(v_stack_mD8, a2, v_r14 + 64, a4);
    v_stack_mF8 = v_xmm0;
    v_stack_mE0 = v_r14 + 6;
    v_stack_m154 = 0;
    v_stack_m108 = 0;
    v_stack_m130 = 0;
    v_stack_m98 = 0;
    v_stack_m128 = 0;
    v_stack_m110 = 0;
    v_stack_m100 = 0;
    if ((*(unsigned __int8 *)(a1 + 688)) != 0) goto loc_00A27983;
loc_00A27390:
    v_stack_m180 = 0;
    a4 = 0;
    v_stack_m188 = v_stack_m140;
    *(unsigned __int8 *)(a1 + 688) = 0;
    v_stack_m190 = 0;
    v_stack_m198 = 0x20019ULL;
    result = _CmOpenDeviceRegKey(*(unsigned __int64 *)(v_rip + 4452324), *(unsigned __int64 *)(a1 + 48), a4 + 16, a4);
    if (sign_flag) goto loc_00A277BA;
    if ((*(unsigned int *)(a1 + 660)) != -1) goto loc_00A27486;
    if ((*(unsigned __int64 *)(v_rip + 4452130)) == 0) goto loc_00A27459;
    v_stack_m168 = 0;
    v_stack_m170 = v_stack_m154;
    v_stack_m178 = 4;
    v_stack_m180 = v_stack_m138;
    v_stack_m188 = v_stack_m130;
    v_stack_m190 = v_rip - 10540314;
    v_stack_m198 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 4452221), *(unsigned __int64 *)(a1 + 48), 1, v_stack_m140);
    if (!sign_flag) goto loc_00A27997;
loc_00A27459:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 660)))) != -1) goto loc_00A2747D;
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_00A279CD;
    *(unsigned int *)(a1 + 660) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 660)));
loc_00A2747D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 660)))) != -2) goto loc_00A279DC;
loc_00A27486:
    v_stack_m168 = 0;
    v_stack_m170 = v_stack_m154;
    v_stack_m178 = 8;
    v_stack_m180 = v_stack_mE8;
    v_stack_m188 = v_stack_m130;
    v_stack_m190 = v_rip - 10540476;
    v_stack_m198 = 0;
    result = PnpGetObjectProperty(*(unsigned __int64 *)(v_rip + 4452087), *(unsigned __int64 *)(a1 + 48), 1, v_stack_m140);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) != 0) goto loc_00A275DA;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC0000023ULL) goto loc_00A275DA;
loc_00A274F8:
    v_stack_m180 = 0;
    v_stack_m188 = v_stack_m158;
    v_stack_m190 = v_stack_m98;
    v_stack_m198 = v_stack_m148;
    v_stack_m158 = 78;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 4451973), *(unsigned __int64 *)(a1 + 48), v_stack_m140, 9);
    v_stack_m180 = 0;
    v_stack_m188 = v_stack_m158;
    v_stack_m190 = v_stack_m14C;
    v_stack_m198 = v_stack_m148;
    v_stack_m158 = 4;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 4451896), *(unsigned __int64 *)(a1 + 48), v_stack_m140, 11);
    if (!sign_flag) goto loc_00A27A6F;
loc_00A27593:
    v_stack_m14C = 0;
loc_00A27598:
    v_stack_mD8 = a1;
    v_stack_mD0 = 0;
    v_stack_m158 = 512;
    result = ExAllocatePool2(256, 512, (unsigned int)((unsigned int)((unsigned int)(0x6E657050ULL))), 11);
    v_stack_m128 = result;
    goto loc_00A278D4;
loc_00A275DA:
    result = PnpGetStableSystemBootTime(v_stack_m108, 512, (unsigned int)((unsigned int)((unsigned int)(0x6E657050ULL))), 11);
    if (sign_flag) goto loc_00A274F8;
    if (((unsigned int)((unsigned int)(0xC000009AULL))) == 0xC0000023ULL) goto loc_00A27A2A;
    if (v_stack_m130 != 16) goto loc_00A27A2A;
    if (v_stack_m154 != 8) goto loc_00A27A2A;
    if ((*(unsigned __int8 *)(v_rip + 4076493)) != ((unsigned __int8)((unsigned int)(0x6E657050ULL)))) goto loc_00A27A2A;
    if (v_stack_m108 != v_stack_mE8) goto loc_00A27A2A;
loc_00A27627:
    goto loc_00A277BA;
loc_00A277BA:
loc_00A278D4:
    if (((*(unsigned int *)(a1 + 396)) & (0x1000ULL)) != 0) goto loc_00A27A99;
    if (!sign_flag) goto loc_00A27928;
    if (((unsigned int)((unsigned int)(0xC0000001ULL))) != 0xC0000034ULL) goto loc_00A277BA;
    if (((*(unsigned int *)(a1 + 560)) & (256)) == 0) goto loc_00A27627;
    result = PipClearDevNodeProblem(a1, 512, (unsigned int)((unsigned int)((unsigned int)(0x6E657050ULL))), 11);
loc_00A2790C:
loc_00A27928:
    if ((*(unsigned __int64 *)(v_stack_mB0 + 8)) == 0) goto loc_00A2790C;
    result = PipSetDevNodeProblem(a1, 19, (unsigned int)(0xC0000182ULL), 11);
    goto loc_00A27627;
loc_00A27983:
    if ((*(unsigned __int8 *)((unsigned int)(0x20000000ULL) + 4)) != 18) goto loc_00A27390;
loc_00A27997:
    if (((unsigned int)((unsigned int)(v_stack_m138))) > 255) goto loc_00A27459;
    result = guard_dispatch_icall((unsigned int)(v_stack_m138), v_stack_m134, (unsigned int)(0xC0000182ULL), 11);
    if (sign_flag) goto loc_00A27459;
    *(unsigned int *)(a1 + 660) = (unsigned int)(v_stack_m134);
    goto loc_00A27459;
loc_00A279CD:
    *(unsigned int *)(a1 + 660) = 0xFFFFFFFEULL;
    goto loc_00A27486;
loc_00A279DC:
    v_stack_p48 = 18;
    v_stack_p40 = (unsigned int)((unsigned int)(0xC0000001ULL));
    v_stack_m138 = (unsigned int)(v_stack_m134);
    v_stack_p38 = v_stack_m138;
    v_stack_p30 = 7;
    v_stack_p28 = v_rip - 10485158;
    v_stack_p20 = 18;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4450726), *(unsigned __int64 *)(a1 + 48), 1, v_stack_p78);
    goto loc_00A27486;
loc_00A27A2A:
    v_stack_p48 = 18;
    v_stack_p40 = 18;
    v_stack_p38 = 18;
    v_stack_p30 = 18;
    v_stack_p28 = v_rip - 10541862;
    v_stack_p20 = 18;
    result = PnpSetObjectProperty(*(unsigned __int64 *)(v_rip + 4450641), *(unsigned __int64 *)(a1 + 48), 1, v_stack_p78);
    goto loc_00A274F8;
loc_00A27A6F:
    if (v_stack_p70 != 4) goto loc_00A27593;
    if (v_stack_p60 == 4) goto loc_00A27598;
    goto loc_00A27593;
loc_00A27A99:
    v_rbx = 0;
    goto loc_00A277BA;
}
```

## 5. (Beta) C Style

```c
int64_t PipCallDriverAddDevice(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint16_t v_stack_m134;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint8_t v_stack_m150;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint8_t v_stack_m190;
    uint32_t v_stack_m198;
    uint64_t v_stack_m48;
    uint16_t v_stack_m98;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;
    uint32_t v_stack_p38;
    uint8_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p60;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (384);
    result = (*(uint64_t *)(v_rip + 0x3E343D)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r14 = 0;
    v_stack_m150 = 0;
    Arg2 = 0;
    v_stack_m120 = 0;
    v_stack_m14C = 0;
    v_stack_m138 = 0;
    v_stack_m140 = 0;
    v_stack_m134 = 0;
    v_stack_mE8 = 0;
    v_stack_m158 = 0;
    v_stack_m148 = 0;
    v_stack_m118 = 0;
    result = memset(v_stack_mD8, Arg2, local_r14 + 64, Arg4);
    v_stack_mF8 = v_xmm0;
    v_stack_mE0 = local_r14 + 6;
    v_stack_m154 = 0;
    v_stack_m108 = 0;
    v_stack_m130 = 0;
    v_stack_m98 = 0;
    v_stack_m128 = 0;
    v_stack_m110 = 0;
    v_stack_m100 = 0;
    if ((*(uint8_t *)(arg1 + 0x2B0)) != 0) goto loc_00A27983;
loc_00A27390:
    v_stack_m180 = 0;
    Arg4 = 0;
    v_stack_m188 = v_stack_m140;
    *(uint8_t *)(arg1 + 0x2B0) = 0;
    v_stack_m190 = 0;
    v_stack_m198 = 0x20019ULL;
    result = _CmOpenDeviceRegKey(*(uint64_t *)(v_rip + 0x43EFE4), *(uint64_t *)(arg1 + 0x30), Arg4 + 16, Arg4);
    if (sign_flag) goto loc_00A277BA;
    if ((*(uint32_t *)(arg1 + 0x294)) != -1) goto loc_00A27486;
    if ((*(uint64_t *)(v_rip + 0x43EF22)) == 0) goto loc_00A27459;
    v_stack_m168 = 0;
    v_stack_m170 = v_stack_m154;
    v_stack_m178 = 4;
    v_stack_m180 = v_stack_m138;
    v_stack_m188 = v_stack_m130;
    v_stack_m190 = v_rip - 10540314;
    v_stack_m198 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x43EF7D), *(uint64_t *)(arg1 + 0x30), 1, v_stack_m140);
    if (!sign_flag) goto loc_00A27997;
loc_00A27459:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x294)))) != -1) goto loc_00A2747D;
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_00A279CD;
    *(uint32_t *)(arg1 + 0x294) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x294)));
loc_00A2747D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x294)))) != -2) goto loc_00A279DC;
loc_00A27486:
    v_stack_m168 = 0;
    v_stack_m170 = v_stack_m154;
    v_stack_m178 = 8;
    v_stack_m180 = v_stack_mE8;
    v_stack_m188 = v_stack_m130;
    v_stack_m190 = v_rip - 10540476;
    v_stack_m198 = 0;
    result = PnpGetObjectProperty(*(uint64_t *)(v_rip + 0x43EEF7), *(uint64_t *)(arg1 + 0x30), 1, v_stack_m140);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) != 0) goto loc_00A275DA;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC0000023ULL) goto loc_00A275DA;
loc_00A274F8:
    v_stack_m180 = 0;
    v_stack_m188 = v_stack_m158;
    v_stack_m190 = v_stack_m98;
    v_stack_m198 = v_stack_m148;
    v_stack_m158 = 78;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x43EE85), *(uint64_t *)(arg1 + 0x30), v_stack_m140, 9);
    v_stack_m180 = 0;
    v_stack_m188 = v_stack_m158;
    v_stack_m190 = v_stack_m14C;
    v_stack_m198 = v_stack_m148;
    v_stack_m158 = 4;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x43EE38), *(uint64_t *)(arg1 + 0x30), v_stack_m140, 11);
    if (!sign_flag) goto loc_00A27A6F;
loc_00A27593:
    v_stack_m14C = 0;
loc_00A27598:
    v_stack_mD8 = Arg1;
    v_stack_mD0 = 0;
    v_stack_m158 = 512;
    result = ExAllocatePool2(256, 512, (uint32_t)((uint32_t)((uint32_t)(0x6E657050ULL))), 11);
    v_stack_m128 = result;
    goto loc_00A278D4;
loc_00A275DA:
    result = PnpGetStableSystemBootTime(v_stack_m108, 512, (uint32_t)((uint32_t)((uint32_t)(0x6E657050ULL))), 11);
    if (sign_flag) goto loc_00A274F8;
    if (((uint32_t)((uint32_t)(0xC000009AULL))) == 0xC0000023ULL) goto loc_00A27A2A;
    if (v_stack_m130 != 16) goto loc_00A27A2A;
    if (v_stack_m154 != 8) goto loc_00A27A2A;
    if ((*(uint8_t *)(v_rip + 0x3E33CD)) != ((uint8_t)((uint32_t)(0x6E657050ULL)))) goto loc_00A27A2A;
    if (v_stack_m108 != v_stack_mE8) goto loc_00A27A2A;
loc_00A27627:
    goto loc_00A277BA;
loc_00A277BA:
loc_00A278D4:
    if (((*(uint32_t *)(arg1 + 0x18C)) & (0x1000ULL)) != 0) goto loc_00A27A99;
    if (!sign_flag) goto loc_00A27928;
    if (((uint32_t)((uint32_t)(0xC0000001ULL))) != 0xC0000034ULL) goto loc_00A277BA;
    if (((*(uint32_t *)(arg1 + 0x230)) & (256)) == 0) goto loc_00A27627;
    result = PipClearDevNodeProblem(Arg1, 512, (uint32_t)((uint32_t)((uint32_t)(0x6E657050ULL))), 11);
loc_00A2790C:
loc_00A27928:
    if ((*(uint64_t *)(v_stack_mB0 + 0x8)) == 0) goto loc_00A2790C;
    result = PipSetDevNodeProblem(Arg1, 19, (uint32_t)(0xC0000182ULL), 11);
    goto loc_00A27627;
loc_00A27983:
    if ((*(uint8_t *)((uint32_t)(0x20000000ULL) + 0x4)) != 18) goto loc_00A27390;
loc_00A27997:
    if (((uint32_t)((uint32_t)(v_stack_m138))) > 255) goto loc_00A27459;
    result = guard_dispatch_icall((uint32_t)(v_stack_m138), v_stack_m134, (uint32_t)(0xC0000182ULL), 11);
    if (sign_flag) goto loc_00A27459;
    *(uint32_t *)(arg1 + 0x294) = (uint32_t)(v_stack_m134);
    goto loc_00A27459;
loc_00A279CD:
    *(uint32_t *)(arg1 + 0x294) = 0xFFFFFFFEULL;
    goto loc_00A27486;
loc_00A279DC:
    v_stack_p48 = 18;
    v_stack_p40 = (uint32_t)((uint32_t)(0xC0000001ULL));
    v_stack_m138 = (uint32_t)(v_stack_m134);
    v_stack_p38 = v_stack_m138;
    v_stack_p30 = 7;
    v_stack_p28 = v_rip - 10485158;
    v_stack_p20 = 18;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x43E9A6), *(uint64_t *)(arg1 + 0x30), 1, v_stack_p78);
    goto loc_00A27486;
loc_00A27A2A:
    v_stack_p48 = 18;
    v_stack_p40 = 18;
    v_stack_p38 = 18;
    v_stack_p30 = 18;
    v_stack_p28 = v_rip - 10541862;
    v_stack_p20 = 18;
    result = PnpSetObjectProperty(*(uint64_t *)(v_rip + 0x43E951), *(uint64_t *)(arg1 + 0x30), 1, v_stack_p78);
    goto loc_00A274F8;
loc_00A27A6F:
    if (v_stack_p70 != 4) goto loc_00A27593;
    if (v_stack_p60 == 4) goto loc_00A27598;
    goto loc_00A27593;
loc_00A27A99:
    local_rbx = 0;
    goto loc_00A277BA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x18C` | `32` | `R` |
| `Arg1` | `+ 0x230` | `32` | `R` |
| `Arg1` | `+ 0x294` | `32` | `R` |
| `Arg1` | `+ 0x294` | `32` | `W` |
| `Arg1` | `+ 0x2B0` | `8` | `R` |
| `Arg1` | `+ 0x2B0` | `8` | `W` |
| `Arg2` | `+ 0x4` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A272E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
