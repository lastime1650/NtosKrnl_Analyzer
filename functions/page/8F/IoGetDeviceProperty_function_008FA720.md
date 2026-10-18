# IoGetDeviceProperty

- RVA: `0x008FA720`–`0x008FAC65` (길이 `1,349` bytes)
- VA: `0x00000001408FA720`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00087D2C`
- 디코드: `328`개 명령, `1,349/1,349` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **20**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008FA76E` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008FA804` → [PiGetDeviceRegProperty](PiGetDeviceRegProperty_function_008FAC6C.md) (function, `0x008FAC6C`)
- `0x008FA820` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008FA883` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008FA8A9` → [ObQueryNameStringMode](../8A/ObQueryNameStringMode_function_008A7ED0.md) (function, `0x008A7ED0`)
- `0x008FA8C7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008FA96E` → [PpHotSwapGetDevnodeRemovalPolicy](PpHotSwapGetDevnodeRemovalPolicy_function_008FB1B4.md) (function, `0x008FB1B4`)
- `0x008FA990` → [PpIrpQueryCapabilities](PpIrpQueryCapabilities_function_008FAF8C.md) (function, `0x008FAF8C`)
- `0x008FAA54` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x008FAAD7` → [PnpBusTypeGuidGet](PnpBusTypeGuidGet_function_008FC720.md) (function, `0x008FC720`)
- `0x008FAB43` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008FAB9A` → [PnpDetermineResourceListSize](PnpDetermineResourceListSize_function_008FC6F8.md) (function, `0x008FC6F8`)
- `0x008FABB8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [PoStoreRequester](../../text/23/PoStoreRequester_function_002304D4.md) at `0x0023061B`
- [PoStoreRequester](../../text/23/PoStoreRequester_function_002304D4.md) at `0x0023062B`
- [HalpDmaGetReservedRegionsForDeviceResources](../../text/55/HalpDmaGetReservedRegionsForDeviceResources_function_00552018.md) at `0x005520A3`
- [HalpDmaGetReservedRegionsForDeviceResources](../../text/55/HalpDmaGetReservedRegionsForDeviceResources_function_00552018.md) at `0x005520E0`
- [PiRebalanceOptOut](../../text/5A/PiRebalanceOptOut_function_005AA664.md) at `0x005AA72D`
- [KseDsCallbackHookAddDevice](../../text/5C/KseDsCallbackHookAddDevice_function_005CBEB0.md) at `0x005CBF24`
- [ArbQueryConflict](../70/ArbQueryConflict_function_0070F410.md) at `0x0070F558`
- [ArbQueryConflict](../70/ArbQueryConflict_function_0070F410.md) at `0x0070F57F`
- [ArbShareDriverExclusive](../70/ArbShareDriverExclusive_function_0070FB1C.md) at `0x0070FB87`
- [ArbShareDriverExclusive](../70/ArbShareDriverExclusive_function_0070FB1C.md) at `0x0070FC56`
- [IoGetDmaAdapter](../72/IoGetDmaAdapter_function_00729450.md) at `0x00729529`
- [IopIsPciRootBus](../72/IopIsPciRootBus_function_0072EF40.md) at `0x0072EF74`
- [IopIsPciRootBus](../72/IopIsPciRootBus_function_0072EF40.md) at `0x0072EFC1`
- [PopRegisterTargetDeviceProtection](../75/PopRegisterTargetDeviceProtection_function_00756A94.md) at `0x00756AF5`
- [PopRegisterTargetDeviceProtection](../75/PopRegisterTargetDeviceProtection_function_00756A94.md) at `0x00756B45`
- [PopRegisterCoolingExtensionProtection](../75/PopRegisterCoolingExtensionProtection_function_007575D0.md) at `0x00757640`
- [PopRegisterCoolingExtensionProtection](../75/PopRegisterCoolingExtensionProtection_function_007575D0.md) at `0x00757693`
- [PopWakeSourceGetDeviceProperty](../75/PopWakeSourceGetDeviceProperty_function_0075CA08.md) at `0x0075CA3B`
- [PopWakeSourceGetDeviceProperty](../75/PopWakeSourceGetDeviceProperty_function_0075CA08.md) at `0x0075CA7A`
- [IoWMISuggestInstanceName](../7B/IoWMISuggestInstanceName_function_007B2520.md) at `0x007B2595`
- [IoWMISuggestInstanceName](../7B/IoWMISuggestInstanceName_function_007B2520.md) at `0x007B25DB`
- [PiControlGetPropertyData](PiControlGetPropertyData_function_008FA330.md) at `0x008FA456`
- [IopProcessSetInterfaceState](../95/IopProcessSetInterfaceState_function_00950964.md) at `0x00950E80`
- [IopQueryDeviceHardwareIdForPdcTask](../95/IopQueryDeviceHardwareIdForPdcTask_function_00953500.md) at `0x00953527`
- [IopQueryDeviceHardwareIdForPdcTask](../95/IopQueryDeviceHardwareIdForPdcTask_function_00953500.md) at `0x00953578`
- [SshpGenerateDeviceFriendlyName](../A2/SshpGenerateDeviceFriendlyName_function_00A2E184.md) at `0x00A2E1EC`
- [SshpGenerateDeviceFriendlyName](../A2/SshpGenerateDeviceFriendlyName_function_00A2E184.md) at `0x00A2E277`
- [SshpGenerateDeviceVerboseDescription](../A2/SshpGenerateDeviceVerboseDescription_function_00A2E448.md) at `0x00A2E491`
- [SshpGenerateDeviceVerboseDescription](../A2/SshpGenerateDeviceVerboseDescription_function_00A2E448.md) at `0x00A2E4C2`
- [SshpGenerateDeviceVerboseDescription](../A2/SshpGenerateDeviceVerboseDescription_function_00A2E448.md) at `0x00A2E4EB`
- [SshpGenerateDeviceVerboseDescription](../A2/SshpGenerateDeviceVerboseDescription_function_00A2E448.md) at `0x00A2E5F8`
- [SshpGenerateDeviceVerboseDescription](../A2/SshpGenerateDeviceVerboseDescription_function_00A2E448.md) at `0x00A2E639`
- [SshpGenerateDeviceVerboseDescription](../A2/SshpGenerateDeviceVerboseDescription_function_00A2E448.md) at `0x00A2E68B`
- [PopGenerateDeviceFriendlyName](../A9/PopGenerateDeviceFriendlyName_function_00A98968.md) at `0x00A98A7A`
- [PopGenerateDeviceFriendlyName](../A9/PopGenerateDeviceFriendlyName_function_00A98968.md) at `0x00A98B05`
- [PopDiagQueryDevicePropertyString](../AA/PopDiagQueryDevicePropertyString_function_00AA2014.md) at `0x00AA2046`
- [PopDiagQueryDevicePropertyString](../AA/PopDiagQueryDevicePropertyString_function_00AA2014.md) at `0x00AA2091`
- [VfIsPCIBus](../../pagevrfy/B9/VfIsPCIBus_function_00B97274.md) at `0x00B972B3`

### Static image references
- `0x008FA73C` → RVA `0x00E0A740` (`.data`; read)
- `0x008FA9FA` → RVA `0x00F8C438` (`.data`; read)
- `0x008FAA1A` → RVA `0x00E66398` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x008FA76E` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008FA820` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008FA883` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008FA8C7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008FAB43` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008FABB8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x008FAB7B` → [sub_00B1F43A](../B1/Unknown_function_00B1F43A.md) (`tail-transfer`)
  - `0x008FABF4` → [sub_00B1F43A + 0x90](../B1/Unknown_function_00B1F43A.md) (`tail-transfer`)
  - `0x008FABFD` → [sub_00B1F43A + 0x1C](../B1/Unknown_function_00B1F43A.md) (`tail-transfer`)
  - `0x008FAC51` → [sub_00B1F43A + 0xDF](../B1/Unknown_function_00B1F43A.md) (`tail-transfer`)
  - `0x008FAC60` → [sub_00B1F43A + 0xDF](../B1/Unknown_function_00B1F43A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008FA720  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
008FA725  55                              push rbp
008FA726  56                              push rsi
008FA727  57                              push rdi
008FA728  41 54                           push r12
008FA72A  41 55                           push r13
008FA72C  41 56                           push r14
008FA72E  41 57                           push r15
008FA730  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
008FA735  48 81 EC C0 00 00 00            sub rsp, 0xc0
008FA73C  48 8B 05 FD FF 50 00            mov rax, qword ptr [rip + 0x50fffd]
008FA743  48 33 C4                        xor rax, rsp
008FA746  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
008FA74A  4C 8B 75 7F                     mov r14, qword ptr [rbp + 0x7f]
008FA74E  8B DA                           mov ebx, edx
008FA750  33 D2                           xor edx, edx
008FA752  48 89 4D AF                     mov qword ptr [rbp - 0x51], rcx
008FA756  45 8B E8                        mov r13d, r8d
008FA759  48 8B F9                        mov rdi, rcx
008FA75C  0F 57 C0                        xorps xmm0, xmm0
008FA75F  48 8D 4D CF                     lea rcx, [rbp - 0x31]
008FA763  4D 8B E1                        mov r12, r9
008FA766  44 8D 42 40                     lea r8d, [rdx + 0x40]
008FA76A  0F 11 45 B7                     movups xmmword ptr [rbp - 0x49], xmm0
008FA76E  E8 CD C4 DC FF                  call 0x1406c6c40
008FA773  33 D2                           xor edx, edx
008FA775  81 E3 FF 0F 00 00               and ebx, 0xfff
008FA77B  89 55 A7                        mov dword ptr [rbp - 0x59], edx
008FA77E  89 55 A3                        mov dword ptr [rbp - 0x5d], edx
008FA781  41 89 16                        mov dword ptr [r14], edx
008FA784  48 85 FF                        test rdi, rdi
008FA787  0F 84 B4 00 00 00               je 0x1408fa841
008FA78D  48 8B 87 38 01 00 00            mov rax, qword ptr [rdi + 0x138]
008FA794  48 8B 70 28                     mov rsi, qword ptr [rax + 0x28]
008FA798  48 85 F6                        test rsi, rsi
008FA79B  0F 84 A4 04 00 00               je 0x1408fac45
008FA7A1  F7 86 8C 01 00 00 00 00 02 00   test dword ptr [rsi + 0x18c], 0x20000
008FA7AB  0F 85 94 04 00 00               jne 0x1408fac45
008FA7B1  83 FB 0B                        cmp ebx, 0xb
008FA7B4  0F 87 8E 00 00 00               ja 0x1408fa848
008FA7BA  0F 84 AF 00 00 00               je 0x1408fa86f
008FA7C0  83 FB 05                        cmp ebx, 5
008FA7C3  0F 84 96 00 00 00               je 0x1408fa85f
008FA7C9  0F 87 58 01 00 00               ja 0x1408fa927
008FA7CF  85 DB                           test ebx, ebx
008FA7D1  0F 84 43 01 00 00               je 0x1408fa91a
008FA7D7  83 EB 01                        sub ebx, 1
008FA7DA  0F 85 87 03 00 00               jne 0x1408fab67
008FA7E0  8D 7A 07                        lea edi, [rdx + 7]
008FA7E3  44 8D 7A 02                     lea r15d, [rdx + 2]
008FA7E7  48 39 56 30                     cmp qword ptr [rsi + 0x30], rdx
008FA7EB  74 54                           je 0x1408fa841
008FA7ED  45 89 2E                        mov dword ptr [r14], r13d
008FA7F0  45 8B CF                        mov r9d, r15d
008FA7F3  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
008FA7F7  44 8B C7                        mov r8d, edi
008FA7FA  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
008FA7FF  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
008FA804  E8 63 04 00 00                  call 0x1408fac6c
008FA809  8B D8                           mov ebx, eax
008FA80B  3D 25 02 00 C0                  cmp eax, 0xc0000225
008FA810  75 05                           jne 0x1408fa817
008FA812  BB 34 00 00 C0                  mov ebx, 0xc0000034
008FA817  8B C3                           mov eax, ebx
008FA819  48 8B 4D 0F                     mov rcx, qword ptr [rbp + 0xf]
008FA81D  48 33 CC                        xor rcx, rsp
008FA820  E8 1B 1E DB FF                  call 0x1406ac640
008FA825  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
008FA82D  48 81 C4 C0 00 00 00            add rsp, 0xc0
008FA834  41 5F                           pop r15
008FA836  41 5E                           pop r14
008FA838  41 5D                           pop r13
008FA83A  41 5C                           pop r12
008FA83C  5F                              pop rdi
008FA83D  5E                              pop rsi
008FA83E  5D                              pop rbp
008FA83F  C3                              ret
008FA840  CC                              int3
008FA841  BB 10 00 00 C0                  mov ebx, 0xc0000010
008FA846  EB CF                           jmp 0x1408fa817
008FA848  41 BF 11 00 00 00               mov r15d, 0x11
008FA84E  41 3B DF                        cmp ebx, r15d
008FA851  0F 87 EB 00 00 00               ja 0x1408fa942
008FA857  75 78                           jne 0x1408fa8d1
008FA859  41 8D 7F F3                     lea edi, [r15 - 0xd]
008FA85D  EB 88                           jmp 0x1408fa7e7
008FA85F  41 BF 08 00 00 00               mov r15d, 8
008FA865  BF 01 00 00 00                  mov edi, 1
008FA86A  E9 78 FF FF FF                  jmp 0x1408fa7e7
008FA86F  41 8D 45 10                     lea eax, [r13 + 0x10]
008FA873  B9 00 01 00 00                  mov ecx, 0x100
008FA878  8B D0                           mov edx, eax
008FA87A  41 B8 50 70 69 6F               mov r8d, 0x6f697050
008FA880  89 45 9F                        mov dword ptr [rbp - 0x61], eax
008FA883  E8 68 78 28 00                  call 0x140b820f0
008FA888  33 F6                           xor esi, esi
008FA88A  48 8B F8                        mov rdi, rax
008FA88D  48 85 C0                        test rax, rax
008FA890  0F 84 31 01 00 00               je 0x1408fa9c7
008FA896  44 8B 45 9F                     mov r8d, dword ptr [rbp - 0x61]
008FA89A  4D 8B CE                        mov r9, r14
008FA89D  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
008FA8A1  48 8B D0                        mov rdx, rax
008FA8A4  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
008FA8A9  E8 22 D6 FA FF                  call 0x1408a7ed0
008FA8AE  8B D8                           mov ebx, eax
008FA8B0  3D 04 00 00 C0                  cmp eax, 0xc0000004
008FA8B5  0F 85 62 02 00 00               jne 0x1408fab1d
008FA8BB  8D 58 1F                        lea ebx, [rax + 0x1f]
008FA8BE  41 83 06 F0                     add dword ptr [r14], -0x10
008FA8C2  33 D2                           xor edx, edx
008FA8C4  48 8B CF                        mov rcx, rdi
008FA8C7  E8 A4 7F 28 00                  call 0x140b82870
008FA8CC  E9 46 FF FF FF                  jmp 0x1408fa817
008FA8D1  83 EB 0C                        sub ebx, 0xc
008FA8D4  0F 84 F2 01 00 00               je 0x1408faacc
008FA8DA  83 EB 01                        sub ebx, 1
008FA8DD  0F 84 EE 00 00 00               je 0x1408fa9d1
008FA8E3  83 EB 01                        sub ebx, 1
008FA8E6  0F 85 8B 00 00 00               jne 0x1408fa977
008FA8EC  39 96 CC 01 00 00               cmp dword ptr [rsi + 0x1cc], edx
008FA8F2  0F 8C 1A FF FF FF               jl 0x1408fa812
008FA8F8  41 C7 06 04 00 00 00            mov dword ptr [r14], 4
008FA8FF  41 83 FD 04                     cmp r13d, 4
008FA903  0F 82 B9 01 00 00               jb 0x1408faac2
008FA909  8B 86 CC 01 00 00               mov eax, dword ptr [rsi + 0x1cc]
008FA90F  41 89 04 24                     mov dword ptr [r12], eax
008FA913  8B DA                           mov ebx, edx
008FA915  E9 FD FE FF FF                  jmp 0x1408fa817
008FA91A  BF 01 00 00 00                  mov edi, 1
008FA91F  44 8B FF                        mov r15d, edi
008FA922  E9 C0 FE FF FF                  jmp 0x1408fa7e7
008FA927  83 EB 06                        sub ebx, 6
008FA92A  0F 84 AB 02 00 00               je 0x1408fabdb
008FA930  83 EB 01                        sub ebx, 1
008FA933  0F 85 C9 01 00 00               jne 0x1408fab02
008FA939  44 8D 7B 0A                     lea r15d, [rbx + 0xa]
008FA93D  E9 23 FF FF FF                  jmp 0x1408fa865
008FA942  83 EB 12                        sub ebx, 0x12
008FA945  0F 84 AF 00 00 00               je 0x1408fa9fa
008FA94B  83 EB 01                        sub ebx, 1
008FA94E  0F 85 9D 02 00 00               jne 0x1408fabf1
008FA954  41 C7 06 04 00 00 00            mov dword ptr [r14], 4
008FA95B  41 83 FD 04                     cmp r13d, 4
008FA95F  0F 82 5D 01 00 00               jb 0x1408faac2
008FA965  4D 8B C4                        mov r8, r12
008FA968  8D 53 01                        lea edx, [rbx + 1]
008FA96B  48 8B CE                        mov rcx, rsi
008FA96E  E8 41 08 00 00                  call 0x1408fb1b4
008FA973  33 FF                           xor edi, edi
008FA975  EB 49                           jmp 0x1408fa9c0
008FA977  83 EB 01                        sub ebx, 1
008FA97A  0F 84 66 02 00 00               je 0x1408fabe6
008FA980  83 FB 01                        cmp ebx, 1
008FA983  0F 85 88 02 00 00               jne 0x1408fac11
008FA989  48 8D 55 CF                     lea rdx, [rbp - 0x31]
008FA98D  48 8B CF                        mov rcx, rdi
008FA990  E8 F7 05 00 00                  call 0x1408faf8c
008FA995  33 FF                           xor edi, edi
008FA997  85 C0                           test eax, eax
008FA999  0F 88 73 FE FF FF               js 0x1408fa812
008FA99F  8B 45 D7                        mov eax, dword ptr [rbp - 0x29]
008FA9A2  83 F8 FF                        cmp eax, -1
008FA9A5  0F 84 67 FE FF FF               je 0x1408fa812
008FA9AB  41 C7 06 04 00 00 00            mov dword ptr [r14], 4
008FA9B2  41 83 FD 04                     cmp r13d, 4
008FA9B6  0F 82 06 01 00 00               jb 0x1408faac2
008FA9BC  41 89 04 24                     mov dword ptr [r12], eax
008FA9C0  8B DF                           mov ebx, edi
008FA9C2  E9 50 FE FF FF                  jmp 0x1408fa817
008FA9C7  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008FA9CC  E9 46 FE FF FF                  jmp 0x1408fa817
008FA9D1  83 BE C8 01 00 00 FF            cmp dword ptr [rsi + 0x1c8], -1
008FA9D8  0F 84 34 FE FF FF               je 0x1408fa812
008FA9DE  41 C7 06 04 00 00 00            mov dword ptr [r14], 4
008FA9E5  41 83 FD 04                     cmp r13d, 4
008FA9E9  0F 82 D3 00 00 00               jb 0x1408faac2
008FA9EF  8B 86 C8 01 00 00               mov eax, dword ptr [rsi + 0x1c8]
008FA9F5  E9 15 FF FF FF                  jmp 0x1408fa90f
008FA9FA  48 3B 35 37 1A 69 00            cmp rsi, qword ptr [rip + 0x691a37]
008FAA01  0F 84 14 02 00 00               je 0x1408fac1b
008FAA07  48 39 56 30                     cmp qword ptr [rsi + 0x30], rdx
008FAA0B  0F 84 30 FE FF FF               je 0x1408fa841
008FAA11  BF 01 00 00 00                  mov edi, 1
008FAA16  44 8D 7F 02                     lea r15d, [rdi + 2]
008FAA1A  48 8B 0D 77 B9 56 00            mov rcx, qword ptr [rip + 0x56b977]
008FAA21  48 8D 45 9F                     lea rax, [rbp - 0x61]
008FAA25  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
008FAA29  41 B9 0B 00 00 00               mov r9d, 0xb
008FAA2F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008FAA34  45 33 C0                        xor r8d, r8d
008FAA37  48 8D 45 A7                     lea rax, [rbp - 0x59]
008FAA3B  C7 45 9F 04 00 00 00            mov dword ptr [rbp - 0x61], 4
008FAA42  48 8B 56 30                     mov rdx, qword ptr [rsi + 0x30]
008FAA46  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008FAA4B  48 8D 45 A3                     lea rax, [rbp - 0x5d]
008FAA4F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008FAA54  E8 17 2E FF FF                  call 0x1408ed870
008FAA59  33 D2                           xor edx, edx
008FAA5B  8B D8                           mov ebx, eax
008FAA5D  85 C0                           test eax, eax
008FAA5F  78 3E                           js 0x1408faa9f
008FAA61  83 7D A3 04                     cmp dword ptr [rbp - 0x5d], 4
008FAA65  75 38                           jne 0x1408faa9f
008FAA67  83 7D 9F 04                     cmp dword ptr [rbp - 0x61], 4
008FAA6B  75 32                           jne 0x1408faa9f
008FAA6D  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
008FAA70  A8 20                           test al, 0x20
008FAA72  75 27                           jne 0x1408faa9b
008FAA74  A8 40                           test al, 0x40
008FAA76  0F 85 A8 01 00 00               jne 0x1408fac24
008FAA7C  25 00 04 00 00                  and eax, 0x400
008FAA81  F7 D8                           neg eax
008FAA83  1B C0                           sbb eax, eax
008FAA85  41 23 C7                        and eax, r15d
008FAA88  48 8B 76 10                     mov rsi, qword ptr [rsi + 0x10]
008FAA8C  85 C0                           test eax, eax
008FAA8E  75 1C                           jne 0x1408faaac
008FAA90  48 3B 35 A1 19 69 00            cmp rsi, qword ptr [rip + 0x6919a1]
008FAA97  75 81                           jne 0x1408faa1a
008FAA99  EB 11                           jmp 0x1408faaac
008FAA9B  8B C7                           mov eax, edi
008FAA9D  EB E9                           jmp 0x1408faa88
008FAA9F  B8 02 00 00 00                  mov eax, 2
008FAAA4  85 DB                           test ebx, ebx
008FAAA6  0F 88 82 01 00 00               js 0x1408fac2e
008FAAAC  41 C7 06 04 00 00 00            mov dword ptr [r14], 4
008FAAB3  41 83 FD 04                     cmp r13d, 4
008FAAB7  72 09                           jb 0x1408faac2
008FAAB9  41 89 04 24                     mov dword ptr [r12], eax
008FAABD  E9 55 FD FF FF                  jmp 0x1408fa817
008FAAC2  BB 23 00 00 C0                  mov ebx, 0xc0000023
008FAAC7  E9 4B FD FF FF                  jmp 0x1408fa817
008FAACC  0F B7 8E D0 01 00 00            movzx ecx, word ptr [rsi + 0x1d0]
008FAAD3  48 8D 55 B7                     lea rdx, [rbp - 0x49]
008FAAD7  E8 44 1C 00 00                  call 0x1408fc720
008FAADC  8B D8                           mov ebx, eax
008FAADE  85 C0                           test eax, eax
008FAAE0  0F 88 31 FD FF FF               js 0x1408fa817
008FAAE6  41 C7 06 10 00 00 00            mov dword ptr [r14], 0x10
008FAAED  41 83 FD 10                     cmp r13d, 0x10
008FAAF1  72 CF                           jb 0x1408faac2
008FAAF3  0F 10 45 B7                     movups xmm0, xmmword ptr [rbp - 0x49]
008FAAF7  F3 41 0F 7F 04 24               movdqu xmmword ptr [r12], xmm0
008FAAFD  E9 15 FD FF FF                  jmp 0x1408fa817
008FAB02  83 EB 01                        sub ebx, 1
008FAB05  0F 84 C5 00 00 00               je 0x1408fabd0
008FAB0B  83 EB 01                        sub ebx, 1
008FAB0E  0F 85 AE 00 00 00               jne 0x1408fabc2
008FAB14  44 8D 7B 0D                     lea r15d, [rbx + 0xd]
008FAB18  E9 48 FD FF FF                  jmp 0x1408fa865
008FAB1D  85 C0                           test eax, eax
008FAB1F  0F 88 99 FD FF FF               js 0x1408fa8be
008FAB25  0F B7 07                        movzx eax, word ptr [rdi]
008FAB28  66 85 C0                        test ax, ax
008FAB2B  74 28                           je 0x1408fab55
008FAB2D  83 C0 02                        add eax, 2
008FAB30  41 89 06                        mov dword ptr [r14], eax
008FAB33  41 3B C5                        cmp eax, r13d
008FAB36  77 25                           ja 0x1408fab5d
008FAB38  44 0F B7 07                     movzx r8d, word ptr [rdi]
008FAB3C  49 8B CC                        mov rcx, r12
008FAB3F  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
008FAB43  E8 F8 BC DC FF                  call 0x1406c6840
008FAB48  0F B7 07                        movzx eax, word ptr [rdi]
008FAB4B  66 42 89 34 20                  mov word ptr [rax + r12], si
008FAB50  E9 6D FD FF FF                  jmp 0x1408fa8c2
008FAB55  41 89 36                        mov dword ptr [r14], esi
008FAB58  E9 65 FD FF FF                  jmp 0x1408fa8c2
008FAB5D  BB 23 00 00 C0                  mov ebx, 0xc0000023
008FAB62  E9 5B FD FF FF                  jmp 0x1408fa8c2
008FAB67  83 EB 01                        sub ebx, 1
008FAB6A  75 0C                           jne 0x1408fab78
008FAB6C  8D 7B 07                        lea edi, [rbx + 7]
008FAB6F  44 8D 7B 03                     lea r15d, [rbx + 3]
008FAB73  E9 6F FC FF FF                  jmp 0x1408fa7e7
008FAB78  83 EB 01                        sub ebx, 1
008FAB7B  0F 84 B9 48 22 00               je 0x140b1f43a
008FAB81  83 FB 01                        cmp ebx, 1
008FAB84  0F 85 87 00 00 00               jne 0x1408fac11
008FAB8A  48 8B 8E 28 02 00 00            mov rcx, qword ptr [rsi + 0x228]
008FAB91  48 85 C9                        test rcx, rcx
008FAB94  0F 84 79 FD FF FF               je 0x1408fa913
008FAB9A  E8 59 1B 00 00                  call 0x1408fc6f8
008FAB9F  41 89 06                        mov dword ptr [r14], eax
008FABA2  41 3B C5                        cmp eax, r13d
008FABA5  0F 87 17 FF FF FF               ja 0x1408faac2
008FABAB  48 8B 96 28 02 00 00            mov rdx, qword ptr [rsi + 0x228]
008FABB2  49 8B CC                        mov rcx, r12
008FABB5  44 8B C0                        mov r8d, eax
008FABB8  E8 83 BC DC FF                  call 0x1406c6840
008FABBD  E9 B1 FD FF FF                  jmp 0x1408fa973
008FABC2  83 FB 01                        cmp ebx, 1
008FABC5  75 4A                           jne 0x1408fac11
008FABC7  44 8D 7B 0D                     lea r15d, [rbx + 0xd]
008FABCB  E9 95 FC FF FF                  jmp 0x1408fa865
008FABD0  41 BF 0C 00 00 00               mov r15d, 0xc
008FABD6  E9 8A FC FF FF                  jmp 0x1408fa865
008FABDB  41 BF 09 00 00 00               mov r15d, 9
008FABE1  E9 7F FC FF FF                  jmp 0x1408fa865
008FABE6  41 BF 17 00 00 00               mov r15d, 0x17
008FABEC  E9 74 FC FF FF                  jmp 0x1408fa865
008FABF1  83 EB 01                        sub ebx, 1
008FABF4  0F 84 D0 48 22 00               je 0x140b1f4ca
008FABFA  83 EB 01                        sub ebx, 1
008FABFD  0F 84 53 48 22 00               je 0x140b1f456
008FAC03  83 FB 01                        cmp ebx, 1
008FAC06  75 09                           jne 0x1408fac11
008FAC08  44 8D 7B 24                     lea r15d, [rbx + 0x24]
008FAC0C  E9 54 FC FF FF                  jmp 0x1408fa865
008FAC11  BB F0 00 00 C0                  mov ebx, 0xc00000f0
008FAC16  E9 FC FB FF FF                  jmp 0x1408fa817
008FAC1B  8B C2                           mov eax, edx
008FAC1D  8B DA                           mov ebx, edx
008FAC1F  E9 88 FE FF FF                  jmp 0x1408faaac
008FAC24  B8 02 00 00 00                  mov eax, 2
008FAC29  E9 5A FE FF FF                  jmp 0x1408faa88
008FAC2E  81 FB 25 02 00 C0               cmp ebx, 0xc0000225
008FAC34  0F 84 D8 FB FF FF               je 0x1408fa812
008FAC3A  81 FB 0E 00 00 C0               cmp ebx, 0xc000000e
008FAC40  E9 CB FB FF FF                  jmp 0x1408fa810
008FAC45  83 FB 12                        cmp ebx, 0x12
008FAC48  0F 84 F3 FB FF FF               je 0x1408fa841
008FAC4E  83 FB 0F                        cmp ebx, 0xf
008FAC51  0F 85 C2 48 22 00               jne 0x140b1f519
008FAC57  48 85 F6                        test rsi, rsi
008FAC5A  0F 85 E1 FB FF FF               jne 0x1408fa841
008FAC60  E9 B4 48 22 00                  jmp 0x140b1f519
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoGetDeviceProperty(__int64 a1, int a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m57;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 5308413)) ^ (v_rsp);
    v_stack_m48 = result;
    a2 = 0;
    v_stack_mA8 = a1;
    v_stack_mA0 = v_xmm0;
    result = memset(v_stack_m88, a2, a2 + 64, a4);
    a2 = 0;
    v_rbx = (unsigned int)(((unsigned int)(a2)) & (0xFFFULL));
    v_stack_mB0 = 0;
    v_stack_mB4 = 0;
    *(unsigned int *)(a5) = 0;
    if (a1 == 0) goto loc_008FA841;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312) + 40) == 0) goto loc_008FAC45;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312) + 40) + 396)) & (0x20000ULL)) != 0) goto loc_008FAC45;
    if (((unsigned int)(v_rbx)) > 11) goto loc_008FA848;
    if (((unsigned int)(v_rbx)) == 11) goto loc_008FA86F;
    if (((unsigned int)(v_rbx)) == 5) goto loc_008FA85F;
    if (((unsigned int)(v_rbx)) > 5) goto loc_008FA927;
    if ((unsigned int)(v_rbx) == 0) goto loc_008FA91A;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_008FAB67;
loc_008FA7E7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312) + 40) + 48)) == 0) goto loc_008FA841;
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(a3));
    v_stack_mD0 = a5;
    v_stack_mD8 = a4;
    result = PiGetDeviceRegProperty(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 312) + 40) + 48), a2, (unsigned int)((unsigned int)(a2 + 7)), (unsigned int)((unsigned int)(a2 + 2)));
loc_008FA810:
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) == 0xC0000225ULL) {
        v_rbx = 0xC0000034ULL;
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)(a2 + 7)), (unsigned int)((unsigned int)(a2 + 2)));
    v_rsp = (v_rsp) + (192);
    return result;
loc_008FA841:
    goto loc_008FA817;
loc_008FA848:
    if (((unsigned int)((unsigned int)(0xC0000010ULL))) > 17) goto loc_008FA942;
    if (((unsigned int)((unsigned int)(0xC0000010ULL))) != 17) goto loc_008FA8D1;
    goto loc_008FA7E7;
loc_008FA85F:
loc_008FA865:
    goto loc_008FA7E7;
loc_008FA86F:
    v_stack_mB8 = (unsigned int)((unsigned int)(a3) + 16);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(a3) + 16)), (unsigned int)(0x6F697050ULL), (unsigned int)((unsigned int)(a2 + 2)));
    v_rsi = 0;
    if (result == 0) goto loc_008FA9C7;
    v_stack_p20 = 0;
    result = ObQueryNameStringMode(v_stack_mA8, result, (unsigned int)(v_stack_mB8), a5);
    if (((unsigned int)(result)) != 0xC0000004ULL) goto loc_008FAB1D;
loc_008FA8BE:
loc_008FA8C2:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(v_stack_mB8), a5);
    goto loc_008FA817;
loc_008FA8D1:
    v_rbx = (unsigned int)((result + 31) - (12));
    if (condition_is_equal) goto loc_008FAACC;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_008FA9D1;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_008FA977;
    if ((*(unsigned int *)(v_rsi + 460)) < 0) goto loc_008FA812;
    *(unsigned int *)(a5) = 4;
    if (((unsigned int)((unsigned int)(a3))) < 4) goto loc_008FAAC2;
loc_008FA90F:
    *(unsigned int *)(a4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 460)));
loc_008FA913:
    goto loc_008FA817;
loc_008FA91A:
    goto loc_008FA7E7;
loc_008FA927:
    v_rbx = (unsigned int)((0) - (6));
    if (condition_is_equal) goto loc_008FABDB;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_008FAB02;
    goto loc_008FA865;
loc_008FA942:
    v_rbx = (unsigned int)((v_rbx) - (18));
    if (condition_is_equal) goto loc_008FA9FA;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_008FABF1;
    *(unsigned int *)(a5) = 4;
    if (((unsigned int)((unsigned int)(a3))) < 4) goto loc_008FAAC2;
    result = PpHotSwapGetDevnodeRemovalPolicy(0, v_rbx + 1, a4, a5);
loc_008FA973:
    v_rdi = 0;
    goto loc_008FA9C0;
loc_008FA977:
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_008FABE6;
    if (((unsigned int)(v_rbx)) != 1) goto loc_008FAC11;
    result = PpIrpQueryCapabilities(0, v_stack_m88, a4, a5);
    v_rdi = 0;
    if (sign_flag) goto loc_008FA812;
    if (((unsigned int)((unsigned int)(v_stack_m80))) == -1) goto loc_008FA812;
    *(unsigned int *)(a5) = 4;
    if (((unsigned int)((unsigned int)(a3))) < 4) goto loc_008FAAC2;
    *(unsigned int *)(a4) = (unsigned int)((unsigned int)(v_stack_m80));
loc_008FA9C0:
    goto loc_008FA817;
loc_008FA9C7:
    goto loc_008FA817;
loc_008FA9D1:
    if ((*(unsigned int *)(v_rsi + 456)) == -1) goto loc_008FA812;
    *(unsigned int *)(a5) = 4;
    if (((unsigned int)((unsigned int)(a3))) < 4) goto loc_008FAAC2;
    goto loc_008FA90F;
loc_008FA9FA:
    if (0 == (*(unsigned __int64 *)(v_rip + 6887991))) goto loc_008FAC1B;
    if ((*(unsigned __int64 *)(v_rsi + 48)) == v_stack_m88) goto loc_008FA841;
loc_008FAA1A:
    v_stack_p38 = (unsigned int)(v_stack_m88);
    v_stack_p30 = v_stack_mB8;
    a3 = 0;
    v_stack_mB8 = 4;
    v_stack_p28 = v_stack_mB0;
    v_stack_p20 = v_stack_mB4;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 5683575), *(unsigned __int64 *)(v_rsi + 48), a3, 11);
    a2 = 0;
    if (sign_flag) goto loc_008FAA9F;
    if (v_stack_mB4 != 4) goto loc_008FAA9F;
    if (v_stack_mB8 != 4) goto loc_008FAA9F;
    if ((((unsigned __int8)((unsigned int)(v_stack_mB0))) & (32)) != 0) goto loc_008FAA9B;
    if ((((unsigned __int8)((unsigned int)(v_stack_mB0))) & (64)) != 0) goto loc_008FAC24;
    result = (unsigned int)(((unsigned int)(v_stack_mB0)) & (0x400ULL));
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) & ((unsigned int)(1 + 2)));
loc_008FAA88:
    if ((unsigned int)(result) != 0) goto loc_008FAAAC;
    if ((*(unsigned __int64 *)(v_rsi + 16)) != (*(unsigned __int64 *)(v_rip + 6887841))) goto loc_008FAA1A;
    goto loc_008FAAAC;
loc_008FAA9B:
    goto loc_008FAA88;
loc_008FAA9F:
    if (sign_flag) goto loc_008FAC2E;
loc_008FAAAC:
    *(unsigned int *)(a5) = 4;
    if (((unsigned int)((unsigned int)(a3))) < 4) goto loc_008FAAC2;
    *(unsigned int *)(a4) = 2;
    goto loc_008FA817;
loc_008FAAC2:
    goto loc_008FA817;
loc_008FAACC:
    result = PnpBusTypeGuidGet(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsi + 16) + 464), v_stack_mA0, a3, 11);
    if (sign_flag) goto loc_008FA817;
    *(unsigned int *)(a5) = 16;
    if (((unsigned int)((unsigned int)(a3))) < 16) goto loc_008FAAC2;
    *(unsigned __int64 *)(a4) = v_xmm0;
    goto loc_008FA817;
loc_008FAB02:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) - (1));
    if (condition_is_equal) goto loc_008FABD0;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_not_equal) goto loc_008FABC2;
    goto loc_008FA865;
loc_008FAB1D:
    if (sign_flag) goto loc_008FA8BE;
    if ((unsigned __int16)(*(unsigned __int16 *)(1)) == 0) goto loc_008FAB55;
    result = (unsigned int)((*(unsigned __int16 *)(1)) + (2));
    *(unsigned int *)(a5) = (unsigned int)(result);
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(a3)))) goto loc_008FAB5D;
    result = memcpy(a4, *(unsigned __int64 *)(1 + 8), *(unsigned __int16 *)(1), 11);
    *(unsigned __int16 *)(*(unsigned __int16 *)(1) + a4 * 1) = (unsigned __int16)(*(unsigned __int64 *)(v_rsi + 16));
    goto loc_008FA8C2;
loc_008FAB55:
    *(unsigned int *)(a5) = (unsigned int)(*(unsigned __int64 *)(v_rsi + 16));
    goto loc_008FA8C2;
loc_008FAB5D:
    goto loc_008FA8C2;
loc_008FAB67:
    v_rbx = (unsigned int)(((unsigned int)(0xC0000023ULL)) - (1));
    if (condition_is_not_equal) goto loc_008FAB78;
    goto loc_008FA7E7;
loc_008FAB78:
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (((unsigned int)(v_rbx)) != 1) goto loc_008FAC11;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 16) + 552) == 0) goto loc_008FA913;
    result = PnpDetermineResourceListSize(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 16) + 552), *(unsigned __int64 *)(1 + 8), *(unsigned __int16 *)(1), 11);
    *(unsigned int *)(a5) = (unsigned int)(result);
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(a3)))) goto loc_008FAAC2;
    result = memcpy(a4, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 16) + 552), (unsigned int)((unsigned int)(result)), 11);
    goto loc_008FA973;
loc_008FABC2:
    if (((unsigned int)(v_rbx)) != 1) goto loc_008FAC11;
    goto loc_008FA865;
loc_008FABD0:
    goto loc_008FA865;
loc_008FABDB:
    goto loc_008FA865;
loc_008FABE6:
    goto loc_008FA865;
loc_008FABF1:
    v_rbx = (unsigned int)((v_rbx) - (1));
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (((unsigned int)(v_rbx)) != 1) goto loc_008FAC11;
    goto loc_008FA865;
loc_008FAC11:
    goto loc_008FA817;
loc_008FAC1B:
    goto loc_008FAAAC;
loc_008FAC24:
    goto loc_008FAA88;
loc_008FAC2E:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 16) + 552))))) == 0xC0000225ULL) goto loc_008FA812;
    goto loc_008FA810;
loc_008FAC45:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi + 16) + 552))))) == 18) goto loc_008FA841;
    if (*(unsigned __int64 *)(v_rsi + 16) != 0) goto loc_008FA841;
}
```

## 5. (Beta) C Style

```c
int64_t IoGetDeviceProperty(int64_t Arg1, int32_t Arg2, void *Arg3, void *Arg4, void *Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m57;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p10;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x50FFFD)) ^ (local_rsp);
    v_stack_m48 = result;
    Arg2 = 0;
    v_stack_mA8 = Arg1;
    v_stack_mA0 = v_xmm0;
    result = memset(v_stack_m88, Arg2, Arg2 + 64, Arg4);
    Arg2 = 0;
    local_rbx = (uint32_t)(((uint32_t)(Arg2)) & (0xFFFULL));
    v_stack_mB0 = 0;
    v_stack_mB4 = 0;
    *(uint32_t *)(arg5) = 0;
    if (Arg1 == 0) goto loc_008FA841;
    if (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x138) + 0x28) == 0) goto loc_008FAC45;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x138) + 0x28) + 0x18C)) & (0x20000ULL)) != 0) goto loc_008FAC45;
    if (((uint32_t)(local_rbx)) > 11) goto loc_008FA848;
    if (((uint32_t)(local_rbx)) == 11) goto loc_008FA86F;
    if (((uint32_t)(local_rbx)) == 5) goto loc_008FA85F;
    if (((uint32_t)(local_rbx)) > 5) goto loc_008FA927;
    if ((uint32_t)(local_rbx) == 0) goto loc_008FA91A;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_008FAB67;
loc_008FA7E7:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x138) + 0x28) + 0x30)) == 0) goto loc_008FA841;
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(Arg3));
    v_stack_mD0 = Arg5;
    v_stack_mD8 = Arg4;
    result = PiGetDeviceRegProperty(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x138) + 0x28) + 0x30), Arg2, (uint32_t)((uint32_t)(Arg2 + 7)), (uint32_t)((uint32_t)(Arg2 + 2)));
loc_008FA810:
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) == 0xC0000225ULL) {
        local_rbx = 0xC0000034ULL;
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)(Arg2 + 7)), (uint32_t)((uint32_t)(Arg2 + 2)));
    local_rsp = (local_rsp) + (192);
    return result;
loc_008FA841:
    goto loc_008FA817;
loc_008FA848:
    if (((uint32_t)((uint32_t)(0xC0000010ULL))) > 17) goto loc_008FA942;
    if (((uint32_t)((uint32_t)(0xC0000010ULL))) != 17) goto loc_008FA8D1;
    goto loc_008FA7E7;
loc_008FA85F:
loc_008FA865:
    goto loc_008FA7E7;
loc_008FA86F:
    v_stack_mB8 = (uint32_t)((uint32_t)(Arg3) + 16);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(Arg3) + 16)), (uint32_t)(0x6F697050ULL), (uint32_t)((uint32_t)(Arg2 + 2)));
    local_rsi = 0;
    if (result == 0) goto loc_008FA9C7;
    v_stack_p20 = 0;
    result = ObQueryNameStringMode(v_stack_mA8, result, (uint32_t)(v_stack_mB8), Arg5);
    if (((uint32_t)(result)) != 0xC0000004ULL) goto loc_008FAB1D;
loc_008FA8BE:
loc_008FA8C2:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(v_stack_mB8), Arg5);
    goto loc_008FA817;
loc_008FA8D1:
    local_rbx = (uint32_t)((result + 31) - (12));
    if (condition_is_equal) goto loc_008FAACC;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_008FA9D1;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_008FA977;
    if ((*(uint32_t *)(local_rsi + 0x1CC)) < 0) goto loc_008FA812;
    *(uint32_t *)(arg5) = 4;
    if (((uint32_t)((uint32_t)(Arg3))) < 4) goto loc_008FAAC2;
loc_008FA90F:
    *(uint32_t *)(arg4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x1CC)));
loc_008FA913:
    goto loc_008FA817;
loc_008FA91A:
    goto loc_008FA7E7;
loc_008FA927:
    local_rbx = (uint32_t)((0) - (6));
    if (condition_is_equal) goto loc_008FABDB;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_008FAB02;
    goto loc_008FA865;
loc_008FA942:
    local_rbx = (uint32_t)((local_rbx) - (18));
    if (condition_is_equal) goto loc_008FA9FA;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_008FABF1;
    *(uint32_t *)(arg5) = 4;
    if (((uint32_t)((uint32_t)(Arg3))) < 4) goto loc_008FAAC2;
    result = PpHotSwapGetDevnodeRemovalPolicy(0, local_rbx + 1, Arg4, Arg5);
loc_008FA973:
    local_rdi = 0;
    goto loc_008FA9C0;
loc_008FA977:
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_008FABE6;
    if (((uint32_t)(local_rbx)) != 1) goto loc_008FAC11;
    result = PpIrpQueryCapabilities(0, v_stack_m88, Arg4, Arg5);
    local_rdi = 0;
    if (sign_flag) goto loc_008FA812;
    if (((uint32_t)((uint32_t)(v_stack_m80))) == -1) goto loc_008FA812;
    *(uint32_t *)(arg5) = 4;
    if (((uint32_t)((uint32_t)(Arg3))) < 4) goto loc_008FAAC2;
    *(uint32_t *)(arg4) = (uint32_t)((uint32_t)(v_stack_m80));
loc_008FA9C0:
    goto loc_008FA817;
loc_008FA9C7:
    goto loc_008FA817;
loc_008FA9D1:
    if ((*(uint32_t *)(local_rsi + 0x1C8)) == -1) goto loc_008FA812;
    *(uint32_t *)(arg5) = 4;
    if (((uint32_t)((uint32_t)(Arg3))) < 4) goto loc_008FAAC2;
    goto loc_008FA90F;
loc_008FA9FA:
    if (0 == (*(uint64_t *)(v_rip + 0x691A37))) goto loc_008FAC1B;
    if ((*(uint64_t *)(local_rsi + 0x30)) == v_stack_m88) goto loc_008FA841;
loc_008FAA1A:
    v_stack_p38 = (uint32_t)(v_stack_m88);
    v_stack_p30 = v_stack_mB8;
    Arg3 = 0;
    v_stack_mB8 = 4;
    v_stack_p28 = v_stack_mB0;
    v_stack_p20 = v_stack_mB4;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x56B977), *(uint64_t *)(local_rsi + 0x30), Arg3, 11);
    Arg2 = 0;
    if (sign_flag) goto loc_008FAA9F;
    if (v_stack_mB4 != 4) goto loc_008FAA9F;
    if (v_stack_mB8 != 4) goto loc_008FAA9F;
    if ((((uint8_t)((uint32_t)(v_stack_mB0))) & (32)) != 0) goto loc_008FAA9B;
    if ((((uint8_t)((uint32_t)(v_stack_mB0))) & (64)) != 0) goto loc_008FAC24;
    result = (uint32_t)(((uint32_t)(v_stack_mB0)) & (0x400ULL));
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) & ((uint32_t)(1 + 2)));
loc_008FAA88:
    if ((uint32_t)(result) != 0) goto loc_008FAAAC;
    if ((*(uint64_t *)(local_rsi + 0x10)) != (*(uint64_t *)(v_rip + 0x6919A1))) goto loc_008FAA1A;
    goto loc_008FAAAC;
loc_008FAA9B:
    goto loc_008FAA88;
loc_008FAA9F:
    if (sign_flag) goto loc_008FAC2E;
loc_008FAAAC:
    *(uint32_t *)(arg5) = 4;
    if (((uint32_t)((uint32_t)(Arg3))) < 4) goto loc_008FAAC2;
    *(uint32_t *)(arg4) = 2;
    goto loc_008FA817;
loc_008FAAC2:
    goto loc_008FA817;
loc_008FAACC:
    result = PnpBusTypeGuidGet(*(uint16_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x1D0), v_stack_mA0, Arg3, 11);
    if (sign_flag) goto loc_008FA817;
    *(uint32_t *)(arg5) = 16;
    if (((uint32_t)((uint32_t)(Arg3))) < 16) goto loc_008FAAC2;
    *(uint64_t *)(arg4) = v_xmm0;
    goto loc_008FA817;
loc_008FAB02:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) - (1));
    if (condition_is_equal) goto loc_008FABD0;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_not_equal) goto loc_008FABC2;
    goto loc_008FA865;
loc_008FAB1D:
    if (sign_flag) goto loc_008FA8BE;
    if ((uint16_t)(*(uint16_t *)(1)) == 0) goto loc_008FAB55;
    result = (uint32_t)((*(uint16_t *)(1)) + (2));
    *(uint32_t *)(arg5) = (uint32_t)(result);
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(Arg3)))) goto loc_008FAB5D;
    result = memcpy(Arg4, *(uint64_t *)(1 + 0x8), *(uint16_t *)(1), 11);
    *(uint16_t *)(*(uint16_t *)(1) + arg4 * 1) = (uint16_t)(*(uint64_t *)(local_rsi + 0x10));
    goto loc_008FA8C2;
loc_008FAB55:
    *(uint32_t *)(arg5) = (uint32_t)(*(uint64_t *)(local_rsi + 0x10));
    goto loc_008FA8C2;
loc_008FAB5D:
    goto loc_008FA8C2;
loc_008FAB67:
    local_rbx = (uint32_t)(((uint32_t)(0xC0000023ULL)) - (1));
    if (condition_is_not_equal) goto loc_008FAB78;
    goto loc_008FA7E7;
loc_008FAB78:
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (((uint32_t)(local_rbx)) != 1) goto loc_008FAC11;
    if (*(uint64_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x228) == 0) goto loc_008FA913;
    result = PnpDetermineResourceListSize(*(uint64_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x228), *(uint64_t *)(1 + 0x8), *(uint16_t *)(1), 11);
    *(uint32_t *)(arg5) = (uint32_t)(result);
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(Arg3)))) goto loc_008FAAC2;
    result = memcpy(Arg4, *(uint64_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x228), (uint32_t)((uint32_t)(result)), 11);
    goto loc_008FA973;
loc_008FABC2:
    if (((uint32_t)(local_rbx)) != 1) goto loc_008FAC11;
    goto loc_008FA865;
loc_008FABD0:
    goto loc_008FA865;
loc_008FABDB:
    goto loc_008FA865;
loc_008FABE6:
    goto loc_008FA865;
loc_008FABF1:
    local_rbx = (uint32_t)((local_rbx) - (1));
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (((uint32_t)(local_rbx)) != 1) goto loc_008FAC11;
    goto loc_008FA865;
loc_008FAC11:
    goto loc_008FA817;
loc_008FAC1B:
    goto loc_008FAAAC;
loc_008FAC24:
    goto loc_008FAA88;
loc_008FAC2E:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x228))))) == 0xC0000225ULL) goto loc_008FA812;
    goto loc_008FA810;
loc_008FAC45:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsi + 0x10) + 0x228))))) == 18) goto loc_008FA841;
    if (*(uint64_t *)(local_rsi + 0x10) != 0) goto loc_008FA841;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x10` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `W` |
| `Arg4` | `+ 0x0` | `128` | `W` |
| `Arg5` | `+ 0x0` | `32` | `R/W` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008FA720&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
