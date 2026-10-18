# PnpDeviceActionWorker

- RVA: `0x00478400`–`0x00478AC3` (길이 `1,731` bytes)
- VA: `0x0000000140478400`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000ACE20`
- 디코드: `389`개 명령, `1,731/1,731` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **22**

### Outgoing calls
- `0x00478479` → [PpDevNodeLockTree](../../page/A1/PpDevNodeLockTree_function_00A19310.md) (function, `0x00A19310`)
- `0x0047848F` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x004784DC` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00478531` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0047854A` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0047858B` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00478590` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0047859F` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x004785AD` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x004785B9` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x004785E7` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00478650` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00478661` → [PnpLogActionQueueEvent](PnpLogActionQueueEvent_function_00478ACC.md) (function, `0x00478ACC`)
- `0x004786B1` → [PiRestartDevice](../../page/AC/PiRestartDevice_function_00ACFA1C.md) (function, `0x00ACFA1C`)
- `0x004786CD` → [PnpLogActionQueueEvent](PnpLogActionQueueEvent_function_00478ACC.md) (function, `0x00478ACC`)
- `0x004786DB` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004786EA` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x004786F8` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00478704` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0047874F` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00478780` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x0047879F` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x004787AB` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x004787FD` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x00478824` → [PnpDeleteDeviceActionRequest](../../page/95/PnpDeleteDeviceActionRequest_function_00955284.md) (function, `0x00955284`)
- `0x00478874` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004788A9` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x004788B7` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x004788C8` → [PpDevNodeUnlockTree](../../page/A2/PpDevNodeUnlockTree_function_00A21290.md) (function, `0x00A21290`)
- `0x004788D4` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00478909` → [PiProcessRequeryDeviceState](../../page/8F/PiProcessRequeryDeviceState_function_008FA054.md) (function, `0x008FA054`)
- `0x0047891E` → [ExfReleasePushLock](../26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00478944` → [PopDirectedDripsClearDisengageReason](PopDirectedDripsClearDisengageReason_function_00477EA4.md) (function, `0x00477EA4`)
- `0x0047896D` → [PpProcessClearProblem](PpProcessClearProblem_function_00478E0C.md) (function, `0x00478E0C`)
- `0x00478989` → [PnpCompleteSystemStartProcess](../5A/PnpCompleteSystemStartProcess_function_005A6F2C.md) (function, `0x005A6F2C`)
- `0x00478A00` → [PnpProcessRebalance](../5A/PnpProcessRebalance_function_005AA7C8.md) (function, `0x005AA7C8`)
- `0x00478A28` → [PiProcessResourceRequirementsChanged](../../page/72/PiProcessResourceRequirementsChanged_function_0072D504.md) (function, `0x0072D504`)
- `0x00478A47` → [PiProcessReenumeration](../../page/A5/PiProcessReenumeration_function_00A51818.md) (function, `0x00A51818`)
- `0x00478AA2` → [PiProcessClearDeviceProblem](../../page/A2/PiProcessClearDeviceProblem_function_00A271CC.md) (function, `0x00A271CC`)
- `0x00478AB9` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [PnpRequestDeviceAction](PnpRequestDeviceAction_function_00477FF8.md) at `0x004782A1`

### Static image references
- `0x00478423` → RVA `0x00E0A740` (`.data`; read)
- `0x00478468` → RVA `0x00E663B0` (`.data`; read/write)
- `0x0047847E` → RVA `0x00F8AD90` (`.data`; read)
- `0x00478494` → RVA `0x00F8AD80` (`.data`; read)
- `0x004784C4` → RVA `0x00F8AD80` (`.data`; write)
- `0x004784EA` → RVA `0x000112D0` (`.rdata`; read)
- `0x004784F7` → RVA `0x000112D8` (`.rdata`; read)
- `0x00478598` → RVA `0x00F0ED00` (`.data`; read)
- `0x004785B2` → RVA `0x00F07450` (`.data`; read)
- `0x004785CB` → RVA `0x00F074D0` (`.data`; read)
- `0x004785D2` → RVA `0x00F0745C` (`.data`; write)
- `0x004785F3` → RVA `0x00F8C5E4` (`.data`; read)
- `0x0047871F` → RVA `0x00F074E8` (`.data`; read)
- `0x00478726` → RVA `0x00F07420` (`.data`; read)
- `0x00478735` → RVA `0x00F074E8` (`.data`; write)
- `0x00478785` → RVA `0x00F0ED08` (`.data`; read/write)
- `0x004787C1` → RVA `0x00F07458` (`.data`; read/write)
- `0x004787D3` → RVA `0x00F074E0` (`.data`; read)
- `0x004787DA` → RVA `0x00F074D8` (`.data`; read/write)
- `0x004787E1` → RVA `0x00F074E0` (`.data`; write)
- `0x00478899` → RVA `0x00F8AD40` (`.data`; write)
- `0x004788A2` → RVA `0x00F8AD60` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00478479` → [PpDevNodeLockTree](../../page/A1/PpDevNodeLockTree_function_00A19310.md) (`.text` → `PAGE`)
  - `0x004786B1` → [PiRestartDevice](../../page/AC/PiRestartDevice_function_00ACFA1C.md) (`.text` → `PAGE`)
  - `0x00478824` → [PnpDeleteDeviceActionRequest](../../page/95/PnpDeleteDeviceActionRequest_function_00955284.md) (`.text` → `PAGE`)
  - `0x004788C8` → [PpDevNodeUnlockTree](../../page/A2/PpDevNodeUnlockTree_function_00A21290.md) (`.text` → `PAGE`)
  - `0x00478909` → [PiProcessRequeryDeviceState](../../page/8F/PiProcessRequeryDeviceState_function_008FA054.md) (`.text` → `PAGE`)
  - `0x00478A28` → [PiProcessResourceRequirementsChanged](../../page/72/PiProcessResourceRequirementsChanged_function_0072D504.md) (`.text` → `PAGE`)
  - `0x00478A47` → [PiProcessReenumeration](../../page/A5/PiProcessReenumeration_function_00A51818.md) (`.text` → `PAGE`)
  - `0x00478AA2` → [PiProcessClearDeviceProblem](../../page/A2/PiProcessClearDeviceProblem_function_00A271CC.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **15**
  - `0x0047897A` → [sub_006F45AA](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x00478983` → [sub_006F45AA](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x00478995` → [sub_006F45AA + 0x61](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x004789EE` → [sub_006F45AA + 0x6B](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x004789F7` → [sub_006F45AA + 0x133](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x00478A1F` → [sub_006F45AA + 0x133](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x00478A4D` → [sub_006F45AA + 0x99](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x00478A55` → [sub_006F45AA + 0x103](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x00478A5B` → [sub_006F45AA + 0x14C](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x00478A64` → [sub_006F45AA + 0xF5](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x00478A76` → [sub_006F45AA + 0x91](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x00478A7F` → [sub_006F45AA + 0xEC](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x00478A88` → [sub_006F45AA + 0xA2](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x00478A91` → [sub_006F45AA + 0x133](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)
  - `0x00478A9A` → [sub_006F45AA + 0xDD](../6F/Unknown_function_006F45AA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00478400  48 8B C4                        mov rax, rsp
00478403  48 89 58 08                     mov qword ptr [rax + 8], rbx
00478407  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0047840B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0047840F  55                              push rbp
00478410  41 54                           push r12
00478412  41 55                           push r13
00478414  41 56                           push r14
00478416  41 57                           push r15
00478418  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0047841C  48 81 EC 90 00 00 00            sub rsp, 0x90
00478423  48 8B 05 16 23 99 00            mov rax, qword ptr [rip + 0x992316]
0047842A  48 33 C4                        xor rax, rsp
0047842D  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
00478431  33 FF                           xor edi, edi
00478433  33 C0                           xor eax, eax
00478435  0F 57 C9                        xorps xmm1, xmm1
00478438  48 89 7D EF                     mov qword ptr [rbp - 0x11], rdi
0047843C  0F 11 4D F7                     movups xmmword ptr [rbp - 9], xmm1
00478440  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00478444  44 8A E7                        mov r12b, dil
00478447  0F 11 4D 07                     movups xmmword ptr [rbp + 7], xmm1
0047844B  44 89 65 EB                     mov dword ptr [rbp - 0x15], r12d
0047844F  8D 5F 01                        lea ebx, [rdi + 1]
00478452  0F 57 C0                        xorps xmm0, xmm0
00478455  40 88 7D E7                     mov byte ptr [rbp - 0x19], dil
00478459  0F 11 45 1F                     movups xmmword ptr [rbp + 0x1f], xmm0
0047845D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00478466  8B CB                           mov ecx, ebx
00478468  48 87 05 41 DF 9E 00            xchg qword ptr [rip + 0x9edf41], rax
0047846F  44 8A EF                        mov r13b, dil
00478472  40 88 7D E8                     mov byte ptr [rbp - 0x18], dil
00478476  44 8A FF                        mov r15b, dil
00478479  E8 92 0E 5A 00                  call 0x140a19310
0047847E  48 8D 0D 0B 29 B1 00            lea rcx, [rip + 0xb1290b]
00478485  40 88 7D EA                     mov byte ptr [rbp - 0x16], dil
00478489  44 8B F7                        mov r14d, edi
0047848C  88 5D E9                        mov byte ptr [rbp - 0x17], bl
0047848F  E8 DC FF D8 FF                  call 0x140208470
00478494  48 8B 35 E5 28 B1 00            mov rsi, qword ptr [rip + 0xb128e5]
0047849B  48 8D 0D DE 28 B1 00            lea rcx, [rip + 0xb128de]
004784A2  8A D8                           mov bl, al
004784A4  48 3B F1                        cmp rsi, rcx
004784A7  0F 84 CE 03 00 00               je 0x14047887b
004784AD  48 39 4E 08                     cmp qword ptr [rsi + 8], rcx
004784B1  0F 85 81 04 00 00               jne 0x140478938
004784B7  48 8B 06                        mov rax, qword ptr [rsi]
004784BA  48 39 70 08                     cmp qword ptr [rax + 8], rsi
004784BE  0F 85 74 04 00 00               jne 0x140478938
004784C4  48 89 05 B5 28 B1 00            mov qword ptr [rip + 0xb128b5], rax
004784CB  48 89 48 08                     mov qword ptr [rax + 8], rcx
004784CF  C6 46 54 01                     mov byte ptr [rsi + 0x54], 1
004784D3  8A D3                           mov dl, bl
004784D5  48 8D 0D B4 28 B1 00            lea rcx, [rip + 0xb128b4]
004784DC  E8 BF A6 F1 FF                  call 0x140392ba0
004784E1  48 85 F6                        test rsi, rsi
004784E4  0F 84 8D 04 00 00               je 0x140478977
004784EA  48 8B 0D DF 8D B9 FF            mov rcx, qword ptr [rip - 0x467221]
004784F1  48 2B 4E 40                     sub rcx, qword ptr [rsi + 0x40]
004784F5  75 0B                           jne 0x140478502
004784F7  48 8B 0D DA 8D B9 FF            mov rcx, qword ptr [rip - 0x467226]
004784FE  48 2B 4E 48                     sub rcx, qword ptr [rsi + 0x48]
00478502  41 BD 01 00 00 00               mov r13d, 1
00478508  48 85 C9                        test rcx, rcx
0047850B  0F 85 89 04 00 00               jne 0x14047899a
00478511  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0047851A  48 8D 5E 58                     lea rbx, [rsi + 0x58]
0047851E  83 C9 FF                        or ecx, 0xffffffff
00478521  45 33 C0                        xor r8d, r8d
00478524  33 D2                           xor edx, edx
00478526  66 01 88 E4 01 00 00            add word ptr [rax + 0x1e4], cx
0047852D  48 8B CB                        mov rcx, rbx
00478530  90                              nop
00478531  E8 FA 7C D9 FF                  call 0x140210230
00478536  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0047853C  4C 8B F8                        mov r15, rax
0047853F  73 0E                           jae 0x14047854f
00478541  4C 8B C3                        mov r8, rbx
00478544  48 8B D0                        mov rdx, rax
00478547  48 8B CB                        mov rcx, rbx
0047854A  E8 41 77 D9 FF                  call 0x14020fc90
0047854F  4D 85 FF                        test r15, r15
00478552  74 04                           je 0x140478558
00478554  45 88 6F 0A                     mov byte ptr [r15 + 0xa], r13b
00478558  44 8A 7E 60                     mov r15b, byte ptr [rsi + 0x60]
0047855C  0F 0D 0B                        prefetchw byte ptr [rbx]
0047855F  48 8B 03                        mov rax, qword ptr [rbx]
00478562  48 8B C8                        mov rcx, rax
00478565  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00478569  48 83 F9 10                     cmp rcx, 0x10
0047856D  48 8D 50 F0                     lea rdx, [rax - 0x10]
00478571  48 0F 46 D7                     cmovbe rdx, rdi
00478575  A8 02                           test al, 2
00478577  0F 85 9E 03 00 00               jne 0x14047891b
0047857D  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
00478582  0F 85 93 03 00 00               jne 0x14047891b
00478588  48 8B CB                        mov rcx, rbx
0047858B  E8 70 90 E6 FF                  call 0x1402e1600
00478590  E8 1B 53 DE FF                  call 0x14025d8b0
00478595  8B 5E 18                        mov ebx, dword ptr [rsi + 0x18]
00478598  48 8D 0D 61 67 A9 00            lea rcx, [rip + 0xa96761]
0047859F  E8 CC FE D8 FF                  call 0x140208470
004785A4  8A D0                           mov dl, al
004785A6  48 8D 0D 53 67 A9 00            lea rcx, [rip + 0xa96753]
004785AD  E8 EE A5 F1 FF                  call 0x140392ba0
004785B2  48 8D 0D 97 EE A8 00            lea rcx, [rip + 0xa8ee97]
004785B9  E8 B2 FE D8 FF                  call 0x140208470
004785BE  48 B9 08 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000008
004785C8  48 8B 09                        mov rcx, qword ptr [rcx]
004785CB  40 38 3D FE EE A8 00            cmp byte ptr [rip + 0xa8eefe], dil
004785D2  89 1D 84 EE A8 00               mov dword ptr [rip + 0xa8ee84], ebx
004785D8  0F 85 E2 03 00 00               jne 0x1404789c0
004785DE  8A D0                           mov dl, al
004785E0  48 8D 0D 69 EE A8 00            lea rcx, [rip + 0xa8ee69]
004785E7  E8 B4 A5 F1 FF                  call 0x140392ba0
004785EC  48 89 76 08                     mov qword ptr [rsi + 8], rsi
004785F0  48 89 36                        mov qword ptr [rsi], rsi
004785F3  39 3D EB 3F B1 00               cmp dword ptr [rip + 0xb13feb], edi
004785F9  0F 85 CD 03 00 00               jne 0x1404789cc
004785FF  45 84 FF                        test r15b, r15b
00478602  0F 85 CF 03 00 00               jne 0x1404789d7
00478608  4C 8B 46 10                     mov r8, qword ptr [rsi + 0x10]
0047860C  49 8D 88 38 01 00 00            lea rcx, [r8 + 0x138]
00478613  4D 85 C0                        test r8, r8
00478616  0F 84 14 03 00 00               je 0x140478930
0047861C  48 8B 01                        mov rax, qword ptr [rcx]
0047861F  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
00478623  81 BA 2C 01 00 00 16 03 00 00   cmp dword ptr [rdx + 0x12c], 0x316
0047862D  0F 84 C8 02 00 00               je 0x1404788fb
00478633  4D 85 C0                        test r8, r8
00478636  0F 84 D7 02 00 00               je 0x140478913
0047863C  48 8B 01                        mov rax, qword ptr [rcx]
0047863F  48 8B 58 28                     mov rbx, qword ptr [rax + 0x28]
00478643  48 85 DB                        test rbx, rbx
00478646  74 1E                           je 0x140478666
00478648  BA 50 6E 70 65                  mov edx, 0x65706e50
0047864D  49 8B C8                        mov rcx, r8
00478650  E8 BB 80 D9 FF                  call 0x140210710
00478655  8B 56 18                        mov edx, dword ptr [rsi + 0x18]
00478658  45 33 C9                        xor r9d, r9d
0047865B  45 8B C5                        mov r8d, r13d
0047865E  48 8B CB                        mov rcx, rbx
00478661  E8 66 04 00 00                  call 0x140478acc
00478666  8B 4E 18                        mov ecx, dword ptr [rsi + 0x18]
00478669  83 F9 0E                        cmp ecx, 0xe
0047866C  0F 8F E0 03 00 00               jg 0x140478a52
00478672  0F 84 CC 03 00 00               je 0x140478a44
00478678  83 F9 07                        cmp ecx, 7
0047867B  0F 8E CD 02 00 00               jle 0x14047894e
00478681  83 E9 08                        sub ecx, 8
00478684  0F 84 BA 03 00 00               je 0x140478a44
0047868A  83 E9 01                        sub ecx, 1
0047868D  0F 84 B1 03 00 00               je 0x140478a44
00478693  83 E9 01                        sub ecx, 1
00478696  0F 84 A8 03 00 00               je 0x140478a44
0047869C  83 E9 01                        sub ecx, 1
0047869F  0F 84 61 02 00 00               je 0x140478906
004786A5  83 E9 01                        sub ecx, 1
004786A8  0F 85 6E 03 00 00               jne 0x140478a1c
004786AE  48 8B CE                        mov rcx, rsi
004786B1  E8 66 73 65 00                  call 0x140acfa1c
004786B6  44 8B F0                        mov r14d, eax
004786B9  48 85 DB                        test rbx, rbx
004786BC  74 22                           je 0x1404786e0
004786BE  8B 56 18                        mov edx, dword ptr [rsi + 0x18]
004786C1  45 8B CE                        mov r9d, r14d
004786C4  41 B8 02 00 00 00               mov r8d, 2
004786CA  48 8B CB                        mov rcx, rbx
004786CD  E8 FA 03 00 00                  call 0x140478acc
004786D2  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
004786D6  BA 50 6E 70 65                  mov edx, 0x65706e50
004786DB  E8 00 F2 E7 FF                  call 0x1402f78e0
004786E0  8B 5E 18                        mov ebx, dword ptr [rsi + 0x18]
004786E3  48 8D 0D 16 66 A9 00            lea rcx, [rip + 0xa96616]
004786EA  E8 81 FD D8 FF                  call 0x140208470
004786EF  8A D0                           mov dl, al
004786F1  48 8D 0D 08 66 A9 00            lea rcx, [rip + 0xa96608]
004786F8  E8 A3 A4 F1 FF                  call 0x140392ba0
004786FD  48 8D 0D 4C ED A8 00            lea rcx, [rip + 0xa8ed4c]
00478704  E8 67 FD D8 FF                  call 0x140208470
00478709  48 B9 08 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000008
00478713  48 8B 11                        mov rdx, qword ptr [rcx]
00478716  40 38 3D B3 ED A8 00            cmp byte ptr [rip + 0xa8edb3], dil
0047871D  74 1D                           je 0x14047873c
0047871F  48 2B 15 C2 ED A8 00            sub rdx, qword ptr [rip + 0xa8edc2]
00478726  4C 8D 3D F3 EC A8 00            lea r15, [rip + 0xa8ecf3]
0047872D  49 01 94 DF D0 00 00 00         add qword ptr [r15 + rbx*8 + 0xd0], rdx
00478735  48 89 3D AC ED A8 00            mov qword ptr [rip + 0xa8edac], rdi
0047873C  8A D0                           mov dl, al
0047873E  C7 05 14 ED A8 00 1C 00 00 00   mov dword ptr [rip + 0xa8ed14], 0x1c
00478748  48 8D 0D 01 ED A8 00            lea rcx, [rip + 0xa8ed01]
0047874F  E8 4C A4 F1 FF                  call 0x140392ba0
00478754  48 8B 1E                        mov rbx, qword ptr [rsi]
00478757  48 39 73 08                     cmp qword ptr [rbx + 8], rsi
0047875B  0F 85 D7 01 00 00               jne 0x140478938
00478761  48 8B 03                        mov rax, qword ptr [rbx]
00478764  48 39 58 08                     cmp qword ptr [rax + 8], rbx
00478768  0F 85 CA 01 00 00               jne 0x140478938
0047876E  48 89 06                        mov qword ptr [rsi], rax
00478771  48 8D 0D 88 65 A9 00            lea rcx, [rip + 0xa96588]
00478778  48 89 70 08                     mov qword ptr [rax + 8], rsi
0047877C  44 8B 63 18                     mov r12d, dword ptr [rbx + 0x18]
00478780  E8 EB FC D8 FF                  call 0x140208470
00478785  83 05 7C 65 A9 00 FF            add dword ptr [rip + 0xa9657c], -1
0047878C  44 8A F8                        mov r15b, al
0047878F  0F 84 AA 01 00 00               je 0x14047893f
00478795  41 8A D7                        mov dl, r15b
00478798  48 8D 0D 61 65 A9 00            lea rcx, [rip + 0xa96561]
0047879F  E8 FC A3 F1 FF                  call 0x140392ba0
004787A4  48 8D 0D A5 EC A8 00            lea rcx, [rip + 0xa8eca5]
004787AB  E8 C0 FC D8 FF                  call 0x140208470
004787B0  48 B9 08 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000008
004787BA  41 83 C8 FF                     or r8d, 0xffffffff
004787BE  48 8B 09                        mov rcx, qword ptr [rcx]
004787C1  44 01 05 90 EC A8 00            add dword ptr [rip + 0xa8ec90], r8d
004787C8  75 1E                           jne 0x1404787e8
004787CA  40 38 3D FF EC A8 00            cmp byte ptr [rip + 0xa8ecff], dil
004787D1  74 15                           je 0x1404787e8
004787D3  48 2B 0D 06 ED A8 00            sub rcx, qword ptr [rip + 0xa8ed06]
004787DA  48 01 0D F7 EC A8 00            add qword ptr [rip + 0xa8ecf7], rcx
004787E1  48 89 3D F8 EC A8 00            mov qword ptr [rip + 0xa8ecf8], rdi
004787E8  48 8D 15 31 EC A8 00            lea rdx, [rip + 0xa8ec31]
004787EF  46 01 44 A2 40                  add dword ptr [rdx + r12*4 + 0x40], r8d
004787F4  48 8D 0D 55 EC A8 00            lea rcx, [rip + 0xa8ec55]
004787FB  8A D0                           mov dl, al
004787FD  E8 9E A3 F1 FF                  call 0x140392ba0
00478802  48 8B 43 38                     mov rax, qword ptr [rbx + 0x38]
00478806  48 85 C0                        test rax, rax
00478809  0F 85 9D 02 00 00               jne 0x140478aac
0047880F  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00478813  48 85 C9                        test rcx, rcx
00478816  0F 85 98 02 00 00               jne 0x140478ab4
0047881C  48 3B DE                        cmp rbx, rsi
0047881F  74 41                           je 0x140478862
00478821  48 8B CB                        mov rcx, rbx
00478824  E8 5B CA 4D 00                  call 0x140955284
00478829  45 85 ED                        test r13d, r13d
0047882C  0F 85 22 FF FF FF               jne 0x140478754
00478832  BB 01 00 00 00                  mov ebx, 1
00478837  44 8B 65 EB                     mov r12d, dword ptr [rbp - 0x15]
0047883B  44 8A 6D E7                     mov r13b, byte ptr [rbp - 0x19]
0047883F  44 8A 7D E8                     mov r15b, byte ptr [rbp - 0x18]
00478843  40 38 7D EA                     cmp byte ptr [rbp - 0x16], dil
00478847  0F 84 31 FC FF FF               je 0x14047847e
0047884D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00478856  48 89 B8 30 06 00 00            mov qword ptr [rax + 0x630], rdi
0047885D  E9 1C FC FF FF                  jmp 0x14047847e
00478862  44 8B EF                        mov r13d, edi
00478865  40 38 7D E9                     cmp byte ptr [rbp - 0x17], dil
00478869  74 B6                           je 0x140478821
0047886B  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0047886F  BA 44 66 6C 74                  mov edx, 0x746c6644
00478874  E8 67 F0 E7 FF                  call 0x1402f78e0
00478879  EB A6                           jmp 0x140478821
0047887B  45 84 E4                        test r12b, r12b
0047887E  0F 85 A4 00 00 00               jne 0x140478928
00478884  45 84 ED                        test r13b, r13b
00478887  0F 85 9B 00 00 00               jne 0x140478928
0047888D  45 84 FF                        test r15b, r15b
00478890  0F 85 92 00 00 00               jne 0x140478928
00478896  45 33 C0                        xor r8d, r8d
00478899  40 88 3D A0 24 B1 00            mov byte ptr [rip + 0xb124a0], dil
004788A0  33 D2                           xor edx, edx
004788A2  48 8D 0D B7 24 B1 00            lea rcx, [rip + 0xb124b7]
004788A9  E8 62 6A EC FF                  call 0x14033f310
004788AE  8A D3                           mov dl, bl
004788B0  48 8D 0D D9 24 B1 00            lea rcx, [rip + 0xb124d9]
004788B7  E8 E4 A2 F1 FF                  call 0x140392ba0
004788BC  48 87 3D ED DA 9E 00            xchg qword ptr [rip + 0x9edaed], rdi
004788C3  B9 01 00 00 00                  mov ecx, 1
004788C8  E8 C3 89 5A 00                  call 0x140a21290
004788CD  48 8B 4D 2F                     mov rcx, qword ptr [rbp + 0x2f]
004788D1  48 33 CC                        xor rcx, rsp
004788D4  E8 67 3D 23 00                  call 0x1406ac640
004788D9  4C 8D 9C 24 90 00 00 00         lea r11, [rsp + 0x90]
004788E1  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
004788E5  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
004788E9  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
004788ED  49 8B E3                        mov rsp, r11
004788F0  41 5F                           pop r15
004788F2  41 5E                           pop r14
004788F4  41 5D                           pop r13
004788F6  41 5C                           pop r12
004788F8  5D                              pop rbp
004788F9  C3                              ret
004788FA  CC                              int3
004788FB  41 BE 01 00 00 C0               mov r14d, 0xc0000001
00478901  E9 DA FD FF FF                  jmp 0x1404786e0
00478906  48 8B CE                        mov rcx, rsi
00478909  E8 46 17 48 00                  call 0x1408fa054
0047890E  E9 A3 FD FF FF                  jmp 0x1404786b6
00478913  48 8B DF                        mov rbx, rdi
00478916  E9 4B FD FF FF                  jmp 0x140478666
0047891B  48 8B CB                        mov rcx, rbx
0047891E  E8 AD AF DE FF                  call 0x1402638d0
00478923  E9 60 FC FF FF                  jmp 0x140478588
00478928  48 8B F7                        mov rsi, rdi
0047892B  E9 A3 FB FF FF                  jmp 0x1404784d3
00478930  48 8B D7                        mov rdx, rdi
00478933  E9 EB FC FF FF                  jmp 0x140478623
00478938  B9 03 00 00 00                  mov ecx, 3
0047893D  CD 29                           int 0x29
0047893F  B9 04 00 00 00                  mov ecx, 4
00478944  E8 5B F5 FF FF                  call 0x140477ea4
00478949  E9 47 FE FF FF                  jmp 0x140478795
0047894E  0F 84 BF 00 00 00               je 0x140478a13
00478954  85 C9                           test ecx, ecx
00478956  0F 84 AE 00 00 00               je 0x140478a0a
0047895C  83 E9 01                        sub ecx, 1
0047895F  0F 84 3A 01 00 00               je 0x140478a9f
00478965  83 E9 01                        sub ecx, 1
00478968  75 78                           jne 0x1404789e2
0047896A  48 8B CE                        mov rcx, rsi
0047896D  E8 9A 04 00 00                  call 0x140478e0c
00478972  E9 3F FD FF FF                  jmp 0x1404786b6
00478977  45 84 E4                        test r12b, r12b
0047897A  0F 85 2A BC 27 00               jne 0x1406f45aa
00478980  45 84 ED                        test r13b, r13b
00478983  0F 85 21 BC 27 00               jne 0x1406f45aa
00478989  E8 9E E5 12 00                  call 0x1405a6f2c
0047898E  44 8A FF                        mov r15b, dil
00478991  40 88 7D E8                     mov byte ptr [rbp - 0x18], dil
00478995  E9 71 BC 27 00                  jmp 0x1406f460b
0047899A  0F 10 46 40                     movups xmm0, xmmword ptr [rsi + 0x40]
0047899E  48 8D 4D 1F                     lea rcx, [rbp + 0x1f]
004789A2  44 88 6D EA                     mov byte ptr [rbp - 0x16], r13b
004789A6  F3 0F 7F 45 1F                  movdqu xmmword ptr [rbp + 0x1f], xmm0
004789AB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004789B4  48 89 88 30 06 00 00            mov qword ptr [rax + 0x630], rcx
004789BB  E9 51 FB FF FF                  jmp 0x140478511
004789C0  48 89 0D 21 EB A8 00            mov qword ptr [rip + 0xa8eb21], rcx
004789C7  E9 12 FC FF FF                  jmp 0x1404785de
004789CC  41 BE 89 01 00 C0               mov r14d, 0xc0000189
004789D2  E9 09 FD FF FF                  jmp 0x1404786e0
004789D7  41 BE 20 01 00 C0               mov r14d, 0xc0000120
004789DD  E9 FE FC FF FF                  jmp 0x1404786e0
004789E2  83 E9 01                        sub ecx, 1
004789E5  0F 84 B4 00 00 00               je 0x140478a9f
004789EB  83 E9 02                        sub ecx, 2
004789EE  0F 84 21 BC 27 00               je 0x1406f4615
004789F4  83 F9 01                        cmp ecx, 1
004789F7  0F 85 E0 BC 27 00               jne 0x1406f46dd
004789FD  48 8B CE                        mov rcx, rsi
00478A00  E8 C3 1D 13 00                  call 0x1405aa7c8
00478A05  E9 AC FC FF FF                  jmp 0x1404786b6
00478A0A  44 88 6D EB                     mov byte ptr [rbp - 0x15], r13b
00478A0E  E9 A6 FC FF FF                  jmp 0x1404786b9
00478A13  44 88 6D E7                     mov byte ptr [rbp - 0x19], r13b
00478A17  E9 9D FC FF FF                  jmp 0x1404786b9
00478A1C  83 F9 01                        cmp ecx, 1
00478A1F  0F 85 B8 BC 27 00               jne 0x1406f46dd
00478A25  48 8B CE                        mov rcx, rsi
00478A28  E8 D7 4A 2B 00                  call 0x14072d504
00478A2D  85 C0                           test eax, eax
00478A2F  45 0F B6 E4                     movzx r12d, r12b
00478A33  45 0F 48 E5                     cmovs r12d, r13d
00478A37  44 0F 49 F0                     cmovns r14d, eax
00478A3B  44 89 65 EB                     mov dword ptr [rbp - 0x15], r12d
00478A3F  E9 75 FC FF FF                  jmp 0x1404786b9
00478A44  48 8B CE                        mov rcx, rsi
00478A47  E8 CC 8D 5D 00                  call 0x140a51818
00478A4C  90                              nop
00478A4D  E9 F1 BB 27 00                  jmp 0x1406f4643
00478A52  83 F9 15                        cmp ecx, 0x15
00478A55  0F 8F 52 BC 27 00               jg 0x1406f46ad
00478A5B  0F 84 95 BC 27 00               je 0x1406f46f6
00478A61  83 E9 0F                        sub ecx, 0xf
00478A64  0F 84 35 BC 27 00               je 0x1406f469f
00478A6A  83 E9 01                        sub ecx, 1
00478A6D  0F 84 3B FC FF FF               je 0x1404786ae
00478A73  83 E9 01                        sub ecx, 1
00478A76  0F 84 BF BB 27 00               je 0x1406f463b
00478A7C  83 E9 01                        sub ecx, 1
00478A7F  0F 84 11 BC 27 00               je 0x1406f4696
00478A85  83 E9 01                        sub ecx, 1
00478A88  0F 84 BE BB 27 00               je 0x1406f464c
00478A8E  83 F9 01                        cmp ecx, 1
00478A91  0F 85 46 BC 27 00               jne 0x1406f46dd
00478A97  8D 51 10                        lea edx, [rcx + 0x10]
00478A9A  E9 E8 BB 27 00                  jmp 0x1406f4687
00478A9F  48 8B CE                        mov rcx, rsi
00478AA2  E8 25 E7 5A 00                  call 0x140a271cc
00478AA7  E9 0A FC FF FF                  jmp 0x1404786b6
00478AAC  44 89 30                        mov dword ptr [rax], r14d
00478AAF  E9 5B FD FF FF                  jmp 0x14047880f
00478AB4  45 33 C0                        xor r8d, r8d
00478AB7  33 D2                           xor edx, edx
00478AB9  E8 52 68 EC FF                  call 0x14033f310
00478ABE  E9 59 FD FF FF                  jmp 0x14047881c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpDeviceActionWorker(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 10035990)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 47) = result;
    v_rdi = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 17) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_xmm1;
    *(unsigned int *)(v_rsp - 95 - 21) = 0;
    *(unsigned __int8 *)(v_rsp - 95 - 25) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 31) = v_xmm0;
    *(unsigned __int8 *)(v_rsp - 95 - 24) = 0;
    result = PpDevNodeLockTree((unsigned int)((unsigned int)(v_rdi + 1)), a2, a3, a4);
loc_0047847E:
    *(unsigned __int8 *)(v_rsp - 95 - 22) = 0;
    *(unsigned __int8 *)(v_rsp - 95 - 23) = (unsigned __int8)(v_rdi + 1);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11610379, a2, a3, a4);
    if ((*(unsigned __int64 *)(v_rip + 11610341)) == (v_rip + 11610334)) goto loc_0047887B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 8)) != (v_rip + 11610334)) goto loc_00478938;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341)) + 8)) != (*(unsigned __int64 *)(v_rip + 11610341))) goto loc_00478938;
    *(unsigned __int64 *)(v_rip + 11610293) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341)) + 8) = v_rip + 11610334;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11610341) + 84) = 1;
loc_004784D3:
    result = KeReleaseSpinLock(v_rip + 11610292, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    if (*(unsigned __int64 *)(v_rip + 11610341) == 0) goto loc_00478977;
    a1 = (*(unsigned __int64 *)(v_rip - 4616737)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 64));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rip - 4616742);
        a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 72));
    }
    if (a1 != 0) goto loc_0047899A;
loc_00478511:
    a1 = (unsigned int)((a1) | (0xFFFFFFFFULL));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_rip + 11610341) + 88, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(v_rip + 11610341) + 88;
        a2 = result;
        a1 = *(unsigned __int64 *)(v_rip + 11610341) + 88;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 88)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 88) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 88))) & (2)) != 0) goto loc_0047891B;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 88))) & (2)) != 0) goto loc_0047891B;
loc_00478588:
    result = KeAbPostRelease(*(unsigned __int64 *)(v_rip + 11610341) + 88, a2, a3, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_rip + 11610341) + 88, a2, a3, a4);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11102049, a2, a3, a4);
    result = KeReleaseSpinLock(v_rip + 11102035, (unsigned __int8)(result), a3, a4);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11071127, (unsigned __int8)(result), a3, a4);
    *(unsigned int *)(v_rip + 11071108) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11610341) + 24)));
    if ((*(unsigned __int8 *)(v_rip + 11071230)) != 0) goto loc_004789C0;
loc_004785DE:
    result = KeReleaseSpinLock(v_rip + 11071081, (unsigned __int8)(result), a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 8) = *(unsigned __int64 *)(v_rip + 11610341);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341)) = *(unsigned __int64 *)(v_rip + 11610341);
    if ((*(unsigned int *)(v_rip + 11616235)) != 0) goto loc_004789CC;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11610341) + 96)) != 0) goto loc_004789D7;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 16) == 0) goto loc_00478930;
loc_00478623:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 16) + 312) + 40) + 300)) == 790) goto loc_004788FB;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 16) == 0) goto loc_00478913;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 16) + 312);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 16) + 312) + 40) != 0) {
        a2 = 0x65706E50ULL;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 16);
        result = ObfReferenceObjectWithTag(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 16), a4);
        a2 = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 11610341) + 24);
        a4 = 0;
        a3 = 1;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 16) + 312) + 40);
        result = PnpLogActionQueueEvent(a1, a2, a3, a4);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11610341) + 24)))) > 14) goto loc_00478A52;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11610341) + 24)))) == 14) goto loc_00478A44;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11610341) + 24)))) <= 7) goto loc_0047894E;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11610341) + 24))) - (8));
    if (condition_is_equal) goto loc_00478A44;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00478A44;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00478A44;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00478906;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00478A1C;
loc_004786AE:
    result = PiRestartDevice(*(unsigned __int64 *)(v_rip + 11610341), a2, a3, a4);
loc_004786B6:
loc_004786B9:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 16) + 312) + 40) != 0) {
        a2 = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 11610341) + 24);
        a4 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a3 = 2;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 16) + 312) + 40);
        result = PnpLogActionQueueEvent(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341) + 16);
        a2 = 0x65706E50ULL;
        result = ObfDereferenceObjectWithTag(a1, a2, a3, a4);
    }
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11101718, a2, a3, a4);
    result = KeReleaseSpinLock(v_rip + 11101704, (unsigned __int8)(result), a3, a4);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11070796, (unsigned __int8)(result), a3, a4);
    v_r15 = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11610341) + 96);
    if ((*(unsigned __int8 *)(v_rip + 11070899)) != 0) {
        a2 = (*(unsigned __int64 *)(v_rip + 11070796)) - (*(unsigned __int64 *)(v_rip + 11070914));
        v_r15 = v_rip + 11070707;
        *(unsigned __int64 *)(v_rip + 11070892) = 0;
    }
    *(unsigned int *)(v_rip + 11070740) = 28;
    result = KeReleaseSpinLock(v_rip + 11070721, (unsigned __int8)(result), a3, a4);
loc_00478754:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341)) + 8)) != (*(unsigned __int64 *)(v_rip + 11610341))) goto loc_00478938;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341))) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341)))) goto loc_00478938;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341))) + 8) = *(unsigned __int64 *)(v_rip + 11610341);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11101576, (unsigned __int8)(result), a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341))) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341)))) goto loc_0047893F;
loc_00478795:
    result = KeReleaseSpinLock(v_rip + 11101537, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11070629, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    if (condition_is_not_equal) goto loc_004787E8;
    if ((*(unsigned __int8 *)(v_rip + 11070719)) != 0) {
        a1 = (*(unsigned __int64 *)(v_rip + 11070629)) - (*(unsigned __int64 *)(v_rip + 11070726));
        *(unsigned __int64 *)(v_rip + 11070712) = 0;
    }
    result = KeReleaseSpinLock(v_rip + 11070549, (unsigned __int8)(result), a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341)) + 56) != 0) goto loc_00478AAC;
loc_0047880F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341)) + 48) != 0) goto loc_00478AB4;
loc_0047881C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341))) == (*(unsigned __int64 *)(v_rip + 11610341))) goto loc_00478862;
loc_00478821:
    result = PnpDeleteDeviceActionRequest(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11610341)), (unsigned __int8)(result), a3, a4);
    if (1 != 0) goto loc_00478754;
    if ((*(unsigned __int8 *)(v_rsp - 95 - 22)) == 0) goto loc_0047847E;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1584) = 0;
    goto loc_0047847E;
loc_00478862:
    if ((*(unsigned __int8 *)(v_rsp - 95 - 23)) == 0) goto loc_00478821;
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(1 + 16), (unsigned int)(0x746C6644ULL), a3, a4);
    goto loc_00478821;
loc_0047887B:
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 21))) != 0) goto loc_00478928;
    if (0 != 0) goto loc_00478928;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 95 - 24)) != 0) goto loc_00478928;
    a3 = 0;
    *(unsigned __int8 *)(v_rip + 11609248) = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 11609271, a2, a3, a4);
    result = KeReleaseSpinLock(v_rip + 11609305, 1, a3, a4);
    result = PpDevNodeUnlockTree(1, 1, a3, a4);
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 47)) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, a3, a4);
    return result;
loc_004788FB:
    goto loc_004786E0;
loc_00478906:
    result = PiProcessRequeryDeviceState(*(unsigned __int64 *)(v_stack_m28 + 56), 1, a3, a4);
    goto loc_004786B6;
loc_00478913:
    goto loc_00478666;
loc_0047891B:
    result = ExfReleasePushLock(*(unsigned __int64 *)(v_stack_m28 + 64), 1, a3, a4);
    goto loc_00478588;
loc_00478928:
    goto loc_004784D3;
loc_00478930:
    goto loc_00478623;
loc_00478938:
loc_0047893F:
    result = PopDirectedDripsClearDisengageReason(4, *(unsigned __int64 *)(v_stack_m28 + 64), a3, a4);
    goto loc_00478795;
loc_0047894E:
    if (condition_is_equal) goto loc_00478A13;
    if (4 == 0) goto loc_00478A0A;
    a1 = (unsigned int)((4) - (1));
    if (condition_is_equal) goto loc_00478A9F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_004789E2;
    result = PpProcessClearProblem(*(unsigned __int64 *)(v_stack_m28 + 64), *(unsigned __int64 *)(v_stack_m28 + 64), a3, a4);
    goto loc_004786B6;
loc_00478977:
    result = PnpCompleteSystemStartProcess(*(unsigned __int64 *)(v_stack_m28 + 64), *(unsigned __int64 *)(v_stack_m28 + 64), a3, a4);
    *(unsigned __int8 *)(v_rsp - 95 - 24) = (unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64));
loc_0047899A:
    *(unsigned __int8 *)(v_rsp - 95 - 22) = 0;
    *(unsigned __int64 *)(v_rsp - 95 + 31) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1584) = v_rsp - 95 + 31;
    goto loc_00478511;
loc_004789C0:
    *(unsigned __int64 *)(v_rip + 11070241) = v_rsp - 95 + 31;
    goto loc_004785DE;
loc_004789CC:
    goto loc_004786E0;
loc_004789D7:
    goto loc_004786E0;
loc_004789E2:
    a1 = (unsigned int)((v_rsp - 95 + 31) - (1));
    if (condition_is_equal) goto loc_00478A9F;
    a1 = (unsigned int)((a1) - (2));
    result = PnpProcessRebalance(*(unsigned __int64 *)(v_stack_m28 + 64), *(unsigned __int64 *)(v_stack_m28 + 64), a3, a4);
    goto loc_004786B6;
loc_00478A0A:
    *(unsigned __int8 *)(v_rsp - 95 - 21) = 0;
    goto loc_004786B9;
loc_00478A13:
    *(unsigned __int8 *)(v_rsp - 95 - 25) = 0;
    goto loc_004786B9;
loc_00478A1C:
    result = PiProcessResourceRequirementsChanged(*(unsigned __int64 *)(v_stack_m28 + 64), *(unsigned __int64 *)(v_stack_m28 + 64), a3, a4);
    v_r12 = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 21)));
    if (sign_flag) { v_r12 = 0; }
    v_r14 = (unsigned int)(0xC0000120ULL);
    if (!sign_flag) { v_r14 = (unsigned int)(result); }
    *(unsigned int *)(v_rsp - 95 - 21) = (unsigned int)(v_r12);
    goto loc_004786B9;
loc_00478A44:
    result = PiProcessReenumeration(*(unsigned __int64 *)(v_stack_m28 + 64), *(unsigned __int64 *)(v_stack_m28 + 64), a3, a4);
loc_00478A52:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_stack_m28 + 64)) - (15));
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_004786AE;
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (1));
loc_00478A9F:
    result = PiProcessClearDeviceProblem(*(unsigned __int64 *)(v_stack_m28 + 64), a1 + 16, a3, a4);
    goto loc_004786B6;
loc_00478AAC:
    *(unsigned int *)(result) = (unsigned int)(v_r14);
    goto loc_0047880F;
loc_00478AB4:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(v_stack_m28 + 64), a2, a3, a4);
    goto loc_0047881C;
}
```

## 5. (Beta) C Style

```c
int64_t PnpDeviceActionWorker(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x992316)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x2F) = result;
    local_rdi = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = v_xmm1;
    *(uint32_t *)(local_rsp - 0x5F - 0x15) = 0;
    *(uint8_t *)(local_rsp - 0x5F - 0x19) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0x1F) = v_xmm0;
    *(uint8_t *)(local_rsp - 0x5F - 0x18) = 0;
    result = PpDevNodeLockTree((uint32_t)((uint32_t)(local_rdi + 1)), Arg2, Arg3, Arg4);
loc_0047847E:
    *(uint8_t *)(local_rsp - 0x5F - 0x16) = 0;
    *(uint8_t *)(local_rsp - 0x5F - 0x17) = (uint8_t)(local_rdi + 1);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11610379, Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(v_rip + 0xB128E5)) == (v_rip + 11610334)) goto loc_0047887B;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x8)) != (v_rip + 11610334)) goto loc_00478938;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5)) + 0x8)) != (*(uint64_t *)(v_rip + 0xB128E5))) goto loc_00478938;
    *(uint64_t *)(v_rip + 0xB128B5) = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5)) + 0x8) = v_rip + 11610334;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x54) = 1;
loc_004784D3:
    result = KeReleaseSpinLock(v_rip + 11610292, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    if (*(uint64_t *)(v_rip + 0xB128E5) == 0) goto loc_00478977;
    Arg1 = (*(uint64_t *)(v_rip - 0x467221)) - (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x40));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(v_rip - 0x467226);
        Arg1 = (Arg1) - (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x48));
    }
    if (Arg1 != 0) goto loc_0047899A;
loc_00478511:
    Arg1 = (uint32_t)((Arg1) | (0xFFFFFFFFULL));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(v_rip + 0xB128E5) + 88, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(v_rip + 0xB128E5) + 88;
        Arg2 = result;
        Arg1 = *(uint64_t *)(v_rip + 0xB128E5) + 88;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x58)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x58) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x58))) & (2)) != 0) goto loc_0047891B;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x58))) & (2)) != 0) goto loc_0047891B;
loc_00478588:
    result = KeAbPostRelease(*(uint64_t *)(v_rip + 0xB128E5) + 88, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_rip + 0xB128E5) + 88, Arg2, Arg3, Arg4);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11102049, Arg2, Arg3, Arg4);
    result = KeReleaseSpinLock(v_rip + 11102035, (uint8_t)(result), Arg3, Arg4);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11071127, (uint8_t)(result), Arg3, Arg4);
    *(uint32_t *)(v_rip + 0xA8EE84) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x18)));
    if ((*(uint8_t *)(v_rip + 0xA8EEFE)) != 0) goto loc_004789C0;
loc_004785DE:
    result = KeReleaseSpinLock(v_rip + 11071081, (uint8_t)(result), Arg3, Arg4);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x8) = *(uint64_t *)(v_rip + 0xB128E5);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5)) = *(uint64_t *)(v_rip + 0xB128E5);
    if ((*(uint32_t *)(v_rip + 0xB13FEB)) != 0) goto loc_004789CC;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x60)) != 0) goto loc_004789D7;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x10) == 0) goto loc_00478930;
loc_00478623:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x10) + 0x138) + 0x28) + 0x12C)) == 790) goto loc_004788FB;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x10) == 0) goto loc_00478913;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x10) + 0x138);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x10) + 0x138) + 0x28) != 0) {
        Arg2 = 0x65706E50ULL;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x10);
        result = ObfReferenceObjectWithTag(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x10), Arg4);
        Arg2 = *(uint32_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x18);
        Arg4 = 0;
        Arg3 = 1;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x10) + 0x138) + 0x28);
        result = PnpLogActionQueueEvent(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x18)))) > 14) goto loc_00478A52;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x18)))) == 14) goto loc_00478A44;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x18)))) <= 7) goto loc_0047894E;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x18))) - (8));
    if (condition_is_equal) goto loc_00478A44;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00478A44;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00478A44;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00478906;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00478A1C;
loc_004786AE:
    result = PiRestartDevice(*(uint64_t *)(v_rip + 0xB128E5), Arg2, Arg3, Arg4);
loc_004786B6:
loc_004786B9:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x10) + 0x138) + 0x28) != 0) {
        Arg2 = *(uint32_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x18);
        Arg4 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg3 = 2;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x10) + 0x138) + 0x28);
        result = PnpLogActionQueueEvent(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x10);
        Arg2 = 0x65706E50ULL;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11101718, Arg2, Arg3, Arg4);
    result = KeReleaseSpinLock(v_rip + 11101704, (uint8_t)(result), Arg3, Arg4);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11070796, (uint8_t)(result), Arg3, Arg4);
    local_r15 = *(uint8_t *)(*(uint64_t *)(v_rip + 0xB128E5) + 0x60);
    if ((*(uint8_t *)(v_rip + 0xA8EDB3)) != 0) {
        Arg2 = (*(uint64_t *)(v_rip + 0xA8ED4C)) - (*(uint64_t *)(v_rip + 0xA8EDC2));
        local_r15 = v_rip + 11070707;
        *(uint64_t *)(v_rip + 0xA8EDAC) = 0;
    }
    *(uint32_t *)(v_rip + 0xA8ED14) = 28;
    result = KeReleaseSpinLock(v_rip + 11070721, (uint8_t)(result), Arg3, Arg4);
loc_00478754:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5)) + 0x8)) != (*(uint64_t *)(v_rip + 0xB128E5))) goto loc_00478938;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5))) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5)))) goto loc_00478938;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5)));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5))) + 0x8) = *(uint64_t *)(v_rip + 0xB128E5);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11101576, (uint8_t)(result), Arg3, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5))) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5)))) goto loc_0047893F;
loc_00478795:
    result = KeReleaseSpinLock(v_rip + 11101537, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11070629, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    Arg3 = (uint32_t)((Arg3) | (0xFFFFFFFFULL));
    if (condition_is_not_equal) goto loc_004787E8;
    if ((*(uint8_t *)(v_rip + 0xA8ECFF)) != 0) {
        Arg1 = (*(uint64_t *)(v_rip + 0xA8ECA5)) - (*(uint64_t *)(v_rip + 0xA8ED06));
        *(uint64_t *)(v_rip + 0xA8ECF8) = 0;
    }
    result = KeReleaseSpinLock(v_rip + 11070549, (uint8_t)(result), Arg3, Arg4);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5)) + 0x38) != 0) goto loc_00478AAC;
loc_0047880F:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5)) + 0x30) != 0) goto loc_00478AB4;
loc_0047881C:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5))) == (*(uint64_t *)(v_rip + 0xB128E5))) goto loc_00478862;
loc_00478821:
    result = PnpDeleteDeviceActionRequest(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB128E5)), (uint8_t)(result), Arg3, Arg4);
    if (1 != 0) goto loc_00478754;
    if ((*(uint8_t *)(local_rsp - 0x5F - 0x16)) == 0) goto loc_0047847E;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x630) = 0;
    goto loc_0047847E;
loc_00478862:
    if ((*(uint8_t *)(local_rsp - 0x5F - 0x17)) == 0) goto loc_00478821;
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(1 + 0x10), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    goto loc_00478821;
loc_0047887B:
    if ((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x15))) != 0) goto loc_00478928;
    if (0 != 0) goto loc_00478928;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x5F - 0x18)) != 0) goto loc_00478928;
    Arg3 = 0;
    *(uint8_t *)(v_rip + 0xB124A0) = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 11609271, Arg2, Arg3, Arg4);
    result = KeReleaseSpinLock(v_rip + 11609305, 1, Arg3, Arg4);
    result = PpDevNodeUnlockTree(1, 1, Arg3, Arg4);
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x2F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, Arg3, Arg4);
    return result;
loc_004788FB:
    goto loc_004786E0;
loc_00478906:
    result = PiProcessRequeryDeviceState(*(uint64_t *)(v_stack_m28 + 0x38), 1, Arg3, Arg4);
    goto loc_004786B6;
loc_00478913:
    goto loc_00478666;
loc_0047891B:
    result = ExfReleasePushLock(*(uint64_t *)(v_stack_m28 + 0x40), 1, Arg3, Arg4);
    goto loc_00478588;
loc_00478928:
    goto loc_004784D3;
loc_00478930:
    goto loc_00478623;
loc_00478938:
loc_0047893F:
    result = PopDirectedDripsClearDisengageReason(4, *(uint64_t *)(v_stack_m28 + 0x40), Arg3, Arg4);
    goto loc_00478795;
loc_0047894E:
    if (condition_is_equal) goto loc_00478A13;
    if (4 == 0) goto loc_00478A0A;
    Arg1 = (uint32_t)((4) - (1));
    if (condition_is_equal) goto loc_00478A9F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_004789E2;
    result = PpProcessClearProblem(*(uint64_t *)(v_stack_m28 + 0x40), *(uint64_t *)(v_stack_m28 + 0x40), Arg3, Arg4);
    goto loc_004786B6;
loc_00478977:
    result = PnpCompleteSystemStartProcess(*(uint64_t *)(v_stack_m28 + 0x40), *(uint64_t *)(v_stack_m28 + 0x40), Arg3, Arg4);
    *(uint8_t *)(local_rsp - 0x5F - 0x18) = (uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40));
loc_0047899A:
    *(uint8_t *)(local_rsp - 0x5F - 0x16) = 0;
    *(uint64_t *)(local_rsp - 0x5F + 0x1F) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x630) = local_rsp - 95 + 31;
    goto loc_00478511;
loc_004789C0:
    *(uint64_t *)(v_rip + 0xA8EB21) = local_rsp - 95 + 31;
    goto loc_004785DE;
loc_004789CC:
    goto loc_004786E0;
loc_004789D7:
    goto loc_004786E0;
loc_004789E2:
    Arg1 = (uint32_t)((local_rsp - 95 + 31) - (1));
    if (condition_is_equal) goto loc_00478A9F;
    Arg1 = (uint32_t)((Arg1) - (2));
    result = PnpProcessRebalance(*(uint64_t *)(v_stack_m28 + 0x40), *(uint64_t *)(v_stack_m28 + 0x40), Arg3, Arg4);
    goto loc_004786B6;
loc_00478A0A:
    *(uint8_t *)(local_rsp - 0x5F - 0x15) = 0;
    goto loc_004786B9;
loc_00478A13:
    *(uint8_t *)(local_rsp - 0x5F - 0x19) = 0;
    goto loc_004786B9;
loc_00478A1C:
    result = PiProcessResourceRequirementsChanged(*(uint64_t *)(v_stack_m28 + 0x40), *(uint64_t *)(v_stack_m28 + 0x40), Arg3, Arg4);
    local_r12 = (uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x15)));
    if (sign_flag) { local_r12 = 0; }
    local_r14 = (uint32_t)(0xC0000120ULL);
    if (!sign_flag) { local_r14 = (uint32_t)(result); }
    *(uint32_t *)(local_rsp - 0x5F - 0x15) = (uint32_t)(local_r12);
    goto loc_004786B9;
loc_00478A44:
    result = PiProcessReenumeration(*(uint64_t *)(v_stack_m28 + 0x40), *(uint64_t *)(v_stack_m28 + 0x40), Arg3, Arg4);
loc_00478A52:
    Arg1 = (uint32_t)((*(uint64_t *)(v_stack_m28 + 0x40)) - (15));
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_004786AE;
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (1));
loc_00478A9F:
    result = PiProcessClearDeviceProblem(*(uint64_t *)(v_stack_m28 + 0x40), Arg1 + 16, Arg3, Arg4);
    goto loc_004786B6;
loc_00478AAC:
    *(uint32_t *)(result) = (uint32_t)(local_r14);
    goto loc_0047880F;
loc_00478AB4:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(*(uint64_t *)(v_stack_m28 + 0x40), Arg2, Arg3, Arg4);
    goto loc_0047881C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00478400&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
