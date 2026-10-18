# PopPepProcessEvent

- RVA: `0x0024B930`–`0x0024CC89` (길이 `4,953` bytes)
- VA: `0x000000014024B930`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00062C9C`
- 디코드: `1,205`개 명령, `4,953/4,953` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **49**; 고유 호출 대상: **31**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **36**

### Outgoing calls
- `0x0024B9C5` → [ExpWaitForSpinLockExclusiveAndAcquire](../32/ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) (function, `0x003239A0`)
- `0x0024BAC1` → [PopPepCompleteComponentActiveActivity](PopPepCompleteComponentActiveActivity_function_0024D5F0.md) (function, `0x0024D5F0`)
- `0x0024BB96` → [PopPepTriggerComponentActiveActivity](PopPepTriggerComponentActiveActivity_function_0024D860.md) (function, `0x0024D860`)
- `0x0024BBA0` → [PopPepTriggerComponentActivatingActivity](PopPepTriggerComponentActivatingActivity_function_0024D790.md) (function, `0x0024D790`)
- `0x0024C0E5` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0024C137` → [ExpWaitForSpinLockExclusiveAndAcquire](../32/ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) (function, `0x003239A0`)
- `0x0024C1C3` → [PopPepTriggerActivity](PopPepTriggerActivity_function_0024CDB0.md) (function, `0x0024CDB0`)
- `0x0024C1D1` → [PopPepPromoteActivities](PopPepPromoteActivities_function_0024D0D0.md) (function, `0x0024D0D0`)
- `0x0024C206` → [PopPepStartActivity](PopPepStartActivity_function_0024D6E0.md) (function, `0x0024D6E0`)
- `0x0024C21A` → [PopPepReleaseActivityLink](PopPepReleaseActivityLink_function_0024CC90.md) (function, `0x0024CC90`)
- `0x0024C34B` → [PopPepStartComponentActivatingActivity](../2B/PopPepStartComponentActivatingActivity_function_002BE740.md) (function, `0x002BE740`)
- `0x0024C3AC` → [ExReleaseSpinLockSharedFromDpcLevel](ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x0024C3CB` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0024C414` → [PopPepCompleteComponentIdleStateChangeActivity](../2B/PopPepCompleteComponentIdleStateChangeActivity_function_002BF1B0.md) (function, `0x002BF1B0`)
- `0x0024C434` → [ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented](../32/ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_00323A70.md) (function, `0x00323A70`)
- `0x0024C453` → [ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented](../32/ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_00323A70.md) (function, `0x00323A70`)
- `0x0024C463` → [PopPepRequestWork](../39/PopPepRequestWork_function_003986F0.md) (function, `0x003986F0`)
- `0x0024C4C7` → [PopPepGetReadyActivityType](../45/PopPepGetReadyActivityType_function_00454858.md) (function, `0x00454858`)
- `0x0024C4E6` → [PopPepStartActivity](PopPepStartActivity_function_0024D6E0.md) (function, `0x0024D6E0`)
- `0x0024C51C` → [ExAcquireSpinLockShared](ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)
- `0x0024C537` → [ExAcquireSpinLockExclusiveAtDpcLevel](ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0024C547` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0024C558` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0024C590` → [KeReleaseSemaphore](../39/KeReleaseSemaphore_function_00397080.md) (function, `0x00397080`)
- `0x0024C5DE` → [ExpTryQueueWorkItem](../39/ExpTryQueueWorkItem_function_0039801C.md) (function, `0x0039801C`)
- `0x0024C620` → [PopPepCompleteDevicePowerOnActivity](../2B/PopPepCompleteDevicePowerOnActivity_function_002BFC90.md) (function, `0x002BFC90`)
- `0x0024C63F` → [PopFxBugCheck](../2B/PopFxBugCheck_function_002BFC6C.md) (function, `0x002BFC6C`)
- `0x0024C7C2` → [PopPepTriggerComponentIdleStateChangeActivity](../46/PopPepTriggerComponentIdleStateChangeActivity_function_00463D90.md) (function, `0x00463D90`)
- `0x0024C7F9` → [PopPepStartDevicePowerOnActivity](../2B/PopPepStartDevicePowerOnActivity_function_002BE770.md) (function, `0x002BE770`)
- `0x0024C843` → [KeReleaseSemaphore](../39/KeReleaseSemaphore_function_00397080.md) (function, `0x00397080`)
- `0x0024C88D` → [ExpTryQueueWorkItem](../39/ExpTryQueueWorkItem_function_0039801C.md) (function, `0x0039801C`)
- `0x0024C944` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0024CA07` → [PopPepStartComponentActivatingActivity](../2B/PopPepStartComponentActivatingActivity_function_002BE740.md) (function, `0x002BE740`)
- `0x0024CA7F` → [PopPepStartDevicePowerOffActivity](../2B/PopPepStartDevicePowerOffActivity_function_002BE790.md) (function, `0x002BE790`)
- `0x0024CAD7` → [PopPepStartActivity](PopPepStartActivity_function_0024D6E0.md) (function, `0x0024D6E0`)
- `0x0024CB1B` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0024CB2A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0024CB42` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0024CB52` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0024CB80` → [PopPepStartDevicePowerOnActivity](../2B/PopPepStartDevicePowerOnActivity_function_002BE770.md) (function, `0x002BE770`)
- `0x0024CBA6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0024CBC3` → [PopPepStartDevicePowerOffActivity](../2B/PopPepStartDevicePowerOffActivity_function_002BE790.md) (function, `0x002BE790`)
- `0x0024CBD9` → [ExReleaseSpinLockExclusive](../2C/ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)
- `0x0024CBFC` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x0024CC06` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0024CC29` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x0024CC3E` → [ExReleaseSpinLockShared](../2F/ExReleaseSpinLockShared_function_002F0EF0.md) (function, `0x002F0EF0`)
- `0x0024CC5B` → [PopFxBugCheck](../2B/PopFxBugCheck_function_002BFC6C.md) (function, `0x002BFC6C`)
- `0x0024CC61` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PopPluginComponentActive](PopPluginComponentActive_function_0024B800.md) at `0x0024B8C5`
- [sub_002BD41B](../2B/Unknown_function_002BD41B.md) at `0x002BD698`
- [sub_002BD95A](../2B/Unknown_function_002BD95A.md) at `0x002BD97C`
- [sub_002BD95A](../2B/Unknown_function_002BD95A.md) at `0x002BDCF3`
- [PopPluginComponentIdleState](../2B/PopPluginComponentIdleState_function_002BE310.md) at `0x002BE3E3`
- [PopFxActivateComponentDependents](../2B/PopFxActivateComponentDependents_function_002BE9F0.md) at `0x002BEC71`
- [PopFxCompleteDevicePowerRequired](../39/PopFxCompleteDevicePowerRequired_function_003908AC.md) at `0x00390918`
- [PopPepCompleteComponentIdleState](../4D/PopPepCompleteComponentIdleState_function_004D8EC4.md) at `0x004D8F80`
- [PopPepUnregisterDevice](../../page/A8/PopPepUnregisterDevice_function_00A8B048.md) at `0x00A8B082`

### Static image references
- `0x0024B965` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0024B998` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0024B9A5` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0024B9EC` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0024BAA3` → RVA `0x0024D5F0` (`PopPepCompleteComponentActiveActivity`; read)
- `0x0024BB5E` → RVA `0x0024D790` (`PopPepTriggerComponentActivatingActivity`; read)
- `0x0024BB83` → RVA `0x0024D860` (`PopPepTriggerComponentActiveActivity`; read)
- `0x0024BBC9` → RVA `0x00001070` (`.rdata`; read)
- `0x0024BBE1` → RVA `0x00001088` (`.rdata`; read)
- `0x0024BC29` → RVA `0x00001074` (`.rdata`; read)
- `0x0024BC3A` → RVA `0x0000108C` (`.rdata`; read)
- `0x0024BC84` → RVA `0x00001098` (`.rdata`; read)
- `0x0024BC8B` → RVA `0x00001080` (`.rdata`; read)
- `0x0024BCF8` → RVA `0x000010C0` (`.rdata`; read)
- `0x0024BF03` → RVA `0x000012E0` (`.rdata`; read)
- `0x0024BF17` → RVA `0x00001318` (`.rdata`; read)
- `0x0024BF21` → RVA `0x00001330` (`.rdata`; read)
- `0x0024BF66` → RVA `0x0000131C` (`.rdata`; read)
- `0x0024BF77` → RVA `0x00001334` (`.rdata`; read)
- `0x0024BFC0` → RVA `0x00001328` (`.rdata`; read)
- `0x0024BFC7` → RVA `0x00001340` (`.rdata`; read)
- `0x0024C338` → RVA `0x002BE740` (`PopPepStartComponentActivatingActivity`; read)
- `0x0024C401` → RVA `0x002BF1B0` (`PopPepCompleteComponentIdleStateChangeActivity`; read)
- `0x0024C41E` → RVA `0x00F0DE58` (`.data`; read)
- `0x0024C584` → RVA `0x00F0E2E0` (`.data`; read)
- `0x0024C59A` → RVA `0x00F0E300` (`.data`; read)
- `0x0024C5CF` → RVA `0x00FC6EA0` (`ALMOSTRO`; read)
- `0x0024C60D` → RVA `0x002BFC90` (`PopPepCompleteDevicePowerOnActivity`; read)
- `0x0024C7AF` → RVA `0x00463D90` (`PopPepTriggerComponentIdleStateChangeActivity`; read)
- `0x0024C7E6` → RVA `0x002BE770` (`PopPepStartDevicePowerOnActivity`; read)
- `0x0024C812` → RVA `0x00F0E300` (`.data`; read/write)
- `0x0024C837` → RVA `0x00F0E5C0` (`.data`; read)
- `0x0024C84D` → RVA `0x00F0E5E0` (`.data`; read)
- `0x0024C8A4` → RVA `0x00F0E5E0` (`.data`; read/write)
- `0x0024CA6C` → RVA `0x002BE790` (`PopPepStartDevicePowerOffActivity`; read)
- `0x0024CB0D` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0024B930  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0024B935  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0024B93A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0024B93F  55                              push rbp
0024B940  56                              push rsi
0024B941  57                              push rdi
0024B942  41 54                           push r12
0024B944  41 55                           push r13
0024B946  41 56                           push r14
0024B948  41 57                           push r15
0024B94A  48 83 EC 60                     sub rsp, 0x60
0024B94E  4C 8B EA                        mov r13, rdx
0024B951  4D 63 F1                        movsxd r14, r9d
0024B954  45 33 E4                        xor r12d, r12d
0024B957  49 63 E8                        movsxd rbp, r8d
0024B95A  C6 84 24 B0 00 00 00 00         mov byte ptr [rsp + 0xb0], 0
0024B962  48 8B D9                        mov rbx, rcx
0024B965  48 8D 35 94 46 DB FF            lea rsi, [rip - 0x24b96c]
0024B96C  BA 02 00 00 00                  mov edx, 2
0024B971  4D 85 ED                        test r13, r13
0024B974  74 0D                           je 0x14024b983
0024B976  83 B9 B4 00 00 00 01            cmp dword ptr [rcx + 0xb4], 1
0024B97D  0F 85 52 0A 00 00               jne 0x14024c3d5
0024B983  C6 84 24 B0 00 00 00 01         mov byte ptr [rsp + 0xb0], 1
0024B98B  45 0F 20 C7                     mov r15, cr8
0024B98F  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
0024B994  44 0F 22 C2                     mov cr8, rdx
0024B998  44 39 25 81 B3 D7 00            cmp dword ptr [rip + 0xd7b381], r12d
0024B99F  0F 85 9C 0B 00 00               jne 0x14024c541
0024B9A5  F6 05 5A B1 D7 00 21            test byte ptr [rip + 0xd7b15a], 0x21
0024B9AC  0F 85 6C 0A 00 00               jne 0x14024c41e
0024B9B2  F0 0F BA 6B 40 1F               lock bts dword ptr [rbx + 0x40], 0x1f
0024B9B8  41 8B F4                        mov esi, r12d
0024B9BB  73 0F                           jae 0x14024b9cc
0024B9BD  41 0F B6 D7                     movzx edx, r15b
0024B9C1  48 8D 4B 40                     lea rcx, [rbx + 0x40]
0024B9C5  E8 D6 7F 0D 00                  call 0x1403239a0
0024B9CA  8B F0                           mov esi, eax
0024B9CC  8B 4B 40                        mov ecx, dword ptr [rbx + 0x40]
0024B9CF  8B C1                           mov eax, ecx
0024B9D1  0F BA F0 1E                     btr eax, 0x1e
0024B9D5  3D 00 00 00 80                  cmp eax, 0x80000000
0024B9DA  74 2E                           je 0x14024ba0a
0024B9DC  0F BA E1 1E                     bt ecx, 0x1e
0024B9E0  72 08                           jb 0x14024b9ea
0024B9E2  F0 81 4B 40 00 00 00 40         lock or dword ptr [rbx + 0x40], 0x40000000
0024B9EA  FF C6                           inc esi
0024B9EC  85 35 BA 98 D7 00               test dword ptr [rip + 0xd798ba], esi
0024B9F2  0F 84 15 11 00 00               je 0x14024cb0d
0024B9F8  F3 90                           pause
0024B9FA  8B 4B 40                        mov ecx, dword ptr [rbx + 0x40]
0024B9FD  8B C1                           mov eax, ecx
0024B9FF  0F BA F0 1E                     btr eax, 0x1e
0024BA03  3D 00 00 00 80                  cmp eax, 0x80000000
0024BA08  75 D2                           jne 0x14024b9dc
0024BA0A  48 8D 35 EF 45 DB FF            lea rsi, [rip - 0x24ba11]
0024BA11  C6 43 7D 01                     mov byte ptr [rbx + 0x7d], 1
0024BA15  4C 8B C5                        mov r8, rbp
0024BA18  83 FD 06                        cmp ebp, 6
0024BA1B  0F 84 53 09 00 00               je 0x14024c374
0024BA21  49 69 C0 88 00 00 00            imul rax, r8, 0x88
0024BA28  8B 8C 30 3C 10 00 00            mov ecx, dword ptr [rax + rsi + 0x103c]
0024BA2F  83 F9 02                        cmp ecx, 2
0024BA32  0F 8C 3C 09 00 00               jl 0x14024c374
0024BA38  44 8B 53 78                     mov r10d, dword ptr [rbx + 0x78]
0024BA3C  44 89 54 24 34                  mov dword ptr [rsp + 0x34], r10d
0024BA41  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0024BA45  0F 85 6D 0E 00 00               jne 0x14024c8b8
0024BA4B  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
0024BA4F  48 8B D0                        mov rdx, rax
0024BA52  4D 85 ED                        test r13, r13
0024BA55  74 09                           je 0x14024ba60
0024BA57  45 03 55 68                     add r10d, dword ptr [r13 + 0x68]
0024BA5B  44 89 54 24 34                  mov dword ptr [rsp + 0x34], r10d
0024BA60  83 FD 06                        cmp ebp, 6
0024BA63  74 61                           je 0x14024bac6
0024BA65  44 89 54 24 34                  mov dword ptr [rsp + 0x34], r10d
0024BA6A  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
0024BA6E  83 FD 05                        cmp ebp, 5
0024BA71  0F 87 B3 0B 00 00               ja 0x14024c62a
0024BA77  80 BC 32 30 10 00 00 01         cmp byte ptr [rdx + rsi + 0x1030], 1
0024BA7F  0F 85 A5 0B 00 00               jne 0x14024c62a
0024BA85  48 8B 4C EB 48                  mov rcx, qword ptr [rbx + rbp*8 + 0x48]
0024BA8A  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
0024BA8E  44 89 54 24 34                  mov dword ptr [rsp + 0x34], r10d
0024BA93  48 63 01                        movsxd rax, dword ptr [rcx]
0024BA96  A8 04                           test al, 4
0024BA98  0F 84 96 0B 00 00               je 0x14024c634
0024BA9E  83 E0 FB                        and eax, 0xfffffffb
0024BAA1  89 01                           mov dword ptr [rcx], eax
0024BAA3  48 8D 0D 46 1B 00 00            lea rcx, [rip + 0x1b46]
0024BAAA  48 8B 84 32 B0 10 00 00         mov rax, qword ptr [rdx + rsi + 0x10b0]
0024BAB2  49 8B D5                        mov rdx, r13
0024BAB5  48 3B C1                        cmp rax, rcx
0024BAB8  0F 85 43 09 00 00               jne 0x14024c401
0024BABE  48 8B CB                        mov rcx, rbx
0024BAC1  E8 2A 1B 00 00                  call 0x14024d5f0
0024BAC6  BA 01 00 00 00                  mov edx, 1
0024BACB  41 83 FE 06                     cmp r14d, 6
0024BACF  0F 84 D5 00 00 00               je 0x14024bbaa
0024BAD5  49 69 C6 88 00 00 00            imul rax, r14, 0x88
0024BADC  4D 8B D6                        mov r10, r14
0024BADF  8B 8C 30 34 10 00 00            mov ecx, dword ptr [rax + rsi + 0x1034]
0024BAE6  85 C9                           test ecx, ecx
0024BAE8  0F 85 4E 07 00 00               jne 0x14024c23c
0024BAEE  41 83 FE 05                     cmp r14d, 5
0024BAF2  77 15                           ja 0x14024bb09
0024BAF4  49 69 C2 88 00 00 00            imul rax, r10, 0x88
0024BAFB  80 BC 30 30 10 00 00 01         cmp byte ptr [rax + rsi + 0x1030], 1
0024BB03  0F 84 45 0E 00 00               je 0x14024c94e
0024BB09  41 8B CC                        mov ecx, r12d
0024BB0C  49 8D 45 38                     lea rax, [r13 + 0x38]
0024BB10  83 F9 01                        cmp ecx, 1
0024BB13  4C 8D 5B 48                     lea r11, [rbx + 0x48]
0024BB17  41 8B D4                        mov edx, r12d
0024BB1A  4C 0F 45 D8                     cmovne r11, rax
0024BB1E  49 8B C4                        mov rax, r12
0024BB21  83 FA 06                        cmp edx, 6
0024BB24  7D 27                           jge 0x14024bb4d
0024BB26  4D 8B 04 C3                     mov r8, qword ptr [r11 + rax*8]
0024BB2A  4D 85 C0                        test r8, r8
0024BB2D  74 17                           je 0x14024bb46
0024BB2F  49 6B CA 22                     imul rcx, r10, 0x22
0024BB33  48 03 C8                        add rcx, rax
0024BB36  8B 8C 8E 40 10 00 00            mov ecx, dword ptr [rsi + rcx*4 + 0x1040]
0024BB3D  41 85 08                        test dword ptr [r8], ecx
0024BB40  0F 85 07 11 00 00               jne 0x14024cc4d
0024BB46  FF C2                           inc edx
0024BB48  48 FF C0                        inc rax
0024BB4B  EB D4                           jmp 0x14024bb21
0024BB4D  4D 85 ED                        test r13, r13
0024BB50  0F 84 48 0E 00 00               je 0x14024c99e
0024BB56  4B 8B 44 F5 38                  mov rax, qword ptr [r13 + r14*8 + 0x38]
0024BB5B  83 08 01                        or dword ptr [rax], 1
0024BB5E  48 8D 0D 2B 1C 00 00            lea rcx, [rip + 0x1c2b]
0024BB65  44 89 60 04                     mov dword ptr [rax + 4], r12d
0024BB69  45 33 C0                        xor r8d, r8d
0024BB6C  49 69 C2 88 00 00 00            imul rax, r10, 0x88
0024BB73  49 8B D5                        mov rdx, r13
0024BB76  48 8B 84 30 A0 10 00 00         mov rax, qword ptr [rax + rsi + 0x10a0]
0024BB7E  48 3B C1                        cmp rax, rcx
0024BB81  74 1A                           je 0x14024bb9d
0024BB83  48 8D 0D D6 1C 00 00            lea rcx, [rip + 0x1cd6]
0024BB8A  48 3B C1                        cmp rax, rcx
0024BB8D  0F 85 1C 0C 00 00               jne 0x14024c7af
0024BB93  48 8B CB                        mov rcx, rbx
0024BB96  E8 C5 1C 00 00                  call 0x14024d860
0024BB9B  EB 08                           jmp 0x14024bba5
0024BB9D  48 8B CB                        mov rcx, rbx
0024BBA0  E8 EB 1B 00 00                  call 0x14024d790
0024BBA5  BA 01 00 00 00                  mov edx, 1
0024BBAA  44 8B F7                        mov r14d, edi
0024BBAD  4D 8B FD                        mov r15, r13
0024BBB0  85 FF                           test edi, edi
0024BBB2  0F 84 5C 04 00 00               je 0x14024c014
0024BBB8  4D 85 ED                        test r13, r13
0024BBBB  0F 84 8E 0E 00 00               je 0x14024ca4f
0024BBC1  48 8B 73 48                     mov rsi, qword ptr [rbx + 0x48]
0024BBC5  4C 8D 4B 48                     lea r9, [rbx + 0x48]
0024BBC9  48 8D 0D A0 54 DB FF            lea rcx, [rip - 0x24ab60]
0024BBD0  44 8B 1E                        mov r11d, dword ptr [rsi]
0024BBD3  41 F6 C3 01                     test r11b, 1
0024BBD7  0F 84 FB 00 00 00               je 0x14024bcd8
0024BBDD  0F B6 6E 10                     movzx ebp, byte ptr [rsi + 0x10]
0024BBE1  4C 8D 05 A0 54 DB FF            lea r8, [rip - 0x24ab60]
0024BBE8  40 84 ED                        test bpl, bpl
0024BBEB  41 8B D4                        mov edx, r12d
0024BBEE  4C 0F 44 C1                     cmove r8, rcx
0024BBF2  85 D2                           test edx, edx
0024BBF4  7F 20                           jg 0x14024bc16
0024BBF6  45 8B 10                        mov r10d, dword ptr [r8]
0024BBF9  45 85 D2                        test r10d, r10d
0024BBFC  74 0C                           je 0x14024bc0a
0024BBFE  49 8B 01                        mov rax, qword ptr [r9]
0024BC01  44 85 10                        test dword ptr [rax], r10d
0024BC04  0F 85 CE 00 00 00               jne 0x14024bcd8
0024BC0A  FF C2                           inc edx
0024BC0C  49 83 C1 08                     add r9, 8
0024BC10  49 83 C0 04                     add r8, 4
0024BC14  EB DC                           jmp 0x14024bbf2
0024BC16  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
0024BC1A  44 8B 8B B4 00 00 00            mov r9d, dword ptr [rbx + 0xb4]
0024BC21  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0024BC25  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
0024BC29  48 8D 05 44 54 DB FF            lea rax, [rip - 0x24abbc]
0024BC30  45 85 C9                        test r9d, r9d
0024BC33  75 4C                           jne 0x14024bc81
0024BC35  B9 01 00 00 00                  mov ecx, 1
0024BC3A  48 8D 15 4B 54 DB FF            lea rdx, [rip - 0x24abb5]
0024BC41  40 84 ED                        test bpl, bpl
0024BC44  44 8B C1                        mov r8d, ecx
0024BC47  44 8B D1                        mov r10d, ecx
0024BC4A  48 0F 44 D0                     cmove rdx, rax
0024BC4E  41 83 F8 03                     cmp r8d, 3
0024BC52  7F 28                           jg 0x14024bc7c
0024BC54  8B 3A                           mov edi, dword ptr [rdx]
0024BC56  85 FF                           test edi, edi
0024BC58  74 16                           je 0x14024bc70
0024BC5A  41 8B C1                        mov eax, r9d
0024BC5D  48 6B C0 1A                     imul rax, rax, 0x1a
0024BC61  49 03 C2                        add rax, r10
0024BC64  48 8B 84 C3 F8 00 00 00         mov rax, qword ptr [rbx + rax*8 + 0xf8]
0024BC6C  85 38                           test dword ptr [rax], edi
0024BC6E  75 68                           jne 0x14024bcd8
0024BC70  41 FF C0                        inc r8d
0024BC73  49 FF C2                        inc r10
0024BC76  48 83 C2 04                     add rdx, 4
0024BC7A  EB D2                           jmp 0x14024bc4e
0024BC7C  41 FF C1                        inc r9d
0024BC7F  EB A8                           jmp 0x14024bc29
0024BC81  40 84 ED                        test bpl, bpl
0024BC84  48 8D 15 0D 54 DB FF            lea rdx, [rip - 0x24abf3]
0024BC8B  48 8D 05 EE 53 DB FF            lea rax, [rip - 0x24ac12]
0024BC92  41 B8 04 00 00 00               mov r8d, 4
0024BC98  48 0F 44 D0                     cmove rdx, rax
0024BC9C  4C 8D 4B 68                     lea r9, [rbx + 0x68]
0024BCA0  41 83 F8 05                     cmp r8d, 5
0024BCA4  7F 1D                           jg 0x14024bcc3
0024BCA6  44 8B 12                        mov r10d, dword ptr [rdx]
0024BCA9  45 85 D2                        test r10d, r10d
0024BCAC  74 08                           je 0x14024bcb6
0024BCAE  49 8B 01                        mov rax, qword ptr [r9]
0024BCB1  44 85 10                        test dword ptr [rax], r10d
0024BCB4  75 22                           jne 0x14024bcd8
0024BCB6  41 FF C0                        inc r8d
0024BCB9  49 83 C1 08                     add r9, 8
0024BCBD  48 83 C2 04                     add rdx, 4
0024BCC1  EB DD                           jmp 0x14024bca0
0024BCC3  8B 46 04                        mov eax, dword ptr [rsi + 4]
0024BCC6  41 83 E3 FE                     and r11d, 0xfffffffe
0024BCCA  41 83 CB 02                     or r11d, 2
0024BCCE  89 46 08                        mov dword ptr [rsi + 8], eax
0024BCD1  44 89 1E                        mov dword ptr [rsi], r11d
0024BCD4  F0 FF 43 78                     lock inc dword ptr [rbx + 0x78]
0024BCD8  41 83 FE 02                     cmp r14d, 2
0024BCDC  0F 85 8D 0C 00 00               jne 0x14024c96f
0024BCE2  45 8B 45 08                     mov r8d, dword ptr [r13 + 8]
0024BCE6  41 8B D0                        mov edx, r8d
0024BCE9  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
0024BCED  44 89 44 24 3C                  mov dword ptr [rsp + 0x3c], r8d
0024BCF2  4C 8D 4B 48                     lea r9, [rbx + 0x48]
0024BCF6  8B C2                           mov eax, edx
0024BCF8  4C 8D 3D C1 53 DB FF            lea r15, [rip - 0x24ac3f]
0024BCFF  48 69 F8 D0 00 00 00            imul rdi, rax, 0xd0
0024BD06  B9 03 00 00 00                  mov ecx, 3
0024BD0B  BD 88 00 00 00                  mov ebp, 0x88
0024BD10  48 81 C7 C0 00 00 00            add rdi, 0xc0
0024BD17  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0024BD1C  48 03 FB                        add rdi, rbx
0024BD1F  41 BE 40 00 00 00               mov r14d, 0x40
0024BD25  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0024BD2A  4D 8B 24 3E                     mov r12, qword ptr [r14 + rdi]
0024BD2E  45 8B 2C 24                     mov r13d, dword ptr [r12]
0024BD32  41 F6 C5 01                     test r13b, 1
0024BD36  0F 84 59 01 00 00               je 0x14024be95
0024BD3C  45 8B 1F                        mov r11d, dword ptr [r15]
0024BD3F  45 85 DB                        test r11d, r11d
0024BD42  0F 84 E8 0C 00 00               je 0x14024ca30
0024BD48  41 0F B6 4C 24 10               movzx ecx, byte ptr [r12 + 0x10]
0024BD4E  48 8D 1D 1B 53 DB FF            lea rbx, [rip - 0x24ace5]
0024BD55  33 F6                           xor esi, esi
0024BD57  88 8C 24 C0 00 00 00            mov byte ptr [rsp + 0xc0], cl
0024BD5E  84 C9                           test cl, cl
0024BD60  48 8D 15 21 53 DB FF            lea rdx, [rip - 0x24acdf]
0024BD67  44 8B C6                        mov r8d, esi
0024BD6A  4D 8B D1                        mov r10, r9
0024BD6D  48 0F 44 D3                     cmove rdx, rbx
0024BD71  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
0024BD79  48 03 D5                        add rdx, rbp
0024BD7C  45 85 C0                        test r8d, r8d
0024BD7F  7F 21                           jg 0x14024bda2
0024BD81  44 8B 0A                        mov r9d, dword ptr [rdx]
0024BD84  45 85 C9                        test r9d, r9d
0024BD87  74 0C                           je 0x14024bd95
0024BD89  49 8B 02                        mov rax, qword ptr [r10]
0024BD8C  44 85 08                        test dword ptr [rax], r9d
0024BD8F  0F 85 EE 00 00 00               jne 0x14024be83
0024BD95  41 FF C0                        inc r8d
0024BD98  49 83 C2 08                     add r10, 8
0024BD9C  48 83 C2 04                     add rdx, 4
0024BDA0  EB DA                           jmp 0x14024bd7c
0024BDA2  41 83 FB 02                     cmp r11d, 2
0024BDA6  0F 85 20 0A 00 00               jne 0x14024c7cc
0024BDAC  8B 7F 08                        mov edi, dword ptr [rdi + 8]
0024BDAF  44 8B DF                        mov r11d, edi
0024BDB2  80 F9 00                        cmp cl, 0
0024BDB5  48 8D 35 CC 52 DB FF            lea rsi, [rip - 0x24ad34]
0024BDBC  48 8D 0D AD 52 DB FF            lea rcx, [rip - 0x24ad53]
0024BDC3  48 0F 44 F1                     cmove rsi, rcx
0024BDC7  48 83 C6 04                     add rsi, 4
0024BDCB  44 3B DF                        cmp r11d, edi
0024BDCE  77 46                           ja 0x14024be16
0024BDD0  B8 01 00 00 00                  mov eax, 1
0024BDD5  4C 8D 04 2E                     lea r8, [rsi + rbp]
0024BDD9  8B D0                           mov edx, eax
0024BDDB  44 8B D0                        mov r10d, eax
0024BDDE  83 FA 03                        cmp edx, 3
0024BDE1  7F 2E                           jg 0x14024be11
0024BDE3  45 8B 08                        mov r9d, dword ptr [r8]
0024BDE6  45 85 C9                        test r9d, r9d
0024BDE9  74 1B                           je 0x14024be06
0024BDEB  41 8B C3                        mov eax, r11d
0024BDEE  48 6B C0 1A                     imul rax, rax, 0x1a
0024BDF2  49 03 C2                        add rax, r10
0024BDF5  48 8B 84 C3 F8 00 00 00         mov rax, qword ptr [rbx + rax*8 + 0xf8]
0024BDFD  44 85 08                        test dword ptr [rax], r9d
0024BE00  0F 85 54 08 00 00               jne 0x14024c65a
0024BE06  FF C2                           inc edx
0024BE08  49 FF C2                        inc r10
0024BE0B  49 83 C0 04                     add r8, 4
0024BE0F  EB CD                           jmp 0x14024bdde
0024BE11  41 FF C3                        inc r11d
0024BE14  EB B5                           jmp 0x14024bdcb
0024BE16  80 BC 24 C0 00 00 00 00         cmp byte ptr [rsp + 0xc0], 0
0024BE1E  48 8D 15 73 52 DB FF            lea rdx, [rip - 0x24ad8d]
0024BE25  48 8D 05 54 52 DB FF            lea rax, [rip - 0x24adac]
0024BE2C  41 B8 04 00 00 00               mov r8d, 4
0024BE32  48 0F 44 D0                     cmove rdx, rax
0024BE36  4C 8D 53 68                     lea r10, [rbx + 0x68]
0024BE3A  48 03 D5                        add rdx, rbp
0024BE3D  41 83 F8 05                     cmp r8d, 5
0024BE41  7F 21                           jg 0x14024be64
0024BE43  44 8B 0A                        mov r9d, dword ptr [rdx]
0024BE46  45 85 C9                        test r9d, r9d
0024BE49  74 0C                           je 0x14024be57
0024BE4B  49 8B 02                        mov rax, qword ptr [r10]
0024BE4E  44 85 08                        test dword ptr [rax], r9d
0024BE51  0F 85 03 08 00 00               jne 0x14024c65a
0024BE57  41 FF C0                        inc r8d
0024BE5A  49 83 C2 08                     add r10, 8
0024BE5E  48 83 C2 04                     add rdx, 4
0024BE62  EB D9                           jmp 0x14024be3d
0024BE64  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
0024BE69  41 83 E5 FE                     and r13d, 0xfffffffe
0024BE6D  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0024BE72  41 83 CD 02                     or r13d, 2
0024BE76  45 89 2C 24                     mov dword ptr [r12], r13d
0024BE7A  41 89 44 24 08                  mov dword ptr [r12 + 8], eax
0024BE7F  F0 FF 47 68                     lock inc dword ptr [rdi + 0x68]
0024BE83  44 8B 44 24 3C                  mov r8d, dword ptr [rsp + 0x3c]
0024BE88  4C 8D 4B 48                     lea r9, [rbx + 0x48]
0024BE8C  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
0024BE90  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0024BE95  48 81 C5 88 00 00 00            add rbp, 0x88
0024BE9C  49 83 C6 08                     add r14, 8
0024BEA0  49 81 C7 88 00 00 00            add r15, 0x88
0024BEA7  48 83 E9 01                     sub rcx, 1
0024BEAB  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0024BEB0  0F 85 74 FE FF FF               jne 0x14024bd2a
0024BEB6  FF C2                           inc edx
0024BEB8  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
0024BEBC  41 3B D0                        cmp edx, r8d
0024BEBF  0F 86 31 FE FF FF               jbe 0x14024bcf6
0024BEC5  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0024BECA  45 33 E4                        xor r12d, r12d
0024BECD  4C 8B AC 24 A8 00 00 00         mov r13, qword ptr [rsp + 0xa8]
0024BED5  48 8B 4B 68                     mov rcx, qword ptr [rbx + 0x68]
0024BED9  4C 8D 53 48                     lea r10, [rbx + 0x48]
0024BEDD  8B 01                           mov eax, dword ptr [rcx]
0024BEDF  A8 01                           test al, 1
0024BEE1  74 12                           je 0x14024bef5
0024BEE3  83 E0 FE                        and eax, 0xfffffffe
0024BEE6  83 C8 02                        or eax, 2
0024BEE9  89 01                           mov dword ptr [rcx], eax
0024BEEB  8B 41 04                        mov eax, dword ptr [rcx + 4]
0024BEEE  89 41 08                        mov dword ptr [rcx + 8], eax
0024BEF1  F0 FF 43 78                     lock inc dword ptr [rbx + 0x78]
0024BEF5  48 8B 7B 70                     mov rdi, qword ptr [rbx + 0x70]
0024BEF9  8B 07                           mov eax, dword ptr [rdi]
0024BEFB  A8 01                           test al, 1
0024BEFD  0F 84 0D 01 00 00               je 0x14024c010
0024BF03  4C 8B 1D D6 53 DB FF            mov r11, qword ptr [rip - 0x24ac2a]
0024BF0A  45 85 DB                        test r11d, r11d
0024BF0D  0F 84 EB 00 00 00               je 0x14024bffe
0024BF13  0F B6 6F 10                     movzx ebp, byte ptr [rdi + 0x10]
0024BF17  48 8D 05 FA 53 DB FF            lea rax, [rip - 0x24ac06]
0024BF1E  40 84 ED                        test bpl, bpl
0024BF21  48 8D 15 08 54 DB FF            lea rdx, [rip - 0x24abf8]
0024BF28  45 8B C4                        mov r8d, r12d
0024BF2B  48 0F 44 D0                     cmove rdx, rax
0024BF2F  45 85 C0                        test r8d, r8d
0024BF32  7F 21                           jg 0x14024bf55
0024BF34  44 8B 0A                        mov r9d, dword ptr [rdx]
0024BF37  45 85 C9                        test r9d, r9d
0024BF3A  74 0C                           je 0x14024bf48
0024BF3C  49 8B 02                        mov rax, qword ptr [r10]
0024BF3F  44 85 08                        test dword ptr [rax], r9d
0024BF42  0F 85 C8 00 00 00               jne 0x14024c010
0024BF48  41 FF C0                        inc r8d
0024BF4B  49 83 C2 08                     add r10, 8
0024BF4F  48 83 C2 04                     add rdx, 4
0024BF53  EB DA                           jmp 0x14024bf2f
0024BF55  41 83 FB 02                     cmp r11d, 2
0024BF59  0F 85 F6 09 00 00               jne 0x14024c955
0024BF5F  45 8B 4F 08                     mov r9d, dword ptr [r15 + 8]
0024BF63  41 8B D1                        mov edx, r9d
0024BF66  4C 8D 35 AF 53 DB FF            lea r14, [rip - 0x24ac51]
0024BF6D  41 3B D1                        cmp edx, r9d
0024BF70  77 4B                           ja 0x14024bfbd
0024BF72  B8 01 00 00 00                  mov eax, 1
0024BF77  4C 8D 15 B6 53 DB FF            lea r10, [rip - 0x24ac4a]
0024BF7E  40 84 ED                        test bpl, bpl
0024BF81  44 8B C0                        mov r8d, eax
0024BF84  44 8B D8                        mov r11d, eax
0024BF87  4D 0F 44 D6                     cmove r10, r14
0024BF8B  41 83 F8 03                     cmp r8d, 3
0024BF8F  7F 28                           jg 0x14024bfb9
0024BF91  41 8B 32                        mov esi, dword ptr [r10]
0024BF94  85 F6                           test esi, esi
0024BF96  74 15                           je 0x14024bfad
0024BF98  8B C2                           mov eax, edx
0024BF9A  48 6B C0 1A                     imul rax, rax, 0x1a
0024BF9E  49 03 C3                        add rax, r11
0024BFA1  48 8B 84 C3 F8 00 00 00         mov rax, qword ptr [rbx + rax*8 + 0xf8]
0024BFA9  85 30                           test dword ptr [rax], esi
0024BFAB  75 63                           jne 0x14024c010
0024BFAD  41 FF C0                        inc r8d
0024BFB0  49 FF C3                        inc r11
0024BFB3  49 83 C2 04                     add r10, 4
0024BFB7  EB D2                           jmp 0x14024bf8b
0024BFB9  FF C2                           inc edx
0024BFBB  EB B0                           jmp 0x14024bf6d
0024BFBD  40 84 ED                        test bpl, bpl
0024BFC0  48 8D 05 61 53 DB FF            lea rax, [rip - 0x24ac9f]
0024BFC7  4C 8D 05 72 53 DB FF            lea r8, [rip - 0x24ac8e]
0024BFCE  BA 04 00 00 00                  mov edx, 4
0024BFD3  4C 0F 44 C0                     cmove r8, rax
0024BFD7  4C 8D 4B 68                     lea r9, [rbx + 0x68]
0024BFDB  83 FA 05                        cmp edx, 5
0024BFDE  7F 1C                           jg 0x14024bffc
0024BFE0  45 8B 10                        mov r10d, dword ptr [r8]
0024BFE3  45 85 D2                        test r10d, r10d
0024BFE6  74 08                           je 0x14024bff0
0024BFE8  49 8B 01                        mov rax, qword ptr [r9]
0024BFEB  44 85 10                        test dword ptr [rax], r10d
0024BFEE  75 20                           jne 0x14024c010
0024BFF0  FF C2                           inc edx
0024BFF2  49 83 C1 08                     add r9, 8
0024BFF6  49 83 C0 04                     add r8, 4
0024BFFA  EB DF                           jmp 0x14024bfdb
0024BFFC  8B 07                           mov eax, dword ptr [rdi]
0024BFFE  83 E0 FE                        and eax, 0xfffffffe
0024C001  83 C8 02                        or eax, 2
0024C004  89 07                           mov dword ptr [rdi], eax
0024C006  8B 47 04                        mov eax, dword ptr [rdi + 4]
0024C009  89 47 08                        mov dword ptr [rdi + 8], eax
0024C00C  F0 FF 43 78                     lock inc dword ptr [rbx + 0x78]
0024C010  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
0024C014  4C 8B BC 24 C8 00 00 00         mov r15, qword ptr [rsp + 0xc8]
0024C01C  40 32 ED                        xor bpl, bpl
0024C01F  4D 85 FF                        test r15, r15
0024C022  0F 85 A5 02 00 00               jne 0x14024c2cd
0024C028  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
0024C02C  41 BE 01 00 00 00               mov r14d, 1
0024C032  85 FF                           test edi, edi
0024C034  0F 84 59 0B 00 00               je 0x14024cb93
0024C03A  8B 43 78                        mov eax, dword ptr [rbx + 0x78]
0024C03D  83 FF 02                        cmp edi, 2
0024C040  0F 85 C6 08 00 00               jne 0x14024c90c
0024C046  4D 85 ED                        test r13, r13
0024C049  74 04                           je 0x14024c04f
0024C04B  41 03 45 68                     add eax, dword ptr [r13 + 0x68]
0024C04F  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
0024C053  45 32 E4                        xor r12b, r12b
0024C056  F6 C1 01                        test cl, 1
0024C059  75 15                           jne 0x14024c070
0024C05B  85 C0                           test eax, eax
0024C05D  75 11                           jne 0x14024c070
0024C05F  40 84 ED                        test bpl, bpl
0024C062  75 0C                           jne 0x14024c070
0024C064  39 83 8C 00 00 00               cmp dword ptr [rbx + 0x8c], eax
0024C06A  0F 84 89 0A 00 00               je 0x14024caf9
0024C070  83 E1 20                        and ecx, 0x20
0024C073  3B C6                           cmp eax, esi
0024C075  0F 87 E7 04 00 00               ja 0x14024c562
0024C07B  80 BC 24 B0 00 00 00 01         cmp byte ptr [rsp + 0xb0], 1
0024C083  0F 85 08 03 00 00               jne 0x14024c391
0024C089  45 33 F6                        xor r14d, r14d
0024C08C  41 8B CE                        mov ecx, r14d
0024C08F  90                              nop
0024C090  83 F9 06                        cmp ecx, 6
0024C093  73 19                           jae 0x14024c0ae
0024C095  8B C1                           mov eax, ecx
0024C097  48 8B 54 C3 48                  mov rdx, qword ptr [rbx + rax*8 + 0x48]
0024C09C  48 85 D2                        test rdx, rdx
0024C09F  74 09                           je 0x14024c0aa
0024C0A1  44 39 32                        cmp dword ptr [rdx], r14d
0024C0A4  0F 85 23 0B 00 00               jne 0x14024cbcd
0024C0AA  FF C1                           inc ecx
0024C0AC  EB E2                           jmp 0x14024c090
0024C0AE  44 38 B3 88 00 00 00            cmp byte ptr [rbx + 0x88], r14b
0024C0B5  74 04                           je 0x14024c0bb
0024C0B7  44 88 73 7D                     mov byte ptr [rbx + 0x7d], r14b
0024C0BB  F6 05 44 AA D7 00 01            test byte ptr [rip + 0xd7aa44], 1
0024C0C2  48 8D 7B 40                     lea rdi, [rbx + 0x40]
0024C0C6  0F 85 17 0B 00 00               jne 0x14024cbe3
0024C0CC  44 89 37                        mov dword ptr [rdi], r14d
0024C0CF  44 39 35 4A AC D7 00            cmp dword ptr [rip + 0xd7ac4a], r14d
0024C0D6  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
0024C0DB  74 11                           je 0x14024c0ee
0024C0DD  44 0F 20 C1                     mov rcx, cr8
0024C0E1  40 0F B6 D6                     movzx edx, sil
0024C0E5  E8 AE 95 2A 00                  call 0x1404f5698
0024C0EA  48 8D 7B 40                     lea rdi, [rbx + 0x40]
0024C0EE  40 0F B6 C6                     movzx eax, sil
0024C0F2  44 0F 22 C0                     mov cr8, rax
0024C0F6  45 84 E4                        test r12b, r12b
0024C0F9  0F 84 20 01 00 00               je 0x14024c21f
0024C0FF  40 32 ED                        xor bpl, bpl
0024C102  44 0F 20 C6                     mov rsi, cr8
0024C106  B8 02 00 00 00                  mov eax, 2
0024C10B  44 0F 22 C0                     mov cr8, rax
0024C10F  83 3D 0A AC D7 00 00            cmp dword ptr [rip + 0xd7ac0a], 0
0024C116  0F 85 35 04 00 00               jne 0x14024c551
0024C11C  F6 05 E3 A9 D7 00 21            test byte ptr [rip + 0xd7a9e3], 0x21
0024C123  0F 85 15 03 00 00               jne 0x14024c43e
0024C129  F0 0F BA 2F 1F                  lock bts dword ptr [rdi], 0x1f
0024C12E  73 0F                           jae 0x14024c13f
0024C130  40 0F B6 D6                     movzx edx, sil
0024C134  48 8B CF                        mov rcx, rdi
0024C137  E8 64 78 0D 00                  call 0x1403239a0
0024C13C  44 8B F0                        mov r14d, eax
0024C13F  8B 17                           mov edx, dword ptr [rdi]
0024C141  8B CA                           mov ecx, edx
0024C143  0F BA F1 1E                     btr ecx, 0x1e
0024C147  81 F9 00 00 00 80               cmp ecx, 0x80000000
0024C14D  74 2E                           je 0x14024c17d
0024C14F  0F BA E2 1E                     bt edx, 0x1e
0024C153  72 07                           jb 0x14024c15c
0024C155  F0 81 0F 00 00 00 40            lock or dword ptr [rdi], 0x40000000
0024C15C  41 FF C6                        inc r14d
0024C15F  44 85 35 46 91 D7 00            test dword ptr [rip + 0xd79146], r14d
0024C166  0F 84 C8 09 00 00               je 0x14024cb34
0024C16C  F3 90                           pause
0024C16E  8B 17                           mov edx, dword ptr [rdi]
0024C170  8B C2                           mov eax, edx
0024C172  0F BA F0 1E                     btr eax, 0x1e
0024C176  3D 00 00 00 80                  cmp eax, 0x80000000
0024C17B  75 D2                           jne 0x14024c14f
0024C17D  F6 43 18 01                     test byte ptr [rbx + 0x18], 1
0024C181  C6 43 7D 01                     mov byte ptr [rbx + 0x7d], 1
0024C185  0F 85 83 00 00 00               jne 0x14024c20e
0024C18B  83 BB 8C 00 00 00 00            cmp dword ptr [rbx + 0x8c], 0
0024C192  75 7A                           jne 0x14024c20e
0024C194  40 38 AB 88 00 00 00            cmp byte ptr [rbx + 0x88], bpl
0024C19B  74 71                           je 0x14024c20e
0024C19D  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
0024C1A1  83 38 00                        cmp dword ptr [rax], 0
0024C1A4  75 68                           jne 0x14024c20e
0024C1A6  48 8B 43 70                     mov rax, qword ptr [rbx + 0x70]
0024C1AA  83 38 00                        cmp dword ptr [rax], 0
0024C1AD  75 5F                           jne 0x14024c20e
0024C1AF  44 8B 73 78                     mov r14d, dword ptr [rbx + 0x78]
0024C1B3  48 8D 7B 78                     lea rdi, [rbx + 0x78]
0024C1B7  45 33 C9                        xor r9d, r9d
0024C1BA  33 D2                           xor edx, edx
0024C1BC  48 8B CB                        mov rcx, rbx
0024C1BF  45 8D 41 04                     lea r8d, [r9 + 4]
0024C1C3  E8 E8 0B 00 00                  call 0x14024cdb0
0024C1C8  33 D2                           xor edx, edx
0024C1CA  48 8B CB                        mov rcx, rbx
0024C1CD  44 8D 42 01                     lea r8d, [rdx + 1]
0024C1D1  E8 FA 0E 00 00                  call 0x14024d0d0
0024C1D6  44 8B 07                        mov r8d, dword ptr [rdi]
0024C1D9  4D 85 FF                        test r15, r15
0024C1DC  0F 84 7B 02 00 00               je 0x14024c45d
0024C1E2  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
0024C1E6  83 38 02                        cmp dword ptr [rax], 2
0024C1E9  0F 85 6E 02 00 00               jne 0x14024c45d
0024C1EF  33 D2                           xor edx, edx
0024C1F1  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0024C1F6  4C 8D 43 48                     lea r8, [rbx + 0x48]
0024C1FA  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0024C1FF  48 8B CB                        mov rcx, rbx
0024C202  44 8D 4A 04                     lea r9d, [rdx + 4]
0024C206  E8 D5 14 00 00                  call 0x14024d6e0
0024C20B  0F B6 E8                        movzx ebp, al
0024C20E  44 0F B6 CE                     movzx r9d, sil
0024C212  41 B0 01                        mov r8b, 1
0024C215  33 D2                           xor edx, edx
0024C217  48 8B CB                        mov rcx, rbx
0024C21A  E8 71 0A 00 00                  call 0x14024cc90
0024C21F  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
0024C227  40 0F B6 C5                     movzx eax, bpl
0024C22B  48 83 C4 60                     add rsp, 0x60
0024C22F  41 5F                           pop r15
0024C231  41 5E                           pop r14
0024C233  41 5D                           pop r13
0024C235  41 5C                           pop r12
0024C237  5F                              pop rdi
0024C238  5E                              pop rsi
0024C239  5D                              pop rbp
0024C23A  C3                              ret
0024C23B  CC                              int3
0024C23C  3B CA                           cmp ecx, edx
0024C23E  0F 85 20 04 00 00               jne 0x14024c664
0024C244  49 6B D2 22                     imul rdx, r10, 0x22
0024C248  8B 8C 96 58 10 00 00            mov ecx, dword ptr [rsi + rdx*4 + 0x1058]
0024C24F  85 C9                           test ecx, ecx
0024C251  75 20                           jne 0x14024c273
0024C253  8B 8C 96 68 10 00 00            mov ecx, dword ptr [rsi + rdx*4 + 0x1068]
0024C25A  85 C9                           test ecx, ecx
0024C25C  75 34                           jne 0x14024c292
0024C25E  8B 8C 96 6C 10 00 00            mov ecx, dword ptr [rsi + rdx*4 + 0x106c]
0024C265  85 C9                           test ecx, ecx
0024C267  75 48                           jne 0x14024c2b1
0024C269  BA 01 00 00 00                  mov edx, 1
0024C26E  E9 7B F8 FF FF                  jmp 0x14024baee
0024C273  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
0024C277  44 8B 00                        mov r8d, dword ptr [rax]
0024C27A  44 85 C1                        test ecx, r8d
0024C27D  74 D4                           je 0x14024c253
0024C27F  41 F6 C0 02                     test r8b, 2
0024C283  74 04                           je 0x14024c289
0024C285  F0 FF 4B 78                     lock dec dword ptr [rbx + 0x78]
0024C289  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
0024C28D  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024C290  EB C1                           jmp 0x14024c253
0024C292  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
0024C296  44 8B 00                        mov r8d, dword ptr [rax]
0024C299  44 85 C1                        test ecx, r8d
0024C29C  74 C0                           je 0x14024c25e
0024C29E  41 F6 C0 02                     test r8b, 2
0024C2A2  74 04                           je 0x14024c2a8
0024C2A4  F0 FF 4B 78                     lock dec dword ptr [rbx + 0x78]
0024C2A8  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
0024C2AC  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024C2AF  EB AD                           jmp 0x14024c25e
0024C2B1  48 8B 43 70                     mov rax, qword ptr [rbx + 0x70]
0024C2B5  8B 10                           mov edx, dword ptr [rax]
0024C2B7  85 D1                           test ecx, edx
0024C2B9  74 AE                           je 0x14024c269
0024C2BB  F6 C2 02                        test dl, 2
0024C2BE  74 04                           je 0x14024c2c4
0024C2C0  F0 FF 4B 78                     lock dec dword ptr [rbx + 0x78]
0024C2C4  48 8B 43 70                     mov rax, qword ptr [rbx + 0x70]
0024C2C8  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024C2CB  EB 9C                           jmp 0x14024c269
0024C2CD  83 7B 78 00                     cmp dword ptr [rbx + 0x78], 0
0024C2D1  0F 87 DC 06 00 00               ja 0x14024c9b3
0024C2D7  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
0024C2DB  4D 85 ED                        test r13, r13
0024C2DE  0F 84 89 01 00 00               je 0x14024c46d
0024C2E4  41 83 7D 68 00                  cmp dword ptr [r13 + 0x68], 0
0024C2E9  0F 86 7E 01 00 00               jbe 0x14024c46d
0024C2EF  41 BE 01 00 00 00               mov r14d, 1
0024C2F5  49 8D 4D 40                     lea rcx, [r13 + 0x40]
0024C2F9  45 8B CE                        mov r9d, r14d
0024C2FC  41 83 F9 03                     cmp r9d, 3
0024C300  0F 8F FD 04 00 00               jg 0x14024c803
0024C306  48 8B 01                        mov rax, qword ptr [rcx]
0024C309  8B 10                           mov edx, dword ptr [rax]
0024C30B  F6 C2 02                        test dl, 2
0024C30E  0F 84 31 03 00 00               je 0x14024c645
0024C314  F0 41 FF 4D 68                  lock dec dword ptr [r13 + 0x68]
0024C319  48 8D 0D E0 3C DB FF            lea rcx, [rip - 0x24c320]
0024C320  49 63 F9                        movsxd rdi, r9d
0024C323  4D 8B C7                        mov r8, r15
0024C326  48 69 C7 88 00 00 00            imul rax, rdi, 0x88
0024C32D  49 8B D5                        mov rdx, r13
0024C330  48 8B 84 08 A8 10 00 00         mov rax, qword ptr [rax + rcx + 0x10a8]
0024C338  48 8D 0D 01 24 07 00            lea rcx, [rip + 0x72401]
0024C33F  48 3B C1                        cmp rax, rcx
0024C342  0F 85 9E 04 00 00               jne 0x14024c7e6
0024C348  48 8B CB                        mov rcx, rbx
0024C34B  E8 F0 23 07 00                  call 0x1402be740
0024C350  0F B6 E8                        movzx ebp, al
0024C353  49 8B 44 FD 38                  mov rax, qword ptr [r13 + rdi*8 + 0x38]
0024C358  83 20 FD                        and dword ptr [rax], 0xfffffffd
0024C35B  49 8B 44 FD 38                  mov rax, qword ptr [r13 + rdi*8 + 0x38]
0024C360  83 20 F7                        and dword ptr [rax], 0xfffffff7
0024C363  49 8B 44 FD 38                  mov rax, qword ptr [r13 + rdi*8 + 0x38]
0024C368  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
0024C36C  83 08 04                        or dword ptr [rax], 4
0024C36F  E9 BE FC FF FF                  jmp 0x14024c032
0024C374  44 8B 53 78                     mov r10d, dword ptr [rbx + 0x78]
0024C378  44 89 54 24 34                  mov dword ptr [rsp + 0x34], r10d
0024C37D  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
0024C385  49 69 C0 88 00 00 00            imul rax, r8, 0x88
0024C38C  E9 BA F6 FF FF                  jmp 0x14024ba4b
0024C391  F6 05 6E A7 D7 00 01            test byte ptr [rip + 0xd7a76e], 1
0024C398  0F 85 72 08 00 00               jne 0x14024cc10
0024C39E  45 33 F6                        xor r14d, r14d
0024C3A1  45 89 75 00                     mov dword ptr [r13], r14d
0024C3A5  48 8D 7B 40                     lea rdi, [rbx + 0x40]
0024C3A9  48 8B CF                        mov rcx, rdi
0024C3AC  E8 DF E1 FF FF                  call 0x14024a590
0024C3B1  83 3D 68 A9 D7 00 00            cmp dword ptr [rip + 0xd7a968], 0
0024C3B8  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
0024C3BD  0F 84 2B FD FF FF               je 0x14024c0ee
0024C3C3  44 0F 20 C1                     mov rcx, cr8
0024C3C7  40 0F B6 D6                     movzx edx, sil
0024C3CB  E8 C8 92 2A 00                  call 0x1404f5698
0024C3D0  E9 19 FD FF FF                  jmp 0x14024c0ee
0024C3D5  83 FD 06                        cmp ebp, 6
0024C3D8  0F 84 15 01 00 00               je 0x14024c4f3
0024C3DE  83 FD 05                        cmp ebp, 5
0024C3E1  0F 87 16 01 00 00               ja 0x14024c4fd
0024C3E7  48 69 CD 88 00 00 00            imul rcx, rbp, 0x88
0024C3EE  80 BC 31 30 10 00 00 01         cmp byte ptr [rcx + rsi + 0x1030], 1
0024C3F6  0F 84 87 F5 FF FF               je 0x14024b983
0024C3FC  E9 FC 00 00 00                  jmp 0x14024c4fd
0024C401  48 8D 0D A8 2D 07 00            lea rcx, [rip + 0x72da8]
0024C408  48 3B C1                        cmp rax, rcx
0024C40B  0F 85 FC 01 00 00               jne 0x14024c60d
0024C411  48 8B CB                        mov rcx, rbx
0024C414  E8 97 2D 07 00                  call 0x1402bf1b0
0024C419  E9 A8 F6 FF FF                  jmp 0x14024bac6
0024C41E  8B 05 34 1A CC 00               mov eax, dword ptr [rip + 0xcc1a34]
0024C424  85 C0                           test eax, eax
0024C426  0F 85 86 F5 FF FF               jne 0x14024b9b2
0024C42C  41 0F B6 D7                     movzx edx, r15b
0024C430  48 8D 4B 40                     lea rcx, [rbx + 0x40]
0024C434  E8 37 76 0D 00                  call 0x140323a70
0024C439  E9 D3 F5 FF FF                  jmp 0x14024ba11
0024C43E  8B 05 14 1A CC 00               mov eax, dword ptr [rip + 0xcc1a14]
0024C444  85 C0                           test eax, eax
0024C446  0F 85 DD FC FF FF               jne 0x14024c129
0024C44C  40 0F B6 D6                     movzx edx, sil
0024C450  48 8B CF                        mov rcx, rdi
0024C453  E8 18 76 0D 00                  call 0x140323a70
0024C458  E9 20 FD FF FF                  jmp 0x14024c17d
0024C45D  41 8B D6                        mov edx, r14d
0024C460  48 8B CB                        mov rcx, rbx
0024C463  E8 88 C2 14 00                  call 0x1403986f0
0024C468  E9 A1 FD FF FF                  jmp 0x14024c20e
0024C46D  80 7B 7D 01                     cmp byte ptr [rbx + 0x7d], 1
0024C471  75 2A                           jne 0x14024c49d
0024C473  44 8B 83 B4 00 00 00            mov r8d, dword ptr [rbx + 0xb4]
0024C47A  41 8B D4                        mov edx, r12d
0024C47D  41 3B D0                        cmp edx, r8d
0024C480  73 1B                           jae 0x14024c49d
0024C482  8B C2                           mov eax, edx
0024C484  48 69 C0 D0 00 00 00            imul rax, rax, 0xd0
0024C48B  83 BC 18 28 01 00 00 00         cmp dword ptr [rax + rbx + 0x128], 0
0024C493  0F 87 F0 05 00 00               ja 0x14024ca89
0024C499  FF C2                           inc edx
0024C49B  EB E0                           jmp 0x14024c47d
0024C49D  83 7B 78 00                     cmp dword ptr [rbx + 0x78], 0
0024C4A1  0F 86 85 FB FF FF               jbe 0x14024c02c
0024C4A7  44 8B 83 B4 00 00 00            mov r8d, dword ptr [rbx + 0xb4]
0024C4AE  41 8B D4                        mov edx, r12d
0024C4B1  41 3B D0                        cmp edx, r8d
0024C4B4  0F 82 B1 07 00 00               jb 0x14024cc6b
0024C4BA  BA 04 00 00 00                  mov edx, 4
0024C4BF  48 8D 4B 48                     lea rcx, [rbx + 0x48]
0024C4C3  44 8D 42 01                     lea r8d, [rdx + 1]
0024C4C7  E8 8C 83 20 00                  call 0x140454858
0024C4CC  44 8B C8                        mov r9d, eax
0024C4CF  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0024C4D4  48 8D 43 78                     lea rax, [rbx + 0x78]
0024C4D8  33 D2                           xor edx, edx
0024C4DA  4C 8D 43 48                     lea r8, [rbx + 0x48]
0024C4DE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0024C4E3  48 8B CB                        mov rcx, rbx
0024C4E6  E8 F5 11 00 00                  call 0x14024d6e0
0024C4EB  0F B6 E8                        movzx ebp, al
0024C4EE  E9 39 FB FF FF                  jmp 0x14024c02c
0024C4F3  41 83 FE 06                     cmp r14d, 6
0024C4F7  0F 84 86 F4 FF FF               je 0x14024b983
0024C4FD  41 83 FE 05                     cmp r14d, 5
0024C501  77 15                           ja 0x14024c518
0024C503  49 69 CE 88 00 00 00            imul rcx, r14, 0x88
0024C50A  80 BC 31 30 10 00 00 01         cmp byte ptr [rcx + rsi + 0x1030], 1
0024C512  0F 84 6B F4 FF FF               je 0x14024b983
0024C518  48 8D 4B 40                     lea rcx, [rbx + 0x40]
0024C51C  E8 BF 17 00 00                  call 0x14024dce0
0024C521  80 7B 7D 01                     cmp byte ptr [rbx + 0x7d], 1
0024C525  44 0F B6 F8                     movzx r15d, al
0024C529  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
0024C52E  0F 84 02 07 00 00               je 0x14024cc36
0024C534  49 8B CD                        mov rcx, r13
0024C537  E8 44 C9 FF FF                  call 0x140248e80
0024C53C  E9 D4 F4 FF FF                  jmp 0x14024ba15
0024C541  B2 02                           mov dl, 2
0024C543  41 0F B6 CF                     movzx ecx, r15b
0024C547  E8 B0 91 2A 00                  call 0x1404f56fc
0024C54C  E9 54 F4 FF FF                  jmp 0x14024b9a5
0024C551  0F B6 D0                        movzx edx, al
0024C554  40 0F B6 CE                     movzx ecx, sil
0024C558  E8 9F 91 2A 00                  call 0x1404f56fc
0024C55D  E9 BA FB FF FF                  jmp 0x14024c11c
0024C562  2B C6                           sub eax, esi
0024C564  0F 84 11 FB FF FF               je 0x14024c07b
0024C56A  8B F8                           mov edi, eax
0024C56C  BB 01 00 00 00                  mov ebx, 1
0024C571  48 85 C9                        test rcx, rcx
0024C574  0F 85 B3 02 00 00               jne 0x14024c82d
0024C57A  4C 8D 3D 7F 3A DB FF            lea r15, [rip - 0x24c581]
0024C581  45 33 C9                        xor r9d, r9d
0024C584  48 8D 0D 55 1D CC 00            lea rcx, [rip + 0xcc1d55]
0024C58B  44 8B C3                        mov r8d, ebx
0024C58E  33 D2                           xor edx, edx
0024C590  E8 EB AA 14 00                  call 0x140397080
0024C595  45 33 F6                        xor r14d, r14d
0024C598  8B F3                           mov esi, ebx
0024C59A  0F 0D 0D 5F 1D CC 00            prefetchw byte ptr [rip + 0xcc1d5f]
0024C5A1  8B 05 59 1D CC 00               mov eax, dword ptr [rip + 0xcc1d59]
0024C5A7  8B C8                           mov ecx, eax
0024C5A9  0B CE                           or ecx, esi
0024C5AB  F0 0F B1 0D 4D 1D CC 00         lock cmpxchg dword ptr [rip + 0xcc1d4d], ecx
0024C5B3  75 F2                           jne 0x14024c5a7
0024C5B5  85 C6                           test esi, eax
0024C5B7  0F 85 5C 02 00 00               jne 0x14024c819
0024C5BD  4B 8D 0C B6                     lea rcx, [r14 + r14*4]
0024C5C1  45 33 C9                        xor r9d, r9d
0024C5C4  49 8D 97 10 E3 F0 00            lea rdx, [r15 + 0xf0e310]
0024C5CB  48 8D 14 CA                     lea rdx, [rdx + rcx*8]
0024C5CF  48 8B 0D CA A8 D7 00            mov rcx, qword ptr [rip + 0xd7a8ca]
0024C5D6  45 8D 41 30                     lea r8d, [r9 + 0x30]
0024C5DA  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
0024C5DE  E8 39 BA 14 00                  call 0x14039801c
0024C5E3  84 C0                           test al, al
0024C5E5  0F 84 23 02 00 00               je 0x14024c80e
0024C5EB  48 2B FB                        sub rdi, rbx
0024C5EE  75 91                           jne 0x14024c581
0024C5F0  4C 8B BC 24 C8 00 00 00         mov r15, qword ptr [rsp + 0xc8]
0024C5F8  4C 8B AC 24 A8 00 00 00         mov r13, qword ptr [rsp + 0xa8]
0024C600  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
0024C608  E9 6E FA FF FF                  jmp 0x14024c07b
0024C60D  48 8D 0D 7C 36 07 00            lea rcx, [rip + 0x7367c]
0024C614  48 3B C1                        cmp rax, rcx
0024C617  48 8B CB                        mov rcx, rbx
0024C61A  0F 85 24 03 00 00               jne 0x14024c944
0024C620  E8 6B 36 07 00                  call 0x1402bfc90
0024C625  E9 9C F4 FF FF                  jmp 0x14024bac6
0024C62A  49 8B 4C ED 38                  mov rcx, qword ptr [r13 + rbp*8 + 0x38]
0024C62F  E9 5F F4 FF FF                  jmp 0x14024ba93
0024C634  48 8B D1                        mov rdx, rcx
0024C637  4C 8B C8                        mov r9, rax
0024C63A  B9 67 06 00 00                  mov ecx, 0x667
0024C63F  E8 28 36 07 00                  call 0x1402bfc6c
0024C644  CC                              int3
0024C645  F6 C2 08                        test dl, 8
0024C648  0F 85 C6 FC FF FF               jne 0x14024c314
0024C64E  41 FF C1                        inc r9d
0024C651  48 83 C1 08                     add rcx, 8
0024C655  E9 A2 FC FF FF                  jmp 0x14024c2fc
0024C65A  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0024C65F  E9 1F F8 FF FF                  jmp 0x14024be83
0024C664  83 F9 02                        cmp ecx, 2
0024C667  0F 85 81 F4 FF FF               jne 0x14024baee
0024C66D  44 38 63 7D                     cmp byte ptr [rbx + 0x7d], r12b
0024C671  74 16                           je 0x14024c689
0024C673  49 69 C2 88 00 00 00            imul rax, r10, 0x88
0024C67A  8B 8C 30 58 10 00 00            mov ecx, dword ptr [rax + rsi + 0x1058]
0024C681  85 C9                           test ecx, ecx
0024C683  0F 85 03 01 00 00               jne 0x14024c78c
0024C689  49 6B D2 22                     imul rdx, r10, 0x22
0024C68D  8B 8C 96 5C 10 00 00            mov ecx, dword ptr [rsi + rdx*4 + 0x105c]
0024C694  85 C9                           test ecx, ecx
0024C696  75 63                           jne 0x14024c6fb
0024C698  8B 8C 96 60 10 00 00            mov ecx, dword ptr [rsi + rdx*4 + 0x1060]
0024C69F  85 C9                           test ecx, ecx
0024C6A1  75 7B                           jne 0x14024c71e
0024C6A3  8B 8C 96 64 10 00 00            mov ecx, dword ptr [rsi + rdx*4 + 0x1064]
0024C6AA  85 C9                           test ecx, ecx
0024C6AC  0F 85 93 00 00 00               jne 0x14024c745
0024C6B2  44 38 63 7D                     cmp byte ptr [rbx + 0x7d], r12b
0024C6B6  0F 84 AD FB FF FF               je 0x14024c269
0024C6BC  49 69 C2 88 00 00 00            imul rax, r10, 0x88
0024C6C3  8B 8C 30 68 10 00 00            mov ecx, dword ptr [rax + rsi + 0x1068]
0024C6CA  85 C9                           test ecx, ecx
0024C6CC  0F 85 97 00 00 00               jne 0x14024c769
0024C6D2  49 69 C2 88 00 00 00            imul rax, r10, 0x88
0024C6D9  8B 8C 30 6C 10 00 00            mov ecx, dword ptr [rax + rsi + 0x106c]
0024C6E0  85 C9                           test ecx, ecx
0024C6E2  0F 84 81 FB FF FF               je 0x14024c269
0024C6E8  48 8B 43 70                     mov rax, qword ptr [rbx + 0x70]
0024C6EC  8B 10                           mov edx, dword ptr [rax]
0024C6EE  85 D1                           test ecx, edx
0024C6F0  0F 84 73 FB FF FF               je 0x14024c269
0024C6F6  E9 C0 FB FF FF                  jmp 0x14024c2bb
0024C6FB  49 8B 45 40                     mov rax, qword ptr [r13 + 0x40]
0024C6FF  44 8B 00                        mov r8d, dword ptr [rax]
0024C702  44 85 C1                        test ecx, r8d
0024C705  74 91                           je 0x14024c698
0024C707  41 F6 C0 02                     test r8b, 2
0024C70B  74 05                           je 0x14024c712
0024C70D  F0 41 FF 4D 68                  lock dec dword ptr [r13 + 0x68]
0024C712  49 8B 45 40                     mov rax, qword ptr [r13 + 0x40]
0024C716  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024C719  E9 7A FF FF FF                  jmp 0x14024c698
0024C71E  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
0024C722  44 8B 00                        mov r8d, dword ptr [rax]
0024C725  44 85 C1                        test ecx, r8d
0024C728  0F 84 75 FF FF FF               je 0x14024c6a3
0024C72E  41 F6 C0 02                     test r8b, 2
0024C732  74 05                           je 0x14024c739
0024C734  F0 41 FF 4D 68                  lock dec dword ptr [r13 + 0x68]
0024C739  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
0024C73D  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024C740  E9 5E FF FF FF                  jmp 0x14024c6a3
0024C745  49 8B 45 50                     mov rax, qword ptr [r13 + 0x50]
0024C749  8B 10                           mov edx, dword ptr [rax]
0024C74B  85 D1                           test ecx, edx
0024C74D  0F 84 5F FF FF FF               je 0x14024c6b2
0024C753  F6 C2 02                        test dl, 2
0024C756  74 05                           je 0x14024c75d
0024C758  F0 41 FF 4D 68                  lock dec dword ptr [r13 + 0x68]
0024C75D  49 8B 45 50                     mov rax, qword ptr [r13 + 0x50]
0024C761  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024C764  E9 49 FF FF FF                  jmp 0x14024c6b2
0024C769  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
0024C76D  8B 10                           mov edx, dword ptr [rax]
0024C76F  85 D1                           test ecx, edx
0024C771  0F 84 5B FF FF FF               je 0x14024c6d2
0024C777  F6 C2 02                        test dl, 2
0024C77A  74 04                           je 0x14024c780
0024C77C  F0 FF 4B 78                     lock dec dword ptr [rbx + 0x78]
0024C780  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
0024C784  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024C787  E9 46 FF FF FF                  jmp 0x14024c6d2
0024C78C  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
0024C790  8B 10                           mov edx, dword ptr [rax]
0024C792  85 D1                           test ecx, edx
0024C794  0F 84 EF FE FF FF               je 0x14024c689
0024C79A  F6 C2 02                        test dl, 2
0024C79D  74 04                           je 0x14024c7a3
0024C79F  F0 FF 4B 78                     lock dec dword ptr [rbx + 0x78]
0024C7A3  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
0024C7A7  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024C7AA  E9 DA FE FF FF                  jmp 0x14024c689
0024C7AF  48 8D 0D DA 75 21 00            lea rcx, [rip + 0x2175da]
0024C7B6  48 3B C1                        cmp rax, rcx
0024C7B9  48 8B CB                        mov rcx, rbx
0024C7BC  0F 85 E4 03 00 00               jne 0x14024cba6
0024C7C2  E8 C9 75 21 00                  call 0x140463d90
0024C7C7  E9 D9 F3 FF FF                  jmp 0x14024bba5
0024C7CC  8B 83 B4 00 00 00               mov eax, dword ptr [rbx + 0xb4]
0024C7D2  41 83 FB 03                     cmp r11d, 3
0024C7D6  0F 84 CC 01 00 00               je 0x14024c9a8
0024C7DC  44 8B D8                        mov r11d, eax
0024C7DF  8B FE                           mov edi, esi
0024C7E1  E9 CC F5 FF FF                  jmp 0x14024bdb2
0024C7E6  48 8D 0D 83 1F 07 00            lea rcx, [rip + 0x71f83]
0024C7ED  48 3B C1                        cmp rax, rcx
0024C7F0  0F 85 76 02 00 00               jne 0x14024ca6c
0024C7F6  48 8B CB                        mov rcx, rbx
0024C7F9  E8 72 1F 07 00                  call 0x1402be770
0024C7FE  E9 4D FB FF FF                  jmp 0x14024c350
0024C803  41 B9 06 00 00 00               mov r9d, 6
0024C809  E9 06 FB FF FF                  jmp 0x14024c314
0024C80E  8B C6                           mov eax, esi
0024C810  F7 D0                           not eax
0024C812  F0 21 05 E7 1A CC 00            lock and dword ptr [rip + 0xcc1ae7], eax
0024C819  41 FF C6                        inc r14d
0024C81C  D1 C6                           rol esi, 1
0024C81E  41 83 FE 04                     cmp r14d, 4
0024C822  0F 83 C3 FD FF FF               jae 0x14024c5eb
0024C828  E9 6D FD FF FF                  jmp 0x14024c59a
0024C82D  4C 8D 2D CC 37 DB FF            lea r13, [rip - 0x24c834]
0024C834  45 33 C9                        xor r9d, r9d
0024C837  48 8D 0D 82 1D CC 00            lea rcx, [rip + 0xcc1d82]
0024C83E  44 8B C3                        mov r8d, ebx
0024C841  33 D2                           xor edx, edx
0024C843  E8 38 A8 14 00                  call 0x140397080
0024C848  45 33 F6                        xor r14d, r14d
0024C84B  8B F3                           mov esi, ebx
0024C84D  0F 0D 0D 8C 1D CC 00            prefetchw byte ptr [rip + 0xcc1d8c]
0024C854  8B 05 86 1D CC 00               mov eax, dword ptr [rip + 0xcc1d86]
0024C85A  8B C8                           mov ecx, eax
0024C85C  0B CE                           or ecx, esi
0024C85E  F0 0F B1 0D 7A 1D CC 00         lock cmpxchg dword ptr [rip + 0xcc1d7a], ecx
0024C866  75 F2                           jne 0x14024c85a
0024C868  85 C6                           test esi, eax
0024C86A  75 3F                           jne 0x14024c8ab
0024C86C  4B 8D 0C B6                     lea rcx, [r14 + r14*4]
0024C870  45 33 C9                        xor r9d, r9d
0024C873  49 8D 95 F0 E5 F0 00            lea rdx, [r13 + 0xf0e5f0]
0024C87A  48 8D 14 CA                     lea rdx, [rdx + rcx*8]
0024C87E  48 8B 0D 1B A6 D7 00            mov rcx, qword ptr [rip + 0xd7a61b]
0024C885  45 8D 41 30                     lea r8d, [r9 + 0x30]
0024C889  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
0024C88D  E8 8A B7 14 00                  call 0x14039801c
0024C892  84 C0                           test al, al
0024C894  74 0A                           je 0x14024c8a0
0024C896  48 2B FB                        sub rdi, rbx
0024C899  75 99                           jne 0x14024c834
0024C89B  E9 58 FD FF FF                  jmp 0x14024c5f8
0024C8A0  8B C6                           mov eax, esi
0024C8A2  F7 D0                           not eax
0024C8A4  F0 21 05 35 1D CC 00            lock and dword ptr [rip + 0xcc1d35], eax
0024C8AB  41 FF C6                        inc r14d
0024C8AE  D1 C6                           rol esi, 1
0024C8B0  41 83 FE 04                     cmp r14d, 4
0024C8B4  73 E0                           jae 0x14024c896
0024C8B6  EB 95                           jmp 0x14024c84d
0024C8B8  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0024C8BC  48 8B D0                        mov rdx, rax
0024C8BF  8B F9                           mov edi, ecx
0024C8C1  83 F9 03                        cmp ecx, 3
0024C8C4  0F 85 96 F1 FF FF               jne 0x14024ba60
0024C8CA  44 8B 8B B4 00 00 00            mov r9d, dword ptr [rbx + 0xb4]
0024C8D1  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0024C8D5  45 85 C9                        test r9d, r9d
0024C8D8  0F 84 82 F1 FF FF               je 0x14024ba60
0024C8DE  48 8D 83 28 01 00 00            lea rax, [rbx + 0x128]
0024C8E5  41 8B D1                        mov edx, r9d
0024C8E8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0024C8F0  44 03 10                        add r10d, dword ptr [rax]
0024C8F3  48 8D 80 D0 00 00 00            lea rax, [rax + 0xd0]
0024C8FA  48 83 EA 01                     sub rdx, 1
0024C8FE  75 F0                           jne 0x14024c8f0
0024C900  49 69 D0 88 00 00 00            imul rdx, r8, 0x88
0024C907  E9 59 F1 FF FF                  jmp 0x14024ba65
0024C90C  83 FF 03                        cmp edi, 3
0024C90F  0F 85 3A F7 FF FF               jne 0x14024c04f
0024C915  8B 93 B4 00 00 00               mov edx, dword ptr [rbx + 0xb4]
0024C91B  85 D2                           test edx, edx
0024C91D  0F 84 2C F7 FF FF               je 0x14024c04f
0024C923  48 8D 8B 28 01 00 00            lea rcx, [rbx + 0x128]
0024C92A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
0024C930  03 01                           add eax, dword ptr [rcx]
0024C932  48 8D 89 D0 00 00 00            lea rcx, [rcx + 0xd0]
0024C939  48 83 EA 01                     sub rdx, 1
0024C93D  75 F1                           jne 0x14024c930
0024C93F  E9 0B F7 FF FF                  jmp 0x14024c04f
0024C944  E8 87 E1 46 00                  call 0x1406baad0
0024C949  E9 78 F1 FF FF                  jmp 0x14024bac6
0024C94E  8B CA                           mov ecx, edx
0024C950  E9 B7 F1 FF FF                  jmp 0x14024bb0c
0024C955  8B 83 B4 00 00 00               mov eax, dword ptr [rbx + 0xb4]
0024C95B  41 83 FB 03                     cmp r11d, 3
0024C95F  0F 84 FB 00 00 00               je 0x14024ca60
0024C965  8B D0                           mov edx, eax
0024C967  45 8B CC                        mov r9d, r12d
0024C96A  E9 F7 F5 FF FF                  jmp 0x14024bf66
0024C96F  8B 83 B4 00 00 00               mov eax, dword ptr [rbx + 0xb4]
0024C975  41 83 FE 03                     cmp r14d, 3
0024C979  41 8B D4                        mov edx, r12d
0024C97C  0F 45 D0                        cmovne edx, eax
0024C97F  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
0024C983  44 8D 40 FF                     lea r8d, [rax - 1]
0024C987  45 0F 45 C4                     cmovne r8d, r12d
0024C98B  44 89 44 24 3C                  mov dword ptr [rsp + 0x3c], r8d
0024C990  41 3B D0                        cmp edx, r8d
0024C993  0F 86 59 F3 FF FF               jbe 0x14024bcf2
0024C999  E9 37 F5 FF FF                  jmp 0x14024bed5
0024C99E  4A 8B 44 F3 48                  mov rax, qword ptr [rbx + r14*8 + 0x48]
0024C9A3  E9 B3 F1 FF FF                  jmp 0x14024bb5b
0024C9A8  44 8B DE                        mov r11d, esi
0024C9AB  8D 78 FF                        lea edi, [rax - 1]
0024C9AE  E9 FF F3 FF FF                  jmp 0x14024bdb2
0024C9B3  48 8D 53 48                     lea rdx, [rbx + 0x48]
0024C9B7  41 8B CC                        mov ecx, r12d
0024C9BA  85 C9                           test ecx, ecx
0024C9BC  0F 8F C8 01 00 00               jg 0x14024cb8a
0024C9C2  48 8B 02                        mov rax, qword ptr [rdx]
0024C9C5  44 8B 00                        mov r8d, dword ptr [rax]
0024C9C8  41 F6 C0 02                     test r8b, 2
0024C9CC  0F 84 12 01 00 00               je 0x14024cae4
0024C9D2  F0 FF 4B 78                     lock dec dword ptr [rbx + 0x78]
0024C9D6  33 D2                           xor edx, edx
0024C9D8  48 63 F9                        movsxd rdi, ecx
0024C9DB  4D 8B C7                        mov r8, r15
0024C9DE  48 69 C7 88 00 00 00            imul rax, rdi, 0x88
0024C9E5  48 8D 0D 14 36 DB FF            lea rcx, [rip - 0x24c9ec]
0024C9EC  48 8B 84 08 A8 10 00 00         mov rax, qword ptr [rax + rcx + 0x10a8]
0024C9F4  48 8D 0D 45 1D 07 00            lea rcx, [rip + 0x71d45]
0024C9FB  48 3B C1                        cmp rax, rcx
0024C9FE  0F 85 6D 01 00 00               jne 0x14024cb71
0024CA04  48 8B CB                        mov rcx, rbx
0024CA07  E8 34 1D 07 00                  call 0x1402be740
0024CA0C  0F B6 E8                        movzx ebp, al
0024CA0F  48 8B 44 FB 48                  mov rax, qword ptr [rbx + rdi*8 + 0x48]
0024CA14  83 20 FD                        and dword ptr [rax], 0xfffffffd
0024CA17  48 8B 44 FB 48                  mov rax, qword ptr [rbx + rdi*8 + 0x48]
0024CA1C  83 20 F7                        and dword ptr [rax], 0xfffffff7
0024CA1F  48 8B 44 FB 48                  mov rax, qword ptr [rbx + rdi*8 + 0x48]
0024CA24  8B 7C 24 30                     mov edi, dword ptr [rsp + 0x30]
0024CA28  83 08 04                        or dword ptr [rax], 4
0024CA2B  E9 F8 F5 FF FF                  jmp 0x14024c028
0024CA30  41 8B 44 24 04                  mov eax, dword ptr [r12 + 4]
0024CA35  41 83 E5 FE                     and r13d, 0xfffffffe
0024CA39  41 83 CD 02                     or r13d, 2
0024CA3D  41 89 44 24 08                  mov dword ptr [r12 + 8], eax
0024CA42  45 89 2C 24                     mov dword ptr [r12], r13d
0024CA46  F0 FF 47 68                     lock inc dword ptr [rdi + 0x68]
0024CA4A  E9 46 F4 FF FF                  jmp 0x14024be95
0024CA4F  83 FF 02                        cmp edi, 2
0024CA52  0F 85 69 F1 FF FF               jne 0x14024bbc1
0024CA58  44 8B F2                        mov r14d, edx
0024CA5B  E9 61 F1 FF FF                  jmp 0x14024bbc1
0024CA60  41 8B D4                        mov edx, r12d
0024CA63  44 8D 48 FF                     lea r9d, [rax - 1]
0024CA67  E9 FA F4 FF FF                  jmp 0x14024bf66
0024CA6C  48 8D 0D 1D 1D 07 00            lea rcx, [rip + 0x71d1d]
0024CA73  48 3B C1                        cmp rax, rcx
0024CA76  48 8B CB                        mov rcx, rbx
0024CA79  0F 85 87 01 00 00               jne 0x14024cc06
0024CA7F  E8 0C 1D 07 00                  call 0x1402be790
0024CA84  E9 C7 F8 FF FF                  jmp 0x14024c350
0024CA89  4C 8D 14 18                     lea r10, [rax + rbx]
0024CA8D  41 BE 01 00 00 00               mov r14d, 1
0024CA93  45 8B CE                        mov r9d, r14d
0024CA96  49 8D 92 00 01 00 00            lea rdx, [r10 + 0x100]
0024CA9D  41 83 F9 03                     cmp r9d, 3
0024CAA1  0F 8F F4 00 00 00               jg 0x14024cb9b
0024CAA7  48 8B 02                        mov rax, qword ptr [rdx]
0024CAAA  8B 08                           mov ecx, dword ptr [rax]
0024CAAC  F6 C1 02                        test cl, 2
0024CAAF  0F 84 A7 00 00 00               je 0x14024cb5c
0024CAB5  49 8D 82 28 01 00 00            lea rax, [r10 + 0x128]
0024CABC  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0024CAC1  4D 8D 82 F8 00 00 00            lea r8, [r10 + 0xf8]
0024CAC8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0024CACD  49 8D 92 C0 00 00 00            lea rdx, [r10 + 0xc0]
0024CAD4  48 8B CB                        mov rcx, rbx
0024CAD7  E8 04 0C 00 00                  call 0x14024d6e0
0024CADC  0F B6 E8                        movzx ebp, al
0024CADF  E9 4E F5 FF FF                  jmp 0x14024c032
0024CAE4  41 F6 C0 08                     test r8b, 8
0024CAE8  0F 85 E4 FE FF FF               jne 0x14024c9d2
0024CAEE  FF C1                           inc ecx
0024CAF0  48 83 C2 08                     add rdx, 8
0024CAF4  E9 C1 FE FF FF                  jmp 0x14024c9ba
0024CAF9  80 BB 88 00 00 00 00            cmp byte ptr [rbx + 0x88], 0
0024CB00  45 0F B6 E4                     movzx r12d, r12b
0024CB04  45 0F 45 E6                     cmovne r12d, r14d
0024CB08  E9 63 F5 FF FF                  jmp 0x14024c070
0024CB0D  8B 05 A5 9F D7 00               mov eax, dword ptr [rip + 0xd79fa5]
0024CB13  A8 40                           test al, 0x40
0024CB15  0F 84 DD EE FF FF               je 0x14024b9f8
0024CB1B  E8 70 29 0C 00                  call 0x14030f490
0024CB20  84 C0                           test al, al
0024CB22  0F 84 D0 EE FF FF               je 0x14024b9f8
0024CB28  8B CE                           mov ecx, esi
0024CB2A  E8 31 29 0C 00                  call 0x14030f460
0024CB2F  E9 C6 EE FF FF                  jmp 0x14024b9fa
0024CB34  8B 05 7E 9F D7 00               mov eax, dword ptr [rip + 0xd79f7e]
0024CB3A  A8 40                           test al, 0x40
0024CB3C  0F 84 2A F6 FF FF               je 0x14024c16c
0024CB42  E8 49 29 0C 00                  call 0x14030f490
0024CB47  84 C0                           test al, al
0024CB49  0F 84 1D F6 FF FF               je 0x14024c16c
0024CB4F  41 8B CE                        mov ecx, r14d
0024CB52  E8 09 29 0C 00                  call 0x14030f460
0024CB57  E9 12 F6 FF FF                  jmp 0x14024c16e
0024CB5C  F6 C1 08                        test cl, 8
0024CB5F  0F 85 50 FF FF FF               jne 0x14024cab5
0024CB65  41 FF C1                        inc r9d
0024CB68  48 83 C2 08                     add rdx, 8
0024CB6C  E9 2C FF FF FF                  jmp 0x14024ca9d
0024CB71  48 8D 0D F8 1B 07 00            lea rcx, [rip + 0x71bf8]
0024CB78  48 3B C1                        cmp rax, rcx
0024CB7B  75 33                           jne 0x14024cbb0
0024CB7D  48 8B CB                        mov rcx, rbx
0024CB80  E8 EB 1B 07 00                  call 0x1402be770
0024CB85  E9 82 FE FF FF                  jmp 0x14024ca0c
0024CB8A  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
0024CB8E  E9 44 F7 FF FF                  jmp 0x14024c2d7
0024CB93  41 8B C4                        mov eax, r12d
0024CB96  E9 B4 F4 FF FF                  jmp 0x14024c04f
0024CB9B  41 B9 06 00 00 00               mov r9d, 6
0024CBA1  E9 0F FF FF FF                  jmp 0x14024cab5
0024CBA6  E8 25 DF 46 00                  call 0x1406baad0
0024CBAB  E9 F5 EF FF FF                  jmp 0x14024bba5
0024CBB0  48 8D 0D D9 1B 07 00            lea rcx, [rip + 0x71bd9]
0024CBB7  48 3B C1                        cmp rax, rcx
0024CBBA  48 8B CB                        mov rcx, rbx
0024CBBD  0F 85 9E 00 00 00               jne 0x14024cc61
0024CBC3  E8 C8 1B 07 00                  call 0x1402be790
0024CBC8  E9 3F FE FF FF                  jmp 0x14024ca0c
0024CBCD  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0024CBD2  48 8D 7B 40                     lea rdi, [rbx + 0x40]
0024CBD6  48 8B CF                        mov rcx, rdi
0024CBD9  E8 12 43 07 00                  call 0x1402c0ef0
0024CBDE  E9 13 F5 FF FF                  jmp 0x14024c0f6
0024CBE3  8B 05 6F 12 CC 00               mov eax, dword ptr [rip + 0xcc126f]
0024CBE9  85 C0                           test eax, eax
0024CBEB  0F 85 DB F4 FF FF               jne 0x14024c0cc
0024CBF1  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0024CBF9  48 8B CF                        mov rcx, rdi
0024CBFC  E8 43 43 07 00                  call 0x1402c0f44
0024CC01  E9 C9 F4 FF FF                  jmp 0x14024c0cf
0024CC06  E8 C5 DE 46 00                  call 0x1406baad0
0024CC0B  E9 40 F7 FF FF                  jmp 0x14024c350
0024CC10  8B 05 42 12 CC 00               mov eax, dword ptr [rip + 0xcc1242]
0024CC16  85 C0                           test eax, eax
0024CC18  0F 85 80 F7 FF FF               jne 0x14024c39e
0024CC1E  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0024CC26  49 8B CD                        mov rcx, r13
0024CC29  E8 16 43 07 00                  call 0x1402c0f44
0024CC2E  45 33 F6                        xor r14d, r14d
0024CC31  E9 6F F7 FF FF                  jmp 0x14024c3a5
0024CC36  41 0F B6 D7                     movzx edx, r15b
0024CC3A  48 8D 4B 40                     lea rcx, [rbx + 0x40]
0024CC3E  E8 AD 42 0A 00                  call 0x1402f0ef0
0024CC43  BA 02 00 00 00                  mov edx, 2
0024CC48  E9 36 ED FF FF                  jmp 0x14024b983
0024CC4D  4C 63 CA                        movsxd r9, edx
0024CC50  4D 8B C2                        mov r8, r10
0024CC53  49 8B D3                        mov rdx, r11
0024CC56  B9 66 06 00 00                  mov ecx, 0x666
0024CC5B  E8 0C 30 07 00                  call 0x1402bfc6c
0024CC60  CC                              int3
0024CC61  E8 6A DE 46 00                  call 0x1406baad0
0024CC66  E9 A1 FD FF FF                  jmp 0x14024ca0c
0024CC6B  8B C2                           mov eax, edx
0024CC6D  48 69 C8 D0 00 00 00            imul rcx, rax, 0xd0
0024CC74  83 BC 19 28 01 00 00 00         cmp dword ptr [rcx + rbx + 0x128], 0
0024CC7C  0F 87 AA F3 FF FF               ja 0x14024c02c
0024CC82  FF C2                           inc edx
0024CC84  E9 28 F8 FF FF                  jmp 0x14024c4b1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPepProcessEvent(__int64 a1, __int64 a2, int a3, int a4, unsigned __int8 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned int v_stack_p3C;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;

    v_stack_p20 = v_rbx;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (96);
    v_r12 = 0;
    v_stack_p18 = 0;
    if (a2 == 0) goto loc_0024B983;
    if ((*(unsigned int *)(a1 + 180)) != 1) goto loc_0024C3D5;
loc_0024B983:
    v_stack_p18 = 1;
    v_stack_m50 = v_cr8;
    if ((*(unsigned int *)(v_rip + 14136193)) != 0) goto loc_0024C541;
loc_0024B9A5:
    if (((*(unsigned __int8 *)(v_rip + 14135642)) & (33)) != 0) goto loc_0024C41E;
loc_0024B9B2:
    v_rsi = 0;
    if (!(condition_is_above_or_equal)) {
        a2 = (unsigned __int8)(v_cr8);
        a1 = a1 + 64;
        result = ExpWaitForSpinLockExclusiveAndAcquire(a1, a2, a3, a4);
        v_rsi = (unsigned int)(result);
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)))))) == 0x80000000ULL) goto loc_0024BA0A;
loc_0024B9DC:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)))))) >= 0x80000000ULL) {
    }
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 14129338)) & ((unsigned int)(v_rsi))) == 0) goto loc_0024CB0D;
loc_0024B9F8:
loc_0024B9FA:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)))))) != 0x80000000ULL) goto loc_0024B9DC;
loc_0024BA0A:
loc_0024BA11:
    *(unsigned __int8 *)(a1 + 125) = 1;
loc_0024BA15:
    if (((unsigned int)((int)(a3))) == 6) goto loc_0024C374;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64))))) * ((int)(a3));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + v_rip - 2406929 * 1 + 4156)))) < 2) goto loc_0024C374;
    v_stack_m64 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 120)));
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(result + v_rip - 2406929 * 1 + 4156)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + v_rip - 2406929 * 1 + 4156)))) != 2) goto loc_0024C8B8;
loc_0024BA4B:
    v_r10 = (unsigned int)(*(unsigned int *)(a1 + 120));
    if (a2 != 0) {
        v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 120))) + (*(unsigned int *)(a2 + 104)));
        v_stack_m64 = (unsigned int)(v_r10);
    }
    if (((unsigned int)((int)(a3))) == 6) goto loc_0024BAC6;
loc_0024BA65:
    v_stack_m64 = (unsigned int)(v_r10);
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m68));
    if (((unsigned int)((int)(a3))) > 5) goto loc_0024C62A;
    if ((*(unsigned __int8 *)(result + v_rip - 2406929 * 1 + 4144)) != 1) goto loc_0024C62A;
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m68));
    v_stack_m64 = (unsigned int)(v_r10);
loc_0024BA93:
    if ((((unsigned __int8)((int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + (int)(a3) * 8 + 72))))) & (4)) == 0) goto loc_0024C634;
    result = (unsigned int)(((int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + (int)(a3) * 8 + 72)))) & (0xFFFFFFFBULL));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + (int)(a3) * 8 + 72)) = (unsigned int)(result);
    if ((*(unsigned __int64 *)(result + v_rip - 2406929 * 1 + 4272)) != (v_rip + 6982)) goto loc_0024C401;
    result = PopPepCompleteComponentActiveActivity(a1, a2, (int)(a3), a4);
loc_0024BAC6:
    if (((unsigned int)((int)(a4))) == 6) goto loc_0024BBAA;
    result = (result) * ((int)(a4));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + v_rip - 2406929 * 1 + 4148))) != 0) goto loc_0024C23C;
loc_0024BAEE:
    if (((unsigned int)((int)(a4))) > 5) goto loc_0024BB09;
    result = (result) * ((int)(a4));
    if ((*(unsigned __int8 *)(result + v_rip - 2406929 * 1 + 4144)) == 1) goto loc_0024C94E;
loc_0024BB09:
loc_0024BB0C:
    v_r11 = a1 + 72;
    if (0 != 1) { v_r11 = a2 + 56; }
loc_0024BB21:
    if (0 >= 6) goto loc_0024BB4D;
    if (*(unsigned __int64 *)(v_r11 + 0 * 8) == 0) goto loc_0024BB46;
    a1 = (0) * ((int)(a4));
    a1 = (a1) + (0);
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_r11 + 0 * 8))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2406929 + a1 * 4 + 4160))))) != 0) goto loc_0024CC4D;
loc_0024BB46:
    a2 = (unsigned int)((0) + 1);
    result = (0) + 1;
    goto loc_0024BB21;
loc_0024BB4D:
    if (a2 == 0) goto loc_0024C99E;
loc_0024BB5B:
    *(unsigned int *)(*(unsigned __int64 *)(a2 + (int)(a4) * 8 + 56) + 4) = 0;
    a3 = 0;
    result = (*(unsigned __int64 *)(a2 + (int)(a4) * 8 + 56)) * ((int)(a4));
    if ((*(unsigned __int64 *)(result + v_rip - 2406929 * 1 + 4256)) == (v_rip + 7211)) goto loc_0024BB9D;
    if ((*(unsigned __int64 *)(result + v_rip - 2406929 * 1 + 4256)) != (v_rip + 7382)) goto loc_0024C7AF;
    result = PopPepTriggerComponentActiveActivity(a1, a2, a3, a4);
    goto loc_0024BBA5;
loc_0024BB9D:
    result = PopPepTriggerComponentActivatingActivity(a1, a2, a3, a4);
loc_0024BBA5:
loc_0024BBAA:
    if ((unsigned int)((unsigned int)(v_stack_m68)) == 0) goto loc_0024C014;
    if (a2 == 0) goto loc_0024CA4F;
loc_0024BBC1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72))))) & (1)) == 0) goto loc_0024BCD8;
    a3 = v_rip - 2403168;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 72) + 16)) == 0) { a3 = v_rip - 2403168; }
loc_0024BBF2:
    if (condition_is_greater) goto loc_0024BC16;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3))) == 0) goto loc_0024BC0A;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 72))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a3))))) != 0) goto loc_0024BCD8;
loc_0024BC0A:
    a2 = (unsigned int)((0) + 1);
    a4 = (a1 + 72) + (8);
    a3 = (a3) + (4);
    goto loc_0024BBF2;
loc_0024BC16:
    v_stack_m64 = (unsigned int)((unsigned int)(v_stack_m64));
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m68));
loc_0024BC29:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 180))) != 0) goto loc_0024BC81;
    a2 = v_rip - 2403253;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 72) + 16)) == 0) { a2 = v_rip - 2403260; }
loc_0024BC4E:
    if (1 > 3) goto loc_0024BC7C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2))) == 0) goto loc_0024BC70;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 180))))) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 180)))));
    result = (result) + (1);
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + result * 8 + 248))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) != 0) goto loc_0024BCD8;
loc_0024BC70:
    a3 = (unsigned int)((1) + 1);
    v_r10 = (1) + 1;
    a2 = (a2) + (4);
    goto loc_0024BC4E;
loc_0024BC7C:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 180))) + 1);
    goto loc_0024BC29;
loc_0024BC81:
    a2 = v_rip - 2403315;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 72) + 16)) == 0) { a2 = v_rip - 2403346; }
loc_0024BCA0:
    if (4 > 5) goto loc_0024BCC3;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2))) == 0) goto loc_0024BCB6;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 104))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) != 0) goto loc_0024BCD8;
loc_0024BCB6:
    a3 = (unsigned int)((4) + 1);
    a4 = (a1 + 104) + (8);
    a2 = (a2) + (4);
    goto loc_0024BCA0;
loc_0024BCC3:
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72)))) & (0xFFFFFFFEULL));
    v_r11 = (unsigned int)((v_r11) | (2));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 4)));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 72)) = (unsigned int)(v_r11);
loc_0024BCD8:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m68))))) != 2) goto loc_0024C96F;
    v_stack_m60 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)))));
    v_stack_m5C = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)));
loc_0024BCF2:
loc_0024BCF6:
    v_rdi = ((unsigned int)(*(unsigned int *)(a2))) * ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8)))))));
    v_rdi = (v_rdi) + (192);
    v_stack_m48 = 3;
    v_rdi = (v_rdi) + (a1);
    v_stack_m40 = v_rdi;
loc_0024BD2A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(64 + v_rdi * 1))))) & (1)) == 0) goto loc_0024BE95;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2403391))) == 0) goto loc_0024CA30;
    v_rsi = 0;
    v_stack_p28 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(64 + v_rdi * 1) + 16));
    a2 = v_rip - 2403551;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(64 + v_rdi * 1) + 16)) == 0) { a2 = v_rip - 2403557; }
    a2 = (a2) + (136);
loc_0024BD7C:
    if (condition_is_greater) goto loc_0024BDA2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2))) == 0) goto loc_0024BD95;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 72))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) != 0) goto loc_0024BE83;
loc_0024BD95:
    a3 = (unsigned int)((0) + 1);
    v_r10 = (a1 + 72) + (8);
    a2 = (a2) + (4);
    goto loc_0024BD7C;
loc_0024BDA2:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2403391)))) != 2) goto loc_0024C7CC;
loc_0024BDB2:
    v_rsi = v_rip - 2403636;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(64 + v_rdi * 1) + 16))) == 0) { v_rsi = v_rip - 2403667; }
    v_rsi = (v_rsi) + (4);
loc_0024BDCB:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8)))))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))))) goto loc_0024BE16;
loc_0024BDDE:
    if (1 > 3) goto loc_0024BE11;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 136 * 1))) == 0) goto loc_0024BE06;
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))))))) * ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8)))))));
    result = (result) + (1);
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + result * 8 + 248))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 136 * 1))))) != 0) goto loc_0024C65A;
loc_0024BE06:
    a2 = (unsigned int)((1) + 1);
    v_r10 = (1) + 1;
    a3 = (v_rsi + 136 * 1) + (4);
    goto loc_0024BDDE;
loc_0024BE11:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8))))) + 1);
    goto loc_0024BDCB;
loc_0024BE16:
    a2 = v_rip - 2403725;
    if (a5 == 0) { a2 = v_rip - 2403756; }
    a2 = (a2) + (136);
loc_0024BE3D:
    if (4 > 5) goto loc_0024BE64;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2))) == 0) goto loc_0024BE57;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 104))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) != 0) goto loc_0024C65A;
loc_0024BE57:
    a3 = (unsigned int)((4) + 1);
    v_r10 = (v_stack_p8 + 104) + (8);
    a2 = (a2) + (4);
    goto loc_0024BE3D;
loc_0024BE64:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(64 + v_rdi * 1)))) & (0xFFFFFFFEULL));
    v_r13 = (unsigned int)((v_r13) | (2));
    *(unsigned int *)(*(unsigned __int64 *)(64 + v_rdi * 1)) = (unsigned int)(v_r13);
    *(unsigned int *)(*(unsigned __int64 *)(64 + v_rdi * 1) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(64 + v_rdi * 1) + 4)));
loc_0024BE83:
loc_0024BE95:
    v_rbp = (136) + (136);
    v_r14 = (64) + (8);
    v_r15 = (v_rip - 2403391) + (136);
    a1 = (v_stack_m48) - (1);
    v_stack_m48 = a1;
    if (condition_is_not_equal) goto loc_0024BD2A;
    a2 = (unsigned int)(((unsigned int)(v_stack_m60)) + 1);
    v_stack_m60 = (unsigned int)(a2);
    if (((unsigned int)(a2)) <= ((unsigned int)((unsigned int)(v_stack_m5C)))) goto loc_0024BCF6;
    v_r12 = 0;
loc_0024BED5:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 104)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 104))))) & (1)) != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 104)))) & (0xFFFFFFFEULL));
        result = (unsigned int)((result) | (2));
        *(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 104)) = (unsigned int)(result);
        result = *(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 104) + 4);
        *(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 104) + 8) = (unsigned int)(result);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 112))))) & (1)) == 0) goto loc_0024C010;
    if ((unsigned int)(*(unsigned __int64 *)(v_rip - 2403370)) == 0) goto loc_0024BFFE;
    a2 = v_rip - 2403320;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8 + 112) + 16)) == 0) { a2 = v_rip - 2403334; }
loc_0024BF2F:
    if (condition_is_greater) goto loc_0024BF55;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2))) == 0) goto loc_0024BF48;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 72))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) != 0) goto loc_0024C010;
loc_0024BF48:
    a3 = (unsigned int)((0) + 1);
    v_r10 = (v_stack_p8 + 72) + (8);
    a2 = (a2) + (4);
    goto loc_0024BF2F;
loc_0024BF55:
    if (((unsigned int)(*(unsigned __int64 *)(v_rip - 2403370))) != 2) goto loc_0024C955;
loc_0024BF66:
loc_0024BF6D:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m40 + 8)))))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m40 + 8))))) goto loc_0024BFBD;
    v_r10 = v_rip - 2403402;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8 + 112) + 16)) == 0) { v_r10 = v_rip - 2403409; }
loc_0024BF8B:
    if (1 > 3) goto loc_0024BFB9;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10))) == 0) goto loc_0024BFAD;
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m40 + 8))))))) * ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m40 + 8)))))));
    result = (result) + (1);
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + result * 8 + 248))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10))))) != 0) goto loc_0024C010;
loc_0024BFAD:
    a3 = (unsigned int)((1) + 1);
    v_r11 = (1) + 1;
    v_r10 = (v_r10) + (4);
    goto loc_0024BF8B;
loc_0024BFB9:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m40 + 8))))) + 1);
    goto loc_0024BF6D;
loc_0024BFBD:
    a3 = v_rip - 2403470;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8 + 112) + 16)) == 0) { a3 = v_rip - 2403487; }
loc_0024BFDB:
    if (4 > 5) goto loc_0024BFFC;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3))) == 0) goto loc_0024BFF0;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 104))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a3))))) != 0) goto loc_0024C010;
loc_0024BFF0:
    a2 = (unsigned int)((4) + 1);
    a4 = (v_stack_p8 + 104) + (8);
    a3 = (a3) + (4);
    goto loc_0024BFDB;
loc_0024BFFC:
loc_0024BFFE:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 112)))) & (0xFFFFFFFEULL));
    result = (unsigned int)((result) | (2));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 112)) = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 112) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 112) + 4)));
loc_0024C010:
loc_0024C014:
    v_rbp = 0;
    if (a6 != 0) goto loc_0024C2CD;
loc_0024C028:
loc_0024C02C:
loc_0024C032:
    if ((unsigned int)((unsigned int)(v_stack_m68)) == 0) goto loc_0024CB93;
    if (((unsigned int)((unsigned int)(v_stack_m68))) != 2) goto loc_0024C90C;
    result = (unsigned int)(*(unsigned int *)(v_stack_p8 + 120));
    if (v_stack_p10 != 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 120))) + (*(unsigned int *)(v_stack_p10 + 104)));
    }
    v_r12 = 0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p8 + 24))) & (1)) != 0) goto loc_0024C070;
    if ((unsigned int)(result) != 0) goto loc_0024C070;
    if (0 != 0) goto loc_0024C070;
    if ((*(unsigned int *)(v_stack_p8 + 140)) == ((unsigned int)(result))) goto loc_0024CAF9;
loc_0024C070:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_stack_p8 + 24)) & (32));
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(v_stack_m64)))) goto loc_0024C562;
loc_0024C07B:
    if (v_stack_p18 != 1) goto loc_0024C391;
    v_r14 = 0;
loc_0024C090:
    if (0 >= 6) goto loc_0024C0AE;
    if (*(unsigned __int64 *)(v_stack_p8 + 0 * 8 + 72) == 0) goto loc_0024C0AA;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 0 * 8 + 72))) != 0) goto loc_0024CBCD;
loc_0024C0AA:
    a1 = (unsigned int)((0) + 1);
    goto loc_0024C090;
loc_0024C0AE:
    if ((*(unsigned __int8 *)(v_stack_p8 + 136)) != 0) {
        *(unsigned __int8 *)(v_stack_p8 + 125) = 0;
    }
    if (((*(unsigned __int8 *)(v_rip + 14133828)) & (1)) != 0) goto loc_0024CBE3;
loc_0024C0CC:
    *(unsigned int *)(v_stack_p8 + 64) = 0;
loc_0024C0CF:
    result = 0;
    v_rdi = v_stack_p8 + 64;
    if ((*(unsigned int *)(v_rip + 14134346)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_stack_m50);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
        v_rdi = v_stack_p8 + 64;
    }
loc_0024C0F6:
    if (0 == 0) goto loc_0024C21F;
    v_rbp = 0;
    if ((*(unsigned int *)(v_rip + 14134282)) != 0) goto loc_0024C551;
loc_0024C11C:
    if (((*(unsigned __int8 *)(v_rip + 14133731)) & (33)) != 0) goto loc_0024C43E;
loc_0024C129:
    result = 2;
    if (!(condition_is_above_or_equal)) {
        a2 = (unsigned __int8)((unsigned __int8)(v_stack_m50));
        a1 = v_rdi;
        result = ExpWaitForSpinLockExclusiveAndAcquire(a1, a2, a3, a4);
        v_r14 = (unsigned int)(result);
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)))))) == 0x80000000ULL) goto loc_0024C17D;
loc_0024C14F:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)))))) >= 0x80000000ULL) {
    }
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((*(unsigned int *)(v_rip + 14127430)) & ((unsigned int)(v_r14))) == 0) goto loc_0024CB34;
loc_0024C16C:
loc_0024C16E:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)))))) != 0x80000000ULL) goto loc_0024C14F;
loc_0024C17D:
    *(unsigned __int8 *)(v_stack_p8 + 125) = 1;
    if (((*(unsigned __int8 *)(v_stack_p8 + 24)) & (1)) != 0) goto loc_0024C20E;
    if ((*(unsigned int *)(v_stack_p8 + 140)) != 0) goto loc_0024C20E;
    if ((*(unsigned __int8 *)(v_stack_p8 + 136)) == 0) goto loc_0024C20E;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 104))) != 0) goto loc_0024C20E;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 112))) != 0) goto loc_0024C20E;
    a4 = 0;
    a2 = 0;
    result = PopPepTriggerActivity(v_stack_p8, a2, a4 + 4, a4);
    a2 = 0;
    result = PopPepPromoteActivities(v_stack_p8, a2, a2 + 1, a4);
    if (a6 == 0) goto loc_0024C45D;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 104))) != 2) goto loc_0024C45D;
    a2 = 0;
    v_stack_m70 = a6;
    v_stack_m78 = v_stack_p8 + 120;
    result = PopPepStartActivity(v_stack_p8, a2, v_stack_p8 + 72, a2 + 4);
loc_0024C20E:
    a2 = 0;
    result = PopPepReleaseActivityLink(v_stack_p8, a2, 1, (unsigned __int8)((unsigned __int8)(v_stack_m50)));
loc_0024C21F:
    v_rsp = (v_rsp) + (96);
    return (unsigned __int8)((unsigned __int8)(result));
loc_0024C23C:
    if (((unsigned int)(v_stack_p8)) != 0) goto loc_0024C664;
    a2 = (a2) * ((unsigned int)(*(unsigned int *)(a3)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(v_stack_m50) + a2 * 4 + 4184))) != 0) goto loc_0024C273;
loc_0024C253:
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(v_stack_m50) + a2 * 4 + 4200))) != 0) goto loc_0024C292;
loc_0024C25E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(v_stack_m50) + a2 * 4 + 4204))) != 0) goto loc_0024C2B1;
loc_0024C269:
    goto loc_0024BAEE;
loc_0024C273:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(v_stack_m50) + a2 * 4 + 4204)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 72)))))) == 0) goto loc_0024C253;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 72))))) & (2)) != 0) {
    }
    goto loc_0024C253;
loc_0024C292:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(v_stack_m50) + a2 * 4 + 4204)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 104)))))) == 0) goto loc_0024C25E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 104))))) & (2)) != 0) {
    }
    goto loc_0024C25E;
loc_0024C2B1:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(v_stack_m50) + a2 * 4 + 4204)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 112)))))) == 0) goto loc_0024C269;
loc_0024C2BB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 112))))) & (2)) != 0) {
    }
    goto loc_0024C269;
loc_0024C2CD:
    if ((*(unsigned int *)(v_stack_p20 + 120)) > 0) goto loc_0024C9B3;
loc_0024C2D7:
    if (v_stack_p10 == 0) goto loc_0024C46D;
    if ((*(unsigned int *)(v_stack_p10 + 104)) <= 0) goto loc_0024C46D;
loc_0024C2FC:
    if (1 > 3) goto loc_0024C803;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + 64))))) & (2)) == 0) goto loc_0024C645;
loc_0024C314:
    result = (*(unsigned __int64 *)(v_stack_p10 + 64)) * ((int)(1));
    if ((*(unsigned __int64 *)(result + v_rip - 2409248 * 1 + 4264)) != (v_rip + 467969)) goto loc_0024C7E6;
    result = PopPepStartComponentActivatingActivity(v_stack_p20, v_stack_p10, a6, 1);
loc_0024C350:
    goto loc_0024C032;
loc_0024C374:
    v_stack_p34 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 120)));
    v_stack_p30 = 2;
    result = (*(unsigned __int64 *)(v_stack_p10 + (int)(1) * 8 + 56)) * (a6);
    goto loc_0024BA4B;
loc_0024C391:
    if (((*(unsigned __int8 *)(v_rip + 14133102)) & (1)) != 0) goto loc_0024CC10;
loc_0024C39E:
    v_r14 = 0;
    *(unsigned int *)(v_stack_p10) = 0;
loc_0024C3A5:
    result = ExReleaseSpinLockSharedFromDpcLevel(v_stack_p20 + 64, v_stack_p10, a6, 1);
    if ((*(unsigned int *)(v_rip + 14133608)) == 0) goto loc_0024C0EE;
    result = KiLowerIrqlProcessIrqlFlags(2, (unsigned __int8)(v_stack_p48), a6, 1);
    goto loc_0024C0EE;
loc_0024C3D5:
    if (((unsigned int)((unsigned __int8)(result))) == 6) goto loc_0024C4F3;
    if (((unsigned int)((unsigned __int8)(result))) > 5) goto loc_0024C4FD;
    a1 = (2) * ((unsigned __int8)(result));
    if ((*(unsigned __int8 *)(a1 + v_stack_p48 * 1 + 4144)) == 1) goto loc_0024B983;
    goto loc_0024C4FD;
loc_0024C401:
    if (result != (v_rip + 470440)) goto loc_0024C60D;
    result = PopPepCompleteComponentIdleStateChangeActivity(v_stack_p20, (unsigned __int8)(v_stack_p48), a6, 1);
    goto loc_0024BAC6;
loc_0024C41E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13376052))) != 0) goto loc_0024B9B2;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_stack_p20 + 64, (unsigned __int8)(a6), a6, 1);
    goto loc_0024BA11;
loc_0024C43E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13376020))) != 0) goto loc_0024C129;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_stack_p20 + 64, (unsigned __int8)(v_stack_p48), a6, 1);
    goto loc_0024C17D;
loc_0024C45D:
    result = PopPepRequestWork(v_stack_p20, 0, a6, 1);
    goto loc_0024C20E;
loc_0024C46D:
    if ((*(unsigned __int8 *)(v_stack_p20 + 125)) != 1) goto loc_0024C49D;
loc_0024C47D:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 180))))) goto loc_0024C49D;
    result = (0) * (0);
    if ((*(unsigned int *)(result + v_stack_p20 * 1 + 296)) > 0) goto loc_0024CA89;
    a2 = (unsigned int)((0) + 1);
    goto loc_0024C47D;
loc_0024C49D:
    if ((*(unsigned int *)(v_stack_p20 + 120)) <= 0) goto loc_0024C02C;
loc_0024C4B1:
    if (0 < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p20 + 180))))) goto loc_0024CC6B;
    result = PopPepGetReadyActivityType(v_stack_p20 + 72, 4, 4 + 1, 1);
    v_stack_p28 = a6;
    a2 = 0;
    v_stack_p20 = v_stack_p20 + 120;
    result = PopPepStartActivity(v_stack_p20, a2, v_stack_p20 + 72, (unsigned int)((unsigned int)(result)));
    goto loc_0024C02C;
loc_0024C4F3:
    if (0 == 6) goto loc_0024B983;
loc_0024C4FD:
    if (0 > 5) goto loc_0024C518;
    a1 = (v_stack_p20) * (0);
    if ((*(unsigned __int8 *)(a1 + v_stack_p48 * 1 + 4144)) == 1) goto loc_0024B983;
loc_0024C518:
    result = ExAcquireSpinLockShared(v_stack_p20 + 64, a2, v_stack_p20 + 72, (unsigned int)((unsigned int)(result)));
    v_stack_p48 = (unsigned __int8)(result);
    if ((*(unsigned __int8 *)(v_stack_p20 + 125)) == 1) goto loc_0024CC36;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_p10, a2, v_stack_p20 + 72, (unsigned int)((unsigned int)(result)));
    goto loc_0024BA15;
loc_0024C541:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)(result)), 2, v_stack_p20 + 72, (unsigned int)((unsigned int)(result)));
    goto loc_0024B9A5;
loc_0024C551:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p48), (unsigned __int8)(result), v_stack_p20 + 72, (unsigned int)((unsigned int)(result)));
    goto loc_0024C11C;
loc_0024C562:
    result = (unsigned int)((result) - ((unsigned int)(v_stack_p48)));
    if (condition_is_equal) goto loc_0024C07B;
    if ((unsigned __int8)(v_stack_p48) != 0) goto loc_0024C82D;
loc_0024C581:
    a4 = 0;
    a2 = 0;
    result = KeReleaseSemaphore(v_rip + 13376853, a2, 1, a4);
    v_r14 = 0;
loc_0024C59A:
loc_0024C5A7:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13376857))))) | (1));
    if (condition_is_not_equal) goto loc_0024C5A7;
    if (((1) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13376857))))) != 0) goto loc_0024C819;
    a4 = 0;
    result = ExpTryQueueWorkItem(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14133450) + 16), v_rip - 2409857 + 15786768 + v_r14 + v_r14 * 4 * 8, a4 + 48, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0024C80E;
loc_0024C5EB:
    v_rdi = ((unsigned int)((unsigned int)(result))) - (1);
    if (condition_is_not_equal) goto loc_0024C581;
loc_0024C5F8:
    goto loc_0024C07B;
loc_0024C60D:
    if (result != (v_rip + 472700)) goto loc_0024C944;
    result = PopPepCompleteDevicePowerOnActivity(v_stack_pA0, v_rip - 2409857 + 15786768 + v_r14 + v_r14 * 4 * 8, a4 + 48, a4);
    goto loc_0024BAC6;
loc_0024C62A:
    goto loc_0024BA93;
loc_0024C634:
    result = PopFxBugCheck((unsigned int)(0x667ULL), *(unsigned __int64 *)(v_stack_pA8 + (unsigned __int8)(result) * 8 + 56), a4 + 48, result);
loc_0024C645:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_pA8 + (unsigned __int8)(result) * 8 + 56))) & (8)) != 0) goto loc_0024C314;
    a4 = (unsigned int)((result) + 1);
    a1 = ((unsigned int)(0x667ULL)) + (8);
    goto loc_0024C2FC;
loc_0024C65A:
    goto loc_0024BE83;
loc_0024C664:
    if (((unsigned int)(a1)) != 2) goto loc_0024BAEE;
    if ((*(unsigned __int8 *)(v_stack_pA0 + 125)) == 0) goto loc_0024C689;
    result = (result) * ((unsigned int)(*(unsigned int *)(v_stack_p20 + 120)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 1 * 1 + 4184))) != 0) goto loc_0024C78C;
loc_0024C689:
    a2 = (*(unsigned __int64 *)(v_stack_pA8 + (unsigned __int8)(result) * 8 + 56)) * ((unsigned int)(*(unsigned int *)(v_stack_p20 + 120)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(1 + a2 * 4 + 4188))) != 0) goto loc_0024C6FB;
loc_0024C698:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(1 + a2 * 4 + 4192))) != 0) goto loc_0024C71E;
loc_0024C6A3:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(1 + a2 * 4 + 4196))) != 0) goto loc_0024C745;
loc_0024C6B2:
    if ((*(unsigned __int8 *)(v_stack_pA0 + 125)) == 0) goto loc_0024C269;
    result = (result) * ((unsigned int)(*(unsigned int *)(v_stack_p20 + 120)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 1 * 1 + 4200))) != 0) goto loc_0024C769;
loc_0024C6D2:
    result = (result) * ((unsigned int)(*(unsigned int *)(v_stack_p20 + 120)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 1 * 1 + 4204))) == 0) goto loc_0024C269;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + 1 * 1 + 4204)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA0 + 112)))))) == 0) goto loc_0024C269;
    goto loc_0024C2BB;
loc_0024C6FB:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + 1 * 1 + 4204)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA8 + 64)))))) == 0) goto loc_0024C698;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA8 + 64))))) & (2)) != 0) {
    }
    goto loc_0024C698;
loc_0024C71E:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + 1 * 1 + 4204)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA8 + 72)))))) == 0) goto loc_0024C6A3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA8 + 72))))) & (2)) != 0) {
    }
    goto loc_0024C6A3;
loc_0024C745:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + 1 * 1 + 4204)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA8 + 80)))))) == 0) goto loc_0024C6B2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA8 + 80))))) & (2)) != 0) {
    }
    goto loc_0024C6B2;
loc_0024C769:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + 1 * 1 + 4204)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA0 + 104)))))) == 0) goto loc_0024C6D2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA0 + 104))))) & (2)) != 0) {
    }
    goto loc_0024C6D2;
loc_0024C78C:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + 1 * 1 + 4204)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA0 + 72)))))) == 0) goto loc_0024C689;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA0 + 72))))) & (2)) != 0) {
    }
    goto loc_0024C689;
loc_0024C7AF:
    if ((*(unsigned __int64 *)(v_stack_pA0 + 72)) != (v_rip + 2192858)) goto loc_0024CBA6;
    result = PopPepTriggerComponentIdleStateChangeActivity(v_stack_pA0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA0 + 72))), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA8 + 72))), a4);
    goto loc_0024BBA5;
loc_0024C7CC:
    if (((unsigned int)(v_r11)) == 3) goto loc_0024C9A8;
    goto loc_0024BDB2;
loc_0024C7E6:
    if (((unsigned int)(*(unsigned int *)(v_stack_pA0 + 180))) != (v_rip + 466819)) goto loc_0024CA6C;
    result = PopPepStartDevicePowerOnActivity(v_stack_pA0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA0 + 72))), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA8 + 72))), a4);
    goto loc_0024C350;
loc_0024C803:
    goto loc_0024C314;
loc_0024C80E:
    result = (unsigned int)(~(1));
loc_0024C819:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((unsigned int)(v_r14)) >= 4) goto loc_0024C5EB;
    goto loc_0024C59A;
loc_0024C82D:
loc_0024C834:
    a4 = 0;
    a2 = 0;
    result = KeReleaseSemaphore(v_rip + 13376898, a2, (unsigned int)((unsigned int)(v_stack_pA0)), a4);
    v_r14 = 0;
loc_0024C84D:
loc_0024C85A:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13376902))))) | ((unsigned int)((unsigned int)((unsigned int)(v_stack_pA0)))));
    if (condition_is_not_equal) goto loc_0024C85A;
    if ((((unsigned int)((unsigned int)((unsigned int)(v_stack_pA0)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13376902))))) != 0) goto loc_0024C8AB;
    a4 = 0;
    result = ExpTryQueueWorkItem(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14132763) + 16), v_rip - 2410548 + 15787504 + v_r14 + v_r14 * 4 * 8, a4 + 48, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0024C8A0;
loc_0024C896:
    v_rdi = (1) - (v_stack_pA0);
    if (condition_is_not_equal) goto loc_0024C834;
    goto loc_0024C5F8;
loc_0024C8A0:
    result = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_pA0))))));
loc_0024C8AB:
    v_r14 = (unsigned int)((v_r14) + 1);
    if (((unsigned int)(v_r14)) >= 4) goto loc_0024C896;
    goto loc_0024C84D;
loc_0024C8B8:
    v_stack_p30 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14132763) + 16));
    if (((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14132763) + 16))) != 3) goto loc_0024BA60;
    v_stack_p30 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14132763) + 16));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pA0 + 180))) == 0) goto loc_0024BA60;
loc_0024C8F0:
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p20 + 120))) + (*(unsigned int *)(v_stack_pA0 + 296)));
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pA0 + 180))))) - (1);
    if (condition_is_not_equal) goto loc_0024C8F0;
    a2 = (a2) * (a4 + 48);
    goto loc_0024BA65;
loc_0024C90C:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 14132763) + 16))))) != 3) goto loc_0024C04F;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pA0 + 180))) == 0) goto loc_0024C04F;
loc_0024C930:
    result = (unsigned int)((v_stack_pA0 + 296 + 208) + (*(unsigned int *)(v_stack_pA0 + 296)));
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_pA0 + 180))) - (1);
    if (condition_is_not_equal) goto loc_0024C930;
    goto loc_0024C04F;
loc_0024C944:
    result = guard_dispatch_icall(v_stack_pA0 + 296 + 208, a2, a4 + 48, (unsigned int)(*(unsigned int *)(v_stack_pA0 + 180)));
    goto loc_0024BAC6;
loc_0024C94E:
    goto loc_0024BB0C;
loc_0024C955:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pA0 + 180)))))) == 3) goto loc_0024CA60;
    goto loc_0024BF66;
loc_0024C96F:
    a2 = 0;
    if (((unsigned int)(v_r14)) != 3) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pA0 + 180))); }
    v_stack_p38 = (unsigned int)(a2);
    a3 = (unsigned int)(*(unsigned int *)(v_stack_pA0 + 180)) - 1;
    if (((unsigned int)(v_r14)) != 3) { a3 = 0; }
    v_stack_p3C = a3;
    if (((unsigned int)(a2)) <= a3) goto loc_0024BCF2;
    goto loc_0024BED5;
loc_0024C99E:
    goto loc_0024BB5B;
loc_0024C9A8:
    goto loc_0024BDB2;
loc_0024C9B3:
loc_0024C9BA:
    if (condition_is_greater) goto loc_0024CB8A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_pA0 + 72))))) & (2)) == 0) goto loc_0024CAE4;
loc_0024C9D2:
    a2 = 0;
    result = (*(unsigned __int64 *)(v_stack_pA0 + 72)) * ((int)(0));
    if ((*(unsigned __int64 *)(result + v_rip - 2410988 * 1 + 4264)) != (v_rip + 466245)) goto loc_0024CB71;
    result = PopPepStartComponentActivatingActivity(v_stack_pA0, a2, a6, 0);
loc_0024CA0C:
    goto loc_0024C028;
loc_0024CA30:
    v_r13 = (unsigned int)((v_rip - 2410548) & (0xFFFFFFFEULL));
    v_r13 = (unsigned int)((v_r13) | (2));
    *(unsigned int *)(v_r12 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 4)));
    *(unsigned int *)(v_r12) = (unsigned int)(v_r13);
    goto loc_0024BE95;
loc_0024CA4F:
    if (((unsigned int)((unsigned int)(v_stack_p30))) != 2) goto loc_0024BBC1;
    goto loc_0024BBC1;
loc_0024CA60:
    goto loc_0024BF66;
loc_0024CA6C:
    if (((unsigned int)(*(unsigned int *)(v_r12 + 4))) != (v_rip + 466205)) goto loc_0024CC06;
    result = PopPepStartDevicePowerOffActivity(v_stack_pA0, 0, a6, (unsigned int)(*(unsigned int *)(v_r12 + 4)) - 1);
    goto loc_0024C350;
loc_0024CA89:
loc_0024CA9D:
    if (1 > 3) goto loc_0024CB9B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + v_stack_pA0 * 1 + 256))))) & (2)) == 0) goto loc_0024CB5C;
loc_0024CAB5:
    v_stack_p28 = a6;
    v_stack_p20 = result + v_stack_pA0 * 1 + 296;
    result = PopPepStartActivity(v_stack_pA0, result + v_stack_pA0 * 1 + 192, result + v_stack_pA0 * 1 + 248, 1);
    goto loc_0024C032;
loc_0024CAE4:
    if ((((unsigned __int8)(result + v_stack_pA0 * 1 + 248)) & (8)) != 0) goto loc_0024C9D2;
    a1 = (unsigned int)((v_stack_pA0) + 1);
    a2 = (result + v_stack_pA0 * 1 + 192) + (8);
    goto loc_0024C9BA;
loc_0024CAF9:
    v_r12 = 0;
    if ((*(unsigned __int8 *)(v_stack_pA0 + 136)) != 0) { v_r12 = 1; }
    goto loc_0024C070;
loc_0024CB0D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14131109)))) & (64)) == 0) goto loc_0024B9F8;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, result + v_stack_pA0 * 1 + 248, 1);
    if ((unsigned __int8)(result) == 0) goto loc_0024B9F8;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_pA0)))), a2, result + v_stack_pA0 * 1 + 248, 1);
    goto loc_0024B9FA;
loc_0024CB34:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14131070)))) & (64)) == 0) goto loc_0024C16C;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_pA0)))), a2, result + v_stack_pA0 * 1 + 248, 1);
    if ((unsigned __int8)(result) == 0) goto loc_0024C16C;
    result = HvlNotifyLongSpinWait(1, a2, result + v_stack_pA0 * 1 + 248, 1);
    goto loc_0024C16E;
loc_0024CB5C:
    if (((1) & (8)) != 0) goto loc_0024CAB5;
    a4 = (unsigned int)((1) + 1);
    a2 = (a2) + (8);
    goto loc_0024CA9D;
loc_0024CB71:
    if (result != (v_rip + 465912)) goto loc_0024CBB0;
    result = PopPepStartDevicePowerOnActivity(v_stack_pA0, a2, result + v_stack_pA0 * 1 + 248, a4);
    goto loc_0024CA0C;
loc_0024CB8A:
    v_stack_p30 = (unsigned int)((unsigned int)(v_stack_p30));
    goto loc_0024C2D7;
loc_0024CB93:
    goto loc_0024C04F;
loc_0024CB9B:
    goto loc_0024CAB5;
loc_0024CBA6:
    result = guard_dispatch_icall(v_stack_pA0, a2, result + v_stack_pA0 * 1 + 248, 6);
    goto loc_0024BBA5;
loc_0024CBB0:
    if (result != (v_rip + 465881)) goto loc_0024CC61;
    result = PopPepStartDevicePowerOffActivity(v_stack_pA0, a2, result + v_stack_pA0 * 1 + 248, 6);
    goto loc_0024CA0C;
loc_0024CBCD:
    result = ExReleaseSpinLockExclusive(v_stack_pA0 + 64, v_stack_p48, result + v_stack_pA0 * 1 + 248, 6);
    goto loc_0024C0F6;
loc_0024CBE3:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13374063))) != 0) goto loc_0024C0CC;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_stack_pA0 + 64, v_stack_p98, result + v_stack_pA0 * 1 + 248, 6);
    goto loc_0024C0CF;
loc_0024CC06:
    result = guard_dispatch_icall(v_stack_pA0 + 64, v_stack_p98, result + v_stack_pA0 * 1 + 248, 6);
    goto loc_0024C350;
loc_0024CC10:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13374018))) != 0) goto loc_0024C39E;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_r13, v_stack_p98, result + v_stack_pA0 * 1 + 248, 6);
    v_r14 = 0;
    goto loc_0024C3A5;
loc_0024CC36:
    result = ExReleaseSpinLockShared(v_stack_pA0 + 64, (unsigned __int8)(a6), result + v_stack_pA0 * 1 + 248, 6);
    goto loc_0024B983;
loc_0024CC4D:
    result = PopFxBugCheck((unsigned int)(0x666ULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_pA0)))), result + v_stack_pA0 * 1, (int)(2));
loc_0024CC61:
    result = guard_dispatch_icall((unsigned int)(0x666ULL), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_pA0)))), result + v_stack_pA0 * 1, (int)(2));
    goto loc_0024CA0C;
loc_0024CC6B:
    a1 = ((unsigned int)(0x666ULL)) * ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_pA0)))))));
    if ((*(unsigned int *)(a1 + v_stack_pA0 * 1 + 296)) > 0) goto loc_0024C02C;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_pA0))))) + 1);
    goto loc_0024C4B1;
}
```

## 5. (Beta) C Style

```c
int64_t PopPepProcessEvent(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint8_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint32_t v_stack_p3C;
    uint64_t v_stack_p48;
    uint64_t v_stack_p58;
    uint64_t v_stack_p8;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;

    v_stack_p20 = local_rbx;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (96);
    local_r12 = 0;
    v_stack_p18 = 0;
    if (Arg2 == 0) goto loc_0024B983;
    if ((*(uint32_t *)(arg1 + 0xB4)) != 1) goto loc_0024C3D5;
loc_0024B983:
    v_stack_p18 = 1;
    v_stack_m50 = v_cr8;
    if ((*(uint32_t *)(v_rip + 0xD7B381)) != 0) goto loc_0024C541;
loc_0024B9A5:
    if (((*(uint8_t *)(v_rip + 0xD7B15A)) & (33)) != 0) goto loc_0024C41E;
loc_0024B9B2:
    local_rsi = 0;
    if (!(condition_is_above_or_equal)) {
        Arg2 = (uint8_t)(v_cr8);
        Arg1 = Arg1 + 64;
        result = ExpWaitForSpinLockExclusiveAndAcquire(Arg1, Arg2, Arg3, Arg4);
        local_rsi = (uint32_t)(result);
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)))))) == 0x80000000ULL) goto loc_0024BA0A;
loc_0024B9DC:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)))))) >= 0x80000000ULL) {
    }
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xD798BA)) & ((uint32_t)(local_rsi))) == 0) goto loc_0024CB0D;
loc_0024B9F8:
loc_0024B9FA:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)))))) != 0x80000000ULL) goto loc_0024B9DC;
loc_0024BA0A:
loc_0024BA11:
    *(uint8_t *)(arg1 + 0x7D) = 1;
loc_0024BA15:
    if (((uint32_t)((int32_t)(Arg3))) == 6) goto loc_0024C374;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40))))) * ((int32_t)(Arg3));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + v_rip - 0x24BA11 * 1 + 0x103C)))) < 2) goto loc_0024C374;
    v_stack_m64 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x78)));
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(result + v_rip - 0x24BA11 * 1 + 0x103C)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + v_rip - 0x24BA11 * 1 + 0x103C)))) != 2) goto loc_0024C8B8;
loc_0024BA4B:
    local_r10 = (uint32_t)(*(uint32_t *)(arg1 + 0x78));
    if (Arg2 != 0) {
        local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x78))) + (*(uint32_t *)(Arg2 + 0x68)));
        v_stack_m64 = (uint32_t)(local_r10);
    }
    if (((uint32_t)((int32_t)(Arg3))) == 6) goto loc_0024BAC6;
loc_0024BA65:
    v_stack_m64 = (uint32_t)(local_r10);
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m68));
    if (((uint32_t)((int32_t)(Arg3))) > 5) goto loc_0024C62A;
    if ((*(uint8_t *)(result + v_rip - 0x24BA11 * 1 + 0x1030)) != 1) goto loc_0024C62A;
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m68));
    v_stack_m64 = (uint32_t)(local_r10);
loc_0024BA93:
    if ((((uint8_t)((int32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + (int32_t)(Arg3) * 8 + 0x48))))) & (4)) == 0) goto loc_0024C634;
    result = (uint32_t)(((int32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + (int32_t)(Arg3) * 8 + 0x48)))) & (0xFFFFFFFBULL));
    *(uint32_t *)(*(uint64_t *)(arg1 + (int32_t)(Arg3) * 8 + 0x48)) = (uint32_t)(result);
    if ((*(uint64_t *)(result + v_rip - 0x24BA11 * 1 + 0x10B0)) != (v_rip + 6982)) goto loc_0024C401;
    result = PopPepCompleteComponentActiveActivity(Arg1, Arg2, (int32_t)(Arg3), Arg4);
loc_0024BAC6:
    if (((uint32_t)((int32_t)(Arg4))) == 6) goto loc_0024BBAA;
    result = (result) * ((int32_t)(Arg4));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + v_rip - 0x24BA11 * 1 + 0x1034))) != 0) goto loc_0024C23C;
loc_0024BAEE:
    if (((uint32_t)((int32_t)(Arg4))) > 5) goto loc_0024BB09;
    result = (result) * ((int32_t)(Arg4));
    if ((*(uint8_t *)(result + v_rip - 0x24BA11 * 1 + 0x1030)) == 1) goto loc_0024C94E;
loc_0024BB09:
loc_0024BB0C:
    local_r11 = Arg1 + 72;
    if (0 != 1) { local_r11 = Arg2 + 56; }
loc_0024BB21:
    if (0 >= 6) goto loc_0024BB4D;
    if (*(uint64_t *)(local_r11 + 0x0 * 8) == 0) goto loc_0024BB46;
    Arg1 = (0) * ((int32_t)(Arg4));
    Arg1 = (Arg1) + (0);
    if (((*(uint32_t *)(*(uint64_t *)(local_r11 + 0x0 * 8))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x24BA11 + arg1 * 4 + 0x1040))))) != 0) goto loc_0024CC4D;
loc_0024BB46:
    Arg2 = (uint32_t)((0) + 1);
    result = (0) + 1;
    goto loc_0024BB21;
loc_0024BB4D:
    if (Arg2 == 0) goto loc_0024C99E;
loc_0024BB5B:
    *(uint32_t *)(*(uint64_t *)(Arg2 + (int32_t)(Arg4) * 8 + 0x38) + 0x4) = 0;
    Arg3 = 0;
    result = (*(uint64_t *)(Arg2 + (int32_t)(Arg4) * 8 + 0x38)) * ((int32_t)(Arg4));
    if ((*(uint64_t *)(result + v_rip - 0x24BA11 * 1 + 0x10A0)) == (v_rip + 7211)) goto loc_0024BB9D;
    if ((*(uint64_t *)(result + v_rip - 0x24BA11 * 1 + 0x10A0)) != (v_rip + 7382)) goto loc_0024C7AF;
    result = PopPepTriggerComponentActiveActivity(Arg1, Arg2, Arg3, Arg4);
    goto loc_0024BBA5;
loc_0024BB9D:
    result = PopPepTriggerComponentActivatingActivity(Arg1, Arg2, Arg3, Arg4);
loc_0024BBA5:
loc_0024BBAA:
    if ((uint32_t)((uint32_t)(v_stack_m68)) == 0) goto loc_0024C014;
    if (Arg2 == 0) goto loc_0024CA4F;
loc_0024BBC1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48))))) & (1)) == 0) goto loc_0024BCD8;
    Arg3 = v_rip - 2403168;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10)) == 0) { Arg3 = v_rip - 2403168; }
loc_0024BBF2:
    if (condition_is_greater) goto loc_0024BC16;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3))) == 0) goto loc_0024BC0A;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x48))) & ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3))))) != 0) goto loc_0024BCD8;
loc_0024BC0A:
    Arg2 = (uint32_t)((0) + 1);
    Arg4 = (Arg1 + 72) + (8);
    Arg3 = (Arg3) + (4);
    goto loc_0024BBF2;
loc_0024BC16:
    v_stack_m64 = (uint32_t)((uint32_t)(v_stack_m64));
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m68));
loc_0024BC29:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB4))) != 0) goto loc_0024BC81;
    Arg2 = v_rip - 2403253;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10)) == 0) { Arg2 = v_rip - 2403260; }
loc_0024BC4E:
    if (1 > 3) goto loc_0024BC7C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))) == 0) goto loc_0024BC70;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB4))))) * ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB4)))));
    result = (result) + (1);
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + result * 8 + 0xF8))) & ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))))) != 0) goto loc_0024BCD8;
loc_0024BC70:
    Arg3 = (uint32_t)((1) + 1);
    local_r10 = (1) + 1;
    Arg2 = (Arg2) + (4);
    goto loc_0024BC4E;
loc_0024BC7C:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB4))) + 1);
    goto loc_0024BC29;
loc_0024BC81:
    Arg2 = v_rip - 2403315;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10)) == 0) { Arg2 = v_rip - 2403346; }
loc_0024BCA0:
    if (4 > 5) goto loc_0024BCC3;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))) == 0) goto loc_0024BCB6;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x68))) & ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))))) != 0) goto loc_0024BCD8;
loc_0024BCB6:
    Arg3 = (uint32_t)((4) + 1);
    Arg4 = (Arg1 + 104) + (8);
    Arg2 = (Arg2) + (4);
    goto loc_0024BCA0;
loc_0024BCC3:
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48)))) & (0xFFFFFFFEULL));
    local_r11 = (uint32_t)((local_r11) | (2));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x4)));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x48)) = (uint32_t)(local_r11);
loc_0024BCD8:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m68))))) != 2) goto loc_0024C96F;
    v_stack_m60 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8)))));
    v_stack_m5C = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8)));
loc_0024BCF2:
loc_0024BCF6:
    local_rdi = ((uint32_t)(*(uint32_t *)(Arg2))) * ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x8)))))));
    local_rdi = (local_rdi) + (192);
    v_stack_m48 = 3;
    local_rdi = (local_rdi) + (Arg1);
    v_stack_m40 = local_rdi;
loc_0024BD2A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(64 + local_rdi * 1))))) & (1)) == 0) goto loc_0024BE95;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x24AC3F))) == 0) goto loc_0024CA30;
    local_rsi = 0;
    v_stack_p28 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(64 + local_rdi * 1) + 0x10));
    Arg2 = v_rip - 2403551;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(64 + local_rdi * 1) + 0x10)) == 0) { Arg2 = v_rip - 2403557; }
    Arg2 = (Arg2) + (136);
loc_0024BD7C:
    if (condition_is_greater) goto loc_0024BDA2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))) == 0) goto loc_0024BD95;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x48))) & ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))))) != 0) goto loc_0024BE83;
loc_0024BD95:
    Arg3 = (uint32_t)((0) + 1);
    local_r10 = (Arg1 + 72) + (8);
    Arg2 = (Arg2) + (4);
    goto loc_0024BD7C;
loc_0024BDA2:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x24AC3F)))) != 2) goto loc_0024C7CC;
loc_0024BDB2:
    local_rsi = v_rip - 2403636;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(64 + local_rdi * 1) + 0x10))) == 0) { local_rsi = v_rip - 2403667; }
    local_rsi = (local_rsi) + (4);
loc_0024BDCB:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))))) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))) goto loc_0024BE16;
loc_0024BDDE:
    if (1 > 3) goto loc_0024BE11;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x88 * 1))) == 0) goto loc_0024BE06;
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))))) * ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))))));
    result = (result) + (1);
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p8 + result * 8 + 0xF8))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x88 * 1))))) != 0) goto loc_0024C65A;
loc_0024BE06:
    Arg2 = (uint32_t)((1) + 1);
    local_r10 = (1) + 1;
    Arg3 = (local_rsi + 136 * 1) + (4);
    goto loc_0024BDDE;
loc_0024BE11:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8))))) + 1);
    goto loc_0024BDCB;
loc_0024BE16:
    Arg2 = v_rip - 2403725;
    if (Arg5 == 0) { Arg2 = v_rip - 2403756; }
    Arg2 = (Arg2) + (136);
loc_0024BE3D:
    if (4 > 5) goto loc_0024BE64;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))) == 0) goto loc_0024BE57;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x68))) & ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))))) != 0) goto loc_0024C65A;
loc_0024BE57:
    Arg3 = (uint32_t)((4) + 1);
    local_r10 = (v_stack_p8 + 104) + (8);
    Arg2 = (Arg2) + (4);
    goto loc_0024BE3D;
loc_0024BE64:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(64 + local_rdi * 1)))) & (0xFFFFFFFEULL));
    local_r13 = (uint32_t)((local_r13) | (2));
    *(uint32_t *)(*(uint64_t *)(64 + local_rdi * 1)) = (uint32_t)(local_r13);
    *(uint32_t *)(*(uint64_t *)(64 + local_rdi * 1) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(64 + local_rdi * 1) + 0x4)));
loc_0024BE83:
loc_0024BE95:
    local_rbp = (136) + (136);
    local_r14 = (64) + (8);
    local_r15 = (v_rip - 2403391) + (136);
    Arg1 = (v_stack_m48) - (1);
    v_stack_m48 = Arg1;
    if (condition_is_not_equal) goto loc_0024BD2A;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m60)) + 1);
    v_stack_m60 = (uint32_t)(Arg2);
    if (((uint32_t)(Arg2)) <= ((uint32_t)((uint32_t)(v_stack_m5C)))) goto loc_0024BCF6;
    local_r12 = 0;
loc_0024BED5:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x68)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x68))))) & (1)) != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x68)))) & (0xFFFFFFFEULL));
        result = (uint32_t)((result) | (2));
        *(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x68)) = (uint32_t)(result);
        result = *(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x68) + 0x4);
        *(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x68) + 0x8) = (uint32_t)(result);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x70))))) & (1)) == 0) goto loc_0024C010;
    if ((uint32_t)(*(uint64_t *)(v_rip - 0x24AC2A)) == 0) goto loc_0024BFFE;
    Arg2 = v_rip - 2403320;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p8 + 0x70) + 0x10)) == 0) { Arg2 = v_rip - 2403334; }
loc_0024BF2F:
    if (condition_is_greater) goto loc_0024BF55;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))) == 0) goto loc_0024BF48;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x48))) & ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))))) != 0) goto loc_0024C010;
loc_0024BF48:
    Arg3 = (uint32_t)((0) + 1);
    local_r10 = (v_stack_p8 + 72) + (8);
    Arg2 = (Arg2) + (4);
    goto loc_0024BF2F;
loc_0024BF55:
    if (((uint32_t)(*(uint64_t *)(v_rip - 0x24AC2A))) != 2) goto loc_0024C955;
loc_0024BF66:
loc_0024BF6D:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m40 + 0x8)))))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m40 + 0x8))))) goto loc_0024BFBD;
    local_r10 = v_rip - 2403402;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p8 + 0x70) + 0x10)) == 0) { local_r10 = v_rip - 2403409; }
loc_0024BF8B:
    if (1 > 3) goto loc_0024BFB9;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10))) == 0) goto loc_0024BFAD;
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m40 + 0x8))))))) * ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m40 + 0x8)))))));
    result = (result) + (1);
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p8 + result * 8 + 0xF8))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10))))) != 0) goto loc_0024C010;
loc_0024BFAD:
    Arg3 = (uint32_t)((1) + 1);
    local_r11 = (1) + 1;
    local_r10 = (local_r10) + (4);
    goto loc_0024BF8B;
loc_0024BFB9:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m40 + 0x8))))) + 1);
    goto loc_0024BF6D;
loc_0024BFBD:
    Arg3 = v_rip - 2403470;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p8 + 0x70) + 0x10)) == 0) { Arg3 = v_rip - 2403487; }
loc_0024BFDB:
    if (4 > 5) goto loc_0024BFFC;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3))) == 0) goto loc_0024BFF0;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x68))) & ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3))))) != 0) goto loc_0024C010;
loc_0024BFF0:
    Arg2 = (uint32_t)((4) + 1);
    Arg4 = (v_stack_p8 + 104) + (8);
    Arg3 = (Arg3) + (4);
    goto loc_0024BFDB;
loc_0024BFFC:
loc_0024BFFE:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x70)))) & (0xFFFFFFFEULL));
    result = (uint32_t)((result) | (2));
    *(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x70)) = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x70) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x70) + 0x4)));
loc_0024C010:
loc_0024C014:
    local_rbp = 0;
    if (Arg6 != 0) goto loc_0024C2CD;
loc_0024C028:
loc_0024C02C:
loc_0024C032:
    if ((uint32_t)((uint32_t)(v_stack_m68)) == 0) goto loc_0024CB93;
    if (((uint32_t)((uint32_t)(v_stack_m68))) != 2) goto loc_0024C90C;
    result = (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x78));
    if (v_stack_p10 != 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x78))) + (*(uint32_t *)(v_stack_p10 + 0x68)));
    }
    local_r12 = 0;
    if ((((uint8_t)(*(uint64_t *)(v_stack_p8 + 0x18))) & (1)) != 0) goto loc_0024C070;
    if ((uint32_t)(result) != 0) goto loc_0024C070;
    if (0 != 0) goto loc_0024C070;
    if ((*(uint32_t *)(v_stack_p8 + 0x8C)) == ((uint32_t)(result))) goto loc_0024CAF9;
loc_0024C070:
    Arg1 = (uint32_t)((*(uint64_t *)(v_stack_p8 + 0x18)) & (32));
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(v_stack_m64)))) goto loc_0024C562;
loc_0024C07B:
    if (v_stack_p18 != 1) goto loc_0024C391;
    local_r14 = 0;
loc_0024C090:
    if (0 >= 6) goto loc_0024C0AE;
    if (*(uint64_t *)(v_stack_p8 + 0x0 * 8 + 0x48) == 0) goto loc_0024C0AA;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x0 * 8 + 0x48))) != 0) goto loc_0024CBCD;
loc_0024C0AA:
    Arg1 = (uint32_t)((0) + 1);
    goto loc_0024C090;
loc_0024C0AE:
    if ((*(uint8_t *)(v_stack_p8 + 0x88)) != 0) {
        *(uint8_t *)(v_stack_p8 + 0x7D) = 0;
    }
    if (((*(uint8_t *)(v_rip + 0xD7AA44)) & (1)) != 0) goto loc_0024CBE3;
loc_0024C0CC:
    *(uint32_t *)(v_stack_p8 + 0x40) = 0;
loc_0024C0CF:
    result = 0;
    local_rdi = v_stack_p8 + 64;
    if ((*(uint32_t *)(v_rip + 0xD7AC4A)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_stack_m50);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
        local_rdi = v_stack_p8 + 64;
    }
loc_0024C0F6:
    if (0 == 0) goto loc_0024C21F;
    local_rbp = 0;
    if ((*(uint32_t *)(v_rip + 0xD7AC0A)) != 0) goto loc_0024C551;
loc_0024C11C:
    if (((*(uint8_t *)(v_rip + 0xD7A9E3)) & (33)) != 0) goto loc_0024C43E;
loc_0024C129:
    result = 2;
    if (!(condition_is_above_or_equal)) {
        Arg2 = (uint8_t)((uint8_t)(v_stack_m50));
        Arg1 = local_rdi;
        result = ExpWaitForSpinLockExclusiveAndAcquire(Arg1, Arg2, Arg3, Arg4);
        local_r14 = (uint32_t)(result);
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)))))) == 0x80000000ULL) goto loc_0024C17D;
loc_0024C14F:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)))))) >= 0x80000000ULL) {
    }
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((*(uint32_t *)(v_rip + 0xD79146)) & ((uint32_t)(local_r14))) == 0) goto loc_0024CB34;
loc_0024C16C:
loc_0024C16E:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)))))) != 0x80000000ULL) goto loc_0024C14F;
loc_0024C17D:
    *(uint8_t *)(v_stack_p8 + 0x7D) = 1;
    if (((*(uint8_t *)(v_stack_p8 + 0x18)) & (1)) != 0) goto loc_0024C20E;
    if ((*(uint32_t *)(v_stack_p8 + 0x8C)) != 0) goto loc_0024C20E;
    if ((*(uint8_t *)(v_stack_p8 + 0x88)) == 0) goto loc_0024C20E;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x68))) != 0) goto loc_0024C20E;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x70))) != 0) goto loc_0024C20E;
    Arg4 = 0;
    Arg2 = 0;
    result = PopPepTriggerActivity(v_stack_p8, Arg2, Arg4 + 4, Arg4);
    Arg2 = 0;
    result = PopPepPromoteActivities(v_stack_p8, Arg2, Arg2 + 1, Arg4);
    if (Arg6 == 0) goto loc_0024C45D;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x68))) != 2) goto loc_0024C45D;
    Arg2 = 0;
    v_stack_m70 = Arg6;
    v_stack_m78 = v_stack_p8 + 120;
    result = PopPepStartActivity(v_stack_p8, Arg2, v_stack_p8 + 72, Arg2 + 4);
loc_0024C20E:
    Arg2 = 0;
    result = PopPepReleaseActivityLink(v_stack_p8, Arg2, 1, (uint8_t)((uint8_t)(v_stack_m50)));
loc_0024C21F:
    local_rsp = (local_rsp) + (96);
    return (uint8_t)((uint8_t)(result));
loc_0024C23C:
    if (((uint32_t)(v_stack_p8)) != 0) goto loc_0024C664;
    Arg2 = (Arg2) * ((uint32_t)(*(uint32_t *)(Arg3)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(v_stack_m50) + Arg2 * 4 + 0x1058))) != 0) goto loc_0024C273;
loc_0024C253:
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(v_stack_m50) + Arg2 * 4 + 0x1068))) != 0) goto loc_0024C292;
loc_0024C25E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(v_stack_m50) + Arg2 * 4 + 0x106C))) != 0) goto loc_0024C2B1;
loc_0024C269:
    goto loc_0024BAEE;
loc_0024C273:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(v_stack_m50) + Arg2 * 4 + 0x106C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x48)))))) == 0) goto loc_0024C253;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x48))))) & (2)) != 0) {
    }
    goto loc_0024C253;
loc_0024C292:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(v_stack_m50) + Arg2 * 4 + 0x106C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x68)))))) == 0) goto loc_0024C25E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x68))))) & (2)) != 0) {
    }
    goto loc_0024C25E;
loc_0024C2B1:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(v_stack_m50) + Arg2 * 4 + 0x106C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x70)))))) == 0) goto loc_0024C269;
loc_0024C2BB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x70))))) & (2)) != 0) {
    }
    goto loc_0024C269;
loc_0024C2CD:
    if ((*(uint32_t *)(v_stack_p20 + 0x78)) > 0) goto loc_0024C9B3;
loc_0024C2D7:
    if (v_stack_p10 == 0) goto loc_0024C46D;
    if ((*(uint32_t *)(v_stack_p10 + 0x68)) <= 0) goto loc_0024C46D;
loc_0024C2FC:
    if (1 > 3) goto loc_0024C803;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p10 + 0x40))))) & (2)) == 0) goto loc_0024C645;
loc_0024C314:
    result = (*(uint64_t *)(v_stack_p10 + 0x40)) * ((int32_t)(1));
    if ((*(uint64_t *)(result + v_rip - 0x24C320 * 1 + 0x10A8)) != (v_rip + 467969)) goto loc_0024C7E6;
    result = PopPepStartComponentActivatingActivity(v_stack_p20, v_stack_p10, Arg6, 1);
loc_0024C350:
    goto loc_0024C032;
loc_0024C374:
    v_stack_p34 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x78)));
    v_stack_p30 = 2;
    result = (*(uint64_t *)(v_stack_p10 + (int32_t)(1) * 8 + 0x38)) * (Arg6);
    goto loc_0024BA4B;
loc_0024C391:
    if (((*(uint8_t *)(v_rip + 0xD7A76E)) & (1)) != 0) goto loc_0024CC10;
loc_0024C39E:
    local_r14 = 0;
    *(uint32_t *)(v_stack_p10) = 0;
loc_0024C3A5:
    result = ExReleaseSpinLockSharedFromDpcLevel(v_stack_p20 + 64, v_stack_p10, Arg6, 1);
    if ((*(uint32_t *)(v_rip + 0xD7A968)) == 0) goto loc_0024C0EE;
    result = KiLowerIrqlProcessIrqlFlags(2, (uint8_t)(v_stack_p48), Arg6, 1);
    goto loc_0024C0EE;
loc_0024C3D5:
    if (((uint32_t)((uint8_t)(result))) == 6) goto loc_0024C4F3;
    if (((uint32_t)((uint8_t)(result))) > 5) goto loc_0024C4FD;
    Arg1 = (2) * ((uint8_t)(result));
    if ((*(uint8_t *)(arg1 + v_stack_p48 * 1 + 0x1030)) == 1) goto loc_0024B983;
    goto loc_0024C4FD;
loc_0024C401:
    if (result != (v_rip + 470440)) goto loc_0024C60D;
    result = PopPepCompleteComponentIdleStateChangeActivity(v_stack_p20, (uint8_t)(v_stack_p48), Arg6, 1);
    goto loc_0024BAC6;
loc_0024C41E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCC1A34))) != 0) goto loc_0024B9B2;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_stack_p20 + 64, (uint8_t)(Arg6), Arg6, 1);
    goto loc_0024BA11;
loc_0024C43E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCC1A14))) != 0) goto loc_0024C129;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_stack_p20 + 64, (uint8_t)(v_stack_p48), Arg6, 1);
    goto loc_0024C17D;
loc_0024C45D:
    result = PopPepRequestWork(v_stack_p20, 0, Arg6, 1);
    goto loc_0024C20E;
loc_0024C46D:
    if ((*(uint8_t *)(v_stack_p20 + 0x7D)) != 1) goto loc_0024C49D;
loc_0024C47D:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0xB4))))) goto loc_0024C49D;
    result = (0) * (0);
    if ((*(uint32_t *)(result + v_stack_p20 * 1 + 0x128)) > 0) goto loc_0024CA89;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_0024C47D;
loc_0024C49D:
    if ((*(uint32_t *)(v_stack_p20 + 0x78)) <= 0) goto loc_0024C02C;
loc_0024C4B1:
    if (0 < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0xB4))))) goto loc_0024CC6B;
    result = PopPepGetReadyActivityType(v_stack_p20 + 72, 4, 4 + 1, 1);
    v_stack_p28 = Arg6;
    Arg2 = 0;
    v_stack_p20 = v_stack_p20 + 120;
    result = PopPepStartActivity(v_stack_p20, Arg2, v_stack_p20 + 72, (uint32_t)((uint32_t)(result)));
    goto loc_0024C02C;
loc_0024C4F3:
    if (0 == 6) goto loc_0024B983;
loc_0024C4FD:
    if (0 > 5) goto loc_0024C518;
    Arg1 = (v_stack_p20) * (0);
    if ((*(uint8_t *)(arg1 + v_stack_p48 * 1 + 0x1030)) == 1) goto loc_0024B983;
loc_0024C518:
    result = ExAcquireSpinLockShared(v_stack_p20 + 64, Arg2, v_stack_p20 + 72, (uint32_t)((uint32_t)(result)));
    v_stack_p48 = (uint8_t)(result);
    if ((*(uint8_t *)(v_stack_p20 + 0x7D)) == 1) goto loc_0024CC36;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_stack_p10, Arg2, v_stack_p20 + 72, (uint32_t)((uint32_t)(result)));
    goto loc_0024BA15;
loc_0024C541:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)(result)), 2, v_stack_p20 + 72, (uint32_t)((uint32_t)(result)));
    goto loc_0024B9A5;
loc_0024C551:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p48), (uint8_t)(result), v_stack_p20 + 72, (uint32_t)((uint32_t)(result)));
    goto loc_0024C11C;
loc_0024C562:
    result = (uint32_t)((result) - ((uint32_t)(v_stack_p48)));
    if (condition_is_equal) goto loc_0024C07B;
    if ((uint8_t)(v_stack_p48) != 0) goto loc_0024C82D;
loc_0024C581:
    Arg4 = 0;
    Arg2 = 0;
    result = KeReleaseSemaphore(v_rip + 13376853, Arg2, 1, Arg4);
    local_r14 = 0;
loc_0024C59A:
loc_0024C5A7:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCC1D59))))) | (1));
    if (condition_is_not_equal) goto loc_0024C5A7;
    if (((1) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCC1D59))))) != 0) goto loc_0024C819;
    Arg4 = 0;
    result = ExpTryQueueWorkItem(*(uint64_t *)(*(uint64_t *)(v_rip + 0xD7A8CA) + 0x10), v_rip - 2409857 + 15786768 + local_r14 + local_r14 * 4 * 8, Arg4 + 48, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0024C80E;
loc_0024C5EB:
    local_rdi = ((uint32_t)((uint32_t)(result))) - (1);
    if (condition_is_not_equal) goto loc_0024C581;
loc_0024C5F8:
    goto loc_0024C07B;
loc_0024C60D:
    if (result != (v_rip + 472700)) goto loc_0024C944;
    result = PopPepCompleteDevicePowerOnActivity(v_stack_pA0, v_rip - 2409857 + 15786768 + local_r14 + local_r14 * 4 * 8, Arg4 + 48, Arg4);
    goto loc_0024BAC6;
loc_0024C62A:
    goto loc_0024BA93;
loc_0024C634:
    result = PopFxBugCheck((uint32_t)(0x667ULL), *(uint64_t *)(v_stack_pA8 + (uint8_t)(result) * 8 + 0x38), Arg4 + 48, result);
loc_0024C645:
    if ((((uint8_t)(*(uint64_t *)(v_stack_pA8 + (uint8_t)(result) * 8 + 0x38))) & (8)) != 0) goto loc_0024C314;
    Arg4 = (uint32_t)((result) + 1);
    Arg1 = ((uint32_t)(0x667ULL)) + (8);
    goto loc_0024C2FC;
loc_0024C65A:
    goto loc_0024BE83;
loc_0024C664:
    if (((uint32_t)(Arg1)) != 2) goto loc_0024BAEE;
    if ((*(uint8_t *)(v_stack_pA0 + 0x7D)) == 0) goto loc_0024C689;
    result = (result) * ((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x78)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1 * 1 + 0x1058))) != 0) goto loc_0024C78C;
loc_0024C689:
    Arg2 = (*(uint64_t *)(v_stack_pA8 + (uint8_t)(result) * 8 + 0x38)) * ((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x78)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(1 + Arg2 * 4 + 0x105C))) != 0) goto loc_0024C6FB;
loc_0024C698:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(1 + Arg2 * 4 + 0x1060))) != 0) goto loc_0024C71E;
loc_0024C6A3:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(1 + Arg2 * 4 + 0x1064))) != 0) goto loc_0024C745;
loc_0024C6B2:
    if ((*(uint8_t *)(v_stack_pA0 + 0x7D)) == 0) goto loc_0024C269;
    result = (result) * ((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x78)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1 * 1 + 0x1068))) != 0) goto loc_0024C769;
loc_0024C6D2:
    result = (result) * ((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x78)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1 * 1 + 0x106C))) == 0) goto loc_0024C269;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1 * 1 + 0x106C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA0 + 0x70)))))) == 0) goto loc_0024C269;
    goto loc_0024C2BB;
loc_0024C6FB:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1 * 1 + 0x106C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA8 + 0x40)))))) == 0) goto loc_0024C698;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA8 + 0x40))))) & (2)) != 0) {
    }
    goto loc_0024C698;
loc_0024C71E:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1 * 1 + 0x106C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA8 + 0x48)))))) == 0) goto loc_0024C6A3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA8 + 0x48))))) & (2)) != 0) {
    }
    goto loc_0024C6A3;
loc_0024C745:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1 * 1 + 0x106C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA8 + 0x50)))))) == 0) goto loc_0024C6B2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA8 + 0x50))))) & (2)) != 0) {
    }
    goto loc_0024C6B2;
loc_0024C769:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1 * 1 + 0x106C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA0 + 0x68)))))) == 0) goto loc_0024C6D2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA0 + 0x68))))) & (2)) != 0) {
    }
    goto loc_0024C6D2;
loc_0024C78C:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1 * 1 + 0x106C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA0 + 0x48)))))) == 0) goto loc_0024C689;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA0 + 0x48))))) & (2)) != 0) {
    }
    goto loc_0024C689;
loc_0024C7AF:
    if ((*(uint64_t *)(v_stack_pA0 + 0x48)) != (v_rip + 2192858)) goto loc_0024CBA6;
    result = PopPepTriggerComponentIdleStateChangeActivity(v_stack_pA0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA0 + 0x48))), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA8 + 0x48))), Arg4);
    goto loc_0024BBA5;
loc_0024C7CC:
    if (((uint32_t)(local_r11)) == 3) goto loc_0024C9A8;
    goto loc_0024BDB2;
loc_0024C7E6:
    if (((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0xB4))) != (v_rip + 466819)) goto loc_0024CA6C;
    result = PopPepStartDevicePowerOnActivity(v_stack_pA0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA0 + 0x48))), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA8 + 0x48))), Arg4);
    goto loc_0024C350;
loc_0024C803:
    goto loc_0024C314;
loc_0024C80E:
    result = (uint32_t)(~(1));
loc_0024C819:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((uint32_t)(local_r14)) >= 4) goto loc_0024C5EB;
    goto loc_0024C59A;
loc_0024C82D:
loc_0024C834:
    Arg4 = 0;
    Arg2 = 0;
    result = KeReleaseSemaphore(v_rip + 13376898, Arg2, (uint32_t)((uint32_t)(v_stack_pA0)), Arg4);
    local_r14 = 0;
loc_0024C84D:
loc_0024C85A:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCC1D86))))) | ((uint32_t)((uint32_t)((uint32_t)(v_stack_pA0)))));
    if (condition_is_not_equal) goto loc_0024C85A;
    if ((((uint32_t)((uint32_t)((uint32_t)(v_stack_pA0)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCC1D86))))) != 0) goto loc_0024C8AB;
    Arg4 = 0;
    result = ExpTryQueueWorkItem(*(uint64_t *)(*(uint64_t *)(v_rip + 0xD7A61B) + 0x10), v_rip - 2410548 + 15787504 + local_r14 + local_r14 * 4 * 8, Arg4 + 48, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0024C8A0;
loc_0024C896:
    local_rdi = (1) - (v_stack_pA0);
    if (condition_is_not_equal) goto loc_0024C834;
    goto loc_0024C5F8;
loc_0024C8A0:
    result = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_pA0))))));
loc_0024C8AB:
    local_r14 = (uint32_t)((local_r14) + 1);
    if (((uint32_t)(local_r14)) >= 4) goto loc_0024C896;
    goto loc_0024C84D;
loc_0024C8B8:
    v_stack_p30 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xD7A61B) + 0x10));
    if (((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xD7A61B) + 0x10))) != 3) goto loc_0024BA60;
    v_stack_p30 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xD7A61B) + 0x10));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0xB4))) == 0) goto loc_0024BA60;
loc_0024C8F0:
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x78))) + (*(uint32_t *)(v_stack_pA0 + 0x128)));
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0xB4))))) - (1);
    if (condition_is_not_equal) goto loc_0024C8F0;
    Arg2 = (Arg2) * (Arg4 + 48);
    goto loc_0024BA65;
loc_0024C90C:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xD7A61B) + 0x10))))) != 3) goto loc_0024C04F;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0xB4))) == 0) goto loc_0024C04F;
loc_0024C930:
    result = (uint32_t)((v_stack_pA0 + 296 + 208) + (*(uint32_t *)(v_stack_pA0 + 0x128)));
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0xB4))) - (1);
    if (condition_is_not_equal) goto loc_0024C930;
    goto loc_0024C04F;
loc_0024C944:
    result = guard_dispatch_icall(v_stack_pA0 + 296 + 208, Arg2, Arg4 + 48, (uint32_t)(*(uint32_t *)(v_stack_pA0 + 0xB4)));
    goto loc_0024BAC6;
loc_0024C94E:
    goto loc_0024BB0C;
loc_0024C955:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0xB4)))))) == 3) goto loc_0024CA60;
    goto loc_0024BF66;
loc_0024C96F:
    Arg2 = 0;
    if (((uint32_t)(local_r14)) != 3) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pA0 + 0xB4))); }
    v_stack_p38 = (uint32_t)(Arg2);
    Arg3 = (uint32_t)(*(uint32_t *)(v_stack_pA0 + 0xB4)) - 1;
    if (((uint32_t)(local_r14)) != 3) { Arg3 = 0; }
    v_stack_p3C = Arg3;
    if (((uint32_t)(Arg2)) <= Arg3) goto loc_0024BCF2;
    goto loc_0024BED5;
loc_0024C99E:
    goto loc_0024BB5B;
loc_0024C9A8:
    goto loc_0024BDB2;
loc_0024C9B3:
loc_0024C9BA:
    if (condition_is_greater) goto loc_0024CB8A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_pA0 + 0x48))))) & (2)) == 0) goto loc_0024CAE4;
loc_0024C9D2:
    Arg2 = 0;
    result = (*(uint64_t *)(v_stack_pA0 + 0x48)) * ((int32_t)(0));
    if ((*(uint64_t *)(result + v_rip - 0x24C9EC * 1 + 0x10A8)) != (v_rip + 466245)) goto loc_0024CB71;
    result = PopPepStartComponentActivatingActivity(v_stack_pA0, Arg2, Arg6, 0);
loc_0024CA0C:
    goto loc_0024C028;
loc_0024CA30:
    local_r13 = (uint32_t)((v_rip - 2410548) & (0xFFFFFFFEULL));
    local_r13 = (uint32_t)((local_r13) | (2));
    *(uint32_t *)(local_r12 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x4)));
    *(uint32_t *)(local_r12) = (uint32_t)(local_r13);
    goto loc_0024BE95;
loc_0024CA4F:
    if (((uint32_t)((uint32_t)(v_stack_p30))) != 2) goto loc_0024BBC1;
    goto loc_0024BBC1;
loc_0024CA60:
    goto loc_0024BF66;
loc_0024CA6C:
    if (((uint32_t)(*(uint32_t *)(local_r12 + 0x4))) != (v_rip + 466205)) goto loc_0024CC06;
    result = PopPepStartDevicePowerOffActivity(v_stack_pA0, 0, Arg6, (uint32_t)(*(uint32_t *)(local_r12 + 0x4)) - 1);
    goto loc_0024C350;
loc_0024CA89:
loc_0024CA9D:
    if (1 > 3) goto loc_0024CB9B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + v_stack_pA0 * 1 + 0x100))))) & (2)) == 0) goto loc_0024CB5C;
loc_0024CAB5:
    v_stack_p28 = Arg6;
    v_stack_p20 = result + v_stack_pA0 * 1 + 296;
    result = PopPepStartActivity(v_stack_pA0, result + v_stack_pA0 * 1 + 192, result + v_stack_pA0 * 1 + 248, 1);
    goto loc_0024C032;
loc_0024CAE4:
    if ((((uint8_t)(result + v_stack_pA0 * 1 + 248)) & (8)) != 0) goto loc_0024C9D2;
    Arg1 = (uint32_t)((v_stack_pA0) + 1);
    Arg2 = (result + v_stack_pA0 * 1 + 192) + (8);
    goto loc_0024C9BA;
loc_0024CAF9:
    local_r12 = 0;
    if ((*(uint8_t *)(v_stack_pA0 + 0x88)) != 0) { local_r12 = 1; }
    goto loc_0024C070;
loc_0024CB0D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD79FA5)))) & (64)) == 0) goto loc_0024B9F8;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, result + v_stack_pA0 * 1 + 248, 1);
    if ((uint8_t)(result) == 0) goto loc_0024B9F8;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_pA0)))), Arg2, result + v_stack_pA0 * 1 + 248, 1);
    goto loc_0024B9FA;
loc_0024CB34:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD79F7E)))) & (64)) == 0) goto loc_0024C16C;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_pA0)))), Arg2, result + v_stack_pA0 * 1 + 248, 1);
    if ((uint8_t)(result) == 0) goto loc_0024C16C;
    result = HvlNotifyLongSpinWait(1, Arg2, result + v_stack_pA0 * 1 + 248, 1);
    goto loc_0024C16E;
loc_0024CB5C:
    if (((1) & (8)) != 0) goto loc_0024CAB5;
    Arg4 = (uint32_t)((1) + 1);
    Arg2 = (Arg2) + (8);
    goto loc_0024CA9D;
loc_0024CB71:
    if (result != (v_rip + 465912)) goto loc_0024CBB0;
    result = PopPepStartDevicePowerOnActivity(v_stack_pA0, Arg2, result + v_stack_pA0 * 1 + 248, Arg4);
    goto loc_0024CA0C;
loc_0024CB8A:
    v_stack_p30 = (uint32_t)((uint32_t)(v_stack_p30));
    goto loc_0024C2D7;
loc_0024CB93:
    goto loc_0024C04F;
loc_0024CB9B:
    goto loc_0024CAB5;
loc_0024CBA6:
    result = guard_dispatch_icall(v_stack_pA0, Arg2, result + v_stack_pA0 * 1 + 248, 6);
    goto loc_0024BBA5;
loc_0024CBB0:
    if (result != (v_rip + 465881)) goto loc_0024CC61;
    result = PopPepStartDevicePowerOffActivity(v_stack_pA0, Arg2, result + v_stack_pA0 * 1 + 248, 6);
    goto loc_0024CA0C;
loc_0024CBCD:
    result = ExReleaseSpinLockExclusive(v_stack_pA0 + 64, v_stack_p48, result + v_stack_pA0 * 1 + 248, 6);
    goto loc_0024C0F6;
loc_0024CBE3:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCC126F))) != 0) goto loc_0024C0CC;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_stack_pA0 + 64, v_stack_p98, result + v_stack_pA0 * 1 + 248, 6);
    goto loc_0024C0CF;
loc_0024CC06:
    result = guard_dispatch_icall(v_stack_pA0 + 64, v_stack_p98, result + v_stack_pA0 * 1 + 248, 6);
    goto loc_0024C350;
loc_0024CC10:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCC1242))) != 0) goto loc_0024C39E;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(local_r13, v_stack_p98, result + v_stack_pA0 * 1 + 248, 6);
    local_r14 = 0;
    goto loc_0024C3A5;
loc_0024CC36:
    result = ExReleaseSpinLockShared(v_stack_pA0 + 64, (uint8_t)(Arg6), result + v_stack_pA0 * 1 + 248, 6);
    goto loc_0024B983;
loc_0024CC4D:
    result = PopFxBugCheck((uint32_t)(0x666ULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_pA0)))), result + v_stack_pA0 * 1, (int32_t)(2));
loc_0024CC61:
    result = guard_dispatch_icall((uint32_t)(0x666ULL), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_pA0)))), result + v_stack_pA0 * 1, (int32_t)(2));
    goto loc_0024CA0C;
loc_0024CC6B:
    Arg1 = ((uint32_t)(0x666ULL)) * ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_pA0)))))));
    if ((*(uint32_t *)(arg1 + v_stack_pA0 * 1 + 0x128)) > 0) goto loc_0024C02C;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_pA0))))) + 1);
    goto loc_0024C4B1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0 + rax*1` | `32` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R/W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x48 + r14*8` | `64` | `R` |
| `Arg1` | `+ 0x48 + rbp*8` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R/W` |
| `Arg1` | `+ 0x7D` | `8` | `R` |
| `Arg1` | `+ 0x7D` | `8` | `W` |
| `Arg1` | `+ 0xB4` | `32` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `R` |
| `Arg1` | `+ 0xF8 + rax*8` | `64` | `R` |
| `Arg1` | `+ 0x128` | `64` | `R` |
| `Arg1` | `+ 0x1030 + rsi*1` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024B930&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
