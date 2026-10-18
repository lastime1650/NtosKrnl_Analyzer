# EtwpCovSampContextGetModule

- RVA: `0x008D7FEC`–`0x008D8EAB` (길이 `3,775` bytes)
- VA: `0x00000001408D7FEC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008556C`
- 디코드: `914`개 명령, `3,775/3,775` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **41**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008D8059` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (function, `0x00443B60`)
- `0x008D812B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008D814F` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008D8172` → [EtwpCovSampContextFastFindModule](EtwpCovSampContextFastFindModule_function_008D9858.md) (function, `0x008D9858`)
- `0x008D819C` → [ProcessForExeModule](../../text/49/ProcessForExeModule_function_0049572C.md) (function, `0x0049572C`)
- `0x008D81B0` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008D81B8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008D81BD` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008D8202` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x008D820A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008D820F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008D8222` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008D8244` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008D82E8` → [EtwpFindDebugId](EtwpFindDebugId_function_008D9D58.md) (function, `0x008D9D58`)
- `0x008D8308` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008D834B` → [EtwpCovSampModuleGetName](../A5/EtwpCovSampModuleGetName_function_00A5095C.md) (function, `0x00A5095C`)
- `0x008D8392` → [EtwpCovSampCheckForSegments](../A0/EtwpCovSampCheckForSegments_function_00A0F990.md) (function, `0x00A0F990`)
- `0x008D83BE` → [EtwpCovSampCheckForSegments](../A0/EtwpCovSampCheckForSegments_function_00A0F990.md) (function, `0x00A0F990`)
- `0x008D8417` → [EtwCovSampHash](../../text/41/EtwCovSampHash_function_0041FBA0.md) (function, `0x0041FBA0`)
- `0x008D8449` → [EtwCovSampHash](../../text/41/EtwCovSampHash_function_0041FBA0.md) (function, `0x0041FBA0`)
- `0x008D8456` → [EtwCovSampHash](../../text/41/EtwCovSampHash_function_0041FBA0.md) (function, `0x0041FBA0`)
- `0x008D8468` → [EtwCovSampHash](../../text/41/EtwCovSampHash_function_0041FBA0.md) (function, `0x0041FBA0`)
- `0x008D84D1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008D84F4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008D8512` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008D884E` → [EtwpCovSampContextFastFindModule](EtwpCovSampContextFastFindModule_function_008D9858.md) (function, `0x008D9858`)
- `0x008D8877` → [ProcessForExeModule](../../text/49/ProcessForExeModule_function_0049572C.md) (function, `0x0049572C`)
- `0x008D8D1B` → [EtwpCheckDebugInfoEqual](../../text/4B/EtwpCheckDebugInfoEqual_function_004BD1B8.md) (function, `0x004BD1B8`)
- `0x008D8D3B` → [EtwpCovSampModuleNameInfoCleanup](../97/EtwpCovSampModuleNameInfoCleanup_function_0097D96C.md) (function, `0x0097D96C`)
- `0x008D8D54` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008D8D84` → [ProcessForExeModule](../../text/49/ProcessForExeModule_function_0049572C.md) (function, `0x0049572C`)
- `0x008D8DE2` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008D8DEA` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008D8DEF` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008D8DF7` → [EtwpCovSampContextPruneModules](EtwpCovSampContextPruneModules_function_008DA03C.md) (function, `0x008DA03C`)
- `0x008D8E4D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008D8E59` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008D8E5E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008D8E6F` → [EtwpCovSampModuleCleanup](../97/EtwpCovSampModuleCleanup_function_0097D91C.md) (function, `0x0097D91C`)
- `0x008D8E7C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008D8E8E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [EtwpCovSampImageNotify](EtwpCovSampImageNotify_function_008D70C0.md) at `0x008D715E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **32**
  - `0x008D8059` → [RtlImageNtHeader](../../text/44/RtlImageNtHeader_function_00443B60.md) (`PAGE` → `.text`)
  - `0x008D812B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008D814F` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008D819C` → [ProcessForExeModule](../../text/49/ProcessForExeModule_function_0049572C.md) (`PAGE` → `.text`)
  - `0x008D81B0` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008D81B8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008D81BD` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008D8202` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x008D820A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008D820F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008D8222` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008D8244` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008D8308` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008D8417` → [EtwCovSampHash](../../text/41/EtwCovSampHash_function_0041FBA0.md) (`PAGE` → `.text`)
  - `0x008D8449` → [EtwCovSampHash](../../text/41/EtwCovSampHash_function_0041FBA0.md) (`PAGE` → `.text`)
  - `0x008D8456` → [EtwCovSampHash](../../text/41/EtwCovSampHash_function_0041FBA0.md) (`PAGE` → `.text`)
  - `0x008D8468` → [EtwCovSampHash](../../text/41/EtwCovSampHash_function_0041FBA0.md) (`PAGE` → `.text`)
  - `0x008D84D1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008D84F4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008D8512` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008D8877` → [ProcessForExeModule](../../text/49/ProcessForExeModule_function_0049572C.md) (`PAGE` → `.text`)
  - `0x008D8D1B` → [EtwpCheckDebugInfoEqual](../../text/4B/EtwpCheckDebugInfoEqual_function_004BD1B8.md) (`PAGE` → `.text`)
  - `0x008D8D54` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008D8D84` → [ProcessForExeModule](../../text/49/ProcessForExeModule_function_0049572C.md) (`PAGE` → `.text`)
  - `0x008D8DE2` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008D8DEA` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008D8DEF` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008D8E4D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008D8E59` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008D8E5E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008D8E7C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008D8E8E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008D7FEC  48 8B C4                        mov rax, rsp
008D7FEF  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
008D7FF3  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
008D7FF7  48 89 48 08                     mov qword ptr [rax + 8], rcx
008D7FFB  53                              push rbx
008D7FFC  56                              push rsi
008D7FFD  57                              push rdi
008D7FFE  41 54                           push r12
008D8000  41 55                           push r13
008D8002  41 56                           push r14
008D8004  41 57                           push r15
008D8006  48 81 EC F0 00 00 00            sub rsp, 0xf0
008D800D  48 8B DA                        mov rbx, rdx
008D8010  4C 8B F9                        mov r15, rcx
008D8013  33 F6                           xor esi, esi
008D8015  44 8B E6                        mov r12d, esi
008D8018  44 8B EE                        mov r13d, esi
008D801B  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
008D8020  44 8B F6                        mov r14d, esi
008D8023  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
008D8027  4C 8B 84 24 58 01 00 00         mov r8, qword ptr [rsp + 0x158]
008D802F  49 89 30                        mov qword ptr [r8], rsi
008D8032  0F 57 C0                        xorps xmm0, xmm0
008D8035  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
008D803A  0F 11 80 60 FF FF FF            movups xmmword ptr [rax - 0xa0], xmm0
008D8041  48 8B BC 24 50 01 00 00         mov rdi, qword ptr [rsp + 0x150]
008D8049  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
008D804D  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
008D8055  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
008D8059  E8 02 BB B6 FF                  call 0x140443b60
008D805E  48 8B C8                        mov rcx, rax
008D8061  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
008D8069  48 85 C0                        test rax, rax
008D806C  75 11                           jne 0x1408d807f
008D806E  C7 44 24 20 BB 00 00 C0         mov dword ptr [rsp + 0x20], 0xc00000bb
008D8076  48 83 CB FF                     or rbx, 0xffffffffffffffff
008D807A  E9 9A 0D 00 00                  jmp 0x1408d8e19
008D807F  8B 40 58                        mov eax, dword ptr [rax + 0x58]
008D8082  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
008D8089  8B 41 08                        mov eax, dword ptr [rcx + 8]
008D808C  89 84 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], eax
008D8093  F7 47 08 00 01 00 00            test dword ptr [rdi + 8], 0x100
008D809A  74 06                           je 0x1408d80a2
008D809C  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
008D80A0  EB 1E                           jmp 0x1408d80c0
008D80A2  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008D80A6  48 85 C9                        test rcx, rcx
008D80A9  75 11                           jne 0x1408d80bc
008D80AB  C7 44 24 20 BB 00 00 C0         mov dword ptr [rsp + 0x20], 0xc00000bb
008D80B3  48 83 CB FF                     or rbx, 0xffffffffffffffff
008D80B7  E9 5D 0D 00 00                  jmp 0x1408d8e19
008D80BC  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
008D80C0  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
008D80C5  41 BD 01 00 00 00               mov r13d, 1
008D80CB  41 F7 47 08 00 04 00 00         test dword ptr [r15 + 8], 0x400
008D80D3  74 32                           je 0x1408d8107
008D80D5  48 8B 83 B0 02 00 00            mov rax, qword ptr [rbx + 0x2b0]
008D80DC  48 39 47 10                     cmp qword ptr [rdi + 0x10], rax
008D80E0  75 07                           jne 0x1408d80e9
008D80E2  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
008D80E7  EB 1E                           jmp 0x1408d8107
008D80E9  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
008D80ED  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
008D80F5  8B 40 28                        mov eax, dword ptr [rax + 0x28]
008D80F8  48 33 C8                        xor rcx, rax
008D80FB  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
008D8100  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
008D8107  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008D8110  48 83 CB FF                     or rbx, 0xffffffffffffffff
008D8114  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
008D811B  90                              nop
008D811C  49 8D BF 98 04 00 00            lea rdi, [r15 + 0x498]
008D8123  45 33 C0                        xor r8d, r8d
008D8126  33 D2                           xor edx, edx
008D8128  48 8B CF                        mov rcx, rdi
008D812B  E8 00 81 93 FF                  call 0x140210230
008D8130  48 8B C8                        mov rcx, rax
008D8133  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008D8138  8D 53 12                        lea edx, [rbx + 0x12]
008D813B  33 C0                           xor eax, eax
008D813D  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
008D8142  74 15                           je 0x1408d8159
008D8144  4C 8B CF                        mov r9, rdi
008D8147  4C 8B C1                        mov r8, rcx
008D814A  33 D2                           xor edx, edx
008D814C  48 8B CF                        mov rcx, rdi
008D814F  E8 F8 82 93 FF                  call 0x14021044c
008D8154  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
008D8159  48 85 C9                        test rcx, rcx
008D815C  74 04                           je 0x1408d8162
008D815E  44 88 69 0A                     mov byte ptr [rcx + 0xa], r13b
008D8162  4C 8B 84 24 58 01 00 00         mov r8, qword ptr [rsp + 0x158]
008D816A  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
008D816F  49 8B CF                        mov rcx, r15
008D8172  E8 E1 16 00 00                  call 0x1408d9858
008D8177  48 85 C0                        test rax, rax
008D817A  74 52                           je 0x1408d81ce
008D817C  4C 8B 84 24 58 01 00 00         mov r8, qword ptr [rsp + 0x158]
008D8184  4D 8B 00                        mov r8, qword ptr [r8]
008D8187  49 3B C0                        cmp rax, r8
008D818A  75 42                           jne 0x1408d81ce
008D818C  44 8B 4C 24 28                  mov r9d, dword ptr [rsp + 0x28]
008D8191  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
008D8199  49 8B CF                        mov rcx, r15
008D819C  E8 8B D5 BB FF                  call 0x14049572c
008D81A1  B8 11 00 00 00                  mov eax, 0x11
008D81A6  F0 48 0F B1 37                  lock cmpxchg qword ptr [rdi], rsi
008D81AB  74 08                           je 0x1408d81b5
008D81AD  48 8B CF                        mov rcx, rdi
008D81B0  E8 8B B2 98 FF                  call 0x140263440
008D81B5  48 8B CF                        mov rcx, rdi
008D81B8  E8 43 94 A0 FF                  call 0x1402e1600
008D81BD  E8 EE 56 98 FF                  call 0x14025d8b0
008D81C2  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
008D81C6  4C 8B EE                        mov r13, rsi
008D81C9  E9 4B 0C 00 00                  jmp 0x1408d8e19
008D81CE  41 8B 87 AC 04 00 00            mov eax, dword ptr [r15 + 0x4ac]
008D81D5  C1 E8 05                        shr eax, 5
008D81D8  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
008D81DC  41 8B 8F A8 04 00 00            mov ecx, dword ptr [r15 + 0x4a8]
008D81E3  41 8B 87 B8 04 00 00            mov eax, dword ptr [r15 + 0x4b8]
008D81EA  3B C8                           cmp ecx, eax
008D81EC  0F 46 C8                        cmovbe ecx, eax
008D81EF  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
008D81F3  B8 11 00 00 00                  mov eax, 0x11
008D81F8  F0 48 0F B1 37                  lock cmpxchg qword ptr [rdi], rsi
008D81FD  74 08                           je 0x1408d8207
008D81FF  48 8B CF                        mov rcx, rdi
008D8202  E8 39 B2 98 FF                  call 0x140263440
008D8207  48 8B CF                        mov rcx, rdi
008D820A  E8 F1 93 A0 FF                  call 0x1402e1600
008D820F  E8 9C 56 98 FF                  call 0x14025d8b0
008D8214  BA B0 00 00 00                  mov edx, 0xb0
008D8219  8D 4A 50                        lea ecx, [rdx + 0x50]
008D821C  41 B8 45 74 77 56               mov r8d, 0x56777445
008D8222  E8 C9 9E 2A 00                  call 0x140b820f0
008D8227  4C 8B F0                        mov r14, rax
008D822A  48 85 C0                        test rax, rax
008D822D  75 0A                           jne 0x1408d8239
008D822F  C7 44 24 20 9A 00 00 C0         mov dword ptr [rsp + 0x20], 0xc000009a
008D8237  EB 8D                           jmp 0x1408d81c6
008D8239  33 D2                           xor edx, edx
008D823B  41 B8 B0 00 00 00               mov r8d, 0xb0
008D8241  49 8B CE                        mov rcx, r14
008D8244  E8 F7 E9 DE FF                  call 0x1406c6c40
008D8249  49 8D 46 48                     lea rax, [r14 + 0x48]
008D824D  48 89 40 08                     mov qword ptr [rax + 8], rax
008D8251  48 89 00                        mov qword ptr [rax], rax
008D8254  49 8D 46 58                     lea rax, [r14 + 0x58]
008D8258  48 89 40 08                     mov qword ptr [rax + 8], rax
008D825C  48 89 00                        mov qword ptr [rax], rax
008D825F  49 89 36                        mov qword ptr [r14], rsi
008D8262  49 89 76 10                     mov qword ptr [r14 + 0x10], rsi
008D8266  4D 89 6E 40                     mov qword ptr [r14 + 0x40], r13
008D826A  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
008D826F  49 89 46 08                     mov qword ptr [r14 + 8], rax
008D8273  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
008D827B  49 89 56 28                     mov qword ptr [r14 + 0x28], rdx
008D827F  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
008D8286  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
008D828A  8B 84 24 8C 00 00 00            mov eax, dword ptr [rsp + 0x8c]
008D8291  41 89 46 24                     mov dword ptr [r14 + 0x24], eax
008D8295  41 8B 46 78                     mov eax, dword ptr [r14 + 0x78]
008D8299  4C 8B 94 24 50 01 00 00         mov r10, qword ptr [rsp + 0x150]
008D82A1  41 8B 4A 08                     mov ecx, dword ptr [r10 + 8]
008D82A5  C1 E1 09                        shl ecx, 9
008D82A8  33 C8                           xor ecx, eax
008D82AA  81 E1 00 00 02 00               and ecx, 0x20000
008D82B0  33 C8                           xor ecx, eax
008D82B2  41 89 4E 78                     mov dword ptr [r14 + 0x78], ecx
008D82B6  48 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rsi
008D82BE  48 89 B4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rsi
008D82C6  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
008D82CA  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
008D82D2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008D82D7  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
008D82DC  4D 8D 4E 38                     lea r9, [r14 + 0x38]
008D82E0  4D 8D 46 30                     lea r8, [r14 + 0x30]
008D82E4  49 8B 4A 10                     mov rcx, qword ptr [r10 + 0x10]
008D82E8  E8 6B 1A 00 00                  call 0x1408d9d58
008D82ED  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008D82F1  85 C0                           test eax, eax
008D82F3  78 20                           js 0x1408d8315
008D82F5  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
008D82F9  41 81 7E 38 00 04 00 00         cmp dword ptr [r14 + 0x38], 0x400
008D8301  76 25                           jbe 0x1408d8328
008D8303  33 D2                           xor edx, edx
008D8305  48 8B C8                        mov rcx, rax
008D8308  E8 63 A5 2A 00                  call 0x140b82870
008D830D  49 89 76 30                     mov qword ptr [r14 + 0x30], rsi
008D8311  41 89 76 38                     mov dword ptr [r14 + 0x38], esi
008D8315  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
008D8319  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
008D831D  85 C0                           test eax, eax
008D831F  75 17                           jne 0x1408d8338
008D8321  8B CE                           mov ecx, esi
008D8323  E9 A6 00 00 00                  jmp 0x1408d83ce
008D8328  8B 48 14                        mov ecx, dword ptr [rax + 0x14]
008D832B  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
008D832F  48 83 C0 04                     add rax, 4
008D8333  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008D8338  4C 8B 84 24 48 01 00 00         mov r8, qword ptr [rsp + 0x148]
008D8340  48 8B 94 24 50 01 00 00         mov rdx, qword ptr [rsp + 0x150]
008D8348  49 8B CE                        mov rcx, r14
008D834B  E8 0C 86 17 00                  call 0x140a5095c
008D8350  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008D8354  85 C0                           test eax, eax
008D8356  0F 88 6A FE FF FF               js 0x1408d81c6
008D835C  49 8B 46 70                     mov rax, qword ptr [r14 + 0x70]
008D8360  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
008D8368  41 8B 46 78                     mov eax, dword ptr [r14 + 0x78]
008D836C  0F B7 C8                        movzx ecx, ax
008D836F  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
008D8377  45 8B 87 58 06 00 00            mov r8d, dword ptr [r15 + 0x658]
008D837E  45 85 C0                        test r8d, r8d
008D8381  74 18                           je 0x1408d839b
008D8383  49 8D 97 18 05 00 00            lea rdx, [r15 + 0x518]
008D838A  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
008D8392  E8 F9 75 13 00                  call 0x140a0f990
008D8397  8B C8                           mov ecx, eax
008D8399  EB 04                           jmp 0x1408d839f
008D839B  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
008D839F  85 C9                           test ecx, ecx
008D83A1  74 27                           je 0x1408d83ca
008D83A3  45 8B 87 5C 06 00 00            mov r8d, dword ptr [r15 + 0x65c]
008D83AA  45 85 C0                        test r8d, r8d
008D83AD  74 1B                           je 0x1408d83ca
008D83AF  49 8D 97 B8 05 00 00            lea rdx, [r15 + 0x5b8]
008D83B6  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
008D83BE  E8 CD 75 13 00                  call 0x140a0f990
008D83C3  8B CE                           mov ecx, esi
008D83C5  85 C0                           test eax, eax
008D83C7  0F 94 C1                        sete cl
008D83CA  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
008D83CE  85 C9                           test ecx, ecx
008D83D0  75 08                           jne 0x1408d83da
008D83D2  85 C0                           test eax, eax
008D83D4  0F 84 C6 00 00 00               je 0x1408d84a0
008D83DA  41 8B 46 78                     mov eax, dword ptr [r14 + 0x78]
008D83DE  C1 E1 10                        shl ecx, 0x10
008D83E1  33 C8                           xor ecx, eax
008D83E3  81 E1 00 00 01 00               and ecx, 0x10000
008D83E9  33 C8                           xor ecx, eax
008D83EB  41 89 4E 78                     mov dword ptr [r14 + 0x78], ecx
008D83EF  41 8B 7E 28                     mov edi, dword ptr [r14 + 0x28]
008D83F3  41 8B 56 20                     mov edx, dword ptr [r14 + 0x20]
008D83F7  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
008D83FB  41 8B 4F 0C                     mov ecx, dword ptr [r15 + 0xc]
008D83FF  89 84 24 50 01 00 00            mov dword ptr [rsp + 0x150], eax
008D8406  89 94 24 54 01 00 00            mov dword ptr [rsp + 0x154], edx
008D840D  8B D1                           mov edx, ecx
008D840F  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
008D8417  E8 84 77 B4 FF                  call 0x14041fba0
008D841C  89 BC 24 50 01 00 00            mov dword ptr [rsp + 0x150], edi
008D8423  8B 4C 24 60                     mov ecx, dword ptr [rsp + 0x60]
008D8427  89 8C 24 54 01 00 00            mov dword ptr [rsp + 0x154], ecx
008D842E  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
008D8433  0F 10 01                        movups xmm0, xmmword ptr [rcx]
008D8436  0F 11 84 24 D8 00 00 00         movups xmmword ptr [rsp + 0xd8], xmm0
008D843E  48 8B D0                        mov rdx, rax
008D8441  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
008D8449  E8 52 77 B4 FF                  call 0x14041fba0
008D844E  48 8B D0                        mov rdx, rax
008D8451  66 48 0F 7E C1                  movq rcx, xmm0
008D8456  E8 45 77 B4 FF                  call 0x14041fba0
008D845B  48 8B D0                        mov rdx, rax
008D845E  66 0F 73 D8 08                  psrldq xmm0, 8
008D8463  66 48 0F 7E C1                  movq rcx, xmm0
008D8468  E8 33 77 B4 FF                  call 0x14041fba0
008D846D  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
008D8475  48 C1 E8 20                     shr rax, 0x20
008D8479  33 84 24 50 01 00 00            xor eax, dword ptr [rsp + 0x150]
008D8480  41 0F 44 C5                     cmove eax, r13d
008D8484  39 74 24 28                     cmp dword ptr [rsp + 0x28], esi
008D8488  75 0B                           jne 0x1408d8495
008D848A  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
008D8492  33 41 28                        xor eax, dword ptr [rcx + 0x28]
008D8495  41 89 46 7C                     mov dword ptr [r14 + 0x7c], eax
008D8499  49 8D BF 98 04 00 00            lea rdi, [r15 + 0x498]
008D84A0  8B 54 24 70                     mov edx, dword ptr [rsp + 0x70]
008D84A4  03 D2                           add edx, edx
008D84A6  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
008D84AA  FF C0                           inc eax
008D84AC  3B C2                           cmp eax, edx
008D84AE  76 2B                           jbe 0x1408d84db
008D84B0  44 8B E2                        mov r12d, edx
008D84B3  B8 80 00 00 00                  mov eax, 0x80
008D84B8  85 D2                           test edx, edx
008D84BA  44 0F 44 E0                     cmove r12d, eax
008D84BE  43 8D 14 24                     lea edx, [r12 + r12]
008D84C2  48 C1 E2 03                     shl rdx, 3
008D84C6  B9 00 01 00 00                  mov ecx, 0x100
008D84CB  41 B8 45 74 77 56               mov r8d, 0x56777445
008D84D1  E8 1A 9C 2A 00                  call 0x140b820f0
008D84D6  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008D84DB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008D84E4  66 01 99 E4 01 00 00            add word ptr [rcx + 0x1e4], bx
008D84EB  90                              nop
008D84EC  45 33 C0                        xor r8d, r8d
008D84EF  33 D2                           xor edx, edx
008D84F1  48 8B CF                        mov rcx, rdi
008D84F4  E8 37 7D 93 FF                  call 0x140210230
008D84F9  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
008D8501  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
008D8507  73 16                           jae 0x1408d851f
008D8509  4C 8B C7                        mov r8, rdi
008D850C  48 8B D0                        mov rdx, rax
008D850F  48 8B CF                        mov rcx, rdi
008D8512  E8 79 77 93 FF                  call 0x14020fc90
008D8517  48 8B 84 24 50 01 00 00         mov rax, qword ptr [rsp + 0x150]
008D851F  48 85 C0                        test rax, rax
008D8522  74 04                           je 0x1408d8528
008D8524  44 88 68 0A                     mov byte ptr [rax + 0xa], r13b
008D8528  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008D8531  49 89 87 A0 04 00 00            mov qword ptr [r15 + 0x4a0], rax
008D8538  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008D853D  48 85 FF                        test rdi, rdi
008D8540  0F 84 D3 02 00 00               je 0x1408d8819
008D8546  41 8B 87 AC 04 00 00            mov eax, dword ptr [r15 + 0x4ac]
008D854D  C1 E8 05                        shr eax, 5
008D8550  44 3B E0                        cmp r12d, eax
008D8553  0F 86 C0 02 00 00               jbe 0x1408d8819
008D8559  41 8B C4                        mov eax, r12d
008D855C  4C 8D 0C C7                     lea r9, [rdi + rax*8]
008D8560  45 8B C4                        mov r8d, r12d
008D8563  41 8D 44 24 FF                  lea eax, [r12 - 1]
008D8568  41 23 C4                        and eax, r12d
008D856B  89 84 24 50 01 00 00            mov dword ptr [rsp + 0x150], eax
008D8572  74 18                           je 0x1408d858c
008D8574  41 8B C4                        mov eax, r12d
008D8577  83 C9 FF                        or ecx, 0xffffffff
008D857A  45 85 E4                        test r12d, r12d
008D857D  74 07                           je 0x1408d8586
008D857F  41 03 CD                        add ecx, r13d
008D8582  D1 E8                           shr eax, 1
008D8584  75 F9                           jne 0x1408d857f
008D8586  45 8B C5                        mov r8d, r13d
008D8589  41 D3 E0                        shl r8d, cl
008D858C  B8 00 00 00 04                  mov eax, 0x4000000
008D8591  44 3B C0                        cmp r8d, eax
008D8594  44 0F 47 C0                     cmova r8d, eax
008D8598  4D 8D 9F B8 04 00 00            lea r11, [r15 + 0x4b8]
008D859F  49 8B C3                        mov rax, r11
008D85A2  49 0B C5                        or rax, r13
008D85A5  41 8B C8                        mov ecx, r8d
008D85A8  4B 8D 14 C1                     lea rdx, [r9 + r8*8]
008D85AC  4C 3B CA                        cmp r9, rdx
008D85AF  48 0F 47 CE                     cmova rcx, rsi
008D85B3  48 85 C9                        test rcx, rcx
008D85B6  74 0B                           je 0x1408d85c3
008D85B8  49 8B F9                        mov rdi, r9
008D85BB  F3 48 AB                        rep stosq qword ptr [rdi], rax
008D85BE  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008D85C3  41 8B 53 04                     mov edx, dword ptr [r11 + 4]
008D85C7  8B CA                           mov ecx, edx
008D85C9  83 E1 1F                        and ecx, 0x1f
008D85CC  48 8B C3                        mov rax, rbx
008D85CF  48 D3 E0                        shl rax, cl
008D85D2  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008D85D7  44 8B D6                        mov r10d, esi
008D85DA  F7 C2 E0 FF FF FF               test edx, 0xffffffe0
008D85E0  0F 86 D2 00 00 00               jbe 0x1408d86b8
008D85E6  49 8B 43 08                     mov rax, qword ptr [r11 + 8]
008D85EA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008D85EF  41 8B D2                        mov edx, r10d
008D85F2  48 8B 0C D0                     mov rcx, qword ptr [rax + rdx*8]
008D85F6  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
008D85FB  41 84 CD                        test r13b, cl
008D85FE  0F 85 9F 00 00 00               jne 0x1408d86a3
008D8604  48 8B 01                        mov rax, qword ptr [rcx]
008D8607  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
008D860C  48 89 04 D7                     mov qword ptr [rdi + rdx*8], rax
008D8610  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
008D8614  48 23 44 24 68                  and rax, qword ptr [rsp + 0x68]
008D8619  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008D861E  0F B6 C0                        movzx eax, al
008D8621  48 05 CB 5D B1 00               add rax, 0xb15dcb
008D8627  48 6B C8 25                     imul rcx, rax, 0x25
008D862B  0F B6 44 24 51                  movzx eax, byte ptr [rsp + 0x51]
008D8630  48 03 C8                        add rcx, rax
008D8633  48 6B D1 25                     imul rdx, rcx, 0x25
008D8637  0F B6 44 24 52                  movzx eax, byte ptr [rsp + 0x52]
008D863C  48 03 D0                        add rdx, rax
008D863F  48 6B CA 25                     imul rcx, rdx, 0x25
008D8643  0F B6 44 24 53                  movzx eax, byte ptr [rsp + 0x53]
008D8648  48 03 C8                        add rcx, rax
008D864B  48 6B D1 25                     imul rdx, rcx, 0x25
008D864F  0F B6 44 24 54                  movzx eax, byte ptr [rsp + 0x54]
008D8654  48 03 D0                        add rdx, rax
008D8657  48 6B CA 25                     imul rcx, rdx, 0x25
008D865B  0F B6 44 24 55                  movzx eax, byte ptr [rsp + 0x55]
008D8660  48 03 C8                        add rcx, rax
008D8663  48 6B D1 25                     imul rdx, rcx, 0x25
008D8667  0F B6 44 24 56                  movzx eax, byte ptr [rsp + 0x56]
008D866C  48 03 D0                        add rdx, rax
008D866F  48 6B D2 25                     imul rdx, rdx, 0x25
008D8673  0F B6 44 24 57                  movzx eax, byte ptr [rsp + 0x57]
008D8678  48 03 C2                        add rax, rdx
008D867B  41 8D 48 FF                     lea ecx, [r8 - 1]
008D867F  8B C0                           mov eax, eax
008D8681  48 23 C8                        and rcx, rax
008D8684  49 8B 04 C9                     mov rax, qword ptr [r9 + rcx*8]
008D8688  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
008D868D  48 89 02                        mov qword ptr [rdx], rax
008D8690  49 89 14 C9                     mov qword ptr [r9 + rcx*8], rdx
008D8694  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008D8699  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
008D869E  E9 4C FF FF FF                  jmp 0x1408d85ef
008D86A3  45 03 D5                        add r10d, r13d
008D86A6  41 8B 53 04                     mov edx, dword ptr [r11 + 4]
008D86AA  8B C2                           mov eax, edx
008D86AC  C1 E8 05                        shr eax, 5
008D86AF  44 3B D0                        cmp r10d, eax
008D86B2  0F 82 2E FF FF FF               jb 0x1408d85e6
008D86B8  4D 89 4B 08                     mov qword ptr [r11 + 8], r9
008D86BC  41 C1 E0 05                     shl r8d, 5
008D86C0  83 E2 1F                        and edx, 0x1f
008D86C3  44 0B C2                        or r8d, edx
008D86C6  45 89 43 04                     mov dword ptr [r11 + 4], r8d
008D86CA  4D 8D 87 A8 04 00 00            lea r8, [r15 + 0x4a8]
008D86D1  39 B4 24 50 01 00 00            cmp dword ptr [rsp + 0x150], esi
008D86D8  74 16                           je 0x1408d86f0
008D86DA  83 C9 FF                        or ecx, 0xffffffff
008D86DD  45 85 E4                        test r12d, r12d
008D86E0  74 08                           je 0x1408d86ea
008D86E2  41 03 CD                        add ecx, r13d
008D86E5  41 D1 EC                        shr r12d, 1
008D86E8  75 F8                           jne 0x1408d86e2
008D86EA  45 8B E5                        mov r12d, r13d
008D86ED  41 D3 E4                        shl r12d, cl
008D86F0  B8 00 00 00 04                  mov eax, 0x4000000
008D86F5  44 3B E0                        cmp r12d, eax
008D86F8  44 0F 47 E0                     cmova r12d, eax
008D86FC  49 8B C0                        mov rax, r8
008D86FF  49 0B C5                        or rax, r13
008D8702  41 8B CC                        mov ecx, r12d
008D8705  4A 8D 14 E7                     lea rdx, [rdi + r12*8]
008D8709  48 3B FA                        cmp rdi, rdx
008D870C  48 0F 47 CE                     cmova rcx, rsi
008D8710  48 85 C9                        test rcx, rcx
008D8713  74 08                           je 0x1408d871d
008D8715  F3 48 AB                        rep stosq qword ptr [rdi], rax
008D8718  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
008D871D  41 8B 50 04                     mov edx, dword ptr [r8 + 4]
008D8721  8B CA                           mov ecx, edx
008D8723  83 E1 1F                        and ecx, 0x1f
008D8726  4C 8B DB                        mov r11, rbx
008D8729  49 D3 E3                        shl r11, cl
008D872C  44 8B CE                        mov r9d, esi
008D872F  F7 C2 E0 FF FF FF               test edx, 0xffffffe0
008D8735  0F 86 C3 00 00 00               jbe 0x1408d87fe
008D873B  49 8B 50 08                     mov rdx, qword ptr [r8 + 8]
008D873F  48 89 94 24 50 01 00 00         mov qword ptr [rsp + 0x150], rdx
008D8747  41 8B C9                        mov ecx, r9d
008D874A  4C 8B 14 CA                     mov r10, qword ptr [rdx + rcx*8]
008D874E  45 84 D5                        test r13b, r10b
008D8751  0F 85 92 00 00 00               jne 0x1408d87e9
008D8757  49 8B 02                        mov rax, qword ptr [r10]
008D875A  48 89 04 CA                     mov qword ptr [rdx + rcx*8], rax
008D875E  49 8B 42 08                     mov rax, qword ptr [r10 + 8]
008D8762  49 23 C3                        and rax, r11
008D8765  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008D876A  0F B6 C0                        movzx eax, al
008D876D  48 05 CB 5D B1 00               add rax, 0xb15dcb
008D8773  48 6B C8 25                     imul rcx, rax, 0x25
008D8777  0F B6 44 24 59                  movzx eax, byte ptr [rsp + 0x59]
008D877C  48 03 C8                        add rcx, rax
008D877F  48 6B D1 25                     imul rdx, rcx, 0x25
008D8783  0F B6 44 24 5A                  movzx eax, byte ptr [rsp + 0x5a]
008D8788  48 03 D0                        add rdx, rax
008D878B  48 6B CA 25                     imul rcx, rdx, 0x25
008D878F  0F B6 44 24 5B                  movzx eax, byte ptr [rsp + 0x5b]
008D8794  48 03 C8                        add rcx, rax
008D8797  48 6B D1 25                     imul rdx, rcx, 0x25
008D879B  0F B6 44 24 5C                  movzx eax, byte ptr [rsp + 0x5c]
008D87A0  48 03 D0                        add rdx, rax
008D87A3  48 6B CA 25                     imul rcx, rdx, 0x25
008D87A7  0F B6 44 24 5D                  movzx eax, byte ptr [rsp + 0x5d]
008D87AC  48 03 C8                        add rcx, rax
008D87AF  48 6B D1 25                     imul rdx, rcx, 0x25
008D87B3  0F B6 44 24 5E                  movzx eax, byte ptr [rsp + 0x5e]
008D87B8  48 03 D0                        add rdx, rax
008D87BB  48 6B D2 25                     imul rdx, rdx, 0x25
008D87BF  0F B6 44 24 5F                  movzx eax, byte ptr [rsp + 0x5f]
008D87C4  48 03 C2                        add rax, rdx
008D87C7  41 8D 4C 24 FF                  lea ecx, [r12 - 1]
008D87CC  8B C0                           mov eax, eax
008D87CE  48 23 C8                        and rcx, rax
008D87D1  48 8B 04 CF                     mov rax, qword ptr [rdi + rcx*8]
008D87D5  49 89 02                        mov qword ptr [r10], rax
008D87D8  4C 89 14 CF                     mov qword ptr [rdi + rcx*8], r10
008D87DC  48 8B 94 24 50 01 00 00         mov rdx, qword ptr [rsp + 0x150]
008D87E4  E9 5E FF FF FF                  jmp 0x1408d8747
008D87E9  45 03 CD                        add r9d, r13d
008D87EC  41 8B 50 04                     mov edx, dword ptr [r8 + 4]
008D87F0  8B C2                           mov eax, edx
008D87F2  C1 E8 05                        shr eax, 5
008D87F5  44 3B C8                        cmp r9d, eax
008D87F8  0F 82 3D FF FF FF               jb 0x1408d873b
008D87FE  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
008D8802  49 89 78 08                     mov qword ptr [r8 + 8], rdi
008D8806  83 E2 1F                        and edx, 0x1f
008D8809  41 C1 E4 05                     shl r12d, 5
008D880D  41 0B D4                        or edx, r12d
008D8810  41 89 50 04                     mov dword ptr [r8 + 4], edx
008D8814  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008D8819  41 BC CB 5D B1 00               mov r12d, 0xb15dcb
008D881F  41 83 BF AC 04 00 00 20         cmp dword ptr [r15 + 0x4ac], 0x20
008D8827  73 12                           jae 0x1408d883b
008D8829  C7 44 24 20 9A 00 00 C0         mov dword ptr [rsp + 0x20], 0xc000009a
008D8831  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
008D8836  E9 DE 05 00 00                  jmp 0x1408d8e19
008D883B  48 8B BC 24 58 01 00 00         mov rdi, qword ptr [rsp + 0x158]
008D8843  4C 8B C7                        mov r8, rdi
008D8846  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
008D884B  49 8B CF                        mov rcx, r15
008D884E  E8 05 10 00 00                  call 0x1408d9858
008D8853  4C 8B C8                        mov r9, rax
008D8856  48 85 C0                        test rax, rax
008D8859  0F 84 00 02 00 00               je 0x1408d8a5f
008D885F  4C 8B 07                        mov r8, qword ptr [rdi]
008D8862  49 3B C0                        cmp rax, r8
008D8865  75 1B                           jne 0x1408d8882
008D8867  44 8B 4C 24 28                  mov r9d, dword ptr [rsp + 0x28]
008D886C  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
008D8874  49 8B CF                        mov rcx, r15
008D8877  E8 B0 CE BB FF                  call 0x14049572c
008D887C  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
008D8880  EB AF                           jmp 0x1408d8831
008D8882  0F BA 68 78 12                  bts dword ptr [rax + 0x78], 0x12
008D8887  41 8B BF AC 04 00 00            mov edi, dword ptr [r15 + 0x4ac]
008D888E  8B CF                           mov ecx, edi
008D8890  83 E1 1F                        and ecx, 0x1f
008D8893  48 8B C3                        mov rax, rbx
008D8896  48 D3 E0                        shl rax, cl
008D8899  49 23 41 08                     and rax, qword ptr [r9 + 8]
008D889D  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
008D88A5  C1 EF 05                        shr edi, 5
008D88A8  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
008D88B0  0F B6 C0                        movzx eax, al
008D88B3  49 03 C4                        add rax, r12
008D88B6  48 6B C8 25                     imul rcx, rax, 0x25
008D88BA  0F B6 84 24 51 01 00 00         movzx eax, byte ptr [rsp + 0x151]
008D88C2  48 03 C8                        add rcx, rax
008D88C5  48 6B D1 25                     imul rdx, rcx, 0x25
008D88C9  0F B6 84 24 52 01 00 00         movzx eax, byte ptr [rsp + 0x152]
008D88D1  48 03 D0                        add rdx, rax
008D88D4  48 6B CA 25                     imul rcx, rdx, 0x25
008D88D8  0F B6 84 24 53 01 00 00         movzx eax, byte ptr [rsp + 0x153]
008D88E0  48 03 C8                        add rcx, rax
008D88E3  48 6B D1 25                     imul rdx, rcx, 0x25
008D88E7  0F B6 84 24 54 01 00 00         movzx eax, byte ptr [rsp + 0x154]
008D88EF  48 03 D0                        add rdx, rax
008D88F2  48 6B CA 25                     imul rcx, rdx, 0x25
008D88F6  0F B6 84 24 55 01 00 00         movzx eax, byte ptr [rsp + 0x155]
008D88FE  48 03 C8                        add rcx, rax
008D8901  48 6B D1 25                     imul rdx, rcx, 0x25
008D8905  0F B6 84 24 56 01 00 00         movzx eax, byte ptr [rsp + 0x156]
008D890D  48 03 D0                        add rdx, rax
008D8910  48 6B D2 25                     imul rdx, rdx, 0x25
008D8914  0F B6 84 24 57 01 00 00         movzx eax, byte ptr [rsp + 0x157]
008D891C  48 03 C2                        add rax, rdx
008D891F  8D 4F FF                        lea ecx, [rdi - 1]
008D8922  8B C0                           mov eax, eax
008D8924  48 23 C8                        and rcx, rax
008D8927  49 8B 87 B0 04 00 00            mov rax, qword ptr [r15 + 0x4b0]
008D892E  48 8D 14 C8                     lea rdx, [rax + rcx*8]
008D8932  49 8B 01                        mov rax, qword ptr [r9]
008D8935  49 BB 02 00 00 00 00 00 00 80   movabs r11, 0x8000000000000002
008D893F  49 23 C3                        and rax, r11
008D8942  49 3B C3                        cmp rax, r11
008D8945  75 03                           jne 0x1408d894a
008D8947  48 8B 06                        mov rax, qword ptr [rsi]
008D894A  48 8B 02                        mov rax, qword ptr [rdx]
008D894D  41 84 C5                        test r13b, al
008D8950  75 19                           jne 0x1408d896b
008D8952  49 3B C1                        cmp rax, r9
008D8955  74 05                           je 0x1408d895c
008D8957  48 8B D0                        mov rdx, rax
008D895A  EB EE                           jmp 0x1408d894a
008D895C  49 8B 01                        mov rax, qword ptr [r9]
008D895F  48 89 02                        mov qword ptr [rdx], rax
008D8962  41 FF 8F A8 04 00 00            dec dword ptr [r15 + 0x4a8]
008D8969  EB 03                           jmp 0x1408d896e
008D896B  48 8B 06                        mov rax, qword ptr [rsi]
008D896E  49 89 31                        mov qword ptr [r9], rsi
008D8971  4D 8D 41 10                     lea r8, [r9 + 0x10]
008D8975  4D 8B 10                        mov r10, qword ptr [r8]
008D8978  4D 85 D2                        test r10, r10
008D897B  0F 84 DE 00 00 00               je 0x1408d8a5f
008D8981  41 8B BF BC 04 00 00            mov edi, dword ptr [r15 + 0x4bc]
008D8988  8B CF                           mov ecx, edi
008D898A  83 E1 1F                        and ecx, 0x1f
008D898D  48 8B C3                        mov rax, rbx
008D8990  48 D3 E0                        shl rax, cl
008D8993  49 23 40 08                     and rax, qword ptr [r8 + 8]
008D8997  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
008D899F  C1 EF 05                        shr edi, 5
008D89A2  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
008D89AA  0F B6 C0                        movzx eax, al
008D89AD  49 03 C4                        add rax, r12
008D89B0  48 6B C8 25                     imul rcx, rax, 0x25
008D89B4  0F B6 84 24 51 01 00 00         movzx eax, byte ptr [rsp + 0x151]
008D89BC  48 03 C8                        add rcx, rax
008D89BF  48 6B D1 25                     imul rdx, rcx, 0x25
008D89C3  0F B6 84 24 52 01 00 00         movzx eax, byte ptr [rsp + 0x152]
008D89CB  48 03 D0                        add rdx, rax
008D89CE  48 6B CA 25                     imul rcx, rdx, 0x25
008D89D2  0F B6 84 24 53 01 00 00         movzx eax, byte ptr [rsp + 0x153]
008D89DA  48 03 C8                        add rcx, rax
008D89DD  48 6B D1 25                     imul rdx, rcx, 0x25
008D89E1  0F B6 84 24 54 01 00 00         movzx eax, byte ptr [rsp + 0x154]
008D89E9  48 03 D0                        add rdx, rax
008D89EC  48 6B CA 25                     imul rcx, rdx, 0x25
008D89F0  0F B6 84 24 55 01 00 00         movzx eax, byte ptr [rsp + 0x155]
008D89F8  48 03 C8                        add rcx, rax
008D89FB  48 6B D1 25                     imul rdx, rcx, 0x25
008D89FF  0F B6 84 24 56 01 00 00         movzx eax, byte ptr [rsp + 0x156]
008D8A07  48 03 D0                        add rdx, rax
008D8A0A  48 6B D2 25                     imul rdx, rdx, 0x25
008D8A0E  0F B6 84 24 57 01 00 00         movzx eax, byte ptr [rsp + 0x157]
008D8A16  48 03 C2                        add rax, rdx
008D8A19  8D 4F FF                        lea ecx, [rdi - 1]
008D8A1C  8B C0                           mov eax, eax
008D8A1E  48 23 C8                        and rcx, rax
008D8A21  49 8B 87 C0 04 00 00            mov rax, qword ptr [r15 + 0x4c0]
008D8A28  48 8D 14 C8                     lea rdx, [rax + rcx*8]
008D8A2C  4D 23 D3                        and r10, r11
008D8A2F  4D 3B D3                        cmp r10, r11
008D8A32  75 03                           jne 0x1408d8a37
008D8A34  48 8B 06                        mov rax, qword ptr [rsi]
008D8A37  48 8B 02                        mov rax, qword ptr [rdx]
008D8A3A  41 84 C5                        test r13b, al
008D8A3D  75 19                           jne 0x1408d8a58
008D8A3F  49 3B C0                        cmp rax, r8
008D8A42  74 05                           je 0x1408d8a49
008D8A44  48 8B D0                        mov rdx, rax
008D8A47  EB EE                           jmp 0x1408d8a37
008D8A49  49 8B 00                        mov rax, qword ptr [r8]
008D8A4C  48 89 02                        mov qword ptr [rdx], rax
008D8A4F  41 FF 8F B8 04 00 00            dec dword ptr [r15 + 0x4b8]
008D8A56  EB 03                           jmp 0x1408d8a5b
008D8A58  48 8B 06                        mov rax, qword ptr [rsi]
008D8A5B  49 89 71 10                     mov qword ptr [r9 + 0x10], rsi
008D8A5F  41 8B 4E 78                     mov ecx, dword ptr [r14 + 0x78]
008D8A63  0F BA F1 14                     btr ecx, 0x14
008D8A67  44 8B 54 24 28                  mov r10d, dword ptr [rsp + 0x28]
008D8A6C  41 8B C2                        mov eax, r10d
008D8A6F  C1 E0 14                        shl eax, 0x14
008D8A72  0B C8                           or ecx, eax
008D8A74  41 89 4E 78                     mov dword ptr [r14 + 0x78], ecx
008D8A78  41 8B 87 60 06 00 00            mov eax, dword ptr [r15 + 0x660]
008D8A7F  41 89 86 80 00 00 00            mov dword ptr [r14 + 0x80], eax
008D8A86  45 01 AF 60 06 00 00            add dword ptr [r15 + 0x660], r13d
008D8A8D  41 8B 8F AC 04 00 00            mov ecx, dword ptr [r15 + 0x4ac]
008D8A94  8B F9                           mov edi, ecx
008D8A96  C1 EF 05                        shr edi, 5
008D8A99  83 E1 1F                        and ecx, 0x1f
008D8A9C  48 8B C3                        mov rax, rbx
008D8A9F  48 D3 E0                        shl rax, cl
008D8AA2  49 23 46 08                     and rax, qword ptr [r14 + 8]
008D8AA6  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008D8AAB  0F B6 C0                        movzx eax, al
008D8AAE  49 03 C4                        add rax, r12
008D8AB1  48 6B C8 25                     imul rcx, rax, 0x25
008D8AB5  0F B6 44 24 49                  movzx eax, byte ptr [rsp + 0x49]
008D8ABA  48 03 C8                        add rcx, rax
008D8ABD  48 6B D1 25                     imul rdx, rcx, 0x25
008D8AC1  0F B6 44 24 4A                  movzx eax, byte ptr [rsp + 0x4a]
008D8AC6  48 03 D0                        add rdx, rax
008D8AC9  48 6B CA 25                     imul rcx, rdx, 0x25
008D8ACD  0F B6 44 24 4B                  movzx eax, byte ptr [rsp + 0x4b]
008D8AD2  48 03 C8                        add rcx, rax
008D8AD5  48 6B D1 25                     imul rdx, rcx, 0x25
008D8AD9  0F B6 44 24 4C                  movzx eax, byte ptr [rsp + 0x4c]
008D8ADE  48 03 D0                        add rdx, rax
008D8AE1  48 6B CA 25                     imul rcx, rdx, 0x25
008D8AE5  0F B6 44 24 4D                  movzx eax, byte ptr [rsp + 0x4d]
008D8AEA  48 03 C8                        add rcx, rax
008D8AED  48 6B D1 25                     imul rdx, rcx, 0x25
008D8AF1  0F B6 44 24 4E                  movzx eax, byte ptr [rsp + 0x4e]
008D8AF6  48 03 D0                        add rdx, rax
008D8AF9  48 6B CA 25                     imul rcx, rdx, 0x25
008D8AFD  0F B6 44 24 4F                  movzx eax, byte ptr [rsp + 0x4f]
008D8B02  48 03 C1                        add rax, rcx
008D8B05  8D 57 FF                        lea edx, [rdi - 1]
008D8B08  8B C0                           mov eax, eax
008D8B0A  48 23 D0                        and rdx, rax
008D8B0D  49 8B 8F B0 04 00 00            mov rcx, qword ptr [r15 + 0x4b0]
008D8B14  48 8B 04 D1                     mov rax, qword ptr [rcx + rdx*8]
008D8B18  49 89 06                        mov qword ptr [r14], rax
008D8B1B  4C 89 34 D1                     mov qword ptr [rcx + rdx*8], r14
008D8B1F  45 01 AF A8 04 00 00            add dword ptr [r15 + 0x4a8], r13d
008D8B26  49 8D 46 48                     lea rax, [r14 + 0x48]
008D8B2A  49 8D 8F C8 04 00 00            lea rcx, [r15 + 0x4c8]
008D8B31  48 8B 11                        mov rdx, qword ptr [rcx]
008D8B34  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
008D8B38  74 07                           je 0x1408d8b41
008D8B3A  B9 03 00 00 00                  mov ecx, 3
008D8B3F  CD 29                           int 0x29
008D8B41  48 89 10                        mov qword ptr [rax], rdx
008D8B44  48 89 48 08                     mov qword ptr [rax + 8], rcx
008D8B48  48 89 42 08                     mov qword ptr [rdx + 8], rax
008D8B4C  48 89 01                        mov qword ptr [rcx], rax
008D8B4F  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
008D8B59  8B 00                           mov eax, dword ptr [rax]
008D8B5B  41 89 86 88 00 00 00            mov dword ptr [r14 + 0x88], eax
008D8B62  45 01 AF D8 04 00 00            add dword ptr [r15 + 0x4d8], r13d
008D8B69  F0 45 01 AF DC 04 00 00         lock add dword ptr [r15 + 0x4dc], r13d
008D8B71  45 8B 5E 78                     mov r11d, dword ptr [r14 + 0x78]
008D8B75  41 0F BA E3 10                  bt r11d, 0x10
008D8B7A  72 09                           jb 0x1408d8b85
008D8B7C  45 85 D2                        test r10d, r10d
008D8B7F  0F 84 18 02 00 00               je 0x1408d8d9d
008D8B85  41 8B 46 7C                     mov eax, dword ptr [r14 + 0x7c]
008D8B89  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
008D8B8D  45 8B 87 BC 04 00 00            mov r8d, dword ptr [r15 + 0x4bc]
008D8B94  41 8B C8                        mov ecx, r8d
008D8B97  83 E1 1F                        and ecx, 0x1f
008D8B9A  4C 8B CB                        mov r9, rbx
008D8B9D  49 D3 E1                        shl r9, cl
008D8BA0  49 8B F9                        mov rdi, r9
008D8BA3  48 23 F8                        and rdi, rax
008D8BA6  48 89 BC 24 50 01 00 00         mov qword ptr [rsp + 0x150], rdi
008D8BAE  41 C1 E8 05                     shr r8d, 5
008D8BB2  45 85 C0                        test r8d, r8d
008D8BB5  0F 84 A2 00 00 00               je 0x1408d8c5d
008D8BBB  48 89 BC 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rdi
008D8BC3  40 0F B6 C7                     movzx eax, dil
008D8BC7  49 03 C4                        add rax, r12
008D8BCA  48 6B C8 25                     imul rcx, rax, 0x25
008D8BCE  0F B6 84 24 51 01 00 00         movzx eax, byte ptr [rsp + 0x151]
008D8BD6  48 03 C8                        add rcx, rax
008D8BD9  48 6B D1 25                     imul rdx, rcx, 0x25
008D8BDD  0F B6 84 24 52 01 00 00         movzx eax, byte ptr [rsp + 0x152]
008D8BE5  48 03 D0                        add rdx, rax
008D8BE8  48 6B CA 25                     imul rcx, rdx, 0x25
008D8BEC  0F B6 84 24 53 01 00 00         movzx eax, byte ptr [rsp + 0x153]
008D8BF4  48 03 C8                        add rcx, rax
008D8BF7  48 6B D1 25                     imul rdx, rcx, 0x25
008D8BFB  0F B6 84 24 54 01 00 00         movzx eax, byte ptr [rsp + 0x154]
008D8C03  48 03 D0                        add rdx, rax
008D8C06  48 6B CA 25                     imul rcx, rdx, 0x25
008D8C0A  0F B6 84 24 55 01 00 00         movzx eax, byte ptr [rsp + 0x155]
008D8C12  48 03 C8                        add rcx, rax
008D8C15  48 6B D1 25                     imul rdx, rcx, 0x25
008D8C19  0F B6 84 24 56 01 00 00         movzx eax, byte ptr [rsp + 0x156]
008D8C21  48 03 D0                        add rdx, rax
008D8C24  48 6B D2 25                     imul rdx, rdx, 0x25
008D8C28  0F B6 84 24 57 01 00 00         movzx eax, byte ptr [rsp + 0x157]
008D8C30  48 03 C2                        add rax, rdx
008D8C33  41 8D 48 FF                     lea ecx, [r8 - 1]
008D8C37  8B C0                           mov eax, eax
008D8C39  48 23 C8                        and rcx, rax
008D8C3C  49 8B 87 C0 04 00 00            mov rax, qword ptr [r15 + 0x4c0]
008D8C43  48 8D 0C C8                     lea rcx, [rax + rcx*8]
008D8C47  48 8B 09                        mov rcx, qword ptr [rcx]
008D8C4A  41 84 CD                        test r13b, cl
008D8C4D  75 0E                           jne 0x1408d8c5d
008D8C4F  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
008D8C53  49 23 C1                        and rax, r9
008D8C56  48 3B F8                        cmp rdi, rax
008D8C59  75 EC                           jne 0x1408d8c47
008D8C5B  EB 03                           jmp 0x1408d8c60
008D8C5D  48 8B CE                        mov rcx, rsi
008D8C60  48 85 C9                        test rcx, rcx
008D8C63  0F 85 8E 00 00 00               jne 0x1408d8cf7
008D8C69  49 8D 7E 10                     lea rdi, [r14 + 0x10]
008D8C6D  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008D8C71  49 23 C1                        and rax, r9
008D8C74  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008D8C79  0F B6 C0                        movzx eax, al
008D8C7C  49 03 C4                        add rax, r12
008D8C7F  48 6B C8 25                     imul rcx, rax, 0x25
008D8C83  0F B6 44 24 29                  movzx eax, byte ptr [rsp + 0x29]
008D8C88  48 03 C8                        add rcx, rax
008D8C8B  48 6B D1 25                     imul rdx, rcx, 0x25
008D8C8F  0F B6 44 24 2A                  movzx eax, byte ptr [rsp + 0x2a]
008D8C94  48 03 D0                        add rdx, rax
008D8C97  48 6B CA 25                     imul rcx, rdx, 0x25
008D8C9B  0F B6 44 24 2B                  movzx eax, byte ptr [rsp + 0x2b]
008D8CA0  48 03 C8                        add rcx, rax
008D8CA3  48 6B D1 25                     imul rdx, rcx, 0x25
008D8CA7  0F B6 44 24 2C                  movzx eax, byte ptr [rsp + 0x2c]
008D8CAC  48 03 D0                        add rdx, rax
008D8CAF  48 6B CA 25                     imul rcx, rdx, 0x25
008D8CB3  0F B6 44 24 2D                  movzx eax, byte ptr [rsp + 0x2d]
008D8CB8  48 03 C8                        add rcx, rax
008D8CBB  48 6B D1 25                     imul rdx, rcx, 0x25
008D8CBF  0F B6 44 24 2E                  movzx eax, byte ptr [rsp + 0x2e]
008D8CC4  48 03 D0                        add rdx, rax
008D8CC7  48 6B CA 25                     imul rcx, rdx, 0x25
008D8CCB  0F B6 44 24 2F                  movzx eax, byte ptr [rsp + 0x2f]
008D8CD0  48 03 C1                        add rax, rcx
008D8CD3  41 8D 50 FF                     lea edx, [r8 - 1]
008D8CD7  8B C0                           mov eax, eax
008D8CD9  48 23 D0                        and rdx, rax
008D8CDC  49 8B 8F C0 04 00 00            mov rcx, qword ptr [r15 + 0x4c0]
008D8CE3  48 8B 04 D1                     mov rax, qword ptr [rcx + rdx*8]
008D8CE7  48 89 07                        mov qword ptr [rdi], rax
008D8CEA  48 89 3C D1                     mov qword ptr [rcx + rdx*8], rdi
008D8CEE  45 01 AF B8 04 00 00            add dword ptr [r15 + 0x4b8], r13d
008D8CF5  EB 6F                           jmp 0x1408d8d66
008D8CF7  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
008D8CFB  39 41 10                        cmp dword ptr [rcx + 0x10], eax
008D8CFE  75 24                           jne 0x1408d8d24
008D8D00  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
008D8D04  39 41 14                        cmp dword ptr [rcx + 0x14], eax
008D8D07  75 1B                           jne 0x1408d8d24
008D8D09  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
008D8D0D  48 39 41 18                     cmp qword ptr [rcx + 0x18], rax
008D8D11  75 11                           jne 0x1408d8d24
008D8D13  49 8B 56 30                     mov rdx, qword ptr [r14 + 0x30]
008D8D17  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
008D8D1B  E8 98 44 BE FF                  call 0x1404bd1b8
008D8D20  85 C0                           test eax, eax
008D8D22  75 0D                           jne 0x1408d8d31
008D8D24  41 0F BA F3 10                  btr r11d, 0x10
008D8D29  45 89 5E 78                     mov dword ptr [r14 + 0x78], r11d
008D8D2D  41 89 76 7C                     mov dword ptr [r14 + 0x7c], esi
008D8D31  41 0F BA 6E 78 13               bts dword ptr [r14 + 0x78], 0x13
008D8D37  49 8D 4E 68                     lea rcx, [r14 + 0x68]
008D8D3B  E8 2C 4C 0A 00                  call 0x14097d96c
008D8D40  49 89 76 70                     mov qword ptr [r14 + 0x70], rsi
008D8D44  66 41 89 76 78                  mov word ptr [r14 + 0x78], si
008D8D49  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
008D8D4D  48 85 C9                        test rcx, rcx
008D8D50  74 07                           je 0x1408d8d59
008D8D52  33 D2                           xor edx, edx
008D8D54  E8 17 9B 2A 00                  call 0x140b82870
008D8D59  49 89 76 30                     mov qword ptr [r14 + 0x30], rsi
008D8D5D  41 89 76 38                     mov dword ptr [r14 + 0x38], esi
008D8D61  44 8B 54 24 28                  mov r10d, dword ptr [rsp + 0x28]
008D8D66  41 F7 47 08 00 04 00 00         test dword ptr [r15 + 8], 0x400
008D8D6E  74 2D                           je 0x1408d8d9d
008D8D70  45 8B CA                        mov r9d, r10d
008D8D73  4D 8B C6                        mov r8, r14
008D8D76  48 8B BC 24 40 01 00 00         mov rdi, qword ptr [rsp + 0x140]
008D8D7E  48 8B D7                        mov rdx, rdi
008D8D81  49 8B CF                        mov rcx, r15
008D8D84  E8 A3 C9 BB FF                  call 0x14049572c
008D8D89  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
008D8D8C  41 89 86 A0 00 00 00            mov dword ptr [r14 + 0xa0], eax
008D8D93  8B 47 2C                        mov eax, dword ptr [rdi + 0x2c]
008D8D96  41 89 86 A4 00 00 00            mov dword ptr [r14 + 0xa4], eax
008D8D9D  49 8B C5                        mov rax, r13
008D8DA0  F0 49 0F C1 46 40               lock xadd qword ptr [r14 + 0x40], rax
008D8DA6  49 03 C5                        add rax, r13
008D8DA9  49 3B C5                        cmp rax, r13
008D8DAC  7F 07                           jg 0x1408d8db5
008D8DAE  B9 0E 00 00 00                  mov ecx, 0xe
008D8DB3  CD 29                           int 0x29
008D8DB5  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
008D8DBD  4C 89 30                        mov qword ptr [rax], r14
008D8DC0  4C 8B F6                        mov r14, rsi
008D8DC3  49 89 B7 A0 04 00 00            mov qword ptr [r15 + 0x4a0], rsi
008D8DCA  49 8D BF 98 04 00 00            lea rdi, [r15 + 0x498]
008D8DD1  48 8B C3                        mov rax, rbx
008D8DD4  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
008D8DD9  24 06                           and al, 6
008D8DDB  3C 02                           cmp al, 2
008D8DDD  75 08                           jne 0x1408d8de7
008D8DDF  48 8B CF                        mov rcx, rdi
008D8DE2  E8 E9 CF 98 FF                  call 0x140265dd0
008D8DE7  48 8B CF                        mov rcx, rdi
008D8DEA  E8 11 88 A0 FF                  call 0x1402e1600
008D8DEF  E8 BC 4A 98 FF                  call 0x14025d8b0
008D8DF4  49 8B CF                        mov rcx, r15
008D8DF7  E8 40 12 00 00                  call 0x1408da03c
008D8DFC  E9 7B FA FF FF                  jmp 0x1408d887c
008D8E01  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008D8E05  33 F6                           xor esi, esi
008D8E07  48 83 CB FF                     or rbx, 0xffffffffffffffff
008D8E0B  4C 8B BC 24 30 01 00 00         mov r15, qword ptr [rsp + 0x130]
008D8E13  44 8B EE                        mov r13d, esi
008D8E16  44 8B F6                        mov r14d, esi
008D8E19  49 8B 8F A0 04 00 00            mov rcx, qword ptr [r15 + 0x4a0]
008D8E20  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008D8E29  48 3B C8                        cmp rcx, rax
008D8E2C  75 35                           jne 0x1408d8e63
008D8E2E  49 89 B7 A0 04 00 00            mov qword ptr [r15 + 0x4a0], rsi
008D8E35  F0 49 0F C1 9F 98 04 00 00      lock xadd qword ptr [r15 + 0x498], rbx
008D8E3E  80 E3 06                        and bl, 6
008D8E41  80 FB 02                        cmp bl, 2
008D8E44  75 0C                           jne 0x1408d8e52
008D8E46  49 8D 8F 98 04 00 00            lea rcx, [r15 + 0x498]
008D8E4D  E8 7E CF 98 FF                  call 0x140265dd0
008D8E52  49 8D 8F 98 04 00 00            lea rcx, [r15 + 0x498]
008D8E59  E8 A2 87 A0 FF                  call 0x1402e1600
008D8E5E  E8 4D 4A 98 FF                  call 0x14025d8b0
008D8E63  4D 85 F6                        test r14, r14
008D8E66  74 19                           je 0x1408d8e81
008D8E68  49 89 76 40                     mov qword ptr [r14 + 0x40], rsi
008D8E6C  49 8B CE                        mov rcx, r14
008D8E6F  E8 A8 4A 0A 00                  call 0x14097d91c
008D8E74  BA 45 74 77 56                  mov edx, 0x56777445
008D8E79  49 8B CE                        mov rcx, r14
008D8E7C  E8 EF 99 2A 00                  call 0x140b82870
008D8E81  4D 85 ED                        test r13, r13
008D8E84  74 0D                           je 0x1408d8e93
008D8E86  BA 45 74 77 56                  mov edx, 0x56777445
008D8E8B  49 8B CD                        mov rcx, r13
008D8E8E  E8 DD 99 2A 00                  call 0x140b82870
008D8E93  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
008D8E97  48 81 C4 F0 00 00 00            add rsp, 0xf0
008D8E9E  41 5F                           pop r15
008D8EA0  41 5E                           pop r14
008D8EA2  41 5D                           pop r13
008D8EA4  41 5C                           pop r12
008D8EA6  5F                              pop rdi
008D8EA7  5E                              pop rsi
008D8EA8  5B                              pop rbx
008D8EA9  C3                              ret
008D8EAA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCovSampContextGetModule(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int8 v_stack_mC9;
    unsigned __int8 v_stack_mCA;
    unsigned __int8 v_stack_mCB;
    unsigned __int8 v_stack_mCC;
    unsigned __int8 v_stack_mCD;
    unsigned __int8 v_stack_mCE;
    unsigned __int8 v_stack_mCF;
    unsigned __int64 v_stack_mD0;
    unsigned __int8 v_stack_mD1;
    unsigned __int8 v_stack_mD2;
    unsigned __int8 v_stack_mD3;
    unsigned __int8 v_stack_mD4;
    unsigned __int8 v_stack_mD5;
    unsigned __int8 v_stack_mD6;
    unsigned __int8 v_stack_mD7;
    unsigned __int64 v_stack_mD8;
    unsigned __int8 v_stack_mD9;
    unsigned __int8 v_stack_mDA;
    unsigned __int8 v_stack_mDB;
    unsigned __int8 v_stack_mDC;
    unsigned __int8 v_stack_mDD;
    unsigned __int8 v_stack_mDE;
    unsigned __int8 v_stack_mDF;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int8 v_stack_mF9;
    unsigned __int8 v_stack_mFA;
    unsigned __int8 v_stack_mFB;
    unsigned __int8 v_stack_mFC;
    unsigned __int8 v_stack_mFD;
    unsigned __int8 v_stack_mFE;
    unsigned __int8 v_stack_mFF;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int8 v_stack_p29;
    unsigned __int8 v_stack_p2A;
    unsigned __int8 v_stack_p2B;
    unsigned int v_stack_p2C;
    unsigned __int8 v_stack_p2D;
    unsigned __int8 v_stack_p2E;
    unsigned __int8 v_stack_p2F;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (240);
    v_rsi = 0;
    v_stack_mE8 = 0;
    v_stack_m100 = 0;
    *(unsigned __int64 *)(a6) = 0;
    v_stack_mB0 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 160) = v_xmm0;
    v_stack_mA8 = *(unsigned __int64 *)(a5 + 32);
    result = RtlImageNtHeader(*(unsigned __int64 *)(a5 + 16), a2, a6, a4);
    v_stack_m70 = result;
    if (result != 0) goto loc_008D807F;
    v_stack_m108 = 0xC00000BBULL;
    v_rbx = (a2) | (-1);
    goto loc_008D8E19;
loc_008D807F:
    v_stack_mA0 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 88)));
    v_stack_m9C = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    if (((*(unsigned int *)(a5 + 8)) & (256)) == 0) goto loc_008D80A2;
    goto loc_008D80C0;
loc_008D80A2:
    if (*(unsigned __int64 *)(a5 + 48) != 0) goto loc_008D80BC;
    v_stack_m108 = 0xC00000BBULL;
    v_rbx = (v_rbx) | (-1);
    goto loc_008D8E19;
loc_008D80BC:
loc_008D80C0:
    v_stack_mB0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 48) + 24);
    if (((*(unsigned int *)(a1 + 8)) & (0x400ULL)) == 0) goto loc_008D8107;
    if ((*(unsigned __int64 *)(a5 + 16)) != (*(unsigned __int64 *)(v_rbx + 688))) goto loc_008D80E9;
    v_stack_m100 = 1;
    goto loc_008D8107;
loc_008D80E9:
    v_stack_m100 = 0;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a5 + 48) + 24)) ^ ((unsigned int)(*(unsigned int *)(v_stack_p18 + 40)));
    v_stack_mB0 = a1;
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 40)));
loc_008D8107:
    v_rbx = (v_rbx) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 1176, a2, a3, a4);
    v_stack_mF8 = result;
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1 + 1176;
        a3 = 0;
        a2 = 0;
        a1 = a1 + 1176;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a1 = v_stack_mF8;
    }
    if (a1 != 0) {
        *(unsigned __int8 *)(a1 + 10) = 1;
    }
    result = EtwpCovSampContextFastFindModule(a1, v_stack_mB0, a6, a4);
    if (result == 0) goto loc_008D81CE;
    if (result != (*(unsigned __int64 *)(a6))) goto loc_008D81CE;
    result = ProcessForExeModule(a1, v_stack_p18, *(unsigned __int64 *)(a6), (unsigned int)(v_stack_m100));
    result = 17;
    if (result != (*(unsigned __int64 *)(a6))) {
        a1 = a1 + 1176;
        result = ExfReleasePushLockShared(a1, v_stack_p18, *(unsigned __int64 *)(a6), (unsigned int)(v_stack_m100));
    }
    result = KeAbPostRelease(a1 + 1176, v_stack_p18, *(unsigned __int64 *)(a6), (unsigned int)(v_stack_m100));
    result = KeLeaveCriticalRegion(a1 + 1176, v_stack_p18, *(unsigned __int64 *)(a6), (unsigned int)(v_stack_m100));
    v_stack_m108 = 0;
loc_008D81C6:
    goto loc_008D8E19;
loc_008D81CE:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1196))) >> (5));
    v_stack_mB8 = (unsigned int)(result);
    a1 = (unsigned int)(*(unsigned int *)(a1 + 1192));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1192)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1208))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1208))); }
    v_stack_mC0 = (unsigned int)(a1);
    result = 17;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1192)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1208))))) {
        a1 = a1 + 1176;
        result = ExfReleasePushLockShared(a1, v_stack_p18, *(unsigned __int64 *)(a6), (unsigned int)(v_stack_m100));
    }
    result = KeAbPostRelease(a1 + 1176, v_stack_p18, *(unsigned __int64 *)(a6), (unsigned int)(v_stack_m100));
    result = KeLeaveCriticalRegion(a1 + 1176, v_stack_p18, *(unsigned __int64 *)(a6), (unsigned int)(v_stack_m100));
    result = ExAllocatePool2(176 + 80, 176, (unsigned int)(0x56777445ULL), (unsigned int)(v_stack_m100));
    if (result != 0) goto loc_008D8239;
    v_stack_m108 = 0xC000009AULL;
    goto loc_008D81C6;
loc_008D8239:
    a2 = 0;
    result = memset(result, a2, 176, (unsigned int)(v_stack_m100));
    *(unsigned __int64 *)(result + 72 + 8) = result + 72;
    *(unsigned __int64 *)(result + 72) = result + 72;
    *(unsigned __int64 *)(result + 88 + 8) = result + 88;
    *(unsigned __int64 *)(result + 88) = result + 88;
    *(unsigned __int64 *)(result) = 0;
    *(unsigned __int64 *)(result + 16) = 0;
    *(unsigned __int64 *)(result + 64) = 0;
    *(unsigned __int64 *)(result + 8) = v_stack_mB0;
    *(unsigned __int64 *)(result + 40) = v_stack_mA8;
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(v_stack_mA0));
    *(unsigned int *)(result + 36) = (unsigned int)((unsigned int)(v_stack_m9C));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 8))) << (9));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 120)))));
    a1 = (unsigned int)((a1) & (0x20000ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 120)))));
    *(unsigned int *)(result + 120) = (unsigned int)(a1);
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    v_stack_mC8 = 0;
    v_stack_mF8 = v_stack_m80;
    v_stack_mF0 = 0;
    result = EtwpFindDebugId(*(unsigned __int64 *)(a5 + 16), v_stack_mA8, result + 48, result + 56);
    v_stack_m108 = (unsigned int)(result);
    if (sign_flag) goto loc_008D8315;
    if ((*(unsigned int *)(result + 56)) <= 0x400ULL) goto loc_008D8328;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 48), a2, result + 48, result + 56);
    *(unsigned __int64 *)(result + 48) = 0;
    *(unsigned int *)(result + 56) = 0;
loc_008D8315:
    v_stack_mF0 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m100)) != 0) goto loc_008D8338;
    goto loc_008D83CE;
loc_008D8328:
    v_stack_mC8 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m100) + 20)));
    result = ((unsigned int)(v_stack_m100)) + (4);
    v_stack_mF8 = result;
loc_008D8338:
    result = EtwpCovSampModuleGetName(result, a5, v_stack_p20, result + 56);
    v_stack_m108 = (unsigned int)(result);
    if (sign_flag) goto loc_008D81C6;
    v_stack_m90 = *(unsigned __int64 *)(result + 112);
    v_stack_m88 = (unsigned __int16)((unsigned int)(*(unsigned int *)(result + 120)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1624))) == 0) goto loc_008D839B;
    result = EtwpCovSampCheckForSegments(v_stack_m90, a1 + 1304, (unsigned int)(*(unsigned int *)(a1 + 1624)), result + 56);
    goto loc_008D839F;
loc_008D839B:
loc_008D839F:
    if ((unsigned int)((unsigned int)(v_stack_mF0)) == 0) goto loc_008D83CA;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1628))) != 0) {
        a2 = a1 + 1464;
        a1 = v_stack_m90;
        result = EtwpCovSampCheckForSegments(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 1628)), result + 56);
        a1 = 0;
        a1 = ((unsigned int)(result) == 0) ? 1 : 0;
    }
loc_008D83CE:
    if ((unsigned int)(a1) != 0) goto loc_008D83DA;
    if ((unsigned int)((unsigned int)(v_stack_m100)) == 0) goto loc_008D84A0;
loc_008D83DA:
    a1 = (unsigned int)((a1) << (16));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 120)))));
    a1 = (unsigned int)((a1) & (0x10000ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 120)))));
    *(unsigned int *)(result + 120) = (unsigned int)(a1);
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 36)));
    v_stack_p2C = (unsigned int)((unsigned int)(*(unsigned int *)(result + 32)));
    result = EtwCovSampHash(a5, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12)))), (unsigned int)(*(unsigned int *)(a1 + 1628)), result + 56);
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 40)));
    v_stack_p2C = (unsigned int)((unsigned int)(v_stack_mC8));
    v_stack_m50 = v_xmm0;
    result = EtwCovSampHash(a5, result, (unsigned int)(*(unsigned int *)(a1 + 1628)), result + 56);
    result = EtwCovSampHash(a5, result, (unsigned int)(*(unsigned int *)(a1 + 1628)), result + 56);
    result = EtwCovSampHash(a5, result, (unsigned int)(*(unsigned int *)(a1 + 1628)), result + 56);
    v_stack_p28 = result;
    result = (result) >> (32);
    result = (unsigned int)((result) ^ (a5));
    if (condition_is_equal) { result = 0; }
    if (v_stack_m100 == 0) {
        a1 = v_stack_p18;
        result = (unsigned int)((result) ^ (*(unsigned int *)(a1 + 40)));
    }
    *(unsigned int *)(result + 124) = (unsigned int)(result);
loc_008D84A0:
    a2 = (unsigned int)(((unsigned int)(v_stack_mB8)) + ((unsigned int)((unsigned int)(v_stack_mB8))));
    result = (unsigned int)(((unsigned int)(v_stack_mC0)) + 1);
    v_r12 = 0;
    if (((unsigned int)(result)) >= = ((unsigned int)(a2))) {
        v_r12 = (unsigned int)(a2);
        result = 128;
        if ((unsigned int)(a2) == 0) { v_r12 = (unsigned int)(result); }
        a2 = v_r12 + v_r12 * 1;
        a2 = (a2) << (3);
        a1 = 256;
        a3 = 0x56777445ULL;
        result = ExAllocatePool2(a1, a2, a3, result + 56);
        v_stack_mE8 = result;
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 1176, a2, a3, result + 56);
    v_stack_p28 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 1176;
        a2 = result;
        a1 = a1 + 1176;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, result + 56);
        result = a5;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 0;
    }
    *(unsigned __int64 *)(a1 + 1184) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (v_stack_mE8 == 0) goto loc_008D8819;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1196))) >> (5));
    if (((unsigned int)(v_r12)) <= ((unsigned int)(result))) goto loc_008D8819;
    result = (unsigned int)((v_r12 - 1) & ((unsigned int)(v_r12)));
    v_stack_p28 = (unsigned int)(result);
    if (condition_is_equal) goto loc_008D858C;
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    if ((unsigned int)(v_r12) == 0) goto loc_008D8586;
loc_008D857F:
    a1 = (unsigned int)((a1) + (0));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) >> (1));
    if (condition_is_not_equal) goto loc_008D857F;
loc_008D8586:
    a3 = (unsigned int)((0) << ((unsigned __int8)(a1)));
loc_008D858C:
    if (((unsigned int)(a3)) > ((unsigned int)((unsigned int)(0x4000000ULL)))) { a3 = (unsigned int)((unsigned int)(0x4000000ULL)); }
    result = (a1 + 1208) | (0);
    a1 = (unsigned int)((unsigned int)(a3));
    if ((v_stack_mE8 + (unsigned int)((unsigned int)(v_r12)) * 8) > (v_stack_mE8 + (unsigned int)((unsigned int)(v_r12)) * 8 + a3 * 8)) { a1 = 0; }
    v_rdi = v_stack_mE8;
    if (a1 != 0) {
        v_rdi = v_stack_mE8 + (unsigned int)((unsigned int)(v_r12)) * 8;
        v_rdi = v_stack_mE8;
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1208 + 4))))) & (31));
    result = (v_rbx) << ((unsigned __int8)(a1));
    v_stack_mC0 = result;
    if (condition_is_below_or_equal) goto loc_008D86B8;
loc_008D85E6:
    v_stack_mF8 = *(unsigned __int64 *)(a1 + 1208 + 8);
loc_008D85EF:
    v_stack_mB8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1208 + 8) + 0 * 8);
    if (((0) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1208 + 8) + 0 * 8)))) != 0) goto loc_008D86A3;
    *(unsigned __int64 *)(v_stack_mF8 + 0 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1208 + 8) + 0 * 8));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1208 + 8) + 0 * 8) + 8)) & (v_stack_mC0);
    v_stack_mD8 = result;
    result = ((unsigned __int8)(result)) + (0xB15DCBULL);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1208 + 8) + 0 * 8)) * (result);
    a1 = (a1) + (v_stack_mD7);
    a2 = (0) * (a1);
    a2 = (a2) + (v_stack_mD6);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_mD5);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_mD4);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_mD3);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_mD2);
    a2 = (a2) * (a2);
    result = (v_stack_mD1) + (a2);
    a1 = (a3 - 1) & ((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(v_stack_mB8) = *(unsigned __int64 *)(v_stack_mE8 + (unsigned int)((unsigned int)(v_r12)) * 8 + a1 * 8);
    *(unsigned __int64 *)(v_stack_mE8 + (unsigned int)((unsigned int)(v_r12)) * 8 + a1 * 8) = v_stack_mB8;
    goto loc_008D85EF;
loc_008D86A3:
    v_r10 = (unsigned int)((0) + (0));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1208 + 4))))) >> (5));
    if (((unsigned int)(v_r10)) < ((unsigned int)(result))) goto loc_008D85E6;
loc_008D86B8:
    *(unsigned __int64 *)(a1 + 1208 + 8) = v_stack_mE8 + (unsigned int)((unsigned int)(v_r12)) * 8;
    a3 = (unsigned int)((a3) << (5));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1208 + 4))) & (31));
    a3 = (unsigned int)((a3) | ((unsigned int)(a2)));
    *(unsigned int *)(a1 + 1208 + 4) = (unsigned int)(a3);
    if (a5 == 0) goto loc_008D86F0;
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    if ((unsigned int)(v_r12) == 0) goto loc_008D86EA;
loc_008D86E2:
    a1 = (unsigned int)((a1) + (0));
    v_r12 = (unsigned int)((v_r12) >> (1));
    if (condition_is_not_equal) goto loc_008D86E2;
loc_008D86EA:
    v_r12 = (unsigned int)((0) << ((unsigned __int8)(a1)));
loc_008D86F0:
    if (((unsigned int)(v_r12)) > ((unsigned int)((unsigned int)(0x4000000ULL)))) { v_r12 = (unsigned int)((unsigned int)(0x4000000ULL)); }
    result = (a1 + 1192) | (0);
    a1 = (unsigned int)((unsigned int)(v_r12));
    if (v_stack_mE8 > (v_stack_mE8 + v_r12 * 8)) { a1 = 0; }
    v_rdi = v_stack_mE8;
    if (a1 != 0) {
        v_rdi = v_stack_mE8;
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1192 + 4))))) & (31));
    v_r11 = (v_rbx) << ((unsigned __int8)(a1));
    if (condition_is_below_or_equal) goto loc_008D87FE;
loc_008D873B:
    v_stack_p28 = *(unsigned __int64 *)(a1 + 1192 + 8);
loc_008D8747:
    if (((0) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1192 + 8) + 0 * 8)))) != 0) goto loc_008D87E9;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1192 + 8) + 0 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1192 + 8) + 0 * 8));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1192 + 8) + 0 * 8) + 8)) & (v_r11);
    v_stack_mD0 = result;
    result = ((unsigned __int8)(result)) + (0xB15DCBULL);
    a1 = (0) * (result);
    a1 = (a1) + (v_stack_mCF);
    a2 = (*(unsigned __int64 *)(a1 + 1192 + 8)) * (a1);
    a2 = (a2) + (v_stack_mCE);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_mCD);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_mCC);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_mCB);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_mCA);
    a2 = (a2) * (a2);
    result = (v_stack_mC9) + (a2);
    a1 = (v_r12 - 1) & ((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1192 + 8) + 0 * 8)) = *(unsigned __int64 *)(v_rdi + a1 * 8);
    *(unsigned __int64 *)(v_rdi + a1 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1192 + 8) + 0 * 8);
    goto loc_008D8747;
loc_008D87E9:
    a4 = (unsigned int)((0) + (0));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1192 + 4))))) >> (5));
    if (((unsigned int)(a4)) < ((unsigned int)(result))) goto loc_008D873B;
loc_008D87FE:
    *(unsigned __int64 *)(a1 + 1192 + 8) = v_rdi;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1192 + 4))) & (31));
    v_r12 = (unsigned int)((v_r12) << (5));
    a2 = (unsigned int)((a2) | ((unsigned int)(v_r12)));
    *(unsigned int *)(a1 + 1192 + 4) = (unsigned int)(a2);
    v_stack_mE8 = *(unsigned __int64 *)(a1 + 1192 + 8);
loc_008D8819:
    if ((*(unsigned int *)(a1 + 1196)) >= 32) goto loc_008D883B;
    v_stack_m108 = 0xC000009AULL;
loc_008D8831:
    goto loc_008D8E19;
loc_008D883B:
    result = EtwpCovSampContextFastFindModule(a1, v_stack_mB0, a6, a4);
    if (result == 0) goto loc_008D8A5F;
    if (result != (*(unsigned __int64 *)(a6))) goto loc_008D8882;
    result = ProcessForExeModule(a1, v_stack_p18, *(unsigned __int64 *)(a6), (unsigned int)(v_stack_m100));
loc_008D887C:
    v_stack_m108 = 0;
    goto loc_008D8831;
loc_008D8882:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1196))))) & (31));
    result = (v_rbx) << ((unsigned __int8)(a1));
    result = (result) & (*(unsigned __int64 *)((unsigned int)(v_stack_m100) + 8));
    v_stack_p28 = result;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1196))) >> (5));
    v_stack_m68 = result;
    result = ((unsigned __int8)(result)) + ((unsigned int)(0xB15DCBULL));
    a1 = (a1) * (result);
    a1 = (a1) + (v_stack_p29);
    a2 = (v_stack_p18) * (a1);
    a2 = (a2) + (v_stack_p2A);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_p2B);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_p2C);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_p2D);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_p2E);
    a2 = (a2) * (a2);
    result = (v_stack_p2F) + (a2);
    a1 = (v_rdi - 1) & ((unsigned int)((unsigned int)(result)));
    result = (*(unsigned __int64 *)((unsigned int)(v_stack_m100))) & (v_r11);
    if (result == v_r11) {
        result = *(unsigned __int64 *)(v_rsi);
    }
    if ((((unsigned __int8)(v_stack_mE8)) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1200) + a1 * 8)))) != 0) goto loc_008D896B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1200) + a1 * 8)) == ((unsigned int)(v_stack_m100))) goto loc_008D895C;
    goto loc_008D894A;
loc_008D895C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1200) + a1 * 8)) = *(unsigned __int64 *)((unsigned int)(v_stack_m100));
    goto loc_008D896E;
loc_008D896B:
loc_008D896E:
    *(unsigned __int64 *)((unsigned int)(v_stack_m100)) = 0;
    if (*(unsigned __int64 *)((unsigned int)(v_stack_m100) + 16) == 0) goto loc_008D8A5F;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1212))))) & (31));
    result = (v_rbx) << ((unsigned __int8)(a1));
    result = (result) & (*(unsigned __int64 *)((unsigned int)(v_stack_m100) + 16 + 8));
    v_stack_p28 = result;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1212))) >> (5));
    v_stack_m60 = result;
    result = ((unsigned __int8)(result)) + ((unsigned int)(0xB15DCBULL));
    a1 = (a1) * (result);
    a1 = (a1) + (v_stack_p29);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1200) + a1 * 8)) * (a1);
    a2 = (a2) + (v_stack_p2A);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_p2B);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_p2C);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_p2D);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_p2E);
    a2 = (a2) * (a2);
    result = (v_stack_p2F) + (a2);
    a1 = (v_rdi - 1) & ((unsigned int)((unsigned int)(result)));
    v_r10 = (*(unsigned __int64 *)((unsigned int)(v_stack_m100) + 16)) & (v_r11);
    result = *(unsigned __int64 *)(a1 + 1216);
    if (v_r10 == v_r11) {
        result = *(unsigned __int64 *)(v_rsi);
    }
    if ((((unsigned __int8)(v_stack_mE8)) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1216) + a1 * 8)))) != 0) goto loc_008D8A58;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1216) + a1 * 8)) == ((unsigned int)(v_stack_m100) + 16)) goto loc_008D8A49;
    goto loc_008D8A37;
loc_008D8A49:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1216) + a1 * 8)) = *(unsigned __int64 *)((unsigned int)(v_stack_m100) + 16);
    goto loc_008D8A5B;
loc_008D8A58:
loc_008D8A5B:
    *(unsigned __int64 *)((unsigned int)(v_stack_m100) + 16) = 0;
loc_008D8A5F:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m100)))) << (20));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 120))) | ((unsigned int)(result)));
    *(unsigned int *)(result + 120) = (unsigned int)(a1);
    *(unsigned int *)(result + 128) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1632)));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1196))))) >> (5));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1196))) & (31));
    result = (v_rbx) << ((unsigned __int8)(a1));
    result = (result) & (*(unsigned __int64 *)(result + 8));
    v_stack_mE0 = result;
    result = ((unsigned __int8)(result)) + ((unsigned int)(0xB15DCBULL));
    a1 = (a1) * (result);
    a1 = (a1) + (v_stack_mDF);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1216) + a1 * 8)) * (a1);
    a2 = (a2) + (v_stack_mDE);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_mDD);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_mDC);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_mDB);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_mDA);
    a1 = (a1) * (a2);
    result = (v_stack_mD9) + (a1);
    a2 = (v_rdi - 1) & ((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1200) + a2 * 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1200) + a2 * 8) = result;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1224) + 8)) != (a1 + 1224)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(result + 72) = *(unsigned __int64 *)(a1 + 1224);
    *(unsigned __int64 *)(result + 72 + 8) = a1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1224) + 8) = result + 72;
    *(unsigned __int64 *)(a1) = result + 72;
    *(unsigned int *)(result + 136) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 72)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1224) + 8)) < (a1 + 1224)) goto loc_008D8B85;
    if ((unsigned int)((unsigned int)(v_stack_m100)) == 0) goto loc_008D8D9D;
loc_008D8B85:
    *(unsigned __int64 *)(result + 24) = (unsigned int)(*(unsigned int *)(result + 124));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1212))))) & (31));
    a4 = (v_rbx) << ((unsigned __int8)(a1));
    v_rdi = (a4) & ((unsigned int)(*(unsigned int *)(result + 124)));
    v_stack_p28 = v_rdi;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1212))) >> (5));
    if ((unsigned int)(a3) == 0) goto loc_008D8C5D;
    v_stack_m58 = v_rdi;
    result = ((unsigned __int8)(v_rdi)) + ((unsigned int)(0xB15DCBULL));
    a1 = (a1) * (result);
    a1 = (a1) + (v_stack_p29);
    a2 = (*(unsigned __int64 *)(a1 + 1224)) * (a1);
    a2 = (a2) + (v_stack_p2A);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_p2B);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_p2C);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_p2D);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_p2E);
    a2 = (a2) * (a2);
    result = (v_stack_p2F) + (a2);
    a1 = (a3 - 1) & ((unsigned int)((unsigned int)(result)));
loc_008D8C47:
    if ((((unsigned __int8)(v_stack_mE8)) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1216) + a1 * 8)))) != 0) goto loc_008D8C5D;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1216) + a1 * 8) + 8)) & (a4);
    if (v_rdi != result) goto loc_008D8C47;
    goto loc_008D8C60;
loc_008D8C5D:
loc_008D8C60:
    if (0 != 0) goto loc_008D8CF7;
    result = (*(unsigned __int64 *)(result + 16 + 8)) & (a4);
    v_stack_m100 = result;
    result = ((unsigned __int8)(result)) + ((unsigned int)(0xB15DCBULL));
    a1 = (0) * (result);
    a1 = (a1) + (v_stack_mFF);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_mFE);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_mFD);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_mFC);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_mFB);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_mFA);
    a1 = (a1) * (a2);
    result = (v_stack_mF9) + (a1);
    a2 = (a3 - 1) & ((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1216) + a2 * 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1216) + a2 * 8) = result + 16;
    goto loc_008D8D66;
loc_008D8CF7:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 1216) + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 32))))) goto loc_008D8D24;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 1216) + 20)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 36))))) goto loc_008D8D24;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1216) + 24)) != (*(unsigned __int64 *)(result + 40))) goto loc_008D8D24;
    result = EtwpCheckDebugInfoEqual(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1216) + 32), *(unsigned __int64 *)(result + 48), a3, a4);
    if ((unsigned int)(result) == 0) {
        *(unsigned int *)(result + 120) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 120)));
        *(unsigned int *)(result + 124) = 0;
    }
    result = EtwpCovSampModuleNameInfoCleanup(result + 104, *(unsigned __int64 *)(result + 48), a3, a4);
    *(unsigned __int64 *)(result + 112) = 0;
    *(unsigned __int16 *)(result + 120) = 0;
    if (*(unsigned __int64 *)(result + 48) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 48), a2, a3, a4);
    }
    *(unsigned __int64 *)(result + 48) = 0;
    *(unsigned int *)(result + 56) = 0;
loc_008D8D66:
    v_rdi = result + 16;
    if (((*(unsigned int *)(a1 + 8)) & (0x400ULL)) != 0) {
        a4 = (unsigned int)((unsigned int)(v_stack_m100));
        a3 = result;
        v_rdi = v_stack_p18;
        a2 = v_rdi;
        a1 = a1;
        result = ProcessForExeModule(a1, a2, a3, a4);
        result = *(unsigned int *)(v_rdi + 40);
        *(unsigned int *)(result + 160) = (unsigned int)(result);
        result = *(unsigned int *)(v_rdi + 44);
        *(unsigned int *)(result + 164) = (unsigned int)(result);
    }
    result = (v_stack_mE8) + (v_stack_mE8);
    if (result <= v_stack_mE8) {
        a1 = 14;
    }
    *(unsigned __int64 *)(a6) = result;
    *(unsigned __int64 *)(a1 + 1184) = 0;
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a1 + 1176;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 + 1176, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1 + 1176, a2, a3, a4);
    result = EtwpCovSampContextPruneModules(a1, a2, a3, a4);
    goto loc_008D887C;
loc_008D8E19:
    if ((*(unsigned __int64 *)(a1 + 1184)) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_008D8E63;
    *(unsigned __int64 *)(a1 + 1184) = 0;
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = a1 + 1176;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 + 1176, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1 + 1176, a2, a3, a4);
loc_008D8E63:
    if (0 != 0) {
        *(unsigned __int64 *)(0 + 64) = 0;
        a1 = 0;
        result = EtwpCovSampModuleCleanup(a1, a2, a3, a4);
        a2 = 0x56777445ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (v_stack_mE8 != 0) {
        a2 = 0x56777445ULL;
        a1 = v_stack_mE8;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (240);
    return (unsigned int)(v_stack_m108);
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCovSampContextGetModule(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint8_t v_stack_mC9;
    uint8_t v_stack_mCA;
    uint8_t v_stack_mCB;
    uint8_t v_stack_mCC;
    uint8_t v_stack_mCD;
    uint8_t v_stack_mCE;
    uint8_t v_stack_mCF;
    uint64_t v_stack_mD0;
    uint8_t v_stack_mD1;
    uint8_t v_stack_mD2;
    uint8_t v_stack_mD3;
    uint8_t v_stack_mD4;
    uint8_t v_stack_mD5;
    uint8_t v_stack_mD6;
    uint8_t v_stack_mD7;
    uint64_t v_stack_mD8;
    uint8_t v_stack_mD9;
    uint8_t v_stack_mDA;
    uint8_t v_stack_mDB;
    uint8_t v_stack_mDC;
    uint8_t v_stack_mDD;
    uint8_t v_stack_mDE;
    uint8_t v_stack_mDF;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint8_t v_stack_mF9;
    uint8_t v_stack_mFA;
    uint8_t v_stack_mFB;
    uint8_t v_stack_mFC;
    uint8_t v_stack_mFD;
    uint8_t v_stack_mFE;
    uint8_t v_stack_mFF;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint8_t v_stack_p29;
    uint8_t v_stack_p2A;
    uint8_t v_stack_p2B;
    uint32_t v_stack_p2C;
    uint8_t v_stack_p2D;
    uint8_t v_stack_p2E;
    uint8_t v_stack_p2F;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (240);
    local_rsi = 0;
    v_stack_mE8 = 0;
    v_stack_m100 = 0;
    *(uint64_t *)(arg6) = 0;
    v_stack_mB0 = v_xmm0;
    *(uint64_t *)(local_rsp - 0xA0) = v_xmm0;
    v_stack_mA8 = *(uint64_t *)(arg5 + 0x20);
    result = RtlImageNtHeader(*(uint64_t *)(arg5 + 0x10), Arg2, Arg6, Arg4);
    v_stack_m70 = result;
    if (result != 0) goto loc_008D807F;
    v_stack_m108 = 0xC00000BBULL;
    local_rbx = (Arg2) | (-1);
    goto loc_008D8E19;
loc_008D807F:
    v_stack_mA0 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x58)));
    v_stack_m9C = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    if (((*(uint32_t *)(arg5 + 0x8)) & (256)) == 0) goto loc_008D80A2;
    goto loc_008D80C0;
loc_008D80A2:
    if (*(uint64_t *)(arg5 + 0x30) != 0) goto loc_008D80BC;
    v_stack_m108 = 0xC00000BBULL;
    local_rbx = (local_rbx) | (-1);
    goto loc_008D8E19;
loc_008D80BC:
loc_008D80C0:
    v_stack_mB0 = *(uint64_t *)(*(uint64_t *)(arg5 + 0x30) + 0x18);
    if (((*(uint32_t *)(arg1 + 0x8)) & (0x400ULL)) == 0) goto loc_008D8107;
    if ((*(uint64_t *)(arg5 + 0x10)) != (*(uint64_t *)(local_rbx + 0x2B0))) goto loc_008D80E9;
    v_stack_m100 = 1;
    goto loc_008D8107;
loc_008D80E9:
    v_stack_m100 = 0;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg5 + 0x30) + 0x18)) ^ ((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x28)));
    v_stack_mB0 = Arg1;
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x28)));
loc_008D8107:
    local_rbx = (local_rbx) | (-1);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 1176, Arg2, Arg3, Arg4);
    v_stack_mF8 = result;
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = Arg1 + 1176;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1 + 1176;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_mF8;
    }
    if (Arg1 != NULL) {
        *(uint8_t *)(arg1 + 0xA) = 1;
    }
    result = EtwpCovSampContextFastFindModule(Arg1, v_stack_mB0, Arg6, Arg4);
    if (result == 0) goto loc_008D81CE;
    if (result != (*(uint64_t *)(arg6))) goto loc_008D81CE;
    result = ProcessForExeModule(Arg1, v_stack_p18, *(uint64_t *)(arg6), (uint32_t)(v_stack_m100));
    result = 17;
    if (result != (*(uint64_t *)(arg6))) {
        Arg1 = Arg1 + 1176;
        result = ExfReleasePushLockShared(Arg1, v_stack_p18, *(uint64_t *)(arg6), (uint32_t)(v_stack_m100));
    }
    result = KeAbPostRelease(Arg1 + 1176, v_stack_p18, *(uint64_t *)(arg6), (uint32_t)(v_stack_m100));
    result = KeLeaveCriticalRegion(Arg1 + 1176, v_stack_p18, *(uint64_t *)(arg6), (uint32_t)(v_stack_m100));
    v_stack_m108 = 0;
loc_008D81C6:
    goto loc_008D8E19;
loc_008D81CE:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4AC))) >> (5));
    v_stack_mB8 = (uint32_t)(result);
    Arg1 = (uint32_t)(*(uint32_t *)(arg1 + 0x4A8));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4A8)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4B8))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4B8))); }
    v_stack_mC0 = (uint32_t)(Arg1);
    result = 17;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4A8)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4B8))))) {
        Arg1 = Arg1 + 1176;
        result = ExfReleasePushLockShared(Arg1, v_stack_p18, *(uint64_t *)(arg6), (uint32_t)(v_stack_m100));
    }
    result = KeAbPostRelease(Arg1 + 1176, v_stack_p18, *(uint64_t *)(arg6), (uint32_t)(v_stack_m100));
    result = KeLeaveCriticalRegion(Arg1 + 1176, v_stack_p18, *(uint64_t *)(arg6), (uint32_t)(v_stack_m100));
    result = ExAllocatePool2(176 + 80, 176, (uint32_t)(0x56777445ULL), (uint32_t)(v_stack_m100));
    if (result != 0) goto loc_008D8239;
    v_stack_m108 = 0xC000009AULL;
    goto loc_008D81C6;
loc_008D8239:
    Arg2 = 0;
    result = memset(result, Arg2, 176, (uint32_t)(v_stack_m100));
    *(uint64_t *)(result + 0x48 + 0x8) = result + 72;
    *(uint64_t *)(result + 0x48) = result + 72;
    *(uint64_t *)(result + 0x58 + 0x8) = result + 88;
    *(uint64_t *)(result + 0x58) = result + 88;
    *(uint64_t *)(result) = 0;
    *(uint64_t *)(result + 0x10) = 0;
    *(uint64_t *)(result + 0x40) = 0;
    *(uint64_t *)(result + 0x8) = v_stack_mB0;
    *(uint64_t *)(result + 0x28) = v_stack_mA8;
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(v_stack_mA0));
    *(uint32_t *)(result + 0x24) = (uint32_t)((uint32_t)(v_stack_m9C));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5 + 0x8))) << (9));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x78)))));
    Arg1 = (uint32_t)((Arg1) & (0x20000ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x78)))));
    *(uint32_t *)(result + 0x78) = (uint32_t)(Arg1);
    v_stack_m80 = 0;
    v_stack_m78 = 0;
    v_stack_mC8 = 0;
    v_stack_mF8 = v_stack_m80;
    v_stack_mF0 = 0;
    result = EtwpFindDebugId(*(uint64_t *)(arg5 + 0x10), v_stack_mA8, result + 48, result + 56);
    v_stack_m108 = (uint32_t)(result);
    if (sign_flag) goto loc_008D8315;
    if ((*(uint32_t *)(result + 0x38)) <= 0x400ULL) goto loc_008D8328;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(result + 0x30), Arg2, result + 48, result + 56);
    *(uint64_t *)(result + 0x30) = 0;
    *(uint32_t *)(result + 0x38) = 0;
loc_008D8315:
    v_stack_mF0 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m100)) != 0) goto loc_008D8338;
    goto loc_008D83CE;
loc_008D8328:
    v_stack_mC8 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m100) + 0x14)));
    result = ((uint32_t)(v_stack_m100)) + (4);
    v_stack_mF8 = result;
loc_008D8338:
    result = EtwpCovSampModuleGetName(result, Arg5, v_stack_p20, result + 56);
    v_stack_m108 = (uint32_t)(result);
    if (sign_flag) goto loc_008D81C6;
    v_stack_m90 = *(uint64_t *)(result + 0x70);
    v_stack_m88 = (uint16_t)((uint32_t)(*(uint32_t *)(result + 0x78)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x658))) == 0) goto loc_008D839B;
    result = EtwpCovSampCheckForSegments(v_stack_m90, Arg1 + 1304, (uint32_t)(*(uint32_t *)(arg1 + 0x658)), result + 56);
    goto loc_008D839F;
loc_008D839B:
loc_008D839F:
    if ((uint32_t)((uint32_t)(v_stack_mF0)) == 0) goto loc_008D83CA;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x65C))) != 0) {
        Arg2 = Arg1 + 1464;
        Arg1 = v_stack_m90;
        result = EtwpCovSampCheckForSegments(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x65C)), result + 56);
        Arg1 = 0;
        Arg1 = ((uint32_t)(result) == 0) ? 1 : 0;
    }
loc_008D83CE:
    if ((uint32_t)(Arg1) != 0) goto loc_008D83DA;
    if ((uint32_t)((uint32_t)(v_stack_m100)) == 0) goto loc_008D84A0;
loc_008D83DA:
    Arg1 = (uint32_t)((Arg1) << (16));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x78)))));
    Arg1 = (uint32_t)((Arg1) & (0x10000ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x78)))));
    *(uint32_t *)(result + 0x78) = (uint32_t)(Arg1);
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24)));
    v_stack_p2C = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20)));
    result = EtwCovSampHash(Arg5, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC)))), (uint32_t)(*(uint32_t *)(arg1 + 0x65C)), result + 56);
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28)));
    v_stack_p2C = (uint32_t)((uint32_t)(v_stack_mC8));
    v_stack_m50 = v_xmm0;
    result = EtwCovSampHash(Arg5, result, (uint32_t)(*(uint32_t *)(arg1 + 0x65C)), result + 56);
    result = EtwCovSampHash(Arg5, result, (uint32_t)(*(uint32_t *)(arg1 + 0x65C)), result + 56);
    result = EtwCovSampHash(Arg5, result, (uint32_t)(*(uint32_t *)(arg1 + 0x65C)), result + 56);
    v_stack_p28 = result;
    result = (result) >> (32);
    result = (uint32_t)((result) ^ (Arg5));
    if (condition_is_equal) { result = 0; }
    if (v_stack_m100 == 0) {
        Arg1 = v_stack_p18;
        result = (uint32_t)((result) ^ (*(uint32_t *)(arg1 + 0x28)));
    }
    *(uint32_t *)(result + 0x7C) = (uint32_t)(result);
loc_008D84A0:
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mB8)) + ((uint32_t)((uint32_t)(v_stack_mB8))));
    result = (uint32_t)(((uint32_t)(v_stack_mC0)) + 1);
    local_r12 = 0;
    if (((uint32_t)(result)) >= = ((uint32_t)(Arg2))) {
        local_r12 = (uint32_t)(Arg2);
        result = 128;
        if ((uint32_t)(Arg2) == 0) { local_r12 = (uint32_t)(result); }
        Arg2 = local_r12 + local_r12 * 1;
        Arg2 = (Arg2) << (3);
        Arg1 = 256;
        Arg3 = 0x56777445ULL;
        result = ExAllocatePool2(Arg1, Arg2, Arg3, result + 56);
        v_stack_mE8 = result;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 1176, Arg2, Arg3, result + 56);
    v_stack_p28 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 1176;
        Arg2 = result;
        Arg1 = Arg1 + 1176;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, result + 56);
        result = Arg5;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 0;
    }
    *(uint64_t *)(arg1 + 0x4A0) = *(uint64_t *)(gs_base + (0 + 0x188));
    if (v_stack_mE8 == 0) goto loc_008D8819;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4AC))) >> (5));
    if (((uint32_t)(local_r12)) <= ((uint32_t)(result))) goto loc_008D8819;
    result = (uint32_t)((local_r12 - 1) & ((uint32_t)(local_r12)));
    v_stack_p28 = (uint32_t)(result);
    if (condition_is_equal) goto loc_008D858C;
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    if ((uint32_t)(local_r12) == 0) goto loc_008D8586;
loc_008D857F:
    Arg1 = (uint32_t)((Arg1) + (0));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) >> (1));
    if (condition_is_not_equal) goto loc_008D857F;
loc_008D8586:
    Arg3 = (uint32_t)((0) << ((uint8_t)(Arg1)));
loc_008D858C:
    if (((uint32_t)(Arg3)) > ((uint32_t)((uint32_t)(0x4000000ULL)))) { Arg3 = (uint32_t)((uint32_t)(0x4000000ULL)); }
    result = (Arg1 + 1208) | (0);
    Arg1 = (uint32_t)((uint32_t)(Arg3));
    if ((v_stack_mE8 + (uint32_t)((uint32_t)(local_r12)) * 8) > (v_stack_mE8 + (uint32_t)((uint32_t)(local_r12)) * 8 + Arg3 * 8)) { Arg1 = 0; }
    local_rdi = v_stack_mE8;
    if (Arg1 != NULL) {
        local_rdi = v_stack_mE8 + (uint32_t)((uint32_t)(local_r12)) * 8;
        local_rdi = v_stack_mE8;
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4B8 + 0x4))))) & (31));
    result = (local_rbx) << ((uint8_t)(Arg1));
    v_stack_mC0 = result;
    if (condition_is_below_or_equal) goto loc_008D86B8;
loc_008D85E6:
    v_stack_mF8 = *(uint64_t *)(arg1 + 0x4B8 + 0x8);
loc_008D85EF:
    v_stack_mB8 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x4B8 + 0x8) + 0x0 * 8);
    if (((0) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4B8 + 0x8) + 0x0 * 8)))) != 0) goto loc_008D86A3;
    *(uint64_t *)(v_stack_mF8 + 0x0 * 8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4B8 + 0x8) + 0x0 * 8));
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4B8 + 0x8) + 0x0 * 8) + 0x8)) & (v_stack_mC0);
    v_stack_mD8 = result;
    result = ((uint8_t)(result)) + (0xB15DCBULL);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x4B8 + 0x8) + 0x0 * 8)) * (result);
    Arg1 = (Arg1) + (v_stack_mD7);
    Arg2 = (0) * (Arg1);
    Arg2 = (Arg2) + (v_stack_mD6);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_mD5);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_mD4);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_mD3);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_mD2);
    Arg2 = (Arg2) * (Arg2);
    result = (v_stack_mD1) + (Arg2);
    Arg1 = (Arg3 - 1) & ((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(v_stack_mB8) = *(uint64_t *)(v_stack_mE8 + (uint32_t)((uint32_t)(local_r12)) * 8 + arg1 * 8);
    *(uint64_t *)(v_stack_mE8 + (uint32_t)((uint32_t)(local_r12)) * 8 + arg1 * 8) = v_stack_mB8;
    goto loc_008D85EF;
loc_008D86A3:
    local_r10 = (uint32_t)((0) + (0));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4B8 + 0x4))))) >> (5));
    if (((uint32_t)(local_r10)) < ((uint32_t)(result))) goto loc_008D85E6;
loc_008D86B8:
    *(uint64_t *)(arg1 + 0x4B8 + 0x8) = v_stack_mE8 + (uint32_t)((uint32_t)(local_r12)) * 8;
    Arg3 = (uint32_t)((Arg3) << (5));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4B8 + 0x4))) & (31));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(Arg2)));
    *(uint32_t *)(arg1 + 0x4B8 + 0x4) = (uint32_t)(Arg3);
    if (Arg5 == NULL) goto loc_008D86F0;
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    if ((uint32_t)(local_r12) == 0) goto loc_008D86EA;
loc_008D86E2:
    Arg1 = (uint32_t)((Arg1) + (0));
    local_r12 = (uint32_t)((local_r12) >> (1));
    if (condition_is_not_equal) goto loc_008D86E2;
loc_008D86EA:
    local_r12 = (uint32_t)((0) << ((uint8_t)(Arg1)));
loc_008D86F0:
    if (((uint32_t)(local_r12)) > ((uint32_t)((uint32_t)(0x4000000ULL)))) { local_r12 = (uint32_t)((uint32_t)(0x4000000ULL)); }
    result = (Arg1 + 1192) | (0);
    Arg1 = (uint32_t)((uint32_t)(local_r12));
    if (v_stack_mE8 > (v_stack_mE8 + local_r12 * 8)) { Arg1 = 0; }
    local_rdi = v_stack_mE8;
    if (Arg1 != NULL) {
        local_rdi = v_stack_mE8;
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4A8 + 0x4))))) & (31));
    local_r11 = (local_rbx) << ((uint8_t)(Arg1));
    if (condition_is_below_or_equal) goto loc_008D87FE;
loc_008D873B:
    v_stack_p28 = *(uint64_t *)(arg1 + 0x4A8 + 0x8);
loc_008D8747:
    if (((0) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4A8 + 0x8) + 0x0 * 8)))) != 0) goto loc_008D87E9;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x4A8 + 0x8) + 0x0 * 8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4A8 + 0x8) + 0x0 * 8));
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4A8 + 0x8) + 0x0 * 8) + 0x8)) & (local_r11);
    v_stack_mD0 = result;
    result = ((uint8_t)(result)) + (0xB15DCBULL);
    Arg1 = (0) * (result);
    Arg1 = (Arg1) + (v_stack_mCF);
    Arg2 = (*(uint64_t *)(arg1 + 0x4A8 + 0x8)) * (Arg1);
    Arg2 = (Arg2) + (v_stack_mCE);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_mCD);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_mCC);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_mCB);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_mCA);
    Arg2 = (Arg2) * (Arg2);
    result = (v_stack_mC9) + (Arg2);
    Arg1 = (local_r12 - 1) & ((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4A8 + 0x8) + 0x0 * 8)) = *(uint64_t *)(local_rdi + arg1 * 8);
    *(uint64_t *)(local_rdi + arg1 * 8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x4A8 + 0x8) + 0x0 * 8);
    goto loc_008D8747;
loc_008D87E9:
    Arg4 = (uint32_t)((0) + (0));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4A8 + 0x4))))) >> (5));
    if (((uint32_t)(Arg4)) < ((uint32_t)(result))) goto loc_008D873B;
loc_008D87FE:
    *(uint64_t *)(arg1 + 0x4A8 + 0x8) = local_rdi;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4A8 + 0x4))) & (31));
    local_r12 = (uint32_t)((local_r12) << (5));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(local_r12)));
    *(uint32_t *)(arg1 + 0x4A8 + 0x4) = (uint32_t)(Arg2);
    v_stack_mE8 = *(uint64_t *)(arg1 + 0x4A8 + 0x8);
loc_008D8819:
    if ((*(uint32_t *)(arg1 + 0x4AC)) >= 32) goto loc_008D883B;
    v_stack_m108 = 0xC000009AULL;
loc_008D8831:
    goto loc_008D8E19;
loc_008D883B:
    result = EtwpCovSampContextFastFindModule(Arg1, v_stack_mB0, Arg6, Arg4);
    if (result == 0) goto loc_008D8A5F;
    if (result != (*(uint64_t *)(arg6))) goto loc_008D8882;
    result = ProcessForExeModule(Arg1, v_stack_p18, *(uint64_t *)(arg6), (uint32_t)(v_stack_m100));
loc_008D887C:
    v_stack_m108 = 0;
    goto loc_008D8831;
loc_008D8882:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4AC))))) & (31));
    result = (local_rbx) << ((uint8_t)(Arg1));
    result = (result) & (*(uint64_t *)((uint32_t)(v_stack_m100) + 0x8));
    v_stack_p28 = result;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4AC))) >> (5));
    v_stack_m68 = result;
    result = ((uint8_t)(result)) + ((uint32_t)(0xB15DCBULL));
    Arg1 = (Arg1) * (result);
    Arg1 = (Arg1) + (v_stack_p29);
    Arg2 = (v_stack_p18) * (Arg1);
    Arg2 = (Arg2) + (v_stack_p2A);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_p2B);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_p2C);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_p2D);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_p2E);
    Arg2 = (Arg2) * (Arg2);
    result = (v_stack_p2F) + (Arg2);
    Arg1 = (local_rdi - 1) & ((uint32_t)((uint32_t)(result)));
    result = (*(uint64_t *)((uint32_t)(v_stack_m100))) & (local_r11);
    if (result == local_r11) {
        result = *(uint64_t *)(local_rsi);
    }
    if ((((uint8_t)(v_stack_mE8)) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4B0) + arg1 * 8)))) != 0) goto loc_008D896B;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x4B0) + arg1 * 8)) == ((uint32_t)(v_stack_m100))) goto loc_008D895C;
    goto loc_008D894A;
loc_008D895C:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4B0) + arg1 * 8)) = *(uint64_t *)((uint32_t)(v_stack_m100));
    goto loc_008D896E;
loc_008D896B:
loc_008D896E:
    *(uint64_t *)((uint32_t)(v_stack_m100)) = 0;
    if (*(uint64_t *)((uint32_t)(v_stack_m100) + 0x10) == 0) goto loc_008D8A5F;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4BC))))) & (31));
    result = (local_rbx) << ((uint8_t)(Arg1));
    result = (result) & (*(uint64_t *)((uint32_t)(v_stack_m100) + 0x10 + 0x8));
    v_stack_p28 = result;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4BC))) >> (5));
    v_stack_m60 = result;
    result = ((uint8_t)(result)) + ((uint32_t)(0xB15DCBULL));
    Arg1 = (Arg1) * (result);
    Arg1 = (Arg1) + (v_stack_p29);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x4B0) + arg1 * 8)) * (Arg1);
    Arg2 = (Arg2) + (v_stack_p2A);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_p2B);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_p2C);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_p2D);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_p2E);
    Arg2 = (Arg2) * (Arg2);
    result = (v_stack_p2F) + (Arg2);
    Arg1 = (local_rdi - 1) & ((uint32_t)((uint32_t)(result)));
    local_r10 = (*(uint64_t *)((uint32_t)(v_stack_m100) + 0x10)) & (local_r11);
    result = *(uint64_t *)(arg1 + 0x4C0);
    if (local_r10 == local_r11) {
        result = *(uint64_t *)(local_rsi);
    }
    if ((((uint8_t)(v_stack_mE8)) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C0) + arg1 * 8)))) != 0) goto loc_008D8A58;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C0) + arg1 * 8)) == ((uint32_t)(v_stack_m100) + 16)) goto loc_008D8A49;
    goto loc_008D8A37;
loc_008D8A49:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C0) + arg1 * 8)) = *(uint64_t *)((uint32_t)(v_stack_m100) + 0x10);
    goto loc_008D8A5B;
loc_008D8A58:
loc_008D8A5B:
    *(uint64_t *)((uint32_t)(v_stack_m100) + 0x10) = 0;
loc_008D8A5F:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m100)))) << (20));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x78))) | ((uint32_t)(result)));
    *(uint32_t *)(result + 0x78) = (uint32_t)(Arg1);
    *(uint32_t *)(result + 0x80) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x660)));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4AC))))) >> (5));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4AC))) & (31));
    result = (local_rbx) << ((uint8_t)(Arg1));
    result = (result) & (*(uint64_t *)(result + 0x8));
    v_stack_mE0 = result;
    result = ((uint8_t)(result)) + ((uint32_t)(0xB15DCBULL));
    Arg1 = (Arg1) * (result);
    Arg1 = (Arg1) + (v_stack_mDF);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C0) + arg1 * 8)) * (Arg1);
    Arg2 = (Arg2) + (v_stack_mDE);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_mDD);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_mDC);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_mDB);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_mDA);
    Arg1 = (Arg1) * (Arg2);
    result = (v_stack_mD9) + (Arg1);
    Arg2 = (local_rdi - 1) & ((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x4B0) + arg2 * 8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x4B0) + arg2 * 8) = result;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C8) + 0x8)) != (Arg1 + 1224)) {
        Arg1 = 3;
    }
    *(uint64_t *)(result + 0x48) = *(uint64_t *)(arg1 + 0x4C8);
    *(void **)(result + 0x48 + 0x8) = Arg1;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x4C8) + 0x8) = result + 72;
    *(uint64_t *)(arg1) = result + 72;
    *(uint32_t *)(result + 0x88) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x48)));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C8) + 0x8)) < (Arg1 + 1224)) goto loc_008D8B85;
    if ((uint32_t)((uint32_t)(v_stack_m100)) == 0) goto loc_008D8D9D;
loc_008D8B85:
    *(uint64_t *)(result + 0x18) = (uint32_t)(*(uint32_t *)(result + 0x7C));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4BC))))) & (31));
    Arg4 = (local_rbx) << ((uint8_t)(Arg1));
    local_rdi = (Arg4) & ((uint32_t)(*(uint32_t *)(result + 0x7C)));
    v_stack_p28 = local_rdi;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4BC))) >> (5));
    if ((uint32_t)(Arg3) == 0) goto loc_008D8C5D;
    v_stack_m58 = local_rdi;
    result = ((uint8_t)(local_rdi)) + ((uint32_t)(0xB15DCBULL));
    Arg1 = (Arg1) * (result);
    Arg1 = (Arg1) + (v_stack_p29);
    Arg2 = (*(uint64_t *)(arg1 + 0x4C8)) * (Arg1);
    Arg2 = (Arg2) + (v_stack_p2A);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_p2B);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_p2C);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_p2D);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_p2E);
    Arg2 = (Arg2) * (Arg2);
    result = (v_stack_p2F) + (Arg2);
    Arg1 = (Arg3 - 1) & ((uint32_t)((uint32_t)(result)));
loc_008D8C47:
    if ((((uint8_t)(v_stack_mE8)) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C0) + arg1 * 8)))) != 0) goto loc_008D8C5D;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C0) + arg1 * 8) + 0x8)) & (Arg4);
    if (local_rdi != result) goto loc_008D8C47;
    goto loc_008D8C60;
loc_008D8C5D:
loc_008D8C60:
    if (0 != 0) goto loc_008D8CF7;
    result = (*(uint64_t *)(result + 0x10 + 0x8)) & (Arg4);
    v_stack_m100 = result;
    result = ((uint8_t)(result)) + ((uint32_t)(0xB15DCBULL));
    Arg1 = (0) * (result);
    Arg1 = (Arg1) + (v_stack_mFF);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_mFE);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_mFD);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_mFC);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_mFB);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_mFA);
    Arg1 = (Arg1) * (Arg2);
    result = (v_stack_mF9) + (Arg1);
    Arg2 = (Arg3 - 1) & ((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x4C0) + arg2 * 8);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x4C0) + arg2 * 8) = result + 16;
    goto loc_008D8D66;
loc_008D8CF7:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x4C0) + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20))))) goto loc_008D8D24;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x4C0) + 0x14)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24))))) goto loc_008D8D24;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C0) + 0x18)) != (*(uint64_t *)(result + 0x28))) goto loc_008D8D24;
    result = EtwpCheckDebugInfoEqual(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4C0) + 0x20), *(uint64_t *)(result + 0x30), Arg3, Arg4);
    if ((uint32_t)(result) == 0) {
        *(uint32_t *)(result + 0x78) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x78)));
        *(uint32_t *)(result + 0x7C) = 0;
    }
    result = EtwpCovSampModuleNameInfoCleanup(result + 104, *(uint64_t *)(result + 0x30), Arg3, Arg4);
    *(uint64_t *)(result + 0x70) = 0;
    *(uint16_t *)(result + 0x78) = 0;
    if (*(uint64_t *)(result + 0x30) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(result + 0x30), Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(result + 0x30) = 0;
    *(uint32_t *)(result + 0x38) = 0;
loc_008D8D66:
    local_rdi = result + 16;
    if (((*(uint32_t *)(arg1 + 0x8)) & (0x400ULL)) != 0) {
        Arg4 = (uint32_t)((uint32_t)(v_stack_m100));
        Arg3 = result;
        local_rdi = v_stack_p18;
        Arg2 = local_rdi;
        Arg1 = Arg1;
        result = ProcessForExeModule(Arg1, Arg2, Arg3, Arg4);
        result = *(uint32_t *)(local_rdi + 0x28);
        *(uint32_t *)(result + 0xA0) = (uint32_t)(result);
        result = *(uint32_t *)(local_rdi + 0x2C);
        *(uint32_t *)(result + 0xA4) = (uint32_t)(result);
    }
    result = (v_stack_mE8) + (v_stack_mE8);
    if (result <= v_stack_mE8) {
        Arg1 = 14;
    }
    *(uint64_t *)(arg6) = result;
    *(uint64_t *)(arg1 + 0x4A0) = 0;
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg1 + 1176;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(Arg1 + 1176, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegion(Arg1 + 1176, Arg2, Arg3, Arg4);
    result = EtwpCovSampContextPruneModules(Arg1, Arg2, Arg3, Arg4);
    goto loc_008D887C;
loc_008D8E19:
    if ((*(uint64_t *)(arg1 + 0x4A0)) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_008D8E63;
    *(uint64_t *)(arg1 + 0x4A0) = 0;
    local_rbx = (uint8_t)((local_rbx) & (6));
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = Arg1 + 1176;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(Arg1 + 1176, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegion(Arg1 + 1176, Arg2, Arg3, Arg4);
loc_008D8E63:
    if (0 != 0) {
        *(uint64_t *)(0 + 0x40) = 0;
        Arg1 = 0;
        result = EtwpCovSampModuleCleanup(Arg1, Arg2, Arg3, Arg4);
        Arg2 = 0x56777445ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_mE8 != 0) {
        Arg2 = 0x56777445ULL;
        Arg1 = v_stack_mE8;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (240);
    return (uint32_t)(v_stack_m108);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x498` | `64` | `R` |
| `Arg1` | `+ 0x498` | `64` | `R/W` |
| `Arg1` | `+ 0x4A0` | `64` | `R` |
| `Arg1` | `+ 0x4A0` | `64` | `W` |
| `Arg1` | `+ 0x4A8` | `32` | `R` |
| `Arg1` | `+ 0x4A8` | `32` | `R/W` |
| `Arg1` | `+ 0x4A8` | `64` | `R` |
| `Arg1` | `+ 0x4AC` | `32` | `R` |
| `Arg1` | `+ 0x4B0` | `64` | `R` |
| `Arg1` | `+ 0x4B8` | `32` | `R` |
| `Arg1` | `+ 0x4B8` | `32` | `R/W` |
| `Arg1` | `+ 0x4B8` | `64` | `R` |
| `Arg1` | `+ 0x4BC` | `32` | `R` |
| `Arg1` | `+ 0x4C0` | `64` | `R` |
| `Arg1` | `+ 0x4C8` | `64` | `R` |
| `Arg1` | `+ 0x4D8` | `32` | `R/W` |
| `Arg1` | `+ 0x4DC` | `32` | `R/W` |
| `Arg1` | `+ 0x518` | `64` | `R` |
| `Arg1` | `+ 0x5B8` | `64` | `R` |
| `Arg1` | `+ 0x658` | `32` | `R` |
| `Arg1` | `+ 0x65C` | `32` | `R` |
| `Arg1` | `+ 0x660` | `32` | `R` |
| `Arg1` | `+ 0x660` | `32` | `R/W` |
| `Arg2` | `+ 0x12` | `32` | `R` |

추가 오프셋 7개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008D7FEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
