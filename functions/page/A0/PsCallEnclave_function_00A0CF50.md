# PsCallEnclave

- RVA: `0x00A0CF50`–`0x00A0D5EA` (길이 `1,690` bytes)
- VA: `0x0000000140A0CF50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A8BD8`
- 디코드: `384`개 명령, `1,690/1,690` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00A0D009` → [PspSelectVsmEnclaveByNumber](PspSelectVsmEnclaveByNumber_function_00A0D610.md) (function, `0x00A0D610`)
- `0x00A0D033` → [PsGetBaseTrapFrame](../../text/44/PsGetBaseTrapFrame_function_004484B0.md) (function, `0x004484B0`)
- `0x00A0D082` → [RtlPrepareEnclaveCall](../../text/46/RtlPrepareEnclaveCall_function_0046CA58.md) (function, `0x0046CA58`)
- `0x00A0D0A2` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00A0D0CA` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A0D0E4` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00A0D103` → [PspFindVsmEnclaveThread](PspFindVsmEnclaveThread_function_00A0D5F0.md) (function, `0x00A0D5F0`)
- `0x00A0D143` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A0D14B` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00A0D1D0` → [VslCallEnclave](VslCallEnclave_function_00A0D838.md) (function, `0x00A0D838`)
- `0x00A0D200` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00A0D291` → [RtlCreateEnclaveReturnFrame](../../text/4B/RtlCreateEnclaveReturnFrame_function_004B3728.md) (function, `0x004B3728`)
- `0x00A0D2B1` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00A0D2D4` → [PsDereferenceVsmEnclave](PsDereferenceVsmEnclave_function_00A0D7D4.md) (function, `0x00A0D7D4`)
- `0x00A0D31B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A0D334` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00A0D358` → [PspFindVsmEnclaveThread](PspFindVsmEnclaveThread_function_00A0D5F0.md) (function, `0x00A0D5F0`)
- `0x00A0D37E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A0D386` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00A0D3C7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A0D3E3` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00A0D40C` → [PspReleaseEnclaveThread](PspReleaseEnclaveThread_function_00A0DA54.md) (function, `0x00A0DA54`)
- `0x00A0D426` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A0D42E` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00A0D4A6` → [PspPrepareEnclaveThreadWait](../AD/PspPrepareEnclaveThreadWait_function_00ADB80C.md) (function, `0x00ADB80C`)
- `0x00A0D501` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00A0D50E` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00A0D51B` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00A0D552` → [MmSelectVsmEnclaveByAddress](../A6/MmSelectVsmEnclaveByAddress_function_00A600B4.md) (function, `0x00A600B4`)
- `0x00A0D57C` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00A0D5A7` → [ZwTerminateProcess](../../text/6A/ZwTerminateProcess_function_006AD650.md) (function, `0x006AD650`)

### Direct callers
- [NtCallEnclave](../../text/6B/NtCallEnclave_function_006BABA0.md) at `0x006BABD3`

### Static image references
- `0x00A0D06E` → RVA `0x00FC74F8` (`ALMOSTRO`; read)
- `0x00A0D075` → RVA `0x00FC74E8` (`ALMOSTRO`; read)
- `0x00A0D285` → RVA `0x00FC74F0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x00A0D033` → [PsGetBaseTrapFrame](../../text/44/PsGetBaseTrapFrame_function_004484B0.md) (`PAGE` → `.text`)
  - `0x00A0D082` → [RtlPrepareEnclaveCall](../../text/46/RtlPrepareEnclaveCall_function_0046CA58.md) (`PAGE` → `.text`)
  - `0x00A0D0A2` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00A0D0CA` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A0D0E4` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00A0D143` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A0D14B` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00A0D200` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00A0D291` → [RtlCreateEnclaveReturnFrame](../../text/4B/RtlCreateEnclaveReturnFrame_function_004B3728.md) (`PAGE` → `.text`)
  - `0x00A0D2B1` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x00A0D31B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A0D334` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00A0D37E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A0D386` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00A0D3C7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A0D3E3` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00A0D426` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A0D42E` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00A0D501` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00A0D50E` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00A0D51B` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00A0D57C` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00A0D5A7` → [ZwTerminateProcess](../../text/6A/ZwTerminateProcess_function_006AD650.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00A0D2B9` → [sub_00B36710 + 0x102](../B3/Unknown_function_00B36710.md) (`tail-transfer`)
  - `0x00A0D495` → [sub_00B36710](../B3/Unknown_function_00B36710.md) (`tail-transfer`)
  - `0x00A0D573` → [sub_00B36710 + 0xE](../B3/Unknown_function_00B36710.md) (`tail-transfer`)
  - `0x00A0D582` → [sub_00B36710 + 0xE](../B3/Unknown_function_00B36710.md) (`tail-transfer`)
  - `0x00A0D5C1` → [sub_00B36710 + 0x1ED](../B3/Unknown_function_00B36710.md) (`tail-transfer`)
  - `0x00A0D5E5` → [sub_00B36710 + 0x1ED](../B3/Unknown_function_00B36710.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A0CF50  48 8B C4                        mov rax, rsp
00A0CF53  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00A0CF57  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00A0CF5B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00A0CF5F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00A0CF63  53                              push rbx
00A0CF64  56                              push rsi
00A0CF65  57                              push rdi
00A0CF66  41 54                           push r12
00A0CF68  41 55                           push r13
00A0CF6A  41 56                           push r14
00A0CF6C  41 57                           push r15
00A0CF6E  48 81 EC B0 00 00 00            sub rsp, 0xb0
00A0CF75  49 8B D9                        mov rbx, r9
00A0CF78  4C 8B E2                        mov r12, rdx
00A0CF7B  33 FF                           xor edi, edi
00A0CF7D  48 89 78 90                     mov qword ptr [rax - 0x70], rdi
00A0CF81  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
00A0CF86  48 89 78 A8                     mov qword ptr [rax - 0x58], rdi
00A0CF8A  48 89 78 B0                     mov qword ptr [rax - 0x50], rdi
00A0CF8E  40 88 7C 24 50                  mov byte ptr [rsp + 0x50], dil
00A0CF93  48 89 78 C0                     mov qword ptr [rax - 0x40], rdi
00A0CF97  65 4C 8B 34 25 88 01 00 00      mov r14, qword ptr gs:[0x188]
00A0CFA0  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
00A0CFA5  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00A0CFAA  44 8D 6F 01                     lea r13d, [rdi + 1]
00A0CFAE  45 38 AE 32 02 00 00            cmp byte ptr [r14 + 0x232], r13b
00A0CFB5  0F 85 6A 05 00 00               jne 0x140a0d525
00A0CFBB  48 39 78 08                     cmp qword ptr [rax + 8], rdi
00A0CFBF  0F 85 2A 05 00 00               jne 0x140a0d4ef
00A0CFC5  48 85 D2                        test rdx, rdx
00A0CFC8  0F 84 61 05 00 00               je 0x140a0d52f
00A0CFCE  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00A0CFD8  48 3B D9                        cmp rbx, rcx
00A0CFDB  48 0F 42 CB                     cmovb rcx, rbx
00A0CFDF  48 8B 01                        mov rax, qword ptr [rcx]
00A0CFE2  48 89 01                        mov qword ptr [rcx], rax
00A0CFE5  49 8B 01                        mov rax, qword ptr [r9]
00A0CFE8  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00A0CFED  EB 05                           jmp 0x140a0cff4
00A0CFEF  E9 E8 02 00 00                  jmp 0x140a0d2dc
00A0CFF4  49 8B 8E B8 00 00 00            mov rcx, qword ptr [r14 + 0xb8]
00A0CFFB  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00A0D000  48 85 D2                        test rdx, rdx
00A0D003  0F 84 41 05 00 00               je 0x140a0d54a
00A0D009  E8 02 06 00 00                  call 0x140a0d610
00A0D00E  85 C0                           test eax, eax
00A0D010  0F 88 C6 02 00 00               js 0x140a0d2dc
00A0D016  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A0D01B  39 78 28                        cmp dword ptr [rax + 0x28], edi
00A0D01E  0F 84 42 04 00 00               je 0x140a0d466
00A0D024  33 D2                           xor edx, edx
00A0D026  40 38 78 4C                     cmp byte ptr [rax + 0x4c], dil
00A0D02A  0F 85 CF 02 00 00               jne 0x140a0d2ff
00A0D030  49 8B CE                        mov rcx, r14
00A0D033  E8 78 B4 A3 FF                  call 0x1404484b0
00A0D038  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00A0D03D  66 45 29 AE E6 01 00 00         sub word ptr [r14 + 0x1e6], r13w
00A0D045  90                              nop
00A0D046  41 8B 4E 74                     mov ecx, dword ptr [r14 + 0x74]
00A0D04A  C1 E9 14                        shr ecx, 0x14
00A0D04D  41 22 CD                        and cl, r13b
00A0D050  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00A0D058  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00A0D05D  48 8D 94 24 98 00 00 00         lea rdx, [rsp + 0x98]
00A0D065  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00A0D06A  88 4C 24 20                     mov byte ptr [rsp + 0x20], cl
00A0D06E  4C 8B 0D 83 A4 5B 00            mov r9, qword ptr [rip + 0x5ba483]
00A0D075  4C 8B 05 6C A4 5B 00            mov r8, qword ptr [rip + 0x5ba46c]
00A0D07C  48 8B D3                        mov rdx, rbx
00A0D07F  48 8B C8                        mov rcx, rax
00A0D082  E8 D1 F9 A5 FF                  call 0x14046ca58
00A0D087  44 8B F8                        mov r15d, eax
00A0D08A  90                              nop
00A0D08B  66 45 01 AE E6 01 00 00         add word ptr [r14 + 0x1e6], r13w
00A0D093  75 12                           jne 0x140a0d0a7
00A0D095  90                              nop
00A0D096  49 8D 8E 98 00 00 00            lea rcx, [r14 + 0x98]
00A0D09D  48 39 09                        cmp qword ptr [rcx], rcx
00A0D0A0  74 05                           je 0x140a0d0a7
00A0D0A2  E8 D9 5B 8D FF                  call 0x1402e2c80
00A0D0A7  45 85 FF                        test r15d, r15d
00A0D0AA  0F 88 1F 02 00 00               js 0x140a0d2cf
00A0D0B0  66 45 29 AE E4 01 00 00         sub word ptr [r14 + 0x1e4], r13w
00A0D0B8  90                              nop
00A0D0B9  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
00A0D0BE  49 83 C4 70                     add r12, 0x70
00A0D0C2  45 33 C0                        xor r8d, r8d
00A0D0C5  33 D2                           xor edx, edx
00A0D0C7  49 8B CC                        mov rcx, r12
00A0D0CA  E8 61 31 80 FF                  call 0x140210230
00A0D0CF  48 8B D8                        mov rbx, rax
00A0D0D2  F0 49 0F BA 2C 24 00            lock bts qword ptr [r12], 0
00A0D0D9  73 0E                           jae 0x140a0d0e9
00A0D0DB  4D 8B C4                        mov r8, r12
00A0D0DE  48 8B D0                        mov rdx, rax
00A0D0E1  49 8B CC                        mov rcx, r12
00A0D0E4  E8 A7 2B 80 FF                  call 0x14020fc90
00A0D0E9  48 85 DB                        test rbx, rbx
00A0D0EC  74 04                           je 0x140a0d0f2
00A0D0EE  44 88 6B 0A                     mov byte ptr [rbx + 0xa], r13b
00A0D0F2  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A0D0F7  48 8B 70 68                     mov rsi, qword ptr [rax + 0x68]
00A0D0FB  EB 16                           jmp 0x140a0d113
00A0D0FD  48 8B D6                        mov rdx, rsi
00A0D100  49 8B CE                        mov rcx, r14
00A0D103  E8 E8 04 00 00                  call 0x140a0d5f0
00A0D108  85 C0                           test eax, eax
00A0D10A  0F 89 E0 01 00 00               jns 0x140a0d2f0
00A0D110  48 8B 36                        mov rsi, qword ptr [rsi]
00A0D113  48 85 F6                        test rsi, rsi
00A0D116  75 E5                           jne 0x140a0d0fd
00A0D118  48 85 F6                        test rsi, rsi
00A0D11B  0F 84 50 03 00 00               je 0x140a0d471
00A0D121  48 83 CB FF                     or rbx, 0xffffffffffffffff
00A0D125  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
00A0D12D  48 8B C3                        mov rax, rbx
00A0D130  F0 49 0F C1 04 24               lock xadd qword ptr [r12], rax
00A0D136  24 06                           and al, 6
00A0D138  3C 02                           cmp al, 2
00A0D13A  0F 84 BE 03 00 00               je 0x140a0d4fe
00A0D140  49 8B CC                        mov rcx, r12
00A0D143  E8 B8 44 8D FF                  call 0x1402e1600
00A0D148  49 8B CE                        mov rcx, r14
00A0D14B  E8 C0 1E 85 FF                  call 0x14025f010
00A0D150  83 7E 24 FF                     cmp dword ptr [rsi + 0x24], -1
00A0D154  0F 84 2D 04 00 00               je 0x140a0d587
00A0D15A  4C 8B A4 24 F8 00 00 00         mov r12, qword ptr [rsp + 0xf8]
00A0D162  66 41 01 9E E6 01 00 00         add word ptr [r14 + 0x1e6], bx
00A0D16A  90                              nop
00A0D16B  41 0F BA AE A4 05 00 00 09      bts dword ptr [r14 + 0x5a4], 9
00A0D174  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
00A0D177  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00A0D17B  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00A0D180  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A0D185  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
00A0D18D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A0D192  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00A0D19A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0D19F  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
00A0D1A7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A0D1AC  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00A0D1B1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0D1B6  44 8B 8C 24 00 01 00 00         mov r9d, dword ptr [rsp + 0x100]
00A0D1BE  4C 8D 84 24 F0 00 00 00         lea r8, [rsp + 0xf0]
00A0D1C6  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00A0D1CB  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A0D1D0  E8 63 06 00 00                  call 0x140a0d838
00A0D1D5  44 8B F8                        mov r15d, eax
00A0D1D8  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
00A0D1DF  41 0F BA B6 A4 05 00 00 09      btr dword ptr [r14 + 0x5a4], 9
00A0D1E8  90                              nop
00A0D1E9  66 45 01 AE E6 01 00 00         add word ptr [r14 + 0x1e6], r13w
00A0D1F1  75 12                           jne 0x140a0d205
00A0D1F3  90                              nop
00A0D1F4  49 8D 86 98 00 00 00            lea rax, [r14 + 0x98]
00A0D1FB  48 39 00                        cmp qword ptr [rax], rax
00A0D1FE  74 05                           je 0x140a0d205
00A0D200  E8 7B 5A 8D FF                  call 0x1402e2c80
00A0D205  40 38 7C 24 50                  cmp byte ptr [rsp + 0x50], dil
00A0D20A  0F 85 8D 03 00 00               jne 0x140a0d59d
00A0D210  45 85 FF                        test r15d, r15d
00A0D213  0F 88 1F 02 00 00               js 0x140a0d438
00A0D219  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00A0D221  48 85 C9                        test rcx, rcx
00A0D224  0F 84 87 03 00 00               je 0x140a0d5b1
00A0D22A  66 41 01 9E E6 01 00 00         add word ptr [r14 + 0x1e6], bx
00A0D232  90                              nop
00A0D233  41 8B 46 74                     mov eax, dword ptr [r14 + 0x74]
00A0D237  C1 E8 14                        shr eax, 0x14
00A0D23A  41 22 C5                        and al, r13b
00A0D23D  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00A0D241  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00A0D246  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A0D24B  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
00A0D253  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A0D258  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00A0D260  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A0D265  8B 84 24 00 01 00 00            mov eax, dword ptr [rsp + 0x100]
00A0D26C  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00A0D270  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A0D275  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
00A0D27A  4D 8B 49 08                     mov r9, qword ptr [r9 + 8]
00A0D27E  4C 8B 05 73 A2 5B 00            mov r8, qword ptr [rip + 0x5ba273]
00A0D285  48 8B 15 64 A2 5B 00            mov rdx, qword ptr [rip + 0x5ba264]
00A0D28C  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00A0D291  E8 92 64 AA FF                  call 0x1404b3728
00A0D296  44 8B F8                        mov r15d, eax
00A0D299  90                              nop
00A0D29A  66 45 01 AE E6 01 00 00         add word ptr [r14 + 0x1e6], r13w
00A0D2A2  75 12                           jne 0x140a0d2b6
00A0D2A4  90                              nop
00A0D2A5  49 8D 86 98 00 00 00            lea rax, [r14 + 0x98]
00A0D2AC  48 39 00                        cmp qword ptr [rax], rax
00A0D2AF  74 05                           je 0x140a0d2b6
00A0D2B1  E8 CA 59 8D FF                  call 0x1402e2c80
00A0D2B6  4D 85 E4                        test r12, r12
00A0D2B9  0F 84 53 95 12 00               je 0x140b36812
00A0D2BF  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
00A0D2C4  41 38 7C 24 4C                  cmp byte ptr [r12 + 0x4c], dil
00A0D2C9  0F 84 DA 00 00 00               je 0x140a0d3a9
00A0D2CF  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A0D2D4  E8 FB 04 00 00                  call 0x140a0d7d4
00A0D2D9  41 8B C7                        mov eax, r15d
00A0D2DC  48 81 C4 B0 00 00 00            add rsp, 0xb0
00A0D2E3  41 5F                           pop r15
00A0D2E5  41 5E                           pop r14
00A0D2E7  41 5D                           pop r13
00A0D2E9  41 5C                           pop r12
00A0D2EB  5F                              pop rdi
00A0D2EC  5E                              pop rsi
00A0D2ED  5B                              pop rbx
00A0D2EE  C3                              ret
00A0D2EF  CC                              int3
00A0D2F0  0F 8E 22 FE FF FF               jle 0x140a0d118
00A0D2F6  48 8B 76 08                     mov rsi, qword ptr [rsi + 8]
00A0D2FA  E9 14 FE FF FF                  jmp 0x140a0d113
00A0D2FF  48 83 CB FF                     or rbx, 0xffffffffffffffff
00A0D303  66 41 01 9E E4 01 00 00         add word ptr [r14 + 0x1e4], bx
00A0D30B  90                              nop
00A0D30C  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00A0D311  49 83 C7 70                     add r15, 0x70
00A0D315  45 33 C0                        xor r8d, r8d
00A0D318  49 8B CF                        mov rcx, r15
00A0D31B  E8 10 2F 80 FF                  call 0x140210230
00A0D320  48 8B F0                        mov rsi, rax
00A0D323  F0 49 0F BA 2F 00               lock bts qword ptr [r15], 0
00A0D329  73 0E                           jae 0x140a0d339
00A0D32B  4D 8B C7                        mov r8, r15
00A0D32E  48 8B D0                        mov rdx, rax
00A0D331  49 8B CF                        mov rcx, r15
00A0D334  E8 57 29 80 FF                  call 0x14020fc90
00A0D339  48 85 F6                        test rsi, rsi
00A0D33C  74 04                           je 0x140a0d342
00A0D33E  44 88 6E 0A                     mov byte ptr [rsi + 0xa], r13b
00A0D342  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A0D347  48 8B 70 68                     mov rsi, qword ptr [rax + 0x68]
00A0D34B  EB 17                           jmp 0x140a0d364
00A0D34D  48 8B D6                        mov rdx, rsi
00A0D350  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00A0D358  E8 93 02 00 00                  call 0x140a0d5f0
00A0D35D  85 C0                           test eax, eax
00A0D35F  79 40                           jns 0x140a0d3a1
00A0D361  48 8B 36                        mov rsi, qword ptr [rsi]
00A0D364  48 85 F6                        test rsi, rsi
00A0D367  75 E4                           jne 0x140a0d34d
00A0D369  48 8B C3                        mov rax, rbx
00A0D36C  F0 49 0F C1 07                  lock xadd qword ptr [r15], rax
00A0D371  24 06                           and al, 6
00A0D373  3C 02                           cmp al, 2
00A0D375  0F 84 90 01 00 00               je 0x140a0d50b
00A0D37B  49 8B CF                        mov rcx, r15
00A0D37E  E8 7D 42 8D FF                  call 0x1402e1600
00A0D383  49 8B CE                        mov rcx, r14
00A0D386  E8 85 1C 85 FF                  call 0x14025f010
00A0D38B  48 85 F6                        test rsi, rsi
00A0D38E  0F 84 FE 01 00 00               je 0x140a0d592
00A0D394  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
00A0D39C  E9 C1 FD FF FF                  jmp 0x140a0d162
00A0D3A1  7E C6                           jle 0x140a0d369
00A0D3A3  48 8B 76 08                     mov rsi, qword ptr [rsi + 8]
00A0D3A7  EB BB                           jmp 0x140a0d364
00A0D3A9  39 7E 24                        cmp dword ptr [rsi + 0x24], edi
00A0D3AC  0F 85 1D FF FF FF               jne 0x140a0d2cf
00A0D3B2  66 41 01 9E E4 01 00 00         add word ptr [r14 + 0x1e4], bx
00A0D3BA  90                              nop
00A0D3BB  49 83 C4 70                     add r12, 0x70
00A0D3BF  45 33 C0                        xor r8d, r8d
00A0D3C2  33 D2                           xor edx, edx
00A0D3C4  49 8B CC                        mov rcx, r12
00A0D3C7  E8 64 2E 80 FF                  call 0x140210230
00A0D3CC  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00A0D3D1  F0 49 0F BA 2C 24 00            lock bts qword ptr [r12], 0
00A0D3D8  73 13                           jae 0x140a0d3ed
00A0D3DA  4D 8B C4                        mov r8, r12
00A0D3DD  48 8B D0                        mov rdx, rax
00A0D3E0  49 8B CC                        mov rcx, r12
00A0D3E3  E8 A8 28 80 FF                  call 0x14020fc90
00A0D3E8  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A0D3ED  48 85 C0                        test rax, rax
00A0D3F0  74 04                           je 0x140a0d3f6
00A0D3F2  44 88 68 0A                     mov byte ptr [rax + 0xa], r13b
00A0D3F6  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A0D3FB  48 8B 81 80 00 00 00            mov rax, qword ptr [rcx + 0x80]
00A0D402  48 89 06                        mov qword ptr [rsi], rax
00A0D405  48 89 B1 80 00 00 00            mov qword ptr [rcx + 0x80], rsi
00A0D40C  E8 43 06 00 00                  call 0x140a0da54
00A0D411  F0 49 0F C1 1C 24               lock xadd qword ptr [r12], rbx
00A0D417  80 E3 06                        and bl, 6
00A0D41A  80 FB 02                        cmp bl, 2
00A0D41D  0F 84 F5 00 00 00               je 0x140a0d518
00A0D423  49 8B CC                        mov rcx, r12
00A0D426  E8 D5 41 8D FF                  call 0x1402e1600
00A0D42B  49 8B CE                        mov rcx, r14
00A0D42E  E8 DD 1B 85 FF                  call 0x14025f010
00A0D433  E9 97 FE FF FF                  jmp 0x140a0d2cf
00A0D438  4D 85 E4                        test r12, r12
00A0D43B  0F 84 7E FE FF FF               je 0x140a0d2bf
00A0D441  45 85 FF                        test r15d, r15d
00A0D444  0F 89 CF FD FF FF               jns 0x140a0d219
00A0D44A  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
00A0D452  4D 85 E4                        test r12, r12
00A0D455  48 0F 45 C7                     cmovne rax, rdi
00A0D459  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00A0D461  E9 B3 FD FF FF                  jmp 0x140a0d219
00A0D466  41 BF 08 00 00 C0               mov r15d, 0xc0000008
00A0D46C  E9 5E FE FF FF                  jmp 0x140a0d2cf
00A0D471  48 8B CF                        mov rcx, rdi
00A0D474  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
00A0D47C  48 39 BC 24 F8 00 00 00         cmp qword ptr [rsp + 0xf8], rdi
00A0D484  0F 85 D2 00 00 00               jne 0x140a0d55c
00A0D48A  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00A0D48F  41 8B 40 48                     mov eax, dword ptr [r8 + 0x48]
00A0D493  85 C0                           test eax, eax
00A0D495  0F 85 75 92 12 00               jne 0x140b36710
00A0D49B  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
00A0D4A3  49 8B C8                        mov rcx, r8
00A0D4A6  E8 61 E3 0C 00                  call 0x140adb80c
00A0D4AB  44 8B F8                        mov r15d, eax
00A0D4AE  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00A0D4B6  45 85 FF                        test r15d, r15d
00A0D4B9  0F 88 A3 00 00 00               js 0x140a0d562
00A0D4BF  48 85 C9                        test rcx, rcx
00A0D4C2  0F 85 9A 00 00 00               jne 0x140a0d562
00A0D4C8  48 83 CB FF                     or rbx, 0xffffffffffffffff
00A0D4CC  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A0D4D1  48 8B B1 80 00 00 00            mov rsi, qword ptr [rcx + 0x80]
00A0D4D8  48 8B 06                        mov rax, qword ptr [rsi]
00A0D4DB  48 89 81 80 00 00 00            mov qword ptr [rcx + 0x80], rax
00A0D4E2  4C 89 76 18                     mov qword ptr [rsi + 0x18], r14
00A0D4E6  48 89 7E 20                     mov qword ptr [rsi + 0x20], rdi
00A0D4EA  E9 36 FC FF FF                  jmp 0x140a0d125
00A0D4EF  48 85 D2                        test rdx, rdx
00A0D4F2  74 3B                           je 0x140a0d52f
00A0D4F4  B8 F0 00 00 C0                  mov eax, 0xc00000f0
00A0D4F9  E9 DE FD FF FF                  jmp 0x140a0d2dc
00A0D4FE  49 8B CC                        mov rcx, r12
00A0D501  E8 CA 88 85 FF                  call 0x140265dd0
00A0D506  E9 35 FC FF FF                  jmp 0x140a0d140
00A0D50B  49 8B CF                        mov rcx, r15
00A0D50E  E8 BD 88 85 FF                  call 0x140265dd0
00A0D513  E9 63 FE FF FF                  jmp 0x140a0d37b
00A0D518  49 8B CC                        mov rcx, r12
00A0D51B  E8 B0 88 85 FF                  call 0x140265dd0
00A0D520  E9 FE FE FF FF                  jmp 0x140a0d423
00A0D525  B8 EF 00 00 C0                  mov eax, 0xc00000ef
00A0D52A  E9 AD FD FF FF                  jmp 0x140a0d2dc
00A0D52F  F7 84 24 00 01 00 00 FE FF FF FF  test dword ptr [rsp + 0x100], 0xfffffffe
00A0D53A  0F 84 8E FA FF FF               je 0x140a0cfce
00A0D540  B8 F1 00 00 C0                  mov eax, 0xc00000f1
00A0D545  E9 92 FD FF FF                  jmp 0x140a0d2dc
00A0D54A  48 8B 94 24 F0 00 00 00         mov rdx, qword ptr [rsp + 0xf0]
00A0D552  E8 5D 2B 05 00                  call 0x140a600b4
00A0D557  E9 B2 FA FF FF                  jmp 0x140a0d00e
00A0D55C  41 BF F0 00 00 C0               mov r15d, 0xc00000f0
00A0D562  48 83 CB FF                     or rbx, 0xffffffffffffffff
00A0D566  48 8B C3                        mov rax, rbx
00A0D569  F0 49 0F C1 04 24               lock xadd qword ptr [r12], rax
00A0D56F  24 06                           and al, 6
00A0D571  3C 02                           cmp al, 2
00A0D573  0F 85 A5 91 12 00               jne 0x140b3671e
00A0D579  49 8B CC                        mov rcx, r12
00A0D57C  E8 4F 88 85 FF                  call 0x140265dd0
00A0D581  90                              nop
00A0D582  E9 97 91 12 00                  jmp 0x140b3671e
00A0D587  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
00A0D58D  E9 3D FD FF FF                  jmp 0x140a0d2cf
00A0D592  41 BF 18 00 00 C0               mov r15d, 0xc0000018
00A0D598  E9 32 FD FF FF                  jmp 0x140a0d2cf
00A0D59D  8B 94 24 00 01 00 00            mov edx, dword ptr [rsp + 0x100]
00A0D5A4  48 8B CB                        mov rcx, rbx
00A0D5A7  E8 A4 00 CA FF                  call 0x1406ad650
00A0D5AC  E9 5F FC FF FF                  jmp 0x140a0d210
00A0D5B1  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00A0D5B6  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
00A0D5BE  48 89 01                        mov qword ptr [rcx], rax
00A0D5C1  E9 37 93 12 00                  jmp 0x140b368fd
00A0D5C6  33 FF                           xor edi, edi
00A0D5C8  44 8D 6F 01                     lea r13d, [rdi + 1]
00A0D5CC  48 83 CB FF                     or rbx, 0xffffffffffffffff
00A0D5D0  48 8B B4 24 A0 00 00 00         mov rsi, qword ptr [rsp + 0xa0]
00A0D5D8  44 8B BC 24 80 00 00 00         mov r15d, dword ptr [rsp + 0x80]
00A0D5E0  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
00A0D5E5  E9 13 93 12 00                  jmp 0x140b368fd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsCallEnclave(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int8 v_stack_m98;
    unsigned __int8 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int8 v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p100;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pF0;
    unsigned __int64 v_stack_pF8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (176);
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    v_stack_m90 = 0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 80) = 0;
    v_stack_m98 = 0;
    *(unsigned __int64 *)(v_rsp - 64) = 0;
    v_stack_m78 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m88 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != ((unsigned __int8)(v_rdi + 1))) goto loc_00A0D525;
    if ((*(unsigned __int64 *)(v_rsp + 8)) != 0) goto loc_00A0D4EF;
    if (a2 == 0) goto loc_00A0D52F;
loc_00A0CFCE:
    if (a4 < a1) { a1 = a4; }
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1);
    v_stack_m70 = *(unsigned __int64 *)(a4);
    goto loc_00A0CFF4;
loc_00A0CFF4:
    if (a2 == 0) goto loc_00A0D54A;
    result = PspSelectVsmEnclaveByNumber(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, v_stack_m90, a4);
loc_00A0D00E:
    if (sign_flag) goto loc_00A0D2DC;
    if ((*(unsigned int *)(v_stack_m90 + 40)) == 0) goto loc_00A0D466;
    a2 = 0;
    if ((*(unsigned __int8 *)(v_stack_m90 + 76)) != 0) goto loc_00A0D2FF;
    result = PsGetBaseTrapFrame(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_m90, a4);
    v_stack_m88 = result;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116))) >> (20));
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(v_rdi + 1)));
    v_stack_mB8 = v_stack_m58;
    v_stack_mC0 = v_stack_m50;
    v_stack_mC8 = (unsigned __int8)(a1);
    result = RtlPrepareEnclaveCall(result, a4, *(unsigned __int64 *)(v_rip + 6005868), *(unsigned __int64 *)(v_rip + 6005891));
    if (condition_is_not_equal) goto loc_00A0D0A7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152, a4, *(unsigned __int64 *)(v_rip + 6005868), *(unsigned __int64 *)(v_rip + 6005891));
    }
    if (sign_flag) goto loc_00A0D2CF;
    v_r12 = (v_stack_m90) + (112);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_r12, a2, a3, *(unsigned __int64 *)(v_rip + 6005891));
    if (!(condition_is_above_or_equal)) {
        a3 = v_r12;
        a2 = result;
        a1 = v_r12;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int64 *)(v_rip + 6005891));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_rdi + 1);
    }
    goto loc_00A0D113;
loc_00A0D0FD:
    result = PspFindVsmEnclaveThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(v_stack_m90 + 104), a3, *(unsigned __int64 *)(v_rip + 6005891));
    if (!sign_flag) goto loc_00A0D2F0;
loc_00A0D113:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + 104)) != 0) goto loc_00A0D0FD;
loc_00A0D118:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + 104)) == 0) goto loc_00A0D471;
    v_rbx = (result) | (-1);
loc_00A0D125:
    v_stack_m48 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + 104));
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00A0D4FE;
loc_00A0D140:
    result = KeAbPostRelease(v_r12, *(unsigned __int64 *)(v_stack_m90 + 104), a3, *(unsigned __int64 *)(v_rip + 6005891));
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(v_stack_m90 + 104), a3, *(unsigned __int64 *)(v_rip + 6005891));
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + 104)) + 36)) == -1) goto loc_00A0D587;
loc_00A0D162:
    v_stack_m80 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + 104)) + 32)));
    v_stack_mA8 = v_stack_m98;
    v_stack_mB0 = v_stack_p18;
    v_stack_mB8 = v_stack_m58;
    v_stack_mC0 = v_stack_m50;
    v_stack_mC8 = v_stack_m70;
    result = VslCallEnclave(v_stack_m90, v_stack_m80, v_stack_p8, (unsigned int)(v_stack_p18));
    v_stack_m68 = (unsigned int)(result);
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m90 + 104)) + 36)) != -1) goto loc_00A0D205;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_m90, v_stack_m80, v_stack_p8, (unsigned int)(v_stack_p18));
    }
    if (v_stack_m98 != 0) goto loc_00A0D59D;
loc_00A0D210:
    if (sign_flag) goto loc_00A0D438;
loc_00A0D219:
    if (v_stack_p8 == 0) goto loc_00A0D5B1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116))) >> (20));
    result = (unsigned __int8)((result) & ((unsigned __int8)(v_rdi + 1)));
    v_stack_mA0 = (unsigned __int8)(result);
    v_stack_mA8 = v_stack_m70;
    v_stack_mB0 = v_stack_m58;
    v_stack_mB8 = v_stack_m50;
    v_stack_mC0 = (unsigned int)((unsigned int)(v_stack_p18));
    v_stack_mC8 = v_stack_p8;
    result = RtlCreateEnclaveReturnFrame(v_stack_m88, *(unsigned __int64 *)(v_rip + 6005348), *(unsigned __int64 *)(v_rip + 6005363), *(unsigned __int64 *)(v_stack_m90 + 8));
    if (condition_is_not_equal) goto loc_00A0D2B6;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_m88, *(unsigned __int64 *)(v_rip + 6005348), *(unsigned __int64 *)(v_rip + 6005363), *(unsigned __int64 *)(v_stack_m90 + 8));
    }
loc_00A0D2BF:
    if ((*(unsigned __int8 *)(v_stack_m90 + 76)) == 0) goto loc_00A0D3A9;
loc_00A0D2CF:
    result = PsDereferenceVsmEnclave(v_stack_m90, *(unsigned __int64 *)(v_rip + 6005348), *(unsigned __int64 *)(v_rip + 6005363), *(unsigned __int64 *)(v_stack_m90 + 8));
loc_00A0D2DC:
    v_rsp = (v_rsp) + (176);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00A0D2F0:
    if (condition_is_less_or_equal) goto loc_00A0D118;
    goto loc_00A0D113;
loc_00A0D2FF:
    v_rbx = (v_rbx) | (-1);
    v_r15 = (v_stack_p58) + (112);
    a3 = 0;
    result = KeAbPreAcquire(v_r15, *(unsigned __int64 *)(v_rip + 6005348), a3, *(unsigned __int64 *)(v_stack_m90 + 8));
    if (!(condition_is_above_or_equal)) {
        a3 = v_r15;
        a2 = result;
        a1 = v_r15;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int64 *)(v_stack_m90 + 8));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_rdi + 1);
    }
    goto loc_00A0D364;
loc_00A0D34D:
    result = PspFindVsmEnclaveThread(v_stack_pF0, *(unsigned __int64 *)(v_stack_p58 + 104), a3, *(unsigned __int64 *)(v_stack_m90 + 8));
    if (!sign_flag) goto loc_00A0D3A1;
loc_00A0D364:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 104)) != 0) goto loc_00A0D34D;
loc_00A0D369:
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_00A0D50B;
loc_00A0D37B:
    result = KeAbPostRelease(v_r15, *(unsigned __int64 *)(v_stack_p58 + 104), a3, *(unsigned __int64 *)(v_stack_m90 + 8));
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(v_stack_p58 + 104), a3, *(unsigned __int64 *)(v_stack_m90 + 8));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 104)) == 0) goto loc_00A0D592;
    v_stack_pA0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 104));
    goto loc_00A0D162;
loc_00A0D3A1:
    if (condition_is_less_or_equal) goto loc_00A0D369;
    goto loc_00A0D364;
loc_00A0D3A9:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 104)) + 8) + 36)) != 0) goto loc_00A0D2CF;
    v_r12 = (v_stack_m90) + (112);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_r12, a2, a3, *(unsigned __int64 *)(v_stack_m90 + 8));
    v_stack_p70 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = v_r12;
        a2 = result;
        a1 = v_r12;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int64 *)(v_stack_m90 + 8));
        result = v_stack_p70;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_rdi + 1);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 104)) + 8)) = *(unsigned __int64 *)(v_stack_p58 + 128);
    *(unsigned __int64 *)(v_stack_p58 + 128) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 104)) + 8);
    result = PspReleaseEnclaveThread(v_stack_p58, a2, a3, *(unsigned __int64 *)(v_stack_m90 + 8));
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_00A0D518;
loc_00A0D423:
    result = KeAbPostRelease(v_r12, a2, a3, *(unsigned __int64 *)(v_stack_m90 + 8));
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, *(unsigned __int64 *)(v_stack_m90 + 8));
    goto loc_00A0D2CF;
loc_00A0D438:
    if (v_r12 == 0) goto loc_00A0D2BF;
    if (!sign_flag) goto loc_00A0D219;
    result = v_stack_pF0;
    if (v_r12 != 0) { result = 0; }
    v_stack_pF0 = result;
    goto loc_00A0D219;
loc_00A0D466:
    goto loc_00A0D2CF;
loc_00A0D471:
    v_stack_p88 = 0;
    if (v_stack_pF8 != 0) goto loc_00A0D55C;
    result = PspPrepareEnclaveThreadWait(v_stack_p58, v_stack_p88, v_stack_p58, *(unsigned __int64 *)(v_stack_m90 + 8));
    if (sign_flag) goto loc_00A0D562;
    if (v_stack_p88 != 0) goto loc_00A0D562;
    v_rbx = (v_rbx) | (-1);
    *(unsigned __int64 *)(v_stack_p58 + 128) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 128));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 128) + 24) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58 + 128) + 32) = 0;
    goto loc_00A0D125;
loc_00A0D4EF:
    if (v_stack_p88 == 0) goto loc_00A0D52F;
    goto loc_00A0D2DC;
loc_00A0D4FE:
    result = ExfTryToWakePushLock(v_r12, v_stack_p88, v_stack_p58, *(unsigned __int64 *)(v_stack_m90 + 8));
    goto loc_00A0D140;
loc_00A0D50B:
    result = ExfTryToWakePushLock((unsigned int)((unsigned int)(result)), v_stack_p88, v_stack_p58, *(unsigned __int64 *)(v_stack_m90 + 8));
    goto loc_00A0D37B;
loc_00A0D518:
    result = ExfTryToWakePushLock(v_r12, v_stack_p88, v_stack_p58, *(unsigned __int64 *)(v_stack_m90 + 8));
    goto loc_00A0D423;
loc_00A0D525:
    goto loc_00A0D2DC;
loc_00A0D52F:
    if (((v_stack_p100) & (0xFFFFFFFEULL)) == 0) goto loc_00A0CFCE;
    goto loc_00A0D2DC;
loc_00A0D54A:
    result = MmSelectVsmEnclaveByAddress(v_r12, v_stack_pF0, v_stack_p58, *(unsigned __int64 *)(v_stack_m90 + 8));
    goto loc_00A0D00E;
loc_00A0D55C:
loc_00A0D562:
    v_rbx = (v_rbx) | (-1);
    result = (unsigned __int8)((v_rbx) & (6));
    result = ExfTryToWakePushLock(v_r12, v_stack_pF0, v_stack_p58, *(unsigned __int64 *)(v_stack_m90 + 8));
loc_00A0D587:
    goto loc_00A0D2CF;
loc_00A0D592:
    goto loc_00A0D2CF;
loc_00A0D59D:
    result = ZwTerminateProcess(v_rbx, (unsigned int)(v_stack_p100), v_stack_p58, *(unsigned __int64 *)(v_stack_m90 + 8));
    goto loc_00A0D210;
loc_00A0D5B1:
    *(unsigned __int64 *)(v_stack_p108) = v_stack_p78;
}
```

## 5. (Beta) C Style

```c
int64_t PsCallEnclave(int64_t Arg1, int64_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint8_t v_stack_m98;
    uint8_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint8_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p100;
    uint64_t v_stack_p108;
    uint64_t v_stack_p18;
    uint64_t v_stack_p58;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint32_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pF0;
    uint64_t v_stack_pF8;

    *(void **)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (176);
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    v_stack_m90 = 0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x50) = 0;
    v_stack_m98 = 0;
    *(uint64_t *)(local_rsp - 0x40) = 0;
    v_stack_m78 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m88 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != ((uint8_t)(local_rdi + 1))) goto loc_00A0D525;
    if ((*(uint64_t *)(local_rsp + 0x8)) != 0) goto loc_00A0D4EF;
    if (Arg2 == 0) goto loc_00A0D52F;
loc_00A0CFCE:
    if (Arg4 < Arg1) { Arg1 = Arg4; }
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg1);
    v_stack_m70 = *(uint64_t *)(arg4);
    goto loc_00A0CFF4;
loc_00A0CFF4:
    if (Arg2 == 0) goto loc_00A0D54A;
    result = PspSelectVsmEnclaveByNumber(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, v_stack_m90, Arg4);
loc_00A0D00E:
    if (sign_flag) goto loc_00A0D2DC;
    if ((*(uint32_t *)(v_stack_m90 + 0x28)) == 0) goto loc_00A0D466;
    Arg2 = 0;
    if ((*(uint8_t *)(v_stack_m90 + 0x4C)) != 0) goto loc_00A0D2FF;
    result = PsGetBaseTrapFrame(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_m90, Arg4);
    v_stack_m88 = result;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74))) >> (20));
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(local_rdi + 1)));
    v_stack_mB8 = v_stack_m58;
    v_stack_mC0 = v_stack_m50;
    v_stack_mC8 = (uint8_t)(Arg1);
    result = RtlPrepareEnclaveCall(result, Arg4, *(uint64_t *)(v_rip + 0x5BA46C), *(uint64_t *)(v_rip + 0x5BA483));
    if (condition_is_not_equal) goto loc_00A0D0A7;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(uint64_t *)(gs_base + (0 + 0x188)) + 152, Arg4, *(uint64_t *)(v_rip + 0x5BA46C), *(uint64_t *)(v_rip + 0x5BA483));
    }
    if (sign_flag) goto loc_00A0D2CF;
    local_r12 = (v_stack_m90) + (112);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_r12, Arg2, Arg3, *(uint64_t *)(v_rip + 0x5BA483));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_r12;
        Arg2 = result;
        Arg1 = local_r12;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, *(uint64_t *)(v_rip + 0x5BA483));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_rdi + 1);
    }
    goto loc_00A0D113;
loc_00A0D0FD:
    result = PspFindVsmEnclaveThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(v_stack_m90 + 0x68), Arg3, *(uint64_t *)(v_rip + 0x5BA483));
    if (!sign_flag) goto loc_00A0D2F0;
loc_00A0D113:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m90 + 0x68)) != 0) goto loc_00A0D0FD;
loc_00A0D118:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m90 + 0x68)) == 0) goto loc_00A0D471;
    local_rbx = (result) | (-1);
loc_00A0D125:
    v_stack_m48 = *(uint64_t *)(*(uint64_t *)(v_stack_m90 + 0x68));
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00A0D4FE;
loc_00A0D140:
    result = KeAbPostRelease(local_r12, *(uint64_t *)(v_stack_m90 + 0x68), Arg3, *(uint64_t *)(v_rip + 0x5BA483));
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(v_stack_m90 + 0x68), Arg3, *(uint64_t *)(v_rip + 0x5BA483));
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + 0x68)) + 0x24)) == -1) goto loc_00A0D587;
loc_00A0D162:
    v_stack_m80 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + 0x68)) + 0x20)));
    v_stack_mA8 = v_stack_m98;
    v_stack_mB0 = v_stack_p18;
    v_stack_mB8 = v_stack_m58;
    v_stack_mC0 = v_stack_m50;
    v_stack_mC8 = v_stack_m70;
    result = VslCallEnclave(v_stack_m90, v_stack_m80, v_stack_p8, (uint32_t)(v_stack_p18));
    v_stack_m68 = (uint32_t)(result);
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m90 + 0x68)) + 0x24)) != -1) goto loc_00A0D205;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_m90, v_stack_m80, v_stack_p8, (uint32_t)(v_stack_p18));
    }
    if (v_stack_m98 != 0) goto loc_00A0D59D;
loc_00A0D210:
    if (sign_flag) goto loc_00A0D438;
loc_00A0D219:
    if (v_stack_p8 == 0) goto loc_00A0D5B1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74))) >> (20));
    result = (uint8_t)((result) & ((uint8_t)(local_rdi + 1)));
    v_stack_mA0 = (uint8_t)(result);
    v_stack_mA8 = v_stack_m70;
    v_stack_mB0 = v_stack_m58;
    v_stack_mB8 = v_stack_m50;
    v_stack_mC0 = (uint32_t)((uint32_t)(v_stack_p18));
    v_stack_mC8 = v_stack_p8;
    result = RtlCreateEnclaveReturnFrame(v_stack_m88, *(uint64_t *)(v_rip + 0x5BA264), *(uint64_t *)(v_rip + 0x5BA273), *(uint64_t *)(v_stack_m90 + 0x8));
    if (condition_is_not_equal) goto loc_00A0D2B6;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_m88, *(uint64_t *)(v_rip + 0x5BA264), *(uint64_t *)(v_rip + 0x5BA273), *(uint64_t *)(v_stack_m90 + 0x8));
    }
loc_00A0D2BF:
    if ((*(uint8_t *)(v_stack_m90 + 0x4C)) == 0) goto loc_00A0D3A9;
loc_00A0D2CF:
    result = PsDereferenceVsmEnclave(v_stack_m90, *(uint64_t *)(v_rip + 0x5BA264), *(uint64_t *)(v_rip + 0x5BA273), *(uint64_t *)(v_stack_m90 + 0x8));
loc_00A0D2DC:
    local_rsp = (local_rsp) + (176);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00A0D2F0:
    if (condition_is_less_or_equal) goto loc_00A0D118;
    goto loc_00A0D113;
loc_00A0D2FF:
    local_rbx = (local_rbx) | (-1);
    local_r15 = (v_stack_p58) + (112);
    Arg3 = 0;
    result = KeAbPreAcquire(local_r15, *(uint64_t *)(v_rip + 0x5BA264), Arg3, *(uint64_t *)(v_stack_m90 + 0x8));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_r15;
        Arg2 = result;
        Arg1 = local_r15;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, *(uint64_t *)(v_stack_m90 + 0x8));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_rdi + 1);
    }
    goto loc_00A0D364;
loc_00A0D34D:
    result = PspFindVsmEnclaveThread(v_stack_pF0, *(uint64_t *)(v_stack_p58 + 0x68), Arg3, *(uint64_t *)(v_stack_m90 + 0x8));
    if (!sign_flag) goto loc_00A0D3A1;
loc_00A0D364:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x68)) != 0) goto loc_00A0D34D;
loc_00A0D369:
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) goto loc_00A0D50B;
loc_00A0D37B:
    result = KeAbPostRelease(local_r15, *(uint64_t *)(v_stack_p58 + 0x68), Arg3, *(uint64_t *)(v_stack_m90 + 0x8));
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(v_stack_p58 + 0x68), Arg3, *(uint64_t *)(v_stack_m90 + 0x8));
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x68)) == 0) goto loc_00A0D592;
    v_stack_pA0 = *(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x68));
    goto loc_00A0D162;
loc_00A0D3A1:
    if (condition_is_less_or_equal) goto loc_00A0D369;
    goto loc_00A0D364;
loc_00A0D3A9:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x68)) + 0x8) + 0x24)) != 0) goto loc_00A0D2CF;
    local_r12 = (v_stack_m90) + (112);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_r12, Arg2, Arg3, *(uint64_t *)(v_stack_m90 + 0x8));
    v_stack_p70 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_r12;
        Arg2 = result;
        Arg1 = local_r12;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, *(uint64_t *)(v_stack_m90 + 0x8));
        result = v_stack_p70;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_rdi + 1);
    }
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x68)) + 0x8)) = *(uint64_t *)(v_stack_p58 + 0x80);
    *(uint64_t *)(v_stack_p58 + 0x80) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x68)) + 0x8);
    result = PspReleaseEnclaveThread(v_stack_p58, Arg2, Arg3, *(uint64_t *)(v_stack_m90 + 0x8));
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_00A0D518;
loc_00A0D423:
    result = KeAbPostRelease(local_r12, Arg2, Arg3, *(uint64_t *)(v_stack_m90 + 0x8));
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, *(uint64_t *)(v_stack_m90 + 0x8));
    goto loc_00A0D2CF;
loc_00A0D438:
    if (local_r12 == 0) goto loc_00A0D2BF;
    if (!sign_flag) goto loc_00A0D219;
    result = v_stack_pF0;
    if (local_r12 != 0) { result = 0; }
    v_stack_pF0 = result;
    goto loc_00A0D219;
loc_00A0D466:
    goto loc_00A0D2CF;
loc_00A0D471:
    v_stack_p88 = 0;
    if (v_stack_pF8 != 0) goto loc_00A0D55C;
    result = PspPrepareEnclaveThreadWait(v_stack_p58, v_stack_p88, v_stack_p58, *(uint64_t *)(v_stack_m90 + 0x8));
    if (sign_flag) goto loc_00A0D562;
    if (v_stack_p88 != 0) goto loc_00A0D562;
    local_rbx = (local_rbx) | (-1);
    *(uint64_t *)(v_stack_p58 + 0x80) = *(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x80));
    *(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x80) + 0x18) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint64_t *)(*(uint64_t *)(v_stack_p58 + 0x80) + 0x20) = 0;
    goto loc_00A0D125;
loc_00A0D4EF:
    if (v_stack_p88 == 0) goto loc_00A0D52F;
    goto loc_00A0D2DC;
loc_00A0D4FE:
    result = ExfTryToWakePushLock(local_r12, v_stack_p88, v_stack_p58, *(uint64_t *)(v_stack_m90 + 0x8));
    goto loc_00A0D140;
loc_00A0D50B:
    result = ExfTryToWakePushLock((uint32_t)((uint32_t)(result)), v_stack_p88, v_stack_p58, *(uint64_t *)(v_stack_m90 + 0x8));
    goto loc_00A0D37B;
loc_00A0D518:
    result = ExfTryToWakePushLock(local_r12, v_stack_p88, v_stack_p58, *(uint64_t *)(v_stack_m90 + 0x8));
    goto loc_00A0D423;
loc_00A0D525:
    goto loc_00A0D2DC;
loc_00A0D52F:
    if (((v_stack_p100) & (0xFFFFFFFEULL)) == 0) goto loc_00A0CFCE;
    goto loc_00A0D2DC;
loc_00A0D54A:
    result = MmSelectVsmEnclaveByAddress(local_r12, v_stack_pF0, v_stack_p58, *(uint64_t *)(v_stack_m90 + 0x8));
    goto loc_00A0D00E;
loc_00A0D55C:
loc_00A0D562:
    local_rbx = (local_rbx) | (-1);
    result = (uint8_t)((local_rbx) & (6));
    result = ExfTryToWakePushLock(local_r12, v_stack_pF0, v_stack_p58, *(uint64_t *)(v_stack_m90 + 0x8));
loc_00A0D587:
    goto loc_00A0D2CF;
loc_00A0D592:
    goto loc_00A0D2CF;
loc_00A0D59D:
    result = ZwTerminateProcess(local_rbx, (uint32_t)(v_stack_p100), v_stack_p58, *(uint64_t *)(v_stack_m90 + 0x8));
    goto loc_00A0D210;
loc_00A0D5B1:
    *(uint64_t *)(v_stack_p108) = v_stack_p78;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A0CF50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
