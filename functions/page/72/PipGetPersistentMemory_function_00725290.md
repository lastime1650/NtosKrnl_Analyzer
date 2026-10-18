# PipGetPersistentMemory

- RVA: `0x00725290`–`0x00725946` (길이 `1,718` bytes)
- VA: `0x0000000140725290`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BBC24`
- 디코드: `452`개 명령, `1,718/1,718` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **37**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00725327` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0072533F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00725355` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00725366` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00725388` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00725399` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007253A5` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007253C2` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x007253DA` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00725400` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0072541C` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00725434` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0072546A` → [PipGetDriverKsrGuid](PipGetDriverKsrGuid_function_00725100.md) (function, `0x00725100`)
- `0x0072548F` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrEnumeratePersistedMemory` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrEnumeratePersistedMemory`)
- `0x007254C8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007254EF` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrEnumeratePersistedMemory` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrEnumeratePersistedMemory`)
- `0x00725555` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrQueryMetadata` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrQueryMetadata`)
- `0x0072556E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00725596` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrQueryMetadata` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrQueryMetadata`)
- `0x007255DC` → [PipMatchPersistentMemory](PipMatchPersistentMemory_function_0072594C.md) (function, `0x0072594C`)
- `0x00725601` → [PipUnpackMetadata](../../text/5A/PipUnpackMetadata_function_005A54AC.md) (function, `0x005A54AC`)
- `0x00725623` → [PipMatchPersistentMemoryV1](PipMatchPersistentMemoryV1_function_00725A30.md) (function, `0x00725A30`)
- `0x0072564F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0072567A` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrClaimPersistedMemory` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrClaimPersistedMemory`)
- `0x007256AA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007256DD` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrClaimPersistedMemory` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrClaimPersistedMemory`)
- `0x0072572E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007257D2` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x00725810` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00725824` → [MmUnmapLockedPages](../../text/24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)
- `0x0072583A` → `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrFreePersistedMemoryBlock` (import, 간접 대상; import `ext-ms-win-ntos-ksr-l1-1-5.dll!KsrFreePersistedMemoryBlock`)
- `0x0072588F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007258E6` → [MmUnmapLockedPages](../../text/24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)
- `0x007258F3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00725905` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00725917` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00725925` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IoAcquireKsrPersistentMemoryEx](IoAcquireKsrPersistentMemoryEx_function_007241A0.md) at `0x0072434C`
- [IoMapKsrPersistentMemoryEx](IoMapKsrPersistentMemoryEx_function_00724490.md) at `0x0072464A`
- [IoQueryKsrPersistentMemorySizeEx](IoQueryKsrPersistentMemorySizeEx_function_007246A0.md) at `0x00724843`
- [IoReserveKsrPersistentMemoryEx](IoReserveKsrPersistentMemoryEx_function_007248C0.md) at `0x00724B53`

### Static image references
- `0x007252AC` → RVA `0x00E0A740` (`.data`; read)
- `0x00725480` → RVA `0x00724E80` (`PipEnumeratePersistedMemory`; read)
- `0x0072548F` → RVA `0x00151330` (`ext-ms-win-ntos-ksr-l1-1-5.dll!KsrEnumeratePersistedMemory (IAT)`; read)
- `0x00725555` → RVA `0x00151328` (`ext-ms-win-ntos-ksr-l1-1-5.dll!KsrQueryMetadata (IAT)`; read)
- `0x0072567A` → RVA `0x001512F0` (`ext-ms-win-ntos-ksr-l1-1-5.dll!KsrClaimPersistedMemory (IAT)`; read)
- `0x0072583A` → RVA `0x00151320` (`ext-ms-win-ntos-ksr-l1-1-5.dll!KsrFreePersistedMemoryBlock (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **27**
  - `0x00725327` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x0072533F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00725355` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00725366` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00725388` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00725399` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007253A5` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007253C2` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x007253DA` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00725400` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x0072541C` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00725434` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x007254C8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0072556E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00725601` → [PipUnpackMetadata](../../text/5A/PipUnpackMetadata_function_005A54AC.md) (`PAGE` → `.text`)
  - `0x0072564F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007256AA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0072572E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007257D2` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (`PAGE` → `.text`)
  - `0x00725810` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00725824` → [MmUnmapLockedPages](../../text/24/MmUnmapLockedPages_function_00246E60.md) (`PAGE` → `.text`)
  - `0x0072588F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007258E6` → [MmUnmapLockedPages](../../text/24/MmUnmapLockedPages_function_00246E60.md) (`PAGE` → `.text`)
  - `0x007258F3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00725905` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00725917` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00725925` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00725290  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00725295  55                              push rbp
00725296  56                              push rsi
00725297  57                              push rdi
00725298  41 54                           push r12
0072529A  41 55                           push r13
0072529C  41 56                           push r14
0072529E  41 57                           push r15
007252A0  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
007252A5  48 81 EC B0 00 00 00            sub rsp, 0xb0
007252AC  48 8B 05 8D 54 6E 00            mov rax, qword ptr [rip + 0x6e548d]
007252B3  48 33 C4                        xor rax, rsp
007252B6  48 89 45 FF                     mov qword ptr [rbp - 1], rax
007252BA  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
007252BE  48 8B F2                        mov rsi, rdx
007252C1  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
007252C5  45 33 FF                        xor r15d, r15d
007252C8  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
007252CC  0F 57 C0                        xorps xmm0, xmm0
007252CF  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
007252D3  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
007252D7  48 89 55 E7                     mov qword ptr [rbp - 0x19], rdx
007252DB  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
007252DF  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
007252E3  4C 89 4D CF                     mov qword ptr [rbp - 0x31], r9
007252E7  4C 89 45 D7                     mov qword ptr [rbp - 0x29], r8
007252EB  48 89 55 B7                     mov qword ptr [rbp - 0x49], rdx
007252EF  44 89 7D 8B                     mov dword ptr [rbp - 0x75], r15d
007252F3  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
007252F7  48 85 F6                        test rsi, rsi
007252FA  0F 84 3A 01 00 00               je 0x14072543a
00725300  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00725307  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
0072530B  48 85 C0                        test rax, rax
0072530E  74 10                           je 0x140725320
00725310  F7 80 8C 01 00 00 00 00 02 00   test dword ptr [rax + 0x18c], 0x20000
0072531A  0F 84 1A 01 00 00               je 0x14072543a
00725320  0F B7 56 02                     movzx edx, word ptr [rsi + 2]
00725324  48 8B CE                        mov rcx, rsi
00725327  E8 48 30 D0 FF                  call 0x140428374
0072532C  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00725330  41 BD 02 00 00 00               mov r13d, 2
00725336  48 85 C9                        test rcx, rcx
00725339  74 30                           je 0x14072536b
0072533B  0F BF 51 02                     movsx edx, word ptr [rcx + 2]
0072533F  E8 30 30 D0 FF                  call 0x140428374
00725344  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00725348  48 83 C1 38                     add rcx, 0x38
0072534C  66 44 39 39                     cmp word ptr [rcx], r15w
00725350  74 19                           je 0x14072536b
00725352  41 8B D5                        mov edx, r13d
00725355  E8 1A 30 D0 FF                  call 0x140428374
0072535A  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0072535E  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00725362  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00725366  E8 09 30 D0 FF                  call 0x140428374
0072536B  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
00725372  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00725376  48 85 C9                        test rcx, rcx
00725379  0F 84 A2 00 00 00               je 0x140725421
0072537F  BA 88 03 00 00                  mov edx, 0x388
00725384  48 8D 59 28                     lea rbx, [rcx + 0x28]
00725388  E8 E7 2F D0 FF                  call 0x140428374
0072538D  66 44 39 3B                     cmp word ptr [rbx], r15w
00725391  74 17                           je 0x1407253aa
00725393  41 8B D5                        mov edx, r13d
00725396  48 8B CB                        mov rcx, rbx
00725399  E8 D6 2F D0 FF                  call 0x140428374
0072539E  0F B7 13                        movzx edx, word ptr [rbx]
007253A1  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
007253A5  E8 CA 2F D0 FF                  call 0x140428374
007253AA  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
007253B1  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
007253B5  48 83 C1 38                     add rcx, 0x38
007253B9  66 44 39 39                     cmp word ptr [rcx], r15w
007253BD  74 20                           je 0x1407253df
007253BF  41 8B D5                        mov edx, r13d
007253C2  E8 AD 2F D0 FF                  call 0x140428374
007253C7  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
007253CE  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
007253D2  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
007253D6  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
007253DA  E8 95 2F D0 FF                  call 0x140428374
007253DF  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
007253E6  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
007253EA  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
007253EE  48 85 C0                        test rax, rax
007253F1  74 2E                           je 0x140725421
007253F3  48 8D 48 38                     lea rcx, [rax + 0x38]
007253F7  66 44 39 39                     cmp word ptr [rcx], r15w
007253FB  74 24                           je 0x140725421
007253FD  41 8B D5                        mov edx, r13d
00725400  E8 6F 2F D0 FF                  call 0x140428374
00725405  48 8B 86 38 01 00 00            mov rax, qword ptr [rsi + 0x138]
0072540C  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00725410  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00725414  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00725418  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
0072541C  E8 53 2F D0 FF                  call 0x140428374
00725421  45 33 C9                        xor r9d, r9d
00725424  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00725429  4C 8B C6                        mov r8, rsi
0072542C  49 8B D5                        mov rdx, r13
0072542F  B9 CA 00 00 00                  mov ecx, 0xca
00725434  E8 27 82 DD FF                  call 0x1404fd660
00725439  CC                              int3
0072543A  44 89 7D 8F                     mov dword ptr [rbp - 0x71], r15d
0072543E  41 8A C7                        mov al, r15b
00725441  88 45 88                        mov byte ptr [rbp - 0x78], al
00725444  4D 8B E7                        mov r12, r15
00725447  88 45 87                        mov byte ptr [rbp - 0x79], al
0072544A  B8 01 00 00 00                  mov eax, 1
0072544F  48 85 D2                        test rdx, rdx
00725452  74 12                           je 0x140725466
00725454  84 85 87 00 00 00               test byte ptr [rbp + 0x87], al
0072545A  74 0A                           je 0x140725466
0072545C  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00725461  E9 B6 04 00 00                  jmp 0x14072591c
00725466  48 8D 55 EF                     lea rdx, [rbp - 0x11]
0072546A  E8 91 FC FF FF                  call 0x140725100
0072546F  8B D8                           mov ebx, eax
00725471  85 C0                           test eax, eax
00725473  0F 88 A3 04 00 00               js 0x14072591c
00725479  0F 57 C0                        xorps xmm0, xmm0
0072547C  4C 8D 45 BF                     lea r8, [rbp - 0x41]
00725480  48 8D 15 F9 F9 FF FF            lea rdx, [rip - 0x607]
00725487  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0072548B  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
0072548F  48 FF 15 9A BE A2 FF            call qword ptr [rip - 0x5d4166]
00725496  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0072549B  8B D8                           mov ebx, eax
0072549D  85 C0                           test eax, eax
0072549F  0F 88 77 04 00 00               js 0x14072591c
007254A5  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
007254A8  85 C0                           test eax, eax
007254AA  75 0A                           jne 0x1407254b6
007254AC  BB 34 00 00 C0                  mov ebx, 0xc0000034
007254B1  E9 66 04 00 00                  jmp 0x14072591c
007254B6  48 8B D0                        mov rdx, rax
007254B9  B9 40 00 00 00                  mov ecx, 0x40
007254BE  48 C1 E2 03                     shl rdx, 3
007254C2  41 B8 50 6E 70 61               mov r8d, 0x61706e50
007254C8  E8 23 CC 45 00                  call 0x140b820f0
007254CD  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
007254D1  48 85 C0                        test rax, rax
007254D4  75 0A                           jne 0x1407254e0
007254D6  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007254DB  E9 3C 04 00 00                  jmp 0x14072591c
007254E0  4C 8D 45 BF                     lea r8, [rbp - 0x41]
007254E4  48 8D 15 95 F9 FF FF            lea rdx, [rip - 0x66b]
007254EB  48 8D 4D EF                     lea rcx, [rbp - 0x11]
007254EF  48 FF 15 3A BE A2 FF            call qword ptr [rip - 0x5d41c6]
007254F6  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007254FB  8B D8                           mov ebx, eax
007254FD  85 C0                           test eax, eax
007254FF  0F 88 17 04 00 00               js 0x14072591c
00725505  41 8B DF                        mov ebx, r15d
00725508  4C 89 7D 97                     mov qword ptr [rbp - 0x69], r15
0072550C  89 5D 9F                        mov dword ptr [rbp - 0x61], ebx
0072550F  4D 8B F7                        mov r14, r15
00725512  49 8B FF                        mov rdi, r15
00725515  41 BD 02 00 00 00               mov r13d, 2
0072551B  3B 5D C7                        cmp ebx, dword ptr [rbp - 0x39]
0072551E  0F 83 37 03 00 00               jae 0x14072585b
00725524  45 33 FF                        xor r15d, r15d
00725527  40 38 7D 88                     cmp byte ptr [rbp - 0x78], dil
0072552B  0F 85 43 03 00 00               jne 0x140725874
00725531  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
00725535  45 33 C9                        xor r9d, r9d
00725538  8B CB                           mov ecx, ebx
0072553A  45 33 C0                        xor r8d, r8d
0072553D  48 8B 1C C8                     mov rbx, qword ptr [rax + rcx*8]
00725541  48 8D 45 8F                     lea rax, [rbp - 0x71]
00725545  48 8B D3                        mov rdx, rbx
00725548  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0072554D  48 8D 4D EF                     lea rcx, [rbp - 0x11]
00725551  48 89 5D 97                     mov qword ptr [rbp - 0x69], rbx
00725555  48 FF 15 CC BD A2 FF            call qword ptr [rip - 0x5d4234]
0072555C  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00725561  8B 55 8F                        mov edx, dword ptr [rbp - 0x71]
00725564  41 8D 4F 40                     lea ecx, [r15 + 0x40]
00725568  41 B8 50 6E 70 61               mov r8d, 0x61706e50
0072556E  E8 7D CB 45 00                  call 0x140b820f0
00725573  4C 8B F8                        mov r15, rax
00725576  48 85 C0                        test rax, rax
00725579  0F 84 57 FF FF FF               je 0x1407254d6
0072557F  44 8B 4D 8F                     mov r9d, dword ptr [rbp - 0x71]
00725583  48 8D 45 8F                     lea rax, [rbp - 0x71]
00725587  4D 8B C7                        mov r8, r15
0072558A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0072558F  48 8B D3                        mov rdx, rbx
00725592  48 8D 4D EF                     lea rcx, [rbp - 0x11]
00725596  48 FF 15 8B BD A2 FF            call qword ptr [rip - 0x5d4275]
0072559D  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007255A2  8B D8                           mov ebx, eax
007255A4  85 C0                           test eax, eax
007255A6  0F 88 51 03 00 00               js 0x1407258fd
007255AC  44 39 6D 8F                     cmp dword ptr [rbp - 0x71], r13d
007255B0  0F 82 9B 02 00 00               jb 0x140725851
007255B6  41 0F B7 07                     movzx eax, word ptr [r15]
007255BA  66 41 3B C5                     cmp ax, r13w
007255BE  75 48                           jne 0x140725608
007255C0  4C 8B 45 CF                     mov r8, qword ptr [rbp - 0x31]
007255C4  48 8D 45 87                     lea rax, [rbp - 0x79]
007255C8  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
007255CC  4D 8B CF                        mov r9, r15
007255CF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007255D4  48 8B CE                        mov rcx, rsi
007255D7  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
007255DC  E8 6B 03 00 00                  call 0x14072594c
007255E1  8B D8                           mov ebx, eax
007255E3  85 C0                           test eax, eax
007255E5  0F 88 12 03 00 00               js 0x1407258fd
007255EB  44 8A 4D 87                     mov r9b, byte ptr [rbp - 0x79]
007255EF  44 88 4D 88                     mov byte ptr [rbp - 0x78], r9b
007255F3  45 84 C9                        test r9b, r9b
007255F6  74 47                           je 0x14072563f
007255F8  4C 8B 45 DF                     mov r8, qword ptr [rbp - 0x21]
007255FC  33 D2                           xor edx, edx
007255FE  49 8B CF                        mov rcx, r15
00725601  E8 A6 FE E7 FF                  call 0x1405a54ac
00725606  EB 32                           jmp 0x14072563a
00725608  BA 01 00 00 00                  mov edx, 1
0072560D  66 3B C2                        cmp ax, dx
00725610  0F 85 3B 02 00 00               jne 0x140725851
00725616  4C 8D 4D 87                     lea r9, [rbp - 0x79]
0072561A  45 33 C0                        xor r8d, r8d
0072561D  49 8B D7                        mov rdx, r15
00725620  48 8B CE                        mov rcx, rsi
00725623  E8 08 04 00 00                  call 0x140725a30
00725628  8B D8                           mov ebx, eax
0072562A  85 C0                           test eax, eax
0072562C  0F 88 CB 02 00 00               js 0x1407258fd
00725632  44 8A 4D 87                     mov r9b, byte ptr [rbp - 0x79]
00725636  44 88 4D 88                     mov byte ptr [rbp - 0x78], r9b
0072563A  45 84 C9                        test r9b, r9b
0072563D  75 1D                           jne 0x14072565c
0072563F  8B 5D 9F                        mov ebx, dword ptr [rbp - 0x61]
00725642  BA 50 6E 70 61                  mov edx, 0x61706e50
00725647  FF C3                           inc ebx
00725649  49 8B CF                        mov rcx, r15
0072564C  89 5D 9F                        mov dword ptr [rbp - 0x61], ebx
0072564F  E8 1C D2 45 00                  call 0x140b82870
00725654  45 33 FF                        xor r15d, r15d
00725657  E9 BF FE FF FF                  jmp 0x14072551b
0072565C  4C 8B 75 97                     mov r14, qword ptr [rbp - 0x69]
00725660  48 8D 45 8B                     lea rax, [rbp - 0x75]
00725664  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00725669  48 8D 4D EF                     lea rcx, [rbp - 0x11]
0072566D  21 7C 24 20                     and dword ptr [rsp + 0x20], edi
00725671  49 8B D6                        mov rdx, r14
00725674  45 33 C9                        xor r9d, r9d
00725677  45 33 C0                        xor r8d, r8d
0072567A  48 FF 15 6F BC A2 FF            call qword ptr [rip - 0x5d4391]
00725681  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00725686  33 DB                           xor ebx, ebx
00725688  3D 23 00 00 C0                  cmp eax, 0xc0000023
0072568D  0F 45 D8                        cmovne ebx, eax
00725690  85 DB                           test ebx, ebx
00725692  0F 88 65 02 00 00               js 0x1407258fd
00725698  8B 55 8B                        mov edx, dword ptr [rbp - 0x75]
0072569B  B9 40 00 00 00                  mov ecx, 0x40
007256A0  48 C1 E2 03                     shl rdx, 3
007256A4  41 B8 50 6E 70 61               mov r8d, 0x61706e50
007256AA  E8 41 CA 45 00                  call 0x140b820f0
007256AF  48 8B F8                        mov rdi, rax
007256B2  48 85 C0                        test rax, rax
007256B5  75 0A                           jne 0x1407256c1
007256B7  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007256BC  E9 3C 02 00 00                  jmp 0x1407258fd
007256C1  44 8B 4D 8B                     mov r9d, dword ptr [rbp - 0x75]
007256C5  48 8D 45 8B                     lea rax, [rbp - 0x75]
007256C9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007256CE  48 8D 4D EF                     lea rcx, [rbp - 0x11]
007256D2  44 21 64 24 20                  and dword ptr [rsp + 0x20], r12d
007256D7  4C 8B C7                        mov r8, rdi
007256DA  49 8B D6                        mov rdx, r14
007256DD  48 FF 15 0C BC A2 FF            call qword ptr [rip - 0x5d43f4]
007256E4  0F 1F 44 00 00                  nop dword ptr [rax + rax]
007256E9  8B D8                           mov ebx, eax
007256EB  85 C0                           test eax, eax
007256ED  0F 88 0A 02 00 00               js 0x1407258fd
007256F3  8B 45 8B                        mov eax, dword ptr [rbp - 0x75]
007256F6  85 C0                           test eax, eax
007256F8  74 21                           je 0x14072571b
007256FA  48 8B CF                        mov rcx, rdi
007256FD  8B D0                           mov edx, eax
007256FF  BE 01 00 00 00                  mov esi, 1
00725704  48 8B 01                        mov rax, qword ptr [rcx]
00725707  48 8D 49 08                     lea rcx, [rcx + 8]
0072570B  48 C1 E8 28                     shr rax, 0x28
0072570F  44 03 E0                        add r12d, eax
00725712  48 2B D6                        sub rdx, rsi
00725715  75 ED                           jne 0x140725704
00725717  48 8B 75 E7                     mov rsi, qword ptr [rbp - 0x19]
0072571B  4A 8D 14 E5 30 00 00 00         lea rdx, [r12*8 + 0x30]
00725723  B9 40 00 00 00                  mov ecx, 0x40
00725728  41 B8 50 6E 70 61               mov r8d, 0x61706e50
0072572E  E8 BD C9 45 00                  call 0x140b820f0
00725733  4C 8B F0                        mov r14, rax
00725736  48 85 C0                        test rax, rax
00725739  0F 84 BE 01 00 00               je 0x1407258fd
0072573F  33 DB                           xor ebx, ebx
00725741  41 C1 E4 0C                     shl r12d, 0xc
00725745  48 89 18                        mov qword ptr [rax], rbx
00725748  4D 8D 4E 30                     lea r9, [r14 + 0x30]
0072574C  66 45 89 6E 0A                  mov word ptr [r14 + 0xa], r13w
00725751  41 8B C4                        mov eax, r12d
00725754  C1 E8 0C                        shr eax, 0xc
00725757  8B D3                           mov edx, ebx
00725759  66 83 C0 06                     add ax, 6
0072575D  49 89 5E 20                     mov qword ptr [r14 + 0x20], rbx
00725761  66 C1 E0 03                     shl ax, 3
00725765  44 8D 6B 01                     lea r13d, [rbx + 1]
00725769  66 41 89 46 08                  mov word ptr [r14 + 8], ax
0072576E  41 89 5E 2C                     mov dword ptr [r14 + 0x2c], ebx
00725772  45 89 66 28                     mov dword ptr [r14 + 0x28], r12d
00725776  44 8B 45 8B                     mov r8d, dword ptr [rbp - 0x75]
0072577A  45 85 C0                        test r8d, r8d
0072577D  74 3C                           je 0x1407257bb
0072577F  8B C2                           mov eax, edx
00725781  49 BA FF FF FF FF FF 00 00 00   movabs r10, 0xffffffffff
0072578B  48 8B 0C C7                     mov rcx, qword ptr [rdi + rax*8]
0072578F  48 8B C1                        mov rax, rcx
00725792  48 C1 E9 28                     shr rcx, 0x28
00725796  49 23 C2                        and rax, r10
00725799  85 C9                           test ecx, ecx
0072579B  74 16                           je 0x1407257b3
0072579D  44 8B C1                        mov r8d, ecx
007257A0  49 89 01                        mov qword ptr [r9], rax
007257A3  49 83 C1 08                     add r9, 8
007257A7  49 03 C5                        add rax, r13
007257AA  4D 2B C5                        sub r8, r13
007257AD  75 F1                           jne 0x1407257a0
007257AF  44 8B 45 8B                     mov r8d, dword ptr [rbp - 0x75]
007257B3  41 03 D5                        add edx, r13d
007257B6  41 3B D0                        cmp edx, r8d
007257B9  72 C4                           jb 0x14072577f
007257BB  C7 44 24 28 10 00 00 40         mov dword ptr [rsp + 0x28], 0x40000010
007257C3  45 33 C9                        xor r9d, r9d
007257C6  45 8B C5                        mov r8d, r13d
007257C9  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
007257CD  33 D2                           xor edx, edx
007257CF  49 8B CE                        mov rcx, r14
007257D2  E8 29 30 BF FF                  call 0x140318800
007257D7  4C 8B E0                        mov r12, rax
007257DA  48 85 C0                        test rax, rax
007257DD  75 0A                           jne 0x1407257e9
007257DF  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007257E4  E9 02 01 00 00                  jmp 0x1407258eb
007257E9  4C 8B 4D AF                     mov r9, qword ptr [rbp - 0x51]
007257ED  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
007257F1  48 8B 00                        mov rax, qword ptr [rax]
007257F4  4D 85 C9                        test r9, r9
007257F7  74 4F                           je 0x140725848
007257F9  48 8B 11                        mov rdx, qword ptr [rcx]
007257FC  48 89 01                        mov qword ptr [rcx], rax
007257FF  48 3B D0                        cmp rdx, rax
00725802  72 47                           jb 0x14072584b
00725804  4D 8B 04 24                     mov r8, qword ptr [r12]
00725808  49 8D 54 24 08                  lea rdx, [r12 + 8]
0072580D  49 8B C9                        mov rcx, r9
00725810  E8 2B 10 FA FF                  call 0x1406c6840
00725815  44 84 AD 87 00 00 00            test byte ptr [rbp + 0x87], r13b
0072581C  74 3D                           je 0x14072585b
0072581E  49 8B D6                        mov rdx, r14
00725821  49 8B CC                        mov rcx, r12
00725824  E8 37 16 B2 FF                  call 0x140246e60
00725829  4C 8B E3                        mov r12, rbx
0072582C  48 8D 4D EF                     lea rcx, [rbp - 0x11]
00725830  48 8B 5D 97                     mov rbx, qword ptr [rbp - 0x69]
00725834  45 8A C5                        mov r8b, r13b
00725837  48 8B D3                        mov rdx, rbx
0072583A  48 FF 15 DF BA A2 FF            call qword ptr [rip - 0x5d4521]
00725841  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00725846  EB 17                           jmp 0x14072585f
00725848  48 89 01                        mov qword ptr [rcx], rax
0072584B  48 8B 5D 97                     mov rbx, qword ptr [rbp - 0x69]
0072584F  EB 12                           jmp 0x140725863
00725851  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00725856  E9 A2 00 00 00                  jmp 0x1407258fd
0072585B  48 8B 5D 97                     mov rbx, qword ptr [rbp - 0x69]
0072585F  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00725863  80 7D 88 00                     cmp byte ptr [rbp - 0x78], 0
00725867  75 0F                           jne 0x140725878
00725869  48 83 21 00                     and qword ptr [rcx], 0
0072586D  BB 34 00 00 C0                  mov ebx, 0xc0000034
00725872  EB 62                           jmp 0x1407258d6
00725874  48 8B 5D 97                     mov rbx, qword ptr [rbp - 0x69]
00725878  4C 8B 6D B7                     mov r13, qword ptr [rbp - 0x49]
0072587C  4D 85 ED                        test r13, r13
0072587F  74 53                           je 0x1407258d4
00725881  BA 38 00 00 00                  mov edx, 0x38
00725886  41 B8 50 6E 70 61               mov r8d, 0x61706e50
0072588C  8D 4A 08                        lea ecx, [rdx + 8]
0072588F  E8 5C C8 45 00                  call 0x140b820f0
00725894  48 8B C8                        mov rcx, rax
00725897  48 85 C0                        test rax, rax
0072589A  75 07                           jne 0x1407258a3
0072589C  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007258A1  EB 33                           jmp 0x1407258d6
007258A3  0F 10 45 EF                     movups xmm0, xmmword ptr [rbp - 0x11]
007258A7  48 F7 DE                        neg rsi
007258AA  F3 0F 7F 40 10                  movdqu xmmword ptr [rax + 0x10], xmm0
007258AF  1B C0                           sbb eax, eax
007258B1  F7 D8                           neg eax
007258B3  FF C0                           inc eax
007258B5  89 01                           mov dword ptr [rcx], eax
007258B7  4C 89 79 30                     mov qword ptr [rcx + 0x30], r15
007258BB  45 33 FF                        xor r15d, r15d
007258BE  4C 89 61 28                     mov qword ptr [rcx + 0x28], r12
007258C2  45 33 E4                        xor r12d, r12d
007258C5  4C 89 71 08                     mov qword ptr [rcx + 8], r14
007258C9  45 33 F6                        xor r14d, r14d
007258CC  48 89 59 20                     mov qword ptr [rcx + 0x20], rbx
007258D0  49 89 4D 00                     mov qword ptr [r13], rcx
007258D4  33 DB                           xor ebx, ebx
007258D6  4D 85 F6                        test r14, r14
007258D9  74 1D                           je 0x1407258f8
007258DB  4D 85 E4                        test r12, r12
007258DE  74 0B                           je 0x1407258eb
007258E0  49 8B D6                        mov rdx, r14
007258E3  49 8B CC                        mov rcx, r12
007258E6  E8 75 15 B2 FF                  call 0x140246e60
007258EB  BA 50 6E 70 61                  mov edx, 0x61706e50
007258F0  49 8B CE                        mov rcx, r14
007258F3  E8 78 CF 45 00                  call 0x140b82870
007258F8  4D 85 FF                        test r15, r15
007258FB  74 0D                           je 0x14072590a
007258FD  BA 50 6E 70 61                  mov edx, 0x61706e50
00725902  49 8B CF                        mov rcx, r15
00725905  E8 66 CF 45 00                  call 0x140b82870
0072590A  48 85 FF                        test rdi, rdi
0072590D  74 0D                           je 0x14072591c
0072590F  BA 50 6E 70 61                  mov edx, 0x61706e50
00725914  48 8B CF                        mov rcx, rdi
00725917  E8 54 CF 45 00                  call 0x140b82870
0072591C  8B C3                           mov eax, ebx
0072591E  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
00725922  48 33 CC                        xor rcx, rsp
00725925  E8 16 6D F8 FF                  call 0x1406ac640
0072592A  48 8B 9C 24 08 01 00 00         mov rbx, qword ptr [rsp + 0x108]
00725932  48 81 C4 B0 00 00 00            add rsp, 0xb0
00725939  41 5F                           pop r15
0072593B  41 5E                           pop r14
0072593D  41 5D                           pop r13
0072593F  41 5C                           pop r12
00725941  5F                              pop rdi
00725942  5E                              pop rsi
00725943  5D                              pop rbp
00725944  C3                              ret
00725945  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipGetPersistentMemory(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3F;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int8 v_stack_mB7;
    unsigned __int8 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p48;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 7230605)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m60 = a5;
    v_r15 = 0;
    v_stack_m98 = a6;
    v_stack_m58 = a2;
    v_stack_m90 = a7;
    v_stack_m70 = a4;
    v_stack_m68 = a3;
    v_stack_m88 = a8;
    v_stack_mB4 = 0;
    v_stack_m50 = v_xmm0;
    if (a2 == 0) goto loc_0072543A;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) == 0) goto loc_00725320;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) + 396)) & (0x20000ULL)) == 0) goto loc_0072543A;
loc_00725320:
    result = IoAddTriageDumpDataBlock(a2, *(unsigned __int16 *)(a2 + 2), a3, a4);
    if (*(unsigned __int64 *)(a2 + 8) == 0) goto loc_0072536B;
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
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) == 0) goto loc_00725421;
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
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 312) + 40) + 16) == 0) goto loc_00725421;
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
    v_stack_mC8 = 0;
    result = KeBugCheckEx(202, 2, a2, a4);
loc_0072543A:
    v_stack_mB0 = 0;
    v_stack_mB7 = 0;
    v_stack_mB8 = 0;
    if (2 == 0) goto loc_00725466;
    if (((v_stack_p48) & (1)) == 0) goto loc_00725466;
    goto loc_0072591C;
loc_00725466:
    result = PipGetDriverKsrGuid(202, v_stack_m50, a2, a4);
    if (sign_flag) goto loc_0072591C;
    v_stack_m80 = v_xmm0;
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrEnumeratePersistedMemory(v_stack_m50, v_rip - 1543, v_stack_m80, a4);
    if (sign_flag) goto loc_0072591C;
    if ((unsigned int)((unsigned int)(v_stack_m78)) != 0) goto loc_007254B6;
    goto loc_0072591C;
loc_007254B6:
    a2 = ((unsigned int)(v_stack_m78)) << (3);
    result = ExAllocatePool2(64, a2, (unsigned int)(0x61706E50ULL), a4);
    v_stack_m80 = result;
    if (result != 0) goto loc_007254E0;
loc_007254D6:
    goto loc_0072591C;
loc_007254E0:
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrEnumeratePersistedMemory(v_stack_m50, v_rip - 1643, v_stack_m80, a4);
    if (sign_flag) goto loc_0072591C;
    v_stack_mA8 = 0;
    v_stack_mA0 = 0;
loc_0072551B:
    if (0 >= v_stack_m78) goto loc_0072585B;
    v_r15 = 0;
    if (v_stack_mB7 != 0) goto loc_00725874;
    a4 = 0;
    a3 = 0;
    v_stack_mC8 = v_stack_mB0;
    v_stack_mA8 = *(unsigned __int64 *)(v_stack_m80 + 0 * 8);
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrQueryMetadata(v_stack_m50, *(unsigned __int64 *)(v_stack_m80 + 0 * 8), a3, a4);
    result = ExAllocatePool2(v_r15 + 64, (unsigned int)(v_stack_mB0), (unsigned int)(0x61706E50ULL), a4);
    if (result == 0) goto loc_007254D6;
    v_stack_mC8 = v_stack_mB0;
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrQueryMetadata(v_stack_m50, *(unsigned __int64 *)(v_stack_m80 + 0 * 8), result, (unsigned int)(v_stack_mB0));
    if (sign_flag) goto loc_007258FD;
    if (v_stack_mB0 < 2) goto loc_00725851;
    if (((unsigned __int16)(*(unsigned __int16 *)(result))) != 2) goto loc_00725608;
    v_stack_mC0 = v_stack_mB8;
    v_stack_mC8 = 0;
    result = PipMatchPersistentMemory(a2, v_stack_m68, v_stack_m70, result);
    if (sign_flag) goto loc_007258FD;
    v_stack_mB7 = (unsigned __int8)(v_stack_mB8);
    if ((unsigned __int8)(v_stack_mB8) == 0) goto loc_0072563F;
    a2 = 0;
    result = PipUnpackMetadata(result, a2, v_stack_m60, v_stack_mB8);
    goto loc_0072563A;
loc_00725608:
    if (((unsigned __int16)(result)) != 1) goto loc_00725851;
    a3 = 0;
    result = PipMatchPersistentMemoryV1(0, result, a3, v_stack_mB8);
    if (sign_flag) goto loc_007258FD;
    v_stack_mB7 = (unsigned __int8)(v_stack_mB8);
loc_0072563A:
    if ((unsigned __int8)(v_stack_mB8) != 0) goto loc_0072565C;
loc_0072563F:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_mA0)) + 1);
    v_stack_mA0 = (unsigned int)(v_rbx);
    result = ExFreePoolWithTag(result, (unsigned int)(0x61706E50ULL), a3, v_stack_mB8);
    v_r15 = 0;
    goto loc_0072551B;
loc_0072565C:
    v_stack_mC0 = v_stack_mB4;
    a4 = 0;
    a3 = 0;
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrClaimPersistedMemory(v_stack_m50, v_stack_mA8, a3, a4);
    v_rbx = 0;
    if (((unsigned int)(result)) != 0xC0000023ULL) { v_rbx = (unsigned int)(result); }
    if (sign_flag) goto loc_007258FD;
    a2 = ((unsigned int)(v_stack_mB4)) << (3);
    result = ExAllocatePool2(64, a2, (unsigned int)(0x61706E50ULL), a4);
    if (result != 0) goto loc_007256C1;
    goto loc_007258FD;
loc_007256C1:
    v_stack_mC0 = v_stack_mB4;
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrClaimPersistedMemory(v_stack_m50, v_stack_mA8, result, (unsigned int)(v_stack_mB4));
    if (sign_flag) goto loc_007258FD;
    if ((unsigned int)((unsigned int)(v_stack_mB4)) == 0) goto loc_0072571B;
loc_00725704:
    result = (*(unsigned __int64 *)(result)) >> (40);
    v_r12 = (unsigned int)((0) + ((unsigned int)(result)));
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_mB4)))) - (1);
    if (condition_is_not_equal) goto loc_00725704;
loc_0072571B:
    result = ExAllocatePool2(64, v_r12 * 8 + 48, (unsigned int)(0x61706E50ULL), (unsigned int)(v_stack_mB4));
    if (result == 0) goto loc_007258FD;
    v_rbx = 0;
    v_r12 = (unsigned int)((v_r12) << (12));
    *(unsigned __int64 *)(result) = 0;
    *(unsigned __int16 *)(result + 10) = 2;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) >> (12));
    result = (unsigned __int16)((result) + (6));
    *(unsigned __int64 *)(result + 32) = 0;
    result = (unsigned __int16)((result) << (3));
    *(unsigned __int16 *)(result + 8) = (unsigned __int16)(result);
    *(unsigned int *)(result + 44) = 0;
    *(unsigned int *)(result + 40) = (unsigned int)(v_r12);
    if ((unsigned int)((unsigned int)(v_stack_mB4)) == 0) goto loc_007257BB;
loc_0072577F:
    a1 = (*(unsigned __int64 *)(result + 0 * 8)) >> (40);
    result = (*(unsigned __int64 *)(result + 0 * 8)) & (v_r10);
    if ((unsigned int)(a1) == 0) goto loc_007257B3;
loc_007257A0:
    *(unsigned __int64 *)(result + 48) = result;
    a4 = (result + 48) + (8);
    result = (result) + (v_rbx + 1);
    a3 = ((unsigned int)((unsigned int)(a1))) - (v_rbx + 1);
    if (condition_is_not_equal) goto loc_007257A0;
loc_007257B3:
    a2 = (unsigned int)((0) + ((unsigned int)(v_rbx + 1)));
    if (((unsigned int)(a2)) < ((unsigned int)((unsigned int)(v_stack_mB4)))) goto loc_0072577F;
loc_007257BB:
    v_stack_mC0 = 0x40000010ULL;
    a4 = 0;
    v_stack_mC8 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(result, a2, (unsigned int)((unsigned int)(v_rbx + 1)), a4);
    if (result != 0) goto loc_007257E9;
    goto loc_007258EB;
loc_007257E9:
    if (v_stack_m90 == 0) goto loc_00725848;
    *(unsigned __int64 *)(v_stack_m98) = *(unsigned __int64 *)(result);
    if ((*(unsigned __int64 *)(v_stack_m98)) < (*(unsigned __int64 *)(result))) goto loc_0072584B;
    result = memcpy(v_stack_m90, result + 8, *(unsigned __int64 *)(result), v_stack_m90);
    if (((v_stack_p48) & ((unsigned __int8)(v_rbx + 1))) == 0) goto loc_0072585B;
    result = MmUnmapLockedPages(result, result, *(unsigned __int64 *)(result), v_stack_m90);
    result = ext_ms_win_ntos_ksr_l1_1_5_dll_KsrFreePersistedMemoryBlock(v_stack_m50, v_stack_mA8, (unsigned __int8)(v_rbx + 1), v_stack_m90);
    goto loc_0072585F;
loc_00725848:
    *(unsigned __int64 *)(v_stack_m50) = result;
loc_0072584B:
    goto loc_00725863;
loc_00725851:
    goto loc_007258FD;
loc_0072585B:
loc_0072585F:
loc_00725863:
    if (v_stack_mB7 != 0) goto loc_00725878;
    goto loc_007258D6;
loc_00725874:
loc_00725878:
    if (v_stack_m88 == 0) goto loc_007258D4;
    result = ExAllocatePool2(56 + 8, 56, (unsigned int)(0x61706E50ULL), v_stack_m90);
    if (result != 0) goto loc_007258A3;
    goto loc_007258D6;
loc_007258A3:
    v_rsi = -(v_stack_m58);
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) + 1);
    *(unsigned int *)(result) = (unsigned int)(result);
    *(unsigned __int64 *)(result + 48) = 0;
    v_r15 = 0;
    *(unsigned __int64 *)(result + 40) = (unsigned int)(0xC000009AULL);
    v_r12 = 0;
    *(unsigned __int64 *)(result + 8) = result;
    v_r14 = 0;
    *(unsigned __int64 *)(result + 32) = (unsigned int)(0xC000009AULL);
    *(unsigned __int64 *)(v_stack_m88) = result;
loc_007258D4:
    v_rbx = 0;
loc_007258D6:
    if (0 == 0) goto loc_007258F8;
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = MmUnmapLockedPages(a1, a2, (unsigned int)(0x61706E50ULL), v_stack_m90);
    }
    result = ExFreePoolWithTag(0, (unsigned int)(0x61706E50ULL), (unsigned int)(0x61706E50ULL), v_stack_m90);
loc_007258F8:
    if (0 != 0) {
        a2 = 0x61706E50ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x61706E50ULL), v_stack_m90);
    }
    if (result != 0) {
        a2 = 0x61706E50ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0x61706E50ULL), v_stack_m90);
    }
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x61706E50ULL), v_stack_m90);
    v_rsp = (v_rsp) + (176);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipGetPersistentMemory(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m3F;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint8_t v_stack_mB7;
    uint8_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p20;
    uint8_t v_stack_p48;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x6E548D)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m60 = Arg5;
    local_r15 = 0;
    v_stack_m98 = Arg6;
    v_stack_m58 = Arg2;
    v_stack_m90 = Arg7;
    v_stack_m70 = Arg4;
    v_stack_m68 = Arg3;
    v_stack_m88 = Arg8;
    v_stack_mB4 = 0;
    v_stack_m50 = v_xmm0;
    if (Arg2 == 0) goto loc_0072543A;
    if (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) == 0) goto loc_00725320;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) + 0x18C)) & (0x20000ULL)) == 0) goto loc_0072543A;
loc_00725320:
    result = IoAddTriageDumpDataBlock(Arg2, *(uint16_t *)(Arg2 + 0x2), Arg3, Arg4);
    if (*(uint64_t *)(Arg2 + 0x8) == 0) goto loc_0072536B;
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
    if (*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) == 0) goto loc_00725421;
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
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x138) + 0x28) + 0x10) == 0) goto loc_00725421;
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
    v_stack_mC8 = 0;
    result = KeBugCheckEx(202, 2, Arg2, Arg4);
loc_0072543A:
    v_stack_mB0 = 0;
    v_stack_mB7 = 0;
    v_stack_mB8 = 0;
    if (2 == 0) goto loc_00725466;
    if (((v_stack_p48) & (1)) == 0) goto loc_00725466;
    goto loc_0072591C;
loc_00725466:
    result = PipGetDriverKsrGuid(202, v_stack_m50, Arg2, Arg4);
    if (sign_flag) goto loc_0072591C;
    v_stack_m80 = v_xmm0;
    result = kernel_indirect_call(v_stack_m50, v_rip - 1543, v_stack_m80, Arg4);
    if (sign_flag) goto loc_0072591C;
    if ((uint32_t)((uint32_t)(v_stack_m78)) != 0) goto loc_007254B6;
    goto loc_0072591C;
loc_007254B6:
    Arg2 = ((uint32_t)(v_stack_m78)) << (3);
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x61706E50ULL), Arg4);
    v_stack_m80 = result;
    if (result != 0) goto loc_007254E0;
loc_007254D6:
    goto loc_0072591C;
loc_007254E0:
    result = kernel_indirect_call(v_stack_m50, v_rip - 1643, v_stack_m80, Arg4);
    if (sign_flag) goto loc_0072591C;
    v_stack_mA8 = 0;
    v_stack_mA0 = 0;
loc_0072551B:
    if (0 >= v_stack_m78) goto loc_0072585B;
    local_r15 = 0;
    if (v_stack_mB7 != 0) goto loc_00725874;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_mC8 = v_stack_mB0;
    v_stack_mA8 = *(uint64_t *)(v_stack_m80 + 0x0 * 8);
    result = kernel_indirect_call(v_stack_m50, *(uint64_t *)(v_stack_m80 + 0x0 * 8), Arg3, Arg4);
    result = ExAllocatePool2(local_r15 + 64, (uint32_t)(v_stack_mB0), (uint32_t)(0x61706E50ULL), Arg4);
    if (result == 0) goto loc_007254D6;
    v_stack_mC8 = v_stack_mB0;
    result = kernel_indirect_call(v_stack_m50, *(uint64_t *)(v_stack_m80 + 0x0 * 8), result, (uint32_t)(v_stack_mB0));
    if (sign_flag) goto loc_007258FD;
    if (v_stack_mB0 < 2) goto loc_00725851;
    if (((uint16_t)(*(uint16_t *)(result))) != 2) goto loc_00725608;
    v_stack_mC0 = v_stack_mB8;
    v_stack_mC8 = 0;
    result = PipMatchPersistentMemory(Arg2, v_stack_m68, v_stack_m70, result);
    if (sign_flag) goto loc_007258FD;
    v_stack_mB7 = (uint8_t)(v_stack_mB8);
    if ((uint8_t)(v_stack_mB8) == 0) goto loc_0072563F;
    Arg2 = 0;
    result = PipUnpackMetadata(result, Arg2, v_stack_m60, v_stack_mB8);
    goto loc_0072563A;
loc_00725608:
    if (((uint16_t)(result)) != 1) goto loc_00725851;
    Arg3 = 0;
    result = PipMatchPersistentMemoryV1(0, result, Arg3, v_stack_mB8);
    if (sign_flag) goto loc_007258FD;
    v_stack_mB7 = (uint8_t)(v_stack_mB8);
loc_0072563A:
    if ((uint8_t)(v_stack_mB8) != 0) goto loc_0072565C;
loc_0072563F:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_mA0)) + 1);
    v_stack_mA0 = (uint32_t)(local_rbx);
    result = ExFreePoolWithTag(result, (uint32_t)(0x61706E50ULL), Arg3, v_stack_mB8);
    local_r15 = 0;
    goto loc_0072551B;
loc_0072565C:
    v_stack_mC0 = v_stack_mB4;
    Arg4 = 0;
    Arg3 = 0;
    result = kernel_indirect_call(v_stack_m50, v_stack_mA8, Arg3, Arg4);
    local_rbx = 0;
    if (((uint32_t)(result)) != 0xC0000023ULL) { local_rbx = (uint32_t)(result); }
    if (sign_flag) goto loc_007258FD;
    Arg2 = ((uint32_t)(v_stack_mB4)) << (3);
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x61706E50ULL), Arg4);
    if (result != 0) goto loc_007256C1;
    goto loc_007258FD;
loc_007256C1:
    v_stack_mC0 = v_stack_mB4;
    result = kernel_indirect_call(v_stack_m50, v_stack_mA8, result, (uint32_t)(v_stack_mB4));
    if (sign_flag) goto loc_007258FD;
    if ((uint32_t)((uint32_t)(v_stack_mB4)) == 0) goto loc_0072571B;
loc_00725704:
    result = (*(uint64_t *)(result)) >> (40);
    local_r12 = (uint32_t)((0) + ((uint32_t)(result)));
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_mB4)))) - (1);
    if (condition_is_not_equal) goto loc_00725704;
loc_0072571B:
    result = ExAllocatePool2(64, local_r12 * 8 + 48, (uint32_t)(0x61706E50ULL), (uint32_t)(v_stack_mB4));
    if (result == 0) goto loc_007258FD;
    local_rbx = 0;
    local_r12 = (uint32_t)((local_r12) << (12));
    *(uint64_t *)(result) = 0;
    *(uint16_t *)(result + 0xA) = 2;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) >> (12));
    result = (uint16_t)((result) + (6));
    *(uint64_t *)(result + 0x20) = 0;
    result = (uint16_t)((result) << (3));
    *(uint16_t *)(result + 0x8) = (uint16_t)(result);
    *(uint32_t *)(result + 0x2C) = 0;
    *(uint32_t *)(result + 0x28) = (uint32_t)(local_r12);
    if ((uint32_t)((uint32_t)(v_stack_mB4)) == 0) goto loc_007257BB;
loc_0072577F:
    Arg1 = (*(uint64_t *)(result + 0x0 * 8)) >> (40);
    result = (*(uint64_t *)(result + 0x0 * 8)) & (local_r10);
    if ((uint32_t)(Arg1) == 0) goto loc_007257B3;
loc_007257A0:
    *(uint64_t *)(result + 0x30) = result;
    Arg4 = (result + 48) + (8);
    result = (result) + (local_rbx + 1);
    Arg3 = ((uint32_t)((uint32_t)(Arg1))) - (local_rbx + 1);
    if (condition_is_not_equal) goto loc_007257A0;
loc_007257B3:
    Arg2 = (uint32_t)((0) + ((uint32_t)(local_rbx + 1)));
    if (((uint32_t)(Arg2)) < ((uint32_t)((uint32_t)(v_stack_mB4)))) goto loc_0072577F;
loc_007257BB:
    v_stack_mC0 = 0x40000010ULL;
    Arg4 = 0;
    v_stack_mC8 = 0;
    Arg2 = 0;
    result = MmMapLockedPagesSpecifyCache(result, Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), Arg4);
    if (result != 0) goto loc_007257E9;
    goto loc_007258EB;
loc_007257E9:
    if (v_stack_m90 == 0) goto loc_00725848;
    *(uint64_t *)(v_stack_m98) = *(uint64_t *)(result);
    if ((*(uint64_t *)(v_stack_m98)) < (*(uint64_t *)(result))) goto loc_0072584B;
    result = memcpy(v_stack_m90, result + 8, *(uint64_t *)(result), v_stack_m90);
    if (((v_stack_p48) & ((uint8_t)(local_rbx + 1))) == 0) goto loc_0072585B;
    result = MmUnmapLockedPages(result, result, *(uint64_t *)(result), v_stack_m90);
    result = kernel_indirect_call(v_stack_m50, v_stack_mA8, (uint8_t)(local_rbx + 1), v_stack_m90);
    goto loc_0072585F;
loc_00725848:
    *(uint64_t *)(v_stack_m50) = result;
loc_0072584B:
    goto loc_00725863;
loc_00725851:
    goto loc_007258FD;
loc_0072585B:
loc_0072585F:
loc_00725863:
    if (v_stack_mB7 != 0) goto loc_00725878;
    goto loc_007258D6;
loc_00725874:
loc_00725878:
    if (v_stack_m88 == 0) goto loc_007258D4;
    result = ExAllocatePool2(56 + 8, 56, (uint32_t)(0x61706E50ULL), v_stack_m90);
    if (result != 0) goto loc_007258A3;
    goto loc_007258D6;
loc_007258A3:
    local_rsi = -(v_stack_m58);
    *(uint64_t *)(result + 0x10) = v_xmm0;
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) + 1);
    *(uint32_t *)(result) = (uint32_t)(result);
    *(uint64_t *)(result + 0x30) = 0;
    local_r15 = 0;
    *(uint64_t *)(result + 0x28) = (uint32_t)(0xC000009AULL);
    local_r12 = 0;
    *(uint64_t *)(result + 0x8) = result;
    local_r14 = 0;
    *(uint64_t *)(result + 0x20) = (uint32_t)(0xC000009AULL);
    *(uint64_t *)(v_stack_m88) = result;
loc_007258D4:
    local_rbx = 0;
loc_007258D6:
    if (0 == 0) goto loc_007258F8;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = MmUnmapLockedPages(Arg1, Arg2, (uint32_t)(0x61706E50ULL), v_stack_m90);
    }
    result = ExFreePoolWithTag(0, (uint32_t)(0x61706E50ULL), (uint32_t)(0x61706E50ULL), v_stack_m90);
loc_007258F8:
    if (0 != 0) {
        Arg2 = 0x61706E50ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x61706E50ULL), v_stack_m90);
    }
    if (result != 0) {
        Arg2 = 0x61706E50ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0x61706E50ULL), v_stack_m90);
    }
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x61706E50ULL), v_stack_m90);
    local_rsp = (local_rsp) + (176);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00725290&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
