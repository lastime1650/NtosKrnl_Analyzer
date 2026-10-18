# PiCMHandleIoctl

- RVA: `0x008EB880`–`0x008EC5A8` (길이 `3,368` bytes)
- VA: `0x00000001408EB880`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086C58`
- 디코드: `831`개 명령, `3,368/3,368` bytes 표시
- 미해석 바이트: `7` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **49**; 고유 호출 대상: **41**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x008EB923` → [PiCMValidateDeviceInstance](PiCMValidateDeviceInstance_function_008E799C.md) (function, `0x008E799C`)
- `0x008EB939` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008EB95C` → [PiCMCapturePropertyInputData](PiCMCapturePropertyInputData_function_008ED3A0.md) (function, `0x008ED3A0`)
- `0x008EBA05` → [PiCMCaptureRegistryPropertyInputData](PiCMCaptureRegistryPropertyInputData_function_008ED078.md) (function, `0x008ED078`)
- `0x008EBA6F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008EBB08` → [CmGetDeviceRegProp](CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x008EBB3F` → [PiCMReturnBufferResultData](PiCMReturnBufferResultData_function_008ED6D0.md) (function, `0x008ED6D0`)
- `0x008EBB53` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008EBB90` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008EBBB9` → [PiCMGetRelatedDeviceInstance](PiCMGetRelatedDeviceInstance_function_008E7DF0.md) (function, `0x008E7DF0`)
- `0x008EBBE4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008EBC7E` → [PiPnpRtlObjectActionCallback](PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008EBCF6` → [PnpGetObjectPropertyWorker](PnpGetObjectPropertyWorker_function_008E1810.md) (function, `0x008E1810`)
- `0x008EBD39` → [PiPnpRtlObjectActionCallback](PiPnpRtlObjectActionCallback_function_008E2850.md) (function, `0x008E2850`)
- `0x008EBD8B` → [PiCMReturnBufferResultData](PiCMReturnBufferResultData_function_008ED6D0.md) (function, `0x008ED6D0`)
- `0x008EBD9F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008EBDDA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008EBDE6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008EBDEF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008EBE30` → [PiCMOpenObjectKey](../96/PiCMOpenObjectKey_function_00961E08.md) (function, `0x00961E08`)
- `0x008EBE59` → [PiCMGetObjectList](PiCMGetObjectList_function_008E7720.md) (function, `0x008E7720`)
- `0x008EBE77` → [PiCMOpenDeviceKey](../96/PiCMOpenDeviceKey_function_00961C00.md) (function, `0x00961C00`)
- `0x008EBEBF` → [PiCMGetDeviceInterfaceList](../A1/PiCMGetDeviceInterfaceList_function_00A163D0.md) (function, `0x00A163D0`)
- `0x008EBEDD` → [PiCMGetDeviceIdList](../A2/PiCMGetDeviceIdList_function_00A2BAAC.md) (function, `0x00A2BAAC`)
- `0x008EBF18` → [PiCMGetDeviceStatus](../9D/PiCMGetDeviceStatus_function_009D136C.md) (function, `0x009D136C`)
- `0x008EBFA6` → [PiCMEnumerateSubKeys](../99/PiCMEnumerateSubKeys_function_009926E8.md) (function, `0x009926E8`)
- `0x008EBFCF` → [PiCMGetDeviceInterfaceAlias](../A4/PiCMGetDeviceInterfaceAlias_function_00A47904.md) (function, `0x00A47904`)
- `0x008EC00A` → [PiCMOpenDeviceInterfaceKey](../96/PiCMOpenDeviceInterfaceKey_function_00961A3C.md) (function, `0x00961A3C`)
- `0x008EC065` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (function, `0x00448990`)
- `0x008EC081` → [PiCMSetObjectProperty](../96/PiCMSetObjectProperty_function_00962564.md) (function, `0x00962564`)
- `0x008EC0C7` → [CmGetInstallerClassRegProp](../99/CmGetInstallerClassRegProp_function_00994940.md) (function, `0x00994940`)
- `0x008EC10D` → [PiCMOpenClassKey](../96/PiCMOpenClassKey_function_009617A8.md) (function, `0x009617A8`)
- `0x008EC12B` → [PiCMGetDeviceDepth](../A9/PiCMGetDeviceDepth_function_00A96B98.md) (function, `0x00A96B98`)
- `0x008EC149` → [PiCMGetObjectPropertyKeys](../A7/PiCMGetObjectPropertyKeys_function_00A7C554.md) (function, `0x00A7C554`)
- `0x008EC1A9` → [PiCMCreateObject](../70/PiCMCreateObject_function_007015EC.md) (function, `0x007015EC`)
- `0x008EC1C7` → [PiCMDeleteObject](../AD/PiCMDeleteObject_function_00AD9FE4.md) (function, `0x00AD9FE4`)
- `0x008EC1E5` → [PiCMSetRegistryProperty](../96/PiCMSetRegistryProperty_function_00963118.md) (function, `0x00963118`)
- `0x008EC1F9` → [PiCMSetDeviceProblem](../AD/PiCMSetDeviceProblem_function_00ADA9E0.md) (function, `0x00ADA9E0`)
- `0x008EC217` → [PiCMQueryRemove](../AD/PiCMQueryRemove_function_00AD43F4.md) (function, `0x00AD43F4`)
- `0x008EC235` → [PiCMRegisterDeviceInterface](../96/PiCMRegisterDeviceInterface_function_00962A94.md) (function, `0x00962A94`)
- `0x008EC253` → [PiCMUnregisterDeviceInterface](../AD/PiCMUnregisterDeviceInterface_function_00AD9758.md) (function, `0x00AD9758`)
- `0x008EC271` → [PiCMCreateDevice](../AC/PiCMCreateDevice_function_00ACB824.md) (function, `0x00ACB824`)
- `0x008EC28F` → [PiCMDeleteDevice](../70/PiCMDeleteDevice_function_007017A4.md) (function, `0x007017A4`)
- `0x008EC2AD` → [PiCMDeviceAction](../96/PiCMDeviceAction_function_0096488C.md) (function, `0x0096488C`)
- `0x008EC2CB` → [PiCMDeleteDeviceInterfaceKey](../70/PiCMDeleteDeviceInterfaceKey_function_007014E4.md) (function, `0x007014E4`)
- `0x008EC2E9` → [PiCMDeleteDeviceKey](../AD/PiCMDeleteDeviceKey_function_00AD6780.md) (function, `0x00AD6780`)
- `0x008EC307` → [PiCMDeleteClassKey](../AD/PiCMDeleteClassKey_function_00AD9EB4.md) (function, `0x00AD9EB4`)
- `0x008EC3E1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008EC3F6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PiCMFastIoDeviceDispatch](PiCMFastIoDeviceDispatch_function_008EB3D0.md) at `0x008EB41E`

### Static image references
- `0x008EB899` → RVA `0x00E0A740` (`.data`; read)
- `0x008EB8F1` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x008EB9BE` → RVA `0x00E663D0` (`.data`; read)
- `0x008EBADD` → RVA `0x00E66398` (`.data`; read)
- `0x008EBC57` → RVA `0x008E2850` (`PiPnpRtlObjectActionCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x008EB939` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008EBA6F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008EBB53` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008EBB90` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008EBBE4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008EBD9F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008EBDDA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008EBDE6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008EBDEF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008EC065` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (`PAGE` → `.text`)
  - `0x008EC3E1` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008EC3F6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008EB880  40 55                           push rbp
008EB882  53                              push rbx
008EB883  56                              push rsi
008EB884  57                              push rdi
008EB885  41 54                           push r12
008EB887  41 55                           push r13
008EB889  41 56                           push r14
008EB88B  41 57                           push r15
008EB88D  48 8D 6C 24 C8                  lea rbp, [rsp - 0x38]
008EB892  48 81 EC 38 01 00 00            sub rsp, 0x138
008EB899  48 8B 05 A0 EE 51 00            mov rax, qword ptr [rip + 0x51eea0]
008EB8A0  48 33 C4                        xor rax, rsp
008EB8A3  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
008EB8A7  48 8B B5 A0 00 00 00            mov rsi, qword ptr [rbp + 0xa0]
008EB8AE  45 33 ED                        xor r13d, r13d
008EB8B1  8B 85 A8 00 00 00               mov eax, dword ptr [rbp + 0xa8]
008EB8B7  41 8B F9                        mov edi, r9d
008EB8BA  4D 8B F8                        mov r15, r8
008EB8BD  44 8B E2                        mov r12d, edx
008EB8C0  48 8B D9                        mov rbx, rcx
008EB8C3  44 89 2E                        mov dword ptr [rsi], r13d
008EB8C6  3D 13 08 47 00                  cmp eax, 0x470813
008EB8CB  74 62                           je 0x1408eb92f
008EB8CD  3D 1B 08 47 00                  cmp eax, 0x47081b
008EB8D2  0F 84 00 01 00 00               je 0x1408eb9d8
008EB8D8  3D 23 08 47 00                  cmp eax, 0x470823
008EB8DD  0F 84 C7 02 00 00               je 0x1408ebbaa
008EB8E3  05 FD F7 B8 FF                  add eax, 0xffb8f7fd
008EB8E8  83 F8 74                        cmp eax, 0x74
008EB8EB  0F 87 22 0A 00 00               ja 0x1408ec313
008EB8F1  48 8D 0D 08 47 71 FF            lea rcx, [rip - 0x8eb8f8]
008EB8F8  0F B6 84 01 98 C4 8E 00         movzx eax, byte ptr [rcx + rax + 0x8ec498]
008EB900  44 8B 94 81 28 C4 8E 00         mov r10d, dword ptr [rcx + rax*4 + 0x8ec428]
008EB908  4C 03 D1                        add r10, rcx
008EB90B  41 FF E2                        jmp r10
008EB90E  CC                              int3
008EB90F  CC                              int3
008EB910  CC                              int3
008EB911  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EB917  48 8B CB                        mov rcx, rbx
008EB91A  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EB91F  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EB923  E8 74 C0 FF FF                  call 0x1408e799c
008EB928  8B D8                           mov ebx, eax
008EB92A  E9 58 02 00 00                  jmp 0x1408ebb87
008EB92F  33 D2                           xor edx, edx
008EB931  48 8D 4D D0                     lea rcx, [rbp - 0x30]
008EB935  44 8D 42 48                     lea r8d, [rdx + 0x48]
008EB939  E8 02 B3 DD FF                  call 0x1406c6c40
008EB93E  44 8B 85 B0 00 00 00            mov r8d, dword ptr [rbp + 0xb0]
008EB945  4C 8D 4D D0                     lea r9, [rbp - 0x30]
008EB949  41 8B D4                        mov edx, r12d
008EB94C  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
008EB951  48 8B CB                        mov rcx, rbx
008EB954  44 89 6C 24 60                  mov dword ptr [rsp + 0x60], r13d
008EB959  4D 8B F5                        mov r14, r13
008EB95C  E8 3F 1A 00 00                  call 0x1408ed3a0
008EB961  8B D8                           mov ebx, eax
008EB963  85 C0                           test eax, eax
008EB965  0F 88 39 04 00 00               js 0x1408ebda4
008EB96B  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
008EB96F  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
008EB974  48 85 D2                        test rdx, rdx
008EB977  74 55                           je 0x1408eb9ce
008EB979  44 39 6D 00                     cmp dword ptr [rbp], r13d
008EB97D  75 4F                           jne 0x1408eb9ce
008EB97F  44 39 6D D4                     cmp dword ptr [rbp - 0x2c], r13d
008EB983  75 49                           jne 0x1408eb9ce
008EB985  4C 39 6D 08                     cmp qword ptr [rbp + 8], r13
008EB989  75 43                           jne 0x1408eb9ce
008EB98B  44 39 6D 10                     cmp dword ptr [rbp + 0x10], r13d
008EB98F  75 3D                           jne 0x1408eb9ce
008EB991  4D 85 FF                        test r15, r15
008EB994  74 38                           je 0x1408eb9ce
008EB996  83 FF 14                        cmp edi, 0x14
008EB999  72 33                           jb 0x1408eb9ce
008EB99B  8B 4D D8                        mov ecx, dword ptr [rbp - 0x28]
008EB99E  41 BC 01 00 00 00               mov r12d, 1
008EB9A4  41 3B CC                        cmp ecx, r12d
008EB9A7  0F 84 15 02 00 00               je 0x1408ebbc2
008EB9AD  81 F9 02 00 01 00               cmp ecx, 0x10002
008EB9B3  0F 85 4B 04 00 00               jne 0x1408ebe04
008EB9B9  45 8D 6C 24 07                  lea r13d, [r12 + 7]
008EB9BE  4C 39 35 0B AA 57 00            cmp qword ptr [rip + 0x57aa0b], r14
008EB9C5  0F 85 FC 01 00 00               jne 0x1408ebbc7
008EB9CB  45 33 ED                        xor r13d, r13d
008EB9CE  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008EB9D3  E9 8B 03 00 00                  jmp 0x1408ebd63
008EB9D8  44 8B 85 B0 00 00 00            mov r8d, dword ptr [rbp + 0xb0]
008EB9DF  4C 8D 4D D0                     lea r9, [rbp - 0x30]
008EB9E3  0F 57 C0                        xorps xmm0, xmm0
008EB9E6  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
008EB9EB  33 C0                           xor eax, eax
008EB9ED  44 89 6C 24 60                  mov dword ptr [rsp + 0x60], r13d
008EB9F2  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
008EB9F6  48 89 45 00                     mov qword ptr [rbp], rax
008EB9FA  4D 8B F5                        mov r14, r13
008EB9FD  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
008EBA01  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
008EBA05  E8 6E 16 00 00                  call 0x1408ed078
008EBA0A  8B D8                           mov ebx, eax
008EBA0C  85 C0                           test eax, eax
008EBA0E  0F 88 44 01 00 00               js 0x1408ebb58
008EBA14  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
008EBA18  48 85 D2                        test rdx, rdx
008EBA1B  0F 84 F5 05 00 00               je 0x1408ec016
008EBA21  44 39 6D D4                     cmp dword ptr [rbp - 0x2c], r13d
008EBA25  0F 85 EB 05 00 00               jne 0x1408ec016
008EBA2B  4C 39 6D F8                     cmp qword ptr [rbp - 8], r13
008EBA2F  0F 85 E1 05 00 00               jne 0x1408ec016
008EBA35  44 39 6D 00                     cmp dword ptr [rbp], r13d
008EBA39  0F 85 D7 05 00 00               jne 0x1408ec016
008EBA3F  44 39 6D F0                     cmp dword ptr [rbp - 0x10], r13d
008EBA43  0F 85 CD 05 00 00               jne 0x1408ec016
008EBA49  4D 85 FF                        test r15, r15
008EBA4C  0F 84 C4 05 00 00               je 0x1408ec016
008EBA52  83 FF 14                        cmp edi, 0x14
008EBA55  0F 82 BB 05 00 00               jb 0x1408ec016
008EBA5B  8D 5F EC                        lea ebx, [rdi - 0x14]
008EBA5E  85 DB                           test ebx, ebx
008EBA60  74 22                           je 0x1408eba84
008EBA62  8B D3                           mov edx, ebx
008EBA64  B9 00 01 00 00                  mov ecx, 0x100
008EBA69  41 B8 50 6E 70 34               mov r8d, 0x34706e50
008EBA6F  E8 7C 66 29 00                  call 0x140b820f0
008EBA74  4C 8B F0                        mov r14, rax
008EBA77  48 85 C0                        test rax, rax
008EBA7A  0F 84 21 09 00 00               je 0x1408ec3a1
008EBA80  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
008EBA84  48 63 45 EC                     movsxd rax, dword ptr [rbp - 0x14]
008EBA88  83 F8 02                        cmp eax, 2
008EBA8B  74 3A                           je 0x1408ebac7
008EBA8D  83 F8 09                        cmp eax, 9
008EBA90  0F 84 63 03 00 00               je 0x1408ebdf9
008EBA96  83 F8 0A                        cmp eax, 0xa
008EBA99  0F 84 9D 03 00 00               je 0x1408ebe3c
008EBA9F  83 F8 25                        cmp eax, 0x25
008EBAA2  0F 87 6E 05 00 00               ja 0x1408ec016
008EBAA8  48 8D 0D 51 45 71 FF            lea rcx, [rip - 0x8ebaaf]
008EBAAF  8B 84 81 10 C5 8E 00            mov eax, dword ptr [rcx + rax*4 + 0x8ec510]
008EBAB6  48 03 C1                        add rax, rcx
008EBAB9  FF E0                           jmp rax
008EBABB  CC                              int3
008EBABC  CC                              int3
008EBABD  CC                              int3
008EBABE  CC                              int3
008EBABF  41 BC 05 00 00 00               mov r12d, 5
008EBAC5  EB 06                           jmp 0x1408ebacd
008EBAC7  41 BC 02 00 00 00               mov r12d, 2
008EBACD  8B 45 D8                        mov eax, dword ptr [rbp - 0x28]
008EBAD0  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
008EBAD4  83 F8 01                        cmp eax, 1
008EBAD7  0F 85 BB 05 00 00               jne 0x1408ec098
008EBADD  48 8B 0D B4 A8 57 00            mov rcx, qword ptr [rip + 0x57a8b4]
008EBAE4  48 8D 44 24 60                  lea rax, [rsp + 0x60]
008EBAE9  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
008EBAEE  45 8B CC                        mov r9d, r12d
008EBAF1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008EBAF6  45 33 C0                        xor r8d, r8d
008EBAF9  48 8D 44 24 64                  lea rax, [rsp + 0x64]
008EBAFE  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
008EBB03  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008EBB08  E8 63 1D 00 00                  call 0x1408ed870
008EBB0D  8B D8                           mov ebx, eax
008EBB0F  85 C0                           test eax, eax
008EBB11  0F 89 94 08 00 00               jns 0x1408ec3ab
008EBB17  8B 45 04                        mov eax, dword ptr [rbp + 4]
008EBB1A  45 33 C9                        xor r9d, r9d
008EBB1D  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
008EBB21  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
008EBB26  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
008EBB2A  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
008EBB2F  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008EBB33  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
008EBB38  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
008EBB3D  8B CB                           mov ecx, ebx
008EBB3F  E8 8C 1B 00 00                  call 0x1408ed6d0
008EBB44  8B D8                           mov ebx, eax
008EBB46  4D 85 F6                        test r14, r14
008EBB49  74 0D                           je 0x1408ebb58
008EBB4B  BA 50 6E 70 34                  mov edx, 0x34706e50
008EBB50  49 8B CE                        mov rcx, r14
008EBB53  E8 18 6D 29 00                  call 0x140b82870
008EBB58  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008EBB61  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
008EBB65  0F B6 B8 32 02 00 00            movzx edi, byte ptr [rax + 0x232]
008EBB6C  48 85 C9                        test rcx, rcx
008EBB6F  74 09                           je 0x1408ebb7a
008EBB71  40 84 FF                        test dil, dil
008EBB74  0F 85 73 02 00 00               jne 0x1408ebded
008EBB7A  48 8B 55 F8                     mov rdx, qword ptr [rbp - 8]
008EBB7E  48 85 D2                        test rdx, rdx
008EBB81  0F 85 DA 04 00 00               jne 0x1408ec061
008EBB87  8B C3                           mov eax, ebx
008EBB89  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
008EBB8D  48 33 CC                        xor rcx, rsp
008EBB90  E8 AB 0A DC FF                  call 0x1406ac640
008EBB95  48 81 C4 38 01 00 00            add rsp, 0x138
008EBB9C  41 5F                           pop r15
008EBB9E  41 5E                           pop r14
008EBBA0  41 5D                           pop r13
008EBBA2  41 5C                           pop r12
008EBBA4  5F                              pop rdi
008EBBA5  5E                              pop rsi
008EBBA6  5B                              pop rbx
008EBBA7  5D                              pop rbp
008EBBA8  C3                              ret
008EBBA9  CC                              int3
008EBBAA  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EBBB0  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EBBB5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EBBB9  E8 32 C2 FF FF                  call 0x1408e7df0
008EBBBE  8B D8                           mov ebx, eax
008EBBC0  EB C5                           jmp 0x1408ebb87
008EBBC2  45 8B EC                        mov r13d, r12d
008EBBC5  EB 09                           jmp 0x1408ebbd0
008EBBC7  45 85 ED                        test r13d, r13d
008EBBCA  0F 84 FB FD FF FF               je 0x1408eb9cb
008EBBD0  8D 5F EC                        lea ebx, [rdi - 0x14]
008EBBD3  85 DB                           test ebx, ebx
008EBBD5  74 23                           je 0x1408ebbfa
008EBBD7  8B D3                           mov edx, ebx
008EBBD9  B9 00 01 00 00                  mov ecx, 0x100
008EBBDE  41 B8 50 6E 70 34               mov r8d, 0x34706e50
008EBBE4  E8 07 65 29 00                  call 0x140b820f0
008EBBE9  4C 8B F0                        mov r14, rax
008EBBEC  48 85 C0                        test rax, rax
008EBBEF  0F 84 45 03 00 00               je 0x1408ebf3a
008EBBF5  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
008EBBFA  48 8B 0D 97 A7 57 00            mov rcx, qword ptr [rip + 0x57a797]
008EBC01  4C 8D 45 EC                     lea r8, [rbp - 0x14]
008EBC05  45 33 C9                        xor r9d, r9d
008EBC08  4C 89 45 A0                     mov qword ptr [rbp - 0x60], r8
008EBC0C  4C 8D 44 24 64                  lea r8, [rsp + 0x64]
008EBC11  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
008EBC16  4C 89 45 A8                     mov qword ptr [rbp - 0x58], r8
008EBC1A  0F 57 C0                        xorps xmm0, xmm0
008EBC1D  48 8B 81 E8 01 00 00            mov rax, qword ptr [rcx + 0x1e8]
008EBC24  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
008EBC29  4C 89 45 C0                     mov qword ptr [rbp - 0x40], r8
008EBC2D  4C 89 4D 80                     mov qword ptr [rbp - 0x80], r9
008EBC31  4C 89 4D 88                     mov qword ptr [rbp - 0x78], r9
008EBC35  44 89 4D BC                     mov dword ptr [rbp - 0x44], r9d
008EBC39  4C 89 4D C8                     mov qword ptr [rbp - 0x38], r9
008EBC3D  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008EBC42  66 0F 7F 45 90                  movdqa xmmword ptr [rbp - 0x70], xmm0
008EBC47  4C 89 75 B0                     mov qword ptr [rbp - 0x50], r14
008EBC4B  89 5D B8                        mov dword ptr [rbp - 0x48], ebx
008EBC4E  48 85 C0                        test rax, rax
008EBC51  0F 84 94 07 00 00               je 0x1408ec3eb
008EBC57  4C 8D 05 F2 6B FF FF            lea r8, [rip - 0x940e]
008EBC5E  41 B9 08 00 00 00               mov r9d, 8
008EBC64  49 3B C0                        cmp rax, r8
008EBC67  0F 85 63 07 00 00               jne 0x1408ec3d0
008EBC6D  48 8D 45 80                     lea rax, [rbp - 0x80]
008EBC71  45 8B C5                        mov r8d, r13d
008EBC74  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008EBC79  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
008EBC7E  E8 CD 6B FF FF                  call 0x1408e2850
008EBC83  3D 02 00 00 C0                  cmp eax, 0xc0000002
008EBC88  0F 84 F8 02 00 00               je 0x1408ebf86
008EBC8E  3D 20 01 00 C0                  cmp eax, 0xc0000120
008EBC93  75 08                           jne 0x1408ebc9d
008EBC95  8B 5D 80                        mov ebx, dword ptr [rbp - 0x80]
008EBC98  E9 BB 00 00 00                  jmp 0x1408ebd58
008EBC9D  85 C0                           test eax, eax
008EBC9F  0F 85 A7 03 00 00               jne 0x1408ec04c
008EBCA5  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
008EBCAA  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008EBCAF  8B 45 C8                        mov eax, dword ptr [rbp - 0x38]
008EBCB2  45 8B C5                        mov r8d, r13d
008EBCB5  4C 8B 4D 90                     mov r9, qword ptr [rbp - 0x70]
008EBCB9  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
008EBCBE  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008EBCC2  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
008EBCC6  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008EBCCB  8B 45 B8                        mov eax, dword ptr [rbp - 0x48]
008EBCCE  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008EBCD2  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
008EBCD6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008EBCDB  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
008EBCDF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008EBCE4  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
008EBCE8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008EBCED  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
008EBCF1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008EBCF6  E8 15 5B FF FF                  call 0x1408e1810
008EBCFB  8B D8                           mov ebx, eax
008EBCFD  4D 85 E4                        test r12, r12
008EBD00  74 56                           je 0x1408ebd58
008EBD02  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
008EBD07  41 B9 08 00 00 00               mov r9d, 8
008EBD0D  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008EBD12  45 8B C5                        mov r8d, r13d
008EBD15  89 45 80                        mov dword ptr [rbp - 0x80], eax
008EBD18  48 8D 05 31 6B FF FF            lea rax, [rip - 0x94cf]
008EBD1F  4C 3B E0                        cmp r12, rax
008EBD22  48 8D 45 80                     lea rax, [rbp - 0x80]
008EBD26  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008EBD2B  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
008EBD33  0F 85 BA 06 00 00               jne 0x1408ec3f3
008EBD39  E8 12 6B FF FF                  call 0x1408e2850
008EBD3E  3D 02 00 00 C0                  cmp eax, 0xc0000002
008EBD43  74 13                           je 0x1408ebd58
008EBD45  3D 20 01 00 C0                  cmp eax, 0xc0000120
008EBD4A  0F 84 45 FF FF FF               je 0x1408ebc95
008EBD50  85 C0                           test eax, eax
008EBD52  0F 85 F4 02 00 00               jne 0x1408ec04c
008EBD58  85 DB                           test ebx, ebx
008EBD5A  0F 89 A0 06 00 00               jns 0x1408ec400
008EBD60  45 33 ED                        xor r13d, r13d
008EBD63  8B 45 14                        mov eax, dword ptr [rbp + 0x14]
008EBD66  45 33 C9                        xor r9d, r9d
008EBD69  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
008EBD6D  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
008EBD72  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
008EBD76  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
008EBD7B  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008EBD7F  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
008EBD84  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
008EBD89  8B CB                           mov ecx, ebx
008EBD8B  E8 40 19 00 00                  call 0x1408ed6d0
008EBD90  8B D8                           mov ebx, eax
008EBD92  4D 85 F6                        test r14, r14
008EBD95  74 0D                           je 0x1408ebda4
008EBD97  BA 50 6E 70 34                  mov edx, 0x34706e50
008EBD9C  49 8B CE                        mov rcx, r14
008EBD9F  E8 CC 6A 29 00                  call 0x140b82870
008EBDA4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008EBDAD  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
008EBDB1  0F B6 B8 32 02 00 00            movzx edi, byte ptr [rax + 0x232]
008EBDB8  48 85 C9                        test rcx, rcx
008EBDBB  74 05                           je 0x1408ebdc2
008EBDBD  40 84 FF                        test dil, dil
008EBDC0  75 22                           jne 0x1408ebde4
008EBDC2  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
008EBDC6  48 85 C9                        test rcx, rcx
008EBDC9  0F 84 B8 FD FF FF               je 0x1408ebb87
008EBDCF  40 84 FF                        test dil, dil
008EBDD2  0F 84 AF FD FF FF               je 0x1408ebb87
008EBDD8  33 D2                           xor edx, edx
008EBDDA  E8 91 6A 29 00                  call 0x140b82870
008EBDDF  E9 A3 FD FF FF                  jmp 0x1408ebb87
008EBDE4  33 D2                           xor edx, edx
008EBDE6  E8 85 6A 29 00                  call 0x140b82870
008EBDEB  EB D5                           jmp 0x1408ebdc2
008EBDED  33 D2                           xor edx, edx
008EBDEF  E8 7C 6A 29 00                  call 0x140b82870
008EBDF4  E9 81 FD FF FF                  jmp 0x1408ebb7a
008EBDF9  41 BC 09 00 00 00               mov r12d, 9
008EBDFF  E9 C9 FC FF FF                  jmp 0x1408ebacd
008EBE04  83 F9 06                        cmp ecx, 6
008EBE07  7E 7A                           jle 0x1408ebe83
008EBE09  81 E9 01 00 01 00               sub ecx, 0x10001
008EBE0F  0F 85 D4 00 00 00               jne 0x1408ebee9
008EBE15  44 8D 69 07                     lea r13d, [rcx + 7]
008EBE19  E9 A0 FB FF FF                  jmp 0x1408eb9be
008EBE1E  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EBE24  48 8B CB                        mov rcx, rbx
008EBE27  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EBE2C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EBE30  E8 D3 5F 07 00                  call 0x140961e08
008EBE35  8B D8                           mov ebx, eax
008EBE37  E9 4B FD FF FF                  jmp 0x1408ebb87
008EBE3C  41 BC 0A 00 00 00               mov r12d, 0xa
008EBE42  E9 86 FC FF FF                  jmp 0x1408ebacd
008EBE47  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EBE4D  48 8B CB                        mov rcx, rbx
008EBE50  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EBE55  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EBE59  E8 C2 B8 FF FF                  call 0x1408e7720
008EBE5E  8B D8                           mov ebx, eax
008EBE60  E9 22 FD FF FF                  jmp 0x1408ebb87
008EBE65  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EBE6B  48 8B CB                        mov rcx, rbx
008EBE6E  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EBE73  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EBE77  E8 84 5D 07 00                  call 0x140961c00
008EBE7C  8B D8                           mov ebx, eax
008EBE7E  E9 04 FD FF FF                  jmp 0x1408ebb87
008EBE83  0F 84 0D 05 00 00               je 0x1408ec396
008EBE89  83 E9 02                        sub ecx, 2
008EBE8C  0F 84 01 01 00 00               je 0x1408ebf93
008EBE92  41 2B CC                        sub ecx, r12d
008EBE95  0F 84 CA 00 00 00               je 0x1408ebf65
008EBE9B  41 2B CC                        sub ecx, r12d
008EBE9E  0F 85 38 02 00 00               jne 0x1408ec0dc
008EBEA4  44 8D 69 03                     lea r13d, [rcx + 3]
008EBEA8  E9 23 FD FF FF                  jmp 0x1408ebbd0
008EBEAD  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EBEB3  48 8B CB                        mov rcx, rbx
008EBEB6  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EBEBB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EBEBF  E8 0C A5 12 00                  call 0x140a163d0
008EBEC4  8B D8                           mov ebx, eax
008EBEC6  E9 BC FC FF FF                  jmp 0x1408ebb87
008EBECB  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EBED1  48 8B CB                        mov rcx, rbx
008EBED4  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EBED9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EBEDD  E8 CA FB 13 00                  call 0x140a2baac
008EBEE2  8B D8                           mov ebx, eax
008EBEE4  E9 9E FC FF FF                  jmp 0x1408ebb87
008EBEE9  83 E9 02                        sub ecx, 2
008EBEEC  0F 85 E9 00 00 00               jne 0x1408ebfdb
008EBEF2  44 8D 69 09                     lea r13d, [rcx + 9]
008EBEF6  E9 C3 FA FF FF                  jmp 0x1408eb9be
008EBEFB  41 BC 01 00 00 00               mov r12d, 1
008EBF01  E9 C7 FB FF FF                  jmp 0x1408ebacd
008EBF06  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EBF0C  48 8B CB                        mov rcx, rbx
008EBF0F  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EBF14  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EBF18  E8 4F 54 0E 00                  call 0x1409d136c
008EBF1D  8B D8                           mov ebx, eax
008EBF1F  E9 63 FC FF FF                  jmp 0x1408ebb87
008EBF24  41 BC 03 00 00 00               mov r12d, 3
008EBF2A  E9 9E FB FF FF                  jmp 0x1408ebacd
008EBF2F  41 BC 0D 00 00 00               mov r12d, 0xd
008EBF35  E9 93 FB FF FF                  jmp 0x1408ebacd
008EBF3A  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008EBF3F  E9 1C FE FF FF                  jmp 0x1408ebd60
008EBF44  41 BC 0F 00 00 00               mov r12d, 0xf
008EBF4A  E9 7E FB FF FF                  jmp 0x1408ebacd
008EBF4F  41 BC 13 00 00 00               mov r12d, 0x13
008EBF55  E9 73 FB FF FF                  jmp 0x1408ebacd
008EBF5A  41 BC 08 00 00 00               mov r12d, 8
008EBF60  E9 68 FB FF FF                  jmp 0x1408ebacd
008EBF65  41 BD 04 00 00 00               mov r13d, 4
008EBF6B  E9 60 FC FF FF                  jmp 0x1408ebbd0
008EBF70  41 BC 0C 00 00 00               mov r12d, 0xc
008EBF76  E9 52 FB FF FF                  jmp 0x1408ebacd
008EBF7B  41 BC 12 00 00 00               mov r12d, 0x12
008EBF81  E9 47 FB FF FF                  jmp 0x1408ebacd
008EBF86  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
008EBF8B  45 33 E4                        xor r12d, r12d
008EBF8E  E9 1C FD FF FF                  jmp 0x1408ebcaf
008EBF93  41 BD 02 00 00 00               mov r13d, 2
008EBF99  E9 32 FC FF FF                  jmp 0x1408ebbd0
008EBF9E  48 8B CB                        mov rcx, rbx
008EBFA1  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EBFA6  E8 3D 67 0A 00                  call 0x1409926e8
008EBFAB  8B D8                           mov ebx, eax
008EBFAD  E9 D5 FB FF FF                  jmp 0x1408ebb87
008EBFB2  41 BC 16 00 00 00               mov r12d, 0x16
008EBFB8  E9 10 FB FF FF                  jmp 0x1408ebacd
008EBFBD  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EBFC3  48 8B CB                        mov rcx, rbx
008EBFC6  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EBFCB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EBFCF  E8 30 B9 15 00                  call 0x140a47904
008EBFD4  8B D8                           mov ebx, eax
008EBFD6  E9 AC FB FF FF                  jmp 0x1408ebb87
008EBFDB  41 2B CC                        sub ecx, r12d
008EBFDE  0F 84 0C 01 00 00               je 0x1408ec0f0
008EBFE4  41 3B CC                        cmp ecx, r12d
008EBFE7  0F 85 E1 F9 FF FF               jne 0x1408eb9ce
008EBFED  41 BD 0B 00 00 00               mov r13d, 0xb
008EBFF3  E9 C6 F9 FF FF                  jmp 0x1408eb9be
008EBFF8  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EBFFE  48 8B CB                        mov rcx, rbx
008EC001  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC006  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC00A  E8 2D 5A 07 00                  call 0x140961a3c
008EC00F  8B D8                           mov ebx, eax
008EC011  E9 71 FB FF FF                  jmp 0x1408ebb87
008EC016  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008EC01B  E9 F7 FA FF FF                  jmp 0x1408ebb17
008EC020  41 BC 0E 00 00 00               mov r12d, 0xe
008EC026  E9 A2 FA FF FF                  jmp 0x1408ebacd
008EC02B  41 BC 15 00 00 00               mov r12d, 0x15
008EC031  E9 97 FA FF FF                  jmp 0x1408ebacd
008EC036  41 BC 0B 00 00 00               mov r12d, 0xb
008EC03C  E9 8C FA FF FF                  jmp 0x1408ebacd
008EC041  41 BC 1D 00 00 00               mov r12d, 0x1d
008EC047  E9 81 FA FF FF                  jmp 0x1408ebacd
008EC04C  BB E5 00 00 C0                  mov ebx, 0xc00000e5
008EC051  E9 0A FD FF FF                  jmp 0x1408ebd60
008EC056  41 BC 17 00 00 00               mov r12d, 0x17
008EC05C  E9 6C FA FF FF                  jmp 0x1408ebacd
008EC061  40 0F B6 CF                     movzx ecx, dil
008EC065  E8 26 C9 B5 FF                  call 0x140448990
008EC06A  E9 18 FB FF FF                  jmp 0x1408ebb87
008EC06F  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC075  48 8B CB                        mov rcx, rbx
008EC078  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC07D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC081  E8 DE 64 07 00                  call 0x140962564
008EC086  8B D8                           mov ebx, eax
008EC088  E9 FA FA FF FF                  jmp 0x1408ebb87
008EC08D  41 BC 10 00 00 00               mov r12d, 0x10
008EC093  E9 35 FA FF FF                  jmp 0x1408ebacd
008EC098  83 F8 02                        cmp eax, 2
008EC09B  0F 85 75 FF FF FF               jne 0x1408ec016
008EC0A1  48 8B 0D F0 A2 57 00            mov rcx, qword ptr [rip + 0x57a2f0]
008EC0A8  48 8D 44 24 60                  lea rax, [rsp + 0x60]
008EC0AD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008EC0B2  45 8B CC                        mov r9d, r12d
008EC0B5  48 8D 44 24 64                  lea rax, [rsp + 0x64]
008EC0BA  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
008EC0BF  45 33 C0                        xor r8d, r8d
008EC0C2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008EC0C7  E8 74 88 0A 00                  call 0x140994940
008EC0CC  E9 3C FA FF FF                  jmp 0x1408ebb0d
008EC0D1  41 BC 23 00 00 00               mov r12d, 0x23
008EC0D7  E9 F1 F9 FF FF                  jmp 0x1408ebacd
008EC0DC  41 3B CC                        cmp ecx, r12d
008EC0DF  0F 85 E9 F8 FF FF               jne 0x1408eb9ce
008EC0E5  41 BD 05 00 00 00               mov r13d, 5
008EC0EB  E9 E0 FA FF FF                  jmp 0x1408ebbd0
008EC0F0  41 BD 0A 00 00 00               mov r13d, 0xa
008EC0F6  E9 C3 F8 FF FF                  jmp 0x1408eb9be
008EC0FB  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC101  48 8B CB                        mov rcx, rbx
008EC104  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC109  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC10D  E8 96 56 07 00                  call 0x1409617a8
008EC112  8B D8                           mov ebx, eax
008EC114  E9 6E FA FF FF                  jmp 0x1408ebb87
008EC119  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC11F  48 8B CB                        mov rcx, rbx
008EC122  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC127  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC12B  E8 68 AA 1A 00                  call 0x140a96b98
008EC130  8B D8                           mov ebx, eax
008EC132  E9 50 FA FF FF                  jmp 0x1408ebb87
008EC137  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC13D  48 8B CB                        mov rcx, rbx
008EC140  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC145  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC149  E8 06 04 19 00                  call 0x140a7c554
008EC14E  8B D8                           mov ebx, eax
008EC150  E9 32 FA FF FF                  jmp 0x1408ebb87
008EC155  41 BC 07 00 00 00               mov r12d, 7
008EC15B  E9 6D F9 FF FF                  jmp 0x1408ebacd
008EC160  41 BC 1F 00 00 00               mov r12d, 0x1f
008EC166  E9 62 F9 FF FF                  jmp 0x1408ebacd
008EC16B  41 BC 14 00 00 00               mov r12d, 0x14
008EC171  E9 57 F9 FF FF                  jmp 0x1408ebacd
008EC176  41 BC 04 00 00 00               mov r12d, 4
008EC17C  E9 4C F9 FF FF                  jmp 0x1408ebacd
008EC181  41 BC 24 00 00 00               mov r12d, 0x24
008EC187  E9 41 F9 FF FF                  jmp 0x1408ebacd
008EC18C  41 BC 1A 00 00 00               mov r12d, 0x1a
008EC192  E9 36 F9 FF FF                  jmp 0x1408ebacd
008EC197  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC19D  48 8B CB                        mov rcx, rbx
008EC1A0  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC1A5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC1A9  E8 3E 54 E1 FF                  call 0x1407015ec
008EC1AE  8B D8                           mov ebx, eax
008EC1B0  E9 D2 F9 FF FF                  jmp 0x1408ebb87
008EC1B5  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC1BB  48 8B CB                        mov rcx, rbx
008EC1BE  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC1C3  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC1C7  E8 18 DE 1E 00                  call 0x140ad9fe4
008EC1CC  8B D8                           mov ebx, eax
008EC1CE  E9 B4 F9 FF FF                  jmp 0x1408ebb87
008EC1D3  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC1D9  48 8B CB                        mov rcx, rbx
008EC1DC  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC1E1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC1E5  E8 2E 6F 07 00                  call 0x140963118
008EC1EA  8B D8                           mov ebx, eax
008EC1EC  E9 96 F9 FF FF                  jmp 0x1408ebb87
008EC1F1  48 8B CB                        mov rcx, rbx
008EC1F4  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC1F9  E8 E2 E7 1E 00                  call 0x140ada9e0
008EC1FE  8B D8                           mov ebx, eax
008EC200  E9 82 F9 FF FF                  jmp 0x1408ebb87
008EC205  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC20B  48 8B CB                        mov rcx, rbx
008EC20E  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC213  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC217  E8 D8 81 1E 00                  call 0x140ad43f4
008EC21C  8B D8                           mov ebx, eax
008EC21E  E9 64 F9 FF FF                  jmp 0x1408ebb87
008EC223  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC229  48 8B CB                        mov rcx, rbx
008EC22C  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC231  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC235  E8 5A 68 07 00                  call 0x140962a94
008EC23A  8B D8                           mov ebx, eax
008EC23C  E9 46 F9 FF FF                  jmp 0x1408ebb87
008EC241  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC247  48 8B CB                        mov rcx, rbx
008EC24A  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC24F  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC253  E8 00 D5 1E 00                  call 0x140ad9758
008EC258  8B D8                           mov ebx, eax
008EC25A  E9 28 F9 FF FF                  jmp 0x1408ebb87
008EC25F  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC265  48 8B CB                        mov rcx, rbx
008EC268  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC26D  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC271  E8 AE F5 1D 00                  call 0x140acb824
008EC276  8B D8                           mov ebx, eax
008EC278  E9 0A F9 FF FF                  jmp 0x1408ebb87
008EC27D  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC283  48 8B CB                        mov rcx, rbx
008EC286  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC28B  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC28F  E8 10 55 E1 FF                  call 0x1407017a4
008EC294  8B D8                           mov ebx, eax
008EC296  E9 EC F8 FF FF                  jmp 0x1408ebb87
008EC29B  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC2A1  48 8B CB                        mov rcx, rbx
008EC2A4  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC2A9  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC2AD  E8 DA 85 07 00                  call 0x14096488c
008EC2B2  8B D8                           mov ebx, eax
008EC2B4  E9 CE F8 FF FF                  jmp 0x1408ebb87
008EC2B9  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC2BF  48 8B CB                        mov rcx, rbx
008EC2C2  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC2C7  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC2CB  E8 14 52 E1 FF                  call 0x1407014e4
008EC2D0  8B D8                           mov ebx, eax
008EC2D2  E9 B0 F8 FF FF                  jmp 0x1408ebb87
008EC2D7  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC2DD  48 8B CB                        mov rcx, rbx
008EC2E0  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC2E5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC2E9  E8 92 A4 1E 00                  call 0x140ad6780
008EC2EE  8B D8                           mov ebx, eax
008EC2F0  E9 92 F8 FF FF                  jmp 0x1408ebb87
008EC2F5  8B 85 B0 00 00 00               mov eax, dword ptr [rbp + 0xb0]
008EC2FB  48 8B CB                        mov rcx, rbx
008EC2FE  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
008EC303  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008EC307  E8 A8 DB 1E 00                  call 0x140ad9eb4
008EC30C  8B D8                           mov ebx, eax
008EC30E  E9 74 F8 FF FF                  jmp 0x1408ebb87
008EC313  BB BB 00 00 C0                  mov ebx, 0xc00000bb
008EC318  E9 6A F8 FF FF                  jmp 0x1408ebb87
008EC31D  41 BC 06 00 00 00               mov r12d, 6
008EC323  E9 A5 F7 FF FF                  jmp 0x1408ebacd
008EC328  41 BC 11 00 00 00               mov r12d, 0x11
008EC32E  E9 9A F7 FF FF                  jmp 0x1408ebacd
008EC333  41 BC 18 00 00 00               mov r12d, 0x18
008EC339  E9 8F F7 FF FF                  jmp 0x1408ebacd
008EC33E  41 BC 19 00 00 00               mov r12d, 0x19
008EC344  E9 84 F7 FF FF                  jmp 0x1408ebacd
008EC349  41 BC 1B 00 00 00               mov r12d, 0x1b
008EC34F  E9 79 F7 FF FF                  jmp 0x1408ebacd
008EC354  41 BC 1C 00 00 00               mov r12d, 0x1c
008EC35A  E9 6E F7 FF FF                  jmp 0x1408ebacd
008EC35F  41 BC 1E 00 00 00               mov r12d, 0x1e
008EC365  E9 63 F7 FF FF                  jmp 0x1408ebacd
008EC36A  41 BC 20 00 00 00               mov r12d, 0x20
008EC370  E9 58 F7 FF FF                  jmp 0x1408ebacd
008EC375  41 BC 21 00 00 00               mov r12d, 0x21
008EC37B  E9 4D F7 FF FF                  jmp 0x1408ebacd
008EC380  41 BC 22 00 00 00               mov r12d, 0x22
008EC386  E9 42 F7 FF FF                  jmp 0x1408ebacd
008EC38B  41 BC 25 00 00 00               mov r12d, 0x25
008EC391  E9 37 F7 FF FF                  jmp 0x1408ebacd
008EC396  41 BD 06 00 00 00               mov r13d, 6
008EC39C  E9 2F F8 FF FF                  jmp 0x1408ebbd0
008EC3A1  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008EC3A6  E9 6C F7 FF FF                  jmp 0x1408ebb17
008EC3AB  8B 45 04                        mov eax, dword ptr [rbp + 4]
008EC3AE  4D 8B CE                        mov r9, r14
008EC3B1  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
008EC3B5  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
008EC3BA  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
008EC3BE  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
008EC3C3  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008EC3C7  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
008EC3CB  E9 68 F7 FF FF                  jmp 0x1408ebb38
008EC3D0  4C 8D 45 80                     lea r8, [rbp - 0x80]
008EC3D4  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
008EC3D9  45 8B C5                        mov r8d, r13d
008EC3DC  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
008EC3E1  E8 EA E6 DC FF                  call 0x1406baad0
008EC3E6  E9 98 F8 FF FF                  jmp 0x1408ebc83
008EC3EB  4C 8B E0                        mov r12, rax
008EC3EE  E9 BC F8 FF FF                  jmp 0x1408ebcaf
008EC3F3  49 8B C4                        mov rax, r12
008EC3F6  E8 D5 E6 DC FF                  call 0x1406baad0
008EC3FB  E9 3E F9 FF FF                  jmp 0x1408ebd3e
008EC400  8B 45 14                        mov eax, dword ptr [rbp + 0x14]
008EC403  4D 8B CE                        mov r9, r14
008EC406  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
008EC40A  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
008EC40F  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
008EC413  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
008EC418  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008EC41C  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
008EC420  E9 5F F9 FF FF                  jmp 0x1408ebd84
008EC425  0F 1F 00                        nop dword ptr [rax]
008EC428  CB                              retf
008EC429  BE 8E 00 AD BE                  mov esi, 0xbead008e
008EC42E  8E 00                           mov es, word ptr [rax]
008EC430  9E                              sahf
008EC431  BF 8E 00 37 C1                  mov edi, 0xc137008e
008EC436  8E 00                           mov es, word ptr [rax]
008EC438  6F                              outsd dx, dword ptr [rsi]
008EC439  C0 8E 00 D3 C1 8E 00            ror byte ptr [rsi - 0x713e2d00], 0
008EC440  06                              .byte 0x06
008EC441  BF 8E 00 19 C1                  mov edi, 0xc119008e
008EC446  8E 00                           mov es, word ptr [rax]
008EC448  F1                              int1
008EC449  C1 8E 00 05 C2 8E 00            ror dword ptr [rsi - 0x713dfb00], 0
008EC450  23 C2                           and eax, edx
008EC452  8E 00                           mov es, word ptr [rax]
008EC454  41 C2 8E 00                     ret 0x8e
008EC458  BD BF 8E 00 11                  mov ebp, 0x11008ebf
008EC45D  B9 8E 00 5F C2                  mov ecx, 0xc25f008e
008EC462  8E 00                           mov es, word ptr [rax]
008EC464  7D C2                           jge 0x1408ec428
008EC466  8E 00                           mov es, word ptr [rax]
008EC468  9B                              wait
008EC469  C2 8E 00                        ret 0x8e
008EC46C  F8                              clc
008EC46D  BF 8E 00 B9 C2                  mov edi, 0xc2b9008e
008EC472  8E 00                           mov es, word ptr [rax]
008EC474  65 BE 8E 00 D7 C2               mov esi, 0xc2d7008e
008EC47A  8E 00                           mov es, word ptr [rax]
008EC47C  FB                              sti
008EC47D  C0 8E 00 F5 C2 8E 00            ror byte ptr [rsi - 0x713d0b00], 0
008EC484  1E                              .byte 0x1e
008EC485  BE 8E 00 97 C1                  mov esi, 0xc197008e
008EC48A  8E 00                           mov es, word ptr [rax]
008EC48C  B5 C1                           mov ch, 0xc1
008EC48E  8E 00                           mov es, word ptr [rax]
008EC490  47 BE 8E 00 13 C3               mov r14d, 0xc313008e
008EC496  8E 00                           mov es, word ptr [rax]
008EC498  00 1B                           add byte ptr [rbx], bl
008EC49A  1B 1B                           sbb ebx, dword ptr [rbx]
008EC49C  01 1B                           add dword ptr [rbx], ebx
008EC49E  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4A0  02 1B                           add bl, byte ptr [rbx]
008EC4A2  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4A4  03 1B                           add ebx, dword ptr [rbx]
008EC4A6  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4A8  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4AA  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4AC  04 1B                           add al, 0x1b
008EC4AE  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4B0  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4B2  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4B4  05 1B 1B 1B 1B                  add eax, 0x1b1b1b1b
008EC4B9  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4BB  1B 06                           sbb eax, dword ptr [rsi]
008EC4BD  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4BF  1B 07                           sbb eax, dword ptr [rdi]
008EC4C1  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4C3  1B 08                           sbb ecx, dword ptr [rax]
008EC4C5  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4C7  1B 09                           sbb ecx, dword ptr [rcx]
008EC4C9  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4CB  1B 0A                           sbb ecx, dword ptr [rdx]
008EC4CD  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4CF  1B 0B                           sbb ecx, dword ptr [rbx]
008EC4D1  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4D3  1B 0C 1B                        sbb ecx, dword ptr [rbx + rbx]
008EC4D6  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4D8  0D 1B 1B 1B 0E                  or eax, 0xe1b1b1b
008EC4DD  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4DF  1B 0F                           sbb ecx, dword ptr [rdi]
008EC4E1  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4E3  1B 10                           sbb edx, dword ptr [rax]
008EC4E5  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4E7  1B 11                           sbb edx, dword ptr [rcx]
008EC4E9  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4EB  1B 12                           sbb edx, dword ptr [rdx]
008EC4ED  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4EF  1B 13                           sbb edx, dword ptr [rbx]
008EC4F1  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4F3  1B 14 1B                        sbb edx, dword ptr [rbx + rbx]
008EC4F6  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4F8  15 1B 1B 1B 16                  adc eax, 0x161b1b1b
008EC4FD  1B 1B                           sbb ebx, dword ptr [rbx]
008EC4FF  1B 17                           sbb edx, dword ptr [rdi]
008EC501  1B 1B                           sbb ebx, dword ptr [rbx]
008EC503  1B 18                           sbb ebx, dword ptr [rax]
008EC505  1B 1B                           sbb ebx, dword ptr [rbx]
008EC507  1B 19                           sbb ebx, dword ptr [rcx]
008EC509  1B 1B                           sbb ebx, dword ptr [rbx]
008EC50B  1B 1A                           sbb ebx, dword ptr [rdx]
008EC50D  0F 1F 00                        nop dword ptr [rax]
008EC510  16                              .byte 0x16
008EC511  C0 8E 00 FB BE 8E 00            ror byte ptr [rsi - 0x71410500], 0
008EC518  16                              .byte 0x16
008EC519  C0 8E 00 24 BF 8E 00            ror byte ptr [rsi - 0x7140dc00], 0
008EC520  76 C1                           jbe 0x1408ec4e3
008EC522  8E 00                           mov es, word ptr [rax]
008EC524  BF BA 8E 00 1D                  mov edi, 0x1d008eba
008EC529  C3                              ret
008EC52A  8E 00                           mov es, word ptr [rax]
008EC52C  55                              push rbp
008EC52D  C1 8E 00 5A BF 8E 00            ror dword ptr [rsi - 0x7140a600], 0
008EC534  16                              .byte 0x16
008EC535  C0 8E 00 16 C0 8E 00            ror byte ptr [rsi - 0x713fea00], 0
008EC53C  36 C0 8E 00 70 BF 8E 00         ror byte ptr ss:[rsi - 0x71409000], 0
008EC544  2F                              .byte 0x2f
008EC545  BF 8E 00 20 C0                  mov edi, 0xc020008e
008EC54A  8E 00                           mov es, word ptr [rax]
008EC54C  44 BF 8E 00 8D C0               mov edi, 0xc08d008e
008EC552  8E 00                           mov es, word ptr [rax]
008EC554  28 C3                           sub bl, al
008EC556  8E 00                           mov es, word ptr [rax]
008EC558  7B BF                           jnp 0x1408ec519
008EC55A  8E 00                           mov es, word ptr [rax]
008EC55C  4F BF 8E 00 6B C1 8E 00 2B C0   movabs r15, 0xc02b008ec16b008e
008EC566  8E 00                           mov es, word ptr [rax]
008EC568  B2 BF                           mov dl, 0xbf
008EC56A  8E 00                           mov es, word ptr [rax]
008EC56C  56                              push rsi
008EC56D  C0 8E 00 33 C3 8E 00            ror byte ptr [rsi - 0x713ccd00], 0
008EC574  3E C3                           ret
008EC576  8E 00                           mov es, word ptr [rax]
008EC578  8C C1                           mov ecx, es
008EC57A  8E 00                           mov es, word ptr [rax]
008EC57C  49 C3                           ret
008EC57E  8E 00                           mov es, word ptr [rax]
008EC580  54                              push rsp
008EC581  C3                              ret
008EC582  8E 00                           mov es, word ptr [rax]
008EC584  41 C0 8E 00 5F C3 8E 00         ror byte ptr [r14 - 0x713ca100], 0
008EC58C  60                              .byte 0x60
008EC58D  C1 8E 00 6A C3 8E 00            ror dword ptr [rsi - 0x713c9600], 0
008EC594  75 C3                           jne 0x1408ec559
008EC596  8E 00                           mov es, word ptr [rax]
008EC598  80 C3 8E                        add bl, 0x8e
008EC59B  00 D1                           add cl, dl
008EC59D  C0 8E 00 81 C1 8E 00            ror byte ptr [rsi - 0x713e7f00], 0
008EC5A4  8B C3                           mov eax, ebx
008EC5A6  8E 00                           mov es, word ptr [rax]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiCMHandleIoctl(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, unsigned int a6, unsigned int a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rsp;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m114;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (312);
    result = (*(unsigned __int64 *)(v_rip + 5369504)) ^ (v_rsp);
    v_stack_m58 = result;
    v_r13 = 0;
    *(unsigned int *)(a5) = 0;
    if (((unsigned int)((unsigned int)(a6))) == 0x470813ULL) goto loc_008EB92F;
    if (((unsigned int)((unsigned int)(a6))) == 0x47081BULL) goto loc_008EB9D8;
    if (((unsigned int)((unsigned int)(a6))) == 0x470823ULL) goto loc_008EBBAA;
    result = (unsigned int)(((unsigned int)(a6)) + (0xFFB8F7FDULL));
    if (((unsigned int)(result)) > 116) goto loc_008EC313;
    v_r10 = ((unsigned int)(*(unsigned int *)(v_rip - 9353464 + *(unsigned __int8 *)(v_rip - 9353464 + result * 1 + 9356440) * 4 + 9356328))) + (v_rip - 9353464);
loc_008EB92F:
    a2 = 0;
    result = memset(v_stack_mA8, a2, a2 + 72, a4);
    v_stack_m114 = 0;
    v_stack_m118 = 0;
    result = PiCMCapturePropertyInputData(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)(a7), v_stack_mA8);
    if (sign_flag) goto loc_008EBDA4;
    v_stack_m110 = v_stack_m98;
    if (v_stack_m98 == 0) goto loc_008EB9CE;
    if (v_stack_m78 != 0) goto loc_008EB9CE;
    if (v_stack_mA4 != 0) goto loc_008EB9CE;
    if (v_stack_m70 != 0) goto loc_008EB9CE;
    if (v_stack_m68 != 0) goto loc_008EB9CE;
    if (a3 == 0) goto loc_008EB9CE;
    if (((unsigned int)((unsigned int)(a4))) < 20) goto loc_008EB9CE;
    if (((unsigned int)((unsigned int)(v_stack_mA0))) == 1) goto loc_008EBBC2;
    if (((unsigned int)((unsigned int)(v_stack_mA0))) != 0x10002ULL) goto loc_008EBE04;
loc_008EB9BE:
    if ((*(unsigned __int64 *)(v_rip + 5745163)) != 0) goto loc_008EBBC7;
loc_008EB9CB:
    v_r13 = 0;
loc_008EB9CE:
    goto loc_008EBD63;
loc_008EB9D8:
    v_stack_m114 = 0;
    result = 0;
    v_stack_m118 = 0;
    v_stack_mA8 = v_xmm0;
    v_stack_m78 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    result = PiCMCaptureRegistryPropertyInputData((unsigned int)(v_stack_mA0), v_stack_m98, (unsigned int)(a7), v_stack_mA8);
    if (sign_flag) goto loc_008EBB58;
    if (v_stack_m98 == 0) goto loc_008EC016;
    if (v_stack_mA4 != 0) goto loc_008EC016;
    if (v_stack_m80 != 0) goto loc_008EC016;
    if (v_stack_m78 != 0) goto loc_008EC016;
    if (v_stack_m88 != 0) goto loc_008EC016;
    if (a3 == 0) goto loc_008EC016;
    if (((unsigned int)((unsigned int)(a4))) < 20) goto loc_008EC016;
    if ((unsigned int)((unsigned int)(a4) - 20) == 0) goto loc_008EBA84;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(a4) - 20)), (unsigned int)(0x34706E50ULL), v_stack_mA8);
    if (result == 0) goto loc_008EC3A1;
loc_008EBA84:
    if (((unsigned int)((int)(v_stack_m8C))) == 2) goto loc_008EBAC7;
    if (((unsigned int)((int)(v_stack_m8C))) == 9) goto loc_008EBDF9;
    if (((unsigned int)((int)(v_stack_m8C))) == 10) goto loc_008EBE3C;
    if (((unsigned int)((int)(v_stack_m8C))) > 37) goto loc_008EC016;
    result = ((unsigned int)(*(unsigned int *)(v_rip - 9353903 + (int)(v_stack_m8C) * 4 + 9356560))) + (v_rip - 9353903);
loc_008EBAC7:
loc_008EBACD:
    v_stack_m118 = (unsigned int)((unsigned int)(a4) - 20);
    if (((unsigned int)((unsigned int)(v_stack_mA0))) != 1) goto loc_008EC098;
    v_stack_m140 = 0;
    v_stack_m148 = v_stack_m118;
    a3 = 0;
    v_stack_m150 = result;
    v_stack_m158 = v_stack_m114;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 5744820), v_stack_m98, a3, 2);
loc_008EBB0D:
    if (!sign_flag) goto loc_008EC3AB;
loc_008EBB17:
    a4 = 0;
    v_stack_m138 = a5;
    v_stack_m140 = (unsigned int)((unsigned int)(a4));
    v_stack_m148 = 0;
    v_stack_m150 = (unsigned int)((unsigned int)(v_stack_m74));
    v_stack_m158 = 0;
loc_008EBB38:
    result = PiCMReturnBufferResultData((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(v_stack_m118), (unsigned int)(v_stack_m114), a4);
    if (result != 0) {
        a2 = 0x34706E50ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(v_stack_m114), a4);
    }
    if (v_stack_m98 == 0) goto loc_008EBB7A;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_008EBDED;
loc_008EBB7A:
    if (v_stack_m80 != 0) goto loc_008EC061;
loc_008EBB87:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m80, (unsigned int)(v_stack_m114), a4);
    v_rsp = (v_rsp) + (312);
    return result;
loc_008EBBAA:
    v_stack_p28 = a5;
    v_stack_p20 = (unsigned int)((unsigned int)(a7));
    result = PiCMGetRelatedDeviceInstance(a1, v_stack_m80, (unsigned int)(v_stack_m114), a4);
    goto loc_008EBB87;
loc_008EBBC2:
    goto loc_008EBBD0;
loc_008EBBC7:
    if (2 == 0) goto loc_008EB9CB;
loc_008EBBD0:
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562) - 20) == 0) goto loc_008EBBFA;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562) - 20)), (unsigned int)(0x34706E50ULL), a4);
    if (result == 0) goto loc_008EBF3A;
loc_008EBBFA:
    a4 = 0;
    v_stack_mD8 = v_stack_m8C;
    v_stack_p70 = *(unsigned __int64 *)(v_rip + 5744535);
    v_stack_mD0 = v_stack_p64;
    v_stack_mB8 = v_stack_p60;
    v_stack_mF8 = 0;
    v_stack_mF0 = 0;
    v_stack_mBC = 0;
    v_stack_mB0 = 0;
    v_stack_p78 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5744535) + 488);
    v_stack_mE8 = v_xmm0;
    v_stack_mC8 = result;
    v_stack_mC0 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562) - 20);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5744535) + 488) == 0) goto loc_008EC3EB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5744535) + 488)) != (v_rip - 37902)) goto loc_008EC3D0;
    v_stack_p28 = v_stack_mF8;
    v_stack_p20 = 2;
    result = PiPnpRtlObjectActionCallback(*(unsigned __int64 *)(v_rip + 5744535), v_stack_p68, 2, 8);
loc_008EBC83:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008EBF86;
    if (((unsigned int)(result)) != 0xC0000120ULL) goto loc_008EBC9D;
loc_008EBC95:
    goto loc_008EBD58;
loc_008EBC9D:
    if ((unsigned int)(result) != 0) goto loc_008EC04C;
loc_008EBCAF:
    v_stack_p50 = (unsigned int)((unsigned int)(v_stack_mB0));
    v_stack_p48 = v_stack_mB8;
    v_stack_p40 = (unsigned int)((unsigned int)(v_stack_mC0));
    v_stack_p38 = v_stack_mC8;
    v_stack_p30 = v_stack_mD0;
    v_stack_p28 = v_stack_mD8;
    v_stack_p20 = v_stack_mE0;
    result = PnpGetObjectPropertyWorker(v_stack_p70, v_stack_p68, 2, v_stack_mE8);
    if (v_stack_p78 == 0) goto loc_008EBD58;
    v_stack_mF8 = (unsigned int)(result);
    v_stack_p28 = v_stack_mF8;
    v_stack_p20 = 2;
    if (v_stack_p78 != (v_rip - 38095)) goto loc_008EC3F3;
    result = PiPnpRtlObjectActionCallback(v_stack_p70, v_stack_p68, 2, 8);
loc_008EBD3E:
    if (((unsigned int)(result)) == 0xC0000002ULL) goto loc_008EBD58;
    if (((unsigned int)(result)) == 0xC0000120ULL) goto loc_008EBC95;
    if ((unsigned int)(result) != 0) goto loc_008EC04C;
loc_008EBD58:
    if (!sign_flag) goto loc_008EC400;
loc_008EBD60:
    v_r13 = 0;
loc_008EBD63:
    a4 = 0;
    v_stack_p40 = a5;
    v_stack_p38 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_p30 = 0;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_m64));
    v_stack_p20 = 0;
loc_008EBD84:
    result = PiCMReturnBufferResultData((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(v_stack_p60), (unsigned int)(v_stack_p64), a4);
    if (result != 0) {
        a2 = 0x34706E50ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(v_stack_p64), a4);
    }
    if (v_stack_m98 == 0) goto loc_008EBDC2;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_008EBDE4;
loc_008EBDC2:
    if (v_stack_m70 == 0) goto loc_008EBB87;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008EBB87;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m70, a2, (unsigned int)(v_stack_p64), a4);
    goto loc_008EBB87;
loc_008EBDE4:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m70, a2, (unsigned int)(v_stack_p64), a4);
    goto loc_008EBDC2;
loc_008EBDED:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m70, a2, (unsigned int)(v_stack_p64), a4);
    goto loc_008EBB7A;
loc_008EBDF9:
    goto loc_008EBACD;
loc_008EBE04:
    if (((unsigned int)(v_stack_m70)) <= 6) goto loc_008EBE83;
    a1 = (unsigned int)((v_stack_m70) - (0x10001ULL));
    if (condition_is_not_equal) goto loc_008EBEE9;
    goto loc_008EB9BE;
loc_008EBE3C:
    goto loc_008EBACD;
loc_008EBE83:
    if (condition_is_equal) goto loc_008EC396;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_008EBF93;
    a1 = (unsigned int)((a1) - (10));
    if (condition_is_equal) goto loc_008EBF65;
    a1 = (unsigned int)((a1) - (10));
    if (condition_is_not_equal) goto loc_008EC0DC;
    goto loc_008EBBD0;
loc_008EBEE9:
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_not_equal) goto loc_008EBFDB;
    goto loc_008EB9BE;
loc_008EBF3A:
    goto loc_008EBD60;
loc_008EBF65:
    goto loc_008EBBD0;
loc_008EBF86:
    v_r12 = 0;
    goto loc_008EBCAF;
loc_008EBF93:
    goto loc_008EBBD0;
loc_008EBFDB:
    a1 = (unsigned int)((v_stack_p70) - (0));
    if (condition_is_equal) goto loc_008EC0F0;
    if (((unsigned int)(a1)) != 0) goto loc_008EB9CE;
    goto loc_008EB9BE;
loc_008EC016:
    goto loc_008EBB17;
loc_008EC04C:
    goto loc_008EBD60;
loc_008EC061:
    result = PiControlFreeUserModeCallersBuffer((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a2, (unsigned int)(v_stack_p64), a4);
    goto loc_008EBB87;
loc_008EC098:
    if (((unsigned int)(result)) != 2) goto loc_008EC016;
    v_stack_p30 = v_stack_p60;
    v_stack_p28 = result;
    a3 = 0;
    v_stack_p20 = v_stack_p64;
    result = CmGetInstallerClassRegProp(*(unsigned __int64 *)(v_rip + 5743344), a2, a3, 0);
    goto loc_008EBB0D;
loc_008EC0DC:
    if (((unsigned int)(*(unsigned __int64 *)(v_rip + 5743344))) != 0) goto loc_008EB9CE;
    goto loc_008EBBD0;
loc_008EC0F0:
    goto loc_008EB9BE;
loc_008EC313:
    goto loc_008EBB87;
loc_008EC396:
    goto loc_008EBBD0;
loc_008EC3A1:
    goto loc_008EBB17;
loc_008EC3AB:
    v_stack_p40 = a5;
    v_stack_p38 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_p30 = 0;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_m74));
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p60));
    goto loc_008EBB38;
loc_008EC3D0:
    v_stack_p28 = v_stack_mF8;
    v_stack_p20 = 0;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 5743344), (unsigned int)(v_stack_p60), 6, result);
    goto loc_008EBC83;
loc_008EC3EB:
    goto loc_008EBCAF;
loc_008EC3F3:
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 5743344), (unsigned int)(v_stack_p60), 6, result);
    goto loc_008EBD3E;
loc_008EC400:
    v_stack_p40 = a5;
    v_stack_p38 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_p30 = 0;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_m64));
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p60));
    goto loc_008EBD84;
}
```

## 5. (Beta) C Style

```c
int64_t PiCMHandleIoctl(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, void *Arg5, uint32_t Arg6, uint32_t Arg7)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rsp;
    uint64_t v_stack_m110;
    uint32_t v_stack_m114;
    uint32_t v_stack_m118;
    uint64_t v_stack_m138;
    uint32_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint32_t v_stack_m158;
    uint64_t v_stack_m58;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p64;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (312);
    result = (*(uint64_t *)(v_rip + 0x51EEA0)) ^ (local_rsp);
    v_stack_m58 = result;
    local_r13 = 0;
    *(uint32_t *)(arg5) = 0;
    if (((uint32_t)((uint32_t)(Arg6))) == 0x470813ULL) goto loc_008EB92F;
    if (((uint32_t)((uint32_t)(Arg6))) == 0x47081BULL) goto loc_008EB9D8;
    if (((uint32_t)((uint32_t)(Arg6))) == 0x470823ULL) goto loc_008EBBAA;
    result = (uint32_t)(((uint32_t)(Arg6)) + (0xFFB8F7FDULL));
    if (((uint32_t)(result)) > 116) goto loc_008EC313;
    local_r10 = ((uint32_t)(*(uint32_t *)(v_rip - 0x8EB8F8 + *(uint8_t *)(v_rip - 0x8EB8F8 + result * 1 + 0x8EC498) * 4 + 0x8EC428))) + (v_rip - 9353464);
loc_008EB92F:
    Arg2 = 0;
    result = memset(v_stack_mA8, Arg2, Arg2 + 72, Arg4);
    v_stack_m114 = 0;
    v_stack_m118 = 0;
    result = PiCMCapturePropertyInputData(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)(Arg7), v_stack_mA8);
    if (sign_flag) goto loc_008EBDA4;
    v_stack_m110 = v_stack_m98;
    if (v_stack_m98 == 0) goto loc_008EB9CE;
    if (v_stack_m78 != 0) goto loc_008EB9CE;
    if (v_stack_mA4 != 0) goto loc_008EB9CE;
    if (v_stack_m70 != 0) goto loc_008EB9CE;
    if (v_stack_m68 != 0) goto loc_008EB9CE;
    if (Arg3 == 0) goto loc_008EB9CE;
    if (((uint32_t)((uint32_t)(Arg4))) < 20) goto loc_008EB9CE;
    if (((uint32_t)((uint32_t)(v_stack_mA0))) == 1) goto loc_008EBBC2;
    if (((uint32_t)((uint32_t)(v_stack_mA0))) != 0x10002ULL) goto loc_008EBE04;
loc_008EB9BE:
    if ((*(uint64_t *)(v_rip + 0x57AA0B)) != 0) goto loc_008EBBC7;
loc_008EB9CB:
    local_r13 = 0;
loc_008EB9CE:
    goto loc_008EBD63;
loc_008EB9D8:
    v_stack_m114 = 0;
    result = 0;
    v_stack_m118 = 0;
    v_stack_mA8 = v_xmm0;
    v_stack_m78 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    result = PiCMCaptureRegistryPropertyInputData((uint32_t)(v_stack_mA0), v_stack_m98, (uint32_t)(Arg7), v_stack_mA8);
    if (sign_flag) goto loc_008EBB58;
    if (v_stack_m98 == 0) goto loc_008EC016;
    if (v_stack_mA4 != 0) goto loc_008EC016;
    if (v_stack_m80 != 0) goto loc_008EC016;
    if (v_stack_m78 != 0) goto loc_008EC016;
    if (v_stack_m88 != 0) goto loc_008EC016;
    if (Arg3 == 0) goto loc_008EC016;
    if (((uint32_t)((uint32_t)(Arg4))) < 20) goto loc_008EC016;
    if ((uint32_t)((uint32_t)(Arg4) - 20) == 0) goto loc_008EBA84;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(Arg4) - 20)), (uint32_t)(0x34706E50ULL), v_stack_mA8);
    if (result == 0) goto loc_008EC3A1;
loc_008EBA84:
    if (((uint32_t)((int32_t)(v_stack_m8C))) == 2) goto loc_008EBAC7;
    if (((uint32_t)((int32_t)(v_stack_m8C))) == 9) goto loc_008EBDF9;
    if (((uint32_t)((int32_t)(v_stack_m8C))) == 10) goto loc_008EBE3C;
    if (((uint32_t)((int32_t)(v_stack_m8C))) > 37) goto loc_008EC016;
    result = ((uint32_t)(*(uint32_t *)(v_rip - 0x8EBAAF + (int32_t)(v_stack_m8C) * 4 + 0x8EC510))) + (v_rip - 9353903);
loc_008EBAC7:
loc_008EBACD:
    v_stack_m118 = (uint32_t)((uint32_t)(Arg4) - 20);
    if (((uint32_t)((uint32_t)(v_stack_mA0))) != 1) goto loc_008EC098;
    v_stack_m140 = 0;
    v_stack_m148 = v_stack_m118;
    Arg3 = 0;
    v_stack_m150 = result;
    v_stack_m158 = v_stack_m114;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x57A8B4), v_stack_m98, Arg3, 2);
loc_008EBB0D:
    if (!sign_flag) goto loc_008EC3AB;
loc_008EBB17:
    Arg4 = 0;
    v_stack_m138 = Arg5;
    v_stack_m140 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m148 = 0;
    v_stack_m150 = (uint32_t)((uint32_t)(v_stack_m74));
    v_stack_m158 = 0;
loc_008EBB38:
    result = PiCMReturnBufferResultData((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(v_stack_m118), (uint32_t)(v_stack_m114), Arg4);
    if (result != 0) {
        Arg2 = 0x34706E50ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(v_stack_m114), Arg4);
    }
    if (v_stack_m98 == 0) goto loc_008EBB7A;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_008EBDED;
loc_008EBB7A:
    if (v_stack_m80 != 0) goto loc_008EC061;
loc_008EBB87:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m80, (uint32_t)(v_stack_m114), Arg4);
    local_rsp = (local_rsp) + (312);
    return result;
loc_008EBBAA:
    v_stack_p28 = Arg5;
    v_stack_p20 = (uint32_t)((uint32_t)(Arg7));
    result = PiCMGetRelatedDeviceInstance(Arg1, v_stack_m80, (uint32_t)(v_stack_m114), Arg4);
    goto loc_008EBB87;
loc_008EBBC2:
    goto loc_008EBBD0;
loc_008EBBC7:
    if (2 == 0) goto loc_008EB9CB;
loc_008EBBD0:
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232) - 20) == 0) goto loc_008EBBFA;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232) - 20)), (uint32_t)(0x34706E50ULL), Arg4);
    if (result == 0) goto loc_008EBF3A;
loc_008EBBFA:
    Arg4 = 0;
    v_stack_mD8 = v_stack_m8C;
    v_stack_p70 = *(uint64_t *)(v_rip + 0x57A797);
    v_stack_mD0 = v_stack_p64;
    v_stack_mB8 = v_stack_p60;
    v_stack_mF8 = 0;
    v_stack_mF0 = 0;
    v_stack_mBC = 0;
    v_stack_mB0 = 0;
    v_stack_p78 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x57A797) + 0x1E8);
    v_stack_mE8 = v_xmm0;
    v_stack_mC8 = result;
    v_stack_mC0 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232) - 20);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x57A797) + 0x1E8) == 0) goto loc_008EC3EB;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x57A797) + 0x1E8)) != (v_rip - 37902)) goto loc_008EC3D0;
    v_stack_p28 = v_stack_mF8;
    v_stack_p20 = 2;
    result = PiPnpRtlObjectActionCallback(*(uint64_t *)(v_rip + 0x57A797), v_stack_p68, 2, 8);
loc_008EBC83:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008EBF86;
    if (((uint32_t)(result)) != 0xC0000120ULL) goto loc_008EBC9D;
loc_008EBC95:
    goto loc_008EBD58;
loc_008EBC9D:
    if ((uint32_t)(result) != 0) goto loc_008EC04C;
loc_008EBCAF:
    v_stack_p50 = (uint32_t)((uint32_t)(v_stack_mB0));
    v_stack_p48 = v_stack_mB8;
    v_stack_p40 = (uint32_t)((uint32_t)(v_stack_mC0));
    v_stack_p38 = v_stack_mC8;
    v_stack_p30 = v_stack_mD0;
    v_stack_p28 = v_stack_mD8;
    v_stack_p20 = v_stack_mE0;
    result = PnpGetObjectPropertyWorker(v_stack_p70, v_stack_p68, 2, v_stack_mE8);
    if (v_stack_p78 == 0) goto loc_008EBD58;
    v_stack_mF8 = (uint32_t)(result);
    v_stack_p28 = v_stack_mF8;
    v_stack_p20 = 2;
    if (v_stack_p78 != (v_rip - 38095)) goto loc_008EC3F3;
    result = PiPnpRtlObjectActionCallback(v_stack_p70, v_stack_p68, 2, 8);
loc_008EBD3E:
    if (((uint32_t)(result)) == 0xC0000002ULL) goto loc_008EBD58;
    if (((uint32_t)(result)) == 0xC0000120ULL) goto loc_008EBC95;
    if ((uint32_t)(result) != 0) goto loc_008EC04C;
loc_008EBD58:
    if (!sign_flag) goto loc_008EC400;
loc_008EBD60:
    local_r13 = 0;
loc_008EBD63:
    Arg4 = 0;
    v_stack_p40 = Arg5;
    v_stack_p38 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_p30 = 0;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_m64));
    v_stack_p20 = 0;
loc_008EBD84:
    result = PiCMReturnBufferResultData((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(v_stack_p60), (uint32_t)(v_stack_p64), Arg4);
    if (result != 0) {
        Arg2 = 0x34706E50ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(v_stack_p64), Arg4);
    }
    if (v_stack_m98 == 0) goto loc_008EBDC2;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_008EBDE4;
loc_008EBDC2:
    if (v_stack_m70 == 0) goto loc_008EBB87;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008EBB87;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m70, Arg2, (uint32_t)(v_stack_p64), Arg4);
    goto loc_008EBB87;
loc_008EBDE4:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m70, Arg2, (uint32_t)(v_stack_p64), Arg4);
    goto loc_008EBDC2;
loc_008EBDED:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m70, Arg2, (uint32_t)(v_stack_p64), Arg4);
    goto loc_008EBB7A;
loc_008EBDF9:
    goto loc_008EBACD;
loc_008EBE04:
    if (((uint32_t)(v_stack_m70)) <= 6) goto loc_008EBE83;
    Arg1 = (uint32_t)((v_stack_m70) - (0x10001ULL));
    if (condition_is_not_equal) goto loc_008EBEE9;
    goto loc_008EB9BE;
loc_008EBE3C:
    goto loc_008EBACD;
loc_008EBE83:
    if (condition_is_equal) goto loc_008EC396;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_008EBF93;
    Arg1 = (uint32_t)((Arg1) - (10));
    if (condition_is_equal) goto loc_008EBF65;
    Arg1 = (uint32_t)((Arg1) - (10));
    if (condition_is_not_equal) goto loc_008EC0DC;
    goto loc_008EBBD0;
loc_008EBEE9:
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_not_equal) goto loc_008EBFDB;
    goto loc_008EB9BE;
loc_008EBF3A:
    goto loc_008EBD60;
loc_008EBF65:
    goto loc_008EBBD0;
loc_008EBF86:
    local_r12 = 0;
    goto loc_008EBCAF;
loc_008EBF93:
    goto loc_008EBBD0;
loc_008EBFDB:
    Arg1 = (uint32_t)((v_stack_p70) - (0));
    if (condition_is_equal) goto loc_008EC0F0;
    if (((uint32_t)(Arg1)) != 0) goto loc_008EB9CE;
    goto loc_008EB9BE;
loc_008EC016:
    goto loc_008EBB17;
loc_008EC04C:
    goto loc_008EBD60;
loc_008EC061:
    result = PiControlFreeUserModeCallersBuffer((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg2, (uint32_t)(v_stack_p64), Arg4);
    goto loc_008EBB87;
loc_008EC098:
    if (((uint32_t)(result)) != 2) goto loc_008EC016;
    v_stack_p30 = v_stack_p60;
    v_stack_p28 = result;
    Arg3 = 0;
    v_stack_p20 = v_stack_p64;
    result = CmGetInstallerClassRegProp(*(uint64_t *)(v_rip + 0x57A2F0), Arg2, Arg3, 0);
    goto loc_008EBB0D;
loc_008EC0DC:
    if (((uint32_t)(*(uint64_t *)(v_rip + 0x57A2F0))) != 0) goto loc_008EB9CE;
    goto loc_008EBBD0;
loc_008EC0F0:
    goto loc_008EB9BE;
loc_008EC313:
    goto loc_008EBB87;
loc_008EC396:
    goto loc_008EBBD0;
loc_008EC3A1:
    goto loc_008EBB17;
loc_008EC3AB:
    v_stack_p40 = Arg5;
    v_stack_p38 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_p30 = 0;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_m74));
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p60));
    goto loc_008EBB38;
loc_008EC3D0:
    v_stack_p28 = v_stack_mF8;
    v_stack_p20 = 0;
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0x57A2F0), (uint32_t)(v_stack_p60), 6, result);
    goto loc_008EBC83;
loc_008EC3EB:
    goto loc_008EBCAF;
loc_008EC3F3:
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0x57A2F0), (uint32_t)(v_stack_p60), 6, result);
    goto loc_008EBD3E;
loc_008EC400:
    v_stack_p40 = Arg5;
    v_stack_p38 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_p30 = 0;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_m64));
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p60));
    goto loc_008EBD84;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008EB880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
