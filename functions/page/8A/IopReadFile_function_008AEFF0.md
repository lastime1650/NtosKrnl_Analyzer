# IopReadFile

- RVA: `0x008AEFF0`–`0x008AF994` (길이 `2,468` bytes)
- VA: `0x00000001408AEFF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007FA74`
- 디코드: `589`개 명령, `2,468/2,468` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x008AF0FB` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x008AF152` → [IopMarkApcRoutineIfAsynchronousIo32](../../text/40/IopMarkApcRoutineIfAsynchronousIo32_function_0040EC90.md) (function, `0x0040EC90`)
- `0x008AF176` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x008AF302` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x008AF325` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x008AF36B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008AF391` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008AF3B4` → [IopWaitAndAcquireFileObjectLock](IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x008AF3D2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AF43F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AF447` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x008AF46C` → [MmIsDriverVerifying](../../text/4A/MmIsDriverVerifying_function_004A8770.md) (function, `0x004A8770`)
- `0x008AF478` → [VfFastIoSnapState](../../pagevrfy/BB/VfFastIoSnapState_function_00BB97BC.md) (function, `0x00BB97BC`)
- `0x008AF4B9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008AF4CD` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (function, `0x00BB9440`)
- `0x008AF59D` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x008AF5A5` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AF5AD` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x008AF5D8` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AF5E9` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x008AF612` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AF631` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x008AF645` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x008AF65F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AF66C` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x008AF6C0` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x008AF773` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008AF7C4` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x008AF7EF` → [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) (function, `0x0023B990`)
- `0x008AF890` → [IopSetCopyInformationExtension](../../text/44/IopSetCopyInformationExtension_function_00444EEC.md) (function, `0x00444EEC`)
- `0x008AF89B` → [Feature_3741482297__private_IsEnabledDeviceUsageNoInline](../../text/59/Feature_3741482297__private_IsEnabledDeviceUsageNoInline_function_00598A10.md) (function, `0x00598A10`)
- `0x008AF8C0` → [IopUnlockAndFreeMdl](../../text/29/IopUnlockAndFreeMdl_function_0029F200.md) (function, `0x0029F200`)
- `0x008AF8D9` → [IopFreeCopyObjectsFromDataBuffer](../../text/4C/IopFreeCopyObjectsFromDataBuffer_function_004C201C.md) (function, `0x004C201C`)
- `0x008AF8F4` → [IopExceptionCleanupEx](IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x008AF8FB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008AF965` → [IopSynchronousServiceTail](../8E/IopSynchronousServiceTail_function_008EB440.md) (function, `0x008EB440`)
- `0x008AF982` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008AF98D` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)

### Direct callers
- [NtReadFile](NtReadFile_function_008AEF10.md) at `0x008AEFC3`
- [NtCopyFileChunk](../94/NtCopyFileChunk_function_0094B600.md) at `0x0094BC81`
- [sub_00B4A690](../B4/Unknown_function_00B4A690.md) at `0x00B4A769`

### Static image references
- `0x008AF2D9` → RVA `0x00FC6B80` (`ALMOSTRO`; read)
- `0x008AF456` → RVA `0x00F04A20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **32**
  - `0x008AF0FB` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x008AF152` → [IopMarkApcRoutineIfAsynchronousIo32](../../text/40/IopMarkApcRoutineIfAsynchronousIo32_function_0040EC90.md) (`PAGE` → `.text`)
  - `0x008AF325` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x008AF36B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008AF391` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008AF3D2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AF43F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AF447` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
  - `0x008AF46C` → [MmIsDriverVerifying](../../text/4A/MmIsDriverVerifying_function_004A8770.md) (`PAGE` → `.text`)
  - `0x008AF478` → [VfFastIoSnapState](../../pagevrfy/BB/VfFastIoSnapState_function_00BB97BC.md) (`PAGE` → `PAGEVRFY`)
  - `0x008AF4B9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008AF4CD` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (`PAGE` → `PAGEVRFY`)
  - `0x008AF59D` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x008AF5A5` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AF5AD` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
  - `0x008AF5D8` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AF5E9` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
  - `0x008AF612` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AF631` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (`PAGE` → `.text`)
  - `0x008AF645` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x008AF65F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AF66C` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
  - `0x008AF6C0` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x008AF773` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008AF7C4` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x008AF7EF` → [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) (`PAGE` → `.text`)
  - `0x008AF890` → [IopSetCopyInformationExtension](../../text/44/IopSetCopyInformationExtension_function_00444EEC.md) (`PAGE` → `.text`)
  - `0x008AF89B` → [Feature_3741482297__private_IsEnabledDeviceUsageNoInline](../../text/59/Feature_3741482297__private_IsEnabledDeviceUsageNoInline_function_00598A10.md) (`PAGE` → `.text`)
  - `0x008AF8C0` → [IopUnlockAndFreeMdl](../../text/29/IopUnlockAndFreeMdl_function_0029F200.md) (`PAGE` → `.text`)
  - `0x008AF8D9` → [IopFreeCopyObjectsFromDataBuffer](../../text/4C/IopFreeCopyObjectsFromDataBuffer_function_004C201C.md) (`PAGE` → `.text`)
  - `0x008AF8FB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008AF98D` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008AEFF0  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
008AEFF5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
008AEFFA  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
008AEFFF  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
008AF004  53                              push rbx
008AF005  56                              push rsi
008AF006  57                              push rdi
008AF007  41 54                           push r12
008AF009  41 55                           push r13
008AF00B  41 56                           push r14
008AF00D  41 57                           push r15
008AF00F  48 81 EC B0 00 00 00            sub rsp, 0xb0
008AF016  48 8B DA                        mov rbx, rdx
008AF019  48 8B F1                        mov rsi, rcx
008AF01C  4C 8B A4 24 28 01 00 00         mov r12, qword ptr [rsp + 0x128]
008AF024  33 C0                           xor eax, eax
008AF026  8B F8                           mov edi, eax
008AF028  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008AF02D  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
008AF031  45 32 ED                        xor r13b, r13b
008AF034  44 8B F0                        mov r14d, eax
008AF037  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
008AF03F  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
008AF043  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008AF048  48 39 84 24 38 01 00 00         cmp qword ptr [rsp + 0x138], rax
008AF050  74 25                           je 0x1408af077
008AF052  4D 85 C0                        test r8, r8
008AF055  75 0E                           jne 0x1408af065
008AF057  48 85 D2                        test rdx, rdx
008AF05A  75 09                           jne 0x1408af065
008AF05C  48 39 81 B0 00 00 00            cmp qword ptr [rcx + 0xb0], rax
008AF063  74 12                           je 0x1408af077
008AF065  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008AF06A  4C 8B BC 24 18 01 00 00         mov r15, qword ptr [rsp + 0x118]
008AF072  E9 52 08 00 00                  jmp 0x1408af8c9
008AF077  48 8B 84 24 50 01 00 00         mov rax, qword ptr [rsp + 0x150]
008AF07F  48 85 C0                        test rax, rax
008AF082  74 28                           je 0x1408af0ac
008AF084  48 8B 00                        mov rax, qword ptr [rax]
008AF087  48 85 C0                        test rax, rax
008AF08A  74 20                           je 0x1408af0ac
008AF08C  44 8B BC 24 20 01 00 00         mov r15d, dword ptr [rsp + 0x120]
008AF094  44 39 78 28                     cmp dword ptr [rax + 0x28], r15d
008AF098  73 1A                           jae 0x1408af0b4
008AF09A  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008AF09F  4C 8B BC 24 18 01 00 00         mov r15, qword ptr [rsp + 0x118]
008AF0A7  E9 1D 08 00 00                  jmp 0x1408af8c9
008AF0AC  44 8B BC 24 20 01 00 00         mov r15d, dword ptr [rsp + 0x120]
008AF0B4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AF0BD  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
008AF0C5  0F B6 80 32 02 00 00            movzx eax, byte ptr [rax + 0x232]
008AF0CC  88 44 24 50                     mov byte ptr [rsp + 0x50], al
008AF0D0  8B 41 50                        mov eax, dword ptr [rcx + 0x50]
008AF0D3  A8 02                           test al, 2
008AF0D5  8B 84 24 48 01 00 00            mov eax, dword ptr [rsp + 0x148]
008AF0DC  74 07                           je 0x1408af0e5
008AF0DE  85 C0                           test eax, eax
008AF0E0  78 03                           js 0x1408af0e5
008AF0E2  41 B5 01                        mov r13b, 1
008AF0E5  44 88 6C 24 51                  mov byte ptr [rsp + 0x51], r13b
008AF0EA  25 00 00 00 40                  and eax, 0x40000000
008AF0EF  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
008AF0F6  0F 94 44 24 53                  sete byte ptr [rsp + 0x53]
008AF0FB  E8 20 C0 9E FF                  call 0x14029b120
008AF100  4C 8B C8                        mov r9, rax
008AF103  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008AF108  40 38 7C 24 50                  cmp byte ptr [rsp + 0x50], dil
008AF10D  0F 84 13 01 00 00               je 0x1408af226
008AF113  48 39 BC 24 38 01 00 00         cmp qword ptr [rsp + 0x138], rdi
008AF11B  0F 85 05 01 00 00               jne 0x1408af226
008AF121  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
008AF129  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
008AF133  48 3B CB                        cmp rcx, rbx
008AF136  48 0F 43 CB                     cmovae rcx, rbx
008AF13A  8B 01                           mov eax, dword ptr [rcx]
008AF13C  89 01                           mov dword ptr [rcx], eax
008AF13E  45 0F B6 C5                     movzx r8d, r13b
008AF142  48 8D 94 24 00 01 00 00         lea rdx, [rsp + 0x100]
008AF14A  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
008AF152  E8 39 FB B5 FF                  call 0x14040ec90
008AF157  48 83 BC 24 58 01 00 00 00      cmp qword ptr [rsp + 0x158], 0
008AF160  75 1B                           jne 0x1408af17d
008AF162  41 8B D7                        mov edx, r15d
008AF165  41 B8 01 00 00 00               mov r8d, 1
008AF16B  4C 8B BC 24 18 01 00 00         mov r15, qword ptr [rsp + 0x118]
008AF173  49 8B CF                        mov rcx, r15
008AF176  E8 45 A0 03 00                  call 0x1408e91c0
008AF17B  EB 08                           jmp 0x1408af185
008AF17D  4C 8B BC 24 18 01 00 00         mov r15, qword ptr [rsp + 0x118]
008AF185  48 83 BE B0 00 00 00 00         cmp qword ptr [rsi + 0xb0], 0
008AF18D  74 20                           je 0x1408af1af
008AF18F  48 F7 84 24 00 01 00 00 FE FF FF FF  test qword ptr [rsp + 0x100], -2
008AF19B  74 12                           je 0x1408af1af
008AF19D  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008AF1A2  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
008AF1A6  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
008AF1AA  E9 1A 07 00 00                  jmp 0x1408af8c9
008AF1AF  4D 85 E4                        test r12, r12
008AF1B2  74 21                           je 0x1408af1d5
008AF1B4  41 F6 C4 03                     test r12b, 3
008AF1B8  0F 85 C4 07 00 00               jne 0x1408af982
008AF1BE  48 8B C3                        mov rax, rbx
008AF1C1  4C 3B E3                        cmp r12, rbx
008AF1C4  49 0F 42 C4                     cmovb rax, r12
008AF1C8  90                              nop
008AF1C9  0F B6 00                        movzx eax, byte ptr [rax]
008AF1CC  49 8B 04 24                     mov rax, qword ptr [r12]
008AF1D0  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008AF1D5  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
008AF1DD  48 85 C0                        test rax, rax
008AF1E0  74 0E                           je 0x1408af1f0
008AF1E2  48 3B C3                        cmp rax, rbx
008AF1E5  48 0F 42 D8                     cmovb rbx, rax
008AF1E9  90                              nop
008AF1EA  8B 03                           mov eax, dword ptr [rbx]
008AF1EC  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
008AF1F0  48 8B 9C 24 F8 00 00 00         mov rbx, qword ptr [rsp + 0xf8]
008AF1F8  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
008AF1FD  EB 50                           jmp 0x1408af24f
008AF1FF  4C 8B BC 24 18 01 00 00         mov r15, qword ptr [rsp + 0x118]
008AF207  48 8B B4 24 F0 00 00 00         mov rsi, qword ptr [rsp + 0xf0]
008AF20F  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
008AF214  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
008AF218  44 0F B6 6C 24 51               movzx r13d, byte ptr [rsp + 0x51]
008AF21E  4C 8B F7                        mov r14, rdi
008AF221  E9 A3 06 00 00                  jmp 0x1408af8c9
008AF226  4D 85 E4                        test r12, r12
008AF229  74 09                           je 0x1408af234
008AF22B  49 8B 04 24                     mov rax, qword ptr [r12]
008AF22F  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008AF234  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
008AF23C  4C 8B BC 24 18 01 00 00         mov r15, qword ptr [rsp + 0x118]
008AF244  48 85 C0                        test rax, rax
008AF247  74 06                           je 0x1408af24f
008AF249  8B 00                           mov eax, dword ptr [rax]
008AF24B  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
008AF24F  0F B6 44 24 50                  movzx eax, byte ptr [rsp + 0x50]
008AF254  84 C0                           test al, al
008AF256  74 7C                           je 0x1408af2d4
008AF258  8B 46 50                        mov eax, dword ptr [rsi + 0x50]
008AF25B  A8 08                           test al, 8
008AF25D  74 70                           je 0x1408af2cf
008AF25F  41 0F B7 89 30 01 00 00         movzx ecx, word ptr [r9 + 0x130]
008AF267  44 8B 84 24 20 01 00 00         mov r8d, dword ptr [rsp + 0x120]
008AF26F  66 85 C9                        test cx, cx
008AF272  74 08                           je 0x1408af27c
008AF274  8D 41 FF                        lea eax, [rcx - 1]
008AF277  41 85 C0                        test r8d, eax
008AF27A  75 0E                           jne 0x1408af28a
008AF27C  8B D1                           mov edx, ecx
008AF27E  41 8B 81 98 00 00 00            mov eax, dword ptr [r9 + 0x98]
008AF285  49 85 C7                        test r15, rax
008AF288  74 28                           je 0x1408af2b2
008AF28A  66 85 C9                        test cx, cx
008AF28D  74 0B                           je 0x1408af29a
008AF28F  33 D2                           xor edx, edx
008AF291  41 8B C0                        mov eax, r8d
008AF294  F7 F1                           div ecx
008AF296  85 D2                           test edx, edx
008AF298  75 0E                           jne 0x1408af2a8
008AF29A  8B D1                           mov edx, ecx
008AF29C  41 8B 81 98 00 00 00            mov eax, dword ptr [r9 + 0x98]
008AF2A3  49 85 C7                        test r15, rax
008AF2A6  74 0A                           je 0x1408af2b2
008AF2A8  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008AF2AD  E9 17 06 00 00                  jmp 0x1408af8c9
008AF2B2  4D 85 E4                        test r12, r12
008AF2B5  74 18                           je 0x1408af2cf
008AF2B7  66 85 C9                        test cx, cx
008AF2BA  74 13                           je 0x1408af2cf
008AF2BC  8D 42 FF                        lea eax, [rdx - 1]
008AF2BF  85 44 24 58                     test dword ptr [rsp + 0x58], eax
008AF2C3  74 0A                           je 0x1408af2cf
008AF2C5  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008AF2CA  E9 FA 05 00 00                  jmp 0x1408af8c9
008AF2CF  0F B6 44 24 50                  movzx eax, byte ptr [rsp + 0x50]
008AF2D4  48 85 DB                        test rbx, rbx
008AF2D7  74 51                           je 0x1408af32a
008AF2D9  4C 8B 05 A0 78 71 00            mov r8, qword ptr [rip + 0x7178a0]
008AF2E0  33 C9                           xor ecx, ecx
008AF2E2  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
008AF2E7  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008AF2EC  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
008AF2F1  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008AF2F6  44 0F B6 C8                     movzx r9d, al
008AF2FA  BA 02 00 00 00                  mov edx, 2
008AF2FF  48 8B CB                        mov rcx, rbx
008AF302  E8 A9 9A FB FF                  call 0x140868db0
008AF307  8B D8                           mov ebx, eax
008AF309  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
008AF30E  4C 89 B4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r14
008AF316  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
008AF31A  85 C0                           test eax, eax
008AF31C  0F 88 A7 05 00 00               js 0x1408af8c9
008AF322  49 8B CE                        mov rcx, r14
008AF325  E8 26 90 99 FF                  call 0x140248350
008AF32A  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
008AF32F  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008AF333  48 8B 40 50                     mov rax, qword ptr [rax + 0x50]
008AF337  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
008AF33F  45 84 ED                        test r13b, r13b
008AF342  0F 84 B0 02 00 00               je 0x1408af5f8
008AF348  8B 5E 50                        mov ebx, dword ptr [rsi + 0x50]
008AF34B  83 E3 04                        and ebx, 4
008AF34E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AF357  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008AF35E  90                              nop
008AF35F  48 8D 8E 80 00 00 00            lea rcx, [rsi + 0x80]
008AF366  45 33 C0                        xor r8d, r8d
008AF369  33 D2                           xor edx, edx
008AF36B  E8 C0 0E 96 FF                  call 0x140210230
008AF370  4C 8B C8                        mov r9, rax
008AF373  C6 44 24 52 00                  mov byte ptr [rsp + 0x52], 0
008AF378  B8 01 00 00 00                  mov eax, 1
008AF37D  87 46 74                        xchg dword ptr [rsi + 0x74], eax
008AF380  85 C0                           test eax, eax
008AF382  75 18                           jne 0x1408af39c
008AF384  4D 85 C9                        test r9, r9
008AF387  74 05                           je 0x1408af38e
008AF389  41 C6 41 0A 01                  mov byte ptr [r9 + 0xa], 1
008AF38E  48 8B CE                        mov rcx, rsi
008AF391  E8 8A 06 96 FF                  call 0x14020fa20
008AF396  33 C9                           xor ecx, ecx
008AF398  8B D9                           mov ebx, ecx
008AF39A  EB 1F                           jmp 0x1408af3bb
008AF39C  85 DB                           test ebx, ebx
008AF39E  41 0F 95 C0                     setne r8b
008AF3A2  48 8D 44 24 52                  lea rax, [rsp + 0x52]
008AF3A7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008AF3AC  0F B6 54 24 50                  movzx edx, byte ptr [rsp + 0x50]
008AF3B1  48 8B CE                        mov rcx, rsi
008AF3B4  E8 1F F3 FF FF                  call 0x1408ae6d8
008AF3B9  8B D8                           mov ebx, eax
008AF3BB  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
008AF3BF  80 7C 24 52 00                  cmp byte ptr [rsp + 0x52], 0
008AF3C4  74 16                           je 0x1408af3dc
008AF3C6  4D 85 F6                        test r14, r14
008AF3C9  0F 84 FA 04 00 00               je 0x1408af8c9
008AF3CF  49 8B CE                        mov rcx, r14
008AF3D2  E8 79 9F A4 FF                  call 0x1402f9350
008AF3D7  E9 ED 04 00 00                  jmp 0x1408af8c9
008AF3DC  4D 85 E4                        test r12, r12
008AF3DF  74 0E                           je 0x1408af3ef
008AF3E1  83 7C 24 58 FE                  cmp dword ptr [rsp + 0x58], -2
008AF3E6  75 10                           jne 0x1408af3f8
008AF3E8  83 7C 24 5C FF                  cmp dword ptr [rsp + 0x5c], -1
008AF3ED  75 09                           jne 0x1408af3f8
008AF3EF  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
008AF3F3  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008AF3F8  48 83 7E 30 00                  cmp qword ptr [rsi + 0x30], 0
008AF3FD  0F 84 C1 01 00 00               je 0x1408af5c4
008AF403  48 83 BC 24 58 01 00 00 00      cmp qword ptr [rsp + 0x158], 0
008AF40C  0F 85 B2 01 00 00               jne 0x1408af5c4
008AF412  0F 57 C0                        xorps xmm0, xmm0
008AF415  0F 11 84 24 90 00 00 00         movups xmmword ptr [rsp + 0x90], xmm0
008AF41D  4C 8B A4 24 A0 00 00 00         mov r12, qword ptr [rsp + 0xa0]
008AF425  4D 8B 64 24 10                  mov r12, qword ptr [r12 + 0x10]
008AF42A  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008AF42F  48 C1 E8 20                     shr rax, 0x20
008AF433  85 C0                           test eax, eax
008AF435  79 1F                           jns 0x1408af456
008AF437  4D 85 F6                        test r14, r14
008AF43A  74 08                           je 0x1408af444
008AF43C  49 8B CE                        mov rcx, r14
008AF43F  E8 0C 9F A4 FF                  call 0x1402f9350
008AF444  48 8B CE                        mov rcx, rsi
008AF447  E8 44 16 9A FF                  call 0x140250a90
008AF44C  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008AF451  E9 73 04 00 00                  jmp 0x1408af8c9
008AF456  8B 05 C4 55 65 00               mov eax, dword ptr [rip + 0x6555c4]
008AF45C  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
008AF461  A8 10                           test al, 0x10
008AF463  74 1A                           je 0x1408af47f
008AF465  49 8B 5D 08                     mov rbx, qword ptr [r13 + 8]
008AF469  48 8B CB                        mov rcx, rbx
008AF46C  E8 FF 92 BF FF                  call 0x1404a8770
008AF471  85 C0                           test eax, eax
008AF473  74 0A                           je 0x1408af47f
008AF475  48 8B CB                        mov rcx, rbx
008AF478  E8 3F A3 30 00                  call 0x140bb97bc
008AF47D  EB 02                           jmp 0x1408af481
008AF47F  33 C0                           xor eax, eax
008AF481  48 8B D8                        mov rbx, rax
008AF484  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
008AF489  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
008AF491  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008AF496  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
008AF49B  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
008AF49F  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008AF4A3  41 B1 01                        mov r9b, 1
008AF4A6  44 8B 84 24 20 01 00 00         mov r8d, dword ptr [rsp + 0x120]
008AF4AE  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
008AF4B3  48 8B CE                        mov rcx, rsi
008AF4B6  49 8B C4                        mov rax, r12
008AF4B9  E8 12 B6 E0 FF                  call 0x1406baad0
008AF4BE  44 0F B6 E8                     movzx r13d, al
008AF4C2  48 85 DB                        test rbx, rbx
008AF4C5  74 0B                           je 0x1408af4d2
008AF4C7  49 8B D4                        mov rdx, r12
008AF4CA  48 8B CB                        mov rcx, rbx
008AF4CD  E8 6E 9F 30 00                  call 0x140bb9440
008AF4D2  45 84 ED                        test r13b, r13b
008AF4D5  0F 84 E3 00 00 00               je 0x1408af5be
008AF4DB  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
008AF4E2  85 C0                           test eax, eax
008AF4E4  74 12                           je 0x1408af4f8
008AF4E6  3D 05 00 00 80                  cmp eax, 0x80000005
008AF4EB  74 0B                           je 0x1408af4f8
008AF4ED  3D 11 00 00 C0                  cmp eax, 0xc0000011
008AF4F2  0F 85 C6 00 00 00               jne 0x1408af5be
008AF4F8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AF501  48 FF 80 80 03 00 00            inc qword ptr [rax + 0x380]
008AF508  65 FF 04 25 DC 2E 00 00         inc dword ptr gs:[0x2edc]
008AF510  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008AF519  8B 8C 24 98 00 00 00            mov ecx, dword ptr [rsp + 0x98]
008AF520  48 01 88 98 03 00 00            add qword ptr [rax + 0x398], rcx
008AF527  65 48 01 0C 25 E8 2E 00 00      add qword ptr gs:[0x2ee8], rcx
008AF530  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
008AF538  0F 10 84 24 90 00 00 00         movups xmm0, xmmword ptr [rsp + 0x90]
008AF540  0F 11 00                        movups xmmword ptr [rax], xmm0
008AF543  44 0F B6 6C 24 51               movzx r13d, byte ptr [rsp + 0x51]
008AF549  EB 36                           jmp 0x1408af581
008AF54B  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
008AF552  48 C7 84 24 98 00 00 00 00 00 00 00  mov qword ptr [rsp + 0x98], 0
008AF55E  4C 8B BC 24 18 01 00 00         mov r15, qword ptr [rsp + 0x118]
008AF566  48 8B B4 24 F0 00 00 00         mov rsi, qword ptr [rsp + 0xf0]
008AF56E  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
008AF573  44 0F B6 6C 24 51               movzx r13d, byte ptr [rsp + 0x51]
008AF579  4C 8B B4 24 80 00 00 00         mov r14, qword ptr [rsp + 0x80]
008AF581  48 83 BC 24 F8 00 00 00 00      cmp qword ptr [rsp + 0xf8], 0
008AF58A  74 1E                           je 0x1408af5aa
008AF58C  F7 46 50 00 00 00 08            test dword ptr [rsi + 0x50], 0x8000000
008AF593  75 0D                           jne 0x1408af5a2
008AF595  45 33 C0                        xor r8d, r8d
008AF598  33 D2                           xor edx, edx
008AF59A  49 8B CE                        mov rcx, r14
008AF59D  E8 6E FD A8 FF                  call 0x14033f310
008AF5A2  49 8B CE                        mov rcx, r14
008AF5A5  E8 A6 9D A4 FF                  call 0x1402f9350
008AF5AA  48 8B CE                        mov rcx, rsi
008AF5AD  E8 DE 14 9A FF                  call 0x140250a90
008AF5B2  8B 9C 24 90 00 00 00            mov ebx, dword ptr [rsp + 0x90]
008AF5B9  E9 0B 03 00 00                  jmp 0x1408af8c9
008AF5BE  44 0F B6 6C 24 51               movzx r13d, byte ptr [rsp + 0x51]
008AF5C4  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
008AF5C9  83 7C 24 5C 00                  cmp dword ptr [rsp + 0x5c], 0
008AF5CE  7D 51                           jge 0x1408af621
008AF5D0  4D 85 F6                        test r14, r14
008AF5D3  74 08                           je 0x1408af5dd
008AF5D5  49 8B CE                        mov rcx, r14
008AF5D8  E8 73 9D A4 FF                  call 0x1402f9350
008AF5DD  45 84 ED                        test r13b, r13b
008AF5E0  0F 84 C2 FC FF FF               je 0x1408af2a8
008AF5E6  48 8B CE                        mov rcx, rsi
008AF5E9  E8 A2 14 9A FF                  call 0x140250a90
008AF5EE  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008AF5F3  E9 D1 02 00 00                  jmp 0x1408af8c9
008AF5F8  4D 85 E4                        test r12, r12
008AF5FB  75 CC                           jne 0x1408af5c9
008AF5FD  F7 46 50 80 02 00 00            test dword ptr [rsi + 0x50], 0x280
008AF604  75 C3                           jne 0x1408af5c9
008AF606  4D 85 F6                        test r14, r14
008AF609  0F 84 99 FC FF FF               je 0x1408af2a8
008AF60F  49 8B CE                        mov rcx, r14
008AF612  E8 39 9D A4 FF                  call 0x1402f9350
008AF617  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008AF61C  E9 A8 02 00 00                  jmp 0x1408af8c9
008AF621  4C 8B A4 24 38 01 00 00         mov r12, qword ptr [rsp + 0x138]
008AF629  4D 85 E4                        test r12, r12
008AF62C  75 08                           jne 0x1408af636
008AF62E  48 8B CE                        mov rcx, rsi
008AF631  E8 BA DF 9E FF                  call 0x14029d5f0
008AF636  45 0F B6 C5                     movzx r8d, r13b
008AF63A  41 80 F0 01                     xor r8b, 1
008AF63E  0F B6 53 4C                     movzx edx, byte ptr [rbx + 0x4c]
008AF642  48 8B CB                        mov rcx, rbx
008AF645  E8 D6 80 95 FF                  call 0x140207720
008AF64A  48 8B F8                        mov rdi, rax
008AF64D  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008AF652  48 85 C0                        test rax, rax
008AF655  75 24                           jne 0x1408af67b
008AF657  4D 85 F6                        test r14, r14
008AF65A  74 08                           je 0x1408af664
008AF65C  49 8B CE                        mov rcx, r14
008AF65F  E8 EC 9C A4 FF                  call 0x1402f9350
008AF664  45 84 ED                        test r13b, r13b
008AF667  74 08                           je 0x1408af671
008AF669  48 8B CE                        mov rcx, rsi
008AF66C  E8 1F 14 9A FF                  call 0x140250a90
008AF671  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008AF676  E9 4E 02 00 00                  jmp 0x1408af8c9
008AF67B  48 89 B0 C0 00 00 00            mov qword ptr [rax + 0xc0], rsi
008AF682  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
008AF68A  48 89 87 98 00 00 00            mov qword ptr [rdi + 0x98], rax
008AF691  33 D2                           xor edx, edx
008AF693  48 89 97 A0 00 00 00            mov qword ptr [rdi + 0xa0], rdx
008AF69A  0F B6 44 24 50                  movzx eax, byte ptr [rsp + 0x50]
008AF69F  88 47 40                        mov byte ptr [rdi + 0x40], al
008AF6A2  88 57 41                        mov byte ptr [rdi + 0x41], dl
008AF6A5  88 57 44                        mov byte ptr [rdi + 0x44], dl
008AF6A8  48 89 57 68                     mov qword ptr [rdi + 0x68], rdx
008AF6AC  89 57 10                        mov dword ptr [rdi + 0x10], edx
008AF6AF  4C 89 77 50                     mov qword ptr [rdi + 0x50], r14
008AF6B3  4D 85 E4                        test r12, r12
008AF6B6  74 39                           je 0x1408af6f1
008AF6B8  BA 49 6F 52 49                  mov edx, 0x49526f49
008AF6BD  49 8B CC                        mov rcx, r12
008AF6C0  E8 4B 10 96 FF                  call 0x140210710
008AF6C5  81 4F 10 00 00 20 00            or dword ptr [rdi + 0x10], 0x200000
008AF6CC  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
008AF6D4  48 89 47 48                     mov qword ptr [rdi + 0x48], rax
008AF6D8  4C 89 A4 24 08 01 00 00         mov qword ptr [rsp + 0x108], r12
008AF6E0  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
008AF6E8  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008AF6ED  33 D2                           xor edx, edx
008AF6EF  EB 1D                           jmp 0x1408af70e
008AF6F1  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
008AF6F9  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
008AF6FE  48 89 4F 48                     mov qword ptr [rdi + 0x48], rcx
008AF702  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
008AF70A  48 89 47 58                     mov qword ptr [rdi + 0x58], rax
008AF70E  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
008AF716  48 89 47 60                     mov qword ptr [rdi + 0x60], rax
008AF71A  4C 8B A7 B8 00 00 00            mov r12, qword ptr [rdi + 0xb8]
008AF721  41 C7 44 24 B8 03 00 00 00      mov dword ptr [r12 - 0x48], 3
008AF72A  49 89 74 24 E8                  mov qword ptr [r12 - 0x18], rsi
008AF72F  48 89 57 18                     mov qword ptr [rdi + 0x18], rdx
008AF733  48 89 57 08                     mov qword ptr [rdi + 8], rdx
008AF737  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
008AF73A  A8 04                           test al, 4
008AF73C  74 63                           je 0x1408af7a1
008AF73E  8B 9C 24 20 01 00 00            mov ebx, dword ptr [rsp + 0x120]
008AF745  85 DB                           test ebx, ebx
008AF747  74 4F                           je 0x1408af798
008AF749  48 83 BC 24 58 01 00 00 00      cmp qword ptr [rsp + 0x158], 0
008AF752  74 11                           je 0x1408af765
008AF754  4C 89 7F 18                     mov qword ptr [rdi + 0x18], r15
008AF758  83 4F 10 50                     or dword ptr [rdi + 0x10], 0x50
008AF75C  4C 89 7F 70                     mov qword ptr [rdi + 0x70], r15
008AF760  E9 EB 00 00 00                  jmp 0x1408af850
008AF765  48 8B D3                        mov rdx, rbx
008AF768  B9 49 00 00 00                  mov ecx, 0x49
008AF76D  41 B8 49 6F 53 42               mov r8d, 0x42536f49
008AF773  E8 78 29 2D 00                  call 0x140b820f0
008AF778  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
008AF77C  48 85 C0                        test rax, rax
008AF77F  75 0A                           jne 0x1408af78b
008AF781  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008AF786  E9 3E 01 00 00                  jmp 0x1408af8c9
008AF78B  83 4F 10 70                     or dword ptr [rdi + 0x10], 0x70
008AF78F  4C 89 7F 70                     mov qword ptr [rdi + 0x70], r15
008AF793  E9 B8 00 00 00                  jmp 0x1408af850
008AF798  83 4F 10 50                     or dword ptr [rdi + 0x10], 0x50
008AF79C  E9 AF 00 00 00                  jmp 0x1408af850
008AF7A1  A8 10                           test al, 0x10
008AF7A3  74 7B                           je 0x1408af820
008AF7A5  8B 9C 24 20 01 00 00            mov ebx, dword ptr [rsp + 0x120]
008AF7AC  85 DB                           test ebx, ebx
008AF7AE  0F 84 9C 00 00 00               je 0x1408af850
008AF7B4  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
008AF7B9  41 B1 01                        mov r9b, 1
008AF7BC  45 33 C0                        xor r8d, r8d
008AF7BF  8B D3                           mov edx, ebx
008AF7C1  49 8B CF                        mov rcx, r15
008AF7C4  E8 27 F4 9E FF                  call 0x14029ebf0
008AF7C9  48 85 C0                        test rax, rax
008AF7CC  0F 84 B6 01 00 00               je 0x1408af988
008AF7D2  0F B6 54 24 50                  movzx edx, byte ptr [rsp + 0x50]
008AF7D7  48 83 BC 24 58 01 00 00 00      cmp qword ptr [rsp + 0x158], 0
008AF7E0  B9 00 00 00 00                  mov ecx, 0
008AF7E5  0F 45 D1                        cmovne edx, ecx
008AF7E8  44 8D 41 01                     lea r8d, [rcx + 1]
008AF7EC  48 8B C8                        mov rcx, rax
008AF7EF  E8 9C C1 98 FF                  call 0x14023b990
008AF7F4  EB 5A                           jmp 0x1408af850
008AF7F6  8B D8                           mov ebx, eax
008AF7F8  4C 8B BC 24 18 01 00 00         mov r15, qword ptr [rsp + 0x118]
008AF800  48 8B B4 24 F0 00 00 00         mov rsi, qword ptr [rsp + 0xf0]
008AF808  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
008AF80D  44 0F B6 6C 24 51               movzx r13d, byte ptr [rsp + 0x51]
008AF813  4C 8B B4 24 80 00 00 00         mov r14, qword ptr [rsp + 0x80]
008AF81B  E9 A9 00 00 00                  jmp 0x1408af8c9
008AF820  4C 89 7F 70                     mov qword ptr [rdi + 0x70], r15
008AF824  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
008AF82C  48 85 C9                        test rcx, rcx
008AF82F  74 1F                           je 0x1408af850
008AF831  48 8B 01                        mov rax, qword ptr [rcx]
008AF834  48 85 C0                        test rax, rax
008AF837  74 17                           je 0x1408af850
008AF839  48 89 47 08                     mov qword ptr [rdi + 8], rax
008AF83D  48 89 11                        mov qword ptr [rcx], rdx
008AF840  48 83 BC 24 38 01 00 00 00      cmp qword ptr [rsp + 0x138], 0
008AF849  74 05                           je 0x1408af850
008AF84B  48 83 4F 60 01                  or qword ptr [rdi + 0x60], 1
008AF850  8B 4F 10                        mov ecx, dword ptr [rdi + 0x10]
008AF853  0F BA E9 08                     bts ecx, 8
008AF857  89 4F 10                        mov dword ptr [rdi + 0x10], ecx
008AF85A  8B 46 50                        mov eax, dword ptr [rsi + 0x50]
008AF85D  A8 08                           test al, 8
008AF85F  74 06                           je 0x1408af867
008AF861  83 C9 01                        or ecx, 1
008AF864  89 4F 10                        mov dword ptr [rdi + 0x10], ecx
008AF867  83 BC 24 88 00 00 00 00         cmp dword ptr [rsp + 0x88], 0
008AF86F  75 07                           jne 0x1408af878
008AF871  0F BA E9 0B                     bts ecx, 0xb
008AF875  89 4F 10                        mov dword ptr [rdi + 0x10], ecx
008AF878  48 8B 94 24 58 01 00 00         mov rdx, qword ptr [rsp + 0x158]
008AF880  48 85 D2                        test rdx, rdx
008AF883  74 7D                           je 0x1408af902
008AF885  C6 47 40 00                     mov byte ptr [rdi + 0x40], 0
008AF889  4C 89 7F 70                     mov qword ptr [rdi + 0x70], r15
008AF88D  48 8B CF                        mov rcx, rdi
008AF890  E8 57 56 B9 FF                  call 0x140444eec
008AF895  8B D8                           mov ebx, eax
008AF897  85 C0                           test eax, eax
008AF899  79 67                           jns 0x1408af902
008AF89B  E8 70 91 CE FF                  call 0x140598a10
008AF8A0  85 C0                           test eax, eax
008AF8A2  74 25                           je 0x1408af8c9
008AF8A4  45 33 E4                        xor r12d, r12d
008AF8A7  4C 89 67 18                     mov qword ptr [rdi + 0x18], r12
008AF8AB  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008AF8B0  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
008AF8B3  A8 10                           test al, 0x10
008AF8B5  74 12                           je 0x1408af8c9
008AF8B7  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
008AF8BB  48 85 C9                        test rcx, rcx
008AF8BE  74 09                           je 0x1408af8c9
008AF8C0  E8 3B F9 9E FF                  call 0x14029f200
008AF8C5  4C 89 67 08                     mov qword ptr [rdi + 8], r12
008AF8C9  48 83 BC 24 58 01 00 00 00      cmp qword ptr [rsp + 0x158], 0
008AF8D2  74 0A                           je 0x1408af8de
008AF8D4  B2 01                           mov dl, 1
008AF8D6  49 8B CF                        mov rcx, r15
008AF8D9  E8 3E 27 C1 FF                  call 0x1404c201c
008AF8DE  48 8B CE                        mov rcx, rsi
008AF8E1  48 85 FF                        test rdi, rdi
008AF8E4  74 15                           je 0x1408af8fb
008AF8E6  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
008AF8EB  45 33 C9                        xor r9d, r9d
008AF8EE  4D 8B C6                        mov r8, r14
008AF8F1  48 8B D7                        mov rdx, rdi
008AF8F4  E8 CF EC FF FF                  call 0x1408ae5c8
008AF8F9  EB 71                           jmp 0x1408af96c
008AF8FB  E8 50 9A A4 FF                  call 0x1402f9350
008AF900  EB 6A                           jmp 0x1408af96c
008AF902  8B 84 24 20 01 00 00            mov eax, dword ptr [rsp + 0x120]
008AF909  41 89 44 24 C0                  mov dword ptr [r12 - 0x40], eax
008AF90E  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
008AF912  41 89 44 24 C8                  mov dword ptr [r12 - 0x38], eax
008AF917  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008AF91C  49 89 44 24 D0                  mov qword ptr [r12 - 0x30], rax
008AF921  48 8B 86 D0 00 00 00            mov rax, qword ptr [rsi + 0xd0]
008AF928  48 85 C0                        test rax, rax
008AF92B  74 13                           je 0x1408af940
008AF92D  8B 00                           mov eax, dword ptr [rax]
008AF92F  A8 10                           test al, 0x10
008AF931  74 0D                           je 0x1408af940
008AF933  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008AF938  8B 40 08                        mov eax, dword ptr [rax + 8]
008AF93B  41 89 44 24 CC                  mov dword ptr [r12 - 0x34], eax
008AF940  33 C0                           xor eax, eax
008AF942  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008AF946  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
008AF94B  0F B6 44 24 50                  movzx eax, byte ptr [rsp + 0x50]
008AF950  88 44 24 20                     mov byte ptr [rsp + 0x20], al
008AF954  44 0F B6 4C 24 53               movzx r9d, byte ptr [rsp + 0x53]
008AF95A  4C 8B C6                        mov r8, rsi
008AF95D  48 8B D7                        mov rdx, rdi
008AF960  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
008AF965  E8 D6 BA 03 00                  call 0x1408eb440
008AF96A  8B D8                           mov ebx, eax
008AF96C  8B C3                           mov eax, ebx
008AF96E  48 81 C4 B0 00 00 00            add rsp, 0xb0
008AF975  41 5F                           pop r15
008AF977  41 5E                           pop r14
008AF979  41 5D                           pop r13
008AF97B  41 5C                           pop r12
008AF97D  5F                              pop rdi
008AF97E  5E                              pop rsi
008AF97F  5B                              pop rbx
008AF980  C3                              ret
008AF981  CC                              int3
008AF982  E8 49 A6 FE FF                  call 0x140899fd0
008AF987  90                              nop
008AF988  B9 9A 00 00 C0                  mov ecx, 0xc000009a
008AF98D  E8 BE 70 A4 FF                  call 0x1402f6a50
008AF992  90                              nop
008AF993  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopReadFile(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, unsigned int a12, __int64 a13, __int64 a14)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int8 v_stack_m95;
    unsigned __int8 v_stack_m96;
    unsigned __int8 v_stack_m97;
    unsigned __int8 v_stack_m98;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (176);
    result = 0;
    v_stack_m70 = 0;
    v_stack_m94 = 0;
    v_r13 = 0;
    v_stack_m68 = 0;
    v_stack_m88 = 0;
    v_stack_m90 = 0;
    if (a10 == 0) goto loc_008AF077;
    if (a3 != 0) goto loc_008AF065;
    if (a2 != 0) goto loc_008AF065;
    if ((*(unsigned __int64 *)(a1 + 176)) == 0) goto loc_008AF077;
loc_008AF065:
    goto loc_008AF8C9;
loc_008AF077:
    if (a13 == 0) goto loc_008AF0AC;
    if (*(unsigned __int64 *)(a13) == 0) goto loc_008AF0AC;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a13) + 40)) >= ((unsigned int)((unsigned int)(a7)))) goto loc_008AF0B4;
    goto loc_008AF8C9;
loc_008AF0AC:
loc_008AF0B4:
    v_stack_m40 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m98 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (2)) == 0) goto loc_008AF0E5;
    if (!(sign_flag)) {
        v_r13 = 1;
    }
    v_stack_m97 = (unsigned __int8)(v_r13);
    result = (unsigned int)(((unsigned int)(a12)) & (0x40000000ULL));
    v_stack_m60 = (unsigned int)(result);
    result = IoGetRelatedDeviceObject(a1, a2, a3, a4);
    v_stack_m80 = result;
    if (v_stack_m98 == 0) goto loc_008AF226;
    if (a10 != 0) goto loc_008AF226;
    if (a5 >= ((unsigned int)(0xC000000DULL))) { a5 = (unsigned int)(0xC000000DULL); }
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(*(unsigned int *)(a5)));
    result = IopMarkApcRoutineIfAsynchronousIo32(a5, v_stack_p18, (unsigned __int8)(v_r13), result);
    if (a14 != 0) goto loc_008AF17D;
    result = ProbeForWrite(a6, (unsigned int)((unsigned int)((unsigned int)(a7))), 1, result);
    goto loc_008AF185;
loc_008AF17D:
loc_008AF185:
    if ((*(unsigned __int64 *)(a1 + 176)) == 0) goto loc_008AF1AF;
    if (((v_stack_p18) & (-2)) == 0) goto loc_008AF1AF;
    v_stack_m94 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_008AF8C9;
loc_008AF1AF:
    if (a8 == 0) goto loc_008AF1D5;
    if ((((unsigned __int8)(a8)) & (3)) != 0) goto loc_008AF982;
    result = (unsigned int)(v_stack_m94);
    if (a8 < ((unsigned int)(v_stack_m94))) { result = a8; }
    v_stack_m90 = *(unsigned __int64 *)(a8);
loc_008AF1D5:
    result = a9;
    v_rbx = (unsigned int)(v_stack_m94);
    if (a9 != 0) {
        v_rbx = (unsigned int)(v_stack_m94);
        if (a9 < ((unsigned int)(v_stack_m94))) { v_rbx = a9; }
        result = *(unsigned int *)(v_rbx);
        v_stack_m88 = (unsigned int)(result);
    }
    goto loc_008AF24F;
loc_008AF226:
    if (a8 != 0) {
        result = *(unsigned __int64 *)(a8);
        v_stack_m90 = result;
    }
    result = a9;
    if (a9 != 0) {
        result = *(unsigned int *)(a9);
        v_stack_m88 = (unsigned int)(result);
    }
    if ((unsigned __int8)(v_stack_m98) == 0) goto loc_008AF2D4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (8)) == 0) goto loc_008AF2CF;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m80 + 304)) == 0) goto loc_008AF27C;
    if ((((unsigned int)((unsigned int)(a7))) & ((unsigned int)(*(unsigned __int16 *)(v_stack_m80 + 304) - 1))) != 0) goto loc_008AF28A;
loc_008AF27C:
    if (((a6) & ((unsigned int)(*(unsigned int *)(v_stack_m80 + 152)))) == 0) goto loc_008AF2B2;
loc_008AF28A:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m80 + 304)) == 0) goto loc_008AF29A;
    a2 = 0;
    if (0 != 0) goto loc_008AF2A8;
loc_008AF29A:
    if (((a6) & ((unsigned int)(*(unsigned int *)(v_stack_m80 + 152)))) == 0) goto loc_008AF2B2;
loc_008AF2A8:
    goto loc_008AF8C9;
loc_008AF2B2:
    if (a8 == 0) goto loc_008AF2CF;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m80 + 304)) == 0) goto loc_008AF2CF;
    if (((v_stack_m90) & ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m80 + 304))) - 1))) == 0) goto loc_008AF2CF;
    goto loc_008AF8C9;
loc_008AF2CF:
loc_008AF2D4:
    if ((unsigned int)(0xC000000DULL) == 0) goto loc_008AF32A;
    a1 = 0;
    v_stack_m78 = 0;
    v_stack_mC0 = 0;
    v_stack_mC8 = v_stack_m78;
    result = ObReferenceObjectByHandle((unsigned int)(0xC000000DULL), 2, *(unsigned __int64 *)(v_rip + 7436448), (unsigned __int8)(v_stack_m98));
    v_stack_m68 = v_stack_m78;
    v_stack_m94 = (unsigned int)(result);
    if (sign_flag) goto loc_008AF8C9;
    result = KeResetEvent(v_stack_m78, 2, *(unsigned __int64 *)(v_rip + 7436448), (unsigned __int8)(v_stack_m98));
loc_008AF32A:
    v_stack_m48 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 8) + 80);
    if ((unsigned __int8)(v_r13) == 0) goto loc_008AF5F8;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 80))) & (4));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 128, a2, a3, (unsigned __int8)(v_stack_m98));
    v_stack_m96 = 0;
    if (1 != 0) goto loc_008AF39C;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(0, a2, a3, result);
    a1 = 0;
    goto loc_008AF3BB;
loc_008AF39C:
    a3 = (0 != 0) ? 1 : 0;
    v_stack_mC8 = v_stack_m96;
    result = IopWaitAndAcquireFileObjectLock(0, v_stack_m98, a3, result);
loc_008AF3BB:
    v_stack_m94 = (unsigned int)((unsigned int)((unsigned int)(result)));
    if (v_stack_m96 == 0) goto loc_008AF3DC;
    if (v_stack_m78 == 0) goto loc_008AF8C9;
    result = ObfDereferenceObject(v_stack_m78, v_stack_m98, a3, result);
    goto loc_008AF8C9;
loc_008AF3DC:
    if (a8 == 0) goto loc_008AF3EF;
    if (v_stack_m90 != -2) goto loc_008AF3F8;
    if (v_stack_m8C == -1) {
        result = *(unsigned __int64 *)(a1 + 104);
        v_stack_m90 = result;
    }
    if ((*(unsigned __int64 *)(a1 + 48)) == 0) goto loc_008AF5C4;
    if (a14 != 0) goto loc_008AF5C4;
    v_stack_m58 = v_xmm0;
    result = (v_stack_m90) >> (32);
    if (!sign_flag) goto loc_008AF456;
    if (v_stack_m78 != 0) {
        a1 = v_stack_m78;
        result = ObfDereferenceObject(a1, v_stack_m98, a3, result);
    }
    result = IopReleaseFileObjectLock(a1, v_stack_m98, a3, result);
    goto loc_008AF8C9;
loc_008AF456:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 6641092)))) & (16)) == 0) goto loc_008AF47F;
    result = MmIsDriverVerifying(*(unsigned __int64 *)(v_stack_m80 + 8), v_stack_m98, a3, result);
    if ((unsigned int)(result) == 0) goto loc_008AF47F;
    result = VfFastIoSnapState(*(unsigned __int64 *)(v_stack_m80 + 8), v_stack_m98, a3, result);
    goto loc_008AF481;
loc_008AF47F:
    result = 0;
loc_008AF481:
    v_stack_mB0 = v_stack_m80;
    v_stack_mB8 = v_stack_m58;
    v_stack_mC0 = a6;
    v_stack_mC8 = (unsigned int)((unsigned int)(v_stack_m88));
    result = guard_dispatch_icall(a1, v_stack_m90, (unsigned int)(a7), 1);
    if (0 != 0) {
        a2 = *(unsigned __int64 *)(v_stack_m48 + 16);
        a1 = 0;
        result = VfFastIoCheckState(a1, a2, (unsigned int)(a7), 1);
    }
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_008AF5BE;
    if ((unsigned int)((unsigned int)(v_stack_m58)) == 0) goto loc_008AF4F8;
    if (((unsigned int)((unsigned int)(v_stack_m58))) == 0x80000005ULL) goto loc_008AF4F8;
    if (((unsigned int)((unsigned int)(v_stack_m58))) != 0xC0000011ULL) goto loc_008AF5BE;
loc_008AF4F8:
    *(unsigned __int64 *)(a5) = v_xmm0;
    goto loc_008AF581;
loc_008AF581:
    if (v_stack_p10 == 0) goto loc_008AF5AA;
    result = a5;
    if (((*(unsigned int *)(a1 + 80)) & (0x8000000ULL)) == 0) {
        a3 = 0;
        a2 = 0;
        a1 = v_stack_m78;
        result = KeSetEvent(a1, a2, a3, 1);
    }
    result = ObfDereferenceObject(v_stack_m78, a2, a3, 1);
loc_008AF5AA:
    result = IopReleaseFileObjectLock(a1, a2, a3, 1);
    goto loc_008AF8C9;
loc_008AF5BE:
loc_008AF5C4:
loc_008AF5C9:
    if (v_stack_m8C >= 0) goto loc_008AF621;
    if (v_stack_m78 != 0) {
        a1 = v_stack_m78;
        result = ObfDereferenceObject(a1, a2, a3, 1);
    }
    if ((unsigned __int8)(v_stack_m97) == 0) goto loc_008AF2A8;
    result = IopReleaseFileObjectLock(a1, a2, a3, 1);
    goto loc_008AF8C9;
loc_008AF5F8:
    if (*(unsigned __int64 *)(v_stack_m48 + 16) != 0) goto loc_008AF5C9;
    if (((*(unsigned int *)(a1 + 80)) & (640)) != 0) goto loc_008AF5C9;
    if (v_stack_m78 == 0) goto loc_008AF2A8;
    result = ObfDereferenceObject(v_stack_m78, a2, a3, 1);
    goto loc_008AF8C9;
loc_008AF621:
    if (a10 == 0) {
        a1 = a1;
        result = IopResetEvent(a1, a2, a3, 1);
    }
    a3 = (unsigned __int8)(((unsigned __int8)(v_stack_m97)) ^ (1));
    result = IopAllocateIrpExReturn((unsigned int)(0xC000000DULL), *(unsigned __int8 *)((unsigned int)(0xC000000DULL) + 76), a3, 1);
    v_stack_m70 = result;
    if (result != 0) goto loc_008AF67B;
    if (v_stack_m78 != 0) {
        a1 = v_stack_m78;
        result = ObfDereferenceObject(a1, *(unsigned __int8 *)((unsigned int)(0xC000000DULL) + 76), a3, 1);
    }
    if ((unsigned __int8)(v_stack_m97) != 0) {
        a1 = a1;
        result = IopReleaseFileObjectLock(a1, *(unsigned __int8 *)((unsigned int)(0xC000000DULL) + 76), a3, 1);
    }
    goto loc_008AF8C9;
loc_008AF67B:
    *(unsigned __int64 *)(result + 192) = a1;
    *(unsigned __int64 *)(result + 152) = v_stack_m40;
    a2 = 0;
    *(unsigned __int64 *)(result + 160) = 0;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)(v_stack_m98);
    *(unsigned __int8 *)(result + 65) = 0;
    *(unsigned __int8 *)(result + 68) = 0;
    *(unsigned __int64 *)(result + 104) = 0;
    *(unsigned int *)(result + 16) = 0;
    *(unsigned __int64 *)(result + 80) = v_stack_m78;
    if (a10 == 0) goto loc_008AF6F1;
    result = ObfReferenceObjectWithTag(a10, (unsigned int)(0x49526F49ULL), a3, 1);
    *(unsigned __int64 *)(result + 72) = a11;
    v_stack_p20 = a10;
    v_stack_m78 = a5;
    a2 = 0;
    goto loc_008AF70E;
loc_008AF6F1:
    v_stack_m78 = a5;
    *(unsigned __int64 *)(result + 72) = a5;
    *(unsigned __int64 *)(result + 88) = v_stack_p18;
loc_008AF70E:
    *(unsigned __int64 *)(result + 96) = v_stack_p20;
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 72) = 3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 24) = a1;
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)(0xC000009AULL) + 48)))) & (4)) == 0) goto loc_008AF7A1;
    if ((unsigned int)((unsigned int)(a7)) == 0) goto loc_008AF798;
    if (a14 == 0) goto loc_008AF765;
    *(unsigned __int64 *)(result + 24) = a6;
    *(unsigned __int64 *)(result + 112) = a6;
    goto loc_008AF850;
loc_008AF765:
    result = ExAllocatePool2(73, (unsigned int)(a7), (unsigned int)(0x42536F49ULL), 1);
    *(unsigned __int64 *)(result + 24) = result;
    if (result != 0) goto loc_008AF78B;
    goto loc_008AF8C9;
loc_008AF78B:
    *(unsigned __int64 *)(result + 112) = a6;
    goto loc_008AF850;
loc_008AF798:
    goto loc_008AF850;
loc_008AF7A1:
    if ((((unsigned __int8)(result)) & (16)) == 0) goto loc_008AF820;
    if ((unsigned int)((unsigned int)(a7)) == 0) goto loc_008AF850;
    v_stack_mC8 = result;
    a3 = 0;
    result = IoAllocateMdl(a6, (unsigned int)((unsigned int)((unsigned int)(a7))), a3, 1);
    if (result == 0) goto loc_008AF988;
    a2 = v_stack_m98;
    if (a14 != 0) { a2 = 0; }
    result = MmProbeAndLockPages(result, a2, 0 + 1, 1);
    goto loc_008AF850;
loc_008AF820:
    *(unsigned __int64 *)(result + 112) = a6;
    if (a13 == 0) goto loc_008AF850;
    if (*(unsigned __int64 *)(a13) == 0) goto loc_008AF850;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a13);
    *(unsigned __int64 *)(a13) = a2;
    if (a10 != 0) {
    }
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 16)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (8)) != 0) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 16))) | (1));
        *(unsigned int *)(result + 16) = (unsigned int)(a1);
    }
    if (v_stack_m60 == 0) {
        *(unsigned int *)(result + 16) = (unsigned int)(a1);
    }
    if (a14 == 0) goto loc_008AF902;
    *(unsigned __int8 *)(result + 64) = 0;
    *(unsigned __int64 *)(result + 112) = a6;
    result = IopSetCopyInformationExtension(result, a14, 0 + 1, 1);
    if (!sign_flag) goto loc_008AF902;
    result = Feature_3741482297__private_IsEnabledDeviceUsageNoInline(result, a14, 0 + 1, 1);
    if ((unsigned int)(result) == 0) goto loc_008AF8C9;
    v_r12 = 0;
    *(unsigned __int64 *)(result + 24) = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m80 + 48)))) & (16)) == 0) goto loc_008AF8C9;
    result = (unsigned int)(*(unsigned int *)(v_stack_m80 + 48));
    if (*(unsigned __int64 *)(result + 8) != 0) {
        result = IopUnlockAndFreeMdl(*(unsigned __int64 *)(result + 8), a14, 0 + 1, 1);
        *(unsigned __int64 *)(result + 8) = 0;
    }
    if (a14 != 0) {
        a2 = 1;
        a1 = a6;
        result = IopFreeCopyObjectsFromDataBuffer(a1, a2, 0 + 1, 1);
    }
    if (result == 0) goto loc_008AF8FB;
    v_stack_mC8 = (unsigned __int8)(v_stack_m97);
    a4 = 0;
    result = IopExceptionCleanupEx(a1, result, v_stack_m78, a4);
    goto loc_008AF96C;
loc_008AF8FB:
    result = ObfDereferenceObject(a1, result, v_stack_m78, a4);
    goto loc_008AF96C;
loc_008AF902:
    *(unsigned int *)(v_r12 - 64) = (unsigned int)((unsigned int)(a7));
    *(unsigned int *)(v_r12 - 56) = (unsigned int)((unsigned int)(v_stack_m88));
    *(unsigned __int64 *)(v_r12 - 48) = v_stack_m90;
    if (*(unsigned __int64 *)(a1 + 208) == 0) goto loc_008AF940;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 208)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 208))))) & (16)) != 0) {
        result = v_stack_m78;
        result = *(unsigned int *)(result + 8);
        *(unsigned int *)(v_r12 - 52) = (unsigned int)(result);
    }
    result = 0;
    v_stack_mB8 = 0;
    v_stack_mC0 = (unsigned __int8)(v_stack_m97);
    v_stack_mC8 = (unsigned __int8)(v_stack_m98);
    result = IopSynchronousServiceTail(v_stack_m80, 0, a1, v_stack_m95);
loc_008AF96C:
    v_rsp = (v_rsp) + (176);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_008AF982:
    result = ExRaiseDatatypeMisalignment(v_stack_m80, 0, a1, v_stack_m95);
loc_008AF988:
    result = RtlRaiseStatus((unsigned int)(0xC000009AULL), 0, a1, v_stack_m95);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopReadFile(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, uint32_t Arg12, int64_t Arg13, int64_t Arg14)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint8_t v_stack_m95;
    uint8_t v_stack_m96;
    uint8_t v_stack_m97;
    uint8_t v_stack_m98;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (176);
    result = 0;
    v_stack_m70 = 0;
    v_stack_m94 = 0;
    local_r13 = 0;
    v_stack_m68 = 0;
    v_stack_m88 = 0;
    v_stack_m90 = 0;
    if (Arg10 == 0) goto loc_008AF077;
    if (Arg3 != 0) goto loc_008AF065;
    if (Arg2 != 0) goto loc_008AF065;
    if ((*(uint64_t *)(arg1 + 0xB0)) == 0) goto loc_008AF077;
loc_008AF065:
    goto loc_008AF8C9;
loc_008AF077:
    if (Arg13 == 0) goto loc_008AF0AC;
    if (*(uint64_t *)(Arg13) == 0) goto loc_008AF0AC;
    if ((*(uint32_t *)(*(uint64_t *)(Arg13) + 0x28)) >= ((uint32_t)((uint32_t)(Arg7)))) goto loc_008AF0B4;
    goto loc_008AF8C9;
loc_008AF0AC:
loc_008AF0B4:
    v_stack_m40 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m98 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (2)) == 0) goto loc_008AF0E5;
    if (!(sign_flag)) {
        local_r13 = 1;
    }
    v_stack_m97 = (uint8_t)(local_r13);
    result = (uint32_t)(((uint32_t)(Arg12)) & (0x40000000ULL));
    v_stack_m60 = (uint32_t)(result);
    result = IoGetRelatedDeviceObject(Arg1, Arg2, Arg3, Arg4);
    v_stack_m80 = result;
    if (v_stack_m98 == 0) goto loc_008AF226;
    if (Arg10 != 0) goto loc_008AF226;
    if (Arg5 >= ((uint32_t)(0xC000000DULL))) { Arg5 = (uint32_t)(0xC000000DULL); }
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(*(uint32_t *)(arg5)));
    result = IopMarkApcRoutineIfAsynchronousIo32(Arg5, v_stack_p18, (uint8_t)(local_r13), result);
    if (Arg14 != 0) goto loc_008AF17D;
    result = ProbeForWrite(Arg6, (uint32_t)((uint32_t)((uint32_t)(Arg7))), 1, result);
    goto loc_008AF185;
loc_008AF17D:
loc_008AF185:
    if ((*(uint64_t *)(arg1 + 0xB0)) == 0) goto loc_008AF1AF;
    if (((v_stack_p18) & (-2)) == 0) goto loc_008AF1AF;
    v_stack_m94 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_008AF8C9;
loc_008AF1AF:
    if (Arg8 == 0) goto loc_008AF1D5;
    if ((((uint8_t)(Arg8)) & (3)) != 0) goto loc_008AF982;
    result = (uint32_t)(v_stack_m94);
    if (Arg8 < ((uint32_t)(v_stack_m94))) { result = Arg8; }
    v_stack_m90 = *(uint64_t *)(Arg8);
loc_008AF1D5:
    result = Arg9;
    local_rbx = (uint32_t)(v_stack_m94);
    if (Arg9 != 0) {
        local_rbx = (uint32_t)(v_stack_m94);
        if (Arg9 < ((uint32_t)(v_stack_m94))) { local_rbx = Arg9; }
        result = *(uint32_t *)(local_rbx);
        v_stack_m88 = (uint32_t)(result);
    }
    goto loc_008AF24F;
loc_008AF226:
    if (Arg8 != 0) {
        result = *(uint64_t *)(Arg8);
        v_stack_m90 = result;
    }
    result = Arg9;
    if (Arg9 != 0) {
        result = *(uint32_t *)(Arg9);
        v_stack_m88 = (uint32_t)(result);
    }
    if ((uint8_t)(v_stack_m98) == 0) goto loc_008AF2D4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (8)) == 0) goto loc_008AF2CF;
    if ((uint16_t)(*(uint16_t *)(v_stack_m80 + 0x130)) == 0) goto loc_008AF27C;
    if ((((uint32_t)((uint32_t)(Arg7))) & ((uint32_t)(*(uint16_t *)(v_stack_m80 + 0x130) - 1))) != 0) goto loc_008AF28A;
loc_008AF27C:
    if (((Arg6) & ((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x98)))) == 0) goto loc_008AF2B2;
loc_008AF28A:
    if ((uint16_t)(*(uint16_t *)(v_stack_m80 + 0x130)) == 0) goto loc_008AF29A;
    Arg2 = 0;
    if (0 != 0) goto loc_008AF2A8;
loc_008AF29A:
    if (((Arg6) & ((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x98)))) == 0) goto loc_008AF2B2;
loc_008AF2A8:
    goto loc_008AF8C9;
loc_008AF2B2:
    if (Arg8 == 0) goto loc_008AF2CF;
    if ((uint16_t)(*(uint16_t *)(v_stack_m80 + 0x130)) == 0) goto loc_008AF2CF;
    if (((v_stack_m90) & ((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m80 + 0x130))) - 1))) == 0) goto loc_008AF2CF;
    goto loc_008AF8C9;
loc_008AF2CF:
loc_008AF2D4:
    if ((uint32_t)(0xC000000DULL) == 0) goto loc_008AF32A;
    Arg1 = 0;
    v_stack_m78 = 0;
    v_stack_mC0 = 0;
    v_stack_mC8 = v_stack_m78;
    result = ObReferenceObjectByHandle((uint32_t)(0xC000000DULL), 2, *(uint64_t *)(v_rip + 0x7178A0), (uint8_t)(v_stack_m98));
    v_stack_m68 = v_stack_m78;
    v_stack_m94 = (uint32_t)(result);
    if (sign_flag) goto loc_008AF8C9;
    result = KeResetEvent(v_stack_m78, 2, *(uint64_t *)(v_rip + 0x7178A0), (uint8_t)(v_stack_m98));
loc_008AF32A:
    v_stack_m48 = *(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x8) + 0x50);
    if ((uint8_t)(local_r13) == 0) goto loc_008AF5F8;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x50))) & (4));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 128, Arg2, Arg3, (uint8_t)(v_stack_m98));
    v_stack_m96 = 0;
    if (1 != 0) goto loc_008AF39C;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(0, Arg2, Arg3, result);
    Arg1 = 0;
    goto loc_008AF3BB;
loc_008AF39C:
    Arg3 = (0 != 0) ? 1 : 0;
    v_stack_mC8 = v_stack_m96;
    result = IopWaitAndAcquireFileObjectLock(0, v_stack_m98, Arg3, result);
loc_008AF3BB:
    v_stack_m94 = (uint32_t)((uint32_t)((uint32_t)(result)));
    if (v_stack_m96 == 0) goto loc_008AF3DC;
    if (v_stack_m78 == 0) goto loc_008AF8C9;
    result = ObfDereferenceObject(v_stack_m78, v_stack_m98, Arg3, result);
    goto loc_008AF8C9;
loc_008AF3DC:
    if (Arg8 == 0) goto loc_008AF3EF;
    if (v_stack_m90 != -2) goto loc_008AF3F8;
    if (v_stack_m8C == -1) {
        result = *(uint64_t *)(arg1 + 0x68);
        v_stack_m90 = result;
    }
    if ((*(uint64_t *)(arg1 + 0x30)) == 0) goto loc_008AF5C4;
    if (Arg14 != 0) goto loc_008AF5C4;
    v_stack_m58 = v_xmm0;
    result = (v_stack_m90) >> (32);
    if (!sign_flag) goto loc_008AF456;
    if (v_stack_m78 != 0) {
        Arg1 = v_stack_m78;
        result = ObfDereferenceObject(Arg1, v_stack_m98, Arg3, result);
    }
    result = IopReleaseFileObjectLock(Arg1, v_stack_m98, Arg3, result);
    goto loc_008AF8C9;
loc_008AF456:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6555C4)))) & (16)) == 0) goto loc_008AF47F;
    result = MmIsDriverVerifying(*(uint64_t *)(v_stack_m80 + 0x8), v_stack_m98, Arg3, result);
    if ((uint32_t)(result) == 0) goto loc_008AF47F;
    result = VfFastIoSnapState(*(uint64_t *)(v_stack_m80 + 0x8), v_stack_m98, Arg3, result);
    goto loc_008AF481;
loc_008AF47F:
    result = 0;
loc_008AF481:
    v_stack_mB0 = v_stack_m80;
    v_stack_mB8 = v_stack_m58;
    v_stack_mC0 = Arg6;
    v_stack_mC8 = (uint32_t)((uint32_t)(v_stack_m88));
    result = guard_dispatch_icall(Arg1, v_stack_m90, (uint32_t)(Arg7), 1);
    if (0 != 0) {
        Arg2 = *(uint64_t *)(v_stack_m48 + 0x10);
        Arg1 = 0;
        result = VfFastIoCheckState(Arg1, Arg2, (uint32_t)(Arg7), 1);
    }
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_008AF5BE;
    if ((uint32_t)((uint32_t)(v_stack_m58)) == 0) goto loc_008AF4F8;
    if (((uint32_t)((uint32_t)(v_stack_m58))) == 0x80000005ULL) goto loc_008AF4F8;
    if (((uint32_t)((uint32_t)(v_stack_m58))) != 0xC0000011ULL) goto loc_008AF5BE;
loc_008AF4F8:
    *(uint64_t *)(arg5) = v_xmm0;
    goto loc_008AF581;
loc_008AF581:
    if (v_stack_p10 == 0) goto loc_008AF5AA;
    result = Arg5;
    if (((*(uint32_t *)(arg1 + 0x50)) & (0x8000000ULL)) == 0) {
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_m78;
        result = KeSetEvent(Arg1, Arg2, Arg3, 1);
    }
    result = ObfDereferenceObject(v_stack_m78, Arg2, Arg3, 1);
loc_008AF5AA:
    result = IopReleaseFileObjectLock(Arg1, Arg2, Arg3, 1);
    goto loc_008AF8C9;
loc_008AF5BE:
loc_008AF5C4:
loc_008AF5C9:
    if (v_stack_m8C >= 0) goto loc_008AF621;
    if (v_stack_m78 != 0) {
        Arg1 = v_stack_m78;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, 1);
    }
    if ((uint8_t)(v_stack_m97) == 0) goto loc_008AF2A8;
    result = IopReleaseFileObjectLock(Arg1, Arg2, Arg3, 1);
    goto loc_008AF8C9;
loc_008AF5F8:
    if (*(uint64_t *)(v_stack_m48 + 0x10) != 0) goto loc_008AF5C9;
    if (((*(uint32_t *)(arg1 + 0x50)) & (640)) != 0) goto loc_008AF5C9;
    if (v_stack_m78 == 0) goto loc_008AF2A8;
    result = ObfDereferenceObject(v_stack_m78, Arg2, Arg3, 1);
    goto loc_008AF8C9;
loc_008AF621:
    if (Arg10 == 0) {
        Arg1 = Arg1;
        result = IopResetEvent(Arg1, Arg2, Arg3, 1);
    }
    Arg3 = (uint8_t)(((uint8_t)(v_stack_m97)) ^ (1));
    result = IopAllocateIrpExReturn((uint32_t)(0xC000000DULL), *(uint8_t *)((uint32_t)(0xC000000DULL) + 0x4C), Arg3, 1);
    v_stack_m70 = result;
    if (result != 0) goto loc_008AF67B;
    if (v_stack_m78 != 0) {
        Arg1 = v_stack_m78;
        result = ObfDereferenceObject(Arg1, *(uint8_t *)((uint32_t)(0xC000000DULL) + 0x4C), Arg3, 1);
    }
    if ((uint8_t)(v_stack_m97) != 0) {
        Arg1 = Arg1;
        result = IopReleaseFileObjectLock(Arg1, *(uint8_t *)((uint32_t)(0xC000000DULL) + 0x4C), Arg3, 1);
    }
    goto loc_008AF8C9;
loc_008AF67B:
    *(void **)(result + 0xC0) = Arg1;
    *(uint64_t *)(result + 0x98) = v_stack_m40;
    Arg2 = 0;
    *(uint64_t *)(result + 0xA0) = 0;
    *(uint8_t *)(result + 0x40) = (uint8_t)(v_stack_m98);
    *(uint8_t *)(result + 0x41) = 0;
    *(uint8_t *)(result + 0x44) = 0;
    *(uint64_t *)(result + 0x68) = 0;
    *(uint32_t *)(result + 0x10) = 0;
    *(uint64_t *)(result + 0x50) = v_stack_m78;
    if (Arg10 == 0) goto loc_008AF6F1;
    result = ObfReferenceObjectWithTag(Arg10, (uint32_t)(0x49526F49ULL), Arg3, 1);
    *(uint64_t *)(result + 0x48) = Arg11;
    v_stack_p20 = Arg10;
    v_stack_m78 = Arg5;
    Arg2 = 0;
    goto loc_008AF70E;
loc_008AF6F1:
    v_stack_m78 = Arg5;
    *(void **)(result + 0x48) = Arg5;
    *(uint64_t *)(result + 0x58) = v_stack_p18;
loc_008AF70E:
    *(uint64_t *)(result + 0x60) = v_stack_p20;
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 3;
    *(void **)(*(uint64_t *)(result + 0xB8) - 0x18) = Arg1;
    *(uint64_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)(0xC000009AULL) + 0x30)))) & (4)) == 0) goto loc_008AF7A1;
    if ((uint32_t)((uint32_t)(Arg7)) == 0) goto loc_008AF798;
    if (Arg14 == 0) goto loc_008AF765;
    *(uint64_t *)(result + 0x18) = Arg6;
    *(uint64_t *)(result + 0x70) = Arg6;
    goto loc_008AF850;
loc_008AF765:
    result = ExAllocatePool2(73, (uint32_t)(Arg7), (uint32_t)(0x42536F49ULL), 1);
    *(uint64_t *)(result + 0x18) = result;
    if (result != 0) goto loc_008AF78B;
    goto loc_008AF8C9;
loc_008AF78B:
    *(uint64_t *)(result + 0x70) = Arg6;
    goto loc_008AF850;
loc_008AF798:
    goto loc_008AF850;
loc_008AF7A1:
    if ((((uint8_t)(result)) & (16)) == 0) goto loc_008AF820;
    if ((uint32_t)((uint32_t)(Arg7)) == 0) goto loc_008AF850;
    v_stack_mC8 = result;
    Arg3 = 0;
    result = IoAllocateMdl(Arg6, (uint32_t)((uint32_t)((uint32_t)(Arg7))), Arg3, 1);
    if (result == 0) goto loc_008AF988;
    Arg2 = v_stack_m98;
    if (Arg14 != 0) { Arg2 = 0; }
    result = MmProbeAndLockPages(result, Arg2, 0 + 1, 1);
    goto loc_008AF850;
loc_008AF820:
    *(uint64_t *)(result + 0x70) = Arg6;
    if (Arg13 == 0) goto loc_008AF850;
    if (*(uint64_t *)(Arg13) == 0) goto loc_008AF850;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(Arg13);
    *(uint64_t *)(Arg13) = Arg2;
    if (Arg10 != 0) {
    }
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (8)) != 0) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x10))) | (1));
        *(uint32_t *)(result + 0x10) = (uint32_t)(Arg1);
    }
    if (v_stack_m60 == 0) {
        *(uint32_t *)(result + 0x10) = (uint32_t)(Arg1);
    }
    if (Arg14 == 0) goto loc_008AF902;
    *(uint8_t *)(result + 0x40) = 0;
    *(uint64_t *)(result + 0x70) = Arg6;
    result = IopSetCopyInformationExtension(result, Arg14, 0 + 1, 1);
    if (!sign_flag) goto loc_008AF902;
    result = Feature_3741482297__private_IsEnabledDeviceUsageNoInline(result, Arg14, 0 + 1, 1);
    if ((uint32_t)(result) == 0) goto loc_008AF8C9;
    local_r12 = 0;
    *(uint64_t *)(result + 0x18) = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x30)))) & (16)) == 0) goto loc_008AF8C9;
    result = (uint32_t)(*(uint32_t *)(v_stack_m80 + 0x30));
    if (*(uint64_t *)(result + 0x8) != 0) {
        result = IopUnlockAndFreeMdl(*(uint64_t *)(result + 0x8), Arg14, 0 + 1, 1);
        *(uint64_t *)(result + 0x8) = 0;
    }
    if (Arg14 != 0) {
        Arg2 = 1;
        Arg1 = Arg6;
        result = IopFreeCopyObjectsFromDataBuffer(Arg1, Arg2, 0 + 1, 1);
    }
    if (result == 0) goto loc_008AF8FB;
    v_stack_mC8 = (uint8_t)(v_stack_m97);
    Arg4 = 0;
    result = IopExceptionCleanupEx(Arg1, result, v_stack_m78, Arg4);
    goto loc_008AF96C;
loc_008AF8FB:
    result = ObfDereferenceObject(Arg1, result, v_stack_m78, Arg4);
    goto loc_008AF96C;
loc_008AF902:
    *(uint32_t *)(local_r12 - 0x40) = (uint32_t)((uint32_t)(Arg7));
    *(uint32_t *)(local_r12 - 0x38) = (uint32_t)((uint32_t)(v_stack_m88));
    *(uint64_t *)(local_r12 - 0x30) = v_stack_m90;
    if (*(uint64_t *)(arg1 + 0xD0) == 0) goto loc_008AF940;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xD0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xD0))))) & (16)) != 0) {
        result = v_stack_m78;
        result = *(uint32_t *)(result + 0x8);
        *(uint32_t *)(local_r12 - 0x34) = (uint32_t)(result);
    }
    result = 0;
    v_stack_mB8 = 0;
    v_stack_mC0 = (uint8_t)(v_stack_m97);
    v_stack_mC8 = (uint8_t)(v_stack_m98);
    result = IopSynchronousServiceTail(v_stack_m80, 0, Arg1, v_stack_m95);
loc_008AF96C:
    local_rsp = (local_rsp) + (176);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_008AF982:
    result = ExRaiseDatatypeMisalignment(v_stack_m80, 0, Arg1, v_stack_m95);
loc_008AF988:
    result = RtlRaiseStatus((uint32_t)(0xC000009AULL), 0, Arg1, v_stack_m95);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x74` | `32` | `R/W` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `R` |
| `Arg5` | `+ 0x0` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008AEFF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
