# AlpcpPortQueryServerInfo

- RVA: `0x0074C784`–`0x0074CB96` (길이 `1,042` bytes)
- VA: `0x000000014074C784`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB704`
- 디코드: `280`개 명령, `1,042/1,042` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0074C7D0` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0074C821` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x0074C850` → [AlpcpReferenceMessageByWaitingThread](../A4/AlpcpReferenceMessageByWaitingThread_function_00A47DFC.md) (function, `0x00A47DFC`)
- `0x0074C874` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0074C889` → [AlpcpLockForCachedReferenceBlob](../88/AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x0074C8D0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0074C8F2` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0074C905` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0074C91B` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (function, `0x0041DAE0`)
- `0x0074C95D` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (function, `0x0041DAE0`)
- `0x0074C979` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0074C981` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0074C9A7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0074C9C7` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0074C9F0` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0074CA05` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0074CA0D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0074CA2B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0074CA59` → [AlpcpGetPortNameInformation](AlpcpGetPortNameInformation_function_0074C6CC.md) (function, `0x0074C6CC`)
- `0x0074CA8C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0074CA9E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0074CAB5` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x0074CABF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0074CB2E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0074CB76` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [NtAlpcQueryInformation](../8E/NtAlpcQueryInformation_function_008E7200.md) at `0x008E7410`

### Static image references
- `0x0074C801` → RVA `0x00FC6AC8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x0074C874` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0074C8D0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0074C8F2` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0074C91B` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (`PAGE` → `.text`)
  - `0x0074C95D` → [ObReferenceObjectSafe](../../text/41/ObReferenceObjectSafe_function_0041DAE0.md) (`PAGE` → `.text`)
  - `0x0074C979` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0074C981` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0074C9A7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0074C9C7` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0074C9F0` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0074CA05` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0074CA0D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0074CA2B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0074CA8C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0074CA9E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0074CABF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0074CB2E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0074CB76` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0074C784  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0074C789  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0074C78E  53                              push rbx
0074C78F  56                              push rsi
0074C790  57                              push rdi
0074C791  41 54                           push r12
0074C793  41 55                           push r13
0074C795  41 56                           push r14
0074C797  41 57                           push r15
0074C799  48 83 EC 70                     sub rsp, 0x70
0074C79D  45 8B E8                        mov r13d, r8d
0074C7A0  4C 8B FA                        mov r15, rdx
0074C7A3  33 DB                           xor ebx, ebx
0074C7A5  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
0074C7AA  48 85 C9                        test rcx, rcx
0074C7AD  0F 85 CD 03 00 00               jne 0x14074cb80
0074C7B3  41 83 F8 08                     cmp r8d, 8
0074C7B7  0F 82 C3 03 00 00               jb 0x14074cb80
0074C7BD  44 8A 8C 24 D0 00 00 00         mov r9b, byte ptr [rsp + 0xd0]
0074C7C5  45 84 C9                        test r9b, r9b
0074C7C8  74 2F                           je 0x14074c7f9
0074C7CA  41 F6 C7 03                     test r15b, 3
0074C7CE  74 06                           je 0x14074c7d6
0074C7D0  E8 FB D7 14 00                  call 0x140899fd0
0074C7D5  CC                              int3
0074C7D6  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
0074C7E0  4C 3B F8                        cmp r15, rax
0074C7E3  49 0F 42 C7                     cmovb rax, r15
0074C7E7  90                              nop
0074C7E8  8A 00                           mov al, byte ptr [rax]
0074C7EA  48 8B 0A                        mov rcx, qword ptr [rdx]
0074C7ED  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
0074C7F2  EB 0D                           jmp 0x14074c801
0074C7F4  E9 8C 03 00 00                  jmp 0x14074cb85
0074C7F9  48 8B 0A                        mov rcx, qword ptr [rdx]
0074C7FC  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
0074C801  4C 8B 05 C0 A2 87 00            mov r8, qword ptr [rip + 0x87a2c0]
0074C808  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0074C80D  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0074C812  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0074C817  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0074C81C  BA 40 00 00 00                  mov edx, 0x40
0074C821  E8 8A C5 11 00                  call 0x140868db0
0074C826  85 C0                           test eax, eax
0074C828  0F 88 57 03 00 00               js 0x14074cb85
0074C82E  48 8B FB                        mov rdi, rbx
0074C831  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
0074C836  89 9C 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], ebx
0074C83D  88 5C 24 30                     mov byte ptr [rsp + 0x30], bl
0074C841  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
0074C846  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
0074C84B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0074C850  E8 A7 B5 2F 00                  call 0x140a47dfc
0074C855  44 8B F0                        mov r14d, eax
0074C858  3D 25 02 00 C0                  cmp eax, 0xc0000225
0074C85D  75 0B                           jne 0x14074c86a
0074C85F  48 8B F3                        mov rsi, rbx
0074C862  44 8B F3                        mov r14d, ebx
0074C865  E9 43 02 00 00                  jmp 0x14074caad
0074C86A  45 85 F6                        test r14d, r14d
0074C86D  79 12                           jns 0x14074c881
0074C86F  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0074C874  E8 D7 CA BA FF                  call 0x1402f9350
0074C879  41 8B C6                        mov eax, r14d
0074C87C  E9 04 03 00 00                  jmp 0x14074cb85
0074C881  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0074C886  48 8B CE                        mov rcx, rsi
0074C889  E8 22 E0 13 00                  call 0x14088a8b0
0074C88E  66 FF 4E E2                     dec word ptr [rsi - 0x1e]
0074C892  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0074C897  48 3B B0 B8 05 00 00            cmp rsi, qword ptr [rax + 0x5b8]
0074C89E  0F 85 09 02 00 00               jne 0x14074caad
0074C8A4  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0074C8A8  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0074C8AD  48 85 C0                        test rax, rax
0074C8B0  0F 84 F7 01 00 00               je 0x14074caad
0074C8B6  4C 8B 60 10                     mov r12, qword ptr [rax + 0x10]
0074C8BA  4D 85 E4                        test r12, r12
0074C8BD  0F 84 EA 01 00 00               je 0x14074caad
0074C8C3  4D 8D 6C 24 F0                  lea r13, [r12 - 0x10]
0074C8C8  45 33 C0                        xor r8d, r8d
0074C8CB  33 D2                           xor edx, edx
0074C8CD  49 8B CD                        mov rcx, r13
0074C8D0  E8 5B 39 AC FF                  call 0x140210230
0074C8D5  48 8B F8                        mov rdi, rax
0074C8D8  B9 11 00 00 00                  mov ecx, 0x11
0074C8DD  33 C0                           xor eax, eax
0074C8DF  F0 49 0F B1 4D 00               lock cmpxchg qword ptr [r13], rcx
0074C8E5  74 10                           je 0x14074c8f7
0074C8E7  4D 8B CD                        mov r9, r13
0074C8EA  4C 8B C7                        mov r8, rdi
0074C8ED  33 D2                           xor edx, edx
0074C8EF  49 8B CD                        mov rcx, r13
0074C8F2  E8 55 3B AC FF                  call 0x14021044c
0074C8F7  48 85 FF                        test rdi, rdi
0074C8FA  74 04                           je 0x14074c900
0074C8FC  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0074C900  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0074C905  E8 D6 B1 14 00                  call 0x140897ae0
0074C90A  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
0074C90F  49 8B 34 24                     mov rsi, qword ptr [r12]
0074C913  48 85 F6                        test rsi, rsi
0074C916  74 4E                           je 0x14074c966
0074C918  48 8B CE                        mov rcx, rsi
0074C91B  E8 C0 11 CD FF                  call 0x14041dae0
0074C920  F6 D8                           neg al
0074C922  48 1B C9                        sbb rcx, rcx
0074C925  48 23 F1                        and rsi, rcx
0074C928  48 85 F6                        test rsi, rsi
0074C92B  74 39                           je 0x14074c966
0074C92D  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0074C932  8B 80 A0 01 00 00               mov eax, dword ptr [rax + 0x1a0]
0074C938  83 E0 06                        and eax, 6
0074C93B  83 F8 02                        cmp eax, 2
0074C93E  74 09                           je 0x14074c949
0074C940  83 F8 04                        cmp eax, 4
0074C943  74 04                           je 0x14074c949
0074C945  49 83 C4 10                     add r12, 0x10
0074C949  4D 8B 24 24                     mov r12, qword ptr [r12]
0074C94D  49 8B FC                        mov rdi, r12
0074C950  4D 85 E4                        test r12, r12
0074C953  74 14                           je 0x14074c969
0074C955  4C 3B E6                        cmp r12, rsi
0074C958  74 0F                           je 0x14074c969
0074C95A  49 8B CC                        mov rcx, r12
0074C95D  E8 7E 11 CD FF                  call 0x14041dae0
0074C962  84 C0                           test al, al
0074C964  75 03                           jne 0x14074c969
0074C966  48 8B FB                        mov rdi, rbx
0074C969  B8 11 00 00 00                  mov eax, 0x11
0074C96E  F0 49 0F B1 5D 00               lock cmpxchg qword ptr [r13], rbx
0074C974  74 08                           je 0x14074c97e
0074C976  49 8B CD                        mov rcx, r13
0074C979  E8 C2 6A B1 FF                  call 0x140263440
0074C97E  49 8B CD                        mov rcx, r13
0074C981  E8 7A 4C B9 FF                  call 0x1402e1600
0074C986  48 85 FF                        test rdi, rdi
0074C989  0F 84 ED 00 00 00               je 0x14074ca7c
0074C98F  48 85 F6                        test rsi, rsi
0074C992  0F 84 E4 00 00 00               je 0x14074ca7c
0074C998  4C 8D A7 60 01 00 00            lea r12, [rdi + 0x160]
0074C99F  45 33 C0                        xor r8d, r8d
0074C9A2  33 D2                           xor edx, edx
0074C9A4  49 8B CC                        mov rcx, r12
0074C9A7  E8 84 38 AC FF                  call 0x140210230
0074C9AC  4C 8B E8                        mov r13, rax
0074C9AF  33 C0                           xor eax, eax
0074C9B1  8D 48 11                        lea ecx, [rax + 0x11]
0074C9B4  F0 49 0F B1 0C 24               lock cmpxchg qword ptr [r12], rcx
0074C9BA  74 10                           je 0x14074c9cc
0074C9BC  4D 8B CC                        mov r9, r12
0074C9BF  4D 8B C5                        mov r8, r13
0074C9C2  33 D2                           xor edx, edx
0074C9C4  49 8B CC                        mov rcx, r12
0074C9C7  E8 80 3A AC FF                  call 0x14021044c
0074C9CC  4D 85 ED                        test r13, r13
0074C9CF  74 05                           je 0x14074c9d6
0074C9D1  41 C6 45 0A 01                  mov byte ptr [r13 + 0xa], 1
0074C9D6  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0074C9DA  A8 01                           test al, 1
0074C9DC  4C 8B EB                        mov r13, rbx
0074C9DF  4C 0F 44 E8                     cmove r13, rax
0074C9E3  4D 85 ED                        test r13, r13
0074C9E6  74 0D                           je 0x14074c9f5
0074C9E8  BA 41 6C 70 63                  mov edx, 0x63706c41
0074C9ED  49 8B CD                        mov rcx, r13
0074C9F0  E8 1B 3D AC FF                  call 0x140210710
0074C9F5  B8 11 00 00 00                  mov eax, 0x11
0074C9FA  F0 49 0F B1 1C 24               lock cmpxchg qword ptr [r12], rbx
0074CA00  74 08                           je 0x14074ca0a
0074CA02  49 8B CC                        mov rcx, r12
0074CA05  E8 36 6A B1 FF                  call 0x140263440
0074CA0A  49 8B CC                        mov rcx, r12
0074CA0D  E8 EE 4B B9 FF                  call 0x1402e1600
0074CA12  4D 85 ED                        test r13, r13
0074CA15  74 65                           je 0x14074ca7c
0074CA17  49 8B 85 D0 01 00 00            mov rax, qword ptr [r13 + 0x1d0]
0074CA1E  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0074CA23  BA 41 6C 70 63                  mov edx, 0x63706c41
0074CA28  49 8B CD                        mov rcx, r13
0074CA2B  E8 B0 AE BA FF                  call 0x1402f78e0
0074CA30  44 8B AC 24 C0 00 00 00         mov r13d, dword ptr [rsp + 0xc0]
0074CA38  41 83 FD 10                     cmp r13d, 0x10
0074CA3C  76 0B                           jbe 0x14074ca49
0074CA3E  41 8D 45 F0                     lea eax, [r13 - 0x10]
0074CA42  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
0074CA49  4C 8D 84 24 B0 00 00 00         lea r8, [rsp + 0xb0]
0074CA51  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
0074CA56  48 8B CE                        mov rcx, rsi
0074CA59  E8 6E FC FF FF                  call 0x14074c6cc
0074CA5E  44 8B F0                        mov r14d, eax
0074CA61  44 8B 64 24 30                  mov r12d, dword ptr [rsp + 0x30]
0074CA66  45 0F B6 E4                     movzx r12d, r12b
0074CA6A  85 C0                           test eax, eax
0074CA6C  B8 01 00 00 00                  mov eax, 1
0074CA71  44 0F 49 E0                     cmovns r12d, eax
0074CA75  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
0074CA7A  EB 08                           jmp 0x14074ca84
0074CA7C  44 8B AC 24 C0 00 00 00         mov r13d, dword ptr [rsp + 0xc0]
0074CA84  48 85 F6                        test rsi, rsi
0074CA87  74 08                           je 0x14074ca91
0074CA89  48 8B CE                        mov rcx, rsi
0074CA8C  E8 BF C8 BA FF                  call 0x1402f9350
0074CA91  48 85 FF                        test rdi, rdi
0074CA94  74 0D                           je 0x14074caa3
0074CA96  48 3B FE                        cmp rdi, rsi
0074CA99  74 08                           je 0x14074caa3
0074CA9B  48 8B CF                        mov rcx, rdi
0074CA9E  E8 AD C8 BA FF                  call 0x1402f9350
0074CAA3  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0074CAA8  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
0074CAAD  48 85 F6                        test rsi, rsi
0074CAB0  74 08                           je 0x14074caba
0074CAB2  48 8B CE                        mov rcx, rsi
0074CAB5  E8 26 B0 14 00                  call 0x140897ae0
0074CABA  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0074CABF  E8 8C C8 BA FF                  call 0x1402f9350
0074CAC4  BE 20 00 00 00                  mov esi, 0x20
0074CAC9  41 BC 04 00 00 C0               mov r12d, 0xc0000004
0074CACF  48 85 FF                        test rdi, rdi
0074CAD2  74 08                           je 0x14074cadc
0074CAD4  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
0074CAD8  03 F0                           add esi, eax
0074CADA  EB 0F                           jmp 0x14074caeb
0074CADC  45 3B F4                        cmp r14d, r12d
0074CADF  75 0A                           jne 0x14074caeb
0074CAE1  8B B4 24 B0 00 00 00            mov esi, dword ptr [rsp + 0xb0]
0074CAE8  83 C6 10                        add esi, 0x10
0074CAEB  44 3B EE                        cmp r13d, esi
0074CAEE  45 0F 42 F4                     cmovb r14d, r12d
0074CAF2  45 85 F6                        test r14d, r14d
0074CAF5  78 46                           js 0x14074cb3d
0074CAF7  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0074CAFB  41 88 07                        mov byte ptr [r15], al
0074CAFE  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0074CB03  49 89 47 08                     mov qword ptr [r15 + 8], rax
0074CB07  48 85 FF                        test rdi, rdi
0074CB0A  74 29                           je 0x14074cb35
0074CB0C  0F B7 07                        movzx eax, word ptr [rdi]
0074CB0F  66 41 89 47 10                  mov word ptr [r15 + 0x10], ax
0074CB14  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
0074CB18  66 41 89 47 12                  mov word ptr [r15 + 0x12], ax
0074CB1D  49 8D 4F 20                     lea rcx, [r15 + 0x20]
0074CB21  49 89 4F 18                     mov qword ptr [r15 + 0x18], rcx
0074CB25  44 0F B7 47 02                  movzx r8d, word ptr [rdi + 2]
0074CB2A  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
0074CB2E  E8 0D 9D F7 FF                  call 0x1406c6840
0074CB33  EB 08                           jmp 0x14074cb3d
0074CB35  41 89 5F 10                     mov dword ptr [r15 + 0x10], ebx
0074CB39  49 89 5F 18                     mov qword ptr [r15 + 0x18], rbx
0074CB3D  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
0074CB45  48 85 C9                        test rcx, rcx
0074CB48  74 14                           je 0x14074cb5e
0074CB4A  BA 00 00 00 80                  mov edx, 0x80000000
0074CB4F  41 8D 04 16                     lea eax, [r14 + rdx]
0074CB53  85 C2                           test edx, eax
0074CB55  75 05                           jne 0x14074cb5c
0074CB57  45 3B F4                        cmp r14d, r12d
0074CB5A  75 02                           jne 0x14074cb5e
0074CB5C  89 31                           mov dword ptr [rcx], esi
0074CB5E  EB 08                           jmp 0x14074cb68
0074CB60  44 8B F0                        mov r14d, eax
0074CB63  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
0074CB68  48 85 FF                        test rdi, rdi
0074CB6B  0F 84 08 FD FF FF               je 0x14074c879
0074CB71  33 D2                           xor edx, edx
0074CB73  48 8B CF                        mov rcx, rdi
0074CB76  E8 F5 5C 43 00                  call 0x140b82870
0074CB7B  E9 F9 FC FF FF                  jmp 0x14074c879
0074CB80  B8 0D 00 00 C0                  mov eax, 0xc000000d
0074CB85  48 83 C4 70                     add rsp, 0x70
0074CB89  41 5F                           pop r15
0074CB8B  41 5E                           pop r14
0074CB8D  41 5D                           pop r13
0074CB8F  41 5C                           pop r12
0074CB91  5F                              pop rdi
0074CB92  5E                              pop rsi
0074CB93  5B                              pop rbx
0074CB94  C3                              ret
0074CB95  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpPortQueryServerInfo(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (112);
    v_rbx = 0;
    v_stack_m70 = 0;
    if (a1 != 0) goto loc_0074CB80;
    if (a3 < 8) goto loc_0074CB80;
    if (a5 == 0) goto loc_0074C7F9;
    if ((((unsigned __int8)(a2)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a2, a3, a5);
    }
    if (a2 < result) { result = a2; }
    v_stack_m50 = *(unsigned __int64 *)(a2);
    goto loc_0074C801;
loc_0074C7F9:
    v_stack_m50 = *(unsigned __int64 *)(a2);
loc_0074C801:
    v_stack_m68 = 0;
    v_stack_m80 = 0;
    v_stack_m88 = v_stack_m68;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(a2), 64, *(unsigned __int64 *)(v_rip + 8889024), a5);
    if (sign_flag) goto loc_0074CB85;
    v_stack_m60 = 0;
    v_stack_p8 = 0;
    v_stack_m78 = 0;
    v_stack_m58 = 0;
    result = AlpcpReferenceMessageByWaitingThread(v_stack_m68, v_stack_m70, *(unsigned __int64 *)(v_rip + 8889024), a5);
    if (((unsigned int)(result)) != 0xC0000225ULL) goto loc_0074C86A;
    goto loc_0074CAAD;
loc_0074C86A:
    if (!sign_flag) goto loc_0074C881;
    result = ObfDereferenceObject(v_stack_m68, v_stack_m70, *(unsigned __int64 *)(v_rip + 8889024), a5);
loc_0074C879:
    goto loc_0074CB85;
loc_0074C881:
    result = AlpcpLockForCachedReferenceBlob(v_stack_m70, v_stack_m70, *(unsigned __int64 *)(v_rip + 8889024), a5);
    if (v_stack_m70 != (*(unsigned __int64 *)(v_stack_m68 + 1464))) goto loc_0074CAAD;
    v_stack_m48 = *(unsigned __int64 *)(v_stack_m70 + 24);
    if (*(unsigned __int64 *)(v_stack_m70 + 24) == 0) goto loc_0074CAAD;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 24) + 16) == 0) goto loc_0074CAAD;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 24) + 16) - 16, a2, a3, a5);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 24) + 16) - 16;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 24) + 16) - 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = AlpcpUnlockMessage(v_stack_m70, a2, a3, a4);
    v_stack_m70 = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 24) + 16)) == 0) goto loc_0074C966;
    result = ObReferenceObjectSafe(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 24) + 16)), a2, a3, a4);
    result = (unsigned __int8)(-(result));
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 24) + 16))) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 24) + 16)));
    if (v_rsi == 0) goto loc_0074C966;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m48 + 416))) & (6));
    if (((unsigned int)(result)) == 2) goto loc_0074C949;
    v_r12 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 24) + 16);
    if (((unsigned int)(result)) != 4) {
        v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 24) + 16)) + (16);
    }
    if (*(unsigned __int64 *)(v_r12) == 0) goto loc_0074C969;
    if ((*(unsigned __int64 *)(v_r12)) == v_rsi) goto loc_0074C969;
    result = ObReferenceObjectSafe(*(unsigned __int64 *)(v_r12), a2, a3, a4);
    v_rdi = *(unsigned __int64 *)(v_r12);
    if ((unsigned __int8)(result) == 0) {
        v_rdi = 0;
    }
    result = 17;
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 24) + 16) - 16;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m70 + 24) + 16) - 16, a2, a3, a4);
    if (v_rdi == 0) goto loc_0074CA7C;
    if (v_rsi == 0) goto loc_0074CA7C;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rdi + 352, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rdi + 352;
        a3 = 0;
        a2 = 0;
        a1 = v_rdi + 352;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_r13 = 0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 24))) & (1)) == 0) { v_r13 = *(unsigned __int64 *)(v_rdi + 24); }
    result = *(unsigned __int64 *)(v_rdi + 24);
    if (v_r13 != 0) {
        a2 = 0x63706C41ULL;
        a1 = v_r13;
        result = ObfReferenceObjectWithTag(a1, a2, a3, a4);
    }
    result = 17;
    if (v_r13 != 0) {
        a1 = v_rdi + 352;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rdi + 352, a2, a3, a4);
    if (v_r13 == 0) goto loc_0074CA7C;
    v_stack_m58 = *(unsigned __int64 *)(v_r13 + 464);
    result = ObfDereferenceObjectWithTag(v_r13, (unsigned int)(0x63706C41ULL), a3, a4);
    if (((unsigned int)((unsigned int)(v_stack_p18))) >= = 16) {
        result = (unsigned int)(v_stack_p18) - 16;
        v_stack_p8 = (unsigned int)(result);
    }
    result = AlpcpGetPortNameInformation(v_rsi, v_stack_m60, v_stack_p8, a4);
    v_r12 = (unsigned __int8)((unsigned int)(v_stack_m78));
    if (!sign_flag) { v_r12 = 1; }
    v_stack_m78 = (unsigned int)(v_r12);
    goto loc_0074CA84;
loc_0074CA7C:
loc_0074CA84:
    result = 1;
    if (v_rsi != 0) {
        a1 = v_rsi;
        result = ObfDereferenceObject(a1, v_stack_m60, v_stack_p8, a4);
    }
    if (v_rdi == 0) goto loc_0074CAA3;
    if (v_rdi != v_rsi) {
        a1 = v_rdi;
        result = ObfDereferenceObject(a1, v_stack_m60, v_stack_p8, a4);
    }
loc_0074CAAD:
    if (v_stack_m70 != 0) {
        a1 = v_stack_m70;
        result = AlpcpUnlockMessage(a1, v_stack_m60, v_stack_p8, a4);
    }
    result = ObfDereferenceObject(v_stack_m68, v_stack_m60, v_stack_p8, a4);
    if (v_stack_m60 == 0) goto loc_0074CADC;
    v_rsi = (unsigned int)((32) + ((unsigned int)(*(unsigned __int16 *)(v_stack_m60 + 2))));
    goto loc_0074CAEB;
loc_0074CADC:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)((unsigned int)(0xC0000004ULL)))) {
        v_rsi = v_stack_p8;
        v_rsi = (unsigned int)((v_rsi) + (16));
    }
    v_r14 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)(v_stack_p18))) < ((unsigned int)(v_rsi))) { v_r14 = (unsigned int)((unsigned int)(0xC0000004ULL)); }
    if (sign_flag) goto loc_0074CB3D;
    *(unsigned __int8 *)(a2) = (unsigned __int8)((unsigned int)(v_stack_m78));
    *(unsigned __int64 *)(a2 + 8) = v_stack_m58;
    if (v_stack_m60 == 0) goto loc_0074CB35;
    *(unsigned __int16 *)(a2 + 16) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m60));
    *(unsigned __int16 *)(a2 + 18) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m60 + 2));
    *(unsigned __int64 *)(a2 + 24) = a2 + 32;
    result = memcpy(a2 + 32, *(unsigned __int64 *)(v_stack_m60 + 8), *(unsigned __int16 *)(v_stack_m60 + 2), a4);
    goto loc_0074CB3D;
loc_0074CB35:
    *(unsigned int *)(a2 + 16) = 0;
    *(unsigned __int64 *)(a2 + 24) = 0;
loc_0074CB3D:
    if (v_stack_p20 == 0) goto loc_0074CB5E;
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(v_r14 + (unsigned int)(0x80000000ULL) * 1))) != 0) goto loc_0074CB5C;
    if (((unsigned int)(v_r14)) == ((unsigned int)((unsigned int)(0xC0000004ULL)))) {
        *(unsigned int *)(v_stack_p20) = (unsigned int)(v_rsi);
    }
    goto loc_0074CB68;
loc_0074CB68:
    if (v_stack_m60 == 0) goto loc_0074C879;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m60, a2, *(unsigned __int16 *)(v_stack_m60 + 2), a4);
    goto loc_0074C879;
loc_0074CB80:
loc_0074CB85:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpPortQueryServerInfo(int64_t Arg1, void *Arg2, int32_t Arg3, int64_t Arg4, uint8_t Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint8_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (112);
    local_rbx = 0;
    v_stack_m70 = 0;
    if (Arg1 != 0) goto loc_0074CB80;
    if (Arg3 < 8) goto loc_0074CB80;
    if (Arg5 == 0) goto loc_0074C7F9;
    if ((((uint8_t)(Arg2)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg5);
    }
    if (Arg2 < result) { result = Arg2; }
    v_stack_m50 = *(uint64_t *)(arg2);
    goto loc_0074C801;
loc_0074C7F9:
    v_stack_m50 = *(uint64_t *)(arg2);
loc_0074C801:
    v_stack_m68 = 0;
    v_stack_m80 = 0;
    v_stack_m88 = v_stack_m68;
    result = ObReferenceObjectByHandle(*(uint64_t *)(arg2), 64, *(uint64_t *)(v_rip + 0x87A2C0), Arg5);
    if (sign_flag) goto loc_0074CB85;
    v_stack_m60 = 0;
    v_stack_p8 = 0;
    v_stack_m78 = 0;
    v_stack_m58 = 0;
    result = AlpcpReferenceMessageByWaitingThread(v_stack_m68, v_stack_m70, *(uint64_t *)(v_rip + 0x87A2C0), Arg5);
    if (((uint32_t)(result)) != 0xC0000225ULL) goto loc_0074C86A;
    goto loc_0074CAAD;
loc_0074C86A:
    if (!sign_flag) goto loc_0074C881;
    result = ObfDereferenceObject(v_stack_m68, v_stack_m70, *(uint64_t *)(v_rip + 0x87A2C0), Arg5);
loc_0074C879:
    goto loc_0074CB85;
loc_0074C881:
    result = AlpcpLockForCachedReferenceBlob(v_stack_m70, v_stack_m70, *(uint64_t *)(v_rip + 0x87A2C0), Arg5);
    if (v_stack_m70 != (*(uint64_t *)(v_stack_m68 + 0x5B8))) goto loc_0074CAAD;
    v_stack_m48 = *(uint64_t *)(v_stack_m70 + 0x18);
    if (*(uint64_t *)(v_stack_m70 + 0x18) == 0) goto loc_0074CAAD;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x18) + 0x10) == 0) goto loc_0074CAAD;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x18) + 0x10) - 16, Arg2, Arg3, Arg5);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = *(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x18) + 0x10) - 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x18) + 0x10) - 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = AlpcpUnlockMessage(v_stack_m70, Arg2, Arg3, Arg4);
    v_stack_m70 = 0;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x18) + 0x10)) == 0) goto loc_0074C966;
    result = ObReferenceObjectSafe(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x18) + 0x10)), Arg2, Arg3, Arg4);
    result = (uint8_t)(-(result));
    local_rsi = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x18) + 0x10))) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x18) + 0x10)));
    if (local_rsi == 0) goto loc_0074C966;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m48 + 0x1A0))) & (6));
    if (((uint32_t)(result)) == 2) goto loc_0074C949;
    local_r12 = *(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x18) + 0x10);
    if (((uint32_t)(result)) != 4) {
        local_r12 = (*(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x18) + 0x10)) + (16);
    }
    if (*(uint64_t *)(local_r12) == 0) goto loc_0074C969;
    if ((*(uint64_t *)(local_r12)) == local_rsi) goto loc_0074C969;
    result = ObReferenceObjectSafe(*(uint64_t *)(local_r12), Arg2, Arg3, Arg4);
    local_rdi = *(uint64_t *)(local_r12);
    if ((uint8_t)(result) == 0) {
        local_rdi = 0;
    }
    result = 17;
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x18) + 0x10) - 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(v_stack_m70 + 0x18) + 0x10) - 16, Arg2, Arg3, Arg4);
    if (local_rdi == 0) goto loc_0074CA7C;
    if (local_rsi == 0) goto loc_0074CA7C;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rdi + 352, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_rdi + 352;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_rdi + 352;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_r13 = 0;
    if ((((uint8_t)(*(uint64_t *)(local_rdi + 0x18))) & (1)) == 0) { local_r13 = *(uint64_t *)(local_rdi + 0x18); }
    result = *(uint64_t *)(local_rdi + 0x18);
    if (local_r13 != 0) {
        Arg2 = 0x63706C41ULL;
        Arg1 = local_r13;
        result = ObfReferenceObjectWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    result = 17;
    if (local_r13 != 0) {
        Arg1 = local_rdi + 352;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(local_rdi + 352, Arg2, Arg3, Arg4);
    if (local_r13 == 0) goto loc_0074CA7C;
    v_stack_m58 = *(uint64_t *)(local_r13 + 0x1D0);
    result = ObfDereferenceObjectWithTag(local_r13, (uint32_t)(0x63706C41ULL), Arg3, Arg4);
    if (((uint32_t)((uint32_t)(v_stack_p18))) >= = 16) {
        result = (uint32_t)(v_stack_p18) - 16;
        v_stack_p8 = (uint32_t)(result);
    }
    result = AlpcpGetPortNameInformation(local_rsi, v_stack_m60, v_stack_p8, Arg4);
    local_r12 = (uint8_t)((uint32_t)(v_stack_m78));
    if (!sign_flag) { local_r12 = 1; }
    v_stack_m78 = (uint32_t)(local_r12);
    goto loc_0074CA84;
loc_0074CA7C:
loc_0074CA84:
    result = 1;
    if (local_rsi != 0) {
        Arg1 = local_rsi;
        result = ObfDereferenceObject(Arg1, v_stack_m60, v_stack_p8, Arg4);
    }
    if (local_rdi == 0) goto loc_0074CAA3;
    if (local_rdi != local_rsi) {
        Arg1 = local_rdi;
        result = ObfDereferenceObject(Arg1, v_stack_m60, v_stack_p8, Arg4);
    }
loc_0074CAAD:
    if (v_stack_m70 != 0) {
        Arg1 = v_stack_m70;
        result = AlpcpUnlockMessage(Arg1, v_stack_m60, v_stack_p8, Arg4);
    }
    result = ObfDereferenceObject(v_stack_m68, v_stack_m60, v_stack_p8, Arg4);
    if (v_stack_m60 == 0) goto loc_0074CADC;
    local_rsi = (uint32_t)((32) + ((uint32_t)(*(uint16_t *)(v_stack_m60 + 0x2))));
    goto loc_0074CAEB;
loc_0074CADC:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)((uint32_t)(0xC0000004ULL)))) {
        local_rsi = v_stack_p8;
        local_rsi = (uint32_t)((local_rsi) + (16));
    }
    local_r14 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)(v_stack_p18))) < ((uint32_t)(local_rsi))) { local_r14 = (uint32_t)((uint32_t)(0xC0000004ULL)); }
    if (sign_flag) goto loc_0074CB3D;
    *(uint8_t *)(arg2) = (uint8_t)((uint32_t)(v_stack_m78));
    *(uint64_t *)(arg2 + 0x8) = v_stack_m58;
    if (v_stack_m60 == 0) goto loc_0074CB35;
    *(uint16_t *)(arg2 + 0x10) = (uint16_t)(*(uint16_t *)(v_stack_m60));
    *(uint16_t *)(arg2 + 0x12) = (uint16_t)(*(uint16_t *)(v_stack_m60 + 0x2));
    *(void **)(arg2 + 0x18) = Arg2 + 32;
    result = memcpy(Arg2 + 32, *(uint64_t *)(v_stack_m60 + 0x8), *(uint16_t *)(v_stack_m60 + 0x2), Arg4);
    goto loc_0074CB3D;
loc_0074CB35:
    *(uint32_t *)(arg2 + 0x10) = 0;
    *(uint64_t *)(arg2 + 0x18) = 0;
loc_0074CB3D:
    if (v_stack_p20 == 0) goto loc_0074CB5E;
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(local_r14 + (uint32_t)(0x80000000ULL) * 1))) != 0) goto loc_0074CB5C;
    if (((uint32_t)(local_r14)) == ((uint32_t)((uint32_t)(0xC0000004ULL)))) {
        *(uint32_t *)(v_stack_p20) = (uint32_t)(local_rsi);
    }
    goto loc_0074CB68;
loc_0074CB68:
    if (v_stack_m60 == 0) goto loc_0074C879;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m60, Arg2, *(uint16_t *)(v_stack_m60 + 0x2), Arg4);
    goto loc_0074C879;
loc_0074CB80:
loc_0074CB85:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)(0xC000000DULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0074C784&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
