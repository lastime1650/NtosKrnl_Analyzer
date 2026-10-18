# KsepResolveApplicableShimsForDriver

- RVA: `0x0074A168`–`0x0074A626` (길이 `1,214` bytes)
- VA: `0x000000014074A168`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AA2A0`
- 디코드: `301`개 명령, `1,214/1,214` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x0074A1B6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0074A1CF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0074A1FF` → [KsepIsShimRegistered](../AC/KsepIsShimRegistered_function_00ACEBCC.md) (function, `0x00ACEBCC`)
- `0x0074A255` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0074A25D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0074A262` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0074A296` → [KsepLoadShimProvider](../../text/5C/KsepLoadShimProvider_function_005CBA44.md) (function, `0x005CBA44`)
- `0x0074A2EC` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x0074A303` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (function, `0x00499A98`)
- `0x0074A326` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0074A33F` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0074A371` → [KsepIsShimRegistered](../AC/KsepIsShimRegistered_function_00ACEBCC.md) (function, `0x00ACEBCC`)
- `0x0074A39D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0074A3A9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0074A3AE` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0074A400` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x0074A414` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (function, `0x00499A98`)
- `0x0074A440` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0074A448` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0074A44D` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0074A467` → [KsepGetLoadedModulesList](KsepGetLoadedModulesList_function_0074A960.md) (function, `0x0074A960`)
- `0x0074A48F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0074A4A8` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0074A4E0` → [KsepResolveShimHooks](KsepResolveShimHooks_function_00749A9C.md) (function, `0x00749A9C`)
- `0x0074A508` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0074A514` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0074A519` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0074A563` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x0074A596` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0074A59E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0074A5A3` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0074A5EE` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (function, `0x004DCFF0`)
- `0x0074A5FF` → [KsepLogInfo](../../text/49/KsepLogInfo_function_00499A68.md) (function, `0x00499A68`)
- `0x0074A609` → [KsepPoolFreePaged](../../text/4B/KsepPoolFreePaged_function_004B0E10.md) (function, `0x004B0E10`)

### Direct callers
- [KsepGetShimsForDriver](../95/KsepGetShimsForDriver_function_00958A78.md) at `0x00958B76`

### Static image references
- `0x0074A185` → RVA `0x00E66CB0` (`.data`; read)
- `0x0074A1F8` → RVA `0x00E66C80` (`.data`; read)
- `0x0074A243` → RVA `0x00E66CB0` (`.data`; read/write)
- `0x0074A2AA` → RVA `0x00F101C0` (`.data`; read/write)
- `0x0074A2B4` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0074A2D0` → RVA `0x00E66CE8` (`.data`; read)
- `0x0074A2DD` → RVA `0x00B00AE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0074A3F4` → RVA `0x00B00B20` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0074A557` → RVA `0x00B00A70` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0074A5B1` → RVA `0x00F105E0` (`.data`; read/write)
- `0x0074A5E5` → RVA `0x00B00AB0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **30**
  - `0x0074A1B6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0074A1CF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0074A255` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0074A25D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0074A262` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0074A296` → [KsepLoadShimProvider](../../text/5C/KsepLoadShimProvider_function_005CBA44.md) (`PAGE` → `.text`)
  - `0x0074A2EC` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`PAGE` → `.text`)
  - `0x0074A303` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (`PAGE` → `.text`)
  - `0x0074A326` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0074A33F` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0074A39D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0074A3A9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0074A3AE` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0074A400` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`PAGE` → `.text`)
  - `0x0074A414` → [KsepLogError](../../text/49/KsepLogError_function_00499A98.md) (`PAGE` → `.text`)
  - `0x0074A440` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0074A448` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0074A44D` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0074A48F` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0074A4A8` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0074A508` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0074A514` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0074A519` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0074A563` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`PAGE` → `.text`)
  - `0x0074A596` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0074A59E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0074A5A3` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0074A5EE` → [KsepDebugPrint](../../text/4D/KsepDebugPrint_function_004DCFF0.md) (`PAGE` → `.text`)
  - `0x0074A5FF` → [KsepLogInfo](../../text/49/KsepLogInfo_function_00499A68.md) (`PAGE` → `.text`)
  - `0x0074A609` → [KsepPoolFreePaged](../../text/4B/KsepPoolFreePaged_function_004B0E10.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0074A168  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0074A16D  55                              push rbp
0074A16E  56                              push rsi
0074A16F  57                              push rdi
0074A170  41 54                           push r12
0074A172  41 55                           push r13
0074A174  41 56                           push r14
0074A176  41 57                           push r15
0074A178  48 83 EC 20                     sub rsp, 0x20
0074A17C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0074A185  4C 8D 35 24 CB 71 00            lea r14, [rip + 0x71cb24]
0074A18C  44 8B FA                        mov r15d, edx
0074A18F  4C 8B E9                        mov r13, rcx
0074A192  48 83 CB FF                     or rbx, 0xffffffffffffffff
0074A196  33 FF                           xor edi, edi
0074A198  48 21 7C 24 78                  and qword ptr [rsp + 0x78], rdi
0074A19D  33 ED                           xor ebp, ebp
0074A19F  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
0074A1A6  45 33 C0                        xor r8d, r8d
0074A1A9  33 D2                           xor edx, edx
0074A1AB  89 6C 24 70                     mov dword ptr [rsp + 0x70], ebp
0074A1AF  49 8B CE                        mov rcx, r14
0074A1B2  90                              nop
0074A1B3  45 33 E4                        xor r12d, r12d
0074A1B6  E8 75 60 AC FF                  call 0x140210230
0074A1BB  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
0074A1C1  48 8B F0                        mov rsi, rax
0074A1C4  73 0E                           jae 0x14074a1d4
0074A1C6  4D 8B C6                        mov r8, r14
0074A1C9  48 8B D0                        mov rdx, rax
0074A1CC  49 8B CE                        mov rcx, r14
0074A1CF  E8 BC 5A AC FF                  call 0x14020fc90
0074A1D4  48 85 F6                        test rsi, rsi
0074A1D7  74 04                           je 0x14074a1dd
0074A1D9  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0074A1DD  45 85 FF                        test r15d, r15d
0074A1E0  74 5E                           je 0x14074a240
0074A1E2  49 8D 75 48                     lea rsi, [r13 + 0x48]
0074A1E6  49 8B ED                        mov rbp, r13
0074A1E9  4D 8B F7                        mov r14, r15
0074A1EC  BF 01 00 00 00                  mov edi, 1
0074A1F1  4C 8D 4D 48                     lea r9, [rbp + 0x48]
0074A1F5  48 8B D5                        mov rdx, rbp
0074A1F8  48 8D 0D 81 CA 71 00            lea rcx, [rip + 0x71ca81]
0074A1FF  E8 C8 49 38 00                  call 0x140acebcc
0074A204  3B C7                           cmp eax, edi
0074A206  75 13                           jne 0x14074a21b
0074A208  48 8B 0E                        mov rcx, qword ptr [rsi]
0074A20B  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
0074A20E  85 C0                           test eax, eax
0074A210  44 0F 44 E7                     cmove r12d, edi
0074A214  FF C0                           inc eax
0074A216  89 41 18                        mov dword ptr [rcx + 0x18], eax
0074A219  EB 0B                           jmp 0x14074a226
0074A21B  48 83 26 00                     and qword ptr [rsi], 0
0074A21F  44 8B E7                        mov r12d, edi
0074A222  89 7C 24 70                     mov dword ptr [rsp + 0x70], edi
0074A226  48 83 C5 50                     add rbp, 0x50
0074A22A  48 83 C6 50                     add rsi, 0x50
0074A22E  4C 2B F7                        sub r14, rdi
0074A231  75 BE                           jne 0x14074a1f1
0074A233  8B 6C 24 70                     mov ebp, dword ptr [rsp + 0x70]
0074A237  4C 8D 35 72 CA 71 00            lea r14, [rip + 0x71ca72]
0074A23E  33 FF                           xor edi, edi
0074A240  48 8B C3                        mov rax, rbx
0074A243  F0 48 0F C1 05 64 CA 71 00      lock xadd qword ptr [rip + 0x71ca64], rax
0074A24C  24 06                           and al, 6
0074A24E  3C 02                           cmp al, 2
0074A250  75 08                           jne 0x14074a25a
0074A252  49 8B CE                        mov rcx, r14
0074A255  E8 76 BB B1 FF                  call 0x140265dd0
0074A25A  49 8B CE                        mov rcx, r14
0074A25D  E8 9E 73 B9 FF                  call 0x1402e1600
0074A262  E8 49 36 B1 FF                  call 0x14025d8b0
0074A267  85 ED                           test ebp, ebp
0074A269  0F 84 E5 01 00 00               je 0x14074a454
0074A26F  33 ED                           xor ebp, ebp
0074A271  41 3B EF                        cmp ebp, r15d
0074A274  0F 83 93 00 00 00               jae 0x14074a30d
0074A27A  48 8D 34 AD 00 00 00 00         lea rsi, [rbp*4]
0074A282  48 03 F5                        add rsi, rbp
0074A285  48 C1 E6 04                     shl rsi, 4
0074A289  49 03 F5                        add rsi, r13
0074A28C  48 83 7E 48 00                  cmp qword ptr [rsi + 0x48], 0
0074A291  75 0E                           jne 0x14074a2a1
0074A293  48 8B CE                        mov rcx, rsi
0074A296  E8 A9 17 E8 FF                  call 0x1405cba44
0074A29B  8B F8                           mov edi, eax
0074A29D  85 C0                           test eax, eax
0074A29F  78 04                           js 0x14074a2a5
0074A2A1  FF C5                           inc ebp
0074A2A3  EB CC                           jmp 0x14074a271
0074A2A5  B8 01 00 00 00                  mov eax, 1
0074A2AA  F0 0F C1 05 0E 5F 7C 00         lock xadd dword ptr [rip + 0x7c5f0e], eax
0074A2B2  FF C0                           inc eax
0074A2B4  48 8D 0D 45 5D 8B FF            lea rcx, [rip - 0x74a2bb]
0074A2BB  83 E0 3F                        and eax, 0x3f
0074A2BE  89 BC C1 E4 01 F1 00            mov dword ptr [rcx + rax*8 + 0xf101e4], edi
0074A2C5  C7 84 C1 E0 01 F1 00 CB 01 07 00  mov dword ptr [rcx + rax*8 + 0xf101e0], 0x701cb
0074A2D0  8B 05 12 CA 71 00               mov eax, dword ptr [rip + 0x71ca12]
0074A2D6  A8 02                           test al, 2
0074A2D8  74 17                           je 0x14074a2f1
0074A2DA  44 8B 06                        mov r8d, dword ptr [rsi]
0074A2DD  48 8D 15 FC 67 3B 00            lea rdx, [rip + 0x3b67fc]
0074A2E4  44 8B CF                        mov r9d, edi
0074A2E7  B9 06 00 00 00                  mov ecx, 6
0074A2EC  E8 FF 2C D9 FF                  call 0x1404dcff0
0074A2F1  44 8B 06                        mov r8d, dword ptr [rsi]
0074A2F4  48 8D 15 E5 67 3B 00            lea rdx, [rip + 0x3b67e5]
0074A2FB  B9 06 00 00 00                  mov ecx, 6
0074A300  44 8B CF                        mov r9d, edi
0074A303  E8 90 F7 D4 FF                  call 0x140499a98
0074A308  E9 F7 02 00 00                  jmp 0x14074a604
0074A30D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0074A316  45 33 C0                        xor r8d, r8d
0074A319  33 D2                           xor edx, edx
0074A31B  49 8B CE                        mov rcx, r14
0074A31E  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
0074A325  90                              nop
0074A326  E8 05 5F AC FF                  call 0x140210230
0074A32B  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
0074A331  48 8B F0                        mov rsi, rax
0074A334  73 0E                           jae 0x14074a344
0074A336  4D 8B C6                        mov r8, r14
0074A339  48 8B D0                        mov rdx, rax
0074A33C  49 8B CE                        mov rcx, r14
0074A33F  E8 4C 59 AC FF                  call 0x14020fc90
0074A344  48 85 F6                        test rsi, rsi
0074A347  74 04                           je 0x14074a34d
0074A349  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0074A34D  33 F6                           xor esi, esi
0074A34F  41 3B F7                        cmp esi, r15d
0074A352  0F 83 C6 00 00 00               jae 0x14074a41e
0074A358  4C 8D 34 B6                     lea r14, [rsi + rsi*4]
0074A35C  49 C1 E6 04                     shl r14, 4
0074A360  48 8D 0D 19 C9 71 00            lea rcx, [rip + 0x71c919]
0074A367  4D 03 F5                        add r14, r13
0074A36A  49 8B D6                        mov rdx, r14
0074A36D  4D 8D 4E 48                     lea r9, [r14 + 0x48]
0074A371  E8 56 48 38 00                  call 0x140acebcc
0074A376  85 C0                           test eax, eax
0074A378  74 0B                           je 0x14074a385
0074A37A  49 8B 46 48                     mov rax, qword ptr [r14 + 0x48]
0074A37E  FF 40 18                        inc dword ptr [rax + 0x18]
0074A381  FF C6                           inc esi
0074A383  EB CA                           jmp 0x14074a34f
0074A385  F0 48 0F C1 1D 22 C9 71 00      lock xadd qword ptr [rip + 0x71c922], rbx
0074A38E  80 E3 06                        and bl, 6
0074A391  80 FB 02                        cmp bl, 2
0074A394  75 0C                           jne 0x14074a3a2
0074A396  48 8D 0D 13 C9 71 00            lea rcx, [rip + 0x71c913]
0074A39D  E8 2E BA B1 FF                  call 0x140265dd0
0074A3A2  48 8D 0D 07 C9 71 00            lea rcx, [rip + 0x71c907]
0074A3A9  E8 52 72 B9 FF                  call 0x1402e1600
0074A3AE  E8 FD 34 B1 FF                  call 0x14025d8b0
0074A3B3  B8 01 00 00 00                  mov eax, 1
0074A3B8  BF 12 04 00 C0                  mov edi, 0xc0000412
0074A3BD  F0 0F C1 05 FB 5D 7C 00         lock xadd dword ptr [rip + 0x7c5dfb], eax
0074A3C5  FF C0                           inc eax
0074A3C7  48 8D 0D 32 5C 8B FF            lea rcx, [rip - 0x74a3ce]
0074A3CE  83 E0 3F                        and eax, 0x3f
0074A3D1  C7 84 C1 E4 01 F1 00 12 04 00 C0  mov dword ptr [rcx + rax*8 + 0xf101e4], 0xc0000412
0074A3DC  C7 84 C1 E0 01 F1 00 E8 01 07 00  mov dword ptr [rcx + rax*8 + 0xf101e0], 0x701e8
0074A3E7  8B 05 FB C8 71 00               mov eax, dword ptr [rip + 0x71c8fb]
0074A3ED  A8 02                           test al, 2
0074A3EF  74 14                           je 0x14074a405
0074A3F1  45 8B 06                        mov r8d, dword ptr [r14]
0074A3F4  48 8D 15 25 67 3B 00            lea rdx, [rip + 0x3b6725]
0074A3FB  B9 06 00 00 00                  mov ecx, 6
0074A400  E8 EB 2B D9 FF                  call 0x1404dcff0
0074A405  45 8B 06                        mov r8d, dword ptr [r14]
0074A408  48 8D 15 11 67 3B 00            lea rdx, [rip + 0x3b6711]
0074A40F  B9 06 00 00 00                  mov ecx, 6
0074A414  E8 7F F6 D4 FF                  call 0x140499a98
0074A419  E9 E6 01 00 00                  jmp 0x14074a604
0074A41E  48 8B C3                        mov rax, rbx
0074A421  F0 48 0F C1 05 86 C8 71 00      lock xadd qword ptr [rip + 0x71c886], rax
0074A42A  BD 06 00 00 00                  mov ebp, 6
0074A42F  4C 8D 35 7A C8 71 00            lea r14, [rip + 0x71c87a]
0074A436  40 22 C5                        and al, bpl
0074A439  3C 02                           cmp al, 2
0074A43B  75 08                           jne 0x14074a445
0074A43D  49 8B CE                        mov rcx, r14
0074A440  E8 8B B9 B1 FF                  call 0x140265dd0
0074A445  49 8B CE                        mov rcx, r14
0074A448  E8 B3 71 B9 FF                  call 0x1402e1600
0074A44D  E8 5E 34 B1 FF                  call 0x14025d8b0
0074A452  EB 05                           jmp 0x14074a459
0074A454  BD 06 00 00 00                  mov ebp, 6
0074A459  45 85 E4                        test r12d, r12d
0074A45C  0F 84 46 01 00 00               je 0x14074a5a8
0074A462  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0074A467  E8 F4 04 00 00                  call 0x14074a960
0074A46C  8B F8                           mov edi, eax
0074A46E  85 C0                           test eax, eax
0074A470  0F 88 8E 01 00 00               js 0x14074a604
0074A476  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0074A47F  45 33 C0                        xor r8d, r8d
0074A482  33 D2                           xor edx, edx
0074A484  49 8B CE                        mov rcx, r14
0074A487  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
0074A48E  90                              nop
0074A48F  E8 9C 5D AC FF                  call 0x140210230
0074A494  F0 49 0F BA 2E 00               lock bts qword ptr [r14], 0
0074A49A  48 8B F0                        mov rsi, rax
0074A49D  73 0E                           jae 0x14074a4ad
0074A49F  4D 8B C6                        mov r8, r14
0074A4A2  48 8B D0                        mov rdx, rax
0074A4A5  49 8B CE                        mov rcx, r14
0074A4A8  E8 E3 57 AC FF                  call 0x14020fc90
0074A4AD  41 BC 01 00 00 00               mov r12d, 1
0074A4B3  48 85 F6                        test rsi, rsi
0074A4B6  74 04                           je 0x14074a4bc
0074A4B8  44 88 66 0A                     mov byte ptr [rsi + 0xa], r12b
0074A4BC  33 F6                           xor esi, esi
0074A4BE  41 3B F7                        cmp esi, r15d
0074A4C1  0F 83 B4 00 00 00               jae 0x14074a57b
0074A4C7  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0074A4CC  4C 8D 34 B6                     lea r14, [rsi + rsi*4]
0074A4D0  4D 03 F6                        add r14, r14
0074A4D3  4B 8B 44 F5 48                  mov rax, qword ptr [r13 + r14*8 + 0x48]
0074A4D8  48 8B 50 10                     mov rdx, qword ptr [rax + 0x10]
0074A4DC  48 8B 52 30                     mov rdx, qword ptr [rdx + 0x30]
0074A4E0  E8 B7 F5 FF FF                  call 0x140749a9c
0074A4E5  8B F8                           mov edi, eax
0074A4E7  85 C0                           test eax, eax
0074A4E9  78 05                           js 0x14074a4f0
0074A4EB  41 03 F4                        add esi, r12d
0074A4EE  EB CE                           jmp 0x14074a4be
0074A4F0  F0 48 0F C1 1D B7 C7 71 00      lock xadd qword ptr [rip + 0x71c7b7], rbx
0074A4F9  40 22 DD                        and bl, bpl
0074A4FC  80 FB 02                        cmp bl, 2
0074A4FF  75 0C                           jne 0x14074a50d
0074A501  48 8D 0D A8 C7 71 00            lea rcx, [rip + 0x71c7a8]
0074A508  E8 C3 B8 B1 FF                  call 0x140265dd0
0074A50D  48 8D 0D 9C C7 71 00            lea rcx, [rip + 0x71c79c]
0074A514  E8 E7 70 B9 FF                  call 0x1402e1600
0074A519  E8 92 33 B1 FF                  call 0x14025d8b0
0074A51E  41 8B C4                        mov eax, r12d
0074A521  F0 0F C1 05 97 5C 7C 00         lock xadd dword ptr [rip + 0x7c5c97], eax
0074A529  41 03 C4                        add eax, r12d
0074A52C  48 8D 0D CD 5A 8B FF            lea rcx, [rip - 0x74a533]
0074A533  83 E0 3F                        and eax, 0x3f
0074A536  89 BC C1 E4 01 F1 00            mov dword ptr [rcx + rax*8 + 0xf101e4], edi
0074A53D  C7 84 C1 E0 01 F1 00 18 02 07 00  mov dword ptr [rcx + rax*8 + 0xf101e0], 0x70218
0074A548  8B 05 9A C7 71 00               mov eax, dword ptr [rip + 0x71c79a]
0074A54E  A8 02                           test al, 2
0074A550  74 16                           je 0x14074a568
0074A552  47 8B 44 F5 00                  mov r8d, dword ptr [r13 + r14*8]
0074A557  48 8D 15 12 65 3B 00            lea rdx, [rip + 0x3b6512]
0074A55E  44 8B CF                        mov r9d, edi
0074A561  8B CD                           mov ecx, ebp
0074A563  E8 88 2A D9 FF                  call 0x1404dcff0
0074A568  47 8B 44 F5 00                  mov r8d, dword ptr [r13 + r14*8]
0074A56D  48 8D 15 FC 64 3B 00            lea rdx, [rip + 0x3b64fc]
0074A574  8B CD                           mov ecx, ebp
0074A576  E9 85 FD FF FF                  jmp 0x14074a300
0074A57B  F0 48 0F C1 1D 2C C7 71 00      lock xadd qword ptr [rip + 0x71c72c], rbx
0074A584  40 22 DD                        and bl, bpl
0074A587  4C 8D 35 22 C7 71 00            lea r14, [rip + 0x71c722]
0074A58E  80 FB 02                        cmp bl, 2
0074A591  75 08                           jne 0x14074a59b
0074A593  49 8B CE                        mov rcx, r14
0074A596  E8 35 B8 B1 FF                  call 0x140265dd0
0074A59B  49 8B CE                        mov rcx, r14
0074A59E  E8 5D 70 B9 FF                  call 0x1402e1600
0074A5A3  E8 08 33 B1 FF                  call 0x14025d8b0
0074A5A8  85 FF                           test edi, edi
0074A5AA  78 58                           js 0x14074a604
0074A5AC  B8 01 00 00 00                  mov eax, 1
0074A5B1  F0 0F C1 05 27 60 7C 00         lock xadd dword ptr [rip + 0x7c6027], eax
0074A5B9  FF C0                           inc eax
0074A5BB  48 8D 0D 3E 5A 8B FF            lea rcx, [rip - 0x74a5c2]
0074A5C2  83 E0 3F                        and eax, 0x3f
0074A5C5  83 A4 C1 E4 03 F1 00 00         and dword ptr [rcx + rax*8 + 0xf103e4], 0
0074A5CD  C7 84 C1 E0 03 F1 00 26 02 07 00  mov dword ptr [rcx + rax*8 + 0xf103e0], 0x70226
0074A5D8  8B 05 0A C7 71 00               mov eax, dword ptr [rip + 0x71c70a]
0074A5DE  A8 01                           test al, 1
0074A5E0  74 11                           je 0x14074a5f3
0074A5E2  45 8B C7                        mov r8d, r15d
0074A5E5  48 8D 15 C4 64 3B 00            lea rdx, [rip + 0x3b64c4]
0074A5EC  8B CD                           mov ecx, ebp
0074A5EE  E8 FD 29 D9 FF                  call 0x1404dcff0
0074A5F3  45 8B C7                        mov r8d, r15d
0074A5F6  48 8D 15 B3 64 3B 00            lea rdx, [rip + 0x3b64b3]
0074A5FD  8B CD                           mov ecx, ebp
0074A5FF  E8 64 F4 D4 FF                  call 0x140499a68
0074A604  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0074A609  E8 02 68 D6 FF                  call 0x1404b0e10
0074A60E  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0074A613  8B C7                           mov eax, edi
0074A615  48 83 C4 20                     add rsp, 0x20
0074A619  41 5F                           pop r15
0074A61B  41 5E                           pop r14
0074A61D  41 5D                           pop r13
0074A61F  41 5C                           pop r12
0074A621  5F                              pop rdi
0074A622  5E                              pop rsi
0074A623  5D                              pop rbp
0074A624  C3                              ret
0074A625  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepResolveApplicableShimsForDriver(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_rbx = (v_rbx) | (-1);
    v_rdi = 0;
    v_rbp = 0;
    a3 = 0;
    a2 = 0;
    v_stack_p18 = 0;
    v_r12 = 0;
    result = KeAbPreAcquire(v_rip + 7457572, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 7457572;
        a2 = result;
        a1 = v_rip + 7457572;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_0074A240;
loc_0074A1F1:
    result = KsepIsShimRegistered(v_rip + 7457409, a1, a3, a1 + 72);
    if (((unsigned int)(result)) != 1) goto loc_0074A21B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 24))) == 0) { v_r12 = 1; }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 24))) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 24) = (unsigned int)(result);
    goto loc_0074A226;
loc_0074A21B:
    v_stack_p18 = 1;
loc_0074A226:
    v_rbp = (a1) + (80);
    v_rsi = (a1 + 72) + (80);
    v_r14 = ((unsigned int)(a2)) - (1);
    if (condition_is_not_equal) goto loc_0074A1F1;
    v_rdi = 0;
loc_0074A240:
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_rip + 7457394;
        result = ExfTryToWakePushLock(a1, a1, a3, a1 + 72);
    }
    result = KeAbPostRelease(v_rip + 7457394, a1, a3, a1 + 72);
    result = KeLeaveCriticalRegion(v_rip + 7457394, a1, a3, a1 + 72);
    if ((unsigned int)((unsigned int)(v_stack_p18)) == 0) goto loc_0074A454;
    v_rbp = 0;
loc_0074A271:
    if (0 >= ((unsigned int)((unsigned int)(a2)))) goto loc_0074A30D;
    v_rsi = (v_rbp * 4) + (0);
    v_rsi = (v_rsi) << (4);
    v_rsi = (v_rsi) + (a1);
    if ((*(unsigned __int64 *)(v_rsi + 72)) != 0) goto loc_0074A2A1;
    result = KsepLoadShimProvider(v_rsi, a1, a3, a1 + 72);
    if (sign_flag) goto loc_0074A2A5;
loc_0074A2A1:
    v_rbp = (unsigned int)((v_rbp) + 1);
    goto loc_0074A271;
loc_0074A2A5:
    result = (unsigned int)((1) + 1);
    result = (unsigned int)((result) & (63));
    *(unsigned int *)(v_rip - 7643835 + result * 8 + 15794660) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(v_rip - 7643835 + result * 8 + 15794656) = 0x701CBULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 7457298));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7457298)))) & (2)) != 0) {
        a3 = *(unsigned int *)(v_rsi);
        a2 = v_rip + 3893244;
        a4 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = 6;
        result = KsepDebugPrint(a1, a2, a3, a4);
    }
loc_0074A300:
    result = KsepLogError(6, v_rip + 3893221, (unsigned int)(*(unsigned int *)(v_rsi)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_0074A604;
loc_0074A30D:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 7457394, a2, a3, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 7457394;
        a2 = result;
        a1 = v_rip + 7457394;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsi = 0;
loc_0074A34F:
    if (0 >= ((unsigned int)((unsigned int)(a2)))) goto loc_0074A41E;
    v_r14 = (v_rsi + v_rsi * 4) << (4);
    v_r14 = (v_r14) + (a1);
    result = KsepIsShimRegistered(v_rip + 7457049, v_r14, a3, v_r14 + 72);
    if ((unsigned int)(result) == 0) goto loc_0074A385;
    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_0074A34F;
loc_0074A385:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    result = *(unsigned __int64 *)(v_r14 + 72);
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = v_rip + 7457043;
        result = ExfTryToWakePushLock(a1, v_r14, a3, v_r14 + 72);
    }
    result = KeAbPostRelease(v_rip + 7457031, v_r14, a3, v_r14 + 72);
    result = KeLeaveCriticalRegion(v_rip + 7457031, v_r14, a3, v_r14 + 72);
    result = (unsigned int)((1) + 1);
    result = (unsigned int)((result) & (63));
    *(unsigned int *)(v_rip - 7644110 + result * 8 + 15794660) = 0xC0000412ULL;
    *(unsigned int *)(v_rip - 7644110 + result * 8 + 15794656) = 0x701E8ULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 7457019));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7457019)))) & (2)) != 0) {
        a3 = *(unsigned int *)(v_r14);
        a2 = v_rip + 3893029;
        a1 = 6;
        result = KsepDebugPrint(a1, a2, a3, v_r14 + 72);
    }
    result = KsepLogError(6, v_rip + 3893009, (unsigned int)(*(unsigned int *)(v_r14)), v_r14 + 72);
    goto loc_0074A604;
loc_0074A41E:
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_rip + 7456890;
        result = ExfTryToWakePushLock(a1, v_rip + 3893009, (unsigned int)(*(unsigned int *)(v_r14)), v_r14 + 72);
    }
    result = KeAbPostRelease(v_rip + 7456890, v_rip + 3893009, (unsigned int)(*(unsigned int *)(v_r14)), v_r14 + 72);
    result = KeLeaveCriticalRegion(v_rip + 7456890, v_rip + 3893009, (unsigned int)(*(unsigned int *)(v_r14)), v_r14 + 72);
    goto loc_0074A459;
loc_0074A454:
loc_0074A459:
    if (1 == 0) goto loc_0074A5A8;
    result = KsepGetLoadedModulesList(v_stack_p20, v_rip + 3893009, (unsigned int)(*(unsigned int *)(v_r14)), v_r14 + 72);
    if (sign_flag) goto loc_0074A604;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 7456890, a2, a3, v_r14 + 72);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 7456890;
        a2 = result;
        a1 = v_rip + 7456890;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_r14 + 72);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsi = 0;
loc_0074A4BE:
    if (0 >= ((unsigned int)((unsigned int)(a2)))) goto loc_0074A57B;
    v_r14 = (v_rsi + v_rsi * 4) + (v_rsi + v_rsi * 4);
    result = KsepResolveShimHooks(v_stack_p20, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_r14 * 8 + 72) + 16) + 48), a3, v_r14 + 72);
    if (sign_flag) goto loc_0074A4F0;
    v_rsi = (unsigned int)((v_rsi) + (1));
    goto loc_0074A4BE;
loc_0074A4F0:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = v_rip + 7456680;
        result = ExfTryToWakePushLock(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_r14 * 8 + 72) + 16) + 48), a3, v_r14 + 72);
    }
    result = KeAbPostRelease(v_rip + 7456668, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_r14 * 8 + 72) + 16) + 48), a3, v_r14 + 72);
    result = KeLeaveCriticalRegion(v_rip + 7456668, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + v_r14 * 8 + 72) + 16) + 48), a3, v_r14 + 72);
    result = (unsigned int)((1) + (1));
    result = (unsigned int)((result) & (63));
    *(unsigned int *)(v_rip - 7644467 + result * 8 + 15794660) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(v_rip - 7644467 + result * 8 + 15794656) = 0x70218ULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 7456666));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7456666)))) & (2)) != 0) {
        a3 = *(unsigned int *)(a1 + v_r14 * 8);
        a2 = v_rip + 3892498;
        a4 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = 6;
        result = KsepDebugPrint(a1, a2, a3, a4);
    }
    goto loc_0074A300;
loc_0074A57B:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = v_rip + 7456546;
        result = ExfTryToWakePushLock(a1, v_rip + 3892476, (unsigned int)(*(unsigned int *)(a1 + v_r14 * 8)), a4);
    }
    result = KeAbPostRelease(v_rip + 7456546, v_rip + 3892476, (unsigned int)(*(unsigned int *)(a1 + v_r14 * 8)), a4);
    result = KeLeaveCriticalRegion(v_rip + 7456546, v_rip + 3892476, (unsigned int)(*(unsigned int *)(a1 + v_r14 * 8)), a4);
loc_0074A5A8:
    if (sign_flag) goto loc_0074A604;
    result = (unsigned int)((1) + 1);
    result = (unsigned int)((result) & (63));
    *(unsigned int *)(v_rip - 7644610 + result * 8 + 15795168) = 0x70226ULL;
    result = (unsigned int)(*(unsigned int *)(v_rip + 7456522));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7456522)))) & (1)) != 0) {
        a3 = (unsigned int)((unsigned int)(a2));
        a2 = v_rip + 3892420;
        a1 = 6;
        result = KsepDebugPrint(a1, a2, a3, a4);
    }
    result = KsepLogInfo(6, v_rip + 3892403, (unsigned int)((unsigned int)((unsigned int)(a2))), a4);
loc_0074A604:
    result = KsepPoolFreePaged(v_stack_p20, v_rip + 3892403, (unsigned int)((unsigned int)((unsigned int)(a2))), a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t KsepResolveApplicableShimsForDriver(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_rbx = (local_rbx) | (-1);
    local_rdi = 0;
    local_rbp = 0;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_p18 = 0;
    local_r12 = 0;
    result = KeAbPreAcquire(v_rip + 7457572, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 7457572;
        Arg2 = result;
        Arg1 = v_rip + 7457572;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_0074A240;
loc_0074A1F1:
    result = KsepIsShimRegistered(v_rip + 7457409, Arg1, Arg3, Arg1 + 72);
    if (((uint32_t)(result)) != 1) goto loc_0074A21B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x18))) == 0) { local_r12 = 1; }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x18))) + 1);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x18) = (uint32_t)(result);
    goto loc_0074A226;
loc_0074A21B:
    v_stack_p18 = 1;
loc_0074A226:
    local_rbp = (Arg1) + (80);
    local_rsi = (Arg1 + 72) + (80);
    local_r14 = ((uint32_t)(Arg2)) - (1);
    if (condition_is_not_equal) goto loc_0074A1F1;
    local_rdi = 0;
loc_0074A240:
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = v_rip + 7457394;
        result = ExfTryToWakePushLock(Arg1, Arg1, Arg3, Arg1 + 72);
    }
    result = KeAbPostRelease(v_rip + 7457394, Arg1, Arg3, Arg1 + 72);
    result = KeLeaveCriticalRegion(v_rip + 7457394, Arg1, Arg3, Arg1 + 72);
    if ((uint32_t)((uint32_t)(v_stack_p18)) == 0) goto loc_0074A454;
    local_rbp = 0;
loc_0074A271:
    if (0 >= ((uint32_t)((uint32_t)(Arg2)))) goto loc_0074A30D;
    local_rsi = (local_rbp * 4) + (0);
    local_rsi = (local_rsi) << (4);
    local_rsi = (local_rsi) + (Arg1);
    if ((*(uint64_t *)(local_rsi + 0x48)) != 0) goto loc_0074A2A1;
    result = KsepLoadShimProvider(local_rsi, Arg1, Arg3, Arg1 + 72);
    if (sign_flag) goto loc_0074A2A5;
loc_0074A2A1:
    local_rbp = (uint32_t)((local_rbp) + 1);
    goto loc_0074A271;
loc_0074A2A5:
    result = (uint32_t)((1) + 1);
    result = (uint32_t)((result) & (63));
    *(uint32_t *)(v_rip - 0x74A2BB + result * 8 + 0xF101E4) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(v_rip - 0x74A2BB + result * 8 + 0xF101E0) = 0x701CBULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x71CA12));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x71CA12)))) & (2)) != 0) {
        Arg3 = *(uint32_t *)(local_rsi);
        Arg2 = v_rip + 3893244;
        a4 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = 6;
        result = KsepDebugPrint(Arg1, Arg2, Arg3, a4);
    }
loc_0074A300:
    result = KsepLogError(6, v_rip + 3893221, (uint32_t)(*(uint32_t *)(local_rsi)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_0074A604;
loc_0074A30D:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 7457394, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 7457394;
        Arg2 = result;
        Arg1 = v_rip + 7457394;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsi = 0;
loc_0074A34F:
    if (0 >= ((uint32_t)((uint32_t)(Arg2)))) goto loc_0074A41E;
    local_r14 = (local_rsi + local_rsi * 4) << (4);
    local_r14 = (local_r14) + (Arg1);
    result = KsepIsShimRegistered(v_rip + 7457049, local_r14, Arg3, local_r14 + 72);
    if ((uint32_t)(result) == 0) goto loc_0074A385;
    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_0074A34F;
loc_0074A385:
    local_rbx = (uint8_t)((local_rbx) & (6));
    result = *(uint64_t *)(local_r14 + 0x48);
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = v_rip + 7457043;
        result = ExfTryToWakePushLock(Arg1, local_r14, Arg3, local_r14 + 72);
    }
    result = KeAbPostRelease(v_rip + 7457031, local_r14, Arg3, local_r14 + 72);
    result = KeLeaveCriticalRegion(v_rip + 7457031, local_r14, Arg3, local_r14 + 72);
    result = (uint32_t)((1) + 1);
    result = (uint32_t)((result) & (63));
    *(uint32_t *)(v_rip - 0x74A3CE + result * 8 + 0xF101E4) = 0xC0000412ULL;
    *(uint32_t *)(v_rip - 0x74A3CE + result * 8 + 0xF101E0) = 0x701E8ULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x71C8FB));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x71C8FB)))) & (2)) != 0) {
        Arg3 = *(uint32_t *)(local_r14);
        Arg2 = v_rip + 3893029;
        Arg1 = 6;
        result = KsepDebugPrint(Arg1, Arg2, Arg3, local_r14 + 72);
    }
    result = KsepLogError(6, v_rip + 3893009, (uint32_t)(*(uint32_t *)(local_r14)), local_r14 + 72);
    goto loc_0074A604;
loc_0074A41E:
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = v_rip + 7456890;
        result = ExfTryToWakePushLock(Arg1, v_rip + 3893009, (uint32_t)(*(uint32_t *)(local_r14)), local_r14 + 72);
    }
    result = KeAbPostRelease(v_rip + 7456890, v_rip + 3893009, (uint32_t)(*(uint32_t *)(local_r14)), local_r14 + 72);
    result = KeLeaveCriticalRegion(v_rip + 7456890, v_rip + 3893009, (uint32_t)(*(uint32_t *)(local_r14)), local_r14 + 72);
    goto loc_0074A459;
loc_0074A454:
loc_0074A459:
    if (1 == 0) goto loc_0074A5A8;
    result = KsepGetLoadedModulesList(v_stack_p20, v_rip + 3893009, (uint32_t)(*(uint32_t *)(local_r14)), local_r14 + 72);
    if (sign_flag) goto loc_0074A604;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 7456890, Arg2, Arg3, local_r14 + 72);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 7456890;
        Arg2 = result;
        Arg1 = v_rip + 7456890;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, local_r14 + 72);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsi = 0;
loc_0074A4BE:
    if (0 >= ((uint32_t)((uint32_t)(Arg2)))) goto loc_0074A57B;
    local_r14 = (local_rsi + local_rsi * 4) + (local_rsi + local_rsi * 4);
    result = KsepResolveShimHooks(v_stack_p20, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + local_r14 * 8 + 0x48) + 0x10) + 0x30), Arg3, local_r14 + 72);
    if (sign_flag) goto loc_0074A4F0;
    local_rsi = (uint32_t)((local_rsi) + (1));
    goto loc_0074A4BE;
loc_0074A4F0:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = v_rip + 7456680;
        result = ExfTryToWakePushLock(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + local_r14 * 8 + 0x48) + 0x10) + 0x30), Arg3, local_r14 + 72);
    }
    result = KeAbPostRelease(v_rip + 7456668, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + local_r14 * 8 + 0x48) + 0x10) + 0x30), Arg3, local_r14 + 72);
    result = KeLeaveCriticalRegion(v_rip + 7456668, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + local_r14 * 8 + 0x48) + 0x10) + 0x30), Arg3, local_r14 + 72);
    result = (uint32_t)((1) + (1));
    result = (uint32_t)((result) & (63));
    *(uint32_t *)(v_rip - 0x74A533 + result * 8 + 0xF101E4) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(v_rip - 0x74A533 + result * 8 + 0xF101E0) = 0x70218ULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x71C79A));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x71C79A)))) & (2)) != 0) {
        Arg3 = *(uint32_t *)(arg1 + local_r14 * 8);
        Arg2 = v_rip + 3892498;
        a4 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = 6;
        result = KsepDebugPrint(Arg1, Arg2, Arg3, a4);
    }
    goto loc_0074A300;
loc_0074A57B:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = v_rip + 7456546;
        result = ExfTryToWakePushLock(Arg1, v_rip + 3892476, (uint32_t)(*(uint32_t *)(arg1 + local_r14 * 8)), a4);
    }
    result = KeAbPostRelease(v_rip + 7456546, v_rip + 3892476, (uint32_t)(*(uint32_t *)(arg1 + local_r14 * 8)), a4);
    result = KeLeaveCriticalRegion(v_rip + 7456546, v_rip + 3892476, (uint32_t)(*(uint32_t *)(arg1 + local_r14 * 8)), a4);
loc_0074A5A8:
    if (sign_flag) goto loc_0074A604;
    result = (uint32_t)((1) + 1);
    result = (uint32_t)((result) & (63));
    *(uint32_t *)(v_rip - 0x74A5C2 + result * 8 + 0xF103E0) = 0x70226ULL;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x71C70A));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x71C70A)))) & (1)) != 0) {
        Arg3 = (uint32_t)((uint32_t)(Arg2));
        Arg2 = v_rip + 3892420;
        Arg1 = 6;
        result = KsepDebugPrint(Arg1, Arg2, Arg3, a4);
    }
    result = KsepLogInfo(6, v_rip + 3892403, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a4);
loc_0074A604:
    result = KsepPoolFreePaged(v_stack_p20, v_rip + 3892403, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a4);
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x0 + r14*8` | `32` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x48 + r14*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0074A168&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
