# MiCreatePagingFile

- RVA: `0x007FEFF4`–`0x007FFB81` (길이 `2,957` bytes)
- VA: `0x00000001407FEFF4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D8144`
- 디코드: `646`개 명령, `2,957/2,957` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **48**; 고유 호출 대상: **38**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x007FF0CE` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x007FF0D7` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x007FF133` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x007FF216` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x007FF27A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007FF28D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007FF2AD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007FF2E6` → [MiCreateSpecialPurposeMemoryPageFile](../80/MiCreateSpecialPurposeMemoryPageFile_function_0080F444.md) (function, `0x0080F444`)
- `0x007FF313` → [RtlCreateSecurityDescriptor](../9F/RtlCreateSecurityDescriptor_function_009F1DF0.md) (function, `0x009F1DF0`)
- `0x007FF32A` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x007FF338` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (function, `0x0045D270`)
- `0x007FF34F` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x007FF37D` → [RtlCreateAcl](../91/RtlCreateAcl_function_00916F00.md) (function, `0x00916F00`)
- `0x007FF3AE` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x007FF3DF` → [RtlpAddKnownAce](../92/RtlpAddKnownAce_function_00929A20.md) (function, `0x00929A20`)
- `0x007FF401` → [RtlSetDaclSecurityDescriptor](../9E/RtlSetDaclSecurityDescriptor_function_009EC210.md) (function, `0x009EC210`)
- `0x007FF4FD` → [IopCreateFile](../8A/IopCreateFile_function_008AB298.md) (function, `0x008AB298`)
- `0x007FF529` → [ZwSetSecurityObject](../../text/6B/ZwSetSecurityObject_function_006B0810.md) (function, `0x006B0810`)
- `0x007FF541` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007FF588` → [ZwSetInformationFile](../../text/6A/ZwSetInformationFile_function_006AD5B0.md) (function, `0x006AD5B0`)
- `0x007FF5DD` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x007FF5F8` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x007FF620` → [MiCheckPageFileMapping](../../text/68/MiCheckPageFileMapping_function_0068032C.md) (function, `0x0068032C`)
- `0x007FF65C` → [IopQueryXxxInformation](../8A/IopQueryXxxInformation_function_008A89D0.md) (function, `0x008A89D0`)
- `0x007FF689` → [PiPagePathSetState](../72/PiPagePathSetState_function_0072BDE0.md) (function, `0x0072BDE0`)
- `0x007FF6A3` → [FsRtlIssueFileNotificationFsctl](../71/FsRtlIssueFileNotificationFsctl_function_007161D8.md) (function, `0x007161D8`)
- `0x007FF6BF` → [MiZeroPageFileFirstPage](../80/MiZeroPageFileFirstPage_function_00800678.md) (function, `0x00800678`)
- `0x007FF6D0` → [PiPagePathSetState](../72/PiPagePathSetState_function_0072BDE0.md) (function, `0x0072BDE0`)
- `0x007FF72A` → [MiCreatePagefile](MiCreatePagefile_function_007FEC30.md) (function, `0x007FEC30`)
- `0x007FF73E` → [MiInsertPageFileInList](MiInsertPageFileInList_function_007FFF80.md) (function, `0x007FFF80`)
- `0x007FF74F` → [MiDeletePagefile](MiDeletePagefile_function_007FFB88.md) (function, `0x007FFB88`)
- `0x007FF796` → [IoInitializeCrashDump](../71/IoInitializeCrashDump_function_00719D88.md) (function, `0x00719D88`)
- `0x007FF820` → [IopCreateFile](../8A/IopCreateFile_function_008AB298.md) (function, `0x008AB298`)
- `0x007FF872` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x007FF8BA` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007FF8D3` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007FF987` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x007FF98F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007FF9B8` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x007FF9D2` → [MiReduceCommitLimits](../../text/68/MiReduceCommitLimits_function_0068CDA0.md) (function, `0x0068CDA0`)
- `0x007FF9F4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x007FFA10` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x007FFA1F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007FFA29` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007FFAB9` → [MiIncreaseCommitLimits](../../text/68/MiIncreaseCommitLimits_function_0068CADC.md) (function, `0x0068CADC`)
- `0x007FFAC3` → [MiAttemptChangePagingFileMaximum](../../text/67/MiAttemptChangePagingFileMaximum_function_0067FE7C.md) (function, `0x0067FE7C`)
- `0x007FFAE7` → [MiCheckAndUpdatePagingFileMinimum](../../text/68/MiCheckAndUpdatePagingFileMinimum_function_006802D4.md) (function, `0x006802D4`)
- `0x007FFB05` → [MiIssuePageExtendRequest](../../text/47/MiIssuePageExtendRequest_function_004752F4.md) (function, `0x004752F4`)

### Direct callers
- [NtCreatePagingFile](../80/NtCreatePagingFile_function_008008A0.md) at `0x008008C8`
- [NtManagePartition](../90/NtManagePartition_function_00902FC0.md) at `0x009032E1`

### Static image references
- `0x007FF0C7` → RVA `0x00FD9D40` (`PAGEDATA`; read)
- `0x007FF323` → RVA `0x00FD9A68` (`PAGEDATA`; read)
- `0x007FF331` → RVA `0x00E67D58` (`.data`; read)
- `0x007FF5A9` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)
- `0x007FF699` → RVA `0x0002B0A0` (`.rdata`; read)
- `0x007FF6A8` → RVA `0x00E38D00` (`.data`; read)
- `0x007FF767` → RVA `0x00E30140` (`.data`; read)
- `0x007FF79B` → RVA `0x00E30140` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x007FF0D7` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x007FF216` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x007FF27A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007FF28D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007FF2AD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007FF32A` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x007FF338` → [RtlLengthSid](../../text/45/RtlLengthSid_function_0045D270.md) (`PAGE` → `.text`)
  - `0x007FF34F` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x007FF529` → [ZwSetSecurityObject](../../text/6B/ZwSetSecurityObject_function_006B0810.md) (`PAGE` → `.text`)
  - `0x007FF541` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007FF588` → [ZwSetInformationFile](../../text/6A/ZwSetInformationFile_function_006AD5B0.md) (`PAGE` → `.text`)
  - `0x007FF5F8` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x007FF620` → [MiCheckPageFileMapping](../../text/68/MiCheckPageFileMapping_function_0068032C.md) (`PAGE` → `.text`)
  - `0x007FF8BA` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007FF8D3` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007FF987` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x007FF98F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007FF9B8` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x007FF9D2` → [MiReduceCommitLimits](../../text/68/MiReduceCommitLimits_function_0068CDA0.md) (`PAGE` → `.text`)
  - `0x007FF9F4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x007FFA1F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007FFA29` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007FFAB9` → [MiIncreaseCommitLimits](../../text/68/MiIncreaseCommitLimits_function_0068CADC.md) (`PAGE` → `.text`)
  - `0x007FFAC3` → [MiAttemptChangePagingFileMaximum](../../text/67/MiAttemptChangePagingFileMaximum_function_0067FE7C.md) (`PAGE` → `.text`)
  - `0x007FFAE7` → [MiCheckAndUpdatePagingFileMinimum](../../text/68/MiCheckAndUpdatePagingFileMinimum_function_006802D4.md) (`PAGE` → `.text`)
  - `0x007FFB05` → [MiIssuePageExtendRequest](../../text/47/MiIssuePageExtendRequest_function_004752F4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007FEFF4  4C 8B DC                        mov r11, rsp
007FEFF7  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
007FEFFB  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
007FEFFF  49 89 7B 18                     mov qword ptr [r11 + 0x18], rdi
007FF003  4D 89 63 20                     mov qword ptr [r11 + 0x20], r12
007FF007  41 55                           push r13
007FF009  41 56                           push r14
007FF00B  41 57                           push r15
007FF00D  48 81 EC 60 01 00 00            sub rsp, 0x160
007FF014  41 8A F1                        mov sil, r9b
007FF017  4D 8B F8                        mov r15, r8
007FF01A  48 8B DA                        mov rbx, rdx
007FF01D  4C 8B E1                        mov r12, rcx
007FF020  33 C0                           xor eax, eax
007FF022  0F 57 C0                        xorps xmm0, xmm0
007FF025  0F 11 84 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm0
007FF02D  41 0F 11 43 80                  movups xmmword ptr [r11 - 0x80], xmm0
007FF032  49 89 43 90                     mov qword ptr [r11 - 0x70], rax
007FF036  41 89 43 98                     mov dword ptr [r11 - 0x68], eax
007FF03A  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
007FF042  0F 57 C9                        xorps xmm1, xmm1
007FF045  0F 11 8C 24 98 00 00 00         movups xmmword ptr [rsp + 0x98], xmm1
007FF04D  33 D2                           xor edx, edx
007FF04F  49 89 93 10 FF FF FF            mov qword ptr [r11 - 0xf0], rdx
007FF056  49 89 93 58 FF FF FF            mov qword ptr [r11 - 0xa8], rdx
007FF05D  49 89 93 60 FF FF FF            mov qword ptr [r11 - 0xa0], rdx
007FF064  41 0F 11 43 A8                  movups xmmword ptr [r11 - 0x58], xmm0
007FF069  41 0F 11 43 B8                  movups xmmword ptr [r11 - 0x48], xmm0
007FF06E  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
007FF072  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
007FF07A  44 8B AC 24 A0 01 00 00         mov r13d, dword ptr [rsp + 0x1a0]
007FF082  41 F7 C5 FF FF 7F 00            test r13d, 0x7fffff
007FF089  0F 85 CA 0A 00 00               jne 0x1407ffb59
007FF08F  45 85 ED                        test r13d, r13d
007FF092  79 0D                           jns 0x1407ff0a1
007FF094  41 F7 C5 00 00 00 42            test r13d, 0x42000000
007FF09B  0F 85 B8 0A 00 00               jne 0x1407ffb59
007FF0A1  41 F7 C5 FF FF 7F FF            test r13d, 0xff7fffff
007FF0A8  0F 95 C1                        setne cl
007FF0AB  41 0F BA E5 17                  bt r13d, 0x17
007FF0B0  0F 92 C0                        setb al
007FF0B3  84 C8                           test al, cl
007FF0B5  0F 85 9E 0A 00 00               jne 0x1407ffb59
007FF0BB  40 84 F6                        test sil, sil
007FF0BE  0F 84 84 00 00 00               je 0x1407ff148
007FF0C4  40 8A D6                        mov dl, sil
007FF0C7  48 8B 0D 72 AC 7D 00            mov rcx, qword ptr [rip + 0x7dac72]
007FF0CE  E8 4D 2D 07 00                  call 0x140871e20
007FF0D3  84 C0                           test al, al
007FF0D5  74 67                           je 0x1407ff13e
007FF0D7  E8 04 72 C3 FF                  call 0x1404362e0
007FF0DC  84 C0                           test al, al
007FF0DE  75 5E                           jne 0x1407ff13e
007FF0E0  41 BE 03 00 00 00               mov r14d, 3
007FF0E6  45 84 E6                        test r14b, r12b
007FF0E9  75 48                           jne 0x1407ff133
007FF0EB  48 BF 00 00 FF FF FF 7F 00 00   movabs rdi, 0x7fffffff0000
007FF0F5  48 8B C7                        mov rax, rdi
007FF0F8  4C 3B E7                        cmp r12, rdi
007FF0FB  49 0F 42 C4                     cmovb rax, r12
007FF0FF  90                              nop
007FF100  8A 00                           mov al, byte ptr [rax]
007FF102  45 84 FE                        test r14b, r15b
007FF105  75 2C                           jne 0x1407ff133
007FF107  48 8B C7                        mov rax, rdi
007FF10A  4C 3B FF                        cmp r15, rdi
007FF10D  49 0F 42 C7                     cmovb rax, r15
007FF111  90                              nop
007FF112  8A 00                           mov al, byte ptr [rax]
007FF114  41 84 DE                        test r14b, bl
007FF117  75 1A                           jne 0x1407ff133
007FF119  48 8B C7                        mov rax, rdi
007FF11C  48 3B DF                        cmp rbx, rdi
007FF11F  48 0F 42 C3                     cmovb rax, rbx
007FF123  90                              nop
007FF124  8A 00                           mov al, byte ptr [rax]
007FF126  48 8B 03                        mov rax, qword ptr [rbx]
007FF129  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
007FF131  EB 30                           jmp 0x1407ff163
007FF133  E8 98 AE 09 00                  call 0x140899fd0
007FF138  90                              nop
007FF139  E9 20 0A 00 00                  jmp 0x1407ffb5e
007FF13E  B8 61 00 00 C0                  mov eax, 0xc0000061
007FF143  E9 16 0A 00 00                  jmp 0x1407ffb5e
007FF148  48 8B 03                        mov rax, qword ptr [rbx]
007FF14B  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
007FF153  48 BF 00 00 FF FF FF 7F 00 00   movabs rdi, 0x7fffffff0000
007FF15D  41 BE 03 00 00 00               mov r14d, 3
007FF163  48 B9 00 E0 FF FF FF 0F 00 00   movabs rcx, 0xfffffffe000
007FF16D  48 3B C1                        cmp rax, rcx
007FF170  0F 87 DC 09 00 00               ja 0x1407ffb52
007FF176  48 3D 00 00 10 00               cmp rax, 0x100000
007FF17C  0F 8C D0 09 00 00               jl 0x1407ffb52
007FF182  40 84 F6                        test sil, sil
007FF185  74 12                           je 0x1407ff199
007FF187  49 8B 1F                        mov rbx, qword ptr [r15]
007FF18A  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
007FF192  EB 10                           jmp 0x1407ff1a4
007FF194  E9 C5 09 00 00                  jmp 0x1407ffb5e
007FF199  49 8B 1F                        mov rbx, qword ptr [r15]
007FF19C  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
007FF1A4  48 3B D9                        cmp rbx, rcx
007FF1A7  0F 87 9E 09 00 00               ja 0x1407ffb4b
007FF1AD  48 3B C3                        cmp rax, rbx
007FF1B0  0F 8F 95 09 00 00               jg 0x1407ffb4b
007FF1B6  40 84 F6                        test sil, sil
007FF1B9  74 15                           je 0x1407ff1d0
007FF1BB  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
007FF1C0  F3 0F 7F 84 24 98 00 00 00      movdqu xmmword ptr [rsp + 0x98], xmm0
007FF1C9  EB 13                           jmp 0x1407ff1de
007FF1CB  E9 8E 09 00 00                  jmp 0x1407ffb5e
007FF1D0  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
007FF1D5  F3 0F 7F 84 24 98 00 00 00      movdqu xmmword ptr [rsp + 0x98], xmm0
007FF1DE  0F B7 8C 24 98 00 00 00         movzx ecx, word ptr [rsp + 0x98]
007FF1E6  66 89 8C 24 9A 00 00 00         mov word ptr [rsp + 0x9a], cx
007FF1EE  0F B7 C1                        movzx eax, cx
007FF1F1  41 BF 01 00 00 00               mov r15d, 1
007FF1F7  66 41 2B C7                     sub ax, r15w
007FF1FB  BA FF 00 00 00                  mov edx, 0xff
007FF200  66 3B C2                        cmp ax, dx
007FF203  0F 87 3B 09 00 00               ja 0x1407ffb44
007FF209  8B D1                           mov edx, ecx
007FF20B  B9 00 01 00 00                  mov ecx, 0x100
007FF210  41 B8 4D 6D 20 20               mov r8d, 0x20206d4d
007FF216  E8 25 C3 B5 FF                  call 0x14035b540
007FF21B  4C 8B E0                        mov r12, rax
007FF21E  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
007FF226  48 85 C0                        test rax, rax
007FF229  0F 84 0E 09 00 00               je 0x1407ffb3d
007FF22F  40 84 F6                        test sil, sil
007FF232  74 65                           je 0x1407ff299
007FF234  0F B7 8C 24 98 00 00 00         movzx ecx, word ptr [rsp + 0x98]
007FF23C  33 F6                           xor esi, esi
007FF23E  66 85 C9                        test cx, cx
007FF241  74 28                           je 0x1407ff26b
007FF243  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
007FF24B  4C 8D 04 0A                     lea r8, [rdx + rcx]
007FF24F  4C 3B C7                        cmp r8, rdi
007FF252  77 05                           ja 0x1407ff259
007FF254  4C 3B C2                        cmp r8, rdx
007FF257  73 12                           jae 0x1407ff26b
007FF259  8A 07                           mov al, byte ptr [rdi]
007FF25B  0F B7 8C 24 98 00 00 00         movzx ecx, word ptr [rsp + 0x98]
007FF263  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
007FF26B  44 0F B7 C1                     movzx r8d, cx
007FF26F  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
007FF277  49 8B CC                        mov rcx, r12
007FF27A  E8 C1 75 EC FF                  call 0x1406c6840
007FF27F  EB 33                           jmp 0x1407ff2b4
007FF281  8B D8                           mov ebx, eax
007FF283  33 D2                           xor edx, edx
007FF285  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
007FF28D  E8 DE 35 38 00                  call 0x140b82870
007FF292  8B C3                           mov eax, ebx
007FF294  E9 C5 08 00 00                  jmp 0x1407ffb5e
007FF299  44 0F B7 84 24 98 00 00 00      movzx r8d, word ptr [rsp + 0x98]
007FF2A2  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
007FF2AA  49 8B CC                        mov rcx, r12
007FF2AD  E8 8E 75 EC FF                  call 0x1406c6840
007FF2B2  33 F6                           xor esi, esi
007FF2B4  4C 89 A4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r12
007FF2BC  41 0F BA E5 17                  bt r13d, 0x17
007FF2C1  73 2D                           jae 0x1407ff2f0
007FF2C3  48 C1 EB 0C                     shr rbx, 0xc
007FF2C7  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
007FF2CF  48 C1 EA 0C                     shr rdx, 0xc
007FF2D3  4C 8D 8C 24 98 00 00 00         lea r9, [rsp + 0x98]
007FF2DB  44 8B C3                        mov r8d, ebx
007FF2DE  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
007FF2E6  E8 59 01 01 00                  call 0x14080f444
007FF2EB  E9 6E 08 00 00                  jmp 0x1407ffb5e
007FF2F0  48 89 B4 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rsi
007FF2F8  48 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rsi
007FF300  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
007FF308  41 8B D7                        mov edx, r15d
007FF30B  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
007FF313  E8 D8 2A 1F 00                  call 0x1409f1df0
007FF318  44 8B F8                        mov r15d, eax
007FF31B  85 C0                           test eax, eax
007FF31D  0F 88 D6 06 00 00               js 0x1407ff9f9
007FF323  48 8B 0D 3E A7 7D 00            mov rcx, qword ptr [rip + 0x7da73e]
007FF32A  E8 41 DF C5 FF                  call 0x14045d270
007FF32F  8B F8                           mov edi, eax
007FF331  48 8B 0D 20 8A 66 00            mov rcx, qword ptr [rip + 0x668a20]
007FF338  E8 33 DF C5 FF                  call 0x14045d270
007FF33D  83 C0 20                        add eax, 0x20
007FF340  03 F8                           add edi, eax
007FF342  8B D7                           mov edx, edi
007FF344  B9 00 01 00 00                  mov ecx, 0x100
007FF349  41 B8 44 61 63 6C               mov r8d, 0x6c636144
007FF34F  E8 EC C1 B5 FF                  call 0x14035b540
007FF354  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
007FF35C  48 85 C0                        test rax, rax
007FF35F  75 0E                           jne 0x1407ff36f
007FF361  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
007FF367  48 8B F8                        mov rdi, rax
007FF36A  E9 92 06 00 00                  jmp 0x1407ffa01
007FF36F  41 B8 02 00 00 00               mov r8d, 2
007FF375  8B D7                           mov edx, edi
007FF377  48 8B F8                        mov rdi, rax
007FF37A  48 8B C8                        mov rcx, rax
007FF37D  E8 7E 7B 11 00                  call 0x140916f00
007FF382  44 8B F8                        mov r15d, eax
007FF385  85 C0                           test eax, eax
007FF387  0F 88 74 06 00 00               js 0x1407ffa01
007FF38D  48 8B 05 D4 A6 7D 00            mov rax, qword ptr [rip + 0x7da6d4]
007FF394  40 88 74 24 28                  mov byte ptr [rsp + 0x28], sil
007FF399  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007FF39E  41 B9 FF 01 1F 00               mov r9d, 0x1f01ff
007FF3A4  45 33 C0                        xor r8d, r8d
007FF3A7  41 8D 50 02                     lea edx, [r8 + 2]
007FF3AB  48 8B CF                        mov rcx, rdi
007FF3AE  E8 6D A6 12 00                  call 0x140929a20
007FF3B3  44 8B F8                        mov r15d, eax
007FF3B6  85 C0                           test eax, eax
007FF3B8  0F 88 43 06 00 00               js 0x1407ffa01
007FF3BE  48 8B 05 93 89 66 00            mov rax, qword ptr [rip + 0x668993]
007FF3C5  40 88 74 24 28                  mov byte ptr [rsp + 0x28], sil
007FF3CA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007FF3CF  41 B9 FF 01 1F 00               mov r9d, 0x1f01ff
007FF3D5  45 33 C0                        xor r8d, r8d
007FF3D8  41 8D 50 02                     lea edx, [r8 + 2]
007FF3DC  48 8B CF                        mov rcx, rdi
007FF3DF  E8 3C A6 12 00                  call 0x140929a20
007FF3E4  44 8B F8                        mov r15d, eax
007FF3E7  85 C0                           test eax, eax
007FF3E9  0F 88 12 06 00 00               js 0x1407ffa01
007FF3EF  45 33 C9                        xor r9d, r9d
007FF3F2  4C 8B C7                        mov r8, rdi
007FF3F5  41 8D 51 01                     lea edx, [r9 + 1]
007FF3F9  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
007FF401  E8 0A CE 1E 00                  call 0x1409ec210
007FF406  44 8B F8                        mov r15d, eax
007FF409  85 C0                           test eax, eax
007FF40B  0F 88 F0 05 00 00               js 0x1407ffa01
007FF411  45 33 FF                        xor r15d, r15d
007FF414  45 85 ED                        test r13d, r13d
007FF417  79 05                           jns 0x1407ff41e
007FF419  41 8B F6                        mov esi, r14d
007FF41C  EB 10                           jmp 0x1407ff42e
007FF41E  41 0F BA E5 19                  bt r13d, 0x19
007FF423  41 8B F7                        mov esi, r15d
007FF426  B8 02 00 00 00                  mov eax, 2
007FF42B  0F 42 F0                        cmovb esi, eax
007FF42E  C7 84 24 E8 00 00 00 30 00 00 00  mov dword ptr [rsp + 0xe8], 0x30
007FF439  4C 89 BC 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r15
007FF441  C7 84 24 00 01 00 00 40 02 00 00  mov dword ptr [rsp + 0x100], 0x240
007FF44C  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
007FF454  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
007FF45C  48 8D 84 24 20 01 00 00         lea rax, [rsp + 0x120]
007FF464  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
007FF46C  4C 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], r15
007FF474  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
007FF47C  48 05 FF 0F 00 00               add rax, 0xfff
007FF482  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
007FF488  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
007FF490  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
007FF495  44 89 7C 24 70                  mov dword ptr [rsp + 0x70], r15d
007FF49A  C7 44 24 68 12 01 00 00         mov dword ptr [rsp + 0x68], 0x112
007FF4A2  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
007FF4A7  44 89 7C 24 58                  mov dword ptr [rsp + 0x58], r15d
007FF4AC  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
007FF4B1  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
007FF4B6  C7 44 24 40 08 90 00 00         mov dword ptr [rsp + 0x40], 0x9008
007FF4BE  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
007FF4C3  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
007FF4CB  C7 44 24 28 06 00 00 00         mov dword ptr [rsp + 0x28], 6
007FF4D3  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
007FF4DB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007FF4E0  4C 8D 8C 24 C0 00 00 00         lea r9, [rsp + 0xc0]
007FF4E8  4C 8D 84 24 E8 00 00 00         lea r8, [rsp + 0xe8]
007FF4F0  BA 03 00 14 00                  mov edx, 0x140003
007FF4F5  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
007FF4FD  E8 96 BD 0A 00                  call 0x1408ab298
007FF502  85 C0                           test eax, eax
007FF504  0F 88 A9 02 00 00               js 0x1407ff7b3
007FF50A  44 39 BC 24 C0 00 00 00         cmp dword ptr [rsp + 0xc0], r15d
007FF512  7C 28                           jl 0x1407ff53c
007FF514  4C 8D 84 24 20 01 00 00         lea r8, [rsp + 0x120]
007FF51C  BA 04 00 00 00                  mov edx, 4
007FF521  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
007FF529  E8 E2 12 EB FF                  call 0x1406b0810
007FF52E  44 8B F8                        mov r15d, eax
007FF531  85 C0                           test eax, eax
007FF533  0F 88 C8 04 00 00               js 0x1407ffa01
007FF539  45 33 FF                        xor r15d, r15d
007FF53C  33 D2                           xor edx, edx
007FF53E  48 8B CF                        mov rcx, rdi
007FF541  E8 2A 33 38 00                  call 0x140b82870
007FF546  49 8B FF                        mov rdi, r15
007FF549  4C 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r15
007FF551  44 8B BC 24 C0 00 00 00         mov r15d, dword ptr [rsp + 0xc0]
007FF559  33 F6                           xor esi, esi
007FF55B  45 85 FF                        test r15d, r15d
007FF55E  0F 88 9D 04 00 00               js 0x1407ffa01
007FF564  C7 44 24 20 14 00 00 00         mov dword ptr [rsp + 0x20], 0x14
007FF56C  44 8D 4E 08                     lea r9d, [rsi + 8]
007FF570  4C 8D 84 24 D0 00 00 00         lea r8, [rsp + 0xd0]
007FF578  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
007FF580  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
007FF588  E8 23 E0 EA FF                  call 0x1406ad5b0
007FF58D  44 8B F8                        mov r15d, eax
007FF590  85 C0                           test eax, eax
007FF592  0F 88 69 04 00 00               js 0x1407ffa01
007FF598  44 8B BC 24 C0 00 00 00         mov r15d, dword ptr [rsp + 0xc0]
007FF5A0  45 85 FF                        test r15d, r15d
007FF5A3  0F 88 58 04 00 00               js 0x1407ffa01
007FF5A9  4C 8B 05 30 75 7C 00            mov r8, qword ptr [rip + 0x7c7530]
007FF5B0  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
007FF5B5  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
007FF5BA  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
007FF5C2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007FF5C7  C7 44 24 20 4D 6D 50 66         mov dword ptr [rsp + 0x20], 0x66506d4d
007FF5CF  45 33 C9                        xor r9d, r9d
007FF5D2  41 8B D6                        mov edx, r14d
007FF5D5  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
007FF5DD  E8 6E A0 06 00                  call 0x140869650
007FF5E2  44 8B F8                        mov r15d, eax
007FF5E5  85 C0                           test eax, eax
007FF5E7  0F 88 14 04 00 00               js 0x1407ffa01
007FF5ED  48 8B BC 24 A8 00 00 00         mov rdi, qword ptr [rsp + 0xa8]
007FF5F5  48 8B CF                        mov rcx, rdi
007FF5F8  E8 23 BB A9 FF                  call 0x14029b120
007FF5FD  8B 48 48                        mov ecx, dword ptr [rax + 0x48]
007FF600  83 F9 36                        cmp ecx, 0x36
007FF603  0F 87 9F 01 00 00               ja 0x1407ff7a8
007FF609  48 B8 00 01 10 00 00 00 60 00   movabs rax, 0x60000000100100
007FF613  48 0F A3 C8                     bt rax, rcx
007FF617  0F 83 8B 01 00 00               jae 0x1407ff7a8
007FF61D  48 8B CF                        mov rcx, rdi
007FF620  E8 07 0D E8 FF                  call 0x14068032c
007FF625  44 8B F8                        mov r15d, eax
007FF628  85 C0                           test eax, eax
007FF62A  0F 88 B7 03 00 00               js 0x1407ff9e7
007FF630  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
007FF635  48 8D 84 24 A0 01 00 00         lea rax, [rsp + 0x1a0]
007FF63D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007FF642  48 8D 84 24 D8 00 00 00         lea rax, [rsp + 0xd8]
007FF64A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007FF64F  45 33 C9                        xor r9d, r9d
007FF652  8D 56 04                        lea edx, [rsi + 4]
007FF655  44 8D 46 08                     lea r8d, [rsi + 8]
007FF659  48 8B CF                        mov rcx, rdi
007FF65C  E8 6F 93 0A 00                  call 0x1408a89d0
007FF661  44 8B F8                        mov r15d, eax
007FF664  85 C0                           test eax, eax
007FF666  0F 88 7B 03 00 00               js 0x1407ff9e7
007FF66C  F6 84 24 DC 00 00 00 04         test byte ptr [rsp + 0xdc], 4
007FF674  74 0B                           je 0x1407ff681
007FF676  41 BF 64 01 00 C0               mov r15d, 0xc0000164
007FF67C  E9 66 03 00 00                  jmp 0x1407ff9e7
007FF681  BA 01 00 00 00                  mov edx, 1
007FF686  48 8B CF                        mov rcx, rdi
007FF689  E8 52 C7 F2 FF                  call 0x14072bde0
007FF68E  44 8B F8                        mov r15d, eax
007FF691  85 C0                           test eax, eax
007FF693  0F 88 4E 03 00 00               js 0x1407ff9e7
007FF699  4C 8D 05 00 BA 82 FF            lea r8, [rip - 0x7d4600]
007FF6A0  48 8B CF                        mov rcx, rdi
007FF6A3  E8 30 6B F1 FF                  call 0x1407161d8
007FF6A8  48 8D 05 51 96 63 00            lea rax, [rip + 0x639651]
007FF6AF  48 8B B4 24 A8 01 00 00         mov rsi, qword ptr [rsp + 0x1a8]
007FF6B7  48 3B F0                        cmp rsi, rax
007FF6BA  75 1E                           jne 0x1407ff6da
007FF6BC  48 8B CF                        mov rcx, rdi
007FF6BF  E8 B4 0F 00 00                  call 0x140800678
007FF6C4  44 8B F8                        mov r15d, eax
007FF6C7  85 C0                           test eax, eax
007FF6C9  79 0F                           jns 0x1407ff6da
007FF6CB  33 D2                           xor edx, edx
007FF6CD  48 8B CF                        mov rcx, rdi
007FF6D0  E8 0B C7 F2 FF                  call 0x14072bde0
007FF6D5  E9 0D 03 00 00                  jmp 0x1407ff9e7
007FF6DA  48 8B C3                        mov rax, rbx
007FF6DD  48 99                           cqo
007FF6DF  41 B8 00 10 00 00               mov r8d, 0x1000
007FF6E5  49 F7 F8                        idiv r8
007FF6E8  48 8B C8                        mov rcx, rax
007FF6EB  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
007FF6F3  48 99                           cqo
007FF6F5  49 F7 F8                        idiv r8
007FF6F8  4C 8B C8                        mov r9, rax
007FF6FB  41 BF 01 00 00 00               mov r15d, 1
007FF701  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
007FF706  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
007FF70B  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
007FF713  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007FF718  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
007FF71C  4C 8B 84 24 80 00 00 00         mov r8, qword ptr [rsp + 0x80]
007FF724  48 8B D7                        mov rdx, rdi
007FF727  48 8B CE                        mov rcx, rsi
007FF72A  E8 01 F5 FF FF                  call 0x1407fec30
007FF72F  48 8B D8                        mov rbx, rax
007FF732  48 85 C0                        test rax, rax
007FF735  0F 84 02 04 00 00               je 0x1407ffb3d
007FF73B  48 8B C8                        mov rcx, rax
007FF73E  E8 3D 08 00 00                  call 0x1407fff80
007FF743  8B F8                           mov edi, eax
007FF745  85 C0                           test eax, eax
007FF747  79 12                           jns 0x1407ff75b
007FF749  41 8B D7                        mov edx, r15d
007FF74C  48 8B CB                        mov rcx, rbx
007FF74F  E8 34 04 00 00                  call 0x1407ffb88
007FF754  8B C7                           mov eax, edi
007FF756  E9 03 04 00 00                  jmp 0x1407ffb5e
007FF75B  48 8D 05 9E 95 63 00            lea rax, [rip + 0x63959e]
007FF762  48 3B F0                        cmp rsi, rax
007FF765  75 3A                           jne 0x1407ff7a1
007FF767  80 3D D2 09 63 00 00            cmp byte ptr [rip + 0x6309d2], 0
007FF76E  75 31                           jne 0x1407ff7a1
007FF770  F6 83 AC 00 00 00 10            test byte ptr [rbx + 0xac], 0x10
007FF777  75 28                           jne 0x1407ff7a1
007FF779  0F 10 43 40                     movups xmm0, xmmword ptr [rbx + 0x40]
007FF77D  F3 0F 7F 84 24 50 01 00 00      movdqu xmmword ptr [rsp + 0x150], xmm0
007FF786  48 8D 94 24 50 01 00 00         lea rdx, [rsp + 0x150]
007FF78E  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
007FF796  E8 ED A5 F1 FF                  call 0x140719d88
007FF79B  88 05 9F 09 63 00               mov byte ptr [rip + 0x63099f], al
007FF7A1  33 C0                           xor eax, eax
007FF7A3  E9 B6 03 00 00                  jmp 0x1407ffb5e
007FF7A8  41 BF 4F 01 00 C0               mov r15d, 0xc000014f
007FF7AE  E9 34 02 00 00                  jmp 0x1407ff9e7
007FF7B3  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
007FF7B8  44 89 7C 24 70                  mov dword ptr [rsp + 0x70], r15d
007FF7BD  C7 44 24 68 12 01 00 00         mov dword ptr [rsp + 0x68], 0x112
007FF7C5  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
007FF7CA  44 89 7C 24 58                  mov dword ptr [rsp + 0x58], r15d
007FF7CF  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
007FF7D4  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
007FF7D9  C7 44 24 40 08 80 00 00         mov dword ptr [rsp + 0x40], 0x8008
007FF7E1  C7 44 24 38 01 00 00 00         mov dword ptr [rsp + 0x38], 1
007FF7E9  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
007FF7EE  C7 44 24 28 06 00 00 00         mov dword ptr [rsp + 0x28], 6
007FF7F6  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
007FF7FE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007FF803  4C 8D 8C 24 C0 00 00 00         lea r9, [rsp + 0xc0]
007FF80B  4C 8D 84 24 E8 00 00 00         lea r8, [rsp + 0xe8]
007FF813  BA 02 00 10 00                  mov edx, 0x100002
007FF818  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
007FF820  E8 73 BA 0A 00                  call 0x1408ab298
007FF825  44 8B F8                        mov r15d, eax
007FF828  45 33 ED                        xor r13d, r13d
007FF82B  85 C0                           test eax, eax
007FF82D  79 0F                           jns 0x1407ff83e
007FF82F  33 F6                           xor esi, esi
007FF831  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
007FF839  E9 D7 01 00 00                  jmp 0x1407ffa15
007FF83E  4C 8B 05 9B 72 7C 00            mov r8, qword ptr [rip + 0x7c729b]
007FF845  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
007FF84A  4C 89 6C 24 30                  mov qword ptr [rsp + 0x30], r13
007FF84F  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
007FF857  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007FF85C  C7 44 24 20 4D 6D 50 66         mov dword ptr [rsp + 0x20], 0x66506d4d
007FF864  45 33 C9                        xor r9d, r9d
007FF867  41 8B D6                        mov edx, r14d
007FF86A  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
007FF872  E8 D9 9D 06 00                  call 0x140869650
007FF877  44 8B F8                        mov r15d, eax
007FF87A  85 C0                           test eax, eax
007FF87C  0F 88 7F 01 00 00               js 0x1407ffa01
007FF882  4D 8B E5                        mov r12, r13
007FF885  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007FF88E  48 89 84 24 18 01 00 00         mov qword ptr [rsp + 0x118], rax
007FF896  49 83 CE FF                     or r14, 0xffffffffffffffff
007FF89A  66 44 01 B0 E6 01 00 00         add word ptr [rax + 0x1e6], r14w
007FF8A2  90                              nop
007FF8A3  48 8B 9C 24 A8 01 00 00         mov rbx, qword ptr [rsp + 0x1a8]
007FF8AB  48 81 C3 40 04 00 00            add rbx, 0x440
007FF8B2  45 33 C0                        xor r8d, r8d
007FF8B5  33 D2                           xor edx, edx
007FF8B7  48 8B CB                        mov rcx, rbx
007FF8BA  E8 71 09 A1 FF                  call 0x140210230
007FF8BF  48 8B F8                        mov rdi, rax
007FF8C2  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
007FF8C8  73 0E                           jae 0x1407ff8d8
007FF8CA  4C 8B C3                        mov r8, rbx
007FF8CD  48 8B D0                        mov rdx, rax
007FF8D0  48 8B CB                        mov rcx, rbx
007FF8D3  E8 B8 03 A1 FF                  call 0x14020fc90
007FF8D8  41 BB 01 00 00 00               mov r11d, 1
007FF8DE  48 85 FF                        test rdi, rdi
007FF8E1  74 04                           je 0x1407ff8e7
007FF8E3  44 88 5F 0A                     mov byte ptr [rdi + 0xa], r11b
007FF8E7  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
007FF8EF  44 8B 89 58 48 00 00            mov r9d, dword ptr [rcx + 0x4858]
007FF8F6  4C 8B 94 24 A8 00 00 00         mov r10, qword ptr [rsp + 0xa8]
007FF8FE  45 3B E9                        cmp r13d, r9d
007FF901  0F 83 32 01 00 00               jae 0x1407ffa39
007FF907  41 8B C5                        mov eax, r13d
007FF90A  48 8B 94 C1 60 48 00 00         mov rdx, qword ptr [rcx + rax*8 + 0x4860]
007FF912  44 0F B7 82 AC 00 00 00         movzx r8d, word ptr [rdx + 0xac]
007FF91A  B8 40 08 00 00                  mov eax, 0x840
007FF91F  66 44 85 C0                     test ax, r8w
007FF923  75 16                           jne 0x1407ff93b
007FF925  48 8B 4A 18                     mov rcx, qword ptr [rdx + 0x18]
007FF929  49 8B 42 28                     mov rax, qword ptr [r10 + 0x28]
007FF92D  48 39 41 28                     cmp qword ptr [rcx + 0x28], rax
007FF931  74 0D                           je 0x1407ff940
007FF933  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
007FF93B  45 03 EB                        add r13d, r11d
007FF93E  EB BE                           jmp 0x1407ff8fe
007FF940  41 0F B7 C8                     movzx ecx, r8w
007FF944  66 F7 D1                        not cx
007FF947  C1 E9 04                        shr ecx, 4
007FF94A  41 23 CB                        and ecx, r11d
007FF94D  8B C6                           mov eax, esi
007FF94F  F7 D0                           not eax
007FF951  41 23 C3                        and eax, r11d
007FF954  3A C8                           cmp cl, al
007FF956  0F 84 DA 00 00 00               je 0x1407ffa36
007FF95C  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
007FF962  B9 02 00 00 00                  mov ecx, 2
007FF967  48 8B BC 24 A8 01 00 00         mov rdi, qword ptr [rsp + 0x1a8]
007FF96F  48 8D 9F 40 04 00 00            lea rbx, [rdi + 0x440]
007FF976  F0 4C 0F C1 33                  lock xadd qword ptr [rbx], r14
007FF97B  41 80 E6 06                     and r14b, 6
007FF97F  44 3A F1                        cmp r14b, cl
007FF982  75 08                           jne 0x1407ff98c
007FF984  48 8B CB                        mov rcx, rbx
007FF987  E8 44 64 A6 FF                  call 0x140265dd0
007FF98C  48 8B CB                        mov rcx, rbx
007FF98F  E8 6C 1C AE FF                  call 0x1402e1600
007FF994  90                              nop
007FF995  48 8B 8C 24 18 01 00 00         mov rcx, qword ptr [rsp + 0x118]
007FF99D  BA 01 00 00 00                  mov edx, 1
007FF9A2  66 01 91 E6 01 00 00            add word ptr [rcx + 0x1e6], dx
007FF9A9  75 12                           jne 0x1407ff9bd
007FF9AB  90                              nop
007FF9AC  48 8D 81 98 00 00 00            lea rax, [rcx + 0x98]
007FF9B3  48 39 00                        cmp qword ptr [rax], rax
007FF9B6  74 05                           je 0x1407ff9bd
007FF9B8  E8 C3 32 AE FF                  call 0x1402e2c80
007FF9BD  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
007FF9C5  48 85 C0                        test rax, rax
007FF9C8  74 0D                           je 0x1407ff9d7
007FF9CA  4C 8B C0                        mov r8, rax
007FF9CD  33 D2                           xor edx, edx
007FF9CF  48 8B CF                        mov rcx, rdi
007FF9D2  E8 C9 D3 E8 FF                  call 0x14068cda0
007FF9D7  4C 8B A4 24 B8 00 00 00         mov r12, qword ptr [rsp + 0xb8]
007FF9DF  48 8B BC 24 A8 00 00 00         mov rdi, qword ptr [rsp + 0xa8]
007FF9E7  48 85 FF                        test rdi, rdi
007FF9EA  74 0D                           je 0x1407ff9f9
007FF9EC  BA 4D 6D 50 66                  mov edx, 0x66506d4d
007FF9F1  48 8B CF                        mov rcx, rdi
007FF9F4  E8 E7 7E AF FF                  call 0x1402f78e0
007FF9F9  48 8B BC 24 90 00 00 00         mov rdi, qword ptr [rsp + 0x90]
007FFA01  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
007FFA09  48 85 C9                        test rcx, rcx
007FFA0C  74 07                           je 0x1407ffa15
007FFA0E  33 D2                           xor edx, edx
007FFA10  E8 5B 1E 0A 00                  call 0x1408a1870
007FFA15  48 85 FF                        test rdi, rdi
007FFA18  74 0A                           je 0x1407ffa24
007FFA1A  33 D2                           xor edx, edx
007FFA1C  48 8B CF                        mov rcx, rdi
007FFA1F  E8 4C 2E 38 00                  call 0x140b82870
007FFA24  33 D2                           xor edx, edx
007FFA26  49 8B CC                        mov rcx, r12
007FFA29  E8 42 2E 38 00                  call 0x140b82870
007FFA2E  41 8B C7                        mov eax, r15d
007FFA31  E9 28 01 00 00                  jmp 0x1407ffb5e
007FFA36  4C 8B E2                        mov r12, rdx
007FFA39  33 D2                           xor edx, edx
007FFA3B  4D 85 E4                        test r12, r12
007FFA3E  75 0B                           jne 0x1407ffa4b
007FFA40  41 BF 25 02 00 C0               mov r15d, 0xc0000225
007FFA46  E9 17 FF FF FF                  jmp 0x1407ff962
007FFA4B  48 8B BC 24 B0 00 00 00         mov rdi, qword ptr [rsp + 0xb0]
007FFA53  48 C1 EF 0C                     shr rdi, 0xc
007FFA57  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
007FFA5F  48 C1 EB 0C                     shr rbx, 0xc
007FFA63  41 39 5C 24 08                  cmp dword ptr [r12 + 8], ebx
007FFA68  76 0B                           jbe 0x1407ffa75
007FFA6A  41 BF F0 00 00 C0               mov r15d, 0xc00000f0
007FFA70  E9 ED FE FF FF                  jmp 0x1407ff962
007FFA75  41 8B 4C 24 04                  mov ecx, dword ptr [r12 + 4]
007FFA7A  3B CF                           cmp ecx, edi
007FFA7C  76 0B                           jbe 0x1407ffa89
007FFA7E  41 BF F1 00 00 C0               mov r15d, 0xc00000f1
007FFA84  E9 D9 FE FF FF                  jmp 0x1407ff962
007FFA89  73 48                           jae 0x1407ffad3
007FFA8B  41 F6 84 24 AC 00 00 00 10      test byte ptr [r12 + 0xac], 0x10
007FFA94  75 28                           jne 0x1407ffabe
007FFA96  8B C7                           mov eax, edi
007FFA98  2B C1                           sub eax, ecx
007FFA9A  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
007FFAA2  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
007FFAA7  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
007FFAAB  45 33 C9                        xor r9d, r9d
007FFAAE  44 8B C0                        mov r8d, eax
007FFAB1  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
007FFAB9  E8 1E D0 E8 FF                  call 0x14068cadc
007FFABE  8B D7                           mov edx, edi
007FFAC0  49 8B CC                        mov rcx, r12
007FFAC3  E8 B4 03 E8 FF                  call 0x14067fe7c
007FFAC8  44 8B F8                        mov r15d, eax
007FFACB  85 C0                           test eax, eax
007FFACD  0F 88 8F FE FF FF               js 0x1407ff962
007FFAD3  41 3B 5C 24 08                  cmp ebx, dword ptr [r12 + 8]
007FFAD8  76 45                           jbe 0x1407ffb1f
007FFADA  41 8B 0C 24                     mov ecx, dword ptr [r12]
007FFADE  8B D3                           mov edx, ebx
007FFAE0  3B D9                           cmp ebx, ecx
007FFAE2  77 0E                           ja 0x1407ffaf2
007FFAE4  49 8B CC                        mov rcx, r12
007FFAE7  E8 E8 07 E8 FF                  call 0x1406802d4
007FFAEC  85 C0                           test eax, eax
007FFAEE  74 EA                           je 0x1407ffada
007FFAF0  EB 2D                           jmp 0x1407ffb1f
007FFAF2  2B D1                           sub edx, ecx
007FFAF4  45 8B CD                        mov r9d, r13d
007FFAF7  41 B8 01 00 00 00               mov r8d, 1
007FFAFD  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
007FFB05  E8 EA 57 C7 FF                  call 0x1404752f4
007FFB0A  41 8B C7                        mov eax, r15d
007FFB0D  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
007FFB13  41 39 5C 24 08                  cmp dword ptr [r12 + 8], ebx
007FFB18  41 0F 42 C7                     cmovb eax, r15d
007FFB1C  44 8B F8                        mov r15d, eax
007FFB1F  B9 02 00 00 00                  mov ecx, 2
007FFB24  3B F1                           cmp esi, ecx
007FFB26  0F 82 3B FE FF FF               jb 0x1407ff967
007FFB2C  8D 41 7E                        lea eax, [rcx + 0x7e]
007FFB2F  66 41 09 84 24 AC 00 00 00      or word ptr [r12 + 0xac], ax
007FFB38  E9 2A FE FF FF                  jmp 0x1407ff967
007FFB3D  B8 9A 00 00 C0                  mov eax, 0xc000009a
007FFB42  EB 1A                           jmp 0x1407ffb5e
007FFB44  B8 33 00 00 C0                  mov eax, 0xc0000033
007FFB49  EB 13                           jmp 0x1407ffb5e
007FFB4B  B8 F1 00 00 C0                  mov eax, 0xc00000f1
007FFB50  EB 0C                           jmp 0x1407ffb5e
007FFB52  B8 F0 00 00 C0                  mov eax, 0xc00000f0
007FFB57  EB 05                           jmp 0x1407ffb5e
007FFB59  B8 F2 00 00 C0                  mov eax, 0xc00000f2
007FFB5E  4C 8D 9C 24 60 01 00 00         lea r11, [rsp + 0x160]
007FFB66  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
007FFB6A  49 8B 73 28                     mov rsi, qword ptr [r11 + 0x28]
007FFB6E  49 8B 7B 30                     mov rdi, qword ptr [r11 + 0x30]
007FFB72  4D 8B 63 38                     mov r12, qword ptr [r11 + 0x38]
007FFB76  49 8B E3                        mov rsp, r11
007FFB79  41 5F                           pop r15
007FFB7B  41 5E                           pop r14
007FFB7D  41 5D                           pop r13
007FFB7F  C3                              ret
007FFB80  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCreatePagingFile(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned int v_stack_m140;
    unsigned int v_stack_m148;
    unsigned __int8 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int8 v_stack_m9C;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int16 v_stack_mDE;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r12;
    v_rsp = (v_rsp) - (352);
    result = 0;
    v_stack_m90 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 128) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    *(unsigned int *)(v_rsp - 104) = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 240) = 0;
    *(unsigned __int64 *)(v_rsp - 168) = 0;
    *(unsigned __int64 *)(v_rsp - 160) = 0;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56) = 0;
    v_stack_mE8 = 0;
    if ((((unsigned int)((unsigned int)(a5))) & (0x7FFFFFULL)) != 0) goto loc_007FFB59;
    if (!sign_flag) goto loc_007FF0A1;
    if ((((unsigned int)((unsigned int)(a5))) & (0x42000000ULL)) != 0) goto loc_007FFB59;
loc_007FF0A1:
    a1 = ((((unsigned int)((unsigned int)(a5))) & (0xFF7FFFFFULL)) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_007FFB59;
    if (a4 == 0) goto loc_007FF148;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 8236146), a4, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_007FF13E;
    result = PsIsCurrentThreadInServerSilo(*(unsigned __int64 *)(v_rip + 8236146), a4, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_007FF13E;
    if (((3) & ((unsigned __int8)(a1))) != 0) goto loc_007FF133;
    result = v_rdi;
    if (a1 < v_rdi) { result = a1; }
    if (((3) & ((unsigned __int8)(a3))) != 0) goto loc_007FF133;
    result = v_rdi;
    if (a3 < v_rdi) { result = a3; }
    if (((3) & (0)) != 0) goto loc_007FF133;
    result = v_rdi;
    if (0 < v_rdi) { result = 0; }
    v_stack_mF0 = *(unsigned __int64 *)(a2);
    goto loc_007FF163;
loc_007FF133:
    result = ExRaiseDatatypeMisalignment(*(unsigned __int64 *)(v_rip + 8236146), a4, a3, a4);
    goto loc_007FFB5E;
loc_007FF13E:
    goto loc_007FFB5E;
loc_007FF148:
    v_stack_mF0 = *(unsigned __int64 *)(a2);
loc_007FF163:
    if ((*(unsigned __int64 *)(a2)) > (*(unsigned __int64 *)(v_rip + 8236146))) goto loc_007FFB52;
    if ((*(unsigned __int64 *)(a2)) < 0x100000ULL) goto loc_007FFB52;
    if (a4 == 0) goto loc_007FF199;
    v_stack_mC8 = *(unsigned __int64 *)(a3);
    goto loc_007FF1A4;
loc_007FF199:
    v_stack_mC8 = *(unsigned __int64 *)(a3);
loc_007FF1A4:
    if ((*(unsigned __int64 *)(a3)) > (*(unsigned __int64 *)(v_rip + 8236146))) goto loc_007FFB4B;
    if ((*(unsigned __int64 *)(a2)) > (*(unsigned __int64 *)(a3))) goto loc_007FFB4B;
    if (a4 == 0) goto loc_007FF1D0;
    v_stack_mE0 = v_xmm0;
    goto loc_007FF1DE;
loc_007FF1D0:
    v_stack_mE0 = v_xmm0;
loc_007FF1DE:
    v_stack_mDE = (unsigned __int16)(v_stack_mE0);
    result = (unsigned __int16)(((unsigned __int16)(v_stack_mE0)) - (1));
    if (((unsigned __int16)(result)) > 255) goto loc_007FFB44;
    result = MiAllocatePool(256, (unsigned int)((unsigned int)(v_stack_mE0)), (unsigned int)(0x20206D4DULL), a4);
    v_stack_mC0 = result;
    if (result == 0) goto loc_007FFB3D;
    if (a4 == 0) goto loc_007FF299;
    v_rsi = 0;
    if ((unsigned __int16)(v_stack_mE0) == 0) goto loc_007FF26B;
    if ((v_stack_mD8 + v_stack_mE0 * 1) > v_rdi) goto loc_007FF259;
    v_rbx = *(unsigned __int64 *)(a3);
    if ((v_stack_mD8 + v_stack_mE0 * 1) < v_stack_mD8) {
        result = *(unsigned __int8 *)(v_rdi);
        a1 = v_stack_mE0;
        v_rbx = v_stack_mC8;
    }
    result = memcpy(result, v_stack_mD8, (unsigned __int16)(a1), a4);
    goto loc_007FF2B4;
loc_007FF299:
    result = memcpy(result, v_stack_mD8, v_stack_mE0, a4);
    v_rsi = 0;
loc_007FF2B4:
    v_stack_mD8 = result;
    if (condition_is_above_or_equal) goto loc_007FF2F0;
    v_rbx = (v_rbx) >> (12);
    a2 = (v_stack_mF0) >> (12);
    result = MiCreateSpecialPurposeMemoryPageFile(a6, a2, (unsigned int)((unsigned int)(v_rbx)), v_stack_mE0);
    goto loc_007FFB5E;
loc_007FF2F0:
    v_stack_m98 = 0;
    v_stack_mD0 = 0;
    v_stack_mF8 = 0;
    result = RtlCreateSecurityDescriptor(v_stack_m58, 1, (unsigned int)((unsigned int)(v_rbx)), v_stack_mE0);
    if (sign_flag) goto loc_007FF9F9;
    result = RtlLengthSid(*(unsigned __int64 *)(v_rip + 8234814), 1, (unsigned int)((unsigned int)(v_rbx)), v_stack_mE0);
    result = RtlLengthSid(*(unsigned __int64 *)(v_rip + 6720032), 1, (unsigned int)((unsigned int)(v_rbx)), v_stack_mE0);
    result = (unsigned int)((result) + (32));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(result))) + ((unsigned int)(result)));
    result = MiAllocatePool(256, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x6C636144ULL), v_stack_mE0);
    v_stack_mE8 = result;
    if (result != 0) goto loc_007FF36F;
    goto loc_007FFA01;
loc_007FF36F:
    result = RtlCreateAcl(result, (unsigned int)((unsigned int)(result)), 2, v_stack_mE0);
    if (sign_flag) goto loc_007FFA01;
    v_stack_m150 = 0;
    v_stack_m158 = *(unsigned __int64 *)(v_rip + 8234708);
    a3 = 0;
    result = RtlpAddKnownAce(result, a3 + 2, a3, (unsigned int)(0x1F01FFULL));
    if (sign_flag) goto loc_007FFA01;
    v_stack_m150 = 0;
    v_stack_m158 = *(unsigned __int64 *)(v_rip + 6719891);
    a3 = 0;
    result = RtlpAddKnownAce(result, a3 + 2, a3, (unsigned int)(0x1F01FFULL));
    if (sign_flag) goto loc_007FFA01;
    a4 = 0;
    result = RtlSetDaclSecurityDescriptor(v_stack_m58, a4 + 1, result, a4);
    if (sign_flag) goto loc_007FFA01;
    v_r15 = 0;
    if (!sign_flag) goto loc_007FF41E;
    goto loc_007FF42E;
loc_007FF41E:
    v_rsi = 0;
    if (condition_is_below) { v_rsi = 2; }
loc_007FF42E:
    v_stack_m90 = 48;
    v_stack_m88 = 0;
    v_stack_m78 = 576;
    v_stack_m80 = v_stack_mE0;
    v_stack_m70 = v_stack_m58;
    v_stack_m68 = 0;
    result = (v_stack_mF0) + (0xFFFULL);
    result = (result) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_mA8 = result;
    v_stack_m100 = 0;
    v_stack_m108 = 0;
    v_stack_m110 = 274;
    v_stack_m118 = 0;
    v_stack_m120 = 0;
    v_stack_m128 = 0;
    v_stack_m130 = 0;
    v_stack_m138 = 0x9008ULL;
    v_stack_m140 = 0;
    v_stack_m148 = 2;
    v_stack_m150 = 6;
    v_stack_m158 = v_stack_mF0;
    result = IopCreateFile(v_stack_mF8, (unsigned int)(0x140003ULL), v_stack_m90, v_stack_mB8);
    if (sign_flag) goto loc_007FF7B3;
    if (v_stack_mB8 < 0) goto loc_007FF53C;
    result = ZwSetSecurityObject(v_stack_mF8, 4, v_stack_m58, v_stack_mB8);
    if (sign_flag) goto loc_007FFA01;
    v_r15 = 0;
loc_007FF53C:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_m58, v_stack_mB8);
    v_stack_mE8 = 0;
    v_rsi = 0;
    if (sign_flag) goto loc_007FFA01;
    v_stack_m158 = 20;
    result = ZwSetInformationFile(v_stack_mF8, v_stack_mB8, v_stack_mA8, v_rsi + 8);
    if (sign_flag) goto loc_007FFA01;
    if (sign_flag) goto loc_007FFA01;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    v_stack_m150 = v_stack_mD0;
    v_stack_m158 = 0x66506D4DULL;
    a4 = 0;
    result = ObpReferenceObjectByHandleWithTag(v_stack_mF8, 3, *(unsigned __int64 *)(v_rip + 8156464), a4);
    if (sign_flag) goto loc_007FFA01;
    result = IoGetRelatedDeviceObject(v_stack_mD0, 3, *(unsigned __int64 *)(v_rip + 8156464), a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 72)))) > 54) goto loc_007FF7A8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 72)))) >= 54) goto loc_007FF7A8;
    result = MiCheckPageFileMapping(v_stack_mD0, 3, *(unsigned __int64 *)(v_rip + 8156464), a4);
    if (sign_flag) goto loc_007FF9E7;
    v_stack_m148 = 0;
    v_stack_m150 = a5;
    v_stack_m158 = v_stack_mA0;
    a4 = 0;
    result = IopQueryXxxInformation(v_stack_mD0, v_rsi + 4, v_rsi + 8, a4);
    if (sign_flag) goto loc_007FF9E7;
    if (((v_stack_m9C) & (4)) == 0) goto loc_007FF681;
    goto loc_007FF9E7;
loc_007FF681:
    result = PiPagePathSetState(v_stack_mD0, 1, v_rsi + 8, a4);
    if (sign_flag) goto loc_007FF9E7;
    result = FsRtlIssueFileNotificationFsctl(v_stack_mD0, 1, v_rip - 8209920, a4);
    if (a6 != (v_rip + 6526545)) goto loc_007FF6DA;
    result = MiZeroPageFileFirstPage(v_stack_mD0, 1, v_rip - 8209920, a4);
    if (!sign_flag) goto loc_007FF6DA;
    a2 = 0;
    result = PiPagePathSetState(v_stack_mD0, a2, v_rip - 8209920, a4);
    goto loc_007FF9E7;
loc_007FF6DA:
    v_stack_m140 = 1;
    v_stack_m148 = (unsigned int)((unsigned int)(a5));
    v_stack_m150 = v_stack_mE0;
    v_stack_m158 = (unsigned int)(v_rbx);
    result = MiCreatePagefile(a6, v_stack_mD0, v_stack_mF8, v_stack_mF0);
    if (result == 0) goto loc_007FFB3D;
    result = MiInsertPageFileInList(result, v_stack_mD0, v_stack_mF8, v_stack_mF0);
    if (!sign_flag) goto loc_007FF75B;
    result = MiDeletePagefile(result, 1, v_stack_mF8, v_stack_mF0);
    goto loc_007FFB5E;
loc_007FF75B:
    if (a6 != (v_rip + 6526366)) goto loc_007FF7A1;
    if ((*(unsigned __int8 *)(v_rip + 6490578)) != 0) goto loc_007FF7A1;
    result = v_rip + 6526366;
    if (((*(unsigned __int8 *)(result + 172)) & (16)) == 0) {
        v_stack_m28 = v_xmm0;
        a2 = v_stack_m28;
        a1 = v_stack_mF8;
        result = IoInitializeCrashDump(a1, a2, v_stack_mF8, v_stack_mF0);
        *(unsigned __int8 *)(v_rip + 6490527) = (unsigned __int8)(result);
    }
    result = 0;
    goto loc_007FFB5E;
loc_007FF7A8:
    goto loc_007FF9E7;
loc_007FF7B3:
    v_stack_m100 = (unsigned int)(0xC000014FULL);
    v_stack_m108 = (unsigned int)((unsigned int)(0xC000014FULL));
    v_stack_m110 = 274;
    v_stack_m118 = (unsigned int)(0xC000014FULL);
    v_stack_m120 = (unsigned int)((unsigned int)(0xC000014FULL));
    v_stack_m128 = (unsigned int)((unsigned int)(0xC000014FULL));
    v_stack_m130 = (unsigned int)(0xC000014FULL);
    v_stack_m138 = 0x8008ULL;
    v_stack_m140 = 1;
    v_stack_m148 = 3;
    v_stack_m150 = 6;
    v_stack_m158 = v_stack_mF0;
    result = IopCreateFile(v_stack_mF8, (unsigned int)(0x100002ULL), v_stack_m90, v_stack_mB8);
    v_r13 = 0;
    if (!sign_flag) goto loc_007FF83E;
    v_rsi = 0;
    v_stack_mF8 = 0;
    goto loc_007FFA15;
loc_007FF83E:
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    v_stack_m150 = v_stack_mD0;
    v_stack_m158 = 0x66506D4DULL;
    a4 = 0;
    result = ObpReferenceObjectByHandleWithTag(v_stack_mF8, 3, *(unsigned __int64 *)(v_rip + 8155803), a4);
    if (sign_flag) goto loc_007FFA01;
    v_stack_m60 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_r14 = (3) | (-1);
    v_rbx = (a6) + (0x440ULL);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rbx, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rbx;
        a2 = result;
        a1 = v_rbx;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_007FF8FE:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a6 + 18520))))) goto loc_007FFA39;
    if ((((unsigned __int16)((unsigned int)(0x840ULL))) & ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a6 + 0 * 8 + 18528) + 172)))) != 0) goto loc_007FF93B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 0 * 8 + 18528) + 24) + 40)) == (*(unsigned __int64 *)(v_stack_mD0 + 40))) goto loc_007FF940;
loc_007FF93B:
    v_r13 = (unsigned int)((v_r13) + (1));
    goto loc_007FF8FE;
loc_007FF940:
    a1 = (unsigned __int16)(~((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a6 + 0 * 8 + 18528) + 172))));
    a1 = (unsigned int)((a1) >> (4));
    a1 = (unsigned int)((a1) & (1));
    result = (unsigned int)(~(0));
    result = (unsigned int)((result) & (1));
    if (((unsigned __int8)(a1)) == ((unsigned __int8)(result))) goto loc_007FFA36;
loc_007FF962:
loc_007FF967:
    v_r14 = (unsigned __int8)((v_r14) & (6));
    if (((unsigned __int8)(v_r14)) == 2) {
        a1 = a6 + 1088;
        result = ExfTryToWakePushLock(a1, *(unsigned __int64 *)(a6 + 0 * 8 + 18528), *(unsigned __int16 *)(*(unsigned __int64 *)(a6 + 0 * 8 + 18528) + 172), (unsigned int)(*(unsigned int *)(a6 + 18520)));
    }
    result = KeAbPostRelease(a6 + 1088, *(unsigned __int64 *)(a6 + 0 * 8 + 18528), *(unsigned __int16 *)(*(unsigned __int64 *)(a6 + 0 * 8 + 18528) + 172), (unsigned int)(*(unsigned int *)(a6 + 18520)));
    if (((unsigned __int8)(v_r14)) != 2) goto loc_007FF9BD;
    result = v_stack_m60 + 152;
    if ((*(unsigned __int64 *)(v_stack_m60 + 152)) != (v_stack_m60 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_m60, 1, *(unsigned __int16 *)(*(unsigned __int64 *)(a6 + 0 * 8 + 18528) + 172), (unsigned int)(*(unsigned int *)(a6 + 18520)));
    }
    result = v_stack_m98;
    if (v_stack_m98 != 0) {
        a3 = v_stack_m98;
        a2 = 0;
        a1 = a6;
        result = MiReduceCommitLimits(a1, a2, a3, (unsigned int)(*(unsigned int *)(a6 + 18520)));
    }
loc_007FF9E7:
    if (v_stack_mD0 != 0) {
        a2 = 0x66506D4DULL;
        a1 = v_stack_mD0;
        result = ObfDereferenceObjectWithTag(a1, a2, a3, (unsigned int)(*(unsigned int *)(a6 + 18520)));
    }
loc_007FFA01:
    if (v_stack_mF8 != 0) {
        a2 = 0;
        result = ObCloseHandle(v_stack_mF8, a2, a3, (unsigned int)(*(unsigned int *)(a6 + 18520)));
    }
    if (v_stack_mE8 != 0) {
        a2 = 0;
        a1 = v_stack_mE8;
        result = ExFreePoolWithTag(a1, a2, a3, (unsigned int)(*(unsigned int *)(a6 + 18520)));
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mC0, a2, a3, (unsigned int)(*(unsigned int *)(a6 + 18520)));
    goto loc_007FFB5E;
loc_007FFA36:
loc_007FFA39:
    a2 = 0;
    if (0 != 0) goto loc_007FFA4B;
    goto loc_007FF962;
loc_007FFA4B:
    v_rdi = (v_stack_mC8) >> (12);
    v_rbx = (v_stack_mF0) >> (12);
    if ((*(unsigned int *)(0 + 8)) <= ((unsigned int)(v_rbx))) goto loc_007FFA75;
    goto loc_007FF962;
loc_007FFA75:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 4)))) <= ((unsigned int)(v_rdi))) goto loc_007FFA89;
    goto loc_007FF962;
loc_007FFA89:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + 4)))) >= ((unsigned int)(v_rdi))) goto loc_007FFAD3;
    result = (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
    if (((*(unsigned __int8 *)(0 + 172)) & (16)) == 0) {
        result = (unsigned int)(v_rdi);
        result = (unsigned int)((result) - ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 4)))));
        v_stack_m98 = result;
        v_stack_m150 = 0;
        v_stack_m158 = 0;
        a4 = 0;
        a3 = (unsigned int)(result);
        a1 = a6;
        result = MiIncreaseCommitLimits(a1, a2, a3, a4);
    }
    result = MiAttemptChangePagingFileMaximum(0, (unsigned int)((unsigned int)(v_rdi)), a3, a4);
    if (sign_flag) goto loc_007FF962;
loc_007FFAD3:
    if (((unsigned int)(v_rbx)) <= (*(unsigned int *)(0 + 8))) goto loc_007FFB1F;
loc_007FFADA:
    if (((unsigned int)(v_rbx)) > ((unsigned int)((unsigned int)(*(unsigned int *)(0))))) goto loc_007FFAF2;
    result = MiCheckAndUpdatePagingFileMinimum(0, (unsigned int)((unsigned int)(v_rbx)), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_007FFADA;
    goto loc_007FFB1F;
loc_007FFAF2:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (0));
    result = MiIssuePageExtendRequest(a6, a2, 1, (unsigned int)((unsigned int)(v_r13)));
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
    if ((*(unsigned int *)(0 + 8)) < ((unsigned int)(v_rbx))) { result = (unsigned int)((unsigned int)(0xC000009AULL)); }
loc_007FFB1F:
    if (0 < 2) goto loc_007FF967;
    goto loc_007FF967;
loc_007FFB3D:
    goto loc_007FFB5E;
loc_007FFB44:
    goto loc_007FFB5E;
loc_007FFB4B:
    goto loc_007FFB5E;
loc_007FFB52:
    goto loc_007FFB5E;
loc_007FFB59:
loc_007FFB5E:
    return (unsigned int)(0xC00000F2ULL);
}
```

## 5. (Beta) C Style

```c
int64_t MiCreatePagingFile(int64_t Arg1, void *Arg2, int64_t Arg3, uint8_t Arg4, uint32_t Arg5, void *Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint32_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint32_t v_stack_m140;
    uint32_t v_stack_m148;
    uint8_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint8_t v_stack_m9C;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint16_t v_stack_mDE;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r12;
    local_rsp = (local_rsp) - (352);
    result = 0;
    v_stack_m90 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x80) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    *(uint32_t *)(local_rsp - 0x68) = 0;
    v_stack_mB8 = v_xmm0;
    v_stack_mE0 = v_xmm1;
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0xF0) = 0;
    *(uint64_t *)(local_rsp - 0xA8) = 0;
    *(uint64_t *)(local_rsp - 0xA0) = 0;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x48) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38) = 0;
    v_stack_mE8 = 0;
    if ((((uint32_t)((uint32_t)(Arg5))) & (0x7FFFFFULL)) != 0) goto loc_007FFB59;
    if (!sign_flag) goto loc_007FF0A1;
    if ((((uint32_t)((uint32_t)(Arg5))) & (0x42000000ULL)) != 0) goto loc_007FFB59;
loc_007FF0A1:
    Arg1 = ((((uint32_t)((uint32_t)(Arg5))) & (0xFF7FFFFFULL)) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_007FFB59;
    if (Arg4 == 0) goto loc_007FF148;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x7DAC72), Arg4, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_007FF13E;
    result = PsIsCurrentThreadInServerSilo(*(uint64_t *)(v_rip + 0x7DAC72), Arg4, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_007FF13E;
    if (((3) & ((uint8_t)(Arg1))) != 0) goto loc_007FF133;
    result = local_rdi;
    if (Arg1 < local_rdi) { result = Arg1; }
    if (((3) & ((uint8_t)(Arg3))) != 0) goto loc_007FF133;
    result = local_rdi;
    if (Arg3 < local_rdi) { result = Arg3; }
    if (((3) & (0)) != 0) goto loc_007FF133;
    result = local_rdi;
    if (0 < local_rdi) { result = 0; }
    v_stack_mF0 = *(uint64_t *)(arg2);
    goto loc_007FF163;
loc_007FF133:
    result = ExRaiseDatatypeMisalignment(*(uint64_t *)(v_rip + 0x7DAC72), Arg4, Arg3, Arg4);
    goto loc_007FFB5E;
loc_007FF13E:
    goto loc_007FFB5E;
loc_007FF148:
    v_stack_mF0 = *(uint64_t *)(arg2);
loc_007FF163:
    if ((*(uint64_t *)(arg2)) > (*(uint64_t *)(v_rip + 0x7DAC72))) goto loc_007FFB52;
    if ((*(uint64_t *)(arg2)) < 0x100000ULL) goto loc_007FFB52;
    if (Arg4 == 0) goto loc_007FF199;
    v_stack_mC8 = *(uint64_t *)(Arg3);
    goto loc_007FF1A4;
loc_007FF199:
    v_stack_mC8 = *(uint64_t *)(Arg3);
loc_007FF1A4:
    if ((*(uint64_t *)(Arg3)) > (*(uint64_t *)(v_rip + 0x7DAC72))) goto loc_007FFB4B;
    if ((*(uint64_t *)(arg2)) > (*(uint64_t *)(Arg3))) goto loc_007FFB4B;
    if (Arg4 == 0) goto loc_007FF1D0;
    v_stack_mE0 = v_xmm0;
    goto loc_007FF1DE;
loc_007FF1D0:
    v_stack_mE0 = v_xmm0;
loc_007FF1DE:
    v_stack_mDE = (uint16_t)(v_stack_mE0);
    result = (uint16_t)(((uint16_t)(v_stack_mE0)) - (1));
    if (((uint16_t)(result)) > 255) goto loc_007FFB44;
    result = MiAllocatePool(256, (uint32_t)((uint32_t)(v_stack_mE0)), (uint32_t)(0x20206D4DULL), Arg4);
    v_stack_mC0 = result;
    if (result == 0) goto loc_007FFB3D;
    if (Arg4 == 0) goto loc_007FF299;
    local_rsi = 0;
    if ((uint16_t)(v_stack_mE0) == 0) goto loc_007FF26B;
    if ((v_stack_mD8 + v_stack_mE0 * 1) > local_rdi) goto loc_007FF259;
    local_rbx = *(uint64_t *)(Arg3);
    if ((v_stack_mD8 + v_stack_mE0 * 1) < v_stack_mD8) {
        result = *(uint8_t *)(local_rdi);
        Arg1 = v_stack_mE0;
        local_rbx = v_stack_mC8;
    }
    result = memcpy(result, v_stack_mD8, (uint16_t)(Arg1), Arg4);
    goto loc_007FF2B4;
loc_007FF299:
    result = memcpy(result, v_stack_mD8, v_stack_mE0, Arg4);
    local_rsi = 0;
loc_007FF2B4:
    v_stack_mD8 = result;
    if (condition_is_above_or_equal) goto loc_007FF2F0;
    local_rbx = (local_rbx) >> (12);
    Arg2 = (v_stack_mF0) >> (12);
    result = MiCreateSpecialPurposeMemoryPageFile(Arg6, Arg2, (uint32_t)((uint32_t)(local_rbx)), v_stack_mE0);
    goto loc_007FFB5E;
loc_007FF2F0:
    v_stack_m98 = 0;
    v_stack_mD0 = 0;
    v_stack_mF8 = 0;
    result = RtlCreateSecurityDescriptor(v_stack_m58, 1, (uint32_t)((uint32_t)(local_rbx)), v_stack_mE0);
    if (sign_flag) goto loc_007FF9F9;
    result = RtlLengthSid(*(uint64_t *)(v_rip + 0x7DA73E), 1, (uint32_t)((uint32_t)(local_rbx)), v_stack_mE0);
    result = RtlLengthSid(*(uint64_t *)(v_rip + 0x668A20), 1, (uint32_t)((uint32_t)(local_rbx)), v_stack_mE0);
    result = (uint32_t)((result) + (32));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(result))) + ((uint32_t)(result)));
    result = MiAllocatePool(256, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x6C636144ULL), v_stack_mE0);
    v_stack_mE8 = result;
    if (result != 0) goto loc_007FF36F;
    goto loc_007FFA01;
loc_007FF36F:
    result = RtlCreateAcl(result, (uint32_t)((uint32_t)(result)), 2, v_stack_mE0);
    if (sign_flag) goto loc_007FFA01;
    v_stack_m150 = 0;
    v_stack_m158 = *(uint64_t *)(v_rip + 0x7DA6D4);
    Arg3 = 0;
    result = RtlpAddKnownAce(result, Arg3 + 2, Arg3, (uint32_t)(0x1F01FFULL));
    if (sign_flag) goto loc_007FFA01;
    v_stack_m150 = 0;
    v_stack_m158 = *(uint64_t *)(v_rip + 0x668993);
    Arg3 = 0;
    result = RtlpAddKnownAce(result, Arg3 + 2, Arg3, (uint32_t)(0x1F01FFULL));
    if (sign_flag) goto loc_007FFA01;
    Arg4 = 0;
    result = RtlSetDaclSecurityDescriptor(v_stack_m58, Arg4 + 1, result, Arg4);
    if (sign_flag) goto loc_007FFA01;
    local_r15 = 0;
    if (!sign_flag) goto loc_007FF41E;
    goto loc_007FF42E;
loc_007FF41E:
    local_rsi = 0;
    if (condition_is_below) { local_rsi = 2; }
loc_007FF42E:
    v_stack_m90 = 48;
    v_stack_m88 = 0;
    v_stack_m78 = 576;
    v_stack_m80 = v_stack_mE0;
    v_stack_m70 = v_stack_m58;
    v_stack_m68 = 0;
    result = (v_stack_mF0) + (0xFFFULL);
    result = (result) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_mA8 = result;
    v_stack_m100 = 0;
    v_stack_m108 = 0;
    v_stack_m110 = 274;
    v_stack_m118 = 0;
    v_stack_m120 = 0;
    v_stack_m128 = 0;
    v_stack_m130 = 0;
    v_stack_m138 = 0x9008ULL;
    v_stack_m140 = 0;
    v_stack_m148 = 2;
    v_stack_m150 = 6;
    v_stack_m158 = v_stack_mF0;
    result = IopCreateFile(v_stack_mF8, (uint32_t)(0x140003ULL), v_stack_m90, v_stack_mB8);
    if (sign_flag) goto loc_007FF7B3;
    if (v_stack_mB8 < 0) goto loc_007FF53C;
    result = ZwSetSecurityObject(v_stack_mF8, 4, v_stack_m58, v_stack_mB8);
    if (sign_flag) goto loc_007FFA01;
    local_r15 = 0;
loc_007FF53C:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_m58, v_stack_mB8);
    v_stack_mE8 = 0;
    local_rsi = 0;
    if (sign_flag) goto loc_007FFA01;
    v_stack_m158 = 20;
    result = ZwSetInformationFile(v_stack_mF8, v_stack_mB8, v_stack_mA8, local_rsi + 8);
    if (sign_flag) goto loc_007FFA01;
    if (sign_flag) goto loc_007FFA01;
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    v_stack_m150 = v_stack_mD0;
    v_stack_m158 = 0x66506D4DULL;
    Arg4 = 0;
    result = ObpReferenceObjectByHandleWithTag(v_stack_mF8, 3, *(uint64_t *)(v_rip + 0x7C7530), Arg4);
    if (sign_flag) goto loc_007FFA01;
    result = IoGetRelatedDeviceObject(v_stack_mD0, 3, *(uint64_t *)(v_rip + 0x7C7530), Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x48)))) > 54) goto loc_007FF7A8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x48)))) >= 54) goto loc_007FF7A8;
    result = MiCheckPageFileMapping(v_stack_mD0, 3, *(uint64_t *)(v_rip + 0x7C7530), Arg4);
    if (sign_flag) goto loc_007FF9E7;
    v_stack_m148 = 0;
    v_stack_m150 = Arg5;
    v_stack_m158 = v_stack_mA0;
    Arg4 = 0;
    result = IopQueryXxxInformation(v_stack_mD0, local_rsi + 4, local_rsi + 8, Arg4);
    if (sign_flag) goto loc_007FF9E7;
    if (((v_stack_m9C) & (4)) == 0) goto loc_007FF681;
    goto loc_007FF9E7;
loc_007FF681:
    result = PiPagePathSetState(v_stack_mD0, 1, local_rsi + 8, Arg4);
    if (sign_flag) goto loc_007FF9E7;
    result = FsRtlIssueFileNotificationFsctl(v_stack_mD0, 1, v_rip - 8209920, Arg4);
    if (Arg6 != (v_rip + 6526545)) goto loc_007FF6DA;
    result = MiZeroPageFileFirstPage(v_stack_mD0, 1, v_rip - 8209920, Arg4);
    if (!sign_flag) goto loc_007FF6DA;
    Arg2 = 0;
    result = PiPagePathSetState(v_stack_mD0, Arg2, v_rip - 8209920, Arg4);
    goto loc_007FF9E7;
loc_007FF6DA:
    v_stack_m140 = 1;
    v_stack_m148 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m150 = v_stack_mE0;
    v_stack_m158 = (uint32_t)(local_rbx);
    result = MiCreatePagefile(Arg6, v_stack_mD0, v_stack_mF8, v_stack_mF0);
    if (result == 0) goto loc_007FFB3D;
    result = MiInsertPageFileInList(result, v_stack_mD0, v_stack_mF8, v_stack_mF0);
    if (!sign_flag) goto loc_007FF75B;
    result = MiDeletePagefile(result, 1, v_stack_mF8, v_stack_mF0);
    goto loc_007FFB5E;
loc_007FF75B:
    if (Arg6 != (v_rip + 6526366)) goto loc_007FF7A1;
    if ((*(uint8_t *)(v_rip + 0x6309D2)) != 0) goto loc_007FF7A1;
    result = v_rip + 6526366;
    if (((*(uint8_t *)(result + 0xAC)) & (16)) == 0) {
        v_stack_m28 = v_xmm0;
        Arg2 = v_stack_m28;
        Arg1 = v_stack_mF8;
        result = IoInitializeCrashDump(Arg1, Arg2, v_stack_mF8, v_stack_mF0);
        *(uint8_t *)(v_rip + 0x63099F) = (uint8_t)(result);
    }
    result = 0;
    goto loc_007FFB5E;
loc_007FF7A8:
    goto loc_007FF9E7;
loc_007FF7B3:
    v_stack_m100 = (uint32_t)(0xC000014FULL);
    v_stack_m108 = (uint32_t)((uint32_t)(0xC000014FULL));
    v_stack_m110 = 274;
    v_stack_m118 = (uint32_t)(0xC000014FULL);
    v_stack_m120 = (uint32_t)((uint32_t)(0xC000014FULL));
    v_stack_m128 = (uint32_t)((uint32_t)(0xC000014FULL));
    v_stack_m130 = (uint32_t)(0xC000014FULL);
    v_stack_m138 = 0x8008ULL;
    v_stack_m140 = 1;
    v_stack_m148 = 3;
    v_stack_m150 = 6;
    v_stack_m158 = v_stack_mF0;
    result = IopCreateFile(v_stack_mF8, (uint32_t)(0x100002ULL), v_stack_m90, v_stack_mB8);
    local_r13 = 0;
    if (!sign_flag) goto loc_007FF83E;
    local_rsi = 0;
    v_stack_mF8 = 0;
    goto loc_007FFA15;
loc_007FF83E:
    v_stack_m140 = 0;
    v_stack_m148 = 0;
    v_stack_m150 = v_stack_mD0;
    v_stack_m158 = 0x66506D4DULL;
    Arg4 = 0;
    result = ObpReferenceObjectByHandleWithTag(v_stack_mF8, 3, *(uint64_t *)(v_rip + 0x7C729B), Arg4);
    if (sign_flag) goto loc_007FFA01;
    v_stack_m60 = *(uint64_t *)(gs_base + (0 + 0x188));
    local_r14 = (3) | (-1);
    local_rbx = (Arg6) + (0x440ULL);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbx, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rbx;
        Arg2 = result;
        Arg1 = local_rbx;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_007FF8FE:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x4858))))) goto loc_007FFA39;
    if ((((uint16_t)((uint32_t)(0x840ULL))) & ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg6 + 0x0 * 8 + 0x4860) + 0xAC)))) != 0) goto loc_007FF93B;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + 0x0 * 8 + 0x4860) + 0x18) + 0x28)) == (*(uint64_t *)(v_stack_mD0 + 0x28))) goto loc_007FF940;
loc_007FF93B:
    local_r13 = (uint32_t)((local_r13) + (1));
    goto loc_007FF8FE;
loc_007FF940:
    Arg1 = (uint16_t)(~((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg6 + 0x0 * 8 + 0x4860) + 0xAC))));
    Arg1 = (uint32_t)((Arg1) >> (4));
    Arg1 = (uint32_t)((Arg1) & (1));
    result = (uint32_t)(~(0));
    result = (uint32_t)((result) & (1));
    if (((uint8_t)(Arg1)) == ((uint8_t)(result))) goto loc_007FFA36;
loc_007FF962:
loc_007FF967:
    local_r14 = (uint8_t)((local_r14) & (6));
    if (((uint8_t)(local_r14)) == 2) {
        Arg1 = Arg6 + 1088;
        result = ExfTryToWakePushLock(Arg1, *(uint64_t *)(arg6 + 0x0 * 8 + 0x4860), *(uint16_t *)(*(uint64_t *)(arg6 + 0x0 * 8 + 0x4860) + 0xAC), (uint32_t)(*(uint32_t *)(arg6 + 0x4858)));
    }
    result = KeAbPostRelease(Arg6 + 1088, *(uint64_t *)(arg6 + 0x0 * 8 + 0x4860), *(uint16_t *)(*(uint64_t *)(arg6 + 0x0 * 8 + 0x4860) + 0xAC), (uint32_t)(*(uint32_t *)(arg6 + 0x4858)));
    if (((uint8_t)(local_r14)) != 2) goto loc_007FF9BD;
    result = v_stack_m60 + 152;
    if ((*(uint64_t *)(v_stack_m60 + 0x98)) != (v_stack_m60 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_m60, 1, *(uint16_t *)(*(uint64_t *)(arg6 + 0x0 * 8 + 0x4860) + 0xAC), (uint32_t)(*(uint32_t *)(arg6 + 0x4858)));
    }
    result = v_stack_m98;
    if (v_stack_m98 != 0) {
        Arg3 = v_stack_m98;
        Arg2 = 0;
        Arg1 = Arg6;
        result = MiReduceCommitLimits(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg6 + 0x4858)));
    }
loc_007FF9E7:
    if (v_stack_mD0 != 0) {
        Arg2 = 0x66506D4DULL;
        Arg1 = v_stack_mD0;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg6 + 0x4858)));
    }
loc_007FFA01:
    if (v_stack_mF8 != 0) {
        Arg2 = 0;
        result = ObCloseHandle(v_stack_mF8, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg6 + 0x4858)));
    }
    if (v_stack_mE8 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mE8;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg6 + 0x4858)));
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mC0, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg6 + 0x4858)));
    goto loc_007FFB5E;
loc_007FFA36:
loc_007FFA39:
    Arg2 = 0;
    if (0 != 0) goto loc_007FFA4B;
    goto loc_007FF962;
loc_007FFA4B:
    local_rdi = (v_stack_mC8) >> (12);
    local_rbx = (v_stack_mF0) >> (12);
    if ((*(uint32_t *)(0 + 0x8)) <= ((uint32_t)(local_rbx))) goto loc_007FFA75;
    goto loc_007FF962;
loc_007FFA75:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4)))) <= ((uint32_t)(local_rdi))) goto loc_007FFA89;
    goto loc_007FF962;
loc_007FFA89:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4)))) >= ((uint32_t)(local_rdi))) goto loc_007FFAD3;
    result = (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
    if (((*(uint8_t *)(0 + 0xAC)) & (16)) == 0) {
        result = (uint32_t)(local_rdi);
        result = (uint32_t)((result) - ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x4)))));
        v_stack_m98 = result;
        v_stack_m150 = 0;
        v_stack_m158 = 0;
        Arg4 = 0;
        Arg3 = (uint32_t)(result);
        Arg1 = Arg6;
        result = MiIncreaseCommitLimits(Arg1, Arg2, Arg3, Arg4);
    }
    result = MiAttemptChangePagingFileMaximum(0, (uint32_t)((uint32_t)(local_rdi)), Arg3, Arg4);
    if (sign_flag) goto loc_007FF962;
loc_007FFAD3:
    if (((uint32_t)(local_rbx)) <= (*(uint32_t *)(0 + 0x8))) goto loc_007FFB1F;
loc_007FFADA:
    if (((uint32_t)(local_rbx)) > ((uint32_t)((uint32_t)(*(uint32_t *)(0))))) goto loc_007FFAF2;
    result = MiCheckAndUpdatePagingFileMinimum(0, (uint32_t)((uint32_t)(local_rbx)), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_007FFADA;
    goto loc_007FFB1F;
loc_007FFAF2:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (0));
    result = MiIssuePageExtendRequest(Arg6, Arg2, 1, (uint32_t)((uint32_t)(local_r13)));
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
    if ((*(uint32_t *)(0 + 0x8)) < ((uint32_t)(local_rbx))) { result = (uint32_t)((uint32_t)(0xC000009AULL)); }
loc_007FFB1F:
    if (0 < 2) goto loc_007FF967;
    goto loc_007FF967;
loc_007FFB3D:
    goto loc_007FFB5E;
loc_007FFB44:
    goto loc_007FFB5E;
loc_007FFB4B:
    goto loc_007FFB5E;
loc_007FFB52:
    goto loc_007FFB5E;
loc_007FFB59:
loc_007FFB5E:
    return (uint32_t)(0xC00000F2ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg6` | `+ 0x0` | `64` | `R/W` |
| `Arg6` | `+ 0x440` | `64` | `R` |
| `Arg6` | `+ 0x4858` | `32` | `R` |
| `Arg6` | `+ 0x4860 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007FEFF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
