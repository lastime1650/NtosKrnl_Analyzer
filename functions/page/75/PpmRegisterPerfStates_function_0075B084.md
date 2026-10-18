# PpmRegisterPerfStates

- RVA: `0x0075B084`–`0x0075BD81` (길이 `3,325` bytes)
- VA: `0x000000014075B084`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC2A4`
- 디코드: `743`개 명령, `3,325/3,325` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **42**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **43**

### Outgoing calls
- `0x0075B0D1` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0075B0E7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0075B130` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0075B14F` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0075B15B` → [KeQueryActiveProcessorAffinity2](../../text/46/KeQueryActiveProcessorAffinity2_function_00469CC0.md) (function, `0x00469CC0`)
- `0x0075B176` → [PpmAcquireLock](../../text/2D/PpmAcquireLock_function_002D9AA4.md) (function, `0x002D9AA4`)
- `0x0075B282` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0075B351` → [PpmAllocatePerfCheck](../76/PpmAllocatePerfCheck_function_00764070.md) (function, `0x00764070`)
- `0x0075B387` → [KeCheckProcessorAffinityEx](../../text/30/KeCheckProcessorAffinityEx_function_00305150.md) (function, `0x00305150`)
- `0x0075B397` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x0075B3AF` → [PpmAllocatePerfCheck](../76/PpmAllocatePerfCheck_function_00764070.md) (function, `0x00764070`)
- `0x0075B3C6` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x0075B3EB` → [PpmConvertTimeFrom](../../text/44/PpmConvertTimeFrom_function_00447510.md) (function, `0x00447510`)
- `0x0075B4B7` → [PopDiagTraceProcessorThrottlePerfTrack](../../text/42/PopDiagTraceProcessorThrottlePerfTrack_function_0042B2B0.md) (function, `0x0042B2B0`)
- `0x0075B56A` → [PpmReleaseLock](../../text/2D/PpmReleaseLock_function_002DA428.md) (function, `0x002DA428`)
- `0x0075B57E` → [KeIsEmptyAffinityEx](../../text/2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x0075B5CB` → [KeFirstGroupAffinityEx](../../text/46/KeFirstGroupAffinityEx_function_00463810.md) (function, `0x00463810`)
- `0x0075B5D5` → [KeFindFirstSetRightGroupAffinity](../../text/2C/KeFindFirstSetRightGroupAffinity_function_002CFB10.md) (function, `0x002CFB10`)
- `0x0075B5DC` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x0075B615` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0075B626` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x0075B69A` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0075B965` → [PpmPerfResizeHistory](../AA/PpmPerfResizeHistory_function_00AAF9C8.md) (function, `0x00AAF9C8`)
- `0x0075B9A5` → [PpmInstallFeedbackCounters](../../text/4D/PpmInstallFeedbackCounters_function_004D477C.md) (function, `0x004D477C`)
- `0x0075BB22` → [KiOrAffinityEx](../../text/39/KiOrAffinityEx_function_0039A84C.md) (function, `0x0039A84C`)
- `0x0075BB31` → [KeIsEqualAffinityEx](../../text/30/KeIsEqualAffinityEx_function_00305230.md) (function, `0x00305230`)
- `0x0075BBEE` → [PpmUpdateProcessorPolicy](../A5/PpmUpdateProcessorPolicy_function_00A53324.md) (function, `0x00A53324`)
- `0x0075BBF6` → [PpmCheckResetProcessors](../../text/5D/PpmCheckResetProcessors_function_005D84D0.md) (function, `0x005D84D0`)
- `0x0075BC01` → [KeCheckProcessorAffinityEx](../../text/30/KeCheckProcessorAffinityEx_function_00305150.md) (function, `0x00305150`)
- `0x0075BC0A` → [PpmParkApplyPolicy](../../text/4B/PpmParkApplyPolicy_function_004B613C.md) (function, `0x004B613C`)
- `0x0075BC0F` → [PpmCheckReInit](../A8/PpmCheckReInit_function_00A84DD8.md) (function, `0x00A84DD8`)
- `0x0075BC23` → [PpmPerfUpdateDomainPolicy](../A9/PpmPerfUpdateDomainPolicy_function_00A97030.md) (function, `0x00A97030`)
- `0x0075BC4F` → [KeIsEqualAffinityEx](../../text/30/KeIsEqualAffinityEx_function_00305230.md) (function, `0x00305230`)
- `0x0075BC5F` → [PpmAcquireLock](../../text/2D/PpmAcquireLock_function_002D9AA4.md) (function, `0x002D9AA4`)
- `0x0075BC70` → [PpmReinitializeHeteroEngine](../A5/PpmReinitializeHeteroEngine_function_00A53108.md) (function, `0x00A53108`)
- `0x0075BCAB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0075BCC9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0075BCEA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0075BCFF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0075BD1F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0075BD48` → [KeSetTimer2](../../text/3A/KeSetTimer2_function_003A08E0.md) (function, `0x003A08E0`)
- `0x0075BD5A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmPerfRegisterNativePerfStates](PpmPerfRegisterNativePerfStates_function_0075ADE0.md) at `0x0075ADE6`
- [PpmPerfRegisterHvPerfStateCounters](../77/PpmPerfRegisterHvPerfStateCounters_function_00770C40.md) at `0x00770D1D`

### Static image references
- `0x0075B0AA` → RVA `0x00E0A740` (`.data`; read)
- `0x0075B16F` → RVA `0x00F0CC00` (`.data`; read)
- `0x0075B2C9` → RVA `0x00FC506C` (`ALMOSTRO`; write)
- `0x0075B380` → RVA `0x00E0B430` (`.data`; read)
- `0x0075B3D4` → RVA `0x00FC5050` (`ALMOSTRO`; read)
- `0x0075B3DD` → RVA `0x00FC506C` (`ALMOSTRO`; read)
- `0x0075B7ED` → RVA `0x00FC50B0` (`ALMOSTRO`; read)
- `0x0075B7FE` → RVA `0x00FC50B0` (`ALMOSTRO`; write)
- `0x0075B824` → RVA `0x00F0B250` (`.data`; read)
- `0x0075B82D` → RVA `0x00F0B250` (`.data`; write)
- `0x0075B83D` → RVA `0x00F0E180` (`.data`; read/write)
- `0x0075B890` → RVA `0x00FC6AF7` (`ALMOSTRO`; write)
- `0x0075B89C` → RVA `0x00FC6AFB` (`ALMOSTRO`; write)
- `0x0075B9C3` → RVA `0x00F0E260` (`.data`; read)
- `0x0075B9D0` → RVA `0x00F0E260` (`.data`; write)
- `0x0075B9D7` → RVA `0x00F0E258` (`.data`; read)
- `0x0075B9EA` → RVA `0x00F0E258` (`.data`; write)
- `0x0075B9F1` → RVA `0x00F0E270` (`.data`; read)
- `0x0075BA01` → RVA `0x00F0E270` (`.data`; write)
- `0x0075BA08` → RVA `0x00F0E268` (`.data`; read)
- `0x0075BA18` → RVA `0x00F0E268` (`.data`; write)
- `0x0075BA1F` → RVA `0x00F0E280` (`.data`; read)
- `0x0075BA2F` → RVA `0x00F0E280` (`.data`; write)
- `0x0075BA36` → RVA `0x00F0E278` (`.data`; read)
- `0x0075BA46` → RVA `0x00F0E278` (`.data`; write)
- `0x0075BA4D` → RVA `0x00F0E290` (`.data`; read)
- `0x0075BA5D` → RVA `0x00F0E290` (`.data`; write)
- `0x0075BA64` → RVA `0x00F0E288` (`.data`; read)
- `0x0075BA74` → RVA `0x00F0E288` (`.data`; write)
- `0x0075BA7B` → RVA `0x00F0E298` (`.data`; read)
- `0x0075BA8B` → RVA `0x00F0E298` (`.data`; write)
- `0x0075BA97` → RVA `0x00F0B258` (`.data`; write)
- `0x0075BA9E` → RVA `0x00FC6CF0` (`ALMOSTRO`; read)
- `0x0075BAA4` → RVA `0x00FC6BA8` (`ALMOSTRO`; read)
- `0x0075BAB4` → RVA `0x00FC6CF0` (`ALMOSTRO`; write)
- `0x0075BABA` → RVA `0x00FC6BB0` (`ALMOSTRO`; read)
- `0x0075BAE1` → RVA `0x00FC6BB0` (`ALMOSTRO`; write)
- `0x0075BB0C` → RVA `0x00E0B432` (`.data`; read)
- `0x0075BB27` → RVA `0x00E0B5A0` (`.data`; read)
- `0x0075BBD5` → RVA `0x00FC6AEC` (`ALMOSTRO`; write)
- `0x0075BBE7` → RVA `0x00F0E180` (`.data`; read)
- `0x0075BC67` → RVA `0x00FC6ADC` (`ALMOSTRO`; write)
- `0x0075BD37` → RVA `0x00F0E1A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **35**
  - `0x0075B0D1` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0075B0E7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0075B130` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0075B14F` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0075B15B` → [KeQueryActiveProcessorAffinity2](../../text/46/KeQueryActiveProcessorAffinity2_function_00469CC0.md) (`PAGE` → `.text`)
  - `0x0075B176` → [PpmAcquireLock](../../text/2D/PpmAcquireLock_function_002D9AA4.md) (`PAGE` → `.text`)
  - `0x0075B282` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0075B387` → [KeCheckProcessorAffinityEx](../../text/30/KeCheckProcessorAffinityEx_function_00305150.md) (`PAGE` → `.text`)
  - `0x0075B397` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (`PAGE` → `.text`)
  - `0x0075B3C6` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGE` → `.text`)
  - `0x0075B3EB` → [PpmConvertTimeFrom](../../text/44/PpmConvertTimeFrom_function_00447510.md) (`PAGE` → `.text`)
  - `0x0075B4B7` → [PopDiagTraceProcessorThrottlePerfTrack](../../text/42/PopDiagTraceProcessorThrottlePerfTrack_function_0042B2B0.md) (`PAGE` → `.text`)
  - `0x0075B56A` → [PpmReleaseLock](../../text/2D/PpmReleaseLock_function_002DA428.md) (`PAGE` → `.text`)
  - `0x0075B57E` → [KeIsEmptyAffinityEx](../../text/2D/KeIsEmptyAffinityEx_function_002D1580.md) (`PAGE` → `.text`)
  - `0x0075B5CB` → [KeFirstGroupAffinityEx](../../text/46/KeFirstGroupAffinityEx_function_00463810.md) (`PAGE` → `.text`)
  - `0x0075B5D5` → [KeFindFirstSetRightGroupAffinity](../../text/2C/KeFindFirstSetRightGroupAffinity_function_002CFB10.md) (`PAGE` → `.text`)
  - `0x0075B5DC` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (`PAGE` → `.text`)
  - `0x0075B615` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0075B626` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (`PAGE` → `.text`)
  - `0x0075B69A` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGE` → `.text`)
  - `0x0075B9A5` → [PpmInstallFeedbackCounters](../../text/4D/PpmInstallFeedbackCounters_function_004D477C.md) (`PAGE` → `.text`)
  - `0x0075BB22` → [KiOrAffinityEx](../../text/39/KiOrAffinityEx_function_0039A84C.md) (`PAGE` → `.text`)
  - `0x0075BB31` → [KeIsEqualAffinityEx](../../text/30/KeIsEqualAffinityEx_function_00305230.md) (`PAGE` → `.text`)
  - `0x0075BBF6` → [PpmCheckResetProcessors](../../text/5D/PpmCheckResetProcessors_function_005D84D0.md) (`PAGE` → `.text`)
  - `0x0075BC01` → [KeCheckProcessorAffinityEx](../../text/30/KeCheckProcessorAffinityEx_function_00305150.md) (`PAGE` → `.text`)
  - `0x0075BC0A` → [PpmParkApplyPolicy](../../text/4B/PpmParkApplyPolicy_function_004B613C.md) (`PAGE` → `.text`)
  - `0x0075BC4F` → [KeIsEqualAffinityEx](../../text/30/KeIsEqualAffinityEx_function_00305230.md) (`PAGE` → `.text`)
  - `0x0075BC5F` → [PpmAcquireLock](../../text/2D/PpmAcquireLock_function_002D9AA4.md) (`PAGE` → `.text`)
  - `0x0075BCAB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0075BCC9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0075BCEA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0075BCFF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0075BD1F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0075BD48` → [KeSetTimer2](../../text/3A/KeSetTimer2_function_003A08E0.md) (`PAGE` → `.text`)
  - `0x0075BD5A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0075B084  48 8B C4                        mov rax, rsp
0075B087  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0075B08B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0075B08F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0075B093  55                              push rbp
0075B094  41 54                           push r12
0075B096  41 55                           push r13
0075B098  41 56                           push r14
0075B09A  41 57                           push r15
0075B09C  48 8D A8 08 FE FF FF            lea rbp, [rax - 0x1f8]
0075B0A3  48 81 EC D0 02 00 00            sub rsp, 0x2d0
0075B0AA  48 8B 05 8F F6 6A 00            mov rax, qword ptr [rip + 0x6af68f]
0075B0B1  48 33 C4                        xor rax, rsp
0075B0B4  48 89 85 C0 01 00 00            mov qword ptr [rbp + 0x1c0], rax
0075B0BB  8A DA                           mov bl, dl
0075B0BD  48 8B F1                        mov rsi, rcx
0075B0C0  BF 00 01 00 00                  mov edi, 0x100
0075B0C5  48 8D 8D B8 00 00 00            lea rcx, [rbp + 0xb8]
0075B0CC  44 8B C7                        mov r8d, edi
0075B0CF  33 D2                           xor edx, edx
0075B0D1  E8 6A BB F6 FF                  call 0x1406c6c40
0075B0D6  0F 57 C0                        xorps xmm0, xmm0
0075B0D9  48 8D 4D A8                     lea rcx, [rbp - 0x58]
0075B0DD  44 8B C7                        mov r8d, edi
0075B0E0  33 D2                           xor edx, edx
0075B0E2  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
0075B0E7  E8 54 BB F6 FF                  call 0x1406c6c40
0075B0EC  44 8B 6E 10                     mov r13d, dword ptr [rsi + 0x10]
0075B0F0  48 8D 4D A8                     lea rcx, [rbp - 0x58]
0075B0F4  44 8B 66 14                     mov r12d, dword ptr [rsi + 0x14]
0075B0F8  0F 57 C0                        xorps xmm0, xmm0
0075B0FB  44 8B 76 24                     mov r14d, dword ptr [rsi + 0x24]
0075B0FF  0F 57 C9                        xorps xmm1, xmm1
0075B102  45 33 FF                        xor r15d, r15d
0075B105  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
0075B10A  33 D2                           xor edx, edx
0075B10C  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
0075B111  41 B8 00 01 00 00               mov r8d, 0x100
0075B117  44 89 64 24 3C                  mov dword ptr [rsp + 0x3c], r12d
0075B11C  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
0075B121  41 8B FF                        mov edi, r15d
0075B124  48 C7 45 A0 01 00 20 00         mov qword ptr [rbp - 0x60], 0x200001
0075B12C  0F 11 4D 88                     movups xmmword ptr [rbp - 0x78], xmm1
0075B130  E8 0B BB F6 FF                  call 0x1406c6c40
0075B135  33 D2                           xor edx, edx
0075B137  48 C7 85 B0 00 00 00 01 00 20 00  mov qword ptr [rbp + 0xb0], 0x200001
0075B142  41 B8 00 01 00 00               mov r8d, 0x100
0075B148  48 8D 8D B8 00 00 00            lea rcx, [rbp + 0xb8]
0075B14F  E8 EC BA F6 FF                  call 0x1406c6c40
0075B154  48 8D 8D B0 00 00 00            lea rcx, [rbp + 0xb0]
0075B15B  E8 60 EB D0 FF                  call 0x140469cc0
0075B160  44 89 7C 24 2C                  mov dword ptr [rsp + 0x2c], r15d
0075B165  45 8B E7                        mov r12d, r15d
0075B168  45 8B CF                        mov r9d, r15d
0075B16B  84 DB                           test bl, bl
0075B16D  75 0F                           jne 0x14075b17e
0075B16F  48 8D 0D 8A 1A 7B 00            lea rcx, [rip + 0x7b1a8a]
0075B176  E8 29 E9 B7 FF                  call 0x1402d9aa4
0075B17B  45 8B CF                        mov r9d, r15d
0075B17E  48 83 4C 24 30 FF               or qword ptr [rsp + 0x30], 0xffffffffffffffff
0075B184  33 DB                           xor ebx, ebx
0075B186  8B D3                           mov edx, ebx
0075B188  41 83 CF FF                     or r15d, 0xffffffff
0075B18C  44 8D 5B 01                     lea r11d, [rbx + 1]
0075B190  41 3B D6                        cmp edx, r14d
0075B193  73 34                           jae 0x14075b1c9
0075B195  8B C2                           mov eax, edx
0075B197  48 8D 0C 40                     lea rcx, [rax + rax*2]
0075B19B  48 8B 86 30 02 00 00            mov rax, qword ptr [rsi + 0x230]
0075B1A2  44 8B 44 C8 0C                  mov r8d, dword ptr [rax + rcx*8 + 0xc]
0075B1A7  41 83 F8 02                     cmp r8d, 2
0075B1AB  73 11                           jae 0x14075b1be
0075B1AD  46 39 7C 84 30                  cmp dword ptr [rsp + r8*4 + 0x30], r15d
0075B1B2  75 05                           jne 0x14075b1b9
0075B1B4  42 89 54 84 30                  mov dword ptr [rsp + r8*4 + 0x30], edx
0075B1B9  41 03 D3                        add edx, r11d
0075B1BC  EB D2                           jmp 0x14075b190
0075B1BE  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
0075B1C4  E9 9A 03 00 00                  jmp 0x14075b563
0075B1C9  44 39 7C 24 30                  cmp dword ptr [rsp + 0x30], r15d
0075B1CE  75 07                           jne 0x14075b1d7
0075B1D0  44 39 7C 24 34                  cmp dword ptr [rsp + 0x34], r15d
0075B1D5  74 E7                           je 0x14075b1be
0075B1D7  44 8B D3                        mov r10d, ebx
0075B1DA  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
0075B1DF  41 B8 02 00 00 00               mov r8d, 2
0075B1E5  44 39 3A                        cmp dword ptr [rdx], r15d
0075B1E8  41 8D 4A 01                     lea ecx, [r10 + 1]
0075B1EC  48 8D 52 04                     lea rdx, [rdx + 4]
0075B1F0  41 0F 44 CA                     cmove ecx, r10d
0075B1F4  44 8B D1                        mov r10d, ecx
0075B1F7  4D 2B C3                        sub r8, r11
0075B1FA  75 E9                           jne 0x14075b1e5
0075B1FC  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
0075B200  45 85 ED                        test r13d, r13d
0075B203  74 33                           je 0x14075b238
0075B205  48 8B 96 38 02 00 00            mov rdx, qword ptr [rsi + 0x238]
0075B20C  4D 8B C5                        mov r8, r13
0075B20F  48 83 C2 1C                     add rdx, 0x1c
0075B213  41 BA 20 00 00 00               mov r10d, 0x20
0075B219  44 39 1A                        cmp dword ptr [rdx], r11d
0075B21C  41 8D 49 01                     lea ecx, [r9 + 1]
0075B220  41 0F 45 C9                     cmovne ecx, r9d
0075B224  49 03 D2                        add rdx, r10
0075B227  44 8B C9                        mov r9d, ecx
0075B22A  4D 2B C3                        sub r8, r11
0075B22D  75 EA                           jne 0x14075b219
0075B22F  44 8B 54 24 28                  mov r10d, dword ptr [rsp + 0x28]
0075B234  89 4C 24 2C                     mov dword ptr [rsp + 0x2c], ecx
0075B238  41 69 DD A8 04 00 00            imul ebx, r13d, 0x4a8
0075B23F  41 8B C5                        mov eax, r13d
0075B242  41 0F AF C2                     imul eax, r10d
0075B246  33 C9                           xor ecx, ecx
0075B248  81 C3 C7 04 00 00               add ebx, 0x4c7
0075B24E  83 E3 F8                        and ebx, 0xfffffff8
0075B251  44 8D 3C 40                     lea r15d, [rax + rax*2]
0075B255  41 C1 E7 04                     shl r15d, 4
0075B259  44 03 FB                        add r15d, ebx
0075B25C  41 8B C7                        mov eax, r15d
0075B25F  45 85 C9                        test r9d, r9d
0075B262  74 0D                           je 0x14075b271
0075B264  41 69 C1 10 03 00 00            imul eax, r9d, 0x310
0075B26B  41 03 C7                        add eax, r15d
0075B26E  45 85 C9                        test r9d, r9d
0075B271  44 0F 44 F9                     cmove r15d, ecx
0075B275  8B D0                           mov edx, eax
0075B277  B9 40 00 00 00                  mov ecx, 0x40
0075B27C  41 B8 50 50 4D 70               mov r8d, 0x704d5050
0075B282  E8 69 6E 42 00                  call 0x140b820f0
0075B287  45 33 C0                        xor r8d, r8d
0075B28A  48 8B F8                        mov rdi, rax
0075B28D  48 85 C0                        test rax, rax
0075B290  75 0B                           jne 0x14075b29d
0075B292  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
0075B298  E9 C6 02 00 00                  jmp 0x14075b563
0075B29D  4C 8D B0 C0 04 00 00            lea r14, [rax + 0x4c0]
0075B2A4  41 8B D7                        mov edx, r15d
0075B2A7  48 03 D7                        add rdx, rdi
0075B2AA  8B C3                           mov eax, ebx
0075B2AC  48 03 C7                        add rax, rdi
0075B2AF  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0075B2B4  41 8B C8                        mov ecx, r8d
0075B2B7  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0075B2BC  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0075B2C0  44 38 46 0B                     cmp byte ptr [rsi + 0xb], r8b
0075B2C4  74 09                           je 0x14075b2cf
0075B2C6  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
0075B2C9  89 05 9D 9D 86 00               mov dword ptr [rip + 0x869d9d], eax
0075B2CF  45 8B F8                        mov r15d, r8d
0075B2D2  41 BC 01 00 00 00               mov r12d, 1
0075B2D8  44 89 7C 24 24                  mov dword ptr [rsp + 0x24], r15d
0075B2DD  41 BA 64 00 00 00               mov r10d, 0x64
0075B2E3  45 3B FD                        cmp r15d, r13d
0075B2E6  0F 83 8E 02 00 00               jae 0x14075b57a
0075B2EC  41 8B C7                        mov eax, r15d
0075B2EF  48 69 D8 A8 04 00 00            imul rbx, rax, 0x4a8
0075B2F6  45 8B E7                        mov r12d, r15d
0075B2F9  49 C1 E4 05                     shl r12, 5
0075B2FD  4C 03 A6 38 02 00 00            add r12, qword ptr [rsi + 0x238]
0075B304  41 8B 44 24 1C                  mov eax, dword ptr [r12 + 0x1c]
0075B309  42 89 44 33 10                  mov dword ptr [rbx + r14 + 0x10], eax
0075B30E  41 8B 04 24                     mov eax, dword ptr [r12]
0075B312  45 39 44 24 1C                  cmp dword ptr [r12 + 0x1c], r8d
0075B317  74 59                           je 0x14075b372
0075B319  41 83 CD FF                     or r13d, 0xffffffff
0075B31D  42 89 44 33 14                  mov dword ptr [rbx + r14 + 0x14], eax
0075B322  45 8D 4A 9D                     lea r9d, [r10 - 0x63]
0075B326  45 39 4C 24 1C                  cmp dword ptr [r12 + 0x1c], r9d
0075B32B  0F 85 D9 00 00 00               jne 0x14075b40a
0075B331  8B C1                           mov eax, ecx
0075B333  41 03 C9                        add ecx, r9d
0075B336  48 69 C0 10 03 00 00            imul rax, rax, 0x310
0075B33D  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0075B341  48 03 C2                        add rax, rdx
0075B344  48 8B C8                        mov rcx, rax
0075B347  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0075B34C  66 44 89 50 3E                  mov word ptr [rax + 0x3e], r10w
0075B351  E8 1A 8D 00 00                  call 0x140764070
0075B356  45 33 C0                        xor r8d, r8d
0075B359  44 8B F8                        mov r15d, eax
0075B35C  85 C0                           test eax, eax
0075B35E  0F 88 FA 01 00 00               js 0x14075b55e
0075B364  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0075B369  4A 89 04 33                     mov qword ptr [rbx + r14], rax
0075B36D  E9 8D 00 00 00                  jmp 0x14075b3ff
0075B372  44 8B E8                        mov r13d, eax
0075B375  83 F8 FF                        cmp eax, -1
0075B378  0F 84 DA 01 00 00               je 0x14075b558
0075B37E  8B D0                           mov edx, eax
0075B380  48 8D 0D A9 00 6B 00            lea rcx, [rip + 0x6b00a9]
0075B387  E8 C4 9D BA FF                  call 0x140305150
0075B38C  85 C0                           test eax, eax
0075B38E  0F 85 C4 01 00 00               jne 0x14075b558
0075B394  41 8B CD                        mov ecx, r13d
0075B397  E8 34 D2 B7 FF                  call 0x1402d85d0
0075B39C  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0075B3A1  48 05 B0 89 00 00               add rax, 0x89b0
0075B3A7  48 8B C8                        mov rcx, rax
0075B3AA  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0075B3AF  E8 BC 8C 00 00                  call 0x140764070
0075B3B4  44 8B F8                        mov r15d, eax
0075B3B7  85 C0                           test eax, eax
0075B3B9  0F 88 9F 01 00 00               js 0x14075b55e
0075B3BF  41 8B D5                        mov edx, r13d
0075B3C2  48 8D 4D A0                     lea rcx, [rbp - 0x60]
0075B3C6  E8 25 03 B0 FF                  call 0x14025b6f0
0075B3CB  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0075B3D0  4A 89 04 33                     mov qword ptr [rbx + r14], rax
0075B3D4  8B 15 76 9C 86 00               mov edx, dword ptr [rip + 0x869c76]
0075B3DA  83 FA FF                        cmp edx, -1
0075B3DD  0F 44 15 88 9C 86 00            cmove edx, dword ptr [rip + 0x869c88]
0075B3E4  8B CA                           mov ecx, edx
0075B3E6  BA 40 42 0F 00                  mov edx, 0xf4240
0075B3EB  E8 20 C1 CE FF                  call 0x140447510
0075B3F0  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0075B3F5  45 33 C0                        xor r8d, r8d
0075B3F8  48 89 81 38 8A 00 00            mov qword ptr [rcx + 0x8a38], rax
0075B3FF  44 8B 7C 24 24                  mov r15d, dword ptr [rsp + 0x24]
0075B404  41 BA 64 00 00 00               mov r10d, 0x64
0075B40A  4A 83 A4 33 A0 04 00 00 00      and qword ptr [rbx + r14 + 0x4a0], 0
0075B413  46 89 54 33 30                  mov dword ptr [rbx + r14 + 0x30], r10d
0075B418  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
0075B41D  4A 89 44 33 08                  mov qword ptr [rbx + r14 + 8], rax
0075B422  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
0075B427  42 89 44 33 18                  mov dword ptr [rbx + r14 + 0x18], eax
0075B42C  41 8B 44 24 14                  mov eax, dword ptr [r12 + 0x14]
0075B431  42 89 44 33 1C                  mov dword ptr [rbx + r14 + 0x1c], eax
0075B436  41 8B 44 24 18                  mov eax, dword ptr [r12 + 0x18]
0075B43B  42 89 44 33 20                  mov dword ptr [rbx + r14 + 0x20], eax
0075B440  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
0075B444  42 89 44 33 54                  mov dword ptr [rbx + r14 + 0x54], eax
0075B449  B8 01 00 00 00                  mov eax, 1
0075B44E  42 89 44 33 58                  mov dword ptr [rbx + r14 + 0x58], eax
0075B453  46 89 54 33 38                  mov dword ptr [rbx + r14 + 0x38], r10d
0075B458  46 89 54 33 50                  mov dword ptr [rbx + r14 + 0x50], r10d
0075B45D  46 89 54 33 5C                  mov dword ptr [rbx + r14 + 0x5c], r10d
0075B462  46 89 54 33 60                  mov dword ptr [rbx + r14 + 0x60], r10d
0075B467  46 89 94 33 84 00 00 00         mov dword ptr [rbx + r14 + 0x84], r10d
0075B46F  46 89 94 33 88 00 00 00         mov dword ptr [rbx + r14 + 0x88], r10d
0075B477  4E 89 84 33 90 00 00 00         mov qword ptr [rbx + r14 + 0x90], r8
0075B47F  44 38 46 07                     cmp byte ptr [rsi + 7], r8b
0075B483  75 06                           jne 0x14075b48b
0075B485  44 38 46 0B                     cmp byte ptr [rsi + 0xb], r8b
0075B489  75 03                           jne 0x14075b48e
0075B48B  41 8A C0                        mov al, r8b
0075B48E  42 88 84 33 8D 00 00 00         mov byte ptr [rbx + r14 + 0x8d], al
0075B496  45 39 54 24 10                  cmp dword ptr [r12 + 0x10], r10d
0075B49B  73 1F                           jae 0x14075b4bc
0075B49D  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
0075B4A7  41 8B CA                        mov ecx, r10d
0075B4AA  4A 89 44 33 28                  mov qword ptr [rbx + r14 + 0x28], rax
0075B4AF  41 8B D5                        mov edx, r13d
0075B4B2  41 2B 4C 24 10                  sub ecx, dword ptr [r12 + 0x10]
0075B4B7  E8 F4 FD CC FF                  call 0x14042b2b0
0075B4BC  41 8B C7                        mov eax, r15d
0075B4BF  4C 8D 54 24 30                  lea r10, [rsp + 0x30]
0075B4C4  0F AF 44 24 28                  imul eax, dword ptr [rsp + 0x28]
0075B4C9  BB 02 00 00 00                  mov ebx, 2
0075B4CE  44 8D 63 FF                     lea r12d, [rbx - 1]
0075B4D2  44 8B D8                        mov r11d, eax
0075B4D5  4C 8D 0C 40                     lea r9, [rax + rax*2]
0075B4D9  49 C1 E1 04                     shl r9, 4
0075B4DD  4C 03 4C 24 58                  add r9, qword ptr [rsp + 0x58]
0075B4E2  41 8B 0A                        mov ecx, dword ptr [r10]
0075B4E5  83 F9 FF                        cmp ecx, -1
0075B4E8  74 4C                           je 0x14075b536
0075B4EA  48 8B 96 30 02 00 00            mov rdx, qword ptr [rsi + 0x230]
0075B4F1  4C 8D 04 49                     lea r8, [rcx + rcx*2]
0075B4F5  48 8B 86 40 02 00 00            mov rax, qword ptr [rsi + 0x240]
0075B4FC  41 03 CB                        add ecx, r11d
0075B4FF  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0075B503  49 89 49 28                     mov qword ptr [r9 + 0x28], rcx
0075B507  42 8A 44 C2 11                  mov al, byte ptr [rdx + r8*8 + 0x11]
0075B50C  41 88 41 21                     mov byte ptr [r9 + 0x21], al
0075B510  42 8A 44 C2 10                  mov al, byte ptr [rdx + r8*8 + 0x10]
0075B515  41 88 41 20                     mov byte ptr [r9 + 0x20], al
0075B519  42 8A 44 C2 12                  mov al, byte ptr [rdx + r8*8 + 0x12]
0075B51E  41 88 41 22                     mov byte ptr [r9 + 0x22], al
0075B522  42 8B 44 C2 08                  mov eax, dword ptr [rdx + r8*8 + 8]
0075B527  41 89 41 24                     mov dword ptr [r9 + 0x24], eax
0075B52B  4A 8B 04 C2                     mov rax, qword ptr [rdx + r8*8]
0075B52F  49 89 01                        mov qword ptr [r9], rax
0075B532  49 83 C1 30                     add r9, 0x30
0075B536  49 83 C2 04                     add r10, 4
0075B53A  49 2B DC                        sub rbx, r12
0075B53D  75 A3                           jne 0x14075b4e2
0075B53F  44 8B 6C 24 48                  mov r13d, dword ptr [rsp + 0x48]
0075B544  45 03 FC                        add r15d, r12d
0075B547  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
0075B54B  45 33 C0                        xor r8d, r8d
0075B54E  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
0075B553  E9 80 FD FF FF                  jmp 0x14075b2d8
0075B558  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
0075B55E  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0075B563  48 8D 0D 96 16 7B 00            lea rcx, [rip + 0x7b1696]
0075B56A  E8 B9 EE B7 FF                  call 0x1402da428
0075B56F  41 BD 01 00 00 00               mov r13d, 1
0075B575  E9 B3 06 00 00                  jmp 0x14075bc2d
0075B57A  48 8D 4D A0                     lea rcx, [rbp - 0x60]
0075B57E  E8 FD 5F B7 FF                  call 0x1402d1580
0075B583  85 C0                           test eax, eax
0075B585  74 3B                           je 0x14075b5c2
0075B587  33 C9                           xor ecx, ecx
0075B589  41 3B CD                        cmp ecx, r13d
0075B58C  73 26                           jae 0x14075b5b4
0075B58E  8B C1                           mov eax, ecx
0075B590  48 69 C0 A8 04 00 00            imul rax, rax, 0x4a8
0075B597  46 39 64 30 10                  cmp dword ptr [rax + r14 + 0x10], r12d
0075B59C  74 05                           je 0x14075b5a3
0075B59E  41 03 CC                        add ecx, r12d
0075B5A1  EB E6                           jmp 0x14075b589
0075B5A3  4A 8B 04 30                     mov rax, qword ptr [rax + r14]
0075B5A7  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
0075B5AB  44 89 A7 30 01 00 00            mov dword ptr [rdi + 0x130], r12d
0075B5B2  EB 44                           jmp 0x14075b5f8
0075B5B4  75 42                           jne 0x14075b5f8
0075B5B6  C7 87 30 01 00 00 02 00 00 00   mov dword ptr [rdi + 0x130], 2
0075B5C0  EB 36                           jmp 0x14075b5f8
0075B5C2  48 8D 55 A0                     lea rdx, [rbp - 0x60]
0075B5C6  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0075B5CB  E8 40 82 D0 FF                  call 0x140463810
0075B5D0  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0075B5D5  E8 36 45 B7 FF                  call 0x1402cfb10
0075B5DA  8B C8                           mov ecx, eax
0075B5DC  E8 EF CF B7 FF                  call 0x1402d85d0
0075B5E1  48 8D 88 B0 89 00 00            lea rcx, [rax + 0x89b0]
0075B5E8  48 89 4F 10                     mov qword ptr [rdi + 0x10], rcx
0075B5EC  8A 80 08 8A 00 00               mov al, byte ptr [rax + 0x8a08]
0075B5F2  88 87 2C 01 00 00               mov byte ptr [rdi + 0x12c], al
0075B5F8  83 67 1C 00                     and dword ptr [rdi + 0x1c], 0
0075B5FC  48 8D 4F 20                     lea rcx, [rdi + 0x20]
0075B600  33 D2                           xor edx, edx
0075B602  C7 47 18 01 00 20 00            mov dword ptr [rdi + 0x18], 0x200001
0075B609  41 B8 00 01 00 00               mov r8d, 0x100
0075B60F  41 BF 01 00 00 00               mov r15d, 1
0075B615  E8 26 B6 F6 FF                  call 0x1406c6c40
0075B61A  0F B7 57 1A                     movzx edx, word ptr [rdi + 0x1a]
0075B61E  4C 8D 45 A0                     lea r8, [rbp - 0x60]
0075B622  48 8D 4F 18                     lea rcx, [rdi + 0x18]
0075B626  E8 35 32 B7 FF                  call 0x1402ce860
0075B62B  48 8B 86 78 01 00 00            mov rax, qword ptr [rsi + 0x178]
0075B632  33 C9                           xor ecx, ecx
0075B634  48 89 87 40 01 00 00            mov qword ptr [rdi + 0x140], rax
0075B63B  48 8B 86 88 01 00 00            mov rax, qword ptr [rsi + 0x188]
0075B642  48 89 87 50 01 00 00            mov qword ptr [rdi + 0x150], rax
0075B649  48 8B 86 90 01 00 00            mov rax, qword ptr [rsi + 0x190]
0075B650  48 89 87 58 01 00 00            mov qword ptr [rdi + 0x158], rax
0075B657  48 8B 86 98 01 00 00            mov rax, qword ptr [rsi + 0x198]
0075B65E  48 89 87 60 01 00 00            mov qword ptr [rdi + 0x160], rax
0075B665  48 8B 86 A0 01 00 00            mov rax, qword ptr [rsi + 0x1a0]
0075B66C  48 89 87 68 01 00 00            mov qword ptr [rdi + 0x168], rax
0075B673  48 8B 86 80 01 00 00            mov rax, qword ptr [rsi + 0x180]
0075B67A  48 89 87 48 01 00 00            mov qword ptr [rdi + 0x148], rax
0075B681  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
0075B685  48 89 87 20 01 00 00            mov qword ptr [rdi + 0x120], rax
0075B68C  4C 89 B7 38 01 00 00            mov qword ptr [rdi + 0x138], r14
0075B693  44 89 BF 24 03 00 00            mov dword ptr [rdi + 0x324], r15d
0075B69A  E8 41 31 C2 FF                  call 0x14037e7e0
0075B69F  44 8B 64 24 3C                  mov r12d, dword ptr [rsp + 0x3c]
0075B6A4  33 DB                           xor ebx, ebx
0075B6A6  48 89 87 B0 04 00 00            mov qword ptr [rdi + 0x4b0], rax
0075B6AD  44 89 A7 C0 01 00 00            mov dword ptr [rdi + 0x1c0], r12d
0075B6B4  44 89 AF 28 01 00 00            mov dword ptr [rdi + 0x128], r13d
0075B6BB  8B 46 2C                        mov eax, dword ptr [rsi + 0x2c]
0075B6BE  8D 4B 07                        lea ecx, [rbx + 7]
0075B6C1  89 87 D0 01 00 00               mov dword ptr [rdi + 0x1d0], eax
0075B6C7  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
0075B6CA  89 87 C4 01 00 00               mov dword ptr [rdi + 0x1c4], eax
0075B6D0  8B 46 1C                        mov eax, dword ptr [rsi + 0x1c]
0075B6D3  89 87 C8 01 00 00               mov dword ptr [rdi + 0x1c8], eax
0075B6D9  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0075B6DC  89 87 CC 01 00 00               mov dword ptr [rdi + 0x1cc], eax
0075B6E2  8A 46 0F                        mov al, byte ptr [rsi + 0xf]
0075B6E5  88 87 F0 01 00 00               mov byte ptr [rdi + 0x1f0], al
0075B6EB  8A 46 04                        mov al, byte ptr [rsi + 4]
0075B6EE  88 87 E9 01 00 00               mov byte ptr [rdi + 0x1e9], al
0075B6F4  48 8B 86 D0 01 00 00            mov rax, qword ptr [rsi + 0x1d0]
0075B6FB  48 89 87 88 01 00 00            mov qword ptr [rdi + 0x188], rax
0075B702  48 8B 86 D8 01 00 00            mov rax, qword ptr [rsi + 0x1d8]
0075B709  48 89 87 90 01 00 00            mov qword ptr [rdi + 0x190], rax
0075B710  48 8B 86 E0 01 00 00            mov rax, qword ptr [rsi + 0x1e0]
0075B717  48 89 87 98 01 00 00            mov qword ptr [rdi + 0x198], rax
0075B71E  48 8B 86 00 02 00 00            mov rax, qword ptr [rsi + 0x200]
0075B725  48 89 87 A0 01 00 00            mov qword ptr [rdi + 0x1a0], rax
0075B72C  48 8B 86 08 02 00 00            mov rax, qword ptr [rsi + 0x208]
0075B733  48 89 87 A8 01 00 00            mov qword ptr [rdi + 0x1a8], rax
0075B73A  48 8B 86 10 02 00 00            mov rax, qword ptr [rsi + 0x210]
0075B741  48 89 87 B0 01 00 00            mov qword ptr [rdi + 0x1b0], rax
0075B748  48 8B 86 B8 01 00 00            mov rax, qword ptr [rsi + 0x1b8]
0075B74F  48 89 87 70 01 00 00            mov qword ptr [rdi + 0x170], rax
0075B756  48 8B 86 C0 01 00 00            mov rax, qword ptr [rsi + 0x1c0]
0075B75D  48 89 87 78 01 00 00            mov qword ptr [rdi + 0x178], rax
0075B764  48 8B 86 C8 01 00 00            mov rax, qword ptr [rsi + 0x1c8]
0075B76B  48 89 87 80 01 00 00            mov qword ptr [rdi + 0x180], rax
0075B772  8A 46 34                        mov al, byte ptr [rsi + 0x34]
0075B775  88 87 09 02 00 00               mov byte ptr [rdi + 0x209], al
0075B77B  38 5E 34                        cmp byte ptr [rsi + 0x34], bl
0075B77E  0F 95 C0                        setne al
0075B781  88 87 08 02 00 00               mov byte ptr [rdi + 0x208], al
0075B787  8A 46 09                        mov al, byte ptr [rsi + 9]
0075B78A  88 87 0B 02 00 00               mov byte ptr [rdi + 0x20b], al
0075B790  48 8D 87 3C 03 00 00            lea rax, [rdi + 0x33c]
0075B797  C7 40 FC 64 00 00 00            mov dword ptr [rax - 4], 0x64
0075B79E  44 89 20                        mov dword ptr [rax], r12d
0075B7A1  48 8D 40 38                     lea rax, [rax + 0x38]
0075B7A5  49 2B CF                        sub rcx, r15
0075B7A8  75 ED                           jne 0x14075b797
0075B7AA  8A 46 06                        mov al, byte ptr [rsi + 6]
0075B7AD  88 87 EA 01 00 00               mov byte ptr [rdi + 0x1ea], al
0075B7B3  8A 46 07                        mov al, byte ptr [rsi + 7]
0075B7B6  88 87 EB 01 00 00               mov byte ptr [rdi + 0x1eb], al
0075B7BC  8A 46 08                        mov al, byte ptr [rsi + 8]
0075B7BF  88 87 EC 01 00 00               mov byte ptr [rdi + 0x1ec], al
0075B7C5  B8 FD 00 00 00                  mov eax, 0xfd
0075B7CA  66 39 46 04                     cmp word ptr [rsi + 4], ax
0075B7CE  74 0C                           je 0x14075b7dc
0075B7D0  41 8A C7                        mov al, r15b
0075B7D3  48 39 9E E0 01 00 00            cmp qword ptr [rsi + 0x1e0], rbx
0075B7DA  74 02                           je 0x14075b7de
0075B7DC  8A C3                           mov al, bl
0075B7DE  88 87 EE 01 00 00               mov byte ptr [rdi + 0x1ee], al
0075B7E4  8A 46 0B                        mov al, byte ptr [rsi + 0xb]
0075B7E7  88 87 ED 01 00 00               mov byte ptr [rdi + 0x1ed], al
0075B7ED  83 3D BC 98 86 00 FF            cmp dword ptr [rip + 0x8698bc], -1
0075B7F4  75 0E                           jne 0x14075b804
0075B7F6  38 5E 0C                        cmp byte ptr [rsi + 0xc], bl
0075B7F9  8B C3                           mov eax, ebx
0075B7FB  0F 95 C0                        setne al
0075B7FE  89 05 AC 98 86 00               mov dword ptr [rip + 0x8698ac], eax
0075B804  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
0075B808  48 89 87 D8 01 00 00            mov qword ptr [rdi + 0x1d8], rax
0075B80F  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
0075B813  48 89 87 E0 01 00 00            mov qword ptr [rdi + 0x1e0], rax
0075B81A  C6 87 E8 01 00 00 64            mov byte ptr [rdi + 0x1e8], 0x64
0075B821  8B 46 28                        mov eax, dword ptr [rsi + 0x28]
0075B824  48 39 05 25 FA 7A 00            cmp qword ptr [rip + 0x7afa25], rax
0075B82B  77 07                           ja 0x14075b834
0075B82D  48 89 05 1C FA 7A 00            mov qword ptr [rip + 0x7afa1c], rax
0075B834  48 39 9F 58 01 00 00            cmp qword ptr [rdi + 0x158], rbx
0075B83B  74 07                           je 0x14075b844
0075B83D  83 0D 3C 29 7B 00 40            or dword ptr [rip + 0x7b293c], 0x40
0075B844  48 39 9F 50 01 00 00            cmp qword ptr [rdi + 0x150], rbx
0075B84B  74 0B                           je 0x14075b858
0075B84D  B8 20 00 00 00                  mov eax, 0x20
0075B852  09 05 28 29 7B 00               or dword ptr [rip + 0x7b2928], eax
0075B858  48 39 9F 48 01 00 00            cmp qword ptr [rdi + 0x148], rbx
0075B85F  74 08                           je 0x14075b869
0075B861  0F BA 2D 17 29 7B 00 09         bts dword ptr [rip + 0x7b2917], 9
0075B869  48 39 9F 68 01 00 00            cmp qword ptr [rdi + 0x168], rbx
0075B870  74 08                           je 0x14075b87a
0075B872  0F BA 2D 06 29 7B 00 07         bts dword ptr [rip + 0x7b2906], 7
0075B87A  48 39 9F 60 01 00 00            cmp qword ptr [rdi + 0x160], rbx
0075B881  74 08                           je 0x14075b88b
0075B883  0F BA 2D F5 28 7B 00 08         bts dword ptr [rip + 0x7b28f5], 8
0075B88B  38 5E 09                        cmp byte ptr [rsi + 9], bl
0075B88E  74 07                           je 0x14075b897
0075B890  44 88 3D 60 B2 86 00            mov byte ptr [rip + 0x86b260], r15b
0075B897  38 5E 0A                        cmp byte ptr [rsi + 0xa], bl
0075B89A  74 07                           je 0x14075b8a3
0075B89C  44 88 3D 58 B2 86 00            mov byte ptr [rip + 0x86b258], r15b
0075B8A3  8A 46 0D                        mov al, byte ptr [rsi + 0xd]
0075B8A6  88 87 EF 01 00 00               mov byte ptr [rdi + 0x1ef], al
0075B8AC  8B 46 48                        mov eax, dword ptr [rsi + 0x48]
0075B8AF  89 87 F4 01 00 00               mov dword ptr [rdi + 0x1f4], eax
0075B8B5  8B 46 4C                        mov eax, dword ptr [rsi + 0x4c]
0075B8B8  89 87 F8 01 00 00               mov dword ptr [rdi + 0x1f8], eax
0075B8BE  8B 46 50                        mov eax, dword ptr [rsi + 0x50]
0075B8C1  89 87 FC 01 00 00               mov dword ptr [rdi + 0x1fc], eax
0075B8C7  8B 46 54                        mov eax, dword ptr [rsi + 0x54]
0075B8CA  89 87 00 02 00 00               mov dword ptr [rdi + 0x200], eax
0075B8D0  8B 46 58                        mov eax, dword ptr [rsi + 0x58]
0075B8D3  89 87 04 02 00 00               mov dword ptr [rdi + 0x204], eax
0075B8D9  F0 09 1C 24                     lock or dword ptr [rsp], ebx
0075B8DD  44 8B E3                        mov r12d, ebx
0075B8E0  45 85 ED                        test r13d, r13d
0075B8E3  0F 84 DA 00 00 00               je 0x14075b9c3
0075B8E9  4D 8D 7E 10                     lea r15, [r14 + 0x10]
0075B8ED  41 83 3F 02                     cmp dword ptr [r15], 2
0075B8F1  0F 84 B3 00 00 00               je 0x14075b9aa
0075B8F7  49 8B 5F F0                     mov rbx, qword ptr [r15 - 0x10]
0075B8FB  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
0075B900  41 8B C4                        mov eax, r12d
0075B903  0F 57 C0                        xorps xmm0, xmm0
0075B906  48 69 C8 A8 04 00 00            imul rcx, rax, 0x4a8
0075B90D  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
0075B912  41 8B C4                        mov eax, r12d
0075B915  C7 43 40 00 00 01 00            mov dword ptr [rbx + 0x40], 0x10000
0075B91C  0F AF 44 24 28                  imul eax, dword ptr [rsp + 0x28]
0075B921  41 B8 02 00 00 00               mov r8d, 2
0075B927  49 03 CE                        add rcx, r14
0075B92A  48 89 3B                        mov qword ptr [rbx], rdi
0075B92D  48 89 4B 08                     mov qword ptr [rbx + 8], rcx
0075B931  48 8D 0C 40                     lea rcx, [rax + rax*2]
0075B935  48 C1 E1 04                     shl rcx, 4
0075B939  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0075B93E  48 03 4C 24 58                  add rcx, qword ptr [rsp + 0x58]
0075B943  83 3A FF                        cmp dword ptr [rdx], -1
0075B946  74 07                           je 0x14075b94f
0075B948  48 89 08                        mov qword ptr [rax], rcx
0075B94B  48 83 C1 30                     add rcx, 0x30
0075B94F  48 83 C2 04                     add rdx, 4
0075B953  48 83 C0 08                     add rax, 8
0075B957  49 83 E8 01                     sub r8, 1
0075B95B  75 E6                           jne 0x14075b943
0075B95D  45 39 07                        cmp dword ptr [r15], r8d
0075B960  74 33                           je 0x14075b995
0075B962  48 8B CB                        mov rcx, rbx
0075B965  E8 5E 40 35 00                  call 0x140aaf9c8
0075B96A  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0075B96F  BA 02 00 00 00                  mov edx, 2
0075B974  48 2B D9                        sub rbx, rcx
0075B977  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0075B97C  48 8B 08                        mov rcx, qword ptr [rax]
0075B97F  48 85 C9                        test rcx, rcx
0075B982  74 05                           je 0x14075b989
0075B984  48 89 4C 03 60                  mov qword ptr [rbx + rax + 0x60], rcx
0075B989  48 83 C0 08                     add rax, 8
0075B98D  48 83 EA 01                     sub rdx, 1
0075B991  75 E9                           jne 0x14075b97c
0075B993  EB 15                           jmp 0x14075b9aa
0075B995  44 8A 46 0E                     mov r8b, byte ptr [rsi + 0xe]
0075B999  48 8D 8B 50 76 FF FF            lea rcx, [rbx - 0x89b0]
0075B9A0  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
0075B9A5  E8 D2 8D D7 FF                  call 0x1404d477c
0075B9AA  41 FF C4                        inc r12d
0075B9AD  49 81 C7 A8 04 00 00            add r15, 0x4a8
0075B9B4  45 3B E5                        cmp r12d, r13d
0075B9B7  0F 82 30 FF FF FF               jb 0x14075b8ed
0075B9BD  33 DB                           xor ebx, ebx
0075B9BF  44 8D 7B 01                     lea r15d, [rbx + 1]
0075B9C3  48 39 1D 96 28 7B 00            cmp qword ptr [rip + 0x7b2896], rbx
0075B9CA  75 0B                           jne 0x14075b9d7
0075B9CC  48 8B 46 60                     mov rax, qword ptr [rsi + 0x60]
0075B9D0  48 89 05 89 28 7B 00            mov qword ptr [rip + 0x7b2889], rax
0075B9D7  48 8B 0D 7A 28 7B 00            mov rcx, qword ptr [rip + 0x7b287a]
0075B9DE  48 85 C9                        test rcx, rcx
0075B9E1  75 0E                           jne 0x14075b9f1
0075B9E3  48 8B 8E E8 01 00 00            mov rcx, qword ptr [rsi + 0x1e8]
0075B9EA  48 89 0D 67 28 7B 00            mov qword ptr [rip + 0x7b2867], rcx
0075B9F1  48 39 1D 78 28 7B 00            cmp qword ptr [rip + 0x7b2878], rbx
0075B9F8  75 0E                           jne 0x14075ba08
0075B9FA  48 8B 86 F0 01 00 00            mov rax, qword ptr [rsi + 0x1f0]
0075BA01  48 89 05 68 28 7B 00            mov qword ptr [rip + 0x7b2868], rax
0075BA08  48 39 1D 59 28 7B 00            cmp qword ptr [rip + 0x7b2859], rbx
0075BA0F  75 0E                           jne 0x14075ba1f
0075BA11  48 8B 86 F8 01 00 00            mov rax, qword ptr [rsi + 0x1f8]
0075BA18  48 89 05 49 28 7B 00            mov qword ptr [rip + 0x7b2849], rax
0075BA1F  48 39 1D 5A 28 7B 00            cmp qword ptr [rip + 0x7b285a], rbx
0075BA26  75 0E                           jne 0x14075ba36
0075BA28  48 8B 86 18 02 00 00            mov rax, qword ptr [rsi + 0x218]
0075BA2F  48 89 05 4A 28 7B 00            mov qword ptr [rip + 0x7b284a], rax
0075BA36  48 39 1D 3B 28 7B 00            cmp qword ptr [rip + 0x7b283b], rbx
0075BA3D  75 0E                           jne 0x14075ba4d
0075BA3F  48 8B 86 20 02 00 00            mov rax, qword ptr [rsi + 0x220]
0075BA46  48 89 05 2B 28 7B 00            mov qword ptr [rip + 0x7b282b], rax
0075BA4D  48 39 1D 3C 28 7B 00            cmp qword ptr [rip + 0x7b283c], rbx
0075BA54  75 0E                           jne 0x14075ba64
0075BA56  48 8B 86 28 02 00 00            mov rax, qword ptr [rsi + 0x228]
0075BA5D  48 89 05 2C 28 7B 00            mov qword ptr [rip + 0x7b282c], rax
0075BA64  48 39 1D 1D 28 7B 00            cmp qword ptr [rip + 0x7b281d], rbx
0075BA6B  75 0E                           jne 0x14075ba7b
0075BA6D  48 8B 86 A8 01 00 00            mov rax, qword ptr [rsi + 0x1a8]
0075BA74  48 89 05 0D 28 7B 00            mov qword ptr [rip + 0x7b280d], rax
0075BA7B  48 39 1D 16 28 7B 00            cmp qword ptr [rip + 0x7b2816], rbx
0075BA82  75 0E                           jne 0x14075ba92
0075BA84  48 8B 86 B0 01 00 00            mov rax, qword ptr [rsi + 0x1b0]
0075BA8B  48 89 05 06 28 7B 00            mov qword ptr [rip + 0x7b2806], rax
0075BA92  48 85 C9                        test rcx, rcx
0075BA95  74 07                           je 0x14075ba9e
0075BA97  44 88 3D BA F7 7A 00            mov byte ptr [rip + 0x7af7ba], r15b
0075BA9E  8B 05 4C B2 86 00               mov eax, dword ptr [rip + 0x86b24c]
0075BAA4  48 8D 35 FD B0 86 00            lea rsi, [rip + 0x86b0fd]
0075BAAB  41 03 C7                        add eax, r15d
0075BAAE  89 87 B8 01 00 00               mov dword ptr [rdi + 0x1b8], eax
0075BAB4  89 05 36 B2 86 00               mov dword ptr [rip + 0x86b236], eax
0075BABA  48 8B 05 EF B0 86 00            mov rax, qword ptr [rip + 0x86b0ef]
0075BAC1  48 39 30                        cmp qword ptr [rax], rsi
0075BAC4  74 07                           je 0x14075bacd
0075BAC6  B9 03 00 00 00                  mov ecx, 3
0075BACB  CD 29                           int 0x29
0075BACD  48 89 37                        mov qword ptr [rdi], rsi
0075BAD0  45 8A C7                        mov r8b, r15b
0075BAD3  48 89 47 08                     mov qword ptr [rdi + 8], rax
0075BAD7  48 89 38                        mov qword ptr [rax], rdi
0075BADA  48 8B 15 C7 B0 86 00            mov rdx, qword ptr [rip + 0x86b0c7]
0075BAE1  48 89 3D C8 B0 86 00            mov qword ptr [rip + 0x86b0c8], rdi
0075BAE8  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
0075BAED  48 3B D6                        cmp rdx, rsi
0075BAF0  74 1A                           je 0x14075bb0c
0075BAF2  8A 82 ED 01 00 00               mov al, byte ptr [rdx + 0x1ed]
0075BAF8  48 8B 12                        mov rdx, qword ptr [rdx]
0075BAFB  F6 D8                           neg al
0075BAFD  1A C9                           sbb cl, cl
0075BAFF  44 22 C1                        and r8b, cl
0075BB02  48 3B D6                        cmp rdx, rsi
0075BB05  75 EB                           jne 0x14075baf2
0075BB07  44 88 44 24 20                  mov byte ptr [rsp + 0x20], r8b
0075BB0C  44 0F B7 0D 1E F9 6A 00         movzx r9d, word ptr [rip + 0x6af91e]
0075BB14  4C 8D 05 15 F9 6A 00            lea r8, [rip + 0x6af915]
0075BB1B  49 8B D0                        mov rdx, r8
0075BB1E  48 8D 4D A0                     lea rcx, [rbp - 0x60]
0075BB22  E8 25 ED C3 FF                  call 0x14039a84c
0075BB27  48 8D 15 72 FA 6A 00            lea rdx, [rip + 0x6afa72]
0075BB2E  49 8B C8                        mov rcx, r8
0075BB31  E8 FA 96 BA FF                  call 0x140305230
0075BB36  85 C0                           test eax, eax
0075BB38  0F 84 9D 00 00 00               je 0x14075bbdb
0075BB3E  48 8B 0D 63 B0 86 00            mov rcx, qword ptr [rip + 0x86b063]
0075BB45  41 8A D7                        mov dl, r15b
0075BB48  48 3B CE                        cmp rcx, rsi
0075BB4B  0F 84 84 00 00 00               je 0x14075bbd5
0075BB51  38 99 EF 01 00 00               cmp byte ptr [rcx + 0x1ef], bl
0075BB57  74 7A                           je 0x14075bbd3
0075BB59  48 8B 87 E0 01 00 00            mov rax, qword ptr [rdi + 0x1e0]
0075BB60  48 39 81 E0 01 00 00            cmp qword ptr [rcx + 0x1e0], rax
0075BB67  75 6A                           jne 0x14075bbd3
0075BB69  8B 87 CC 01 00 00               mov eax, dword ptr [rdi + 0x1cc]
0075BB6F  39 81 CC 01 00 00               cmp dword ptr [rcx + 0x1cc], eax
0075BB75  75 5C                           jne 0x14075bbd3
0075BB77  8B 87 C4 01 00 00               mov eax, dword ptr [rdi + 0x1c4]
0075BB7D  39 81 C4 01 00 00               cmp dword ptr [rcx + 0x1c4], eax
0075BB83  75 4E                           jne 0x14075bbd3
0075BB85  8B 87 F4 01 00 00               mov eax, dword ptr [rdi + 0x1f4]
0075BB8B  39 81 F4 01 00 00               cmp dword ptr [rcx + 0x1f4], eax
0075BB91  75 40                           jne 0x14075bbd3
0075BB93  8B 87 F8 01 00 00               mov eax, dword ptr [rdi + 0x1f8]
0075BB99  39 81 F8 01 00 00               cmp dword ptr [rcx + 0x1f8], eax
0075BB9F  75 32                           jne 0x14075bbd3
0075BBA1  8B 87 FC 01 00 00               mov eax, dword ptr [rdi + 0x1fc]
0075BBA7  39 81 FC 01 00 00               cmp dword ptr [rcx + 0x1fc], eax
0075BBAD  75 24                           jne 0x14075bbd3
0075BBAF  8B 87 00 02 00 00               mov eax, dword ptr [rdi + 0x200]
0075BBB5  39 81 00 02 00 00               cmp dword ptr [rcx + 0x200], eax
0075BBBB  75 16                           jne 0x14075bbd3
0075BBBD  8B 87 04 02 00 00               mov eax, dword ptr [rdi + 0x204]
0075BBC3  39 81 04 02 00 00               cmp dword ptr [rcx + 0x204], eax
0075BBC9  75 08                           jne 0x14075bbd3
0075BBCB  48 8B 09                        mov rcx, qword ptr [rcx]
0075BBCE  E9 75 FF FF FF                  jmp 0x14075bb48
0075BBD3  8A D3                           mov dl, bl
0075BBD5  88 15 11 AF 86 00               mov byte ptr [rip + 0x86af11], dl
0075BBDB  48 8B D7                        mov rdx, rdi
0075BBDE  66 C7 87 BC 04 00 00 01 01      mov word ptr [rdi + 0x4bc], 0x101
0075BBE7  48 8D 0D 92 25 7B 00            lea rcx, [rip + 0x7b2592]
0075BBEE  E8 31 77 2F 00                  call 0x140a53324
0075BBF3  48 8B CF                        mov rcx, rdi
0075BBF6  E8 D5 C8 E7 FF                  call 0x1405d84d0
0075BBFB  33 D2                           xor edx, edx
0075BBFD  48 8D 4D A0                     lea rcx, [rbp - 0x60]
0075BC01  E8 4A 95 BA FF                  call 0x140305150
0075BC06  85 C0                           test eax, eax
0075BC08  74 05                           je 0x14075bc0f
0075BC0A  E8 2D A5 D5 FF                  call 0x1404b613c
0075BC0F  E8 C4 91 32 00                  call 0x140a84dd8
0075BC14  48 8B FB                        mov rdi, rbx
0075BC17  44 8B FB                        mov r15d, ebx
0075BC1A  41 BD 01 00 00 00               mov r13d, 1
0075BC20  41 8A CD                        mov cl, r13b
0075BC23  E8 08 B4 33 00                  call 0x140a97030
0075BC28  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0075BC2D  8A 5C 24 20                     mov bl, byte ptr [rsp + 0x20]
0075BC31  45 33 F6                        xor r14d, r14d
0075BC34  44 39 2D B5 B0 86 00            cmp dword ptr [rip + 0x86b0b5], r13d
0075BC3B  77 04                           ja 0x14075bc41
0075BC3D  84 DB                           test bl, bl
0075BC3F  74 34                           je 0x14075bc75
0075BC41  48 8D 15 58 F9 6A 00            lea rdx, [rip + 0x6af958]
0075BC48  48 8D 0D E1 F7 6A 00            lea rcx, [rip + 0x6af7e1]
0075BC4F  E8 DC 95 BA FF                  call 0x140305230
0075BC54  85 C0                           test eax, eax
0075BC56  74 1D                           je 0x14075bc75
0075BC58  48 8D 0D A1 0F 7B 00            lea rcx, [rip + 0x7b0fa1]
0075BC5F  E8 40 DE B7 FF                  call 0x1402d9aa4
0075BC64  45 33 C0                        xor r8d, r8d
0075BC67  88 1D 6F AE 86 00               mov byte ptr [rip + 0x86ae6f], bl
0075BC6D  41 8A CD                        mov cl, r13b
0075BC70  E8 93 74 2F 00                  call 0x140a53108
0075BC75  48 85 FF                        test rdi, rdi
0075BC78  0F 84 A6 00 00 00               je 0x14075bd24
0075BC7E  8B 44 24 2C                     mov eax, dword ptr [rsp + 0x2c]
0075BC82  85 C0                           test eax, eax
0075BC84  0F 84 8D 00 00 00               je 0x14075bd17
0075BC8A  49 8D 5C 24 10                  lea rbx, [r12 + 0x10]
0075BC8F  8B F0                           mov esi, eax
0075BC91  48 8B 03                        mov rax, qword ptr [rbx]
0075BC94  48 85 C0                        test rax, rax
0075BC97  74 6E                           je 0x14075bd07
0075BC99  48 8B 48 58                     mov rcx, qword ptr [rax + 0x58]
0075BC9D  41 BC 50 50 4D 70               mov r12d, 0x704d5050
0075BCA3  48 85 C9                        test rcx, rcx
0075BCA6  74 0F                           je 0x14075bcb7
0075BCA8  41 8B D4                        mov edx, r12d
0075BCAB  E8 C0 6B 42 00                  call 0x140b82870
0075BCB0  48 8B 03                        mov rax, qword ptr [rbx]
0075BCB3  4C 89 70 58                     mov qword ptr [rax + 0x58], r14
0075BCB7  48 8B 03                        mov rax, qword ptr [rbx]
0075BCBA  48 8B 88 98 00 00 00            mov rcx, qword ptr [rax + 0x98]
0075BCC1  48 85 C9                        test rcx, rcx
0075BCC4  74 12                           je 0x14075bcd8
0075BCC6  41 8B D4                        mov edx, r12d
0075BCC9  E8 A2 6B 42 00                  call 0x140b82870
0075BCCE  48 8B 03                        mov rax, qword ptr [rbx]
0075BCD1  4C 89 B0 98 00 00 00            mov qword ptr [rax + 0x98], r14
0075BCD8  48 8B 03                        mov rax, qword ptr [rbx]
0075BCDB  48 8B 88 D8 00 00 00            mov rcx, qword ptr [rax + 0xd8]
0075BCE2  48 85 C9                        test rcx, rcx
0075BCE5  74 12                           je 0x14075bcf9
0075BCE7  41 8B D4                        mov edx, r12d
0075BCEA  E8 81 6B 42 00                  call 0x140b82870
0075BCEF  48 8B 03                        mov rax, qword ptr [rbx]
0075BCF2  4C 89 B0 D8 00 00 00            mov qword ptr [rax + 0xd8], r14
0075BCF9  48 8B 0B                        mov rcx, qword ptr [rbx]
0075BCFC  41 8B D4                        mov edx, r12d
0075BCFF  E8 6C 6B 42 00                  call 0x140b82870
0075BD04  4C 89 33                        mov qword ptr [rbx], r14
0075BD07  48 81 C3 10 03 00 00            add rbx, 0x310
0075BD0E  49 2B F5                        sub rsi, r13
0075BD11  0F 85 7A FF FF FF               jne 0x14075bc91
0075BD17  BA 50 50 4D 70                  mov edx, 0x704d5050
0075BD1C  48 8B CF                        mov rcx, rdi
0075BD1F  E8 4C 6B 42 00                  call 0x140b82870
0075BD24  48 83 4D 90 FF                  or qword ptr [rbp - 0x70], 0xffffffffffffffff
0075BD29  4C 8D 4D 88                     lea r9, [rbp - 0x78]
0075BD2D  48 BA 00 98 3B 9E F7 FF FF FF   movabs rdx, 0xfffffff79e3b9800
0075BD37  48 8D 0D 62 24 7B 00            lea rcx, [rip + 0x7b2462]
0075BD3E  49 B8 00 68 C4 61 08 00 00 00   movabs r8, 0x861c46800
0075BD48  E8 93 4B C4 FF                  call 0x1403a08e0
0075BD4D  41 8B C7                        mov eax, r15d
0075BD50  48 8B 8D C0 01 00 00            mov rcx, qword ptr [rbp + 0x1c0]
0075BD57  48 33 CC                        xor rcx, rsp
0075BD5A  E8 E1 08 F5 FF                  call 0x1406ac640
0075BD5F  4C 8D 9C 24 D0 02 00 00         lea r11, [rsp + 0x2d0]
0075BD67  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0075BD6B  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0075BD6F  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0075BD73  49 8B E3                        mov rsp, r11
0075BD76  41 5F                           pop r15
0075BD78  41 5E                           pop r14
0075BD7A  41 5D                           pop r13
0075BD7C  41 5C                           pop r12
0075BD7E  5D                              pop rbp
0075BD7F  C3                              ret
0075BD80  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmRegisterPerfStates(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned int v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned int v_stack_m2BC;
    unsigned int v_stack_m2C0;
    unsigned int v_stack_m2C4;
    unsigned __int64 v_stack_m2C8;
    unsigned int v_stack_m2CC;
    unsigned int v_stack_m2D0;
    unsigned int v_stack_m2D4;
    unsigned __int8 v_stack_m2D8;
    unsigned int v_stack_m2F8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (720);
    result = (*(unsigned __int64 *)(v_rip + 7009935)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 504 + 448) = result;
    a2 = 0;
    result = memset(v_rsp - 504 + 184, a2, 256, a4);
    a2 = 0;
    v_stack_m280 = v_xmm0;
    result = memset(v_rsp - 504 - 88, a2, 256, a4);
    v_r15 = 0;
    v_stack_m2B0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    a2 = 0;
    v_stack_m2D8 = 0;
    v_stack_m2BC = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)));
    v_stack_m298 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 504 - 96) = 0x200001ULL;
    *(unsigned __int64 *)(v_rsp - 504 - 120) = v_xmm1;
    result = memset(v_rsp - 504 - 88, a2, 256, a4);
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 504 + 176) = 0x200001ULL;
    result = memset(v_rsp - 504 + 184, a2, 256, a4);
    result = KeQueryActiveProcessorAffinity2(v_rsp - 504 + 176, a2, 256, a4);
    v_stack_m2CC = 0;
    if ((unsigned __int8)((unsigned __int8)(a2)) == 0) {
        a1 = v_rip + 8067722;
        result = PpmAcquireLock(a1, a2, 256, 0);
        a4 = 0;
    }
    v_rbx = 0;
    v_r15 = (unsigned int)((v_r15) | (0xFFFFFFFFULL));
loc_0075B190:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 36))))) goto loc_0075B1C9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 560) + 0 + 0 * 2 * 8 + 12)))) >= 2) goto loc_0075B1BE;
    if ((*(unsigned int *)(v_rsp + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 560) + 0 + 0 * 2 * 8 + 12)) * 4 + 48)) == ((unsigned int)(v_r15))) {
        *(unsigned int *)(v_rsp + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 560) + 0 + 0 * 2 * 8 + 12)) * 4 + 48) = 0;
    }
    a2 = (unsigned int)((0) + ((unsigned int)(v_rbx + 1)));
    goto loc_0075B190;
loc_0075B1BE:
    goto loc_0075B563;
loc_0075B1C9:
    if (v_stack_m2C8 != ((unsigned int)((unsigned int)(0xC000000DULL)))) goto loc_0075B1D7;
    if (v_stack_m2C4 == ((unsigned int)((unsigned int)(0xC000000DULL)))) goto loc_0075B1BE;
loc_0075B1D7:
loc_0075B1E5:
    a1 = 0 + 1;
    if ((*(unsigned int *)(v_stack_m2C8)) == ((unsigned int)((unsigned int)(0xC000000DULL)))) { a1 = 0; }
    a3 = (2) - (v_rbx + 1);
    if (condition_is_not_equal) goto loc_0075B1E5;
    v_stack_m2D0 = (unsigned int)(a1);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))) == 0) goto loc_0075B238;
    a2 = (*(unsigned __int64 *)(a1 + 568)) + (28);
loc_0075B219:
    a1 = a4 + 1;
    if ((*(unsigned int *)(a2)) != ((unsigned int)(v_rbx + 1))) { a1 = (unsigned int)(a4); }
    a2 = (a2) + (32);
    a3 = ((unsigned int)(*(unsigned int *)(a1 + 16))) - (v_rbx + 1);
    if (condition_is_not_equal) goto loc_0075B219;
    v_stack_m2CC = (unsigned int)(a1);
loc_0075B238:
    v_rbx = (unsigned int)((v_rbx) * ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) * ((unsigned int)((unsigned int)(v_stack_m2D0))));
    a1 = 0;
    v_rbx = (unsigned int)((v_rbx) + (0x4C7ULL));
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFF8ULL));
    v_r15 = (unsigned int)((result + result * 2) << (4));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_rbx)));
    result = (unsigned int)((unsigned int)(v_r15));
    if ((unsigned int)((unsigned int)((unsigned int)(a1))) != 0) {
        result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) * ((unsigned int)((unsigned int)((unsigned int)(a1)))));
        result = (unsigned int)((result) + ((unsigned int)(v_r15)));
    }
    if ((unsigned int)((unsigned int)((unsigned int)(a1))) == 0) { v_r15 = 0; }
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)(result)), (unsigned int)(0x704D5050ULL), (unsigned int)((unsigned int)(a1)));
    a3 = 0;
    if (result != 0) goto loc_0075B29D;
    goto loc_0075B563;
loc_0075B29D:
    a2 = ((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)))) + (result);
    result = ((unsigned int)((unsigned int)(v_rbx))) + (result);
    v_stack_m2B8 = a2;
    v_stack_m2A0 = result;
    v_stack_m2C0 = 0;
    if ((*(unsigned __int8 *)(a1 + 11)) != 0) {
        result = *(unsigned int *)(a1 + 48);
        *(unsigned int *)(v_rip + 8822173) = (unsigned int)(result);
    }
loc_0075B2D8:
    v_stack_m2D4 = 0;
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) goto loc_0075B57A;
    v_rbx = (v_rbx) * (0);
    v_r12 = (0) << (5);
    v_r12 = (v_r12) + (*(unsigned __int64 *)(a1 + 568));
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 28)));
    if ((*(unsigned int *)(v_r12 + 28)) == 0) goto loc_0075B372;
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 16))) | (0xFFFFFFFFULL));
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12)));
    if ((*(unsigned int *)(v_r12 + 28)) != ((unsigned int)(100 - 99))) goto loc_0075B40A;
    a1 = (unsigned int)((0) + ((unsigned int)(100 - 99)));
    result = (0) * (0);
    v_stack_m2C0 = (unsigned int)(a1);
    result = (result) + (a2);
    v_stack_m2A8 = result;
    *(unsigned __int16 *)(result + 62) = 100;
    result = PpmAllocatePerfCheck(result, a2, a3, 100 - 99);
    a3 = 0;
    if (sign_flag) goto loc_0075B55E;
    *(unsigned __int64 *)(v_rbx + result + 1216 * 1) = v_stack_m2A8;
    goto loc_0075B3FF;
loc_0075B372:
    if (((unsigned int)(v_stack_m2A8)) == -1) goto loc_0075B558;
    result = KeCheckProcessorAffinityEx(v_rip + 7012521, (unsigned int)((unsigned int)(v_stack_m2A8)), a3, 100 - 99);
    if ((unsigned int)(result) != 0) goto loc_0075B558;
    result = KeGetPrcb((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m2A8)))), (unsigned int)((unsigned int)(v_stack_m2A8)), a3, 100 - 99);
    v_stack_m288 = result;
    result = (result) + (0x89B0ULL);
    v_stack_m2A8 = result;
    result = PpmAllocatePerfCheck(result, (unsigned int)((unsigned int)(v_stack_m2A8)), a3, 100 - 99);
    if (sign_flag) goto loc_0075B55E;
    result = KeAddProcessorAffinityEx(v_rsp - 504 - 96, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m2A8)))), a3, 100 - 99);
    *(unsigned __int64 *)(v_rbx + result + 1216 * 1) = v_stack_m2A8;
    a2 = (unsigned int)(*(unsigned int *)(v_rip + 8821878));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8821878)))) == -1) { a2 = *(unsigned int *)(v_rip + 8821896); }
    result = PpmConvertTimeFrom((unsigned int)(a2), (unsigned int)(0xF4240ULL), a3, 100 - 99);
    a3 = 0;
    *(unsigned __int64 *)(v_stack_m288 + 35384) = result;
loc_0075B3FF:
loc_0075B40A:
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 48) = 100;
    *(unsigned __int64 *)(v_rbx + result + 1216 * 1 + 8) = *(unsigned __int64 *)(v_r12 + 8);
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 16)));
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 20)));
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 24)));
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 84) = (unsigned int)((unsigned int)(v_stack_m2BC));
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 88) = 1;
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 56) = 100;
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 80) = 100;
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 92) = 100;
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 96) = 100;
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 132) = 100;
    *(unsigned int *)(v_rbx + result + 1216 * 1 + 136) = 100;
    *(unsigned __int64 *)(v_rbx + result + 1216 * 1 + 144) = 0;
    if ((*(unsigned __int8 *)(a1 + 7)) != 0) goto loc_0075B48B;
    result = 1;
    if ((*(unsigned __int8 *)(a1 + 11)) == 0) {
        result = 0;
    }
    *(unsigned __int8 *)(v_rbx + result + 1216 * 1 + 141) = (unsigned __int8)(result);
    if ((*(unsigned int *)(v_r12 + 16)) < 100) {
        a1 = 100;
        *(unsigned __int64 *)(v_rbx + result + 1216 * 1 + 40) = result;
        a2 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m2A8)));
        a1 = (unsigned int)((a1) - (*(unsigned int *)(v_r12 + 16)));
        result = PopDiagTraceProcessorThrottlePerfTrack(a1, a2, a3, 100 - 99);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m2D4)))) * (v_stack_m2D0));
    a4 = (result + result * 2) << (4);
    a4 = (a4) + (v_stack_m2A0);
loc_0075B4E2:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2C8)))) != -1) {
        a2 = *(unsigned __int64 *)(a1 + 560);
        a3 = (unsigned int)(*(unsigned int *)(v_stack_m2C8)) + (unsigned int)(*(unsigned int *)(v_stack_m2C8)) * 2;
        result = *(unsigned __int64 *)(a1 + 576);
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m2C8))) + ((unsigned int)((unsigned int)((unsigned int)(result)))));
        a1 = *(unsigned __int64 *)(result + a1 * 8);
        *(unsigned __int64 *)(a4 + 40) = a1;
        result = *(unsigned __int8 *)(a2 + a3 * 8 + 17);
        *(unsigned __int8 *)(a4 + 33) = (unsigned __int8)(result);
        result = *(unsigned __int8 *)(a2 + a3 * 8 + 16);
        *(unsigned __int8 *)(a4 + 32) = (unsigned __int8)(result);
        result = *(unsigned __int8 *)(a2 + a3 * 8 + 18);
        *(unsigned __int8 *)(a4 + 34) = (unsigned __int8)(result);
        result = *(unsigned int *)(a2 + a3 * 8 + 8);
        *(unsigned int *)(a4 + 36) = (unsigned int)(result);
        result = *(unsigned __int64 *)(a2 + a3 * 8);
        *(unsigned __int64 *)(a4) = result;
        a4 = (a4) + (48);
    }
    v_r10 = (v_stack_m2C8) + (4);
    v_rbx = (2) - (2 - 1);
    if (condition_is_not_equal) goto loc_0075B4E2;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m2D4)) + ((unsigned int)(2 - 1)));
    a3 = 0;
    goto loc_0075B2D8;
loc_0075B558:
loc_0075B55E:
loc_0075B563:
    result = PpmReleaseLock(v_rip + 8066710, v_stack_m2B8, a3, a4);
    goto loc_0075BC2D;
loc_0075B57A:
    result = KeIsEmptyAffinityEx(v_rsp - 504 - 96, v_stack_m2B8, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0075B5C2;
    a1 = 0;
loc_0075B589:
    if (0 >= 1) goto loc_0075B5B4;
    result = (0) * (0);
    if ((*(unsigned int *)(result + result + 1216 * 1 + 16)) == ((unsigned int)(v_stack_m2B8))) goto loc_0075B5A3;
    a1 = (unsigned int)((a1) + ((unsigned int)(v_stack_m2B8)));
    goto loc_0075B589;
loc_0075B5A3:
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(result + result + 1216 * 1);
    *(unsigned int *)(result + 304) = (unsigned int)(v_stack_m2B8);
    goto loc_0075B5F8;
loc_0075B5B4:
    if (condition_is_not_equal) goto loc_0075B5F8;
    *(unsigned int *)(result + 304) = 2;
    goto loc_0075B5F8;
loc_0075B5C2:
    result = KeFirstGroupAffinityEx(v_stack_m280, v_rsp - 504 - 96, a3, a4);
    result = KeFindFirstSetRightGroupAffinity(v_stack_m280, v_rsp - 504 - 96, a3, a4);
    result = KeGetPrcb((unsigned int)((unsigned int)(result)), v_rsp - 504 - 96, a3, a4);
    *(unsigned __int64 *)(result + 16) = result + 35248;
    *(unsigned __int8 *)(result + 300) = (unsigned __int8)(*(unsigned __int8 *)(result + 35336));
loc_0075B5F8:
    a2 = 0;
    *(unsigned int *)(result + 24) = 0x200001ULL;
    result = memset(result + 32, a2, 256, a4);
    result = KiCopyAffinityEx(result + 24, *(unsigned __int16 *)(result + 26), v_rsp - 504 - 96, a4);
    a1 = 0;
    *(unsigned __int64 *)(result + 320) = *(unsigned __int64 *)(a1 + 376);
    *(unsigned __int64 *)(result + 336) = *(unsigned __int64 *)(a1 + 392);
    *(unsigned __int64 *)(result + 344) = *(unsigned __int64 *)(a1 + 400);
    *(unsigned __int64 *)(result + 352) = *(unsigned __int64 *)(a1 + 408);
    *(unsigned __int64 *)(result + 360) = *(unsigned __int64 *)(a1 + 416);
    *(unsigned __int64 *)(result + 328) = *(unsigned __int64 *)(a1 + 384);
    *(unsigned __int64 *)(result + 288) = *(unsigned __int64 *)(a1 + 104);
    *(unsigned __int64 *)(result + 312) = result + 1216;
    *(unsigned int *)(result + 804) = 1;
    result = KeQueryPerformanceCounter(a1, *(unsigned __int16 *)(result + 26), v_rsp - 504 - 96, a4);
    v_rbx = 0;
    *(unsigned __int64 *)(result + 1200) = result;
    *(unsigned int *)(result + 448) = (unsigned int)((unsigned int)(v_stack_m2BC));
    *(unsigned int *)(result + 296) = 1;
    *(unsigned int *)(result + 464) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44)));
    *(unsigned int *)(result + 452) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
    *(unsigned int *)(result + 456) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)));
    *(unsigned int *)(result + 460) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    *(unsigned __int8 *)(result + 496) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 15));
    *(unsigned __int8 *)(result + 489) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 4));
    *(unsigned __int64 *)(result + 392) = *(unsigned __int64 *)(a1 + 464);
    *(unsigned __int64 *)(result + 400) = *(unsigned __int64 *)(a1 + 472);
    *(unsigned __int64 *)(result + 408) = *(unsigned __int64 *)(a1 + 480);
    *(unsigned __int64 *)(result + 416) = *(unsigned __int64 *)(a1 + 512);
    *(unsigned __int64 *)(result + 424) = *(unsigned __int64 *)(a1 + 520);
    *(unsigned __int64 *)(result + 432) = *(unsigned __int64 *)(a1 + 528);
    *(unsigned __int64 *)(result + 368) = *(unsigned __int64 *)(a1 + 440);
    *(unsigned __int64 *)(result + 376) = *(unsigned __int64 *)(a1 + 448);
    *(unsigned __int64 *)(result + 384) = *(unsigned __int64 *)(a1 + 456);
    *(unsigned __int8 *)(result + 521) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 52));
    result = ((*(unsigned __int8 *)(a1 + 52)) != 0) ? 1 : 0;
    *(unsigned __int8 *)(result + 520) = (unsigned __int8)(result);
    *(unsigned __int8 *)(result + 523) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 9));
loc_0075B797:
    *(unsigned int *)(result + 828 - 4) = 100;
    *(unsigned int *)(result + 828) = (unsigned int)((unsigned int)(v_stack_m2BC));
    a1 = (v_rbx + 7) - (1);
    if (condition_is_not_equal) goto loc_0075B797;
    *(unsigned __int8 *)(result + 490) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 6));
    *(unsigned __int8 *)(result + 491) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 7));
    *(unsigned __int8 *)(result + 492) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 8));
    if ((*(unsigned __int16 *)(a1 + 4)) == 253) goto loc_0075B7DC;
    result = 1;
    if ((*(unsigned __int64 *)(a1 + 480)) != 0) {
        result = 0;
    }
    *(unsigned __int8 *)(result + 494) = (unsigned __int8)(result);
    *(unsigned __int8 *)(result + 493) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 11));
    result = *(unsigned __int8 *)(a1 + 11);
    if ((*(unsigned int *)(v_rip + 8820924)) == -1) {
        result = 0;
        result = ((*(unsigned __int8 *)(a1 + 12)) != 0) ? 1 : 0;
        *(unsigned int *)(v_rip + 8820908) = (unsigned int)(result);
    }
    *(unsigned __int64 *)(result + 472) = *(unsigned __int64 *)(a1 + 56);
    *(unsigned __int64 *)(result + 480) = *(unsigned __int64 *)(a1 + 64);
    *(unsigned __int8 *)(result + 488) = 100;
    if ((*(unsigned __int64 *)(v_rip + 8059429)) <= ((unsigned int)(*(unsigned int *)(a1 + 40)))) {
        *(unsigned __int64 *)(v_rip + 8059420) = (unsigned int)(*(unsigned int *)(a1 + 40));
    }
    if ((*(unsigned __int64 *)(result + 344)) != 0) {
    }
    result = (unsigned int)(*(unsigned int *)(a1 + 40));
    if ((*(unsigned __int64 *)(result + 336)) != 0) {
        result = 32;
    }
    if ((*(unsigned __int64 *)(result + 328)) != 0) {
    }
    if ((*(unsigned __int64 *)(result + 360)) != 0) {
    }
    if ((*(unsigned __int64 *)(result + 352)) != 0) {
    }
    if ((*(unsigned __int8 *)(a1 + 9)) != 0) {
        *(unsigned __int8 *)(v_rip + 8827488) = 1;
    }
    if ((*(unsigned __int8 *)(a1 + 10)) != 0) {
        *(unsigned __int8 *)(v_rip + 8827480) = 1;
    }
    *(unsigned __int8 *)(result + 495) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 13));
    *(unsigned int *)(result + 500) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 72)));
    *(unsigned int *)(result + 504) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 76)));
    *(unsigned int *)(result + 508) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 80)));
    *(unsigned int *)(result + 512) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 84)));
    *(unsigned int *)(result + 516) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 88)));
    if (1 == 0) goto loc_0075B9C3;
loc_0075B8ED:
    if ((*(unsigned int *)(result + 1216 + 16)) == 2) goto loc_0075B9AA;
    a1 = (a1) * (0);
    v_stack_m298 = v_xmm0;
    *(unsigned int *)(*(unsigned __int64 *)(result + 1216 + 16 - 16) + 64) = 0x10000ULL;
    result = (unsigned int)((0) * (v_stack_m2D0));
    a1 = (a1) + (result + 1216);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1216 + 16 - 16)) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1216 + 16 - 16) + 8) = a1;
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (v_stack_m2A0);
loc_0075B943:
    if ((*(unsigned int *)(v_stack_m2C8)) != -1) {
        *(unsigned __int64 *)(v_stack_m298) = a1;
        a1 = (a1) + (48);
    }
    a2 = (v_stack_m2C8) + (4);
    result = (v_stack_m298) + (8);
    a3 = (2) - (1);
    if (condition_is_not_equal) goto loc_0075B943;
    if ((*(unsigned int *)(result + 1216 + 16)) == ((unsigned int)(a3))) goto loc_0075B995;
    result = PpmPerfResizeHistory(*(unsigned __int64 *)(result + 1216 + 16 - 16), a2, a3, a4);
    v_rbx = (*(unsigned __int64 *)(result + 1216 + 16 - 16)) - (v_stack_m298);
loc_0075B97C:
    if (*(unsigned __int64 *)(v_stack_m298) != 0) {
        *(unsigned __int64 *)(v_rbx + v_stack_m298 * 1 + 96) = *(unsigned __int64 *)(v_stack_m298);
    }
    result = (v_stack_m298) + (8);
    a2 = (2) - (1);
    if (condition_is_not_equal) goto loc_0075B97C;
    goto loc_0075B9AA;
loc_0075B995:
    result = PpmInstallFeedbackCounters(v_rbx - 35248, v_stack_m298, *(unsigned __int8 *)(a1 + 14), a4);
loc_0075B9AA:
    v_r12 = (unsigned int)((0) + 1);
    v_r15 = (result + 1216 + 16) + (0x4A8ULL);
    if (((unsigned int)(v_r12)) < 1) goto loc_0075B8ED;
    v_rbx = 0;
loc_0075B9C3:
    if ((*(unsigned __int64 *)(v_rip + 8071318)) == 0) {
        result = *(unsigned __int64 *)(a1 + 96);
        *(unsigned __int64 *)(v_rip + 8071305) = result;
    }
    if (*(unsigned __int64 *)(v_rip + 8071290) == 0) {
        a1 = *(unsigned __int64 *)(a1 + 488);
        *(unsigned __int64 *)(v_rip + 8071271) = a1;
    }
    if ((*(unsigned __int64 *)(v_rip + 8071288)) == 0) {
        result = *(unsigned __int64 *)(a1 + 496);
        *(unsigned __int64 *)(v_rip + 8071272) = result;
    }
    if ((*(unsigned __int64 *)(v_rip + 8071257)) == 0) {
        result = *(unsigned __int64 *)(a1 + 504);
        *(unsigned __int64 *)(v_rip + 8071241) = result;
    }
    if ((*(unsigned __int64 *)(v_rip + 8071258)) == 0) {
        result = *(unsigned __int64 *)(a1 + 536);
        *(unsigned __int64 *)(v_rip + 8071242) = result;
    }
    if ((*(unsigned __int64 *)(v_rip + 8071227)) == 0) {
        result = *(unsigned __int64 *)(a1 + 544);
        *(unsigned __int64 *)(v_rip + 8071211) = result;
    }
    if ((*(unsigned __int64 *)(v_rip + 8071228)) == 0) {
        result = *(unsigned __int64 *)(a1 + 552);
        *(unsigned __int64 *)(v_rip + 8071212) = result;
    }
    if ((*(unsigned __int64 *)(v_rip + 8071197)) == 0) {
        result = *(unsigned __int64 *)(a1 + 424);
        *(unsigned __int64 *)(v_rip + 8071181) = result;
    }
    if ((*(unsigned __int64 *)(v_rip + 8071190)) == 0) {
        result = *(unsigned __int64 *)(a1 + 432);
        *(unsigned __int64 *)(v_rip + 8071174) = result;
    }
    if (a1 != 0) {
        *(unsigned __int8 *)(v_rip + 8058810) = (unsigned __int8)(v_rbx + 1);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 8827468))) + ((unsigned int)(v_rbx + 1)));
    *(unsigned int *)(result + 440) = (unsigned int)(result);
    *(unsigned int *)(v_rip + 8827446) = (unsigned int)(result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8827119))) != (v_rip + 8827133)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(result) = v_rip + 8827133;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_rip + 8827119);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8827119)) = result;
    *(unsigned __int64 *)(v_rip + 8827080) = result;
    v_stack_m2D8 = (unsigned __int8)(v_rbx + 1);
    if ((*(unsigned __int64 *)(v_rip + 8827079)) == (v_rip + 8827133)) goto loc_0075BB0C;
loc_0075BAF2:
    result = (unsigned __int8)(-(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 8827079) + 493)));
    a3 = (unsigned __int8)(((unsigned __int8)(v_rbx + 1)) & ((unsigned __int8)(a1)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8827079))) != (v_rip + 8827133)) goto loc_0075BAF2;
    v_stack_m2D8 = (unsigned __int8)(a3);
loc_0075BB0C:
    result = KiOrAffinityEx(v_rsp - 504 - 96, v_rip + 7010581, v_rip + 7010581, *(unsigned __int16 *)(v_rip + 7010590));
    result = KeIsEqualAffinityEx(v_rip + 7010581, v_rip + 7010930, v_rip + 7010581, *(unsigned __int16 *)(v_rip + 7010590));
    if ((unsigned int)(result) == 0) goto loc_0075BBDB;
loc_0075BB48:
    if ((*(unsigned __int64 *)(v_rip + 8826979)) == (v_rip + 8827133)) goto loc_0075BBD5;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 8826979) + 495)) == 0) goto loc_0075BBD3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8826979) + 480)) != (*(unsigned __int64 *)(result + 480))) goto loc_0075BBD3;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8826979) + 460)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 460))))) goto loc_0075BBD3;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8826979) + 452)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 452))))) goto loc_0075BBD3;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8826979) + 500)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 500))))) goto loc_0075BBD3;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8826979) + 504)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 504))))) goto loc_0075BBD3;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8826979) + 508)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 508))))) goto loc_0075BBD3;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8826979) + 512)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 512))))) goto loc_0075BBD3;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8826979) + 516)) != ((unsigned int)((unsigned int)(*(unsigned int *)(result + 516))))) goto loc_0075BBD3;
    goto loc_0075BB48;
loc_0075BBD3:
loc_0075BBD5:
    *(unsigned __int8 *)(v_rip + 8826641) = 0;
loc_0075BBDB:
    *(unsigned __int16 *)(result + 1212) = 257;
    result = PpmUpdateProcessorPolicy(v_rip + 8070546, result, v_rip + 7010581, *(unsigned __int16 *)(v_rip + 7010590));
    result = PpmCheckResetProcessors(result, result, v_rip + 7010581, *(unsigned __int16 *)(v_rip + 7010590));
    a2 = 0;
    result = KeCheckProcessorAffinityEx(v_rsp - 504 - 96, a2, v_rip + 7010581, *(unsigned __int16 *)(v_rip + 7010590));
    if ((unsigned int)(result) != 0) {
        result = PpmParkApplyPolicy(v_rsp - 504 - 96, a2, v_rip + 7010581, *(unsigned __int16 *)(v_rip + 7010590));
    }
    result = PpmCheckReInit(v_rsp - 504 - 96, a2, v_rip + 7010581, *(unsigned __int16 *)(v_rip + 7010590));
    result = PpmPerfUpdateDomainPolicy(1, a2, v_rip + 7010581, *(unsigned __int16 *)(v_rip + 7010590));
loc_0075BC2D:
    v_r14 = 0;
    if ((*(unsigned int *)(v_rip + 8827061)) > 1) goto loc_0075BC41;
    if ((unsigned __int8)(v_stack_m2D8) == 0) goto loc_0075BC75;
loc_0075BC41:
    result = KeIsEqualAffinityEx(v_rip + 7010273, v_rip + 7010648, v_rip + 7010581, *(unsigned __int16 *)(v_rip + 7010590));
    if ((unsigned int)(result) != 0) {
        a1 = v_rip + 8064929;
        result = PpmAcquireLock(a1, v_rip + 7010648, v_rip + 7010581, *(unsigned __int16 *)(v_rip + 7010590));
        a3 = 0;
        *(unsigned __int8 *)(v_rip + 8826479) = (unsigned __int8)(v_stack_m2D8);
        a1 = 1;
        result = PpmReinitializeHeteroEngine(a1, v_rip + 7010648, a3, *(unsigned __int16 *)(v_rip + 7010590));
    }
    if (0 == 0) goto loc_0075BD24;
    if ((unsigned int)((unsigned int)(v_stack_m2CC)) == 0) goto loc_0075BD17;
loc_0075BC91:
    if (*(unsigned __int64 *)(v_stack_m2B8 + 16) == 0) goto loc_0075BD07;
    result = *(unsigned __int64 *)(v_stack_m2B8 + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2B8 + 16) + 88) != 0) {
        a2 = (unsigned int)((unsigned int)(0x704D5050ULL));
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2B8 + 16) + 88), a2, a3, *(unsigned __int16 *)(v_rip + 7010590));
        result = *(unsigned __int64 *)(v_stack_m2B8 + 16);
        *(unsigned __int64 *)(result + 88) = 0;
    }
    result = *(unsigned __int64 *)(v_stack_m2B8 + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2B8 + 16) + 152) != 0) {
        a2 = (unsigned int)((unsigned int)(0x704D5050ULL));
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2B8 + 16) + 152), a2, a3, *(unsigned __int16 *)(v_rip + 7010590));
        result = *(unsigned __int64 *)(v_stack_m2B8 + 16);
        *(unsigned __int64 *)(result + 152) = 0;
    }
    result = *(unsigned __int64 *)(v_stack_m2B8 + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2B8 + 16) + 216) != 0) {
        a2 = (unsigned int)((unsigned int)(0x704D5050ULL));
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2B8 + 16) + 216), a2, a3, *(unsigned __int16 *)(v_rip + 7010590));
        result = *(unsigned __int64 *)(v_stack_m2B8 + 16);
        *(unsigned __int64 *)(result + 216) = 0;
    }
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m2B8 + 16), (unsigned int)((unsigned int)((unsigned int)(0x704D5050ULL))), a3, *(unsigned __int16 *)(v_rip + 7010590));
    *(unsigned __int64 *)(v_stack_m2B8 + 16) = 0;
loc_0075BD07:
    v_rbx = (v_stack_m2B8 + 16) + (784);
    v_rsi = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m2CC)))) - (1);
    if (condition_is_not_equal) goto loc_0075BC91;
loc_0075BD17:
    result = ExFreePoolWithTag(0, (unsigned int)(0x704D5050ULL), a3, *(unsigned __int16 *)(v_rip + 7010590));
loc_0075BD24:
    result = KeSetTimer2(v_rip + 8070242, (unsigned int)(0x704D5050ULL), a3, v_rsp - 504 - 120);
    a1 = (*(unsigned __int64 *)(v_rsp - 504 + 448)) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x704D5050ULL), a3, v_rsp - 504 - 120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmRegisterPerfStates(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint32_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint32_t v_stack_m2BC;
    uint32_t v_stack_m2C0;
    uint32_t v_stack_m2C4;
    uint64_t v_stack_m2C8;
    uint32_t v_stack_m2CC;
    uint32_t v_stack_m2D0;
    uint32_t v_stack_m2D4;
    uint8_t v_stack_m2D8;
    uint32_t v_stack_m2F8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (720);
    result = (*(uint64_t *)(v_rip + 0x6AF68F)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x1F8 + 0x1C0) = result;
    Arg2 = 0;
    result = memset(local_rsp - 504 + 184, Arg2, 256, a4);
    Arg2 = 0;
    v_stack_m280 = v_xmm0;
    result = memset(local_rsp - 504 - 88, Arg2, 256, a4);
    local_r15 = 0;
    v_stack_m2B0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    Arg2 = 0;
    v_stack_m2D8 = 0;
    v_stack_m2BC = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)));
    v_stack_m298 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x1F8 - 0x60) = 0x200001ULL;
    *(uint64_t *)(local_rsp - 0x1F8 - 0x78) = v_xmm1;
    result = memset(local_rsp - 504 - 88, Arg2, 256, a4);
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x1F8 + 0xB0) = 0x200001ULL;
    result = memset(local_rsp - 504 + 184, Arg2, 256, a4);
    result = KeQueryActiveProcessorAffinity2(local_rsp - 504 + 176, Arg2, 256, a4);
    v_stack_m2CC = 0;
    if ((uint8_t)((uint8_t)(Arg2)) == 0) {
        Arg1 = v_rip + 8067722;
        result = PpmAcquireLock(Arg1, Arg2, 256, 0);
        a4 = 0;
    }
    local_rbx = 0;
    local_r15 = (uint32_t)((local_r15) | (0xFFFFFFFFULL));
loc_0075B190:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x24))))) goto loc_0075B1C9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x230) + 0x0 + 0x0 * 2 * 8 + 0xC)))) >= 2) goto loc_0075B1BE;
    if ((*(uint32_t *)(local_rsp + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x230) + 0x0 + 0x0 * 2 * 8 + 0xC)) * 4 + 0x30)) == ((uint32_t)(local_r15))) {
        *(uint32_t *)(local_rsp + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x230) + 0x0 + 0x0 * 2 * 8 + 0xC)) * 4 + 0x30) = 0;
    }
    Arg2 = (uint32_t)((0) + ((uint32_t)(local_rbx + 1)));
    goto loc_0075B190;
loc_0075B1BE:
    goto loc_0075B563;
loc_0075B1C9:
    if (v_stack_m2C8 != ((uint32_t)((uint32_t)(0xC000000DULL)))) goto loc_0075B1D7;
    if (v_stack_m2C4 == ((uint32_t)((uint32_t)(0xC000000DULL)))) goto loc_0075B1BE;
loc_0075B1D7:
loc_0075B1E5:
    Arg1 = 0 + 1;
    if ((*(uint32_t *)(v_stack_m2C8)) == ((uint32_t)((uint32_t)(0xC000000DULL)))) { Arg1 = 0; }
    a3 = (2) - (local_rbx + 1);
    if (condition_is_not_equal) goto loc_0075B1E5;
    v_stack_m2D0 = (uint32_t)(Arg1);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))) == 0) goto loc_0075B238;
    Arg2 = (*(uint64_t *)(arg1 + 0x238)) + (28);
loc_0075B219:
    Arg1 = a4 + 1;
    if ((*(uint32_t *)(Arg2)) != ((uint32_t)(local_rbx + 1))) { Arg1 = (uint32_t)(a4); }
    Arg2 = (Arg2) + (32);
    a3 = ((uint32_t)(*(uint32_t *)(arg1 + 0x10))) - (local_rbx + 1);
    if (condition_is_not_equal) goto loc_0075B219;
    v_stack_m2CC = (uint32_t)(Arg1);
loc_0075B238:
    local_rbx = (uint32_t)((local_rbx) * ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) * ((uint32_t)((uint32_t)(v_stack_m2D0))));
    Arg1 = 0;
    local_rbx = (uint32_t)((local_rbx) + (0x4C7ULL));
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFF8ULL));
    local_r15 = (uint32_t)((result + result * 2) << (4));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(local_rbx)));
    result = (uint32_t)((uint32_t)(local_r15));
    if ((uint32_t)((uint32_t)((uint32_t)(Arg1))) != 0) {
        result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) * ((uint32_t)((uint32_t)((uint32_t)(Arg1)))));
        result = (uint32_t)((result) + ((uint32_t)(local_r15)));
    }
    if ((uint32_t)((uint32_t)((uint32_t)(Arg1))) == 0) { local_r15 = 0; }
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)(result)), (uint32_t)(0x704D5050ULL), (uint32_t)((uint32_t)(Arg1)));
    a3 = 0;
    if (result != 0) goto loc_0075B29D;
    goto loc_0075B563;
loc_0075B29D:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)))) + (result);
    result = ((uint32_t)((uint32_t)(local_rbx))) + (result);
    v_stack_m2B8 = Arg2;
    v_stack_m2A0 = result;
    v_stack_m2C0 = 0;
    if ((*(uint8_t *)(arg1 + 0xB)) != 0) {
        result = *(uint32_t *)(arg1 + 0x30);
        *(uint32_t *)(v_rip + 0x869D9D) = (uint32_t)(result);
    }
loc_0075B2D8:
    v_stack_m2D4 = 0;
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) goto loc_0075B57A;
    local_rbx = (local_rbx) * (0);
    local_r12 = (0) << (5);
    local_r12 = (local_r12) + (*(uint64_t *)(arg1 + 0x238));
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x1C)));
    if ((*(uint32_t *)(local_r12 + 0x1C)) == 0) goto loc_0075B372;
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x10))) | (0xFFFFFFFFULL));
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12)));
    if ((*(uint32_t *)(local_r12 + 0x1C)) != ((uint32_t)(100 - 99))) goto loc_0075B40A;
    Arg1 = (uint32_t)((0) + ((uint32_t)(100 - 99)));
    result = (0) * (0);
    v_stack_m2C0 = (uint32_t)(Arg1);
    result = (result) + (Arg2);
    v_stack_m2A8 = result;
    *(uint16_t *)(result + 0x3E) = 100;
    result = PpmAllocatePerfCheck(result, Arg2, a3, 100 - 99);
    a3 = 0;
    if (sign_flag) goto loc_0075B55E;
    *(uint64_t *)(local_rbx + result + 0x4C0 * 1) = v_stack_m2A8;
    goto loc_0075B3FF;
loc_0075B372:
    if (((uint32_t)(v_stack_m2A8)) == -1) goto loc_0075B558;
    result = KeCheckProcessorAffinityEx(v_rip + 7012521, (uint32_t)((uint32_t)(v_stack_m2A8)), a3, 100 - 99);
    if ((uint32_t)(result) != 0) goto loc_0075B558;
    result = KeGetPrcb((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m2A8)))), (uint32_t)((uint32_t)(v_stack_m2A8)), a3, 100 - 99);
    v_stack_m288 = result;
    result = (result) + (0x89B0ULL);
    v_stack_m2A8 = result;
    result = PpmAllocatePerfCheck(result, (uint32_t)((uint32_t)(v_stack_m2A8)), a3, 100 - 99);
    if (sign_flag) goto loc_0075B55E;
    result = KeAddProcessorAffinityEx(local_rsp - 504 - 96, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m2A8)))), a3, 100 - 99);
    *(uint64_t *)(local_rbx + result + 0x4C0 * 1) = v_stack_m2A8;
    Arg2 = (uint32_t)(*(uint32_t *)(v_rip + 0x869C76));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x869C76)))) == -1) { Arg2 = *(uint32_t *)(v_rip + 0x869C88); }
    result = PpmConvertTimeFrom((uint32_t)(Arg2), (uint32_t)(0xF4240ULL), a3, 100 - 99);
    a3 = 0;
    *(uint64_t *)(v_stack_m288 + 0x8A38) = result;
loc_0075B3FF:
loc_0075B40A:
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x30) = 100;
    *(uint64_t *)(local_rbx + result + 0x4C0 * 1 + 0x8) = *(uint64_t *)(local_r12 + 0x8);
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x10)));
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x14)));
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x18)));
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x54) = (uint32_t)((uint32_t)(v_stack_m2BC));
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x58) = 1;
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x38) = 100;
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x50) = 100;
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x5C) = 100;
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x60) = 100;
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x84) = 100;
    *(uint32_t *)(local_rbx + result + 0x4C0 * 1 + 0x88) = 100;
    *(uint64_t *)(local_rbx + result + 0x4C0 * 1 + 0x90) = 0;
    if ((*(uint8_t *)(arg1 + 0x7)) != 0) goto loc_0075B48B;
    result = 1;
    if ((*(uint8_t *)(arg1 + 0xB)) == 0) {
        result = 0;
    }
    *(uint8_t *)(local_rbx + result + 0x4C0 * 1 + 0x8D) = (uint8_t)(result);
    if ((*(uint32_t *)(local_r12 + 0x10)) < 100) {
        Arg1 = 100;
        *(uint64_t *)(local_rbx + result + 0x4C0 * 1 + 0x28) = result;
        Arg2 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m2A8)));
        Arg1 = (uint32_t)((Arg1) - (*(uint32_t *)(local_r12 + 0x10)));
        result = PopDiagTraceProcessorThrottlePerfTrack(Arg1, Arg2, a3, 100 - 99);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m2D4)))) * (v_stack_m2D0));
    a4 = (result + result * 2) << (4);
    a4 = (a4) + (v_stack_m2A0);
loc_0075B4E2:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2C8)))) != -1) {
        Arg2 = *(uint64_t *)(arg1 + 0x230);
        a3 = (uint32_t)(*(uint32_t *)(v_stack_m2C8)) + (uint32_t)(*(uint32_t *)(v_stack_m2C8)) * 2;
        result = *(uint64_t *)(arg1 + 0x240);
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m2C8))) + ((uint32_t)((uint32_t)((uint32_t)(result)))));
        Arg1 = *(uint64_t *)(result + arg1 * 8);
        *(void **)(a4 + 0x28) = Arg1;
        result = *(uint8_t *)(Arg2 + a3 * 8 + 0x11);
        *(uint8_t *)(a4 + 0x21) = (uint8_t)(result);
        result = *(uint8_t *)(Arg2 + a3 * 8 + 0x10);
        *(uint8_t *)(a4 + 0x20) = (uint8_t)(result);
        result = *(uint8_t *)(Arg2 + a3 * 8 + 0x12);
        *(uint8_t *)(a4 + 0x22) = (uint8_t)(result);
        result = *(uint32_t *)(Arg2 + a3 * 8 + 0x8);
        *(uint32_t *)(a4 + 0x24) = (uint32_t)(result);
        result = *(uint64_t *)(Arg2 + a3 * 8);
        *(uint64_t *)(a4) = result;
        a4 = (a4) + (48);
    }
    local_r10 = (v_stack_m2C8) + (4);
    local_rbx = (2) - (2 - 1);
    if (condition_is_not_equal) goto loc_0075B4E2;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m2D4)) + ((uint32_t)(2 - 1)));
    a3 = 0;
    goto loc_0075B2D8;
loc_0075B558:
loc_0075B55E:
loc_0075B563:
    result = PpmReleaseLock(v_rip + 8066710, v_stack_m2B8, a3, a4);
    goto loc_0075BC2D;
loc_0075B57A:
    result = KeIsEmptyAffinityEx(local_rsp - 504 - 96, v_stack_m2B8, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_0075B5C2;
    Arg1 = 0;
loc_0075B589:
    if (0 >= 1) goto loc_0075B5B4;
    result = (0) * (0);
    if ((*(uint32_t *)(result + result + 0x4C0 * 1 + 0x10)) == ((uint32_t)(v_stack_m2B8))) goto loc_0075B5A3;
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(v_stack_m2B8)));
    goto loc_0075B589;
loc_0075B5A3:
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(result + result + 0x4C0 * 1);
    *(uint32_t *)(result + 0x130) = (uint32_t)(v_stack_m2B8);
    goto loc_0075B5F8;
loc_0075B5B4:
    if (condition_is_not_equal) goto loc_0075B5F8;
    *(uint32_t *)(result + 0x130) = 2;
    goto loc_0075B5F8;
loc_0075B5C2:
    result = KeFirstGroupAffinityEx(v_stack_m280, local_rsp - 504 - 96, a3, a4);
    result = KeFindFirstSetRightGroupAffinity(v_stack_m280, local_rsp - 504 - 96, a3, a4);
    result = KeGetPrcb((uint32_t)((uint32_t)(result)), local_rsp - 504 - 96, a3, a4);
    *(uint64_t *)(result + 0x10) = result + 35248;
    *(uint8_t *)(result + 0x12C) = (uint8_t)(*(uint8_t *)(result + 0x8A08));
loc_0075B5F8:
    Arg2 = 0;
    *(uint32_t *)(result + 0x18) = 0x200001ULL;
    result = memset(result + 32, Arg2, 256, a4);
    result = KiCopyAffinityEx(result + 24, *(uint16_t *)(result + 0x1A), local_rsp - 504 - 96, a4);
    Arg1 = 0;
    *(uint64_t *)(result + 0x140) = *(uint64_t *)(arg1 + 0x178);
    *(uint64_t *)(result + 0x150) = *(uint64_t *)(arg1 + 0x188);
    *(uint64_t *)(result + 0x158) = *(uint64_t *)(arg1 + 0x190);
    *(uint64_t *)(result + 0x160) = *(uint64_t *)(arg1 + 0x198);
    *(uint64_t *)(result + 0x168) = *(uint64_t *)(arg1 + 0x1A0);
    *(uint64_t *)(result + 0x148) = *(uint64_t *)(arg1 + 0x180);
    *(uint64_t *)(result + 0x120) = *(uint64_t *)(arg1 + 0x68);
    *(uint64_t *)(result + 0x138) = result + 1216;
    *(uint32_t *)(result + 0x324) = 1;
    result = KeQueryPerformanceCounter(Arg1, *(uint16_t *)(result + 0x1A), local_rsp - 504 - 96, a4);
    local_rbx = 0;
    *(uint64_t *)(result + 0x4B0) = result;
    *(uint32_t *)(result + 0x1C0) = (uint32_t)((uint32_t)(v_stack_m2BC));
    *(uint32_t *)(result + 0x128) = 1;
    *(uint32_t *)(result + 0x1D0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C)));
    *(uint32_t *)(result + 0x1C4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    *(uint32_t *)(result + 0x1C8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    *(uint32_t *)(result + 0x1CC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    *(uint8_t *)(result + 0x1F0) = (uint8_t)(*(uint8_t *)(arg1 + 0xF));
    *(uint8_t *)(result + 0x1E9) = (uint8_t)(*(uint8_t *)(arg1 + 0x4));
    *(uint64_t *)(result + 0x188) = *(uint64_t *)(arg1 + 0x1D0);
    *(uint64_t *)(result + 0x190) = *(uint64_t *)(arg1 + 0x1D8);
    *(uint64_t *)(result + 0x198) = *(uint64_t *)(arg1 + 0x1E0);
    *(uint64_t *)(result + 0x1A0) = *(uint64_t *)(arg1 + 0x200);
    *(uint64_t *)(result + 0x1A8) = *(uint64_t *)(arg1 + 0x208);
    *(uint64_t *)(result + 0x1B0) = *(uint64_t *)(arg1 + 0x210);
    *(uint64_t *)(result + 0x170) = *(uint64_t *)(arg1 + 0x1B8);
    *(uint64_t *)(result + 0x178) = *(uint64_t *)(arg1 + 0x1C0);
    *(uint64_t *)(result + 0x180) = *(uint64_t *)(arg1 + 0x1C8);
    *(uint8_t *)(result + 0x209) = (uint8_t)(*(uint8_t *)(arg1 + 0x34));
    result = ((*(uint8_t *)(arg1 + 0x34)) != 0) ? 1 : 0;
    *(uint8_t *)(result + 0x208) = (uint8_t)(result);
    *(uint8_t *)(result + 0x20B) = (uint8_t)(*(uint8_t *)(arg1 + 0x9));
loc_0075B797:
    *(uint32_t *)(result + 0x33C - 0x4) = 100;
    *(uint32_t *)(result + 0x33C) = (uint32_t)((uint32_t)(v_stack_m2BC));
    Arg1 = (local_rbx + 7) - (1);
    if (condition_is_not_equal) goto loc_0075B797;
    *(uint8_t *)(result + 0x1EA) = (uint8_t)(*(uint8_t *)(arg1 + 0x6));
    *(uint8_t *)(result + 0x1EB) = (uint8_t)(*(uint8_t *)(arg1 + 0x7));
    *(uint8_t *)(result + 0x1EC) = (uint8_t)(*(uint8_t *)(arg1 + 0x8));
    if ((*(uint16_t *)(arg1 + 0x4)) == 253) goto loc_0075B7DC;
    result = 1;
    if ((*(uint64_t *)(arg1 + 0x1E0)) != 0) {
        result = 0;
    }
    *(uint8_t *)(result + 0x1EE) = (uint8_t)(result);
    *(uint8_t *)(result + 0x1ED) = (uint8_t)(*(uint8_t *)(arg1 + 0xB));
    result = *(uint8_t *)(arg1 + 0xB);
    if ((*(uint32_t *)(v_rip + 0x8698BC)) == -1) {
        result = 0;
        result = ((*(uint8_t *)(arg1 + 0xC)) != 0) ? 1 : 0;
        *(uint32_t *)(v_rip + 0x8698AC) = (uint32_t)(result);
    }
    *(uint64_t *)(result + 0x1D8) = *(uint64_t *)(arg1 + 0x38);
    *(uint64_t *)(result + 0x1E0) = *(uint64_t *)(arg1 + 0x40);
    *(uint8_t *)(result + 0x1E8) = 100;
    if ((*(uint64_t *)(v_rip + 0x7AFA25)) <= ((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) {
        *(uint64_t *)(v_rip + 0x7AFA1C) = (uint32_t)(*(uint32_t *)(arg1 + 0x28));
    }
    if ((*(uint64_t *)(result + 0x158)) != 0) {
    }
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x28));
    if ((*(uint64_t *)(result + 0x150)) != 0) {
        result = 32;
    }
    if ((*(uint64_t *)(result + 0x148)) != 0) {
    }
    if ((*(uint64_t *)(result + 0x168)) != 0) {
    }
    if ((*(uint64_t *)(result + 0x160)) != 0) {
    }
    if ((*(uint8_t *)(arg1 + 0x9)) != 0) {
        *(uint8_t *)(v_rip + 0x86B260) = 1;
    }
    if ((*(uint8_t *)(arg1 + 0xA)) != 0) {
        *(uint8_t *)(v_rip + 0x86B258) = 1;
    }
    *(uint8_t *)(result + 0x1EF) = (uint8_t)(*(uint8_t *)(arg1 + 0xD));
    *(uint32_t *)(result + 0x1F4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x48)));
    *(uint32_t *)(result + 0x1F8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4C)));
    *(uint32_t *)(result + 0x1FC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)));
    *(uint32_t *)(result + 0x200) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x54)));
    *(uint32_t *)(result + 0x204) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x58)));
    if (1 == 0) goto loc_0075B9C3;
loc_0075B8ED:
    if ((*(uint32_t *)(result + 0x4C0 + 0x10)) == 2) goto loc_0075B9AA;
    Arg1 = (Arg1) * (0);
    v_stack_m298 = v_xmm0;
    *(uint32_t *)(*(uint64_t *)(result + 0x4C0 + 0x10 - 0x10) + 0x40) = 0x10000ULL;
    result = (uint32_t)((0) * (v_stack_m2D0));
    Arg1 = (Arg1) + (result + 1216);
    *(uint64_t *)(*(uint64_t *)(result + 0x4C0 + 0x10 - 0x10)) = result;
    *(void **)(*(uint64_t *)(result + 0x4C0 + 0x10 - 0x10) + 0x8) = Arg1;
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (v_stack_m2A0);
loc_0075B943:
    if ((*(uint32_t *)(v_stack_m2C8)) != -1) {
        *(void **)(v_stack_m298) = Arg1;
        Arg1 = (Arg1) + (48);
    }
    Arg2 = (v_stack_m2C8) + (4);
    result = (v_stack_m298) + (8);
    a3 = (2) - (1);
    if (condition_is_not_equal) goto loc_0075B943;
    if ((*(uint32_t *)(result + 0x4C0 + 0x10)) == ((uint32_t)(a3))) goto loc_0075B995;
    result = PpmPerfResizeHistory(*(uint64_t *)(result + 0x4C0 + 0x10 - 0x10), Arg2, a3, a4);
    local_rbx = (*(uint64_t *)(result + 0x4C0 + 0x10 - 0x10)) - (v_stack_m298);
loc_0075B97C:
    if (*(uint64_t *)(v_stack_m298) != 0) {
        *(uint64_t *)(local_rbx + v_stack_m298 * 1 + 0x60) = *(uint64_t *)(v_stack_m298);
    }
    result = (v_stack_m298) + (8);
    Arg2 = (2) - (1);
    if (condition_is_not_equal) goto loc_0075B97C;
    goto loc_0075B9AA;
loc_0075B995:
    result = PpmInstallFeedbackCounters(local_rbx - 35248, v_stack_m298, *(uint8_t *)(arg1 + 0xE), a4);
loc_0075B9AA:
    local_r12 = (uint32_t)((0) + 1);
    local_r15 = (result + 1216 + 16) + (0x4A8ULL);
    if (((uint32_t)(local_r12)) < 1) goto loc_0075B8ED;
    local_rbx = 0;
loc_0075B9C3:
    if ((*(uint64_t *)(v_rip + 0x7B2896)) == 0) {
        result = *(uint64_t *)(arg1 + 0x60);
        *(uint64_t *)(v_rip + 0x7B2889) = result;
    }
    if (*(uint64_t *)(v_rip + 0x7B287A) == 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x1E8);
        *(void **)(v_rip + 0x7B2867) = Arg1;
    }
    if ((*(uint64_t *)(v_rip + 0x7B2878)) == 0) {
        result = *(uint64_t *)(arg1 + 0x1F0);
        *(uint64_t *)(v_rip + 0x7B2868) = result;
    }
    if ((*(uint64_t *)(v_rip + 0x7B2859)) == 0) {
        result = *(uint64_t *)(arg1 + 0x1F8);
        *(uint64_t *)(v_rip + 0x7B2849) = result;
    }
    if ((*(uint64_t *)(v_rip + 0x7B285A)) == 0) {
        result = *(uint64_t *)(arg1 + 0x218);
        *(uint64_t *)(v_rip + 0x7B284A) = result;
    }
    if ((*(uint64_t *)(v_rip + 0x7B283B)) == 0) {
        result = *(uint64_t *)(arg1 + 0x220);
        *(uint64_t *)(v_rip + 0x7B282B) = result;
    }
    if ((*(uint64_t *)(v_rip + 0x7B283C)) == 0) {
        result = *(uint64_t *)(arg1 + 0x228);
        *(uint64_t *)(v_rip + 0x7B282C) = result;
    }
    if ((*(uint64_t *)(v_rip + 0x7B281D)) == 0) {
        result = *(uint64_t *)(arg1 + 0x1A8);
        *(uint64_t *)(v_rip + 0x7B280D) = result;
    }
    if ((*(uint64_t *)(v_rip + 0x7B2816)) == 0) {
        result = *(uint64_t *)(arg1 + 0x1B0);
        *(uint64_t *)(v_rip + 0x7B2806) = result;
    }
    if (Arg1 != NULL) {
        *(uint8_t *)(v_rip + 0x7AF7BA) = (uint8_t)(local_rbx + 1);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x86B24C))) + ((uint32_t)(local_rbx + 1)));
    *(uint32_t *)(result + 0x1B8) = (uint32_t)(result);
    *(uint32_t *)(v_rip + 0x86B236) = (uint32_t)(result);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x86B0EF))) != (v_rip + 8827133)) {
        Arg1 = 3;
    }
    *(uint64_t *)(result) = v_rip + 8827133;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(v_rip + 0x86B0EF);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x86B0EF)) = result;
    *(uint64_t *)(v_rip + 0x86B0C8) = result;
    v_stack_m2D8 = (uint8_t)(local_rbx + 1);
    if ((*(uint64_t *)(v_rip + 0x86B0C7)) == (v_rip + 8827133)) goto loc_0075BB0C;
loc_0075BAF2:
    result = (uint8_t)(-(*(uint8_t *)(*(uint64_t *)(v_rip + 0x86B0C7) + 0x1ED)));
    a3 = (uint8_t)(((uint8_t)(local_rbx + 1)) & ((uint8_t)(Arg1)));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x86B0C7))) != (v_rip + 8827133)) goto loc_0075BAF2;
    v_stack_m2D8 = (uint8_t)(a3);
loc_0075BB0C:
    result = KiOrAffinityEx(local_rsp - 504 - 96, v_rip + 7010581, v_rip + 7010581, *(uint16_t *)(v_rip + 0x6AF91E));
    result = KeIsEqualAffinityEx(v_rip + 7010581, v_rip + 7010930, v_rip + 7010581, *(uint16_t *)(v_rip + 0x6AF91E));
    if ((uint32_t)(result) == 0) goto loc_0075BBDB;
loc_0075BB48:
    if ((*(uint64_t *)(v_rip + 0x86B063)) == (v_rip + 8827133)) goto loc_0075BBD5;
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x86B063) + 0x1EF)) == 0) goto loc_0075BBD3;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x86B063) + 0x1E0)) != (*(uint64_t *)(result + 0x1E0))) goto loc_0075BBD3;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x86B063) + 0x1CC)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1CC))))) goto loc_0075BBD3;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x86B063) + 0x1C4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1C4))))) goto loc_0075BBD3;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x86B063) + 0x1F4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1F4))))) goto loc_0075BBD3;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x86B063) + 0x1F8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1F8))))) goto loc_0075BBD3;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x86B063) + 0x1FC)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1FC))))) goto loc_0075BBD3;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x86B063) + 0x200)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x200))))) goto loc_0075BBD3;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x86B063) + 0x204)) != ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x204))))) goto loc_0075BBD3;
    goto loc_0075BB48;
loc_0075BBD3:
loc_0075BBD5:
    *(uint8_t *)(v_rip + 0x86AF11) = 0;
loc_0075BBDB:
    *(uint16_t *)(result + 0x4BC) = 257;
    result = PpmUpdateProcessorPolicy(v_rip + 8070546, result, v_rip + 7010581, *(uint16_t *)(v_rip + 0x6AF91E));
    result = PpmCheckResetProcessors(result, result, v_rip + 7010581, *(uint16_t *)(v_rip + 0x6AF91E));
    Arg2 = 0;
    result = KeCheckProcessorAffinityEx(local_rsp - 504 - 96, Arg2, v_rip + 7010581, *(uint16_t *)(v_rip + 0x6AF91E));
    if ((uint32_t)(result) != 0) {
        result = PpmParkApplyPolicy(local_rsp - 504 - 96, Arg2, v_rip + 7010581, *(uint16_t *)(v_rip + 0x6AF91E));
    }
    result = PpmCheckReInit(local_rsp - 504 - 96, Arg2, v_rip + 7010581, *(uint16_t *)(v_rip + 0x6AF91E));
    result = PpmPerfUpdateDomainPolicy(1, Arg2, v_rip + 7010581, *(uint16_t *)(v_rip + 0x6AF91E));
loc_0075BC2D:
    local_r14 = 0;
    if ((*(uint32_t *)(v_rip + 0x86B0B5)) > 1) goto loc_0075BC41;
    if ((uint8_t)(v_stack_m2D8) == 0) goto loc_0075BC75;
loc_0075BC41:
    result = KeIsEqualAffinityEx(v_rip + 7010273, v_rip + 7010648, v_rip + 7010581, *(uint16_t *)(v_rip + 0x6AF91E));
    if ((uint32_t)(result) != 0) {
        Arg1 = v_rip + 8064929;
        result = PpmAcquireLock(Arg1, v_rip + 7010648, v_rip + 7010581, *(uint16_t *)(v_rip + 0x6AF91E));
        a3 = 0;
        *(uint8_t *)(v_rip + 0x86AE6F) = (uint8_t)(v_stack_m2D8);
        Arg1 = 1;
        result = PpmReinitializeHeteroEngine(Arg1, v_rip + 7010648, a3, *(uint16_t *)(v_rip + 0x6AF91E));
    }
    if (0 == 0) goto loc_0075BD24;
    if ((uint32_t)((uint32_t)(v_stack_m2CC)) == 0) goto loc_0075BD17;
loc_0075BC91:
    if (*(uint64_t *)(v_stack_m2B8 + 0x10) == 0) goto loc_0075BD07;
    result = *(uint64_t *)(v_stack_m2B8 + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m2B8 + 0x10) + 0x58) != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x704D5050ULL));
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(v_stack_m2B8 + 0x10) + 0x58), Arg2, a3, *(uint16_t *)(v_rip + 0x6AF91E));
        result = *(uint64_t *)(v_stack_m2B8 + 0x10);
        *(uint64_t *)(result + 0x58) = 0;
    }
    result = *(uint64_t *)(v_stack_m2B8 + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m2B8 + 0x10) + 0x98) != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x704D5050ULL));
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(v_stack_m2B8 + 0x10) + 0x98), Arg2, a3, *(uint16_t *)(v_rip + 0x6AF91E));
        result = *(uint64_t *)(v_stack_m2B8 + 0x10);
        *(uint64_t *)(result + 0x98) = 0;
    }
    result = *(uint64_t *)(v_stack_m2B8 + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m2B8 + 0x10) + 0xD8) != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x704D5050ULL));
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(v_stack_m2B8 + 0x10) + 0xD8), Arg2, a3, *(uint16_t *)(v_rip + 0x6AF91E));
        result = *(uint64_t *)(v_stack_m2B8 + 0x10);
        *(uint64_t *)(result + 0xD8) = 0;
    }
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m2B8 + 0x10), (uint32_t)((uint32_t)((uint32_t)(0x704D5050ULL))), a3, *(uint16_t *)(v_rip + 0x6AF91E));
    *(uint64_t *)(v_stack_m2B8 + 0x10) = 0;
loc_0075BD07:
    local_rbx = (v_stack_m2B8 + 16) + (784);
    local_rsi = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m2CC)))) - (1);
    if (condition_is_not_equal) goto loc_0075BC91;
loc_0075BD17:
    result = ExFreePoolWithTag(0, (uint32_t)(0x704D5050ULL), a3, *(uint16_t *)(v_rip + 0x6AF91E));
loc_0075BD24:
    result = KeSetTimer2(v_rip + 8070242, (uint32_t)(0x704D5050ULL), a3, local_rsp - 504 - 120);
    Arg1 = (*(uint64_t *)(local_rsp - 0x1F8 + 0x1C0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x704D5050ULL), a3, local_rsp - 504 - 120);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x4` | `16` | `R` |
| `Arg1` | `+ 0x6` | `8` | `R` |
| `Arg1` | `+ 0x7` | `8` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x9` | `8` | `R` |
| `Arg1` | `+ 0xA` | `8` | `R` |
| `Arg1` | `+ 0xB` | `8` | `R` |
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0xD` | `8` | `R` |
| `Arg1` | `+ 0xE` | `8` | `R` |
| `Arg1` | `+ 0xF` | `8` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x24` | `32` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x34` | `8` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `32` | `R` |
| `Arg1` | `+ 0x4C` | `32` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x54` | `32` | `R` |
| `Arg1` | `+ 0x58` | `32` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x178` | `64` | `R` |

추가 오프셋 25개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0075B084&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
