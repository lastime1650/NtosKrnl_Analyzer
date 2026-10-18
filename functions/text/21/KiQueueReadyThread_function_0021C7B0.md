# KiQueueReadyThread

- RVA: `0x0021C7B0`–`0x0021D34F` (길이 `2,975` bytes)
- VA: `0x000000014021C7B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005EF6C`
- 디코드: `711`개 명령, `2,975/2,975` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **43**; 고유 호출 대상: **36**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x0021C862` → [KiComputeGroupSchedulingRank](KiComputeGroupSchedulingRank_function_0021EB84.md) (function, `0x0021EB84`)
- `0x0021C8CC` → [KiCheckForMaxOverQuotaScb](../20/KiCheckForMaxOverQuotaScb_function_002027A0.md) (function, `0x002027A0`)
- `0x0021C91A` → [KiEnterDeferredReadyState](../39/KiEnterDeferredReadyState_function_00397420.md) (function, `0x00397420`)
- `0x0021C9A9` → [KiDeferredReadySingleThread](../25/KiDeferredReadySingleThread_function_00252FE0.md) (function, `0x00252FE0`)
- `0x0021C9D3` → [KiDeferredReadySingleThread](../25/KiDeferredReadySingleThread_function_00252FE0.md) (function, `0x00252FE0`)
- `0x0021C9FB` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x0021CA08` → [KiFlushSoftwareInterruptBatch](../25/KiFlushSoftwareInterruptBatch_function_00252200.md) (function, `0x00252200`)
- `0x0021CAB5` → [KiUpdateVpBackingThreadPriorityOnReadyQueueInsertion](KiUpdateVpBackingThreadPriorityOnReadyQueueInsertion_function_0021D360.md) (function, `0x0021D360`)
- `0x0021CBDB` → [KiUpdateSoftParkElectionStatisticsOnInsertion](KiUpdateSoftParkElectionStatisticsOnInsertion_function_00218F40.md) (function, `0x00218F40`)
- `0x0021CBE0` → [KeIsForceParkingEnabled](KeIsForceParkingEnabled_function_00218F20.md) (function, `0x00218F20`)
- `0x0021CC4B` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x0021CC57` → [KiCheckForMaxOverQuotaScb](../20/KiCheckForMaxOverQuotaScb_function_002027A0.md) (function, `0x002027A0`)
- `0x0021CC95` → [KiAddThreadToScbQueue](../20/KiAddThreadToScbQueue_function_002010DC.md) (function, `0x002010DC`)
- `0x0021CD0C` → [KxWaitForLockChainValid](KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0021CD29` → [KeWakeAddressAll](KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0021CDF2` → [KiIsThreadConstrainedBySchedulingGroup](../30/KiIsThreadConstrainedBySchedulingGroup_function_0030B200.md) (function, `0x0030B200`)
- `0x0021CE03` → [KiShouldPreemptionBeDeferred](../35/KiShouldPreemptionBeDeferred_function_00356310.md) (function, `0x00356310`)
- `0x0021CE88` → [KiUpdateLocalReadyQueueStatisticsOnInsertion](../4A/KiUpdateLocalReadyQueueStatisticsOnInsertion_function_004A9290.md) (function, `0x004A9290`)
- `0x0021CECC` → [KiComputeNewPriority](../3C/KiComputeNewPriority_function_003C2D8C.md) (function, `0x003C2D8C`)
- `0x0021CEDB` → [KiUpdateVPBackingThreadPriority](../30/KiUpdateVPBackingThreadPriority_function_00306040.md) (function, `0x00306040`)
- `0x0021CEF1` → [KiUpdateThreadPriority](../25/KiUpdateThreadPriority_function_00257810.md) (function, `0x00257810`)
- `0x0021CEF9` → [KiQueryQuantumReset](KiQueryQuantumReset_function_0021F6B4.md) (function, `0x0021F6B4`)
- `0x0021CF20` → [KiTryScheduleNextForegroundBoost](../47/KiTryScheduleNextForegroundBoost_function_0047B51C.md) (function, `0x0047B51C`)
- `0x0021CF2E` → [KiCheckThreadAffinity](../25/KiCheckThreadAffinity_function_00256DD0.md) (function, `0x00256DD0`)
- `0x0021CF52` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x0021CF77` → [HalpDisableInterrupts](../25/HalpDisableInterrupts_function_002521A0.md) (function, `0x002521A0`)
- `0x0021CFD1` → [HalpInterruptSendIpi](../25/HalpInterruptSendIpi_function_00252310.md) (function, `0x00252310`)
- `0x0021CFE9` → [KiIsThreadExemptFromForcePark](../4D/KiIsThreadExemptFromForcePark_function_004D7B80.md) (function, `0x004D7B80`)
- `0x0021CFFC` → [KiArmForceParkDutyCyclingForSharedReadyQueue](../4F/KiArmForceParkDutyCyclingForSharedReadyQueue_function_004FB604.md) (function, `0x004FB604`)
- `0x0021D027` → [KiCheckMaxOverQuotaTransition](../35/KiCheckMaxOverQuotaTransition_function_00354884.md) (function, `0x00354884`)
- `0x0021D054` → [KiRecomputeGroupSchedulingRank](../45/KiRecomputeGroupSchedulingRank_function_00452FC8.md) (function, `0x00452FC8`)
- `0x0021D0C1` → [EtwTraceScbRankChange](../4F/EtwTraceScbRankChange_function_004F899C.md) (function, `0x004F899C`)
- `0x0021D12E` → [KiRemoveSchedulingGroupQueue](../20/KiRemoveSchedulingGroupQueue_function_00202638.md) (function, `0x00202638`)
- `0x0021D15E` → [KiComputeThreadAffinity](../39/KiComputeThreadAffinity_function_00399DE0.md) (function, `0x00399DE0`)
- `0x0021D175` → [KiCheckPrcbAffinityEx](../43/KiCheckPrcbAffinityEx_function_004366A0.md) (function, `0x004366A0`)
- `0x0021D1BB` → [EtwTraceScbRankChange](../4F/EtwTraceScbRankChange_function_004F899C.md) (function, `0x004F899C`)
- `0x0021D223` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0021D232` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0021D246` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0021D251` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0021D2C3` → [EtwTraceReadyQueueInsertion](../22/EtwTraceReadyQueueInsertion_function_00223444.md) (function, `0x00223444`)
- `0x0021D323` → [EtwTraceThreadAffinity](../3C/EtwTraceThreadAffinity_function_003C29A0.md) (function, `0x003C29A0`)
- `0x0021D345` → [EtwTraceIdealProcessor](../3C/EtwTraceIdealProcessor_function_003C0808.md) (function, `0x003C0808`)

### Direct callers
- [KiHandleDeferredPreemption](../20/KiHandleDeferredPreemption_function_00202ECC.md) at `0x00203155`
- [KeYieldExecution](../20/KeYieldExecution_function_00209FA0.md) at `0x0020A1B1`
- [sub_0021B896](Unknown_function_0021B896.md) at `0x0021B93D`
- [sub_0021C5F2](Unknown_function_0021C5F2.md) at `0x0021C638`
- [KiCheckForThreadDispatch](../25/KiCheckForThreadDispatch_function_00250648.md) at `0x00250748`
- [sub_00251E24](../25/Unknown_function_00251E24.md) at `0x00251E8D`

### Static image references
- `0x0021C7DD` → RVA `0x00FC6BF8` (`ALMOSTRO`; read)
- `0x0021C867` → RVA `0x00FC6B14` (`ALMOSTRO`; read)
- `0x0021C8AB` → RVA `0x00FC5380` (`ALMOSTRO`; read)
- `0x0021CB1E` → RVA `0x00FC6B38` (`ALMOSTRO`; read)
- `0x0021CEFE` → RVA `0x00FC5098` (`ALMOSTRO`; read)
- `0x0021CF61` → RVA `0x00FC6BC5` (`ALMOSTRO`; read)
- `0x0021D0DD` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0021D215` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0021D32D` → RVA `0x00FC6B10` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0021CB7A` → [sub_006D6928 + 0x15](../6D/Unknown_function_006D6928.md) (`tail-transfer`)
  - `0x0021D17C` → [sub_006D6928](../6D/Unknown_function_006D6928.md) (`tail-transfer`)
  - `0x0021D189` → [sub_006D6928](../6D/Unknown_function_006D6928.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0021C7B0  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0021C7B5  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0021C7BA  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0021C7BF  55                              push rbp
0021C7C0  53                              push rbx
0021C7C1  56                              push rsi
0021C7C2  57                              push rdi
0021C7C3  41 54                           push r12
0021C7C5  41 55                           push r13
0021C7C7  41 56                           push r14
0021C7C9  41 57                           push r15
0021C7CB  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
0021C7D0  48 81 EC 98 00 00 00            sub rsp, 0x98
0021C7D7  49 8B 58 48                     mov rbx, qword ptr [r8 + 0x48]
0021C7DB  33 F6                           xor esi, esi
0021C7DD  48 8B 05 14 A4 DA 00            mov rax, qword ptr [rip + 0xdaa414]
0021C7E4  4D 8B E8                        mov r13, r8
0021C7E7  4C 8B F2                        mov r14, rdx
0021C7EA  45 0F B6 A0 35 02 00 00         movzx r12d, byte ptr [r8 + 0x235]
0021C7F2  4C 8B F9                        mov r15, rcx
0021C7F5  C7 45 D7 FF FF FF FF            mov dword ptr [rbp - 0x29], 0xffffffff
0021C7FC  C7 45 D3 FF FF FF FF            mov dword ptr [rbp - 0x2d], 0xffffffff
0021C803  C6 45 CF 00                     mov byte ptr [rbp - 0x31], 0
0021C807  48 89 75 DF                     mov qword ptr [rbp - 0x21], rsi
0021C80B  44 89 65 7F                     mov dword ptr [rbp + 0x7f], r12d
0021C80F  49 39 80 38 02 00 00            cmp qword ptr [r8 + 0x238], rax
0021C816  0F 85 79 06 00 00               jne 0x14021ce95
0021C81C  49 3B 58 20                     cmp rbx, qword ptr [r8 + 0x20]
0021C820  0F 83 7B 06 00 00               jae 0x14021cea1
0021C826  49 8B 7D 68                     mov rdi, qword ptr [r13 + 0x68]
0021C82A  48 85 FF                        test rdi, rdi
0021C82D  74 72                           je 0x14021c8a1
0021C82F  41 8B 9F D8 00 00 00            mov ebx, dword ptr [r15 + 0xd8]
0021C836  4C 8B E6                        mov r12, rsi
0021C839  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
0021C83D  48 03 DF                        add rbx, rdi
0021C840  0F B7 43 70                     movzx eax, word ptr [rbx + 0x70]
0021C844  44 8B 7B 7C                     mov r15d, dword ptr [rbx + 0x7c]
0021C848  44 0F B7 F0                     movzx r14d, ax
0021C84C  66 41 83 E6 02                  and r14w, 2
0021C851  A8 04                           test al, 4
0021C853  0F 85 C8 07 00 00               jne 0x14021d021
0021C859  4C 8B CB                        mov r9, rbx
0021C85C  49 8B D5                        mov rdx, r13
0021C85F  48 8B CF                        mov rcx, rdi
0021C862  E8 1D 23 00 00                  call 0x14021eb84
0021C867  F7 05 A3 A2 DA 00 00 40 00 00   test dword ptr [rip + 0xdaa2a3], 0x4000
0021C871  0F 85 C1 08 00 00               jne 0x14021d138
0021C877  03 73 7C                        add esi, dword ptr [rbx + 0x7c]
0021C87A  48 8B 9B A0 01 00 00            mov rbx, qword ptr [rbx + 0x1a0]
0021C881  48 85 DB                        test rbx, rbx
0021C884  0F 84 5D 05 00 00               je 0x14021cde7
0021C88A  41 8B 85 D8 00 00 00            mov eax, dword ptr [r13 + 0xd8]
0021C891  48 8B FB                        mov rdi, rbx
0021C894  48 2B F8                        sub rdi, rax
0021C897  EB A7                           jmp 0x14021c840
0021C899  4C 8B 7D 67                     mov r15, qword ptr [rbp + 0x67]
0021C89D  4C 8B 75 6F                     mov r14, qword ptr [rbp + 0x6f]
0021C8A1  41 0F BE 85 C3 00 00 00         movsx eax, byte ptr [r13 + 0xc3]
0021C8A9  33 FF                           xor edi, edi
0021C8AB  3B 05 CF 8A DA 00               cmp eax, dword ptr [rip + 0xda8acf]
0021C8B1  8B D7                           mov edx, edi
0021C8B3  0F 8C 50 03 00 00               jl 0x14021cc09
0021C8B9  49 8B 45 68                     mov rax, qword ptr [r13 + 0x68]
0021C8BD  48 85 C0                        test rax, rax
0021C8C0  74 13                           je 0x14021c8d5
0021C8C2  41 8B 8F D8 00 00 00            mov ecx, dword ptr [r15 + 0xd8]
0021C8C9  48 03 C8                        add rcx, rax
0021C8CC  E8 CF 5E FE FF                  call 0x1402027a0
0021C8D1  84 C0                           test al, al
0021C8D3  75 2B                           jne 0x14021c900
0021C8D5  49 8B 87 C0 00 00 00            mov rax, qword ptr [r15 + 0xc0]
0021C8DC  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
0021C8E0  49 8B 8D 40 02 00 00            mov rcx, qword ptr [r13 + 0x240]
0021C8E7  41 0F B6 87 D0 00 00 00         movzx eax, byte ptr [r15 + 0xd0]
0021C8EF  66 3B 01                        cmp ax, word ptr [rcx]
0021C8F2  0F 83 8C 07 00 00               jae 0x14021d084
0021C8F8  4C 8B 44 C1 08                  mov r8, qword ptr [rcx + rax*8 + 8]
0021C8FD  49 23 D0                        and rdx, r8
0021C900  41 F7 45 78 00 10 00 00         test dword ptr [r13 + 0x78], 0x1000
0021C908  75 09                           jne 0x14021c913
0021C90A  48 85 D2                        test rdx, rdx
0021C90D  0F 84 2F 01 00 00               je 0x14021ca42
0021C913  49 8B 77 10                     mov rsi, qword ptr [r15 + 0x10]
0021C917  49 8B CD                        mov rcx, r13
0021C91A  E8 01 AB 17 00                  call 0x140397420
0021C91F  49 8B 0E                        mov rcx, qword ptr [r14]
0021C922  4C 8B C7                        mov r8, rdi
0021C925  4C 8B C9                        mov r9, rcx
0021C928  8B D7                           mov edx, edi
0021C92A  49 83 E1 FE                     and r9, 0xfffffffffffffffe
0021C92E  41 BE 01 00 00 00               mov r14d, 1
0021C934  4C 89 4D F7                     mov qword ptr [rbp - 9], r9
0021C938  83 E1 01                        and ecx, 1
0021C93B  0F 84 01 05 00 00               je 0x14021ce42
0021C941  41 3B CE                        cmp ecx, r14d
0021C944  75 15                           jne 0x14021c95b
0021C946  49 8B 81 58 8E 00 00            mov rax, qword ptr [r9 + 0x8e58]
0021C94D  4D 8B 81 58 8E 00 00            mov r8, qword ptr [r9 + 0x8e58]
0021C954  49 83 C0 08                     add r8, 8
0021C958  0F B6 10                        movzx edx, byte ptr [rax]
0021C95B  85 D2                           test edx, edx
0021C95D  74 13                           je 0x14021c972
0021C95F  90                              nop
0021C960  8D 42 FF                        lea eax, [rdx - 1]
0021C963  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
0021C967  8B D0                           mov edx, eax
0021C969  F0 48 21 79 30                  lock and qword ptr [rcx + 0x30], rdi
0021C96E  85 C0                           test eax, eax
0021C970  75 EE                           jne 0x14021c960
0021C972  48 8B 5D 6F                     mov rbx, qword ptr [rbp + 0x6f]
0021C976  33 C0                           xor eax, eax
0021C978  48 8B 7D DF                     mov rdi, qword ptr [rbp - 0x21]
0021C97C  48 89 03                        mov qword ptr [rbx], rax
0021C97F  48 85 FF                        test rdi, rdi
0021C982  0F 85 06 08 00 00               jne 0x14021d18e
0021C988  33 D2                           xor edx, edx
0021C98A  F0 41 0F BA 75 78 0C            lock btr dword ptr [r13 + 0x78], 0xc
0021C991  48 89 55 B7                     mov qword ptr [rbp - 0x49], rdx
0021C995  4C 8D 45 B7                     lea r8, [rbp - 0x49]
0021C999  49 8B D5                        mov rdx, r13
0021C99C  45 88 A5 35 02 00 00            mov byte ptr [r13 + 0x235], r12b
0021C9A3  45 33 C9                        xor r9d, r9d
0021C9A6  49 8B CF                        mov rcx, r15
0021C9A9  E8 32 66 03 00                  call 0x140252fe0
0021C9AE  48 8B 5D B7                     mov rbx, qword ptr [rbp - 0x49]
0021C9B2  48 85 DB                        test rbx, rbx
0021C9B5  0F 84 2F 09 00 00               je 0x14021d2ea
0021C9BB  48 8B 03                        mov rax, qword ptr [rbx]
0021C9BE  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0021C9C2  48 8D 93 28 FF FF FF            lea rdx, [rbx - 0xd8]
0021C9C9  45 33 C9                        xor r9d, r9d
0021C9CC  4C 8D 45 B7                     lea r8, [rbp - 0x49]
0021C9D0  49 8B CF                        mov rcx, r15
0021C9D3  E8 08 66 03 00                  call 0x140252fe0
0021C9D8  48 8B 5D B7                     mov rbx, qword ptr [rbp - 0x49]
0021C9DC  41 FF C6                        inc r14d
0021C9DF  48 85 DB                        test rbx, rbx
0021C9E2  74 07                           je 0x14021c9eb
0021C9E4  48 8B 03                        mov rax, qword ptr [rbx]
0021C9E7  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
0021C9EB  49 8D BF D8 35 00 00            lea rdi, [r15 + 0x35d8]
0021C9F2  41 F6 C6 0F                     test r14b, 0xf
0021C9F6  75 08                           jne 0x14021ca00
0021C9F8  48 8B CF                        mov rcx, rdi
0021C9FB  E8 00 58 03 00                  call 0x140252200
0021CA00  48 85 DB                        test rbx, rbx
0021CA03  75 BD                           jne 0x14021c9c2
0021CA05  48 8B CF                        mov rcx, rdi
0021CA08  E8 F3 57 03 00                  call 0x140252200
0021CA0D  48 85 F6                        test rsi, rsi
0021CA10  0F 85 98 03 00 00               jne 0x14021cdae
0021CA16  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
0021CA1A  49 39 47 08                     cmp qword ptr [r15 + 8], rax
0021CA1E  0F 84 8A 03 00 00               je 0x14021cdae
0021CA24  49 39 77 10                     cmp qword ptr [r15 + 0x10], rsi
0021CA28  0F 84 80 03 00 00               je 0x14021cdae
0021CA2E  41 38 77 20                     cmp byte ptr [r15 + 0x20], sil
0021CA32  0F 84 24 05 00 00               je 0x14021cf5c
0021CA38  41 C6 47 06 01                  mov byte ptr [r15 + 6], 1
0021CA3D  E9 6C 03 00 00                  jmp 0x14021cdae
0021CA42  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
0021CA4C  41 88 BD 35 02 00 00            mov byte ptr [r13 + 0x235], dil
0021CA53  8B 00                           mov eax, dword ptr [rax]
0021CA55  41 89 85 B4 01 00 00            mov dword ptr [r13 + 0x1b4], eax
0021CA5C  49 8B 45 68                     mov rax, qword ptr [r13 + 0x68]
0021CA60  48 85 C0                        test rax, rax
0021CA63  0F 84 D1 03 00 00               je 0x14021ce3a
0021CA69  41 8B 97 D8 00 00 00            mov edx, dword ptr [r15 + 0xd8]
0021CA70  48 03 D0                        add rdx, rax
0021CA73  49 8B 87 B8 8E 00 00            mov rax, qword ptr [r15 + 0x8eb8]
0021CA7A  48 85 C0                        test rax, rax
0021CA7D  74 04                           je 0x14021ca83
0021CA7F  40 88 78 10                     mov byte ptr [rax + 0x10], dil
0021CA83  32 DB                           xor bl, bl
0021CA85  41 C6 85 84 01 00 00 01         mov byte ptr [r13 + 0x184], 1
0021CA8D  41 BE 01 00 00 00               mov r14d, 1
0021CA93  48 85 D2                        test rdx, rdx
0021CA96  0F 85 7D 01 00 00               jne 0x14021cc19
0021CA9C  41 F7 45 78 00 00 40 00         test dword ptr [r13 + 0x78], 0x400000
0021CAA4  49 0F BE B5 C3 00 00 00         movsx rsi, byte ptr [r13 + 0xc3]
0021CAAC  0F 85 BF 05 00 00               jne 0x14021d071
0021CAB2  49 8B CD                        mov rcx, r13
0021CAB5  E8 A6 08 00 00                  call 0x14021d360
0021CABA  41 F7 45 78 00 20 00 00         test dword ptr [r13 + 0x78], 0x2000
0021CAC2  49 8B 97 40 8E 00 00            mov rdx, qword ptr [r15 + 0x8e40]
0021CAC9  0F 84 D6 01 00 00               je 0x14021cca5
0021CACF  48 85 D2                        test rdx, rdx
0021CAD2  0F 84 CD 01 00 00               je 0x14021cca5
0021CAD8  49 8B 8D 40 02 00 00            mov rcx, qword ptr [r13 + 0x240]
0021CADF  41 0F B6 87 D0 00 00 00         movzx eax, byte ptr [r15 + 0xd0]
0021CAE7  66 3B 01                        cmp ax, word ptr [rcx]
0021CAEA  0F 83 9C 05 00 00               jae 0x14021d08c
0021CAF0  48 8B 4C C1 08                  mov rcx, qword ptr [rcx + rax*8 + 8]
0021CAF5  48 23 CA                        and rcx, rdx
0021CAF8  48 3B CA                        cmp rcx, rdx
0021CAFB  0F 85 A4 01 00 00               jne 0x14021cca5
0021CB01  84 DB                           test bl, bl
0021CB03  0F 85 9C 01 00 00               jne 0x14021cca5
0021CB09  49 8B 9F 48 8E 00 00            mov rbx, qword ptr [r15 + 0x8e48]
0021CB10  48 8D 7E 04                     lea rdi, [rsi + 4]
0021CB14  48 C1 E7 04                     shl rdi, 4
0021CB18  0F 57 C0                        xorps xmm0, xmm0
0021CB1B  48 03 FB                        add rdi, rbx
0021CB1E  F7 05 10 A0 DA 00 00 00 20 00   test dword ptr [rip + 0xdaa010], 0x200000
0021CB28  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
0021CB2C  74 3D                           je 0x14021cb6b
0021CB2E  48 89 5D C7                     mov qword ptr [rbp - 0x39], rbx
0021CB32  48 8D 55 BF                     lea rdx, [rbp - 0x41]
0021CB36  48 C7 45 BF 00 00 00 00         mov qword ptr [rbp - 0x41], 0
0021CB3E  90                              nop
0021CB3F  48 87 13                        xchg qword ptr [rbx], rdx
0021CB42  48 85 D2                        test rdx, rdx
0021CB45  0F 85 03 04 00 00               jne 0x14021cf4e
0021CB4B  49 8D 85 D8 00 00 00            lea rax, [r13 + 0xd8]
0021CB52  45 85 E4                        test r12d, r12d
0021CB55  75 28                           jne 0x14021cb7f
0021CB57  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0021CB5B  48 39 39                        cmp qword ptr [rcx], rdi
0021CB5E  0F 84 FA 04 00 00               je 0x14021d05e
0021CB64  B9 03 00 00 00                  mov ecx, 3
0021CB69  CD 29                           int 0x29
0021CB6B  C7 45 E7 00 00 00 00            mov dword ptr [rbp - 0x19], 0
0021CB72  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0021CB78  73 D1                           jae 0x14021cb4b
0021CB7A  E9 BE 9D 4B 00                  jmp 0x1406d693d
0021CB7F  48 8B 0F                        mov rcx, qword ptr [rdi]
0021CB82  48 39 79 08                     cmp qword ptr [rcx + 8], rdi
0021CB86  75 DC                           jne 0x14021cb64
0021CB88  48 89 08                        mov qword ptr [rax], rcx
0021CB8B  48 89 78 08                     mov qword ptr [rax + 8], rdi
0021CB8F  48 89 41 08                     mov qword ptr [rcx + 8], rax
0021CB93  48 89 07                        mov qword ptr [rdi], rax
0021CB96  41 0F B3 B7 DC 83 00 00         btr dword ptr [r15 + 0x83dc], esi
0021CB9E  8B 43 08                        mov eax, dword ptr [rbx + 8]
0021CBA1  0F AB F0                        bts eax, esi
0021CBA4  89 43 08                        mov dword ptr [rbx + 8], eax
0021CBA7  41 8B 85 18 02 00 00            mov eax, dword ptr [r13 + 0x218]
0021CBAE  0F BA E8 1F                     bts eax, 0x1f
0021CBB2  41 89 85 18 02 00 00            mov dword ptr [r13 + 0x218], eax
0021CBB9  FF 43 0C                        inc dword ptr [rbx + 0xc]
0021CBBC  44 39 73 0C                     cmp dword ptr [rbx + 0xc], r14d
0021CBC0  0F 84 40 04 00 00               je 0x14021d006
0021CBC6  41 8B 45 54                     mov eax, dword ptr [r13 + 0x54]
0021CBCA  49 8B D5                        mov rdx, r13
0021CBCD  41 89 85 F8 06 00 00            mov dword ptr [r13 + 0x6f8], eax
0021CBD4  48 8B CB                        mov rcx, rbx
0021CBD7  48 01 43 10                     add qword ptr [rbx + 0x10], rax
0021CBDB  E8 60 C3 FF FF                  call 0x140218f40
0021CBE0  E8 3B C3 FF FF                  call 0x140218f20
0021CBE5  84 C0                           test al, al
0021CBE7  0F 85 EE 03 00 00               jne 0x14021cfdb
0021CBED  F7 05 41 9F DA 00 00 00 20 00   test dword ptr [rip + 0xda9f41], 0x200000
0021CBF7  0F 85 E6 00 00 00               jne 0x14021cce3
0021CBFD  F0 48 83 23 00                  lock and qword ptr [rbx], 0
0021CC02  33 FF                           xor edi, edi
0021CC04  E9 25 01 00 00                  jmp 0x14021cd2e
0021CC09  41 F6 47 23 10                  test byte ptr [r15 + 0x23], 0x10
0021CC0E  0F 84 EC FC FF FF               je 0x14021c900
0021CC14  E9 A0 FC FF FF                  jmp 0x14021c8b9
0021CC19  41 8B 45 78                     mov eax, dword ptr [r13 + 0x78]
0021CC1D  A9 00 0C 00 00                  test eax, 0xc00
0021CC22  0F 85 74 FE FF FF               jne 0x14021ca9c
0021CC28  41 80 BD C3 00 00 00 10         cmp byte ptr [r13 + 0xc3], 0x10
0021CC30  4C 8B CA                        mov r9, rdx
0021CC33  4C 8B 92 80 00 00 00            mov r10, qword ptr [rdx + 0x80]
0021CC3A  44 8B C7                        mov r8d, edi
0021CC3D  44 8B DF                        mov r11d, edi
0021CC40  7D 41                           jge 0x14021cc83
0021CC42  0F BA E0 09                     bt eax, 9
0021CC46  72 3B                           jb 0x14021cc83
0021CC48  49 8B CD                        mov rcx, r13
0021CC4B  E8 C0 96 13 00                  call 0x140356310
0021CC50  84 C0                           test al, al
0021CC52  75 2F                           jne 0x14021cc83
0021CC54  48 8B CA                        mov rcx, rdx
0021CC57  E8 44 5B FE FF                  call 0x1402027a0
0021CC5C  84 C0                           test al, al
0021CC5E  0F 85 35 06 00 00               jne 0x14021d299
0021CC64  45 03 41 7C                     add r8d, dword ptr [r9 + 0x7c]
0021CC68  4D 85 D2                        test r10, r10
0021CC6B  0F 85 E7 05 00 00               jne 0x14021d258
0021CC71  45 85 C0                        test r8d, r8d
0021CC74  0F 84 E8 05 00 00               je 0x14021d262
0021CC7A  45 85 DB                        test r11d, r11d
0021CC7D  74 04                           je 0x14021cc83
0021CC7F  41 0F B6 DE                     movzx ebx, r14b
0021CC83  45 85 C0                        test r8d, r8d
0021CC86  0F 84 10 FE FF FF               je 0x14021ca9c
0021CC8C  45 8B CC                        mov r9d, r12d
0021CC8F  4D 8B C5                        mov r8, r13
0021CC92  49 8B CF                        mov rcx, r15
0021CC95  E8 42 44 FE FF                  call 0x1402010dc
0021CC9A  41 BB 02 00 00 00               mov r11d, 2
0021CCA0  E9 8C 00 00 00                  jmp 0x14021cd31
0021CCA5  48 8D 86 44 08 00 00            lea rax, [rsi + 0x844]
0021CCAC  48 C1 E0 04                     shl rax, 4
0021CCB0  49 8D 8D D8 00 00 00            lea rcx, [r13 + 0xd8]
0021CCB7  49 03 C7                        add rax, r15
0021CCBA  45 85 E4                        test r12d, r12d
0021CCBD  0F 85 8B 01 00 00               jne 0x14021ce4e
0021CCC3  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
0021CCC7  48 39 02                        cmp qword ptr [rdx], rax
0021CCCA  0F 85 94 FE FF FF               jne 0x14021cb64
0021CCD0  48 89 01                        mov qword ptr [rcx], rax
0021CCD3  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0021CCD7  48 89 0A                        mov qword ptr [rdx], rcx
0021CCDA  48 89 48 08                     mov qword ptr [rax + 8], rcx
0021CCDE  E9 8E 01 00 00                  jmp 0x14021ce71
0021CCE3  0F 0D 4D BF                     prefetchw byte ptr [rbp - 0x41]
0021CCE7  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
0021CCEB  33 FF                           xor edi, edi
0021CCED  48 85 C0                        test rax, rax
0021CCF0  75 1F                           jne 0x14021cd11
0021CCF2  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
0021CCF6  48 8D 45 BF                     lea rax, [rbp - 0x41]
0021CCFA  F0 48 0F B1 39                  lock cmpxchg qword ptr [rcx], rdi
0021CCFF  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0021CD03  48 3B C1                        cmp rax, rcx
0021CD06  74 26                           je 0x14021cd2e
0021CD08  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0021CD0C  E8 8F AD FF FF                  call 0x140217aa0
0021CD11  48 8D 48 08                     lea rcx, [rax + 8]
0021CD15  48 89 7D BF                     mov qword ptr [rbp - 0x41], rdi
0021CD19  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
0021CD1D  48 8B C2                        mov rax, rdx
0021CD20  48 87 01                        xchg qword ptr [rcx], rax
0021CD23  32 C2                           xor al, dl
0021CD25  A8 04                           test al, 4
0021CD27  74 05                           je 0x14021cd2e
0021CD29  E8 F2 AE FF FF                  call 0x140217c20
0021CD2E  45 8B DE                        mov r11d, r14d
0021CD31  45 32 D2                        xor r10b, r10b
0021CD34  F7 05 D6 9D DA 00 00 08 00 00   test dword ptr [rip + 0xda9dd6], 0x800
0021CD3E  0F 85 60 05 00 00               jne 0x14021d2a4
0021CD44  48 8B 5D 6F                     mov rbx, qword ptr [rbp + 0x6f]
0021CD48  4C 8B C7                        mov r8, rdi
0021CD4B  8B C7                           mov eax, edi
0021CD4D  48 8B 13                        mov rdx, qword ptr [rbx]
0021CD50  4C 8B CA                        mov r9, rdx
0021CD53  49 83 E1 FE                     and r9, 0xfffffffffffffffe
0021CD57  4C 89 4D EF                     mov qword ptr [rbp - 0x11], r9
0021CD5B  41 23 D6                        and edx, r14d
0021CD5E  74 7E                           je 0x14021cdde
0021CD60  41 3B D6                        cmp edx, r14d
0021CD63  75 15                           jne 0x14021cd7a
0021CD65  49 8B 81 58 8E 00 00            mov rax, qword ptr [r9 + 0x8e58]
0021CD6C  4D 8B 81 58 8E 00 00            mov r8, qword ptr [r9 + 0x8e58]
0021CD73  49 83 C0 08                     add r8, 8
0021CD77  0F B6 00                        movzx eax, byte ptr [rax]
0021CD7A  85 C0                           test eax, eax
0021CD7C  74 15                           je 0x14021cd93
0021CD7E  66 90                           nop
0021CD80  8D 48 FF                        lea ecx, [rax - 1]
0021CD83  49 8B 14 C8                     mov rdx, qword ptr [r8 + rcx*8]
0021CD87  8B C1                           mov eax, ecx
0021CD89  F0 48 83 62 30 00               lock and qword ptr [rdx + 0x30], 0
0021CD8F  85 C9                           test ecx, ecx
0021CD91  75 ED                           jne 0x14021cd80
0021CD93  33 C0                           xor eax, eax
0021CD95  48 89 03                        mov qword ptr [rbx], rax
0021CD98  45 84 D2                        test r10b, r10b
0021CD9B  0F 85 15 05 00 00               jne 0x14021d2b6
0021CDA1  48 8B 7D DF                     mov rdi, qword ptr [rbp - 0x21]
0021CDA5  48 85 FF                        test rdi, rdi
0021CDA8  0F 85 E6 02 00 00               jne 0x14021d094
0021CDAE  80 7D CF 00                     cmp byte ptr [rbp - 0x31], 0
0021CDB2  0F 85 3E 05 00 00               jne 0x14021d2f6
0021CDB8  44 8B 4D D3                     mov r9d, dword ptr [rbp - 0x2d]
0021CDBC  44 8B 45 D7                     mov r8d, dword ptr [rbp - 0x29]
0021CDC0  45 3B C1                        cmp r8d, r9d
0021CDC3  0F 85 64 05 00 00               jne 0x14021d32d
0021CDC9  48 81 C4 98 00 00 00            add rsp, 0x98
0021CDD0  41 5F                           pop r15
0021CDD2  41 5E                           pop r14
0021CDD4  41 5D                           pop r13
0021CDD6  41 5C                           pop r12
0021CDD8  5F                              pop rdi
0021CDD9  5E                              pop rsi
0021CDDA  5B                              pop rbx
0021CDDB  5D                              pop rbp
0021CDDC  C3                              ret
0021CDDD  CC                              int3
0021CDDE  4C 8D 45 EF                     lea r8, [rbp - 0x11]
0021CDE2  41 8B C6                        mov eax, r14d
0021CDE5  EB 99                           jmp 0x14021cd80
0021CDE7  4C 8B 6D 77                     mov r13, qword ptr [rbp + 0x77]
0021CDEB  49 8B CD                        mov rcx, r13
0021CDEE  4C 89 65 DF                     mov qword ptr [rbp - 0x21], r12
0021CDF2  E8 09 E4 0E 00                  call 0x14030b200
0021CDF7  44 8B 65 7F                     mov r12d, dword ptr [rbp + 0x7f]
0021CDFB  84 C0                           test al, al
0021CDFD  0F 84 96 FA FF FF               je 0x14021c899
0021CE03  E8 08 95 13 00                  call 0x140356310
0021CE08  84 C0                           test al, al
0021CE0A  0F 84 89 FA FF FF               je 0x14021c899
0021CE10  85 F6                           test esi, esi
0021CE12  0F 84 81 FA FF FF               je 0x14021c899
0021CE18  41 F7 45 78 00 0C 00 00         test dword ptr [r13 + 0x78], 0xc00
0021CE20  4C 8B 7D 67                     mov r15, qword ptr [rbp + 0x67]
0021CE24  4C 8B 75 6F                     mov r14, qword ptr [rbp + 0x6f]
0021CE28  0F 85 73 FA FF FF               jne 0x14021c8a1
0021CE2E  F0 41 0F BA 6D 78 0B            lock bts dword ptr [r13 + 0x78], 0xb
0021CE35  E9 67 FA FF FF                  jmp 0x14021c8a1
0021CE3A  48 8B D7                        mov rdx, rdi
0021CE3D  E9 31 FC FF FF                  jmp 0x14021ca73
0021CE42  4C 8D 45 F7                     lea r8, [rbp - 9]
0021CE46  41 8B D6                        mov edx, r14d
0021CE49  E9 12 FB FF FF                  jmp 0x14021c960
0021CE4E  48 8B 10                        mov rdx, qword ptr [rax]
0021CE51  48 39 42 08                     cmp qword ptr [rdx + 8], rax
0021CE55  0F 85 09 FD FF FF               jne 0x14021cb64
0021CE5B  48 89 11                        mov qword ptr [rcx], rdx
0021CE5E  48 89 41 08                     mov qword ptr [rcx + 8], rax
0021CE62  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0021CE66  48 89 08                        mov qword ptr [rax], rcx
0021CE69  41 0F AB B7 DC 83 00 00         bts dword ptr [r15 + 0x83dc], esi
0021CE71  41 8B 87 D8 83 00 00            mov eax, dword ptr [r15 + 0x83d8]
0021CE78  49 8B D5                        mov rdx, r13
0021CE7B  0F AB F0                        bts eax, esi
0021CE7E  49 8B CF                        mov rcx, r15
0021CE81  41 89 87 D8 83 00 00            mov dword ptr [r15 + 0x83d8], eax
0021CE88  E8 03 C4 28 00                  call 0x1404a9290
0021CE8D  44 8B DF                        mov r11d, edi
0021CE90  E9 9C FE FF FF                  jmp 0x14021cd31
0021CE95  41 8B 40 74                     mov eax, dword ptr [r8 + 0x74]
0021CE99  A8 08                           test al, 8
0021CE9B  0F 85 7B F9 FF FF               jne 0x14021c81c
0021CEA1  F0 49 0F BA 68 40 00            lock bts qword ptr [r8 + 0x40], 0
0021CEA8  73 0C                           jae 0x14021ceb6
0021CEAA  F0 41 0F BA 68 78 0C            lock bts dword ptr [r8 + 0x78], 0xc
0021CEB1  E9 70 F9 FF FF                  jmp 0x14021c826
0021CEB6  41 8B 80 4C 02 00 00            mov eax, dword ptr [r8 + 0x24c]
0021CEBD  89 45 D7                        mov dword ptr [rbp - 0x29], eax
0021CEC0  49 3B 58 20                     cmp rbx, qword ptr [r8 + 0x20]
0021CEC4  72 65                           jb 0x14021cf2b
0021CEC6  41 B0 01                        mov r8b, 1
0021CEC9  49 8B CD                        mov rcx, r13
0021CECC  E8 BB 5E 1A 00                  call 0x1403c2d8c
0021CED1  45 33 C9                        xor r9d, r9d
0021CED4  33 D2                           xor edx, edx
0021CED6  49 8B CD                        mov rcx, r13
0021CED9  8B F8                           mov edi, eax
0021CEDB  E8 60 91 0E 00                  call 0x140306040
0021CEE0  84 C0                           test al, al
0021CEE2  75 12                           jne 0x14021cef6
0021CEE4  44 8B CF                        mov r9d, edi
0021CEE7  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
0021CEEC  4D 8B C5                        mov r8, r13
0021CEEF  33 C9                           xor ecx, ecx
0021CEF1  E8 1A A9 03 00                  call 0x140257810
0021CEF6  49 8B CD                        mov rcx, r13
0021CEF9  E8 B6 27 00 00                  call 0x14021f6b4
0021CEFE  0F AF 05 93 81 DA 00            imul eax, dword ptr [rip + 0xda8193]
0021CF05  8B C8                           mov ecx, eax
0021CF07  41 8B 45 78                     mov eax, dword ptr [r13 + 0x78]
0021CF0B  48 03 CB                        add rcx, rbx
0021CF0E  A8 20                           test al, 0x20
0021CF10  74 07                           je 0x14021cf19
0021CF12  F0 41 0F BA 75 78 05            lock btr dword ptr [r13 + 0x78], 5
0021CF19  49 89 4D 20                     mov qword ptr [r13 + 0x20], rcx
0021CF1D  49 8B CD                        mov rcx, r13
0021CF20  E8 F7 E5 25 00                  call 0x14047b51c
0021CF25  44 8B E6                        mov r12d, esi
0021CF28  89 75 7F                        mov dword ptr [rbp + 0x7f], esi
0021CF2B  49 8B CD                        mov rcx, r13
0021CF2E  E8 9D 9E 03 00                  call 0x140256dd0
0021CF33  85 C0                           test eax, eax
0021CF35  0F 84 23 02 00 00               je 0x14021d15e
0021CF3B  41 8B 85 4C 02 00 00            mov eax, dword ptr [r13 + 0x24c]
0021CF42  89 45 D3                        mov dword ptr [rbp - 0x2d], eax
0021CF45  49 89 75 40                     mov qword ptr [r13 + 0x40], rsi
0021CF49  E9 D8 F8 FF FF                  jmp 0x14021c826
0021CF4E  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0021CF52  E8 59 AF 03 00                  call 0x140257eb0
0021CF57  E9 EF FB FF FF                  jmp 0x14021cb4b
0021CF5C  33 C0                           xor eax, eax
0021CF5E  0F 57 C0                        xorps xmm0, xmm0
0021CF61  38 05 5E 9C DA 00               cmp byte ptr [rip + 0xda9c5e], al
0021CF67  F3 0F 7F 45 03                  movdqu xmmword ptr [rbp + 3], xmm0
0021CF6C  74 53                           je 0x14021cfc1
0021CF6E  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
0021CF77  E8 24 52 03 00                  call 0x1402521a0
0021CF7C  41 8B 90 A8 00 00 00            mov edx, dword ptr [r8 + 0xa8]
0021CF83  44 0F B6 C8                     movzx r9d, al
0021CF87  8B CA                           mov ecx, edx
0021CF89  83 C9 04                        or ecx, 4
0021CF8C  41 89 88 A8 00 00 00            mov dword ptr [r8 + 0xa8], ecx
0021CF93  85 D2                           test edx, edx
0021CF95  75 24                           jne 0x14021cfbb
0021CF97  B9 15 00 01 C0                  mov ecx, 0xc0010015
0021CF9C  0F 32                           rdmsr
0021CF9E  48 C1 E2 20                     shl rdx, 0x20
0021CFA2  48 0B C2                        or rax, rdx
0021CFA5  48 BA 00 00 00 00 01 00 00 00   movabs rdx, 0x100000000
0021CFAF  48 0B C2                        or rax, rdx
0021CFB2  48 8B D0                        mov rdx, rax
0021CFB5  48 C1 EA 20                     shr rdx, 0x20
0021CFB9  0F 30                           wrmsr
0021CFBB  45 84 C9                        test r9b, r9b
0021CFBE  74 01                           je 0x14021cfc1
0021CFC0  FB                              sti
0021CFC1  BA 2F 00 00 00                  mov edx, 0x2f
0021CFC6  C7 45 FF 05 00 00 00            mov dword ptr [rbp - 1], 5
0021CFCD  48 8D 4D FF                     lea rcx, [rbp - 1]
0021CFD1  E8 3A 53 03 00                  call 0x140252310
0021CFD6  E9 D3 FD FF FF                  jmp 0x14021cdae
0021CFDB  41 F6 47 23 20                  test byte ptr [r15 + 0x23], 0x20
0021CFE0  0F 84 07 FC FF FF               je 0x14021cbed
0021CFE6  49 8B CD                        mov rcx, r13
0021CFE9  E8 92 AB 2B 00                  call 0x1404d7b80
0021CFEE  84 C0                           test al, al
0021CFF0  0F 85 F7 FB FF FF               jne 0x14021cbed
0021CFF6  48 8B D3                        mov rdx, rbx
0021CFF9  49 8B CF                        mov rcx, r15
0021CFFC  E8 03 E6 2D 00                  call 0x1404fb604
0021D001  E9 E7 FB FF FF                  jmp 0x14021cbed
0021D006  48 8B 8B D0 02 00 00            mov rcx, qword ptr [rbx + 0x2d0]
0021D00D  48 8B 83 C8 02 00 00            mov rax, qword ptr [rbx + 0x2c8]
0021D014  F0 48 09 81 88 01 00 00         lock or qword ptr [rcx + 0x188], rax
0021D01C  E9 A5 FB FF FF                  jmp 0x14021cbc6
0021D021  48 8B D7                        mov rdx, rdi
0021D024  48 8B CB                        mov rcx, rbx
0021D027  E8 58 78 13 00                  call 0x140354884
0021D02C  84 C0                           test al, al
0021D02E  0F 85 E7 00 00 00               jne 0x14021d11b
0021D034  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0021D038  48 39 03                        cmp qword ptr [rbx], rax
0021D03B  0F 82 26 F8 FF FF               jb 0x14021c867
0021D041  F6 43 70 02                     test byte ptr [rbx + 0x70], 2
0021D045  0F 85 1C F8 FF FF               jne 0x14021c867
0021D04B  4D 8B C5                        mov r8, r13
0021D04E  48 8B D3                        mov rdx, rbx
0021D051  48 8B CF                        mov rcx, rdi
0021D054  E8 6F 5F 23 00                  call 0x140452fc8
0021D059  E9 09 F8 FF FF                  jmp 0x14021c867
0021D05E  48 89 38                        mov qword ptr [rax], rdi
0021D061  48 89 48 08                     mov qword ptr [rax + 8], rcx
0021D065  48 89 01                        mov qword ptr [rcx], rax
0021D068  48 89 47 08                     mov qword ptr [rdi + 8], rax
0021D06C  E9 2D FB FF FF                  jmp 0x14021cb9e
0021D071  49 8B 85 C8 03 00 00            mov rax, qword ptr [r13 + 0x3c8]
0021D078  F0 81 08 00 00 04 00            lock or dword ptr [rax], 0x40000
0021D07F  E9 2E FA FF FF                  jmp 0x14021cab2
0021D084  4C 8B C7                        mov r8, rdi
0021D087  E9 71 F8 FF FF                  jmp 0x14021c8fd
0021D08C  48 8B CF                        mov rcx, rdi
0021D08F  E9 61 FA FF FF                  jmp 0x14021caf5
0021D094  48 8B DF                        mov rbx, rdi
0021D097  44 0F B6 8B C0 FE FF FF         movzx r9d, byte ptr [rbx - 0x140]
0021D09F  48 8D 8B 50 FE FF FF            lea rcx, [rbx - 0x1b0]
0021D0A6  41 8B 87 D8 00 00 00            mov eax, dword ptr [r15 + 0xd8]
0021D0AD  44 8B 83 CC FE FF FF            mov r8d, dword ptr [rbx - 0x134]
0021D0B4  48 2B C8                        sub rcx, rax
0021D0B7  41 8B 57 24                     mov edx, dword ptr [r15 + 0x24]
0021D0BB  41 D0 E9                        shr r9b, 1
0021D0BE  45 22 CE                        and r9b, r14b
0021D0C1  E8 D6 B8 2D 00                  call 0x1404f899c
0021D0C6  48 8B 1B                        mov rbx, qword ptr [rbx]
0021D0C9  48 85 DB                        test rbx, rbx
0021D0CC  75 C9                           jne 0x14021d097
0021D0CE  33 D2                           xor edx, edx
0021D0D0  8B DA                           mov ebx, edx
0021D0D2  F0 49 0F BA 6F 30 00            lock bts qword ptr [r15 + 0x30], 0
0021D0D9  73 1B                           jae 0x14021d0f6
0021D0DB  FF C3                           inc ebx
0021D0DD  85 1D C9 81 DA 00               test dword ptr [rip + 0xda81c9], ebx
0021D0E3  0F 84 2C 01 00 00               je 0x14021d215
0021D0E9  F3 90                           pause
0021D0EB  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
0021D0EF  48 85 C0                        test rax, rax
0021D0F2  74 DE                           je 0x14021d0d2
0021D0F4  EB E5                           jmp 0x14021d0db
0021D0F6  48 8B 07                        mov rax, qword ptr [rdi]
0021D0F9  B9 FF FE 00 00                  mov ecx, 0xfeff
0021D0FE  33 D2                           xor edx, edx
0021D100  66 21 8F C0 FE FF FF            and word ptr [rdi - 0x140], cx
0021D107  48 89 17                        mov qword ptr [rdi], rdx
0021D10A  48 8B F8                        mov rdi, rax
0021D10D  48 85 C0                        test rax, rax
0021D110  0F 84 C0 01 00 00               je 0x14021d2d6
0021D116  48 8B 00                        mov rax, qword ptr [rax]
0021D119  EB E5                           jmp 0x14021d100
0021D11B  F6 43 70 01                     test byte ptr [rbx + 0x70], 1
0021D11F  0F 84 42 F7 FF FF               je 0x14021c867
0021D125  41 B0 01                        mov r8b, 1
0021D128  48 8B D3                        mov rdx, rbx
0021D12B  49 8B CD                        mov rcx, r13
0021D12E  E8 05 55 FE FF                  call 0x140202638
0021D133  E9 2F F7 FF FF                  jmp 0x14021c867
0021D138  44 3B 7B 7C                     cmp r15d, dword ptr [rbx + 0x7c]
0021D13C  0F 84 35 01 00 00               je 0x14021d277
0021D142  B8 00 01 00 00                  mov eax, 0x100
0021D147  66 09 43 70                     or word ptr [rbx + 0x70], ax
0021D14B  4C 89 A3 B0 01 00 00            mov qword ptr [rbx + 0x1b0], r12
0021D152  4C 8D A3 B0 01 00 00            lea r12, [rbx + 0x1b0]
0021D159  E9 19 F7 FF FF                  jmp 0x14021c877
0021D15E  E8 7D CC 17 00                  call 0x140399de0
0021D163  85 C0                           test eax, eax
0021D165  0F 84 D0 FD FF FF               je 0x14021cf3b
0021D16B  49 8B 8D 40 02 00 00            mov rcx, qword ptr [r13 + 0x240]
0021D172  49 8B D7                        mov rdx, r15
0021D175  E8 26 95 21 00                  call 0x1404366a0
0021D17A  84 C0                           test al, al
0021D17C  0F 85 A6 97 4B 00               jne 0x1406d6928
0021D182  F0 41 0F BA 6D 78 0C            lock bts dword ptr [r13 + 0x78], 0xc
0021D189  E9 9A 97 4B 00                  jmp 0x1406d6928
0021D18E  48 8B DF                        mov rbx, rdi
0021D191  44 0F B6 8B C0 FE FF FF         movzx r9d, byte ptr [rbx - 0x140]
0021D199  48 8D 8B 50 FE FF FF            lea rcx, [rbx - 0x1b0]
0021D1A0  41 8B 87 D8 00 00 00            mov eax, dword ptr [r15 + 0xd8]
0021D1A7  44 8B 83 CC FE FF FF            mov r8d, dword ptr [rbx - 0x134]
0021D1AE  48 2B C8                        sub rcx, rax
0021D1B1  41 8B 57 24                     mov edx, dword ptr [r15 + 0x24]
0021D1B5  41 D0 E9                        shr r9b, 1
0021D1B8  45 22 CE                        and r9b, r14b
0021D1BB  E8 DC B7 2D 00                  call 0x1404f899c
0021D1C0  48 8B 1B                        mov rbx, qword ptr [rbx]
0021D1C3  48 85 DB                        test rbx, rbx
0021D1C6  75 C9                           jne 0x14021d191
0021D1C8  33 C0                           xor eax, eax
0021D1CA  8B D8                           mov ebx, eax
0021D1CC  0F 1F 40 00                     nop dword ptr [rax]
0021D1D0  F0 49 0F BA 6F 30 00            lock bts qword ptr [r15 + 0x30], 0
0021D1D7  73 17                           jae 0x14021d1f0
0021D1D9  FF C3                           inc ebx
0021D1DB  85 1D CB 80 DA 00               test dword ptr [rip + 0xda80cb], ebx
0021D1E1  74 59                           je 0x14021d23c
0021D1E3  F3 90                           pause
0021D1E5  49 8B 47 30                     mov rax, qword ptr [r15 + 0x30]
0021D1E9  48 85 C0                        test rax, rax
0021D1EC  74 E2                           je 0x14021d1d0
0021D1EE  EB E9                           jmp 0x14021d1d9
0021D1F0  48 8B 07                        mov rax, qword ptr [rdi]
0021D1F3  B9 FF FE 00 00                  mov ecx, 0xfeff
0021D1F8  33 D2                           xor edx, edx
0021D1FA  66 21 8F C0 FE FF FF            and word ptr [rdi - 0x140], cx
0021D201  48 89 17                        mov qword ptr [rdi], rdx
0021D204  48 8B F8                        mov rdi, rax
0021D207  48 85 C0                        test rax, rax
0021D20A  0F 84 D0 00 00 00               je 0x14021d2e0
0021D210  48 8B 00                        mov rax, qword ptr [rax]
0021D213  EB E5                           jmp 0x14021d1fa
0021D215  8B 05 9D 98 DA 00               mov eax, dword ptr [rip + 0xda989d]
0021D21B  A8 40                           test al, 0x40
0021D21D  0F 84 C6 FE FF FF               je 0x14021d0e9
0021D223  E8 68 22 0F 00                  call 0x14030f490
0021D228  84 C0                           test al, al
0021D22A  0F 84 B9 FE FF FF               je 0x14021d0e9
0021D230  8B CB                           mov ecx, ebx
0021D232  E8 29 22 0F 00                  call 0x14030f460
0021D237  E9 AF FE FF FF                  jmp 0x14021d0eb
0021D23C  8B 05 76 98 DA 00               mov eax, dword ptr [rip + 0xda9876]
0021D242  A8 40                           test al, 0x40
0021D244  74 9D                           je 0x14021d1e3
0021D246  E8 45 22 0F 00                  call 0x14030f490
0021D24B  84 C0                           test al, al
0021D24D  74 94                           je 0x14021d1e3
0021D24F  8B CB                           mov ecx, ebx
0021D251  E8 0A 22 0F 00                  call 0x14030f460
0021D256  EB 8D                           jmp 0x14021d1e5
0021D258  49 8B 81 80 00 00 00            mov rax, qword ptr [r9 + 0x80]
0021D25F  44 03 18                        add r11d, dword ptr [rax]
0021D262  4D 8B 89 A0 01 00 00            mov r9, qword ptr [r9 + 0x1a0]
0021D269  4D 85 C9                        test r9, r9
0021D26C  0F 84 08 FA FF FF               je 0x14021cc7a
0021D272  E9 ED F9 FF FF                  jmp 0x14021cc64
0021D277  0F B7 4B 70                     movzx ecx, word ptr [rbx + 0x70]
0021D27B  33 C0                           xor eax, eax
0021D27D  66 D1 E9                        shr cx, 1
0021D280  66 83 E1 01                     and cx, 1
0021D284  66 45 85 F6                     test r14w, r14w
0021D288  0F 95 C0                        setne al
0021D28B  66 3B C1                        cmp ax, cx
0021D28E  0F 84 E3 F5 FF FF               je 0x14021c877
0021D294  E9 A9 FE FF FF                  jmp 0x14021d142
0021D299  41 B8 FF FF FF FF               mov r8d, 0xffffffff
0021D29F  E9 DF F9 FF FF                  jmp 0x14021cc83
0021D2A4  45 0F B6 D6                     movzx r10d, r14b
0021D2A8  66 F0 41 FF 85 64 03 00 00      lock inc word ptr [r13 + 0x364]
0021D2B1  E9 8E FA FF FF                  jmp 0x14021cd44
0021D2B6  41 8B 57 24                     mov edx, dword ptr [r15 + 0x24]
0021D2BA  45 33 C9                        xor r9d, r9d
0021D2BD  45 8B C3                        mov r8d, r11d
0021D2C0  49 8B CD                        mov rcx, r13
0021D2C3  E8 7C 61 00 00                  call 0x140223444
0021D2C8  66 F0 41 FF 8D 64 03 00 00      lock dec word ptr [r13 + 0x364]
0021D2D1  E9 CB FA FF FF                  jmp 0x14021cda1
0021D2D6  F0 49 21 57 30                  lock and qword ptr [r15 + 0x30], rdx
0021D2DB  E9 CE FA FF FF                  jmp 0x14021cdae
0021D2E0  F0 49 21 57 30                  lock and qword ptr [r15 + 0x30], rdx
0021D2E5  E9 A0 F6 FF FF                  jmp 0x14021c98a
0021D2EA  49 8D BF D8 35 00 00            lea rdi, [r15 + 0x35d8]
0021D2F1  E9 0F F7 FF FF                  jmp 0x14021ca05
0021D2F6  45 8B 45 74                     mov r8d, dword ptr [r13 + 0x74]
0021D2FA  45 33 C9                        xor r9d, r9d
0021D2FD  49 8B 85 40 02 00 00            mov rax, qword ptr [r13 + 0x240]
0021D304  49 8B CD                        mov rcx, r13
0021D307  41 0F B7 95 48 02 00 00         movzx edx, word ptr [r13 + 0x248]
0021D30F  41 C1 E8 03                     shr r8d, 3
0021D313  41 80 E0 01                     and r8b, 1
0021D317  66 C7 44 24 28 36 05            mov word ptr [rsp + 0x28], 0x536
0021D31E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0021D323  E8 78 56 1A 00                  call 0x1403c29a0
0021D328  E9 8B FA FF FF                  jmp 0x14021cdb8
0021D32D  F7 05 D9 97 DA 00 00 00 00 08   test dword ptr [rip + 0xda97d9], 0x8000000
0021D337  0F 84 8C FA FF FF               je 0x14021cdc9
0021D33D  BA 46 05 00 00                  mov edx, 0x546
0021D342  49 8B CD                        mov rcx, r13
0021D345  E8 BE 34 1A 00                  call 0x1403c0808
0021D34A  E9 7A FA FF FF                  jmp 0x14021cdc9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiQueueReadyThread(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m5C;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned __int8 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int16 v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (152);
    v_rsi = 0;
    v_stack_m88 = 0xFFFFFFFFULL;
    v_stack_m8C = 0xFFFFFFFFULL;
    v_stack_m90 = 0;
    v_stack_m80 = 0;
    v_stack_p20 = (unsigned int)(*(unsigned __int8 *)(a3 + 565));
    if ((*(unsigned __int64 *)(a3 + 568)) != (*(unsigned __int64 *)(v_rip + 14328852))) goto loc_0021CE95;
loc_0021C81C:
    if ((*(unsigned __int64 *)(a3 + 72)) >= (*(unsigned __int64 *)(a3 + 32))) goto loc_0021CEA1;
loc_0021C826:
    if (*(unsigned __int64 *)(a3 + 104) == 0) goto loc_0021C8A1;
    v_rbx = ((unsigned int)(*(unsigned int *)(a1 + 216))) + (*(unsigned __int64 *)(a3 + 104));
loc_0021C840:
    v_r14 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_rbx + 112))) & (2));
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_rbx + 112))) & (4)) != 0) goto loc_0021D021;
    result = KiComputeGroupSchedulingRank(*(unsigned __int64 *)(a3 + 104), v_stack_p8, a3, v_rbx);
loc_0021C867:
    if (((*(unsigned int *)(v_rip + 14328483)) & (0x4000ULL)) != 0) goto loc_0021D138;
loc_0021C877:
    v_rsi = (unsigned int)((v_rsi) + (*(unsigned int *)(v_rbx + 124)));
    if (*(unsigned __int64 *)(v_rbx + 416) == 0) goto loc_0021CDE7;
    v_rdi = (*(unsigned __int64 *)(v_rbx + 416)) - ((unsigned int)(*(unsigned int *)(v_stack_p8 + 216)));
    goto loc_0021C840;
loc_0021C899:
loc_0021C8A1:
    v_rdi = 0;
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(v_stack_p8 + 195)))) < (*(unsigned int *)(v_rip + 14322383))) goto loc_0021CC09;
loc_0021C8B9:
    if (*(unsigned __int64 *)(v_stack_p8 + 104) == 0) goto loc_0021C8D5;
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_p8 + 216))) + (*(unsigned __int64 *)(v_stack_p8 + 104));
    result = KiCheckForMaxOverQuotaScb(a1, 0, a3, v_rbx);
    if ((unsigned __int8)(result) != 0) goto loc_0021C900;
loc_0021C8D5:
    if (((unsigned __int16)(*(unsigned __int8 *)(v_stack_p8 + 208))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 576)))) goto loc_0021D084;
loc_0021C8FD:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 192) + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 576) + *(unsigned __int8 *)(v_stack_p8 + 208) * 8 + 8));
loc_0021C900:
    if (((*(unsigned int *)(v_stack_p8 + 120)) & (0x1000ULL)) != 0) goto loc_0021C913;
    if (a2 == 0) goto loc_0021CA42;
loc_0021C913:
    result = KiEnterDeferredReadyState(v_stack_p8, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 576) + *(unsigned __int8 *)(v_stack_p8 + 208) * 8 + 8), v_rbx);
    a4 = (*(unsigned __int64 *)(v_stack_p10)) & (-2);
    v_stack_m68 = a4;
    a1 = (unsigned int)((*(unsigned __int64 *)(v_stack_p10)) & (1));
    if (condition_is_equal) goto loc_0021CE42;
    if (((unsigned int)(a1)) == 1) {
        result = *(unsigned __int64 *)(a4 + 36440);
        a3 = *(unsigned __int64 *)(a4 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_0021C972;
loc_0021C960:
    if ((unsigned int)(a2 - 1) != 0) goto loc_0021C960;
loc_0021C972:
    result = 0;
    *(unsigned __int64 *)(v_stack_p10) = 0;
    if (v_stack_m80 != 0) goto loc_0021D18E;
    a2 = 0;
loc_0021C98A:
    v_stack_mA8 = 0;
    *(unsigned __int8 *)(v_stack_p8 + 565) = 0;
    a4 = 0;
    result = KiDeferredReadySingleThread(v_stack_p8, v_stack_p8, v_stack_mA8, a4);
    if (v_stack_mA8 == 0) goto loc_0021D2EA;
    v_stack_mA8 = *(unsigned __int64 *)(v_stack_mA8);
loc_0021C9C2:
    a4 = 0;
    result = KiDeferredReadySingleThread(v_stack_p8, v_stack_mA8 - 216, v_stack_mA8, a4);
    v_r14 = (unsigned int)((1) + 1);
    if (v_stack_mA8 != 0) {
        result = *(unsigned __int64 *)(v_stack_mA8);
        v_stack_mA8 = result;
    }
    if ((((unsigned __int8)(v_r14)) & (15)) == 0) {
        a1 = v_stack_p8 + 13784;
        result = KiFlushSoftwareInterruptBatch(a1, v_stack_mA8 - 216, v_stack_mA8, a4);
    }
    if (v_stack_mA8 != 0) goto loc_0021C9C2;
loc_0021CA05:
    result = KiFlushSoftwareInterruptBatch(v_stack_p8 + 13784, v_stack_mA8 - 216, v_stack_mA8, a4);
    if (*(unsigned __int64 *)(v_stack_p8 + 16) != 0) goto loc_0021CDAE;
    if ((*(unsigned __int64 *)(v_stack_p8 + 8)) == (*(unsigned __int64 *)(v_stack_p8 + 24))) goto loc_0021CDAE;
    if ((*(unsigned __int64 *)(v_stack_p8 + 16)) == (*(unsigned __int64 *)(v_stack_p8 + 16))) goto loc_0021CDAE;
    if ((*(unsigned __int8 *)(v_stack_p8 + 32)) == ((unsigned __int8)(*(unsigned __int64 *)(v_stack_p8 + 16)))) goto loc_0021CF5C;
    *(unsigned __int8 *)(v_stack_p8 + 6) = 1;
    goto loc_0021CDAE;
loc_0021CA42:
    *(unsigned __int8 *)(v_stack_p8 + 565) = (unsigned __int8)(v_stack_p8 + 13784);
    *(unsigned int *)(v_stack_p8 + 436) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 24))));
    if (*(unsigned __int64 *)(v_stack_p8 + 104) == 0) goto loc_0021CE3A;
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_p8 + 216))) + (*(unsigned __int64 *)(v_stack_p8 + 104));
loc_0021CA73:
    if (*(unsigned __int64 *)(v_stack_p8 + 36536) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p8 + 36536) + 16) = (unsigned __int8)(v_stack_p8 + 13784);
    }
    v_rbx = 0;
    *(unsigned __int8 *)(v_stack_p8 + 388) = 1;
    if (a2 != 0) goto loc_0021CC19;
loc_0021CA9C:
    if (((*(unsigned int *)(v_stack_p8 + 120)) & (0x400000ULL)) != 0) goto loc_0021D071;
loc_0021CAB2:
    result = KiUpdateVpBackingThreadPriorityOnReadyQueueInsertion(v_stack_p8, a2, v_stack_mA8, a4);
    if (((*(unsigned int *)(v_stack_p8 + 120)) & (0x2000ULL)) == 0) goto loc_0021CCA5;
    if (*(unsigned __int64 *)(v_stack_p8 + 36416) == 0) goto loc_0021CCA5;
    if (((unsigned __int16)(*(unsigned __int8 *)(v_stack_p8 + 208))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 576)))) goto loc_0021D08C;
loc_0021CAF5:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 576) + *(unsigned __int8 *)(v_stack_p8 + 208) * 8 + 8)) & (*(unsigned __int64 *)(v_stack_p8 + 36416));
    if (a1 != (*(unsigned __int64 *)(v_stack_p8 + 36416))) goto loc_0021CCA5;
    if (0 != 0) goto loc_0021CCA5;
    v_rdi = ((__int8)(*(unsigned __int8 *)(v_stack_p8 + 195)) + 4) << (4);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_stack_p8 + 36424));
    v_stack_mA0 = v_xmm0;
    if (((*(unsigned int *)(v_rip + 14327824)) & (0x200000ULL)) == 0) goto loc_0021CB6B;
    v_stack_m98 = *(unsigned __int64 *)(v_stack_p8 + 36424);
    v_stack_mA0 = 0;
    if (v_stack_mA0 != 0) goto loc_0021CF4E;
loc_0021CB4B:
    if (0 != 0) goto loc_0021CB7F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8))) == v_rdi) goto loc_0021D05E;
loc_0021CB64:
loc_0021CB6B:
    v_stack_m78 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8))) >= v_rdi) goto loc_0021CB4B;
loc_0021CB7F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 8)) != v_rdi) goto loc_0021CB64;
    *(unsigned __int64 *)(v_stack_p8 + 216) = *(unsigned __int64 *)(v_rdi);
    *(unsigned __int64 *)(v_stack_p8 + 216 + 8) = v_rdi;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 8) = v_stack_p8 + 216;
    *(unsigned __int64 *)(v_rdi) = v_stack_p8 + 216;
loc_0021CB9E:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 36424) + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 36424) + 8)));
    *(unsigned int *)(v_stack_p8 + 536) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 536)));
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 36424) + 12)) == 1) goto loc_0021D006;
loc_0021CBC6:
    *(unsigned int *)(v_stack_p8 + 1784) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 84)));
    result = KiUpdateSoftParkElectionStatisticsOnInsertion(*(unsigned __int64 *)(v_stack_p8 + 36424), v_stack_p8, v_stack_mA8, a4);
    result = KeIsForceParkingEnabled(*(unsigned __int64 *)(v_stack_p8 + 36424), v_stack_p8, v_stack_mA8, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0021CFDB;
loc_0021CBED:
    if (((*(unsigned int *)(v_rip + 14327617)) & (0x200000ULL)) != 0) goto loc_0021CCE3;
    v_rdi = 0;
    goto loc_0021CD2E;
loc_0021CC09:
    if (((*(unsigned __int8 *)(v_stack_p8 + 35)) & (16)) == 0) goto loc_0021C900;
    goto loc_0021C8B9;
loc_0021CC19:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 120)))) & (0xC00ULL)) != 0) goto loc_0021CA9C;
    if ((*(unsigned __int8 *)(v_stack_p8 + 195)) >= 16) goto loc_0021CC83;
    if ((*(unsigned __int8 *)(v_stack_p8 + 195)) < 16) goto loc_0021CC83;
    result = KiShouldPreemptionBeDeferred(v_stack_p8, v_stack_p8, 0, v_stack_p8);
    if ((unsigned __int8)(result) != 0) goto loc_0021CC83;
    result = KiCheckForMaxOverQuotaScb(v_stack_p8, v_stack_p8, 0, v_stack_p8);
    if ((unsigned __int8)(result) != 0) goto loc_0021D299;
loc_0021CC64:
    a3 = (unsigned int)((0) + (*(unsigned int *)(v_stack_p8 + 124)));
    if (*(unsigned __int64 *)(v_stack_p8 + 128) != 0) goto loc_0021D258;
    if ((unsigned int)(a3) == 0) goto loc_0021D262;
loc_0021CC7A:
    v_rbx = *(unsigned __int64 *)(v_stack_p8 + 36424);
    if (0 != 0) {
        v_rbx = 1;
    }
    if ((unsigned int)(a3) == 0) goto loc_0021CA9C;
    result = KiAddThreadToScbQueue(v_stack_p8, v_stack_p8, v_stack_p8, 0);
    goto loc_0021CD31;
loc_0021CCA5:
    result = ((__int8)(*(unsigned __int8 *)(v_stack_p8 + 195)) + 2116) << (4);
    result = (result) + (v_stack_p8);
    if (0 != 0) goto loc_0021CE4E;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_0021CB64;
    *(unsigned __int64 *)(v_stack_p8 + 216) = result;
    *(unsigned __int64 *)(v_stack_p8 + 216 + 8) = *(unsigned __int64 *)(result + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = v_stack_p8 + 216;
    *(unsigned __int64 *)(result + 8) = v_stack_p8 + 216;
    goto loc_0021CE71;
loc_0021CCE3:
    v_rdi = 0;
    if (v_stack_mA0 != 0) goto loc_0021CD11;
    if (v_stack_mA0 == v_stack_mA0) goto loc_0021CD2E;
    result = KxWaitForLockChainValid(v_stack_mA0, *(unsigned __int64 *)(result + 8), v_stack_p8, 0);
loc_0021CD11:
    v_stack_mA0 = 0;
    result = (unsigned __int8)((v_stack_m98) ^ ((unsigned __int8)(v_stack_m98)));
    if ((((unsigned __int8)(result)) & (4)) != 0) {
        result = KeWakeAddressAll(result + 8, v_stack_m98, v_stack_p8, 0);
    }
loc_0021CD31:
    v_r10 = 0;
    if (((*(unsigned int *)(v_rip + 14327254)) & (0x800ULL)) != 0) goto loc_0021D2A4;
loc_0021CD44:
    a4 = (*(unsigned __int64 *)(v_stack_p10)) & (-2);
    v_stack_m70 = a4;
    a2 = (unsigned int)((*(unsigned __int64 *)(v_stack_p10)) & (1));
    if (condition_is_equal) goto loc_0021CDDE;
    result = 0;
    if (((unsigned int)(a2)) == 1) {
        result = *(unsigned __int64 *)(a4 + 36440);
        a3 = *(unsigned __int64 *)(a4 + 36440);
        a3 = (a3) + (8);
        result = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(result) == 0) goto loc_0021CD93;
loc_0021CD80:
    if ((unsigned int)(result - 1) != 0) goto loc_0021CD80;
loc_0021CD93:
    result = 0;
    *(unsigned __int64 *)(v_stack_p10) = 0;
    if (0 != 0) goto loc_0021D2B6;
loc_0021CDA1:
    if (v_stack_m80 != 0) goto loc_0021D094;
loc_0021CDAE:
    if (v_stack_m90 != 0) goto loc_0021D2F6;
loc_0021CDB8:
    if (((unsigned int)((unsigned int)(v_stack_m88))) != ((unsigned int)((unsigned int)(v_stack_m8C)))) goto loc_0021D32D;
loc_0021CDC9:
    v_rsp = (v_rsp) + (152);
    return result;
loc_0021CDDE:
    goto loc_0021CD80;
loc_0021CDE7:
    v_stack_m80 = 0;
    result = KiIsThreadConstrainedBySchedulingGroup(v_stack_p18, *(unsigned __int64 *)(a3 + result - 1 * 8), v_stack_m70, (unsigned int)(v_stack_m8C));
    if ((unsigned __int8)(result) == 0) goto loc_0021C899;
    result = KiShouldPreemptionBeDeferred(v_stack_p18, *(unsigned __int64 *)(a3 + result - 1 * 8), v_stack_m70, (unsigned int)(v_stack_m8C));
    if ((unsigned __int8)(result) == 0) goto loc_0021C899;
    if ((unsigned int)((__int8)(*(unsigned __int8 *)(v_stack_p8 + 195))) == 0) goto loc_0021C899;
    if (((*(unsigned int *)(v_stack_p18 + 120)) & (0xC00ULL)) != 0) goto loc_0021C8A1;
    goto loc_0021C8A1;
loc_0021CE3A:
    goto loc_0021CA73;
loc_0021CE42:
    goto loc_0021C960;
loc_0021CE4E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) != result) goto loc_0021CB64;
    *(unsigned __int64 *)(v_stack_p18) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(v_stack_p18 + 8) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = v_stack_p18;
    *(unsigned __int64 *)(result) = v_stack_p18;
loc_0021CE71:
    *(unsigned int *)(v_stack_p8 + 33752) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 33752)));
    result = KiUpdateLocalReadyQueueStatisticsOnInsertion(v_stack_p8, v_stack_p18, v_stack_m68, (unsigned int)(v_stack_m8C));
    goto loc_0021CD31;
loc_0021CE95:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m68 + 116)))) & (8)) != 0) goto loc_0021C81C;
loc_0021CEA1:
    if (condition_is_above_or_equal) goto loc_0021CEB6;
    goto loc_0021C826;
loc_0021CEB6:
    v_stack_m88 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68 + 588)));
    if (v_stack_p10 < (*(unsigned __int64 *)(v_stack_m68 + 32))) goto loc_0021CF2B;
    result = KiComputeNewPriority(v_stack_p18, v_stack_p18, 1, (unsigned int)(v_stack_m8C));
    a4 = 0;
    a2 = 0;
    result = KiUpdateVPBackingThreadPriority(v_stack_p18, a2, 1, a4);
    if ((unsigned __int8)(result) == 0) {
        a4 = (unsigned int)((unsigned int)((unsigned int)(result)));
        v_stack_p20 = (unsigned __int8)((__int8)(*(unsigned __int8 *)(v_stack_p8 + 195)));
        a3 = v_stack_p18;
        a1 = 0;
        result = KiUpdateThreadPriority(a1, a2, a3, a4);
    }
    result = KiQueryQuantumReset(v_stack_p18, a2, a3, a4);
    result = (unsigned int)((result) * (*(unsigned int *)(v_rip + 14320019)));
    a1 = ((unsigned int)((unsigned int)(result))) + (v_stack_p10);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18 + 120)))) & (32)) != 0) {
    }
    *(unsigned __int64 *)(v_stack_p18 + 32) = a1;
    result = KiTryScheduleNextForegroundBoost(v_stack_p18, a2, a3, a4);
    v_stack_p20 = (unsigned int)((__int8)(*(unsigned __int8 *)(v_stack_p8 + 195)));
loc_0021CF2B:
    result = KiCheckThreadAffinity(v_stack_p18, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0021D15E;
loc_0021CF3B:
    v_stack_m8C = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 588)));
    *(unsigned __int64 *)(v_stack_p18 + 64) = (__int8)(*(unsigned __int8 *)(v_stack_p8 + 195));
    goto loc_0021C826;
loc_0021CF4E:
    result = KxWaitForLockOwnerShip(v_stack_mA0, a2, a3, a4);
    goto loc_0021CB4B;
loc_0021CF5C:
    result = 0;
    v_stack_m5C = v_xmm0;
    if ((*(unsigned __int8 *)(v_rip + 14326878)) == 0) goto loc_0021CFC1;
    result = HalpDisableInterrupts(v_stack_mA0, a2, *(unsigned __int64 *)(gs_base + (0 + 32)), a4);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168))))) | (4));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168) = (unsigned int)(a1);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168))) == 0) {
        a1 = 0xC0010015ULL;
        a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 168))) << (32);
        result = (result) | (a2);
        result = (result) | (a2);
        a2 = result;
        a2 = (a2) >> (32);
    }
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
    }
    v_stack_m60 = 5;
    result = HalpInterruptSendIpi(v_stack_m60, 47, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    goto loc_0021CDAE;
loc_0021CFDB:
    if (((*(unsigned __int8 *)(v_stack_p8 + 35)) & (32)) == 0) goto loc_0021CBED;
    result = KiIsThreadExemptFromForcePark(v_stack_p18, 47, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    if ((unsigned __int8)(result) != 0) goto loc_0021CBED;
    result = KiArmForceParkDutyCyclingForSharedReadyQueue(v_stack_p8, v_stack_p10, *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    goto loc_0021CBED;
loc_0021D006:
    goto loc_0021CBC6;
loc_0021D021:
    result = KiCheckMaxOverQuotaTransition(v_stack_p10, (unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(gs_base + (0 + 32)), (unsigned __int8)(result));
    if ((unsigned __int8)(result) != 0) goto loc_0021D11B;
    if ((*(unsigned __int64 *)(v_stack_p10)) < (*(unsigned __int64 *)(v_stack_p10 + 24))) goto loc_0021C867;
    if (((*(unsigned __int8 *)(v_stack_p10 + 112)) & (2)) != 0) goto loc_0021C867;
    result = KiRecomputeGroupSchedulingRank((unsigned int)((unsigned int)(result)), v_stack_p10, v_stack_p18, (unsigned __int8)(result));
    goto loc_0021C867;
loc_0021D05E:
    *(unsigned __int64 *)(result) = (unsigned int)((unsigned int)(result));
    *(unsigned __int64 *)(result + 8) = (unsigned int)((unsigned int)(result));
    *(unsigned __int64 *)((unsigned int)((unsigned int)(result))) = result;
    *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 8) = result;
    goto loc_0021CB9E;
loc_0021D071:
    goto loc_0021CAB2;
loc_0021D084:
    goto loc_0021C8FD;
loc_0021D08C:
    goto loc_0021CAF5;
loc_0021D094:
loc_0021D097:
    a1 = ((unsigned int)((unsigned int)(result)) - 432) - ((unsigned int)(*(unsigned int *)(v_stack_p8 + 216)));
    a4 = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)((unsigned int)(result)) - 320)) >> (1));
    a4 = (unsigned __int8)((a4) & ((unsigned __int8)(v_stack_p10)));
    result = EtwTraceScbRankChange(a1, (unsigned int)(*(unsigned int *)(v_stack_p8 + 36)), (unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) - 308)), a4);
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result))) != 0) goto loc_0021D097;
    a2 = 0;
loc_0021D0D2:
    if (condition_is_above_or_equal) goto loc_0021D0F6;
loc_0021D0DB:
    v_rbx = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14320073)) & ((unsigned int)(v_rbx))) == 0) goto loc_0021D215;
loc_0021D0E9:
loc_0021D0EB:
    if (*(unsigned __int64 *)(v_stack_p8 + 48) == 0) goto loc_0021D0D2;
    goto loc_0021D0DB;
loc_0021D0F6:
    a2 = 0;
loc_0021D100:
    *(unsigned __int64 *)((unsigned int)((unsigned int)(result))) = 0;
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result))) == 0) goto loc_0021D2D6;
    goto loc_0021D100;
loc_0021D11B:
    if (((*(unsigned __int8 *)(v_rbx + 112)) & (1)) == 0) goto loc_0021C867;
    result = KiRemoveSchedulingGroupQueue(v_stack_p18, v_rbx, 1, a4);
    goto loc_0021C867;
loc_0021D138:
    if (((unsigned int)(v_stack_p8)) == (*(unsigned int *)(v_rbx + 124))) goto loc_0021D277;
loc_0021D142:
    *(unsigned __int64 *)(v_rbx + 432) = (unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(v_stack_p8 + 195))));
    goto loc_0021C877;
loc_0021D15E:
    result = KiComputeThreadAffinity(v_stack_p18, v_rbx, 1, a4);
    if ((unsigned int)(result) == 0) goto loc_0021CF3B;
    result = KiCheckPrcbAffinityEx(*(unsigned __int64 *)(v_stack_p18 + 576), v_stack_p8, 1, a4);
loc_0021D18E:
loc_0021D191:
    a1 = (*(unsigned __int64 *)((unsigned int)((unsigned int)(result))) - 432) - ((unsigned int)(*(unsigned int *)(v_stack_p8 + 216)));
    a4 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result))) - 320)) >> (1));
    a4 = (unsigned __int8)((a4) & ((unsigned __int8)(v_stack_p10)));
    result = EtwTraceScbRankChange(a1, (unsigned int)(*(unsigned int *)(v_stack_p8 + 36)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result))) - 308)), a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)))) != 0) goto loc_0021D191;
    result = 0;
loc_0021D1D0:
    if (condition_is_above_or_equal) goto loc_0021D1F0;
loc_0021D1D9:
    v_rbx = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14319819)) & ((unsigned int)(v_rbx))) == 0) goto loc_0021D23C;
loc_0021D1E3:
loc_0021D1E5:
    if (*(unsigned __int64 *)(v_stack_p8 + 48) == 0) goto loc_0021D1D0;
    goto loc_0021D1D9;
loc_0021D1F0:
    a2 = 0;
loc_0021D1FA:
    *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)))) = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)))) == 0) goto loc_0021D2E0;
    goto loc_0021D1FA;
loc_0021D215:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14325917)))) & (64)) == 0) goto loc_0021D0E9;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)(0xFEFFULL), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result))) - 308)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0021D0E9;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result))) - 308)), a4);
    goto loc_0021D0EB;
loc_0021D23C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14325878)))) & (64)) == 0) goto loc_0021D1E3;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result))) - 308)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0021D1E3;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result))) - 308)), a4);
    goto loc_0021D1E5;
loc_0021D258:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m80))) + (*(unsigned int *)(*(unsigned __int64 *)(a4 + 128))));
loc_0021D262:
    if (*(unsigned __int64 *)(a4 + 416) == 0) goto loc_0021CC7A;
    goto loc_0021CC64;
loc_0021D277:
    result = 0;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(v_rbx + 112)) >> (1));
    a1 = (unsigned __int16)((a1) & (1));
    result = ((unsigned __int16)(v_stack_p10) != 0) ? 1 : 0;
    if (((unsigned __int16)(result)) == ((unsigned __int16)(a1))) goto loc_0021C877;
    goto loc_0021D142;
loc_0021D299:
    goto loc_0021CC83;
loc_0021D2A4:
    goto loc_0021CD44;
loc_0021D2B6:
    a4 = 0;
    result = EtwTraceReadyQueueInsertion(v_stack_p18, (unsigned int)(*(unsigned int *)(v_stack_p8 + 36)), (unsigned int)((unsigned int)(v_r11)), a4);
    goto loc_0021CDA1;
loc_0021D2D6:
    goto loc_0021CDAE;
loc_0021D2E0:
    goto loc_0021C98A;
loc_0021D2EA:
    goto loc_0021CA05;
loc_0021D2F6:
    a4 = 0;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18 + 116))) >> (3));
    a3 = (unsigned __int8)((a3) & (1));
    v_stack_p28 = 0x536ULL;
    v_stack_p20 = *(unsigned __int64 *)(v_stack_p18 + 576);
    result = EtwTraceThreadAffinity(v_stack_p18, *(unsigned __int16 *)(v_stack_p18 + 584), a3, a4);
    goto loc_0021CDB8;
loc_0021D32D:
    if (((*(unsigned int *)(v_rip + 14325721)) & (0x8000000ULL)) == 0) goto loc_0021CDC9;
    result = EtwTraceIdealProcessor(v_stack_p18, (unsigned int)(0x546ULL), a3, a4);
    goto loc_0021CDC9;
}
```

## 5. (Beta) C Style

```c
int64_t KiQueueReadyThread(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m5C;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint8_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint16_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (152);
    local_rsi = 0;
    v_stack_m88 = 0xFFFFFFFFULL;
    v_stack_m8C = 0xFFFFFFFFULL;
    v_stack_m90 = 0;
    v_stack_m80 = 0;
    v_stack_p20 = (uint32_t)(*(uint8_t *)(arg3 + 0x235));
    if ((*(uint64_t *)(arg3 + 0x238)) != (*(uint64_t *)(v_rip + 0xDAA414))) goto loc_0021CE95;
loc_0021C81C:
    if ((*(uint64_t *)(arg3 + 0x48)) >= (*(uint64_t *)(arg3 + 0x20))) goto loc_0021CEA1;
loc_0021C826:
    if (*(uint64_t *)(arg3 + 0x68) == 0) goto loc_0021C8A1;
    local_rbx = ((uint32_t)(*(uint32_t *)(arg1 + 0xD8))) + (*(uint64_t *)(arg3 + 0x68));
loc_0021C840:
    local_r14 = (uint16_t)(((uint16_t)(*(uint16_t *)(local_rbx + 0x70))) & (2));
    if ((((uint8_t)(*(uint16_t *)(local_rbx + 0x70))) & (4)) != 0) goto loc_0021D021;
    result = KiComputeGroupSchedulingRank(*(uint64_t *)(arg3 + 0x68), v_stack_p8, Arg3, local_rbx);
loc_0021C867:
    if (((*(uint32_t *)(v_rip + 0xDAA2A3)) & (0x4000ULL)) != 0) goto loc_0021D138;
loc_0021C877:
    local_rsi = (uint32_t)((local_rsi) + (*(uint32_t *)(local_rbx + 0x7C)));
    if (*(uint64_t *)(local_rbx + 0x1A0) == 0) goto loc_0021CDE7;
    local_rdi = (*(uint64_t *)(local_rbx + 0x1A0)) - ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xD8)));
    goto loc_0021C840;
loc_0021C899:
loc_0021C8A1:
    local_rdi = 0;
    if (((uint32_t)((int8_t)(*(uint8_t *)(v_stack_p8 + 0xC3)))) < (*(uint32_t *)(v_rip + 0xDA8ACF))) goto loc_0021CC09;
loc_0021C8B9:
    if (*(uint64_t *)(v_stack_p8 + 0x68) == 0) goto loc_0021C8D5;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xD8))) + (*(uint64_t *)(v_stack_p8 + 0x68));
    result = KiCheckForMaxOverQuotaScb(Arg1, 0, Arg3, local_rbx);
    if ((uint8_t)(result) != 0) goto loc_0021C900;
loc_0021C8D5:
    if (((uint16_t)(*(uint8_t *)(v_stack_p8 + 0xD0))) >= (*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x240)))) goto loc_0021D084;
loc_0021C8FD:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xC0) + 0x8)) & (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x240) + *(uint8_t *)(v_stack_p8 + 0xD0) * 8 + 0x8));
loc_0021C900:
    if (((*(uint32_t *)(v_stack_p8 + 0x78)) & (0x1000ULL)) != 0) goto loc_0021C913;
    if (Arg2 == 0) goto loc_0021CA42;
loc_0021C913:
    result = KiEnterDeferredReadyState(v_stack_p8, Arg2, *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x240) + *(uint8_t *)(v_stack_p8 + 0xD0) * 8 + 0x8), local_rbx);
    a4 = (*(uint64_t *)(v_stack_p10)) & (-2);
    v_stack_m68 = a4;
    Arg1 = (uint32_t)((*(uint64_t *)(v_stack_p10)) & (1));
    if (condition_is_equal) goto loc_0021CE42;
    if (((uint32_t)(Arg1)) == 1) {
        result = *(uint64_t *)(a4 + 0x8E58);
        Arg3 = *(uint64_t *)(a4 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_0021C972;
loc_0021C960:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_0021C960;
loc_0021C972:
    result = 0;
    *(uint64_t *)(v_stack_p10) = 0;
    if (v_stack_m80 != 0) goto loc_0021D18E;
    Arg2 = 0;
loc_0021C98A:
    v_stack_mA8 = 0;
    *(uint8_t *)(v_stack_p8 + 0x235) = 0;
    a4 = 0;
    result = KiDeferredReadySingleThread(v_stack_p8, v_stack_p8, v_stack_mA8, a4);
    if (v_stack_mA8 == 0) goto loc_0021D2EA;
    v_stack_mA8 = *(uint64_t *)(v_stack_mA8);
loc_0021C9C2:
    a4 = 0;
    result = KiDeferredReadySingleThread(v_stack_p8, v_stack_mA8 - 216, v_stack_mA8, a4);
    local_r14 = (uint32_t)((1) + 1);
    if (v_stack_mA8 != 0) {
        result = *(uint64_t *)(v_stack_mA8);
        v_stack_mA8 = result;
    }
    if ((((uint8_t)(local_r14)) & (15)) == 0) {
        Arg1 = v_stack_p8 + 13784;
        result = KiFlushSoftwareInterruptBatch(Arg1, v_stack_mA8 - 216, v_stack_mA8, a4);
    }
    if (v_stack_mA8 != 0) goto loc_0021C9C2;
loc_0021CA05:
    result = KiFlushSoftwareInterruptBatch(v_stack_p8 + 13784, v_stack_mA8 - 216, v_stack_mA8, a4);
    if (*(uint64_t *)(v_stack_p8 + 0x10) != 0) goto loc_0021CDAE;
    if ((*(uint64_t *)(v_stack_p8 + 0x8)) == (*(uint64_t *)(v_stack_p8 + 0x18))) goto loc_0021CDAE;
    if ((*(uint64_t *)(v_stack_p8 + 0x10)) == (*(uint64_t *)(v_stack_p8 + 0x10))) goto loc_0021CDAE;
    if ((*(uint8_t *)(v_stack_p8 + 0x20)) == ((uint8_t)(*(uint64_t *)(v_stack_p8 + 0x10)))) goto loc_0021CF5C;
    *(uint8_t *)(v_stack_p8 + 0x6) = 1;
    goto loc_0021CDAE;
loc_0021CA42:
    *(uint8_t *)(v_stack_p8 + 0x235) = (uint8_t)(v_stack_p8 + 13784);
    *(uint32_t *)(v_stack_p8 + 0x1B4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x18))));
    if (*(uint64_t *)(v_stack_p8 + 0x68) == 0) goto loc_0021CE3A;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xD8))) + (*(uint64_t *)(v_stack_p8 + 0x68));
loc_0021CA73:
    if (*(uint64_t *)(v_stack_p8 + 0x8EB8) != 0) {
        *(uint8_t *)(*(uint64_t *)(v_stack_p8 + 0x8EB8) + 0x10) = (uint8_t)(v_stack_p8 + 13784);
    }
    local_rbx = 0;
    *(uint8_t *)(v_stack_p8 + 0x184) = 1;
    if (Arg2 != 0) goto loc_0021CC19;
loc_0021CA9C:
    if (((*(uint32_t *)(v_stack_p8 + 0x78)) & (0x400000ULL)) != 0) goto loc_0021D071;
loc_0021CAB2:
    result = KiUpdateVpBackingThreadPriorityOnReadyQueueInsertion(v_stack_p8, Arg2, v_stack_mA8, a4);
    if (((*(uint32_t *)(v_stack_p8 + 0x78)) & (0x2000ULL)) == 0) goto loc_0021CCA5;
    if (*(uint64_t *)(v_stack_p8 + 0x8E40) == 0) goto loc_0021CCA5;
    if (((uint16_t)(*(uint8_t *)(v_stack_p8 + 0xD0))) >= (*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x240)))) goto loc_0021D08C;
loc_0021CAF5:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x240) + *(uint8_t *)(v_stack_p8 + 0xD0) * 8 + 0x8)) & (*(uint64_t *)(v_stack_p8 + 0x8E40));
    if (Arg1 != (*(uint64_t *)(v_stack_p8 + 0x8E40))) goto loc_0021CCA5;
    if (0 != 0) goto loc_0021CCA5;
    local_rdi = ((int8_t)(*(uint8_t *)(v_stack_p8 + 0xC3)) + 4) << (4);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_stack_p8 + 0x8E48));
    v_stack_mA0 = v_xmm0;
    if (((*(uint32_t *)(v_rip + 0xDAA010)) & (0x200000ULL)) == 0) goto loc_0021CB6B;
    v_stack_m98 = *(uint64_t *)(v_stack_p8 + 0x8E48);
    v_stack_mA0 = 0;
    if (v_stack_mA0 != 0) goto loc_0021CF4E;
loc_0021CB4B:
    if (0 != 0) goto loc_0021CB7F;
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8))) == local_rdi) goto loc_0021D05E;
loc_0021CB64:
loc_0021CB6B:
    v_stack_m78 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8))) >= local_rdi) goto loc_0021CB4B;
loc_0021CB7F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi) + 0x8)) != local_rdi) goto loc_0021CB64;
    *(uint64_t *)(v_stack_p8 + 0xD8) = *(uint64_t *)(local_rdi);
    *(uint64_t *)(v_stack_p8 + 0xD8 + 0x8) = local_rdi;
    *(uint64_t *)(*(uint64_t *)(local_rdi) + 0x8) = v_stack_p8 + 216;
    *(uint64_t *)(local_rdi) = v_stack_p8 + 216;
loc_0021CB9E:
    *(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x8E48) + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x8E48) + 0x8)));
    *(uint32_t *)(v_stack_p8 + 0x218) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x218)));
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x8E48) + 0xC)) == 1) goto loc_0021D006;
loc_0021CBC6:
    *(uint32_t *)(v_stack_p8 + 0x6F8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x54)));
    result = KiUpdateSoftParkElectionStatisticsOnInsertion(*(uint64_t *)(v_stack_p8 + 0x8E48), v_stack_p8, v_stack_mA8, a4);
    result = KeIsForceParkingEnabled(*(uint64_t *)(v_stack_p8 + 0x8E48), v_stack_p8, v_stack_mA8, a4);
    if ((uint8_t)(result) != 0) goto loc_0021CFDB;
loc_0021CBED:
    if (((*(uint32_t *)(v_rip + 0xDA9F41)) & (0x200000ULL)) != 0) goto loc_0021CCE3;
    local_rdi = 0;
    goto loc_0021CD2E;
loc_0021CC09:
    if (((*(uint8_t *)(v_stack_p8 + 0x23)) & (16)) == 0) goto loc_0021C900;
    goto loc_0021C8B9;
loc_0021CC19:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x78)))) & (0xC00ULL)) != 0) goto loc_0021CA9C;
    if ((*(uint8_t *)(v_stack_p8 + 0xC3)) >= 16) goto loc_0021CC83;
    if ((*(uint8_t *)(v_stack_p8 + 0xC3)) < 16) goto loc_0021CC83;
    result = KiShouldPreemptionBeDeferred(v_stack_p8, v_stack_p8, 0, v_stack_p8);
    if ((uint8_t)(result) != 0) goto loc_0021CC83;
    result = KiCheckForMaxOverQuotaScb(v_stack_p8, v_stack_p8, 0, v_stack_p8);
    if ((uint8_t)(result) != 0) goto loc_0021D299;
loc_0021CC64:
    Arg3 = (uint32_t)((0) + (*(uint32_t *)(v_stack_p8 + 0x7C)));
    if (*(uint64_t *)(v_stack_p8 + 0x80) != 0) goto loc_0021D258;
    if ((uint32_t)(Arg3) == 0) goto loc_0021D262;
loc_0021CC7A:
    local_rbx = *(uint64_t *)(v_stack_p8 + 0x8E48);
    if (0 != 0) {
        local_rbx = 1;
    }
    if ((uint32_t)(Arg3) == 0) goto loc_0021CA9C;
    result = KiAddThreadToScbQueue(v_stack_p8, v_stack_p8, v_stack_p8, 0);
    goto loc_0021CD31;
loc_0021CCA5:
    result = ((int8_t)(*(uint8_t *)(v_stack_p8 + 0xC3)) + 2116) << (4);
    result = (result) + (v_stack_p8);
    if (0 != 0) goto loc_0021CE4E;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_0021CB64;
    *(uint64_t *)(v_stack_p8 + 0xD8) = result;
    *(uint64_t *)(v_stack_p8 + 0xD8 + 0x8) = *(uint64_t *)(result + 0x8);
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = v_stack_p8 + 216;
    *(uint64_t *)(result + 0x8) = v_stack_p8 + 216;
    goto loc_0021CE71;
loc_0021CCE3:
    local_rdi = 0;
    if (v_stack_mA0 != 0) goto loc_0021CD11;
    if (v_stack_mA0 == v_stack_mA0) goto loc_0021CD2E;
    result = KxWaitForLockChainValid(v_stack_mA0, *(uint64_t *)(result + 0x8), v_stack_p8, 0);
loc_0021CD11:
    v_stack_mA0 = 0;
    result = (uint8_t)((v_stack_m98) ^ ((uint8_t)(v_stack_m98)));
    if ((((uint8_t)(result)) & (4)) != 0) {
        result = KeWakeAddressAll(result + 8, v_stack_m98, v_stack_p8, 0);
    }
loc_0021CD31:
    local_r10 = 0;
    if (((*(uint32_t *)(v_rip + 0xDA9DD6)) & (0x800ULL)) != 0) goto loc_0021D2A4;
loc_0021CD44:
    a4 = (*(uint64_t *)(v_stack_p10)) & (-2);
    v_stack_m70 = a4;
    Arg2 = (uint32_t)((*(uint64_t *)(v_stack_p10)) & (1));
    if (condition_is_equal) goto loc_0021CDDE;
    result = 0;
    if (((uint32_t)(Arg2)) == 1) {
        result = *(uint64_t *)(a4 + 0x8E58);
        Arg3 = *(uint64_t *)(a4 + 0x8E58);
        Arg3 = (Arg3) + (8);
        result = *(uint8_t *)(result);
    }
    if ((uint32_t)(result) == 0) goto loc_0021CD93;
loc_0021CD80:
    if ((uint32_t)(result - 1) != 0) goto loc_0021CD80;
loc_0021CD93:
    result = 0;
    *(uint64_t *)(v_stack_p10) = 0;
    if (0 != 0) goto loc_0021D2B6;
loc_0021CDA1:
    if (v_stack_m80 != 0) goto loc_0021D094;
loc_0021CDAE:
    if (v_stack_m90 != 0) goto loc_0021D2F6;
loc_0021CDB8:
    if (((uint32_t)((uint32_t)(v_stack_m88))) != ((uint32_t)((uint32_t)(v_stack_m8C)))) goto loc_0021D32D;
loc_0021CDC9:
    local_rsp = (local_rsp) + (152);
    return result;
loc_0021CDDE:
    goto loc_0021CD80;
loc_0021CDE7:
    v_stack_m80 = 0;
    result = KiIsThreadConstrainedBySchedulingGroup(v_stack_p18, *(uint64_t *)(arg3 + result - 0x1 * 8), v_stack_m70, (uint32_t)(v_stack_m8C));
    if ((uint8_t)(result) == 0) goto loc_0021C899;
    result = KiShouldPreemptionBeDeferred(v_stack_p18, *(uint64_t *)(arg3 + result - 0x1 * 8), v_stack_m70, (uint32_t)(v_stack_m8C));
    if ((uint8_t)(result) == 0) goto loc_0021C899;
    if ((uint32_t)((int8_t)(*(uint8_t *)(v_stack_p8 + 0xC3))) == 0) goto loc_0021C899;
    if (((*(uint32_t *)(v_stack_p18 + 0x78)) & (0xC00ULL)) != 0) goto loc_0021C8A1;
    goto loc_0021C8A1;
loc_0021CE3A:
    goto loc_0021CA73;
loc_0021CE42:
    goto loc_0021C960;
loc_0021CE4E:
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) != result) goto loc_0021CB64;
    *(uint64_t *)(v_stack_p18) = *(uint64_t *)(result);
    *(uint64_t *)(v_stack_p18 + 0x8) = result;
    *(uint64_t *)(*(uint64_t *)(result) + 0x8) = v_stack_p18;
    *(uint64_t *)(result) = v_stack_p18;
loc_0021CE71:
    *(uint32_t *)(v_stack_p8 + 0x83D8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x83D8)));
    result = KiUpdateLocalReadyQueueStatisticsOnInsertion(v_stack_p8, v_stack_p18, v_stack_m68, (uint32_t)(v_stack_m8C));
    goto loc_0021CD31;
loc_0021CE95:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m68 + 0x74)))) & (8)) != 0) goto loc_0021C81C;
loc_0021CEA1:
    if (condition_is_above_or_equal) goto loc_0021CEB6;
    goto loc_0021C826;
loc_0021CEB6:
    v_stack_m88 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68 + 0x24C)));
    if (v_stack_p10 < (*(uint64_t *)(v_stack_m68 + 0x20))) goto loc_0021CF2B;
    result = KiComputeNewPriority(v_stack_p18, v_stack_p18, 1, (uint32_t)(v_stack_m8C));
    a4 = 0;
    Arg2 = 0;
    result = KiUpdateVPBackingThreadPriority(v_stack_p18, Arg2, 1, a4);
    if ((uint8_t)(result) == 0) {
        a4 = (uint32_t)((uint32_t)((uint32_t)(result)));
        v_stack_p20 = (uint8_t)((int8_t)(*(uint8_t *)(v_stack_p8 + 0xC3)));
        Arg3 = v_stack_p18;
        Arg1 = 0;
        result = KiUpdateThreadPriority(Arg1, Arg2, Arg3, a4);
    }
    result = KiQueryQuantumReset(v_stack_p18, Arg2, Arg3, a4);
    result = (uint32_t)((result) * (*(uint32_t *)(v_rip + 0xDA8193)));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (v_stack_p10);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x78)))) & (32)) != 0) {
    }
    *(void **)(v_stack_p18 + 0x20) = Arg1;
    result = KiTryScheduleNextForegroundBoost(v_stack_p18, Arg2, Arg3, a4);
    v_stack_p20 = (uint32_t)((int8_t)(*(uint8_t *)(v_stack_p8 + 0xC3)));
loc_0021CF2B:
    result = KiCheckThreadAffinity(v_stack_p18, Arg2, Arg3, a4);
    if ((uint32_t)(result) == 0) goto loc_0021D15E;
loc_0021CF3B:
    v_stack_m8C = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x24C)));
    *(uint64_t *)(v_stack_p18 + 0x40) = (int8_t)(*(uint8_t *)(v_stack_p8 + 0xC3));
    goto loc_0021C826;
loc_0021CF4E:
    result = KxWaitForLockOwnerShip(v_stack_mA0, Arg2, Arg3, a4);
    goto loc_0021CB4B;
loc_0021CF5C:
    result = 0;
    v_stack_m5C = v_xmm0;
    if ((*(uint8_t *)(v_rip + 0xDA9C5E)) == 0) goto loc_0021CFC1;
    result = HalpDisableInterrupts(v_stack_mA0, Arg2, *(uint64_t *)(gs_base + (0 + 0x20)), a4);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8))))) | (4));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8) = (uint32_t)(Arg1);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8))) == 0) {
        Arg1 = 0xC0010015ULL;
        Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA8))) << (32);
        result = (result) | (Arg2);
        result = (result) | (Arg2);
        Arg2 = result;
        Arg2 = (Arg2) >> (32);
    }
    if ((uint8_t)((uint8_t)(result)) != 0) {
    }
    v_stack_m60 = 5;
    result = HalpInterruptSendIpi(v_stack_m60, 47, *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    goto loc_0021CDAE;
loc_0021CFDB:
    if (((*(uint8_t *)(v_stack_p8 + 0x23)) & (32)) == 0) goto loc_0021CBED;
    result = KiIsThreadExemptFromForcePark(v_stack_p18, 47, *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    if ((uint8_t)(result) != 0) goto loc_0021CBED;
    result = KiArmForceParkDutyCyclingForSharedReadyQueue(v_stack_p8, v_stack_p10, *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    goto loc_0021CBED;
loc_0021D006:
    goto loc_0021CBC6;
loc_0021D021:
    result = KiCheckMaxOverQuotaTransition(v_stack_p10, (uint32_t)((uint32_t)(result)), *(uint64_t *)(gs_base + (0 + 0x20)), (uint8_t)(result));
    if ((uint8_t)(result) != 0) goto loc_0021D11B;
    if ((*(uint64_t *)(v_stack_p10)) < (*(uint64_t *)(v_stack_p10 + 0x18))) goto loc_0021C867;
    if (((*(uint8_t *)(v_stack_p10 + 0x70)) & (2)) != 0) goto loc_0021C867;
    result = KiRecomputeGroupSchedulingRank((uint32_t)((uint32_t)(result)), v_stack_p10, v_stack_p18, (uint8_t)(result));
    goto loc_0021C867;
loc_0021D05E:
    *(uint64_t *)(result) = (uint32_t)((uint32_t)(result));
    *(uint64_t *)(result + 0x8) = (uint32_t)((uint32_t)(result));
    *(uint64_t *)((uint32_t)((uint32_t)(result))) = result;
    *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x8) = result;
    goto loc_0021CB9E;
loc_0021D071:
    goto loc_0021CAB2;
loc_0021D084:
    goto loc_0021C8FD;
loc_0021D08C:
    goto loc_0021CAF5;
loc_0021D094:
loc_0021D097:
    Arg1 = ((uint32_t)((uint32_t)(result)) - 432) - ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xD8)));
    a4 = (uint8_t)((*(uint8_t *)((uint32_t)((uint32_t)(result)) - 0x140)) >> (1));
    a4 = (uint8_t)((a4) & ((uint8_t)(v_stack_p10)));
    result = EtwTraceScbRankChange(Arg1, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x24)), (uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) - 0x134)), a4);
    if (*(uint64_t *)((uint32_t)((uint32_t)(result))) != 0) goto loc_0021D097;
    Arg2 = 0;
loc_0021D0D2:
    if (condition_is_above_or_equal) goto loc_0021D0F6;
loc_0021D0DB:
    local_rbx = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xDA81C9)) & ((uint32_t)(local_rbx))) == 0) goto loc_0021D215;
loc_0021D0E9:
loc_0021D0EB:
    if (*(uint64_t *)(v_stack_p8 + 0x30) == 0) goto loc_0021D0D2;
    goto loc_0021D0DB;
loc_0021D0F6:
    Arg2 = 0;
loc_0021D100:
    *(uint64_t *)((uint32_t)((uint32_t)(result))) = 0;
    if (*(uint64_t *)((uint32_t)((uint32_t)(result))) == 0) goto loc_0021D2D6;
    goto loc_0021D100;
loc_0021D11B:
    if (((*(uint8_t *)(local_rbx + 0x70)) & (1)) == 0) goto loc_0021C867;
    result = KiRemoveSchedulingGroupQueue(v_stack_p18, local_rbx, 1, a4);
    goto loc_0021C867;
loc_0021D138:
    if (((uint32_t)(v_stack_p8)) == (*(uint32_t *)(local_rbx + 0x7C))) goto loc_0021D277;
loc_0021D142:
    *(uint64_t *)(local_rbx + 0x1B0) = (uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(v_stack_p8 + 0xC3))));
    goto loc_0021C877;
loc_0021D15E:
    result = KiComputeThreadAffinity(v_stack_p18, local_rbx, 1, a4);
    if ((uint32_t)(result) == 0) goto loc_0021CF3B;
    result = KiCheckPrcbAffinityEx(*(uint64_t *)(v_stack_p18 + 0x240), v_stack_p8, 1, a4);
loc_0021D18E:
loc_0021D191:
    Arg1 = (*(uint64_t *)((uint32_t)((uint32_t)(result))) - 432) - ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xD8)));
    a4 = (uint8_t)((*(uint8_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result))) - 0x140)) >> (1));
    a4 = (uint8_t)((a4) & ((uint8_t)(v_stack_p10)));
    result = EtwTraceScbRankChange(Arg1, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x24)), (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result))) - 0x134)), a4);
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)))) != 0) goto loc_0021D191;
    result = 0;
loc_0021D1D0:
    if (condition_is_above_or_equal) goto loc_0021D1F0;
loc_0021D1D9:
    local_rbx = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xDA80CB)) & ((uint32_t)(local_rbx))) == 0) goto loc_0021D23C;
loc_0021D1E3:
loc_0021D1E5:
    if (*(uint64_t *)(v_stack_p8 + 0x30) == 0) goto loc_0021D1D0;
    goto loc_0021D1D9;
loc_0021D1F0:
    Arg2 = 0;
loc_0021D1FA:
    *(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)))) = 0;
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)))) == 0) goto loc_0021D2E0;
    goto loc_0021D1FA;
loc_0021D215:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDA989D)))) & (64)) == 0) goto loc_0021D0E9;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)(0xFEFFULL), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result))) - 0x134)), a4);
    if ((uint8_t)(result) == 0) goto loc_0021D0E9;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result))) - 0x134)), a4);
    goto loc_0021D0EB;
loc_0021D23C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xDA9876)))) & (64)) == 0) goto loc_0021D1E3;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result))) - 0x134)), a4);
    if ((uint8_t)(result) == 0) goto loc_0021D1E3;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result))) - 0x134)), a4);
    goto loc_0021D1E5;
loc_0021D258:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m80))) + (*(uint32_t *)(*(uint64_t *)(a4 + 0x80))));
loc_0021D262:
    if (*(uint64_t *)(a4 + 0x1A0) == 0) goto loc_0021CC7A;
    goto loc_0021CC64;
loc_0021D277:
    result = 0;
    Arg1 = (uint16_t)((*(uint16_t *)(local_rbx + 0x70)) >> (1));
    Arg1 = (uint16_t)((Arg1) & (1));
    result = ((uint16_t)(v_stack_p10) != 0) ? 1 : 0;
    if (((uint16_t)(result)) == ((uint16_t)(Arg1))) goto loc_0021C877;
    goto loc_0021D142;
loc_0021D299:
    goto loc_0021CC83;
loc_0021D2A4:
    goto loc_0021CD44;
loc_0021D2B6:
    a4 = 0;
    result = EtwTraceReadyQueueInsertion(v_stack_p18, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x24)), (uint32_t)((uint32_t)(local_r11)), a4);
    goto loc_0021CDA1;
loc_0021D2D6:
    goto loc_0021CDAE;
loc_0021D2E0:
    goto loc_0021C98A;
loc_0021D2EA:
    goto loc_0021CA05;
loc_0021D2F6:
    a4 = 0;
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x74))) >> (3));
    Arg3 = (uint8_t)((Arg3) & (1));
    v_stack_p28 = 0x536ULL;
    v_stack_p20 = *(uint64_t *)(v_stack_p18 + 0x240);
    result = EtwTraceThreadAffinity(v_stack_p18, *(uint16_t *)(v_stack_p18 + 0x248), Arg3, a4);
    goto loc_0021CDB8;
loc_0021D32D:
    if (((*(uint32_t *)(v_rip + 0xDA97D9)) & (0x8000000ULL)) == 0) goto loc_0021CDC9;
    result = EtwTraceIdealProcessor(v_stack_p18, (uint32_t)(0x546ULL), Arg3, a4);
    goto loc_0021CDC9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD8` | `32` | `R` |
| `Arg3` | `+ 0x20` | `64` | `R` |
| `Arg3` | `+ 0x20` | `64` | `W` |
| `Arg3` | `+ 0x40` | `64` | `R/W` |
| `Arg3` | `+ 0x40` | `64` | `W` |
| `Arg3` | `+ 0x48` | `64` | `R` |
| `Arg3` | `+ 0x68` | `64` | `R` |
| `Arg3` | `+ 0x74` | `32` | `R` |
| `Arg3` | `+ 0x78` | `32` | `R` |
| `Arg3` | `+ 0x78` | `32` | `R/W` |
| `Arg3` | `+ 0x235` | `8` | `R` |
| `Arg3` | `+ 0x238` | `64` | `R` |
| `Arg3` | `+ 0x240` | `64` | `R` |
| `Arg3` | `+ 0x24C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0021C7B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
