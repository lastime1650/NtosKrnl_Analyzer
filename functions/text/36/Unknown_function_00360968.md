# sub_00360968

- RVA: `0x00360968`–`0x003612E1` (길이 `2,425` bytes)
- VA: `0x0000000140360968`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079CA4`
- 디코드: `587`개 명령, `2,425/2,425` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x003609B2` → [PspReturnResourceQuota](../38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x003609CB` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00360AC3` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00360AFF` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00360B12` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00360B8E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00360BBD` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00360C11` → [PspReturnResourceQuota](../38/PspReturnResourceQuota_function_0038FFC4.md) (function, `0x0038FFC4`)
- `0x00360C79` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x00360CB1` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)
- `0x00360CDE` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00360D01` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00360D44` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00360D62` → [ExpCheckForLookaside](../4A/ExpCheckForLookaside_function_004A52DC.md) (function, `0x004A52DC`)
- `0x00360D77` → [KeCheckForTimer](../4D/KeCheckForTimer_function_004D870C.md) (function, `0x004D870C`)
- `0x00360D8C` → [ExpCheckForResource](../49/ExpCheckForResource_function_0049CA24.md) (function, `0x0049CA24`)
- `0x00360DA5` → [ExpCheckForWorker](../4E/ExpCheckForWorker_function_004EC8FC.md) (function, `0x004EC8FC`)
- `0x00360DCC` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00360DFF` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (function, `0x00B84080`)
- `0x00360E2F` → [EtwTracePool](../2E/EtwTracePool_function_002ECEEC.md) (function, `0x002ECEEC`)
- `0x00360EB4` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (function, `0x00B84080`)
- `0x00360EE0` → [EtwTracePool](../2E/EtwTracePool_function_002ECEEC.md) (function, `0x002ECEEC`)
- `0x00360EED` → [ExIsSpecialPoolAddress](../49/ExIsSpecialPoolAddress_function_0049C410.md) (function, `0x0049C410`)
- `0x00360F0C` → [RtlpHpLargeFree](../2E/RtlpHpLargeFree_function_002EC89C.md) (function, `0x002EC89C`)
- `0x00360FDF` → [RtlpHpLfhThreadDataInitializeSet](../4F/RtlpHpLfhThreadDataInitializeSet_function_004F6334.md) (function, `0x004F6334`)
- `0x00361026` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00361030` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x0036103E` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x003610A1` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003610C4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003610D4` → [MmDeterminePoolType](../35/MmDeterminePoolType_function_0035F5B0.md) (function, `0x0035F5B0`)
- `0x00361118` → [ExpFreePoolChecks](../35/ExpFreePoolChecks_function_0035F4F0.md) (function, `0x0035F4F0`)
- `0x0036114C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00361183` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003611B2` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003611FF` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00361224` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0036128C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003612B2` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003612D4` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x003609BC` → RVA `0x00EFA7C0` (`.data`; read)
- `0x003609DE` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x003609F2` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00360A55` → RVA `0x00E27F80` (`.data`; read)
- `0x00360AAD` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x00360B1F` → RVA `0x00EFED50` (`.data`; read)
- `0x00360C98` → RVA `0x00F0DE58` (`.data`; read)
- `0x00360CAA` → RVA `0x00EFACF8` (`.data`; read)
- `0x00360D32` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x00360D67` → RVA `0x00FC6BD0` (`ALMOSTRO`; read)
- `0x003610CA` → RVA `0x00EFED20` (`.data`; read/write)
- `0x003610E6` → RVA `0x00FCEC68` (`ALMOSTRO`; read)
- `0x00361242` → RVA `0x00FC6ED8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00360DFF` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (`.text` → `POOLCODE`)
  - `0x00360EB4` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **47**
  - `0x0036097C` → [sub_003602E3 + 0x27B](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00360992` → [sub_003602E3 + 0x27B](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x003609A3` → [sub_003602E3 + 0x27B](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x003609B7` → [sub_003602E3 + 0x27B](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x003609C2` → [sub_003602E3 + 0x5D3](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x003609D0` → [sub_0035FB85 + 0x241](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360AD2` → [sub_003602E3 + 0x3B0](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00360B09` → [sub_0035FB85 + 0x311](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360B5D` → [sub_0035FB85 + 0x2E9](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360B6C` → [sub_0035FB85 + 0x2E9](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360C22` → [sub_0035FB85 + 0x389](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360C38` → [sub_003602E3 + 0x289](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00360C40` → [sub_0035FB85 + 0x335](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360C85` → [sub_0035FB85 + 0x33C](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360C8B` → [sub_0035FB85 + 0x738](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360CA0` → [sub_003602E3 + 0x372](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00360CB6` → [sub_003602E3 + 0x384](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00360D99` → [sub_0035FB85 + 0x13F](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360DAA` → [sub_0035FB85 + 0x13F](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360E06` → [sub_0035FB85 + 0x181](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360E34` → [sub_0035FB85 + 0x181](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360E46` → [sub_0035FB85 + 0x2E0](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360E70` → [sub_0035FB85 + 0x2E0](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360E79` → [sub_0035FB85 + 0x2E0](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360E96` → [sub_003602E3 + 0xCF](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00360EBB` → [sub_0035FB85 + 0x6B8](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360EE5` → [sub_0035FB85 + 0x6B8](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360EF4` → [sub_003602E3 + 0x30F](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00360F01` → [sub_003602E3 + 0x14F](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00360F11` → [sub_0035FB85 + 0x738](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360F43` → [sub_0035FB85 + 0x2E0](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360F52` → [sub_0035FB85 + 0x2E0](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360F7E` → [sub_0035FB85 + 0x2E9](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360F8C` → [sub_0035FB85 + 0x2E9](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360F95` → [sub_0035FB85 + 0x4A4](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360FCD` → [sub_003602E3 + 0x54A](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00360FD7` → [sub_0035FB85 + 0x738](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00360FE4` → [sub_0035FB85 + 0x49A](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00361035` → [sub_003602E3 + 0x305](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00361043` → [sub_003602E3 + 0x3B0](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x0036107E` → [sub_0035FB85 + 0x673](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x003611BA` → [sub_003602E3 + 0x176](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x003611C6` → [sub_003602E3 + 0x17C](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x003611CD` → [sub_003602E3 + 0x54](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x003611D9` → [sub_003602E3 + 0x5A](Unknown_function_003602E3.md) (`tail-transfer`)
  - `0x00361252` → [sub_0035FB85 + 0x31E](../35/Unknown_function_0035FB85.md) (`tail-transfer`)
  - `0x00361260` → [sub_0035FB85 + 0x31E](../35/Unknown_function_0035FB85.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00360968  48 3B D3                        cmp rdx, rbx
0036096B  48 8B C8                        mov rcx, rax
0036096E  48 0F 47 D3                     cmova rdx, rbx
00360972  48 2B CA                        sub rcx, rdx
00360975  F0 49 0F B1 4C 24 40            lock cmpxchg qword ptr [r12 + 0x40], rcx
0036097C  0F 85 DC FB FF FF               jne 0x14036055e
00360982  48 8B C2                        mov rax, rdx
00360985  F0 49 0F C1 44 24 48            lock xadd qword ptr [r12 + 0x48], rax
0036098C  48 03 D0                        add rdx, rax
0036098F  49 3B 10                        cmp rdx, qword ptr [r8]
00360992  0F 86 C6 FB FF FF               jbe 0x14036055e
00360998  45 33 C0                        xor r8d, r8d
0036099B  4D 87 44 24 48                  xchg qword ptr [r12 + 0x48], r8
003609A0  4D 85 C0                        test r8, r8
003609A3  0F 84 B5 FB FF FF               je 0x14036055e
003609A9  45 33 C9                        xor r9d, r9d
003609AC  49 8B D4                        mov rdx, r12
003609AF  41 8B CF                        mov ecx, r15d
003609B2  E8 0D F6 02 00                  call 0x14038ffc4
003609B7  E9 A2 FB FF FF                  jmp 0x14036055e
003609BC  8B 05 FE 9D B9 00               mov eax, dword ptr [rip + 0xb99dfe]
003609C2  E9 EF FE FF FF                  jmp 0x1403608b6
003609C7  48 8D 4D B7                     lea rcx, [rbp - 0x49]
003609CB  E8 E0 74 EF FF                  call 0x140257eb0
003609D0  E9 F1 F3 FF FF                  jmp 0x14035fdc6
003609D5  49 8B CE                        mov rcx, r14
003609D8  81 E1 00 01 00 00               and ecx, 0x100
003609DE  48 3B 3D CB 60 C6 00            cmp rdi, qword ptr [rip + 0xc660cb]
003609E5  0F 84 C2 00 00 00               je 0x140360aad
003609EB  4C 8B AF F8 02 00 00            mov r13, qword ptr [rdi + 0x2f8]
003609F2  4C 8D 0D 07 F6 C9 FF            lea r9, [rip - 0x3609f9]
003609F9  33 C0                           xor eax, eax
003609FB  48 85 C9                        test rcx, rcx
003609FE  0F 95 C0                        setne al
00360A01  44 8B E0                        mov r12d, eax
00360A04  43 0F B6 84 E1 50 73 FC 00      movzx eax, byte ptr [r9 + r12*8 + 0xfc7350]
00360A0D  88 45 7F                        mov byte ptr [rbp + 0x7f], al
00360A10  41 8B C4                        mov eax, r12d
00360A13  48 C1 E0 07                     shl rax, 7
00360A17  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00360A1B  4E 8D 34 28                     lea r14, [rax + r13]
00360A1F  41 0F 0D 0E                     prefetchw byte ptr [r14]
00360A23  4D 8B 3E                        mov r15, qword ptr [r14]
00360A26  49 8B 46 40                     mov rax, qword ptr [r14 + 0x40]
00360A2A  49 83 7E 50 00                  cmp qword ptr [r14 + 0x50], 0
00360A2F  74 20                           je 0x140360a51
00360A31  4D 6B C4 38                     imul r8, r12, 0x38
00360A35  49 3B C7                        cmp rax, r15
00360A38  76 17                           jbe 0x140360a51
00360A3A  4B 8B 94 08 48 66 F0 00         mov rdx, qword ptr [r8 + r9 + 0xf06648]
00360A42  48 8B C8                        mov rcx, rax
00360A45  49 2B CF                        sub rcx, r15
00360A48  48 3B CA                        cmp rcx, rdx
00360A4B  0F 87 72 01 00 00               ja 0x140360bc3
00360A51  4C 8B 45 8F                     mov r8, qword ptr [rbp - 0x71]
00360A55  4C 8D 15 24 75 AC 00            lea r10, [rip + 0xac7524]
00360A5C  4C 8B 5D AF                     mov r11, qword ptr [rbp - 0x51]
00360A60  4D 3B C7                        cmp r8, r15
00360A63  4D 8B CF                        mov r9, r15
00360A66  49 8B CF                        mov rcx, r15
00360A69  49 8B C7                        mov rax, r15
00360A6C  4D 0F 42 C8                     cmovb r9, r8
00360A70  49 2B C8                        sub rcx, r8
00360A73  33 D2                           xor edx, edx
00360A75  4D 3B C7                        cmp r8, r15
00360A78  48 0F 42 D1                     cmovb rdx, rcx
00360A7C  F0 49 0F B1 16                  lock cmpxchg qword ptr [r14], rdx
00360A81  4C 8B F8                        mov r15, rax
00360A84  75 DA                           jne 0x140360a60
00360A86  4D 2B C1                        sub r8, r9
00360A89  0F 85 55 02 00 00               jne 0x140360ce4
00360A8F  F6 45 7F 04                     test byte ptr [rbp + 0x7f], 4
00360A93  74 10                           je 0x140360aa5
00360A95  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00360A99  48 F7 D8                        neg rax
00360A9C  F0 4A 01 84 E7 00 02 00 00      lock add qword ptr [rdi + r12*8 + 0x200], rax
00360AA5  4C 8B 65 67                     mov r12, qword ptr [rbp + 0x67]
00360AA9  4C 8B 6D 6F                     mov r13, qword ptr [rbp + 0x6f]
00360AAD  83 3D 5C 45 C6 00 00            cmp dword ptr [rip + 0xc6455c], 0
00360AB4  74 12                           je 0x140360ac8
00360AB6  33 D2                           xor edx, edx
00360AB8  48 8D 4F D0                     lea rcx, [rdi - 0x30]
00360ABC  44 8B CB                        mov r9d, ebx
00360ABF  44 8D 42 01                     lea r8d, [rdx + 1]
00360AC3  E8 1C FF EA FF                  call 0x1402109e4
00360AC8  F0 48 0F C1 77 D0               lock xadd qword ptr [rdi - 0x30], rsi
00360ACE  48 83 EE 01                     sub rsi, 1
00360AD2  0F 8F BB FB FF FF               jg 0x140360693
00360AD8  48 8B 4F D8                     mov rcx, qword ptr [rdi - 0x28]
00360ADC  48 85 C9                        test rcx, rcx
00360ADF  0F 85 04 05 00 00               jne 0x140360fe9
00360AE5  48 85 F6                        test rsi, rsi
00360AE8  0F 89 4C 05 00 00               jns 0x14036103a
00360AEE  33 D2                           xor edx, edx
00360AF0  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00360AF5  44 8D 49 04                     lea r9d, [rcx + 4]
00360AF9  4C 8B C7                        mov r8, rdi
00360AFC  8D 4A 18                        lea ecx, [rdx + 0x18]
00360AFF  E8 5C CB 19 00                  call 0x1404fd660
00360B04  CC                              int3
00360B05  4C 8B 7D 8F                     mov r15, qword ptr [rbp - 0x71]
00360B09  E9 88 F3 FF FF                  jmp 0x14035fe96
00360B0E  48 8D 4D B7                     lea rcx, [rbp - 0x49]
00360B12  E8 C9 21 FE FF                  call 0x140342ce0
00360B17  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
00360B1F  44 8B 05 2A E2 B9 00            mov r8d, dword ptr [rip + 0xb9e22a]
00360B26  8B C8                           mov ecx, eax
00360B28  41 FF C8                        dec r8d
00360B2B  48 8D 05 CE F4 C9 FF            lea rax, [rip - 0x360b32]
00360B32  48 8B 94 C8 20 AD EF 00         mov rdx, qword ptr [rax + rcx*8 + 0xefad20]
00360B3A  4B 8D 0C 80                     lea rcx, [r8 + r8*4]
00360B3E  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00360B42  48 C1 E1 04                     shl rcx, 4
00360B46  48 F7 D8                        neg rax
00360B49  48 03 CA                        add rcx, rdx
00360B4C  49 0F BA E7 08                  bt r15, 8
00360B51  72 0F                           jb 0x140360b62
00360B53  F0 48 FF 41 18                  lock inc qword ptr [rcx + 0x18]
00360B58  F0 48 01 41 08                  lock add qword ptr [rcx + 8], rax
00360B5D  E9 0C F3 FF FF                  jmp 0x14035fe6e
00360B62  F0 48 FF 41 30                  lock inc qword ptr [rcx + 0x30]
00360B67  F0 48 01 41 20                  lock add qword ptr [rcx + 0x20], rax
00360B6C  E9 FD F2 FF FF                  jmp 0x14035fe6e
00360B71  4C 39 55 7F                     cmp qword ptr [rbp + 0x7f], r10
00360B75  0F 85 AC 00 00 00               jne 0x140360c27
00360B7B  4D 8B C8                        mov r9, r8
00360B7E  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00360B83  4D 8B C7                        mov r8, r15
00360B86  48 8B D7                        mov rdx, rdi
00360B89  B9 21 00 00 00                  mov ecx, 0x21
00360B8E  E8 CD CA 19 00                  call 0x1404fd660
00360B93  CC                              int3
00360B94  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00360B9E  48 3B F0                        cmp rsi, rax
00360BA1  0F 83 37 06 00 00               jae 0x1403611de
00360BA7  BA 02 00 00 00                  mov edx, 2
00360BAC  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00360BB1  4C 8B CE                        mov r9, rsi
00360BB4  B9 F1 01 00 00                  mov ecx, 0x1f1
00360BB9  44 8D 42 FF                     lea r8d, [rdx - 1]
00360BBD  E8 9E CA 19 00                  call 0x1404fd660
00360BC2  CC                              int3
00360BC3  48 3B 55 8F                     cmp rdx, qword ptr [rbp - 0x71]
00360BC7  48 8B C8                        mov rcx, rax
00360BCA  48 0F 47 55 8F                  cmova rdx, qword ptr [rbp - 0x71]
00360BCF  48 2B CA                        sub rcx, rdx
00360BD2  F0 49 0F B1 4E 40               lock cmpxchg qword ptr [r14 + 0x40], rcx
00360BD8  0F 85 73 FE FF FF               jne 0x140360a51
00360BDE  48 8B C2                        mov rax, rdx
00360BE1  F0 49 0F C1 46 48               lock xadd qword ptr [r14 + 0x48], rax
00360BE7  48 03 D0                        add rdx, rax
00360BEA  4B 3B 94 08 48 66 F0 00         cmp rdx, qword ptr [r8 + r9 + 0xf06648]
00360BF2  0F 86 59 FE FF FF               jbe 0x140360a51
00360BF8  45 33 C0                        xor r8d, r8d
00360BFB  4D 87 46 48                     xchg qword ptr [r14 + 0x48], r8
00360BFF  4D 85 C0                        test r8, r8
00360C02  0F 84 49 FE FF FF               je 0x140360a51
00360C08  45 33 C9                        xor r9d, r9d
00360C0B  49 8B D6                        mov rdx, r14
00360C0E  41 8B CC                        mov ecx, r12d
00360C11  E8 AE F3 02 00                  call 0x14038ffc4
00360C16  E9 36 FE FF FF                  jmp 0x140360a51
00360C1B  48 81 C3 C0 00 00 00            add rbx, 0xc0
00360C22  E9 E7 F2 FF FF                  jmp 0x14035ff0e
00360C27  4C 89 55 7F                     mov qword ptr [rbp + 0x7f], r10
00360C2B  4F 8D 24 13                     lea r12, [r11 + r10]
00360C2F  41 0F 0D 0C 24                  prefetchw byte ptr [r12]
00360C34  4D 8B 34 24                     mov r14, qword ptr [r12]
00360C38  E9 2F F9 FF FF                  jmp 0x14036056c
00360C3D  48 85 D2                        test rdx, rdx
00360C40  0F 84 74 F2 FF FF               je 0x14035feba
00360C46  41 8D 47 0F                     lea eax, [r15 + 0xf]
00360C4A  C1 E8 04                        shr eax, 4
00360C4D  4C 8D 3D AC F3 C9 FF            lea r15, [rip - 0x360c54]
00360C54  42 0F B6 8C 38 80 0B 01 00      movzx ecx, byte ptr [rax + r15 + 0x10b80]
00360C5D  83 C1 DF                        add ecx, -0x21
00360C60  48 FF C1                        inc rcx
00360C63  48 C1 E1 06                     shl rcx, 6
00360C67  48 03 CA                        add rcx, rdx
00360C6A  FF 41 1C                        inc dword ptr [rcx + 0x1c]
00360C6D  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
00360C71  66 39 01                        cmp word ptr [rcx], ax
00360C74  73 1A                           jae 0x140360c90
00360C76  48 8B D6                        mov rdx, rsi
00360C79  E8 32 99 35 00                  call 0x1406ba5b0
00360C7E  B8 01 00 00 00                  mov eax, 1
00360C83  85 C0                           test eax, eax
00360C85  0F 84 36 F2 FF FF               je 0x14035fec1
00360C8B  E9 2D F6 FF FF                  jmp 0x1403602bd
00360C90  FF 41 20                        inc dword ptr [rcx + 0x20]
00360C93  41 8B C6                        mov eax, r14d
00360C96  EB EB                           jmp 0x140360c83
00360C98  8B 05 BA D1 BA 00               mov eax, dword ptr [rip + 0xbad1ba]
00360C9E  85 C0                           test eax, eax
00360CA0  0F 85 AF F9 FF FF               jne 0x140360655
00360CA6  48 8B 55 5F                     mov rdx, qword ptr [rbp + 0x5f]
00360CAA  48 8D 0D 47 A0 B9 00            lea rcx, [rip + 0xb9a047]
00360CB1  E8 92 02 F9 FF                  call 0x1402f0f48
00360CB6  E9 AC F9 FF FF                  jmp 0x140360667
00360CBB  48 8B 4F D8                     mov rcx, qword ptr [rdi - 0x28]
00360CBF  48 85 C9                        test rcx, rcx
00360CC2  75 43                           jne 0x140360d07
00360CC4  48 85 F6                        test rsi, rsi
00360CC7  0F 89 5F 03 00 00               jns 0x14036102c
00360CCD  33 D2                           xor edx, edx
00360CCF  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00360CD4  44 8D 49 04                     lea r9d, [rcx + 4]
00360CD8  4C 8B C7                        mov r8, rdi
00360CDB  8D 4A 18                        lea ecx, [rdx + 0x18]
00360CDE  E8 7D C9 19 00                  call 0x1404fd660
00360CE3  CC                              int3
00360CE4  4D 3B EA                        cmp r13, r10
00360CE7  0F 85 E5 00 00 00               jne 0x140360dd2
00360CED  4C 8B 4D 8F                     mov r9, qword ptr [rbp - 0x71]
00360CF1  48 8B D7                        mov rdx, rdi
00360CF4  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00360CF9  B9 21 00 00 00                  mov ecx, 0x21
00360CFE  4D 8B C4                        mov r8, r12
00360D01  E8 5A C9 19 00                  call 0x1404fd660
00360D06  CC                              int3
00360D07  41 B9 03 00 00 00               mov r9d, 3
00360D0D  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00360D12  4C 8D 1D E7 F2 C9 FF            lea r11, [rip - 0x360d19]
00360D19  4C 8B C7                        mov r8, rdi
00360D1C  48 8D 47 D0                     lea rax, [rdi - 0x30]
00360D20  48 C1 E8 08                     shr rax, 8
00360D24  0F B6 D0                        movzx edx, al
00360D27  41 8D 49 15                     lea ecx, [r9 + 0x15]
00360D2B  0F B6 47 E8                     movzx eax, byte ptr [rdi - 0x18]
00360D2F  48 33 D0                        xor rdx, rax
00360D32  0F B6 05 13 61 C6 00            movzx eax, byte ptr [rip + 0xc66113]
00360D39  48 33 D0                        xor rdx, rax
00360D3C  49 8B 94 D3 00 78 FC 00         mov rdx, qword ptr [r11 + rdx*8 + 0xfc7800]
00360D44  E8 17 C9 19 00                  call 0x1404fd660
00360D49  CC                              int3
00360D4A  41 F6 C7 C0                     test r15b, 0xc0
00360D4E  0F 95 C1                        setne cl
00360D51  0F BA E0 09                     bt eax, 9
00360D55  0F 92 C0                        setb al
00360D58  84 C8                           test al, cl
00360D5A  74 0B                           je 0x140360d67
00360D5C  49 8B D6                        mov rdx, r14
00360D5F  48 8B CE                        mov rcx, rsi
00360D62  E8 75 45 14 00                  call 0x1404a52dc
00360D67  8B 05 63 5E C6 00               mov eax, dword ptr [rip + 0xc65e63]
00360D6D  A8 01                           test al, 1
00360D6F  74 0B                           je 0x140360d7c
00360D71  49 8B D6                        mov rdx, r14
00360D74  48 8B CE                        mov rcx, rsi
00360D77  E8 90 79 17 00                  call 0x1404d870c
00360D7C  8B 05 4E 5E C6 00               mov eax, dword ptr [rip + 0xc65e4e]
00360D82  A8 04                           test al, 4
00360D84  74 0B                           je 0x140360d91
00360D86  49 8B D6                        mov rdx, r14
00360D89  48 8B CE                        mov rcx, rsi
00360D8C  E8 93 BC 13 00                  call 0x14049ca24
00360D91  8B 05 39 5E C6 00               mov eax, dword ptr [rip + 0xc65e39]
00360D97  A8 02                           test al, 2
00360D99  0F 84 25 EF FF FF               je 0x14035fcc4
00360D9F  49 8B D6                        mov rdx, r14
00360DA2  48 8B CE                        mov rcx, rsi
00360DA5  E8 52 BB 18 00                  call 0x1404ec8fc
00360DAA  E9 15 EF FF FF                  jmp 0x14035fcc4
00360DAF  48 85 D2                        test rdx, rdx
00360DB2  74 03                           je 0x140360db7
00360DB4  44 8B FE                        mov r15d, esi
00360DB7  45 8B CF                        mov r9d, r15d
00360DBA  4D 8B C4                        mov r8, r12
00360DBD  BA 0D 00 00 00                  mov edx, 0xd
00360DC2  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00360DC7  B9 C2 00 00 00                  mov ecx, 0xc2
00360DCC  E8 8F C8 19 00                  call 0x1404fd660
00360DD1  CC                              int3
00360DD2  4D 8B EA                        mov r13, r10
00360DD5  4F 8D 34 13                     lea r14, [r11 + r10]
00360DD9  41 0F 0D 0E                     prefetchw byte ptr [r14]
00360DDD  4D 8B 3E                        mov r15, qword ptr [r14]
00360DE0  E9 7B FC FF FF                  jmp 0x140360a60
00360DE5  41 8B D7                        mov edx, r15d
00360DE8  48 8D 45 87                     lea rax, [rbp - 0x79]
00360DEC  83 E2 10                        and edx, 0x10
00360DEF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00360DF4  4C 8D 4D 6F                     lea r9, [rbp + 0x6f]
00360DF8  49 8B CF                        mov rcx, r15
00360DFB  4C 8D 45 A3                     lea r8, [rbp - 0x5d]
00360DFF  E8 7C 32 82 00                  call 0x140b84080
00360E04  85 C0                           test eax, eax
00360E06  0F 88 FA EE FF FF               js 0x14035fd06
00360E0C  8B 55 A3                        mov edx, dword ptr [rbp - 0x5d]
00360E0F  44 38 75 6F                     cmp byte ptr [rbp + 0x6f], r14b
00360E13  74 06                           je 0x140360e1b
00360E15  83 CA 08                        or edx, 8
00360E18  89 55 A3                        mov dword ptr [rbp - 0x5d], edx
00360E1B  48 8B 45 8F                     mov rax, qword ptr [rbp - 0x71]
00360E1F  B9 22 0E 00 00                  mov ecx, 0xe22
00360E24  4C 8B CF                        mov r9, rdi
00360E27  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00360E2C  44 8B C3                        mov r8d, ebx
00360E2F  E8 B8 C0 F8 FF                  call 0x1402eceec
00360E34  E9 CD EE FF FF                  jmp 0x14035fd06
00360E39  49 63 C1                        movsxd rax, r9d
00360E3C  41 F6 44 C0 38 01               test byte ptr [r8 + rax*8 + 0x38], 1
00360E42  4D 8D 1C C0                     lea r11, [r8 + rax*8]
00360E46  0F 85 19 F0 FF FF               jne 0x14035fe65
00360E4C  49 8B 43 38                     mov rax, qword ptr [r11 + 0x38]
00360E50  4E 8D 14 95 3F 00 00 00         lea r10, [r10*4 + 0x3f]
00360E58  49 83 E2 C0                     and r10, 0xffffffffffffffc0
00360E5C  BB 80 00 00 00                  mov ebx, 0x80
00360E61  49 83 FA 40                     cmp r10, 0x40
00360E65  4C 0F 44 D3                     cmove r10, rbx
00360E69  49 8D 1C 0A                     lea rbx, [r10 + rcx]
00360E6D  48 3B C8                        cmp rcx, rax
00360E70  0F 8D EF EF FF FF               jge 0x14035fe65
00360E76  48 3B D8                        cmp rbx, rax
00360E79  0F 8D E6 EF FF FF               jge 0x14035fe65
00360E7F  F0 49 0F B1 5B 38               lock cmpxchg qword ptr [r11 + 0x38], rbx
00360E85  0F 84 8B 00 00 00               je 0x140360f16
00360E8B  48 8B 0A                        mov rcx, qword ptr [rdx]
00360E8E  EB D9                           jmp 0x140360e69
00360E90  41 8B D3                        mov edx, r11d
00360E93  45 8B D3                        mov r10d, r11d
00360E96  E9 17 F5 FF FF                  jmp 0x1403603b2
00360E9B  8B D7                           mov edx, edi
00360E9D  48 8D 45 77                     lea rax, [rbp + 0x77]
00360EA1  83 E2 10                        and edx, 0x10
00360EA4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00360EA9  4C 8D 4D 67                     lea r9, [rbp + 0x67]
00360EAD  48 8B CF                        mov rcx, rdi
00360EB0  4C 8D 45 9F                     lea r8, [rbp - 0x61]
00360EB4  E8 C7 31 82 00                  call 0x140b84080
00360EB9  85 C0                           test eax, eax
00360EBB  0F 88 7C F3 FF FF               js 0x14036023d
00360EC1  8B 55 9F                        mov edx, dword ptr [rbp - 0x61]
00360EC4  44 38 7D 67                     cmp byte ptr [rbp + 0x67], r15b
00360EC8  74 06                           je 0x140360ed0
00360ECA  83 CA 08                        or edx, 8
00360ECD  89 55 9F                        mov dword ptr [rbp - 0x61], edx
00360ED0  B9 22 0E 00 00                  mov ecx, 0xe22
00360ED5  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00360EDA  4D 8B CC                        mov r9, r12
00360EDD  44 8B C6                        mov r8d, esi
00360EE0  E8 07 C0 F8 FF                  call 0x1402eceec
00360EE5  E9 53 F3 FF FF                  jmp 0x14036023d
00360EEA  49 8B CC                        mov rcx, r12
00360EED  E8 1E B5 13 00                  call 0x14049c410
00360EF2  85 C0                           test eax, eax
00360EF4  0F 85 F8 F6 FF FF               jne 0x1403605f2
00360EFA  4C 8D 05 FF F0 C9 FF            lea r8, [rip - 0x360f01]
00360F01  E9 2C F5 FF FF                  jmp 0x140360432
00360F06  48 8B D6                        mov rdx, rsi
00360F09  49 8B CD                        mov rcx, r13
00360F0C  E8 8B B9 F8 FF                  call 0x1402ec89c
00360F11  E9 A7 F3 FF FF                  jmp 0x1403602bd
00360F16  49 8B 50 48                     mov rdx, qword ptr [r8 + 0x48]
00360F1A  48 2B C3                        sub rax, rbx
00360F1D  4C 8B D0                        mov r10, rax
00360F20  49 F7 DA                        neg r10
00360F23  48 85 C0                        test rax, rax
00360F26  4C 0F 49 D0                     cmovns r10, rax
00360F2A  49 63 C1                        movsxd rax, r9d
00360F2D  48 8D 0C 40                     lea rcx, [rax + rax*2]
00360F31  48 8B 44 CA 10                  mov rax, qword ptr [rdx + rcx*8 + 0x10]
00360F36  4C 8B 44 CA 18                  mov r8, qword ptr [rdx + rcx*8 + 0x18]
00360F3B  48 85 C0                        test rax, rax
00360F3E  75 09                           jne 0x140360f49
00360F40  4D 85 C0                        test r8, r8
00360F43  0F 84 1C EF FF FF               je 0x14035fe65
00360F49  49 F7 DA                        neg r10
00360F4C  F0 4C 01 54 CA 20               lock add qword ptr [rdx + rcx*8 + 0x20], r10
00360F52  E9 0E EF FF FF                  jmp 0x14035fe65
00360F57  49 8B 50 48                     mov rdx, qword ptr [r8 + 0x48]
00360F5B  48 2B C3                        sub rax, rbx
00360F5E  48 8B C8                        mov rcx, rax
00360F61  48 F7 D9                        neg rcx
00360F64  48 85 C0                        test rax, rax
00360F67  48 0F 49 C8                     cmovns rcx, rax
00360F6B  49 03 D2                        add rdx, r10
00360F6E  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
00360F72  4C 8B 42 18                     mov r8, qword ptr [rdx + 0x18]
00360F76  48 85 C0                        test rax, rax
00360F79  75 09                           jne 0x140360f84
00360F7B  4D 85 C0                        test r8, r8
00360F7E  0F 84 EA EE FF FF               je 0x14035fe6e
00360F84  48 F7 D9                        neg rcx
00360F87  F0 48 01 4A 20                  lock add qword ptr [rdx + 0x20], rcx
00360F8C  E9 DD EE FF FF                  jmp 0x14035fe6e
00360F91  80 7F 16 01                     cmp byte ptr [rdi + 0x16], 1
00360F95  0F 84 8E F0 FF FF               je 0x140360029
00360F9B  8B CB                           mov ecx, ebx
00360F9D  48 8B C3                        mov rax, rbx
00360FA0  48 C1 E8 06                     shr rax, 6
00360FA4  83 E1 3F                        and ecx, 0x3f
00360FA7  48 8B 54 C7 40                  mov rdx, qword ptr [rdi + rax*8 + 0x40]
00360FAC  49 C7 C0 FE FF FF FF            mov r8, 0xfffffffffffffffe
00360FB3  49 D3 C0                        rol r8, cl
00360FB6  4C 8B CB                        mov r9, rbx
00360FB9  48 8D 0C C7                     lea rcx, [rdi + rax*8]
00360FBD  49 8B C0                        mov rax, r8
00360FC0  48 23 C2                        and rax, rdx
00360FC3  49 F7 D0                        not r8
00360FC6  48 89 41 40                     mov qword ptr [rcx + 0x40], rax
00360FCA  4C 85 C2                        test rdx, r8
00360FCD  0F 84 5A F8 FF FF               je 0x14036082d
00360FD3  66 FF 47 20                     inc word ptr [rdi + 0x20]
00360FD7  E9 E1 F2 FF FF                  jmp 0x1403602bd
00360FDC  48 8B CE                        mov rcx, rsi
00360FDF  E8 50 53 19 00                  call 0x1404f6334
00360FE4  E9 36 F0 FF FF                  jmp 0x14036001f
00360FE9  41 B9 03 00 00 00               mov r9d, 3
00360FEF  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00360FF4  4C 8D 1D 05 F0 C9 FF            lea r11, [rip - 0x360ffb]
00360FFB  4C 8B C7                        mov r8, rdi
00360FFE  48 8D 47 D0                     lea rax, [rdi - 0x30]
00361002  48 C1 E8 08                     shr rax, 8
00361006  0F B6 D0                        movzx edx, al
00361009  41 8D 49 15                     lea ecx, [r9 + 0x15]
0036100D  0F B6 47 E8                     movzx eax, byte ptr [rdi - 0x18]
00361011  48 33 D0                        xor rdx, rax
00361014  0F B6 05 31 5E C6 00            movzx eax, byte ptr [rip + 0xc65e31]
0036101B  48 33 D0                        xor rdx, rax
0036101E  49 8B 94 D3 00 78 FC 00         mov rdx, qword ptr [r11 + rdx*8 + 0xfc7800]
00361026  E8 35 C6 19 00                  call 0x1404fd660
0036102B  CC                              int3
0036102C  48 8D 4F D0                     lea rcx, [rdi - 0x30]
00361030  E8 5F 13 04 00                  call 0x1403a2394
00361035  E9 AE F5 FF FF                  jmp 0x1403605e8
0036103A  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0036103E  E8 51 13 04 00                  call 0x1403a2394
00361043  E9 4B F6 FF FF                  jmp 0x140360693
00361048  8B 03                           mov eax, dword ptr [rbx]
0036104A  4C 8D 43 10                     lea r8, [rbx + 0x10]
0036104E  8B C8                           mov ecx, eax
00361050  44 8B D0                        mov r10d, eax
00361053  C1 E9 10                        shr ecx, 0x10
00361056  41 81 E2 00 40 00 00            and r10d, 0x4000
0036105D  74 04                           je 0x140361063
0036105F  4C 8D 43 18                     lea r8, [rbx + 0x18]
00361063  4D 3B C4                        cmp r8, r12
00361066  72 3F                           jb 0x1403610a7
00361068  4D 8D 8C 24 FF 0F 00 00         lea r9, [r12 + 0xfff]
00361070  49 81 E1 00 F0 FF FF            and r9, 0xfffffffffffff000
00361077  4E 8D 04 22                     lea r8, [rdx + r12]
0036107B  4D 3B C1                        cmp r8, r9
0036107E  0F 83 74 F1 FF FF               jae 0x1403601f8
00361084  41 38 08                        cmp byte ptr [r8], cl
00361087  0F 84 37 02 00 00               je 0x1403612c4
0036108D  4C 8B C8                        mov r9, rax
00361090  48 C7 44 24 20 24 00 00 00      mov qword ptr [rsp + 0x20], 0x24
00361099  49 8B D4                        mov rdx, r12
0036109C  B9 C1 00 00 00                  mov ecx, 0xc1
003610A1  E8 BA C5 19 00                  call 0x1404fd660
003610A6  CC                              int3
003610A7  41 38 08                        cmp byte ptr [r8], cl
003610AA  0F 84 0C 02 00 00               je 0x1403612bc
003610B0  4C 8B C8                        mov r9, rax
003610B3  48 C7 44 24 20 23 00 00 00      mov qword ptr [rsp + 0x20], 0x23
003610BC  49 8B D4                        mov rdx, r12
003610BF  B9 C1 00 00 00                  mov ecx, 0xc1
003610C4  E8 97 C5 19 00                  call 0x1404fd660
003610C9  CC                              int3
003610CA  F0 FF 0D 4F DC B9 00            lock dec dword ptr [rip + 0xb9dc4f]
003610D1  49 8B CC                        mov rcx, r12
003610D4  E8 D7 E4 FF FF                  call 0x14035f5b0
003610D9  49 8B DC                        mov rbx, r12
003610DC  48 8B F8                        mov rdi, rax
003610DF  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
003610E6  44 38 3D 7B DB C6 00            cmp byte ptr [rip + 0xc6db7b], r15b
003610ED  0F 85 96 00 00 00               jne 0x140361189
003610F3  8B 53 04                        mov edx, dword ptr [rbx + 4]
003610F6  41 8B C4                        mov eax, r12d
003610F9  25 FF 0F 00 00                  and eax, 0xfff
003610FE  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00361103  B9 00 10 00 00                  mov ecx, 0x1000
00361108  41 B9 80 00 00 00               mov r9d, 0x80
0036110E  2B C8                           sub ecx, eax
00361110  8B F1                           mov esi, ecx
00361112  44 8B C1                        mov r8d, ecx
00361115  49 8B CC                        mov rcx, r12
00361118  E8 D3 E3 FF FF                  call 0x14035f4f0
0036111D  4C 8B DF                        mov r11, rdi
00361120  41 81 E3 00 01 00 00            and r11d, 0x100
00361127  44 0F 20 C1                     mov rcx, cr8
0036112B  0F 94 C0                        sete al
0036112E  FE C0                           inc al
00361130  3A C8                           cmp cl, al
00361132  76 1E                           jbe 0x140361152
00361134  0F B6 D1                        movzx edx, cl
00361137  4D 8B CC                        mov r9, r12
0036113A  B9 C1 00 00 00                  mov ecx, 0xc1
0036113F  48 C7 44 24 20 31 00 00 00      mov qword ptr [rsp + 0x20], 0x31
00361148  44 8D 41 3F                     lea r8d, [rcx + 0x3f]
0036114C  E8 0F C5 19 00                  call 0x1404fd660
00361151  CC                              int3
00361152  0F B7 13                        movzx edx, word ptr [rbx]
00361155  81 E2 FF 1F 00 00               and edx, 0x1fff
0036115B  4C 8D 72 0F                     lea r14, [rdx + 0xf]
0036115F  49 83 E6 F0                     and r14, 0xfffffffffffffff0
00361163  4C 3B F6                        cmp r14, rsi
00361166  0F 84 DC FE FF FF               je 0x140361048
0036116C  44 8B C2                        mov r8d, edx
0036116F  48 C7 44 24 20 21 00 00 00      mov qword ptr [rsp + 0x20], 0x21
00361178  49 8B D4                        mov rdx, r12
0036117B  4C 8B CE                        mov r9, rsi
0036117E  B9 C1 00 00 00                  mov ecx, 0xc1
00361183  E8 D8 C4 19 00                  call 0x1404fd660
00361188  CC                              int3
00361189  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00361193  48 3B D8                        cmp rbx, rax
00361196  0F 83 C9 00 00 00               jae 0x140361265
0036119C  BA 02 00 00 00                  mov edx, 2
003611A1  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
003611A6  4C 8B CB                        mov r9, rbx
003611A9  B9 F1 01 00 00                  mov ecx, 0x1f1
003611AE  44 8D 42 FF                     lea r8d, [rdx - 1]
003611B2  E8 A9 C4 19 00                  call 0x1404fd660
003611B7  CC                              int3
003611B8  3C 04                           cmp al, 4
003611BA  0F 84 99 F2 FF FF               je 0x140360459
003611C0  41 BE 00 01 00 00               mov r14d, 0x100
003611C6  E9 94 F2 FF FF                  jmp 0x14036045f
003611CB  3C 04                           cmp al, 4
003611CD  0F 84 64 F1 FF FF               je 0x140360337
003611D3  41 BE 00 01 00 00               mov r14d, 0x100
003611D9  E9 5F F1 FF FF                  jmp 0x14036033d
003611DE  40 F6 C6 07                     test sil, 7
003611E2  74 21                           je 0x140361205
003611E4  B8 02 00 00 00                  mov eax, 2
003611E9  48 C7 44 24 20 08 00 00 00      mov qword ptr [rsp + 0x20], 8
003611F2  44 8B C0                        mov r8d, eax
003611F5  8B D0                           mov edx, eax
003611F7  4C 8B CE                        mov r9, rsi
003611FA  B9 F1 01 00 00                  mov ecx, 0x1f1
003611FF  E8 5C C4 19 00                  call 0x1404fd660
00361204  CC                              int3
00361205  49 8D 04 37                     lea rax, [r15 + rsi]
00361209  48 3B C6                        cmp rax, rsi
0036120C  73 1C                           jae 0x14036122a
0036120E  BA 02 00 00 00                  mov edx, 2
00361213  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00361218  4C 8B CE                        mov r9, rsi
0036121B  B9 F1 01 00 00                  mov ecx, 0x1f1
00361220  44 8D 42 01                     lea r8d, [rdx + 1]
00361224  E8 37 C4 19 00                  call 0x1404fd660
00361229  CC                              int3
0036122A  48 BB 00 00 00 00 00 80 00 00   movabs rbx, 0x800000000000
00361234  49 8B FF                        mov rdi, r15
00361237  48 03 DE                        add rbx, rsi
0036123A  48 C1 EF 03                     shr rdi, 3
0036123E  48 C1 EB 03                     shr rbx, 3
00361242  48 03 1D 8F 5C C6 00            add rbx, qword ptr [rip + 0xc65c8f]
00361249  48 85 FF                        test rdi, rdi
0036124C  75 7E                           jne 0x1403612cc
0036124E  41 F6 C7 07                     test r15b, 7
00361252  0F 84 4B EC FF FF               je 0x14035fea3
00361258  41 0F B6 C7                     movzx eax, r15b
0036125C  24 07                           and al, 7
0036125E  88 03                           mov byte ptr [rbx], al
00361260  E9 3E EC FF FF                  jmp 0x14035fea3
00361265  48 8D 83 00 10 00 00            lea rax, [rbx + 0x1000]
0036126C  48 3B C3                        cmp rax, rbx
0036126F  73 21                           jae 0x140361292
00361271  B9 00 10 00 00                  mov ecx, 0x1000
00361276  BA 02 00 00 00                  mov edx, 2
0036127B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00361280  4C 8B CB                        mov r9, rbx
00361283  B9 F1 01 00 00                  mov ecx, 0x1f1
00361288  44 8D 42 01                     lea r8d, [rdx + 1]
0036128C  E8 CF C3 19 00                  call 0x1404fd660
00361291  CC                              int3
00361292  48 B9 00 00 00 00 00 80 00 00   movabs rcx, 0x800000000000
0036129C  33 D2                           xor edx, edx
0036129E  48 03 CB                        add rcx, rbx
003612A1  41 B8 00 02 00 00               mov r8d, 0x200
003612A7  48 C1 E9 03                     shr rcx, 3
003612AB  48 03 0D 26 5C C6 00            add rcx, qword ptr [rip + 0xc65c26]
003612B2  E8 89 59 36 00                  call 0x1406c6c40
003612B7  E9 37 FE FF FF                  jmp 0x1403610f3
003612BC  49 FF C0                        inc r8
003612BF  E9 9F FD FF FF                  jmp 0x140361063
003612C4  49 FF C0                        inc r8
003612C7  E9 AF FD FF FF                  jmp 0x14036107b
003612CC  4C 8B C7                        mov r8, rdi
003612CF  33 D2                           xor edx, edx
003612D1  48 8B CB                        mov rcx, rbx
003612D4  E8 67 59 36 00                  call 0x1406c6c40
003612D9  48 03 DF                        add rbx, rdi
003612DC  E9 6D FF FF FF                  jmp 0x14036124e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00360968(__int64 a1, __int64 a2, __int64 a3, int a4)
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
int64_t sub_00360968(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4)
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00360968&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
