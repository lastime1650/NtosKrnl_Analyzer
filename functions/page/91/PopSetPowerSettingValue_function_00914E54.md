# PopSetPowerSettingValue

- RVA: `0x00914E54`–`0x00915293` (길이 `1,087` bytes)
- VA: `0x0000000140914E54`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A694`
- 디코드: `284`개 명령, `1,087/1,087` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00914E9C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00914EB4` → [PopIncrementPowerSettingPendingUpdates](../../text/38/PopIncrementPowerSettingPendingUpdates_function_0038FE38.md) (function, `0x0038FE38`)
- `0x00914EC7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00914ED5` → [PopValidatePowerSettingData](PopValidatePowerSettingData_function_00915368.md) (function, `0x00915368`)
- `0x00914EDD` → [PopStateIsSessionSpecific](PopStateIsSessionSpecific_function_0091529C.md) (function, `0x0091529C`)
- `0x00914EED` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x00914EF7` → [PopFindPowerSettingConfiguration](PopFindPowerSettingConfiguration_function_009152E0.md) (function, `0x009152E0`)
- `0x00914F3C` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x00914F64` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00914F7C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00914F9D` → [PopIncrementPowerSettingPendingUpdates](../../text/38/PopIncrementPowerSettingPendingUpdates_function_0038FE38.md) (function, `0x0038FE38`)
- `0x00914FA7` → [PopSetNotificationWork](../../text/48/PopSetNotificationWork_function_00482C78.md) (function, `0x00482C78`)
- `0x00914FB6` → [PopSetNotificationWork](../../text/48/PopSetNotificationWork_function_00482C78.md) (function, `0x00482C78`)
- `0x00914FBD` → [PopDecrementPowerSettingPendingUpdates](../../text/39/PopDecrementPowerSettingPendingUpdates_function_0039007C.md) (function, `0x0039007C`)
- `0x0091500F` → [PopArePowerSettingsEqual](PopArePowerSettingsEqual_function_0091606C.md) (function, `0x0091606C`)
- `0x0091505E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00915097` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009150A9` → [PopUnreferencePowerSetting](PopUnreferencePowerSetting_function_009164A4.md) (function, `0x009164A4`)
- `0x00915146` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00915170` → [PopGetListHead](PopGetListHead_function_00914DE4.md) (function, `0x00914DE4`)
- `0x00915261` → [PoRegisterPowerSettingCallback](../A8/PoRegisterPowerSettingCallback_function_00A82150.md) (function, `0x00A82150`)
- `0x00915289` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)

### Direct callers
- [PopInitilizeAcDcSettings](../../text/48/PopInitilizeAcDcSettings_function_004828D0.md) at `0x004828FA`
- [PopInitilizeAcDcSettings](../../text/48/PopInitilizeAcDcSettings_function_004828D0.md) at `0x00482922`
- [PopScanIdleList](../../text/49/PopScanIdleList_function_00497F04.md) at `0x004982B9`
- [PopSetSessionDisplayStatus](PopSetSessionDisplayStatus_function_00912E7C.md) at `0x00912EF1`
- [PopSetSessionDisplayStatus](PopSetSessionDisplayStatus_function_00912E7C.md) at `0x00912F10`
- [PopAdaptiveGetConsoleSessionState](PopAdaptiveGetConsoleSessionState_function_00913FB4.md) at `0x00914164`
- [PopAdaptiveGetConsoleSessionState](PopAdaptiveGetConsoleSessionState_function_00913FB4.md) at `0x00914183`
- [PopSetSessionUserStatus](PopSetSessionUserStatus_function_00914BB8.md) at `0x00914C28`
- [PopSetSessionUserStatus](PopSetSessionUserStatus_function_00914BB8.md) at `0x00914C4A`
- [PopSetNewPolicyValue](PopSetNewPolicyValue_function_00914C6C.md) at `0x00914D3C`
- [PopSetPowerSettingValueAcDc](PopSetPowerSettingValueAcDc_function_00914D6C.md) at `0x00914D95`
- [PopSetPowerSettingValueAcDc](PopSetPowerSettingValueAcDc_function_00914D6C.md) at `0x00914DB5`
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x00956AA4`
- [PopUpdateConsoleDisplayState](../A3/PopUpdateConsoleDisplayState_function_00A31298.md) at `0x00A312FB`
- [PopUpdateConsoleDisplayState](../A3/PopUpdateConsoleDisplayState_function_00A31298.md) at `0x00A3131B`
- [PopUpdateConsoleDisplayState](../A3/PopUpdateConsoleDisplayState_function_00A31298.md) at `0x00A31350`
- [PopUpdateConsoleDisplayState](../A3/PopUpdateConsoleDisplayState_function_00A31298.md) at `0x00A31370`
- [PopPdcIdleResiliencyCallback](../A3/PopPdcIdleResiliencyCallback_function_00A31518.md) at `0x00A3155B`
- [PopPdcIdleResiliencyCallback](../A3/PopPdcIdleResiliencyCallback_function_00A31518.md) at `0x00A3157B`
- [PopNotifyLidStateChange](../AC/PopNotifyLidStateChange_function_00AC34A8.md) at `0x00AC350B`
- [PopNotifyLidStateChange](../AC/PopNotifyLidStateChange_function_00AC34A8.md) at `0x00AC352D`

### Static image references
- `0x00914EE2` → RVA `0x00F0DF40` (`.data`; read)
- `0x00914F81` → RVA `0x00F0CA60` (`.data`; read)
- `0x0091507B` → RVA `0x00E676E0` (`.data`; read/write)
- `0x009150C3` → RVA `0x00F0CE0C` (`.data`; read)
- `0x0091518A` → RVA `0x00F0C6E0` (`.data`; read)
- `0x00915215` → RVA `0x00E676D8` (`.data`; read)
- `0x00915222` → RVA `0x00E676DC` (`.data`; read)
- `0x00915250` → RVA `0x00A39340` (`PopTracePowerSettingChange`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x00914E9C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00914EB4` → [PopIncrementPowerSettingPendingUpdates](../../text/38/PopIncrementPowerSettingPendingUpdates_function_0038FE38.md) (`PAGE` → `.text`)
  - `0x00914EC7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00914EED` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (`PAGE` → `.text`)
  - `0x00914F3C` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x00914F64` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
  - `0x00914F7C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00914F9D` → [PopIncrementPowerSettingPendingUpdates](../../text/38/PopIncrementPowerSettingPendingUpdates_function_0038FE38.md) (`PAGE` → `.text`)
  - `0x00914FA7` → [PopSetNotificationWork](../../text/48/PopSetNotificationWork_function_00482C78.md) (`PAGE` → `.text`)
  - `0x00914FB6` → [PopSetNotificationWork](../../text/48/PopSetNotificationWork_function_00482C78.md) (`PAGE` → `.text`)
  - `0x00914FBD` → [PopDecrementPowerSettingPendingUpdates](../../text/39/PopDecrementPowerSettingPendingUpdates_function_0039007C.md) (`PAGE` → `.text`)
  - `0x0091505E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00915097` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00915146` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00915289` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00914E54  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00914E59  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00914E5E  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00914E63  55                              push rbp
00914E64  56                              push rsi
00914E65  57                              push rdi
00914E66  41 54                           push r12
00914E68  41 55                           push r13
00914E6A  41 56                           push r14
00914E6C  41 57                           push r15
00914E6E  48 83 EC 70                     sub rsp, 0x70
00914E72  33 C0                           xor eax, eax
00914E74  45 8B E9                        mov r13d, r9d
00914E77  40 8A E8                        mov bpl, al
00914E7A  88 44 24 41                     mov byte ptr [rsp + 0x41], al
00914E7E  8B F2                           mov esi, edx
00914E80  89 6C 24 44                     mov dword ptr [rsp + 0x44], ebp
00914E84  48 8B D9                        mov rbx, rcx
00914E87  41 8B D1                        mov edx, r9d
00914E8A  41 B8 50 53 65 74               mov r8d, 0x74655350
00914E90  88 44 24 42                     mov byte ptr [rsp + 0x42], al
00914E94  B9 00 01 00 00                  mov ecx, 0x100
00914E99  44 8B F0                        mov r14d, eax
00914E9C  E8 4F D2 26 00                  call 0x140b820f0
00914EA1  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00914EA6  4C 8B E0                        mov r12, rax
00914EA9  48 85 C0                        test rax, rax
00914EAC  0F 84 2B 01 00 00               je 0x140914fdd
00914EB2  33 C9                           xor ecx, ecx
00914EB4  E8 7F AF A7 FF                  call 0x14038fe38
00914EB9  48 8B 94 24 D0 00 00 00         mov rdx, qword ptr [rsp + 0xd0]
00914EC1  45 8B C5                        mov r8d, r13d
00914EC4  49 8B CC                        mov rcx, r12
00914EC7  E8 74 19 DB FF                  call 0x1406c6840
00914ECC  4D 8B C4                        mov r8, r12
00914ECF  41 8B D5                        mov edx, r13d
00914ED2  48 8B CB                        mov rcx, rbx
00914ED5  E8 8E 04 00 00                  call 0x140915368
00914EDA  48 8B CB                        mov rcx, rbx
00914EDD  E8 BA 03 00 00                  call 0x14091529c
00914EE2  48 8D 0D 57 90 5F 00            lea rcx, [rip + 0x5f9057]
00914EE9  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00914EED  E8 AE 96 8F FF                  call 0x14020e5a0
00914EF2  8B D6                           mov edx, esi
00914EF4  48 8B CB                        mov rcx, rbx
00914EF7  E8 E4 03 00 00                  call 0x1409152e0
00914EFC  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00914F01  48 8B D8                        mov rbx, rax
00914F04  48 85 C0                        test rax, rax
00914F07  0F 84 29 02 00 00               je 0x140915136
00914F0D  48 63 84 24 C0 00 00 00         movsxd rax, dword ptr [rsp + 0xc0]
00914F15  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00914F1A  48 8B 6C C3 40                  mov rbp, qword ptr [rbx + rax*8 + 0x40]
00914F1F  48 85 ED                        test rbp, rbp
00914F22  0F 84 C1 00 00 00               je 0x140914fe9
00914F28  44 39 6D 04                     cmp dword ptr [rbp + 4], r13d
00914F2C  0F 85 B7 00 00 00               jne 0x140914fe9
00914F32  48 8D 4D 0C                     lea rcx, [rbp + 0xc]
00914F36  4D 8B C5                        mov r8, r13
00914F39  49 8B D4                        mov rdx, r12
00914F3C  E8 2F 57 DA FF                  call 0x1406ba670
00914F41  49 3B C5                        cmp rax, r13
00914F44  0F 85 9A 00 00 00               jne 0x140914fe4
00914F4A  8B 6C 24 44                     mov ebp, dword ptr [rsp + 0x44]
00914F4E  45 33 FF                        xor r15d, r15d
00914F51  41 8B FF                        mov edi, r15d
00914F54  41 8A F7                        mov sil, r15b
00914F57  41 BE 01 00 00 00               mov r14d, 1
00914F5D  48 8D 0D DC 8F 5F 00            lea rcx, [rip + 0x5f8fdc]
00914F64  E8 57 CA 93 FF                  call 0x1402519c0
00914F69  44 38 7C 24 41                  cmp byte ptr [rsp + 0x41], r15b
00914F6E  0F 85 D4 02 00 00               jne 0x140915248
00914F74  BA 50 53 65 74                  mov edx, 0x74655350
00914F79  49 8B CC                        mov rcx, r12
00914F7C  E8 EF D8 26 00                  call 0x140b82870
00914F81  83 3D D8 7A 5F 00 03            cmp dword ptr [rip + 0x5f7ad8], 3
00914F88  72 31                           jb 0x140914fbb
00914F8A  44 38 7C 24 42                  cmp byte ptr [rsp + 0x42], r15b
00914F8F  0F 85 D6 02 00 00               jne 0x14091526b
00914F95  40 84 ED                        test bpl, bpl
00914F98  74 12                           je 0x140914fac
00914F9A  41 8A CE                        mov cl, r14b
00914F9D  E8 96 AE A7 FF                  call 0x14038fe38
00914FA2  B9 20 00 00 00                  mov ecx, 0x20
00914FA7  E8 CC DC B6 FF                  call 0x140482c78
00914FAC  40 84 F6                        test sil, sil
00914FAF  74 0A                           je 0x140914fbb
00914FB1  B9 80 00 00 00                  mov ecx, 0x80
00914FB6  E8 BD DC B6 FF                  call 0x140482c78
00914FBB  33 C9                           xor ecx, ecx
00914FBD  E8 BA B0 A7 FF                  call 0x14039007c
00914FC2  8B C7                           mov eax, edi
00914FC4  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
00914FCC  48 83 C4 70                     add rsp, 0x70
00914FD0  41 5F                           pop r15
00914FD2  41 5E                           pop r14
00914FD4  41 5D                           pop r13
00914FD6  41 5C                           pop r12
00914FD8  5F                              pop rdi
00914FD9  5E                              pop rsi
00914FDA  5D                              pop rbp
00914FDB  C3                              ret
00914FDC  CC                              int3
00914FDD  B8 9A 00 00 C0                  mov eax, 0xc000009a
00914FE2  EB E0                           jmp 0x140914fc4
00914FE4  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00914FE9  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00914FEE  48 8D 73 40                     lea rsi, [rbx + 0x40]
00914FF2  45 32 E4                        xor r12b, r12b
00914FF5  45 33 FF                        xor r15d, r15d
00914FF8  41 8D 5F 01                     lea ebx, [r15 + 1]
00914FFC  4C 3B F8                        cmp r15, rax
00914FFF  74 2D                           je 0x14091502e
00915001  4D 85 F6                        test r14, r14
00915004  75 1D                           jne 0x140915023
00915006  48 8B 0E                        mov rcx, qword ptr [rsi]
00915009  45 8B C5                        mov r8d, r13d
0091500C  48 8B D7                        mov rdx, rdi
0091500F  E8 58 10 00 00                  call 0x14091606c
00915014  84 C0                           test al, al
00915016  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0091501B  74 06                           je 0x140915023
0091501D  4C 8B 36                        mov r14, qword ptr [rsi]
00915020  41 01 1E                        add dword ptr [r14], ebx
00915023  48 39 2E                        cmp qword ptr [rsi], rbp
00915026  45 0F B6 E4                     movzx r12d, r12b
0091502A  44 0F 44 E3                     cmove r12d, ebx
0091502E  4C 03 FB                        add r15, rbx
00915031  48 83 C6 08                     add rsi, 8
00915035  49 83 FF 03                     cmp r15, 3
00915039  7C C1                           jl 0x140914ffc
0091503B  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00915040  45 33 FF                        xor r15d, r15d
00915043  41 8B FF                        mov edi, r15d
00915046  4D 85 F6                        test r14, r14
00915049  0F 85 C5 00 00 00               jne 0x140915114
0091504F  41 8D 55 0C                     lea edx, [r13 + 0xc]
00915053  B9 00 01 00 00                  mov ecx, 0x100
00915058  41 B8 50 53 65 74               mov r8d, 0x74655350
0091505E  E8 8D D0 26 00                  call 0x140b820f0
00915063  4C 8B F0                        mov r14, rax
00915066  48 85 C0                        test rax, rax
00915069  0F 84 AC 00 00 00               je 0x14091511b
0091506F  41 8D 77 01                     lea esi, [r15 + 1]
00915073  44 89 68 04                     mov dword ptr [rax + 4], r13d
00915077  89 30                           mov dword ptr [rax], esi
00915079  8B C6                           mov eax, esi
0091507B  F0 0F C1 05 5D 26 55 00         lock xadd dword ptr [rip + 0x55265d], eax
00915083  03 C6                           add eax, esi
00915085  74 F2                           je 0x140915079
00915087  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0091508C  49 8D 4E 0C                     lea rcx, [r14 + 0xc]
00915090  4D 8B C5                        mov r8, r13
00915093  41 89 46 08                     mov dword ptr [r14 + 8], eax
00915097  E8 A4 17 DB FF                  call 0x1406c6840
0091509C  48 85 ED                        test rbp, rbp
0091509F  74 0D                           je 0x1409150ae
009150A1  45 84 E4                        test r12b, r12b
009150A4  74 45                           je 0x1409150eb
009150A6  48 8B CD                        mov rcx, rbp
009150A9  E8 F6 13 00 00                  call 0x1409164a4
009150AE  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009150B3  8B 6C 24 44                     mov ebp, dword ptr [rsp + 0x44]
009150B7  4C 89 74 C3 40                  mov qword ptr [rbx + rax*8 + 0x40], r14
009150BC  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
009150C3  39 05 43 7D 5F 00               cmp dword ptr [rip + 0x5f7d43], eax
009150C9  74 3B                           je 0x140915106
009150CB  44 39 7B 38                     cmp dword ptr [rbx + 0x38], r15d
009150CF  75 06                           jne 0x1409150d7
009150D1  44 39 7B 3C                     cmp dword ptr [rbx + 0x3c], r15d
009150D5  74 5A                           je 0x140915131
009150D7  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
009150DC  41 BE 01 00 00 00               mov r14d, 1
009150E2  44 09 73 34                     or dword ptr [rbx + 0x34], r14d
009150E6  E9 72 FE FF FF                  jmp 0x140914f5d
009150EB  48 8D 53 10                     lea rdx, [rbx + 0x10]
009150EF  48 8B 02                        mov rax, qword ptr [rdx]
009150F2  48 3B C2                        cmp rax, rdx
009150F5  74 AF                           je 0x1409150a6
009150F7  48 39 68 48                     cmp qword ptr [rax + 0x48], rbp
009150FB  75 04                           jne 0x140915101
009150FD  4C 89 78 48                     mov qword ptr [rax + 0x48], r15
00915101  48 8B 00                        mov rax, qword ptr [rax]
00915104  EB EC                           jmp 0x1409150f2
00915106  44 38 7C 24 40                  cmp byte ptr [rsp + 0x40], r15b
0091510B  40 0F B6 ED                     movzx ebp, bpl
0091510F  0F 44 EE                        cmove ebp, esi
00915112  EB B7                           jmp 0x1409150cb
00915114  BE 01 00 00 00                  mov esi, 1
00915119  EB 81                           jmp 0x14091509c
0091511B  8B 6C 24 44                     mov ebp, dword ptr [rsp + 0x44]
0091511F  BF 9A 00 00 C0                  mov edi, 0xc000009a
00915124  41 8A F7                        mov sil, r15b
00915127  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
0091512C  E9 26 FE FF FF                  jmp 0x140914f57
00915131  40 8A F7                        mov sil, dil
00915134  EB F1                           jmp 0x140915127
00915136  BA 58 00 00 00                  mov edx, 0x58
0091513B  B9 00 01 00 00                  mov ecx, 0x100
00915140  41 B8 50 53 65 74               mov r8d, 0x74655350
00915146  E8 A5 CF 26 00                  call 0x140b820f0
0091514B  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00915150  48 8B D8                        mov rbx, rax
00915153  48 85 C0                        test rax, rax
00915156  0F 84 DC 00 00 00               je 0x140915238
0091515C  48 8B AC 24 B0 00 00 00         mov rbp, qword ptr [rsp + 0xb0]
00915164  48 8B CD                        mov rcx, rbp
00915167  0F 10 45 00                     movups xmm0, xmmword ptr [rbp]
0091516B  F3 0F 7F 40 20                  movdqu xmmword ptr [rax + 0x20], xmm0
00915170  E8 6F FC FF FF                  call 0x140914de4
00915175  4C 8D 43 10                     lea r8, [rbx + 0x10]
00915179  4C 8B D0                        mov r10, rax
0091517C  4D 89 40 08                     mov qword ptr [r8 + 8], r8
00915180  4D 89 00                        mov qword ptr [r8], r8
00915183  44 38 74 24 40                  cmp byte ptr [rsp + 0x40], r14b
00915188  75 65                           jne 0x1409151ef
0091518A  48 8B 0D 4F 75 5F 00            mov rcx, qword ptr [rip + 0x5f754f]
00915191  4C 8D 1D 48 75 5F 00            lea r11, [rip + 0x5f7548]
00915198  49 3B CB                        cmp rcx, r11
0091519B  74 4F                           je 0x1409151ec
0091519D  4C 8D 09                        lea r9, [rcx]
009151A0  48 8B 09                        mov rcx, qword ptr [rcx]
009151A3  49 8B 51 24                     mov rdx, qword ptr [r9 + 0x24]
009151A7  48 2B 55 00                     sub rdx, qword ptr [rbp]
009151AB  75 08                           jne 0x1409151b5
009151AD  49 8B 51 2C                     mov rdx, qword ptr [r9 + 0x2c]
009151B1  48 2B 55 08                     sub rdx, qword ptr [rbp + 8]
009151B5  48 85 D2                        test rdx, rdx
009151B8  75 DE                           jne 0x140915198
009151BA  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
009151BE  48 39 08                        cmp qword ptr [rax], rcx
009151C1  75 38                           jne 0x1409151fb
009151C3  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
009151C7  48 39 02                        cmp qword ptr [rdx], rax
009151CA  75 2F                           jne 0x1409151fb
009151CC  48 89 51 08                     mov qword ptr [rcx + 8], rdx
009151D0  48 89 0A                        mov qword ptr [rdx], rcx
009151D3  49 8B 50 08                     mov rdx, qword ptr [r8 + 8]
009151D7  4C 39 02                        cmp qword ptr [rdx], r8
009151DA  75 1F                           jne 0x1409151fb
009151DC  4C 89 00                        mov qword ptr [rax], r8
009151DF  48 89 50 08                     mov qword ptr [rax + 8], rdx
009151E3  48 89 02                        mov qword ptr [rdx], rax
009151E6  49 89 40 08                     mov qword ptr [r8 + 8], rax
009151EA  EB AC                           jmp 0x140915198
009151EC  83 CE FF                        or esi, 0xffffffff
009151EF  89 73 30                        mov dword ptr [rbx + 0x30], esi
009151F2  49 8B 42 08                     mov rax, qword ptr [r10 + 8]
009151F6  4C 39 10                        cmp qword ptr [rax], r10
009151F9  74 07                           je 0x140915202
009151FB  B9 03 00 00 00                  mov ecx, 3
00915200  CD 29                           int 0x29
00915202  4C 89 13                        mov qword ptr [rbx], r10
00915205  B9 01 00 00 00                  mov ecx, 1
0091520A  48 89 43 08                     mov qword ptr [rbx + 8], rax
0091520E  48 89 18                        mov qword ptr [rax], rbx
00915211  49 89 5A 08                     mov qword ptr [r10 + 8], rbx
00915215  44 39 35 BC 24 55 00            cmp dword ptr [rip + 0x5524bc], r14d
0091521C  88 4C 24 41                     mov byte ptr [rsp + 0x41], cl
00915220  75 0D                           jne 0x14091522f
00915222  44 39 35 B3 24 55 00            cmp dword ptr [rip + 0x5524b3], r14d
00915229  0F 84 DE FC FF FF               je 0x140914f0d
0091522F  88 4C 24 42                     mov byte ptr [rsp + 0x42], cl
00915233  E9 D5 FC FF FF                  jmp 0x140914f0d
00915238  BF 9A 00 00 C0                  mov edi, 0xc000009a
0091523D  41 8A F6                        mov sil, r14b
00915240  45 33 FF                        xor r15d, r15d
00915243  E9 0F FD FF FF                  jmp 0x140914f57
00915248  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
00915250  4C 8D 05 E9 40 12 00            lea r8, [rip + 0x1240e9]
00915257  45 33 C9                        xor r9d, r9d
0091525A  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0091525F  33 C9                           xor ecx, ecx
00915261  E8 EA CE 16 00                  call 0x140a82150
00915266  E9 09 FD FF FF                  jmp 0x140914f74
0091526B  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00915270  48 8D 0D 61 24 55 00            lea rcx, [rip + 0x552461]
00915277  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
0091527C  45 33 C9                        xor r9d, r9d
0091527F  45 33 C0                        xor r8d, r8d
00915282  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00915287  33 D2                           xor edx, edx
00915289  E8 82 BA D9 FF                  call 0x1406b0d10
0091528E  E9 02 FD FF FF                  jmp 0x140914f95
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSetPowerSettingValue(__int64 a1, int a2, int a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m64;
    unsigned __int8 v_stack_m66;
    unsigned __int8 v_stack_m67;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p41;
    unsigned __int8 v_stack_p42;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pB0;
    unsigned int v_stack_pC0;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_m67 = 0;
    v_stack_m64 = 0;
    v_stack_m66 = 0;
    result = ExAllocatePool2(256, (unsigned int)(a4), (unsigned int)(0x74655350ULL), a4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00914FDD;
    a1 = 0;
    result = PopIncrementPowerSettingPendingUpdates(a1, (unsigned int)(a4), (unsigned int)(0x74655350ULL), a4);
    result = memcpy(result, a5, (unsigned int)((unsigned int)((unsigned int)(a4))), a4);
    result = PopValidatePowerSettingData(0, (unsigned int)((unsigned int)((unsigned int)(a4))), result, a4);
    result = PopStateIsSessionSpecific(0, (unsigned int)((unsigned int)((unsigned int)(a4))), result, a4);
    v_stack_m68 = (unsigned __int8)(result);
    result = ExAcquireFastMutex(v_rip + 6262871, (unsigned int)((unsigned int)((unsigned int)(a4))), result, a4);
    result = PopFindPowerSettingConfiguration(0, (unsigned int)((unsigned int)((unsigned int)(a2))), result, a4);
    v_stack_m48 = result;
    if (result == 0) goto loc_00915136;
loc_00914F0D:
    v_stack_m50 = (int)(v_stack_p18);
    if (*(unsigned __int64 *)(result + (int)(v_stack_p18) * 8 + 64) == 0) goto loc_00914FE9;
    if ((*(unsigned int *)(*(unsigned __int64 *)(result + (int)(v_stack_p18) * 8 + 64) + 4)) != ((unsigned int)((unsigned int)(a4)))) goto loc_00914FE9;
    result = RtlCompareMemory(*(unsigned __int64 *)(result + (int)(v_stack_p18) * 8 + 64) + 12, result, (unsigned int)(a4), a4);
    if (result != ((unsigned int)(a4))) goto loc_00914FE4;
    v_r15 = 0;
loc_00914F57:
loc_00914F5D:
    result = ExReleaseFastMutex(v_rip + 6262748, result, (unsigned int)(a4), a4);
    if (v_stack_m67 != 0) goto loc_00915248;
loc_00914F74:
    result = ExFreePoolWithTag(result, (unsigned int)(0x74655350ULL), (unsigned int)(a4), a4);
    if ((*(unsigned int *)(v_rip + 6257368)) < 3) goto loc_00914FBB;
    if (v_stack_m66 != 0) goto loc_0091526B;
loc_00914F95:
    if ((unsigned __int8)((unsigned int)(v_stack_m64)) != 0) {
        a1 = 1;
        result = PopIncrementPowerSettingPendingUpdates(a1, (unsigned int)(0x74655350ULL), (unsigned int)(a4), a4);
        a1 = 32;
        result = PopSetNotificationWork(a1, (unsigned int)(0x74655350ULL), (unsigned int)(a4), a4);
    }
    if (0 != 0) {
        a1 = 128;
        result = PopSetNotificationWork(a1, (unsigned int)(0x74655350ULL), (unsigned int)(a4), a4);
    }
    a1 = 0;
    result = PopDecrementPowerSettingPendingUpdates(a1, (unsigned int)(0x74655350ULL), (unsigned int)(a4), a4);
loc_00914FC4:
    v_rsp = (v_rsp) + (112);
    return 0;
loc_00914FDD:
    goto loc_00914FC4;
loc_00914FE4:
loc_00914FE9:
    v_r12 = 0;
    v_r15 = 0;
loc_00914FFC:
    if (0 == v_stack_p58) goto loc_0091502E;
    if (1 != 0) goto loc_00915023;
    result = PopArePowerSettingsEqual(*(unsigned __int64 *)(v_stack_p10 + 64), v_stack_p50, (unsigned int)((unsigned int)((unsigned int)(a4))), a4);
    v_r14 = 1;
    if ((unsigned __int8)(result) != 0) {
        v_r14 = *(unsigned __int64 *)(v_stack_p10 + 64);
    }
    v_r12 = 0;
    if ((*(unsigned __int64 *)(v_stack_p10 + 64)) == ((unsigned int)(v_stack_m64))) { v_r12 = (unsigned int)(v_r15 + 1); }
loc_0091502E:
    v_r15 = (v_r15) + (v_r15 + 1);
    v_rsi = (v_stack_p10 + 64) + (8);
    if (v_r15 < 3) goto loc_00914FFC;
    v_r15 = 0;
    if (v_r14 != 0) goto loc_00915114;
    result = ExAllocatePool2(256, (unsigned int)(a4) + 12, (unsigned int)(0x74655350ULL), a4);
    if (result == 0) goto loc_0091511B;
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)(a4));
    *(unsigned int *)(result) = (unsigned int)(v_r15 + 1);
loc_00915079:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15 + 1))) + ((unsigned int)(v_r15 + 1)));
    if (condition_is_equal) goto loc_00915079;
    *(unsigned int *)(result + 8) = (unsigned int)(result);
    result = memcpy(result + 12, v_stack_p50, (unsigned int)(a4), a4);
loc_0091509C:
    if ((unsigned int)(v_stack_m64) == 0) goto loc_009150AE;
    if ((unsigned __int8)(v_r12) == 0) goto loc_009150EB;
loc_009150A6:
    result = PopUnreferencePowerSetting((unsigned int)(v_stack_m64), v_stack_p50, (unsigned int)(a4), a4);
loc_009150AE:
    *(unsigned __int64 *)(v_stack_p60 + v_stack_p58 * 8 + 64) = result;
    if ((*(unsigned int *)(v_rip + 6257987)) == ((unsigned int)((unsigned int)(v_stack_pC0)))) goto loc_00915106;
loc_009150CB:
    if ((*(unsigned int *)(v_stack_p60 + 56)) != 0) goto loc_009150D7;
    if ((*(unsigned int *)(v_stack_p60 + 60)) == 0) goto loc_00915131;
loc_009150D7:
    goto loc_00914F5D;
loc_009150EB:
loc_009150F2:
    if ((*(unsigned __int64 *)(v_stack_p60 + 16)) == (v_stack_p60 + 16)) goto loc_009150A6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p60 + 16) + 72)) == ((unsigned int)(v_stack_p44))) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p60 + 16) + 72) = 0;
    }
    goto loc_009150F2;
loc_00915106:
    v_rbp = (unsigned __int8)((unsigned int)(v_stack_p44));
    if (v_stack_p40 == 0) { v_rbp = (unsigned int)(v_r15 + 1); }
    goto loc_009150CB;
loc_00915114:
    goto loc_0091509C;
loc_0091511B:
loc_00915127:
    goto loc_00914F57;
loc_00915131:
    goto loc_00915127;
loc_00915136:
    result = ExAllocatePool2(256, 88, (unsigned int)(0x74655350ULL), a4);
    v_stack_p60 = result;
    if (result == 0) goto loc_00915238;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    result = PopGetListHead(v_stack_pB0, 88, (unsigned int)(0x74655350ULL), a4);
    *(unsigned __int64 *)(result + 16 + 8) = result + 16;
    *(unsigned __int64 *)(result + 16) = result + 16;
    if (v_stack_p40 != 1) goto loc_009151EF;
loc_00915198:
    if ((*(unsigned __int64 *)(v_rip + 6255951)) == (v_rip + 6255944)) goto loc_009151EC;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951) + 36)) - (*(unsigned __int64 *)(v_stack_pB0));
    if (!(condition_is_not_equal)) {
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951) + 44);
        a2 = (a2) - (*(unsigned __int64 *)(v_stack_pB0 + 8));
    }
    if (a2 != 0) goto loc_00915198;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951)))) goto loc_009151FB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951)) + 8) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951)) + 8))) goto loc_009151FB;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951)) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951)) + 8) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951)) + 8) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8))) != (result + 16)) goto loc_009151FB;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951)) + 8)) = result + 16;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951)) + 8) + 8) = *(unsigned __int64 *)(result + 16 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951)) + 8);
    *(unsigned __int64 *)(result + 16 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6255951)) + 8);
    goto loc_00915198;
loc_009151EC:
    v_rsi = (unsigned int)(((unsigned __int8)((unsigned int)(0xC000009AULL))) | (0xFFFFFFFFULL));
loc_009151EF:
    *(unsigned int *)(result + 48) = (unsigned int)(v_rsi);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) {
        a1 = 3;
    }
    *(unsigned __int64 *)(result) = result;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(result + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = result;
    *(unsigned __int64 *)(result + 8) = result;
    v_stack_p41 = 1;
    if ((*(unsigned int *)(v_rip + 5579964)) != 1) goto loc_0091522F;
    if ((*(unsigned int *)(v_rip + 5579955)) == 1) goto loc_00914F0D;
loc_0091522F:
    v_stack_p42 = 1;
    goto loc_00914F0D;
loc_00915238:
    v_r15 = 0;
    goto loc_00914F57;
loc_00915248:
    a4 = 0;
    v_stack_p20 = 0;
    a1 = 0;
    result = PoRegisterPowerSettingCallback(a1, v_stack_pB0, v_rip + 1196265, a4);
    goto loc_00914F74;
loc_0091526B:
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    a4 = 0;
    a3 = 0;
    v_stack_p20 = 0;
    a2 = 0;
    result = ZwUpdateWnfStateData(v_rip + 5579873, a2, a3, a4);
    goto loc_00914F95;
}
```

## 5. (Beta) C Style

```c
int64_t PopSetPowerSettingValue(int64_t Arg1, int32_t Arg2, int32_t Arg3, void *Arg4, int64_t Arg5)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m64;
    uint8_t v_stack_m66;
    uint8_t v_stack_m67;
    uint8_t v_stack_m68;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint8_t v_stack_p40;
    uint8_t v_stack_p41;
    uint8_t v_stack_p42;
    uint32_t v_stack_p44;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p8;
    uint64_t v_stack_pB0;
    uint32_t v_stack_pC0;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_m67 = 0;
    v_stack_m64 = 0;
    v_stack_m66 = 0;
    result = ExAllocatePool2(256, (uint32_t)(Arg4), (uint32_t)(0x74655350ULL), Arg4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00914FDD;
    Arg1 = 0;
    result = PopIncrementPowerSettingPendingUpdates(Arg1, (uint32_t)(Arg4), (uint32_t)(0x74655350ULL), Arg4);
    result = memcpy(result, Arg5, (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg4);
    result = PopValidatePowerSettingData(0, (uint32_t)((uint32_t)((uint32_t)(Arg4))), result, Arg4);
    result = PopStateIsSessionSpecific(0, (uint32_t)((uint32_t)((uint32_t)(Arg4))), result, Arg4);
    v_stack_m68 = (uint8_t)(result);
    result = ExAcquireFastMutex(v_rip + 6262871, (uint32_t)((uint32_t)((uint32_t)(Arg4))), result, Arg4);
    result = PopFindPowerSettingConfiguration(0, (uint32_t)((uint32_t)((uint32_t)(Arg2))), result, Arg4);
    v_stack_m48 = result;
    if (result == 0) goto loc_00915136;
loc_00914F0D:
    v_stack_m50 = (int32_t)(v_stack_p18);
    if (*(uint64_t *)(result + (int32_t)(v_stack_p18) * 8 + 0x40) == 0) goto loc_00914FE9;
    if ((*(uint32_t *)(*(uint64_t *)(result + (int32_t)(v_stack_p18) * 8 + 0x40) + 0x4)) != ((uint32_t)((uint32_t)(Arg4)))) goto loc_00914FE9;
    result = RtlCompareMemory(*(uint64_t *)(result + (int32_t)(v_stack_p18) * 8 + 0x40) + 12, result, (uint32_t)(Arg4), Arg4);
    if (result != ((uint32_t)(Arg4))) goto loc_00914FE4;
    local_r15 = 0;
loc_00914F57:
loc_00914F5D:
    result = ExReleaseFastMutex(v_rip + 6262748, result, (uint32_t)(Arg4), Arg4);
    if (v_stack_m67 != 0) goto loc_00915248;
loc_00914F74:
    result = ExFreePoolWithTag(result, (uint32_t)(0x74655350ULL), (uint32_t)(Arg4), Arg4);
    if ((*(uint32_t *)(v_rip + 0x5F7AD8)) < 3) goto loc_00914FBB;
    if (v_stack_m66 != 0) goto loc_0091526B;
loc_00914F95:
    if ((uint8_t)((uint32_t)(v_stack_m64)) != 0) {
        Arg1 = 1;
        result = PopIncrementPowerSettingPendingUpdates(Arg1, (uint32_t)(0x74655350ULL), (uint32_t)(Arg4), Arg4);
        Arg1 = 32;
        result = PopSetNotificationWork(Arg1, (uint32_t)(0x74655350ULL), (uint32_t)(Arg4), Arg4);
    }
    if (0 != 0) {
        Arg1 = 128;
        result = PopSetNotificationWork(Arg1, (uint32_t)(0x74655350ULL), (uint32_t)(Arg4), Arg4);
    }
    Arg1 = 0;
    result = PopDecrementPowerSettingPendingUpdates(Arg1, (uint32_t)(0x74655350ULL), (uint32_t)(Arg4), Arg4);
loc_00914FC4:
    local_rsp = (local_rsp) + (112);
    return 0;
loc_00914FDD:
    goto loc_00914FC4;
loc_00914FE4:
loc_00914FE9:
    local_r12 = 0;
    local_r15 = 0;
loc_00914FFC:
    if (0 == v_stack_p58) goto loc_0091502E;
    if (1 != 0) goto loc_00915023;
    result = PopArePowerSettingsEqual(*(uint64_t *)(v_stack_p10 + 0x40), v_stack_p50, (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg4);
    local_r14 = 1;
    if ((uint8_t)(result) != 0) {
        local_r14 = *(uint64_t *)(v_stack_p10 + 0x40);
    }
    local_r12 = 0;
    if ((*(uint64_t *)(v_stack_p10 + 0x40)) == ((uint32_t)(v_stack_m64))) { local_r12 = (uint32_t)(local_r15 + 1); }
loc_0091502E:
    local_r15 = (local_r15) + (local_r15 + 1);
    local_rsi = (v_stack_p10 + 64) + (8);
    if (local_r15 < 3) goto loc_00914FFC;
    local_r15 = 0;
    if (local_r14 != 0) goto loc_00915114;
    result = ExAllocatePool2(256, (uint32_t)(Arg4) + 12, (uint32_t)(0x74655350ULL), Arg4);
    if (result == 0) goto loc_0091511B;
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)(Arg4));
    *(uint32_t *)(result) = (uint32_t)(local_r15 + 1);
loc_00915079:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15 + 1))) + ((uint32_t)(local_r15 + 1)));
    if (condition_is_equal) goto loc_00915079;
    *(uint32_t *)(result + 0x8) = (uint32_t)(result);
    result = memcpy(result + 12, v_stack_p50, (uint32_t)(Arg4), Arg4);
loc_0091509C:
    if ((uint32_t)(v_stack_m64) == 0) goto loc_009150AE;
    if ((uint8_t)(local_r12) == 0) goto loc_009150EB;
loc_009150A6:
    result = PopUnreferencePowerSetting((uint32_t)(v_stack_m64), v_stack_p50, (uint32_t)(Arg4), Arg4);
loc_009150AE:
    *(uint64_t *)(v_stack_p60 + v_stack_p58 * 8 + 0x40) = result;
    if ((*(uint32_t *)(v_rip + 0x5F7D43)) == ((uint32_t)((uint32_t)(v_stack_pC0)))) goto loc_00915106;
loc_009150CB:
    if ((*(uint32_t *)(v_stack_p60 + 0x38)) != 0) goto loc_009150D7;
    if ((*(uint32_t *)(v_stack_p60 + 0x3C)) == 0) goto loc_00915131;
loc_009150D7:
    goto loc_00914F5D;
loc_009150EB:
loc_009150F2:
    if ((*(uint64_t *)(v_stack_p60 + 0x10)) == (v_stack_p60 + 16)) goto loc_009150A6;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p60 + 0x10) + 0x48)) == ((uint32_t)(v_stack_p44))) {
        *(uint64_t *)(*(uint64_t *)(v_stack_p60 + 0x10) + 0x48) = 0;
    }
    goto loc_009150F2;
loc_00915106:
    local_rbp = (uint8_t)((uint32_t)(v_stack_p44));
    if (v_stack_p40 == 0) { local_rbp = (uint32_t)(local_r15 + 1); }
    goto loc_009150CB;
loc_00915114:
    goto loc_0091509C;
loc_0091511B:
loc_00915127:
    goto loc_00914F57;
loc_00915131:
    goto loc_00915127;
loc_00915136:
    result = ExAllocatePool2(256, 88, (uint32_t)(0x74655350ULL), Arg4);
    v_stack_p60 = result;
    if (result == 0) goto loc_00915238;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    result = PopGetListHead(v_stack_pB0, 88, (uint32_t)(0x74655350ULL), Arg4);
    *(uint64_t *)(result + 0x10 + 0x8) = result + 16;
    *(uint64_t *)(result + 0x10) = result + 16;
    if (v_stack_p40 != 1) goto loc_009151EF;
loc_00915198:
    if ((*(uint64_t *)(v_rip + 0x5F754F)) == (v_rip + 6255944)) goto loc_009151EC;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F) + 0x24)) - (*(uint64_t *)(v_stack_pB0));
    if (!(condition_is_not_equal)) {
        Arg2 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F) + 0x2C);
        Arg2 = (Arg2) - (*(uint64_t *)(v_stack_pB0 + 0x8));
    }
    if (Arg2 != 0) goto loc_00915198;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F)))) goto loc_009151FB;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F)) + 0x8) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F)) + 0x8))) goto loc_009151FB;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F)) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F)) + 0x8) + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F)) + 0x8) + 0x8)) = *(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F));
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8))) != (result + 16)) goto loc_009151FB;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F)) + 0x8)) = result + 16;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F)) + 0x8) + 0x8) = *(uint64_t *)(result + 0x10 + 0x8);
    *(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F)) + 0x8);
    *(uint64_t *)(result + 0x10 + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5F754F)) + 0x8);
    goto loc_00915198;
loc_009151EC:
    local_rsi = (uint32_t)(((uint8_t)((uint32_t)(0xC000009AULL))) | (0xFFFFFFFFULL));
loc_009151EF:
    *(uint32_t *)(result + 0x30) = (uint32_t)(local_rsi);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) {
        Arg1 = 3;
    }
    *(uint64_t *)(result) = result;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(result + 0x8);
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = result;
    *(uint64_t *)(result + 0x8) = result;
    v_stack_p41 = 1;
    if ((*(uint32_t *)(v_rip + 0x5524BC)) != 1) goto loc_0091522F;
    if ((*(uint32_t *)(v_rip + 0x5524B3)) == 1) goto loc_00914F0D;
loc_0091522F:
    v_stack_p42 = 1;
    goto loc_00914F0D;
loc_00915238:
    local_r15 = 0;
    goto loc_00914F57;
loc_00915248:
    Arg4 = 0;
    v_stack_p20 = 0;
    Arg1 = 0;
    result = PoRegisterPowerSettingCallback(Arg1, v_stack_pB0, v_rip + 1196265, Arg4);
    goto loc_00914F74;
loc_0091526B:
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p20 = 0;
    Arg2 = 0;
    result = ZwUpdateWnfStateData(v_rip + 5579873, Arg2, Arg3, Arg4);
    goto loc_00914F95;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0xC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00914E54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
