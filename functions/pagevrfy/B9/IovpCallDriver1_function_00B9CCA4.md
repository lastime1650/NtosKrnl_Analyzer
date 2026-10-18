# IovpCallDriver1

- RVA: `0x00B9CCA4`–`0x00B9D26A` (길이 `1,478` bytes)
- VA: `0x0000000140B9CCA4`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2468`
- 디코드: `382`개 명령, `1,478/1,478` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00B9CCEF` → [VfIrpDatabaseEntryFindAndLock](../BB/VfIrpDatabaseEntryFindAndLock_function_00BB7074.md) (function, `0x00BB7074`)
- `0x00B9CD08` → [VfIrpDatabaseEntryFindAndLock](../BB/VfIrpDatabaseEntryFindAndLock_function_00BB7074.md) (function, `0x00BB7074`)
- `0x00B9CD23` → [VfPacketCreateAndLock](../BA/VfPacketCreateAndLock_function_00BAB420.md) (function, `0x00BAB420`)
- `0x00B9CD7B` → [VfPendingShouldForce](../BA/VfPendingShouldForce_function_00BA1BB8.md) (function, `0x00BA1BB8`)
- `0x00B9CDCB` → [IovpSessionDataCreate](../BA/IovpSessionDataCreate_function_00BAC6FC.md) (function, `0x00BAC6FC`)
- `0x00B9CE05` → [IovUtilGetBottomDeviceObjectWithTag](../BA/IovUtilGetBottomDeviceObjectWithTag_function_00BA2A20.md) (function, `0x00BA2A20`)
- `0x00B9CE19` → [VfIrpLogRecordEvent](../BA/VfIrpLogRecordEvent_function_00BAB674.md) (function, `0x00BAB674`)
- `0x00B9CE26` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00B9CE39` → [IovpSessionDataReference](../BA/IovpSessionDataReference_function_00BAC870.md) (function, `0x00BAC870`)
- `0x00B9CE57` → [ViErrorReport1](../../text/61/ViErrorReport1_function_00614584.md) (function, `0x00614584`)
- `0x00B9CE75` → [ViErrorReport1](../../text/61/ViErrorReport1_function_00614584.md) (function, `0x00614584`)
- `0x00B9CEB1` → [MdlInvariantPreProcessing1](../../text/61/MdlInvariantPreProcessing1_function_00613CEC.md) (function, `0x00613CEC`)
- `0x00B9CEC1` → [IovpExamineDevObjForwarding](IovpExamineDevObjForwarding_function_00B9D59C.md) (function, `0x00B9D59C`)
- `0x00B9CEF2` → [IovpExamineIrpStackForwarding](IovpExamineIrpStackForwarding_function_00B9D640.md) (function, `0x00B9D640`)
- `0x00B9CF0E` → [VfPendingStartLogging](../BA/VfPendingStartLogging_function_00BA1CC4.md) (function, `0x00BA1CC4`)
- `0x00B9CF1E` → [VfMajorIsNewRequest](../BA/VfMajorIsNewRequest_function_00BA2F24.md) (function, `0x00BA2F24`)
- `0x00B9CF55` → [IovpAdvanceStackDownwards](IovpAdvanceStackDownwards_function_00B9CB1C.md) (function, `0x00B9CB1C`)
- `0x00B9CFB4` → [IovUtilGetLowerDeviceObjectWithTag](../BA/IovUtilGetLowerDeviceObjectWithTag_function_00BA2A84.md) (function, `0x00BA2A84`)
- `0x00B9CFC6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00B9CFDB` → [VfGetPristineDispatchRoutine](VfGetPristineDispatchRoutine_function_00B9D87C.md) (function, `0x00B9D87C`)
- `0x00B9D081` → [IovUtilGetBottomDeviceObjectWithTag](../BA/IovUtilGetBottomDeviceObjectWithTag_function_00BA2A20.md) (function, `0x00BA2A20`)
- `0x00B9D092` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00B9D09F` → [KeAcquireQueuedSpinLock](../../text/27/KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x00B9D0AF` → [IovUtilIsDeviceObjectMarked](../BA/IovUtilIsDeviceObjectMarked_function_00BA2B34.md) (function, `0x00BA2B34`)
- `0x00B9D0D0` → [KeReleaseQueuedSpinLock](../../text/27/KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x00B9D0E2` → [IovUtilIsDeviceObjectMarked](../BA/IovUtilIsDeviceObjectMarked_function_00BA2B34.md) (function, `0x00BA2B34`)
- `0x00B9D111` → [VfAvlInitializeLockContext](../../text/4A/VfAvlInitializeLockContext_function_004A686C.md) (function, `0x004A686C`)
- `0x00B9D127` → [VfAvlLookupTreeNode](../../text/3E/VfAvlLookupTreeNode_function_003EF1B4.md) (function, `0x003EF1B4`)
- `0x00B9D13E` → [VfAvlCleanupLockContext](../../text/3E/VfAvlCleanupLockContext_function_003EF56C.md) (function, `0x003EF56C`)
- `0x00B9D15E` → [VfMajorVerifyNewIrp](../BA/VfMajorVerifyNewIrp_function_00BA332C.md) (function, `0x00BA332C`)
- `0x00B9D18C` → [VfMajorVerifyNewRequest](../BA/VfMajorVerifyNewRequest_function_00BA33DC.md) (function, `0x00BA33DC`)
- `0x00B9D1B1` → [VfMajorVerifyIrpStackDownward](../BA/VfMajorVerifyIrpStackDownward_function_00BA319C.md) (function, `0x00BA319C`)
- `0x00B9D20C` → [IovpSessionDataReference](../BA/IovpSessionDataReference_function_00BAC870.md) (function, `0x00BAC870`)
- `0x00B9D22D` → [ViWdBeforeCallDriver](../BA/ViWdBeforeCallDriver_function_00BACA00.md) (function, `0x00BACA00`)
- `0x00B9D235` → [VfIrpDatabaseEntryReleaseLock](../BB/VfIrpDatabaseEntryReleaseLock_function_00BB3FD4.md) (function, `0x00BB3FD4`)
- `0x00B9D246` → [VfPendingFinishLogging](../BA/VfPendingFinishLogging_function_00BA1A60.md) (function, `0x00BA1A60`)

### Direct callers
- [VfBeforeCallDriver](VfBeforeCallDriver_function_00B9DC58.md) at `0x00B9DD74`

### Static image references
- `0x00B9CE9C` → RVA `0x00F04A20` (`.data`; read)
- `0x00B9D120` → RVA `0x00FFDCC0` (`PAGEVRFD`; read)
- `0x00B9D215` → RVA `0x00F04950` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x00B9CE26` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGEVRFY` → `.text`)
  - `0x00B9CE57` → [ViErrorReport1](../../text/61/ViErrorReport1_function_00614584.md) (`PAGEVRFY` → `.text`)
  - `0x00B9CE75` → [ViErrorReport1](../../text/61/ViErrorReport1_function_00614584.md) (`PAGEVRFY` → `.text`)
  - `0x00B9CEB1` → [MdlInvariantPreProcessing1](../../text/61/MdlInvariantPreProcessing1_function_00613CEC.md) (`PAGEVRFY` → `.text`)
  - `0x00B9CFC6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGEVRFY` → `.text`)
  - `0x00B9D092` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGEVRFY` → `.text`)
  - `0x00B9D09F` → [KeAcquireQueuedSpinLock](../../text/27/KeAcquireQueuedSpinLock_function_00273D80.md) (`PAGEVRFY` → `.text`)
  - `0x00B9D0D0` → [KeReleaseQueuedSpinLock](../../text/27/KeReleaseQueuedSpinLock_function_00272540.md) (`PAGEVRFY` → `.text`)
  - `0x00B9D111` → [VfAvlInitializeLockContext](../../text/4A/VfAvlInitializeLockContext_function_004A686C.md) (`PAGEVRFY` → `.text`)
  - `0x00B9D127` → [VfAvlLookupTreeNode](../../text/3E/VfAvlLookupTreeNode_function_003EF1B4.md) (`PAGEVRFY` → `.text`)
  - `0x00B9D13E` → [VfAvlCleanupLockContext](../../text/3E/VfAvlCleanupLockContext_function_003EF56C.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B9CCA4  40 55                           push rbp
00B9CCA6  53                              push rbx
00B9CCA7  56                              push rsi
00B9CCA8  57                              push rdi
00B9CCA9  41 54                           push r12
00B9CCAB  41 55                           push r13
00B9CCAD  41 56                           push r14
00B9CCAF  41 57                           push r15
00B9CCB1  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00B9CCB6  48 81 EC 88 00 00 00            sub rsp, 0x88
00B9CCBD  4C 8B B1 A8 00 00 00            mov r14, qword ptr [rcx + 0xa8]
00B9CCC4  33 FF                           xor edi, edi
00B9CCC6  48 89 7D E7                     mov qword ptr [rbp - 0x19], rdi
00B9CCCA  4C 8B F9                        mov r15, rcx
00B9CCCD  48 89 7D D7                     mov qword ptr [rbp - 0x29], rdi
00B9CCD1  89 7D 6F                        mov dword ptr [rbp + 0x6f], edi
00B9CCD4  44 0F 20 C3                     mov rbx, cr8
00B9CCD8  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00B9CCDC  8B F7                           mov esi, edi
00B9CCDE  25 00 00 00 C0                  and eax, 0xc0000000
00B9CCE3  74 20                           je 0x140b9cd05
00B9CCE5  3D 00 00 00 40                  cmp eax, 0x40000000
00B9CCEA  75 0B                           jne 0x140b9ccf7
00B9CCEC  49 8B CE                        mov rcx, r14
00B9CCEF  E8 80 A3 01 00                  call 0x140bb7074
00B9CCF4  48 8B F0                        mov rsi, rax
00B9CCF7  4C 8B EE                        mov r13, rsi
00B9CCFA  48 85 F6                        test rsi, rsi
00B9CCFD  0F 84 52 05 00 00               je 0x140b9d255
00B9CD03  EB 3E                           jmp 0x140b9cd43
00B9CD05  49 8B CE                        mov rcx, r14
00B9CD08  E8 67 A3 01 00                  call 0x140bb7074
00B9CD0D  48 8B F0                        mov rsi, rax
00B9CD10  4C 8B E8                        mov r13, rax
00B9CD13  48 85 C0                        test rax, rax
00B9CD16  74 08                           je 0x140b9cd20
00B9CD18  41 0F BA 6E 10 1E               bts dword ptr [r14 + 0x10], 0x1e
00B9CD1E  EB 23                           jmp 0x140b9cd43
00B9CD20  49 8B CE                        mov rcx, r14
00B9CD23  E8 F8 E6 00 00                  call 0x140bab420
00B9CD28  4C 8B E8                        mov r13, rax
00B9CD2B  48 8B F0                        mov rsi, rax
00B9CD2E  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00B9CD32  4D 85 ED                        test r13, r13
00B9CD35  0F 84 12 05 00 00               je 0x140b9d24d
00B9CD3B  0F BA E8 1E                     bts eax, 0x1e
00B9CD3F  41 89 46 10                     mov dword ptr [r14 + 0x10], eax
00B9CD43  8B 8E E8 00 00 00               mov ecx, dword ptr [rsi + 0xe8]
00B9CD49  4D 8B C6                        mov r8, r14
00B9CD4C  88 5E 3D                        mov byte ptr [rsi + 0x3d], bl
00B9CD4F  8A D3                           mov dl, bl
00B9CD51  88 5E 3C                        mov byte ptr [rsi + 0x3c], bl
00B9CD54  49 8B 87 B0 00 00 00            mov rax, qword ptr [r15 + 0xb0]
00B9CD5B  4D 8B A6 B8 00 00 00            mov r12, qword ptr [r14 + 0xb8]
00B9CD62  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B9CD67  49 83 EC 48                     sub r12, 0x48
00B9CD6B  4D 8B CC                        mov r9, r12
00B9CD6E  48 89 7D EF                     mov qword ptr [rbp - 0x11], rdi
00B9CD72  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
00B9CD76  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00B9CD7B  E8 38 4E 00 00                  call 0x140ba1bb8
00B9CD80  48 8B 8E F0 00 00 00            mov rcx, qword ptr [rsi + 0xf0]
00B9CD87  8B D0                           mov edx, eax
00B9CD89  49 8B BF A0 00 00 00            mov rdi, qword ptr [r15 + 0xa0]
00B9CD90  89 45 77                        mov dword ptr [rbp + 0x77], eax
00B9CD93  48 89 4D DF                     mov qword ptr [rbp - 0x21], rcx
00B9CD97  48 89 7D F7                     mov qword ptr [rbp - 9], rdi
00B9CD9B  48 85 C9                        test rcx, rcx
00B9CD9E  74 08                           je 0x140b9cda8
00B9CDA0  33 C0                           xor eax, eax
00B9CDA2  49 83 C5 38                     add r13, 0x38
00B9CDA6  EB 36                           jmp 0x140b9cdde
00B9CDA8  4C 8D 6E 38                     lea r13, [rsi + 0x38]
00B9CDAC  41 8B 45 00                     mov eax, dword ptr [r13]
00B9CDB0  A8 01                           test al, 1
00B9CDB2  75 28                           jne 0x140b9cddc
00B9CDB4  83 C8 01                        or eax, 1
00B9CDB7  C7 45 67 01 00 00 00            mov dword ptr [rbp + 0x67], 1
00B9CDBE  44 8B C2                        mov r8d, edx
00B9CDC1  41 89 45 00                     mov dword ptr [r13], eax
00B9CDC5  48 8B D6                        mov rdx, rsi
00B9CDC8  48 8B CF                        mov rcx, rdi
00B9CDCB  E8 2C F9 00 00                  call 0x140bac6fc
00B9CDD0  48 8B C8                        mov rcx, rax
00B9CDD3  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00B9CDD7  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
00B9CDDA  EB 05                           jmp 0x140b9cde1
00B9CDDC  33 C0                           xor eax, eax
00B9CDDE  89 45 67                        mov dword ptr [rbp + 0x67], eax
00B9CDE1  49 89 0F                        mov qword ptr [r15], rcx
00B9CDE4  49 89 77 10                     mov qword ptr [r15 + 0x10], rsi
00B9CDE8  48 85 C9                        test rcx, rcx
00B9CDEB  0F 84 41 04 00 00               je 0x140b9d232
00B9CDF1  48 BB 14 00 00 00 80 F7 FF FF   movabs rbx, 0xfffff78000000014
00B9CDFB  48 8B 1B                        mov rbx, qword ptr [rbx]
00B9CDFE  85 C0                           test eax, eax
00B9CE00  74 3E                           je 0x140b9ce40
00B9CE02  48 8B CF                        mov rcx, rdi
00B9CE05  E8 16 5C 00 00                  call 0x140ba2a20
00B9CE0A  8B 8E E8 00 00 00               mov ecx, dword ptr [rsi + 0xe8]
00B9CE10  4D 8B C6                        mov r8, r14
00B9CE13  48 8B D0                        mov rdx, rax
00B9CE16  48 8B F8                        mov rdi, rax
00B9CE19  E8 56 E8 00 00                  call 0x140bab674
00B9CE1E  BA 56 72 66 49                  mov edx, 0x49667256
00B9CE23  48 8B CF                        mov rcx, rdi
00B9CE26  E8 B5 AA 75 FF                  call 0x1402f78e0
00B9CE2B  F0 FF 46 14                     lock inc dword ptr [rsi + 0x14]
00B9CE2F  48 8B 7D DF                     mov rdi, qword ptr [rbp - 0x21]
00B9CE33  FF 46 18                        inc dword ptr [rsi + 0x18]
00B9CE36  48 8B CF                        mov rcx, rdi
00B9CE39  E8 32 FA 00 00                  call 0x140bac870
00B9CE3E  EB 04                           jmp 0x140b9ce44
00B9CE40  48 8B 7D DF                     mov rdi, qword ptr [rbp - 0x21]
00B9CE44  49 83 7E 68 00                  cmp qword ptr [r14 + 0x68], 0
00B9CE49  74 16                           je 0x140b9ce61
00B9CE4B  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
00B9CE4F  4D 8B C6                        mov r8, r14
00B9CE52  B9 03 02 00 00                  mov ecx, 0x203
00B9CE57  E8 28 77 A7 FF                  call 0x140614584
00B9CE5C  49 83 66 68 00                  and qword ptr [r14 + 0x68], 0
00B9CE61  41 8B 45 00                     mov eax, dword ptr [r13]
00B9CE65  A8 10                           test al, 0x10
00B9CE67  74 11                           je 0x140b9ce7a
00B9CE69  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
00B9CE6D  4D 8B C6                        mov r8, r14
00B9CE70  B9 05 02 00 00                  mov ecx, 0x205
00B9CE75  E8 0A 77 A7 FF                  call 0x140614584
00B9CE7A  41 8A 46 42                     mov al, byte ptr [r14 + 0x42]
00B9CE7E  41 38 46 43                     cmp byte ptr [r14 + 0x43], al
00B9CE82  7F 32                           jg 0x140b9ceb6
00B9CE84  41 8A 04 24                     mov al, byte ptr [r12]
00B9CE88  2C 03                           sub al, 3
00B9CE8A  3C 01                           cmp al, 1
00B9CE8C  77 28                           ja 0x140b9ceb6
00B9CE8E  49 8B 87 A8 00 00 00            mov rax, qword ptr [r15 + 0xa8]
00B9CE95  48 83 78 08 00                  cmp qword ptr [rax + 8], 0
00B9CE9A  74 1A                           je 0x140b9ceb6
00B9CE9C  F7 05 7A 7B 36 00 00 60 00 00   test dword ptr [rip + 0x367b7a], 0x6000
00B9CEA6  74 0E                           je 0x140b9ceb6
00B9CEA8  4D 8B C4                        mov r8, r12
00B9CEAB  48 8B D6                        mov rdx, rsi
00B9CEAE  49 8B CF                        mov rcx, r15
00B9CEB1  E8 36 6E A7 FF                  call 0x140613cec
00B9CEB6  4C 8B 6D F7                     mov r13, qword ptr [rbp - 9]
00B9CEBA  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00B9CEBE  49 8B CD                        mov rcx, r13
00B9CEC1  E8 D6 06 00 00                  call 0x140b9d59c
00B9CEC6  8B 55 67                        mov edx, dword ptr [rbp + 0x67]
00B9CEC9  4D 8B CE                        mov r9, r14
00B9CECC  89 47 38                        mov dword ptr [rdi + 0x38], eax
00B9CECF  48 8B CE                        mov rcx, rsi
00B9CED2  48 8D 45 6F                     lea rax, [rbp + 0x6f]
00B9CED6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B9CEDB  48 8D 45 D7                     lea rax, [rbp - 0x29]
00B9CEDF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B9CEE4  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00B9CEE8  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00B9CEED  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B9CEF2  E8 49 07 00 00                  call 0x140b9d640
00B9CEF7  83 7D 77 00                     cmp dword ptr [rbp + 0x77], 0
00B9CEFB  74 1A                           je 0x140b9cf17
00B9CEFD  F0 FF 46 14                     lock inc dword ptr [rsi + 0x14]
00B9CF01  FF 46 18                        inc dword ptr [rsi + 0x18]
00B9CF04  49 8B CE                        mov rcx, r14
00B9CF07  4C 89 A6 D8 00 00 00            mov qword ptr [rsi + 0xd8], r12
00B9CF0E  E8 B1 4D 00 00                  call 0x140ba1cc4
00B9CF13  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00B9CF17  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
00B9CF1B  49 8B D4                        mov rdx, r12
00B9CF1E  E8 01 60 00 00                  call 0x140ba2f24
00B9CF23  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
00B9CF27  48 8D 55 E7                     lea rdx, [rbp - 0x19]
00B9CF2B  4C 8B 4D D7                     mov r9, qword ptr [rbp - 0x29]
00B9CF2F  48 83 C1 50                     add rcx, 0x50
00B9CF33  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00B9CF38  4D 8B C4                        mov r8, r12
00B9CF3B  8B 55 6F                        mov edx, dword ptr [rbp + 0x6f]
00B9CF3E  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
00B9CF46  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00B9CF4A  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
00B9CF4E  41 8A 56 43                     mov dl, byte ptr [r14 + 0x43]
00B9CF52  89 45 77                        mov dword ptr [rbp + 0x77], eax
00B9CF55  E8 C2 FB FF FF                  call 0x140b9cb1c
00B9CF5A  48 8B 7D E7                     mov rdi, qword ptr [rbp - 0x19]
00B9CF5E  48 89 5F 30                     mov qword ptr [rdi + 0x30], rbx
00B9CF62  85 C0                           test eax, eax
00B9CF64  75 4B                           jne 0x140b9cfb1
00B9CF66  41 0F BA 6F 18 1A               bts dword ptr [r15 + 0x18], 0x1a
00B9CF6C  49 8D 47 20                     lea rax, [r15 + 0x20]
00B9CF70  83 7D 77 00                     cmp dword ptr [rbp + 0x77], 0
00B9CF74  48 89 40 08                     mov qword ptr [rax + 8], rax
00B9CF78  48 89 00                        mov qword ptr [rax], rax
00B9CF7B  48 89 5F 38                     mov qword ptr [rdi + 0x38], rbx
00B9CF7F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B9CF88  48 8B 7D E7                     mov rdi, qword ptr [rbp - 0x19]
00B9CF8C  48 89 47 70                     mov qword ptr [rdi + 0x70], rax
00B9CF90  74 1F                           je 0x140b9cfb1
00B9CF92  83 7D 67 00                     cmp dword ptr [rbp + 0x67], 0
00B9CF96  41 0F 10 46 30                  movups xmm0, xmmword ptr [r14 + 0x30]
00B9CF9B  F3 0F 7F 47 50                  movdqu xmmword ptr [rdi + 0x50], xmm0
00B9CFA0  41 0F 10 4E 30                  movups xmm1, xmmword ptr [r14 + 0x30]
00B9CFA5  F3 0F 7F 4F 60                  movdqu xmmword ptr [rdi + 0x60], xmm1
00B9CFAA  74 05                           je 0x140b9cfb1
00B9CFAC  0F BA 6F 04 1B                  bts dword ptr [rdi + 4], 0x1b
00B9CFB1  49 8B CD                        mov rcx, r13
00B9CFB4  E8 CB 5A 00 00                  call 0x140ba2a84
00B9CFB9  48 85 C0                        test rax, rax
00B9CFBC  74 0F                           je 0x140b9cfcd
00B9CFBE  BA 56 72 66 49                  mov edx, 0x49667256
00B9CFC3  48 8B C8                        mov rcx, rax
00B9CFC6  E8 15 A9 75 FF                  call 0x1402f78e0
00B9CFCB  EB 05                           jmp 0x140b9cfd2
00B9CFCD  0F BA 6F 04 1C                  bts dword ptr [rdi + 4], 0x1c
00B9CFD2  41 0F B6 14 24                  movzx edx, byte ptr [r12]
00B9CFD7  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00B9CFDB  E8 9C 08 00 00                  call 0x140b9d87c
00B9CFE0  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
00B9CFE4  49 8D 57 20                     lea rdx, [r15 + 0x20]
00B9CFE8  0F BA 77 04 1E                  btr dword ptr [rdi + 4], 0x1e
00B9CFED  48 8D 47 10                     lea rax, [rdi + 0x10]
00B9CFF1  4C 8B 00                        mov r8, qword ptr [rax]
00B9CFF4  49 39 40 08                     cmp qword ptr [r8 + 8], rax
00B9CFF8  74 07                           je 0x140b9d001
00B9CFFA  B9 03 00 00 00                  mov ecx, 3
00B9CFFF  CD 29                           int 0x29
00B9D001  4C 89 02                        mov qword ptr [rdx], r8
00B9D004  48 89 42 08                     mov qword ptr [rdx + 8], rax
00B9D008  49 89 50 08                     mov qword ptr [r8 + 8], rdx
00B9D00C  48 89 10                        mov qword ptr [rax], rdx
00B9D00F  49 89 7F 08                     mov qword ptr [r15 + 8], rdi
00B9D013  4D 89 77 48                     mov qword ptr [r15 + 0x48], r14
00B9D017  49 8B 86 B8 00 00 00            mov rax, qword ptr [r14 + 0xb8]
00B9D01E  0F 10 40 B8                     movups xmm0, xmmword ptr [rax - 0x48]
00B9D022  41 0F 11 47 50                  movups xmmword ptr [r15 + 0x50], xmm0
00B9D027  0F 10 48 C8                     movups xmm1, xmmword ptr [rax - 0x38]
00B9D02B  41 0F 11 4F 60                  movups xmmword ptr [r15 + 0x60], xmm1
00B9D030  0F 10 40 D8                     movups xmm0, xmmword ptr [rax - 0x28]
00B9D034  41 0F 11 47 70                  movups xmmword ptr [r15 + 0x70], xmm0
00B9D039  0F 10 48 E8                     movups xmm1, xmmword ptr [rax - 0x18]
00B9D03D  41 0F 11 8F 80 00 00 00         movups xmmword ptr [r15 + 0x80], xmm1
00B9D045  F2 0F 10 40 F8                  movsd xmm0, qword ptr [rax - 8]
00B9D04A  F2 41 0F 11 87 90 00 00 00      movsd qword ptr [r15 + 0x90], xmm0
00B9D053  41 F6 44 24 03 01               test byte ptr [r12 + 3], 1
00B9D059  74 06                           je 0x140b9d061
00B9D05B  41 0F BA 6F 18 18               bts dword ptr [r15 + 0x18], 0x18
00B9D061  41 80 3C 24 1B                  cmp byte ptr [r12], 0x1b
00B9D066  0F 85 D7 00 00 00               jne 0x140b9d143
00B9D06C  41 80 7C 24 01 02               cmp byte ptr [r12 + 1], 2
00B9D072  0F 85 CB 00 00 00               jne 0x140b9d143
00B9D078  41 0F BA 6F 18 1D               bts dword ptr [r15 + 0x18], 0x1d
00B9D07E  49 8B CD                        mov rcx, r13
00B9D081  E8 9A 59 00 00                  call 0x140ba2a20
00B9D086  BA 56 72 66 49                  mov edx, 0x49667256
00B9D08B  49 89 47 40                     mov qword ptr [r15 + 0x40], rax
00B9D08F  48 8B C8                        mov rcx, rax
00B9D092  E8 49 A8 75 FF                  call 0x1402f78e0
00B9D097  B9 0A 00 00 00                  mov ecx, 0xa
00B9D09C  49 8B DD                        mov rbx, r13
00B9D09F  E8 DC 6C 6D FF                  call 0x140273d80
00B9D0A4  44 8A C0                        mov r8b, al
00B9D0A7  BA 01 00 00 00                  mov edx, 1
00B9D0AC  48 8B CB                        mov rcx, rbx
00B9D0AF  E8 80 5A 00 00                  call 0x140ba2b34
00B9D0B4  85 C0                           test eax, eax
00B9D0B6  75 10                           jne 0x140b9d0c8
00B9D0B8  48 8B 93 38 01 00 00            mov rdx, qword ptr [rbx + 0x138]
00B9D0BF  48 8B 5A 30                     mov rbx, qword ptr [rdx + 0x30]
00B9D0C3  48 85 DB                        test rbx, rbx
00B9D0C6  75 DF                           jne 0x140b9d0a7
00B9D0C8  41 8A D0                        mov dl, r8b
00B9D0CB  B9 0A 00 00 00                  mov ecx, 0xa
00B9D0D0  E8 6B 54 6D FF                  call 0x140272540
00B9D0D5  48 85 DB                        test rbx, rbx
00B9D0D8  74 17                           je 0x140b9d0f1
00B9D0DA  BA 03 00 00 00                  mov edx, 3
00B9D0DF  49 8B CD                        mov rcx, r13
00B9D0E2  E8 4D 5A 00 00                  call 0x140ba2b34
00B9D0E7  85 C0                           test eax, eax
00B9D0E9  75 06                           jne 0x140b9d0f1
00B9D0EB  41 0F BA 6F 18 1C               bts dword ptr [r15 + 0x18], 0x1c
00B9D0F1  33 C0                           xor eax, eax
00B9D0F3  0F 57 C0                        xorps xmm0, xmm0
00B9D0F6  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
00B9D0FA  8B 05 20 79 36 00               mov eax, dword ptr [rip + 0x367920]
00B9D100  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00B9D104  A8 10                           test al, 0x10
00B9D106  74 3B                           je 0x140b9d143
00B9D108  BA 01 00 00 00                  mov edx, 1
00B9D10D  48 8D 4D FF                     lea rcx, [rbp - 1]
00B9D111  E8 56 97 90 FF                  call 0x1404a686c
00B9D116  45 33 C9                        xor r9d, r9d
00B9D119  48 8D 55 FF                     lea rdx, [rbp - 1]
00B9D11D  4D 8B C5                        mov r8, r13
00B9D120  48 8D 0D 99 0B 46 00            lea rcx, [rip + 0x460b99]
00B9D127  E8 88 20 85 FF                  call 0x1403ef1b4
00B9D12C  48 85 C0                        test rax, rax
00B9D12F  74 09                           je 0x140b9d13a
00B9D131  F0 83 48 10 02                  lock or dword ptr [rax + 0x10], 2
00B9D136  48 8B 7D E7                     mov rdi, qword ptr [rbp - 0x19]
00B9D13A  48 8D 4D FF                     lea rcx, [rbp - 1]
00B9D13E  E8 29 24 85 FF                  call 0x1403ef56c
00B9D143  83 7D 67 00                     cmp dword ptr [rbp + 0x67], 0
00B9D147  48 8B 5D 7F                     mov rbx, qword ptr [rbp + 0x7f]
00B9D14B  74 16                           je 0x140b9d163
00B9D14D  4C 8B CF                        mov r9, rdi
00B9D150  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00B9D155  4D 8B C4                        mov r8, r12
00B9D158  49 8B D6                        mov rdx, r14
00B9D15B  48 8B CE                        mov rcx, rsi
00B9D15E  E8 C9 61 00 00                  call 0x140ba332c
00B9D163  83 7D 77 00                     cmp dword ptr [rbp + 0x77], 0
00B9D167  74 2A                           je 0x140b9d193
00B9D169  F7 46 38 00 00 08 00            test dword ptr [rsi + 0x38], 0x80000
00B9D170  75 21                           jne 0x140b9d193
00B9D172  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00B9D177  4D 8B CC                        mov r9, r12
00B9D17A  48 8B 5D D7                     mov rbx, qword ptr [rbp - 0x29]
00B9D17E  49 8B D5                        mov rdx, r13
00B9D181  4C 8B C3                        mov r8, rbx
00B9D184  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B9D189  48 8B CE                        mov rcx, rsi
00B9D18C  E8 4B 62 00 00                  call 0x140ba33dc
00B9D191  EB 04                           jmp 0x140b9d197
00B9D193  48 8B 5D D7                     mov rbx, qword ptr [rbp - 0x29]
00B9D197  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00B9D19B  4D 8B CC                        mov r9, r12
00B9D19E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00B9D1A3  4C 8B C3                        mov r8, rbx
00B9D1A6  49 8B D5                        mov rdx, r13
00B9D1A9  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B9D1AE  48 8B CE                        mov rcx, rsi
00B9D1B1  E8 E6 5F 00 00                  call 0x140ba319c
00B9D1B6  48 8B 55 DF                     mov rdx, qword ptr [rbp - 0x21]
00B9D1BA  4C 89 6A 30                     mov qword ptr [rdx + 0x30], r13
00B9D1BE  41 8A 46 43                     mov al, byte ptr [r14 + 0x43]
00B9D1C2  88 86 BA 00 00 00               mov byte ptr [rsi + 0xba], al
00B9D1C8  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00B9D1CC  41 0F 10 46 30                  movups xmm0, xmmword ptr [r14 + 0x30]
00B9D1D1  F3 0F 7F 40 60                  movdqu xmmword ptr [rax + 0x60], xmm0
00B9D1D6  41 8A 46 43                     mov al, byte ptr [r14 + 0x43]
00B9D1DA  3C 02                           cmp al, 2
00B9D1DC  7E 2B                           jle 0x140b9d209
00B9D1DE  49 8B 8E B8 00 00 00            mov rcx, qword ptr [r14 + 0xb8]
00B9D1E5  FE C8                           dec al
00B9D1E7  41 88 46 43                     mov byte ptr [r14 + 0x43], al
00B9D1EB  48 8D 41 B8                     lea rax, [rcx - 0x48]
00B9D1EF  49 89 86 B8 00 00 00            mov qword ptr [r14 + 0xb8], rax
00B9D1F6  80 89 73 FF FF FF 10            or byte ptr [rcx - 0x8d], 0x10
00B9D1FD  41 FE 46 43                     inc byte ptr [r14 + 0x43]
00B9D201  49 83 86 B8 00 00 00 48         add qword ptr [r14 + 0xb8], 0x48
00B9D209  48 8B CA                        mov rcx, rdx
00B9D20C  E8 5F F6 00 00                  call 0x140bac870
00B9D211  F0 FF 46 14                     lock inc dword ptr [rsi + 0x14]
00B9D215  8B 05 35 77 36 00               mov eax, dword ptr [rip + 0x367735]
00B9D21B  49 8B 57 30                     mov rdx, qword ptr [r15 + 0x30]
00B9D21F  85 C0                           test eax, eax
00B9D221  74 0F                           je 0x140b9d232
00B9D223  4C 8D 86 F8 00 00 00            lea r8, [rsi + 0xf8]
00B9D22A  49 8B CE                        mov rcx, r14
00B9D22D  E8 CE F7 00 00                  call 0x140baca00
00B9D232  48 8B CE                        mov rcx, rsi
00B9D235  E8 9A 6D 01 00                  call 0x140bb3fd4
00B9D23A  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
00B9D23E  48 85 C0                        test rax, rax
00B9D241  74 12                           je 0x140b9d255
00B9D243  48 8B C8                        mov rcx, rax
00B9D246  E8 15 48 00 00                  call 0x140ba1a60
00B9D24B  EB 08                           jmp 0x140b9d255
00B9D24D  0F BA E8 1F                     bts eax, 0x1f
00B9D251  41 89 46 10                     mov dword ptr [r14 + 0x10], eax
00B9D255  48 81 C4 88 00 00 00            add rsp, 0x88
00B9D25C  41 5F                           pop r15
00B9D25E  41 5E                           pop r14
00B9D260  41 5D                           pop r13
00B9D262  41 5C                           pop r12
00B9D264  5F                              pop rdi
00B9D265  5E                              pop rsi
00B9D266  5B                              pop rbx
00B9D267  5D                              pop rbp
00B9D268  C3                              ret
00B9D269  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IovpCallDriver1(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (136);
    v_rdi = 0;
    v_stack_m78 = 0;
    v_stack_m88 = 0;
    v_stack_p10 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 168) + 16))) & (0xC0000000ULL));
    if (condition_is_equal) goto loc_00B9CD05;
    v_rsi = 0;
    if (((unsigned int)(result)) == 0x40000000ULL) {
        a1 = *(unsigned __int64 *)(a1 + 168);
        result = VfIrpDatabaseEntryFindAndLock(a1, a2, a3, a4);
        v_rsi = result;
    }
    if (v_rsi == 0) goto loc_00B9D255;
    goto loc_00B9CD43;
loc_00B9CD05:
    result = VfIrpDatabaseEntryFindAndLock(*(unsigned __int64 *)(a1 + 168), a2, a3, a4);
    if (result == 0) goto loc_00B9CD20;
    goto loc_00B9CD43;
loc_00B9CD20:
    result = VfPacketCreateAndLock(*(unsigned __int64 *)(a1 + 168), a2, a3, a4);
    if (result == 0) goto loc_00B9D24D;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 168) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 168) + 16)));
loc_00B9CD43:
    *(unsigned __int8 *)(result + 61) = (unsigned __int8)(v_cr8);
    *(unsigned __int8 *)(result + 60) = (unsigned __int8)(v_cr8);
    v_stack_mA0 = *(unsigned __int64 *)(a1 + 176);
    v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 184)) - (72);
    v_stack_m70 = 0;
    v_stack_p20 = *(unsigned __int64 *)(a1 + 176);
    v_stack_mA8 = result;
    result = VfPendingShouldForce((unsigned int)(*(unsigned int *)(result + 232)), (unsigned __int8)(v_cr8), *(unsigned __int64 *)(a1 + 168), v_r12);
    v_stack_p18 = (unsigned int)(result);
    v_stack_m80 = *(unsigned __int64 *)(result + 240);
    v_stack_m68 = *(unsigned __int64 *)(a1 + 160);
    if (*(unsigned __int64 *)(result + 240) == 0) goto loc_00B9CDA8;
    result = 0;
    v_r13 = (result) + (56);
    goto loc_00B9CDDE;
loc_00B9CDA8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 56)))) & (1)) != 0) goto loc_00B9CDDC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 56))) | (1));
    v_stack_p8 = 1;
    *(unsigned int *)(result + 56) = (unsigned int)(result);
    result = IovpSessionDataCreate(*(unsigned __int64 *)(a1 + 160), result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_r12);
    v_stack_m80 = result;
    goto loc_00B9CDE1;
loc_00B9CDDC:
    result = 0;
loc_00B9CDDE:
    v_stack_p8 = 0;
loc_00B9CDE1:
    *(unsigned __int64 *)(a1) = 0;
    *(unsigned __int64 *)(a1 + 16) = 0;
    if (0 == 0) goto loc_00B9D232;
    if (0 == 0) goto loc_00B9CE40;
    result = IovUtilGetBottomDeviceObjectWithTag(*(unsigned __int64 *)(a1 + 160), result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_r12);
    result = VfIrpLogRecordEvent((unsigned int)(*(unsigned int *)(result + 232)), result, *(unsigned __int64 *)(a1 + 168), v_r12);
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x49667256ULL), *(unsigned __int64 *)(a1 + 168), v_r12);
    result = IovpSessionDataReference(v_stack_m80, (unsigned int)(0x49667256ULL), *(unsigned __int64 *)(a1 + 168), v_r12);
    goto loc_00B9CE44;
loc_00B9CE40:
loc_00B9CE44:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 104)) != 0) {
        a2 = v_stack_p20;
        a3 = *(unsigned __int64 *)(a1 + 168);
        a1 = 515;
        result = ViErrorReport1(a1, a2, a3, v_r12);
    }
    result = (unsigned int)(*(unsigned int *)(result + 56));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 56)))) & (16)) != 0) {
        a2 = v_stack_p20;
        a3 = *(unsigned __int64 *)(a1 + 168);
        a1 = 517;
        result = ViErrorReport1(a1, a2, a3, v_r12);
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 67)) > ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 66)))) goto loc_00B9CEB6;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r12)) - (3));
    if (((unsigned __int8)(result)) > 1) goto loc_00B9CEB6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 8)) == 0) goto loc_00B9CEB6;
    result = *(unsigned __int64 *)(a1 + 168);
    if (((*(unsigned int *)(v_rip + 3570554)) & (0x6000ULL)) != 0) {
        a3 = v_r12;
        a2 = result;
        a1 = a1;
        result = MdlInvariantPreProcessing1(a1, a2, a3, v_r12);
    }
    result = IovpExamineDevObjForwarding(v_stack_m68, *(unsigned __int64 *)(v_stack_m80 + 48), a3, v_r12);
    *(unsigned int *)(v_stack_m80 + 56) = (unsigned int)(result);
    v_stack_m90 = v_stack_p10;
    v_stack_m98 = v_stack_m88;
    v_stack_mA0 = v_r12;
    v_stack_mA8 = v_stack_p20;
    result = IovpExamineIrpStackForwarding(result, (unsigned int)(v_stack_p8), a3, *(unsigned __int64 *)(a1 + 168));
    if (v_stack_p18 != 0) {
        a1 = *(unsigned __int64 *)(a1 + 168);
        *(unsigned __int64 *)(result + 216) = v_r12;
        result = VfPendingStartLogging(a1, (unsigned int)(v_stack_p8), a3, *(unsigned __int64 *)(a1 + 168));
        v_stack_m70 = result;
    }
    result = VfMajorIsNewRequest(v_stack_m88, v_r12, a3, *(unsigned __int64 *)(a1 + 168));
    a1 = (v_stack_m80) + (80);
    v_stack_m90 = v_stack_m78;
    v_stack_m98 = 1;
    v_stack_mA0 = (unsigned int)(result);
    v_stack_mA8 = (unsigned int)((unsigned int)(v_stack_p10));
    v_stack_p18 = (unsigned int)(result);
    result = IovpAdvanceStackDownwards(a1, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 67), v_r12, v_stack_m88);
    *(unsigned __int64 *)(v_stack_m78 + 48) = *(unsigned __int64 *)(v_cr8);
    if ((unsigned int)(result) != 0) goto loc_00B9CFB1;
    *(unsigned __int64 *)(a1 + 32 + 8) = a1 + 32;
    *(unsigned __int64 *)(a1 + 32) = a1 + 32;
    *(unsigned __int64 *)(v_stack_m78 + 56) = *(unsigned __int64 *)(v_cr8);
    *(unsigned __int64 *)(v_stack_m78 + 112) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (v_stack_p18 == 0) goto loc_00B9CFB1;
    *(unsigned __int64 *)(v_stack_m78 + 80) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m78 + 96) = v_xmm1;
    if (v_stack_p8 != 0) {
    }
    result = IovUtilGetLowerDeviceObjectWithTag(v_stack_m68, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 67), v_r12, v_stack_m88);
    if (result == 0) goto loc_00B9CFCD;
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x49667256ULL), v_r12, v_stack_m88);
    goto loc_00B9CFD2;
loc_00B9CFCD:
loc_00B9CFD2:
    result = VfGetPristineDispatchRoutine(*(unsigned __int64 *)(v_stack_m68 + 8), *(unsigned __int8 *)(v_r12), v_r12, v_stack_m88);
    *(unsigned __int64 *)(v_stack_m78 + 40) = result;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m78 + 16) + 8)) != (v_stack_m78 + 16)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a1 + 32) = *(unsigned __int64 *)(v_stack_m78 + 16);
    *(unsigned __int64 *)(a1 + 32 + 8) = v_stack_m78 + 16;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m78 + 16) + 8) = a1 + 32;
    *(unsigned __int64 *)(v_stack_m78 + 16) = a1 + 32;
    *(unsigned __int64 *)(a1 + 8) = v_stack_m78;
    *(unsigned __int64 *)(a1 + 72) = *(unsigned __int64 *)(a1 + 168);
    *(unsigned __int64 *)(a1 + 80) = v_xmm0;
    *(unsigned __int64 *)(a1 + 96) = v_xmm1;
    *(unsigned __int64 *)(a1 + 112) = v_xmm0;
    *(unsigned __int64 *)(a1 + 128) = v_xmm1;
    *(unsigned __int64 *)(a1 + 144) = v_xmm0;
    if (((*(unsigned __int8 *)(v_r12 + 3)) & (1)) != 0) {
    }
    if ((*(unsigned __int8 *)(v_r12)) != 27) goto loc_00B9D143;
    if ((*(unsigned __int8 *)(v_r12 + 1)) != 2) goto loc_00B9D143;
    result = IovUtilGetBottomDeviceObjectWithTag(v_stack_m68, a1 + 32, *(unsigned __int64 *)(v_stack_m78 + 16), v_stack_m88);
    *(unsigned __int64 *)(a1 + 64) = result;
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x49667256ULL), *(unsigned __int64 *)(v_stack_m78 + 16), v_stack_m88);
    result = KeAcquireQueuedSpinLock(10, (unsigned int)(0x49667256ULL), *(unsigned __int64 *)(v_stack_m78 + 16), v_stack_m88);
loc_00B9D0A7:
    result = IovUtilIsDeviceObjectMarked(v_stack_m68, 1, (unsigned __int8)(result), v_stack_m88);
    if ((unsigned int)(result) != 0) goto loc_00B9D0C8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + 312) + 48) != 0) goto loc_00B9D0A7;
loc_00B9D0C8:
    result = KeReleaseQueuedSpinLock(10, (unsigned __int8)((unsigned __int8)(result)), (unsigned __int8)(result), v_stack_m88);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + 312) + 48) == 0) goto loc_00B9D0F1;
    result = IovUtilIsDeviceObjectMarked(v_stack_m68, 3, (unsigned __int8)(result), v_stack_m88);
    if ((unsigned int)(result) == 0) {
    }
    result = 0;
    v_stack_m50 = 0;
    v_stack_m60 = v_xmm0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3569952)))) & (16)) == 0) goto loc_00B9D143;
    result = VfAvlInitializeLockContext(v_stack_m60, 1, (unsigned __int8)(result), v_stack_m88);
    a4 = 0;
    result = VfAvlLookupTreeNode(v_rip + 4590489, v_stack_m60, v_stack_m68, a4);
    v_rdi = v_stack_m78;
    if (result != 0) {
        v_rdi = v_stack_m78;
    }
    result = VfAvlCleanupLockContext(v_stack_m60, v_stack_m60, v_stack_m68, a4);
loc_00B9D143:
    if (v_stack_p8 != 0) {
        a4 = v_rdi;
        v_stack_mA8 = v_stack_p20;
        a3 = v_r12;
        a2 = *(unsigned __int64 *)(a1 + 168);
        a1 = result;
        result = VfMajorVerifyNewIrp(a1, a2, a3, a4);
    }
    if (v_stack_p18 == 0) goto loc_00B9D193;
    if (((*(unsigned int *)(result + 56)) & (0x80000ULL)) != 0) goto loc_00B9D193;
    v_stack_mA0 = v_stack_p20;
    v_stack_mA8 = v_rdi;
    result = VfMajorVerifyNewRequest(result, v_stack_m68, v_stack_m88, v_r12);
    goto loc_00B9D197;
loc_00B9D193:
loc_00B9D197:
    v_stack_mA0 = v_stack_p20;
    v_stack_mA8 = v_rdi;
    result = VfMajorVerifyIrpStackDownward(result, v_stack_m68, v_stack_m88, v_r12);
    *(unsigned __int64 *)(v_stack_m80 + 48) = v_stack_m68;
    *(unsigned __int8 *)(result + 186) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 67));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8) + 96) = v_xmm0;
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 67);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 67))) >= = 2) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 184);
        result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 67)) - 1);
        *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 67) = (unsigned __int8)(result);
        result = a1 - 72;
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 168) + 184) = result;
    }
    result = IovpSessionDataReference(v_stack_m80, v_stack_m80, v_stack_m88, v_r12);
    result = (unsigned int)(*(unsigned int *)(v_rip + 3569461));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3569461))) != 0) {
        a3 = result + 248;
        a1 = *(unsigned __int64 *)(a1 + 168);
        result = ViWdBeforeCallDriver(a1, *(unsigned __int64 *)(a1 + 48), a3, v_r12);
    }
    result = VfIrpDatabaseEntryReleaseLock(result, *(unsigned __int64 *)(a1 + 48), a3, v_r12);
    if (v_stack_m70 == 0) goto loc_00B9D255;
    result = VfPendingFinishLogging(v_stack_m70, *(unsigned __int64 *)(a1 + 48), a3, v_r12);
    goto loc_00B9D255;
loc_00B9D24D:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 168) + 16) = (unsigned int)(result);
loc_00B9D255:
    v_rsp = (v_rsp) + (136);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IovpCallDriver1(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (136);
    local_rdi = 0;
    v_stack_m78 = 0;
    v_stack_m88 = 0;
    v_stack_p10 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x10))) & (0xC0000000ULL));
    if (condition_is_equal) goto loc_00B9CD05;
    local_rsi = 0;
    if (((uint32_t)(result)) == 0x40000000ULL) {
        Arg1 = *(uint64_t *)(arg1 + 0xA8);
        result = VfIrpDatabaseEntryFindAndLock(Arg1, a2, a3, a4);
        local_rsi = result;
    }
    if (local_rsi == 0) goto loc_00B9D255;
    goto loc_00B9CD43;
loc_00B9CD05:
    result = VfIrpDatabaseEntryFindAndLock(*(uint64_t *)(arg1 + 0xA8), a2, a3, a4);
    if (result == 0) goto loc_00B9CD20;
    goto loc_00B9CD43;
loc_00B9CD20:
    result = VfPacketCreateAndLock(*(uint64_t *)(arg1 + 0xA8), a2, a3, a4);
    if (result == 0) goto loc_00B9D24D;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x10)));
loc_00B9CD43:
    *(uint8_t *)(result + 0x3D) = (uint8_t)(v_cr8);
    *(uint8_t *)(result + 0x3C) = (uint8_t)(v_cr8);
    v_stack_mA0 = *(uint64_t *)(arg1 + 0xB0);
    local_r12 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0xB8)) - (72);
    v_stack_m70 = 0;
    v_stack_p20 = *(uint64_t *)(arg1 + 0xB0);
    v_stack_mA8 = result;
    result = VfPendingShouldForce((uint32_t)(*(uint32_t *)(result + 0xE8)), (uint8_t)(v_cr8), *(uint64_t *)(arg1 + 0xA8), local_r12);
    v_stack_p18 = (uint32_t)(result);
    v_stack_m80 = *(uint64_t *)(result + 0xF0);
    v_stack_m68 = *(uint64_t *)(arg1 + 0xA0);
    if (*(uint64_t *)(result + 0xF0) == 0) goto loc_00B9CDA8;
    result = 0;
    local_r13 = (result) + (56);
    goto loc_00B9CDDE;
loc_00B9CDA8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x38)))) & (1)) != 0) goto loc_00B9CDDC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x38))) | (1));
    v_stack_p8 = 1;
    *(uint32_t *)(result + 0x38) = (uint32_t)(result);
    result = IovpSessionDataCreate(*(uint64_t *)(arg1 + 0xA0), result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_r12);
    v_stack_m80 = result;
    goto loc_00B9CDE1;
loc_00B9CDDC:
    result = 0;
loc_00B9CDDE:
    v_stack_p8 = 0;
loc_00B9CDE1:
    *(uint64_t *)(arg1) = 0;
    *(uint64_t *)(arg1 + 0x10) = 0;
    if (0 == 0) goto loc_00B9D232;
    if (0 == 0) goto loc_00B9CE40;
    result = IovUtilGetBottomDeviceObjectWithTag(*(uint64_t *)(arg1 + 0xA0), result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_r12);
    result = VfIrpLogRecordEvent((uint32_t)(*(uint32_t *)(result + 0xE8)), result, *(uint64_t *)(arg1 + 0xA8), local_r12);
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x49667256ULL), *(uint64_t *)(arg1 + 0xA8), local_r12);
    result = IovpSessionDataReference(v_stack_m80, (uint32_t)(0x49667256ULL), *(uint64_t *)(arg1 + 0xA8), local_r12);
    goto loc_00B9CE44;
loc_00B9CE40:
loc_00B9CE44:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x68)) != 0) {
        a2 = v_stack_p20;
        a3 = *(uint64_t *)(arg1 + 0xA8);
        Arg1 = 515;
        result = ViErrorReport1(Arg1, a2, a3, local_r12);
    }
    result = (uint32_t)(*(uint32_t *)(result + 0x38));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x38)))) & (16)) != 0) {
        a2 = v_stack_p20;
        a3 = *(uint64_t *)(arg1 + 0xA8);
        Arg1 = 517;
        result = ViErrorReport1(Arg1, a2, a3, local_r12);
    }
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x43)) > ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x42)))) goto loc_00B9CEB6;
    result = (uint8_t)((*(uint8_t *)(local_r12)) - (3));
    if (((uint8_t)(result)) > 1) goto loc_00B9CEB6;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x8)) == 0) goto loc_00B9CEB6;
    result = *(uint64_t *)(arg1 + 0xA8);
    if (((*(uint32_t *)(v_rip + 0x367B7A)) & (0x6000ULL)) != 0) {
        a3 = local_r12;
        a2 = result;
        Arg1 = Arg1;
        result = MdlInvariantPreProcessing1(Arg1, a2, a3, local_r12);
    }
    result = IovpExamineDevObjForwarding(v_stack_m68, *(uint64_t *)(v_stack_m80 + 0x30), a3, local_r12);
    *(uint32_t *)(v_stack_m80 + 0x38) = (uint32_t)(result);
    v_stack_m90 = v_stack_p10;
    v_stack_m98 = v_stack_m88;
    v_stack_mA0 = local_r12;
    v_stack_mA8 = v_stack_p20;
    result = IovpExamineIrpStackForwarding(result, (uint32_t)(v_stack_p8), a3, *(uint64_t *)(arg1 + 0xA8));
    if (v_stack_p18 != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0xA8);
        *(uint64_t *)(result + 0xD8) = local_r12;
        result = VfPendingStartLogging(Arg1, (uint32_t)(v_stack_p8), a3, *(uint64_t *)(arg1 + 0xA8));
        v_stack_m70 = result;
    }
    result = VfMajorIsNewRequest(v_stack_m88, local_r12, a3, *(uint64_t *)(arg1 + 0xA8));
    Arg1 = (v_stack_m80) + (80);
    v_stack_m90 = v_stack_m78;
    v_stack_m98 = 1;
    v_stack_mA0 = (uint32_t)(result);
    v_stack_mA8 = (uint32_t)((uint32_t)(v_stack_p10));
    v_stack_p18 = (uint32_t)(result);
    result = IovpAdvanceStackDownwards(Arg1, *(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x43), local_r12, v_stack_m88);
    *(uint64_t *)(v_stack_m78 + 0x30) = *(uint64_t *)(v_cr8);
    if ((uint32_t)(result) != 0) goto loc_00B9CFB1;
    *(void **)(arg1 + 0x20 + 0x8) = Arg1 + 32;
    *(void **)(arg1 + 0x20) = Arg1 + 32;
    *(uint64_t *)(v_stack_m78 + 0x38) = *(uint64_t *)(v_cr8);
    *(uint64_t *)(v_stack_m78 + 0x70) = *(uint64_t *)(gs_base + (0 + 0x188));
    if (v_stack_p18 == 0) goto loc_00B9CFB1;
    *(uint64_t *)(v_stack_m78 + 0x50) = v_xmm0;
    *(uint64_t *)(v_stack_m78 + 0x60) = v_xmm1;
    if (v_stack_p8 != 0) {
    }
    result = IovUtilGetLowerDeviceObjectWithTag(v_stack_m68, *(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x43), local_r12, v_stack_m88);
    if (result == 0) goto loc_00B9CFCD;
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x49667256ULL), local_r12, v_stack_m88);
    goto loc_00B9CFD2;
loc_00B9CFCD:
loc_00B9CFD2:
    result = VfGetPristineDispatchRoutine(*(uint64_t *)(v_stack_m68 + 0x8), *(uint8_t *)(local_r12), local_r12, v_stack_m88);
    *(uint64_t *)(v_stack_m78 + 0x28) = result;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m78 + 0x10) + 0x8)) != (v_stack_m78 + 16)) {
        Arg1 = 3;
    }
    *(uint64_t *)(arg1 + 0x20) = *(uint64_t *)(v_stack_m78 + 0x10);
    *(uint64_t *)(arg1 + 0x20 + 0x8) = v_stack_m78 + 16;
    *(void **)(*(uint64_t *)(v_stack_m78 + 0x10) + 0x8) = Arg1 + 32;
    *(void **)(v_stack_m78 + 0x10) = Arg1 + 32;
    *(uint64_t *)(arg1 + 0x8) = v_stack_m78;
    *(uint64_t *)(arg1 + 0x48) = *(uint64_t *)(arg1 + 0xA8);
    *(uint64_t *)(arg1 + 0x50) = v_xmm0;
    *(uint64_t *)(arg1 + 0x60) = v_xmm1;
    *(uint64_t *)(arg1 + 0x70) = v_xmm0;
    *(uint64_t *)(arg1 + 0x80) = v_xmm1;
    *(uint64_t *)(arg1 + 0x90) = v_xmm0;
    if (((*(uint8_t *)(local_r12 + 0x3)) & (1)) != 0) {
    }
    if ((*(uint8_t *)(local_r12)) != 27) goto loc_00B9D143;
    if ((*(uint8_t *)(local_r12 + 0x1)) != 2) goto loc_00B9D143;
    result = IovUtilGetBottomDeviceObjectWithTag(v_stack_m68, Arg1 + 32, *(uint64_t *)(v_stack_m78 + 0x10), v_stack_m88);
    *(uint64_t *)(arg1 + 0x40) = result;
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x49667256ULL), *(uint64_t *)(v_stack_m78 + 0x10), v_stack_m88);
    result = KeAcquireQueuedSpinLock(10, (uint32_t)(0x49667256ULL), *(uint64_t *)(v_stack_m78 + 0x10), v_stack_m88);
loc_00B9D0A7:
    result = IovUtilIsDeviceObjectMarked(v_stack_m68, 1, (uint8_t)(result), v_stack_m88);
    if ((uint32_t)(result) != 0) goto loc_00B9D0C8;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m68 + 0x138) + 0x30) != 0) goto loc_00B9D0A7;
loc_00B9D0C8:
    result = KeReleaseQueuedSpinLock(10, (uint8_t)((uint8_t)(result)), (uint8_t)(result), v_stack_m88);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m68 + 0x138) + 0x30) == 0) goto loc_00B9D0F1;
    result = IovUtilIsDeviceObjectMarked(v_stack_m68, 3, (uint8_t)(result), v_stack_m88);
    if ((uint32_t)(result) == 0) {
    }
    result = 0;
    v_stack_m50 = 0;
    v_stack_m60 = v_xmm0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x367920)))) & (16)) == 0) goto loc_00B9D143;
    result = VfAvlInitializeLockContext(v_stack_m60, 1, (uint8_t)(result), v_stack_m88);
    a4 = 0;
    result = VfAvlLookupTreeNode(v_rip + 4590489, v_stack_m60, v_stack_m68, a4);
    local_rdi = v_stack_m78;
    if (result != 0) {
        local_rdi = v_stack_m78;
    }
    result = VfAvlCleanupLockContext(v_stack_m60, v_stack_m60, v_stack_m68, a4);
loc_00B9D143:
    if (v_stack_p8 != 0) {
        a4 = local_rdi;
        v_stack_mA8 = v_stack_p20;
        a3 = local_r12;
        a2 = *(uint64_t *)(arg1 + 0xA8);
        Arg1 = result;
        result = VfMajorVerifyNewIrp(Arg1, a2, a3, a4);
    }
    if (v_stack_p18 == 0) goto loc_00B9D193;
    if (((*(uint32_t *)(result + 0x38)) & (0x80000ULL)) != 0) goto loc_00B9D193;
    v_stack_mA0 = v_stack_p20;
    v_stack_mA8 = local_rdi;
    result = VfMajorVerifyNewRequest(result, v_stack_m68, v_stack_m88, local_r12);
    goto loc_00B9D197;
loc_00B9D193:
loc_00B9D197:
    v_stack_mA0 = v_stack_p20;
    v_stack_mA8 = local_rdi;
    result = VfMajorVerifyIrpStackDownward(result, v_stack_m68, v_stack_m88, local_r12);
    *(uint64_t *)(v_stack_m80 + 0x30) = v_stack_m68;
    *(uint8_t *)(result + 0xBA) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x43));
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x60) = v_xmm0;
    result = *(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x43);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x43))) >= = 2) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0xB8);
        result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x43)) - 1);
        *(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x43) = (uint8_t)(result);
        result = Arg1 - 72;
        *(uint64_t *)(*(uint64_t *)(arg1 + 0xA8) + 0xB8) = result;
    }
    result = IovpSessionDataReference(v_stack_m80, v_stack_m80, v_stack_m88, local_r12);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x367735));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x367735))) != 0) {
        a3 = result + 248;
        Arg1 = *(uint64_t *)(arg1 + 0xA8);
        result = ViWdBeforeCallDriver(Arg1, *(uint64_t *)(arg1 + 0x30), a3, local_r12);
    }
    result = VfIrpDatabaseEntryReleaseLock(result, *(uint64_t *)(arg1 + 0x30), a3, local_r12);
    if (v_stack_m70 == 0) goto loc_00B9D255;
    result = VfPendingFinishLogging(v_stack_m70, *(uint64_t *)(arg1 + 0x30), a3, local_r12);
    goto loc_00B9D255;
loc_00B9D24D:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x10) = (uint32_t)(result);
loc_00B9D255:
    local_rsp = (local_rsp) + (136);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `32` | `R/W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x48` | `64` | `W` |
| `Arg1` | `+ 0x50` | `128` | `R` |
| `Arg1` | `+ 0x60` | `128` | `R` |
| `Arg1` | `+ 0x70` | `128` | `R` |
| `Arg1` | `+ 0x80` | `128` | `R` |
| `Arg1` | `+ 0x90` | `64` | `W` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B9CCA4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
