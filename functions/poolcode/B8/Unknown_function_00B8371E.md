# sub_00B8371E

- RVA: `0x00B8371E`–`0x00B84077` (길이 `2,393` bytes)
- VA: `0x0000000140B8371E`
- 실행 섹션: `POOLCODE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007BE80`
- 디코드: `583`개 명령, `2,393/2,393` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x00B83768` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x00B83781` → [KxWaitForLockOwnerShip](../../text/25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00B8387E` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00B838BA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B838CD` → [KeReleaseInStackQueuedSpinLock](../../text/34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00B83949` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B83978` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B839CC` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x00B83A32` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x00B83A6A` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../../text/2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x00B83A97` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B83ABA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B83AFD` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B83B18` → [ExpCheckForLookaside](../../text/4A/ExpCheckForLookaside_function_004A52DC.md) (function, `0x004A52DC`)
- `0x00B83B2E` → [KeCheckForTimer](../../text/4D/KeCheckForTimer_function_004D870C.md) (function, `0x004D870C`)
- `0x00B83B44` → [ExpCheckForResource](../../text/49/ExpCheckForResource_function_0049CA24.md) (function, `0x0049CA24`)
- `0x00B83B5E` → [ExpCheckForWorker](../../text/4E/ExpCheckForWorker_function_004EC8FC.md) (function, `0x004EC8FC`)
- `0x00B83B85` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B83BB7` → [ExpPoolFlagsToPoolType](ExpPoolFlagsToPoolType_function_00B84080.md) (function, `0x00B84080`)
- `0x00B83BE7` → [EtwTracePool](../../text/2E/EtwTracePool_function_002ECEEC.md) (function, `0x002ECEEC`)
- `0x00B83C6C` → [ExpPoolFlagsToPoolType](ExpPoolFlagsToPoolType_function_00B84080.md) (function, `0x00B84080`)
- `0x00B83C98` → [EtwTracePool](../../text/2E/EtwTracePool_function_002ECEEC.md) (function, `0x002ECEEC`)
- `0x00B83CA5` → [ExIsSpecialPoolAddress](../../text/49/ExIsSpecialPoolAddress_function_0049C410.md) (function, `0x0049C410`)
- `0x00B83CC6` → [RtlpHpLargeFree](../../text/2E/RtlpHpLargeFree_function_002EC89C.md) (function, `0x002EC89C`)
- `0x00B83D99` → [RtlpHpLfhThreadDataInitializeSet](../../text/4F/RtlpHpLfhThreadDataInitializeSet_function_004F6334.md) (function, `0x004F6334`)
- `0x00B83DE0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B83DEA` → [ObpDeferObjectDeletion](../../text/3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x00B83DF8` → [ObpDeferObjectDeletion](../../text/3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x00B83E5A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B83E7D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B83E8D` → [MmDeterminePoolType](../../text/35/MmDeterminePoolType_function_0035F5B0.md) (function, `0x0035F5B0`)
- `0x00B83ED1` → [ExpFreePoolChecks](../../text/35/ExpFreePoolChecks_function_0035F4F0.md) (function, `0x0035F4F0`)
- `0x00B83F02` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B83F39` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B83F5E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B83F95` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B83FBA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B84022` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00B84048` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B8406A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B83772` → RVA `0x00EFA7C0` (`.data`; read)
- `0x00B83795` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x00B837A9` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00B8380D` → RVA `0x00E27F80` (`.data`; read)
- `0x00B83868` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x00B838DA` → RVA `0x00EFED50` (`.data`; read)
- `0x00B83A51` → RVA `0x00F0DE58` (`.data`; read)
- `0x00B83A63` → RVA `0x00EFACF8` (`.data`; read)
- `0x00B83AEB` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x00B83B1D` → RVA `0x00FC6BD0` (`ALMOSTRO`; read)
- `0x00B83E83` → RVA `0x00EFED20` (`.data`; read/write)
- `0x00B83E9F` → RVA `0x00FCEC68` (`ALMOSTRO`; read)
- `0x00B83FD8` → RVA `0x00FC6ED8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **38**
  - `0x00B83768` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (`POOLCODE` → `.text`)
  - `0x00B83781` → [KxWaitForLockOwnerShip](../../text/25/KxWaitForLockOwnerShip_function_00257EB0.md) (`POOLCODE` → `.text`)
  - `0x00B8387E` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`POOLCODE` → `.text`)
  - `0x00B838BA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B838CD` → [KeReleaseInStackQueuedSpinLock](../../text/34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (`POOLCODE` → `.text`)
  - `0x00B83949` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B83978` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B839CC` → [PspReturnResourceQuota](../../text/38/PspReturnResourceQuota_function_0038FFC4.md) (`POOLCODE` → `.text`)
  - `0x00B83A32` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`POOLCODE` → `.text`)
  - `0x00B83A6A` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../../text/2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (`POOLCODE` → `.text`)
  - `0x00B83A97` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B83ABA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B83AFD` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B83B18` → [ExpCheckForLookaside](../../text/4A/ExpCheckForLookaside_function_004A52DC.md) (`POOLCODE` → `.text`)
  - `0x00B83B2E` → [KeCheckForTimer](../../text/4D/KeCheckForTimer_function_004D870C.md) (`POOLCODE` → `.text`)
  - `0x00B83B44` → [ExpCheckForResource](../../text/49/ExpCheckForResource_function_0049CA24.md) (`POOLCODE` → `.text`)
  - `0x00B83B5E` → [ExpCheckForWorker](../../text/4E/ExpCheckForWorker_function_004EC8FC.md) (`POOLCODE` → `.text`)
  - `0x00B83B85` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B83BE7` → [EtwTracePool](../../text/2E/EtwTracePool_function_002ECEEC.md) (`POOLCODE` → `.text`)
  - `0x00B83C98` → [EtwTracePool](../../text/2E/EtwTracePool_function_002ECEEC.md) (`POOLCODE` → `.text`)
  - `0x00B83CA5` → [ExIsSpecialPoolAddress](../../text/49/ExIsSpecialPoolAddress_function_0049C410.md) (`POOLCODE` → `.text`)
  - `0x00B83CC6` → [RtlpHpLargeFree](../../text/2E/RtlpHpLargeFree_function_002EC89C.md) (`POOLCODE` → `.text`)
  - `0x00B83D99` → [RtlpHpLfhThreadDataInitializeSet](../../text/4F/RtlpHpLfhThreadDataInitializeSet_function_004F6334.md) (`POOLCODE` → `.text`)
  - `0x00B83DE0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B83DEA` → [ObpDeferObjectDeletion](../../text/3A/ObpDeferObjectDeletion_function_003A2394.md) (`POOLCODE` → `.text`)
  - `0x00B83DF8` → [ObpDeferObjectDeletion](../../text/3A/ObpDeferObjectDeletion_function_003A2394.md) (`POOLCODE` → `.text`)
  - `0x00B83E5A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B83E7D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B83E8D` → [MmDeterminePoolType](../../text/35/MmDeterminePoolType_function_0035F5B0.md) (`POOLCODE` → `.text`)
  - `0x00B83ED1` → [ExpFreePoolChecks](../../text/35/ExpFreePoolChecks_function_0035F4F0.md) (`POOLCODE` → `.text`)
  - `0x00B83F02` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B83F39` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B83F5E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B83F95` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B83FBA` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B84022` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`POOLCODE` → `.text`)
  - `0x00B84048` → [memset](../../text/6C/memset_function_006C6C40.md) (`POOLCODE` → `.text`)
  - `0x00B8406A` → [memset](../../text/6C/memset_function_006C6C40.md) (`POOLCODE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **45**
  - `0x00B83732` → [sub_00B830A9 + 0x275](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83748` → [sub_00B830A9 + 0x275](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83759` → [sub_00B830A9 + 0x275](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B8376D` → [sub_00B830A9 + 0x275](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83778` → [sub_00B830A9 + 0x5C7](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83786` → [sub_00B82950 + 0x235](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B8388D` → [sub_00B830A9 + 0x3A8](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B838C4` → [sub_00B82950 + 0x306](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83918` → [sub_00B82950 + 0x2DF](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83927` → [sub_00B82950 + 0x2DF](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B839DD` → [sub_00B82950 + 0x37F](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B839F3` → [sub_00B830A9 + 0x283](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B839FB` → [sub_00B82950 + 0x32A](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83A3E` → [sub_00B82950 + 0x331](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83A44` → [sub_00B82950 + 0x724](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83A59` → [sub_00B830A9 + 0x36A](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83A6F` → [sub_00B830A9 + 0x37C](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83B51` → [sub_00B82950 + 0x135](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83B63` → [sub_00B82950 + 0x135](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83BBE` → [sub_00B82950 + 0x175](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83BEC` → [sub_00B82950 + 0x175](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83BFE` → [sub_00B82950 + 0x2D6](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83C28` → [sub_00B82950 + 0x2D6](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83C31` → [sub_00B82950 + 0x2D6](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83C4E` → [sub_00B830A9 + 0xC4](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83C73` → [sub_00B82950 + 0x6A4](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83C9D` → [sub_00B82950 + 0x6A4](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83CB1` → [sub_00B82950 + 0x5C](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83CBB` → [sub_00B830A9 + 0x146](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83CCB` → [sub_00B82950 + 0x724](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83CFD` → [sub_00B82950 + 0x2D6](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83D0C` → [sub_00B82950 + 0x2D6](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83D38` → [sub_00B82950 + 0x2DF](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83D46` → [sub_00B82950 + 0x2DF](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83D4F` → [sub_00B82950 + 0x496](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83D87` → [sub_00B830A9 + 0x53E](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83D91` → [sub_00B82950 + 0x724](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83D9E` → [sub_00B82950 + 0x48C](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83DEF` → [sub_00B830A9 + 0x302](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83DFD` → [sub_00B830A9 + 0x3A8](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83E37` → [sub_00B82950 + 0x65F](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83F66` → [sub_00B830A9 + 0x167](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83F6F` → [sub_00B830A9 + 0x16C](Unknown_function_00B830A9.md) (`tail-transfer`)
  - `0x00B83FE8` → [sub_00B82950 + 0x313](Unknown_function_00B82950.md) (`tail-transfer`)
  - `0x00B83FF6` → [sub_00B82950 + 0x313](Unknown_function_00B82950.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B8371E  48 3B D3                        cmp rdx, rbx
00B83721  48 8B C8                        mov rcx, rax
00B83724  48 0F 47 D3                     cmova rdx, rbx
00B83728  48 2B CA                        sub rcx, rdx
00B8372B  F0 49 0F B1 4C 24 40            lock cmpxchg qword ptr [r12 + 0x40], rcx
00B83732  0F 85 E6 FB FF FF               jne 0x140b8331e
00B83738  48 8B C2                        mov rax, rdx
00B8373B  F0 49 0F C1 44 24 48            lock xadd qword ptr [r12 + 0x48], rax
00B83742  48 03 D0                        add rdx, rax
00B83745  49 3B 10                        cmp rdx, qword ptr [r8]
00B83748  0F 86 D0 FB FF FF               jbe 0x140b8331e
00B8374E  45 33 C0                        xor r8d, r8d
00B83751  4D 87 44 24 48                  xchg qword ptr [r12 + 0x48], r8
00B83756  4D 85 C0                        test r8, r8
00B83759  0F 84 BF FB FF FF               je 0x140b8331e
00B8375F  45 33 C9                        xor r9d, r9d
00B83762  49 8B D4                        mov rdx, r12
00B83765  41 8B CF                        mov ecx, r15d
00B83768  E8 57 C8 80 FF                  call 0x14038ffc4
00B8376D  E9 AC FB FF FF                  jmp 0x140b8331e
00B83772  8B 05 48 70 37 00               mov eax, dword ptr [rip + 0x377048]
00B83778  E9 F3 FE FF FF                  jmp 0x140b83670
00B8377D  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00B83781  E8 2A 47 6D FF                  call 0x140257eb0
00B83786  E9 FA F3 FF FF                  jmp 0x140b82b85
00B8378B  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00B8378F  81 E1 00 01 00 00               and ecx, 0x100
00B83795  48 3B 3D 14 33 44 00            cmp rdi, qword ptr [rip + 0x443314]
00B8379C  0F 84 C6 00 00 00               je 0x140b83868
00B837A2  4C 8B AF F8 02 00 00            mov r13, qword ptr [rdi + 0x2f8]
00B837A9  4C 8D 0D 50 C8 47 FF            lea r9, [rip - 0xb837b0]
00B837B0  41 8B C4                        mov eax, r12d
00B837B3  48 85 C9                        test rcx, rcx
00B837B6  0F 95 C0                        setne al
00B837B9  44 8B E0                        mov r12d, eax
00B837BC  43 0F B6 84 E1 50 73 FC 00      movzx eax, byte ptr [r9 + r12*8 + 0xfc7350]
00B837C5  88 45 A7                        mov byte ptr [rbp - 0x59], al
00B837C8  41 8B C4                        mov eax, r12d
00B837CB  48 C1 E0 07                     shl rax, 7
00B837CF  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00B837D3  4E 8D 34 28                     lea r14, [rax + r13]
00B837D7  41 0F 0D 0E                     prefetchw byte ptr [r14]
00B837DB  4D 8B 3E                        mov r15, qword ptr [r14]
00B837DE  49 8B 46 40                     mov rax, qword ptr [r14 + 0x40]
00B837E2  49 83 7E 50 00                  cmp qword ptr [r14 + 0x50], 0
00B837E7  74 20                           je 0x140b83809
00B837E9  4D 6B C4 38                     imul r8, r12, 0x38
00B837ED  49 3B C7                        cmp rax, r15
00B837F0  76 17                           jbe 0x140b83809
00B837F2  4B 8B 94 08 48 66 F0 00         mov rdx, qword ptr [r8 + r9 + 0xf06648]
00B837FA  48 8B C8                        mov rcx, rax
00B837FD  49 2B CF                        sub rcx, r15
00B83800  48 3B CA                        cmp rcx, rdx
00B83803  0F 87 75 01 00 00               ja 0x140b8397e
00B83809  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
00B8380D  4C 8D 15 6C 47 2A 00            lea r10, [rip + 0x2a476c]
00B83814  4C 8B 5D BF                     mov r11, qword ptr [rbp - 0x41]
00B83818  4D 3B C7                        cmp r8, r15
00B8381B  4D 8B CF                        mov r9, r15
00B8381E  49 8B CF                        mov rcx, r15
00B83821  49 8B C7                        mov rax, r15
00B83824  4D 0F 42 C8                     cmovb r9, r8
00B83828  49 2B C8                        sub rcx, r8
00B8382B  33 D2                           xor edx, edx
00B8382D  4D 3B C7                        cmp r8, r15
00B83830  48 0F 42 D1                     cmovb rdx, rcx
00B83834  F0 49 0F B1 16                  lock cmpxchg qword ptr [r14], rdx
00B83839  4C 8B F8                        mov r15, rax
00B8383C  75 DA                           jne 0x140b83818
00B8383E  4D 2B C1                        sub r8, r9
00B83841  0F 85 56 02 00 00               jne 0x140b83a9d
00B83847  F6 45 A7 04                     test byte ptr [rbp - 0x59], 4
00B8384B  74 10                           je 0x140b8385d
00B8384D  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00B83851  48 F7 D8                        neg rax
00B83854  F0 4A 01 84 E7 00 02 00 00      lock add qword ptr [rdi + r12*8 + 0x200], rax
00B8385D  4C 8B 6D 67                     mov r13, qword ptr [rbp + 0x67]
00B83861  45 33 E4                        xor r12d, r12d
00B83864  4C 8B 7D 77                     mov r15, qword ptr [rbp + 0x77]
00B83868  83 3D A1 17 44 00 00            cmp dword ptr [rip + 0x4417a1], 0
00B8386F  74 12                           je 0x140b83883
00B83871  33 D2                           xor edx, edx
00B83873  48 8D 4F D0                     lea rcx, [rdi - 0x30]
00B83877  44 8B CB                        mov r9d, ebx
00B8387A  44 8D 42 01                     lea r8d, [rdx + 1]
00B8387E  E8 61 D1 68 FF                  call 0x1402109e4
00B83883  F0 48 0F C1 77 D0               lock xadd qword ptr [rdi - 0x30], rsi
00B83889  48 83 EE 01                     sub rsi, 1
00B8388D  0F 8F BE FB FF FF               jg 0x140b83451
00B83893  48 8B 4F D8                     mov rcx, qword ptr [rdi - 0x28]
00B83897  48 85 C9                        test rcx, rcx
00B8389A  0F 85 03 05 00 00               jne 0x140b83da3
00B838A0  48 85 F6                        test rsi, rsi
00B838A3  0F 89 4B 05 00 00               jns 0x140b83df4
00B838A9  33 D2                           xor edx, edx
00B838AB  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00B838B0  44 8D 49 04                     lea r9d, [rcx + 4]
00B838B4  4C 8B C7                        mov r8, rdi
00B838B7  8D 4A 18                        lea ecx, [rdx + 0x18]
00B838BA  E8 A1 9D 97 FF                  call 0x1404fd660
00B838BF  CC                              int3
00B838C0  48 8B 75 9F                     mov rsi, qword ptr [rbp - 0x61]
00B838C4  E9 8D F3 FF FF                  jmp 0x140b82c56
00B838C9  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00B838CD  E8 0E F4 7B FF                  call 0x140342ce0
00B838D2  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
00B838DA  44 8B 05 6F B4 37 00            mov r8d, dword ptr [rip + 0x37b46f]
00B838E1  8B C8                           mov ecx, eax
00B838E3  41 FF C8                        dec r8d
00B838E6  48 8D 05 13 C7 47 FF            lea rax, [rip - 0xb838ed]
00B838ED  48 8B 94 C8 20 AD EF 00         mov rdx, qword ptr [rax + rcx*8 + 0xefad20]
00B838F5  4B 8D 0C 80                     lea rcx, [r8 + r8*4]
00B838F9  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00B838FD  48 C1 E1 04                     shl rcx, 4
00B83901  48 F7 D8                        neg rax
00B83904  48 03 CA                        add rcx, rdx
00B83907  48 0F BA E6 08                  bt rsi, 8
00B8390C  72 0F                           jb 0x140b8391d
00B8390E  F0 48 FF 41 18                  lock inc qword ptr [rcx + 0x18]
00B83913  F0 48 01 41 08                  lock add qword ptr [rcx + 8], rax
00B83918  E9 12 F3 FF FF                  jmp 0x140b82c2f
00B8391D  F0 48 FF 41 30                  lock inc qword ptr [rcx + 0x30]
00B83922  F0 48 01 41 20                  lock add qword ptr [rcx + 0x20], rax
00B83927  E9 03 F3 FF FF                  jmp 0x140b82c2f
00B8392C  4C 39 55 97                     cmp qword ptr [rbp - 0x69], r10
00B83930  0F 85 AC 00 00 00               jne 0x140b839e2
00B83936  4D 8B C8                        mov r9, r8
00B83939  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00B8393E  4D 8B C7                        mov r8, r15
00B83941  48 8B D7                        mov rdx, rdi
00B83944  B9 21 00 00 00                  mov ecx, 0x21
00B83949  E8 12 9D 97 FF                  call 0x1404fd660
00B8394E  CC                              int3
00B8394F  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00B83959  4C 3B F0                        cmp r14, rax
00B8395C  0F 83 12 06 00 00               jae 0x140b83f74
00B83962  BA 02 00 00 00                  mov edx, 2
00B83967  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00B8396C  4D 8B CE                        mov r9, r14
00B8396F  B9 F1 01 00 00                  mov ecx, 0x1f1
00B83974  44 8D 42 FF                     lea r8d, [rdx - 1]
00B83978  E8 E3 9C 97 FF                  call 0x1404fd660
00B8397D  CC                              int3
00B8397E  48 3B 55 9F                     cmp rdx, qword ptr [rbp - 0x61]
00B83982  48 8B C8                        mov rcx, rax
00B83985  48 0F 47 55 9F                  cmova rdx, qword ptr [rbp - 0x61]
00B8398A  48 2B CA                        sub rcx, rdx
00B8398D  F0 49 0F B1 4E 40               lock cmpxchg qword ptr [r14 + 0x40], rcx
00B83993  0F 85 70 FE FF FF               jne 0x140b83809
00B83999  48 8B C2                        mov rax, rdx
00B8399C  F0 49 0F C1 46 48               lock xadd qword ptr [r14 + 0x48], rax
00B839A2  48 03 D0                        add rdx, rax
00B839A5  4B 3B 94 08 48 66 F0 00         cmp rdx, qword ptr [r8 + r9 + 0xf06648]
00B839AD  0F 86 56 FE FF FF               jbe 0x140b83809
00B839B3  45 33 C0                        xor r8d, r8d
00B839B6  4D 87 46 48                     xchg qword ptr [r14 + 0x48], r8
00B839BA  4D 85 C0                        test r8, r8
00B839BD  0F 84 46 FE FF FF               je 0x140b83809
00B839C3  45 33 C9                        xor r9d, r9d
00B839C6  49 8B D6                        mov rdx, r14
00B839C9  41 8B CC                        mov ecx, r12d
00B839CC  E8 F3 C5 80 FF                  call 0x14038ffc4
00B839D1  E9 33 FE FF FF                  jmp 0x140b83809
00B839D6  48 81 C3 C0 00 00 00            add rbx, 0xc0
00B839DD  E9 ED F2 FF FF                  jmp 0x140b82ccf
00B839E2  4C 89 55 97                     mov qword ptr [rbp - 0x69], r10
00B839E6  4F 8D 24 13                     lea r12, [r11 + r10]
00B839EA  41 0F 0D 0C 24                  prefetchw byte ptr [r12]
00B839EF  49 8B 34 24                     mov rsi, qword ptr [r12]
00B839F3  E9 34 F9 FF FF                  jmp 0x140b8332c
00B839F8  48 85 D2                        test rdx, rdx
00B839FB  0F 84 79 F2 FF FF               je 0x140b82c7a
00B83A01  8D 46 0F                        lea eax, [rsi + 0xf]
00B83A04  C1 E8 04                        shr eax, 4
00B83A07  48 8D 35 F2 C5 47 FF            lea rsi, [rip - 0xb83a0e]
00B83A0E  0F B6 8C 30 80 0B 01 00         movzx ecx, byte ptr [rax + rsi + 0x10b80]
00B83A16  83 C1 DF                        add ecx, -0x21
00B83A19  48 FF C1                        inc rcx
00B83A1C  48 C1 E1 06                     shl rcx, 6
00B83A20  48 03 CA                        add rcx, rdx
00B83A23  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00B83A26  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00B83A2A  66 39 01                        cmp word ptr [rcx], ax
00B83A2D  73 1A                           jae 0x140b83a49
00B83A2F  49 8B D6                        mov rdx, r14
00B83A32  E8 79 6B B3 FF                  call 0x1406ba5b0
00B83A37  B8 01 00 00 00                  mov eax, 1
00B83A3C  85 C0                           test eax, eax
00B83A3E  0F 84 3D F2 FF FF               je 0x140b82c81
00B83A44  E9 2B F6 FF FF                  jmp 0x140b83074
00B83A49  FF 41 20                        inc dword ptr [rcx + 0x20]
00B83A4C  41 8B C4                        mov eax, r12d
00B83A4F  EB EB                           jmp 0x140b83a3c
00B83A51  8B 05 01 A4 38 00               mov eax, dword ptr [rip + 0x38a401]
00B83A57  85 C0                           test eax, eax
00B83A59  0F 85 B4 F9 FF FF               jne 0x140b83413
00B83A5F  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
00B83A63  48 8D 0D 8E 72 37 00            lea rcx, [rip + 0x37728e]
00B83A6A  E8 D9 D4 76 FF                  call 0x1402f0f48
00B83A6F  E9 B1 F9 FF FF                  jmp 0x140b83425
00B83A74  48 8B 4F D8                     mov rcx, qword ptr [rdi - 0x28]
00B83A78  48 85 C9                        test rcx, rcx
00B83A7B  75 43                           jne 0x140b83ac0
00B83A7D  48 85 F6                        test rsi, rsi
00B83A80  0F 89 60 03 00 00               jns 0x140b83de6
00B83A86  33 D2                           xor edx, edx
00B83A88  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00B83A8D  44 8D 49 04                     lea r9d, [rcx + 4]
00B83A91  4C 8B C7                        mov r8, rdi
00B83A94  8D 4A 18                        lea ecx, [rdx + 0x18]
00B83A97  E8 C4 9B 97 FF                  call 0x1404fd660
00B83A9C  CC                              int3
00B83A9D  4D 3B EA                        cmp r13, r10
00B83AA0  0F 85 E5 00 00 00               jne 0x140b83b8b
00B83AA6  4C 8B 4D 9F                     mov r9, qword ptr [rbp - 0x61]
00B83AAA  48 8B D7                        mov rdx, rdi
00B83AAD  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00B83AB2  B9 21 00 00 00                  mov ecx, 0x21
00B83AB7  4D 8B C4                        mov r8, r12
00B83ABA  E8 A1 9B 97 FF                  call 0x1404fd660
00B83ABF  CC                              int3
00B83AC0  41 B9 03 00 00 00               mov r9d, 3
00B83AC6  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B83ACB  4C 8D 1D 2E C5 47 FF            lea r11, [rip - 0xb83ad2]
00B83AD2  4C 8B C7                        mov r8, rdi
00B83AD5  48 8D 47 D0                     lea rax, [rdi - 0x30]
00B83AD9  48 C1 E8 08                     shr rax, 8
00B83ADD  0F B6 D0                        movzx edx, al
00B83AE0  41 8D 49 15                     lea ecx, [r9 + 0x15]
00B83AE4  0F B6 47 E8                     movzx eax, byte ptr [rdi - 0x18]
00B83AE8  48 33 D0                        xor rdx, rax
00B83AEB  0F B6 05 5A 33 44 00            movzx eax, byte ptr [rip + 0x44335a]
00B83AF2  48 33 D0                        xor rdx, rax
00B83AF5  49 8B 94 D3 00 78 FC 00         mov rdx, qword ptr [r11 + rdx*8 + 0xfc7800]
00B83AFD  E8 5E 9B 97 FF                  call 0x1404fd660
00B83B02  CC                              int3
00B83B03  40 F6 C6 C0                     test sil, 0xc0
00B83B07  0F 95 C1                        setne cl
00B83B0A  0F BA E0 09                     bt eax, 9
00B83B0E  0F 92 C0                        setb al
00B83B11  84 C8                           test al, cl
00B83B13  74 08                           je 0x140b83b1d
00B83B15  49 8B CE                        mov rcx, r14
00B83B18  E8 BF 17 92 FF                  call 0x1404a52dc
00B83B1D  8B 05 AD 30 44 00               mov eax, dword ptr [rip + 0x4430ad]
00B83B23  A8 01                           test al, 1
00B83B25  74 0C                           je 0x140b83b33
00B83B27  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
00B83B2B  49 8B CE                        mov rcx, r14
00B83B2E  E8 D9 4B 95 FF                  call 0x1404d870c
00B83B33  8B 05 97 30 44 00               mov eax, dword ptr [rip + 0x443097]
00B83B39  A8 04                           test al, 4
00B83B3B  74 0C                           je 0x140b83b49
00B83B3D  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
00B83B41  49 8B CE                        mov rcx, r14
00B83B44  E8 DB 8E 91 FF                  call 0x14049ca24
00B83B49  8B 05 81 30 44 00               mov eax, dword ptr [rip + 0x443081]
00B83B4F  A8 02                           test al, 2
00B83B51  0F 84 2E EF FF FF               je 0x140b82a85
00B83B57  48 8B 55 9F                     mov rdx, qword ptr [rbp - 0x61]
00B83B5B  49 8B CE                        mov rcx, r14
00B83B5E  E8 99 8D 96 FF                  call 0x1404ec8fc
00B83B63  E9 1D EF FF FF                  jmp 0x140b82a85
00B83B68  48 85 D2                        test rdx, rdx
00B83B6B  74 03                           je 0x140b83b70
00B83B6D  45 8B E6                        mov r12d, r14d
00B83B70  45 8B CC                        mov r9d, r12d
00B83B73  4D 8B C5                        mov r8, r13
00B83B76  BA 0D 00 00 00                  mov edx, 0xd
00B83B7B  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00B83B80  B9 C2 00 00 00                  mov ecx, 0xc2
00B83B85  E8 D6 9A 97 FF                  call 0x1404fd660
00B83B8A  CC                              int3
00B83B8B  4D 8B EA                        mov r13, r10
00B83B8E  4F 8D 34 13                     lea r14, [r11 + r10]
00B83B92  41 0F 0D 0E                     prefetchw byte ptr [r14]
00B83B96  4D 8B 3E                        mov r15, qword ptr [r14]
00B83B99  E9 7A FC FF FF                  jmp 0x140b83818
00B83B9E  8B D6                           mov edx, esi
00B83BA0  48 8D 45 A8                     lea rax, [rbp - 0x58]
00B83BA4  83 E2 10                        and edx, 0x10
00B83BA7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B83BAC  4C 8D 4D 77                     lea r9, [rbp + 0x77]
00B83BB0  48 8B CE                        mov rcx, rsi
00B83BB3  4C 8D 45 AF                     lea r8, [rbp - 0x51]
00B83BB7  E8 C4 04 00 00                  call 0x140b84080
00B83BBC  85 C0                           test eax, eax
00B83BBE  0F 88 01 EF FF FF               js 0x140b82ac5
00B83BC4  80 7D 77 00                     cmp byte ptr [rbp + 0x77], 0
00B83BC8  8B 55 AF                        mov edx, dword ptr [rbp - 0x51]
00B83BCB  74 06                           je 0x140b83bd3
00B83BCD  83 CA 08                        or edx, 8
00B83BD0  89 55 AF                        mov dword ptr [rbp - 0x51], edx
00B83BD3  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00B83BD7  B9 22 0E 00 00                  mov ecx, 0xe22
00B83BDC  4C 8B CF                        mov r9, rdi
00B83BDF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B83BE4  44 8B C3                        mov r8d, ebx
00B83BE7  E8 00 93 76 FF                  call 0x1402eceec
00B83BEC  E9 D4 EE FF FF                  jmp 0x140b82ac5
00B83BF1  49 63 C1                        movsxd rax, r9d
00B83BF4  41 F6 44 C0 38 01               test byte ptr [r8 + rax*8 + 0x38], 1
00B83BFA  4D 8D 1C C0                     lea r11, [r8 + rax*8]
00B83BFE  0F 85 22 F0 FF FF               jne 0x140b82c26
00B83C04  49 8B 43 38                     mov rax, qword ptr [r11 + 0x38]
00B83C08  4E 8D 14 95 3F 00 00 00         lea r10, [r10*4 + 0x3f]
00B83C10  49 83 E2 C0                     and r10, 0xffffffffffffffc0
00B83C14  BB 80 00 00 00                  mov ebx, 0x80
00B83C19  49 83 FA 40                     cmp r10, 0x40
00B83C1D  4C 0F 44 D3                     cmove r10, rbx
00B83C21  49 8D 1C 0A                     lea rbx, [r10 + rcx]
00B83C25  48 3B C8                        cmp rcx, rax
00B83C28  0F 8D F8 EF FF FF               jge 0x140b82c26
00B83C2E  48 3B D8                        cmp rbx, rax
00B83C31  0F 8D EF EF FF FF               jge 0x140b82c26
00B83C37  F0 49 0F B1 5B 38               lock cmpxchg qword ptr [r11 + 0x38], rbx
00B83C3D  0F 84 8D 00 00 00               je 0x140b83cd0
00B83C43  48 8B 0A                        mov rcx, qword ptr [rdx]
00B83C46  EB D9                           jmp 0x140b83c21
00B83C48  41 8B D4                        mov edx, r12d
00B83C4B  45 8B D4                        mov r10d, r12d
00B83C4E  E9 1A F5 FF FF                  jmp 0x140b8316d
00B83C53  8B D7                           mov edx, edi
00B83C55  48 8D 45 7F                     lea rax, [rbp + 0x7f]
00B83C59  83 E2 10                        and edx, 0x10
00B83C5C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B83C61  4C 8D 4D 67                     lea r9, [rbp + 0x67]
00B83C65  48 8B CF                        mov rcx, rdi
00B83C68  4C 8D 45 AB                     lea r8, [rbp - 0x55]
00B83C6C  E8 0F 04 00 00                  call 0x140b84080
00B83C71  85 C0                           test eax, eax
00B83C73  0F 88 7B F3 FF FF               js 0x140b82ff4
00B83C79  8B 55 AB                        mov edx, dword ptr [rbp - 0x55]
00B83C7C  44 38 65 67                     cmp byte ptr [rbp + 0x67], r12b
00B83C80  74 06                           je 0x140b83c88
00B83C82  83 CA 08                        or edx, 8
00B83C85  89 55 AB                        mov dword ptr [rbp - 0x55], edx
00B83C88  B9 22 0E 00 00                  mov ecx, 0xe22
00B83C8D  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00B83C92  4D 8B CD                        mov r9, r13
00B83C95  44 8B C6                        mov r8d, esi
00B83C98  E8 4F 92 76 FF                  call 0x1402eceec
00B83C9D  E9 52 F3 FF FF                  jmp 0x140b82ff4
00B83CA2  49 8B CD                        mov rcx, r13
00B83CA5  E8 66 87 91 FF                  call 0x14049c410
00B83CAA  BA 00 01 00 00                  mov edx, 0x100
00B83CAF  85 C0                           test eax, eax
00B83CB1  0F 85 F5 EC FF FF               jne 0x140b829ac
00B83CB7  44 8D 42 FF                     lea r8d, [rdx - 1]
00B83CBB  E9 2F F5 FF FF                  jmp 0x140b831ef
00B83CC0  49 8B D6                        mov rdx, r14
00B83CC3  49 8B CF                        mov rcx, r15
00B83CC6  E8 D1 8B 76 FF                  call 0x1402ec89c
00B83CCB  E9 A4 F3 FF FF                  jmp 0x140b83074
00B83CD0  49 8B 50 48                     mov rdx, qword ptr [r8 + 0x48]
00B83CD4  48 2B C3                        sub rax, rbx
00B83CD7  4C 8B D0                        mov r10, rax
00B83CDA  49 F7 DA                        neg r10
00B83CDD  48 85 C0                        test rax, rax
00B83CE0  4C 0F 49 D0                     cmovns r10, rax
00B83CE4  49 63 C1                        movsxd rax, r9d
00B83CE7  48 8D 0C 40                     lea rcx, [rax + rax*2]
00B83CEB  48 8B 44 CA 10                  mov rax, qword ptr [rdx + rcx*8 + 0x10]
00B83CF0  4C 8B 44 CA 18                  mov r8, qword ptr [rdx + rcx*8 + 0x18]
00B83CF5  48 85 C0                        test rax, rax
00B83CF8  75 09                           jne 0x140b83d03
00B83CFA  4D 85 C0                        test r8, r8
00B83CFD  0F 84 23 EF FF FF               je 0x140b82c26
00B83D03  49 F7 DA                        neg r10
00B83D06  F0 4C 01 54 CA 20               lock add qword ptr [rdx + rcx*8 + 0x20], r10
00B83D0C  E9 15 EF FF FF                  jmp 0x140b82c26
00B83D11  49 8B 50 48                     mov rdx, qword ptr [r8 + 0x48]
00B83D15  48 2B C3                        sub rax, rbx
00B83D18  48 8B C8                        mov rcx, rax
00B83D1B  48 F7 D9                        neg rcx
00B83D1E  48 85 C0                        test rax, rax
00B83D21  48 0F 49 C8                     cmovns rcx, rax
00B83D25  49 03 D2                        add rdx, r10
00B83D28  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
00B83D2C  4C 8B 42 18                     mov r8, qword ptr [rdx + 0x18]
00B83D30  48 85 C0                        test rax, rax
00B83D33  75 09                           jne 0x140b83d3e
00B83D35  4D 85 C0                        test r8, r8
00B83D38  0F 84 F1 EE FF FF               je 0x140b82c2f
00B83D3E  48 F7 D9                        neg rcx
00B83D41  F0 48 01 4A 20                  lock add qword ptr [rdx + 0x20], rcx
00B83D46  E9 E4 EE FF FF                  jmp 0x140b82c2f
00B83D4B  80 7F 16 01                     cmp byte ptr [rdi + 0x16], 1
00B83D4F  0F 84 91 F0 FF FF               je 0x140b82de6
00B83D55  8B CB                           mov ecx, ebx
00B83D57  48 8B C3                        mov rax, rbx
00B83D5A  48 C1 E8 06                     shr rax, 6
00B83D5E  83 E1 3F                        and ecx, 0x3f
00B83D61  48 8B 54 C7 40                  mov rdx, qword ptr [rdi + rax*8 + 0x40]
00B83D66  49 C7 C0 FE FF FF FF            mov r8, 0xfffffffffffffffe
00B83D6D  49 D3 C0                        rol r8, cl
00B83D70  4C 8B CB                        mov r9, rbx
00B83D73  48 8D 0C C7                     lea rcx, [rdi + rax*8]
00B83D77  49 8B C0                        mov rax, r8
00B83D7A  48 23 C2                        and rax, rdx
00B83D7D  49 F7 D0                        not r8
00B83D80  48 89 41 40                     mov qword ptr [rcx + 0x40], rax
00B83D84  4C 85 C2                        test rdx, r8
00B83D87  0F 84 5A F8 FF FF               je 0x140b835e7
00B83D8D  66 FF 47 20                     inc word ptr [rdi + 0x20]
00B83D91  E9 DE F2 FF FF                  jmp 0x140b83074
00B83D96  48 8B CE                        mov rcx, rsi
00B83D99  E8 96 25 97 FF                  call 0x1404f6334
00B83D9E  E9 39 F0 FF FF                  jmp 0x140b82ddc
00B83DA3  41 B9 03 00 00 00               mov r9d, 3
00B83DA9  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B83DAE  4C 8D 1D 4B C2 47 FF            lea r11, [rip - 0xb83db5]
00B83DB5  4C 8B C7                        mov r8, rdi
00B83DB8  48 8D 47 D0                     lea rax, [rdi - 0x30]
00B83DBC  48 C1 E8 08                     shr rax, 8
00B83DC0  0F B6 D0                        movzx edx, al
00B83DC3  41 8D 49 15                     lea ecx, [r9 + 0x15]
00B83DC7  0F B6 47 E8                     movzx eax, byte ptr [rdi - 0x18]
00B83DCB  48 33 D0                        xor rdx, rax
00B83DCE  0F B6 05 77 30 44 00            movzx eax, byte ptr [rip + 0x443077]
00B83DD5  48 33 D0                        xor rdx, rax
00B83DD8  49 8B 94 D3 00 78 FC 00         mov rdx, qword ptr [r11 + rdx*8 + 0xfc7800]
00B83DE0  E8 7B 98 97 FF                  call 0x1404fd660
00B83DE5  CC                              int3
00B83DE6  48 8D 4F D0                     lea rcx, [rdi - 0x30]
00B83DEA  E8 A5 E5 81 FF                  call 0x1403a2394
00B83DEF  E9 B7 F5 FF FF                  jmp 0x140b833ab
00B83DF4  48 8D 4F D0                     lea rcx, [rdi - 0x30]
00B83DF8  E8 97 E5 81 FF                  call 0x1403a2394
00B83DFD  E9 4F F6 FF FF                  jmp 0x140b83451
00B83E02  8B 03                           mov eax, dword ptr [rbx]
00B83E04  4C 8D 43 10                     lea r8, [rbx + 0x10]
00B83E08  8B C8                           mov ecx, eax
00B83E0A  44 8B D0                        mov r10d, eax
00B83E0D  C1 E9 10                        shr ecx, 0x10
00B83E10  41 81 E2 00 40 00 00            and r10d, 0x4000
00B83E17  74 04                           je 0x140b83e1d
00B83E19  4C 8D 43 18                     lea r8, [rbx + 0x18]
00B83E1D  4D 3B C5                        cmp r8, r13
00B83E20  72 3E                           jb 0x140b83e60
00B83E22  4D 8D 8D FF 0F 00 00            lea r9, [r13 + 0xfff]
00B83E29  49 81 E1 00 F0 FF FF            and r9, 0xfffffffffffff000
00B83E30  4E 8D 04 2A                     lea r8, [rdx + r13]
00B83E34  4D 3B C1                        cmp r8, r9
00B83E37  0F 83 72 F1 FF FF               jae 0x140b82faf
00B83E3D  41 38 08                        cmp byte ptr [r8], cl
00B83E40  0F 84 14 02 00 00               je 0x140b8405a
00B83E46  4C 8B C8                        mov r9, rax
00B83E49  48 C7 44 24 20 24 00 00 00      mov qword ptr [rsp + 0x20], 0x24
00B83E52  49 8B D5                        mov rdx, r13
00B83E55  B9 C1 00 00 00                  mov ecx, 0xc1
00B83E5A  E8 01 98 97 FF                  call 0x1404fd660
00B83E5F  CC                              int3
00B83E60  41 38 08                        cmp byte ptr [r8], cl
00B83E63  0F 84 E9 01 00 00               je 0x140b84052
00B83E69  4C 8B C8                        mov r9, rax
00B83E6C  48 C7 44 24 20 23 00 00 00      mov qword ptr [rsp + 0x20], 0x23
00B83E75  49 8B D5                        mov rdx, r13
00B83E78  B9 C1 00 00 00                  mov ecx, 0xc1
00B83E7D  E8 DE 97 97 FF                  call 0x1404fd660
00B83E82  CC                              int3
00B83E83  F0 FF 0D 96 AE 37 00            lock dec dword ptr [rip + 0x37ae96]
00B83E8A  49 8B CD                        mov rcx, r13
00B83E8D  E8 1E B7 7D FF                  call 0x14035f5b0
00B83E92  49 8B DD                        mov rbx, r13
00B83E95  48 8B F8                        mov rdi, rax
00B83E98  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
00B83E9F  44 38 25 C2 AD 44 00            cmp byte ptr [rip + 0x44adc2], r12b
00B83EA6  0F 85 93 00 00 00               jne 0x140b83f3f
00B83EAC  8B 53 04                        mov edx, dword ptr [rbx + 4]
00B83EAF  41 8B C5                        mov eax, r13d
00B83EB2  25 FF 0F 00 00                  and eax, 0xfff
00B83EB7  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00B83EBC  B9 00 10 00 00                  mov ecx, 0x1000
00B83EC1  41 B9 80 00 00 00               mov r9d, 0x80
00B83EC7  2B C8                           sub ecx, eax
00B83EC9  8B F1                           mov esi, ecx
00B83ECB  44 8B C1                        mov r8d, ecx
00B83ECE  49 8B CD                        mov rcx, r13
00B83ED1  E8 1A B6 7D FF                  call 0x14035f4f0
00B83ED6  4C 8B DF                        mov r11, rdi
00B83ED9  41 B8 00 01 00 00               mov r8d, 0x100
00B83EDF  4D 23 D8                        and r11, r8
00B83EE2  44 0F 20 C1                     mov rcx, cr8
00B83EE6  0F 94 C0                        sete al
00B83EE9  FE C0                           inc al
00B83EEB  3A C8                           cmp cl, al
00B83EED  76 19                           jbe 0x140b83f08
00B83EEF  0F B6 D1                        movzx edx, cl
00B83EF2  4D 8B CD                        mov r9, r13
00B83EF5  41 8D 48 C1                     lea ecx, [r8 - 0x3f]
00B83EF9  48 C7 44 24 20 31 00 00 00      mov qword ptr [rsp + 0x20], 0x31
00B83F02  E8 59 97 97 FF                  call 0x1404fd660
00B83F07  CC                              int3
00B83F08  0F B7 13                        movzx edx, word ptr [rbx]
00B83F0B  81 E2 FF 1F 00 00               and edx, 0x1fff
00B83F11  4C 8D 72 0F                     lea r14, [rdx + 0xf]
00B83F15  49 83 E6 F0                     and r14, 0xfffffffffffffff0
00B83F19  4C 3B F6                        cmp r14, rsi
00B83F1C  0F 84 E0 FE FF FF               je 0x140b83e02
00B83F22  44 8B C2                        mov r8d, edx
00B83F25  48 C7 44 24 20 21 00 00 00      mov qword ptr [rsp + 0x20], 0x21
00B83F2E  49 8B D5                        mov rdx, r13
00B83F31  4C 8B CE                        mov r9, rsi
00B83F34  B9 C1 00 00 00                  mov ecx, 0xc1
00B83F39  E8 22 97 97 FF                  call 0x1404fd660
00B83F3E  CC                              int3
00B83F3F  48 3B DE                        cmp rbx, rsi
00B83F42  0F 83 B3 00 00 00               jae 0x140b83ffb
00B83F48  BA 02 00 00 00                  mov edx, 2
00B83F4D  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00B83F52  4C 8B CB                        mov r9, rbx
00B83F55  B9 F1 01 00 00                  mov ecx, 0x1f1
00B83F5A  44 8D 42 FF                     lea r8d, [rdx - 1]
00B83F5E  E8 FD 96 97 FF                  call 0x1404fd660
00B83F63  CC                              int3
00B83F64  3C 04                           cmp al, 4
00B83F66  0F 84 A4 F2 FF FF               je 0x140b83210
00B83F6C  48 8B F2                        mov rsi, rdx
00B83F6F  E9 A1 F2 FF FF                  jmp 0x140b83215
00B83F74  41 F6 C6 07                     test r14b, 7
00B83F78  74 21                           je 0x140b83f9b
00B83F7A  B8 02 00 00 00                  mov eax, 2
00B83F7F  48 C7 44 24 20 08 00 00 00      mov qword ptr [rsp + 0x20], 8
00B83F88  44 8B C0                        mov r8d, eax
00B83F8B  8B D0                           mov edx, eax
00B83F8D  4D 8B CE                        mov r9, r14
00B83F90  B9 F1 01 00 00                  mov ecx, 0x1f1
00B83F95  E8 C6 96 97 FF                  call 0x1404fd660
00B83F9A  CC                              int3
00B83F9B  4A 8D 04 36                     lea rax, [rsi + r14]
00B83F9F  49 3B C6                        cmp rax, r14
00B83FA2  73 1C                           jae 0x140b83fc0
00B83FA4  BA 02 00 00 00                  mov edx, 2
00B83FA9  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00B83FAE  4D 8B CE                        mov r9, r14
00B83FB1  B9 F1 01 00 00                  mov ecx, 0x1f1
00B83FB6  44 8D 42 01                     lea r8d, [rdx + 1]
00B83FBA  E8 A1 96 97 FF                  call 0x1404fd660
00B83FBF  CC                              int3
00B83FC0  48 BB 00 00 00 00 00 80 00 00   movabs rbx, 0x800000000000
00B83FCA  48 8B FE                        mov rdi, rsi
00B83FCD  49 03 DE                        add rbx, r14
00B83FD0  48 C1 EF 03                     shr rdi, 3
00B83FD4  48 C1 EB 03                     shr rbx, 3
00B83FD8  48 03 1D F9 2E 44 00            add rbx, qword ptr [rip + 0x442ef9]
00B83FDF  48 85 FF                        test rdi, rdi
00B83FE2  75 7E                           jne 0x140b84062
00B83FE4  40 F6 C6 07                     test sil, 7
00B83FE8  0F 84 75 EC FF FF               je 0x140b82c63
00B83FEE  40 0F B6 C6                     movzx eax, sil
00B83FF2  24 07                           and al, 7
00B83FF4  88 03                           mov byte ptr [rbx], al
00B83FF6  E9 68 EC FF FF                  jmp 0x140b82c63
00B83FFB  48 8D 83 00 10 00 00            lea rax, [rbx + 0x1000]
00B84002  48 3B C3                        cmp rax, rbx
00B84005  73 21                           jae 0x140b84028
00B84007  B9 00 10 00 00                  mov ecx, 0x1000
00B8400C  BA 02 00 00 00                  mov edx, 2
00B84011  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B84016  4C 8B CB                        mov r9, rbx
00B84019  B9 F1 01 00 00                  mov ecx, 0x1f1
00B8401E  44 8D 42 01                     lea r8d, [rdx + 1]
00B84022  E8 39 96 97 FF                  call 0x1404fd660
00B84027  CC                              int3
00B84028  48 B9 00 00 00 00 00 80 00 00   movabs rcx, 0x800000000000
00B84032  33 D2                           xor edx, edx
00B84034  48 03 CB                        add rcx, rbx
00B84037  41 B8 00 02 00 00               mov r8d, 0x200
00B8403D  48 C1 E9 03                     shr rcx, 3
00B84041  48 03 0D 90 2E 44 00            add rcx, qword ptr [rip + 0x442e90]
00B84048  E8 F3 2B B4 FF                  call 0x1406c6c40
00B8404D  E9 5A FE FF FF                  jmp 0x140b83eac
00B84052  49 FF C0                        inc r8
00B84055  E9 C3 FD FF FF                  jmp 0x140b83e1d
00B8405A  49 FF C0                        inc r8
00B8405D  E9 D2 FD FF FF                  jmp 0x140b83e34
00B84062  4C 8B C7                        mov r8, rdi
00B84065  33 D2                           xor edx, edx
00B84067  48 8B CB                        mov rcx, rbx
00B8406A  E8 D1 2B B4 FF                  call 0x1406c6c40
00B8406F  48 03 DF                        add rbx, rdi
00B84072  E9 6D FF FF FF                  jmp 0x140b83fe4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B8371E(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    unsigned __int64 v_stack_p20;

    if (a2 > v_rbx) { a2 = v_rbx; }
    a1 = (result) - (a2);
    a2 = (a2) + (a2);
    a3 = 0;
    a4 = 0;
    result = PspReturnResourceQuota((unsigned int)((unsigned int)(v_r15)), v_r12, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B8371E(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    uint64_t v_stack_p20;

    if (Arg2 > local_rbx) { Arg2 = local_rbx; }
    Arg1 = (result) - (Arg2);
    Arg2 = (Arg2) + (Arg2);
    Arg3 = 0;
    Arg4 = 0;
    result = PspReturnResourceQuota((uint32_t)((uint32_t)(local_r15)), local_r12, Arg3, Arg4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=poolcode&rva=0x00B8371E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
