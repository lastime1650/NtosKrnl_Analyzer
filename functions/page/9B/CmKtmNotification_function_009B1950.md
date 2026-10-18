# CmKtmNotification

- RVA: `0x009B1950`–`0x009B1E6F` (길이 `1,311` bytes)
- VA: `0x00000001409B1950`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009E2F8`
- 디코드: `318`개 명령, `1,311/1,311` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **39**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x009B19CA` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x009B19D2` → [CmpIsCmRm](CmpIsCmRm_function_009B1E78.md) (function, `0x009B1E78`)
- `0x009B1A08` → [TmReferenceEnlistmentKey](../../text/4F/TmReferenceEnlistmentKey_function_004FE300.md) (function, `0x004FE300`)
- `0x009B1A17` → [LOCK_TRANSACTION_LIST](../87/LOCK_TRANSACTION_LIST_function_00874AD4.md) (function, `0x00874AD4`)
- `0x009B1A32` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x009B1A37` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x009B1A73` → [LOCK_HIVE_LOAD](LOCK_HIVE_LOAD_function_009B2300.md) (function, `0x009B2300`)
- `0x009B1A7E` → [CmpIsCmRm](CmpIsCmRm_function_009B1E78.md) (function, `0x009B1E78`)
- `0x009B1AA4` → [CmpTransMgrPrepare](CmpTransMgrPrepare_function_009B175C.md) (function, `0x009B175C`)
- `0x009B1ADC` → [CmLogTmRmAction](CmLogTmRmAction_function_009B1598.md) (function, `0x009B1598`)
- `0x009B1B18` → [TmDereferenceEnlistmentKey](../../text/4F/TmDereferenceEnlistmentKey_function_004FE0C0.md) (function, `0x004FE0C0`)
- `0x009B1B22` → [UNLOCK_HIVE_LOAD](UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x009B1B78` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x009B1B86` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009B1BE3` → [CmpTransMgrRollback](CmpTransMgrRollback_function_009B1400.md) (function, `0x009B1400`)
- `0x009B1BF8` → [CmpCleanupTransactionState](../84/CmpCleanupTransactionState_function_008428E0.md) (function, `0x008428E0`)
- `0x009B1C22` → [TmDereferenceEnlistmentKey](../../text/4F/TmDereferenceEnlistmentKey_function_004FE0C0.md) (function, `0x004FE0C0`)
- `0x009B1C5B` → [TmRollbackComplete](../../text/4F/TmRollbackComplete_function_004FE360.md) (function, `0x004FE360`)
- `0x009B1C78` → [CmpTransMgrCommit](../9A/CmpTransMgrCommit_function_009AE8AC.md) (function, `0x009AE8AC`)
- `0x009B1CAA` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x009B1CAF` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x009B1CB9` → [TmRollbackComplete](../../text/4F/TmRollbackComplete_function_004FE360.md) (function, `0x004FE360`)
- `0x009B1CCE` → [CmpAccountForLogReservation](../84/CmpAccountForLogReservation_function_00842850.md) (function, `0x00842850`)
- `0x009B1CFD` → [CmpRecoverEnlistment](../7F/CmpRecoverEnlistment_function_007F0014.md) (function, `0x007F0014`)
- `0x009B1D11` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x009B1D16` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x009B1D20` → [TmPrepareComplete](../../text/4F/TmPrepareComplete_function_004FE200.md) (function, `0x004FE200`)
- `0x009B1D39` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x009B1D3E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x009B1D48` → [TmCommitComplete](../../text/4F/TmCommitComplete_function_004FE020.md) (function, `0x004FE020`)
- `0x009B1D5D` → [CmpQueryNameString](CmpQueryNameString_function_009BA2AC.md) (function, `0x009BA2AC`)
- `0x009B1D73` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (function, `0x0039FC50`)
- `0x009B1D8A` → [UNLOCK_HIVE_LOAD](UNLOCK_HIVE_LOAD_function_009B2EBC.md) (function, `0x009B2EBC`)
- `0x009B1D98` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x009B1DDC` → [TmCommitComplete](../../text/4F/TmCommitComplete_function_004FE020.md) (function, `0x004FE020`)
- `0x009B1DF5` → [TmReadOnlyEnlistment](../../text/4F/TmReadOnlyEnlistment_function_004FE280.md) (function, `0x004FE280`)
- `0x009B1E02` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x009B1E57` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009B1E65` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009B196C` → RVA `0x00E0A740` (`.data`; read)
- `0x009B1A2B` → RVA `0x00EF5820` (`.data`; read)
- `0x009B1A3C` → RVA `0x00EEFC78` (`.data`; read)
- `0x009B1A43` → RVA `0x00E09AE0` (`.data`; read)
- `0x009B1A50` → RVA `0x00FD81D0` (`PAGEDATA`; read)
- `0x009B1A66` → RVA `0x00FD8220` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x009B19CA` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x009B1A08` → [TmReferenceEnlistmentKey](../../text/4F/TmReferenceEnlistmentKey_function_004FE300.md) (`PAGE` → `.text`)
  - `0x009B1A32` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x009B1A37` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x009B1B18` → [TmDereferenceEnlistmentKey](../../text/4F/TmDereferenceEnlistmentKey_function_004FE0C0.md) (`PAGE` → `.text`)
  - `0x009B1B78` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x009B1B86` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009B1C22` → [TmDereferenceEnlistmentKey](../../text/4F/TmDereferenceEnlistmentKey_function_004FE0C0.md) (`PAGE` → `.text`)
  - `0x009B1C5B` → [TmRollbackComplete](../../text/4F/TmRollbackComplete_function_004FE360.md) (`PAGE` → `.text`)
  - `0x009B1CAA` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x009B1CAF` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x009B1CB9` → [TmRollbackComplete](../../text/4F/TmRollbackComplete_function_004FE360.md) (`PAGE` → `.text`)
  - `0x009B1D11` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x009B1D16` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x009B1D20` → [TmPrepareComplete](../../text/4F/TmPrepareComplete_function_004FE200.md) (`PAGE` → `.text`)
  - `0x009B1D39` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x009B1D3E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x009B1D48` → [TmCommitComplete](../../text/4F/TmCommitComplete_function_004FE020.md) (`PAGE` → `.text`)
  - `0x009B1D73` → [EtwGetKernelTraceTimestamp](../../text/39/EtwGetKernelTraceTimestamp_function_0039FC50.md) (`PAGE` → `.text`)
  - `0x009B1DDC` → [TmCommitComplete](../../text/4F/TmCommitComplete_function_004FE020.md) (`PAGE` → `.text`)
  - `0x009B1DF5` → [TmReadOnlyEnlistment](../../text/4F/TmReadOnlyEnlistment_function_004FE280.md) (`PAGE` → `.text`)
  - `0x009B1E02` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x009B1E57` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x009B1DA9` → [sub_00B2DBCA](../B2/Unknown_function_00B2DBCA.md) (`tail-transfer`)
  - `0x009B1DEF` → [sub_00B2DBCA + 0x14](../B2/Unknown_function_00B2DBCA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009B1950  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
009B1955  55                              push rbp
009B1956  56                              push rsi
009B1957  57                              push rdi
009B1958  41 54                           push r12
009B195A  41 55                           push r13
009B195C  41 56                           push r14
009B195E  41 57                           push r15
009B1960  48 8D 6C 24 F1                  lea rbp, [rsp - 0xf]
009B1965  48 81 EC D0 00 00 00            sub rsp, 0xd0
009B196C  48 8B 05 CD 8D 45 00            mov rax, qword ptr [rip + 0x458dcd]
009B1973  48 33 C4                        xor rax, rsp
009B1976  48 89 45 FF                     mov qword ptr [rbp - 1], rax
009B197A  48 8B 5D 7F                     mov rbx, qword ptr [rbp + 0x7f]
009B197E  45 33 FF                        xor r15d, r15d
009B1981  0F 57 C0                        xorps xmm0, xmm0
009B1984  4C 89 7D 87                     mov qword ptr [rbp - 0x79], r15
009B1988  33 C0                           xor eax, eax
009B198A  4C 89 7D A7                     mov qword ptr [rbp - 0x59], r15
009B198E  0F 57 C9                        xorps xmm1, xmm1
009B1991  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
009B1995  48 8B F1                        mov rsi, rcx
009B1998  44 88 7D 81                     mov byte ptr [rbp - 0x7f], r15b
009B199C  48 8D 4D B7                     lea rcx, [rbp - 0x49]
009B19A0  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
009B19A5  0F 11 45 B7                     movups xmmword ptr [rbp - 0x49], xmm0
009B19A9  44 89 7D 8F                     mov dword ptr [rbp - 0x71], r15d
009B19AD  45 8A EF                        mov r13b, r15b
009B19B0  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
009B19B4  41 8B F9                        mov edi, r9d
009B19B7  4C 8B F2                        mov r14, rdx
009B19BA  0F 11 4D 97                     movups xmmword ptr [rbp - 0x69], xmm1
009B19BE  C6 45 80 01                     mov byte ptr [rbp - 0x80], 1
009B19C2  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
009B19C6  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
009B19CA  E8 A1 A4 A4 FF                  call 0x1403fbe70
009B19CF  49 8B CE                        mov rcx, r14
009B19D2  E8 A1 04 00 00                  call 0x1409b1e78
009B19D7  84 C0                           test al, al
009B19D9  0F 84 0E 03 00 00               je 0x1409b1ced
009B19DF  41 8B 46 68                     mov eax, dword ptr [r14 + 0x68]
009B19E3  A8 08                           test al, 8
009B19E5  0F 85 D5 02 00 00               jne 0x1409b1cc0
009B19EB  81 FF 00 01 00 00               cmp edi, 0x100
009B19F1  0F 84 00 03 00 00               je 0x1409b1cf7
009B19F7  40 F6 C7 0E                     test dil, 0xe
009B19FB  0F 84 BF 02 00 00               je 0x1409b1cc0
009B1A01  48 8D 55 87                     lea rdx, [rbp - 0x79]
009B1A05  48 8B CE                        mov rcx, rsi
009B1A08  E8 F3 C8 B4 FF                  call 0x1404fe300
009B1A0D  8B D8                           mov ebx, eax
009B1A0F  85 C0                           test eax, eax
009B1A11  0F 85 5D 01 00 00               jne 0x1409b1b74
009B1A17  E8 B8 30 EC FF                  call 0x140874ad4
009B1A1C  48 8B 55 87                     mov rdx, qword ptr [rbp - 0x79]
009B1A20  8B 42 30                        mov eax, dword ptr [rdx + 0x30]
009B1A23  A8 08                           test al, 8
009B1A25  0F 85 5B 02 00 00               jne 0x1409b1c86
009B1A2B  48 8D 0D EE 3D 54 00            lea rcx, [rip + 0x543dee]
009B1A32  E8 69 E9 89 FF                  call 0x1402503a0
009B1A37  E8 74 BE 8A FF                  call 0x14025d8b0
009B1A3C  4C 39 35 35 E2 53 00            cmp qword ptr [rip + 0x53e235], r14
009B1A43  48 8B 0D 96 80 45 00            mov rcx, qword ptr [rip + 0x458096]
009B1A4A  0F 85 5F 01 00 00               jne 0x1409b1baf
009B1A50  4C 39 3D 79 67 62 00            cmp qword ptr [rip + 0x626779], r15
009B1A57  0F 85 F5 02 00 00               jne 0x1409b1d52
009B1A5D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009B1A66  48 39 05 B3 67 62 00            cmp qword ptr [rip + 0x6267b3], rax
009B1A6D  0F 84 34 01 00 00               je 0x1409b1ba7
009B1A73  E8 88 08 00 00                  call 0x1409b2300
009B1A78  41 B4 01                        mov r12b, 1
009B1A7B  49 8B CE                        mov rcx, r14
009B1A7E  E8 F5 03 00 00                  call 0x1409b1e78
009B1A83  84 C0                           test al, al
009B1A85  0F 84 89 01 00 00               je 0x1409b1c14
009B1A8B  83 FF 02                        cmp edi, 2
009B1A8E  0F 85 D3 01 00 00               jne 0x1409b1c67
009B1A94  48 8B 55 87                     mov rdx, qword ptr [rbp - 0x79]
009B1A98  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
009B1A9D  4C 8D 45 8F                     lea r8, [rbp - 0x71]
009B1AA1  49 8B CE                        mov rcx, r14
009B1AA4  E8 B3 FC FF FF                  call 0x1409b175c
009B1AA9  44 8D 47 02                     lea r8d, [rdi + 2]
009B1AAD  89 45 93                        mov dword ptr [rbp - 0x6d], eax
009B1AB0  8B D8                           mov ebx, eax
009B1AB2  85 C0                           test eax, eax
009B1AB4  0F 88 48 01 00 00               js 0x1409b1c02
009B1ABA  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
009B1ABE  89 5D 93                        mov dword ptr [rbp - 0x6d], ebx
009B1AC1  48 8D 41 10                     lea rax, [rcx + 0x10]
009B1AC5  48 39 00                        cmp qword ptr [rax], rax
009B1AC8  0F 84 16 02 00 00               je 0x1409b1ce4
009B1ACE  85 DB                           test ebx, ebx
009B1AD0  0F 88 0E 02 00 00               js 0x1409b1ce4
009B1AD6  48 8B D1                        mov rdx, rcx
009B1AD9  49 8B CE                        mov rcx, r14
009B1ADC  E8 B7 FA FF FF                  call 0x1409b1598
009B1AE1  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
009B1AE5  83 FF 02                        cmp edi, 2
009B1AE8  41 8B DF                        mov ebx, r15d
009B1AEB  0F 44 D8                        cmove ebx, eax
009B1AEE  C6 45 81 01                     mov byte ptr [rbp - 0x7f], 1
009B1AF2  83 FF 04                        cmp edi, 4
009B1AF5  0F 84 BD 00 00 00               je 0x1409b1bb8
009B1AFB  83 FF 08                        cmp edi, 8
009B1AFE  0F 84 B4 00 00 00               je 0x1409b1bb8
009B1B04  44 8A 7C 24 40                  mov r15b, byte ptr [rsp + 0x40]
009B1B09  41 80 FF 01                     cmp r15b, 1
009B1B0D  0F 84 AA 00 00 00               je 0x1409b1bbd
009B1B13  33 D2                           xor edx, edx
009B1B15  48 8B CE                        mov rcx, rsi
009B1B18  E8 A3 C5 B4 FF                  call 0x1404fe0c0
009B1B1D  45 84 E4                        test r12b, r12b
009B1B20  74 05                           je 0x1409b1b27
009B1B22  E8 95 13 00 00                  call 0x1409b2ebc
009B1B27  80 7D 81 01                     cmp byte ptr [rbp - 0x7f], 1
009B1B2B  0F 84 0A 01 00 00               je 0x1409b1c3b
009B1B31  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
009B1B35  48 85 C0                        test rax, rax
009B1B38  0F 85 C1 02 00 00               jne 0x1409b1dff
009B1B3E  83 FF 02                        cmp edi, 2
009B1B41  0F 84 D5 02 00 00               je 0x1409b1e1c
009B1B47  83 FF 04                        cmp edi, 4
009B1B4A  0F 84 C4 02 00 00               je 0x1409b1e14
009B1B50  83 FF 08                        cmp edi, 8
009B1B53  0F 84 B3 02 00 00               je 0x1409b1e0c
009B1B59  48 8B 05 70 66 62 00            mov rax, qword ptr [rip + 0x626670]
009B1B60  48 85 C0                        test rax, rax
009B1B63  0F 85 BB 02 00 00               jne 0x1409b1e24
009B1B69  48 83 7D 9F 00                  cmp qword ptr [rbp - 0x61], 0
009B1B6E  0F 85 ED 02 00 00               jne 0x1409b1e61
009B1B74  48 8D 4D B7                     lea rcx, [rbp - 0x49]
009B1B78  E8 D3 E1 A6 FF                  call 0x14041fd50
009B1B7D  8B C3                           mov eax, ebx
009B1B7F  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
009B1B83  48 33 CC                        xor rcx, rsp
009B1B86  E8 B5 AA CF FF                  call 0x1406ac640
009B1B8B  48 8B 9C 24 20 01 00 00         mov rbx, qword ptr [rsp + 0x120]
009B1B93  48 81 C4 D0 00 00 00            add rsp, 0xd0
009B1B9A  41 5F                           pop r15
009B1B9C  41 5E                           pop r14
009B1B9E  41 5D                           pop r13
009B1BA0  41 5C                           pop r12
009B1BA2  5F                              pop rdi
009B1BA3  5E                              pop rsi
009B1BA4  5D                              pop rbp
009B1BA5  C3                              ret
009B1BA6  CC                              int3
009B1BA7  45 8A E7                        mov r12b, r15b
009B1BAA  E9 CC FE FF FF                  jmp 0x1409b1a7b
009B1BAF  49 8B 4E 50                     mov rcx, qword ptr [r14 + 0x50]
009B1BB3  E9 98 FE FF FF                  jmp 0x1409b1a50
009B1BB8  44 8A 7C 24 40                  mov r15b, byte ptr [rsp + 0x40]
009B1BBD  48 83 79 48 00                  cmp qword ptr [rcx + 0x48], 0
009B1BC2  74 08                           je 0x1409b1bcc
009B1BC4  48 8B 41 50                     mov rax, qword ptr [rcx + 0x50]
009B1BC8  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
009B1BCC  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
009B1BCF  A8 20                           test al, 0x20
009B1BD1  0F 85 F1 00 00 00               jne 0x1409b1cc8
009B1BD7  85 DB                           test ebx, ebx
009B1BD9  0F 88 EA 01 00 00               js 0x1409b1dc9
009B1BDF  48 8D 55 8F                     lea rdx, [rbp - 0x71]
009B1BE3  E8 18 F8 FF FF                  call 0x1409b1400
009B1BE8  44 8A 4D 80                     mov r9b, byte ptr [rbp - 0x80]
009B1BEC  44 8B C7                        mov r8d, edi
009B1BEF  48 8B 55 87                     mov rdx, qword ptr [rbp - 0x79]
009B1BF3  49 8B CE                        mov rcx, r14
009B1BF6  8B D8                           mov ebx, eax
009B1BF8  E8 E3 0C E9 FF                  call 0x1408428e0
009B1BFD  E9 11 FF FF FF                  jmp 0x1409b1b13
009B1C02  83 FF 04                        cmp edi, 4
009B1C05  0F 84 AF FE FF FF               je 0x1409b1aba
009B1C0B  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
009B1C0F  E9 E7 FE FF FF                  jmp 0x1409b1afb
009B1C14  45 84 E4                        test r12b, r12b
009B1C17  0F 85 6D 01 00 00               jne 0x1409b1d8a
009B1C1D  33 D2                           xor edx, edx
009B1C1F  48 8B CE                        mov rcx, rsi
009B1C22  E8 99 C4 B4 FF                  call 0x1404fe0c0
009B1C27  4C 39 7D 9F                     cmp qword ptr [rbp - 0x61], r15
009B1C2B  0F 85 63 01 00 00               jne 0x1409b1d94
009B1C31  B8 0D 00 00 C0                  mov eax, 0xc000000d
009B1C36  E9 44 FF FF FF                  jmp 0x1409b1b7f
009B1C3B  83 FF 02                        cmp edi, 2
009B1C3E  0F 84 A2 01 00 00               je 0x1409b1de6
009B1C44  83 FF 04                        cmp edi, 4
009B1C47  0F 84 8A 01 00 00               je 0x1409b1dd7
009B1C4D  83 FF 08                        cmp edi, 8
009B1C50  0F 85 DB FE FF FF               jne 0x1409b1b31
009B1C56  33 D2                           xor edx, edx
009B1C58  48 8B CE                        mov rcx, rsi
009B1C5B  E8 00 C7 B4 FF                  call 0x1404fe360
009B1C60  8B D8                           mov ebx, eax
009B1C62  E9 CA FE FF FF                  jmp 0x1409b1b31
009B1C67  83 FF 04                        cmp edi, 4
009B1C6A  0F 85 32 01 00 00               jne 0x1409b1da2
009B1C70  48 8B 55 87                     mov rdx, qword ptr [rbp - 0x79]
009B1C74  4C 8D 45 8F                     lea r8, [rbp - 0x71]
009B1C78  E8 2F CC FF FF                  call 0x1409ae8ac
009B1C7D  44 8D 47 0C                     lea r8d, [rdi + 0xc]
009B1C81  E9 27 FE FF FF                  jmp 0x1409b1aad
009B1C86  83 FF 02                        cmp edi, 2
009B1C89  74 79                           je 0x1409b1d04
009B1C8B  83 FF 04                        cmp edi, 4
009B1C8E  0F 84 98 00 00 00               je 0x1409b1d2c
009B1C94  83 FF 08                        cmp edi, 8
009B1C97  0F 85 D7 FE FF FF               jne 0x1409b1b74
009B1C9D  83 C8 02                        or eax, 2
009B1CA0  48 8D 0D 79 3B 54 00            lea rcx, [rip + 0x543b79]
009B1CA7  89 42 30                        mov dword ptr [rdx + 0x30], eax
009B1CAA  E8 F1 E6 89 FF                  call 0x1402503a0
009B1CAF  E8 FC BB 8A FF                  call 0x14025d8b0
009B1CB4  33 D2                           xor edx, edx
009B1CB6  48 8B CE                        mov rcx, rsi
009B1CB9  E8 A2 C6 B4 FF                  call 0x1404fe360
009B1CBE  EB 65                           jmp 0x1409b1d25
009B1CC0  41 8B DF                        mov ebx, r15d
009B1CC3  E9 AC FE FF FF                  jmp 0x1409b1b74
009B1CC8  45 33 C0                        xor r8d, r8d
009B1CCB  49 8B CE                        mov rcx, r14
009B1CCE  E8 7D 0B E9 FF                  call 0x140842850
009B1CD3  85 C0                           test eax, eax
009B1CD5  0F 89 E1 00 00 00               jns 0x1409b1dbc
009B1CDB  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
009B1CDF  E9 F3 FE FF FF                  jmp 0x1409b1bd7
009B1CE4  44 88 7D 80                     mov byte ptr [rbp - 0x80], r15b
009B1CE8  E9 01 FE FF FF                  jmp 0x1409b1aee
009B1CED  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009B1CF2  E9 7D FE FF FF                  jmp 0x1409b1b74
009B1CF7  4C 8B C3                        mov r8, rbx
009B1CFA  49 8B CE                        mov rcx, r14
009B1CFD  E8 12 E3 E3 FF                  call 0x1407f0014
009B1D02  EB 21                           jmp 0x1409b1d25
009B1D04  83 C8 01                        or eax, 1
009B1D07  48 8D 0D 12 3B 54 00            lea rcx, [rip + 0x543b12]
009B1D0E  89 42 30                        mov dword ptr [rdx + 0x30], eax
009B1D11  E8 8A E6 89 FF                  call 0x1402503a0
009B1D16  E8 95 BB 8A FF                  call 0x14025d8b0
009B1D1B  33 D2                           xor edx, edx
009B1D1D  48 8B CE                        mov rcx, rsi
009B1D20  E8 DB C4 B4 FF                  call 0x1404fe200
009B1D25  8B D8                           mov ebx, eax
009B1D27  E9 48 FE FF FF                  jmp 0x1409b1b74
009B1D2C  83 C8 04                        or eax, 4
009B1D2F  48 8D 0D EA 3A 54 00            lea rcx, [rip + 0x543aea]
009B1D36  89 42 30                        mov dword ptr [rdx + 0x30], eax
009B1D39  E8 62 E6 89 FF                  call 0x1402503a0
009B1D3E  E8 6D BB 8A FF                  call 0x14025d8b0
009B1D43  33 D2                           xor edx, edx
009B1D45  48 8B CE                        mov rcx, rsi
009B1D48  E8 D3 C2 B4 FF                  call 0x1404fe020
009B1D4D  E9 22 FE FF FF                  jmp 0x1409b1b74
009B1D52  48 8B 89 08 06 00 00            mov rcx, qword ptr [rcx + 0x608]
009B1D59  48 8D 55 97                     lea rdx, [rbp - 0x69]
009B1D5D  E8 4A 85 00 00                  call 0x1409ba2ac
009B1D62  85 C0                           test eax, eax
009B1D64  0F 88 F3 FC FF FF               js 0x1409b1a5d
009B1D6A  BA 00 00 02 00                  mov edx, 0x20000
009B1D6F  48 8D 4D DF                     lea rcx, [rbp - 0x21]
009B1D73  E8 D8 DE 9E FF                  call 0x14039fc50
009B1D78  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
009B1D7C  0F 10 40 58                     movups xmm0, xmmword ptr [rax + 0x58]
009B1D80  F3 0F 7F 45 CF                  movdqu xmmword ptr [rbp - 0x31], xmm0
009B1D85  E9 D3 FC FF FF                  jmp 0x1409b1a5d
009B1D8A  E8 2D 11 00 00                  call 0x1409b2ebc
009B1D8F  E9 89 FE FF FF                  jmp 0x1409b1c1d
009B1D94  48 8D 4D 97                     lea rcx, [rbp - 0x69]
009B1D98  E8 63 EA 00 00                  call 0x1409c0800
009B1D9D  E9 8F FE FF FF                  jmp 0x1409b1c31
009B1DA2  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
009B1DA6  83 FF 08                        cmp edi, 8
009B1DA9  0F 84 1B BE 17 00               je 0x140b2dbca
009B1DAF  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009B1DB4  89 5D 93                        mov dword ptr [rbp - 0x6d], ebx
009B1DB7  E9 48 FD FF FF                  jmp 0x1409b1b04
009B1DBC  48 8B 45 87                     mov rax, qword ptr [rbp - 0x79]
009B1DC0  83 60 30 DF                     and dword ptr [rax + 0x30], 0xffffffdf
009B1DC4  E9 12 FF FF FF                  jmp 0x1409b1cdb
009B1DC9  83 FF 04                        cmp edi, 4
009B1DCC  0F 84 41 FD FF FF               je 0x1409b1b13
009B1DD2  E9 08 FE FF FF                  jmp 0x1409b1bdf
009B1DD7  33 D2                           xor edx, edx
009B1DD9  48 8B CE                        mov rcx, rsi
009B1DDC  E8 3F C2 B4 FF                  call 0x1404fe020
009B1DE1  E9 4B FD FF FF                  jmp 0x1409b1b31
009B1DE6  33 D2                           xor edx, edx
009B1DE8  48 8B CE                        mov rcx, rsi
009B1DEB  41 80 FF 01                     cmp r15b, 1
009B1DEF  0F 85 E9 BD 17 00               jne 0x140b2dbde
009B1DF5  E8 86 C4 B4 FF                  call 0x1404fe280
009B1DFA  E9 61 FE FF FF                  jmp 0x1409b1c60
009B1DFF  48 8B C8                        mov rcx, rax
009B1E02  E8 A9 B4 CF FF                  call 0x1406ad2b0
009B1E07  E9 32 FD FF FF                  jmp 0x1409b1b3e
009B1E0C  41 B5 20                        mov r13b, 0x20
009B1E0F  E9 45 FD FF FF                  jmp 0x1409b1b59
009B1E14  41 B5 1E                        mov r13b, 0x1e
009B1E17  E9 3D FD FF FF                  jmp 0x1409b1b59
009B1E1C  41 B5 1F                        mov r13b, 0x1f
009B1E1F  E9 35 FD FF FF                  jmp 0x1409b1b59
009B1E24  45 84 ED                        test r13b, r13b
009B1E27  0F 84 3C FD FF FF               je 0x1409b1b69
009B1E2D  48 83 7D 9F 00                  cmp qword ptr [rbp - 0x61], 0
009B1E32  0F 84 3C FD FF FF               je 0x1409b1b74
009B1E38  8B 55 8F                        mov edx, dword ptr [rbp - 0x71]
009B1E3B  48 8D 4D 97                     lea rcx, [rbp - 0x69]
009B1E3F  44 8B 4D 93                     mov r9d, dword ptr [rbp - 0x6d]
009B1E43  4C 8D 45 CF                     lea r8, [rbp - 0x31]
009B1E47  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
009B1E4C  41 8A CD                        mov cl, r13b
009B1E4F  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
009B1E53  48 8D 55 DF                     lea rdx, [rbp - 0x21]
009B1E57  E8 74 8C D0 FF                  call 0x1406baad0
009B1E5C  E9 08 FD FF FF                  jmp 0x1409b1b69
009B1E61  48 8D 4D 97                     lea rcx, [rbp - 0x69]
009B1E65  E8 96 E9 00 00                  call 0x1409c0800
009B1E6A  E9 05 FD FF FF                  jmp 0x1409b1b74
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmKtmNotification(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m47;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int8 v_stack_mC6;
    unsigned __int8 v_stack_mC7;
    unsigned __int8 v_stack_mC8;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p40;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 4558285)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r15 = 0;
    v_stack_mC0 = 0;
    result = 0;
    v_stack_mA0 = 0;
    v_stack_m80 = 0;
    v_stack_mC6 = 0;
    v_stack_mC8 = 0;
    v_stack_m90 = v_xmm0;
    v_stack_mB8 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_mB0 = v_xmm1;
    v_stack_mC7 = 1;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    result = CmpInitializeThreadInfo(v_stack_m90, a2, a3, a4);
    result = CmpIsCmRm(a2, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_009B1CED;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 104)))) & (8)) != 0) goto loc_009B1CC0;
    if (((unsigned int)((unsigned int)(a4))) == 256) goto loc_009B1CF7;
    if ((((unsigned __int8)((unsigned int)(a4))) & (14)) == 0) goto loc_009B1CC0;
    result = TmReferenceEnlistmentKey(a1, v_stack_mC0, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_009B1B74;
    result = LOCK_TRANSACTION_LIST(a1, v_stack_mC0, a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC0 + 48)))) & (8)) != 0) goto loc_009B1C86;
    result = ExReleaseFastMutexUnsafe(v_rip + 5520878, v_stack_mC0, a3, a4);
    result = KeLeaveCriticalRegion(v_rip + 5520878, v_stack_mC0, a3, a4);
    if ((*(unsigned __int64 *)(v_rip + 5497397)) != a2) goto loc_009B1BAF;
loc_009B1A50:
    if ((*(unsigned __int64 *)(v_rip + 6449017)) != 0) goto loc_009B1D52;
loc_009B1A5D:
    if ((*(unsigned __int64 *)(v_rip + 6449075)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_009B1BA7;
    result = LOCK_HIVE_LOAD(*(unsigned __int64 *)(v_rip + 4554902), v_stack_mC0, a3, a4);
loc_009B1A7B:
    result = CmpIsCmRm(a2, v_stack_mC0, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_009B1C14;
    if (((unsigned int)((unsigned int)(a4))) != 2) goto loc_009B1C67;
    result = CmpTransMgrPrepare(a2, v_stack_mC0, v_stack_mB8, v_stack_mC8);
loc_009B1AAD:
    v_stack_mB4 = (unsigned int)(result);
    if (sign_flag) goto loc_009B1C02;
loc_009B1ABA:
    v_stack_mB4 = (unsigned int)((unsigned int)((unsigned int)(result)));
    if ((*(unsigned __int64 *)(v_stack_mC0 + 16)) == (v_stack_mC0 + 16)) goto loc_009B1CE4;
    if (sign_flag) goto loc_009B1CE4;
    result = CmLogTmRmAction(a2, v_stack_mC0, (unsigned int)(a4) + 2, v_stack_mC8);
    v_rbx = 0;
    if (((unsigned int)((unsigned int)(a4))) == 2) { v_rbx = (unsigned int)(result); }
loc_009B1AEE:
    v_stack_mC6 = 1;
    if (((unsigned int)((unsigned int)(a4))) == 4) goto loc_009B1BB8;
loc_009B1AFB:
    if (((unsigned int)((unsigned int)(a4))) == 8) goto loc_009B1BB8;
loc_009B1B04:
    if (((unsigned __int8)(v_stack_mC8)) == 1) goto loc_009B1BBD;
loc_009B1B13:
    a2 = 0;
    result = TmDereferenceEnlistmentKey(a1, a2, (unsigned int)(a4) + 2, v_stack_mC8);
    if (1 != 0) {
        result = UNLOCK_HIVE_LOAD(a1, a2, (unsigned int)(a4) + 2, v_stack_mC8);
    }
    if (v_stack_mC6 == 1) goto loc_009B1C3B;
loc_009B1B31:
    if (v_stack_mA0 != 0) goto loc_009B1DFF;
loc_009B1B3E:
    if (((unsigned int)((unsigned int)(a4))) == 2) goto loc_009B1E1C;
    if (((unsigned int)((unsigned int)(a4))) == 4) goto loc_009B1E14;
    if (((unsigned int)((unsigned int)(a4))) == 8) goto loc_009B1E0C;
loc_009B1B59:
    if (*(unsigned __int64 *)(v_rip + 6448752) != 0) goto loc_009B1E24;
loc_009B1B69:
    if (v_stack_mA8 != 0) goto loc_009B1E61;
loc_009B1B74:
    result = CmCleanupThreadInfo(v_stack_m90, a2, (unsigned int)(a4) + 2, v_stack_mC8);
loc_009B1B7F:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(a4) + 2, v_stack_mC8);
    v_rsp = (v_rsp) + (208);
    return result;
loc_009B1BA7:
    goto loc_009B1A7B;
loc_009B1BAF:
    goto loc_009B1A50;
loc_009B1BB8:
loc_009B1BBD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 80) + 72)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 80) + 80);
        v_stack_mA0 = result;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 80) + 48)))) & (32)) != 0) goto loc_009B1CC8;
loc_009B1BD7:
    if (sign_flag) goto loc_009B1DC9;
loc_009B1BDF:
    result = CmpTransMgrRollback(*(unsigned __int64 *)(a2 + 80), v_stack_mB8, (unsigned int)(a4) + 2, v_stack_mC8);
    result = CmpCleanupTransactionState(0, v_stack_mC0, (unsigned int)((unsigned int)((unsigned int)(a4))), v_stack_mC7);
    goto loc_009B1B13;
loc_009B1C02:
    if (((unsigned int)((unsigned int)(a4))) == 4) goto loc_009B1ABA;
    goto loc_009B1AFB;
loc_009B1C14:
    if ((unsigned __int8)((unsigned __int8)(v_stack_mC8)) != 0) goto loc_009B1D8A;
loc_009B1C1D:
    a2 = 0;
    result = TmDereferenceEnlistmentKey(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a4))), v_stack_mC7);
    if (v_stack_mA8 != v_stack_p40) goto loc_009B1D94;
loc_009B1C31:
    goto loc_009B1B7F;
loc_009B1C3B:
    if (((unsigned int)((unsigned int)(a4))) == 2) goto loc_009B1DE6;
    if (((unsigned int)((unsigned int)(a4))) == 4) goto loc_009B1DD7;
    if (((unsigned int)((unsigned int)(a4))) != 8) goto loc_009B1B31;
    a2 = 0;
    result = TmRollbackComplete(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a4))), v_stack_mC7);
loc_009B1C60:
    goto loc_009B1B31;
loc_009B1C67:
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_009B1DA2;
    result = CmpTransMgrCommit(a1, v_stack_mC0, v_stack_mB8, v_stack_mC7);
    goto loc_009B1AAD;
loc_009B1C86:
    if (((unsigned int)((unsigned int)(a4))) == 2) goto loc_009B1D04;
    if (((unsigned int)((unsigned int)(a4))) == 4) goto loc_009B1D2C;
    if (((unsigned int)((unsigned int)(a4))) != 8) goto loc_009B1B74;
    result = (unsigned int)((result) | (2));
    *(unsigned int *)(v_stack_mC0 + 48) = (unsigned int)(result);
    result = ExReleaseFastMutexUnsafe(v_rip + 5520249, v_stack_mC0, (unsigned int)(a4) + 12, v_stack_mC7);
    result = KeLeaveCriticalRegion(v_rip + 5520249, v_stack_mC0, (unsigned int)(a4) + 12, v_stack_mC7);
    a2 = 0;
    result = TmRollbackComplete(a1, a2, (unsigned int)(a4) + 12, v_stack_mC7);
    goto loc_009B1D25;
loc_009B1CC0:
    goto loc_009B1B74;
loc_009B1CC8:
    a3 = 0;
    result = CmpAccountForLogReservation(0, a2, a3, v_stack_mC7);
    if (!sign_flag) goto loc_009B1DBC;
loc_009B1CDB:
    goto loc_009B1BD7;
loc_009B1CE4:
    v_stack_mC7 = (unsigned __int8)(v_stack_p40);
    goto loc_009B1AEE;
loc_009B1CED:
    goto loc_009B1B74;
loc_009B1CF7:
    result = CmpRecoverEnlistment(0, a2, (unsigned int)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1D25;
loc_009B1D04:
    result = (unsigned int)((result) | (1));
    *(unsigned int *)(a2 + 48) = (unsigned int)(result);
    result = ExReleaseFastMutexUnsafe(v_rip + 5520146, a2, (unsigned int)(0xC000000DULL), v_stack_mC7);
    result = KeLeaveCriticalRegion(v_rip + 5520146, a2, (unsigned int)(0xC000000DULL), v_stack_mC7);
    a2 = 0;
    result = TmPrepareComplete(a1, a2, (unsigned int)(0xC000000DULL), v_stack_mC7);
loc_009B1D25:
    goto loc_009B1B74;
loc_009B1D2C:
    result = (unsigned int)((result) | (4));
    *(unsigned int *)(a2 + 48) = (unsigned int)(result);
    result = ExReleaseFastMutexUnsafe(v_rip + 5520106, a2, (unsigned int)(0xC000000DULL), v_stack_mC7);
    result = KeLeaveCriticalRegion(v_rip + 5520106, a2, (unsigned int)(0xC000000DULL), v_stack_mC7);
    a2 = 0;
    result = TmCommitComplete(a1, a2, (unsigned int)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1B74;
loc_009B1D52:
    result = CmpQueryNameString(*(unsigned __int64 *)(a1 + 1544), v_stack_mB0, (unsigned int)(0xC000000DULL), v_stack_mC7);
    if (sign_flag) goto loc_009B1A5D;
    result = EtwGetKernelTraceTimestamp(v_stack_m68, (unsigned int)(0x20000ULL), (unsigned int)(0xC000000DULL), v_stack_mC7);
    v_stack_m78 = v_xmm0;
    goto loc_009B1A5D;
loc_009B1D8A:
    result = UNLOCK_HIVE_LOAD(v_stack_m68, (unsigned int)(0x20000ULL), (unsigned int)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1C1D;
loc_009B1D94:
    result = RtlFreeAnsiString(v_stack_mB0, (unsigned int)(0x20000ULL), (unsigned int)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1C31;
loc_009B1DA2:
    v_stack_mB4 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_009B1B04;
loc_009B1DBC:
    goto loc_009B1CDB;
loc_009B1DC9:
    if (((unsigned int)((unsigned int)(a4))) == 4) goto loc_009B1B13;
    goto loc_009B1BDF;
loc_009B1DD7:
    a2 = 0;
    result = TmCommitComplete(a1, a2, (unsigned int)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1B31;
loc_009B1DE6:
    a2 = 0;
    result = TmReadOnlyEnlistment(a1, a2, (unsigned int)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1C60;
loc_009B1DFF:
    result = ZwClose(result, a2, (unsigned int)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1B3E;
loc_009B1E0C:
    goto loc_009B1B59;
loc_009B1E14:
    goto loc_009B1B59;
loc_009B1E1C:
    goto loc_009B1B59;
loc_009B1E24:
    if (31 == 0) goto loc_009B1B69;
    if (v_stack_mA8 == 0) goto loc_009B1B74;
    v_stack_p28 = v_stack_mB0;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_mB8));
    result = guard_dispatch_icall(31, v_stack_m68, v_stack_m78, (unsigned int)(v_stack_mB4));
    goto loc_009B1B69;
loc_009B1E61:
    result = RtlFreeAnsiString(v_stack_mB0, v_stack_m68, v_stack_m78, (unsigned int)(v_stack_mB4));
    goto loc_009B1B74;
}
```

## 5. (Beta) C Style

```c
int64_t CmKtmNotification(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, uint64_t Arg5, uint64_t Arg6, int64_t Arg7)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m47;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint8_t v_stack_mC6;
    uint8_t v_stack_mC7;
    uint8_t v_stack_mC8;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p40;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x458DCD)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r15 = 0;
    v_stack_mC0 = 0;
    result = 0;
    v_stack_mA0 = 0;
    v_stack_m80 = 0;
    v_stack_mC6 = 0;
    v_stack_mC8 = 0;
    v_stack_m90 = v_xmm0;
    v_stack_mB8 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_mB0 = v_xmm1;
    v_stack_mC7 = 1;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    result = CmpInitializeThreadInfo(v_stack_m90, Arg2, Arg3, Arg4);
    result = CmpIsCmRm(Arg2, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_009B1CED;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x68)))) & (8)) != 0) goto loc_009B1CC0;
    if (((uint32_t)((uint32_t)(Arg4))) == 256) goto loc_009B1CF7;
    if ((((uint8_t)((uint32_t)(Arg4))) & (14)) == 0) goto loc_009B1CC0;
    result = TmReferenceEnlistmentKey(Arg1, v_stack_mC0, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_009B1B74;
    result = LOCK_TRANSACTION_LIST(Arg1, v_stack_mC0, Arg3, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x30)))) & (8)) != 0) goto loc_009B1C86;
    result = ExReleaseFastMutexUnsafe(v_rip + 5520878, v_stack_mC0, Arg3, Arg4);
    result = KeLeaveCriticalRegion(v_rip + 5520878, v_stack_mC0, Arg3, Arg4);
    if ((*(uint64_t *)(v_rip + 0x53E235)) != Arg2) goto loc_009B1BAF;
loc_009B1A50:
    if ((*(uint64_t *)(v_rip + 0x626779)) != 0) goto loc_009B1D52;
loc_009B1A5D:
    if ((*(uint64_t *)(v_rip + 0x6267B3)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_009B1BA7;
    result = LOCK_HIVE_LOAD(*(uint64_t *)(v_rip + 0x458096), v_stack_mC0, Arg3, Arg4);
loc_009B1A7B:
    result = CmpIsCmRm(Arg2, v_stack_mC0, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_009B1C14;
    if (((uint32_t)((uint32_t)(Arg4))) != 2) goto loc_009B1C67;
    result = CmpTransMgrPrepare(Arg2, v_stack_mC0, v_stack_mB8, v_stack_mC8);
loc_009B1AAD:
    v_stack_mB4 = (uint32_t)(result);
    if (sign_flag) goto loc_009B1C02;
loc_009B1ABA:
    v_stack_mB4 = (uint32_t)((uint32_t)((uint32_t)(result)));
    if ((*(uint64_t *)(v_stack_mC0 + 0x10)) == (v_stack_mC0 + 16)) goto loc_009B1CE4;
    if (sign_flag) goto loc_009B1CE4;
    result = CmLogTmRmAction(Arg2, v_stack_mC0, (uint32_t)(Arg4) + 2, v_stack_mC8);
    local_rbx = 0;
    if (((uint32_t)((uint32_t)(Arg4))) == 2) { local_rbx = (uint32_t)(result); }
loc_009B1AEE:
    v_stack_mC6 = 1;
    if (((uint32_t)((uint32_t)(Arg4))) == 4) goto loc_009B1BB8;
loc_009B1AFB:
    if (((uint32_t)((uint32_t)(Arg4))) == 8) goto loc_009B1BB8;
loc_009B1B04:
    if (((uint8_t)(v_stack_mC8)) == 1) goto loc_009B1BBD;
loc_009B1B13:
    Arg2 = 0;
    result = TmDereferenceEnlistmentKey(Arg1, Arg2, (uint32_t)(Arg4) + 2, v_stack_mC8);
    if (1 != 0) {
        result = UNLOCK_HIVE_LOAD(Arg1, Arg2, (uint32_t)(Arg4) + 2, v_stack_mC8);
    }
    if (v_stack_mC6 == 1) goto loc_009B1C3B;
loc_009B1B31:
    if (v_stack_mA0 != 0) goto loc_009B1DFF;
loc_009B1B3E:
    if (((uint32_t)((uint32_t)(Arg4))) == 2) goto loc_009B1E1C;
    if (((uint32_t)((uint32_t)(Arg4))) == 4) goto loc_009B1E14;
    if (((uint32_t)((uint32_t)(Arg4))) == 8) goto loc_009B1E0C;
loc_009B1B59:
    if (*(uint64_t *)(v_rip + 0x626670) != 0) goto loc_009B1E24;
loc_009B1B69:
    if (v_stack_mA8 != 0) goto loc_009B1E61;
loc_009B1B74:
    result = CmCleanupThreadInfo(v_stack_m90, Arg2, (uint32_t)(Arg4) + 2, v_stack_mC8);
loc_009B1B7F:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(Arg4) + 2, v_stack_mC8);
    local_rsp = (local_rsp) + (208);
    return result;
loc_009B1BA7:
    goto loc_009B1A7B;
loc_009B1BAF:
    goto loc_009B1A50;
loc_009B1BB8:
loc_009B1BBD:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x50) + 0x48)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg2 + 0x50) + 0x50);
        v_stack_mA0 = result;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x50) + 0x30)))) & (32)) != 0) goto loc_009B1CC8;
loc_009B1BD7:
    if (sign_flag) goto loc_009B1DC9;
loc_009B1BDF:
    result = CmpTransMgrRollback(*(uint64_t *)(arg2 + 0x50), v_stack_mB8, (uint32_t)(Arg4) + 2, v_stack_mC8);
    result = CmpCleanupTransactionState(0, v_stack_mC0, (uint32_t)((uint32_t)((uint32_t)(Arg4))), v_stack_mC7);
    goto loc_009B1B13;
loc_009B1C02:
    if (((uint32_t)((uint32_t)(Arg4))) == 4) goto loc_009B1ABA;
    goto loc_009B1AFB;
loc_009B1C14:
    if ((uint8_t)((uint8_t)(v_stack_mC8)) != 0) goto loc_009B1D8A;
loc_009B1C1D:
    Arg2 = 0;
    result = TmDereferenceEnlistmentKey(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg4))), v_stack_mC7);
    if (v_stack_mA8 != v_stack_p40) goto loc_009B1D94;
loc_009B1C31:
    goto loc_009B1B7F;
loc_009B1C3B:
    if (((uint32_t)((uint32_t)(Arg4))) == 2) goto loc_009B1DE6;
    if (((uint32_t)((uint32_t)(Arg4))) == 4) goto loc_009B1DD7;
    if (((uint32_t)((uint32_t)(Arg4))) != 8) goto loc_009B1B31;
    Arg2 = 0;
    result = TmRollbackComplete(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg4))), v_stack_mC7);
loc_009B1C60:
    goto loc_009B1B31;
loc_009B1C67:
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_009B1DA2;
    result = CmpTransMgrCommit(Arg1, v_stack_mC0, v_stack_mB8, v_stack_mC7);
    goto loc_009B1AAD;
loc_009B1C86:
    if (((uint32_t)((uint32_t)(Arg4))) == 2) goto loc_009B1D04;
    if (((uint32_t)((uint32_t)(Arg4))) == 4) goto loc_009B1D2C;
    if (((uint32_t)((uint32_t)(Arg4))) != 8) goto loc_009B1B74;
    result = (uint32_t)((result) | (2));
    *(uint32_t *)(v_stack_mC0 + 0x30) = (uint32_t)(result);
    result = ExReleaseFastMutexUnsafe(v_rip + 5520249, v_stack_mC0, (uint32_t)(Arg4) + 12, v_stack_mC7);
    result = KeLeaveCriticalRegion(v_rip + 5520249, v_stack_mC0, (uint32_t)(Arg4) + 12, v_stack_mC7);
    Arg2 = 0;
    result = TmRollbackComplete(Arg1, Arg2, (uint32_t)(Arg4) + 12, v_stack_mC7);
    goto loc_009B1D25;
loc_009B1CC0:
    goto loc_009B1B74;
loc_009B1CC8:
    Arg3 = 0;
    result = CmpAccountForLogReservation(0, Arg2, Arg3, v_stack_mC7);
    if (!sign_flag) goto loc_009B1DBC;
loc_009B1CDB:
    goto loc_009B1BD7;
loc_009B1CE4:
    v_stack_mC7 = (uint8_t)(v_stack_p40);
    goto loc_009B1AEE;
loc_009B1CED:
    goto loc_009B1B74;
loc_009B1CF7:
    result = CmpRecoverEnlistment(0, Arg2, (uint32_t)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1D25;
loc_009B1D04:
    result = (uint32_t)((result) | (1));
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
    result = ExReleaseFastMutexUnsafe(v_rip + 5520146, Arg2, (uint32_t)(0xC000000DULL), v_stack_mC7);
    result = KeLeaveCriticalRegion(v_rip + 5520146, Arg2, (uint32_t)(0xC000000DULL), v_stack_mC7);
    Arg2 = 0;
    result = TmPrepareComplete(Arg1, Arg2, (uint32_t)(0xC000000DULL), v_stack_mC7);
loc_009B1D25:
    goto loc_009B1B74;
loc_009B1D2C:
    result = (uint32_t)((result) | (4));
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
    result = ExReleaseFastMutexUnsafe(v_rip + 5520106, Arg2, (uint32_t)(0xC000000DULL), v_stack_mC7);
    result = KeLeaveCriticalRegion(v_rip + 5520106, Arg2, (uint32_t)(0xC000000DULL), v_stack_mC7);
    Arg2 = 0;
    result = TmCommitComplete(Arg1, Arg2, (uint32_t)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1B74;
loc_009B1D52:
    result = CmpQueryNameString(*(uint64_t *)(Arg1 + 0x608), v_stack_mB0, (uint32_t)(0xC000000DULL), v_stack_mC7);
    if (sign_flag) goto loc_009B1A5D;
    result = EtwGetKernelTraceTimestamp(v_stack_m68, (uint32_t)(0x20000ULL), (uint32_t)(0xC000000DULL), v_stack_mC7);
    v_stack_m78 = v_xmm0;
    goto loc_009B1A5D;
loc_009B1D8A:
    result = UNLOCK_HIVE_LOAD(v_stack_m68, (uint32_t)(0x20000ULL), (uint32_t)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1C1D;
loc_009B1D94:
    result = RtlFreeAnsiString(v_stack_mB0, (uint32_t)(0x20000ULL), (uint32_t)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1C31;
loc_009B1DA2:
    v_stack_mB4 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_009B1B04;
loc_009B1DBC:
    goto loc_009B1CDB;
loc_009B1DC9:
    if (((uint32_t)((uint32_t)(Arg4))) == 4) goto loc_009B1B13;
    goto loc_009B1BDF;
loc_009B1DD7:
    Arg2 = 0;
    result = TmCommitComplete(Arg1, Arg2, (uint32_t)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1B31;
loc_009B1DE6:
    Arg2 = 0;
    result = TmReadOnlyEnlistment(Arg1, Arg2, (uint32_t)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1C60;
loc_009B1DFF:
    result = ZwClose(result, Arg2, (uint32_t)(0xC000000DULL), v_stack_mC7);
    goto loc_009B1B3E;
loc_009B1E0C:
    goto loc_009B1B59;
loc_009B1E14:
    goto loc_009B1B59;
loc_009B1E1C:
    goto loc_009B1B59;
loc_009B1E24:
    if (31 == 0) goto loc_009B1B69;
    if (v_stack_mA8 == 0) goto loc_009B1B74;
    v_stack_p28 = v_stack_mB0;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_mB8));
    result = guard_dispatch_icall(31, v_stack_m68, v_stack_m78, (uint32_t)(v_stack_mB4));
    goto loc_009B1B69;
loc_009B1E61:
    result = RtlFreeAnsiString(v_stack_mB0, v_stack_m68, v_stack_m78, (uint32_t)(v_stack_mB4));
    goto loc_009B1B74;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x50` | `64` | `R` |
| `Arg2` | `+ 0x68` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009B1950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
