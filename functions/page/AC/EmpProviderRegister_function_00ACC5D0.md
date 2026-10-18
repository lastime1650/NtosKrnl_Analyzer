# EmpProviderRegister

- RVA: `0x00ACC5D0`–`0x00ACC9D1` (길이 `1,025` bytes)
- VA: `0x0000000140ACC5D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A06E8`
- 디코드: `290`개 명령, `1,025/1,025` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00ACC610` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00ACC629` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00ACC670` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ACC6C7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ACC710` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ACC737` → [EmpSearchEntryDatabase](../../text/58/EmpSearchEntryDatabase_function_00580CE8.md) (function, `0x00580CE8`)
- `0x00ACC7BB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ACC7F3` → [EmpSearchCallbackDatabase](../../text/58/EmpSearchCallbackDatabase_function_00580CB0.md) (function, `0x00580CB0`)
- `0x00ACC84E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ACC89B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ACC8DC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ACC8E9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ACC91E` → [EmpQueueRuleUpdateState](../../text/58/EmpQueueRuleUpdateState_function_005809B0.md) (function, `0x005809B0`)
- `0x00ACC951` → [EmpQueueRuleUpdateState](../../text/58/EmpQueueRuleUpdateState_function_005809B0.md) (function, `0x005809B0`)
- `0x00ACC96D` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00ACC9A0` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00ACC9AC` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- [EmProviderRegister](../71/EmProviderRegister_function_007132C0.md) at `0x007132E2`
- [HalRegisterErrataCallbacks](../../init/BE/HalRegisterErrataCallbacks_function_00BEEE80.md) at `0x00BEEEA4`
- [EmInitSystem](../../init/C7/EmInitSystem_function_00C71150.md) at `0x00C712A7`
- [EmInitSystem](../../init/C7/EmInitSystem_function_00C71150.md) at `0x00C712CC`
- [EmInitSystem](../../init/C7/EmInitSystem_function_00C71150.md) at `0x00C712EF`
- [PoInitSystem](../../init/C7/PoInitSystem_function_00C72358.md) at `0x00C72D86`

### Static image references
- `0x00ACC5F3` → RVA `0x00F8F1E0` (`.data`; read)
- `0x00ACC988` → RVA `0x00F8F1E0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00ACC610` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00ACC629` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00ACC670` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ACC6C7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ACC710` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ACC737` → [EmpSearchEntryDatabase](../../text/58/EmpSearchEntryDatabase_function_00580CE8.md) (`PAGE` → `.text`)
  - `0x00ACC7BB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ACC7F3` → [EmpSearchCallbackDatabase](../../text/58/EmpSearchCallbackDatabase_function_00580CB0.md) (`PAGE` → `.text`)
  - `0x00ACC84E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ACC89B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ACC8DC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ACC8E9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ACC91E` → [EmpQueueRuleUpdateState](../../text/58/EmpQueueRuleUpdateState_function_005809B0.md) (`PAGE` → `.text`)
  - `0x00ACC951` → [EmpQueueRuleUpdateState](../../text/58/EmpQueueRuleUpdateState_function_005809B0.md) (`PAGE` → `.text`)
  - `0x00ACC96D` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00ACC9A0` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00ACC9AC` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ACC5D0  48 8B C4                        mov rax, rsp
00ACC5D3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00ACC5D7  48 89 68 18                     mov qword ptr [rax + 0x18], rbp
00ACC5DB  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
00ACC5DF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00ACC5E3  57                              push rdi
00ACC5E4  41 54                           push r12
00ACC5E6  41 55                           push r13
00ACC5E8  41 56                           push r14
00ACC5EA  41 57                           push r15
00ACC5EC  48 83 EC 20                     sub rsp, 0x20
00ACC5F0  41 8B E8                        mov ebp, r8d
00ACC5F3  48 8D 35 E6 2B 4C 00            lea rsi, [rip + 0x4c2be6]
00ACC5FA  4C 8B FA                        mov r15, rdx
00ACC5FD  4C 8B F1                        mov r14, rcx
00ACC600  48 8B CE                        mov rcx, rsi
00ACC603  45 33 C0                        xor r8d, r8d
00ACC606  33 D2                           xor edx, edx
00ACC608  4D 8B E1                        mov r12, r9
00ACC60B  45 33 ED                        xor r13d, r13d
00ACC60E  33 FF                           xor edi, edi
00ACC610  E8 1B 3C 74 FF                  call 0x140210230
00ACC615  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00ACC61B  48 8B D8                        mov rbx, rax
00ACC61E  73 0E                           jae 0x140acc62e
00ACC620  4C 8B C6                        mov r8, rsi
00ACC623  48 8B D0                        mov rdx, rax
00ACC626  48 8B CE                        mov rcx, rsi
00ACC629  E8 62 36 74 FF                  call 0x14020fc90
00ACC62E  48 85 DB                        test rbx, rbx
00ACC631  74 04                           je 0x140acc637
00ACC633  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00ACC637  48 39 7C 24 78                  cmp qword ptr [rsp + 0x78], rdi
00ACC63C  0F 84 3D 03 00 00               je 0x140acc97f
00ACC642  85 ED                           test ebp, ebp
00ACC644  74 09                           je 0x140acc64f
00ACC646  4D 85 FF                        test r15, r15
00ACC649  0F 84 30 03 00 00               je 0x140acc97f
00ACC64F  8B 74 24 70                     mov esi, dword ptr [rsp + 0x70]
00ACC653  85 F6                           test esi, esi
00ACC655  74 09                           je 0x140acc660
00ACC657  4D 85 E4                        test r12, r12
00ACC65A  0F 84 1F 03 00 00               je 0x140acc97f
00ACC660  BA 48 00 00 00                  mov edx, 0x48
00ACC665  B9 00 01 00 00                  mov ecx, 0x100
00ACC66A  41 B8 45 4D 70 72               mov r8d, 0x72704d45
00ACC670  E8 7B 5A 0B 00                  call 0x140b820f0
00ACC675  33 C9                           xor ecx, ecx
00ACC677  48 8B D8                        mov rbx, rax
00ACC67A  48 85 C0                        test rax, rax
00ACC67D  75 0A                           jne 0x140acc689
00ACC67F  BF 9A 00 00 C0                  mov edi, 0xc000009a
00ACC684  E9 FB 02 00 00                  jmp 0x140acc984
00ACC689  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00ACC68D  89 48 20                        mov dword ptr [rax + 0x20], ecx
00ACC690  48 89 48 28                     mov qword ptr [rax + 0x28], rcx
00ACC694  89 48 30                        mov dword ptr [rax + 0x30], ecx
00ACC697  48 89 48 08                     mov qword ptr [rax + 8], rcx
00ACC69B  89 48 10                        mov dword ptr [rax + 0x10], ecx
00ACC69E  48 83 C0 38                     add rax, 0x38
00ACC6A2  48 89 40 08                     mov qword ptr [rax + 8], rax
00ACC6A6  48 89 00                        mov qword ptr [rax], rax
00ACC6A9  85 ED                           test ebp, ebp
00ACC6AB  0F 84 F0 00 00 00               je 0x140acc7a1
00ACC6B1  41 BE 00 01 00 00               mov r14d, 0x100
00ACC6B7  8D 14 ED 00 00 00 00            lea edx, [rbp*8]
00ACC6BE  41 8B CE                        mov ecx, r14d
00ACC6C1  41 B8 45 4D 70 72               mov r8d, 0x72704d45
00ACC6C7  E8 24 5A 0B 00                  call 0x140b820f0
00ACC6CC  48 89 43 08                     mov qword ptr [rbx + 8], rax
00ACC6D0  48 85 C0                        test rax, rax
00ACC6D3  75 0A                           jne 0x140acc6df
00ACC6D5  BF 9A 00 00 C0                  mov edi, 0xc000009a
00ACC6DA  E9 61 01 00 00                  jmp 0x140acc840
00ACC6DF  89 6B 10                        mov dword ptr [rbx + 0x10], ebp
00ACC6E2  49 8D 47 08                     lea rax, [r15 + 8]
00ACC6E6  48 8B CD                        mov rcx, rbp
00ACC6E9  48 39 38                        cmp qword ptr [rax], rdi
00ACC6EC  74 03                           je 0x140acc6f1
00ACC6EE  FF 43 20                        inc dword ptr [rbx + 0x20]
00ACC6F1  48 83 C0 18                     add rax, 0x18
00ACC6F5  48 83 E9 01                     sub rcx, 1
00ACC6F9  75 EE                           jne 0x140acc6e9
00ACC6FB  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00ACC6FE  85 C0                           test eax, eax
00ACC700  74 1C                           je 0x140acc71e
00ACC702  C1 E0 05                        shl eax, 5
00ACC705  41 B8 45 4D 70 72               mov r8d, 0x72704d45
00ACC70B  8B D0                           mov edx, eax
00ACC70D  49 8B CE                        mov rcx, r14
00ACC710  E8 DB 59 0B 00                  call 0x140b820f0
00ACC715  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00ACC719  48 85 C0                        test rax, rax
00ACC71C  74 B7                           je 0x140acc6d5
00ACC71E  45 33 D2                        xor r10d, r10d
00ACC721  44 3B D5                        cmp r10d, ebp
00ACC724  73 76                           jae 0x140acc79c
00ACC726  4F 8D 34 52                     lea r14, [r10 + r10*2]
00ACC72A  4B 8B 0C F7                     mov rcx, qword ptr [r15 + r14*8]
00ACC72E  48 85 C9                        test rcx, rcx
00ACC731  0F 84 04 01 00 00               je 0x140acc83b
00ACC737  E8 AC 45 AB FF                  call 0x140580ce8
00ACC73C  48 8B D0                        mov rdx, rax
00ACC73F  48 85 C0                        test rax, rax
00ACC742  0F 84 EC 00 00 00               je 0x140acc834
00ACC748  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00ACC74C  4A 89 14 D0                     mov qword ptr [rax + r10*8], rdx
00ACC750  4B 8B 44 F7 08                  mov rax, qword ptr [r15 + r14*8 + 8]
00ACC755  48 85 C0                        test rax, rax
00ACC758  74 3D                           je 0x140acc797
00ACC75A  41 8B CD                        mov ecx, r13d
00ACC75D  48 C1 E1 05                     shl rcx, 5
00ACC761  48 03 4B 18                     add rcx, qword ptr [rbx + 0x18]
00ACC765  48 89 01                        mov qword ptr [rcx], rax
00ACC768  4B 8B 44 F7 10                  mov rax, qword ptr [r15 + r14*8 + 0x10]
00ACC76D  48 89 41 08                     mov qword ptr [rcx + 8], rax
00ACC771  48 8D 42 38                     lea rax, [rdx + 0x38]
00ACC775  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00ACC779  48 83 C1 10                     add rcx, 0x10
00ACC77D  48 39 02                        cmp qword ptr [rdx], rax
00ACC780  0F 85 6D 01 00 00               jne 0x140acc8f3
00ACC786  48 89 01                        mov qword ptr [rcx], rax
00ACC789  41 FF C5                        inc r13d
00ACC78C  48 89 51 08                     mov qword ptr [rcx + 8], rdx
00ACC790  48 89 0A                        mov qword ptr [rdx], rcx
00ACC793  48 89 48 08                     mov qword ptr [rax + 8], rcx
00ACC797  41 FF C2                        inc r10d
00ACC79A  EB 85                           jmp 0x140acc721
00ACC79C  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00ACC7A1  85 F6                           test esi, esi
00ACC7A3  0F 84 56 01 00 00               je 0x140acc8ff
00ACC7A9  8D 14 F5 00 00 00 00            lea edx, [rsi*8]
00ACC7B0  B9 00 01 00 00                  mov ecx, 0x100
00ACC7B5  41 B8 45 4D 70 72               mov r8d, 0x72704d45
00ACC7BB  E8 30 59 0B 00                  call 0x140b820f0
00ACC7C0  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
00ACC7C4  48 85 C0                        test rax, rax
00ACC7C7  0F 84 08 FF FF FF               je 0x140acc6d5
00ACC7CD  89 73 30                        mov dword ptr [rbx + 0x30], esi
00ACC7D0  45 33 D2                        xor r10d, r10d
00ACC7D3  44 3B D6                        cmp r10d, esi
00ACC7D6  0F 83 1E 01 00 00               jae 0x140acc8fa
00ACC7DC  4F 8D 1C 52                     lea r11, [r10 + r10*2]
00ACC7E0  4B 8B 6C DC 08                  mov rbp, qword ptr [r12 + r11*8 + 8]
00ACC7E5  48 85 ED                        test rbp, rbp
00ACC7E8  74 51                           je 0x140acc83b
00ACC7EA  4B 8B 0C DC                     mov rcx, qword ptr [r12 + r11*8]
00ACC7EE  48 85 C9                        test rcx, rcx
00ACC7F1  74 48                           je 0x140acc83b
00ACC7F3  E8 B8 44 AB FF                  call 0x140580cb0
00ACC7F8  48 8B C8                        mov rcx, rax
00ACC7FB  48 85 C0                        test rax, rax
00ACC7FE  74 34                           je 0x140acc834
00ACC800  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00ACC804  48 85 C0                        test rax, rax
00ACC807  74 05                           je 0x140acc80e
00ACC809  48 3B C5                        cmp rax, rbp
00ACC80C  75 1F                           jne 0x140acc82d
00ACC80E  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00ACC812  4A 89 0C D0                     mov qword ptr [rax + r10*8], rcx
00ACC816  41 FF C2                        inc r10d
00ACC819  4B 8B 44 DC 08                  mov rax, qword ptr [r12 + r11*8 + 8]
00ACC81E  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
00ACC822  4B 8B 44 DC 10                  mov rax, qword ptr [r12 + r11*8 + 0x10]
00ACC827  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
00ACC82B  EB A6                           jmp 0x140acc7d3
00ACC82D  BF 35 00 00 C0                  mov edi, 0xc0000035
00ACC832  EB 0C                           jmp 0x140acc840
00ACC834  BF 25 02 00 C0                  mov edi, 0xc0000225
00ACC839  EB 05                           jmp 0x140acc840
00ACC83B  BF 0D 00 00 C0                  mov edi, 0xc000000d
00ACC840  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00ACC844  48 85 C9                        test rcx, rcx
00ACC847  74 0A                           je 0x140acc853
00ACC849  BA 45 4D 70 72                  mov edx, 0x72704d45
00ACC84E  E8 1D 60 0B 00                  call 0x140b82870
00ACC853  48 83 7B 18 00                  cmp qword ptr [rbx + 0x18], 0
00ACC858  74 46                           je 0x140acc8a0
00ACC85A  33 D2                           xor edx, edx
00ACC85C  45 85 ED                        test r13d, r13d
00ACC85F  74 31                           je 0x140acc892
00ACC861  4C 8B 43 18                     mov r8, qword ptr [rbx + 0x18]
00ACC865  49 83 C0 10                     add r8, 0x10
00ACC869  8B CA                           mov ecx, edx
00ACC86B  48 C1 E1 05                     shl rcx, 5
00ACC86F  4C 03 C1                        add r8, rcx
00ACC872  49 8B 08                        mov rcx, qword ptr [r8]
00ACC875  4C 39 41 08                     cmp qword ptr [rcx + 8], r8
00ACC879  75 78                           jne 0x140acc8f3
00ACC87B  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
00ACC87F  4C 39 00                        cmp qword ptr [rax], r8
00ACC882  75 6F                           jne 0x140acc8f3
00ACC884  FF C2                           inc edx
00ACC886  48 89 08                        mov qword ptr [rax], rcx
00ACC889  48 89 41 08                     mov qword ptr [rcx + 8], rax
00ACC88D  41 3B D5                        cmp edx, r13d
00ACC890  72 CF                           jb 0x140acc861
00ACC892  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00ACC896  BA 45 4D 70 72                  mov edx, 0x72704d45
00ACC89B  E8 D0 5F 0B 00                  call 0x140b82870
00ACC8A0  48 83 7B 28 00                  cmp qword ptr [rbx + 0x28], 0
00ACC8A5  74 3A                           je 0x140acc8e1
00ACC8A7  85 F6                           test esi, esi
00ACC8A9  74 28                           je 0x140acc8d3
00ACC8AB  45 33 C0                        xor r8d, r8d
00ACC8AE  4C 8B CE                        mov r9, rsi
00ACC8B1  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00ACC8B5  49 8B 0C 00                     mov rcx, qword ptr [r8 + rax]
00ACC8B9  48 85 C9                        test rcx, rcx
00ACC8BC  74 0B                           je 0x140acc8c9
00ACC8BE  83 79 18 00                     cmp dword ptr [rcx + 0x18], 0
00ACC8C2  75 05                           jne 0x140acc8c9
00ACC8C4  48 83 61 10 00                  and qword ptr [rcx + 0x10], 0
00ACC8C9  49 83 C0 08                     add r8, 8
00ACC8CD  49 83 E9 01                     sub r9, 1
00ACC8D1  75 DE                           jne 0x140acc8b1
00ACC8D3  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00ACC8D7  BA 45 4D 70 72                  mov edx, 0x72704d45
00ACC8DC  E8 8F 5F 0B 00                  call 0x140b82870
00ACC8E1  BA 45 4D 70 72                  mov edx, 0x72704d45
00ACC8E6  48 8B CB                        mov rcx, rbx
00ACC8E9  E8 82 5F 0B 00                  call 0x140b82870
00ACC8EE  E9 91 00 00 00                  jmp 0x140acc984
00ACC8F3  B9 03 00 00 00                  mov ecx, 3
00ACC8F8  CD 29                           int 0x29
00ACC8FA  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00ACC8FF  33 ED                           xor ebp, ebp
00ACC901  39 7B 10                        cmp dword ptr [rbx + 0x10], edi
00ACC904  76 2C                           jbe 0x140acc932
00ACC906  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00ACC90A  48 8B 14 E8                     mov rdx, qword ptr [rax + rbp*8]
00ACC90E  F0 FF 42 10                     lock inc dword ptr [rdx + 0x10]
00ACC912  48 8B 72 48                     mov rsi, qword ptr [rdx + 0x48]
00ACC916  EB 0E                           jmp 0x140acc926
00ACC918  48 8B 4E F8                     mov rcx, qword ptr [rsi - 8]
00ACC91C  33 D2                           xor edx, edx
00ACC91E  E8 8D 40 AB FF                  call 0x1405809b0
00ACC923  48 8B 36                        mov rsi, qword ptr [rsi]
00ACC926  48 85 F6                        test rsi, rsi
00ACC929  75 ED                           jne 0x140acc918
00ACC92B  FF C5                           inc ebp
00ACC92D  3B 6B 10                        cmp ebp, dword ptr [rbx + 0x10]
00ACC930  72 D4                           jb 0x140acc906
00ACC932  33 ED                           xor ebp, ebp
00ACC934  39 7B 30                        cmp dword ptr [rbx + 0x30], edi
00ACC937  76 2C                           jbe 0x140acc965
00ACC939  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00ACC93D  48 8B 14 E8                     mov rdx, qword ptr [rax + rbp*8]
00ACC941  F0 FF 42 18                     lock inc dword ptr [rdx + 0x18]
00ACC945  48 8B 72 30                     mov rsi, qword ptr [rdx + 0x30]
00ACC949  EB 0E                           jmp 0x140acc959
00ACC94B  48 8B 4E F8                     mov rcx, qword ptr [rsi - 8]
00ACC94F  33 D2                           xor edx, edx
00ACC951  E8 5A 40 AB FF                  call 0x1405809b0
00ACC956  48 8B 36                        mov rsi, qword ptr [rsi]
00ACC959  48 85 F6                        test rsi, rsi
00ACC95C  75 ED                           jne 0x140acc94b
00ACC95E  FF C5                           inc ebp
00ACC960  3B 6B 30                        cmp ebp, dword ptr [rbx + 0x30]
00ACC963  72 D4                           jb 0x140acc939
00ACC965  4D 85 F6                        test r14, r14
00ACC968  74 08                           je 0x140acc972
00ACC96A  49 8B CE                        mov rcx, r14
00ACC96D  E8 AE 30 74 FF                  call 0x14020fa20
00ACC972  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00ACC977  4C 89 33                        mov qword ptr [rbx], r14
00ACC97A  48 89 18                        mov qword ptr [rax], rbx
00ACC97D  EB 05                           jmp 0x140acc984
00ACC97F  BF 0D 00 00 C0                  mov edi, 0xc000000d
00ACC984  48 83 CA FF                     or rdx, 0xffffffffffffffff
00ACC988  F0 48 0F C1 15 4F 28 4C 00      lock xadd qword ptr [rip + 0x4c284f], rdx
00ACC991  80 E2 06                        and dl, 6
00ACC994  80 FA 02                        cmp dl, 2
00ACC997  75 0C                           jne 0x140acc9a5
00ACC999  48 8D 0D 40 28 4C 00            lea rcx, [rip + 0x4c2840]
00ACC9A0  E8 2B 94 79 FF                  call 0x140265dd0
00ACC9A5  48 8D 0D 34 28 4C 00            lea rcx, [rip + 0x4c2834]
00ACC9AC  E8 4F 4C 81 FF                  call 0x1402e1600
00ACC9B1  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00ACC9B6  8B C7                           mov eax, edi
00ACC9B8  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
00ACC9BD  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00ACC9C2  48 83 C4 20                     add rsp, 0x20
00ACC9C6  41 5F                           pop r15
00ACC9C8  41 5E                           pop r14
00ACC9CA  41 5D                           pop r13
00ACC9CC  41 5C                           pop r12
00ACC9CE  5F                              pop rdi
00ACC9CF  C3                              ret
00ACC9D0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmpProviderRegister(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    v_r13 = 0;
    v_rdi = 0;
    result = KeAbPreAcquire(v_rip + 4991974, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 4991974;
        a2 = result;
        a1 = v_rip + 4991974;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (a6 == 0) goto loc_00ACC97F;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00ACC64F;
    if (a2 == 0) goto loc_00ACC97F;
loc_00ACC64F:
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_00ACC660;
    if (a4 == 0) goto loc_00ACC97F;
loc_00ACC660:
    result = ExAllocatePool2(256, 72, (unsigned int)(0x72704D45ULL), a4);
    a1 = 0;
    if (result != 0) goto loc_00ACC689;
    goto loc_00ACC984;
loc_00ACC689:
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned int *)(result + 32) = 0;
    *(unsigned __int64 *)(result + 40) = 0;
    *(unsigned int *)(result + 48) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    *(unsigned int *)(result + 16) = 0;
    result = (result) + (56);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00ACC7A1;
    result = ExAllocatePool2(256, (unsigned int)(a3) * 8, (unsigned int)(0x72704D45ULL), a4);
    *(unsigned __int64 *)(result + 8) = result;
    if (result != 0) goto loc_00ACC6DF;
loc_00ACC6D5:
    goto loc_00ACC840;
loc_00ACC6DF:
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(a3));
loc_00ACC6E9:
    if ((*(unsigned __int64 *)(a2 + 8)) != ((unsigned int)(0xC000009AULL))) {
    }
    result = (a2 + 8) + (24);
    a1 = ((unsigned int)(a3)) - (1);
    if (condition_is_not_equal) goto loc_00ACC6E9;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 32))) == 0) goto loc_00ACC71E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) << (5));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x72704D45ULL), a4);
    *(unsigned __int64 *)(result + 24) = result;
    if (result == 0) goto loc_00ACC6D5;
loc_00ACC71E:
    v_r10 = 0;
loc_00ACC721:
    if (0 >= ((unsigned int)((unsigned int)(a3)))) goto loc_00ACC79C;
    if (*(unsigned __int64 *)(a2 + v_r10 + v_r10 * 2 * 8) == 0) goto loc_00ACC83B;
    result = EmpSearchEntryDatabase(*(unsigned __int64 *)(a2 + v_r10 + v_r10 * 2 * 8), (unsigned int)((unsigned int)(result)), (unsigned int)(0x72704D45ULL), a4);
    if (result == 0) goto loc_00ACC834;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + v_r10 * 8) = result;
    if (*(unsigned __int64 *)(a2 + v_r10 + v_r10 * 2 * 8 + 8) == 0) goto loc_00ACC797;
    a1 = (0) << (5);
    a1 = (a1) + (*(unsigned __int64 *)(result + 24));
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a2 + v_r10 + v_r10 * 2 * 8 + 8);
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(a2 + v_r10 + v_r10 * 2 * 8 + 16);
    a1 = (a1) + (16);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 56 + 8))) != (result + 56)) goto loc_00ACC8F3;
    *(unsigned __int64 *)(a1) = result + 56;
    v_r13 = (unsigned int)((v_r13) + 1);
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(result + 56 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 56 + 8)) = a1;
    *(unsigned __int64 *)(result + 56 + 8) = a1;
loc_00ACC797:
    v_r10 = (unsigned int)((v_r10) + 1);
    goto loc_00ACC721;
loc_00ACC79C:
loc_00ACC7A1:
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_00ACC8FF;
    result = ExAllocatePool2(256, (unsigned int)(a5) * 8, (unsigned int)(0x72704D45ULL), a4);
    *(unsigned __int64 *)(result + 40) = result;
    if (result == 0) goto loc_00ACC6D5;
    *(unsigned int *)(result + 48) = (unsigned int)((unsigned int)(a5));
    v_r10 = 0;
loc_00ACC7D3:
    if (0 >= ((unsigned int)((unsigned int)(a5)))) goto loc_00ACC8FA;
    if (*(unsigned __int64 *)(a4 + v_r10 + v_r10 * 2 * 8 + 8) == 0) goto loc_00ACC83B;
    if (*(unsigned __int64 *)(a4 + v_r10 + v_r10 * 2 * 8) == 0) goto loc_00ACC83B;
    result = EmpSearchCallbackDatabase(*(unsigned __int64 *)(a4 + v_r10 + v_r10 * 2 * 8), (unsigned int)(a5) * 8, (unsigned int)(0x72704D45ULL), a4);
    if (result == 0) goto loc_00ACC834;
    if (*(unsigned __int64 *)(result + 16) == 0) goto loc_00ACC80E;
    if ((*(unsigned __int64 *)(result + 16)) != (*(unsigned __int64 *)(a4 + v_r10 + v_r10 * 2 * 8 + 8))) goto loc_00ACC82D;
loc_00ACC80E:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) + v_r10 * 8) = result;
    v_r10 = (unsigned int)((v_r10) + 1);
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(a4 + v_r10 + v_r10 * 2 * 8 + 8);
    *(unsigned __int64 *)(result + 32) = *(unsigned __int64 *)(a4 + v_r10 + v_r10 * 2 * 8 + 16);
    goto loc_00ACC7D3;
loc_00ACC82D:
    goto loc_00ACC840;
loc_00ACC834:
    goto loc_00ACC840;
loc_00ACC83B:
loc_00ACC840:
    result = *(unsigned __int64 *)(a4 + v_r10 + v_r10 * 2 * 8 + 16);
    if (*(unsigned __int64 *)(result + 8) != 0) {
        a2 = 0x72704D45ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 8), a2, (unsigned int)(0x72704D45ULL), a4);
    }
    if ((*(unsigned __int64 *)(result + 24)) == 0) goto loc_00ACC8A0;
    a2 = 0;
    if ((unsigned int)(v_r13) == 0) goto loc_00ACC892;
loc_00ACC861:
    a3 = (*(unsigned __int64 *)(result + 24)) + (16);
    a1 = (0) << (5);
    a3 = (a3) + (a1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 8)) != a3) goto loc_00ACC8F3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 8))) != a3) goto loc_00ACC8F3;
    a2 = (unsigned int)((a2) + 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 8)) = *(unsigned __int64 *)(a3);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 8) = *(unsigned __int64 *)(a3 + 8);
    if (((unsigned int)(a2)) < ((unsigned int)(v_r13))) goto loc_00ACC861;
loc_00ACC892:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 24), (unsigned int)(0x72704D45ULL), a3, a4);
loc_00ACC8A0:
    if ((*(unsigned __int64 *)(result + 40)) == 0) goto loc_00ACC8E1;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_00ACC8D3;
    a3 = 0;
loc_00ACC8B1:
    if (*(unsigned __int64 *)(a3 + *(unsigned __int64 *)(result + 40) * 1) == 0) goto loc_00ACC8C9;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a3 + *(unsigned __int64 *)(result + 40) * 1) + 24)) == 0) {
    }
    a3 = (a3) + (8);
    a4 = ((unsigned int)(a5)) - (1);
    if (condition_is_not_equal) goto loc_00ACC8B1;
loc_00ACC8D3:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 40), (unsigned int)(0x72704D45ULL), a3, a4);
loc_00ACC8E1:
    result = ExFreePoolWithTag(result, (unsigned int)(0x72704D45ULL), a3, a4);
    goto loc_00ACC984;
loc_00ACC8F3:
loc_00ACC8FA:
loc_00ACC8FF:
    v_rbp = 0;
    if ((*(unsigned int *)(result + 16)) <= ((unsigned int)((unsigned int)(0xC000000DULL)))) goto loc_00ACC932;
loc_00ACC906:
    goto loc_00ACC926;
loc_00ACC918:
    a2 = 0;
    result = EmpQueueRuleUpdateState(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + v_rbp * 8) + 72) - 8), a2, a3, a4);
loc_00ACC926:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + v_rbp * 8) + 72)) != 0) goto loc_00ACC918;
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((unsigned int)(v_rbp)) < (*(unsigned int *)(result + 16))) goto loc_00ACC906;
loc_00ACC932:
    v_rbp = 0;
    if ((*(unsigned int *)(result + 48)) <= ((unsigned int)((unsigned int)(0xC000000DULL)))) goto loc_00ACC965;
loc_00ACC939:
    goto loc_00ACC959;
loc_00ACC94B:
    a2 = 0;
    result = EmpQueueRuleUpdateState(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) + v_rbp * 8) + 48) - 8), a2, a3, a4);
loc_00ACC959:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 40) + v_rbp * 8) + 48)) != 0) goto loc_00ACC94B;
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((unsigned int)(v_rbp)) < (*(unsigned int *)(result + 48))) goto loc_00ACC939;
loc_00ACC965:
    if (v_stack_p8 != 0) {
        a1 = v_stack_p8;
        result = ObfReferenceObject(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(result) = v_stack_p8;
    *(unsigned __int64 *)(a6) = result;
    goto loc_00ACC984;
loc_00ACC97F:
loc_00ACC984:
    a2 = (a2) | (-1);
    a2 = (unsigned __int8)((a2) & (6));
    result = a6;
    if (((unsigned __int8)(a2)) == 2) {
        a1 = v_rip + 4991040;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 4991028, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
}
```

## 5. (Beta) C Style

```c
int64_t EmpProviderRegister(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, void *Arg6)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rbp;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    local_r13 = 0;
    local_rdi = 0;
    result = KeAbPreAcquire(v_rip + 4991974, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 4991974;
        Arg2 = result;
        Arg1 = v_rip + 4991974;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (Arg6 == NULL) goto loc_00ACC97F;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00ACC64F;
    if (Arg2 == 0) goto loc_00ACC97F;
loc_00ACC64F:
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_00ACC660;
    if (Arg4 == 0) goto loc_00ACC97F;
loc_00ACC660:
    result = ExAllocatePool2(256, 72, (uint32_t)(0x72704D45ULL), Arg4);
    Arg1 = 0;
    if (result != 0) goto loc_00ACC689;
    goto loc_00ACC984;
loc_00ACC689:
    *(uint64_t *)(result + 0x18) = 0;
    *(uint32_t *)(result + 0x20) = 0;
    *(uint64_t *)(result + 0x28) = 0;
    *(uint32_t *)(result + 0x30) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    *(uint32_t *)(result + 0x10) = 0;
    result = (result) + (56);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00ACC7A1;
    result = ExAllocatePool2(256, (uint32_t)(Arg3) * 8, (uint32_t)(0x72704D45ULL), Arg4);
    *(uint64_t *)(result + 0x8) = result;
    if (result != 0) goto loc_00ACC6DF;
loc_00ACC6D5:
    goto loc_00ACC840;
loc_00ACC6DF:
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(Arg3));
loc_00ACC6E9:
    if ((*(uint64_t *)(Arg2 + 0x8)) != ((uint32_t)(0xC000009AULL))) {
    }
    result = (Arg2 + 8) + (24);
    Arg1 = ((uint32_t)(Arg3)) - (1);
    if (condition_is_not_equal) goto loc_00ACC6E9;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20))) == 0) goto loc_00ACC71E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) << (5));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x72704D45ULL), Arg4);
    *(uint64_t *)(result + 0x18) = result;
    if (result == 0) goto loc_00ACC6D5;
loc_00ACC71E:
    local_r10 = 0;
loc_00ACC721:
    if (0 >= ((uint32_t)((uint32_t)(Arg3)))) goto loc_00ACC79C;
    if (*(uint64_t *)(Arg2 + local_r10 + local_r10 * 2 * 8) == 0) goto loc_00ACC83B;
    result = EmpSearchEntryDatabase(*(uint64_t *)(Arg2 + local_r10 + local_r10 * 2 * 8), (uint32_t)((uint32_t)(result)), (uint32_t)(0x72704D45ULL), Arg4);
    if (result == 0) goto loc_00ACC834;
    *(uint64_t *)(*(uint64_t *)(result + 0x8) + local_r10 * 8) = result;
    if (*(uint64_t *)(Arg2 + local_r10 + local_r10 * 2 * 8 + 0x8) == 0) goto loc_00ACC797;
    Arg1 = (0) << (5);
    Arg1 = (Arg1) + (*(uint64_t *)(result + 0x18));
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg2 + local_r10 + local_r10 * 2 * 8 + 0x8);
    *(uint64_t *)(Arg1 + 0x8) = *(uint64_t *)(Arg2 + local_r10 + local_r10 * 2 * 8 + 0x10);
    Arg1 = (Arg1) + (16);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x38 + 0x8))) != (result + 56)) goto loc_00ACC8F3;
    *(uint64_t *)(Arg1) = result + 56;
    local_r13 = (uint32_t)((local_r13) + 1);
    *(uint64_t *)(Arg1 + 0x8) = *(uint64_t *)(result + 0x38 + 0x8);
    *(uint64_t *)(*(uint64_t *)(result + 0x38 + 0x8)) = Arg1;
    *(uint64_t *)(result + 0x38 + 0x8) = Arg1;
loc_00ACC797:
    local_r10 = (uint32_t)((local_r10) + 1);
    goto loc_00ACC721;
loc_00ACC79C:
loc_00ACC7A1:
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_00ACC8FF;
    result = ExAllocatePool2(256, (uint32_t)(Arg5) * 8, (uint32_t)(0x72704D45ULL), Arg4);
    *(uint64_t *)(result + 0x28) = result;
    if (result == 0) goto loc_00ACC6D5;
    *(uint32_t *)(result + 0x30) = (uint32_t)((uint32_t)(Arg5));
    local_r10 = 0;
loc_00ACC7D3:
    if (0 >= ((uint32_t)((uint32_t)(Arg5)))) goto loc_00ACC8FA;
    if (*(uint64_t *)(Arg4 + local_r10 + local_r10 * 2 * 8 + 0x8) == 0) goto loc_00ACC83B;
    if (*(uint64_t *)(Arg4 + local_r10 + local_r10 * 2 * 8) == 0) goto loc_00ACC83B;
    result = EmpSearchCallbackDatabase(*(uint64_t *)(Arg4 + local_r10 + local_r10 * 2 * 8), (uint32_t)(Arg5) * 8, (uint32_t)(0x72704D45ULL), Arg4);
    if (result == 0) goto loc_00ACC834;
    if (*(uint64_t *)(result + 0x10) == 0) goto loc_00ACC80E;
    if ((*(uint64_t *)(result + 0x10)) != (*(uint64_t *)(Arg4 + local_r10 + local_r10 * 2 * 8 + 0x8))) goto loc_00ACC82D;
loc_00ACC80E:
    *(uint64_t *)(*(uint64_t *)(result + 0x28) + local_r10 * 8) = result;
    local_r10 = (uint32_t)((local_r10) + 1);
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(Arg4 + local_r10 + local_r10 * 2 * 8 + 0x8);
    *(uint64_t *)(result + 0x20) = *(uint64_t *)(Arg4 + local_r10 + local_r10 * 2 * 8 + 0x10);
    goto loc_00ACC7D3;
loc_00ACC82D:
    goto loc_00ACC840;
loc_00ACC834:
    goto loc_00ACC840;
loc_00ACC83B:
loc_00ACC840:
    result = *(uint64_t *)(Arg4 + local_r10 + local_r10 * 2 * 8 + 0x10);
    if (*(uint64_t *)(result + 0x8) != 0) {
        Arg2 = 0x72704D45ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(result + 0x8), Arg2, (uint32_t)(0x72704D45ULL), Arg4);
    }
    if ((*(uint64_t *)(result + 0x18)) == 0) goto loc_00ACC8A0;
    Arg2 = 0;
    if ((uint32_t)(local_r13) == 0) goto loc_00ACC892;
loc_00ACC861:
    Arg3 = (*(uint64_t *)(result + 0x18)) + (16);
    Arg1 = (0) << (5);
    Arg3 = (Arg3) + (Arg1);
    if ((*(uint64_t *)(*(uint64_t *)(Arg3) + 0x8)) != Arg3) goto loc_00ACC8F3;
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0x8))) != Arg3) goto loc_00ACC8F3;
    Arg2 = (uint32_t)((Arg2) + 1);
    *(uint64_t *)(*(uint64_t *)(Arg3 + 0x8)) = *(uint64_t *)(Arg3);
    *(uint64_t *)(*(uint64_t *)(Arg3) + 0x8) = *(uint64_t *)(Arg3 + 0x8);
    if (((uint32_t)(Arg2)) < ((uint32_t)(local_r13))) goto loc_00ACC861;
loc_00ACC892:
    result = ExFreePoolWithTag(*(uint64_t *)(result + 0x18), (uint32_t)(0x72704D45ULL), Arg3, Arg4);
loc_00ACC8A0:
    if ((*(uint64_t *)(result + 0x28)) == 0) goto loc_00ACC8E1;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_00ACC8D3;
    Arg3 = 0;
loc_00ACC8B1:
    if (*(uint64_t *)(Arg3 + *(uint64_t *)(result + 0x28) * 1) == 0) goto loc_00ACC8C9;
    if ((*(uint32_t *)(*(uint64_t *)(Arg3 + *(uint64_t *)(result + 0x28) * 1) + 0x18)) == 0) {
    }
    Arg3 = (Arg3) + (8);
    Arg4 = ((uint32_t)(Arg5)) - (1);
    if (condition_is_not_equal) goto loc_00ACC8B1;
loc_00ACC8D3:
    result = ExFreePoolWithTag(*(uint64_t *)(result + 0x28), (uint32_t)(0x72704D45ULL), Arg3, Arg4);
loc_00ACC8E1:
    result = ExFreePoolWithTag(result, (uint32_t)(0x72704D45ULL), Arg3, Arg4);
    goto loc_00ACC984;
loc_00ACC8F3:
loc_00ACC8FA:
loc_00ACC8FF:
    local_rbp = 0;
    if ((*(uint32_t *)(result + 0x10)) <= ((uint32_t)((uint32_t)(0xC000000DULL)))) goto loc_00ACC932;
loc_00ACC906:
    goto loc_00ACC926;
loc_00ACC918:
    Arg2 = 0;
    result = EmpQueueRuleUpdateState(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + local_rbp * 8) + 0x48) - 0x8), Arg2, Arg3, Arg4);
loc_00ACC926:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + local_rbp * 8) + 0x48)) != 0) goto loc_00ACC918;
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((uint32_t)(local_rbp)) < (*(uint32_t *)(result + 0x10))) goto loc_00ACC906;
loc_00ACC932:
    local_rbp = 0;
    if ((*(uint32_t *)(result + 0x30)) <= ((uint32_t)((uint32_t)(0xC000000DULL)))) goto loc_00ACC965;
loc_00ACC939:
    goto loc_00ACC959;
loc_00ACC94B:
    Arg2 = 0;
    result = EmpQueueRuleUpdateState(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x28) + local_rbp * 8) + 0x30) - 0x8), Arg2, Arg3, Arg4);
loc_00ACC959:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x28) + local_rbp * 8) + 0x30)) != 0) goto loc_00ACC94B;
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((uint32_t)(local_rbp)) < (*(uint32_t *)(result + 0x30))) goto loc_00ACC939;
loc_00ACC965:
    if (v_stack_p8 != 0) {
        Arg1 = v_stack_p8;
        result = ObfReferenceObject(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(result) = v_stack_p8;
    *(uint64_t *)(arg6) = result;
    goto loc_00ACC984;
loc_00ACC97F:
loc_00ACC984:
    Arg2 = (Arg2) | (-1);
    Arg2 = (uint8_t)((Arg2) & (6));
    result = Arg6;
    if (((uint8_t)(Arg2)) == 2) {
        Arg1 = v_rip + 4991040;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(v_rip + 4991028, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ACC5D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
