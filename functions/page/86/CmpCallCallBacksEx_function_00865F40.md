# CmpCallCallBacksEx

- RVA: `0x00865F40`–`0x008668D6` (길이 `2,454` bytes)
- VA: `0x0000000140865F40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006BBD8`
- 디코드: `534`개 명령, `2,454/2,454` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **23**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00866008` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00866035` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008660B8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008660C6` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00866101` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x0086611E` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x0086613C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00866198` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086620D` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x00866245` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x008662A2` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008662B0` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00866349` → [CmpCallbackFillObjectContext](CmpCallbackFillObjectContext_function_00866A10.md) (function, `0x00866A10`)
- `0x00866381` → [VrpRegistryCallback](VrpRegistryCallback_function_00867450.md) (function, `0x00867450`)
- `0x00866388` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00866415` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x00866445` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x00866493` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x008664E7` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x00866519` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00866554` → [CmpCallbackFillObjectContext](CmpCallbackFillObjectContext_function_00866A10.md) (function, `0x00866A10`)
- `0x0086658E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00866595` → [VrpRegistryCallback](VrpRegistryCallback_function_00867450.md) (function, `0x00867450`)
- `0x008665F6` → [CmpCallbackFetchCallContext](CmpCallbackFetchCallContext_function_008668E0.md) (function, `0x008668E0`)
- `0x0086661D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086664A` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008666CA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00866701` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00866736` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00866827` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00866887` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x00866898` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x008668B8` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008668C2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008668CC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [NtRenameKey](../7E/NtRenameKey_function_007E04B0.md) at `0x007E07F7`
- [NtReplaceKey](../7E/NtReplaceKey_function_007E0970.md) at `0x007E0B18`
- [NtRestoreKey](../7E/NtRestoreKey_function_007E0CC0.md) at `0x007E0E60`
- [NtSaveMergedKeys](../7E/NtSaveMergedKeys_function_007E1070.md) at `0x007E12A1`
- [NtSetInformationKey](../84/NtSetInformationKey_function_00843720.md) at `0x008439BF`
- [NtSetInformationKey](../84/NtSetInformationKey_function_00843720.md) at `0x00843B50`
- [NtSetValueKey](../84/NtSetValueKey_function_00844EA0.md) at `0x00845478`
- [NtSetValueKey](../84/NtSetValueKey_function_00844EA0.md) at `0x008455A0`
- [NtDeleteValueKey](../84/NtDeleteValueKey_function_00848770.md) at `0x00848AA8`
- [NtDeleteValueKey](../84/NtDeleteValueKey_function_00848770.md) at `0x00848BB8`
- [NtDeleteKey](../84/NtDeleteKey_function_00849920.md) at `0x00849A89`
- [NtDeleteKey](../84/NtDeleteKey_function_00849920.md) at `0x00849C07`
- [sub_0086560A](Unknown_function_0086560A.md) at `0x00865670`
- [sub_0086560A](Unknown_function_0086560A.md) at `0x00865AE0`
- [CmPostCallbackNotification](CmPostCallbackNotification_function_00865D50.md) at `0x00865DD6`
- [CmpCallCallBacks](CmpCallCallBacks_function_00865E10.md) at `0x00865E33`
- [CmPostCallbackNotificationEx](CmPostCallbackNotificationEx_function_00865E50.md) at `0x00865F05`
- [NtQueryKey](NtQueryKey_function_008676E0.md) at `0x00867A12`
- [NtQueryKey](NtQueryKey_function_008676E0.md) at `0x00867B34`
- [CmpSecurityMethod](../87/CmpSecurityMethod_function_00870CC0.md) at `0x00871058`
- [CmpSecurityMethod](../87/CmpSecurityMethod_function_00870CC0.md) at `0x008710F9`
- [CmLoadDifferencingKey](../87/CmLoadDifferencingKey_function_00875670.md) at `0x00875D06`
- [CmLoadDifferencingKey](../87/CmLoadDifferencingKey_function_00875670.md) at `0x008760A2`
- [CmpParseKey](../89/CmpParseKey_function_0089DDC0.md) at `0x0089E027`
- [CmpParseKey](../89/CmpParseKey_function_0089DDC0.md) at `0x0089E189`
- [CmpParseKey](../89/CmpParseKey_function_0089DDC0.md) at `0x0089E3A9`
- [NtQueryMultipleValueKey](../8B/NtQueryMultipleValueKey_function_008B13B0.md) at `0x008B16BC`
- [NtQueryMultipleValueKey](../8B/NtQueryMultipleValueKey_function_008B13B0.md) at `0x008B1892`
- [NtEnumerateKey](../8B/NtEnumerateKey_function_008B1F70.md) at `0x008B231A`
- [NtEnumerateKey](../8B/NtEnumerateKey_function_008B1F70.md) at `0x008B2429`
- [NtQueryValueKey](../8B/NtQueryValueKey_function_008B2A00.md) at `0x008B3069`
- [NtQueryValueKey](../8B/NtQueryValueKey_function_008B2A00.md) at `0x008B3142`
- [NtEnumerateValueKey](../8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B3E15`
- [NtEnumerateValueKey](../8B/NtEnumerateValueKey_function_008B3B50.md) at `0x008B41BD`
- [CmUnloadKey](../9A/CmUnloadKey_function_009AF2FC.md) at `0x009AF67B`
- [CmUnloadKey](../9A/CmUnloadKey_function_009AF2FC.md) at `0x009AF7A9`
- [NtFlushKey](../A8/NtFlushKey_function_00A8A030.md) at `0x00A8A30C`
- [NtFlushKey](../A8/NtFlushKey_function_00A8A030.md) at `0x00A8A343`
- [sub_00B44216](../B4/Unknown_function_00B44216.md) at `0x00B44298`

### Static image references
- `0x00865FD5` → RVA `0x00EF7BE0` (`.data`; read)
- `0x00866001` → RVA `0x00EF7BD0` (`.data`; read)
- `0x008660D1` → RVA `0x00EF7BF0` (`.data`; read)
- `0x008660DE` → RVA `0x00E0EC68` (`.data`; read)
- `0x008661AF` → RVA `0x00B82850` (`ExFreePool`; read)
- `0x00866232` → RVA `0x00EF7BB8` (`.data`; read)
- `0x00866375` → RVA `0x00867450` (`VrpRegistryCallback`; read)
- `0x008666A2` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x008666A8` → RVA `0x00EEFB88` (`.data`; read)
- `0x008666B6` → RVA `0x00E2C980` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **30**
  - `0x00866008` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00866035` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008660B8` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008660C6` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00866101` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x0086611E` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x0086613C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00866198` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086620D` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x00866245` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x008662A2` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008662B0` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00866388` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00866415` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x00866445` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x00866493` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x008664E7` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x00866519` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0086658E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0086661D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086664A` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008666CA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00866701` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00866736` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00866827` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00866887` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x00866898` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x008668B8` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008668C2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008668CC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00865F40  4C 8B DC                        mov r11, rsp
00865F43  45 88 4B 20                     mov byte ptr [r11 + 0x20], r9b
00865F47  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
00865F4B  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
00865F4F  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00865F53  53                              push rbx
00865F54  56                              push rsi
00865F55  57                              push rdi
00865F56  41 54                           push r12
00865F58  41 55                           push r13
00865F5A  41 56                           push r14
00865F5C  41 57                           push r15
00865F5E  48 81 EC D0 00 00 00            sub rsp, 0xd0
00865F65  41 0F B6 F1                     movzx esi, r9b
00865F69  4D 8B D0                        mov r10, r8
00865F6C  4C 8B CA                        mov r9, rdx
00865F6F  44 8B C1                        mov r8d, ecx
00865F72  45 33 F6                        xor r14d, r14d
00865F75  44 89 74 24 24                  mov dword ptr [rsp + 0x24], r14d
00865F7A  0F 57 C0                        xorps xmm0, xmm0
00865F7D  33 C0                           xor eax, eax
00865F7F  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00865F84  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00865F89  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00865F8E  49 89 43 80                     mov qword ptr [r11 - 0x80], rax
00865F92  41 0F 11 43 A0                  movups xmmword ptr [r11 - 0x60], xmm0
00865F97  41 8B D6                        mov edx, r14d
00865F9A  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00865F9F  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00865FA4  88 44 24 21                     mov byte ptr [rsp + 0x21], al
00865FA8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00865FB1  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00865FB9  40 80 FE 01                     cmp sil, 1
00865FBD  0F 85 DA 04 00 00               jne 0x14086649d
00865FC3  4C 8D B8 28 06 00 00            lea r15, [rax + 0x628]
00865FCA  4C 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r15
00865FD2  49 8B 07                        mov rax, qword ptr [r15]
00865FD5  4C 8D 25 04 1C 69 00            lea r12, [rip + 0x691c04]
00865FDC  48 85 C0                        test rax, rax
00865FDF  0F 85 BD 01 00 00               jne 0x1408661a2
00865FE5  49 8B FC                        mov rdi, r12
00865FE8  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00865FED  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00865FF6  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00865FFD  90                              nop
00865FFE  45 33 C0                        xor r8d, r8d
00866001  48 8D 0D C8 1B 69 00            lea rcx, [rip + 0x691bc8]
00866008  E8 23 A2 9A FF                  call 0x140210230
0086600D  48 8B D8                        mov rbx, rax
00866010  B9 11 00 00 00                  mov ecx, 0x11
00866015  33 C0                           xor eax, eax
00866017  F0 48 0F B1 0D B0 1B 69 00      lock cmpxchg qword ptr [rip + 0x691bb0], rcx
00866020  74 18                           je 0x14086603a
00866022  4C 8D 0D A7 1B 69 00            lea r9, [rip + 0x691ba7]
00866029  4C 8B C3                        mov r8, rbx
0086602C  33 D2                           xor edx, edx
0086602E  48 8D 0D 9B 1B 69 00            lea rcx, [rip + 0x691b9b]
00866035  E8 12 A4 9A FF                  call 0x14021044c
0086603A  48 85 DB                        test rbx, rbx
0086603D  74 04                           je 0x140866043
0086603F  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00866043  4C 8B AC 24 40 01 00 00         mov r13, qword ptr [rsp + 0x140]
0086604B  48 8B 3F                        mov rdi, qword ptr [rdi]
0086604E  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00866053  49 3B FC                        cmp rdi, r12
00866056  0F 84 4F 01 00 00               je 0x1408661ab
0086605C  4C 8D 67 10                     lea r12, [rdi + 0x10]
00866060  4C 89 A4 24 90 00 00 00         mov qword ptr [rsp + 0x90], r12
00866068  41 8B 04 24                     mov eax, dword ptr [r12]
0086606C  85 C0                           test eax, eax
0086606E  0F 88 E4 05 00 00               js 0x140866658
00866074  F0 41 FF 04 24                  lock inc dword ptr [r12]
00866079  0F 0D 0D 50 1B 69 00            prefetchw byte ptr [rip + 0x691b50]
00866080  48 8B 05 49 1B 69 00            mov rax, qword ptr [rip + 0x691b49]
00866087  48 8B C8                        mov rcx, rax
0086608A  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086608E  48 8D 50 F0                     lea rdx, [rax - 0x10]
00866092  48 83 F9 10                     cmp rcx, 0x10
00866096  49 0F 46 D6                     cmovbe rdx, r14
0086609A  A8 02                           test al, 2
0086609C  0F 85 EF 00 00 00               jne 0x140866191
008660A2  F0 48 0F B1 15 25 1B 69 00      lock cmpxchg qword ptr [rip + 0x691b25], rdx
008660AB  0F 85 E0 00 00 00               jne 0x140866191
008660B1  48 8D 0D 18 1B 69 00            lea rcx, [rip + 0x691b18]
008660B8  E8 43 B5 A7 FF                  call 0x1402e1600
008660BD  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008660C6  E8 25 8F 9F FF                  call 0x14025eff0
008660CB  32 C0                           xor al, al
008660CD  88 44 24 20                     mov byte ptr [rsp + 0x20], al
008660D1  83 3D 18 1B 69 00 00            cmp dword ptr [rip + 0x691b18], 0
008660D8  0F 85 2B 04 00 00               jne 0x140866509
008660DE  83 3D 83 8B 5A 00 00            cmp dword ptr [rip + 0x5a8b83], 0
008660E5  0F 84 A6 07 00 00               je 0x140866891
008660EB  65 4C 8B 34 25 20 00 00 00      mov r14, qword ptr gs:[0x20]
008660F4  49 8B B6 A0 08 00 00            mov rsi, qword ptr [r14 + 0x8a0]
008660FB  FF 46 14                        inc dword ptr [rsi + 0x14]
008660FE  48 8B CE                        mov rcx, rsi
00866101  E8 6A 44 E5 FF                  call 0x1406ba570
00866106  48 8B D8                        mov rbx, rax
00866109  48 85 C0                        test rax, rax
0086610C  75 36                           jne 0x140866144
0086610E  FF 46 18                        inc dword ptr [rsi + 0x18]
00866111  49 8B B6 A8 08 00 00            mov rsi, qword ptr [r14 + 0x8a8]
00866118  FF 46 14                        inc dword ptr [rsi + 0x14]
0086611B  48 8B CE                        mov rcx, rsi
0086611E  E8 4D 44 E5 FF                  call 0x1406ba570
00866123  48 8B D8                        mov rbx, rax
00866126  48 85 C0                        test rax, rax
00866129  75 19                           jne 0x140866144
0086612B  FF 46 18                        inc dword ptr [rsi + 0x18]
0086612E  8B 56 2C                        mov edx, dword ptr [rsi + 0x2c]
00866131  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00866135  44 8B 46 28                     mov r8d, dword ptr [rsi + 0x28]
00866139  8B 4E 24                        mov ecx, dword ptr [rsi + 0x24]
0086613C  E8 8F 49 E5 FF                  call 0x1406baad0
00866141  48 8B D8                        mov rbx, rax
00866144  48 85 DB                        test rbx, rbx
00866147  74 06                           je 0x14086614f
00866149  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
0086614D  89 03                           mov dword ptr [rbx], eax
0086614F  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00866154  0F B6 B4 24 28 01 00 00         movzx esi, byte ptr [rsp + 0x128]
0086615C  45 33 F6                        xor r14d, r14d
0086615F  48 85 DB                        test rbx, rbx
00866162  0F 84 53 03 00 00               je 0x1408664bb
00866168  48 89 7B 18                     mov qword ptr [rbx + 0x18], rdi
0086616C  4C 89 73 20                     mov qword ptr [rbx + 0x20], r14
00866170  48 8D 4B 10                     lea rcx, [rbx + 0x10]
00866174  49 8B 07                        mov rax, qword ptr [r15]
00866177  48 89 01                        mov qword ptr [rcx], rax
0086617A  49 89 0F                        mov qword ptr [r15], rcx
0086617D  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00866181  4C 39 29                        cmp qword ptr [rcx], r13
00866184  0F 84 A1 03 00 00               je 0x14086652b
0086618A  B9 03 00 00 00                  mov ecx, 3
0086618F  CD 29                           int 0x29
00866191  48 8D 0D 38 1A 69 00            lea rcx, [rip + 0x691a38]
00866198  E8 33 D7 9F FF                  call 0x1402638d0
0086619D  E9 0F FF FF FF                  jmp 0x1408660b1
008661A2  48 8B 78 08                     mov rdi, qword ptr [rax + 8]
008661A6  E9 3D FE FF FF                  jmp 0x140865fe8
008661AB  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
008661AF  4C 8D 3D 9A C6 31 00            lea r15, [rip + 0x31c69a]
008661B6  E9 9B 00 00 00                  jmp 0x140866256
008661BB  48 89 0A                        mov qword ptr [rdx], rcx
008661BE  48 89 51 08                     mov qword ptr [rcx + 8], rdx
008661C2  49 8B 07                        mov rax, qword ptr [r15]
008661C5  48 85 C0                        test rax, rax
008661C8  74 06                           je 0x1408661d0
008661CA  48 8B 00                        mov rax, qword ptr [rax]
008661CD  49 89 07                        mov qword ptr [r15], rax
008661D0  83 3D 19 1A 69 00 00            cmp dword ptr [rip + 0x691a19], 0
008661D7  0F 85 54 05 00 00               jne 0x140866731
008661DD  83 3D 84 8A 5A 00 00            cmp dword ptr [rip + 0x5a8a84], 0
008661E4  0F 84 21 05 00 00               je 0x14086670b
008661EA  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008661F3  48 8B 8A A0 08 00 00            mov rcx, qword ptr [rdx + 0x8a0]
008661FA  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008661FD  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00866201  66 39 01                        cmp word ptr [rcx], ax
00866204  0F 83 E9 05 00 00               jae 0x1408667f3
0086620A  48 8B D3                        mov rdx, rbx
0086620D  E8 9E 43 E5 FF                  call 0x1406ba5b0
00866212  4C 8D 3D 37 C6 31 00            lea r15, [rip + 0x31c637]
00866219  B8 FF FF FF FF                  mov eax, 0xffffffff
0086621E  F0 41 0F C1 04 24               lock xadd dword ptr [r12], eax
00866224  FF C8                           dec eax
00866226  3D 00 00 00 80                  cmp eax, 0x80000000
0086622B  75 1D                           jne 0x14086624a
0086622D  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00866232  48 83 3D 7E 19 69 00 00         cmp qword ptr [rip + 0x69197e], 0
0086623A  74 0E                           je 0x14086624a
0086623C  33 D2                           xor edx, edx
0086623E  48 8D 0D 73 19 69 00            lea rcx, [rip + 0x691973]
00866245  E8 96 DD A3 FF                  call 0x1402a3fe0
0086624A  40 32 F6                        xor sil, sil
0086624D  C6 44 24 21 01                  mov byte ptr [rsp + 0x21], 1
00866252  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
00866256  41 BC 40 00 00 00               mov r12d, 0x40
0086625C  80 7C 24 20 00                  cmp byte ptr [rsp + 0x20], 0
00866261  74 56                           je 0x1408662b9
00866263  0F 0D 0D 66 19 69 00            prefetchw byte ptr [rip + 0x691966]
0086626A  48 8B 05 5F 19 69 00            mov rax, qword ptr [rip + 0x69195f]
00866271  48 8B C8                        mov rcx, rax
00866274  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00866278  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086627C  48 83 F9 10                     cmp rcx, 0x10
00866280  49 0F 46 D6                     cmovbe rdx, r14
00866284  A8 02                           test al, 2
00866286  0F 85 00 02 00 00               jne 0x14086648c
0086628C  F0 48 0F B1 15 3B 19 69 00      lock cmpxchg qword ptr [rip + 0x69193b], rdx
00866295  0F 85 F1 01 00 00               jne 0x14086648c
0086629B  48 8D 0D 2E 19 69 00            lea rcx, [rip + 0x69192e]
008662A2  E8 59 B3 A7 FF                  call 0x1402e1600
008662A7  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008662B0  E8 3B 8D 9F FF                  call 0x14025eff0
008662B5  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
008662B9  4C 8B 94 24 20 01 00 00         mov r10, qword ptr [rsp + 0x120]
008662C1  4C 8B 8C 24 18 01 00 00         mov r9, qword ptr [rsp + 0x118]
008662C9  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
008662CE  44 8B 84 24 10 01 00 00         mov r8d, dword ptr [rsp + 0x110]
008662D6  40 84 F6                        test sil, sil
008662D9  0F 85 8C 01 00 00               jne 0x14086646b
008662DF  80 7C 24 21 01                  cmp byte ptr [rsp + 0x21], 1
008662E4  0F 84 56 04 00 00               je 0x140866740
008662EA  49 8B D1                        mov rdx, r9
008662ED  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
008662F2  4C 89 54 24 50                  mov qword ptr [rsp + 0x50], r10
008662F7  41 8B F0                        mov esi, r8d
008662FA  44 89 84 24 30 01 00 00         mov dword ptr [rsp + 0x130], r8d
00866302  4D 39 6D 00                     cmp qword ptr [r13], r13
00866306  0F 84 5F 01 00 00               je 0x14086646b
0086630C  49 8B 5D 08                     mov rbx, qword ptr [r13 + 8]
00866310  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00866315  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00866319  4C 39 2B                        cmp qword ptr [rbx], r13
0086631C  0F 85 68 FE FF FF               jne 0x14086618a
00866322  48 39 18                        cmp qword ptr [rax], rbx
00866325  0F 85 5F FE FF FF               jne 0x14086618a
0086632B  49 89 45 08                     mov qword ptr [r13 + 8], rax
0086632F  4C 89 28                        mov qword ptr [rax], r13
00866332  48 8B 7B 18                     mov rdi, qword ptr [rbx + 0x18]
00866336  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0086633B  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
0086633F  48 89 42 20                     mov qword ptr [rdx + 0x20], rax
00866343  4C 8D 47 18                     lea r8, [rdi + 0x18]
00866347  8B CE                           mov ecx, esi
00866349  E8 C2 06 00 00                  call 0x140866a10
0086634E  48 83 BC 24 20 01 00 00 00      cmp qword ptr [rsp + 0x120], 0
00866357  74 0C                           je 0x140866365
00866359  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
0086635C  A8 01                           test al, 1
0086635E  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
00866363  75 05                           jne 0x14086636a
00866365  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
0086636A  48 63 D6                        movsxd rdx, esi
0086636D  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
00866371  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00866375  4C 8D 0D D4 10 00 00            lea r9, [rip + 0x10d4]
0086637C  49 3B C1                        cmp rax, r9
0086637F  75 07                           jne 0x140866388
00866381  E8 CA 10 00 00                  call 0x140867450
00866386  EB 05                           jmp 0x14086638d
00866388  E8 43 47 E5 FF                  call 0x1406baad0
0086638D  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
00866391  EB 27                           jmp 0x1408663ba
00866393  45 33 F6                        xor r14d, r14d
00866396  4C 8D 3D B3 C4 31 00            lea r15, [rip + 0x31c4b3]
0086639D  45 8D 66 40                     lea r12d, [r14 + 0x40]
008663A1  4C 8B AC 24 40 01 00 00         mov r13, qword ptr [rsp + 0x140]
008663A9  8B B4 24 30 01 00 00            mov esi, dword ptr [rsp + 0x130]
008663B0  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
008663B5  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
008663BA  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
008663C2  48 8B 81 28 06 00 00            mov rax, qword ptr [rcx + 0x628]
008663C9  48 85 C0                        test rax, rax
008663CC  74 0A                           je 0x1408663d8
008663CE  48 8B 00                        mov rax, qword ptr [rax]
008663D1  48 89 81 28 06 00 00            mov qword ptr [rcx + 0x628], rax
008663D8  83 3D 11 18 69 00 00            cmp dword ptr [rip + 0x691811], 0
008663DF  0F 85 E0 02 00 00               jne 0x1408666c5
008663E5  83 3D 7C 88 5A 00 00            cmp dword ptr [rip + 0x5a887c], 0
008663EC  0F 84 B0 02 00 00               je 0x1408666a2
008663F2  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008663FB  48 8B 8A A0 08 00 00            mov rcx, qword ptr [rdx + 0x8a0]
00866402  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00866405  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00866409  66 39 01                        cmp word ptr [rcx], ax
0086640C  0F 83 C2 02 00 00               jae 0x1408666d4
00866412  48 8B D3                        mov rdx, rbx
00866415  E8 96 41 E5 FF                  call 0x1406ba5b0
0086641A  B8 FF FF FF FF                  mov eax, 0xffffffff
0086641F  F0 0F C1 47 10                  lock xadd dword ptr [rdi + 0x10], eax
00866424  FF C8                           dec eax
00866426  3D 00 00 00 80                  cmp eax, 0x80000000
0086642B  75 1D                           jne 0x14086644a
0086642D  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00866432  48 83 3D 7E 17 69 00 00         cmp qword ptr [rip + 0x69177e], 0
0086643A  74 0E                           je 0x14086644a
0086643C  33 D2                           xor edx, edx
0086643E  48 8D 0D 73 17 69 00            lea rcx, [rip + 0x691773]
00866445  E8 96 DB A3 FF                  call 0x1402a3fe0
0086644A  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
0086644F  81 7C 24 24 03 05 00 C0         cmp dword ptr [rsp + 0x24], 0xc0000503
00866457  75 06                           jne 0x14086645f
00866459  8B 42 18                        mov eax, dword ptr [rdx + 0x18]
0086645C  89 42 08                        mov dword ptr [rdx + 8], eax
0086645F  41 8B CE                        mov ecx, r14d
00866462  89 4C 24 24                     mov dword ptr [rsp + 0x24], ecx
00866466  E9 97 FE FF FF                  jmp 0x140866302
0086646B  80 7C 24 21 01                  cmp byte ptr [rsp + 0x21], 1
00866470  0F 84 D8 03 00 00               je 0x14086684e
00866476  8B C1                           mov eax, ecx
00866478  48 81 C4 D0 00 00 00            add rsp, 0xd0
0086647F  41 5F                           pop r15
00866481  41 5E                           pop r14
00866483  41 5D                           pop r13
00866485  41 5C                           pop r12
00866487  5F                              pop rdi
00866488  5E                              pop rsi
00866489  5B                              pop rbx
0086648A  C3                              ret
0086648B  CC                              int3
0086648C  48 8D 0D 3D 17 69 00            lea rcx, [rip + 0x69173d]
00866493  E8 38 D4 9F FF                  call 0x1402638d0
00866498  E9 FE FD FF FF                  jmp 0x14086629b
0086649D  4C 8D 3D AC C3 31 00            lea r15, [rip + 0x31c3ac]
008664A4  41 BC 40 00 00 00               mov r12d, 0x40
008664AA  4C 8B AC 24 40 01 00 00         mov r13, qword ptr [rsp + 0x140]
008664B2  8B 4C 24 24                     mov ecx, dword ptr [rsp + 0x24]
008664B6  E9 1B FE FF FF                  jmp 0x1408662d6
008664BB  B8 FF FF FF FF                  mov eax, 0xffffffff
008664C0  F0 41 0F C1 04 24               lock xadd dword ptr [r12], eax
008664C6  FF C8                           dec eax
008664C8  3D 00 00 00 80                  cmp eax, 0x80000000
008664CD  75 1D                           jne 0x1408664ec
008664CF  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
008664D4  48 83 3D DC 16 69 00 00         cmp qword ptr [rip + 0x6916dc], 0
008664DC  74 0E                           je 0x1408664ec
008664DE  33 D2                           xor edx, edx
008664E0  48 8D 0D D1 16 69 00            lea rcx, [rip + 0x6916d1]
008664E7  E8 F4 DA A3 FF                  call 0x1402a3fe0
008664EC  B9 9A 00 00 C0                  mov ecx, 0xc000009a
008664F1  89 4C 24 24                     mov dword ptr [rsp + 0x24], ecx
008664F5  C6 44 24 21 01                  mov byte ptr [rsp + 0x21], 1
008664FA  40 32 F6                        xor sil, sil
008664FD  4C 8D 3D 4C C3 31 00            lea r15, [rip + 0x31c34c]
00866504  E9 4D FD FF FF                  jmp 0x140866256
00866509  41 B8 43 4D 63 69               mov r8d, 0x69634d43
0086650F  BA 30 00 00 00                  mov edx, 0x30
00866514  B9 00 01 00 00                  mov ecx, 0x100
00866519  E8 D2 BB 31 00                  call 0x140b820f0
0086651E  48 8B D8                        mov rbx, rax
00866521  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00866526  E9 34 FC FF FF                  jmp 0x14086615f
0086652B  4C 89 2B                        mov qword ptr [rbx], r13
0086652E  48 8D 43 08                     lea rax, [rbx + 8]
00866532  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00866537  48 89 08                        mov qword ptr [rax], rcx
0086653A  48 89 19                        mov qword ptr [rcx], rbx
0086653D  49 89 5D 08                     mov qword ptr [r13 + 8], rbx
00866541  4C 8D 47 18                     lea r8, [rdi + 0x18]
00866545  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
0086654D  8B 8C 24 10 01 00 00            mov ecx, dword ptr [rsp + 0x110]
00866554  E8 B7 04 00 00                  call 0x140866a10
00866559  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
00866561  48 85 C9                        test rcx, rcx
00866564  0F 85 FA 00 00 00               jne 0x140866664
0086656A  4C 8B 84 24 18 01 00 00         mov r8, qword ptr [rsp + 0x118]
00866572  48 63 94 24 10 01 00 00         movsxd rdx, dword ptr [rsp + 0x110]
0086657A  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0086657E  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
00866582  4C 8D 0D C7 0E 00 00            lea r9, [rip + 0xec7]
00866589  49 3B C1                        cmp rax, r9
0086658C  74 07                           je 0x140866595
0086658E  E8 3D 45 E5 FF                  call 0x1406baad0
00866593  EB 05                           jmp 0x14086659a
00866595  E8 B6 0E 00 00                  call 0x140867450
0086659A  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
0086659E  EB 36                           jmp 0x1408665d6
008665A0  45 33 F6                        xor r14d, r14d
008665A3  4C 8B AC 24 40 01 00 00         mov r13, qword ptr [rsp + 0x140]
008665AB  0F B6 B4 24 28 01 00 00         movzx esi, byte ptr [rsp + 0x128]
008665B3  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
008665B7  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
008665BC  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
008665C1  4C 8B A4 24 90 00 00 00         mov r12, qword ptr [rsp + 0x90]
008665C9  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008665CE  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
008665D6  8B 8C 24 10 01 00 00            mov ecx, dword ptr [rsp + 0x110]
008665DD  83 F9 0E                        cmp ecx, 0xe
008665E0  0F 85 91 00 00 00               jne 0x140866677
008665E6  44 89 74 24 24                  mov dword ptr [rsp + 0x24], r14d
008665EB  4C 8B C3                        mov r8, rbx
008665EE  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
008665F6  E8 E5 02 00 00                  call 0x1408668e0
008665FB  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00866600  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00866609  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00866610  90                              nop
00866611  45 33 C0                        xor r8d, r8d
00866614  33 D2                           xor edx, edx
00866616  48 8D 0D B3 15 69 00            lea rcx, [rip + 0x6915b3]
0086661D  E8 0E 9C 9A FF                  call 0x140210230
00866622  48 8B D8                        mov rbx, rax
00866625  33 C0                           xor eax, eax
00866627  B9 11 00 00 00                  mov ecx, 0x11
0086662C  F0 48 0F B1 0D 9B 15 69 00      lock cmpxchg qword ptr [rip + 0x69159b], rcx
00866635  74 18                           je 0x14086664f
00866637  4C 8D 0D 92 15 69 00            lea r9, [rip + 0x691592]
0086663E  4C 8B C3                        mov r8, rbx
00866641  33 D2                           xor edx, edx
00866643  48 8D 0D 86 15 69 00            lea rcx, [rip + 0x691586]
0086664A  E8 FD 9D 9A FF                  call 0x14021044c
0086664F  48 85 DB                        test rbx, rbx
00866652  74 04                           je 0x140866658
00866654  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00866658  4C 8D 25 81 15 69 00            lea r12, [rip + 0x691581]
0086665F  E9 E7 F9 FF FF                  jmp 0x14086604b
00866664  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
00866667  A8 01                           test al, 1
00866669  0F 84 FB FE FF FF               je 0x14086656a
0086666F  4C 8B C1                        mov r8, rcx
00866672  E9 FB FE FF FF                  jmp 0x140866572
00866677  85 C0                           test eax, eax
00866679  0F 89 6C FF FF FF               jns 0x1408665eb
0086667F  48 8B 0B                        mov rcx, qword ptr [rbx]
00866682  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00866687  48 8B 10                        mov rdx, qword ptr [rax]
0086668A  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
0086668E  0F 85 F6 FA FF FF               jne 0x14086618a
00866694  48 39 1A                        cmp qword ptr [rdx], rbx
00866697  0F 85 ED FA FF FF               jne 0x14086618a
0086669D  E9 19 FB FF FF                  jmp 0x1408661bb
008666A2  8B 0D D8 03 76 00               mov ecx, dword ptr [rip + 0x7603d8]
008666A8  0F AF 0D D9 94 68 00            imul ecx, dword ptr [rip + 0x6894d9]
008666AF  83 F9 40                        cmp ecx, 0x40
008666B2  41 0F 47 CC                     cmova ecx, r12d
008666B6  0F B7 05 C3 62 5C 00            movzx eax, word ptr [rip + 0x5c62c3]
008666BD  3B C1                           cmp eax, ecx
008666BF  0F 82 B8 01 00 00               jb 0x14086687d
008666C5  33 D2                           xor edx, edx
008666C7  48 8B CB                        mov rcx, rbx
008666CA  E8 A1 C1 31 00                  call 0x140b82870
008666CF  E9 46 FD FF FF                  jmp 0x14086641a
008666D4  FF 41 20                        inc dword ptr [rcx + 0x20]
008666D7  48 8B 8A A8 08 00 00            mov rcx, qword ptr [rdx + 0x8a8]
008666DE  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008666E1  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008666E5  66 39 01                        cmp word ptr [rcx], ax
008666E8  0F 82 24 FD FF FF               jb 0x140866412
008666EE  FF 41 20                        inc dword ptr [rcx + 0x20]
008666F1  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
008666F5  48 8B CB                        mov rcx, rbx
008666F8  49 3B C7                        cmp rax, r15
008666FB  0F 85 CB 01 00 00               jne 0x1408668cc
00866701  E8 4A C1 31 00                  call 0x140b82850
00866706  E9 0F FD FF FF                  jmp 0x14086641a
0086670B  8B 0D 6F 03 76 00               mov ecx, dword ptr [rip + 0x76036f]
00866711  0F AF 0D 70 94 68 00            imul ecx, dword ptr [rip + 0x689470]
00866718  B8 40 00 00 00                  mov eax, 0x40
0086671D  3B C8                           cmp ecx, eax
0086671F  0F 47 C8                        cmova ecx, eax
00866722  0F B7 05 57 62 5C 00            movzx eax, word ptr [rip + 0x5c6257]
00866729  3B C1                           cmp eax, ecx
0086672B  0F 82 7D 01 00 00               jb 0x1408668ae
00866731  33 D2                           xor edx, edx
00866733  48 8B CB                        mov rcx, rbx
00866736  E8 35 C1 31 00                  call 0x140b82870
0086673B  E9 D2 FA FF FF                  jmp 0x140866212
00866740  0F 57 C0                        xorps xmm0, xmm0
00866743  33 C0                           xor eax, eax
00866745  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
0086674A  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
0086674F  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00866754  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0086675C  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00866761  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00866766  8B B4 24 30 01 00 00            mov esi, dword ptr [rsp + 0x130]
0086676D  8D 46 E5                        lea eax, [rsi - 0x1b]
00866770  A9 FD FF FF FF                  test eax, 0xfffffffd
00866775  0F 85 B6 00 00 00               jne 0x140866831
0086677B  81 F9 03 05 00 C0               cmp ecx, 0xc0000503
00866781  0F 85 E5 00 00 00               jne 0x14086686c
00866787  49 8B 41 48                     mov rax, qword ptr [r9 + 0x48]
0086678B  48 8B 10                        mov rdx, qword ptr [rax]
0086678E  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
00866793  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00866798  81 F9 03 05 00 C0               cmp ecx, 0xc0000503
0086679E  0F 85 9F 00 00 00               jne 0x140866843
008667A4  41 8D 40 E6                     lea eax, [r8 - 0x1a]
008667A8  A9 FD FF FF FF                  test eax, 0xfffffffd
008667AD  41 8B C6                        mov eax, r14d
008667B0  0F 84 BE 00 00 00               je 0x140866874
008667B6  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
008667BA  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
008667BE  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
008667C3  4D 85 D2                        test r10, r10
008667C6  0F 84 36 FB FF FF               je 0x140866302
008667CC  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
008667D4  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008667D9  48 8D 44 24 58                  lea rax, [rsp + 0x58]
008667DE  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
008667E6  4C 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r10
008667EE  E9 0F FB FF FF                  jmp 0x140866302
008667F3  FF 41 20                        inc dword ptr [rcx + 0x20]
008667F6  48 8B 8A A8 08 00 00            mov rcx, qword ptr [rdx + 0x8a8]
008667FD  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00866800  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00866804  66 39 01                        cmp word ptr [rcx], ax
00866807  0F 82 FD F9 FF FF               jb 0x14086620a
0086680D  FF 41 20                        inc dword ptr [rcx + 0x20]
00866810  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00866814  4C 8D 3D 35 C0 31 00            lea r15, [rip + 0x31c035]
0086681B  48 8B CB                        mov rcx, rbx
0086681E  49 3B C7                        cmp rax, r15
00866821  0F 85 9B 00 00 00               jne 0x1408668c2
00866827  E8 24 C0 31 00                  call 0x140b82850
0086682C  E9 E8 F9 FF FF                  jmp 0x140866219
00866831  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
00866839  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0086683E  E9 55 FF FF FF                  jmp 0x140866798
00866843  8B C1                           mov eax, ecx
00866845  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00866849  E9 6C FF FF FF                  jmp 0x1408667ba
0086684E  48 85 D2                        test rdx, rdx
00866851  0F 84 1F FC FF FF               je 0x140866476
00866857  8B 4A 18                        mov ecx, dword ptr [rdx + 0x18]
0086685A  85 C9                           test ecx, ecx
0086685C  0F 88 14 FC FF FF               js 0x140866476
00866862  B9 03 05 00 C0                  mov ecx, 0xc0000503
00866867  E9 0A FC FF FF                  jmp 0x140866476
0086686C  49 8B D6                        mov rdx, r14
0086686F  E9 1A FF FF FF                  jmp 0x14086678e
00866874  41 8B 42 0C                     mov eax, dword ptr [r10 + 0xc]
00866878  E9 39 FF FF FF                  jmp 0x1408667b6
0086687D  48 8B D3                        mov rdx, rbx
00866880  48 8D 0D F9 60 5C 00            lea rcx, [rip + 0x5c60f9]
00866887  E8 24 3D E5 FF                  call 0x1406ba5b0
0086688C  E9 89 FB FF FF                  jmp 0x14086641a
00866891  48 8D 0D E8 60 5C 00            lea rcx, [rip + 0x5c60e8]
00866898  E8 D3 3C E5 FF                  call 0x1406ba570
0086689D  48 8B D8                        mov rbx, rax
008668A0  48 85 C0                        test rax, rax
008668A3  0F 85 78 FC FF FF               jne 0x140866521
008668A9  E9 5B FC FF FF                  jmp 0x140866509
008668AE  48 8B D3                        mov rdx, rbx
008668B1  48 8D 0D C8 60 5C 00            lea rcx, [rip + 0x5c60c8]
008668B8  E8 F3 3C E5 FF                  call 0x1406ba5b0
008668BD  E9 50 F9 FF FF                  jmp 0x140866212
008668C2  E8 09 42 E5 FF                  call 0x1406baad0
008668C7  E9 4D F9 FF FF                  jmp 0x140866219
008668CC  E8 FF 41 E5 FF                  call 0x1406baad0
008668D1  E9 44 FB FF FF                  jmp 0x14086641a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCallCallBacksEx(int a1, __int64 a2, __int64 a3, unsigned __int8 a4, unsigned int a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE4;
    unsigned __int8 v_stack_mE7;
    unsigned __int8 v_stack_mE8;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p120;
    unsigned __int8 v_stack_p128;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p21;
    unsigned int v_stack_p24;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned int v_stack_p8;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;

    *(unsigned __int8 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (208);
    v_r14 = 0;
    v_stack_mE4 = 0;
    result = 0;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 128) = 0;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm0;
    v_stack_mD8 = 0;
    v_stack_mB8 = 0;
    v_stack_mE7 = 0;
    v_stack_m68 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (a4 != 1) goto loc_0086649D;
    v_stack_m70 = *(unsigned __int64 *)(gs_base + (0 + 392)) + 1576;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1576) != 0) goto loc_008661A2;
loc_00865FE8:
    v_stack_mE8 = 1;
    a3 = 0;
    result = KeAbPreAcquire(v_rip + 6888392, 0, a3, a2);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6888359;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 6888347;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_0086604B:
    v_stack_mD0 = *(unsigned __int64 *)(v_rip + 6888452);
    if ((*(unsigned __int64 *)(v_rip + 6888452)) == (v_rip + 6888452)) goto loc_008661AB;
    v_stack_m78 = *(unsigned __int64 *)(v_rip + 6888452) + 16;
    if (sign_flag) goto loc_00866658;
    a1 = (*(unsigned __int64 *)(v_rip + 6888265)) & (-16);
    a2 = *(unsigned __int64 *)(v_rip + 6888265) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6888265))) & (2)) != 0) goto loc_00866191;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6888265))) & (2)) != 0) goto loc_00866191;
loc_008660B1:
    result = KeAbPostRelease(v_rip + 6888216, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    result = 0;
    v_stack_mE8 = 0;
    if ((*(unsigned int *)(v_rip + 6888216)) != 0) goto loc_00866509;
    if ((*(unsigned int *)(v_rip + 5933955)) == 0) goto loc_00866891;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2208), a2, a3, a4);
    if (result != 0) goto loc_00866144;
    result = ExpInterlockedPopEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2216), a2, a3, a4);
    v_rbx = result;
    if (result == 0) {
        a2 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2216) + 44);
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2216) + 48);
        a3 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2216) + 40);
        a1 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2216) + 36);
        result = guard_dispatch_icall(a1, a2, a3, a4);
        v_rbx = result;
    }
    if (v_rbx != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36);
        *(unsigned int *)(v_rbx) = (unsigned int)(result);
    }
    v_stack_mC0 = v_rbx;
    v_r14 = 0;
loc_0086615F:
    if (v_rbx == 0) goto loc_008664BB;
    *(unsigned __int64 *)(v_rbx + 24) = *(unsigned __int64 *)(v_rip + 6888452);
    *(unsigned __int64 *)(v_rbx + 32) = 0;
    *(unsigned __int64 *)(v_rbx + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1576);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1576) = v_rbx + 16;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8))) == a7) goto loc_0086652B;
loc_0086618A:
loc_00866191:
    result = ExfReleasePushLock(v_rip + 6887992, a2, a3, a4);
    goto loc_008660B1;
loc_008661A2:
    goto loc_00865FE8;
loc_008661AB:
    goto loc_00866256;
loc_008661BB:
    *(unsigned __int64 *)(a2) = (unsigned int)(v_stack_mE4);
    *(unsigned __int64 *)((unsigned int)(v_stack_mE4) + 8) = a2;
    result = *(unsigned __int64 *)(v_rip + 3262106);
    if (*(unsigned __int64 *)(v_rip + 3262106) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3262106));
        *(unsigned __int64 *)(v_rip + 3262106) = result;
    }
    if ((*(unsigned int *)(v_rip + 6887961)) != 0) goto loc_00866731;
    if ((*(unsigned int *)(v_rip + 5933700)) == 0) goto loc_0086670B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2208))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2208) + 16)))) goto loc_008667F3;
loc_0086620A:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2208), v_rbx, a3, a4);
loc_00866212:
loc_00866219:
    result = (unsigned int)(((unsigned int)(0xFFFFFFFFULL)) - 1);
    if (((unsigned int)(result)) != 0x80000000ULL) goto loc_0086624A;
    if ((*(unsigned __int64 *)(v_rip + 6887806)) != 0) {
        a2 = 0;
        a1 = v_rip + 6887795;
        result = ExfUnblockPushLock(a1, a2, a3, a4);
    }
    v_rsi = 0;
    v_stack_mE7 = 1;
loc_00866256:
    if (v_stack_mE8 == 0) goto loc_008662B9;
    a1 = (*(unsigned __int64 *)(v_rip + 6887775)) & (-16);
    a2 = *(unsigned __int64 *)(v_rip + 6887775) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6887775))) & (2)) != 0) goto loc_0086648C;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6887775))) & (2)) != 0) goto loc_0086648C;
loc_0086629B:
    result = KeAbPostRelease(v_rip + 6887726, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
loc_008662B9:
loc_008662D6:
    if (0 != 0) goto loc_0086646B;
    if (v_stack_mE7 == 1) goto loc_00866740;
    v_stack_mD8 = v_stack_p10;
    v_stack_mB8 = v_stack_p18;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p8));
loc_00866302:
    if ((*(unsigned __int64 *)(a7)) == a7) goto loc_0086646B;
    v_stack_mC8 = *(unsigned __int64 *)(a7 + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8))) != a7) goto loc_0086618A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 8))) != (*(unsigned __int64 *)(a7 + 8))) goto loc_0086618A;
    *(unsigned __int64 *)(a7 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 8)) = a7;
    v_stack_mD0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 24);
    *(unsigned __int64 *)(v_stack_p10 + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 32);
    result = CmpCallbackFillObjectContext((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))))), v_stack_p10, *(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 24) + 24, v_stack_p10);
    if (v_stack_p18 == 0) goto loc_00866365;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 24) + 20)))) & (1)) == 0) {
        a3 = v_stack_mD8;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 24) + 40)) != (v_rip + 4308)) goto loc_00866388;
    result = VrpRegistryCallback(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 24) + 32), (int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))))), a3, v_rip + 4308);
    goto loc_0086638D;
loc_00866388:
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 24) + 32), (int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))))), a3, v_rip + 4308);
loc_0086638D:
    v_stack_mE4 = (unsigned int)(result);
    goto loc_008663BA;
loc_008663BA:
    result = *(unsigned __int64 *)(v_stack_m68 + 1576);
    if (*(unsigned __int64 *)(v_stack_m68 + 1576) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68 + 1576));
        *(unsigned __int64 *)(v_stack_m68 + 1576) = result;
    }
    if ((*(unsigned int *)(v_rip + 6887441)) != 0) goto loc_008666C5;
    if ((*(unsigned int *)(v_rip + 5933180)) == 0) goto loc_008666A2;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2208))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2208) + 16)))) goto loc_008666D4;
loc_00866412:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2208), *(unsigned __int64 *)(a7 + 8), a3, v_rip + 4308);
loc_0086641A:
    result = (unsigned int)(((unsigned int)(0xFFFFFFFFULL)) - 1);
    if (((unsigned int)(result)) != 0x80000000ULL) goto loc_0086644A;
    if ((*(unsigned __int64 *)(v_rip + 6887294)) != 0) {
        a2 = 0;
        a1 = v_rip + 6887283;
        result = ExfUnblockPushLock(a1, a2, a3, v_rip + 4308);
    }
    if (v_stack_mE4 == 0xC0000503ULL) {
        result = *(unsigned int *)(v_stack_mD8 + 24);
        *(unsigned int *)(v_stack_mD8 + 8) = (unsigned int)(result);
    }
    v_stack_mE4 = 0;
    goto loc_00866302;
loc_0086646B:
    if (v_stack_mE7 == 1) goto loc_0086684E;
loc_00866476:
    v_rsp = (v_rsp) + (208);
    return 0;
loc_0086648C:
    result = ExfReleasePushLock(v_rip + 6887229, v_stack_mD8, a3, v_rip + 4308);
    goto loc_0086629B;
loc_0086649D:
    goto loc_008662D6;
loc_008664BB:
    result = (unsigned int)(((unsigned int)(0xFFFFFFFFULL)) - 1);
    if (((unsigned int)(result)) != 0x80000000ULL) goto loc_008664EC;
    if ((*(unsigned __int64 *)(v_rip + 6887132)) != 0) {
        a2 = 0;
        a1 = v_rip + 6887121;
        result = ExfUnblockPushLock(a1, a2, a3, v_rip + 4308);
    }
    v_stack_p24 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_p21 = 1;
    v_rsi = 0;
    goto loc_00866256;
loc_00866509:
    result = ExAllocatePool2(256, 48, (unsigned int)(0x69634D43ULL), v_rip + 4308);
loc_00866521:
    v_stack_p48 = result;
    goto loc_0086615F;
loc_0086652B:
    *(unsigned __int64 *)(result) = a7;
    v_stack_p40 = result + 8;
    *(unsigned __int64 *)(result + 8) = 256;
    *(unsigned __int64 *)(256) = result;
    *(unsigned __int64 *)(a7 + 8) = result;
    result = CmpCallbackFillObjectContext((unsigned int)(v_stack_p110), v_stack_p118, *(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 24) + 24, v_rip + 4308);
    if (v_stack_p120 != 0) goto loc_00866664;
loc_0086656A:
loc_00866572:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 24) + 40)) == (v_rip + 3783)) goto loc_00866595;
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 24) + 32), (int)(v_stack_p110), v_stack_p118, v_rip + 3783);
    goto loc_0086659A;
loc_00866595:
    result = VrpRegistryCallback(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 24) + 32), (int)(v_stack_p110), v_stack_p118, v_rip + 3783);
loc_0086659A:
    v_stack_p24 = (unsigned int)(result);
    goto loc_008665D6;
loc_008665D6:
    if (((unsigned int)((unsigned int)(v_stack_p110))) != 14) goto loc_00866677;
    v_stack_p24 = 0;
loc_008665EB:
    result = CmpCallbackFetchCallContext((unsigned int)(v_stack_p110), v_stack_p118, result, v_rip + 3783);
    v_stack_p20 = 1;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6886835, a2, a3, v_rip + 3783);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6886802;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 6886790;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    goto loc_0086604B;
loc_00866664:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a7 + 8) + 24) + 20)))) & (1)) == 0) goto loc_0086656A;
    goto loc_00866572;
loc_00866677:
    if (!sign_flag) goto loc_008665EB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) != result) goto loc_0086618A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p40))) != result) goto loc_0086618A;
    goto loc_008661BB;
loc_008666A2:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 7734232))) * (*(unsigned int *)(v_rip + 6853849)));
    if (a1 > 64) { a1 = (unsigned int)(v_rip + 6886785); }
    if (((unsigned int)(*(unsigned __int16 *)(v_rip + 6054595))) < a1) goto loc_0086687D;
loc_008666C5:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a1, a4);
    goto loc_0086641A;
loc_008666D4:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2216))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2216) + 16)))) goto loc_00866412;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2216) + 56)) != (v_rip + 3261260)) goto loc_008668CC;
    result = ExFreePool(result, a2, a1, a4);
    goto loc_0086641A;
loc_0086670B:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 7734127))) * (*(unsigned int *)(v_rip + 6853744)));
    if (a1 > 64) { a1 = 64; }
    if (((unsigned int)(*(unsigned __int16 *)(v_rip + 6054487))) < a1) goto loc_008668AE;
loc_00866731:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a1, a4);
    goto loc_00866212;
loc_00866740:
    result = 0;
    v_stack_p58 = v_xmm0;
    v_stack_p68 = v_xmm0;
    v_stack_p78 = v_xmm0;
    v_stack_p88 = 0;
    v_stack_p30 = v_stack_p58;
    if ((((unsigned int)((unsigned int)(a5) - 27)) & (0xFFFFFFFDULL)) != 0) goto loc_00866831;
    if (0 != 0xC0000503ULL) goto loc_0086686C;
loc_0086678E:
    v_stack_p58 = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72));
loc_00866798:
    if (0 != 0xC0000503ULL) goto loc_00866843;
    if ((((unsigned int)(a1 - 26)) & (0xFFFFFFFDULL)) == 0) goto loc_00866874;
loc_008667B6:
    v_stack_p60 = 0;
loc_008667BA:
    v_stack_p70 = 0;
    v_stack_p68 = a4;
    if (v_stack_p18 == 0) goto loc_00866302;
    v_stack_p50 = v_stack_pA8;
    v_stack_pA8 = v_stack_p58;
    v_stack_pB0 = v_stack_p18;
    goto loc_00866302;
loc_008667F3:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p30 + 2216))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p30 + 2216) + 16)))) goto loc_0086620A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p30 + 2216) + 56)) != (v_rip + 3260469)) goto loc_008668C2;
    result = ExFreePool(0, v_stack_p30, a1, a4);
    goto loc_00866219;
loc_00866831:
    v_stack_p58 = a6;
    goto loc_00866798;
loc_00866843:
    v_stack_p60 = 0;
    goto loc_008667BA;
loc_0086684E:
    if (v_stack_p30 == 0) goto loc_00866476;
    if (sign_flag) goto loc_00866476;
    goto loc_00866476;
loc_0086686C:
    goto loc_0086678E;
loc_00866874:
    goto loc_008667B6;
loc_0086687D:
    result = ExpInterlockedPushEntrySList(v_rip + 6054137, result, a1, a4);
    goto loc_0086641A;
loc_00866891:
    result = ExpInterlockedPopEntrySList(v_rip + 6054120, result, a1, a4);
    if (result != 0) goto loc_00866521;
    goto loc_00866509;
loc_008668AE:
    result = ExpInterlockedPushEntrySList(v_rip + 6054088, result, a1, a4);
    goto loc_00866212;
loc_008668C2:
    result = guard_dispatch_icall(v_rip + 6054088, result, a1, a4);
    goto loc_00866219;
loc_008668CC:
    result = guard_dispatch_icall(v_rip + 6054088, result, a1, a4);
    goto loc_0086641A;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCallCallBacksEx(int32_t Arg1, int64_t Arg2, int64_t Arg3, uint8_t Arg4, void *Arg5, int64_t Arg6, void *Arg7)
{
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m108;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE4;
    uint8_t v_stack_mE7;
    uint8_t v_stack_mE8;
    uint32_t v_stack_p0;
    uint64_t v_stack_p10;
    uint32_t v_stack_p110;
    uint64_t v_stack_p118;
    uint64_t v_stack_p120;
    uint8_t v_stack_p128;
    uint64_t v_stack_p140;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint8_t v_stack_p21;
    uint32_t v_stack_p24;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;
    uint32_t v_stack_p8;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;

    *(uint8_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (208);
    local_r14 = 0;
    v_stack_mE4 = 0;
    result = 0;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x80) = 0;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm0;
    v_stack_mD8 = 0;
    v_stack_mB8 = 0;
    v_stack_mE7 = 0;
    v_stack_m68 = *(uint64_t *)(gs_base + (0 + 0x188));
    if (Arg4 != 1) goto loc_0086649D;
    v_stack_m70 = *(uint64_t *)(gs_base + (0 + 0x188)) + 1576;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x628) != 0) goto loc_008661A2;
loc_00865FE8:
    v_stack_mE8 = 1;
    Arg3 = 0;
    result = KeAbPreAcquire(v_rip + 6888392, 0, Arg3, Arg2);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = v_rip + 6888359;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 6888347;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_0086604B:
    v_stack_mD0 = *(uint64_t *)(v_rip + 0x691C04);
    if ((*(uint64_t *)(v_rip + 0x691C04)) == (v_rip + 6888452)) goto loc_008661AB;
    v_stack_m78 = *(uint64_t *)(v_rip + 0x691C04) + 16;
    if (sign_flag) goto loc_00866658;
    Arg1 = (*(uint64_t *)(v_rip + 0x691B49)) & (-16);
    Arg2 = *(uint64_t *)(v_rip + 0x691B49) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x691B49))) & (2)) != 0) goto loc_00866191;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x691B49))) & (2)) != 0) goto loc_00866191;
loc_008660B1:
    result = KeAbPostRelease(v_rip + 6888216, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    result = 0;
    v_stack_mE8 = 0;
    if ((*(uint32_t *)(v_rip + 0x691B18)) != 0) goto loc_00866509;
    if ((*(uint32_t *)(v_rip + 0x5A8B83)) == 0) goto loc_00866891;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A0), Arg2, Arg3, Arg4);
    if (result != 0) goto loc_00866144;
    result = ExpInterlockedPopEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A8), Arg2, Arg3, Arg4);
    local_rbx = result;
    if (result == 0) {
        Arg2 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A8) + 0x2C);
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A8) + 0x30);
        Arg3 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A8) + 0x28);
        Arg1 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A8) + 0x24);
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
        local_rbx = result;
    }
    if (local_rbx != 0) {
        result = *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24);
        *(uint32_t *)(local_rbx) = (uint32_t)(result);
    }
    v_stack_mC0 = local_rbx;
    local_r14 = 0;
loc_0086615F:
    if (local_rbx == 0) goto loc_008664BB;
    *(uint64_t *)(local_rbx + 0x18) = *(uint64_t *)(v_rip + 0x691C04);
    *(uint64_t *)(local_rbx + 0x20) = 0;
    *(uint64_t *)(local_rbx + 0x10) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x628);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x628) = local_rbx + 16;
    if ((*(uint64_t *)(*(uint64_t *)(arg7 + 0x8))) == Arg7) goto loc_0086652B;
loc_0086618A:
loc_00866191:
    result = ExfReleasePushLock(v_rip + 6887992, Arg2, Arg3, Arg4);
    goto loc_008660B1;
loc_008661A2:
    goto loc_00865FE8;
loc_008661AB:
    goto loc_00866256;
loc_008661BB:
    *(uint64_t *)(Arg2) = (uint32_t)(v_stack_mE4);
    *(uint64_t *)((uint32_t)(v_stack_mE4) + 0x8) = Arg2;
    result = *(uint64_t *)(v_rip + 0x31C69A);
    if (*(uint64_t *)(v_rip + 0x31C69A) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x31C69A));
        *(uint64_t *)(v_rip + 0x31C69A) = result;
    }
    if ((*(uint32_t *)(v_rip + 0x691A19)) != 0) goto loc_00866731;
    if ((*(uint32_t *)(v_rip + 0x5A8A84)) == 0) goto loc_0086670B;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A0))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A0) + 0x10)))) goto loc_008667F3;
loc_0086620A:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A0), local_rbx, Arg3, Arg4);
loc_00866212:
loc_00866219:
    result = (uint32_t)(((uint32_t)(0xFFFFFFFFULL)) - 1);
    if (((uint32_t)(result)) != 0x80000000ULL) goto loc_0086624A;
    if ((*(uint64_t *)(v_rip + 0x69197E)) != 0) {
        Arg2 = 0;
        Arg1 = v_rip + 6887795;
        result = ExfUnblockPushLock(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsi = 0;
    v_stack_mE7 = 1;
loc_00866256:
    if (v_stack_mE8 == 0) goto loc_008662B9;
    Arg1 = (*(uint64_t *)(v_rip + 0x69195F)) & (-16);
    Arg2 = *(uint64_t *)(v_rip + 0x69195F) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x69195F))) & (2)) != 0) goto loc_0086648C;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x69195F))) & (2)) != 0) goto loc_0086648C;
loc_0086629B:
    result = KeAbPostRelease(v_rip + 6887726, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
loc_008662B9:
loc_008662D6:
    if (0 != 0) goto loc_0086646B;
    if (v_stack_mE7 == 1) goto loc_00866740;
    v_stack_mD8 = v_stack_p10;
    v_stack_mB8 = v_stack_p18;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p8));
loc_00866302:
    if ((*(uint64_t *)(arg7)) == Arg7) goto loc_0086646B;
    v_stack_mC8 = *(uint64_t *)(arg7 + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(arg7 + 0x8))) != Arg7) goto loc_0086618A;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x8))) != (*(uint64_t *)(arg7 + 0x8))) goto loc_0086618A;
    *(uint64_t *)(arg7 + 0x8) = *(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x8);
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x8)) = Arg7;
    v_stack_mD0 = *(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x18);
    *(uint64_t *)(v_stack_p10 + 0x20) = *(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x20);
    result = CmpCallbackFillObjectContext((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))))), v_stack_p10, *(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x18) + 24, v_stack_p10);
    if (v_stack_p18 == 0) goto loc_00866365;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x18) + 0x14)))) & (1)) == 0) {
        Arg3 = v_stack_mD8;
    }
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x18) + 0x28)) != (v_rip + 4308)) goto loc_00866388;
    result = VrpRegistryCallback(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x18) + 0x20), (int32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))))), Arg3, v_rip + 4308);
    goto loc_0086638D;
loc_00866388:
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x18) + 0x20), (int32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))))), Arg3, v_rip + 4308);
loc_0086638D:
    v_stack_mE4 = (uint32_t)(result);
    goto loc_008663BA;
loc_008663BA:
    result = *(uint64_t *)(v_stack_m68 + 0x628);
    if (*(uint64_t *)(v_stack_m68 + 0x628) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(v_stack_m68 + 0x628));
        *(uint64_t *)(v_stack_m68 + 0x628) = result;
    }
    if ((*(uint32_t *)(v_rip + 0x691811)) != 0) goto loc_008666C5;
    if ((*(uint32_t *)(v_rip + 0x5A887C)) == 0) goto loc_008666A2;
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A0))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A0) + 0x10)))) goto loc_008666D4;
loc_00866412:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A0), *(uint64_t *)(arg7 + 0x8), Arg3, v_rip + 4308);
loc_0086641A:
    result = (uint32_t)(((uint32_t)(0xFFFFFFFFULL)) - 1);
    if (((uint32_t)(result)) != 0x80000000ULL) goto loc_0086644A;
    if ((*(uint64_t *)(v_rip + 0x69177E)) != 0) {
        Arg2 = 0;
        Arg1 = v_rip + 6887283;
        result = ExfUnblockPushLock(Arg1, Arg2, Arg3, v_rip + 4308);
    }
    if (v_stack_mE4 == 0xC0000503ULL) {
        result = *(uint32_t *)(v_stack_mD8 + 0x18);
        *(uint32_t *)(v_stack_mD8 + 0x8) = (uint32_t)(result);
    }
    v_stack_mE4 = 0;
    goto loc_00866302;
loc_0086646B:
    if (v_stack_mE7 == 1) goto loc_0086684E;
loc_00866476:
    local_rsp = (local_rsp) + (208);
    return 0;
loc_0086648C:
    result = ExfReleasePushLock(v_rip + 6887229, v_stack_mD8, Arg3, v_rip + 4308);
    goto loc_0086629B;
loc_0086649D:
    goto loc_008662D6;
loc_008664BB:
    result = (uint32_t)(((uint32_t)(0xFFFFFFFFULL)) - 1);
    if (((uint32_t)(result)) != 0x80000000ULL) goto loc_008664EC;
    if ((*(uint64_t *)(v_rip + 0x6916DC)) != 0) {
        Arg2 = 0;
        Arg1 = v_rip + 6887121;
        result = ExfUnblockPushLock(Arg1, Arg2, Arg3, v_rip + 4308);
    }
    v_stack_p24 = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_p21 = 1;
    local_rsi = 0;
    goto loc_00866256;
loc_00866509:
    result = ExAllocatePool2(256, 48, (uint32_t)(0x69634D43ULL), v_rip + 4308);
loc_00866521:
    v_stack_p48 = result;
    goto loc_0086615F;
loc_0086652B:
    *(void **)(result) = Arg7;
    v_stack_p40 = result + 8;
    *(uint64_t *)(result + 0x8) = 256;
    *(uint64_t *)(256) = result;
    *(uint64_t *)(arg7 + 0x8) = result;
    result = CmpCallbackFillObjectContext((uint32_t)(v_stack_p110), v_stack_p118, *(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x18) + 24, v_rip + 4308);
    if (v_stack_p120 != 0) goto loc_00866664;
loc_0086656A:
loc_00866572:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x18) + 0x28)) == (v_rip + 3783)) goto loc_00866595;
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x18) + 0x20), (int32_t)(v_stack_p110), v_stack_p118, v_rip + 3783);
    goto loc_0086659A;
loc_00866595:
    result = VrpRegistryCallback(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x18) + 0x20), (int32_t)(v_stack_p110), v_stack_p118, v_rip + 3783);
loc_0086659A:
    v_stack_p24 = (uint32_t)(result);
    goto loc_008665D6;
loc_008665D6:
    if (((uint32_t)((uint32_t)(v_stack_p110))) != 14) goto loc_00866677;
    v_stack_p24 = 0;
loc_008665EB:
    result = CmpCallbackFetchCallContext((uint32_t)(v_stack_p110), v_stack_p118, result, v_rip + 3783);
    v_stack_p20 = 1;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6886835, Arg2, Arg3, v_rip + 3783);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = v_rip + 6886802;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 6886790;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    goto loc_0086604B;
loc_00866664:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg7 + 0x8) + 0x18) + 0x14)))) & (1)) == 0) goto loc_0086656A;
    goto loc_00866572;
loc_00866677:
    if (!sign_flag) goto loc_008665EB;
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) != result) goto loc_0086618A;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p40))) != result) goto loc_0086618A;
    goto loc_008661BB;
loc_008666A2:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x7603D8))) * (*(uint32_t *)(v_rip + 0x6894D9)));
    if (Arg1 > 64) { Arg1 = (uint32_t)(v_rip + 6886785); }
    if (((uint32_t)(*(uint16_t *)(v_rip + 0x5C62C3))) < Arg1) goto loc_0086687D;
loc_008666C5:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg1, Arg4);
    goto loc_0086641A;
loc_008666D4:
    if ((*(uint16_t *)(*(uint64_t *)(Arg2 + 0x8A8))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg2 + 0x8A8) + 0x10)))) goto loc_00866412;
    if ((*(uint64_t *)(*(uint64_t *)(Arg2 + 0x8A8) + 0x38)) != (v_rip + 3261260)) goto loc_008668CC;
    result = ExFreePool(result, Arg2, Arg1, Arg4);
    goto loc_0086641A;
loc_0086670B:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x76036F))) * (*(uint32_t *)(v_rip + 0x689470)));
    if (Arg1 > 64) { Arg1 = 64; }
    if (((uint32_t)(*(uint16_t *)(v_rip + 0x5C6257))) < Arg1) goto loc_008668AE;
loc_00866731:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg1, Arg4);
    goto loc_00866212;
loc_00866740:
    result = 0;
    v_stack_p58 = v_xmm0;
    v_stack_p68 = v_xmm0;
    v_stack_p78 = v_xmm0;
    v_stack_p88 = 0;
    v_stack_p30 = v_stack_p58;
    if ((((uint32_t)((uint32_t)(Arg5) - 27)) & (0xFFFFFFFDULL)) != 0) goto loc_00866831;
    if (0 != 0xC0000503ULL) goto loc_0086686C;
loc_0086678E:
    v_stack_p58 = *(uint64_t *)(*(uint64_t *)(Arg4 + 0x48));
loc_00866798:
    if (0 != 0xC0000503ULL) goto loc_00866843;
    if ((((uint32_t)(Arg1 - 26)) & (0xFFFFFFFDULL)) == 0) goto loc_00866874;
loc_008667B6:
    v_stack_p60 = 0;
loc_008667BA:
    v_stack_p70 = 0;
    v_stack_p68 = Arg4;
    if (v_stack_p18 == 0) goto loc_00866302;
    v_stack_p50 = v_stack_pA8;
    v_stack_pA8 = v_stack_p58;
    v_stack_pB0 = v_stack_p18;
    goto loc_00866302;
loc_008667F3:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p30 + 0x8A8))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p30 + 0x8A8) + 0x10)))) goto loc_0086620A;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p30 + 0x8A8) + 0x38)) != (v_rip + 3260469)) goto loc_008668C2;
    result = ExFreePool(0, v_stack_p30, Arg1, Arg4);
    goto loc_00866219;
loc_00866831:
    v_stack_p58 = Arg6;
    goto loc_00866798;
loc_00866843:
    v_stack_p60 = 0;
    goto loc_008667BA;
loc_0086684E:
    if (v_stack_p30 == 0) goto loc_00866476;
    if (sign_flag) goto loc_00866476;
    goto loc_00866476;
loc_0086686C:
    goto loc_0086678E;
loc_00866874:
    goto loc_008667B6;
loc_0086687D:
    result = ExpInterlockedPushEntrySList(v_rip + 6054137, result, Arg1, Arg4);
    goto loc_0086641A;
loc_00866891:
    result = ExpInterlockedPopEntrySList(v_rip + 6054120, result, Arg1, Arg4);
    if (result != 0) goto loc_00866521;
    goto loc_00866509;
loc_008668AE:
    result = ExpInterlockedPushEntrySList(v_rip + 6054088, result, Arg1, Arg4);
    goto loc_00866212;
loc_008668C2:
    result = guard_dispatch_icall(v_rip + 6054088, result, Arg1, Arg4);
    goto loc_00866219;
loc_008668CC:
    result = guard_dispatch_icall(v_rip + 6054088, result, Arg1, Arg4);
    goto loc_0086641A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `- 0x1B` | `32` | `R` |
| `Arg7` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x8` | `64` | `R` |
| `Arg7` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00865F40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
