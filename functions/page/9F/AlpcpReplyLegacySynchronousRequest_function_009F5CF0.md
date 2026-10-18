# AlpcpReplyLegacySynchronousRequest

- RVA: `0x009F5CF0`–`0x009F61DD` (길이 `1,261` bytes)
- VA: `0x00000001409F5CF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A6B24`
- 디코드: `327`개 명령, `1,261/1,261` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009F5D85` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x009F5DCA` → [AlpcpValidateDataInformation](../AD/AlpcpValidateDataInformation_function_00ADA7C8.md) (function, `0x00ADA7C8`)
- `0x009F5E5E` → [AlpcpLookupMessage](../89/AlpcpLookupMessage_function_00895A40.md) (function, `0x00895A40`)
- `0x009F5E89` → [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)
- `0x009F5EDF` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009F5F04` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x009F5F57` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x009F5F5F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F5FC5` → [AlpcpAvailableBufferSize](../89/AlpcpAvailableBufferSize_function_00895390.md) (function, `0x00895390`)
- `0x009F5FDD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009F5FF1` → [AlpcpCaptureMessageData](../89/AlpcpCaptureMessageData_function_008929A0.md) (function, `0x008929A0`)
- `0x009F602B` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x009F604A` → [AlpcpRemoveMessageFromPendingQueue](../88/AlpcpRemoveMessageFromPendingQueue_function_0088FD70.md) (function, `0x0088FD70`)
- `0x009F60C4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009F60E0` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x009F611C` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x009F6124` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F6151` → [AlpcpClearOwnerPortMessage](../88/AlpcpClearOwnerPortMessage_function_0088FD30.md) (function, `0x0088FD30`)
- `0x009F6159` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x009F616A` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x009F6199` → [KeReleaseSemaphoreEx](../../text/34/KeReleaseSemaphoreEx_function_003468C0.md) (function, `0x003468C0`)
- `0x009F61A3` → [AlpcpUnlockMessage](../89/AlpcpUnlockMessage_function_00897AE0.md) (function, `0x00897AE0`)
- `0x009F61BA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtReplyWaitReceivePortEx](../89/NtReplyWaitReceivePortEx_function_00895850.md) at `0x008959E1`
- [NtReplyPort](NtReplyPort_function_009F5BE0.md) at `0x009F5C8D`

### Static image references
- `0x009F5D0B` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x009F5D85` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x009F5EDF` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009F5F04` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x009F5F57` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x009F5F5F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F5FDD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009F60C4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009F60E0` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x009F611C` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x009F6124` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F6159` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x009F6199` → [KeReleaseSemaphoreEx](../../text/34/KeReleaseSemaphoreEx_function_003468C0.md) (`PAGE` → `.text`)
  - `0x009F61BA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009F5CF0  4C 8B DC                        mov r11, rsp
009F5CF3  49 89 5B 18                     mov qword ptr [r11 + 0x18], rbx
009F5CF7  49 89 73 20                     mov qword ptr [r11 + 0x20], rsi
009F5CFB  57                              push rdi
009F5CFC  41 54                           push r12
009F5CFE  41 55                           push r13
009F5D00  41 56                           push r14
009F5D02  41 57                           push r15
009F5D04  48 81 EC C0 00 00 00            sub rsp, 0xc0
009F5D0B  48 8B 05 2E 4A 41 00            mov rax, qword ptr [rip + 0x414a2e]
009F5D12  48 33 C4                        xor rax, rsp
009F5D15  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
009F5D1D  4C 8B EA                        mov r13, rdx
009F5D20  48 8B C1                        mov rax, rcx
009F5D23  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
009F5D28  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
009F5D30  0F 57 C0                        xorps xmm0, xmm0
009F5D33  33 C9                           xor ecx, ecx
009F5D35  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
009F5D3A  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
009F5D3F  49 89 4B 80                     mov qword ptr [r11 - 0x80], rcx
009F5D43  33 FF                           xor edi, edi
009F5D45  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
009F5D4A  4C 8B 30                        mov r14, qword ptr [rax]
009F5D4D  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
009F5D55  45 84 C0                        test r8b, r8b
009F5D58  0F 84 91 00 00 00               je 0x1409f5def
009F5D5E  33 C0                           xor eax, eax
009F5D60  41 0F 11 43 B8                  movups xmmword ptr [r11 - 0x48], xmm0
009F5D65  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
009F5D69  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
009F5D73  4C 3B EA                        cmp r13, rdx
009F5D76  49 0F 42 D5                     cmovb rdx, r13
009F5D7A  8D 59 28                        lea ebx, [rcx + 0x28]
009F5D7D  44 8B C3                        mov r8d, ebx
009F5D80  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
009F5D85  E8 46 6C CC FF                  call 0x1406bc9d0
009F5D8A  0F B7 4C 24 48                  movzx ecx, word ptr [rsp + 0x48]
009F5D8F  8D 04 0B                        lea eax, [rbx + rcx]
009F5D92  66 3B C8                        cmp cx, ax
009F5D95  73 0D                           jae 0x1409f5da4
009F5D97  48 03 CB                        add rcx, rbx
009F5D9A  0F B7 44 24 4A                  movzx eax, word ptr [rsp + 0x4a]
009F5D9F  48 3B C8                        cmp rcx, rax
009F5DA2  76 0E                           jbe 0x1409f5db2
009F5DA4  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009F5DA9  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
009F5DAD  E9 FB 03 00 00                  jmp 0x1409f61ad
009F5DB2  66 89 4C 24 4A                  mov word ptr [rsp + 0x4a], cx
009F5DB7  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
009F5DBB  66 39 7C 24 4E                  cmp word ptr [rsp + 0x4e], di
009F5DC0  74 1B                           je 0x1409f5ddd
009F5DC2  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
009F5DC7  49 8B CD                        mov rcx, r13
009F5DCA  E8 F9 49 0E 00                  call 0x140ada7c8
009F5DCF  8B D8                           mov ebx, eax
009F5DD1  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009F5DD5  85 C0                           test eax, eax
009F5DD7  0F 88 D0 03 00 00               js 0x1409f61ad
009F5DDD  44 8B 44 24 68                  mov r8d, dword ptr [rsp + 0x68]
009F5DE2  EB 69                           jmp 0x1409f5e4d
009F5DE4  8B D8                           mov ebx, eax
009F5DE6  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009F5DEA  E9 BE 03 00 00                  jmp 0x1409f61ad
009F5DEF  0F 10 12                        movups xmm2, xmmword ptr [rdx]
009F5DF2  0F 11 54 24 48                  movups xmmword ptr [rsp + 0x48], xmm2
009F5DF7  0F 10 42 10                     movups xmm0, xmmword ptr [rdx + 0x10]
009F5DFB  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
009F5E00  F2 0F 10 4A 20                  movsd xmm1, qword ptr [rdx + 0x20]
009F5E05  F2 0F 11 4C 24 68               movsd qword ptr [rsp + 0x68], xmm1
009F5E0B  44 8B C7                        mov r8d, edi
009F5E0E  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
009F5E12  66 41 0F 7E D1                  movd r9d, xmm2
009F5E17  BB 28 00 00 00                  mov ebx, 0x28
009F5E1C  42 8D 14 0B                     lea edx, [rbx + r9]
009F5E20  66 44 3B CA                     cmp r9w, dx
009F5E24  72 0A                           jb 0x1409f5e30
009F5E26  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009F5E2B  E9 7D 03 00 00                  jmp 0x1409f61ad
009F5E30  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
009F5E35  48 C1 E8 10                     shr rax, 0x10
009F5E39  0F B7 C8                        movzx ecx, ax
009F5E3C  41 0F B7 C1                     movzx eax, r9w
009F5E40  48 03 C3                        add rax, rbx
009F5E43  48 3B C1                        cmp rax, rcx
009F5E46  77 DE                           ja 0x1409f5e26
009F5E48  66 89 54 24 4A                  mov word ptr [rsp + 0x4a], dx
009F5E4D  48 8D 44 24 38                  lea rax, [rsp + 0x38]
009F5E52  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F5E57  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
009F5E5B  49 8B CE                        mov rcx, r14
009F5E5E  E8 DD FB E9 FF                  call 0x140895a40
009F5E63  8B D8                           mov ebx, eax
009F5E65  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009F5E69  85 C0                           test eax, eax
009F5E6B  0F 88 3C 03 00 00               js 0x1409f61ad
009F5E71  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
009F5E76  8B 4E 28                        mov ecx, dword ptr [rsi + 0x28]
009F5E79  84 C9                           test cl, cl
009F5E7B  79 1B                           jns 0x1409f5e98
009F5E7D  41 B8 00 00 01 00               mov r8d, 0x10000
009F5E83  48 8B D6                        mov rdx, rsi
009F5E86  49 8B CE                        mov rcx, r14
009F5E89  E8 92 E2 E9 FF                  call 0x140894120
009F5E8E  BB 37 00 00 C0                  mov ebx, 0xc0000037
009F5E93  E9 15 03 00 00                  jmp 0x1409f61ad
009F5E98  0F BA E1 09                     bt ecx, 9
009F5E9C  0F 82 FE 02 00 00               jb 0x1409f61a0
009F5EA2  48 39 7E 20                     cmp qword ptr [rsi + 0x20], rdi
009F5EA6  0F 84 F4 02 00 00               je 0x1409f61a0
009F5EAC  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
009F5EB0  49 3B D6                        cmp rdx, r14
009F5EB3  0F 84 DA 00 00 00               je 0x1409f5f93
009F5EB9  F6 C1 07                        test cl, 7
009F5EBC  0F 85 A9 00 00 00               jne 0x1409f5f6b
009F5EC2  4C 8B 7E 18                     mov r15, qword ptr [rsi + 0x18]
009F5EC6  4D 85 FF                        test r15, r15
009F5EC9  0F 84 D1 02 00 00               je 0x1409f61a0
009F5ECF  49 8B 77 10                     mov rsi, qword ptr [r15 + 0x10]
009F5ED3  48 8D 5E F0                     lea rbx, [rsi - 0x10]
009F5ED7  45 33 C0                        xor r8d, r8d
009F5EDA  33 D2                           xor edx, edx
009F5EDC  48 8B CB                        mov rcx, rbx
009F5EDF  E8 4C A3 81 FF                  call 0x140210230
009F5EE4  48 8B C8                        mov rcx, rax
009F5EE7  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
009F5EEC  33 C0                           xor eax, eax
009F5EEE  44 8D 60 11                     lea r12d, [rax + 0x11]
009F5EF2  F0 4C 0F B1 23                  lock cmpxchg qword ptr [rbx], r12
009F5EF7  74 15                           je 0x1409f5f0e
009F5EF9  4C 8B CB                        mov r9, rbx
009F5EFC  4C 8B C1                        mov r8, rcx
009F5EFF  33 D2                           xor edx, edx
009F5F01  48 8B CB                        mov rcx, rbx
009F5F04  E8 43 A5 81 FF                  call 0x14021044c
009F5F09  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
009F5F0E  48 85 C9                        test rcx, rcx
009F5F11  74 04                           je 0x1409f5f17
009F5F13  C6 41 0A 01                     mov byte ptr [rcx + 0xa], 1
009F5F17  41 8B 87 A0 01 00 00            mov eax, dword ptr [r15 + 0x1a0]
009F5F1E  D1 E8                           shr eax, 1
009F5F20  83 E0 03                        and eax, 3
009F5F23  83 E8 01                        sub eax, 1
009F5F26  74 1A                           je 0x1409f5f42
009F5F28  83 F8 01                        cmp eax, 1
009F5F2B  75 15                           jne 0x1409f5f42
009F5F2D  4C 39 36                        cmp qword ptr [rsi], r14
009F5F30  74 0B                           je 0x1409f5f3d
009F5F32  4C 39 76 08                     cmp qword ptr [rsi + 8], r14
009F5F36  74 05                           je 0x1409f5f3d
009F5F38  44 8A FF                        mov r15b, dil
009F5F3B  EB 0D                           jmp 0x1409f5f4a
009F5F3D  41 B7 01                        mov r15b, 1
009F5F40  EB 08                           jmp 0x1409f5f4a
009F5F42  4C 39 76 10                     cmp qword ptr [rsi + 0x10], r14
009F5F46  41 0F 94 C7                     sete r15b
009F5F4A  49 8B C4                        mov rax, r12
009F5F4D  F0 48 0F B1 3B                  lock cmpxchg qword ptr [rbx], rdi
009F5F52  74 08                           je 0x1409f5f5c
009F5F54  48 8B CB                        mov rcx, rbx
009F5F57  E8 E4 D4 86 FF                  call 0x140263440
009F5F5C  48 8B CB                        mov rcx, rbx
009F5F5F  E8 9C B6 8E FF                  call 0x1402e1600
009F5F64  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
009F5F69  EB 48                           jmp 0x1409f5fb3
009F5F6B  41 8B 86 A0 01 00 00            mov eax, dword ptr [r14 + 0x1a0]
009F5F72  83 E0 06                        and eax, 6
009F5F75  3C 06                           cmp al, 6
009F5F77  0F 85 23 02 00 00               jne 0x1409f61a0
009F5F7D  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
009F5F81  48 85 C0                        test rax, rax
009F5F84  0F 84 16 02 00 00               je 0x1409f61a0
009F5F8A  48 39 10                        cmp qword ptr [rax], rdx
009F5F8D  0F 85 0D 02 00 00               jne 0x1409f61a0
009F5F93  8B C1                           mov eax, ecx
009F5F95  83 E0 07                        and eax, 7
009F5F98  3C 03                           cmp al, 3
009F5F9A  0F 85 00 02 00 00               jne 0x1409f61a0
009F5FA0  0F BA E1 0D                     bt ecx, 0xd
009F5FA4  0F 82 F6 01 00 00               jb 0x1409f61a0
009F5FAA  41 B7 01                        mov r15b, 1
009F5FAD  41 BC 11 00 00 00               mov r12d, 0x11
009F5FB3  45 84 FF                        test r15b, r15b
009F5FB6  0F 84 E4 01 00 00               je 0x1409f61a0
009F5FBC  48 0F BF 54 24 48               movsx rdx, word ptr [rsp + 0x48]
009F5FC2  48 8B CE                        mov rcx, rsi
009F5FC5  E8 C6 F3 E9 FF                  call 0x140895390
009F5FCA  48 3B D0                        cmp rdx, rax
009F5FCD  77 1B                           ja 0x1409f5fea
009F5FCF  48 8D 8E 18 01 00 00            lea rcx, [rsi + 0x118]
009F5FD6  4C 8B C2                        mov r8, rdx
009F5FD9  49 8D 55 28                     lea rdx, [r13 + 0x28]
009F5FDD  E8 5E 08 CD FF                  call 0x1406c6840
009F5FE2  8B DF                           mov ebx, edi
009F5FE4  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
009F5FE8  EB 12                           jmp 0x1409f5ffc
009F5FEA  4D 8D 45 28                     lea r8, [r13 + 0x28]
009F5FEE  48 8B CE                        mov rcx, rsi
009F5FF1  E8 AA C9 E9 FF                  call 0x1408929a0
009F5FF6  8B D8                           mov ebx, eax
009F5FF8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009F5FFC  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
009F6001  EB 21                           jmp 0x1409f6024
009F6003  8B D8                           mov ebx, eax
009F6005  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009F6009  33 FF                           xor edi, edi
009F600B  44 8D 67 11                     lea r12d, [rdi + 0x11]
009F600F  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
009F6014  4C 8B B4 24 80 00 00 00         mov r14, qword ptr [rsp + 0x80]
009F601C  4C 8B AC 24 90 00 00 00         mov r13, qword ptr [rsp + 0x90]
009F6024  85 DB                           test ebx, ebx
009F6026  79 0D                           jns 0x1409f6035
009F6028  48 8B CE                        mov rcx, rsi
009F602B  E8 B0 1A EA FF                  call 0x140897ae0
009F6030  E9 78 01 00 00                  jmp 0x1409f61ad
009F6035  0F BA 6E 28 10                  bts dword ptr [rsi + 0x28], 0x10
009F603A  F0 09 3C 24                     lock or dword ptr [rsp], edi
009F603E  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
009F6043  48 8B 73 18                     mov rsi, qword ptr [rbx + 0x18]
009F6047  48 8B CB                        mov rcx, rbx
009F604A  E8 21 9D E9 FF                  call 0x14088fd70
009F604F  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
009F6053  89 83 F0 00 00 00               mov dword ptr [rbx + 0xf0], eax
009F6059  66 C7 83 F4 00 00 00 02 00      mov word ptr [rbx + 0xf4], 2
009F6062  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009F606B  0F 10 80 08 05 00 00            movups xmm0, xmmword ptr [rax + 0x508]
009F6072  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
009F6077  F3 0F 7F 83 F8 00 00 00         movdqu xmmword ptr [rbx + 0xf8], xmm0
009F607F  8B 4B 28                        mov ecx, dword ptr [rbx + 0x28]
009F6082  0F BA E9 09                     bts ecx, 9
009F6086  89 4B 28                        mov dword ptr [rbx + 0x28], ecx
009F6089  8B 96 A0 01 00 00               mov edx, dword ptr [rsi + 0x1a0]
009F608F  D1 EA                           shr edx, 1
009F6091  83 E2 03                        and edx, 3
009F6094  8D 04 D5 00 00 00 00            lea eax, [rdx*8]
009F609B  33 C1                           xor eax, ecx
009F609D  83 E0 78                        and eax, 0x78
009F60A0  33 C1                           xor eax, ecx
009F60A2  89 43 28                        mov dword ptr [rbx + 0x28], eax
009F60A5  83 EA 01                        sub edx, 1
009F60A8  74 0A                           je 0x1409f60b4
009F60AA  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
009F60AE  48 89 43 78                     mov qword ptr [rbx + 0x78], rax
009F60B2  EB 7A                           jmp 0x1409f612e
009F60B4  4C 8B 7E 10                     mov r15, qword ptr [rsi + 0x10]
009F60B8  49 8D 5F F0                     lea rbx, [r15 - 0x10]
009F60BC  45 33 C0                        xor r8d, r8d
009F60BF  33 D2                           xor edx, edx
009F60C1  48 8B CB                        mov rcx, rbx
009F60C4  E8 67 A1 81 FF                  call 0x140210230
009F60C9  48 8B F0                        mov rsi, rax
009F60CC  33 C0                           xor eax, eax
009F60CE  F0 4C 0F B1 23                  lock cmpxchg qword ptr [rbx], r12
009F60D3  74 10                           je 0x1409f60e5
009F60D5  4C 8B CB                        mov r9, rbx
009F60D8  4C 8B C6                        mov r8, rsi
009F60DB  33 D2                           xor edx, edx
009F60DD  48 8B CB                        mov rcx, rbx
009F60E0  E8 67 A3 81 FF                  call 0x14021044c
009F60E5  48 85 F6                        test rsi, rsi
009F60E8  74 04                           je 0x1409f60ee
009F60EA  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
009F60EE  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
009F60F2  48 85 D2                        test rdx, rdx
009F60F5  75 0B                           jne 0x1409f6102
009F60F7  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
009F60FC  48 89 78 78                     mov qword ptr [rax + 0x78], rdi
009F6100  EB 0D                           jmp 0x1409f610f
009F6102  48 8B 52 38                     mov rdx, qword ptr [rdx + 0x38]
009F6106  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
009F610B  48 89 51 78                     mov qword ptr [rcx + 0x78], rdx
009F610F  49 8B C4                        mov rax, r12
009F6112  F0 48 0F B1 3B                  lock cmpxchg qword ptr [rbx], rdi
009F6117  74 08                           je 0x1409f6121
009F6119  48 8B CB                        mov rcx, rbx
009F611C  E8 1F D3 86 FF                  call 0x140263440
009F6121  48 8B CB                        mov rcx, rbx
009F6124  E8 D7 B4 8E FF                  call 0x1402e1600
009F6129  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
009F612E  48 8B 73 20                     mov rsi, qword ptr [rbx + 0x20]
009F6132  48 89 7B 20                     mov qword ptr [rbx + 0x20], rdi
009F6136  66 FF 4B E2                     dec word ptr [rbx - 0x1e]
009F613A  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
009F613D  0F BA E8 08                     bts eax, 8
009F6141  0F BA F0 10                     btr eax, 0x10
009F6145  83 E0 FD                        and eax, 0xfffffffd
009F6148  83 C8 05                        or eax, 5
009F614B  89 43 28                        mov dword ptr [rbx + 0x28], eax
009F614E  48 8B CB                        mov rcx, rbx
009F6151  E8 DA 9B E9 FF                  call 0x14088fd30
009F6156  49 8B CE                        mov rcx, r14
009F6159  E8 C2 98 81 FF                  call 0x14020fa20
009F615E  4C 89 73 18                     mov qword ptr [rbx + 0x18], r14
009F6162  0F BA 6B 28 0C                  bts dword ptr [rbx + 0x28], 0xc
009F6167  48 8B CB                        mov rcx, rbx
009F616A  E8 71 19 EA FF                  call 0x140897ae0
009F616F  41 8B 45 30                     mov eax, dword ptr [r13 + 0x30]
009F6173  A8 04                           test al, 4
009F6175  74 0A                           je 0x1409f6181
009F6177  49 89 75 18                     mov qword ptr [r13 + 0x18], rsi
009F617B  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
009F617F  EB 2C                           jmp 0x1409f61ad
009F6181  48 8D 8E 18 05 00 00            lea rcx, [rsi + 0x518]
009F6188  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
009F618D  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
009F6191  BA 01 00 00 00                  mov edx, 1
009F6196  44 8B C2                        mov r8d, edx
009F6199  E8 22 07 95 FF                  call 0x1403468c0
009F619E  EB DB                           jmp 0x1409f617b
009F61A0  48 8B CE                        mov rcx, rsi
009F61A3  E8 38 19 EA FF                  call 0x140897ae0
009F61A8  BB 22 00 00 C0                  mov ebx, 0xc0000022
009F61AD  8B C3                           mov eax, ebx
009F61AF  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
009F61B7  48 33 CC                        xor rcx, rsp
009F61BA  E8 81 64 CB FF                  call 0x1406ac640
009F61BF  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
009F61C7  49 8B 5B 40                     mov rbx, qword ptr [r11 + 0x40]
009F61CB  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
009F61CF  49 8B E3                        mov rsp, r11
009F61D2  41 5F                           pop r15
009F61D4  41 5E                           pop r14
009F61D6  41 5D                           pop r13
009F61D8  41 5C                           pop r12
009F61DA  5F                              pop rdi
009F61DB  C3                              ret
009F61DC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpReplyLegacySynchronousRequest(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int16 v_stack_m9A;
    unsigned __int16 v_stack_m9E;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mE8;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 4278830)) ^ (v_rsp);
    v_stack_m30 = result;
    v_stack_m70 = a1;
    v_stack_m58 = a1;
    a1 = 0;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 128) = 0;
    v_rdi = 0;
    v_stack_mB0 = 0;
    v_stack_m68 = *(unsigned __int64 *)(a1);
    if (a3 == 0) goto loc_009F5DEF;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56) = 0;
    if (a2 < a2) { a2 = a2; }
    result = RtlCopyVolatileMemory(v_stack_mA0, a2, (unsigned int)((unsigned int)(a1 + 40)), a4);
    if (((unsigned __int16)(v_stack_mA0)) >= ((unsigned __int16)(a1 + 40 + v_stack_mA0 * 1))) goto loc_009F5DA4;
    a1 = (v_stack_mA0) + (a1 + 40);
    if (a1 <= v_stack_m9E) goto loc_009F5DB2;
loc_009F5DA4:
    v_stack_mB8 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_009F61AD;
loc_009F5DB2:
    v_stack_m9E = (unsigned __int16)(a1);
    v_stack_mB8 = 0;
    if (v_stack_m9A == 0) goto loc_009F5DDD;
    result = AlpcpValidateDataInformation(a2, v_stack_mA0, (unsigned int)((unsigned int)(a1 + 40)), a4);
    v_stack_mB8 = (unsigned int)(result);
    if (sign_flag) goto loc_009F61AD;
loc_009F5DDD:
    goto loc_009F5E4D;
loc_009F5DEF:
    v_stack_mA0 = v_xmm2;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm1;
    v_stack_m80 = 0;
    if (((unsigned __int16)(a4)) < ((unsigned __int16)(40 + a4 * 1))) goto loc_009F5E30;
loc_009F5E26:
    goto loc_009F61AD;
loc_009F5E30:
    result = (v_stack_mA0) >> (16);
    result = ((unsigned __int16)(a4)) + ((unsigned int)(0xC000000DULL));
    if (result > ((unsigned __int16)(result))) goto loc_009F5E26;
    v_stack_m9E = (unsigned __int16)(40 + a4 * 1);
loc_009F5E4D:
    v_stack_mC8 = v_stack_mB0;
    result = AlpcpLookupMessage(*(unsigned __int64 *)(a1), (unsigned int)(v_stack_m88), 0, a4);
    v_stack_mB8 = (unsigned int)(result);
    if (sign_flag) goto loc_009F61AD;
    if (!sign_flag) goto loc_009F5E98;
    result = AlpcpCancelMessage(*(unsigned __int64 *)(a1), v_stack_mB0, (unsigned int)(0x10000ULL), a4);
    goto loc_009F61AD;
loc_009F5E98:
    if (condition_is_below) goto loc_009F61A0;
    if ((*(unsigned __int64 *)(v_stack_mB0 + 32)) == 0) goto loc_009F61A0;
    if ((*(unsigned __int64 *)(v_stack_mB0 + 16)) == (*(unsigned __int64 *)(a1))) goto loc_009F5F93;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (7)) != 0) goto loc_009F5F6B;
    if (*(unsigned __int64 *)(v_stack_mB0 + 24) == 0) goto loc_009F61A0;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) - 16, a2, a3, a4);
    v_stack_m78 = result;
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) - 16;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) - 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a1 = v_stack_m78;
    }
    if (a1 != 0) {
        *(unsigned __int8 *)(a1 + 10) = 1;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 416))) >> (1));
    result = (unsigned int)((result) & (3));
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_009F5F42;
    if (((unsigned int)(result)) != 1) goto loc_009F5F42;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16))) == (*(unsigned __int64 *)(a1))) goto loc_009F5F3D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) + 8)) == (*(unsigned __int64 *)(a1))) goto loc_009F5F3D;
    goto loc_009F5F4A;
loc_009F5F3D:
    goto loc_009F5F4A;
loc_009F5F42:
    v_r15 = ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) + 16)) == (*(unsigned __int64 *)(a1))) ? 1 : 0;
loc_009F5F4A:
    result = result + 17;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) + 16)) != (*(unsigned __int64 *)(a1))) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) - 16;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) - 16, a2, a3, a4);
    goto loc_009F5FB3;
loc_009F5F6B:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 416))) & (6));
    if (((unsigned __int8)(result)) != 6) goto loc_009F61A0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16) == 0) goto loc_009F61A0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16))) != 0) goto loc_009F61A0;
loc_009F5F93:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) - 16))) & (7));
    if (((unsigned __int8)(result)) != 3) goto loc_009F61A0;
    if (((unsigned __int8)(result)) < 3) goto loc_009F61A0;
loc_009F5FB3:
    if (1 == 0) goto loc_009F61A0;
    result = AlpcpAvailableBufferSize(v_stack_mB0, (__int16)(v_stack_mA0), a3, a4);
    if (((__int16)(v_stack_mA0)) > result) goto loc_009F5FEA;
    result = memcpy(v_stack_mB0 + 280, a2 + 40, (__int16)(v_stack_mA0), a4);
    v_stack_mB8 = 0;
    goto loc_009F5FFC;
loc_009F5FEA:
    result = AlpcpCaptureMessageData(v_stack_mB0, a2 + 40, a2 + 40, a4);
    v_stack_mB8 = (unsigned int)(result);
loc_009F5FFC:
    goto loc_009F6024;
loc_009F6024:
    if (!sign_flag) goto loc_009F6035;
    result = AlpcpUnlockMessage(v_stack_mB0, a2 + 40, a2 + 40, a4);
    goto loc_009F61AD;
loc_009F6035:
    result = AlpcpRemoveMessageFromPendingQueue(v_stack_mB0, a2 + 40, a2 + 40, a4);
    *(unsigned int *)(v_stack_mB0 + 240) = (unsigned int)((unsigned int)(v_stack_mA0));
    *(unsigned __int16 *)(v_stack_mB0 + 244) = 2;
    *(unsigned __int64 *)(v_stack_mB0 + 248) = v_xmm0;
    *(unsigned int *)(v_stack_mB0 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB0 + 40)));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 416))) >> (1));
    a2 = (unsigned int)((a2) & (3));
    result = (unsigned int)((a2 * 8) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB0 + 40)))));
    result = (unsigned int)((result) & (120));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mB0 + 40)))));
    *(unsigned int *)(v_stack_mB0 + 40) = (unsigned int)(result);
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_009F60B4;
    *(unsigned __int64 *)(v_stack_mB0 + 120) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 56);
    goto loc_009F612E;
loc_009F60B4:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) - 16, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) - 16;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) - 16;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) + 8) != 0) goto loc_009F6102;
    *(unsigned __int64 *)(v_stack_mB0 + 120) = 0;
    goto loc_009F610F;
loc_009F6102:
    *(unsigned __int64 *)(v_stack_mB0 + 120) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) + 8) + 56);
loc_009F610F:
    result = 17;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) + 8) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) - 16;
        result = ExfReleasePushLockShared(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) + 8) + 56), a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) - 16, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) + 8) + 56), a3, a4);
loc_009F612E:
    *(unsigned __int64 *)(v_stack_mB0 + 32) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mB0 + 40))) & (0xFFFFFFFDULL));
    result = (unsigned int)((result) | (5));
    *(unsigned int *)(v_stack_mB0 + 40) = (unsigned int)(result);
    result = AlpcpClearOwnerPortMessage(v_stack_mB0, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) + 8) + 56), a3, a4);
    result = ObfReferenceObject(*(unsigned __int64 *)(a1), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) + 8) + 56), a3, a4);
    *(unsigned __int64 *)(v_stack_mB0 + 24) = *(unsigned __int64 *)(a1);
    result = AlpcpUnlockMessage(v_stack_mB0, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mB0 + 24) + 16) + 8) + 56), a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m70 + 48)))) & (4)) == 0) goto loc_009F6181;
    *(unsigned __int64 *)(v_stack_m70 + 24) = *(unsigned __int64 *)(v_stack_mB0 + 32);
loc_009F617B:
    goto loc_009F61AD;
loc_009F6181:
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
    result = KeReleaseSemaphoreEx(*(unsigned __int64 *)(v_stack_mB0 + 32) + 1304, 1, 1, a4);
    goto loc_009F617B;
loc_009F61A0:
    result = AlpcpUnlockMessage(*(unsigned __int64 *)(v_stack_mB0 + 32), 1, 1, a4);
loc_009F61AD:
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, 1, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpReplyLegacySynchronousRequest(void *Arg1, void *Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint16_t v_stack_m9A;
    uint16_t v_stack_m9E;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mE8;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x414A2E)) ^ (local_rsp);
    v_stack_m30 = result;
    v_stack_m70 = Arg1;
    v_stack_m58 = Arg1;
    Arg1 = 0;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x80) = 0;
    local_rdi = 0;
    v_stack_mB0 = 0;
    v_stack_m68 = *(uint64_t *)(arg1);
    if (Arg3 == 0) goto loc_009F5DEF;
    result = 0;
    *(uint64_t *)(local_rsp - 0x48) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38) = 0;
    if (Arg2 < Arg2) { Arg2 = Arg2; }
    result = RtlCopyVolatileMemory(v_stack_mA0, Arg2, (uint32_t)((uint32_t)(Arg1 + 40)), a4);
    if (((uint16_t)(v_stack_mA0)) >= ((uint16_t)(Arg1 + 40 + v_stack_mA0 * 1))) goto loc_009F5DA4;
    Arg1 = (v_stack_mA0) + (Arg1 + 40);
    if (Arg1 <= v_stack_m9E) goto loc_009F5DB2;
loc_009F5DA4:
    v_stack_mB8 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_009F61AD;
loc_009F5DB2:
    v_stack_m9E = (uint16_t)(Arg1);
    v_stack_mB8 = 0;
    if (v_stack_m9A == 0) goto loc_009F5DDD;
    result = AlpcpValidateDataInformation(Arg2, v_stack_mA0, (uint32_t)((uint32_t)(Arg1 + 40)), a4);
    v_stack_mB8 = (uint32_t)(result);
    if (sign_flag) goto loc_009F61AD;
loc_009F5DDD:
    goto loc_009F5E4D;
loc_009F5DEF:
    v_stack_mA0 = v_xmm2;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm1;
    v_stack_m80 = 0;
    if (((uint16_t)(a4)) < ((uint16_t)(40 + a4 * 1))) goto loc_009F5E30;
loc_009F5E26:
    goto loc_009F61AD;
loc_009F5E30:
    result = (v_stack_mA0) >> (16);
    result = ((uint16_t)(a4)) + ((uint32_t)(0xC000000DULL));
    if (result > ((uint16_t)(result))) goto loc_009F5E26;
    v_stack_m9E = (uint16_t)(40 + a4 * 1);
loc_009F5E4D:
    v_stack_mC8 = v_stack_mB0;
    result = AlpcpLookupMessage(*(uint64_t *)(arg1), (uint32_t)(v_stack_m88), 0, a4);
    v_stack_mB8 = (uint32_t)(result);
    if (sign_flag) goto loc_009F61AD;
    if (!sign_flag) goto loc_009F5E98;
    result = AlpcpCancelMessage(*(uint64_t *)(arg1), v_stack_mB0, (uint32_t)(0x10000ULL), a4);
    goto loc_009F61AD;
loc_009F5E98:
    if (condition_is_below) goto loc_009F61A0;
    if ((*(uint64_t *)(v_stack_mB0 + 0x20)) == 0) goto loc_009F61A0;
    if ((*(uint64_t *)(v_stack_mB0 + 0x10)) == (*(uint64_t *)(arg1))) goto loc_009F5F93;
    if ((((uint8_t)(*(uint64_t *)(arg1))) & (7)) != 0) goto loc_009F5F6B;
    if (*(uint64_t *)(v_stack_mB0 + 0x18) == 0) goto loc_009F61A0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) - 16, Arg2, Arg3, a4);
    v_stack_m78 = result;
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) - 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) - 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
        Arg1 = v_stack_m78;
    }
    if (Arg1 != NULL) {
        *(uint8_t *)(arg1 + 0xA) = 1;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x1A0))) >> (1));
    result = (uint32_t)((result) & (3));
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_009F5F42;
    if (((uint32_t)(result)) != 1) goto loc_009F5F42;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10))) == (*(uint64_t *)(arg1))) goto loc_009F5F3D;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) + 0x8)) == (*(uint64_t *)(arg1))) goto loc_009F5F3D;
    goto loc_009F5F4A;
loc_009F5F3D:
    goto loc_009F5F4A;
loc_009F5F42:
    local_r15 = ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) + 0x10)) == (*(uint64_t *)(arg1))) ? 1 : 0;
loc_009F5F4A:
    result = result + 17;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) + 0x10)) != (*(uint64_t *)(arg1))) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) - 16;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) - 16, Arg2, Arg3, a4);
    goto loc_009F5FB3;
loc_009F5F6B:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x1A0))) & (6));
    if (((uint8_t)(result)) != 6) goto loc_009F61A0;
    if (*(uint64_t *)(*(uint64_t *)(arg1) + 0x10) == 0) goto loc_009F61A0;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1) + 0x10))) != 0) goto loc_009F61A0;
loc_009F5F93:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) - 16))) & (7));
    if (((uint8_t)(result)) != 3) goto loc_009F61A0;
    if (((uint8_t)(result)) < 3) goto loc_009F61A0;
loc_009F5FB3:
    if (1 == 0) goto loc_009F61A0;
    result = AlpcpAvailableBufferSize(v_stack_mB0, (int16_t)(v_stack_mA0), Arg3, a4);
    if (((int16_t)(v_stack_mA0)) > result) goto loc_009F5FEA;
    result = memcpy(v_stack_mB0 + 280, Arg2 + 40, (int16_t)(v_stack_mA0), a4);
    v_stack_mB8 = 0;
    goto loc_009F5FFC;
loc_009F5FEA:
    result = AlpcpCaptureMessageData(v_stack_mB0, Arg2 + 40, Arg2 + 40, a4);
    v_stack_mB8 = (uint32_t)(result);
loc_009F5FFC:
    goto loc_009F6024;
loc_009F6024:
    if (!sign_flag) goto loc_009F6035;
    result = AlpcpUnlockMessage(v_stack_mB0, Arg2 + 40, Arg2 + 40, a4);
    goto loc_009F61AD;
loc_009F6035:
    result = AlpcpRemoveMessageFromPendingQueue(v_stack_mB0, Arg2 + 40, Arg2 + 40, a4);
    *(uint32_t *)(v_stack_mB0 + 0xF0) = (uint32_t)((uint32_t)(v_stack_mA0));
    *(uint16_t *)(v_stack_mB0 + 0xF4) = 2;
    *(uint64_t *)(v_stack_mB0 + 0xF8) = v_xmm0;
    *(uint32_t *)(v_stack_mB0 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x28)));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x1A0))) >> (1));
    Arg2 = (uint32_t)((Arg2) & (3));
    result = (uint32_t)((Arg2 * 8) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x28)))));
    result = (uint32_t)((result) & (120));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x28)))));
    *(uint32_t *)(v_stack_mB0 + 0x28) = (uint32_t)(result);
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_009F60B4;
    *(uint64_t *)(v_stack_mB0 + 0x78) = *(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x38);
    goto loc_009F612E;
loc_009F60B4:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) - 16, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) - 16;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) - 16;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) + 0x8) != 0) goto loc_009F6102;
    *(uint64_t *)(v_stack_mB0 + 0x78) = 0;
    goto loc_009F610F;
loc_009F6102:
    *(uint64_t *)(v_stack_mB0 + 0x78) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) + 0x8) + 0x38);
loc_009F610F:
    result = 17;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) + 0x8) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) - 16;
        result = ExfReleasePushLockShared(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) + 0x8) + 0x38), Arg3, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) - 16, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) + 0x8) + 0x38), Arg3, a4);
loc_009F612E:
    *(uint64_t *)(v_stack_mB0 + 0x20) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mB0 + 0x28))) & (0xFFFFFFFDULL));
    result = (uint32_t)((result) | (5));
    *(uint32_t *)(v_stack_mB0 + 0x28) = (uint32_t)(result);
    result = AlpcpClearOwnerPortMessage(v_stack_mB0, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) + 0x8) + 0x38), Arg3, a4);
    result = ObfReferenceObject(*(uint64_t *)(arg1), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) + 0x8) + 0x38), Arg3, a4);
    *(uint64_t *)(v_stack_mB0 + 0x18) = *(uint64_t *)(arg1);
    result = AlpcpUnlockMessage(v_stack_mB0, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mB0 + 0x18) + 0x10) + 0x8) + 0x38), Arg3, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x30)))) & (4)) == 0) goto loc_009F6181;
    *(uint64_t *)(v_stack_m70 + 0x18) = *(uint64_t *)(v_stack_mB0 + 0x20);
loc_009F617B:
    goto loc_009F61AD;
loc_009F6181:
    v_stack_mC0 = 0;
    v_stack_mC8 = 0;
    result = KeReleaseSemaphoreEx(*(uint64_t *)(v_stack_mB0 + 0x20) + 1304, 1, 1, a4);
    goto loc_009F617B;
loc_009F61A0:
    result = AlpcpUnlockMessage(*(uint64_t *)(v_stack_mB0 + 0x20), 1, 1, a4);
loc_009F61AD:
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, 1, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x10` | `128` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F5CF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
