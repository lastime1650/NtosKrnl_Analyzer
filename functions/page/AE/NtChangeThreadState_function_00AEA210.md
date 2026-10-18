# NtChangeThreadState

- RVA: `0x00AEA210`–`0x00AEA66B` (길이 `1,115` bytes)
- VA: `0x0000000140AEA210`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009F5C4`
- 디코드: `316`개 명령, `1,115/1,115` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00AEA276` → [Feature_SuspendThread2__private_IsEnabledNoReportingNoInline](../../text/5C/Feature_SuspendThread2__private_IsEnabledNoReportingNoInline_function_005C357C.md) (function, `0x005C357C`)
- `0x00AEA285` → [Feature_SuspendThread2__private_IsEnabledNoReportingNoInline](../../text/5C/Feature_SuspendThread2__private_IsEnabledNoReportingNoInline_function_005C357C.md) (function, `0x005C357C`)
- `0x00AEA2A4` → [PspProcessSuspendThreadParameters](../../text/5E/PspProcessSuspendThreadParameters_function_005E3510.md) (function, `0x005E3510`)
- `0x00AEA2D4` → [Feature_SuspendThread2__private_IsEnabledNoReportingNoInline](../../text/5C/Feature_SuspendThread2__private_IsEnabledNoReportingNoInline_function_005C357C.md) (function, `0x005C357C`)
- `0x00AEA2E2` → [Feature_SuspendThread2__private_IsEnabledNoReportingNoInline](../../text/5C/Feature_SuspendThread2__private_IsEnabledNoReportingNoInline_function_005C357C.md) (function, `0x005C357C`)
- `0x00AEA31F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AEA36A` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AEA390` → [Feature_SuspendThread2__private_IsEnabledOtherReporting](../../text/5E/Feature_SuspendThread2__private_IsEnabledOtherReporting_function_005E3430.md) (function, `0x005E3430`)
- `0x00AEA3D7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00AEA3F0` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00AEA45E` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00AEA466` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00AEA486` → [PsMultiResumeThread](../../text/20/PsMultiResumeThread_function_002027C4.md) (function, `0x002027C4`)
- `0x00AEA4AF` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00AEA4C9` → [PspSuspendThread](../78/PspSuspendThread_function_00787A0C.md) (function, `0x00787A0C`)
- `0x00AEA4EF` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00AEA508` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00AEA535` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00AEA53D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00AEA56A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00AEA583` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00AEA5B2` → [PsMultiResumeThread](../../text/20/PsMultiResumeThread_function_002027C4.md) (function, `0x002027C4`)
- `0x00AEA5D5` → [PsSuspendThread](../A1/PsSuspendThread_function_00A110D0.md) (function, `0x00A110D0`)
- `0x00AEA5F6` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00AEA5FF` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00AEA614` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00AEA62C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEA63F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEA64D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AEA227` → RVA `0x00E0A740` (`.data`; read)
- `0x00AEA303` → RVA `0x00FC7230` (`ALMOSTRO`; read)
- `0x00AEA353` → RVA `0x00FC6AC8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **25**
  - `0x00AEA276` → [Feature_SuspendThread2__private_IsEnabledNoReportingNoInline](../../text/5C/Feature_SuspendThread2__private_IsEnabledNoReportingNoInline_function_005C357C.md) (`PAGE` → `.text`)
  - `0x00AEA285` → [Feature_SuspendThread2__private_IsEnabledNoReportingNoInline](../../text/5C/Feature_SuspendThread2__private_IsEnabledNoReportingNoInline_function_005C357C.md) (`PAGE` → `.text`)
  - `0x00AEA2A4` → [PspProcessSuspendThreadParameters](../../text/5E/PspProcessSuspendThreadParameters_function_005E3510.md) (`PAGE` → `.text`)
  - `0x00AEA2D4` → [Feature_SuspendThread2__private_IsEnabledNoReportingNoInline](../../text/5C/Feature_SuspendThread2__private_IsEnabledNoReportingNoInline_function_005C357C.md) (`PAGE` → `.text`)
  - `0x00AEA2E2` → [Feature_SuspendThread2__private_IsEnabledNoReportingNoInline](../../text/5C/Feature_SuspendThread2__private_IsEnabledNoReportingNoInline_function_005C357C.md) (`PAGE` → `.text`)
  - `0x00AEA390` → [Feature_SuspendThread2__private_IsEnabledOtherReporting](../../text/5E/Feature_SuspendThread2__private_IsEnabledOtherReporting_function_005E3430.md) (`PAGE` → `.text`)
  - `0x00AEA3D7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00AEA3F0` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00AEA45E` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00AEA466` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00AEA486` → [PsMultiResumeThread](../../text/20/PsMultiResumeThread_function_002027C4.md) (`PAGE` → `.text`)
  - `0x00AEA4AF` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00AEA4EF` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00AEA508` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00AEA535` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00AEA53D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00AEA56A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00AEA583` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00AEA5B2` → [PsMultiResumeThread](../../text/20/PsMultiResumeThread_function_002027C4.md) (`PAGE` → `.text`)
  - `0x00AEA5F6` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00AEA5FF` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00AEA614` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00AEA62C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEA63F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEA64D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AEA210  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00AEA215  55                              push rbp
00AEA216  56                              push rsi
00AEA217  57                              push rdi
00AEA218  41 54                           push r12
00AEA21A  41 55                           push r13
00AEA21C  41 56                           push r14
00AEA21E  41 57                           push r15
00AEA220  48 8B EC                        mov rbp, rsp
00AEA223  48 83 EC 70                     sub rsp, 0x70
00AEA227  48 8B 05 12 05 32 00            mov rax, qword ptr [rip + 0x320512]
00AEA22E  48 33 C4                        xor rax, rsp
00AEA231  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00AEA235  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEA23E  0F 57 C0                        xorps xmm0, xmm0
00AEA241  48 83 65 E0 00                  and qword ptr [rbp - 0x20], 0
00AEA246  49 8B D9                        mov rbx, r9
00AEA249  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
00AEA24E  45 8B F0                        mov r14d, r8d
00AEA251  44 8B 65 68                     mov r12d, dword ptr [rbp + 0x68]
00AEA255  4C 8B EA                        mov r13, rdx
00AEA258  40 8A B0 32 02 00 00            mov sil, byte ptr [rax + 0x232]
00AEA25F  4C 8B F9                        mov r15, rcx
00AEA262  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00AEA266  45 85 C0                        test r8d, r8d
00AEA269  74 1A                           je 0x140aea285
00AEA26B  41 83 F8 01                     cmp r8d, 1
00AEA26F  74 44                           je 0x140aea2b5
00AEA271  BF 03 00 00 C0                  mov edi, 0xc0000003
00AEA276  E8 01 93 AD FF                  call 0x1405c357c
00AEA27B  85 C0                           test eax, eax
00AEA27D  0F 85 C1 03 00 00               jne 0x140aea644
00AEA283  EB 5D                           jmp 0x140aea2e2
00AEA285  E8 F2 92 AD FF                  call 0x1405c357c
00AEA28A  85 C0                           test eax, eax
00AEA28C  74 27                           je 0x140aea2b5
00AEA28E  44 8B 45 60                     mov r8d, dword ptr [rbp + 0x60]
00AEA292  48 8D 45 E8                     lea rax, [rbp - 0x18]
00AEA296  44 8A CE                        mov r9b, sil
00AEA299  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEA29E  48 8B D3                        mov rdx, rbx
00AEA2A1  41 8B CC                        mov ecx, r12d
00AEA2A4  E8 67 92 AF FF                  call 0x1405e3510
00AEA2A9  8B F8                           mov edi, eax
00AEA2AB  85 C0                           test eax, eax
00AEA2AD  0F 88 91 03 00 00               js 0x140aea644
00AEA2B3  EB 2D                           jmp 0x140aea2e2
00AEA2B5  83 7D 60 00                     cmp dword ptr [rbp + 0x60], 0
00AEA2B9  74 0A                           je 0x140aea2c5
00AEA2BB  BF 04 00 00 C0                  mov edi, 0xc0000004
00AEA2C0  E9 7F 03 00 00                  jmp 0x140aea644
00AEA2C5  48 85 DB                        test rbx, rbx
00AEA2C8  74 0A                           je 0x140aea2d4
00AEA2CA  BF 0D 00 00 C0                  mov edi, 0xc000000d
00AEA2CF  E9 70 03 00 00                  jmp 0x140aea644
00AEA2D4  E8 A3 92 AD FF                  call 0x1405c357c
00AEA2D9  85 C0                           test eax, eax
00AEA2DB  74 05                           je 0x140aea2e2
00AEA2DD  45 85 E4                        test r12d, r12d
00AEA2E0  75 E8                           jne 0x140aea2ca
00AEA2E2  E8 95 92 AD FF                  call 0x1405c357c
00AEA2E7  85 C0                           test eax, eax
00AEA2E9  75 05                           jne 0x140aea2f0
00AEA2EB  45 85 E4                        test r12d, r12d
00AEA2EE  75 DA                           jne 0x140aea2ca
00AEA2F0  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
00AEA2F6  48 8D 45 D8                     lea rax, [rbp - 0x28]
00AEA2FA  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00AEA300  44 8A CE                        mov r9b, sil
00AEA303  4C 8B 05 26 CF 4D 00            mov r8, qword ptr [rip + 0x4dcf26]
00AEA30A  BA 01 00 00 00                  mov edx, 1
00AEA30F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEA314  49 8B CF                        mov rcx, r15
00AEA317  C7 44 24 20 50 73 54 63         mov dword ptr [rsp + 0x20], 0x63547350
00AEA31F  E8 2C F3 D7 FF                  call 0x140869650
00AEA324  8B F8                           mov edi, eax
00AEA326  85 C0                           test eax, eax
00AEA328  0F 88 03 03 00 00               js 0x140aea631
00AEA32E  33 D2                           xor edx, edx
00AEA330  45 85 F6                        test r14d, r14d
00AEA333  74 06                           je 0x140aea33b
00AEA335  41 83 FE 01                     cmp r14d, 1
00AEA339  75 05                           jne 0x140aea340
00AEA33B  BA 02 00 00 00                  mov edx, 2
00AEA340  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
00AEA346  48 8D 45 E0                     lea rax, [rbp - 0x20]
00AEA34A  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00AEA350  44 8A CE                        mov r9b, sil
00AEA353  4C 8B 05 6E C7 4D 00            mov r8, qword ptr [rip + 0x4dc76e]
00AEA35A  49 8B CD                        mov rcx, r13
00AEA35D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEA362  C7 44 24 20 50 73 54 63         mov dword ptr [rsp + 0x20], 0x63547350
00AEA36A  E8 E1 F2 D7 FF                  call 0x140869650
00AEA36F  8B F8                           mov edi, eax
00AEA371  85 C0                           test eax, eax
00AEA373  0F 88 A2 02 00 00               js 0x140aea61b
00AEA379  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
00AEA37D  48 8B 75 E0                     mov rsi, qword ptr [rbp - 0x20]
00AEA381  48 39 30                        cmp qword ptr [rax], rsi
00AEA384  74 0A                           je 0x140aea390
00AEA386  BF 0D 00 00 C0                  mov edi, 0xc000000d
00AEA38B  E9 8F 02 00 00                  jmp 0x140aea61f
00AEA390  E8 9B 90 AF FF                  call 0x1405e3430
00AEA395  65 4C 8B 2C 25 88 01 00 00      mov r13, qword ptr gs:[0x188]
00AEA39E  48 83 CB FF                     or rbx, 0xffffffffffffffff
00AEA3A2  85 C0                           test eax, eax
00AEA3A4  0F 84 9D 01 00 00               je 0x140aea547
00AEA3AA  48 8B 75 E0                     mov rsi, qword ptr [rbp - 0x20]
00AEA3AE  8D 4B 02                        lea ecx, [rbx + 2]
00AEA3B1  49 3B F5                        cmp rsi, r13
00AEA3B4  75 05                           jne 0x140aea3bb
00AEA3B6  44 84 E1                        test cl, r12b
00AEA3B9  75 CB                           jne 0x140aea386
00AEA3BB  66 41 29 8D E4 01 00 00         sub word ptr [r13 + 0x1e4], cx
00AEA3C3  45 33 C0                        xor r8d, r8d
00AEA3C6  4C 8B 7D D8                     mov r15, qword ptr [rbp - 0x28]
00AEA3CA  33 D2                           xor edx, edx
00AEA3CC  88 4D D0                        mov byte ptr [rbp - 0x30], cl
00AEA3CF  49 83 C7 08                     add r15, 8
00AEA3D3  49 8B CF                        mov rcx, r15
00AEA3D6  90                              nop
00AEA3D7  E8 54 5E 72 FF                  call 0x140210230
00AEA3DC  F0 49 0F BA 2F 00               lock bts qword ptr [r15], 0
00AEA3E2  48 8B F0                        mov rsi, rax
00AEA3E5  73 0E                           jae 0x140aea3f5
00AEA3E7  4D 8B C7                        mov r8, r15
00AEA3EA  48 8B D0                        mov rdx, rax
00AEA3ED  49 8B CF                        mov rcx, r15
00AEA3F0  E8 9B 58 72 FF                  call 0x14020fc90
00AEA3F5  48 85 F6                        test rsi, rsi
00AEA3F8  74 04                           je 0x140aea3fe
00AEA3FA  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
00AEA3FE  45 85 F6                        test r14d, r14d
00AEA401  74 22                           je 0x140aea425
00AEA403  41 83 FE 01                     cmp r14d, 1
00AEA407  75 40                           jne 0x140aea449
00AEA409  48 8B 75 D8                     mov rsi, qword ptr [rbp - 0x28]
00AEA40D  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
00AEA410  85 C0                           test eax, eax
00AEA412  75 0A                           jne 0x140aea41e
00AEA414  BF 0D 00 00 C0                  mov edi, 0xc000000d
00AEA419  E9 C6 01 00 00                  jmp 0x140aea5e4
00AEA41E  FF C8                           dec eax
00AEA420  89 46 14                        mov dword ptr [rsi + 0x14], eax
00AEA423  EB 24                           jmp 0x140aea449
00AEA425  48 8B 75 D8                     mov rsi, qword ptr [rbp - 0x28]
00AEA429  8B 4E 14                        mov ecx, dword ptr [rsi + 0x14]
00AEA42C  8B 56 10                        mov edx, dword ptr [rsi + 0x10]
00AEA42F  03 CA                           add ecx, edx
00AEA431  81 F9 FF FF FF 7F               cmp ecx, 0x7fffffff
00AEA437  75 0A                           jne 0x140aea443
00AEA439  BF 4A 00 00 C0                  mov edi, 0xc000004a
00AEA43E  E9 A1 01 00 00                  jmp 0x140aea5e4
00AEA443  8D 42 01                        lea eax, [rdx + 1]
00AEA446  89 46 10                        mov dword ptr [rsi + 0x10], eax
00AEA449  48 83 CB FF                     or rbx, 0xffffffffffffffff
00AEA44D  48 8B C3                        mov rax, rbx
00AEA450  F0 49 0F C1 07                  lock xadd qword ptr [r15], rax
00AEA455  24 06                           and al, 6
00AEA457  3C 02                           cmp al, 2
00AEA459  75 08                           jne 0x140aea463
00AEA45B  49 8B CF                        mov rcx, r15
00AEA45E  E8 6D B9 77 FF                  call 0x140265dd0
00AEA463  49 8B CF                        mov rcx, r15
00AEA466  E8 95 71 7F FF                  call 0x1402e1600
00AEA46B  45 85 F6                        test r14d, r14d
00AEA46E  74 22                           je 0x140aea492
00AEA470  41 83 FE 01                     cmp r14d, 1
00AEA474  0F 85 93 01 00 00               jne 0x140aea60d
00AEA47A  48 8B 75 E0                     mov rsi, qword ptr [rbp - 0x20]
00AEA47E  33 D2                           xor edx, edx
00AEA480  48 8B CE                        mov rcx, rsi
00AEA483  45 8B C6                        mov r8d, r14d
00AEA486  E8 39 83 71 FF                  call 0x1402027c4
00AEA48B  8B F8                           mov edi, eax
00AEA48D  E9 7F 01 00 00                  jmp 0x140aea611
00AEA492  8B 45 E8                        mov eax, dword ptr [rbp - 0x18]
00AEA495  48 8B 75 E0                     mov rsi, qword ptr [rbp - 0x20]
00AEA499  24 02                           and al, 2
00AEA49B  F6 D8                           neg al
00AEA49D  48 8D 45 F0                     lea rax, [rbp - 0x10]
00AEA4A1  48 1B FF                        sbb rdi, rdi
00AEA4A4  48 23 F8                        and rdi, rax
00AEA4A7  49 3B F5                        cmp rsi, r13
00AEA4AA  74 0D                           je 0x140aea4b9
00AEA4AC  49 8B CD                        mov rcx, r13
00AEA4AF  E8 5C 4B 77 FF                  call 0x14025f010
00AEA4B4  45 32 F6                        xor r14b, r14b
00AEA4B7  EB 04                           jmp 0x140aea4bd
00AEA4B9  44 8A 75 D0                     mov r14b, byte ptr [rbp - 0x30]
00AEA4BD  45 33 C9                        xor r9d, r9d
00AEA4C0  4C 8B C7                        mov r8, rdi
00AEA4C3  41 8B D4                        mov edx, r12d
00AEA4C6  48 8B CE                        mov rcx, rsi
00AEA4C9  E8 3E D5 C9 FF                  call 0x140787a0c
00AEA4CE  8B F8                           mov edi, eax
00AEA4D0  41 BC 01 00 00 00               mov r12d, 1
00AEA4D6  49 3B F5                        cmp rsi, r13
00AEA4D9  74 0C                           je 0x140aea4e7
00AEA4DB  66 41 01 9D E4 01 00 00         add word ptr [r13 + 0x1e4], bx
00AEA4E3  45 8A F4                        mov r14b, r12b
00AEA4E6  90                              nop
00AEA4E7  45 33 C0                        xor r8d, r8d
00AEA4EA  33 D2                           xor edx, edx
00AEA4EC  49 8B CF                        mov rcx, r15
00AEA4EF  E8 3C 5D 72 FF                  call 0x140210230
00AEA4F4  F0 49 0F BA 2F 00               lock bts qword ptr [r15], 0
00AEA4FA  48 8B F0                        mov rsi, rax
00AEA4FD  73 0E                           jae 0x140aea50d
00AEA4FF  4D 8B C7                        mov r8, r15
00AEA502  48 8B D0                        mov rdx, rax
00AEA505  49 8B CF                        mov rcx, r15
00AEA508  E8 83 57 72 FF                  call 0x14020fc90
00AEA50D  48 85 F6                        test rsi, rsi
00AEA510  74 04                           je 0x140aea516
00AEA512  44 88 66 0A                     mov byte ptr [rsi + 0xa], r12b
00AEA516  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
00AEA51A  85 FF                           test edi, edi
00AEA51C  78 04                           js 0x140aea522
00AEA51E  44 01 60 14                     add dword ptr [rax + 0x14], r12d
00AEA522  FF 48 10                        dec dword ptr [rax + 0x10]
00AEA525  F0 49 0F C1 1F                  lock xadd qword ptr [r15], rbx
00AEA52A  80 E3 06                        and bl, 6
00AEA52D  80 FB 02                        cmp bl, 2
00AEA530  75 08                           jne 0x140aea53a
00AEA532  49 8B CF                        mov rcx, r15
00AEA535  E8 96 B8 77 FF                  call 0x140265dd0
00AEA53A  49 8B CF                        mov rcx, r15
00AEA53D  E8 BE 70 7F FF                  call 0x1402e1600
00AEA542  E9 C1 00 00 00                  jmp 0x140aea608
00AEA547  66 41 01 9D E4 01 00 00         add word ptr [r13 + 0x1e4], bx
00AEA54F  41 BC 01 00 00 00               mov r12d, 1
00AEA555  48 8B 75 D8                     mov rsi, qword ptr [rbp - 0x28]
00AEA559  45 33 C0                        xor r8d, r8d
00AEA55C  48 83 C6 08                     add rsi, 8
00AEA560  44 88 65 D0                     mov byte ptr [rbp - 0x30], r12b
00AEA564  48 8B CE                        mov rcx, rsi
00AEA567  33 D2                           xor edx, edx
00AEA569  90                              nop
00AEA56A  E8 C1 5C 72 FF                  call 0x140210230
00AEA56F  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00AEA575  4C 8B F8                        mov r15, rax
00AEA578  73 0E                           jae 0x140aea588
00AEA57A  4C 8B C6                        mov r8, rsi
00AEA57D  48 8B D0                        mov rdx, rax
00AEA580  48 8B CE                        mov rcx, rsi
00AEA583  E8 08 57 72 FF                  call 0x14020fc90
00AEA588  4D 85 FF                        test r15, r15
00AEA58B  74 04                           je 0x140aea591
00AEA58D  45 88 67 0A                     mov byte ptr [r15 + 0xa], r12b
00AEA591  48 8B 75 D8                     mov rsi, qword ptr [rbp - 0x28]
00AEA595  45 85 F6                        test r14d, r14d
00AEA598  74 28                           je 0x140aea5c2
00AEA59A  45 3B F4                        cmp r14d, r12d
00AEA59D  75 45                           jne 0x140aea5e4
00AEA59F  83 7E 14 00                     cmp dword ptr [rsi + 0x14], 0
00AEA5A3  0F 84 6B FE FF FF               je 0x140aea414
00AEA5A9  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00AEA5AD  45 8B C4                        mov r8d, r12d
00AEA5B0  33 D2                           xor edx, edx
00AEA5B2  E8 0D 82 71 FF                  call 0x1402027c4
00AEA5B7  8B F8                           mov edi, eax
00AEA5B9  85 C0                           test eax, eax
00AEA5BB  78 27                           js 0x140aea5e4
00AEA5BD  FF 4E 14                        dec dword ptr [rsi + 0x14]
00AEA5C0  EB 22                           jmp 0x140aea5e4
00AEA5C2  81 7E 14 FF FF FF 7F            cmp dword ptr [rsi + 0x14], 0x7fffffff
00AEA5C9  0F 84 6A FE FF FF               je 0x140aea439
00AEA5CF  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00AEA5D3  33 D2                           xor edx, edx
00AEA5D5  E8 F6 6A F2 FF                  call 0x140a110d0
00AEA5DA  8B F8                           mov edi, eax
00AEA5DC  85 C0                           test eax, eax
00AEA5DE  78 04                           js 0x140aea5e4
00AEA5E0  44 01 66 14                     add dword ptr [rsi + 0x14], r12d
00AEA5E4  F0 48 0F C1 5E 08               lock xadd qword ptr [rsi + 8], rbx
00AEA5EA  80 E3 06                        and bl, 6
00AEA5ED  80 FB 02                        cmp bl, 2
00AEA5F0  75 09                           jne 0x140aea5fb
00AEA5F2  48 8D 4E 08                     lea rcx, [rsi + 8]
00AEA5F6  E8 D5 B7 77 FF                  call 0x140265dd0
00AEA5FB  48 8D 4E 08                     lea rcx, [rsi + 8]
00AEA5FF  E8 FC 6F 7F FF                  call 0x1402e1600
00AEA604  44 8A 75 D0                     mov r14b, byte ptr [rbp - 0x30]
00AEA608  45 84 F6                        test r14b, r14b
00AEA60B  74 0E                           je 0x140aea61b
00AEA60D  48 8B 75 E0                     mov rsi, qword ptr [rbp - 0x20]
00AEA611  49 8B CD                        mov rcx, r13
00AEA614  E8 F7 49 77 FF                  call 0x14025f010
00AEA619  EB 04                           jmp 0x140aea61f
00AEA61B  48 8B 75 E0                     mov rsi, qword ptr [rbp - 0x20]
00AEA61F  48 85 F6                        test rsi, rsi
00AEA622  74 0D                           je 0x140aea631
00AEA624  BA 50 73 54 63                  mov edx, 0x63547350
00AEA629  48 8B CE                        mov rcx, rsi
00AEA62C  E8 AF D2 80 FF                  call 0x1402f78e0
00AEA631  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00AEA635  48 85 C9                        test rcx, rcx
00AEA638  74 0A                           je 0x140aea644
00AEA63A  BA 50 73 54 63                  mov edx, 0x63547350
00AEA63F  E8 9C D2 80 FF                  call 0x1402f78e0
00AEA644  8B C7                           mov eax, edi
00AEA646  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00AEA64A  48 33 CC                        xor rcx, rsp
00AEA64D  E8 EE 1F BC FF                  call 0x1406ac640
00AEA652  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
00AEA65A  48 83 C4 70                     add rsp, 0x70
00AEA65E  41 5F                           pop r15
00AEA660  41 5E                           pop r14
00AEA662  41 5D                           pop r13
00AEA664  41 5C                           pop r12
00AEA666  5F                              pop rdi
00AEA667  5E                              pop rsi
00AEA668  5D                              pop rbp
00AEA669  C3                              ret
00AEA66A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtChangeThreadState(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 3278098)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m50 = v_xmm0;
    if (a3 == 0) goto loc_00AEA285;
    if (a3 == 1) goto loc_00AEA2B5;
    result = Feature_SuspendThread2__private_IsEnabledNoReportingNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00AEA644;
    goto loc_00AEA2E2;
loc_00AEA285:
    result = Feature_SuspendThread2__private_IsEnabledNoReportingNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00AEA2B5;
    v_stack_m88 = v_stack_m50;
    result = PspProcessSuspendThreadParameters((unsigned int)((unsigned int)((unsigned int)(a6))), a4, (unsigned int)(a5), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00AEA644;
    goto loc_00AEA2E2;
loc_00AEA2B5:
    if (a5 == 0) goto loc_00AEA2C5;
    goto loc_00AEA644;
loc_00AEA2C5:
    if (a4 == 0) goto loc_00AEA2D4;
loc_00AEA2CA:
    goto loc_00AEA644;
loc_00AEA2D4:
    result = Feature_SuspendThread2__private_IsEnabledNoReportingNoInline((unsigned int)((unsigned int)((unsigned int)(a6))), a4, (unsigned int)(a5), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if ((unsigned int)(result) == 0) goto loc_00AEA2E2;
    if ((unsigned int)((unsigned int)(a6)) != 0) goto loc_00AEA2CA;
loc_00AEA2E2:
    result = Feature_SuspendThread2__private_IsEnabledNoReportingNoInline((unsigned int)((unsigned int)((unsigned int)(a6))), a4, (unsigned int)(a5), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if ((unsigned int)(result) != 0) goto loc_00AEA2F0;
    if ((unsigned int)((unsigned int)(a6)) != 0) goto loc_00AEA2CA;
loc_00AEA2F0:
    v_stack_m80 = v_stack_m60;
    v_stack_m88 = 0x63547350ULL;
    result = ObpReferenceObjectByHandleWithTag(a1, 1, *(unsigned __int64 *)(v_rip + 5099302), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00AEA631;
    a2 = 0;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00AEA33B;
    if (((unsigned int)((unsigned int)(a3))) == 1) {
        a2 = 2;
    }
    v_stack_m80 = v_stack_m58;
    v_stack_m88 = 0x63547350ULL;
    result = ObpReferenceObjectByHandleWithTag(a2, a2, *(unsigned __int64 *)(v_rip + 5097326), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00AEA61B;
    if ((*(unsigned __int64 *)(v_stack_m60)) == v_stack_m58) goto loc_00AEA390;
loc_00AEA386:
    goto loc_00AEA61F;
loc_00AEA390:
    result = Feature_SuspendThread2__private_IsEnabledOtherReporting(a2, a2, *(unsigned __int64 *)(v_rip + 5097326), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_rbx = (a4) | (-1);
    if ((unsigned int)(result) == 0) goto loc_00AEA547;
    if (v_stack_m58 != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00AEA3BB;
    if ((((unsigned __int8)(v_rbx + 2)) & ((unsigned __int8)((unsigned int)(a6)))) != 0) goto loc_00AEA386;
loc_00AEA3BB:
    a3 = 0;
    a2 = 0;
    v_stack_m68 = (unsigned __int8)(v_rbx + 2);
    v_r15 = (v_stack_m60) + (8);
    result = KeAbPreAcquire(v_r15, a2, a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (!(condition_is_above_or_equal)) {
        a3 = v_r15;
        a2 = result;
        a1 = v_r15;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00AEA425;
    if (((unsigned int)((unsigned int)(a3))) != 1) goto loc_00AEA449;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m60 + 20))) != 0) goto loc_00AEA41E;
loc_00AEA414:
    goto loc_00AEA5E4;
loc_00AEA41E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m60 + 20))) - 1);
    *(unsigned int *)(v_stack_m60 + 20) = (unsigned int)(result);
    goto loc_00AEA449;
loc_00AEA425:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m60 + 20))) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m60 + 16)))));
    if (((unsigned int)(a1)) != 0x7FFFFFFFULL) goto loc_00AEA443;
loc_00AEA439:
    goto loc_00AEA5E4;
loc_00AEA443:
    *(unsigned int *)(v_stack_m60 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m60 + 16)) + 1);
loc_00AEA449:
    v_rbx = (v_rbx) | (-1);
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_r15;
        result = ExfTryToWakePushLock(a1, (unsigned int)(*(unsigned int *)(v_stack_m60 + 16)), a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    result = KeAbPostRelease(v_r15, (unsigned int)(*(unsigned int *)(v_stack_m60 + 16)), a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00AEA492;
    if (((unsigned int)((unsigned int)(a3))) != 1) goto loc_00AEA60D;
    a2 = 0;
    result = PsMultiResumeThread(v_stack_m58, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    goto loc_00AEA611;
loc_00AEA492:
    result = (unsigned __int8)(((unsigned int)(v_stack_m50)) & (2));
    result = (unsigned __int8)(-(result));
    v_rdi = ((unsigned int)((unsigned int)(result))) & (v_stack_m48);
    if (v_stack_m58 == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00AEA4B9;
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_r14 = 0;
    goto loc_00AEA4BD;
loc_00AEA4B9:
loc_00AEA4BD:
    a4 = 0;
    result = PspSuspendThread(v_stack_m58, (unsigned int)((unsigned int)((unsigned int)(a6))), v_rdi, a4);
    v_r14 = v_stack_m68;
    if (v_stack_m58 != (*(unsigned __int64 *)(gs_base + (0 + 392)))) {
        v_r14 = 1;
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_r15, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_r15;
        a2 = result;
        a1 = v_r15;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (!(sign_flag)) {
    }
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    result = v_stack_m60;
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = v_r15;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_r15, a2, a3, a4);
    goto loc_00AEA608;
loc_00AEA547:
    a3 = 0;
    v_rsi = (v_stack_m60) + (8);
    v_stack_m68 = 1;
    a2 = 0;
    result = KeAbPreAcquire(v_rsi, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rsi;
        a2 = result;
        a1 = v_rsi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((unsigned int)(v_r14) == 0) goto loc_00AEA5C2;
    if (((unsigned int)(v_r14)) != 1) goto loc_00AEA5E4;
    if ((*(unsigned int *)(v_stack_m60 + 20)) == 0) goto loc_00AEA414;
    a2 = 0;
    result = PsMultiResumeThread(v_stack_m58, a2, 1, a4);
    if (sign_flag) goto loc_00AEA5E4;
    goto loc_00AEA5E4;
loc_00AEA5C2:
    if ((*(unsigned int *)(v_stack_m60 + 20)) == 0x7FFFFFFFULL) goto loc_00AEA439;
    a2 = 0;
    result = PsSuspendThread(v_stack_m58, a2, 1, a4);
    if (!(sign_flag)) {
    }
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = v_stack_m60 + 8;
        result = ExfTryToWakePushLock(a1, a2, 1, a4);
    }
    result = KeAbPostRelease(v_stack_m60 + 8, a2, 1, a4);
loc_00AEA608:
    if ((unsigned __int8)(v_stack_m68) == 0) goto loc_00AEA61B;
loc_00AEA60D:
loc_00AEA611:
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, 1, a4);
    goto loc_00AEA61F;
loc_00AEA61B:
loc_00AEA61F:
    if (v_stack_m58 != 0) {
        a2 = 0x63547350ULL;
        a1 = v_stack_m58;
        result = ObfDereferenceObjectWithTag(a1, a2, 1, a4);
    }
    if (v_stack_m60 != 0) {
        a2 = 0x63547350ULL;
        result = ObfDereferenceObjectWithTag(v_stack_m60, a2, 1, a4);
    }
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 1, a4);
    v_rsp = (v_rsp) + (112);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtChangeThreadState(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint8_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x320512)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m50 = v_xmm0;
    if (Arg3 == 0) goto loc_00AEA285;
    if (Arg3 == 1) goto loc_00AEA2B5;
    result = Feature_SuspendThread2__private_IsEnabledNoReportingNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AEA644;
    goto loc_00AEA2E2;
loc_00AEA285:
    result = Feature_SuspendThread2__private_IsEnabledNoReportingNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AEA2B5;
    v_stack_m88 = v_stack_m50;
    result = PspProcessSuspendThreadParameters((uint32_t)((uint32_t)((uint32_t)(Arg6))), Arg4, (uint32_t)(Arg5), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00AEA644;
    goto loc_00AEA2E2;
loc_00AEA2B5:
    if (Arg5 == 0) goto loc_00AEA2C5;
    goto loc_00AEA644;
loc_00AEA2C5:
    if (Arg4 == 0) goto loc_00AEA2D4;
loc_00AEA2CA:
    goto loc_00AEA644;
loc_00AEA2D4:
    result = Feature_SuspendThread2__private_IsEnabledNoReportingNoInline((uint32_t)((uint32_t)((uint32_t)(Arg6))), Arg4, (uint32_t)(Arg5), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if ((uint32_t)(result) == 0) goto loc_00AEA2E2;
    if ((uint32_t)((uint32_t)(Arg6)) != 0) goto loc_00AEA2CA;
loc_00AEA2E2:
    result = Feature_SuspendThread2__private_IsEnabledNoReportingNoInline((uint32_t)((uint32_t)((uint32_t)(Arg6))), Arg4, (uint32_t)(Arg5), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if ((uint32_t)(result) != 0) goto loc_00AEA2F0;
    if ((uint32_t)((uint32_t)(Arg6)) != 0) goto loc_00AEA2CA;
loc_00AEA2F0:
    v_stack_m80 = v_stack_m60;
    v_stack_m88 = 0x63547350ULL;
    result = ObpReferenceObjectByHandleWithTag(Arg1, 1, *(uint64_t *)(v_rip + 0x4DCF26), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00AEA631;
    Arg2 = 0;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00AEA33B;
    if (((uint32_t)((uint32_t)(Arg3))) == 1) {
        Arg2 = 2;
    }
    v_stack_m80 = v_stack_m58;
    v_stack_m88 = 0x63547350ULL;
    result = ObpReferenceObjectByHandleWithTag(Arg2, Arg2, *(uint64_t *)(v_rip + 0x4DC76E), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00AEA61B;
    if ((*(uint64_t *)(v_stack_m60)) == v_stack_m58) goto loc_00AEA390;
loc_00AEA386:
    goto loc_00AEA61F;
loc_00AEA390:
    result = Feature_SuspendThread2__private_IsEnabledOtherReporting(Arg2, Arg2, *(uint64_t *)(v_rip + 0x4DC76E), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    local_rbx = (Arg4) | (-1);
    if ((uint32_t)(result) == 0) goto loc_00AEA547;
    if (v_stack_m58 != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00AEA3BB;
    if ((((uint8_t)(local_rbx + 2)) & ((uint8_t)((uint32_t)(Arg6)))) != 0) goto loc_00AEA386;
loc_00AEA3BB:
    Arg3 = 0;
    Arg2 = 0;
    v_stack_m68 = (uint8_t)(local_rbx + 2);
    local_r15 = (v_stack_m60) + (8);
    result = KeAbPreAcquire(local_r15, Arg2, Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_r15;
        Arg2 = result;
        Arg1 = local_r15;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00AEA425;
    if (((uint32_t)((uint32_t)(Arg3))) != 1) goto loc_00AEA449;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x14))) != 0) goto loc_00AEA41E;
loc_00AEA414:
    goto loc_00AEA5E4;
loc_00AEA41E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x14))) - 1);
    *(uint32_t *)(v_stack_m60 + 0x14) = (uint32_t)(result);
    goto loc_00AEA449;
loc_00AEA425:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x14))) + ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x10)))));
    if (((uint32_t)(Arg1)) != 0x7FFFFFFFULL) goto loc_00AEA443;
loc_00AEA439:
    goto loc_00AEA5E4;
loc_00AEA443:
    *(uint32_t *)(v_stack_m60 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m60 + 0x10)) + 1);
loc_00AEA449:
    local_rbx = (local_rbx) | (-1);
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = local_r15;
        result = ExfTryToWakePushLock(Arg1, (uint32_t)(*(uint32_t *)(v_stack_m60 + 0x10)), Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    result = KeAbPostRelease(local_r15, (uint32_t)(*(uint32_t *)(v_stack_m60 + 0x10)), Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00AEA492;
    if (((uint32_t)((uint32_t)(Arg3))) != 1) goto loc_00AEA60D;
    Arg2 = 0;
    result = PsMultiResumeThread(v_stack_m58, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    goto loc_00AEA611;
loc_00AEA492:
    result = (uint8_t)(((uint32_t)(v_stack_m50)) & (2));
    result = (uint8_t)(-(result));
    local_rdi = ((uint32_t)((uint32_t)(result))) & (v_stack_m48);
    if (v_stack_m58 == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00AEA4B9;
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    local_r14 = 0;
    goto loc_00AEA4BD;
loc_00AEA4B9:
loc_00AEA4BD:
    Arg4 = 0;
    result = PspSuspendThread(v_stack_m58, (uint32_t)((uint32_t)((uint32_t)(Arg6))), local_rdi, Arg4);
    local_r14 = v_stack_m68;
    if (v_stack_m58 != (*(uint64_t *)(gs_base + (0 + 0x188)))) {
        local_r14 = 1;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_r15, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_r15;
        Arg2 = result;
        Arg1 = local_r15;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (!(sign_flag)) {
    }
    local_rbx = (uint8_t)((local_rbx) & (6));
    result = v_stack_m60;
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = local_r15;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(local_r15, Arg2, Arg3, Arg4);
    goto loc_00AEA608;
loc_00AEA547:
    Arg3 = 0;
    local_rsi = (v_stack_m60) + (8);
    v_stack_m68 = 1;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rsi, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rsi;
        Arg2 = result;
        Arg1 = local_rsi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((uint32_t)(local_r14) == 0) goto loc_00AEA5C2;
    if (((uint32_t)(local_r14)) != 1) goto loc_00AEA5E4;
    if ((*(uint32_t *)(v_stack_m60 + 0x14)) == 0) goto loc_00AEA414;
    Arg2 = 0;
    result = PsMultiResumeThread(v_stack_m58, Arg2, 1, Arg4);
    if (sign_flag) goto loc_00AEA5E4;
    goto loc_00AEA5E4;
loc_00AEA5C2:
    if ((*(uint32_t *)(v_stack_m60 + 0x14)) == 0x7FFFFFFFULL) goto loc_00AEA439;
    Arg2 = 0;
    result = PsSuspendThread(v_stack_m58, Arg2, 1, Arg4);
    if (!(sign_flag)) {
    }
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = v_stack_m60 + 8;
        result = ExfTryToWakePushLock(Arg1, Arg2, 1, Arg4);
    }
    result = KeAbPostRelease(v_stack_m60 + 8, Arg2, 1, Arg4);
loc_00AEA608:
    if ((uint8_t)(v_stack_m68) == 0) goto loc_00AEA61B;
loc_00AEA60D:
loc_00AEA611:
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, 1, Arg4);
    goto loc_00AEA61F;
loc_00AEA61B:
loc_00AEA61F:
    if (v_stack_m58 != 0) {
        Arg2 = 0x63547350ULL;
        Arg1 = v_stack_m58;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, 1, Arg4);
    }
    if (v_stack_m60 != 0) {
        Arg2 = 0x63547350ULL;
        result = ObfDereferenceObjectWithTag(v_stack_m60, Arg2, 1, Arg4);
    }
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 1, Arg4);
    local_rsp = (local_rsp) + (112);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AEA210&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
