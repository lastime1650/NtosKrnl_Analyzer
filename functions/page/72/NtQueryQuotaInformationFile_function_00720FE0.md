# NtQueryQuotaInformationFile

- RVA: `0x00720FE0`–`0x0072172A` (길이 `1,866` bytes)
- VA: `0x0000000140720FE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C78A8`
- 디코드: `475`개 명령, `1,866/1,866` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007210BD` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x007210E4` → [RtlLengthRequiredSid](../9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x007210FB` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00721140` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x007211AA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007211C5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007211E9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00721226` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0072124F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007212B8` → [IopCheckGetQuotaBufferValidity](../71/IopCheckGetQuotaBufferValidity_function_0071AF24.md) (function, `0x0071AF24`)
- `0x007212E7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00721300` → [RtlValidSid](../92/RtlValidSid_function_00929710.md) (function, `0x00929710`)
- `0x00721313` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00721334` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x00721386` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007213B1` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x007213D3` → [IopWaitAndAcquireFileObjectLock](../8A/IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x007213ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0072140E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0072142A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00721437` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0072144D` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x0072145A` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x00721462` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x00721475` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x00721493` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0072149D` → [IopAllocateIrpCleanup](../A1/IopAllocateIrpCleanup_function_00A1E2D4.md) (function, `0x00A1E2D4`)
- `0x00721547` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00721575` → [IopExceptionCleanupEx](../8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x00721584` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007215D1` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x007215E3` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x007215FA` → [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) (function, `0x0023B990`)
- `0x0072161A` → [MmUpdateMdlTracker](../../text/45/MmUpdateMdlTracker_function_00456468.md) (function, `0x00456468`)
- `0x00721649` → [IopExceptionCleanupEx](../8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x0072165A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007216E1` → [IopSynchronousServiceTail](../8E/IopSynchronousServiceTail_function_008EB440.md) (function, `0x008EB440`)
- `0x00721711` → [IopSynchronousApiServiceTail](../8A/IopSynchronousApiServiceTail_function_008ACE3C.md) (function, `0x008ACE3C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007215FF` → RVA `0x00FC6BBC` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x007211AA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007211C5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007211E9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00721226` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0072124F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007212E7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00721313` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00721334` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (`PAGE` → `.text`)
  - `0x00721386` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007213B1` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x007213ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0072140E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0072142A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00721437` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0072144D` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x0072145A` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (`PAGE` → `.text`)
  - `0x00721462` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x00721475` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x00721493` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00721547` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00721584` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007215D1` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x007215E3` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGE` → `.text`)
  - `0x007215FA` → [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) (`PAGE` → `.text`)
  - `0x0072161A` → [MmUpdateMdlTracker](../../text/45/MmUpdateMdlTracker_function_00456468.md) (`PAGE` → `.text`)
  - `0x0072165A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00720FE0  4C 8B DC                        mov r11, rsp
00720FE3  45 89 4B 20                     mov dword ptr [r11 + 0x20], r9d
00720FE7  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
00720FEB  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
00720FEF  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
00720FF3  53                              push rbx
00720FF4  56                              push rsi
00720FF5  57                              push rdi
00720FF6  41 54                           push r12
00720FF8  41 55                           push r13
00720FFA  41 56                           push r14
00720FFC  41 57                           push r15
00720FFE  48 81 EC A0 00 00 00            sub rsp, 0xa0
00721005  4D 8B D0                        mov r10, r8
00721008  48 8B C2                        mov rax, rdx
0072100B  4C 8B F9                        mov r15, rcx
0072100E  33 FF                           xor edi, edi
00721010  49 89 7B 80                     mov qword ptr [r11 - 0x80], rdi
00721014  44 8B E7                        mov r12d, edi
00721017  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
0072101C  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00721021  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00721025  49 89 7B 90                     mov qword ptr [r11 - 0x70], rdi
00721029  49 89 7B 88                     mov qword ptr [r11 - 0x78], rdi
0072102D  0F 57 C0                        xorps xmm0, xmm0
00721030  41 0F 11 43 B8                  movups xmmword ptr [r11 - 0x48], xmm0
00721035  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
0072103E  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
00721046  44 8A B2 32 02 00 00            mov r14b, byte ptr [rdx + 0x232]
0072104D  44 88 74 24 41                  mov byte ptr [rsp + 0x41], r14b
00721052  45 84 F6                        test r14b, r14b
00721055  0F 84 00 02 00 00               je 0x14072125b
0072105B  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00721065  48 8B CB                        mov rcx, rbx
00721068  48 3B C3                        cmp rax, rbx
0072106B  48 0F 42 C8                     cmovb rcx, rax
0072106F  8B 01                           mov eax, dword ptr [rcx]
00721071  89 01                           mov dword ptr [rcx], eax
00721073  48 8B 82 B8 00 00 00            mov rax, qword ptr [rdx + 0xb8]
0072107A  48 39 B8 10 03 00 00            cmp qword ptr [rax + 0x310], rdi
00721081  74 2E                           je 0x1407210b1
00721083  0F B7 80 EC 06 00 00            movzx eax, word ptr [rax + 0x6ec]
0072108A  B9 4C 01 00 00                  mov ecx, 0x14c
0072108F  66 3B C1                        cmp ax, cx
00721092  74 0D                           je 0x1407210a1
00721094  B9 C4 01 00 00                  mov ecx, 0x1c4
00721099  66 3B C1                        cmp ax, cx
0072109C  40 8A C7                        mov al, dil
0072109F  75 02                           jne 0x1407210a3
007210A1  B0 01                           mov al, 1
007210A3  88 44 24 42                     mov byte ptr [rsp + 0x42], al
007210A7  84 C0                           test al, al
007210A9  41 B8 04 00 00 00               mov r8d, 4
007210AF  75 06                           jne 0x1407210b7
007210B1  41 B8 08 00 00 00               mov r8d, 8
007210B7  41 8B D1                        mov edx, r9d
007210BA  49 8B CA                        mov rcx, r10
007210BD  E8 FE 80 1C 00                  call 0x1408e91c0
007210C2  4C 8B AC 24 18 01 00 00         mov r13, qword ptr [rsp + 0x118]
007210CA  4D 85 ED                        test r13, r13
007210CD  74 43                           je 0x140721112
007210CF  49 8D 45 01                     lea rax, [r13 + 1]
007210D3  48 3B C3                        cmp rax, rbx
007210D6  48 0F 43 C3                     cmovae rax, rbx
007210DA  90                              nop
007210DB  8A 00                           mov al, byte ptr [rax]
007210DD  88 44 24 40                     mov byte ptr [rsp + 0x40], al
007210E1  0F B6 C8                        movzx ecx, al
007210E4  E8 E7 93 2A 00                  call 0x1409ca4d0
007210E9  44 8B F0                        mov r14d, eax
007210EC  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
007210F1  85 C0                           test eax, eax
007210F3  74 27                           je 0x14072111c
007210F5  41 F6 C5 03                     test r13b, 3
007210F9  74 05                           je 0x140721100
007210FB  E8 D0 8E 17 00                  call 0x140899fd0
00721100  4B 8D 0C 2E                     lea rcx, [r14 + r13]
00721104  48 3B CB                        cmp rcx, rbx
00721107  77 05                           ja 0x14072110e
00721109  49 3B CD                        cmp rcx, r13
0072110C  73 0E                           jae 0x14072111c
0072110E  8A 03                           mov al, byte ptr [rbx]
00721110  EB 05                           jmp 0x140721117
00721112  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00721117  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
0072111C  48 8B B4 24 08 01 00 00         mov rsi, qword ptr [rsp + 0x108]
00721124  48 85 F6                        test rsi, rsi
00721127  0F 84 A2 00 00 00               je 0x1407211cf
0072112D  39 BC 24 10 01 00 00            cmp dword ptr [rsp + 0x110], edi
00721134  0F 84 95 00 00 00               je 0x1407211cf
0072113A  40 F6 C6 03                     test sil, 3
0072113E  74 05                           je 0x140721145
00721140  E8 8B 8E 17 00                  call 0x140899fd0
00721145  44 8B A4 24 10 01 00 00         mov r12d, dword ptr [rsp + 0x110]
0072114D  49 8D 04 34                     lea rax, [r12 + rsi]
00721151  48 3B C3                        cmp rax, rbx
00721154  77 05                           ja 0x14072115b
00721156  48 3B C6                        cmp rax, rsi
00721159  73 07                           jae 0x140721162
0072115B  8A 03                           mov al, byte ptr [rbx]
0072115D  44 8B 74 24 50                  mov r14d, dword ptr [rsp + 0x50]
00721162  8B 8C 24 10 01 00 00            mov ecx, dword ptr [rsp + 0x110]
00721169  83 C1 03                        add ecx, 3
0072116C  41 BF FC FF FF FF               mov r15d, 0xfffffffc
00721172  41 23 CF                        and ecx, r15d
00721175  41 8B C6                        mov eax, r14d
00721178  F7 D0                           not eax
0072117A  3B C8                           cmp ecx, eax
0072117C  76 0A                           jbe 0x140721188
0072117E  B8 0D 00 00 C0                  mov eax, 0xc000000d
00721183  E9 8E 05 00 00                  jmp 0x140721716
00721188  3B 8C 24 10 01 00 00            cmp ecx, dword ptr [rsp + 0x110]
0072118F  73 0A                           jae 0x14072119b
00721191  B8 0D 00 00 C0                  mov eax, 0xc000000d
00721196  E9 7B 05 00 00                  jmp 0x140721716
0072119B  42 8D 14 31                     lea edx, [rcx + r14]
0072119F  B9 61 00 00 00                  mov ecx, 0x61
007211A4  41 B8 49 6F 53 73               mov r8d, 0x73536f49
007211AA  E8 41 0F 46 00                  call 0x140b820f0
007211AF  48 8B D8                        mov rbx, rax
007211B2  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007211B7  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
007211BC  4D 8B C4                        mov r8, r12
007211BF  48 8B D6                        mov rdx, rsi
007211C2  48 8B C8                        mov rcx, rax
007211C5  E8 76 56 FA FF                  call 0x1406c6840
007211CA  4C 8B E7                        mov r12, rdi
007211CD  EB 34                           jmp 0x140721203
007211CF  89 BC 24 10 01 00 00            mov dword ptr [rsp + 0x110], edi
007211D6  4D 85 ED                        test r13, r13
007211D9  74 1D                           je 0x1407211f8
007211DB  41 8B D6                        mov edx, r14d
007211DE  B9 21 01 00 00                  mov ecx, 0x121
007211E3  41 B8 49 6F 53 73               mov r8d, 0x73536f49
007211E9  E8 02 0F 46 00                  call 0x140b820f0
007211EE  48 8B D8                        mov rbx, rax
007211F1  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007211F6  EB 05                           jmp 0x1407211fd
007211F8  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
007211FD  41 BF FC FF FF FF               mov r15d, 0xfffffffc
00721203  4D 85 ED                        test r13, r13
00721206  74 2A                           je 0x140721232
00721208  8B B4 24 10 01 00 00            mov esi, dword ptr [rsp + 0x110]
0072120F  83 C6 03                        add esi, 3
00721212  49 23 F7                        and rsi, r15
00721215  48 03 F3                        add rsi, rbx
00721218  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
0072121D  45 8B C6                        mov r8d, r14d
00721220  49 8B D5                        mov rdx, r13
00721223  48 8B CE                        mov rcx, rsi
00721226  E8 15 56 FA FF                  call 0x1406c6840
0072122B  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
0072122F  88 46 01                        mov byte ptr [rsi + 1], al
00721232  44 8A 74 24 41                  mov r14b, byte ptr [rsp + 0x41]
00721237  4C 8B BC 24 E0 00 00 00         mov r15, qword ptr [rsp + 0xe0]
0072123F  EB 5C                           jmp 0x14072129d
00721241  8B D8                           mov ebx, eax
00721243  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00721248  48 85 C9                        test rcx, rcx
0072124B  74 07                           je 0x140721254
0072124D  33 D2                           xor edx, edx
0072124F  E8 1C 16 46 00                  call 0x140b82870
00721254  8B C3                           mov eax, ebx
00721256  E9 BB 04 00 00                  jmp 0x140721716
0072125B  48 39 BC 24 08 01 00 00         cmp qword ptr [rsp + 0x108], rdi
00721263  74 1A                           je 0x14072127f
00721265  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0072126A  39 BC 24 10 01 00 00            cmp dword ptr [rsp + 0x110], edi
00721271  48 0F 45 84 24 08 01 00 00      cmovne rax, qword ptr [rsp + 0x108]
0072127A  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0072127F  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00721284  4C 8B AC 24 18 01 00 00         mov r13, qword ptr [rsp + 0x118]
0072128C  4D 85 ED                        test r13, r13
0072128F  49 0F 45 C5                     cmovne rax, r13
00721293  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00721298  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
0072129D  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007212A2  48 85 C9                        test rcx, rcx
007212A5  74 4C                           je 0x1407212f3
007212A7  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
007212AC  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007212B1  8B 94 24 10 01 00 00            mov edx, dword ptr [rsp + 0x110]
007212B8  E8 67 9C FF FF                  call 0x14071af24
007212BD  8B F0                           mov esi, eax
007212BF  85 C0                           test eax, eax
007212C1  79 30                           jns 0x1407212f3
007212C3  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007212C8  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
007212D0  48 89 41 08                     mov qword ptr [rcx + 8], rax
007212D4  EB 07                           jmp 0x1407212dd
007212D6  8B F0                           mov esi, eax
007212D8  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
007212DD  48 85 DB                        test rbx, rbx
007212E0  74 0A                           je 0x1407212ec
007212E2  33 D2                           xor edx, edx
007212E4  48 8B CB                        mov rcx, rbx
007212E7  E8 84 15 46 00                  call 0x140b82870
007212EC  8B C6                           mov eax, esi
007212EE  E9 23 04 00 00                  jmp 0x140721716
007212F3  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
007212F8  48 85 F6                        test rsi, rsi
007212FB  74 25                           je 0x140721322
007212FD  48 8B CE                        mov rcx, rsi
00721300  E8 0B 84 20 00                  call 0x140929710
00721305  84 C0                           test al, al
00721307  75 19                           jne 0x140721322
00721309  48 85 DB                        test rbx, rbx
0072130C  74 0A                           je 0x140721318
0072130E  33 D2                           xor edx, edx
00721310  48 8B CB                        mov rcx, rbx
00721313  E8 58 15 46 00                  call 0x140b82870
00721318  B8 78 00 00 C0                  mov eax, 0xc0000078
0072131D  E9 F4 03 00 00                  jmp 0x140721716
00721322  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00721327  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
0072132C  45 8A C6                        mov r8b, r14b
0072132F  33 D2                           xor edx, edx
00721331  49 8B CF                        mov rcx, r15
00721334  E8 F7 C1 B7 FF                  call 0x14029d530
00721339  8B F0                           mov esi, eax
0072133B  85 C0                           test eax, eax
0072133D  78 9E                           js 0x1407212dd
0072133F  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00721344  4D 8D 7E 50                     lea r15, [r14 + 0x50]
00721348  4C 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r15
00721350  41 8B 37                        mov esi, dword ptr [r15]
00721353  40 F6 C6 02                     test sil, 2
00721357  0F 84 A3 00 00 00               je 0x140721400
0072135D  C1 EE 02                        shr esi, 2
00721360  40 80 E6 01                     and sil, 1
00721364  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0072136D  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00721374  90                              nop
00721375  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0072137A  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
00721381  45 33 C0                        xor r8d, r8d
00721384  33 D2                           xor edx, edx
00721386  E8 A5 EE AE FF                  call 0x140210230
0072138B  4C 8B C8                        mov r9, rax
0072138E  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00721393  B8 01 00 00 00                  mov eax, 1
00721398  87 43 74                        xchg dword ptr [rbx + 0x74], eax
0072139B  85 C0                           test eax, eax
0072139D  75 1B                           jne 0x1407213ba
0072139F  4D 85 C9                        test r9, r9
007213A2  74 05                           je 0x1407213a9
007213A4  41 C6 41 0A 01                  mov byte ptr [r9 + 0xa], 1
007213A9  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
007213AE  49 8B CE                        mov rcx, r14
007213B1  E8 6A E6 AE FF                  call 0x14020fa20
007213B6  8B DF                           mov ebx, edi
007213B8  EB 20                           jmp 0x1407213da
007213BA  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007213BF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007213C4  44 8A C6                        mov r8b, sil
007213C7  8A 54 24 41                     mov dl, byte ptr [rsp + 0x41]
007213CB  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
007213D0  49 8B CE                        mov rcx, r14
007213D3  E8 00 D3 18 00                  call 0x1408ae6d8
007213D8  8B D8                           mov ebx, eax
007213DA  40 38 7C 24 40                  cmp byte ptr [rsp + 0x40], dil
007213DF  74 13                           je 0x1407213f4
007213E1  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
007213E6  48 85 C9                        test rcx, rcx
007213E9  74 49                           je 0x140721434
007213EB  33 D2                           xor edx, edx
007213ED  E8 7E 14 46 00                  call 0x140b82870
007213F2  EB 40                           jmp 0x140721434
007213F4  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
007213F9  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
007213FE  EB 57                           jmp 0x140721457
00721400  BA 18 00 00 00                  mov edx, 0x18
00721405  8D 4A 28                        lea ecx, [rdx + 0x28]
00721408  41 B8 49 6F 45 76               mov r8d, 0x76456f49
0072140E  E8 DD 0C 46 00                  call 0x140b820f0
00721413  4C 8B E0                        mov r12, rax
00721416  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0072141B  48 85 C0                        test rax, rax
0072141E  75 23                           jne 0x140721443
00721420  48 85 DB                        test rbx, rbx
00721423  74 0A                           je 0x14072142f
00721425  33 D2                           xor edx, edx
00721427  48 8B CB                        mov rcx, rbx
0072142A  E8 41 14 46 00                  call 0x140b82870
0072142F  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00721434  49 8B CE                        mov rcx, r14
00721437  E8 14 7F BD FF                  call 0x1402f9350
0072143C  8B C3                           mov eax, ebx
0072143E  E9 D3 02 00 00                  jmp 0x140721716
00721443  45 33 C0                        xor r8d, r8d
00721446  41 8D 50 01                     lea edx, [r8 + 1]
0072144A  48 8B C8                        mov rcx, rax
0072144D  E8 BE C8 CE FF                  call 0x14040dd10
00721452  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00721457  49 8B CE                        mov rcx, r14
0072145A  E8 91 C1 B7 FF                  call 0x14029d5f0
0072145F  49 8B CE                        mov rcx, r14
00721462  E8 B9 9C B7 FF                  call 0x14029b120
00721467  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0072146C  45 33 C0                        xor r8d, r8d
0072146F  8A 50 4C                        mov dl, byte ptr [rax + 0x4c]
00721472  48 8B C8                        mov rcx, rax
00721475  E8 A6 62 AE FF                  call 0x140207720
0072147A  48 8B F0                        mov rsi, rax
0072147D  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00721482  48 85 C0                        test rax, rax
00721485  75 20                           jne 0x1407214a7
00721487  41 8B 07                        mov eax, dword ptr [r15]
0072148A  A8 02                           test al, 2
0072148C  75 0A                           jne 0x140721498
0072148E  33 D2                           xor edx, edx
00721490  49 8B CC                        mov rcx, r12
00721493  E8 D8 13 46 00                  call 0x140b82870
00721498  33 D2                           xor edx, edx
0072149A  49 8B CE                        mov rcx, r14
0072149D  E8 32 CE 2F 00                  call 0x140a1e2d4
007214A2  E9 D3 00 00 00                  jmp 0x14072157a
007214A7  4C 89 B0 C0 00 00 00            mov qword ptr [rax + 0xc0], r14
007214AE  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
007214B6  48 89 86 98 00 00 00            mov qword ptr [rsi + 0x98], rax
007214BD  8A 44 24 41                     mov al, byte ptr [rsp + 0x41]
007214C1  88 46 40                        mov byte ptr [rsi + 0x40], al
007214C4  40 38 7C 24 40                  cmp byte ptr [rsp + 0x40], dil
007214C9  74 0D                           je 0x1407214d8
007214CB  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
007214D3  48 8B CF                        mov rcx, rdi
007214D6  EB 14                           jmp 0x1407214ec
007214D8  C7 46 10 04 00 00 00            mov dword ptr [rsi + 0x10], 4
007214DF  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
007214E7  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
007214EC  48 89 4E 50                     mov qword ptr [rsi + 0x50], rcx
007214F0  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
007214F4  48 89 7E 58                     mov qword ptr [rsi + 0x58], rdi
007214F8  4C 8B BE B8 00 00 00            mov r15, qword ptr [rsi + 0xb8]
007214FF  41 C6 47 B8 19                  mov byte ptr [r15 - 0x48], 0x19
00721504  4D 89 77 E8                     mov qword ptr [r15 - 0x18], r14
00721508  48 89 9E A0 00 00 00            mov qword ptr [rsi + 0xa0], rbx
0072150F  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00721514  49 89 47 D0                     mov qword ptr [r15 - 0x30], rax
00721518  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
0072151F  41 89 47 D8                     mov dword ptr [r15 - 0x28], eax
00721523  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00721528  8B 40 30                        mov eax, dword ptr [rax + 0x30]
0072152B  A8 04                           test al, 4
0072152D  74 76                           je 0x1407215a5
0072152F  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
00721536  85 C0                           test eax, eax
00721538  74 62                           je 0x14072159c
0072153A  8B D0                           mov edx, eax
0072153C  B9 41 00 00 00                  mov ecx, 0x41
00721541  41 B8 49 6F 53 42               mov r8d, 0x42536f49
00721547  E8 A4 0B 46 00                  call 0x140b820f0
0072154C  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
00721550  48 85 C0                        test rax, rax
00721553  75 3E                           jne 0x140721593
00721555  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0072155D  8B 00                           mov eax, dword ptr [rax]
0072155F  D1 E8                           shr eax, 1
00721561  24 01                           and al, 1
00721563  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00721567  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
0072156C  45 33 C0                        xor r8d, r8d
0072156F  48 8B D6                        mov rdx, rsi
00721572  49 8B CE                        mov rcx, r14
00721575  E8 4E D0 18 00                  call 0x1408ae5c8
0072157A  48 85 DB                        test rbx, rbx
0072157D  74 0A                           je 0x140721589
0072157F  33 D2                           xor edx, edx
00721581  48 8B CB                        mov rcx, rbx
00721584  E8 E7 12 46 00                  call 0x140b82870
00721589  B8 9A 00 00 C0                  mov eax, 0xc000009a
0072158E  E9 83 01 00 00                  jmp 0x140721716
00721593  83 4E 10 70                     or dword ptr [rsi + 0x10], 0x70
00721597  E9 CA 00 00 00                  jmp 0x140721666
0072159C  48 89 7E 18                     mov qword ptr [rsi + 0x18], rdi
007215A0  E9 C1 00 00 00                  jmp 0x140721666
007215A5  A8 10                           test al, 0x10
007215A7  0F 84 B9 00 00 00               je 0x140721666
007215AD  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
007215B4  85 C0                           test eax, eax
007215B6  0F 84 BD 00 00 00               je 0x140721679
007215BC  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
007215C1  41 B1 01                        mov r9b, 1
007215C4  45 33 C0                        xor r8d, r8d
007215C7  8B D0                           mov edx, eax
007215C9  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
007215D1  E8 1A D6 B7 FF                  call 0x14029ebf0
007215D6  48 8B D8                        mov rbx, rax
007215D9  48 85 C0                        test rax, rax
007215DC  75 0A                           jne 0x1407215e8
007215DE  B9 9A 00 00 C0                  mov ecx, 0xc000009a
007215E3  E8 68 54 BD FF                  call 0x1402f6a50
007215E8  45 0F B6 67 B8                  movzx r12d, byte ptr [r15 - 0x48]
007215ED  41 B8 01 00 00 00               mov r8d, 1
007215F3  8A 54 24 41                     mov dl, byte ptr [rsp + 0x41]
007215F7  48 8B CB                        mov rcx, rbx
007215FA  E8 91 A3 B1 FF                  call 0x14023b990
007215FF  8B 05 B7 55 8A 00               mov eax, dword ptr [rip + 0x8a55b7]
00721605  A8 01                           test al, 1
00721607  74 16                           je 0x14072161f
00721609  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
0072160E  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
00721612  4A 8B 54 E0 70                  mov rdx, qword ptr [rax + r12*8 + 0x70]
00721617  48 8B CB                        mov rcx, rbx
0072161A  E8 49 4E D3 FF                  call 0x140456468
0072161F  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
00721626  EB 51                           jmp 0x140721679
00721628  8B D8                           mov ebx, eax
0072162A  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0072162F  0F B6 51 50                     movzx edx, byte ptr [rcx + 0x50]
00721633  D1 EA                           shr edx, 1
00721635  83 E2 01                        and edx, 1
00721638  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
0072163C  4C 8B 4C 24 70                  mov r9, qword ptr [rsp + 0x70]
00721641  45 33 C0                        xor r8d, r8d
00721644  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00721649  E8 7A CF 18 00                  call 0x1408ae5c8
0072164E  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00721653  48 85 C9                        test rcx, rcx
00721656  74 07                           je 0x14072165f
00721658  33 D2                           xor edx, edx
0072165A  E8 11 12 46 00                  call 0x140b82870
0072165F  8B C3                           mov eax, ebx
00721661  E9 B0 00 00 00                  jmp 0x140721716
00721666  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
0072166E  48 89 46 70                     mov qword ptr [rsi + 0x70], rax
00721672  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
00721679  41 89 47 C0                     mov dword ptr [r15 - 0x40], eax
0072167D  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00721682  49 89 47 C8                     mov qword ptr [r15 - 0x38], rax
00721686  41 88 7F BA                     mov byte ptr [r15 - 0x46], dil
0072168A  40 8A C7                        mov al, dil
0072168D  40 38 BC 24 20 01 00 00         cmp byte ptr [rsp + 0x120], dil
00721695  74 07                           je 0x14072169e
00721697  41 C6 47 BA 01                  mov byte ptr [r15 - 0x46], 1
0072169C  B0 01                           mov al, 1
0072169E  40 38 BC 24 00 01 00 00         cmp byte ptr [rsp + 0x100], dil
007216A6  74 06                           je 0x1407216ae
007216A8  0C 02                           or al, 2
007216AA  41 88 47 BA                     mov byte ptr [r15 - 0x46], al
007216AE  4D 85 ED                        test r13, r13
007216B1  74 06                           je 0x1407216b9
007216B3  0C 04                           or al, 4
007216B5  41 88 47 BA                     mov byte ptr [r15 - 0x46], al
007216B9  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
007216C1  8A 5C 24 40                     mov bl, byte ptr [rsp + 0x40]
007216C5  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
007216C9  44 8A 7C 24 41                  mov r15b, byte ptr [rsp + 0x41]
007216CE  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
007216D3  45 33 C9                        xor r9d, r9d
007216D6  4D 8B C6                        mov r8, r14
007216D9  48 8B D6                        mov rdx, rsi
007216DC  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
007216E1  E8 5A 9D 1C 00                  call 0x1408eb440
007216E6  84 DB                           test bl, bl
007216E8  75 2C                           jne 0x140721716
007216EA  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
007216F2  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
007216F7  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
007216FF  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00721704  45 8A CF                        mov r9b, r15b
00721707  4C 8B C6                        mov r8, rsi
0072170A  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0072170F  8B C8                           mov ecx, eax
00721711  E8 26 B7 18 00                  call 0x1408ace3c
00721716  48 81 C4 A0 00 00 00            add rsp, 0xa0
0072171D  41 5F                           pop r15
0072171F  41 5E                           pop r14
00721721  41 5D                           pop r13
00721723  41 5C                           pop r12
00721725  5F                              pop rdi
00721726  5E                              pop rsi
00721727  5B                              pop rbx
00721728  C3                              ret
00721729  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryQuotaInformationFile(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int8 a5, __int64 a6, unsigned int a7, __int64 a8, unsigned __int8 a9)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int8 v_stack_m96;
    unsigned __int8 v_stack_m97;
    unsigned __int8 v_stack_m98;
    unsigned int v_stack_mA8;
    unsigned __int8 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p8;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    v_rdi = 0;
    *(unsigned __int64 *)(v_rsp - 128) = 0;
    v_stack_m68 = 0;
    v_stack_m90 = 0;
    v_stack_m88 = 0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm0;
    v_stack_m58 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m97 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_0072125B;
    a1 = v_rbx;
    if (a2 < v_rbx) { a1 = a2; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) == 0) goto loc_007210B1;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 332) goto loc_007210A1;
    result = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 452) {
        result = 1;
    }
    v_stack_m96 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) {
        a3 = 8;
    }
    result = ProbeForWrite(a3, (unsigned int)(a4), a3, a4);
    if (a8 == 0) goto loc_00721112;
    result = a8 + 1;
    if ((a8 + 1) >= v_rbx) { result = v_rbx; }
    v_stack_m98 = (unsigned __int8)(*(unsigned __int8 *)(result));
    result = RtlLengthRequiredSid((unsigned __int8)(*(unsigned __int8 *)(result)), (unsigned int)(a4), a3, a4);
    v_stack_m88 = (unsigned int)((unsigned int)((unsigned int)(result)));
    if ((unsigned int)(result) == 0) goto loc_0072111C;
    if ((((unsigned __int8)(a8)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment((unsigned __int8)(*(unsigned __int8 *)(result)), (unsigned int)(a4), a3, a4);
    }
    if (((unsigned int)((unsigned int)(result)) + a8 * 1) > v_rbx) goto loc_0072110E;
    if (((unsigned int)((unsigned int)(result)) + a8 * 1) >= a8) goto loc_0072111C;
loc_0072110E:
    goto loc_00721117;
loc_00721112:
    v_stack_m98 = 0;
loc_00721117:
loc_0072111C:
    if (a6 == 0) goto loc_007211CF;
    if (a7 == 0) goto loc_007211CF;
    result = *(unsigned __int8 *)(v_rbx);
    if ((((unsigned __int8)(a6)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment((unsigned int)((unsigned int)(result)) + a8 * 1, (unsigned int)(a4), a3, a4);
    }
    if (((unsigned int)(a7) + a6 * 1) > v_rbx) goto loc_0072115B;
    result = (unsigned int)(a7) + a6 * 1;
    v_r14 = (unsigned int)(v_stack_m88);
    if (((unsigned int)(a7) + a6 * 1) < a6) {
        result = *(unsigned __int8 *)(v_rbx);
        v_r14 = v_stack_m88;
    }
    a1 = (unsigned int)(((unsigned int)(a7)) + (3));
    a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(0xFFFFFFFCULL))));
    result = (unsigned int)(~((unsigned int)((unsigned int)(v_r14))));
    if (((unsigned int)(a1)) <= ((unsigned int)(result))) goto loc_00721188;
    goto loc_00721716;
loc_00721188:
    if (((unsigned int)(a1)) >= a7) goto loc_0072119B;
    goto loc_00721716;
loc_0072119B:
    result = ExAllocatePool2(97, a1 + v_r14 * 1, (unsigned int)(0x73536F49ULL), a4);
    v_stack_m90 = result;
    v_stack_m78 = result;
    result = memcpy(result, a6, (unsigned int)(a7), a4);
    goto loc_00721203;
loc_007211CF:
    v_stack_p38 = 0;
    if (a8 == 0) goto loc_007211F8;
    result = ExAllocatePool2(289, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(0x73536F49ULL), a4);
    v_stack_m90 = result;
    goto loc_007211FD;
loc_007211F8:
loc_007211FD:
loc_00721203:
    v_rsi = a6;
    if (a8 != 0) {
        v_rsi = a7;
        v_rsi = (unsigned int)((v_rsi) + (3));
        v_rsi = (v_rsi) & ((unsigned int)(0xFFFFFFFCULL));
        v_rsi = (v_rsi) + (v_stack_m90);
        v_stack_m70 = v_rsi;
        a3 = (unsigned int)(v_r14);
        a2 = a8;
        a1 = v_rsi;
        result = memcpy(a1, a2, a3, a4);
        result = v_stack_m98;
        *(unsigned __int8 *)(v_rsi + 1) = (unsigned __int8)(result);
    }
    goto loc_0072129D;
loc_0072125B:
    if (a6 != 0) {
        result = v_stack_m78;
        if (a7 != 0) { result = a6; }
        v_stack_m78 = result;
    }
    result = v_stack_m70;
    if (a8 != 0) { result = a8; }
    v_stack_m70 = result;
loc_0072129D:
    if (v_stack_m78 == 0) goto loc_007212F3;
    v_stack_m60 = 0;
    result = IopCheckGetQuotaBufferValidity(v_stack_m78, (unsigned int)(a7), v_stack_m60, a4);
    if (!sign_flag) goto loc_007212F3;
    *(unsigned __int64 *)(v_stack_p10 + 8) = v_stack_m60;
    goto loc_007212DD;
loc_007212DD:
    result = v_stack_m60;
    if (v_stack_m90 != 0) {
        a2 = 0;
        a1 = v_stack_m90;
        result = ExFreePoolWithTag(a1, a2, v_stack_m60, a4);
    }
    goto loc_00721716;
loc_007212F3:
    if (v_stack_m70 == 0) goto loc_00721322;
    result = RtlValidSid(v_stack_m70, a2, v_stack_m60, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00721322;
    if (v_stack_m90 != 0) {
        a2 = 0;
        a1 = v_stack_m90;
        result = ExFreePoolWithTag(a1, a2, v_stack_m60, a4);
    }
    goto loc_00721716;
loc_00721322:
    v_stack_mB8 = 0;
    a2 = 0;
    result = IopReferenceFileObject(v_stack_p8, a2, (unsigned __int8)(v_stack_m97), v_stack_m80);
    if (sign_flag) goto loc_007212DD;
    v_stack_m50 = v_stack_m80 + 80;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m80 + 80)))) & (2)) == 0) goto loc_00721400;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m80 + 80))) >> (2));
    v_rsi = (unsigned __int8)((v_rsi) & (1));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m80 + 128, a2, a3, v_stack_m80);
    v_stack_m98 = 0;
    if (1 != 0) goto loc_007213BA;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(v_stack_m80, a2, a3, result);
    goto loc_007213DA;
loc_007213BA:
    v_stack_mB8 = v_stack_m98;
    result = IopWaitAndAcquireFileObjectLock(v_stack_m80, v_stack_m97, (unsigned __int8)(v_rsi), result);
loc_007213DA:
    if (v_stack_m98 == 0) goto loc_007213F4;
    if (v_stack_m90 == 0) goto loc_00721434;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, a2, (unsigned __int8)(v_rsi), result);
    goto loc_00721434;
loc_007213F4:
    v_stack_m98 = 1;
    goto loc_00721457;
loc_00721400:
    result = ExAllocatePool2(24 + 40, 24, (unsigned int)(0x76456F49ULL), result);
    v_stack_m68 = result;
    if (result != 0) goto loc_00721443;
    if (v_stack_m90 != 0) {
        a2 = 0;
        a1 = v_stack_m90;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x76456F49ULL), result);
    }
loc_00721434:
    result = ObfDereferenceObject(v_stack_m80, a2, (unsigned int)(0x76456F49ULL), result);
    goto loc_00721716;
loc_00721443:
    a3 = 0;
    result = KeInitializeEvent((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a3 + 1, a3, result);
    v_stack_m98 = 0;
loc_00721457:
    result = IopResetEvent(v_stack_m80, a3 + 1, a3, result);
    result = IoGetRelatedDeviceObject(v_stack_m80, a3 + 1, a3, result);
    v_stack_m88 = result;
    a3 = 0;
    result = IopAllocateIrpExReturn(result, *(unsigned __int8 *)(result + 76), a3, result);
    v_stack_m60 = result;
    if (result != 0) goto loc_007214A7;
    result = (unsigned int)(*(unsigned int *)(v_stack_m80 + 80));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m80 + 80)))) & (2)) == 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, result);
    }
    a2 = 0;
    result = IopAllocateIrpCleanup(v_stack_m80, a2, a3, result);
    goto loc_0072157A;
loc_007214A7:
    *(unsigned __int64 *)(result + 192) = v_stack_m80;
    *(unsigned __int64 *)(result + 152) = v_stack_m58;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)(v_stack_m97);
    if (v_stack_m98 == 0) goto loc_007214D8;
    goto loc_007214EC;
loc_007214D8:
    *(unsigned int *)(result + 16) = 4;
loc_007214EC:
    *(unsigned __int64 *)(result + 80) = v_stack_m68;
    *(unsigned __int64 *)(result + 72) = v_stack_m48;
    *(unsigned __int64 *)(result + 88) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 72) = 25;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 24) = v_stack_m80;
    *(unsigned __int64 *)(result + 160) = (unsigned int)(0xC000009AULL);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 48) = v_stack_m78;
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 40) = (unsigned int)((unsigned int)(a7));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m88 + 48)))) & (4)) == 0) goto loc_007215A5;
    if ((unsigned int)((unsigned int)(v_stack_p20)) == 0) goto loc_0072159C;
    result = ExAllocatePool2(65, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), (unsigned int)(0x42536F49ULL), result);
    *(unsigned __int64 *)(result + 24) = result;
    if (result != 0) goto loc_00721593;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m50))) >> (1));
    result = (unsigned __int8)((result) & (1));
    v_stack_mB8 = (unsigned __int8)(result);
    a3 = 0;
    result = IopExceptionCleanupEx(v_stack_m80, result, a3, v_stack_m68);
loc_0072157A:
    if ((unsigned int)(0xC000009AULL) != 0) {
        a2 = 0;
        a1 = (unsigned int)(0xC000009AULL);
        result = ExFreePoolWithTag(a1, a2, a3, v_stack_m68);
    }
    goto loc_00721716;
loc_00721593:
    goto loc_00721666;
loc_0072159C:
    *(unsigned __int64 *)(result + 24) = 0;
    goto loc_00721666;
loc_007215A5:
    if ((((unsigned __int8)((unsigned int)(0xC000009AULL))) & (16)) == 0) goto loc_00721666;
    if ((unsigned int)((unsigned int)(v_stack_p20)) == 0) goto loc_00721679;
    v_stack_mB8 = result;
    a3 = 0;
    result = IoAllocateMdl(v_stack_p18, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), a3, 1);
    if (result == 0) {
        a1 = 0xC000009AULL;
        result = RtlRaiseStatus(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), a3, 1);
    }
    result = MmProbeAndLockPages(result, v_stack_m97, 1, 1);
    result = (unsigned int)(*(unsigned int *)(v_rip + 9065911));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9065911)))) & (1)) != 0) {
        a3 = v_stack_m88;
        result = *(unsigned __int64 *)(a3 + 8);
        a2 = *(unsigned __int64 *)(result + *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 72) * 8 + 112);
        a1 = result;
        result = MmUpdateMdlTracker(a1, a2, a3, 1);
    }
    goto loc_00721679;
loc_00721666:
    *(unsigned __int64 *)(result + 112) = v_stack_p18;
loc_00721679:
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 64) = (unsigned int)((unsigned int)(v_stack_p20));
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 56) = v_stack_m70;
    *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 70) = 0;
    result = 0;
    if (a9 != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 70) = 1;
        result = 1;
    }
    if (a5 != 0) {
        result = (unsigned __int8)((result) | (2));
        *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 70) = (unsigned __int8)(result);
    }
    if (a8 != 0) {
        result = (unsigned __int8)((result) | (4));
        *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 70) = (unsigned __int8)(result);
    }
    v_stack_mA8 = 2;
    v_stack_mB0 = (unsigned __int8)(v_stack_m98);
    v_stack_mB8 = (unsigned __int8)(v_stack_m97);
    a4 = 0;
    result = IopSynchronousServiceTail(v_stack_m88, result, v_stack_m80, a4);
    if ((unsigned __int8)(v_stack_m98) == 0) {
        a1 = v_stack_p10;
        v_stack_mB0 = a1;
        a1 = v_stack_m48;
        v_stack_mB8 = a1;
        a4 = (unsigned __int8)(v_stack_m97);
        a3 = result;
        a2 = v_stack_m68;
        a1 = (unsigned int)(result);
        result = IopSynchronousApiServiceTail(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryQuotaInformationFile(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint8_t Arg5, int64_t Arg6, void *Arg7, int64_t Arg8, uint8_t Arg9)
{
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint8_t v_stack_m96;
    uint8_t v_stack_m97;
    uint8_t v_stack_m98;
    uint32_t v_stack_mA8;
    uint8_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p38;
    uint64_t v_stack_p8;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    local_rdi = 0;
    *(uint64_t *)(local_rsp - 0x80) = 0;
    v_stack_m68 = 0;
    v_stack_m90 = 0;
    v_stack_m88 = 0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0x48) = v_xmm0;
    v_stack_m58 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m97 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_0072125B;
    Arg1 = local_rbx;
    if (Arg2 < local_rbx) { Arg1 = Arg2; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) == 0) goto loc_007210B1;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 332) goto loc_007210A1;
    result = 0;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 452) {
        result = 1;
    }
    v_stack_m96 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) {
        Arg3 = 8;
    }
    result = ProbeForWrite(Arg3, (uint32_t)(Arg4), Arg3, Arg4);
    if (Arg8 == 0) goto loc_00721112;
    result = Arg8 + 1;
    if ((Arg8 + 1) >= local_rbx) { result = local_rbx; }
    v_stack_m98 = (uint8_t)(*(uint8_t *)(result));
    result = RtlLengthRequiredSid((uint8_t)(*(uint8_t *)(result)), (uint32_t)(Arg4), Arg3, Arg4);
    v_stack_m88 = (uint32_t)((uint32_t)((uint32_t)(result)));
    if ((uint32_t)(result) == 0) goto loc_0072111C;
    if ((((uint8_t)(Arg8)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment((uint8_t)(*(uint8_t *)(result)), (uint32_t)(Arg4), Arg3, Arg4);
    }
    if (((uint32_t)((uint32_t)(result)) + Arg8 * 1) > local_rbx) goto loc_0072110E;
    if (((uint32_t)((uint32_t)(result)) + Arg8 * 1) >= Arg8) goto loc_0072111C;
loc_0072110E:
    goto loc_00721117;
loc_00721112:
    v_stack_m98 = 0;
loc_00721117:
loc_0072111C:
    if (Arg6 == 0) goto loc_007211CF;
    if (Arg7 == NULL) goto loc_007211CF;
    result = *(uint8_t *)(local_rbx);
    if ((((uint8_t)(Arg6)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment((uint32_t)((uint32_t)(result)) + Arg8 * 1, (uint32_t)(Arg4), Arg3, Arg4);
    }
    if (((uint32_t)(Arg7) + Arg6 * 1) > local_rbx) goto loc_0072115B;
    result = (uint32_t)(Arg7) + Arg6 * 1;
    local_r14 = (uint32_t)(v_stack_m88);
    if (((uint32_t)(Arg7) + Arg6 * 1) < Arg6) {
        result = *(uint8_t *)(local_rbx);
        local_r14 = v_stack_m88;
    }
    Arg1 = (uint32_t)(((uint32_t)(Arg7)) + (3));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(0xFFFFFFFCULL))));
    result = (uint32_t)(~((uint32_t)((uint32_t)(local_r14))));
    if (((uint32_t)(Arg1)) <= ((uint32_t)(result))) goto loc_00721188;
    goto loc_00721716;
loc_00721188:
    if (((uint32_t)(Arg1)) >= Arg7) goto loc_0072119B;
    goto loc_00721716;
loc_0072119B:
    result = ExAllocatePool2(97, Arg1 + local_r14 * 1, (uint32_t)(0x73536F49ULL), Arg4);
    v_stack_m90 = result;
    v_stack_m78 = result;
    result = memcpy(result, Arg6, (uint32_t)(Arg7), Arg4);
    goto loc_00721203;
loc_007211CF:
    v_stack_p38 = 0;
    if (Arg8 == 0) goto loc_007211F8;
    result = ExAllocatePool2(289, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(0x73536F49ULL), Arg4);
    v_stack_m90 = result;
    goto loc_007211FD;
loc_007211F8:
loc_007211FD:
loc_00721203:
    local_rsi = Arg6;
    if (Arg8 != 0) {
        local_rsi = Arg7;
        local_rsi = (uint32_t)((local_rsi) + (3));
        local_rsi = (local_rsi) & ((uint32_t)(0xFFFFFFFCULL));
        local_rsi = (local_rsi) + (v_stack_m90);
        v_stack_m70 = local_rsi;
        Arg3 = (uint32_t)(local_r14);
        Arg2 = Arg8;
        Arg1 = local_rsi;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m98;
        *(uint8_t *)(local_rsi + 0x1) = (uint8_t)(result);
    }
    goto loc_0072129D;
loc_0072125B:
    if (Arg6 != 0) {
        result = v_stack_m78;
        if (Arg7 != NULL) { result = Arg6; }
        v_stack_m78 = result;
    }
    result = v_stack_m70;
    if (Arg8 != 0) { result = Arg8; }
    v_stack_m70 = result;
loc_0072129D:
    if (v_stack_m78 == 0) goto loc_007212F3;
    v_stack_m60 = 0;
    result = IopCheckGetQuotaBufferValidity(v_stack_m78, (uint32_t)(Arg7), v_stack_m60, Arg4);
    if (!sign_flag) goto loc_007212F3;
    *(uint64_t *)(v_stack_p10 + 0x8) = v_stack_m60;
    goto loc_007212DD;
loc_007212DD:
    result = v_stack_m60;
    if (v_stack_m90 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m90;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m60, Arg4);
    }
    goto loc_00721716;
loc_007212F3:
    if (v_stack_m70 == 0) goto loc_00721322;
    result = RtlValidSid(v_stack_m70, Arg2, v_stack_m60, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00721322;
    if (v_stack_m90 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m90;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m60, Arg4);
    }
    goto loc_00721716;
loc_00721322:
    v_stack_mB8 = 0;
    Arg2 = 0;
    result = IopReferenceFileObject(v_stack_p8, Arg2, (uint8_t)(v_stack_m97), v_stack_m80);
    if (sign_flag) goto loc_007212DD;
    v_stack_m50 = v_stack_m80 + 80;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x50)))) & (2)) == 0) goto loc_00721400;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x50))) >> (2));
    local_rsi = (uint8_t)((local_rsi) & (1));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m80 + 128, Arg2, Arg3, v_stack_m80);
    v_stack_m98 = 0;
    if (1 != 0) goto loc_007213BA;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(v_stack_m80, Arg2, Arg3, result);
    goto loc_007213DA;
loc_007213BA:
    v_stack_mB8 = v_stack_m98;
    result = IopWaitAndAcquireFileObjectLock(v_stack_m80, v_stack_m97, (uint8_t)(local_rsi), result);
loc_007213DA:
    if (v_stack_m98 == 0) goto loc_007213F4;
    if (v_stack_m90 == 0) goto loc_00721434;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m90, Arg2, (uint8_t)(local_rsi), result);
    goto loc_00721434;
loc_007213F4:
    v_stack_m98 = 1;
    goto loc_00721457;
loc_00721400:
    result = ExAllocatePool2(24 + 40, 24, (uint32_t)(0x76456F49ULL), result);
    v_stack_m68 = result;
    if (result != 0) goto loc_00721443;
    if (v_stack_m90 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m90;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x76456F49ULL), result);
    }
loc_00721434:
    result = ObfDereferenceObject(v_stack_m80, Arg2, (uint32_t)(0x76456F49ULL), result);
    goto loc_00721716;
loc_00721443:
    Arg3 = 0;
    result = KeInitializeEvent((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), Arg3 + 1, Arg3, result);
    v_stack_m98 = 0;
loc_00721457:
    result = IopResetEvent(v_stack_m80, Arg3 + 1, Arg3, result);
    result = IoGetRelatedDeviceObject(v_stack_m80, Arg3 + 1, Arg3, result);
    v_stack_m88 = result;
    Arg3 = 0;
    result = IopAllocateIrpExReturn(result, *(uint8_t *)(result + 0x4C), Arg3, result);
    v_stack_m60 = result;
    if (result != 0) goto loc_007214A7;
    result = (uint32_t)(*(uint32_t *)(v_stack_m80 + 0x50));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x50)))) & (2)) == 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, result);
    }
    Arg2 = 0;
    result = IopAllocateIrpCleanup(v_stack_m80, Arg2, Arg3, result);
    goto loc_0072157A;
loc_007214A7:
    *(uint64_t *)(result + 0xC0) = v_stack_m80;
    *(uint64_t *)(result + 0x98) = v_stack_m58;
    *(uint8_t *)(result + 0x40) = (uint8_t)(v_stack_m97);
    if (v_stack_m98 == 0) goto loc_007214D8;
    goto loc_007214EC;
loc_007214D8:
    *(uint32_t *)(result + 0x10) = 4;
loc_007214EC:
    *(uint64_t *)(result + 0x50) = v_stack_m68;
    *(uint64_t *)(result + 0x48) = v_stack_m48;
    *(uint64_t *)(result + 0x58) = 0;
    *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 25;
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x18) = v_stack_m80;
    *(uint64_t *)(result + 0xA0) = (uint32_t)(0xC000009AULL);
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x30) = v_stack_m78;
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x28) = (uint32_t)((uint32_t)(Arg7));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + 0x30)))) & (4)) == 0) goto loc_007215A5;
    if ((uint32_t)((uint32_t)(v_stack_p20)) == 0) goto loc_0072159C;
    result = ExAllocatePool2(65, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), (uint32_t)(0x42536F49ULL), result);
    *(uint64_t *)(result + 0x18) = result;
    if (result != 0) goto loc_00721593;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m50))) >> (1));
    result = (uint8_t)((result) & (1));
    v_stack_mB8 = (uint8_t)(result);
    Arg3 = 0;
    result = IopExceptionCleanupEx(v_stack_m80, result, Arg3, v_stack_m68);
loc_0072157A:
    if ((uint32_t)(0xC000009AULL) != 0) {
        Arg2 = 0;
        Arg1 = (uint32_t)(0xC000009AULL);
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, v_stack_m68);
    }
    goto loc_00721716;
loc_00721593:
    goto loc_00721666;
loc_0072159C:
    *(uint64_t *)(result + 0x18) = 0;
    goto loc_00721666;
loc_007215A5:
    if ((((uint8_t)((uint32_t)(0xC000009AULL))) & (16)) == 0) goto loc_00721666;
    if ((uint32_t)((uint32_t)(v_stack_p20)) == 0) goto loc_00721679;
    v_stack_mB8 = result;
    Arg3 = 0;
    result = IoAllocateMdl(v_stack_p18, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), Arg3, 1);
    if (result == 0) {
        Arg1 = 0xC000009AULL;
        result = RtlRaiseStatus(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), Arg3, 1);
    }
    result = MmProbeAndLockPages(result, v_stack_m97, 1, 1);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x8A55B7));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8A55B7)))) & (1)) != 0) {
        Arg3 = v_stack_m88;
        result = *(uint64_t *)(Arg3 + 0x8);
        Arg2 = *(uint64_t *)(result + *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x48) * 8 + 0x70);
        Arg1 = result;
        result = MmUpdateMdlTracker(Arg1, Arg2, Arg3, 1);
    }
    goto loc_00721679;
loc_00721666:
    *(uint64_t *)(result + 0x70) = v_stack_p18;
loc_00721679:
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x40) = (uint32_t)((uint32_t)(v_stack_p20));
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x38) = v_stack_m70;
    *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x46) = 0;
    result = 0;
    if (Arg9 != 0) {
        *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x46) = 1;
        result = 1;
    }
    if (Arg5 != 0) {
        result = (uint8_t)((result) | (2));
        *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x46) = (uint8_t)(result);
    }
    if (Arg8 != 0) {
        result = (uint8_t)((result) | (4));
        *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x46) = (uint8_t)(result);
    }
    v_stack_mA8 = 2;
    v_stack_mB0 = (uint8_t)(v_stack_m98);
    v_stack_mB8 = (uint8_t)(v_stack_m97);
    Arg4 = 0;
    result = IopSynchronousServiceTail(v_stack_m88, result, v_stack_m80, Arg4);
    if ((uint8_t)(v_stack_m98) == 0) {
        Arg1 = v_stack_p10;
        v_stack_mB0 = Arg1;
        Arg1 = v_stack_m48;
        v_stack_mB8 = Arg1;
        Arg4 = (uint8_t)(v_stack_m97);
        Arg3 = result;
        Arg2 = v_stack_m68;
        Arg1 = (uint32_t)(result);
        result = IopSynchronousApiServiceTail(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x0 + rsi*1` | `64` | `R` |
| `Arg7` | `+ 0x1` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00720FE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
