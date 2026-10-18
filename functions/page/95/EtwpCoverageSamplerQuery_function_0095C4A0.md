# EtwpCoverageSamplerQuery

- RVA: `0x0095C4A0`–`0x0095D2D0` (길이 `3,632` bytes)
- VA: `0x000000014095C4A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00092CF4`
- 디코드: `824`개 명령, `3,632/3,632` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **44**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0095C540` → [EtwpCovSampAcquireSamplerRundown](../8D/EtwpCovSampAcquireSamplerRundown_function_008D7F7C.md) (function, `0x008D7F7C`)
- `0x0095C56A` → [EtwpCovSampCaptureFlushSampleBuffers](../../text/43/EtwpCovSampCaptureFlushSampleBuffers_function_0043C0B4.md) (function, `0x0043C0B4`)
- `0x0095C57D` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0095C5A8` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x0095C5B8` → [EtwpCovSampCaptureQueueBuffer](../../text/46/EtwpCovSampCaptureQueueBuffer_function_004620D0.md) (function, `0x004620D0`)
- `0x0095C5D2` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0095C5F4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0095C60D` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0095C6E8` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0095C709` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0095C826` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0095C82B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0095CAF7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0095CB12` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0095CB49` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0095CB65` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0095CB6F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0095CB74` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0095CBC7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0095CBE2` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0095CC19` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0095CC35` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0095CC3F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0095CC44` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0095CCB7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0095CD95` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0095CDE6` → [RtlStringCchCopyNW](../../text/47/RtlStringCchCopyNW_function_0047169C.md) (function, `0x0047169C`)
- `0x0095CE4B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0095CE67` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0095CEE9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0095CEEE` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0095CF33` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0095CFD2` → [EtwpCovSampCaptureFlushStats](../AA/EtwpCovSampCaptureFlushStats_function_00AAF6C0.md) (function, `0x00AAF6C0`)
- `0x0095D0B1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0095D0B6` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0095D0BE` → [EtwpCovSampContextPruneModules](../8D/EtwpCovSampContextPruneModules_function_008DA03C.md) (function, `0x008DA03C`)
- `0x0095D118` → [EtwpCovSampReleaseSamplerRundown](../8D/EtwpCovSampReleaseSamplerRundown_function_008D7850.md) (function, `0x008D7850`)
- `0x0095D12A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0095D176` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0095D1D7` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0095D209` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0095D259` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0095D28C` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0095D2AF` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)

### Direct callers
- [EtwpQueryCoverageSamplerInformation](EtwpQueryCoverageSamplerInformation_function_0095D2D8.md) at `0x0095D3A4`

### Static image references
- `0x0095C4B5` → RVA `0x00E0A740` (`.data`; read)
- `0x0095C4ED` → RVA `0x00EFF1E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **40**
  - `0x0095C56A` → [EtwpCovSampCaptureFlushSampleBuffers](../../text/43/EtwpCovSampCaptureFlushSampleBuffers_function_0043C0B4.md) (`PAGE` → `.text`)
  - `0x0095C57D` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0095C5A8` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x0095C5B8` → [EtwpCovSampCaptureQueueBuffer](../../text/46/EtwpCovSampCaptureQueueBuffer_function_004620D0.md) (`PAGE` → `.text`)
  - `0x0095C5D2` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x0095C5F4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0095C60D` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0095C6E8` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0095C709` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0095C826` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0095C82B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0095CAF7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0095CB12` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0095CB49` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0095CB65` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0095CB6F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0095CB74` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0095CBC7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0095CBE2` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0095CC19` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0095CC35` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0095CC3F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0095CC44` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0095CCB7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0095CD95` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0095CDE6` → [RtlStringCchCopyNW](../../text/47/RtlStringCchCopyNW_function_0047169C.md) (`PAGE` → `.text`)
  - `0x0095CE4B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0095CE67` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0095CEE9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0095CEEE` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0095CF33` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0095D0B1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0095D0B6` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0095D12A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0095D176` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0095D1D7` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0095D209` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0095D259` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0095D28C` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0095D2AF` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x0095D219` → [sub_00B27A94](../B2/Unknown_function_00B27A94.md) (`tail-transfer`)
  - `0x0095D243` → [sub_00B27A94 + 0x13](../B2/Unknown_function_00B27A94.md) (`tail-transfer`)
  - `0x0095D27F` → [sub_00B27A94 + 0x4C](../B2/Unknown_function_00B27A94.md) (`tail-transfer`)
  - `0x0095D292` → [sub_00B27A94 + 0x4C](../B2/Unknown_function_00B27A94.md) (`tail-transfer`)
  - `0x0095D2A6` → [sub_00B27A94 + 0x63](../B2/Unknown_function_00B27A94.md) (`tail-transfer`)
  - `0x0095D2B5` → [sub_00B27A94 + 0x63](../B2/Unknown_function_00B27A94.md) (`tail-transfer`)
  - `0x0095D2C0` → [sub_00B27A94 + 0x87](../B2/Unknown_function_00B27A94.md) (`tail-transfer`)
  - `0x0095D2CB` → [sub_00B27A94 + 0x76](../B2/Unknown_function_00B27A94.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0095C4A0  4C 8B DC                        mov r11, rsp
0095C4A3  53                              push rbx
0095C4A4  56                              push rsi
0095C4A5  57                              push rdi
0095C4A6  41 54                           push r12
0095C4A8  41 55                           push r13
0095C4AA  41 56                           push r14
0095C4AC  41 57                           push r15
0095C4AE  48 81 EC E0 01 00 00            sub rsp, 0x1e0
0095C4B5  48 8B 05 84 E2 4A 00            mov rax, qword ptr [rip + 0x4ae284]
0095C4BC  48 33 C4                        xor rax, rsp
0095C4BF  48 89 84 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rax
0095C4C7  4C 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r9
0095C4CF  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
0095C4D4  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
0095C4D9  4C 8B F1                        mov r14, rcx
0095C4DC  48 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rcx
0095C4E4  33 F6                           xor esi, esi
0095C4E6  49 89 B3 98 FE FF FF            mov qword ptr [r11 - 0x168], rsi
0095C4ED  48 8B 1D F4 2C 5A 00            mov rbx, qword ptr [rip + 0x5a2cf4]
0095C4F4  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
0095C4FC  0F 57 C0                        xorps xmm0, xmm0
0095C4FF  41 0F 11 43 98                  movups xmmword ptr [r11 - 0x68], xmm0
0095C504  41 0F 11 43 A8                  movups xmmword ptr [r11 - 0x58], xmm0
0095C509  4C 8D 69 10                     lea r13, [rcx + 0x10]
0095C50D  4C 89 AC 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], r13
0095C515  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0095C51A  49 89 B3 A8 FE FF FF            mov qword ptr [r11 - 0x158], rsi
0095C521  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
0095C529  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
0095C52D  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
0095C532  49 89 B3 B0 FE FF FF            mov qword ptr [r11 - 0x150], rsi
0095C539  49 8D 8B 98 FE FF FF            lea rcx, [r11 - 0x168]
0095C540  E8 37 BA F7 FF                  call 0x1408d7f7c
0095C545  8B F8                           mov edi, eax
0095C547  85 C0                           test eax, eax
0095C549  0F 88 36 0C 00 00               js 0x14095d185
0095C54F  4C 39 B4 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], r14
0095C557  0F 85 23 0C 00 00               jne 0x14095d180
0095C55D  33 C0                           xor eax, eax
0095C55F  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
0095C567  48 8B CB                        mov rcx, rbx
0095C56A  E8 45 FB AD FF                  call 0x14043c0b4
0095C56F  33 D2                           xor edx, edx
0095C571  44 8D 46 50                     lea r8d, [rsi + 0x50]
0095C575  48 8D 8C 24 60 01 00 00         lea rcx, [rsp + 0x160]
0095C57D  E8 BE A6 D6 FF                  call 0x1406c6c40
0095C582  B8 FA BF A5 F1                  mov eax, 0xf1a5bffa
0095C587  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
0095C58F  48 C7 84 24 60 01 00 00 1D 1B 00 00  mov qword ptr [rsp + 0x160], 0x1b1d
0095C59B  45 33 C0                        xor r8d, r8d
0095C59E  33 D2                           xor edx, edx
0095C5A0  48 8D 8C 24 90 01 00 00         lea rcx, [rsp + 0x190]
0095C5A8  E8 63 17 AB FF                  call 0x14040dd10
0095C5AD  48 8D 94 24 60 01 00 00         lea rdx, [rsp + 0x160]
0095C5B5  48 8B CB                        mov rcx, rbx
0095C5B8  E8 13 5B B0 FF                  call 0x1404620d0
0095C5BD  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0095C5C2  45 33 C9                        xor r9d, r9d
0095C5C5  45 33 C0                        xor r8d, r8d
0095C5C8  33 D2                           xor edx, edx
0095C5CA  48 8D 8C 24 90 01 00 00         lea rcx, [rsp + 0x190]
0095C5D2  E8 D9 20 8B FF                  call 0x14020e6b0
0095C5D7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0095C5E0  48 83 CB FF                     or rbx, 0xffffffffffffffff
0095C5E4  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
0095C5EB  90                              nop
0095C5EC  45 33 C0                        xor r8d, r8d
0095C5EF  33 D2                           xor edx, edx
0095C5F1  49 8B CE                        mov rcx, r14
0095C5F4  E8 37 3C 8B FF                  call 0x140210230
0095C5F9  48 8B F8                        mov rdi, rax
0095C5FC  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
0095C602  73 0E                           jae 0x14095c612
0095C604  4D 8B C6                        mov r8, r14
0095C607  48 8B D0                        mov rdx, rax
0095C60A  49 8B CE                        mov rcx, r14
0095C60D  E8 7E 36 8B FF                  call 0x14020fc90
0095C612  41 BF 01 00 00 00               mov r15d, 1
0095C618  48 85 FF                        test rdi, rdi
0095C61B  74 04                           je 0x14095c621
0095C61D  44 88 7F 0A                     mov byte ptr [rdi + 0xa], r15b
0095C621  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0095C62A  49 89 46 08                     mov qword ptr [r14 + 8], rax
0095C62E  8B D6                           mov edx, esi
0095C630  89 54 24 68                     mov dword ptr [rsp + 0x68], edx
0095C634  49 8D 8E 90 06 00 00            lea rcx, [r14 + 0x690]
0095C63B  48 8B 01                        mov rax, qword ptr [rcx]
0095C63E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0095C643  48 3B C1                        cmp rax, rcx
0095C646  0F 85 4B 0B 00 00               jne 0x14095d197
0095C64C  8B C2                           mov eax, edx
0095C64E  48 C1 E0 03                     shl rax, 3
0095C652  BA FF FF FF FF                  mov edx, 0xffffffff
0095C657  8B CA                           mov ecx, edx
0095C659  48 3B C2                        cmp rax, rdx
0095C65C  0F 46 C8                        cmovbe ecx, eax
0095C65F  48 3B D0                        cmp rdx, rax
0095C662  1B FF                           sbb edi, edi
0095C664  41 B8 95 00 00 C0               mov r8d, 0xc0000095
0095C66A  41 23 F8                        and edi, r8d
0095C66D  48 3B C2                        cmp rax, rdx
0095C670  0F 87 19 0B 00 00               ja 0x14095d18f
0095C676  8D 81 D0 04 00 00               lea eax, [rcx + 0x4d0]
0095C67C  3B C1                           cmp eax, ecx
0095C67E  0F 43 D0                        cmovae edx, eax
0095C681  89 54 24 70                     mov dword ptr [rsp + 0x70], edx
0095C685  1B FF                           sbb edi, edi
0095C687  41 23 F8                        and edi, r8d
0095C68A  3B C1                           cmp eax, ecx
0095C68C  0F 82 FD 0A 00 00               jb 0x14095d18f
0095C692  8B C6                           mov eax, esi
0095C694  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0095C698  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0095C69C  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
0095C6A0  89 74 24 54                     mov dword ptr [rsp + 0x54], esi
0095C6A4  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
0095C6A8  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
0095C6B0  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
0095C6B8  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
0095C6C0  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0095C6C8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0095C6D1  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
0095C6D8  90                              nop
0095C6D9  49 8D BD 98 04 00 00            lea rdi, [r13 + 0x498]
0095C6E0  45 33 C0                        xor r8d, r8d
0095C6E3  33 D2                           xor edx, edx
0095C6E5  48 8B CF                        mov rcx, rdi
0095C6E8  E8 43 3B 8B FF                  call 0x140210230
0095C6ED  4C 8B E0                        mov r12, rax
0095C6F0  B9 11 00 00 00                  mov ecx, 0x11
0095C6F5  33 C0                           xor eax, eax
0095C6F7  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
0095C6FC  74 10                           je 0x14095c70e
0095C6FE  4C 8B CF                        mov r9, rdi
0095C701  4D 8B C4                        mov r8, r12
0095C704  33 D2                           xor edx, edx
0095C706  48 8B CF                        mov rcx, rdi
0095C709  E8 3E 3D 8B FF                  call 0x14021044c
0095C70E  4D 85 E4                        test r12, r12
0095C711  74 05                           je 0x14095c718
0095C713  45 88 7C 24 0A                  mov byte ptr [r12 + 0xa], r15b
0095C718  4D 8D 95 C8 04 00 00            lea r10, [r13 + 0x4c8]
0095C71F  4D 8B 02                        mov r8, qword ptr [r10]
0095C722  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
0095C727  44 8B E6                        mov r12d, esi
0095C72A  44 8B DE                        mov r11d, esi
0095C72D  4C 8B 8C 24 98 00 00 00         mov r9, qword ptr [rsp + 0x98]
0095C735  49 8B D0                        mov rdx, r8
0095C738  4D 3B C2                        cmp r8, r10
0095C73B  0F 84 7C 0A 00 00               je 0x14095d1bd
0095C741  4D 8B 00                        mov r8, qword ptr [r8]
0095C744  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
0095C749  39 72 3C                        cmp dword ptr [rdx + 0x3c], esi
0095C74C  75 09                           jne 0x14095c757
0095C74E  F7 42 30 00 00 10 00            test dword ptr [rdx + 0x30], 0x100000
0095C755  74 DE                           je 0x14095c735
0095C757  48 39 72 20                     cmp qword ptr [rdx + 0x20], rsi
0095C75B  75 16                           jne 0x14095c773
0095C75D  4C 39 7A F8                     cmp qword ptr [rdx - 8], r15
0095C761  0F 84 49 0A 00 00               je 0x14095d1b0
0095C767  8B C6                           mov eax, esi
0095C769  87 42 3C                        xchg dword ptr [rdx + 0x3c], eax
0095C76C  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
0095C771  EB BA                           jmp 0x14095c72d
0095C773  45 03 E7                        add r12d, r15d
0095C776  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
0095C77B  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
0095C780  44 01 7C 24 30                  add dword ptr [rsp + 0x30], r15d
0095C785  8B 42 30                        mov eax, dword ptr [rdx + 0x30]
0095C788  0F B7 C8                        movzx ecx, ax
0095C78B  8D 0C 4D 02 00 00 00            lea ecx, [rcx*2 + 2]
0095C792  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
0095C796  03 C1                           add eax, ecx
0095C798  BF FF FF FF FF                  mov edi, 0xffffffff
0095C79D  3B C1                           cmp eax, ecx
0095C79F  0F 43 F8                        cmovae edi, eax
0095C7A2  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
0095C7A6  1B FF                           sbb edi, edi
0095C7A8  81 E7 95 00 00 C0               and edi, 0xc0000095
0095C7AE  3B C1                           cmp eax, ecx
0095C7B0  0F 82 D9 09 00 00               jb 0x14095d18f
0095C7B6  8B 4A F0                        mov ecx, dword ptr [rdx - 0x10]
0095C7B9  8D 41 FF                        lea eax, [rcx - 1]
0095C7BC  83 E0 03                        and eax, 3
0095C7BF  2B C8                           sub ecx, eax
0095C7C1  83 C1 03                        add ecx, 3
0095C7C4  42 8D 04 19                     lea eax, [rcx + r11]
0095C7C8  41 BB FF FF FF FF               mov r11d, 0xffffffff
0095C7CE  3B C1                           cmp eax, ecx
0095C7D0  44 0F 43 D8                     cmovae r11d, eax
0095C7D4  44 89 5C 24 50                  mov dword ptr [rsp + 0x50], r11d
0095C7D9  1B FF                           sbb edi, edi
0095C7DB  81 E7 95 00 00 C0               and edi, 0xc0000095
0095C7E1  3B C1                           cmp eax, ecx
0095C7E3  0F 82 A6 09 00 00               jb 0x14095d18f
0095C7E9  48 83 C2 48                     add rdx, 0x48
0095C7ED  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
0095C7F5  49 39 01                        cmp qword ptr [r9], rax
0095C7F8  74 07                           je 0x14095c801
0095C7FA  B9 03 00 00 00                  mov ecx, 3
0095C7FF  CD 29                           int 0x29
0095C801  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
0095C809  48 89 02                        mov qword ptr [rdx], rax
0095C80C  4C 89 4A 08                     mov qword ptr [rdx + 8], r9
0095C810  49 89 11                        mov qword ptr [r9], rdx
0095C813  4C 8B CA                        mov r9, rdx
0095C816  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
0095C81E  E9 12 FF FF FF                  jmp 0x14095c735
0095C823  48 8B CF                        mov rcx, rdi
0095C826  E8 D5 4D 98 FF                  call 0x1402e1600
0095C82B  E8 80 10 90 FF                  call 0x14025d8b0
0095C830  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0095C834  48 8D 0C 40                     lea rcx, [rax + rax*2]
0095C838  48 C1 E1 04                     shl rcx, 4
0095C83C  41 B9 FF FF FF FF               mov r9d, 0xffffffff
0095C842  41 8B C1                        mov eax, r9d
0095C845  49 3B C9                        cmp rcx, r9
0095C848  0F 46 C1                        cmovbe eax, ecx
0095C84B  4C 3B C9                        cmp r9, rcx
0095C84E  1B FF                           sbb edi, edi
0095C850  41 B8 95 00 00 C0               mov r8d, 0xc0000095
0095C856  41 23 F8                        and edi, r8d
0095C859  49 3B C9                        cmp rcx, r9
0095C85C  0F 87 2D 09 00 00               ja 0x14095d18f
0095C862  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
0095C866  03 C1                           add eax, ecx
0095C868  41 8B D1                        mov edx, r9d
0095C86B  3B C1                           cmp eax, ecx
0095C86D  0F 43 D0                        cmovae edx, eax
0095C870  1B FF                           sbb edi, edi
0095C872  41 23 F8                        and edi, r8d
0095C875  3B C1                           cmp eax, ecx
0095C877  0F 82 12 09 00 00               jb 0x14095d18f
0095C87D  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
0095C881  03 C2                           add eax, edx
0095C883  41 8B C9                        mov ecx, r9d
0095C886  3B C2                           cmp eax, edx
0095C888  0F 43 C8                        cmovae ecx, eax
0095C88B  1B FF                           sbb edi, edi
0095C88D  41 23 F8                        and edi, r8d
0095C890  3B C2                           cmp eax, edx
0095C892  0F 82 F7 08 00 00               jb 0x14095d18f
0095C898  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0095C89C  03 C1                           add eax, ecx
0095C89E  41 8B D1                        mov edx, r9d
0095C8A1  3B C1                           cmp eax, ecx
0095C8A3  0F 43 D0                        cmovae edx, eax
0095C8A6  89 54 24 70                     mov dword ptr [rsp + 0x70], edx
0095C8AA  1B FF                           sbb edi, edi
0095C8AC  41 23 F8                        and edi, r8d
0095C8AF  3B C1                           cmp eax, ecx
0095C8B1  0F 82 D8 08 00 00               jb 0x14095d18f
0095C8B7  39 54 24 38                     cmp dword ptr [rsp + 0x38], edx
0095C8BB  0F 82 20 09 00 00               jb 0x14095d1e1
0095C8C1  45 85 E4                        test r12d, r12d
0095C8C4  0F 85 28 09 00 00               jne 0x14095d1f2
0095C8CA  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0095C8CF  8B 40 10                        mov eax, dword ptr [rax + 0x10]
0095C8D2  41 84 C7                        test r15b, al
0095C8D5  0F 85 CE 01 00 00               jne 0x14095caa9
0095C8DB  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0095C8E0  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0095C8E5  48 8D 50 14                     lea rdx, [rax + 0x14]
0095C8E9  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
0095C8EE  4C 8B E2                        mov r12, rdx
0095C8F1  48 89 94 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdx
0095C8F9  48 83 C2 2C                     add rdx, 0x2c
0095C8FD  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
0095C902  0F 57 C0                        xorps xmm0, xmm0
0095C905  33 C0                           xor eax, eax
0095C907  41 0F 11 04 24                  movups xmmword ptr [r12], xmm0
0095C90C  41 0F 11 44 24 10               movups xmmword ptr [r12 + 0x10], xmm0
0095C912  49 89 44 24 20                  mov qword ptr [r12 + 0x20], rax
0095C917  41 89 44 24 28                  mov dword ptr [r12 + 0x28], eax
0095C91C  41 C7 04 24 2C 00 00 00         mov dword ptr [r12], 0x2c
0095C924  41 8B 86 BC 06 00 00            mov eax, dword ptr [r14 + 0x6bc]
0095C92B  41 89 44 24 08                  mov dword ptr [r12 + 8], eax
0095C930  41 B8 54 04 00 00               mov r8d, 0x454
0095C936  45 89 44 24 10                  mov dword ptr [r12 + 0x10], r8d
0095C93B  8B C2                           mov eax, edx
0095C93D  41 2B C4                        sub eax, r12d
0095C940  41 89 44 24 0C                  mov dword ptr [r12 + 0xc], eax
0095C945  48 8B CA                        mov rcx, rdx
0095C948  48 89 94 24 30 01 00 00         mov qword ptr [rsp + 0x130], rdx
0095C950  49 03 D0                        add rdx, r8
0095C953  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
0095C958  49 8D 45 08                     lea rax, [r13 + 8]
0095C95C  41 B8 08 00 00 00               mov r8d, 8
0095C962  45 8D 48 78                     lea r9d, [r8 + 0x78]
0095C966  0F 10 00                        movups xmm0, xmmword ptr [rax]
0095C969  0F 11 01                        movups xmmword ptr [rcx], xmm0
0095C96C  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
0095C970  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
0095C974  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
0095C978  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
0095C97C  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
0095C980  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
0095C984  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
0095C988  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
0095C98C  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
0095C990  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
0095C994  0F 10 40 60                     movups xmm0, xmmword ptr [rax + 0x60]
0095C998  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
0095C99C  49 03 C9                        add rcx, r9
0095C99F  0F 10 48 70                     movups xmm1, xmmword ptr [rax + 0x70]
0095C9A3  0F 11 49 F0                     movups xmmword ptr [rcx - 0x10], xmm1
0095C9A7  49 03 C1                        add rax, r9
0095C9AA  49 83 E8 01                     sub r8, 1
0095C9AE  75 B6                           jne 0x14095c966
0095C9B0  0F 10 00                        movups xmm0, xmmword ptr [rax]
0095C9B3  0F 11 01                        movups xmmword ptr [rcx], xmm0
0095C9B6  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
0095C9BA  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
0095C9BE  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
0095C9C2  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
0095C9C6  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
0095C9CA  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
0095C9CE  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
0095C9D2  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
0095C9D6  8B 40 50                        mov eax, dword ptr [rax + 0x50]
0095C9D9  89 41 50                        mov dword ptr [rcx + 0x50], eax
0095C9DC  41 C7 44 24 18 3C 00 00 00      mov dword ptr [r12 + 0x18], 0x3c
0095C9E5  8B C2                           mov eax, edx
0095C9E7  41 2B C4                        sub eax, r12d
0095C9EA  41 89 44 24 14                  mov dword ptr [r12 + 0x14], eax
0095C9EF  48 89 94 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rdx
0095C9F7  48 83 C2 3C                     add rdx, 0x3c
0095C9FB  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
0095CA00  8B 4C 24 68                     mov ecx, dword ptr [rsp + 0x68]
0095CA04  41 89 4C 24 20                  mov dword ptr [r12 + 0x20], ecx
0095CA09  8B C2                           mov eax, edx
0095CA0B  41 2B C4                        sub eax, r12d
0095CA0E  41 89 44 24 1C                  mov dword ptr [r12 + 0x1c], eax
0095CA13  48 89 94 24 00 01 00 00         mov qword ptr [rsp + 0x100], rdx
0095CA1B  48 8D 3C CA                     lea rdi, [rdx + rcx*8]
0095CA1F  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
0095CA24  48 89 BC 24 38 01 00 00         mov qword ptr [rsp + 0x138], rdi
0095CA2C  4D 8B 86 90 06 00 00            mov r8, qword ptr [r14 + 0x690]
0095CA33  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
0095CA38  49 8D 86 90 06 00 00            lea rax, [r14 + 0x690]
0095CA3F  4C 3B C0                        cmp r8, rax
0095CA42  0F 84 06 02 00 00               je 0x14095cc4e
0095CA48  4C 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r8
0095CA50  44 8B CE                        mov r9d, esi
0095CA53  89 B4 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], esi
0095CA5A  45 3B 48 14                     cmp r9d, dword ptr [r8 + 0x14]
0095CA5E  73 44                           jae 0x14095caa4
0095CA60  41 8B C9                        mov ecx, r9d
0095CA63  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
0095CA67  4C 8D 14 C8                     lea r10, [rax + rcx*8]
0095CA6B  4C 89 94 24 40 01 00 00         mov qword ptr [rsp + 0x140], r10
0095CA73  49 39 32                        cmp qword ptr [r10], rsi
0095CA76  75 0D                           jne 0x14095ca85
0095CA78  45 03 CF                        add r9d, r15d
0095CA7B  44 89 8C 24 A8 00 00 00         mov dword ptr [rsp + 0xa8], r9d
0095CA83  EB D5                           jmp 0x14095ca5a
0095CA85  48 3B D7                        cmp rdx, rdi
0095CA88  73 1A                           jae 0x14095caa4
0095CA8A  41 8B 02                        mov eax, dword ptr [r10]
0095CA8D  89 02                           mov dword ptr [rdx], eax
0095CA8F  41 8B 42 04                     mov eax, dword ptr [r10 + 4]
0095CA93  89 42 04                        mov dword ptr [rdx + 4], eax
0095CA96  48 83 C2 08                     add rdx, 8
0095CA9A  48 89 94 24 00 01 00 00         mov qword ptr [rsp + 0x100], rdx
0095CAA2  EB D4                           jmp 0x14095ca78
0095CAA4  4D 8B 00                        mov r8, qword ptr [r8]
0095CAA7  EB 8A                           jmp 0x14095ca33
0095CAA9  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0095CAB1  48 8B 80 28 05 00 00            mov rax, qword ptr [rax + 0x528]
0095CAB8  48 85 C0                        test rax, rax
0095CABB  0F 84 B8 00 00 00               je 0x14095cb79
0095CAC1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0095CAC6  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0095CACF  48 89 8C 24 10 01 00 00         mov qword ptr [rsp + 0x110], rcx
0095CAD7  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
0095CADE  66 41 2B C7                     sub ax, r15w
0095CAE2  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
0095CAE9  90                              nop
0095CAEA  45 33 C0                        xor r8d, r8d
0095CAED  33 D2                           xor edx, edx
0095CAEF  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0095CAF4  48 8B CF                        mov rcx, rdi
0095CAF7  E8 34 37 8B FF                  call 0x140210230
0095CAFC  4C 8B E0                        mov r12, rax
0095CAFF  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0095CB05  73 10                           jae 0x14095cb17
0095CB07  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0095CB0C  4C 8B C1                        mov r8, rcx
0095CB0F  48 8B D0                        mov rdx, rax
0095CB12  E8 79 31 8B FF                  call 0x14020fc90
0095CB17  4D 85 E4                        test r12, r12
0095CB1A  74 05                           je 0x14095cb21
0095CB1C  45 88 7C 24 0A                  mov byte ptr [r12 + 0xa], r15b
0095CB21  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0095CB2A  48 89 84 24 18 01 00 00         mov qword ptr [rsp + 0x118], rax
0095CB32  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0095CB37  48 89 47 08                     mov qword ptr [rdi + 8], rax
0095CB3B  44 8B 47 14                     mov r8d, dword ptr [rdi + 0x14]
0095CB3F  49 C1 E0 02                     shl r8, 2
0095CB43  48 8D 4F 18                     lea rcx, [rdi + 0x18]
0095CB47  33 D2                           xor edx, edx
0095CB49  E8 F2 A0 D6 FF                  call 0x1406c6c40
0095CB4E  48 89 77 08                     mov qword ptr [rdi + 8], rsi
0095CB52  48 8B C3                        mov rax, rbx
0095CB55  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
0095CB5A  24 06                           and al, 6
0095CB5C  3C 02                           cmp al, 2
0095CB5E  75 0A                           jne 0x14095cb6a
0095CB60  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0095CB65  E8 66 92 90 FF                  call 0x140265dd0
0095CB6A  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0095CB6F  E8 8C 4A 98 FF                  call 0x1402e1600
0095CB74  E8 37 0D 90 FF                  call 0x14025d8b0
0095CB79  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0095CB81  48 8B 80 30 05 00 00            mov rax, qword ptr [rax + 0x530]
0095CB88  48 85 C0                        test rax, rax
0095CB8B  0F 84 4A FD FF FF               je 0x14095c8db
0095CB91  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0095CB96  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0095CB9F  48 89 8C 24 20 01 00 00         mov qword ptr [rsp + 0x120], rcx
0095CBA7  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
0095CBAE  66 41 2B C7                     sub ax, r15w
0095CBB2  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
0095CBB9  90                              nop
0095CBBA  45 33 C0                        xor r8d, r8d
0095CBBD  33 D2                           xor edx, edx
0095CBBF  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0095CBC4  48 8B CF                        mov rcx, rdi
0095CBC7  E8 64 36 8B FF                  call 0x140210230
0095CBCC  4C 8B E0                        mov r12, rax
0095CBCF  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0095CBD5  73 10                           jae 0x14095cbe7
0095CBD7  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0095CBDC  4C 8B C1                        mov r8, rcx
0095CBDF  48 8B D0                        mov rdx, rax
0095CBE2  E8 A9 30 8B FF                  call 0x14020fc90
0095CBE7  4D 85 E4                        test r12, r12
0095CBEA  74 05                           je 0x14095cbf1
0095CBEC  45 88 7C 24 0A                  mov byte ptr [r12 + 0xa], r15b
0095CBF1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0095CBFA  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
0095CC02  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0095CC07  48 89 47 08                     mov qword ptr [rdi + 8], rax
0095CC0B  44 8B 47 14                     mov r8d, dword ptr [rdi + 0x14]
0095CC0F  49 C1 E0 02                     shl r8, 2
0095CC13  48 8D 4F 18                     lea rcx, [rdi + 0x18]
0095CC17  33 D2                           xor edx, edx
0095CC19  E8 22 A0 D6 FF                  call 0x1406c6c40
0095CC1E  48 89 77 08                     mov qword ptr [rdi + 8], rsi
0095CC22  48 8B C3                        mov rax, rbx
0095CC25  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
0095CC2A  24 06                           and al, 6
0095CC2C  3C 02                           cmp al, 2
0095CC2E  75 0A                           jne 0x14095cc3a
0095CC30  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0095CC35  E8 96 91 90 FF                  call 0x140265dd0
0095CC3A  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0095CC3F  E8 BC 49 98 FF                  call 0x1402e1600
0095CC44  E8 67 0C 90 FF                  call 0x14025d8b0
0095CC49  E9 8D FC FF FF                  jmp 0x14095c8db
0095CC4E  EB 2E                           jmp 0x14095cc7e
0095CC50  8B F8                           mov edi, eax
0095CC52  33 F6                           xor esi, esi
0095CC54  48 83 CB FF                     or rbx, 0xffffffffffffffff
0095CC58  44 8D 7E 01                     lea r15d, [rsi + 1]
0095CC5C  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
0095CC64  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0095CC68  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0095CC6C  4C 8B B4 24 E0 00 00 00         mov r14, qword ptr [rsp + 0xe0]
0095CC74  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
0095CC79  E9 5A 04 00 00                  jmp 0x14095d0d8
0095CC7E  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
0095CC82  41 89 4C 24 28                  mov dword ptr [r12 + 0x28], ecx
0095CC87  8B C7                           mov eax, edi
0095CC89  41 2B C4                        sub eax, r12d
0095CC8C  41 89 44 24 24                  mov dword ptr [r12 + 0x24], eax
0095CC91  4C 8B CF                        mov r9, rdi
0095CC94  48 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rdi
0095CC9C  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
0095CCA0  48 C1 E1 04                     shl rcx, 4
0095CCA4  48 03 F9                        add rdi, rcx
0095CCA7  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
0095CCAC  4C 8B C7                        mov r8, rdi
0095CCAF  4D 2B C1                        sub r8, r9
0095CCB2  33 D2                           xor edx, edx
0095CCB4  49 8B C9                        mov rcx, r9
0095CCB7  E8 84 9F D6 FF                  call 0x1406c6c40
0095CCBC  4C 8B CF                        mov r9, rdi
0095CCBF  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
0095CCC4  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0095CCC8  48 03 F8                        add rdi, rax
0095CCCB  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
0095CCD0  48 89 BC 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rdi
0095CCD8  48 8B CF                        mov rcx, rdi
0095CCDB  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
0095CCE3  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
0095CCE7  48 03 F8                        add rdi, rax
0095CCEA  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
0095CCEF  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
0095CCF4  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
0095CCFC  89 B4 24 80 00 00 00            mov dword ptr [rsp + 0x80], esi
0095CD03  48 8B BC 24 90 00 00 00         mov rdi, qword ptr [rsp + 0x90]
0095CD0B  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
0095CD10  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
0095CD18  48 3B F8                        cmp rdi, rax
0095CD1B  0F 84 23 02 00 00               je 0x14095cf44
0095CD21  48 8B 07                        mov rax, qword ptr [rdi]
0095CD24  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0095CD29  41 8B C1                        mov eax, r9d
0095CD2C  41 2B C4                        sub eax, r12d
0095CD2F  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
0095CD37  89 42 08                        mov dword ptr [rdx + 8], eax
0095CD3A  8B 47 A8                        mov eax, dword ptr [rdi - 0x58]
0095CD3D  89 42 0C                        mov dword ptr [rdx + 0xc], eax
0095CD40  41 2B CC                        sub ecx, r12d
0095CD43  89 0A                           mov dword ptr [rdx], ecx
0095CD45  8B 47 E8                        mov eax, dword ptr [rdi - 0x18]
0095CD48  0F B7 C8                        movzx ecx, ax
0095CD4B  89 4A 04                        mov dword ptr [rdx + 4], ecx
0095CD4E  8B 47 94                        mov eax, dword ptr [rdi - 0x6c]
0095CD51  89 42 10                        mov dword ptr [rdx + 0x10], eax
0095CD54  8B 47 90                        mov eax, dword ptr [rdi - 0x70]
0095CD57  89 42 14                        mov dword ptr [rdx + 0x14], eax
0095CD5A  8B 47 98                        mov eax, dword ptr [rdi - 0x68]
0095CD5D  89 42 18                        mov dword ptr [rdx + 0x18], eax
0095CD60  8B 47 EC                        mov eax, dword ptr [rdi - 0x14]
0095CD63  89 42 1C                        mov dword ptr [rdx + 0x1c], eax
0095CD66  8B 47 F0                        mov eax, dword ptr [rdi - 0x10]
0095CD69  89 42 20                        mov dword ptr [rdx + 0x20], eax
0095CD6C  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0095CD6F  89 42 24                        mov dword ptr [rdx + 0x24], eax
0095CD72  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
0095CD75  89 42 28                        mov dword ptr [rdx + 0x28], eax
0095CD78  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
0095CD7B  89 42 2C                        mov dword ptr [rdx + 0x2c], eax
0095CD7E  48 83 C2 30                     add rdx, 0x30
0095CD82  48 89 94 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rdx
0095CD8A  44 8B 47 A8                     mov r8d, dword ptr [rdi - 0x58]
0095CD8E  48 8B 57 A0                     mov rdx, qword ptr [rdi - 0x60]
0095CD92  49 8B C9                        mov rcx, r9
0095CD95  E8 A6 9A D6 FF                  call 0x1406c6840
0095CD9A  8B 47 A8                        mov eax, dword ptr [rdi - 0x58]
0095CD9D  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0095CDA2  48 83 C1 03                     add rcx, 3
0095CDA6  48 03 C8                        add rcx, rax
0095CDA9  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
0095CDAD  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0095CDB2  48 3B 8C 24 F0 00 00 00         cmp rcx, qword ptr [rsp + 0xf0]
0095CDBA  0F 87 84 01 00 00               ja 0x14095cf44
0095CDC0  8B 47 E8                        mov eax, dword ptr [rdi - 0x18]
0095CDC3  44 0F B7 C8                     movzx r9d, ax
0095CDC7  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
0095CDCF  48 2B 94 24 A0 00 00 00         sub rdx, qword ptr [rsp + 0xa0]
0095CDD7  48 D1 FA                        sar rdx, 1
0095CDDA  4C 8B 47 E0                     mov r8, qword ptr [rdi - 0x20]
0095CDDE  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0095CDE6  E8 B1 48 B1 FF                  call 0x14047169c
0095CDEB  44 8B 5F E8                     mov r11d, dword ptr [rdi - 0x18]
0095CDEF  41 0F B7 C3                     movzx eax, r11w
0095CDF3  41 03 C7                        add eax, r15d
0095CDF6  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0095CDFE  48 8D 0C 41                     lea rcx, [rcx + rax*2]
0095CE02  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
0095CE0A  48 3B 8C 24 B8 00 00 00         cmp rcx, qword ptr [rsp + 0xb8]
0095CE12  0F 87 2C 01 00 00               ja 0x14095cf44
0095CE18  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0095CE21  48 89 8C 24 48 01 00 00         mov qword ptr [rsp + 0x148], rcx
0095CE29  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
0095CE30  66 41 2B C7                     sub ax, r15w
0095CE34  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
0095CE3B  90                              nop
0095CE3C  4D 8D A5 98 04 00 00            lea r12, [r13 + 0x498]
0095CE43  45 33 C0                        xor r8d, r8d
0095CE46  33 D2                           xor edx, edx
0095CE48  49 8B CC                        mov rcx, r12
0095CE4B  E8 E0 33 8B FF                  call 0x140210230
0095CE50  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0095CE55  F0 49 0F BA 2C 24 00            lock bts qword ptr [r12], 0
0095CE5C  73 13                           jae 0x14095ce71
0095CE5E  4D 8B C4                        mov r8, r12
0095CE61  48 8B D0                        mov rdx, rax
0095CE64  49 8B CC                        mov rcx, r12
0095CE67  E8 24 2E 8B FF                  call 0x14020fc90
0095CE6C  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0095CE71  48 85 C0                        test rax, rax
0095CE74  74 04                           je 0x14095ce7a
0095CE76  44 88 78 0A                     mov byte ptr [rax + 0xa], r15b
0095CE7A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0095CE83  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
0095CE8B  49 89 85 A0 04 00 00            mov qword ptr [r13 + 0x4a0], rax
0095CE92  48 8B 4F D8                     mov rcx, qword ptr [rdi - 0x28]
0095CE96  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
0095CE9D  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0095CEA2  49 89 0C D0                     mov qword ptr [r8 + rdx*8], rcx
0095CEA6  41 03 D7                        add edx, r15d
0095CEA9  89 94 24 80 00 00 00            mov dword ptr [rsp + 0x80], edx
0095CEB0  48 89 77 D8                     mov qword ptr [rdi - 0x28], rsi
0095CEB4  48 89 77 E0                     mov qword ptr [rdi - 0x20], rsi
0095CEB8  81 67 E8 00 00 FF FF            and dword ptr [rdi - 0x18], 0xffff0000
0095CEBF  8B 47 E8                        mov eax, dword ptr [rdi - 0x18]
0095CEC2  0F BA E8 13                     bts eax, 0x13
0095CEC6  89 47 E8                        mov dword ptr [rdi - 0x18], eax
0095CEC9  49 89 B5 A0 04 00 00            mov qword ptr [r13 + 0x4a0], rsi
0095CED0  4D 8D A5 98 04 00 00            lea r12, [r13 + 0x498]
0095CED7  48 8B C3                        mov rax, rbx
0095CEDA  F0 49 0F C1 04 24               lock xadd qword ptr [r12], rax
0095CEE0  24 06                           and al, 6
0095CEE2  3C 02                           cmp al, 2
0095CEE4  74 4A                           je 0x14095cf30
0095CEE6  49 8B CC                        mov rcx, r12
0095CEE9  E8 12 47 98 FF                  call 0x1402e1600
0095CEEE  E8 BD 09 90 FF                  call 0x14025d8b0
0095CEF3  B8 FF FF FF FF                  mov eax, 0xffffffff
0095CEF8  01 44 24 30                     add dword ptr [rsp + 0x30], eax
0095CEFC  4C 39 7F B0                     cmp qword ptr [rdi - 0x50], r15
0095CF00  74 38                           je 0x14095cf3a
0095CF02  8B C6                           mov eax, esi
0095CF04  87 47 F4                        xchg dword ptr [rdi - 0xc], eax
0095CF07  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0095CF0C  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0095CF11  4C 8B A4 24 C0 00 00 00         mov r12, qword ptr [rsp + 0xc0]
0095CF19  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0095CF1E  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0095CF26  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
0095CF2B  E9 E0 FD FF FF                  jmp 0x14095cd10
0095CF30  49 8B CC                        mov rcx, r12
0095CF33  E8 98 8E 90 FF                  call 0x140265dd0
0095CF38  EB AC                           jmp 0x14095cee6
0095CF3A  F0 45 01 BD 64 06 00 00         lock add dword ptr [r13 + 0x664], r15d
0095CF42  EB BE                           jmp 0x14095cf02
0095CF44  41 0F 10 85 5C 04 00 00         movups xmm0, xmmword ptr [r13 + 0x45c]
0095CF4C  48 8B BC 24 C8 00 00 00         mov rdi, qword ptr [rsp + 0xc8]
0095CF54  0F 11 07                        movups xmmword ptr [rdi], xmm0
0095CF57  41 0F 10 8D 6C 04 00 00         movups xmm1, xmmword ptr [r13 + 0x46c]
0095CF5F  0F 11 4F 10                     movups xmmword ptr [rdi + 0x10], xmm1
0095CF63  41 0F 10 85 7C 04 00 00         movups xmm0, xmmword ptr [r13 + 0x47c]
0095CF6B  0F 11 47 20                     movups xmmword ptr [rdi + 0x20], xmm0
0095CF6F  F2 41 0F 10 8D 8C 04 00 00      movsd xmm1, qword ptr [r13 + 0x48c]
0095CF78  F2 0F 11 4F 30                  movsd qword ptr [rdi + 0x30], xmm1
0095CF7D  41 8B 85 94 04 00 00            mov eax, dword ptr [r13 + 0x494]
0095CF84  89 47 38                        mov dword ptr [rdi + 0x38], eax
0095CF87  0F 57 C0                        xorps xmm0, xmm0
0095CF8A  33 C0                           xor eax, eax
0095CF8C  41 0F 11 85 5C 04 00 00         movups xmmword ptr [r13 + 0x45c], xmm0
0095CF94  41 0F 11 85 6C 04 00 00         movups xmmword ptr [r13 + 0x46c], xmm0
0095CF9C  41 0F 11 85 7C 04 00 00         movups xmmword ptr [r13 + 0x47c], xmm0
0095CFA4  49 89 85 8C 04 00 00            mov qword ptr [r13 + 0x48c], rax
0095CFAB  41 89 85 94 04 00 00            mov dword ptr [r13 + 0x494], eax
0095CFB2  0F 11 84 24 B0 01 00 00         movups xmmword ptr [rsp + 0x1b0], xmm0
0095CFBA  0F 11 84 24 C0 01 00 00         movups xmmword ptr [rsp + 0x1c0], xmm0
0095CFC2  48 8D 94 24 B0 01 00 00         lea rdx, [rsp + 0x1b0]
0095CFCA  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0095CFD2  E8 E9 26 15 00                  call 0x140aaf6c0
0095CFD7  8B 84 24 B0 01 00 00            mov eax, dword ptr [rsp + 0x1b0]
0095CFDE  89 47 1C                        mov dword ptr [rdi + 0x1c], eax
0095CFE1  8B 84 24 B4 01 00 00            mov eax, dword ptr [rsp + 0x1b4]
0095CFE8  89 47 20                        mov dword ptr [rdi + 0x20], eax
0095CFEB  8B 84 24 B8 01 00 00            mov eax, dword ptr [rsp + 0x1b8]
0095CFF2  89 47 24                        mov dword ptr [rdi + 0x24], eax
0095CFF5  8B 84 24 BC 01 00 00            mov eax, dword ptr [rsp + 0x1bc]
0095CFFC  89 47 28                        mov dword ptr [rdi + 0x28], eax
0095CFFF  8B 84 24 C0 01 00 00            mov eax, dword ptr [rsp + 0x1c0]
0095D006  89 47 2C                        mov dword ptr [rdi + 0x2c], eax
0095D009  8B 84 24 C4 01 00 00            mov eax, dword ptr [rsp + 0x1c4]
0095D010  89 47 30                        mov dword ptr [rdi + 0x30], eax
0095D013  8B 84 24 C8 01 00 00            mov eax, dword ptr [rsp + 0x1c8]
0095D01A  89 47 34                        mov dword ptr [rdi + 0x34], eax
0095D01D  8B 84 24 CC 01 00 00            mov eax, dword ptr [rsp + 0x1cc]
0095D024  89 47 38                        mov dword ptr [rdi + 0x38], eax
0095D027  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0095D02C  41 2B C4                        sub eax, r12d
0095D02F  41 89 44 24 04                  mov dword ptr [r12 + 4], eax
0095D034  EB 2B                           jmp 0x14095d061
0095D036  8B F8                           mov edi, eax
0095D038  33 F6                           xor esi, esi
0095D03A  48 83 CB FF                     or rbx, 0xffffffffffffffff
0095D03E  44 8D 7E 01                     lea r15d, [rsi + 1]
0095D042  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
0095D04A  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
0095D04E  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
0095D052  4C 8B B4 24 E0 00 00 00         mov r14, qword ptr [rsp + 0xe0]
0095D05A  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
0095D05F  EB 77                           jmp 0x14095d0d8
0095D061  49 8B BE 90 06 00 00            mov rdi, qword ptr [r14 + 0x690]
0095D068  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
0095D06D  49 8D 86 90 06 00 00            lea rax, [r14 + 0x690]
0095D074  48 3B F8                        cmp rdi, rax
0095D077  0F 85 AC 01 00 00               jne 0x14095d229
0095D07D  45 01 BE BC 06 00 00            add dword ptr [r14 + 0x6bc], r15d
0095D084  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0095D08C  39 B0 04 05 00 00               cmp dword ptr [rax + 0x504], esi
0095D092  0F 85 AB 00 00 00               jne 0x14095d143
0095D098  49 89 76 08                     mov qword ptr [r14 + 8], rsi
0095D09C  48 8B C3                        mov rax, rbx
0095D09F  F0 49 0F C1 06                  lock xadd qword ptr [r14], rax
0095D0A4  24 06                           and al, 6
0095D0A6  3C 02                           cmp al, 2
0095D0A8  0F 84 C5 00 00 00               je 0x14095d173
0095D0AE  49 8B CE                        mov rcx, r14
0095D0B1  E8 4A 45 98 FF                  call 0x1402e1600
0095D0B6  E8 F5 07 90 FF                  call 0x14025d8b0
0095D0BB  49 8B CD                        mov rcx, r13
0095D0BE  E8 79 CF F7 FF                  call 0x1408da03c
0095D0C3  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
0095D0C7  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
0095D0CF  89 01                           mov dword ptr [rcx], eax
0095D0D1  8B FE                           mov edi, esi
0095D0D3  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
0095D0D8  49 8B 8D A0 04 00 00            mov rcx, qword ptr [r13 + 0x4a0]
0095D0DF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0095D0E8  48 3B C8                        cmp rcx, rax
0095D0EB  0F 84 77 01 00 00               je 0x14095d268
0095D0F1  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
0095D0F5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0095D0FE  48 3B C8                        cmp rcx, rax
0095D101  0F 84 90 01 00 00               je 0x14095d297
0095D107  4D 85 E4                        test r12, r12
0095D10A  0F 85 AA 01 00 00               jne 0x14095d2ba
0095D110  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0095D118  E8 33 A7 F7 FF                  call 0x1408d7850
0095D11D  8B C7                           mov eax, edi
0095D11F  48 8B 8C 24 D0 01 00 00         mov rcx, qword ptr [rsp + 0x1d0]
0095D127  48 33 CC                        xor rcx, rsp
0095D12A  E8 11 F5 D4 FF                  call 0x1406ac640
0095D12F  48 81 C4 E0 01 00 00            add rsp, 0x1e0
0095D136  41 5F                           pop r15
0095D138  41 5E                           pop r14
0095D13A  41 5D                           pop r13
0095D13C  41 5C                           pop r12
0095D13E  5F                              pop rdi
0095D13F  5E                              pop rsi
0095D140  5B                              pop rbx
0095D141  C3                              ret
0095D142  CC                              int3
0095D143  89 B0 04 05 00 00               mov dword ptr [rax + 0x504], esi
0095D149  48 8D 90 B0 03 00 00            lea rdx, [rax + 0x3b0]
0095D150  48 8B 0A                        mov rcx, qword ptr [rdx]
0095D153  EB 14                           jmp 0x14095d169
0095D155  8B 80 04 05 00 00               mov eax, dword ptr [rax + 0x504]
0095D15B  89 41 1C                        mov dword ptr [rcx + 0x1c], eax
0095D15E  48 8B 09                        mov rcx, qword ptr [rcx]
0095D161  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0095D169  48 3B CA                        cmp rcx, rdx
0095D16C  75 E7                           jne 0x14095d155
0095D16E  E9 25 FF FF FF                  jmp 0x14095d098
0095D173  49 8B CE                        mov rcx, r14
0095D176  E8 55 8C 90 FF                  call 0x140265dd0
0095D17B  E9 2E FF FF FF                  jmp 0x14095d0ae
0095D180  BF 89 01 00 C0                  mov edi, 0xc0000189
0095D185  41 BF 01 00 00 00               mov r15d, 1
0095D18B  48 83 CB FF                     or rbx, 0xffffffffffffffff
0095D18F  4C 8B E6                        mov r12, rsi
0095D192  E9 41 FF FF FF                  jmp 0x14095d0d8
0095D197  03 50 10                        add edx, dword ptr [rax + 0x10]
0095D19A  48 8B 00                        mov rax, qword ptr [rax]
0095D19D  48 3B C1                        cmp rax, rcx
0095D1A0  75 F5                           jne 0x14095d197
0095D1A2  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0095D1A7  89 54 24 68                     mov dword ptr [rsp + 0x68], edx
0095D1AB  E9 9C F4 FF FF                  jmp 0x14095c64c
0095D1B0  F0 45 01 BD 64 06 00 00         lock add dword ptr [r13 + 0x664], r15d
0095D1B8  E9 AA F5 FF FF                  jmp 0x14095c767
0095D1BD  49 8D BD 98 04 00 00            lea rdi, [r13 + 0x498]
0095D1C4  B8 11 00 00 00                  mov eax, 0x11
0095D1C9  F0 48 0F B1 37                  lock cmpxchg qword ptr [rdi], rsi
0095D1CE  0F 84 4F F6 FF FF               je 0x14095c823
0095D1D4  48 8B CF                        mov rcx, rdi
0095D1D7  E8 64 62 90 FF                  call 0x140263440
0095D1DC  E9 42 F6 FF FF                  jmp 0x14095c823
0095D1E1  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
0095D1E9  89 11                           mov dword ptr [rcx], edx
0095D1EB  BF 23 00 00 C0                  mov edi, 0xc0000023
0095D1F0  EB 9D                           jmp 0x14095d18f
0095D1F2  42 8D 04 E5 00 00 00 00         lea eax, [r12*8]
0095D1FA  8B F8                           mov edi, eax
0095D1FC  41 B8 45 74 77 56               mov r8d, 0x56777445
0095D202  8B D0                           mov edx, eax
0095D204  B9 00 01 00 00                  mov ecx, 0x100
0095D209  E8 E2 4E 22 00                  call 0x140b820f0
0095D20E  4C 8B E0                        mov r12, rax
0095D211  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0095D216  48 85 C0                        test rax, rax
0095D219  0F 85 75 A8 1C 00               jne 0x140b27a94
0095D21F  BF 9A 00 00 C0                  mov edi, 0xc000009a
0095D224  E9 AF FE FF FF                  jmp 0x14095d0d8
0095D229  4C 8B E7                        mov r12, rdi
0095D22C  48 89 BC 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdi
0095D234  48 8B 3F                        mov rdi, qword ptr [rdi]
0095D237  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
0095D23C  4D 3B A6 80 06 00 00            cmp r12, qword ptr [r14 + 0x680]
0095D243  0F 85 5E A8 1C 00               jne 0x140b27aa7
0095D249  45 8B 44 24 14                  mov r8d, dword ptr [r12 + 0x14]
0095D24E  49 C1 E0 03                     shl r8, 3
0095D252  33 D2                           xor edx, edx
0095D254  49 8B 4C 24 18                  mov rcx, qword ptr [r12 + 0x18]
0095D259  E8 E2 99 D6 FF                  call 0x1406c6c40
0095D25E  41 89 74 24 10                  mov dword ptr [r12 + 0x10], esi
0095D263  E9 05 FE FF FF                  jmp 0x14095d06d
0095D268  49 89 B5 A0 04 00 00            mov qword ptr [r13 + 0x4a0], rsi
0095D26F  48 8B C3                        mov rax, rbx
0095D272  F0 49 0F C1 85 98 04 00 00      lock xadd qword ptr [r13 + 0x498], rax
0095D27B  24 06                           and al, 6
0095D27D  3C 02                           cmp al, 2
0095D27F  0F 85 5B A8 1C 00               jne 0x140b27ae0
0095D285  49 8D 8D 98 04 00 00            lea rcx, [r13 + 0x498]
0095D28C  E8 3F 8B 90 FF                  call 0x140265dd0
0095D291  90                              nop
0095D292  E9 49 A8 1C 00                  jmp 0x140b27ae0
0095D297  49 89 76 08                     mov qword ptr [r14 + 8], rsi
0095D29B  F0 49 0F C1 1E                  lock xadd qword ptr [r14], rbx
0095D2A0  80 E3 06                        and bl, 6
0095D2A3  80 FB 02                        cmp bl, 2
0095D2A6  0F 85 4B A8 1C 00               jne 0x140b27af7
0095D2AC  49 8B CE                        mov rcx, r14
0095D2AF  E8 1C 8B 90 FF                  call 0x140265dd0
0095D2B4  90                              nop
0095D2B5  E9 3D A8 1C 00                  jmp 0x140b27af7
0095D2BA  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
0095D2BE  85 C0                           test eax, eax
0095D2C0  0F 84 55 A8 1C 00               je 0x140b27b1b
0095D2C6  49 8B DC                        mov rbx, r12
0095D2C9  8B F0                           mov esi, eax
0095D2CB  E9 3A A8 1C 00                  jmp 0x140b27b0a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCoverageSamplerQuery(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned int v_stack_m1A8;
    unsigned int v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C4;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1E0;
    unsigned int v_stack_m1E4;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pF8;

    v_rsp = (v_rsp) - (480);
    result = (*(unsigned __int64 *)(v_rip + 4907652)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m148 = a4;
    v_stack_m1E0 = a3;
    v_stack_m1A0 = a2;
    v_stack_m138 = a1;
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp - 360) = 0;
    v_stack_m190 = *(unsigned __int64 *)(v_rip + 5909748);
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm0;
    v_stack_m140 = a1 + 16;
    v_stack_m1D0 = 0;
    *(unsigned __int64 *)(v_rsp - 344) = 0;
    v_stack_m188 = v_xmm0;
    v_stack_m1E4 = 0;
    v_stack_m1C0 = 0;
    *(unsigned __int64 *)(v_rsp - 336) = 0;
    result = EtwpCovSampAcquireSamplerRundown(v_rsp - 360, a2, a3, a4);
    if (sign_flag) goto loc_0095D185;
    if (v_stack_m168 != a1) goto loc_0095D180;
    result = 0;
    v_stack_mB0 = 0;
    result = EtwpCovSampCaptureFlushSampleBuffers(*(unsigned __int64 *)(v_rip + 5909748), a2, a3, a4);
    a2 = 0;
    result = memset(v_stack_mB8, a2, v_rsi + 80, a4);
    v_stack_mA8 = (unsigned int)(0xF1A5BFFAULL);
    v_stack_mB8 = 0x1B1DULL;
    a3 = 0;
    a2 = 0;
    result = KeInitializeEvent(v_stack_m88, a2, a3, a4);
    result = EtwpCovSampCaptureQueueBuffer(*(unsigned __int64 *)(v_rip + 5909748), v_stack_mB8, a3, a4);
    v_stack_m1F8 = 0;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_stack_m88, a2, a3, a4);
    v_rbx = (*(unsigned __int64 *)(v_rip + 5909748)) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1;
        a2 = result;
        a1 = a1;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m1B0 = 0;
    v_stack_m1D8 = *(unsigned __int64 *)(a1 + 1680);
    if ((*(unsigned __int64 *)(a1 + 1680)) != (a1 + 1680)) goto loc_0095D197;
loc_0095C64C:
    result = (0) << (3);
    a1 = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    if (result <= ((unsigned int)(0xFFFFFFFFULL))) { a1 = (unsigned int)(result); }
    v_rdi = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_0095D18F;
    a2 = (unsigned int)(0xFFFFFFFFULL);
    if (((unsigned int)(a1 + 1232)) >= ((unsigned int)(a1))) { a2 = (unsigned int)(a1 + 1232); }
    v_stack_m1A8 = (unsigned int)(a2);
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (((unsigned int)(a1 + 1232)) < ((unsigned int)(a1))) goto loc_0095D18F;
    v_stack_m1E4 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1E8 = 0;
    v_stack_m1C4 = 0;
    v_stack_m1C8 = 0;
    v_stack_m180 = v_stack_m188;
    v_stack_m188 = v_stack_m188;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 16 + 1176, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1 + 16 + 1176;
        a3 = 0;
        a2 = 0;
        a1 = a1 + 16 + 1176;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_m1D8 = *(unsigned __int64 *)(a1 + 16 + 1224);
loc_0095C72D:
loc_0095C735:
    if ((*(unsigned __int64 *)(a1 + 16 + 1224)) == (a1 + 16 + 1224)) goto loc_0095D1BD;
    v_stack_m1D8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16 + 1224));
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 16 + 1224) + 60)) != 0) goto loc_0095C757;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 16 + 1224) + 48)) & (0x100000ULL)) == 0) goto loc_0095C735;
loc_0095C757:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16 + 1224) + 32)) != 0) goto loc_0095C773;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16 + 1224) - 8)) == 1) goto loc_0095D1B0;
loc_0095C767:
    goto loc_0095C72D;
loc_0095C773:
    v_r12 = (unsigned int)((0) + (1));
    v_stack_m1E4 = (unsigned int)(v_r12);
    v_stack_m1B8 = (unsigned int)(v_r12);
    result = (unsigned int)(((unsigned int)(v_stack_m1C4)) + ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16 + 1224) + 48))) * 2 + 2)));
    v_rdi = (unsigned int)(0xFFFFFFFFULL);
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16 + 1224) + 48))) * 2 + 2))) { v_rdi = (unsigned int)(result); }
    v_stack_m1C4 = (unsigned int)(v_rdi);
    v_rdi = (unsigned int)((v_rdi) & (0xC0000095ULL));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16 + 1224) + 48))) * 2 + 2))) goto loc_0095D18F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16 + 1224) - 16)) - 1) & (3));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16 + 1224) - 16))) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) + (3));
    v_r11 = (unsigned int)(0xFFFFFFFFULL);
    if (((unsigned int)(a1 + 0 * 1)) >= ((unsigned int)(a1))) { v_r11 = (unsigned int)(a1 + 0 * 1); }
    v_stack_m1C8 = (unsigned int)(v_r11);
    v_rdi = (unsigned int)((v_rdi) & (0xC0000095ULL));
    if (((unsigned int)(a1 + 0 * 1)) < ((unsigned int)(a1))) goto loc_0095D18F;
    a2 = (*(unsigned __int64 *)(a1 + 16 + 1224)) + (72);
    if ((*(unsigned __int64 *)(v_stack_m180)) != v_stack_m188) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a2) = v_stack_m188;
    *(unsigned __int64 *)(a2 + 8) = v_stack_m180;
    *(unsigned __int64 *)(v_stack_m180) = a2;
    v_stack_m180 = a2;
    goto loc_0095C735;
loc_0095C823:
    result = KeAbPostRelease(v_rdi, a2, v_stack_m1D8, a2);
    result = KeLeaveCriticalRegion(v_rdi, a2, v_stack_m1D8, a2);
    a1 = ((unsigned int)(v_stack_m1E8) + (unsigned int)(v_stack_m1E8) * 2) << (4);
    result = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    if (a1 <= ((unsigned int)(0xFFFFFFFFULL))) { result = (unsigned int)(a1); }
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (a1 > ((unsigned int)(0xFFFFFFFFULL))) goto loc_0095D18F;
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(v_stack_m1A8))));
    a2 = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(v_stack_m1A8)))) { a2 = (unsigned int)(result); }
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(v_stack_m1A8)))) goto loc_0095D18F;
    result = (unsigned int)(((unsigned int)(v_stack_m1C4)) + ((unsigned int)(a2)));
    a1 = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    if (((unsigned int)(result)) >= ((unsigned int)(a2))) { a1 = (unsigned int)(result); }
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (((unsigned int)(result)) < ((unsigned int)(a2))) goto loc_0095D18F;
    result = (unsigned int)(((unsigned int)(v_stack_m1C8)) + ((unsigned int)(a1)));
    a2 = (unsigned int)((unsigned int)((unsigned int)(0xFFFFFFFFULL)));
    if (((unsigned int)(result)) >= ((unsigned int)(a1))) { a2 = (unsigned int)(result); }
    v_stack_m1A8 = (unsigned int)(a2);
    v_rdi = (unsigned int)((v_rdi) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (((unsigned int)(result)) < ((unsigned int)(a1))) goto loc_0095D18F;
    if (v_stack_m1E0 < ((unsigned int)(a2))) goto loc_0095D1E1;
    if ((unsigned int)(v_r12) != 0) goto loc_0095D1F2;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1A0 + 16))))) != 0) goto loc_0095CAA9;
loc_0095C8DB:
    v_stack_m1D0 = v_stack_m1A0;
    v_stack_m1D0 = v_stack_m1A0 + 20;
    v_stack_m158 = v_stack_m1A0 + 20;
    a2 = (v_stack_m1A0 + 20) + (44);
    v_stack_m1D0 = a2;
    result = 0;
    *(unsigned __int64 *)(v_stack_m1A0 + 20) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m1A0 + 20 + 16) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m1A0 + 20 + 32) = 0;
    *(unsigned int *)(v_stack_m1A0 + 20 + 40) = 0;
    *(unsigned int *)(v_stack_m1A0 + 20) = 44;
    *(unsigned int *)(v_stack_m1A0 + 20 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1724)));
    *(unsigned int *)(v_stack_m1A0 + 20 + 16) = (unsigned int)((unsigned int)(0x454ULL));
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(v_stack_m1A0 + 20)));
    *(unsigned int *)(v_stack_m1A0 + 20 + 12) = (unsigned int)(result);
    v_stack_mE8 = a2;
    a2 = (a2) + ((unsigned int)(0x454ULL));
    v_stack_m1D0 = a2;
loc_0095C966:
    *(unsigned __int64 *)(a2) = v_xmm0;
    *(unsigned __int64 *)(a2 + 16) = v_xmm1;
    *(unsigned __int64 *)(a2 + 32) = v_xmm0;
    *(unsigned __int64 *)(a2 + 48) = v_xmm1;
    *(unsigned __int64 *)(a2 + 64) = v_xmm0;
    *(unsigned __int64 *)(a2 + 80) = v_xmm1;
    *(unsigned __int64 *)(a2 + 96) = v_xmm0;
    a1 = (a2) + (8 + 120);
    *(unsigned __int64 *)(a1 - 16) = v_xmm1;
    result = (a1 + 16 + 8) + (8 + 120);
    a3 = (8) - (1);
    if (condition_is_not_equal) goto loc_0095C966;
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    *(unsigned __int64 *)(a1 + 32) = v_xmm0;
    *(unsigned __int64 *)(a1 + 48) = v_xmm1;
    *(unsigned __int64 *)(a1 + 64) = v_xmm0;
    *(unsigned int *)(a1 + 80) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 80)));
    *(unsigned int *)(v_stack_m1A0 + 20 + 24) = 60;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(v_stack_m1A0 + 20)));
    *(unsigned int *)(v_stack_m1A0 + 20 + 20) = (unsigned int)(result);
    v_stack_m150 = a2;
    a2 = (a2) + (60);
    v_stack_m1D0 = a2;
    *(unsigned int *)(v_stack_m1A0 + 20 + 32) = (unsigned int)((unsigned int)(v_stack_m1B0));
    result = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(v_stack_m1A0 + 20)));
    *(unsigned int *)(v_stack_m1A0 + 20 + 28) = (unsigned int)(result);
    v_stack_m118 = a2;
    v_stack_m1D0 = a2 + (unsigned int)(v_stack_m1B0) * 8;
    v_stack_mE0 = a2 + (unsigned int)(v_stack_m1B0) * 8;
loc_0095CA33:
    v_stack_m1D8 = *(unsigned __int64 *)(a1 + 1680);
    if ((*(unsigned __int64 *)(a1 + 1680)) == (a1 + 1680)) goto loc_0095CC4E;
    v_stack_m120 = *(unsigned __int64 *)(a1 + 1680);
    v_stack_m170 = 0;
loc_0095CA5A:
    if (0 >= (*(unsigned int *)(*(unsigned __int64 *)(a1 + 1680) + 20))) goto loc_0095CAA4;
    v_stack_mD8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1680) + 24) + 0 * 8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1680) + 24) + 0 * 8)) != 0) goto loc_0095CA85;
loc_0095CA78:
    a4 = (unsigned int)((0) + (1));
    v_stack_m170 = (unsigned int)(a4);
    goto loc_0095CA5A;
loc_0095CA85:
    if (a2 >= (a2 + (unsigned int)(v_stack_m1B0) * 8)) goto loc_0095CAA4;
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1680) + 24) + 0 * 8)));
    *(unsigned int *)(a2 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1680) + 24) + 0 * 8 + 4)));
    a2 = (a2) + (8);
    v_stack_m118 = a2;
    goto loc_0095CA78;
loc_0095CAA4:
    goto loc_0095CA33;
loc_0095CAA9:
    if (*(unsigned __int64 *)(v_stack_m190 + 1320) == 0) goto loc_0095CB79;
    v_stack_m1E0 = *(unsigned __int64 *)(v_stack_m190 + 1320);
    v_stack_m108 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m1E0, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a1 = v_stack_m1E0;
        a3 = a1;
        a2 = result;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_m100 = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(v_stack_m1E0 + 8) = *(unsigned __int64 *)(gs_base + (0 + 392));
    a3 = ((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 20))) << (2);
    a2 = 0;
    result = memset(v_stack_m1E0 + 24, a2, a3, a4);
    *(unsigned __int64 *)(v_stack_m1E0 + 8) = 0;
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_stack_m1E0;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_stack_m1E0, a2, a3, a4);
    result = KeLeaveCriticalRegion(v_stack_m1E0, a2, a3, a4);
loc_0095CB79:
    if (*(unsigned __int64 *)(v_stack_m190 + 1328) == 0) goto loc_0095C8DB;
    v_stack_m1E0 = *(unsigned __int64 *)(v_stack_m190 + 1328);
    v_stack_mF8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m1E0, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a1 = v_stack_m1E0;
        a3 = a1;
        a2 = result;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_mF0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(v_stack_m1E0 + 8) = *(unsigned __int64 *)(gs_base + (0 + 392));
    a3 = ((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 20))) << (2);
    a2 = 0;
    result = memset(v_stack_m1E0 + 24, a2, a3, a4);
    *(unsigned __int64 *)(v_stack_m1E0 + 8) = 0;
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_stack_m1E0;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_stack_m1E0, a2, a3, a4);
    result = KeLeaveCriticalRegion(v_stack_m1E0, a2, a3, a4);
    goto loc_0095C8DB;
loc_0095CC4E:
    goto loc_0095CC7E;
loc_0095CC7E:
    *(unsigned int *)(result + 40) = (unsigned int)((unsigned int)(v_stack_m1E8));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m1E0))) - ((unsigned int)(result)));
    *(unsigned int *)(result + 36) = (unsigned int)(result);
    v_stack_m130 = v_stack_m1E0;
    a1 = ((unsigned int)(v_stack_m1E8) + (unsigned int)(v_stack_m1E8) * 2) << (4);
    v_rdi = (v_stack_m1E0) + (a1);
    v_stack_m1D0 = v_rdi;
    a3 = (v_rdi) - (v_stack_m1E0);
    a2 = 0;
    result = memset(v_stack_m1E0, a2, a3, v_stack_m1E0);
    v_stack_m1A0 = v_rdi;
    v_rdi = (v_rdi) + ((unsigned int)(v_stack_m1C8));
    v_stack_m1D0 = v_rdi;
    v_stack_m128 = v_rdi;
    v_stack_m178 = v_rdi;
    v_rdi = (v_rdi) + ((unsigned int)(v_stack_m1C4));
    v_stack_m1B0 = v_rdi;
    v_stack_m1D0 = v_rdi;
    v_stack_m160 = v_rdi;
    v_stack_m198 = 0;
    v_stack_m1D8 = v_stack_m188;
loc_0095CD10:
    if (v_stack_m188 == v_stack_m188) goto loc_0095CF44;
    v_stack_m1D8 = *(unsigned __int64 *)(v_stack_m188);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - ((unsigned int)(result)));
    *(unsigned int *)(v_stack_m130 + 8) = (unsigned int)(result);
    *(unsigned int *)(v_stack_m130 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 - 88)));
    a1 = (unsigned int)((v_rdi) - ((unsigned int)(result)));
    *(unsigned int *)(v_stack_m130) = (unsigned int)(a1);
    *(unsigned int *)(v_stack_m130 + 4) = (unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m188 - 24))));
    *(unsigned int *)(v_stack_m130 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 - 108)));
    *(unsigned int *)(v_stack_m130 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 - 112)));
    *(unsigned int *)(v_stack_m130 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 - 104)));
    *(unsigned int *)(v_stack_m130 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 - 20)));
    *(unsigned int *)(v_stack_m130 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 - 16)));
    *(unsigned int *)(v_stack_m130 + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 + 16)));
    *(unsigned int *)(v_stack_m130 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 + 20)));
    *(unsigned int *)(v_stack_m130 + 44) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 + 24)));
    a2 = (v_stack_m130) + (48);
    v_stack_m130 = a2;
    result = memcpy(v_rdi, *(unsigned __int64 *)(v_stack_m188 - 96), (unsigned int)(*(unsigned int *)(v_stack_m188 - 88)), v_rdi);
    a1 = (v_stack_m1A0) + (3);
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(v_stack_m188 - 88)));
    a1 = (a1) & (-4);
    v_stack_m1A0 = a1;
    if (a1 > v_stack_m128) goto loc_0095CF44;
    a2 = (v_stack_m160) - (v_stack_m178);
    a2 = (a2) >> (1);
    result = RtlStringCchCopyNW(v_stack_m178, a2, *(unsigned __int64 *)(v_stack_m188 - 32), (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m188 - 24))));
    result = (unsigned int)(((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m188 - 24)))) + (1));
    v_stack_m178 = v_stack_m178 + result * 2;
    if ((v_stack_m178 + result * 2) > v_stack_m160) goto loc_0095CF44;
    v_stack_mD0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 16 + 1176, a2, a3, (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m188 - 24))));
    v_stack_m1B0 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 16 + 1176;
        a2 = result;
        a1 = a1 + 16 + 1176;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m188 - 24))));
        result = v_stack_m1B0;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_mC8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(a1 + 16 + 1184) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(v_stack_m1C0 + (unsigned int)(v_stack_m198) * 8) = *(unsigned __int64 *)(v_stack_m188 - 40);
    a2 = (unsigned int)(((unsigned int)(v_stack_m198)) + (1));
    v_stack_m198 = (unsigned int)(a2);
    *(unsigned __int64 *)(v_stack_m188 - 40) = 0;
    *(unsigned __int64 *)(v_stack_m188 - 32) = 0;
    *(unsigned int *)(v_stack_m188 - 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m188 - 24)));
    *(unsigned __int64 *)(a1 + 16 + 1184) = 0;
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0095CF30;
loc_0095CEE6:
    result = KeAbPostRelease(a1 + 16 + 1176, a2, v_stack_m1C0, (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m188 - 24))));
    result = KeLeaveCriticalRegion(a1 + 16 + 1176, a2, v_stack_m1C0, (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m188 - 24))));
    if ((*(unsigned __int64 *)(v_stack_m188 - 80)) == 1) goto loc_0095CF3A;
loc_0095CF02:
    v_stack_m1B0 = v_stack_m1D0;
    goto loc_0095CD10;
loc_0095CF30:
    result = ExfTryToWakePushLock(v_stack_m158, a2, v_stack_m1C0, v_stack_m1A0);
    goto loc_0095CEE6;
loc_0095CF3A:
    goto loc_0095CF02;
loc_0095CF44:
    *(unsigned __int64 *)(v_stack_m150) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m150 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m150 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m150 + 48) = v_xmm1;
    *(unsigned int *)(v_stack_m150 + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16 + 1172)));
    result = 0;
    *(unsigned __int64 *)(a1 + 16 + 1116) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16 + 1132) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16 + 1148) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16 + 1164) = 0;
    *(unsigned int *)(a1 + 16 + 1172) = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    result = EtwpCovSampCaptureFlushStats(v_stack_m190, v_stack_m68, v_stack_m1C0, v_stack_m1A0);
    *(unsigned int *)(v_stack_m150 + 28) = (unsigned int)((unsigned int)(v_stack_m68));
    *(unsigned int *)(v_stack_m150 + 32) = (unsigned int)((unsigned int)(v_stack_m64));
    *(unsigned int *)(v_stack_m150 + 36) = (unsigned int)((unsigned int)(v_stack_m60));
    *(unsigned int *)(v_stack_m150 + 40) = (unsigned int)((unsigned int)(v_stack_m5C));
    *(unsigned int *)(v_stack_m150 + 44) = (unsigned int)((unsigned int)(v_stack_m58));
    *(unsigned int *)(v_stack_m150 + 48) = (unsigned int)((unsigned int)(v_stack_m54));
    *(unsigned int *)(v_stack_m150 + 52) = (unsigned int)((unsigned int)(v_stack_m50));
    *(unsigned int *)(v_stack_m150 + 56) = (unsigned int)((unsigned int)(v_stack_m4C));
    result = (unsigned int)((v_stack_m1B0) - ((unsigned int)(v_stack_m158)));
    *(unsigned int *)(v_stack_m158 + 4) = (unsigned int)(result);
    goto loc_0095D061;
loc_0095D061:
    v_stack_m1D8 = *(unsigned __int64 *)(a1 + 1680);
loc_0095D06D:
    if ((*(unsigned __int64 *)(a1 + 1680)) != (a1 + 1680)) goto loc_0095D229;
    if ((*(unsigned int *)(v_stack_m190 + 1284)) != 0) goto loc_0095D143;
loc_0095D098:
    *(unsigned __int64 *)(a1 + 8) = 0;
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0095D173;
loc_0095D0AE:
    result = KeAbPostRelease(a1, v_stack_m68, v_stack_m1C0, v_stack_m1A0);
    result = KeLeaveCriticalRegion(a1, v_stack_m68, v_stack_m1C0, v_stack_m1A0);
    result = EtwpCovSampContextPruneModules(a1 + 16, v_stack_m68, v_stack_m1C0, v_stack_m1A0);
    *(unsigned int *)(v_stack_m148) = (unsigned int)((unsigned int)(v_stack_m1A8));
loc_0095D0D8:
    if ((*(unsigned __int64 *)(a1 + 16 + 1184)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0095D268;
    if ((*(unsigned __int64 *)(a1 + 8)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0095D297;
    if (v_stack_m1C0 != 0) goto loc_0095D2BA;
    result = EtwpCovSampReleaseSamplerRundown(v_stack_m168, v_stack_m68, v_stack_m1C0, v_stack_m1A0);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m68, v_stack_m1C0, v_stack_m1A0);
    v_rsp = (v_rsp) + (480);
    return result;
loc_0095D143:
    *(unsigned int *)(result + 1284) = 0;
    goto loc_0095D169;
loc_0095D155:
    *(unsigned int *)(*(unsigned __int64 *)(result + 944) + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 1284)));
loc_0095D169:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 944))) != (result + 944)) goto loc_0095D155;
    goto loc_0095D098;
loc_0095D173:
    result = ExfTryToWakePushLock(a1, result + 944, v_stack_m1C0, v_stack_m1A0);
    goto loc_0095D0AE;
loc_0095D180:
loc_0095D185:
    v_rbx = (v_rbx) | (-1);
loc_0095D18F:
    goto loc_0095D0D8;
loc_0095D197:
    a2 = (unsigned int)((result + 944) + (*(unsigned int *)(result + 16)));
    if ((*(unsigned __int64 *)(result)) != a1) goto loc_0095D197;
    v_stack_p40 = *(unsigned __int64 *)(result);
    v_stack_p68 = (unsigned int)(a2);
    goto loc_0095C64C;
loc_0095D1B0:
    goto loc_0095C767;
loc_0095D1BD:
    if ((*(unsigned __int64 *)(result)) == a1) goto loc_0095C823;
    result = ExfReleasePushLockShared(a1 + 16 + 1176, a2, v_stack_m1C0, v_stack_m1A0);
    goto loc_0095C823;
loc_0095D1E1:
    *(unsigned int *)(v_stack_pD0) = (unsigned int)(a2);
    goto loc_0095D18F;
loc_0095D1F2:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(0 * 8)), (unsigned int)(0x56777445ULL), v_stack_m1A0);
    v_stack_p58 = result;
    goto loc_0095D0D8;
loc_0095D229:
    v_stack_pF8 = (unsigned int)(0xC000009AULL);
    v_stack_p40 = *(unsigned __int64 *)((unsigned int)(0xC000009AULL));
    a3 = ((unsigned int)(*(unsigned int *)((unsigned int)(0xC000009AULL) + 20))) << (3);
    a2 = 0;
    result = memset(*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 24), a2, a3, v_stack_m1A0);
    *(unsigned int *)((unsigned int)(0xC000009AULL) + 16) = 0;
    goto loc_0095D06D;
loc_0095D268:
    *(unsigned __int64 *)(a1 + 16 + 1184) = 0;
    result = (unsigned __int8)((v_rbx) & (6));
    result = ExfTryToWakePushLock(a1 + 16 + 1176, a2, a3, v_stack_m1A0);
loc_0095D297:
    *(unsigned __int64 *)(a1 + 8) = 0;
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    result = ExfTryToWakePushLock(a1, a2, a3, v_stack_m1A0);
loc_0095D2BA:
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCoverageSamplerQuery(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint32_t v_stack_m1A8;
    uint32_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C4;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1E0;
    uint32_t v_stack_m1E4;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_m88;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p34;
    uint64_t v_stack_p40;
    uint64_t v_stack_p58;
    uint32_t v_stack_p68;
    uint64_t v_stack_p88;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pF8;

    local_rsp = (local_rsp) - (480);
    result = (*(uint64_t *)(v_rip + 0x4AE284)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m148 = Arg4;
    v_stack_m1E0 = Arg3;
    v_stack_m1A0 = Arg2;
    v_stack_m138 = Arg1;
    local_rsi = 0;
    *(uint64_t *)(local_rsp - 0x168) = 0;
    v_stack_m190 = *(uint64_t *)(v_rip + 0x5A2CF4);
    *(uint64_t *)(local_rsp - 0x68) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm0;
    v_stack_m140 = Arg1 + 16;
    v_stack_m1D0 = 0;
    *(uint64_t *)(local_rsp - 0x158) = 0;
    v_stack_m188 = v_xmm0;
    v_stack_m1E4 = 0;
    v_stack_m1C0 = 0;
    *(uint64_t *)(local_rsp - 0x150) = 0;
    result = EtwpCovSampAcquireSamplerRundown(local_rsp - 360, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_0095D185;
    if (v_stack_m168 != Arg1) goto loc_0095D180;
    result = 0;
    v_stack_mB0 = 0;
    result = EtwpCovSampCaptureFlushSampleBuffers(*(uint64_t *)(v_rip + 0x5A2CF4), Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = memset(v_stack_mB8, Arg2, local_rsi + 80, Arg4);
    v_stack_mA8 = (uint32_t)(0xF1A5BFFAULL);
    v_stack_mB8 = 0x1B1DULL;
    Arg3 = 0;
    Arg2 = 0;
    result = KeInitializeEvent(v_stack_m88, Arg2, Arg3, Arg4);
    result = EtwpCovSampCaptureQueueBuffer(*(uint64_t *)(v_rip + 0x5A2CF4), v_stack_mB8, Arg3, Arg4);
    v_stack_m1F8 = 0;
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_stack_m88, Arg2, Arg3, Arg4);
    local_rbx = (*(uint64_t *)(v_rip + 0x5A2CF4)) | (-1);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1;
        Arg2 = result;
        Arg1 = Arg1;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m1B0 = 0;
    v_stack_m1D8 = *(uint64_t *)(arg1 + 0x690);
    if ((*(uint64_t *)(arg1 + 0x690)) != (Arg1 + 1680)) goto loc_0095D197;
loc_0095C64C:
    result = (0) << (3);
    Arg1 = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    if (result <= ((uint32_t)(0xFFFFFFFFULL))) { Arg1 = (uint32_t)(result); }
    local_rdi = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_0095D18F;
    Arg2 = (uint32_t)(0xFFFFFFFFULL);
    if (((uint32_t)(Arg1 + 1232)) >= ((uint32_t)(Arg1))) { Arg2 = (uint32_t)(Arg1 + 1232); }
    v_stack_m1A8 = (uint32_t)(Arg2);
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (((uint32_t)(Arg1 + 1232)) < ((uint32_t)(Arg1))) goto loc_0095D18F;
    v_stack_m1E4 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1E8 = 0;
    v_stack_m1C4 = 0;
    v_stack_m1C8 = 0;
    v_stack_m180 = v_stack_m188;
    v_stack_m188 = v_stack_m188;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 16 + 1176, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = Arg1 + 16 + 1176;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1 + 16 + 1176;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_m1D8 = *(uint64_t *)(arg1 + 0x10 + 0x4C8);
loc_0095C72D:
loc_0095C735:
    if ((*(uint64_t *)(arg1 + 0x10 + 0x4C8)) == (Arg1 + 16 + 1224)) goto loc_0095D1BD;
    v_stack_m1D8 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10 + 0x4C8));
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x10 + 0x4C8) + 0x3C)) != 0) goto loc_0095C757;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x10 + 0x4C8) + 0x30)) & (0x100000ULL)) == 0) goto loc_0095C735;
loc_0095C757:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x10 + 0x4C8) + 0x20)) != 0) goto loc_0095C773;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x10 + 0x4C8) - 0x8)) == 1) goto loc_0095D1B0;
loc_0095C767:
    goto loc_0095C72D;
loc_0095C773:
    local_r12 = (uint32_t)((0) + (1));
    v_stack_m1E4 = (uint32_t)(local_r12);
    v_stack_m1B8 = (uint32_t)(local_r12);
    result = (uint32_t)(((uint32_t)(v_stack_m1C4)) + ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10 + 0x4C8) + 0x30))) * 2 + 2)));
    local_rdi = (uint32_t)(0xFFFFFFFFULL);
    if (((uint32_t)(result)) >= ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10 + 0x4C8) + 0x30))) * 2 + 2))) { local_rdi = (uint32_t)(result); }
    v_stack_m1C4 = (uint32_t)(local_rdi);
    local_rdi = (uint32_t)((local_rdi) & (0xC0000095ULL));
    if (((uint32_t)(result)) < ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10 + 0x4C8) + 0x30))) * 2 + 2))) goto loc_0095D18F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10 + 0x4C8) - 0x10)) - 1) & (3));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10 + 0x4C8) - 0x10))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) + (3));
    local_r11 = (uint32_t)(0xFFFFFFFFULL);
    if (((uint32_t)(Arg1 + 0 * 1)) >= ((uint32_t)(Arg1))) { local_r11 = (uint32_t)(Arg1 + 0 * 1); }
    v_stack_m1C8 = (uint32_t)(local_r11);
    local_rdi = (uint32_t)((local_rdi) & (0xC0000095ULL));
    if (((uint32_t)(Arg1 + 0 * 1)) < ((uint32_t)(Arg1))) goto loc_0095D18F;
    Arg2 = (*(uint64_t *)(arg1 + 0x10 + 0x4C8)) + (72);
    if ((*(uint64_t *)(v_stack_m180)) != v_stack_m188) {
        Arg1 = 3;
    }
    *(uint64_t *)(Arg2) = v_stack_m188;
    *(uint64_t *)(Arg2 + 0x8) = v_stack_m180;
    *(uint64_t *)(v_stack_m180) = Arg2;
    v_stack_m180 = Arg2;
    goto loc_0095C735;
loc_0095C823:
    result = KeAbPostRelease(local_rdi, Arg2, v_stack_m1D8, Arg2);
    result = KeLeaveCriticalRegion(local_rdi, Arg2, v_stack_m1D8, Arg2);
    Arg1 = ((uint32_t)(v_stack_m1E8) + (uint32_t)(v_stack_m1E8) * 2) << (4);
    result = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    if (Arg1 <= ((uint32_t)(0xFFFFFFFFULL))) { result = (uint32_t)(Arg1); }
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (Arg1 > ((uint32_t)(0xFFFFFFFFULL))) goto loc_0095D18F;
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(v_stack_m1A8))));
    Arg2 = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(v_stack_m1A8)))) { Arg2 = (uint32_t)(result); }
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(v_stack_m1A8)))) goto loc_0095D18F;
    result = (uint32_t)(((uint32_t)(v_stack_m1C4)) + ((uint32_t)(Arg2)));
    Arg1 = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    if (((uint32_t)(result)) >= ((uint32_t)(Arg2))) { Arg1 = (uint32_t)(result); }
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (((uint32_t)(result)) < ((uint32_t)(Arg2))) goto loc_0095D18F;
    result = (uint32_t)(((uint32_t)(v_stack_m1C8)) + ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((uint32_t)((uint32_t)(0xFFFFFFFFULL)));
    if (((uint32_t)(result)) >= ((uint32_t)(Arg1))) { Arg2 = (uint32_t)(result); }
    v_stack_m1A8 = (uint32_t)(Arg2);
    local_rdi = (uint32_t)((local_rdi) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (((uint32_t)(result)) < ((uint32_t)(Arg1))) goto loc_0095D18F;
    if (v_stack_m1E0 < ((uint32_t)(Arg2))) goto loc_0095D1E1;
    if ((uint32_t)(local_r12) != 0) goto loc_0095D1F2;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x10))))) != 0) goto loc_0095CAA9;
loc_0095C8DB:
    v_stack_m1D0 = v_stack_m1A0;
    v_stack_m1D0 = v_stack_m1A0 + 20;
    v_stack_m158 = v_stack_m1A0 + 20;
    Arg2 = (v_stack_m1A0 + 20) + (44);
    v_stack_m1D0 = Arg2;
    result = 0;
    *(uint64_t *)(v_stack_m1A0 + 0x14) = v_xmm0;
    *(uint64_t *)(v_stack_m1A0 + 0x14 + 0x10) = v_xmm0;
    *(uint64_t *)(v_stack_m1A0 + 0x14 + 0x20) = 0;
    *(uint32_t *)(v_stack_m1A0 + 0x14 + 0x28) = 0;
    *(uint32_t *)(v_stack_m1A0 + 0x14) = 44;
    *(uint32_t *)(v_stack_m1A0 + 0x14 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x6BC)));
    *(uint32_t *)(v_stack_m1A0 + 0x14 + 0x10) = (uint32_t)((uint32_t)(0x454ULL));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(v_stack_m1A0 + 20)));
    *(uint32_t *)(v_stack_m1A0 + 0x14 + 0xC) = (uint32_t)(result);
    v_stack_mE8 = Arg2;
    Arg2 = (Arg2) + ((uint32_t)(0x454ULL));
    v_stack_m1D0 = Arg2;
loc_0095C966:
    *(uint64_t *)(Arg2) = v_xmm0;
    *(uint64_t *)(Arg2 + 0x10) = v_xmm1;
    *(uint64_t *)(Arg2 + 0x20) = v_xmm0;
    *(uint64_t *)(Arg2 + 0x30) = v_xmm1;
    *(uint64_t *)(Arg2 + 0x40) = v_xmm0;
    *(uint64_t *)(Arg2 + 0x50) = v_xmm1;
    *(uint64_t *)(Arg2 + 0x60) = v_xmm0;
    Arg1 = (Arg2) + (8 + 120);
    *(uint64_t *)(arg1 - 0x10) = v_xmm1;
    result = (Arg1 + 16 + 8) + (8 + 120);
    Arg3 = (8) - (1);
    if (condition_is_not_equal) goto loc_0095C966;
    *(uint64_t *)(arg1) = v_xmm0;
    *(uint64_t *)(arg1 + 0x10) = v_xmm1;
    *(uint64_t *)(arg1 + 0x20) = v_xmm0;
    *(uint64_t *)(arg1 + 0x30) = v_xmm1;
    *(uint64_t *)(arg1 + 0x40) = v_xmm0;
    *(uint32_t *)(arg1 + 0x50) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x50)));
    *(uint32_t *)(v_stack_m1A0 + 0x14 + 0x18) = 60;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(v_stack_m1A0 + 20)));
    *(uint32_t *)(v_stack_m1A0 + 0x14 + 0x14) = (uint32_t)(result);
    v_stack_m150 = Arg2;
    Arg2 = (Arg2) + (60);
    v_stack_m1D0 = Arg2;
    *(uint32_t *)(v_stack_m1A0 + 0x14 + 0x20) = (uint32_t)((uint32_t)(v_stack_m1B0));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(v_stack_m1A0 + 20)));
    *(uint32_t *)(v_stack_m1A0 + 0x14 + 0x1C) = (uint32_t)(result);
    v_stack_m118 = Arg2;
    v_stack_m1D0 = Arg2 + (uint32_t)(v_stack_m1B0) * 8;
    v_stack_mE0 = Arg2 + (uint32_t)(v_stack_m1B0) * 8;
loc_0095CA33:
    v_stack_m1D8 = *(uint64_t *)(arg1 + 0x690);
    if ((*(uint64_t *)(arg1 + 0x690)) == (Arg1 + 1680)) goto loc_0095CC4E;
    v_stack_m120 = *(uint64_t *)(arg1 + 0x690);
    v_stack_m170 = 0;
loc_0095CA5A:
    if (0 >= (*(uint32_t *)(*(uint64_t *)(arg1 + 0x690) + 0x14))) goto loc_0095CAA4;
    v_stack_mD8 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x690) + 0x18) + 0 * 8;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x690) + 0x18) + 0x0 * 8)) != 0) goto loc_0095CA85;
loc_0095CA78:
    Arg4 = (uint32_t)((0) + (1));
    v_stack_m170 = (uint32_t)(Arg4);
    goto loc_0095CA5A;
loc_0095CA85:
    if (Arg2 >= (Arg2 + (uint32_t)(v_stack_m1B0) * 8)) goto loc_0095CAA4;
    *(uint32_t *)(Arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x690) + 0x18) + 0x0 * 8)));
    *(uint32_t *)(Arg2 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x690) + 0x18) + 0x0 * 8 + 0x4)));
    Arg2 = (Arg2) + (8);
    v_stack_m118 = Arg2;
    goto loc_0095CA78;
loc_0095CAA4:
    goto loc_0095CA33;
loc_0095CAA9:
    if (*(uint64_t *)(v_stack_m190 + 0x528) == 0) goto loc_0095CB79;
    v_stack_m1E0 = *(uint64_t *)(v_stack_m190 + 0x528);
    v_stack_m108 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - (1));
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m1E0, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg1 = v_stack_m1E0;
        Arg3 = Arg1;
        Arg2 = result;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_m100 = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(v_stack_m1E0 + 0x8) = *(uint64_t *)(gs_base + (0 + 0x188));
    Arg3 = ((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x14))) << (2);
    Arg2 = 0;
    result = memset(v_stack_m1E0 + 24, Arg2, Arg3, Arg4);
    *(uint64_t *)(v_stack_m1E0 + 0x8) = 0;
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = v_stack_m1E0;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(v_stack_m1E0, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegion(v_stack_m1E0, Arg2, Arg3, Arg4);
loc_0095CB79:
    if (*(uint64_t *)(v_stack_m190 + 0x530) == 0) goto loc_0095C8DB;
    v_stack_m1E0 = *(uint64_t *)(v_stack_m190 + 0x530);
    v_stack_mF8 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - (1));
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m1E0, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg1 = v_stack_m1E0;
        Arg3 = Arg1;
        Arg2 = result;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_mF0 = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(v_stack_m1E0 + 0x8) = *(uint64_t *)(gs_base + (0 + 0x188));
    Arg3 = ((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x14))) << (2);
    Arg2 = 0;
    result = memset(v_stack_m1E0 + 24, Arg2, Arg3, Arg4);
    *(uint64_t *)(v_stack_m1E0 + 0x8) = 0;
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = v_stack_m1E0;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(v_stack_m1E0, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegion(v_stack_m1E0, Arg2, Arg3, Arg4);
    goto loc_0095C8DB;
loc_0095CC4E:
    goto loc_0095CC7E;
loc_0095CC7E:
    *(uint32_t *)(result + 0x28) = (uint32_t)((uint32_t)(v_stack_m1E8));
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m1E0))) - ((uint32_t)(result)));
    *(uint32_t *)(result + 0x24) = (uint32_t)(result);
    v_stack_m130 = v_stack_m1E0;
    Arg1 = ((uint32_t)(v_stack_m1E8) + (uint32_t)(v_stack_m1E8) * 2) << (4);
    local_rdi = (v_stack_m1E0) + (Arg1);
    v_stack_m1D0 = local_rdi;
    Arg3 = (local_rdi) - (v_stack_m1E0);
    Arg2 = 0;
    result = memset(v_stack_m1E0, Arg2, Arg3, v_stack_m1E0);
    v_stack_m1A0 = local_rdi;
    local_rdi = (local_rdi) + ((uint32_t)(v_stack_m1C8));
    v_stack_m1D0 = local_rdi;
    v_stack_m128 = local_rdi;
    v_stack_m178 = local_rdi;
    local_rdi = (local_rdi) + ((uint32_t)(v_stack_m1C4));
    v_stack_m1B0 = local_rdi;
    v_stack_m1D0 = local_rdi;
    v_stack_m160 = local_rdi;
    v_stack_m198 = 0;
    v_stack_m1D8 = v_stack_m188;
loc_0095CD10:
    if (v_stack_m188 == v_stack_m188) goto loc_0095CF44;
    v_stack_m1D8 = *(uint64_t *)(v_stack_m188);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - ((uint32_t)(result)));
    *(uint32_t *)(v_stack_m130 + 0x8) = (uint32_t)(result);
    *(uint32_t *)(v_stack_m130 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x58)));
    Arg1 = (uint32_t)((local_rdi) - ((uint32_t)(result)));
    *(uint32_t *)(v_stack_m130) = (uint32_t)(Arg1);
    *(uint32_t *)(v_stack_m130 + 0x4) = (uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x18))));
    *(uint32_t *)(v_stack_m130 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x6C)));
    *(uint32_t *)(v_stack_m130 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x70)));
    *(uint32_t *)(v_stack_m130 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x68)));
    *(uint32_t *)(v_stack_m130 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x14)));
    *(uint32_t *)(v_stack_m130 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x10)));
    *(uint32_t *)(v_stack_m130 + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x10)));
    *(uint32_t *)(v_stack_m130 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x14)));
    *(uint32_t *)(v_stack_m130 + 0x2C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 + 0x18)));
    Arg2 = (v_stack_m130) + (48);
    v_stack_m130 = Arg2;
    result = memcpy(local_rdi, *(uint64_t *)(v_stack_m188 - 0x60), (uint32_t)(*(uint32_t *)(v_stack_m188 - 0x58)), local_rdi);
    Arg1 = (v_stack_m1A0) + (3);
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x58)));
    Arg1 = (Arg1) & (-4);
    v_stack_m1A0 = Arg1;
    if (Arg1 > v_stack_m128) goto loc_0095CF44;
    Arg2 = (v_stack_m160) - (v_stack_m178);
    Arg2 = (Arg2) >> (1);
    result = RtlStringCchCopyNW(v_stack_m178, Arg2, *(uint64_t *)(v_stack_m188 - 0x20), (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x18))));
    result = (uint32_t)(((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x18)))) + (1));
    v_stack_m178 = v_stack_m178 + result * 2;
    if ((v_stack_m178 + result * 2) > v_stack_m160) goto loc_0095CF44;
    v_stack_mD0 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - (1));
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 16 + 1176, Arg2, Arg3, (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x18))));
    v_stack_m1B0 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 16 + 1176;
        Arg2 = result;
        Arg1 = Arg1 + 16 + 1176;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x18))));
        result = v_stack_m1B0;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_mC8 = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(arg1 + 0x10 + 0x4A0) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(v_stack_m1C0 + (uint32_t)(v_stack_m198) * 8) = *(uint64_t *)(v_stack_m188 - 0x28);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m198)) + (1));
    v_stack_m198 = (uint32_t)(Arg2);
    *(uint64_t *)(v_stack_m188 - 0x28) = 0;
    *(uint64_t *)(v_stack_m188 - 0x20) = 0;
    *(uint32_t *)(v_stack_m188 - 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x18)));
    *(uint64_t *)(arg1 + 0x10 + 0x4A0) = 0;
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0095CF30;
loc_0095CEE6:
    result = KeAbPostRelease(Arg1 + 16 + 1176, Arg2, v_stack_m1C0, (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x18))));
    result = KeLeaveCriticalRegion(Arg1 + 16 + 1176, Arg2, v_stack_m1C0, (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m188 - 0x18))));
    if ((*(uint64_t *)(v_stack_m188 - 0x50)) == 1) goto loc_0095CF3A;
loc_0095CF02:
    v_stack_m1B0 = v_stack_m1D0;
    goto loc_0095CD10;
loc_0095CF30:
    result = ExfTryToWakePushLock(v_stack_m158, Arg2, v_stack_m1C0, v_stack_m1A0);
    goto loc_0095CEE6;
loc_0095CF3A:
    goto loc_0095CF02;
loc_0095CF44:
    *(uint64_t *)(v_stack_m150) = v_xmm0;
    *(uint64_t *)(v_stack_m150 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m150 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m150 + 0x30) = v_xmm1;
    *(uint32_t *)(v_stack_m150 + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10 + 0x494)));
    result = 0;
    *(uint64_t *)(arg1 + 0x10 + 0x45C) = v_xmm0;
    *(uint64_t *)(arg1 + 0x10 + 0x46C) = v_xmm0;
    *(uint64_t *)(arg1 + 0x10 + 0x47C) = v_xmm0;
    *(uint64_t *)(arg1 + 0x10 + 0x48C) = 0;
    *(uint32_t *)(arg1 + 0x10 + 0x494) = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    result = EtwpCovSampCaptureFlushStats(v_stack_m190, v_stack_m68, v_stack_m1C0, v_stack_m1A0);
    *(uint32_t *)(v_stack_m150 + 0x1C) = (uint32_t)((uint32_t)(v_stack_m68));
    *(uint32_t *)(v_stack_m150 + 0x20) = (uint32_t)((uint32_t)(v_stack_m64));
    *(uint32_t *)(v_stack_m150 + 0x24) = (uint32_t)((uint32_t)(v_stack_m60));
    *(uint32_t *)(v_stack_m150 + 0x28) = (uint32_t)((uint32_t)(v_stack_m5C));
    *(uint32_t *)(v_stack_m150 + 0x2C) = (uint32_t)((uint32_t)(v_stack_m58));
    *(uint32_t *)(v_stack_m150 + 0x30) = (uint32_t)((uint32_t)(v_stack_m54));
    *(uint32_t *)(v_stack_m150 + 0x34) = (uint32_t)((uint32_t)(v_stack_m50));
    *(uint32_t *)(v_stack_m150 + 0x38) = (uint32_t)((uint32_t)(v_stack_m4C));
    result = (uint32_t)((v_stack_m1B0) - ((uint32_t)(v_stack_m158)));
    *(uint32_t *)(v_stack_m158 + 0x4) = (uint32_t)(result);
    goto loc_0095D061;
loc_0095D061:
    v_stack_m1D8 = *(uint64_t *)(arg1 + 0x690);
loc_0095D06D:
    if ((*(uint64_t *)(arg1 + 0x690)) != (Arg1 + 1680)) goto loc_0095D229;
    if ((*(uint32_t *)(v_stack_m190 + 0x504)) != 0) goto loc_0095D143;
loc_0095D098:
    *(uint64_t *)(arg1 + 0x8) = 0;
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0095D173;
loc_0095D0AE:
    result = KeAbPostRelease(Arg1, v_stack_m68, v_stack_m1C0, v_stack_m1A0);
    result = KeLeaveCriticalRegion(Arg1, v_stack_m68, v_stack_m1C0, v_stack_m1A0);
    result = EtwpCovSampContextPruneModules(Arg1 + 16, v_stack_m68, v_stack_m1C0, v_stack_m1A0);
    *(uint32_t *)(v_stack_m148) = (uint32_t)((uint32_t)(v_stack_m1A8));
loc_0095D0D8:
    if ((*(uint64_t *)(arg1 + 0x10 + 0x4A0)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0095D268;
    if ((*(uint64_t *)(arg1 + 0x8)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0095D297;
    if (v_stack_m1C0 != 0) goto loc_0095D2BA;
    result = EtwpCovSampReleaseSamplerRundown(v_stack_m168, v_stack_m68, v_stack_m1C0, v_stack_m1A0);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m68, v_stack_m1C0, v_stack_m1A0);
    local_rsp = (local_rsp) + (480);
    return result;
loc_0095D143:
    *(uint32_t *)(result + 0x504) = 0;
    goto loc_0095D169;
loc_0095D155:
    *(uint32_t *)(*(uint64_t *)(result + 0x3B0) + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x504)));
loc_0095D169:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x3B0))) != (result + 944)) goto loc_0095D155;
    goto loc_0095D098;
loc_0095D173:
    result = ExfTryToWakePushLock(Arg1, result + 944, v_stack_m1C0, v_stack_m1A0);
    goto loc_0095D0AE;
loc_0095D180:
loc_0095D185:
    local_rbx = (local_rbx) | (-1);
loc_0095D18F:
    goto loc_0095D0D8;
loc_0095D197:
    Arg2 = (uint32_t)((result + 944) + (*(uint32_t *)(result + 0x10)));
    if ((*(uint64_t *)(result)) != Arg1) goto loc_0095D197;
    v_stack_p40 = *(uint64_t *)(result);
    v_stack_p68 = (uint32_t)(Arg2);
    goto loc_0095C64C;
loc_0095D1B0:
    goto loc_0095C767;
loc_0095D1BD:
    if ((*(uint64_t *)(result)) == Arg1) goto loc_0095C823;
    result = ExfReleasePushLockShared(Arg1 + 16 + 1176, Arg2, v_stack_m1C0, v_stack_m1A0);
    goto loc_0095C823;
loc_0095D1E1:
    *(uint32_t *)(v_stack_pD0) = (uint32_t)(Arg2);
    goto loc_0095D18F;
loc_0095D1F2:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(0 * 8)), (uint32_t)(0x56777445ULL), v_stack_m1A0);
    v_stack_p58 = result;
    goto loc_0095D0D8;
loc_0095D229:
    v_stack_pF8 = (uint32_t)(0xC000009AULL);
    v_stack_p40 = *(uint64_t *)((uint32_t)(0xC000009AULL));
    Arg3 = ((uint32_t)(*(uint32_t *)((uint32_t)(0xC000009AULL) + 0x14))) << (3);
    Arg2 = 0;
    result = memset(*(uint64_t *)((uint32_t)(0xC000009AULL) + 0x18), Arg2, Arg3, v_stack_m1A0);
    *(uint32_t *)((uint32_t)(0xC000009AULL) + 0x10) = 0;
    goto loc_0095D06D;
loc_0095D268:
    *(uint64_t *)(arg1 + 0x10 + 0x4A0) = 0;
    result = (uint8_t)((local_rbx) & (6));
    result = ExfTryToWakePushLock(Arg1 + 16 + 1176, Arg2, Arg3, v_stack_m1A0);
loc_0095D297:
    *(uint64_t *)(arg1 + 0x8) = 0;
    local_rbx = (uint8_t)((local_rbx) & (6));
    result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, v_stack_m1A0);
loc_0095D2BA:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg1` | `+ 0x20` | `128` | `R` |
| `Arg1` | `+ 0x30` | `128` | `R` |
| `Arg1` | `+ 0x40` | `128` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x50` | `128` | `R` |
| `Arg1` | `+ 0x60` | `128` | `R` |
| `Arg1` | `+ 0x70` | `128` | `R` |
| `Arg1` | `+ 0x45C` | `128` | `R` |
| `Arg1` | `+ 0x46C` | `128` | `R` |
| `Arg1` | `+ 0x47C` | `128` | `R` |
| `Arg1` | `+ 0x48C` | `64` | `R` |
| `Arg1` | `+ 0x48C` | `64` | `W` |
| `Arg1` | `+ 0x494` | `32` | `R` |
| `Arg1` | `+ 0x494` | `32` | `W` |
| `Arg1` | `+ 0x498` | `64` | `R` |
| `Arg1` | `+ 0x498` | `64` | `R/W` |
| `Arg1` | `+ 0x4A0` | `64` | `R` |
| `Arg1` | `+ 0x4A0` | `64` | `W` |
| `Arg1` | `+ 0x4C8` | `64` | `R` |
| `Arg1` | `+ 0x664` | `32` | `R/W` |
| `Arg1` | `+ 0x680` | `64` | `R` |
| `Arg1` | `+ 0x690` | `64` | `R` |
| `Arg1` | `+ 0x6BC` | `32` | `R` |
| `Arg1` | `+ 0x6BC` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0095C4A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
