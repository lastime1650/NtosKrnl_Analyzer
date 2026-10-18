# CmpCallbackFillObjectContext

- RVA: `0x00866A10`–`0x00867442` (길이 `2,610` bytes)
- VA: `0x0000000140866A10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006BC34`
- 디코드: `626`개 명령, `2,610/2,610` bytes 표시
- 미해석 바이트: `3` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **44**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00866AEC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00866B19` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00866BDA` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00866BE8` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00866C28` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00866C55` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00866CBE` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00866CEB` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00866D54` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00866D81` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00866E03` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00866E30` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00866EA6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00866EB4` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00866F01` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00866F0F` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00866F5C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00866F6A` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00866FB7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00866FC5` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00867015` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00867042` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x008670BB` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008670E8` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0086714D` → [CmpLockContextListShared](../99/CmpLockContextListShared_function_0099E6C0.md) (function, `0x0099E6C0`)
- `0x008671AC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008671D9` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x00867243` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00867251` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086729A` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x008672BD` → [CmpLockContextListShared](../99/CmpLockContextListShared_function_0099E6C0.md) (function, `0x0099E6C0`)
- `0x008672DE` → [CmpUnlockContextList](../93/CmpUnlockContextList_function_00936C10.md) (function, `0x00936C10`)
- `0x008672EF` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00867300` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00867311` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00867321` → [CmpGetCallbackObjectContext](../94/CmpGetCallbackObjectContext_function_0094D670.md) (function, `0x0094D670`)
- `0x00867336` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00867347` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00867357` → [CmpGetCallbackObjectContext](../94/CmpGetCallbackObjectContext_function_0094D670.md) (function, `0x0094D670`)
- `0x0086736B` → [CmpGetCallbackObjectContext](../94/CmpGetCallbackObjectContext_function_0094D670.md) (function, `0x0094D670`)
- `0x0086737F` → [CmpGetCallbackObjectContext](../94/CmpGetCallbackObjectContext_function_0094D670.md) (function, `0x0094D670`)
- `0x00867393` → [CmpGetCallbackObjectContext](../94/CmpGetCallbackObjectContext_function_0094D670.md) (function, `0x0094D670`)
- `0x008673A7` → [CmpGetCallbackObjectContext](../94/CmpGetCallbackObjectContext_function_0094D670.md) (function, `0x0094D670`)
- `0x008673BB` → [CmpGetCallbackObjectContext](../94/CmpGetCallbackObjectContext_function_0094D670.md) (function, `0x0094D670`)

### Direct callers
- [CmpCallCallBacksEx](CmpCallCallBacksEx_function_00865F40.md) at `0x00866349`
- [CmpCallCallBacksEx](CmpCallCallBacksEx_function_00865F40.md) at `0x00866554`

### Static image references
- `0x00866A5F` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00866AD8` → RVA `0x00EF7BC8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **34**
  - `0x00866AEC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00866B19` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00866BDA` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00866BE8` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00866C28` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00866C55` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00866CBE` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00866CEB` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00866D54` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00866D81` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00866E03` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00866E30` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00866EA6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00866EB4` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00866F01` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00866F0F` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00866F5C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00866F6A` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00866FB7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00866FC5` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00867015` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00867042` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008670BB` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008670E8` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x008671AC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008671D9` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x00867243` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00867251` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086729A` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x008672EF` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00867300` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00867311` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00867336` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00867347` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008673E0` → [VrpRegistryCallback + 0x5](VrpRegistryCallback_function_00867450.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00866A10  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00866A15  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00866A1A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00866A1F  57                              push rdi
00866A20  41 56                           push r14
00866A22  41 57                           push r15
00866A24  48 83 EC 20                     sub rsp, 0x20
00866A28  49 8B F0                        mov rsi, r8
00866A2B  48 8B DA                        mov rbx, rdx
00866A2E  83 F9 32                        cmp ecx, 0x32
00866A31  74 61                           je 0x140866a94
00866A33  83 F9 1C                        cmp ecx, 0x1c
00866A36  0F 84 04 01 00 00               je 0x140866b40
00866A3C  83 F9 08                        cmp ecx, 8
00866A3F  0F 84 15 01 00 00               je 0x140866b5a
00866A45  83 F9 07                        cmp ecx, 7
00866A48  0F 84 25 01 00 00               je 0x140866b73
00866A4E  83 F9 1D                        cmp ecx, 0x1d
00866A51  0F 84 35 01 00 00               je 0x140866b8c
00866A57  83 F9 31                        cmp ecx, 0x31
00866A5A  77 48                           ja 0x140866aa4
00866A5C  48 63 C1                        movsxd rax, ecx
00866A5F  48 8D 15 9A 95 79 FF            lea rdx, [rip - 0x866a66]
00866A66  0F B6 84 02 10 74 86 00         movzx eax, byte ptr [rdx + rax + 0x867410]
00866A6E  8B 8C 82 CC 73 86 00            mov ecx, dword ptr [rdx + rax*4 + 0x8673cc]
00866A75  48 03 CA                        add rcx, rdx
00866A78  FF E1                           jmp rcx
00866A7A  CC                              int3
00866A7B  CC                              int3
00866A7C  CC                              int3
00866A7D  CC                              int3
00866A7E  48 8B 03                        mov rax, qword ptr [rbx]
00866A81  33 FF                           xor edi, edi
00866A83  8B EF                           mov ebp, edi
00866A85  48 85 C0                        test rax, rax
00866A88  0F 85 3F 03 00 00               jne 0x140866dcd
00866A8E  48 89 6B 10                     mov qword ptr [rbx + 0x10], rbp
00866A92  EB 10                           jmp 0x140866aa4
00866A94  48 8B 03                        mov rax, qword ptr [rbx]
00866A97  33 FF                           xor edi, edi
00866A99  8B EF                           mov ebp, edi
00866A9B  48 85 C0                        test rax, rax
00866A9E  75 1E                           jne 0x140866abe
00866AA0  48 89 6B 28                     mov qword ptr [rbx + 0x28], rbp
00866AA4  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00866AA9  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00866AAE  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00866AB3  48 83 C4 20                     add rsp, 0x20
00866AB7  41 5F                           pop r15
00866AB9  41 5E                           pop r14
00866ABB  5F                              pop rdi
00866ABC  C3                              ret
00866ABD  CC                              int3
00866ABE  81 38 32 30 79 6B               cmp dword ptr [rax], 0x6b793032
00866AC4  75 DA                           jne 0x140866aa0
00866AC6  4C 8D 70 48                     lea r14, [rax + 0x48]
00866ACA  4D 39 36                        cmp qword ptr [r14], r14
00866ACD  74 D1                           je 0x140866aa0
00866ACF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00866AD8  48 8D 0D E9 10 69 00            lea rcx, [rip + 0x6910e9]
00866ADF  45 33 C0                        xor r8d, r8d
00866AE2  33 D2                           xor edx, edx
00866AE4  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00866AEB  90                              nop
00866AEC  E8 3F 97 9A FF                  call 0x140210230
00866AF1  4C 8B F8                        mov r15, rax
00866AF4  B9 11 00 00 00                  mov ecx, 0x11
00866AF9  33 C0                           xor eax, eax
00866AFB  F0 48 0F B1 0D C4 10 69 00      lock cmpxchg qword ptr [rip + 0x6910c4], rcx
00866B04  74 18                           je 0x140866b1e
00866B06  4C 8D 0D BB 10 69 00            lea r9, [rip + 0x6910bb]
00866B0D  4D 8B C7                        mov r8, r15
00866B10  33 D2                           xor edx, edx
00866B12  48 8D 0D AF 10 69 00            lea rcx, [rip + 0x6910af]
00866B19  E8 2E 99 9A FF                  call 0x14021044c
00866B1E  4D 85 FF                        test r15, r15
00866B21  74 05                           je 0x140866b28
00866B23  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
00866B28  49 8B 06                        mov rax, qword ptr [r14]
00866B2B  49 3B C6                        cmp rax, r14
00866B2E  74 6B                           je 0x140866b9b
00866B30  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00866B34  48 3B 0E                        cmp rcx, qword ptr [rsi]
00866B37  74 5E                           je 0x140866b97
00866B39  7C 60                           jl 0x140866b9b
00866B3B  48 8B 00                        mov rax, qword ptr [rax]
00866B3E  EB EB                           jmp 0x140866b2b
00866B40  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00866B44  33 FF                           xor edi, edi
00866B46  8B EF                           mov ebp, edi
00866B48  48 85 C0                        test rax, rax
00866B4B  0F 85 A1 00 00 00               jne 0x140866bf2
00866B51  48 89 6B 58                     mov qword ptr [rbx + 0x58], rbp
00866B55  E9 4A FF FF FF                  jmp 0x140866aa4
00866B5A  48 8B 02                        mov rax, qword ptr [rdx]
00866B5D  33 FF                           xor edi, edi
00866B5F  8B EF                           mov ebp, edi
00866B61  48 85 C0                        test rax, rax
00866B64  0F 85 1E 01 00 00               jne 0x140866c88
00866B6A  48 89 6B 38                     mov qword ptr [rbx + 0x38], rbp
00866B6E  E9 31 FF FF FF                  jmp 0x140866aa4
00866B73  48 8B 02                        mov rax, qword ptr [rdx]
00866B76  33 FF                           xor edi, edi
00866B78  8B EF                           mov ebp, edi
00866B7A  48 85 C0                        test rax, rax
00866B7D  0F 85 9B 01 00 00               jne 0x140866d1e
00866B83  48 89 6B 30                     mov qword ptr [rbx + 0x30], rbp
00866B87  E9 18 FF FF FF                  jmp 0x140866aa4
00866B8C  33 FF                           xor edi, edi
00866B8E  48 89 7B 28                     mov qword ptr [rbx + 0x28], rdi
00866B92  E9 0D FF FF FF                  jmp 0x140866aa4
00866B97  48 8B 68 38                     mov rbp, qword ptr [rax + 0x38]
00866B9B  0F 0D 0D 26 10 69 00            prefetchw byte ptr [rip + 0x691026]
00866BA2  48 8B 05 1F 10 69 00            mov rax, qword ptr [rip + 0x69101f]
00866BA9  48 8B C8                        mov rcx, rax
00866BAC  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00866BB0  48 83 F9 10                     cmp rcx, 0x10
00866BB4  48 8D 50 F0                     lea rdx, [rax - 0x10]
00866BB8  48 0F 46 D7                     cmovbe rdx, rdi
00866BBC  A8 02                           test al, 2
00866BBE  0F 85 24 07 00 00               jne 0x1408672e8
00866BC4  F0 48 0F B1 15 FB 0F 69 00      lock cmpxchg qword ptr [rip + 0x690ffb], rdx
00866BCD  0F 85 15 07 00 00               jne 0x1408672e8
00866BD3  48 8D 0D EE 0F 69 00            lea rcx, [rip + 0x690fee]
00866BDA  E8 21 AA A7 FF                  call 0x1402e1600
00866BDF  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00866BE8  E8 03 84 9F FF                  call 0x14025eff0
00866BED  E9 AE FE FF FF                  jmp 0x140866aa0
00866BF2  81 38 32 30 79 6B               cmp dword ptr [rax], 0x6b793032
00866BF8  0F 85 53 FF FF FF               jne 0x140866b51
00866BFE  4C 8D 70 48                     lea r14, [rax + 0x48]
00866C02  4D 39 36                        cmp qword ptr [r14], r14
00866C05  0F 84 46 FF FF FF               je 0x140866b51
00866C0B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00866C14  48 8D 0D AD 0F 69 00            lea rcx, [rip + 0x690fad]
00866C1B  45 33 C0                        xor r8d, r8d
00866C1E  33 D2                           xor edx, edx
00866C20  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00866C27  90                              nop
00866C28  E8 03 96 9A FF                  call 0x140210230
00866C2D  4C 8B F8                        mov r15, rax
00866C30  B9 11 00 00 00                  mov ecx, 0x11
00866C35  33 C0                           xor eax, eax
00866C37  F0 48 0F B1 0D 88 0F 69 00      lock cmpxchg qword ptr [rip + 0x690f88], rcx
00866C40  74 18                           je 0x140866c5a
00866C42  4C 8D 0D 7F 0F 69 00            lea r9, [rip + 0x690f7f]
00866C49  4D 8B C7                        mov r8, r15
00866C4C  33 D2                           xor edx, edx
00866C4E  48 8D 0D 73 0F 69 00            lea rcx, [rip + 0x690f73]
00866C55  E8 F2 97 9A FF                  call 0x14021044c
00866C5A  4D 85 FF                        test r15, r15
00866C5D  74 05                           je 0x140866c64
00866C5F  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
00866C64  49 8B 06                        mov rax, qword ptr [r14]
00866C67  49 3B C6                        cmp rax, r14
00866C6A  0F 84 F7 01 00 00               je 0x140866e67
00866C70  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00866C74  48 3B 0E                        cmp rcx, qword ptr [rsi]
00866C77  0F 84 E6 01 00 00               je 0x140866e63
00866C7D  0F 8C E4 01 00 00               jl 0x140866e67
00866C83  48 8B 00                        mov rax, qword ptr [rax]
00866C86  EB DF                           jmp 0x140866c67
00866C88  81 38 32 30 79 6B               cmp dword ptr [rax], 0x6b793032
00866C8E  0F 85 D6 FE FF FF               jne 0x140866b6a
00866C94  4C 8D 70 48                     lea r14, [rax + 0x48]
00866C98  4D 39 36                        cmp qword ptr [r14], r14
00866C9B  0F 84 C9 FE FF FF               je 0x140866b6a
00866CA1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00866CAA  48 8D 0D 17 0F 69 00            lea rcx, [rip + 0x690f17]
00866CB1  45 33 C0                        xor r8d, r8d
00866CB4  33 D2                           xor edx, edx
00866CB6  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00866CBD  90                              nop
00866CBE  E8 6D 95 9A FF                  call 0x140210230
00866CC3  4C 8B F8                        mov r15, rax
00866CC6  B9 11 00 00 00                  mov ecx, 0x11
00866CCB  33 C0                           xor eax, eax
00866CCD  F0 48 0F B1 0D F2 0E 69 00      lock cmpxchg qword ptr [rip + 0x690ef2], rcx
00866CD6  74 18                           je 0x140866cf0
00866CD8  4C 8D 0D E9 0E 69 00            lea r9, [rip + 0x690ee9]
00866CDF  4D 8B C7                        mov r8, r15
00866CE2  33 D2                           xor edx, edx
00866CE4  48 8D 0D DD 0E 69 00            lea rcx, [rip + 0x690edd]
00866CEB  E8 5C 97 9A FF                  call 0x14021044c
00866CF0  4D 85 FF                        test r15, r15
00866CF3  74 05                           je 0x140866cfa
00866CF5  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
00866CFA  49 8B 06                        mov rax, qword ptr [r14]
00866CFD  49 3B C6                        cmp rax, r14
00866D00  0F 84 BC 01 00 00               je 0x140866ec2
00866D06  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00866D0A  48 3B 0E                        cmp rcx, qword ptr [rsi]
00866D0D  0F 84 AB 01 00 00               je 0x140866ebe
00866D13  0F 8C A9 01 00 00               jl 0x140866ec2
00866D19  48 8B 00                        mov rax, qword ptr [rax]
00866D1C  EB DF                           jmp 0x140866cfd
00866D1E  81 38 32 30 79 6B               cmp dword ptr [rax], 0x6b793032
00866D24  0F 85 59 FE FF FF               jne 0x140866b83
00866D2A  4C 8D 70 48                     lea r14, [rax + 0x48]
00866D2E  4D 39 36                        cmp qword ptr [r14], r14
00866D31  0F 84 4C FE FF FF               je 0x140866b83
00866D37  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00866D40  48 8D 0D 81 0E 69 00            lea rcx, [rip + 0x690e81]
00866D47  45 33 C0                        xor r8d, r8d
00866D4A  33 D2                           xor edx, edx
00866D4C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00866D53  90                              nop
00866D54  E8 D7 94 9A FF                  call 0x140210230
00866D59  4C 8B F8                        mov r15, rax
00866D5C  B9 11 00 00 00                  mov ecx, 0x11
00866D61  33 C0                           xor eax, eax
00866D63  F0 48 0F B1 0D 5C 0E 69 00      lock cmpxchg qword ptr [rip + 0x690e5c], rcx
00866D6C  74 18                           je 0x140866d86
00866D6E  4C 8D 0D 53 0E 69 00            lea r9, [rip + 0x690e53]
00866D75  4D 8B C7                        mov r8, r15
00866D78  33 D2                           xor edx, edx
00866D7A  48 8D 0D 47 0E 69 00            lea rcx, [rip + 0x690e47]
00866D81  E8 C6 96 9A FF                  call 0x14021044c
00866D86  4D 85 FF                        test r15, r15
00866D89  74 05                           je 0x140866d90
00866D8B  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
00866D90  49 8B 06                        mov rax, qword ptr [r14]
00866D93  49 3B C6                        cmp rax, r14
00866D96  0F 84 81 01 00 00               je 0x140866f1d
00866D9C  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00866DA0  48 3B 0E                        cmp rcx, qword ptr [rsi]
00866DA3  0F 84 70 01 00 00               je 0x140866f19
00866DA9  0F 8C 6E 01 00 00               jl 0x140866f1d
00866DAF  48 8B 00                        mov rax, qword ptr [rax]
00866DB2  EB DF                           jmp 0x140866d93
00866DB4  48 8B 03                        mov rax, qword ptr [rbx]
00866DB7  33 FF                           xor edi, edi
00866DB9  8B EF                           mov ebp, edi
00866DBB  48 85 C0                        test rax, rax
00866DBE  0F 85 B2 03 00 00               jne 0x140867176
00866DC4  48 89 6B 18                     mov qword ptr [rbx + 0x18], rbp
00866DC8  E9 D7 FC FF FF                  jmp 0x140866aa4
00866DCD  81 38 32 30 79 6B               cmp dword ptr [rax], 0x6b793032
00866DD3  0F 85 B5 FC FF FF               jne 0x140866a8e
00866DD9  4C 8D 70 48                     lea r14, [rax + 0x48]
00866DDD  4D 39 36                        cmp qword ptr [r14], r14
00866DE0  0F 84 A8 FC FF FF               je 0x140866a8e
00866DE6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00866DEF  48 8D 0D D2 0D 69 00            lea rcx, [rip + 0x690dd2]
00866DF6  45 33 C0                        xor r8d, r8d
00866DF9  33 D2                           xor edx, edx
00866DFB  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00866E02  90                              nop
00866E03  E8 28 94 9A FF                  call 0x140210230
00866E08  4C 8B F8                        mov r15, rax
00866E0B  B9 11 00 00 00                  mov ecx, 0x11
00866E10  33 C0                           xor eax, eax
00866E12  F0 48 0F B1 0D AD 0D 69 00      lock cmpxchg qword ptr [rip + 0x690dad], rcx
00866E1B  74 18                           je 0x140866e35
00866E1D  4C 8D 0D A4 0D 69 00            lea r9, [rip + 0x690da4]
00866E24  4D 8B C7                        mov r8, r15
00866E27  33 D2                           xor edx, edx
00866E29  48 8D 0D 98 0D 69 00            lea rcx, [rip + 0x690d98]
00866E30  E8 17 96 9A FF                  call 0x14021044c
00866E35  4D 85 FF                        test r15, r15
00866E38  74 05                           je 0x140866e3f
00866E3A  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
00866E3F  49 8B 06                        mov rax, qword ptr [r14]
00866E42  49 3B C6                        cmp rax, r14
00866E45  0F 84 2D 01 00 00               je 0x140866f78
00866E4B  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00866E4F  48 3B 0E                        cmp rcx, qword ptr [rsi]
00866E52  0F 84 1C 01 00 00               je 0x140866f74
00866E58  0F 8C 1A 01 00 00               jl 0x140866f78
00866E5E  48 8B 00                        mov rax, qword ptr [rax]
00866E61  EB DF                           jmp 0x140866e42
00866E63  48 8B 68 38                     mov rbp, qword ptr [rax + 0x38]
00866E67  0F 0D 0D 5A 0D 69 00            prefetchw byte ptr [rip + 0x690d5a]
00866E6E  48 8B 05 53 0D 69 00            mov rax, qword ptr [rip + 0x690d53]
00866E75  48 8B C8                        mov rcx, rax
00866E78  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00866E7C  48 83 F9 10                     cmp rcx, 0x10
00866E80  48 8D 50 F0                     lea rdx, [rax - 0x10]
00866E84  48 0F 46 D7                     cmovbe rdx, rdi
00866E88  A8 02                           test al, 2
00866E8A  0F 85 69 04 00 00               jne 0x1408672f9
00866E90  F0 48 0F B1 15 2F 0D 69 00      lock cmpxchg qword ptr [rip + 0x690d2f], rdx
00866E99  0F 85 5A 04 00 00               jne 0x1408672f9
00866E9F  48 8D 0D 22 0D 69 00            lea rcx, [rip + 0x690d22]
00866EA6  E8 55 A7 A7 FF                  call 0x1402e1600
00866EAB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00866EB4  E8 37 81 9F FF                  call 0x14025eff0
00866EB9  E9 93 FC FF FF                  jmp 0x140866b51
00866EBE  48 8B 68 38                     mov rbp, qword ptr [rax + 0x38]
00866EC2  0F 0D 0D FF 0C 69 00            prefetchw byte ptr [rip + 0x690cff]
00866EC9  48 8B 05 F8 0C 69 00            mov rax, qword ptr [rip + 0x690cf8]
00866ED0  48 8B C8                        mov rcx, rax
00866ED3  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00866ED7  48 83 F9 10                     cmp rcx, 0x10
00866EDB  48 8D 50 F0                     lea rdx, [rax - 0x10]
00866EDF  48 0F 46 D7                     cmovbe rdx, rdi
00866EE3  A8 02                           test al, 2
00866EE5  0F 85 1F 04 00 00               jne 0x14086730a
00866EEB  F0 48 0F B1 15 D4 0C 69 00      lock cmpxchg qword ptr [rip + 0x690cd4], rdx
00866EF4  0F 85 10 04 00 00               jne 0x14086730a
00866EFA  48 8D 0D C7 0C 69 00            lea rcx, [rip + 0x690cc7]
00866F01  E8 FA A6 A7 FF                  call 0x1402e1600
00866F06  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00866F0F  E8 DC 80 9F FF                  call 0x14025eff0
00866F14  E9 51 FC FF FF                  jmp 0x140866b6a
00866F19  48 8B 68 38                     mov rbp, qword ptr [rax + 0x38]
00866F1D  0F 0D 0D A4 0C 69 00            prefetchw byte ptr [rip + 0x690ca4]
00866F24  48 8B 05 9D 0C 69 00            mov rax, qword ptr [rip + 0x690c9d]
00866F2B  48 8B C8                        mov rcx, rax
00866F2E  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00866F32  48 83 F9 10                     cmp rcx, 0x10
00866F36  48 8D 50 F0                     lea rdx, [rax - 0x10]
00866F3A  48 0F 46 D7                     cmovbe rdx, rdi
00866F3E  A8 02                           test al, 2
00866F40  0F 85 4D 03 00 00               jne 0x140867293
00866F46  F0 48 0F B1 15 79 0C 69 00      lock cmpxchg qword ptr [rip + 0x690c79], rdx
00866F4F  0F 85 3E 03 00 00               jne 0x140867293
00866F55  48 8D 0D 6C 0C 69 00            lea rcx, [rip + 0x690c6c]
00866F5C  E8 9F A6 A7 FF                  call 0x1402e1600
00866F61  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00866F6A  E8 81 80 9F FF                  call 0x14025eff0
00866F6F  E9 0F FC FF FF                  jmp 0x140866b83
00866F74  48 8B 68 38                     mov rbp, qword ptr [rax + 0x38]
00866F78  0F 0D 0D 49 0C 69 00            prefetchw byte ptr [rip + 0x690c49]
00866F7F  48 8B 05 42 0C 69 00            mov rax, qword ptr [rip + 0x690c42]
00866F86  48 8B C8                        mov rcx, rax
00866F89  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00866F8D  48 83 F9 10                     cmp rcx, 0x10
00866F91  48 8D 50 F0                     lea rdx, [rax - 0x10]
00866F95  48 0F 46 D7                     cmovbe rdx, rdi
00866F99  A8 02                           test al, 2
00866F9B  0F 85 8E 03 00 00               jne 0x14086732f
00866FA1  F0 48 0F B1 15 1E 0C 69 00      lock cmpxchg qword ptr [rip + 0x690c1e], rdx
00866FAA  0F 85 7F 03 00 00               jne 0x14086732f
00866FB0  48 8D 0D 11 0C 69 00            lea rcx, [rip + 0x690c11]
00866FB7  E8 44 A6 A7 FF                  call 0x1402e1600
00866FBC  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00866FC5  E8 26 80 9F FF                  call 0x14025eff0
00866FCA  E9 BF FA FF FF                  jmp 0x140866a8e
00866FCF  48 8B 03                        mov rax, qword ptr [rbx]
00866FD2  33 FF                           xor edi, edi
00866FD4  8B EF                           mov ebp, edi
00866FD6  48 85 C0                        test rax, rax
00866FD9  0F 84 A4 FB FF FF               je 0x140866b83
00866FDF  81 38 32 30 79 6B               cmp dword ptr [rax], 0x6b793032
00866FE5  0F 85 98 FB FF FF               jne 0x140866b83
00866FEB  4C 8D 70 48                     lea r14, [rax + 0x48]
00866FEF  4D 39 36                        cmp qword ptr [r14], r14
00866FF2  0F 84 8B FB FF FF               je 0x140866b83
00866FF8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00867001  48 8D 0D C0 0B 69 00            lea rcx, [rip + 0x690bc0]
00867008  45 33 C0                        xor r8d, r8d
0086700B  33 D2                           xor edx, edx
0086700D  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00867014  90                              nop
00867015  E8 16 92 9A FF                  call 0x140210230
0086701A  4C 8B F8                        mov r15, rax
0086701D  B9 11 00 00 00                  mov ecx, 0x11
00867022  33 C0                           xor eax, eax
00867024  F0 48 0F B1 0D 9B 0B 69 00      lock cmpxchg qword ptr [rip + 0x690b9b], rcx
0086702D  74 18                           je 0x140867047
0086702F  4C 8D 0D 92 0B 69 00            lea r9, [rip + 0x690b92]
00867036  4D 8B C7                        mov r8, r15
00867039  33 D2                           xor edx, edx
0086703B  48 8D 0D 86 0B 69 00            lea rcx, [rip + 0x690b86]
00867042  E8 05 94 9A FF                  call 0x14021044c
00867047  4D 85 FF                        test r15, r15
0086704A  74 05                           je 0x140867051
0086704C  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
00867051  49 8B 06                        mov rax, qword ptr [r14]
00867054  49 3B C6                        cmp rax, r14
00867057  0F 84 C0 FE FF FF               je 0x140866f1d
0086705D  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00867061  48 3B 0E                        cmp rcx, qword ptr [rsi]
00867064  0F 84 AF FE FF FF               je 0x140866f19
0086706A  0F 8C AD FE FF FF               jl 0x140866f1d
00867070  48 8B 00                        mov rax, qword ptr [rax]
00867073  EB DF                           jmp 0x140867054
00867075  48 8B 03                        mov rax, qword ptr [rbx]
00867078  33 FF                           xor edi, edi
0086707A  8B EF                           mov ebp, edi
0086707C  48 85 C0                        test rax, rax
0086707F  0F 84 FE FA FF FF               je 0x140866b83
00867085  81 38 32 30 79 6B               cmp dword ptr [rax], 0x6b793032
0086708B  0F 85 F2 FA FF FF               jne 0x140866b83
00867091  4C 8D 70 48                     lea r14, [rax + 0x48]
00867095  4D 39 36                        cmp qword ptr [r14], r14
00867098  0F 84 E5 FA FF FF               je 0x140866b83
0086709E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008670A7  48 8D 0D 1A 0B 69 00            lea rcx, [rip + 0x690b1a]
008670AE  45 33 C0                        xor r8d, r8d
008670B1  33 D2                           xor edx, edx
008670B3  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008670BA  90                              nop
008670BB  E8 70 91 9A FF                  call 0x140210230
008670C0  4C 8B F8                        mov r15, rax
008670C3  B9 11 00 00 00                  mov ecx, 0x11
008670C8  33 C0                           xor eax, eax
008670CA  F0 48 0F B1 0D F5 0A 69 00      lock cmpxchg qword ptr [rip + 0x690af5], rcx
008670D3  74 18                           je 0x1408670ed
008670D5  4C 8D 0D EC 0A 69 00            lea r9, [rip + 0x690aec]
008670DC  4D 8B C7                        mov r8, r15
008670DF  33 D2                           xor edx, edx
008670E1  48 8D 0D E0 0A 69 00            lea rcx, [rip + 0x690ae0]
008670E8  E8 5F 93 9A FF                  call 0x14021044c
008670ED  4D 85 FF                        test r15, r15
008670F0  74 05                           je 0x1408670f7
008670F2  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
008670F7  49 8B 06                        mov rax, qword ptr [r14]
008670FA  49 3B C6                        cmp rax, r14
008670FD  0F 84 5C 01 00 00               je 0x14086725f
00867103  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00867107  48 3B 0E                        cmp rcx, qword ptr [rsi]
0086710A  0F 84 4B 01 00 00               je 0x14086725b
00867110  0F 8C 49 01 00 00               jl 0x14086725f
00867116  48 8B 00                        mov rax, qword ptr [rax]
00867119  EB DF                           jmp 0x1408670fa
0086711B  48 8B 03                        mov rax, qword ptr [rbx]
0086711E  33 FF                           xor edi, edi
00867120  48 85 C0                        test rax, rax
00867123  0F 85 7B 01 00 00               jne 0x1408672a4
00867129  48 89 7B 28                     mov qword ptr [rbx + 0x28], rdi
0086712D  E9 72 F9 FF FF                  jmp 0x140866aa4
00867132  48 8B 03                        mov rax, qword ptr [rbx]
00867135  33 FF                           xor edi, edi
00867137  48 85 C0                        test rax, rax
0086713A  74 ED                           je 0x140867129
0086713C  81 38 32 30 79 6B               cmp dword ptr [rax], 0x6b793032
00867142  75 E5                           jne 0x140867129
00867144  4C 8D 70 48                     lea r14, [rax + 0x48]
00867148  4D 39 36                        cmp qword ptr [r14], r14
0086714B  74 DC                           je 0x140867129
0086714D  E8 6E 75 13 00                  call 0x14099e6c0
00867152  49 8B 06                        mov rax, qword ptr [r14]
00867155  49 3B C6                        cmp rax, r14
00867158  0F 84 80 01 00 00               je 0x1408672de
0086715E  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00867162  48 3B 0E                        cmp rcx, qword ptr [rsi]
00867165  0F 84 6F 01 00 00               je 0x1408672da
0086716B  0F 8C 6D 01 00 00               jl 0x1408672de
00867171  48 8B 00                        mov rax, qword ptr [rax]
00867174  EB DF                           jmp 0x140867155
00867176  81 38 32 30 79 6B               cmp dword ptr [rax], 0x6b793032
0086717C  0F 85 42 FC FF FF               jne 0x140866dc4
00867182  4C 8D 70 48                     lea r14, [rax + 0x48]
00867186  4D 39 36                        cmp qword ptr [r14], r14
00867189  0F 84 35 FC FF FF               je 0x140866dc4
0086718F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00867198  48 8D 0D 29 0A 69 00            lea rcx, [rip + 0x690a29]
0086719F  45 33 C0                        xor r8d, r8d
008671A2  33 D2                           xor edx, edx
008671A4  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008671AB  90                              nop
008671AC  E8 7F 90 9A FF                  call 0x140210230
008671B1  4C 8B F8                        mov r15, rax
008671B4  B9 11 00 00 00                  mov ecx, 0x11
008671B9  33 C0                           xor eax, eax
008671BB  F0 48 0F B1 0D 04 0A 69 00      lock cmpxchg qword ptr [rip + 0x690a04], rcx
008671C4  74 18                           je 0x1408671de
008671C6  4C 8D 0D FB 09 69 00            lea r9, [rip + 0x6909fb]
008671CD  4D 8B C7                        mov r8, r15
008671D0  33 D2                           xor edx, edx
008671D2  48 8D 0D EF 09 69 00            lea rcx, [rip + 0x6909ef]
008671D9  E8 6E 92 9A FF                  call 0x14021044c
008671DE  4D 85 FF                        test r15, r15
008671E1  74 05                           je 0x1408671e8
008671E3  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
008671E8  49 8B 06                        mov rax, qword ptr [r14]
008671EB  49 3B C6                        cmp rax, r14
008671EE  74 14                           je 0x140867204
008671F0  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
008671F4  48 3B 0E                        cmp rcx, qword ptr [rsi]
008671F7  74 07                           je 0x140867200
008671F9  7C 09                           jl 0x140867204
008671FB  48 8B 00                        mov rax, qword ptr [rax]
008671FE  EB EB                           jmp 0x1408671eb
00867200  48 8B 68 38                     mov rbp, qword ptr [rax + 0x38]
00867204  0F 0D 0D BD 09 69 00            prefetchw byte ptr [rip + 0x6909bd]
0086720B  48 8B 05 B6 09 69 00            mov rax, qword ptr [rip + 0x6909b6]
00867212  48 8B C8                        mov rcx, rax
00867215  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00867219  48 83 F9 10                     cmp rcx, 0x10
0086721D  48 8D 50 F0                     lea rdx, [rax - 0x10]
00867221  48 0F 46 D7                     cmovbe rdx, rdi
00867225  A8 02                           test al, 2
00867227  0F 85 13 01 00 00               jne 0x140867340
0086722D  F0 48 0F B1 15 92 09 69 00      lock cmpxchg qword ptr [rip + 0x690992], rdx
00867236  0F 85 04 01 00 00               jne 0x140867340
0086723C  48 8D 0D 85 09 69 00            lea rcx, [rip + 0x690985]
00867243  E8 B8 A3 A7 FF                  call 0x1402e1600
00867248  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00867251  E8 9A 7D 9F FF                  call 0x14025eff0
00867256  E9 69 FB FF FF                  jmp 0x140866dc4
0086725B  48 8B 68 38                     mov rbp, qword ptr [rax + 0x38]
0086725F  0F 0D 0D 62 09 69 00            prefetchw byte ptr [rip + 0x690962]
00867266  48 8B 05 5B 09 69 00            mov rax, qword ptr [rip + 0x69095b]
0086726D  48 8B C8                        mov rcx, rax
00867270  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00867274  48 83 F9 10                     cmp rcx, 0x10
00867278  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086727C  48 0F 46 D7                     cmovbe rdx, rdi
00867280  A8 02                           test al, 2
00867282  75 0F                           jne 0x140867293
00867284  F0 48 0F B1 15 3B 09 69 00      lock cmpxchg qword ptr [rip + 0x69093b], rdx
0086728D  0F 84 C2 FC FF FF               je 0x140866f55
00867293  48 8D 0D 2E 09 69 00            lea rcx, [rip + 0x69092e]
0086729A  E8 31 C6 9F FF                  call 0x1402638d0
0086729F  E9 B1 FC FF FF                  jmp 0x140866f55
008672A4  81 38 32 30 79 6B               cmp dword ptr [rax], 0x6b793032
008672AA  0F 85 79 FE FF FF               jne 0x140867129
008672B0  4C 8D 70 48                     lea r14, [rax + 0x48]
008672B4  4D 39 36                        cmp qword ptr [r14], r14
008672B7  0F 84 6C FE FF FF               je 0x140867129
008672BD  E8 FE 73 13 00                  call 0x14099e6c0
008672C2  49 8B 06                        mov rax, qword ptr [r14]
008672C5  49 3B C6                        cmp rax, r14
008672C8  74 14                           je 0x1408672de
008672CA  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
008672CE  48 3B 0E                        cmp rcx, qword ptr [rsi]
008672D1  74 07                           je 0x1408672da
008672D3  7C 09                           jl 0x1408672de
008672D5  48 8B 00                        mov rax, qword ptr [rax]
008672D8  EB EB                           jmp 0x1408672c5
008672DA  48 8B 78 38                     mov rdi, qword ptr [rax + 0x38]
008672DE  E8 2D F9 0C 00                  call 0x140936c10
008672E3  E9 41 FE FF FF                  jmp 0x140867129
008672E8  48 8D 0D D9 08 69 00            lea rcx, [rip + 0x6908d9]
008672EF  E8 DC C5 9F FF                  call 0x1402638d0
008672F4  E9 DA F8 FF FF                  jmp 0x140866bd3
008672F9  48 8D 0D C8 08 69 00            lea rcx, [rip + 0x6908c8]
00867300  E8 CB C5 9F FF                  call 0x1402638d0
00867305  E9 95 FB FF FF                  jmp 0x140866e9f
0086730A  48 8D 0D B7 08 69 00            lea rcx, [rip + 0x6908b7]
00867311  E8 BA C5 9F FF                  call 0x1402638d0
00867316  E9 DF FB FF FF                  jmp 0x140866efa
0086731B  48 8B 0B                        mov rcx, qword ptr [rbx]
0086731E  48 8B D6                        mov rdx, rsi
00867321  E8 4A 63 0E 00                  call 0x14094d670
00867326  48 89 43 38                     mov qword ptr [rbx + 0x38], rax
0086732A  E9 75 F7 FF FF                  jmp 0x140866aa4
0086732F  48 8D 0D 92 08 69 00            lea rcx, [rip + 0x690892]
00867336  E8 95 C5 9F FF                  call 0x1402638d0
0086733B  E9 70 FC FF FF                  jmp 0x140866fb0
00867340  48 8D 0D 81 08 69 00            lea rcx, [rip + 0x690881]
00867347  E8 84 C5 9F FF                  call 0x1402638d0
0086734C  E9 EB FE FF FF                  jmp 0x14086723c
00867351  48 8B 0B                        mov rcx, qword ptr [rbx]
00867354  48 8B D6                        mov rdx, rsi
00867357  E8 14 63 0E 00                  call 0x14094d670
0086735C  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00867360  E9 3F F7 FF FF                  jmp 0x140866aa4
00867365  48 8B 0B                        mov rcx, qword ptr [rbx]
00867368  48 8B D6                        mov rdx, rsi
0086736B  E8 00 63 0E 00                  call 0x14094d670
00867370  48 89 43 48                     mov qword ptr [rbx + 0x48], rax
00867374  E9 2B F7 FF FF                  jmp 0x140866aa4
00867379  48 8B 0B                        mov rcx, qword ptr [rbx]
0086737C  48 8B D6                        mov rdx, rsi
0086737F  E8 EC 62 0E 00                  call 0x14094d670
00867384  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
00867388  E9 17 F7 FF FF                  jmp 0x140866aa4
0086738D  48 8B 0B                        mov rcx, qword ptr [rbx]
00867390  48 8B D6                        mov rdx, rsi
00867393  E8 D8 62 0E 00                  call 0x14094d670
00867398  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
0086739C  E9 03 F7 FF FF                  jmp 0x140866aa4
008673A1  48 8B 0B                        mov rcx, qword ptr [rbx]
008673A4  48 8B D6                        mov rdx, rsi
008673A7  E8 C4 62 0E 00                  call 0x14094d670
008673AC  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
008673B0  E9 EF F6 FF FF                  jmp 0x140866aa4
008673B5  48 8B 0B                        mov rcx, qword ptr [rbx]
008673B8  48 8B D6                        mov rdx, rsi
008673BB  E8 B0 62 0E 00                  call 0x14094d670
008673C0  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
008673C4  E9 DB F6 FF FF                  jmp 0x140866aa4
008673C9  0F 1F 00                        nop dword ptr [rax]
008673CC  51                              push rcx
008673CD  73 86                           jae 0x140867355
008673CF  00 75 70                        add byte ptr [rbp + 0x70], dh
008673D2  86 00                           xchg byte ptr [rax], al
008673D4  8D 73 86                        lea esi, [rbx - 0x7a]
008673D7  00 1B                           add byte ptr [rbx], bl
008673D9  71 86                           jno 0x140867361
008673DB  00 CF                           add bh, cl
008673DD  6F                              outsd dx, dword ptr [rsi]
008673DE  86 00                           xchg byte ptr [rax], al
008673E0  79 73                           jns 0x140867455
008673E2  86 00                           xchg byte ptr [rax], al
008673E4  1B 73 86                        sbb esi, dword ptr [rbx - 0x7a]
008673E7  00 7E 6A                        add byte ptr [rsi + 0x6a], bh
008673EA  86 00                           xchg byte ptr [rax], al
008673EC  94                              xchg esp, eax
008673ED  6A 86                           push -0x7a
008673EF  00 8C 6B 86 00 40 6B            add byte ptr [rbx + rbp*2 + 0x6b400086], cl
008673F6  86 00                           xchg byte ptr [rax], al
008673F8  65 73 86                        jae 0x140867381
008673FB  00 B4 6D 86 00 32 71            add byte ptr [rbp + rbp*2 + 0x71320086], dh
00867402  86 00                           xchg byte ptr [rax], al
00867404  A1 73 86 00 B5 73 86 00 A4      movabs eax, dword ptr [0xa4008673b5008673]
0086740D  6A 86                           push -0x7a
0086740F  00 00                           add byte ptr [rax], al
00867411  01 02                           add dword ptr [rdx], eax
00867413  03 02                           add eax, dword ptr [rdx]
00867415  04 05                           add al, 5
00867417  10 10                           adc byte ptr [rax], dl
00867419  06                              .byte 0x06
0086741A  10 10                           adc byte ptr [rax], dl
0086741C  10 10                           adc byte ptr [rax], dl
0086741E  07                              .byte 0x07
0086741F  08 08                           or byte ptr [rax], cl
00867421  08 08                           or byte ptr [rax], cl
00867423  08 08                           or byte ptr [rax], cl
00867425  08 08                           or byte ptr [rax], cl
00867427  08 08                           or byte ptr [rax], cl
00867429  09 0A                           or dword ptr [rdx], ecx
0086742B  09 10                           or dword ptr [rax], edx
0086742D  10 00                           adc byte ptr [rax], al
0086742F  08 0B                           or byte ptr [rbx], cl
00867431  08 0C 08                        or byte ptr [rax + rcx], cl
00867434  0D 08 0E 08 10                  or eax, 0x10080e08
00867439  0E                              .byte 0x0e
0086743A  08 0E                           or byte ptr [rsi], cl
0086743C  08 0E                           or byte ptr [rsi], cl
0086743E  08 0F                           or byte ptr [rdi], cl
00867440  08 0F                           or byte ptr [rdi], cl
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCallbackFillObjectContext(int a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if (a1 == 50) goto loc_00866A94;
    if (a1 == 28) goto loc_00866B40;
    if (a1 == 8) goto loc_00866B5A;
    if (a1 == 7) goto loc_00866B73;
    if (a1 == 29) goto loc_00866B8C;
    if (a1 > 49) goto loc_00866AA4;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 8809062 + *(unsigned __int8 *)(v_rip - 8809062 + (int)(a1) * 1 + 8811536) * 4 + 8811468))) + (v_rip - 8809062);
loc_00866A94:
    v_rdi = 0;
    if (*(unsigned __int64 *)(a2) != 0) goto loc_00866ABE;
loc_00866AA0:
    *(unsigned __int64 *)(a2 + 40) = 0;
loc_00866AA4:
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(a2);
loc_00866ABE:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2))) != 0x6B793032ULL) goto loc_00866AA0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 72)) == (*(unsigned __int64 *)(a2) + 72)) goto loc_00866AA0;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6885609, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6885563;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 6885551;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_00866B2B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 72)) == (*(unsigned __int64 *)(a2) + 72)) goto loc_00866B9B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 72) + 32)) == (*(unsigned __int64 *)(v_stack_p18))) goto loc_00866B97;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 72) + 32)) < (*(unsigned __int64 *)(v_stack_p18))) goto loc_00866B9B;
    goto loc_00866B2B;
loc_00866B40:
    v_rdi = 0;
    if (*(unsigned __int64 *)(v_stack_p8 + 8) != 0) goto loc_00866BF2;
loc_00866B51:
    *(unsigned __int64 *)(v_stack_p8 + 88) = 0;
    goto loc_00866AA4;
loc_00866B5A:
    v_rdi = 0;
    if (*(unsigned __int64 *)(a2) != 0) goto loc_00866C88;
loc_00866B6A:
    *(unsigned __int64 *)(v_stack_p8 + 56) = 0;
    goto loc_00866AA4;
loc_00866B73:
    v_rdi = 0;
    if (*(unsigned __int64 *)(a2) != 0) goto loc_00866D1E;
loc_00866B83:
    *(unsigned __int64 *)(v_stack_p8 + 48) = 0;
    goto loc_00866AA4;
loc_00866B8C:
    v_rdi = 0;
    *(unsigned __int64 *)(v_stack_p8 + 40) = 0;
    goto loc_00866AA4;
loc_00866B97:
loc_00866B9B:
    a1 = (*(unsigned __int64 *)(v_rip + 6885407)) & (-16);
    a2 = *(unsigned __int64 *)(v_rip + 6885407) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6885407))) & (2)) != 0) goto loc_008672E8;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6885407))) & (2)) != 0) goto loc_008672E8;
loc_00866BD3:
    result = KeAbPostRelease(v_rip + 6885358, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    goto loc_00866AA0;
loc_00866BF2:
    if ((*(unsigned int *)(result)) != 0x6B793032ULL) goto loc_00866B51;
    if ((*(unsigned __int64 *)(result + 72)) == (result + 72)) goto loc_00866B51;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6885293, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6885247;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 6885235;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_00866C67:
    if ((*(unsigned __int64 *)(result + 72)) == (result + 72)) goto loc_00866E67;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72) + 32)) == (*(unsigned __int64 *)(v_stack_p18))) goto loc_00866E63;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72) + 32)) < (*(unsigned __int64 *)(v_stack_p18))) goto loc_00866E67;
    goto loc_00866C67;
loc_00866C88:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)))) != 0x6B793032ULL) goto loc_00866B6A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72)) goto loc_00866B6A;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6885143, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6885097;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 6885085;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_00866CFD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72)) goto loc_00866EC2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72) + 32)) == (*(unsigned __int64 *)(v_stack_p18))) goto loc_00866EBE;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72) + 32)) < (*(unsigned __int64 *)(v_stack_p18))) goto loc_00866EC2;
    goto loc_00866CFD;
loc_00866D1E:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72)))) != 0x6B793032ULL) goto loc_00866B83;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72)) + 72)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72)) + 72)) goto loc_00866B83;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6884993, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6884947;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 6884935;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_00866D93:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72)) + 72)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72)) + 72)) goto loc_00866F1D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72)) + 72) + 32)) == (*(unsigned __int64 *)(v_stack_p18))) goto loc_00866F19;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72)) + 72)) + 72) + 32)) < (*(unsigned __int64 *)(v_stack_p18))) goto loc_00866F1D;
    goto loc_00866D93;
loc_00866E63:
loc_00866E67:
    a1 = (*(unsigned __int64 *)(v_rip + 6884691)) & (-16);
    a2 = *(unsigned __int64 *)(v_rip + 6884691) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6884691))) & (2)) != 0) goto loc_008672F9;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6884691))) & (2)) != 0) goto loc_008672F9;
loc_00866E9F:
    result = KeAbPostRelease(v_rip + 6884642, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    goto loc_00866B51;
loc_00866EBE:
loc_00866EC2:
    a1 = (*(unsigned __int64 *)(v_rip + 6884600)) & (-16);
    a2 = *(unsigned __int64 *)(v_rip + 6884600) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6884600))) & (2)) != 0) goto loc_0086730A;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6884600))) & (2)) != 0) goto loc_0086730A;
loc_00866EFA:
    result = KeAbPostRelease(v_rip + 6884551, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    goto loc_00866B6A;
loc_00866F19:
loc_00866F1D:
    a1 = (*(unsigned __int64 *)(v_rip + 6884509)) & (-16);
    a2 = *(unsigned __int64 *)(v_rip + 6884509) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6884509))) & (2)) != 0) goto loc_00867293;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6884509))) & (2)) != 0) goto loc_00867293;
loc_00866F55:
    result = KeAbPostRelease(v_rip + 6884460, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    goto loc_00866B83;
loc_00867293:
    result = ExfReleasePushLock(v_rip + 6883630, a2, a3, a4);
    goto loc_00866F55;
loc_008672E8:
    result = ExfReleasePushLock(v_rip + 6883545, a2, a3, a4);
    goto loc_00866BD3;
loc_008672F9:
    result = ExfReleasePushLock(v_rip + 6883528, a2, a3, a4);
    goto loc_00866E9F;
loc_0086730A:
    result = ExfReleasePushLock(v_rip + 6883511, a2, a3, a4);
    goto loc_00866EFA;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCallbackFillObjectContext(int32_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if (Arg1 == 50) goto loc_00866A94;
    if (Arg1 == 28) goto loc_00866B40;
    if (Arg1 == 8) goto loc_00866B5A;
    if (Arg1 == 7) goto loc_00866B73;
    if (Arg1 == 29) goto loc_00866B8C;
    if (Arg1 > 49) goto loc_00866AA4;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x866A66 + *(uint8_t *)(v_rip - 0x866A66 + (int32_t)(Arg1) * 1 + 0x867410) * 4 + 0x8673CC))) + (v_rip - 8809062);
loc_00866A94:
    local_rdi = 0;
    if (*(uint64_t *)(arg2) != 0) goto loc_00866ABE;
loc_00866AA0:
    *(uint64_t *)(arg2 + 0x28) = 0;
loc_00866AA4:
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(arg2);
loc_00866ABE:
    if ((*(uint32_t *)(*(uint64_t *)(arg2))) != 0x6B793032ULL) goto loc_00866AA0;
    if ((*(uint64_t *)(*(uint64_t *)(arg2) + 0x48)) == (*(uint64_t *)(arg2) + 72)) goto loc_00866AA0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6885609, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6885563;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 6885551;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_00866B2B:
    if ((*(uint64_t *)(*(uint64_t *)(arg2) + 0x48)) == (*(uint64_t *)(arg2) + 72)) goto loc_00866B9B;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x48) + 0x20)) == (*(uint64_t *)(v_stack_p18))) goto loc_00866B97;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x48) + 0x20)) < (*(uint64_t *)(v_stack_p18))) goto loc_00866B9B;
    goto loc_00866B2B;
loc_00866B40:
    local_rdi = 0;
    if (*(uint64_t *)(v_stack_p8 + 0x8) != 0) goto loc_00866BF2;
loc_00866B51:
    *(uint64_t *)(v_stack_p8 + 0x58) = 0;
    goto loc_00866AA4;
loc_00866B5A:
    local_rdi = 0;
    if (*(uint64_t *)(arg2) != 0) goto loc_00866C88;
loc_00866B6A:
    *(uint64_t *)(v_stack_p8 + 0x38) = 0;
    goto loc_00866AA4;
loc_00866B73:
    local_rdi = 0;
    if (*(uint64_t *)(arg2) != 0) goto loc_00866D1E;
loc_00866B83:
    *(uint64_t *)(v_stack_p8 + 0x30) = 0;
    goto loc_00866AA4;
loc_00866B8C:
    local_rdi = 0;
    *(uint64_t *)(v_stack_p8 + 0x28) = 0;
    goto loc_00866AA4;
loc_00866B97:
loc_00866B9B:
    Arg1 = (*(uint64_t *)(v_rip + 0x69101F)) & (-16);
    Arg2 = *(uint64_t *)(v_rip + 0x69101F) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x69101F))) & (2)) != 0) goto loc_008672E8;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x69101F))) & (2)) != 0) goto loc_008672E8;
loc_00866BD3:
    result = KeAbPostRelease(v_rip + 6885358, Arg2, Arg3, a4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, a4);
    goto loc_00866AA0;
loc_00866BF2:
    if ((*(uint32_t *)(result)) != 0x6B793032ULL) goto loc_00866B51;
    if ((*(uint64_t *)(result + 0x48)) == (result + 72)) goto loc_00866B51;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6885293, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6885247;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 6885235;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_00866C67:
    if ((*(uint64_t *)(result + 0x48)) == (result + 72)) goto loc_00866E67;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x48) + 0x20)) == (*(uint64_t *)(v_stack_p18))) goto loc_00866E63;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x48) + 0x20)) < (*(uint64_t *)(v_stack_p18))) goto loc_00866E67;
    goto loc_00866C67;
loc_00866C88:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)))) != 0x6B793032ULL) goto loc_00866B6A;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x48)) == (*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 72)) goto loc_00866B6A;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6885143, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6885097;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 6885085;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_00866CFD:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x48)) == (*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 72)) goto loc_00866EC2;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x48) + 0x20)) == (*(uint64_t *)(v_stack_p18))) goto loc_00866EBE;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x48) + 0x20)) < (*(uint64_t *)(v_stack_p18))) goto loc_00866EC2;
    goto loc_00866CFD;
loc_00866D1E:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x48)))) != 0x6B793032ULL) goto loc_00866B83;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x48)) + 0x48)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x48)) + 72)) goto loc_00866B83;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6884993, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6884947;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 6884935;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_00866D93:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x48)) + 0x48)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x48)) + 72)) goto loc_00866F1D;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x48)) + 0x48) + 0x20)) == (*(uint64_t *)(v_stack_p18))) goto loc_00866F19;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48)) + 0x48)) + 0x48) + 0x20)) < (*(uint64_t *)(v_stack_p18))) goto loc_00866F1D;
    goto loc_00866D93;
loc_00866E63:
loc_00866E67:
    Arg1 = (*(uint64_t *)(v_rip + 0x690D53)) & (-16);
    Arg2 = *(uint64_t *)(v_rip + 0x690D53) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x690D53))) & (2)) != 0) goto loc_008672F9;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x690D53))) & (2)) != 0) goto loc_008672F9;
loc_00866E9F:
    result = KeAbPostRelease(v_rip + 6884642, Arg2, Arg3, a4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, a4);
    goto loc_00866B51;
loc_00866EBE:
loc_00866EC2:
    Arg1 = (*(uint64_t *)(v_rip + 0x690CF8)) & (-16);
    Arg2 = *(uint64_t *)(v_rip + 0x690CF8) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x690CF8))) & (2)) != 0) goto loc_0086730A;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x690CF8))) & (2)) != 0) goto loc_0086730A;
loc_00866EFA:
    result = KeAbPostRelease(v_rip + 6884551, Arg2, Arg3, a4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, a4);
    goto loc_00866B6A;
loc_00866F19:
loc_00866F1D:
    Arg1 = (*(uint64_t *)(v_rip + 0x690C9D)) & (-16);
    Arg2 = *(uint64_t *)(v_rip + 0x690C9D) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x690C9D))) & (2)) != 0) goto loc_00867293;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x690C9D))) & (2)) != 0) goto loc_00867293;
loc_00866F55:
    result = KeAbPostRelease(v_rip + 6884460, Arg2, Arg3, a4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, a4);
    goto loc_00866B83;
loc_00867293:
    result = ExfReleasePushLock(v_rip + 6883630, Arg2, Arg3, a4);
    goto loc_00866F55;
loc_008672E8:
    result = ExfReleasePushLock(v_rip + 6883545, Arg2, Arg3, a4);
    goto loc_00866BD3;
loc_008672F9:
    result = ExfReleasePushLock(v_rip + 6883528, Arg2, Arg3, a4);
    goto loc_00866E9F;
loc_0086730A:
    result = ExfReleasePushLock(v_rip + 6883511, Arg2, Arg3, a4);
    goto loc_00866EFA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `W` |
| `Arg2` | `+ 0x30` | `64` | `W` |
| `Arg2` | `+ 0x38` | `64` | `W` |
| `Arg2` | `+ 0x58` | `64` | `W` |
| `Arg3` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00866A10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
