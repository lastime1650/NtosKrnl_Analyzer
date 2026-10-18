# NtLockFile

- RVA: `0x009D86D0`–`0x009D8D41` (길이 `1,649` bytes)
- VA: `0x00000001409D86D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A2E74`
- 디코드: `369`개 명령, `1,649/1,649` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009D8757` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x009D8807` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009D885E` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009D8899` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009D88C4` → [IopSetLockOperationProcess](../../text/43/IopSetLockOperationProcess_function_00433740.md) (function, `0x00433740`)
- `0x009D88DD` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x009D896D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009D89F2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009D8A4C` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x009D8A60` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x009D8A8F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009D8AC8` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009D8AF7` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x009D8B13` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009D8B4D` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x009D8B6D` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x009D8B88` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x009D8B90` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009D8C32` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009D8C73` → [IopExceptionCleanupEx](../8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x009D8C9D` → [IopSynchronousServiceTail](../8E/IopSynchronousServiceTail_function_008EB440.md) (function, `0x008EB440`)
- `0x009D8CB4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009D8CDD` → [IopWaitAndAcquireFileObjectLock](../8A/IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x009D8CED` → [MmIsDriverVerifying](../../text/4A/MmIsDriverVerifying_function_004A8770.md) (function, `0x004A8770`)
- `0x009D8CFD` → [VfFastIoSnapState](../../pagevrfy/BB/VfFastIoSnapState_function_00BB97BC.md) (function, `0x00BB97BC`)
- `0x009D8D10` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (function, `0x00BB9440`)
- `0x009D8D1D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009D8D2A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009D8D37` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009D890B` → RVA `0x00F04A20` (`.data`; read)
- `0x009D8B20` → RVA `0x00FC6B80` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x009D8757` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (`PAGE` → `.text`)
  - `0x009D8807` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009D8899` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009D88C4` → [IopSetLockOperationProcess](../../text/43/IopSetLockOperationProcess_function_00433740.md) (`PAGE` → `.text`)
  - `0x009D88DD` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x009D896D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009D89F2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009D8A4C` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (`PAGE` → `.text`)
  - `0x009D8A60` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x009D8A8F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009D8AC8` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009D8AF7` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x009D8B13` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009D8B6D` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x009D8B88` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x009D8B90` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009D8C32` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009D8CB4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009D8CED` → [MmIsDriverVerifying](../../text/4A/MmIsDriverVerifying_function_004A8770.md) (`PAGE` → `.text`)
  - `0x009D8CFD` → [VfFastIoSnapState](../../pagevrfy/BB/VfFastIoSnapState_function_00BB97BC.md) (`PAGE` → `PAGEVRFY`)
  - `0x009D8D10` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (`PAGE` → `PAGEVRFY`)
  - `0x009D8D1D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009D8D2A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009D8D37` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x009D89E9` → [sub_00B2FAB0](../B2/Unknown_function_00B2FAB0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009D86D0  4C 8B DC                        mov r11, rsp
009D86D3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
009D86D7  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
009D86DB  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
009D86DF  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
009D86E3  57                              push rdi
009D86E4  41 54                           push r12
009D86E6  41 55                           push r13
009D86E8  41 56                           push r14
009D86EA  41 57                           push r15
009D86EC  48 81 EC C0 00 00 00            sub rsp, 0xc0
009D86F3  48 8B F2                        mov rsi, rdx
009D86F6  48 8B 9C 24 20 01 00 00         mov rbx, qword ptr [rsp + 0x120]
009D86FE  48 8B BC 24 18 01 00 00         mov rdi, qword ptr [rsp + 0x118]
009D8706  45 33 FF                        xor r15d, r15d
009D8709  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
009D870E  45 8B EF                        mov r13d, r15d
009D8711  4C 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r15
009D8719  4D 89 7B 88                     mov qword ptr [r11 - 0x78], r15
009D871D  4D 89 7B 90                     mov qword ptr [r11 - 0x70], r15
009D8721  4D 89 7B A8                     mov qword ptr [r11 - 0x58], r15
009D8725  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009D872E  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
009D8736  44 0F B6 A0 32 02 00 00         movzx r12d, byte ptr [rax + 0x232]
009D873E  44 88 64 24 51                  mov byte ptr [rsp + 0x51], r12b
009D8743  49 8D 43 A8                     lea rax, [r11 - 0x58]
009D8747  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009D874C  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
009D8751  45 0F B6 C4                     movzx r8d, r12b
009D8755  33 D2                           xor edx, edx
009D8757  E8 D4 4D 8C FF                  call 0x14029d530
009D875C  85 C0                           test eax, eax
009D875E  0F 88 97 02 00 00               js 0x1409d89fb
009D8764  45 84 E4                        test r12b, r12b
009D8767  0F 84 AC 02 00 00               je 0x1409d8a19
009D876D  F6 84 24 94 00 00 00 03         test byte ptr [rsp + 0x94], 3
009D8775  0F 84 34 05 00 00               je 0x1409d8caf
009D877B  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
009D8785  48 8B D0                        mov rdx, rax
009D8788  48 39 84 24 10 01 00 00         cmp qword ptr [rsp + 0x110], rax
009D8790  48 0F 42 94 24 10 01 00 00      cmovb rdx, qword ptr [rsp + 0x110]
009D8799  8B 0A                           mov ecx, dword ptr [rdx]
009D879B  89 0A                           mov dword ptr [rdx], ecx
009D879D  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009D87A2  0F B6 51 50                     movzx edx, byte ptr [rcx + 0x50]
009D87A6  80 E2 02                        and dl, 2
009D87A9  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009D87B2  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
009D87BA  4C 8B 81 B8 00 00 00            mov r8, qword ptr [rcx + 0xb8]
009D87C1  4D 39 B8 10 03 00 00            cmp qword ptr [r8 + 0x310], r15
009D87C8  75 4C                           jne 0x1409d8816
009D87CA  E9 89 00 00 00                  jmp 0x1409d8858
009D87CF  48 3B D8                        cmp rbx, rax
009D87D2  48 0F 42 C3                     cmovb rax, rbx
009D87D6  90                              nop
009D87D7  0F B6 08                        movzx ecx, byte ptr [rax]
009D87DA  48 8B 03                        mov rax, qword ptr [rbx]
009D87DD  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009D87E2  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009D87E7  48 83 B8 B0 00 00 00 00         cmp qword ptr [rax + 0xb0], 0
009D87EF  75 05                           jne 0x1409d87f6
009D87F1  E9 AF 00 00 00                  jmp 0x1409d88a5
009D87F6  48 F7 84 24 00 01 00 00 FE FF FF FF  test qword ptr [rsp + 0x100], -2
009D8802  74 ED                           je 0x1409d87f1
009D8804  48 8B C8                        mov rcx, rax
009D8807  E8 44 0B 92 FF                  call 0x1402f9350
009D880C  B8 0D 00 00 C0                  mov eax, 0xc000000d
009D8811  E9 E5 01 00 00                  jmp 0x1409d89fb
009D8816  41 0F B7 88 EC 06 00 00         movzx ecx, word ptr [r8 + 0x6ec]
009D881E  41 B8 4C 01 00 00               mov r8d, 0x14c
009D8824  66 41 3B C8                     cmp cx, r8w
009D8828  75 3A                           jne 0x1409d8864
009D882A  84 D2                           test dl, dl
009D882C  75 2A                           jne 0x1409d8858
009D882E  4C 8B 84 24 00 01 00 00         mov r8, qword ptr [rsp + 0x100]
009D8836  49 83 C8 01                     or r8, 1
009D883A  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
009D8842  8B 11                           mov edx, dword ptr [rcx]
009D8844  8B 0A                           mov ecx, dword ptr [rdx]
009D8846  89 0A                           mov dword ptr [rdx], ecx
009D8848  48 89 94 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdx
009D8850  4C 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], r8
009D8858  40 F6 C7 03                     test dil, 3
009D885C  74 14                           je 0x1409d8872
009D885E  E8 6D 17 EC FF                  call 0x140899fd0
009D8863  CC                              int3
009D8864  41 B8 C4 01 00 00               mov r8d, 0x1c4
009D886A  66 41 3B C8                     cmp cx, r8w
009D886E  75 E8                           jne 0x1409d8858
009D8870  EB B8                           jmp 0x1409d882a
009D8872  48 8B C8                        mov rcx, rax
009D8875  48 3B F8                        cmp rdi, rax
009D8878  48 0F 42 CF                     cmovb rcx, rdi
009D887C  90                              nop
009D887D  0F B6 09                        movzx ecx, byte ptr [rcx]
009D8880  48 8B 0F                        mov rcx, qword ptr [rdi]
009D8883  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
009D8888  F6 C3 03                        test bl, 3
009D888B  75 D1                           jne 0x1409d885e
009D888D  E9 3D FF FF FF                  jmp 0x1409d87cf
009D8892  8B D8                           mov ebx, eax
009D8894  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009D8899  E8 B2 0A 92 FF                  call 0x1402f9350
009D889E  8B C3                           mov eax, ebx
009D88A0  E9 56 01 00 00                  jmp 0x1409d89fb
009D88A5  C6 40 48 01                     mov byte ptr [rax + 0x48], 1
009D88A9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009D88B2  48 8B 90 B8 00 00 00            mov rdx, qword ptr [rax + 0xb8]
009D88B9  45 33 C0                        xor r8d, r8d
009D88BC  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
009D88C1  48 8B CB                        mov rcx, rbx
009D88C4  E8 77 AE A5 FF                  call 0x140433740
009D88C9  85 C0                           test eax, eax
009D88CB  0F 88 2A 01 00 00               js 0x1409d89fb
009D88D1  48 85 F6                        test rsi, rsi
009D88D4  0F 85 46 02 00 00               jne 0x1409d8b20
009D88DA  48 8B CB                        mov rcx, rbx
009D88DD  E8 3E 28 8C FF                  call 0x14029b120
009D88E2  48 8B F0                        mov rsi, rax
009D88E5  4C 8B 70 08                     mov r14, qword ptr [rax + 8]
009D88E9  49 8B 46 50                     mov rax, qword ptr [r14 + 0x50]
009D88ED  48 85 C0                        test rax, rax
009D88F0  0F 84 43 01 00 00               je 0x1409d8a39
009D88F6  48 8B 78 30                     mov rdi, qword ptr [rax + 0x30]
009D88FA  48 85 FF                        test rdi, rdi
009D88FD  0F 84 36 01 00 00               je 0x1409d8a39
009D8903  0F 57 C0                        xorps xmm0, xmm0
009D8906  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
009D890B  8B 05 0F C1 52 00               mov eax, dword ptr [rip + 0x52c10f]
009D8911  A8 10                           test al, 0x10
009D8913  0F 85 D1 03 00 00               jne 0x1409d8cea
009D8919  4D 8B F7                        mov r14, r15
009D891C  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
009D8921  48 8D 44 24 60                  lea rax, [rsp + 0x60]
009D8926  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009D892B  0F B6 84 24 38 01 00 00         movzx eax, byte ptr [rsp + 0x138]
009D8933  88 44 24 30                     mov byte ptr [rsp + 0x30], al
009D8937  0F B6 84 24 30 01 00 00         movzx eax, byte ptr [rsp + 0x130]
009D893F  88 44 24 28                     mov byte ptr [rsp + 0x28], al
009D8943  8B 84 24 28 01 00 00            mov eax, dword ptr [rsp + 0x128]
009D894A  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009D894E  4C 8B 8C 24 A8 00 00 00         mov r9, qword ptr [rsp + 0xa8]
009D8956  4D 8B 89 B8 00 00 00            mov r9, qword ptr [r9 + 0xb8]
009D895D  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
009D8962  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
009D8967  48 8B CB                        mov rcx, rbx
009D896A  48 8B C7                        mov rax, rdi
009D896D  E8 5E 21 CE FF                  call 0x1406baad0
009D8972  44 0F B6 E0                     movzx r12d, al
009D8976  4D 85 F6                        test r14, r14
009D8979  0F 85 8B 03 00 00               jne 0x1409d8d0a
009D897F  45 84 E4                        test r12b, r12b
009D8982  0F 84 AB 00 00 00               je 0x1409d8a33
009D8988  F6 84 24 00 01 00 00 01         test byte ptr [rsp + 0x100], 1
009D8990  75 12                           jne 0x1409d89a4
009D8992  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
009D899A  0F 10 44 24 60                  movups xmm0, xmmword ptr [rsp + 0x60]
009D899F  0F 11 00                        movups xmmword ptr [rax], xmm0
009D89A2  EB 15                           jmp 0x1409d89b9
009D89A4  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
009D89AC  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
009D89B0  89 41 04                        mov dword ptr [rcx + 4], eax
009D89B3  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
009D89B7  89 01                           mov dword ptr [rcx], eax
009D89B9  EB 1D                           jmp 0x1409d89d8
009D89BB  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
009D89BF  48 C7 44 24 68 00 00 00 00      mov qword ptr [rsp + 0x68], 0
009D89C8  45 33 FF                        xor r15d, r15d
009D89CB  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
009D89D0  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
009D89D8  4D 85 ED                        test r13, r13
009D89DB  0F 85 96 01 00 00               jne 0x1409d8b77
009D89E1  48 83 BB B0 00 00 00 00         cmp qword ptr [rbx + 0xb0], 0
009D89E9  0F 85 C1 70 15 00               jne 0x140b2fab0
009D89EF  48 8B CB                        mov rcx, rbx
009D89F2  E8 59 09 92 FF                  call 0x1402f9350
009D89F7  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
009D89FB  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
009D8A03  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
009D8A07  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
009D8A0B  49 8B E3                        mov rsp, r11
009D8A0E  41 5F                           pop r15
009D8A10  41 5E                           pop r14
009D8A12  41 5D                           pop r13
009D8A14  41 5C                           pop r12
009D8A16  5F                              pop rdi
009D8A17  C3                              ret
009D8A18  CC                              int3
009D8A19  48 8B 07                        mov rax, qword ptr [rdi]
009D8A1C  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
009D8A21  48 8B 03                        mov rax, qword ptr [rbx]
009D8A24  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009D8A29  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009D8A2E  E9 72 FE FF FF                  jmp 0x1409d88a5
009D8A33  44 0F B6 64 24 51               movzx r12d, byte ptr [rsp + 0x51]
009D8A39  48 8D 7B 50                     lea rdi, [rbx + 0x50]
009D8A3D  44 8B 37                        mov r14d, dword ptr [rdi]
009D8A40  41 F6 C6 02                     test r14b, 2
009D8A44  75 58                           jne 0x1409d8a9e
009D8A46  45 32 FF                        xor r15b, r15b
009D8A49  48 8B CB                        mov rcx, rbx
009D8A4C  E8 9F 4B 8C FF                  call 0x14029d5f0
009D8A51  45 0F B6 C7                     movzx r8d, r15b
009D8A55  41 80 F0 01                     xor r8b, 1
009D8A59  0F B6 56 4C                     movzx edx, byte ptr [rsi + 0x4c]
009D8A5D  48 8B CE                        mov rcx, rsi
009D8A60  E8 BB EC 82 FF                  call 0x140207720
009D8A65  4C 8B F0                        mov r14, rax
009D8A68  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
009D8A70  48 85 C0                        test rax, rax
009D8A73  0F 85 21 01 00 00               jne 0x1409d8b9a
009D8A79  4D 85 ED                        test r13, r13
009D8A7C  0F 85 A5 02 00 00               jne 0x1409d8d27
009D8A82  8B 07                           mov eax, dword ptr [rdi]
009D8A84  A8 02                           test al, 2
009D8A86  0F 85 A8 02 00 00               jne 0x1409d8d34
009D8A8C  48 8B CB                        mov rcx, rbx
009D8A8F  E8 BC 08 92 FF                  call 0x1402f9350
009D8A94  B8 9A 00 00 C0                  mov eax, 0xc000009a
009D8A99  E9 5D FF FF FF                  jmp 0x1409d89fb
009D8A9E  41 C1 EE 02                     shr r14d, 2
009D8AA2  41 80 E6 01                     and r14b, 1
009D8AA6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009D8AAF  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
009D8AB6  90                              nop
009D8AB7  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
009D8ABC  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
009D8AC3  45 33 C0                        xor r8d, r8d
009D8AC6  33 D2                           xor edx, edx
009D8AC8  E8 63 77 83 FF                  call 0x140210230
009D8ACD  4C 8B C8                        mov r9, rax
009D8AD0  C6 44 24 50 00                  mov byte ptr [rsp + 0x50], 0
009D8AD5  B8 01 00 00 00                  mov eax, 1
009D8ADA  87 43 74                        xchg dword ptr [rbx + 0x74], eax
009D8ADD  85 C0                           test eax, eax
009D8ADF  0F 85 DE 01 00 00               jne 0x1409d8cc3
009D8AE5  4D 85 C9                        test r9, r9
009D8AE8  74 05                           je 0x1409d8aef
009D8AEA  41 C6 41 0A 01                  mov byte ptr [r9 + 0xa], 1
009D8AEF  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
009D8AF4  48 8B CB                        mov rcx, rbx
009D8AF7  E8 24 6F 83 FF                  call 0x14020fa20
009D8AFC  80 7C 24 50 00                  cmp byte ptr [rsp + 0x50], 0
009D8B01  0F 84 A0 01 00 00               je 0x1409d8ca7
009D8B07  4D 85 ED                        test r13, r13
009D8B0A  0F 85 0A 02 00 00               jne 0x1409d8d1a
009D8B10  48 8B CB                        mov rcx, rbx
009D8B13  E8 38 08 92 FF                  call 0x1402f9350
009D8B18  41 8B C7                        mov eax, r15d
009D8B1B  E9 DB FE FF FF                  jmp 0x1409d89fb
009D8B20  4C 8B 05 59 E0 5E 00            mov r8, qword ptr [rip + 0x5ee059]
009D8B27  4C 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r15
009D8B2F  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
009D8B34  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
009D8B3C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009D8B41  45 0F B6 CC                     movzx r9d, r12b
009D8B45  BA 02 00 00 00                  mov edx, 2
009D8B4A  48 8B CE                        mov rcx, rsi
009D8B4D  E8 5E 02 E9 FF                  call 0x140868db0
009D8B52  4C 8B AC 24 98 00 00 00         mov r13, qword ptr [rsp + 0x98]
009D8B5A  4C 89 AC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r13
009D8B62  85 C0                           test eax, eax
009D8B64  0F 88 70 FD FF FF               js 0x1409d88da
009D8B6A  49 8B CD                        mov rcx, r13
009D8B6D  E8 DE F7 86 FF                  call 0x140248350
009D8B72  E9 63 FD FF FF                  jmp 0x1409d88da
009D8B77  F7 43 50 00 00 00 08            test dword ptr [rbx + 0x50], 0x8000000
009D8B7E  75 0D                           jne 0x1409d8b8d
009D8B80  45 33 C0                        xor r8d, r8d
009D8B83  33 D2                           xor edx, edx
009D8B85  49 8B CD                        mov rcx, r13
009D8B88  E8 83 67 96 FF                  call 0x14033f310
009D8B8D  49 8B CD                        mov rcx, r13
009D8B90  E8 BB 07 92 FF                  call 0x1402f9350
009D8B95  E9 47 FE FF FF                  jmp 0x1409d89e1
009D8B9A  48 89 98 C0 00 00 00            mov qword ptr [rax + 0xc0], rbx
009D8BA1  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
009D8BA9  49 89 86 98 00 00 00            mov qword ptr [r14 + 0x98], rax
009D8BB0  45 88 66 40                     mov byte ptr [r14 + 0x40], r12b
009D8BB4  4D 89 6E 50                     mov qword ptr [r14 + 0x50], r13
009D8BB8  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
009D8BC0  49 89 46 48                     mov qword ptr [r14 + 0x48], rax
009D8BC4  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
009D8BCC  49 89 46 58                     mov qword ptr [r14 + 0x58], rax
009D8BD0  48 8B BC 24 08 01 00 00         mov rdi, qword ptr [rsp + 0x108]
009D8BD8  49 89 7E 60                     mov qword ptr [r14 + 0x60], rdi
009D8BDC  49 8B BE B8 00 00 00            mov rdi, qword ptr [r14 + 0xb8]
009D8BE3  66 C7 47 B8 11 01               mov word ptr [rdi - 0x48], 0x111
009D8BE9  48 89 5F E8                     mov qword ptr [rdi - 0x18], rbx
009D8BED  C6 47 BA 00                     mov byte ptr [rdi - 0x46], 0
009D8BF1  32 C0                           xor al, al
009D8BF3  38 84 24 30 01 00 00            cmp byte ptr [rsp + 0x130], al
009D8BFA  74 06                           je 0x1409d8c02
009D8BFC  C6 47 BA 01                     mov byte ptr [rdi - 0x46], 1
009D8C00  B0 01                           mov al, 1
009D8C02  80 BC 24 38 01 00 00 00         cmp byte ptr [rsp + 0x138], 0
009D8C0A  74 05                           je 0x1409d8c11
009D8C0C  0C 02                           or al, 2
009D8C0E  88 47 BA                        mov byte ptr [rdi - 0x46], al
009D8C11  8B 84 24 28 01 00 00            mov eax, dword ptr [rsp + 0x128]
009D8C18  89 47 C8                        mov dword ptr [rdi - 0x38], eax
009D8C1B  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
009D8C20  48 89 47 D0                     mov qword ptr [rdi - 0x30], rax
009D8C24  BA 08 00 00 00                  mov edx, 8
009D8C29  8D 4A 59                        lea ecx, [rdx + 0x59]
009D8C2C  41 B8 49 6F 4C 65               mov r8d, 0x654c6f49
009D8C32  E8 B9 94 1A 00                  call 0x140b820f0
009D8C37  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009D8C3C  48 89 08                        mov qword ptr [rax], rcx
009D8C3F  49 89 86 A0 00 00 00            mov qword ptr [r14 + 0xa0], rax
009D8C46  48 89 47 C0                     mov qword ptr [rdi - 0x40], rax
009D8C4A  EB 33                           jmp 0x1409d8c7f
009D8C4C  8B D8                           mov ebx, eax
009D8C4E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009D8C53  0F B6 51 50                     movzx edx, byte ptr [rcx + 0x50]
009D8C57  D1 EA                           shr edx, 1
009D8C59  83 E2 01                        and edx, 1
009D8C5C  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
009D8C60  45 33 C9                        xor r9d, r9d
009D8C63  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
009D8C6B  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
009D8C73  E8 50 59 ED FF                  call 0x1408ae5c8
009D8C78  8B C3                           mov eax, ebx
009D8C7A  E9 7C FD FF FF                  jmp 0x1409d89fb
009D8C7F  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
009D8C87  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
009D8C8C  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
009D8C91  45 33 C9                        xor r9d, r9d
009D8C94  4C 8B C3                        mov r8, rbx
009D8C97  49 8B D6                        mov rdx, r14
009D8C9A  48 8B CE                        mov rcx, rsi
009D8C9D  E8 9E 27 F1 FF                  call 0x1408eb440
009D8CA2  E9 54 FD FF FF                  jmp 0x1409d89fb
009D8CA7  41 B7 01                        mov r15b, 1
009D8CAA  E9 9A FD FF FF                  jmp 0x1409d8a49
009D8CAF  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009D8CB4  E8 97 06 92 FF                  call 0x1402f9350
009D8CB9  B8 22 00 00 C0                  mov eax, 0xc0000022
009D8CBE  E9 38 FD FF FF                  jmp 0x1409d89fb
009D8CC3  48 8D 44 24 50                  lea rax, [rsp + 0x50]
009D8CC8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009D8CCD  45 0F B6 C6                     movzx r8d, r14b
009D8CD1  41 0F B6 D4                     movzx edx, r12b
009D8CD5  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
009D8CDA  48 8B CB                        mov rcx, rbx
009D8CDD  E8 F6 59 ED FF                  call 0x1408ae6d8
009D8CE2  44 8B F8                        mov r15d, eax
009D8CE5  E9 12 FE FF FF                  jmp 0x1409d8afc
009D8CEA  49 8B CE                        mov rcx, r14
009D8CED  E8 7E FA AC FF                  call 0x1404a8770
009D8CF2  85 C0                           test eax, eax
009D8CF4  0F 84 1F FC FF FF               je 0x1409d8919
009D8CFA  49 8B CE                        mov rcx, r14
009D8CFD  E8 BA 0A 1E 00                  call 0x140bb97bc
009D8D02  4C 8B F0                        mov r14, rax
009D8D05  E9 12 FC FF FF                  jmp 0x1409d891c
009D8D0A  48 8B D7                        mov rdx, rdi
009D8D0D  49 8B CE                        mov rcx, r14
009D8D10  E8 2B 07 1E 00                  call 0x140bb9440
009D8D15  E9 65 FC FF FF                  jmp 0x1409d897f
009D8D1A  49 8B CD                        mov rcx, r13
009D8D1D  E8 2E 06 92 FF                  call 0x1402f9350
009D8D22  E9 E9 FD FF FF                  jmp 0x1409d8b10
009D8D27  49 8B CD                        mov rcx, r13
009D8D2A  E8 21 06 92 FF                  call 0x1402f9350
009D8D2F  E9 4E FD FF FF                  jmp 0x1409d8a82
009D8D34  48 8B CB                        mov rcx, rbx
009D8D37  E8 54 7D 87 FF                  call 0x140250a90
009D8D3C  E9 4B FD FF FF                  jmp 0x1409d8a8c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtLockFile(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned int a8, unsigned __int8 a9, unsigned __int8 a10)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int8 v_stack_m54;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int8 v_stack_m6F;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int8 v_stack_m97;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int8 v_stack_mB8;
    unsigned __int8 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (192);
    v_r15 = 0;
    v_stack_m90 = 0;
    v_stack_m60 = 0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    v_stack_m40 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m97 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_mC8 = v_rsp - 88;
    a2 = 0;
    result = IopReferenceFileObject(a1, a2, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m90);
    if (sign_flag) goto loc_009D89FB;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_009D8A19;
    if (((v_stack_m54) & (3)) == 0) goto loc_009D8CAF;
    a2 = result;
    if (a5 < result) { a2 = a5; }
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m90 + 80)) & (2));
    v_stack_m38 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) != 0) goto loc_009D8816;
    goto loc_009D8858;
loc_009D87CF:
    if (a7 < result) { result = a7; }
    v_stack_m70 = *(unsigned __int64 *)(a7);
    if ((*(unsigned __int64 *)(v_stack_m90 + 176)) != 0) goto loc_009D87F6;
loc_009D87F1:
    goto loc_009D88A5;
loc_009D87F6:
    if (((v_stack_p18) & (-2)) == 0) goto loc_009D87F1;
    result = ObfDereferenceObject(v_stack_m90, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), v_stack_m90);
    goto loc_009D89FB;
loc_009D8816:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) != 332) goto loc_009D8864;
loc_009D882A:
    if ((unsigned __int8)(a2) == 0) {
        a3 = v_stack_p18;
        a3 = (a3) | (1);
        a1 = a5;
        a2 = *(unsigned int *)(a1);
        a1 = *(unsigned int *)(a2);
        *(unsigned int *)(a2) = (unsigned int)(a1);
        v_stack_p28 = a2;
        v_stack_p18 = a3;
    }
    if ((((unsigned __int8)(a6)) & (3)) == 0) goto loc_009D8872;
loc_009D885E:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, v_stack_m90);
loc_009D8864:
    if (((unsigned __int16)(a1)) != 452) goto loc_009D8858;
    goto loc_009D882A;
loc_009D8872:
    a1 = result;
    if (a6 < result) { a1 = a6; }
    v_stack_m78 = *(unsigned __int64 *)(a6);
    if ((((unsigned __int8)(a7)) & (3)) != 0) goto loc_009D885E;
    goto loc_009D87CF;
loc_009D88A5:
    *(unsigned __int8 *)(result + 72) = 1;
    a3 = 0;
    result = IopSetLockOperationProcess(v_stack_m90, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, v_stack_m90);
    if (sign_flag) goto loc_009D89FB;
    if (a2 != 0) goto loc_009D8B20;
loc_009D88DA:
    result = IoGetRelatedDeviceObject(v_stack_m90, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, v_stack_m90);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80) == 0) goto loc_009D8A39;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80) + 48) == 0) goto loc_009D8A39;
    v_stack_m88 = v_xmm0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5423375)))) & (16)) != 0) goto loc_009D8CEA;
loc_009D8919:
loc_009D891C:
    v_stack_mA8 = result;
    v_stack_mB0 = v_stack_m88;
    v_stack_mB8 = a10;
    v_stack_mC0 = a9;
    v_stack_mC8 = (unsigned int)((unsigned int)(a8));
    result = guard_dispatch_icall(v_stack_m90, v_stack_m78, v_stack_m70, *(unsigned __int64 *)(v_stack_m40 + 184));
    if (0 != 0) goto loc_009D8D0A;
loc_009D897F:
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_009D8A33;
    if (((v_stack_p18) & (1)) != 0) goto loc_009D89A4;
    *(unsigned __int64 *)(a5) = v_xmm0;
    goto loc_009D89B9;
loc_009D89A4:
    *(unsigned int *)(a5 + 4) = (unsigned int)((unsigned int)(v_stack_m80));
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(v_stack_m88));
loc_009D89B9:
    goto loc_009D89D8;
loc_009D89D8:
    if (0 != 0) goto loc_009D8B77;
loc_009D89E1:
    result = ObfDereferenceObject(v_stack_m90, v_stack_m78, v_stack_m70, *(unsigned __int64 *)(v_stack_m40 + 184));
loc_009D89FB:
    return (unsigned int)(v_stack_m88);
loc_009D8A19:
    v_stack_m50 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80) + 48));
    v_stack_m48 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 48));
    goto loc_009D88A5;
loc_009D8A33:
loc_009D8A39:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 80)))) & (2)) != 0) goto loc_009D8A9E;
    v_r15 = 0;
loc_009D8A49:
    result = IopResetEvent(*(unsigned __int64 *)(v_stack_m28 + 48), v_stack_m78, v_stack_m70, *(unsigned __int64 *)(v_stack_m40 + 184));
    a3 = (unsigned __int8)((0) ^ (1));
    result = IopAllocateIrpExReturn(*(unsigned __int64 *)(v_stack_m28 + 56), *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 76), a3, *(unsigned __int64 *)(v_stack_m40 + 184));
    v_stack_m40 = result;
    if (result != 0) goto loc_009D8B9A;
    if (0 != 0) goto loc_009D8D27;
loc_009D8A82:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 48) + 80)))) & (2)) != 0) goto loc_009D8D34;
loc_009D8A8C:
    result = ObfDereferenceObject(*(unsigned __int64 *)(v_stack_m28 + 48), *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 76), a3, *(unsigned __int64 *)(v_stack_m40 + 184));
    goto loc_009D89FB;
loc_009D8A9E:
    v_r14 = (unsigned int)((result) >> (2));
    v_r14 = (unsigned __int8)((v_r14) & (1));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m68 + 128, a2, a3, *(unsigned __int64 *)(v_stack_m40 + 184));
    v_stack_m70 = 0;
    if (1 != 0) goto loc_009D8CC3;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(v_stack_m68, a2, a3, result);
loc_009D8AFC:
    if (v_stack_m70 == 0) goto loc_009D8CA7;
    if (0 != 0) goto loc_009D8D1A;
loc_009D8B10:
    result = ObfDereferenceObject(v_stack_m68, a2, a3, result);
    goto loc_009D89FB;
loc_009D8B20:
    v_stack_m28 = 0;
    v_stack_m98 = 0;
    v_stack_mA0 = v_stack_m28;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(v_stack_m28 + 56), 2, *(unsigned __int64 *)(v_rip + 6217817), (unsigned __int8)(v_stack_m6F));
    v_stack_m38 = v_stack_m28;
    if (sign_flag) goto loc_009D88DA;
    result = KeResetEvent(v_stack_m28, 2, *(unsigned __int64 *)(v_rip + 6217817), (unsigned __int8)(v_stack_m6F));
    goto loc_009D88DA;
loc_009D8B77:
    if (((*(unsigned int *)(v_stack_m68 + 80)) & (0x8000000ULL)) == 0) {
        a3 = 0;
        a2 = 0;
        a1 = v_stack_m28;
        result = KeSetEvent(a1, a2, a3, (unsigned __int8)(v_stack_m6F));
    }
    result = ObfDereferenceObject(v_stack_m28, a2, a3, (unsigned __int8)(v_stack_m6F));
    goto loc_009D89E1;
loc_009D8B9A:
    *(unsigned __int64 *)(result + 192) = v_stack_m68;
    *(unsigned __int64 *)(v_r14 + 152) = v_stack_m18;
    *(unsigned __int8 *)(v_r14 + 64) = (unsigned __int8)(v_stack_m6F);
    *(unsigned __int64 *)(v_r14 + 80) = v_stack_m28;
    *(unsigned __int64 *)(v_r14 + 72) = a5;
    *(unsigned __int64 *)(v_r14 + 88) = v_stack_p40;
    *(unsigned __int64 *)(v_r14 + 96) = v_stack_p48;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 184) - 72) = 273;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 184) - 24) = v_stack_m68;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_r14 + 184) - 70) = 0;
    result = 0;
    if (a9 != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_r14 + 184) - 70) = 1;
        result = 1;
    }
    if (a10 != 0) {
        result = (unsigned __int8)((result) | (2));
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_r14 + 184) - 70) = (unsigned __int8)(result);
    }
    *(unsigned int *)(*(unsigned __int64 *)(v_r14 + 184) - 56) = (unsigned int)((unsigned int)(a8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 184) - 48) = v_stack_m50;
    result = ExAllocatePool2(8 + 89, 8, (unsigned int)(0x654C6F49ULL), (unsigned __int8)(v_stack_m6F));
    *(unsigned __int64 *)(result) = v_stack_m48;
    *(unsigned __int64 *)(v_r14 + 160) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 184) - 64) = result;
    goto loc_009D8C7F;
loc_009D8C7F:
    v_stack_m90 = 2;
    v_stack_m98 = 0;
    v_stack_mA0 = (unsigned __int8)(v_stack_m6F);
    a4 = 0;
    result = IopSynchronousServiceTail(*(unsigned __int64 *)(v_stack_m28 + 56), v_r14, v_stack_m68, a4);
    goto loc_009D89FB;
loc_009D8CA7:
    goto loc_009D8A49;
loc_009D8CAF:
    result = ObfDereferenceObject(v_stack_m68, v_r14, v_stack_m68, a4);
    goto loc_009D89FB;
loc_009D8CC3:
    v_stack_mA0 = v_stack_m70;
    result = IopWaitAndAcquireFileObjectLock(v_stack_m68, (unsigned __int8)(v_stack_m6F), (unsigned __int8)(v_r14), a4);
    goto loc_009D8AFC;
loc_009D8CEA:
    result = MmIsDriverVerifying(v_r14, (unsigned __int8)(v_stack_m6F), (unsigned __int8)(v_r14), a4);
    if ((unsigned int)(result) == 0) goto loc_009D8919;
    result = VfFastIoSnapState(v_r14, (unsigned __int8)(v_stack_m6F), (unsigned __int8)(v_r14), a4);
    goto loc_009D891C;
loc_009D8D0A:
    result = VfFastIoCheckState(result, *(unsigned __int64 *)(v_r14 + 184), (unsigned __int8)(v_r14), a4);
    goto loc_009D897F;
loc_009D8D1A:
    result = ObfDereferenceObject(v_stack_m28, *(unsigned __int64 *)(v_r14 + 184), (unsigned __int8)(v_r14), a4);
    goto loc_009D8B10;
loc_009D8D27:
    result = ObfDereferenceObject(v_stack_m28, *(unsigned __int64 *)(v_r14 + 184), (unsigned __int8)(v_r14), a4);
    goto loc_009D8A82;
loc_009D8D34:
    result = IopReleaseFileObjectLock(v_stack_m68, *(unsigned __int64 *)(v_r14 + 184), (unsigned __int8)(v_r14), a4);
    goto loc_009D8A8C;
}
```

## 5. (Beta) C Style

```c
int64_t NtLockFile(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, void *Arg6, void *Arg7, uint32_t Arg8, uint8_t Arg9, uint8_t Arg10)
{
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint8_t v_stack_m54;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint8_t v_stack_m6F;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint8_t v_stack_m97;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint8_t v_stack_mB8;
    uint8_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p28;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (192);
    local_r15 = 0;
    v_stack_m90 = 0;
    v_stack_m60 = 0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    v_stack_m40 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m97 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_mC8 = local_rsp - 88;
    Arg2 = 0;
    result = IopReferenceFileObject(Arg1, Arg2, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m90);
    if (sign_flag) goto loc_009D89FB;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_009D8A19;
    if (((v_stack_m54) & (3)) == 0) goto loc_009D8CAF;
    Arg2 = result;
    if (Arg5 < result) { Arg2 = Arg5; }
    *(uint32_t *)(Arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg2)));
    Arg2 = (uint8_t)((*(uint8_t *)(v_stack_m90 + 0x50)) & (2));
    v_stack_m38 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) != 0) goto loc_009D8816;
    goto loc_009D8858;
loc_009D87CF:
    if (Arg7 < result) { result = Arg7; }
    v_stack_m70 = *(uint64_t *)(arg7);
    if ((*(uint64_t *)(v_stack_m90 + 0xB0)) != 0) goto loc_009D87F6;
loc_009D87F1:
    goto loc_009D88A5;
loc_009D87F6:
    if (((v_stack_p18) & (-2)) == 0) goto loc_009D87F1;
    result = ObfDereferenceObject(v_stack_m90, Arg2, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), v_stack_m90);
    goto loc_009D89FB;
loc_009D8816:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) != 332) goto loc_009D8864;
loc_009D882A:
    if ((uint8_t)(Arg2) == 0) {
        Arg3 = v_stack_p18;
        Arg3 = (Arg3) | (1);
        Arg1 = Arg5;
        Arg2 = *(uint32_t *)(Arg1);
        Arg1 = *(uint32_t *)(Arg2);
        *(uint32_t *)(Arg2) = (uint32_t)(Arg1);
        v_stack_p28 = Arg2;
        v_stack_p18 = Arg3;
    }
    if ((((uint8_t)(Arg6)) & (3)) == 0) goto loc_009D8872;
loc_009D885E:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, v_stack_m90);
loc_009D8864:
    if (((uint16_t)(Arg1)) != 452) goto loc_009D8858;
    goto loc_009D882A;
loc_009D8872:
    Arg1 = result;
    if (Arg6 < result) { Arg1 = Arg6; }
    v_stack_m78 = *(uint64_t *)(arg6);
    if ((((uint8_t)(Arg7)) & (3)) != 0) goto loc_009D885E;
    goto loc_009D87CF;
loc_009D88A5:
    *(uint8_t *)(result + 0x48) = 1;
    Arg3 = 0;
    result = IopSetLockOperationProcess(v_stack_m90, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, v_stack_m90);
    if (sign_flag) goto loc_009D89FB;
    if (Arg2 != 0) goto loc_009D8B20;
loc_009D88DA:
    result = IoGetRelatedDeviceObject(v_stack_m90, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, v_stack_m90);
    if (*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50) == 0) goto loc_009D8A39;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50) + 0x30) == 0) goto loc_009D8A39;
    v_stack_m88 = v_xmm0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x52C10F)))) & (16)) != 0) goto loc_009D8CEA;
loc_009D8919:
loc_009D891C:
    v_stack_mA8 = result;
    v_stack_mB0 = v_stack_m88;
    v_stack_mB8 = Arg10;
    v_stack_mC0 = Arg9;
    v_stack_mC8 = (uint32_t)((uint32_t)(Arg8));
    result = guard_dispatch_icall(v_stack_m90, v_stack_m78, v_stack_m70, *(uint64_t *)(v_stack_m40 + 0xB8));
    if (0 != 0) goto loc_009D8D0A;
loc_009D897F:
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_009D8A33;
    if (((v_stack_p18) & (1)) != 0) goto loc_009D89A4;
    *(uint64_t *)(arg5) = v_xmm0;
    goto loc_009D89B9;
loc_009D89A4:
    *(uint32_t *)(arg5 + 0x4) = (uint32_t)((uint32_t)(v_stack_m80));
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(v_stack_m88));
loc_009D89B9:
    goto loc_009D89D8;
loc_009D89D8:
    if (0 != 0) goto loc_009D8B77;
loc_009D89E1:
    result = ObfDereferenceObject(v_stack_m90, v_stack_m78, v_stack_m70, *(uint64_t *)(v_stack_m40 + 0xB8));
loc_009D89FB:
    return (uint32_t)(v_stack_m88);
loc_009D8A19:
    v_stack_m50 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50) + 0x30));
    v_stack_m48 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x30));
    goto loc_009D88A5;
loc_009D8A33:
loc_009D8A39:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x50)))) & (2)) != 0) goto loc_009D8A9E;
    local_r15 = 0;
loc_009D8A49:
    result = IopResetEvent(*(uint64_t *)(v_stack_m28 + 0x30), v_stack_m78, v_stack_m70, *(uint64_t *)(v_stack_m40 + 0xB8));
    Arg3 = (uint8_t)((0) ^ (1));
    result = IopAllocateIrpExReturn(*(uint64_t *)(v_stack_m28 + 0x38), *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x4C), Arg3, *(uint64_t *)(v_stack_m40 + 0xB8));
    v_stack_m40 = result;
    if (result != 0) goto loc_009D8B9A;
    if (0 != 0) goto loc_009D8D27;
loc_009D8A82:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x30) + 0x50)))) & (2)) != 0) goto loc_009D8D34;
loc_009D8A8C:
    result = ObfDereferenceObject(*(uint64_t *)(v_stack_m28 + 0x30), *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x4C), Arg3, *(uint64_t *)(v_stack_m40 + 0xB8));
    goto loc_009D89FB;
loc_009D8A9E:
    local_r14 = (uint32_t)((result) >> (2));
    local_r14 = (uint8_t)((local_r14) & (1));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m68 + 128, Arg2, Arg3, *(uint64_t *)(v_stack_m40 + 0xB8));
    v_stack_m70 = 0;
    if (1 != 0) goto loc_009D8CC3;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(v_stack_m68, Arg2, Arg3, result);
loc_009D8AFC:
    if (v_stack_m70 == 0) goto loc_009D8CA7;
    if (0 != 0) goto loc_009D8D1A;
loc_009D8B10:
    result = ObfDereferenceObject(v_stack_m68, Arg2, Arg3, result);
    goto loc_009D89FB;
loc_009D8B20:
    v_stack_m28 = 0;
    v_stack_m98 = 0;
    v_stack_mA0 = v_stack_m28;
    result = ObReferenceObjectByHandle(*(uint64_t *)(v_stack_m28 + 0x38), 2, *(uint64_t *)(v_rip + 0x5EE059), (uint8_t)(v_stack_m6F));
    v_stack_m38 = v_stack_m28;
    if (sign_flag) goto loc_009D88DA;
    result = KeResetEvent(v_stack_m28, 2, *(uint64_t *)(v_rip + 0x5EE059), (uint8_t)(v_stack_m6F));
    goto loc_009D88DA;
loc_009D8B77:
    if (((*(uint32_t *)(v_stack_m68 + 0x50)) & (0x8000000ULL)) == 0) {
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_m28;
        result = KeSetEvent(Arg1, Arg2, Arg3, (uint8_t)(v_stack_m6F));
    }
    result = ObfDereferenceObject(v_stack_m28, Arg2, Arg3, (uint8_t)(v_stack_m6F));
    goto loc_009D89E1;
loc_009D8B9A:
    *(uint64_t *)(result + 0xC0) = v_stack_m68;
    *(uint64_t *)(local_r14 + 0x98) = v_stack_m18;
    *(uint8_t *)(local_r14 + 0x40) = (uint8_t)(v_stack_m6F);
    *(uint64_t *)(local_r14 + 0x50) = v_stack_m28;
    *(void **)(local_r14 + 0x48) = Arg5;
    *(uint64_t *)(local_r14 + 0x58) = v_stack_p40;
    *(uint64_t *)(local_r14 + 0x60) = v_stack_p48;
    *(uint16_t *)(*(uint64_t *)(local_r14 + 0xB8) - 0x48) = 273;
    *(uint64_t *)(*(uint64_t *)(local_r14 + 0xB8) - 0x18) = v_stack_m68;
    *(uint8_t *)(*(uint64_t *)(local_r14 + 0xB8) - 0x46) = 0;
    result = 0;
    if (Arg9 != 0) {
        *(uint8_t *)(*(uint64_t *)(local_r14 + 0xB8) - 0x46) = 1;
        result = 1;
    }
    if (Arg10 != 0) {
        result = (uint8_t)((result) | (2));
        *(uint8_t *)(*(uint64_t *)(local_r14 + 0xB8) - 0x46) = (uint8_t)(result);
    }
    *(uint32_t *)(*(uint64_t *)(local_r14 + 0xB8) - 0x38) = (uint32_t)((uint32_t)(Arg8));
    *(uint64_t *)(*(uint64_t *)(local_r14 + 0xB8) - 0x30) = v_stack_m50;
    result = ExAllocatePool2(8 + 89, 8, (uint32_t)(0x654C6F49ULL), (uint8_t)(v_stack_m6F));
    *(uint64_t *)(result) = v_stack_m48;
    *(uint64_t *)(local_r14 + 0xA0) = result;
    *(uint64_t *)(*(uint64_t *)(local_r14 + 0xB8) - 0x40) = result;
    goto loc_009D8C7F;
loc_009D8C7F:
    v_stack_m90 = 2;
    v_stack_m98 = 0;
    v_stack_mA0 = (uint8_t)(v_stack_m6F);
    Arg4 = 0;
    result = IopSynchronousServiceTail(*(uint64_t *)(v_stack_m28 + 0x38), local_r14, v_stack_m68, Arg4);
    goto loc_009D89FB;
loc_009D8CA7:
    goto loc_009D8A49;
loc_009D8CAF:
    result = ObfDereferenceObject(v_stack_m68, local_r14, v_stack_m68, Arg4);
    goto loc_009D89FB;
loc_009D8CC3:
    v_stack_mA0 = v_stack_m70;
    result = IopWaitAndAcquireFileObjectLock(v_stack_m68, (uint8_t)(v_stack_m6F), (uint8_t)(local_r14), Arg4);
    goto loc_009D8AFC;
loc_009D8CEA:
    result = MmIsDriverVerifying(local_r14, (uint8_t)(v_stack_m6F), (uint8_t)(local_r14), Arg4);
    if ((uint32_t)(result) == 0) goto loc_009D8919;
    result = VfFastIoSnapState(local_r14, (uint8_t)(v_stack_m6F), (uint8_t)(local_r14), Arg4);
    goto loc_009D891C;
loc_009D8D0A:
    result = VfFastIoCheckState(result, *(uint64_t *)(local_r14 + 0xB8), (uint8_t)(local_r14), Arg4);
    goto loc_009D897F;
loc_009D8D1A:
    result = ObfDereferenceObject(v_stack_m28, *(uint64_t *)(local_r14 + 0xB8), (uint8_t)(local_r14), Arg4);
    goto loc_009D8B10;
loc_009D8D27:
    result = ObfDereferenceObject(v_stack_m28, *(uint64_t *)(local_r14 + 0xB8), (uint8_t)(local_r14), Arg4);
    goto loc_009D8A82;
loc_009D8D34:
    result = IopReleaseFileObjectLock(v_stack_m68, *(uint64_t *)(local_r14 + 0xB8), (uint8_t)(local_r14), Arg4);
    goto loc_009D8A8C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `32` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |
| `Arg5` | `+ 0x0` | `128` | `R` |
| `Arg5` | `+ 0x4` | `32` | `W` |
| `Arg6` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009D86D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
