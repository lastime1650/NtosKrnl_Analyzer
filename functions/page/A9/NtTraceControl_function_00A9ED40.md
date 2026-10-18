# NtTraceControl

- RVA: `0x00A9ED40`–`0x00A9F90F` (길이 `3,023` bytes)
- VA: `0x0000000140A9ED40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BA98C`
- 디코드: `748`개 명령, `3,023/3,023` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **51**; 고유 호출 대상: **49**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A9ED89` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00A9EE15` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00A9EEB7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A9EEE9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A9EF6D` → [EtwpValidateLoggerInfo](../8B/EtwpValidateLoggerInfo_function_008BF9B0.md) (function, `0x008BF9B0`)
- `0x00A9EFBE` → [WdiDispatchControl](../A5/WdiDispatchControl_function_00A5C308.md) (function, `0x00A5C308`)
- `0x00A9EFE4` → [EtwpCreateActivityId](../../text/43/EtwpCreateActivityId_function_0043F0A0.md) (function, `0x0043F0A0`)
- `0x00A9F027` → [EtwpRealtimeConnect](../A6/EtwpRealtimeConnect_function_00A65C88.md) (function, `0x00A65C88`)
- `0x00A9F075` → [EtwpTransitionToRealtime](../../text/65/EtwpTransitionToRealtime_function_006518D8.md) (function, `0x006518D8`)
- `0x00A9F082` → [EtwpIncrementTraceFile](../7B/EtwpIncrementTraceFile_function_007B9210.md) (function, `0x007B9210`)
- `0x00A9F08F` → [EtwpFlushTrace](../AF/EtwpFlushTrace_function_00AF47B4.md) (function, `0x00AF47B4`)
- `0x00A9F09C` → [EtwpUpdateTrace](../AB/EtwpUpdateTrace_function_00ABCC7C.md) (function, `0x00ABCC7C`)
- `0x00A9F0A9` → [EtwpQueryTrace](../8B/EtwpQueryTrace_function_008BF8B0.md) (function, `0x008BF8B0`)
- `0x00A9F0B9` → [EtwpStopTrace](../9B/EtwpStopTrace_function_009BCE84.md) (function, `0x009BCE84`)
- `0x00A9F0DA` → [EtwpStartTrace](EtwpStartTrace_function_00A99D08.md) (function, `0x00A99D08`)
- `0x00A9F107` → [EtwpRealtimeDisconnectConsumerByHandle](EtwpRealtimeDisconnectConsumerByHandle_function_00A9E368.md) (function, `0x00A9E368`)
- `0x00A9F186` → [EtwpReceiveReplyDataBlock](../A8/EtwpReceiveReplyDataBlock_function_00A87954.md) (function, `0x00A87954`)
- `0x00A9F1AC` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (function, `0x00433560`)
- `0x00A9F1B7` → [EtwpSendReplyDataBlock](../9F/EtwpSendReplyDataBlock_function_009FEC64.md) (function, `0x009FEC64`)
- `0x00A9F1F4` → [EtwpEnableGuid](../A5/EtwpEnableGuid_function_00A5CD28.md) (function, `0x00A5CD28`)
- `0x00A9F211` → [EtwpNotifyGuid](../8C/EtwpNotifyGuid_function_008C8110.md) (function, `0x008C8110`)
- `0x00A9F23F` → [EtwpReceiveNotification](../8B/EtwpReceiveNotification_function_008BF9F0.md) (function, `0x008BF9F0`)
- `0x00A9F27F` → [EtwpRegisterUMProvider](../8C/EtwpRegisterUMProvider_function_008C22A0.md) (function, `0x008C22A0`)
- `0x00A9F29A` → [WdiUpdateSem](../../text/64/WdiUpdateSem_function_0064E064.md) (function, `0x0064E064`)
- `0x00A9F2EC` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (function, `0x00433560`)
- `0x00A9F323` → [EtwpEnumerateTraceGuids](../A5/EtwpEnumerateTraceGuids_function_00A5F6FC.md) (function, `0x00A5F6FC`)
- `0x00A9F361` → [EtwpGetTraceGuidInfo](../9E/EtwpGetTraceGuidInfo_function_009E8BD0.md) (function, `0x009E8BD0`)
- `0x00A9F37D` → [EtwpGetTraceGuidList](../A5/EtwpGetTraceGuidList_function_00A5FEC4.md) (function, `0x00A5FEC4`)
- `0x00A9F3AE` → [EtwpQueryReferenceTime](../7B/EtwpQueryReferenceTime_function_007B92F0.md) (function, `0x007B92F0`)
- `0x00A9F420` → [EtwpUseDescriptorTypeUm](../AC/EtwpUseDescriptorTypeUm_function_00AC3338.md) (function, `0x00AC3338`)
- `0x00A9F44D` → [EtwpSetProviderTraitsUm](../9F/EtwpSetProviderTraitsUm_function_009F3514.md) (function, `0x009F3514`)
- `0x00A9F48E` → [EtwpUpdateDisallowList](../9E/EtwpUpdateDisallowList_function_009EA880.md) (function, `0x009EA880`)
- `0x00A9F4B5` → [EtwpAddNotificationEvent](../A5/EtwpAddNotificationEvent_function_00A5FC44.md) (function, `0x00A5FC44`)
- `0x00A9F4FF` → [EtwpGetGuidList](../8C/EtwpGetGuidList_function_008C2F00.md) (function, `0x008C2F00`)
- `0x00A9F549` → [EtwpGetCompressionSettings](../../text/65/EtwpGetCompressionSettings_function_006535A8.md) (function, `0x006535A8`)
- `0x00A9F56E` → [EtwpSetCompressionSettings](../../text/65/EtwpSetCompressionSettings_function_00653910.md) (function, `0x00653910`)
- `0x00A9F594` → [EtwpGetDisallowList](../A7/EtwpGetDisallowList_function_00A7DE80.md) (function, `0x00A7DE80`)
- `0x00A9F5C2` → [EtwpGetTraceGroupInfo](../9A/EtwpGetTraceGroupInfo_function_009A9CC0.md) (function, `0x009A9CC0`)
- `0x00A9F63A` → [EtwpUpdatePeriodicCaptureState](../7B/EtwpUpdatePeriodicCaptureState_function_007BCC4C.md) (function, `0x007BCC4C`)
- `0x00A9F6BD` → [EtwpSetProviderBinaryTracking](../A0/EtwpSetProviderBinaryTracking_function_00A03BF4.md) (function, `0x00A03BF4`)
- `0x00A9F6E0` → [EtwpQuerySessionDemuxObject](../7B/EtwpQuerySessionDemuxObject_function_007BC8B0.md) (function, `0x007BC8B0`)
- `0x00A9F71C` → [EtwpRegisterPrivateSession](../7B/EtwpRegisterPrivateSession_function_007BC92C.md) (function, `0x007BC92C`)
- `0x00A9F768` → [EtwpGetPrivateSessionTraceHandle](../7B/EtwpGetPrivateSessionTraceHandle_function_007BC5A8.md) (function, `0x007BC5A8`)
- `0x00A9F7DE` → [EtwpTrackProviderBinary](../7B/EtwpTrackProviderBinary_function_007B9198.md) (function, `0x007B9198`)
- `0x00A9F7F5` → [EtwpGetPmcSessions](../../text/64/EtwpGetPmcSessions_function_0064EB08.md) (function, `0x0064EB08`)
- `0x00A9F80C` → [EtwpGetPmcOwnership](../../text/64/EtwpGetPmcOwnership_function_0064E960.md) (function, `0x0064E960`)
- `0x00A9F83B` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x00A9F850` → [EtwpQueryUsedProcessorCount](../../text/3E/EtwpQueryUsedProcessorCount_function_003EB940.md) (function, `0x003EB940`)
- `0x00A9F859` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x00A9F884` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A9F8F7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PerfDiagpProxyWorker](../7A/PerfDiagpProxyWorker_function_007AEF20.md) at `0x007AF05D`
- [PerfDiagpUpdatePerfDiagLoggerEnableFlags](../7A/PerfDiagpUpdatePerfDiagLoggerEnableFlags_function_007AF21C.md) at `0x007AF308`
- [PerfDiagpSaveActiveDCLLogFileName](PerfDiagpSaveActiveDCLLogFileName_function_00A9EB80.md) at `0x00A9EC52`

### Static image references
- `0x00A9F79E` → RVA `0x00E0EB1C` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x00A9ED89` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x00A9EEB7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A9EEE9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A9EFE4` → [EtwpCreateActivityId](../../text/43/EtwpCreateActivityId_function_0043F0A0.md) (`PAGE` → `.text`)
  - `0x00A9F075` → [EtwpTransitionToRealtime](../../text/65/EtwpTransitionToRealtime_function_006518D8.md) (`PAGE` → `.text`)
  - `0x00A9F1AC` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (`PAGE` → `.text`)
  - `0x00A9F29A` → [WdiUpdateSem](../../text/64/WdiUpdateSem_function_0064E064.md) (`PAGE` → `.text`)
  - `0x00A9F2EC` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (`PAGE` → `.text`)
  - `0x00A9F549` → [EtwpGetCompressionSettings](../../text/65/EtwpGetCompressionSettings_function_006535A8.md) (`PAGE` → `.text`)
  - `0x00A9F56E` → [EtwpSetCompressionSettings](../../text/65/EtwpSetCompressionSettings_function_00653910.md) (`PAGE` → `.text`)
  - `0x00A9F7F5` → [EtwpGetPmcSessions](../../text/64/EtwpGetPmcSessions_function_0064EB08.md) (`PAGE` → `.text`)
  - `0x00A9F80C` → [EtwpGetPmcOwnership](../../text/64/EtwpGetPmcOwnership_function_0064E960.md) (`PAGE` → `.text`)
  - `0x00A9F850` → [EtwpQueryUsedProcessorCount](../../text/3E/EtwpQueryUsedProcessorCount_function_003EB940.md) (`PAGE` → `.text`)
  - `0x00A9F884` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A9F8F7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A9ED40  48 8B C4                        mov rax, rsp
00A9ED43  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00A9ED47  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00A9ED4B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00A9ED4F  89 48 08                        mov dword ptr [rax + 8], ecx
00A9ED52  53                              push rbx
00A9ED53  56                              push rsi
00A9ED54  57                              push rdi
00A9ED55  41 54                           push r12
00A9ED57  41 55                           push r13
00A9ED59  41 56                           push r14
00A9ED5B  41 57                           push r15
00A9ED5D  48 83 EC 60                     sub rsp, 0x60
00A9ED61  4D 8B D9                        mov r11, r9
00A9ED64  44 8B E9                        mov r13d, ecx
00A9ED67  44 8B D1                        mov r10d, ecx
00A9ED6A  45 33 F6                        xor r14d, r14d
00A9ED6D  41 8B FE                        mov edi, r14d
00A9ED70  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
00A9ED75  44 89 70 98                     mov dword ptr [rax - 0x68], r14d
00A9ED79  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A9ED82  44 8A 80 32 02 00 00            mov r8b, byte ptr [rax + 0x232]
00A9ED89  E8 62 F4 85 FF                  call 0x1402fe1f0
00A9ED8E  4C 8B A0 40 03 00 00            mov r12, qword ptr [rax + 0x340]
00A9ED95  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00A9ED9A  41 8B DE                        mov ebx, r14d
00A9ED9D  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
00A9EDA1  44 88 74 24 38                  mov byte ptr [rsp + 0x38], r14b
00A9EDA6  45 84 C0                        test r8b, r8b
00A9EDA9  0F 84 BA 00 00 00               je 0x140a9ee69
00A9EDAF  45 8B CA                        mov r9d, r10d
00A9EDB2  41 C1 E9 1F                     shr r9d, 0x1f
00A9EDB6  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
00A9EDBB  41 0F BA F5 1F                  btr r13d, 0x1f
00A9EDC0  45 84 C9                        test r9b, r9b
00A9EDC3  45 0F 44 EA                     cmove r13d, r10d
00A9EDC7  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00A9EDD1  48 85 D2                        test rdx, rdx
00A9EDD4  74 22                           je 0x140a9edf8
00A9EDD6  44 39 B4 24 B0 00 00 00         cmp dword ptr [rsp + 0xb0], r14d
00A9EDDE  74 20                           je 0x140a9ee00
00A9EDE0  8B 8C 24 B0 00 00 00            mov ecx, dword ptr [rsp + 0xb0]
00A9EDE7  48 03 CA                        add rcx, rdx
00A9EDEA  48 3B CB                        cmp rcx, rbx
00A9EDED  77 05                           ja 0x140a9edf4
00A9EDEF  48 3B CA                        cmp rcx, rdx
00A9EDF2  73 0C                           jae 0x140a9ee00
00A9EDF4  8A 03                           mov al, byte ptr [rbx]
00A9EDF6  EB 08                           jmp 0x140a9ee00
00A9EDF8  44 89 B4 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r14d
00A9EE00  4D 85 DB                        test r11, r11
00A9EE03  74 17                           je 0x140a9ee1c
00A9EE05  8B 94 24 C0 00 00 00            mov edx, dword ptr [rsp + 0xc0]
00A9EE0C  41 B8 01 00 00 00               mov r8d, 1
00A9EE12  49 8B CB                        mov rcx, r11
00A9EE15  E8 A6 A3 E4 FF                  call 0x1408e91c0
00A9EE1A  EB 08                           jmp 0x140a9ee24
00A9EE1C  44 89 B4 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r14d
00A9EE24  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00A9EE2C  48 85 C0                        test rax, rax
00A9EE2F  74 19                           je 0x140a9ee4a
00A9EE31  48 3B C3                        cmp rax, rbx
00A9EE34  48 0F 42 D8                     cmovb rbx, rax
00A9EE38  8B 03                           mov eax, dword ptr [rbx]
00A9EE3A  89 03                           mov dword ptr [rbx], eax
00A9EE3C  44 89 AC 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r13d
00A9EE44  8B 5C 24 3C                     mov ebx, dword ptr [rsp + 0x3c]
00A9EE48  EB 1F                           jmp 0x140a9ee69
00A9EE4A  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A9EE4F  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
00A9EE53  E9 95 0A 00 00                  jmp 0x140a9f8ed
00A9EE58  8B D8                           mov ebx, eax
00A9EE5A  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
00A9EE5E  45 33 F6                        xor r14d, r14d
00A9EE61  41 8B FE                        mov edi, r14d
00A9EE64  E9 84 0A 00 00                  jmp 0x140a9f8ed
00A9EE69  41 83 FD 1B                     cmp r13d, 0x1b
00A9EE6D  77 1C                           ja 0x140a9ee8b
00A9EE6F  B8 00 50 00 08                  mov eax, 0x8005000
00A9EE74  44 0F A3 E8                     bt eax, r13d
00A9EE78  73 11                           jae 0x140a9ee8b
00A9EE7A  44 8B BC 24 C0 00 00 00         mov r15d, dword ptr [rsp + 0xc0]
00A9EE82  8B B4 24 B0 00 00 00            mov esi, dword ptr [rsp + 0xb0]
00A9EE89  EB 79                           jmp 0x140a9ef04
00A9EE8B  8B B4 24 B0 00 00 00            mov esi, dword ptr [rsp + 0xb0]
00A9EE92  44 8B BC 24 C0 00 00 00         mov r15d, dword ptr [rsp + 0xc0]
00A9EE9A  85 F6                           test esi, esi
00A9EE9C  75 05                           jne 0x140a9eea3
00A9EE9E  45 85 FF                        test r15d, r15d
00A9EEA1  74 61                           je 0x140a9ef04
00A9EEA3  41 8B D7                        mov edx, r15d
00A9EEA6  41 3B F7                        cmp esi, r15d
00A9EEA9  0F 47 D6                        cmova edx, esi
00A9EEAC  B9 01 01 00 00                  mov ecx, 0x101
00A9EEB1  41 B8 45 74 77 50               mov r8d, 0x50777445
00A9EEB7  E8 34 32 0E 00                  call 0x140b820f0
00A9EEBC  48 8B F8                        mov rdi, rax
00A9EEBF  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A9EEC4  48 85 C0                        test rax, rax
00A9EEC7  75 0A                           jne 0x140a9eed3
00A9EEC9  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A9EECE  E9 1A 0A 00 00                  jmp 0x140a9f8ed
00A9EED3  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00A9EEDB  48 85 C9                        test rcx, rcx
00A9EEDE  74 2C                           je 0x140a9ef0c
00A9EEE0  4C 8B C6                        mov r8, rsi
00A9EEE3  48 8B D1                        mov rdx, rcx
00A9EEE6  48 8B C8                        mov rcx, rax
00A9EEE9  E8 52 79 C2 FF                  call 0x1406c6840
00A9EEEE  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00A9EEF6  EB 14                           jmp 0x140a9ef0c
00A9EEF8  8B D8                           mov ebx, eax
00A9EEFA  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00A9EEFF  E9 E9 09 00 00                  jmp 0x140a9f8ed
00A9EF04  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00A9EF0C  41 83 FD 19                     cmp r13d, 0x19
00A9EF10  0F 87 A9 04 00 00               ja 0x140a9f3bf
00A9EF16  0F 84 72 04 00 00               je 0x140a9f38e
00A9EF1C  41 83 FD 0E                     cmp r13d, 0xe
00A9EF20  0F 87 0F 02 00 00               ja 0x140a9f135
00A9EF26  0F 84 C2 01 00 00               je 0x140a9f0ee
00A9EF2C  41 83 FD 06                     cmp r13d, 6
00A9EF30  77 5C                           ja 0x140a9ef8e
00A9EF32  74 20                           je 0x140a9ef54
00A9EF34  41 8B C5                        mov eax, r13d
00A9EF37  83 E8 01                        sub eax, 1
00A9EF3A  74 18                           je 0x140a9ef54
00A9EF3C  83 E8 01                        sub eax, 1
00A9EF3F  74 13                           je 0x140a9ef54
00A9EF41  83 E8 01                        sub eax, 1
00A9EF44  74 0E                           je 0x140a9ef54
00A9EF46  83 E8 01                        sub eax, 1
00A9EF49  74 09                           je 0x140a9ef54
00A9EF4B  83 F8 01                        cmp eax, 1
00A9EF4E  0F 85 6C 08 00 00               jne 0x140a9f7c0
00A9EF54  B8 B0 00 00 00                  mov eax, 0xb0
00A9EF59  3B F0                           cmp esi, eax
00A9EF5B  0F 82 DB 00 00 00               jb 0x140a9f03c
00A9EF61  44 3B F8                        cmp r15d, eax
00A9EF64  0F 82 D2 00 00 00               jb 0x140a9f03c
00A9EF6A  48 8B CF                        mov rcx, rdi
00A9EF6D  E8 3E 0A E2 FF                  call 0x1408bf9b0
00A9EF72  8B D8                           mov ebx, eax
00A9EF74  85 C0                           test eax, eax
00A9EF76  0F 88 C5 00 00 00               js 0x140a9f041
00A9EF7C  39 37                           cmp dword ptr [rdi], esi
00A9EF7E  0F 86 B3 00 00 00               jbe 0x140a9f037
00A9EF84  BB 06 02 00 C0                  mov ebx, 0xc0000206
00A9EF89  E9 D7 08 00 00                  jmp 0x140a9f865
00A9EF8E  41 8B C5                        mov eax, r13d
00A9EF91  83 E8 07                        sub eax, 7
00A9EF94  74 BE                           je 0x140a9ef54
00A9EF96  83 E8 04                        sub eax, 4
00A9EF99  74 77                           je 0x140a9f012
00A9EF9B  83 E8 01                        sub eax, 1
00A9EF9E  74 2A                           je 0x140a9efca
00A9EFA0  83 F8 01                        cmp eax, 1
00A9EFA3  0F 85 17 08 00 00               jne 0x140a9f7c0
00A9EFA9  83 FE 30                        cmp esi, 0x30
00A9EFAC  0F 85 AE 08 00 00               jne 0x140a9f860
00A9EFB2  45 85 FF                        test r15d, r15d
00A9EFB5  0F 85 A5 08 00 00               jne 0x140a9f860
00A9EFBB  48 8B CF                        mov rcx, rdi
00A9EFBE  E8 45 D3 FB FF                  call 0x140a5c308
00A9EFC3  8B D8                           mov ebx, eax
00A9EFC5  E9 9B 08 00 00                  jmp 0x140a9f865
00A9EFCA  41 BC 10 00 00 00               mov r12d, 0x10
00A9EFD0  45 3B FC                        cmp r15d, r12d
00A9EFD3  0F 85 87 08 00 00               jne 0x140a9f860
00A9EFD9  41 8B DE                        mov ebx, r14d
00A9EFDC  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00A9EFE4  E8 B7 00 9A FF                  call 0x14043f0a0
00A9EFE9  E9 7F 08 00 00                  jmp 0x140a9f86d
00A9EFEE  8B D8                           mov ebx, eax
00A9EFF0  44 8B BC 24 C0 00 00 00         mov r15d, dword ptr [rsp + 0xc0]
00A9EFF8  44 8B AC 24 A0 00 00 00         mov r13d, dword ptr [rsp + 0xa0]
00A9F000  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00A9F005  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00A9F00D  E9 5B 08 00 00                  jmp 0x140a9f86d
00A9F012  83 FE 60                        cmp esi, 0x60
00A9F015  0F 85 45 08 00 00               jne 0x140a9f860
00A9F01B  44 3B FE                        cmp r15d, esi
00A9F01E  0F 85 3C 08 00 00               jne 0x140a9f860
00A9F024  48 8B CF                        mov rcx, rdi
00A9F027  E8 5C 6C FC FF                  call 0x140a65c88
00A9F02C  8B D8                           mov ebx, eax
00A9F02E  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00A9F032  E9 2E 08 00 00                  jmp 0x140a9f865
00A9F037  41 8B DE                        mov ebx, r14d
00A9F03A  EB 05                           jmp 0x140a9f041
00A9F03C  BB 06 02 00 C0                  mov ebx, 0xc0000206
00A9F041  85 DB                           test ebx, ebx
00A9F043  0F 88 1C 08 00 00               js 0x140a9f865
00A9F049  41 8B C5                        mov eax, r13d
00A9F04C  83 E8 01                        sub eax, 1
00A9F04F  74 6F                           je 0x140a9f0c0
00A9F051  83 E8 01                        sub eax, 1
00A9F054  74 5A                           je 0x140a9f0b0
00A9F056  83 E8 01                        sub eax, 1
00A9F059  74 48                           je 0x140a9f0a3
00A9F05B  83 E8 01                        sub eax, 1
00A9F05E  74 36                           je 0x140a9f096
00A9F060  83 E8 01                        sub eax, 1
00A9F063  74 24                           je 0x140a9f089
00A9F065  83 E8 01                        sub eax, 1
00A9F068  74 12                           je 0x140a9f07c
00A9F06A  83 F8 01                        cmp eax, 1
00A9F06D  75 72                           jne 0x140a9f0e1
00A9F06F  48 8B D7                        mov rdx, rdi
00A9F072  49 8B CC                        mov rcx, r12
00A9F075  E8 5E 28 BB FF                  call 0x1406518d8
00A9F07A  EB 63                           jmp 0x140a9f0df
00A9F07C  48 8B D7                        mov rdx, rdi
00A9F07F  49 8B CC                        mov rcx, r12
00A9F082  E8 89 A1 D1 FF                  call 0x1407b9210
00A9F087  EB 56                           jmp 0x140a9f0df
00A9F089  48 8B D7                        mov rdx, rdi
00A9F08C  49 8B CC                        mov rcx, r12
00A9F08F  E8 20 57 05 00                  call 0x140af47b4
00A9F094  EB 49                           jmp 0x140a9f0df
00A9F096  48 8B D7                        mov rdx, rdi
00A9F099  49 8B CC                        mov rcx, r12
00A9F09C  E8 DB DB 01 00                  call 0x140abcc7c
00A9F0A1  EB 3C                           jmp 0x140a9f0df
00A9F0A3  48 8B D7                        mov rdx, rdi
00A9F0A6  49 8B CC                        mov rcx, r12
00A9F0A9  E8 02 08 E2 FF                  call 0x1408bf8b0
00A9F0AE  EB 2F                           jmp 0x140a9f0df
00A9F0B0  45 33 C0                        xor r8d, r8d
00A9F0B3  48 8B D7                        mov rdx, rdi
00A9F0B6  49 8B CC                        mov rcx, r12
00A9F0B9  E8 C6 DD F1 FF                  call 0x1409bce84
00A9F0BE  EB 1F                           jmp 0x140a9f0df
00A9F0C0  48 8B 4F 50                     mov rcx, qword ptr [rdi + 0x50]
00A9F0C4  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
00A9F0C8  0F B6 44 24 38                  movzx eax, byte ptr [rsp + 0x38]
00A9F0CD  48 0B C8                        or rcx, rax
00A9F0D0  48 89 4F 50                     mov qword ptr [rdi + 0x50], rcx
00A9F0D4  48 8B D7                        mov rdx, rdi
00A9F0D7  49 8B CC                        mov rcx, r12
00A9F0DA  E8 29 AC FF FF                  call 0x140a99d08
00A9F0DF  8B D8                           mov ebx, eax
00A9F0E1  C7 44 24 30 B0 00 00 00         mov dword ptr [rsp + 0x30], 0xb0
00A9F0E9  E9 77 07 00 00                  jmp 0x140a9f865
00A9F0EE  83 FE 08                        cmp esi, 8
00A9F0F1  0F 85 69 07 00 00               jne 0x140a9f860
00A9F0F7  45 85 FF                        test r15d, r15d
00A9F0FA  0F 85 60 07 00 00               jne 0x140a9f860
00A9F100  8B 09                           mov ecx, dword ptr [rcx]
00A9F102  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00A9F107  E8 5C F2 FF FF                  call 0x140a9e368
00A9F10C  E9 B2 FE FF FF                  jmp 0x140a9efc3
00A9F111  8B D8                           mov ebx, eax
00A9F113  44 8B BC 24 C0 00 00 00         mov r15d, dword ptr [rsp + 0xc0]
00A9F11B  44 8B AC 24 A0 00 00 00         mov r13d, dword ptr [rsp + 0xa0]
00A9F123  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00A9F128  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00A9F130  E9 38 07 00 00                  jmp 0x140a9f86d
00A9F135  41 83 FD 14                     cmp r13d, 0x14
00A9F139  0F 87 65 01 00 00               ja 0x140a9f2a4
00A9F13F  0F 84 44 01 00 00               je 0x140a9f289
00A9F145  41 8B C5                        mov eax, r13d
00A9F148  83 E8 0F                        sub eax, 0xf
00A9F14B  0F 84 F8 00 00 00               je 0x140a9f249
00A9F151  83 E8 01                        sub eax, 1
00A9F154  0F 84 BE 00 00 00               je 0x140a9f218
00A9F15A  83 E8 01                        sub eax, 1
00A9F15D  74 62                           je 0x140a9f1c1
00A9F15F  83 E8 01                        sub eax, 1
00A9F162  74 36                           je 0x140a9f19a
00A9F164  83 F8 01                        cmp eax, 1
00A9F167  0F 85 53 06 00 00               jne 0x140a9f7c0
00A9F16D  83 FE 08                        cmp esi, 8
00A9F170  0F 85 EA 06 00 00               jne 0x140a9f860
00A9F176  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
00A9F17B  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A9F180  41 8B D7                        mov edx, r15d
00A9F183  48 8B CF                        mov rcx, rdi
00A9F186  E8 C9 87 FE FF                  call 0x140a87954
00A9F18B  8B D8                           mov ebx, eax
00A9F18D  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00A9F191  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A9F195  E9 CB 06 00 00                  jmp 0x140a9f865
00A9F19A  83 FE 48                        cmp esi, 0x48
00A9F19D  0F 82 BD 06 00 00               jb 0x140a9f860
00A9F1A3  39 77 04                        cmp dword ptr [rdi + 4], esi
00A9F1A6  0F 85 B4 06 00 00               jne 0x140a9f860
00A9F1AC  E8 AF 43 99 FF                  call 0x140433560
00A9F1B1  89 47 24                        mov dword ptr [rdi + 0x24], eax
00A9F1B4  48 8B CF                        mov rcx, rdi
00A9F1B7  E8 A8 FA F5 FF                  call 0x1409fec64
00A9F1BC  E9 02 FE FF FF                  jmp 0x140a9efc3
00A9F1C1  83 FE 48                        cmp esi, 0x48
00A9F1C4  0F 82 96 06 00 00               jb 0x140a9f860
00A9F1CA  41 83 FF 48                     cmp r15d, 0x48
00A9F1CE  0F 85 8C 06 00 00               jne 0x140a9f860
00A9F1D4  39 77 04                        cmp dword ptr [rdi + 4], esi
00A9F1D7  0F 85 83 06 00 00               jne 0x140a9f860
00A9F1DD  83 3F 03                        cmp dword ptr [rdi], 3
00A9F1E0  75 26                           jne 0x140a9f208
00A9F1E2  83 FE 78                        cmp esi, 0x78
00A9F1E5  0F 82 75 06 00 00               jb 0x140a9f860
00A9F1EB  41 B0 01                        mov r8b, 1
00A9F1EE  48 8B D7                        mov rdx, rdi
00A9F1F1  49 8B CC                        mov rcx, r12
00A9F1F4  E8 2F DB FB FF                  call 0x140a5cd28
00A9F1F9  8B D8                           mov ebx, eax
00A9F1FB  C7 44 24 30 48 00 00 00         mov dword ptr [rsp + 0x30], 0x48
00A9F203  E9 5D 06 00 00                  jmp 0x140a9f865
00A9F208  41 B0 01                        mov r8b, 1
00A9F20B  48 8B D7                        mov rdx, rdi
00A9F20E  49 8B CC                        mov rcx, r12
00A9F211  E8 FA 8E E2 FF                  call 0x1408c8110
00A9F216  EB E1                           jmp 0x140a9f1f9
00A9F218  85 F6                           test esi, esi
00A9F21A  0F 85 40 06 00 00               jne 0x140a9f860
00A9F220  41 8D 47 B8                     lea eax, [r15 - 0x48]
00A9F224  3D B8 FF 00 00                  cmp eax, 0xffb8
00A9F229  0F 87 31 06 00 00               ja 0x140a9f860
00A9F22F  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00A9F234  44 8A 44 24 38                  mov r8b, byte ptr [rsp + 0x38]
00A9F239  41 8B D7                        mov edx, r15d
00A9F23C  48 8B CF                        mov rcx, rdi
00A9F23F  E8 AC 07 E2 FF                  call 0x1408bf9f0
00A9F244  E9 7A FD FF FF                  jmp 0x140a9efc3
00A9F249  81 FE A0 00 00 00               cmp esi, 0xa0
00A9F24F  0F 85 0B 06 00 00               jne 0x140a9f860
00A9F255  41 8D 87 60 FF FF FF            lea eax, [r15 - 0xa0]
00A9F25C  3D 60 FF 00 00                  cmp eax, 0xff60
00A9F261  0F 87 F9 05 00 00               ja 0x140a9f860
00A9F267  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00A9F26C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A9F271  44 8A 4C 24 38                  mov r9b, byte ptr [rsp + 0x38]
00A9F276  45 8B C7                        mov r8d, r15d
00A9F279  48 8B D7                        mov rdx, rdi
00A9F27C  49 8B CC                        mov rcx, r12
00A9F27F  E8 1C 30 E2 FF                  call 0x1408c22a0
00A9F284  E9 3A FD FF FF                  jmp 0x140a9efc3
00A9F289  85 F6                           test esi, esi
00A9F28B  0F 85 CF 05 00 00               jne 0x140a9f860
00A9F291  45 85 FF                        test r15d, r15d
00A9F294  0F 85 C6 05 00 00               jne 0x140a9f860
00A9F29A  E8 C5 ED BA FF                  call 0x14064e064
00A9F29F  E9 1F FD FF FF                  jmp 0x140a9efc3
00A9F2A4  41 8B C5                        mov eax, r13d
00A9F2A7  83 E8 15                        sub eax, 0x15
00A9F2AA  0F 84 BB 00 00 00               je 0x140a9f36b
00A9F2B0  83 E8 01                        sub eax, 1
00A9F2B3  0F 84 84 00 00 00               je 0x140a9f33d
00A9F2B9  83 E8 01                        sub eax, 1
00A9F2BC  74 43                           je 0x140a9f301
00A9F2BE  83 F8 01                        cmp eax, 1
00A9F2C1  0F 85 F9 04 00 00               jne 0x140a9f7c0
00A9F2C7  85 F6                           test esi, esi
00A9F2C9  0F 85 91 05 00 00               jne 0x140a9f860
00A9F2CF  45 85 FF                        test r15d, r15d
00A9F2D2  0F 85 88 05 00 00               jne 0x140a9f860
00A9F2D8  45 39 B4 24 F8 10 00 00         cmp dword ptr [r12 + 0x10f8], r14d
00A9F2E0  74 0A                           je 0x140a9f2ec
00A9F2E2  BB 22 00 00 C0                  mov ebx, 0xc0000022
00A9F2E7  E9 79 05 00 00                  jmp 0x140a9f865
00A9F2EC  E8 6F 42 99 FF                  call 0x140433560
00A9F2F1  41 89 84 24 F8 10 00 00         mov dword ptr [r12 + 0x10f8], eax
00A9F2F9  41 8B DE                        mov ebx, r14d
00A9F2FC  E9 64 05 00 00                  jmp 0x140a9f865
00A9F301  41 8B CF                        mov ecx, r15d
00A9F304  48 B8 8F E3 38 8E E3 38 8E E3   movabs rax, 0xe38e38e38e38e38f
00A9F30E  48 F7 E1                        mul rcx
00A9F311  48 C1 EA 05                     shr rdx, 5
00A9F315  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00A9F31A  44 8B C2                        mov r8d, edx
00A9F31D  48 8B D7                        mov rdx, rdi
00A9F320  49 8B CC                        mov rcx, r12
00A9F323  E8 D4 03 FC FF                  call 0x140a5f6fc
00A9F328  8B D8                           mov ebx, eax
00A9F32A  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00A9F32E  8D 0C C0                        lea ecx, [rax + rax*8]
00A9F331  C1 E1 02                        shl ecx, 2
00A9F334  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00A9F338  E9 28 05 00 00                  jmp 0x140a9f865
00A9F33D  41 BC 10 00 00 00               mov r12d, 0x10
00A9F343  41 3B F4                        cmp esi, r12d
00A9F346  0F 85 14 05 00 00               jne 0x140a9f860
00A9F34C  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00A9F351  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00A9F356  4C 8B C7                        mov r8, rdi
00A9F359  48 8B D7                        mov rdx, rdi
00A9F35C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A9F361  E8 6A 98 F4 FF                  call 0x1409e8bd0
00A9F366  E9 58 FC FF FF                  jmp 0x140a9efc3
00A9F36B  45 8B C7                        mov r8d, r15d
00A9F36E  41 C1 E8 04                     shr r8d, 4
00A9F372  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00A9F377  48 8B D7                        mov rdx, rdi
00A9F37A  49 8B CC                        mov rcx, r12
00A9F37D  E8 42 0B FC FF                  call 0x140a5fec4
00A9F382  8B D8                           mov ebx, eax
00A9F384  C1 64 24 30 04                  shl dword ptr [rsp + 0x30], 4
00A9F389  E9 D7 04 00 00                  jmp 0x140a9f865
00A9F38E  83 FE 04                        cmp esi, 4
00A9F391  0F 85 C9 04 00 00               jne 0x140a9f860
00A9F397  44 8D 66 0C                     lea r12d, [rsi + 0xc]
00A9F39B  45 3B FC                        cmp r15d, r12d
00A9F39E  0F 85 BC 04 00 00               jne 0x140a9f860
00A9F3A4  8B 17                           mov edx, dword ptr [rdi]
00A9F3A6  4C 8B C7                        mov r8, rdi
00A9F3A9  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A9F3AE  E8 3D 9F D1 FF                  call 0x1407b92f0
00A9F3B3  8B D8                           mov ebx, eax
00A9F3B5  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00A9F3BA  E9 A6 04 00 00                  jmp 0x140a9f865
00A9F3BF  41 83 FD 25                     cmp r13d, 0x25
00A9F3C3  0F 87 7B 02 00 00               ja 0x140a9f644
00A9F3C9  0F 84 FD 01 00 00               je 0x140a9f5cc
00A9F3CF  41 83 FD 20                     cmp r13d, 0x20
00A9F3D3  0F 87 30 01 00 00               ja 0x140a9f509
00A9F3D9  0F 84 04 01 00 00               je 0x140a9f4e3
00A9F3DF  41 8B C5                        mov eax, r13d
00A9F3E2  83 E8 1A                        sub eax, 0x1a
00A9F3E5  0F 84 DF 03 00 00               je 0x140a9f7ca
00A9F3EB  83 E8 01                        sub eax, 1
00A9F3EE  0F 84 A4 00 00 00               je 0x140a9f498
00A9F3F4  83 E8 01                        sub eax, 1
00A9F3F7  74 5E                           je 0x140a9f457
00A9F3F9  83 E8 02                        sub eax, 2
00A9F3FC  74 2C                           je 0x140a9f42a
00A9F3FE  83 F8 01                        cmp eax, 1
00A9F401  0F 85 B9 03 00 00               jne 0x140a9f7c0
00A9F407  44 8D 60 0F                     lea r12d, [rax + 0xf]
00A9F40B  41 3B F4                        cmp esi, r12d
00A9F40E  0F 85 4C 04 00 00               jne 0x140a9f860
00A9F414  45 85 FF                        test r15d, r15d
00A9F417  0F 85 43 04 00 00               jne 0x140a9f860
00A9F41D  48 8B CF                        mov rcx, rdi
00A9F420  E8 13 3F 02 00                  call 0x140ac3338
00A9F425  E9 99 FB FF FF                  jmp 0x140a9efc3
00A9F42A  83 FE 18                        cmp esi, 0x18
00A9F42D  0F 85 2D 04 00 00               jne 0x140a9f860
00A9F433  41 8D 47 88                     lea eax, [r15 - 0x78]
00A9F437  3D 88 FF 00 00                  cmp eax, 0xff88
00A9F43C  0F 87 1E 04 00 00               ja 0x140a9f860
00A9F442  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00A9F447  41 8B D7                        mov edx, r15d
00A9F44A  48 8B CF                        mov rcx, rdi
00A9F44D  E8 C2 40 F5 FF                  call 0x1409f3514
00A9F452  E9 6C FB FF FF                  jmp 0x140a9efc3
00A9F457  83 FE 08                        cmp esi, 8
00A9F45A  0F 82 00 04 00 00               jb 0x140a9f860
00A9F460  44 8B 47 04                     mov r8d, dword ptr [rdi + 4]
00A9F464  41 8B C8                        mov ecx, r8d
00A9F467  48 C1 E1 04                     shl rcx, 4
00A9F46B  48 83 C1 08                     add rcx, 8
00A9F46F  8B C6                           mov eax, esi
00A9F471  48 3B C8                        cmp rcx, rax
00A9F474  0F 85 E6 03 00 00               jne 0x140a9f860
00A9F47A  41 8B C0                        mov eax, r8d
00A9F47D  48 8D 4F 08                     lea rcx, [rdi + 8]
00A9F481  F7 D8                           neg eax
00A9F483  4D 1B C9                        sbb r9, r9
00A9F486  4C 23 C9                        and r9, rcx
00A9F489  8B 17                           mov edx, dword ptr [rdi]
00A9F48B  49 8B CC                        mov rcx, r12
00A9F48E  E8 ED B3 F4 FF                  call 0x1409ea880
00A9F493  E9 2B FB FF FF                  jmp 0x140a9efc3
00A9F498  83 FE 04                        cmp esi, 4
00A9F49B  0F 85 BF 03 00 00               jne 0x140a9f860
00A9F4A1  8B 09                           mov ecx, dword ptr [rcx]
00A9F4A3  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00A9F4A8  48 85 C9                        test rcx, rcx
00A9F4AB  0F 84 AF 03 00 00               je 0x140a9f860
00A9F4B1  8A 54 24 38                     mov dl, byte ptr [rsp + 0x38]
00A9F4B5  E8 8A 07 FC FF                  call 0x140a5fc44
00A9F4BA  E9 04 FB FF FF                  jmp 0x140a9efc3
00A9F4BF  8B D8                           mov ebx, eax
00A9F4C1  44 8B BC 24 C0 00 00 00         mov r15d, dword ptr [rsp + 0xc0]
00A9F4C9  44 8B AC 24 A0 00 00 00         mov r13d, dword ptr [rsp + 0xa0]
00A9F4D1  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00A9F4D6  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00A9F4DE  E9 8A 03 00 00                  jmp 0x140a9f86d
00A9F4E3  45 8B CF                        mov r9d, r15d
00A9F4E6  41 C1 E9 04                     shr r9d, 4
00A9F4EA  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00A9F4EF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A9F4F4  4C 8B C7                        mov r8, rdi
00A9F4F7  BA 02 00 00 00                  mov edx, 2
00A9F4FC  49 8B CC                        mov rcx, r12
00A9F4FF  E8 FC 39 E2 FF                  call 0x1408c2f00
00A9F504  E9 79 FE FF FF                  jmp 0x140a9f382
00A9F509  41 8B C5                        mov eax, r13d
00A9F50C  83 E8 21                        sub eax, 0x21
00A9F50F  0F 84 89 00 00 00               je 0x140a9f59e
00A9F515  83 E8 01                        sub eax, 1
00A9F518  74 5E                           je 0x140a9f578
00A9F51A  83 E8 01                        sub eax, 1
00A9F51D  74 34                           je 0x140a9f553
00A9F51F  83 F8 01                        cmp eax, 1
00A9F522  0F 85 98 02 00 00               jne 0x140a9f7c0
00A9F528  83 FE 08                        cmp esi, 8
00A9F52B  0F 85 2F 03 00 00               jne 0x140a9f860
00A9F531  44 8D 60 0F                     lea r12d, [rax + 0xf]
00A9F535  45 3B FC                        cmp r15d, r12d
00A9F538  0F 85 22 03 00 00               jne 0x140a9f860
00A9F53E  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00A9F543  48 8B D7                        mov rdx, rdi
00A9F546  48 8B CF                        mov rcx, rdi
00A9F549  E8 5A 40 BB FF                  call 0x1406535a8
00A9F54E  E9 70 FA FF FF                  jmp 0x140a9efc3
00A9F553  41 BC 10 00 00 00               mov r12d, 0x10
00A9F559  41 3B F4                        cmp esi, r12d
00A9F55C  0F 85 FE 02 00 00               jne 0x140a9f860
00A9F562  45 85 FF                        test r15d, r15d
00A9F565  0F 85 F5 02 00 00               jne 0x140a9f860
00A9F56B  48 8B CF                        mov rcx, rdi
00A9F56E  E8 9D 43 BB FF                  call 0x140653910
00A9F573  E9 4B FA FF FF                  jmp 0x140a9efc3
00A9F578  83 FE 08                        cmp esi, 8
00A9F57B  0F 85 DF 02 00 00               jne 0x140a9f860
00A9F581  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00A9F586  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00A9F58B  4C 8B C7                        mov r8, rdi
00A9F58E  48 8B D7                        mov rdx, rdi
00A9F591  49 8B CC                        mov rcx, r12
00A9F594  E8 E7 E8 FD FF                  call 0x140a7de80
00A9F599  E9 25 FA FF FF                  jmp 0x140a9efc3
00A9F59E  41 BC 10 00 00 00               mov r12d, 0x10
00A9F5A4  41 3B F4                        cmp esi, r12d
00A9F5A7  0F 85 B3 02 00 00               jne 0x140a9f860
00A9F5AD  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00A9F5B2  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00A9F5B7  4C 8B C7                        mov r8, rdi
00A9F5BA  48 8B D7                        mov rdx, rdi
00A9F5BD  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A9F5C2  E8 F9 A6 F0 FF                  call 0x1409a9cc0
00A9F5C7  E9 F7 F9 FF FF                  jmp 0x140a9efc3
00A9F5CC  83 FE 0C                        cmp esi, 0xc
00A9F5CF  0F 82 8B 02 00 00               jb 0x140a9f860
00A9F5D5  44 0F B7 47 08                  movzx r8d, word ptr [rdi + 8]
00A9F5DA  41 BC 10 00 00 00               mov r12d, 0x10
00A9F5E0  66 45 3B C4                     cmp r8w, r12w
00A9F5E4  0F 87 76 02 00 00               ja 0x140a9f860
00A9F5EA  8B 57 04                        mov edx, dword ptr [rdi + 4]
00A9F5ED  8D 42 FF                        lea eax, [rdx - 1]
00A9F5F0  83 F8 03                        cmp eax, 3
00A9F5F3  0F 86 67 02 00 00               jbe 0x140a9f860
00A9F5F9  66 45 85 C0                     test r8w, r8w
00A9F5FD  75 0E                           jne 0x140a9f60d
00A9F5FF  85 D2                           test edx, edx
00A9F601  0F 85 59 02 00 00               jne 0x140a9f860
00A9F607  66 45 85 C0                     test r8w, r8w
00A9F60B  74 08                           je 0x140a9f615
00A9F60D  85 D2                           test edx, edx
00A9F60F  0F 84 4B 02 00 00               je 0x140a9f860
00A9F615  49 8B C8                        mov rcx, r8
00A9F618  48 C1 E1 04                     shl rcx, 4
00A9F61C  48 83 C1 0C                     add rcx, 0xc
00A9F620  8B C6                           mov eax, esi
00A9F622  48 3B C8                        cmp rcx, rax
00A9F625  0F 85 35 02 00 00               jne 0x140a9f860
00A9F62B  66 45 85 C0                     test r8w, r8w
00A9F62F  4D 8B CE                        mov r9, r14
00A9F632  74 04                           je 0x140a9f638
00A9F634  4C 8D 4F 0C                     lea r9, [rdi + 0xc]
00A9F638  8B 0F                           mov ecx, dword ptr [rdi]
00A9F63A  E8 0D D6 D1 FF                  call 0x1407bcc4c
00A9F63F  E9 7F F9 FF FF                  jmp 0x140a9efc3
00A9F644  41 83 FD 2B                     cmp r13d, 0x2b
00A9F648  0F 87 5B 01 00 00               ja 0x140a9f7a9
00A9F64E  0F 84 38 01 00 00               je 0x140a9f78c
00A9F654  41 8B C5                        mov eax, r13d
00A9F657  83 E8 26                        sub eax, 0x26
00A9F65A  0F 84 D8 00 00 00               je 0x140a9f738
00A9F660  83 E8 01                        sub eax, 1
00A9F663  0F 84 93 00 00 00               je 0x140a9f6fc
00A9F669  83 E8 01                        sub eax, 1
00A9F66C  74 59                           je 0x140a9f6c7
00A9F66E  83 E8 01                        sub eax, 1
00A9F671  74 38                           je 0x140a9f6ab
00A9F673  83 F8 01                        cmp eax, 1
00A9F676  0F 85 44 01 00 00               jne 0x140a9f7c0
00A9F67C  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00A9F684  41 83 FF 04                     cmp r15d, 4
00A9F688  72 17                           jb 0x140a9f6a1
00A9F68A  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
00A9F68F  89 07                           mov dword ptr [rdi], eax
00A9F691  C7 44 24 30 04 00 00 00         mov dword ptr [rsp + 0x30], 4
00A9F699  41 8B DE                        mov ebx, r14d
00A9F69C  E9 CC 01 00 00                  jmp 0x140a9f86d
00A9F6A1  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A9F6A6  E9 C2 01 00 00                  jmp 0x140a9f86d
00A9F6AB  83 FE 08                        cmp esi, 8
00A9F6AE  0F 82 AC 01 00 00               jb 0x140a9f860
00A9F6B4  44 8A 47 04                     mov r8b, byte ptr [rdi + 4]
00A9F6B8  8B 17                           mov edx, dword ptr [rdi]
00A9F6BA  49 8B CC                        mov rcx, r12
00A9F6BD  E8 32 45 F6 FF                  call 0x140a03bf4
00A9F6C2  E9 FC F8 FF FF                  jmp 0x140a9efc3
00A9F6C7  83 FE 08                        cmp esi, 8
00A9F6CA  0F 82 90 01 00 00               jb 0x140a9f860
00A9F6D0  41 83 FF 02                     cmp r15d, 2
00A9F6D4  0F 82 86 01 00 00               jb 0x140a9f860
00A9F6DA  48 8B D7                        mov rdx, rdi
00A9F6DD  48 8B 0F                        mov rcx, qword ptr [rdi]
00A9F6E0  E8 CB D1 D1 FF                  call 0x1407bc8b0
00A9F6E5  8B D8                           mov ebx, eax
00A9F6E7  85 C0                           test eax, eax
00A9F6E9  0F 85 76 01 00 00               jne 0x140a9f865
00A9F6EF  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
00A9F6F7  E9 69 01 00 00                  jmp 0x140a9f865
00A9F6FC  83 FE 02                        cmp esi, 2
00A9F6FF  0F 82 5B 01 00 00               jb 0x140a9f860
00A9F705  41 83 FF 08                     cmp r15d, 8
00A9F709  0F 82 51 01 00 00               jb 0x140a9f860
00A9F70F  4C 8D 47 04                     lea r8, [rdi + 4]
00A9F713  4C 8B CF                        mov r9, rdi
00A9F716  0F B7 17                        movzx edx, word ptr [rdi]
00A9F719  49 8B CC                        mov rcx, r12
00A9F71C  E8 0B D2 D1 FF                  call 0x1407bc92c
00A9F721  8B D8                           mov ebx, eax
00A9F723  85 C0                           test eax, eax
00A9F725  0F 85 3A 01 00 00               jne 0x140a9f865
00A9F72B  C7 44 24 30 08 00 00 00         mov dword ptr [rsp + 0x30], 8
00A9F733  E9 2D 01 00 00                  jmp 0x140a9f865
00A9F738  83 FE 08                        cmp esi, 8
00A9F73B  0F 82 1F 01 00 00               jb 0x140a9f860
00A9F741  40 F6 C6 07                     test sil, 7
00A9F745  0F 85 15 01 00 00               jne 0x140a9f860
00A9F74B  41 83 FF 02                     cmp r15d, 2
00A9F74F  0F 82 0B 01 00 00               jb 0x140a9f860
00A9F755  C1 EE 03                        shr esi, 3
00A9F758  66 44 89 74 24 34               mov word ptr [rsp + 0x34], r14w
00A9F75E  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00A9F763  8B D6                           mov edx, esi
00A9F765  48 8B CF                        mov rcx, rdi
00A9F768  E8 3B CE D1 FF                  call 0x1407bc5a8
00A9F76D  8B D8                           mov ebx, eax
00A9F76F  85 C0                           test eax, eax
00A9F771  0F 85 EE 00 00 00               jne 0x140a9f865
00A9F777  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
00A9F77F  0F B7 44 24 34                  movzx eax, word ptr [rsp + 0x34]
00A9F784  66 89 07                        mov word ptr [rdi], ax
00A9F787  E9 D9 00 00 00                  jmp 0x140a9f865
00A9F78C  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00A9F794  41 83 FF 04                     cmp r15d, 4
00A9F798  0F 82 03 FF FF FF               jb 0x140a9f6a1
00A9F79E  8B 05 78 F3 36 00               mov eax, dword ptr [rip + 0x36f378]
00A9F7A4  E9 E6 FE FF FF                  jmp 0x140a9f68f
00A9F7A9  41 8B C5                        mov eax, r13d
00A9F7AC  83 E8 2C                        sub eax, 0x2c
00A9F7AF  74 65                           je 0x140a9f816
00A9F7B1  83 E8 01                        sub eax, 1
00A9F7B4  74 49                           je 0x140a9f7ff
00A9F7B6  83 E8 01                        sub eax, 1
00A9F7B9  74 2D                           je 0x140a9f7e8
00A9F7BB  83 F8 01                        cmp eax, 1
00A9F7BE  74 0A                           je 0x140a9f7ca
00A9F7C0  BB 10 00 00 C0                  mov ebx, 0xc0000010
00A9F7C5  E9 9B 00 00 00                  jmp 0x140a9f865
00A9F7CA  83 FE 08                        cmp esi, 8
00A9F7CD  0F 85 8D 00 00 00               jne 0x140a9f860
00A9F7D3  41 83 FD 2F                     cmp r13d, 0x2f
00A9F7D7  41 0F 94 C0                     sete r8b
00A9F7DB  48 8B D7                        mov rdx, rdi
00A9F7DE  E8 B5 99 D1 FF                  call 0x1407b9198
00A9F7E3  E9 DB F7 FF FF                  jmp 0x140a9efc3
00A9F7E8  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00A9F7ED  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00A9F7F2  48 8B CF                        mov rcx, rdi
00A9F7F5  E8 0E F3 BA FF                  call 0x14064eb08
00A9F7FA  E9 C4 F7 FF FF                  jmp 0x140a9efc3
00A9F7FF  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00A9F804  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00A9F809  48 8B CF                        mov rcx, rdi
00A9F80C  E8 4F F1 BA FF                  call 0x14064e960
00A9F811  E9 AD F7 FF FF                  jmp 0x140a9efc3
00A9F816  83 FE 08                        cmp esi, 8
00A9F819  75 45                           jne 0x140a9f860
00A9F81B  41 83 FF 04                     cmp r15d, 4
00A9F81F  72 3F                           jb 0x140a9f860
00A9F821  0F B7 17                        movzx edx, word ptr [rdi]
00A9F824  81 FA FF FF 00 00               cmp edx, 0xffff
00A9F82A  75 09                           jne 0x140a9f835
00A9F82C  41 0F B6 94 24 98 11 00 00      movzx edx, byte ptr [r12 + 0x1198]
00A9F835  45 33 C0                        xor r8d, r8d
00A9F838  49 8B CC                        mov rcx, r12
00A9F83B  E8 E0 30 E9 FF                  call 0x140932920
00A9F840  48 8B C8                        mov rcx, rax
00A9F843  48 85 C0                        test rax, rax
00A9F846  74 18                           je 0x140a9f860
00A9F848  C7 44 24 30 04 00 00 00         mov dword ptr [rsp + 0x30], 4
00A9F850  E8 EB C0 94 FF                  call 0x1403eb940
00A9F855  89 07                           mov dword ptr [rdi], eax
00A9F857  33 D2                           xor edx, edx
00A9F859  E8 02 49 F6 FF                  call 0x140a04160
00A9F85E  EB 05                           jmp 0x140a9f865
00A9F860  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A9F865  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00A9F86D  85 DB                           test ebx, ebx
00A9F86F  78 31                           js 0x140a9f8a2
00A9F871  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00A9F875  85 C0                           test eax, eax
00A9F877  74 1B                           je 0x140a9f894
00A9F879  41 3B C7                        cmp eax, r15d
00A9F87C  77 0D                           ja 0x140a9f88b
00A9F87E  44 8B C0                        mov r8d, eax
00A9F881  48 8B D7                        mov rdx, rdi
00A9F884  E8 B7 6F C2 FF                  call 0x1406c6840
00A9F889  EB 09                           jmp 0x140a9f894
00A9F88B  BB 23 00 00 C0                  mov ebx, 0xc0000023
00A9F890  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
00A9F894  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00A9F89C  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00A9F8A0  89 01                           mov dword ptr [rcx], eax
00A9F8A2  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
00A9F8A8  75 12                           jne 0x140a9f8bc
00A9F8AA  41 8D 45 F1                     lea eax, [r13 - 0xf]
00A9F8AE  83 F8 01                        cmp eax, 1
00A9F8B1  76 1F                           jbe 0x140a9f8d2
00A9F8B3  41 8D 45 EB                     lea eax, [r13 - 0x15]
00A9F8B7  83 F8 01                        cmp eax, 1
00A9F8BA  76 16                           jbe 0x140a9f8d2
00A9F8BC  41 83 FD 2E                     cmp r13d, 0x2e
00A9F8C0  77 1E                           ja 0x140a9f8e0
00A9F8C2  48 B9 00 00 88 00 D7 41 00 00   movabs rcx, 0x41d700880000
00A9F8CC  4C 0F A3 E9                     bt rcx, r13
00A9F8D0  73 0E                           jae 0x140a9f8e0
00A9F8D2  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00A9F8DA  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00A9F8DE  89 01                           mov dword ptr [rcx], eax
00A9F8E0  EB 0B                           jmp 0x140a9f8ed
00A9F8E2  8B D8                           mov ebx, eax
00A9F8E4  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
00A9F8E8  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00A9F8ED  48 85 FF                        test rdi, rdi
00A9F8F0  74 0A                           je 0x140a9f8fc
00A9F8F2  33 D2                           xor edx, edx
00A9F8F4  48 8B CF                        mov rcx, rdi
00A9F8F7  E8 74 2F 0E 00                  call 0x140b82870
00A9F8FC  8B C3                           mov eax, ebx
00A9F8FE  48 83 C4 60                     add rsp, 0x60
00A9F902  41 5F                           pop r15
00A9F904  41 5E                           pop r14
00A9F906  41 5D                           pop r13
00A9F908  41 5C                           pop r12
00A9F90A  5F                              pop rdi
00A9F90B  5E                              pop rsi
00A9F90C  5B                              pop rbx
00A9F90D  C3                              ret
00A9F90E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtTraceControl(int a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int8 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_r14 = 0;
    v_stack_m58 = 0;
    *(unsigned int *)(v_rsp - 104) = 0;
    result = PsGetCurrentServerSiloGlobals(a1, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a4);
    v_stack_m50 = *(unsigned __int64 *)(result + 832);
    v_stack_m5C = 0;
    v_stack_m60 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00A9EE69;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a1)))) >> (31));
    v_stack_m60 = (unsigned int)(a4);
    v_r13 = (unsigned int)(a1);
    if ((unsigned __int8)(a4) == 0) { v_r13 = (unsigned int)((unsigned int)(a1)); }
    if (a2 == 0) goto loc_00A9EDF8;
    if (v_stack_p18 == 0) goto loc_00A9EE00;
    a1 = ((unsigned int)(v_stack_p18)) + (a2);
    if (a1 > 0) goto loc_00A9EDF4;
    if (a1 >= a2) goto loc_00A9EE00;
loc_00A9EDF4:
    goto loc_00A9EE00;
loc_00A9EDF8:
    v_stack_p18 = 0;
loc_00A9EE00:
    if (a4 == 0) goto loc_00A9EE1C;
    result = ProbeForWrite(a4, (unsigned int)(a5), 1, a4);
    goto loc_00A9EE24;
loc_00A9EE1C:
    v_stack_p28 = 0;
loc_00A9EE24:
    if (a6 == 0) goto loc_00A9EE4A;
    v_rbx = 0;
    if (a6 < 0) { v_rbx = a6; }
    *(unsigned int *)(v_rbx) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)));
    v_stack_p8 = (unsigned int)(v_r13);
    goto loc_00A9EE69;
loc_00A9EE4A:
    v_stack_m5C = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00A9F8ED;
loc_00A9EE69:
    if (((unsigned int)(v_r13)) > 27) goto loc_00A9EE8B;
    if (((unsigned int)(v_r13)) >= 27) goto loc_00A9EE8B;
    goto loc_00A9EF04;
loc_00A9EE8B:
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) goto loc_00A9EEA3;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_00A9EF04;
loc_00A9EEA3:
    a2 = (unsigned int)((unsigned int)((unsigned int)(a5)));
    if (((unsigned int)((unsigned int)(v_stack_p18))) > ((unsigned int)((unsigned int)(a5)))) { a2 = (unsigned int)((unsigned int)(v_stack_p18)); }
    result = ExAllocatePool2(257, a2, (unsigned int)(0x50777445ULL), a4);
    v_stack_m58 = result;
    if (result != 0) goto loc_00A9EED3;
    goto loc_00A9F8ED;
loc_00A9EED3:
    if (v_stack_p10 == 0) goto loc_00A9EF0C;
    result = memcpy(result, v_stack_p10, (unsigned int)(v_stack_p18), a4);
    goto loc_00A9EF0C;
loc_00A9EF04:
loc_00A9EF0C:
    if (((unsigned int)(v_r13)) > 25) goto loc_00A9F3BF;
    if (((unsigned int)(v_r13)) == 25) goto loc_00A9F38E;
    if (((unsigned int)(v_r13)) > 14) goto loc_00A9F135;
    if (((unsigned int)(v_r13)) == 14) goto loc_00A9F0EE;
    if (((unsigned int)(v_r13)) > 6) goto loc_00A9EF8E;
    if (((unsigned int)(v_r13)) == 6) goto loc_00A9EF54;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - (1));
    if (condition_is_equal) goto loc_00A9EF54;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9EF54;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9EF54;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9EF54;
    if (((unsigned int)(result)) != 1) goto loc_00A9F7C0;
loc_00A9EF54:
    if (((unsigned int)((unsigned int)(v_stack_p18))) < 176) goto loc_00A9F03C;
    if (((unsigned int)((unsigned int)(a5))) < 176) goto loc_00A9F03C;
    result = EtwpValidateLoggerInfo(result, v_stack_p10, (unsigned int)(v_stack_p18), a4);
    if (sign_flag) goto loc_00A9F041;
    if ((*(unsigned int *)(result)) <= ((unsigned int)((unsigned int)(v_stack_p18)))) goto loc_00A9F037;
    goto loc_00A9F865;
loc_00A9EF8E:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - (7));
    if (condition_is_equal) goto loc_00A9EF54;
    result = (unsigned int)((result) - (4));
    if (condition_is_equal) goto loc_00A9F012;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9EFCA;
    if (((unsigned int)(result)) != 1) goto loc_00A9F7C0;
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 48) goto loc_00A9F860;
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_00A9F860;
    result = WdiDispatchControl(result, v_stack_p10, (unsigned int)(v_stack_p18), a4);
loc_00A9EFC3:
    goto loc_00A9F865;
loc_00A9EFCA:
    if (((unsigned int)((unsigned int)(a5))) != 16) goto loc_00A9F860;
    result = EtwpCreateActivityId(v_stack_p20, v_stack_p10, (unsigned int)(v_stack_p18), a4);
    goto loc_00A9F86D;
loc_00A9F012:
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 96) goto loc_00A9F860;
    if (((unsigned int)((unsigned int)(a5))) != ((unsigned int)((unsigned int)(v_stack_p18)))) goto loc_00A9F860;
    result = EtwpRealtimeConnect(result, v_stack_p10, (unsigned int)(v_stack_p18), a4);
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_p18));
    goto loc_00A9F865;
loc_00A9F037:
    goto loc_00A9F041;
loc_00A9F03C:
loc_00A9F041:
    if (sign_flag) goto loc_00A9F865;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - (1));
    if (condition_is_equal) goto loc_00A9F0C0;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F0B0;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F0A3;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F096;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F089;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F07C;
    if (((unsigned int)(result)) != 1) goto loc_00A9F0E1;
    result = EtwpTransitionToRealtime(16, result, (unsigned int)(v_stack_p18), a4);
    goto loc_00A9F0DF;
loc_00A9F07C:
    result = EtwpIncrementTraceFile(16, result, (unsigned int)(v_stack_p18), a4);
    goto loc_00A9F0DF;
loc_00A9F089:
    result = EtwpFlushTrace(16, result, (unsigned int)(v_stack_p18), a4);
    goto loc_00A9F0DF;
loc_00A9F096:
    result = EtwpUpdateTrace(16, result, (unsigned int)(v_stack_p18), a4);
    goto loc_00A9F0DF;
loc_00A9F0A3:
    result = EtwpQueryTrace(16, result, (unsigned int)(v_stack_p18), a4);
    goto loc_00A9F0DF;
loc_00A9F0B0:
    a3 = 0;
    result = EtwpStopTrace(16, result, a3, a4);
    goto loc_00A9F0DF;
loc_00A9F0C0:
    a1 = (*(unsigned __int64 *)(result + 80)) & (-2);
    a1 = (a1) | (v_stack_m60);
    *(unsigned __int64 *)(result + 80) = a1;
    result = EtwpStartTrace(16, result, a3, a4);
loc_00A9F0DF:
loc_00A9F0E1:
    v_stack_m68 = 176;
    goto loc_00A9F865;
loc_00A9F0EE:
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 8) goto loc_00A9F860;
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_00A9F860;
    v_stack_m48 = (unsigned int)(*(unsigned int *)(16));
    result = EtwpRealtimeDisconnectConsumerByHandle((unsigned int)(*(unsigned int *)(16)), result, a3, a4);
    goto loc_00A9EFC3;
loc_00A9F135:
    if (((unsigned int)(v_r13)) > 20) goto loc_00A9F2A4;
    if (((unsigned int)(v_r13)) == 20) goto loc_00A9F289;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - (15));
    if (condition_is_equal) goto loc_00A9F249;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F218;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F1C1;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F19A;
    if (((unsigned int)(result)) != 1) goto loc_00A9F7C0;
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 8) goto loc_00A9F860;
    v_stack_m64 = 0;
    result = EtwpReceiveReplyDataBlock(result, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m64, a4);
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m64));
    goto loc_00A9F865;
loc_00A9F19A:
    if (((unsigned int)((unsigned int)(v_stack_p18))) < 72) goto loc_00A9F860;
    if ((*(unsigned int *)(result + 4)) != ((unsigned int)((unsigned int)(v_stack_p18)))) goto loc_00A9F860;
    result = PsGetCurrentProcessId(result, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m64, a4);
    *(unsigned int *)(result + 36) = (unsigned int)(result);
    result = EtwpSendReplyDataBlock(result, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m64, a4);
    goto loc_00A9EFC3;
loc_00A9F1C1:
    if (((unsigned int)((unsigned int)(v_stack_p18))) < 72) goto loc_00A9F860;
    if (((unsigned int)((unsigned int)(a5))) != 72) goto loc_00A9F860;
    if ((*(unsigned int *)(result + 4)) != ((unsigned int)((unsigned int)(v_stack_p18)))) goto loc_00A9F860;
    if ((*(unsigned int *)(result)) != 3) goto loc_00A9F208;
    if (((unsigned int)((unsigned int)(v_stack_p18))) < 120) goto loc_00A9F860;
    result = EtwpEnableGuid(16, result, 1, a4);
loc_00A9F1F9:
    v_stack_m68 = 72;
    goto loc_00A9F865;
loc_00A9F208:
    result = EtwpNotifyGuid(16, result, 1, a4);
    goto loc_00A9F1F9;
loc_00A9F218:
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) goto loc_00A9F860;
    if (((unsigned int)((unsigned int)(a5) - 72)) > 0xFFB8ULL) goto loc_00A9F860;
    result = EtwpReceiveNotification(result, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m60, v_stack_m68);
    goto loc_00A9EFC3;
loc_00A9F249:
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 160) goto loc_00A9F860;
    if (((unsigned int)((unsigned int)(a5) - 160)) > 0xFF60ULL) goto loc_00A9F860;
    v_stack_m78 = v_stack_m68;
    result = EtwpRegisterUMProvider(16, result, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m60);
    goto loc_00A9EFC3;
loc_00A9F289:
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) goto loc_00A9F860;
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_00A9F860;
    result = WdiUpdateSem(16, result, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m60);
    goto loc_00A9EFC3;
loc_00A9F2A4:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - (21));
    if (condition_is_equal) goto loc_00A9F36B;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F33D;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F301;
    if (((unsigned int)(result)) != 1) goto loc_00A9F7C0;
    if ((unsigned int)((unsigned int)(v_stack_p18)) != 0) goto loc_00A9F860;
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_00A9F860;
    if ((*(unsigned int *)(16 + 4344)) == 0) goto loc_00A9F2EC;
    goto loc_00A9F865;
loc_00A9F2EC:
    result = PsGetCurrentProcessId(16, result, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m60);
    *(unsigned int *)(16 + 4344) = (unsigned int)(result);
    goto loc_00A9F865;
loc_00A9F301:
    a2 = (result) >> (5);
    result = EtwpEnumerateTraceGuids(16, result, (unsigned int)((unsigned int)(a2)), v_stack_m68);
    a1 = (unsigned int)(((unsigned int)(v_stack_m68) + (unsigned int)(v_stack_m68) * 8) << (2));
    v_stack_m68 = a1;
    goto loc_00A9F865;
loc_00A9F33D:
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 16) goto loc_00A9F860;
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = EtwpGetTraceGuidInfo(v_stack_m50, result, result, v_stack_m68);
    goto loc_00A9EFC3;
loc_00A9F36B:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) >> (4));
    result = EtwpGetTraceGuidList(16, result, a3, v_stack_m68);
loc_00A9F382:
    goto loc_00A9F865;
loc_00A9F38E:
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 4) goto loc_00A9F860;
    if (((unsigned int)((unsigned int)(a5))) != ((unsigned int)((unsigned int)(v_stack_p18) + 12))) goto loc_00A9F860;
    result = EtwpQueryReferenceTime(v_stack_m50, (unsigned int)(*(unsigned int *)(result)), result, v_stack_m68);
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_p18) + 12);
    goto loc_00A9F865;
loc_00A9F3BF:
    if (((unsigned int)(v_r13)) > 37) goto loc_00A9F644;
    if (((unsigned int)(v_r13)) == 37) goto loc_00A9F5CC;
    if (((unsigned int)(v_r13)) > 32) goto loc_00A9F509;
    if (((unsigned int)(v_r13)) == 32) goto loc_00A9F4E3;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - (26));
    if (condition_is_equal) goto loc_00A9F7CA;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F498;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F457;
    result = (unsigned int)((result) - (2));
    if (condition_is_equal) goto loc_00A9F42A;
    if (((unsigned int)(result)) != 1) goto loc_00A9F7C0;
    if (((unsigned int)((unsigned int)(v_stack_p18))) != ((unsigned int)(result + 15))) goto loc_00A9F860;
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_00A9F860;
    result = EtwpUseDescriptorTypeUm(result, (unsigned int)(*(unsigned int *)(result)), result, v_stack_m68);
    goto loc_00A9EFC3;
loc_00A9F42A:
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 24) goto loc_00A9F860;
    if (((unsigned int)((unsigned int)(a5) - 120)) > 0xFF88ULL) goto loc_00A9F860;
    result = EtwpSetProviderTraitsUm(result, (unsigned int)((unsigned int)((unsigned int)(a5))), v_stack_m68, v_stack_m68);
    goto loc_00A9EFC3;
loc_00A9F457:
    if (((unsigned int)((unsigned int)(v_stack_p18))) < 8) goto loc_00A9F860;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 4))))) << (4);
    a1 = (a1) + (8);
    if (a1 != ((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) goto loc_00A9F860;
    result = (unsigned int)(-((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 4))))));
    a4 = (v_stack_m68) & (result + 8);
    result = EtwpUpdateDisallowList(result + 15, (unsigned int)(*(unsigned int *)(result)), (unsigned int)(*(unsigned int *)(result + 4)), a4);
    goto loc_00A9EFC3;
loc_00A9F498:
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 4) goto loc_00A9F860;
    v_stack_m40 = (unsigned int)(*(unsigned int *)(result + 15));
    if ((unsigned int)(*(unsigned int *)(result + 15)) == 0) goto loc_00A9F860;
    result = EtwpAddNotificationEvent((unsigned int)(*(unsigned int *)(result + 15)), v_stack_m60, (unsigned int)(*(unsigned int *)(result + 4)), a4);
    goto loc_00A9EFC3;
loc_00A9F4E3:
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) >> (4));
    v_stack_m78 = v_stack_m68;
    result = EtwpGetGuidList(result + 15, 2, result, a4);
    goto loc_00A9F382;
loc_00A9F509:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - (33));
    if (condition_is_equal) goto loc_00A9F59E;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F578;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F553;
    if (((unsigned int)(result)) != 1) goto loc_00A9F7C0;
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 8) goto loc_00A9F860;
    if (((unsigned int)((unsigned int)(a5))) != ((unsigned int)(result + 15))) goto loc_00A9F860;
    v_stack_m68 = (unsigned int)(result + 15);
    result = EtwpGetCompressionSettings(result, result, result, a4);
    goto loc_00A9EFC3;
loc_00A9F553:
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 16) goto loc_00A9F860;
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_00A9F860;
    result = EtwpSetCompressionSettings(result, result, result, a4);
    goto loc_00A9EFC3;
loc_00A9F578:
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 8) goto loc_00A9F860;
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = EtwpGetDisallowList(16, result, result, v_stack_m68);
    goto loc_00A9EFC3;
loc_00A9F59E:
    if (((unsigned int)((unsigned int)(v_stack_p18))) != 16) goto loc_00A9F860;
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = EtwpGetTraceGroupInfo(v_stack_m50, result, result, v_stack_m68);
    goto loc_00A9EFC3;
loc_00A9F5CC:
    if (((unsigned int)((unsigned int)(v_stack_p18))) < 12) goto loc_00A9F860;
    if (((unsigned __int16)(*(unsigned __int16 *)(result + 8))) > 16) goto loc_00A9F860;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)) - 1)) <= 3) goto loc_00A9F860;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 8)) != 0) goto loc_00A9F60D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 4))) != 0) goto loc_00A9F860;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 8)) == 0) goto loc_00A9F615;
loc_00A9F60D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 4))) == 0) goto loc_00A9F860;
loc_00A9F615:
    a1 = (*(unsigned __int16 *)(result + 8)) << (4);
    a1 = (a1) + (12);
    if (a1 != ((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) goto loc_00A9F860;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 8)) != 0) {
        a4 = result + 12;
    }
    result = EtwpUpdatePeriodicCaptureState((unsigned int)(*(unsigned int *)(result)), (unsigned int)(*(unsigned int *)(result + 4)), *(unsigned __int16 *)(result + 8), a4);
    goto loc_00A9EFC3;
loc_00A9F644:
    if (((unsigned int)(v_r13)) > 43) goto loc_00A9F7A9;
    if (((unsigned int)(v_r13)) == 43) goto loc_00A9F78C;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - (38));
    if (condition_is_equal) goto loc_00A9F738;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F6FC;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F6C7;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F6AB;
    if (((unsigned int)(result)) != 1) goto loc_00A9F7C0;
    if (((unsigned int)((unsigned int)(a5))) < 4) goto loc_00A9F6A1;
loc_00A9F68F:
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)(16 + 16)));
    v_stack_m68 = 4;
    goto loc_00A9F86D;
loc_00A9F6A1:
    goto loc_00A9F86D;
loc_00A9F6AB:
    if (((unsigned int)((unsigned int)(v_stack_p18))) < 8) goto loc_00A9F860;
    result = EtwpSetProviderBinaryTracking(16, (unsigned int)(*(unsigned int *)(result)), *(unsigned __int8 *)(result + 4), a4);
    goto loc_00A9EFC3;
loc_00A9F6C7:
    if (((unsigned int)((unsigned int)(v_stack_p18))) < 8) goto loc_00A9F860;
    if (((unsigned int)((unsigned int)(a5))) < 2) goto loc_00A9F860;
    result = EtwpQuerySessionDemuxObject(*(unsigned __int64 *)(result), result, *(unsigned __int8 *)(result + 4), a4);
    if ((unsigned int)(result) != 0) goto loc_00A9F865;
    v_stack_m68 = 2;
    goto loc_00A9F865;
loc_00A9F6FC:
    if (((unsigned int)((unsigned int)(v_stack_p18))) < 2) goto loc_00A9F860;
    if (((unsigned int)((unsigned int)(a5))) < 8) goto loc_00A9F860;
    result = EtwpRegisterPrivateSession(16, *(unsigned __int16 *)(result), result + 4, result);
    if ((unsigned int)(result) != 0) goto loc_00A9F865;
    v_stack_m68 = 8;
    goto loc_00A9F865;
loc_00A9F738:
    if (((unsigned int)((unsigned int)(v_stack_p18))) < 8) goto loc_00A9F860;
    if ((((unsigned __int8)((unsigned int)(v_stack_p18))) & (7)) != 0) goto loc_00A9F860;
    if (((unsigned int)((unsigned int)(a5))) < 2) goto loc_00A9F860;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_p18)) >> (3));
    v_stack_m64 = 0;
    result = EtwpGetPrivateSessionTraceHandle(result, (unsigned int)((unsigned int)(v_rsi)), v_stack_m64, result);
    if ((unsigned int)(result) != 0) goto loc_00A9F865;
    v_stack_m68 = 2;
    *(unsigned __int16 *)(result) = (unsigned __int16)(v_stack_m64);
    goto loc_00A9F865;
loc_00A9F78C:
    if (((unsigned int)((unsigned int)(a5))) < 4) goto loc_00A9F6A1;
    goto loc_00A9F68F;
loc_00A9F7A9:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - (44));
    if (condition_is_equal) goto loc_00A9F816;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F7FF;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00A9F7E8;
    if (((unsigned int)(result)) == 1) goto loc_00A9F7CA;
loc_00A9F7C0:
    goto loc_00A9F865;
loc_00A9F7CA:
    if (((unsigned int)(v_rsi)) != 8) goto loc_00A9F860;
    a3 = (((unsigned int)(v_r13)) == 47) ? 1 : 0;
    result = EtwpTrackProviderBinary(v_stack_p20, result, a3, result);
    goto loc_00A9EFC3;
loc_00A9F7E8:
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = EtwpGetPmcSessions(result, v_stack_m68, a3, result);
    goto loc_00A9EFC3;
loc_00A9F7FF:
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = EtwpGetPmcOwnership(result, v_stack_m68, a3, result);
    goto loc_00A9EFC3;
loc_00A9F816:
    if (((unsigned int)(v_rsi)) != 8) goto loc_00A9F860;
    if (((unsigned int)((unsigned int)(a5))) < 4) goto loc_00A9F860;
    if (((unsigned int)(*(unsigned __int16 *)(result))) == 0xFFFFULL) {
        a2 = *(unsigned __int8 *)(16 + 4504);
    }
    a3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(16, a2, a3, result);
    if (result == 0) goto loc_00A9F860;
    v_stack_m68 = 4;
    result = EtwpQueryUsedProcessorCount(result, a2, a3, result);
    *(unsigned int *)(result) = (unsigned int)(result);
    a2 = 0;
    result = EtwpReleaseLoggerContext(result, a2, a3, result);
    goto loc_00A9F865;
loc_00A9F860:
loc_00A9F865:
loc_00A9F86D:
    if (sign_flag) goto loc_00A9F8A2;
    if ((unsigned int)((unsigned int)(v_stack_m68)) == 0) goto loc_00A9F894;
    if (((unsigned int)((unsigned int)(v_stack_m68))) > ((unsigned int)((unsigned int)(a5)))) goto loc_00A9F88B;
    result = memcpy(v_stack_p20, result, (unsigned int)((unsigned int)((unsigned int)(v_stack_m68))), result);
    goto loc_00A9F894;
loc_00A9F88B:
    v_stack_m5C = (unsigned int)((unsigned int)(0xC0000023ULL));
loc_00A9F894:
    *(unsigned int *)(a6) = (unsigned int)((unsigned int)(v_stack_m68));
loc_00A9F8A2:
    if (((unsigned int)((unsigned int)(0xC0000023ULL))) != 0xC0000023ULL) goto loc_00A9F8BC;
    if (((unsigned int)(v_r13 - 15)) <= 1) goto loc_00A9F8D2;
    if (((unsigned int)(v_r13 - 21)) <= 1) goto loc_00A9F8D2;
loc_00A9F8BC:
    if (((unsigned int)(v_r13)) > 46) goto loc_00A9F8E0;
    result = v_r13 - 21;
    if (((unsigned int)(v_r13)) < 46) {
        a1 = a6;
        result = v_stack_m68;
        *(unsigned int *)(a1) = (unsigned int)(result);
    }
    goto loc_00A9F8ED;
loc_00A9F8ED:
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m68))), result);
    }
    v_rsp = (v_rsp) + (96);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000023ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t NtTraceControl(int32_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, void *Arg6)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint8_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    local_r14 = 0;
    v_stack_m58 = 0;
    *(uint32_t *)(local_rsp - 0x68) = 0;
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg4);
    v_stack_m50 = *(uint64_t *)(result + 0x340);
    v_stack_m5C = 0;
    v_stack_m60 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00A9EE69;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg1)))) >> (31));
    v_stack_m60 = (uint32_t)(Arg4);
    local_r13 = (uint32_t)(Arg1);
    if ((uint8_t)(Arg4) == 0) { local_r13 = (uint32_t)((uint32_t)(Arg1)); }
    if (Arg2 == 0) goto loc_00A9EDF8;
    if (v_stack_p18 == 0) goto loc_00A9EE00;
    Arg1 = ((uint32_t)(v_stack_p18)) + (Arg2);
    if (Arg1 > 0) goto loc_00A9EDF4;
    if (Arg1 >= Arg2) goto loc_00A9EE00;
loc_00A9EDF4:
    goto loc_00A9EE00;
loc_00A9EDF8:
    v_stack_p18 = 0;
loc_00A9EE00:
    if (Arg4 == 0) goto loc_00A9EE1C;
    result = ProbeForWrite(Arg4, (uint32_t)(Arg5), 1, Arg4);
    goto loc_00A9EE24;
loc_00A9EE1C:
    v_stack_p28 = 0;
loc_00A9EE24:
    if (Arg6 == NULL) goto loc_00A9EE4A;
    local_rbx = 0;
    if (Arg6 < 0) { local_rbx = Arg6; }
    *(uint32_t *)(local_rbx) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)));
    v_stack_p8 = (uint32_t)(local_r13);
    goto loc_00A9EE69;
loc_00A9EE4A:
    v_stack_m5C = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00A9F8ED;
loc_00A9EE69:
    if (((uint32_t)(local_r13)) > 27) goto loc_00A9EE8B;
    if (((uint32_t)(local_r13)) >= 27) goto loc_00A9EE8B;
    goto loc_00A9EF04;
loc_00A9EE8B:
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) goto loc_00A9EEA3;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_00A9EF04;
loc_00A9EEA3:
    Arg2 = (uint32_t)((uint32_t)((uint32_t)(Arg5)));
    if (((uint32_t)((uint32_t)(v_stack_p18))) > ((uint32_t)((uint32_t)(Arg5)))) { Arg2 = (uint32_t)((uint32_t)(v_stack_p18)); }
    result = ExAllocatePool2(257, Arg2, (uint32_t)(0x50777445ULL), Arg4);
    v_stack_m58 = result;
    if (result != 0) goto loc_00A9EED3;
    goto loc_00A9F8ED;
loc_00A9EED3:
    if (v_stack_p10 == 0) goto loc_00A9EF0C;
    result = memcpy(result, v_stack_p10, (uint32_t)(v_stack_p18), Arg4);
    goto loc_00A9EF0C;
loc_00A9EF04:
loc_00A9EF0C:
    if (((uint32_t)(local_r13)) > 25) goto loc_00A9F3BF;
    if (((uint32_t)(local_r13)) == 25) goto loc_00A9F38E;
    if (((uint32_t)(local_r13)) > 14) goto loc_00A9F135;
    if (((uint32_t)(local_r13)) == 14) goto loc_00A9F0EE;
    if (((uint32_t)(local_r13)) > 6) goto loc_00A9EF8E;
    if (((uint32_t)(local_r13)) == 6) goto loc_00A9EF54;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - (1));
    if (condition_is_equal) goto loc_00A9EF54;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9EF54;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9EF54;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9EF54;
    if (((uint32_t)(result)) != 1) goto loc_00A9F7C0;
loc_00A9EF54:
    if (((uint32_t)((uint32_t)(v_stack_p18))) < 176) goto loc_00A9F03C;
    if (((uint32_t)((uint32_t)(Arg5))) < 176) goto loc_00A9F03C;
    result = EtwpValidateLoggerInfo(result, v_stack_p10, (uint32_t)(v_stack_p18), Arg4);
    if (sign_flag) goto loc_00A9F041;
    if ((*(uint32_t *)(result)) <= ((uint32_t)((uint32_t)(v_stack_p18)))) goto loc_00A9F037;
    goto loc_00A9F865;
loc_00A9EF8E:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - (7));
    if (condition_is_equal) goto loc_00A9EF54;
    result = (uint32_t)((result) - (4));
    if (condition_is_equal) goto loc_00A9F012;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9EFCA;
    if (((uint32_t)(result)) != 1) goto loc_00A9F7C0;
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 48) goto loc_00A9F860;
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_00A9F860;
    result = WdiDispatchControl(result, v_stack_p10, (uint32_t)(v_stack_p18), Arg4);
loc_00A9EFC3:
    goto loc_00A9F865;
loc_00A9EFCA:
    if (((uint32_t)((uint32_t)(Arg5))) != 16) goto loc_00A9F860;
    result = EtwpCreateActivityId(v_stack_p20, v_stack_p10, (uint32_t)(v_stack_p18), Arg4);
    goto loc_00A9F86D;
loc_00A9F012:
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 96) goto loc_00A9F860;
    if (((uint32_t)((uint32_t)(Arg5))) != ((uint32_t)((uint32_t)(v_stack_p18)))) goto loc_00A9F860;
    result = EtwpRealtimeConnect(result, v_stack_p10, (uint32_t)(v_stack_p18), Arg4);
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_p18));
    goto loc_00A9F865;
loc_00A9F037:
    goto loc_00A9F041;
loc_00A9F03C:
loc_00A9F041:
    if (sign_flag) goto loc_00A9F865;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - (1));
    if (condition_is_equal) goto loc_00A9F0C0;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F0B0;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F0A3;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F096;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F089;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F07C;
    if (((uint32_t)(result)) != 1) goto loc_00A9F0E1;
    result = EtwpTransitionToRealtime(16, result, (uint32_t)(v_stack_p18), Arg4);
    goto loc_00A9F0DF;
loc_00A9F07C:
    result = EtwpIncrementTraceFile(16, result, (uint32_t)(v_stack_p18), Arg4);
    goto loc_00A9F0DF;
loc_00A9F089:
    result = EtwpFlushTrace(16, result, (uint32_t)(v_stack_p18), Arg4);
    goto loc_00A9F0DF;
loc_00A9F096:
    result = EtwpUpdateTrace(16, result, (uint32_t)(v_stack_p18), Arg4);
    goto loc_00A9F0DF;
loc_00A9F0A3:
    result = EtwpQueryTrace(16, result, (uint32_t)(v_stack_p18), Arg4);
    goto loc_00A9F0DF;
loc_00A9F0B0:
    Arg3 = 0;
    result = EtwpStopTrace(16, result, Arg3, Arg4);
    goto loc_00A9F0DF;
loc_00A9F0C0:
    Arg1 = (*(uint64_t *)(result + 0x50)) & (-2);
    Arg1 = (Arg1) | (v_stack_m60);
    *(uint64_t *)(result + 0x50) = Arg1;
    result = EtwpStartTrace(16, result, Arg3, Arg4);
loc_00A9F0DF:
loc_00A9F0E1:
    v_stack_m68 = 176;
    goto loc_00A9F865;
loc_00A9F0EE:
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 8) goto loc_00A9F860;
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_00A9F860;
    v_stack_m48 = (uint32_t)(*(uint32_t *)(16));
    result = EtwpRealtimeDisconnectConsumerByHandle((uint32_t)(*(uint32_t *)(16)), result, Arg3, Arg4);
    goto loc_00A9EFC3;
loc_00A9F135:
    if (((uint32_t)(local_r13)) > 20) goto loc_00A9F2A4;
    if (((uint32_t)(local_r13)) == 20) goto loc_00A9F289;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - (15));
    if (condition_is_equal) goto loc_00A9F249;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F218;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F1C1;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F19A;
    if (((uint32_t)(result)) != 1) goto loc_00A9F7C0;
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 8) goto loc_00A9F860;
    v_stack_m64 = 0;
    result = EtwpReceiveReplyDataBlock(result, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m64, Arg4);
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m64));
    goto loc_00A9F865;
loc_00A9F19A:
    if (((uint32_t)((uint32_t)(v_stack_p18))) < 72) goto loc_00A9F860;
    if ((*(uint32_t *)(result + 0x4)) != ((uint32_t)((uint32_t)(v_stack_p18)))) goto loc_00A9F860;
    result = PsGetCurrentProcessId(result, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m64, Arg4);
    *(uint32_t *)(result + 0x24) = (uint32_t)(result);
    result = EtwpSendReplyDataBlock(result, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m64, Arg4);
    goto loc_00A9EFC3;
loc_00A9F1C1:
    if (((uint32_t)((uint32_t)(v_stack_p18))) < 72) goto loc_00A9F860;
    if (((uint32_t)((uint32_t)(Arg5))) != 72) goto loc_00A9F860;
    if ((*(uint32_t *)(result + 0x4)) != ((uint32_t)((uint32_t)(v_stack_p18)))) goto loc_00A9F860;
    if ((*(uint32_t *)(result)) != 3) goto loc_00A9F208;
    if (((uint32_t)((uint32_t)(v_stack_p18))) < 120) goto loc_00A9F860;
    result = EtwpEnableGuid(16, result, 1, Arg4);
loc_00A9F1F9:
    v_stack_m68 = 72;
    goto loc_00A9F865;
loc_00A9F208:
    result = EtwpNotifyGuid(16, result, 1, Arg4);
    goto loc_00A9F1F9;
loc_00A9F218:
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) goto loc_00A9F860;
    if (((uint32_t)((uint32_t)(Arg5) - 72)) > 0xFFB8ULL) goto loc_00A9F860;
    result = EtwpReceiveNotification(result, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m60, v_stack_m68);
    goto loc_00A9EFC3;
loc_00A9F249:
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 160) goto loc_00A9F860;
    if (((uint32_t)((uint32_t)(Arg5) - 160)) > 0xFF60ULL) goto loc_00A9F860;
    v_stack_m78 = v_stack_m68;
    result = EtwpRegisterUMProvider(16, result, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m60);
    goto loc_00A9EFC3;
loc_00A9F289:
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) goto loc_00A9F860;
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_00A9F860;
    result = WdiUpdateSem(16, result, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m60);
    goto loc_00A9EFC3;
loc_00A9F2A4:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - (21));
    if (condition_is_equal) goto loc_00A9F36B;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F33D;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F301;
    if (((uint32_t)(result)) != 1) goto loc_00A9F7C0;
    if ((uint32_t)((uint32_t)(v_stack_p18)) != 0) goto loc_00A9F860;
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_00A9F860;
    if ((*(uint32_t *)(16 + 0x10F8)) == 0) goto loc_00A9F2EC;
    goto loc_00A9F865;
loc_00A9F2EC:
    result = PsGetCurrentProcessId(16, result, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m60);
    *(uint32_t *)(16 + 0x10F8) = (uint32_t)(result);
    goto loc_00A9F865;
loc_00A9F301:
    Arg2 = (result) >> (5);
    result = EtwpEnumerateTraceGuids(16, result, (uint32_t)((uint32_t)(Arg2)), v_stack_m68);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m68) + (uint32_t)(v_stack_m68) * 8) << (2));
    v_stack_m68 = Arg1;
    goto loc_00A9F865;
loc_00A9F33D:
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 16) goto loc_00A9F860;
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = EtwpGetTraceGuidInfo(v_stack_m50, result, result, v_stack_m68);
    goto loc_00A9EFC3;
loc_00A9F36B:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) >> (4));
    result = EtwpGetTraceGuidList(16, result, Arg3, v_stack_m68);
loc_00A9F382:
    goto loc_00A9F865;
loc_00A9F38E:
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 4) goto loc_00A9F860;
    if (((uint32_t)((uint32_t)(Arg5))) != ((uint32_t)((uint32_t)(v_stack_p18) + 12))) goto loc_00A9F860;
    result = EtwpQueryReferenceTime(v_stack_m50, (uint32_t)(*(uint32_t *)(result)), result, v_stack_m68);
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_p18) + 12);
    goto loc_00A9F865;
loc_00A9F3BF:
    if (((uint32_t)(local_r13)) > 37) goto loc_00A9F644;
    if (((uint32_t)(local_r13)) == 37) goto loc_00A9F5CC;
    if (((uint32_t)(local_r13)) > 32) goto loc_00A9F509;
    if (((uint32_t)(local_r13)) == 32) goto loc_00A9F4E3;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - (26));
    if (condition_is_equal) goto loc_00A9F7CA;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F498;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F457;
    result = (uint32_t)((result) - (2));
    if (condition_is_equal) goto loc_00A9F42A;
    if (((uint32_t)(result)) != 1) goto loc_00A9F7C0;
    if (((uint32_t)((uint32_t)(v_stack_p18))) != ((uint32_t)(result + 15))) goto loc_00A9F860;
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_00A9F860;
    result = EtwpUseDescriptorTypeUm(result, (uint32_t)(*(uint32_t *)(result)), result, v_stack_m68);
    goto loc_00A9EFC3;
loc_00A9F42A:
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 24) goto loc_00A9F860;
    if (((uint32_t)((uint32_t)(Arg5) - 120)) > 0xFF88ULL) goto loc_00A9F860;
    result = EtwpSetProviderTraitsUm(result, (uint32_t)((uint32_t)((uint32_t)(Arg5))), v_stack_m68, v_stack_m68);
    goto loc_00A9EFC3;
loc_00A9F457:
    if (((uint32_t)((uint32_t)(v_stack_p18))) < 8) goto loc_00A9F860;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))))) << (4);
    Arg1 = (Arg1) + (8);
    if (Arg1 != ((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) goto loc_00A9F860;
    result = (uint32_t)(-((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))))));
    Arg4 = (v_stack_m68) & (result + 8);
    result = EtwpUpdateDisallowList(result + 15, (uint32_t)(*(uint32_t *)(result)), (uint32_t)(*(uint32_t *)(result + 0x4)), Arg4);
    goto loc_00A9EFC3;
loc_00A9F498:
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 4) goto loc_00A9F860;
    v_stack_m40 = (uint32_t)(*(uint32_t *)(result + 0xF));
    if ((uint32_t)(*(uint32_t *)(result + 0xF)) == 0) goto loc_00A9F860;
    result = EtwpAddNotificationEvent((uint32_t)(*(uint32_t *)(result + 0xF)), v_stack_m60, (uint32_t)(*(uint32_t *)(result + 0x4)), Arg4);
    goto loc_00A9EFC3;
loc_00A9F4E3:
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) >> (4));
    v_stack_m78 = v_stack_m68;
    result = EtwpGetGuidList(result + 15, 2, result, Arg4);
    goto loc_00A9F382;
loc_00A9F509:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - (33));
    if (condition_is_equal) goto loc_00A9F59E;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F578;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F553;
    if (((uint32_t)(result)) != 1) goto loc_00A9F7C0;
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 8) goto loc_00A9F860;
    if (((uint32_t)((uint32_t)(Arg5))) != ((uint32_t)(result + 15))) goto loc_00A9F860;
    v_stack_m68 = (uint32_t)(result + 15);
    result = EtwpGetCompressionSettings(result, result, result, Arg4);
    goto loc_00A9EFC3;
loc_00A9F553:
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 16) goto loc_00A9F860;
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_00A9F860;
    result = EtwpSetCompressionSettings(result, result, result, Arg4);
    goto loc_00A9EFC3;
loc_00A9F578:
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 8) goto loc_00A9F860;
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = EtwpGetDisallowList(16, result, result, v_stack_m68);
    goto loc_00A9EFC3;
loc_00A9F59E:
    if (((uint32_t)((uint32_t)(v_stack_p18))) != 16) goto loc_00A9F860;
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = EtwpGetTraceGroupInfo(v_stack_m50, result, result, v_stack_m68);
    goto loc_00A9EFC3;
loc_00A9F5CC:
    if (((uint32_t)((uint32_t)(v_stack_p18))) < 12) goto loc_00A9F860;
    if (((uint16_t)(*(uint16_t *)(result + 0x8))) > 16) goto loc_00A9F860;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)) - 1)) <= 3) goto loc_00A9F860;
    if ((uint16_t)(*(uint16_t *)(result + 0x8)) != 0) goto loc_00A9F60D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))) != 0) goto loc_00A9F860;
    if ((uint16_t)(*(uint16_t *)(result + 0x8)) == 0) goto loc_00A9F615;
loc_00A9F60D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))) == 0) goto loc_00A9F860;
loc_00A9F615:
    Arg1 = (*(uint16_t *)(result + 0x8)) << (4);
    Arg1 = (Arg1) + (12);
    if (Arg1 != ((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) goto loc_00A9F860;
    if ((uint16_t)(*(uint16_t *)(result + 0x8)) != 0) {
        Arg4 = result + 12;
    }
    result = EtwpUpdatePeriodicCaptureState((uint32_t)(*(uint32_t *)(result)), (uint32_t)(*(uint32_t *)(result + 0x4)), *(uint16_t *)(result + 0x8), Arg4);
    goto loc_00A9EFC3;
loc_00A9F644:
    if (((uint32_t)(local_r13)) > 43) goto loc_00A9F7A9;
    if (((uint32_t)(local_r13)) == 43) goto loc_00A9F78C;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - (38));
    if (condition_is_equal) goto loc_00A9F738;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F6FC;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F6C7;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F6AB;
    if (((uint32_t)(result)) != 1) goto loc_00A9F7C0;
    if (((uint32_t)((uint32_t)(Arg5))) < 4) goto loc_00A9F6A1;
loc_00A9F68F:
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)(16 + 0x10)));
    v_stack_m68 = 4;
    goto loc_00A9F86D;
loc_00A9F6A1:
    goto loc_00A9F86D;
loc_00A9F6AB:
    if (((uint32_t)((uint32_t)(v_stack_p18))) < 8) goto loc_00A9F860;
    result = EtwpSetProviderBinaryTracking(16, (uint32_t)(*(uint32_t *)(result)), *(uint8_t *)(result + 0x4), Arg4);
    goto loc_00A9EFC3;
loc_00A9F6C7:
    if (((uint32_t)((uint32_t)(v_stack_p18))) < 8) goto loc_00A9F860;
    if (((uint32_t)((uint32_t)(Arg5))) < 2) goto loc_00A9F860;
    result = EtwpQuerySessionDemuxObject(*(uint64_t *)(result), result, *(uint8_t *)(result + 0x4), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00A9F865;
    v_stack_m68 = 2;
    goto loc_00A9F865;
loc_00A9F6FC:
    if (((uint32_t)((uint32_t)(v_stack_p18))) < 2) goto loc_00A9F860;
    if (((uint32_t)((uint32_t)(Arg5))) < 8) goto loc_00A9F860;
    result = EtwpRegisterPrivateSession(16, *(uint16_t *)(result), result + 4, result);
    if ((uint32_t)(result) != 0) goto loc_00A9F865;
    v_stack_m68 = 8;
    goto loc_00A9F865;
loc_00A9F738:
    if (((uint32_t)((uint32_t)(v_stack_p18))) < 8) goto loc_00A9F860;
    if ((((uint8_t)((uint32_t)(v_stack_p18))) & (7)) != 0) goto loc_00A9F860;
    if (((uint32_t)((uint32_t)(Arg5))) < 2) goto loc_00A9F860;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_p18)) >> (3));
    v_stack_m64 = 0;
    result = EtwpGetPrivateSessionTraceHandle(result, (uint32_t)((uint32_t)(local_rsi)), v_stack_m64, result);
    if ((uint32_t)(result) != 0) goto loc_00A9F865;
    v_stack_m68 = 2;
    *(uint16_t *)(result) = (uint16_t)(v_stack_m64);
    goto loc_00A9F865;
loc_00A9F78C:
    if (((uint32_t)((uint32_t)(Arg5))) < 4) goto loc_00A9F6A1;
    goto loc_00A9F68F;
loc_00A9F7A9:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - (44));
    if (condition_is_equal) goto loc_00A9F816;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F7FF;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00A9F7E8;
    if (((uint32_t)(result)) == 1) goto loc_00A9F7CA;
loc_00A9F7C0:
    goto loc_00A9F865;
loc_00A9F7CA:
    if (((uint32_t)(local_rsi)) != 8) goto loc_00A9F860;
    Arg3 = (((uint32_t)(local_r13)) == 47) ? 1 : 0;
    result = EtwpTrackProviderBinary(v_stack_p20, result, Arg3, result);
    goto loc_00A9EFC3;
loc_00A9F7E8:
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = EtwpGetPmcSessions(result, v_stack_m68, Arg3, result);
    goto loc_00A9EFC3;
loc_00A9F7FF:
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = EtwpGetPmcOwnership(result, v_stack_m68, Arg3, result);
    goto loc_00A9EFC3;
loc_00A9F816:
    if (((uint32_t)(local_rsi)) != 8) goto loc_00A9F860;
    if (((uint32_t)((uint32_t)(Arg5))) < 4) goto loc_00A9F860;
    if (((uint32_t)(*(uint16_t *)(result))) == 0xFFFFULL) {
        Arg2 = *(uint8_t *)(16 + 0x1198);
    }
    Arg3 = 0;
    result = EtwpAcquireLoggerContextByLoggerId(16, Arg2, Arg3, result);
    if (result == 0) goto loc_00A9F860;
    v_stack_m68 = 4;
    result = EtwpQueryUsedProcessorCount(result, Arg2, Arg3, result);
    *(uint32_t *)(result) = (uint32_t)(result);
    Arg2 = 0;
    result = EtwpReleaseLoggerContext(result, Arg2, Arg3, result);
    goto loc_00A9F865;
loc_00A9F860:
loc_00A9F865:
loc_00A9F86D:
    if (sign_flag) goto loc_00A9F8A2;
    if ((uint32_t)((uint32_t)(v_stack_m68)) == 0) goto loc_00A9F894;
    if (((uint32_t)((uint32_t)(v_stack_m68))) > ((uint32_t)((uint32_t)(Arg5)))) goto loc_00A9F88B;
    result = memcpy(v_stack_p20, result, (uint32_t)((uint32_t)((uint32_t)(v_stack_m68))), result);
    goto loc_00A9F894;
loc_00A9F88B:
    v_stack_m5C = (uint32_t)((uint32_t)(0xC0000023ULL));
loc_00A9F894:
    *(uint32_t *)(arg6) = (uint32_t)((uint32_t)(v_stack_m68));
loc_00A9F8A2:
    if (((uint32_t)((uint32_t)(0xC0000023ULL))) != 0xC0000023ULL) goto loc_00A9F8BC;
    if (((uint32_t)(local_r13 - 15)) <= 1) goto loc_00A9F8D2;
    if (((uint32_t)(local_r13 - 21)) <= 1) goto loc_00A9F8D2;
loc_00A9F8BC:
    if (((uint32_t)(local_r13)) > 46) goto loc_00A9F8E0;
    result = local_r13 - 21;
    if (((uint32_t)(local_r13)) < 46) {
        Arg1 = Arg6;
        result = v_stack_m68;
        *(uint32_t *)(Arg1) = (uint32_t)(result);
    }
    goto loc_00A9F8ED;
loc_00A9F8ED:
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m68))), result);
    }
    local_rsp = (local_rsp) + (96);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000023ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A9ED40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
