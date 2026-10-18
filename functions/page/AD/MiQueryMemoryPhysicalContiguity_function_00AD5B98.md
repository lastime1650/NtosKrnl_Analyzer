# MiQueryMemoryPhysicalContiguity

- RVA: `0x00AD5B98`–`0x00AD60D3` (길이 `1,339` bytes)
- VA: `0x0000000140AD5B98`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BEE88`
- 디코드: `334`개 명령, `1,339/1,339` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00AD5C2C` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00AD5CDE` → [MiGetLargestPageIndex](../../text/49/MiGetLargestPageIndex_function_0049F730.md) (function, `0x0049F730`)
- `0x00AD5D9A` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00AD5DCB` → [MmSizeOfMdl](../../text/46/MmSizeOfMdl_function_00460A10.md) (function, `0x00460A10`)
- `0x00AD5DDE` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00AD5E51` → [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) (function, `0x0023B990`)
- `0x00AD5E7C` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x00AD5EAD` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00AD5F06` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)
- `0x00AD5F29` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (function, `0x00316690`)
- `0x00AD5F9F` → [MiQueryVaPhysicalContiguity](../../text/68/MiQueryVaPhysicalContiguity_function_006875B8.md) (function, `0x006875B8`)
- `0x00AD5FE5` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)
- `0x00AD6002` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00AD602D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AD6052` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AD6075` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (function, `0x002AEF10`)
- `0x00AD608A` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00AD609E` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x00AD60A8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AD60BA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MmQueryVirtualMemory](../9D/MmQueryVirtualMemory_function_009D9280.md) at `0x009D9657`

### Static image references
- `0x00AD5BAB` → RVA `0x00E0A740` (`.data`; read)
- `0x00AD5CF7` → RVA `0x00011C60` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **18**
  - `0x00AD5CDE` → [MiGetLargestPageIndex](../../text/49/MiGetLargestPageIndex_function_0049F730.md) (`PAGE` → `.text`)
  - `0x00AD5DCB` → [MmSizeOfMdl](../../text/46/MmSizeOfMdl_function_00460A10.md) (`PAGE` → `.text`)
  - `0x00AD5DDE` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00AD5E51` → [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) (`PAGE` → `.text`)
  - `0x00AD5E7C` → [MmMapLockedPagesSpecifyCache](../../text/31/MmMapLockedPagesSpecifyCache_function_00318800.md) (`PAGE` → `.text`)
  - `0x00AD5EAD` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00AD5F06` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (`PAGE` → `.text`)
  - `0x00AD5F29` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (`PAGE` → `.text`)
  - `0x00AD5F9F` → [MiQueryVaPhysicalContiguity](../../text/68/MiQueryVaPhysicalContiguity_function_006875B8.md) (`PAGE` → `.text`)
  - `0x00AD5FE5` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (`PAGE` → `.text`)
  - `0x00AD6002` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00AD602D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AD6052` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AD6075` → [MiUnlockAndDereferenceVadShared](../../text/2A/MiUnlockAndDereferenceVadShared_function_002AEF10.md) (`PAGE` → `.text`)
  - `0x00AD608A` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00AD609E` → [MmUnlockPages](../../text/29/MmUnlockPages_function_0029EEE0.md) (`PAGE` → `.text`)
  - `0x00AD60A8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AD60BA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AD5B98  40 53                           push rbx
00AD5B9A  56                              push rsi
00AD5B9B  57                              push rdi
00AD5B9C  41 54                           push r12
00AD5B9E  41 55                           push r13
00AD5BA0  41 56                           push r14
00AD5BA2  41 57                           push r15
00AD5BA4  48 81 EC 00 01 00 00            sub rsp, 0x100
00AD5BAB  48 8B 05 8E 4B 33 00            mov rax, qword ptr [rip + 0x334b8e]
00AD5BB2  48 33 C4                        xor rax, rsp
00AD5BB5  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00AD5BBD  44 88 4C 24 30                  mov byte ptr [rsp + 0x30], r9b
00AD5BC2  48 8B DA                        mov rbx, rdx
00AD5BC5  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
00AD5BCA  33 FF                           xor edi, edi
00AD5BCC  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00AD5BD0  0F 57 C0                        xorps xmm0, xmm0
00AD5BD3  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
00AD5BDB  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
00AD5BE3  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
00AD5BEB  44 8B F7                        mov r14d, edi
00AD5BEE  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00AD5BF3  8B F7                           mov esi, edi
00AD5BF5  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AD5BFA  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
00AD5BFE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AD5C07  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AD5C0C  8D 57 28                        lea edx, [rdi + 0x28]
00AD5C0F  4C 3B C2                        cmp r8, rdx
00AD5C12  74 0A                           je 0x140ad5c1e
00AD5C14  BB 04 00 00 C0                  mov ebx, 0xc0000004
00AD5C19  E9 4F 04 00 00                  jmp 0x140ad606d
00AD5C1E  45 84 C9                        test r9b, r9b
00AD5C21  74 42                           je 0x140ad5c65
00AD5C23  41 B8 08 00 00 00               mov r8d, 8
00AD5C29  48 8B CB                        mov rcx, rbx
00AD5C2C  E8 8F 35 E1 FF                  call 0x1408e91c0
00AD5C31  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AD5C34  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00AD5C39  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
00AD5C3D  0F 11 4C 24 78                  movups xmmword ptr [rsp + 0x78], xmm1
00AD5C42  F2 0F 10 43 20                  movsd xmm0, qword ptr [rbx + 0x20]
00AD5C47  F2 0F 11 84 24 88 00 00 00      movsd qword ptr [rsp + 0x88], xmm0
00AD5C50  44 8A 4C 24 30                  mov r9b, byte ptr [rsp + 0x30]
00AD5C55  EB 2D                           jmp 0x140ad5c84
00AD5C57  8B D8                           mov ebx, eax
00AD5C59  33 FF                           xor edi, edi
00AD5C5B  44 8B F7                        mov r14d, edi
00AD5C5E  8B F7                           mov esi, edi
00AD5C60  E9 08 04 00 00                  jmp 0x140ad606d
00AD5C65  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AD5C68  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00AD5C6D  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
00AD5C71  0F 11 4C 24 78                  movups xmmword ptr [rsp + 0x78], xmm1
00AD5C76  F2 0F 10 43 20                  movsd xmm0, qword ptr [rbx + 0x20]
00AD5C7B  F2 0F 11 84 24 88 00 00 00      movsd qword ptr [rsp + 0x88], xmm0
00AD5C84  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
00AD5C8B  F7 C2 FE FF FF FF               test edx, 0xfffffffe
00AD5C91  0F 85 D1 03 00 00               jne 0x140ad6068
00AD5C97  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
00AD5CA1  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00AD5CA6  4C 3B E0                        cmp r12, rax
00AD5CA9  0F 87 B9 03 00 00               ja 0x140ad6068
00AD5CAF  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00AD5CB4  48 85 DB                        test rbx, rbx
00AD5CB7  74 0E                           je 0x140ad5cc7
00AD5CB9  48 8D 43 FF                     lea rax, [rbx - 1]
00AD5CBD  48 85 C3                        test rbx, rax
00AD5CC0  B8 01 00 00 00                  mov eax, 1
00AD5CC5  74 02                           je 0x140ad5cc9
00AD5CC7  8B C7                           mov eax, edi
00AD5CC9  85 C0                           test eax, eax
00AD5CCB  0F 84 97 03 00 00               je 0x140ad6068
00AD5CD1  48 81 FB 00 10 00 00            cmp rbx, 0x1000
00AD5CD8  0F 86 8A 03 00 00               jbe 0x140ad6068
00AD5CDE  E8 4D 9A 9C FF                  call 0x14049f730
00AD5CE3  44 8B C0                        mov r8d, eax
00AD5CE6  44 89 44 24 40                  mov dword ptr [rsp + 0x40], r8d
00AD5CEB  83 F8 03                        cmp eax, 3
00AD5CEE  73 30                           jae 0x140ad5d20
00AD5CF0  48 8B D3                        mov rdx, rbx
00AD5CF3  48 C1 EA 0C                     shr rdx, 0xc
00AD5CF7  48 8D 0D 62 BF 53 FF            lea rcx, [rip - 0xac409e]
00AD5CFE  4A 8D 0C C1                     lea rcx, [rcx + r8*8]
00AD5D02  48 39 11                        cmp qword ptr [rcx], rdx
00AD5D05  74 0D                           je 0x140ad5d14
00AD5D07  41 FF C0                        inc r8d
00AD5D0A  48 83 C1 08                     add rcx, 8
00AD5D0E  41 83 F8 03                     cmp r8d, 3
00AD5D12  72 EE                           jb 0x140ad5d02
00AD5D14  44 89 44 24 40                  mov dword ptr [rsp + 0x40], r8d
00AD5D19  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
00AD5D20  41 83 F8 03                     cmp r8d, 3
00AD5D24  75 0A                           jne 0x140ad5d30
00AD5D26  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00AD5D2B  E9 3D 03 00 00                  jmp 0x140ad606d
00AD5D30  48 8D 43 FF                     lea rax, [rbx - 1]
00AD5D34  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00AD5D39  48 85 C1                        test rcx, rax
00AD5D3C  0F 85 26 03 00 00               jne 0x140ad6068
00AD5D42  48 F7 D0                        not rax
00AD5D45  49 23 C4                        and rax, r12
00AD5D48  49 3B C4                        cmp rax, r12
00AD5D4B  0F 85 17 03 00 00               jne 0x140ad6068
00AD5D51  83 E2 01                        and edx, 1
00AD5D54  03 D2                           add edx, edx
00AD5D56  89 54 24 58                     mov dword ptr [rsp + 0x58], edx
00AD5D5A  33 D2                           xor edx, edx
00AD5D5C  48 8B C1                        mov rax, rcx
00AD5D5F  48 F7 F3                        div rbx
00AD5D62  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00AD5D6A  4C 8D 2C 85 00 00 00 00         lea r13, [rax*4]
00AD5D72  49 83 FD 20                     cmp r13, 0x20
00AD5D76  77 3A                           ja 0x140ad5db2
00AD5D78  4C 8D BC 24 D0 00 00 00         lea r15, [rsp + 0xd0]
00AD5D80  45 84 C9                        test r9b, r9b
00AD5D83  0F 84 04 01 00 00               je 0x140ad5e8d
00AD5D89  41 B8 04 00 00 00               mov r8d, 4
00AD5D8F  49 8B D5                        mov rdx, r13
00AD5D92  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AD5D9A  E8 21 34 E1 FF                  call 0x1408e91c0
00AD5D9F  E9 E9 00 00 00                  jmp 0x140ad5e8d
00AD5DA4  8B D8                           mov ebx, eax
00AD5DA6  33 FF                           xor edi, edi
00AD5DA8  44 8B F7                        mov r14d, edi
00AD5DAB  8B F7                           mov esi, edi
00AD5DAD  E9 BB 02 00 00                  jmp 0x140ad606d
00AD5DB2  B8 00 F0 FF FF                  mov eax, 0xfffff000
00AD5DB7  4C 3B E8                        cmp r13, rax
00AD5DBA  0F 87 A8 02 00 00               ja 0x140ad6068
00AD5DC0  49 8B D5                        mov rdx, r13
00AD5DC3  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AD5DCB  E8 40 AC 98 FF                  call 0x140460a10
00AD5DD0  48 8B D0                        mov rdx, rax
00AD5DD3  B9 40 00 00 00                  mov ecx, 0x40
00AD5DD8  41 B8 4D 6D 20 20               mov r8d, 0x20206d4d
00AD5DDE  E8 5D 57 88 FF                  call 0x14035b540
00AD5DE3  4C 8B F0                        mov r14, rax
00AD5DE6  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AD5DEB  48 85 C0                        test rax, rax
00AD5DEE  75 0A                           jne 0x140ad5dfa
00AD5DF0  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AD5DF5  E9 73 02 00 00                  jmp 0x140ad606d
00AD5DFA  48 89 38                        mov qword ptr [rax], rdi
00AD5DFD  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00AD5E05  44 8B C2                        mov r8d, edx
00AD5E08  41 8B C8                        mov ecx, r8d
00AD5E0B  41 B9 FF 0F 00 00               mov r9d, 0xfff
00AD5E11  49 23 C9                        and rcx, r9
00AD5E14  49 03 C9                        add rcx, r9
00AD5E17  49 03 CD                        add rcx, r13
00AD5E1A  48 C1 E9 0C                     shr rcx, 0xc
00AD5E1E  66 83 C1 06                     add cx, 6
00AD5E22  66 C1 E1 03                     shl cx, 3
00AD5E26  66 89 48 08                     mov word ptr [rax + 8], cx
00AD5E2A  66 89 78 0A                     mov word ptr [rax + 0xa], di
00AD5E2E  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
00AD5E35  48 89 50 20                     mov qword ptr [rax + 0x20], rdx
00AD5E39  45 23 C1                        and r8d, r9d
00AD5E3C  44 89 40 2C                     mov dword ptr [rax + 0x2c], r8d
00AD5E40  44 89 68 28                     mov dword ptr [rax + 0x28], r13d
00AD5E44  41 B8 01 00 00 00               mov r8d, 1
00AD5E4A  8A 54 24 30                     mov dl, byte ptr [rsp + 0x30]
00AD5E4E  49 8B CE                        mov rcx, r14
00AD5E51  E8 3A 5B 76 FF                  call 0x14023b990
00AD5E56  90                              nop
00AD5E57  41 F6 46 0A 05                  test byte ptr [r14 + 0xa], 5
00AD5E5C  74 06                           je 0x140ad5e64
00AD5E5E  4D 8B 7E 18                     mov r15, qword ptr [r14 + 0x18]
00AD5E62  EB 20                           jmp 0x140ad5e84
00AD5E64  C7 44 24 28 10 00 00 40         mov dword ptr [rsp + 0x28], 0x40000010
00AD5E6C  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00AD5E70  45 33 C9                        xor r9d, r9d
00AD5E73  33 D2                           xor edx, edx
00AD5E75  45 8D 41 01                     lea r8d, [r9 + 1]
00AD5E79  49 8B CE                        mov rcx, r14
00AD5E7C  E8 7F 29 84 FF                  call 0x140318800
00AD5E81  4C 8B F8                        mov r15, rax
00AD5E84  4D 85 FF                        test r15, r15
00AD5E87  0F 84 63 FF FF FF               je 0x140ad5df0
00AD5E8D  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00AD5E92  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AD5E97  48 39 81 B8 00 00 00            cmp qword ptr [rcx + 0xb8], rax
00AD5E9E  74 1A                           je 0x140ad5eba
00AD5EA0  4C 8D 84 24 A0 00 00 00         lea r8, [rsp + 0xa0]
00AD5EA8  33 D2                           xor edx, edx
00AD5EAA  48 8B C8                        mov rcx, rax
00AD5EAD  E8 6E 09 74 FF                  call 0x140216820
00AD5EB2  C7 44 24 34 01 00 00 00         mov dword ptr [rsp + 0x34], 1
00AD5EBA  49 C1 EC 0C                     shr r12, 0xc
00AD5EBE  48 C1 EB 0C                     shr rbx, 0xc
00AD5EC2  4C 8B C7                        mov r8, rdi
00AD5EC5  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
00AD5ECA  4C 3B 84 24 90 00 00 00         cmp r8, qword ptr [rsp + 0x90]
00AD5ED2  0F 83 05 01 00 00               jae 0x140ad5fdd
00AD5ED8  48 85 F6                        test rsi, rsi
00AD5EDB  74 3B                           je 0x140ad5f18
00AD5EDD  0F B6 56 20                     movzx edx, byte ptr [rsi + 0x20]
00AD5EE1  48 C1 E2 20                     shl rdx, 0x20
00AD5EE5  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
00AD5EE8  48 0B D0                        or rdx, rax
00AD5EEB  4C 3B E2                        cmp r12, rdx
00AD5EEE  72 13                           jb 0x140ad5f03
00AD5EF0  0F B6 56 21                     movzx edx, byte ptr [rsi + 0x21]
00AD5EF4  48 C1 E2 20                     shl rdx, 0x20
00AD5EF8  8B 46 1C                        mov eax, dword ptr [rsi + 0x1c]
00AD5EFB  48 0B D0                        or rdx, rax
00AD5EFE  4C 3B E2                        cmp r12, rdx
00AD5F01  76 10                           jbe 0x140ad5f13
00AD5F03  48 8B CE                        mov rcx, rsi
00AD5F06  E8 05 90 7D FF                  call 0x1402aef10
00AD5F0B  48 8B F7                        mov rsi, rdi
00AD5F0E  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AD5F13  48 85 F6                        test rsi, rsi
00AD5F16  75 27                           jne 0x140ad5f3f
00AD5F18  49 8B CC                        mov rcx, r12
00AD5F1B  48 C1 E1 0C                     shl rcx, 0xc
00AD5F1F  4C 8D 44 24 44                  lea r8, [rsp + 0x44]
00AD5F24  BA 02 00 00 00                  mov edx, 2
00AD5F29  E8 62 07 84 FF                  call 0x140316690
00AD5F2E  48 8B F0                        mov rsi, rax
00AD5F31  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AD5F36  48 85 C0                        test rax, rax
00AD5F39  0F 84 8B 00 00 00               je 0x140ad5fca
00AD5F3F  4A 8D 14 23                     lea rdx, [rbx + r12]
00AD5F43  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
00AD5F4B  0F B6 4E 21                     movzx ecx, byte ptr [rsi + 0x21]
00AD5F4F  48 C1 E1 20                     shl rcx, 0x20
00AD5F53  8B 46 1C                        mov eax, dword ptr [rsi + 0x1c]
00AD5F56  48 0B C8                        or rcx, rax
00AD5F59  48 8D 42 FF                     lea rax, [rdx - 1]
00AD5F5D  48 3B C1                        cmp rax, rcx
00AD5F60  77 71                           ja 0x140ad5fd3
00AD5F62  8B 46 30                        mov eax, dword ptr [rsi + 0x30]
00AD5F65  A8 70                           test al, 0x70
00AD5F67  0F 94 C1                        sete cl
00AD5F6A  0F BA E0 15                     bt eax, 0x15
00AD5F6E  0F 92 C0                        setb al
00AD5F71  84 C8                           test al, cl
00AD5F73  0F 84 AD FD FF FF               je 0x140ad5d26
00AD5F79  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00AD5F7E  41 89 3C 87                     mov dword ptr [r15 + rax*4], edi
00AD5F82  49 C1 E4 0C                     shl r12, 0xc
00AD5F86  44 8B 4C 24 58                  mov r9d, dword ptr [rsp + 0x58]
00AD5F8B  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
00AD5F90  49 8B D4                        mov rdx, r12
00AD5F93  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00AD5F98  48 81 C1 00 04 00 00            add rcx, 0x400
00AD5F9F  E8 14 16 BB FF                  call 0x1406875b8
00AD5FA4  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
00AD5FA9  43 8B 0C 87                     mov ecx, dword ptr [r15 + r8*4]
00AD5FAD  8B D1                           mov edx, ecx
00AD5FAF  33 D0                           xor edx, eax
00AD5FB1  83 E2 03                        and edx, 3
00AD5FB4  33 D1                           xor edx, ecx
00AD5FB6  43 89 14 87                     mov dword ptr [r15 + r8*4], edx
00AD5FBA  49 FF C0                        inc r8
00AD5FBD  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
00AD5FC5  E9 FB FE FF FF                  jmp 0x140ad5ec5
00AD5FCA  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
00AD5FCE  E9 A7 00 00 00                  jmp 0x140ad607a
00AD5FD3  BB 18 00 00 C0                  mov ebx, 0xc0000018
00AD5FD8  E9 90 00 00 00                  jmp 0x140ad606d
00AD5FDD  48 85 F6                        test rsi, rsi
00AD5FE0  74 10                           je 0x140ad5ff2
00AD5FE2  48 8B CE                        mov rcx, rsi
00AD5FE5  E8 26 8F 7D FF                  call 0x1402aef10
00AD5FEA  48 8B F7                        mov rsi, rdi
00AD5FED  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AD5FF2  39 7C 24 34                     cmp dword ptr [rsp + 0x34], edi
00AD5FF6  74 13                           je 0x140ad600b
00AD5FF8  33 D2                           xor edx, edx
00AD5FFA  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
00AD6002  E8 29 1D 74 FF                  call 0x140217d30
00AD6007  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
00AD600B  48 8D 84 24 D0 00 00 00         lea rax, [rsp + 0xd0]
00AD6013  4C 3B F8                        cmp r15, rax
00AD6016  75 3F                           jne 0x140ad6057
00AD6018  40 38 7C 24 30                  cmp byte ptr [rsp + 0x30], dil
00AD601D  74 25                           je 0x140ad6044
00AD601F  4D 8B C5                        mov r8, r13
00AD6022  49 8B D7                        mov rdx, r15
00AD6025  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AD602D  E8 0E 08 BF FF                  call 0x1406c6840
00AD6032  EB 23                           jmp 0x140ad6057
00AD6034  8B D8                           mov ebx, eax
00AD6036  33 FF                           xor edi, edi
00AD6038  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00AD603D  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00AD6042  EB 29                           jmp 0x140ad606d
00AD6044  4D 8B C5                        mov r8, r13
00AD6047  49 8B D7                        mov rdx, r15
00AD604A  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AD6052  E8 E9 07 BF FF                  call 0x1406c6840
00AD6057  8B DF                           mov ebx, edi
00AD6059  EB 12                           jmp 0x140ad606d
00AD605B  8B D8                           mov ebx, eax
00AD605D  33 FF                           xor edi, edi
00AD605F  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00AD6064  8B F7                           mov esi, edi
00AD6066  EB 05                           jmp 0x140ad606d
00AD6068  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AD606D  48 85 F6                        test rsi, rsi
00AD6070  74 08                           je 0x140ad607a
00AD6072  48 8B CE                        mov rcx, rsi
00AD6075  E8 96 8E 7D FF                  call 0x1402aef10
00AD607A  39 7C 24 34                     cmp dword ptr [rsp + 0x34], edi
00AD607E  74 0F                           je 0x140ad608f
00AD6080  33 D2                           xor edx, edx
00AD6082  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
00AD608A  E8 A1 1C 74 FF                  call 0x140217d30
00AD608F  4D 85 F6                        test r14, r14
00AD6092  74 19                           je 0x140ad60ad
00AD6094  41 F6 46 0A 02                  test byte ptr [r14 + 0xa], 2
00AD6099  74 08                           je 0x140ad60a3
00AD609B  49 8B CE                        mov rcx, r14
00AD609E  E8 3D 8E 7C FF                  call 0x14029eee0
00AD60A3  33 D2                           xor edx, edx
00AD60A5  49 8B CE                        mov rcx, r14
00AD60A8  E8 C3 C7 0A 00                  call 0x140b82870
00AD60AD  8B C3                           mov eax, ebx
00AD60AF  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00AD60B7  48 33 CC                        xor rcx, rsp
00AD60BA  E8 81 65 BD FF                  call 0x1406ac640
00AD60BF  48 81 C4 00 01 00 00            add rsp, 0x100
00AD60C6  41 5F                           pop r15
00AD60C8  41 5E                           pop r14
00AD60CA  41 5D                           pop r13
00AD60CC  41 5C                           pop r12
00AD60CE  5F                              pop rdi
00AD60CF  5E                              pop rsi
00AD60D0  5B                              pop rbx
00AD60D1  C3                              ret
00AD60D2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiQueryMemoryPhysicalContiguity(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned __int8 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;

    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 3361678)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m108 = a4;
    v_stack_mD8 = a1;
    v_rdi = 0;
    v_stack_mF4 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    v_stack_mF0 = 0;
    v_stack_m100 = 0;
    v_stack_m104 = 0;
    v_stack_mE8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (a3 == (v_rdi + 40)) goto loc_00AD5C1E;
    goto loc_00AD606D;
loc_00AD5C1E:
    if (a4 == 0) goto loc_00AD5C65;
    result = ProbeForWrite((unsigned int)(0xC0000004ULL), v_rdi + 40, 8, a4);
    v_stack_mD0 = v_xmm0;
    v_stack_mC0 = v_xmm1;
    v_stack_mB0 = v_xmm0;
    goto loc_00AD5C84;
loc_00AD5C65:
    v_stack_mD0 = v_xmm0;
    v_stack_mC0 = v_xmm1;
    v_stack_mB0 = v_xmm0;
loc_00AD5C84:
    if ((((unsigned int)((unsigned int)(v_stack_mB8))) & (0xFFFFFFFEULL)) != 0) goto loc_00AD6068;
    if (v_stack_mD0 > result) goto loc_00AD6068;
    if (v_stack_mC0 == 0) goto loc_00AD5CC7;
    result = 1;
    if (((v_stack_mC0) & (v_stack_mC0 - 1)) != 0) {
        result = 0;
    }
    if ((unsigned int)(result) == 0) goto loc_00AD6068;
    if (v_stack_mC0 <= 0x1000ULL) goto loc_00AD6068;
    result = MiGetLargestPageIndex((unsigned int)(0xC0000004ULL), (unsigned int)(v_stack_mB8), 8, v_stack_m108);
    v_stack_mF8 = (unsigned int)((unsigned int)((unsigned int)(result)));
    if (((unsigned int)(result)) >= 3) goto loc_00AD5D20;
    a2 = (v_stack_mC0) >> (12);
loc_00AD5D02:
    if ((*(unsigned __int64 *)(v_rip - 11288734 + (unsigned int)((unsigned int)(result)) * 8)) == a2) goto loc_00AD5D14;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) + 1);
    a1 = (v_rip - 11288734 + (unsigned int)((unsigned int)(result)) * 8) + (8);
    if (((unsigned int)(a3)) < 3) goto loc_00AD5D02;
loc_00AD5D14:
    v_stack_mF8 = (unsigned int)(a3);
loc_00AD5D20:
    if (((unsigned int)(a3)) != 3) goto loc_00AD5D30;
loc_00AD5D26:
    goto loc_00AD606D;
loc_00AD5D30:
    if (((v_stack_mC8) & ((unsigned int)(0xC00000BBULL) - 1)) != 0) goto loc_00AD6068;
    result = ~((unsigned int)(0xC00000BBULL) - 1);
    result = (result) & (v_stack_mD0);
    if (result != v_stack_mD0) goto loc_00AD6068;
    a2 = (unsigned int)(((unsigned int)(v_stack_mB8)) & (1));
    a2 = (unsigned int)((a2) + ((unsigned int)(a2)));
    v_stack_mE0 = (unsigned int)(a2);
    a2 = 0;
    v_stack_mA8 = v_stack_mC8;
    if ((v_stack_mC8 * 4) > 32) goto loc_00AD5DB2;
    if ((unsigned __int8)(v_stack_m108) == 0) goto loc_00AD5E8D;
    result = ProbeForWrite(v_stack_mB0, v_stack_mC8 * 4, 4, v_stack_m108);
    goto loc_00AD5E8D;
loc_00AD5DB2:
    if ((v_stack_mC8 * 4) > ((unsigned int)(0xFFFFF000ULL))) goto loc_00AD6068;
    result = MmSizeOfMdl(v_stack_mB0, v_stack_mC8 * 4, 4, v_stack_m108);
    result = MiAllocatePool(64, result, (unsigned int)(0x20206D4DULL), v_stack_m108);
    v_stack_mF0 = result;
    if (result != 0) goto loc_00AD5DFA;
loc_00AD5DF0:
    goto loc_00AD606D;
loc_00AD5DFA:
    *(unsigned __int64 *)(result) = 0;
    a1 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mB0))))) & ((unsigned int)(0xFFFULL));
    a1 = (a1) + ((unsigned int)(0xFFFULL));
    a1 = (a1) + (v_stack_mC8 * 4);
    a1 = (a1) >> (12);
    a1 = (unsigned __int16)((a1) + (6));
    a1 = (unsigned __int16)((a1) << (3));
    *(unsigned __int16 *)(result + 8) = (unsigned __int16)(a1);
    *(unsigned __int16 *)(result + 10) = 0;
    a2 = (v_stack_mB0) & (0xFFFFFFFFFFFFF000ULL);
    *(unsigned __int64 *)(result + 32) = a2;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mB0))) & ((unsigned int)((unsigned int)(0xFFFULL))));
    *(unsigned int *)(result + 44) = (unsigned int)(a3);
    *(unsigned int *)(result + 40) = (unsigned int)(v_stack_mC8 * 4);
    result = MmProbeAndLockPages(result, v_stack_m108, 1, (unsigned int)(0xFFFULL));
    if (((*(unsigned __int8 *)(result + 10)) & (5)) == 0) goto loc_00AD5E64;
    goto loc_00AD5E84;
loc_00AD5E64:
    v_stack_m110 = 0x40000010ULL;
    v_stack_m118 = 0;
    a4 = 0;
    a2 = 0;
    result = MmMapLockedPagesSpecifyCache(result, a2, a4 + 1, a4);
loc_00AD5E84:
    if (result == 0) goto loc_00AD5DF0;
loc_00AD5E8D:
    result = v_stack_mD8;
    if ((*(unsigned __int64 *)(v_stack_mE8 + 184)) != v_stack_mD8) {
        a3 = v_stack_m98;
        a2 = 0;
        a1 = v_stack_mD8;
        result = KiStackAttachProcess(a1, a2, a3, a4);
        v_stack_m104 = 1;
    }
    v_r12 = (v_stack_mD0) >> (12);
    v_rbx = ((unsigned int)(0xC000009AULL)) >> (12);
loc_00AD5EC5:
    v_stack_mE8 = 0;
    if (0 >= v_stack_mA8) goto loc_00AD5FDD;
    if (0 == 0) goto loc_00AD5F18;
    a2 = (*(unsigned __int8 *)(0 + 32)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(0 + 24)));
    if (v_r12 < a2) goto loc_00AD5F03;
    a2 = (*(unsigned __int8 *)(0 + 33)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(0 + 28)));
    result = (unsigned int)(*(unsigned int *)(0 + 28));
    v_rsi = 0;
    if (v_r12 >= = a2) {
        a1 = 0;
        result = MiUnlockAndDereferenceVadShared(a1, a2, 0, a4);
        v_rsi = 0;
        v_stack_m100 = 0;
    }
    if (v_rsi != 0) goto loc_00AD5F3F;
loc_00AD5F18:
    a1 = (v_r12) << (12);
    result = MiObtainReferencedVadEx(a1, 2, v_stack_mF4, a4);
    v_stack_m100 = result;
    if (result == 0) goto loc_00AD5FCA;
loc_00AD5F3F:
    v_stack_mA0 = v_rbx + v_r12 * 1;
    a1 = (*(unsigned __int8 *)(result + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(result + 28)));
    if ((v_rbx + v_r12 * 1 - 1) > a1) goto loc_00AD5FD3;
    a1 = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 48)))) & (112)) == 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00AD5D26;
    *(unsigned int *)(result + v_stack_mE8 * 4) = 0;
    v_r12 = (v_r12) << (12);
    a1 = (v_stack_mD8) + (0x400ULL);
    result = MiQueryVaPhysicalContiguity(a1, v_r12, (unsigned int)(v_stack_mF8), (unsigned int)(v_stack_mE0));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + v_stack_mE8 * 4))))) ^ ((unsigned int)(result)));
    a2 = (unsigned int)((a2) & (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + v_stack_mE8 * 4)))));
    *(unsigned int *)(result + v_stack_mE8 * 4) = (unsigned int)(a2);
    a3 = (v_stack_mE8) + 1;
    goto loc_00AD5EC5;
loc_00AD5FCA:
    goto loc_00AD607A;
loc_00AD5FD3:
    goto loc_00AD606D;
loc_00AD5FDD:
    v_rsi = result;
    if (result != 0) {
        a1 = result;
        result = MiUnlockAndDereferenceVadShared(a1, a2, a3, (unsigned int)(v_stack_mE0));
        v_rsi = 0;
        v_stack_m100 = 0;
    }
    if (v_stack_m104 != 0) {
        a2 = 0;
        a1 = v_stack_m98;
        result = KiUnstackDetachProcess(a1, a2, a3, (unsigned int)(v_stack_mE0));
        v_stack_m104 = 0;
    }
    if (result != v_stack_m68) goto loc_00AD6057;
    if (v_stack_m108 == 0) goto loc_00AD6044;
    result = memcpy(v_stack_mB0, result, v_stack_mC8 * 4, (unsigned int)(v_stack_mE0));
    goto loc_00AD6057;
loc_00AD6044:
    result = memcpy(v_stack_mB0, result, v_stack_mC8 * 4, (unsigned int)(v_stack_mE0));
loc_00AD6057:
    goto loc_00AD606D;
loc_00AD6068:
loc_00AD606D:
    if (v_rsi != 0) {
        a1 = v_rsi;
        result = MiUnlockAndDereferenceVadShared(a1, result, v_stack_mC8 * 4, (unsigned int)(v_stack_mE0));
    }
    if (v_stack_m104 != 0) {
        a2 = 0;
        a1 = v_stack_m98;
        result = KiUnstackDetachProcess(a1, a2, v_stack_mC8 * 4, (unsigned int)(v_stack_mE0));
    }
    if (result == 0) goto loc_00AD60AD;
    if (((*(unsigned __int8 *)(result + 10)) & (2)) != 0) {
        a1 = result;
        result = MmUnlockPages(a1, a2, v_stack_mC8 * 4, (unsigned int)(v_stack_mE0));
    }
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_mC8 * 4, (unsigned int)(v_stack_mE0));
loc_00AD60AD:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_mC8 * 4, (unsigned int)(v_stack_mE0));
    v_rsp = (v_rsp) + (256);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiQueryMemoryPhysicalContiguity(int64_t Arg1, void *Arg2, int64_t Arg3, uint8_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m104;
    uint8_t v_stack_m108;
    uint32_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m48;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;

    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0x334B8E)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m108 = Arg4;
    v_stack_mD8 = Arg1;
    local_rdi = 0;
    v_stack_mF4 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    v_stack_mF0 = 0;
    v_stack_m100 = 0;
    v_stack_m104 = 0;
    v_stack_mE8 = *(uint64_t *)(gs_base + (0 + 0x188));
    if (Arg3 == (local_rdi + 40)) goto loc_00AD5C1E;
    goto loc_00AD606D;
loc_00AD5C1E:
    if (Arg4 == 0) goto loc_00AD5C65;
    result = ProbeForWrite((uint32_t)(0xC0000004ULL), local_rdi + 40, 8, Arg4);
    v_stack_mD0 = v_xmm0;
    v_stack_mC0 = v_xmm1;
    v_stack_mB0 = v_xmm0;
    goto loc_00AD5C84;
loc_00AD5C65:
    v_stack_mD0 = v_xmm0;
    v_stack_mC0 = v_xmm1;
    v_stack_mB0 = v_xmm0;
loc_00AD5C84:
    if ((((uint32_t)((uint32_t)(v_stack_mB8))) & (0xFFFFFFFEULL)) != 0) goto loc_00AD6068;
    if (v_stack_mD0 > result) goto loc_00AD6068;
    if (v_stack_mC0 == 0) goto loc_00AD5CC7;
    result = 1;
    if (((v_stack_mC0) & (v_stack_mC0 - 1)) != 0) {
        result = 0;
    }
    if ((uint32_t)(result) == 0) goto loc_00AD6068;
    if (v_stack_mC0 <= 0x1000ULL) goto loc_00AD6068;
    result = MiGetLargestPageIndex((uint32_t)(0xC0000004ULL), (uint32_t)(v_stack_mB8), 8, v_stack_m108);
    v_stack_mF8 = (uint32_t)((uint32_t)((uint32_t)(result)));
    if (((uint32_t)(result)) >= 3) goto loc_00AD5D20;
    Arg2 = (v_stack_mC0) >> (12);
loc_00AD5D02:
    if ((*(uint64_t *)(v_rip - 0xAC409E + (uint32_t)((uint32_t)(result)) * 8)) == Arg2) goto loc_00AD5D14;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result))) + 1);
    Arg1 = (v_rip - 11288734 + (uint32_t)((uint32_t)(result)) * 8) + (8);
    if (((uint32_t)(Arg3)) < 3) goto loc_00AD5D02;
loc_00AD5D14:
    v_stack_mF8 = (uint32_t)(Arg3);
loc_00AD5D20:
    if (((uint32_t)(Arg3)) != 3) goto loc_00AD5D30;
loc_00AD5D26:
    goto loc_00AD606D;
loc_00AD5D30:
    if (((v_stack_mC8) & ((uint32_t)(0xC00000BBULL) - 1)) != 0) goto loc_00AD6068;
    result = ~((uint32_t)(0xC00000BBULL) - 1);
    result = (result) & (v_stack_mD0);
    if (result != v_stack_mD0) goto loc_00AD6068;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mB8)) & (1));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg2)));
    v_stack_mE0 = (uint32_t)(Arg2);
    Arg2 = 0;
    v_stack_mA8 = v_stack_mC8;
    if ((v_stack_mC8 * 4) > 32) goto loc_00AD5DB2;
    if ((uint8_t)(v_stack_m108) == 0) goto loc_00AD5E8D;
    result = ProbeForWrite(v_stack_mB0, v_stack_mC8 * 4, 4, v_stack_m108);
    goto loc_00AD5E8D;
loc_00AD5DB2:
    if ((v_stack_mC8 * 4) > ((uint32_t)(0xFFFFF000ULL))) goto loc_00AD6068;
    result = MmSizeOfMdl(v_stack_mB0, v_stack_mC8 * 4, 4, v_stack_m108);
    result = MiAllocatePool(64, result, (uint32_t)(0x20206D4DULL), v_stack_m108);
    v_stack_mF0 = result;
    if (result != 0) goto loc_00AD5DFA;
loc_00AD5DF0:
    goto loc_00AD606D;
loc_00AD5DFA:
    *(uint64_t *)(result) = 0;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mB0))))) & ((uint32_t)(0xFFFULL));
    Arg1 = (Arg1) + ((uint32_t)(0xFFFULL));
    Arg1 = (Arg1) + (v_stack_mC8 * 4);
    Arg1 = (Arg1) >> (12);
    Arg1 = (uint16_t)((Arg1) + (6));
    Arg1 = (uint16_t)((Arg1) << (3));
    *(uint16_t *)(result + 0x8) = (uint16_t)(Arg1);
    *(uint16_t *)(result + 0xA) = 0;
    Arg2 = (v_stack_mB0) & (0xFFFFFFFFFFFFF000ULL);
    *(void **)(result + 0x20) = Arg2;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mB0))) & ((uint32_t)((uint32_t)(0xFFFULL))));
    *(uint32_t *)(result + 0x2C) = (uint32_t)(Arg3);
    *(uint32_t *)(result + 0x28) = (uint32_t)(v_stack_mC8 * 4);
    result = MmProbeAndLockPages(result, v_stack_m108, 1, (uint32_t)(0xFFFULL));
    if (((*(uint8_t *)(result + 0xA)) & (5)) == 0) goto loc_00AD5E64;
    goto loc_00AD5E84;
loc_00AD5E64:
    v_stack_m110 = 0x40000010ULL;
    v_stack_m118 = 0;
    Arg4 = 0;
    Arg2 = 0;
    result = MmMapLockedPagesSpecifyCache(result, Arg2, Arg4 + 1, Arg4);
loc_00AD5E84:
    if (result == 0) goto loc_00AD5DF0;
loc_00AD5E8D:
    result = v_stack_mD8;
    if ((*(uint64_t *)(v_stack_mE8 + 0xB8)) != v_stack_mD8) {
        Arg3 = v_stack_m98;
        Arg2 = 0;
        Arg1 = v_stack_mD8;
        result = KiStackAttachProcess(Arg1, Arg2, Arg3, Arg4);
        v_stack_m104 = 1;
    }
    local_r12 = (v_stack_mD0) >> (12);
    local_rbx = ((uint32_t)(0xC000009AULL)) >> (12);
loc_00AD5EC5:
    v_stack_mE8 = 0;
    if (0 >= v_stack_mA8) goto loc_00AD5FDD;
    if (0 == 0) goto loc_00AD5F18;
    Arg2 = (*(uint8_t *)(0 + 0x20)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(0 + 0x18)));
    if (local_r12 < Arg2) goto loc_00AD5F03;
    Arg2 = (*(uint8_t *)(0 + 0x21)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(0 + 0x1C)));
    result = (uint32_t)(*(uint32_t *)(0 + 0x1C));
    local_rsi = 0;
    if (local_r12 >= = Arg2) {
        Arg1 = 0;
        result = MiUnlockAndDereferenceVadShared(Arg1, Arg2, 0, Arg4);
        local_rsi = 0;
        v_stack_m100 = 0;
    }
    if (local_rsi != 0) goto loc_00AD5F3F;
loc_00AD5F18:
    Arg1 = (local_r12) << (12);
    result = MiObtainReferencedVadEx(Arg1, 2, v_stack_mF4, Arg4);
    v_stack_m100 = result;
    if (result == 0) goto loc_00AD5FCA;
loc_00AD5F3F:
    v_stack_mA0 = local_rbx + local_r12 * 1;
    Arg1 = (*(uint8_t *)(result + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    if ((local_rbx + local_r12 * 1 - 1) > Arg1) goto loc_00AD5FD3;
    Arg1 = ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x30)))) & (112)) == 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00AD5D26;
    *(uint32_t *)(result + v_stack_mE8 * 4) = 0;
    local_r12 = (local_r12) << (12);
    Arg1 = (v_stack_mD8) + (0x400ULL);
    result = MiQueryVaPhysicalContiguity(Arg1, local_r12, (uint32_t)(v_stack_mF8), (uint32_t)(v_stack_mE0));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + v_stack_mE8 * 4))))) ^ ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) & (3));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + v_stack_mE8 * 4)))));
    *(uint32_t *)(result + v_stack_mE8 * 4) = (uint32_t)(Arg2);
    Arg3 = (v_stack_mE8) + 1;
    goto loc_00AD5EC5;
loc_00AD5FCA:
    goto loc_00AD607A;
loc_00AD5FD3:
    goto loc_00AD606D;
loc_00AD5FDD:
    local_rsi = result;
    if (result != 0) {
        Arg1 = result;
        result = MiUnlockAndDereferenceVadShared(Arg1, Arg2, Arg3, (uint32_t)(v_stack_mE0));
        local_rsi = 0;
        v_stack_m100 = 0;
    }
    if (v_stack_m104 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m98;
        result = KiUnstackDetachProcess(Arg1, Arg2, Arg3, (uint32_t)(v_stack_mE0));
        v_stack_m104 = 0;
    }
    if (result != v_stack_m68) goto loc_00AD6057;
    if (v_stack_m108 == 0) goto loc_00AD6044;
    result = memcpy(v_stack_mB0, result, v_stack_mC8 * 4, (uint32_t)(v_stack_mE0));
    goto loc_00AD6057;
loc_00AD6044:
    result = memcpy(v_stack_mB0, result, v_stack_mC8 * 4, (uint32_t)(v_stack_mE0));
loc_00AD6057:
    goto loc_00AD606D;
loc_00AD6068:
loc_00AD606D:
    if (local_rsi != 0) {
        Arg1 = local_rsi;
        result = MiUnlockAndDereferenceVadShared(Arg1, result, v_stack_mC8 * 4, (uint32_t)(v_stack_mE0));
    }
    if (v_stack_m104 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m98;
        result = KiUnstackDetachProcess(Arg1, Arg2, v_stack_mC8 * 4, (uint32_t)(v_stack_mE0));
    }
    if (result == 0) goto loc_00AD60AD;
    if (((*(uint8_t *)(result + 0xA)) & (2)) != 0) {
        Arg1 = result;
        result = MmUnlockPages(Arg1, Arg2, v_stack_mC8 * 4, (uint32_t)(v_stack_mE0));
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_mC8 * 4, (uint32_t)(v_stack_mE0));
loc_00AD60AD:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_mC8 * 4, (uint32_t)(v_stack_mE0));
    local_rsp = (local_rsp) + (256);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x10` | `128` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AD5B98&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
