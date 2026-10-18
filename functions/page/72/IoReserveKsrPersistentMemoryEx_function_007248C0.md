# IoReserveKsrPersistentMemoryEx

- RVA: `0x007248C0`–`0x00724DEC` (길이 `1,324` bytes)
- VA: `0x00000001407248C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C8220`
- 디코드: `352`개 명령, `1,324/1,324` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00724935` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0072496B` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00724982` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00724996` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007249A7` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007249C9` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007249D9` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007249E6` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00724A01` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00724A19` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00724A3D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00724A59` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00724A71` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00724ABA` → [PipGetDriverKsrGuid](PipGetDriverKsrGuid_function_00725100.md) (function, `0x00725100`)
- `0x00724B07` → [PipGetDeviceObjectLocation](PipGetDeviceObjectLocation_function_00724EA4.md) (function, `0x00724EA4`)
- `0x00724B53` → [PipGetPersistentMemory](PipGetPersistentMemory_function_00725290.md) (function, `0x00725290`)
- `0x00724B97` → [MmAllocatePagesForMdlEx](../../text/3E/MmAllocatePagesForMdlEx_function_003EA8C0.md) (function, `0x003EA8C0`)
- `0x00724BBD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00724BD3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00724BEC` → [MmUnmapLockedPages](../../text/24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)
- `0x00724BF4` → [MmFreePagesFromMdl](../../text/3F/MmFreePagesFromMdl_function_003F82E0.md) (function, `0x003F82E0`)
- `0x00724BFF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00724C0F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00724C1F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00724C2D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00724C5F` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x00724C7A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00724C99` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00724CE0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00724D18` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00724D2E` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrMdlToMemoryRuns` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrMdlToMemoryRuns`)
- `0x00724D4C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00724D71` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrMdlToMemoryRuns` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrMdlToMemoryRuns`)
- `0x00724DA5` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrPersistMemoryWithMetadata` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrPersistMemoryWithMetadata`)

### Direct callers
- [IoReserveKsrPersistentMemory](IoReserveKsrPersistentMemory_function_00724880.md) at `0x007248A3`

### Static image references
- `0x007248D9` → RVA `0x00E0A740` (`.data`; read)
- `0x00724A77` → RVA `0x00F8A988` (`.data`; read)
- `0x00724D2E` → RVA `0x001512E8` (`ext-ms-win-ntos-ksr-l1-1-5.dll!KsrMdlToMemoryRuns (IAT)`; read)
- `0x00724DA5` → RVA `0x00151310` (`ext-ms-win-ntos-ksr-l1-1-5.dll!KsrPersistMemoryWithMetadata (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **28**
  - `0x00724935` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0072496B` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00724982` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00724996` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007249A7` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007249C9` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007249D9` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007249E6` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00724A01` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00724A19` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00724A3D` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00724A59` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00724A71` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00724B97` → [MmAllocatePagesForMdlEx](../../text/3E/MmAllocatePagesForMdlEx_function_003EA8C0.md) (`PAGE` → `.text`)
  - `0x00724BBD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00724BD3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00724BEC` → [MmUnmapLockedPages](../../text/24/MmUnmapLockedPages_function_00246E60.md) (`PAGE` → `.text`)
  - `0x00724BF4` → [MmFreePagesFromMdl](../../text/3F/MmFreePagesFromMdl_function_003F82E0.md) (`PAGE` → `.text`)
  - `0x00724BFF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00724C0F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00724C1F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00724C2D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00724C5F` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (`PAGE` → `.text`)
  - `0x00724C7A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00724C99` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00724CE0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00724D18` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00724D4C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007248C0  40 55                           push rbp
007248C2  53                              push rbx
007248C3  56                              push rsi
007248C4  57                              push rdi
007248C5  41 54                           push r12
007248C7  41 55                           push r13
007248C9  41 56                           push r14
007248CB  41 57                           push r15
007248CD  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
007248D2  48 81 EC C8 00 00 00            sub rsp, 0xc8
007248D9  48 8B 05 60 5E 6E 00            mov rax, qword ptr [rip + 0x6e5e60]
007248E0  48 33 C4                        xor rax, rsp
007248E3  48 89 45 F7                     mov qword ptr [rbp - 9], rax
007248E7  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
007248EE  33 DB                           xor ebx, ebx
007248F0  0F 57 C0                        xorps xmm0, xmm0
007248F3  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
007248F7  48 89 5D CF                     mov qword ptr [rbp - 0x31], rbx
007248FB  48 8B F2                        mov rsi, rdx
007248FE  48 89 5D D7                     mov qword ptr [rbp - 0x29], rbx
00724902  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
00724906  89 5D 8F                        mov dword ptr [rbp - 0x71], ebx
00724909  4C 89 4D C7                     mov qword ptr [rbp - 0x39], r9
0072490D  4C 89 45 BF                     mov qword ptr [rbp - 0x41], r8
00724911  48 89 4D B7                     mov qword ptr [rbp - 0x49], rcx
00724915  44 0F 20 C0                     mov rax, cr8
00724919  84 C0                           test al, al
0072491B  74 1E                           je 0x14072493b
0072491D  44 0F 20 C0                     mov rax, cr8
00724921  44 0F B6 C0                     movzx r8d, al
00724925  8D 53 01                        lea edx, [rbx + 1]
00724928  45 33 C9                        xor r9d, r9d
0072492B  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00724930  B9 21 01 00 00                  mov ecx, 0x121
00724935  E8 26 8D DD FF                  call 0x1404fd660
0072493A  CC                              int3
0072493B  48 85 F6                        test rsi, rsi
0072493E  0F 84 33 01 00 00               je 0x140724a77
00724944  48 8B 82 38 01 00 00            mov rax, qword ptr [rdx + 0x138]
0072494B  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
0072494F  48 85 C0                        test rax, rax
00724952  74 10                           je 0x140724964
00724954  F7 80 8C 01 00 00 00 00 02 00   test dword ptr [rax + 0x18c], 0x20000
0072495E  0F 84 13 01 00 00               je 0x140724a77
00724964  0F B7 52 02                     movzx edx, word ptr [rdx + 2]
00724968  48 8B CE                        mov rcx, rsi
0072496B  E8 04 3A D0 FF                  call 0x140428374
00724970  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00724974  BF 02 00 00 00                  mov edi, 2
00724979  48 85 C9                        test rcx, rcx
0072497C  74 2E                           je 0x1407249ac
0072497E  0F BF 51 02                     movsx edx, word ptr [rcx + 2]
00724982  E8 ED 39 D0 FF                  call 0x140428374
00724987  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0072498B  48 83 C1 38                     add rcx, 0x38
0072498F  66 39 19                        cmp word ptr [rcx], bx
00724992  74 18                           je 0x1407249ac
00724994  8B D7                           mov edx, edi
00724996  E8 D9 39 D0 FF                  call 0x140428374
0072499B  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0072499F  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
007249A3  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
007249A7  E8 C8 39 D0 FF                  call 0x140428374
007249AC  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
007249B3  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
007249B7  48 85 C9                        test rcx, rcx
007249BA  0F 84 9E 00 00 00               je 0x140724a5e
007249C0  BA 88 03 00 00                  mov edx, 0x388
007249C5  4C 8D 71 28                     lea r14, [rcx + 0x28]
007249C9  E8 A6 39 D0 FF                  call 0x140428374
007249CE  66 41 39 1E                     cmp word ptr [r14], bx
007249D2  74 17                           je 0x1407249eb
007249D4  8B D7                           mov edx, edi
007249D6  49 8B CE                        mov rcx, r14
007249D9  E8 96 39 D0 FF                  call 0x140428374
007249DE  41 0F B7 16                     movzx edx, word ptr [r14]
007249E2  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
007249E6  E8 89 39 D0 FF                  call 0x140428374
007249EB  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
007249F2  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
007249F6  48 83 C1 38                     add rcx, 0x38
007249FA  66 39 19                        cmp word ptr [rcx], bx
007249FD  74 1F                           je 0x140724a1e
007249FF  8B D7                           mov edx, edi
00724A01  E8 6E 39 D0 FF                  call 0x140428374
00724A06  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00724A0D  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00724A11  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00724A15  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00724A19  E8 56 39 D0 FF                  call 0x140428374
00724A1E  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00724A25  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00724A29  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00724A2D  48 85 C0                        test rax, rax
00724A30  74 2C                           je 0x140724a5e
00724A32  48 8D 48 38                     lea rcx, [rax + 0x38]
00724A36  66 39 19                        cmp word ptr [rcx], bx
00724A39  74 23                           je 0x140724a5e
00724A3B  8B D7                           mov edx, edi
00724A3D  E8 32 39 D0 FF                  call 0x140428374
00724A42  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00724A49  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00724A4D  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00724A51  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00724A55  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00724A59  E8 16 39 D0 FF                  call 0x140428374
00724A5E  45 33 C9                        xor r9d, r9d
00724A61  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00724A66  4C 8B C6                        mov r8, rsi
00724A69  48 8B D7                        mov rdx, rdi
00724A6C  B9 CA 00 00 00                  mov ecx, 0xca
00724A71  E8 EA 8B DD FF                  call 0x1404fd660
00724A76  CC                              int3
00724A77  38 1D 0B 5F 86 00               cmp byte ptr [rip + 0x865f0b], bl
00724A7D  4C 8B F3                        mov r14, rbx
00724A80  48 89 5D 9F                     mov qword ptr [rbp - 0x61], rbx
00724A84  4C 8B EB                        mov r13, rbx
00724A87  48 89 5D AF                     mov qword ptr [rbp - 0x51], rbx
00724A8B  4C 8B E3                        mov r12, rbx
00724A8E  89 5D 93                        mov dword ptr [rbp - 0x6d], ebx
00724A91  4C 8B FB                        mov r15, rbx
00724A94  48 89 5D A7                     mov qword ptr [rbp - 0x59], rbx
00724A98  89 5D 97                        mov dword ptr [rbp - 0x69], ebx
00724A9B  75 0A                           jne 0x140724aa7
00724A9D  BF BB 00 00 C0                  mov edi, 0xc00000bb
00724AA2  E9 7D 01 00 00                  jmp 0x140724c24
00724AA7  39 5D 7F                        cmp dword ptr [rbp + 0x7f], ebx
00724AAA  74 0A                           je 0x140724ab6
00724AAC  BF F2 00 00 C0                  mov edi, 0xc00000f2
00724AB1  E9 6E 01 00 00                  jmp 0x140724c24
00724AB6  48 8D 55 E7                     lea rdx, [rbp - 0x19]
00724ABA  E8 41 06 00 00                  call 0x140725100
00724ABF  8B F8                           mov edi, eax
00724AC1  85 C0                           test eax, eax
00724AC3  0F 88 5B 01 00 00               js 0x140724c24
00724AC9  48 85 F6                        test rsi, rsi
00724ACC  74 56                           je 0x140724b24
00724ACE  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
00724AD2  48 85 C0                        test rax, rax
00724AD5  74 25                           je 0x140724afc
00724AD7  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00724ADB  48 89 4D AF                     mov qword ptr [rbp - 0x51], rcx
00724ADF  48 85 C9                        test rcx, rcx
00724AE2  74 0E                           je 0x140724af2
00724AE4  0F B7 08                        movzx ecx, word ptr [rax]
00724AE7  66 85 C9                        test cx, cx
00724AEA  74 06                           je 0x140724af2
00724AEC  8B C1                           mov eax, ecx
00724AEE  D1 E8                           shr eax, 1
00724AF0  EB 2F                           jmp 0x140724b21
00724AF2  BF 0D 00 00 C0                  mov edi, 0xc000000d
00724AF7  E9 28 01 00 00                  jmp 0x140724c24
00724AFC  4C 8D 45 A7                     lea r8, [rbp - 0x59]
00724B00  48 8B CE                        mov rcx, rsi
00724B03  48 8D 55 97                     lea rdx, [rbp - 0x69]
00724B07  E8 98 03 00 00                  call 0x140724ea4
00724B0C  4C 8B 6D A7                     mov r13, qword ptr [rbp - 0x59]
00724B10  8B F8                           mov edi, eax
00724B12  85 C0                           test eax, eax
00724B14  0F 88 93 00 00 00               js 0x140724bad
00724B1A  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
00724B1D  4C 89 6D AF                     mov qword ptr [rbp - 0x51], r13
00724B21  89 45 93                        mov dword ptr [rbp - 0x6d], eax
00724B24  4C 8B 4D C7                     mov r9, qword ptr [rbp - 0x39]
00724B28  48 8D 45 D7                     lea rax, [rbp - 0x29]
00724B2C  4C 8B 45 BF                     mov r8, qword ptr [rbp - 0x41]
00724B30  48 8B D6                        mov rdx, rsi
00724B33  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00724B37  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
00724B3F  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00724B44  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00724B49  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00724B4E  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00724B53  E8 38 07 00 00                  call 0x140725290
00724B58  3D 34 00 00 C0                  cmp eax, 0xc0000034
00724B5D  8B FB                           mov edi, ebx
00724B5F  0F 45 F8                        cmovne edi, eax
00724B62  85 FF                           test edi, edi
00724B64  78 47                           js 0x140724bad
00724B66  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00724B6A  4C 8B C3                        mov r8, rbx
00724B6D  48 05 07 10 00 00               add rax, 0x1007
00724B73  C7 44 24 28 14 00 00 00         mov dword ptr [rsp + 0x28], 0x14
00724B7B  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
00724B81  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00724B89  4C 8B C8                        mov r9, rax
00724B8C  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
00724B90  48 83 CA FF                     or rdx, 0xffffffffffffffff
00724B94  48 8B CB                        mov rcx, rbx
00724B97  E8 24 5D CC FF                  call 0x1403ea8c0
00724B9C  4C 8B E0                        mov r12, rax
00724B9F  48 85 C0                        test rax, rax
00724BA2  0F 85 9F 00 00 00               jne 0x140724c47
00724BA8  BF 9A 00 00 C0                  mov edi, 0xc000009a
00724BAD  48 8B F3                        mov rsi, rbx
00724BB0  4D 85 ED                        test r13, r13
00724BB3  74 0D                           je 0x140724bc2
00724BB5  BA 50 6E 70 61                  mov edx, 0x61706e50
00724BBA  49 8B CD                        mov rcx, r13
00724BBD  E8 AE DC 45 00                  call 0x140b82870
00724BC2  41 BD 50 6E 70 61               mov r13d, 0x61706e50
00724BC8  48 85 F6                        test rsi, rsi
00724BCB  74 0B                           je 0x140724bd8
00724BCD  41 8B D5                        mov edx, r13d
00724BD0  48 8B CE                        mov rcx, rsi
00724BD3  E8 98 DC 45 00                  call 0x140b82870
00724BD8  4D 85 E4                        test r12, r12
00724BDB  74 27                           je 0x140724c04
00724BDD  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00724BE1  48 85 C0                        test rax, rax
00724BE4  74 0B                           je 0x140724bf1
00724BE6  49 8B D4                        mov rdx, r12
00724BE9  48 8B C8                        mov rcx, rax
00724BEC  E8 6F 22 B2 FF                  call 0x140246e60
00724BF1  49 8B CC                        mov rcx, r12
00724BF4  E8 E7 36 CD FF                  call 0x1403f82e0
00724BF9  41 8B D5                        mov edx, r13d
00724BFC  49 8B CC                        mov rcx, r12
00724BFF  E8 6C DC 45 00                  call 0x140b82870
00724C04  4D 85 FF                        test r15, r15
00724C07  74 0B                           je 0x140724c14
00724C09  41 8B D5                        mov edx, r13d
00724C0C  49 8B CF                        mov rcx, r15
00724C0F  E8 5C DC 45 00                  call 0x140b82870
00724C14  4D 85 F6                        test r14, r14
00724C17  74 0B                           je 0x140724c24
00724C19  41 8B D5                        mov edx, r13d
00724C1C  49 8B CE                        mov rcx, r14
00724C1F  E8 4C DC 45 00                  call 0x140b82870
00724C24  8B C7                           mov eax, edi
00724C26  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
00724C2A  48 33 CC                        xor rcx, rsp
00724C2D  E8 0E 7A F8 FF                  call 0x1406ac640
00724C32  48 81 C4 C8 00 00 00            add rsp, 0xc8
00724C39  41 5F                           pop r15
00724C3B  41 5E                           pop r14
00724C3D  41 5D                           pop r13
00724C3F  41 5C                           pop r12
00724C41  5F                              pop rdi
00724C42  5E                              pop rsi
00724C43  5B                              pop rbx
00724C44  5D                              pop rbp
00724C45  C3                              ret
00724C46  CC                              int3
00724C47  45 33 C9                        xor r9d, r9d
00724C4A  C7 44 24 28 20 00 00 40         mov dword ptr [rsp + 0x28], 0x40000020
00724C52  33 D2                           xor edx, edx
00724C54  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00724C58  49 8B CC                        mov rcx, r12
00724C5B  45 8D 41 01                     lea r8d, [r9 + 1]
00724C5F  E8 9C 3B BF FF                  call 0x140318800
00724C64  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
00724C68  48 8B C8                        mov rcx, rax
00724C6B  48 85 C0                        test rax, rax
00724C6E  0F 84 34 FF FF FF               je 0x140724ba8
00724C74  4C 8B 45 B7                     mov r8, qword ptr [rbp - 0x49]
00724C78  33 D2                           xor edx, edx
00724C7A  E8 C1 1F FA FF                  call 0x1406c6c40
00724C7F  8B 45 93                        mov eax, dword ptr [rbp - 0x6d]
00724C82  B9 40 00 00 00                  mov ecx, 0x40
00724C87  41 B8 50 6E 70 61               mov r8d, 0x61706e50
00724C8D  8D 04 45 18 00 00 00            lea eax, [rax*2 + 0x18]
00724C94  8B D0                           mov edx, eax
00724C96  89 45 97                        mov dword ptr [rbp - 0x69], eax
00724C99  E8 52 D4 45 00                  call 0x140b820f0
00724C9E  4C 8B F8                        mov r15, rax
00724CA1  48 85 C0                        test rax, rax
00724CA4  0F 84 03 FF FF FF               je 0x140724bad
00724CAA  8B 4D 6F                        mov ecx, dword ptr [rbp + 0x6f]
00724CAD  BF 02 00 00 00                  mov edi, 2
00724CB2  66 89 38                        mov word ptr [rax], di
00724CB5  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00724CB9  49 89 47 08                     mov qword ptr [r15 + 8], rax
00724CBD  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
00724CC1  41 89 4F 14                     mov dword ptr [r15 + 0x14], ecx
00724CC5  48 85 C0                        test rax, rax
00724CC8  74 08                           je 0x140724cd2
00724CCA  0F B7 08                        movzx ecx, word ptr [rax]
00724CCD  66 41 89 4F 10                  mov word ptr [r15 + 0x10], cx
00724CD2  BA 38 00 00 00                  mov edx, 0x38
00724CD7  41 B8 50 6E 70 61               mov r8d, 0x61706e50
00724CDD  8D 4A 08                        lea ecx, [rdx + 8]
00724CE0  E8 0B D4 45 00                  call 0x140b820f0
00724CE5  4C 8B F0                        mov r14, rax
00724CE8  48 85 C0                        test rax, rax
00724CEB  0F 84 B7 FE FF FF               je 0x140724ba8
00724CF1  0F 10 45 E7                     movups xmm0, xmmword ptr [rbp - 0x19]
00724CF5  F3 0F 7F 40 10                  movdqu xmmword ptr [rax + 0x10], xmm0
00724CFA  48 85 F6                        test rsi, rsi
00724CFD  75 05                           jne 0x140724d04
00724CFF  8D 46 01                        lea eax, [rsi + 1]
00724D02  EB 1B                           jmp 0x140724d1f
00724D04  8B 45 93                        mov eax, dword ptr [rbp - 0x6d]
00724D07  49 8D 4F 18                     lea rcx, [r15 + 0x18]
00724D0B  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
00724D0F  03 C0                           add eax, eax
00724D11  44 8B C0                        mov r8d, eax
00724D14  41 89 47 04                     mov dword ptr [r15 + 4], eax
00724D18  E8 23 1B FA FF                  call 0x1406c6840
00724D1D  8B C7                           mov eax, edi
00724D1F  4C 8D 4D 8F                     lea r9, [rbp - 0x71]
00724D23  41 89 06                        mov dword ptr [r14], eax
00724D26  45 33 C0                        xor r8d, r8d
00724D29  33 D2                           xor edx, edx
00724D2B  49 8B CC                        mov rcx, r12
00724D2E  48 FF 15 B3 C5 A2 FF            call qword ptr [rip - 0x5d3a4d]
00724D35  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00724D3A  8B 55 8F                        mov edx, dword ptr [rbp - 0x71]
00724D3D  B9 40 00 00 00                  mov ecx, 0x40
00724D42  48 C1 E2 03                     shl rdx, 3
00724D46  41 B8 50 6E 70 61               mov r8d, 0x61706e50
00724D4C  E8 9F D3 45 00                  call 0x140b820f0
00724D51  48 8B F0                        mov rsi, rax
00724D54  48 85 C0                        test rax, rax
00724D57  75 0A                           jne 0x140724d63
00724D59  BF 9A 00 00 C0                  mov edi, 0xc000009a
00724D5E  E9 4D FE FF FF                  jmp 0x140724bb0
00724D63  44 8B 45 8F                     mov r8d, dword ptr [rbp - 0x71]
00724D67  4C 8D 4D 8F                     lea r9, [rbp - 0x71]
00724D6B  48 8B D6                        mov rdx, rsi
00724D6E  49 8B CC                        mov rcx, r12
00724D71  48 FF 15 70 C5 A2 FF            call qword ptr [rip - 0x5d3a90]
00724D78  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00724D7D  8B F8                           mov edi, eax
00724D7F  85 C0                           test eax, eax
00724D81  0F 88 29 FE FF FF               js 0x140724bb0
00724D87  44 8B 45 8F                     mov r8d, dword ptr [rbp - 0x71]
00724D8B  48 8D 45 CF                     lea rax, [rbp - 0x31]
00724D8F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00724D94  48 8D 4D E7                     lea rcx, [rbp - 0x19]
00724D98  8B 45 97                        mov eax, dword ptr [rbp - 0x69]
00724D9B  4D 8B CF                        mov r9, r15
00724D9E  48 8B D6                        mov rdx, rsi
00724DA1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00724DA5  48 FF 15 64 C5 A2 FF            call qword ptr [rip - 0x5d3a9c]
00724DAC  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00724DB1  8B F8                           mov edi, eax
00724DB3  85 C0                           test eax, eax
00724DB5  0F 88 F5 FD FF FF               js 0x140724bb0
00724DBB  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00724DBF  49 89 46 28                     mov qword ptr [r14 + 0x28], rax
00724DC3  4D 89 7E 30                     mov qword ptr [r14 + 0x30], r15
00724DC7  4C 8B FB                        mov r15, rbx
00724DCA  4D 89 66 08                     mov qword ptr [r14 + 8], r12
00724DCE  4C 8B E3                        mov r12, rbx
00724DD1  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
00724DD5  49 89 46 20                     mov qword ptr [r14 + 0x20], rax
00724DD9  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
00724DDD  48 89 5D 9F                     mov qword ptr [rbp - 0x61], rbx
00724DE1  4C 89 30                        mov qword ptr [rax], r14
00724DE4  4C 8B F3                        mov r14, rbx
00724DE7  E9 C4 FD FF FF                  jmp 0x140724bb0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoReserveKsrPersistentMemoryEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m47;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;

    v_rsp = (v_rsp) - (200);
    result = (*(unsigned __int64 *)(v_rip + 7233120)) ^ (v_rsp);
    v_stack_m50 = result;
    v_rbx = 0;
    v_stack_m68 = a8;
    v_stack_m78 = 0;
    v_stack_m70 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_mB8 = 0;
    v_stack_m80 = a4;
    v_stack_m88 = a3;
    v_stack_m90 = a1;
    result = v_cr8;
    if ((unsigned __int8)(v_cr8) != 0) {
        result = v_cr8;
        a3 = (unsigned __int8)(result);
        a2 = v_rbx + 1;
        a4 = 0;
        v_stack_mE8 = 0;
        a1 = 289;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (a2 == 0) goto loc_00724A77;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) == 0) goto loc_00724964;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) + 396)) & (0x20000ULL)) == 0) goto loc_00724A77;
loc_00724964:
    result = IoAddTriageDumpDataBlock(a2, *(unsigned __int16 *)(a2 + 2), a3, a4);
    if (*(unsigned __int64 *)(a2 + 8) == 0) goto loc_007249AC;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(a2 + 8), (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 8) + 2)), a3, a4);
    a1 = (*(unsigned __int64 *)(a2 + 8)) + (56);
    if ((*(unsigned __int16 *)(a1)) != 0) {
        a2 = 2;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(a2 + 8);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) == 0) goto loc_00724A5E;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40), 904, a3, a4);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) + 40)) != 0) {
        a2 = 2;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) + 40);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) + 40 + 8);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40)) + (56);
    result = *(unsigned __int64 *)(a2 + 312);
    if ((*(unsigned __int16 *)(a1)) != 0) {
        a2 = 2;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(a2 + 312);
        a1 = *(unsigned __int64 *)(result + 40);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) + 16) == 0) goto loc_00724A5E;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) + 16);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) + 16) + 56)) != 0) {
        a2 = 2;
        result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) + 16) + 56, a2, a3, a4);
        result = *(unsigned __int64 *)(a2 + 312);
        a1 = *(unsigned __int64 *)(result + 40);
        a1 = *(unsigned __int64 *)(a1 + 16);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    a4 = 0;
    v_stack_mE8 = 0;
    result = KeBugCheckEx(202, 2, a2, a4);
loc_00724A77:
    v_stack_mA8 = 0;
    v_stack_m98 = 0;
    v_stack_mB4 = 0;
    v_stack_mA0 = 0;
    v_stack_mB0 = 0;
    if ((*(unsigned __int8 *)(v_rip + 8806155)) != 0) goto loc_00724AA7;
    goto loc_00724C24;
loc_00724AA7:
    if (a7 == 0) goto loc_00724AB6;
    goto loc_00724C24;
loc_00724AB6:
    result = PipGetDriverKsrGuid(202, v_stack_m60, a2, a4);
    if (sign_flag) goto loc_00724C24;
    if (a2 == 0) goto loc_00724B24;
    if (v_stack_m88 == 0) goto loc_00724AFC;
    v_stack_m98 = *(unsigned __int64 *)(v_stack_m88 + 8);
    if (*(unsigned __int64 *)(v_stack_m88 + 8) == 0) goto loc_00724AF2;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m88)) == 0) goto loc_00724AF2;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m88)))) >> (1));
    goto loc_00724B21;
loc_00724AF2:
    goto loc_00724C24;
loc_00724AFC:
    result = PipGetDeviceObjectLocation(a2, v_stack_mB0, v_stack_mA0, a4);
    if (sign_flag) goto loc_00724BAD;
    v_stack_m98 = v_stack_mA0;
loc_00724B21:
    v_stack_mB4 = (unsigned int)((unsigned int)(v_stack_mB0));
loc_00724B24:
    v_stack_mC8 = 1;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = v_stack_m70;
    v_stack_mE8 = 0;
    result = PipGetPersistentMemory(v_stack_m90, a2, v_stack_m88, v_stack_m80);
    v_rdi = 0;
    if (((unsigned int)(result)) != 0xC0000034ULL) { v_rdi = (unsigned int)(result); }
    if (sign_flag) goto loc_00724BAD;
    result = (a6) + (0x1007ULL);
    v_stack_mE0 = 20;
    result = (result) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_mE8 = 1;
    v_stack_m90 = result;
    a2 = (a2) | (-1);
    result = MmAllocatePagesForMdlEx(0, a2, 0, result);
    if (result != 0) goto loc_00724C47;
loc_00724BA8:
loc_00724BAD:
loc_00724BB0:
    if (v_stack_mA0 != 0) {
        a2 = 0x61706E50ULL;
        a1 = v_stack_mA0;
        result = ExFreePoolWithTag(a1, a2, 0, result);
    }
    if (0 != 0) {
        a2 = (unsigned int)((unsigned int)(0x61706E50ULL));
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, 0, result);
    }
    if (result == 0) goto loc_00724C04;
    result = v_stack_mA8;
    if (v_stack_mA8 != 0) {
        a2 = result;
        a1 = v_stack_mA8;
        result = MmUnmapLockedPages(a1, a2, 0, result);
    }
    result = MmFreePagesFromMdl(result, a2, 0, result);
    result = ExFreePoolWithTag(result, (unsigned int)((unsigned int)((unsigned int)(0x61706E50ULL))), 0, result);
loc_00724C04:
    if (0 != 0) {
        a2 = (unsigned int)((unsigned int)(0x61706E50ULL));
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, 0, result);
    }
    if (0 != 0) {
        a2 = (unsigned int)((unsigned int)(0x61706E50ULL));
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, 0, result);
    }
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 0, result);
    v_rsp = (v_rsp) + (200);
    return result;
loc_00724C47:
    a4 = 0;
    v_stack_p28 = 0x40000020ULL;
    a2 = 0;
    v_stack_p20 = 0;
    result = MmMapLockedPagesSpecifyCache(result, a2, a4 + 1, a4);
    v_stack_mA8 = result;
    if (result == 0) goto loc_00724BA8;
    a2 = 0;
    result = memset(result, a2, v_stack_m90, a4);
    v_stack_mB0 = (unsigned int)((unsigned int)(v_stack_mB4) * 2 + 24);
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)((unsigned int)(v_stack_mB4) * 2 + 24)), (unsigned int)(0x61706E50ULL), a4);
    if (result == 0) goto loc_00724BAD;
    *(unsigned __int16 *)(result) = 2;
    *(unsigned __int64 *)(result + 8) = a6;
    *(unsigned int *)(result + 20) = (unsigned int)((unsigned int)(a5));
    if (v_stack_m80 != 0) {
        a1 = *(unsigned __int16 *)(v_stack_m80);
        *(unsigned __int16 *)(result + 16) = (unsigned __int16)(a1);
    }
    result = ExAllocatePool2(56 + 8, 56, (unsigned int)(0x61706E50ULL), a4);
    if (result == 0) goto loc_00724BA8;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    if (0 != 0) goto loc_00724D04;
    goto loc_00724D1F;
loc_00724D04:
    result = (unsigned int)(((unsigned int)(v_stack_mB4)) + ((unsigned int)((unsigned int)(v_stack_mB4))));
    *(unsigned int *)(result + 4) = (unsigned int)(result);
    result = memcpy(result + 24, v_stack_m98, (unsigned int)((unsigned int)(result)), a4);
loc_00724D1F:
    *(unsigned int *)(result) = 2;
    a3 = 0;
    a2 = 0;
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrMdlToMemoryRuns(result, a2, a3, v_stack_mB8);
    a2 = ((unsigned int)(v_stack_mB8)) << (3);
    result = ExAllocatePool2(64, a2, (unsigned int)(0x61706E50ULL), v_stack_mB8);
    if (result != 0) goto loc_00724D63;
    goto loc_00724BB0;
loc_00724D63:
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrMdlToMemoryRuns(result, result, (unsigned int)(v_stack_mB8), v_stack_mB8);
    if (sign_flag) goto loc_00724BB0;
    v_stack_p28 = v_stack_m78;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_mB0));
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrPersistMemoryWithMetadata(v_stack_m60, result, (unsigned int)(v_stack_mB8), result);
    if (sign_flag) goto loc_00724BB0;
    *(unsigned __int64 *)(result + 40) = v_stack_mA8;
    *(unsigned __int64 *)(result + 48) = result;
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result + 32) = v_stack_m78;
    v_stack_mA8 = 0;
    *(unsigned __int64 *)(v_stack_m68) = result;
    goto loc_00724BB0;
}
```

## 5. (Beta) C Style

```c
int64_t IoReserveKsrPersistentMemoryEx(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m47;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;

    local_rsp = (local_rsp) - (200);
    result = (*(uint64_t *)(v_rip + 0x6E5E60)) ^ (local_rsp);
    v_stack_m50 = result;
    local_rbx = 0;
    v_stack_m68 = Arg8;
    v_stack_m78 = 0;
    v_stack_m70 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_mB8 = 0;
    v_stack_m80 = Arg4;
    v_stack_m88 = Arg3;
    v_stack_m90 = Arg1;
    result = v_cr8;
    if ((uint8_t)(v_cr8) != 0) {
        result = v_cr8;
        Arg3 = (uint8_t)(result);
        Arg2 = local_rbx + 1;
        Arg4 = 0;
        v_stack_mE8 = 0;
        Arg1 = 289;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg2 == 0) goto loc_00724A77;
    if (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) == 0) goto loc_00724964;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) + 0x18C)) & (0x20000ULL)) == 0) goto loc_00724A77;
loc_00724964:
    result = IoAddTriageDumpDataBlock(Arg2, *(uint16_t *)(Arg2 + 0x2), Arg3, Arg4);
    if (*(uint64_t *)(Arg2 + 0x8) == 0) goto loc_007249AC;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(Arg2 + 0x8), (int16_t)(*(uint16_t *)(*(uint64_t *)(Arg2 + 0x8) + 0x2)), Arg3, Arg4);
    Arg1 = (*(uint64_t *)(Arg2 + 0x8)) + (56);
    if ((*(uint16_t *)(Arg1)) != 0) {
        Arg2 = 2;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(Arg2 + 0x8);
        Arg2 = *(uint16_t *)(Arg1 + 0x38);
        Arg1 = *(uint64_t *)(Arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) == 0) goto loc_00724A5E;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28), 904, Arg3, Arg4);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) + 0x28)) != 0) {
        Arg2 = 2;
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) + 40;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, Arg3, Arg4);
        Arg2 = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) + 0x28);
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) + 0x28 + 0x8);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28)) + (56);
    result = *(uint64_t *)(Arg2 + 0x138);
    if ((*(uint16_t *)(Arg1)) != 0) {
        Arg2 = 2;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, Arg3, Arg4);
        result = *(uint64_t *)(Arg2 + 0x138);
        Arg1 = *(uint64_t *)(result + 0x28);
        Arg2 = *(uint16_t *)(Arg1 + 0x38);
        Arg1 = *(uint64_t *)(Arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) + 0x10) == 0) goto loc_00724A5E;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) + 0x10);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) + 0x10) + 0x38)) != 0) {
        Arg2 = 2;
        result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) + 0x10) + 56, Arg2, Arg3, Arg4);
        result = *(uint64_t *)(Arg2 + 0x138);
        Arg1 = *(uint64_t *)(result + 0x28);
        Arg1 = *(uint64_t *)(Arg1 + 0x10);
        Arg2 = *(uint16_t *)(Arg1 + 0x38);
        Arg1 = *(uint64_t *)(Arg1 + 0x40);
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, Arg3, Arg4);
    }
    Arg4 = 0;
    v_stack_mE8 = 0;
    result = KeBugCheckEx(202, 2, Arg2, Arg4);
loc_00724A77:
    v_stack_mA8 = 0;
    v_stack_m98 = 0;
    v_stack_mB4 = 0;
    v_stack_mA0 = 0;
    v_stack_mB0 = 0;
    if ((*(uint8_t *)(v_rip + 0x865F0B)) != 0) goto loc_00724AA7;
    goto loc_00724C24;
loc_00724AA7:
    if (Arg7 == 0) goto loc_00724AB6;
    goto loc_00724C24;
loc_00724AB6:
    result = PipGetDriverKsrGuid(202, v_stack_m60, Arg2, Arg4);
    if (sign_flag) goto loc_00724C24;
    if (Arg2 == 0) goto loc_00724B24;
    if (v_stack_m88 == 0) goto loc_00724AFC;
    v_stack_m98 = *(uint64_t *)(v_stack_m88 + 0x8);
    if (*(uint64_t *)(v_stack_m88 + 0x8) == 0) goto loc_00724AF2;
    if ((uint16_t)(*(uint16_t *)(v_stack_m88)) == 0) goto loc_00724AF2;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m88)))) >> (1));
    goto loc_00724B21;
loc_00724AF2:
    goto loc_00724C24;
loc_00724AFC:
    result = PipGetDeviceObjectLocation(Arg2, v_stack_mB0, v_stack_mA0, Arg4);
    if (sign_flag) goto loc_00724BAD;
    v_stack_m98 = v_stack_mA0;
loc_00724B21:
    v_stack_mB4 = (uint32_t)((uint32_t)(v_stack_mB0));
loc_00724B24:
    v_stack_mC8 = 1;
    v_stack_mD0 = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = v_stack_m70;
    v_stack_mE8 = 0;
    result = PipGetPersistentMemory(v_stack_m90, Arg2, v_stack_m88, v_stack_m80);
    local_rdi = 0;
    if (((uint32_t)(result)) != 0xC0000034ULL) { local_rdi = (uint32_t)(result); }
    if (sign_flag) goto loc_00724BAD;
    result = (Arg6) + (0x1007ULL);
    v_stack_mE0 = 20;
    result = (result) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_mE8 = 1;
    v_stack_m90 = result;
    Arg2 = (Arg2) | (-1);
    result = MmAllocatePagesForMdlEx(0, Arg2, 0, result);
    if (result != 0) goto loc_00724C47;
loc_00724BA8:
loc_00724BAD:
loc_00724BB0:
    if (v_stack_mA0 != 0) {
        Arg2 = 0x61706E50ULL;
        Arg1 = v_stack_mA0;
        result = ExFreePoolWithTag(Arg1, Arg2, 0, result);
    }
    if (0 != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x61706E50ULL));
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, 0, result);
    }
    if (result == 0) goto loc_00724C04;
    result = v_stack_mA8;
    if (v_stack_mA8 != 0) {
        Arg2 = result;
        Arg1 = v_stack_mA8;
        result = MmUnmapLockedPages(Arg1, Arg2, 0, result);
    }
    result = MmFreePagesFromMdl(result, Arg2, 0, result);
    result = ExFreePoolWithTag(result, (uint32_t)((uint32_t)((uint32_t)(0x61706E50ULL))), 0, result);
loc_00724C04:
    if (0 != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x61706E50ULL));
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, 0, result);
    }
    if (0 != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x61706E50ULL));
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, 0, result);
    }
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 0, result);
    local_rsp = (local_rsp) + (200);
    return result;
loc_00724C47:
    Arg4 = 0;
    v_stack_p28 = 0x40000020ULL;
    Arg2 = 0;
    v_stack_p20 = 0;
    result = MmMapLockedPagesSpecifyCache(result, Arg2, Arg4 + 1, Arg4);
    v_stack_mA8 = result;
    if (result == 0) goto loc_00724BA8;
    Arg2 = 0;
    result = memset(result, Arg2, v_stack_m90, Arg4);
    v_stack_mB0 = (uint32_t)((uint32_t)(v_stack_mB4) * 2 + 24);
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)((uint32_t)(v_stack_mB4) * 2 + 24)), (uint32_t)(0x61706E50ULL), Arg4);
    if (result == 0) goto loc_00724BAD;
    *(uint16_t *)(result) = 2;
    *(uint64_t *)(result + 0x8) = Arg6;
    *(uint32_t *)(result + 0x14) = (uint32_t)((uint32_t)(Arg5));
    if (v_stack_m80 != 0) {
        Arg1 = *(uint16_t *)(v_stack_m80);
        *(uint16_t *)(result + 0x10) = (uint16_t)(Arg1);
    }
    result = ExAllocatePool2(56 + 8, 56, (uint32_t)(0x61706E50ULL), Arg4);
    if (result == 0) goto loc_00724BA8;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    if (0 != 0) goto loc_00724D04;
    goto loc_00724D1F;
loc_00724D04:
    result = (uint32_t)(((uint32_t)(v_stack_mB4)) + ((uint32_t)((uint32_t)(v_stack_mB4))));
    *(uint32_t *)(result + 0x4) = (uint32_t)(result);
    result = memcpy(result + 24, v_stack_m98, (uint32_t)((uint32_t)(result)), Arg4);
loc_00724D1F:
    *(uint32_t *)(result) = 2;
    Arg3 = 0;
    Arg2 = 0;
    result = kernel_indirect_call(result, Arg2, Arg3, v_stack_mB8);
    Arg2 = ((uint32_t)(v_stack_mB8)) << (3);
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x61706E50ULL), v_stack_mB8);
    if (result != 0) goto loc_00724D63;
    goto loc_00724BB0;
loc_00724D63:
    result = kernel_indirect_call(result, result, (uint32_t)(v_stack_mB8), v_stack_mB8);
    if (sign_flag) goto loc_00724BB0;
    v_stack_p28 = v_stack_m78;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_mB0));
    result = kernel_indirect_call(v_stack_m60, result, (uint32_t)(v_stack_mB8), result);
    if (sign_flag) goto loc_00724BB0;
    *(uint64_t *)(result + 0x28) = v_stack_mA8;
    *(uint64_t *)(result + 0x30) = result;
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result + 0x20) = v_stack_m78;
    v_stack_mA8 = 0;
    *(uint64_t *)(v_stack_m68) = result;
    goto loc_00724BB0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007248C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
