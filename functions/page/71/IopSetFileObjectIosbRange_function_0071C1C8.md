# IopSetFileObjectIosbRange

- RVA: `0x0071C1C8`–`0x0071C68A` (길이 `1,218` bytes)
- VA: `0x000000014071C1C8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C7378`
- 디코드: `302`개 명령, `1,218/1,218` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0071C25C` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x0071C286` → [RtlInsertElementGenericTableAvl](../../text/3E/RtlInsertElementGenericTableAvl_function_003EE510.md) (function, `0x003EE510`)
- `0x0071C2E3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0071C349` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0071C354` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0071C385` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x0071C399` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x0071C3B4` → [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) (function, `0x0023B990`)
- `0x0071C429` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x0071C482` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0071C4D3` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0071C4EF` → [IopAllocateFileObjectExtension](../../text/41/IopAllocateFileObjectExtension_function_00418FB0.md) (function, `0x00418FB0`)
- `0x0071C50C` → [IopSetTypeSpecificFoExtension](../../text/45/IopSetTypeSpecificFoExtension_function_00452B50.md) (function, `0x00452B50`)
- `0x0071C55D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0071C567` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0071C603` → [MmUnmapLockedPages](../../text/24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)
- `0x0071C60D` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x0071C617` → [IoFreeMdl](../../text/29/IoFreeMdl_function_0029EA80.md) (function, `0x0029EA80`)
- `0x0071C62B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0071C635` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0071C653` → [RtlDeleteElementGenericTableAvl](../../text/3E/RtlDeleteElementGenericTableAvl_function_003EE750.md) (function, `0x003EE750`)
- `0x0071C663` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0071C66F` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)

### Direct callers
- [sub_006DA8DA](../../text/6D/Unknown_function_006DA8DA.md) at `0x006DA9BE`

### Static image references
- `0x0071C255` → RVA `0x00F8D880` (`.data`; read)
- `0x0071C27F` → RVA `0x00F8D800` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x0071C25C` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (`PAGE` → `.text`)
  - `0x0071C286` → [RtlInsertElementGenericTableAvl](../../text/3E/RtlInsertElementGenericTableAvl_function_003EE510.md) (`PAGE` → `.text`)
  - `0x0071C2E3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0071C385` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x0071C399` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGE` → `.text`)
  - `0x0071C3B4` → [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) (`PAGE` → `.text`)
  - `0x0071C429` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (`PAGE` → `.text`)
  - `0x0071C482` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0071C4D3` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0071C4EF` → [IopAllocateFileObjectExtension](../../text/41/IopAllocateFileObjectExtension_function_00418FB0.md) (`PAGE` → `.text`)
  - `0x0071C50C` → [IopSetTypeSpecificFoExtension](../../text/45/IopSetTypeSpecificFoExtension_function_00452B50.md) (`PAGE` → `.text`)
  - `0x0071C55D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0071C567` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0071C603` → [MmUnmapLockedPages](../../text/24/MmUnmapLockedPages_function_00246E60.md) (`PAGE` → `.text`)
  - `0x0071C60D` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x0071C617` → [IoFreeMdl](../../text/29/IoFreeMdl_function_0029EA80.md) (`PAGE` → `.text`)
  - `0x0071C62B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0071C635` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0071C653` → [RtlDeleteElementGenericTableAvl](../../text/3E/RtlDeleteElementGenericTableAvl_function_003EE750.md) (`PAGE` → `.text`)
  - `0x0071C663` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0071C66F` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0071C1C8  48 8B C4                        mov rax, rsp
0071C1CB  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0071C1CF  48 89 48 08                     mov qword ptr [rax + 8], rcx
0071C1D3  56                              push rsi
0071C1D4  57                              push rdi
0071C1D5  41 54                           push r12
0071C1D7  41 55                           push r13
0071C1D9  41 56                           push r14
0071C1DB  41 57                           push r15
0071C1DD  48 81 EC A8 00 00 00            sub rsp, 0xa8
0071C1E4  48 83 60 80 00                  and qword ptr [rax - 0x80], 0
0071C1E9  C6 84 24 F0 00 00 00 00         mov byte ptr [rsp + 0xf0], 0
0071C1F1  C6 40 20 00                     mov byte ptr [rax + 0x20], 0
0071C1F5  33 FF                           xor edi, edi
0071C1F7  48 21 78 C0                     and qword ptr [rax - 0x40], rdi
0071C1FB  45 33 F6                        xor r14d, r14d
0071C1FE  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
0071C203  48 21 7C 24 38                  and qword ptr [rsp + 0x38], rdi
0071C208  33 C0                           xor eax, eax
0071C20A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0071C20F  45 33 FF                        xor r15d, r15d
0071C212  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0071C21B  48 8B B0 B8 00 00 00            mov rsi, qword ptr [rax + 0xb8]
0071C222  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
0071C227  48 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], rsi
0071C22F  4C 8B 62 18                     mov r12, qword ptr [rdx + 0x18]
0071C233  45 8B 6C 24 08                  mov r13d, dword ptr [r12 + 8]
0071C238  45 85 ED                        test r13d, r13d
0071C23B  75 0A                           jne 0x14071c247
0071C23D  B8 0D 00 00 C0                  mov eax, 0xc000000d
0071C242  E9 30 04 00 00                  jmp 0x14071c677
0071C247  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
0071C24C  4D 8B 24 24                     mov r12, qword ptr [r12]
0071C250  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
0071C255  48 8D 0D 24 16 87 00            lea rcx, [rip + 0x871624]
0071C25C  E8 3F 23 AF FF                  call 0x14020e5a0
0071C261  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
0071C269  4C 8D 8C 24 F8 00 00 00         lea r9, [rsp + 0xf8]
0071C271  41 B8 10 00 00 00               mov r8d, 0x10
0071C277  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
0071C27F  48 8D 0D 7A 15 87 00            lea rcx, [rip + 0x87157a]
0071C286  E8 85 22 CD FF                  call 0x1403ee510
0071C28B  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0071C290  48 85 C0                        test rax, rax
0071C293  75 0E                           jne 0x14071c2a3
0071C295  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
0071C29B  44 8A E7                        mov r12b, dil
0071C29E  E9 46 03 00 00                  jmp 0x14071c5e9
0071C2A3  40 38 BC 24 F8 00 00 00         cmp byte ptr [rsp + 0xf8], dil
0071C2AB  75 1F                           jne 0x14071c2cc
0071C2AD  48 8B 78 08                     mov rdi, qword ptr [rax + 8]
0071C2B1  EB 14                           jmp 0x14071c2c7
0071C2B3  4C 39 67 08                     cmp qword ptr [rdi + 8], r12
0071C2B7  75 0A                           jne 0x14071c2c3
0071C2B9  4B 8D 04 2C                     lea rax, [r12 + r13]
0071C2BD  48 39 47 10                     cmp qword ptr [rdi + 0x10], rax
0071C2C1  74 09                           je 0x14071c2cc
0071C2C3  48 8B 7F 28                     mov rdi, qword ptr [rdi + 0x28]
0071C2C7  48 85 FF                        test rdi, rdi
0071C2CA  75 E7                           jne 0x14071c2b3
0071C2CC  48 85 FF                        test rdi, rdi
0071C2CF  0F 85 96 01 00 00               jne 0x14071c46b
0071C2D5  8D 57 30                        lea edx, [rdi + 0x30]
0071C2D8  B9 00 01 00 00                  mov ecx, 0x100
0071C2DD  41 B8 49 6F 54 65               mov r8d, 0x65546f49
0071C2E3  E8 08 5E 46 00                  call 0x140b820f0
0071C2E8  48 8B F8                        mov rdi, rax
0071C2EB  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0071C2F0  48 85 C0                        test rax, rax
0071C2F3  75 0E                           jne 0x14071c303
0071C2F5  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
0071C2FB  45 8A E6                        mov r12b, r14b
0071C2FE  E9 E6 02 00 00                  jmp 0x14071c5e9
0071C303  B0 01                           mov al, 1
0071C305  88 84 24 F0 00 00 00            mov byte ptr [rsp + 0xf0], al
0071C30C  88 44 24 31                     mov byte ptr [rsp + 0x31], al
0071C310  48 83 BE 10 03 00 00 00         cmp qword ptr [rsi + 0x310], 0
0071C318  74 34                           je 0x14071c34e
0071C31A  0F B7 86 EC 06 00 00            movzx eax, word ptr [rsi + 0x6ec]
0071C321  B9 4C 01 00 00                  mov ecx, 0x14c
0071C326  66 3B C1                        cmp ax, cx
0071C329  74 0E                           je 0x14071c339
0071C32B  B9 C4 01 00 00                  mov ecx, 0x1c4
0071C330  66 3B C1                        cmp ax, cx
0071C333  74 04                           je 0x14071c339
0071C335  32 C0                           xor al, al
0071C337  EB 02                           jmp 0x14071c33b
0071C339  B0 01                           mov al, 1
0071C33B  88 44 24 30                     mov byte ptr [rsp + 0x30], al
0071C33F  84 C0                           test al, al
0071C341  74 0B                           je 0x14071c34e
0071C343  41 F6 C4 03                     test r12b, 3
0071C347  74 10                           je 0x14071c359
0071C349  E8 82 DC 17 00                  call 0x140899fd0
0071C34E  41 F6 C4 07                     test r12b, 7
0071C352  74 05                           je 0x14071c359
0071C354  E8 77 DC 17 00                  call 0x140899fd0
0071C359  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
0071C363  4B 8D 0C 2C                     lea rcx, [r12 + r13]
0071C367  48 3B C8                        cmp rcx, rax
0071C36A  77 05                           ja 0x14071c371
0071C36C  49 3B CC                        cmp rcx, r12
0071C36F  73 02                           jae 0x14071c373
0071C371  8A 00                           mov al, byte ptr [rax]
0071C373  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0071C379  41 B1 01                        mov r9b, 1
0071C37C  45 33 C0                        xor r8d, r8d
0071C37F  41 8B D5                        mov edx, r13d
0071C382  49 8B CC                        mov rcx, r12
0071C385  E8 66 28 B8 FF                  call 0x14029ebf0
0071C38A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0071C38F  48 85 C0                        test rax, rax
0071C392  75 0A                           jne 0x14071c39e
0071C394  B9 9A 00 00 C0                  mov ecx, 0xc000009a
0071C399  E8 B2 A6 BD FF                  call 0x1402f6a50
0071C39E  41 B8 01 00 00 00               mov r8d, 1
0071C3A4  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
0071C3AC  8A 52 40                        mov dl, byte ptr [rdx + 0x40]
0071C3AF  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0071C3B4  E8 D7 F5 B1 FF                  call 0x14023b990
0071C3B9  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0071C3BE  EB 34                           jmp 0x14071c3f4
0071C3C0  44 8B F8                        mov r15d, eax
0071C3C3  8A 44 24 31                     mov al, byte ptr [rsp + 0x31]
0071C3C7  88 84 24 F0 00 00 00            mov byte ptr [rsp + 0xf0], al
0071C3CE  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0071C3D3  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
0071C3D8  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
0071C3DD  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
0071C3E2  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0071C3E7  48 8B B4 24 88 00 00 00         mov rsi, qword ptr [rsp + 0x88]
0071C3EF  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
0071C3F4  45 85 FF                        test r15d, r15d
0071C3F7  0F 88 DF 01 00 00               js 0x14071c5dc
0071C3FD  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0071C402  F6 46 0A 05                     test byte ptr [rsi + 0xa], 5
0071C406  74 06                           je 0x14071c40e
0071C408  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0071C40C  EB 20                           jmp 0x14071c42e
0071C40E  C7 44 24 28 10 00 00 40         mov dword ptr [rsp + 0x28], 0x40000010
0071C416  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
0071C41B  45 33 C9                        xor r9d, r9d
0071C41E  33 D2                           xor edx, edx
0071C420  45 8D 41 01                     lea r8d, [r9 + 1]
0071C424  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0071C429  E8 D2 C3 BF FF                  call 0x140318800
0071C42E  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0071C433  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0071C438  48 85 C0                        test rax, rax
0071C43B  74 28                           je 0x14071c465
0071C43D  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0071C442  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
0071C446  4C 89 67 08                     mov qword ptr [rdi + 8], r12
0071C44A  41 8B CD                        mov ecx, r13d
0071C44D  49 03 CC                        add rcx, r12
0071C450  48 89 4F 10                     mov qword ptr [rdi + 0x10], rcx
0071C454  C7 07 01 00 00 00               mov dword ptr [rdi], 1
0071C45A  48 83 67 28 00                  and qword ptr [rdi + 0x28], 0
0071C45F  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
0071C463  EB 06                           jmp 0x14071c46b
0071C465  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
0071C46B  45 85 FF                        test r15d, r15d
0071C46E  0F 88 68 01 00 00               js 0x14071c5dc
0071C474  BA 30 00 00 00                  mov edx, 0x30
0071C479  8D 4A 10                        lea ecx, [rdx + 0x10]
0071C47C  41 B8 49 6F 54 65               mov r8d, 0x65546f49
0071C482  E8 69 5C 46 00                  call 0x140b820f0
0071C487  4C 8B F0                        mov r14, rax
0071C48A  48 85 C0                        test rax, rax
0071C48D  75 13                           jne 0x14071c4a2
0071C48F  41 BF 9A 00 00 C0               mov r15d, 0xc000009a
0071C495  44 8A A4 24 F0 00 00 00         mov r12b, byte ptr [rsp + 0xf0]
0071C49D  E9 47 01 00 00                  jmp 0x14071c5e9
0071C4A2  4C 89 20                        mov qword ptr [rax], r12
0071C4A5  41 8B C5                        mov eax, r13d
0071C4A8  49 03 C4                        add rax, r12
0071C4AB  49 89 46 08                     mov qword ptr [r14 + 8], rax
0071C4AF  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
0071C4B3  48 2B 4F 08                     sub rcx, qword ptr [rdi + 8]
0071C4B7  49 03 CC                        add rcx, r12
0071C4BA  49 89 4E 18                     mov qword ptr [r14 + 0x18], rcx
0071C4BE  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0071C4C2  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
0071C4C6  49 83 66 28 00                  and qword ptr [r14 + 0x28], 0
0071C4CB  BA 49 6F 43 70                  mov edx, 0x70436f49
0071C4D0  48 8B CE                        mov rcx, rsi
0071C4D3  E8 38 42 AF FF                  call 0x140210710
0071C4D8  49 89 76 20                     mov qword ptr [r14 + 0x20], rsi
0071C4DC  45 33 C0                        xor r8d, r8d
0071C4DF  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
0071C4E4  4C 8B AC 24 E0 00 00 00         mov r13, qword ptr [rsp + 0xe0]
0071C4EC  49 8B CD                        mov rcx, r13
0071C4EF  E8 BC CA CF FF                  call 0x140418fb0
0071C4F4  44 8B F8                        mov r15d, eax
0071C4F7  85 C0                           test eax, eax
0071C4F9  0F 88 DD 00 00 00               js 0x14071c5dc
0071C4FF  4D 8B C6                        mov r8, r14
0071C502  BA 02 00 00 00                  mov edx, 2
0071C507  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0071C50C  E8 3F 66 D3 FF                  call 0x140452b50
0071C511  44 8B F8                        mov r15d, eax
0071C514  3D 01 00 00 C0                  cmp eax, 0xc0000001
0071C519  0F 85 84 00 00 00               jne 0x14071c5a3
0071C51F  49 8B 8D D0 00 00 00            mov rcx, qword ptr [r13 + 0xd0]
0071C526  48 85 C9                        test rcx, rcx
0071C529  74 04                           je 0x14071c52f
0071C52B  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
0071C52F  49 39 76 20                     cmp qword ptr [r14 + 0x20], rsi
0071C533  75 6E                           jne 0x14071c5a3
0071C535  48 8B D1                        mov rdx, rcx
0071C538  48 85 D2                        test rdx, rdx
0071C53B  74 37                           je 0x14071c574
0071C53D  48 8B 02                        mov rax, qword ptr [rdx]
0071C540  49 39 06                        cmp qword ptr [r14], rax
0071C543  75 0A                           jne 0x14071c54f
0071C545  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0071C549  49 39 46 08                     cmp qword ptr [r14 + 8], rax
0071C54D  74 06                           je 0x14071c555
0071C54F  48 8B 52 28                     mov rdx, qword ptr [rdx + 0x28]
0071C553  EB E3                           jmp 0x14071c538
0071C555  BA 49 6F 43 70                  mov edx, 0x70436f49
0071C55A  48 8B CE                        mov rcx, rsi
0071C55D  E8 7E B3 BD FF                  call 0x1402f78e0
0071C562  33 D2                           xor edx, edx
0071C564  49 8B CE                        mov rcx, r14
0071C567  E8 04 63 46 00                  call 0x140b82870
0071C56C  45 33 FF                        xor r15d, r15d
0071C56F  E9 F4 00 00 00                  jmp 0x14071c668
0071C574  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
0071C578  49 89 46 28                     mov qword ptr [r14 + 0x28], rax
0071C57C  F0 4C 0F B1 71 28               lock cmpxchg qword ptr [rcx + 0x28], r14
0071C582  49 3B 46 28                     cmp rax, qword ptr [r14 + 0x28]
0071C586  74 18                           je 0x14071c5a0
0071C588  0F 0D 49 28                     prefetchw byte ptr [rcx + 0x28]
0071C58C  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
0071C590  49 89 46 28                     mov qword ptr [r14 + 0x28], rax
0071C594  F0 4C 0F B1 71 28               lock cmpxchg qword ptr [rcx + 0x28], r14
0071C59A  49 3B 46 28                     cmp rax, qword ptr [r14 + 0x28]
0071C59E  75 EC                           jne 0x14071c58c
0071C5A0  45 33 FF                        xor r15d, r15d
0071C5A3  44 8A A4 24 F0 00 00 00         mov r12b, byte ptr [rsp + 0xf0]
0071C5AB  45 85 FF                        test r15d, r15d
0071C5AE  78 39                           js 0x14071c5e9
0071C5B0  41 80 FC 01                     cmp r12b, 1
0071C5B4  75 22                           jne 0x14071c5d8
0071C5B6  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0071C5BB  44 38 A4 24 F8 00 00 00         cmp byte ptr [rsp + 0xf8], r12b
0071C5C3  75 05                           jne 0x14071c5ca
0071C5C5  48 89 31                        mov qword ptr [rcx], rsi
0071C5C8  EB 08                           jmp 0x14071c5d2
0071C5CA  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0071C5CE  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
0071C5D2  48 89 79 08                     mov qword ptr [rcx + 8], rdi
0071C5D6  EB 0C                           jmp 0x14071c5e4
0071C5D8  FF 07                           inc dword ptr [rdi]
0071C5DA  EB 08                           jmp 0x14071c5e4
0071C5DC  44 8A A4 24 F0 00 00 00         mov r12b, byte ptr [rsp + 0xf0]
0071C5E4  45 85 FF                        test r15d, r15d
0071C5E7  79 7F                           jns 0x14071c668
0071C5E9  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0071C5EE  48 85 F6                        test rsi, rsi
0071C5F1  74 29                           je 0x14071c61c
0071C5F3  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0071C5F8  48 85 C0                        test rax, rax
0071C5FB  74 0B                           je 0x14071c608
0071C5FD  48 8B D6                        mov rdx, rsi
0071C600  48 8B C8                        mov rcx, rax
0071C603  E8 58 A8 B2 FF                  call 0x140246e60
0071C608  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0071C60D  E8 CE 28 B8 FF                  call 0x14029eee0
0071C612  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0071C617  E8 64 24 B8 FF                  call 0x14029ea80
0071C61C  4D 85 F6                        test r14, r14
0071C61F  74 19                           je 0x14071c63a
0071C621  BA 49 6F 43 70                  mov edx, 0x70436f49
0071C626  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0071C62B  E8 B0 B2 BD FF                  call 0x1402f78e0
0071C630  33 D2                           xor edx, edx
0071C632  49 8B CE                        mov rcx, r14
0071C635  E8 36 62 46 00                  call 0x140b82870
0071C63A  80 BC 24 F8 00 00 00 01         cmp byte ptr [rsp + 0xf8], 1
0071C642  75 14                           jne 0x14071c658
0071C644  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
0071C64C  48 8D 0D AD 11 87 00            lea rcx, [rip + 0x8711ad]
0071C653  E8 F8 20 CD FF                  call 0x1403ee750
0071C658  41 80 FC 01                     cmp r12b, 1
0071C65C  75 0A                           jne 0x14071c668
0071C65E  33 D2                           xor edx, edx
0071C660  48 8B CF                        mov rcx, rdi
0071C663  E8 08 62 46 00                  call 0x140b82870
0071C668  48 8D 0D 11 12 87 00            lea rcx, [rip + 0x871211]
0071C66F  E8 4C 53 B3 FF                  call 0x1402519c0
0071C674  41 8B C7                        mov eax, r15d
0071C677  48 81 C4 A8 00 00 00            add rsp, 0xa8
0071C67E  41 5F                           pop r15
0071C680  41 5E                           pop r14
0071C682  41 5D                           pop r13
0071C684  41 5C                           pop r12
0071C686  5F                              pop rdi
0071C687  5E                              pop rsi
0071C688  C3                              ret
0071C689  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopSetFileObjectIosbRange(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int8 v_stack_mA7;
    unsigned __int8 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (168);
    v_stack_p18 = 0;
    *(unsigned __int8 *)(v_rsp + 32) = 0;
    v_rdi = 0;
    v_r14 = 0;
    v_stack_m68 = 0;
    result = 0;
    v_stack_m90 = 0;
    v_r15 = 0;
    v_stack_m98 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 8))) != 0) goto loc_0071C247;
    goto loc_0071C677;
loc_0071C247:
    v_stack_m88 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 8)));
    v_stack_m60 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 24));
    result = ExAcquireFastMutex(v_rip + 8853028, a2, a3, a4);
    v_stack_m48 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    result = RtlInsertElementGenericTableAvl(v_rip + 8852858, v_stack_m48, 16, v_stack_p20);
    v_stack_m78 = result;
    if (result != 0) goto loc_0071C2A3;
    goto loc_0071C5E9;
loc_0071C2A3:
    if (v_stack_p20 != 0) goto loc_0071C2CC;
    goto loc_0071C2C7;
loc_0071C2B3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8)) != 0) goto loc_0071C2C3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 16)) == (0 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 8)) * 1)) goto loc_0071C2CC;
loc_0071C2C3:
loc_0071C2C7:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 40) != 0) goto loc_0071C2B3;
loc_0071C2CC:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 40) != 0) goto loc_0071C46B;
    result = ExAllocatePool2(256, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 40) + 48, (unsigned int)(0x65546F49ULL), v_stack_p20);
    v_stack_m70 = result;
    if (result != 0) goto loc_0071C303;
    goto loc_0071C5E9;
loc_0071C303:
    v_stack_p18 = 1;
    v_stack_mA7 = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) == 0) goto loc_0071C34E;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 332) goto loc_0071C339;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 452) goto loc_0071C339;
    result = 0;
    goto loc_0071C33B;
loc_0071C339:
loc_0071C33B:
    v_stack_mA8 = 1;
    if (1 == 0) goto loc_0071C34E;
    if (((0) & (3)) == 0) goto loc_0071C359;
    result = ExRaiseDatatypeMisalignment(452, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 40) + 48, (unsigned int)(0x65546F49ULL), v_stack_p20);
loc_0071C34E:
    if (((0) & (7)) != 0) {
        result = ExRaiseDatatypeMisalignment(452, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 40) + 48, (unsigned int)(0x65546F49ULL), v_stack_p20);
    }
    if ((0 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 8)) * 1) > result) goto loc_0071C371;
    if ((0 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 8)) * 1) < 0) {
        result = *(unsigned __int8 *)(result);
    }
    a3 = 0;
    result = IoAllocateMdl(0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 8)))), a3, 1);
    v_stack_mA0 = result;
    if (result == 0) {
        a1 = 0xC000009AULL;
        result = RtlRaiseStatus(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 8)))), a3, 1);
    }
    result = MmProbeAndLockPages(v_stack_mA0, *(unsigned __int8 *)(v_stack_p10 + 64), 1, 1);
    goto loc_0071C3F4;
loc_0071C3F4:
    if (sign_flag) goto loc_0071C5DC;
    if (((*(unsigned __int8 *)(v_stack_mA0 + 10)) & (5)) == 0) goto loc_0071C40E;
    goto loc_0071C42E;
loc_0071C40E:
    v_stack_mB0 = 0x40000010ULL;
    a4 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(v_stack_mA0, a2, a4 + 1, a4);
loc_0071C42E:
    v_stack_m90 = result;
    if (result == 0) goto loc_0071C465;
    *(unsigned __int64 *)(result + 24) = v_stack_mA0;
    *(unsigned __int64 *)(result + 8) = 0;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 8))))) + (0);
    *(unsigned __int64 *)(result + 16) = a1;
    *(unsigned int *)(result) = 1;
    *(unsigned __int64 *)(result + 32) = result;
    goto loc_0071C46B;
loc_0071C465:
loc_0071C46B:
    if (sign_flag) goto loc_0071C5DC;
    result = ExAllocatePool2(48 + 16, 48, (unsigned int)(0x65546F49ULL), a4);
    if (result != 0) goto loc_0071C4A2;
    goto loc_0071C5E9;
loc_0071C4A2:
    *(unsigned __int64 *)(result) = v_stack_p18;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 24) + 8))))) + (v_stack_p18);
    *(unsigned __int64 *)(result + 8) = result;
    a1 = (*(unsigned __int64 *)(result + 32)) - (*(unsigned __int64 *)(result + 8));
    a1 = (a1) + (v_stack_p18);
    *(unsigned __int64 *)(result + 24) = a1;
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(result + 24);
    result = ObfReferenceObjectWithTag(v_stack_m98, (unsigned int)(0x70436F49ULL), (unsigned int)(0x65546F49ULL), a4);
    *(unsigned __int64 *)(result + 32) = v_stack_m98;
    a3 = 0;
    result = IopAllocateFileObjectExtension(v_stack_p8, v_stack_m80, a3, a4);
    if (sign_flag) goto loc_0071C5DC;
    result = IopSetTypeSpecificFoExtension(v_stack_m80, 2, result, a4);
    if (((unsigned int)(result)) != 0xC0000001ULL) goto loc_0071C5A3;
    if (*(unsigned __int64 *)(v_stack_p8 + 208) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 208) + 24);
    }
    if ((*(unsigned __int64 *)(result + 32)) != v_stack_m98) goto loc_0071C5A3;
loc_0071C538:
    if (a1 == 0) goto loc_0071C574;
    if ((*(unsigned __int64 *)(result)) != (*(unsigned __int64 *)(a1))) goto loc_0071C54F;
    if ((*(unsigned __int64 *)(result + 8)) == (*(unsigned __int64 *)(a1 + 8))) goto loc_0071C555;
loc_0071C54F:
    goto loc_0071C538;
loc_0071C555:
    result = ObfDereferenceObjectWithTag(v_stack_m98, (unsigned int)(0x70436F49ULL), result, a4);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, result, a4);
    v_r15 = 0;
    goto loc_0071C668;
loc_0071C574:
    *(unsigned __int64 *)(result + 40) = *(unsigned __int64 *)(result + 40);
    if ((*(unsigned __int64 *)(result + 40)) == (*(unsigned __int64 *)(result + 40))) goto loc_0071C5A0;
loc_0071C58C:
    *(unsigned __int64 *)(result + 40) = *(unsigned __int64 *)(result + 40);
    if ((*(unsigned __int64 *)(result + 40)) != (*(unsigned __int64 *)(result + 40))) goto loc_0071C58C;
loc_0071C5A0:
    v_r15 = 0;
loc_0071C5A3:
    if (sign_flag) goto loc_0071C5E9;
    if (((unsigned __int8)(v_stack_p18)) != 1) goto loc_0071C5D8;
    if (v_stack_p20 != ((unsigned __int8)(v_stack_p18))) goto loc_0071C5CA;
    *(unsigned __int64 *)(v_stack_m78) = v_stack_m98;
    goto loc_0071C5D2;
loc_0071C5CA:
    *(unsigned __int64 *)(result + 40) = *(unsigned __int64 *)(v_stack_m78 + 8);
loc_0071C5D2:
    *(unsigned __int64 *)(v_stack_m78 + 8) = result;
    goto loc_0071C5E4;
loc_0071C5D8:
    goto loc_0071C5E4;
loc_0071C5DC:
loc_0071C5E4:
    if (!sign_flag) goto loc_0071C668;
loc_0071C5E9:
    if (v_stack_mA0 == 0) goto loc_0071C61C;
    result = v_stack_m90;
    if (v_stack_m90 != 0) {
        a2 = v_stack_mA0;
        a1 = v_stack_m90;
        result = MmUnmapLockedPages(a1, a2, result, a4);
    }
    result = MmUnlockPages(v_stack_mA0, a2, result, a4);
    result = IoFreeMdl(v_stack_mA0, a2, result, a4);
loc_0071C61C:
    if (result != 0) {
        a2 = 0x70436F49ULL;
        a1 = v_stack_m98;
        result = ObfDereferenceObjectWithTag(a1, a2, result, a4);
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, result, a4);
    }
    if (v_stack_p20 == 1) {
        a2 = v_stack_m48;
        a1 = v_rip + 8851885;
        result = RtlDeleteElementGenericTableAvl(a1, a2, result, a4);
    }
    if (((unsigned __int8)(v_stack_p18)) == 1) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, result, a4);
    }
    result = ExReleaseFastMutex(v_rip + 8851985, a2, result, a4);
loc_0071C677:
    v_rsp = (v_rsp) + (168);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t IopSetFileObjectIosbRange(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint8_t v_stack_mA7;
    uint8_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(void **)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (168);
    v_stack_p18 = 0;
    *(uint8_t *)(local_rsp + 0x20) = 0;
    local_rdi = 0;
    local_r14 = 0;
    v_stack_m68 = 0;
    result = 0;
    v_stack_m90 = 0;
    local_r15 = 0;
    v_stack_m98 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x8))) != 0) goto loc_0071C247;
    goto loc_0071C677;
loc_0071C247:
    v_stack_m88 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x8)));
    v_stack_m60 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x18));
    result = ExAcquireFastMutex(v_rip + 8853028, Arg2, a3, a4);
    v_stack_m48 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    result = RtlInsertElementGenericTableAvl(v_rip + 8852858, v_stack_m48, 16, v_stack_p20);
    v_stack_m78 = result;
    if (result != 0) goto loc_0071C2A3;
    goto loc_0071C5E9;
loc_0071C2A3:
    if (v_stack_p20 != 0) goto loc_0071C2CC;
    goto loc_0071C2C7;
loc_0071C2B3:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8)) != 0) goto loc_0071C2C3;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x10)) == (0 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x8)) * 1)) goto loc_0071C2CC;
loc_0071C2C3:
loc_0071C2C7:
    if (*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x28) != 0) goto loc_0071C2B3;
loc_0071C2CC:
    if (*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x28) != 0) goto loc_0071C46B;
    result = ExAllocatePool2(256, *(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x28) + 48, (uint32_t)(0x65546F49ULL), v_stack_p20);
    v_stack_m70 = result;
    if (result != 0) goto loc_0071C303;
    goto loc_0071C5E9;
loc_0071C303:
    v_stack_p18 = 1;
    v_stack_mA7 = 1;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) == 0) goto loc_0071C34E;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 332) goto loc_0071C339;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 452) goto loc_0071C339;
    result = 0;
    goto loc_0071C33B;
loc_0071C339:
loc_0071C33B:
    v_stack_mA8 = 1;
    if (1 == 0) goto loc_0071C34E;
    if (((0) & (3)) == 0) goto loc_0071C359;
    result = ExRaiseDatatypeMisalignment(452, *(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x28) + 48, (uint32_t)(0x65546F49ULL), v_stack_p20);
loc_0071C34E:
    if (((0) & (7)) != 0) {
        result = ExRaiseDatatypeMisalignment(452, *(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x28) + 48, (uint32_t)(0x65546F49ULL), v_stack_p20);
    }
    if ((0 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x8)) * 1) > result) goto loc_0071C371;
    if ((0 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x8)) * 1) < 0) {
        result = *(uint8_t *)(result);
    }
    a3 = 0;
    result = IoAllocateMdl(0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x8)))), a3, 1);
    v_stack_mA0 = result;
    if (result == 0) {
        Arg1 = 0xC000009AULL;
        result = RtlRaiseStatus(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x8)))), a3, 1);
    }
    result = MmProbeAndLockPages(v_stack_mA0, *(uint8_t *)(v_stack_p10 + 0x40), 1, 1);
    goto loc_0071C3F4;
loc_0071C3F4:
    if (sign_flag) goto loc_0071C5DC;
    if (((*(uint8_t *)(v_stack_mA0 + 0xA)) & (5)) == 0) goto loc_0071C40E;
    goto loc_0071C42E;
loc_0071C40E:
    v_stack_mB0 = 0x40000010ULL;
    a4 = 0;
    Arg2 = 0;
    result = MmMapLockedPagesSpecifyCache(v_stack_mA0, Arg2, a4 + 1, a4);
loc_0071C42E:
    v_stack_m90 = result;
    if (result == 0) goto loc_0071C465;
    *(uint64_t *)(result + 0x18) = v_stack_mA0;
    *(uint64_t *)(result + 0x8) = 0;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x8))))) + (0);
    *(uint64_t *)(result + 0x10) = Arg1;
    *(uint32_t *)(result) = 1;
    *(uint64_t *)(result + 0x20) = result;
    goto loc_0071C46B;
loc_0071C465:
loc_0071C46B:
    if (sign_flag) goto loc_0071C5DC;
    result = ExAllocatePool2(48 + 16, 48, (uint32_t)(0x65546F49ULL), a4);
    if (result != 0) goto loc_0071C4A2;
    goto loc_0071C5E9;
loc_0071C4A2:
    *(uint64_t *)(result) = v_stack_p18;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x18) + 0x8))))) + (v_stack_p18);
    *(uint64_t *)(result + 0x8) = result;
    Arg1 = (*(uint64_t *)(result + 0x20)) - (*(uint64_t *)(result + 0x8));
    Arg1 = (Arg1) + (v_stack_p18);
    *(uint64_t *)(result + 0x18) = Arg1;
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(result + 0x18);
    result = ObfReferenceObjectWithTag(v_stack_m98, (uint32_t)(0x70436F49ULL), (uint32_t)(0x65546F49ULL), a4);
    *(uint64_t *)(result + 0x20) = v_stack_m98;
    a3 = 0;
    result = IopAllocateFileObjectExtension(v_stack_p8, v_stack_m80, a3, a4);
    if (sign_flag) goto loc_0071C5DC;
    result = IopSetTypeSpecificFoExtension(v_stack_m80, 2, result, a4);
    if (((uint32_t)(result)) != 0xC0000001ULL) goto loc_0071C5A3;
    if (*(uint64_t *)(v_stack_p8 + 0xD0) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0xD0) + 0x18);
    }
    if ((*(uint64_t *)(result + 0x20)) != v_stack_m98) goto loc_0071C5A3;
loc_0071C538:
    if (Arg1 == 0) goto loc_0071C574;
    if ((*(uint64_t *)(result)) != (*(uint64_t *)(Arg1))) goto loc_0071C54F;
    if ((*(uint64_t *)(result + 0x8)) == (*(uint64_t *)(Arg1 + 0x8))) goto loc_0071C555;
loc_0071C54F:
    goto loc_0071C538;
loc_0071C555:
    result = ObfDereferenceObjectWithTag(v_stack_m98, (uint32_t)(0x70436F49ULL), result, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, result, a4);
    local_r15 = 0;
    goto loc_0071C668;
loc_0071C574:
    *(uint64_t *)(result + 0x28) = *(uint64_t *)(result + 0x28);
    if ((*(uint64_t *)(result + 0x28)) == (*(uint64_t *)(result + 0x28))) goto loc_0071C5A0;
loc_0071C58C:
    *(uint64_t *)(result + 0x28) = *(uint64_t *)(result + 0x28);
    if ((*(uint64_t *)(result + 0x28)) != (*(uint64_t *)(result + 0x28))) goto loc_0071C58C;
loc_0071C5A0:
    local_r15 = 0;
loc_0071C5A3:
    if (sign_flag) goto loc_0071C5E9;
    if (((uint8_t)(v_stack_p18)) != 1) goto loc_0071C5D8;
    if (v_stack_p20 != ((uint8_t)(v_stack_p18))) goto loc_0071C5CA;
    *(uint64_t *)(v_stack_m78) = v_stack_m98;
    goto loc_0071C5D2;
loc_0071C5CA:
    *(uint64_t *)(result + 0x28) = *(uint64_t *)(v_stack_m78 + 0x8);
loc_0071C5D2:
    *(uint64_t *)(v_stack_m78 + 0x8) = result;
    goto loc_0071C5E4;
loc_0071C5D8:
    goto loc_0071C5E4;
loc_0071C5DC:
loc_0071C5E4:
    if (!sign_flag) goto loc_0071C668;
loc_0071C5E9:
    if (v_stack_mA0 == 0) goto loc_0071C61C;
    result = v_stack_m90;
    if (v_stack_m90 != 0) {
        Arg2 = v_stack_mA0;
        Arg1 = v_stack_m90;
        result = MmUnmapLockedPages(Arg1, Arg2, result, a4);
    }
    result = MmUnlockPages(v_stack_mA0, Arg2, result, a4);
    result = IoFreeMdl(v_stack_mA0, Arg2, result, a4);
loc_0071C61C:
    if (result != 0) {
        Arg2 = 0x70436F49ULL;
        Arg1 = v_stack_m98;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, result, a4);
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, result, a4);
    }
    if (v_stack_p20 == 1) {
        Arg2 = v_stack_m48;
        Arg1 = v_rip + 8851885;
        result = RtlDeleteElementGenericTableAvl(Arg1, Arg2, result, a4);
    }
    if (((uint8_t)(v_stack_p18)) == 1) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, result, a4);
    }
    result = ExReleaseFastMutex(v_rip + 8851985, Arg2, result, a4);
loc_0071C677:
    local_rsp = (local_rsp) + (168);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0071C1C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
