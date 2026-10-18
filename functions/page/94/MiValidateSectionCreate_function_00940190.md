# MiValidateSectionCreate

- RVA: `0x00940190`–`0x00940D11` (길이 `2,945` bytes)
- VA: `0x0000000140940190`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000901F0`
- 디코드: `555`개 명령, `2,945/2,945` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00940214` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00940330` → [MiMapImageInSystemSpace](MiMapImageInSystemSpace_function_00941DD8.md) (function, `0x00941DD8`)
- `0x0094044D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0094045A` → [MiUnmapImageInSystemSpace](MiUnmapImageInSystemSpace_function_0094206C.md) (function, `0x0094206C`)
- `0x009404E2` → [PsSetSystemPagePriorityThread](../../text/45/PsSetSystemPagePriorityThread_function_00459084.md) (function, `0x00459084`)
- `0x0094052C` → [MiPrefetchControlArea](../93/MiPrefetchControlArea_function_0093E830.md) (function, `0x0093E830`)
- `0x00940598` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x009405F5` → [KeCopyPage](../../text/6B/KeCopyPage_function_006BA0F0.md) (function, `0x006BA0F0`)
- `0x00940619` → [KeZeroSinglePage](../../text/6B/KeZeroSinglePage_function_006BA030.md) (function, `0x006BA030`)
- `0x009407CC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0094082A` → [MiStrongCodeImage](../../text/4B/MiStrongCodeImage_function_004BE728.md) (function, `0x004BE728`)
- `0x0094083D` → [MiRevertRelocations](../93/MiRevertRelocations_function_0093F1D8.md) (function, `0x0093F1D8`)
- `0x00940910` → [MiWriteSegmentSignatureFlags](../../text/4B/MiWriteSegmentSignatureFlags_function_004B78C4.md) (function, `0x004B78C4`)
- `0x00940930` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009409AD` → [PsRevertToUserPagePriorityThread](../../text/46/PsRevertToUserPagePriorityThread_function_00462D40.md) (function, `0x00462D40`)
- `0x009409F2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00940A80` → [MiWalkEntireImage](../../text/36/MiWalkEntireImage_function_00365D70.md) (function, `0x00365D70`)
- `0x00940B4F` → [MiCreatePerSessionProtos](../A6/MiCreatePerSessionProtos_function_00A666D8.md) (function, `0x00A666D8`)
- `0x00940B63` → [PsRevertToUserPagePriorityThread](../../text/46/PsRevertToUserPagePriorityThread_function_00462D40.md) (function, `0x00462D40`)
- `0x00940B7E` → [MiDereferencePerSessionProtos](../A2/MiDereferencePerSessionProtos_function_00A2EDE8.md) (function, `0x00A2EDE8`)
- `0x00940BBD` → [SepScheduleImageVerificationCallbacks](../AA/SepScheduleImageVerificationCallbacks_function_00AA50A8.md) (function, `0x00AA50A8`)
- `0x00940BDB` → [MiImageCantMove](../../text/68/MiImageCantMove_function_0068CAA4.md) (function, `0x0068CAA4`)
- `0x00940C08` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00940C14` → [MiDereferencePerSessionProtos](../A2/MiDereferencePerSessionProtos_function_00A2EDE8.md) (function, `0x00A2EDE8`)
- `0x00940C29` → [MiFlushEntireTbDueToAttributeChange](../../text/30/MiFlushEntireTbDueToAttributeChange_function_00308AE0.md) (function, `0x00308AE0`)
- `0x00940CC3` → [MiCaptureSecureImageBaseAddress](../AA/MiCaptureSecureImageBaseAddress_function_00AA881C.md) (function, `0x00AA881C`)
- `0x00940D07` → [MiStrongCodeImage](../../text/4B/MiStrongCodeImage_function_004BE728.md) (function, `0x004BE728`)

### Direct callers
- [MiPromoteControlAreaToStrongCode](../80/MiPromoteControlAreaToStrongCode_function_0080720C.md) at `0x00807240`
- [MiValidateSectionSigningPolicy](../93/MiValidateSectionSigningPolicy_function_0093FF40.md) at `0x00940002`
- [MiMapImageForEnclaveUse](../AB/MiMapImageForEnclaveUse_function_00AB213C.md) at `0x00AB2237`

### Static image references
- `0x009401A2` → RVA `0x00E0A740` (`.data`; read)
- `0x00940522` → RVA `0x00010880` (`.rdata`; read)
- `0x009406FB` → RVA `0x00F04E60` (`.data`; read)
- `0x00940709` → RVA `0x00E67D68` (`.data`; read)
- `0x00940977` → RVA `0x00E2D7F8` (`.data`; write)
- `0x0094098D` → RVA `0x00FC6A88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x00940214` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0094044D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009404E2` → [PsSetSystemPagePriorityThread](../../text/45/PsSetSystemPagePriorityThread_function_00459084.md) (`PAGE` → `.text`)
  - `0x00940598` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x009405F5` → [KeCopyPage](../../text/6B/KeCopyPage_function_006BA0F0.md) (`PAGE` → `.text`)
  - `0x00940619` → [KeZeroSinglePage](../../text/6B/KeZeroSinglePage_function_006BA030.md) (`PAGE` → `.text`)
  - `0x009407CC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0094082A` → [MiStrongCodeImage](../../text/4B/MiStrongCodeImage_function_004BE728.md) (`PAGE` → `.text`)
  - `0x00940910` → [MiWriteSegmentSignatureFlags](../../text/4B/MiWriteSegmentSignatureFlags_function_004B78C4.md) (`PAGE` → `.text`)
  - `0x00940930` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009409AD` → [PsRevertToUserPagePriorityThread](../../text/46/PsRevertToUserPagePriorityThread_function_00462D40.md) (`PAGE` → `.text`)
  - `0x009409F2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00940A80` → [MiWalkEntireImage](../../text/36/MiWalkEntireImage_function_00365D70.md) (`PAGE` → `.text`)
  - `0x00940B63` → [PsRevertToUserPagePriorityThread](../../text/46/PsRevertToUserPagePriorityThread_function_00462D40.md) (`PAGE` → `.text`)
  - `0x00940BDB` → [MiImageCantMove](../../text/68/MiImageCantMove_function_0068CAA4.md) (`PAGE` → `.text`)
  - `0x00940C08` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00940C29` → [MiFlushEntireTbDueToAttributeChange](../../text/30/MiFlushEntireTbDueToAttributeChange_function_00308AE0.md) (`PAGE` → `.text`)
  - `0x00940D07` → [MiStrongCodeImage](../../text/4B/MiStrongCodeImage_function_004BE728.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x00940B0B` → [sub_00B2542C](../B2/Unknown_function_00B2542C.md) (`tail-transfer`)
  - `0x00940B58` → [sub_00B2542C + 0x9](../B2/Unknown_function_00B2542C.md) (`tail-transfer`)
  - `0x00940B72` → [sub_00B2542C + 0x20](../B2/Unknown_function_00B2542C.md) (`tail-transfer`)
  - `0x00940B84` → [sub_00B2542C + 0x20](../B2/Unknown_function_00B2542C.md) (`tail-transfer`)
  - `0x00940BC4` → [sub_00B2542C + 0x43](../B2/Unknown_function_00B2542C.md) (`tail-transfer`)
  - `0x00940C36` → [sub_00B2542C + 0x55](../B2/Unknown_function_00B2542C.md) (`tail-transfer`)
  - `0x00940C78` → [sub_00B2542C + 0x62](../B2/Unknown_function_00B2542C.md) (`tail-transfer`)
  - `0x00940C85` → [sub_00B2542C + 0x7C](../B2/Unknown_function_00B2542C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00940190  40 53                           push rbx
00940192  56                              push rsi
00940193  41 54                           push r12
00940195  41 55                           push r13
00940197  41 56                           push r14
00940199  41 57                           push r15
0094019B  48 81 EC 18 02 00 00            sub rsp, 0x218
009401A2  48 8B 05 97 A5 4C 00            mov rax, qword ptr [rip + 0x4ca597]
009401A9  48 33 C4                        xor rax, rsp
009401AC  48 89 84 24 00 02 00 00         mov qword ptr [rsp + 0x200], rax
009401B4  49 8B C1                        mov rax, r9
009401B7  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
009401BF  44 89 84 24 E0 00 00 00         mov dword ptr [rsp + 0xe0], r8d
009401C7  4C 8B FA                        mov r15, rdx
009401CA  48 8B F1                        mov rsi, rcx
009401CD  48 89 8C 24 30 01 00 00         mov qword ptr [rsp + 0x130], rcx
009401D5  48 89 8C 24 78 01 00 00         mov qword ptr [rsp + 0x178], rcx
009401DD  48 89 94 24 80 01 00 00         mov qword ptr [rsp + 0x180], rdx
009401E5  44 89 84 24 10 01 00 00         mov dword ptr [rsp + 0x110], r8d
009401ED  48 89 84 24 88 01 00 00         mov qword ptr [rsp + 0x188], rax
009401F5  48 83 A4 24 98 00 00 00 00      and qword ptr [rsp + 0x98], 0
009401FE  C6 84 24 90 00 00 00 00         mov byte ptr [rsp + 0x90], 0
00940206  33 D2                           xor edx, edx
00940208  44 8D 42 50                     lea r8d, [rdx + 0x50]
0094020C  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
00940214  E8 27 6A D8 FF                  call 0x1406c6c40
00940219  33 C0                           xor eax, eax
0094021B  89 84 24 AC 00 00 00            mov dword ptr [rsp + 0xac], eax
00940222  44 8D 70 01                     lea r14d, [rax + 1]
00940226  44 89 B4 24 CC 00 00 00         mov dword ptr [rsp + 0xcc], r14d
0094022E  49 8B 47 60                     mov rax, qword ptr [r15 + 0x60]
00940232  48 83 E0 F8                     and rax, 0xfffffffffffffff8
00940236  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
0094023E  41 8D 5E 05                     lea ebx, [r14 + 5]
00940242  89 9C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ebx
00940249  83 A4 24 A0 00 00 00 00         and dword ptr [rsp + 0xa0], 0
00940251  C6 84 24 A4 00 00 00 00         mov byte ptr [rsp + 0xa4], 0
00940259  83 A4 24 E4 00 00 00 00         and dword ptr [rsp + 0xe4], 0
00940261  83 A4 24 C8 00 00 00 00         and dword ptr [rsp + 0xc8], 0
00940269  45 33 E4                        xor r12d, r12d
0094026C  4C 89 A4 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r12
00940274  49 8D 47 38                     lea rax, [r15 + 0x38]
00940278  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
00940280  F7 00 00 08 00 00               test dword ptr [rax], 0x800
00940286  0F 85 74 08 00 00               jne 0x140940b00
0094028C  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00940290  8B 48 34                        mov ecx, dword ptr [rax + 0x34]
00940293  F6 C1 10                        test cl, 0x10
00940296  8B 8C 24 70 02 00 00            mov ecx, dword ptr [rsp + 0x270]
0094029D  0F 85 82 08 00 00               jne 0x140940b25
009402A3  49 8D 47 3E                     lea rax, [r15 + 0x3e]
009402A7  48 89 84 24 90 01 00 00         mov qword ptr [rsp + 0x190], rax
009402AF  8A 00                           mov al, byte ptr [rax]
009402B1  24 0C                           and al, 0xc
009402B3  8B D1                           mov edx, ecx
009402B5  0F BA EA 18                     bts edx, 0x18
009402B9  3C 04                           cmp al, 4
009402BB  0F 45 D1                        cmovne edx, ecx
009402BE  89 94 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], edx
009402C5  89 94 24 1C 01 00 00            mov dword ptr [rsp + 0x11c], edx
009402CC  0F BA E2 1E                     bt edx, 0x1e
009402D0  0F 82 09 08 00 00               jb 0x140940adf
009402D6  F6 C2 05                        test dl, 5
009402D9  0F 85 4E 08 00 00               jne 0x140940b2d
009402DF  45 33 ED                        xor r13d, r13d
009402E2  44 89 AC 24 C4 00 00 00         mov dword ptr [rsp + 0xc4], r13d
009402EA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009402F3  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
009402FA  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
00940302  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
0094030A  8B C3                           mov eax, ebx
0094030C  41 23 C6                        and eax, r14d
0094030F  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
00940316  89 84 24 18 01 00 00            mov dword ptr [rsp + 0x118], eax
0094031D  0F 85 A8 01 00 00               jne 0x1409404cb
00940323  4C 8D 84 24 B0 01 00 00         lea r8, [rsp + 0x1b0]
0094032B  8B D3                           mov edx, ebx
0094032D  49 8B CF                        mov rcx, r15
00940330  E8 A3 1A 00 00                  call 0x140941dd8
00940335  8B F0                           mov esi, eax
00940337  85 C0                           test eax, eax
00940339  0F 88 30 08 00 00               js 0x140940b6f
0094033F  4C 8B 8C 24 B0 01 00 00         mov r9, qword ptr [rsp + 0x1b0]
00940347  4C 89 8C 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r9
0094034F  4D 8B 17                        mov r10, qword ptr [r15]
00940352  4C 89 94 24 00 01 00 00         mov qword ptr [rsp + 0x100], r10
0094035A  4C 89 94 24 68 01 00 00         mov qword ptr [rsp + 0x168], r10
00940362  48 8B 84 24 28 01 00 00         mov rax, qword ptr [rsp + 0x128]
0094036A  48 83 C0 28                     add rax, 0x28
0094036E  48 89 84 24 98 01 00 00         mov qword ptr [rsp + 0x198], rax
00940376  48 89 84 24 A8 01 00 00         mov qword ptr [rsp + 0x1a8], rax
0094037E  48 8B 18                        mov rbx, qword ptr [rax]
00940381  48 89 9C 24 70 01 00 00         mov qword ptr [rsp + 0x170], rbx
00940389  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
00940391  48 85 DB                        test rbx, rbx
00940394  0F 85 9C 01 00 00               jne 0x140940536
0094039A  45 33 E4                        xor r12d, r12d
0094039D  44 89 A4 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r12d
009403A5  4C 8B 9C 24 B0 01 00 00         mov r11, qword ptr [rsp + 0x1b0]
009403AD  4C 89 9C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r11
009403B5  44 8B AC 24 C0 01 00 00         mov r13d, dword ptr [rsp + 0x1c0]
009403BD  45 8B C5                        mov r8d, r13d
009403C0  41 C1 E0 0C                     shl r8d, 0xc
009403C4  44 89 84 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r8d
009403CC  44 89 84 24 D0 00 00 00         mov dword ptr [rsp + 0xd0], r8d
009403D4  41 8B D0                        mov edx, r8d
009403D7  89 94 24 B4 00 00 00            mov dword ptr [rsp + 0xb4], edx
009403DE  44 88 B4 24 90 00 00 00         mov byte ptr [rsp + 0x90], r14b
009403E6  48 8B 84 24 28 01 00 00         mov rax, qword ptr [rsp + 0x128]
009403EE  48 83 C0 20                     add rax, 0x20
009403F2  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
009403FA  48 8B 00                        mov rax, qword ptr [rax]
009403FD  48 85 C0                        test rax, rax
00940400  74 0E                           je 0x140940410
00940402  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
00940406  48 39 48 28                     cmp qword ptr [rax + 0x28], rcx
0094040A  0F 85 67 01 00 00               jne 0x140940577
00940410  44 39 B4 24 A0 00 00 00         cmp dword ptr [rsp + 0xa0], r14d
00940418  0F 84 82 07 00 00               je 0x140940ba0
0094041E  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
00940425  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
0094042C  85 F6                           test esi, esi
0094042E  0F 89 B6 02 00 00               jns 0x1409406ea
00940434  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
0094043C  48 3B 8C 24 F0 00 00 00         cmp rcx, qword ptr [rsp + 0xf0]
00940444  74 0C                           je 0x140940452
00940446  48 85 C9                        test rcx, rcx
00940449  74 07                           je 0x140940452
0094044B  33 D2                           xor edx, edx
0094044D  E8 1E 24 24 00                  call 0x140b82870
00940452  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
0094045A  E8 0D 1C 00 00                  call 0x14094206c
0094045F  44 8B AC 24 C4 00 00 00         mov r13d, dword ptr [rsp + 0xc4]
00940467  45 85 ED                        test r13d, r13d
0094046A  0F 85 9E 07 00 00               jne 0x140940c0e
00940470  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
00940477  85 C0                           test eax, eax
00940479  0F 85 0E 05 00 00               jne 0x14094098d
0094047F  85 F6                           test esi, esi
00940481  0F 89 DF 03 00 00               jns 0x140940866
00940487  81 FE 23 00 00 C0               cmp esi, 0xc0000023
0094048D  0F 85 E4 04 00 00               jne 0x140940977
00940493  8B 8C 24 D0 00 00 00            mov ecx, dword ptr [rsp + 0xd0]
0094049A  3B 8C 24 A0 00 00 00            cmp ecx, dword ptr [rsp + 0xa0]
009404A1  0F 8D D0 04 00 00               jge 0x140940977
009404A7  8B 9C 24 A8 00 00 00            mov ebx, dword ptr [rsp + 0xa8]
009404AE  4C 8B A4 24 E8 00 00 00         mov r12, qword ptr [rsp + 0xe8]
009404B6  85 C0                           test eax, eax
009404B8  0F 84 7C 05 00 00               je 0x140940a3a
009404BE  44 89 B4 24 CC 00 00 00         mov dword ptr [rsp + 0xcc], r14d
009404C6  E9 3F FE FF FF                  jmp 0x14094030a
009404CB  65 4C 8B 24 25 88 01 00 00      mov r12, qword ptr gs:[0x188]
009404D4  4C 89 A4 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r12
009404DC  41 8B D6                        mov edx, r14d
009404DF  49 8B CC                        mov rcx, r12
009404E2  E8 9D 8B B1 FF                  call 0x140459084
009404E7  8B F0                           mov esi, eax
009404E9  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
009404F0  48 8B 84 24 50 01 00 00         mov rax, qword ptr [rsp + 0x150]
009404F8  F7 00 00 00 00 08               test dword ptr [rax], 0x8000000
009404FE  0F 85 45 06 00 00               jne 0x140940b49
00940504  83 BC 24 CC 00 00 00 00         cmp dword ptr [rsp + 0xcc], 0
0094050C  0F 84 11 FE FF FF               je 0x140940323
00940512  83 4C 24 28 FF                  or dword ptr [rsp + 0x28], 0xffffffff
00940517  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
0094051C  45 8B CE                        mov r9d, r14d
0094051F  45 33 C0                        xor r8d, r8d
00940522  48 8B 15 57 03 6D FF            mov rdx, qword ptr [rip - 0x92fca9]
00940529  49 8B CF                        mov rcx, r15
0094052C  E8 FF E2 FF FF                  call 0x14093e830
00940531  E9 ED FD FF FF                  jmp 0x140940323
00940536  48 8B CB                        mov rcx, rbx
00940539  83 E1 03                        and ecx, 3
0094053C  48 8B C3                        mov rax, rbx
0094053F  48 83 E0 F8                     and rax, 0xfffffffffffffff8
00940543  48 BA F8 FF FF FF FF FF FF 7F   movabs rdx, 0x7ffffffffffffff8
0094054D  48 3B C2                        cmp rax, rdx
00940550  0F 86 71 05 00 00               jbe 0x140940ac7
00940556  48 8B C3                        mov rax, rbx
00940559  48 85 C9                        test rcx, rcx
0094055C  0F 85 27 06 00 00               jne 0x140940b89
00940562  44 8D 61 04                     lea r12d, [rcx + 4]
00940566  48 83 E0 FB                     and rax, 0xfffffffffffffffb
0094056A  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00940572  E9 26 FE FF FF                  jmp 0x14094039d
00940577  83 BC 24 A0 00 00 00 02         cmp dword ptr [rsp + 0xa0], 2
0094057F  0F 85 C3 03 00 00               jne 0x140940948
00940585  44 89 AC 24 D4 00 00 00         mov dword ptr [rsp + 0xd4], r13d
0094058D  B9 00 01 00 00                  mov ecx, 0x100
00940592  41 B8 4D 6D 49 68               mov r8d, 0x68496d4d
00940598  E8 A3 AF A1 FF                  call 0x14035b540
0094059D  4C 8B D8                        mov r11, rax
009405A0  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
009405A8  48 89 84 24 58 01 00 00         mov qword ptr [rsp + 0x158], rax
009405B0  48 85 C0                        test rax, rax
009405B3  0F 84 CA 03 00 00               je 0x140940983
009405B9  33 F6                           xor esi, esi
009405BB  89 B4 24 20 01 00 00            mov dword ptr [rsp + 0x120], esi
009405C2  4C 8B C0                        mov r8, rax
009405C5  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
009405CD  33 C0                           xor eax, eax
009405CF  89 84 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], eax
009405D6  41 3B C5                        cmp eax, r13d
009405D9  0F 83 55 02 00 00               jae 0x140940834
009405DF  C1 E0 0C                        shl eax, 0xc
009405E2  8B C8                           mov ecx, eax
009405E4  48 8B 94 24 F0 00 00 00         mov rdx, qword ptr [rsp + 0xf0]
009405EC  48 03 D1                        add rdx, rcx
009405EF  49 03 C8                        add rcx, r8
009405F2  45 8B C6                        mov r8d, r14d
009405F5  E8 F6 9A D7 FF                  call 0x1406ba0f0
009405FA  4C 8B 9C 24 F8 00 00 00         mov r11, qword ptr [rsp + 0xf8]
00940602  E9 CC 00 00 00                  jmp 0x1409406d3
00940607  8B 8C 24 BC 00 00 00            mov ecx, dword ptr [rsp + 0xbc]
0094060E  C1 E1 0C                        shl ecx, 0xc
00940611  48 03 8C 24 38 01 00 00         add rcx, qword ptr [rsp + 0x138]
00940619  E8 12 9A D7 FF                  call 0x1406ba030
0094061E  41 BE 01 00 00 00               mov r14d, 1
00940624  44 8B A4 24 B0 00 00 00         mov r12d, dword ptr [rsp + 0xb0]
0094062C  4C 8B 9C 24 58 01 00 00         mov r11, qword ptr [rsp + 0x158]
00940634  4C 89 9C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r11
0094063C  8B B4 24 20 01 00 00            mov esi, dword ptr [rsp + 0x120]
00940643  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
0094064B  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
00940653  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
0094065B  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
00940663  48 8B 9C 24 70 01 00 00         mov rbx, qword ptr [rsp + 0x170]
0094066B  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
00940672  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
00940679  44 8B AC 24 D4 00 00 00         mov r13d, dword ptr [rsp + 0xd4]
00940681  48 8B 84 24 78 01 00 00         mov rax, qword ptr [rsp + 0x178]
00940689  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
00940691  4C 8B BC 24 80 01 00 00         mov r15, qword ptr [rsp + 0x180]
00940699  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
009406A0  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
009406A7  48 8B 84 24 88 01 00 00         mov rax, qword ptr [rsp + 0x188]
009406AF  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
009406B7  8B 84 24 D0 00 00 00            mov eax, dword ptr [rsp + 0xd0]
009406BE  89 84 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], eax
009406C5  8B 84 24 1C 01 00 00            mov eax, dword ptr [rsp + 0x11c]
009406CC  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
009406D3  8B 84 24 BC 00 00 00            mov eax, dword ptr [rsp + 0xbc]
009406DA  41 03 C6                        add eax, r14d
009406DD  4C 8B 84 24 38 01 00 00         mov r8, qword ptr [rsp + 0x138]
009406E5  E9 E5 FE FF FF                  jmp 0x1409405cf
009406EA  48 83 A4 24 08 01 00 00 00      and qword ptr [rsp + 0x108], 0
009406F3  83 A4 24 DC 00 00 00 00         and dword ptr [rsp + 0xdc], 0
009406FB  48 83 3D 5D 47 5C 00 00         cmp qword ptr [rip + 0x5c475d], 0
00940703  0F 84 27 03 00 00               je 0x140940a30
00940709  8B 05 59 76 52 00               mov eax, dword ptr [rip + 0x527659]
0094070F  F7 D8                           neg eax
00940711  48 1B C9                        sbb rcx, rcx
00940714  48 8D 84 24 08 01 00 00         lea rax, [rsp + 0x108]
0094071C  48 23 C8                        and rcx, rax
0094071F  48 8D 84 24 DC 00 00 00         lea rax, [rsp + 0xdc]
00940727  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0094072F  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00940734  48 8D 84 24 E4 00 00 00         lea rax, [rsp + 0xe4]
0094073C  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00940741  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00940749  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0094074E  8A 84 24 80 02 00 00            mov al, byte ptr [rsp + 0x280]
00940755  88 44 24 60                     mov byte ptr [rsp + 0x60], al
00940759  8A 84 24 78 02 00 00            mov al, byte ptr [rsp + 0x278]
00940760  88 44 24 58                     mov byte ptr [rsp + 0x58], al
00940764  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
0094076C  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00940771  44 8B AC 24 D8 00 00 00         mov r13d, dword ptr [rsp + 0xd8]
00940779  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
0094077E  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
00940786  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0094078B  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
00940793  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00940798  48 8D 84 24 A4 00 00 00         lea rax, [rsp + 0xa4]
009407A0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009407A5  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
009407AD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009407B2  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
009407B7  44 8B C2                        mov r8d, edx
009407BA  49 8B D3                        mov rdx, r11
009407BD  48 8B 8C 24 30 01 00 00         mov rcx, qword ptr [rsp + 0x130]
009407C5  48 8B 05 94 46 5C 00            mov rax, qword ptr [rip + 0x5c4694]
009407CC  E8 FF A2 D7 FF                  call 0x1406baad0
009407D1  8B F0                           mov esi, eax
009407D3  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
009407DB  48 85 C9                        test rcx, rcx
009407DE  0F 85 EF 01 00 00               jne 0x1409409d3
009407E4  81 FE 2D 01 00 00               cmp esi, 0x12d
009407EA  0F 84 E8 03 00 00               je 0x140940bd8
009407F0  8B 8C 24 AC 00 00 00            mov ecx, dword ptr [rsp + 0xac]
009407F7  81 FE 2E 01 00 00               cmp esi, 0x12e
009407FD  41 0F 44 CE                     cmove ecx, r14d
00940801  89 8C 24 AC 00 00 00            mov dword ptr [rsp + 0xac], ecx
00940808  85 C9                           test ecx, ecx
0094080A  0F 84 24 FC FF FF               je 0x140940434
00940810  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
00940818  8A 00                           mov al, byte ptr [rax]
0094081A  24 0C                           and al, 0xc
0094081C  3C 04                           cmp al, 4
0094081E  0F 84 C9 03 00 00               je 0x140940bed
00940824  41 8B D6                        mov edx, r14d
00940827  49 8B CF                        mov rcx, r15
0094082A  E8 F9 DE B7 FF                  call 0x1404be728
0094082F  E9 00 FC FF FF                  jmp 0x140940434
00940834  45 8B C5                        mov r8d, r13d
00940837  49 8B D7                        mov rdx, r15
0094083A  49 8B CB                        mov rcx, r11
0094083D  E8 96 E9 FF FF                  call 0x14093f1d8
00940842  4C 8B 9C 24 F8 00 00 00         mov r11, qword ptr [rsp + 0xf8]
0094084A  8B 94 24 B4 00 00 00            mov edx, dword ptr [rsp + 0xb4]
00940851  44 8B 84 24 C0 00 00 00         mov r8d, dword ptr [rsp + 0xc0]
00940859  4C 8B 8C 24 F0 00 00 00         mov r9, qword ptr [rsp + 0xf0]
00940861  E9 B8 FB FF FF                  jmp 0x14094041e
00940866  0F 84 52 01 00 00               je 0x1409409be
0094086C  45 3B E6                        cmp r12d, r14d
0094086F  0F 87 87 01 00 00               ja 0x1409409fc
00940875  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
0094087D  48 8B C1                        mov rax, rcx
00940880  48 83 E0 F8                     and rax, 0xfffffffffffffff8
00940884  49 B9 F8 FF FF FF FF FF FF 7F   movabs r9, 0x7ffffffffffffff8
0094088E  49 3B C1                        cmp rax, r9
00940891  0F 87 9C 03 00 00               ja 0x140940c33
00940897  48 C1 E1 03                     shl rcx, 3
0094089B  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
009408A3  4C 8B AC 24 00 01 00 00         mov r13, qword ptr [rsp + 0x100]
009408AB  49 8B 45 38                     mov rax, qword ptr [r13 + 0x38]
009408AF  8A 50 2E                        mov dl, byte ptr [rax + 0x2e]
009408B2  84 D2                           test dl, dl
009408B4  0F 88 8E 03 00 00               js 0x140940c48
009408BA  4C 8B 84 24 98 01 00 00         mov r8, qword ptr [rsp + 0x198]
009408C2  48 8B C3                        mov rax, rbx
009408C5  F0 49 0F B1 08                  lock cmpxchg qword ptr [r8], rcx
009408CA  48 8B D8                        mov rbx, rax
009408CD  0F 85 86 03 00 00               jne 0x140940c59
009408D3  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
009408DB  F6 84 24 98 00 00 00 03         test byte ptr [rsp + 0x98], 3
009408E3  0F 85 76 01 00 00               jne 0x140940a5f
009408E9  85 F6                           test esi, esi
009408EB  78 36                           js 0x140940923
009408ED  41 8A 45 0F                     mov al, byte ptr [r13 + 0xf]
009408F1  8B 94 24 E4 00 00 00            mov edx, dword ptr [rsp + 0xe4]
009408F8  80 E2 07                        and dl, 7
009408FB  C0 E2 04                        shl dl, 4
009408FE  24 80                           and al, 0x80
00940900  0A D0                           or dl, al
00940902  8A 84 24 90 00 00 00            mov al, byte ptr [rsp + 0x90]
00940909  24 0F                           and al, 0xf
0094090B  0A D0                           or dl, al
0094090D  49 8B CD                        mov rcx, r13
00940910  E8 AF 6F B7 FF                  call 0x1404b78c4
00940915  83 BC 24 AC 00 00 00 00         cmp dword ptr [rsp + 0xac], 0
0094091D  0F 85 DC 03 00 00               jne 0x140940cff
00940923  8B C6                           mov eax, esi
00940925  48 8B 8C 24 00 02 00 00         mov rcx, qword ptr [rsp + 0x200]
0094092D  48 33 CC                        xor rcx, rsp
00940930  E8 0B BD D6 FF                  call 0x1406ac640
00940935  48 81 C4 18 02 00 00            add rsp, 0x218
0094093C  41 5F                           pop r15
0094093E  41 5E                           pop r14
00940940  41 5D                           pop r13
00940942  41 5C                           pop r12
00940944  5E                              pop rsi
00940945  5B                              pop rbx
00940946  C3                              ret
00940947  CC                              int3
00940948  49 8B 42 38                     mov rax, qword ptr [r10 + 0x38]
0094094C  8B 48 40                        mov ecx, dword ptr [rax + 0x40]
0094094F  F7 C1 FF 0F 00 00               test ecx, 0xfff
00940955  41 BD 00 00 00 00               mov r13d, 0
0094095B  41 0F 95 C5                     setne r13b
0094095F  C1 E9 0C                        shr ecx, 0xc
00940962  44 03 E9                        add r13d, ecx
00940965  41 8B D5                        mov edx, r13d
00940968  C1 E2 0C                        shl edx, 0xc
0094096B  89 94 24 B4 00 00 00            mov dword ptr [rsp + 0xb4], edx
00940972  E9 0E FC FF FF                  jmp 0x140940585
00940977  C7 05 77 CE 4E 00 75 00 00 00   mov dword ptr [rip + 0x4ece77], 0x75
00940981  EB A0                           jmp 0x140940923
00940983  BE 9A 00 00 C0                  mov esi, 0xc000009a
00940988  E9 BD FE FF FF                  jmp 0x14094084a
0094098D  48 F7 05 F0 60 68 00 00 00 02 00  test qword ptr [rip + 0x6860f0], 0x20000
00940998  0F 85 8B 02 00 00               jne 0x140940c29
0094099E  8B 94 24 C8 00 00 00            mov edx, dword ptr [rsp + 0xc8]
009409A5  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
009409AD  E8 8E 23 B2 FF                  call 0x140462d40
009409B2  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
009409B9  E9 C1 FA FF FF                  jmp 0x14094047f
009409BE  80 BC 24 90 00 00 00 00         cmp byte ptr [rsp + 0x90], 0
009409C6  0F 85 A0 FE FF FF               jne 0x14094086c
009409CC  33 C0                           xor eax, eax
009409CE  E9 52 FF FF FF                  jmp 0x140940925
009409D3  85 F6                           test esi, esi
009409D5  0F 88 D5 01 00 00               js 0x140940bb0
009409DB  45 84 EE                        test r14b, r13b
009409DE  0F 85 CC 01 00 00               jne 0x140940bb0
009409E4  48 85 C9                        test rcx, rcx
009409E7  0F 84 F7 FD FF FF               je 0x1409407e4
009409ED  BA 43 49 73 63                  mov edx, 0x63734943
009409F2  E8 79 1E 24 00                  call 0x140b82870
009409F7  E9 E8 FD FF FF                  jmp 0x1409407e4
009409FC  4C 8B AC 24 00 01 00 00         mov r13, qword ptr [rsp + 0x100]
00940A04  41 83 FC 03                     cmp r12d, 3
00940A08  0F 87 CD FE FF FF               ja 0x1409408db
00940A0E  48 8B CB                        mov rcx, rbx
00940A11  83 E1 03                        and ecx, 3
00940A14  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00940A1C  48 83 E0 FC                     and rax, 0xfffffffffffffffc
00940A20  48 0B C8                        or rcx, rax
00940A23  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
00940A2B  E9 AB FE FF FF                  jmp 0x1409408db
00940A30  BE 28 04 00 C0                  mov esi, 0xc0000428
00940A35  E9 AA FD FF FF                  jmp 0x1409407e4
00940A3A  41 0B DE                        or ebx, r14d
00940A3D  89 9C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ebx
00940A44  44 39 B4 24 A0 00 00 00         cmp dword ptr [rsp + 0xa0], r14d
00940A4C  0F 85 B8 F8 FF FF               jne 0x14094030a
00940A52  83 A4 24 CC 00 00 00 00         and dword ptr [rsp + 0xcc], 0
00940A5A  E9 AB F8 FF FF                  jmp 0x14094030a
00940A5F  48 F7 05 1E 60 68 00 00 20 00 00  test qword ptr [rip + 0x68601e], 0x2000
00940A6A  0F 85 30 02 00 00               jne 0x140940ca0
00940A70  44 8B 8C 24 E0 00 00 00         mov r9d, dword ptr [rsp + 0xe0]
00940A78  45 8B C6                        mov r8d, r14d
00940A7B  33 D2                           xor edx, edx
00940A7D  49 8B CF                        mov rcx, r15
00940A80  E8 EB 52 A2 FF                  call 0x140365d70
00940A85  8B F0                           mov esi, eax
00940A87  85 C0                           test eax, eax
00940A89  0F 88 50 02 00 00               js 0x140940cdf
00940A8F  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
00940A97  48 83 E2 FC                     and rdx, 0xfffffffffffffffc
00940A9B  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
00940AA3  49 8B 45 38                     mov rax, qword ptr [r13 + 0x38]
00940AA7  8A 48 2E                        mov cl, byte ptr [rax + 0x2e]
00940AAA  84 C9                           test cl, cl
00940AAC  0F 88 3C 02 00 00               js 0x140940cee
00940AB2  48 8B C3                        mov rax, rbx
00940AB5  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
00940ABD  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
00940AC2  E9 22 FE FF FF                  jmp 0x1409408e9
00940AC7  45 8B E6                        mov r12d, r14d
00940ACA  44 89 B4 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r14d
00940AD2  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
00940ADA  E9 C6 F8 FF FF                  jmp 0x1409403a5
00940ADF  4D 39 A7 90 00 00 00            cmp qword ptr [r15 + 0x90], r12
00940AE6  0F 85 EA F7 FF FF               jne 0x1409402d6
00940AEC  C7 05 02 CD 4E 00 74 00 00 00   mov dword ptr [rip + 0x4ecd02], 0x74
00940AF6  B8 7B 00 00 C0                  mov eax, 0xc000007b
00940AFB  E9 25 FE FF FF                  jmp 0x140940925
00940B00  8B 8C 24 70 02 00 00            mov ecx, dword ptr [rsp + 0x270]
00940B07  0F BA E1 1E                     bt ecx, 0x1e
00940B0B  0F 83 1B 49 1E 00               jae 0x140b2542c
00940B11  C7 05 DD CC 4E 00 73 00 00 00   mov dword ptr [rip + 0x4eccdd], 0x73
00940B1B  B8 33 04 00 C0                  mov eax, 0xc0000433
00940B20  E9 00 FE FF FF                  jmp 0x140940925
00940B25  83 C9 40                        or ecx, 0x40
00940B28  E9 76 F7 FF FF                  jmp 0x1409402a3
00940B2D  BB 07 00 00 00                  mov ebx, 7
00940B32  89 9C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ebx
00940B39  C7 84 24 A0 00 00 00 02 00 00 00  mov dword ptr [rsp + 0xa0], 2
00940B44  E9 96 F7 FF FF                  jmp 0x1409402df
00940B49  83 CA FF                        or edx, 0xffffffff
00940B4C  49 8B CF                        mov rcx, r15
00940B4F  E8 84 5B 12 00                  call 0x140a666d8
00940B54  8B D8                           mov ebx, eax
00940B56  85 C0                           test eax, eax
00940B58  0F 89 D7 48 1E 00               jns 0x140b25435
00940B5E  8B D6                           mov edx, esi
00940B60  49 8B CC                        mov rcx, r12
00940B63  E8 D8 21 B2 FF                  call 0x140462d40
00940B68  8B C3                           mov eax, ebx
00940B6A  E9 B6 FD FF FF                  jmp 0x140940925
00940B6F  45 85 ED                        test r13d, r13d
00940B72  0F 84 D4 48 1E 00               je 0x140b2544c
00940B78  83 CA FF                        or edx, 0xffffffff
00940B7B  49 8B CF                        mov rcx, r15
00940B7E  E8 65 E2 0E 00                  call 0x140a2ede8
00940B83  90                              nop
00940B84  E9 C3 48 1E 00                  jmp 0x140b2544c
00940B89  48 83 E0 FC                     and rax, 0xfffffffffffffffc
00940B8D  45 33 E4                        xor r12d, r12d
00940B90  49 3B CE                        cmp rcx, r14
00940B93  41 0F 95 C4                     setne r12b
00940B97  41 83 C4 02                     add r12d, 2
00940B9B  E9 C6 F9 FF FF                  jmp 0x140940566
00940BA0  C7 84 24 A0 00 00 00 02 00 00 00  mov dword ptr [rsp + 0xa0], 2
00940BAB  E9 6E F8 FF FF                  jmp 0x14094041e
00940BB0  45 8B CD                        mov r9d, r13d
00940BB3  44 8B C6                        mov r8d, esi
00940BB6  8B 94 24 DC 00 00 00            mov edx, dword ptr [rsp + 0xdc]
00940BBD  E8 E6 44 16 00                  call 0x140aa50a8
00940BC2  85 C0                           test eax, eax
00940BC4  0F 88 A5 48 1E 00               js 0x140b2546f
00940BCA  48 83 A4 24 08 01 00 00 00      and qword ptr [rsp + 0x108], 0
00940BD3  E9 0C FC FF FF                  jmp 0x1409407e4
00940BD8  49 8B CF                        mov rcx, r15
00940BDB  E8 C4 BE D4 FF                  call 0x14068caa4
00940BE0  44 89 B4 24 AC 00 00 00         mov dword ptr [rsp + 0xac], r14d
00940BE8  E9 23 FC FF FF                  jmp 0x140940810
00940BED  4C 63 CE                        movsxd r9, esi
00940BF0  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00940BF6  4C 8B 84 24 30 01 00 00         mov r8, qword ptr [rsp + 0x130]
00940BFE  BA 0E 15 05 00                  mov edx, 0x5150e
00940C03  B9 1A 00 00 00                  mov ecx, 0x1a
00940C08  E8 53 CA BB FF                  call 0x1404fd660
00940C0D  CC                              int3
00940C0E  83 CA FF                        or edx, 0xffffffff
00940C11  49 8B CF                        mov rcx, r15
00940C14  E8 CF E1 0E 00                  call 0x140a2ede8
00940C19  45 33 ED                        xor r13d, r13d
00940C1C  44 89 AC 24 C4 00 00 00         mov dword ptr [rsp + 0xc4], r13d
00940C24  E9 47 F8 FF FF                  jmp 0x140940470
00940C29  E8 B2 7E 9C FF                  call 0x140308ae0
00940C2E  E9 6B FD FF FF                  jmp 0x14094099e
00940C33  45 85 E4                        test r12d, r12d
00940C36  0F 85 45 48 1E 00               jne 0x140b25481
00940C3C  48 83 E1 FD                     and rcx, 0xfffffffffffffffd
00940C40  49 0B CE                        or rcx, r14
00940C43  E9 53 FC FF FF                  jmp 0x14094089b
00940C48  48 83 C9 04                     or rcx, 4
00940C4C  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
00940C54  E9 61 FC FF FF                  jmp 0x1409408ba
00940C59  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00940C61  48 8B D1                        mov rdx, rcx
00940C64  48 C1 EA 03                     shr rdx, 3
00940C68  48 B8 FF FF FF FF FF FF FF 0F   movabs rax, 0xfffffffffffffff
00940C72  48 3B D0                        cmp rdx, rax
00940C75  48 8B C3                        mov rax, rbx
00940C78  0F 86 10 48 1E 00               jbe 0x140b2548e
00940C7E  48 83 E0 F8                     and rax, 0xfffffffffffffff8
00940C82  49 3B C1                        cmp rax, r9
00940C85  0F 87 1D 48 1E 00               ja 0x140b254a8
00940C8B  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
00940C8F  48 83 C9 02                     or rcx, 2
00940C93  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
00940C9B  E9 22 FC FF FF                  jmp 0x1409408c2
00940CA0  41 F7 47 5C 00 00 0C 00         test dword ptr [r15 + 0x5c], 0xc0000
00940CA8  0F 84 C2 FD FF FF               je 0x140940a70
00940CAE  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
00940CB6  48 83 38 00                     cmp qword ptr [rax], 0
00940CBA  0F 84 B0 FD FF FF               je 0x140940a70
00940CC0  49 8B CF                        mov rcx, r15
00940CC3  E8 54 7B 16 00                  call 0x140aa881c
00940CC8  85 C0                           test eax, eax
00940CCA  0F 89 A0 FD FF FF               jns 0x140940a70
00940CD0  C7 05 1E CB 4E 00 76 00 00 00   mov dword ptr [rip + 0x4ecb1e], 0x76
00940CDA  E9 46 FC FF FF                  jmp 0x140940925
00940CDF  C7 05 0F CB 4E 00 77 00 00 00   mov dword ptr [rip + 0x4ecb0f], 0x77
00940CE9  E9 37 FC FF FF                  jmp 0x140940925
00940CEE  48 83 CA 04                     or rdx, 4
00940CF2  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
00940CFA  E9 B3 FD FF FF                  jmp 0x140940ab2
00940CFF  BA 02 00 00 00                  mov edx, 2
00940D04  49 8B CF                        mov rcx, r15
00940D07  E8 1C DA B7 FF                  call 0x1404be728
00940D0C  E9 12 FC FF FF                  jmp 0x140940923
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiValidateSectionCreate(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, unsigned __int8 a6, unsigned __int8 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned int v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m164;
    unsigned int v_stack_m168;
    unsigned int v_stack_m16C;
    unsigned int v_stack_m170;
    unsigned int v_stack_m174;
    unsigned int v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned int v_stack_m184;
    unsigned int v_stack_m188;
    unsigned int v_stack_m18C;
    unsigned int v_stack_m190;
    unsigned int v_stack_m194;
    unsigned int v_stack_m198;
    unsigned int v_stack_m19C;
    unsigned int v_stack_m1A0;
    unsigned __int8 v_stack_m1A4;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int8 v_stack_m1B8;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int8 v_stack_m1E8;
    unsigned __int8 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned int v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned int v_stack_m220;
    unsigned int v_stack_m228;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p1A0;
    unsigned __int64 v_stack_p1A8;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned int v_stack_pA0;
    unsigned int v_stack_pA8;
    unsigned int v_stack_pAC;
    unsigned int v_stack_pB0;
    unsigned int v_stack_pB4;
    unsigned int v_stack_pB8;
    unsigned int v_stack_pC4;
    unsigned int v_stack_pC8;
    unsigned int v_stack_pCC;
    unsigned int v_stack_pDC;
    unsigned int v_stack_pE0;
    unsigned __int64 v_stack_pE8;

    v_rsp = (v_rsp) - (536);
    result = (*(unsigned __int64 *)(v_rip + 5023127)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m108 = a4;
    v_stack_m168 = a3;
    v_stack_m118 = a1;
    v_stack_mD0 = a1;
    v_stack_mC8 = a2;
    v_stack_m138 = a3;
    v_stack_mC0 = a4;
    v_stack_m1B8 = 0;
    a2 = 0;
    result = memset(v_stack_m98, a2, a2 + 80, a4);
    result = 0;
    v_stack_m19C = 0;
    v_stack_m17C = (unsigned int)(result + 1);
    result = (*(unsigned __int64 *)(a2 + 96)) & (-8);
    v_stack_m120 = result;
    v_stack_m1A0 = (unsigned int)(result + 1 + 5);
    v_stack_m1A4 = 0;
    v_r12 = 0;
    v_stack_m160 = 0;
    v_stack_mF8 = a2 + 56;
    if (((*(unsigned int *)(a2 + 56)) & (0x800ULL)) != 0) goto loc_00940B00;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 52)))) & (16)) != 0) goto loc_00940B25;
loc_009402A3:
    v_stack_mB8 = a2 + 62;
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 + 62)) & (12));
    a2 = (unsigned int)((unsigned int)((unsigned int)(a5)));
    if (((unsigned __int8)(result)) != 4) { a2 = (unsigned int)((unsigned int)(a5)); }
    v_stack_m170 = (unsigned int)(a2);
    v_stack_m12C = (unsigned int)(a2);
    if (((unsigned __int8)(result)) < 4) goto loc_00940ADF;
loc_009402D6:
    if ((((unsigned __int8)(a2)) & (5)) != 0) goto loc_00940B2D;
loc_009402DF:
    v_r13 = 0;
    v_stack_m184 = 0;
    v_stack_m100 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_mE8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
loc_0094030A:
    result = (unsigned int)(((unsigned int)((unsigned int)(result + 1 + 5))) & ((unsigned int)(result + 1)));
    v_stack_m190 = (unsigned int)(result);
    v_stack_m130 = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_009404CB;
loc_00940323:
    result = MiMapImageInSystemSpace(a2, (unsigned int)((unsigned int)(result + 1 + 5)), v_stack_m98, a4);
    if (sign_flag) goto loc_00940B6F;
    v_stack_m158 = v_stack_m98;
    v_stack_m148 = *(unsigned __int64 *)(a2);
    v_stack_mE0 = *(unsigned __int64 *)(a2);
    result = (v_stack_m120) + (40);
    v_stack_mB0 = result;
    v_stack_mA0 = result;
    v_stack_mD8 = *(unsigned __int64 *)(result);
    v_stack_m1B0 = *(unsigned __int64 *)(result);
    if (*(unsigned __int64 *)(result) != 0) goto loc_00940536;
    v_r12 = 0;
loc_0094039D:
    v_stack_m198 = 0;
loc_009403A5:
    v_stack_m150 = v_stack_m98;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m88)))) << (12));
    v_stack_m188 = a3;
    v_stack_m178 = a3;
    v_stack_m194 = (unsigned int)((unsigned int)(a3));
    v_stack_m1B8 = (unsigned __int8)(result + 1);
    result = (v_stack_m120) + (32);
    v_stack_mA8 = result;
    if (*(unsigned __int64 *)(result) == 0) goto loc_00940410;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 40)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 48))) goto loc_00940577;
loc_00940410:
    if (v_stack_m1A8 == ((unsigned int)(result + 1))) goto loc_00940BA0;
loc_0094041E:
    v_stack_m178 = (unsigned int)((unsigned int)(v_stack_m1A8));
    if (!sign_flag) goto loc_009406EA;
loc_00940434:
    if (v_stack_m150 == v_stack_m158) goto loc_00940452;
    result = (unsigned int)(v_stack_m1A8);
    if (v_stack_m150 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m150, a2, a3, v_stack_m98);
    }
    result = MiUnmapImageInSystemSpace(v_stack_m98, a2, a3, v_stack_m98);
    if ((unsigned int)((unsigned int)(v_stack_m184)) != 0) goto loc_00940C0E;
loc_00940470:
    if ((unsigned int)((unsigned int)(v_stack_m190)) != 0) goto loc_0094098D;
loc_0094047F:
    if (!sign_flag) goto loc_00940866;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC0000023ULL) goto loc_00940977;
    if (((unsigned int)((unsigned int)(v_stack_m178))) >= v_stack_m1A8) goto loc_00940977;
    if ((unsigned int)((unsigned int)(v_stack_m190)) == 0) goto loc_00940A3A;
    v_stack_m17C = (unsigned int)(result + 1);
    goto loc_0094030A;
loc_009404CB:
    v_stack_m160 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = PsSetSystemPagePriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)((unsigned int)(result + 1)), a3, v_stack_m98);
    v_stack_m180 = (unsigned int)(result);
    if (((*(unsigned int *)(v_stack_mF8)) & (0x8000000ULL)) != 0) goto loc_00940B49;
    if (v_stack_m17C == 0) goto loc_00940323;
    a3 = 0;
    result = MiPrefetchControlArea(0, *(unsigned __int64 *)(v_rip - 9632937), a3, (unsigned int)((unsigned int)(result + 1)));
    goto loc_00940323;
loc_00940536:
    a1 = (unsigned int)(((unsigned int)(v_stack_m1A0)) & (3));
    result = ((unsigned int)(v_stack_m1A0)) & (-8);
    if (result <= (*(unsigned __int64 *)(v_rip - 9632937))) goto loc_00940AC7;
    if (a1 != 0) goto loc_00940B89;
loc_00940566:
    result = ((unsigned int)(v_stack_m1A0)) & (-5);
    v_stack_m1B0 = result;
    goto loc_0094039D;
loc_00940577:
    if (v_stack_m1A8 != 2) goto loc_00940948;
loc_00940585:
    v_stack_m174 = (unsigned int)((unsigned int)(v_stack_m184));
    result = MiAllocatePool(256, *(unsigned __int64 *)(v_rip - 9632937), (unsigned int)(0x68496D4DULL), (unsigned int)((unsigned int)(result + 1)));
    v_stack_m150 = result;
    v_stack_mF0 = result;
    if (result == 0) goto loc_00940983;
    v_rsi = 0;
    v_stack_m128 = 0;
    v_stack_m110 = result;
    result = 0;
loc_009405CF:
    v_stack_m18C = 0;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m184)))) goto loc_00940834;
    result = (unsigned int)((result) << (12));
    a2 = (v_stack_m158) + ((unsigned int)((unsigned int)(result)));
    a1 = ((unsigned int)((unsigned int)(result))) + (result);
    result = KeCopyPage(a1, a2, (unsigned int)((unsigned int)(result + 1)), (unsigned int)((unsigned int)(result + 1)));
    goto loc_009406D3;
loc_009406D3:
    result = (unsigned int)(((unsigned int)(v_stack_m18C)) + ((unsigned int)(result + 1)));
    goto loc_009405CF;
loc_009406EA:
    if ((*(unsigned __int64 *)(v_rip + 6047581)) == 0) goto loc_00940A30;
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rip + 5404249))));
    a1 = (a1) & (v_stack_m140);
    v_stack_m1C8 = v_stack_m16C;
    v_stack_m1D0 = a1;
    v_stack_m1D8 = v_stack_m164;
    v_stack_m1E0 = v_stack_m1B8;
    v_stack_m1E8 = a7;
    v_stack_m1F0 = a6;
    v_stack_m1F8 = v_stack_m1B0;
    v_stack_m200 = (unsigned int)((unsigned int)(v_stack_m170));
    v_stack_m208 = v_stack_m108;
    v_stack_m210 = v_stack_m100;
    v_stack_m218 = v_stack_m1A4;
    v_stack_m220 = v_stack_m1A8;
    v_stack_m228 = (unsigned int)(v_stack_m110);
    result = guard_dispatch_icall(v_stack_m118, v_stack_m150, (unsigned int)((unsigned int)(a2)), (unsigned int)((unsigned int)(result + 1)));
    if (v_stack_m140 != 0) goto loc_009409D3;
loc_009407E4:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 301) goto loc_00940BD8;
    a1 = (unsigned int)(v_stack_m19C);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 302) { a1 = (unsigned int)(result + 1); }
    v_stack_m19C = (unsigned int)(a1);
    if ((unsigned int)(a1) == 0) goto loc_00940434;
loc_00940810:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_mB8)) & (12));
    if (((unsigned __int8)(result)) == 4) goto loc_00940BED;
    result = MiStrongCodeImage(a2, (unsigned int)((unsigned int)(result + 1)), (unsigned int)((unsigned int)(a2)), (unsigned int)((unsigned int)(result + 1)));
    goto loc_00940434;
loc_00940834:
    result = MiRevertRelocations(v_stack_m150, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m170))), (unsigned int)((unsigned int)(result + 1)));
loc_0094084A:
    goto loc_0094041E;
loc_00940866:
    if (((unsigned __int8)(result)) == 4) goto loc_009409BE;
loc_0094086C:
    if (((unsigned int)(a1 + 4)) > ((unsigned int)(result + 1))) goto loc_009409FC;
    result = (v_stack_m1B0) & (-8);
    if (result > v_stack_m158) goto loc_00940C33;
    a1 = (v_stack_m1B0) << (3);
loc_0094089B:
    v_stack_m1B0 = a1;
    if (sign_flag) goto loc_00940C48;
loc_009408BA:
loc_009408C2:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m148 + 56) + 46)) != 0) goto loc_00940C59;
loc_009408DB:
    if (((v_stack_m1B0) & (3)) != 0) goto loc_00940A5F;
loc_009408E9:
    if (sign_flag) goto loc_00940923;
    a2 = (unsigned __int8)(((unsigned int)(v_stack_m164)) & (7));
    a2 = (unsigned __int8)((a2) << (4));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m148 + 15)) & (128));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
    result = (unsigned __int8)((v_stack_m1B8) & (15));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
    result = MiWriteSegmentSignatureFlags(v_stack_m148, a2, v_stack_mB0, v_stack_m158);
    if (v_stack_m19C != 0) goto loc_00940CFF;
loc_00940923:
loc_00940925:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_mB0, v_stack_m158);
    v_rsp = (v_rsp) + (536);
    return result;
loc_00940948:
    v_r13 = ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 56) + 64)))) & (0xFFFULL)) != 0) ? 1 : 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 56) + 64))) >> (12));
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)(a1)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) << (12));
    v_stack_pB4 = (unsigned int)(a2);
    goto loc_00940585;
loc_00940977:
    *(unsigned int *)(v_rip + 5164663) = 117;
    goto loc_00940923;
loc_00940983:
    goto loc_0094084A;
loc_0094098D:
    if (((*(unsigned __int64 *)(v_rip + 6840560)) & (0x20000ULL)) != 0) goto loc_00940C29;
loc_0094099E:
    result = PsRevertToUserPagePriorityThread(v_stack_pE8, (unsigned int)(v_stack_pC8), v_stack_mB0, v_stack_m158);
    goto loc_0094047F;
loc_009409BE:
    if (v_stack_p90 != 0) goto loc_0094086C;
    result = 0;
    goto loc_00940925;
loc_009409D3:
    if (sign_flag) goto loc_00940BB0;
    if ((((unsigned __int8)(result + 1)) & ((unsigned __int8)(v_r13))) != 0) goto loc_00940BB0;
    if (v_stack_pE8 == 0) goto loc_009407E4;
    result = ExFreePoolWithTag(v_stack_pE8, (unsigned int)(0x63734943ULL), v_stack_mB0, v_stack_m158);
    goto loc_009407E4;
loc_009409FC:
    if (((unsigned int)(a1 + 4)) > 3) goto loc_009408DB;
    a1 = (unsigned int)((v_stack_m1B0) & (3));
    result = (v_stack_p98) & (-4);
    a1 = (a1) | (result);
    v_stack_p98 = a1;
    goto loc_009408DB;
loc_00940A30:
    goto loc_009407E4;
loc_00940A3A:
    v_rbx = (unsigned int)((v_stack_m1B0) | ((unsigned int)(result + 1)));
    v_stack_pA8 = (unsigned int)(v_rbx);
    if (v_stack_pA0 != ((unsigned int)(result + 1))) goto loc_0094030A;
    goto loc_0094030A;
loc_00940A5F:
    if (((*(unsigned __int64 *)(v_rip + 6840350)) & (0x2000ULL)) != 0) goto loc_00940CA0;
loc_00940A70:
    a2 = 0;
    result = MiWalkEntireImage(0, a2, (unsigned int)((unsigned int)(result + 1)), (unsigned int)(v_stack_pE0));
    if (sign_flag) goto loc_00940CDF;
    a2 = (v_stack_p98) & (-4);
    v_stack_p98 = a2;
    if (sign_flag) goto loc_00940CEE;
loc_00940AB2:
    goto loc_009408E9;
loc_00940AC7:
    v_stack_pB0 = (unsigned int)(result + 1);
    v_stack_p98 = v_stack_p1A8;
    goto loc_009403A5;
loc_00940ADF:
    if ((*(unsigned __int64 *)(a2 + 144)) != ((unsigned int)((unsigned int)(result + 1)))) goto loc_009402D6;
    *(unsigned int *)(v_rip + 5164290) = 116;
    goto loc_00940925;
loc_00940B00:
    *(unsigned int *)(v_rip + 5164253) = 115;
    goto loc_00940925;
loc_00940B25:
    a1 = (unsigned int)(((unsigned int)(a5)) | (64));
    goto loc_009402A3;
loc_00940B2D:
    v_stack_pA8 = 7;
    v_stack_pA0 = 2;
    goto loc_009402DF;
loc_00940B49:
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    result = MiCreatePerSessionProtos(a2, a2, (unsigned int)((unsigned int)(result + 1)), (unsigned int)(v_stack_pE0));
    result = PsRevertToUserPagePriorityThread((unsigned int)((unsigned int)(result + 1)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)(result + 1)), (unsigned int)(v_stack_pE0));
    goto loc_00940925;
loc_00940B6F:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) | (0xFFFFFFFFULL));
    result = MiDereferencePerSessionProtos(a2, a2, (unsigned int)((unsigned int)(result + 1)), (unsigned int)(v_stack_pE0));
loc_00940B89:
    result = (result) & (-4);
    v_r12 = 0;
    v_r12 = (a2 != (result + 1)) ? 1 : 0;
    v_r12 = (unsigned int)((v_r12) + (2));
    goto loc_00940566;
loc_00940BA0:
    v_stack_pA0 = 2;
    goto loc_0094041E;
loc_00940BB0:
    result = SepScheduleImageVerificationCallbacks(a2, (unsigned int)(v_stack_pDC), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)(v_stack_p100)));
    goto loc_009407E4;
loc_00940BD8:
    result = MiImageCantMove(a2, (unsigned int)(v_stack_pDC), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)(v_stack_p100)));
    v_stack_pAC = (unsigned int)(result + 1);
    goto loc_00940810;
loc_00940BED:
    result = KeBugCheckEx(26, (unsigned int)(0x5150EULL), v_stack_p130, (int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_00940C0E:
    a2 = (unsigned int)(((unsigned int)(0x5150EULL)) | (0xFFFFFFFFULL));
    result = MiDereferencePerSessionProtos(a2, a2, v_stack_p130, (int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    v_r13 = 0;
    v_stack_pC4 = 0;
    goto loc_00940470;
loc_00940C29:
    result = MiFlushEntireTbDueToAttributeChange(a2, a2, v_stack_p130, (int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_0094099E;
loc_00940C33:
    a1 = (a2) & (-3);
    a1 = (a1) | (result + 1);
    goto loc_0094089B;
loc_00940C48:
    a1 = (a1) | (4);
    v_stack_p98 = a1;
    goto loc_009408BA;
loc_00940C59:
    a2 = (v_stack_p98) >> (3);
    result = ((unsigned int)((unsigned int)(result))) & (-8);
    a1 = (v_stack_p98) & (-2);
    a1 = (a1) | (2);
    v_stack_p98 = a1;
    goto loc_009408C2;
loc_00940CA0:
    if (((*(unsigned int *)(a2 + 92)) & (0xC0000ULL)) == 0) goto loc_00940A70;
    if ((*(unsigned __int64 *)(v_stack_p1A0)) == 0) goto loc_00940A70;
    result = MiCaptureSecureImageBaseAddress(a2, a2, v_stack_p130, (int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (!sign_flag) goto loc_00940A70;
    *(unsigned int *)(v_rip + 5163806) = 118;
    goto loc_00940925;
loc_00940CDF:
    *(unsigned int *)(v_rip + 5163791) = 119;
    goto loc_00940925;
loc_00940CEE:
    a2 = (a2) | (4);
    v_stack_p98 = a2;
    goto loc_00940AB2;
loc_00940CFF:
    result = MiStrongCodeImage(a2, 2, v_stack_p130, (int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_00940923;
}
```

## 5. (Beta) C Style

```c
int64_t MiValidateSectionCreate(void *Arg1, void *Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint8_t Arg6, uint8_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint32_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m164;
    uint32_t v_stack_m168;
    uint32_t v_stack_m16C;
    uint32_t v_stack_m170;
    uint32_t v_stack_m174;
    uint32_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint32_t v_stack_m184;
    uint32_t v_stack_m188;
    uint32_t v_stack_m18C;
    uint32_t v_stack_m190;
    uint32_t v_stack_m194;
    uint32_t v_stack_m198;
    uint32_t v_stack_m19C;
    uint32_t v_stack_m1A0;
    uint8_t v_stack_m1A4;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint8_t v_stack_m1B8;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint8_t v_stack_m1E8;
    uint8_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint32_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint32_t v_stack_m220;
    uint32_t v_stack_m228;
    uint64_t v_stack_m48;
    uint32_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p100;
    uint64_t v_stack_p108;
    uint64_t v_stack_p130;
    uint64_t v_stack_p1A0;
    uint64_t v_stack_p1A8;
    uint64_t v_stack_p20;
    uint8_t v_stack_p90;
    uint64_t v_stack_p98;
    uint32_t v_stack_pA0;
    uint32_t v_stack_pA8;
    uint32_t v_stack_pAC;
    uint32_t v_stack_pB0;
    uint32_t v_stack_pB4;
    uint32_t v_stack_pB8;
    uint32_t v_stack_pC4;
    uint32_t v_stack_pC8;
    uint32_t v_stack_pCC;
    uint32_t v_stack_pDC;
    uint32_t v_stack_pE0;
    uint64_t v_stack_pE8;

    local_rsp = (local_rsp) - (536);
    result = (*(uint64_t *)(v_rip + 0x4CA597)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m108 = Arg4;
    v_stack_m168 = Arg3;
    v_stack_m118 = Arg1;
    v_stack_mD0 = Arg1;
    v_stack_mC8 = Arg2;
    v_stack_m138 = Arg3;
    v_stack_mC0 = Arg4;
    v_stack_m1B8 = 0;
    Arg2 = 0;
    result = memset(v_stack_m98, Arg2, Arg2 + 80, Arg4);
    result = 0;
    v_stack_m19C = 0;
    v_stack_m17C = (uint32_t)(result + 1);
    result = (*(uint64_t *)(arg2 + 0x60)) & (-8);
    v_stack_m120 = result;
    v_stack_m1A0 = (uint32_t)(result + 1 + 5);
    v_stack_m1A4 = 0;
    local_r12 = 0;
    v_stack_m160 = 0;
    v_stack_mF8 = Arg2 + 56;
    if (((*(uint32_t *)(arg2 + 0x38)) & (0x800ULL)) != 0) goto loc_00940B00;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x34)))) & (16)) != 0) goto loc_00940B25;
loc_009402A3:
    v_stack_mB8 = Arg2 + 62;
    result = (uint8_t)((*(uint8_t *)(arg2 + 0x3E)) & (12));
    Arg2 = (uint32_t)((uint32_t)((uint32_t)(Arg5)));
    if (((uint8_t)(result)) != 4) { Arg2 = (uint32_t)((uint32_t)(Arg5)); }
    v_stack_m170 = (uint32_t)(Arg2);
    v_stack_m12C = (uint32_t)(Arg2);
    if (((uint8_t)(result)) < 4) goto loc_00940ADF;
loc_009402D6:
    if ((((uint8_t)(Arg2)) & (5)) != 0) goto loc_00940B2D;
loc_009402DF:
    local_r13 = 0;
    v_stack_m184 = 0;
    v_stack_m100 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_mE8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
loc_0094030A:
    result = (uint32_t)(((uint32_t)((uint32_t)(result + 1 + 5))) & ((uint32_t)(result + 1)));
    v_stack_m190 = (uint32_t)(result);
    v_stack_m130 = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_009404CB;
loc_00940323:
    result = MiMapImageInSystemSpace(Arg2, (uint32_t)((uint32_t)(result + 1 + 5)), v_stack_m98, Arg4);
    if (sign_flag) goto loc_00940B6F;
    v_stack_m158 = v_stack_m98;
    v_stack_m148 = *(uint64_t *)(arg2);
    v_stack_mE0 = *(uint64_t *)(arg2);
    result = (v_stack_m120) + (40);
    v_stack_mB0 = result;
    v_stack_mA0 = result;
    v_stack_mD8 = *(uint64_t *)(result);
    v_stack_m1B0 = *(uint64_t *)(result);
    if (*(uint64_t *)(result) != 0) goto loc_00940536;
    local_r12 = 0;
loc_0094039D:
    v_stack_m198 = 0;
loc_009403A5:
    v_stack_m150 = v_stack_m98;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m88)))) << (12));
    v_stack_m188 = Arg3;
    v_stack_m178 = Arg3;
    v_stack_m194 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m1B8 = (uint8_t)(result + 1);
    result = (v_stack_m120) + (32);
    v_stack_mA8 = result;
    if (*(uint64_t *)(result) == 0) goto loc_00940410;
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x28)) != (*(uint64_t *)(*(uint64_t *)(result) + 0x30))) goto loc_00940577;
loc_00940410:
    if (v_stack_m1A8 == ((uint32_t)(result + 1))) goto loc_00940BA0;
loc_0094041E:
    v_stack_m178 = (uint32_t)((uint32_t)(v_stack_m1A8));
    if (!sign_flag) goto loc_009406EA;
loc_00940434:
    if (v_stack_m150 == v_stack_m158) goto loc_00940452;
    result = (uint32_t)(v_stack_m1A8);
    if (v_stack_m150 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m150, Arg2, Arg3, v_stack_m98);
    }
    result = MiUnmapImageInSystemSpace(v_stack_m98, Arg2, Arg3, v_stack_m98);
    if ((uint32_t)((uint32_t)(v_stack_m184)) != 0) goto loc_00940C0E;
loc_00940470:
    if ((uint32_t)((uint32_t)(v_stack_m190)) != 0) goto loc_0094098D;
loc_0094047F:
    if (!sign_flag) goto loc_00940866;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC0000023ULL) goto loc_00940977;
    if (((uint32_t)((uint32_t)(v_stack_m178))) >= v_stack_m1A8) goto loc_00940977;
    if ((uint32_t)((uint32_t)(v_stack_m190)) == 0) goto loc_00940A3A;
    v_stack_m17C = (uint32_t)(result + 1);
    goto loc_0094030A;
loc_009404CB:
    v_stack_m160 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = PsSetSystemPagePriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)((uint32_t)(result + 1)), Arg3, v_stack_m98);
    v_stack_m180 = (uint32_t)(result);
    if (((*(uint32_t *)(v_stack_mF8)) & (0x8000000ULL)) != 0) goto loc_00940B49;
    if (v_stack_m17C == 0) goto loc_00940323;
    Arg3 = 0;
    result = MiPrefetchControlArea(0, *(uint64_t *)(v_rip - 0x92FCA9), Arg3, (uint32_t)((uint32_t)(result + 1)));
    goto loc_00940323;
loc_00940536:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m1A0)) & (3));
    result = ((uint32_t)(v_stack_m1A0)) & (-8);
    if (result <= (*(uint64_t *)(v_rip - 0x92FCA9))) goto loc_00940AC7;
    if (Arg1 != NULL) goto loc_00940B89;
loc_00940566:
    result = ((uint32_t)(v_stack_m1A0)) & (-5);
    v_stack_m1B0 = result;
    goto loc_0094039D;
loc_00940577:
    if (v_stack_m1A8 != 2) goto loc_00940948;
loc_00940585:
    v_stack_m174 = (uint32_t)((uint32_t)(v_stack_m184));
    result = MiAllocatePool(256, *(uint64_t *)(v_rip - 0x92FCA9), (uint32_t)(0x68496D4DULL), (uint32_t)((uint32_t)(result + 1)));
    v_stack_m150 = result;
    v_stack_mF0 = result;
    if (result == 0) goto loc_00940983;
    local_rsi = 0;
    v_stack_m128 = 0;
    v_stack_m110 = result;
    result = 0;
loc_009405CF:
    v_stack_m18C = 0;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m184)))) goto loc_00940834;
    result = (uint32_t)((result) << (12));
    Arg2 = (v_stack_m158) + ((uint32_t)((uint32_t)(result)));
    Arg1 = ((uint32_t)((uint32_t)(result))) + (result);
    result = KeCopyPage(Arg1, Arg2, (uint32_t)((uint32_t)(result + 1)), (uint32_t)((uint32_t)(result + 1)));
    goto loc_009406D3;
loc_009406D3:
    result = (uint32_t)(((uint32_t)(v_stack_m18C)) + ((uint32_t)(result + 1)));
    goto loc_009405CF;
loc_009406EA:
    if ((*(uint64_t *)(v_rip + 0x5C475D)) == 0) goto loc_00940A30;
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_rip + 0x527659))));
    Arg1 = (Arg1) & (v_stack_m140);
    v_stack_m1C8 = v_stack_m16C;
    v_stack_m1D0 = Arg1;
    v_stack_m1D8 = v_stack_m164;
    v_stack_m1E0 = v_stack_m1B8;
    v_stack_m1E8 = Arg7;
    v_stack_m1F0 = Arg6;
    v_stack_m1F8 = v_stack_m1B0;
    v_stack_m200 = (uint32_t)((uint32_t)(v_stack_m170));
    v_stack_m208 = v_stack_m108;
    v_stack_m210 = v_stack_m100;
    v_stack_m218 = v_stack_m1A4;
    v_stack_m220 = v_stack_m1A8;
    v_stack_m228 = (uint32_t)(v_stack_m110);
    result = guard_dispatch_icall(v_stack_m118, v_stack_m150, (uint32_t)((uint32_t)(Arg2)), (uint32_t)((uint32_t)(result + 1)));
    if (v_stack_m140 != 0) goto loc_009409D3;
loc_009407E4:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 301) goto loc_00940BD8;
    Arg1 = (uint32_t)(v_stack_m19C);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 302) { Arg1 = (uint32_t)(result + 1); }
    v_stack_m19C = (uint32_t)(Arg1);
    if ((uint32_t)(Arg1) == 0) goto loc_00940434;
loc_00940810:
    result = (uint8_t)((*(uint8_t *)(v_stack_mB8)) & (12));
    if (((uint8_t)(result)) == 4) goto loc_00940BED;
    result = MiStrongCodeImage(Arg2, (uint32_t)((uint32_t)(result + 1)), (uint32_t)((uint32_t)(Arg2)), (uint32_t)((uint32_t)(result + 1)));
    goto loc_00940434;
loc_00940834:
    result = MiRevertRelocations(v_stack_m150, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m170))), (uint32_t)((uint32_t)(result + 1)));
loc_0094084A:
    goto loc_0094041E;
loc_00940866:
    if (((uint8_t)(result)) == 4) goto loc_009409BE;
loc_0094086C:
    if (((uint32_t)(Arg1 + 4)) > ((uint32_t)(result + 1))) goto loc_009409FC;
    result = (v_stack_m1B0) & (-8);
    if (result > v_stack_m158) goto loc_00940C33;
    Arg1 = (v_stack_m1B0) << (3);
loc_0094089B:
    v_stack_m1B0 = Arg1;
    if (sign_flag) goto loc_00940C48;
loc_009408BA:
loc_009408C2:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m148 + 0x38) + 0x2E)) != 0) goto loc_00940C59;
loc_009408DB:
    if (((v_stack_m1B0) & (3)) != 0) goto loc_00940A5F;
loc_009408E9:
    if (sign_flag) goto loc_00940923;
    Arg2 = (uint8_t)(((uint32_t)(v_stack_m164)) & (7));
    Arg2 = (uint8_t)((Arg2) << (4));
    result = (uint8_t)((*(uint8_t *)(v_stack_m148 + 0xF)) & (128));
    Arg2 = (uint8_t)((Arg2) | ((uint8_t)(result)));
    result = (uint8_t)((v_stack_m1B8) & (15));
    Arg2 = (uint8_t)((Arg2) | ((uint8_t)(result)));
    result = MiWriteSegmentSignatureFlags(v_stack_m148, Arg2, v_stack_mB0, v_stack_m158);
    if (v_stack_m19C != 0) goto loc_00940CFF;
loc_00940923:
loc_00940925:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_mB0, v_stack_m158);
    local_rsp = (local_rsp) + (536);
    return result;
loc_00940948:
    local_r13 = ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x38) + 0x40)))) & (0xFFFULL)) != 0) ? 1 : 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2) + 0x38) + 0x40))) >> (12));
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) << (12));
    v_stack_pB4 = (uint32_t)(Arg2);
    goto loc_00940585;
loc_00940977:
    *(uint32_t *)(v_rip + 0x4ECE77) = 117;
    goto loc_00940923;
loc_00940983:
    goto loc_0094084A;
loc_0094098D:
    if (((*(uint64_t *)(v_rip + 0x6860F0)) & (0x20000ULL)) != 0) goto loc_00940C29;
loc_0094099E:
    result = PsRevertToUserPagePriorityThread(v_stack_pE8, (uint32_t)(v_stack_pC8), v_stack_mB0, v_stack_m158);
    goto loc_0094047F;
loc_009409BE:
    if (v_stack_p90 != 0) goto loc_0094086C;
    result = 0;
    goto loc_00940925;
loc_009409D3:
    if (sign_flag) goto loc_00940BB0;
    if ((((uint8_t)(result + 1)) & ((uint8_t)(local_r13))) != 0) goto loc_00940BB0;
    if (v_stack_pE8 == 0) goto loc_009407E4;
    result = ExFreePoolWithTag(v_stack_pE8, (uint32_t)(0x63734943ULL), v_stack_mB0, v_stack_m158);
    goto loc_009407E4;
loc_009409FC:
    if (((uint32_t)(Arg1 + 4)) > 3) goto loc_009408DB;
    Arg1 = (uint32_t)((v_stack_m1B0) & (3));
    result = (v_stack_p98) & (-4);
    Arg1 = (Arg1) | (result);
    v_stack_p98 = Arg1;
    goto loc_009408DB;
loc_00940A30:
    goto loc_009407E4;
loc_00940A3A:
    local_rbx = (uint32_t)((v_stack_m1B0) | ((uint32_t)(result + 1)));
    v_stack_pA8 = (uint32_t)(local_rbx);
    if (v_stack_pA0 != ((uint32_t)(result + 1))) goto loc_0094030A;
    goto loc_0094030A;
loc_00940A5F:
    if (((*(uint64_t *)(v_rip + 0x68601E)) & (0x2000ULL)) != 0) goto loc_00940CA0;
loc_00940A70:
    Arg2 = 0;
    result = MiWalkEntireImage(0, Arg2, (uint32_t)((uint32_t)(result + 1)), (uint32_t)(v_stack_pE0));
    if (sign_flag) goto loc_00940CDF;
    Arg2 = (v_stack_p98) & (-4);
    v_stack_p98 = Arg2;
    if (sign_flag) goto loc_00940CEE;
loc_00940AB2:
    goto loc_009408E9;
loc_00940AC7:
    v_stack_pB0 = (uint32_t)(result + 1);
    v_stack_p98 = v_stack_p1A8;
    goto loc_009403A5;
loc_00940ADF:
    if ((*(uint64_t *)(arg2 + 0x90)) != ((uint32_t)((uint32_t)(result + 1)))) goto loc_009402D6;
    *(uint32_t *)(v_rip + 0x4ECD02) = 116;
    goto loc_00940925;
loc_00940B00:
    *(uint32_t *)(v_rip + 0x4ECCDD) = 115;
    goto loc_00940925;
loc_00940B25:
    Arg1 = (uint32_t)(((uint32_t)(Arg5)) | (64));
    goto loc_009402A3;
loc_00940B2D:
    v_stack_pA8 = 7;
    v_stack_pA0 = 2;
    goto loc_009402DF;
loc_00940B49:
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    result = MiCreatePerSessionProtos(Arg2, Arg2, (uint32_t)((uint32_t)(result + 1)), (uint32_t)(v_stack_pE0));
    result = PsRevertToUserPagePriorityThread((uint32_t)((uint32_t)(result + 1)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)(result + 1)), (uint32_t)(v_stack_pE0));
    goto loc_00940925;
loc_00940B6F:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) | (0xFFFFFFFFULL));
    result = MiDereferencePerSessionProtos(Arg2, Arg2, (uint32_t)((uint32_t)(result + 1)), (uint32_t)(v_stack_pE0));
loc_00940B89:
    result = (result) & (-4);
    local_r12 = 0;
    local_r12 = (Arg2 != (result + 1)) ? 1 : 0;
    local_r12 = (uint32_t)((local_r12) + (2));
    goto loc_00940566;
loc_00940BA0:
    v_stack_pA0 = 2;
    goto loc_0094041E;
loc_00940BB0:
    result = SepScheduleImageVerificationCallbacks(Arg2, (uint32_t)(v_stack_pDC), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)(v_stack_p100)));
    goto loc_009407E4;
loc_00940BD8:
    result = MiImageCantMove(Arg2, (uint32_t)(v_stack_pDC), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)(v_stack_p100)));
    v_stack_pAC = (uint32_t)(result + 1);
    goto loc_00940810;
loc_00940BED:
    result = KeBugCheckEx(26, (uint32_t)(0x5150EULL), v_stack_p130, (int32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_00940C0E:
    Arg2 = (uint32_t)(((uint32_t)(0x5150EULL)) | (0xFFFFFFFFULL));
    result = MiDereferencePerSessionProtos(Arg2, Arg2, v_stack_p130, (int32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    local_r13 = 0;
    v_stack_pC4 = 0;
    goto loc_00940470;
loc_00940C29:
    result = MiFlushEntireTbDueToAttributeChange(Arg2, Arg2, v_stack_p130, (int32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_0094099E;
loc_00940C33:
    Arg1 = (Arg2) & (-3);
    Arg1 = (Arg1) | (result + 1);
    goto loc_0094089B;
loc_00940C48:
    Arg1 = (Arg1) | (4);
    v_stack_p98 = Arg1;
    goto loc_009408BA;
loc_00940C59:
    Arg2 = (v_stack_p98) >> (3);
    result = ((uint32_t)((uint32_t)(result))) & (-8);
    Arg1 = (v_stack_p98) & (-2);
    Arg1 = (Arg1) | (2);
    v_stack_p98 = Arg1;
    goto loc_009408C2;
loc_00940CA0:
    if (((*(uint32_t *)(arg2 + 0x5C)) & (0xC0000ULL)) == 0) goto loc_00940A70;
    if ((*(uint64_t *)(v_stack_p1A0)) == 0) goto loc_00940A70;
    result = MiCaptureSecureImageBaseAddress(Arg2, Arg2, v_stack_p130, (int32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (!sign_flag) goto loc_00940A70;
    *(uint32_t *)(v_rip + 0x4ECB1E) = 118;
    goto loc_00940925;
loc_00940CDF:
    *(uint32_t *)(v_rip + 0x4ECB0F) = 119;
    goto loc_00940925;
loc_00940CEE:
    Arg2 = (Arg2) | (4);
    v_stack_p98 = Arg2;
    goto loc_00940AB2;
loc_00940CFF:
    result = MiStrongCodeImage(Arg2, 2, v_stack_p130, (int32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_00940923;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x3E` | `64` | `R` |
| `Arg2` | `+ 0x5C` | `32` | `R` |
| `Arg2` | `+ 0x60` | `64` | `R` |
| `Arg2` | `+ 0x90` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00940190&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
