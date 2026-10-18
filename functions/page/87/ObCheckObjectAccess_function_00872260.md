# ObCheckObjectAccess

- RVA: `0x00872260`–`0x00872813` (길이 `1,459` bytes)
- VA: `0x0000000140872260`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C628`
- 디코드: `352`개 명령, `1,459/1,459` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **26**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00872354` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0087237B` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008723C0` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x00872420` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00872434` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00872495` → [SeOpenObjectAuditAlarmWithTransaction](../86/SeOpenObjectAuditAlarmWithTransaction_function_0086E790.md) (function, `0x0086E790`)
- `0x008724A2` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008724B0` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008724C2` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008724D0` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00872541` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008725A2` → [CmpSecurityMethod](CmpSecurityMethod_function_00870CC0.md) (function, `0x00870CC0`)
- `0x008725F7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0087261F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00872646` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0087267E` → [IopGetSetSecurityObject](IopGetSetSecurityObject_function_00873A80.md) (function, `0x00873A80`)
- `0x008726A6` → [ObDereferenceSecurityDescriptor](ObDereferenceSecurityDescriptor_function_008740A0.md) (function, `0x008740A0`)
- `0x008726B7` → [ObpReferenceSecurityDescriptorSlow](ObpReferenceSecurityDescriptorSlow_function_0087484C.md) (function, `0x0087484C`)
- `0x008726CC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008726E8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0087272D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0087277C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008727A5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008727B7` → [SepConcatenatePrivileges](../9D/SepConcatenatePrivileges_function_009D7AD0.md) (function, `0x009D7AD0`)
- `0x008727C7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00872809` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PspReferenceCpuPartitionByHandle](../78/PspReferenceCpuPartitionByHandle_function_007846F4.md) at `0x0078479E`

### Static image references
- `0x00872288` → RVA `0x00FC7800` (`ALMOSTRO`; read)
- `0x008722A5` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x008722B7` → RVA `0x008BA2B0` (`SeDefaultObjectMethod`; read)
- `0x00872522` → RVA `0x00E0B38C` (`.data`; read)
- `0x00872561` → RVA `0x00870CC0` (`CmpSecurityMethod`; read)
- `0x0087265C` → RVA `0x00873A80` (`IopGetSetSecurityObject`; read)
- `0x008726DC` → RVA `0x00E0B38C` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **20**
  - `0x00872354` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x0087237B` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008723C0` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x00872420` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00872434` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008724A2` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008724B0` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008724C2` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008724D0` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00872541` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008725F7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0087261F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00872646` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008726CC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008726E8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0087272D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0087277C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008727A5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008727C7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00872809` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00872260  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00872265  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
0087226A  55                              push rbp
0087226B  56                              push rsi
0087226C  57                              push rdi
0087226D  41 54                           push r12
0087226F  41 55                           push r13
00872271  41 56                           push r14
00872273  41 57                           push r15
00872275  48 81 EC 80 00 00 00            sub rsp, 0x80
0087227C  48 8D 41 D0                     lea rax, [rcx - 0x30]
00872280  45 0F B6 F9                     movzx r15d, r9b
00872284  48 C1 E8 08                     shr rax, 8
00872288  4C 8D 2D 71 55 75 00            lea r13, [rip + 0x755571]
0087228F  45 33 C9                        xor r9d, r9d
00872292  44 0F B6 C0                     movzx r8d, al
00872296  0F B6 41 E8                     movzx eax, byte ptr [rcx - 0x18]
0087229A  48 8B F2                        mov rsi, rdx
0087229D  4C 33 C0                        xor r8, rax
008722A0  44 89 4C 24 58                  mov dword ptr [rsp + 0x58], r9d
008722A5  0F B6 05 A0 4B 75 00            movzx eax, byte ptr [rip + 0x754ba0]
008722AC  48 8B E9                        mov rbp, rcx
008722AF  4C 33 C0                        xor r8, rax
008722B2  4C 89 4C 24 60                  mov qword ptr [rsp + 0x60], r9
008722B7  48 8D 05 F2 7F 04 00            lea rax, [rip + 0x47ff2]
008722BE  44 89 4C 24 50                  mov dword ptr [rsp + 0x50], r9d
008722C3  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
008722C8  4F 8B 6C C5 00                  mov r13, qword ptr [r13 + r8*8]
008722CD  49 39 85 98 00 00 00            cmp qword ptr [r13 + 0x98], rax
008722D4  0F 85 48 02 00 00               jne 0x140872522
008722DA  0F 0D 49 F8                     prefetchw byte ptr [rcx - 8]
008722DE  48 8B 51 F8                     mov rdx, qword ptr [rcx - 8]
008722E2  F6 C2 0F                        test dl, 0xf
008722E5  74 16                           je 0x1408722fd
008722E7  48 8D 4A FF                     lea rcx, [rdx - 1]
008722EB  48 8B C2                        mov rax, rdx
008722EE  F0 48 0F B1 4D F8               lock cmpxchg qword ptr [rbp - 8], rcx
008722F4  74 07                           je 0x1408722fd
008722F6  48 8B D0                        mov rdx, rax
008722F9  A8 0F                           test al, 0xf
008722FB  75 EA                           jne 0x1408722e7
008722FD  48 8B DA                        mov rbx, rdx
00872300  83 E2 0F                        and edx, 0xf
00872303  48 83 E3 F0                     and rbx, 0xfffffffffffffff0
00872307  83 FA 01                        cmp edx, 1
0087230A  77 09                           ja 0x140872315
0087230C  48 85 DB                        test rbx, rbx
0087230F  0F 85 9B 03 00 00               jne 0x1408726b0
00872315  45 32 E4                        xor r12b, r12b
00872318  44 88 A4 24 C0 00 00 00         mov byte ptr [rsp + 0xc0], r12b
00872320  48 85 DB                        test rbx, rbx
00872323  0F 84 D8 02 00 00               je 0x140872601
00872329  41 8B F9                        mov edi, r9d
0087232C  4D 8D 75 4C                     lea r14, [r13 + 0x4c]
00872330  48 85 DB                        test rbx, rbx
00872333  0F 84 96 02 00 00               je 0x1408725cf
00872339  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00872342  B2 01                           mov dl, 1
00872344  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0087234B  90                              nop
0087234C  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00872350  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00872354  E8 67 F8 99 FF                  call 0x140211bc0
00872359  48 83 7E 20 00                  cmp qword ptr [rsi + 0x20], 0
0087235E  74 20                           je 0x140872380
00872360  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00872369  B2 01                           mov dl, 1
0087236B  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00872372  90                              nop
00872373  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00872377  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0087237B  E8 40 F8 99 FF                  call 0x140211bc0
00872380  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00872388  48 8D 56 20                     lea rdx, [rsi + 0x20]
0087238C  44 8B 4E 10                     mov r9d, dword ptr [rsi + 0x10]
00872390  41 B0 01                        mov r8b, 1
00872393  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00872398  48 8B CB                        mov rcx, rbx
0087239B  48 8D 44 24 58                  lea rax, [rsp + 0x58]
008723A0  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008723A5  48 8D 44 24 60                  lea rax, [rsp + 0x60]
008723AA  44 88 7C 24 38                  mov byte ptr [rsp + 0x38], r15b
008723AF  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
008723B4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008723B9  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
008723BC  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008723C0  E8 FB 47 B3 FF                  call 0x1403a6bc0
008723C5  4C 8B 4C 24 60                  mov r9, qword ptr [rsp + 0x60]
008723CA  44 0F B6 F8                     movzx r15d, al
008723CE  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
008723D3  4D 85 C9                        test r9, r9
008723D6  74 6A                           je 0x140872442
008723D8  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
008723DC  45 8B 01                        mov r8d, dword ptr [r9]
008723DF  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008723E4  4C 8B 30                        mov r14, qword ptr [rax]
008723E7  41 8B 16                        mov edx, dword ptr [r14]
008723EA  41 8D 0C 10                     lea ecx, [r8 + rdx]
008723EE  83 F9 03                        cmp ecx, 3
008723F1  0F 87 42 03 00 00               ja 0x140872739
008723F7  4D 85 F6                        test r14, r14
008723FA  0F 84 EA 01 00 00               je 0x1408725ea
00872400  85 D2                           test edx, edx
00872402  0F 85 29 02 00 00               jne 0x140872631
00872408  41 BC 08 00 00 00               mov r12d, 8
0087240E  47 8D 04 40                     lea r8d, [r8 + r8*2]
00872412  41 8B CC                        mov ecx, r12d
00872415  41 C1 E0 02                     shl r8d, 2
00872419  49 8D 51 08                     lea rdx, [r9 + 8]
0087241D  49 03 CE                        add rcx, r14
00872420  E8 1B 44 E5 FF                  call 0x1406c6840
00872425  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0087242A  8B 01                           mov eax, dword ptr [rcx]
0087242C  41 01 06                        add dword ptr [r14], eax
0087242F  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00872434  E8 47 39 C0 FF                  call 0x140475d80
00872439  44 0F B6 A4 24 C0 00 00 00      movzx r12d, byte ptr [rsp + 0xc0]
00872442  45 84 FF                        test r15b, r15b
00872445  74 10                           je 0x140872457
00872447  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
0087244B  09 46 14                        or dword ptr [rsi + 0x14], eax
0087244E  0F BA E8 19                     bts eax, 0x19
00872452  F7 D0                           not eax
00872454  21 46 10                        and dword ptr [rsi + 0x10], eax
00872457  0F B6 94 24 D8 00 00 00         movzx edx, byte ptr [rsp + 0xd8]
0087245F  84 D2                           test dl, dl
00872461  74 37                           je 0x14087249a
00872463  48 8D 46 0A                     lea rax, [rsi + 0xa]
00872467  4C 8B CB                        mov r9, rbx
0087246A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0087246F  49 8D 4D 10                     lea rcx, [r13 + 0x10]
00872473  48 C7 44 24 40 00 00 00 00      mov qword ptr [rsp + 0x40], 0
0087247C  45 33 C0                        xor r8d, r8d
0087247F  88 54 24 38                     mov byte ptr [rsp + 0x38], dl
00872483  48 8B D5                        mov rdx, rbp
00872486  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
0087248B  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
00872490  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00872495  E8 F6 C2 FF FF                  call 0x14086e790
0087249A  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
0087249E  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008724A2  E8 69 D5 9E FF                  call 0x14025fa10
008724A7  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008724B0  E8 3B CB 9E FF                  call 0x14025eff0
008724B5  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
008724B9  48 85 C9                        test rcx, rcx
008724BC  74 17                           je 0x1408724d5
008724BE  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008724C2  E8 49 D5 9E FF                  call 0x14025fa10
008724C7  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008724D0  E8 1B CB 9E FF                  call 0x14025eff0
008724D5  45 84 E4                        test r12b, r12b
008724D8  0F 85 14 01 00 00               jne 0x1408725f2
008724DE  0F 0D 4D F8                     prefetchw byte ptr [rbp - 8]
008724E2  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
008724E6  48 8B C8                        mov rcx, rax
008724E9  48 33 CB                        xor rcx, rbx
008724EC  48 83 F9 0F                     cmp rcx, 0xf
008724F0  0F 83 A8 01 00 00               jae 0x14087269e
008724F6  48 8D 48 01                     lea rcx, [rax + 1]
008724FA  F0 48 0F B1 4D F8               lock cmpxchg qword ptr [rbp - 8], rcx
00872500  75 E4                           jne 0x1408724e6
00872502  41 0F B6 C7                     movzx eax, r15b
00872506  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0087250E  48 81 C4 80 00 00 00            add rsp, 0x80
00872515  41 5F                           pop r15
00872517  41 5E                           pop r14
00872519  41 5D                           pop r13
0087251B  41 5C                           pop r12
0087251D  5F                              pop rdi
0087251E  5E                              pop rsi
0087251F  5D                              pop rbp
00872520  C3                              ret
00872521  CC                              int3
00872522  8B 05 64 8E 59 00               mov eax, dword ptr [rip + 0x598e64]
00872528  B9 00 01 00 00                  mov ecx, 0x100
0087252D  8B D0                           mov edx, eax
0087252F  C7 44 24 54 BF 01 00 00         mov dword ptr [rsp + 0x54], 0x1bf
00872537  41 B8 4F 62 53 71               mov r8d, 0x7153624f
0087253D  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00872541  E8 AA FB 30 00                  call 0x140b820f0
00872546  48 8B D8                        mov rbx, rax
00872549  48 85 C0                        test rax, rax
0087254C  0F 84 36 01 00 00               je 0x140872688
00872552  49 8B 85 98 00 00 00            mov rax, qword ptr [r13 + 0x98]
00872559  4D 8D 75 4C                     lea r14, [r13 + 0x4c]
0087255D  41 8B 4D 64                     mov ecx, dword ptr [r13 + 0x64]
00872561  48 8D 15 58 E7 FF FF            lea rdx, [rip - 0x18a8]
00872568  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
0087256D  4C 8D 65 F8                     lea r12, [rbp - 8]
00872571  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00872576  4C 8B CB                        mov r9, rbx
00872579  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0087257D  4C 8D 44 24 54                  lea r8, [rsp + 0x54]
00872582  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00872587  48 3B C2                        cmp rax, rdx
0087258A  0F 85 CC 00 00 00               jne 0x14087265c
00872590  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00872595  BA 01 00 00 00                  mov edx, 1
0087259A  48 8B CD                        mov rcx, rbp
0087259D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008725A2  E8 19 E7 FF FF                  call 0x140870cc0
008725A7  8B F8                           mov edi, eax
008725A9  3D 23 00 00 C0                  cmp eax, 0xc0000023
008725AE  0F 84 13 01 00 00               je 0x1408726c7
008725B4  85 FF                           test edi, edi
008725B6  0F 88 85 00 00 00               js 0x140872641
008725BC  41 B4 01                        mov r12b, 1
008725BF  45 33 C9                        xor r9d, r9d
008725C2  44 88 A4 24 C0 00 00 00         mov byte ptr [rsp + 0xc0], r12b
008725CA  E9 61 FD FF FF                  jmp 0x140872330
008725CF  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
008725D2  09 46 14                        or dword ptr [rsi + 0x14], eax
008725D5  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
008725DD  44 89 4E 10                     mov dword ptr [rsi + 0x10], r9d
008725E1  89 38                           mov dword ptr [rax], edi
008725E3  B0 01                           mov al, 1
008725E5  E9 1C FF FF FF                  jmp 0x140872506
008725EA  45 33 E4                        xor r12d, r12d
008725ED  E9 1C FE FF FF                  jmp 0x14087240e
008725F2  33 D2                           xor edx, edx
008725F4  48 8B CB                        mov rcx, rbx
008725F7  E8 74 02 31 00                  call 0x140b82870
008725FC  E9 01 FF FF FF                  jmp 0x140872502
00872601  41 F6 45 42 08                  test byte ptr [r13 + 0x42], 8
00872606  74 1D                           je 0x140872625
00872608  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0087260D  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00872611  41 B9 01 00 00 00               mov r9d, 1
00872617  4D 8B C5                        mov r8, r13
0087261A  B9 89 01 00 00                  mov ecx, 0x189
0087261F  E8 3C B0 C8 FF                  call 0x1404fd660
00872624  CC                              int3
00872625  F6 45 EA 02                     test byte ptr [rbp - 0x16], 2
00872629  0F 84 FA FC FF FF               je 0x140872329
0087262F  EB D7                           jmp 0x140872608
00872631  8D 04 52                        lea eax, [rdx + rdx*2]
00872634  44 8D 24 85 08 00 00 00         lea r12d, [rax*4 + 8]
0087263C  E9 CD FD FF FF                  jmp 0x14087240e
00872641  33 D2                           xor edx, edx
00872643  48 8B CB                        mov rcx, rbx
00872646  E8 25 02 31 00                  call 0x140b82870
0087264B  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00872653  89 38                           mov dword ptr [rax], edi
00872655  32 C0                           xor al, al
00872657  E9 AA FE FF FF                  jmp 0x140872506
0087265C  48 8D 15 1D 14 00 00            lea rdx, [rip + 0x141d]
00872663  48 3B C2                        cmp rax, rdx
00872666  BA 01 00 00 00                  mov edx, 1
0087266B  0F 85 8B 01 00 00               jne 0x1408727fc
00872671  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00872676  48 8B CD                        mov rcx, rbp
00872679  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087267E  E8 FD 13 00 00                  call 0x140873a80
00872683  E9 1F FF FF FF                  jmp 0x1408725a7
00872688  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00872690  BF 9A 00 00 C0                  mov edi, 0xc000009a
00872695  89 38                           mov dword ptr [rax], edi
00872697  32 C0                           xor al, al
00872699  E9 68 FE FF FF                  jmp 0x140872506
0087269E  BA 01 00 00 00                  mov edx, 1
008726A3  48 8B CB                        mov rcx, rbx
008726A6  E8 F5 19 00 00                  call 0x1408740a0
008726AB  E9 52 FE FF FF                  jmp 0x140872502
008726B0  4C 8B C3                        mov r8, rbx
008726B3  48 8D 4D D0                     lea rcx, [rbp - 0x30]
008726B7  E8 90 21 00 00                  call 0x14087484c
008726BC  48 8B D8                        mov rbx, rax
008726BF  45 33 C9                        xor r9d, r9d
008726C2  E9 4E FC FF FF                  jmp 0x140872315
008726C7  33 D2                           xor edx, edx
008726C9  48 8B CB                        mov rcx, rbx
008726CC  E8 9F 01 31 00                  call 0x140b82870
008726D1  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
008726D5  B9 00 01 00 00                  mov ecx, 0x100
008726DA  8B D0                           mov edx, eax
008726DC  89 05 AA 8C 59 00               mov dword ptr [rip + 0x598caa], eax
008726E2  41 B8 4F 62 53 71               mov r8d, 0x7153624f
008726E8  E8 03 FA 30 00                  call 0x140b820f0
008726ED  48 8B D8                        mov rbx, rax
008726F0  48 85 C0                        test rax, rax
008726F3  74 93                           je 0x140872688
008726F5  41 8B 4D 64                     mov ecx, dword ptr [r13 + 0x64]
008726F9  4C 8D 44 24 54                  lea r8, [rsp + 0x54]
008726FE  49 8B 85 98 00 00 00            mov rax, qword ptr [r13 + 0x98]
00872705  4C 8B CB                        mov r9, rbx
00872708  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
0087270D  BA 01 00 00 00                  mov edx, 1
00872712  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00872717  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0087271B  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00872720  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00872725  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0087272A  48 8B CD                        mov rcx, rbp
0087272D  E8 9E 83 E4 FF                  call 0x1406baad0
00872732  8B F8                           mov edi, eax
00872734  E9 7B FE FF FF                  jmp 0x1408725b4
00872739  41 BC 08 00 00 00               mov r12d, 8
0087273F  45 85 C0                        test r8d, r8d
00872742  0F 84 90 00 00 00               je 0x1408727d8
00872748  43 8D 04 40                     lea eax, [r8 + r8*2]
0087274C  8D 0C 85 08 00 00 00            lea ecx, [rax*4 + 8]
00872753  4D 85 F6                        test r14, r14
00872756  0F 84 84 00 00 00               je 0x1408727e0
0087275C  85 D2                           test edx, edx
0087275E  0F 84 80 00 00 00               je 0x1408727e4
00872764  8D 04 52                        lea eax, [rdx + rdx*2]
00872767  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
0087276E  8D 14 01                        lea edx, [rcx + rax]
00872771  41 B8 53 65 50 72               mov r8d, 0x72506553
00872777  B9 00 01 00 00                  mov ecx, 0x100
0087277C  E8 6F F9 30 00                  call 0x140b820f0
00872781  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00872786  48 8B C8                        mov rcx, rax
00872789  48 85 C0                        test rax, rax
0087278C  0F 84 9D FC FF FF               je 0x14087242f
00872792  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
00872797  49 8B 16                        mov rdx, qword ptr [r14]
0087279A  48 85 D2                        test rdx, rdx
0087279D  75 4A                           jne 0x1408727e9
0087279F  45 33 E4                        xor r12d, r12d
008727A2  45 8B C4                        mov r8d, r12d
008727A5  E8 96 40 E5 FF                  call 0x1406c6840
008727AA  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
008727AF  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
008727B4  49 8B CC                        mov rcx, r12
008727B7  E8 14 53 16 00                  call 0x1409d7ad0
008727BC  80 7E 0B 00                     cmp byte ptr [rsi + 0xb], 0
008727C0  74 0A                           je 0x1408727cc
008727C2  49 8B 0E                        mov rcx, qword ptr [r14]
008727C5  33 D2                           xor edx, edx
008727C7  E8 A4 00 31 00                  call 0x140b82870
008727CC  4D 89 26                        mov qword ptr [r14], r12
008727CF  C6 46 0B 01                     mov byte ptr [rsi + 0xb], 1
008727D3  E9 57 FC FF FF                  jmp 0x14087242f
008727D8  41 8B CC                        mov ecx, r12d
008727DB  E9 73 FF FF FF                  jmp 0x140872753
008727E0  33 C0                           xor eax, eax
008727E2  EB 8A                           jmp 0x14087276e
008727E4  41 8B C4                        mov eax, r12d
008727E7  EB 85                           jmp 0x14087276e
008727E9  8B 02                           mov eax, dword ptr [rdx]
008727EB  85 C0                           test eax, eax
008727ED  74 B3                           je 0x1408727a2
008727EF  8D 04 40                        lea eax, [rax + rax*2]
008727F2  44 8D 24 85 08 00 00 00         lea r12d, [rax*4 + 8]
008727FA  EB A6                           jmp 0x1408727a2
008727FC  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00872801  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00872806  48 8B CD                        mov rcx, rbp
00872809  E8 C2 82 E4 FF                  call 0x1406baad0
0087280E  E9 94 FD FF FF                  jmp 0x1408725a7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObCheckObjectAccess(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int8 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p50;
    unsigned int v_stack_p54;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int8 v_stack_p8;
    unsigned __int8 v_stack_pC0;

    v_stack_p10 = v_rbx;
    v_stack_p20 = (unsigned __int8)(a4);
    v_rsp = (v_rsp) - (128);
    result = (a1 - 48) >> (8);
    a4 = 0;
    a3 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(a1 - 24));
    v_stack_m60 = 0;
    a3 = (a3) ^ (*(unsigned __int8 *)(v_rip + 7687072));
    v_stack_m58 = 0;
    v_stack_m68 = 0;
    v_stack_m64 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7689585 + a3 * 8) + 152)) != (v_rip + 294898)) goto loc_00872522;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 - 8))) & (15)) == 0) goto loc_008722FD;
loc_008722E7:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 - 8))) & (15)) == 0) goto loc_008722FD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 - 8))) & (15)) != 0) goto loc_008722E7;
loc_008722FD:
    a2 = (unsigned int)((*(unsigned __int64 *)(a1 - 8)) & (15));
    v_rbx = (*(unsigned __int64 *)(a1 - 8)) & (-16);
    if (((unsigned int)(a2)) > 1) goto loc_00872315;
    if (v_rbx != 0) goto loc_008726B0;
loc_00872315:
    v_r12 = 0;
    v_stack_p8 = 0;
    if (v_rbx == 0) goto loc_00872601;
loc_00872329:
loc_00872330:
    if (v_rbx == 0) goto loc_008725CF;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 48) + 48), 1, a3, a4);
    if ((*(unsigned __int64 *)(a2 + 32)) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = 1;
        a1 = *(unsigned __int64 *)(a2 + 32);
        a1 = *(unsigned __int64 *)(a1 + 48);
        result = ExAcquireResourceSharedLite(a1, a2, a3, a4);
    }
    v_stack_m70 = a5;
    v_stack_m78 = v_stack_m60;
    v_stack_m80 = (unsigned __int8)((unsigned __int8)(a4));
    v_stack_m88 = *(unsigned __int64 *)(v_rip + 7689585 + a3 * 8) + 76;
    v_stack_m90 = v_stack_m58;
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 20)));
    result = SeAccessCheck(v_rbx, a2 + 32, 1, (unsigned int)(*(unsigned int *)(a2 + 16)));
    v_stack_m50 = v_stack_m58;
    if (v_stack_m58 == 0) goto loc_00872442;
    v_stack_m48 = *(unsigned __int64 *)(a2 + 72);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m58)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72)))) * 1)) > 3) goto loc_00872739;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72)) == 0) goto loc_008725EA;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72))))) != 0) goto loc_00872631;
loc_0087240E:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m58)) + (unsigned int)(*(unsigned int *)(v_stack_m58)) * 2) << (2));
    a1 = (8) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72)));
    result = memcpy(a1, v_stack_m58 + 8, a3, v_stack_m58);
loc_0087242F:
    result = CmSiFreeMemory(v_stack_m58, v_stack_m58 + 8, a3, v_stack_m58);
loc_00872442:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        result = v_stack_m60;
        result = (unsigned int)(~(result));
    }
    if ((unsigned __int8)(v_stack_p20) != 0) {
        result = a2 + 10;
        a4 = v_rbx;
        v_stack_m70 = result;
        a1 = *(unsigned __int64 *)(v_rip + 7689585 + a3 * 8) + 16;
        v_stack_m78 = 0;
        a3 = 0;
        v_stack_m80 = (unsigned __int8)(v_stack_p20);
        a2 = a1;
        v_stack_m88 = (unsigned __int8)((unsigned __int8)(result));
        v_stack_m90 = 0;
        v_stack_m98 = a2;
        result = SeOpenObjectAuditAlarmWithTransaction(a1, a2, a3, a4);
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 48) + 48), a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    if (*(unsigned __int64 *)(a2 + 32) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) + 48);
        result = ExReleaseResourceLite(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, a2, a3, a4);
    }
    if ((unsigned __int8)(v_stack_p8) != 0) goto loc_008725F2;
loc_008724E6:
    a1 = (*(unsigned __int64 *)(a1 - 8)) ^ (v_rbx);
    if (a1 >= 15) goto loc_0087269E;
    if (a1 != 15) goto loc_008724E6;
loc_00872502:
loc_00872506:
    v_rsp = (v_rsp) + (128);
    return (unsigned __int8)((unsigned __int8)(result));
loc_00872522:
    v_stack_p54 = 447;
    v_stack_p50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5869156)));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5869156)))), (unsigned int)(0x7153624FULL), a4);
    if (result == 0) goto loc_00872688;
    v_stack_p40 = (unsigned __int8)((unsigned __int8)(result));
    v_stack_p38 = *(unsigned __int64 *)(v_rip + 7689585 + a3 * 8) + 76;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7689585 + a3 * 8) + 100)));
    v_stack_p28 = a1 - 8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7689585 + a3 * 8) + 152)) != (v_rip - 6312)) goto loc_0087265C;
    v_stack_p20 = v_stack_p50;
    result = CmpSecurityMethod(a1, 1, v_stack_p54, result);
loc_008725A7:
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_008726C7;
loc_008725B4:
    if (sign_flag) goto loc_00872641;
    a4 = 0;
    v_stack_pC0 = 1;
    goto loc_00872330;
loc_008725CF:
    *(unsigned int *)(a2 + 16) = 0;
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_00872506;
loc_008725EA:
    v_r12 = 0;
    goto loc_0087240E;
loc_008725F2:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_p54, a4);
    goto loc_00872502;
loc_00872601:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 7689585 + a3 * 8) + 66)) & (8)) != 0) {
        v_stack_p20 = 0;
        a2 = a1 - 48;
        a4 = 1;
        a3 = *(unsigned __int64 *)(v_rip + 7689585 + a3 * 8);
        a1 = 393;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(a1 - 22)) & (2)) == 0) goto loc_00872329;
    goto loc_00872608;
loc_00872631:
    goto loc_0087240E;
loc_00872641:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, a4);
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = 0;
    goto loc_00872506;
loc_0087265C:
    if (0 != (v_rip + 5149)) goto loc_008727FC;
    v_stack_p20 = v_stack_p50;
    result = IopGetSetSecurityObject(a1, 1, a3, a4);
    goto loc_008725A7;
loc_00872688:
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(0xC000009AULL));
    result = 0;
    goto loc_00872506;
loc_0087269E:
    result = ObDereferenceSecurityDescriptor(0, 1, a3, a4);
    goto loc_00872502;
loc_008726B0:
    result = ObpReferenceSecurityDescriptorSlow(a1 - 48, 1, result, a4);
    a4 = 0;
    goto loc_00872315;
loc_008726C7:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, result, a4);
    *(unsigned int *)(v_rip + 5868714) = (unsigned int)((unsigned int)(v_stack_p50));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_p50))), (unsigned int)(0x7153624FULL), a4);
    if (result == 0) goto loc_00872688;
    v_stack_p40 = (unsigned __int8)((unsigned __int8)(result));
    v_stack_p38 = *(unsigned __int64 *)(v_rip + 7689585 + a3 * 8) + 76;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7689585 + a3 * 8) + 100)));
    v_stack_p28 = a2 + a2 * 2 * 4 + 8;
    v_stack_p20 = v_stack_p50;
    result = guard_dispatch_icall(a1, 1, v_stack_p54, result);
    goto loc_008725B4;
loc_00872739:
    if ((unsigned int)(v_stack_p54) == 0) goto loc_008727D8;
loc_00872753:
    if (*(unsigned __int64 *)(v_rip + 7689585 + a3 * 8) + 76 == 0) goto loc_008727E0;
    if (1 == 0) goto loc_008727E4;
loc_0087276E:
    result = ExAllocatePool2(256, v_stack_p54 + v_stack_p54 * 2 * 4 + 8 + 1 + 1 * 2 * 4 + 8 * 1, (unsigned int)(0x72506553ULL), result);
    v_stack_p78 = result;
    if (result == 0) goto loc_0087242F;
    if (*(unsigned __int64 *)(v_stack_p70) != 0) goto loc_008727E9;
    v_r12 = 0;
loc_008727A2:
    result = memcpy(result, *(unsigned __int64 *)(v_stack_p70), 0, result);
    result = SepConcatenatePrivileges(v_stack_p78, *(unsigned __int64 *)(v_stack_p70), v_stack_p68, result);
    if ((*(unsigned __int8 *)(a2 + 11)) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_p70);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, v_stack_p68, result);
    }
    *(unsigned __int64 *)(v_stack_p70) = v_stack_p78;
    *(unsigned __int8 *)(a2 + 11) = 1;
    goto loc_0087242F;
loc_008727D8:
    goto loc_00872753;
loc_008727E0:
    result = 0;
    goto loc_0087276E;
loc_008727E4:
    goto loc_0087276E;
loc_008727E9:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2))) == 0) goto loc_008727A2;
    goto loc_008727A2;
loc_008727FC:
    v_stack_p20 = v_stack_p50;
    result = guard_dispatch_icall(a1, a2, v_stack_p68, result);
    goto loc_008725A7;
}
```

## 5. (Beta) C Style

```c
int64_t ObCheckObjectAccess(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint8_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_p10;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;
    uint32_t v_stack_p50;
    uint32_t v_stack_p54;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint8_t v_stack_p8;
    uint8_t v_stack_pC0;

    v_stack_p10 = local_rbx;
    v_stack_p20 = (uint8_t)(Arg4);
    local_rsp = (local_rsp) - (128);
    result = (Arg1 - 48) >> (8);
    Arg4 = 0;
    Arg3 = ((uint8_t)(result)) ^ (*(uint8_t *)(arg1 - 0x18));
    v_stack_m60 = 0;
    Arg3 = (Arg3) ^ (*(uint8_t *)(v_rip + 0x754BA0));
    v_stack_m58 = 0;
    v_stack_m68 = 0;
    v_stack_m64 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x755571 + Arg3 * 8) + 0x98)) != (v_rip + 294898)) goto loc_00872522;
    if ((((uint8_t)(*(uint64_t *)(arg1 - 0x8))) & (15)) == 0) goto loc_008722FD;
loc_008722E7:
    if ((((uint8_t)(*(uint64_t *)(arg1 - 0x8))) & (15)) == 0) goto loc_008722FD;
    if ((((uint8_t)(*(uint64_t *)(arg1 - 0x8))) & (15)) != 0) goto loc_008722E7;
loc_008722FD:
    Arg2 = (uint32_t)((*(uint64_t *)(arg1 - 0x8)) & (15));
    local_rbx = (*(uint64_t *)(arg1 - 0x8)) & (-16);
    if (((uint32_t)(Arg2)) > 1) goto loc_00872315;
    if (local_rbx != 0) goto loc_008726B0;
loc_00872315:
    local_r12 = 0;
    v_stack_p8 = 0;
    if (local_rbx == 0) goto loc_00872601;
loc_00872329:
loc_00872330:
    if (local_rbx == 0) goto loc_008725CF;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)(arg2 + 0x30) + 0x30), 1, Arg3, Arg4);
    if ((*(uint64_t *)(arg2 + 0x20)) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = 1;
        Arg1 = *(uint64_t *)(arg2 + 0x20);
        Arg1 = *(uint64_t *)(arg1 + 0x30);
        result = ExAcquireResourceSharedLite(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = Arg5;
    v_stack_m78 = v_stack_m60;
    v_stack_m80 = (uint8_t)((uint8_t)(Arg4));
    v_stack_m88 = *(uint64_t *)(v_rip + 0x755571 + Arg3 * 8) + 76;
    v_stack_m90 = v_stack_m58;
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x14)));
    result = SeAccessCheck(local_rbx, Arg2 + 32, 1, (uint32_t)(*(uint32_t *)(arg2 + 0x10)));
    v_stack_m50 = v_stack_m58;
    if (v_stack_m58 == 0) goto loc_00872442;
    v_stack_m48 = *(uint64_t *)(arg2 + 0x48);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m58)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48)))) * 1)) > 3) goto loc_00872739;
    if (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48)) == 0) goto loc_008725EA;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48))))) != 0) goto loc_00872631;
loc_0087240E:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m58)) + (uint32_t)(*(uint32_t *)(v_stack_m58)) * 2) << (2));
    Arg1 = (8) + (*(uint64_t *)(*(uint64_t *)(arg2 + 0x48)));
    result = memcpy(Arg1, v_stack_m58 + 8, Arg3, v_stack_m58);
loc_0087242F:
    result = CmSiFreeMemory(v_stack_m58, v_stack_m58 + 8, Arg3, v_stack_m58);
loc_00872442:
    if ((uint8_t)((uint8_t)(result)) != 0) {
        result = v_stack_m60;
        result = (uint32_t)(~(result));
    }
    if ((uint8_t)(v_stack_p20) != 0) {
        result = Arg2 + 10;
        Arg4 = local_rbx;
        v_stack_m70 = result;
        Arg1 = *(uint64_t *)(v_rip + 0x755571 + Arg3 * 8) + 16;
        v_stack_m78 = 0;
        Arg3 = 0;
        v_stack_m80 = (uint8_t)(v_stack_p20);
        Arg2 = Arg1;
        v_stack_m88 = (uint8_t)((uint8_t)(result));
        v_stack_m90 = 0;
        v_stack_m98 = Arg2;
        result = SeOpenObjectAuditAlarmWithTransaction(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(arg2 + 0x30) + 0x30), Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    if (*(uint64_t *)(arg2 + 0x20) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x20) + 0x30);
        result = ExReleaseResourceLite(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint8_t)(v_stack_p8) != 0) goto loc_008725F2;
loc_008724E6:
    Arg1 = (*(uint64_t *)(arg1 - 0x8)) ^ (local_rbx);
    if (Arg1 >= 15) goto loc_0087269E;
    if (Arg1 != 15) goto loc_008724E6;
loc_00872502:
loc_00872506:
    local_rsp = (local_rsp) + (128);
    return (uint8_t)((uint8_t)(result));
loc_00872522:
    v_stack_p54 = 447;
    v_stack_p50 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x598E64)));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x598E64)))), (uint32_t)(0x7153624FULL), Arg4);
    if (result == 0) goto loc_00872688;
    v_stack_p40 = (uint8_t)((uint8_t)(result));
    v_stack_p38 = *(uint64_t *)(v_rip + 0x755571 + Arg3 * 8) + 76;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x755571 + Arg3 * 8) + 0x64)));
    v_stack_p28 = Arg1 - 8;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x755571 + Arg3 * 8) + 0x98)) != (v_rip - 6312)) goto loc_0087265C;
    v_stack_p20 = v_stack_p50;
    result = CmpSecurityMethod(Arg1, 1, v_stack_p54, result);
loc_008725A7:
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_008726C7;
loc_008725B4:
    if (sign_flag) goto loc_00872641;
    Arg4 = 0;
    v_stack_pC0 = 1;
    goto loc_00872330;
loc_008725CF:
    *(uint32_t *)(arg2 + 0x10) = 0;
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_00872506;
loc_008725EA:
    local_r12 = 0;
    goto loc_0087240E;
loc_008725F2:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_p54, Arg4);
    goto loc_00872502;
loc_00872601:
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x755571 + Arg3 * 8) + 0x42)) & (8)) != 0) {
        v_stack_p20 = 0;
        Arg2 = Arg1 - 48;
        Arg4 = 1;
        Arg3 = *(uint64_t *)(v_rip + 0x755571 + Arg3 * 8);
        Arg1 = 393;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint8_t *)(arg1 - 0x16)) & (2)) == 0) goto loc_00872329;
    goto loc_00872608;
loc_00872631:
    goto loc_0087240E;
loc_00872641:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, Arg4);
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = 0;
    goto loc_00872506;
loc_0087265C:
    if (0 != (v_rip + 5149)) goto loc_008727FC;
    v_stack_p20 = v_stack_p50;
    result = IopGetSetSecurityObject(Arg1, 1, Arg3, Arg4);
    goto loc_008725A7;
loc_00872688:
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(0xC000009AULL));
    result = 0;
    goto loc_00872506;
loc_0087269E:
    result = ObDereferenceSecurityDescriptor(0, 1, Arg3, Arg4);
    goto loc_00872502;
loc_008726B0:
    result = ObpReferenceSecurityDescriptorSlow(Arg1 - 48, 1, result, Arg4);
    Arg4 = 0;
    goto loc_00872315;
loc_008726C7:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, result, Arg4);
    *(uint32_t *)(v_rip + 0x598CAA) = (uint32_t)((uint32_t)(v_stack_p50));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_p50))), (uint32_t)(0x7153624FULL), Arg4);
    if (result == 0) goto loc_00872688;
    v_stack_p40 = (uint8_t)((uint8_t)(result));
    v_stack_p38 = *(uint64_t *)(v_rip + 0x755571 + Arg3 * 8) + 76;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x755571 + Arg3 * 8) + 0x64)));
    v_stack_p28 = Arg2 + Arg2 * 2 * 4 + 8;
    v_stack_p20 = v_stack_p50;
    result = guard_dispatch_icall(Arg1, 1, v_stack_p54, result);
    goto loc_008725B4;
loc_00872739:
    if ((uint32_t)(v_stack_p54) == 0) goto loc_008727D8;
loc_00872753:
    if (*(uint64_t *)(v_rip + 0x755571 + Arg3 * 8) + 76 == 0) goto loc_008727E0;
    if (1 == 0) goto loc_008727E4;
loc_0087276E:
    result = ExAllocatePool2(256, v_stack_p54 + v_stack_p54 * 2 * 4 + 8 + 1 + 1 * 2 * 4 + 8 * 1, (uint32_t)(0x72506553ULL), result);
    v_stack_p78 = result;
    if (result == 0) goto loc_0087242F;
    if (*(uint64_t *)(v_stack_p70) != 0) goto loc_008727E9;
    local_r12 = 0;
loc_008727A2:
    result = memcpy(result, *(uint64_t *)(v_stack_p70), 0, result);
    result = SepConcatenatePrivileges(v_stack_p78, *(uint64_t *)(v_stack_p70), v_stack_p68, result);
    if ((*(uint8_t *)(arg2 + 0xB)) != 0) {
        Arg1 = *(uint64_t *)(v_stack_p70);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_p68, result);
    }
    *(uint64_t *)(v_stack_p70) = v_stack_p78;
    *(uint8_t *)(arg2 + 0xB) = 1;
    goto loc_0087242F;
loc_008727D8:
    goto loc_00872753;
loc_008727E0:
    result = 0;
    goto loc_0087276E;
loc_008727E4:
    goto loc_0087276E;
loc_008727E9:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))) == 0) goto loc_008727A2;
    goto loc_008727A2;
loc_008727FC:
    v_stack_p20 = v_stack_p50;
    result = guard_dispatch_icall(Arg1, Arg2, v_stack_p68, result);
    goto loc_008725A7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x30` | `64` | `R` |
| `Arg1` | `- 0x18` | `8` | `R` |
| `Arg1` | `- 0x16` | `8` | `R` |
| `Arg1` | `- 0x8` | `8` | `R` |
| `Arg1` | `- 0x8` | `64` | `R` |
| `Arg2` | `+ 0xA` | `64` | `R` |
| `Arg2` | `+ 0xB` | `8` | `R` |
| `Arg2` | `+ 0xB` | `8` | `W` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R/W` |
| `Arg2` | `+ 0x10` | `32` | `W` |
| `Arg2` | `+ 0x14` | `32` | `R` |
| `Arg2` | `+ 0x14` | `32` | `R/W` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x48` | `64` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00872260&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
