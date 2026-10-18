# KiExecuteAllDpcs

- RVA: `0x0025B740`–`0x0025CBEE` (길이 `5,294` bytes)
- VA: `0x000000014025B740`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064050`
- 디코드: `1,160`개 명령, `5,294/5,294` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **48**; 고유 호출 대상: **39**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x0025B8CC` → [KiAcquireSpinLockInstrumented](../20/KiAcquireSpinLockInstrumented_function_002084F0.md) (function, `0x002084F0`)
- `0x0025BA00` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x0025BC07` → [KiAbProcessThreadLocks](../22/KiAbProcessThreadLocks_function_00221D30.md) (function, `0x00221D30`)
- `0x0025BC25` → [KiAbPropagateBoosts](../22/KiAbPropagateBoosts_function_00222E60.md) (function, `0x00222E60`)
- `0x0025BC73` → [KiDeferredReadySingleThread](KiDeferredReadySingleThread_function_00252FE0.md) (function, `0x00252FE0`)
- `0x0025BC9F` → [KiFlushSoftwareInterruptBatch](KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x0025BCC9` → [KiSendSoftwareInterruptAffinity](../30/KiSendSoftwareInterruptAffinity_function_0030E834.md) (function, `0x0030E834`)
- `0x0025BD60` → [HalpInterruptSendIpi](HalpInterruptSendIpi_function_00252310.md) (function, `0x00252310`)
- `0x0025BD84` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0025BDB0` → [KiSwapDirectoryTableBaseTarget](../22/KiSwapDirectoryTableBaseTarget_function_00227FF0.md) (function, `0x00227FF0`)
- `0x0025BDC6` → [PpmPerfAction](../2D/PpmPerfAction_function_002D7E70.md) (function, `0x002D7E70`)
- `0x0025BDCD` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0025C094` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0025C0A9` → [KxWaitForSpinLockAndAcquire](../20/KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)
- `0x0025C0DE` → [KxReleaseSpinLock](../20/KxReleaseSpinLock_function_00206670.md) (function, `0x00206670`)
- `0x0025C0FC` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0025C19F` → [KiFlushSoftwareInterruptBatch](KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x0025C1BC` → [KiReadyDeferredReadyList](../30/KiReadyDeferredReadyList_function_0030DD80.md) (function, `0x0030DD80`)
- `0x0025C231` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0025C2C9` → [KeAddProcessorAffinityEx](KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x0025C2E0` → [KeAddGroupAffinityEx](KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x0025C377` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x0025C3B9` → [EtwTraceScheduleThread](../30/EtwTraceScheduleThread_function_0030B74C.md) (function, `0x0030B74C`)
- `0x0025C3EE` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0025C41E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0025C4EA` → [EtwpLogKernelEvent](EtwpLogKernelEvent_function_0025CC00.md) (function, `0x0025CC00`)
- `0x0025C598` → [KiAcquireMultiplePrcbLocks](../39/KiAcquireMultiplePrcbLocks_function_00393160.md) (function, `0x00393160`)
- `0x0025C5E1` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0025C5F4` → [KiStartRescheduleContext](../30/KiStartRescheduleContext_function_0030C6B0.md) (function, `0x0030C6B0`)
- `0x0025C634` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x0025C739` → [KiInsertNewDpcRuntime](../3F/KiInsertNewDpcRuntime_function_003FE4CC.md) (function, `0x003FE4CC`)
- `0x0025C761` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0025C77D` → [KiEnterLongDpcProcessing](../30/KiEnterLongDpcProcessing_function_0030BE54.md) (function, `0x0030BE54`)
- `0x0025C78D` → [RtlGetSystemTimePrecise](../37/RtlGetSystemTimePrecise_function_0037EDD0.md) (function, `0x0037EDD0`)
- `0x0025C7B8` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x0025C7DE` → [EtwTraceLongDpcDetectionEvent](../42/EtwTraceLongDpcDetectionEvent_function_0042A940.md) (function, `0x0042A940`)
- `0x0025C7F2` → [EtwpGetHostPerfCounter](../3A/EtwpGetHostPerfCounter_function_003A4134.md) (function, `0x003A4134`)
- `0x0025C80C` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x0025C865` → [KiSearchForNewThreadsForRescheduleContext](KiSearchForNewThreadsForRescheduleContext_function_00258620.md) (function, `0x00258620`)
- `0x0025C8AD` → [KiCommitRescheduleContextEntry](../30/KiCommitRescheduleContextEntry_function_0030CFD0.md) (function, `0x0030CFD0`)
- `0x0025C97F` → [KiFindRescheduleContextEntryForPrcb](../35/KiFindRescheduleContextEntryForPrcb_function_00353060.md) (function, `0x00353060`)
- `0x0025C9F3` → [KiAdjustRescheduleContextEntryForThreadRemoval](../35/KiAdjustRescheduleContextEntryForThreadRemoval_function_00352340.md) (function, `0x00352340`)
- `0x0025CA66` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025CAC7` → [KiDoesThreadDominateRescheduleContextEntry](KiDoesThreadDominateRescheduleContextEntry_function_002581D0.md) (function, `0x002581D0`)
- `0x0025CB17` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025CB41` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)
- `0x0025CB50` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x0025CB7A` → [KiInsertDeferredReadyList](../20/KiInsertDeferredReadyList_function_00201310.md) (function, `0x00201310`)

### Direct callers
- [KiRetireDpcList](../21/KiRetireDpcList_function_0021A0B0.md) at `0x0021A505`
- [KiExecuteDpc](../5C/KiExecuteDpc_function_005C84F0.md) at `0x005C85AD`

### Static image references
- `0x0025B753` → RVA `0x00E0A740` (`.data`; read)
- `0x0025B813` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0025B884` → RVA `0x00FC51D0` (`ALMOSTRO`; read)
- `0x0025B8AE` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0025B8BB` → RVA `0x00F0DE58` (`.data`; read)
- `0x0025B991` → RVA `0x00FC7250` (`ALMOSTRO`; read)
- `0x0025B99E` → RVA `0x00FC6F78` (`ALMOSTRO`; read)
- `0x0025BA1A` → RVA `0x00FCFC80` (`CACHEALI`; read)
- `0x0025BB99` → RVA `0x0030DEB0` (`KiAbDeferredProcessingWorker`; read)
- `0x0025BD8E` → RVA `0x00227FF0` (`KiSwapDirectoryTableBaseTarget`; read)
- `0x0025BDB7` → RVA `0x002D7E70` (`PpmPerfAction`; read)
- `0x0025C33F` → RVA `0x00FC5007` (`ALMOSTRO`; read)
- `0x0025C34B` → RVA `0x00FCD260` (`ALMOSTRO`; read)
- `0x0025C367` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x0025C466` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0025B740  40 53                           push rbx
0025B742  56                              push rsi
0025B743  57                              push rdi
0025B744  41 54                           push r12
0025B746  41 55                           push r13
0025B748  41 56                           push r14
0025B74A  41 57                           push r15
0025B74C  48 81 EC 00 02 00 00            sub rsp, 0x200
0025B753  48 8B 05 E6 EF BA 00            mov rax, qword ptr [rip + 0xbaefe6]
0025B75A  48 33 C4                        xor rax, rsp
0025B75D  48 89 84 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rax
0025B765  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
0025B76A  49 8B C0                        mov rax, r8
0025B76D  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
0025B775  4C 8B FA                        mov r15, rdx
0025B778  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
0025B780  48 89 8C 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rcx
0025B788  4C 8B D9                        mov r11, rcx
0025B78B  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0025B790  4C 8B E9                        mov r13, rcx
0025B793  48 89 8C 24 30 01 00 00         mov qword ptr [rsp + 0x130], rcx
0025B79B  48 89 94 24 18 01 00 00         mov qword ptr [rsp + 0x118], rdx
0025B7A3  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
0025B7AB  44 89 8C 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r9d
0025B7B3  33 F6                           xor esi, esi
0025B7B5  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0025B7BA  0F 57 C0                        xorps xmm0, xmm0
0025B7BD  0F 11 84 24 60 01 00 00         movups xmmword ptr [rsp + 0x160], xmm0
0025B7C5  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
0025B7CA  0F 57 C9                        xorps xmm1, xmm1
0025B7CD  0F 11 8C 24 A8 01 00 00         movups xmmword ptr [rsp + 0x1a8], xmm1
0025B7D5  0F 11 8C 24 B8 01 00 00         movups xmmword ptr [rsp + 0x1b8], xmm1
0025B7DD  41 8B C1                        mov eax, r9d
0025B7E0  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
0025B7E8  4C 8D 80 2C 01 00 00            lea r8, [rax + 0x12c]
0025B7EF  4F 8D 04 40                     lea r8, [r8 + r8*2]
0025B7F3  49 C1 E0 04                     shl r8, 4
0025B7F7  4C 03 C1                        add r8, rcx
0025B7FA  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
0025B7FF  4D 8D 70 18                     lea r14, [r8 + 0x18]
0025B803  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
0025B808  41 8B 06                        mov eax, dword ptr [r14]
0025B80B  85 C0                           test eax, eax
0025B80D  0F 84 11 0A 00 00               je 0x14025c224
0025B813  8B 05 EB B2 D6 00               mov eax, dword ptr [rip + 0xd6b2eb]
0025B819  84 C0                           test al, al
0025B81B  0F 89 A2 0B 00 00               jns 0x14025c3c3
0025B821  45 85 C9                        test r9d, r9d
0025B824  0F 85 DB 12 00 00               jne 0x14025cb05
0025B82A  B8 44 0F 00 00                  mov eax, 0xf44
0025B82F  C7 44 24 7C 02 0A 50 00         mov dword ptr [rsp + 0x7c], 0x500a02
0025B837  66 89 44 24 78                  mov word ptr [rsp + 0x78], ax
0025B83C  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0025B841  48 89 8C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rcx
0025B849  49 8D 83 90 2D 00 00            lea rax, [r11 + 0x2d90]
0025B850  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
0025B858  48 8B 00                        mov rax, qword ptr [rax]
0025B85B  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
0025B863  4D 8B E0                        mov r12, r8
0025B866  BF 02 00 00 00                  mov edi, 2
0025B86B  41 8B 0E                        mov ecx, dword ptr [r14]
0025B86E  41 8B 40 28                     mov eax, dword ptr [r8 + 0x28]
0025B872  85 C0                           test eax, eax
0025B874  0F 95 C2                        setne dl
0025B877  45 85 C9                        test r9d, r9d
0025B87A  75 14                           jne 0x14025b890
0025B87C  85 C0                           test eax, eax
0025B87E  0F 85 EC 0E 00 00               jne 0x14025c770
0025B884  3B 0D 46 99 D6 00               cmp ecx, dword ptr [rip + 0xd69946]
0025B88A  0F 83 E0 0E 00 00               jae 0x14025c770
0025B890  32 DB                           xor bl, bl
0025B892  F7 05 68 B2 D6 00 00 00 04 00   test dword ptr [rip + 0xd6b268], 0x40000
0025B89C  0F 85 34 0F 00 00               jne 0x14025c7d6
0025B8A2  84 DB                           test bl, bl
0025B8A4  0F 85 CD 0E 00 00               jne 0x14025c777
0025B8AA  49 8D 58 10                     lea rbx, [r8 + 0x10]
0025B8AE  F6 05 51 B2 D6 00 21            test byte ptr [rip + 0xd6b251], 0x21
0025B8B5  0F 84 DF 07 00 00               je 0x14025c09a
0025B8BB  8B 05 97 25 CB 00               mov eax, dword ptr [rip + 0xcb2597]
0025B8C1  85 C0                           test eax, eax
0025B8C3  0F 85 D1 07 00 00               jne 0x14025c09a
0025B8C9  48 8B CB                        mov rcx, rbx
0025B8CC  E8 1F CC FA FF                  call 0x1402084f0
0025B8D1  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
0025B8D6  41 83 3E 01                     cmp dword ptr [r14], 1
0025B8DA  0F 8E D3 07 00 00               jle 0x14025c0b3
0025B8E0  49 8B 0C 24                     mov rcx, qword ptr [r12]
0025B8E4  48 8B 01                        mov rax, qword ptr [rcx]
0025B8E7  49 89 04 24                     mov qword ptr [r12], rax
0025B8EB  48 85 C0                        test rax, rax
0025B8EE  75 05                           jne 0x14025b8f5
0025B8F0  4D 89 64 24 08                  mov qword ptr [r12 + 8], r12
0025B8F5  4C 8D 79 F8                     lea r15, [rcx - 8]
0025B8F9  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
0025B8FD  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0025B902  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
0025B906  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0025B90E  4D 8B 77 28                     mov r14, qword ptr [r15 + 0x28]
0025B912  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
0025B916  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
0025B91E  4D 8B 67 38                     mov r12, qword ptr [r15 + 0x38]
0025B922  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
0025B92A  4C 89 A4 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r12
0025B932  49 89 77 38                     mov qword ptr [r15 + 0x38], rsi
0025B936  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0025B93B  8B 01                           mov eax, dword ptr [rcx]
0025B93D  FF C8                           dec eax
0025B93F  89 01                           mov dword ptr [rcx], eax
0025B941  4D 89 78 20                     mov qword ptr [r8 + 0x20], r15
0025B945  F6 05 BA B1 D6 00 01            test byte ptr [rip + 0xd6b1ba], 1
0025B94C  0F 85 4D 0E 00 00               jne 0x14025c79f
0025B952  F0 48 83 23 00                  lock and qword ptr [rbx], 0
0025B957  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0025B960  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0025B967  4D 85 C0                        test r8, r8
0025B96A  0F 85 60 0A 00 00               jne 0x14025c3d0
0025B970  FB                              sti
0025B971  F7 05 89 B1 D6 00 00 00 04 00   test dword ptr [rip + 0xd6b189], 0x40000
0025B97B  0F 84 84 00 00 00               je 0x14025ba05
0025B981  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0025B986  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
0025B98E  49 8B D7                        mov rdx, r15
0025B991  48 33 15 B8 B8 D6 00            xor rdx, qword ptr [rip + 0xd6b8b8]
0025B998  48 0F CA                        bswap rdx
0025B99B  48 33 D0                        xor rdx, rax
0025B99E  48 8B 05 D3 B5 D6 00            mov rax, qword ptr [rip + 0xd6b5d3]
0025B9A5  8B C8                           mov ecx, eax
0025B9A7  48 D3 CA                        ror rdx, cl
0025B9AA  48 33 D0                        xor rdx, rax
0025B9AD  48 B8 77 72 DD F3 C7 C6 35 7E   movabs rax, 0x7e35c6c7f3dd7277
0025B9B7  48 0F AF D0                     imul rdx, rax
0025B9BB  48 89 94 24 68 01 00 00         mov qword ptr [rsp + 0x168], rdx
0025B9C3  48 8D 84 24 60 01 00 00         lea rax, [rsp + 0x160]
0025B9CB  48 89 84 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], rax
0025B9D3  48 C7 84 24 D0 01 00 00 10 00 00 00  mov qword ptr [rsp + 0x1d0], 0x10
0025B9DF  41 B9 65 0F 00 00               mov r9d, 0xf65
0025B9E5  C7 44 24 20 02 0A 50 00         mov dword ptr [rsp + 0x20], 0x500a02
0025B9ED  BA 01 00 00 00                  mov edx, 1
0025B9F2  41 B8 00 00 04 20               mov r8d, 0x20040000
0025B9F8  48 8D 8C 24 C8 01 00 00         lea rcx, [rsp + 0x1c8]
0025BA00  E8 4B 99 FD FF                  call 0x140235350
0025BA05  48 83 BC 24 C0 00 00 00 00      cmp qword ptr [rsp + 0xc0], 0
0025BA0E  0F 84 B8 00 00 00               je 0x14025bacc
0025BA14  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
0025BA18  8B DE                           mov ebx, esi
0025BA1A  4C 8B 05 5F 42 D7 00            mov r8, qword ptr [rip + 0xd7425f]
0025BA21  4D 85 C0                        test r8, r8
0025BA24  0F 84 7A 09 00 00               je 0x14025c3a4
0025BA2A  41 8B 90 A8 11 00 00            mov edx, dword ptr [r8 + 0x11a8]
0025BA31  0F BC CA                        bsf ecx, edx
0025BA34  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
0025BA38  74 45                           je 0x14025ba7f
0025BA3A  41 BC 01 00 00 00               mov r12d, 1
0025BA40  8D 42 FF                        lea eax, [rdx - 1]
0025BA43  23 D0                           and edx, eax
0025BA45  48 8B C1                        mov rax, rcx
0025BA48  48 C1 E0 05                     shl rax, 5
0025BA4C  48 05 CC 11 00 00               add rax, 0x11cc
0025BA52  49 03 C0                        add rax, r8
0025BA55  74 17                           je 0x14025ba6e
0025BA57  8B 40 04                        mov eax, dword ptr [rax + 4]
0025BA5A  84 C0                           test al, al
0025BA5C  79 10                           jns 0x14025ba6e
0025BA5E  41 0F B6 8C 48 99 11 00 00      movzx ecx, byte ptr [r8 + rcx*2 + 0x1199]
0025BA67  41 8B C4                        mov eax, r12d
0025BA6A  D3 E0                           shl eax, cl
0025BA6C  0B D8                           or ebx, eax
0025BA6E  0F BC CA                        bsf ecx, edx
0025BA71  75 CD                           jne 0x14025ba40
0025BA73  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
0025BA77  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
0025BA7F  F6 C3 02                        test bl, 2
0025BA82  0F 85 72 06 00 00               jne 0x14025c0fa
0025BA88  48 89 B4 24 A8 01 00 00         mov qword ptr [rsp + 0x1a8], rsi
0025BA90  F6 C3 04                        test bl, 4
0025BA93  0F 85 F4 0C 00 00               jne 0x14025c78d
0025BA99  48 89 B4 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rsi
0025BAA1  F6 C3 08                        test bl, 8
0025BAA4  0F 84 43 06 00 00               je 0x14025c0ed
0025BAAA  0F 31                           rdtsc
0025BAAC  48 C1 E2 20                     shl rdx, 0x20
0025BAB0  48 0B C2                        or rax, rdx
0025BAB3  48 89 84 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], rax
0025BABB  F6 C3 10                        test bl, 0x10
0025BABE  0F 85 2E 0D 00 00               jne 0x14025c7f2
0025BAC4  48 89 B4 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rsi
0025BACC  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0025BAD4  8B 81 E4 01 00 00               mov eax, dword ptr [rcx + 0x1e4]
0025BADA  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0025BADE  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
0025BAE5  0F B6 81 32 02 00 00            movzx eax, byte ptr [rcx + 0x232]
0025BAEC  88 44 24 31                     mov byte ptr [rsp + 0x31], al
0025BAF0  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0025BAF4  48 8B 94 24 00 01 00 00         mov rdx, qword ptr [rsp + 0x100]
0025BAFC  8B 02                           mov eax, dword ptr [rdx]
0025BAFE  8B C8                           mov ecx, eax
0025BB00  83 E1 0F                        and ecx, 0xf
0025BB03  FF C0                           inc eax
0025BB05  89 02                           mov dword ptr [rdx], eax
0025BB07  8B C1                           mov eax, ecx
0025BB09  48 FF C1                        inc rcx
0025BB0C  48 8D 0C 48                     lea rcx, [rax + rcx*2]
0025BB10  48 8D 0C CA                     lea rcx, [rdx + rcx*8]
0025BB14  48 89 8C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rcx
0025BB1C  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0025BB21  48 89 01                        mov qword ptr [rcx], rax
0025BB24  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0025BB2E  48 8B 00                        mov rax, qword ptr [rax]
0025BB31  48 89 41 08                     mov qword ptr [rcx + 8], rax
0025BB35  48 89 71 10                     mov qword ptr [rcx + 0x10], rsi
0025BB39  48 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rcx
0025BB41  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0025BB46  41 89 B0 5C 86 00 00            mov dword ptr [r8 + 0x865c], esi
0025BB4D  0F 31                           rdtsc
0025BB4F  48 C1 E2 20                     shl rdx, 0x20
0025BB53  48 0B C2                        or rax, rdx
0025BB56  48 8B C8                        mov rcx, rax
0025BB59  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0025BB61  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
0025BB69  4C 89 20                        mov qword ptr [rax], r12
0025BB6C  49 83 FC 01                     cmp r12, 1
0025BB70  74 05                           je 0x14025bb77
0025BB72  49 89 4C 24 20                  mov qword ptr [r12 + 0x20], rcx
0025BB77  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0025BB7C  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
0025BB81  75 16                           jne 0x14025bb99
0025BB83  49 89 80 20 38 00 00            mov qword ptr [r8 + 0x3820], rax
0025BB8A  49 89 88 30 38 00 00            mov qword ptr [r8 + 0x3830], rcx
0025BB91  41 C6 80 BA 38 00 00 01         mov byte ptr [r8 + 0x38ba], 1
0025BB99  48 8D 0D 10 23 0B 00            lea rcx, [rip + 0xb2310]
0025BBA0  48 3B C1                        cmp rax, rcx
0025BBA3  0F 85 E5 01 00 00               jne 0x14025bd8e
0025BBA9  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
0025BBAE  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
0025BBB3  4D 8D BE 78 91 00 00            lea r15, [r14 + 0x9178]
0025BBBA  49 8B 8E 70 91 00 00            mov rcx, qword ptr [r14 + 0x9170]
0025BBC1  48 85 C9                        test rcx, rcx
0025BBC4  74 50                           je 0x14025bc16
0025BBC6  48 8B 01                        mov rax, qword ptr [rcx]
0025BBC9  49 89 86 70 91 00 00            mov qword ptr [r14 + 0x9170], rax
0025BBD0  48 8D 99 D0 FC FF FF            lea rbx, [rcx - 0x330]
0025BBD7  48 C7 01 01 00 00 00            mov qword ptr [rcx], 1
0025BBDE  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0025BBE3  0F B6 83 19 03 00 00            movzx eax, byte ptr [rbx + 0x319]
0025BBEA  4D 8D BE 78 91 00 00            lea r15, [r14 + 0x9178]
0025BBF1  84 C0                           test al, al
0025BBF3  74 17                           je 0x14025bc0c
0025BBF5  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0025BBFA  4D 8B CF                        mov r9, r15
0025BBFD  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0025BC02  8B D7                           mov edx, edi
0025BC04  48 8B CB                        mov rcx, rbx
0025BC07  E8 24 61 FC FF                  call 0x140221d30
0025BC0C  66 F0 FF 8B 64 03 00 00         lock dec word ptr [rbx + 0x364]
0025BC14  EB A4                           jmp 0x14025bbba
0025BC16  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0025BC1B  49 8D 96 70 91 00 00            lea rdx, [r14 + 0x9170]
0025BC22  49 8B CF                        mov rcx, r15
0025BC25  E8 36 72 FC FF                  call 0x140222e60
0025BC2A  49 83 BE 70 91 00 00 00         cmp qword ptr [r14 + 0x9170], 0
0025BC32  0F 85 7B FF FF FF               jne 0x14025bbb3
0025BC38  49 89 B6 A0 91 00 00            mov qword ptr [r14 + 0x91a0], rsi
0025BC3F  89 74 24 6C                     mov dword ptr [rsp + 0x6c], esi
0025BC43  44 8B FE                        mov r15d, esi
0025BC46  89 74 24 6C                     mov dword ptr [rsp + 0x6c], esi
0025BC4A  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0025BC4F  48 85 DB                        test rbx, rbx
0025BC52  74 52                           je 0x14025bca6
0025BC54  48 8B 03                        mov rax, qword ptr [rbx]
0025BC57  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0025BC5C  48 85 DB                        test rbx, rbx
0025BC5F  74 45                           je 0x14025bca6
0025BC61  48 8D 93 28 FF FF FF            lea rdx, [rbx - 0xd8]
0025BC68  45 33 C9                        xor r9d, r9d
0025BC6B  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0025BC70  49 8B CE                        mov rcx, r14
0025BC73  E8 68 73 FF FF                  call 0x140252fe0
0025BC78  41 FF C7                        inc r15d
0025BC7B  44 89 7C 24 6C                  mov dword ptr [rsp + 0x6c], r15d
0025BC80  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0025BC85  48 85 DB                        test rbx, rbx
0025BC88  74 08                           je 0x14025bc92
0025BC8A  48 8B 03                        mov rax, qword ptr [rbx]
0025BC8D  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0025BC92  41 F6 C7 0F                     test r15b, 0xf
0025BC96  75 0C                           jne 0x14025bca4
0025BC98  49 8D 8E D8 35 00 00            lea rcx, [r14 + 0x35d8]
0025BC9F  E8 5C 65 FF FF                  call 0x140252200
0025BCA4  EB B6                           jmp 0x14025bc5c
0025BCA6  41 0F B6 86 D9 35 00 00         movzx eax, byte ptr [r14 + 0x35d9]
0025BCAE  84 C0                           test al, al
0025BCB0  0F 84 1C 01 00 00               je 0x14025bdd2
0025BCB6  3C 01                           cmp al, 1
0025BCB8  74 3A                           je 0x14025bcf4
0025BCBA  49 8D 8E E0 35 00 00            lea rcx, [r14 + 0x35e0]
0025BCC1  41 0F B6 96 D8 35 00 00         movzx edx, byte ptr [r14 + 0x35d8]
0025BCC9  E8 66 2B 0B 00                  call 0x14030e834
0025BCCE  41 80 BE D9 35 00 00 02         cmp byte ptr [r14 + 0x35d9], 2
0025BCD6  0F 84 8E 00 00 00               je 0x14025bd6a
0025BCDC  41 C6 86 D9 35 00 00 00         mov byte ptr [r14 + 0x35d9], 0
0025BCE4  41 C7 86 DC 35 00 00 FF FF 00 00  mov dword ptr [r14 + 0x35dc], 0xffff
0025BCEF  E9 DE 00 00 00                  jmp 0x14025bdd2
0025BCF4  45 0F B6 86 D8 35 00 00         movzx r8d, byte ptr [r14 + 0x35d8]
0025BCFC  41 8B 96 DC 35 00 00            mov edx, dword ptr [r14 + 0x35dc]
0025BD03  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0025BD0C  8B 81 D4 8E 00 00               mov eax, dword ptr [rcx + 0x8ed4]
0025BD12  FF C0                           inc eax
0025BD14  89 81 D4 8E 00 00               mov dword ptr [rcx + 0x8ed4], eax
0025BD1A  33 C0                           xor eax, eax
0025BD1C  89 84 24 74 01 00 00            mov dword ptr [rsp + 0x174], eax
0025BD23  0F 57 C0                        xorps xmm0, xmm0
0025BD26  0F 11 84 24 70 01 00 00         movups xmmword ptr [rsp + 0x170], xmm0
0025BD2E  89 84 24 80 01 00 00            mov dword ptr [rsp + 0x180], eax
0025BD35  C7 84 24 70 01 00 00 06 00 00 00  mov dword ptr [rsp + 0x170], 6
0025BD40  89 94 24 78 01 00 00            mov dword ptr [rsp + 0x178], edx
0025BD47  BA 1F 00 00 00                  mov edx, 0x1f
0025BD4C  41 80 F8 01                     cmp r8b, 1
0025BD50  B8 2F 00 00 00                  mov eax, 0x2f
0025BD55  0F 45 D0                        cmovne edx, eax
0025BD58  48 8D 8C 24 70 01 00 00         lea rcx, [rsp + 0x170]
0025BD60  E8 AB 65 FF FF                  call 0x140252310
0025BD65  E9 64 FF FF FF                  jmp 0x14025bcce
0025BD6A  49 C7 86 E0 35 00 00 01 00 20 00  mov qword ptr [r14 + 0x35e0], 0x200001
0025BD75  49 8D 8E E8 35 00 00            lea rcx, [r14 + 0x35e8]
0025BD7C  33 D2                           xor edx, edx
0025BD7E  41 B8 00 01 00 00               mov r8d, 0x100
0025BD84  E8 B7 AE 46 00                  call 0x1406c6c40
0025BD89  E9 4E FF FF FF                  jmp 0x14025bcdc
0025BD8E  48 8D 0D 5B C2 FC FF            lea rcx, [rip - 0x33da5]
0025BD95  4C 8B 8C 24 B8 00 00 00         mov r9, qword ptr [rsp + 0xb8]
0025BD9D  4D 8B C6                        mov r8, r14
0025BDA0  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0025BDA8  48 3B C1                        cmp rax, rcx
0025BDAB  75 0A                           jne 0x14025bdb7
0025BDAD  49 8B CF                        mov rcx, r15
0025BDB0  E8 3B C2 FC FF                  call 0x140227ff0
0025BDB5  EB 1B                           jmp 0x14025bdd2
0025BDB7  48 8D 0D B2 C0 07 00            lea rcx, [rip + 0x7c0b2]
0025BDBE  48 3B C1                        cmp rax, rcx
0025BDC1  49 8B CF                        mov rcx, r15
0025BDC4  75 07                           jne 0x14025bdcd
0025BDC6  E8 A5 C0 07 00                  call 0x1402d7e70
0025BDCB  EB 05                           jmp 0x14025bdd2
0025BDCD  E8 FE EC 45 00                  call 0x1406baad0
0025BDD2  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
0025BDD7  EB 76                           jmp 0x14025be4f
0025BDD9  33 F6                           xor esi, esi
0025BDDB  8D 7E 02                        lea edi, [rsi + 2]
0025BDDE  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
0025BDE6  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
0025BDEE  4C 8B A4 24 E0 00 00 00         mov r12, qword ptr [rsp + 0xe0]
0025BDF6  4C 89 A4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r12
0025BDFE  8B 84 24 A8 00 00 00            mov eax, dword ptr [rsp + 0xa8]
0025BE05  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0025BE09  0F B6 44 24 30                  movzx eax, byte ptr [rsp + 0x30]
0025BE0E  88 44 24 31                     mov byte ptr [rsp + 0x31], al
0025BE12  48 8B 8C 24 18 01 00 00         mov rcx, qword ptr [rsp + 0x118]
0025BE1A  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
0025BE22  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
0025BE2A  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
0025BE32  4C 8B AC 24 30 01 00 00         mov r13, qword ptr [rsp + 0x130]
0025BE3A  4C 89 AC 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r13
0025BE42  44 8B 84 24 B0 00 00 00         mov r8d, dword ptr [rsp + 0xb0]
0025BE4A  44 89 44 24 40                  mov dword ptr [rsp + 0x40], r8d
0025BE4F  0F 31                           rdtsc
0025BE51  48 C1 E2 20                     shl rdx, 0x20
0025BE55  48 0B C2                        or rax, rdx
0025BE58  48 8B D8                        mov rbx, rax
0025BE5B  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
0025BE60  45 85 C0                        test r8d, r8d
0025BE63  0F 85 C1 01 00 00               jne 0x14025c02a
0025BE69  45 88 83 BA 38 00 00            mov byte ptr [r11 + 0x38ba], r8b
0025BE70  4D 8B 83 18 83 00 00            mov r8, qword ptr [r11 + 0x8318]
0025BE77  4D 85 C0                        test r8, r8
0025BE7A  0F 84 8E 02 00 00               je 0x14025c10e
0025BE80  41 8B 8B 20 83 00 00            mov ecx, dword ptr [r11 + 0x8320]
0025BE87  48 8D 14 49                     lea rdx, [rcx + rcx*2]
0025BE8B  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0025BE90  49 89 04 D0                     mov qword ptr [r8 + rdx*8], rax
0025BE94  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0025BE9C  49 89 4C D0 08                  mov qword ptr [r8 + rdx*8 + 8], rcx
0025BEA1  49 89 5C D0 10                  mov qword ptr [r8 + rdx*8 + 0x10], rbx
0025BEA6  41 FF 83 20 83 00 00            inc dword ptr [r11 + 0x8320]
0025BEAD  41 83 BB 20 83 00 00 20         cmp dword ptr [r11 + 0x8320], 0x20
0025BEB5  72 07                           jb 0x14025bebe
0025BEB7  41 89 B3 20 83 00 00            mov dword ptr [r11 + 0x8320], esi
0025BEBE  4C 8B C3                        mov r8, rbx
0025BEC1  4C 2B C1                        sub r8, rcx
0025BEC4  4D 8B 93 10 38 00 00            mov r10, qword ptr [r11 + 0x3810]
0025BECB  4D 85 D2                        test r10, r10
0025BECE  0F 84 38 01 00 00               je 0x14025c00c
0025BED4  45 8B 5A 04                     mov r11d, dword ptr [r10 + 4]
0025BED8  41 8B CB                        mov ecx, r11d
0025BEDB  83 E1 1F                        and ecx, 0x1f
0025BEDE  49 C7 C6 FF FF FF FF            mov r14, 0xffffffffffffffff
0025BEE5  49 D3 E6                        shl r14, cl
0025BEE8  4D 8B CE                        mov r9, r14
0025BEEB  4C 23 4C 24 48                  and r9, qword ptr [rsp + 0x48]
0025BEF0  4D 8B F9                        mov r15, r9
0025BEF3  49 C1 EF 38                     shr r15, 0x38
0025BEF7  4D 8B E1                        mov r12, r9
0025BEFA  49 C1 EC 30                     shr r12, 0x30
0025BEFE  49 8B C1                        mov rax, r9
0025BF01  48 C1 E8 28                     shr rax, 0x28
0025BF05  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0025BF0D  49 8B C1                        mov rax, r9
0025BF10  48 C1 E8 20                     shr rax, 0x20
0025BF14  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0025BF1C  49 8B C1                        mov rax, r9
0025BF1F  48 C1 E8 18                     shr rax, 0x18
0025BF23  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
0025BF2B  49 8B C1                        mov rax, r9
0025BF2E  48 C1 E8 10                     shr rax, 0x10
0025BF32  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
0025BF3A  49 8B D1                        mov rdx, r9
0025BF3D  48 C1 EA 08                     shr rdx, 8
0025BF41  41 C1 EB 05                     shr r11d, 5
0025BF45  45 85 DB                        test r11d, r11d
0025BF48  0F 84 E3 07 00 00               je 0x14025c731
0025BF4E  4C 89 8C 24 98 01 00 00         mov qword ptr [rsp + 0x198], r9
0025BF56  41 0F B6 C1                     movzx eax, r9b
0025BF5A  48 05 CB 5D B1 00               add rax, 0xb15dcb
0025BF60  48 6B C8 25                     imul rcx, rax, 0x25
0025BF64  0F B6 C2                        movzx eax, dl
0025BF67  48 03 C8                        add rcx, rax
0025BF6A  48 6B D1 25                     imul rdx, rcx, 0x25
0025BF6E  0F B6 84 24 E0 00 00 00         movzx eax, byte ptr [rsp + 0xe0]
0025BF76  48 03 D0                        add rdx, rax
0025BF79  48 6B CA 25                     imul rcx, rdx, 0x25
0025BF7D  0F B6 84 24 D8 00 00 00         movzx eax, byte ptr [rsp + 0xd8]
0025BF85  48 03 C8                        add rcx, rax
0025BF88  48 6B D1 25                     imul rdx, rcx, 0x25
0025BF8C  0F B6 84 24 90 00 00 00         movzx eax, byte ptr [rsp + 0x90]
0025BF94  48 03 D0                        add rdx, rax
0025BF97  48 6B CA 25                     imul rcx, rdx, 0x25
0025BF9B  0F B6 84 24 88 00 00 00         movzx eax, byte ptr [rsp + 0x88]
0025BFA3  48 03 C8                        add rcx, rax
0025BFA6  48 6B D1 25                     imul rdx, rcx, 0x25
0025BFAA  41 0F B6 C4                     movzx eax, r12b
0025BFAE  48 03 D0                        add rdx, rax
0025BFB1  48 6B C2 25                     imul rax, rdx, 0x25
0025BFB5  49 03 C7                        add rax, r15
0025BFB8  41 8D 53 FF                     lea edx, [r11 - 1]
0025BFBC  8B C0                           mov eax, eax
0025BFBE  48 23 D0                        and rdx, rax
0025BFC1  49 8B 42 08                     mov rax, qword ptr [r10 + 8]
0025BFC5  48 8D 0C D0                     lea rcx, [rax + rdx*8]
0025BFC9  48 8B 11                        mov rdx, qword ptr [rcx]
0025BFCC  48 8B CA                        mov rcx, rdx
0025BFCF  F6 C2 01                        test dl, 1
0025BFD2  0F 85 59 07 00 00               jne 0x14025c731
0025BFD8  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0025BFDC  49 23 C6                        and rax, r14
0025BFDF  4C 3B C8                        cmp r9, rax
0025BFE2  75 E5                           jne 0x14025bfc9
0025BFE4  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
0025BFE8  4B 8D 0C 40                     lea rcx, [r8 + r8*2]
0025BFEC  48 C1 E9 02                     shr rcx, 2
0025BFF0  48 C1 E8 02                     shr rax, 2
0025BFF4  48 03 C8                        add rcx, rax
0025BFF7  48 89 4A 10                     mov qword ptr [rdx + 0x10], rcx
0025BFFB  C6 42 18 01                     mov byte ptr [rdx + 0x18], 1
0025BFFF  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
0025C004  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
0025C00C  49 89 B3 20 38 00 00            mov qword ptr [r11 + 0x3820], rsi
0025C013  49 C7 83 28 38 00 00 FF FF FF FF  mov qword ptr [r11 + 0x3828], 0xffffffffffffffff
0025C01E  49 89 B3 30 38 00 00            mov qword ptr [r11 + 0x3830], rsi
0025C025  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
0025C02A  49 83 FC 01                     cmp r12, 1
0025C02E  74 19                           je 0x14025c049
0025C030  49 2B 5C 24 20                  sub rbx, qword ptr [r12 + 0x20]
0025C035  49 01 5C 24 18                  add qword ptr [r12 + 0x18], rbx
0025C03A  49 FF 44 24 28                  inc qword ptr [r12 + 0x28]
0025C03F  49 01 5C 24 50                  add qword ptr [r12 + 0x50], rbx
0025C044  49 FF 44 24 58                  inc qword ptr [r12 + 0x58]
0025C049  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0025C053  48 8B 00                        mov rax, qword ptr [rax]
0025C056  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
0025C05E  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
0025C062  4C 8B BC 24 80 00 00 00         mov r15, qword ptr [rsp + 0x80]
0025C06A  41 8B 87 E4 01 00 00            mov eax, dword ptr [r15 + 0x1e4]
0025C071  8B 4C 24 44                     mov ecx, dword ptr [rsp + 0x44]
0025C075  3B C8                           cmp ecx, eax
0025C077  0F 84 7B 03 00 00               je 0x14025c3f8
0025C07D  44 8B C9                        mov r9d, ecx
0025C080  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0025C085  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
0025C08A  BA 04 00 00 00                  mov edx, 4
0025C08F  B9 C7 00 00 00                  mov ecx, 0xc7
0025C094  E8 C7 15 2A 00                  call 0x1404fd660
0025C099  CC                              int3
0025C09A  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0025C0A0  0F 83 30 F8 FF FF               jae 0x14025b8d6
0025C0A6  48 8B CB                        mov rcx, rbx
0025C0A9  E8 12 C5 FA FF                  call 0x1402085c0
0025C0AE  E9 1E F8 FF FF                  jmp 0x14025b8d1
0025C0B3  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0025C0BB  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
0025C0C3  66 F0 83 A4 48 BC 38 00 00 ED   lock and word ptr [rax + rcx*2 + 0x38bc], 0xffed
0025C0CD  41 89 70 28                     mov dword ptr [r8 + 0x28], esi
0025C0D1  41 83 3E 00                     cmp dword ptr [r14], 0
0025C0D5  0F 85 05 F8 FF FF               jne 0x14025b8e0
0025C0DB  48 8B CB                        mov rcx, rbx
0025C0DE  E8 8D A5 FA FF                  call 0x140206670
0025C0E3  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
0025C0E8  E9 37 04 00 00                  jmp 0x14025c524
0025C0ED  48 89 B4 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], rsi
0025C0F5  E9 C1 F9 FF FF                  jmp 0x14025babb
0025C0FA  33 C9                           xor ecx, ecx
0025C0FC  E8 DF 26 12 00                  call 0x14037e7e0
0025C101  48 89 84 24 A8 01 00 00         mov qword ptr [rsp + 0x1a8], rax
0025C109  E9 82 F9 FF FF                  jmp 0x14025ba90
0025C10E  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0025C116  E9 A3 FD FF FF                  jmp 0x14025bebe
0025C11B  41 0F B6 85 D9 35 00 00         movzx eax, byte ptr [r13 + 0x35d9]
0025C123  84 C0                           test al, al
0025C125  0F 85 77 01 00 00               jne 0x14025c2a2
0025C12B  41 C6 85 D9 35 00 00 01         mov byte ptr [r13 + 0x35d9], 1
0025C133  41 8B 46 24                     mov eax, dword ptr [r14 + 0x24]
0025C137  41 89 85 DC 35 00 00            mov dword ptr [r13 + 0x35dc], eax
0025C13E  41 F6 44 DF 33 02               test byte ptr [r15 + rbx*8 + 0x33], 2
0025C144  0F 85 64 02 00 00               jne 0x14025c3ae
0025C14A  41 F6 44 DF 33 04               test byte ptr [r15 + rbx*8 + 0x33], 4
0025C150  74 16                           je 0x14025c168
0025C152  41 0F BE 4C DF 34               movsx ecx, byte ptr [r15 + rbx*8 + 0x34]
0025C158  49 8B 86 B8 8E 00 00            mov rax, qword ptr [r14 + 0x8eb8]
0025C15F  48 85 C0                        test rax, rax
0025C162  0F 85 8B 01 00 00               jne 0x14025c2f3
0025C168  41 F6 44 DF 33 01               test byte ptr [r15 + rbx*8 + 0x33], 1
0025C16E  74 0D                           je 0x14025c17d
0025C170  49 8B 44 DF 28                  mov rax, qword ptr [r15 + rbx*8 + 0x28]
0025C175  66 F0 FF 88 64 03 00 00         lock dec word ptr [rax + 0x364]
0025C17D  FF C6                           inc esi
0025C17F  41 0F B6 07                     movzx eax, byte ptr [r15]
0025C183  3B F0                           cmp esi, eax
0025C185  0F 82 E5 00 00 00               jb 0x14025c270
0025C18B  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
0025C193  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0025C198  48 8D 8F D8 35 00 00            lea rcx, [rdi + 0x35d8]
0025C19F  E8 5C 60 FF FF                  call 0x140252200
0025C1A4  33 F6                           xor esi, esi
0025C1A6  48 83 BC 24 A0 00 00 00 00      cmp qword ptr [rsp + 0xa0], 0
0025C1AF  74 10                           je 0x14025c1c1
0025C1B1  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
0025C1B9  48 8B CF                        mov rcx, rdi
0025C1BC  E8 BF 1B 0B 00                  call 0x14030dd80
0025C1C1  48 85 DB                        test rbx, rbx
0025C1C4  0F 95 C0                        setne al
0025C1C7  84 C0                           test al, al
0025C1C9  74 58                           je 0x14025c223
0025C1CB  8B D6                           mov edx, esi
0025C1CD  48 8B CB                        mov rcx, rbx
0025C1D0  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0025C1D4  48 89 8C 24 58 01 00 00         mov qword ptr [rsp + 0x158], rcx
0025C1DC  83 E3 01                        and ebx, 1
0025C1DF  0F 84 AD 01 00 00               je 0x14025c392
0025C1E5  83 FB 01                        cmp ebx, 1
0025C1E8  75 15                           jne 0x14025c1ff
0025C1EA  48 8B B1 58 8E 00 00            mov rsi, qword ptr [rcx + 0x8e58]
0025C1F1  48 83 C6 08                     add rsi, 8
0025C1F5  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
0025C1FC  0F B6 10                        movzx edx, byte ptr [rax]
0025C1FF  85 D2                           test edx, edx
0025C201  74 20                           je 0x14025c223
0025C203  0F 1F 40 00                     nop dword ptr [rax]
0025C207  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0025C210  8D 42 FF                        lea eax, [rdx - 1]
0025C213  8B D0                           mov edx, eax
0025C215  48 8B 0C C6                     mov rcx, qword ptr [rsi + rax*8]
0025C219  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
0025C21F  85 C0                           test eax, eax
0025C221  75 ED                           jne 0x14025c210
0025C223  FA                              cli
0025C224  B0 01                           mov al, 1
0025C226  48 8B 8C 24 F8 01 00 00         mov rcx, qword ptr [rsp + 0x1f8]
0025C22E  48 33 CC                        xor rcx, rsp
0025C231  E8 0A 04 45 00                  call 0x1406ac640
0025C236  48 81 C4 00 02 00 00            add rsp, 0x200
0025C23D  41 5F                           pop r15
0025C23F  41 5E                           pop r14
0025C241  41 5D                           pop r13
0025C243  41 5C                           pop r12
0025C245  5F                              pop rdi
0025C246  5E                              pop rsi
0025C247  5B                              pop rbx
0025C248  C3                              ret
0025C249  CC                              int3
0025C24A  48 8B DE                        mov rbx, rsi
0025C24D  48 89 9C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rbx
0025C255  45 84 C9                        test r9b, r9b
0025C258  0F 84 64 05 00 00               je 0x14025c7c2
0025C25E  41 80 3F 00                     cmp byte ptr [r15], 0
0025C262  0F 86 2B FF FF FF               jbe 0x14025c193
0025C268  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0025C270  8B C6                           mov eax, esi
0025C272  48 8D 1C 80                     lea rbx, [rax + rax*4]
0025C276  4D 8B 74 DF 10                  mov r14, qword ptr [r15 + rbx*8 + 0x10]
0025C27B  41 0F B6 44 DF 33               movzx eax, byte ptr [r15 + rbx*8 + 0x33]
0025C281  A8 10                           test al, 0x10
0025C283  0F 85 92 FE FF FF               jne 0x14025c11b
0025C289  A8 08                           test al, 8
0025C28B  0F 84 AD FE FF FF               je 0x14025c13e
0025C291  90                              nop
0025C292  41 80 7E 07 00                  cmp byte ptr [r14 + 7], 0
0025C297  0F 85 7E FE FF FF               jne 0x14025c11b
0025C29D  E9 9C FE FF FF                  jmp 0x14025c13e
0025C2A2  3C 01                           cmp al, 1
0025C2A4  75 44                           jne 0x14025c2ea
0025C2A6  41 8B 95 DC 35 00 00            mov edx, dword ptr [r13 + 0x35dc]
0025C2AD  41 3B 56 24                     cmp edx, dword ptr [r14 + 0x24]
0025C2B1  0F 84 87 FE FF FF               je 0x14025c13e
0025C2B7  41 C6 85 D9 35 00 00 02         mov byte ptr [r13 + 0x35d9], 2
0025C2BF  4D 8D A5 E0 35 00 00            lea r12, [r13 + 0x35e0]
0025C2C6  49 8B CC                        mov rcx, r12
0025C2C9  E8 22 F4 FF FF                  call 0x14025b6f0
0025C2CE  4D 8B 86 C8 00 00 00            mov r8, qword ptr [r14 + 0xc8]
0025C2D5  41 0F B6 96 D0 00 00 00         movzx edx, byte ptr [r14 + 0xd0]
0025C2DD  49 8B CC                        mov rcx, r12
0025C2E0  E8 DB F3 FF FF                  call 0x14025b6c0
0025C2E5  E9 54 FE FF FF                  jmp 0x14025c13e
0025C2EA  4D 8D A5 E0 35 00 00            lea r12, [r13 + 0x35e0]
0025C2F1  EB DB                           jmp 0x14025c2ce
0025C2F3  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0025C2F8  49 83 B8 B8 8E 00 00 00         cmp qword ptr [r8 + 0x8eb8], 0
0025C300  0F 84 62 FE FF FF               je 0x14025c168
0025C306  4D 3B C6                        cmp r8, r14
0025C309  0F 84 59 FE FF FF               je 0x14025c168
0025C30F  8B 10                           mov edx, dword ptr [rax]
0025C311  8B C2                           mov eax, edx
0025C313  25 00 00 04 00                  and eax, 0x40000
0025C318  0F BA E2 14                     bt edx, 0x14
0025C31C  72 13                           jb 0x14025c331
0025C31E  85 C0                           test eax, eax
0025C320  0F 84 42 FE FF FF               je 0x14025c168
0025C326  0F B6 C2                        movzx eax, dl
0025C329  3B C1                           cmp eax, ecx
0025C32B  0F 8D 37 FE FF FF               jge 0x14025c168
0025C331  49 8B 88 B8 8E 00 00            mov rcx, qword ptr [r8 + 0x8eb8]
0025C338  89 79 0C                        mov dword ptr [rcx + 0xc], edi
0025C33B  45 8B 66 24                     mov r12d, dword ptr [r14 + 0x24]
0025C33F  80 3D C1 8C D6 00 00            cmp byte ptr [rip + 0xd68cc1], 0
0025C346  75 1B                           jne 0x14025c363
0025C348  41 8B C4                        mov eax, r12d
0025C34B  48 8D 15 0E 0F D7 00            lea rdx, [rip + 0xd70f0e]
0025C352  46 0F B6 24 62                  movzx r12d, byte ptr [rdx + r12*2]
0025C357  41 C1 E4 06                     shl r12d, 6
0025C35B  0F B6 44 42 01                  movzx eax, byte ptr [rdx + rax*2 + 1]
0025C360  44 0B E0                        or r12d, eax
0025C363  44 89 61 08                     mov dword ptr [rcx + 8], r12d
0025C367  8B 05 A7 A7 D6 00               mov eax, dword ptr [rip + 0xd6a7a7]
0025C36D  A8 20                           test al, 0x20
0025C36F  74 0B                           je 0x14025c37c
0025C371  8B D7                           mov edx, edi
0025C373  41 8B 4E 24                     mov ecx, dword ptr [r14 + 0x24]
0025C377  E8 44 EF 29 00                  call 0x1404fb2c0
0025C37C  41 8B D4                        mov edx, r12d
0025C37F  41 8B C4                        mov eax, r12d
0025C382  48 C1 EA 20                     shr rdx, 0x20
0025C386  B9 C2 00 00 40                  mov ecx, 0x400000c2
0025C38B  0F 30                           wrmsr
0025C38D  E9 D6 FD FF FF                  jmp 0x14025c168
0025C392  48 8D B4 24 58 01 00 00         lea rsi, [rsp + 0x158]
0025C39A  BA 01 00 00 00                  mov edx, 1
0025C39F  E9 5B FE FF FF                  jmp 0x14025c1ff
0025C3A4  BB 1E 00 00 00                  mov ebx, 0x1e
0025C3A9  E9 D1 F6 FF FF                  jmp 0x14025ba7f
0025C3AE  49 8B 4C DF 28                  mov rcx, qword ptr [r15 + rbx*8 + 0x28]
0025C3B3  45 33 C0                        xor r8d, r8d
0025C3B6  49 8B D6                        mov rdx, r14
0025C3B9  E8 8E F3 0A 00                  call 0x14030b74c
0025C3BE  E9 87 FD FF FF                  jmp 0x14025c14a
0025C3C3  48 89 B4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rsi
0025C3CB  E9 79 F4 FF FF                  jmp 0x14025b849
0025C3D0  41 0F 0D 08                     prefetchw byte ptr [r8]
0025C3D4  41 8B 00                        mov eax, dword ptr [r8]
0025C3D7  8B D0                           mov edx, eax
0025C3D9  0F BA F2 15                     btr edx, 0x15
0025C3DD  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0025C3E2  75 F3                           jne 0x14025c3d7
0025C3E4  0F BA E0 15                     bt eax, 0x15
0025C3E8  0F 83 82 F5 FF FF               jae 0x14025b970
0025C3EE  E8 DD 6D 00 00                  call 0x1402631d0
0025C3F3  E9 78 F5 FF FF                  jmp 0x14025b970
0025C3F8  49 0F BE 87 32 02 00 00         movsx rax, byte ptr [r15 + 0x232]
0025C400  38 44 24 31                     cmp byte ptr [rsp + 0x31], al
0025C404  74 1E                           je 0x14025c424
0025C406  4C 8B C0                        mov r8, rax
0025C409  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0025C40E  41 B9 04 00 00 00               mov r9d, 4
0025C414  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0025C419  B9 F9 01 00 00                  mov ecx, 0x1f9
0025C41E  E8 3D 12 2A 00                  call 0x1404fd660
0025C423  CC                              int3
0025C424  49 8B 83 B8 8E 00 00            mov rax, qword ptr [r11 + 0x8eb8]
0025C42B  48 85 C0                        test rax, rax
0025C42E  0F 85 33 05 00 00               jne 0x14025c967
0025C434  4C 8B 94 24 C0 00 00 00         mov r10, qword ptr [rsp + 0xc0]
0025C43C  4D 85 D2                        test r10, r10
0025C43F  0F 84 C0 00 00 00               je 0x14025c505
0025C445  45 8B 72 04                     mov r14d, dword ptr [r10 + 4]
0025C449  45 0F B7 3A                     movzx r15d, word ptr [r10]
0025C44D  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0025C452  48 89 84 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], rax
0025C45A  48 C7 84 24 F0 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x1f0], 8
0025C466  48 8B 05 3B A6 D6 00            mov rax, qword ptr [rip + 0xd6a63b]
0025C46D  8B 98 A8 11 00 00               mov ebx, dword ptr [rax + 0x11a8]
0025C473  0F BC CB                        bsf ecx, ebx
0025C476  89 4C 24 74                     mov dword ptr [rsp + 0x74], ecx
0025C47A  0F 84 7D 00 00 00               je 0x14025c4fd
0025C480  8D 43 FF                        lea eax, [rbx - 1]
0025C483  23 D8                           and ebx, eax
0025C485  44 8B C1                        mov r8d, ecx
0025C488  8B C1                           mov eax, ecx
0025C48A  48 C1 E0 05                     shl rax, 5
0025C48E  48 8B 15 13 A6 D6 00            mov rdx, qword ptr [rip + 0xd6a613]
0025C495  48 05 CC 11 00 00               add rax, 0x11cc
0025C49B  48 03 C2                        add rax, rdx
0025C49E  74 4F                           je 0x14025c4ef
0025C4A0  8B 40 04                        mov eax, dword ptr [rax + 4]
0025C4A3  84 C0                           test al, al
0025C4A5  79 48                           jns 0x14025c4ef
0025C4A7  0F B6 84 4A 99 11 00 00         movzx eax, byte ptr [rdx + rcx*2 + 0x1199]
0025C4AF  48 8D 8C C4 A0 01 00 00         lea rcx, [rsp + rax*8 + 0x1a0]
0025C4B7  48 89 8C 24 D8 01 00 00         mov qword ptr [rsp + 0x1d8], rcx
0025C4BF  48 C7 84 24 E0 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x1e0], 8
0025C4CB  46 0F B6 84 42 98 11 00 00      movzx r8d, byte ptr [rdx + r8*2 + 0x1198]
0025C4D4  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
0025C4D9  66 44 89 7C 24 20               mov word ptr [rsp + 0x20], r15w
0025C4DF  44 8B CF                        mov r9d, edi
0025C4E2  48 8D 8C 24 D8 01 00 00         lea rcx, [rsp + 0x1d8]
0025C4EA  E8 11 07 00 00                  call 0x14025cc00
0025C4EF  0F BC CB                        bsf ecx, ebx
0025C4F2  75 8C                           jne 0x14025c480
0025C4F4  89 4C 24 74                     mov dword ptr [rsp + 0x74], ecx
0025C4F8  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
0025C4FD  4C 8B BC 24 80 00 00 00         mov r15, qword ptr [rsp + 0x80]
0025C505  FA                              cli
0025C506  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
0025C50B  41 8B 40 18                     mov eax, dword ptr [r8 + 0x18]
0025C50F  85 C0                           test eax, eax
0025C511  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
0025C516  44 8B 4C 24 40                  mov r9d, dword ptr [rsp + 0x40]
0025C51B  4D 8B E0                        mov r12, r8
0025C51E  0F 85 47 F3 FF FF               jne 0x14025b86b
0025C524  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
0025C52C  49 89 83 90 2D 00 00            mov qword ptr [r11 + 0x2d90], rax
0025C533  41 F7 83 EC 00 00 00 00 08 00 00  test dword ptr [r11 + 0xec], 0x800
0025C53E  0F 84 E0 FC FF FF               je 0x14025c224
0025C544  4D 3B BB 38 38 00 00            cmp r15, qword ptr [r11 + 0x3838]
0025C54B  0F 84 D3 FC FF FF               je 0x14025c224
0025C551  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0025C55A  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0025C561  4D 85 C0                        test r8, r8
0025C564  0F 85 D9 01 00 00               jne 0x14025c743
0025C56A  FB                              sti
0025C56B  4C 89 9C 24 90 01 00 00         mov qword ptr [rsp + 0x190], r11
0025C573  49 8B DB                        mov rbx, r11
0025C576  48 83 CB 01                     or rbx, 1
0025C57A  48 89 9C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rbx
0025C582  48 89 9C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rbx
0025C58A  49 8B 8B 58 8E 00 00            mov rcx, qword ptr [r11 + 0x8e58]
0025C591  0F B6 11                        movzx edx, byte ptr [rcx]
0025C594  48 83 C1 08                     add rcx, 8
0025C598  E8 C3 6B 13 00                  call 0x140393160
0025C59D  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
0025C5A2  41 81 A6 EC 00 00 00 FF F7 FF FF  and dword ptr [r14 + 0xec], 0xfffff7ff
0025C5AD  49 8B 86 38 38 00 00            mov rax, qword ptr [r14 + 0x3838]
0025C5B4  48 85 C0                        test rax, rax
0025C5B7  0F 84 04 FC FF FF               je 0x14025c1c1
0025C5BD  49 39 46 10                     cmp qword ptr [r14 + 0x10], rax
0025C5C1  0F 85 FA FB FF FF               jne 0x14025c1c1
0025C5C7  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
0025C5CF  4D 8B BE E8 37 00 00            mov r15, qword ptr [r14 + 0x37e8]
0025C5D6  33 D2                           xor edx, edx
0025C5D8  41 B8 F0 00 00 00               mov r8d, 0xf0
0025C5DE  49 8B CF                        mov rcx, r15
0025C5E1  E8 5A A6 46 00                  call 0x1406c6c40
0025C5E6  45 33 C0                        xor r8d, r8d
0025C5E9  48 8D 94 24 D0 00 00 00         lea rdx, [rsp + 0xd0]
0025C5F1  49 8B CF                        mov rcx, r15
0025C5F4  E8 B7 00 0B 00                  call 0x14030c6b0
0025C5F9  49 8B 86 38 38 00 00            mov rax, qword ptr [r14 + 0x3838]
0025C600  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0025C605  48 89 B4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rsi
0025C60D  4D 8B 66 08                     mov r12, qword ptr [r14 + 8]
0025C611  45 8B 44 24 78                  mov r8d, dword ptr [r12 + 0x78]
0025C616  41 0F BA E0 0C                  bt r8d, 0xc
0025C61B  0F 82 58 03 00 00               jb 0x14025c979
0025C621  4D 3B A6 80 8E 00 00            cmp r12, qword ptr [r14 + 0x8e80]
0025C628  0F 84 4B 03 00 00               je 0x14025c979
0025C62E  49 8B D6                        mov rdx, r14
0025C631  49 8B CF                        mov rcx, r15
0025C634  E8 27 6A 0F 00                  call 0x140353060
0025C639  4C 8B F0                        mov r14, rax
0025C63C  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
0025C641  41 8B 49 78                     mov ecx, dword ptr [r9 + 0x78]
0025C645  83 E1 02                        and ecx, 2
0025C648  41 83 E0 02                     and r8d, 2
0025C64C  44 3A C1                        cmp r8b, cl
0025C64F  0F 87 47 04 00 00               ja 0x14025ca9c
0025C655  49 8B 06                        mov rax, qword ptr [r14]
0025C658  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0025C65C  49 89 4E 10                     mov qword ptr [r14 + 0x10], rcx
0025C660  48 3B 48 18                     cmp rcx, qword ptr [rax + 0x18]
0025C664  0F 94 C2                        sete dl
0025C667  41 0F B6 46 20                  movzx eax, byte ptr [r14 + 0x20]
0025C66C  24 FE                           and al, 0xfe
0025C66E  0A D0                           or dl, al
0025C670  41 88 56 20                     mov byte ptr [r14 + 0x20], dl
0025C674  8B 41 78                        mov eax, dword ptr [rcx + 0x78]
0025C677  D1 E8                           shr eax, 1
0025C679  24 01                           and al, 1
0025C67B  02 C0                           add al, al
0025C67D  80 E2 FD                        and dl, 0xfd
0025C680  32 C2                           xor al, dl
0025C682  24 C7                           and al, 0xc7
0025C684  0C 04                           or al, 4
0025C686  41 88 46 20                     mov byte ptr [r14 + 0x20], al
0025C68A  49 89 76 18                     mov qword ptr [r14 + 0x18], rsi
0025C68E  41 80 66 21 FE                  and byte ptr [r14 + 0x21], 0xfe
0025C693  41 80 4E 22 01                  or byte ptr [r14 + 0x22], 1
0025C698  41 8B 4C 24 78                  mov ecx, dword ptr [r12 + 0x78]
0025C69D  41 0B 49 78                     or ecx, dword ptr [r9 + 0x78]
0025C6A1  F6 C1 02                        test cl, 2
0025C6A4  0F 84 DF 03 00 00               je 0x14025ca89
0025C6AA  44 8B DE                        mov r11d, esi
0025C6AD  41 80 3F 00                     cmp byte ptr [r15], 0
0025C6B1  0F 86 D2 03 00 00               jbe 0x14025ca89
0025C6B7  41 8B C3                        mov eax, r11d
0025C6BA  4C 8D 0C 85 02 00 00 00         lea r9, [rax*4 + 2]
0025C6C2  4C 03 C8                        add r9, rax
0025C6C5  4F 8D 0C CF                     lea r9, [r15 + r9*8]
0025C6C9  4D 3B F1                        cmp r14, r9
0025C6CC  0F 84 A7 03 00 00               je 0x14025ca79
0025C6D2  48 89 B4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rsi
0025C6DA  49 8B 11                        mov rdx, qword ptr [r9]
0025C6DD  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
0025C6E2  41 8B 44 24 78                  mov eax, dword ptr [r12 + 0x78]
0025C6E7  49 8B 49 18                     mov rcx, qword ptr [r9 + 0x18]
0025C6EB  A8 02                           test al, 2
0025C6ED  48 8D 41 FF                     lea rax, [rcx - 1]
0025C6F1  0F 85 15 03 00 00               jne 0x14025ca0c
0025C6F7  4C 8B 52 18                     mov r10, qword ptr [rdx + 0x18]
0025C6FB  48 83 F8 FC                     cmp rax, -4
0025C6FF  0F 86 4B 04 00 00               jbe 0x14025cb50
0025C705  4D 89 51 10                     mov qword ptr [r9 + 0x10], r10
0025C709  41 0F B6 41 20                  movzx eax, byte ptr [r9 + 0x20]
0025C70E  0C 01                           or al, 1
0025C710  41 88 41 20                     mov byte ptr [r9 + 0x20], al
0025C714  41 8B 4A 78                     mov ecx, dword ptr [r10 + 0x78]
0025C718  D1 E9                           shr ecx, 1
0025C71A  80 E1 01                        and cl, 1
0025C71D  02 C9                           add cl, cl
0025C71F  24 FD                           and al, 0xfd
0025C721  32 C8                           xor cl, al
0025C723  80 E1 E7                        and cl, 0xe7
0025C726  80 C9 04                        or cl, 4
0025C729  80 E1 DF                        and cl, 0xdf
0025C72C  E9 25 03 00 00                  jmp 0x14025ca56
0025C731  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0025C736  49 8B CA                        mov rcx, r10
0025C739  E8 8E 1D 1A 00                  call 0x1403fe4cc
0025C73E  E9 BC F8 FF FF                  jmp 0x14025bfff
0025C743  41 0F 0D 08                     prefetchw byte ptr [r8]
0025C747  41 8B 00                        mov eax, dword ptr [r8]
0025C74A  8B D0                           mov edx, eax
0025C74C  0F BA F2 15                     btr edx, 0x15
0025C750  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0025C755  75 F3                           jne 0x14025c74a
0025C757  0F BA E0 15                     bt eax, 0x15
0025C75B  0F 83 09 FE FF FF               jae 0x14025c56a
0025C761  E8 6A 6A 00 00                  call 0x1402631d0
0025C766  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
0025C76B  E9 FA FD FF FF                  jmp 0x14025c56a
0025C770  B3 01                           mov bl, 1
0025C772  E9 1B F1 FF FF                  jmp 0x14025b892
0025C777  49 8B D7                        mov rdx, r15
0025C77A  49 8B CB                        mov rcx, r11
0025C77D  E8 D2 F6 0A 00                  call 0x14030be54
0025C782  84 C0                           test al, al
0025C784  74 46                           je 0x14025c7cc
0025C786  32 C0                           xor al, al
0025C788  E9 99 FA FF FF                  jmp 0x14025c226
0025C78D  E8 3E 26 12 00                  call 0x14037edd0
0025C792  48 89 84 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rax
0025C79A  E9 02 F3 FF FF                  jmp 0x14025baa1
0025C79F  8B 05 B3 16 CB 00               mov eax, dword ptr [rip + 0xcb16b3]
0025C7A5  85 C0                           test eax, eax
0025C7A7  0F 85 A5 F1 FF FF               jne 0x14025b952
0025C7AD  48 8B 94 24 38 02 00 00         mov rdx, qword ptr [rsp + 0x238]
0025C7B5  48 8B CB                        mov rcx, rbx
0025C7B8  E8 33 67 13 00                  call 0x140392ef0
0025C7BD  E9 95 F1 FF FF                  jmp 0x14025b957
0025C7C2  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0025C7C7  E9 DA F9 FF FF                  jmp 0x14025c1a6
0025C7CC  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
0025C7D1  E9 D4 F0 FF FF                  jmp 0x14025b8aa
0025C7D6  84 DB                           test bl, bl
0025C7D8  0F 84 CC F0 FF FF               je 0x14025b8aa
0025C7DE  E8 5D E1 1C 00                  call 0x14042a940
0025C7E3  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
0025C7E8  4C 8B 5C 24 38                  mov r11, qword ptr [rsp + 0x38]
0025C7ED  E9 B0 F0 FF FF                  jmp 0x14025b8a2
0025C7F2  E8 3D 79 14 00                  call 0x1403a4134
0025C7F7  48 89 84 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rax
0025C7FF  E9 C8 F2 FF FF                  jmp 0x14025bacc
0025C804  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0025C809  49 8B CF                        mov rcx, r15
0025C80C  E8 4F 68 0F 00                  call 0x140353060
0025C811  4C 8B C0                        mov r8, rax
0025C814  0F B6 48 20                     movzx ecx, byte ptr [rax + 0x20]
0025C818  44 8B D1                        mov r10d, ecx
0025C81B  41 D1 EA                        shr r10d, 1
0025C81E  41 83 E2 01                     and r10d, 1
0025C822  4C 8B 08                        mov r9, qword ptr [rax]
0025C825  F6 C1 20                        test cl, 0x20
0025C828  75 04                           jne 0x14025c82e
0025C82A  80 48 22 01                     or byte ptr [rax + 0x22], 1
0025C82E  80 60 22 FD                     and byte ptr [rax + 0x22], 0xfd
0025C832  49 8B 41 18                     mov rax, qword ptr [r9 + 0x18]
0025C836  49 89 40 10                     mov qword ptr [r8 + 0x10], rax
0025C83A  80 E1 C5                        and cl, 0xc5
0025C83D  80 C9 05                        or cl, 5
0025C840  41 88 48 20                     mov byte ptr [r8 + 0x20], cl
0025C844  49 8B 41 18                     mov rax, qword ptr [r9 + 0x18]
0025C848  49 89 40 18                     mov qword ptr [r8 + 0x18], rax
0025C84C  41 80 60 21 FE                  and byte ptr [r8 + 0x21], 0xfe
0025C851  45 85 D2                        test r10d, r10d
0025C854  0F 85 8C 02 00 00               jne 0x14025cae6
0025C85A  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
0025C862  49 8B CF                        mov rcx, r15
0025C865  E8 B6 BD FF FF                  call 0x140258620
0025C86A  45 32 C9                        xor r9b, r9b
0025C86D  F7 05 9D A2 D6 00 00 04 00 00   test dword ptr [rip + 0xd6a29d], 0x400
0025C877  44 8B E6                        mov r12d, esi
0025C87A  44 0F 45 E7                     cmovne r12d, edi
0025C87E  44 8B F6                        mov r14d, esi
0025C881  45 38 0F                        cmp byte ptr [r15], r9b
0025C884  76 51                           jbe 0x14025c8d7
0025C886  32 DB                           xor bl, bl
0025C888  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0025C88D  41 8B C6                        mov eax, r14d
0025C890  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
0025C898  48 03 C8                        add rcx, rax
0025C89B  49 8D 0C CF                     lea rcx, [r15 + rcx*8]
0025C89F  4C 8D 8C 24 A0 00 00 00         lea r9, [rsp + 0xa0]
0025C8A7  45 8B C4                        mov r8d, r12d
0025C8AA  48 8B D7                        mov rdx, rdi
0025C8AD  E8 1E 07 0B 00                  call 0x14030cfd0
0025C8B2  0A D8                           or bl, al
0025C8B4  41 FF C6                        inc r14d
0025C8B7  41 0F B6 07                     movzx eax, byte ptr [r15]
0025C8BB  44 3B F0                        cmp r14d, eax
0025C8BE  72 CD                           jb 0x14025c88d
0025C8C0  88 5C 24 30                     mov byte ptr [rsp + 0x30], bl
0025C8C4  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
0025C8CC  BF 02 00 00 00                  mov edi, 2
0025C8D1  44 0F B6 4C 24 30               movzx r9d, byte ptr [rsp + 0x30]
0025C8D7  41 83 7F 08 01                  cmp dword ptr [r15 + 8], 1
0025C8DC  75 1C                           jne 0x14025c8fa
0025C8DE  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
0025C8E2  48 8B 88 58 8E 00 00            mov rcx, qword ptr [rax + 0x8e58]
0025C8E9  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
0025C8ED  FE C0                           inc al
0025C8EF  88 41 01                        mov byte ptr [rcx + 1], al
0025C8F2  3A 01                           cmp al, byte ptr [rcx]
0025C8F4  72 04                           jb 0x14025c8fa
0025C8F6  C6 41 01 00                     mov byte ptr [rcx + 1], 0
0025C8FA  4C 8B C6                        mov r8, rsi
0025C8FD  8B D6                           mov edx, esi
0025C8FF  48 8B CB                        mov rcx, rbx
0025C902  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0025C906  48 89 8C 24 50 01 00 00         mov qword ptr [rsp + 0x150], rcx
0025C90E  83 E3 01                        and ebx, 1
0025C911  74 45                           je 0x14025c958
0025C913  83 FB 01                        cmp ebx, 1
0025C916  75 15                           jne 0x14025c92d
0025C918  4C 8B 81 58 8E 00 00            mov r8, qword ptr [rcx + 0x8e58]
0025C91F  49 83 C0 08                     add r8, 8
0025C923  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
0025C92A  0F B6 10                        movzx edx, byte ptr [rax]
0025C92D  85 D2                           test edx, edx
0025C92F  0F 84 15 F9 FF FF               je 0x14025c24a
0025C935  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
0025C940  8D 42 FF                        lea eax, [rdx - 1]
0025C943  8B D0                           mov edx, eax
0025C945  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0025C949  F0 48 83 61 30 00               lock and qword ptr [rcx + 0x30], 0
0025C94F  85 C0                           test eax, eax
0025C951  75 ED                           jne 0x14025c940
0025C953  E9 F2 F8 FF FF                  jmp 0x14025c24a
0025C958  4C 8D 84 24 50 01 00 00         lea r8, [rsp + 0x150]
0025C960  BA 01 00 00 00                  mov edx, 1
0025C965  EB C6                           jmp 0x14025c92d
0025C967  45 85 C0                        test r8d, r8d
0025C96A  0F 85 C4 FA FF FF               jne 0x14025c434
0025C970  F0 FF 48 1C                     lock dec dword ptr [rax + 0x1c]
0025C974  E9 BB FA FF FF                  jmp 0x14025c434
0025C979  49 8B D6                        mov rdx, r14
0025C97C  49 8B CF                        mov rcx, r15
0025C97F  E8 DC 66 0F 00                  call 0x140353060
0025C984  4C 8B D0                        mov r10, rax
0025C987  0F B6 48 20                     movzx ecx, byte ptr [rax + 0x20]
0025C98B  44 8B D9                        mov r11d, ecx
0025C98E  41 D1 EB                        shr r11d, 1
0025C991  41 83 E3 01                     and r11d, 1
0025C995  4C 8B 00                        mov r8, qword ptr [rax]
0025C998  F6 C1 20                        test cl, 0x20
0025C99B  75 04                           jne 0x14025c9a1
0025C99D  80 48 22 01                     or byte ptr [rax + 0x22], 1
0025C9A1  80 60 22 FD                     and byte ptr [rax + 0x22], 0xfd
0025C9A5  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
0025C9A9  49 89 42 10                     mov qword ptr [r10 + 0x10], rax
0025C9AD  80 E1 C5                        and cl, 0xc5
0025C9B0  80 C9 05                        or cl, 5
0025C9B3  41 88 4A 20                     mov byte ptr [r10 + 0x20], cl
0025C9B7  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
0025C9BB  49 89 42 18                     mov qword ptr [r10 + 0x18], rax
0025C9BF  41 80 62 21 FE                  and byte ptr [r10 + 0x21], 0xfe
0025C9C4  45 85 DB                        test r11d, r11d
0025C9C7  0F 84 8D FE FF FF               je 0x14025c85a
0025C9CD  44 8B F6                        mov r14d, esi
0025C9D0  41 80 3F 00                     cmp byte ptr [r15], 0
0025C9D4  76 2E                           jbe 0x14025ca04
0025C9D6  41 8B C6                        mov eax, r14d
0025C9D9  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
0025C9E1  48 03 C8                        add rcx, rax
0025C9E4  49 8D 0C CF                     lea rcx, [r15 + rcx*8]
0025C9E8  49 3B CA                        cmp rcx, r10
0025C9EB  74 0B                           je 0x14025c9f8
0025C9ED  45 33 C9                        xor r9d, r9d
0025C9F0  41 B0 01                        mov r8b, 1
0025C9F3  E8 48 59 0F 00                  call 0x140352340
0025C9F8  41 FF C6                        inc r14d
0025C9FB  41 0F B6 07                     movzx eax, byte ptr [r15]
0025C9FF  44 3B F0                        cmp r14d, eax
0025CA02  72 D2                           jb 0x14025c9d6
0025CA04  45 85 DB                        test r11d, r11d
0025CA07  E9 EA 00 00 00                  jmp 0x14025caf6
0025CA0C  4C 8B 92 80 8E 00 00            mov r10, qword ptr [rdx + 0x8e80]
0025CA13  48 83 F8 FC                     cmp rax, -4
0025CA17  0F 86 FA 00 00 00               jbe 0x14025cb17
0025CA1D  4D 89 61 10                     mov qword ptr [r9 + 0x10], r12
0025CA21  41 0F B6 41 20                  movzx eax, byte ptr [r9 + 0x20]
0025CA26  24 FE                           and al, 0xfe
0025CA28  41 88 41 20                     mov byte ptr [r9 + 0x20], al
0025CA2C  41 8B 4C 24 78                  mov ecx, dword ptr [r12 + 0x78]
0025CA31  D1 E9                           shr ecx, 1
0025CA33  80 E1 01                        and cl, 1
0025CA36  02 C9                           add cl, cl
0025CA38  24 FD                           and al, 0xfd
0025CA3A  32 C8                           xor cl, al
0025CA3C  80 E1 E7                        and cl, 0xe7
0025CA3F  80 C9 04                        or cl, 4
0025CA42  0F B6 C1                        movzx eax, cl
0025CA45  24 DF                           and al, 0xdf
0025CA47  80 C9 20                        or cl, 0x20
0025CA4A  0F B6 C9                        movzx ecx, cl
0025CA4D  0F B6 C0                        movzx eax, al
0025CA50  4D 3B E2                        cmp r12, r10
0025CA53  0F 44 C8                        cmove ecx, eax
0025CA56  41 88 49 20                     mov byte ptr [r9 + 0x20], cl
0025CA5A  4D 89 51 18                     mov qword ptr [r9 + 0x18], r10
0025CA5E  41 80 61 21 FE                  and byte ptr [r9 + 0x21], 0xfe
0025CA63  49 8B CA                        mov rcx, r10
0025CA66  E8 C5 67 0F 00                  call 0x140353230
0025CA6B  84 C0                           test al, al
0025CA6D  75 0A                           jne 0x14025ca79
0025CA6F  8B 42 24                        mov eax, dword ptr [rdx + 0x24]
0025CA72  41 89 82 18 02 00 00            mov dword ptr [r10 + 0x218], eax
0025CA79  41 FF C3                        inc r11d
0025CA7C  41 0F B6 07                     movzx eax, byte ptr [r15]
0025CA80  44 3B D8                        cmp r11d, eax
0025CA83  0F 82 2E FC FF FF               jb 0x14025c6b7
0025CA89  41 8B 44 24 78                  mov eax, dword ptr [r12 + 0x78]
0025CA8E  D1 E8                           shr eax, 1
0025CA90  83 E0 01                        and eax, 1
0025CA93  41 89 47 04                     mov dword ptr [r15 + 4], eax
0025CA97  E9 BE FD FF FF                  jmp 0x14025c85a
0025CA9C  8B C6                           mov eax, esi
0025CA9E  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0025CAA2  41 0F B6 0F                     movzx ecx, byte ptr [r15]
0025CAA6  3B C1                           cmp eax, ecx
0025CAA8  73 32                           jae 0x14025cadc
0025CAAA  48 8D 0C 85 02 00 00 00         lea rcx, [rax*4 + 2]
0025CAB2  48 03 C8                        add rcx, rax
0025CAB5  49 8D 0C CF                     lea rcx, [r15 + rcx*8]
0025CAB9  4C 3B F1                        cmp r14, rcx
0025CABC  74 16                           je 0x14025cad4
0025CABE  45 33 C9                        xor r9d, r9d
0025CAC1  44 8B C7                        mov r8d, edi
0025CAC4  49 8B D4                        mov rdx, r12
0025CAC7  E8 04 B7 FF FF                  call 0x1402581d0
0025CACC  84 C0                           test al, al
0025CACE  0F 84 30 FD FF FF               je 0x14025c804
0025CAD4  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
0025CAD8  FF C0                           inc eax
0025CADA  EB C2                           jmp 0x14025ca9e
0025CADC  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
0025CAE1  E9 6F FB FF FF                  jmp 0x14025c655
0025CAE6  44 8B DE                        mov r11d, esi
0025CAE9  41 80 3F 00                     cmp byte ptr [r15], 0
0025CAED  0F 87 9D 00 00 00               ja 0x14025cb90
0025CAF3  45 85 D2                        test r10d, r10d
0025CAF6  0F 84 5E FD FF FF               je 0x14025c85a
0025CAFC  41 89 77 04                     mov dword ptr [r15 + 4], esi
0025CB00  E9 55 FD FF FF                  jmp 0x14025c85a
0025CB05  B8 42 0F 00 00                  mov eax, 0xf42
0025CB0A  C7 44 24 7C 02 18 50 00         mov dword ptr [rsp + 0x7c], 0x501802
0025CB12  E9 20 ED FF FF                  jmp 0x14025b837
0025CB17  E8 14 67 0F 00                  call 0x140353230
0025CB1C  84 C0                           test al, al
0025CB1E  0F 85 F9 FE FF FF               jne 0x14025ca1d
0025CB24  41 F6 41 21 01                  test byte ptr [r9 + 0x21], 1
0025CB29  74 04                           je 0x14025cb2f
0025CB2B  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0025CB2F  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025CB36  48 8B D1                        mov rdx, rcx
0025CB39  48 8D 8C 24 C8 00 00 00         lea rcx, [rsp + 0xc8]
0025CB41  E8 CA 47 FA FF                  call 0x140201310
0025CB46  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0025CB4B  E9 CD FE FF FF                  jmp 0x14025ca1d
0025CB50  E8 DB 66 0F 00                  call 0x140353230
0025CB55  84 C0                           test al, al
0025CB57  0F 85 A8 FB FF FF               jne 0x14025c705
0025CB5D  41 F6 41 21 01                  test byte ptr [r9 + 0x21], 1
0025CB62  74 04                           je 0x14025cb68
0025CB64  83 49 74 02                     or dword ptr [rcx + 0x74], 2
0025CB68  C6 81 35 02 00 00 01            mov byte ptr [rcx + 0x235], 1
0025CB6F  48 8B D1                        mov rdx, rcx
0025CB72  48 8D 8C 24 C8 00 00 00         lea rcx, [rsp + 0xc8]
0025CB7A  E8 91 47 FA FF                  call 0x140201310
0025CB7F  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0025CB84  E9 7C FB FF FF                  jmp 0x14025c705
0025CB89  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0025CB90  41 8B C3                        mov eax, r11d
0025CB93  48 8D 14 85 02 00 00 00         lea rdx, [rax*4 + 2]
0025CB9B  48 03 D0                        add rdx, rax
0025CB9E  49 8D 14 D7                     lea rdx, [r15 + rdx*8]
0025CBA2  49 3B D0                        cmp rdx, r8
0025CBA5  74 36                           je 0x14025cbdd
0025CBA7  4C 8B 32                        mov r14, qword ptr [rdx]
0025CBAA  44 0F B6 4A 20                  movzx r9d, byte ptr [rdx + 0x20]
0025CBAF  41 F6 C1 20                     test r9b, 0x20
0025CBB3  75 04                           jne 0x14025cbb9
0025CBB5  80 4A 22 01                     or byte ptr [rdx + 0x22], 1
0025CBB9  80 62 22 FD                     and byte ptr [rdx + 0x22], 0xfd
0025CBBD  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0025CBC1  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
0025CBC5  41 80 E1 C5                     and r9b, 0xc5
0025CBC9  41 80 C9 05                     or r9b, 5
0025CBCD  44 88 4A 20                     mov byte ptr [rdx + 0x20], r9b
0025CBD1  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0025CBD5  48 89 42 18                     mov qword ptr [rdx + 0x18], rax
0025CBD9  80 62 21 FE                     and byte ptr [rdx + 0x21], 0xfe
0025CBDD  41 FF C3                        inc r11d
0025CBE0  41 0F B6 07                     movzx eax, byte ptr [r15]
0025CBE4  44 3B D8                        cmp r11d, eax
0025CBE7  72 A7                           jb 0x14025cb90
0025CBE9  E9 05 FF FF FF                  jmp 0x14025caf3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiExecuteAllDpcs(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1BC;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1CC;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned int v_stack_m1F4;
    unsigned int v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int8 v_stack_m207;
    unsigned __int8 v_stack_m208;
    unsigned int v_stack_m218;
    unsigned int v_stack_m238;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_p150;
    unsigned __int64 v_stack_p158;
    unsigned __int64 v_stack_p190;
    unsigned __int64 v_stack_p1B0;
    unsigned __int64 v_stack_p1C0;
    unsigned __int64 v_stack_p1D8;
    unsigned __int64 v_stack_p1E0;
    unsigned __int64 v_stack_p1E8;
    unsigned __int64 v_stack_p1F0;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p238;
    unsigned int v_stack_p28;
    unsigned __int8 v_stack_p30;
    unsigned __int8 v_stack_p31;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p74;
    unsigned int v_stack_p7C;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pE8;

    v_rsp = (v_rsp) - (512);
    result = (*(unsigned __int64 *)(v_rip + 12251110)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m1F8 = a4;
    v_stack_m138 = a3;
    v_stack_m1B8 = a2;
    v_stack_m148 = a1;
    v_stack_m200 = a1;
    v_stack_m108 = a1;
    v_stack_m120 = a2;
    v_stack_m118 = a3;
    v_stack_m188 = a4;
    v_rsi = 0;
    v_stack_m1F0 = 0;
    v_stack_mD8 = v_xmm0;
    v_stack_m1C0 = 0;
    v_stack_m90 = v_xmm1;
    v_stack_m80 = v_xmm1;
    v_stack_m128 = (unsigned int)(a4);
    a3 = ((unsigned int)(a4) + 300 + (unsigned int)(a4) + 300 * 2) << (4);
    a3 = (a3) + (a1);
    v_stack_m1D8 = a3;
    v_stack_m1E0 = a3 + 24;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 24))) == 0) goto loc_0025C224;
    if (!sign_flag) goto loc_0025C3C3;
    if (a4 != 0) goto loc_0025CB05;
    v_stack_m1BC = 0x500A02ULL;
loc_0025B837:
    v_stack_m1C0 = (unsigned __int16)((unsigned int)(0xF44ULL));
    v_stack_m178 = v_stack_m1C0;
loc_0025B849:
    v_stack_mF0 = a1 + 11664;
    v_stack_m150 = *(unsigned __int64 *)(a1 + 11664);
loc_0025B86B:
    a2 = ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 40))) != 0) ? 1 : 0;
    if (a4 != 0) goto loc_0025B890;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 40))) != 0) goto loc_0025C770;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 24)))) >= (*(unsigned int *)(v_rip + 14063942))) goto loc_0025C770;
loc_0025B890:
    v_rbx = 0;
loc_0025B892:
    if (((*(unsigned int *)(v_rip + 14070376)) & (0x40000ULL)) != 0) goto loc_0025C7D6;
loc_0025B8A2:
    if (0 != 0) goto loc_0025C777;
loc_0025B8AA:
    if (((*(unsigned __int8 *)(v_rip + 14070353)) & (33)) == 0) goto loc_0025C09A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13313431))) != 0) goto loc_0025C09A;
    result = KiAcquireSpinLockInstrumented(a3 + 16, a2, a3, a4);
loc_0025B8D1:
loc_0025B8D6:
    if ((*(unsigned int *)(a3 + 24)) <= 1) goto loc_0025C0B3;
loc_0025B8E0:
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(*(unsigned __int64 *)(a3));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3)) == 0) {
        *(unsigned __int64 *)(a3 + 8) = a3;
    }
    v_stack_m1F0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 24);
    v_stack_m1B0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 32);
    v_stack_m180 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 48);
    v_stack_m1A0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 56);
    v_stack_m158 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 56);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 56) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1E0))) - 1);
    *(unsigned int *)(v_stack_m1E0) = (unsigned int)(result);
    *(unsigned __int64 *)(v_stack_m1D8 + 32) = *(unsigned __int64 *)(a3) - 8;
    if (((*(unsigned __int8 *)(v_rip + 14070202)) & (1)) != 0) goto loc_0025C79F;
loc_0025B952:
loc_0025B957:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0025C3D0;
loc_0025B970:
    if (((*(unsigned int *)(v_rip + 14070153)) & (0x40000ULL)) != 0) {
        result = v_stack_m1F0;
        v_stack_mD8 = result;
        a2 = *(unsigned __int64 *)(a3) - 8;
        a2 = (a2) ^ (*(unsigned __int64 *)(v_rip + 14071992));
        a2 = (a2) ^ (result);
        result = *(unsigned __int64 *)(v_rip + 14071251);
        a1 = (unsigned int)(result);
        a2 = (a2) ^ (result);
        a2 = (a2) * (result);
        v_stack_mD0 = a2;
        result = v_stack_mD8;
        v_stack_m70 = result;
        v_stack_m68 = 16;
        a4 = 0xF65ULL;
        v_stack_m218 = 0x500A02ULL;
        a2 = 1;
        a3 = 0x20040000ULL;
        a1 = v_stack_m70;
        result = EtwTraceKernelEvent(a1, a2, a3, a4);
    }
    if (v_stack_m178 == 0) goto loc_0025BACC;
    v_stack_m1D0 = 0;
    if (*(unsigned __int64 *)(v_rip + 14107231) == 0) goto loc_0025C3A4;
    v_stack_m1D0 = (unsigned int)(a1);
    if (*(unsigned __int64 *)(v_rip + 14107231) == 0) goto loc_0025BA7F;
loc_0025BA40:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 14107231) + 4520))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 14107231) + 4520)) - 1)));
    result = (a1) << (5);
    result = (result) + (0x11CCULL);
    result = (result) + (*(unsigned __int64 *)(v_rip + 14107231));
    if (condition_is_equal) goto loc_0025BA6E;
    result = (unsigned int)(*(unsigned int *)(result + 4));
    v_rbx = 0;
    if (sign_flag) {
        a1 = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 14107231) + a1 * 2 + 4505);
        result = 1;
        result = (unsigned int)((result) << ((unsigned __int8)(a1)));
        v_rbx = (unsigned int)((0) | ((unsigned int)(result)));
    }
    if (condition_is_not_equal) goto loc_0025BA40;
    v_stack_m1D0 = (unsigned int)(a1);
loc_0025BA7F:
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_0025C0FA;
    v_stack_m90 = 0;
loc_0025BA90:
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) goto loc_0025C78D;
    v_stack_m88 = 0;
loc_0025BAA1:
    if ((((unsigned __int8)(v_rbx)) & (8)) == 0) goto loc_0025C0ED;
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_stack_m80 = result;
loc_0025BABB:
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) goto loc_0025C7F2;
    v_stack_m78 = 0;
loc_0025BACC:
    v_stack_m1F4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B8 + 484)));
    v_stack_m190 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B8 + 484)));
    v_stack_m207 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m1B8 + 562));
    v_stack_m208 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m1B8 + 562));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138))))) & (15));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m138))) + 1);
    *(unsigned int *)(v_stack_m138) = (unsigned int)(result);
    a1 = (a1) + 1;
    v_stack_m140 = v_stack_m138 + (unsigned int)((unsigned int)(a1)) + a1 * 2 * 8;
    *(unsigned __int64 *)(v_stack_m138 + (unsigned int)((unsigned int)(a1)) + a1 * 2 * 8) = v_stack_m1F0;
    *(unsigned __int64 *)(v_stack_m138 + (unsigned int)((unsigned int)(a1)) + a1 * 2 * 8 + 8) = *(unsigned __int64 *)(v_stack_m1F0);
    *(unsigned __int64 *)(v_stack_m138 + (unsigned int)((unsigned int)(a1)) + a1 * 2 * 8 + 16) = 0;
    v_stack_m160 = v_stack_m138 + (unsigned int)((unsigned int)(a1)) + a1 * 2 * 8;
    *(unsigned int *)(v_stack_m200 + 34396) = 0;
    a2 = (v_stack_m138) << (32);
    result = (*(unsigned __int64 *)(v_stack_m1F0)) | (a2);
    v_stack_m1A8 = result;
    *(unsigned __int64 *)(v_stack_mF0) = v_stack_m1A0;
    if (v_stack_m1A0 != 1) {
        *(unsigned __int64 *)(v_stack_m1A0 + 32) = result;
    }
    if (v_stack_m1F8 == 0) {
        *(unsigned __int64 *)(v_stack_m200 + 14368) = v_stack_m1F0;
        *(unsigned __int64 *)(v_stack_m200 + 14384) = result;
        *(unsigned __int8 *)(v_stack_m200 + 14522) = 1;
    }
    if (v_stack_m1F0 != (v_rip + 729872)) goto loc_0025BD8E;
    v_stack_m1E8 = 0;
    v_stack_m1E8 = 0;
loc_0025BBB3:
loc_0025BBBA:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 37232) == 0) goto loc_0025BC16;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 37232) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 37232));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 37232)) = 1;
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 37232) - 816 + 793);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 37232) - 816 + 793)) != 0) {
        v_stack_m218 = 0;
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 37240;
        a3 = v_stack_m1E8;
        a2 = 2;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 37232) - 816;
        result = KiAbProcessThreadLocks(a1, a2, a3, a4);
    }
    goto loc_0025BBBA;
loc_0025BC16:
    result = KiAbPropagateBoosts(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 37240, *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 37232, v_stack_m1E8, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 37232)) != 0) goto loc_0025BBB3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 37280) = 0;
    v_stack_m1CC = 0;
    v_stack_m1CC = 0;
    if (v_stack_m1E8 == 0) goto loc_0025BCA6;
    v_stack_m1E8 = *(unsigned __int64 *)(v_stack_m1E8);
loc_0025BC5C:
    if (v_stack_m1E8 == 0) goto loc_0025BCA6;
    a4 = 0;
    result = KiDeferredReadySingleThread(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40), v_stack_m1E8 - 216, v_stack_m1E8, a4);
    v_r15 = (unsigned int)((0) + 1);
    v_stack_m1CC = (unsigned int)(v_r15);
    if (v_stack_m1E8 != 0) {
        result = *(unsigned __int64 *)(v_stack_m1E8);
        v_stack_m1E8 = result;
    }
    if ((((unsigned __int8)(v_r15)) & (15)) == 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13784;
        result = KiFlushSoftwareInterruptBatch(a1, v_stack_m1E8 - 216, v_stack_m1E8, a4);
    }
    goto loc_0025BC5C;
loc_0025BCA6:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13785)) == 0) goto loc_0025BDD2;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13785))) == 1) goto loc_0025BCF4;
    result = KiSendSoftwareInterruptAffinity(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13792, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13784), v_stack_m1E8, a4);
loc_0025BCCE:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13785)) == 2) goto loc_0025BD6A;
loc_0025BCDC:
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13785) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13788) = 0xFFFFULL;
    goto loc_0025BDD2;
loc_0025BCF4:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36564))) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36564) = (unsigned int)(result);
    result = 0;
    v_stack_mC4 = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = 0;
    v_stack_mC8 = 6;
    v_stack_mC0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13788)));
    a2 = 31;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13784))) != 1) { a2 = 47; }
    result = HalpInterruptSendIpi(v_stack_mC8, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13784), a4);
    goto loc_0025BCCE;
loc_0025BD6A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13792) = 0x200001ULL;
    a2 = 0;
    result = memset(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40) + 13800, a2, 256, a4);
    goto loc_0025BCDC;
loc_0025BD8E:
    if (result != (v_rip - 212389)) goto loc_0025BDB7;
    result = KiSwapDirectoryTableBaseTarget(v_r15, v_stack_m1B0, *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40), v_stack_m180);
    goto loc_0025BDD2;
loc_0025BDB7:
    if (result != (v_rip + 508082)) goto loc_0025BDCD;
    result = PpmPerfAction(v_r15, v_stack_m1B0, *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40), v_stack_m180);
    goto loc_0025BDD2;
loc_0025BDCD:
    result = guard_dispatch_icall(v_r15, v_stack_m1B0, *(unsigned __int64 *)(*(unsigned __int64 *)(a3) - 8 + 40), v_stack_m180);
loc_0025BDD2:
    goto loc_0025BE4F;
loc_0025BE4F:
    a2 = (v_stack_m1B0) << (32);
    result = (result) | (a2);
    if ((unsigned int)((unsigned int)(v_stack_m1F8)) != 0) goto loc_0025C02A;
    *(unsigned __int8 *)(v_stack_m200 + 14522) = (unsigned __int8)((unsigned int)(v_stack_m1F8));
    if (*(unsigned __int64 *)(v_stack_m200 + 33560) == 0) goto loc_0025C10E;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200 + 33560) + (unsigned int)(*(unsigned int *)(v_stack_m200 + 33568)) + (unsigned int)(*(unsigned int *)(v_stack_m200 + 33568)) * 2 * 8) = v_stack_m1F0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200 + 33560) + (unsigned int)(*(unsigned int *)(v_stack_m200 + 33568)) + (unsigned int)(*(unsigned int *)(v_stack_m200 + 33568)) * 2 * 8 + 8) = v_stack_m1A8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200 + 33560) + (unsigned int)(*(unsigned int *)(v_stack_m200 + 33568)) + (unsigned int)(*(unsigned int *)(v_stack_m200 + 33568)) * 2 * 8 + 16) = result;
    if ((*(unsigned int *)(v_stack_m200 + 33568)) >= 32) {
        *(unsigned int *)(v_stack_m200 + 33568) = 0;
    }
    a3 = (result) - (v_stack_m1A8);
    if (*(unsigned __int64 *)(v_stack_m200 + 14352) == 0) goto loc_0025C00C;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m200 + 14352) + 4))))) & (31));
    v_r14 = (-1) << ((unsigned __int8)(a1));
    a4 = (v_r14) & (v_stack_m1F0);
    v_r15 = (a4) >> (56);
    v_r12 = (a4) >> (48);
    result = (a4) >> (40);
    v_stack_m1B0 = result;
    result = (a4) >> (32);
    v_stack_m1A8 = result;
    result = (a4) >> (24);
    v_stack_m160 = result;
    result = (a4) >> (16);
    v_stack_m158 = result;
    a2 = (a4) >> (8);
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m200 + 14352) + 4))) >> (5));
    if ((unsigned int)(v_r11) == 0) goto loc_0025C731;
    v_stack_mA0 = a4;
    result = ((unsigned __int8)(a4)) + (0xB15DCBULL);
    a1 = (a1) * (result);
    a1 = (a1) + ((unsigned __int8)(a2));
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_m158);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_m160);
    a2 = (a2) * (a1);
    a2 = (a2) + (v_stack_m1A8);
    a1 = (a1) * (a2);
    a1 = (a1) + (v_stack_m1B0);
    a2 = (a2) * (a1);
    a2 = (a2) + ((unsigned __int8)(v_r12));
    result = ((unsigned __int8)(v_r12)) * (a2);
    result = (result) + (v_r15);
    a2 = (v_r11 - 1) & ((unsigned int)((unsigned int)(result)));
loc_0025BFC9:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200 + 14352) + 8) + a2 * 8))) & (1)) != 0) goto loc_0025C731;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200 + 14352) + 8) + a2 * 8) + 8)) & (v_r14);
    if (a4 != result) goto loc_0025BFC9;
    a1 = (a3 + a3 * 2) >> (2);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200 + 14352) + 8) + a2 * 8) + 16)) >> (2);
    a1 = (a1) + (result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200 + 14352) + 8) + a2 * 8) + 16) = a1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200 + 14352) + 8) + a2 * 8) + 24) = 1;
loc_0025BFFF:
loc_0025C00C:
    *(unsigned __int64 *)(v_stack_m200 + 14368) = 0;
    *(unsigned __int64 *)(v_stack_m200 + 14376) = -1;
    *(unsigned __int64 *)(v_stack_m200 + 14384) = 0;
loc_0025C02A:
    v_rbx = result;
    if (v_stack_m1A0 != 1) {
        v_rbx = (result) - (*(unsigned __int64 *)(v_stack_m1A0 + 32));
    }
    *(unsigned __int64 *)(v_stack_m140 + 16) = *(unsigned __int64 *)(result);
    if (((unsigned int)((unsigned int)(v_stack_m1F4))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B8 + 484))))) goto loc_0025C3F8;
    v_stack_m218 = (unsigned int)(*(unsigned int *)(v_stack_m1B8 + 484));
    result = KeBugCheckEx(199, 4, v_stack_m1F0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4))));
loc_0025C09A:
    if (((unsigned int)((unsigned int)(v_stack_m1F4))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1B8 + 484))))) goto loc_0025B8D6;
    result = KxWaitForSpinLockAndAcquire(v_rbx, 4, v_stack_m1F0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4))));
    goto loc_0025B8D1;
loc_0025C0B3:
    *(unsigned int *)(v_stack_m1F0 + 40) = 0;
    if ((*(unsigned int *)(v_r14)) != 0) goto loc_0025B8E0;
    result = KxReleaseSpinLock(v_rbx, 4, v_stack_m1F0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4))));
    goto loc_0025C524;
loc_0025C0ED:
    v_stack_m80 = 0;
    goto loc_0025BABB;
loc_0025C0FA:
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, 4, v_stack_m1F0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4))));
    v_stack_m90 = result;
    goto loc_0025BA90;
loc_0025C10E:
    goto loc_0025BEBE;
loc_0025C11B:
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 13785)) != 0) goto loc_0025C2A2;
    *(unsigned __int8 *)(a1 + 13785) = 1;
    *(unsigned int *)(a1 + 13788) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 36)));
loc_0025C13E:
    if (((*(unsigned __int8 *)(v_stack_m1B8 + v_rbx * 8 + 51)) & (2)) != 0) goto loc_0025C3AE;
loc_0025C14A:
    if (((*(unsigned __int8 *)(v_stack_m1B8 + v_rbx * 8 + 51)) & (4)) == 0) goto loc_0025C168;
    if (*(unsigned __int64 *)(v_r14 + 36536) != 0) goto loc_0025C2F3;
loc_0025C168:
    result = *(unsigned __int64 *)(v_r14 + 36536);
    if (((*(unsigned __int8 *)(v_stack_m1B8 + v_rbx * 8 + 51)) & (1)) != 0) {
        result = *(unsigned __int64 *)(v_stack_m1B8 + v_rbx * 8 + 40);
    }
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((unsigned int)(v_rsi)) < ((unsigned int)(*(unsigned __int8 *)(v_stack_m1B8)))) goto loc_0025C270;
loc_0025C193:
    result = KiFlushSoftwareInterruptBatch(v_stack_m200 + 13784, 4, v_stack_m1F0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4))));
    v_rsi = 0;
loc_0025C1A6:
    if (v_stack_m198 != 0) {
        a2 = v_stack_m198;
        a1 = v_stack_m200;
        result = KiReadyDeferredReadyList(a1, a2, v_stack_m1F0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4))));
    }
    result = (v_stack_m168 != 0) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) goto loc_0025C223;
    a1 = (v_stack_m168) & (-2);
    v_stack_mE0 = a1;
    v_rbx = (unsigned int)((v_stack_m168) & (1));
    if (condition_is_equal) goto loc_0025C392;
    if (((unsigned int)(v_rbx)) == 1) {
        v_rsi = *(unsigned __int64 *)(a1 + 36440);
        v_rsi = (v_rsi) + (8);
        result = *(unsigned __int64 *)(a1 + 36440);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0025C223;
loc_0025C210:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0025C210;
loc_0025C223:
loc_0025C224:
loc_0025C226:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)((unsigned int)(a2 - 1)), v_stack_m1F0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4))));
    v_rsp = (v_rsp) + (512);
    return result;
loc_0025C24A:
    v_stack_pD0 = v_rsi;
    if ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4)))) == 0) goto loc_0025C7C2;
    if ((*(unsigned __int8 *)(v_stack_m1B8)) <= 0) goto loc_0025C193;
loc_0025C270:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 51))) & (16)) != 0) goto loc_0025C11B;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 51))) & (8)) == 0) goto loc_0025C13E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 16) + 7)) != 0) goto loc_0025C11B;
    goto loc_0025C13E;
loc_0025C2A2:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 51))) != 1) goto loc_0025C2EA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 13788)))) == (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 16) + 36))) goto loc_0025C13E;
    *(unsigned __int8 *)(a1 + 13785) = 2;
    result = KeAddProcessorAffinityEx(a1 + 13792, (unsigned int)(*(unsigned int *)(a1 + 13788)), v_stack_m1F0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4))));
loc_0025C2CE:
    result = KeAddGroupAffinityEx(a1 + 13792, *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 16) + 208), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 16) + 200), (unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4))));
    goto loc_0025C13E;
loc_0025C2EA:
    goto loc_0025C2CE;
loc_0025C2F3:
    if ((*(unsigned __int64 *)(v_stack_p38 + 36536)) == 0) goto loc_0025C168;
    if (v_stack_p38 == (*(unsigned __int64 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 16))) goto loc_0025C168;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))) & (0x40000ULL));
    if (condition_is_below) goto loc_0025C331;
    if ((unsigned int)(result) == 0) goto loc_0025C168;
    if (((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(result))))) >= ((unsigned int)(a1 + 13792))) goto loc_0025C168;
loc_0025C331:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p38 + 36536) + 12) = (unsigned int)(v_stack_m200);
    result = (unsigned __int8)((unsigned int)(*(unsigned int *)(result)));
    v_r12 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 16) + 36));
    if ((*(unsigned __int8 *)(v_rip + 14060737)) == 0) {
        result = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 16) + 36)));
        a2 = v_rip + 14094094;
        v_r12 = *(unsigned __int8 *)(a2 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 16) + 36)) * 2);
        v_r12 = (unsigned int)((v_r12) << (6));
        result = *(unsigned __int8 *)(a2 + result * 2 + 1);
        v_r12 = (unsigned int)((v_r12) | ((unsigned int)(result)));
    }
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p38 + 36536) + 8) = (unsigned int)(v_r12);
    result = (unsigned int)(*(unsigned int *)(v_rip + 14067623));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14067623)))) & (32)) != 0) {
        a2 = (unsigned int)(v_stack_m200);
        a1 = *(unsigned int *)(*(unsigned __int64 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 16) + 36);
        result = EtwTraceXSchedulerPriorityKickSend(a1, a2, v_stack_p38, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4))));
    }
    a2 = ((unsigned int)((unsigned int)(v_r12))) >> (32);
    goto loc_0025C168;
loc_0025C392:
    goto loc_0025C1FF;
loc_0025C3A4:
    goto loc_0025BA7F;
loc_0025C3AE:
    a3 = 0;
    result = EtwTraceScheduleThread(*(unsigned __int64 *)(v_stack_m1B8 + 30 * 8 + 40), *(unsigned __int64 *)(v_stack_m1B8 + (unsigned int)((unsigned int)(v_rsi)) + (unsigned int)((unsigned int)(v_rsi)) * 4 * 8 + 16), a3, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4))));
    goto loc_0025C14A;
loc_0025C3C3:
    v_stack_pC0 = v_stack_p158;
    goto loc_0025B849;
loc_0025C3D0:
loc_0025C3D7:
    if (condition_is_not_equal) goto loc_0025C3D7;
    if (condition_is_above_or_equal) goto loc_0025B970;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(v_stack_m1B8 + 30 * 8 + 40), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1F4))));
    goto loc_0025B970;
loc_0025C3F8:
    result = (__int8)(*(unsigned __int8 *)(v_stack_m1B8 + 562));
    if (v_stack_p31 != ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_stack_m1B8 + 562))))) {
        a3 = (__int8)(*(unsigned __int8 *)(v_stack_m1B8 + 562));
        v_stack_p20 = v_stack_p158;
        a4 = 4;
        a2 = v_stack_p48;
        a1 = 505;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_stack_m200 + 36536) != 0) goto loc_0025C967;
loc_0025C434:
    if (v_stack_pC0 == 0) goto loc_0025C505;
    v_stack_p1E8 = v_stack_p48;
    v_stack_p1F0 = 8;
    v_stack_p74 = (unsigned int)(a1);
    if (v_stack_pC0 == 0) goto loc_0025C4FD;
loc_0025C480:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 14067259) + 4520))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 14067259) + 4520)) - 1)));
    result = ((unsigned int)((unsigned int)(a1))) << (5);
    result = (result) + (0x11CCULL);
    result = (result) + (*(unsigned __int64 *)(v_rip + 14067219));
    if (condition_is_equal) goto loc_0025C4EF;
    result = (unsigned int)(*(unsigned int *)(result + 4));
    if (sign_flag) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 14067219) + a1 * 2 + 4505);
        a1 = v_rsp + result * 8 + 416;
        v_stack_p1D8 = a1;
        v_stack_p1E0 = 8;
        a3 = *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 14067219) + (unsigned int)((unsigned int)(a1)) * 2 + 4504);
        v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_pC0 + 4)));
        v_stack_p20 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_pC0));
        a4 = (unsigned int)(v_stack_m200);
        a1 = v_stack_p1D8;
        result = EtwpLogKernelEvent(a1, *(unsigned __int64 *)(v_rip + 14067219), a3, a4);
    }
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 4))) != 0) goto loc_0025C480;
    v_stack_p74 = (unsigned int)(a1);
loc_0025C4FD:
loc_0025C505:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p60 + 24))) != 0) goto loc_0025B86B;
loc_0025C524:
    *(unsigned __int64 *)(v_stack_p38 + 11664) = v_stack_pE8;
    if (((*(unsigned int *)(v_stack_p38 + 236)) & (0x800ULL)) == 0) goto loc_0025C224;
    if (v_stack_p80 == (*(unsigned __int64 *)(v_stack_p38 + 14392))) goto loc_0025C224;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0025C743;
loc_0025C56A:
    v_stack_p190 = v_stack_p38;
    v_rbx = (v_stack_p38) | (1);
    v_stack_pE8 = v_rbx;
    v_stack_pD0 = v_rbx;
    a1 = (*(unsigned __int64 *)(v_stack_p38 + 36440)) + (8);
    result = KiAcquireMultiplePrcbLocks(a1, *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 36440)), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), (unsigned int)(v_stack_p40));
    if (*(unsigned __int64 *)(v_stack_p38 + 14392) == 0) goto loc_0025C1C1;
    if ((*(unsigned __int64 *)(v_stack_p38 + 16)) != (*(unsigned __int64 *)(v_stack_p38 + 14392))) goto loc_0025C1C1;
    v_stack_pA0 = v_stack_p158;
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_stack_p38 + 14312), a2, 240, (unsigned int)(v_stack_p40));
    a3 = 0;
    result = KiStartRescheduleContext(*(unsigned __int64 *)(v_stack_p38 + 14312), v_stack_pD0, a3, (unsigned int)(v_stack_p40));
    v_stack_p58 = *(unsigned __int64 *)(v_stack_p38 + 14392);
    v_stack_pC8 = v_stack_p158;
    if (condition_is_below) goto loc_0025C979;
    if ((*(unsigned __int64 *)(v_stack_p38 + 8)) == (*(unsigned __int64 *)(v_stack_p38 + 36480))) goto loc_0025C979;
    result = KiFindRescheduleContextEntryForPrcb(*(unsigned __int64 *)(v_stack_p38 + 14312), v_stack_p38, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p38 + 8) + 120)), (unsigned int)(v_stack_p40));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p58 + 120))) & (2));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p38 + 8) + 120))) & (2));
    if (((unsigned __int8)(a3)) > ((unsigned __int8)(a1))) goto loc_0025CA9C;
loc_0025C655:
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8);
    a2 = ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24))) ? 1 : 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(result + 32)) & (254));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(a2);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) + 120))) >> (1));
    result = (unsigned __int8)((result) & (1));
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    a2 = (unsigned __int8)((a2) & (253));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a2)));
    result = (unsigned __int8)((result) & (199));
    result = (unsigned __int8)((result) | (4));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(result);
    *(unsigned __int64 *)(result + 24) = v_stack_p158;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p38 + 8) + 120))) | (*(unsigned int *)(v_stack_p58 + 120)));
    if ((((unsigned __int8)(a1)) & (2)) == 0) goto loc_0025CA89;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312))) <= 0) goto loc_0025CA89;
loc_0025C6B7:
    a4 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p158)))) * 4 + 2) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p158)))));
    if (result == (*(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8)) goto loc_0025CA79;
    v_stack_pC8 = v_stack_p158;
    v_stack_p58 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p38 + 8) + 120)))) & (2)) != 0) goto loc_0025CA0C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8 + 24) - 1) <= -4) goto loc_0025CB50;
loc_0025C705:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8) + 24);
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8 + 32)) | (1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8 + 32) = (unsigned __int8)(result);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8) + 24) + 120))) >> (1));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (253));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (231));
    a1 = (unsigned __int8)((a1) | (4));
    a1 = (unsigned __int8)((a1) & (223));
    goto loc_0025CA56;
loc_0025C731:
    result = KiInsertNewDpcRuntime(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8) + 24), v_stack_p48, a3, *(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8);
    goto loc_0025BFFF;
loc_0025C743:
loc_0025C74A:
    if (condition_is_not_equal) goto loc_0025C74A;
    if (condition_is_above_or_equal) goto loc_0025C56A;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8) + 24), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, *(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8);
    goto loc_0025C56A;
loc_0025C770:
    goto loc_0025B892;
loc_0025C777:
    result = KiEnterLongDpcProcessing(v_stack_p38, *(unsigned __int64 *)(v_stack_p38 + 14312), a3, *(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8);
    if ((unsigned __int8)(result) == 0) goto loc_0025C7CC;
    result = 0;
    goto loc_0025C226;
loc_0025C78D:
    result = RtlGetSystemTimePrecise(v_stack_p38, *(unsigned __int64 *)(v_stack_p38 + 14312), a3, *(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8);
    v_stack_p1B0 = result;
    goto loc_0025BAA1;
loc_0025C79F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13309619))) != 0) goto loc_0025B952;
    result = KiReleaseSpinLockInstrumented(1, v_stack_p238, a3, *(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8);
    goto loc_0025B957;
loc_0025C7C2:
    goto loc_0025C1A6;
loc_0025C7CC:
    goto loc_0025B8AA;
loc_0025C7D6:
    if (1 == 0) goto loc_0025B8AA;
    result = EtwTraceLongDpcDetectionEvent(1, v_stack_p238, v_stack_p60, *(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8);
    goto loc_0025B8A2;
loc_0025C7F2:
    result = EtwpGetHostPerfCounter(1, v_stack_p238, v_stack_p60, *(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8);
    v_stack_p1C0 = result;
    goto loc_0025BACC;
loc_0025C804:
    result = KiFindRescheduleContextEntryForPrcb(*(unsigned __int64 *)(v_stack_p38 + 14312), v_stack_p38, v_stack_p60, *(unsigned __int64 *)(v_stack_p38 + 14312) + a4 * 8);
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(result + 32)))) >> (1));
    v_r10 = (unsigned int)((v_r10) & (1));
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (32)) == 0) {
    }
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(result + 32)) & (197));
    a1 = (unsigned __int8)((a1) | (5));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    if ((unsigned int)(v_r10) != 0) goto loc_0025CAE6;
loc_0025C85A:
    result = KiSearchForNewThreadsForRescheduleContext(*(unsigned __int64 *)(v_stack_p38 + 14312), v_stack_pA0, result, *(unsigned __int64 *)(result));
    a4 = 0;
    v_r12 = (unsigned int)((unsigned int)(v_stack_p158));
    if (((*(unsigned int *)(v_rip + 14066333)) & (0x400ULL)) != 0) { v_r12 = (unsigned int)(v_stack_p38); }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312))) <= 0) goto loc_0025C8D7;
    v_rbx = 0;
loc_0025C88D:
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p158)))) * 4 + 2) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p158)))));
    result = KiCommitRescheduleContextEntry(*(unsigned __int64 *)(v_stack_p38 + 14312) + a1 * 8, v_stack_p38, (unsigned int)((unsigned int)(v_r12)), v_stack_pA0);
    v_rbx = (unsigned __int8)((v_rbx) | ((unsigned __int8)(result)));
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p158))) + 1);
    if (((unsigned int)(v_r14)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312))))) goto loc_0025C88D;
    v_stack_p30 = (unsigned __int8)(v_rbx);
loc_0025C8D7:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + 8)) != 1) goto loc_0025C8FA;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + 16) + 36440) + 1)) + 1);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + 16) + 36440) + 1) = (unsigned __int8)(result);
    if (((unsigned __int8)(result)) >= (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + 16) + 36440)))) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + 16) + 36440) + 1) = 0;
    }
    a1 = (v_stack_pE8) & (-2);
    v_stack_p150 = a1;
    v_rbx = (unsigned int)((v_stack_pE8) & (1));
    if (condition_is_equal) goto loc_0025C958;
    if (((unsigned int)(v_rbx)) == 1) {
        a3 = *(unsigned __int64 *)(a1 + 36440);
        a3 = (a3) + (8);
        result = *(unsigned __int64 *)(a1 + 36440);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0025C24A;
loc_0025C940:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0025C940;
    goto loc_0025C24A;
loc_0025C958:
    goto loc_0025C92D;
loc_0025C967:
    if ((unsigned int)(v_stack_p150) != 0) goto loc_0025C434;
    goto loc_0025C434;
loc_0025C979:
    result = KiFindRescheduleContextEntryForPrcb(*(unsigned __int64 *)(v_stack_p38 + 14312), v_r14, v_stack_p150, v_stack_p30);
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(result + 32)))) >> (1));
    v_r11 = (unsigned int)((v_r11) & (1));
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 32))) & (32)) == 0) {
    }
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(result + 32)) & (197));
    a1 = (unsigned __int8)((a1) | (5));
    *(unsigned __int8 *)(result + 32) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 24);
    if ((unsigned int)(v_r11) == 0) goto loc_0025C85A;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312))) <= 0) goto loc_0025CA04;
loc_0025C9D6:
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p158)))) * 4 + 2) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p158)))));
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p158))));
    if ((*(unsigned __int64 *)(v_stack_p38 + 14312) + a1 * 8) != result) {
        a4 = 0;
        a3 = 1;
        result = KiAdjustRescheduleContextEntryForThreadRemoval(*(unsigned __int64 *)(v_stack_p38 + 14312) + a1 * 8, v_r14, a3, a4);
    }
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p158))) + 1);
    if (((unsigned int)(v_r14)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312))))) goto loc_0025C9D6;
loc_0025CA04:
    goto loc_0025CAF6;
loc_0025CA0C:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312))) <= -4) goto loc_0025CB17;
loc_0025CA1D:
    *(unsigned __int64 *)(a4 + 16) = v_r12;
    result = (unsigned __int8)((*(unsigned __int8 *)(a4 + 32)) & (254));
    *(unsigned __int8 *)(a4 + 32) = (unsigned __int8)(result);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r12 + 120))) >> (1));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (253));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (231));
    a1 = (unsigned __int8)((a1) | (4));
    result = (unsigned __int8)(((unsigned __int8)(a1)) & (223));
    a1 = (unsigned __int8)((a1) | (32));
    a1 = (unsigned __int8)(a1);
    if (v_r12 == (*(unsigned __int64 *)(v_r14 + 36480))) { a1 = (unsigned int)((unsigned __int8)(result)); }
loc_0025CA56:
    *(unsigned __int8 *)(a4 + 32) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(a4 + 24) = *(unsigned __int64 *)(v_r14 + 36480);
    result = KiIsPrcbThread(*(unsigned __int64 *)(v_r14 + 36480), v_r14, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned int *)(v_r14 + 36);
        *(unsigned int *)(*(unsigned __int64 *)(v_r14 + 36480) + 536) = (unsigned int)(result);
    }
    v_r11 = (unsigned int)((v_r11) + 1);
    if (((unsigned int)(v_r11)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312))))) goto loc_0025C6B7;
loc_0025CA89:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r12 + 120))) >> (1));
    result = (unsigned int)((result) & (1));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + 4) = (unsigned int)(result);
    goto loc_0025C85A;
loc_0025CA9C:
loc_0025CA9E:
    v_stack_p44 = (unsigned int)((unsigned int)((unsigned int)(v_stack_p158)));
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_p158)))) >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312))))) goto loc_0025CADC;
    a1 = ((unsigned int)((unsigned int)(v_stack_p158)) * 4 + 2) + ((unsigned int)((unsigned int)(v_stack_p158)));
    if (v_r14 == (*(unsigned __int64 *)(v_stack_p38 + 14312) + a1 * 8)) goto loc_0025CAD4;
    a4 = 0;
    result = KiDoesThreadDominateRescheduleContextEntry(*(unsigned __int64 *)(v_stack_p38 + 14312) + a1 * 8, v_r12, 2, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0025C804;
loc_0025CAD4:
    result = (unsigned int)(((unsigned int)(v_stack_p44)) + 1);
    goto loc_0025CA9E;
loc_0025CADC:
    goto loc_0025C655;
loc_0025CAE6:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312))) > 0) goto loc_0025CB90;
loc_0025CAF3:
loc_0025CAF6:
    if ((unsigned int)(*(unsigned __int64 *)(v_r14 + 36480)) == 0) goto loc_0025C85A;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + 4) = (unsigned int)(v_stack_p158);
    goto loc_0025C85A;
loc_0025CB05:
    v_stack_p7C = 0x501802ULL;
    goto loc_0025B837;
loc_0025CB17:
    result = KiIsPrcbThread(*(unsigned __int64 *)(v_stack_p38 + 14312) + a1 * 8, v_r12, 2, v_stack_p58);
    if ((unsigned __int8)(result) != 0) goto loc_0025CA1D;
    if (((*(unsigned __int8 *)(v_stack_p58 + 33)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a1 * 8 + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_pC8, *(unsigned __int64 *)(v_stack_p38 + 14312) + a1 * 8, 2, v_stack_p58);
    goto loc_0025CA1D;
loc_0025CB50:
    result = KiIsPrcbThread(v_stack_pC8, v_stack_p58, 2, v_stack_p58);
    if ((unsigned __int8)(result) != 0) goto loc_0025C705;
    if (((*(unsigned __int8 *)(v_stack_p58 + 33)) & (1)) != 0) {
    }
    *(unsigned __int8 *)(v_stack_pC8 + 565) = 1;
    result = KiInsertDeferredReadyList(v_stack_pC8, v_stack_pC8, 2, v_stack_p58);
    goto loc_0025C705;
loc_0025CB90:
    a2 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p158)))) * 4 + 2) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p158)))));
    if ((*(unsigned __int64 *)(v_stack_p38 + 14312) + a2 * 8) == 2) goto loc_0025CBDD;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a2 * 8 + 32))) & (32)) == 0) {
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a2 * 8 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a2 * 8) + 24);
    a4 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a2 * 8 + 32)) & (197));
    a4 = (unsigned __int8)((a4) | (5));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a2 * 8 + 32) = (unsigned __int8)(a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a2 * 8 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 14312) + a2 * 8) + 24);
loc_0025CBDD:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p158))) + 1);
    if (((unsigned int)(v_r11)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 14312))))) goto loc_0025CB90;
    goto loc_0025CAF3;
}
```

## 5. (Beta) C Style

```c
int64_t KiExecuteAllDpcs(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1BC;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1CC;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint32_t v_stack_m1F4;
    uint32_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint8_t v_stack_m207;
    uint8_t v_stack_m208;
    uint32_t v_stack_m218;
    uint32_t v_stack_m238;
    uint64_t v_stack_m40;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;
    uint64_t v_stack_p150;
    uint64_t v_stack_p158;
    uint64_t v_stack_p190;
    uint64_t v_stack_p1B0;
    uint64_t v_stack_p1C0;
    uint64_t v_stack_p1D8;
    uint64_t v_stack_p1E0;
    uint64_t v_stack_p1E8;
    uint64_t v_stack_p1F0;
    uint64_t v_stack_p20;
    uint64_t v_stack_p238;
    uint32_t v_stack_p28;
    uint8_t v_stack_p30;
    uint8_t v_stack_p31;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p74;
    uint32_t v_stack_p7C;
    uint64_t v_stack_p80;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pE8;

    local_rsp = (local_rsp) - (512);
    result = (*(uint64_t *)(v_rip + 0xBAEFE6)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m1F8 = Arg4;
    v_stack_m138 = Arg3;
    v_stack_m1B8 = Arg2;
    v_stack_m148 = Arg1;
    v_stack_m200 = Arg1;
    v_stack_m108 = Arg1;
    v_stack_m120 = Arg2;
    v_stack_m118 = Arg3;
    v_stack_m188 = Arg4;
    local_rsi = 0;
    v_stack_m1F0 = 0;
    v_stack_mD8 = v_xmm0;
    v_stack_m1C0 = 0;
    v_stack_m90 = v_xmm1;
    v_stack_m80 = v_xmm1;
    v_stack_m128 = (uint32_t)(Arg4);
    Arg3 = ((uint32_t)(Arg4) + 300 + (uint32_t)(Arg4) + 300 * 2) << (4);
    Arg3 = (Arg3) + (Arg1);
    v_stack_m1D8 = Arg3;
    v_stack_m1E0 = Arg3 + 24;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x18))) == 0) goto loc_0025C224;
    if (!sign_flag) goto loc_0025C3C3;
    if (Arg4 != NULL) goto loc_0025CB05;
    v_stack_m1BC = 0x500A02ULL;
loc_0025B837:
    v_stack_m1C0 = (uint16_t)((uint32_t)(0xF44ULL));
    v_stack_m178 = v_stack_m1C0;
loc_0025B849:
    v_stack_mF0 = Arg1 + 11664;
    v_stack_m150 = *(uint64_t *)(arg1 + 0x2D90);
loc_0025B86B:
    Arg2 = ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x28))) != 0) ? 1 : 0;
    if (Arg4 != NULL) goto loc_0025B890;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x28))) != 0) goto loc_0025C770;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x18)))) >= (*(uint32_t *)(v_rip + 0xD69946))) goto loc_0025C770;
loc_0025B890:
    local_rbx = 0;
loc_0025B892:
    if (((*(uint32_t *)(v_rip + 0xD6B268)) & (0x40000ULL)) != 0) goto loc_0025C7D6;
loc_0025B8A2:
    if (0 != 0) goto loc_0025C777;
loc_0025B8AA:
    if (((*(uint8_t *)(v_rip + 0xD6B251)) & (33)) == 0) goto loc_0025C09A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB2597))) != 0) goto loc_0025C09A;
    result = KiAcquireSpinLockInstrumented(Arg3 + 16, Arg2, Arg3, Arg4);
loc_0025B8D1:
loc_0025B8D6:
    if ((*(uint32_t *)(Arg3 + 0x18)) <= 1) goto loc_0025C0B3;
loc_0025B8E0:
    *(uint64_t *)(Arg3) = *(uint64_t *)(*(uint64_t *)(Arg3));
    if (*(uint64_t *)(*(uint64_t *)(Arg3)) == 0) {
        *(uint64_t *)(Arg3 + 0x8) = Arg3;
    }
    v_stack_m1F0 = *(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x18);
    v_stack_m1B0 = *(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x20);
    v_stack_m180 = *(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x30);
    v_stack_m1A0 = *(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x38);
    v_stack_m158 = *(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x38);
    *(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x38) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1E0))) - 1);
    *(uint32_t *)(v_stack_m1E0) = (uint32_t)(result);
    *(uint64_t *)(v_stack_m1D8 + 0x20) = *(uint64_t *)(Arg3) - 8;
    if (((*(uint8_t *)(v_rip + 0xD6B1BA)) & (1)) != 0) goto loc_0025C79F;
loc_0025B952:
loc_0025B957:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0025C3D0;
loc_0025B970:
    if (((*(uint32_t *)(v_rip + 0xD6B189)) & (0x40000ULL)) != 0) {
        result = v_stack_m1F0;
        v_stack_mD8 = result;
        Arg2 = *(uint64_t *)(Arg3) - 8;
        Arg2 = (Arg2) ^ (*(uint64_t *)(v_rip + 0xD6B8B8));
        Arg2 = (Arg2) ^ (result);
        result = *(uint64_t *)(v_rip + 0xD6B5D3);
        Arg1 = (uint32_t)(result);
        Arg2 = (Arg2) ^ (result);
        Arg2 = (Arg2) * (result);
        v_stack_mD0 = Arg2;
        result = v_stack_mD8;
        v_stack_m70 = result;
        v_stack_m68 = 16;
        Arg4 = 0xF65ULL;
        v_stack_m218 = 0x500A02ULL;
        Arg2 = 1;
        Arg3 = 0x20040000ULL;
        Arg1 = v_stack_m70;
        result = EtwTraceKernelEvent(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m178 == 0) goto loc_0025BACC;
    v_stack_m1D0 = 0;
    if (*(uint64_t *)(v_rip + 0xD7425F) == 0) goto loc_0025C3A4;
    v_stack_m1D0 = (uint32_t)(Arg1);
    if (*(uint64_t *)(v_rip + 0xD7425F) == 0) goto loc_0025BA7F;
loc_0025BA40:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xD7425F) + 0x11A8))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xD7425F) + 0x11A8)) - 1)));
    result = (Arg1) << (5);
    result = (result) + (0x11CCULL);
    result = (result) + (*(uint64_t *)(v_rip + 0xD7425F));
    if (condition_is_equal) goto loc_0025BA6E;
    result = (uint32_t)(*(uint32_t *)(result + 0x4));
    local_rbx = 0;
    if (sign_flag) {
        Arg1 = *(uint8_t *)(*(uint64_t *)(v_rip + 0xD7425F) + arg1 * 2 + 0x1199);
        result = 1;
        result = (uint32_t)((result) << ((uint8_t)(Arg1)));
        local_rbx = (uint32_t)((0) | ((uint32_t)(result)));
    }
    if (condition_is_not_equal) goto loc_0025BA40;
    v_stack_m1D0 = (uint32_t)(Arg1);
loc_0025BA7F:
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_0025C0FA;
    v_stack_m90 = 0;
loc_0025BA90:
    if ((((uint8_t)(local_rbx)) & (4)) != 0) goto loc_0025C78D;
    v_stack_m88 = 0;
loc_0025BAA1:
    if ((((uint8_t)(local_rbx)) & (8)) == 0) goto loc_0025C0ED;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    v_stack_m80 = result;
loc_0025BABB:
    if ((((uint8_t)(local_rbx)) & (16)) != 0) goto loc_0025C7F2;
    v_stack_m78 = 0;
loc_0025BACC:
    v_stack_m1F4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B8 + 0x1E4)));
    v_stack_m190 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B8 + 0x1E4)));
    v_stack_m207 = (uint8_t)(*(uint8_t *)(v_stack_m1B8 + 0x232));
    v_stack_m208 = (uint8_t)(*(uint8_t *)(v_stack_m1B8 + 0x232));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138))))) & (15));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m138))) + 1);
    *(uint32_t *)(v_stack_m138) = (uint32_t)(result);
    Arg1 = (Arg1) + 1;
    v_stack_m140 = v_stack_m138 + (uint32_t)((uint32_t)(Arg1)) + Arg1 * 2 * 8;
    *(uint64_t *)(v_stack_m138 + (uint32_t)((uint32_t)(arg1)) + arg1 * 2 * 8) = v_stack_m1F0;
    *(uint64_t *)(v_stack_m138 + (uint32_t)((uint32_t)(arg1)) + arg1 * 2 * 8 + 0x8) = *(uint64_t *)(v_stack_m1F0);
    *(uint64_t *)(v_stack_m138 + (uint32_t)((uint32_t)(arg1)) + arg1 * 2 * 8 + 0x10) = 0;
    v_stack_m160 = v_stack_m138 + (uint32_t)((uint32_t)(Arg1)) + Arg1 * 2 * 8;
    *(uint32_t *)(v_stack_m200 + 0x865C) = 0;
    Arg2 = (v_stack_m138) << (32);
    result = (*(uint64_t *)(v_stack_m1F0)) | (Arg2);
    v_stack_m1A8 = result;
    *(uint64_t *)(v_stack_mF0) = v_stack_m1A0;
    if (v_stack_m1A0 != 1) {
        *(uint64_t *)(v_stack_m1A0 + 0x20) = result;
    }
    if (v_stack_m1F8 == 0) {
        *(uint64_t *)(v_stack_m200 + 0x3820) = v_stack_m1F0;
        *(uint64_t *)(v_stack_m200 + 0x3830) = result;
        *(uint8_t *)(v_stack_m200 + 0x38BA) = 1;
    }
    if (v_stack_m1F0 != (v_rip + 729872)) goto loc_0025BD8E;
    v_stack_m1E8 = 0;
    v_stack_m1E8 = 0;
loc_0025BBB3:
loc_0025BBBA:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x9170) == 0) goto loc_0025BC16;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x9170) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x9170));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x9170)) = 1;
    result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x9170) - 0x330 + 0x319);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x9170) - 0x330 + 0x319)) != 0) {
        v_stack_m218 = 0;
        Arg4 = *(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 37240;
        Arg3 = v_stack_m1E8;
        Arg2 = 2;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x9170) - 816;
        result = KiAbProcessThreadLocks(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_0025BBBA;
loc_0025BC16:
    result = KiAbPropagateBoosts(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 37240, *(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 37232, v_stack_m1E8, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x9170)) != 0) goto loc_0025BBB3;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x91A0) = 0;
    v_stack_m1CC = 0;
    v_stack_m1CC = 0;
    if (v_stack_m1E8 == 0) goto loc_0025BCA6;
    v_stack_m1E8 = *(uint64_t *)(v_stack_m1E8);
loc_0025BC5C:
    if (v_stack_m1E8 == 0) goto loc_0025BCA6;
    Arg4 = 0;
    result = KiDeferredReadySingleThread(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28), v_stack_m1E8 - 216, v_stack_m1E8, Arg4);
    local_r15 = (uint32_t)((0) + 1);
    v_stack_m1CC = (uint32_t)(local_r15);
    if (v_stack_m1E8 != 0) {
        result = *(uint64_t *)(v_stack_m1E8);
        v_stack_m1E8 = result;
    }
    if ((((uint8_t)(local_r15)) & (15)) == 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 13784;
        result = KiFlushSoftwareInterruptBatch(Arg1, v_stack_m1E8 - 216, v_stack_m1E8, Arg4);
    }
    goto loc_0025BC5C;
loc_0025BCA6:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x35D9)) == 0) goto loc_0025BDD2;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x35D9))) == 1) goto loc_0025BCF4;
    result = KiSendSoftwareInterruptAffinity(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 13792, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x35D8), v_stack_m1E8, Arg4);
loc_0025BCCE:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x35D9)) == 2) goto loc_0025BD6A;
loc_0025BCDC:
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x35D9) = 0;
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x35DC) = 0xFFFFULL;
    goto loc_0025BDD2;
loc_0025BCF4:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8ED4))) + 1);
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8ED4) = (uint32_t)(result);
    result = 0;
    v_stack_mC4 = 0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = 0;
    v_stack_mC8 = 6;
    v_stack_mC0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x35DC)));
    Arg2 = 31;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x35D8))) != 1) { Arg2 = 47; }
    result = HalpInterruptSendIpi(v_stack_mC8, Arg2, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x35D8), Arg4);
    goto loc_0025BCCE;
loc_0025BD6A:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 0x35E0) = 0x200001ULL;
    Arg2 = 0;
    result = memset(*(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28) + 13800, Arg2, 256, Arg4);
    goto loc_0025BCDC;
loc_0025BD8E:
    if (result != (v_rip - 212389)) goto loc_0025BDB7;
    result = KiSwapDirectoryTableBaseTarget(local_r15, v_stack_m1B0, *(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28), v_stack_m180);
    goto loc_0025BDD2;
loc_0025BDB7:
    if (result != (v_rip + 508082)) goto loc_0025BDCD;
    result = PpmPerfAction(local_r15, v_stack_m1B0, *(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28), v_stack_m180);
    goto loc_0025BDD2;
loc_0025BDCD:
    result = guard_dispatch_icall(local_r15, v_stack_m1B0, *(uint64_t *)(*(uint64_t *)(Arg3) - 0x8 + 0x28), v_stack_m180);
loc_0025BDD2:
    goto loc_0025BE4F;
loc_0025BE4F:
    Arg2 = (v_stack_m1B0) << (32);
    result = (result) | (Arg2);
    if ((uint32_t)((uint32_t)(v_stack_m1F8)) != 0) goto loc_0025C02A;
    *(uint8_t *)(v_stack_m200 + 0x38BA) = (uint8_t)((uint32_t)(v_stack_m1F8));
    if (*(uint64_t *)(v_stack_m200 + 0x8318) == 0) goto loc_0025C10E;
    *(uint64_t *)(*(uint64_t *)(v_stack_m200 + 0x8318) + (uint32_t)(*(uint32_t *)(v_stack_m200 + 0x8320)) + (uint32_t)(*(uint32_t *)(v_stack_m200 + 0x8320)) * 2 * 8) = v_stack_m1F0;
    *(uint64_t *)(*(uint64_t *)(v_stack_m200 + 0x8318) + (uint32_t)(*(uint32_t *)(v_stack_m200 + 0x8320)) + (uint32_t)(*(uint32_t *)(v_stack_m200 + 0x8320)) * 2 * 8 + 0x8) = v_stack_m1A8;
    *(uint64_t *)(*(uint64_t *)(v_stack_m200 + 0x8318) + (uint32_t)(*(uint32_t *)(v_stack_m200 + 0x8320)) + (uint32_t)(*(uint32_t *)(v_stack_m200 + 0x8320)) * 2 * 8 + 0x10) = result;
    if ((*(uint32_t *)(v_stack_m200 + 0x8320)) >= 32) {
        *(uint32_t *)(v_stack_m200 + 0x8320) = 0;
    }
    Arg3 = (result) - (v_stack_m1A8);
    if (*(uint64_t *)(v_stack_m200 + 0x3810) == 0) goto loc_0025C00C;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m200 + 0x3810) + 0x4))))) & (31));
    local_r14 = (-1) << ((uint8_t)(Arg1));
    Arg4 = (local_r14) & (v_stack_m1F0);
    local_r15 = (Arg4) >> (56);
    local_r12 = (Arg4) >> (48);
    result = (Arg4) >> (40);
    v_stack_m1B0 = result;
    result = (Arg4) >> (32);
    v_stack_m1A8 = result;
    result = (Arg4) >> (24);
    v_stack_m160 = result;
    result = (Arg4) >> (16);
    v_stack_m158 = result;
    Arg2 = (Arg4) >> (8);
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m200 + 0x3810) + 0x4))) >> (5));
    if ((uint32_t)(local_r11) == 0) goto loc_0025C731;
    v_stack_mA0 = Arg4;
    result = ((uint8_t)(Arg4)) + (0xB15DCBULL);
    Arg1 = (Arg1) * (result);
    Arg1 = (Arg1) + ((uint8_t)(Arg2));
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m158);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_m160);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + (v_stack_m1A8);
    Arg1 = (Arg1) * (Arg2);
    Arg1 = (Arg1) + (v_stack_m1B0);
    Arg2 = (Arg2) * (Arg1);
    Arg2 = (Arg2) + ((uint8_t)(local_r12));
    result = ((uint8_t)(local_r12)) * (Arg2);
    result = (result) + (local_r15);
    Arg2 = (local_r11 - 1) & ((uint32_t)((uint32_t)(result)));
loc_0025BFC9:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m200 + 0x3810) + 0x8) + Arg2 * 8))) & (1)) != 0) goto loc_0025C731;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m200 + 0x3810) + 0x8) + Arg2 * 8) + 0x8)) & (local_r14);
    if (Arg4 != result) goto loc_0025BFC9;
    Arg1 = (Arg3 + Arg3 * 2) >> (2);
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m200 + 0x3810) + 0x8) + Arg2 * 8) + 0x10)) >> (2);
    Arg1 = (Arg1) + (result);
    *(void **)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m200 + 0x3810) + 0x8) + Arg2 * 8) + 0x10) = Arg1;
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m200 + 0x3810) + 0x8) + Arg2 * 8) + 0x18) = 1;
loc_0025BFFF:
loc_0025C00C:
    *(uint64_t *)(v_stack_m200 + 0x3820) = 0;
    *(uint64_t *)(v_stack_m200 + 0x3828) = -1;
    *(uint64_t *)(v_stack_m200 + 0x3830) = 0;
loc_0025C02A:
    local_rbx = result;
    if (v_stack_m1A0 != 1) {
        local_rbx = (result) - (*(uint64_t *)(v_stack_m1A0 + 0x20));
    }
    *(uint64_t *)(v_stack_m140 + 0x10) = *(uint64_t *)(result);
    if (((uint32_t)((uint32_t)(v_stack_m1F4))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B8 + 0x1E4))))) goto loc_0025C3F8;
    v_stack_m218 = (uint32_t)(*(uint32_t *)(v_stack_m1B8 + 0x1E4));
    result = KeBugCheckEx(199, 4, v_stack_m1F0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4))));
loc_0025C09A:
    if (((uint32_t)((uint32_t)(v_stack_m1F4))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1B8 + 0x1E4))))) goto loc_0025B8D6;
    result = KxWaitForSpinLockAndAcquire(local_rbx, 4, v_stack_m1F0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4))));
    goto loc_0025B8D1;
loc_0025C0B3:
    *(uint32_t *)(v_stack_m1F0 + 0x28) = 0;
    if ((*(uint32_t *)(local_r14)) != 0) goto loc_0025B8E0;
    result = KxReleaseSpinLock(local_rbx, 4, v_stack_m1F0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4))));
    goto loc_0025C524;
loc_0025C0ED:
    v_stack_m80 = 0;
    goto loc_0025BABB;
loc_0025C0FA:
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, 4, v_stack_m1F0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4))));
    v_stack_m90 = result;
    goto loc_0025BA90;
loc_0025C10E:
    goto loc_0025BEBE;
loc_0025C11B:
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x35D9)) != 0) goto loc_0025C2A2;
    *(uint8_t *)(arg1 + 0x35D9) = 1;
    *(uint32_t *)(arg1 + 0x35DC) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x24)));
loc_0025C13E:
    if (((*(uint8_t *)(v_stack_m1B8 + local_rbx * 8 + 0x33)) & (2)) != 0) goto loc_0025C3AE;
loc_0025C14A:
    if (((*(uint8_t *)(v_stack_m1B8 + local_rbx * 8 + 0x33)) & (4)) == 0) goto loc_0025C168;
    if (*(uint64_t *)(local_r14 + 0x8EB8) != 0) goto loc_0025C2F3;
loc_0025C168:
    result = *(uint64_t *)(local_r14 + 0x8EB8);
    if (((*(uint8_t *)(v_stack_m1B8 + local_rbx * 8 + 0x33)) & (1)) != 0) {
        result = *(uint64_t *)(v_stack_m1B8 + local_rbx * 8 + 0x28);
    }
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((uint32_t)(local_rsi)) < ((uint32_t)(*(uint8_t *)(v_stack_m1B8)))) goto loc_0025C270;
loc_0025C193:
    result = KiFlushSoftwareInterruptBatch(v_stack_m200 + 13784, 4, v_stack_m1F0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4))));
    local_rsi = 0;
loc_0025C1A6:
    if (v_stack_m198 != 0) {
        Arg2 = v_stack_m198;
        Arg1 = v_stack_m200;
        result = KiReadyDeferredReadyList(Arg1, Arg2, v_stack_m1F0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4))));
    }
    result = (v_stack_m168 != 0) ? 1 : 0;
    if ((uint8_t)(result) == 0) goto loc_0025C223;
    Arg1 = (v_stack_m168) & (-2);
    v_stack_mE0 = Arg1;
    local_rbx = (uint32_t)((v_stack_m168) & (1));
    if (condition_is_equal) goto loc_0025C392;
    if (((uint32_t)(local_rbx)) == 1) {
        local_rsi = *(uint64_t *)(arg1 + 0x8E58);
        local_rsi = (local_rsi) + (8);
        result = *(uint64_t *)(arg1 + 0x8E58);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0025C223;
loc_0025C210:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0025C210;
loc_0025C223:
loc_0025C224:
loc_0025C226:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)((uint32_t)(Arg2 - 1)), v_stack_m1F0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4))));
    local_rsp = (local_rsp) + (512);
    return result;
loc_0025C24A:
    v_stack_pD0 = local_rsi;
    if ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4)))) == 0) goto loc_0025C7C2;
    if ((*(uint8_t *)(v_stack_m1B8)) <= 0) goto loc_0025C193;
loc_0025C270:
    if ((((uint8_t)(*(uint8_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x33))) & (16)) != 0) goto loc_0025C11B;
    if ((((uint8_t)(*(uint8_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x33))) & (8)) == 0) goto loc_0025C13E;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x10) + 0x7)) != 0) goto loc_0025C11B;
    goto loc_0025C13E;
loc_0025C2A2:
    if (((uint8_t)(*(uint8_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x33))) != 1) goto loc_0025C2EA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x35DC)))) == (*(uint32_t *)(*(uint64_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x10) + 0x24))) goto loc_0025C13E;
    *(uint8_t *)(arg1 + 0x35D9) = 2;
    result = KeAddProcessorAffinityEx(Arg1 + 13792, (uint32_t)(*(uint32_t *)(arg1 + 0x35DC)), v_stack_m1F0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4))));
loc_0025C2CE:
    result = KeAddGroupAffinityEx(Arg1 + 13792, *(uint8_t *)(*(uint64_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x10) + 0xD0), *(uint64_t *)(*(uint64_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x10) + 0xC8), (uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4))));
    goto loc_0025C13E;
loc_0025C2EA:
    goto loc_0025C2CE;
loc_0025C2F3:
    if ((*(uint64_t *)(v_stack_p38 + 0x8EB8)) == 0) goto loc_0025C168;
    if (v_stack_p38 == (*(uint64_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x10))) goto loc_0025C168;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))) & (0x40000ULL));
    if (condition_is_below) goto loc_0025C331;
    if ((uint32_t)(result) == 0) goto loc_0025C168;
    if (((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(result))))) >= ((uint32_t)(Arg1 + 13792))) goto loc_0025C168;
loc_0025C331:
    *(uint32_t *)(*(uint64_t *)(v_stack_p38 + 0x8EB8) + 0xC) = (uint32_t)(v_stack_m200);
    result = (uint8_t)((uint32_t)(*(uint32_t *)(result)));
    local_r12 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x10) + 0x24));
    if ((*(uint8_t *)(v_rip + 0xD68CC1)) == 0) {
        result = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x10) + 0x24)));
        Arg2 = v_rip + 14094094;
        local_r12 = *(uint8_t *)(Arg2 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x10) + 0x24)) * 2);
        local_r12 = (uint32_t)((local_r12) << (6));
        result = *(uint8_t *)(Arg2 + result * 2 + 0x1);
        local_r12 = (uint32_t)((local_r12) | ((uint32_t)(result)));
    }
    *(uint32_t *)(*(uint64_t *)(v_stack_p38 + 0x8EB8) + 0x8) = (uint32_t)(local_r12);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xD6A7A7));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD6A7A7)))) & (32)) != 0) {
        Arg2 = (uint32_t)(v_stack_m200);
        Arg1 = *(uint32_t *)(*(uint64_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x10) + 0x24);
        result = EtwTraceXSchedulerPriorityKickSend(Arg1, Arg2, v_stack_p38, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4))));
    }
    Arg2 = ((uint32_t)((uint32_t)(local_r12))) >> (32);
    goto loc_0025C168;
loc_0025C392:
    goto loc_0025C1FF;
loc_0025C3A4:
    goto loc_0025BA7F;
loc_0025C3AE:
    Arg3 = 0;
    result = EtwTraceScheduleThread(*(uint64_t *)(v_stack_m1B8 + 0x1E * 8 + 0x28), *(uint64_t *)(v_stack_m1B8 + (uint32_t)((uint32_t)(local_rsi)) + (uint32_t)((uint32_t)(local_rsi)) * 4 * 8 + 0x10), Arg3, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4))));
    goto loc_0025C14A;
loc_0025C3C3:
    v_stack_pC0 = v_stack_p158;
    goto loc_0025B849;
loc_0025C3D0:
loc_0025C3D7:
    if (condition_is_not_equal) goto loc_0025C3D7;
    if (condition_is_above_or_equal) goto loc_0025B970;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(v_stack_m1B8 + 0x1E * 8 + 0x28), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))), Arg3, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1F4))));
    goto loc_0025B970;
loc_0025C3F8:
    result = (int8_t)(*(uint8_t *)(v_stack_m1B8 + 0x232));
    if (v_stack_p31 != ((uint8_t)((int8_t)(*(uint8_t *)(v_stack_m1B8 + 0x232))))) {
        Arg3 = (int8_t)(*(uint8_t *)(v_stack_m1B8 + 0x232));
        v_stack_p20 = v_stack_p158;
        Arg4 = 4;
        Arg2 = v_stack_p48;
        Arg1 = 505;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(v_stack_m200 + 0x8EB8) != 0) goto loc_0025C967;
loc_0025C434:
    if (v_stack_pC0 == 0) goto loc_0025C505;
    v_stack_p1E8 = v_stack_p48;
    v_stack_p1F0 = 8;
    v_stack_p74 = (uint32_t)(Arg1);
    if (v_stack_pC0 == 0) goto loc_0025C4FD;
loc_0025C480:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xD6A63B) + 0x11A8))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xD6A63B) + 0x11A8)) - 1)));
    result = ((uint32_t)((uint32_t)(Arg1))) << (5);
    result = (result) + (0x11CCULL);
    result = (result) + (*(uint64_t *)(v_rip + 0xD6A613));
    if (condition_is_equal) goto loc_0025C4EF;
    result = (uint32_t)(*(uint32_t *)(result + 0x4));
    if (sign_flag) {
        result = *(uint8_t *)(*(uint64_t *)(v_rip + 0xD6A613) + arg1 * 2 + 0x1199);
        Arg1 = local_rsp + result * 8 + 416;
        v_stack_p1D8 = Arg1;
        v_stack_p1E0 = 8;
        Arg3 = *(uint8_t *)(*(uint64_t *)(v_rip + 0xD6A613) + (uint32_t)((uint32_t)(arg1)) * 2 + 0x1198);
        v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_pC0 + 0x4)));
        v_stack_p20 = (uint16_t)(*(uint16_t *)(v_stack_pC0));
        Arg4 = (uint32_t)(v_stack_m200);
        Arg1 = v_stack_p1D8;
        result = EtwpLogKernelEvent(Arg1, *(uint64_t *)(v_rip + 0xD6A613), Arg3, Arg4);
    }
    if ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x4))) != 0) goto loc_0025C480;
    v_stack_p74 = (uint32_t)(Arg1);
loc_0025C4FD:
loc_0025C505:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p60 + 0x18))) != 0) goto loc_0025B86B;
loc_0025C524:
    *(uint64_t *)(v_stack_p38 + 0x2D90) = v_stack_pE8;
    if (((*(uint32_t *)(v_stack_p38 + 0xEC)) & (0x800ULL)) == 0) goto loc_0025C224;
    if (v_stack_p80 == (*(uint64_t *)(v_stack_p38 + 0x3838))) goto loc_0025C224;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0025C743;
loc_0025C56A:
    v_stack_p190 = v_stack_p38;
    local_rbx = (v_stack_p38) | (1);
    v_stack_pE8 = local_rbx;
    v_stack_pD0 = local_rbx;
    Arg1 = (*(uint64_t *)(v_stack_p38 + 0x8E58)) + (8);
    result = KiAcquireMultiplePrcbLocks(Arg1, *(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x8E58)), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), (uint32_t)(v_stack_p40));
    if (*(uint64_t *)(v_stack_p38 + 0x3838) == 0) goto loc_0025C1C1;
    if ((*(uint64_t *)(v_stack_p38 + 0x10)) != (*(uint64_t *)(v_stack_p38 + 0x3838))) goto loc_0025C1C1;
    v_stack_pA0 = v_stack_p158;
    Arg2 = 0;
    result = memset(*(uint64_t *)(v_stack_p38 + 0x37E8), Arg2, 240, (uint32_t)(v_stack_p40));
    Arg3 = 0;
    result = KiStartRescheduleContext(*(uint64_t *)(v_stack_p38 + 0x37E8), v_stack_pD0, Arg3, (uint32_t)(v_stack_p40));
    v_stack_p58 = *(uint64_t *)(v_stack_p38 + 0x3838);
    v_stack_pC8 = v_stack_p158;
    if (condition_is_below) goto loc_0025C979;
    if ((*(uint64_t *)(v_stack_p38 + 0x8)) == (*(uint64_t *)(v_stack_p38 + 0x8E80))) goto loc_0025C979;
    result = KiFindRescheduleContextEntryForPrcb(*(uint64_t *)(v_stack_p38 + 0x37E8), v_stack_p38, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p38 + 0x8) + 0x78)), (uint32_t)(v_stack_p40));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p58 + 0x78))) & (2));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p38 + 0x8) + 0x78))) & (2));
    if (((uint8_t)(Arg3)) > ((uint8_t)(Arg1))) goto loc_0025CA9C;
loc_0025C655:
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(result) + 0x8);
    Arg2 = ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) == (*(uint64_t *)(*(uint64_t *)(result) + 0x18))) ? 1 : 0;
    result = (uint8_t)((*(uint8_t *)(result + 0x20)) & (254));
    Arg2 = (uint8_t)((Arg2) | ((uint8_t)(result)));
    *(uint8_t *)(result + 0x20) = (uint8_t)(Arg2);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result) + 0x8) + 0x78))) >> (1));
    result = (uint8_t)((result) & (1));
    result = (uint8_t)((result) + ((uint8_t)(result)));
    Arg2 = (uint8_t)((Arg2) & (253));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg2)));
    result = (uint8_t)((result) & (199));
    result = (uint8_t)((result) | (4));
    *(uint8_t *)(result + 0x20) = (uint8_t)(result);
    *(uint64_t *)(result + 0x18) = v_stack_p158;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p38 + 0x8) + 0x78))) | (*(uint32_t *)(v_stack_p58 + 0x78)));
    if ((((uint8_t)(Arg1)) & (2)) == 0) goto loc_0025CA89;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8))) <= 0) goto loc_0025CA89;
loc_0025C6B7:
    Arg4 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p158)))) * 4 + 2) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p158)))));
    if (result == (*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg4 * 8)) goto loc_0025CA79;
    v_stack_pC8 = v_stack_p158;
    v_stack_p58 = *(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + arg4 * 8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p38 + 0x8) + 0x78)))) & (2)) != 0) goto loc_0025CA0C;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + arg4 * 8 + 0x18) - 1) <= -4) goto loc_0025CB50;
loc_0025C705:
    *(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + arg4 * 8 + 0x10) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + arg4 * 8) + 0x18);
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + arg4 * 8 + 0x20)) | (1));
    *(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + arg4 * 8 + 0x20) = (uint8_t)(result);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + arg4 * 8) + 0x18) + 0x78))) >> (1));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (253));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (231));
    Arg1 = (uint8_t)((Arg1) | (4));
    Arg1 = (uint8_t)((Arg1) & (223));
    goto loc_0025CA56;
loc_0025C731:
    result = KiInsertNewDpcRuntime(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + arg4 * 8) + 0x18), v_stack_p48, Arg3, *(uint64_t *)(v_stack_p38 + 0x37E8) + Arg4 * 8);
    goto loc_0025BFFF;
loc_0025C743:
loc_0025C74A:
    if (condition_is_not_equal) goto loc_0025C74A;
    if (condition_is_above_or_equal) goto loc_0025C56A;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + arg4 * 8) + 0x18), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))), Arg3, *(uint64_t *)(v_stack_p38 + 0x37E8) + Arg4 * 8);
    goto loc_0025C56A;
loc_0025C770:
    goto loc_0025B892;
loc_0025C777:
    result = KiEnterLongDpcProcessing(v_stack_p38, *(uint64_t *)(v_stack_p38 + 0x37E8), Arg3, *(uint64_t *)(v_stack_p38 + 0x37E8) + Arg4 * 8);
    if ((uint8_t)(result) == 0) goto loc_0025C7CC;
    result = 0;
    goto loc_0025C226;
loc_0025C78D:
    result = RtlGetSystemTimePrecise(v_stack_p38, *(uint64_t *)(v_stack_p38 + 0x37E8), Arg3, *(uint64_t *)(v_stack_p38 + 0x37E8) + Arg4 * 8);
    v_stack_p1B0 = result;
    goto loc_0025BAA1;
loc_0025C79F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCB16B3))) != 0) goto loc_0025B952;
    result = KiReleaseSpinLockInstrumented(1, v_stack_p238, Arg3, *(uint64_t *)(v_stack_p38 + 0x37E8) + Arg4 * 8);
    goto loc_0025B957;
loc_0025C7C2:
    goto loc_0025C1A6;
loc_0025C7CC:
    goto loc_0025B8AA;
loc_0025C7D6:
    if (1 == 0) goto loc_0025B8AA;
    result = EtwTraceLongDpcDetectionEvent(1, v_stack_p238, v_stack_p60, *(uint64_t *)(v_stack_p38 + 0x37E8) + Arg4 * 8);
    goto loc_0025B8A2;
loc_0025C7F2:
    result = EtwpGetHostPerfCounter(1, v_stack_p238, v_stack_p60, *(uint64_t *)(v_stack_p38 + 0x37E8) + Arg4 * 8);
    v_stack_p1C0 = result;
    goto loc_0025BACC;
loc_0025C804:
    result = KiFindRescheduleContextEntryForPrcb(*(uint64_t *)(v_stack_p38 + 0x37E8), v_stack_p38, v_stack_p60, *(uint64_t *)(v_stack_p38 + 0x37E8) + Arg4 * 8);
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(result + 0x20)))) >> (1));
    local_r10 = (uint32_t)((local_r10) & (1));
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (32)) == 0) {
    }
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    Arg1 = (uint8_t)((*(uint8_t *)(result + 0x20)) & (197));
    Arg1 = (uint8_t)((Arg1) | (5));
    *(uint8_t *)(result + 0x20) = (uint8_t)(Arg1);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    if ((uint32_t)(local_r10) != 0) goto loc_0025CAE6;
loc_0025C85A:
    result = KiSearchForNewThreadsForRescheduleContext(*(uint64_t *)(v_stack_p38 + 0x37E8), v_stack_pA0, result, *(uint64_t *)(result));
    Arg4 = 0;
    local_r12 = (uint32_t)((uint32_t)(v_stack_p158));
    if (((*(uint32_t *)(v_rip + 0xD6A29D)) & (0x400ULL)) != 0) { local_r12 = (uint32_t)(v_stack_p38); }
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8))) <= 0) goto loc_0025C8D7;
    local_rbx = 0;
loc_0025C88D:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p158)))) * 4 + 2) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p158)))));
    result = KiCommitRescheduleContextEntry(*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg1 * 8, v_stack_p38, (uint32_t)((uint32_t)(local_r12)), v_stack_pA0);
    local_rbx = (uint8_t)((local_rbx) | ((uint8_t)(result)));
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p158))) + 1);
    if (((uint32_t)(local_r14)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8))))) goto loc_0025C88D;
    v_stack_p30 = (uint8_t)(local_rbx);
loc_0025C8D7:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + 0x8)) != 1) goto loc_0025C8FA;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + 0x10) + 0x8E58) + 0x1)) + 1);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = (uint8_t)(result);
    if (((uint8_t)(result)) >= (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + 0x10) + 0x8E58)))) {
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + 0x10) + 0x8E58) + 0x1) = 0;
    }
    Arg1 = (v_stack_pE8) & (-2);
    v_stack_p150 = Arg1;
    local_rbx = (uint32_t)((v_stack_pE8) & (1));
    if (condition_is_equal) goto loc_0025C958;
    if (((uint32_t)(local_rbx)) == 1) {
        Arg3 = *(uint64_t *)(arg1 + 0x8E58);
        Arg3 = (Arg3) + (8);
        result = *(uint64_t *)(arg1 + 0x8E58);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0025C24A;
loc_0025C940:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0025C940;
    goto loc_0025C24A;
loc_0025C958:
    goto loc_0025C92D;
loc_0025C967:
    if ((uint32_t)(v_stack_p150) != 0) goto loc_0025C434;
    goto loc_0025C434;
loc_0025C979:
    result = KiFindRescheduleContextEntryForPrcb(*(uint64_t *)(v_stack_p38 + 0x37E8), local_r14, v_stack_p150, v_stack_p30);
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(result + 0x20)))) >> (1));
    local_r11 = (uint32_t)((local_r11) & (1));
    if ((((uint8_t)(*(uint8_t *)(result + 0x20))) & (32)) == 0) {
    }
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    Arg1 = (uint8_t)((*(uint8_t *)(result + 0x20)) & (197));
    Arg1 = (uint8_t)((Arg1) | (5));
    *(uint8_t *)(result + 0x20) = (uint8_t)(Arg1);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(*(uint64_t *)(result) + 0x18);
    if ((uint32_t)(local_r11) == 0) goto loc_0025C85A;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8))) <= 0) goto loc_0025CA04;
loc_0025C9D6:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p158)))) * 4 + 2) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p158)))));
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p158))));
    if ((*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg1 * 8) != result) {
        Arg4 = 0;
        Arg3 = 1;
        result = KiAdjustRescheduleContextEntryForThreadRemoval(*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg1 * 8, local_r14, Arg3, Arg4);
    }
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p158))) + 1);
    if (((uint32_t)(local_r14)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8))))) goto loc_0025C9D6;
loc_0025CA04:
    goto loc_0025CAF6;
loc_0025CA0C:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8))) <= -4) goto loc_0025CB17;
loc_0025CA1D:
    *(uint64_t *)(arg4 + 0x10) = local_r12;
    result = (uint8_t)((*(uint8_t *)(arg4 + 0x20)) & (254));
    *(uint8_t *)(arg4 + 0x20) = (uint8_t)(result);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r12 + 0x78))) >> (1));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (253));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (231));
    Arg1 = (uint8_t)((Arg1) | (4));
    result = (uint8_t)(((uint8_t)(Arg1)) & (223));
    Arg1 = (uint8_t)((Arg1) | (32));
    Arg1 = (uint8_t)(Arg1);
    if (local_r12 == (*(uint64_t *)(local_r14 + 0x8E80))) { Arg1 = (uint32_t)((uint8_t)(result)); }
loc_0025CA56:
    *(uint8_t *)(arg4 + 0x20) = (uint8_t)(Arg1);
    *(uint64_t *)(arg4 + 0x18) = *(uint64_t *)(local_r14 + 0x8E80);
    result = KiIsPrcbThread(*(uint64_t *)(local_r14 + 0x8E80), local_r14, Arg3, Arg4);
    if ((uint8_t)(result) == 0) {
        result = *(uint32_t *)(local_r14 + 0x24);
        *(uint32_t *)(*(uint64_t *)(local_r14 + 0x8E80) + 0x218) = (uint32_t)(result);
    }
    local_r11 = (uint32_t)((local_r11) + 1);
    if (((uint32_t)(local_r11)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8))))) goto loc_0025C6B7;
loc_0025CA89:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r12 + 0x78))) >> (1));
    result = (uint32_t)((result) & (1));
    *(uint32_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + 0x4) = (uint32_t)(result);
    goto loc_0025C85A;
loc_0025CA9C:
loc_0025CA9E:
    v_stack_p44 = (uint32_t)((uint32_t)((uint32_t)(v_stack_p158)));
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_p158)))) >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8))))) goto loc_0025CADC;
    Arg1 = ((uint32_t)((uint32_t)(v_stack_p158)) * 4 + 2) + ((uint32_t)((uint32_t)(v_stack_p158)));
    if (local_r14 == (*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg1 * 8)) goto loc_0025CAD4;
    Arg4 = 0;
    result = KiDoesThreadDominateRescheduleContextEntry(*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg1 * 8, local_r12, 2, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0025C804;
loc_0025CAD4:
    result = (uint32_t)(((uint32_t)(v_stack_p44)) + 1);
    goto loc_0025CA9E;
loc_0025CADC:
    goto loc_0025C655;
loc_0025CAE6:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8))) > 0) goto loc_0025CB90;
loc_0025CAF3:
loc_0025CAF6:
    if ((uint32_t)(*(uint64_t *)(local_r14 + 0x8E80)) == 0) goto loc_0025C85A;
    *(uint32_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + 0x4) = (uint32_t)(v_stack_p158);
    goto loc_0025C85A;
loc_0025CB05:
    v_stack_p7C = 0x501802ULL;
    goto loc_0025B837;
loc_0025CB17:
    result = KiIsPrcbThread(*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg1 * 8, local_r12, 2, v_stack_p58);
    if ((uint8_t)(result) != 0) goto loc_0025CA1D;
    if (((*(uint8_t *)(v_stack_p58 + 0x21)) & (1)) != 0) {
    }
    *(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + arg1 * 8 + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_pC8, *(uint64_t *)(v_stack_p38 + 0x37E8) + Arg1 * 8, 2, v_stack_p58);
    goto loc_0025CA1D;
loc_0025CB50:
    result = KiIsPrcbThread(v_stack_pC8, v_stack_p58, 2, v_stack_p58);
    if ((uint8_t)(result) != 0) goto loc_0025C705;
    if (((*(uint8_t *)(v_stack_p58 + 0x21)) & (1)) != 0) {
    }
    *(uint8_t *)(v_stack_pC8 + 0x235) = 1;
    result = KiInsertDeferredReadyList(v_stack_pC8, v_stack_pC8, 2, v_stack_p58);
    goto loc_0025C705;
loc_0025CB90:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p158)))) * 4 + 2) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p158)))));
    if ((*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg2 * 8) == 2) goto loc_0025CBDD;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg2 * 8 + 0x20))) & (32)) == 0) {
    }
    *(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg2 * 8 + 0x10) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg2 * 8) + 0x18);
    Arg4 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg2 * 8 + 0x20)) & (197));
    Arg4 = (uint8_t)((Arg4) | (5));
    *(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg2 * 8 + 0x20) = (uint8_t)(Arg4);
    *(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg2 * 8 + 0x18) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8) + Arg2 * 8) + 0x18);
loc_0025CBDD:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p158))) + 1);
    if (((uint32_t)(local_r11)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x37E8))))) goto loc_0025CB90;
    goto loc_0025CAF3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x2D90` | `64` | `R` |
| `Arg1` | `+ 0x35D9` | `8` | `R` |
| `Arg1` | `+ 0x35D9` | `8` | `W` |
| `Arg1` | `+ 0x35DC` | `32` | `R` |
| `Arg1` | `+ 0x35DC` | `32` | `W` |
| `Arg1` | `+ 0x35E0` | `64` | `R` |
| `Arg4` | `+ 0x0 + r8*2` | `64` | `R` |
| `Arg4` | `+ 0x12C` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0025B740&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
