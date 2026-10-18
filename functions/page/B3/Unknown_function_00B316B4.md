# sub_00B316B4

- RVA: `0x00B316B4`–`0x00B32591` (길이 `3,805` bytes)
- VA: `0x0000000140B316B4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A715C`
- 디코드: `784`개 명령, `3,805/3,805` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **51**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00B31785` → [PspLockJobShared](../91/PspLockJobShared_function_0091A490.md) (function, `0x0091A490`)
- `0x00B3179F` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x00B317CA` → [PspQueryJobHierarchyProcessIdList](../91/PspQueryJobHierarchyProcessIdList_function_0091854C.md) (function, `0x0091854C`)
- `0x00B31821` → [PspLockJobShared](../91/PspLockJobShared_function_0091A490.md) (function, `0x0091A490`)
- `0x00B3187E` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x00B318C2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B31904` → [PspLockJobListShared](../A0/PspLockJobListShared_function_00A04428.md) (function, `0x00A04428`)
- `0x00B3190E` → [PspUnlockJobListShared](../9F/PspUnlockJobListShared_function_009FF588.md) (function, `0x009FF588`)
- `0x00B31922` → [PspLockJobMemoryLimitsShared](../91/PspLockJobMemoryLimitsShared_function_0091A394.md) (function, `0x0091A394`)
- `0x00B3198A` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00B31996` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00B319A8` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x00B319DA` → [PspLockJobShared](../91/PspLockJobShared_function_0091A490.md) (function, `0x0091A490`)
- `0x00B31A2F` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x00B31A47` → [PspLockJobShared](../91/PspLockJobShared_function_0091A490.md) (function, `0x0091A490`)
- `0x00B31ABB` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x00B31AEB` → [PspLockJobShared](../91/PspLockJobShared_function_0091A490.md) (function, `0x0091A490`)
- `0x00B31BCC` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x00B31BEB` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B31C65` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B31CC8` → [PspLockJobShared](../91/PspLockJobShared_function_0091A490.md) (function, `0x0091A490`)
- `0x00B31D28` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x00B31EF4` → [PsGetJobServerSilo](../../text/4C/PsGetJobServerSilo_function_004C2440.md) (function, `0x004C2440`)
- `0x00B31F04` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (function, `0x00443B30`)
- `0x00B31F76` → [MmQueryApiSetSchema](../../text/4C/MmQueryApiSetSchema_function_004C013C.md) (function, `0x004C013C`)
- `0x00B31F7E` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x00B31FC0` → [PsGetServerSiloServiceSessionId](../../text/45/PsGetServerSiloServiceSessionId_function_0045ED00.md) (function, `0x0045ED00`)
- `0x00B31FDE` → [PspGetJobSilo](../../text/41/PspGetJobSilo_function_00418670.md) (function, `0x00418670`)
- `0x00B31FF3` → [ObGetSiloRootDirectoryPath](../83/ObGetSiloRootDirectoryPath_function_0083CD74.md) (function, `0x0083CD74`)
- `0x00B3206B` → [RtlCopyToUser](../70/RtlCopyToUser_function_00705D68.md) (function, `0x00705D68`)
- `0x00B32072` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x00B32091` → [RtlCopyToUser](../70/RtlCopyToUser_function_00705D68.md) (function, `0x00705D68`)
- `0x00B32098` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x00B320E9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B32114` → [PsGetParentSilo](../A7/PsGetParentSilo_function_00A70760.md) (function, `0x00A70760`)
- `0x00B3211F` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (function, `0x00443B30`)
- `0x00B3214E` → [PspIsSiloInServerSilo](../../text/5E/PspIsSiloInServerSilo_function_005E2724.md) (function, `0x005E2724`)
- `0x00B321DE` → [PspLimitViolationRateControlToleranceLimitField](../A7/PspLimitViolationRateControlToleranceLimitField_function_00A7D628.md) (function, `0x00A7D628`)
- `0x00B322ED` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (function, `0x0048FDC0`)
- `0x00B322F9` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x00B3230D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B3239E` → [PspQueryJobHierarchyAccountingInformation](../91/PspQueryJobHierarchyAccountingInformation_function_0091864C.md) (function, `0x0091864C`)
- `0x00B323E5` → [PsGetJobServerSilo](../../text/4C/PsGetJobServerSilo_function_004C2440.md) (function, `0x004C2440`)
- `0x00B323F2` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (function, `0x00443B30`)
- `0x00B32407` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x00B32476` → [PspLockJobShared](../91/PspLockJobShared_function_0091A490.md) (function, `0x0091A490`)
- `0x00B324A5` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x00B324BD` → [PspLockJobShared](../91/PspLockJobShared_function_0091A490.md) (function, `0x0091A490`)
- `0x00B324EC` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x00B3251D` → [PspLockJobShared](../91/PspLockJobShared_function_0091A490.md) (function, `0x0091A490`)
- `0x00B32539` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B31B0C` → RVA `0x00FC7120` (`ALMOSTRO`; read)
- `0x00B31F47` → RVA `0x00E0A74C` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x00B318C2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B3198A` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00B31996` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00B31BEB` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00B31C65` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B31EF4` → [PsGetJobServerSilo](../../text/4C/PsGetJobServerSilo_function_004C2440.md) (`PAGE` → `.text`)
  - `0x00B31F04` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (`PAGE` → `.text`)
  - `0x00B31F76` → [MmQueryApiSetSchema](../../text/4C/MmQueryApiSetSchema_function_004C013C.md) (`PAGE` → `.text`)
  - `0x00B31F7E` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (`PAGE` → `.text`)
  - `0x00B31FC0` → [PsGetServerSiloServiceSessionId](../../text/45/PsGetServerSiloServiceSessionId_function_0045ED00.md) (`PAGE` → `.text`)
  - `0x00B31FDE` → [PspGetJobSilo](../../text/41/PspGetJobSilo_function_00418670.md) (`PAGE` → `.text`)
  - `0x00B32072` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x00B32098` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x00B320E9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B3211F` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (`PAGE` → `.text`)
  - `0x00B3214E` → [PspIsSiloInServerSilo](../../text/5E/PspIsSiloInServerSilo_function_005E2724.md) (`PAGE` → `.text`)
  - `0x00B322ED` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (`PAGE` → `.text`)
  - `0x00B322F9` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (`PAGE` → `.text`)
  - `0x00B3230D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B323E5` → [PsGetJobServerSilo](../../text/4C/PsGetJobServerSilo_function_004C2440.md) (`PAGE` → `.text`)
  - `0x00B323F2` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (`PAGE` → `.text`)
  - `0x00B32407` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **47**
  - `0x00B316D7` → [NtQueryInformationJobObject + 0xA82](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B316E2` → [NtQueryInformationJobObject + 0xA82](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B316EF` → [NtQueryInformationJobObject + 0x318](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B316F7` → [NtQueryInformationJobObject + 0xA82](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B316FD` → [NtQueryInformationJobObject + 0x77F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B3174A` → [NtQueryInformationJobObject + 0x826](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B3177A` → [NtQueryInformationJobObject + 0x826](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B317AC` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B317D6` → [NtQueryInformationJobObject + 0xCA9](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B317E1` → [NtQueryInformationJobObject + 0xCF0](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B317EA` → [NtQueryInformationJobObject + 0x8A2](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B318CC` → [NtQueryInformationJobObject + 0x82B](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B318F5` → [NtQueryInformationJobObject + 0x82B](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B318FF` → [NtQueryInformationJobObject + 0x821](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B3191B` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B319C0` → [NtQueryInformationJobObject + 0x987](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31A3C` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31AC8` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31C6F` → [NtQueryInformationJobObject + 0x82B](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31C95` → [NtQueryInformationJobObject + 0x82B](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31D35` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31D3F` → [NtQueryInformationJobObject + 0x821](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31D80` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31DA3` → [NtQueryInformationJobObject + 0x821](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31E38` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31EBD` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31EC8` → [NtQueryInformationJobObject + 0x44B](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31FAC` → [NtQueryInformationJobObject + 0x821](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31FD6` → [NtQueryInformationJobObject + 0x821](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B31FFC` → [NtQueryInformationJobObject + 0x821](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B320EF` → [NtQueryInformationJobObject + 0x82B](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B32162` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B32204` → [NtQueryInformationJobObject + 0x570](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B322DB` → [NtQueryInformationJobObject + 0x6F8](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B322E8` → [NtQueryInformationJobObject + 0x6F8](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B3231C` → [NtQueryInformationJobObject + 0x82B](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B32342` → [NtQueryInformationJobObject + 0x82B](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B323CB` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B323D5` → [NtQueryInformationJobObject + 0x821](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B32461` → [NtQueryInformationJobObject + 0x821](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B3246B` → [NtQueryInformationJobObject + 0x821](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B324B2` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B324F9` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B32512` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B32546` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B32563` → [NtQueryInformationJobObject + 0x81F](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)
  - `0x00B3258C` → [NtQueryInformationJobObject + 0x821](../9F/NtQueryInformationJobObject_function_009FB860.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B316B4  41 8B CE                        mov ecx, r14d
00B316B7  83 E9 03                        sub ecx, 3
00B316BA  74 38                           je 0x140b316f4
00B316BC  2B CA                           sub ecx, edx
00B316BE  74 34                           je 0x140b316f4
00B316C0  83 E9 06                        sub ecx, 6
00B316C3  74 2F                           je 0x140b316f4
00B316C5  83 E9 03                        sub ecx, 3
00B316C8  74 2A                           je 0x140b316f4
00B316CA  83 E9 11                        sub ecx, 0x11
00B316CD  74 25                           je 0x140b316f4
00B316CF  83 E9 06                        sub ecx, 6
00B316D2  74 20                           je 0x140b316f4
00B316D4  83 F9 01                        cmp ecx, 1
00B316D7  0F 85 05 AC EC FF               jne 0x1409fc2e2
00B316DD  8D 41 1F                        lea eax, [rcx + 0x1f]
00B316E0  3B D8                           cmp ebx, eax
00B316E2  0F 85 FA AB EC FF               jne 0x1409fc2e2
00B316E8  44 8B E8                        mov r13d, eax
00B316EB  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00B316EF  E9 84 A4 EC FF                  jmp 0x1409fbb78
00B316F4  41 3B DD                        cmp ebx, r13d
00B316F7  0F 82 E5 AB EC FF               jb 0x1409fc2e2
00B316FD  E9 DD A8 EC FF                  jmp 0x1409fbfdf
00B31702  83 EA 01                        sub edx, 1
00B31705  0F 84 A6 00 00 00               je 0x140b317b1
00B3170B  83 EA 01                        sub edx, 1
00B3170E  74 6F                           je 0x140b3177f
00B31710  83 FA 01                        cmp edx, 1
00B31713  0F 85 B7 0C 00 00               jne 0x140b323d0
00B31719  0F 57 C0                        xorps xmm0, xmm0
00B3171C  33 C0                           xor eax, eax
00B3171E  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
00B31726  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00B3172B  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00B31730  0F 11 00                        movups xmmword ptr [rax], xmm0
00B31733  0F 11 40 10                     movups xmmword ptr [rax + 0x10], xmm0
00B31737  F2 0F 10 84 24 50 01 00 00      movsd xmm0, qword ptr [rsp + 0x150]
00B31740  F2 0F 11 40 20                  movsd qword ptr [rax + 0x20], xmm0
00B31745  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00B3174A  E9 37 A9 EC FF                  jmp 0x1409fc086
00B3174F  8B D8                           mov ebx, eax
00B31751  83 64 24 70 00                  and dword ptr [rsp + 0x70], 0
00B31756  33 F6                           xor esi, esi
00B31758  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00B3175D  44 8B 6C 24 58                  mov r13d, dword ptr [rsp + 0x58]
00B31762  44 8B FE                        mov r15d, esi
00B31765  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00B3176D  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B31772  4C 8B A4 24 80 00 00 00         mov r12, qword ptr [rsp + 0x80]
00B3177A  E9 07 A9 EC FF                  jmp 0x1409fc086
00B3177F  48 8B D1                        mov rdx, rcx
00B31782  48 8B CF                        mov rcx, rdi
00B31785  E8 06 8D DE FF                  call 0x14091a490
00B3178A  8B 87 20 02 00 00               mov eax, dword ptr [rdi + 0x220]
00B31790  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
00B31797  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00B3179C  48 8B CF                        mov rcx, rdi
00B3179F  E8 5C 86 DE FF                  call 0x140919e00
00B317A4  4C 8D BC 24 B0 00 00 00         lea r15, [rsp + 0xb0]
00B317AC  E9 CE A8 EC FF                  jmp 0x1409fc07f
00B317B1  89 74 24 70                     mov dword ptr [rsp + 0x70], esi
00B317B5  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
00B317BA  44 8B 44 24 6C                  mov r8d, dword ptr [rsp + 0x6c]
00B317BF  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00B317C4  49 8B D6                        mov rdx, r14
00B317C7  48 8B CF                        mov rcx, rdi
00B317CA  E8 7D 6D DE FF                  call 0x14091854c
00B317CF  8B D8                           mov ebx, eax
00B317D1  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00B317D6  E9 2E AD EC FF                  jmp 0x1409fc509
00B317DB  41 8B D6                        mov edx, r14d
00B317DE  83 EA 08                        sub edx, 8
00B317E1  0F 84 69 AD EC FF               je 0x1409fc550
00B317E7  83 EA 01                        sub edx, 1
00B317EA  0F 84 12 A9 EC FF               je 0x1409fc102
00B317F0  83 EA 01                        sub edx, 1
00B317F3  0F 84 0B 01 00 00               je 0x140b31904
00B317F9  83 FA 01                        cmp edx, 1
00B317FC  0F 85 CE 0B 00 00               jne 0x140b323d0
00B31802  48 39 74 24 50                  cmp qword ptr [rsp + 0x50], rsi
00B31807  0F 84 ED 00 00 00               je 0x140b318fa
00B3180D  44 8B 74 24 6C                  mov r14d, dword ptr [rsp + 0x6c]
00B31812  45 84 F4                        test r12b, r14b
00B31815  0F 85 DF 00 00 00               jne 0x140b318fa
00B3181B  48 8B D1                        mov rdx, rcx
00B3181E  48 8B CF                        mov rcx, rdi
00B31821  E8 6A 8C DE FF                  call 0x14091a490
00B31826  44 8B EE                        mov r13d, esi
00B31829  44 0F B7 8F 08 01 00 00         movzx r9d, word ptr [rdi + 0x108]
00B31831  66 41 3B F1                     cmp si, r9w
00B31835  73 3F                           jae 0x140b31876
00B31837  48 8D 8F 10 01 00 00            lea rcx, [rdi + 0x110]
00B3183E  0F B7 C6                        movzx eax, si
00B31841  0F B7 D6                        movzx edx, si
00B31844  44 0F B7 44 24 68               movzx r8d, word ptr [rsp + 0x68]
00B3184A  48 39 31                        cmp qword ptr [rcx], rsi
00B3184D  74 12                           je 0x140b31861
00B3184F  41 8B C5                        mov eax, r13d
00B31852  66 44 89 84 44 30 0A 00 00      mov word ptr [rsp + rax*2 + 0xa30], r8w
00B3185B  45 03 EC                        add r13d, r12d
00B3185E  0F B7 C2                        movzx eax, dx
00B31861  66 41 03 C4                     add ax, r12w
00B31865  44 0F B7 C0                     movzx r8d, ax
00B31869  48 83 C1 08                     add rcx, 8
00B3186D  0F B7 D0                        movzx edx, ax
00B31870  66 41 3B C1                     cmp ax, r9w
00B31874  72 D4                           jb 0x140b3184a
00B31876  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00B3187B  48 8B CF                        mov rcx, rdi
00B3187E  E8 7D 85 DE FF                  call 0x140919e00
00B31883  45 03 ED                        add r13d, r13d
00B31886  44 89 6C 24 70                  mov dword ptr [rsp + 0x70], r13d
00B3188B  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00B31890  45 3B F5                        cmp r14d, r13d
00B31893  1B DB                           sbb ebx, ebx
00B31895  81 E3 23 00 00 C0               and ebx, 0xc0000023
00B3189B  45 3B EE                        cmp r13d, r14d
00B3189E  44 0F 47 AC 24 8C 00 00 00      cmova r13d, dword ptr [rsp + 0x8c]
00B318A7  44 89 AC 24 8C 00 00 00         mov dword ptr [rsp + 0x8c], r13d
00B318AF  45 8B C5                        mov r8d, r13d
00B318B2  48 8D 94 24 30 0A 00 00         lea rdx, [rsp + 0xa30]
00B318BA  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00B318BF  49 8B CE                        mov rcx, r14
00B318C2  E8 79 4F B9 FF                  call 0x1406c6840
00B318C7  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00B318CC  E9 BA A7 EC FF                  jmp 0x1409fc08b
00B318D1  8B D8                           mov ebx, eax
00B318D3  33 F6                           xor esi, esi
00B318D5  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00B318DA  44 8B FE                        mov r15d, esi
00B318DD  44 8B AC 24 8C 00 00 00         mov r13d, dword ptr [rsp + 0x8c]
00B318E5  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
00B318ED  4C 8B A4 24 80 00 00 00         mov r12, qword ptr [rsp + 0x80]
00B318F5  E9 91 A7 EC FF                  jmp 0x1409fc08b
00B318FA  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00B318FF  E9 7D A7 EC FF                  jmp 0x1409fc081
00B31904  E8 1F 2B ED FF                  call 0x140a04428
00B31909  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00B3190E  E8 75 DC EC FF                  call 0x1409ff588
00B31913  4C 8D BC 24 D0 00 00 00         lea r15, [rsp + 0xd0]
00B3191B  E9 5F A7 EC FF                  jmp 0x1409fc07f
00B31920  33 D2                           xor edx, edx
00B31922  E8 6D 8A DE FF                  call 0x14091a394
00B31927  48 8B 8F B0 02 00 00            mov rcx, qword ptr [rdi + 0x2b0]
00B3192E  48 C1 E1 0C                     shl rcx, 0xc
00B31932  48 89 8C 24 90 04 00 00         mov qword ptr [rsp + 0x490], rcx
00B3193A  48 8B 8F B8 02 00 00            mov rcx, qword ptr [rdi + 0x2b8]
00B31941  48 C1 E1 0C                     shl rcx, 0xc
00B31945  48 89 8C 24 98 04 00 00         mov qword ptr [rsp + 0x498], rcx
00B3194D  48 8B 8F D0 02 00 00            mov rcx, qword ptr [rdi + 0x2d0]
00B31954  48 C1 E1 0C                     shl rcx, 0xc
00B31958  48 89 8C 24 A8 04 00 00         mov qword ptr [rsp + 0x4a8], rcx
00B31960  48 8B 8F C0 02 00 00            mov rcx, qword ptr [rdi + 0x2c0]
00B31967  48 C1 E1 0C                     shl rcx, 0xc
00B3196B  48 89 8C 24 B0 04 00 00         mov qword ptr [rsp + 0x4b0], rcx
00B31973  B8 11 00 00 00                  mov eax, 0x11
00B31978  F0 48 0F B1 B7 F0 04 00 00      lock cmpxchg qword ptr [rdi + 0x4f0], rsi
00B31981  74 0C                           je 0x140b3198f
00B31983  48 8D 8F F0 04 00 00            lea rcx, [rdi + 0x4f0]
00B3198A  E8 B1 1A 73 FF                  call 0x140263440
00B3198F  48 8D 8F F0 04 00 00            lea rcx, [rdi + 0x4f0]
00B31996  E8 65 FC 7A FF                  call 0x1402e1600
00B3199B  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00B319A0  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00B319A5  48 8B CF                        mov rcx, rdi
00B319A8  E8 53 84 DE FF                  call 0x140919e00
00B319AD  48 8B 87 C8 02 00 00            mov rax, qword ptr [rdi + 0x2c8]
00B319B4  48 C1 E0 0C                     shl rax, 0xc
00B319B8  48 89 84 24 A0 04 00 00         mov qword ptr [rsp + 0x4a0], rax
00B319C0  E9 22 A8 EC FF                  jmp 0x1409fc1e7
00B319C5  BB 07 00 00 00                  mov ebx, 7
00B319CA  33 C0                           xor eax, eax
00B319CC  66 89 84 24 F6 01 00 00         mov word ptr [rsp + 0x1f6], ax
00B319D4  48 8B D1                        mov rdx, rcx
00B319D7  48 8B CF                        mov rcx, rdi
00B319DA  E8 B1 8A DE FF                  call 0x14091a490
00B319DF  8B 8F 10 06 00 00               mov ecx, dword ptr [rdi + 0x610]
00B319E5  8B C1                           mov eax, ecx
00B319E7  C1 E8 09                        shr eax, 9
00B319EA  41 22 C4                        and al, r12b
00B319ED  88 84 24 F4 01 00 00            mov byte ptr [rsp + 0x1f4], al
00B319F4  C1 E9 13                        shr ecx, 0x13
00B319F7  41 22 CC                        and cl, r12b
00B319FA  88 8C 24 F5 01 00 00            mov byte ptr [rsp + 0x1f5], cl
00B31A01  8B 87 14 06 00 00               mov eax, dword ptr [rdi + 0x614]
00B31A07  F7 D0                           not eax
00B31A09  83 E0 08                        and eax, 8
00B31A0C  83 E3 F7                        and ebx, 0xfffffff7
00B31A0F  0B C3                           or eax, ebx
00B31A11  89 84 24 F0 01 00 00            mov dword ptr [rsp + 0x1f0], eax
00B31A18  48 8B 87 A0 04 00 00            mov rax, qword ptr [rdi + 0x4a0]
00B31A1F  48 89 84 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rax
00B31A27  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00B31A2C  48 8B CF                        mov rcx, rdi
00B31A2F  E8 CC 83 DE FF                  call 0x140919e00
00B31A34  4C 8D BC 24 F0 01 00 00         lea r15, [rsp + 0x1f0]
00B31A3C  E9 3E A6 EC FF                  jmp 0x1409fc07f
00B31A41  48 8B D1                        mov rdx, rcx
00B31A44  48 8B CF                        mov rcx, rdi
00B31A47  E8 44 8A DE FF                  call 0x14091a490
00B31A4C  48 8B 87 D8 04 00 00            mov rax, qword ptr [rdi + 0x4d8]
00B31A53  48 85 C0                        test rax, rax
00B31A56  74 5B                           je 0x140b31ab3
00B31A58  44 8B 48 28                     mov r9d, dword ptr [rax + 0x28]
00B31A5C  41 F6 C1 40                     test r9b, 0x40
00B31A60  75 51                           jne 0x140b31ab3
00B31A62  8B 40 2C                        mov eax, dword ptr [rax + 0x2c]
00B31A65  89 84 24 DC 00 00 00            mov dword ptr [rsp + 0xdc], eax
00B31A6C  41 8B C9                        mov ecx, r9d
00B31A6F  83 E1 04                        and ecx, 4
00B31A72  BB 02 00 00 00                  mov ebx, 2
00B31A77  0B CB                           or ecx, ebx
00B31A79  D1 E9                           shr ecx, 1
00B31A7B  8B D1                           mov edx, ecx
00B31A7D  83 CA 04                        or edx, 4
00B31A80  45 84 CC                        test r12b, r9b
00B31A83  0F 44 D1                        cmove edx, ecx
00B31A86  8B CA                           mov ecx, edx
00B31A88  83 C9 08                        or ecx, 8
00B31A8B  44 84 CB                        test bl, r9b
00B31A8E  0F 44 CA                        cmove ecx, edx
00B31A91  8B D1                           mov edx, ecx
00B31A93  83 CA 10                        or edx, 0x10
00B31A96  41 F6 C1 20                     test r9b, 0x20
00B31A9A  0F 44 D1                        cmove edx, ecx
00B31A9D  44 8D 43 7E                     lea r8d, [rbx + 0x7e]
00B31AA1  8B C2                           mov eax, edx
00B31AA3  83 C8 20                        or eax, 0x20
00B31AA6  45 84 C8                        test r8b, r9b
00B31AA9  0F 44 C2                        cmove eax, edx
00B31AAC  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
00B31AB3  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00B31AB8  48 8B CF                        mov rcx, rdi
00B31ABB  E8 40 83 DE FF                  call 0x140919e00
00B31AC0  4C 8D BC 24 D8 00 00 00         lea r15, [rsp + 0xd8]
00B31AC8  E9 B2 A5 EC FF                  jmp 0x1409fc07f
00B31ACD  48 39 74 24 50                  cmp qword ptr [rsp + 0x50], rsi
00B31AD2  0F 84 22 FE FF FF               je 0x140b318fa
00B31AD8  8B 5C 24 6C                     mov ebx, dword ptr [rsp + 0x6c]
00B31ADC  F6 C3 0F                        test bl, 0xf
00B31ADF  0F 85 15 FE FF FF               jne 0x140b318fa
00B31AE5  48 8B D1                        mov rdx, rcx
00B31AE8  48 8B CF                        mov rcx, rdi
00B31AEB  E8 A0 89 DE FF                  call 0x14091a490
00B31AF0  8B 87 00 01 00 00               mov eax, dword ptr [rdi + 0x100]
00B31AF6  41 B8 80 00 00 00               mov r8d, 0x80
00B31AFC  A8 10                           test al, 0x10
00B31AFE  41 8D 40 82                     lea eax, [r8 - 0x7e]
00B31B02  75 61                           jne 0x140b31b65
00B31B04  48 8D 8C 24 20 07 00 00         lea rcx, [rsp + 0x720]
00B31B0C  48 8D 15 0D 56 49 00            lea rdx, [rip + 0x49560d]
00B31B13  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00B31B16  0F 11 01                        movups xmmword ptr [rcx], xmm0
00B31B19  0F 10 4A 10                     movups xmm1, xmmword ptr [rdx + 0x10]
00B31B1D  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00B31B21  0F 10 42 20                     movups xmm0, xmmword ptr [rdx + 0x20]
00B31B25  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00B31B29  0F 10 4A 30                     movups xmm1, xmmword ptr [rdx + 0x30]
00B31B2D  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
00B31B31  0F 10 42 40                     movups xmm0, xmmword ptr [rdx + 0x40]
00B31B35  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
00B31B39  0F 10 4A 50                     movups xmm1, xmmword ptr [rdx + 0x50]
00B31B3D  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
00B31B41  0F 10 42 60                     movups xmm0, xmmword ptr [rdx + 0x60]
00B31B45  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
00B31B49  49 03 C8                        add rcx, r8
00B31B4C  0F 10 4A 70                     movups xmm1, xmmword ptr [rdx + 0x70]
00B31B50  0F 11 49 F0                     movups xmmword ptr [rcx - 0x10], xmm1
00B31B54  49 03 D0                        add rdx, r8
00B31B57  48 83 E8 01                     sub rax, 1
00B31B5B  75 B6                           jne 0x140b31b13
00B31B5D  48 8B 02                        mov rax, qword ptr [rdx]
00B31B60  48 89 01                        mov qword ptr [rcx], rax
00B31B63  EB 5F                           jmp 0x140b31bc4
00B31B65  48 8D 8F 08 01 00 00            lea rcx, [rdi + 0x108]
00B31B6C  48 8D 94 24 20 07 00 00         lea rdx, [rsp + 0x720]
00B31B74  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00B31B77  0F 11 02                        movups xmmword ptr [rdx], xmm0
00B31B7A  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
00B31B7E  0F 11 4A 10                     movups xmmword ptr [rdx + 0x10], xmm1
00B31B82  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
00B31B86  0F 11 42 20                     movups xmmword ptr [rdx + 0x20], xmm0
00B31B8A  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
00B31B8E  0F 11 4A 30                     movups xmmword ptr [rdx + 0x30], xmm1
00B31B92  0F 10 41 40                     movups xmm0, xmmword ptr [rcx + 0x40]
00B31B96  0F 11 42 40                     movups xmmword ptr [rdx + 0x40], xmm0
00B31B9A  0F 10 49 50                     movups xmm1, xmmword ptr [rcx + 0x50]
00B31B9E  0F 11 4A 50                     movups xmmword ptr [rdx + 0x50], xmm1
00B31BA2  0F 10 41 60                     movups xmm0, xmmword ptr [rcx + 0x60]
00B31BA6  0F 11 42 60                     movups xmmword ptr [rdx + 0x60], xmm0
00B31BAA  49 03 D0                        add rdx, r8
00B31BAD  0F 10 49 70                     movups xmm1, xmmword ptr [rcx + 0x70]
00B31BB1  0F 11 4A F0                     movups xmmword ptr [rdx - 0x10], xmm1
00B31BB5  49 03 C8                        add rcx, r8
00B31BB8  48 83 E8 01                     sub rax, 1
00B31BBC  75 B6                           jne 0x140b31b74
00B31BBE  48 8B 01                        mov rax, qword ptr [rcx]
00B31BC1  48 89 02                        mov qword ptr [rdx], rax
00B31BC4  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00B31BC9  48 8B CF                        mov rcx, rdi
00B31BCC  E8 2F 82 DE FF                  call 0x140919e00
00B31BD1  44 0F B7 B4 24 20 07 00 00      movzx r14d, word ptr [rsp + 0x720]
00B31BDA  45 8B C6                        mov r8d, r14d
00B31BDD  49 C1 E0 04                     shl r8, 4
00B31BE1  33 D2                           xor edx, edx
00B31BE3  48 8D 8C 24 30 08 00 00         lea rcx, [rsp + 0x830]
00B31BEB  E8 50 50 B9 FF                  call 0x1406c6c40
00B31BF0  66 41 3B F6                     cmp si, r14w
00B31BF4  73 37                           jae 0x140b31c2d
00B31BF6  48 8D 94 24 30 08 00 00         lea rdx, [rsp + 0x830]
00B31BFE  4C 8D 84 24 28 07 00 00         lea r8, [rsp + 0x728]
00B31C06  0F B7 CE                        movzx ecx, si
00B31C09  0F B7 44 24 68                  movzx eax, word ptr [rsp + 0x68]
00B31C0E  66 89 42 08                     mov word ptr [rdx + 8], ax
00B31C12  49 8B 00                        mov rax, qword ptr [r8]
00B31C15  48 89 02                        mov qword ptr [rdx], rax
00B31C18  66 41 03 CC                     add cx, r12w
00B31C1C  0F B7 C1                        movzx eax, cx
00B31C1F  4D 8D 40 08                     lea r8, [r8 + 8]
00B31C23  48 8D 52 10                     lea rdx, [rdx + 0x10]
00B31C27  66 41 3B CE                     cmp cx, r14w
00B31C2B  72 E1                           jb 0x140b31c0e
00B31C2D  41 8B C6                        mov eax, r14d
00B31C30  C1 E0 04                        shl eax, 4
00B31C33  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00B31C37  44 8B E8                        mov r13d, eax
00B31C3A  3B D8                           cmp ebx, eax
00B31C3C  44 0F 42 EB                     cmovb r13d, ebx
00B31C40  44 89 6C 24 58                  mov dword ptr [rsp + 0x58], r13d
00B31C45  1B DB                           sbb ebx, ebx
00B31C47  81 E3 23 00 00 C0               and ebx, 0xc0000023
00B31C4D  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00B31C52  45 8B C5                        mov r8d, r13d
00B31C55  48 8D 94 24 30 08 00 00         lea rdx, [rsp + 0x830]
00B31C5D  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00B31C62  49 8B CE                        mov rcx, r14
00B31C65  E8 D6 4B B9 FF                  call 0x1406c6840
00B31C6A  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00B31C6F  E9 17 A4 EC FF                  jmp 0x1409fc08b
00B31C74  8B D8                           mov ebx, eax
00B31C76  33 F6                           xor esi, esi
00B31C78  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00B31C7D  44 8B 6C 24 58                  mov r13d, dword ptr [rsp + 0x58]
00B31C82  44 8B FE                        mov r15d, esi
00B31C85  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
00B31C8D  4C 8B A4 24 80 00 00 00         mov r12, qword ptr [rsp + 0x80]
00B31C95  E9 F1 A3 EC FF                  jmp 0x1409fc08b
00B31C9A  41 83 EE 01                     sub r14d, 1
00B31C9E  0F 84 E1 00 00 00               je 0x140b31d85
00B31CA4  41 83 EE 01                     sub r14d, 1
00B31CA8  0F 84 96 00 00 00               je 0x140b31d44
00B31CAE  41 83 EE 01                     sub r14d, 1
00B31CB2  0F 84 82 00 00 00               je 0x140b31d3a
00B31CB8  41 83 FE 01                     cmp r14d, 1
00B31CBC  0F 85 0E 07 00 00               jne 0x140b323d0
00B31CC2  48 8B D1                        mov rdx, rcx
00B31CC5  48 8B CF                        mov rcx, rdi
00B31CC8  E8 C3 87 DE FF                  call 0x14091a490
00B31CCD  48 8B 8F 08 06 00 00            mov rcx, qword ptr [rdi + 0x608]
00B31CD4  48 85 C9                        test rcx, rcx
00B31CD7  74 47                           je 0x140b31d20
00B31CD9  44 89 A4 24 D8 01 00 00         mov dword ptr [rsp + 0x1d8], r12d
00B31CE1  8B 51 30                        mov edx, dword ptr [rcx + 0x30]
00B31CE4  41 84 D4                        test r12b, dl
00B31CE7  74 18                           je 0x140b31d01
00B31CE9  45 8D 66 02                     lea r12d, [r14 + 2]
00B31CED  44 89 A4 24 D8 01 00 00         mov dword ptr [rsp + 0x1d8], r12d
00B31CF5  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00B31CF9  48 89 84 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rax
00B31D01  BB 02 00 00 00                  mov ebx, 2
00B31D06  84 D3                           test bl, dl
00B31D08  74 16                           je 0x140b31d20
00B31D0A  41 83 CC 04                     or r12d, 4
00B31D0E  44 89 A4 24 D8 01 00 00         mov dword ptr [rsp + 0x1d8], r12d
00B31D16  8A 41 40                        mov al, byte ptr [rcx + 0x40]
00B31D19  88 84 24 DC 01 00 00            mov byte ptr [rsp + 0x1dc], al
00B31D20  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00B31D25  48 8B CF                        mov rcx, rdi
00B31D28  E8 D3 80 DE FF                  call 0x140919e00
00B31D2D  4C 8D BC 24 D0 01 00 00         lea r15, [rsp + 0x1d0]
00B31D35  E9 45 A3 EC FF                  jmp 0x1409fc07f
00B31D3A  BB 02 00 00 C0                  mov ebx, 0xc0000002
00B31D3F  E9 3D A3 EC FF                  jmp 0x1409fc081
00B31D44  0F 10 87 C0 05 00 00            movups xmm0, xmmword ptr [rdi + 0x5c0]
00B31D4B  F3 0F 7F 84 24 F0 02 00 00      movdqu xmmword ptr [rsp + 0x2f0], xmm0
00B31D54  83 7C 24 6C 24                  cmp dword ptr [rsp + 0x6c], 0x24
00B31D59  75 1D                           jne 0x140b31d78
00B31D5B  0F 10 87 D0 05 00 00            movups xmm0, xmmword ptr [rdi + 0x5d0]
00B31D62  F3 0F 7F 84 24 00 03 00 00      movdqu xmmword ptr [rsp + 0x300], xmm0
00B31D6B  8B 87 BC 05 00 00               mov eax, dword ptr [rdi + 0x5bc]
00B31D71  89 84 24 10 03 00 00            mov dword ptr [rsp + 0x310], eax
00B31D78  4C 8D BC 24 F0 02 00 00         lea r15, [rsp + 0x2f0]
00B31D80  E9 FA A2 EC FF                  jmp 0x1409fc07f
00B31D85  48 8B 87 20 06 00 00            mov rax, qword ptr [rdi + 0x620]
00B31D8C  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
00B31D94  4C 8D BC 24 E8 00 00 00         lea r15, [rsp + 0xe8]
00B31D9C  8B DE                           mov ebx, esi
00B31D9E  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00B31DA3  E9 D9 A2 EC FF                  jmp 0x1409fc081
00B31DA8  89 B4 24 C4 02 00 00            mov dword ptr [rsp + 0x2c4], esi
00B31DAF  48 8B 84 24 00 02 00 00         mov rax, qword ptr [rsp + 0x200]
00B31DB7  48 89 84 24 90 02 00 00         mov qword ptr [rsp + 0x290], rax
00B31DBF  48 8B 84 24 08 02 00 00         mov rax, qword ptr [rsp + 0x208]
00B31DC7  48 89 84 24 98 02 00 00         mov qword ptr [rsp + 0x298], rax
00B31DCF  48 8B 84 24 10 02 00 00         mov rax, qword ptr [rsp + 0x210]
00B31DD7  48 89 84 24 A0 02 00 00         mov qword ptr [rsp + 0x2a0], rax
00B31DDF  48 8B 84 24 30 02 00 00         mov rax, qword ptr [rsp + 0x230]
00B31DE7  48 89 84 24 A8 02 00 00         mov qword ptr [rsp + 0x2a8], rax
00B31DEF  48 8B 84 24 18 02 00 00         mov rax, qword ptr [rsp + 0x218]
00B31DF7  48 89 84 24 B0 02 00 00         mov qword ptr [rsp + 0x2b0], rax
00B31DFF  8B 84 24 20 02 00 00            mov eax, dword ptr [rsp + 0x220]
00B31E06  89 84 24 B8 02 00 00            mov dword ptr [rsp + 0x2b8], eax
00B31E0D  8B 84 24 24 02 00 00            mov eax, dword ptr [rsp + 0x224]
00B31E14  89 84 24 BC 02 00 00            mov dword ptr [rsp + 0x2bc], eax
00B31E1B  8B 84 24 28 02 00 00            mov eax, dword ptr [rsp + 0x228]
00B31E22  B9 04 82 27 00                  mov ecx, 0x278204
00B31E27  23 C1                           and eax, ecx
00B31E29  89 84 24 C0 02 00 00            mov dword ptr [rsp + 0x2c0], eax
00B31E30  4C 8D BC 24 90 02 00 00         lea r15, [rsp + 0x290]
00B31E38  E9 42 A2 EC FF                  jmp 0x1409fc07f
00B31E3D  89 B4 24 8C 02 00 00            mov dword ptr [rsp + 0x28c], esi
00B31E44  48 8B 84 24 00 02 00 00         mov rax, qword ptr [rsp + 0x200]
00B31E4C  48 89 84 24 60 02 00 00         mov qword ptr [rsp + 0x260], rax
00B31E54  48 8B 84 24 08 02 00 00         mov rax, qword ptr [rsp + 0x208]
00B31E5C  48 89 84 24 68 02 00 00         mov qword ptr [rsp + 0x268], rax
00B31E64  48 8B 84 24 10 02 00 00         mov rax, qword ptr [rsp + 0x210]
00B31E6C  48 89 84 24 70 02 00 00         mov qword ptr [rsp + 0x270], rax
00B31E74  48 8B 84 24 18 02 00 00         mov rax, qword ptr [rsp + 0x218]
00B31E7C  48 89 84 24 78 02 00 00         mov qword ptr [rsp + 0x278], rax
00B31E84  8B 84 24 20 02 00 00            mov eax, dword ptr [rsp + 0x220]
00B31E8B  89 84 24 80 02 00 00            mov dword ptr [rsp + 0x280], eax
00B31E92  8B 84 24 24 02 00 00            mov eax, dword ptr [rsp + 0x224]
00B31E99  89 84 24 84 02 00 00            mov dword ptr [rsp + 0x284], eax
00B31EA0  8B 84 24 28 02 00 00            mov eax, dword ptr [rsp + 0x228]
00B31EA7  B9 04 02 07 00                  mov ecx, 0x70204
00B31EAC  23 C1                           and eax, ecx
00B31EAE  89 84 24 88 02 00 00            mov dword ptr [rsp + 0x288], eax
00B31EB5  4C 8D BC 24 60 02 00 00         lea r15, [rsp + 0x260]
00B31EBD  E9 BD A1 EC FF                  jmp 0x1409fc07f
00B31EC2  41 8B CE                        mov ecx, r14d
00B31EC5  83 E9 22                        sub ecx, 0x22
00B31EC8  0F 84 DD 9D EC FF               je 0x1409fbcab
00B31ECE  83 E9 02                        sub ecx, 2
00B31ED1  0F 84 1D 02 00 00               je 0x140b320f4
00B31ED7  83 E9 01                        sub ecx, 1
00B31EDA  0F 84 FB 00 00 00               je 0x140b31fdb
00B31EE0  83 F9 01                        cmp ecx, 1
00B31EE3  0F 85 E7 04 00 00               jne 0x140b323d0
00B31EE9  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00B31EF1  48 8B CF                        mov rcx, rdi
00B31EF4  E8 47 05 99 FF                  call 0x1404c2440
00B31EF9  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
00B31F01  48 8B CB                        mov rcx, rbx
00B31F04  E8 27 1C 91 FF                  call 0x140443b30
00B31F09  84 C0                           test al, al
00B31F0B  0F 85 96 00 00 00               jne 0x140b31fa7
00B31F11  48 8B 8B E0 05 00 00            mov rcx, qword ptr [rbx + 0x5e0]
00B31F18  8B 81 F8 04 00 00               mov eax, dword ptr [rcx + 0x4f8]
00B31F1E  89 84 24 0C 01 00 00            mov dword ptr [rsp + 0x10c], eax
00B31F25  8B 81 FC 04 00 00               mov eax, dword ptr [rcx + 0x4fc]
00B31F2B  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
00B31F32  40 88 B4 24 14 01 00 00         mov byte ptr [rsp + 0x114], sil
00B31F3A  8B 81 38 05 00 00               mov eax, dword ptr [rcx + 0x538]
00B31F40  89 84 24 28 01 00 00            mov dword ptr [rsp + 0x128], eax
00B31F47  8B 05 FF 87 2D 00               mov eax, dword ptr [rip + 0x2d87ff]
00B31F4D  0F B7 C0                        movzx eax, ax
00B31F50  89 84 24 2C 01 00 00            mov dword ptr [rsp + 0x12c], eax
00B31F57  40 38 74 24 5C                  cmp byte ptr [rsp + 0x5c], sil
00B31F5C  75 53                           jne 0x140b31fb1
00B31F5E  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
00B31F66  48 8D 94 24 A8 00 00 00         lea rdx, [rsp + 0xa8]
00B31F6E  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00B31F76  E8 C1 E1 98 FF                  call 0x1404c013c
00B31F7B  48 8B CB                        mov rcx, rbx
00B31F7E  E8 1D 31 6F FF                  call 0x1402250a0
00B31F83  48 8B 88 F0 03 00 00            mov rcx, qword ptr [rax + 0x3f0]
00B31F8A  48 89 8C 24 18 01 00 00         mov qword ptr [rsp + 0x118], rcx
00B31F92  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00B31F9A  48 8B 08                        mov rcx, qword ptr [rax]
00B31F9D  48 89 8C 24 20 01 00 00         mov qword ptr [rsp + 0x120], rcx
00B31FA5  EB 16                           jmp 0x140b31fbd
00B31FA7  BB 09 05 00 C0                  mov ebx, 0xc0000509
00B31FAC  E9 D0 A0 EC FF                  jmp 0x1409fc081
00B31FB1  0F 57 C0                        xorps xmm0, xmm0
00B31FB4  F3 0F 7F 84 24 18 01 00 00      movdqu xmmword ptr [rsp + 0x118], xmm0
00B31FBD  48 8B CB                        mov rcx, rbx
00B31FC0  E8 3B CD 92 FF                  call 0x14045ed00
00B31FC5  89 84 24 08 01 00 00            mov dword ptr [rsp + 0x108], eax
00B31FCC  8B DE                           mov ebx, esi
00B31FCE  4C 8D BC 24 08 01 00 00         lea r15, [rsp + 0x108]
00B31FD6  E9 A6 A0 EC FF                  jmp 0x1409fc081
00B31FDB  48 8B CF                        mov rcx, rdi
00B31FDE  E8 8D 66 8E FF                  call 0x140418670
00B31FE3  48 85 C0                        test rax, rax
00B31FE6  74 BF                           je 0x140b31fa7
00B31FE8  48 8D 94 24 F8 00 00 00         lea rdx, [rsp + 0xf8]
00B31FF0  48 8B C8                        mov rcx, rax
00B31FF3  E8 7C AD D0 FF                  call 0x14083cd74
00B31FF8  8B D8                           mov ebx, eax
00B31FFA  85 C0                           test eax, eax
00B31FFC  0F 88 7F A0 EC FF               js 0x1409fc081
00B32002  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00B32007  44 0F B7 A4 24 F8 00 00 00      movzx r12d, word ptr [rsp + 0xf8]
00B32010  45 8D 6C 24 10                  lea r13d, [r12 + 0x10]
00B32015  44 89 6C 24 58                  mov dword ptr [rsp + 0x58], r13d
00B3201A  44 3B 6C 24 6C                  cmp r13d, dword ptr [rsp + 0x6c]
00B3201F  0F 87 AB 00 00 00               ja 0x140b320d0
00B32025  0F 57 C0                        xorps xmm0, xmm0
00B32028  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
00B32030  66 44 89 A4 24 90 00 00 00      mov word ptr [rsp + 0x90], r12w
00B32039  66 44 89 A4 24 92 00 00 00      mov word ptr [rsp + 0x92], r12w
00B32042  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00B32047  49 8D 46 10                     lea rax, [r14 + 0x10]
00B3204B  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00B32053  41 B8 10 00 00 00               mov r8d, 0x10
00B32059  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00B32061  49 8B CE                        mov rcx, r14
00B32064  40 38 74 24 5C                  cmp byte ptr [rsp + 0x5c], sil
00B32069  74 07                           je 0x140b32072
00B3206B  E8 F8 3C BD FF                  call 0x140705d68
00B32070  EB 05                           jmp 0x140b32077
00B32072  E8 59 A9 B8 FF                  call 0x1406bc9d0
00B32077  4D 8B C4                        mov r8, r12
00B3207A  48 8B 94 24 00 01 00 00         mov rdx, qword ptr [rsp + 0x100]
00B32082  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00B3208A  40 38 74 24 5C                  cmp byte ptr [rsp + 0x5c], sil
00B3208F  74 07                           je 0x140b32098
00B32091  E8 D2 3C BD FF                  call 0x140705d68
00B32096  EB 05                           jmp 0x140b3209d
00B32098  E8 33 A9 B8 FF                  call 0x1406bc9d0
00B3209D  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00B320A2  4D 85 E4                        test r12, r12
00B320A5  74 04                           je 0x140b320ab
00B320A7  45 89 2C 24                     mov dword ptr [r12], r13d
00B320AB  EB 32                           jmp 0x140b320df
00B320AD  8B D8                           mov ebx, eax
00B320AF  33 F6                           xor esi, esi
00B320B1  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00B320B6  44 8B 6C 24 58                  mov r13d, dword ptr [rsp + 0x58]
00B320BB  44 8B FE                        mov r15d, esi
00B320BE  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
00B320C6  4C 8B A4 24 80 00 00 00         mov r12, qword ptr [rsp + 0x80]
00B320CE  EB 0F                           jmp 0x140b320df
00B320D0  BB 23 00 00 C0                  mov ebx, 0xc0000023
00B320D5  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00B320DA  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00B320DF  33 D2                           xor edx, edx
00B320E1  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
00B320E9  E8 82 07 05 00                  call 0x140b82870
00B320EE  90                              nop
00B320EF  E9 97 9F EC FF                  jmp 0x1409fc08b
00B320F4  F7 87 10 06 00 00 00 00 00 40   test dword ptr [rdi + 0x610], 0x40000000
00B320FE  0F 84 A3 FE FF FF               je 0x140b31fa7
00B32104  8B 87 BC 05 00 00               mov eax, dword ptr [rdi + 0x5bc]
00B3210A  89 84 24 E0 01 00 00            mov dword ptr [rsp + 0x1e0], eax
00B32111  48 8B CF                        mov rcx, rdi
00B32114  E8 47 E6 F3 FF                  call 0x140a70760
00B32119  48 8B D8                        mov rbx, rax
00B3211C  48 8B C8                        mov rcx, rax
00B3211F  E8 0C 1A 91 FF                  call 0x140443b30
00B32124  84 C0                           test al, al
00B32126  75 0F                           jne 0x140b32137
00B32128  8B 83 BC 05 00 00               mov eax, dword ptr [rbx + 0x5bc]
00B3212E  89 84 24 E4 01 00 00            mov dword ptr [rsp + 0x1e4], eax
00B32135  EB 07                           jmp 0x140b3213e
00B32137  89 B4 24 E4 01 00 00            mov dword ptr [rsp + 0x1e4], esi
00B3213E  8B 87 B0 05 00 00               mov eax, dword ptr [rdi + 0x5b0]
00B32144  89 84 24 E8 01 00 00            mov dword ptr [rsp + 0x1e8], eax
00B3214B  48 8B CF                        mov rcx, rdi
00B3214E  E8 D1 05 AB FF                  call 0x1405e2724
00B32153  88 84 24 EC 01 00 00            mov byte ptr [rsp + 0x1ec], al
00B3215A  4C 8D BC 24 E0 01 00 00         lea r15, [rsp + 0x1e0]
00B32162  E9 18 9F EC FF                  jmp 0x1409fc07f
00B32167  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
00B3216F  48 8B 41 50                     mov rax, qword ptr [rcx + 0x50]
00B32173  48 85 C0                        test rax, rax
00B32176  75 04                           jne 0x140b3217c
00B32178  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00B3217C  48 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], rax
00B32184  48 8B 41 58                     mov rax, qword ptr [rcx + 0x58]
00B32188  48 85 C0                        test rax, rax
00B3218B  75 04                           jne 0x140b32191
00B3218D  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00B32191  48 89 84 24 90 01 00 00         mov qword ptr [rsp + 0x190], rax
00B32199  48 8B 41 60                     mov rax, qword ptr [rcx + 0x60]
00B3219D  48 85 C0                        test rax, rax
00B321A0  75 04                           jne 0x140b321a6
00B321A2  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
00B321A6  48 C1 E0 0C                     shl rax, 0xc
00B321AA  48 89 84 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rax
00B321B2  48 8B 41 68                     mov rax, qword ptr [rcx + 0x68]
00B321B6  48 85 C0                        test rax, rax
00B321B9  75 04                           jne 0x140b321bf
00B321BB  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
00B321BF  48 C1 E0 0C                     shl rax, 0xc
00B321C3  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
00B321CB  8B D6                           mov edx, esi
00B321CD  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
00B321D2  4C 8D 41 30                     lea r8, [rcx + 0x30]
00B321D6  48 8D 8C 24 60 01 00 00         lea rcx, [rsp + 0x160]
00B321DE  E8 45 B4 F4 FF                  call 0x140a7d628
00B321E3  41 8B 48 40                     mov ecx, dword ptr [r8 + 0x40]
00B321E7  85 C9                           test ecx, ecx
00B321E9  74 05                           je 0x140b321f0
00B321EB  45 88 21                        mov byte ptr [r9], r12b
00B321EE  EB 03                           jmp 0x140b321f3
00B321F0  41 8B 08                        mov ecx, dword ptr [r8]
00B321F3  89 08                           mov dword ptr [rax], ecx
00B321F5  41 03 D4                        add edx, r12d
00B321F8  49 83 C0 04                     add r8, 4
00B321FC  4D 03 CC                        add r9, r12
00B321FF  83 FA 03                        cmp edx, 3
00B32202  7C D2                           jl 0x140b321d6
00B32204  E9 C7 9B EC FF                  jmp 0x1409fbdd0
00B32209  83 F8 50                        cmp eax, 0x50
00B3220C  0F 85 CE 00 00 00               jne 0x140b322e0
00B32212  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
00B3221A  48 89 84 24 38 03 00 00         mov qword ptr [rsp + 0x338], rax
00B32222  48 8B 84 24 70 01 00 00         mov rax, qword ptr [rsp + 0x170]
00B3222A  48 89 84 24 40 03 00 00         mov qword ptr [rsp + 0x340], rax
00B32232  48 8B 84 24 78 01 00 00         mov rax, qword ptr [rsp + 0x178]
00B3223A  48 89 84 24 48 03 00 00         mov qword ptr [rsp + 0x348], rax
00B32242  48 8B 84 24 80 01 00 00         mov rax, qword ptr [rsp + 0x180]
00B3224A  48 89 84 24 50 03 00 00         mov qword ptr [rsp + 0x350], rax
00B32252  48 8B 84 24 88 01 00 00         mov rax, qword ptr [rsp + 0x188]
00B3225A  48 89 84 24 58 03 00 00         mov qword ptr [rsp + 0x358], rax
00B32262  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
00B3226A  48 89 84 24 60 03 00 00         mov qword ptr [rsp + 0x360], rax
00B32272  48 8B 84 24 98 01 00 00         mov rax, qword ptr [rsp + 0x198]
00B3227A  48 89 84 24 68 03 00 00         mov qword ptr [rsp + 0x368], rax
00B32282  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
00B3228A  48 89 84 24 70 03 00 00         mov qword ptr [rsp + 0x370], rax
00B32292  8B 84 24 A8 01 00 00            mov eax, dword ptr [rsp + 0x1a8]
00B32299  89 84 24 78 03 00 00            mov dword ptr [rsp + 0x378], eax
00B322A0  8B 84 24 AC 01 00 00            mov eax, dword ptr [rsp + 0x1ac]
00B322A7  89 84 24 7C 03 00 00            mov dword ptr [rsp + 0x37c], eax
00B322AE  8B 84 24 60 01 00 00            mov eax, dword ptr [rsp + 0x160]
00B322B5  B9 04 02 07 00                  mov ecx, 0x70204
00B322BA  23 C1                           and eax, ecx
00B322BC  89 84 24 30 03 00 00            mov dword ptr [rsp + 0x330], eax
00B322C3  8B 84 24 64 01 00 00            mov eax, dword ptr [rsp + 0x164]
00B322CA  23 C1                           and eax, ecx
00B322CC  89 84 24 34 03 00 00            mov dword ptr [rsp + 0x334], eax
00B322D3  4C 8D BC 24 30 03 00 00         lea r15, [rsp + 0x330]
00B322DB  E9 78 9C EC FF                  jmp 0x1409fbf58
00B322E0  4C 8D BC 24 60 01 00 00         lea r15, [rsp + 0x160]
00B322E8  E9 6B 9C EC FF                  jmp 0x1409fbf58
00B322ED  E8 CE DA 95 FF                  call 0x14048fdc0
00B322F2  90                              nop
00B322F3  45 8B C5                        mov r8d, r13d
00B322F6  48 8B C8                        mov rcx, rax
00B322F9  E8 A2 2D 6F FF                  call 0x1402250a0
00B322FE  48 8B 90 08 05 00 00            mov rdx, qword ptr [rax + 0x508]
00B32305  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00B3230A  49 8B CE                        mov rcx, r14
00B3230D  E8 2E 45 B9 FF                  call 0x1406c6840
00B32312  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00B32317  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00B3231C  E9 6A 9D EC FF                  jmp 0x1409fc08b
00B32321  8B D8                           mov ebx, eax
00B32323  33 F6                           xor esi, esi
00B32325  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00B3232A  44 8B 6C 24 58                  mov r13d, dword ptr [rsp + 0x58]
00B3232F  44 8B FE                        mov r15d, esi
00B32332  4C 8B B4 24 A8 00 00 00         mov r14, qword ptr [rsp + 0xa8]
00B3233A  4C 8B A4 24 80 00 00 00         mov r12, qword ptr [rsp + 0x80]
00B32342  E9 44 9D EC FF                  jmp 0x1409fc08b
00B32347  41 83 EE 01                     sub r14d, 1
00B3234B  0F 84 17 02 00 00               je 0x140b32568
00B32351  41 83 EE 01                     sub r14d, 1
00B32355  0F 84 F0 01 00 00               je 0x140b3254b
00B3235B  BB 02 00 00 00                  mov ebx, 2
00B32360  44 2B F3                        sub r14d, ebx
00B32363  0F 84 AE 01 00 00               je 0x140b32517
00B32369  41 83 EE 01                     sub r14d, 1
00B3236D  0F 84 8B 01 00 00               je 0x140b324fe
00B32373  41 83 EE 01                     sub r14d, 1
00B32377  0F 84 3A 01 00 00               je 0x140b324b7
00B3237D  41 83 EE 01                     sub r14d, 1
00B32381  0F 84 E9 00 00 00               je 0x140b32470
00B32387  41 83 EE 01                     sub r14d, 1
00B3238B  74 4D                           je 0x140b323da
00B3238D  41 83 FE 01                     cmp r14d, 1
00B32391  75 3D                           jne 0x140b323d0
00B32393  48 8D 94 24 50 05 00 00         lea rdx, [rsp + 0x550]
00B3239B  48 8B CF                        mov rcx, rdi
00B3239E  E8 A9 62 DE FF                  call 0x14091864c
00B323A3  48 8B 84 24 10 07 00 00         mov rax, qword ptr [rsp + 0x710]
00B323AB  48 89 84 24 50 02 00 00         mov qword ptr [rsp + 0x250], rax
00B323B3  48 8B 84 24 18 07 00 00         mov rax, qword ptr [rsp + 0x718]
00B323BB  48 89 84 24 58 02 00 00         mov qword ptr [rsp + 0x258], rax
00B323C3  4C 8D BC 24 50 02 00 00         lea r15, [rsp + 0x250]
00B323CB  E9 AF 9C EC FF                  jmp 0x1409fc07f
00B323D0  BB 03 00 00 C0                  mov ebx, 0xc0000003
00B323D5  E9 A7 9C EC FF                  jmp 0x1409fc081
00B323DA  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00B323E2  48 8B CF                        mov rcx, rdi
00B323E5  E8 56 00 99 FF                  call 0x1404c2440
00B323EA  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00B323F2  E8 39 17 91 FF                  call 0x140443b30
00B323F7  84 C0                           test al, al
00B323F9  0F 85 A8 FB FF FF               jne 0x140b31fa7
00B323FF  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00B32407  E8 94 2C 6F FF                  call 0x1402250a0
00B3240C  39 B0 3C 05 00 00               cmp dword ptr [rax + 0x53c], esi
00B32412  74 52                           je 0x140b32466
00B32414  0F 10 80 58 05 00 00            movups xmm0, xmmword ptr [rax + 0x558]
00B3241B  F3 0F 7F 84 24 E0 03 00 00      movdqu xmmword ptr [rsp + 0x3e0], xmm0
00B32424  8B 88 40 05 00 00               mov ecx, dword ptr [rax + 0x540]
00B3242A  89 8C 24 F0 03 00 00            mov dword ptr [rsp + 0x3f0], ecx
00B32431  8B CE                           mov ecx, esi
00B32433  48 8D 94 24 F4 03 00 00         lea rdx, [rsp + 0x3f4]
00B3243B  4C 8D 80 44 05 00 00            lea r8, [rax + 0x544]
00B32442  41 0F B6 00                     movzx eax, byte ptr [r8]
00B32446  66 89 02                        mov word ptr [rdx], ax
00B32449  41 03 CC                        add ecx, r12d
00B3244C  4D 03 C4                        add r8, r12
00B3244F  48 03 D3                        add rdx, rbx
00B32452  83 F9 0F                        cmp ecx, 0xf
00B32455  72 EB                           jb 0x140b32442
00B32457  8B DE                           mov ebx, esi
00B32459  4C 8D BC 24 E0 03 00 00         lea r15, [rsp + 0x3e0]
00B32461  E9 1B 9C EC FF                  jmp 0x1409fc081
00B32466  BB 22 00 00 80                  mov ebx, 0x80000022
00B3246B  E9 11 9C EC FF                  jmp 0x1409fc081
00B32470  48 8B D1                        mov rdx, rcx
00B32473  48 8B CF                        mov rcx, rdi
00B32476  E8 15 80 DE FF                  call 0x14091a490
00B3247B  8B 8F 48 04 00 00               mov ecx, dword ptr [rdi + 0x448]
00B32481  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00B32488  83 F9 08                        cmp ecx, 8
00B3248B  41 0F 42 C4                     cmovb eax, r12d
00B3248F  89 84 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], eax
00B32496  89 8C 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], ecx
00B3249D  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00B324A2  48 8B CF                        mov rcx, rdi
00B324A5  E8 56 79 DE FF                  call 0x140919e00
00B324AA  4C 8D BC 24 C0 00 00 00         lea r15, [rsp + 0xc0]
00B324B2  E9 C8 9B EC FF                  jmp 0x1409fc07f
00B324B7  48 8B D1                        mov rdx, rcx
00B324BA  48 8B CF                        mov rcx, rdi
00B324BD  E8 CE 7F DE FF                  call 0x14091a490
00B324C2  8B 8F 40 04 00 00               mov ecx, dword ptr [rdi + 0x440]
00B324C8  8B 84 24 C8 00 00 00            mov eax, dword ptr [rsp + 0xc8]
00B324CF  83 F9 05                        cmp ecx, 5
00B324D2  41 0F 42 C4                     cmovb eax, r12d
00B324D6  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
00B324DD  89 8C 24 CC 00 00 00            mov dword ptr [rsp + 0xcc], ecx
00B324E4  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00B324E9  48 8B CF                        mov rcx, rdi
00B324EC  E8 0F 79 DE FF                  call 0x140919e00
00B324F1  4C 8D BC 24 C8 00 00 00         lea r15, [rsp + 0xc8]
00B324F9  E9 81 9B EC FF                  jmp 0x1409fc07f
00B324FE  8B 87 14 06 00 00               mov eax, dword ptr [rdi + 0x614]
00B32504  D1 E8                           shr eax, 1
00B32506  41 22 C4                        and al, r12b
00B32509  88 44 24 5F                     mov byte ptr [rsp + 0x5f], al
00B3250D  4C 8D 7C 24 5F                  lea r15, [rsp + 0x5f]
00B32512  E9 68 9B EC FF                  jmp 0x1409fc07f
00B32517  48 8B D1                        mov rdx, rcx
00B3251A  48 8B CF                        mov rcx, rdi
00B3251D  E8 6E 7F DE FF                  call 0x14091a490
00B32522  48 8B 87 10 07 00 00            mov rax, qword ptr [rdi + 0x710]
00B32529  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00B32531  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00B32536  48 8B CF                        mov rcx, rdi
00B32539  E8 C2 78 DE FF                  call 0x140919e00
00B3253E  4C 8D BC 24 F0 00 00 00         lea r15, [rsp + 0xf0]
00B32546  E9 34 9B EC FF                  jmp 0x1409fc07f
00B3254B  0F 10 87 D0 05 00 00            movups xmm0, xmmword ptr [rdi + 0x5d0]
00B32552  F3 0F 7F 84 24 18 03 00 00      movdqu xmmword ptr [rsp + 0x318], xmm0
00B3255B  4C 8D BC 24 18 03 00 00         lea r15, [rsp + 0x318]
00B32563  E9 17 9B EC FF                  jmp 0x1409fc07f
00B32568  8B DE                           mov ebx, esi
00B3256A  48 8B 8F 00 07 00 00            mov rcx, qword ptr [rdi + 0x700]
00B32571  48 85 C9                        test rcx, rcx
00B32574  74 11                           je 0x140b32587
00B32576  0F B6 44 24 5D                  movzx eax, byte ptr [rsp + 0x5d]
00B3257B  48 83 F9 FF                     cmp rcx, -1
00B3257F  41 0F 45 C4                     cmovne eax, r12d
00B32583  88 44 24 5D                     mov byte ptr [rsp + 0x5d], al
00B32587  4C 8D 7C 24 5D                  lea r15, [rsp + 0x5d]
00B3258C  E9 F0 9A EC FF                  jmp 0x1409fc081
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B316B4(__int64 a1, int a2)
{
    unsigned __int64 v_stack_p100;
    unsigned int v_stack_p108;
    unsigned int v_stack_p10C;
    unsigned int v_stack_p110;
    unsigned __int8 v_stack_p114;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p120;
    unsigned int v_stack_p128;
    unsigned int v_stack_p12C;
    unsigned __int64 v_stack_p150;
    unsigned __int64 v_stack_p160;
    unsigned int v_stack_p164;
    unsigned __int64 v_stack_p168;
    unsigned __int64 v_stack_p170;
    unsigned __int64 v_stack_p178;
    unsigned __int64 v_stack_p180;
    unsigned __int64 v_stack_p188;
    unsigned __int64 v_stack_p190;
    unsigned __int64 v_stack_p198;
    unsigned __int64 v_stack_p1A0;
    unsigned int v_stack_p1A8;
    unsigned int v_stack_p1AC;
    unsigned __int64 v_stack_p1B0;
    unsigned __int64 v_stack_p1D0;
    unsigned int v_stack_p1D8;
    unsigned __int8 v_stack_p1DC;
    unsigned int v_stack_p1E0;
    unsigned int v_stack_p1E4;
    unsigned int v_stack_p1E8;
    unsigned __int8 v_stack_p1EC;
    unsigned int v_stack_p1F0;
    unsigned __int8 v_stack_p1F4;
    unsigned __int8 v_stack_p1F5;
    unsigned __int16 v_stack_p1F6;
    unsigned __int64 v_stack_p1F8;
    unsigned __int64 v_stack_p200;
    unsigned __int64 v_stack_p208;
    unsigned __int64 v_stack_p210;
    unsigned __int64 v_stack_p218;
    unsigned int v_stack_p220;
    unsigned int v_stack_p224;
    unsigned int v_stack_p228;
    unsigned __int64 v_stack_p230;
    unsigned __int64 v_stack_p250;
    unsigned __int64 v_stack_p258;
    unsigned __int64 v_stack_p260;
    unsigned __int64 v_stack_p268;
    unsigned __int64 v_stack_p270;
    unsigned __int64 v_stack_p278;
    unsigned int v_stack_p280;
    unsigned int v_stack_p284;
    unsigned int v_stack_p288;
    unsigned int v_stack_p28C;
    unsigned __int64 v_stack_p290;
    unsigned __int64 v_stack_p298;
    unsigned __int64 v_stack_p2A0;
    unsigned __int64 v_stack_p2A8;
    unsigned __int64 v_stack_p2B0;
    unsigned int v_stack_p2B8;
    unsigned int v_stack_p2BC;
    unsigned int v_stack_p2C0;
    unsigned int v_stack_p2C4;
    unsigned __int64 v_stack_p2F0;
    unsigned __int64 v_stack_p300;
    unsigned int v_stack_p310;
    unsigned __int64 v_stack_p318;
    unsigned int v_stack_p330;
    unsigned int v_stack_p334;
    unsigned __int64 v_stack_p338;
    unsigned __int64 v_stack_p340;
    unsigned __int64 v_stack_p348;
    unsigned __int64 v_stack_p350;
    unsigned __int64 v_stack_p358;
    unsigned __int64 v_stack_p360;
    unsigned __int64 v_stack_p368;
    unsigned __int64 v_stack_p370;
    unsigned int v_stack_p378;
    unsigned int v_stack_p37C;
    unsigned __int64 v_stack_p3E0;
    unsigned int v_stack_p3F0;
    unsigned __int64 v_stack_p3F4;
    unsigned __int8 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p490;
    unsigned __int64 v_stack_p498;
    unsigned __int64 v_stack_p4A0;
    unsigned __int64 v_stack_p4A8;
    unsigned __int64 v_stack_p4B0;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p550;
    unsigned int v_stack_p58;
    unsigned __int8 v_stack_p5C;
    unsigned __int8 v_stack_p5D;
    unsigned __int8 v_stack_p5F;
    unsigned __int64 v_stack_p60;
    unsigned __int16 v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p710;
    unsigned __int64 v_stack_p718;
    unsigned __int64 v_stack_p720;
    unsigned __int64 v_stack_p728;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p830;
    unsigned int v_stack_p8C;
    unsigned __int64 v_stack_p90;
    unsigned __int16 v_stack_p92;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA30;
    unsigned __int64 v_stack_pA8;
    unsigned int v_stack_pB0;
    unsigned int v_stack_pC0;
    unsigned int v_stack_pC4;
    unsigned int v_stack_pC8;
    unsigned int v_stack_pCC;
    unsigned __int64 v_stack_pD0;
    unsigned int v_stack_pD8;
    unsigned int v_stack_pDC;
    unsigned __int64 v_stack_pE8;
    unsigned __int64 v_stack_pF0;
    unsigned __int64 v_stack_pF8;

    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - (3));
    if (condition_is_equal) goto loc_00B316F4;
    a1 = (unsigned int)((a1) - (a2));
    if (condition_is_equal) goto loc_00B316F4;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00B316F4;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00B316F4;
    a1 = (unsigned int)((a1) - (17));
    if (condition_is_equal) goto loc_00B316F4;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00B316F4;
    v_stack_p58 = (unsigned int)(a1 + 31);
loc_00B316F4:
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B316B4(int64_t Arg1, int32_t Arg2)
{
    uint64_t v_stack_p100;
    uint32_t v_stack_p108;
    uint32_t v_stack_p10C;
    uint32_t v_stack_p110;
    uint8_t v_stack_p114;
    uint64_t v_stack_p118;
    uint64_t v_stack_p120;
    uint32_t v_stack_p128;
    uint32_t v_stack_p12C;
    uint64_t v_stack_p150;
    uint64_t v_stack_p160;
    uint32_t v_stack_p164;
    uint64_t v_stack_p168;
    uint64_t v_stack_p170;
    uint64_t v_stack_p178;
    uint64_t v_stack_p180;
    uint64_t v_stack_p188;
    uint64_t v_stack_p190;
    uint64_t v_stack_p198;
    uint64_t v_stack_p1A0;
    uint32_t v_stack_p1A8;
    uint32_t v_stack_p1AC;
    uint64_t v_stack_p1B0;
    uint64_t v_stack_p1D0;
    uint32_t v_stack_p1D8;
    uint8_t v_stack_p1DC;
    uint32_t v_stack_p1E0;
    uint32_t v_stack_p1E4;
    uint32_t v_stack_p1E8;
    uint8_t v_stack_p1EC;
    uint32_t v_stack_p1F0;
    uint8_t v_stack_p1F4;
    uint8_t v_stack_p1F5;
    uint16_t v_stack_p1F6;
    uint64_t v_stack_p1F8;
    uint64_t v_stack_p200;
    uint64_t v_stack_p208;
    uint64_t v_stack_p210;
    uint64_t v_stack_p218;
    uint32_t v_stack_p220;
    uint32_t v_stack_p224;
    uint32_t v_stack_p228;
    uint64_t v_stack_p230;
    uint64_t v_stack_p250;
    uint64_t v_stack_p258;
    uint64_t v_stack_p260;
    uint64_t v_stack_p268;
    uint64_t v_stack_p270;
    uint64_t v_stack_p278;
    uint32_t v_stack_p280;
    uint32_t v_stack_p284;
    uint32_t v_stack_p288;
    uint32_t v_stack_p28C;
    uint64_t v_stack_p290;
    uint64_t v_stack_p298;
    uint64_t v_stack_p2A0;
    uint64_t v_stack_p2A8;
    uint64_t v_stack_p2B0;
    uint32_t v_stack_p2B8;
    uint32_t v_stack_p2BC;
    uint32_t v_stack_p2C0;
    uint32_t v_stack_p2C4;
    uint64_t v_stack_p2F0;
    uint64_t v_stack_p300;
    uint32_t v_stack_p310;
    uint64_t v_stack_p318;
    uint32_t v_stack_p330;
    uint32_t v_stack_p334;
    uint64_t v_stack_p338;
    uint64_t v_stack_p340;
    uint64_t v_stack_p348;
    uint64_t v_stack_p350;
    uint64_t v_stack_p358;
    uint64_t v_stack_p360;
    uint64_t v_stack_p368;
    uint64_t v_stack_p370;
    uint32_t v_stack_p378;
    uint32_t v_stack_p37C;
    uint64_t v_stack_p3E0;
    uint32_t v_stack_p3F0;
    uint64_t v_stack_p3F4;
    uint8_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p490;
    uint64_t v_stack_p498;
    uint64_t v_stack_p4A0;
    uint64_t v_stack_p4A8;
    uint64_t v_stack_p4B0;
    uint64_t v_stack_p50;
    uint64_t v_stack_p550;
    uint32_t v_stack_p58;
    uint8_t v_stack_p5C;
    uint8_t v_stack_p5D;
    uint8_t v_stack_p5F;
    uint64_t v_stack_p60;
    uint16_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint32_t v_stack_p70;
    uint64_t v_stack_p710;
    uint64_t v_stack_p718;
    uint64_t v_stack_p720;
    uint64_t v_stack_p728;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;
    uint64_t v_stack_p830;
    uint32_t v_stack_p8C;
    uint64_t v_stack_p90;
    uint16_t v_stack_p92;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA30;
    uint64_t v_stack_pA8;
    uint32_t v_stack_pB0;
    uint32_t v_stack_pC0;
    uint32_t v_stack_pC4;
    uint32_t v_stack_pC8;
    uint32_t v_stack_pCC;
    uint64_t v_stack_pD0;
    uint32_t v_stack_pD8;
    uint32_t v_stack_pDC;
    uint64_t v_stack_pE8;
    uint64_t v_stack_pF0;
    uint64_t v_stack_pF8;

    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - (3));
    if (condition_is_equal) goto loc_00B316F4;
    Arg1 = (uint32_t)((Arg1) - (Arg2));
    if (condition_is_equal) goto loc_00B316F4;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00B316F4;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00B316F4;
    Arg1 = (uint32_t)((Arg1) - (17));
    if (condition_is_equal) goto loc_00B316F4;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00B316F4;
    v_stack_p58 = (uint32_t)(Arg1 + 31);
loc_00B316F4:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B316B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
