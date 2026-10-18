# PopAllocateHiberContext

- RVA: `0x00ADC05C`–`0x00ADC6E3` (길이 `1,671` bytes)
- VA: `0x0000000140ADC05C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF660`
- 디코드: `394`개 명령, `1,671/1,671` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **32**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **27**

### Outgoing calls
- `0x00ADC0B0` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00ADC0B5` → [Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline_function_005CE348.md) (function, `0x005CE348`)
- `0x00ADC0C5` → [Feature_Servicing_ARM64_LLVMHibernate__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_Servicing_ARM64_LLVMHibernate__private_IsEnabledDeviceUsageNoInline_function_005D4C00.md) (function, `0x005D4C00`)
- `0x00ADC0E3` → [MmLockPreChargedPagedPool](MmLockPreChargedPagedPool_function_00AD6E20.md) (function, `0x00AD6E20`)
- `0x00ADC19C` → [IoGetDumpStack](IoGetDumpStack_function_00AD9D6C.md) (function, `0x00AD9D6C`)
- `0x00ADC251` → [MmBuildMdlForNonPagedPool](../../text/23/MmBuildMdlForNonPagedPool_function_0023A870.md) (function, `0x0023A870`)
- `0x00ADC2B1` → [MmBuildMdlForNonPagedPool](../../text/23/MmBuildMdlForNonPagedPool_function_0023A870.md) (function, `0x0023A870`)
- `0x00ADC2B9` → [PopLoadResumeContext](PopLoadResumeContext_function_00AD1C0C.md) (function, `0x00AD1C0C`)
- `0x00ADC2DD` → [BcdOpenStore](../A4/BcdOpenStore_function_00A4116C.md) (function, `0x00A4116C`)
- `0x00ADC303` → [PopBcdEstablishResumeObject](../77/PopBcdEstablishResumeObject_function_007700E4.md) (function, `0x007700E4`)
- `0x00ADC317` → [BcdCloseStore](../A3/BcdCloseStore_function_00A3C68C.md) (function, `0x00A3C68C`)
- `0x00ADC32A` → [PopBcdSetPendingResume](../77/PopBcdSetPendingResume_function_007706F8.md) (function, `0x007706F8`)
- `0x00ADC335` → [BcdCloseObject](../A3/BcdCloseObject_function_00A3FB08.md) (function, `0x00A3FB08`)
- `0x00ADC347` → [BcdCloseStore](../A3/BcdCloseStore_function_00A3C68C.md) (function, `0x00A3C68C`)
- `0x00ADC356` → [BcdForciblyUnloadStore](../82/BcdForciblyUnloadStore_function_008232FC.md) (function, `0x008232FC`)
- `0x00ADC35F` → [RtlClearAllBits](../../text/45/RtlClearAllBits_function_00450230.md) (function, `0x00450230`)
- `0x00ADC368` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (function, `0x00362490`)
- `0x00ADC370` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (function, `0x00362490`)
- `0x00ADC37C` → [PopGetHwConfigurationSignature](../../pagelk/B6/PopGetHwConfigurationSignature_function_00B6D5A4.md) (function, `0x00B6D5A4`)
- `0x00ADC38A` → [PopHiberInitializeResources](../75/PopHiberInitializeResources_function_0075D5FC.md) (function, `0x0075D5FC`)
- `0x00ADC393` → [PopGetBitlockerKeyLocation](../../pagelk/B6/PopGetBitlockerKeyLocation_function_00B6BBFC.md) (function, `0x00B6BBFC`)
- `0x00ADC3B5` → [PopDiscardRange](../../pagelk/B7/PopDiscardRange_function_00B794F8.md) (function, `0x00B794F8`)
- `0x00ADC3E6` → [PoSetHiberRange](../../text/47/PoSetHiberRange_function_0047C580.md) (function, `0x0047C580`)
- `0x00ADC400` → [PoSetHiberRange](../../text/47/PoSetHiberRange_function_0047C580.md) (function, `0x0047C580`)
- `0x00ADC415` → [MmMarkHiberRange](../7F/MmMarkHiberRange_function_007FE3D0.md) (function, `0x007FE3D0`)
- `0x00ADC424` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00ADC45D` → [PopAllocatePages](../../pagelk/B7/PopAllocatePages_function_00B7E3FC.md) (function, `0x00B7E3FC`)
- `0x00ADC4E4` → [PoSetHiberRange](../../text/47/PoSetHiberRange_function_0047C580.md) (function, `0x0047C580`)
- `0x00ADC507` → [PopInternalAddToDumpFile](../../text/5C/PopInternalAddToDumpFile_function_005CE634.md) (function, `0x005CE634`)
- `0x00ADC517` → [PopInternalAddToDumpFile](../../text/5C/PopInternalAddToDumpFile_function_005CE634.md) (function, `0x005CE634`)
- `0x00ADC521` → [PopCheckpointSystemSleep](../../pagelk/B7/PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00ADC53C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00ADC547` → [PopAllocatePages](../../pagelk/B7/PopAllocatePages_function_00B7E3FC.md) (function, `0x00B7E3FC`)
- `0x00ADC564` → [PopCheckpointSystemSleep](../../pagelk/B7/PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00ADC593` → [PoSetHiberRange](../../text/47/PoSetHiberRange_function_0047C580.md) (function, `0x0047C580`)
- `0x00ADC5AD` → [PopInternalAddToDumpFile](../../text/5C/PopInternalAddToDumpFile_function_005CE634.md) (function, `0x005CE634`)
- `0x00ADC5BD` → [PopInternalAddToDumpFile](../../text/5C/PopInternalAddToDumpFile_function_005CE634.md) (function, `0x005CE634`)
- `0x00ADC5C7` → [PopCheckpointSystemSleep](../../pagelk/B7/PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00ADC5E2` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00ADC60E` → [PoSetHiberRange](../../text/47/PoSetHiberRange_function_0047C580.md) (function, `0x0047C580`)
- `0x00ADC641` → [VslAllocateSecureHibernateResources](../71/VslAllocateSecureHibernateResources_function_00718788.md) (function, `0x00718788`)
- `0x00ADC656` → [PopCheckpointSystemSleep](../../pagelk/B7/PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00ADC65B` → [PopFreeHiberContext](../70/PopFreeHiberContext_function_00704F1C.md) (function, `0x00704F1C`)
- `0x00ADC679` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (function, `0x006AD790`)
- `0x00ADC68E` → [BgkResumePrepare](../../pagelk/B6/BgkResumePrepare_function_00B63ACC.md) (function, `0x00B63ACC`)
- `0x00ADC6AC` → [Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline_function_005D4A08.md) (function, `0x005D4A08`)
- `0x00ADC6C0` → [HvlAllocateHibernateResources](../71/HvlAllocateHibernateResources_function_007186D4.md) (function, `0x007186D4`)

### Direct callers
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7EFDE`

### Static image references
- `0x00ADC079` → RVA `0x00F0BD74` (`.data`; read)
- `0x00ADC093` → RVA `0x00F0BF68` (`.data`; read)
- `0x00ADC0A9` → RVA `0x00F0BD90` (`.data`; write)
- `0x00ADC0D5` → RVA `0x00F0BF78` (`.data`; read)
- `0x00ADC0DC` → RVA `0x00F0BF70` (`.data`; read)
- `0x00ADC0E8` → RVA `0x00F0BF90` (`.data`; read)
- `0x00ADC0F3` → RVA `0x00E676F8` (`.data`; write)
- `0x00ADC100` → RVA `0x00F0BFA0` (`.data`; read)
- `0x00ADC10C` → RVA `0x00F0BF80` (`.data`; read)
- `0x00ADC11A` → RVA `0x00F0BFE0` (`.data`; read)
- `0x00ADC128` → RVA `0x00F0BFC0` (`.data`; read)
- `0x00ADC136` → RVA `0x00F0BFF0` (`.data`; read)
- `0x00ADC144` → RVA `0x00F0BFE8` (`.data`; read)
- `0x00ADC156` → RVA `0x00F0BFB0` (`.data`; read)
- `0x00ADC169` → RVA `0x00F0BF28` (`.data`; read)
- `0x00ADC187` → RVA `0x00F0CF0C` (`.data`; read)
- `0x00ADC1B7` → RVA `0x00F0BD4C` (`.data`; read)
- `0x00ADC1CE` → RVA `0x00F0BD54` (`.data`; read)
- `0x00ADC204` → RVA `0x00F0BF88` (`.data`; read)
- `0x00ADC3BA` → RVA `0x00E0AA1C` (`.data`; read)
- `0x00ADC3C3` → RVA `0x00F59CC8` (`.data`; read)
- `0x00ADC3CF` → RVA `0x00F49B40` (`.data`; read)
- `0x00ADC3F2` → RVA `0x00FCF280` (`CACHEALI`; read)
- `0x00ADC405` → RVA `0x00F0BF48` (`.data`; read)
- `0x00ADC41A` → RVA `0x00E00808` (`.data`; read)
- `0x00ADC620` → RVA `0x00FC6A84` (`ALMOSTRO`; read)
- `0x00ADC697` → RVA `0x00F0DD9C` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **32**
  - `0x00ADC0B0` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00ADC0B5` → [Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline_function_005CE348.md) (`PAGE` → `.text`)
  - `0x00ADC0C5` → [Feature_Servicing_ARM64_LLVMHibernate__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_Servicing_ARM64_LLVMHibernate__private_IsEnabledDeviceUsageNoInline_function_005D4C00.md) (`PAGE` → `.text`)
  - `0x00ADC251` → [MmBuildMdlForNonPagedPool](../../text/23/MmBuildMdlForNonPagedPool_function_0023A870.md) (`PAGE` → `.text`)
  - `0x00ADC2B1` → [MmBuildMdlForNonPagedPool](../../text/23/MmBuildMdlForNonPagedPool_function_0023A870.md) (`PAGE` → `.text`)
  - `0x00ADC35F` → [RtlClearAllBits](../../text/45/RtlClearAllBits_function_00450230.md) (`PAGE` → `.text`)
  - `0x00ADC368` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (`PAGE` → `.text`)
  - `0x00ADC370` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (`PAGE` → `.text`)
  - `0x00ADC37C` → [PopGetHwConfigurationSignature](../../pagelk/B6/PopGetHwConfigurationSignature_function_00B6D5A4.md) (`PAGE` → `PAGELK`)
  - `0x00ADC393` → [PopGetBitlockerKeyLocation](../../pagelk/B6/PopGetBitlockerKeyLocation_function_00B6BBFC.md) (`PAGE` → `PAGELK`)
  - `0x00ADC3B5` → [PopDiscardRange](../../pagelk/B7/PopDiscardRange_function_00B794F8.md) (`PAGE` → `PAGELK`)
  - `0x00ADC3E6` → [PoSetHiberRange](../../text/47/PoSetHiberRange_function_0047C580.md) (`PAGE` → `.text`)
  - `0x00ADC400` → [PoSetHiberRange](../../text/47/PoSetHiberRange_function_0047C580.md) (`PAGE` → `.text`)
  - `0x00ADC424` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00ADC45D` → [PopAllocatePages](../../pagelk/B7/PopAllocatePages_function_00B7E3FC.md) (`PAGE` → `PAGELK`)
  - `0x00ADC4E4` → [PoSetHiberRange](../../text/47/PoSetHiberRange_function_0047C580.md) (`PAGE` → `.text`)
  - `0x00ADC507` → [PopInternalAddToDumpFile](../../text/5C/PopInternalAddToDumpFile_function_005CE634.md) (`PAGE` → `.text`)
  - `0x00ADC517` → [PopInternalAddToDumpFile](../../text/5C/PopInternalAddToDumpFile_function_005CE634.md) (`PAGE` → `.text`)
  - `0x00ADC521` → [PopCheckpointSystemSleep](../../pagelk/B7/PopCheckpointSystemSleep_function_00B77C90.md) (`PAGE` → `PAGELK`)
  - `0x00ADC53C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00ADC547` → [PopAllocatePages](../../pagelk/B7/PopAllocatePages_function_00B7E3FC.md) (`PAGE` → `PAGELK`)
  - `0x00ADC564` → [PopCheckpointSystemSleep](../../pagelk/B7/PopCheckpointSystemSleep_function_00B77C90.md) (`PAGE` → `PAGELK`)
  - `0x00ADC593` → [PoSetHiberRange](../../text/47/PoSetHiberRange_function_0047C580.md) (`PAGE` → `.text`)
  - `0x00ADC5AD` → [PopInternalAddToDumpFile](../../text/5C/PopInternalAddToDumpFile_function_005CE634.md) (`PAGE` → `.text`)
  - `0x00ADC5BD` → [PopInternalAddToDumpFile](../../text/5C/PopInternalAddToDumpFile_function_005CE634.md) (`PAGE` → `.text`)
  - `0x00ADC5C7` → [PopCheckpointSystemSleep](../../pagelk/B7/PopCheckpointSystemSleep_function_00B77C90.md) (`PAGE` → `PAGELK`)
  - `0x00ADC5E2` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00ADC60E` → [PoSetHiberRange](../../text/47/PoSetHiberRange_function_0047C580.md) (`PAGE` → `.text`)
  - `0x00ADC656` → [PopCheckpointSystemSleep](../../pagelk/B7/PopCheckpointSystemSleep_function_00B77C90.md) (`PAGE` → `PAGELK`)
  - `0x00ADC679` → [ZwQuerySystemInformation](../../text/6A/ZwQuerySystemInformation_function_006AD790.md) (`PAGE` → `.text`)
  - `0x00ADC68E` → [BgkResumePrepare](../../pagelk/B6/BgkResumePrepare_function_00B63ACC.md) (`PAGE` → `PAGELK`)
  - `0x00ADC6AC` → [Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline](../../text/5D/Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline_function_005D4A08.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ADC05C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00ADC061  55                              push rbp
00ADC062  56                              push rsi
00ADC063  57                              push rdi
00ADC064  41 54                           push r12
00ADC066  41 55                           push r13
00ADC068  41 56                           push r14
00ADC06A  41 57                           push r15
00ADC06C  48 8B EC                        mov rbp, rsp
00ADC06F  48 83 EC 40                     sub rsp, 0x40
00ADC073  45 33 F6                        xor r14d, r14d
00ADC076  48 8B F1                        mov rsi, rcx
00ADC079  83 3D F4 FC 42 00 05            cmp dword ptr [rip + 0x42fcf4], 5
00ADC080  4C 89 75 58                     mov qword ptr [rbp + 0x58], r14
00ADC084  4C 89 75 F0                     mov qword ptr [rbp - 0x10], r14
00ADC088  66 44 89 75 48                  mov word ptr [rbp + 0x48], r14w
00ADC08D  0F 85 32 06 00 00               jne 0x140adc6c5
00ADC093  48 8B 1D CE FE 42 00            mov rbx, qword ptr [rip + 0x42fece]
00ADC09A  33 D2                           xor edx, edx
00ADC09C  48 8B CB                        mov rcx, rbx
00ADC09F  4C 89 75 50                     mov qword ptr [rbp + 0x50], r14
00ADC0A3  41 B8 F0 01 00 00               mov r8d, 0x1f0
00ADC0A9  48 89 1D E0 FC 42 00            mov qword ptr [rip + 0x42fce0], rbx
00ADC0B0  E8 8B AB BE FF                  call 0x1406c6c40
00ADC0B5  E8 8E 22 AF FF                  call 0x1405ce348
00ADC0BA  85 C0                           test eax, eax
00ADC0BC  74 07                           je 0x140adc0c5
00ADC0BE  C6 83 ED 01 00 00 01            mov byte ptr [rbx + 0x1ed], 1
00ADC0C5  E8 36 8B AF FF                  call 0x1405d4c00
00ADC0CA  85 C0                           test eax, eax
00ADC0CC  74 07                           je 0x140adc0d5
00ADC0CE  C6 83 EE 01 00 00 01            mov byte ptr [rbx + 0x1ee], 1
00ADC0D5  48 8B 15 9C FE 42 00            mov rdx, qword ptr [rip + 0x42fe9c]
00ADC0DC  48 8B 0D 8D FE 42 00            mov rcx, qword ptr [rip + 0x42fe8d]
00ADC0E3  E8 38 AD FF FF                  call 0x140ad6e20
00ADC0E8  0F 10 05 A1 FE 42 00            movups xmm0, xmmword ptr [rip + 0x42fea1]
00ADC0EF  4C 8D 6B 20                     lea r13, [rbx + 0x20]
00ADC0F3  44 89 35 FE B5 38 00            mov dword ptr [rip + 0x38b5fe], r14d
00ADC0FA  F3 41 0F 7F 45 00               movdqu xmmword ptr [r13], xmm0
00ADC100  0F 10 0D 99 FE 42 00            movups xmm1, xmmword ptr [rip + 0x42fe99]
00ADC107  F3 0F 7F 4B 40                  movdqu xmmword ptr [rbx + 0x40], xmm1
00ADC10C  48 8B 05 6D FE 42 00            mov rax, qword ptr [rip + 0x42fe6d]
00ADC113  48 89 83 D8 00 00 00            mov qword ptr [rbx + 0xd8], rax
00ADC11A  48 8B 05 BF FE 42 00            mov rax, qword ptr [rip + 0x42febf]
00ADC121  48 89 83 60 01 00 00            mov qword ptr [rbx + 0x160], rax
00ADC128  48 8B 05 91 FE 42 00            mov rax, qword ptr [rip + 0x42fe91]
00ADC12F  48 89 83 E8 00 00 00            mov qword ptr [rbx + 0xe8], rax
00ADC136  48 8B 05 B3 FE 42 00            mov rax, qword ptr [rip + 0x42feb3]
00ADC13D  48 89 83 F0 00 00 00            mov qword ptr [rbx + 0xf0], rax
00ADC144  48 8B 05 9D FE 42 00            mov rax, qword ptr [rip + 0x42fe9d]
00ADC14B  48 89 83 F8 00 00 00            mov qword ptr [rbx + 0xf8], rax
00ADC152  48 8D 43 50                     lea rax, [rbx + 0x50]
00ADC156  0F 10 05 53 FE 42 00            movups xmm0, xmmword ptr [rip + 0x42fe53]
00ADC15D  F3 0F 7F 43 30                  movdqu xmmword ptr [rbx + 0x30], xmm0
00ADC162  48 89 40 08                     mov qword ptr [rax + 8], rax
00ADC166  48 89 00                        mov qword ptr [rax], rax
00ADC169  4C 39 35 B8 FD 42 00            cmp qword ptr [rip + 0x42fdb8], r14
00ADC170  75 15                           jne 0x140adc187
00ADC172  BF 0F 00 00 C0                  mov edi, 0xc000000f
00ADC177  C7 06 0A 00 00 00               mov dword ptr [rsi], 0xa
00ADC17D  B9 2A 00 00 00                  mov ecx, 0x2a
00ADC182  E9 CF 04 00 00                  jmp 0x140adc656
00ADC187  44 8B 0D 7E 0D 43 00            mov r9d, dword ptr [rip + 0x430d7e]
00ADC18E  4C 8D A3 B8 00 00 00            lea r12, [rbx + 0xb8]
00ADC195  41 83 E1 10                     and r9d, 0x10
00ADC199  49 8B D4                        mov rdx, r12
00ADC19C  E8 CB DB FF FF                  call 0x140ad9d6c
00ADC1A1  8B F8                           mov edi, eax
00ADC1A3  85 C0                           test eax, eax
00ADC1A5  79 10                           jns 0x140adc1b7
00ADC1A7  C7 06 0A 00 00 00               mov dword ptr [rsi], 0xa
00ADC1AD  B9 2B 00 00 00                  mov ecx, 0x2b
00ADC1B2  E9 9F 04 00 00                  jmp 0x140adc656
00ADC1B7  8B 05 8F FB 42 00               mov eax, dword ptr [rip + 0x42fb8f]
00ADC1BD  BA 02 00 00 00                  mov edx, 2
00ADC1C2  4D 8B 3C 24                     mov r15, qword ptr [r12]
00ADC1C6  41 0F B6 CE                     movzx ecx, r14b
00ADC1CA  85 C0                           test eax, eax
00ADC1CC  79 09                           jns 0x140adc1d7
00ADC1CE  39 15 80 FB 42 00               cmp dword ptr [rip + 0x42fb80], edx
00ADC1D4  0F 44 CA                        cmove ecx, edx
00ADC1D7  80 C9 01                        or cl, 1
00ADC1DA  44 0F B6 C1                     movzx r8d, cl
00ADC1DE  0F 20 E2                        mov rdx, cr4
00ADC1E1  81 E2 00 10 00 00               and edx, 0x1000
00ADC1E7  41 8A C0                        mov al, r8b
00ADC1EA  0C 08                           or al, 8
00ADC1EC  BF FF 0F 00 00                  mov edi, 0xfff
00ADC1F1  0F B6 C8                        movzx ecx, al
00ADC1F4  48 85 D2                        test rdx, rdx
00ADC1F7  41 0F 44 C8                     cmove ecx, r8d
00ADC1FB  4C 8B 83 E8 00 00 00            mov r8, qword ptr [rbx + 0xe8]
00ADC202  88 0B                           mov byte ptr [rbx], cl
00ADC204  48 8B 0D 7D FD 42 00            mov rcx, qword ptr [rip + 0x42fd7d]
00ADC20B  8B D1                           mov edx, ecx
00ADC20D  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00ADC214  8B C2                           mov eax, edx
00ADC216  4D 89 30                        mov qword ptr [r8], r14
00ADC219  48 23 C7                        and rax, rdi
00ADC21C  66 45 89 70 0A                  mov word ptr [r8 + 0xa], r14w
00ADC221  48 05 FF 8F 01 00               add rax, 0x18fff
00ADC227  49 89 48 20                     mov qword ptr [r8 + 0x20], rcx
00ADC22B  48 C1 E8 0C                     shr rax, 0xc
00ADC22F  23 D7                           and edx, edi
00ADC231  66 83 C0 06                     add ax, 6
00ADC235  41 89 50 2C                     mov dword ptr [r8 + 0x2c], edx
00ADC239  66 C1 E0 03                     shl ax, 3
00ADC23D  66 41 89 40 08                  mov word ptr [r8 + 8], ax
00ADC242  41 C7 40 28 00 80 01 00         mov dword ptr [r8 + 0x28], 0x18000
00ADC24A  48 8B 8B E8 00 00 00            mov rcx, qword ptr [rbx + 0xe8]
00ADC251  E8 1A E6 75 FF                  call 0x14023a870
00ADC256  48 8B 93 F0 00 00 00            mov rdx, qword ptr [rbx + 0xf0]
00ADC25D  48 85 D2                        test rdx, rdx
00ADC260  74 54                           je 0x140adc2b6
00ADC262  48 8B 0D 7F FD 42 00            mov rcx, qword ptr [rip + 0x42fd7f]
00ADC269  41 B8 FF 1F 00 00               mov r8d, 0x1fff
00ADC26F  0F B7 C1                        movzx eax, cx
00ADC272  4C 89 32                        mov qword ptr [rdx], r14
00ADC275  66 23 C7                        and ax, di
00ADC278  66 44 89 72 0A                  mov word ptr [rdx + 0xa], r14w
00ADC27D  66 41 03 C0                     add ax, r8w
00ADC281  C7 42 28 00 10 00 00            mov dword ptr [rdx + 0x28], 0x1000
00ADC288  66 C1 E8 0C                     shr ax, 0xc
00ADC28C  66 83 C0 06                     add ax, 6
00ADC290  66 C1 E0 03                     shl ax, 3
00ADC294  66 89 42 08                     mov word ptr [rdx + 8], ax
00ADC298  48 8B C1                        mov rax, rcx
00ADC29B  23 CF                           and ecx, edi
00ADC29D  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
00ADC2A3  48 89 42 20                     mov qword ptr [rdx + 0x20], rax
00ADC2A7  89 4A 2C                        mov dword ptr [rdx + 0x2c], ecx
00ADC2AA  48 8B 8B F0 00 00 00            mov rcx, qword ptr [rbx + 0xf0]
00ADC2B1  E8 BA E5 75 FF                  call 0x14023a870
00ADC2B6  48 8B CB                        mov rcx, rbx
00ADC2B9  E8 4E 59 FF FF                  call 0x140ad1c0c
00ADC2BE  8B F8                           mov edi, eax
00ADC2C0  85 C0                           test eax, eax
00ADC2C2  79 10                           jns 0x140adc2d4
00ADC2C4  C7 06 0C 00 00 00               mov dword ptr [rsi], 0xc
00ADC2CA  B9 2C 00 00 00                  mov ecx, 0x2c
00ADC2CF  E9 82 03 00 00                  jmp 0x140adc656
00ADC2D4  4C 8D 45 58                     lea r8, [rbp + 0x58]
00ADC2D8  BA 02 00 00 00                  mov edx, 2
00ADC2DD  E8 8A 4E F6 FF                  call 0x140a4116c
00ADC2E2  8B F8                           mov edi, eax
00ADC2E4  85 C0                           test eax, eax
00ADC2E6  79 10                           jns 0x140adc2f8
00ADC2E8  C7 06 0D 00 00 00               mov dword ptr [rsi], 0xd
00ADC2EE  B9 2D 00 00 00                  mov ecx, 0x2d
00ADC2F3  E9 5E 03 00 00                  jmp 0x140adc656
00ADC2F8  4C 8B 75 58                     mov r14, qword ptr [rbp + 0x58]
00ADC2FC  48 8D 55 50                     lea rdx, [rbp + 0x50]
00ADC300  49 8B CE                        mov rcx, r14
00ADC303  E8 DC 3D C9 FF                  call 0x1407700e4
00ADC308  8B F8                           mov edi, eax
00ADC30A  49 8B CE                        mov rcx, r14
00ADC30D  85 C0                           test eax, eax
00ADC30F  79 15                           jns 0x140adc326
00ADC311  C7 06 0E 00 00 00               mov dword ptr [rsi], 0xe
00ADC317  E8 70 03 F6 FF                  call 0x140a3c68c
00ADC31C  B9 2E 00 00 00                  mov ecx, 0x2e
00ADC321  E9 30 03 00 00                  jmp 0x140adc656
00ADC326  4C 8B 4D 50                     mov r9, qword ptr [rbp + 0x50]
00ADC32A  E8 C9 43 C9 FF                  call 0x1407706f8
00ADC32F  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
00ADC333  8B F8                           mov edi, eax
00ADC335  E8 CE 37 F6 FF                  call 0x140a3fb08
00ADC33A  49 8B CE                        mov rcx, r14
00ADC33D  85 FF                           test edi, edi
00ADC33F  79 15                           jns 0x140adc356
00ADC341  C7 06 0F 00 00 00               mov dword ptr [rsi], 0xf
00ADC347  E8 40 03 F6 FF                  call 0x140a3c68c
00ADC34C  B9 2F 00 00 00                  mov ecx, 0x2f
00ADC351  E9 00 03 00 00                  jmp 0x140adc656
00ADC356  E8 A1 6F D4 FF                  call 0x1408232fc
00ADC35B  48 8D 4B 30                     lea rcx, [rbx + 0x30]
00ADC35F  E8 CC 3E 97 FF                  call 0x140450230
00ADC364  48 8D 4B 40                     lea rcx, [rbx + 0x40]
00ADC368  E8 23 61 88 FF                  call 0x140362490
00ADC36D  49 8B CD                        mov rcx, r13
00ADC370  E8 1B 61 88 FF                  call 0x140362490
00ADC375  48 8D 8B E0 01 00 00            lea rcx, [rbx + 0x1e0]
00ADC37C  E8 23 12 09 00                  call 0x140b6d5a4
00ADC381  48 8B CB                        mov rcx, rbx
00ADC384  89 83 E4 01 00 00               mov dword ptr [rbx + 0x1e4], eax
00ADC38A  E8 6D 12 C8 FF                  call 0x14075d5fc
00ADC38F  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00ADC393  E8 64 F8 08 00                  call 0x140b6bbfc
00ADC398  45 33 F6                        xor r14d, r14d
00ADC39B  85 C0                           test eax, eax
00ADC39D  78 1B                           js 0x140adc3ba
00ADC39F  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
00ADC3A3  45 8D 46 04                     lea r8d, [r14 + 4]
00ADC3A7  48 C1 EA 0C                     shr rdx, 0xc
00ADC3AB  48 8B CB                        mov rcx, rbx
00ADC3AE  48 89 93 58 01 00 00            mov qword ptr [rbx + 0x158], rdx
00ADC3B5  E8 3E D1 09 00                  call 0x140b794f8
00ADC3BA  44 38 35 5B E6 32 00            cmp byte ptr [rip + 0x32e65b], r14b
00ADC3C1  74 09                           je 0x140adc3cc
00ADC3C3  44 38 35 FE D8 47 00            cmp byte ptr [rip + 0x47d8fe], r14b
00ADC3CA  74 39                           je 0x140adc405
00ADC3CC  45 33 C9                        xor r9d, r9d
00ADC3CF  4C 8D 05 6A D7 46 00            lea r8, [rip + 0x46d76a]
00ADC3D6  BF 44 62 67 20                  mov edi, 0x20676244
00ADC3DB  48 8B CB                        mov rcx, rbx
00ADC3DE  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00ADC3E2  41 8D 51 02                     lea edx, [r9 + 2]
00ADC3E6  E8 95 01 9A FF                  call 0x14047c580
00ADC3EB  45 33 C9                        xor r9d, r9d
00ADC3EE  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00ADC3F2  4C 8D 05 87 2E 4F 00            lea r8, [rip + 0x4f2e87]
00ADC3F9  48 8B CB                        mov rcx, rbx
00ADC3FC  41 8D 51 02                     lea edx, [r9 + 2]
00ADC400  E8 7B 01 9A FF                  call 0x14047c580
00ADC405  48 8B 15 3C FB 42 00            mov rdx, qword ptr [rip + 0x42fb3c]
00ADC40C  41 B8 00 30 01 00               mov r8d, 0x13000
00ADC412  48 8B CB                        mov rcx, rbx
00ADC415  E8 B6 1F D2 FF                  call 0x1407fe3d0
00ADC41A  48 8B 05 E7 43 32 00            mov rax, qword ptr [rip + 0x3243e7]
00ADC421  48 8B CB                        mov rcx, rbx
00ADC424  E8 A7 E6 BD FF                  call 0x1406baad0
00ADC429  41 8B 45 00                     mov eax, dword ptr [r13]
00ADC42D  C1 E8 03                        shr eax, 3
00ADC430  05 FF 0F 00 00                  add eax, 0xfff
00ADC435  C1 E8 0C                        shr eax, 0xc
00ADC438  8B D0                           mov edx, eax
00ADC43A  89 83 A8 00 00 00               mov dword ptr [rbx + 0xa8], eax
00ADC440  4C 39 B3 10 01 00 00            cmp qword ptr [rbx + 0x110], r14
00ADC447  74 12                           je 0x140adc45b
00ADC449  8B 8B 18 01 00 00               mov ecx, dword ptr [rbx + 0x118]
00ADC44F  3B C8                           cmp ecx, eax
00ADC451  76 08                           jbe 0x140adc45b
00ADC453  89 8B A8 00 00 00               mov dword ptr [rbx + 0xa8], ecx
00ADC459  8B D1                           mov edx, ecx
00ADC45B  8B CA                           mov ecx, edx
00ADC45D  E8 9A 1F 0A 00                  call 0x140b7e3fc
00ADC462  8B BB CC 00 00 00               mov edi, dword ptr [rbx + 0xcc]
00ADC468  48 89 83 A0 00 00 00            mov qword ptr [rbx + 0xa0], rax
00ADC46F  85 FF                           test edi, edi
00ADC471  79 10                           jns 0x140adc483
00ADC473  C7 06 10 00 00 00               mov dword ptr [rsi], 0x10
00ADC479  B9 30 00 00 00                  mov ecx, 0x30
00ADC47E  E9 D3 01 00 00                  jmp 0x140adc656
00ADC483  49 8B 04 24                     mov rax, qword ptr [r12]
00ADC487  44 38 B0 18 01 00 00            cmp byte ptr [rax + 0x118], r14b
00ADC48E  0F 84 AE 00 00 00               je 0x140adc542
00ADC494  48 8B 80 10 01 00 00            mov rax, qword ptr [rax + 0x110]
00ADC49B  48 83 C0 28                     add rax, 0x28
00ADC49F  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00ADC4A3  48 8B 38                        mov rdi, qword ptr [rax]
00ADC4A6  48 3B F8                        cmp rdi, rax
00ADC4A9  0F 84 6E 01 00 00               je 0x140adc61d
00ADC4AF  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
00ADC4B2  85 C0                           test eax, eax
00ADC4B4  74 3D                           je 0x140adc4f3
00ADC4B6  A9 FF 0F 00 00                  test eax, 0xfff
00ADC4BB  75 3F                           jne 0x140adc4fc
00ADC4BD  4C 8D 67 48                     lea r12, [rdi + 0x48]
00ADC4C1  41 BD 02 00 00 00               mov r13d, 2
00ADC4C7  4D 8B 04 24                     mov r8, qword ptr [r12]
00ADC4CB  4D 85 C0                        test r8, r8
00ADC4CE  74 19                           je 0x140adc4e9
00ADC4D0  44 8B 4F 40                     mov r9d, dword ptr [rdi + 0x40]
00ADC4D4  BA 00 80 00 00                  mov edx, 0x8000
00ADC4D9  48 8B CB                        mov rcx, rbx
00ADC4DC  C7 44 24 20 63 62 75 66         mov dword ptr [rsp + 0x20], 0x66756263
00ADC4E4  E8 97 00 9A FF                  call 0x14047c580
00ADC4E9  49 83 C4 08                     add r12, 8
00ADC4ED  49 83 ED 01                     sub r13, 1
00ADC4F1  75 D4                           jne 0x140adc4c7
00ADC4F3  48 8B 3F                        mov rdi, qword ptr [rdi]
00ADC4F6  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00ADC4FA  EB AA                           jmp 0x140adc4a6
00ADC4FC  45 33 C0                        xor r8d, r8d
00ADC4FF  48 8D 4F F8                     lea rcx, [rdi - 8]
00ADC503  41 8D 50 70                     lea edx, [r8 + 0x70]
00ADC507  E8 28 21 AF FF                  call 0x1405ce634
00ADC50C  45 33 C0                        xor r8d, r8d
00ADC50F  BA F0 01 00 00                  mov edx, 0x1f0
00ADC514  48 8B CB                        mov rcx, rbx
00ADC517  E8 18 21 AF FF                  call 0x1405ce634
00ADC51C  B9 31 00 00 00                  mov ecx, 0x31
00ADC521  E8 6A B7 09 00                  call 0x140b77c90
00ADC526  BA 02 01 00 00                  mov edx, 0x102
00ADC52B  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00ADC530  4D 8B CF                        mov r9, r15
00ADC533  41 B8 0A 00 00 00               mov r8d, 0xa
00ADC539  8D 4A 9E                        lea ecx, [rdx - 0x62]
00ADC53C  E8 1F 11 A2 FF                  call 0x1404fd660
00ADC541  CC                              int3
00ADC542  B9 10 00 00 00                  mov ecx, 0x10
00ADC547  E8 B0 1E 0A 00                  call 0x140b7e3fc
00ADC54C  49 89 47 08                     mov qword ptr [r15 + 8], rax
00ADC550  48 85 C0                        test rax, rax
00ADC553  75 21                           jne 0x140adc576
00ADC555  8B BB CC 00 00 00               mov edi, dword ptr [rbx + 0xcc]
00ADC55B  8D 48 32                        lea ecx, [rax + 0x32]
00ADC55E  C7 06 11 00 00 00               mov dword ptr [rsi], 0x11
00ADC564  E8 27 B7 09 00                  call 0x140b77c90
00ADC569  85 FF                           test edi, edi
00ADC56B  0F 88 EA 00 00 00               js 0x140adc65b
00ADC571  E9 52 01 00 00                  jmp 0x140adc6c8
00ADC576  4C 8D 80 00 20 00 00            lea r8, [rax + 0x2000]
00ADC57D  C7 44 24 20 44 6D 65 6D         mov dword ptr [rsp + 0x20], 0x6d656d44
00ADC585  BA 00 80 00 00                  mov edx, 0x8000
00ADC58A  41 B9 00 E0 00 00               mov r9d, 0xe000
00ADC590  48 8B CB                        mov rcx, rbx
00ADC593  E8 E8 FF 99 FF                  call 0x14047c580
00ADC598  41 F7 47 70 FF 0F 00 00         test dword ptr [r15 + 0x70], 0xfff
00ADC5A0  74 46                           je 0x140adc5e8
00ADC5A2  45 33 C0                        xor r8d, r8d
00ADC5A5  BA 08 01 00 00                  mov edx, 0x108
00ADC5AA  49 8B CF                        mov rcx, r15
00ADC5AD  E8 82 20 AF FF                  call 0x1405ce634
00ADC5B2  45 33 C0                        xor r8d, r8d
00ADC5B5  BA F0 01 00 00                  mov edx, 0x1f0
00ADC5BA  48 8B CB                        mov rcx, rbx
00ADC5BD  E8 72 20 AF FF                  call 0x1405ce634
00ADC5C2  B9 33 00 00 00                  mov ecx, 0x33
00ADC5C7  E8 C4 B6 09 00                  call 0x140b77c90
00ADC5CC  BA 02 01 00 00                  mov edx, 0x102
00ADC5D1  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00ADC5D6  4D 8B CF                        mov r9, r15
00ADC5D9  41 B8 0A 00 00 00               mov r8d, 0xa
00ADC5DF  8D 4A 9E                        lea ecx, [rdx - 0x62]
00ADC5E2  E8 79 10 A2 FF                  call 0x1404fd660
00ADC5E7  CC                              int3
00ADC5E8  49 8D 7F 10                     lea rdi, [r15 + 0x10]
00ADC5EC  41 BE 02 00 00 00               mov r14d, 2
00ADC5F2  4C 8B 07                        mov r8, qword ptr [rdi]
00ADC5F5  4D 85 C0                        test r8, r8
00ADC5F8  74 19                           je 0x140adc613
00ADC5FA  45 8B 4F 70                     mov r9d, dword ptr [r15 + 0x70]
00ADC5FE  BA 00 80 00 00                  mov edx, 0x8000
00ADC603  48 8B CB                        mov rcx, rbx
00ADC606  C7 44 24 20 63 62 75 66         mov dword ptr [rsp + 0x20], 0x66756263
00ADC60E  E8 6D FF 99 FF                  call 0x14047c580
00ADC613  48 83 C7 08                     add rdi, 8
00ADC617  49 83 EE 01                     sub r14, 1
00ADC61B  75 D5                           jne 0x140adc5f2
00ADC61D  45 33 F6                        xor r14d, r14d
00ADC620  44 38 35 5D A4 4E 00            cmp byte ptr [rip + 0x4ea45d], r14b
00ADC627  74 39                           je 0x140adc662
00ADC629  4C 8D 83 00 01 00 00            lea r8, [rbx + 0x100]
00ADC630  C6 83 E8 01 00 00 01            mov byte ptr [rbx + 0x1e8], 1
00ADC637  48 8D 93 08 01 00 00            lea rdx, [rbx + 0x108]
00ADC63E  48 8B CB                        mov rcx, rbx
00ADC641  E8 42 C1 C3 FF                  call 0x140718788
00ADC646  8B F8                           mov edi, eax
00ADC648  85 C0                           test eax, eax
00ADC64A  79 1D                           jns 0x140adc669
00ADC64C  C7 06 13 00 00 00               mov dword ptr [rsi], 0x13
00ADC652  41 8D 4E 35                     lea ecx, [r14 + 0x35]
00ADC656  E8 35 B6 09 00                  call 0x140b77c90
00ADC65B  E8 BC 88 C2 FF                  call 0x140704f1c
00ADC660  EB 66                           jmp 0x140adc6c8
00ADC662  44 88 B3 E8 01 00 00            mov byte ptr [rbx + 0x1e8], r14b
00ADC669  45 33 C9                        xor r9d, r9d
00ADC66C  48 8D 55 48                     lea rdx, [rbp + 0x48]
00ADC670  B9 91 00 00 00                  mov ecx, 0x91
00ADC675  45 8D 41 02                     lea r8d, [r9 + 2]
00ADC679  E8 12 11 BD FF                  call 0x1406ad790
00ADC67E  85 C0                           test eax, eax
00ADC680  78 09                           js 0x140adc68b
00ADC682  8A 45 48                        mov al, byte ptr [rbp + 0x48]
00ADC685  88 83 E9 01 00 00               mov byte ptr [rbx + 0x1e9], al
00ADC68B  48 8B CB                        mov rcx, rbx
00ADC68E  E8 39 74 08 00                  call 0x140b63acc
00ADC693  85 C0                           test eax, eax
00ADC695  78 07                           js 0x140adc69e
00ADC697  C6 05 FE 16 43 00 01            mov byte ptr [rip + 0x4316fe], 1
00ADC69E  8B 83 20 01 00 00               mov eax, dword ptr [rbx + 0x120]
00ADC6A4  FF C8                           dec eax
00ADC6A6  89 83 D0 00 00 00               mov dword ptr [rbx + 0xd0], eax
00ADC6AC  E8 57 83 AF FF                  call 0x1405d4a08
00ADC6B1  F7 D8                           neg eax
00ADC6B3  1B D2                           sbb edx, edx
00ADC6B5  33 C9                           xor ecx, ecx
00ADC6B7  81 E2 F0 00 00 00               and edx, 0xf0
00ADC6BD  83 C2 10                        add edx, 0x10
00ADC6C0  E8 0F C0 C3 FF                  call 0x1407186d4
00ADC6C5  41 8B FE                        mov edi, r14d
00ADC6C8  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
00ADC6D0  8B C7                           mov eax, edi
00ADC6D2  48 83 C4 40                     add rsp, 0x40
00ADC6D6  41 5F                           pop r15
00ADC6D8  41 5E                           pop r14
00ADC6DA  41 5D                           pop r13
00ADC6DC  41 5C                           pop r12
00ADC6DE  5F                              pop rdi
00ADC6DF  5E                              pop rsi
00ADC6E0  5D                              pop rbp
00ADC6E1  C3                              ret
00ADC6E2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopAllocateHiberContext(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m58;
    unsigned __int16 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (64);
    v_r14 = 0;
    v_stack_p20 = 0;
    v_stack_m48 = 0;
    v_stack_p10 = 0;
    if ((*(unsigned int *)(v_rip + 4390132)) != 5) goto loc_00ADC6C5;
    a2 = 0;
    v_stack_p18 = 0;
    *(unsigned __int64 *)(v_rip + 4390112) = *(unsigned __int64 *)(v_rip + 4390606);
    result = memset(*(unsigned __int64 *)(v_rip + 4390606), a2, 496, a4);
    result = Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_rip + 4390606), a2, 496, a4);
    if ((unsigned int)(result) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4390606) + 493) = 1;
    }
    result = Feature_Servicing_ARM64_LLVMHibernate__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_rip + 4390606), a2, 496, a4);
    if ((unsigned int)(result) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4390606) + 494) = 1;
    }
    result = MmLockPreChargedPagedPool(*(unsigned __int64 *)(v_rip + 4390541), *(unsigned __int64 *)(v_rip + 4390556), 496, a4);
    *(unsigned int *)(v_rip + 3716606) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 32) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 64) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 216) = *(unsigned __int64 *)(v_rip + 4390509);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 352) = *(unsigned __int64 *)(v_rip + 4390591);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 232) = *(unsigned __int64 *)(v_rip + 4390545);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 240) = *(unsigned __int64 *)(v_rip + 4390579);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 248) = *(unsigned __int64 *)(v_rip + 4390557);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 48) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 80 + 8) = *(unsigned __int64 *)(v_rip + 4390606) + 80;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 80) = *(unsigned __int64 *)(v_rip + 4390606) + 80;
    if ((*(unsigned __int64 *)(v_rip + 4390328)) != 0) goto loc_00ADC187;
    *(unsigned int *)(a1) = 10;
    goto loc_00ADC656;
loc_00ADC187:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4394366))) & (16));
    result = IoGetDumpStack(42, *(unsigned __int64 *)(v_rip + 4390606) + 184, 496, a4);
    if (!sign_flag) goto loc_00ADC1B7;
    *(unsigned int *)(a1) = 10;
    goto loc_00ADC656;
loc_00ADC1B7:
    if (sign_flag) {
        a1 = 0;
        if ((*(unsigned int *)(v_rip + 4389760)) == 2) { a1 = 2; }
    }
    a1 = (unsigned __int8)((a1) | (1));
    a2 = (unsigned int)((v_cr4) & (0x1000ULL));
    result = (unsigned __int8)(((unsigned __int8)((unsigned __int8)(a1))) | (8));
    a1 = (unsigned __int8)(result);
    if (a2 == 0) { a1 = (unsigned int)((unsigned __int8)(a1)); }
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4390606)) = (unsigned __int8)(a1);
    a1 = (*(unsigned __int64 *)(v_rip + 4390269)) & (0xFFFFFFFFFFFFF000ULL);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 232)) = 0;
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 4390269)))))) & ((unsigned int)(0xFFFULL));
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 232) + 10) = 0;
    result = (result) + (0x18FFFULL);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 232) + 32) = a1;
    result = (result) >> (12);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 4390269)))) & ((unsigned int)((unsigned int)(0xFFFULL))));
    result = (unsigned __int16)((result) + (6));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 232) + 44) = a2;
    result = (unsigned __int16)((result) << (3));
    *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 232) + 8) = (unsigned __int16)(result);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 232) + 40) = 0x18000ULL;
    result = MmBuildMdlForNonPagedPool(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 232), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 232), a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 240) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 4390271);
        a3 = 0x1FFFULL;
        result = (unsigned __int16)(a1);
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 240)) = 0;
        result = (unsigned __int16)((result) & ((unsigned __int16)((unsigned int)(0xFFFULL))));
        *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 240) + 10) = 0;
        result = (unsigned __int16)((result) + ((unsigned __int16)(a3)));
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 240) + 40) = 0x1000ULL;
        result = (unsigned __int16)((result) >> (12));
        result = (unsigned __int16)((result) + (6));
        result = (unsigned __int16)((result) << (3));
        *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 240) + 8) = (unsigned __int16)(result);
        result = a1;
        a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(0xFFFULL))));
        result = (result) & (0xFFFFFFFFFFFFF000ULL);
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 240) + 32) = result;
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 240) + 44) = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 240);
        result = MmBuildMdlForNonPagedPool(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 240), a3, a4);
    }
    result = PopLoadResumeContext(*(unsigned __int64 *)(v_rip + 4390606), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 240), a3, a4);
    if (!sign_flag) goto loc_00ADC2D4;
    *(unsigned int *)(a1) = 12;
    goto loc_00ADC656;
loc_00ADC2D4:
    result = BcdOpenStore(44, 2, v_stack_p20, a4);
    if (!sign_flag) goto loc_00ADC2F8;
    *(unsigned int *)(a1) = 13;
    goto loc_00ADC656;
loc_00ADC2F8:
    result = PopBcdEstablishResumeObject(v_stack_p20, v_stack_p18, v_stack_p20, a4);
    if (!sign_flag) goto loc_00ADC326;
    *(unsigned int *)(a1) = 14;
    result = BcdCloseStore(v_stack_p20, v_stack_p18, v_stack_p20, a4);
    goto loc_00ADC656;
loc_00ADC326:
    result = PopBcdSetPendingResume(46, v_stack_p18, v_stack_p20, v_stack_p18);
    result = BcdCloseObject(v_stack_p18, v_stack_p18, v_stack_p20, v_stack_p18);
    if (!sign_flag) goto loc_00ADC356;
    *(unsigned int *)(a1) = 15;
    result = BcdCloseStore(v_stack_p20, v_stack_p18, v_stack_p20, v_stack_p18);
    goto loc_00ADC656;
loc_00ADC356:
    result = BcdForciblyUnloadStore(47, v_stack_p18, v_stack_p20, v_stack_p18);
    result = RtlClearAllBits(*(unsigned __int64 *)(v_rip + 4390606) + 48, v_stack_p18, v_stack_p20, v_stack_p18);
    result = RtlSetAllBits(*(unsigned __int64 *)(v_rip + 4390606) + 64, v_stack_p18, v_stack_p20, v_stack_p18);
    result = RtlSetAllBits(*(unsigned __int64 *)(v_rip + 4390606) + 32, v_stack_p18, v_stack_p20, v_stack_p18);
    result = PopGetHwConfigurationSignature(*(unsigned __int64 *)(v_rip + 4390606) + 480, v_stack_p18, v_stack_p20, v_stack_p18);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4390606) + 484) = (unsigned int)(result);
    result = PopHiberInitializeResources(*(unsigned __int64 *)(v_rip + 4390606), v_stack_p18, v_stack_p20, v_stack_p18);
    result = PopGetBitlockerKeyLocation(v_stack_m48, v_stack_p18, v_stack_p20, v_stack_p18);
    v_r14 = 0;
    if (!(sign_flag)) {
        a2 = v_stack_m48;
        a3 = v_r14 + 4;
        a2 = (a2) >> (12);
        a1 = *(unsigned __int64 *)(v_rip + 4390606);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 344) = a2;
        result = PopDiscardRange(a1, a2, a3, v_stack_p18);
    }
    if ((*(unsigned __int8 *)(v_rip + 3335771)) == 0) goto loc_00ADC3CC;
    v_rdi = (unsigned int)((unsigned int)(result));
    if ((*(unsigned __int8 *)(v_rip + 4708606)) != 0) {
        a4 = 0;
        a3 = v_rip + 4642666;
        v_rdi = 0x20676244ULL;
        a1 = *(unsigned __int64 *)(v_rip + 4390606);
        v_stack_m58 = (unsigned int)(v_rdi);
        a2 = a4 + 2;
        result = PoSetHiberRange(a1, a2, a3, a4);
        a4 = 0;
        v_stack_m58 = (unsigned int)(v_rdi);
        a3 = v_rip + 5189255;
        a1 = *(unsigned __int64 *)(v_rip + 4390606);
        a2 = a4 + 2;
        result = PoSetHiberRange(a1, a2, a3, a4);
    }
    result = MmMarkHiberRange(*(unsigned __int64 *)(v_rip + 4390606), *(unsigned __int64 *)(v_rip + 4389692), (unsigned int)(0x13000ULL), a4);
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 4390606), *(unsigned __int64 *)(v_rip + 4389692), (unsigned int)(0x13000ULL), a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4390606) + 32))) >> (3));
    result = (unsigned int)((result) + (0xFFFULL));
    result = (unsigned int)((result) >> (12));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4390606) + 168) = (unsigned int)(result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 272)) == 0) goto loc_00ADC45B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4390606) + 280)))) >= = ((unsigned int)(result))) {
        *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4390606) + 168) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4390606) + 280)));
        a2 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4390606) + 280)));
    }
    result = PopAllocatePages((unsigned int)(a2), a2, (unsigned int)(0x13000ULL), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 160) = result;
    if (!sign_flag) goto loc_00ADC483;
    *(unsigned int *)(a1) = 16;
    goto loc_00ADC656;
loc_00ADC483:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184) + 280)) == 0) goto loc_00ADC542;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184) + 272)) + (40);
    v_stack_p18 = result;
loc_00ADC4A6:
    if ((*(unsigned __int64 *)(result)) == result) goto loc_00ADC61D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result) + 64))) == 0) goto loc_00ADC4F3;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result) + 64)))) & (0xFFFULL)) != 0) goto loc_00ADC4FC;
loc_00ADC4C7:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result) + 64));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 72) != 0) {
        a4 = *(unsigned int *)(*(unsigned __int64 *)(result) + 64);
        a2 = 0x8000ULL;
        a1 = *(unsigned __int64 *)(v_rip + 4390606);
        v_stack_m58 = 0x66756263ULL;
        result = PoSetHiberRange(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 72), a4);
    }
    v_r12 = (*(unsigned __int64 *)(result) + 72) + (8);
    v_r13 = (2) - (1);
    if (condition_is_not_equal) goto loc_00ADC4C7;
loc_00ADC4F3:
    goto loc_00ADC4A6;
loc_00ADC4FC:
    a3 = 0;
    result = PopInternalAddToDumpFile(*(unsigned __int64 *)(*(unsigned __int64 *)(result)) - 8, a3 + 112, a3, a4);
    a3 = 0;
    result = PopInternalAddToDumpFile(*(unsigned __int64 *)(v_rip + 4390606), 496, a3, a4);
    result = PopCheckpointSystemSleep(49, 496, a3, a4);
    v_stack_m58 = *(unsigned __int64 *)(v_rip + 4390606);
    result = KeBugCheckEx(258 - 98, 258, 10, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184));
loc_00ADC542:
    result = PopAllocatePages(16, 258, 10, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184) + 8) = result;
    if (result != 0) goto loc_00ADC576;
    *(unsigned int *)(a1) = 17;
    result = PopCheckpointSystemSleep(result + 50, 258, 10, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184));
    if (sign_flag) goto loc_00ADC65B;
    goto loc_00ADC6C8;
loc_00ADC576:
    v_stack_m58 = 0x6D656D44ULL;
    result = PoSetHiberRange(*(unsigned __int64 *)(v_rip + 4390606), (unsigned int)(0x8000ULL), result + 8192, (unsigned int)(0xE000ULL));
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184) + 112)) & (0xFFFULL)) != 0) {
        a3 = 0;
        a2 = 264;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184);
        result = PopInternalAddToDumpFile(a1, a2, a3, (unsigned int)(0xE000ULL));
        a3 = 0;
        a2 = 496;
        a1 = *(unsigned __int64 *)(v_rip + 4390606);
        result = PopInternalAddToDumpFile(a1, a2, a3, (unsigned int)(0xE000ULL));
        a1 = 51;
        result = PopCheckpointSystemSleep(a1, a2, a3, (unsigned int)(0xE000ULL));
        a2 = 258;
        v_stack_m58 = *(unsigned __int64 *)(v_rip + 4390606);
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184);
        a3 = 10;
        a1 = a2 - 98;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
loc_00ADC5F2:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184) + 16) != 0) {
        a4 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184) + 112);
        a2 = 0x8000ULL;
        a1 = *(unsigned __int64 *)(v_rip + 4390606);
        v_stack_m58 = 0x66756263ULL;
        result = PoSetHiberRange(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184) + 16), a4);
    }
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4390606) + 184) + 16) + (8);
    v_r14 = (2) - (1);
    if (condition_is_not_equal) goto loc_00ADC5F2;
loc_00ADC61D:
    v_r14 = 0;
    if ((*(unsigned __int8 *)(v_rip + 5153885)) == 0) goto loc_00ADC662;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4390606) + 488) = 1;
    result = VslAllocateSecureHibernateResources(*(unsigned __int64 *)(v_rip + 4390606), *(unsigned __int64 *)(v_rip + 4390606) + 264, *(unsigned __int64 *)(v_rip + 4390606) + 256, a4);
    if (!sign_flag) goto loc_00ADC669;
    *(unsigned int *)(a1) = 19;
loc_00ADC656:
    result = PopCheckpointSystemSleep(v_r14 + 53, *(unsigned __int64 *)(v_rip + 4390606) + 264, *(unsigned __int64 *)(v_rip + 4390606) + 256, a4);
loc_00ADC65B:
    result = PopFreeHiberContext(v_r14 + 53, *(unsigned __int64 *)(v_rip + 4390606) + 264, *(unsigned __int64 *)(v_rip + 4390606) + 256, a4);
    goto loc_00ADC6C8;
loc_00ADC662:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4390606) + 488) = 0;
loc_00ADC669:
    a4 = 0;
    result = ZwQuerySystemInformation(145, v_stack_p10, a4 + 2, a4);
    if (!(sign_flag)) {
        result = v_stack_p10;
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4390606) + 489) = (unsigned __int8)(result);
    }
    result = BgkResumePrepare(*(unsigned __int64 *)(v_rip + 4390606), v_stack_p10, a4 + 2, a4);
    if (!(sign_flag)) {
        *(unsigned __int8 *)(v_rip + 4396798) = 1;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4390606) + 288))) - 1);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4390606) + 208) = (unsigned int)(result);
    result = Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_rip + 4390606), v_stack_p10, a4 + 2, a4);
    result = (unsigned int)(-(result));
    a1 = 0;
    a2 = (unsigned int)((v_stack_p10) & (240));
    a2 = (unsigned int)((a2) + (16));
    result = HvlAllocateHibernateResources(a1, a2, a4 + 2, a4);
loc_00ADC6C5:
loc_00ADC6C8:
    v_rsp = (v_rsp) + (64);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t PopAllocateHiberContext(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint32_t v_stack_m58;
    uint16_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (64);
    local_r14 = 0;
    v_stack_p20 = 0;
    v_stack_m48 = 0;
    v_stack_p10 = 0;
    if ((*(uint32_t *)(v_rip + 0x42FCF4)) != 5) goto loc_00ADC6C5;
    Arg2 = 0;
    v_stack_p18 = 0;
    *(uint64_t *)(v_rip + 0x42FCE0) = *(uint64_t *)(v_rip + 0x42FECE);
    result = memset(*(uint64_t *)(v_rip + 0x42FECE), Arg2, 496, a4);
    result = Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(v_rip + 0x42FECE), Arg2, 496, a4);
    if ((uint32_t)(result) != 0) {
        *(uint8_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x1ED) = 1;
    }
    result = Feature_Servicing_ARM64_LLVMHibernate__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(v_rip + 0x42FECE), Arg2, 496, a4);
    if ((uint32_t)(result) != 0) {
        *(uint8_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x1EE) = 1;
    }
    result = MmLockPreChargedPagedPool(*(uint64_t *)(v_rip + 0x42FE8D), *(uint64_t *)(v_rip + 0x42FE9C), 496, a4);
    *(uint32_t *)(v_rip + 0x38B5FE) = 0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x20) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x40) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xD8) = *(uint64_t *)(v_rip + 0x42FE6D);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x160) = *(uint64_t *)(v_rip + 0x42FEBF);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xE8) = *(uint64_t *)(v_rip + 0x42FE91);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xF0) = *(uint64_t *)(v_rip + 0x42FEB3);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xF8) = *(uint64_t *)(v_rip + 0x42FE9D);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x30) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x50 + 0x8) = *(uint64_t *)(v_rip + 0x42FECE) + 80;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x50) = *(uint64_t *)(v_rip + 0x42FECE) + 80;
    if ((*(uint64_t *)(v_rip + 0x42FDB8)) != 0) goto loc_00ADC187;
    *(uint32_t *)(arg1) = 10;
    goto loc_00ADC656;
loc_00ADC187:
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x430D7E))) & (16));
    result = IoGetDumpStack(42, *(uint64_t *)(v_rip + 0x42FECE) + 184, 496, a4);
    if (!sign_flag) goto loc_00ADC1B7;
    *(uint32_t *)(arg1) = 10;
    goto loc_00ADC656;
loc_00ADC1B7:
    if (sign_flag) {
        Arg1 = 0;
        if ((*(uint32_t *)(v_rip + 0x42FB80)) == 2) { Arg1 = 2; }
    }
    Arg1 = (uint8_t)((Arg1) | (1));
    Arg2 = (uint32_t)((v_cr4) & (0x1000ULL));
    result = (uint8_t)(((uint8_t)((uint8_t)(Arg1))) | (8));
    Arg1 = (uint8_t)(result);
    if (Arg2 == 0) { Arg1 = (uint32_t)((uint8_t)(Arg1)); }
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x42FECE)) = (uint8_t)(Arg1);
    Arg1 = (*(uint64_t *)(v_rip + 0x42FD7D)) & (0xFFFFFFFFFFFFF000ULL);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xE8)) = 0;
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0x42FD7D)))))) & ((uint32_t)(0xFFFULL));
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xE8) + 0xA) = 0;
    result = (result) + (0x18FFFULL);
    *(void **)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xE8) + 0x20) = Arg1;
    result = (result) >> (12);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0x42FD7D)))) & ((uint32_t)((uint32_t)(0xFFFULL))));
    result = (uint16_t)((result) + (6));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xE8) + 0x2C) = Arg2;
    result = (uint16_t)((result) << (3));
    *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xE8) + 0x8) = (uint16_t)(result);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xE8) + 0x28) = 0x18000ULL;
    result = MmBuildMdlForNonPagedPool(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xE8), Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xE8), a4);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xF0) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x42FD7F);
        a3 = 0x1FFFULL;
        result = (uint16_t)(Arg1);
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xF0)) = 0;
        result = (uint16_t)((result) & ((uint16_t)((uint32_t)(0xFFFULL))));
        *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xF0) + 0xA) = 0;
        result = (uint16_t)((result) + ((uint16_t)(a3)));
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xF0) + 0x28) = 0x1000ULL;
        result = (uint16_t)((result) >> (12));
        result = (uint16_t)((result) + (6));
        result = (uint16_t)((result) << (3));
        *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xF0) + 0x8) = (uint16_t)(result);
        result = Arg1;
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(0xFFFULL))));
        result = (result) & (0xFFFFFFFFFFFFF000ULL);
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xF0) + 0x20) = result;
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xF0) + 0x2C) = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xF0);
        result = MmBuildMdlForNonPagedPool(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xF0), a3, a4);
    }
    result = PopLoadResumeContext(*(uint64_t *)(v_rip + 0x42FECE), *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xF0), a3, a4);
    if (!sign_flag) goto loc_00ADC2D4;
    *(uint32_t *)(arg1) = 12;
    goto loc_00ADC656;
loc_00ADC2D4:
    result = BcdOpenStore(44, 2, v_stack_p20, a4);
    if (!sign_flag) goto loc_00ADC2F8;
    *(uint32_t *)(arg1) = 13;
    goto loc_00ADC656;
loc_00ADC2F8:
    result = PopBcdEstablishResumeObject(v_stack_p20, v_stack_p18, v_stack_p20, a4);
    if (!sign_flag) goto loc_00ADC326;
    *(uint32_t *)(arg1) = 14;
    result = BcdCloseStore(v_stack_p20, v_stack_p18, v_stack_p20, a4);
    goto loc_00ADC656;
loc_00ADC326:
    result = PopBcdSetPendingResume(46, v_stack_p18, v_stack_p20, v_stack_p18);
    result = BcdCloseObject(v_stack_p18, v_stack_p18, v_stack_p20, v_stack_p18);
    if (!sign_flag) goto loc_00ADC356;
    *(uint32_t *)(arg1) = 15;
    result = BcdCloseStore(v_stack_p20, v_stack_p18, v_stack_p20, v_stack_p18);
    goto loc_00ADC656;
loc_00ADC356:
    result = BcdForciblyUnloadStore(47, v_stack_p18, v_stack_p20, v_stack_p18);
    result = RtlClearAllBits(*(uint64_t *)(v_rip + 0x42FECE) + 48, v_stack_p18, v_stack_p20, v_stack_p18);
    result = RtlSetAllBits(*(uint64_t *)(v_rip + 0x42FECE) + 64, v_stack_p18, v_stack_p20, v_stack_p18);
    result = RtlSetAllBits(*(uint64_t *)(v_rip + 0x42FECE) + 32, v_stack_p18, v_stack_p20, v_stack_p18);
    result = PopGetHwConfigurationSignature(*(uint64_t *)(v_rip + 0x42FECE) + 480, v_stack_p18, v_stack_p20, v_stack_p18);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x1E4) = (uint32_t)(result);
    result = PopHiberInitializeResources(*(uint64_t *)(v_rip + 0x42FECE), v_stack_p18, v_stack_p20, v_stack_p18);
    result = PopGetBitlockerKeyLocation(v_stack_m48, v_stack_p18, v_stack_p20, v_stack_p18);
    local_r14 = 0;
    if (!(sign_flag)) {
        Arg2 = v_stack_m48;
        a3 = local_r14 + 4;
        Arg2 = (Arg2) >> (12);
        Arg1 = *(uint64_t *)(v_rip + 0x42FECE);
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x158) = Arg2;
        result = PopDiscardRange(Arg1, Arg2, a3, v_stack_p18);
    }
    if ((*(uint8_t *)(v_rip + 0x32E65B)) == 0) goto loc_00ADC3CC;
    local_rdi = (uint32_t)((uint32_t)(result));
    if ((*(uint8_t *)(v_rip + 0x47D8FE)) != 0) {
        a4 = 0;
        a3 = v_rip + 4642666;
        local_rdi = 0x20676244ULL;
        Arg1 = *(uint64_t *)(v_rip + 0x42FECE);
        v_stack_m58 = (uint32_t)(local_rdi);
        Arg2 = a4 + 2;
        result = PoSetHiberRange(Arg1, Arg2, a3, a4);
        a4 = 0;
        v_stack_m58 = (uint32_t)(local_rdi);
        a3 = v_rip + 5189255;
        Arg1 = *(uint64_t *)(v_rip + 0x42FECE);
        Arg2 = a4 + 2;
        result = PoSetHiberRange(Arg1, Arg2, a3, a4);
    }
    result = MmMarkHiberRange(*(uint64_t *)(v_rip + 0x42FECE), *(uint64_t *)(v_rip + 0x42FB3C), (uint32_t)(0x13000ULL), a4);
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0x42FECE), *(uint64_t *)(v_rip + 0x42FB3C), (uint32_t)(0x13000ULL), a4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x20))) >> (3));
    result = (uint32_t)((result) + (0xFFFULL));
    result = (uint32_t)((result) >> (12));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xA8) = (uint32_t)(result);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x110)) == 0) goto loc_00ADC45B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x118)))) >= = ((uint32_t)(result))) {
        *(uint32_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xA8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x118)));
        Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x118)));
    }
    result = PopAllocatePages((uint32_t)(Arg2), Arg2, (uint32_t)(0x13000ULL), a4);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xA0) = result;
    if (!sign_flag) goto loc_00ADC483;
    *(uint32_t *)(arg1) = 16;
    goto loc_00ADC656;
loc_00ADC483:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8) + 0x118)) == 0) goto loc_00ADC542;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8) + 0x110)) + (40);
    v_stack_p18 = result;
loc_00ADC4A6:
    if ((*(uint64_t *)(result)) == result) goto loc_00ADC61D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result) + 0x40))) == 0) goto loc_00ADC4F3;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result) + 0x40)))) & (0xFFFULL)) != 0) goto loc_00ADC4FC;
loc_00ADC4C7:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(result) + 0x40));
    if (*(uint64_t *)(*(uint64_t *)(result) + 0x48) != 0) {
        a4 = *(uint32_t *)(*(uint64_t *)(result) + 0x40);
        Arg2 = 0x8000ULL;
        Arg1 = *(uint64_t *)(v_rip + 0x42FECE);
        v_stack_m58 = 0x66756263ULL;
        result = PoSetHiberRange(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(result) + 0x48), a4);
    }
    local_r12 = (*(uint64_t *)(result) + 72) + (8);
    local_r13 = (2) - (1);
    if (condition_is_not_equal) goto loc_00ADC4C7;
loc_00ADC4F3:
    goto loc_00ADC4A6;
loc_00ADC4FC:
    a3 = 0;
    result = PopInternalAddToDumpFile(*(uint64_t *)(*(uint64_t *)(result)) - 8, a3 + 112, a3, a4);
    a3 = 0;
    result = PopInternalAddToDumpFile(*(uint64_t *)(v_rip + 0x42FECE), 496, a3, a4);
    result = PopCheckpointSystemSleep(49, 496, a3, a4);
    v_stack_m58 = *(uint64_t *)(v_rip + 0x42FECE);
    result = KeBugCheckEx(258 - 98, 258, 10, *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8));
loc_00ADC542:
    result = PopAllocatePages(16, 258, 10, *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8) + 0x8) = result;
    if (result != 0) goto loc_00ADC576;
    *(uint32_t *)(arg1) = 17;
    result = PopCheckpointSystemSleep(result + 50, 258, 10, *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8));
    if (sign_flag) goto loc_00ADC65B;
    goto loc_00ADC6C8;
loc_00ADC576:
    v_stack_m58 = 0x6D656D44ULL;
    result = PoSetHiberRange(*(uint64_t *)(v_rip + 0x42FECE), (uint32_t)(0x8000ULL), result + 8192, (uint32_t)(0xE000ULL));
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8) + 0x70)) & (0xFFFULL)) != 0) {
        a3 = 0;
        Arg2 = 264;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8);
        result = PopInternalAddToDumpFile(Arg1, Arg2, a3, (uint32_t)(0xE000ULL));
        a3 = 0;
        Arg2 = 496;
        Arg1 = *(uint64_t *)(v_rip + 0x42FECE);
        result = PopInternalAddToDumpFile(Arg1, Arg2, a3, (uint32_t)(0xE000ULL));
        Arg1 = 51;
        result = PopCheckpointSystemSleep(Arg1, Arg2, a3, (uint32_t)(0xE000ULL));
        Arg2 = 258;
        v_stack_m58 = *(uint64_t *)(v_rip + 0x42FECE);
        a4 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8);
        a3 = 10;
        Arg1 = Arg2 - 98;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
loc_00ADC5F2:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8) + 0x10) != 0) {
        a4 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8) + 0x70);
        Arg2 = 0x8000ULL;
        Arg1 = *(uint64_t *)(v_rip + 0x42FECE);
        v_stack_m58 = 0x66756263ULL;
        result = PoSetHiberRange(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8) + 0x10), a4);
    }
    local_rdi = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xB8) + 16) + (8);
    local_r14 = (2) - (1);
    if (condition_is_not_equal) goto loc_00ADC5F2;
loc_00ADC61D:
    local_r14 = 0;
    if ((*(uint8_t *)(v_rip + 0x4EA45D)) == 0) goto loc_00ADC662;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x1E8) = 1;
    result = VslAllocateSecureHibernateResources(*(uint64_t *)(v_rip + 0x42FECE), *(uint64_t *)(v_rip + 0x42FECE) + 264, *(uint64_t *)(v_rip + 0x42FECE) + 256, a4);
    if (!sign_flag) goto loc_00ADC669;
    *(uint32_t *)(arg1) = 19;
loc_00ADC656:
    result = PopCheckpointSystemSleep(local_r14 + 53, *(uint64_t *)(v_rip + 0x42FECE) + 264, *(uint64_t *)(v_rip + 0x42FECE) + 256, a4);
loc_00ADC65B:
    result = PopFreeHiberContext(local_r14 + 53, *(uint64_t *)(v_rip + 0x42FECE) + 264, *(uint64_t *)(v_rip + 0x42FECE) + 256, a4);
    goto loc_00ADC6C8;
loc_00ADC662:
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x1E8) = 0;
loc_00ADC669:
    a4 = 0;
    result = ZwQuerySystemInformation(145, v_stack_p10, a4 + 2, a4);
    if (!(sign_flag)) {
        result = v_stack_p10;
        *(uint8_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x1E9) = (uint8_t)(result);
    }
    result = BgkResumePrepare(*(uint64_t *)(v_rip + 0x42FECE), v_stack_p10, a4 + 2, a4);
    if (!(sign_flag)) {
        *(uint8_t *)(v_rip + 0x4316FE) = 1;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0x120))) - 1);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x42FECE) + 0xD0) = (uint32_t)(result);
    result = Feature_CrashDumpOneMBTransferSize__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(v_rip + 0x42FECE), v_stack_p10, a4 + 2, a4);
    result = (uint32_t)(-(result));
    Arg1 = 0;
    Arg2 = (uint32_t)((v_stack_p10) & (240));
    Arg2 = (uint32_t)((Arg2) + (16));
    result = HvlAllocateHibernateResources(Arg1, Arg2, a4 + 2, a4);
loc_00ADC6C5:
loc_00ADC6C8:
    local_rsp = (local_rsp) + (64);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ADC05C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
