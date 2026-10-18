# NtCopyFileChunk

- RVA: `0x0094B600`–`0x0094BDB4` (길이 `1,972` bytes)
- VA: `0x000000014094B600`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000913C0`
- 디코드: `441`개 명령, `1,972/1,972` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0094B683` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (function, `0x004F4EC4`)
- `0x0094B73B` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x0094B802` → [IopXxxControlFile](../8E/IopXxxControlFile_function_008E9AD0.md) (function, `0x008E9AD0`)
- `0x0094B80C` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (function, `0x004F4EC4`)
- `0x0094B831` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x0094B85B` → [ObReferenceFileObjectForWrite](ObReferenceFileObjectForWrite_function_0094BDC0.md) (function, `0x0094BDC0`)
- `0x0094B871` → [IopFileObjectRevoked](../../text/41/IopFileObjectRevoked_function_004159D0.md) (function, `0x004159D0`)
- `0x0094B89A` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x0094B8BA` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x0094B8D2` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (function, `0x004F4EC4`)
- `0x0094B8ED` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0094B925` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0094B93A` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (function, `0x004F4EC4`)
- `0x0094B961` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0094B972` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (function, `0x004F4EC4`)
- `0x0094B9AF` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (function, `0x004F4EC4`)
- `0x0094B9CF` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x0094B9F5` → [ObReferenceFileObjectForWrite](ObReferenceFileObjectForWrite_function_0094BDC0.md) (function, `0x0094BDC0`)
- `0x0094BA07` → [IopFileObjectRevoked](../../text/41/IopFileObjectRevoked_function_004159D0.md) (function, `0x004159D0`)
- `0x0094BA9B` → [IopPopulateCopyWriteWorkerData](../../text/40/IopPopulateCopyWriteWorkerData_function_00400B48.md) (function, `0x00400B48`)
- `0x0094BB13` → [ZwCreateEvent](../../text/6A/ZwCreateEvent_function_006AD9D0.md) (function, `0x006AD9D0`)
- `0x0094BB50` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x0094BBB4` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x0094BBDA` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x0094BC1B` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0094BC81` → [IopReadFile](../8A/IopReadFile_function_008AEFF0.md) (function, `0x008AEFF0`)
- `0x0094BCB8` → [IopWaitForSynchronousIoEvent](../../text/43/IopWaitForSynchronousIoEvent_function_0043F0F0.md) (function, `0x0043F0F0`)
- `0x0094BCCE` → [IoIs32bitProcess](../../text/40/IoIs32bitProcess_function_0040DFE0.md) (function, `0x0040DFE0`)
- `0x0094BD05` → [IoIs32bitProcess](../../text/40/IoIs32bitProcess_function_0040DFE0.md) (function, `0x0040DFE0`)
- `0x0094BD27` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0094BD42` → [IopFreeCopyObjectsFromDataBuffer](../../text/4C/IopFreeCopyObjectsFromDataBuffer_function_004C201C.md) (function, `0x004C201C`)
- `0x0094BD47` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (function, `0x004F4EC4`)
- `0x0094BD5D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0094BD6F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0094BD84` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x0094BD91` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0094BB22` → RVA `0x00FC6B80` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **28**
  - `0x0094B683` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (`PAGE` → `.text`)
  - `0x0094B80C` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (`PAGE` → `.text`)
  - `0x0094B831` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (`PAGE` → `.text`)
  - `0x0094B871` → [IopFileObjectRevoked](../../text/41/IopFileObjectRevoked_function_004159D0.md) (`PAGE` → `.text`)
  - `0x0094B89A` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x0094B8BA` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x0094B8D2` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (`PAGE` → `.text`)
  - `0x0094B8ED` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0094B925` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0094B93A` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (`PAGE` → `.text`)
  - `0x0094B961` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0094B972` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (`PAGE` → `.text`)
  - `0x0094B9AF` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (`PAGE` → `.text`)
  - `0x0094B9CF` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (`PAGE` → `.text`)
  - `0x0094BA07` → [IopFileObjectRevoked](../../text/41/IopFileObjectRevoked_function_004159D0.md) (`PAGE` → `.text`)
  - `0x0094BA9B` → [IopPopulateCopyWriteWorkerData](../../text/40/IopPopulateCopyWriteWorkerData_function_00400B48.md) (`PAGE` → `.text`)
  - `0x0094BB13` → [ZwCreateEvent](../../text/6A/ZwCreateEvent_function_006AD9D0.md) (`PAGE` → `.text`)
  - `0x0094BBDA` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x0094BC1B` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x0094BCB8` → [IopWaitForSynchronousIoEvent](../../text/43/IopWaitForSynchronousIoEvent_function_0043F0F0.md) (`PAGE` → `.text`)
  - `0x0094BCCE` → [IoIs32bitProcess](../../text/40/IoIs32bitProcess_function_0040DFE0.md) (`PAGE` → `.text`)
  - `0x0094BD05` → [IoIs32bitProcess](../../text/40/IoIs32bitProcess_function_0040DFE0.md) (`PAGE` → `.text`)
  - `0x0094BD27` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x0094BD42` → [IopFreeCopyObjectsFromDataBuffer](../../text/4C/IopFreeCopyObjectsFromDataBuffer_function_004C201C.md) (`PAGE` → `.text`)
  - `0x0094BD47` → [Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline_function_004F4EC4.md) (`PAGE` → `.text`)
  - `0x0094BD5D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0094BD6F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0094BD91` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0094B600  48 8B C4                        mov rax, rsp
0094B603  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0094B607  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0094B60B  48 89 48 08                     mov qword ptr [rax + 8], rcx
0094B60F  53                              push rbx
0094B610  56                              push rsi
0094B611  57                              push rdi
0094B612  41 54                           push r12
0094B614  41 55                           push r13
0094B616  41 56                           push r14
0094B618  41 57                           push r15
0094B61A  48 81 EC 60 01 00 00            sub rsp, 0x160
0094B621  0F 29 70 B8                     movaps xmmword ptr [rax - 0x48], xmm6
0094B625  4D 8B E1                        mov r12, r9
0094B628  4C 8B F1                        mov r14, rcx
0094B62B  33 DB                           xor ebx, ebx
0094B62D  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
0094B631  0F 57 C0                        xorps xmm0, xmm0
0094B634  0F 11 80 50 FF FF FF            movups xmmword ptr [rax - 0xb0], xmm0
0094B63B  8B F3                           mov esi, ebx
0094B63D  48 89 98 10 FF FF FF            mov qword ptr [rax - 0xf0], rbx
0094B644  48 89 9C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rbx
0094B64C  48 83 88 18 FF FF FF FF         or qword ptr [rax - 0xe8], 0xffffffffffffffff
0094B654  44 8B FB                        mov r15d, ebx
0094B657  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
0094B65F  48 89 9C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rbx
0094B667  48 89 98 F8 FE FF FF            mov qword ptr [rax - 0x108], rbx
0094B66E  48 89 98 F0 FE FF FF            mov qword ptr [rax - 0x110], rbx
0094B675  48 89 9C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rbx
0094B67D  8B FB                           mov edi, ebx
0094B67F  89 7C 24 78                     mov dword ptr [rsp + 0x78], edi
0094B683  E8 3C 98 BA FF                  call 0x1404f4ec4
0094B688  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0094B691  44 8A A8 32 02 00 00            mov r13b, byte ptr [rax + 0x232]
0094B698  44 88 6C 24 74                  mov byte ptr [rsp + 0x74], r13b
0094B69D  F7 84 24 E8 01 00 00 FE FF FF FF  test dword ptr [rsp + 0x1e8], 0xfffffffe
0094B6A8  74 0A                           je 0x14094b6b4
0094B6AA  B8 0D 00 00 C0                  mov eax, 0xc000000d
0094B6AF  E9 E4 06 00 00                  jmp 0x14094bd98
0094B6B4  45 84 ED                        test r13b, r13b
0094B6B7  0F 84 94 00 00 00               je 0x14094b751
0094B6BD  48 8B 94 24 C8 01 00 00         mov rdx, qword ptr [rsp + 0x1c8]
0094B6C5  F6 C2 03                        test dl, 3
0094B6C8  75 71                           jne 0x14094b73b
0094B6CA  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
0094B6D4  48 8B C1                        mov rax, rcx
0094B6D7  48 3B D1                        cmp rdx, rcx
0094B6DA  48 0F 42 C2                     cmovb rax, rdx
0094B6DE  90                              nop
0094B6DF  8A 00                           mov al, byte ptr [rax]
0094B6E1  48 8B 02                        mov rax, qword ptr [rdx]
0094B6E4  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
0094B6EC  48 8B 94 24 D0 01 00 00         mov rdx, qword ptr [rsp + 0x1d0]
0094B6F4  F6 C2 03                        test dl, 3
0094B6F7  75 42                           jne 0x14094b73b
0094B6F9  48 8B C1                        mov rax, rcx
0094B6FC  48 3B D1                        cmp rdx, rcx
0094B6FF  48 0F 42 C2                     cmovb rax, rdx
0094B703  90                              nop
0094B704  8A 00                           mov al, byte ptr [rax]
0094B706  48 8B 02                        mov rax, qword ptr [rdx]
0094B709  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
0094B711  4C 3B E1                        cmp r12, rcx
0094B714  49 0F 42 CC                     cmovb rcx, r12
0094B718  8B 01                           mov eax, dword ptr [rcx]
0094B71A  89 01                           mov dword ptr [rcx], eax
0094B71C  41 0F 10 34 24                  movups xmm6, xmmword ptr [r12]
0094B721  0F 11 B4 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm6
0094B729  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
0094B731  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
0094B739  EB 49                           jmp 0x14094b784
0094B73B  E8 90 E8 F4 FF                  call 0x140899fd0
0094B740  90                              nop
0094B741  33 DB                           xor ebx, ebx
0094B743  8B 7C 24 70                     mov edi, dword ptr [rsp + 0x70]
0094B747  8B F3                           mov esi, ebx
0094B749  44 8B FB                        mov r15d, ebx
0094B74C  E9 E7 05 00 00                  jmp 0x14094bd38
0094B751  48 8B 8C 24 C8 01 00 00         mov rcx, qword ptr [rsp + 0x1c8]
0094B759  48 8B 09                        mov rcx, qword ptr [rcx]
0094B75C  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
0094B764  48 8B 84 24 D0 01 00 00         mov rax, qword ptr [rsp + 0x1d0]
0094B76C  48 8B 00                        mov rax, qword ptr [rax]
0094B76F  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
0094B777  41 0F 10 34 24                  movups xmm6, xmmword ptr [r12]
0094B77C  0F 11 B4 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm6
0094B784  F6 84 24 E8 01 00 00 01         test byte ptr [rsp + 0x1e8], 1
0094B78C  74 7E                           je 0x14094b80c
0094B78E  4C 89 B4 24 28 01 00 00         mov qword ptr [rsp + 0x128], r14
0094B796  48 89 8C 24 30 01 00 00         mov qword ptr [rsp + 0x130], rcx
0094B79E  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
0094B7A6  8B 84 24 C0 01 00 00            mov eax, dword ptr [rsp + 0x1c0]
0094B7AD  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
0094B7B5  C7 44 24 58 01 00 00 00         mov dword ptr [rsp + 0x58], 1
0094B7BD  88 5C 24 50                     mov byte ptr [rsp + 0x50], bl
0094B7C1  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
0094B7C5  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
0094B7CA  C7 44 24 38 20 00 00 00         mov dword ptr [rsp + 0x38], 0x20
0094B7D2  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
0094B7DA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0094B7DF  C7 44 24 28 44 83 09 00         mov dword ptr [rsp + 0x28], 0x98344
0094B7E7  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0094B7EC  45 33 C9                        xor r9d, r9d
0094B7EF  45 33 C0                        xor r8d, r8d
0094B7F2  48 8B 94 24 B0 01 00 00         mov rdx, qword ptr [rsp + 0x1b0]
0094B7FA  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
0094B802  E8 C9 E2 F9 FF                  call 0x1408e9ad0
0094B807  E9 8C 05 00 00                  jmp 0x14094bd98
0094B80C  E8 B3 96 BA FF                  call 0x1404f4ec4
0094B811  85 C0                           test eax, eax
0094B813  0F 84 B1 00 00 00               je 0x14094b8ca
0094B819  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0094B81E  4C 8D 8C 24 90 00 00 00         lea r9, [rsp + 0x90]
0094B826  45 8A C5                        mov r8b, r13b
0094B829  BA 01 00 00 00                  mov edx, 1
0094B82E  49 8B CE                        mov rcx, r14
0094B831  E8 FA 1C 95 FF                  call 0x14029d530
0094B836  8B F8                           mov edi, eax
0094B838  85 C0                           test eax, eax
0094B83A  0F 88 F8 04 00 00               js 0x14094bd38
0094B840  4C 8D 8C 24 A8 00 00 00         lea r9, [rsp + 0xa8]
0094B848  4C 8D 84 24 88 00 00 00         lea r8, [rsp + 0x88]
0094B850  41 8A D5                        mov dl, r13b
0094B853  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
0094B85B  E8 60 05 00 00                  call 0x14094bdc0
0094B860  8B F8                           mov edi, eax
0094B862  44 8B F0                        mov r14d, eax
0094B865  85 C0                           test eax, eax
0094B867  78 19                           js 0x14094b882
0094B869  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0094B871  E8 5A A1 AC FF                  call 0x1404159d0
0094B876  84 C0                           test al, al
0094B878  74 08                           je 0x14094b882
0094B87A  BF 10 09 00 C0                  mov edi, 0xc0000910
0094B87F  44 8B F7                        mov r14d, edi
0094B882  45 85 F6                        test r14d, r14d
0094B885  0F 88 AD 04 00 00               js 0x14094bd38
0094B88B  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0094B893  8B 41 50                        mov eax, dword ptr [rcx + 0x50]
0094B896  A8 08                           test al, 8
0094B898  74 0D                           je 0x14094b8a7
0094B89A  E8 81 F8 94 FF                  call 0x14029b120
0094B89F  8B B8 98 00 00 00               mov edi, dword ptr [rax + 0x98]
0094B8A5  EB 04                           jmp 0x14094b8ab
0094B8A7  8B 7C 24 78                     mov edi, dword ptr [rsp + 0x78]
0094B8AB  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0094B8B3  8B 41 50                        mov eax, dword ptr [rcx + 0x50]
0094B8B6  A8 08                           test al, 8
0094B8B8  74 10                           je 0x14094b8ca
0094B8BA  E8 61 F8 94 FF                  call 0x14029b120
0094B8BF  8B 88 98 00 00 00               mov ecx, dword ptr [rax + 0x98]
0094B8C5  3B F9                           cmp edi, ecx
0094B8C7  0F 46 F9                        cmovbe edi, ecx
0094B8CA  44 8B B4 24 C0 01 00 00         mov r14d, dword ptr [rsp + 0x1c0]
0094B8D2  E8 ED 95 BA FF                  call 0x1404f4ec4
0094B8D7  49 8D 56 50                     lea rdx, [r14 + 0x50]
0094B8DB  41 B8 49 6F 43 70               mov r8d, 0x70436f49
0094B8E1  85 C0                           test eax, eax
0094B8E3  74 3B                           je 0x14094b920
0094B8E5  48 03 D7                        add rdx, rdi
0094B8E8  B9 4B 00 00 00                  mov ecx, 0x4b
0094B8ED  E8 FE 67 23 00                  call 0x140b820f0
0094B8F2  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
0094B8FA  48 85 C0                        test rax, rax
0094B8FD  75 0A                           jne 0x14094b909
0094B8FF  BF 9A 00 00 C0                  mov edi, 0xc000009a
0094B904  E9 2F 04 00 00                  jmp 0x14094bd38
0094B909  48 8D 70 50                     lea rsi, [rax + 0x50]
0094B90D  48 03 F7                        add rsi, rdi
0094B910  48 F7 D7                        not rdi
0094B913  48 23 F7                        and rsi, rdi
0094B916  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
0094B91E  EB 1A                           jmp 0x14094b93a
0094B920  B9 43 00 00 00                  mov ecx, 0x43
0094B925  E8 C6 67 23 00                  call 0x140b820f0
0094B92A  48 8B F0                        mov rsi, rax
0094B92D  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0094B935  48 85 C0                        test rax, rax
0094B938  74 C5                           je 0x14094b8ff
0094B93A  E8 85 95 BA FF                  call 0x1404f4ec4
0094B93F  85 C0                           test eax, eax
0094B941  74 06                           je 0x14094b949
0094B943  4C 8D 76 B0                     lea r14, [rsi - 0x50]
0094B947  EB 0F                           jmp 0x14094b958
0094B949  4C 8B F6                        mov r14, rsi
0094B94C  48 83 C6 50                     add rsi, 0x50
0094B950  48 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], rsi
0094B958  33 D2                           xor edx, edx
0094B95A  44 8D 42 50                     lea r8d, [rdx + 0x50]
0094B95E  49 8B CE                        mov rcx, r14
0094B961  E8 DA B2 D7 FF                  call 0x1406c6c40
0094B966  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
0094B96E  49 89 46 40                     mov qword ptr [r14 + 0x40], rax
0094B972  E8 4D 95 BA FF                  call 0x1404f4ec4
0094B977  85 C0                           test eax, eax
0094B979  74 34                           je 0x14094b9af
0094B97B  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0094B983  49 89 46 38                     mov qword ptr [r14 + 0x38], rax
0094B987  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0094B98F  49 89 46 30                     mov qword ptr [r14 + 0x30], rax
0094B993  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
0094B99B  49 89 46 48                     mov qword ptr [r14 + 0x48], rax
0094B99F  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
0094B9A7  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
0094B9AF  E8 10 95 BA FF                  call 0x1404f4ec4
0094B9B4  85 C0                           test eax, eax
0094B9B6  75 6E                           jne 0x14094ba26
0094B9B8  4D 8D 4E 38                     lea r9, [r14 + 0x38]
0094B9BC  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0094B9C1  45 8A C5                        mov r8b, r13b
0094B9C4  8D 50 01                        lea edx, [rax + 1]
0094B9C7  48 8B 8C 24 A0 01 00 00         mov rcx, qword ptr [rsp + 0x1a0]
0094B9CF  E8 5C 1B 95 FF                  call 0x14029d530
0094B9D4  8B F8                           mov edi, eax
0094B9D6  85 C0                           test eax, eax
0094B9D8  0F 88 5A 03 00 00               js 0x14094bd38
0094B9DE  4D 8D 46 30                     lea r8, [r14 + 0x30]
0094B9E2  4C 8D 8C 24 A8 00 00 00         lea r9, [rsp + 0xa8]
0094B9EA  41 8A D5                        mov dl, r13b
0094B9ED  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
0094B9F5  E8 C6 03 00 00                  call 0x14094bdc0
0094B9FA  8B F8                           mov edi, eax
0094B9FC  44 8B E8                        mov r13d, eax
0094B9FF  85 C0                           test eax, eax
0094BA01  78 15                           js 0x14094ba18
0094BA03  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
0094BA07  E8 C4 9F AC FF                  call 0x1404159d0
0094BA0C  84 C0                           test al, al
0094BA0E  74 08                           je 0x14094ba18
0094BA10  BF 10 09 00 C0                  mov edi, 0xc0000910
0094BA15  44 8B EF                        mov r13d, edi
0094BA18  45 85 ED                        test r13d, r13d
0094BA1B  0F 88 17 03 00 00               js 0x14094bd38
0094BA21  44 8A 6C 24 74                  mov r13b, byte ptr [rsp + 0x74]
0094BA26  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
0094BA2A  8B 51 50                        mov edx, dword ptr [rcx + 0x50]
0094BA2D  8B C2                           mov eax, edx
0094BA2F  83 E0 02                        and eax, 2
0094BA32  89 84 24 E8 01 00 00            mov dword ptr [rsp + 0x1e8], eax
0094BA39  C1 EA 02                        shr edx, 2
0094BA3C  80 E2 01                        and dl, 1
0094BA3F  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
0094BA43  4D 8D 4E 20                     lea r9, [r14 + 0x20]
0094BA47  4C 8B C3                        mov r8, rbx
0094BA4A  85 C0                           test eax, eax
0094BA4C  4C 0F 44 84 24 B0 01 00 00      cmove r8, qword ptr [rsp + 0x1b0]
0094BA55  49 8D 56 38                     lea rdx, [r14 + 0x38]
0094BA59  4C 89 4C 24 50                  mov qword ptr [rsp + 0x50], r9
0094BA5E  8B 84 24 AC 00 00 00            mov eax, dword ptr [rsp + 0xac]
0094BA65  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0094BA69  48 8B 84 24 E0 01 00 00         mov rax, qword ptr [rsp + 0x1e0]
0094BA71  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0094BA76  48 8B 84 24 D0 01 00 00         mov rax, qword ptr [rsp + 0x1d0]
0094BA7E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0094BA83  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
0094BA88  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
0094BA8D  44 8B 8C 24 C0 01 00 00         mov r9d, dword ptr [rsp + 0x1c0]
0094BA95  4C 8B C6                        mov r8, rsi
0094BA98  49 8B D4                        mov rdx, r12
0094BA9B  E8 A8 50 AB FF                  call 0x140400b48
0094BAA0  8B F8                           mov edi, eax
0094BAA2  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
0094BAA6  85 C0                           test eax, eax
0094BAA8  79 09                           jns 0x14094bab3
0094BAAA  49 89 5E 30                     mov qword ptr [r14 + 0x30], rbx
0094BAAE  E9 85 02 00 00                  jmp 0x14094bd38
0094BAB3  39 9C 24 E8 01 00 00            cmp dword ptr [rsp + 0x1e8], ebx
0094BABA  0F 84 2B 01 00 00               je 0x14094bbeb
0094BAC0  48 C7 84 24 F8 00 00 00 30 00 00 00  mov qword ptr [rsp + 0xf8], 0x30
0094BACC  48 C7 84 24 10 01 00 00 00 02 00 00  mov qword ptr [rsp + 0x110], 0x200
0094BAD8  48 89 9C 24 00 01 00 00         mov qword ptr [rsp + 0x100], rbx
0094BAE0  48 89 9C 24 08 01 00 00         mov qword ptr [rsp + 0x108], rbx
0094BAE8  0F 57 C0                        xorps xmm0, xmm0
0094BAEB  F3 0F 7F 84 24 18 01 00 00      movdqu xmmword ptr [rsp + 0x118], xmm0
0094BAF4  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
0094BAF8  41 B9 01 00 00 00               mov r9d, 1
0094BAFE  4C 8D 84 24 F8 00 00 00         lea r8, [rsp + 0xf8]
0094BB06  BA 03 00 1F 00                  mov edx, 0x1f0003
0094BB0B  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
0094BB13  E8 B8 1E D6 FF                  call 0x1406ad9d0
0094BB18  8B F8                           mov edi, eax
0094BB1A  85 C0                           test eax, eax
0094BB1C  0F 88 16 02 00 00               js 0x14094bd38
0094BB22  4C 8B 05 57 B0 67 00            mov r8, qword ptr [rip + 0x67b057]
0094BB29  48 89 9C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rbx
0094BB31  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0094BB36  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
0094BB3E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0094BB43  45 33 C9                        xor r9d, r9d
0094BB46  33 D2                           xor edx, edx
0094BB48  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0094BB50  E8 5B D2 F1 FF                  call 0x140868db0
0094BB55  8B F8                           mov edi, eax
0094BB57  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
0094BB5F  48 89 8C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rcx
0094BB67  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
0094BB6B  85 C0                           test eax, eax
0094BB6D  0F 88 C5 01 00 00               js 0x14094bd38
0094BB73  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
0094BB77  48 89 48 50                     mov qword ptr [rax + 0x50], rcx
0094BB7B  48 8B 84 24 B0 01 00 00         mov rax, qword ptr [rsp + 0x1b0]
0094BB83  48 85 C0                        test rax, rax
0094BB86  74 57                           je 0x14094bbdf
0094BB88  4C 8B 05 F1 AF 67 00            mov r8, qword ptr [rip + 0x67aff1]
0094BB8F  48 89 9C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rbx
0094BB97  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0094BB9C  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
0094BBA4  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0094BBA9  45 8A CD                        mov r9b, r13b
0094BBAC  BA 02 00 00 00                  mov edx, 2
0094BBB1  48 8B C8                        mov rcx, rax
0094BBB4  E8 F7 D1 F1 FF                  call 0x140868db0
0094BBB9  8B F8                           mov edi, eax
0094BBBB  4C 8B BC 24 D0 00 00 00         mov r15, qword ptr [rsp + 0xd0]
0094BBC3  4C 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r15
0094BBCB  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
0094BBCF  85 C0                           test eax, eax
0094BBD1  0F 88 61 01 00 00               js 0x14094bd38
0094BBD7  49 8B CF                        mov rcx, r15
0094BBDA  E8 71 C7 8F FF                  call 0x140248350
0094BBDF  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
0094BBE3  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
0094BBEB  45 84 ED                        test r13b, r13b
0094BBEE  74 21                           je 0x14094bc11
0094BBF0  F3 41 0F 7F 34 24               movdqu xmmword ptr [r12], xmm6
0094BBF6  EB 1F                           jmp 0x14094bc17
0094BBF8  8B 7C 24 70                     mov edi, dword ptr [rsp + 0x70]
0094BBFC  48 8B B4 24 80 00 00 00         mov rsi, qword ptr [rsp + 0x80]
0094BC04  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
0094BC0C  E9 27 01 00 00                  jmp 0x14094bd38
0094BC11  F3 41 0F 7F 34 24               movdqu xmmword ptr [r12], xmm6
0094BC17  49 8B 4E 38                     mov rcx, qword ptr [r14 + 0x38]
0094BC1B  E8 00 3E 8C FF                  call 0x14020fa20
0094BC20  49 8D 46 38                     lea rax, [r14 + 0x38]
0094BC24  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0094BC29  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
0094BC2E  C7 44 24 58 00 00 00 40         mov dword ptr [rsp + 0x58], 0x40000000
0094BC36  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
0094BC3B  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
0094BC40  48 8B 84 24 D8 01 00 00         mov rax, qword ptr [rsp + 0x1d8]
0094BC48  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0094BC4D  48 8B 84 24 C8 01 00 00         mov rax, qword ptr [rsp + 0x1c8]
0094BC55  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0094BC5A  8B 84 24 C0 01 00 00            mov eax, dword ptr [rsp + 0x1c0]
0094BC61  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0094BC65  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0094BC6A  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0094BC6F  45 33 C9                        xor r9d, r9d
0094BC72  45 33 C0                        xor r8d, r8d
0094BC75  48 8B 94 24 B0 01 00 00         mov rdx, qword ptr [rsp + 0x1b0]
0094BC7D  49 8B 4E 38                     mov rcx, qword ptr [r14 + 0x38]
0094BC81  E8 6A 33 F6 FF                  call 0x1408aeff0
0094BC86  8B F8                           mov edi, eax
0094BC88  48 8B F3                        mov rsi, rbx
0094BC8B  85 C0                           test eax, eax
0094BC8D  0F 88 9B 00 00 00               js 0x14094bd2e
0094BC93  39 9C 24 E8 01 00 00            cmp dword ptr [rsp + 0x1e8], ebx
0094BC9A  0F 84 8E 00 00 00               je 0x14094bd2e
0094BCA0  4C 8B 8C 24 D8 00 00 00         mov r9, qword ptr [rsp + 0xd8]
0094BCA8  44 8A 44 24 78                  mov r8b, byte ptr [rsp + 0x78]
0094BCAD  41 8A D5                        mov dl, r13b
0094BCB0  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
0094BCB8  E8 33 34 AF FF                  call 0x14043f0f0
0094BCBD  8B F8                           mov edi, eax
0094BCBF  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
0094BCC3  85 C0                           test eax, eax
0094BCC5  78 53                           js 0x14094bd1a
0094BCC7  45 84 ED                        test r13b, r13b
0094BCCA  74 37                           je 0x14094bd03
0094BCCC  33 C9                           xor ecx, ecx
0094BCCE  E8 0D 23 AC FF                  call 0x14040dfe0
0094BCD3  84 C0                           test al, al
0094BCD5  74 0C                           je 0x14094bce3
0094BCD7  41 8B 04 24                     mov eax, dword ptr [r12]
0094BCDB  8B 08                           mov ecx, dword ptr [rax]
0094BCDD  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
0094BCE1  EB 08                           jmp 0x14094bceb
0094BCE3  41 8B 04 24                     mov eax, dword ptr [r12]
0094BCE7  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
0094BCEB  8B 7C 24 70                     mov edi, dword ptr [rsp + 0x70]
0094BCEF  EB 29                           jmp 0x14094bd1a
0094BCF1  33 DB                           xor ebx, ebx
0094BCF3  8B 7C 24 70                     mov edi, dword ptr [rsp + 0x70]
0094BCF7  8B F3                           mov esi, ebx
0094BCF9  4C 8B BC 24 98 00 00 00         mov r15, qword ptr [rsp + 0x98]
0094BD01  EB 35                           jmp 0x14094bd38
0094BD03  33 C9                           xor ecx, ecx
0094BD05  E8 D6 22 AC FF                  call 0x14040dfe0
0094BD0A  84 C0                           test al, al
0094BD0C  74 08                           je 0x14094bd16
0094BD0E  41 8B 04 24                     mov eax, dword ptr [r12]
0094BD12  8B 38                           mov edi, dword ptr [rax]
0094BD14  EB 04                           jmp 0x14094bd1a
0094BD16  41 8B 3C 24                     mov edi, dword ptr [r12]
0094BD1A  4D 85 FF                        test r15, r15
0094BD1D  74 19                           je 0x14094bd38
0094BD1F  45 33 C0                        xor r8d, r8d
0094BD22  33 D2                           xor edx, edx
0094BD24  49 8B CF                        mov rcx, r15
0094BD27  E8 E4 35 9F FF                  call 0x14033f310
0094BD2C  EB 0A                           jmp 0x14094bd38
0094BD2E  B8 03 01 00 00                  mov eax, 0x103
0094BD33  85 FF                           test edi, edi
0094BD35  0F 49 F8                        cmovns edi, eax
0094BD38  48 85 F6                        test rsi, rsi
0094BD3B  74 0A                           je 0x14094bd47
0094BD3D  B2 01                           mov dl, 1
0094BD3F  48 8B CE                        mov rcx, rsi
0094BD42  E8 D5 62 B7 FF                  call 0x1404c201c
0094BD47  E8 78 91 BA FF                  call 0x1404f4ec4
0094BD4C  85 C0                           test eax, eax
0094BD4E  74 24                           je 0x14094bd74
0094BD50  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0094BD58  48 85 C9                        test rcx, rcx
0094BD5B  74 05                           je 0x14094bd62
0094BD5D  E8 EE D5 9A FF                  call 0x1402f9350
0094BD62  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0094BD6A  48 85 C9                        test rcx, rcx
0094BD6D  74 05                           je 0x14094bd74
0094BD6F  E8 DC D5 9A FF                  call 0x1402f9350
0094BD74  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0094BD7C  48 83 F9 FF                     cmp rcx, -1
0094BD80  74 07                           je 0x14094bd89
0094BD82  33 D2                           xor edx, edx
0094BD84  E8 E7 5A F5 FF                  call 0x1408a1870
0094BD89  4D 85 FF                        test r15, r15
0094BD8C  74 08                           je 0x14094bd96
0094BD8E  49 8B CF                        mov rcx, r15
0094BD91  E8 BA D5 9A FF                  call 0x1402f9350
0094BD96  8B C7                           mov eax, edi
0094BD98  0F 28 B4 24 50 01 00 00         movaps xmm6, xmmword ptr [rsp + 0x150]
0094BDA0  48 81 C4 60 01 00 00            add rsp, 0x160
0094BDA7  41 5F                           pop r15
0094BDA9  41 5E                           pop r14
0094BDAB  41 5D                           pop r13
0094BDAD  41 5C                           pop r12
0094BDAF  5F                              pop rdi
0094BDB0  5E                              pop rsi
0094BDB1  5B                              pop rbx
0094BDB2  C3                              ret
0094BDB3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtCopyFileChunk(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, unsigned __int8 a10)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int8 v_stack_m124;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m140;
    unsigned __int8 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (352);
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm6;
    v_rbx = 0;
    v_stack_m128 = 0;
    *(unsigned __int64 *)(v_rsp - 176) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 240) = 0;
    v_stack_mC0 = 0;
    v_stack_m100 = 0;
    v_stack_mB8 = 0;
    *(unsigned __int64 *)(v_rsp - 264) = 0;
    *(unsigned __int64 *)(v_rsp - 272) = 0;
    v_stack_mD8 = 0;
    v_stack_m120 = 0;
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    v_stack_m124 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (((a10) & (0xFFFFFFFEULL)) == 0) goto loc_0094B6B4;
    goto loc_0094BD98;
loc_0094B6B4:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_0094B751;
    if ((((unsigned __int8)(a6)) & (3)) != 0) goto loc_0094B73B;
    if (a6 < a1) { a1 = a6; }
    v_stack_mF8 = *(unsigned __int64 *)(a6);
    if ((((unsigned __int8)(a7)) & (3)) != 0) goto loc_0094B73B;
    if (a7 < a1) { a1 = a7; }
    v_stack_mE0 = *(unsigned __int64 *)(a7);
    if (a4 < a1) { a1 = a4; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_mB0 = v_xmm6;
    goto loc_0094B784;
loc_0094B73B:
    result = ExRaiseDatatypeMisalignment(v_stack_mF8, a7, a3, a4);
    v_rbx = 0;
    goto loc_0094BD38;
loc_0094B751:
    v_stack_mF8 = *(unsigned __int64 *)(a6);
    v_stack_mE0 = *(unsigned __int64 *)(a7);
    v_stack_mB0 = v_xmm6;
loc_0094B784:
    if (((a10) & (1)) == 0) goto loc_0094B80C;
    v_stack_m70 = a1;
    v_stack_m68 = *(unsigned __int64 *)(a6);
    v_stack_m60 = *(unsigned __int64 *)(a7);
    v_stack_m58 = (unsigned int)(a5);
    v_stack_m140 = 1;
    v_stack_m148 = 0;
    v_stack_m150 = 0;
    v_stack_m158 = 0;
    v_stack_m160 = 32;
    v_stack_m168 = v_stack_m70;
    v_stack_m170 = 0x98344ULL;
    v_stack_m178 = a4;
    a4 = 0;
    a3 = 0;
    result = IopXxxControlFile(v_stack_p10, v_stack_p18, a3, a4);
    goto loc_0094BD98;
loc_0094B80C:
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(v_stack_p10, v_stack_p18, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0094B8CA;
    v_stack_m178 = 0;
    result = IopReferenceFileObject(a1, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m108);
    if (sign_flag) goto loc_0094BD38;
    result = ObReferenceFileObjectForWrite(v_stack_p10, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m110, v_stack_mF0);
    if (sign_flag) goto loc_0094B882;
    result = IopFileObjectRevoked(v_stack_m110, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m110, v_stack_mF0);
    v_rdi = (unsigned int)((unsigned int)(result));
    v_r14 = (unsigned int)((unsigned int)(result));
    if ((unsigned __int8)(result) != 0) {
        v_rdi = 0xC0000910ULL;
        v_r14 = (unsigned int)(v_rdi);
    }
    if (sign_flag) goto loc_0094BD38;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m108 + 80)))) & (8)) == 0) goto loc_0094B8A7;
    result = IoGetRelatedDeviceObject(v_stack_m108, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m110, v_stack_mF0);
    goto loc_0094B8AB;
loc_0094B8A7:
loc_0094B8AB:
    result = (unsigned int)(*(unsigned int *)(v_stack_m110 + 80));
    v_rdi = (unsigned int)(v_stack_m120);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m110 + 80)))) & (8)) != 0) {
        result = IoGetRelatedDeviceObject(v_stack_m110, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m110, v_stack_mF0);
        a1 = *(unsigned int *)(result + 152);
        v_rdi = (unsigned int)(v_stack_m120);
        if (((unsigned int)((unsigned int)(v_stack_m120))) <= ((unsigned int)(a1))) { v_rdi = (unsigned int)(a1); }
    }
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(a1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m110, v_stack_mF0);
    if ((unsigned int)(result) == 0) goto loc_0094B920;
    a2 = ((unsigned int)(a5) + 80) + (v_rdi);
    result = ExAllocatePool2(75, a2, (unsigned int)(0x70436F49ULL), v_stack_mF0);
    v_stack_mD8 = result;
    if (result != 0) goto loc_0094B909;
loc_0094B8FF:
    goto loc_0094BD38;
loc_0094B909:
    v_rsi = (result + 80) + ((unsigned int)(0xC000009AULL));
    v_rdi = ~((unsigned int)(0xC000009AULL));
    v_rsi = (v_rsi) & (v_rdi);
    v_stack_m118 = v_rsi;
    goto loc_0094B93A;
loc_0094B920:
    result = ExAllocatePool2(67, a2, (unsigned int)(0x70436F49ULL), v_stack_mF0);
    v_stack_m118 = result;
    if (result == 0) goto loc_0094B8FF;
loc_0094B93A:
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(67, a2, (unsigned int)(0x70436F49ULL), v_stack_mF0);
    if ((unsigned int)(result) == 0) goto loc_0094B949;
    goto loc_0094B958;
loc_0094B949:
    v_rsi = (result) + (80);
    v_stack_m118 = v_rsi;
loc_0094B958:
    a2 = 0;
    result = memset(result, a2, a2 + 80, v_stack_mF0);
    *(unsigned __int64 *)(result + 64) = v_stack_mF8;
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(result, a2, a2 + 80, v_stack_mF0);
    if ((unsigned int)(result) != 0) {
        result = v_stack_m108;
        *(unsigned __int64 *)(result + 56) = result;
        result = v_stack_m110;
        *(unsigned __int64 *)(result + 48) = result;
        result = v_stack_mD8;
        *(unsigned __int64 *)(result + 72) = result;
        v_stack_m108 = 0;
        v_stack_m110 = 0;
    }
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(result, a2, a2 + 80, v_stack_mF0);
    if ((unsigned int)(result) != 0) goto loc_0094BA26;
    v_stack_m178 = 0;
    result = IopReferenceFileObject(v_stack_p8, result + 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), result + 56);
    if (sign_flag) goto loc_0094BD38;
    result = ObReferenceFileObjectForWrite(v_stack_p10, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), result + 48, v_stack_mF0);
    if (sign_flag) goto loc_0094BA18;
    result = IopFileObjectRevoked(*(unsigned __int64 *)(result + 48), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), result + 48, v_stack_mF0);
    v_rdi = (unsigned int)((unsigned int)(result));
    v_r13 = (unsigned int)((unsigned int)(result));
    if ((unsigned __int8)(result) != 0) {
        v_rdi = 0xC0000910ULL;
        v_r13 = (unsigned int)(v_rdi);
    }
    if (sign_flag) goto loc_0094BD38;
loc_0094BA26:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 48) + 80))))) & (2));
    v_stack_p50 = (unsigned int)(result);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 48) + 80))) >> (2));
    a2 = (unsigned __int8)((a2) & (1));
    v_stack_m120 = (unsigned int)(a2);
    a3 = 0;
    if ((unsigned int)(result) == 0) { a3 = v_stack_p18; }
    v_stack_m148 = result + 32;
    v_stack_m150 = (unsigned int)((unsigned int)(v_stack_mEC));
    v_stack_m158 = a9;
    v_stack_m160 = a7;
    v_stack_m168 = a3;
    v_stack_m170 = result + 56;
    result = IopPopulateCopyWriteWorkerData(*(unsigned __int64 *)(result + 48), 0, v_rsi, (unsigned int)(a5));
    v_stack_m128 = (unsigned int)(result);
    if (!sign_flag) goto loc_0094BAB3;
    *(unsigned __int64 *)(result + 48) = 0;
    goto loc_0094BD38;
loc_0094BAB3:
    if (a10 == 0) goto loc_0094BBEB;
    v_stack_mA0 = 48;
    v_stack_m88 = 512;
    v_stack_m98 = 0;
    v_stack_m90 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m178 = 0;
    result = ZwCreateEvent(v_stack_mE8, (unsigned int)(0x1F0003ULL), v_stack_mA0, 1);
    if (sign_flag) goto loc_0094BD38;
    v_stack_mD0 = 0;
    v_stack_m170 = 0;
    v_stack_m178 = v_stack_mD0;
    a4 = 0;
    a2 = 0;
    result = ObReferenceObjectByHandle(v_stack_mE8, a2, *(unsigned __int64 *)(v_rip + 6795351), a4);
    v_stack_mC0 = v_stack_mD0;
    v_stack_m128 = (unsigned int)(result);
    if (sign_flag) goto loc_0094BD38;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 80) = v_stack_mD0;
    if (v_stack_p18 == 0) goto loc_0094BBDF;
    v_stack_mC8 = 0;
    v_stack_m170 = 0;
    v_stack_m178 = v_stack_mC8;
    result = ObReferenceObjectByHandle(v_stack_p18, 2, *(unsigned __int64 *)(v_rip + 6795249), (unsigned __int8)(v_stack_m124));
    v_stack_m100 = v_stack_mC8;
    v_stack_m128 = (unsigned int)(result);
    if (sign_flag) goto loc_0094BD38;
    result = KeResetEvent(v_stack_mC8, 2, *(unsigned __int64 *)(v_rip + 6795249), (unsigned __int8)(v_stack_m124));
loc_0094BBDF:
    v_stack_mB8 = *(unsigned __int64 *)(result + 32);
loc_0094BBEB:
    if ((unsigned __int8)(v_stack_m124) == 0) goto loc_0094BC11;
    *(unsigned __int64 *)(a4) = v_xmm6;
    goto loc_0094BC17;
loc_0094BC11:
    *(unsigned __int64 *)(a4) = v_xmm6;
loc_0094BC17:
    result = ObfReferenceObject(*(unsigned __int64 *)(result + 56), 2, *(unsigned __int64 *)(v_rip + 6795249), (unsigned __int8)(v_stack_m124));
    v_stack_m130 = result + 56;
    v_stack_m138 = 0;
    v_stack_m140 = 0x40000000ULL;
    v_stack_m148 = 0;
    v_stack_m150 = 0;
    v_stack_m158 = a8;
    v_stack_m160 = a6;
    v_stack_m168 = (unsigned int)((unsigned int)(a5));
    v_stack_m170 = v_rsi;
    v_stack_m178 = 0;
    a4 = 0;
    a3 = 0;
    result = IopReadFile(*(unsigned __int64 *)(result + 56), v_stack_p18, a3, a4);
    if (sign_flag) goto loc_0094BD2E;
    if (a10 == 0) goto loc_0094BD2E;
    result = IopWaitForSynchronousIoEvent(v_stack_mB8, (unsigned __int8)(v_stack_m124), v_stack_m120, v_stack_mC0);
    v_stack_m128 = (unsigned int)(result);
    if (sign_flag) goto loc_0094BD1A;
    if ((unsigned __int8)(v_stack_m124) == 0) goto loc_0094BD03;
    a1 = 0;
    result = IoIs32bitProcess(a1, (unsigned __int8)(v_stack_m124), v_stack_m120, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_0094BCE3;
    v_stack_m128 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a4)))));
    goto loc_0094BCEB;
loc_0094BCE3:
    v_stack_m128 = (unsigned int)((unsigned int)(*(unsigned int *)(a4)));
loc_0094BCEB:
    goto loc_0094BD1A;
loc_0094BD03:
    a1 = 0;
    result = IoIs32bitProcess(a1, (unsigned __int8)(v_stack_m124), v_stack_m120, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_0094BD16;
    goto loc_0094BD1A;
loc_0094BD16:
loc_0094BD1A:
    if (v_stack_mC8 == 0) goto loc_0094BD38;
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_stack_mC8, a2, a3, v_stack_mC0);
    goto loc_0094BD38;
loc_0094BD2E:
    v_rdi = (unsigned int)(*(unsigned int *)(a4));
    if (!sign_flag) { v_rdi = 259; }
loc_0094BD38:
    result = 259;
    if (0 != 0) {
        a2 = 1;
        a1 = 0;
        result = IopFreeCopyObjectsFromDataBuffer(a1, a2, a3, v_stack_mC0);
    }
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, v_stack_mC0);
    if ((unsigned int)(result) == 0) goto loc_0094BD74;
    if (v_stack_m108 != 0) {
        result = ObfDereferenceObject(v_stack_m108, a2, a3, v_stack_mC0);
    }
    if (v_stack_m110 != 0) {
        result = ObfDereferenceObject(v_stack_m110, a2, a3, v_stack_mC0);
    }
    if (v_stack_mE8 != -1) {
        a2 = 0;
        result = ObCloseHandle(v_stack_mE8, a2, a3, v_stack_mC0);
    }
    if (v_stack_mC8 != 0) {
        a1 = v_stack_mC8;
        result = ObfDereferenceObject(a1, a2, a3, v_stack_mC0);
    }
loc_0094BD98:
    v_rsp = (v_rsp) + (352);
    return (unsigned int)((unsigned int)(v_rdi));
}
```

## 5. (Beta) C Style

```c
int64_t NtCopyFileChunk(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, void *Arg5, void *Arg6, void *Arg7, int64_t Arg8, int64_t Arg9, uint8_t Arg10)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint8_t v_stack_m124;
    uint32_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m140;
    uint8_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p50;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (352);
    *(uint64_t *)(local_rsp - 0x48) = v_xmm6;
    local_rbx = 0;
    v_stack_m128 = 0;
    *(uint64_t *)(local_rsp - 0xB0) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xF0) = 0;
    v_stack_mC0 = 0;
    v_stack_m100 = 0;
    v_stack_mB8 = 0;
    *(uint64_t *)(local_rsp - 0x108) = 0;
    *(uint64_t *)(local_rsp - 0x110) = 0;
    v_stack_mD8 = 0;
    v_stack_m120 = 0;
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    v_stack_m124 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (((Arg10) & (0xFFFFFFFEULL)) == 0) goto loc_0094B6B4;
    goto loc_0094BD98;
loc_0094B6B4:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_0094B751;
    if ((((uint8_t)(Arg6)) & (3)) != 0) goto loc_0094B73B;
    if (Arg6 < Arg1) { Arg1 = Arg6; }
    v_stack_mF8 = *(uint64_t *)(arg6);
    if ((((uint8_t)(Arg7)) & (3)) != 0) goto loc_0094B73B;
    if (Arg7 < Arg1) { Arg1 = Arg7; }
    v_stack_mE0 = *(uint64_t *)(arg7);
    if (Arg4 < Arg1) { Arg1 = Arg4; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    v_stack_mB0 = v_xmm6;
    goto loc_0094B784;
loc_0094B73B:
    result = ExRaiseDatatypeMisalignment(v_stack_mF8, Arg7, Arg3, Arg4);
    local_rbx = 0;
    goto loc_0094BD38;
loc_0094B751:
    v_stack_mF8 = *(uint64_t *)(arg6);
    v_stack_mE0 = *(uint64_t *)(arg7);
    v_stack_mB0 = v_xmm6;
loc_0094B784:
    if (((Arg10) & (1)) == 0) goto loc_0094B80C;
    v_stack_m70 = Arg1;
    v_stack_m68 = *(uint64_t *)(arg6);
    v_stack_m60 = *(uint64_t *)(arg7);
    v_stack_m58 = (uint32_t)(Arg5);
    v_stack_m140 = 1;
    v_stack_m148 = 0;
    v_stack_m150 = 0;
    v_stack_m158 = 0;
    v_stack_m160 = 32;
    v_stack_m168 = v_stack_m70;
    v_stack_m170 = 0x98344ULL;
    v_stack_m178 = Arg4;
    Arg4 = 0;
    Arg3 = 0;
    result = IopXxxControlFile(v_stack_p10, v_stack_p18, Arg3, Arg4);
    goto loc_0094BD98;
loc_0094B80C:
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(v_stack_p10, v_stack_p18, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0094B8CA;
    v_stack_m178 = 0;
    result = IopReferenceFileObject(Arg1, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m108);
    if (sign_flag) goto loc_0094BD38;
    result = ObReferenceFileObjectForWrite(v_stack_p10, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m110, v_stack_mF0);
    if (sign_flag) goto loc_0094B882;
    result = IopFileObjectRevoked(v_stack_m110, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m110, v_stack_mF0);
    local_rdi = (uint32_t)((uint32_t)(result));
    local_r14 = (uint32_t)((uint32_t)(result));
    if ((uint8_t)(result) != 0) {
        local_rdi = 0xC0000910ULL;
        local_r14 = (uint32_t)(local_rdi);
    }
    if (sign_flag) goto loc_0094BD38;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m108 + 0x50)))) & (8)) == 0) goto loc_0094B8A7;
    result = IoGetRelatedDeviceObject(v_stack_m108, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m110, v_stack_mF0);
    goto loc_0094B8AB;
loc_0094B8A7:
loc_0094B8AB:
    result = (uint32_t)(*(uint32_t *)(v_stack_m110 + 0x50));
    local_rdi = (uint32_t)(v_stack_m120);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m110 + 0x50)))) & (8)) != 0) {
        result = IoGetRelatedDeviceObject(v_stack_m110, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m110, v_stack_mF0);
        Arg1 = *(uint32_t *)(result + 0x98);
        local_rdi = (uint32_t)(v_stack_m120);
        if (((uint32_t)((uint32_t)(v_stack_m120))) <= ((uint32_t)(Arg1))) { local_rdi = (uint32_t)(Arg1); }
    }
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(Arg1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m110, v_stack_mF0);
    if ((uint32_t)(result) == 0) goto loc_0094B920;
    Arg2 = ((uint32_t)(Arg5) + 80) + (local_rdi);
    result = ExAllocatePool2(75, Arg2, (uint32_t)(0x70436F49ULL), v_stack_mF0);
    v_stack_mD8 = result;
    if (result != 0) goto loc_0094B909;
loc_0094B8FF:
    goto loc_0094BD38;
loc_0094B909:
    local_rsi = (result + 80) + ((uint32_t)(0xC000009AULL));
    local_rdi = ~((uint32_t)(0xC000009AULL));
    local_rsi = (local_rsi) & (local_rdi);
    v_stack_m118 = local_rsi;
    goto loc_0094B93A;
loc_0094B920:
    result = ExAllocatePool2(67, Arg2, (uint32_t)(0x70436F49ULL), v_stack_mF0);
    v_stack_m118 = result;
    if (result == 0) goto loc_0094B8FF;
loc_0094B93A:
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(67, Arg2, (uint32_t)(0x70436F49ULL), v_stack_mF0);
    if ((uint32_t)(result) == 0) goto loc_0094B949;
    goto loc_0094B958;
loc_0094B949:
    local_rsi = (result) + (80);
    v_stack_m118 = local_rsi;
loc_0094B958:
    Arg2 = 0;
    result = memset(result, Arg2, Arg2 + 80, v_stack_mF0);
    *(uint64_t *)(result + 0x40) = v_stack_mF8;
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(result, Arg2, Arg2 + 80, v_stack_mF0);
    if ((uint32_t)(result) != 0) {
        result = v_stack_m108;
        *(uint64_t *)(result + 0x38) = result;
        result = v_stack_m110;
        *(uint64_t *)(result + 0x30) = result;
        result = v_stack_mD8;
        *(uint64_t *)(result + 0x48) = result;
        v_stack_m108 = 0;
        v_stack_m110 = 0;
    }
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(result, Arg2, Arg2 + 80, v_stack_mF0);
    if ((uint32_t)(result) != 0) goto loc_0094BA26;
    v_stack_m178 = 0;
    result = IopReferenceFileObject(v_stack_p8, result + 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), result + 56);
    if (sign_flag) goto loc_0094BD38;
    result = ObReferenceFileObjectForWrite(v_stack_p10, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), result + 48, v_stack_mF0);
    if (sign_flag) goto loc_0094BA18;
    result = IopFileObjectRevoked(*(uint64_t *)(result + 0x30), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), result + 48, v_stack_mF0);
    local_rdi = (uint32_t)((uint32_t)(result));
    local_r13 = (uint32_t)((uint32_t)(result));
    if ((uint8_t)(result) != 0) {
        local_rdi = 0xC0000910ULL;
        local_r13 = (uint32_t)(local_rdi);
    }
    if (sign_flag) goto loc_0094BD38;
loc_0094BA26:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x30) + 0x50))))) & (2));
    v_stack_p50 = (uint32_t)(result);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x30) + 0x50))) >> (2));
    Arg2 = (uint8_t)((Arg2) & (1));
    v_stack_m120 = (uint32_t)(Arg2);
    Arg3 = 0;
    if ((uint32_t)(result) == 0) { Arg3 = v_stack_p18; }
    v_stack_m148 = result + 32;
    v_stack_m150 = (uint32_t)((uint32_t)(v_stack_mEC));
    v_stack_m158 = Arg9;
    v_stack_m160 = Arg7;
    v_stack_m168 = Arg3;
    v_stack_m170 = result + 56;
    result = IopPopulateCopyWriteWorkerData(*(uint64_t *)(result + 0x30), 0, local_rsi, (uint32_t)(Arg5));
    v_stack_m128 = (uint32_t)(result);
    if (!sign_flag) goto loc_0094BAB3;
    *(uint64_t *)(result + 0x30) = 0;
    goto loc_0094BD38;
loc_0094BAB3:
    if (Arg10 == 0) goto loc_0094BBEB;
    v_stack_mA0 = 48;
    v_stack_m88 = 512;
    v_stack_m98 = 0;
    v_stack_m90 = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m178 = 0;
    result = ZwCreateEvent(v_stack_mE8, (uint32_t)(0x1F0003ULL), v_stack_mA0, 1);
    if (sign_flag) goto loc_0094BD38;
    v_stack_mD0 = 0;
    v_stack_m170 = 0;
    v_stack_m178 = v_stack_mD0;
    Arg4 = 0;
    Arg2 = 0;
    result = ObReferenceObjectByHandle(v_stack_mE8, Arg2, *(uint64_t *)(v_rip + 0x67B057), Arg4);
    v_stack_mC0 = v_stack_mD0;
    v_stack_m128 = (uint32_t)(result);
    if (sign_flag) goto loc_0094BD38;
    *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x50) = v_stack_mD0;
    if (v_stack_p18 == 0) goto loc_0094BBDF;
    v_stack_mC8 = 0;
    v_stack_m170 = 0;
    v_stack_m178 = v_stack_mC8;
    result = ObReferenceObjectByHandle(v_stack_p18, 2, *(uint64_t *)(v_rip + 0x67AFF1), (uint8_t)(v_stack_m124));
    v_stack_m100 = v_stack_mC8;
    v_stack_m128 = (uint32_t)(result);
    if (sign_flag) goto loc_0094BD38;
    result = KeResetEvent(v_stack_mC8, 2, *(uint64_t *)(v_rip + 0x67AFF1), (uint8_t)(v_stack_m124));
loc_0094BBDF:
    v_stack_mB8 = *(uint64_t *)(result + 0x20);
loc_0094BBEB:
    if ((uint8_t)(v_stack_m124) == 0) goto loc_0094BC11;
    *(uint64_t *)(arg4) = v_xmm6;
    goto loc_0094BC17;
loc_0094BC11:
    *(uint64_t *)(arg4) = v_xmm6;
loc_0094BC17:
    result = ObfReferenceObject(*(uint64_t *)(result + 0x38), 2, *(uint64_t *)(v_rip + 0x67AFF1), (uint8_t)(v_stack_m124));
    v_stack_m130 = result + 56;
    v_stack_m138 = 0;
    v_stack_m140 = 0x40000000ULL;
    v_stack_m148 = 0;
    v_stack_m150 = 0;
    v_stack_m158 = Arg8;
    v_stack_m160 = Arg6;
    v_stack_m168 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m170 = local_rsi;
    v_stack_m178 = 0;
    Arg4 = 0;
    Arg3 = 0;
    result = IopReadFile(*(uint64_t *)(result + 0x38), v_stack_p18, Arg3, Arg4);
    if (sign_flag) goto loc_0094BD2E;
    if (Arg10 == 0) goto loc_0094BD2E;
    result = IopWaitForSynchronousIoEvent(v_stack_mB8, (uint8_t)(v_stack_m124), v_stack_m120, v_stack_mC0);
    v_stack_m128 = (uint32_t)(result);
    if (sign_flag) goto loc_0094BD1A;
    if ((uint8_t)(v_stack_m124) == 0) goto loc_0094BD03;
    Arg1 = 0;
    result = IoIs32bitProcess(Arg1, (uint8_t)(v_stack_m124), v_stack_m120, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_0094BCE3;
    v_stack_m128 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(arg4)))));
    goto loc_0094BCEB;
loc_0094BCE3:
    v_stack_m128 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4)));
loc_0094BCEB:
    goto loc_0094BD1A;
loc_0094BD03:
    Arg1 = 0;
    result = IoIs32bitProcess(Arg1, (uint8_t)(v_stack_m124), v_stack_m120, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_0094BD16;
    goto loc_0094BD1A;
loc_0094BD16:
loc_0094BD1A:
    if (v_stack_mC8 == 0) goto loc_0094BD38;
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_stack_mC8, Arg2, Arg3, v_stack_mC0);
    goto loc_0094BD38;
loc_0094BD2E:
    local_rdi = (uint32_t)(*(uint32_t *)(arg4));
    if (!sign_flag) { local_rdi = 259; }
loc_0094BD38:
    result = 259;
    if (0 != 0) {
        Arg2 = 1;
        Arg1 = 0;
        result = IopFreeCopyObjectsFromDataBuffer(Arg1, Arg2, Arg3, v_stack_mC0);
    }
    result = Feature_CopyFileChunk_BufferAlignment__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, v_stack_mC0);
    if ((uint32_t)(result) == 0) goto loc_0094BD74;
    if (v_stack_m108 != 0) {
        result = ObfDereferenceObject(v_stack_m108, Arg2, Arg3, v_stack_mC0);
    }
    if (v_stack_m110 != 0) {
        result = ObfDereferenceObject(v_stack_m110, Arg2, Arg3, v_stack_mC0);
    }
    if (v_stack_mE8 != -1) {
        Arg2 = 0;
        result = ObCloseHandle(v_stack_mE8, Arg2, Arg3, v_stack_mC0);
    }
    if (v_stack_mC8 != 0) {
        Arg1 = v_stack_mC8;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, v_stack_mC0);
    }
loc_0094BD98:
    local_rsp = (local_rsp) + (352);
    return (uint32_t)((uint32_t)(local_rdi));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `128` | `R` |
| `Arg5` | `+ 0x50` | `64` | `R` |
| `Arg6` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0094B600&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
