# sub_0086560A

- RVA: `0x0086560A`–`0x00865B4B` (길이 `1,345` bytes)
- VA: `0x000000014086560A`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006BB28`
- 디코드: `319`개 명령, `1,345/1,345` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0086563A` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x00865670` → [CmpCallCallBacksEx](CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x00865691` → [CmpFireCleanupNotifications](CmpFireCleanupNotifications_function_008649B0.md) (function, `0x008649B0`)
- `0x008656C3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008656E8` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00865741` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086574F` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086577E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00865793` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x008657C5` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008657E1` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00865811` → [CmLockHive](../85/CmLockHive_function_008512B4.md) (function, `0x008512B4`)
- `0x00865845` → [CmpPostNotify](CmpPostNotify_function_008645D8.md) (function, `0x008645D8`)
- `0x0086585B` → [SeReleaseSubjectContext](SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00865881` → [CmUnlockHive](../85/CmUnlockHive_function_00851D6C.md) (function, `0x00851D6C`)
- `0x0086588B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00865893` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00865905` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086597E` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008659F8` → [CmpDereferenceKeyControlBlock](../85/CmpDereferenceKeyControlBlock_function_00851310.md) (function, `0x00851310`)
- `0x00865A19` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00865A24` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x00865A38` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x00865A40` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x00865A48` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00865A5D` → [CmpDereferenceKeyControlBlock](../85/CmpDereferenceKeyControlBlock_function_00851310.md) (function, `0x00851310`)
- `0x00865A62` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x00865A81` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (function, `0x00456A7C`)
- `0x00865AE0` → [CmpCallCallBacksEx](CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)
- `0x00865B08` → [CmpDeleteHive](CmpDeleteHive_function_0086450C.md) (function, `0x0086450C`)
- `0x00865B16` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00865B1F` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0086562E` → RVA `0x00EEFB88` (`.data`; read)
- `0x008656A1` → RVA `0x00EF7BC8` (`.data`; read)
- `0x008656C8` → RVA `0x00EF7BC8` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x0086563A` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x008656C3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008656E8` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00865741` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086574F` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086577E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00865793` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x008657C5` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008657E1` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086588B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00865893` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00865905` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086597E` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00865A19` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00865A24` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x00865A38` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x00865A40` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x00865A48` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00865A62` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x00865A81` → [CmpIsRegistryLockAcquired](../../text/45/CmpIsRegistryLockAcquired_function_00456A7C.md) (`PAGE` → `.text`)
  - `0x00865B16` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00865B1F` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **13**
  - `0x00865725` → [sub_00865B4C + 0xE0](Unknown_function_00865B4C.md) (`tail-transfer`)
  - `0x00865734` → [sub_00865B4C + 0xE0](Unknown_function_00865B4C.md) (`tail-transfer`)
  - `0x00865757` → [sub_00865C6D + 0xAD](Unknown_function_00865C6D.md) (`tail-transfer`)
  - `0x008657AC` → [sub_00865C6D + 0xD](Unknown_function_00865C6D.md) (`tail-transfer`)
  - `0x0086581D` → [sub_00865C6D](Unknown_function_00865C6D.md) (`tail-transfer`)
  - `0x00865851` → [sub_00865C6D](Unknown_function_00865C6D.md) (`tail-transfer`)
  - `0x008658AD` → [sub_00865B4C + 0x62](Unknown_function_00865B4C.md) (`tail-transfer`)
  - `0x008658D6` → [sub_00865C6D + 0x9B](Unknown_function_00865C6D.md) (`tail-transfer`)
  - `0x00865958` → [sub_00865C6D + 0x48](Unknown_function_00865C6D.md) (`tail-transfer`)
  - `0x008659A3` → [sub_00865C6D + 0x5F](Unknown_function_00865C6D.md) (`tail-transfer`)
  - `0x00865A13` → [sub_00865B4C + 0xD6](Unknown_function_00865B4C.md) (`tail-transfer`)
  - `0x00865A72` → [sub_00865B4C](Unknown_function_00865B4C.md) (`tail-transfer`)
  - `0x00865AE8` → [sub_00865B4C + 0xF1](Unknown_function_00865B4C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0086560A  48 89 BC 24 28 01 00 00         mov qword ptr [rsp + 0x128], rdi
00865612  4C 89 B4 24 30 01 00 00         mov qword ptr [rsp + 0x130], r14
0086561A  4C 89 BC 24 38 01 00 00         mov qword ptr [rsp + 0x138], r15
00865622  45 8D 7D 01                     lea r15d, [r13 + 1]
00865626  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086562D  90                              nop
0086562E  39 35 54 A5 68 00               cmp dword ptr [rip + 0x68a554], esi
00865634  0F 84 37 01 00 00               je 0x140865771
0086563A  E8 3D 14 BF FF                  call 0x140456a7c
0086563F  85 C0                           test eax, eax
00865641  0F 85 2A 01 00 00               jne 0x140865771
00865647  48 8D 45 A7                     lea rax, [rbp - 0x59]
0086564B  48 89 5D 17                     mov qword ptr [rbp + 0x17], rbx
0086564F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00865654  48 8D 55 17                     lea rdx, [rbp + 0x17]
00865658  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0086565D  41 8D 4D 0E                     lea ecx, [r13 + 0xe]
00865661  45 0F B6 CF                     movzx r9d, r15b
00865665  C7 44 24 20 19 00 00 00         mov dword ptr [rsp + 0x20], 0x19
0086566D  45 33 C0                        xor r8d, r8d
00865670  E8 CB 08 00 00                  call 0x140865f40
00865675  81 3B 32 30 79 6B               cmp dword ptr [rbx], 0x6b793032
0086567B  0F 85 F0 00 00 00               jne 0x140865771
00865681  48 8D 7B 48                     lea rdi, [rbx + 0x48]
00865685  48 39 3F                        cmp qword ptr [rdi], rdi
00865688  0F 84 E3 00 00 00               je 0x140865771
0086568E  48 8B CB                        mov rcx, rbx
00865691  E8 1A F3 FF FF                  call 0x1408649b0
00865696  48 8D 45 87                     lea rax, [rbp - 0x79]
0086569A  45 33 C0                        xor r8d, r8d
0086569D  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
008656A1  48 8D 0D 20 25 69 00            lea rcx, [rip + 0x692520]
008656A8  48 8D 45 87                     lea rax, [rbp - 0x79]
008656AC  33 D2                           xor edx, edx
008656AE  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
008656B2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008656BB  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008656C2  90                              nop
008656C3  E8 68 AB 9A FF                  call 0x140210230
008656C8  F0 48 0F BA 2D F6 24 69 00 00   lock bts qword ptr [rip + 0x6924f6], 0
008656D2  4C 8B F0                        mov r14, rax
008656D5  73 16                           jae 0x1408656ed
008656D7  4C 8D 05 EA 24 69 00            lea r8, [rip + 0x6924ea]
008656DE  48 8B D0                        mov rdx, rax
008656E1  48 8D 0D E0 24 69 00            lea rcx, [rip + 0x6924e0]
008656E8  E8 A3 A5 9A FF                  call 0x14020fc90
008656ED  4D 85 F6                        test r14, r14
008656F0  74 04                           je 0x1408656f6
008656F2  45 88 7E 0A                     mov byte ptr [r14 + 0xa], r15b
008656F6  48 8B 07                        mov rax, qword ptr [rdi]
008656F9  48 3B C7                        cmp rax, rdi
008656FC  0F 85 0D 02 00 00               jne 0x14086590f
00865702  0F 0D 0D BF 24 69 00            prefetchw byte ptr [rip + 0x6924bf]
00865709  48 8B 05 B8 24 69 00            mov rax, qword ptr [rip + 0x6924b8]
00865710  48 8B C8                        mov rcx, rax
00865713  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00865717  48 83 F9 10                     cmp rcx, 0x10
0086571B  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086571F  49 0F 46 D5                     cmovbe rdx, r13
00865723  A8 02                           test al, 2
00865725  0F 85 01 05 00 00               jne 0x140865c2c
0086572B  F0 48 0F B1 15 94 24 69 00      lock cmpxchg qword ptr [rip + 0x692494], rdx
00865734  0F 85 F2 04 00 00               jne 0x140865c2c
0086573A  48 8D 0D 87 24 69 00            lea rcx, [rip + 0x692487]
00865741  E8 BA BE A7 FF                  call 0x1402e1600
00865746  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086574F  E8 9C 98 9F FF                  call 0x14025eff0
00865754  45 84 E4                        test r12b, r12b
00865757  0F 85 BD 05 00 00               jne 0x140865d1a
0086575D  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
00865761  48 8D 45 87                     lea rax, [rbp - 0x79]
00865765  48 3B C8                        cmp rcx, rax
00865768  0F 85 73 01 00 00               jne 0x1408658e1
0086576E  45 32 E4                        xor r12b, r12b
00865771  48 8B 4B 38                     mov rcx, qword ptr [rbx + 0x38]
00865775  48 85 C9                        test rcx, rcx
00865778  74 09                           je 0x140865783
0086577A  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0086577E  E8 CD 3B A9 FF                  call 0x1402f9350
00865783  48 8D 45 97                     lea rax, [rbp - 0x69]
00865787  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
0086578B  48 8D 45 97                     lea rax, [rbp - 0x69]
0086578F  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00865793  E8 9C 43 36 00                  call 0x140bc9b34
00865798  4C 8B 73 08                     mov r14, qword ptr [rbx + 8]
0086579C  8B 03                           mov eax, dword ptr [rbx]
0086579E  4D 85 F6                        test r14, r14
008657A1  0F 84 BB 02 00 00               je 0x140865a62
008657A7  3D 32 30 79 6B                  cmp eax, 0x6b793032
008657AC  0F 85 C8 04 00 00               jne 0x140865c7a
008657B2  48 39 73 10                     cmp qword ptr [rbx + 0x10], rsi
008657B6  0F 84 DC 00 00 00               je 0x140865898
008657BC  45 33 C0                        xor r8d, r8d
008657BF  49 8D 4E 30                     lea rcx, [r14 + 0x30]
008657C3  33 D2                           xor edx, edx
008657C5  E8 66 AA 9A FF                  call 0x140210230
008657CA  F0 49 0F BA 6E 30 00            lock bts qword ptr [r14 + 0x30], 0
008657D1  48 8B F0                        mov rsi, rax
008657D4  73 10                           jae 0x1408657e6
008657D6  4D 8D 46 30                     lea r8, [r14 + 0x30]
008657DA  48 8B D0                        mov rdx, rax
008657DD  49 8D 4E 30                     lea rcx, [r14 + 0x30]
008657E1  E8 AA A4 9A FF                  call 0x14020fc90
008657E6  48 85 F6                        test rsi, rsi
008657E9  74 04                           je 0x1408657ef
008657EB  44 88 7E 0A                     mov byte ptr [rsi + 0xa], r15b
008657EF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008657F8  49 89 46 38                     mov qword ptr [r14 + 0x38], rax
008657FC  4C 39 6B 10                     cmp qword ptr [rbx + 0x10], r13
00865800  0F 84 8A 00 00 00               je 0x140865890
00865806  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0086580A  48 8B 70 20                     mov rsi, qword ptr [rax + 0x20]
0086580E  48 8B CE                        mov rcx, rsi
00865811  E8 9E BA FE FF                  call 0x1408512b4
00865816  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0086581A  48 85 C9                        test rcx, rcx
0086581D  0F 84 4A 04 00 00               je 0x140865c6d
00865823  48 8D 41 10                     lea rax, [rcx + 0x10]
00865827  48 39 00                        cmp qword ptr [rax], rax
0086582A  74 1E                           je 0x14086584a
0086582C  48 8D 45 97                     lea rax, [rbp - 0x69]
00865830  41 B9 0B 01 00 00               mov r9d, 0x10b
00865836  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086583B  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00865840  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
00865845  E8 8E ED FF FF                  call 0x1408645d8
0086584A  48 8B 7B 10                     mov rdi, qword ptr [rbx + 0x10]
0086584E  48 85 FF                        test rdi, rdi
00865851  0F 84 16 04 00 00               je 0x140865c6d
00865857  48 8D 4F 38                     lea rcx, [rdi + 0x38]
0086585B  E8 B0 5E 00 00                  call 0x14086b710
00865860  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00865864  48 8B 07                        mov rax, qword ptr [rdi]
00865867  48 89 02                        mov qword ptr [rdx], rax
0086586A  48 8B 17                        mov rdx, qword ptr [rdi]
0086586D  48 85 D2                        test rdx, rdx
00865870  74 08                           je 0x14086587a
00865872  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00865876  48 89 42 08                     mov qword ptr [rdx + 8], rax
0086587A  48 8B CE                        mov rcx, rsi
0086587D  4C 89 6B 10                     mov qword ptr [rbx + 0x10], r13
00865881  E8 E6 C4 FE FF                  call 0x140851d6c
00865886  33 D2                           xor edx, edx
00865888  48 8B CF                        mov rcx, rdi
0086588B  E8 E0 CF 31 00                  call 0x140b82870
00865890  49 8B CE                        mov rcx, r14
00865893  E8 28 3A 36 00                  call 0x140bc92c0
00865898  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
0086589B  45 32 C9                        xor r9b, r9b
0086589E  A8 40                           test al, 0x40
008658A0  0F 84 DD 00 00 00               je 0x140865983
008658A6  45 8B C5                        mov r8d, r13d
008658A9  41 83 F8 04                     cmp r8d, 4
008658AD  0F 83 FB 02 00 00               jae 0x140865bae
008658B3  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008658B7  41 8B C8                        mov ecx, r8d
008658BA  48 8D 14 C8                     lea rdx, [rax + rcx*8]
008658BE  48 8B C3                        mov rax, rbx
008658C1  F0 4C 0F B1 AA 88 00 00 00      lock cmpxchg qword ptr [rdx + 0x88], r13
008658CA  0F 84 9C 00 00 00               je 0x14086596c
008658D0  48 FF C8                        dec rax
008658D3  49 3B C7                        cmp rax, r15
008658D6  0F 86 2C 04 00 00               jbe 0x140865d08
008658DC  41 FF C0                        inc r8d
008658DF  EB C8                           jmp 0x1408658a9
008658E1  48 8D 45 87                     lea rax, [rbp - 0x79]
008658E5  48 39 41 08                     cmp qword ptr [rcx + 8], rax
008658E9  75 73                           jne 0x14086595e
008658EB  48 8B 01                        mov rax, qword ptr [rcx]
008658EE  48 39 48 08                     cmp qword ptr [rax + 8], rcx
008658F2  75 6A                           jne 0x14086595e
008658F4  48 8D 55 87                     lea rdx, [rbp - 0x79]
008658F8  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
008658FC  48 89 50 08                     mov qword ptr [rax + 8], rdx
00865900  BA 43 4D 63 63                  mov edx, 0x63634d43
00865905  E8 66 CF 31 00                  call 0x140b82870
0086590A  E9 4E FE FF FF                  jmp 0x14086575d
0086590F  48 39 78 08                     cmp qword ptr [rax + 8], rdi
00865913  75 49                           jne 0x14086595e
00865915  48 8B 08                        mov rcx, qword ptr [rax]
00865918  48 39 41 08                     cmp qword ptr [rcx + 8], rax
0086591C  75 40                           jne 0x14086595e
0086591E  48 89 0F                        mov qword ptr [rdi], rcx
00865921  48 89 79 08                     mov qword ptr [rcx + 8], rdi
00865925  48 8D 48 10                     lea rcx, [rax + 0x10]
00865929  4C 8B 01                        mov r8, qword ptr [rcx]
0086592C  49 39 48 08                     cmp qword ptr [r8 + 8], rcx
00865930  75 2C                           jne 0x14086595e
00865932  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00865936  48 39 0A                        cmp qword ptr [rdx], rcx
00865939  75 23                           jne 0x14086595e
0086593B  4C 89 02                        mov qword ptr [rdx], r8
0086593E  49 3B D0                        cmp rdx, r8
00865941  49 89 50 08                     mov qword ptr [r8 + 8], rdx
00865945  48 8D 55 87                     lea rdx, [rbp - 0x79]
00865949  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
0086594D  45 0F B6 E4                     movzx r12d, r12b
00865951  45 0F 44 E7                     cmove r12d, r15d
00865955  48 39 11                        cmp qword ptr [rcx], rdx
00865958  0F 84 57 03 00 00               je 0x140865cb5
0086595E  B9 03 00 00 00                  mov ecx, 3
00865963  CD 29                           int 0x29
00865965  48 89 11                        mov qword ptr [rcx], rdx
00865968  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0086596C  B8 BF FF 00 00                  mov eax, 0xffbf
00865971  66 21 43 30                     and word ptr [rbx + 0x30], ax
00865975  45 84 C9                        test r9b, r9b
00865978  74 09                           je 0x140865983
0086597A  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0086597E  E8 3D 39 36 00                  call 0x140bc92c0
00865983  49 8B 76 20                     mov rsi, qword ptr [r14 + 0x20]
00865987  0F 0D 8E 88 10 00 00            prefetchw byte ptr [rsi + 0x1088]
0086598E  8B 86 88 10 00 00               mov eax, dword ptr [rsi + 0x1088]
00865994  85 C0                           test eax, eax
00865996  74 11                           je 0x1408659a9
00865998  8D 48 01                        lea ecx, [rax + 1]
0086599B  F0 0F B1 8E 88 10 00 00         lock cmpxchg dword ptr [rsi + 0x1088], ecx
008659A3  0F 85 23 03 00 00               jne 0x140865ccc
008659A9  44 38 BE 80 0B 00 00            cmp byte ptr [rsi + 0xb80], r15b
008659B0  75 21                           jne 0x1408659d3
008659B2  45 0F B6 E7                     movzx r12d, r15b
008659B6  44 88 7D 67                     mov byte ptr [rbp + 0x67], r15b
008659BA  F0 44 0F C1 BE 8C 10 00 00      lock xadd dword ptr [rsi + 0x108c], r15d
008659C3  41 83 E7 7F                     and r15d, 0x7f
008659C7  42 C7 84 BE 90 10 00 00 10 00 00 00  mov dword ptr [rsi + r15*4 + 0x1090], 0x10
008659D3  48 8B 7B 58                     mov rdi, qword ptr [rbx + 0x58]
008659D7  48 85 FF                        test rdi, rdi
008659DA  74 4D                           je 0x140865a29
008659DC  0F B7 07                        movzx eax, word ptr [rdi]
008659DF  66 44 3B E8                     cmp r13w, ax
008659E3  7F 27                           jg 0x140865a0c
008659E5  66 FF C0                        inc ax
008659E8  4C 8D 7F 10                     lea r15, [rdi + 0x10]
008659EC  44 0F B7 E0                     movzx r12d, ax
008659F0  49 8B 0F                        mov rcx, qword ptr [r15]
008659F3  48 85 C9                        test rcx, rcx
008659F6  74 05                           je 0x1408659fd
008659F8  E8 13 B9 FE FF                  call 0x140851310
008659FD  49 83 C7 18                     add r15, 0x18
00865A01  49 83 EC 01                     sub r12, 1
00865A05  75 E9                           jne 0x1408659f0
00865A07  44 0F B6 65 67                  movzx r12d, byte ptr [rbp + 0x67]
00865A0C  80 7F 02 00                     cmp byte ptr [rdi + 2], 0
00865A10  48 8B CF                        mov rcx, rdi
00865A13  0F 85 09 02 00 00               jne 0x140865c22
00865A19  E8 62 03 C1 FF                  call 0x140475d80
00865A1E  33 D2                           xor edx, edx
00865A20  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00865A24  E8 77 5F BB FF                  call 0x14041b9a0
00865A29  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
00865A2C  A8 20                           test al, 0x20
00865A2E  74 2A                           je 0x140865a5a
00865A30  48 8B 7B 68                     mov rdi, qword ptr [rbx + 0x68]
00865A34  48 8D 4F 40                     lea rcx, [rdi + 0x40]
00865A38  E8 A3 94 A3 FF                  call 0x14029eee0
00865A3D  48 8B CF                        mov rcx, rdi
00865A40  E8 9B 94 A3 FF                  call 0x14029eee0
00865A45  48 8B CF                        mov rcx, rdi
00865A48  E8 33 03 C1 FF                  call 0x140475d80
00865A4D  B8 DF FF 00 00                  mov eax, 0xffdf
00865A52  4C 89 6B 68                     mov qword ptr [rbx + 0x68], r13
00865A56  66 21 43 30                     and word ptr [rbx + 0x30], ax
00865A5A  49 8B CE                        mov rcx, r14
00865A5D  E8 AE B8 FE FF                  call 0x140851310
00865A62  E8 1D 40 36 00                  call 0x140bc9a84
00865A67  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
00865A6B  48 8D 4D 97                     lea rcx, [rbp - 0x69]
00865A6F  48 3B C1                        cmp rax, rcx
00865A72  0F 85 D4 00 00 00               jne 0x140865b4c
00865A78  83 3D 09 A1 68 00 00            cmp dword ptr [rip + 0x68a109], 0
00865A7F  74 64                           je 0x140865ae5
00865A81  E8 F6 0F BF FF                  call 0x140456a7c
00865A86  85 C0                           test eax, eax
00865A88  75 5B                           jne 0x140865ae5
00865A8A  48 8D 45 A7                     lea rax, [rbp - 0x59]
00865A8E  48 39 45 A7                     cmp qword ptr [rbp - 0x59], rax
00865A92  74 51                           je 0x140865ae5
00865A94  48 8D 45 17                     lea rax, [rbp + 0x17]
00865A98  48 C7 45 E7 00 00 00 00         mov qword ptr [rbp - 0x19], 0
00865AA0  45 33 C9                        xor r9d, r9d
00865AA3  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00865AA7  48 8D 45 A7                     lea rax, [rbp - 0x59]
00865AAB  4C 89 6D 0B                     mov qword ptr [rbp + 0xb], r13
00865AAF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00865AB4  48 8D 55 DF                     lea rdx, [rbp - 0x21]
00865AB8  0F 57 C0                        xorps xmm0, xmm0
00865ABB  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00865AC0  45 33 C0                        xor r8d, r8d
00865AC3  C7 44 24 20 19 00 00 00         mov dword ptr [rsp + 0x20], 0x19
00865ACB  41 8D 49 19                     lea ecx, [r9 + 0x19]
00865ACF  44 89 6D 13                     mov dword ptr [rbp + 0x13], r13d
00865AD3  F3 0F 7F 45 FB                  movdqu xmmword ptr [rbp - 5], xmm0
00865AD8  4C 89 6D DF                     mov qword ptr [rbp - 0x21], r13
00865ADC  44 89 6D F7                     mov dword ptr [rbp - 9], r13d
00865AE0  E8 5B 04 00 00                  call 0x140865f40
00865AE5  45 84 E4                        test r12b, r12b
00865AE8  0F 85 4F 01 00 00               jne 0x140865c3d
00865AEE  48 85 F6                        test rsi, rsi
00865AF1  74 1A                           je 0x140865b0d
00865AF3  B8 FF FF FF FF                  mov eax, 0xffffffff
00865AF8  F0 0F C1 86 88 10 00 00         lock xadd dword ptr [rsi + 0x1088], eax
00865B00  83 F8 01                        cmp eax, 1
00865B03  75 08                           jne 0x140865b0d
00865B05  48 8B CE                        mov rcx, rsi
00865B08  E8 FF E9 FF FF                  call 0x14086450c
00865B0D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00865B16  E8 D5 94 9F FF                  call 0x14025eff0
00865B1B  48 8D 4D B7                     lea rcx, [rbp - 0x49]
00865B1F  E8 2C A2 BB FF                  call 0x14041fd50
00865B24  4C 8B B4 24 30 01 00 00         mov r14, qword ptr [rsp + 0x130]
00865B2C  48 8B BC 24 28 01 00 00         mov rdi, qword ptr [rsp + 0x128]
00865B34  4C 8B BC 24 38 01 00 00         mov r15, qword ptr [rsp + 0x138]
00865B3C  48 81 C4 F0 00 00 00            add rsp, 0xf0
00865B43  41 5D                           pop r13
00865B45  41 5C                           pop r12
00865B47  5E                              pop rsi
00865B48  5B                              pop rbx
00865B49  5D                              pop rbp
00865B4A  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0086560A(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34, __int64 a35, __int64 a36, __int64 a37, __int64 a38, __int64 a39)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p138;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;

    v_stack_p128 = v_rdi;
    v_stack_p130 = v_r14;
    v_stack_p138 = v_r15;
    if ((*(unsigned int *)(v_rip + 6858068)) == ((unsigned int)(v_rsi))) goto loc_00865771;
    result = CmpIsRegistryLockAcquired(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00865771;
    *(unsigned __int64 *)(v_rbp + 23) = v_rbx;
    v_stack_p30 = v_rbp - 89;
    v_stack_p28 = v_rbx;
    v_stack_p20 = 25;
    a3 = 0;
    result = CmpCallCallBacksEx(v_r13 + 14, v_rbp + 23, a3, (unsigned __int8)(v_r13 + 1));
    if ((*(unsigned int *)(v_rbx)) != 0x6B793032ULL) goto loc_00865771;
    if ((*(unsigned __int64 *)(v_rbx + 72)) == (v_rbx + 72)) goto loc_00865771;
    result = CmpFireCleanupNotifications(v_rbx, v_rbp + 23, a3, (unsigned __int8)(v_r13 + 1));
    a3 = 0;
    *(unsigned __int64 *)(v_rbp - 113) = v_rbp - 121;
    a2 = 0;
    *(unsigned __int64 *)(v_rbp - 121) = v_rbp - 121;
    result = KeAbPreAcquire(v_rip + 6890784, a2, a3, (unsigned __int8)(v_r13 + 1));
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 6890730;
        a2 = result;
        a1 = v_rip + 6890720;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned __int8)(v_r13 + 1));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_r13 + 1);
    }
    if ((*(unsigned __int64 *)(v_rbx + 72)) != (v_rbx + 72)) goto loc_0086590F;
    a1 = (*(unsigned __int64 *)(v_rip + 6890680)) & (-16);
    a2 = *(unsigned __int64 *)(v_rip + 6890680) - 16;
    if (a1 <= 16) { a2 = v_r13; }
    result = KeAbPostRelease(v_rip + 6890631, a2, a3, (unsigned __int8)(v_r13 + 1));
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, (unsigned __int8)(v_r13 + 1));
loc_0086575D:
    if ((*(unsigned __int64 *)(v_rbp - 121)) != (v_rbp - 121)) goto loc_008658E1;
    v_r12 = 0;
loc_00865771:
    result = v_rbp - 121;
    if (*(unsigned __int64 *)(v_rbx + 56) != 0) {
        a1 = (*(unsigned __int64 *)(v_rbx + 56)) & (-2);
        result = ObfDereferenceObject(a1, a2, a3, (unsigned __int8)(v_r13 + 1));
    }
    *(unsigned __int64 *)(v_rbp - 97) = v_rbp - 105;
    *(unsigned __int64 *)(v_rbp - 105) = v_rbp - 105;
    result = CmpLockRegistry(a1, a2, a3, (unsigned __int8)(v_r13 + 1));
    if (*(unsigned __int64 *)(v_rbx + 8) == 0) goto loc_00865A62;
    if ((*(unsigned __int64 *)(v_rbx + 16)) == v_rsi) goto loc_00865898;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_rbx + 8) + 48, a2, a3, (unsigned __int8)(v_r13 + 1));
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(v_rbx + 8) + 48;
        a2 = result;
        a1 = *(unsigned __int64 *)(v_rbx + 8) + 48;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned __int8)(v_r13 + 1));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_r13 + 1);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 56) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(v_rbx + 16)) == v_r13) goto loc_00865890;
    result = CmLockHive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 32), a2, a3, (unsigned __int8)(v_r13 + 1));
    result = *(unsigned __int64 *)(v_rbx + 16) + 16;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16) + 16)) != (*(unsigned __int64 *)(v_rbx + 16) + 16)) {
        result = v_rbp - 105;
        a4 = 267;
        v_stack_p30 = result;
        v_stack_p28 = v_r13;
        v_stack_p20 = (unsigned __int8)(v_r13);
        result = CmpPostNotify(*(unsigned __int64 *)(v_rbx + 16), a2, a3, a4);
    }
    result = SeReleaseSubjectContext(*(unsigned __int64 *)(v_rbx + 16) + 56, a2, a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16) + 8);
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16)) + 8) = result;
    }
    *(unsigned __int64 *)(v_rbx + 16) = v_r13;
    result = CmUnlockHive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16)), a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rbx + 16), a2, a3, a4);
loc_00865890:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_rbx + 8), a2, a3, a4);
loc_00865898:
    a4 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 48)))) & (64)) == 0) goto loc_00865983;
loc_008658A9:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r13)))) == 4) goto loc_0086596C;
    result = (v_rbx) - 1;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) + 1);
    goto loc_008658A9;
loc_008658E1:
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13)))) + 8)) != (v_rbp - 121)) goto loc_0086595E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13))))) + 8)) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13)))))) goto loc_0086595E;
    *(unsigned __int64 *)(v_rbp - 121) = *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13)))));
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13))))) + 8) = v_rbp - 121;
    result = ExFreePoolWithTag((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13)))), (unsigned int)(0x63634D43ULL), a3, a4);
    goto loc_0086575D;
loc_0086590F:
    if ((*(unsigned __int64 *)(result + 8)) != (*(unsigned __int64 *)(v_rbx + 16))) goto loc_0086595E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) != result) goto loc_0086595E;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16)) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = *(unsigned __int64 *)(v_rbx + 16);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) != (result + 16)) goto loc_0086595E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8))) != (result + 16)) goto loc_0086595E;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8)) = *(unsigned __int64 *)(result + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) = *(unsigned __int64 *)(result + 16 + 8);
    v_r12 = 0;
    if ((*(unsigned __int64 *)(result + 16 + 8)) == (*(unsigned __int64 *)(result + 16))) { v_r12 = (unsigned int)(v_r13 + 1); }
loc_0086595E:
    *(unsigned __int64 *)(3) = v_rbp - 121;
    *(unsigned __int64 *)(v_rbp - 121 + 8) = 3;
loc_0086596C:
    result = (unsigned int)(0xFFBFULL);
    if (0 != 0) {
        a1 = *(unsigned __int64 *)(v_rbx + 8);
        result = CmpUnlockKcb(a1, v_rbp - 121, *(unsigned __int64 *)(result + 16), a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 32) + 4232))) == 0) goto loc_008659A9;
loc_008659A9:
    v_r15 = v_r13 + 1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 32) + 2944)) == ((unsigned __int8)(v_r13 + 1))) {
        v_r12 = (unsigned __int8)(v_r13 + 1);
        *(unsigned __int8 *)(v_rbp + 103) = (unsigned __int8)(v_r13 + 1);
        v_r15 = (unsigned int)((v_r13 + 1) & (127));
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 32) + v_r15 * 4 + 4240) = 16;
    }
    if (*(unsigned __int64 *)(v_rbx + 88) == 0) goto loc_00865A29;
    if (((unsigned __int16)(v_r13)) > ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 88))))) goto loc_00865A0C;
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbx + 88))) + 1);
loc_008659F0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 88) + 16) != 0) {
        result = CmpDereferenceKeyControlBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 88) + 16), v_rbp - 121, *(unsigned __int64 *)(result + 16), a4);
    }
    v_r15 = (*(unsigned __int64 *)(v_rbx + 88) + 16) + (24);
    v_r12 = ((unsigned __int16)(result)) - (1);
    if (condition_is_not_equal) goto loc_008659F0;
loc_00865A0C:
    result = CmSiFreeMemory(*(unsigned __int64 *)(v_rbx + 88), v_rbp - 121, *(unsigned __int64 *)(result + 16), a4);
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_rbp - 49, a2, *(unsigned __int64 *)(result + 16), a4);
loc_00865A29:
    result = (unsigned int)(*(unsigned int *)(v_rbx + 48));
    v_rdi = *(unsigned __int64 *)(v_rbx + 88);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 48)))) & (32)) != 0) {
        v_rdi = *(unsigned __int64 *)(v_rbx + 104);
        a1 = v_rdi + 64;
        result = MmUnlockPages(a1, a2, *(unsigned __int64 *)(result + 16), a4);
        a1 = v_rdi;
        result = MmUnlockPages(a1, a2, *(unsigned __int64 *)(result + 16), a4);
        a1 = v_rdi;
        result = CmSiFreeMemory(a1, a2, *(unsigned __int64 *)(result + 16), a4);
        result = 0xFFDFULL;
        *(unsigned __int64 *)(v_rbx + 104) = v_r13;
    }
    result = CmpDereferenceKeyControlBlock(*(unsigned __int64 *)(v_rbx + 8), a2, *(unsigned __int64 *)(result + 16), a4);
loc_00865A62:
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_rbx + 8), a2, *(unsigned __int64 *)(result + 16), a4);
    if ((*(unsigned int *)(v_rip + 6856969)) == 0) goto loc_00865AE5;
    result = CmpIsRegistryLockAcquired(v_rbp - 105, a2, *(unsigned __int64 *)(result + 16), a4);
    if ((unsigned int)(result) != 0) goto loc_00865AE5;
    result = v_rbp - 89;
    if ((*(unsigned __int64 *)(v_rbp - 89)) != (v_rbp - 89)) {
        result = v_rbp + 23;
        *(unsigned __int64 *)(v_rbp - 25) = 0;
        a4 = 0;
        *(unsigned __int64 *)(v_rbp - 17) = result;
        result = v_rbp - 89;
        *(unsigned __int64 *)(v_rbp + 11) = v_r13;
        v_stack_p30 = result;
        a2 = v_rbp - 33;
        v_stack_p28 = v_r13;
        a3 = 0;
        v_stack_p20 = 25;
        a1 = a4 + 25;
        *(unsigned int *)(v_rbp + 19) = (unsigned int)(v_r13);
        *(unsigned __int64 *)(v_rbp - 5) = v_xmm0;
        *(unsigned __int64 *)(v_rbp - 33) = v_r13;
        *(unsigned int *)(v_rbp - 9) = (unsigned int)(v_r13);
        result = CmpCallCallBacksEx(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 32) == 0) goto loc_00865B0D;
    result = (unsigned int)(0xFFFFFFFFULL);
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL))) == 1) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 32);
        result = CmpDeleteHive(a1, a2, a3, a4);
    }
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    result = CmCleanupThreadInfo(v_rbp - 73, a2, a3, a4);
    v_rsp = (v_rsp) + (240);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0086560A(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, uint64_t Arg33, uint64_t Arg34, uint64_t Arg35, uint64_t Arg36, int64_t Arg37, int64_t Arg38, int64_t Arg39)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p128;
    uint64_t v_stack_p130;
    uint64_t v_stack_p138;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;

    v_stack_p128 = local_rdi;
    v_stack_p130 = local_r14;
    v_stack_p138 = local_r15;
    if ((*(uint32_t *)(v_rip + 0x68A554)) == ((uint32_t)(local_rsi))) goto loc_00865771;
    result = CmpIsRegistryLockAcquired(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00865771;
    *(uint64_t *)(local_rbp + 0x17) = local_rbx;
    v_stack_p30 = local_rbp - 89;
    v_stack_p28 = local_rbx;
    v_stack_p20 = 25;
    Arg3 = 0;
    result = CmpCallCallBacksEx(local_r13 + 14, local_rbp + 23, Arg3, (uint8_t)(local_r13 + 1));
    if ((*(uint32_t *)(local_rbx)) != 0x6B793032ULL) goto loc_00865771;
    if ((*(uint64_t *)(local_rbx + 0x48)) == (local_rbx + 72)) goto loc_00865771;
    result = CmpFireCleanupNotifications(local_rbx, local_rbp + 23, Arg3, (uint8_t)(local_r13 + 1));
    Arg3 = 0;
    *(uint64_t *)(local_rbp - 0x71) = local_rbp - 121;
    Arg2 = 0;
    *(uint64_t *)(local_rbp - 0x79) = local_rbp - 121;
    result = KeAbPreAcquire(v_rip + 6890784, Arg2, Arg3, (uint8_t)(local_r13 + 1));
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 6890730;
        Arg2 = result;
        Arg1 = v_rip + 6890720;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint8_t)(local_r13 + 1));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_r13 + 1);
    }
    if ((*(uint64_t *)(local_rbx + 0x48)) != (local_rbx + 72)) goto loc_0086590F;
    Arg1 = (*(uint64_t *)(v_rip + 0x6924B8)) & (-16);
    Arg2 = *(uint64_t *)(v_rip + 0x6924B8) - 16;
    if (Arg1 <= 16) { Arg2 = local_r13; }
    result = KeAbPostRelease(v_rip + 6890631, Arg2, Arg3, (uint8_t)(local_r13 + 1));
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, (uint8_t)(local_r13 + 1));
loc_0086575D:
    if ((*(uint64_t *)(local_rbp - 0x79)) != (local_rbp - 121)) goto loc_008658E1;
    local_r12 = 0;
loc_00865771:
    result = local_rbp - 121;
    if (*(uint64_t *)(local_rbx + 0x38) != 0) {
        Arg1 = (*(uint64_t *)(local_rbx + 0x38)) & (-2);
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, (uint8_t)(local_r13 + 1));
    }
    *(uint64_t *)(local_rbp - 0x61) = local_rbp - 105;
    *(uint64_t *)(local_rbp - 0x69) = local_rbp - 105;
    result = CmpLockRegistry(Arg1, Arg2, Arg3, (uint8_t)(local_r13 + 1));
    if (*(uint64_t *)(local_rbx + 0x8) == 0) goto loc_00865A62;
    if ((*(uint64_t *)(local_rbx + 0x10)) == local_rsi) goto loc_00865898;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(local_rbx + 0x8) + 48, Arg2, Arg3, (uint8_t)(local_r13 + 1));
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(local_rbx + 0x8) + 48;
        Arg2 = result;
        Arg1 = *(uint64_t *)(local_rbx + 0x8) + 48;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint8_t)(local_r13 + 1));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_r13 + 1);
    }
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x38) = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(local_rbx + 0x10)) == local_r13) goto loc_00865890;
    result = CmLockHive(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x20), Arg2, Arg3, (uint8_t)(local_r13 + 1));
    result = *(uint64_t *)(local_rbx + 0x10) + 16;
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x10)) != (*(uint64_t *)(local_rbx + 0x10) + 16)) {
        result = local_rbp - 105;
        Arg4 = 267;
        v_stack_p30 = result;
        v_stack_p28 = local_r13;
        v_stack_p20 = (uint8_t)(local_r13);
        result = CmpPostNotify(*(uint64_t *)(local_rbx + 0x10), Arg2, Arg3, Arg4);
    }
    result = SeReleaseSubjectContext(*(uint64_t *)(local_rbx + 0x10) + 56, Arg2, Arg3, Arg4);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x8)) = *(uint64_t *)(*(uint64_t *)(local_rbx + 0x10));
    result = *(uint64_t *)(*(uint64_t *)(local_rbx + 0x10));
    if (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x10)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x8);
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x10)) + 0x8) = result;
    }
    *(uint64_t *)(local_rbx + 0x10) = local_r13;
    result = CmUnlockHive(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x20), *(uint64_t *)(*(uint64_t *)(local_rbx + 0x10)), Arg3, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rbx + 0x10), Arg2, Arg3, Arg4);
loc_00865890:
    result = CmpUnlockKcb(*(uint64_t *)(local_rbx + 0x8), Arg2, Arg3, Arg4);
loc_00865898:
    Arg4 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x30)))) & (64)) == 0) goto loc_00865983;
loc_008658A9:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r13)))) == 4) goto loc_0086596C;
    result = (local_rbx) - 1;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) + 1);
    goto loc_008658A9;
loc_008658E1:
    if ((*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13)))) + 0x8)) != (local_rbp - 121)) goto loc_0086595E;
    if ((*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13))))) + 0x8)) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13)))))) goto loc_0086595E;
    *(uint64_t *)(local_rbp - 0x79) = *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13)))));
    *(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13))))) + 0x8) = local_rbp - 121;
    result = ExFreePoolWithTag((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13)))), (uint32_t)(0x63634D43ULL), Arg3, Arg4);
    goto loc_0086575D;
loc_0086590F:
    if ((*(uint64_t *)(result + 0x8)) != (*(uint64_t *)(local_rbx + 0x10))) goto loc_0086595E;
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) != result) goto loc_0086595E;
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x10)) = *(uint64_t *)(result);
    *(uint64_t *)(*(uint64_t *)(result) + 0x8) = *(uint64_t *)(local_rbx + 0x10);
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) != (result + 16)) goto loc_0086595E;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8))) != (result + 16)) goto loc_0086595E;
    *(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8)) = *(uint64_t *)(result + 0x10);
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) = *(uint64_t *)(result + 0x10 + 0x8);
    local_r12 = 0;
    if ((*(uint64_t *)(result + 0x10 + 0x8)) == (*(uint64_t *)(result + 0x10))) { local_r12 = (uint32_t)(local_r13 + 1); }
loc_0086595E:
    *(uint64_t *)(3) = local_rbp - 121;
    *(uint64_t *)(local_rbp - 0x79 + 0x8) = 3;
loc_0086596C:
    result = (uint32_t)(0xFFBFULL);
    if (0 != 0) {
        Arg1 = *(uint64_t *)(local_rbx + 0x8);
        result = CmpUnlockKcb(Arg1, local_rbp - 121, *(uint64_t *)(result + 0x10), Arg4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x20) + 0x1088))) == 0) goto loc_008659A9;
loc_008659A9:
    local_r15 = local_r13 + 1;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x20) + 0xB80)) == ((uint8_t)(local_r13 + 1))) {
        local_r12 = (uint8_t)(local_r13 + 1);
        *(uint8_t *)(local_rbp + 0x67) = (uint8_t)(local_r13 + 1);
        local_r15 = (uint32_t)((local_r13 + 1) & (127));
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x20) + local_r15 * 4 + 0x1090) = 16;
    }
    if (*(uint64_t *)(local_rbx + 0x58) == 0) goto loc_00865A29;
    if (((uint16_t)(local_r13)) > ((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbx + 0x58))))) goto loc_00865A0C;
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_rbx + 0x58))) + 1);
loc_008659F0:
    if (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x58) + 0x10) != 0) {
        result = CmpDereferenceKeyControlBlock(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x58) + 0x10), local_rbp - 121, *(uint64_t *)(result + 0x10), Arg4);
    }
    local_r15 = (*(uint64_t *)(local_rbx + 0x58) + 16) + (24);
    local_r12 = ((uint16_t)(result)) - (1);
    if (condition_is_not_equal) goto loc_008659F0;
loc_00865A0C:
    result = CmSiFreeMemory(*(uint64_t *)(local_rbx + 0x58), local_rbp - 121, *(uint64_t *)(result + 0x10), Arg4);
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(local_rbp - 49, Arg2, *(uint64_t *)(result + 0x10), Arg4);
loc_00865A29:
    result = (uint32_t)(*(uint32_t *)(local_rbx + 0x30));
    local_rdi = *(uint64_t *)(local_rbx + 0x58);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x30)))) & (32)) != 0) {
        local_rdi = *(uint64_t *)(local_rbx + 0x68);
        Arg1 = local_rdi + 64;
        result = MmUnlockPages(Arg1, Arg2, *(uint64_t *)(result + 0x10), Arg4);
        Arg1 = local_rdi;
        result = MmUnlockPages(Arg1, Arg2, *(uint64_t *)(result + 0x10), Arg4);
        Arg1 = local_rdi;
        result = CmSiFreeMemory(Arg1, Arg2, *(uint64_t *)(result + 0x10), Arg4);
        result = 0xFFDFULL;
        *(uint64_t *)(local_rbx + 0x68) = local_r13;
    }
    result = CmpDereferenceKeyControlBlock(*(uint64_t *)(local_rbx + 0x8), Arg2, *(uint64_t *)(result + 0x10), Arg4);
loc_00865A62:
    result = CmpUnlockRegistry(*(uint64_t *)(local_rbx + 0x8), Arg2, *(uint64_t *)(result + 0x10), Arg4);
    if ((*(uint32_t *)(v_rip + 0x68A109)) == 0) goto loc_00865AE5;
    result = CmpIsRegistryLockAcquired(local_rbp - 105, Arg2, *(uint64_t *)(result + 0x10), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00865AE5;
    result = local_rbp - 89;
    if ((*(uint64_t *)(local_rbp - 0x59)) != (local_rbp - 89)) {
        result = local_rbp + 23;
        *(uint64_t *)(local_rbp - 0x19) = 0;
        Arg4 = 0;
        *(uint64_t *)(local_rbp - 0x11) = result;
        result = local_rbp - 89;
        *(uint64_t *)(local_rbp + 0xB) = local_r13;
        v_stack_p30 = result;
        Arg2 = local_rbp - 33;
        v_stack_p28 = local_r13;
        Arg3 = 0;
        v_stack_p20 = 25;
        Arg1 = Arg4 + 25;
        *(uint32_t *)(local_rbp + 0x13) = (uint32_t)(local_r13);
        *(uint64_t *)(local_rbp - 0x5) = v_xmm0;
        *(uint64_t *)(local_rbp - 0x21) = local_r13;
        *(uint32_t *)(local_rbp - 0x9) = (uint32_t)(local_r13);
        result = CmpCallCallBacksEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x20) == 0) goto loc_00865B0D;
    result = (uint32_t)(0xFFFFFFFFULL);
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL))) == 1) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x20);
        result = CmpDeleteHive(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    result = CmCleanupThreadInfo(local_rbp - 73, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (240);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0086560A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
