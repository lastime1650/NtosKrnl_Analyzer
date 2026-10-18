# EtwpKernelTraceRundown

- RVA: `0x009E4080`–`0x009E446E` (길이 `1,006` bytes)
- VA: `0x00000001409E4080`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A4080`
- 디코드: `292`개 명령, `1,006/1,006` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009E40B3` → [IoSetThreadHardErrorMode](../../text/46/IoSetThreadHardErrorMode_function_00466BF0.md) (function, `0x00466BF0`)
- `0x009E40C9` → [EtwpOpenLogger](../../text/2F/EtwpOpenLogger_function_002F77F0.md) (function, `0x002F77F0`)
- `0x009E40F5` → [EtwpLogRefSetAutoMark](../7C/EtwpLogRefSetAutoMark_function_007C01A8.md) (function, `0x007C01A8`)
- `0x009E4138` → [EtwpProcessThreadImageRundown](EtwpProcessThreadImageRundown_function_009E4568.md) (function, `0x009E4568`)
- `0x009E417A` → [CmEtwRunDown](../A8/CmEtwRunDown_function_00A85AC0.md) (function, `0x00A85AC0`)
- `0x009E4192` → [EtwpSampledProfileRunDown](../A7/EtwpSampledProfileRunDown_function_00A7F60C.md) (function, `0x00A7F60C`)
- `0x009E41B3` → [EtwpSampledProfileRunDown](../A7/EtwpSampledProfileRunDown_function_00A7F60C.md) (function, `0x00A7F60C`)
- `0x009E41D4` → [EtwpSpinLockConfigRunDown](../7C/EtwpSpinLockConfigRunDown_function_007C0B54.md) (function, `0x007C0B54`)
- `0x009E41F6` → [EtwpExecutiveResourceConfigRunDown](../7C/EtwpExecutiveResourceConfigRunDown_function_007C005C.md) (function, `0x007C005C`)
- `0x009E421A` → [PsPerfLogSessionRundown](../78/PsPerfLogSessionRundown_function_00788DB0.md) (function, `0x00788DB0`)
- `0x009E4235` → [EtwpPoolRunDown](../7C/EtwpPoolRunDown_function_007C0650.md) (function, `0x007C0650`)
- `0x009E4250` → [EtwpClockSourceRunDown](../7B/EtwpClockSourceRunDown_function_007BFEE0.md) (function, `0x007BFEE0`)
- `0x009E426B` → [KeTraceHgsPlusRundown](../../text/5C/KeTraceHgsPlusRundown_function_005C3728.md) (function, `0x005C3728`)
- `0x009E4286` → [KeTraceParkingRundown](../../text/5C/KeTraceParkingRundown_function_005C95F4.md) (function, `0x005C95F4`)
- `0x009E42A2` → [KeTraceThreadAffinityRundown](../../text/5C/KeTraceThreadAffinityRundown_function_005C379C.md) (function, `0x005C379C`)
- `0x009E42BC` → [KeTraceSchedulingGroupRundown](../../text/5C/KeTraceSchedulingGroupRundown_function_005C8D20.md) (function, `0x005C8D20`)
- `0x009E42E5` → [MmLogSystemShareablePfnInfo](../80/MmLogSystemShareablePfnInfo_function_008093F4.md) (function, `0x008093F4`)
- `0x009E42FC` → [MmIdentifyPhysicalMemory](../AA/MmIdentifyPhysicalMemory_function_00AAD05C.md) (function, `0x00AAD05C`)
- `0x009E431C` → [EtwpLogMemInfoRundown](../7C/EtwpLogMemInfoRundown_function_007C0144.md) (function, `0x007C0144`)
- `0x009E4345` → [MmIdentifyPhysicalMemory](../AA/MmIdentifyPhysicalMemory_function_00AAD05C.md) (function, `0x00AAD05C`)
- `0x009E4366` → [MmLogQueryCombineStats](../90/MmLogQueryCombineStats_function_00901D04.md) (function, `0x00901D04`)
- `0x009E4388` → [WmiTraceRundownNotify](WmiTraceRundownNotify_function_009E46E0.md) (function, `0x009E46E0`)
- `0x009E43B4` → [PopExecuteOnTargetProcessors](../../text/2D/PopExecuteOnTargetProcessors_function_002DD834.md) (function, `0x002DD834`)
- `0x009E43D3` → [EtwpObjectTypeRundown](../7C/EtwpObjectTypeRundown_function_007C04F4.md) (function, `0x007C04F4`)
- `0x009E43E9` → [EtwpProcessorRundown](../7C/EtwpProcessorRundown_function_007C0868.md) (function, `0x007C0868`)
- `0x009E440F` → [MmIdentifyPhysicalMemory](../AA/MmIdentifyPhysicalMemory_function_00AAD05C.md) (function, `0x00AAD05C`)
- `0x009E441A` → [MmLogSystemShareablePfnInfo](../80/MmLogSystemShareablePfnInfo_function_008093F4.md) (function, `0x008093F4`)
- `0x009E4432` → [EtwpLogRefSetAutoMark](../7C/EtwpLogRefSetAutoMark_function_007C01A8.md) (function, `0x007C01A8`)
- `0x009E4442` → [EtwpCloseLogger](../../text/41/EtwpCloseLogger_function_00418060.md) (function, `0x00418060`)
- `0x009E444A` → [IoSetThreadHardErrorMode](../../text/46/IoSetThreadHardErrorMode_function_00466BF0.md) (function, `0x00466BF0`)

### Direct callers
- [EtwpUpdateSelectedGroupMasks](../../text/49/EtwpUpdateSelectedGroupMasks_function_0049B114.md) at `0x0049B427`
- [EtwpUpdateSelectedGroupMasks](../../text/49/EtwpUpdateSelectedGroupMasks_function_0049B114.md) at `0x0049B59D`
- [EtwKernelMemoryRundown](../7B/EtwKernelMemoryRundown_function_007B7DEC.md) at `0x007B7E65`
- [EtwpLogKernelTraceRundown](EtwpLogKernelTraceRundown_function_009E400C.md) at `0x009E4054`

### Static image references
- `0x009E43A3` → RVA `0x004A22D0` (`PpmTracePerfIdleRundown`; read)
- `0x009E43AD` → RVA `0x00FC7120` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x009E40B3` → [IoSetThreadHardErrorMode](../../text/46/IoSetThreadHardErrorMode_function_00466BF0.md) (`PAGE` → `.text`)
  - `0x009E40C9` → [EtwpOpenLogger](../../text/2F/EtwpOpenLogger_function_002F77F0.md) (`PAGE` → `.text`)
  - `0x009E426B` → [KeTraceHgsPlusRundown](../../text/5C/KeTraceHgsPlusRundown_function_005C3728.md) (`PAGE` → `.text`)
  - `0x009E4286` → [KeTraceParkingRundown](../../text/5C/KeTraceParkingRundown_function_005C95F4.md) (`PAGE` → `.text`)
  - `0x009E42A2` → [KeTraceThreadAffinityRundown](../../text/5C/KeTraceThreadAffinityRundown_function_005C379C.md) (`PAGE` → `.text`)
  - `0x009E42BC` → [KeTraceSchedulingGroupRundown](../../text/5C/KeTraceSchedulingGroupRundown_function_005C8D20.md) (`PAGE` → `.text`)
  - `0x009E43B4` → [PopExecuteOnTargetProcessors](../../text/2D/PopExecuteOnTargetProcessors_function_002DD834.md) (`PAGE` → `.text`)
  - `0x009E4442` → [EtwpCloseLogger](../../text/41/EtwpCloseLogger_function_00418060.md) (`PAGE` → `.text`)
  - `0x009E444A` → [IoSetThreadHardErrorMode](../../text/46/IoSetThreadHardErrorMode_function_00466BF0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009E4080  48 8B C4                        mov rax, rsp
009E4083  48 89 58 08                     mov qword ptr [rax + 8], rbx
009E4087  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
009E408B  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
009E408F  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
009E4093  57                              push rdi
009E4094  41 54                           push r12
009E4096  41 55                           push r13
009E4098  41 56                           push r14
009E409A  41 57                           push r15
009E409C  48 83 EC 40                     sub rsp, 0x40
009E40A0  48 8B D9                        mov rbx, rcx
009E40A3  41 0F B6 F1                     movzx esi, r9b
009E40A7  33 C9                           xor ecx, ecx
009E40A9  C6 40 C8 00                     mov byte ptr [rax - 0x38], 0
009E40AD  45 8B F8                        mov r15d, r8d
009E40B0  4C 8B E2                        mov r12, rdx
009E40B3  E8 38 2B A8 FF                  call 0x140466bf0
009E40B8  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
009E40BD  45 33 C0                        xor r8d, r8d
009E40C0  49 8B D4                        mov rdx, r12
009E40C3  41 8B CF                        mov ecx, r15d
009E40C6  44 8A E8                        mov r13b, al
009E40C9  E8 22 37 91 FF                  call 0x1402f77f0
009E40CE  48 8B E8                        mov rbp, rax
009E40D1  48 85 C0                        test rax, rax
009E40D4  0F 84 6D 03 00 00               je 0x1409e4447
009E40DA  48 85 DB                        test rbx, rbx
009E40DD  0F 84 B6 00 00 00               je 0x1409e4199
009E40E3  8B 4B 04                        mov ecx, dword ptr [rbx + 4]
009E40E6  F6 C1 20                        test cl, 0x20
009E40E9  74 0F                           je 0x1409e40fa
009E40EB  40 84 F6                        test sil, sil
009E40EE  75 0A                           jne 0x1409e40fa
009E40F0  48 8B D0                        mov rdx, rax
009E40F3  33 C9                           xor ecx, ecx
009E40F5  E8 AE C0 DD FF                  call 0x1407c01a8
009E40FA  F7 03 04 C0 00 00               test dword ptr [rbx], 0xc004
009E4100  75 1A                           jne 0x1409e411c
009E4102  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
009E4105  A8 40                           test al, 0x40
009E4107  75 13                           jne 0x1409e411c
009E4109  8B 03                           mov eax, dword ptr [rbx]
009E410B  A8 01                           test al, 1
009E410D  75 0D                           jne 0x1409e411c
009E410F  A8 02                           test al, 2
009E4111  75 09                           jne 0x1409e411c
009E4113  F7 43 04 00 00 00 08            test dword ptr [rbx + 4], 0x8000000
009E411A  74 21                           je 0x1409e413d
009E411C  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
009E4123  44 8A C6                        mov r8b, sil
009E4126  4C 8B 8C 24 90 00 00 00         mov r9, qword ptr [rsp + 0x90]
009E412E  48 8B D5                        mov rdx, rbp
009E4131  48 8B CB                        mov rcx, rbx
009E4134  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009E4138  E8 2B 04 00 00                  call 0x1409e4568
009E413D  48 85 DB                        test rbx, rbx
009E4140  74 57                           je 0x1409e4199
009E4142  F7 03 00 00 02 00               test dword ptr [rbx], 0x20000
009E4148  74 0E                           je 0x1409e4158
009E414A  F7 43 08 00 00 00 01            test dword ptr [rbx + 8], 0x1000000
009E4151  75 0E                           jne 0x1409e4161
009E4153  45 33 C9                        xor r9d, r9d
009E4156  EB 0C                           jmp 0x1409e4164
009E4158  F7 43 08 00 00 00 01            test dword ptr [rbx + 8], 0x1000000
009E415F  74 1E                           je 0x1409e417f
009E4161  41 B1 01                        mov r9b, 1
009E4164  44 8B 03                        mov r8d, dword ptr [rbx]
009E4167  41 8B D7                        mov edx, r15d
009E416A  41 C1 E8 11                     shr r8d, 0x11
009E416E  49 8B CC                        mov rcx, r12
009E4171  41 80 E0 01                     and r8b, 1
009E4175  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
009E417A  E8 41 19 0A 00                  call 0x140a85ac0
009E417F  48 8D 7B 04                     lea rdi, [rbx + 4]
009E4183  8B 07                           mov eax, dword ptr [rdi]
009E4185  A8 02                           test al, 2
009E4187  74 14                           je 0x1409e419d
009E4189  41 B0 01                        mov r8b, 1
009E418C  40 8A D6                        mov dl, sil
009E418F  48 8B CD                        mov rcx, rbp
009E4192  E8 75 B4 09 00                  call 0x140a7f60c
009E4197  EB 09                           jmp 0x1409e41a2
009E4199  48 8D 7B 04                     lea rdi, [rbx + 4]
009E419D  48 85 DB                        test rbx, rbx
009E41A0  74 1C                           je 0x1409e41be
009E41A2  F7 07 00 04 00 00               test dword ptr [rdi], 0x400
009E41A8  74 14                           je 0x1409e41be
009E41AA  45 33 C0                        xor r8d, r8d
009E41AD  40 8A D6                        mov dl, sil
009E41B0  48 8B CD                        mov rcx, rbp
009E41B3  E8 54 B4 09 00                  call 0x140a7f60c
009E41B8  4C 8D 73 04                     lea r14, [rbx + 4]
009E41BC  EB 08                           jmp 0x1409e41c6
009E41BE  4C 8B F7                        mov r14, rdi
009E41C1  48 85 DB                        test rbx, rbx
009E41C4  74 19                           je 0x1409e41df
009E41C6  F7 07 00 00 01 00               test dword ptr [rdi], 0x10000
009E41CC  74 11                           je 0x1409e41df
009E41CE  40 8A D6                        mov dl, sil
009E41D1  48 8B CD                        mov rcx, rbp
009E41D4  E8 7B C9 DD FF                  call 0x1407c0b54
009E41D9  48 8D 7B 04                     lea rdi, [rbx + 4]
009E41DD  EB 08                           jmp 0x1409e41e7
009E41DF  49 8B FE                        mov rdi, r14
009E41E2  48 85 DB                        test rbx, rbx
009E41E5  74 1A                           je 0x1409e4201
009E41E7  41 F7 06 00 00 02 00            test dword ptr [r14], 0x20000
009E41EE  74 11                           je 0x1409e4201
009E41F0  40 8A D6                        mov dl, sil
009E41F3  48 8B CD                        mov rcx, rbp
009E41F6  E8 61 BE DD FF                  call 0x1407c005c
009E41FB  4C 8D 73 04                     lea r14, [rbx + 4]
009E41FF  EB 08                           jmp 0x1409e4209
009E4201  4C 8B F7                        mov r14, rdi
009E4204  48 85 DB                        test rbx, rbx
009E4207  74 69                           je 0x1409e4272
009E4209  F7 07 08 00 40 00               test dword ptr [rdi], 0x400008
009E420F  74 10                           je 0x1409e4221
009E4211  44 8B C6                        mov r8d, esi
009E4214  41 8B D7                        mov edx, r15d
009E4217  49 8B CC                        mov rcx, r12
009E421A  E8 91 4B DA FF                  call 0x140788db0
009E421F  EB 05                           jmp 0x1409e4226
009E4221  48 85 DB                        test rbx, rbx
009E4224  74 4C                           je 0x1409e4272
009E4226  41 F7 06 49 00 00 08            test dword ptr [r14], 0x8000049
009E422D  74 0D                           je 0x1409e423c
009E422F  40 8A D6                        mov dl, sil
009E4232  48 8B CD                        mov rcx, rbp
009E4235  E8 16 C4 DD FF                  call 0x1407c0650
009E423A  EB 05                           jmp 0x1409e4241
009E423C  48 85 DB                        test rbx, rbx
009E423F  74 31                           je 0x1409e4272
009E4241  F7 43 08 00 00 10 00            test dword ptr [rbx + 8], 0x100000
009E4248  74 0D                           je 0x1409e4257
009E424A  40 8A D6                        mov dl, sil
009E424D  48 8B CD                        mov rcx, rbp
009E4250  E8 8B BC DD FF                  call 0x1407bfee0
009E4255  EB 05                           jmp 0x1409e425c
009E4257  48 85 DB                        test rbx, rbx
009E425A  74 16                           je 0x1409e4272
009E425C  48 8D 7B 14                     lea rdi, [rbx + 0x14]
009E4260  F7 07 80 01 00 00               test dword ptr [rdi], 0x180
009E4266  74 0E                           je 0x1409e4276
009E4268  40 8A CE                        mov cl, sil
009E426B  E8 B8 F4 BD FF                  call 0x1405c3728
009E4270  EB 09                           jmp 0x1409e427b
009E4272  48 8D 7B 14                     lea rdi, [rbx + 0x14]
009E4276  48 85 DB                        test rbx, rbx
009E4279  74 46                           je 0x1409e42c1
009E427B  F7 07 00 20 00 00               test dword ptr [rdi], 0x2000
009E4281  74 0E                           je 0x1409e4291
009E4283  40 8A CE                        mov cl, sil
009E4286  E8 69 53 BE FF                  call 0x1405c95f4
009E428B  48 8D 7B 14                     lea rdi, [rbx + 0x14]
009E428F  EB 05                           jmp 0x1409e4296
009E4291  48 85 DB                        test rbx, rbx
009E4294  74 2B                           je 0x1409e42c1
009E4296  F7 43 04 00 10 00 00            test dword ptr [rbx + 4], 0x1000
009E429D  74 0A                           je 0x1409e42a9
009E429F  40 8A CE                        mov cl, sil
009E42A2  E8 F5 F4 BD FF                  call 0x1405c379c
009E42A7  EB 05                           jmp 0x1409e42ae
009E42A9  48 85 DB                        test rbx, rbx
009E42AC  74 13                           je 0x1409e42c1
009E42AE  F7 07 00 40 00 00               test dword ptr [rdi], 0x4000
009E42B4  74 0B                           je 0x1409e42c1
009E42B6  41 8B D7                        mov edx, r15d
009E42B9  49 8B CC                        mov rcx, r12
009E42BC  E8 5F 4A BE FF                  call 0x1405c8d20
009E42C1  48 8D 7B 04                     lea rdi, [rbx + 4]
009E42C5  40 84 F6                        test sil, sil
009E42C8  0F 85 22 01 00 00               jne 0x1409e43f0
009E42CE  48 85 DB                        test rbx, rbx
009E42D1  0F 84 E4 00 00 00               je 0x1409e43bb
009E42D7  F7 07 00 00 00 08               test dword ptr [rdi], 0x8000000
009E42DD  74 24                           je 0x1409e4303
009E42DF  41 8B D7                        mov edx, r15d
009E42E2  49 8B CC                        mov rcx, r12
009E42E5  E8 0A 51 E2 FF                  call 0x1408093f4
009E42EA  41 B8 85 02 00 00               mov r8d, 0x285
009E42F0  41 B9 01 00 00 00               mov r9d, 1
009E42F6  41 8B D7                        mov edx, r15d
009E42F9  49 8B CC                        mov rcx, r12
009E42FC  E8 5B 8D 0C 00                  call 0x140aad05c
009E4301  EB 09                           jmp 0x1409e430c
009E4303  48 85 DB                        test rbx, rbx
009E4306  0F 84 AF 00 00 00               je 0x1409e43bb
009E430C  8B 07                           mov eax, dword ptr [rdi]
009E430E  A8 09                           test al, 9
009E4310  75 07                           jne 0x1409e4319
009E4312  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
009E4315  A8 40                           test al, 0x40
009E4317  74 31                           je 0x1409e434a
009E4319  48 8B CD                        mov rcx, rbp
009E431C  E8 23 BE DD FF                  call 0x1407c0144
009E4321  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
009E4324  41 8B D7                        mov edx, r15d
009E4327  49 8B CC                        mov rcx, r12
009E432A  A8 40                           test al, 0x40
009E432C  74 0E                           je 0x1409e433c
009E432E  41 B8 8A 02 00 00               mov r8d, 0x28a
009E4334  41 B9 02 00 00 00               mov r9d, 2
009E433A  EB 09                           jmp 0x1409e4345
009E433C  41 B8 23 02 00 00               mov r8d, 0x223
009E4342  45 33 C9                        xor r9d, r9d
009E4345  E8 12 8D 0C 00                  call 0x140aad05c
009E434A  48 85 DB                        test rbx, rbx
009E434D  74 6C                           je 0x1409e43bb
009E434F  F7 43 04 00 00 08 00            test dword ptr [rbx + 4], 0x80000
009E4356  74 1B                           je 0x1409e4373
009E4358  45 33 C0                        xor r8d, r8d
009E435B  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
009E4363  49 8B CC                        mov rcx, r12
009E4366  E8 99 D9 F1 FF                  call 0x140901d04
009E436B  44 8B BC 24 80 00 00 00         mov r15d, dword ptr [rsp + 0x80]
009E4373  F7 03 00 02 00 00               test dword ptr [rbx], 0x200
009E4379  74 14                           je 0x1409e438f
009E437B  48 8B 8D 50 05 00 00            mov rcx, qword ptr [rbp + 0x550]
009E4382  41 8B D7                        mov edx, r15d
009E4385  48 8B 09                        mov rcx, qword ptr [rcx]
009E4388  E8 53 03 00 00                  call 0x1409e46e0
009E438D  EB 05                           jmp 0x1409e4394
009E438F  48 85 DB                        test rbx, rbx
009E4392  74 27                           je 0x1409e43bb
009E4394  48 8D 7B 10                     lea rdi, [rbx + 0x10]
009E4398  F7 07 00 80 00 00               test dword ptr [rdi], 0x8000
009E439E  74 1F                           je 0x1409e43bf
009E43A0  45 33 C9                        xor r9d, r9d
009E43A3  48 8D 15 26 DF AB FF            lea rdx, [rip - 0x5420da]
009E43AA  45 33 C0                        xor r8d, r8d
009E43AD  48 8D 0D 6C 2D 5E 00            lea rcx, [rip + 0x5e2d6c]
009E43B4  E8 7B 94 8F FF                  call 0x1402dd834
009E43B9  EB 09                           jmp 0x1409e43c4
009E43BB  48 8D 7B 10                     lea rdi, [rbx + 0x10]
009E43BF  48 85 DB                        test rbx, rbx
009E43C2  74 73                           je 0x1409e4437
009E43C4  8B 07                           mov eax, dword ptr [rdi]
009E43C6  A8 40                           test al, 0x40
009E43C8  75 04                           jne 0x1409e43ce
009E43CA  84 C0                           test al, al
009E43CC  79 0A                           jns 0x1409e43d8
009E43CE  33 D2                           xor edx, edx
009E43D0  48 8B CD                        mov rcx, rbp
009E43D3  E8 1C C1 DD FF                  call 0x1407c04f4
009E43D8  48 85 DB                        test rbx, rbx
009E43DB  74 5A                           je 0x1409e4437
009E43DD  F7 43 08 00 00 01 00            test dword ptr [rbx + 8], 0x10000
009E43E4  74 51                           je 0x1409e4437
009E43E6  48 8B CD                        mov rcx, rbp
009E43E9  E8 7A C4 DD FF                  call 0x1407c0868
009E43EE  EB 47                           jmp 0x1409e4437
009E43F0  48 85 DB                        test rbx, rbx
009E43F3  74 42                           je 0x1409e4437
009E43F5  F7 07 00 00 00 08               test dword ptr [rdi], 0x8000000
009E43FB  74 24                           je 0x1409e4421
009E43FD  41 B8 85 02 00 00               mov r8d, 0x285
009E4403  41 B9 01 00 00 00               mov r9d, 1
009E4409  41 8B D7                        mov edx, r15d
009E440C  49 8B CC                        mov rcx, r12
009E440F  E8 48 8C 0C 00                  call 0x140aad05c
009E4414  41 8B D7                        mov edx, r15d
009E4417  49 8B CC                        mov rcx, r12
009E441A  E8 D5 4F E2 FF                  call 0x1408093f4
009E441F  EB 05                           jmp 0x1409e4426
009E4421  48 85 DB                        test rbx, rbx
009E4424  74 11                           je 0x1409e4437
009E4426  8B 07                           mov eax, dword ptr [rdi]
009E4428  A8 20                           test al, 0x20
009E442A  74 0B                           je 0x1409e4437
009E442C  48 8B D5                        mov rdx, rbp
009E442F  40 8A CE                        mov cl, sil
009E4432  E8 71 BD DD FF                  call 0x1407c01a8
009E4437  44 8A 44 24 30                  mov r8b, byte ptr [rsp + 0x30]
009E443C  49 8B D4                        mov rdx, r12
009E443F  41 8B CF                        mov ecx, r15d
009E4442  E8 19 3C A3 FF                  call 0x140418060
009E4447  41 8A CD                        mov cl, r13b
009E444A  E8 A1 27 A8 FF                  call 0x140466bf0
009E444F  4C 8D 5C 24 40                  lea r11, [rsp + 0x40]
009E4454  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
009E4458  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
009E445C  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
009E4460  49 8B E3                        mov rsp, r11
009E4463  41 5F                           pop r15
009E4465  41 5E                           pop r14
009E4467  41 5D                           pop r13
009E4469  41 5C                           pop r12
009E446B  5F                              pop rdi
009E446C  C3                              ret
009E446D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpKernelTraceRundown(__int64 a1, __int64 a2, int a3, unsigned __int8 a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_p18;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (64);
    a1 = 0;
    *(unsigned __int8 *)(v_rsp - 56) = 0;
    result = IoSetThreadHardErrorMode(a1, a2, a3, a4);
    a3 = 0;
    result = EtwpOpenLogger((unsigned int)((unsigned int)((unsigned int)(a3))), a2, a3, v_stack_m38);
    if (result == 0) goto loc_009E4447;
    if (0 == 0) goto loc_009E4199;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (32)) == 0) goto loc_009E40FA;
    if (a4 == 0) {
        a2 = result;
        a1 = 0;
        result = EtwpLogRefSetAutoMark(a1, a2, a3, v_stack_m38);
    }
    if (((*(unsigned int *)(a1)) & (0xC004ULL)) != 0) goto loc_009E411C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 16)))) & (64)) != 0) goto loc_009E411C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (1)) != 0) goto loc_009E411C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) != 0) goto loc_009E411C;
    result = (unsigned int)(*(unsigned int *)(a1));
    if (((*(unsigned int *)(a1 + 4)) & (0x8000000ULL)) != 0) {
        result = a6;
        a3 = a4;
        a4 = a5;
        a2 = result;
        a1 = 0;
        v_stack_m48 = (unsigned int)(result);
        result = EtwpProcessThreadImageRundown(a1, a2, a3, a4);
    }
    if (a1 == 0) goto loc_009E4199;
    if (((*(unsigned int *)(a1)) & (0x20000ULL)) == 0) goto loc_009E4158;
    if (((*(unsigned int *)(a1 + 8)) & (0x1000000ULL)) != 0) goto loc_009E4161;
    a4 = 0;
    goto loc_009E4164;
loc_009E4158:
    if (((*(unsigned int *)(a1 + 8)) & (0x1000000ULL)) == 0) goto loc_009E417F;
loc_009E4161:
loc_009E4164:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) >> (17));
    a3 = (unsigned __int8)((a3) & (1));
    v_stack_m48 = 0;
    result = CmEtwRunDown(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a3, 1);
loc_009E417F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (2)) == 0) goto loc_009E419D;
    result = EtwpSampledProfileRunDown(result, 0, 1, 1);
    goto loc_009E41A2;
loc_009E4199:
loc_009E419D:
    if (a1 == 0) goto loc_009E41BE;
loc_009E41A2:
    if (((*(unsigned int *)(a1 + 4)) & (0x400ULL)) == 0) goto loc_009E41BE;
    a3 = 0;
    result = EtwpSampledProfileRunDown(result, 0, a3, 1);
    goto loc_009E41C6;
loc_009E41BE:
    if (a1 == 0) goto loc_009E41DF;
loc_009E41C6:
    if (((*(unsigned int *)(a1 + 4)) & (0x10000ULL)) == 0) goto loc_009E41DF;
    result = EtwpSpinLockConfigRunDown(result, 0, a3, 1);
    goto loc_009E41E7;
loc_009E41DF:
    if (a1 == 0) goto loc_009E4201;
loc_009E41E7:
    if (((*(unsigned int *)(a1 + 4)) & (0x20000ULL)) == 0) goto loc_009E4201;
    result = EtwpExecutiveResourceConfigRunDown(result, 0, a3, 1);
    goto loc_009E4209;
loc_009E4201:
    if (a1 == 0) goto loc_009E4272;
loc_009E4209:
    if (((*(unsigned int *)(a1 + 4)) & (0x400008ULL)) == 0) goto loc_009E4221;
    result = PsPerfLogSessionRundown(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), 0, 1);
    goto loc_009E4226;
loc_009E4221:
    if (a1 == 0) goto loc_009E4272;
loc_009E4226:
    if (((*(unsigned int *)(a1 + 4)) & (0x8000049ULL)) == 0) goto loc_009E423C;
    result = EtwpPoolRunDown(result, 0, 0, 1);
    goto loc_009E4241;
loc_009E423C:
    if (a1 == 0) goto loc_009E4272;
loc_009E4241:
    if (((*(unsigned int *)(a1 + 8)) & (0x100000ULL)) == 0) goto loc_009E4257;
    result = EtwpClockSourceRunDown(result, 0, 0, 1);
    goto loc_009E425C;
loc_009E4257:
    if (a1 == 0) goto loc_009E4272;
loc_009E425C:
    if (((*(unsigned int *)(a1 + 20)) & (384)) == 0) goto loc_009E4276;
    result = KeTraceHgsPlusRundown(0, 0, 0, 1);
    goto loc_009E427B;
loc_009E4272:
loc_009E4276:
    if (a1 == 0) goto loc_009E42C1;
loc_009E427B:
    if (((*(unsigned int *)(a1 + 20)) & (0x2000ULL)) == 0) goto loc_009E4291;
    result = KeTraceParkingRundown(0, 0, 0, 1);
    goto loc_009E4296;
loc_009E4291:
    if (a1 == 0) goto loc_009E42C1;
loc_009E4296:
    if (((*(unsigned int *)(a1 + 4)) & (0x1000ULL)) == 0) goto loc_009E42A9;
    result = KeTraceThreadAffinityRundown(0, 0, 0, 1);
    goto loc_009E42AE;
loc_009E42A9:
    if (a1 == 0) goto loc_009E42C1;
loc_009E42AE:
    if (((*(unsigned int *)(a1 + 20)) & (0x4000ULL)) != 0) {
        a2 = (unsigned int)((unsigned int)(a3));
        a1 = a2;
        result = KeTraceSchedulingGroupRundown(a1, a2, 0, 1);
    }
    if (0 != 0) goto loc_009E43F0;
    if (a1 == 0) goto loc_009E43BB;
    if (((*(unsigned int *)(a1 + 4)) & (0x8000000ULL)) == 0) goto loc_009E4303;
    result = MmLogSystemShareablePfnInfo(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), 0, 1);
    result = MmIdentifyPhysicalMemory(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), 645, 1);
    goto loc_009E430C;
loc_009E4303:
    if (a1 == 0) goto loc_009E43BB;
loc_009E430C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (9)) != 0) goto loc_009E4319;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 20)))) & (64)) == 0) goto loc_009E434A;
loc_009E4319:
    result = EtwpLogMemInfoRundown(result, (unsigned int)((unsigned int)((unsigned int)(a3))), 645, 1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 20)))) & (64)) == 0) goto loc_009E433C;
    goto loc_009E4345;
loc_009E433C:
    a4 = 0;
loc_009E4345:
    result = MmIdentifyPhysicalMemory(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), 547, a4);
loc_009E434A:
    if (a1 == 0) goto loc_009E43BB;
    v_r15 = (unsigned int)(a3);
    if (((*(unsigned int *)(a1 + 4)) & (0x80000ULL)) != 0) {
        a3 = 0;
        a2 = v_stack_p18;
        a1 = a2;
        result = MmLogQueryCombineStats(a1, a2, a3, a4);
        v_r15 = v_stack_p18;
    }
    if (((*(unsigned int *)(a1)) & (512)) == 0) goto loc_009E438F;
    result = WmiTraceRundownNotify(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1360)), (unsigned int)((unsigned int)(v_r15)), a3, a4);
    goto loc_009E4394;
loc_009E438F:
    if (a1 == 0) goto loc_009E43BB;
loc_009E4394:
    if (((*(unsigned int *)(a1 + 16)) & (0x8000ULL)) == 0) goto loc_009E43BF;
    a4 = 0;
    a3 = 0;
    result = PopExecuteOnTargetProcessors(v_rip + 6172012, v_rip - 5513434, a3, a4);
    goto loc_009E43C4;
loc_009E43BB:
loc_009E43BF:
    if (a1 == 0) goto loc_009E4437;
loc_009E43C4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 16)))) & (64)) != 0) goto loc_009E43CE;
    result = (unsigned int)(*(unsigned int *)(a1 + 16));
    if (sign_flag) {
        a2 = 0;
        a1 = result;
        result = EtwpObjectTypeRundown(a1, a2, a3, a4);
    }
    if (a1 == 0) goto loc_009E4437;
    if (((*(unsigned int *)(a1 + 8)) & (0x10000ULL)) == 0) goto loc_009E4437;
    result = EtwpProcessorRundown(result, a2, a3, a4);
    goto loc_009E4437;
loc_009E43F0:
    if (a1 == 0) goto loc_009E4437;
    if (((*(unsigned int *)(a1 + 16)) & (0x8000000ULL)) == 0) goto loc_009E4421;
    result = MmIdentifyPhysicalMemory(0, (unsigned int)((unsigned int)(v_r15)), 645, 1);
    result = MmLogSystemShareablePfnInfo(0, (unsigned int)((unsigned int)(v_r15)), 645, 1);
    goto loc_009E4426;
loc_009E4421:
    if (a1 == 0) goto loc_009E4437;
loc_009E4426:
    result = (unsigned int)(*(unsigned int *)(a1 + 16));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 16)))) & (32)) != 0) {
        a2 = result;
        a1 = 0;
        result = EtwpLogRefSetAutoMark(a1, a2, 645, 1);
    }
    result = EtwpCloseLogger((unsigned int)((unsigned int)(v_r15)), a2, v_stack_m38, 1);
loc_009E4447:
    result = IoSetThreadHardErrorMode((unsigned __int8)((unsigned __int8)(result)), a2, v_stack_m38, 1);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpKernelTraceRundown(int64_t Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4, int64_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_m48;
    uint64_t v_stack_p18;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (64);
    Arg1 = 0;
    *(uint8_t *)(local_rsp - 0x38) = 0;
    result = IoSetThreadHardErrorMode(Arg1, Arg2, Arg3, Arg4);
    Arg3 = 0;
    result = EtwpOpenLogger((uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg2, Arg3, v_stack_m38);
    if (result == 0) goto loc_009E4447;
    if (0 == 0) goto loc_009E4199;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x4)))) & (32)) == 0) goto loc_009E40FA;
    if (Arg4 == 0) {
        Arg2 = result;
        Arg1 = 0;
        result = EtwpLogRefSetAutoMark(Arg1, Arg2, Arg3, v_stack_m38);
    }
    if (((*(uint32_t *)(Arg1)) & (0xC004ULL)) != 0) goto loc_009E411C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)))) & (64)) != 0) goto loc_009E411C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1)))) & (1)) != 0) goto loc_009E411C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1)))) & (2)) != 0) goto loc_009E411C;
    result = (uint32_t)(*(uint32_t *)(Arg1));
    if (((*(uint32_t *)(Arg1 + 0x4)) & (0x8000000ULL)) != 0) {
        result = Arg6;
        Arg3 = Arg4;
        Arg4 = Arg5;
        Arg2 = result;
        Arg1 = 0;
        v_stack_m48 = (uint32_t)(result);
        result = EtwpProcessThreadImageRundown(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg1 == 0) goto loc_009E4199;
    if (((*(uint32_t *)(Arg1)) & (0x20000ULL)) == 0) goto loc_009E4158;
    if (((*(uint32_t *)(Arg1 + 0x8)) & (0x1000000ULL)) != 0) goto loc_009E4161;
    Arg4 = 0;
    goto loc_009E4164;
loc_009E4158:
    if (((*(uint32_t *)(Arg1 + 0x8)) & (0x1000000ULL)) == 0) goto loc_009E417F;
loc_009E4161:
loc_009E4164:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1))) >> (17));
    Arg3 = (uint8_t)((Arg3) & (1));
    v_stack_m48 = 0;
    result = CmEtwRunDown(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg3, 1);
loc_009E417F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x4)))) & (2)) == 0) goto loc_009E419D;
    result = EtwpSampledProfileRunDown(result, 0, 1, 1);
    goto loc_009E41A2;
loc_009E4199:
loc_009E419D:
    if (Arg1 == 0) goto loc_009E41BE;
loc_009E41A2:
    if (((*(uint32_t *)(Arg1 + 0x4)) & (0x400ULL)) == 0) goto loc_009E41BE;
    Arg3 = 0;
    result = EtwpSampledProfileRunDown(result, 0, Arg3, 1);
    goto loc_009E41C6;
loc_009E41BE:
    if (Arg1 == 0) goto loc_009E41DF;
loc_009E41C6:
    if (((*(uint32_t *)(Arg1 + 0x4)) & (0x10000ULL)) == 0) goto loc_009E41DF;
    result = EtwpSpinLockConfigRunDown(result, 0, Arg3, 1);
    goto loc_009E41E7;
loc_009E41DF:
    if (Arg1 == 0) goto loc_009E4201;
loc_009E41E7:
    if (((*(uint32_t *)(Arg1 + 0x4)) & (0x20000ULL)) == 0) goto loc_009E4201;
    result = EtwpExecutiveResourceConfigRunDown(result, 0, Arg3, 1);
    goto loc_009E4209;
loc_009E4201:
    if (Arg1 == 0) goto loc_009E4272;
loc_009E4209:
    if (((*(uint32_t *)(Arg1 + 0x4)) & (0x400008ULL)) == 0) goto loc_009E4221;
    result = PsPerfLogSessionRundown(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), 0, 1);
    goto loc_009E4226;
loc_009E4221:
    if (Arg1 == 0) goto loc_009E4272;
loc_009E4226:
    if (((*(uint32_t *)(Arg1 + 0x4)) & (0x8000049ULL)) == 0) goto loc_009E423C;
    result = EtwpPoolRunDown(result, 0, 0, 1);
    goto loc_009E4241;
loc_009E423C:
    if (Arg1 == 0) goto loc_009E4272;
loc_009E4241:
    if (((*(uint32_t *)(Arg1 + 0x8)) & (0x100000ULL)) == 0) goto loc_009E4257;
    result = EtwpClockSourceRunDown(result, 0, 0, 1);
    goto loc_009E425C;
loc_009E4257:
    if (Arg1 == 0) goto loc_009E4272;
loc_009E425C:
    if (((*(uint32_t *)(Arg1 + 0x14)) & (384)) == 0) goto loc_009E4276;
    result = KeTraceHgsPlusRundown(0, 0, 0, 1);
    goto loc_009E427B;
loc_009E4272:
loc_009E4276:
    if (Arg1 == 0) goto loc_009E42C1;
loc_009E427B:
    if (((*(uint32_t *)(Arg1 + 0x14)) & (0x2000ULL)) == 0) goto loc_009E4291;
    result = KeTraceParkingRundown(0, 0, 0, 1);
    goto loc_009E4296;
loc_009E4291:
    if (Arg1 == 0) goto loc_009E42C1;
loc_009E4296:
    if (((*(uint32_t *)(Arg1 + 0x4)) & (0x1000ULL)) == 0) goto loc_009E42A9;
    result = KeTraceThreadAffinityRundown(0, 0, 0, 1);
    goto loc_009E42AE;
loc_009E42A9:
    if (Arg1 == 0) goto loc_009E42C1;
loc_009E42AE:
    if (((*(uint32_t *)(Arg1 + 0x14)) & (0x4000ULL)) != 0) {
        Arg2 = (uint32_t)((uint32_t)(Arg3));
        Arg1 = Arg2;
        result = KeTraceSchedulingGroupRundown(Arg1, Arg2, 0, 1);
    }
    if (0 != 0) goto loc_009E43F0;
    if (Arg1 == 0) goto loc_009E43BB;
    if (((*(uint32_t *)(Arg1 + 0x4)) & (0x8000000ULL)) == 0) goto loc_009E4303;
    result = MmLogSystemShareablePfnInfo(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), 0, 1);
    result = MmIdentifyPhysicalMemory(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), 645, 1);
    goto loc_009E430C;
loc_009E4303:
    if (Arg1 == 0) goto loc_009E43BB;
loc_009E430C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x4)))) & (9)) != 0) goto loc_009E4319;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x14)))) & (64)) == 0) goto loc_009E434A;
loc_009E4319:
    result = EtwpLogMemInfoRundown(result, (uint32_t)((uint32_t)((uint32_t)(Arg3))), 645, 1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x14)))) & (64)) == 0) goto loc_009E433C;
    goto loc_009E4345;
loc_009E433C:
    Arg4 = 0;
loc_009E4345:
    result = MmIdentifyPhysicalMemory(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), 547, Arg4);
loc_009E434A:
    if (Arg1 == 0) goto loc_009E43BB;
    local_r15 = (uint32_t)(Arg3);
    if (((*(uint32_t *)(Arg1 + 0x4)) & (0x80000ULL)) != 0) {
        Arg3 = 0;
        Arg2 = v_stack_p18;
        Arg1 = Arg2;
        result = MmLogQueryCombineStats(Arg1, Arg2, Arg3, Arg4);
        local_r15 = v_stack_p18;
    }
    if (((*(uint32_t *)(Arg1)) & (512)) == 0) goto loc_009E438F;
    result = WmiTraceRundownNotify(*(uint64_t *)(*(uint64_t *)(result + 0x550)), (uint32_t)((uint32_t)(local_r15)), Arg3, Arg4);
    goto loc_009E4394;
loc_009E438F:
    if (Arg1 == 0) goto loc_009E43BB;
loc_009E4394:
    if (((*(uint32_t *)(Arg1 + 0x10)) & (0x8000ULL)) == 0) goto loc_009E43BF;
    Arg4 = 0;
    Arg3 = 0;
    result = PopExecuteOnTargetProcessors(v_rip + 6172012, v_rip - 5513434, Arg3, Arg4);
    goto loc_009E43C4;
loc_009E43BB:
loc_009E43BF:
    if (Arg1 == 0) goto loc_009E4437;
loc_009E43C4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)))) & (64)) != 0) goto loc_009E43CE;
    result = (uint32_t)(*(uint32_t *)(Arg1 + 0x10));
    if (sign_flag) {
        Arg2 = 0;
        Arg1 = result;
        result = EtwpObjectTypeRundown(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg1 == 0) goto loc_009E4437;
    if (((*(uint32_t *)(Arg1 + 0x8)) & (0x10000ULL)) == 0) goto loc_009E4437;
    result = EtwpProcessorRundown(result, Arg2, Arg3, Arg4);
    goto loc_009E4437;
loc_009E43F0:
    if (Arg1 == 0) goto loc_009E4437;
    if (((*(uint32_t *)(Arg1 + 0x10)) & (0x8000000ULL)) == 0) goto loc_009E4421;
    result = MmIdentifyPhysicalMemory(0, (uint32_t)((uint32_t)(local_r15)), 645, 1);
    result = MmLogSystemShareablePfnInfo(0, (uint32_t)((uint32_t)(local_r15)), 645, 1);
    goto loc_009E4426;
loc_009E4421:
    if (Arg1 == 0) goto loc_009E4437;
loc_009E4426:
    result = (uint32_t)(*(uint32_t *)(Arg1 + 0x10));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)))) & (32)) != 0) {
        Arg2 = result;
        Arg1 = 0;
        result = EtwpLogRefSetAutoMark(Arg1, Arg2, 645, 1);
    }
    result = EtwpCloseLogger((uint32_t)((uint32_t)(local_r15)), Arg2, v_stack_m38, 1);
loc_009E4447:
    result = IoSetThreadHardErrorMode((uint8_t)((uint8_t)(result)), Arg2, v_stack_m38, 1);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009E4080&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
