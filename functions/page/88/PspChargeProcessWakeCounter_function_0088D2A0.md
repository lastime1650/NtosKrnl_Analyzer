# PspChargeProcessWakeCounter

- RVA: `0x0088D2A0`–`0x0088D749` (길이 `1,193` bytes)
- VA: `0x000000014088D2A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007D45C`
- 디코드: `278`개 명령, `1,193/1,193` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0088D31B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0088D33C` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0088D3E5` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0088D3ED` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0088D3F7` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0088D46E` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0088D5B7` → [PspIsProcessInJob](../A2/PspIsProcessInJob_function_00A23A58.md) (function, `0x00A23A58`)
- `0x0088D63F` → [EtwTraceWakeCounter](EtwTraceWakeCounter_function_0088B73C.md) (function, `0x0088B73C`)
- `0x0088D658` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x0088D67D` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x0088D6A9` → [EtwTraceWakeEvent](../70/EtwTraceWakeEvent_function_007042C8.md) (function, `0x007042C8`)
- `0x0088D6E3` → [PspChargeJobWakeCounter](../9D/PspChargeJobWakeCounter_function_009D5D20.md) (function, `0x009D5D20`)
- `0x0088D714` → [EtwTraceWakeCounter](EtwTraceWakeCounter_function_0088B73C.md) (function, `0x0088B73C`)

### Direct callers
- [PsReleaseProcessWakeCounter](PsReleaseProcessWakeCounter_function_0088B940.md) at `0x0088B978`
- [AlpcMessageCleanupProcedure](AlpcMessageCleanupProcedure_function_0088BBA0.md) at `0x0088BC2C`
- [AlpcMessageCleanupProcedure](AlpcMessageCleanupProcedure_function_0088BBA0.md) at `0x0088BC75`
- [PsChargeProcessWakeCounter](PsChargeProcessWakeCounter_function_0088BCD0.md) at `0x0088BD1A`
- [AlpcpSendMessage](AlpcpSendMessage_function_0088BD40.md) at `0x0088C458`
- [AlpcpSendMessage](AlpcpSendMessage_function_0088BD40.md) at `0x0088C4A2`
- [sub_0088E1DC](Unknown_function_0088E1DC.md) at `0x0088E270`
- [sub_0088E1DC](Unknown_function_0088E1DC.md) at `0x0088EC55`
- [PspAdjustKeepAliveCountProcess](../A7/PspAdjustKeepAliveCountProcess_function_00A7EE04.md) at `0x00A7EE35`

### Static image references
- `0x0088D444` → RVA `0x00FC6B10` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x0088D31B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0088D33C` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0088D3E5` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0088D3ED` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0088D3F7` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0088D46E` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0088D658` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (`PAGE` → `.text`)
  - `0x0088D67D` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0088D2A0  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0088D2A5  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0088D2AA  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0088D2AE  53                              push rbx
0088D2AF  55                              push rbp
0088D2B0  56                              push rsi
0088D2B1  57                              push rdi
0088D2B2  41 54                           push r12
0088D2B4  41 55                           push r13
0088D2B6  41 56                           push r14
0088D2B8  41 57                           push r15
0088D2BA  48 83 EC 78                     sub rsp, 0x78
0088D2BE  4C 63 A4 24 E0 00 00 00         movsxd r12, dword ptr [rsp + 0xe0]
0088D2C6  48 8D B1 C8 01 00 00            lea rsi, [rcx + 0x1c8]
0088D2CD  33 C0                           xor eax, eax
0088D2CF  44 89 44 24 4C                  mov dword ptr [rsp + 0x4c], r8d
0088D2D4  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0088D2D8  48 8B F9                        mov rdi, rcx
0088D2DB  8B C2                           mov eax, edx
0088D2DD  C7 44 24 48 01 00 00 00         mov dword ptr [rsp + 0x48], 1
0088D2E5  83 E0 02                        and eax, 2
0088D2E8  C6 84 24 C0 00 00 00 00         mov byte ptr [rsp + 0xc0], 0
0088D2F0  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0088D2F4  48 8B CE                        mov rcx, rsi
0088D2F7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0088D300  41 0F 95 C5                     setne r13b
0088D304  45 33 C0                        xor r8d, r8d
0088D307  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
0088D30C  33 D2                           xor edx, edx
0088D30E  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0088D313  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0088D31A  90                              nop
0088D31B  E8 10 2F 98 FF                  call 0x140210230
0088D320  48 8B D8                        mov rbx, rax
0088D323  B9 11 00 00 00                  mov ecx, 0x11
0088D328  33 C0                           xor eax, eax
0088D32A  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
0088D32F  74 10                           je 0x14088d341
0088D331  4C 8B CE                        mov r9, rsi
0088D334  4C 8B C3                        mov r8, rbx
0088D337  33 D2                           xor edx, edx
0088D339  48 8B CE                        mov rcx, rsi
0088D33C  E8 0B 31 98 FF                  call 0x14021044c
0088D341  48 85 DB                        test rbx, rbx
0088D344  74 04                           je 0x14088d34a
0088D346  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0088D34A  4C 8B BF A0 02 00 00            mov r15, qword ptr [rdi + 0x2a0]
0088D351  45 0F B6 F5                     movzx r14d, r13b
0088D355  0F B6 AC 24 E8 00 00 00         movzx ebp, byte ptr [rsp + 0xe8]
0088D35D  4D 85 FF                        test r15, r15
0088D360  0F 85 19 01 00 00               jne 0x14088d47f
0088D366  45 32 ED                        xor r13b, r13b
0088D369  40 84 ED                        test bpl, bpl
0088D36C  74 13                           je 0x14088d381
0088D36E  45 84 ED                        test r13b, r13b
0088D371  75 0E                           jne 0x14088d381
0088D373  48 83 BF 20 07 00 00 00         cmp qword ptr [rdi + 0x720], 0
0088D37B  0F 84 CB 01 00 00               je 0x14088d54c
0088D381  45 84 F6                        test r14b, r14b
0088D384  0F 84 3E 01 00 00               je 0x14088d4c8
0088D38A  44 8B 8C 24 D0 00 00 00         mov r9d, dword ptr [rsp + 0xd0]
0088D392  48 8D 8F 4C 07 00 00            lea rcx, [rdi + 0x74c]
0088D399  C7 44 24 4C 07 00 00 00         mov dword ptr [rsp + 0x4c], 7
0088D3A1  41 8B C4                        mov eax, r12d
0088D3A4  F0 0F C1 01                     lock xadd dword ptr [rcx], eax
0088D3A8  42 8D 0C 20                     lea ecx, [rax + r12]
0088D3AC  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
0088D3B1  44 8B C1                        mov r8d, ecx
0088D3B4  8B D1                           mov edx, ecx
0088D3B6  41 C1 E8 1F                     shr r8d, 0x1f
0088D3BA  0F BA F2 1F                     btr edx, 0x1f
0088D3BE  85 C9                           test ecx, ecx
0088D3C0  41 0F B6 D8                     movzx ebx, r8b
0088D3C4  0F 49 D1                        cmovns edx, ecx
0088D3C7  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
0088D3CB  45 84 F6                        test r14b, r14b
0088D3CE  0F 84 0C 01 00 00               je 0x14088d4e0
0088D3D4  B8 11 00 00 00                  mov eax, 0x11
0088D3D9  33 C9                           xor ecx, ecx
0088D3DB  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
0088D3E0  74 08                           je 0x14088d3ea
0088D3E2  48 8B CE                        mov rcx, rsi
0088D3E5  E8 56 60 9D FF                  call 0x140263440
0088D3EA  48 8B CE                        mov rcx, rsi
0088D3ED  E8 0E 42 A5 FF                  call 0x1402e1600
0088D3F2  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0088D3F7  E8 F4 1B 9D FF                  call 0x14025eff0
0088D3FC  80 BC 24 C0 00 00 00 00         cmp byte ptr [rsp + 0xc0], 0
0088D404  0F 85 55 02 00 00               jne 0x14088d65f
0088D40A  8B 74 24 44                     mov esi, dword ptr [rsp + 0x44]
0088D40E  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0088D416  48 85 C0                        test rax, rax
0088D419  74 02                           je 0x14088d41d
0088D41B  89 30                           mov dword ptr [rax], esi
0088D41D  84 DB                           test bl, bl
0088D41F  0F 85 8E 02 00 00               jne 0x14088d6b3
0088D425  45 84 ED                        test r13b, r13b
0088D428  0F 85 85 02 00 00               jne 0x14088d6b3
0088D42E  44 8B AC 24 D0 00 00 00         mov r13d, dword ptr [rsp + 0xd0]
0088D436  49 8B DC                        mov rbx, r12
0088D439  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
0088D43E  0F 84 C9 01 00 00               je 0x14088d60d
0088D444  F7 05 C2 96 73 00 00 20 00 00   test dword ptr [rip + 0x7396c2], 0x2000
0088D44E  0F 85 99 02 00 00               jne 0x14088d6ed
0088D454  40 84 ED                        test bpl, bpl
0088D457  0F 84 E7 01 00 00               je 0x14088d644
0088D45D  BA 50 73 57 6B                  mov edx, 0x6b577350
0088D462  48 8B CF                        mov rcx, rdi
0088D465  45 85 E4                        test r12d, r12d
0088D468  0F 8E EA 01 00 00               jle 0x14088d658
0088D46E  E8 9D 32 98 FF                  call 0x140210710
0088D473  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
0088D477  48 0B C7                        or rax, rdi
0088D47A  E9 C7 01 00 00                  jmp 0x14088d646
0088D47F  41 8B 8F 10 06 00 00            mov ecx, dword ptr [r15 + 0x610]
0088D486  0F BA E1 0C                     bt ecx, 0xc
0088D48A  0F 83 D6 FE FF FF               jae 0x14088d366
0088D490  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0088D499  44 8B 54 24 50                  mov r10d, dword ptr [rsp + 0x50]
0088D49E  4C 8B 88 B8 00 00 00            mov r9, qword ptr [rax + 0xb8]
0088D4A5  40 84 ED                        test bpl, bpl
0088D4A8  0F 84 70 02 00 00               je 0x14088d71e
0088D4AE  45 85 D2                        test r10d, r10d
0088D4B1  74 6E                           je 0x14088d521
0088D4B3  0F BA E1 17                     bt ecx, 0x17
0088D4B7  73 68                           jae 0x14088d521
0088D4B9  45 85 E4                        test r12d, r12d
0088D4BC  7E 63                           jle 0x14088d521
0088D4BE  32 DB                           xor bl, bl
0088D4C0  45 32 ED                        xor r13b, r13b
0088D4C3  E9 0C FF FF FF                  jmp 0x14088d3d4
0088D4C8  4C 63 8C 24 D0 00 00 00         movsxd r9, dword ptr [rsp + 0xd0]
0088D4D0  49 8D 89 CA 01 00 00            lea rcx, [r9 + 0x1ca]
0088D4D7  48 8D 0C 8F                     lea rcx, [rdi + rcx*4]
0088D4DB  E9 C1 FE FF FF                  jmp 0x14088d3a1
0088D4E0  48 83 BF 20 07 00 00 00         cmp qword ptr [rdi + 0x720], 0
0088D4E8  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
0088D4EC  0F 84 E2 FE FF FF               je 0x14088d3d4
0088D4F2  41 8B C9                        mov ecx, r9d
0088D4F5  41 B9 01 00 00 00               mov r9d, 1
0088D4FB  41 D3 E1                        shl r9d, cl
0088D4FE  45 85 E4                        test r12d, r12d
0088D501  7E 50                           jle 0x14088d553
0088D503  44 85 8F 44 07 00 00            test dword ptr [rdi + 0x744], r9d
0088D50A  74 65                           je 0x14088d571
0088D50C  83 FA 01                        cmp edx, 1
0088D50F  75 60                           jne 0x14088d571
0088D511  88 94 24 C0 00 00 00            mov byte ptr [rsp + 0xc0], dl
0088D518  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
0088D51C  E9 B3 FE FF FF                  jmp 0x14088d3d4
0088D521  8B 9C 24 C8 00 00 00            mov ebx, dword ptr [rsp + 0xc8]
0088D528  F6 C3 01                        test bl, 1
0088D52B  75 4E                           jne 0x14088d57b
0088D52D  41 8B 81 F0 01 00 00            mov eax, dword ptr [r9 + 0x1f0]
0088D534  A8 40                           test al, 0x40
0088D536  75 09                           jne 0x14088d541
0088D538  45 85 D2                        test r10d, r10d
0088D53B  0F 85 A8 00 00 00               jne 0x14088d5e9
0088D541  45 32 F6                        xor r14b, r14b
0088D544  41 B5 01                        mov r13b, 1
0088D547  E9 1D FE FF FF                  jmp 0x14088d369
0088D54C  32 DB                           xor bl, bl
0088D54E  E9 81 FE FF FF                  jmp 0x14088d3d4
0088D553  44 85 8F 48 07 00 00            test dword ptr [rdi + 0x748], r9d
0088D55A  74 15                           je 0x14088d571
0088D55C  85 D2                           test edx, edx
0088D55E  75 11                           jne 0x14088d571
0088D560  C6 84 24 C0 00 00 00 01         mov byte ptr [rsp + 0xc0], 1
0088D568  89 54 24 44                     mov dword ptr [rsp + 0x44], edx
0088D56C  E9 63 FE FF FF                  jmp 0x14088d3d4
0088D571  C6 84 24 C0 00 00 00 00         mov byte ptr [rsp + 0xc0], 0
0088D579  EB 9D                           jmp 0x14088d518
0088D57B  49 8B 81 A0 02 00 00            mov rax, qword ptr [r9 + 0x2a0]
0088D582  48 85 C0                        test rax, rax
0088D585  74 A6                           je 0x14088d52d
0088D587  49 8B 81 A0 02 00 00            mov rax, qword ptr [r9 + 0x2a0]
0088D58E  48 8B 88 20 05 00 00            mov rcx, qword ptr [rax + 0x520]
0088D595  49 8B 87 20 05 00 00            mov rax, qword ptr [r15 + 0x520]
0088D59C  48 3B C8                        cmp rcx, rax
0088D59F  75 8C                           jne 0x14088d52d
0088D5A1  8B 8C 24 D0 00 00 00            mov ecx, dword ptr [rsp + 0xd0]
0088D5A8  41 BB 01 00 00 00               mov r11d, 1
0088D5AE  41 D3 E3                        shl r11d, cl
0088D5B1  49 8B D7                        mov rdx, r15
0088D5B4  49 8B C9                        mov rcx, r9
0088D5B7  E8 9C 64 19 00                  call 0x140a23a58
0088D5BC  3D 24 01 00 00                  cmp eax, 0x124
0088D5C1  75 0D                           jne 0x14088d5d0
0088D5C3  44 85 9A A0 04 00 00            test dword ptr [rdx + 0x4a0], r11d
0088D5CA  0F 85 5A 01 00 00               jne 0x14088d72a
0088D5D0  49 8B 87 20 05 00 00            mov rax, qword ptr [r15 + 0x520]
0088D5D7  48 3B D0                        cmp rdx, rax
0088D5DA  0F 84 4D FF FF FF               je 0x14088d52d
0088D5E0  48 8B 92 18 05 00 00            mov rdx, qword ptr [rdx + 0x518]
0088D5E7  EB CB                           jmp 0x14088d5b4
0088D5E9  C7 44 24 4C 07 00 00 00         mov dword ptr [rsp + 0x4c], 7
0088D5F1  C7 44 24 48 05 00 00 00         mov dword ptr [rsp + 0x48], 5
0088D5F9  85 DB                           test ebx, ebx
0088D5FB  0F 88 3B 01 00 00               js 0x14088d73c
0088D601  45 0F B6 F5                     movzx r14d, r13b
0088D605  41 B5 01                        mov r13b, 1
0088D608  E9 5C FD FF FF                  jmp 0x14088d369
0088D60D  F7 05 F9 94 73 00 00 02 00 00   test dword ptr [rip + 0x7394f9], 0x200
0088D617  74 2B                           je 0x14088d644
0088D619  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
0088D621  45 33 C9                        xor r9d, r9d
0088D624  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0088D629  45 8B C5                        mov r8d, r13d
0088D62C  33 C0                           xor eax, eax
0088D62E  41 0F B6 D6                     movzx edx, r14b
0088D632  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
0088D637  48 8B CF                        mov rcx, rdi
0088D63A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0088D63F  E8 F8 E0 FF FF                  call 0x14088b73c
0088D644  33 C0                           xor eax, eax
0088D646  48 83 C4 78                     add rsp, 0x78
0088D64A  41 5F                           pop r15
0088D64C  41 5E                           pop r14
0088D64E  41 5D                           pop r13
0088D650  41 5C                           pop r12
0088D652  5F                              pop rdi
0088D653  5E                              pop rsi
0088D654  5D                              pop rbp
0088D655  5B                              pop rbx
0088D656  C3                              ret
0088D657  CC                              int3
0088D658  E8 43 68 9D FF                  call 0x140263ea0
0088D65D  EB E5                           jmp 0x14088d644
0088D65F  33 C0                           xor eax, eax
0088D661  48 8D 8F 20 07 00 00            lea rcx, [rdi + 0x720]
0088D668  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0088D66C  45 33 C9                        xor r9d, r9d
0088D66F  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0088D673  45 33 C0                        xor r8d, r8d
0088D676  33 D2                           xor edx, edx
0088D678  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0088D67D  E8 8E 36 E2 FF                  call 0x1406b0d10
0088D682  F7 05 84 94 73 00 00 04 00 00   test dword ptr [rip + 0x739484], 0x400
0088D68C  8B 74 24 44                     mov esi, dword ptr [rsp + 0x44]
0088D690  0F 84 78 FD FF FF               je 0x14088d40e
0088D696  83 FE 01                        cmp esi, 1
0088D699  0F 85 6F FD FF FF               jne 0x14088d40e
0088D69F  8B 94 24 D0 00 00 00            mov edx, dword ptr [rsp + 0xd0]
0088D6A6  48 8B CF                        mov rcx, rdi
0088D6A9  E8 1A 6C E7 FF                  call 0x1407042c8
0088D6AE  E9 5B FD FF FF                  jmp 0x14088d40e
0088D6B3  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
0088D6BB  4D 8B CC                        mov r9, r12
0088D6BE  44 8B AC 24 D0 00 00 00         mov r13d, dword ptr [rsp + 0xd0]
0088D6C6  33 D2                           xor edx, edx
0088D6C8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0088D6CD  45 8B C5                        mov r8d, r13d
0088D6D0  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0088D6D4  49 8B CF                        mov rcx, r15
0088D6D7  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
0088D6DC  49 8B DC                        mov rbx, r12
0088D6DF  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0088D6E3  E8 38 86 14 00                  call 0x1409d5d20
0088D6E8  E9 4C FD FF FF                  jmp 0x14088d439
0088D6ED  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
0088D6F5  4C 8B CB                        mov r9, rbx
0088D6F8  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0088D6FD  45 8B C5                        mov r8d, r13d
0088D700  48 63 C6                        movsxd rax, esi
0088D703  48 8B CF                        mov rcx, rdi
0088D706  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
0088D70B  41 0F B6 D6                     movzx edx, r14b
0088D70F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0088D714  E8 23 E0 FF FF                  call 0x14088b73c
0088D719  E9 36 FD FF FF                  jmp 0x14088d454
0088D71E  8B 9C 24 C8 00 00 00            mov ebx, dword ptr [rsp + 0xc8]
0088D725  E9 03 FE FF FF                  jmp 0x14088d52d
0088D72A  45 0F B6 F5                     movzx r14d, r13b
0088D72E  45 85 E4                        test r12d, r12d
0088D731  0F 8F 87 FD FF FF               jg 0x14088d4be
0088D737  E9 F1 FD FF FF                  jmp 0x14088d52d
0088D73C  C7 44 24 48 07 00 00 00         mov dword ptr [rsp + 0x48], 7
0088D744  E9 B8 FE FF FF                  jmp 0x14088d601
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspChargeProcessWakeCounter(__int64 a1, int a2, int a3, __int64 a4, unsigned int a5, unsigned __int8 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned __int8 v_stack_p8;
    unsigned int v_stack_pC8;
    unsigned int v_stack_pD0;
    unsigned __int64 v_stack_pD8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (120);
    result = 0;
    v_stack_m6C = a3;
    v_stack_m74 = 0;
    v_stack_m70 = 1;
    result = (unsigned int)(((unsigned int)(a2)) & (2));
    v_stack_p8 = 0;
    v_stack_m68 = (unsigned int)(result);
    v_r13 = (condition_is_not_equal) ? 1 : 0;
    a3 = 0;
    v_stack_m78 = 0;
    a2 = 0;
    v_stack_m60 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeAbPreAcquire(a1 + 456, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1 + 456;
        a3 = 0;
        a2 = 0;
        a1 = a1 + 456;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(a1 + 672) != 0) goto loc_0088D47F;
loc_0088D366:
    v_r13 = 0;
loc_0088D369:
    if (a6 == 0) goto loc_0088D381;
    if (0 != 0) goto loc_0088D381;
    if ((*(unsigned __int64 *)(a1 + 1824)) == 0) goto loc_0088D54C;
loc_0088D381:
    if ((unsigned __int8)((unsigned __int8)(v_r13)) == 0) goto loc_0088D4C8;
    v_stack_m6C = 7;
loc_0088D3A1:
    v_stack_m78 = 1;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((int)(a5))) + (int)(a5) * 1))) >> (31));
    a2 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((int)(a5))) + (int)(a5) * 1));
    if (!sign_flag) { a2 = (unsigned int)((unsigned int)((unsigned int)((int)(a5))) + (int)(a5) * 1); }
    v_stack_m74 = a2;
    if ((unsigned __int8)((unsigned __int8)(v_r13)) == 0) goto loc_0088D4E0;
loc_0088D3D4:
    a1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = a1 + 456;
        result = ExfReleasePushLockShared(a1, a2, a3, (unsigned int)(v_stack_p18));
    }
    result = KeAbPostRelease(a1 + 456, a2, a3, (unsigned int)(v_stack_p18));
    result = KeLeaveCriticalRegionThread(v_stack_m60, a2, a3, (unsigned int)(v_stack_p18));
    if (v_stack_p8 != 0) goto loc_0088D65F;
loc_0088D40E:
    if (a7 != 0) {
        *(unsigned int *)(a7) = (unsigned int)((unsigned int)(v_stack_m74));
    }
    if ((unsigned __int8)((unsigned __int8)(a3)) != 0) goto loc_0088D6B3;
    if (0 != 0) goto loc_0088D6B3;
loc_0088D439:
    if (v_stack_m78 == 0) goto loc_0088D60D;
    if (((*(unsigned int *)(v_rip + 7575234)) & (0x2000ULL)) != 0) goto loc_0088D6ED;
loc_0088D454:
    if (a6 == 0) goto loc_0088D644;
    if (condition_is_less_or_equal) goto loc_0088D658;
    result = ObfReferenceObjectWithTag(a1, (unsigned int)(0x6B577350ULL), a3, (unsigned int)(v_stack_p18));
    result = ((unsigned int)(v_stack_m6C)) | (a1);
    goto loc_0088D646;
loc_0088D47F:
    if (condition_is_above_or_equal) goto loc_0088D366;
    if (a6 == 0) goto loc_0088D71E;
    if ((unsigned int)((unsigned int)(v_stack_m68)) == 0) goto loc_0088D521;
    if (condition_is_above_or_equal) goto loc_0088D521;
    if (condition_is_less_or_equal) goto loc_0088D521;
loc_0088D4BE:
    v_rbx = 0;
    v_r13 = 0;
    goto loc_0088D3D4;
loc_0088D4C8:
    goto loc_0088D3A1;
loc_0088D4E0:
    v_stack_m74 = (unsigned int)((unsigned int)(0x6B577350ULL));
    if ((*(unsigned __int64 *)(a1 + 1824)) == 0) goto loc_0088D3D4;
    a4 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((int)(v_stack_p18))))));
    if (condition_is_less_or_equal) goto loc_0088D553;
    if (((*(unsigned int *)(a1 + 1860)) & ((unsigned int)(a4))) == 0) goto loc_0088D571;
    if (((unsigned int)((unsigned int)(0x6B577350ULL))) != 1) goto loc_0088D571;
    v_stack_p8 = (unsigned __int8)((unsigned int)(0x6B577350ULL));
loc_0088D518:
    v_stack_m74 = (unsigned int)((unsigned int)(0x6B577350ULL));
    goto loc_0088D3D4;
loc_0088D521:
    if ((((unsigned __int8)((unsigned int)(v_stack_p10))) & (1)) != 0) goto loc_0088D57B;
loc_0088D52D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4 + 496)))) & (64)) != 0) goto loc_0088D541;
    if ((unsigned int)((unsigned int)(v_stack_m68)) != 0) goto loc_0088D5E9;
loc_0088D541:
    v_r14 = 0;
    goto loc_0088D369;
loc_0088D54C:
    v_rbx = 0;
    goto loc_0088D3D4;
loc_0088D553:
    if (((*(unsigned int *)(a1 + 1864)) & ((unsigned int)(a4))) == 0) goto loc_0088D571;
    if ((unsigned int)((unsigned int)(0x6B577350ULL)) != 0) goto loc_0088D571;
    v_stack_p8 = 1;
    v_stack_m74 = (unsigned int)((unsigned int)(0x6B577350ULL));
    goto loc_0088D3D4;
loc_0088D571:
    v_stack_p8 = 0;
    goto loc_0088D518;
loc_0088D57B:
    if (*(unsigned __int64 *)(a4 + 672) == 0) goto loc_0088D52D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 672) + 1312)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 672) + 1312))) goto loc_0088D52D;
    v_r11 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(v_stack_p18))));
loc_0088D5B4:
    result = PspIsProcessInJob(a4, *(unsigned __int64 *)(a1 + 672), a3, a4);
    if (((unsigned int)(result)) != 292) goto loc_0088D5D0;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 672) + 1184)) & ((unsigned int)(v_r11))) != 0) goto loc_0088D72A;
loc_0088D5D0:
    if ((*(unsigned __int64 *)(a1 + 672)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 672) + 1312))) goto loc_0088D52D;
    goto loc_0088D5B4;
loc_0088D5E9:
    v_stack_m6C = 7;
    v_stack_m70 = 5;
    if (sign_flag) goto loc_0088D73C;
loc_0088D601:
    goto loc_0088D369;
loc_0088D60D:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 672) + 1312);
    if (((*(unsigned int *)(v_rip + 7574777)) & (512)) != 0) {
        result = v_stack_p20;
        a4 = 0;
        v_stack_m88 = result;
        a3 = 1;
        result = 0;
        a2 = 1;
        v_stack_m90 = a1;
        a1 = a1;
        v_stack_m98 = 0;
        result = EtwTraceWakeCounter(a1, a2, a3, a4);
    }
    result = 0;
loc_0088D646:
    v_rsp = (v_rsp) + (120);
    return result;
loc_0088D658:
    result = ObDereferenceObjectDeferDeleteWithTag(a1, a2, a3, a4);
    goto loc_0088D644;
loc_0088D65F:
    result = 0;
    v_stack_p30 = 0;
    a4 = 0;
    v_stack_p28 = 0;
    a3 = 0;
    a2 = 0;
    v_stack_p20 = 0;
    result = ZwUpdateWnfStateData(a1 + 1824, a2, a3, a4);
    if (((*(unsigned int *)(v_rip + 7574660)) & (0x400ULL)) == 0) goto loc_0088D40E;
    if (((unsigned int)((unsigned int)(v_stack_p44))) != 1) goto loc_0088D40E;
    result = EtwTraceWakeEvent(a1, (unsigned int)(v_stack_pD0), a3, a4);
    goto loc_0088D40E;
loc_0088D6B3:
    a2 = 0;
    v_stack_p30 = v_stack_pD8;
    v_stack_p28 = a1;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p48));
    result = PspChargeJobWakeCounter(*(unsigned __int64 *)(a1 + 672), a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_pD0))), (int)(a5));
    goto loc_0088D439;
loc_0088D6ED:
    v_stack_p30 = v_stack_pD8;
    v_stack_p28 = a1;
    v_stack_p20 = (int)((unsigned int)((unsigned int)(v_stack_p44)));
    result = EtwTraceWakeCounter(a1, 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_pD0))), (int)(a5));
    goto loc_0088D454;
loc_0088D71E:
    goto loc_0088D52D;
loc_0088D72A:
    if (condition_is_greater) goto loc_0088D4BE;
    goto loc_0088D52D;
loc_0088D73C:
    v_stack_p48 = 7;
    goto loc_0088D601;
}
```

## 5. (Beta) C Style

```c
int64_t PspChargeProcessWakeCounter(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint8_t Arg6, int64_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint8_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint8_t v_stack_p8;
    uint32_t v_stack_pC8;
    uint32_t v_stack_pD0;
    uint64_t v_stack_pD8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (120);
    result = 0;
    v_stack_m6C = Arg3;
    v_stack_m74 = 0;
    v_stack_m70 = 1;
    result = (uint32_t)(((uint32_t)(Arg2)) & (2));
    v_stack_p8 = 0;
    v_stack_m68 = (uint32_t)(result);
    local_r13 = (condition_is_not_equal) ? 1 : 0;
    Arg3 = 0;
    v_stack_m78 = 0;
    Arg2 = 0;
    v_stack_m60 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeAbPreAcquire(Arg1 + 456, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = Arg1 + 456;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1 + 456;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(arg1 + 0x2A0) != 0) goto loc_0088D47F;
loc_0088D366:
    local_r13 = 0;
loc_0088D369:
    if (Arg6 == 0) goto loc_0088D381;
    if (0 != 0) goto loc_0088D381;
    if ((*(uint64_t *)(arg1 + 0x720)) == 0) goto loc_0088D54C;
loc_0088D381:
    if ((uint8_t)((uint8_t)(local_r13)) == 0) goto loc_0088D4C8;
    v_stack_m6C = 7;
loc_0088D3A1:
    v_stack_m78 = 1;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((int32_t)(Arg5))) + (int32_t)(Arg5) * 1))) >> (31));
    Arg2 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((int32_t)(Arg5))) + (int32_t)(Arg5) * 1));
    if (!sign_flag) { Arg2 = (uint32_t)((uint32_t)((uint32_t)((int32_t)(Arg5))) + (int32_t)(Arg5) * 1); }
    v_stack_m74 = Arg2;
    if ((uint8_t)((uint8_t)(local_r13)) == 0) goto loc_0088D4E0;
loc_0088D3D4:
    Arg1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = Arg1 + 456;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, (uint32_t)(v_stack_p18));
    }
    result = KeAbPostRelease(Arg1 + 456, Arg2, Arg3, (uint32_t)(v_stack_p18));
    result = KeLeaveCriticalRegionThread(v_stack_m60, Arg2, Arg3, (uint32_t)(v_stack_p18));
    if (v_stack_p8 != 0) goto loc_0088D65F;
loc_0088D40E:
    if (Arg7 != 0) {
        *(uint32_t *)(Arg7) = (uint32_t)((uint32_t)(v_stack_m74));
    }
    if ((uint8_t)((uint8_t)(Arg3)) != 0) goto loc_0088D6B3;
    if (0 != 0) goto loc_0088D6B3;
loc_0088D439:
    if (v_stack_m78 == 0) goto loc_0088D60D;
    if (((*(uint32_t *)(v_rip + 0x7396C2)) & (0x2000ULL)) != 0) goto loc_0088D6ED;
loc_0088D454:
    if (Arg6 == 0) goto loc_0088D644;
    if (condition_is_less_or_equal) goto loc_0088D658;
    result = ObfReferenceObjectWithTag(Arg1, (uint32_t)(0x6B577350ULL), Arg3, (uint32_t)(v_stack_p18));
    result = ((uint32_t)(v_stack_m6C)) | (Arg1);
    goto loc_0088D646;
loc_0088D47F:
    if (condition_is_above_or_equal) goto loc_0088D366;
    if (Arg6 == 0) goto loc_0088D71E;
    if ((uint32_t)((uint32_t)(v_stack_m68)) == 0) goto loc_0088D521;
    if (condition_is_above_or_equal) goto loc_0088D521;
    if (condition_is_less_or_equal) goto loc_0088D521;
loc_0088D4BE:
    local_rbx = 0;
    local_r13 = 0;
    goto loc_0088D3D4;
loc_0088D4C8:
    goto loc_0088D3A1;
loc_0088D4E0:
    v_stack_m74 = (uint32_t)((uint32_t)(0x6B577350ULL));
    if ((*(uint64_t *)(arg1 + 0x720)) == 0) goto loc_0088D3D4;
    Arg4 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((int32_t)(v_stack_p18))))));
    if (condition_is_less_or_equal) goto loc_0088D553;
    if (((*(uint32_t *)(arg1 + 0x744)) & ((uint32_t)(Arg4))) == 0) goto loc_0088D571;
    if (((uint32_t)((uint32_t)(0x6B577350ULL))) != 1) goto loc_0088D571;
    v_stack_p8 = (uint8_t)((uint32_t)(0x6B577350ULL));
loc_0088D518:
    v_stack_m74 = (uint32_t)((uint32_t)(0x6B577350ULL));
    goto loc_0088D3D4;
loc_0088D521:
    if ((((uint8_t)((uint32_t)(v_stack_p10))) & (1)) != 0) goto loc_0088D57B;
loc_0088D52D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x1F0)))) & (64)) != 0) goto loc_0088D541;
    if ((uint32_t)((uint32_t)(v_stack_m68)) != 0) goto loc_0088D5E9;
loc_0088D541:
    local_r14 = 0;
    goto loc_0088D369;
loc_0088D54C:
    local_rbx = 0;
    goto loc_0088D3D4;
loc_0088D553:
    if (((*(uint32_t *)(arg1 + 0x748)) & ((uint32_t)(Arg4))) == 0) goto loc_0088D571;
    if ((uint32_t)((uint32_t)(0x6B577350ULL)) != 0) goto loc_0088D571;
    v_stack_p8 = 1;
    v_stack_m74 = (uint32_t)((uint32_t)(0x6B577350ULL));
    goto loc_0088D3D4;
loc_0088D571:
    v_stack_p8 = 0;
    goto loc_0088D518;
loc_0088D57B:
    if (*(uint64_t *)(Arg4 + 0x2A0) == 0) goto loc_0088D52D;
    if ((*(uint64_t *)(*(uint64_t *)(Arg4 + 0x2A0) + 0x520)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x2A0) + 0x520))) goto loc_0088D52D;
    local_r11 = (uint32_t)((1) << ((uint8_t)((uint32_t)(v_stack_p18))));
loc_0088D5B4:
    result = PspIsProcessInJob(Arg4, *(uint64_t *)(arg1 + 0x2A0), Arg3, Arg4);
    if (((uint32_t)(result)) != 292) goto loc_0088D5D0;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x2A0) + 0x4A0)) & ((uint32_t)(local_r11))) != 0) goto loc_0088D72A;
loc_0088D5D0:
    if ((*(uint64_t *)(arg1 + 0x2A0)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x2A0) + 0x520))) goto loc_0088D52D;
    goto loc_0088D5B4;
loc_0088D5E9:
    v_stack_m6C = 7;
    v_stack_m70 = 5;
    if (sign_flag) goto loc_0088D73C;
loc_0088D601:
    goto loc_0088D369;
loc_0088D60D:
    result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x2A0) + 0x520);
    if (((*(uint32_t *)(v_rip + 0x7394F9)) & (512)) != 0) {
        result = v_stack_p20;
        Arg4 = 0;
        v_stack_m88 = result;
        Arg3 = 1;
        result = 0;
        Arg2 = 1;
        v_stack_m90 = Arg1;
        Arg1 = Arg1;
        v_stack_m98 = 0;
        result = EtwTraceWakeCounter(Arg1, Arg2, Arg3, Arg4);
    }
    result = 0;
loc_0088D646:
    local_rsp = (local_rsp) + (120);
    return result;
loc_0088D658:
    result = ObDereferenceObjectDeferDeleteWithTag(Arg1, Arg2, Arg3, Arg4);
    goto loc_0088D644;
loc_0088D65F:
    result = 0;
    v_stack_p30 = 0;
    Arg4 = 0;
    v_stack_p28 = 0;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_p20 = 0;
    result = ZwUpdateWnfStateData(Arg1 + 1824, Arg2, Arg3, Arg4);
    if (((*(uint32_t *)(v_rip + 0x739484)) & (0x400ULL)) == 0) goto loc_0088D40E;
    if (((uint32_t)((uint32_t)(v_stack_p44))) != 1) goto loc_0088D40E;
    result = EtwTraceWakeEvent(Arg1, (uint32_t)(v_stack_pD0), Arg3, Arg4);
    goto loc_0088D40E;
loc_0088D6B3:
    Arg2 = 0;
    v_stack_p30 = v_stack_pD8;
    v_stack_p28 = Arg1;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p48));
    result = PspChargeJobWakeCounter(*(uint64_t *)(arg1 + 0x2A0), Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_pD0))), (int32_t)(Arg5));
    goto loc_0088D439;
loc_0088D6ED:
    v_stack_p30 = v_stack_pD8;
    v_stack_p28 = Arg1;
    v_stack_p20 = (int32_t)((uint32_t)((uint32_t)(v_stack_p44)));
    result = EtwTraceWakeCounter(Arg1, 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_pD0))), (int32_t)(Arg5));
    goto loc_0088D454;
loc_0088D71E:
    goto loc_0088D52D;
loc_0088D72A:
    if (condition_is_greater) goto loc_0088D4BE;
    goto loc_0088D52D;
loc_0088D73C:
    v_stack_p48 = 7;
    goto loc_0088D601;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0 + rcx*4` | `64` | `R` |
| `Arg1` | `+ 0x1C8` | `64` | `R` |
| `Arg1` | `+ 0x2A0` | `64` | `R` |
| `Arg1` | `+ 0x720` | `64` | `R` |
| `Arg1` | `+ 0x744` | `32` | `R` |
| `Arg1` | `+ 0x748` | `32` | `R` |
| `Arg1` | `+ 0x74C` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0088D2A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
