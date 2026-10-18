# PfSetSuperfetchInformation

- RVA: `0x00ADE6E8`–`0x00ADF309` (길이 `3,105` bytes)
- VA: `0x0000000140ADE6E8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB9BC`
- 디코드: `728`개 명령, `3,105/3,105` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **50**; 고유 호출 대상: **31**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00ADE79F` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00ADE8E5` → [PfpScenCtxPrefetchStateSet](../../pagelk/B6/PfpScenCtxPrefetchStateSet_function_00B6B4A8.md) (function, `0x00B6B4A8`)
- `0x00ADE970` → [PfpPartitionFindByHandle](../90/PfpPartitionFindByHandle_function_00902E48.md) (function, `0x00902E48`)
- `0x00ADE98B` → [PfTSetTraceWorkerPriority](../../text/5C/PfTSetTraceWorkerPriority_function_005CDD60.md) (function, `0x005CDD60`)
- `0x00ADEA0E` → [PfpProcessScenarioPhase](../A9/PfpProcessScenarioPhase_function_00A96D44.md) (function, `0x00A96D44`)
- `0x00ADEA36` → [PfpPrefetchRequest](../93/PfpPrefetchRequest_function_009385CC.md) (function, `0x009385CC`)
- `0x00ADEA44` → [EtwTiLogSyscallUsage](../90/EtwTiLogSyscallUsage_function_00903890.md) (function, `0x00903890`)
- `0x00ADEABB` → [PfpPartitionFindByHandle](../90/PfpPartitionFindByHandle_function_00902E48.md) (function, `0x00902E48`)
- `0x00ADEAD1` → [PfGenerateTrace](../75/PfGenerateTrace_function_0075101C.md) (function, `0x0075101C`)
- `0x00ADEBE1` → [PfpPartitionFindByHandle](../90/PfpPartitionFindByHandle_function_00902E48.md) (function, `0x00902E48`)
- `0x00ADEBFE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ADEC59` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00ADEC76` → [PfpLogEventRequest](../AC/PfpLogEventRequest_function_00AC1278.md) (function, `0x00AC1278`)
- `0x00ADECBC` → [PfpRpControlRequest](../A7/PfpRpControlRequest_function_00A7CF24.md) (function, `0x00A7CF24`)
- `0x00ADED11` → [PfpDeprioritizeOldPagesInWs](PfpDeprioritizeOldPagesInWs_function_00ADF310.md) (function, `0x00ADF310`)
- `0x00ADED6F` → [MmSetMinimumAgeRate](../AB/MmSetMinimumAgeRate_function_00AB16C0.md) (function, `0x00AB16C0`)
- `0x00ADED9D` → [PfpPfnPrioRequest](../90/PfpPfnPrioRequest_function_00902488.md) (function, `0x00902488`)
- `0x00ADEEC3` → [MmSetTrimWhileAgingState](../../text/67/MmSetTrimWhileAgingState_function_0067EF5C.md) (function, `0x0067EF5C`)
- `0x00ADEFB1` → [PsReferencePartitionByHandle](../90/PsReferencePartitionByHandle_function_0090337C.md) (function, `0x0090337C`)
- `0x00ADEFD1` → [PfpPartitionFindOrCreate](../75/PfpPartitionFindOrCreate_function_00752080.md) (function, `0x00752080`)
- `0x00ADEFF1` → [PfpPartitionAccessTraceLockAcquire](../../pagelk/B6/PfpPartitionAccessTraceLockAcquire_function_00B6BBC4.md) (function, `0x00B6BBC4`)
- `0x00ADF036` → [PfTCleanup](../75/PfTCleanup_function_00751208.md) (function, `0x00751208`)
- `0x00ADF041` → [PfTInitialize](../75/PfTInitialize_function_00751554.md) (function, `0x00751554`)
- `0x00ADF05B` → [PfTStart](../75/PfTStart_function_007517AC.md) (function, `0x007517AC`)
- `0x00ADF06D` → [PfpPartitionAccessTraceLockRelease](../../pagelk/B6/PfpPartitionAccessTraceLockRelease_function_00B6BBE0.md) (function, `0x00B6BBE0`)
- `0x00ADF090` → [PfpPartitionRundownProtectionAcquire](../../text/48/PfpPartitionRundownProtectionAcquire_function_0048402C.md) (function, `0x0048402C`)
- `0x00ADF121` → [PfpScenCtxServiceThreadSet](../../pagelk/B6/PfpScenCtxServiceThreadSet_function_00B6B7D8.md) (function, `0x00B6B7D8`)
- `0x00ADF136` → [PfpPartitionRundownProtectionRelease](../../text/47/PfpPartitionRundownProtectionRelease_function_0047BB54.md) (function, `0x0047BB54`)
- `0x00ADF1D0` → [PfpSetParameter](../75/PfpSetParameter_function_007533FC.md) (function, `0x007533FC`)
- `0x00ADF215` → [PfpPartitionAccessTraceLockRelease](../../pagelk/B6/PfpPartitionAccessTraceLockRelease_function_00B6BBE0.md) (function, `0x00B6BBE0`)
- `0x00ADF22A` → [PfpPartitionAccessTraceLockAcquire](../../pagelk/B6/PfpPartitionAccessTraceLockAcquire_function_00B6BBC4.md) (function, `0x00B6BBC4`)
- `0x00ADF234` → [PfTCleanup](../75/PfTCleanup_function_00751208.md) (function, `0x00751208`)
- `0x00ADF23F` → [PfTInitialize](../75/PfTInitialize_function_00751554.md) (function, `0x00751554`)
- `0x00ADF247` → [PfpPartitionAccessTraceLockRelease](../../pagelk/B6/PfpPartitionAccessTraceLockRelease_function_00B6BBE0.md) (function, `0x00B6BBE0`)
- `0x00ADF24F` → [PfpPartitionRundownProtectionRelease](../../text/47/PfpPartitionRundownProtectionRelease_function_0047BB54.md) (function, `0x0047BB54`)
- `0x00ADF261` → [PfpPartitionRundownProtectionRelease](../../text/47/PfpPartitionRundownProtectionRelease_function_0047BB54.md) (function, `0x0047BB54`)
- `0x00ADF270` → [PfpPartitionDereferenceParent](../../text/34/PfpPartitionDereferenceParent_function_00341CDC.md) (function, `0x00341CDC`)
- `0x00ADF285` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00ADF29C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ADF2C6` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00ADF2CC` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00ADF2D2` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00ADF2D8` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00ADF2DE` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00ADF2E4` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00ADF2EA` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00ADF2F0` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00ADF2F6` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00ADF2FC` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00ADF302` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF54F7`

### Static image references
- `0x00ADE798` → RVA `0x00FD9B08` (`PAGEDATA`; read)
- `0x00ADE8DE` → RVA `0x00E670D0` (`.data`; read)
- `0x00ADEFC5` → RVA `0x00E66EB0` (`.data`; read)
- `0x00ADF1A3` → RVA `0x00E670CC` (`.data`; read)
- `0x00ADF1C2` → RVA `0x00B014E0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ADF1C9` → RVA `0x00E66EB8` (`.data`; read)
- `0x00ADF1E7` → RVA `0x00E670CC` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00ADE8E5` → [PfpScenCtxPrefetchStateSet](../../pagelk/B6/PfpScenCtxPrefetchStateSet_function_00B6B4A8.md) (`PAGE` → `PAGELK`)
  - `0x00ADE98B` → [PfTSetTraceWorkerPriority](../../text/5C/PfTSetTraceWorkerPriority_function_005CDD60.md) (`PAGE` → `.text`)
  - `0x00ADEBFE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ADEC59` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00ADEEC3` → [MmSetTrimWhileAgingState](../../text/67/MmSetTrimWhileAgingState_function_0067EF5C.md) (`PAGE` → `.text`)
  - `0x00ADEFF1` → [PfpPartitionAccessTraceLockAcquire](../../pagelk/B6/PfpPartitionAccessTraceLockAcquire_function_00B6BBC4.md) (`PAGE` → `PAGELK`)
  - `0x00ADF06D` → [PfpPartitionAccessTraceLockRelease](../../pagelk/B6/PfpPartitionAccessTraceLockRelease_function_00B6BBE0.md) (`PAGE` → `PAGELK`)
  - `0x00ADF090` → [PfpPartitionRundownProtectionAcquire](../../text/48/PfpPartitionRundownProtectionAcquire_function_0048402C.md) (`PAGE` → `.text`)
  - `0x00ADF121` → [PfpScenCtxServiceThreadSet](../../pagelk/B6/PfpScenCtxServiceThreadSet_function_00B6B7D8.md) (`PAGE` → `PAGELK`)
  - `0x00ADF136` → [PfpPartitionRundownProtectionRelease](../../text/47/PfpPartitionRundownProtectionRelease_function_0047BB54.md) (`PAGE` → `.text`)
  - `0x00ADF215` → [PfpPartitionAccessTraceLockRelease](../../pagelk/B6/PfpPartitionAccessTraceLockRelease_function_00B6BBE0.md) (`PAGE` → `PAGELK`)
  - `0x00ADF22A` → [PfpPartitionAccessTraceLockAcquire](../../pagelk/B6/PfpPartitionAccessTraceLockAcquire_function_00B6BBC4.md) (`PAGE` → `PAGELK`)
  - `0x00ADF247` → [PfpPartitionAccessTraceLockRelease](../../pagelk/B6/PfpPartitionAccessTraceLockRelease_function_00B6BBE0.md) (`PAGE` → `PAGELK`)
  - `0x00ADF24F` → [PfpPartitionRundownProtectionRelease](../../text/47/PfpPartitionRundownProtectionRelease_function_0047BB54.md) (`PAGE` → `.text`)
  - `0x00ADF261` → [PfpPartitionRundownProtectionRelease](../../text/47/PfpPartitionRundownProtectionRelease_function_0047BB54.md) (`PAGE` → `.text`)
  - `0x00ADF270` → [PfpPartitionDereferenceParent](../../text/34/PfpPartitionDereferenceParent_function_00341CDC.md) (`PAGE` → `.text`)
  - `0x00ADF29C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ADE6E8  4C 8B DC                        mov r11, rsp
00ADE6EB  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
00ADE6EF  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00ADE6F3  45 88 4B 20                     mov byte ptr [r11 + 0x20], r9b
00ADE6F7  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00ADE6FB  57                              push rdi
00ADE6FC  41 54                           push r12
00ADE6FE  41 55                           push r13
00ADE700  41 56                           push r14
00ADE702  41 57                           push r15
00ADE704  48 81 EC 50 01 00 00            sub rsp, 0x150
00ADE70B  41 0F 29 73 C8                  movaps xmmword ptr [r11 - 0x38], xmm6
00ADE710  45 8A F1                        mov r14b, r9b
00ADE713  41 8B D8                        mov ebx, r8d
00ADE716  48 8B FA                        mov rdi, rdx
00ADE719  0F 57 C0                        xorps xmm0, xmm0
00ADE71C  41 0F 11 43 A8                  movups xmmword ptr [r11 - 0x58], xmm0
00ADE721  41 0F 11 43 B8                  movups xmmword ptr [r11 - 0x48], xmm0
00ADE726  33 F6                           xor esi, esi
00ADE728  49 89 B3 78 FF FF FF            mov qword ptr [r11 - 0x88], rsi
00ADE72F  0F 11 84 24 B8 00 00 00         movups xmmword ptr [rsp + 0xb8], xmm0
00ADE737  41 89 73 08                     mov dword ptr [r11 + 8], esi
00ADE73B  33 C0                           xor eax, eax
00ADE73D  49 89 83 34 FF FF FF            mov qword ptr [r11 - 0xcc], rax
00ADE744  49 89 83 30 FF FF FF            mov qword ptr [r11 - 0xd0], rax
00ADE74B  0F 11 84 24 C8 00 00 00         movups xmmword ptr [rsp + 0xc8], xmm0
00ADE753  0F 11 84 24 D8 00 00 00         movups xmmword ptr [rsp + 0xd8], xmm0
00ADE75B  89 B4 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], esi
00ADE762  49 89 73 80                     mov qword ptr [r11 - 0x80], rsi
00ADE766  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
00ADE76B  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
00ADE76F  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
00ADE774  48 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], rsi
00ADE77C  48 89 B4 24 98 00 00 00         mov qword ptr [rsp + 0x98], rsi
00ADE784  49 89 B3 18 FF FF FF            mov qword ptr [r11 - 0xe8], rsi
00ADE78B  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00ADE790  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00ADE795  41 8A D1                        mov dl, r9b
00ADE798  48 8B 0D 69 B3 4F 00            mov rcx, qword ptr [rip + 0x4fb369]
00ADE79F  E8 7C 36 D9 FF                  call 0x140871e20
00ADE7A4  84 C0                           test al, al
00ADE7A6  75 0A                           jne 0x140ade7b2
00ADE7A8  BB 22 00 00 C0                  mov ebx, 0xc0000022
00ADE7AD  E9 53 0A 00 00                  jmp 0x140adf205
00ADE7B2  83 FB 20                        cmp ebx, 0x20
00ADE7B5  74 0A                           je 0x140ade7c1
00ADE7B7  BB 04 00 00 C0                  mov ebx, 0xc0000004
00ADE7BC  E9 44 0A 00 00                  jmp 0x140adf205
00ADE7C1  8B DE                           mov ebx, esi
00ADE7C3  0F 57 C0                        xorps xmm0, xmm0
00ADE7C6  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
00ADE7CB  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
00ADE7D0  0F 10 07                        movups xmm0, xmmword ptr [rdi]
00ADE7D3  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
00ADE7D8  0F 10 4F 10                     movups xmm1, xmmword ptr [rdi + 0x10]
00ADE7DC  0F 11 4C 24 48                  movups xmmword ptr [rsp + 0x48], xmm1
00ADE7E1  EB 0C                           jmp 0x140ade7ef
00ADE7E3  8B D8                           mov ebx, eax
00ADE7E5  33 F6                           xor esi, esi
00ADE7E7  44 8A B4 24 98 01 00 00         mov r14b, byte ptr [rsp + 0x198]
00ADE7EF  85 DB                           test ebx, ebx
00ADE7F1  0F 88 0E 0A 00 00               js 0x140adf205
00ADE7F7  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00ADE7FC  83 F8 2D                        cmp eax, 0x2d
00ADE7FF  0F 85 FB 09 00 00               jne 0x140adf200
00ADE805  48 C1 E8 20                     shr rax, 0x20
00ADE809  3D 43 68 75 6B                  cmp eax, 0x6b756843
00ADE80E  0F 85 EC 09 00 00               jne 0x140adf200
00ADE814  8B 7C 24 40                     mov edi, dword ptr [rsp + 0x40]
00ADE818  83 FF 0E                        cmp edi, 0xe
00ADE81B  0F 8F A5 04 00 00               jg 0x140adecc6
00ADE821  0F 84 8D 04 00 00               je 0x140adecb4
00ADE827  8B CF                           mov ecx, edi
00ADE829  83 E9 03                        sub ecx, 3
00ADE82C  0F 84 BF 02 00 00               je 0x140adeaf1
00ADE832  83 E9 01                        sub ecx, 1
00ADE835  0F 84 13 02 00 00               je 0x140adea4e
00ADE83B  83 E9 01                        sub ecx, 1
00ADE83E  0F 84 EA 01 00 00               je 0x140adea2e
00ADE844  83 E9 02                        sub ecx, 2
00ADE847  0F 84 40 05 00 00               je 0x140aded8d
00ADE84D  83 E9 03                        sub ecx, 3
00ADE850  0F 84 60 01 00 00               je 0x140ade9b6
00ADE856  83 E9 01                        sub ecx, 1
00ADE859  0F 84 A4 00 00 00               je 0x140ade903
00ADE85F  83 F9 02                        cmp ecx, 2
00ADE862  0F 85 97 04 00 00               jne 0x140adecff
00ADE868  83 7C 24 50 08                  cmp dword ptr [rsp + 0x50], 8
00ADE86D  74 0A                           je 0x140ade879
00ADE86F  BB 06 02 00 C0                  mov ebx, 0xc0000206
00ADE874  E9 8C 09 00 00                  jmp 0x140adf205
00ADE879  45 84 F6                        test r14b, r14b
00ADE87C  74 21                           je 0x140ade89f
00ADE87E  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADE883  A8 03                           test al, 3
00ADE885  0F 85 3B 0A 00 00               jne 0x140adf2c6
00ADE88B  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00ADE895  49 3B C7                        cmp rax, r15
00ADE898  49 0F 43 C7                     cmovae rax, r15
00ADE89C  90                              nop
00ADE89D  8A 00                           mov al, byte ptr [rax]
00ADE89F  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00ADE8A4  4D 8B 00                        mov r8, qword ptr [r8]
00ADE8A7  4C 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r8
00ADE8AF  BF 01 00 00 00                  mov edi, 1
00ADE8B4  66 44 3B C7                     cmp r8w, di
00ADE8B8  0F 85 D8 03 00 00               jne 0x140adec96
00ADE8BE  49 8B D0                        mov rdx, r8
00ADE8C1  48 C1 EA 20                     shr rdx, 0x20
00ADE8C5  8D 42 FF                        lea eax, [rdx - 1]
00ADE8C8  83 F8 04                        cmp eax, 4
00ADE8CB  0F 87 C5 03 00 00               ja 0x140adec96
00ADE8D1  49 C1 E8 10                     shr r8, 0x10
00ADE8D5  44 23 C7                        and r8d, edi
00ADE8D8  44 03 C7                        add r8d, edi
00ADE8DB  45 33 C9                        xor r9d, r9d
00ADE8DE  48 8D 0D EB 87 38 00            lea rcx, [rip + 0x3887eb]
00ADE8E5  E8 BE CB 08 00                  call 0x140b6b4a8
00ADE8EA  E9 8C 03 00 00                  jmp 0x140adec7b
00ADE8EF  8B D8                           mov ebx, eax
00ADE8F1  33 F6                           xor esi, esi
00ADE8F3  8D 7E 01                        lea edi, [rsi + 1]
00ADE8F6  44 8A B4 24 98 01 00 00         mov r14b, byte ptr [rsp + 0x198]
00ADE8FE  E9 07 09 00 00                  jmp 0x140adf20a
00ADE903  B8 10 00 00 00                  mov eax, 0x10
00ADE908  39 44 24 50                     cmp dword ptr [rsp + 0x50], eax
00ADE90C  0F 85 5D FF FF FF               jne 0x140ade86f
00ADE912  45 84 F6                        test r14b, r14b
00ADE915  74 21                           je 0x140ade938
00ADE917  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADE91C  A8 07                           test al, 7
00ADE91E  0F 85 A8 09 00 00               jne 0x140adf2cc
00ADE924  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00ADE92E  49 3B C7                        cmp rax, r15
00ADE931  49 0F 43 C7                     cmovae rax, r15
00ADE935  90                              nop
00ADE936  8A 00                           mov al, byte ptr [rax]
00ADE938  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADE93D  0F 10 00                        movups xmm0, xmmword ptr [rax]
00ADE940  F3 0F 7F 84 24 B8 00 00 00      movdqu xmmword ptr [rsp + 0xb8], xmm0
00ADE949  BF 01 00 00 00                  mov edi, 1
00ADE94E  39 BC 24 B8 00 00 00            cmp dword ptr [rsp + 0xb8], edi
00ADE955  0F 85 F6 01 00 00               jne 0x140adeb51
00ADE95B  45 8A CE                        mov r9b, r14b
00ADE95E  4C 8B 84 24 C0 00 00 00         mov r8, qword ptr [rsp + 0xc0]
00ADE966  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00ADE96B  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00ADE970  E8 D3 44 E2 FF                  call 0x140902e48
00ADE975  8B D8                           mov ebx, eax
00ADE977  85 C0                           test eax, eax
00ADE979  0F 88 8B 08 00 00               js 0x140adf20a
00ADE97F  8B 94 24 BC 00 00 00            mov edx, dword ptr [rsp + 0xbc]
00ADE986  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00ADE98B  E8 D0 F3 AE FF                  call 0x1405cdd60
00ADE990  8B DE                           mov ebx, esi
00ADE992  B9 89 01 00 C0                  mov ecx, 0xc0000189
00ADE997  83 F8 1F                        cmp eax, 0x1f
00ADE99A  0F 4F D9                        cmovg ebx, ecx
00ADE99D  E9 68 08 00 00                  jmp 0x140adf20a
00ADE9A2  8B D8                           mov ebx, eax
00ADE9A4  33 F6                           xor esi, esi
00ADE9A6  8D 7E 01                        lea edi, [rsi + 1]
00ADE9A9  44 8A B4 24 98 01 00 00         mov r14b, byte ptr [rsp + 0x198]
00ADE9B1  E9 54 08 00 00                  jmp 0x140adf20a
00ADE9B6  83 7C 24 50 20                  cmp dword ptr [rsp + 0x50], 0x20
00ADE9BB  0F 85 AE FE FF FF               jne 0x140ade86f
00ADE9C1  45 84 F6                        test r14b, r14b
00ADE9C4  74 21                           je 0x140ade9e7
00ADE9C6  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADE9CB  A8 07                           test al, 7
00ADE9CD  0F 85 FF 08 00 00               jne 0x140adf2d2
00ADE9D3  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00ADE9DD  49 3B C7                        cmp rax, r15
00ADE9E0  49 0F 43 C7                     cmovae rax, r15
00ADE9E4  90                              nop
00ADE9E5  8A 00                           mov al, byte ptr [rax]
00ADE9E7  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADE9EC  0F 10 00                        movups xmm0, xmmword ptr [rax]
00ADE9EF  0F 11 84 24 20 01 00 00         movups xmmword ptr [rsp + 0x120], xmm0
00ADE9F7  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00ADE9FB  0F 11 8C 24 30 01 00 00         movups xmmword ptr [rsp + 0x130], xmm1
00ADEA03  41 8A D6                        mov dl, r14b
00ADEA06  48 8D 8C 24 20 01 00 00         lea rcx, [rsp + 0x120]
00ADEA0E  E8 31 83 FB FF                  call 0x140a96d44
00ADEA13  8B D8                           mov ebx, eax
00ADEA15  E9 EB 07 00 00                  jmp 0x140adf205
00ADEA1A  8B D8                           mov ebx, eax
00ADEA1C  33 F6                           xor esi, esi
00ADEA1E  8D 7E 01                        lea edi, [rsi + 1]
00ADEA21  44 8A B4 24 98 01 00 00         mov r14b, byte ptr [rsp + 0x198]
00ADEA29  E9 DC 07 00 00                  jmp 0x140adf20a
00ADEA2E  41 8A D6                        mov dl, r14b
00ADEA31  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
00ADEA36  E8 91 9B E5 FF                  call 0x1409385cc
00ADEA3B  8B D8                           mov ebx, eax
00ADEA3D  BA 11 00 00 00                  mov edx, 0x11
00ADEA42  8B C8                           mov ecx, eax
00ADEA44  E8 47 4E E2 FF                  call 0x140903890
00ADEA49  E9 B7 07 00 00                  jmp 0x140adf205
00ADEA4E  B8 10 00 00 00                  mov eax, 0x10
00ADEA53  39 44 24 50                     cmp dword ptr [rsp + 0x50], eax
00ADEA57  0F 85 12 FE FF FF               jne 0x140ade86f
00ADEA5D  45 84 F6                        test r14b, r14b
00ADEA60  74 21                           je 0x140adea83
00ADEA62  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADEA67  A8 07                           test al, 7
00ADEA69  0F 85 69 08 00 00               jne 0x140adf2d8
00ADEA6F  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00ADEA79  49 3B C7                        cmp rax, r15
00ADEA7C  49 0F 43 C7                     cmovae rax, r15
00ADEA80  90                              nop
00ADEA81  8A 00                           mov al, byte ptr [rax]
00ADEA83  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADEA88  0F 10 00                        movups xmm0, xmmword ptr [rax]
00ADEA8B  F3 0F 7F 84 24 A8 00 00 00      movdqu xmmword ptr [rsp + 0xa8], xmm0
00ADEA94  BF 01 00 00 00                  mov edi, 1
00ADEA99  39 BC 24 A8 00 00 00            cmp dword ptr [rsp + 0xa8], edi
00ADEAA0  0F 85 AB 00 00 00               jne 0x140adeb51
00ADEAA6  45 8A CE                        mov r9b, r14b
00ADEAA9  4C 8B 84 24 B0 00 00 00         mov r8, qword ptr [rsp + 0xb0]
00ADEAB1  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00ADEAB6  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00ADEABB  E8 88 43 E2 FF                  call 0x140902e48
00ADEAC0  8B D8                           mov ebx, eax
00ADEAC2  85 C0                           test eax, eax
00ADEAC4  0F 88 40 07 00 00               js 0x140adf20a
00ADEACA  33 D2                           xor edx, edx
00ADEACC  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00ADEAD1  E8 46 25 C7 FF                  call 0x14075101c
00ADEAD6  8B DE                           mov ebx, esi
00ADEAD8  E9 2D 07 00 00                  jmp 0x140adf20a
00ADEADD  8B D8                           mov ebx, eax
00ADEADF  33 F6                           xor esi, esi
00ADEAE1  8D 7E 01                        lea edi, [rsi + 1]
00ADEAE4  44 8A B4 24 98 01 00 00         mov r14b, byte ptr [rsp + 0x198]
00ADEAEC  E9 19 07 00 00                  jmp 0x140adf20a
00ADEAF1  83 7C 24 50 18                  cmp dword ptr [rsp + 0x50], 0x18
00ADEAF6  0F 85 73 FD FF FF               jne 0x140ade86f
00ADEAFC  45 84 F6                        test r14b, r14b
00ADEAFF  74 23                           je 0x140adeb24
00ADEB01  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADEB06  A8 07                           test al, 7
00ADEB08  0F 85 D0 07 00 00               jne 0x140adf2de
00ADEB0E  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00ADEB18  49 3B C7                        cmp rax, r15
00ADEB1B  49 0F 43 C7                     cmovae rax, r15
00ADEB1F  90                              nop
00ADEB20  8A 00                           mov al, byte ptr [rax]
00ADEB22  EB 0A                           jmp 0x140adeb2e
00ADEB24  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00ADEB2E  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADEB33  0F 10 00                        movups xmm0, xmmword ptr [rax]
00ADEB36  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00ADEB3B  F2 0F 10 48 10                  movsd xmm1, qword ptr [rax + 0x10]
00ADEB40  F2 0F 11 4C 24 78               movsd qword ptr [rsp + 0x78], xmm1
00ADEB46  BF 01 00 00 00                  mov edi, 1
00ADEB4B  39 7C 24 68                     cmp dword ptr [rsp + 0x68], edi
00ADEB4F  74 0A                           je 0x140adeb5b
00ADEB51  BB 59 00 00 C0                  mov ebx, 0xc0000059
00ADEB56  E9 AF 06 00 00                  jmp 0x140adf20a
00ADEB5B  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
00ADEB60  4D 85 E4                        test r12, r12
00ADEB63  0F 84 2D 01 00 00               je 0x140adec96
00ADEB69  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00ADEB6E  48 C1 E8 20                     shr rax, 0x20
00ADEB72  44 8B E8                        mov r13d, eax
00ADEB75  41 C1 ED 07                     shr r13d, 7
00ADEB79  45 85 ED                        test r13d, r13d
00ADEB7C  0F 84 14 01 00 00               je 0x140adec96
00ADEB82  83 E0 1F                        and eax, 0x1f
00ADEB85  83 E8 02                        sub eax, 2
00ADEB88  74 2A                           je 0x140adebb4
00ADEB8A  2B C7                           sub eax, edi
00ADEB8C  74 26                           je 0x140adebb4
00ADEB8E  83 E8 02                        sub eax, 2
00ADEB91  74 1A                           je 0x140adebad
00ADEB93  BA 16 00 00 00                  mov edx, 0x16
00ADEB98  3B C2                           cmp eax, edx
00ADEB9A  74 0A                           je 0x140adeba6
00ADEB9C  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00ADEBA1  E9 64 06 00 00                  jmp 0x140adf20a
00ADEBA6  B8 10 00 00 00                  mov eax, 0x10
00ADEBAB  EB 0C                           jmp 0x140adebb9
00ADEBAD  B8 0C 00 00 00                  mov eax, 0xc
00ADEBB2  EB 05                           jmp 0x140adebb9
00ADEBB4  B8 24 00 00 00                  mov eax, 0x24
00ADEBB9  44 3B E8                        cmp r13d, eax
00ADEBBC  0F 82 D4 00 00 00               jb 0x140adec96
00ADEBC2  41 81 FD F0 0F 00 00            cmp r13d, 0xff0
00ADEBC9  0F 83 C7 00 00 00               jae 0x140adec96
00ADEBCF  45 8A CE                        mov r9b, r14b
00ADEBD2  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
00ADEBD7  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00ADEBDC  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00ADEBE1  E8 62 42 E2 FF                  call 0x140902e48
00ADEBE6  8B D8                           mov ebx, eax
00ADEBE8  85 C0                           test eax, eax
00ADEBEA  0F 88 1A 06 00 00               js 0x140adf20a
00ADEBF0  41 8B D5                        mov edx, r13d
00ADEBF3  B9 00 01 00 00                  mov ecx, 0x100
00ADEBF8  41 B8 50 66 45 44               mov r8d, 0x44456650
00ADEBFE  E8 ED 34 0A 00                  call 0x140b820f0
00ADEC03  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00ADEC0B  48 85 C0                        test rax, rax
00ADEC0E  75 0A                           jne 0x140adec1a
00ADEC10  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00ADEC15  E9 F0 05 00 00                  jmp 0x140adf20a
00ADEC1A  45 84 F6                        test r14b, r14b
00ADEC1D  74 26                           je 0x140adec45
00ADEC1F  44 84 E7                        test dil, r12b
00ADEC22  0F 85 BC 06 00 00               jne 0x140adf2e4
00ADEC28  8B 4C 24 6C                     mov ecx, dword ptr [rsp + 0x6c]
00ADEC2C  48 C1 E9 07                     shr rcx, 7
00ADEC30  49 03 CC                        add rcx, r12
00ADEC33  49 3B CF                        cmp rcx, r15
00ADEC36  77 05                           ja 0x140adec3d
00ADEC38  49 3B CC                        cmp rcx, r12
00ADEC3B  73 08                           jae 0x140adec45
00ADEC3D  41 8A 07                        mov al, byte ptr [r15]
00ADEC40  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
00ADEC45  44 8B 44 24 6C                  mov r8d, dword ptr [rsp + 0x6c]
00ADEC4A  49 C1 E8 07                     shr r8, 7
00ADEC4E  49 8B D4                        mov rdx, r12
00ADEC51  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00ADEC59  E8 E2 7B BE FF                  call 0x1406c6840
00ADEC5E  90                              nop
00ADEC5F  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00ADEC67  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00ADEC6C  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
00ADEC71  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00ADEC76  E8 FD 25 FE FF                  call 0x140ac1278
00ADEC7B  8B D8                           mov ebx, eax
00ADEC7D  E9 88 05 00 00                  jmp 0x140adf20a
00ADEC82  8B D8                           mov ebx, eax
00ADEC84  33 F6                           xor esi, esi
00ADEC86  8D 7E 01                        lea edi, [rsi + 1]
00ADEC89  44 8A B4 24 98 01 00 00         mov r14b, byte ptr [rsp + 0x198]
00ADEC91  E9 74 05 00 00                  jmp 0x140adf20a
00ADEC96  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00ADEC9B  E9 6A 05 00 00                  jmp 0x140adf20a
00ADECA0  8B D8                           mov ebx, eax
00ADECA2  33 F6                           xor esi, esi
00ADECA4  8D 7E 01                        lea edi, [rsi + 1]
00ADECA7  44 8A B4 24 98 01 00 00         mov r14b, byte ptr [rsp + 0x198]
00ADECAF  E9 56 05 00 00                  jmp 0x140adf20a
00ADECB4  41 8A D6                        mov dl, r14b
00ADECB7  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
00ADECBC  E8 63 E2 F9 FF                  call 0x140a7cf24
00ADECC1  E9 4D FD FF FF                  jmp 0x140adea13
00ADECC6  8B CF                           mov ecx, edi
00ADECC8  83 E9 0F                        sub ecx, 0xf
00ADECCB  0F 84 93 04 00 00               je 0x140adf164
00ADECD1  83 E9 03                        sub ecx, 3
00ADECD4  0F 84 07 02 00 00               je 0x140adeee1
00ADECDA  83 E9 01                        sub ecx, 1
00ADECDD  0F 84 DC 00 00 00               je 0x140adedbf
00ADECE3  83 E9 03                        sub ecx, 3
00ADECE6  0F 84 A1 00 00 00               je 0x140aded8d
00ADECEC  83 E9 03                        sub ecx, 3
00ADECEF  74 2A                           je 0x140aded1b
00ADECF1  83 E9 01                        sub ecx, 1
00ADECF4  74 13                           je 0x140aded09
00ADECF6  83 F9 03                        cmp ecx, 3
00ADECF9  0F 84 8E 00 00 00               je 0x140aded8d
00ADECFF  BB 03 00 00 C0                  mov ebx, 0xc0000003
00ADED04  E9 FC 04 00 00                  jmp 0x140adf205
00ADED09  41 8A D6                        mov dl, r14b
00ADED0C  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
00ADED11  E8 FA 05 00 00                  call 0x140adf310
00ADED16  E9 F8 FC FF FF                  jmp 0x140adea13
00ADED1B  83 7C 24 50 08                  cmp dword ptr [rsp + 0x50], 8
00ADED20  0F 85 49 FB FF FF               jne 0x140ade86f
00ADED26  8B DE                           mov ebx, esi
00ADED28  45 84 F6                        test r14b, r14b
00ADED2B  74 21                           je 0x140aded4e
00ADED2D  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADED32  A8 03                           test al, 3
00ADED34  0F 85 B0 05 00 00               jne 0x140adf2ea
00ADED3A  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00ADED44  49 3B C7                        cmp rax, r15
00ADED47  49 0F 43 C7                     cmovae rax, r15
00ADED4B  90                              nop
00ADED4C  8A 00                           mov al, byte ptr [rax]
00ADED4E  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00ADED53  48 8B 09                        mov rcx, qword ptr [rcx]
00ADED56  48 89 8C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rcx
00ADED5E  BF 01 00 00 00                  mov edi, 1
00ADED63  3B CF                           cmp ecx, edi
00ADED65  0F 85 2B FF FF FF               jne 0x140adec96
00ADED6B  48 C1 E9 20                     shr rcx, 0x20
00ADED6F  E8 4C 29 FD FF                  call 0x140ab16c0
00ADED74  E9 91 04 00 00                  jmp 0x140adf20a
00ADED79  8B D8                           mov ebx, eax
00ADED7B  33 F6                           xor esi, esi
00ADED7D  8D 7E 01                        lea edi, [rsi + 1]
00ADED80  44 8A B4 24 98 01 00 00         mov r14b, byte ptr [rsp + 0x198]
00ADED88  E9 7D 04 00 00                  jmp 0x140adf20a
00ADED8D  4C 8D 84 24 A0 00 00 00         lea r8, [rsp + 0xa0]
00ADED95  41 8A D6                        mov dl, r14b
00ADED98  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
00ADED9D  E8 E6 36 E2 FF                  call 0x140902488
00ADEDA2  8B D8                           mov ebx, eax
00ADEDA4  BA 16 00 00 00                  mov edx, 0x16
00ADEDA9  83 FF 07                        cmp edi, 7
00ADEDAC  74 0A                           je 0x140adedb8
00ADEDAE  8B C6                           mov eax, esi
00ADEDB0  3B FA                           cmp edi, edx
00ADEDB2  0F 95 C0                        setne al
00ADEDB5  8D 50 17                        lea edx, [rax + 0x17]
00ADEDB8  8B CB                           mov ecx, ebx
00ADEDBA  E9 85 FC FF FF                  jmp 0x140adea44
00ADEDBF  83 7C 24 50 20                  cmp dword ptr [rsp + 0x50], 0x20
00ADEDC4  0F 85 A5 FA FF FF               jne 0x140ade86f
00ADEDCA  8B DE                           mov ebx, esi
00ADEDCC  45 84 F6                        test r14b, r14b
00ADEDCF  74 21                           je 0x140adedf2
00ADEDD1  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADEDD6  A8 07                           test al, 7
00ADEDD8  0F 85 12 05 00 00               jne 0x140adf2f0
00ADEDDE  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00ADEDE8  49 3B C7                        cmp rax, r15
00ADEDEB  49 0F 43 C7                     cmovae rax, r15
00ADEDEF  90                              nop
00ADEDF0  8A 00                           mov al, byte ptr [rax]
00ADEDF2  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADEDF7  0F 10 00                        movups xmm0, xmmword ptr [rax]
00ADEDFA  0F 11 84 24 C8 00 00 00         movups xmmword ptr [rsp + 0xc8], xmm0
00ADEE02  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
00ADEE06  0F 11 8C 24 D8 00 00 00         movups xmmword ptr [rsp + 0xd8], xmm1
00ADEE0E  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00ADEE16  83 F9 03                        cmp ecx, 3
00ADEE19  0F 85 E1 03 00 00               jne 0x140adf200
00ADEE1F  48 C1 E9 20                     shr rcx, 0x20
00ADEE23  83 F9 06                        cmp ecx, 6
00ADEE26  0F 8D D4 03 00 00               jge 0x140adf200
00ADEE2C  4C 8B 84 24 D0 00 00 00         mov r8, qword ptr [rsp + 0xd0]
00ADEE34  41 80 F8 07                     cmp r8b, 7
00ADEE38  0F 87 C2 03 00 00               ja 0x140adf200
00ADEE3E  4D 8B C8                        mov r9, r8
00ADEE41  49 C1 E9 08                     shr r9, 8
00ADEE45  41 80 F9 07                     cmp r9b, 7
00ADEE49  0F 87 B1 03 00 00               ja 0x140adf200
00ADEE4F  49 8B C0                        mov rax, r8
00ADEE52  48 C1 E8 10                     shr rax, 0x10
00ADEE56  66 85 C0                        test ax, ax
00ADEE59  0F 85 A1 03 00 00               jne 0x140adf200
00ADEE5F  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00ADEE67  83 F9 05                        cmp ecx, 5
00ADEE6A  75 1B                           jne 0x140adee87
00ADEE6C  48 85 C0                        test rax, rax
00ADEE6F  0F 84 8B 03 00 00               je 0x140adf200
00ADEE75  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
00ADEE7D  48 3B C2                        cmp rax, rdx
00ADEE80  77 1F                           ja 0x140adeea1
00ADEE82  E9 79 03 00 00                  jmp 0x140adf200
00ADEE87  48 85 C0                        test rax, rax
00ADEE8A  0F 85 70 03 00 00               jne 0x140adf200
00ADEE90  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
00ADEE98  48 85 D2                        test rdx, rdx
00ADEE9B  0F 85 5F 03 00 00               jne 0x140adf200
00ADEEA1  66 89 74 24 6E                  mov word ptr [rsp + 0x6e], si
00ADEEA6  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
00ADEEAA  44 88 44 24 6C                  mov byte ptr [rsp + 0x6c], r8b
00ADEEAF  44 88 4C 24 6D                  mov byte ptr [rsp + 0x6d], r9b
00ADEEB4  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00ADEEB9  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
00ADEEBE  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00ADEEC3  E8 94 00 BA FF                  call 0x14067ef5c
00ADEEC8  E9 38 03 00 00                  jmp 0x140adf205
00ADEECD  8B D8                           mov ebx, eax
00ADEECF  33 F6                           xor esi, esi
00ADEED1  8D 7E 01                        lea edi, [rsi + 1]
00ADEED4  44 8A B4 24 98 01 00 00         mov r14b, byte ptr [rsp + 0x198]
00ADEEDC  E9 29 03 00 00                  jmp 0x140adf20a
00ADEEE1  83 7C 24 50 20                  cmp dword ptr [rsp + 0x50], 0x20
00ADEEE6  0F 85 83 F9 FF FF               jne 0x140ade86f
00ADEEEC  45 84 F6                        test r14b, r14b
00ADEEEF  74 23                           je 0x140adef14
00ADEEF1  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADEEF6  A8 07                           test al, 7
00ADEEF8  0F 85 F8 03 00 00               jne 0x140adf2f6
00ADEEFE  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00ADEF08  49 3B C7                        cmp rax, r15
00ADEF0B  49 0F 43 C7                     cmovae rax, r15
00ADEF0F  90                              nop
00ADEF10  8A 00                           mov al, byte ptr [rax]
00ADEF12  EB 0A                           jmp 0x140adef1e
00ADEF14  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00ADEF1E  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00ADEF23  41 0F 10 34 24                  movups xmm6, xmmword ptr [r12]
00ADEF28  0F 11 B4 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm6
00ADEF30  41 0F 10 44 24 10               movups xmm0, xmmword ptr [r12 + 0x10]
00ADEF36  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
00ADEF3E  66 48 0F 7E F0                  movq rax, xmm6
00ADEF43  83 F8 03                        cmp eax, 3
00ADEF46  0F 85 B4 02 00 00               jne 0x140adf200
00ADEF4C  48 C1 E8 20                     shr rax, 0x20
00ADEF50  83 F8 02                        cmp eax, 2
00ADEF53  0F 83 A7 02 00 00               jae 0x140adf200
00ADEF59  66 0F 6F C6                     movdqa xmm0, xmm6
00ADEF5D  66 0F 73 D8 08                  psrldq xmm0, 8
00ADEF62  66 0F 7E C1                     movd ecx, xmm0
00ADEF66  89 8C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ecx
00ADEF6D  F7 C1 FC FF FF FF               test ecx, 0xfffffffc
00ADEF73  0F 85 87 02 00 00               jne 0x140adf200
00ADEF79  85 C0                           test eax, eax
00ADEF7B  75 14                           jne 0x140adef91
00ADEF7D  48 39 B4 24 18 01 00 00         cmp qword ptr [rsp + 0x118], rsi
00ADEF85  74 0A                           je 0x140adef91
00ADEF87  BB 30 00 00 C0                  mov ebx, 0xc0000030
00ADEF8C  E9 74 02 00 00                  jmp 0x140adf205
00ADEF91  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00ADEF96  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ADEF9B  41 B9 50 66 50 74               mov r9d, 0x74506650
00ADEFA1  45 8A C6                        mov r8b, r14b
00ADEFA4  BA 03 00 1F 00                  mov edx, 0x1f0003
00ADEFA9  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
00ADEFB1  E8 C6 43 E2 FF                  call 0x14090337c
00ADEFB6  8B D8                           mov ebx, eax
00ADEFB8  85 C0                           test eax, eax
00ADEFBA  0F 88 45 02 00 00               js 0x140adf205
00ADEFC0  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00ADEFC5  48 8D 15 E4 7E 38 00            lea rdx, [rip + 0x387ee4]
00ADEFCC  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00ADEFD1  E8 AA 30 C7 FF                  call 0x140752080
00ADEFD6  8B D8                           mov ebx, eax
00ADEFD8  BF 01 00 00 00                  mov edi, 1
00ADEFDD  85 C0                           test eax, eax
00ADEFDF  0F 88 25 02 00 00               js 0x140adf20a
00ADEFE5  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
00ADEFE9  4C 8B 6C 24 30                  mov r13, qword ptr [rsp + 0x30]
00ADEFEE  49 8B CD                        mov rcx, r13
00ADEFF1  E8 CE CB 08 00                  call 0x140b6bbc4
00ADEFF6  66 0F 6F C6                     movdqa xmm0, xmm6
00ADEFFA  66 0F 73 D8 04                  psrldq xmm0, 4
00ADEFFF  66 0F 7E C0                     movd eax, xmm0
00ADF003  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
00ADF00A  85 C0                           test eax, eax
00ADF00C  75 0F                           jne 0x140adf01d
00ADF00E  41 8B 5D 48                     mov ebx, dword ptr [r13 + 0x48]
00ADF012  F7 D3                           not ebx
00ADF014  23 9C 24 80 00 00 00            and ebx, dword ptr [rsp + 0x80]
00ADF01B  EB 29                           jmp 0x140adf046
00ADF01D  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00ADF024  F7 D0                           not eax
00ADF026  4C 8B 6C 24 30                  mov r13, qword ptr [rsp + 0x30]
00ADF02B  41 8B 5D 48                     mov ebx, dword ptr [r13 + 0x48]
00ADF02F  23 D8                           and ebx, eax
00ADF031  33 D2                           xor edx, edx
00ADF033  49 8B CD                        mov rcx, r13
00ADF036  E8 CD 21 C7 FF                  call 0x140751208
00ADF03B  40 8A D7                        mov dl, dil
00ADF03E  49 8B CD                        mov rcx, r13
00ADF041  E8 0E 25 C7 FF                  call 0x140751554
00ADF046  4C 8D 8C 24 90 00 00 00         lea r9, [rsp + 0x90]
00ADF04E  45 8A C6                        mov r8b, r14b
00ADF051  8B D3                           mov edx, ebx
00ADF053  4C 8B 6C 24 30                  mov r13, qword ptr [rsp + 0x30]
00ADF058  49 8B CD                        mov rcx, r13
00ADF05B  E8 4C 27 C7 FF                  call 0x1407517ac
00ADF060  8B D8                           mov ebx, eax
00ADF062  85 C0                           test eax, eax
00ADF064  0F 88 A0 01 00 00               js 0x140adf20a
00ADF06A  49 8B CD                        mov rcx, r13
00ADF06D  E8 6E CB 08 00                  call 0x140b6bbe0
00ADF072  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
00ADF076  8B 84 24 84 00 00 00            mov eax, dword ptr [rsp + 0x84]
00ADF07D  85 C0                           test eax, eax
00ADF07F  0F 85 8E 00 00 00               jne 0x140adf113
00ADF085  4C 89 AC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r13
00ADF08D  49 8B CD                        mov rcx, r13
00ADF090  E8 97 4F 9A FF                  call 0x14048402c
00ADF095  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
00ADF09D  48 89 84 24 18 01 00 00         mov qword ptr [rsp + 0x118], rax
00ADF0A5  45 84 F6                        test r14b, r14b
00ADF0A8  74 39                           je 0x140adf0e3
00ADF0AA  41 F6 C4 07                     test r12b, 7
00ADF0AE  0F 85 48 02 00 00               jne 0x140adf2fc
00ADF0B4  4D 3B E7                        cmp r12, r15
00ADF0B7  4D 0F 43 E7                     cmovae r12, r15
00ADF0BB  41 8A 04 24                     mov al, byte ptr [r12]
00ADF0BF  41 88 04 24                     mov byte ptr [r12], al
00ADF0C3  41 8A 44 24 1F                  mov al, byte ptr [r12 + 0x1f]
00ADF0C8  41 88 44 24 1F                  mov byte ptr [r12 + 0x1f], al
00ADF0CD  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
00ADF0D2  8B 84 24 04 01 00 00            mov eax, dword ptr [rsp + 0x104]
00ADF0D9  0F 10 B4 24 00 01 00 00         movups xmm6, xmmword ptr [rsp + 0x100]
00ADF0E1  EB 07                           jmp 0x140adf0ea
00ADF0E3  8B 84 24 84 00 00 00            mov eax, dword ptr [rsp + 0x84]
00ADF0EA  41 0F 11 34 24                  movups xmmword ptr [r12], xmm6
00ADF0EF  0F 10 84 24 10 01 00 00         movups xmm0, xmmword ptr [rsp + 0x110]
00ADF0F7  41 0F 11 44 24 10               movups xmmword ptr [r12 + 0x10], xmm0
00ADF0FD  EB 14                           jmp 0x140adf113
00ADF0FF  8B D8                           mov ebx, eax
00ADF101  33 F6                           xor esi, esi
00ADF103  8D 7E 01                        lea edi, [rsi + 1]
00ADF106  44 8A B4 24 98 01 00 00         mov r14b, byte ptr [rsp + 0x198]
00ADF10E  E9 F7 00 00 00                  jmp 0x140adf20a
00ADF113  8B D6                           mov edx, esi
00ADF115  85 C0                           test eax, eax
00ADF117  0F 94 C2                        sete dl
00ADF11A  48 8D 0D AF 7F 38 00            lea rcx, [rip + 0x387faf]
00ADF121  E8 B2 C6 08 00                  call 0x140b6b7d8
00ADF126  4C 8B BC 24 88 00 00 00         mov r15, qword ptr [rsp + 0x88]
00ADF12E  4D 85 FF                        test r15, r15
00ADF131  74 08                           je 0x140adf13b
00ADF133  49 8B CF                        mov rcx, r15
00ADF136  E8 19 CA 99 FF                  call 0x14047bb54
00ADF13B  48 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], rsi
00ADF143  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
00ADF14B  E9 BA 00 00 00                  jmp 0x140adf20a
00ADF150  8B D8                           mov ebx, eax
00ADF152  33 F6                           xor esi, esi
00ADF154  8D 7E 01                        lea edi, [rsi + 1]
00ADF157  44 8A B4 24 98 01 00 00         mov r14b, byte ptr [rsp + 0x198]
00ADF15F  E9 A6 00 00 00                  jmp 0x140adf20a
00ADF164  83 7C 24 50 04                  cmp dword ptr [rsp + 0x50], 4
00ADF169  0F 85 00 F7 FF FF               jne 0x140ade86f
00ADF16F  45 84 F6                        test r14b, r14b
00ADF172  74 21                           je 0x140adf195
00ADF174  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADF179  A8 03                           test al, 3
00ADF17B  0F 85 81 01 00 00               jne 0x140adf302
00ADF181  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00ADF18B  49 3B C7                        cmp rax, r15
00ADF18E  49 0F 43 C7                     cmovae rax, r15
00ADF192  90                              nop
00ADF193  8A 00                           mov al, byte ptr [rax]
00ADF195  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00ADF19A  8B 00                           mov eax, dword ptr [rax]
00ADF19C  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
00ADF1A3  8B 15 23 7F 38 00               mov edx, dword ptr [rip + 0x387f23]
00ADF1A9  03 D0                           add edx, eax
00ADF1AB  89 94 24 80 01 00 00            mov dword ptr [rsp + 0x180], edx
00ADF1B2  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00ADF1BA  4C 8D 8C 24 80 01 00 00         lea r9, [rsp + 0x180]
00ADF1C2  48 8D 15 17 23 02 00            lea rdx, [rip + 0x22317]
00ADF1C9  48 8B 0D E8 7C 38 00            mov rcx, qword ptr [rip + 0x387ce8]
00ADF1D0  E8 27 42 C7 FF                  call 0x1407533fc
00ADF1D5  8B D8                           mov ebx, eax
00ADF1D7  BF 01 00 00 00                  mov edi, 1
00ADF1DC  85 C0                           test eax, eax
00ADF1DE  78 2A                           js 0x140adf20a
00ADF1E0  8B 84 24 80 01 00 00            mov eax, dword ptr [rsp + 0x180]
00ADF1E7  89 05 DF 7E 38 00               mov dword ptr [rip + 0x387edf], eax
00ADF1ED  EB 1B                           jmp 0x140adf20a
00ADF1EF  8B D8                           mov ebx, eax
00ADF1F1  33 F6                           xor esi, esi
00ADF1F3  8D 7E 01                        lea edi, [rsi + 1]
00ADF1F6  44 8A B4 24 98 01 00 00         mov r14b, byte ptr [rsp + 0x198]
00ADF1FE  EB 0A                           jmp 0x140adf20a
00ADF200  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00ADF205  BF 01 00 00 00                  mov edi, 1
00ADF20A  39 74 24 58                     cmp dword ptr [rsp + 0x58], esi
00ADF20E  74 0A                           je 0x140adf21a
00ADF210  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00ADF215  E8 C6 C9 08 00                  call 0x140b6bbe0
00ADF21A  4C 8B BC 24 88 00 00 00         mov r15, qword ptr [rsp + 0x88]
00ADF222  4D 85 FF                        test r15, r15
00ADF225  74 2D                           je 0x140adf254
00ADF227  49 8B CF                        mov rcx, r15
00ADF22A  E8 95 C9 08 00                  call 0x140b6bbc4
00ADF22F  33 D2                           xor edx, edx
00ADF231  49 8B CF                        mov rcx, r15
00ADF234  E8 CF 1F C7 FF                  call 0x140751208
00ADF239  40 8A D7                        mov dl, dil
00ADF23C  49 8B CF                        mov rcx, r15
00ADF23F  E8 10 23 C7 FF                  call 0x140751554
00ADF244  49 8B CF                        mov rcx, r15
00ADF247  E8 94 C9 08 00                  call 0x140b6bbe0
00ADF24C  49 8B CF                        mov rcx, r15
00ADF24F  E8 00 C9 99 FF                  call 0x14047bb54
00ADF254  4C 8B 6C 24 30                  mov r13, qword ptr [rsp + 0x30]
00ADF259  4D 85 ED                        test r13, r13
00ADF25C  74 08                           je 0x140adf266
00ADF25E  49 8B CD                        mov rcx, r13
00ADF261  E8 EE C8 99 FF                  call 0x14047bb54
00ADF266  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00ADF26B  48 85 C9                        test rcx, rcx
00ADF26E  74 05                           je 0x140adf275
00ADF270  E8 67 2A 86 FF                  call 0x140341cdc
00ADF275  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00ADF27D  48 85 C9                        test rcx, rcx
00ADF280  74 08                           je 0x140adf28a
00ADF282  41 8A D6                        mov dl, r14b
00ADF285  E8 E6 25 DC FF                  call 0x1408a1870
00ADF28A  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00ADF292  48 85 C0                        test rax, rax
00ADF295  74 0A                           je 0x140adf2a1
00ADF297  33 D2                           xor edx, edx
00ADF299  48 8B C8                        mov rcx, rax
00ADF29C  E8 CF 35 0A 00                  call 0x140b82870
00ADF2A1  8B C3                           mov eax, ebx
00ADF2A3  4C 8D 9C 24 50 01 00 00         lea r11, [rsp + 0x150]
00ADF2AB  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00ADF2AF  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00ADF2B3  41 0F 28 73 F0                  movaps xmm6, xmmword ptr [r11 - 0x10]
00ADF2B8  49 8B E3                        mov rsp, r11
00ADF2BB  41 5F                           pop r15
00ADF2BD  41 5E                           pop r14
00ADF2BF  41 5D                           pop r13
00ADF2C1  41 5C                           pop r12
00ADF2C3  5F                              pop rdi
00ADF2C4  C3                              ret
00ADF2C5  CC                              int3
00ADF2C6  E8 05 AD DB FF                  call 0x140899fd0
00ADF2CB  90                              nop
00ADF2CC  E8 FF AC DB FF                  call 0x140899fd0
00ADF2D1  90                              nop
00ADF2D2  E8 F9 AC DB FF                  call 0x140899fd0
00ADF2D7  90                              nop
00ADF2D8  E8 F3 AC DB FF                  call 0x140899fd0
00ADF2DD  90                              nop
00ADF2DE  E8 ED AC DB FF                  call 0x140899fd0
00ADF2E3  90                              nop
00ADF2E4  E8 E7 AC DB FF                  call 0x140899fd0
00ADF2E9  90                              nop
00ADF2EA  E8 E1 AC DB FF                  call 0x140899fd0
00ADF2EF  90                              nop
00ADF2F0  E8 DB AC DB FF                  call 0x140899fd0
00ADF2F5  90                              nop
00ADF2F6  E8 D5 AC DB FF                  call 0x140899fd0
00ADF2FB  90                              nop
00ADF2FC  E8 CF AC DB FF                  call 0x140899fd0
00ADF301  90                              nop
00ADF302  E8 C9 AC DB FF                  call 0x140899fd0
00ADF307  90                              nop
00ADF308  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfSetSuperfetchInformation(int a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int16 v_stack_m10A;
    unsigned __int8 v_stack_m10B;
    unsigned int v_stack_m10C;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned __int8 v_stack_p20;
    unsigned int v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int8 *)(v_rsp + 32) = (unsigned __int8)(a4);
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (336);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm6;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm0;
    v_rsi = 0;
    *(unsigned __int64 *)(v_rsp - 136) = 0;
    v_stack_mC0 = v_xmm0;
    *(unsigned int *)(v_rsp + 8) = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 204) = 0;
    *(unsigned __int64 *)(v_rsp - 208) = 0;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm0;
    v_stack_mD8 = 0;
    *(unsigned __int64 *)(v_rsp - 128) = 0;
    v_stack_m118 = 0;
    v_stack_m120 = 0;
    v_stack_m148 = 0;
    v_stack_mF0 = 0;
    v_stack_mE0 = 0;
    *(unsigned __int64 *)(v_rsp - 232) = 0;
    v_stack_m110 = v_xmm0;
    v_stack_m100 = 0;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5223273), (unsigned __int8)(a4), a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00ADE7B2;
    goto loc_00ADF205;
loc_00ADE7B2:
    if (((unsigned int)((unsigned int)(0xC0000022ULL))) == 32) goto loc_00ADE7C1;
    goto loc_00ADF205;
loc_00ADE7C1:
    v_stack_m140 = v_xmm0;
    v_stack_m130 = v_xmm0;
    v_stack_m140 = v_xmm0;
    v_stack_m130 = v_xmm1;
    goto loc_00ADE7EF;
loc_00ADE7EF:
    if (sign_flag) goto loc_00ADF205;
    if (((unsigned int)(v_stack_m140)) != 45) goto loc_00ADF200;
    result = (v_stack_m140) >> (32);
    if (((unsigned int)(result)) != 0x6B756843ULL) goto loc_00ADF200;
    if (((unsigned int)((unsigned int)(v_stack_m138))) > 14) goto loc_00ADECC6;
    if (((unsigned int)((unsigned int)(v_stack_m138))) == 14) goto loc_00ADECB4;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m138)))) - (3));
    if (condition_is_equal) goto loc_00ADEAF1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00ADEA4E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00ADEA2E;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00ADED8D;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00ADE9B6;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00ADE903;
    if (a1 != 2) goto loc_00ADECFF;
    if (v_stack_m128 == 8) goto loc_00ADE879;
loc_00ADE86F:
    goto loc_00ADF205;
loc_00ADE879:
    if ((unsigned __int8)((unsigned __int8)(a4)) == 0) goto loc_00ADE89F;
    if ((((unsigned __int8)(v_stack_m130)) & (3)) != 0) goto loc_00ADF2C6;
    result = v_stack_m130;
    if (v_stack_m130 >= v_r15) { result = v_r15; }
loc_00ADE89F:
    v_stack_m88 = *(unsigned __int64 *)(v_stack_m130);
    if (((unsigned __int16)(*(unsigned __int64 *)(v_stack_m130))) != 1) goto loc_00ADEC96;
    a2 = (*(unsigned __int64 *)(v_stack_m130)) >> (32);
    if (((unsigned int)(a2 - 1)) > 4) goto loc_00ADEC96;
    a3 = (*(unsigned __int64 *)(v_stack_m130)) >> (16);
    a3 = (unsigned int)((a3) & (1));
    a3 = (unsigned int)((a3) + (1));
    a4 = 0;
    result = PfpScenCtxPrefetchStateSet(v_rip + 3704811, a2, a3, a4);
    goto loc_00ADEC7B;
loc_00ADE903:
    if (v_stack_m128 != 16) goto loc_00ADE86F;
    if ((unsigned __int8)((unsigned __int8)(a4)) == 0) goto loc_00ADE938;
    if ((((unsigned __int8)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2CC;
    result = v_stack_m130;
    if (v_stack_m130 >= v_r15) { result = v_r15; }
loc_00ADE938:
    v_stack_mC0 = v_xmm0;
    if (v_stack_mC0 != 1) goto loc_00ADEB51;
    result = PfpPartitionFindByHandle(v_stack_m148, v_stack_m118, v_stack_mB8, (unsigned __int8)((unsigned __int8)(a4)));
    if (sign_flag) goto loc_00ADF20A;
    result = PfTSetTraceWorkerPriority(v_stack_m148, (unsigned int)(v_stack_mBC), v_stack_mB8, (unsigned __int8)((unsigned __int8)(a4)));
    v_rbx = 0;
    if (((unsigned int)(result)) > 31) { v_rbx = (unsigned int)((unsigned int)(0xC0000189ULL)); }
    goto loc_00ADF20A;
loc_00ADE9B6:
    if (v_stack_m128 != 32) goto loc_00ADE86F;
    if ((unsigned __int8)((unsigned __int8)(a4)) == 0) goto loc_00ADE9E7;
    if ((((unsigned __int8)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2D2;
    result = v_stack_m130;
    if (v_stack_m130 >= v_r15) { result = v_r15; }
loc_00ADE9E7:
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm1;
    result = PfpProcessScenarioPhase(v_stack_m58, (unsigned __int8)((unsigned __int8)(a4)), v_stack_mB8, (unsigned __int8)((unsigned __int8)(a4)));
loc_00ADEA13:
    goto loc_00ADF205;
loc_00ADEA2E:
    result = PfpPrefetchRequest(v_stack_m140, (unsigned __int8)((unsigned __int8)(a4)), v_stack_mB8, (unsigned __int8)((unsigned __int8)(a4)));
loc_00ADEA44:
    result = EtwTiLogSyscallUsage((unsigned int)((unsigned int)(result)), 17, v_stack_mB8, (unsigned __int8)((unsigned __int8)(a4)));
    goto loc_00ADF205;
loc_00ADEA4E:
    if (v_stack_m128 != 16) goto loc_00ADE86F;
    if ((unsigned __int8)((unsigned __int8)(a4)) == 0) goto loc_00ADEA83;
    if ((((unsigned __int8)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2D8;
    result = v_stack_m130;
    if (v_stack_m130 >= v_r15) { result = v_r15; }
loc_00ADEA83:
    v_stack_mD0 = v_xmm0;
    if (v_stack_mD0 != 1) goto loc_00ADEB51;
    result = PfpPartitionFindByHandle(v_stack_m148, v_stack_m118, v_stack_mC8, (unsigned __int8)((unsigned __int8)(a4)));
    if (sign_flag) goto loc_00ADF20A;
    a2 = 0;
    result = PfGenerateTrace(v_stack_m148, a2, v_stack_mC8, (unsigned __int8)((unsigned __int8)(a4)));
    goto loc_00ADF20A;
loc_00ADEAF1:
    if (v_stack_m128 != 24) goto loc_00ADE86F;
    if ((unsigned __int8)((unsigned __int8)(a4)) == 0) goto loc_00ADEB24;
    if ((((unsigned __int8)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2DE;
    result = v_stack_m130;
    if (v_stack_m130 >= v_r15) { result = v_r15; }
    goto loc_00ADEB2E;
loc_00ADEB24:
loc_00ADEB2E:
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm1;
    if (v_stack_m110 == 1) goto loc_00ADEB5B;
loc_00ADEB51:
    goto loc_00ADF20A;
loc_00ADEB5B:
    if (v_stack_m100 == 0) goto loc_00ADEC96;
    result = (v_stack_m110) >> (32);
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (7));
    if ((unsigned int)(v_r13) == 0) goto loc_00ADEC96;
    result = (unsigned int)((result) & (31));
    result = (unsigned int)((result) - (2));
    if (condition_is_equal) goto loc_00ADEBB4;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00ADEBB4;
    result = (unsigned int)((result) - (2));
    if (condition_is_equal) goto loc_00ADEBAD;
    if (((unsigned int)(result)) == 22) goto loc_00ADEBA6;
    goto loc_00ADF20A;
loc_00ADEBA6:
    goto loc_00ADEBB9;
loc_00ADEBAD:
    goto loc_00ADEBB9;
loc_00ADEBB4:
loc_00ADEBB9:
    if (((unsigned int)(v_r13)) < 36) goto loc_00ADEC96;
    if (((unsigned int)(v_r13)) >= 0xFF0ULL) goto loc_00ADEC96;
    result = PfpPartitionFindByHandle(v_stack_m148, v_stack_m118, v_stack_m108, (unsigned __int8)((unsigned __int8)(a4)));
    if (sign_flag) goto loc_00ADF20A;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r13)), (unsigned int)(0x44456650ULL), (unsigned __int8)((unsigned __int8)(a4)));
    v_stack_mE0 = result;
    if (result != 0) goto loc_00ADEC1A;
    goto loc_00ADF20A;
loc_00ADEC1A:
    if ((unsigned __int8)((unsigned __int8)(a4)) == 0) goto loc_00ADEC45;
    if (((1) & ((unsigned __int8)(v_stack_m100))) != 0) goto loc_00ADF2E4;
    a1 = ((unsigned int)(v_stack_m10C)) >> (7);
    a1 = (a1) + (v_stack_m100);
    if (a1 > v_r15) goto loc_00ADEC3D;
    v_r12 = v_stack_m100;
    if (a1 < v_stack_m100) {
        result = *(unsigned __int8 *)(v_r15);
        v_r12 = v_stack_m100;
    }
    a3 = ((unsigned int)(v_stack_m10C)) >> (7);
    result = memcpy(v_stack_mE0, v_r12, a3, (unsigned __int8)((unsigned __int8)(a4)));
    v_stack_m100 = v_stack_mE0;
    result = PfpLogEventRequest(v_stack_m148, v_stack_m110, a3, (unsigned __int8)((unsigned __int8)(a4)));
loc_00ADEC7B:
    goto loc_00ADF20A;
loc_00ADEC96:
    goto loc_00ADF20A;
loc_00ADECB4:
    result = PfpRpControlRequest(v_stack_m140, (unsigned __int8)((unsigned __int8)(a4)), a3, (unsigned __int8)((unsigned __int8)(a4)));
    goto loc_00ADEA13;
loc_00ADECC6:
    a1 = (unsigned int)((1) - (15));
    if (condition_is_equal) goto loc_00ADF164;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00ADEEE1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00ADEDBF;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00ADED8D;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00ADED1B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00ADED09;
    if (a1 == 3) goto loc_00ADED8D;
loc_00ADECFF:
    goto loc_00ADF205;
loc_00ADED09:
    result = PfpDeprioritizeOldPagesInWs(v_stack_m140, (unsigned __int8)((unsigned __int8)(a4)), a3, (unsigned __int8)((unsigned __int8)(a4)));
    goto loc_00ADEA13;
loc_00ADED1B:
    if (v_stack_m128 != 8) goto loc_00ADE86F;
    if ((unsigned __int8)((unsigned __int8)(a4)) == 0) goto loc_00ADED4E;
    if ((((unsigned __int8)(v_stack_m130)) & (3)) != 0) goto loc_00ADF2EA;
    result = v_stack_m130;
    if (v_stack_m130 >= v_r15) { result = v_r15; }
loc_00ADED4E:
    v_stack_m80 = *(unsigned __int64 *)(v_stack_m130);
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m130))) != 1) goto loc_00ADEC96;
    a1 = (*(unsigned __int64 *)(v_stack_m130)) >> (32);
    result = MmSetMinimumAgeRate(a1, (unsigned __int8)((unsigned __int8)(a4)), a3, (unsigned __int8)((unsigned __int8)(a4)));
    goto loc_00ADF20A;
loc_00ADED8D:
    result = PfpPfnPrioRequest(v_stack_m140, (unsigned __int8)((unsigned __int8)(a4)), v_stack_mD8, (unsigned __int8)((unsigned __int8)(a4)));
    if (1 != 7) {
        result = 0;
        result = (1 != 22) ? 1 : 0;
        a2 = result + 23;
    }
    goto loc_00ADEA44;
loc_00ADEDBF:
    if (v_stack_m128 != 32) goto loc_00ADE86F;
    if ((unsigned __int8)((unsigned __int8)(a4)) == 0) goto loc_00ADEDF2;
    if ((((unsigned __int8)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2F0;
    result = v_stack_m130;
    if (v_stack_m130 >= v_r15) { result = v_r15; }
loc_00ADEDF2:
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm1;
    if (((unsigned int)(v_stack_mB0)) != 3) goto loc_00ADF200;
    a1 = (v_stack_mB0) >> (32);
    if (a1 >= 6) goto loc_00ADF200;
    if (((unsigned __int8)(v_stack_mA8)) > 7) goto loc_00ADF200;
    a4 = (v_stack_mA8) >> (8);
    if (((unsigned __int8)(a4)) > 7) goto loc_00ADF200;
    result = (v_stack_mA8) >> (16);
    if ((unsigned __int16)(result) != 0) goto loc_00ADF200;
    if (a1 != 5) goto loc_00ADEE87;
    if (v_stack_mA0 == 0) goto loc_00ADF200;
    if (v_stack_mA0 > v_stack_m98) goto loc_00ADEEA1;
    goto loc_00ADF200;
loc_00ADEE87:
    if (v_stack_mA0 != 0) goto loc_00ADF200;
    if (v_stack_m98 != 0) goto loc_00ADF200;
loc_00ADEEA1:
    v_stack_m10A = 0;
    v_stack_m110 = a1;
    v_stack_m10C = (unsigned __int8)(v_stack_mA8);
    v_stack_m10B = (unsigned __int8)(a4);
    v_stack_m108 = v_stack_mA0;
    v_stack_m100 = v_stack_m98;
    result = MmSetTrimWhileAgingState(v_stack_m110, v_stack_m98, v_stack_mA8, a4);
    goto loc_00ADF205;
loc_00ADEEE1:
    if (v_stack_m128 != 32) goto loc_00ADE86F;
    if ((unsigned __int8)((unsigned __int8)(a4)) == 0) goto loc_00ADEF14;
    if ((((unsigned __int8)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2F6;
    result = v_stack_m130;
    if (v_stack_m130 >= v_r15) { result = v_r15; }
    goto loc_00ADEF1E;
loc_00ADEF14:
loc_00ADEF1E:
    v_stack_m78 = v_xmm6;
    v_stack_m68 = v_xmm0;
    if (((unsigned int)(*(unsigned __int8 *)(result))) != 3) goto loc_00ADF200;
    result = (*(unsigned __int8 *)(result)) >> (32);
    if (((unsigned int)(result)) >= 2) goto loc_00ADF200;
    v_stack_mF8 = (unsigned int)(v_stack_m110);
    if ((((unsigned int)(v_stack_m110)) & (0xFFFFFFFCULL)) != 0) goto loc_00ADF200;
    if ((unsigned int)(result) != 0) goto loc_00ADEF91;
    if (v_stack_m60 == 0) goto loc_00ADEF91;
    goto loc_00ADF205;
loc_00ADEF91:
    v_stack_m158 = v_stack_m118;
    result = PsReferencePartitionByHandle(v_stack_m68, (unsigned int)(0x1F0003ULL), (unsigned __int8)((unsigned __int8)(a4)), (unsigned int)(0x74506650ULL));
    if (sign_flag) goto loc_00ADF205;
    result = PfpPartitionFindOrCreate(v_stack_m148, v_rip + 3702500, v_stack_m118, (unsigned int)(0x74506650ULL));
    if (sign_flag) goto loc_00ADF20A;
    v_stack_m120 = 1;
    result = PfpPartitionAccessTraceLockAcquire(v_stack_m148, v_rip + 3702500, v_stack_m118, (unsigned int)(0x74506650ULL));
    v_stack_mF4 = (unsigned int)(result);
    if ((unsigned int)(result) != 0) goto loc_00ADF01D;
    v_rbx = (unsigned int)(~((unsigned int)(*(unsigned int *)(v_stack_m148 + 72))));
    v_rbx = (unsigned int)((v_rbx) & (v_stack_mF8));
    goto loc_00ADF046;
loc_00ADF01D:
    result = (unsigned int)(~((unsigned int)(v_stack_mF8)));
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m148 + 72))) & ((unsigned int)(result)));
    a2 = 0;
    result = PfTCleanup(v_stack_m148, a2, v_stack_m118, (unsigned int)(0x74506650ULL));
    result = PfTInitialize(v_stack_m148, 1, v_stack_m118, (unsigned int)(0x74506650ULL));
loc_00ADF046:
    result = PfTStart(v_stack_m148, (unsigned int)((unsigned int)(v_rbx)), (unsigned __int8)((unsigned __int8)(a4)), v_stack_mE8);
    if (sign_flag) goto loc_00ADF20A;
    result = PfpPartitionAccessTraceLockRelease(v_stack_m148, (unsigned int)((unsigned int)(v_rbx)), (unsigned __int8)((unsigned __int8)(a4)), v_stack_mE8);
    v_stack_m120 = 0;
    if ((unsigned int)((unsigned int)(v_stack_mF4)) != 0) goto loc_00ADF113;
    v_stack_mF0 = v_stack_m148;
    result = PfpPartitionRundownProtectionAcquire(v_stack_m148, (unsigned int)((unsigned int)(v_rbx)), (unsigned __int8)((unsigned __int8)(a4)), v_stack_mE8);
    v_stack_m60 = v_stack_mE8;
    if ((unsigned __int8)((unsigned __int8)(a4)) == 0) goto loc_00ADF0E3;
    if ((((unsigned __int8)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2FC;
    v_r12 = v_stack_m130;
    if (v_stack_m130 >= v_r15) { v_r12 = v_r15; }
    *(unsigned __int8 *)(v_r12) = (unsigned __int8)(*(unsigned __int8 *)(v_r12));
    *(unsigned __int8 *)(v_r12 + 31) = (unsigned __int8)(*(unsigned __int8 *)(v_r12 + 31));
    goto loc_00ADF0EA;
loc_00ADF0E3:
loc_00ADF0EA:
    *(unsigned __int64 *)(v_stack_m130) = v_xmm6;
    *(unsigned __int64 *)(v_stack_m130 + 16) = v_xmm0;
    goto loc_00ADF113;
loc_00ADF113:
    a2 = ((unsigned int)((unsigned int)(v_stack_mF4)) == 0) ? 1 : 0;
    result = PfpScenCtxServiceThreadSet(v_rip + 3702703, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_mE8);
    if (v_stack_mF0 != 0) {
        a1 = v_stack_mF0;
        result = PfpPartitionRundownProtectionRelease(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_mE8);
    }
    v_stack_mF0 = 0;
    v_stack_mE8 = 0;
    goto loc_00ADF20A;
loc_00ADF164:
    if (v_stack_m128 != 4) goto loc_00ADE86F;
    if ((unsigned __int8)((unsigned __int8)(a4)) == 0) goto loc_00ADF195;
    if ((((unsigned __int8)(v_stack_m130)) & (3)) != 0) goto loc_00ADF302;
    result = v_stack_m130;
    if (v_stack_m130 >= v_stack_mF0) { result = v_stack_mF0; }
loc_00ADF195:
    v_stack_m90 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m130)));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3702563))) + ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m130)))));
    v_stack_p8 = (unsigned int)(a2);
    v_stack_m158 = 4;
    result = PfpSetParameter(*(unsigned __int64 *)(v_rip + 3701992), v_rip + 140055, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
    if (sign_flag) goto loc_00ADF20A;
    *(unsigned int *)(v_rip + 3702495) = (unsigned int)((unsigned int)(v_stack_p8));
    goto loc_00ADF20A;
loc_00ADF200:
loc_00ADF205:
loc_00ADF20A:
    result = (unsigned int)(v_stack_p8);
    if (v_stack_m120 != 0) {
        a1 = v_stack_m148;
        result = PfpPartitionAccessTraceLockRelease(a1, v_rip + 140055, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
    }
    if (v_stack_mF0 != 0) {
        a1 = v_stack_mF0;
        result = PfpPartitionAccessTraceLockAcquire(a1, v_rip + 140055, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
        a2 = 0;
        a1 = v_stack_mF0;
        result = PfTCleanup(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
        a2 = 1;
        a1 = v_stack_mF0;
        result = PfTInitialize(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
        a1 = v_stack_mF0;
        result = PfpPartitionAccessTraceLockRelease(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
        a1 = v_stack_mF0;
        result = PfpPartitionRundownProtectionRelease(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
    }
    if (v_stack_m148 != 0) {
        a1 = v_stack_m148;
        result = PfpPartitionRundownProtectionRelease(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
    }
    if (v_stack_m118 != 0) {
        result = PfpPartitionDereferenceParent(v_stack_m118, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
    }
    if (v_stack_mE8 != 0) {
        a2 = (unsigned __int8)((unsigned __int8)(a4));
        result = ObCloseHandle(v_stack_mE8, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
    }
    result = v_stack_mE0;
    if (v_stack_mE0 != 0) {
        a2 = 0;
        a1 = v_stack_mE0;
        result = ExFreePoolWithTag(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
    }
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
loc_00ADF2C6:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
loc_00ADF2CC:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
loc_00ADF2D2:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
loc_00ADF2D8:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
loc_00ADF2DE:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
loc_00ADF2E4:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
loc_00ADF2EA:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
loc_00ADF2F0:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
loc_00ADF2F6:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
loc_00ADF2FC:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
loc_00ADF302:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned __int8)((unsigned __int8)(a4)), v_stack_p8);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfSetSuperfetchInformation(int32_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint16_t v_stack_m10A;
    uint8_t v_stack_m10B;
    uint32_t v_stack_m10C;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint32_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m28;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint8_t v_stack_p20;
    uint32_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint8_t *)(local_rsp + 0x20) = (uint8_t)(Arg4);
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (336);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm6;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x48) = v_xmm0;
    local_rsi = 0;
    *(uint64_t *)(local_rsp - 0x88) = 0;
    v_stack_mC0 = v_xmm0;
    *(uint32_t *)(local_rsp + 0x8) = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0xCC) = 0;
    *(uint64_t *)(local_rsp - 0xD0) = 0;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm0;
    v_stack_mD8 = 0;
    *(uint64_t *)(local_rsp - 0x80) = 0;
    v_stack_m118 = 0;
    v_stack_m120 = 0;
    v_stack_m148 = 0;
    v_stack_mF0 = 0;
    v_stack_mE0 = 0;
    *(uint64_t *)(local_rsp - 0xE8) = 0;
    v_stack_m110 = v_xmm0;
    v_stack_m100 = 0;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4FB369), (uint8_t)(Arg4), Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00ADE7B2;
    goto loc_00ADF205;
loc_00ADE7B2:
    if (((uint32_t)((uint32_t)(0xC0000022ULL))) == 32) goto loc_00ADE7C1;
    goto loc_00ADF205;
loc_00ADE7C1:
    v_stack_m140 = v_xmm0;
    v_stack_m130 = v_xmm0;
    v_stack_m140 = v_xmm0;
    v_stack_m130 = v_xmm1;
    goto loc_00ADE7EF;
loc_00ADE7EF:
    if (sign_flag) goto loc_00ADF205;
    if (((uint32_t)(v_stack_m140)) != 45) goto loc_00ADF200;
    result = (v_stack_m140) >> (32);
    if (((uint32_t)(result)) != 0x6B756843ULL) goto loc_00ADF200;
    if (((uint32_t)((uint32_t)(v_stack_m138))) > 14) goto loc_00ADECC6;
    if (((uint32_t)((uint32_t)(v_stack_m138))) == 14) goto loc_00ADECB4;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m138)))) - (3));
    if (condition_is_equal) goto loc_00ADEAF1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00ADEA4E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00ADEA2E;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00ADED8D;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00ADE9B6;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00ADE903;
    if (Arg1 != 2) goto loc_00ADECFF;
    if (v_stack_m128 == 8) goto loc_00ADE879;
loc_00ADE86F:
    goto loc_00ADF205;
loc_00ADE879:
    if ((uint8_t)((uint8_t)(Arg4)) == 0) goto loc_00ADE89F;
    if ((((uint8_t)(v_stack_m130)) & (3)) != 0) goto loc_00ADF2C6;
    result = v_stack_m130;
    if (v_stack_m130 >= local_r15) { result = local_r15; }
loc_00ADE89F:
    v_stack_m88 = *(uint64_t *)(v_stack_m130);
    if (((uint16_t)(*(uint64_t *)(v_stack_m130))) != 1) goto loc_00ADEC96;
    Arg2 = (*(uint64_t *)(v_stack_m130)) >> (32);
    if (((uint32_t)(Arg2 - 1)) > 4) goto loc_00ADEC96;
    Arg3 = (*(uint64_t *)(v_stack_m130)) >> (16);
    Arg3 = (uint32_t)((Arg3) & (1));
    Arg3 = (uint32_t)((Arg3) + (1));
    Arg4 = 0;
    result = PfpScenCtxPrefetchStateSet(v_rip + 3704811, Arg2, Arg3, Arg4);
    goto loc_00ADEC7B;
loc_00ADE903:
    if (v_stack_m128 != 16) goto loc_00ADE86F;
    if ((uint8_t)((uint8_t)(Arg4)) == 0) goto loc_00ADE938;
    if ((((uint8_t)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2CC;
    result = v_stack_m130;
    if (v_stack_m130 >= local_r15) { result = local_r15; }
loc_00ADE938:
    v_stack_mC0 = v_xmm0;
    if (v_stack_mC0 != 1) goto loc_00ADEB51;
    result = PfpPartitionFindByHandle(v_stack_m148, v_stack_m118, v_stack_mB8, (uint8_t)((uint8_t)(Arg4)));
    if (sign_flag) goto loc_00ADF20A;
    result = PfTSetTraceWorkerPriority(v_stack_m148, (uint32_t)(v_stack_mBC), v_stack_mB8, (uint8_t)((uint8_t)(Arg4)));
    local_rbx = 0;
    if (((uint32_t)(result)) > 31) { local_rbx = (uint32_t)((uint32_t)(0xC0000189ULL)); }
    goto loc_00ADF20A;
loc_00ADE9B6:
    if (v_stack_m128 != 32) goto loc_00ADE86F;
    if ((uint8_t)((uint8_t)(Arg4)) == 0) goto loc_00ADE9E7;
    if ((((uint8_t)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2D2;
    result = v_stack_m130;
    if (v_stack_m130 >= local_r15) { result = local_r15; }
loc_00ADE9E7:
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm1;
    result = PfpProcessScenarioPhase(v_stack_m58, (uint8_t)((uint8_t)(Arg4)), v_stack_mB8, (uint8_t)((uint8_t)(Arg4)));
loc_00ADEA13:
    goto loc_00ADF205;
loc_00ADEA2E:
    result = PfpPrefetchRequest(v_stack_m140, (uint8_t)((uint8_t)(Arg4)), v_stack_mB8, (uint8_t)((uint8_t)(Arg4)));
loc_00ADEA44:
    result = EtwTiLogSyscallUsage((uint32_t)((uint32_t)(result)), 17, v_stack_mB8, (uint8_t)((uint8_t)(Arg4)));
    goto loc_00ADF205;
loc_00ADEA4E:
    if (v_stack_m128 != 16) goto loc_00ADE86F;
    if ((uint8_t)((uint8_t)(Arg4)) == 0) goto loc_00ADEA83;
    if ((((uint8_t)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2D8;
    result = v_stack_m130;
    if (v_stack_m130 >= local_r15) { result = local_r15; }
loc_00ADEA83:
    v_stack_mD0 = v_xmm0;
    if (v_stack_mD0 != 1) goto loc_00ADEB51;
    result = PfpPartitionFindByHandle(v_stack_m148, v_stack_m118, v_stack_mC8, (uint8_t)((uint8_t)(Arg4)));
    if (sign_flag) goto loc_00ADF20A;
    Arg2 = 0;
    result = PfGenerateTrace(v_stack_m148, Arg2, v_stack_mC8, (uint8_t)((uint8_t)(Arg4)));
    goto loc_00ADF20A;
loc_00ADEAF1:
    if (v_stack_m128 != 24) goto loc_00ADE86F;
    if ((uint8_t)((uint8_t)(Arg4)) == 0) goto loc_00ADEB24;
    if ((((uint8_t)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2DE;
    result = v_stack_m130;
    if (v_stack_m130 >= local_r15) { result = local_r15; }
    goto loc_00ADEB2E;
loc_00ADEB24:
loc_00ADEB2E:
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm1;
    if (v_stack_m110 == 1) goto loc_00ADEB5B;
loc_00ADEB51:
    goto loc_00ADF20A;
loc_00ADEB5B:
    if (v_stack_m100 == 0) goto loc_00ADEC96;
    result = (v_stack_m110) >> (32);
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (7));
    if ((uint32_t)(local_r13) == 0) goto loc_00ADEC96;
    result = (uint32_t)((result) & (31));
    result = (uint32_t)((result) - (2));
    if (condition_is_equal) goto loc_00ADEBB4;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00ADEBB4;
    result = (uint32_t)((result) - (2));
    if (condition_is_equal) goto loc_00ADEBAD;
    if (((uint32_t)(result)) == 22) goto loc_00ADEBA6;
    goto loc_00ADF20A;
loc_00ADEBA6:
    goto loc_00ADEBB9;
loc_00ADEBAD:
    goto loc_00ADEBB9;
loc_00ADEBB4:
loc_00ADEBB9:
    if (((uint32_t)(local_r13)) < 36) goto loc_00ADEC96;
    if (((uint32_t)(local_r13)) >= 0xFF0ULL) goto loc_00ADEC96;
    result = PfpPartitionFindByHandle(v_stack_m148, v_stack_m118, v_stack_m108, (uint8_t)((uint8_t)(Arg4)));
    if (sign_flag) goto loc_00ADF20A;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r13)), (uint32_t)(0x44456650ULL), (uint8_t)((uint8_t)(Arg4)));
    v_stack_mE0 = result;
    if (result != 0) goto loc_00ADEC1A;
    goto loc_00ADF20A;
loc_00ADEC1A:
    if ((uint8_t)((uint8_t)(Arg4)) == 0) goto loc_00ADEC45;
    if (((1) & ((uint8_t)(v_stack_m100))) != 0) goto loc_00ADF2E4;
    Arg1 = ((uint32_t)(v_stack_m10C)) >> (7);
    Arg1 = (Arg1) + (v_stack_m100);
    if (Arg1 > local_r15) goto loc_00ADEC3D;
    local_r12 = v_stack_m100;
    if (Arg1 < v_stack_m100) {
        result = *(uint8_t *)(local_r15);
        local_r12 = v_stack_m100;
    }
    Arg3 = ((uint32_t)(v_stack_m10C)) >> (7);
    result = memcpy(v_stack_mE0, local_r12, Arg3, (uint8_t)((uint8_t)(Arg4)));
    v_stack_m100 = v_stack_mE0;
    result = PfpLogEventRequest(v_stack_m148, v_stack_m110, Arg3, (uint8_t)((uint8_t)(Arg4)));
loc_00ADEC7B:
    goto loc_00ADF20A;
loc_00ADEC96:
    goto loc_00ADF20A;
loc_00ADECB4:
    result = PfpRpControlRequest(v_stack_m140, (uint8_t)((uint8_t)(Arg4)), Arg3, (uint8_t)((uint8_t)(Arg4)));
    goto loc_00ADEA13;
loc_00ADECC6:
    Arg1 = (uint32_t)((1) - (15));
    if (condition_is_equal) goto loc_00ADF164;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00ADEEE1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00ADEDBF;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00ADED8D;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00ADED1B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00ADED09;
    if (Arg1 == 3) goto loc_00ADED8D;
loc_00ADECFF:
    goto loc_00ADF205;
loc_00ADED09:
    result = PfpDeprioritizeOldPagesInWs(v_stack_m140, (uint8_t)((uint8_t)(Arg4)), Arg3, (uint8_t)((uint8_t)(Arg4)));
    goto loc_00ADEA13;
loc_00ADED1B:
    if (v_stack_m128 != 8) goto loc_00ADE86F;
    if ((uint8_t)((uint8_t)(Arg4)) == 0) goto loc_00ADED4E;
    if ((((uint8_t)(v_stack_m130)) & (3)) != 0) goto loc_00ADF2EA;
    result = v_stack_m130;
    if (v_stack_m130 >= local_r15) { result = local_r15; }
loc_00ADED4E:
    v_stack_m80 = *(uint64_t *)(v_stack_m130);
    if (((uint32_t)(*(uint64_t *)(v_stack_m130))) != 1) goto loc_00ADEC96;
    Arg1 = (*(uint64_t *)(v_stack_m130)) >> (32);
    result = MmSetMinimumAgeRate(Arg1, (uint8_t)((uint8_t)(Arg4)), Arg3, (uint8_t)((uint8_t)(Arg4)));
    goto loc_00ADF20A;
loc_00ADED8D:
    result = PfpPfnPrioRequest(v_stack_m140, (uint8_t)((uint8_t)(Arg4)), v_stack_mD8, (uint8_t)((uint8_t)(Arg4)));
    if (1 != 7) {
        result = 0;
        result = (1 != 22) ? 1 : 0;
        Arg2 = result + 23;
    }
    goto loc_00ADEA44;
loc_00ADEDBF:
    if (v_stack_m128 != 32) goto loc_00ADE86F;
    if ((uint8_t)((uint8_t)(Arg4)) == 0) goto loc_00ADEDF2;
    if ((((uint8_t)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2F0;
    result = v_stack_m130;
    if (v_stack_m130 >= local_r15) { result = local_r15; }
loc_00ADEDF2:
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm1;
    if (((uint32_t)(v_stack_mB0)) != 3) goto loc_00ADF200;
    Arg1 = (v_stack_mB0) >> (32);
    if (Arg1 >= 6) goto loc_00ADF200;
    if (((uint8_t)(v_stack_mA8)) > 7) goto loc_00ADF200;
    Arg4 = (v_stack_mA8) >> (8);
    if (((uint8_t)(Arg4)) > 7) goto loc_00ADF200;
    result = (v_stack_mA8) >> (16);
    if ((uint16_t)(result) != 0) goto loc_00ADF200;
    if (Arg1 != 5) goto loc_00ADEE87;
    if (v_stack_mA0 == 0) goto loc_00ADF200;
    if (v_stack_mA0 > v_stack_m98) goto loc_00ADEEA1;
    goto loc_00ADF200;
loc_00ADEE87:
    if (v_stack_mA0 != 0) goto loc_00ADF200;
    if (v_stack_m98 != 0) goto loc_00ADF200;
loc_00ADEEA1:
    v_stack_m10A = 0;
    v_stack_m110 = Arg1;
    v_stack_m10C = (uint8_t)(v_stack_mA8);
    v_stack_m10B = (uint8_t)(Arg4);
    v_stack_m108 = v_stack_mA0;
    v_stack_m100 = v_stack_m98;
    result = MmSetTrimWhileAgingState(v_stack_m110, v_stack_m98, v_stack_mA8, Arg4);
    goto loc_00ADF205;
loc_00ADEEE1:
    if (v_stack_m128 != 32) goto loc_00ADE86F;
    if ((uint8_t)((uint8_t)(Arg4)) == 0) goto loc_00ADEF14;
    if ((((uint8_t)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2F6;
    result = v_stack_m130;
    if (v_stack_m130 >= local_r15) { result = local_r15; }
    goto loc_00ADEF1E;
loc_00ADEF14:
loc_00ADEF1E:
    v_stack_m78 = v_xmm6;
    v_stack_m68 = v_xmm0;
    if (((uint32_t)(*(uint8_t *)(result))) != 3) goto loc_00ADF200;
    result = (*(uint8_t *)(result)) >> (32);
    if (((uint32_t)(result)) >= 2) goto loc_00ADF200;
    v_stack_mF8 = (uint32_t)(v_stack_m110);
    if ((((uint32_t)(v_stack_m110)) & (0xFFFFFFFCULL)) != 0) goto loc_00ADF200;
    if ((uint32_t)(result) != 0) goto loc_00ADEF91;
    if (v_stack_m60 == 0) goto loc_00ADEF91;
    goto loc_00ADF205;
loc_00ADEF91:
    v_stack_m158 = v_stack_m118;
    result = PsReferencePartitionByHandle(v_stack_m68, (uint32_t)(0x1F0003ULL), (uint8_t)((uint8_t)(Arg4)), (uint32_t)(0x74506650ULL));
    if (sign_flag) goto loc_00ADF205;
    result = PfpPartitionFindOrCreate(v_stack_m148, v_rip + 3702500, v_stack_m118, (uint32_t)(0x74506650ULL));
    if (sign_flag) goto loc_00ADF20A;
    v_stack_m120 = 1;
    result = PfpPartitionAccessTraceLockAcquire(v_stack_m148, v_rip + 3702500, v_stack_m118, (uint32_t)(0x74506650ULL));
    v_stack_mF4 = (uint32_t)(result);
    if ((uint32_t)(result) != 0) goto loc_00ADF01D;
    local_rbx = (uint32_t)(~((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x48))));
    local_rbx = (uint32_t)((local_rbx) & (v_stack_mF8));
    goto loc_00ADF046;
loc_00ADF01D:
    result = (uint32_t)(~((uint32_t)(v_stack_mF8)));
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m148 + 0x48))) & ((uint32_t)(result)));
    Arg2 = 0;
    result = PfTCleanup(v_stack_m148, Arg2, v_stack_m118, (uint32_t)(0x74506650ULL));
    result = PfTInitialize(v_stack_m148, 1, v_stack_m118, (uint32_t)(0x74506650ULL));
loc_00ADF046:
    result = PfTStart(v_stack_m148, (uint32_t)((uint32_t)(local_rbx)), (uint8_t)((uint8_t)(Arg4)), v_stack_mE8);
    if (sign_flag) goto loc_00ADF20A;
    result = PfpPartitionAccessTraceLockRelease(v_stack_m148, (uint32_t)((uint32_t)(local_rbx)), (uint8_t)((uint8_t)(Arg4)), v_stack_mE8);
    v_stack_m120 = 0;
    if ((uint32_t)((uint32_t)(v_stack_mF4)) != 0) goto loc_00ADF113;
    v_stack_mF0 = v_stack_m148;
    result = PfpPartitionRundownProtectionAcquire(v_stack_m148, (uint32_t)((uint32_t)(local_rbx)), (uint8_t)((uint8_t)(Arg4)), v_stack_mE8);
    v_stack_m60 = v_stack_mE8;
    if ((uint8_t)((uint8_t)(Arg4)) == 0) goto loc_00ADF0E3;
    if ((((uint8_t)(v_stack_m130)) & (7)) != 0) goto loc_00ADF2FC;
    local_r12 = v_stack_m130;
    if (v_stack_m130 >= local_r15) { local_r12 = local_r15; }
    *(uint8_t *)(local_r12) = (uint8_t)(*(uint8_t *)(local_r12));
    *(uint8_t *)(local_r12 + 0x1F) = (uint8_t)(*(uint8_t *)(local_r12 + 0x1F));
    goto loc_00ADF0EA;
loc_00ADF0E3:
loc_00ADF0EA:
    *(uint64_t *)(v_stack_m130) = v_xmm6;
    *(uint64_t *)(v_stack_m130 + 0x10) = v_xmm0;
    goto loc_00ADF113;
loc_00ADF113:
    Arg2 = ((uint32_t)((uint32_t)(v_stack_mF4)) == 0) ? 1 : 0;
    result = PfpScenCtxServiceThreadSet(v_rip + 3702703, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_mE8);
    if (v_stack_mF0 != 0) {
        Arg1 = v_stack_mF0;
        result = PfpPartitionRundownProtectionRelease(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_mE8);
    }
    v_stack_mF0 = 0;
    v_stack_mE8 = 0;
    goto loc_00ADF20A;
loc_00ADF164:
    if (v_stack_m128 != 4) goto loc_00ADE86F;
    if ((uint8_t)((uint8_t)(Arg4)) == 0) goto loc_00ADF195;
    if ((((uint8_t)(v_stack_m130)) & (3)) != 0) goto loc_00ADF302;
    result = v_stack_m130;
    if (v_stack_m130 >= v_stack_mF0) { result = v_stack_mF0; }
loc_00ADF195:
    v_stack_m90 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m130)));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x387F23))) + ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m130)))));
    v_stack_p8 = (uint32_t)(Arg2);
    v_stack_m158 = 4;
    result = PfpSetParameter(*(uint64_t *)(v_rip + 0x387CE8), v_rip + 140055, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
    if (sign_flag) goto loc_00ADF20A;
    *(uint32_t *)(v_rip + 0x387EDF) = (uint32_t)((uint32_t)(v_stack_p8));
    goto loc_00ADF20A;
loc_00ADF200:
loc_00ADF205:
loc_00ADF20A:
    result = (uint32_t)(v_stack_p8);
    if (v_stack_m120 != 0) {
        Arg1 = v_stack_m148;
        result = PfpPartitionAccessTraceLockRelease(Arg1, v_rip + 140055, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
    }
    if (v_stack_mF0 != 0) {
        Arg1 = v_stack_mF0;
        result = PfpPartitionAccessTraceLockAcquire(Arg1, v_rip + 140055, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
        Arg2 = 0;
        Arg1 = v_stack_mF0;
        result = PfTCleanup(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
        Arg2 = 1;
        Arg1 = v_stack_mF0;
        result = PfTInitialize(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
        Arg1 = v_stack_mF0;
        result = PfpPartitionAccessTraceLockRelease(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
        Arg1 = v_stack_mF0;
        result = PfpPartitionRundownProtectionRelease(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
    }
    if (v_stack_m148 != 0) {
        Arg1 = v_stack_m148;
        result = PfpPartitionRundownProtectionRelease(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
    }
    if (v_stack_m118 != 0) {
        result = PfpPartitionDereferenceParent(v_stack_m118, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
    }
    if (v_stack_mE8 != 0) {
        Arg2 = (uint8_t)((uint8_t)(Arg4));
        result = ObCloseHandle(v_stack_mE8, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
    }
    result = v_stack_mE0;
    if (v_stack_mE0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mE0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
    }
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
loc_00ADF2C6:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
loc_00ADF2CC:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
loc_00ADF2D2:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
loc_00ADF2D8:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
loc_00ADF2DE:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
loc_00ADF2E4:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
loc_00ADF2EA:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
loc_00ADF2F0:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
loc_00ADF2F6:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
loc_00ADF2FC:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
loc_00ADF302:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint8_t)((uint8_t)(Arg4)), v_stack_p8);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x10` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ADE6E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
