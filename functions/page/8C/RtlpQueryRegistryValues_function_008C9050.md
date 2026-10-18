# RtlpQueryRegistryValues

- RVA: `0x008C9050`–`0x008C9556` (길이 `1,286` bytes)
- VA: `0x00000001408C9050`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00084134`
- 디코드: `340`개 명령, `1,286/1,286` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **36**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008C90AF` → [RtlpGetRegistryHandle](RtlpGetRegistryHandle_function_008C955C.md) (function, `0x008C955C`)
- `0x008C90D3` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x008C90E6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008C9104` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008C9177` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x008C91AA` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x008C91EB` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008C920D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008C9238` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008C924C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008C9280` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x008C92B8` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x008C930D` → [ZwEnumerateValueKey](../../text/6A/ZwEnumerateValueKey_function_006AD330.md) (function, `0x006AD330`)
- `0x008C9329` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008C933D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008C937B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008C93BA` → [RtlpCallQueryRegistryRoutine](../8B/RtlpCallQueryRegistryRoutine_function_008BE844.md) (function, `0x008BE844`)
- `0x008C93FA` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x008C9410` → [DbgPrint](../../text/35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x008C944F` → [RtlpCallQueryRegistryRoutine](../8B/RtlpCallQueryRegistryRoutine_function_008BE844.md) (function, `0x008BE844`)
- `0x008C9480` → [ZwDeleteValueKey](../../text/6A/ZwDeleteValueKey_function_006AECB0.md) (function, `0x006AECB0`)
- `0x008C94B5` → [RtlpCallQueryRegistryRoutine](../8B/RtlpCallQueryRegistryRoutine_function_008BE844.md) (function, `0x008BE844`)
- `0x008C94E7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008C9513` → [ZwDeleteValueKey](../../text/6A/ZwDeleteValueKey_function_006AECB0.md) (function, `0x006AECB0`)
- `0x008C9549` → [DbgPrint](../../text/35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)

### Direct callers
- [FsRtlOpenFileSystemRegistryKeyFromFsGuid](../71/FsRtlOpenFileSystemRegistryKeyFromFsGuid_function_00715980.md) at `0x00715B04`
- [IopQueryPassiveInterruptRegistryOptions](../72/IopQueryPassiveInterruptRegistryOptions_function_0072BBB4.md) at `0x0072BCA0`
- [PiDevCfgQueryDriverNode](../73/PiDevCfgQueryDriverNode_function_0073435C.md) at `0x00734A77`
- [PiDevCfgQueryDriverNode](../73/PiDevCfgQueryDriverNode_function_0073435C.md) at `0x00734B6D`
- [PiDrvDbQuerySystemPathWin32](../74/PiDrvDbQuerySystemPathWin32_function_007421F4.md) at `0x0074252B`
- [PspSiloGetMultiUserTsFromRegistry](../78/PspSiloGetMultiUserTsFromRegistry_function_00780428.md) at `0x0078048E`
- [PspSiloGetSuiteMaskStringFromRegistry](../78/PspSiloGetSuiteMaskStringFromRegistry_function_007804C4.md) at `0x00780526`
- [PspQueryForwardersEnabled](../78/PspQueryForwardersEnabled_function_00781A0C.md) at `0x00781A6A`
- [RtlSetActiveTimeBias](../78/RtlSetActiveTimeBias_function_0078FA2C.md) at `0x0078FAA0`
- [RtlpUpdateDynamicTimeZones](../79/RtlpUpdateDynamicTimeZones_function_0079019C.md) at `0x0079037D`
- [SmKmRegParamsLoad](../7A/SmKmRegParamsLoad_function_007A8C64.md) at `0x007A8D23`
- [SmHwAcceleratorMgrAcquireAccelerators](../7A/SmHwAcceleratorMgrAcquireAccelerators_function_007AA628.md) at `0x007AA79B`
- [PerfDiagpUpdatePerfDiagLoggerEnableFlags](../7A/PerfDiagpUpdatePerfDiagLoggerEnableFlags_function_007AF21C.md) at `0x007AF29D`
- [EtwpGetPmcCpuHierarchyRegistry](../7B/EtwpGetPmcCpuHierarchyRegistry_function_007B687C.md) at `0x007B6979`
- [EtwpLoadMicroarchitecturalProfileGroup](../7B/EtwpLoadMicroarchitecturalProfileGroup_function_007B6F74.md) at `0x007B70EB`
- [EtwpLoadMicroarchitecturalProfileSource](../7B/EtwpLoadMicroarchitecturalProfileSource_function_007B7288.md) at `0x007B7524`
- [EtwStartAutoLogger](../7B/EtwStartAutoLogger_function_007BD2F8.md) at `0x007BD55C`
- [EtwStartAutoLogger](../7B/EtwStartAutoLogger_function_007BD2F8.md) at `0x007BD695`
- [EtwStartAutoLogger](../7B/EtwStartAutoLogger_function_007BD2F8.md) at `0x007BDBFF`
- [EtwStartAutoLogger](../7B/EtwStartAutoLogger_function_007BD2F8.md) at `0x007BDDAB`
- [ExpReadTimeZoneInformation](../7C/ExpReadTimeZoneInformation_function_007C61D8.md) at `0x007C6246`
- [ExIsStateSeparationEnabled](../7C/ExIsStateSeparationEnabled_function_007C75E0.md) at `0x007C7645`
- [ExpGetNumberOfInitialSessionsFromRegistry](../7C/ExpGetNumberOfInitialSessionsFromRegistry_function_007C7678.md) at `0x007C76DA`
- [VRegSetup](../83/VRegSetup_function_0083AE90.md) at `0x0083AEED`
- [WmipGetGuidSecurityDescriptor](WmipGetGuidSecurityDescriptor_function_008C7B4C.md) at `0x008C7BFA`
- [RtlQueryRegistryValues](RtlQueryRegistryValues_function_008C8FD0.md) at `0x008C8FD9`
- [RtlQueryRegistryValuesEx](RtlQueryRegistryValuesEx_function_008C8FF0.md) at `0x008C8FF9`
- [PiDevCfgClearDeviceMigrationNode](../96/PiDevCfgClearDeviceMigrationNode_function_00965780.md) at `0x009658C7`
- [PiDevCfgQueryDriverConfiguration](../97/PiDevCfgQueryDriverConfiguration_function_0097584C.md) at `0x00975A9B`
- [PiDevCfgConfigureDevice](../97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00978308`
- [PiDevCfgQueryDeviceMigrationNode](../9B/PiDevCfgQueryDeviceMigrationNode_function_009BD328.md) at `0x009BD5BC`
- [ExpPcwDisabledStatus](../A6/ExpPcwDisabledStatus_function_00A611E0.md) at `0x00A61264`
- [RtlpQueryTimeZoneInformationWorker](../A6/RtlpQueryTimeZoneInformationWorker_function_00A6BB6C.md) at `0x00A6BD2D`
- [EtwpEnableAutoLoggerProvider](../A9/EtwpEnableAutoLoggerProvider_function_00A92B00.md) at `0x00A92EC8`
- [EtwpEnableAutoLoggerProvider](../A9/EtwpEnableAutoLoggerProvider_function_00A92B00.md) at `0x00A92F70`
- [EtwpGetAutoLoggerProviderFilter](../A9/EtwpGetAutoLoggerProviderFilter_function_00A93248.md) at `0x00A9389E`
- [EtwpGetAutoLoggerProviderFilter](../A9/EtwpGetAutoLoggerProviderFilter_function_00A93248.md) at `0x00A939A1`
- [EtwpGetAutoLoggerLevelKwFilter](../A9/EtwpGetAutoLoggerLevelKwFilter_function_00A93AA8.md) at `0x00A93D94`
- [EtwpGetAutoLoggerLevelKwFilter](../A9/EtwpGetAutoLoggerLevelKwFilter_function_00A93AA8.md) at `0x00A93DE6`
- [EtwpGetAutoLoggerEventNameFilter](../A9/EtwpGetAutoLoggerEventNameFilter_function_00A93E78.md) at `0x00A94233`
- [EtwpGetAutoLoggerEventNameFilter](../A9/EtwpGetAutoLoggerEventNameFilter_function_00A93E78.md) at `0x00A942B3`
- [PiCreateDriverSwDeviceCallback](../AB/PiCreateDriverSwDeviceCallback_function_00ABB420.md) at `0x00ABB63D`
- [sub_00B1B086](../B1/Unknown_function_00B1B086.md) at `0x00B1B0B3`
- [sub_00B3C216](../B3/Unknown_function_00B3C216.md) at `0x00B3C2E0`

### Static image references
- `0x008C9409` → RVA `0x00B059B0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x008C90D3` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x008C90E6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008C9104` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008C9177` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x008C91AA` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x008C91EB` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008C920D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008C9238` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008C924C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008C9280` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x008C92B8` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x008C930D` → [ZwEnumerateValueKey](../../text/6A/ZwEnumerateValueKey_function_006AD330.md) (`PAGE` → `.text`)
  - `0x008C9329` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008C933D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008C937B` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008C93FA` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x008C9410` → [DbgPrint](../../text/35/DbgPrint_function_00358CB0.md) (`PAGE` → `.text`)
  - `0x008C9480` → [ZwDeleteValueKey](../../text/6A/ZwDeleteValueKey_function_006AECB0.md) (`PAGE` → `.text`)
  - `0x008C94E7` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008C9513` → [ZwDeleteValueKey](../../text/6A/ZwDeleteValueKey_function_006AECB0.md) (`PAGE` → `.text`)
  - `0x008C9549` → [DbgPrint](../../text/35/DbgPrint_function_00358CB0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008C9050  48 8B C4                        mov rax, rsp
008C9053  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
008C9057  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
008C905B  89 48 08                        mov dword ptr [rax + 8], ecx
008C905E  55                              push rbp
008C905F  56                              push rsi
008C9060  57                              push rdi
008C9061  41 54                           push r12
008C9063  41 55                           push r13
008C9065  41 56                           push r14
008C9067  41 57                           push r15
008C9069  48 8D 68 B1                     lea rbp, [rax - 0x4f]
008C906D  48 81 EC A0 00 00 00            sub rsp, 0xa0
008C9074  0F 57 C0                        xorps xmm0, xmm0
008C9077  33 C0                           xor eax, eax
008C9079  4D 8B E1                        mov r12, r9
008C907C  48 89 45 07                     mov qword ptr [rbp + 7], rax
008C9080  4D 8B F0                        mov r14, r8
008C9083  89 45 0F                        mov dword ptr [rbp + 0xf], eax
008C9086  0F 57 C9                        xorps xmm1, xmm1
008C9089  4C 8D 4D BF                     lea r9, [rbp - 0x41]
008C908D  33 FF                           xor edi, edi
008C908F  45 33 C0                        xor r8d, r8d
008C9092  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
008C9096  48 89 7D BF                     mov qword ptr [rbp - 0x41], rdi
008C909A  48 8B DA                        mov rbx, rdx
008C909D  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
008C90A1  89 7D 77                        mov dword ptr [rbp + 0x77], edi
008C90A4  44 8B F9                        mov r15d, ecx
008C90A7  0F 11 45 D7                     movups xmmword ptr [rbp - 0x29], xmm0
008C90AB  0F 11 4D C7                     movups xmmword ptr [rbp - 0x39], xmm1
008C90AF  E8 A8 04 00 00                  call 0x1408c955c
008C90B4  85 C0                           test eax, eax
008C90B6  0F 88 58 01 00 00               js 0x1408c9214
008C90BC  41 8B F7                        mov esi, r15d
008C90BF  48 8D 4D D7                     lea rcx, [rbp - 0x29]
008C90C3  81 E6 00 00 00 40               and esi, 0x40000000
008C90C9  44 8B FF                        mov r15d, edi
008C90CC  48 0F 45 DF                     cmovne rbx, rdi
008C90D0  48 8B D3                        mov rdx, rbx
008C90D3  E8 A8 16 B6 FF                  call 0x14042a780
008C90D8  BA 88 00 00 00                  mov edx, 0x88
008C90DD  41 B8 52 71 72 76               mov r8d, 0x76727152
008C90E3  8D 4A 78                        lea ecx, [rdx + 0x78]
008C90E6  E8 05 90 2B 00                  call 0x140b820f0
008C90EB  48 8B F8                        mov rdi, rax
008C90EE  48 85 C0                        test rax, rax
008C90F1  75 1B                           jne 0x1408c910e
008C90F3  BB 17 00 00 C0                  mov ebx, 0xc0000017
008C90F8  85 F6                           test esi, esi
008C90FA  0F 85 12 01 00 00               jne 0x1408c9212
008C9100  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
008C9104  E8 A7 41 DE FF                  call 0x1406ad2b0
008C9109  E9 04 01 00 00                  jmp 0x1408c9212
008C910E  44 89 78 08                     mov dword ptr [rax + 8], r15d
008C9112  41 8B DF                        mov ebx, r15d
008C9115  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
008C9119  41 BD 86 00 00 00               mov r13d, 0x86
008C911F  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
008C9123  49 8B 16                        mov rdx, qword ptr [r14]
008C9126  48 85 D2                        test rdx, rdx
008C9129  0F 84 97 00 00 00               je 0x1408c91c6
008C912F  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
008C9133  A8 20                           test al, 0x20
008C9135  74 1B                           je 0x1408c9152
008C9137  4D 39 7E 10                     cmp qword ptr [r14 + 0x10], r15
008C913B  0F 84 2C 01 00 00               je 0x1408c926d
008C9141  A8 01                           test al, 1
008C9143  0F 85 24 01 00 00               jne 0x1408c926d
008C9149  48 85 D2                        test rdx, rdx
008C914C  0F 85 1B 01 00 00               jne 0x1408c926d
008C9152  A8 03                           test al, 3
008C9154  0F 85 13 02 00 00               jne 0x1408c936d
008C915A  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
008C915E  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
008C9162  A8 01                           test al, 1
008C9164  0F 85 0D 01 00 00               jne 0x1408c9277
008C916A  48 85 D2                        test rdx, rdx
008C916D  0F 84 6F 01 00 00               je 0x1408c92e2
008C9173  48 8D 4D C7                     lea rcx, [rbp - 0x39]
008C9177  E8 04 16 B6 FF                  call 0x14042a780
008C917C  41 8B C7                        mov eax, r15d
008C917F  41 FF C7                        inc r15d
008C9182  83 F8 04                        cmp eax, 4
008C9185  0F 8F 79 02 00 00               jg 0x1408c9404
008C918B  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
008C918F  48 8D 45 77                     lea rax, [rbp + 0x77]
008C9193  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008C9198  48 8D 55 C7                     lea rdx, [rbp - 0x39]
008C919C  4C 8B CF                        mov r9, rdi
008C919F  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
008C91A4  41 B8 01 00 00 00               mov r8d, 1
008C91AA  E8 01 42 DE FF                  call 0x1406ad3b0
008C91AF  8B D8                           mov ebx, eax
008C91B1  3D 05 00 00 80                  cmp eax, 0x80000005
008C91B6  0F 85 5E 02 00 00               jne 0x1408c941a
008C91BC  8B 75 77                        mov esi, dword ptr [rbp + 0x77]
008C91BF  48 85 FF                        test rdi, rdi
008C91C2  74 79                           je 0x1408c923d
008C91C4  EB 6D                           jmp 0x1408c9233
008C91C6  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
008C91CA  A8 21                           test al, 0x21
008C91CC  0F 85 5D FF FF FF               jne 0x1408c912f
008C91D2  EB 05                           jmp 0x1408c91d9
008C91D4  BB 17 00 00 C0                  mov ebx, 0xc0000017
008C91D9  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
008C91DD  48 85 C9                        test rcx, rcx
008C91E0  74 0E                           je 0x1408c91f0
008C91E2  F7 45 57 00 00 00 40            test dword ptr [rbp + 0x57], 0x40000000
008C91E9  75 05                           jne 0x1408c91f0
008C91EB  E8 C0 40 DE FF                  call 0x1406ad2b0
008C91F0  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
008C91F4  48 85 C9                        test rcx, rcx
008C91F7  74 0A                           je 0x1408c9203
008C91F9  48 3B 4D BF                     cmp rcx, qword ptr [rbp - 0x41]
008C91FD  0F 85 F7 01 00 00               jne 0x1408c93fa
008C9203  48 85 FF                        test rdi, rdi
008C9206  74 0A                           je 0x1408c9212
008C9208  33 D2                           xor edx, edx
008C920A  48 8B CF                        mov rcx, rdi
008C920D  E8 5E 96 2B 00                  call 0x140b82870
008C9212  8B C3                           mov eax, ebx
008C9214  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
008C921C  48 81 C4 A0 00 00 00            add rsp, 0xa0
008C9223  41 5F                           pop r15
008C9225  41 5E                           pop r14
008C9227  41 5D                           pop r13
008C9229  41 5C                           pop r12
008C922B  5F                              pop rdi
008C922C  5E                              pop rsi
008C922D  5D                              pop rbp
008C922E  C3                              ret
008C922F  CC                              int3
008C9230  8B 75 77                        mov esi, dword ptr [rbp + 0x77]
008C9233  33 D2                           xor edx, edx
008C9235  48 8B CF                        mov rcx, rdi
008C9238  E8 33 96 2B 00                  call 0x140b82870
008C923D  41 B8 52 71 72 76               mov r8d, 0x76727152
008C9243  48 8D 56 0A                     lea rdx, [rsi + 0xa]
008C9247  B9 00 01 00 00                  mov ecx, 0x100
008C924C  E8 9F 8E 2B 00                  call 0x140b820f0
008C9251  33 C9                           xor ecx, ecx
008C9253  48 8B F8                        mov rdi, rax
008C9256  48 85 C0                        test rax, rax
008C9259  0F 84 75 FF FF FF               je 0x1408c91d4
008C925F  8B D9                           mov ebx, ecx
008C9261  89 48 08                        mov dword ptr [rax + 8], ecx
008C9264  4C 8D 6E 08                     lea r13, [rsi + 8]
008C9268  E9 0F FF FF FF                  jmp 0x1408c917c
008C926D  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008C9272  E9 62 FF FF FF                  jmp 0x1408c91d9
008C9277  48 85 D2                        test rdx, rdx
008C927A  74 F1                           je 0x1408c926d
008C927C  48 8D 4D D7                     lea rcx, [rbp - 0x29]
008C9280  E8 FB 14 B6 FF                  call 0x14042a780
008C9285  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
008C9289  4C 8D 45 E7                     lea r8, [rbp - 0x19]
008C928D  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
008C9291  48 8D 4D B7                     lea rcx, [rbp - 0x49]
008C9295  48 8D 45 D7                     lea rax, [rbp - 0x29]
008C9299  C7 45 E7 30 00 00 00            mov dword ptr [rbp - 0x19], 0x30
008C92A0  0F 57 C0                        xorps xmm0, xmm0
008C92A3  48 89 45 F7                     mov qword ptr [rbp - 9], rax
008C92A7  BA 00 00 00 02                  mov edx, 0x2000000
008C92AC  C7 45 FF 40 02 00 00            mov dword ptr [rbp - 1], 0x240
008C92B3  F3 0F 7F 45 07                  movdqu xmmword ptr [rbp + 7], xmm0
008C92B8  E8 53 40 DE FF                  call 0x1406ad310
008C92BD  8B D8                           mov ebx, eax
008C92BF  85 C0                           test eax, eax
008C92C1  78 0A                           js 0x1408c92cd
008C92C3  4D 39 3E                        cmp qword ptr [r14], r15
008C92C6  75 22                           jne 0x1408c92ea
008C92C8  EB 0B                           jmp 0x1408c92d5
008C92CA  45 33 FF                        xor r15d, r15d
008C92CD  85 DB                           test ebx, ebx
008C92CF  0F 88 04 FF FF FF               js 0x1408c91d9
008C92D5  4C 8B 65 6F                     mov r12, qword ptr [rbp + 0x6f]
008C92D9  49 83 C6 38                     add r14, 0x38
008C92DD  E9 41 FE FF FF                  jmp 0x1408c9123
008C92E2  A8 08                           test al, 8
008C92E4  0F 85 E2 01 00 00               jne 0x1408c94cc
008C92EA  45 8B E7                        mov r12d, r15d
008C92ED  41 8B F7                        mov esi, r15d
008C92F0  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
008C92F4  48 8D 45 77                     lea rax, [rbp + 0x77]
008C92F8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008C92FD  4C 8B CF                        mov r9, rdi
008C9300  41 B8 01 00 00 00               mov r8d, 1
008C9306  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
008C930B  8B D6                           mov edx, esi
008C930D  E8 1E 40 DE FF                  call 0x1406ad330
008C9312  8B D8                           mov ebx, eax
008C9314  3D 05 00 00 80                  cmp eax, 0x80000005
008C9319  75 72                           jne 0x1408c938d
008C931B  44 8B 7D 77                     mov r15d, dword ptr [rbp + 0x77]
008C931F  48 85 FF                        test rdi, rdi
008C9322  74 0A                           je 0x1408c932e
008C9324  33 D2                           xor edx, edx
008C9326  48 8B CF                        mov rcx, rdi
008C9329  E8 42 95 2B 00                  call 0x140b82870
008C932E  41 B8 52 71 72 76               mov r8d, 0x76727152
008C9334  49 8D 57 0A                     lea rdx, [r15 + 0xa]
008C9338  B9 00 01 00 00                  mov ecx, 0x100
008C933D  E8 AE 8D 2B 00                  call 0x140b820f0
008C9342  48 8B F8                        mov rdi, rax
008C9345  48 85 C0                        test rax, rax
008C9348  0F 84 86 FE FF FF               je 0x1408c91d4
008C934E  33 DB                           xor ebx, ebx
008C9350  4D 8D 6F 08                     lea r13, [r15 + 8]
008C9354  21 58 08                        and dword ptr [rax + 8], ebx
008C9357  FF CE                           dec esi
008C9359  41 8B C4                        mov eax, r12d
008C935C  41 FF C4                        inc r12d
008C935F  83 F8 04                        cmp eax, 4
008C9362  0F 8F D5 01 00 00               jg 0x1408c953d
008C9368  45 33 FF                        xor r15d, r15d
008C936B  EB 76                           jmp 0x1408c93e3
008C936D  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
008C9371  48 3B 4D BF                     cmp rcx, qword ptr [rbp - 0x41]
008C9375  0F 84 DF FD FF FF               je 0x1408c915a
008C937B  E8 30 3F DE FF                  call 0x1406ad2b0
008C9380  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
008C9384  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
008C9388  E9 CD FD FF FF                  jmp 0x1408c915a
008C938D  3D 1A 00 00 80                  cmp eax, 0x8000001a
008C9392  74 56                           je 0x1408c93ea
008C9394  85 C0                           test eax, eax
008C9396  78 29                           js 0x1408c93c1
008C9398  8A 45 7F                        mov al, byte ptr [rbp + 0x7f]
008C939B  4C 8D 4D 77                     lea r9, [rbp + 0x77]
008C939F  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
008C93A3  4C 8B C7                        mov r8, rdi
008C93A6  88 44 24 30                     mov byte ptr [rsp + 0x30], al
008C93AA  49 8B D6                        mov rdx, r14
008C93AD  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
008C93B1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008C93B6  44 89 6D 77                     mov dword ptr [rbp + 0x77], r13d
008C93BA  E8 85 54 FF FF                  call 0x1408be844
008C93BF  8B D8                           mov ebx, eax
008C93C1  3D 23 00 00 C0                  cmp eax, 0xc0000023
008C93C6  0F 84 4F FF FF FF               je 0x1408c931b
008C93CC  85 C0                           test eax, eax
008C93CE  0F 88 F9 FE FF FF               js 0x1408c92cd
008C93D4  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
008C93D8  45 8B E7                        mov r12d, r15d
008C93DB  A8 40                           test al, 0x40
008C93DD  0F 85 10 01 00 00               jne 0x1408c94f3
008C93E3  FF C6                           inc esi
008C93E5  E9 06 FF FF FF                  jmp 0x1408c92f0
008C93EA  85 F6                           test esi, esi
008C93EC  0F 84 35 01 00 00               je 0x1408c9527
008C93F2  41 8B DF                        mov ebx, r15d
008C93F5  E9 D3 FE FF FF                  jmp 0x1408c92cd
008C93FA  E8 B1 3E DE FF                  call 0x1406ad2b0
008C93FF  E9 FF FD FF FF                  jmp 0x1408c9203
008C9404  BA FD 04 00 00                  mov edx, 0x4fd
008C9409  48 8D 0D A0 C5 23 00            lea rcx, [rip + 0x23c5a0]
008C9410  E8 9B F8 A8 FF                  call 0x140358cb0
008C9415  E9 BF FD FF FF                  jmp 0x1408c91d9
008C941A  33 C9                           xor ecx, ecx
008C941C  85 C0                           test eax, eax
008C941E  78 6A                           js 0x1408c948a
008C9420  83 7F 04 07                     cmp dword ptr [rdi + 4], 7
008C9424  75 0B                           jne 0x1408c9431
008C9426  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
008C9429  66 89 0C 38                     mov word ptr [rax + rdi], cx
008C942D  83 47 0C 02                     add dword ptr [rdi + 0xc], 2
008C9431  8A 45 7F                        mov al, byte ptr [rbp + 0x7f]
008C9434  4C 8D 4D 77                     lea r9, [rbp + 0x77]
008C9438  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
008C943C  4C 8B C7                        mov r8, rdi
008C943F  88 44 24 30                     mov byte ptr [rsp + 0x30], al
008C9443  49 8B D6                        mov rdx, r14
008C9446  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
008C944B  44 89 6D 77                     mov dword ptr [rbp + 0x77], r13d
008C944F  E8 F0 53 FF FF                  call 0x1408be844
008C9454  8B D8                           mov ebx, eax
008C9456  3D 23 00 00 C0                  cmp eax, 0xc0000023
008C945B  0F 84 CF FD FF FF               je 0x1408c9230
008C9461  45 33 FF                        xor r15d, r15d
008C9464  85 C0                           test eax, eax
008C9466  0F 88 61 FE FF FF               js 0x1408c92cd
008C946C  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
008C9470  A8 40                           test al, 0x40
008C9472  0F 84 5D FE FF FF               je 0x1408c92d5
008C9478  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
008C947C  48 8D 55 C7                     lea rdx, [rbp - 0x39]
008C9480  E8 2B 58 DE FF                  call 0x1406aecb0
008C9485  E9 4B FE FF FF                  jmp 0x1408c92d5
008C948A  3D 34 00 00 C0                  cmp eax, 0xc0000034
008C948F  75 2B                           jne 0x1408c94bc
008C9491  8A 45 7F                        mov al, byte ptr [rbp + 0x7f]
008C9494  4C 8D 4D 77                     lea r9, [rbp + 0x77]
008C9498  89 4F 04                        mov dword ptr [rdi + 4], ecx
008C949B  4C 8B C7                        mov r8, rdi
008C949E  89 4F 0C                        mov dword ptr [rdi + 0xc], ecx
008C94A1  49 8B D6                        mov rdx, r14
008C94A4  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
008C94A8  88 44 24 30                     mov byte ptr [rsp + 0x30], al
008C94AC  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
008C94B1  44 89 6D 77                     mov dword ptr [rbp + 0x77], r13d
008C94B5  E8 8A 53 FF FF                  call 0x1408be844
008C94BA  8B D8                           mov ebx, eax
008C94BC  3D 23 00 00 C0                  cmp eax, 0xc0000023
008C94C1  0F 84 F5 FC FF FF               je 0x1408c91bc
008C94C7  E9 FE FD FF FF                  jmp 0x1408c92ca
008C94CC  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
008C94D0  45 33 C9                        xor r9d, r9d
008C94D3  49 8B 06                        mov rax, qword ptr [r14]
008C94D6  45 33 C0                        xor r8d, r8d
008C94D9  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008C94DE  33 D2                           xor edx, edx
008C94E0  33 C9                           xor ecx, ecx
008C94E2  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
008C94E7  E8 E4 15 DF FF                  call 0x1406baad0
008C94EC  8B D8                           mov ebx, eax
008C94EE  E9 DA FD FF FF                  jmp 0x1408c92cd
008C94F3  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
008C94F7  48 8D 47 14                     lea rax, [rdi + 0x14]
008C94FB  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
008C94FF  48 8D 55 C7                     lea rdx, [rbp - 0x39]
008C9503  0F B7 47 10                     movzx eax, word ptr [rdi + 0x10]
008C9507  66 89 45 C7                     mov word ptr [rbp - 0x39], ax
008C950B  0F B7 47 10                     movzx eax, word ptr [rdi + 0x10]
008C950F  66 89 45 C9                     mov word ptr [rbp - 0x37], ax
008C9513  E8 98 57 DE FF                  call 0x1406aecb0
008C9518  85 C0                           test eax, eax
008C951A  0F 88 C3 FE FF FF               js 0x1408c93e3
008C9520  FF CE                           dec esi
008C9522  E9 BC FE FF FF                  jmp 0x1408c93e3
008C9527  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
008C952B  A8 04                           test al, 4
008C952D  0F 84 BF FE FF FF               je 0x1408c93f2
008C9533  BB 34 00 00 C0                  mov ebx, 0xc0000034
008C9538  E9 90 FD FF FF                  jmp 0x1408c92cd
008C953D  BA B2 05 00 00                  mov edx, 0x5b2
008C9542  48 8D 0D 67 C4 23 00            lea rcx, [rip + 0x23c467]
008C9549  E8 62 F7 A8 FF                  call 0x140358cb0
008C954E  45 33 FF                        xor r15d, r15d
008C9551  E9 7F FD FF FF                  jmp 0x1408c92d5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpQueryRegistryValues(int a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p30;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    result = 0;
    *(unsigned __int64 *)(v_rsp - 79 + 7) = 0;
    *(unsigned int *)(v_rsp - 79 + 15) = 0;
    v_rdi = 0;
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 25) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 79 - 65) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 9) = v_xmm0;
    *(unsigned int *)(v_rsp - 79 + 119) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 41) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 79 - 57) = v_xmm1;
    result = RtlpGetRegistryHandle(a1, a2, a3, v_rsp - 79 - 65);
    if (sign_flag) goto loc_008C9214;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) & (0x40000000ULL));
    if (condition_is_not_equal) { a2 = 0; }
    result = RtlInitUnicodeString(v_rsp - 79 - 41, a2, a3, v_rsp - 79 - 65);
    result = ExAllocatePool2(136 + 120, 136, (unsigned int)(0x76727152ULL), v_rsp - 79 - 65);
    if (result != 0) goto loc_008C910E;
    if ((unsigned int)(v_rsi) != 0) goto loc_008C9212;
    result = ZwClose(*(unsigned __int64 *)(v_rsp - 79 - 65), 136, (unsigned int)(0x76727152ULL), v_rsp - 79 - 65);
    goto loc_008C9212;
loc_008C910E:
    *(unsigned int *)(result + 8) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 73) = *(unsigned __int64 *)(v_rsp - 79 - 65);
loc_008C9123:
    if (*(unsigned __int64 *)(a3) == 0) goto loc_008C91C6;
loc_008C912F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 8)))) & (32)) == 0) goto loc_008C9152;
    if ((*(unsigned __int64 *)(a3 + 16)) == 0) goto loc_008C926D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 8)))) & (1)) != 0) goto loc_008C926D;
    if (*(unsigned __int64 *)(a3) != 0) goto loc_008C926D;
loc_008C9152:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 8)))) & (3)) != 0) goto loc_008C936D;
loc_008C915A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 8)))) & (1)) != 0) goto loc_008C9277;
    if (*(unsigned __int64 *)(a3 + 16) == 0) goto loc_008C92E2;
    result = RtlInitUnicodeString(v_rsp - 79 - 57, *(unsigned __int64 *)(a3 + 16), (unsigned int)(0x76727152ULL), v_rsp - 79 - 65);
loc_008C917C:
    v_r15 = (unsigned int)((0) + 1);
    if (0 > 4) goto loc_008C9404;
    v_stack_mB0 = v_rsp - 79 + 119;
    v_stack_mB8 = 134;
    result = ZwQueryValueKey(*(unsigned __int64 *)(v_rsp - 79 - 73), v_rsp - 79 - 57, 1, result);
    if (((unsigned int)(result)) != 0x80000005ULL) goto loc_008C941A;
loc_008C91BC:
    if (result == 0) goto loc_008C923D;
    goto loc_008C9233;
loc_008C91C6:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 8)))) & (33)) != 0) goto loc_008C912F;
    goto loc_008C91D9;
loc_008C91D4:
loc_008C91D9:
    if (*(unsigned __int64 *)(v_rsp - 79 - 65) == 0) goto loc_008C91F0;
    result = (unsigned int)(*(unsigned int *)(a3 + 8));
    if (((*(unsigned int *)(v_rsp - 79 + 87)) & (0x40000000ULL)) == 0) {
        result = ZwClose(*(unsigned __int64 *)(v_rsp - 79 - 65), v_rsp - 79 - 57, 1, result);
    }
    if (*(unsigned __int64 *)(v_rsp - 79 - 73) == 0) goto loc_008C9203;
    if ((*(unsigned __int64 *)(v_rsp - 79 - 73)) != (*(unsigned __int64 *)(v_rsp - 79 - 65))) goto loc_008C93FA;
loc_008C9203:
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, 1, result);
    }
loc_008C9214:
    v_rsp = (v_rsp) + (160);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000017ULL)));
loc_008C9230:
loc_008C9233:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 1, result);
loc_008C923D:
    result = ExAllocatePool2(256, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)) + 10, (unsigned int)(0x76727152ULL), result);
    a1 = 0;
    if (result == 0) goto loc_008C91D4;
    *(unsigned int *)(result + 8) = 0;
    goto loc_008C917C;
loc_008C926D:
    goto loc_008C91D9;
loc_008C9277:
    if ((unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)) + 10 == 0) goto loc_008C926D;
    result = RtlInitUnicodeString(v_rsp - 79 - 41, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)) + 10, (unsigned int)(0x76727152ULL), result);
    *(unsigned __int64 *)(v_rsp - 79 - 17) = *(unsigned __int64 *)(v_rsp - 79 - 65);
    *(unsigned int *)(v_rsp - 79 - 25) = 48;
    *(unsigned __int64 *)(v_rsp - 79 - 9) = v_rsp - 79 - 41;
    *(unsigned int *)(v_rsp - 79 - 1) = 576;
    *(unsigned __int64 *)(v_rsp - 79 + 7) = v_xmm0;
    result = ZwOpenKey(v_rsp - 79 - 73, (unsigned int)(0x2000000ULL), v_rsp - 79 - 25, result);
    if (sign_flag) goto loc_008C92CD;
    if ((*(unsigned __int64 *)(a3)) != v_r15) goto loc_008C92EA;
    goto loc_008C92D5;
loc_008C92CA:
    v_r15 = 0;
loc_008C92CD:
    if (sign_flag) goto loc_008C91D9;
loc_008C92D5:
    v_r14 = (a3) + (56);
    goto loc_008C9123;
loc_008C92E2:
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_008C94CC;
loc_008C92EA:
loc_008C92F0:
    v_stack_p28 = v_rsp - 79 + 119;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)) + 8);
    result = ZwEnumerateValueKey(*(unsigned __int64 *)(v_rsp - 79 - 73), 0, 1, result);
    if (((unsigned int)(result)) != 0x80000005ULL) goto loc_008C938D;
loc_008C931B:
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, 1, result);
    }
    result = ExAllocatePool2(256, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)) + 10, (unsigned int)(0x76727152ULL), result);
    if (result == 0) goto loc_008C91D4;
    v_rbx = 0;
    v_rsi = (unsigned int)((0) - 1);
    v_r12 = (unsigned int)((0) + 1);
    if (0 > 4) goto loc_008C953D;
    v_r15 = 0;
    goto loc_008C93E3;
loc_008C936D:
    if ((*(unsigned __int64 *)(v_rsp - 79 - 73)) == (*(unsigned __int64 *)(v_rsp - 79 - 65))) goto loc_008C915A;
    result = ZwClose(*(unsigned __int64 *)(v_rsp - 79 - 73), (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)) + 10, (unsigned int)(0x76727152ULL), result);
    *(unsigned __int64 *)(v_rsp - 79 - 73) = *(unsigned __int64 *)(v_rsp - 79 - 65);
    goto loc_008C915A;
loc_008C938D:
    if (((unsigned int)(*(unsigned __int64 *)(v_rsp - 79 - 65))) == 0x8000001AULL) goto loc_008C93EA;
    result = *(unsigned __int64 *)(v_rsp - 79 - 65);
    if (!(sign_flag)) {
        result = *(unsigned __int8 *)(v_rsp - 79 + 127);
        a4 = v_rsp - 79 + 119;
        a1 = *(unsigned __int64 *)(v_rsp - 79 - 73);
        a3 = result;
        v_stack_p30 = (unsigned __int8)(result);
        a2 = v_r14;
        result = *(unsigned __int64 *)(v_rsp - 79 + 111);
        v_stack_p20 = result;
        *(unsigned int *)(v_rsp - 79 + 119) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)) + 8);
        result = RtlpCallQueryRegistryRoutine(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_008C931B;
    if (sign_flag) goto loc_008C92CD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r14 + 8)))) & (64)) != 0) goto loc_008C94F3;
loc_008C93E3:
    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_008C92F0;
loc_008C93EA:
    if ((unsigned int)(v_rsi) == 0) goto loc_008C9527;
loc_008C93F2:
    goto loc_008C92CD;
loc_008C93FA:
    result = ZwClose(a1, a2, a3, a4);
    goto loc_008C9203;
loc_008C9404:
    result = DbgPrint(v_rip + 2344352, (unsigned int)(0x4FDULL), a3, a4);
    goto loc_008C91D9;
loc_008C941A:
    a1 = 0;
    if (sign_flag) goto loc_008C948A;
    if ((*(unsigned int *)(result + 4)) == 7) {
        result = *(unsigned int *)(v_rsp - 79 + 119);
        *(unsigned __int16 *)(result + result * 1) = 0;
    }
    v_stack_p30 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 79 + 127));
    v_stack_p20 = 0;
    *(unsigned int *)(v_rsp - 79 + 119) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)) + 8);
    result = RtlpCallQueryRegistryRoutine(*(unsigned __int64 *)(v_rsp - 79 - 73), v_r14, result, v_rsp - 79 + 119);
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_008C9230;
    v_r15 = 0;
    if (sign_flag) goto loc_008C92CD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r14 + 8)))) & (64)) == 0) goto loc_008C92D5;
    result = ZwDeleteValueKey(*(unsigned __int64 *)(v_rsp - 79 - 73), v_rsp - 79 - 57, result, v_rsp - 79 + 119);
    goto loc_008C92D5;
loc_008C948A:
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) == 0xC0000034ULL) {
        result = *(unsigned __int8 *)(v_rsp - 79 + 127);
        a4 = v_rsp - 79 + 119;
        *(unsigned int *)(result + 4) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 79 - 73));
        a3 = result;
        *(unsigned int *)(result + 12) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 79 - 73));
        a2 = v_r14;
        a1 = *(unsigned __int64 *)(v_rsp - 79 - 73);
        v_stack_p30 = (unsigned __int8)(result);
        v_stack_p20 = 0;
        *(unsigned int *)(v_rsp - 79 + 119) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)) + 8);
        result = RtlpCallQueryRegistryRoutine(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_008C91BC;
    goto loc_008C92CA;
loc_008C94CC:
    a4 = 0;
    a3 = 0;
    v_stack_p28 = *(unsigned __int64 *)(v_r14 + 24);
    a2 = 0;
    a1 = 0;
    v_stack_p20 = 0;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_008C92CD;
loc_008C94F3:
    *(unsigned __int64 *)(v_rsp - 79 - 49) = result + 20;
    *(unsigned __int16 *)(v_rsp - 79 - 57) = (unsigned __int16)(*(unsigned __int16 *)(result + 16));
    *(unsigned __int16 *)(v_rsp - 79 - 55) = (unsigned __int16)(*(unsigned __int16 *)(result + 16));
    result = ZwDeleteValueKey(*(unsigned __int64 *)(v_rsp - 79 - 73), v_rsp - 79 - 57, a3, a4);
    if (sign_flag) goto loc_008C93E3;
    v_rsi = (unsigned int)((v_rsi) - 1);
    goto loc_008C93E3;
loc_008C9527:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r14 + 8)))) & (4)) == 0) goto loc_008C93F2;
    goto loc_008C92CD;
loc_008C953D:
    result = DbgPrint(v_rip + 2344039, (unsigned int)(0x5B2ULL), a3, a4);
    v_r15 = 0;
    goto loc_008C92D5;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpQueryRegistryValues(int32_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p30;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    result = 0;
    *(uint64_t *)(local_rsp - 0x4F + 0x7) = 0;
    *(uint32_t *)(local_rsp - 0x4F + 0xF) = 0;
    local_rdi = 0;
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x19) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x4F - 0x41) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x9) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x4F + 0x77) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x29) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x4F - 0x39) = v_xmm1;
    result = RtlpGetRegistryHandle(Arg1, Arg2, Arg3, local_rsp - 79 - 65);
    if (sign_flag) goto loc_008C9214;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) & (0x40000000ULL));
    if (condition_is_not_equal) { Arg2 = 0; }
    result = RtlInitUnicodeString(local_rsp - 79 - 41, Arg2, Arg3, local_rsp - 79 - 65);
    result = ExAllocatePool2(136 + 120, 136, (uint32_t)(0x76727152ULL), local_rsp - 79 - 65);
    if (result != 0) goto loc_008C910E;
    if ((uint32_t)(local_rsi) != 0) goto loc_008C9212;
    result = ZwClose(*(uint64_t *)(local_rsp - 0x4F - 0x41), 136, (uint32_t)(0x76727152ULL), local_rsp - 79 - 65);
    goto loc_008C9212;
loc_008C910E:
    *(uint32_t *)(result + 0x8) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x49) = *(uint64_t *)(local_rsp - 0x4F - 0x41);
loc_008C9123:
    if (*(uint64_t *)(arg3) == 0) goto loc_008C91C6;
loc_008C912F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x8)))) & (32)) == 0) goto loc_008C9152;
    if ((*(uint64_t *)(arg3 + 0x10)) == 0) goto loc_008C926D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x8)))) & (1)) != 0) goto loc_008C926D;
    if (*(uint64_t *)(arg3) != 0) goto loc_008C926D;
loc_008C9152:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x8)))) & (3)) != 0) goto loc_008C936D;
loc_008C915A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x8)))) & (1)) != 0) goto loc_008C9277;
    if (*(uint64_t *)(arg3 + 0x10) == 0) goto loc_008C92E2;
    result = RtlInitUnicodeString(local_rsp - 79 - 57, *(uint64_t *)(arg3 + 0x10), (uint32_t)(0x76727152ULL), local_rsp - 79 - 65);
loc_008C917C:
    local_r15 = (uint32_t)((0) + 1);
    if (0 > 4) goto loc_008C9404;
    v_stack_mB0 = local_rsp - 79 + 119;
    v_stack_mB8 = 134;
    result = ZwQueryValueKey(*(uint64_t *)(local_rsp - 0x4F - 0x49), local_rsp - 79 - 57, 1, result);
    if (((uint32_t)(result)) != 0x80000005ULL) goto loc_008C941A;
loc_008C91BC:
    if (result == 0) goto loc_008C923D;
    goto loc_008C9233;
loc_008C91C6:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x8)))) & (33)) != 0) goto loc_008C912F;
    goto loc_008C91D9;
loc_008C91D4:
loc_008C91D9:
    if (*(uint64_t *)(local_rsp - 0x4F - 0x41) == 0) goto loc_008C91F0;
    result = (uint32_t)(*(uint32_t *)(arg3 + 0x8));
    if (((*(uint32_t *)(local_rsp - 0x4F + 0x57)) & (0x40000000ULL)) == 0) {
        result = ZwClose(*(uint64_t *)(local_rsp - 0x4F - 0x41), local_rsp - 79 - 57, 1, result);
    }
    if (*(uint64_t *)(local_rsp - 0x4F - 0x49) == 0) goto loc_008C9203;
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x49)) != (*(uint64_t *)(local_rsp - 0x4F - 0x41))) goto loc_008C93FA;
loc_008C9203:
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, 1, result);
    }
loc_008C9214:
    local_rsp = (local_rsp) + (160);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000017ULL)));
loc_008C9230:
loc_008C9233:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 1, result);
loc_008C923D:
    result = ExAllocatePool2(256, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)) + 10, (uint32_t)(0x76727152ULL), result);
    Arg1 = 0;
    if (result == 0) goto loc_008C91D4;
    *(uint32_t *)(result + 0x8) = 0;
    goto loc_008C917C;
loc_008C926D:
    goto loc_008C91D9;
loc_008C9277:
    if ((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)) + 10 == 0) goto loc_008C926D;
    result = RtlInitUnicodeString(local_rsp - 79 - 41, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)) + 10, (uint32_t)(0x76727152ULL), result);
    *(uint64_t *)(local_rsp - 0x4F - 0x11) = *(uint64_t *)(local_rsp - 0x4F - 0x41);
    *(uint32_t *)(local_rsp - 0x4F - 0x19) = 48;
    *(uint64_t *)(local_rsp - 0x4F - 0x9) = local_rsp - 79 - 41;
    *(uint32_t *)(local_rsp - 0x4F - 0x1) = 576;
    *(uint64_t *)(local_rsp - 0x4F + 0x7) = v_xmm0;
    result = ZwOpenKey(local_rsp - 79 - 73, (uint32_t)(0x2000000ULL), local_rsp - 79 - 25, result);
    if (sign_flag) goto loc_008C92CD;
    if ((*(uint64_t *)(arg3)) != local_r15) goto loc_008C92EA;
    goto loc_008C92D5;
loc_008C92CA:
    local_r15 = 0;
loc_008C92CD:
    if (sign_flag) goto loc_008C91D9;
loc_008C92D5:
    local_r14 = (Arg3) + (56);
    goto loc_008C9123;
loc_008C92E2:
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_008C94CC;
loc_008C92EA:
loc_008C92F0:
    v_stack_p28 = local_rsp - 79 + 119;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)) + 8);
    result = ZwEnumerateValueKey(*(uint64_t *)(local_rsp - 0x4F - 0x49), 0, 1, result);
    if (((uint32_t)(result)) != 0x80000005ULL) goto loc_008C938D;
loc_008C931B:
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, 1, result);
    }
    result = ExAllocatePool2(256, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)) + 10, (uint32_t)(0x76727152ULL), result);
    if (result == 0) goto loc_008C91D4;
    local_rbx = 0;
    local_rsi = (uint32_t)((0) - 1);
    local_r12 = (uint32_t)((0) + 1);
    if (0 > 4) goto loc_008C953D;
    local_r15 = 0;
    goto loc_008C93E3;
loc_008C936D:
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x49)) == (*(uint64_t *)(local_rsp - 0x4F - 0x41))) goto loc_008C915A;
    result = ZwClose(*(uint64_t *)(local_rsp - 0x4F - 0x49), (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)) + 10, (uint32_t)(0x76727152ULL), result);
    *(uint64_t *)(local_rsp - 0x4F - 0x49) = *(uint64_t *)(local_rsp - 0x4F - 0x41);
    goto loc_008C915A;
loc_008C938D:
    if (((uint32_t)(*(uint64_t *)(local_rsp - 0x4F - 0x41))) == 0x8000001AULL) goto loc_008C93EA;
    result = *(uint64_t *)(local_rsp - 0x4F - 0x41);
    if (!(sign_flag)) {
        result = *(uint8_t *)(local_rsp - 0x4F + 0x7F);
        Arg4 = local_rsp - 79 + 119;
        Arg1 = *(uint64_t *)(local_rsp - 0x4F - 0x49);
        Arg3 = result;
        v_stack_p30 = (uint8_t)(result);
        Arg2 = local_r14;
        result = *(uint64_t *)(local_rsp - 0x4F + 0x6F);
        v_stack_p20 = result;
        *(uint32_t *)(local_rsp - 0x4F + 0x77) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)) + 8);
        result = RtlpCallQueryRegistryRoutine(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
    }
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_008C931B;
    if (sign_flag) goto loc_008C92CD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x8)))) & (64)) != 0) goto loc_008C94F3;
loc_008C93E3:
    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_008C92F0;
loc_008C93EA:
    if ((uint32_t)(local_rsi) == 0) goto loc_008C9527;
loc_008C93F2:
    goto loc_008C92CD;
loc_008C93FA:
    result = ZwClose(Arg1, Arg2, Arg3, Arg4);
    goto loc_008C9203;
loc_008C9404:
    result = DbgPrint(v_rip + 2344352, (uint32_t)(0x4FDULL), Arg3, Arg4);
    goto loc_008C91D9;
loc_008C941A:
    Arg1 = 0;
    if (sign_flag) goto loc_008C948A;
    if ((*(uint32_t *)(result + 0x4)) == 7) {
        result = *(uint32_t *)(local_rsp - 0x4F + 0x77);
        *(uint16_t *)(result + result * 1) = 0;
    }
    v_stack_p30 = (uint8_t)(*(uint8_t *)(local_rsp - 0x4F + 0x7F));
    v_stack_p20 = 0;
    *(uint32_t *)(local_rsp - 0x4F + 0x77) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)) + 8);
    result = RtlpCallQueryRegistryRoutine(*(uint64_t *)(local_rsp - 0x4F - 0x49), local_r14, result, local_rsp - 79 + 119);
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_008C9230;
    local_r15 = 0;
    if (sign_flag) goto loc_008C92CD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x8)))) & (64)) == 0) goto loc_008C92D5;
    result = ZwDeleteValueKey(*(uint64_t *)(local_rsp - 0x4F - 0x49), local_rsp - 79 - 57, result, local_rsp - 79 + 119);
    goto loc_008C92D5;
loc_008C948A:
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) == 0xC0000034ULL) {
        result = *(uint8_t *)(local_rsp - 0x4F + 0x7F);
        Arg4 = local_rsp - 79 + 119;
        *(uint32_t *)(result + 0x4) = (uint32_t)(*(uint64_t *)(local_rsp - 0x4F - 0x49));
        Arg3 = result;
        *(uint32_t *)(result + 0xC) = (uint32_t)(*(uint64_t *)(local_rsp - 0x4F - 0x49));
        Arg2 = local_r14;
        Arg1 = *(uint64_t *)(local_rsp - 0x4F - 0x49);
        v_stack_p30 = (uint8_t)(result);
        v_stack_p20 = 0;
        *(uint32_t *)(local_rsp - 0x4F + 0x77) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)) + 8);
        result = RtlpCallQueryRegistryRoutine(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
    }
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_008C91BC;
    goto loc_008C92CA;
loc_008C94CC:
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p28 = *(uint64_t *)(local_r14 + 0x18);
    Arg2 = 0;
    Arg1 = 0;
    v_stack_p20 = 0;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    goto loc_008C92CD;
loc_008C94F3:
    *(uint64_t *)(local_rsp - 0x4F - 0x31) = result + 20;
    *(uint16_t *)(local_rsp - 0x4F - 0x39) = (uint16_t)(*(uint16_t *)(result + 0x10));
    *(uint16_t *)(local_rsp - 0x4F - 0x37) = (uint16_t)(*(uint16_t *)(result + 0x10));
    result = ZwDeleteValueKey(*(uint64_t *)(local_rsp - 0x4F - 0x49), local_rsp - 79 - 57, Arg3, Arg4);
    if (sign_flag) goto loc_008C93E3;
    local_rsi = (uint32_t)((local_rsi) - 1);
    goto loc_008C93E3;
loc_008C9527:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x8)))) & (4)) == 0) goto loc_008C93F2;
    goto loc_008C92CD;
loc_008C953D:
    result = DbgPrint(v_rip + 2344039, (uint32_t)(0x5B2ULL), Arg3, Arg4);
    local_r15 = 0;
    goto loc_008C92D5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C9050&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
