# sub_0025308F

- RVA: `0x0025308F`–`0x00254457` (길이 `5,064` bytes)
- VA: `0x000000014025308F`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063724`
- 디코드: `1,168`개 명령, `5,064/5,064` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **20**

### Outgoing calls
- `0x00253116` → [KiComputeNewPriority](../3C/KiComputeNewPriority_function_003C2D8C.md) (function, `0x003C2D8C`)
- `0x00253195` → [KiComputeThreadQos](KiComputeThreadQos_function_00258010.md) (function, `0x00258010`)
- `0x002531D6` → [KiComputeThreadQos](KiComputeThreadQos_function_00258010.md) (function, `0x00258010`)
- `0x0025334B` → [KiChooseTargetProcessor](KiChooseTargetProcessor_function_002556D8.md) (function, `0x002556D8`)
- `0x002533F9` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00253672` → [KiIsPrcbThread](../35/KiIsPrcbThread_function_00353230.md) (function, `0x00353230`)
- `0x002537B1` → [KeFindFirstSetLeftAffinityEx](../45/KeFindFirstSetLeftAffinityEx_function_004530E0.md) (function, `0x004530E0`)
- `0x0025389C` → [KiIsIsolationUnitIdleByHandle](KiIsIsolationUnitIdleByHandle_function_00256C70.md) (function, `0x00256C70`)
- `0x002538B6` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002538C2` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00253A0D` → [KiIsQosGroupingClass](../39/KiIsQosGroupingClass_function_00392430.md) (function, `0x00392430`)
- `0x00253A6A` → [RtlCopyVolatileMemory](../6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x00253A7D` → [KeIsEmptyGroupMask](KeIsEmptyGroupMask_function_002553B0.md) (function, `0x002553B0`)
- `0x00253ACA` → [KeIsEmptyGroupMask](KeIsEmptyGroupMask_function_002553B0.md) (function, `0x002553B0`)
- `0x00253B21` → [KiHeteroSelectIdleProcessorFromSubNode](KiHeteroSelectIdleProcessorFromSubNode_function_00255504.md) (function, `0x00255504`)
- `0x00253D15` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00253D24` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00253DA8` → [KiHeteroSelectProcessorToPreempt](KiHeteroSelectProcessorToPreempt_function_002560D0.md) (function, `0x002560D0`)
- `0x00253E03` → [KiAttemptToScheduleThreadToBusyIsolationUnit](KiAttemptToScheduleThreadToBusyIsolationUnit_function_00259B00.md) (function, `0x00259B00`)
- `0x00253F17` → [KeAddProcessorAffinityEx](KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00253F2D` → [KeAddGroupAffinityEx](KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x00253FC9` → [EtwTraceXSchedulerPriorityKickSend](../4F/EtwTraceXSchedulerPriorityKickSend_function_004FB2C0.md) (function, `0x004FB2C0`)
- `0x00253FFA` → [EtwTraceScheduleThread](../30/EtwTraceScheduleThread_function_0030B74C.md) (function, `0x0030B74C`)
- `0x002540A8` → [KiHeteroAttemptPreemptionSwapOnSubNode](../3C/KiHeteroAttemptPreemptionSwapOnSubNode_function_003C1144.md) (function, `0x003C1144`)
- `0x00254184` → [KiIsIsolationUnitIdleByHandle](KiIsIsolationUnitIdleByHandle_function_00256C70.md) (function, `0x00256C70`)
- `0x00254239` → [KiUpdateVpBackingThreadPriorityOnReadyQueueInsertion](../21/KiUpdateVpBackingThreadPriorityOnReadyQueueInsertion_function_0021D360.md) (function, `0x0021D360`)
- `0x002542DA` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002542EA` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00254375` → [Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline](../4E/Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline_function_004EF7C0.md) (function, `0x004EF7C0`)
- `0x0025439D` → [Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline](../4E/Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline_function_004EF7C0.md) (function, `0x004EF7C0`)
- `0x002543B8` → [KiComputeThreadPriority](../3C/KiComputeThreadPriority_function_003C45F4.md) (function, `0x003C45F4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0025315E` → RVA `0x00FC50A0` (`ALMOSTRO`; read)
- `0x002531EA` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x002531F6` → RVA `0x00FC6B38` (`ALMOSTRO`; read)
- `0x00253209` → RVA `0x00FC6AF5` (`ALMOSTRO`; read)
- `0x00253227` → RVA `0x00FC5098` (`ALMOSTRO`; read)
- `0x00253279` → RVA `0x00FC6BF8` (`ALMOSTRO`; read)
- `0x0025329B` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x002532D1` → RVA `0x00FC6FF0` (`ALMOSTRO`; read)
- `0x0025331D` → RVA `0x00FC6B78` (`ALMOSTRO`; read)
- `0x00253329` → RVA `0x00FC6D18` (`ALMOSTRO`; read)
- `0x002533BC` → RVA `0x00FC52E0` (`ALMOSTRO`; read)
- `0x002536AC` → RVA `0x00F233CC` (`.data`; read)
- `0x00253790` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002538AC` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00253903` → RVA `0x00FC537C` (`ALMOSTRO`; read)
- `0x00253950` → RVA `0x00FC6D14` (`ALMOSTRO`; read)
- `0x00253D5E` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x00253D75` → RVA `0x00E2DBD0` (`.data`; read)
- `0x00253F79` → RVA `0x00FC5007` (`ALMOSTRO`; read)
- `0x00253FBC` → RVA `0x00FC6B14` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **61**
  - `0x0025309B` → [sub_002546EC + 0x242](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002530C5` → [sub_002546EC + 0x1B3](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253106` → [sub_002546EC + 0x1D5](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253164` → [sub_002546EC + 0xB97](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253185` → [sub_002546EC + 0xA8F](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002531BC` → [sub_002546EC + 0xBC9](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002531CD` → [sub_002546EC + 0x2E0](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002531E4` → [sub_002546EC + 0x44](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253263` → [sub_002546EC + 0x89F](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253290` → [sub_002546EC + 0x15D](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002532AE` → [sub_002546EC + 0x706](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002532BD` → [sub_002546EC + 0x961](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002532C5` → [sub_002546EC + 0x961](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x0025332F` → [sub_002546EC + 0x8A7](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253387` → [sub_002546EC + 0x40C](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002533C8` → [sub_002546EC + 0xFB](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002534A2` → [sub_002546EC + 0xB4](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002534C1` → [sub_002546EC + 0x4F](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002534EB` → [sub_002546EC + 0xB08](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x0025359B` → [sub_002546EC + 0x8CB](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002535EB` → [sub_002546EC + 0x524](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002535F7` → [sub_002546EC + 0x596](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253628` → [sub_002546EC + 0x715](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253636` → [sub_002546EC + 0x932](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002536A7` → [sub_002546EC + 0x596](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002536E6` → [sub_002546EC + 0xBD6](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002536FE` → [sub_002546EC + 0xBD6](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x0025373F` → [sub_00254461](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00253892` → [sub_002546EC + 0x47D](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253964` → [sub_002546EC + 0xBFA](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253AE0` → [sub_002546EC + 0xC11](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253AFB` → [sub_002546EC + 0xC11](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253C7A` → [sub_002546EC + 0x68](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253C9D` → [sub_002546EC + 0x196](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253E8A` → [sub_002546EC + 0xA07](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253E95` → [sub_002546EC + 0xC44](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00253E9B` → [sub_002546EC + 0xC8C](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00254013` → [sub_002546EC + 0x4C8](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x0025404E` → [sub_002546EC + 0x1A4](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00254057` → [sub_002546EC + 0x220](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00254068` → [sub_00254461 + 0x249](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x002540B8` → [sub_002546EC + 0x413](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002540EB` → [sub_002546EC + 0xD7](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00254122` → [sub_002546EC + 0x228](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x0025417A` → [sub_002546EC + 0x491](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002541A2` → [sub_002546EC + 0x110](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002541EA` → [sub_002546EC + 0xCF](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x0025421A` → [sub_00254461 + 0x1C2](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x00254230` → [sub_002546EC + 0x509](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x0025424D` → [sub_002546EC](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00254256` → [sub_002546EC](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x0025426D` → [sub_002546EC + 0x51C](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00254281` → [sub_002546EC](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00254289` → [sub_002546EC](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002542B2` → [sub_00254461 + 0xE](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x002542C1` → [sub_00254461 + 0x27](Unknown_function_00254461.md) (`tail-transfer`)
  - `0x002542C7` → [sub_006D8256 + 0x72](../6D/Unknown_function_006D8256.md) (`tail-transfer`)
  - `0x0025433F` → [sub_002546EC + 0x204](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00254386` → [sub_002546EC + 0x1DC](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x002543E7` → [sub_002546EC + 0x57](Unknown_function_002546EC.md) (`tail-transfer`)
  - `0x00254433` → [sub_002546EC + 0x6D4](Unknown_function_002546EC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0025308F  4C 89 A4 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], r12
00253097  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
0025309B  0F 85 8D 18 00 00               jne 0x14025492e
002530A1  45 32 E4                        xor r12b, r12b
002530A4  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
002530AE  40 38 B3 36 02 00 00            cmp byte ptr [rbx + 0x236], sil
002530B5  0F 84 74 13 00 00               je 0x14025442f
002530BB  80 BB C3 00 00 00 10            cmp byte ptr [rbx + 0xc3], 0x10
002530C2  41 B6 3F                        mov r14b, 0x3f
002530C5  0F 8D D4 17 00 00               jge 0x14025489f
002530CB  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
002530D0  32 DB                           xor bl, bl
002530D2  8B 08                           mov ecx, dword ptr [rax]
002530D4  41 2B 89 B4 01 00 00            sub ecx, dword ptr [r9 + 0x1b4]
002530DB  4D 3B 69 20                     cmp r13, qword ptr [r9 + 0x20]
002530DF  73 20                           jae 0x140253101
002530E1  41 80 B9 33 02 00 00 0E         cmp byte ptr [r9 + 0x233], 0xe
002530E9  7D 21                           jge 0x14025310c
002530EB  BA F0 0F 00 00                  mov edx, 0xff0
002530F0  66 41 85 91 06 02 00 00         test word ptr [r9 + 0x206], dx
002530F8  75 34                           jne 0x14025312e
002530FA  83 F9 02                        cmp ecx, 2
002530FD  73 0D                           jae 0x14025310c
002530FF  EB 2D                           jmp 0x14025312e
00253101  B3 04                           mov bl, 4
00253103  83 F9 02                        cmp ecx, 2
00253106  0F 82 B5 17 00 00               jb 0x1402548c1
0025310C  40 B6 01                        mov sil, 1
0025310F  49 8B C9                        mov rcx, r9
00253112  44 0F B6 C6                     movzx r8d, sil
00253116  E8 71 FC 16 00                  call 0x1403c2d8c
0025311B  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
00253120  45 84 E4                        test r12b, r12b
00253123  45 0F B6 F6                     movzx r14d, r14b
00253127  0F B6 C8                        movzx ecx, al
0025312A  44 0F 44 F1                     cmove r14d, ecx
0025312E  49 8B 81 20 02 00 00            mov rax, qword ptr [r9 + 0x220]
00253135  8B 80 88 00 00 00               mov eax, dword ptr [rax + 0x88]
0025313B  0F BA E0 0D                     bt eax, 0xd
0025313F  73 03                           jae 0x140253144
00253141  80 CB 02                        or bl, 2
00253144  41 8B 51 78                     mov edx, dword ptr [r9 + 0x78]
00253148  0F B6 C3                        movzx eax, bl
0025314B  F6 C2 08                        test dl, 8
0025314E  F6 D0                           not al
00253150  0F 94 C1                        sete cl
00253153  22 C8                           and cl, al
00253155  F6 C1 01                        test cl, 1
00253158  0F 85 F8 11 00 00               jne 0x140254356
0025315E  39 3D 3C 1F D7 00               cmp dword ptr [rip + 0xd71f3c], edi
00253164  0F 85 19 21 00 00               jne 0x140255283
0025316A  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0025316F  41 80 FE 3F                     cmp r14b, 0x3f
00253173  74 43                           je 0x1402531b8
00253175  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0025317E  44 3A B3 C3 00 00 00            cmp r14b, byte ptr [rbx + 0xc3]
00253185  0F 8F F0 1F 00 00               jg 0x14025517b
0025318B  48 8B CB                        mov rcx, rbx
0025318E  44 88 B3 C3 00 00 00            mov byte ptr [rbx + 0xc3], r14b
00253195  E8 76 4E 00 00                  call 0x140258010
0025319A  0F B6 8B 04 02 00 00            movzx ecx, byte ptr [rbx + 0x204]
002531A1  3B C1                           cmp eax, ecx
002531A3  74 06                           je 0x1402531ab
002531A5  88 83 04 02 00 00               mov byte ptr [rbx + 0x204], al
002531AB  F7 43 78 00 00 40 00            test dword ptr [rbx + 0x78], 0x400000
002531B2  0F 85 3C 11 00 00               jne 0x1402542f4
002531B8  40 F6 C6 02                     test sil, 2
002531BC  0F 85 F3 20 00 00               jne 0x1402552b5
002531C2  40 80 E6 01                     and sil, 1
002531C6  80 BB 36 02 00 00 02            cmp byte ptr [rbx + 0x236], 2
002531CD  0F 84 F9 17 00 00               je 0x1402549cc
002531D3  48 8B CB                        mov rcx, rbx
002531D6  E8 35 4E 00 00                  call 0x140258010
002531DB  0F B6 8B 04 02 00 00            movzx ecx, byte ptr [rbx + 0x204]
002531E2  3B C1                           cmp eax, ecx
002531E4  0F 85 46 15 00 00               jne 0x140254730
002531EA  4C 8D 1D 0F CE DA FF            lea r11, [rip - 0x2531f1]
002531F1  40 84 F6                        test sil, sil
002531F4  74 4E                           je 0x140253244
002531F6  F7 05 38 39 D7 00 00 00 04 00   test dword ptr [rip + 0xd73938], 0x40000
00253200  0F B6 93 8B 02 00 00            movzx edx, byte ptr [rbx + 0x28b]
00253207  74 1E                           je 0x140253227
00253209  40 38 3D E5 38 D7 00            cmp byte ptr [rip + 0xd738e5], dil
00253210  74 15                           je 0x140253227
00253212  0F B6 83 04 02 00 00            movzx eax, byte ptr [rbx + 0x204]
00253219  83 F8 04                        cmp eax, 4
0025321C  0F 85 C6 0E 00 00               jne 0x1402540e8
00253222  BA 24 00 00 00                  mov edx, 0x24
00253227  0F AF 15 6A 1E D7 00            imul edx, dword ptr [rip + 0xd71e6a]
0025322E  8B 43 78                        mov eax, dword ptr [rbx + 0x78]
00253231  8B CA                           mov ecx, edx
00253233  49 03 CD                        add rcx, r13
00253236  A8 20                           test al, 0x20
00253238  74 06                           je 0x140253240
0025323A  F0 0F BA 73 78 05               lock btr dword ptr [rbx + 0x78], 5
00253240  48 89 4B 20                     mov qword ptr [rbx + 0x20], rcx
00253244  8B 93 4C 02 00 00               mov edx, dword ptr [rbx + 0x24c]
0025324A  89 55 C0                        mov dword ptr [rbp - 0x40], edx
0025324D  66 89 BB 35 02 00 00            mov word ptr [rbx + 0x235], di
00253254  39 BB E4 01 00 00               cmp dword ptr [rbx + 0x1e4], edi
0025325A  75 0D                           jne 0x140253269
0025325C  80 BB 86 01 00 00 01            cmp byte ptr [rbx + 0x186], 1
00253263  0F 85 22 1D 00 00               jne 0x140254f8b
00253269  41 B4 01                        mov r12b, 1
0025326C  45 32 F6                        xor r14b, r14b
0025326F  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00253274  0F BA 73 74 01                  btr dword ptr [rbx + 0x74], 1
00253279  48 8B 05 78 39 D7 00            mov rax, qword ptr [rip + 0xd73978]
00253280  41 0F 92 C5                     setb r13b
00253284  44 88 6C 24 42                  mov byte ptr [rsp + 0x42], r13b
00253289  48 39 83 38 02 00 00            cmp qword ptr [rbx + 0x238], rax
00253290  0F 85 B3 15 00 00               jne 0x140254849
00253296  44 8B 44 24 78                  mov r8d, dword ptr [rsp + 0x78]
0025329B  F7 05 6B 38 D7 00 00 00 00 08   test dword ptr [rip + 0xd7386b], 0x8000000
002532A5  8B 83 4C 02 00 00               mov eax, dword ptr [rbx + 0x24c]
002532AB  89 45 DC                        mov dword ptr [rbp - 0x24], eax
002532AE  0F 85 3E 1B 00 00               jne 0x140254df2
002532B4  32 C0                           xor al, al
002532B6  88 44 24 43                     mov byte ptr [rsp + 0x43], al
002532BA  45 84 C0                        test r8b, r8b
002532BD  0F 85 8A 1D 00 00               jne 0x14025504d
002532C3  84 C0                           test al, al
002532C5  0F 85 82 1D 00 00               jne 0x14025504d
002532CB  33 C0                           xor eax, eax
002532CD  48 89 7D 48                     mov qword ptr [rbp + 0x48], rdi
002532D1  39 05 19 3D D7 00               cmp dword ptr [rip + 0xd73d19], eax
002532D7  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
002532DB  0F 84 CB 03 00 00               je 0x1402536ac
002532E1  48 8B 93 40 02 00 00            mov rdx, qword ptr [rbx + 0x240]
002532E8  44 8B C7                        mov r8d, edi
002532EB  0F B7 02                        movzx eax, word ptr [rdx]
002532EE  66 3B F8                        cmp di, ax
002532F1  0F 83 B3 04 00 00               jae 0x1402537aa
002532F7  48 83 C2 08                     add rdx, 8
002532FB  44 8B C8                        mov r9d, eax
002532FE  48 8B 02                        mov rax, qword ptr [rdx]
00253301  48 8D 52 08                     lea rdx, [rdx + 8]
00253305  F3 48 0F B8 C8                  popcnt rcx, rax
0025330A  44 03 C1                        add r8d, ecx
0025330D  49 83 E9 01                     sub r9, 1
00253311  75 EB                           jne 0x1402532fe
00253313  41 83 F8 01                     cmp r8d, 1
00253317  0F 86 8D 04 00 00               jbe 0x1402537aa
0025331D  39 3D 55 38 D7 00               cmp dword ptr [rip + 0xd73855], edi
00253323  0F 85 A0 05 00 00               jne 0x1402538c9
00253329  39 3D E9 39 D7 00               cmp dword ptr [rip + 0xd739e9], edi
0025332F  0F 85 5E 1C 00 00               jne 0x140254f93
00253335  4C 8B 83 40 02 00 00            mov r8, qword ptr [rbx + 0x240]
0025333C  4C 8D 4D 40                     lea r9, [rbp + 0x40]
00253340  48 8B D3                        mov rdx, rbx
00253343  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00253348  49 8B CF                        mov rcx, r15
0025334B  E8 88 23 00 00                  call 0x1402556d8
00253350  48 8B 75 40                     mov rsi, qword ptr [rbp + 0x40]
00253354  48 83 E6 FE                     and rsi, 0xfffffffffffffffe
00253358  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
0025335D  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
00253361  4C 8B C7                        mov r8, rdi
00253364  48 8B CA                        mov rcx, rdx
00253367  44 8B CF                        mov r9d, edi
0025336A  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0025336E  48 89 4D 28                     mov qword ptr [rbp + 0x28], rcx
00253372  83 E2 01                        and edx, 1
00253375  0F 85 6A 10 00 00               jne 0x1402543e5
0025337B  0F B6 49 23                     movzx ecx, byte ptr [rcx + 0x23]
0025337F  F6 D1                           not cl
00253381  83 E1 01                        and ecx, 1
00253384  3B 4D 48                        cmp ecx, dword ptr [rbp + 0x48]
00253387  0F 85 6B 17 00 00               jne 0x140254af8
0025338D  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00253392  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
00253395  89 83 18 02 00 00               mov dword ptr [rbx + 0x218], eax
0025339B  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
0025339F  48 85 C0                        test rax, rax
002533A2  0F 84 53 0D 00 00               je 0x1402540fb
002533A8  44 8B 8E D8 00 00 00            mov r9d, dword ptr [rsi + 0xd8]
002533AF  4C 03 C8                        add r9, rax
002533B2  4C 89 4D A8                     mov qword ptr [rbp - 0x58], r9
002533B6  0F 85 62 0F 00 00               jne 0x14025431e
002533BC  39 3D 1E 1F D7 00               cmp dword ptr [rip + 0xd71f1e], edi
002533C2  74 0A                           je 0x1402533ce
002533C4  F6 46 23 20                     test byte ptr [rsi + 0x23], 0x20
002533C8  0F 85 19 14 00 00               jne 0x1402547e7
002533CE  39 7D 48                        cmp dword ptr [rbp + 0x48], edi
002533D1  0F 84 FA 09 00 00               je 0x140253dd1
002533D7  4D 8B B7 E8 37 00 00            mov r14, qword ptr [r15 + 0x37e8]
002533DE  33 D2                           xor edx, edx
002533E0  4C 8B 6D 40                     mov r13, qword ptr [rbp + 0x40]
002533E4  41 B8 F0 00 00 00               mov r8d, 0xf0
002533EA  49 8B F5                        mov rsi, r13
002533ED  49 8B CE                        mov rcx, r14
002533F0  48 83 E6 FE                     and rsi, 0xfffffffffffffffe
002533F4  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
002533F9  E8 42 38 47 00                  call 0x1406c6c40
002533FE  45 8B DD                        mov r11d, r13d
00253401  44 8B CF                        mov r9d, edi
00253404  41 83 E3 01                     and r11d, 1
00253408  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
0025340C  48 8B CE                        mov rcx, rsi
0025340F  44 89 5C 24 70                  mov dword ptr [rsp + 0x70], r11d
00253414  45 8B E5                        mov r12d, r13d
00253417  44 89 4C 24 58                  mov dword ptr [rsp + 0x58], r9d
0025341C  4C 8B D7                        mov r10, rdi
0025341F  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
00253423  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
00253428  0F 84 98 0F 00 00               je 0x1402543c6
0025342E  41 83 FB 01                     cmp r11d, 1
00253432  75 1F                           jne 0x140253453
00253434  48 8B 86 58 8E 00 00            mov rax, qword ptr [rsi + 0x8e58]
0025343B  4C 8B 96 58 8E 00 00            mov r10, qword ptr [rsi + 0x8e58]
00253442  49 83 C2 08                     add r10, 8
00253446  4C 89 55 80                     mov qword ptr [rbp - 0x80], r10
0025344A  44 0F B6 08                     movzx r9d, byte ptr [rax]
0025344E  44 89 4C 24 58                  mov dword ptr [rsp + 0x58], r9d
00253453  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00253457  44 8B C7                        mov r8d, edi
0025345A  45 85 C9                        test r9d, r9d
0025345D  0F 84 0B 01 00 00               je 0x14025356e
00253463  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
00253468  49 8D 5E 30                     lea rbx, [r14 + 0x30]
0025346C  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
00253471  0F 57 C0                        xorps xmm0, xmm0
00253474  33 C0                           xor eax, eax
00253476  0F 11 43 E0                     movups xmmword ptr [rbx - 0x20], xmm0
0025347A  0F 11 43 F0                     movups xmmword ptr [rbx - 0x10], xmm0
0025347E  48 89 03                        mov qword ptr [rbx], rax
00253481  48 C7 43 F8 FF FF FF FF         mov qword ptr [rbx - 8], 0xffffffffffffffff
00253489  C6 43 04 3F                     mov byte ptr [rbx + 4], 0x3f
0025348D  4D 8B 2A                        mov r13, qword ptr [r10]
00253490  4C 89 6B E0                     mov qword ptr [rbx - 0x20], r13
00253494  48 89 7B E8                     mov qword ptr [rbx - 0x18], rdi
00253498  49 8B 8D 48 8E 00 00            mov rcx, qword ptr [r13 + 0x8e48]
0025349F  48 85 C9                        test rcx, rcx
002534A2  0F 85 F8 12 00 00               jne 0x1402547a0
002534A8  49 8B 75 10                     mov rsi, qword ptr [r13 + 0x10]
002534AC  48 89 73 F0                     mov qword ptr [rbx - 0x10], rsi
002534B0  48 85 F6                        test rsi, rsi
002534B3  75 08                           jne 0x1402534bd
002534B5  49 8B 75 08                     mov rsi, qword ptr [r13 + 8]
002534B9  48 89 73 F0                     mov qword ptr [rbx - 0x10], rsi
002534BD  49 39 75 10                     cmp qword ptr [r13 + 0x10], rsi
002534C1  0F 84 74 12 00 00               je 0x14025473b
002534C7  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002534D0  0F B6 0B                        movzx ecx, byte ptr [rbx]
002534D3  4C 3B E8                        cmp r13, rax
002534D6  0F 84 78 0C 00 00               je 0x140254154
002534DC  80 E1 FB                        and cl, 0xfb
002534DF  88 0B                           mov byte ptr [rbx], cl
002534E1  45 32 E4                        xor r12b, r12b
002534E4  F7 46 78 00 00 40 00            test dword ptr [rsi + 0x78], 0x400000
002534EB  0F 85 03 1D 00 00               jne 0x1402551f4
002534F1  41 0F B6 45 23                  movzx eax, byte ptr [r13 + 0x23]
002534F6  0F B6 13                        movzx edx, byte ptr [rbx]
002534F9  F6 D0                           not al
002534FB  24 01                           and al, 1
002534FD  80 E2 FE                        and dl, 0xfe
00253500  0A D0                           or dl, al
00253502  88 13                           mov byte ptr [rbx], dl
00253504  49 8B 45 38                     mov rax, qword ptr [r13 + 0x38]
00253508  0F B6 08                        movzx ecx, byte ptr [rax]
0025350B  C0 E9 06                        shr cl, 6
0025350E  32 CA                           xor cl, dl
00253510  80 E1 02                        and cl, 2
00253513  32 CA                           xor cl, dl
00253515  0F B6 C1                        movzx eax, cl
00253518  88 03                           mov byte ptr [rbx], al
0025351A  D1 E8                           shr eax, 1
0025351C  83 E0 01                        and eax, 1
0025351F  41 3B C0                        cmp eax, r8d
00253522  44 0F 4F C0                     cmovg r8d, eax
00253526  49 83 C2 08                     add r10, 8
0025352A  48 83 C3 28                     add rbx, 0x28
0025352E  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00253533  49 83 E9 01                     sub r9, 1
00253537  4C 89 55 80                     mov qword ptr [rbp - 0x80], r10
0025353B  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
00253540  0F 85 2B FF FF FF               jne 0x140253471
00253546  4C 8B 6D 40                     mov r13, qword ptr [rbp + 0x40]
0025354A  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
0025354E  4D 8B E5                        mov r12, r13
00253551  4C 8B 7D E0                     mov r15, qword ptr [rbp - 0x20]
00253555  44 8B 4C 24 58                  mov r9d, dword ptr [rsp + 0x58]
0025355A  44 8B 5C 24 70                  mov r11d, dword ptr [rsp + 0x70]
0025355F  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00253564  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00253569  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
0025356E  45 89 46 04                     mov dword ptr [r14 + 4], r8d
00253572  BA 01 00 00 00                  mov edx, 1
00253577  45 89 5E 08                     mov dword ptr [r14 + 8], r11d
0025357B  45 88 0E                        mov byte ptr [r14], r9b
0025357E  45 85 DB                        test r11d, r11d
00253581  0F 84 4E 0B 00 00               je 0x1402540d5
00253587  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
0025358E  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
00253592  49 8B CE                        mov rcx, r14
00253595  88 04 0A                        mov byte ptr [rdx + rcx], al
00253598  45 85 C0                        test r8d, r8d
0025359B  0F 85 16 1A 00 00               jne 0x140254fb7
002535A1  45 0F B6 06                     movzx r8d, byte ptr [r14]
002535A5  4C 8B CF                        mov r9, rdi
002535A8  8B D7                           mov edx, edi
002535AA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
002535B0  41 3B D0                        cmp edx, r8d
002535B3  73 19                           jae 0x1402535ce
002535B5  8B C2                           mov eax, edx
002535B7  48 8D 0C 80                     lea rcx, [rax + rax*4]
002535BB  49 39 74 CE 10                  cmp qword ptr [r14 + rcx*8 + 0x10], rsi
002535C0  49 8D 04 CE                     lea rax, [r14 + rcx*8]
002535C4  74 04                           je 0x1402535ca
002535C6  FF C2                           inc edx
002535C8  EB E6                           jmp 0x1402535b0
002535CA  4C 8D 48 10                     lea r9, [rax + 0x10]
002535CE  44 8B 53 78                     mov r10d, dword ptr [rbx + 0x78]
002535D2  41 0F B6 41 20                  movzx eax, byte ptr [r9 + 0x20]
002535D7  41 D1 EA                        shr r10d, 1
002535DA  D1 E8                           shr eax, 1
002535DC  41 83 E2 01                     and r10d, 1
002535E0  83 E0 01                        and eax, 1
002535E3  44 89 54 24 70                  mov dword ptr [rsp + 0x70], r10d
002535E8  44 3B D0                        cmp r10d, eax
002535EB  0F 83 1F 16 00 00               jae 0x140254c10
002535F1  44 8B DF                        mov r11d, edi
002535F4  41 38 3E                        cmp byte ptr [r14], dil
002535F7  0F 86 85 16 00 00               jbe 0x140254c82
002535FD  4C 8B 65 D0                     mov r12, qword ptr [rbp - 0x30]
00253601  44 0F B6 7C 24 42               movzx r15d, byte ptr [rsp + 0x42]
00253607  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
0025360C  41 8B C3                        mov eax, r11d
0025360F  48 8D 0C 80                     lea rcx, [rax + rax*4]
00253613  49 8B 5C CE 10                  mov rbx, qword ptr [r14 + rcx*8 + 0x10]
00253618  4D 8D 0C CE                     lea r9, [r14 + rcx*8]
0025361C  49 8B 4C CE 28                  mov rcx, qword ptr [r14 + rcx*8 + 0x28]
00253621  48 8D 41 FF                     lea rax, [rcx - 1]
00253625  48 3B DE                        cmp rbx, rsi
00253628  0F 84 D3 17 00 00               je 0x140254e01
0025362E  48 8B 73 18                     mov rsi, qword ptr [rbx + 0x18]
00253632  48 83 F8 FC                     cmp rax, -4
00253636  0F 86 E2 19 00 00               jbe 0x14025501e
0025363C  41 0F B6 41 30                  movzx eax, byte ptr [r9 + 0x30]
00253641  0C 01                           or al, 1
00253643  49 89 71 20                     mov qword ptr [r9 + 0x20], rsi
00253647  41 88 41 30                     mov byte ptr [r9 + 0x30], al
0025364B  24 FD                           and al, 0xfd
0025364D  8B 4E 78                        mov ecx, dword ptr [rsi + 0x78]
00253650  D1 E9                           shr ecx, 1
00253652  80 E1 01                        and cl, 1
00253655  02 C9                           add cl, cl
00253657  32 C8                           xor cl, al
00253659  80 E1 E7                        and cl, 0xe7
0025365C  80 C9 04                        or cl, 4
0025365F  80 E1 DF                        and cl, 0xdf
00253662  41 88 49 30                     mov byte ptr [r9 + 0x30], cl
00253666  48 8B CE                        mov rcx, rsi
00253669  41 80 61 31 FE                  and byte ptr [r9 + 0x31], 0xfe
0025366E  49 89 71 28                     mov qword ptr [r9 + 0x28], rsi
00253672  E8 B9 FB 0F 00                  call 0x140353230
00253677  84 C0                           test al, al
00253679  75 09                           jne 0x140253684
0025367B  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0025367E  89 86 18 02 00 00               mov dword ptr [rsi + 0x218], eax
00253684  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00253689  41 0F B6 06                     movzx eax, byte ptr [r14]
0025368D  41 FF C3                        inc r11d
00253690  44 3B D8                        cmp r11d, eax
00253693  0F 82 73 FF FF FF               jb 0x14025360c
00253699  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
0025369E  44 8B 54 24 70                  mov r10d, dword ptr [rsp + 0x70]
002536A3  4C 8B 7D E0                     mov r15, qword ptr [rbp - 0x20]
002536A7  E9 D6 15 00 00                  jmp 0x140254c82
002536AC  8B 05 1A FD CC 00               mov eax, dword ptr [rip + 0xccfd1a]
002536B2  83 F8 04                        cmp eax, 4
002536B5  0F 85 26 FC FF FF               jne 0x1402532e1
002536BB  44 8B AB 18 02 00 00            mov r13d, dword ptr [rbx + 0x218]
002536C2  4C 8B 83 40 02 00 00            mov r8, qword ptr [rbx + 0x240]
002536C9  41 0F BA F5 1F                  btr r13d, 0x1f
002536CE  4B 8B B4 EB 40 8C FC 00         mov rsi, qword ptr [r11 + r13*8 + 0xfc8c40]
002536D6  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
002536DB  0F B6 86 D0 00 00 00            movzx eax, byte ptr [rsi + 0xd0]
002536E2  66 41 3B 00                     cmp ax, word ptr [r8]
002536E6  0F 83 D6 1B 00 00               jae 0x1402552c2
002536EC  0F B6 8E D1 00 00 00            movzx ecx, byte ptr [rsi + 0xd1]
002536F3  49 8B 54 C0 08                  mov rdx, qword ptr [r8 + rax*8 + 8]
002536F8  48 D3 EA                        shr rdx, cl
002536FB  F6 C2 01                        test dl, 1
002536FE  0F 84 BE 1B 00 00               je 0x1402552c2
00253704  44 8B 4B 78                     mov r9d, dword ptr [rbx + 0x78]
00253708  48 8B CE                        mov rcx, rsi
0025370B  48 8B 5E 38                     mov rbx, qword ptr [rsi + 0x38]
0025370F  41 D1 E9                        shr r9d, 1
00253712  41 83 E1 01                     and r9d, 1
00253716  41 8B D1                        mov edx, r9d
00253719  44 89 4C 24 70                  mov dword ptr [rsp + 0x70], r9d
0025371E  0F B6 1B                        movzx ebx, byte ptr [rbx]
00253721  8B C3                           mov eax, ebx
00253723  48 89 75 F8                     mov qword ptr [rbp - 8], rsi
00253727  C1 E8 07                        shr eax, 7
0025372A  44 3B C8                        cmp r9d, eax
0025372D  0F 42 D0                        cmovb edx, eax
00253730  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
00253734  8B C2                           mov eax, edx
00253736  48 0B C8                        or rcx, rax
00253739  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
0025373D  85 D2                           test edx, edx
0025373F  0F 84 1C 0D 00 00               je 0x140254461
00253745  83 FA 01                        cmp edx, 1
00253748  0F 85 26 0A 00 00               jne 0x140254174
0025374E  48 8B 86 58 8E 00 00            mov rax, qword ptr [rsi + 0x8e58]
00253755  0F B6 08                        movzx ecx, byte ptr [rax]
00253758  4C 8D 78 08                     lea r15, [rax + 8]
0025375C  85 C9                           test ecx, ecx
0025375E  0F 84 10 0A 00 00               je 0x140254174
00253764  44 8B E1                        mov r12d, ecx
00253767  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00253770  49 8B 37                        mov rsi, qword ptr [r15]
00253773  44 8B F7                        mov r14d, edi
00253776  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00253780  F0 48 0F BA 6E 30 00            lock bts qword ptr [rsi + 0x30], 0
00253787  0F 83 CF 09 00 00               jae 0x14025415c
0025378D  41 FF C6                        inc r14d
00253790  44 85 35 15 1B D7 00            test dword ptr [rip + 0xd71b15], r14d
00253797  0F 84 2F 0B 00 00               je 0x1402542cc
0025379D  F3 90                           pause
0025379F  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
002537A3  48 85 C0                        test rax, rax
002537A6  74 D8                           je 0x140253780
002537A8  EB E3                           jmp 0x14025378d
002537AA  48 8B 8B 40 02 00 00            mov rcx, qword ptr [rbx + 0x240]
002537B1  E8 2A F9 1F 00                  call 0x1404530e0
002537B6  44 8B 4B 78                     mov r9d, dword ptr [rbx + 0x78]
002537BA  48 8D 35 3F C8 DA FF            lea rsi, [rip - 0x2537c1]
002537C1  8B C8                           mov ecx, eax
002537C3  41 D1 E9                        shr r9d, 1
002537C6  41 83 E1 01                     and r9d, 1
002537CA  41 8B D1                        mov edx, r9d
002537CD  44 89 4C 24 70                  mov dword ptr [rsp + 0x70], r9d
002537D2  48 8B B4 CE 40 8C FC 00         mov rsi, qword ptr [rsi + rcx*8 + 0xfc8c40]
002537DA  48 8B CE                        mov rcx, rsi
002537DD  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
002537E2  48 8B 5E 38                     mov rbx, qword ptr [rsi + 0x38]
002537E6  0F B6 1B                        movzx ebx, byte ptr [rbx]
002537E9  8B C3                           mov eax, ebx
002537EB  48 89 75 20                     mov qword ptr [rbp + 0x20], rsi
002537EF  C1 E8 07                        shr eax, 7
002537F2  44 3B C8                        cmp r9d, eax
002537F5  0F 42 D0                        cmovb edx, eax
002537F8  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
002537FC  8B C2                           mov eax, edx
002537FE  48 0B C8                        or rcx, rax
00253801  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
00253805  85 D2                           test edx, edx
00253807  0F 84 3C 0C 00 00               je 0x140254449
0025380D  83 FA 01                        cmp edx, 1
00253810  0F 85 76 00 00 00               jne 0x14025388c
00253816  48 8B 86 58 8E 00 00            mov rax, qword ptr [rsi + 0x8e58]
0025381D  0F B6 08                        movzx ecx, byte ptr [rax]
00253820  4C 8D 60 08                     lea r12, [rax + 8]
00253824  85 C9                           test ecx, ecx
00253826  74 5E                           je 0x140253886
00253828  44 8B E9                        mov r13d, ecx
0025382B  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00253834  0F 1F 40 00                     nop dword ptr [rax]
00253838  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00253840  49 8B 34 24                     mov rsi, qword ptr [r12]
00253844  44 8B F7                        mov r14d, edi
00253847  F0 48 0F BA 6E 30 00            lock bts qword ptr [rsi + 0x30], 0
0025384E  73 19                           jae 0x140253869
00253850  41 FF C6                        inc r14d
00253853  44 85 35 52 1A D7 00            test dword ptr [rip + 0xd71a52], r14d
0025385A  74 50                           je 0x1402538ac
0025385C  F3 90                           pause
0025385E  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
00253862  48 85 C0                        test rax, rax
00253865  74 E0                           je 0x140253847
00253867  EB E7                           jmp 0x140253850
00253869  49 83 C4 08                     add r12, 8
0025386D  49 83 ED 01                     sub r13, 1
00253871  75 CD                           jne 0x140253840
00253873  44 8B 4C 24 70                  mov r9d, dword ptr [rsp + 0x70]
00253878  45 32 F6                        xor r14b, r14b
0025387B  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00253880  44 0F B6 6C 24 42               movzx r13d, byte ptr [rsp + 0x42]
00253886  44 0F B6 64 24 40               movzx r12d, byte ptr [rsp + 0x40]
0025388C  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
00253890  32 18                           xor bl, byte ptr [rax]
00253892  0F 88 D1 12 00 00               js 0x140254b69
00253898  48 8D 4D 40                     lea rcx, [rbp + 0x40]
0025389C  E8 CF 33 00 00                  call 0x140256c70
002538A1  89 45 48                        mov dword ptr [rbp + 0x48], eax
002538A4  89 7D 4C                        mov dword ptr [rbp + 0x4c], edi
002538A7  E9 B1 FA FF FF                  jmp 0x14025335d
002538AC  8B 05 06 32 D7 00               mov eax, dword ptr [rip + 0xd73206]
002538B2  A8 40                           test al, 0x40
002538B4  74 A6                           je 0x14025385c
002538B6  E8 D5 BB 0B 00                  call 0x14030f490
002538BB  84 C0                           test al, al
002538BD  74 9D                           je 0x14025385c
002538BF  41 8B CE                        mov ecx, r14d
002538C2  E8 99 BB 0B 00                  call 0x14030f460
002538C7  EB 95                           jmp 0x14025385e
002538C9  44 0F B6 83 04 02 00 00         movzx r8d, byte ptr [rbx + 0x204]
002538D1  33 C0                           xor eax, eax
002538D3  8B 4B 50                        mov ecx, dword ptr [rbx + 0x50]
002538D6  8B D7                           mov edx, edi
002538D8  0F B6 B3 05 02 00 00            movzx esi, byte ptr [rbx + 0x205]
002538DF  0F 57 C0                        xorps xmm0, xmm0
002538E2  4C 8B 93 40 02 00 00            mov r10, qword ptr [rbx + 0x240]
002538E9  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
002538ED  8B 43 54                        mov eax, dword ptr [rbx + 0x54]
002538F0  3B C8                           cmp ecx, eax
002538F2  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
002538F6  0F 46 C8                        cmovbe ecx, eax
002538F9  C7 85 A0 00 00 00 05 04 03 02   mov dword ptr [rbp + 0xa0], 0x2030405
00253903  3B 0D 73 1A D7 00               cmp ecx, dword ptr [rip + 0xd71a73]
00253909  66 C7 85 A4 00 00 00 06 00      mov word ptr [rbp + 0xa4], 6
00253912  0F 93 C2                        setae dl
00253915  C6 85 A6 00 00 00 01            mov byte ptr [rbp + 0xa6], 1
0025391C  8B C2                           mov eax, edx
0025391E  4C 89 55 80                     mov qword ptr [rbp - 0x80], r10
00253922  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
00253926  44 89 45 8C                     mov dword ptr [rbp - 0x74], r8d
0025392A  4A 8D 0C 40                     lea rcx, [rax + r8*2]
0025392E  89 55 90                        mov dword ptr [rbp - 0x70], edx
00253931  41 8B 84 8B 60 54 FC 00         mov eax, dword ptr [r11 + rcx*4 + 0xfc5460]
00253939  0F B6 8B C3 00 00 00            movzx ecx, byte ptr [rbx + 0xc3]
00253940  89 45 94                        mov dword ptr [rbp - 0x6c], eax
00253943  42 0F B6 84 05 A0 00 00 00      movzx eax, byte ptr [rbp + r8 + 0xa0]
0025394C  88 44 24 55                     mov byte ptr [rsp + 0x55], al
00253950  8B 05 BE 33 D7 00               mov eax, dword ptr [rip + 0xd733be]
00253956  88 4D 88                        mov byte ptr [rbp - 0x78], cl
00253959  40 88 74 24 41                  mov byte ptr [rsp + 0x41], sil
0025395E  40 88 75 98                     mov byte ptr [rbp - 0x68], sil
00253962  A8 08                           test al, 8
00253964  0F 85 7C 19 00 00               jne 0x1402552e6
0025396A  40 88 7C 24 54                  mov byte ptr [rsp + 0x54], dil
0025396F  8B 5B 78                        mov ebx, dword ptr [rbx + 0x78]
00253972  0F B7 44 24 54                  movzx eax, word ptr [rsp + 0x54]
00253977  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
0025397C  D1 EB                           shr ebx, 1
0025397E  83 E3 01                        and ebx, 1
00253981  66 89 45 9A                     mov word ptr [rbp - 0x66], ax
00253985  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00253989  41 8B 82 4C 02 00 00            mov eax, dword ptr [r10 + 0x24c]
00253990  89 5D 9C                        mov dword ptr [rbp - 0x64], ebx
00253993  49 8B 9C C3 40 8C FC 00         mov rbx, qword ptr [r11 + rax*8 + 0xfc8c40]
0025399B  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
002539A0  48 8B 83 C0 00 00 00            mov rax, qword ptr [rbx + 0xc0]
002539A7  44 8B C7                        mov r8d, edi
002539AA  48 89 7D 00                     mov qword ptr [rbp], rdi
002539AE  0F B7 55 02                     movzx edx, word ptr [rbp + 2]
002539B2  89 7C 24 70                     mov dword ptr [rsp + 0x70], edi
002539B6  0F B7 80 8A 00 00 00            movzx eax, word ptr [rax + 0x8a]
002539BD  66 89 44 24 54                  mov word ptr [rsp + 0x54], ax
002539C2  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
002539C6  0F B7 C0                        movzx eax, ax
002539C9  66 85 D2                        test dx, dx
002539CC  0F 85 8C 03 00 00               jne 0x140253d5e
002539D2  C7 44 24 60 01 00 00 00         mov dword ptr [rsp + 0x60], 1
002539DA  83 F8 FF                        cmp eax, -1
002539DD  0F 84 AC 03 00 00               je 0x140253d8f
002539E3  4D 8B A4 C3 C0 F6 FC 00         mov r12, qword ptr [r11 + rax*8 + 0xfcf6c0]
002539EB  0F 57 C9                        xorps xmm1, xmm1
002539EE  4C 8B AB C0 00 00 00            mov r13, qword ptr [rbx + 0xc0]
002539F5  0F 57 C0                        xorps xmm0, xmm0
002539F8  8B 4D 8C                        mov ecx, dword ptr [rbp - 0x74]
002539FB  0F 11 45 70                     movups xmmword ptr [rbp + 0x70], xmm0
002539FF  0F 11 8D 80 00 00 00            movups xmmword ptr [rbp + 0x80], xmm1
00253A06  0F 11 8D 90 00 00 00            movups xmmword ptr [rbp + 0x90], xmm1
00253A0D  E8 1E EA 13 00                  call 0x140392430
00253A12  84 C0                           test al, al
00253A14  0F 85 14 03 00 00               jne 0x140253d2e
00253A1A  F7 05 14 31 D7 00 00 00 80 00   test dword ptr [rip + 0xd73114], 0x800000
00253A24  0F 84 04 03 00 00               je 0x140253d2e
00253A2A  41 F6 44 24 0A 08               test byte ptr [r12 + 0xa], 8
00253A30  0F 84 F8 02 00 00               je 0x140253d2e
00253A36  41 BE 01 00 00 00               mov r14d, 1
00253A3C  8B 45 94                        mov eax, dword ptr [rbp - 0x6c]
00253A3F  40 0F B6 D6                     movzx edx, sil
00253A43  83 C0 FD                        add eax, -3
00253A46  48 C1 E2 05                     shl rdx, 5
00253A4A  83 F8 01                        cmp eax, 1
00253A4D  0F 87 89 06 00 00               ja 0x1402540dc
00253A53  48 81 C2 38 02 00 00            add rdx, 0x238
00253A5A  49 03 D4                        add rdx, r12
00253A5D  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
00253A64  41 B8 20 00 00 00               mov r8d, 0x20
00253A6A  E8 61 8F 46 00                  call 0x1406bc9d0
00253A6F  41 0F 10 44 24 10               movups xmm0, xmmword ptr [r12 + 0x10]
00253A75  0F 11 45 70                     movups xmmword ptr [rbp + 0x70], xmm0
00253A79  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00253A7D  E8 2E 19 00 00                  call 0x1402553b0
00253A82  85 C0                           test eax, eax
00253A84  0F 85 79 01 00 00               jne 0x140253c03
00253A8A  0F 57 C0                        xorps xmm0, xmm0
00253A8D  8D 50 20                        lea edx, [rax + 0x20]
00253A90  0F 57 C9                        xorps xmm1, xmm1
00253A93  45 32 C0                        xor r8b, r8b
00253A96  0F 11 45 50                     movups xmmword ptr [rbp + 0x50], xmm0
00253A9A  48 8B CF                        mov rcx, rdi
00253A9D  0F 11 4D 60                     movups xmmword ptr [rbp + 0x60], xmm1
00253AA1  48 8D 45 70                     lea rax, [rbp + 0x70]
00253AA5  48 0F A3 08                     bt qword ptr [rax], rcx
00253AA9  0F 92 C0                        setb al
00253AAC  84 C0                           test al, al
00253AAE  0F 85 35 01 00 00               jne 0x140253be9
00253AB4  48 FF C1                        inc rcx
00253AB7  48 83 EA 01                     sub rdx, 1
00253ABB  75 E4                           jne 0x140253aa1
00253ABD  0F 28 45 60                     movaps xmm0, xmmword ptr [rbp + 0x60]
00253AC1  66 0F 7F 45 50                  movdqa xmmword ptr [rbp + 0x50], xmm0
00253AC6  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00253ACA  E8 E1 18 00 00                  call 0x1402553b0
00253ACF  85 C0                           test eax, eax
00253AD1  75 A6                           jne 0x140253a79
00253AD3  41 0F B7 04 24                  movzx eax, word ptr [r12]
00253AD8  66 41 39 85 8A 00 00 00         cmp word ptr [r13 + 0x8a], ax
00253AE0  0F 85 17 18 00 00               jne 0x1402552fd
00253AE6  41 0F B7 8D 88 00 00 00         movzx ecx, word ptr [r13 + 0x88]
00253AEE  48 8D 45 50                     lea rax, [rbp + 0x50]
00253AF2  48 0F A3 08                     bt qword ptr [rax], rcx
00253AF6  0F 92 C0                        setb al
00253AF9  84 C0                           test al, al
00253AFB  0F 84 FC 17 00 00               je 0x1402552fd
00253B01  49 8B F5                        mov rsi, r13
00253B04  4C 8B 4D 80                     mov r9, qword ptr [rbp - 0x80]
00253B08  48 8D 45 88                     lea rax, [rbp - 0x78]
00253B0C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00253B11  4C 8B C3                        mov r8, rbx
00253B14  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00253B19  48 8B D6                        mov rdx, rsi
00253B1C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00253B21  E8 DE 19 00 00                  call 0x140255504
00253B26  48 8B D8                        mov rbx, rax
00253B29  48 85 C0                        test rax, rax
00253B2C  0F 84 04 02 00 00               je 0x140253d36
00253B32  83 7D 90 01                     cmp dword ptr [rbp - 0x70], 1
00253B36  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00253B3B  48 8B B0 C0 00 00 00            mov rsi, qword ptr [rax + 0xc0]
00253B42  44 8B 5C 24 50                  mov r11d, dword ptr [rsp + 0x50]
00253B47  4D 8B A5 C0 00 00 00            mov r12, qword ptr [r13 + 0xc0]
00253B4E  75 18                           jne 0x140253b68
00253B50  39 7D 8C                        cmp dword ptr [rbp - 0x74], edi
00253B53  75 13                           jne 0x140253b68
00253B55  8B 45 94                        mov eax, dword ptr [rbp - 0x6c]
00253B58  FF C8                           dec eax
00253B5A  83 F8 01                        cmp eax, 1
00253B5D  77 09                           ja 0x140253b68
00253B5F  45 85 DB                        test r11d, r11d
00253B62  0F 84 9C 04 00 00               je 0x140254004
00253B68  0F B6 74 24 41                  movzx esi, byte ptr [rsp + 0x41]
00253B6D  49 63 C3                        movsxd rax, r11d
00253B70  4C 8B EB                        mov r13, rbx
00253B73  48 8B C8                        mov rcx, rax
00253B76  48 89 5D 08                     mov qword ptr [rbp + 8], rbx
00253B7A  48 33 CB                        xor rcx, rbx
00253B7D  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
00253B81  48 33 C8                        xor rcx, rax
00253B84  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
00253B88  45 85 DB                        test r11d, r11d
00253B8B  0F 84 76 05 00 00               je 0x140254107
00253B91  41 83 FB 01                     cmp r11d, 1
00253B95  0F 85 C7 00 00 00               jne 0x140253c62
00253B9B  48 8B 83 58 8E 00 00            mov rax, qword ptr [rbx + 0x8e58]
00253BA2  0F B6 10                        movzx edx, byte ptr [rax]
00253BA5  4C 8D 70 08                     lea r14, [rax + 8]
00253BA9  85 D2                           test edx, edx
00253BAB  0F 84 B1 00 00 00               je 0x140253c62
00253BB1  44 8B E2                        mov r12d, edx
00253BB4  4C 8B EB                        mov r13, rbx
00253BB7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00253BC0  49 8B 1E                        mov rbx, qword ptr [r14]
00253BC3  8B F7                           mov esi, edi
00253BC5  F0 48 0F BA 6B 30 00            lock bts qword ptr [rbx + 0x30], 0
00253BCC  73 72                           jae 0x140253c40
00253BCE  FF C6                           inc esi
00253BD0  85 35 D6 16 D7 00               test dword ptr [rip + 0xd716d6], esi
00253BD6  0F 84 2B 01 00 00               je 0x140253d07
00253BDC  F3 90                           pause
00253BDE  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
00253BE2  48 85 C0                        test rax, rax
00253BE5  74 DE                           je 0x140253bc5
00253BE7  EB E5                           jmp 0x140253bce
00253BE9  0F B6 84 0D 80 00 00 00         movzx eax, byte ptr [rbp + rcx + 0x80]
00253BF1  41 3A C0                        cmp al, r8b
00253BF4  75 37                           jne 0x140253c2d
00253BF6  48 8D 45 60                     lea rax, [rbp + 0x60]
00253BFA  48 0F AB 08                     bts qword ptr [rax], rcx
00253BFE  E9 B1 FE FF FF                  jmp 0x140253ab4
00253C03  44 3B 74 24 50                  cmp r14d, dword ptr [rsp + 0x50]
00253C08  0F 8F 79 01 00 00               jg 0x140253d87
00253C0E  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
00253C12  4C 8D 1D E7 C3 DA FF            lea r11, [rip - 0x253c19]
00253C19  0F B7 44 24 54                  movzx eax, word ptr [rsp + 0x54]
00253C1E  0F B6 74 24 41                  movzx esi, byte ptr [rsp + 0x41]
00253C23  44 8B 44 24 70                  mov r8d, dword ptr [rsp + 0x70]
00253C28  E9 99 FD FF FF                  jmp 0x1402539c6
00253C2D  0F 86 81 FE FF FF               jbe 0x140253ab4
00253C33  0F 57 C0                        xorps xmm0, xmm0
00253C36  44 0F B6 C0                     movzx r8d, al
00253C3A  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
00253C3E  EB B6                           jmp 0x140253bf6
00253C40  49 83 C6 08                     add r14, 8
00253C44  49 83 EC 01                     sub r12, 1
00253C48  0F 85 72 FF FF FF               jne 0x140253bc0
00253C4E  0F B6 75 98                     movzx esi, byte ptr [rbp - 0x68]
00253C52  8B 45 9C                        mov eax, dword ptr [rbp - 0x64]
00253C55  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00253C59  40 88 74 24 41                  mov byte ptr [rsp + 0x41], sil
00253C5E  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00253C62  48 8B D1                        mov rdx, rcx
00253C65  44 8B C1                        mov r8d, ecx
00253C68  48 83 E2 FE                     and rdx, 0xfffffffffffffffe
00253C6C  4C 8B D7                        mov r10, rdi
00253C6F  48 89 55 10                     mov qword ptr [rbp + 0x10], rdx
00253C73  44 8B CF                        mov r9d, edi
00253C76  41 83 E0 01                     and r8d, 1
00253C7A  0F 85 D4 0A 00 00               jne 0x140254754
00253C80  F6 42 23 01                     test byte ptr [rdx + 0x23], 1
00253C84  0F 84 93 04 00 00               je 0x14025411d
00253C8A  4C 8B C9                        mov r9, rcx
00253C8D  4C 8B C7                        mov r8, rdi
00253C90  49 83 E1 FE                     and r9, 0xfffffffffffffffe
00253C94  8B D7                           mov edx, edi
00253C96  4C 89 4D 18                     mov qword ptr [rbp + 0x18], r9
00253C9A  83 E1 01                        and ecx, 1
00253C9D  0F 84 DF 0B 00 00               je 0x140254882
00253CA3  83 F9 01                        cmp ecx, 1
00253CA6  75 15                           jne 0x140253cbd
00253CA8  49 8B 81 58 8E 00 00            mov rax, qword ptr [r9 + 0x8e58]
00253CAF  4D 8B 81 58 8E 00 00            mov r8, qword ptr [r9 + 0x8e58]
00253CB6  49 83 C0 08                     add r8, 8
00253CBA  0F B6 10                        movzx edx, byte ptr [rax]
00253CBD  85 D2                           test edx, edx
00253CBF  74 31                           je 0x140253cf2
00253CC1  0F 1F 40 00                     nop dword ptr [rax]
00253CC5  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
00253CD0  8D 42 FF                        lea eax, [rdx - 1]
00253CD3  49 8B 0C C0                     mov rcx, qword ptr [r8 + rax*8]
00253CD7  8B D0                           mov edx, eax
00253CD9  F0 48 21 79 30                  lock and qword ptr [rcx + 0x30], rdi
00253CDE  85 C0                           test eax, eax
00253CE0  75 EE                           jne 0x140253cd0
00253CE2  0F B6 75 98                     movzx esi, byte ptr [rbp - 0x68]
00253CE6  8B 45 9C                        mov eax, dword ptr [rbp - 0x64]
00253CE9  40 88 74 24 41                  mov byte ptr [rsp + 0x41], sil
00253CEE  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00253CF2  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
00253CF7  4C 8D 1D 02 C3 DA FF            lea r11, [rip - 0x253cfe]
00253CFE  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
00253D02  E9 99 FC FF FF                  jmp 0x1402539a0
00253D07  8B 05 AB 2D D7 00               mov eax, dword ptr [rip + 0xd72dab]
00253D0D  A8 40                           test al, 0x40
00253D0F  0F 84 C7 FE FF FF               je 0x140253bdc
00253D15  E8 76 B7 0B 00                  call 0x14030f490
00253D1A  84 C0                           test al, al
00253D1C  0F 84 BA FE FF FF               je 0x140253bdc
00253D22  8B CE                           mov ecx, esi
00253D24  E8 37 B7 0B 00                  call 0x14030f460
00253D29  E9 B0 FE FF FF                  jmp 0x140253bde
00253D2E  44 8B F7                        mov r14d, edi
00253D31  E9 06 FD FF FF                  jmp 0x140253a3c
00253D36  0F B7 86 88 00 00 00            movzx eax, word ptr [rsi + 0x88]
00253D3D  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00253D41  48 0F B3 01                     btr qword ptr [rcx], rax
00253D45  0F B7 86 88 00 00 00            movzx eax, word ptr [rsi + 0x88]
00253D4C  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00253D50  48 0F B3 01                     btr qword ptr [rcx], rax
00253D54  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
00253D59  E9 68 FD FF FF                  jmp 0x140253ac6
00253D5E  0F B7 0D 9B 12 D7 00            movzx ecx, word ptr [rip + 0xd7129b]
00253D65  41 FF C0                        inc r8d
00253D68  44 89 44 24 70                  mov dword ptr [rsp + 0x70], r8d
00253D6D  44 3B C1                        cmp r8d, ecx
00253D70  74 1D                           je 0x140253d8f
00253D72  0F AF C8                        imul ecx, eax
00253D75  48 8B 05 54 9E BD 00            mov rax, qword ptr [rip + 0xbd9e54]
00253D7C  41 03 C8                        add ecx, r8d
00253D7F  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
00253D82  E9 53 FC FF FF                  jmp 0x1402539da
00253D87  41 FF CE                        dec r14d
00253D8A  E9 E0 FC FF FF                  jmp 0x140253a6f
00253D8F  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
00253D93  48 8D 45 40                     lea rax, [rbp + 0x40]
00253D97  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00253D9C  4C 8D 4D 88                     lea r9, [rbp - 0x78]
00253DA0  48 8B D3                        mov rdx, rbx
00253DA3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00253DA8  E8 23 23 00 00                  call 0x1402560d0
00253DAD  85 C0                           test eax, eax
00253DAF  0F 89 83 03 00 00               jns 0x140254138
00253DB5  0F B6 75 98                     movzx esi, byte ptr [rbp - 0x68]
00253DB9  4C 8D 1D 40 C2 DA FF            lea r11, [rip - 0x253dc0]
00253DC0  8B 45 9C                        mov eax, dword ptr [rbp - 0x64]
00253DC3  40 88 74 24 41                  mov byte ptr [rsp + 0x41], sil
00253DC8  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00253DCC  E9 CF FB FF FF                  jmp 0x1402539a0
00253DD1  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
00253DD5  45 84 F6                        test r14b, r14b
00253DD8  0F 85 E2 03 00 00               jne 0x1402541c0
00253DDE  48 8D 45 A8                     lea rax, [rbp - 0x58]
00253DE2  45 0F B6 C5                     movzx r8d, r13b
00253DE6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00253DEB  4C 8D 4D 40                     lea r9, [rbp + 0x40]
00253DEF  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00253DF3  48 8B D3                        mov rdx, rbx
00253DF6  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00253DFB  49 8B CF                        mov rcx, r15
00253DFE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00253E03  E8 F8 5C 00 00                  call 0x140259b00
00253E08  84 C0                           test al, al
00253E0A  75 79                           jne 0x140253e85
00253E0C  4C 8B 4D A8                     mov r9, qword ptr [rbp - 0x58]
00253E10  E9 AB 03 00 00                  jmp 0x1402541c0
00253E15  41 0F B6 87 D9 35 00 00         movzx eax, byte ptr [r15 + 0x35d9]
00253E1D  84 C0                           test al, al
00253E1F  0F 85 CC 00 00 00               jne 0x140253ef1
00253E25  41 C6 87 D9 35 00 00 01         mov byte ptr [r15 + 0x35d9], 1
00253E2D  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
00253E30  41 89 87 DC 35 00 00            mov dword ptr [r15 + 0x35dc], eax
00253E37  41 F6 44 DE 33 02               test byte ptr [r14 + rbx*8 + 0x33], 2
00253E3D  0F 85 A1 01 00 00               jne 0x140253fe4
00253E43  41 F6 44 DE 33 04               test byte ptr [r14 + rbx*8 + 0x33], 4
00253E49  74 16                           je 0x140253e61
00253E4B  48 8B 86 B8 8E 00 00            mov rax, qword ptr [rsi + 0x8eb8]
00253E52  41 0F BE 4C DE 34               movsx ecx, byte ptr [r14 + rbx*8 + 0x34]
00253E58  48 85 C0                        test rax, rax
00253E5B  0F 85 DF 00 00 00               jne 0x140253f40
00253E61  41 F6 44 DE 33 01               test byte ptr [r14 + rbx*8 + 0x33], 1
00253E67  74 0D                           je 0x140253e76
00253E69  49 8B 44 DE 28                  mov rax, qword ptr [r14 + rbx*8 + 0x28]
00253E6E  66 F0 FF 88 64 03 00 00         lock dec word ptr [rax + 0x364]
00253E76  41 0F B6 06                     movzx eax, byte ptr [r14]
00253E7A  FF C7                           inc edi
00253E7C  3B F8                           cmp edi, eax
00253E7E  72 40                           jb 0x140253ec0
00253E80  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00253E85  80 7C 24 78 00                  cmp byte ptr [rsp + 0x78], 0
00253E8A  0F 85 63 12 00 00               jne 0x1402550f3
00253E90  80 7C 24 43 00                  cmp byte ptr [rsp + 0x43], 0
00253E95  0F 85 95 14 00 00               jne 0x140255330
00253E9B  E9 D8 14 00 00                  jmp 0x140255378
00253EA0  CC                              int3
00253EA1  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00253EA6  33 C0                           xor eax, eax
00253EA8  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00253EAC  48 89 7B 40                     mov qword ptr [rbx + 0x40], rdi
00253EB0  45 84 C9                        test r9b, r9b
00253EB3  74 D0                           je 0x140253e85
00253EB5  41 38 06                        cmp byte ptr [r14], al
00253EB8  76 CB                           jbe 0x140253e85
00253EBA  4C 8B 6D A0                     mov r13, qword ptr [rbp - 0x60]
00253EBE  66 90                           nop
00253EC0  8B C7                           mov eax, edi
00253EC2  48 8D 1C 80                     lea rbx, [rax + rax*4]
00253EC6  41 0F B6 44 DE 33               movzx eax, byte ptr [r14 + rbx*8 + 0x33]
00253ECC  49 8B 74 DE 10                  mov rsi, qword ptr [r14 + rbx*8 + 0x10]
00253ED1  A8 10                           test al, 0x10
00253ED3  0F 85 3C FF FF FF               jne 0x140253e15
00253ED9  A8 08                           test al, 8
00253EDB  0F 84 56 FF FF FF               je 0x140253e37
00253EE1  90                              nop
00253EE2  80 7E 07 00                     cmp byte ptr [rsi + 7], 0
00253EE6  0F 84 4B FF FF FF               je 0x140253e37
00253EEC  E9 24 FF FF FF                  jmp 0x140253e15
00253EF1  3C 01                           cmp al, 1
00253EF3  75 42                           jne 0x140253f37
00253EF5  41 8B 97 DC 35 00 00            mov edx, dword ptr [r15 + 0x35dc]
00253EFC  3B 56 24                        cmp edx, dword ptr [rsi + 0x24]
00253EFF  0F 84 32 FF FF FF               je 0x140253e37
00253F05  4D 8D A7 E0 35 00 00            lea r12, [r15 + 0x35e0]
00253F0C  41 C6 87 D9 35 00 00 02         mov byte ptr [r15 + 0x35d9], 2
00253F14  49 8B CC                        mov rcx, r12
00253F17  E8 D4 77 00 00                  call 0x14025b6f0
00253F1C  4C 8B 86 C8 00 00 00            mov r8, qword ptr [rsi + 0xc8]
00253F23  49 8B CC                        mov rcx, r12
00253F26  0F B6 96 D0 00 00 00            movzx edx, byte ptr [rsi + 0xd0]
00253F2D  E8 8E 77 00 00                  call 0x14025b6c0
00253F32  E9 00 FF FF FF                  jmp 0x140253e37
00253F37  4D 8D A7 E0 35 00 00            lea r12, [r15 + 0x35e0]
00253F3E  EB DC                           jmp 0x140253f1c
00253F40  49 83 BF B8 8E 00 00 00         cmp qword ptr [r15 + 0x8eb8], 0
00253F48  0F 84 13 FF FF FF               je 0x140253e61
00253F4E  4C 3B FE                        cmp r15, rsi
00253F51  0F 84 0A FF FF FF               je 0x140253e61
00253F57  8B 10                           mov edx, dword ptr [rax]
00253F59  8B C2                           mov eax, edx
00253F5B  25 00 00 04 00                  and eax, 0x40000
00253F60  0F BA E2 14                     bt edx, 0x14
00253F64  72 13                           jb 0x140253f79
00253F66  85 C0                           test eax, eax
00253F68  0F 84 F3 FE FF FF               je 0x140253e61
00253F6E  0F B6 C2                        movzx eax, dl
00253F71  3B C1                           cmp eax, ecx
00253F73  0F 8D E8 FE FF FF               jge 0x140253e61
00253F79  80 3D 87 10 D7 00 00            cmp byte ptr [rip + 0xd71087], 0
00253F80  BA 02 00 00 00                  mov edx, 2
00253F85  49 8B 8F B8 8E 00 00            mov rcx, qword ptr [r15 + 0x8eb8]
00253F8C  89 51 0C                        mov dword ptr [rcx + 0xc], edx
00253F8F  44 8B 66 24                     mov r12d, dword ptr [rsi + 0x24]
00253F93  75 23                           jne 0x140253fb8
00253F95  41 8B C4                        mov eax, r12d
00253F98  4C 8D 05 61 C0 DA FF            lea r8, [rip - 0x253f9f]
00253F9F  47 0F B6 A4 60 60 D2 FC 00      movzx r12d, byte ptr [r8 + r12*2 + 0xfcd260]
00253FA8  41 C1 E4 06                     shl r12d, 6
00253FAC  41 0F B6 84 40 61 D2 FC 00      movzx eax, byte ptr [r8 + rax*2 + 0xfcd261]
00253FB5  44 0B E0                        or r12d, eax
00253FB8  44 89 61 08                     mov dword ptr [rcx + 8], r12d
00253FBC  8B 05 52 2B D7 00               mov eax, dword ptr [rip + 0xd72b52]
00253FC2  A8 20                           test al, 0x20
00253FC4  74 08                           je 0x140253fce
00253FC6  8B 4E 24                        mov ecx, dword ptr [rsi + 0x24]
00253FC9  E8 F2 72 2A 00                  call 0x1404fb2c0
00253FCE  41 8B D4                        mov edx, r12d
00253FD1  B9 C2 00 00 40                  mov ecx, 0x400000c2
00253FD6  48 C1 EA 20                     shr rdx, 0x20
00253FDA  41 8B C4                        mov eax, r12d
00253FDD  0F 30                           wrmsr
00253FDF  E9 7D FE FF FF                  jmp 0x140253e61
00253FE4  49 8B 4C DE 28                  mov rcx, qword ptr [r14 + rbx*8 + 0x28]
00253FE9  48 8B D6                        mov rdx, rsi
00253FEC  48 3B 4C 24 48                  cmp rcx, qword ptr [rsp + 0x48]
00253FF1  0F 85 55 01 00 00               jne 0x14025414c
00253FF7  4D 8B C5                        mov r8, r13
00253FFA  E8 4D 77 0B 00                  call 0x14030b74c
00253FFF  E9 3F FE FF FF                  jmp 0x140253e43
00254004  4C 8B 55 80                     mov r10, qword ptr [rbp - 0x80]
00254008  0F B7 86 88 00 00 00            movzx eax, word ptr [rsi + 0x88]
0025400F  66 41 3B 02                     cmp ax, word ptr [r10]
00254013  0F 83 9B 0B 00 00               jae 0x140254bb4
00254019  4D 8B 44 C2 08                  mov r8, qword ptr [r10 + rax*8 + 8]
0025401E  0F B6 8E B9 00 00 00            movzx ecx, byte ptr [rsi + 0xb9]
00254025  0F B6 44 24 41                  movzx eax, byte ptr [rsp + 0x41]
0025402A  03 C8                           add ecx, eax
0025402C  48 8B 86 C0 00 00 00            mov rax, qword ptr [rsi + 0xc0]
00254033  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
00254037  4C 8B 4C C8 10                  mov r9, qword ptr [rax + rcx*8 + 0x10]
0025403C  48 8B 54 C8 08                  mov rdx, qword ptr [rax + rcx*8 + 8]
00254041  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00254045  49 23 D1                        and rdx, r9
00254048  49 23 D0                        and rdx, r8
0025404B  4D 23 C8                        and r9, r8
0025404E  0F 84 3C 08 00 00               je 0x140254890
00254054  48 85 D2                        test rdx, rdx
00254057  0F 84 AF 08 00 00               je 0x14025490c
0025405D  4C 8B 46 10                     mov r8, qword ptr [rsi + 0x10]
00254061  48 85 93 C8 00 00 00            test qword ptr [rbx + 0xc8], rdx
00254068  0F 85 3C 06 00 00               jne 0x1402546aa
0025406E  48 8B 8B 60 8E 00 00            mov rcx, qword ptr [rbx + 0x8e60]
00254075  44 8B F7                        mov r14d, edi
00254078  48 8B C1                        mov rax, rcx
0025407B  4D 8B CA                        mov r9, r10
0025407E  49 23 C0                        and rax, r8
00254081  49 8B D5                        mov rdx, r13
00254084  48 3B C1                        cmp rax, rcx
00254087  4C 8B C3                        mov r8, rbx
0025408A  48 8D 45 40                     lea rax, [rbp + 0x40]
0025408E  49 8B CC                        mov rcx, r12
00254091  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00254096  41 0F 94 C6                     sete r14b
0025409A  48 8D 45 88                     lea rax, [rbp - 0x78]
0025409E  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
002540A3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002540A8  E8 97 D0 16 00                  call 0x1403c1144
002540AD  85 C0                           test eax, eax
002540AF  0F 89 83 00 00 00               jns 0x140254138
002540B5  4C 3B E6                        cmp r12, rsi
002540B8  0F 85 41 0A 00 00               jne 0x140254aff
002540BE  0F B6 75 98                     movzx esi, byte ptr [rbp - 0x68]
002540C2  44 8B 5D 9C                     mov r11d, dword ptr [rbp - 0x64]
002540C6  40 88 74 24 41                  mov byte ptr [rsp + 0x41], sil
002540CB  44 89 5C 24 50                  mov dword ptr [rsp + 0x50], r11d
002540D0  E9 98 FA FF FF                  jmp 0x140253b6d
002540D5  32 C0                           xor al, al
002540D7  E9 B6 F4 FF FF                  jmp 0x140253592
002540DC  48 81 C2 38 01 00 00            add rdx, 0x138
002540E3  E9 72 F9 FF FF                  jmp 0x140253a5a
002540E8  83 F8 07                        cmp eax, 7
002540EB  0F 85 D2 06 00 00               jne 0x1402547c3
002540F1  BA 02 00 00 00                  mov edx, 2
002540F6  E9 2C F1 FF FF                  jmp 0x140253227
002540FB  4C 8B CF                        mov r9, rdi
002540FE  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
00254102  E9 B5 F2 FF FF                  jmp 0x1402533bc
00254107  4C 8D 75 08                     lea r14, [rbp + 8]
0025410B  BA 01 00 00 00                  mov edx, 1
00254110  E9 9C FA FF FF                  jmp 0x140253bb1
00254115  85 D2                           test edx, edx
00254117  0F 84 6D FB FF FF               je 0x140253c8a
0025411D  41 F6 45 23 10                  test byte ptr [r13 + 0x23], 0x10
00254122  0F 85 EC 07 00 00               jne 0x140254914
00254128  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
0025412C  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
00254130  48 C7 45 48 01 00 00 00         mov qword ptr [rbp + 0x48], 1
00254138  44 0F B6 6C 24 42               movzx r13d, byte ptr [rsp + 0x42]
0025413E  45 32 F6                        xor r14b, r14b
00254141  44 0F B6 64 24 40               movzx r12d, byte ptr [rsp + 0x40]
00254147  E9 04 F2 FF FF                  jmp 0x140253350
0025414C  45 33 C0                        xor r8d, r8d
0025414F  E9 A6 FE FF FF                  jmp 0x140253ffa
00254154  80 C9 04                        or cl, 4
00254157  E9 83 F3 FF FF                  jmp 0x1402534df
0025415C  49 83 C7 08                     add r15, 8
00254160  49 83 EC 01                     sub r12, 1
00254164  0F 85 06 F6 FF FF               jne 0x140253770
0025416A  44 8B 4C 24 70                  mov r9d, dword ptr [rsp + 0x70]
0025416F  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00254174  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
00254178  32 18                           xor bl, byte ptr [rax]
0025417A  0F 88 FD 09 00 00               js 0x140254b7d
00254180  48 8D 4D 40                     lea rcx, [rbp + 0x40]
00254184  E8 E7 2A 00 00                  call 0x140256c70
00254189  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0025418E  89 45 48                        mov dword ptr [rbp + 0x48], eax
00254191  89 7D 4C                        mov dword ptr [rbp + 0x4c], edi
00254194  44 89 AB 18 02 00 00            mov dword ptr [rbx + 0x218], r13d
0025419B  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
0025419F  48 85 C0                        test rax, rax
002541A2  0F 84 54 06 00 00               je 0x1402547fc
002541A8  44 8B 8E D8 00 00 00            mov r9d, dword ptr [rsi + 0xd8]
002541AF  4C 03 C8                        add r9, rax
002541B2  44 0F B6 6C 24 42               movzx r13d, byte ptr [rsp + 0x42]
002541B8  4C 89 4D A8                     mov qword ptr [rbp - 0x58], r9
002541BC  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
002541C0  49 8B D1                        mov rdx, r9
002541C3  45 84 ED                        test r13b, r13b
002541C6  75 16                           jne 0x1402541de
002541C8  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
002541D2  8B 00                           mov eax, dword ptr [rax]
002541D4  4C 8B 4D A8                     mov r9, qword ptr [rbp - 0x58]
002541D8  89 83 B4 01 00 00               mov dword ptr [rbx + 0x1b4], eax
002541DE  4D 85 C9                        test r9, r9
002541E1  75 16                           jne 0x1402541f9
002541E3  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
002541E7  48 85 C0                        test rax, rax
002541EA  0F 84 CB 05 00 00               je 0x1402547bb
002541F0  8B 96 D8 00 00 00               mov edx, dword ptr [rsi + 0xd8]
002541F6  48 03 D0                        add rdx, rax
002541F9  48 8B 86 B8 8E 00 00            mov rax, qword ptr [rsi + 0x8eb8]
00254200  48 85 C0                        test rax, rax
00254203  74 04                           je 0x140254209
00254205  40 88 78 10                     mov byte ptr [rax + 0x10], dil
00254209  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
0025420E  C6 83 84 01 00 00 01            mov byte ptr [rbx + 0x184], 1
00254215  32 DB                           xor bl, bl
00254217  48 85 D2                        test rdx, rdx
0025421A  0F 85 03 04 00 00               jne 0x140254623
00254220  41 F7 47 78 00 00 40 00         test dword ptr [r15 + 0x78], 0x400000
00254228  4D 0F BE B7 C3 00 00 00         movsx r14, byte ptr [r15 + 0xc3]
00254230  0F 85 BF 09 00 00               jne 0x140254bf5
00254236  49 8B CF                        mov rcx, r15
00254239  E8 22 91 FC FF                  call 0x14021d360
0025423E  41 F7 47 78 00 20 00 00         test dword ptr [r15 + 0x78], 0x2000
00254246  48 8B 8E 40 8E 00 00            mov rcx, qword ptr [rsi + 0x8e40]
0025424D  0F 84 99 04 00 00               je 0x1402546ec
00254253  48 85 C9                        test rcx, rcx
00254256  0F 84 90 04 00 00               je 0x1402546ec
0025425C  49 8B 97 40 02 00 00            mov rdx, qword ptr [r15 + 0x240]
00254263  0F B6 86 D0 00 00 00            movzx eax, byte ptr [rsi + 0xd0]
0025426A  66 3B 02                        cmp ax, word ptr [rdx]
0025426D  0F 83 95 09 00 00               jae 0x140254c08
00254273  48 8B 54 C2 08                  mov rdx, qword ptr [rdx + rax*8 + 8]
00254278  48 8B C1                        mov rax, rcx
0025427B  48 23 C2                        and rax, rdx
0025427E  48 3B C1                        cmp rax, rcx
00254281  0F 85 65 04 00 00               jne 0x1402546ec
00254287  84 DB                           test bl, bl
00254289  0F 85 5D 04 00 00               jne 0x1402546ec
0025428F  48 8B 9E 48 8E 00 00            mov rbx, qword ptr [rsi + 0x8e48]
00254296  0F 57 C0                        xorps xmm0, xmm0
00254299  49 8D 76 04                     lea rsi, [r14 + 4]
0025429D  48 C1 E6 04                     shl rsi, 4
002542A1  48 03 F3                        add rsi, rbx
002542A4  F7 05 8A 28 D7 00 00 00 20 00   test dword ptr [rip + 0xd7288a], 0x200000
002542AE  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
002542B2  0F 85 B7 01 00 00               jne 0x14025446f
002542B8  89 7D D8                        mov dword ptr [rbp - 0x28], edi
002542BB  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
002542C1  0F 83 C1 01 00 00               jae 0x140254488
002542C7  E9 FC 3F 48 00                  jmp 0x1406d82c8
002542CC  8B 05 E6 27 D7 00               mov eax, dword ptr [rip + 0xd727e6]
002542D2  A8 40                           test al, 0x40
002542D4  0F 84 C3 F4 FF FF               je 0x14025379d
002542DA  E8 B1 B1 0B 00                  call 0x14030f490
002542DF  84 C0                           test al, al
002542E1  0F 84 B6 F4 FF FF               je 0x14025379d
002542E7  41 8B CE                        mov ecx, r14d
002542EA  E8 71 B1 0B 00                  call 0x14030f460
002542EF  E9 AB F4 FF FF                  jmp 0x14025379f
002542F4  48 8B 8B C8 03 00 00            mov rcx, qword ptr [rbx + 0x3c8]
002542FB  0F BE 93 C3 00 00 00            movsx edx, byte ptr [rbx + 0xc3]
00254302  8B 01                           mov eax, dword ptr [rcx]
00254304  44 0F B6 C0                     movzx r8d, al
00254308  41 3B D0                        cmp edx, r8d
0025430B  0F 84 A7 EE FF FF               je 0x1402531b8
00254311  8B C2                           mov eax, edx
00254313  41 2B C0                        sub eax, r8d
00254316  F0 01 01                        lock add dword ptr [rcx], eax
00254319  E9 9A EE FF FF                  jmp 0x1402531b8
0025431E  80 BB C3 00 00 00 10            cmp byte ptr [rbx + 0xc3], 0x10
00254325  0F 8D 91 F0 FF FF               jge 0x1402533bc
0025432B  F7 43 78 00 02 00 00            test dword ptr [rbx + 0x78], 0x200
00254332  0F 85 84 F0 FF FF               jne 0x1402533bc
00254338  49 8B C9                        mov rcx, r9
0025433B  F6 41 70 02                     test byte ptr [rcx + 0x70], 2
0025433F  0F 85 AB 05 00 00               jne 0x1402548f0
00254345  48 8B 89 A0 01 00 00            mov rcx, qword ptr [rcx + 0x1a0]
0025434C  48 85 C9                        test rcx, rcx
0025434F  75 EA                           jne 0x14025433b
00254351  E9 66 F0 FF FF                  jmp 0x1402533bc
00254356  41 38 B9 C3 00 00 00            cmp byte ptr [r9 + 0xc3], dil
0025435D  0F 8E FB ED FF FF               jle 0x14025315e
00254363  0F BE 5C 24 43                  movsx ebx, byte ptr [rsp + 0x43]
00254368  41 3A 99 66 03 00 00            cmp bl, byte ptr [r9 + 0x366]
0025436F  0F 8E F5 ED FF FF               jle 0x14025316a
00254375  E8 46 B4 29 00                  call 0x1404ef7c0
0025437A  85 C0                           test eax, eax
0025437C  BA 0F 00 00 00                  mov edx, 0xf
00254381  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00254386  0F 85 3C 05 00 00               jne 0x1402548c8
0025438C  0F BE 80 33 02 00 00            movsx eax, byte ptr [rax + 0x233]
00254393  03 D8                           add ebx, eax
00254395  83 FB 10                        cmp ebx, 0x10
00254398  0F 4D DA                        cmovge ebx, edx
0025439B  2B D8                           sub ebx, eax
0025439D  E8 1E B4 29 00                  call 0x1404ef7c0
002543A2  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002543A7  45 33 C0                        xor r8d, r8d
002543AA  33 D2                           xor edx, edx
002543AC  48 8B C8                        mov rcx, rax
002543AF  88 98 66 03 00 00               mov byte ptr [rax + 0x366], bl
002543B5  48 8B D8                        mov rbx, rax
002543B8  E8 37 02 17 00                  call 0x1403c45f4
002543BD  44 0F B6 F0                     movzx r14d, al
002543C1  E9 A9 ED FF FF                  jmp 0x14025316f
002543C6  4C 8D 55 F0                     lea r10, [rbp - 0x10]
002543CA  41 B9 01 00 00 00               mov r9d, 1
002543D0  4C 89 55 80                     mov qword ptr [rbp - 0x80], r10
002543D4  44 8B C7                        mov r8d, edi
002543D7  44 89 4C 24 58                  mov dword ptr [rsp + 0x58], r9d
002543DC  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
002543E0  E9 7E F0 FF FF                  jmp 0x140253463
002543E5  85 D2                           test edx, edx
002543E7  0F 84 56 03 00 00               je 0x140254743
002543ED  83 FA 01                        cmp edx, 1
002543F0  75 0F                           jne 0x140254401
002543F2  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
002543F9  44 0F B6 08                     movzx r9d, byte ptr [rax]
002543FD  4C 8D 40 08                     lea r8, [rax + 8]
00254401  B9 01 00 00 00                  mov ecx, 1
00254406  45 85 C9                        test r9d, r9d
00254409  0F 84 75 EF FF FF               je 0x140253384
0025440F  41 8B D1                        mov edx, r9d
00254412  49 8B 00                        mov rax, qword ptr [r8]
00254415  4D 8D 40 08                     lea r8, [r8 + 8]
00254419  0F B6 40 23                     movzx eax, byte ptr [rax + 0x23]
0025441D  F6 D0                           not al
0025441F  83 E0 01                        and eax, 1
00254422  23 C8                           and ecx, eax
00254424  48 83 EA 01                     sub rdx, 1
00254428  75 E8                           jne 0x140254412
0025442A  E9 55 EF FF FF                  jmp 0x140253384
0025442F  4C 3B 6B 20                     cmp r13, qword ptr [rbx + 0x20]
00254433  0F 83 87 09 00 00               jae 0x140254dc0
00254439  0F B6 83 35 02 00 00            movzx eax, byte ptr [rbx + 0x235]
00254440  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00254444  E9 8A ED FF FF                  jmp 0x1402531d3
00254449  4C 8D 65 20                     lea r12, [rbp + 0x20]
0025444D  B9 01 00 00 00                  mov ecx, 1
00254452  E9 D1 F3 FF FF                  jmp 0x140253828
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0025308F(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned __int8 a8, __int64 a9, unsigned int a10, unsigned int a11, unsigned int a12, __int64 a13, unsigned int a14, unsigned __int8 a15)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    unsigned __int64 v_stack_p1B8;
    unsigned __int8 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p41;
    unsigned __int8 v_stack_p42;
    unsigned __int8 v_stack_p43;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int8 v_stack_p54;
    unsigned __int8 v_stack_p55;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;

    v_stack_p1B8 = v_r12;
    *(unsigned __int64 *)(v_rbp - 24) = v_rdi;
    v_r12 = 0;
    if ((*(unsigned __int8 *)(v_rbx + 566)) == ((unsigned __int8)(v_rsi))) goto loc_0025442F;
    v_rbx = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) - (*(unsigned int *)(a9 + 436)));
    if (v_r13 >= (*(unsigned __int64 *)(a9 + 32))) goto loc_00253101;
    if ((*(unsigned __int8 *)(a9 + 563)) >= 14) goto loc_0025310C;
    if (((*(unsigned __int16 *)(a9 + 518)) & ((unsigned __int16)((unsigned int)(0xFF0ULL)))) != 0) goto loc_0025312E;
    if (((unsigned int)(a1)) >= 2) goto loc_0025310C;
    goto loc_0025312E;
loc_00253101:
loc_0025310C:
    result = KiComputeNewPriority(a9, (unsigned int)(0xFF0ULL), 1, a9);
    v_r14 = 63;
    if (0 == 0) { v_r14 = (unsigned int)((unsigned __int8)(result)); }
loc_0025312E:
    v_rbx = 4;
    if (!(condition_is_above_or_equal)) {
        v_rbx = (unsigned __int8)((4) | (2));
    }
    result = (unsigned __int8)(~((unsigned __int8)(v_rbx)));
    a1 = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a9 + 120)))) & (8)) == 0) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    if ((((unsigned __int8)(a1)) & (1)) != 0) goto loc_00254356;
loc_0025315E:
loc_0025316A:
loc_0025316F:
    if (((unsigned __int8)(v_r14)) == 63) goto loc_002531B8;
    *(unsigned __int8 *)(a9 + 195) = (unsigned __int8)(v_r14);
    result = KiComputeThreadQos(a9, *(unsigned __int64 *)(gs_base + (0 + 32)), 1, a9);
    if (((unsigned int)(result)) != ((unsigned int)(*(unsigned __int8 *)(a9 + 516)))) {
        *(unsigned __int8 *)(a9 + 516) = (unsigned __int8)(result);
    }
    if (((*(unsigned int *)(a9 + 120)) & (0x400000ULL)) != 0) goto loc_002542F4;
loc_002531B8:
    v_rsi = (unsigned __int8)((1) & (1));
loc_002531D3:
    result = KiComputeThreadQos(a9, *(unsigned __int64 *)(gs_base + (0 + 32)), 1, a9);
    if ((unsigned __int8)(v_rsi) == 0) goto loc_00253244;
    if (((*(unsigned int *)(v_rip + 14104888)) & (0x40000ULL)) == 0) goto loc_00253227;
    if ((*(unsigned __int8 *)(v_rip + 14104805)) == ((unsigned __int8)(v_rdi))) goto loc_00253227;
    if (((unsigned int)(*(unsigned __int8 *)(a9 + 516))) != 4) goto loc_002540E8;
loc_00253227:
    a2 = (unsigned int)((36) * (*(unsigned int *)(v_rip + 14098026)));
    a1 = ((unsigned int)((unsigned int)(a2))) + (v_r13);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a9 + 120)))) & (32)) != 0) {
    }
    *(unsigned __int64 *)(a9 + 32) = a1;
loc_00253244:
    *(unsigned int *)(v_rbp - 64) = (unsigned int)((unsigned int)(*(unsigned int *)(a9 + 588)));
    *(unsigned __int16 *)(a9 + 565) = (unsigned __int16)(v_rdi);
    if ((*(unsigned int *)(a9 + 484)) != ((unsigned int)(v_rdi))) goto loc_00253269;
loc_00253269:
    v_r14 = 0;
    v_stack_p40 = 1;
    v_r13 = (condition_is_below) ? 1 : 0;
    v_stack_p42 = (unsigned __int8)(v_r13);
    *(unsigned int *)(v_rbp - 36) = (unsigned int)((unsigned int)(*(unsigned int *)(a9 + 588)));
    result = 0;
    v_stack_p43 = 0;
    result = 0;
    *(unsigned __int64 *)(v_rbp + 72) = v_rdi;
    *(unsigned __int64 *)(v_rbp + 64) = 0;
    if ((*(unsigned int *)(v_rip + 14105881)) == 0) goto loc_002536AC;
loc_002532E1:
    if (((unsigned __int16)(v_rdi)) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a9 + 576))))) goto loc_002537AA;
    a2 = (*(unsigned __int64 *)(a9 + 576)) + (8);
loc_002532FE:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + ((unsigned int)(a1)));
    a4 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a9 + 576))))) - (1);
    if (condition_is_not_equal) goto loc_002532FE;
    if (((unsigned int)(a3)) <= 1) goto loc_002537AA;
    if ((*(unsigned int *)(v_rip + 14104661)) != ((unsigned int)(v_rdi))) goto loc_002538C9;
    v_stack_p20 = 0;
    result = KiChooseTargetProcessor(v_r15, a9, *(unsigned __int64 *)(a9 + 576), v_rbp + 64);
loc_00253350:
    v_rsi = (*(unsigned __int64 *)(v_rbp + 64)) & (-2);
    v_stack_p60 = v_rsi;
loc_0025335D:
    a1 = (*(unsigned __int64 *)(v_rbp + 64)) & (-2);
    *(unsigned __int64 *)(v_rbp + 40) = a1;
    a2 = (unsigned int)((*(unsigned __int64 *)(v_rbp + 64)) & (1));
    if (condition_is_not_equal) goto loc_002543E5;
    a1 = (unsigned __int8)(~(*(unsigned __int8 *)(a1 + 35)));
    a1 = (unsigned int)((a1) & (1));
loc_00253384:
    *(unsigned int *)(a9 + 536) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 36)));
    if (*(unsigned __int64 *)(a9 + 104) == 0) goto loc_002540FB;
    a4 = ((unsigned int)(*(unsigned int *)(v_rsi + 216))) + (*(unsigned __int64 *)(a9 + 104));
    *(unsigned __int64 *)(v_rbp - 88) = a4;
    if (condition_is_not_equal) goto loc_0025431E;
loc_002533BC:
    if ((*(unsigned int *)(v_rip + 14098206)) == ((unsigned int)(v_rdi))) goto loc_002533CE;
loc_002533CE:
    if ((*(unsigned int *)(v_rbp + 72)) == ((unsigned int)(v_rdi))) goto loc_00253DD1;
    a2 = 0;
    v_rsi = (*(unsigned __int64 *)(v_rbp + 64)) & (-2);
    v_stack_p60 = v_rsi;
    result = memset(*(unsigned __int64 *)(v_r15 + 14312), a2, 240, a4);
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp + 64)))) & (1));
    *(unsigned __int64 *)(v_rbp - 128) = v_rdi;
    v_stack_p70 = (unsigned int)(v_r11);
    v_stack_p58 = (unsigned int)((unsigned int)((unsigned int)(v_rdi)));
    *(unsigned __int64 *)(v_rbp - 16) = v_rsi;
    v_stack_p68 = (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp + 64)));
    if (condition_is_equal) goto loc_002543C6;
    v_r10 = v_rdi;
    if (((unsigned int)(v_r11)) == 1) {
        result = *(unsigned __int64 *)(v_rsi + 36440);
        v_r10 = *(unsigned __int64 *)(v_rsi + 36440);
        v_r10 = (v_r10) + (8);
        *(unsigned __int64 *)(v_rbp - 128) = v_r10;
        a4 = *(unsigned __int8 *)(result);
        v_stack_p58 = (unsigned int)(a4);
    }
    v_stack_p50 = (unsigned int)(v_rdi);
    if ((unsigned int)(a4) == 0) goto loc_0025356E;
loc_00253463:
    v_stack_p68 = a4;
loc_00253471:
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48 - 32) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48 - 16) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48 - 8) = -1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48 + 4) = 63;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48 - 32) = *(unsigned __int64 *)(v_r10);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48 - 24) = v_rdi;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48 - 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r10) + 16);
    v_rsi = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r10) + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r10) + 16) == 0) {
        v_rsi = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r10) + 8);
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48 - 16) = v_rsi;
    }
    if ((*(unsigned __int64 *)(v_r10)) == (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_00254154;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48)) & (251));
loc_002534DF:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48) = (unsigned __int8)(a1);
    v_r12 = 0;
    result = (unsigned __int8)(~(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r10) + 35)));
    result = (unsigned __int8)((result) & (1));
    a2 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48)) & (254));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48) = (unsigned __int8)(a2);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r10) + 56))) >> (6));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(a2)));
    a1 = (unsigned __int8)((a1) & (2));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(a2)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312) + 48) = (unsigned __int8)((unsigned __int8)(a1));
    result = (unsigned int)(((unsigned __int8)(a1)) >> (1));
    result = (unsigned int)((result) & (1));
    a3 = (unsigned int)((unsigned int)(v_rdi));
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)((unsigned int)(v_rdi))))) { a3 = (unsigned int)(result); }
    v_r10 = (v_r10) + (8);
    v_rbx = (*(unsigned __int64 *)(v_r15 + 14312) + 48) + (40);
    v_stack_p50 = (unsigned int)(a3);
    a4 = (a4) - (1);
    *(unsigned __int64 *)(v_rbp - 128) = v_r10;
    v_stack_p68 = a4;
    if (condition_is_not_equal) goto loc_00253471;
    v_stack_p68 = *(unsigned __int64 *)(v_rbp + 64);
loc_0025356E:
    *(unsigned int *)(*(unsigned __int64 *)(v_r15 + 14312) + 4) = (unsigned int)(a3);
    *(unsigned int *)(*(unsigned __int64 *)(v_r15 + 14312) + 8) = (unsigned int)((unsigned int)(a14));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312)) = (unsigned __int8)((unsigned int)(a11));
    if ((unsigned int)((unsigned int)(a14)) == 0) goto loc_002540D5;
loc_00253592:
    *(unsigned __int8 *)(1 + *(unsigned __int64 *)(v_r15 + 14312) * 1) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 16) + 36440) + 1));
loc_002535B0:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312))))) goto loc_002535CE;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16)) == a12) goto loc_002535CA;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + 1);
    goto loc_002535B0;
loc_002535CA:
loc_002535CE:
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(a9 + 120))) >> (1));
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16 + 32)) >> (1));
    v_r10 = (unsigned int)((v_r10) & (1));
    result = (unsigned int)((result) & (1));
    v_stack_p70 = (unsigned int)(v_r10);
loc_0025360C:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 48)) | (1));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 24);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 48) = (unsigned __int8)(result);
    result = (unsigned __int8)((result) & (253));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 24) + 120))) >> (1));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) & (231));
    a1 = (unsigned __int8)((a1) | (4));
    a1 = (unsigned __int8)((a1) & (223));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 48) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 24);
    result = KiIsPrcbThread(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 24), a2, *(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312)), *(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 36);
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 24) + 536) = (unsigned int)(result);
    }
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + 1);
    if (((unsigned int)(v_r11)) < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r15 + 14312))))) goto loc_0025360C;
loc_002536AC:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13434138)))) != 4) goto loc_002532E1;
    v_stack_p60 = *(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 536)) * 8 + 16550976);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 576) + *(unsigned __int8 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 536)) * 8 + 16550976) + 208) * 8 + 8)) >> ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 536)) * 8 + 16550976) + 209)));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 120))) >> (1));
    a4 = (unsigned int)((a4) & (1));
    v_stack_p70 = (unsigned int)(a4);
    *(unsigned __int64 *)(v_rbp - 8) = *(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 536)) * 8 + 16550976);
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 536)) * 8 + 16550976) + 56))))) >> (7));
    a2 = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(a4)) < ((unsigned int)(result))) { a2 = (unsigned int)(result); }
    a1 = (*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 536)) * 8 + 16550976)) & (-2);
    a1 = (a1) | ((unsigned int)((unsigned int)(a2)));
    *(unsigned __int64 *)(v_rbp + 64) = a1;
    if (((unsigned int)(a2)) != 1) goto loc_00254174;
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 536)) * 8 + 16550976) + 36440))) == 0) goto loc_00254174;
loc_00253770:
loc_00253780:
    if (condition_is_above_or_equal) goto loc_0025415C;
loc_0025378D:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + 1);
    if (((*(unsigned int *)(v_rip + 14097173)) & ((unsigned int)(v_r14))) == 0) goto loc_002542CC;
loc_0025379D:
loc_0025379F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 536)) * 8 + 16550976) + 36440) + 8) + 48) == 0) goto loc_00253780;
    goto loc_0025378D;
loc_002537AA:
    result = KeFindFirstSetLeftAffinityEx(*(unsigned __int64 *)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 536)) * 8 + 16550976) + 56)) + 576), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 576), a4);
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 536)) * 8 + 16550976) + 56)) + 120))) >> (1));
    a4 = (unsigned int)((a4) & (1));
    v_stack_p70 = (unsigned int)(a4);
    v_stack_p60 = *(unsigned __int64 *)(v_rip - 2439105 + (unsigned int)((unsigned int)(result)) * 8 + 16550976);
    *(unsigned __int64 *)(v_rbp + 32) = *(unsigned __int64 *)(v_rip - 2439105 + (unsigned int)((unsigned int)(result)) * 8 + 16550976);
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2439105 + (unsigned int)((unsigned int)(result)) * 8 + 16550976) + 56))))) >> (7));
    a2 = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(a4)) < ((unsigned int)(result))) { a2 = (unsigned int)(result); }
    a1 = (*(unsigned __int64 *)(v_rip - 2439105 + (unsigned int)((unsigned int)(result)) * 8 + 16550976)) & (-2);
    a1 = (a1) | ((unsigned int)((unsigned int)(a2)));
    *(unsigned __int64 *)(v_rbp + 64) = a1;
    if ((unsigned int)(a2) == 0) goto loc_00254449;
    if (((unsigned int)(a2)) != 1) goto loc_0025388C;
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2439105 + (unsigned int)((unsigned int)(result)) * 8 + 16550976) + 36440))) == 0) goto loc_00253886;
loc_00253828:
loc_00253840:
loc_00253847:
    if (condition_is_above_or_equal) goto loc_00253869;
loc_00253850:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + 1);
    if (((*(unsigned int *)(v_rip + 14096978)) & ((unsigned int)(v_r14))) == 0) goto loc_002538AC;
loc_0025385C:
loc_0025385E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2439105 + (unsigned int)((unsigned int)(result)) * 8 + 16550976) + 36440) + 8) + 48) == 0) goto loc_00253847;
    goto loc_00253850;
loc_00253869:
    v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2439105 + (unsigned int)((unsigned int)(result)) * 8 + 16550976) + 36440) + 8) + (8);
    v_r13 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2439105 + (unsigned int)((unsigned int)(result)) * 8 + 16550976) + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_00253840;
    v_r14 = 0;
loc_00253886:
loc_0025388C:
    v_rbx = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 2439105 + (unsigned int)((unsigned int)(result)) * 8 + 16550976) + 56))) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(a12 + 56))));
    result = KiIsIsolationUnitIdleByHandle(v_rbp + 64, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 576), (unsigned int)(a14));
    *(unsigned int *)(v_rbp + 72) = (unsigned int)(result);
    *(unsigned int *)(v_rbp + 76) = (unsigned int)(v_rdi);
    goto loc_0025335D;
loc_002538AC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14103046)))) & (64)) == 0) goto loc_0025385C;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rbp + 64, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 576), (unsigned int)(a14));
    if ((unsigned __int8)(result) == 0) goto loc_0025385C;
    result = HvlNotifyLongSpinWait(0, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 576), (unsigned int)(a14));
    goto loc_0025385E;
loc_002538C9:
    result = 0;
    *(unsigned __int64 *)(v_rbp - 104) = 0;
    *(unsigned __int64 *)(v_rbp - 120) = v_xmm0;
    a1 = (unsigned int)(*(unsigned int *)(v_rbx + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 84))))) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 84))); }
    *(unsigned int *)(v_rbp + 160) = 0x2030405ULL;
    *(unsigned __int16 *)(v_rbp + 164) = 6;
    a2 = (((unsigned int)(a1)) >= (*(unsigned int *)(v_rip + 14097011))) ? 1 : 0;
    *(unsigned __int8 *)(v_rbp + 166) = 1;
    *(unsigned __int64 *)(v_rbp - 128) = *(unsigned __int64 *)(v_rbx + 576);
    *(unsigned __int64 *)(v_rbp - 56) = v_rdi;
    *(unsigned int *)(v_rbp - 116) = (unsigned int)(*(unsigned __int8 *)(v_rbx + 516));
    *(unsigned int *)(v_rbp - 112) = (unsigned int)(a2);
    *(unsigned int *)(v_rbp - 108) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + (unsigned int)((unsigned int)(a2)) + *(unsigned __int8 *)(v_rbx + 516) * 2 * 4 + 16536672)));
    v_stack_p55 = (unsigned __int8)(*(unsigned __int8 *)(v_rbp + *(unsigned __int8 *)(v_rbx + 516) * 1 + 160));
    *(unsigned __int8 *)(v_rbp - 120) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 195));
    v_stack_p41 = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 517));
    *(unsigned __int8 *)(v_rbp - 104) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 517));
    v_stack_p54 = (unsigned __int8)(v_rdi);
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 120))) >> (1));
    v_rbx = (unsigned int)((v_rbx) & (1));
    *(unsigned __int16 *)(v_rbp - 102) = (unsigned __int16)(v_stack_p54);
    v_stack_p50 = (unsigned int)(v_rbx);
    *(unsigned int *)(v_rbp - 100) = (unsigned int)(v_rbx);
    v_stack_p68 = *(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(a9 + 588)) * 8 + 16550976);
loc_002539A0:
    *(unsigned __int64 *)(v_rbp) = v_rdi;
    v_stack_p70 = (unsigned int)(v_rdi);
    v_stack_p54 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(a9 + 588)) * 8 + 16550976) + 192) + 138));
    v_stack_p60 = (unsigned int)(*(unsigned __int16 *)(v_rbp + 2));
loc_002539C6:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rbp + 2)) != 0) goto loc_00253D5E;
    v_stack_p60 = 1;
loc_002539DA:
    if (((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(a9 + 588)) * 8 + 16550976) + 192) + 138)))) == -1) goto loc_00253D8F;
    *(unsigned __int64 *)(v_rbp + 112) = v_xmm0;
    *(unsigned __int64 *)(v_rbp + 128) = v_xmm1;
    *(unsigned __int64 *)(v_rbp + 144) = v_xmm1;
    result = KiIsQosGroupingClass((unsigned int)(*(unsigned int *)(v_rbp - 116)), *(unsigned __int16 *)(v_rbp + 2), (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(a14));
    if ((unsigned __int8)(result) != 0) goto loc_00253D2E;
    if (((*(unsigned int *)(v_rip + 14102804)) & (0x800000ULL)) == 0) goto loc_00253D2E;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r11 + (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(a9 + 588)) * 8 + 16550976) + 192) + 138)) * 8 + 16578240) + 10)) & (8)) == 0) goto loc_00253D2E;
loc_00253A3C:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp - 108))) + (-3));
    a2 = ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 517))) << (5);
    if (((unsigned int)(result)) > 1) goto loc_002540DC;
    a2 = (a2) + (568);
loc_00253A5A:
    a2 = (a2) + (*(unsigned __int64 *)(v_r11 + (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(a9 + 588)) * 8 + 16550976) + 192) + 138)) * 8 + 16578240));
    result = RtlCopyVolatileMemory(v_rbp + 128, a2, 32, (unsigned int)(a14));
loc_00253A6F:
    *(unsigned __int64 *)(v_rbp + 112) = v_xmm0;
loc_00253A79:
    result = KeIsEmptyGroupMask(v_rbp + 112, a2, 32, (unsigned int)(a14));
    if ((unsigned int)(result) != 0) goto loc_00253C03;
    a3 = 0;
    *(unsigned __int64 *)(v_rbp + 80) = v_xmm0;
    *(unsigned __int64 *)(v_rbp + 96) = v_xmm1;
loc_00253AA1:
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_00253BE9;
loc_00253AB4:
    a1 = (v_rdi) + 1;
    a2 = (result + 32) - (1);
    if (condition_is_not_equal) goto loc_00253AA1;
    *(unsigned __int64 *)(v_rbp + 80) = v_xmm0;
loc_00253AC6:
    result = KeIsEmptyGroupMask(v_rbp + 80, a2, a3, (unsigned int)(a14));
    if ((unsigned int)(result) != 0) goto loc_00253A79;
    result = ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(a9 + 588)) * 8 + 16550976) + 192) + 138)) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r11 + (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(a9 + 588)) * 8 + 16550976) + 192) + 138)) * 8 + 16578240))))) ? 1 : 0;
    v_stack_p28 = 1;
    v_stack_p20 = v_rbp - 120;
    result = KiHeteroSelectIdleProcessorFromSubNode(a9, *(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(a9 + 588)) * 8 + 16550976) + 192), *(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(a9 + 588)) * 8 + 16550976), *(unsigned __int64 *)(v_rbp - 128));
    if (result == 0) goto loc_00253D36;
    if ((*(unsigned int *)(v_rbp - 112)) != 1) goto loc_00253B68;
    if ((*(unsigned int *)(v_rbp - 116)) != ((unsigned int)(v_rdi))) goto loc_00253B68;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp - 108))) - 1);
    if (((unsigned int)(result)) > 1) goto loc_00253B68;
    if ((unsigned int)((unsigned int)(a10)) == 0) goto loc_00254004;
loc_00253B68:
loc_00253B6D:
    *(unsigned __int64 *)(v_rbp + 8) = result;
    a1 = ((int)((unsigned int)((unsigned int)(a10)))) ^ (result);
    a1 = (a1) & (-2);
    a1 = (a1) ^ ((int)((unsigned int)((unsigned int)(a10))));
    *(unsigned __int64 *)(v_rbp - 56) = a1;
    if ((unsigned int)((unsigned int)(a10)) == 0) goto loc_00254107;
    if (((unsigned int)((unsigned int)(a10))) != 1) goto loc_00253C62;
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 36440))) == 0) goto loc_00253C62;
loc_00253BB1:
loc_00253BC0:
loc_00253BC5:
    if (condition_is_above_or_equal) goto loc_00253C40;
loc_00253BCE:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + 1);
    if (((*(unsigned int *)(v_rip + 14096086)) & ((unsigned int)(v_rsi))) == 0) goto loc_00253D07;
loc_00253BDC:
loc_00253BDE:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 36440) + 8) + 48) == 0) goto loc_00253BC5;
    goto loc_00253BCE;
loc_00253BE9:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbp + a1 * 1 + 128))) != ((unsigned __int8)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(a9 + 588)) * 8 + 16550976)))) goto loc_00253C2D;
loc_00253BF6:
    goto loc_00253AB4;
loc_00253C03:
    if (((unsigned int)(*(unsigned __int64 *)(result + 36440) + 8)) > a10) goto loc_00253D87;
    goto loc_002539C6;
loc_00253C2D:
    if (((unsigned int)(*(unsigned __int64 *)(result + 36440) + 8)) <= a10) goto loc_00253AB4;
    *(unsigned __int64 *)(v_rbp + 96) = v_xmm0;
    goto loc_00253BF6;
loc_00253C40:
    v_r14 = (*(unsigned __int64 *)(result + 36440) + 8) + (8);
    v_r12 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 36440))))) - (1);
    if (condition_is_not_equal) goto loc_00253BC0;
    v_stack_p41 = (unsigned __int8)(*(unsigned __int8 *)(v_rbp - 104));
    v_stack_p50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 100)));
loc_00253C62:
    a2 = (*(unsigned __int64 *)(v_rbp - 56)) & (-2);
    *(unsigned __int64 *)(v_rbp + 16) = a2;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rbp - 56)))) & (1));
    if (((*(unsigned __int8 *)(a2 + 35)) & (1)) == 0) goto loc_0025411D;
loc_00253C8A:
    a4 = (*(unsigned __int64 *)(v_rbp - 56)) & (-2);
    *(unsigned __int64 *)(v_rbp + 24) = a4;
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rbp - 56)) & (1));
    result = (unsigned int)(*(unsigned int *)(v_rbp - 100));
    if (((unsigned int)(a1)) == 1) {
        result = *(unsigned __int64 *)(a4 + 36440);
        a3 = *(unsigned __int64 *)(a4 + 36440);
        a3 = (a3) + (8);
        a2 = *(unsigned __int8 *)(result);
    }
    if ((unsigned int)(a2) == 0) goto loc_00253CF2;
loc_00253CD0:
    if ((unsigned int)(a2 - 1) != 0) goto loc_00253CD0;
    v_stack_p41 = (unsigned __int8)(*(unsigned __int8 *)(v_rbp - 104));
    v_stack_p50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 100)));
loc_00253CF2:
    *(unsigned __int64 *)(v_rbp - 56) = v_rdi;
    goto loc_002539A0;
loc_00253D07:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14101931)))) & (64)) == 0) goto loc_00253BDC;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(a3 + a2 - 1 * 8), (unsigned int)((unsigned int)(a2 - 1)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00253BDC;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rbp - 104))), (unsigned int)((unsigned int)(a2 - 1)), a3, a4);
    goto loc_00253BDE;
loc_00253D2E:
    goto loc_00253A3C;
loc_00253D36:
    goto loc_00253AC6;
loc_00253D5E:
    a3 = (unsigned int)((a3) + 1);
    v_stack_p70 = (unsigned int)(a3);
    if (((unsigned int)(a3)) == ((unsigned int)(*(unsigned __int16 *)(v_rip + 14095003)))) goto loc_00253D8F;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rip + 14095003)) * ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int8 *)(v_rbp - 104) + 136))));
    a1 = (unsigned int)((a1) + ((unsigned int)(a3)));
    goto loc_002539DA;
loc_00253D87:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - 1);
    goto loc_00253A6F;
loc_00253D8F:
    v_stack_p20 = v_rbp + 64;
    result = KiHeteroSelectProcessorToPreempt(a9, a13, *(unsigned __int64 *)(v_rbp - 128), v_rbp - 120);
    if (!sign_flag) goto loc_00254138;
    v_stack_p41 = (unsigned __int8)(*(unsigned __int8 *)(v_rbp - 104));
    v_stack_p50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 100)));
    goto loc_002539A0;
loc_00253DD1:
    if ((unsigned __int8)(v_r14) != 0) goto loc_002541C0;
    v_stack_p30 = v_rbp - 88;
    v_stack_p28 = *(unsigned __int64 *)(v_rbp - 96);
    v_stack_p20 = *(unsigned __int64 *)(v_rbp - 48);
    result = KiAttemptToScheduleThreadToBusyIsolationUnit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 536)) * 8 + 16550976) + 36440) + 8, a13, (unsigned __int8)(result), v_rbp + 64);
    if ((unsigned __int8)(result) != 0) goto loc_00253E85;
    goto loc_002541C0;
loc_00253E85:
loc_00254004:
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int8 *)(v_rbp - 104) + 185)) + ((unsigned int)(v_stack_p41)));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(v_rbp - 104) + 192) + a1 + a1 * 2 * 8 + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(v_rbp - 104) + 192) + a1 + a1 * 2 * 8 + 16));
    a2 = (a2) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 128) + *(unsigned __int16 *)(*(unsigned __int8 *)(v_rbp - 104) + 136) * 8 + 8));
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int8 *)(v_rbp - 104) + 192) + a1 + a1 * 2 * 8 + 16)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp - 128) + *(unsigned __int16 *)(*(unsigned __int8 *)(v_rbp - 104) + 136) * 8 + 8));
    result = (*(unsigned __int64 *)(a13 + 36448)) & (*(unsigned __int64 *)(*(unsigned __int8 *)(v_rbp - 104) + 16));
    v_stack_p30 = v_rbp + 64;
    v_r14 = (result == (*(unsigned __int64 *)(a13 + 36448))) ? 1 : 0;
    v_stack_p28 = (unsigned int)(v_r14);
    v_stack_p20 = v_rbp - 120;
    result = KiHeteroAttemptPreemptionSwapOnSubNode(*(unsigned __int64 *)(v_rbp - 96), result, a13, *(unsigned __int64 *)(v_rbp - 128));
    if (!sign_flag) goto loc_00254138;
    v_stack_p41 = (unsigned __int8)(*(unsigned __int8 *)(v_rbp - 104));
    v_stack_p50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 100)));
    goto loc_00253B6D;
loc_002540D5:
    result = 0;
    goto loc_00253592;
loc_002540DC:
    a2 = (result) + (312);
    goto loc_00253A5A;
loc_002540E8:
    goto loc_00253227;
loc_002540FB:
    *(unsigned __int64 *)(v_rbp - 88) = v_rdi;
    goto loc_002533BC;
loc_00254107:
    goto loc_00253BB1;
loc_0025411D:
    *(unsigned __int64 *)(v_rbp + 64) = *(unsigned __int64 *)(v_rbp - 96);
    *(unsigned __int64 *)(v_rbp - 56) = v_rdi;
    *(unsigned __int64 *)(v_rbp + 72) = 1;
loc_00254138:
    v_r14 = 0;
    goto loc_00253350;
loc_00254154:
    a1 = (unsigned __int8)((*(unsigned __int64 *)(v_rbp - 96)) | (4));
    goto loc_002534DF;
loc_0025415C:
    v_r15 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r11 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 14312) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) * 4 * 8 + 16) + 536)) * 8 + 16550976) + 36440) + 8) + (8);
    v_r12 = (a8) - (1);
    if (condition_is_not_equal) goto loc_00253770;
loc_00254174:
    v_rbx = (unsigned __int8)((a13) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(a12 + 56))));
    result = KiIsIsolationUnitIdleByHandle(v_rbp + 64, 1, a13, (unsigned int)(a14));
    *(unsigned int *)(v_rbp + 72) = (unsigned int)(result);
    *(unsigned int *)(v_rbp + 76) = (unsigned int)(v_rdi);
    *(unsigned int *)(a9 + 536) = (unsigned int)(v_stack_p42);
    a4 = ((unsigned int)(*(unsigned int *)(a12 + 216))) + (*(unsigned __int64 *)(a9 + 104));
    *(unsigned __int64 *)(v_rbp - 88) = a4;
loc_002541C0:
    result = *(unsigned __int64 *)(a9 + 104);
    if ((unsigned __int8)(v_stack_p42) == 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(a9 + 104));
        a4 = *(unsigned __int64 *)(v_rbp - 88);
        *(unsigned int *)(a9 + 436) = (unsigned int)(result);
    }
    if (a4 != 0) goto loc_002541F9;
    a2 = ((unsigned int)(*(unsigned int *)(a12 + 216))) + (*(unsigned __int64 *)(a9 + 104));
loc_002541F9:
    if (*(unsigned __int64 *)(a12 + 36536) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(a12 + 36536) + 16) = (unsigned __int8)(v_rdi);
    }
    *(unsigned __int8 *)(a9 + 388) = 1;
    v_rbx = 0;
    result = KiUpdateVpBackingThreadPriorityOnReadyQueueInsertion(a9, a2, a13, a4);
    result = (*(unsigned __int64 *)(a12 + 36416)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a9 + 576) + *(unsigned __int8 *)(a12 + 208) * 8 + 8));
    v_rsi = ((__int8)(*(unsigned __int8 *)(a9 + 195)) + 4) << (4);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(a12 + 36424));
    *(unsigned __int64 *)(v_rbp - 80) = v_xmm0;
    *(unsigned int *)(v_rbp - 40) = (unsigned int)(v_rdi);
loc_002542CC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14100454)))) & (64)) == 0) goto loc_0025379D;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(a12 + 36416), *(unsigned __int64 *)(*(unsigned __int64 *)(a9 + 576) + *(unsigned __int8 *)(a12 + 208) * 8 + 8), a13, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0025379D;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(a9 + 195)))), *(unsigned __int64 *)(*(unsigned __int64 *)(a9 + 576) + *(unsigned __int8 *)(a12 + 208) * 8 + 8), a13, a4);
    goto loc_0025379F;
loc_002542F4:
    if (((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a12 + 36424) + 195)))) == ((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a12 + 36424) + 968))))))) goto loc_002531B8;
    result = (unsigned int)(((unsigned int)((unsigned int)((__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a12 + 36424) + 195))))) - ((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a12 + 36424) + 968)))))));
    goto loc_002531B8;
loc_0025431E:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a12 + 36424) + 195)) >= 16) goto loc_002533BC;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a12 + 36424) + 120)) & (512)) != 0) goto loc_002533BC;
loc_0025433B:
    if (*(unsigned __int64 *)(a4 + 416) != 0) goto loc_0025433B;
    goto loc_002533BC;
loc_00254356:
    if ((*(unsigned __int8 *)(a4 + 195)) <= ((unsigned __int8)(v_rdi))) goto loc_0025315E;
    if (((unsigned __int8)((__int8)(v_stack_p43))) <= (*(unsigned __int8 *)(a4 + 870))) goto loc_0025316A;
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline(*(unsigned __int64 *)(a4 + 416), (__int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a12 + 36424) + 195)), (unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a12 + 36424) + 968)))), a4);
    v_rbx = (unsigned int)(((__int8)(v_stack_p43)) + ((unsigned int)((__int8)(*(unsigned __int8 *)(a9 + 563)))));
    if (((unsigned int)(v_rbx)) >= 16) { v_rbx = 15; }
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)((__int8)(*(unsigned __int8 *)(a9 + 563)))));
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline(*(unsigned __int64 *)(a4 + 416), 15, (unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a12 + 36424) + 968)))), a4);
    a3 = 0;
    a2 = 0;
    *(unsigned __int8 *)(a9 + 870) = (unsigned __int8)(v_rbx);
    result = KiComputeThreadPriority(a9, a2, a3, a4);
    goto loc_0025316F;
loc_002543C6:
    *(unsigned __int64 *)(v_rbp - 128) = v_rbp - 16;
    v_stack_p58 = 1;
    v_stack_p50 = (unsigned int)(v_rdi);
    goto loc_00253463;
loc_002543E5:
    if (0 == 1) {
        result = *(unsigned __int64 *)(a9 + 36440);
        a4 = *(unsigned __int8 *)(result);
        a3 = result + 8;
    }
    if ((unsigned int)(a4) == 0) goto loc_00253384;
loc_00254412:
    result = (unsigned __int8)(~(*(unsigned __int8 *)(*(unsigned __int64 *)(a3) + 35)));
    result = (unsigned int)((result) & (1));
    a1 = (unsigned int)((1) & ((unsigned int)(result)));
    a2 = ((unsigned int)((unsigned int)(a4))) - (1);
    if (condition_is_not_equal) goto loc_00254412;
    goto loc_00253384;
loc_0025442F:
    v_stack_p58 = (unsigned int)(*(unsigned __int8 *)(a9 + 565));
    goto loc_002531D3;
loc_00254449:
    goto loc_00253828;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0025308F(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint8_t Arg8, void *Arg9, uint32_t Arg10, uint32_t Arg11, uint32_t Arg12, void *Arg13, uint32_t Arg14, uint8_t Arg15)
{
    uint8_t *arg9 = (uint8_t *)Arg9;
    uint8_t *arg13 = (uint8_t *)Arg13;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    uint64_t v_stack_p1B8;
    uint8_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p40;
    uint8_t v_stack_p41;
    uint8_t v_stack_p42;
    uint8_t v_stack_p43;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint8_t v_stack_p54;
    uint8_t v_stack_p55;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;

    v_stack_p1B8 = local_r12;
    *(uint64_t *)(local_rbp - 0x18) = local_rdi;
    local_r12 = 0;
    if ((*(uint8_t *)(local_rbx + 0x236)) == ((uint8_t)(local_rsi))) goto loc_0025442F;
    local_rbx = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) - (*(uint32_t *)(arg9 + 0x1B4)));
    if (local_r13 >= (*(uint64_t *)(arg9 + 0x20))) goto loc_00253101;
    if ((*(uint8_t *)(arg9 + 0x233)) >= 14) goto loc_0025310C;
    if (((*(uint16_t *)(arg9 + 0x206)) & ((uint16_t)((uint32_t)(0xFF0ULL)))) != 0) goto loc_0025312E;
    if (((uint32_t)(Arg1)) >= 2) goto loc_0025310C;
    goto loc_0025312E;
loc_00253101:
loc_0025310C:
    result = KiComputeNewPriority(Arg9, (uint32_t)(0xFF0ULL), 1, Arg9);
    local_r14 = 63;
    if (0 == 0) { local_r14 = (uint32_t)((uint8_t)(result)); }
loc_0025312E:
    local_rbx = 4;
    if (!(condition_is_above_or_equal)) {
        local_rbx = (uint8_t)((4) | (2));
    }
    result = (uint8_t)(~((uint8_t)(local_rbx)));
    Arg1 = ((((uint8_t)((uint32_t)(*(uint32_t *)(arg9 + 0x78)))) & (8)) == 0) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    if ((((uint8_t)(Arg1)) & (1)) != 0) goto loc_00254356;
loc_0025315E:
loc_0025316A:
loc_0025316F:
    if (((uint8_t)(local_r14)) == 63) goto loc_002531B8;
    *(uint8_t *)(arg9 + 0xC3) = (uint8_t)(local_r14);
    result = KiComputeThreadQos(Arg9, *(uint64_t *)(gs_base + (0 + 0x20)), 1, Arg9);
    if (((uint32_t)(result)) != ((uint32_t)(*(uint8_t *)(arg9 + 0x204)))) {
        *(uint8_t *)(arg9 + 0x204) = (uint8_t)(result);
    }
    if (((*(uint32_t *)(arg9 + 0x78)) & (0x400000ULL)) != 0) goto loc_002542F4;
loc_002531B8:
    local_rsi = (uint8_t)((1) & (1));
loc_002531D3:
    result = KiComputeThreadQos(Arg9, *(uint64_t *)(gs_base + (0 + 0x20)), 1, Arg9);
    if ((uint8_t)(local_rsi) == 0) goto loc_00253244;
    if (((*(uint32_t *)(v_rip + 0xD73938)) & (0x40000ULL)) == 0) goto loc_00253227;
    if ((*(uint8_t *)(v_rip + 0xD738E5)) == ((uint8_t)(local_rdi))) goto loc_00253227;
    if (((uint32_t)(*(uint8_t *)(arg9 + 0x204))) != 4) goto loc_002540E8;
loc_00253227:
    Arg2 = (uint32_t)((36) * (*(uint32_t *)(v_rip + 0xD71E6A)));
    Arg1 = ((uint32_t)((uint32_t)(Arg2))) + (local_r13);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg9 + 0x78)))) & (32)) != 0) {
    }
    *(uint64_t *)(arg9 + 0x20) = Arg1;
loc_00253244:
    *(uint32_t *)(local_rbp - 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(arg9 + 0x24C)));
    *(uint16_t *)(arg9 + 0x235) = (uint16_t)(local_rdi);
    if ((*(uint32_t *)(arg9 + 0x1E4)) != ((uint32_t)(local_rdi))) goto loc_00253269;
loc_00253269:
    local_r14 = 0;
    v_stack_p40 = 1;
    local_r13 = (condition_is_below) ? 1 : 0;
    v_stack_p42 = (uint8_t)(local_r13);
    *(uint32_t *)(local_rbp - 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(arg9 + 0x24C)));
    result = 0;
    v_stack_p43 = 0;
    result = 0;
    *(uint64_t *)(local_rbp + 0x48) = local_rdi;
    *(uint64_t *)(local_rbp + 0x40) = 0;
    if ((*(uint32_t *)(v_rip + 0xD73D19)) == 0) goto loc_002536AC;
loc_002532E1:
    if (((uint16_t)(local_rdi)) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg9 + 0x240))))) goto loc_002537AA;
    Arg2 = (*(uint64_t *)(arg9 + 0x240)) + (8);
loc_002532FE:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + ((uint32_t)(Arg1)));
    Arg4 = ((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg9 + 0x240))))) - (1);
    if (condition_is_not_equal) goto loc_002532FE;
    if (((uint32_t)(Arg3)) <= 1) goto loc_002537AA;
    if ((*(uint32_t *)(v_rip + 0xD73855)) != ((uint32_t)(local_rdi))) goto loc_002538C9;
    v_stack_p20 = 0;
    result = KiChooseTargetProcessor(local_r15, Arg9, *(uint64_t *)(arg9 + 0x240), local_rbp + 64);
loc_00253350:
    local_rsi = (*(uint64_t *)(local_rbp + 0x40)) & (-2);
    v_stack_p60 = local_rsi;
loc_0025335D:
    Arg1 = (*(uint64_t *)(local_rbp + 0x40)) & (-2);
    *(uint64_t *)(local_rbp + 0x28) = Arg1;
    Arg2 = (uint32_t)((*(uint64_t *)(local_rbp + 0x40)) & (1));
    if (condition_is_not_equal) goto loc_002543E5;
    Arg1 = (uint8_t)(~(*(uint8_t *)(Arg1 + 0x23)));
    Arg1 = (uint32_t)((Arg1) & (1));
loc_00253384:
    *(uint32_t *)(arg9 + 0x218) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x24)));
    if (*(uint64_t *)(arg9 + 0x68) == 0) goto loc_002540FB;
    Arg4 = ((uint32_t)(*(uint32_t *)(local_rsi + 0xD8))) + (*(uint64_t *)(arg9 + 0x68));
    *(uint64_t *)(local_rbp - 0x58) = Arg4;
    if (condition_is_not_equal) goto loc_0025431E;
loc_002533BC:
    if ((*(uint32_t *)(v_rip + 0xD71F1E)) == ((uint32_t)(local_rdi))) goto loc_002533CE;
loc_002533CE:
    if ((*(uint32_t *)(local_rbp + 0x48)) == ((uint32_t)(local_rdi))) goto loc_00253DD1;
    Arg2 = 0;
    local_rsi = (*(uint64_t *)(local_rbp + 0x40)) & (-2);
    v_stack_p60 = local_rsi;
    result = memset(*(uint64_t *)(local_r15 + 0x37E8), Arg2, 240, Arg4);
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_rbp + 0x40)))) & (1));
    *(uint64_t *)(local_rbp - 0x80) = local_rdi;
    v_stack_p70 = (uint32_t)(local_r11);
    v_stack_p58 = (uint32_t)((uint32_t)((uint32_t)(local_rdi)));
    *(uint64_t *)(local_rbp - 0x10) = local_rsi;
    v_stack_p68 = (uint32_t)((uint32_t)(*(uint64_t *)(local_rbp + 0x40)));
    if (condition_is_equal) goto loc_002543C6;
    local_r10 = local_rdi;
    if (((uint32_t)(local_r11)) == 1) {
        result = *(uint64_t *)(local_rsi + 0x8E58);
        local_r10 = *(uint64_t *)(local_rsi + 0x8E58);
        local_r10 = (local_r10) + (8);
        *(uint64_t *)(local_rbp - 0x80) = local_r10;
        Arg4 = *(uint8_t *)(result);
        v_stack_p58 = (uint32_t)(Arg4);
    }
    v_stack_p50 = (uint32_t)(local_rdi);
    if ((uint32_t)(Arg4) == 0) goto loc_0025356E;
loc_00253463:
    v_stack_p68 = Arg4;
loc_00253471:
    result = 0;
    *(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30 - 0x20) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30 - 0x10) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30) = 0;
    *(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30 - 0x8) = -1;
    *(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30 + 0x4) = 63;
    *(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30 - 0x20) = *(uint64_t *)(local_r10);
    *(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30 - 0x18) = local_rdi;
    *(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30 - 0x10) = *(uint64_t *)(*(uint64_t *)(local_r10) + 0x10);
    local_rsi = *(uint64_t *)(*(uint64_t *)(local_r10) + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(local_r10) + 0x10) == 0) {
        local_rsi = *(uint64_t *)(*(uint64_t *)(local_r10) + 0x8);
        *(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30 - 0x10) = local_rsi;
    }
    if ((*(uint64_t *)(local_r10)) == (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_00254154;
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30)) & (251));
loc_002534DF:
    *(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30) = (uint8_t)(Arg1);
    local_r12 = 0;
    result = (uint8_t)(~(*(uint8_t *)(*(uint64_t *)(local_r10) + 0x23)));
    result = (uint8_t)((result) & (1));
    Arg2 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30)) & (254));
    Arg2 = (uint8_t)((Arg2) | ((uint8_t)(result)));
    *(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30) = (uint8_t)(Arg2);
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_r10) + 0x38))) >> (6));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(Arg2)));
    Arg1 = (uint8_t)((Arg1) & (2));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(Arg2)));
    *(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x30) = (uint8_t)((uint8_t)(Arg1));
    result = (uint32_t)(((uint8_t)(Arg1)) >> (1));
    result = (uint32_t)((result) & (1));
    Arg3 = (uint32_t)((uint32_t)(local_rdi));
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)((uint32_t)(local_rdi))))) { Arg3 = (uint32_t)(result); }
    local_r10 = (local_r10) + (8);
    local_rbx = (*(uint64_t *)(local_r15 + 0x37E8) + 48) + (40);
    v_stack_p50 = (uint32_t)(Arg3);
    Arg4 = (Arg4) - (1);
    *(uint64_t *)(local_rbp - 0x80) = local_r10;
    v_stack_p68 = Arg4;
    if (condition_is_not_equal) goto loc_00253471;
    v_stack_p68 = *(uint64_t *)(local_rbp + 0x40);
loc_0025356E:
    *(uint32_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x4) = (uint32_t)(Arg3);
    *(uint32_t *)(*(uint64_t *)(local_r15 + 0x37E8) + 0x8) = (uint32_t)((uint32_t)(Arg14));
    *(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8)) = (uint8_t)((uint32_t)(Arg11));
    if ((uint32_t)((uint32_t)(Arg14)) == 0) goto loc_002540D5;
loc_00253592:
    *(uint8_t *)(1 + *(uint64_t *)(local_r15 + 0x37E8) * 1) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp - 0x10) + 0x8E58) + 0x1));
loc_002535B0:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8))))) goto loc_002535CE;
    if ((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10)) == Arg12) goto loc_002535CA;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + 1);
    goto loc_002535B0;
loc_002535CA:
loc_002535CE:
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg9 + 0x78))) >> (1));
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10 + 0x20)) >> (1));
    local_r10 = (uint32_t)((local_r10) & (1));
    result = (uint32_t)((result) & (1));
    v_stack_p70 = (uint32_t)(local_r10);
loc_0025360C:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x30)) | (1));
    *(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x20) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x18);
    *(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x30) = (uint8_t)(result);
    result = (uint8_t)((result) & (253));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x18) + 0x78))) >> (1));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) & (231));
    Arg1 = (uint8_t)((Arg1) | (4));
    Arg1 = (uint8_t)((Arg1) & (223));
    *(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x30) = (uint8_t)(Arg1);
    *(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x28) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x18);
    result = KiIsPrcbThread(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x18), Arg2, *(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8)), *(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8);
    if ((uint8_t)(result) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x24);
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x18) + 0x218) = (uint32_t)(result);
    }
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + 1);
    if (((uint32_t)(local_r11)) < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(local_r15 + 0x37E8))))) goto loc_0025360C;
loc_002536AC:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCCFD1A)))) != 4) goto loc_002532E1;
    v_stack_p60 = *(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x218)) * 8 + 0xFC8C40);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x240) + *(uint8_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x218)) * 8 + 0xFC8C40) + 0xD0) * 8 + 0x8)) >> ((uint8_t)(*(uint8_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x218)) * 8 + 0xFC8C40) + 0xD1)));
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x78))) >> (1));
    Arg4 = (uint32_t)((Arg4) & (1));
    v_stack_p70 = (uint32_t)(Arg4);
    *(uint64_t *)(local_rbp - 0x8) = *(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x218)) * 8 + 0xFC8C40);
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x218)) * 8 + 0xFC8C40) + 0x38))))) >> (7));
    Arg2 = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(Arg4)) < ((uint32_t)(result))) { Arg2 = (uint32_t)(result); }
    Arg1 = (*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x218)) * 8 + 0xFC8C40)) & (-2);
    Arg1 = (Arg1) | ((uint32_t)((uint32_t)(Arg2)));
    *(uint64_t *)(local_rbp + 0x40) = Arg1;
    if (((uint32_t)(Arg2)) != 1) goto loc_00254174;
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x218)) * 8 + 0xFC8C40) + 0x8E58))) == 0) goto loc_00254174;
loc_00253770:
loc_00253780:
    if (condition_is_above_or_equal) goto loc_0025415C;
loc_0025378D:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + 1);
    if (((*(uint32_t *)(v_rip + 0xD71B15)) & ((uint32_t)(local_r14))) == 0) goto loc_002542CC;
loc_0025379D:
loc_0025379F:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x218)) * 8 + 0xFC8C40) + 0x8E58) + 0x8) + 0x30) == 0) goto loc_00253780;
    goto loc_0025378D;
loc_002537AA:
    result = KeFindFirstSetLeftAffinityEx(*(uint64_t *)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x218)) * 8 + 0xFC8C40) + 0x38)) + 0x240), Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x240), Arg4);
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x218)) * 8 + 0xFC8C40) + 0x38)) + 0x78))) >> (1));
    Arg4 = (uint32_t)((Arg4) & (1));
    v_stack_p70 = (uint32_t)(Arg4);
    v_stack_p60 = *(uint64_t *)(v_rip - 0x2537C1 + (uint32_t)((uint32_t)(result)) * 8 + 0xFC8C40);
    *(uint64_t *)(local_rbp + 0x20) = *(uint64_t *)(v_rip - 0x2537C1 + (uint32_t)((uint32_t)(result)) * 8 + 0xFC8C40);
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x2537C1 + (uint32_t)((uint32_t)(result)) * 8 + 0xFC8C40) + 0x38))))) >> (7));
    Arg2 = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(Arg4)) < ((uint32_t)(result))) { Arg2 = (uint32_t)(result); }
    Arg1 = (*(uint64_t *)(v_rip - 0x2537C1 + (uint32_t)((uint32_t)(result)) * 8 + 0xFC8C40)) & (-2);
    Arg1 = (Arg1) | ((uint32_t)((uint32_t)(Arg2)));
    *(uint64_t *)(local_rbp + 0x40) = Arg1;
    if ((uint32_t)(Arg2) == 0) goto loc_00254449;
    if (((uint32_t)(Arg2)) != 1) goto loc_0025388C;
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x2537C1 + (uint32_t)((uint32_t)(result)) * 8 + 0xFC8C40) + 0x8E58))) == 0) goto loc_00253886;
loc_00253828:
loc_00253840:
loc_00253847:
    if (condition_is_above_or_equal) goto loc_00253869;
loc_00253850:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + 1);
    if (((*(uint32_t *)(v_rip + 0xD71A52)) & ((uint32_t)(local_r14))) == 0) goto loc_002538AC;
loc_0025385C:
loc_0025385E:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x2537C1 + (uint32_t)((uint32_t)(result)) * 8 + 0xFC8C40) + 0x8E58) + 0x8) + 0x30) == 0) goto loc_00253847;
    goto loc_00253850;
loc_00253869:
    local_r12 = (*(uint64_t *)(*(uint64_t *)(v_rip - 0x2537C1 + (uint32_t)((uint32_t)(result)) * 8 + 0xFC8C40) + 0x8E58) + 8) + (8);
    local_r13 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x2537C1 + (uint32_t)((uint32_t)(result)) * 8 + 0xFC8C40) + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_00253840;
    local_r14 = 0;
loc_00253886:
loc_0025388C:
    local_rbx = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip - 0x2537C1 + (uint32_t)((uint32_t)(result)) * 8 + 0xFC8C40) + 0x38))) ^ (*(uint8_t *)(*(uint64_t *)(Arg12 + 0x38))));
    result = KiIsIsolationUnitIdleByHandle(local_rbp + 64, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x240), (uint32_t)(Arg14));
    *(uint32_t *)(local_rbp + 0x48) = (uint32_t)(result);
    *(uint32_t *)(local_rbp + 0x4C) = (uint32_t)(local_rdi);
    goto loc_0025335D;
loc_002538AC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD73206)))) & (64)) == 0) goto loc_0025385C;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_rbp + 64, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x240), (uint32_t)(Arg14));
    if ((uint8_t)(result) == 0) goto loc_0025385C;
    result = HvlNotifyLongSpinWait(0, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x240), (uint32_t)(Arg14));
    goto loc_0025385E;
loc_002538C9:
    result = 0;
    *(uint64_t *)(local_rbp - 0x68) = 0;
    *(uint64_t *)(local_rbp - 0x78) = v_xmm0;
    Arg1 = (uint32_t)(*(uint32_t *)(local_rbx + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x54))))) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x54))); }
    *(uint32_t *)(local_rbp + 0xA0) = 0x2030405ULL;
    *(uint16_t *)(local_rbp + 0xA4) = 6;
    Arg2 = (((uint32_t)(Arg1)) >= (*(uint32_t *)(v_rip + 0xD71A73))) ? 1 : 0;
    *(uint8_t *)(local_rbp + 0xA6) = 1;
    *(uint64_t *)(local_rbp - 0x80) = *(uint64_t *)(local_rbx + 0x240);
    *(uint64_t *)(local_rbp - 0x38) = local_rdi;
    *(uint32_t *)(local_rbp - 0x74) = (uint32_t)(*(uint8_t *)(local_rbx + 0x204));
    *(uint32_t *)(local_rbp - 0x70) = (uint32_t)(Arg2);
    *(uint32_t *)(local_rbp - 0x6C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + (uint32_t)((uint32_t)(Arg2)) + *(uint8_t *)(local_rbx + 0x204) * 2 * 4 + 0xFC5460)));
    v_stack_p55 = (uint8_t)(*(uint8_t *)(local_rbp + *(uint8_t *)(local_rbx + 0x204) * 1 + 0xA0));
    *(uint8_t *)(local_rbp - 0x78) = (uint8_t)(*(uint8_t *)(local_rbx + 0xC3));
    v_stack_p41 = (uint8_t)(*(uint8_t *)(local_rbx + 0x205));
    *(uint8_t *)(local_rbp - 0x68) = (uint8_t)(*(uint8_t *)(local_rbx + 0x205));
    v_stack_p54 = (uint8_t)(local_rdi);
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x78))) >> (1));
    local_rbx = (uint32_t)((local_rbx) & (1));
    *(uint16_t *)(local_rbp - 0x66) = (uint16_t)(v_stack_p54);
    v_stack_p50 = (uint32_t)(local_rbx);
    *(uint32_t *)(local_rbp - 0x64) = (uint32_t)(local_rbx);
    v_stack_p68 = *(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(arg9 + 0x24C)) * 8 + 0xFC8C40);
loc_002539A0:
    *(uint64_t *)(local_rbp) = local_rdi;
    v_stack_p70 = (uint32_t)(local_rdi);
    v_stack_p54 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(arg9 + 0x24C)) * 8 + 0xFC8C40) + 0xC0) + 0x8A));
    v_stack_p60 = (uint32_t)(*(uint16_t *)(local_rbp + 0x2));
loc_002539C6:
    if ((uint16_t)(*(uint16_t *)(local_rbp + 0x2)) != 0) goto loc_00253D5E;
    v_stack_p60 = 1;
loc_002539DA:
    if (((uint32_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(arg9 + 0x24C)) * 8 + 0xFC8C40) + 0xC0) + 0x8A)))) == -1) goto loc_00253D8F;
    *(uint64_t *)(local_rbp + 0x70) = v_xmm0;
    *(uint64_t *)(local_rbp + 0x80) = v_xmm1;
    *(uint64_t *)(local_rbp + 0x90) = v_xmm1;
    result = KiIsQosGroupingClass((uint32_t)(*(uint32_t *)(local_rbp - 0x74)), *(uint16_t *)(local_rbp + 0x2), (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(Arg14));
    if ((uint8_t)(result) != 0) goto loc_00253D2E;
    if (((*(uint32_t *)(v_rip + 0xD73114)) & (0x800000ULL)) == 0) goto loc_00253D2E;
    if (((*(uint8_t *)(*(uint64_t *)(local_r11 + (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(arg9 + 0x24C)) * 8 + 0xFC8C40) + 0xC0) + 0x8A)) * 8 + 0xFCF6C0) + 0xA)) & (8)) == 0) goto loc_00253D2E;
loc_00253A3C:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp - 0x6C))) + (-3));
    Arg2 = ((uint8_t)(*(uint8_t *)(local_rbx + 0x205))) << (5);
    if (((uint32_t)(result)) > 1) goto loc_002540DC;
    Arg2 = (Arg2) + (568);
loc_00253A5A:
    Arg2 = (Arg2) + (*(uint64_t *)(local_r11 + (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(arg9 + 0x24C)) * 8 + 0xFC8C40) + 0xC0) + 0x8A)) * 8 + 0xFCF6C0));
    result = RtlCopyVolatileMemory(local_rbp + 128, Arg2, 32, (uint32_t)(Arg14));
loc_00253A6F:
    *(uint64_t *)(local_rbp + 0x70) = v_xmm0;
loc_00253A79:
    result = KeIsEmptyGroupMask(local_rbp + 112, Arg2, 32, (uint32_t)(Arg14));
    if ((uint32_t)(result) != 0) goto loc_00253C03;
    Arg3 = 0;
    *(uint64_t *)(local_rbp + 0x50) = v_xmm0;
    *(uint64_t *)(local_rbp + 0x60) = v_xmm1;
loc_00253AA1:
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_00253BE9;
loc_00253AB4:
    Arg1 = (local_rdi) + 1;
    Arg2 = (result + 32) - (1);
    if (condition_is_not_equal) goto loc_00253AA1;
    *(uint64_t *)(local_rbp + 0x50) = v_xmm0;
loc_00253AC6:
    result = KeIsEmptyGroupMask(local_rbp + 80, Arg2, Arg3, (uint32_t)(Arg14));
    if ((uint32_t)(result) != 0) goto loc_00253A79;
    result = ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(arg9 + 0x24C)) * 8 + 0xFC8C40) + 0xC0) + 0x8A)) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r11 + (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(arg9 + 0x24C)) * 8 + 0xFC8C40) + 0xC0) + 0x8A)) * 8 + 0xFCF6C0))))) ? 1 : 0;
    v_stack_p28 = 1;
    v_stack_p20 = local_rbp - 120;
    result = KiHeteroSelectIdleProcessorFromSubNode(Arg9, *(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(arg9 + 0x24C)) * 8 + 0xFC8C40) + 0xC0), *(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(arg9 + 0x24C)) * 8 + 0xFC8C40), *(uint64_t *)(local_rbp - 0x80));
    if (result == 0) goto loc_00253D36;
    if ((*(uint32_t *)(local_rbp - 0x70)) != 1) goto loc_00253B68;
    if ((*(uint32_t *)(local_rbp - 0x74)) != ((uint32_t)(local_rdi))) goto loc_00253B68;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp - 0x6C))) - 1);
    if (((uint32_t)(result)) > 1) goto loc_00253B68;
    if ((uint32_t)((uint32_t)(Arg10)) == 0) goto loc_00254004;
loc_00253B68:
loc_00253B6D:
    *(uint64_t *)(local_rbp + 0x8) = result;
    Arg1 = ((int32_t)((uint32_t)((uint32_t)(Arg10)))) ^ (result);
    Arg1 = (Arg1) & (-2);
    Arg1 = (Arg1) ^ ((int32_t)((uint32_t)((uint32_t)(Arg10))));
    *(uint64_t *)(local_rbp - 0x38) = Arg1;
    if ((uint32_t)((uint32_t)(Arg10)) == 0) goto loc_00254107;
    if (((uint32_t)((uint32_t)(Arg10))) != 1) goto loc_00253C62;
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(result + 0x8E58))) == 0) goto loc_00253C62;
loc_00253BB1:
loc_00253BC0:
loc_00253BC5:
    if (condition_is_above_or_equal) goto loc_00253C40;
loc_00253BCE:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + 1);
    if (((*(uint32_t *)(v_rip + 0xD716D6)) & ((uint32_t)(local_rsi))) == 0) goto loc_00253D07;
loc_00253BDC:
loc_00253BDE:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8E58) + 0x8) + 0x30) == 0) goto loc_00253BC5;
    goto loc_00253BCE;
loc_00253BE9:
    if (((uint8_t)(*(uint8_t *)(local_rbp + Arg1 * 1 + 0x80))) != ((uint8_t)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(arg9 + 0x24C)) * 8 + 0xFC8C40)))) goto loc_00253C2D;
loc_00253BF6:
    goto loc_00253AB4;
loc_00253C03:
    if (((uint32_t)(*(uint64_t *)(result + 0x8E58) + 8)) > Arg10) goto loc_00253D87;
    goto loc_002539C6;
loc_00253C2D:
    if (((uint32_t)(*(uint64_t *)(result + 0x8E58) + 8)) <= Arg10) goto loc_00253AB4;
    *(uint64_t *)(local_rbp + 0x60) = v_xmm0;
    goto loc_00253BF6;
loc_00253C40:
    local_r14 = (*(uint64_t *)(result + 0x8E58) + 8) + (8);
    local_r12 = ((uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(result + 0x8E58))))) - (1);
    if (condition_is_not_equal) goto loc_00253BC0;
    v_stack_p41 = (uint8_t)(*(uint8_t *)(local_rbp - 0x68));
    v_stack_p50 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x64)));
loc_00253C62:
    Arg2 = (*(uint64_t *)(local_rbp - 0x38)) & (-2);
    *(uint64_t *)(local_rbp + 0x10) = Arg2;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_rbp - 0x38)))) & (1));
    if (((*(uint8_t *)(Arg2 + 0x23)) & (1)) == 0) goto loc_0025411D;
loc_00253C8A:
    Arg4 = (*(uint64_t *)(local_rbp - 0x38)) & (-2);
    *(uint64_t *)(local_rbp + 0x18) = Arg4;
    Arg1 = (uint32_t)((*(uint64_t *)(local_rbp - 0x38)) & (1));
    result = (uint32_t)(*(uint32_t *)(local_rbp - 0x64));
    if (((uint32_t)(Arg1)) == 1) {
        result = *(uint64_t *)(Arg4 + 0x8E58);
        Arg3 = *(uint64_t *)(Arg4 + 0x8E58);
        Arg3 = (Arg3) + (8);
        Arg2 = *(uint8_t *)(result);
    }
    if ((uint32_t)(Arg2) == 0) goto loc_00253CF2;
loc_00253CD0:
    if ((uint32_t)(Arg2 - 1) != 0) goto loc_00253CD0;
    v_stack_p41 = (uint8_t)(*(uint8_t *)(local_rbp - 0x68));
    v_stack_p50 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x64)));
loc_00253CF2:
    *(uint64_t *)(local_rbp - 0x38) = local_rdi;
    goto loc_002539A0;
loc_00253D07:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD72DAB)))) & (64)) == 0) goto loc_00253BDC;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(Arg3 + Arg2 - 0x1 * 8), (uint32_t)((uint32_t)(Arg2 - 1)), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00253BDC;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint8_t *)(local_rbp - 0x68))), (uint32_t)((uint32_t)(Arg2 - 1)), Arg3, Arg4);
    goto loc_00253BDE;
loc_00253D2E:
    goto loc_00253A3C;
loc_00253D36:
    goto loc_00253AC6;
loc_00253D5E:
    Arg3 = (uint32_t)((Arg3) + 1);
    v_stack_p70 = (uint32_t)(Arg3);
    if (((uint32_t)(Arg3)) == ((uint32_t)(*(uint16_t *)(v_rip + 0xD7129B)))) goto loc_00253D8F;
    Arg1 = (uint32_t)((*(uint16_t *)(v_rip + 0xD7129B)) * ((uint32_t)(*(uint16_t *)(*(uint8_t *)(local_rbp - 0x68) + 0x88))));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg3)));
    goto loc_002539DA;
loc_00253D87:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - 1);
    goto loc_00253A6F;
loc_00253D8F:
    v_stack_p20 = local_rbp + 64;
    result = KiHeteroSelectProcessorToPreempt(Arg9, Arg13, *(uint64_t *)(local_rbp - 0x80), local_rbp - 120);
    if (!sign_flag) goto loc_00254138;
    v_stack_p41 = (uint8_t)(*(uint8_t *)(local_rbp - 0x68));
    v_stack_p50 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x64)));
    goto loc_002539A0;
loc_00253DD1:
    if ((uint8_t)(local_r14) != 0) goto loc_002541C0;
    v_stack_p30 = local_rbp - 88;
    v_stack_p28 = *(uint64_t *)(local_rbp - 0x60);
    v_stack_p20 = *(uint64_t *)(local_rbp - 0x30);
    result = KiAttemptToScheduleThreadToBusyIsolationUnit(*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x218)) * 8 + 0xFC8C40) + 0x8E58) + 8, Arg13, (uint8_t)(result), local_rbp + 64);
    if ((uint8_t)(result) != 0) goto loc_00253E85;
    goto loc_002541C0;
loc_00253E85:
loc_00254004:
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint8_t *)(local_rbp - 0x68) + 0xB9)) + ((uint32_t)(v_stack_p41)));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint8_t *)(local_rbp - 0x68) + 0xC0) + Arg1 + Arg1 * 2 * 8 + 0x8)) & (*(uint64_t *)(*(uint64_t *)(*(uint8_t *)(local_rbp - 0x68) + 0xC0) + Arg1 + Arg1 * 2 * 8 + 0x10));
    Arg2 = (Arg2) & (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x80) + *(uint16_t *)(*(uint8_t *)(local_rbp - 0x68) + 0x88) * 8 + 0x8));
    Arg4 = (*(uint64_t *)(*(uint64_t *)(*(uint8_t *)(local_rbp - 0x68) + 0xC0) + Arg1 + Arg1 * 2 * 8 + 0x10)) & (*(uint64_t *)(*(uint64_t *)(local_rbp - 0x80) + *(uint16_t *)(*(uint8_t *)(local_rbp - 0x68) + 0x88) * 8 + 0x8));
    result = (*(uint64_t *)(arg13 + 0x8E60)) & (*(uint64_t *)(*(uint8_t *)(local_rbp - 0x68) + 0x10));
    v_stack_p30 = local_rbp + 64;
    local_r14 = (result == (*(uint64_t *)(arg13 + 0x8E60))) ? 1 : 0;
    v_stack_p28 = (uint32_t)(local_r14);
    v_stack_p20 = local_rbp - 120;
    result = KiHeteroAttemptPreemptionSwapOnSubNode(*(uint64_t *)(local_rbp - 0x60), result, Arg13, *(uint64_t *)(local_rbp - 0x80));
    if (!sign_flag) goto loc_00254138;
    v_stack_p41 = (uint8_t)(*(uint8_t *)(local_rbp - 0x68));
    v_stack_p50 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x64)));
    goto loc_00253B6D;
loc_002540D5:
    result = 0;
    goto loc_00253592;
loc_002540DC:
    Arg2 = (result) + (312);
    goto loc_00253A5A;
loc_002540E8:
    goto loc_00253227;
loc_002540FB:
    *(uint64_t *)(local_rbp - 0x58) = local_rdi;
    goto loc_002533BC;
loc_00254107:
    goto loc_00253BB1;
loc_0025411D:
    *(uint64_t *)(local_rbp + 0x40) = *(uint64_t *)(local_rbp - 0x60);
    *(uint64_t *)(local_rbp - 0x38) = local_rdi;
    *(uint64_t *)(local_rbp + 0x48) = 1;
loc_00254138:
    local_r14 = 0;
    goto loc_00253350;
loc_00254154:
    Arg1 = (uint8_t)((*(uint64_t *)(local_rbp - 0x60)) | (4));
    goto loc_002534DF;
loc_0025415C:
    local_r15 = (*(uint64_t *)(*(uint64_t *)(local_r11 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x37E8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) * 4 * 8 + 0x10) + 0x218)) * 8 + 0xFC8C40) + 0x8E58) + 8) + (8);
    local_r12 = (Arg8) - (1);
    if (condition_is_not_equal) goto loc_00253770;
loc_00254174:
    local_rbx = (uint8_t)((Arg13) ^ (*(uint8_t *)(*(uint64_t *)(Arg12 + 0x38))));
    result = KiIsIsolationUnitIdleByHandle(local_rbp + 64, 1, Arg13, (uint32_t)(Arg14));
    *(uint32_t *)(local_rbp + 0x48) = (uint32_t)(result);
    *(uint32_t *)(local_rbp + 0x4C) = (uint32_t)(local_rdi);
    *(uint32_t *)(arg9 + 0x218) = (uint32_t)(v_stack_p42);
    Arg4 = ((uint32_t)(*(uint32_t *)(Arg12 + 0xD8))) + (*(uint64_t *)(arg9 + 0x68));
    *(uint64_t *)(local_rbp - 0x58) = Arg4;
loc_002541C0:
    result = *(uint64_t *)(arg9 + 0x68);
    if ((uint8_t)(v_stack_p42) == 0) {
        result = *(uint32_t *)(*(uint64_t *)(arg9 + 0x68));
        Arg4 = *(uint64_t *)(local_rbp - 0x58);
        *(uint32_t *)(arg9 + 0x1B4) = (uint32_t)(result);
    }
    if (Arg4 != 0) goto loc_002541F9;
    Arg2 = ((uint32_t)(*(uint32_t *)(Arg12 + 0xD8))) + (*(uint64_t *)(arg9 + 0x68));
loc_002541F9:
    if (*(uint64_t *)(Arg12 + 0x8EB8) != 0) {
        *(uint8_t *)(*(uint64_t *)(Arg12 + 0x8EB8) + 0x10) = (uint8_t)(local_rdi);
    }
    *(uint8_t *)(arg9 + 0x184) = 1;
    local_rbx = 0;
    result = KiUpdateVpBackingThreadPriorityOnReadyQueueInsertion(Arg9, Arg2, Arg13, Arg4);
    result = (*(uint64_t *)(Arg12 + 0x8E40)) & (*(uint64_t *)(*(uint64_t *)(arg9 + 0x240) + *(uint8_t *)(Arg12 + 0xD0) * 8 + 0x8));
    local_rsi = ((int8_t)(*(uint8_t *)(arg9 + 0xC3)) + 4) << (4);
    local_rsi = (local_rsi) + (*(uint64_t *)(Arg12 + 0x8E48));
    *(uint64_t *)(local_rbp - 0x50) = v_xmm0;
    *(uint32_t *)(local_rbp - 0x28) = (uint32_t)(local_rdi);
loc_002542CC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD727E6)))) & (64)) == 0) goto loc_0025379D;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(Arg12 + 0x8E40), *(uint64_t *)(*(uint64_t *)(arg9 + 0x240) + *(uint8_t *)(Arg12 + 0xD0) * 8 + 0x8), Arg13, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0025379D;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(arg9 + 0xC3)))), *(uint64_t *)(*(uint64_t *)(arg9 + 0x240) + *(uint8_t *)(Arg12 + 0xD0) * 8 + 0x8), Arg13, Arg4);
    goto loc_0025379F;
loc_002542F4:
    if (((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(Arg12 + 0x8E48) + 0xC3)))) == ((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg12 + 0x8E48) + 0x3C8))))))) goto loc_002531B8;
    result = (uint32_t)(((uint32_t)((uint32_t)((int8_t)(*(uint8_t *)(*(uint64_t *)(Arg12 + 0x8E48) + 0xC3))))) - ((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg12 + 0x8E48) + 0x3C8)))))));
    goto loc_002531B8;
loc_0025431E:
    if ((*(uint8_t *)(*(uint64_t *)(Arg12 + 0x8E48) + 0xC3)) >= 16) goto loc_002533BC;
    if (((*(uint32_t *)(*(uint64_t *)(Arg12 + 0x8E48) + 0x78)) & (512)) != 0) goto loc_002533BC;
loc_0025433B:
    if (*(uint64_t *)(Arg4 + 0x1A0) != 0) goto loc_0025433B;
    goto loc_002533BC;
loc_00254356:
    if ((*(uint8_t *)(Arg4 + 0xC3)) <= ((uint8_t)(local_rdi))) goto loc_0025315E;
    if (((uint8_t)((int8_t)(v_stack_p43))) <= (*(uint8_t *)(Arg4 + 0x366))) goto loc_0025316A;
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline(*(uint64_t *)(Arg4 + 0x1A0), (int8_t)(*(uint8_t *)(*(uint64_t *)(Arg12 + 0x8E48) + 0xC3)), (uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg12 + 0x8E48) + 0x3C8)))), Arg4);
    local_rbx = (uint32_t)(((int8_t)(v_stack_p43)) + ((uint32_t)((int8_t)(*(uint8_t *)(arg9 + 0x233)))));
    if (((uint32_t)(local_rbx)) >= 16) { local_rbx = 15; }
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)((int8_t)(*(uint8_t *)(arg9 + 0x233)))));
    result = Feature_StackingDecayBoosts__private_IsEnabledNoReportingNoInline(*(uint64_t *)(Arg4 + 0x1A0), 15, (uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg12 + 0x8E48) + 0x3C8)))), Arg4);
    Arg3 = 0;
    Arg2 = 0;
    *(uint8_t *)(arg9 + 0x366) = (uint8_t)(local_rbx);
    result = KiComputeThreadPriority(Arg9, Arg2, Arg3, Arg4);
    goto loc_0025316F;
loc_002543C6:
    *(uint64_t *)(local_rbp - 0x80) = local_rbp - 16;
    v_stack_p58 = 1;
    v_stack_p50 = (uint32_t)(local_rdi);
    goto loc_00253463;
loc_002543E5:
    if (0 == 1) {
        result = *(uint64_t *)(arg9 + 0x8E58);
        Arg4 = *(uint8_t *)(result);
        Arg3 = result + 8;
    }
    if ((uint32_t)(Arg4) == 0) goto loc_00253384;
loc_00254412:
    result = (uint8_t)(~(*(uint8_t *)(*(uint64_t *)(Arg3) + 0x23)));
    result = (uint32_t)((result) & (1));
    Arg1 = (uint32_t)((1) & ((uint32_t)(result)));
    Arg2 = ((uint32_t)((uint32_t)(Arg4))) - (1);
    if (condition_is_not_equal) goto loc_00254412;
    goto loc_00253384;
loc_0025442F:
    v_stack_p58 = (uint32_t)(*(uint8_t *)(arg9 + 0x235));
    goto loc_002531D3;
loc_00254449:
    goto loc_00253828;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg9` | `+ 0x20` | `64` | `R` |
| `Arg9` | `+ 0x68` | `64` | `R` |
| `Arg9` | `+ 0x78` | `32` | `R` |
| `Arg9` | `+ 0xC3` | `8` | `R` |
| `Arg9` | `+ 0xC3` | `8` | `W` |
| `Arg9` | `+ 0x184` | `8` | `W` |
| `Arg9` | `+ 0x1B4` | `32` | `R` |
| `Arg9` | `+ 0x1B4` | `32` | `W` |
| `Arg9` | `+ 0x204` | `8` | `R` |
| `Arg9` | `+ 0x204` | `8` | `W` |
| `Arg9` | `+ 0x206` | `16` | `R` |
| `Arg9` | `+ 0x218` | `32` | `W` |
| `Arg9` | `+ 0x220` | `64` | `R` |
| `Arg9` | `+ 0x233` | `8` | `R` |
| `Arg9` | `+ 0x236` | `8` | `R` |
| `Arg9` | `+ 0x240` | `64` | `R` |
| `Arg9` | `+ 0x24C` | `32` | `R` |
| `Arg9` | `+ 0x366` | `8` | `R` |
| `Arg9` | `+ 0x366` | `8` | `W` |
| `Arg9` | `+ 0x3C8` | `64` | `R` |
| `Arg13` | `+ 0xC0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0025308F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
