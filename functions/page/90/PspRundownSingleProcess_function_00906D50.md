# PspRundownSingleProcess

- RVA: `0x00906D50`–`0x009071BA` (길이 `1,130` bytes)
- VA: `0x0000000140906D50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00088D48`
- 디코드: `274`개 명령, `1,130/1,130` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00906DB8` → [ExWaitForRundownProtectionRelease](../../text/2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (function, `0x002A4CB0`)
- `0x00906DF4` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x00906E05` → [ObKillProcess](ObKillProcess_function_00904F30.md) (function, `0x00904F30`)
- `0x00906E0D` → [MmCleanProcessAddressSpace](../A1/MmCleanProcessAddressSpace_function_00A17EC0.md) (function, `0x00A17EC0`)
- `0x00906E19` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00906E4F` → [AlpcpFreeBuffer](AlpcpFreeBuffer_function_009071C0.md) (function, `0x009071C0`)
- `0x00906E95` → [AlpcpFreeBuffer](AlpcpFreeBuffer_function_009071C0.md) (function, `0x009071C0`)
- `0x00906EC5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00906EF4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00906F0A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00906F25` → [KeSetProcess](../../text/35/KeSetProcess_function_003520E8.md) (function, `0x003520E8`)
- `0x00906F42` → [PspRemoveProcessFromJobChain](PspRemoveProcessFromJobChain_function_00907288.md) (function, `0x00907288`)
- `0x00906F4A` → [PspNotifyEmptyJobsInJobChain](PspNotifyEmptyJobsInJobChain_function_00906D04.md) (function, `0x00906D04`)
- `0x00906F61` → [PspClearProcessThreadCidRefs](PspClearProcessThreadCidRefs_function_009071D8.md) (function, `0x009071D8`)
- `0x00906F71` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0090702A` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (function, `0x00497378`)
- `0x0090703C` → [PspSendProcessNotificationToJobChain](../A4/PspSendProcessNotificationToJobChain_function_00A45ADC.md) (function, `0x00A45ADC`)
- `0x00907049` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (function, `0x00460164`)
- `0x00907085` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x00907096` → [ObReferenceProcessHandleTable](../89/ObReferenceProcessHandleTable_function_00893B70.md) (function, `0x00893B70`)
- `0x009070AD` → [ExSweepHandleTable](ExSweepHandleTable_function_00904D3C.md) (function, `0x00904D3C`)
- `0x009070B9` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00907152` → [KeRundownSecureProcess](../../text/5B/KeRundownSecureProcess_function_005B9868.md) (function, `0x005B9868`)
- `0x00907178` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00907195` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009071A9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PsTerminateMinimalProcess](../78/PsTerminateMinimalProcess_function_007861A8.md) at `0x007862EA`
- [PsCreateMinimalProcess](../78/PsCreateMinimalProcess_function_00786D14.md) at `0x0078700F`
- [PspTerminateAllThreads](../8C/PspTerminateAllThreads_function_008C97D0.md) at `0x008C9A0F`
- [PspExitLastThread](PspExitLastThread_function_00904184.md) at `0x00904265`
- [PspCreateProcess](../A1/PspCreateProcess_function_00A12758.md) at `0x00A12CDF`
- [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A14D01`
- [PspProcessRundownWorkerSingle](../AB/PspProcessRundownWorkerSingle_function_00ABCC10.md) at `0x00ABCC3D`
- [PspProcessRundownWorker](../AC/PspProcessRundownWorker_function_00AC31D0.md) at `0x00AC31FB`
- [PspProcessRundownWorker](../AC/PspProcessRundownWorker_function_00AC31D0.md) at `0x00AC3233`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEB378`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEB49A`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEB581`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEB662`
- [sub_00B20CE6](../B2/Unknown_function_00B20CE6.md) at `0x00B20CF0`

### Static image references
- `0x00906D6C` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00906DB8` → [ExWaitForRundownProtectionRelease](../../text/2A/ExWaitForRundownProtectionRelease_function_002A4CB0.md) (`PAGE` → `.text`)
  - `0x00906DF4` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x00906E19` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00906EC5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00906EF4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00906F0A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00906F25` → [KeSetProcess](../../text/35/KeSetProcess_function_003520E8.md) (`PAGE` → `.text`)
  - `0x00906F71` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0090702A` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (`PAGE` → `.text`)
  - `0x00907049` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (`PAGE` → `.text`)
  - `0x00907085` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x009070B9` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00907152` → [KeRundownSecureProcess](../../text/5B/KeRundownSecureProcess_function_005B9868.md) (`PAGE` → `.text`)
  - `0x00907178` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00907195` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009071A9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00907186` → [sub_00B20E92](../B2/Unknown_function_00B20E92.md) (`tail-transfer`)
  - `0x0090719B` → [sub_00B20E92](../B2/Unknown_function_00B20E92.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00906D50  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00906D55  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00906D5A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00906D5F  57                              push rdi
00906D60  41 54                           push r12
00906D62  41 55                           push r13
00906D64  41 56                           push r14
00906D66  41 57                           push r15
00906D68  48 83 EC 60                     sub rsp, 0x60
00906D6C  48 8B 05 CD 39 50 00            mov rax, qword ptr [rip + 0x5039cd]
00906D73  48 33 C4                        xor rax, rsp
00906D76  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00906D7B  0F 57 C0                        xorps xmm0, xmm0
00906D7E  44 0F B6 F2                     movzx r14d, dl
00906D82  45 33 E4                        xor r12d, r12d
00906D85  48 8B F9                        mov rdi, rcx
00906D88  41 BD 01 00 00 00               mov r13d, 1
00906D8E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00906D93  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
00906D98  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00906D9D  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
00906DA6  84 D2                           test dl, dl
00906DA8  0F 84 98 02 00 00               je 0x140907046
00906DAE  48 8D 9F E8 01 00 00            lea rbx, [rdi + 0x1e8]
00906DB5  48 8B CB                        mov rcx, rbx
00906DB8  E8 F3 DE 99 FF                  call 0x1402a4cb0
00906DBD  49 8B C5                        mov rax, r13
00906DC0  48 87 03                        xchg qword ptr [rbx], rax
00906DC3  48 8B 87 A0 02 00 00            mov rax, qword ptr [rdi + 0x2a0]
00906DCA  48 85 C0                        test rax, rax
00906DCD  0F 85 C2 01 00 00               jne 0x140906f95
00906DD3  4C 39 A7 70 01 00 00            cmp qword ptr [rdi + 0x170], r12
00906DDA  0F 85 6F 03 00 00               jne 0x14090714f
00906DE0  F7 87 F4 01 00 00 00 00 04 00   test dword ptr [rdi + 0x1f4], 0x40000
00906DEA  74 32                           je 0x140906e1e
00906DEC  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00906DF1  48 8B CF                        mov rcx, rdi
00906DF4  E8 07 FA 90 FF                  call 0x140216800
00906DF9  4C 39 A7 00 03 00 00            cmp qword ptr [rdi + 0x300], r12
00906E00  74 08                           je 0x140906e0a
00906E02  48 8B CF                        mov rcx, rdi
00906E05  E8 26 E1 FF FF                  call 0x140904f30
00906E0A  48 8B CF                        mov rcx, rdi
00906E0D  E8 AE 10 11 00                  call 0x140a17ec0
00906E12  33 D2                           xor edx, edx
00906E14  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00906E19  E8 12 0F 91 FF                  call 0x140217d30
00906E1E  4C 39 A7 48 06 00 00            cmp qword ptr [rdi + 0x648], r12
00906E25  0F 85 31 03 00 00               jne 0x14090715c
00906E2B  48 8B 8F 80 07 00 00            mov rcx, qword ptr [rdi + 0x780]
00906E32  48 85 C9                        test rcx, rcx
00906E35  74 33                           je 0x140906e6a
00906E37  48 8B 11                        mov rdx, qword ptr [rcx]
00906E3A  48 85 D2                        test rdx, rdx
00906E3D  75 20                           jne 0x140906e5f
00906E3F  48 8D 41 08                     lea rax, [rcx + 8]
00906E43  48 8B 10                        mov rdx, qword ptr [rax]
00906E46  48 85 D2                        test rdx, rdx
00906E49  75 17                           jne 0x140906e62
00906E4B  48 8B 59 10                     mov rbx, qword ptr [rcx + 0x10]
00906E4F  E8 6C 03 00 00                  call 0x1409071c0
00906E54  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
00906E58  74 10                           je 0x140906e6a
00906E5A  48 8B CB                        mov rcx, rbx
00906E5D  EB D8                           jmp 0x140906e37
00906E5F  48 8B C1                        mov rax, rcx
00906E62  48 8B CA                        mov rcx, rdx
00906E65  4C 89 20                        mov qword ptr [rax], r12
00906E68  EB CD                           jmp 0x140906e37
00906E6A  4C 89 A7 80 07 00 00            mov qword ptr [rdi + 0x780], r12
00906E71  48 8B 8F 90 07 00 00            mov rcx, qword ptr [rdi + 0x790]
00906E78  48 85 C9                        test rcx, rcx
00906E7B  74 33                           je 0x140906eb0
00906E7D  48 8B 11                        mov rdx, qword ptr [rcx]
00906E80  48 85 D2                        test rdx, rdx
00906E83  75 20                           jne 0x140906ea5
00906E85  48 8D 41 08                     lea rax, [rcx + 8]
00906E89  48 8B 10                        mov rdx, qword ptr [rax]
00906E8C  48 85 D2                        test rdx, rdx
00906E8F  75 17                           jne 0x140906ea8
00906E91  48 8B 59 10                     mov rbx, qword ptr [rcx + 0x10]
00906E95  E8 26 03 00 00                  call 0x1409071c0
00906E9A  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
00906E9E  74 10                           je 0x140906eb0
00906EA0  48 8B CB                        mov rcx, rbx
00906EA3  EB D8                           jmp 0x140906e7d
00906EA5  48 8B C1                        mov rax, rcx
00906EA8  48 8B CA                        mov rcx, rdx
00906EAB  4C 89 20                        mov qword ptr [rax], r12
00906EAE  EB CD                           jmp 0x140906e7d
00906EB0  4C 89 A7 90 07 00 00            mov qword ptr [rdi + 0x790], r12
00906EB7  48 8B 8F A8 01 00 00            mov rcx, qword ptr [rdi + 0x1a8]
00906EBE  48 85 C9                        test rcx, rcx
00906EC1  74 0E                           je 0x140906ed1
00906EC3  33 D2                           xor edx, edx
00906EC5  E8 A6 B9 27 00                  call 0x140b82870
00906ECA  4C 89 A7 A8 01 00 00            mov qword ptr [rdi + 0x1a8], r12
00906ED1  48 8B 87 B0 07 00 00            mov rax, qword ptr [rdi + 0x7b0]
00906ED8  48 85 C0                        test rax, rax
00906EDB  0F 85 BF 02 00 00               jne 0x1409071a0
00906EE1  48 8B 8F A8 02 00 00            mov rcx, qword ptr [rdi + 0x2a8]
00906EE8  48 85 C9                        test rcx, rcx
00906EEB  74 0C                           je 0x140906ef9
00906EED  4C 89 A7 A8 02 00 00            mov qword ptr [rdi + 0x2a8], r12
00906EF4  E8 57 24 9F FF                  call 0x1402f9350
00906EF9  48 8B 8F 30 03 00 00            mov rcx, qword ptr [rdi + 0x330]
00906F00  48 85 C9                        test rcx, rcx
00906F03  74 11                           je 0x140906f16
00906F05  BA 50 73 43 72                  mov edx, 0x72437350
00906F0A  E8 D1 09 9F FF                  call 0x1402f78e0
00906F0F  4C 89 A7 30 03 00 00            mov qword ptr [rdi + 0x330], r12
00906F16  F7 87 F4 01 00 00 00 00 04 00   test dword ptr [rdi + 0x1f4], 0x40000
00906F20  74 08                           je 0x140906f2a
00906F22  48 8B CF                        mov rcx, rdi
00906F25  E8 BE B1 A4 FF                  call 0x1403520e8
00906F2A  48 8B 87 A0 02 00 00            mov rax, qword ptr [rdi + 0x2a0]
00906F31  48 85 C0                        test rax, rax
00906F34  74 19                           je 0x140906f4f
00906F36  45 33 C9                        xor r9d, r9d
00906F39  33 D2                           xor edx, edx
00906F3B  48 8B CF                        mov rcx, rdi
00906F3E  45 8D 41 04                     lea r8d, [r9 + 4]
00906F42  E8 41 03 00 00                  call 0x140907288
00906F47  48 8B CF                        mov rcx, rdi
00906F4A  E8 B5 FD FF FF                  call 0x140906d04
00906F4F  48 8B 97 D0 01 00 00            mov rdx, qword ptr [rdi + 0x1d0]
00906F56  48 85 D2                        test rdx, rdx
00906F59  74 0B                           je 0x140906f66
00906F5B  4C 8B C7                        mov r8, rdi
00906F5E  49 8B CF                        mov rcx, r15
00906F61  E8 72 02 00 00                  call 0x1409071d8
00906F66  41 8A C6                        mov al, r14b
00906F69  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00906F6E  48 33 CC                        xor rcx, rsp
00906F71  E8 CA 56 DA FF                  call 0x1406ac640
00906F76  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00906F7B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00906F7F  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
00906F83  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00906F87  49 8B E3                        mov rsp, r11
00906F8A  41 5F                           pop r15
00906F8C  41 5E                           pop r14
00906F8E  41 5D                           pop r13
00906F90  41 5C                           pop r12
00906F92  5F                              pop rdi
00906F93  C3                              ret
00906F94  CC                              int3
00906F95  48 8D 8F F0 01 00 00            lea rcx, [rdi + 0x1f0]
00906F9C  8B 01                           mov eax, dword ptr [rcx]
00906F9E  41 84 C5                        test r13b, al
00906FA1  0F 85 2C FE FF FF               jne 0x140906dd3
00906FA7  8B 87 54 05 00 00               mov eax, dword ptr [rdi + 0x554]
00906FAD  BA 8F 00 00 C0                  mov edx, 0xc000008f
00906FB2  41 B9 08 00 00 00               mov r9d, 8
00906FB8  3B C2                           cmp eax, edx
00906FBA  0F 8F 03 01 00 00               jg 0x1409070c3
00906FC0  0F 84 81 01 00 00               je 0x140907147
00906FC6  BA 1D 00 00 C0                  mov edx, 0xc000001d
00906FCB  3B C2                           cmp eax, edx
00906FCD  0F 8F 1F 01 00 00               jg 0x1409070f2
00906FD3  0F 84 6E 01 00 00               je 0x140907147
00906FD9  3D 01 00 00 80                  cmp eax, 0x80000001
00906FDE  0F 84 63 01 00 00               je 0x140907147
00906FE4  3D 02 00 00 80                  cmp eax, 0x80000002
00906FE9  0F 84 58 01 00 00               je 0x140907147
00906FEF  3D 03 00 00 80                  cmp eax, 0x80000003
00906FF4  0F 84 4D 01 00 00               je 0x140907147
00906FFA  3D 04 00 00 80                  cmp eax, 0x80000004
00906FFF  0F 84 42 01 00 00               je 0x140907147
00907005  3D 05 00 00 C0                  cmp eax, 0xc0000005
0090700A  0F 84 37 01 00 00               je 0x140907147
00907010  3D 06 00 00 C0                  cmp eax, 0xc0000006
00907015  41 BB 07 00 00 00               mov r11d, 7
0090701B  0F 84 26 01 00 00               je 0x140907147
00907021  41 B8 20 00 00 00               mov r8d, 0x20
00907027  41 8B D1                        mov edx, r9d
0090702A  E8 49 03 B9 FF                  call 0x140497378
0090702F  4C 8B 87 D0 01 00 00            mov r8, qword ptr [rdi + 0x1d0]
00907036  49 8B D3                        mov rdx, r11
00907039  48 8B CF                        mov rcx, rdi
0090703C  E8 9B EA 13 00                  call 0x140a45adc
00907041  E9 8D FD FF FF                  jmp 0x140906dd3
00907046  49 8B D7                        mov rdx, r15
00907049  E8 16 91 B5 FF                  call 0x140460164
0090704E  8B 87 80 03 00 00               mov eax, dword ptr [rdi + 0x380]
00907054  85 C0                           test eax, eax
00907056  75 27                           jne 0x14090707f
00907058  0F 0D 8F F4 01 00 00            prefetchw byte ptr [rdi + 0x1f4]
0090705F  8B 87 F4 01 00 00               mov eax, dword ptr [rdi + 0x1f4]
00907065  8B C8                           mov ecx, eax
00907067  81 C9 08 00 00 02               or ecx, 0x2000008
0090706D  F0 0F B1 8F F4 01 00 00         lock cmpxchg dword ptr [rdi + 0x1f4], ecx
00907075  75 EE                           jne 0x140907065
00907077  0F BA E0 19                     bt eax, 0x19
0090707B  45 0F 43 F5                     cmovae r14d, r13d
0090707F  49 8B D7                        mov rdx, r15
00907082  48 8B CF                        mov rcx, rdi
00907085  E8 36 91 B5 FF                  call 0x1404601c0
0090708A  45 84 F6                        test r14b, r14b
0090708D  0F 85 1B FD FF FF               jne 0x140906dae
00907093  48 8B CF                        mov rcx, rdi
00907096  E8 D5 CA F8 FF                  call 0x140893b70
0090709B  48 85 C0                        test rax, rax
0090709E  0F 84 C2 FE FF FF               je 0x140906f66
009070A4  45 8A C5                        mov r8b, r13b
009070A7  48 8B D0                        mov rdx, rax
009070AA  48 8B CF                        mov rcx, rdi
009070AD  E8 8A DC FF FF                  call 0x140904d3c
009070B2  48 8D 8F E8 01 00 00            lea rcx, [rdi + 0x1e8]
009070B9  E8 C2 2D A4 FF                  call 0x140349e80
009070BE  E9 A3 FE FF FF                  jmp 0x140906f66
009070C3  BA 96 00 00 C0                  mov edx, 0xc0000096
009070C8  3B C2                           cmp eax, edx
009070CA  7E 4C                           jle 0x140907118
009070CC  3D FD 00 00 C0                  cmp eax, 0xc00000fd
009070D1  74 74                           je 0x140907147
009070D3  3D 3A 01 00 C0                  cmp eax, 0xc000013a
009070D8  74 6D                           je 0x140907147
009070DA  3D B4 02 00 C0                  cmp eax, 0xc00002b4
009070DF  74 66                           je 0x140907147
009070E1  3D B5 02 00 C0                  cmp eax, 0xc00002b5
009070E6  74 5F                           je 0x140907147
009070E8  3D C9 02 00 C0                  cmp eax, 0xc00002c9
009070ED  E9 23 FF FF FF                  jmp 0x140907015
009070F2  3D 25 00 00 C0                  cmp eax, 0xc0000025
009070F7  74 4E                           je 0x140907147
009070F9  3D 26 00 00 C0                  cmp eax, 0xc0000026
009070FE  74 47                           je 0x140907147
00907100  3D 8C 00 00 C0                  cmp eax, 0xc000008c
00907105  74 40                           je 0x140907147
00907107  3D 8D 00 00 C0                  cmp eax, 0xc000008d
0090710C  74 39                           je 0x140907147
0090710E  3D 8E 00 00 C0                  cmp eax, 0xc000008e
00907113  E9 FD FE FF FF                  jmp 0x140907015
00907118  74 2D                           je 0x140907147
0090711A  3D 90 00 00 C0                  cmp eax, 0xc0000090
0090711F  74 26                           je 0x140907147
00907121  3D 91 00 00 C0                  cmp eax, 0xc0000091
00907126  74 1F                           je 0x140907147
00907128  3D 92 00 00 C0                  cmp eax, 0xc0000092
0090712D  74 18                           je 0x140907147
0090712F  3D 93 00 00 C0                  cmp eax, 0xc0000093
00907134  74 11                           je 0x140907147
00907136  3D 94 00 00 C0                  cmp eax, 0xc0000094
0090713B  74 0A                           je 0x140907147
0090713D  3D 95 00 00 C0                  cmp eax, 0xc0000095
00907142  E9 CE FE FF FF                  jmp 0x140907015
00907147  4D 8B D9                        mov r11, r9
0090714A  E9 D2 FE FF FF                  jmp 0x140907021
0090714F  48 8B CF                        mov rcx, rdi
00907152  E8 11 27 CB FF                  call 0x1405b9868
00907157  E9 84 FC FF FF                  jmp 0x140906de0
0090715C  48 83 CB FF                     or rbx, 0xffffffffffffffff
00907160  48 8D B7 58 06 00 00            lea rsi, [rdi + 0x658]
00907167  66 41 01 9F E4 01 00 00         add word ptr [r15 + 0x1e4], bx
0090716F  48 8B CE                        mov rcx, rsi
00907172  45 33 C0                        xor r8d, r8d
00907175  33 D2                           xor edx, edx
00907177  90                              nop
00907178  E8 B3 90 90 FF                  call 0x140210230
0090717D  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00907183  48 8B E8                        mov rbp, rax
00907186  0F 83 06 9D 21 00               jae 0x140b20e92
0090718C  4C 8B C6                        mov r8, rsi
0090718F  48 8B D0                        mov rdx, rax
00907192  48 8B CE                        mov rcx, rsi
00907195  E8 F6 8A 90 FF                  call 0x14020fc90
0090719A  90                              nop
0090719B  E9 F2 9C 21 00                  jmp 0x140b20e92
009071A0  48 8B 8F B0 07 00 00            mov rcx, qword ptr [rdi + 0x7b0]
009071A7  33 D2                           xor edx, edx
009071A9  E8 C2 B6 27 00                  call 0x140b82870
009071AE  4C 89 A7 B0 07 00 00            mov qword ptr [rdi + 0x7b0], r12
009071B5  E9 27 FD FF FF                  jmp 0x140906ee1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspRundownSingleProcess(__int64 a1, unsigned __int8 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 5257677)) ^ (v_rsp);
    v_stack_m38 = result;
    v_r12 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    if (a2 == 0) goto loc_00907046;
loc_00906DAE:
    result = ExWaitForRundownProtectionRelease(a1 + 488, a2, a3, a4);
    if (*(unsigned __int64 *)(a1 + 672) != 0) goto loc_00906F95;
loc_00906DD3:
    if ((*(unsigned __int64 *)(a1 + 368)) != 0) goto loc_0090714F;
loc_00906DE0:
    if (((*(unsigned int *)(a1 + 500)) & (0x40000ULL)) == 0) goto loc_00906E1E;
    result = KeStackAttachProcess(a1, v_stack_m68, a3, a4);
    if ((*(unsigned __int64 *)(a1 + 768)) != 0) {
        a1 = a1;
        result = ObKillProcess(a1, v_stack_m68, a3, a4);
    }
    result = MmCleanProcessAddressSpace(a1, v_stack_m68, a3, a4);
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m68, a2, a3, a4);
loc_00906E1E:
    if ((*(unsigned __int64 *)(a1 + 1608)) != 0) goto loc_0090715C;
    if (*(unsigned __int64 *)(a1 + 1920) == 0) goto loc_00906E6A;
loc_00906E37:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1920)) != 0) goto loc_00906E5F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1920) + 8) != 0) goto loc_00906E62;
    result = AlpcpFreeBuffer(*(unsigned __int64 *)(a1 + 1920), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1920) + 8), a3, a4);
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1920) + 16)) & (-4);
    if (condition_is_equal) goto loc_00906E6A;
    goto loc_00906E37;
loc_00906E5F:
loc_00906E62:
    *(unsigned __int64 *)(v_rbx) = 0;
    goto loc_00906E37;
loc_00906E6A:
    *(unsigned __int64 *)(a1 + 1920) = 0;
    if (*(unsigned __int64 *)(a1 + 1936) == 0) goto loc_00906EB0;
loc_00906E7D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1936)) != 0) goto loc_00906EA5;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1936) + 8) != 0) goto loc_00906EA8;
    result = AlpcpFreeBuffer(*(unsigned __int64 *)(a1 + 1936), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1936) + 8), a3, a4);
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1936) + 16)) & (-4);
    if (condition_is_equal) goto loc_00906EB0;
    goto loc_00906E7D;
loc_00906EA5:
loc_00906EA8:
    *(unsigned __int64 *)(v_rbx) = 0;
    goto loc_00906E7D;
loc_00906EB0:
    *(unsigned __int64 *)(a1 + 1936) = 0;
    result = v_rbx;
    if (*(unsigned __int64 *)(a1 + 424) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 424), a2, a3, a4);
        *(unsigned __int64 *)(a1 + 424) = 0;
    }
    if (*(unsigned __int64 *)(a1 + 1968) != 0) goto loc_009071A0;
loc_00906EE1:
    result = *(unsigned __int64 *)(a1 + 1968);
    if (*(unsigned __int64 *)(a1 + 680) != 0) {
        *(unsigned __int64 *)(a1 + 680) = 0;
        result = ObfDereferenceObject(*(unsigned __int64 *)(a1 + 680), a2, a3, a4);
    }
    if (*(unsigned __int64 *)(a1 + 816) != 0) {
        a2 = 0x72437350ULL;
        result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(a1 + 816), a2, a3, a4);
        *(unsigned __int64 *)(a1 + 816) = 0;
    }
    if (((*(unsigned int *)(a1 + 500)) & (0x40000ULL)) != 0) {
        a1 = a1;
        result = KeSetProcess(a1, a2, a3, a4);
    }
    result = *(unsigned __int64 *)(a1 + 672);
    if (*(unsigned __int64 *)(a1 + 672) != 0) {
        a4 = 0;
        a2 = 0;
        a1 = a1;
        a3 = a4 + 4;
        result = PspRemoveProcessFromJobChain(a1, a2, a3, a4);
        a1 = a1;
        result = PspNotifyEmptyJobsInJobChain(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(a1 + 464) != 0) {
        a3 = a1;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = PspClearProcessThreadCidRefs(a1, *(unsigned __int64 *)(a1 + 464), a3, a4);
    }
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a1 + 464), a3, a4);
    return result;
loc_00906F95:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 496))))) != 0) goto loc_00906DD3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1364)))) > ((unsigned int)((unsigned int)(0xC000008FULL)))) goto loc_009070C3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1364)))) == ((unsigned int)((unsigned int)(0xC000008FULL)))) goto loc_00907147;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1364)))) > ((unsigned int)((unsigned int)(0xC000001DULL)))) goto loc_009070F2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1364)))) == ((unsigned int)((unsigned int)(0xC000001DULL)))) goto loc_00907147;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1364)))) == 0x80000001ULL) goto loc_00907147;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1364)))) == 0x80000002ULL) goto loc_00907147;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1364)))) == 0x80000003ULL) goto loc_00907147;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1364)))) == 0x80000004ULL) goto loc_00907147;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1364)))) == 0xC0000005ULL) goto loc_00907147;
loc_00907015:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1364)))) == 0xC0000006ULL) goto loc_00907147;
loc_00907021:
    result = RtlInterlockedSetClearBits(a1 + 496, 8, 32, 8);
    result = PspSendProcessNotificationToJobChain(a1, 7, *(unsigned __int64 *)(a1 + 464), 8);
    goto loc_00906DD3;
loc_00907046:
    result = PspLockProcessExclusive(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(a1 + 464), 8);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 896))) != 0) goto loc_0090707F;
loc_00907065:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 500))))) | (0x2000008ULL));
    if (condition_is_not_equal) goto loc_00907065;
    if (condition_is_above_or_equal) { a2 = 1; }
loc_0090707F:
    result = PspUnlockProcessExclusive(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(a1 + 464), 8);
    if (a2 != 0) goto loc_00906DAE;
    result = ObReferenceProcessHandleTable(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(a1 + 464), 8);
    if (result == 0) goto loc_00906F66;
    result = ExSweepHandleTable(a1, result, 1, 8);
    result = ExReleaseRundownProtection(a1 + 488, result, 1, 8);
    goto loc_00906F66;
loc_009070C3:
    if (((unsigned int)(result)) <= ((unsigned int)((unsigned int)(0xC0000096ULL)))) goto loc_00907118;
    if (((unsigned int)(result)) == 0xC00000FDULL) goto loc_00907147;
    if (((unsigned int)(result)) == 0xC000013AULL) goto loc_00907147;
    if (((unsigned int)(result)) == 0xC00002B4ULL) goto loc_00907147;
    if (((unsigned int)(result)) == 0xC00002B5ULL) goto loc_00907147;
    goto loc_00907015;
loc_009070F2:
    if (((unsigned int)(result)) == 0xC0000025ULL) goto loc_00907147;
    if (((unsigned int)(result)) == 0xC0000026ULL) goto loc_00907147;
    if (((unsigned int)(result)) == 0xC000008CULL) goto loc_00907147;
    if (((unsigned int)(result)) == 0xC000008DULL) goto loc_00907147;
    goto loc_00907015;
loc_00907118:
    if (((unsigned int)(result)) == 0xC000008EULL) goto loc_00907147;
    if (((unsigned int)(result)) == 0xC0000090ULL) goto loc_00907147;
    if (((unsigned int)(result)) == 0xC0000091ULL) goto loc_00907147;
    if (((unsigned int)(result)) == 0xC0000092ULL) goto loc_00907147;
    if (((unsigned int)(result)) == 0xC0000093ULL) goto loc_00907147;
    if (((unsigned int)(result)) == 0xC0000094ULL) goto loc_00907147;
    goto loc_00907015;
loc_00907147:
    goto loc_00907021;
loc_0090714F:
    result = KeRundownSecureProcess(a1, (unsigned int)(0xC0000096ULL), 1, 8);
    goto loc_00906DE0;
loc_0090715C:
    v_rbx = (*(unsigned __int64 *)(v_stack_m28 + 56)) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 1624, a2, a3, 8);
    result = ExfAcquirePushLockExclusiveEx(a1 + 1624, result, a1 + 1624, 8);
loc_009071A0:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 1968), a2, a1 + 1624, 8);
    *(unsigned __int64 *)(a1 + 1968) = 0;
    goto loc_00906EE1;
}
```

## 5. (Beta) C Style

```c
int64_t PspRundownSingleProcess(void *Arg1, uint8_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0x5039CD)) ^ (local_rsp);
    v_stack_m38 = result;
    local_r12 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    if (Arg2 == 0) goto loc_00907046;
loc_00906DAE:
    result = ExWaitForRundownProtectionRelease(Arg1 + 488, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(arg1 + 0x2A0) != 0) goto loc_00906F95;
loc_00906DD3:
    if ((*(uint64_t *)(arg1 + 0x170)) != 0) goto loc_0090714F;
loc_00906DE0:
    if (((*(uint32_t *)(arg1 + 0x1F4)) & (0x40000ULL)) == 0) goto loc_00906E1E;
    result = KeStackAttachProcess(Arg1, v_stack_m68, Arg3, Arg4);
    if ((*(uint64_t *)(arg1 + 0x300)) != 0) {
        Arg1 = Arg1;
        result = ObKillProcess(Arg1, v_stack_m68, Arg3, Arg4);
    }
    result = MmCleanProcessAddressSpace(Arg1, v_stack_m68, Arg3, Arg4);
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m68, Arg2, Arg3, Arg4);
loc_00906E1E:
    if ((*(uint64_t *)(arg1 + 0x648)) != 0) goto loc_0090715C;
    if (*(uint64_t *)(arg1 + 0x780) == 0) goto loc_00906E6A;
loc_00906E37:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x780)) != 0) goto loc_00906E5F;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x780) + 0x8) != 0) goto loc_00906E62;
    result = AlpcpFreeBuffer(*(uint64_t *)(arg1 + 0x780), *(uint64_t *)(*(uint64_t *)(arg1 + 0x780) + 0x8), Arg3, Arg4);
    local_rbx = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x780) + 0x10)) & (-4);
    if (condition_is_equal) goto loc_00906E6A;
    goto loc_00906E37;
loc_00906E5F:
loc_00906E62:
    *(uint64_t *)(local_rbx) = 0;
    goto loc_00906E37;
loc_00906E6A:
    *(uint64_t *)(arg1 + 0x780) = 0;
    if (*(uint64_t *)(arg1 + 0x790) == 0) goto loc_00906EB0;
loc_00906E7D:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x790)) != 0) goto loc_00906EA5;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x790) + 0x8) != 0) goto loc_00906EA8;
    result = AlpcpFreeBuffer(*(uint64_t *)(arg1 + 0x790), *(uint64_t *)(*(uint64_t *)(arg1 + 0x790) + 0x8), Arg3, Arg4);
    local_rbx = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x790) + 0x10)) & (-4);
    if (condition_is_equal) goto loc_00906EB0;
    goto loc_00906E7D;
loc_00906EA5:
loc_00906EA8:
    *(uint64_t *)(local_rbx) = 0;
    goto loc_00906E7D;
loc_00906EB0:
    *(uint64_t *)(arg1 + 0x790) = 0;
    result = local_rbx;
    if (*(uint64_t *)(arg1 + 0x1A8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x1A8), Arg2, Arg3, Arg4);
        *(uint64_t *)(arg1 + 0x1A8) = 0;
    }
    if (*(uint64_t *)(arg1 + 0x7B0) != 0) goto loc_009071A0;
loc_00906EE1:
    result = *(uint64_t *)(arg1 + 0x7B0);
    if (*(uint64_t *)(arg1 + 0x2A8) != 0) {
        *(uint64_t *)(arg1 + 0x2A8) = 0;
        result = ObfDereferenceObject(*(uint64_t *)(arg1 + 0x2A8), Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(arg1 + 0x330) != 0) {
        Arg2 = 0x72437350ULL;
        result = ObfDereferenceObjectWithTag(*(uint64_t *)(arg1 + 0x330), Arg2, Arg3, Arg4);
        *(uint64_t *)(arg1 + 0x330) = 0;
    }
    if (((*(uint32_t *)(arg1 + 0x1F4)) & (0x40000ULL)) != 0) {
        Arg1 = Arg1;
        result = KeSetProcess(Arg1, Arg2, Arg3, Arg4);
    }
    result = *(uint64_t *)(arg1 + 0x2A0);
    if (*(uint64_t *)(arg1 + 0x2A0) != 0) {
        Arg4 = 0;
        Arg2 = 0;
        Arg1 = Arg1;
        Arg3 = Arg4 + 4;
        result = PspRemoveProcessFromJobChain(Arg1, Arg2, Arg3, Arg4);
        Arg1 = Arg1;
        result = PspNotifyEmptyJobsInJobChain(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(arg1 + 0x1D0) != 0) {
        Arg3 = Arg1;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = PspClearProcessThreadCidRefs(Arg1, *(uint64_t *)(arg1 + 0x1D0), Arg3, Arg4);
    }
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(arg1 + 0x1D0), Arg3, Arg4);
    return result;
loc_00906F95:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1F0))))) != 0) goto loc_00906DD3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x554)))) > ((uint32_t)((uint32_t)(0xC000008FULL)))) goto loc_009070C3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x554)))) == ((uint32_t)((uint32_t)(0xC000008FULL)))) goto loc_00907147;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x554)))) > ((uint32_t)((uint32_t)(0xC000001DULL)))) goto loc_009070F2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x554)))) == ((uint32_t)((uint32_t)(0xC000001DULL)))) goto loc_00907147;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x554)))) == 0x80000001ULL) goto loc_00907147;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x554)))) == 0x80000002ULL) goto loc_00907147;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x554)))) == 0x80000003ULL) goto loc_00907147;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x554)))) == 0x80000004ULL) goto loc_00907147;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x554)))) == 0xC0000005ULL) goto loc_00907147;
loc_00907015:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x554)))) == 0xC0000006ULL) goto loc_00907147;
loc_00907021:
    result = RtlInterlockedSetClearBits(Arg1 + 496, 8, 32, 8);
    result = PspSendProcessNotificationToJobChain(Arg1, 7, *(uint64_t *)(arg1 + 0x1D0), 8);
    goto loc_00906DD3;
loc_00907046:
    result = PspLockProcessExclusive(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(arg1 + 0x1D0), 8);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x380))) != 0) goto loc_0090707F;
loc_00907065:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1F4))))) | (0x2000008ULL));
    if (condition_is_not_equal) goto loc_00907065;
    if (condition_is_above_or_equal) { Arg2 = 1; }
loc_0090707F:
    result = PspUnlockProcessExclusive(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(arg1 + 0x1D0), 8);
    if (Arg2 != 0) goto loc_00906DAE;
    result = ObReferenceProcessHandleTable(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(arg1 + 0x1D0), 8);
    if (result == 0) goto loc_00906F66;
    result = ExSweepHandleTable(Arg1, result, 1, 8);
    result = ExReleaseRundownProtection(Arg1 + 488, result, 1, 8);
    goto loc_00906F66;
loc_009070C3:
    if (((uint32_t)(result)) <= ((uint32_t)((uint32_t)(0xC0000096ULL)))) goto loc_00907118;
    if (((uint32_t)(result)) == 0xC00000FDULL) goto loc_00907147;
    if (((uint32_t)(result)) == 0xC000013AULL) goto loc_00907147;
    if (((uint32_t)(result)) == 0xC00002B4ULL) goto loc_00907147;
    if (((uint32_t)(result)) == 0xC00002B5ULL) goto loc_00907147;
    goto loc_00907015;
loc_009070F2:
    if (((uint32_t)(result)) == 0xC0000025ULL) goto loc_00907147;
    if (((uint32_t)(result)) == 0xC0000026ULL) goto loc_00907147;
    if (((uint32_t)(result)) == 0xC000008CULL) goto loc_00907147;
    if (((uint32_t)(result)) == 0xC000008DULL) goto loc_00907147;
    goto loc_00907015;
loc_00907118:
    if (((uint32_t)(result)) == 0xC000008EULL) goto loc_00907147;
    if (((uint32_t)(result)) == 0xC0000090ULL) goto loc_00907147;
    if (((uint32_t)(result)) == 0xC0000091ULL) goto loc_00907147;
    if (((uint32_t)(result)) == 0xC0000092ULL) goto loc_00907147;
    if (((uint32_t)(result)) == 0xC0000093ULL) goto loc_00907147;
    if (((uint32_t)(result)) == 0xC0000094ULL) goto loc_00907147;
    goto loc_00907015;
loc_00907147:
    goto loc_00907021;
loc_0090714F:
    result = KeRundownSecureProcess(Arg1, (uint32_t)(0xC0000096ULL), 1, 8);
    goto loc_00906DE0;
loc_0090715C:
    local_rbx = (*(uint64_t *)(v_stack_m28 + 0x38)) | (-1);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 1624, Arg2, Arg3, 8);
    result = ExfAcquirePushLockExclusiveEx(Arg1 + 1624, result, Arg1 + 1624, 8);
loc_009071A0:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x7B0), Arg2, Arg1 + 1624, 8);
    *(uint64_t *)(arg1 + 0x7B0) = 0;
    goto loc_00906EE1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x170` | `64` | `R` |
| `Arg1` | `+ 0x1A8` | `64` | `R` |
| `Arg1` | `+ 0x1A8` | `64` | `W` |
| `Arg1` | `+ 0x1D0` | `64` | `R` |
| `Arg1` | `+ 0x1E8` | `64` | `R` |
| `Arg1` | `+ 0x1F0` | `64` | `R` |
| `Arg1` | `+ 0x1F4` | `8` | `R` |
| `Arg1` | `+ 0x1F4` | `32` | `R` |
| `Arg1` | `+ 0x2A0` | `64` | `R` |
| `Arg1` | `+ 0x2A8` | `64` | `R` |
| `Arg1` | `+ 0x2A8` | `64` | `W` |
| `Arg1` | `+ 0x300` | `64` | `R` |
| `Arg1` | `+ 0x330` | `64` | `R` |
| `Arg1` | `+ 0x330` | `64` | `W` |
| `Arg1` | `+ 0x380` | `32` | `R` |
| `Arg1` | `+ 0x554` | `32` | `R` |
| `Arg1` | `+ 0x648` | `64` | `R` |
| `Arg1` | `+ 0x658` | `64` | `R` |
| `Arg1` | `+ 0x780` | `64` | `R` |
| `Arg1` | `+ 0x780` | `64` | `W` |
| `Arg1` | `+ 0x790` | `64` | `R` |
| `Arg1` | `+ 0x790` | `64` | `W` |
| `Arg1` | `+ 0x7B0` | `64` | `R` |
| `Arg1` | `+ 0x7B0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00906D50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
